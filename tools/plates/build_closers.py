# -*- coding: utf-8 -*-
"""Assemble the 13 flow-blocker plates into a document on the Andry stylesheet."""
import re, io
import plates_a, plates_b

run = io.open('run.html', encoding='utf-8').read()
sprite = re.search(r'(<svg width="0" height="0".*?</svg>)', run, re.S).group(1)
css = re.findall(r'<style>(.*?)</style>', run, re.S)[0]

PLATES = plates_a.PLATES + plates_b.PLATES
assert len(PLATES) == 13, len(PLATES)
assert [p['id'] for p in PLATES] == ['C-%02d' % i for i in range(1, 14)]

CHROME = """
/* ==========================================================================
   THE THIRTEEN — document chrome. Additive: every rule is namespaced to a
   class the Andry system does not define, so the plates render as the
   approved 171 do.
   ========================================================================== */
.doc{max-width:1720px;}
.new-mast > *{max-width:1240px;}

.new-mast{padding:76px 0 44px;border-bottom:2px solid var(--ink);}
.new-mast h1{margin:18px 0 0;font-size:clamp(38px,6vw,66px);line-height:.98;
  letter-spacing:-.035em;font-weight:800;text-wrap:balance;max-width:17ch;}
.new-mast h1 em{display:block;font-style:normal;color:var(--brand);}
.new-dek{margin:26px 0 0;max-width:63ch;font-size:18px;line-height:1.5;color:var(--ink-2);}
.new-dek + .new-dek{margin-top:14px;font-size:16px;color:var(--muted);}
.new-dek strong{color:var(--ink);font-weight:650;}
.new-dek em{font-style:italic;color:var(--ink);}

.rules{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px;margin-top:38px;}
.rule{border:1px solid var(--line);border-radius:var(--radius-lg);background:var(--surface);
  padding:18px 20px;}
.rule b{display:block;font-size:14px;font-weight:730;letter-spacing:-.01em;margin-bottom:6px;}
.rule span{display:block;font-size:13px;line-height:1.5;color:var(--muted);}

.new-grid{display:grid;grid-template-columns:repeat(auto-fill,402px);
  gap:44px 34px;justify-content:start;padding:8px 0 12px;}
.new-cap{margin-top:16px;max-width:402px;display:flex;flex-direction:column;gap:8px;}
.new-cap h4{margin:0;font-size:15px;font-weight:700;letter-spacing:-.01em;
  display:flex;gap:9px;align-items:baseline;}
.new-cap h4 b{font-family:var(--num);font-size:12.5px;font-weight:650;color:var(--brand);flex:none;}
.new-cap p{margin:0;font-size:13.5px;line-height:1.55;color:var(--muted);}
.new-cap q{font-style:normal;color:var(--ink-2);font-weight:600;}
.new-cap q::before{content:"\\201C";} .new-cap q::after{content:"\\201D";}
.new-cap .plate__tags{margin-top:1px;}
.fix--closes{background:var(--brand-soft);color:var(--brand);}

.stage-new{padding:44px 0 8px;scroll-margin-top:70px;}
.new-nav{position:sticky;top:0;z-index:40;background:var(--page);border-bottom:1px solid var(--line);}
.new-nav ol{display:flex;gap:6px;list-style:none;margin:0;padding:11px 0;overflow-x:auto;}
.new-nav a{display:inline-flex;align-items:center;gap:8px;text-decoration:none;white-space:nowrap;
  padding:7px 14px;border-radius:var(--radius-pill);border:1px solid var(--line);
  background:var(--surface);color:var(--ink-2);font-size:13px;font-weight:650;}
.new-nav a:hover{border-color:var(--brand);color:var(--brand);}
.new-nav a b{font-family:var(--num);font-size:11px;color:var(--faint);font-weight:650;}

@media (max-width:940px){
  .new-grid{display:flex;overflow-x:auto;gap:28px;padding-bottom:26px;
    scroll-snap-type:x proximity;-webkit-overflow-scrolling:touch;}
  .new-grid > .plate{scroll-snap-align:start;}
  .new-mast{padding:56px 0 36px;}
}
"""

GROUPS = [
    ('g1', 'Getting in', 'C-01 C-02 C-06 C-07',
     'The first screen anyone sees, the slide that hands them off, and the two ends of password recovery. '
     'Four screens that decide whether a person reaches the product at all.'),
    ('g2', 'Proving who you are', 'C-04 C-05',
     'The steps #11 asserts in its own stepper &mdash; one marked done, one marked pending, neither drawn. '
     'Step 3 is also what stops the name mismatch that #90 exists to explain.'),
    ('g3', 'Getting money in and out', 'C-03 C-08 C-09',
     'The account number #18 promises on the next screen, and the two instrument forms that #19, #20, #87 '
     'and #90 all reach for.'),
    ('g4', 'The documents you are asked to accept', 'C-10 C-11 C-12 C-13',
     'One viewer, four texts. Every one of them is linked from a moment where a person is being asked to '
     'agree, hand over a passport, or move money &mdash; and none of them existed.'),
]

