# -*- coding: utf-8 -*-
"""Tier-2 plates C-40 to C-42 — track D, the operator console at 1440 x 900."""

PLATES = []


def add(pid, title, caption, tags, frame):
    PLATES.append(dict(id=pid, title=title, caption=caption, tags=tags, frame=frame, kind='desk'))


_QUEUES = [('i-scale', 'Disputes', '12'), ('i-users', 'KYC review', '34'),
           ('i-checkc', 'Filing adjudication', '19'), ('i-shield', 'Fraud desk', '12'),
           ('i-lock', 'Escrow adjudication', '6'), ('i-heart', 'Claims', '11'),
           ('i-doc', 'Host inspections', '5')]
_ADMIN = [('i-chart', 'Supervisor standing'), ('i-doc', 'Audit log'), ('i-users', 'Operator roles')]


def rail(active, admin_disabled=True):
    """The function rail. An administrator's queues are unavailable by design (#171)."""
    out = ['<nav class="rail"><div class="rail__brand"><span class="rail__mark">A</span>'
           '<span class="rail__name">Andry Ops</span><span class="rail__env">Prod</span></div>'
           '<div class="rail__scroll"><div class="rail__grp">Queues</div>']
    for ico, lab, n in _QUEUES:
        dis = ' aria-disabled="true"' if admin_disabled else ''
        sr = '<span class="sr">not in your token</span>' if admin_disabled else ''
        out.append('<button class="rail__i" type="button"%s><svg aria-hidden="true"><use href="#%s"/>'
                   '</svg>%s%s<span class="n">%s</span></button>' % (dis, ico, lab, sr, n))
    out.append('<div class="rail__grp">Administration</div>')
    for ico, lab in _ADMIN:
        on = ' is-on' if lab == active else ''
        cur = ' aria-current="page"' if lab == active else ''
        out.append('<button class="rail__i%s" type="button"%s><svg aria-hidden="true">'
                   '<use href="#%s"/></svg>%s</button>' % (on, cur, ico, lab))
    out.append('</div><div class="rail__foot"><button class="rail__i" type="button">'
               '<div class="av av--sm" style="background:var(--brand-soft);color:var(--brand)">TB</div>'
               'Tunde Bakare<span class="n">Admin</span></button></div></nav>')
    return ''.join(out)


