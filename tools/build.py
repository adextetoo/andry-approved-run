# -*- coding: utf-8 -*-
import re, io, json

A = io.open('artifact-bcb571a9-1787418264-6488.html', encoding='utf-8').read()
B = io.open('artifact-de881528-1787405719-3b32.html', encoding='utf-8').read()
d = json.load(io.open('parsed.json', encoding='utf-8'))
sec = json.load(io.open('sections.json', encoding='utf-8'))
arecs, brecs = d['a'], d['b']
smap = {int(k): v for k, v in sec['map'].items()}

# --- assets lifted from the source artifacts -------------------------------
sprite = re.search(r'(<svg width="0" height="0".*?</svg>)', B, re.S).group(1)
css = re.findall(r'<style>(.*?)</style>', B, re.S)[1]

# Two defects in the inherited stylesheet, corrected here rather than in any
# plate: the console frame rule was unreachable, and the KYC stepper labels
# were typeset as a 2px connector line. See stylesheet_repairs.py.
import stylesheet_repairs
css = stylesheet_repairs.repair(css)

# --- assemble the 171 records ----------------------------------------------
screens = []
for i in range(171):
    a, b = arecs[i], brecs[i]
    from_a = a['status'] == 'appr'
    rec = dict(
        num=b['num'], name=b['name'], desc=b['desc'], kind=b['kind'],
        src='complete' if from_a else 'track',
        # B's "171-build: ..." reference chips are dropped: the provenance chip added
        # below states which review's tag the plate carries, and the two disagree - see
        # the note in the masthead. Design notes (New, Reworked, audit refs) are kept.
        extra=[x for x in b['extra'] if not x.startswith('171-build')],
        frame=(a['frame'] if from_a else b['frame']))
    rec.update(smap[b['num']])
    screens.append(rec)

assert len(screens) == 171
assert sum(1 for s in screens if s['src'] == 'complete') == 66
assert sum(1 for s in screens if s['src'] == 'track') == 105

TRACKDEK = {
 'A': 'The person who buys units and carries the risk.',
 'B': 'The named supervisor who stands behind each animal.',
 'C': 'The ranch that houses the herd and files the record.',
 'D': 'Named case-workers with hardware keys, working queues against published SLAs.'}

CHROME = """
/* ==========================================================================
   THE APPROVED RUN - document chrome.
   Additive only: every rule below is namespaced to a class the Andry system
   does not define, so the 171 plates render exactly as they do at source.
   ========================================================================== */

/* the run is 171 plates wide, so the page opens out past the source width;
   the reading column inside the masthead stays where prose wants it. */
.doc{max-width:1720px;}
.run-mast > *{max-width:1240px;}

.run-mast{padding:76px 0 44px;border-bottom:2px solid var(--ink);}
.run-mast h1{margin:18px 0 0;font-size:clamp(38px,6.2vw,68px);line-height:.98;
  letter-spacing:-.035em;font-weight:800;text-wrap:balance;max-width:16ch;}
.run-mast h1 em{display:block;font-style:normal;color:var(--brand);}
.run-dek{margin:26px 0 0;max-width:62ch;font-size:18px;line-height:1.5;color:var(--ink-2);}
.run-dek + .run-dek{margin-top:14px;font-size:16px;color:var(--muted);}
.run-dek em{font-style:italic;color:var(--ink);}

.ledger{margin:40px 0 0;border:1px solid var(--line);border-radius:var(--radius-lg);
  overflow:hidden;background:var(--surface);}
/* colour stated on the table itself: a table does not inherit colour in quirks mode */
.ledger table{width:100%;border-collapse:collapse;font-size:14px;color:var(--ink);}
.ledger th,.ledger td{padding:13px 16px;text-align:left;border-bottom:1px solid var(--line);}
.ledger thead th{background:var(--surface-2);font-size:11px;font-weight:700;
  letter-spacing:.13em;text-transform:uppercase;color:var(--muted);}
.ledger tbody tr:last-child td{border-bottom:0;}
.ledger tfoot td{background:var(--surface-2);font-weight:750;
  border-top:1px solid var(--line-2);border-bottom:0;}
.ledger .n{text-align:right;font-family:var(--num);font-variant-numeric:tabular-nums;font-weight:650;}
.ledger th.n{text-align:right;}
.ledger .who{font-weight:700;color:var(--ink);}
.ledger .who span{display:block;font-weight:450;font-size:12.5px;color:var(--muted);margin-top:2px;}
.ledger-scroll{overflow-x:auto;}

.prov{display:inline-flex;align-items:center;gap:6px;font-family:var(--num);font-size:11px;
  font-weight:650;letter-spacing:.02em;padding:3px 9px;border-radius:var(--radius-sm);
  white-space:nowrap;background:var(--surface-3);color:var(--ink-2);font-style:normal;}
.prov::before{content:"";width:5px;height:5px;border-radius:1px;background:currentColor;}
.prov--complete{background:var(--gold-soft);color:var(--gold-ink);}
.prov--track{background:var(--brand-soft);color:var(--brand);}

.run-legend{display:flex;flex-wrap:wrap;gap:12px 26px;margin-top:26px;
  font-size:13px;color:var(--muted);align-items:center;}
.run-legend span{display:inline-flex;align-items:center;gap:8px;}

.run-grid{display:grid;grid-template-columns:repeat(auto-fill,402px);
  gap:44px 34px;justify-content:start;padding:8px 0 12px;}
.run-deskgrid{overflow-x:auto;padding:8px 0 20px;}
.run-deskgrid .fx-item--desk{margin:0 0 48px;}

.run-cap{margin-top:16px;max-width:402px;display:flex;flex-direction:column;gap:8px;}
.run-cap--wide{max-width:1000px;}
.run-cap h4{margin:0;font-size:15px;font-weight:700;letter-spacing:-.01em;
  display:flex;gap:9px;align-items:baseline;}
.run-cap h4 b{font-family:var(--num);font-size:12.5px;font-weight:650;color:var(--faint);flex:none;}
.run-cap p{margin:0;font-size:13.5px;line-height:1.5;color:var(--muted);}
.run-cap .plate__tags{margin-top:1px;}

.run-nav{position:sticky;top:0;z-index:40;background:var(--page);
  border-bottom:1px solid var(--line);}
.run-nav ol{display:flex;gap:6px;list-style:none;margin:0;padding:11px 0;overflow-x:auto;}
.run-nav a{display:inline-flex;align-items:center;gap:8px;text-decoration:none;white-space:nowrap;
  padding:7px 14px;border-radius:var(--radius-pill);border:1px solid var(--line);
  background:var(--surface);color:var(--ink-2);font-size:13px;font-weight:650;}
.run-nav a:hover{border-color:var(--brand);color:var(--brand);}
.run-nav a b{font-family:var(--num);font-size:11px;color:var(--faint);font-weight:650;}

.stage-run{padding:44px 0 8px;scroll-margin-top:70px;}
.track-open{scroll-margin-top:70px;}

/* Below two plates' worth of room the grid becomes a shelf rather than
   shrinking the frames: a 402 x 874 mock is only honest at 402 x 874. */
@media (max-width:940px){
  .run-grid{display:flex;overflow-x:auto;gap:28px;padding-bottom:26px;
    scroll-snap-type:x proximity;-webkit-overflow-scrolling:touch;}
  .run-grid > .plate{scroll-snap-align:start;}
  .run-mast{padding:56px 0 36px;}
}
"""

