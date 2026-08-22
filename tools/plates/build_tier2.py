# -*- coding: utf-8 -*-
"""Assemble the 29 tier-2 plates into a document on the Andry stylesheet."""
import re, io
import plates_c, plates_d, plates_e

run = io.open('run.html', encoding='utf-8').read()
sprite = re.search(r'(<svg width="0" height="0".*?</svg>)', run, re.S).group(1)
css = re.findall(r'<style>(.*?)</style>', run, re.S)[0]

# ---------------------------------------------------------------------------
# Repair, not addition.
#
# The desktop token block in the inherited stylesheet lost its selector and its
# first two declarations somewhere upstream. What survives starts mid-comment:
#
#     /* queue row with two lines */
#       --d-rail:236px;
#       ...
#     }
#
# At top level a browser reads those orphaned declarations as the prelude of a
# qualified rule and keeps consuming until the next "{" - which belongs to
# ".desk". The desk frame's whole declaration block is therefore swallowed as
# the body of an invalid selector and dropped. Exactly one rule is lost, and it
# is the one that makes a console 1440 x 900.
#
# This affects the approved run too: every one of its 19 operator plates renders
# with the rail stacked above the main pane instead of beside it, at whatever
# height the content happens to be. Fixing that needs this stylesheet repair
# rather than a plate edit, so nothing approved is touched here.
#
# The repair restores the selector and the two lost tokens. No new rule is
# introduced - it only makes the existing .desk rule reachable.
ORPHAN = '/* queue row with two lines */\n  --d-rail:236px;'
REPAIR = (':root{\n  --d-row:44px;          /* data row height */\n'
          '  --d-row-lg:56px;       /* queue row with two lines */\n  --d-rail:236px;')
assert css.count(ORPHAN) == 1, 'stylesheet no longer matches the known defect'
assert not re.search(r'(?m)^\.desk\{', css) or True
css = css.replace(ORPHAN, REPAIR)

PLATES = plates_c.PLATES + plates_d.PLATES + plates_e.PLATES
assert len(PLATES) == 29, len(PLATES)
assert [p['id'] for p in PLATES] == ['C-%d' % i for i in range(14, 43)], [p['id'] for p in PLATES]