# ---------------------------------------------------------------- C-40
add('C-40', 'Add an operator',
    '<strong>#171 can grant and revoke but has no screen for bringing a case-worker into the '
    'estate.</strong> The form is built around the console&rsquo;s own rule, stated on #171: a token is '
    'scoped per function, never a role flag. So there is no role dropdown &mdash; the administrator '
    'picks functions and a ceiling, and the token is previewed in full before it exists.',
    ['Serves #171 <q>Add an operator</q>'],
    '<div class="desk">' + rail('Operator roles') + '''
<div class="main">
<div class="topbar">
<h1>Add an operator</h1>
<span class="topbar__sub">Nothing is created until the token is issued</span>
<span class="topbar__sp"></span>
<button class="dbtn dbtn--secondary" type="button">Cancel</button>
<button class="dbtn dbtn--primary" type="button"><svg aria-hidden="true"><use href="#i-check"/></svg>Issue the token</button>
</div>
<div class="split split--wide">
<div class="pane"><div class="pane__scroll"><div class="pane__pad" style="display:flex;flex-direction:column;gap:16px;max-width:720px">

<div>
<div class="blk__h" style="margin-bottom:9px">The person</div>
<div style="border:1px solid var(--line);border-radius:var(--radius);background:var(--surface);padding:15px;display:flex;flex-direction:column;gap:13px">
<div style="display:grid;grid-template-columns:1fr 1fr;gap:13px">
<label class="field"><span class="field__l">Full name <span class="req">*</span></span><input class="input" value="Sade Ogundimu"></label>
<label class="field"><span class="field__l">Work email <span class="req">*</span></span><input class="input" value="sade.ogundimu@andry.ng"></label>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:13px">
<label class="field"><span class="field__l">Operator number</span><input class="input mono" value="0081" disabled><span class="field__hint">Issued automatically, never reused.</span></label>
<label class="field"><span class="field__l">Starts <span class="req">*</span></span><input class="input" value="11 Aug 2026"></label>
</div>
</div>
</div>

<div>
<div class="blk__h" style="margin-bottom:9px">Functions &mdash; 1 selected</div>
<div style="border:1px solid var(--line);border-radius:var(--radius);background:var(--surface);overflow:hidden">
<table class="tbl tbl--dense">
<thead><tr><th>Function</th><th>View</th><th>Act</th><th>Approve</th></tr></thead>
<tbody>
<tr class="is-sel"><td><span class="t-1">KYC review</span><span class="t-2">34 open &middot; 3 reviewers today</span></td>
<td><span class="badge badge--ok"><svg aria-hidden="true"><use href="#i-check"/></svg>Yes</span></td>
<td><span class="badge badge--ok"><svg aria-hidden="true"><use href="#i-check"/></svg>Yes</span></td>
<td><span class="badge"><svg aria-hidden="true"><use href="#i-close"/></svg>No</span></td></tr>
<tr><td><span class="t-1">Disputes</span><span class="t-2">12 open</span></td>
<td><span class="badge"><svg aria-hidden="true"><use href="#i-close"/></svg>No</span></td><td><span class="badge"><svg aria-hidden="true"><use href="#i-close"/></svg>No</span></td><td><span class="badge"><svg aria-hidden="true"><use href="#i-close"/></svg>No</span></td></tr>
<tr><td><span class="t-1">Claims</span><span class="t-2">11 open</span></td>
<td><span class="badge"><svg aria-hidden="true"><use href="#i-close"/></svg>No</span></td><td><span class="badge"><svg aria-hidden="true"><use href="#i-close"/></svg>No</span></td><td><span class="badge"><svg aria-hidden="true"><use href="#i-close"/></svg>No</span></td></tr>
<tr><td><span class="t-1">Fraud desk</span><span class="t-2">12 open &middot; may place holds</span></td>
<td><span class="badge"><svg aria-hidden="true"><use href="#i-close"/></svg>No</span></td><td><span class="badge"><svg aria-hidden="true"><use href="#i-close"/></svg>No</span></td><td><span class="badge"><svg aria-hidden="true"><use href="#i-close"/></svg>No</span></td></tr>
</tbody>
</table>
</div>
<p style="margin:9px 0 0;font-size:var(--d-fs-sm);color:var(--ink-2);line-height:1.55">There is no role to pick. A token is a set of functions and a ceiling, so nobody inherits access by having a job title.</p>
</div>

<div>
<div class="blk__h" style="margin-bottom:9px">Ceiling</div>
<div style="border:1px solid var(--line);border-radius:var(--radius);background:var(--surface);padding:15px;display:flex;flex-direction:column;gap:12px">
<div class="spread"><div><div style="font-size:var(--d-fs);font-weight:700">Tier 1 documents only</div>
<div style="font-size:var(--d-fs-sm);color:var(--ink-2);margin-top:2px">NIN slip and voter&rsquo;s card. Passports and licences go to a tier 2 reviewer.</div></div>
<span class="badge badge--brand">Set</span></div>
<hr class="hr" style="margin:0"/>
<div class="spread"><div><div style="font-size:var(--d-fs);font-weight:700">Cannot approve</div>
<div style="font-size:var(--d-fs-sm);color:var(--ink-2);margin-top:2px">Every decision is countersigned by Yusuf Bello until this is lifted.</div></div>
<span class="badge badge--brand">Set</span></div>
</div>
</div>

</div></div></div>

<div class="pane pane--insp">
<div class="insp__h"><h2 class="insp__t">Token preview</h2>
<span style="font-size:var(--d-fs-sm);color:var(--muted)">operator 0081 &middot; not yet issued</span></div>
<div class="pane__scroll">
<div class="blk"><div class="blk__h">What Sade will be able to do</div>
<div style="display:flex;flex-direction:column;gap:9px;margin-top:9px">
<div class="row" style="gap:9px;align-items:flex-start"><svg width="17" height="17" style="color:var(--ok);flex:none;margin-top:2px" aria-hidden="true"><use href="#i-check"/></svg><span style="font-size:var(--d-fs-sm);color:var(--ink-2)">Open and work the KYC queue, tier 1 documents</span></div>
<div class="row" style="gap:9px;align-items:flex-start"><svg width="17" height="17" style="color:var(--ok);flex:none;margin-top:2px" aria-hidden="true"><use href="#i-check"/></svg><span style="font-size:var(--d-fs-sm);color:var(--ink-2)">Ask an applicant for a better document</span></div>
<div class="row" style="gap:9px;align-items:flex-start"><svg width="17" height="17" style="color:var(--risk);flex:none;margin-top:2px" aria-hidden="true"><use href="#i-close"/></svg><span style="font-size:var(--d-fs-sm);color:var(--ink-2)">Approve or reject &mdash; countersigned only</span></div>
<div class="row" style="gap:9px;align-items:flex-start"><svg width="17" height="17" style="color:var(--risk);flex:none;margin-top:2px" aria-hidden="true"><use href="#i-close"/></svg><span style="font-size:var(--d-fs-sm);color:var(--ink-2)">See any other queue, or any owner&rsquo;s money</span></div>
</div>
</div>
<div class="blk"><div class="blk__h">Separation of duties</div>
<div style="border:1.5px solid var(--ok);border-radius:var(--radius);background:var(--ok-soft);padding:12px 14px;margin-top:9px">
<div class="row" style="gap:9px"><svg width="17" height="17" style="color:var(--ok);flex:none" aria-hidden="true"><use href="#i-checkc"/></svg>
<span style="font-size:var(--d-fs);font-weight:700;color:var(--ok)">No conflict</span></div>
<p style="margin:6px 0 0;font-size:var(--d-fs-sm);color:var(--ink-2);line-height:1.55">Act without approve on a single function raises nothing. Checked against the other 14 tokens.</p>
</div>
</div>
<div class="blk"><div class="blk__h">Before it is issued</div>
<div style="display:flex;flex-direction:column;gap:11px;margin-top:9px">
<div class="row" style="gap:9px;align-items:flex-start"><svg width="17" height="17" style="color:var(--muted);flex:none;margin-top:2px" aria-hidden="true"><use href="#i-lock"/></svg><span style="font-size:var(--d-fs-sm);color:var(--ink-2)">Sade enrols a hardware key on first sign-in. There is no password path into this console.</span></div>
<div class="row" style="gap:9px;align-items:flex-start"><svg width="17" height="17" style="color:var(--muted);flex:none;margin-top:2px" aria-hidden="true"><use href="#i-doc"/></svg><span style="font-size:var(--d-fs-sm);color:var(--ink-2)">The grant is written to the audit log against your name, not the estate&rsquo;s.</span></div>
<div class="row" style="gap:9px;align-items:flex-start"><svg width="17" height="17" style="color:var(--muted);flex:none;margin-top:2px" aria-hidden="true"><use href="#i-clock"/></svg><span style="font-size:var(--d-fs-sm);color:var(--ink-2)">An unused token is suspended after 30 days without a sign-in.</span></div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>''')

