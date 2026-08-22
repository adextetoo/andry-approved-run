# -*- coding: utf-8 -*-
"""Bring the gap register up to date: all 42 are drawn, and record the two
stylesheet defects the drawing work surfaced.

The register page carries its own stylesheet and never inherited either Andry
defect, so nothing here is a CSS repair - this is a content update.
"""
import io, re

p = 'closing.html'
s = io.open(p, encoding='utf-8').read()

# --------------------------------------------------------------- new styles
NEW_CSS = """
/* --- status, added when the register was closed --- */
.tag--done{background:var(--ok-soft);color:var(--ok);}
.tag--done::before{border-radius:50%;}

.closed{margin-top:34px;border:1.5px solid var(--ok);border-radius:var(--radius-lg);
  background:var(--ok-soft);padding:20px 24px;}
.closed h2{margin:0 0 8px;font-size:16px;font-weight:750;letter-spacing:-.012em;color:var(--ok);
  display:flex;align-items:center;gap:9px;}
.closed p{margin:0 0 12px;font-size:14.5px;line-height:1.6;color:var(--ink-2);max-width:70ch;}
.closed p:last-child{margin-bottom:0;}
.closed a{font-weight:650;}
.closed strong{color:var(--ink);font-weight:680;}

.defects{margin-top:26px;display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px;}
.defect{border:1px solid var(--line);border-left:3px solid var(--warn);
  border-radius:0 var(--radius) var(--radius) 0;background:var(--surface);padding:16px 18px;}
.defect b{display:block;font-size:14px;font-weight:730;letter-spacing:-.01em;margin-bottom:6px;}
.defect p{margin:0 0 8px;font-size:13px;line-height:1.55;color:var(--muted);}
.defect p:last-child{margin-bottom:0;}
.defect code{font-family:var(--num);font-size:12px;background:var(--surface-3);
  padding:1px 5px;border-radius:4px;color:var(--ink-2);}
.defect .fixed{display:inline-flex;align-items:center;gap:6px;font-family:var(--num);font-size:11px;
  font-weight:650;padding:3px 9px;border-radius:var(--radius-sm);
  background:var(--ok-soft);color:var(--ok);margin-top:4px;}
"""
anchor = '.note{margin-top:56px;'
assert s.count(anchor) == 1
s = s.replace(anchor, NEW_CSS + '\n' + anchor)

# ------------------------------------------------- a "drawn" chip per entry
def chip_for(cid):
    n = int(cid.split('-')[1])
    where = ('the thirteen', 'closers') if n <= 13 else ('the twenty-nine', 'closers-2')
    return '<span class="tag tag--done">Drawn &middot; %s</span>' % where[0]

ids = re.findall(r'<div class="item__id">(C-\d+)</div>', s)
assert len(ids) == 42
out, pos, i = [], 0, 0
for m in re.finditer(r'<div class="tags">', s):
    out.append(s[pos:m.end()])
    out.append(chip_for(ids[i]))
    pos, i = m.end(), i + 1
out.append(s[pos:])
s = ''.join(out)
assert s.count('tag--done') == 42 + 2  # 42 chips + the two CSS rules

# ------------------------------------------------------- the closing banner
BANNER = '''
  <div class="closed">
    <h2><span aria-hidden="true">&#10003;</span> All 42 are drawn</h2>
    <p>The register is closed. The <strong>13 flow-blockers</strong> are drawn in
      <a href="../closers/">the thirteen</a>, and the <strong>29 named destinations</strong> in
      <a href="../closers-2/">the twenty-nine</a> &mdash; both on the Andry design system, with
      nothing in the approved 171 altered. Every labelled affordance in the run now points at a
      screen that exists.</p>
    <p>The counts below are kept as they were found, so the register still reads as the audit that
      produced them rather than as a summary written afterwards.</p>
  </div>

  <div class="defects">
    <div class="defect">
      <b>The operator consoles had no frame</b>
      <p>The desktop token block had lost its selector upstream, so it began mid-comment with
        orphaned declarations. A browser reads those as a rule prelude and consumes until the next
        brace &mdash; which belongs to <code>.desk</code> &mdash; swallowing the console frame's
        whole declaration block. All 19 operator plates were rendering with the rail stacked above
        the main pane.</p>
      <span class="fixed">Fixed in the stylesheet</span>
    </div>
    <div class="defect">
      <b>The KYC stepper labels collided</b>
      <p><code>.kyc__l</code> was defined as a 2px connector line, but every stepper in the product
        puts its step label inside it &mdash; #11, #103 and #132. The text overflowed that box and
        ran into the heading beneath.</p>
      <span class="fixed">Fixed in the stylesheet</span>
    </div>
  </div>
'''
tail = '</header>'
assert s.count(tail) == 1
s = s.replace(tail, BANNER + tail)

# ---------------------------------------------------- masthead dek + eyebrow
s = s.replace(
    '<p class="eyebrow">Andry &middot; gap register against the approved 171</p>',
    '<p class="eyebrow">Andry &middot; gap register against the approved 171 &middot; closed</p>')

old_dek = ('    a register of what sits <em>behind</em> it. <strong>42 screens close every dead end</strong>,\n'
           '    of which <strong>13 block a journey from completing at all</strong>.</p>')
assert s.count(old_dek) == 1
s = s.replace(old_dek,
    '    a register of what sits <em>behind</em> it. <strong>42 screens close every dead end</strong>,\n'
    '    of which <strong>13 block a journey from completing at all</strong>. All 42 have since been\n'
    '    drawn.</p>')

# the closing note should say the defects were fixed, not merely observed
old_note = ('  <p>Nothing in the approved 171 was modified, moved or re-rendered to produce this. The register\n'
            '    was built by parsing the published run, and the affordance counts were verified against the\n'
            '    live DOM at <b>adextetoo.github.io/andry-approved-run</b>: 1,296 buttons, 35 links, 171 plates.</p>')
assert s.count(old_note) == 1
s = s.replace(old_note,
    '  <p>Nothing in the approved 171 was modified, moved or re-rendered to produce this register. It was\n'
    '    built by parsing the published run, and the affordance counts were verified against the live DOM\n'
    '    at <b>adextetoo.github.io/andry-approved-run</b>: 1,296 buttons, 35 links, 171 plates.</p>\n'
    '  <p>Two stylesheet defects surfaced later, while the 42 were being drawn, and both are now fixed\n'
    '    &mdash; in the stylesheet, never in a plate. They are summarised at the top of this page and\n'
    '    documented in <b>tools/stylesheet_repairs.py</b>.</p>')

io.open(p, 'w', encoding='utf-8').write(s)
print('closing.html updated: 42 drawn chips, closing banner, defect cards, dek and note')