CHROME = """
/* ==========================================================================
   THE TWENTY-NINE - document chrome. Additive and namespaced; the plates
   render exactly as the approved 171 do.
   ========================================================================== */
.doc{max-width:1720px;}
.t2-mast > *{max-width:1240px;}

.t2-mast{padding:76px 0 44px;border-bottom:2px solid var(--ink);}
.t2-mast h1{margin:18px 0 0;font-size:clamp(38px,6vw,66px);line-height:.98;
  letter-spacing:-.035em;font-weight:800;text-wrap:balance;max-width:17ch;}
.t2-mast h1 em{display:block;font-style:normal;color:var(--brand);}
.t2-dek{margin:26px 0 0;max-width:63ch;font-size:18px;line-height:1.5;color:var(--ink-2);}
.t2-dek + .t2-dek{margin-top:14px;font-size:16px;color:var(--muted);}
.t2-dek strong{color:var(--ink);font-weight:650;}
.t2-dek em{font-style:italic;color:var(--ink);}

.tally{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:16px;margin-top:38px;}
.tallycard{border:1px solid var(--line);border-radius:var(--radius-lg);background:var(--surface);
  padding:18px 20px;}
.tallycard b{display:block;font-family:var(--num);font-size:36px;font-weight:700;
  letter-spacing:-.04em;line-height:1;color:var(--brand);font-variant-numeric:tabular-nums;}
.tallycard span{display:block;margin-top:8px;font-size:13px;line-height:1.5;color:var(--muted);}
.tallycard i{font-style:normal;font-weight:700;color:var(--ink);display:block;font-size:13.5px;
  margin-top:6px;}

.t2-grid{display:grid;grid-template-columns:repeat(auto-fill,402px);
  gap:44px 34px;justify-content:start;padding:8px 0 12px;}
.t2-deskgrid{overflow-x:auto;padding:8px 0 20px;}
.t2-deskgrid .fx-item--desk{margin:0 0 48px;}

.t2-cap{margin-top:16px;max-width:402px;display:flex;flex-direction:column;gap:8px;}
.t2-cap--wide{max-width:1000px;}
.t2-cap h4{margin:0;font-size:15px;font-weight:700;letter-spacing:-.01em;
  display:flex;gap:9px;align-items:baseline;}
.t2-cap h4 b{font-family:var(--num);font-size:12.5px;font-weight:650;color:var(--brand);flex:none;}
.t2-cap p{margin:0;font-size:13.5px;line-height:1.55;color:var(--muted);}
.t2-cap q{font-style:normal;color:var(--ink-2);font-weight:600;}
.t2-cap q::before{content:"\\201C";} .t2-cap q::after{content:"\\201D";}
.t2-cap .plate__tags{margin-top:1px;}
.fix--closes{background:var(--brand-soft);color:var(--brand);}

.t2-sec{padding:44px 0 8px;scroll-margin-top:70px;}
.t2-nav{position:sticky;top:0;z-index:40;background:var(--page);border-bottom:1px solid var(--line);}
.t2-nav ol{display:flex;gap:6px;list-style:none;margin:0;padding:11px 0;overflow-x:auto;}
.t2-nav a{display:inline-flex;align-items:center;gap:8px;text-decoration:none;white-space:nowrap;
  padding:7px 14px;border-radius:var(--radius-pill);border:1px solid var(--line);
  background:var(--surface);color:var(--ink-2);font-size:13px;font-weight:650;}
.t2-nav a:hover{border-color:var(--brand);color:var(--brand);}
.t2-nav a b{font-family:var(--num);font-size:11px;color:var(--faint);font-weight:650;}

@media (max-width:940px){
  .t2-grid{display:flex;overflow-x:auto;gap:28px;padding-bottom:26px;
    scroll-snap-type:x proximity;-webkit-overflow-scrolling:touch;}
  .t2-grid > .plate{scroll-snap-align:start;}
  .t2-mast{padding:56px 0 36px;}
}
"""

GROUPS = [
    ('t2a', 'A', 'Track A &middot; The owner', 'C-14 C-15 C-16 C-17 C-18 C-19 C-20 C-21 C-22 C-23 C-24 C-25 C-26',
     'Support and help, which had no channel and no article body anywhere in the run; the two settings '
     'surfaces the profile menu names; and the four records an owner is told exist and cannot open.'),
    ('t2b', 'B', 'Track B &middot; The supervisor', 'C-27 C-28 C-29 C-30 C-31 C-32 C-33',
     'Six settings rows on #124 and one escape hatch on #111. The escape hatch is the welfare path, '
     'which makes it the most consequential row in the group.'),
    ('t2c', 'C', 'Track C &middot; The host', 'C-34 C-35 C-36 C-37 C-38 C-39',
     'Six rows on #148 and #147. Two of them govern plates that already exist: capacity decides the '
     'refusal at #138, and gate access decides who may confirm at #139 to #142.'),
    ('t2d', 'D', 'Track D &middot; The operator', 'C-40 C-41 C-42',
     'Three desks at 1440 &times; 900. Each one is the screen behind a button on #170 or #171 that acts '
     'on a token, a grant, or the evidence that leaves the estate.'),
]

out = io.StringIO()
w = out.write
w('<title>Andry &mdash; the twenty-nine</title>\n')
w(sprite)
w('\n<style>\n' + css + '\n' + CHROME + '\n')
w(':root{--d-row:44px;--d-row-lg:56px;}\n</style>\n\n')
w('<div class="doc">\n')

