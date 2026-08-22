# -*- coding: utf-8 -*-
"""Tier-2 plates C-27 to C-39 — track B the supervisor, track C the host."""
from plates_a import ST
from plates_c import tabbar, bar

PLATES = []


def add(pid, title, caption, tags, frame):
    PLATES.append(dict(id=pid, title=title, caption=caption, tags=tags, frame=frame))


# ================================================================ TRACK B
# ---------------------------------------------------------------- C-27
add('C-27', 'Coverage &mdash; states and ranches',
    '<strong>The setting that decides every assignment a supervisor is offered.</strong> Named on #124 '
    'with its current value and drawn nowhere. Widening coverage is the lever a supervisor with an empty '
    'week reaches for, so the consequence of each state is priced in travel time rather than left as a '
    'checkbox.',
    ['Serves #124 <q>States</q>'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to settings') + '''
<div class="scroll"><div class="pad pb stack g5">
<div class="card stack g2" style="margin-top:6px">
<div class="spread"><span class="lbl">Working area</span><span class="badge badge--brand"><svg><use href="#i-pin"/></svg>3 states</span></div>
<span class="sub">61 animals across 2 host ranches. You are offered assignments only inside this area.</span>
</div>
<div class="sect" style="margin-top:2px"><div class="sect__h"><h3>States you cover</h3></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Oyo</span><span class="tiny">Ayalar Ranch &middot; 47 animals &middot; 22 km from home</span></span><span class="badge badge--ok"><svg><use href="#i-check"/></svg>On</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Osun</span><span class="tiny">Ilesa Highland Ranch &middot; 14 animals &middot; 61 km</span></span><span class="badge badge--ok"><svg><use href="#i-check"/></svg>On</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Kwara</span><span class="tiny">No host ranch yet &middot; nothing to be offered</span></span><span class="badge"><svg><use href="#i-clock"/></svg>Idle</span></button>
</div></div>
<div class="sect"><div class="sect__h"><h3>Could be added</h3></div>
<div class="list">
<div class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Ogun</span><span class="tiny">9 host ranches &middot; 128 km &middot; about 2 hours each way</span></span><button class="btn btn--sm btn--secondary" style="min-height:40px">Add</button></div>
<div class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Ekiti</span><span class="tiny">2 host ranches &middot; 94 km &middot; about 90 minutes</span></span><button class="btn btn--sm btn--secondary" style="min-height:40px">Add</button></div>
</div></div>
<div class="card card--plain stack g3">
<div class="row" style="gap:10px"><svg width="19" height="19" style="color:var(--warn);flex:none"><use href="#i-alert"/></svg>
<span class="grow" style="font-size:14px;font-weight:700">Adding a state is a promise</span></div>
<p class="sub" style="margin:0">A weekly visit is a weekly visit whatever the distance. Take Ogun only if you can reach it every week in the rains &mdash; a missed record counts against your standing, not against the road.</p>
</div>
</div></div>
<div class="actionbar"><button class="btn btn--primary btn--block">Save coverage</button></div>
''' + tabbar('sup', 4) + '''
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-28
add('C-28', 'Payout account &mdash; supervisor',
    '<strong>Named twice, including as an onboarding task on #104 while an application is under '
    'review.</strong> Same name-match check as the owner form, on a fixed monthly pay date rather than '
    'on demand &mdash; so the screen leads with when money arrives, which is the thing a supervisor is '
    'actually here to confirm.',
    ['Serves #124, #104', 'May share C-08'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to settings') + '''
<div class="scroll"><div class="pad pb stack g5">
<div class="card card--brand stack g2">
<span class="lbl">Next payment</span>
<span class="money money--xl">&#8358;27,000.00</span>
<span class="fx" style="color:rgba(255,255,255,.72)">07 Sep 2026 &middot; 6 assignments for August</span>
</div>
<div class="verify">
<div class="verify__top">
<svg width="20" height="20" style="color:var(--ok);flex:none"><use href="#i-checkc"/></svg>
<div class="grow"><div style="font-size:13.5px;font-weight:700;color:var(--ok)">Name matches your licence</div>
<div class="tiny" style="color:var(--ok)">Checked with GTBank on 12 Mar 2026</div></div>
</div>
<div class="verify__row"><span class="k">Bank</span><span class="grow v">Guaranty Trust Bank</span></div>
<div class="verify__row"><span class="k">Account</span><span class="grow mono" style="font-weight:650;color:var(--ink)">&bull;&bull;&bull;&bull;&bull;&bull;4419</span></div>
<div class="verify__row"><span class="k">Name</span><span class="grow v">ADEKOLA TAIWO</span></div>
</div>
<div class="card card--plain stack g3">
<div class="row" style="gap:10px"><svg width="19" height="19" style="color:var(--muted);flex:none"><use href="#i-calendar"/></svg>
<span class="grow" style="font-size:14px;font-weight:700">Paid on the 7th, for the month before</span></div>
<p class="sub" style="margin:0">Work filed in August is paid on 7 September. A record rejected on appeal is added to the next run rather than held back &mdash; you are not paid late for winning an appeal.</p>
</div>
<div class="sect" style="margin-top:2px"><div class="sect__h"><h3>Recent payments</h3><a href="#">All 17</a></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14px;font-weight:660">07 Aug 2026</span><span class="tiny">July &middot; 6 assignments &middot; 1 late deduction</span></span><span class="money money--sm">&#8358;25,650.00</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14px;font-weight:660">07 Jul 2026</span><span class="tiny">June &middot; 6 assignments</span></span><span class="money money--sm">&#8358;27,000.00</span></button>
</div></div>
</div></div>
<div class="actionbar"><button class="btn btn--secondary btn--block">Change this account</button>
<p class="tiny" style="margin:9px 0 0;text-align:center">A change takes effect from the following month, never mid-run.</p></div>
''' + tabbar('sup', 4) + '''
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-29
add('C-29', 'Privacy &mdash; what owners see',
    '<strong>A supervisor is a named individual carrying a public record.</strong> #124 offers this row '
    'and nothing opens. Rather than list toggles, the screen shows the profile exactly as an owner sees '
    'it and marks each line shown, hidden or fixed &mdash; the fixed ones being the price of the licence.',
    ['Serves #124 <q>Privacy and what owners see</q>'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to settings') + '''
<div class="scroll"><div class="pad pb stack g5">
<p class="sub" style="margin:6px 0 0">This is your profile as an owner sees it before assigning you an animal.</p>
<div class="card stack g3">
<div class="row" style="gap:11px">
<div class="av av--lg" style="background:var(--brand-soft);color:var(--brand)">AT</div>
<div class="grow"><div style="font-size:17px;font-weight:750;letter-spacing:-.015em">Adekola Taiwo</div>
<div class="tiny">Supervisor &middot; SUP-2481-AT &middot; Oyo, Osun, Kwara</div>
<div class="row" style="gap:5px;margin-top:5px"><svg width="14" height="14" style="color:var(--gold)"><use href="#i-star"/></svg><span class="tiny" style="color:var(--ink-2)">4.8 &middot; 214 ratings &middot; 61 herds</span></div></div>
</div>
</div>
<div class="sect" style="margin-top:2px"><div class="sect__h"><h3>Always shown</h3></div>
<div class="card card--plain stack g3">
<div class="row" style="gap:10px"><svg width="18" height="18" style="color:var(--muted);flex:none"><use href="#i-lock"/></svg><span class="grow tiny" style="color:var(--ink-2)">Your name, licence reference and states</span></div>
<div class="row" style="gap:10px"><svg width="18" height="18" style="color:var(--muted);flex:none"><use href="#i-lock"/></svg><span class="grow tiny" style="color:var(--ink-2)">On-time rate, rejections and your filing record</span></div>
<span class="tiny">These cannot be hidden. An owner is trusting an animal to you and the record is the basis of that trust.</span>
</div></div>
<div class="sect"><div class="sect__h"><h3>Your choice</h3></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Photograph</span><span class="tiny">Owners assigning in person recognise you at the gate</span></span><span class="badge badge--ok"><svg><use href="#i-check"/></svg>Shown</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Years supervising</span><span class="tiny">Since March 2025</span></span><span class="badge badge--ok"><svg><use href="#i-check"/></svg>Shown</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Written notes on your ratings</span><span class="tiny">The comments owners leave, not just the score</span></span><span class="badge"><svg><use href="#i-eye"/></svg>Hidden</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Other ranches you cover</span><span class="tiny">Lets an owner judge how thinly you are spread</span></span><span class="badge"><svg><use href="#i-eye"/></svg>Hidden</span></button>
</div></div>
<div class="card card--plain stack g3">
<div class="row" style="gap:10px"><svg width="19" height="19" style="color:var(--ok);flex:none"><use href="#i-shield"/></svg>
<span class="grow" style="font-size:14px;font-weight:700">Never shown to anyone</span></div>
<p class="sub" style="margin:0">Your address, phone number, bank account, permit documents and earnings. Owners message you through Andry and never see a contact detail.</p>
</div>
</div></div>''' + tabbar('sup', 4) + '''
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-30
add('C-30', 'Practice filing &mdash; nothing is filed',
    '<strong>Offered to applicants waiting on review at #104.</strong> The safest place to learn the '
    'filing standard is one where a mistake costs nothing. It is the real checklist with the real '
    'rejection reasons, marked throughout so it can never be mistaken for a live record &mdash; which '
    'is the one thing a practice mode must not get wrong.',
    ['Serves #104 <q>Practise a record</q>'],
    '<div class="phone">' + ST + '''
<div class="vp">
<div class="offline" style="background:var(--brand-soft);color:var(--brand)"><svg width="16" height="16"><use href="#i-eye"/></svg>Practice &mdash; nothing here is filed or paid</div>
''' + bar('Leave practice') + '''
<div class="scroll"><div class="pad pb stack g5">
<div class="card stack g2">
<div class="spread"><span class="lbl">Practice animal</span><span class="badge badge--brand">Not real</span></div>
<div style="font-size:16px;font-weight:730">Sokoto Gudali bull</div>
<span class="mono tiny">DEMO-0001-XX &middot; pen 4 &middot; Ayalar Ranch</span>
</div>
<div class="sect" style="margin-top:2px"><div class="sect__h"><h3>The eight-point record</h3><span class="tiny mono">3 of 8</span></div>
<div class="card card--plain stack g4">
<div class="row" style="gap:11px"><svg width="19" height="19" style="color:var(--ok);flex:none"><use href="#i-checkc"/></svg>
<span class="grow"><span style="display:block;font-size:14px;font-weight:660">Tag photograph</span><span class="tiny" style="color:var(--ok)">Accepted &mdash; all characters legible</span></span></div>
<div class="row" style="gap:11px"><svg width="19" height="19" style="color:var(--ok);flex:none"><use href="#i-checkc"/></svg>
<span class="grow"><span style="display:block;font-size:14px;font-weight:660">Animal, full body, left side</span><span class="tiny" style="color:var(--ok)">Accepted</span></span></div>
<div class="row" style="gap:11px"><svg width="19" height="19" style="color:var(--risk);flex:none"><use href="#i-close"/></svg>
<span class="grow"><span style="display:block;font-size:14px;font-weight:660">Weight on the scale</span><span class="tiny" style="color:var(--risk)">Rejected &mdash; the reading is out of frame. This is the single most common rejection: 41% of all of them.</span></span></div>
<div class="row" style="gap:11px"><svg width="19" height="19" style="color:var(--faint);flex:none"><use href="#i-camera"/></svg>
<span class="grow"><span style="display:block;font-size:14px;font-weight:660;color:var(--muted)">Body condition score</span><span class="tiny">Not started</span></span></div>
</div></div>
<div class="card stack g3" style="border-color:var(--brand)">
<div class="row" style="gap:10px"><svg width="19" height="19" style="color:var(--brand);flex:none"><use href="#i-info"/></svg>
<span class="grow" style="font-size:14px;font-weight:700">Why that one failed</span></div>
<p class="sub" style="margin:0">An adjudicator has to read the number without taking your word for it. Stand square to the scale, get the whole display in shot, and take it before the animal steps off &mdash; not after.</p>
<button class="btn btn--sm btn--secondary">Try that step again</button>
</div>
<p class="tiny" style="margin:0;padding:11px 12px;background:var(--surface-2);border-radius:var(--radius)">Practise as often as you like. Nothing is filed, no owner is notified, no payment is made and none of it touches your standing.</p>
</div></div>
<div class="actionbar"><button class="btn btn--primary btn--block">Continue the practice record</button></div>
''' + tabbar('sup', 0) + '''
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-31
add('C-31', 'Raise an issue on this animal',
    '<strong>The welfare escape hatch on #111, which opened onto nothing.</strong> It is offered '
    'mid-visit with the animal in front of the supervisor, so the screen is built for one hand and a '
    'short attention span: severity first because it decides who is called, then a photograph, then '
    'everything else.',
    ['Serves #111'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to the checklist') + '''
<div class="scroll"><div class="pad pb stack g5">
<div class="card card--tight row" style="gap:10px">
<div class="av av--sq av--md" style="background:var(--surface-3)"></div>
<span class="grow"><span style="display:block;font-size:14px;font-weight:680">Sokoto Gudali, bull</span><span class="mono tiny">AND-4471-KX &middot; pen 4</span></span>
</div>
<div class="sect" style="margin-top:0"><div class="sect__h"><h3>How bad is it?</h3></div>
<div class="stack g2">
<button class="listitem" style="border:1.5px solid var(--risk);border-radius:var(--radius);padding:13px;background:var(--risk-soft)">
<svg width="21" height="21" style="color:var(--risk);flex:none"><use href="#i-alert"/></svg>
<span class="grow"><span style="display:block;font-size:14.5px;font-weight:700;color:var(--risk)">Down, bleeding or not breathing right</span><span class="tiny" style="color:var(--ink-2)">Calls the on-call vet now and tells the ranch. Do not file a record.</span></span></button>
<button class="listitem" style="border:1px solid var(--line-2);border-radius:var(--radius);padding:13px">
<svg width="21" height="21" style="color:var(--warn);flex:none"><use href="#i-alert"/></svg>
<span class="grow"><span style="display:block;font-size:14.5px;font-weight:700">Lame, thin, or off its feed</span><span class="tiny">Vet visit booked within 48 hours. File the record as normal.</span></span></button>
<button class="listitem" style="border:1px solid var(--line-2);border-radius:var(--radius);padding:13px">
<svg width="21" height="21" style="color:var(--muted);flex:none"><use href="#i-info"/></svg>
<span class="grow"><span style="display:block;font-size:14.5px;font-weight:700">Something the owner should know</span><span class="tiny">Logged on the animal. No vet, no escalation.</span></span></button>
</div></div>
<div class="sect"><div class="sect__h"><h3>Photograph it</h3></div>
<div style="border:1.5px dashed var(--line-2);border-radius:var(--radius-lg);padding:22px 18px;text-align:center">
<svg width="30" height="30" style="color:var(--faint)"><use href="#i-camera"/></svg>
<p class="tiny" style="margin:8px 0 0">One clear photograph of what you are describing. It goes to the vet before they set off.</p></div>
</div>
<label class="field"><span class="field__l">What you can see</span>
<input class="input" value="Not putting weight on the near hind leg. Standing away from the trough."></label>
<div class="card card--plain stack g3">
<div class="row" style="gap:10px"><svg width="19" height="19" style="color:var(--ok);flex:none"><use href="#i-shield"/></svg>
<span class="grow" style="font-size:14px;font-weight:700">Raising this never counts against you</span></div>
<p class="sub" style="margin:0">A visit that ends in an issue instead of a record is still a completed visit and is paid as one. Supervisors who raise issues early are the ones we keep.</p>
</div>
</div></div>
<div class="actionbar"><button class="btn btn--primary btn--block">Raise the issue</button>
<button class="btn btn--ghost btn--block" style="margin-top:6px">Cancel &mdash; go back to filing</button></div>
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-32
add('C-32', 'Earnings statement &mdash; supervisor',
    '<strong>#121 summarises and links to sixty-one entries.</strong> A statement, not a feed: each line '
    'reconciles to an assignment, and the deductions are itemised rather than netted off. A supervisor '
    'querying their pay needs to point at the row they disagree with.',
    ['Serves #121 <q>All 61</q>'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to earnings', right='<button class="appbar__btn" aria-label="Export"><svg width="24" height="24"><use href="#i-download"/></svg></button>') + '''
<div class="pad" style="padding-bottom:12px"><div class="chips">
<button class="chip is-on">August<span class="chip__n">6</span></button>
<button class="chip">July<span class="chip__n">6</span></button>
<button class="chip">June<span class="chip__n">5</span></button>
<button class="chip">All<span class="chip__n">61</span></button>
</div></div>
<div class="scroll"><div class="pad pb stack g4">
<div class="card stack g3">
<div class="spread"><span class="lbl">August, so far</span><span class="tiny">paid 07 Sep</span></div>
<span class="money money--xl">&#8358;27,000.00</span>
<hr class="hr" style="margin:0"/>
<div class="spread"><span class="tiny">6 assignments</span><span class="money money--sm">&#8358;27,000.00</span></div>
<div class="spread"><span class="tiny">Late deductions</span><span class="money money--sm">&#8358;0.00</span></div>
</div>
<div class="sect" style="margin-top:2px"><div class="sect__h"><h3>Every line</h3></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14px;font-weight:660">AND-4471-KX &middot; Sokoto Gudali</span><span class="tiny">Filed 02 Aug, on time &middot; Ayalar, pen 4</span></span><span class="money money--sm">&#8358;4,500.00</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14px;font-weight:660">AND-3902-QT &middot; White Fulani</span><span class="tiny">Filed 01 Aug, on time &middot; Ayalar, pen 2</span></span><span class="money money--sm">&#8358;4,500.00</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14px;font-weight:660">AND-5188-BV &middot; Kalahari Red</span><span class="tiny">Filed 29 Jul, on time &middot; Ilesa Highland</span></span><span class="money money--sm">&#8358;4,500.00</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14px;font-weight:660">AND-6014-PD &middot; Bunaji heifer</span><span class="tiny" style="color:var(--warn)">Filed 28 Jul, 1 day late &middot; &minus;&#8358;1,350.00 deducted 07 Aug</span></span><span class="money money--sm">&#8358;3,150.00</span></button>
</div></div>
<div class="card card--plain stack g3">
<div class="row" style="gap:10px"><svg width="19" height="19" style="color:var(--muted);flex:none"><use href="#i-scale"/></svg>
<span class="grow" style="font-size:14px;font-weight:700">How a late deduction works</span></div>
<p class="sub" style="margin:0">30% of the fee for that assignment, once, however late it is. It is not applied when the ranch was closed, when the vet held the animal, or when you raised an issue instead.</p>
<button class="btn btn--sm btn--secondary">Query a line</button>
</div>
</div></div>''' + tabbar('sup', 3) + '''
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-33
add('C-33', 'Notification settings &mdash; supervisor',
    '<strong>A different set from the owner&rsquo;s at #51.</strong> Visit reminders, owner messages, '
    'marketing. The reminders that protect a supervisor&rsquo;s standing are marked as such and cannot '
    'be turned off entirely &mdash; only moved &mdash; because a missed record is the one thing this '
    'screen can genuinely prevent.',
    ['Serves #124 <q>Notifications</q>'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to settings') + '''
<div class="scroll"><div class="pad pb stack g5">
<div class="sect" style="margin-top:6px"><div class="sect__h"><h3>Visits</h3></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">The evening before</span><span class="tiny">18:00, listing tomorrow&rsquo;s animals and pens</span></span><span class="badge badge--ok"><svg><use href="#i-check"/></svg>On</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Morning of</span><span class="tiny">06:30</span></span><span class="badge badge--ok"><svg><use href="#i-check"/></svg>On</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Six hours before a record is late</span><span class="tiny" style="color:var(--ink-2)">Protects your on-time rate &mdash; you can move the time, not remove it</span></span><span class="badge badge--brand"><svg><use href="#i-lock"/></svg>Always on</span></button>
</div></div>
<div class="sect"><div class="sect__h"><h3>Assignments</h3></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">New assignment offered</span><span class="tiny">Expires in 96 hours if you do not answer</span></span><span class="badge badge--ok"><svg><use href="#i-check"/></svg>On</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">An owner revoked you</span><span class="tiny">Always sent by email as well</span></span><span class="badge badge--ok"><svg><use href="#i-check"/></svg>On</span></button>
</div></div>
<div class="sect"><div class="sect__h"><h3>Owners</h3></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Messages from owners</span><span class="tiny">Quiet 21:00 to 06:30 &mdash; nothing wakes you</span></span><span class="badge badge--ok"><svg><use href="#i-check"/></svg>On</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">A rating was left</span><span class="tiny">Weekly summary rather than each one</span></span><span class="badge badge--ok"><svg><use href="#i-check"/></svg>Weekly</span></button>
</div></div>
<div class="sect"><div class="sect__h"><h3>From Andry</h3></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Filing standard changes</span><span class="tiny">Rare, and worth reading</span></span><span class="badge badge--ok"><svg><use href="#i-check"/></svg>On</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Marketing and new features</span><span class="tiny">Off</span></span><span class="badge"><svg><use href="#i-close"/></svg>Off</span></button>
</div></div>
<p class="tiny" style="margin:0">Permit expiry and licence decisions are sent by email and SMS whatever is set here. They are not marketing.</p>
</div></div>''' + tabbar('sup', 4) + '''
</div><div class="hi"></div></div>''')

# ================================================================ TRACK C
# ---------------------------------------------------------------- C-34
add('C-34', 'Capacity and species',
    '<strong>The setting that governs intake, and therefore the refusal already drawn at #138.</strong> '
    'Capacity is shown as used against declared, per species, because a ranch with room for cattle and '
    'none for goats is the ordinary case &mdash; a single total would hide exactly the constraint that '
    'blocks an arrival.',
    ['Serves #148', 'Governs #138'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to settings') + '''
<div class="scroll"><div class="pad pb stack g5">
<div class="card stack g3" style="margin-top:6px">
<div class="spread"><span class="lbl">Places used</span><span class="badge badge--warn"><svg><use href="#i-alert"/></svg>80% full</span></div>
<span class="money money--xl">1,284 <span style="font-size:18px;color:var(--muted);font-weight:600">of 1,600</span></span>
<div class="prog"><i style="width:80%"></i></div>
<span class="tiny">316 places free. Intake is refused automatically at 100%, per species.</span>
</div>
<div class="sect" style="margin-top:2px"><div class="sect__h"><h3>By species</h3></div>
<div class="card card--plain stack g4">
<div class="stack g2">
<div class="spread"><span style="font-size:14px;font-weight:680">Cattle</span><span class="mono tiny" style="color:var(--ink-2)">912 of 1,000</span></div>
<div class="prog"><i style="width:91%"></i></div>
</div>
<div class="stack g2">
<div class="spread"><span style="font-size:14px;font-weight:680">Goats</span><span class="mono tiny" style="color:var(--risk)">400 of 400 &mdash; full</span></div>
<div class="prog"><i style="width:100%;background:var(--risk)"></i></div>
</div>
<div class="stack g2">
<div class="spread"><span style="font-size:14px;font-weight:680">Sheep</span><span class="mono tiny" style="color:var(--ink-2)">0 of 200</span></div>
<div class="prog"><i style="width:0%"></i></div>
</div>
</div></div>
<div class="card stack g3" style="border-color:var(--warn);background:var(--warn-soft)">
<div class="row" style="gap:10px"><svg width="19" height="19" style="color:var(--warn);flex:none"><use href="#i-alert"/></svg>
<span class="grow" style="font-size:14px;font-weight:700;color:var(--warn)">Goats are full and 4 are booked in</span></div>
<p class="sub" style="margin:0;color:var(--ink-2)">Two arrivals on 19 Aug will be refused unless places free up or you raise the declared number. Raising it needs an inspection.</p>
</div>
<div class="sect"><div class="sect__h"><h3>Declared capacity</h3></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Cattle &middot; 1,000</span><span class="tiny">Set at inspection, 14 Feb 2025</span></span><span class="badge"><svg><use href="#i-lock"/></svg>Inspected</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Goats &middot; 400</span><span class="tiny">Set at inspection, 14 Feb 2025</span></span><span class="badge"><svg><use href="#i-lock"/></svg>Inspected</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Sheep &middot; 200</span><span class="tiny">Declared but never stocked</span></span><span class="badge"><svg><use href="#i-lock"/></svg>Inspected</span></button>
</div></div>
<p class="tiny" style="margin:0;padding:11px 12px;background:var(--surface-2);border-radius:var(--radius)">Capacity is a welfare figure, not a business one. It is set by an inspector against pen area, water and shade, and only an inspector can raise it.</p>
</div></div>
<div class="actionbar"><button class="btn btn--secondary btn--block">Request a capacity re-inspection</button></div>
''' + tabbar('host', 4) + '''
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-35
add('C-35', 'Staff and gate access',
    '<strong>The permission model behind the escrow confirmations at #139 to #142.</strong> Who may '
    'confirm a transfer is the single most consequential setting a ranch holds, so the screen separates '
    'confirming from handling and states plainly that one person holding both is a risk the ranch owns.',
    ['Serves #148', 'Governs #139&ndash;#142'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to settings', right='<button class="appbar__btn" aria-label="Add someone"><svg width="24" height="24"><use href="#i-plus"/></svg></button>') + '''
<div class="scroll"><div class="pad pb stack g5">
<p class="sub" style="margin:6px 0 0">Three people. Only one can confirm that an animal has arrived, which is what releases a buyer&rsquo;s money.</p>
<div class="list">
<button class="listitem"><div class="av av--md" style="background:var(--brand-soft);color:var(--brand)">OA</div>
<span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Olusegun Ayalar</span><span class="tiny">Owner &middot; added 14 Feb 2025</span>
<div class="row" style="gap:5px;margin-top:5px"><span class="badge badge--ok"><svg><use href="#i-check"/></svg>Can confirm</span><span class="badge"><svg><use href="#i-scan"/></svg>Tag reader</span></div></span>
<svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
<button class="listitem"><div class="av av--md" style="background:var(--surface-3);color:var(--muted)">IB</div>
<span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Ibrahim Bala</span><span class="tiny">Herdsman &middot; added 03 Mar 2025</span>
<div class="row" style="gap:5px;margin-top:5px"><span class="badge"><svg><use href="#i-scan"/></svg>Tag reader</span></div></span>
<svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
<button class="listitem"><div class="av av--md" style="background:var(--surface-3);color:var(--muted)">FO</div>
<span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Funmi Okoro</span><span class="tiny">Gate office &middot; added 21 Jun 2026</span>
<div class="row" style="gap:5px;margin-top:5px"><span class="badge"><svg><use href="#i-scan"/></svg>Tag reader</span><span class="badge badge--warn"><svg><use href="#i-clock"/></svg>Not used in 30 days</span></div></span>
<svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
</div>
<div class="card card--plain stack g3">
<div class="row" style="gap:10px"><svg width="19" height="19" style="color:var(--warn);flex:none"><use href="#i-alert"/></svg>
<span class="grow" style="font-size:14px;font-weight:700">One person can confirm</span></div>
<p class="sub" style="margin:0">If Olusegun is away, no arrival can be confirmed and every escrow waits. Adding a second person is the fix; it is your call, and it is also your risk if that person confirms an animal that is not there.</p>
</div>
<div class="sect" style="margin-top:2px"><div class="sect__h"><h3>Recent gate activity</h3><a href="#">All</a></div>
<div class="tl">
<div class="tlitem"><div class="spread"><span style="font-size:13.5px;font-weight:650">Ibrahim Bala scanned AND-6014-PD</span><span class="tiny mono">today 08:12</span></div></div>
<div class="tlitem tlitem--past"><div class="spread"><span class="sub">Olusegun confirmed 2 arrivals</span><span class="tiny mono">03 Aug 16:40</span></div></div>
<div class="tlitem tlitem--past"><div class="spread"><span class="sub">Funmi Okoro added</span><span class="tiny mono">21 Jun 09:02</span></div></div>
</div></div>
</div></div>''' + tabbar('host', 4) + '''
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-36
add('C-36', 'Payout account &mdash; ranch',
    '<strong>A company account, which is why it may not simply reuse the owner form.</strong> #148 names '
    'it and nothing opens. The check is against the registered company rather than a personal ID, and '
    'the screen says which document settled it &mdash; a ranch changing bank details is the classic '
    'invoice-fraud target and the audit trail is the defence.',
    ['Serves #148', 'Company, not personal'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to settings') + '''
<div class="scroll"><div class="pad pb stack g5">
<div class="card card--brand stack g2">
<span class="lbl">Next payment</span>
<span class="money money--xl">&#8358;486,000.00</span>
<span class="fx" style="color:rgba(255,255,255,.72)">07 Sep 2026 &middot; keep on 1,284 animals for August</span>
</div>
<div class="verify">
<div class="verify__top">
<svg width="20" height="20" style="color:var(--ok);flex:none"><use href="#i-checkc"/></svg>
<div class="grow"><div style="font-size:13.5px;font-weight:700;color:var(--ok)">Matches the registered company</div>
<div class="tiny" style="color:var(--ok)">Checked against CAC certificate RC 1102884</div></div>
</div>
<div class="verify__row"><span class="k">Bank</span><span class="grow v">Zenith Bank</span></div>
<div class="verify__row"><span class="k">Account</span><span class="grow mono" style="font-weight:650;color:var(--ink)">&bull;&bull;&bull;&bull;8814</span></div>
<div class="verify__row"><span class="k">Name</span><span class="grow v">AYALAR RANCH LIMITED</span></div>
<div class="verify__row" style="align-items:flex-start">
<svg width="18" height="18" style="color:var(--muted);flex:none;margin-top:2px"><use href="#i-info"/></svg>
<span class="grow tiny">A personal account cannot be used, even the owner&rsquo;s. Keep and escrow money belongs to the company that signed the hosting agreement.</span>
</div>
</div>
<div class="card stack g3" style="border-color:var(--warn);background:var(--warn-soft)">
<div class="row" style="gap:10px"><svg width="19" height="19" style="color:var(--warn);flex:none"><use href="#i-shield"/></svg>
<span class="grow" style="font-size:14px;font-weight:700;color:var(--warn)">Changing this takes 5 working days</span></div>
<p class="sub" style="margin:0;color:var(--ink-2)">A new account is confirmed by a call to the number on your CAC record, not to any number given with the request. Payouts continue to the old account until it clears. This is the commonest fraud against ranches and the delay is the defence.</p>
</div>
<div class="sect" style="margin-top:2px"><div class="sect__h"><h3>Changes to this account</h3></div>
<div class="tl">
<div class="tlitem tlitem--past"><div class="spread"><span class="sub">Set at onboarding</span><span class="tiny mono">14 Feb 2025</span></div>
<span class="tiny">Confirmed by Olusegun Ayalar with CAC certificate and a bank letter.</span></div>
</div></div>
</div></div>
<div class="actionbar"><button class="btn btn--secondary btn--block">Request a change</button></div>
''' + tabbar('host', 4) + '''
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-37
add('C-37', 'Inspection reports &mdash; all',
    '<strong>#147 links to four reports going back to February 2025.</strong> Only one report plate '
    'exists, #25, and it is the owner-facing view. This is the ranch&rsquo;s own history, with open '
    'actions surfaced above closed reports because an outstanding remedy is the only thing here with a '
    'deadline.',
    ['Serves #147 <q>All inspection reports</q>'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to compliance', right='<button class="appbar__btn" aria-label="Export"><svg width="24" height="24"><use href="#i-download"/></svg></button>') + '''
<div class="scroll"><div class="pad pb stack g5">
<div class="card stack g3" style="border-color:var(--warn);background:var(--warn-soft);margin-top:6px">
<div class="spread"><span class="lbl" style="color:var(--warn)">Open action</span>
<span class="cd"><b>17</b><i>d</i><b>04</b><i>h</i><b>30</b><i>m</i></span></div>
<span style="font-size:14.5px;font-weight:700;color:var(--warn)">Shade over pens A-01 to A-04</span>
<p class="sub" style="margin:0;color:var(--ink-2)">Raised 21 Jul 2026 &middot; due 21 Aug 2026. Photographs of the finished work close it without a visit.</p>
<button class="btn btn--sm btn--primary">Send photographs</button>
</div>
<div class="sect" style="margin-top:2px"><div class="sect__h"><h3>Reports</h3><span class="tiny">4 since Feb 2025</span></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">21 Jul 2026 &middot; Routine</span><span class="tiny">Inspector Dr. Bello Aminu &middot; 1 action raised</span></span>
<span class="badge badge--warn"><svg><use href="#i-clock"/></svg>1 open</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">04 Feb 2026 &middot; Routine</span><span class="tiny">Inspector Grace Aondona &middot; no actions</span></span>
<span class="badge badge--ok"><svg><use href="#i-check"/></svg>Passed</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">18 Aug 2025 &middot; Capacity</span><span class="tiny">Raised the goat pen limit from 250 to 400</span></span>
<span class="badge badge--ok"><svg><use href="#i-check"/></svg>Passed</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">14 Feb 2025 &middot; Onboarding</span><span class="tiny">Set capacity at 1,600 places across three species</span></span>
<span class="badge badge--ok"><svg><use href="#i-check"/></svg>Passed</span></button>
</div></div>
<div class="card card--plain stack g3">
<div class="row" style="gap:10px"><svg width="19" height="19" style="color:var(--muted);flex:none"><use href="#i-eye"/></svg>
<span class="grow" style="font-size:14px;font-weight:700">Owners see these too</span></div>
<p class="sub" style="margin:0">Every owner with an animal here can read the full report, including open actions. Hiding one would be worth less than the trust it costs.</p>
</div>
</div></div>''' + tabbar('host', 4) + '''
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-38
add('C-38', 'Earnings statement &mdash; host',
    '<strong>#144 summarises and links to thirty-seven entries.</strong> Same shape as the '
    'supervisor&rsquo;s on the host&rsquo;s own figures, with the two things a ranch actually queries '
    'shown as lines rather than a net: keep on animals that arrived mid-month, and keep withheld on an '
    'animal under a welfare hold.',
    ['Serves #144 <q>All 37</q>'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to earnings', right='<button class="appbar__btn" aria-label="Export"><svg width="24" height="24"><use href="#i-download"/></svg></button>') + '''
<div class="pad" style="padding-bottom:12px"><div class="chips">
<button class="chip is-on">August<span class="chip__n">4</span></button>
<button class="chip">July<span class="chip__n">4</span></button>
<button class="chip">All<span class="chip__n">37</span></button>
</div></div>
<div class="scroll"><div class="pad pb stack g4">
<div class="card stack g3">
<div class="spread"><span class="lbl">August, so far</span><span class="tiny">paid 07 Sep</span></div>
<span class="money money--xl">&#8358;486,000.00</span>
<hr class="hr" style="margin:0"/>
<div class="spread"><span class="tiny">Keep &middot; 1,284 animals</span><span class="money money--sm">&#8358;489,600.00</span></div>
<div class="spread"><span class="tiny">Withheld &middot; 1 welfare hold</span><span class="money money--sm" style="color:var(--risk)">&minus;&#8358;3,600.00</span></div>
</div>
<div class="sect" style="margin-top:2px"><div class="sect__h"><h3>Every line</h3></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14px;font-weight:660">Keep &middot; cattle, 912 head</span><span class="tiny">Full month &middot; &#8358;420.00 each</span></span><span class="money money--sm">&#8358;383,040.00</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14px;font-weight:660">Keep &middot; goats, 400 head</span><span class="tiny">Full month &middot; &#8358;260.00 each</span></span><span class="money money--sm">&#8358;104,000.00</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14px;font-weight:660">Keep &middot; 6 arrivals</span><span class="tiny">Part month from 19 Jul, pro rata</span></span><span class="money money--sm">&#8358;2,560.00</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14px;font-weight:660">Withheld &middot; AND-5188-BV</span><span class="tiny" style="color:var(--risk)">Welfare hold from 28 Jul &mdash; released when the vet clears it</span></span><span class="money money--sm" style="color:var(--risk)">&minus;&#8358;3,600.00</span></button>
</div></div>
<div class="card card--plain stack g3">
<div class="row" style="gap:10px"><svg width="19" height="19" style="color:var(--muted);flex:none"><use href="#i-scale"/></svg>
<span class="grow" style="font-size:14px;font-weight:700">Withheld is not lost</span></div>
<p class="sub" style="margin:0">Keep on an animal under a welfare hold is held, not cancelled, and is paid in the run after the vet clears it. If the hold becomes a removal, it is not paid.</p>
<button class="btn btn--sm btn--secondary">Query a line</button>
</div>
</div></div>''' + tabbar('host', 3) + '''
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-39
add('C-39', 'Notification settings &mdash; ranch',
    '<strong>#148 states that escrow, arrivals and supervisor visits are always on.</strong> That is a '
    'policy, and a policy deserves a screen that explains it. Everything that moves money or an animal '
    'is fixed; everything else is the ranch&rsquo;s to switch, including the routing that decides whether '
    'the gate office is woken at 02:00.',
    ['Serves #148 <q>Notifications</q>'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to settings') + '''
<div class="scroll"><div class="pad pb stack g5">
<div class="card card--tight row" style="gap:10px;margin-top:6px">
<svg width="19" height="19" style="color:var(--brand);flex:none"><use href="#i-lock"/></svg>
<span class="grow tiny">Anything that moves money or an animal is always on. Those alerts are the record that the ranch was told.</span>
</div>
<div class="sect" style="margin-top:0"><div class="sect__h"><h3>Always on</h3></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Escrow waiting on your confirmation</span><span class="tiny">A buyer&rsquo;s money is held until you act</span></span><span class="badge badge--brand"><svg><use href="#i-lock"/></svg>Fixed</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Animals arriving or leaving</span><span class="tiny">Including a transfer you have not accepted</span></span><span class="badge badge--brand"><svg><use href="#i-lock"/></svg>Fixed</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Supervisor visits and welfare holds</span><span class="tiny">Including an issue raised at the pen</span></span><span class="badge badge--brand"><svg><use href="#i-lock"/></svg>Fixed</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Inspection actions and deadlines</span><span class="tiny">At 14 days, 7 days and 24 hours</span></span><span class="badge badge--brand"><svg><use href="#i-lock"/></svg>Fixed</span></button>
</div></div>
<div class="sect"><div class="sect__h"><h3>Your choice</h3></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Owner messages</span><span class="tiny">Quiet 20:00 to 06:00</span></span><span class="badge badge--ok"><svg><use href="#i-check"/></svg>On</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Capacity above 90%</span><span class="tiny">Warns before an arrival is refused</span></span><span class="badge badge--ok"><svg><use href="#i-check"/></svg>On</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Monthly earnings summary</span><span class="tiny">On the 7th, with the payment</span></span><span class="badge badge--ok"><svg><use href="#i-check"/></svg>On</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Marketing from Andry</span><span class="tiny">Off</span></span><span class="badge"><svg><use href="#i-close"/></svg>Off</span></button>
</div></div>
<div class="sect"><div class="sect__h"><h3>Who gets woken</h3></div>
<div class="card card--plain stack g3">
<div class="spread"><span class="sub"><b style="color:var(--ink)">Olusegun Ayalar</b> &middot; owner</span><span class="tiny">Everything, any hour</span></div>
<div class="spread"><span class="sub"><b style="color:var(--ink)">Funmi Okoro</b> &middot; gate office</span><span class="tiny">Arrivals only, 06:00 to 20:00</span></div>
<span class="tiny">An overnight arrival still reaches Olusegun. Nothing is silently dropped because the gate office is closed.</span>
</div></div>
</div></div>''' + tabbar('host', 4) + '''
</div><div class="hi"></div></div>''')
