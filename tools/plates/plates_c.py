# -*- coding: utf-8 -*-
"""Tier-2 plates C-14 to C-26 — track A, the owner."""
from plates_a import ST

_TABS = {
    'owner': [('i-home', 'Home'), ('i-market', 'Market'), ('i-portfolio', 'Portfolio'),
              ('i-activity', 'Activity'), ('i-profile', 'Profile')],
    'sup':   [('i-home', 'Today'), ('i-pin', 'Visits'), ('i-msg', 'Messages'),
              ('i-wallet', 'Earnings'), ('i-profile', 'Profile')],
    'host':  [('i-home', 'Ranch'), ('i-portfolio', 'Herd'), ('i-msg', 'Messages'),
              ('i-wallet', 'Earnings'), ('i-profile', 'Profile')],
}


def tabbar(kind, active):
    out = ['<div class="tabbar">']
    for i, (ico, lab) in enumerate(_TABS[kind]):
        on = ' is-on' if i == active else ''
        out.append('<button class="tabbar__i%s"><svg><use href="#%s"/></svg><span>%s</span></button>'
                   % (on, ico, lab))
    out.append('</div>')
    return ''.join(out)


def bar(title, back='Back', right=''):
    return ('<div class="appbar">'
            '<button class="appbar__btn" aria-label="%s"><svg width="24" height="24">'
            '<use href="#i-back"/></svg></button>'
            '<div class="appbar__title">%s</div>%s</div>' % (back, title, right))


PLATES = []


def add(pid, title, caption, tags, frame):
    PLATES.append(dict(id=pid, title=title, caption=caption, tags=tags, frame=frame))