out = io.StringIO()
w = out.write

w('<title>Andry &mdash; the approved run</title>\n')
w(sprite)
w('\n<style>\n' + css + '\n' + CHROME + '\n')
w('</style>\n\n')

w('<div class="doc">\n')

# ---------------- masthead ----------------
w('<header class="run-mast">\n')
w('  <p class="eyebrow">Andry &middot; screens carrying an approval</p>\n')
w('  <h1>The approved run<em>171 plates, two reviews</em></h1>\n')
w('  <p class="run-dek">Both source artifacts were read for screens tagged <strong>Approved in\n')
w('    review</strong>, and only those screens were kept. <em>The complete product, 171 screens</em>\n')
w('    contributed 66. <em>The approved 171</em> contributed 105. Every plate below carries an\n')
w('    approval; nothing untagged was brought across.</p>\n')
w('  <p class="run-dek">The two approved sets turn out to be exactly complementary &mdash; they do\n')
w('    not share a single screen, and between them they cover the run end to end. What the older\n')
w('    build approved, the newer one had marked <em>carried over</em>; what the newer one approved,\n')
w('    the older one had not yet signed off. So the merged set is the whole product, 171 of 171,\n')
w('    with each plate lifted from the artifact that approved it and its origin kept in the\n')
w('    caption.</p>\n')
w('  <p class="run-dek">One discrepancy is worth recording. <em>The approved 171</em> also carries\n')
w('    small <span class="mono">171-build:</span> chips reporting what the older build had said\n')
w('    about a screen, and on 63 plates those chips read <em>approved</em> even though the older\n')
w('    build never tagged them. This page follows the tags, which is what was asked for, so those\n')
w('    reference chips have been dropped rather than left to contradict the provenance chip beside\n')
w('    them. Design notes from the source captions &mdash; <em>New</em>, <em>Reworked</em>, audit\n')
w('    references &mdash; are kept as they were.</p>\n')

tot_c = sum(1 for s in screens if s['src'] == 'complete')
tot_t = 171 - tot_c
w('  <div class="ledger"><div class="ledger-scroll"><table>\n')
w('    <thead><tr><th>Track</th><th class="n">Screens</th>'
  '<th class="n">complete-171</th><th class="n">approved-171</th><th>Surface</th></tr></thead>\n')
