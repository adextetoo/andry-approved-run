# -*- coding: utf-8 -*-
import re, html, json, io, sys

def balanced(h, start):
    """Return (block, end_index) for the div opening at `start`."""
    assert h.startswith('<div', start), h[start:start+40]
    i = start; depth = 0
    tag = re.compile(r'</?div\b', re.I)
    while True:
        m = tag.search(h, i)
        if not m: raise ValueError('unbalanced at %d' % start)
        if m.group(0).lower() == '<div':
            depth += 1
            i = h.index('>', m.end()) + 1
        else:
            depth -= 1
            i = h.index('>', m.end()) + 1
            if depth == 0:
                return h[start:i], i

def norm(s):
    s = html.unescape(re.sub('<[^>]+>', '', s))
    s = s.split('\u00b7')[-1]
    return re.sub(r'[^a-z0-9]+', '', s.lower())

A = io.open('artifact-bcb571a9-1787418264-6488.html', encoding='utf-8').read()
B = io.open('artifact-de881528-1787405719-3b32.html', encoding='utf-8').read()

# ---------- parse B ----------
brecs = []
for m in re.finditer(r'<div class="(plate|fx-item--desk)"[^>]*>', B):
    blk, _ = balanced(B, m.start())
    cap = re.search(r'<div class="plate__cap"[^>]*>(.*)</div>\s*$', blk, re.S)
    capin = cap.group(1) if cap else ''
    h4 = re.search(r'<h4>#(\d+)\s*&middot;\s*(.*?)</h4>', capin, re.S)
    if not h4:
        continue
    p = re.search(r'<p>(.*?)</p>', capin, re.S)
    tags = re.search(r'<div class="plate__tags">(.*?)</div>', capin, re.S)
    tagsin = tags.group(1) if tags else ''
    frame = blk[:cap.start(1) - len('<div class="plate__cap">')] if cap else blk
    # frame = everything before the caption div
    ci = blk.rfind('<div class="plate__cap"')
    frame = blk[blk.index('>', blk.index('<div'))+1:ci]
    brecs.append(dict(
        num=int(h4.group(1)), name=h4.group(2).strip(),
        desc=(p.group(1).strip() if p else ''),
        kind=('desk' if m.group(1) == 'fx-item--desk' else 'phone'),
        status=('appr' if 'fix--appr' in tagsin else 'ret'),
        extra=[t for t in re.findall(r'<span class="fix[^"]*"[^>]*>(.*?)</span>', tagsin)
               if 'Approved in review' not in t and 'Carried over' not in t],
        frame=frame.strip()))

# ---------- parse A ----------
arecs = []
for m in re.finditer(r'<div class="fx-item(?: fx-item--desk)?"[^>]*>', A):
    blk, _ = balanced(A, m.start())
    nm = re.search(r'<div class="fx-name">(.*?)</div>', blk, re.S)
    if not nm: continue
    tags = re.search(r'<div class="plate__tags"[^>]*>(.*?)</div>', blk, re.S)
    tagsin = tags.group(1) if tags else ''
    # frame = markup after the tags div (or after the name div)
    cut = blk.index('</div>', blk.index('<div class="plate__tags"')) + 6 if tags else nm.end()
    frame = blk[cut:blk.rfind('</div>')]
    arecs.append(dict(
        name=nm.group(1).strip(),
        kind=('desk' if 'fx-item--desk' in m.group(0) else 'phone'),
        status=('appr' if 'Approved in review' in tagsin else 'other'),
        label=re.sub(r'<[^>]+>', '', tagsin).strip(),
        frame=frame.strip()))

print('B records:', len(brecs), 'appr:', sum(1 for r in brecs if r['status']=='appr'))
print('A records:', len(arecs), 'appr:', sum(1 for r in arecs if r['status']=='appr'))

bynorm = {}
for r in brecs: bynorm.setdefault(norm(r['name']), []).append(r)
unmatched = []
for r in arecs:
    k = norm(r['name'])
    if k in bynorm and len(bynorm[k]) == 1:
        r['num'] = bynorm[k][0]['num']
        r['bdesc'] = bynorm[k][0]['desc']
    else:
        r['num'] = None
        unmatched.append((r['name'], len(bynorm.get(k, []))))
print('A unmatched/ambiguous:', len(unmatched))
for u in unmatched[:20]: print('   ', u)
json.dump(dict(b=brecs, a=arecs), io.open('parsed.json','w',encoding='utf-8'))