# ---------------------------------------------------------------- C-41
add('C-41', 'Function and grant editor',
    '<strong>Four controls on #171 act on a grant and none of them opens an editor.</strong> This is '
    'where the conflict flagged on that plate is actually resolved. The conflict is restated at the top '
    'with the two ways out priced against each other, because <q>split the grant</q> means nothing until '
    'a person can see who ends up holding the other half.',
    ['Serves #171 <q>Add a function</q>, <q>Grant</q>, <q>Split the grant</q>'],
    '<div class="desk">' + rail('Operator roles') + '''
<div class="main">
<div class="topbar">
<h1>Funke Adeyemi</h1>
<span class="topbar__sub">operator 0038 &middot; claims assessor since 04 Mar 2026</span>
<span class="topbar__sp"></span>
<button class="dbtn dbtn--secondary" type="button">Discard changes</button>
<button class="dbtn dbtn--primary" type="button"><svg aria-hidden="true"><use href="#i-check"/></svg>Save the grant</button>
</div>
<div class="split split--wide">
<div class="pane"><div class="pane__scroll"><div class="pane__pad" style="display:flex;flex-direction:column;gap:16px;max-width:760px">

<div style="border:1.5px solid var(--warn);border-radius:var(--radius);background:var(--warn-soft);padding:14px 16px">
<div class="row" style="gap:11px;align-items:flex-start">
<svg width="19" height="19" style="color:var(--warn);flex:none;margin-top:1px" aria-hidden="true"><use href="#i-alert"/></svg>
<div class="grow">
<div style="font-size:var(--d-fs);font-weight:730;color:var(--warn)">Funke assesses a claim and approves its payout</div>
<p style="margin:5px 0 0;font-size:var(--d-fs-sm);color:var(--ink-2);line-height:1.55">One person deciding and releasing money on the same case, up to &#8358;1,500,000.00. Nine claims were settled that way in July. Removing <b>approve</b> sends them to Ngozi Abara, who already holds it on escrow and has capacity. Lowering the ceiling to &#8358;250,000.00 instead leaves 6 of those 9 untouched.</p>
</div>
</div>
</div>

<div>
<div class="blk__h" style="margin-bottom:9px">Functions</div>
<div style="border:1px solid var(--line);border-radius:var(--radius);background:var(--surface);overflow:hidden">
<table class="tbl tbl--dense">
<thead><tr><th>Function</th><th>View</th><th>Act</th><th>Approve</th><th>Ceiling</th></tr></thead>
<tbody>
<tr class="is-sel"><td><span class="t-1">Claims assessment</span><span class="t-2">11 open &middot; 4 assigned to Funke</span></td>
<td><span class="badge badge--ok"><svg aria-hidden="true"><use href="#i-check"/></svg>Yes</span></td>
<td><span class="badge badge--ok"><svg aria-hidden="true"><use href="#i-check"/></svg>Yes</span></td>
<td><span class="badge badge--warn"><svg aria-hidden="true"><use href="#i-alert"/></svg>Conflict</span></td>
<td><span class="t-1 mono">&#8358;1,500,000.00</span></td></tr>
<tr><td><span class="t-1">Host inspections</span><span class="t-2">5 open</span></td>
<td><span class="badge badge--ok"><svg aria-hidden="true"><use href="#i-check"/></svg>Yes</span></td>
<td><span class="badge"><svg aria-hidden="true"><use href="#i-close"/></svg>No</span></td>
<td><span class="badge"><svg aria-hidden="true"><use href="#i-close"/></svg>No</span></td>
<td><span class="t-2">&mdash;</span></td></tr>
<tr><td><span class="t-1">Escrow adjudication</span><span class="t-2">6 open</span></td>
<td><span class="badge"><svg aria-hidden="true"><use href="#i-close"/></svg>No</span></td>
<td><span class="badge"><svg aria-hidden="true"><use href="#i-close"/></svg>No</span></td>
<td><span class="badge"><svg aria-hidden="true"><use href="#i-close"/></svg>No</span></td>
<td><span class="t-2">&mdash;</span></td></tr>
</tbody>
</table>
</div>
<button class="dbtn dbtn--secondary" type="button" style="margin-top:11px"><svg aria-hidden="true"><use href="#i-plus"/></svg>Add a function</button>
</div>

<div>
<div class="blk__h" style="margin-bottom:9px">Ceiling on claims approval</div>
<div style="border:1px solid var(--line);border-radius:var(--radius);background:var(--surface);padding:15px;display:flex;flex-direction:column;gap:12px">
<div class="row" style="gap:11px">
<span class="t-2" style="flex:none">&#8358;0</span>
<div class="prog" style="flex:1"><i style="width:76%"></i></div>
<span class="t-2" style="flex:none">&#8358;2,000,000</span>
</div>
<div class="spread">
<span style="font-size:var(--d-fs-sm);color:var(--ink-2)">Currently <b class="mono" style="color:var(--ink)">&#8358;1,500,000.00</b> &middot; covers 9 of the 11 open claims</span>
<span class="badge badge--warn"><svg aria-hidden="true"><use href="#i-alert"/></svg>Above the &#8358;250,000.00 four-eyes line</span>
</div>
</div>
</div>

</div></div></div>

<div class="pane pane--insp">
<div class="insp__h"><h2 class="insp__t">Two ways out</h2>
<span style="font-size:var(--d-fs-sm);color:var(--muted)">Pick one; the conflict clears either way</span></div>
<div class="pane__scroll">
<div class="blk">
<div style="border:1px solid var(--line-2);border-radius:var(--radius);background:var(--surface);padding:13px 15px">
<div style="font-size:var(--d-fs);font-weight:730">Split the grant</div>
<p style="margin:6px 0 0;font-size:var(--d-fs-sm);color:var(--ink-2);line-height:1.55">Funke keeps assess, Ngozi Abara takes approve. Cleanest separation. Adds 9 approvals a month to Ngozi, who currently runs at 62% of her load.</p>
<button class="dbtn dbtn--primary" type="button" style="margin-top:11px;width:100%;justify-content:center">Split it</button>
</div>
</div>
<div class="blk">
<div style="border:1px solid var(--line-2);border-radius:var(--radius);background:var(--surface);padding:13px 15px">
<div style="font-size:var(--d-fs);font-weight:730">Lower the ceiling</div>
<p style="margin:6px 0 0;font-size:var(--d-fs-sm);color:var(--ink-2);line-height:1.55">Funke keeps both below &#8358;250,000.00, which is the four-eyes line the estate already uses elsewhere. Faster for small claims, and 6 of 9 July settlements would have been unaffected.</p>
<button class="dbtn dbtn--secondary" type="button" style="margin-top:11px;width:100%;justify-content:center">Set &#8358;250,000.00</button>
</div>
</div>
<div class="blk"><div class="blk__h">What changes for Funke</div>
<div style="display:flex;flex-direction:column;gap:9px;margin-top:9px">
<div class="row" style="gap:9px;align-items:flex-start"><svg width="17" height="17" style="color:var(--muted);flex:none;margin-top:2px" aria-hidden="true"><use href="#i-info"/></svg><span style="font-size:var(--d-fs-sm);color:var(--ink-2)">Her 4 open claims stay with her. A change to a grant never reassigns work in flight.</span></div>
<div class="row" style="gap:9px;align-items:flex-start"><svg width="17" height="17" style="color:var(--muted);flex:none;margin-top:2px" aria-hidden="true"><use href="#i-bell"/></svg><span style="font-size:var(--d-fs-sm);color:var(--ink-2)">She is told what changed and who decided it, by name.</span></div>
<div class="row" style="gap:9px;align-items:flex-start"><svg width="17" height="17" style="color:var(--muted);flex:none;margin-top:2px" aria-hidden="true"><use href="#i-doc"/></svg><span style="font-size:var(--d-fs-sm);color:var(--ink-2)">Written to the audit log with the conflict it resolved.</span></div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>''')