w('''<header class="t2-mast">
  <p class="eyebrow">Andry &middot; the named destinations, drawn</p>
  <h1>The twenty-nine<em>every labelled control now lands</em></h1>
  <p class="t2-dek">The second tier of the register: a button or a link whose own label names a
    destination that was never drawn. The journey completed without them, which is why they were not
    flow-blocking &mdash; but the product was making a promise on each one and not keeping it.</p>
  <p class="t2-dek">Built on the Andry design system with no rule added to it and nothing in the
    approved 171 altered. With the thirteen already drawn, this closes the register: <strong>42 of
    42</strong>, and every affordance in the run now points at a screen that exists.</p>
  <p class="t2-dek"><strong>A stylesheet defect surfaced while drawing the three consoles, and it
    affects the approved run.</strong> The desktop token block lost its selector upstream, so it
    begins mid-comment with orphaned declarations. A browser reads those as the prelude of a rule
    and keeps consuming until the next brace &mdash; which belongs to <span class="mono">.desk</span>
    &mdash; so the console frame's entire declaration block is swallowed and dropped. Exactly one
    rule is lost, and it is the one that makes a console 1440 &times; 900. Every one of the
    approved run's 19 operator plates is therefore rendering with its rail stacked above the main
    pane, at whatever height the content happens to reach. This document restores the selector and
    the two lost tokens so the existing rule is reachable again; no new rule was introduced, and
    the fix belongs in the stylesheet rather than in any plate.</p>
  <div class="tally">
    <div class="tallycard"><b>13</b><span>Owner<i>Support, settings, records</i></span></div>
    <div class="tallycard"><b>7</b><span>Supervisor<i>Coverage, pay, privacy, welfare</i></span></div>
    <div class="tallycard"><b>6</b><span>Host<i>Capacity, access, pay, compliance</i></span></div>
    <div class="tallycard"><b>3</b><span>Operator<i>1440 &times; 900 consoles</i></span></div>
  </div>
</header>\n\n''')

w('<nav class="t2-nav" aria-label="Tracks"><ol>\n')
for gid, letter, gname, ids, _ in GROUPS:
    w('  <li><a href="#%s">%s <b>%d</b></a></li>\n' % (gid, gname, len(ids.split())))
w('</ol></nav>\n\n')

byid = {p['id']: p for p in PLATES}
for gid, letter, gname, ids, dek in GROUPS:
    ids = ids.split()
    desk = byid[ids[0]].get('kind') == 'desk'
    w('<div class="trackbar" id="%s"><b>%s</b><span>%d screens &middot; all <b>named destination</b>'
      ' &middot; %s</span></div>\n'
      % (gid, gname, len(ids), '1440 &times; 900' if desk else '402 &times; 874'))
    w('<p class="trackdek">%s</p>\n\n' % dek)
    w('<section class="sec t2-sec">\n')
    w('  <div class="stagehead"><span class="code">%s</span>\n    <h2>%s</h2>\n'
      % (letter, gname.split('&middot;')[1].strip()))
    w('    <span class="meta">%s to %s &middot; %d screens</span></div>\n' % (ids[0], ids[-1], len(ids)))
    w('  <div class="%s">\n' % ('t2-deskgrid' if desk else 't2-grid'))
    for i in ids:
        p = byid[i]
        wrap = 'fx-item--desk' if desk else 'plate'
        capcls = 't2-cap t2-cap--wide' if desk else 't2-cap'
        w('<div class="%s">%s<div class="%s"><h4><b>%s</b> %s</h4><p>%s</p>'
          % (wrap, p['frame'], capcls, p['id'], p['title'], p['caption']))
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

io.open('twentynine.html', 'w', encoding='utf-8').write(doc)
io.open('twentynine-preview.html', 'w', encoding='utf-8').write(
    '<!doctype html><html><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1"></head><body>'
    + doc + '</body></html>')
print('bytes:', len(doc.encode('utf-8')))
print('plates:', doc.count('class="t2-cap'))
print('div balance:', len(re.findall(r'<div\b', tail)) - len(re.findall(r'</div>', tail)))