w('    <tbody>\n')
for t in sec['tracks']:
    ts = [s for s in screens if s['track'] == t['id']]
    c = sum(1 for s in ts if s['src'] == 'complete')
    surface = '1440 &times; 900' if t['id'] == 'D' else '402 &times; 874'
    w('      <tr><td class="who">%s<span>%s</span></td><td class="n">%d</td>'
      '<td class="n">%d</td><td class="n">%d</td><td class="mono">%s</td></tr>\n'
      % (t['title'], TRACKDEK[t['id']], len(ts), c, len(ts) - c, surface))
w('    </tbody>\n')
w('    <tfoot><tr><td>All four tracks</td><td class="n">171</td><td class="n">%d</td>'
  '<td class="n">%d</td><td class="mono">38 stages</td></tr></tfoot>\n' % (tot_c, tot_t))
w('  </table></div></div>\n')

w('  <div class="run-legend">\n')
w('    <span><i class="fix fix--appr"><b>&#10003;</b> Approved in review</i> carried by all 171</span>\n')
w('    <span><i class="prov prov--complete">complete-171</i> approved in <em>the complete product,'
  ' 171 screens</em> &mdash; %d</span>\n' % tot_c)
w('    <span><i class="prov prov--track">approved-171</i> approved in <em>the approved 171</em>'
  ' &mdash; %d</span>\n' % tot_t)
w('  </div>\n</header>\n\n')

# ---------------- sticky nav ----------------
w('<nav class="run-nav" aria-label="Tracks"><ol>\n')
for t in sec['tracks']:
    ts = [s for s in screens if s['track'] == t['id']]
    w('  <li><a href="#track-%s">%s <b>%d</b></a></li>\n' % (t['id'], t['title'], len(ts)))
w('</ol></nav>\n\n')

# ---------------- the run ----------------
for t in sec['tracks']:
    ts = [s for s in screens if s['track'] == t['id']]
    c = sum(1 for s in ts if s['src'] == 'complete')
    stage_ids = [st for st in sec['stages'] if st['track'] == t['id']]
    w('<div class="trackbar track-open" id="track-%s"><b>%s</b><span>%d screens &middot; '
      '%d stages &middot; %d from complete-171 &middot; %d from approved-171</span></div>\n'
      % (t['id'], t['title'], len(ts), len(stage_ids), c, len(ts) - c))
    w('<p class="trackdek">%s</p>\n\n' % TRACKDEK[t['id']])

    for st in stage_ids:
        ss = [s for s in screens if s['stage'] == st['id']]
        if not ss:
            continue
        c2 = sum(1 for s in ss if s['src'] == 'complete')
        w('<section class="sec stage-run" id="%s">\n' % st['id'])
        w('  <div class="stagehead"><span class="code">%s</span>\n    <h2>%s</h2>\n'
          % (st['code'], st['title']))
        w('    <span class="meta">#%d to #%d &middot; %d screens &middot; <b>%d</b> complete-171 '
          '&middot; <b>%d</b> approved-171</span></div>\n'
          % (ss[0]['num'], ss[-1]['num'], len(ss), c2, len(ss) - c2))

        desk = ss[0]['kind'] == 'desk'
        w('  <div class="%s">\n' % ('run-deskgrid' if desk else 'run-grid'))
        for s in ss:
            wrap = 'fx-item--desk' if desk else 'plate'
            capcls = 'run-cap run-cap--wide' if desk else 'run-cap'
            w('<div class="%s">%s<div class="%s"><h4><b>#%d</b> %s</h4>'
              % (wrap, s['frame'], capcls, s['num'], s['name']))
            if s['desc']:
                w('<p>%s</p>' % s['desc'])
            w('<div class="plate__tags">'
              '<span class="fix fix--appr"><b>&#10003;</b> Approved in review</span>'
              '<span class="prov prov--%s">%s</span>'
              % (s['src'], 'complete-171' if s['src'] == 'complete' else 'approved-171'))
            for x in s['extra']:
                w('<span class="fix">%s</span>' % x)
            w('</div></div></div>\n')
        w('  </div>\n</section>\n\n')

w('</div>\n')

doc = out.getvalue()

# The published page inherits <meta charset=utf8> from the artifact shell, but the
# markup should not depend on that: escape every non-ASCII character in the title and
# body to a numeric reference. The stylesheet is left alone - character references are
# not decoded inside CSS, and its only non-ASCII characters sit in comments.
cut = doc.index('</style>')
head, css_part, tail = doc[:doc.index('<style>')], doc[doc.index('<style>'):cut], doc[cut:]
def ascii_only(s):
    return ''.join(c if ord(c) < 128 else '&#%d;' % ord(c) for c in s)
doc = ascii_only(head) + css_part + ascii_only(tail)

io.open('approved-run.html', 'w', encoding='utf-8').write(doc)
print('bytes:', len(doc.encode('utf-8')))
print('plates emitted:', doc.count('class="run-cap'))
print('appr chips:', doc.count('fix--appr'))
print('complete chips:', doc.count('prov--complete">complete-171'))
print('track chips:', doc.count('prov--track">approved-171'))