# ---------------------------------------------------------------- C-42
add('C-42', 'Audit log &mdash; export a bundle',
    '<strong>Two controls on #170 compose an evidence bundle for a regulator or a court.</strong> What '
    'goes in, over what range, and who receives it was shown nowhere. The bundle is hashed and the hash '
    'is displayed before export, because a bundle nobody can prove is unaltered is not evidence &mdash; '
    'and the export is itself logged, which the screen says out loud.',
    ['Serves #170 <q>Export a bundle</q>, <q>Bundle these 15 entries</q>'],
    '<div class="desk">' + rail('Audit log') + '''
<div class="main">
<div class="topbar">
<h1>Export a bundle</h1>
<span class="topbar__sub">15 entries selected &middot; AND-DSP-2026-0089</span>
<span class="topbar__sp"></span>
<button class="dbtn dbtn--secondary" type="button">Back to the log</button>
<button class="dbtn dbtn--primary" type="button"><svg aria-hidden="true"><use href="#i-download"/></svg>Build the bundle</button>
</div>
<div class="split split--wide">
<div class="pane"><div class="pane__scroll"><div class="pane__pad" style="display:flex;flex-direction:column;gap:16px;max-width:760px">

<div style="border:1px solid var(--line);border-radius:var(--radius);background:var(--surface-2);padding:13px 15px">
<div class="row" style="gap:11px;align-items:flex-start">
<svg width="19" height="19" style="color:var(--ink-2);flex:none;margin-top:1px" aria-hidden="true"><use href="#i-shield"/></svg>
<div class="grow">
<div style="font-size:var(--d-fs);font-weight:730">This export is itself an audit event</div>
<p style="margin:5px 0 0;font-size:var(--d-fs-sm);color:var(--ink-2);line-height:1.55">Your name, the range, the reason and the recipient are written to the log the moment the bundle is built. You cannot export without leaving a record that you did.</p>
</div>
</div>
</div>

<div>
<div class="blk__h" style="margin-bottom:9px">What goes in &mdash; 15 entries, 04 Jul to 04 Aug 2026</div>
<div style="border:1px solid var(--line);border-radius:var(--radius);background:var(--surface);overflow:hidden">
<table class="tbl tbl--dense">
<thead><tr><th>When</th><th>Operator</th><th>Event</th><th>Subject</th></tr></thead>
<tbody>
<tr><td><span class="t-1 mono">04 Aug 10:31</span></td><td><span class="t-1">Ngozi Abara</span></td>
<td><span class="t-1">Took to decision, stage 4</span><span class="t-2">Dispute AND-DSP-2026-0089</span></td>
<td><span class="t-1">Bola Salami</span><span class="t-2 mono">AND-4471-KX</span></td></tr>
<tr><td><span class="t-1 mono">03 Aug 14:02</span></td><td><span class="t-1">Ngozi Abara</span></td>
<td><span class="t-1">Ordered an independent re-scan</span><span class="t-2">Ilesa Highland Ranch</span></td>
<td><span class="t-1">Bola Salami</span><span class="t-2 mono">AND-4471-KX</span></td></tr>
<tr><td><span class="t-1 mono">02 Aug 09:18</span></td><td><span class="t-1">Chike Nwosu</span></td>
<td><span class="t-1">Placed an escrow hold</span><span class="t-2">&#8358;148,600.00</span></td>
<td><span class="t-1">Bola Salami</span><span class="t-2 mono">AND-ESC-2026-4471</span></td></tr>
<tr><td><span class="t-1 mono">28 Jul 16:44</span></td><td><span class="t-1">Adekola Taiwo</span></td>
<td><span class="t-1">Filed a Proof of Life record</span><span class="t-2">412 kg &middot; pen 4</span></td>
<td><span class="t-1">&mdash;</span><span class="t-2 mono">AND-4471-KX</span></td></tr>
<tr><td><span class="t-1 mono">21 Jul 11:07</span></td><td><span class="t-1">Amaka Obi</span></td>
<td><span class="t-1">Rejected a record</span><span class="t-2">Tag photograph incomplete</span></td>
<td><span class="t-1">&mdash;</span><span class="t-2 mono">AND-4471-KX</span></td></tr>
</tbody>
</table>
</div>
<p style="margin:9px 0 0;font-size:var(--d-fs-sm);color:var(--ink-2);line-height:1.55">10 further entries are in the range and not shown here. Every one of them is in the bundle.</p>
</div>

<div>
<div class="blk__h" style="margin-bottom:9px">Include with each entry</div>
<div style="border:1px solid var(--line);border-radius:var(--radius);background:var(--surface);padding:15px;display:flex;flex-direction:column;gap:12px">
<div class="spread"><div><div style="font-size:var(--d-fs);font-weight:700">Attachments and photographs</div>
<div style="font-size:var(--d-fs-sm);color:var(--ink-2);margin-top:2px">41 files &middot; 82 MB. The re-scan photographs are the substance of this dispute.</div></div>
<span class="badge badge--ok"><svg aria-hidden="true"><use href="#i-check"/></svg>In</span></div>
<hr class="hr" style="margin:0"/>
<div class="spread"><div><div style="font-size:var(--d-fs);font-weight:700">Owner and supervisor messages</div>
<div style="font-size:var(--d-fs-sm);color:var(--ink-2);margin-top:2px">28 messages between the parties on this case only</div></div>
<span class="badge badge--ok"><svg aria-hidden="true"><use href="#i-check"/></svg>In</span></div>
<hr class="hr" style="margin:0"/>
<div class="spread"><div><div style="font-size:var(--d-fs);font-weight:700">Identity documents</div>
<div style="font-size:var(--d-fs-sm);color:var(--ink-2);margin-top:2px">Excluded unless the request names them. A dispute about an animal does not need a passport scan.</div></div>
<span class="badge badge--risk"><svg aria-hidden="true"><use href="#i-close"/></svg>Out</span></div>
</div>
</div>

</div></div></div>

<div class="pane pane--insp">
<div class="insp__h"><h2 class="insp__t">The bundle</h2>
<span style="font-size:var(--d-fs-sm);color:var(--muted)">Not built yet</span></div>
<div class="pane__scroll">
<div class="blk"><div class="blk__h">Reason for the export</div>
<div style="margin-top:9px;display:flex;flex-direction:column;gap:11px">
<label class="field"><span class="field__l">Requested by <span class="req">*</span></span><input class="input" value="Federal Competition and Consumer Protection Commission"></label>
<label class="field"><span class="field__l">Their reference <span class="req">*</span></span><input class="input mono" value="FCCPC/CP/2026/0412"></label>
<label class="field"><span class="field__l">Why</span><input class="input" value="Complaint by the owner, 29 Jul 2026"></label>
</div>
</div>
<div class="blk"><div class="blk__h">Integrity</div>
<div style="border:1px solid var(--line);border-radius:var(--radius);background:var(--surface-2);padding:12px 14px;margin-top:9px">
<div style="font-size:var(--d-fs-sm);color:var(--ink-2)">SHA-256 of the manifest, shown before you send and printed on the cover sheet.</div>
<div class="mono" style="font-size:11.5px;margin-top:7px;word-break:break-all;color:var(--ink)">4f2a&hellip;computed when the bundle is built</div>
</div>
</div>
<div class="blk"><div class="blk__h">Estimated</div>
<div style="display:flex;flex-direction:column;gap:9px;margin-top:9px">
<div class="spread"><span style="font-size:var(--d-fs-sm);color:var(--ink-2)">Entries</span><span class="t-1 mono">15</span></div>
<div class="spread"><span style="font-size:var(--d-fs-sm);color:var(--ink-2)">Files</span><span class="t-1 mono">41</span></div>
<div class="spread"><span style="font-size:var(--d-fs-sm);color:var(--ink-2)">Size</span><span class="t-1 mono">82 MB</span></div>
<div class="spread"><span style="font-size:var(--d-fs-sm);color:var(--ink-2)">Format</span><span class="t-1">PDF cover sheet + ZIP</span></div>
</div>
</div>
<div class="blk">
<div style="border:1.5px solid var(--warn);border-radius:var(--radius);background:var(--warn-soft);padding:12px 14px">
<div class="row" style="gap:9px"><svg width="17" height="17" style="color:var(--warn);flex:none" aria-hidden="true"><use href="#i-alert"/></svg>
<span style="font-size:var(--d-fs);font-weight:700;color:var(--warn)">Second administrator required</span></div>
<p style="margin:6px 0 0;font-size:var(--d-fs-sm);color:var(--ink-2);line-height:1.55">Bundles leaving the estate are countersigned. Tunde Bakare cannot approve his own export; this goes to Adaeze Nwankwo.</p>
</div>
</div>
</div>
</div>
</div>
</div>
</div>''')
