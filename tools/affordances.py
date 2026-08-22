# -*- coding: utf-8 -*-
"""Inventory every navigational affordance on every screen of the approved run."""
import re, io, json, html, collections

h = io.open('run.html', encoding='utf-8').read()
body = h[h.index('<div class="doc">'):]


def balanced(s, start):
    i, depth = start, 0
    tag = re.compile(r'</?div\b', re.I)
    while True:
        m = tag.search(s, i)
        if not m:
            raise ValueError('unbalanced')
        if m.group(0).lower() == '<div':
            depth += 1
        else:
            depth -= 1
        i = s.index('>', m.end()) + 1
        if depth == 0:
            return s[start:i], i


def text(frag):
    t = re.sub(r'<svg\b.*?</svg>', ' ', frag, flags=re.S | re.I)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t)
    return re.sub(r'\s+', ' ', t).strip()


# --- split into screens -------------------------------------------------------
screens = []
for m in re.finditer(r'<div class="(plate|fx-item--desk)">', body):
    blk, _ = balanced(body, m.start())
    cap = re.search(r'<h4><b>#(\d+)</b>\s*(.*?)</h4>', blk, re.S)
    num, name = int(cap.group(1)), text(cap.group(2))
    ci = blk.rfind('<div class="run-cap')
    frame = blk[blk.index('>') + 1:ci]
    prov = 'complete-171' if 'prov--complete' in blk else 'approved-171'
    screens.append(dict(num=num, name=name, frame=frame, prov=prov,
                        kind='desk' if m.group(1).endswith('desk') else 'phone'))
screens.sort(key=lambda s: s['num'])
assert len(screens) == 171, len(screens)

# --- classify affordances -----------------------------------------------------
# Buttons whose class implies an in-place control rather than a destination.
INPLACE = ('chip', 'fchip', 'tab ', 'tab"', 'stepper', 'reveal', 'seg__i',
           'kbd', 'pill', 'toggle', 'sw__', 'dot')

rows = []
for s in screens:
    seen = collections.Counter()

    def add(kind, label, cls=''):
        label = label.strip()
        if not label or len(label) > 90:
            return
        key = (kind, label.lower())
        seen[key] += 1
        if seen[key] > 1:
            return
        rows.append(dict(num=s['num'], screen=s['name'], track=s['name'],
                         kind=kind, label=label, cls=cls, prov=s['prov']))

    f = s['frame']
    # explicit links
    for m in re.finditer(r'<a\b([^>]*)>(.*?)</a>', f, re.S):
        add('link', text(m.group(2)), m.group(1))
    # buttons
    for m in re.finditer(r'<button\b([^>]*)>(.*?)</button>', f, re.S):
        attrs, inner = m.group(1), m.group(2)
        cls = (re.search(r'class="([^"]*)"', attrs) or [None, ''])[1] if 'class="' in attrs else ''
        lbl = text(inner) or (re.search(r'aria-label="([^"]*)"', attrs).group(1)
                              if 'aria-label="' in attrs else '')
        if any(k in cls for k in INPLACE):
            k = 'control'
        elif 'tabbar__i' in cls:
            k = 'tabbar'
        elif 'rail__i' in cls:
            k = 'rail'
        elif 'listitem' in cls:
            k = 'listitem'
        elif 'appbar__btn' in cls:
            k = 'appbar'
        elif 'fab' in cls:
            k = 'fab'
        elif 'btn' in cls or 'dbtn' in cls:
            k = 'cta'
        else:
            k = 'other'
        add(k, lbl, cls)

json.dump(dict(screens=[{k: v for k, v in s.items() if k != 'frame'} for s in screens],
               rows=rows), io.open('affordances.json', 'w', encoding='utf-8'))

print('screens:', len(screens))
c = collections.Counter(r['kind'] for r in rows)
for k, v in c.most_common():
    print('  %-9s %d' % (k, v))
print('total affordances (deduped per screen):', len(rows))