out = io.StringIO()
w = out.write
w('<title>Andry &mdash; the thirteen</title>\n')
w(sprite)
w('\n<style>\n' + css + '\n' + CHROME + '\n')
w(':root{--d-row:44px;--d-row-lg:56px;}\n</style>\n\n')
w('<div class="doc">\n')

w('''<header class="new-mast">
  <p class="eyebrow">Andry &middot; the flow-blockers, drawn</p>
  <h1>The thirteen<em>screens that let the run finish</em></h1>
  <p class="new-dek">Thirteen plates, built on the Andry design system with no rule added to it and
    nothing in the approved 171 touched. Each one closes a place where a journey stopped: a slide that
    was never made, a step a stepper claimed was done, an account number a screen promised on the
    next screen, a document four plates asked people to accept.</p>
  <p class="new-dek">They are drawn at 402 &times; 874 on the same component set as the run, so they
    can be read beside it without translation. Where a plate had to invent a fact &mdash; a bank, a
    fee, a loss rate &mdash; it is consistent with the figures already published across the 171.</p>
  <p class="new-dek"><strong>One defect surfaced while matching #11.</strong> Its KYC stepper puts the
    step labels inside <span class="mono">.kyc__l</span>, which the system defines as a 2px connector
    line. The text overflows that 2px box and collides with the heading beneath it &mdash; visible on
    the approved plate today. C-04 and C-05 set the same labels in a nowrap span instead, so the new
    work does not inherit the collision. Fixing #11 itself needs a stylesheet change rather than a
    plate edit, and nothing approved was touched here.</p>
  <div class="rules">
    <div class="rule"><b>Nothing approved was altered</b><span>No plate in the 171 was edited, moved
      or re-rendered. These sit behind them.</span></div>
    <div class="rule"><b>No new components</b><span>Every element here already exists in the system:
      the KYC stepper, the verify module, the strength meter, the countdown.</span></div>
    <div class="rule"><b>The reason before the request</b><span>Andry explains why a constraint exists
      wherever it imposes one. These follow that, including where it is unflattering.</span></div>
    <div class="rule"><b>Real numbers throughout</b><span>Loss rates, fees, hold periods and dates are
      specific and reconcile with what the run already states.</span></div>
  </div>
</header>\n\n''')

w('<nav class="new-nav" aria-label="Groups"><ol>\n')
for gid, gname, ids, _ in GROUPS:
    w('  <li><a href="#%s">%s <b>%d</b></a></li>\n' % (gid, gname, len(ids.split())))
w('</ol></nav>\n\n')

byid = {p['id']: p for p in PLATES}
for gid, gname, ids, dek in GROUPS:
    ids = ids.split()
    w('<section class="sec stage-new" id="%s">\n' % gid)
    w('  <div class="stagehead"><span class="code">%s</span>\n    <h2>%s</h2>\n'
      % (ids[0].replace('C-', 'C'), gname))
    w('    <span class="meta">%s &middot; %d screens &middot; all <b>flow-blocking</b></span></div>\n'
      % (' to '.join([ids[0], ids[-1]]) if len(ids) > 1 else ids[0], len(ids)))
    w('  <p class="trackdek">%s</p>\n' % dek)
    w('  <div class="new-grid">\n')
    for i in ids:
        p = byid[i]
        w('<div class="plate">%s<div class="new-cap"><h4><b>%s</b> %s</h4><p>%s</p>'
          % (p['frame'], p['id'], p['title'], p['caption']))
        w('<div class="plate__tags"><span class="fix fix--closes">Closes %s</span>' % p['id'])
        for t in p['tags']:
            w('<span class="fix">%s</span>' % t)
        w('</div></div></div>\n')
    w('  </div>\n</section>\n\n')

w('</div>\n')
doc = out.getvalue()

cut = doc.index('</style>')
head, css_part, tail = doc[:doc.index('<style>')], doc[doc.index('<style>'):cut], doc[cut:]
ascii_only = lambda s: ''.join(c if ord(c) < 128 else '&#%d;' % ord(c) for c in s)
doc = ascii_only(head) + css_part + ascii_only(tail)

io.open('thirteen.html', 'w', encoding='utf-8').write(doc)
io.open('thirteen-preview.html', 'w', encoding='utf-8').write(
    '<!doctype html><html><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1"></head><body>'
    + doc + '</body></html>')
print('bytes:', len(doc.encode('utf-8')))
print('plates:', doc.count('class="new-cap"'))
print('div balance:', len(re.findall(r'<div\b', tail)) - len(re.findall(r'</div>', tail)))