# ---------------------------------------------------------------- C-14
add('C-14', 'Support &mdash; talk to a person',
    '<strong>Three plates offer a human; none showed the channel.</strong> #12 even publishes opening '
    'hours and a four-minute response time. The queue position and the wait are given as facts rather '
    'than a spinner, and the alternative is offered in the same breath &mdash; a person who cannot wait '
    'eleven minutes should be told what else works before they sit through it.',
    ['Serves #12, #20, #44'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to help', right='<button class="appbar__btn" aria-label="More"><svg width="24" height="24"><use href="#i-more"/></svg></button>') + '''
<div class="scroll"><div class="pad pb stack g5">
<div class="card card--brand stack g2">
<span class="lbl">You are in the queue</span>
<div class="spread" style="align-items:baseline">
<span class="money money--lg">3rd</span>
<span class="cd" style="color:#fff"><b style="color:#fff">00</b><i style="color:rgba(255,255,255,.7)">d</i><b style="color:#fff">00</b><i style="color:rgba(255,255,255,.7)">h</i><b style="color:#fff">11</b><i style="color:rgba(255,255,255,.7)">m</i></span>
</div>
<span class="fx" style="color:rgba(255,255,255,.72)">Longer than usual. Two reviewers are on lunch until 13:00.</span>
</div>
<div class="card card--plain stack g3">
<span class="lbl">What we already know</span>
<div class="verify__row" style="padding:0;border:0"><span class="k">About</span><span class="grow v">KYC could not be verified</span></div>
<div class="verify__row" style="padding:0;border:0"><span class="k">Reference</span><span class="grow mono" style="font-weight:650;color:var(--ink)">AND-SUP-2026-8841</span></div>
<div class="verify__row" style="padding:0;border:0"><span class="k">Attempts</span><span class="grow v">2 of 3 used, last 04 Aug 09:52</span></div>
<span class="tiny">You will not be asked to repeat any of this.</span>
</div>
<div class="sect">
<div class="sect__h"><h3>Faster than waiting</h3></div>
<div class="list">
<button class="listitem"><span class="av av--sq av--md" style="background:var(--brand-soft);color:var(--brand)"><svg width="21" height="21"><use href="#i-doc"/></svg></span>
<span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Which documents are accepted</span><span class="tiny">Answers 6 in 10 of these calls</span></span>
<svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
<button class="listitem"><span class="av av--sq av--md" style="background:var(--surface-3);color:var(--muted)"><svg width="21" height="21"><use href="#i-refresh"/></svg></span>
<span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Try the upload again</span><span class="tiny">A clearer photograph clears most rejections</span></span>
<svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
</div></div>
<p class="tiny" style="margin:0;padding:11px 12px;background:var(--surface-2);border-radius:var(--radius)">Leave this screen and you keep your place &mdash; we send a notification when a reviewer picks it up. Andry will never ask for your password or a card number in this chat.</p>
</div></div>
<div class="actionbar">
<div class="row" style="gap:9px">
<input class="input" value="" placeholder="Type your message">
<button class="btn btn--primary" style="min-height:50px;padding:0 16px"><svg width="19" height="19"><use href="#i-send"/></svg><span class="sr">Send</span></button>
</div>
<button class="btn btn--ghost btn--block" style="margin-top:6px">Ask for a callback instead</button>
</div>
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-15
add('C-15', 'Help &mdash; all articles',
    '<strong>#77 shows four articles and links to sixty-two.</strong> The index groups by the moment a '
    'person is in rather than by department, which is what a support taxonomy usually optimises for. '
    'Counts are shown per group so the size of each subject is legible before tapping into it.',
    ['Serves #77 <q>All 62</q>'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to help') + '''
<div class="pad" style="padding-bottom:12px">
<div class="inputwrap"><input class="input" value="" placeholder="Search 62 articles"><span class="reveal" style="pointer-events:none"><svg width="19" height="19" style="color:var(--faint)"><use href="#i-search"/></svg></span></div>
</div>
<div class="pad" style="padding-bottom:12px"><div class="chips">
<button class="chip is-on">All<span class="chip__n">62</span></button>
<button class="chip">Money<span class="chip__n">18</span></button>
<button class="chip">Your animal<span class="chip__n">15</span></button>
<button class="chip">Account<span class="chip__n">12</span></button>
<button class="chip">Selling<span class="chip__n">9</span></button>
<button class="chip">Trouble<span class="chip__n">8</span></button>
</div></div>
<div class="scroll"><div class="pad pb">
<div class="sect" style="margin-top:0"><div class="sect__h"><h3>Read most this week</h3></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Proof of life is late</span><span class="tiny">What Andry does at 24 hours, 72 hours and 7 days overdue</span></span><svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">I cannot withdraw</span><span class="tiny">Holds, unverified bank accounts and the &#8358;500.00 minimum</span></span><svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">KYC was rejected</span><span class="tiny">The four reasons it fails, and how to resubmit without waiting</span></span><svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
</div></div>
<div class="sect"><div class="sect__h"><h3>Money</h3><a href="#">All 18</a></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">How long a bank transfer takes</span><span class="tiny">And what to do when the reference was left off</span></span><svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Every fee, in one place</span><span class="tiny">Card, withdrawal, commission and what the host takes</span></span><svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
</div></div>
<div class="sect"><div class="sect__h"><h3>Your animal</h3><a href="#">All 15</a></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">What a supervisor actually checks</span><span class="tiny">The eight-point weekly record, and what fails it</span></span><svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">If your animal dies</span><span class="tiny">Insurance, the 10% excess, and the 30 to 45 day wait</span></span><svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
</div></div>
</div></div>''' + tabbar('owner', 4) + '''
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-16
add('C-16', 'Help &mdash; article',
    '<strong>No plate in the run renders article body copy</strong>, which orphans all sixty-two rows on '
    '#77. One screen serves them all. It opens with the answer instead of a preamble, and closes by '
    'asking whether it worked &mdash; the only signal that tells anyone which of the sixty-two are '
    'earning their place.',
    ['Serves #77 rows, #12'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to articles', right='<button class="appbar__btn" aria-label="Share"><svg width="24" height="24"><use href="#i-share"/></svg></button>') + '''
<div class="scroll"><div class="pad pb stack g5">
<div class="stack g2" style="margin-top:2px">
<span class="badge badge--brand">Your animal</span>
<h2 style="margin:0;font-size:24px;line-height:1.2;letter-spacing:-.026em;font-weight:780">Proof of life is late. What happens now?</h2>
<span class="tiny">Updated 12 Jul 2026 &middot; 2 min read</span>
</div>
<div class="card stack g2">
<span class="lbl">Short answer</span>
<p style="margin:0;font-size:14.5px;line-height:1.55;color:var(--ink-2)">Nothing happens to your units. The supervisor is chased at 24 hours, replaced at 7 days, and you are told at every step. You do not need to do anything.</p>
</div>
<div class="stack g4">
<div class="stack g2">
<h3 style="margin:0;font-size:16px;font-weight:730">At 24 hours</h3>
<p style="margin:0;font-size:14px;line-height:1.6;color:var(--ink-2)">The supervisor gets a reminder and the animal is marked <b style="color:var(--ink)">Proof overdue</b> on your portfolio. Most records land the same day; a late visit is usually a bad road, not a bad animal.</p>
</div>
<div class="stack g2">
<h3 style="margin:0;font-size:16px;font-weight:730">At 72 hours</h3>
<p style="margin:0;font-size:14px;line-height:1.6;color:var(--ink-2)">The host is asked to confirm the animal is on site, independently of the supervisor. That confirmation is logged and you can read it. The supervisor&rsquo;s on-time rate takes the hit.</p>
</div>
<div class="stack g2">
<h3 style="margin:0;font-size:16px;font-weight:730">At 7 days</h3>
<p style="margin:0;font-size:14px;line-height:1.6;color:var(--ink-2)">The assignment is pulled and reassigned to another supervisor within 48 hours, at no cost to you. If the host also cannot confirm, the animal is treated as a possible loss and the claims desk opens a case without waiting for you to ask.</p>
</div>
</div>
<div class="card card--plain stack g3">
<div class="row" style="gap:10px"><svg width="19" height="19" style="color:var(--brand);flex:none"><use href="#i-bell"/></svg>
<span class="grow" style="font-size:14px;font-weight:700">You can turn the chasing off</span></div>
<p class="sub" style="margin:0">Some owners would rather not hear about a one-day delay. Notification settings has a switch for overdue alerts; the escalation still happens either way.</p>
</div>
<div class="card stack g3">
<span style="font-size:14px;font-weight:700">Did this answer it?</span>
<div class="row" style="gap:9px">
<button class="btn btn--secondary" style="flex:1">Yes</button>
<button class="btn btn--secondary" style="flex:1">No</button>
</div>
<span class="tiny">If not, the next screen puts you in the queue with this article attached.</span>
</div>
</div></div>''' + tabbar('owner', 4) + '''
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-17
add('C-17', 'Support &mdash; my requests',
    '<strong>#77 links to a history that does not exist.</strong> Every row carries the state and the '
    'clock, because the question a person opens this screen with is always <q>is anyone still looking '
    'at this</q>. A closed request keeps its outcome rather than disappearing.',
    ['Serves #77 <q>History</q>'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to help') + '''
<div class="pad" style="padding-bottom:6px"><div class="tabs">
<button class="tab is-on">Open<span class="n">2</span></button>
<button class="tab">Closed<span class="n">7</span></button>
</div></div>
<div class="scroll"><div class="pad pb stack g4">
<div class="card stack g3" style="margin-top:14px">
<div class="spread" style="align-items:flex-start">
<div class="grow"><span style="display:block;font-size:15px;font-weight:700">KYC could not be verified</span>
<span class="mono tiny">AND-SUP-2026-8841 &middot; raised 04 Aug, 09:58</span></div>
<span class="badge badge--warn"><svg><use href="#i-clock"/></svg>With a reviewer</span>
</div>
<hr class="hr" style="margin:0"/>
<div class="row" style="gap:11px;align-items:flex-start">
<div class="av av--sm" style="background:var(--brand-soft);color:var(--brand)">YB</div>
<span class="sub grow"><b style="color:var(--ink)">Yusuf Bello</b> replied 24 minutes ago &mdash; &ldquo;The address on the levy receipt is cut off at the bottom edge. Send the same document with all four corners visible and I will clear it today.&rdquo;</span>
</div>
<button class="btn btn--primary btn--block btn--sm">Reply and attach a document</button>
</div>
<div class="card stack g3">
<div class="spread" style="align-items:flex-start">
<div class="grow"><span style="display:block;font-size:15px;font-weight:700">Payment failed twice on the same card</span>
<span class="mono tiny">AND-SUP-2026-8802 &middot; raised 02 Aug, 16:20</span></div>
<span class="badge badge--info"><svg><use href="#i-send"/></svg>With your bank</span>
</div>
<span class="sub">We raised this with Guaranty Trust on your behalf on 03 Aug. Banks answer these in 5 to 10 working days and we chase on day 6.</span>
<div class="spread"><span class="tiny">Next chase</span><span class="cd"><b>02</b><i>d</i><b>04</b><i>h</i><b>30</b><i>m</i></span></div>
</div>
<div class="state" style="padding:26px 6px 4px">
<p style="max-width:34ch">Closed requests keep their outcome for two years, including anything a reviewer decided and why.</p>
</div>
</div></div>''' + tabbar('owner', 4) + '''
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-18
add('C-18', 'Security',
    '<strong>A profile row naming three surfaces at once.</strong> #15 and #16 exist for enrolment and '
    'recovery, but the hub that reaches them and the device list do not. Sessions are the part people '
    'come here for &mdash; a stranger&rsquo;s device is the thing they are hunting &mdash; so it is '
    'shown with place, time and a single-tap end, not buried under a settings list.',
    ['Serves #92 <q>Security</q>'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to profile') + '''
<div class="scroll"><div class="pad pb stack g5">
<div class="sect" style="margin-top:6px"><div class="sect__h"><h3>Signing in</h3></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Password</span><span class="tiny">Changed 21 Jul 2026</span></span><svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Two-factor</span><span class="tiny">Authenticator app &middot; 8 recovery codes left</span></span><span class="badge badge--ok"><svg><use href="#i-check"/></svg>On</span><svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Face ID on this phone</span><span class="tiny">Opens the app; never authorises a payout on its own</span></span><span class="badge badge--ok"><svg><use href="#i-check"/></svg>On</span><svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
</div></div>
<div class="sect"><div class="sect__h"><h3>Where you are signed in</h3><a href="#">End all others</a></div>
<div class="card card--plain stack g4">
<div class="row" style="gap:11px">
<svg width="20" height="20" style="color:var(--ok);flex:none"><use href="#i-checkc"/></svg>
<span class="grow"><span style="display:block;font-size:14px;font-weight:680">iPhone 13 &middot; this device</span><span class="tiny">Ibadan &middot; active now</span></span>
</div>
<div class="row" style="gap:11px">
<svg width="20" height="20" style="color:var(--muted);flex:none"><use href="#i-card"/></svg>
<span class="grow"><span style="display:block;font-size:14px;font-weight:680">Chrome on Windows</span><span class="tiny">Lagos &middot; last used 21 Jul, 14:08</span></span>
<button class="btn btn--sm btn--secondary" style="min-height:40px">End</button>
</div>
<div class="row" style="gap:11px">
<svg width="20" height="20" style="color:var(--risk);flex:none"><use href="#i-alert"/></svg>
<span class="grow"><span style="display:block;font-size:14px;font-weight:680">Android &middot; Tecno Spark</span><span class="tiny" style="color:var(--risk)">Kano &middot; first seen 03 Aug, 23:41 &mdash; you have not used this before</span></span>
<button class="btn btn--sm btn--secondary" style="min-height:40px">End</button>
</div>
</div></div>
<div class="card stack g3">
<div class="row" style="gap:10px"><svg width="19" height="19" style="color:var(--muted);flex:none"><use href="#i-info"/></svg>
<span class="grow" style="font-size:14px;font-weight:700">What ending a session does</span></div>
<p class="sub" style="margin:0">It signs that device out immediately. It does not change your password, and it does not stop someone who knows it from signing back in &mdash; change the password too if you do not recognise a device.</p>
</div>
<div class="sect"><div class="sect__h"><h3>Recent security events</h3><a href="#">All 24</a></div>
<div class="tl">
<div class="tlitem"><div class="spread"><span style="font-size:13.5px;font-weight:650">New device signed in &mdash; Kano</span><span class="tiny mono">03 Aug 23:41</span></div></div>
<div class="tlitem tlitem--past"><div class="spread"><span class="sub">Password changed</span><span class="tiny mono">21 Jul 14:02</span></div></div>
<div class="tlitem tlitem--past"><div class="spread"><span class="sub">Two-factor turned on</span><span class="tiny mono">02 Jun 08:19</span></div></div>
</div></div>
</div></div>''' + tabbar('owner', 4) + '''
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-19
add('C-19', 'Currency &amp; region',
    '<strong>Named on the profile menu with its current value, and drawn nowhere.</strong> Every money '
    'figure in the product depends on the rate this screen governs, so the screen says plainly what '
    'changing the display currency does <em>not</em> do: it does not change what you hold, and it does '
    'not change what a withdrawal pays.',
    ['Serves #92 <q>Currency &amp; region</q>'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to profile') + '''
<div class="scroll"><div class="pad pb stack g5">
<div class="sect" style="margin-top:6px"><div class="sect__h"><h3>You hold and settle in</h3></div>
<div class="card card--brand stack g2">
<span class="lbl">Account currency</span>
<span class="money money--lg">Naira &middot; &#8358;</span>
<span class="fx" style="color:rgba(255,255,255,.72)">Fixed at sign-up and cannot be changed. Units are bought, sold and paid out in Naira.</span>
</div></div>
<div class="sect"><div class="sect__h"><h3>Also show prices in</h3></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">US dollar &middot; $</span><span class="tiny">Alongside every figure, in smaller type</span></span><span class="badge badge--ok"><svg><use href="#i-check"/></svg>On</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Pound sterling &middot; &pound;</span><span class="tiny">Off</span></span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Nothing &mdash; Naira only</span><span class="tiny">Off</span></span></button>
</div></div>
<div class="card card--plain stack g3">
<div class="spread"><span class="lbl">Rate used</span><span class="mono" style="font-weight:650;color:var(--ink)">1,562.60</span></div>
<span class="tiny">Central Bank of Nigeria mid-rate, refreshed at 09:00 WAT daily and stamped on every receipt. A second currency is a reference only &mdash; nothing is converted, held or paid in it.</span>
</div>
<div class="sect"><div class="sect__h"><h3>Region</h3></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Country</span><span class="tiny">Nigeria &middot; set by your verified ID</span></span><span class="badge"><svg><use href="#i-lock"/></svg>Fixed</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Language</span><span class="tiny">English</span></span><svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Time zone</span><span class="tiny">West Africa Time &middot; UTC+1</span></span><svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
</div></div>
<p class="tiny" style="margin:0">Hausa and Yoruba are being translated and will appear here when the whole product is covered, not before.</p>
</div></div>''' + tabbar('owner', 4) + '''
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-20
add('C-20', 'Points statement',
    '<strong>#95 promises a dated ledger of every credit and redemption.</strong> Built as a statement '
    'rather than a feed, so it reconciles: an opening balance, dated movements with a running total, '
    'and the expiry that most points schemes bury.',
    ['Serves #95 <q>Points statement</q>'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to rewards', right='<button class="appbar__btn" aria-label="Export"><svg width="24" height="24"><use href="#i-download"/></svg></button>') + '''
<div class="pad" style="padding-bottom:12px"><div class="chips">
<button class="chip is-on">All<span class="chip__n">31</span></button>
<button class="chip">Earned<span class="chip__n">24</span></button>
<button class="chip">Spent<span class="chip__n">7</span></button>
</div></div>
<div class="scroll"><div class="pad pb stack g4">
<div class="card stack g2">
<div class="spread"><span class="lbl">Balance today</span><span class="badge badge--gold"><svg><use href="#i-star"/></svg>Silver</span></div>
<span class="money money--xl">3,480</span>
<div class="spread"><span class="tiny">2,150 expire 31 Dec 2026</span><span class="delta delta--up">+380 this month</span></div>
</div>
<div class="sect" style="margin-top:2px"><div class="sect__h"><h3>August 2026</h3><span class="tiny mono">Running total</span></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14px;font-weight:660">Bought 20 units &middot; AND-4471-KX</span><span class="tiny">04 Aug 2026 &middot; 1 point per &#8358;1,000.00</span></span>
<span style="text-align:right;flex:none"><span class="money money--sm" style="display:block;color:var(--ok)">+191</span><span class="tiny mono">3,480</span></span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14px;font-weight:660">Redeemed &mdash; one free withdrawal</span><span class="tiny">02 Aug 2026 &middot; used 03 Aug</span></span>
<span style="text-align:right;flex:none"><span class="money money--sm" style="display:block;color:var(--risk)">&minus;1,000</span><span class="tiny mono">3,289</span></span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14px;font-weight:660">Ifeanyi Eze completed KYC</span><span class="tiny">01 Aug 2026 &middot; referral bonus</span></span>
<span style="text-align:right;flex:none"><span class="money money--sm" style="display:block;color:var(--ok)">+500</span><span class="tiny mono">4,289</span></span></button>
</div></div>
<div class="sect"><div class="sect__h"><h3>July 2026</h3></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14px;font-weight:660">Held units 90 days &middot; AND-3902-QT</span><span class="tiny">28 Jul 2026 &middot; loyalty credit</span></span>
<span style="text-align:right;flex:none"><span class="money money--sm" style="display:block;color:var(--ok)">+250</span><span class="tiny mono">3,789</span></span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14px;font-weight:660">Points expired unused</span><span class="tiny">01 Jul 2026 &middot; earned Jul 2024</span></span>
<span style="text-align:right;flex:none"><span class="money money--sm" style="display:block;color:var(--muted)">&minus;120</span><span class="tiny mono">3,539</span></span></button>
</div></div>
<p class="tiny" style="margin:0;padding:11px 12px;background:var(--surface-2);border-radius:var(--radius)">Points expire two years after they are earned, oldest spent first. They have no cash value and cannot be transferred or withdrawn.</p>
</div></div>''' + tabbar('owner', 4) + '''
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-21
add('C-21', 'Reward redemption &mdash; confirm',
    '<strong>#95 has four priced buttons and nothing between the tap and the spend.</strong> The sheet '
    'states the balance after, not just the cost, and names where the reward will actually appear. '
    'Reversibility is the honest part: this one cannot be undone, so it says so above the button.',
    ['Serves #95 redemption buttons'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to rewards') + '''
<div class="scroll"><div class="pad pb stack g4" style="opacity:.45" aria-hidden="true">
<div class="card stack g2"><span class="lbl">Balance today</span><span class="money money--xl">3,480</span></div>
<div class="sect"><div class="sect__h"><h3>Redeem</h3></div>
<div class="card card--plain"><div class="spread"><span style="font-size:14px;font-weight:660">One free withdrawal</span><button class="btn btn--sm btn--secondary">1,000 pts</button></div></div></div>
</div></div>
<div class="scrim"></div>
<div class="sheet">
<div class="sheet__grab"></div>
<div class="stack g4">
<div class="stack g2">
<h3 style="margin:0;font-size:19px;font-weight:760;letter-spacing:-.02em">Spend 1,000 points?</h3>
<p class="sub" style="margin:0">One free withdrawal, on top of the 4 free ones you have left this month.</p>
</div>
<div class="card card--plain stack g2">
<div class="spread"><span class="tiny">Balance now</span><span class="money money--sm">3,480</span></div>
<div class="spread"><span class="tiny">This redemption</span><span class="money money--sm" style="color:var(--risk)">&minus;1,000</span></div>
<hr class="hr" style="margin:2px 0"/>
<div class="spread"><span style="font-size:13.5px;font-weight:680">Balance after</span><span class="money money--lg">2,480</span></div>
</div>
<div class="row" style="gap:9px;padding:11px 12px;background:var(--warn-soft);border-radius:var(--radius)">
<svg width="18" height="18" style="color:var(--warn);flex:none"><use href="#i-alert"/></svg>
<span class="tiny" style="color:var(--warn)">Redemptions cannot be reversed and points cannot be bought back.</span>
</div>
<span class="tiny">The credit appears in Payment methods within a minute and is used automatically on your next withdrawal. It expires 90 days from today.</span>
<div class="stack g2">
<button class="btn btn--primary btn--block">Redeem 1,000 points</button>
<button class="btn btn--ghost btn--block">Keep my points</button>
</div>
</div>
</div>
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-22
add('C-22', 'Referrals &mdash; all',
    '<strong>#94 summarises and links to the full list.</strong> The state of each invitee is the whole '
    'content: a referral pays on verified identity, not on sign-up, so anyone stuck at <em>joined</em> '
    'is money the referrer has not been paid. Naming that state is more useful than a total.',
    ['Serves #94 <q>View all</q>'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to referrals') + '''
<div class="pad" style="padding-bottom:6px"><div class="tabs">
<button class="tab is-on">Paid<span class="n">6</span></button>
<button class="tab">Waiting<span class="n">3</span></button>
<button class="tab">Lapsed<span class="n">2</span></button>
</div></div>
<div class="scroll"><div class="pad pb stack g4">
<div class="card stack g2" style="margin-top:14px">
<div class="spread"><span class="lbl">Earned from referrals</span><span class="tiny">11 invited</span></div>
<span class="money money--xl">3,000 pts</span>
<span class="fx">500 points each, paid when they finish identity verification</span>
</div>
<div class="list">
<button class="listitem"><div class="av av--md" style="background:var(--brand-soft);color:var(--brand)">IE</div>
<span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Ifeanyi Eze</span><span class="tiny">Verified 01 Aug 2026 &middot; joined 28 Jul</span></span>
<span class="money money--sm" style="color:var(--ok)">+500</span></button>
<button class="listitem"><div class="av av--md" style="background:var(--brand-soft);color:var(--brand)">HM</div>
<span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Hauwa Mohammed</span><span class="tiny">Verified 24 Jul 2026 &middot; joined 22 Jul</span></span>
<span class="money money--sm" style="color:var(--ok)">+500</span></button>
<button class="listitem"><div class="av av--md" style="background:var(--surface-3);color:var(--muted)">BS</div>
<span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Bola Salami</span><span class="tiny" style="color:var(--warn)">Joined 03 Aug &mdash; identity not finished</span></span>
<span class="badge badge--warn"><svg><use href="#i-clock"/></svg>Waiting</span></button>
<button class="listitem"><div class="av av--md" style="background:var(--surface-3);color:var(--muted)">MA</div>
<span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Musa Aliyu</span><span class="tiny">Invited 12 Jun &middot; never opened the link</span></span>
<span class="badge"><svg><use href="#i-clock"/></svg>Lapsed</span></button>
</div>
<div class="card card--plain stack g3">
<div class="row" style="gap:10px"><svg width="19" height="19" style="color:var(--muted);flex:none"><use href="#i-info"/></svg>
<span class="grow" style="font-size:14px;font-weight:700">Three are waiting on their own verification</span></div>
<p class="sub" style="margin:0">Nothing you can do speeds it up, and nudging people about it is the fastest way to be reported as spam. An invitation lapses 60 days after it is sent.</p>
</div>
<button class="btn btn--secondary btn--block">Share your code &middot; TAIWO-4471</button>
</div></div>''' + tabbar('owner', 4) + '''
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-23
add('C-23', 'Pedigree certificate',
    '<strong>#26 shows three generations and offers the certificate itself.</strong> It is a trust '
    'artefact, so it is drawn as a document with an issuer, a reference and a verification route rather '
    'than as an app screen &mdash; and it states which lines are attested and which are declared by the '
    'host, because a pedigree that hides its weakest link is worth nothing.',
    ['Serves #26 <q>View full pedigree certificate</q>'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to genealogy', right='<button class="appbar__btn" aria-label="Download as PDF"><svg width="24" height="24"><use href="#i-download"/></svg></button>') + '''
<div class="scroll"><div class="pad pb stack g5">
<div class="card stack g3" style="border-color:var(--line-2)">
<div class="spread" style="align-items:flex-start">
<div><span class="lbl">Certificate of pedigree</span>
<div style="font-size:19px;font-weight:760;letter-spacing:-.02em;margin-top:4px">Sokoto Gudali bull</div>
<span class="mono tiny">AND-4471-KX</span></div>
<svg width="34" height="34" style="color:var(--brand);flex:none"><use href="#i-dna"/></svg>
</div>
<hr class="hr" style="margin:0"/>
<div class="verify__row" style="padding:0;border:0"><span class="k">Issued by</span><span class="grow v">Ayalar Ranch, Oyo State</span></div>
<div class="verify__row" style="padding:0;border:0"><span class="k">Reference</span><span class="grow mono" style="font-weight:650;color:var(--ink)">PED-4471-2026-03</span></div>
<div class="verify__row" style="padding:0;border:0"><span class="k">Born</span><span class="grow v">approx. March 2024</span></div>
</div>
<div class="verify">
<div class="verify__top">
<svg width="20" height="20" style="color:var(--ok);flex:none"><use href="#i-shield"/></svg>
<div class="grow"><div style="font-size:13.5px;font-weight:700;color:var(--ok)">Two generations attested</div>
<div class="tiny" style="color:var(--ok)">By Dr. Bello Aminu, NVMA 14822, on 02 Mar 2026</div></div>
</div>
<div class="verify__row" style="align-items:flex-start">
<svg width="18" height="18" style="color:var(--muted);flex:none;margin-top:2px"><use href="#i-info"/></svg>
<span class="grow tiny">The third generation is declared by the host from its own herd book and is not independently attested. It is shown because withholding it would be worse, not because it carries the same weight.</span>
</div>
</div>
<div class="sect" style="margin-top:2px"><div class="sect__h"><h3>Line</h3></div>
<div class="tl">
<div class="tlitem"><div class="spread"><span style="font-size:14px;font-weight:680">Sire &middot; AND-2201-GB</span><span class="badge badge--ok"><svg><use href="#i-check"/></svg>Attested</span></div>
<span class="tiny">Sokoto Gudali &middot; Ayalar Ranch &middot; 14 recorded offspring</span></div>
<div class="tlitem"><div class="spread"><span style="font-size:14px;font-weight:680">Dam &middot; AND-1988-WF</span><span class="badge badge--ok"><svg><use href="#i-check"/></svg>Attested</span></div>
<span class="tiny">White Fulani cross &middot; Ayalar Ranch &middot; 6 recorded offspring</span></div>
<div class="tlitem tlitem--past"><div class="spread"><span class="sub">Grand-sire &middot; unregistered</span><span class="badge"><svg><use href="#i-doc"/></svg>Declared</span></div>
<span class="tiny">Named in the Ayalar herd book, entry 2019/114. No Andry record.</span></div>
</div></div>
<div class="card card--plain stack g3">
<div class="row" style="gap:11px">
<svg width="19" height="19" style="color:var(--brand);flex:none"><use href="#i-qr"/></svg>
<span class="grow"><span style="display:block;font-size:14px;font-weight:680">Anyone can check this certificate</span><span class="tiny">Scan the code on the printed copy, or enter the reference at andry.ng/verify</span></span>
</div>
<span class="tiny">Verification shows the reference, the issuer and the attesting vet. It does not show who owns units.</span>
</div>
</div></div>
<div class="actionbar"><button class="btn btn--secondary btn--block">Download (PDF, 640 KB)</button></div>
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-24
add('C-24', 'Supervisor directory',
    '<strong>#67 shows four candidates and links to twelve.</strong> The hosts directory at #71 is a '
    'different list. Sorting defaults to on-time filing rather than rating, because the rating is a '
    'popularity figure and the filing record is the thing an owner is actually buying.',
    ['Serves #67 <q>See all 12</q>'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to assign', right='<button class="appbar__btn" aria-label="Filter"><svg width="24" height="24"><use href="#i-filter"/></svg></button>') + '''
<div class="pad" style="padding-bottom:12px"><div class="chips">
<button class="chip is-on">On-time first</button>
<button class="chip">Nearest</button>
<button class="chip">Rating</button>
<button class="chip">Fee</button>
</div></div>
<div class="scroll"><div class="pad pb">
<p class="tiny" style="margin:0 0 12px">12 supervisors cover Ayalar Ranch. Verified means Andry has checked the licence, the bank account and two references.</p>
<div class="list">
<button class="listitem"><div class="av av--md" style="background:var(--brand-soft);color:var(--brand)">BN</div>
<span class="grow"><span class="row" style="gap:6px"><span style="font-size:14.5px;font-weight:680">Bello Nurudeen</span><span class="badge badge--ok"><svg><use href="#i-shield"/></svg>Verified</span></span>
<span class="tiny">100% on time &middot; 132 ratings &middot; 44 herds &middot; Oyo State</span>
<span class="tiny mono" style="color:var(--ink-2)">&#8358;4,500.00 a month</span></span>
<svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
<button class="listitem"><div class="av av--md" style="background:var(--brand-soft);color:var(--brand)">GA</div>
<span class="grow"><span class="row" style="gap:6px"><span style="font-size:14.5px;font-weight:680">Grace Aondona</span><span class="badge badge--ok"><svg><use href="#i-shield"/></svg>Verified</span></span>
<span class="tiny">99% on time &middot; 76 ratings &middot; 33 herds &middot; Benue State</span>
<span class="tiny mono" style="color:var(--ink-2)">&#8358;4,200.00 a month</span></span>
<svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
<button class="listitem"><div class="av av--md" style="background:var(--brand-soft);color:var(--brand)">CO</div>
<span class="grow"><span class="row" style="gap:6px"><span style="font-size:14.5px;font-weight:680">Chiamaka Obi</span><span class="badge badge--ok"><svg><use href="#i-shield"/></svg>Verified</span></span>
<span class="tiny">97% on time &middot; 89 ratings &middot; 28 herds &middot; Osun State</span>
<span class="tiny mono" style="color:var(--ink-2)">&#8358;4,500.00 a month</span></span>
<svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
<button class="listitem"><div class="av av--md" style="background:var(--surface-3);color:var(--muted)">MS</div>
<span class="grow"><span class="row" style="gap:6px"><span style="font-size:14.5px;font-weight:680">Musa Sanni</span><span class="badge badge--warn"><svg><use href="#i-clock"/></svg>Checks pending</span></span>
<span class="tiny">94% on time &middot; 57 ratings &middot; 19 herds &middot; Kano State</span>
<span class="tiny mono" style="color:var(--ink-2)">&#8358;3,900.00 a month</span></span>
<svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
<button class="listitem"><div class="av av--md" style="background:var(--surface-3);color:var(--muted)">TA</div>
<span class="grow"><span class="row" style="gap:6px"><span style="font-size:14.5px;font-weight:680">Adekola Taiwo</span><span class="badge badge--risk"><svg><use href="#i-alert"/></svg>1 rejection</span></span>
<span class="tiny">91% on time &middot; 214 ratings &middot; 61 herds &middot; Oyo State</span>
<span class="tiny mono" style="color:var(--ink-2)">&#8358;4,800.00 a month</span></span>
<svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
</div>
<p class="tiny" style="margin:14px 0 0;padding:11px 12px;background:var(--surface-2);border-radius:var(--radius)">A supervisor with checks pending can still be assigned. They cannot file a record that counts until the checks clear.</p>
</div></div>''' + tabbar('owner', 2) + '''
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-25
add('C-25', 'Supervisor record &mdash; filings and ratings',
    '<strong>#68 cites 148 filings and 214 ratings as links, and neither opens.</strong> This is the '
    'evidence an owner wants before handing over an animal. The rejection is put first rather than '
    'buried at the bottom of a five-star average, because one rejection is the only entry on this '
    'screen that changes a decision.',
    ['Serves #68 <q>All 148</q>, <q>All 214</q>'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to supervisor') + '''
<div class="pad" style="padding-bottom:6px"><div class="tabs">
<button class="tab is-on">Filings<span class="n">148</span></button>
<button class="tab">Ratings<span class="n">214</span></button>
</div></div>
<div class="scroll"><div class="pad pb stack g4">
<div class="card stack g3" style="margin-top:14px">
<div class="spread"><span class="lbl">Filed on time</span><span class="money money--lg">91%</span></div>
<div class="prog"><i style="width:91%"></i></div>
<div class="spread"><span class="tiny">135 on time &middot; 12 late &middot; 1 rejected</span><span class="tiny">since 04 Mar 2025</span></div>
</div>
<div class="card stack g3" style="border-color:var(--risk);background:var(--risk-soft)">
<div class="row" style="gap:10px">
<svg width="19" height="19" style="color:var(--risk);flex:none"><use href="#i-alert"/></svg>
<span class="grow" style="font-size:14px;font-weight:700;color:var(--risk)">One record rejected &middot; 18 Jul 2026</span>
</div>
<p class="sub" style="margin:0;color:var(--ink-2)">The tag photograph did not show the full tag, so the adjudicator could not confirm which animal was weighed. Refiled correctly the same day and accepted.</p>
<button class="btn btn--sm btn--secondary">Read the adjudication</button>
</div>
<div class="sect" style="margin-top:2px"><div class="sect__h"><h3>Recent filings</h3></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14px;font-weight:660">AND-4471-KX &middot; Sokoto Gudali</span><span class="tiny">02 Aug 2026, 09:14 &middot; 412 kg &middot; Ayalar, pen 4</span></span>
<span class="badge badge--ok"><svg><use href="#i-check"/></svg>On time</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14px;font-weight:660">AND-3902-QT &middot; White Fulani</span><span class="tiny">01 Aug 2026, 17:40 &middot; 308 kg &middot; Ayalar, pen 2</span></span>
<span class="badge badge--warn"><svg><use href="#i-clock"/></svg>1 day late</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14px;font-weight:660">AND-5188-BV &middot; Kalahari Red</span><span class="tiny">29 Jul 2026, 08:02 &middot; 44 kg &middot; Ilesa Highland</span></span>
<span class="badge badge--ok"><svg><use href="#i-check"/></svg>On time</span></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14px;font-weight:660">AND-6014-PD &middot; Bunaji heifer</span><span class="tiny">28 Jul 2026, 10:31 &middot; 266 kg &middot; Ayalar, pen 4</span></span>
<span class="badge badge--ok"><svg><use href="#i-check"/></svg>On time</span></button>
</div></div>
<p class="tiny" style="margin:0">Filings older than 24 months are kept but not listed here. Every one of them is in the animal&rsquo;s own Proof of Life archive.</p>
</div></div>''' + tabbar('owner', 2) + '''
</div><div class="hi"></div></div>''')

# ---------------------------------------------------------------- C-26
add('C-26', 'Unit transfer &mdash; tracking',
    '<strong>#81 offers to track a transfer and the owner-side view was never drawn.</strong> The host '
    'confirmation plates at #139 to #142 are a different actor&rsquo;s screens. What the seller needs is '
    'the position of their money, so escrow state leads and the animal detail follows.',
    ['Serves #81 <q>Track unit transfer</q>'],
    '<div class="phone">' + ST + '''
<div class="vp">''' + bar('Back to offers') + '''
<div class="scroll"><div class="pad pb stack g5">
<div class="card card--brand stack g2">
<span class="lbl">Held in escrow for you</span>
<span class="money money--xl">&#8358;100,200.00</span>
<span class="fx" style="color:rgba(255,255,255,.72)">40 units &middot; AND-5188-BV &middot; buyer Ifeanyi Eze</span>
</div>
<div class="sect" style="margin-top:2px"><div class="sect__h"><h3>Where it has got to</h3></div>
<div class="tl">
<div class="tlitem tlitem--past"><div class="spread"><span class="sub">Offer accepted</span><span class="tiny mono">04 Aug 10:02</span></div>
<span class="tiny">Buyer&rsquo;s money moved into escrow the same minute.</span></div>
<div class="tlitem tlitem--past"><div class="spread"><span class="sub">Register updated</span><span class="tiny mono">04 Aug 10:03</span></div>
<span class="tiny">40 units moved from you to Ifeanyi Eze against the tag.</span></div>
<div class="tlitem"><div class="spread"><span style="font-size:14px;font-weight:680">Waiting on the ranch to confirm</span><span class="tiny mono">now</span></div>
<span class="tiny">Ayalar Ranch confirms the animal is on site and a supervisor scans the tag. Usually inside 4 hours during working hours.</span></div>
<div class="tlitem"><div class="spread"><span class="sub" style="color:var(--faint)">Money released to you</span><span class="tiny mono" style="color:var(--faint)">then</span></div>
<span class="tiny">Lands in your wallet immediately, not your bank.</span></div>
</div></div>
<div class="card card--plain stack g3">
<div class="spread">
<span class="row" style="gap:7px"><svg width="17" height="17" style="color:var(--warn);flex:none"><use href="#i-clock"/></svg><span class="tiny">Escrow reverses automatically if unconfirmed</span></span>
<span class="cd"><b>13</b><i>d</i><b>21</b><i>h</i><b>58</b><i>m</i></span>
</div>
<span class="tiny">If Ayalar cannot confirm within 14 days, the units come back to you and the buyer is refunded in full. Neither side is charged.</span>
</div>
<div class="sect"><div class="sect__h"><h3>If something is wrong</h3></div>
<div class="list">
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Message Ayalar Ranch</span><span class="tiny">Answered in about 4 hours, 08:00 to 18:00</span></span><svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
<button class="listitem"><span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Report a problem with this transfer</span><span class="tiny">Opens a dispute and freezes the escrow where it stands</span></span><svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
</div></div>
</div></div>''' + tabbar('owner', 3) + '''
</div><div class="hi"></div></div>''')
