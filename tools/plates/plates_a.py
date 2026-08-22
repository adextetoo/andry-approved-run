# -*- coding: utf-8 -*-
"""Plates C-01 to C-07 — onboarding, funding, identity, recovery."""

ST = ('<div class="st"><span>10:30</span><div class="st__notch"></div>'
      '<span class="st__r"><svg width="17" height="11" viewBox="0 0 17 11" fill="currentColor">'
      '<rect x="0" y="7" width="3" height="4" rx="1"/><rect x="4.5" y="5" width="3" height="6" rx="1"/>'
      '<rect x="9" y="2.5" width="3" height="8.5" rx="1"/><rect x="13.5" y="0" width="3" height="11" rx="1"/></svg>'
      '<svg width="24" height="11" viewBox="0 0 24 11" fill="none" stroke="currentColor" stroke-width="1.3">'
      '<rect x="1" y="1.5" width="18" height="8" rx="2.4"/>'
      '<rect x="2.8" y="3.3" width="12" height="4.4" rx="1.2" fill="currentColor" stroke="none"/>'
      '<path d="M21 4.3v2.4" stroke-linecap="round"/></svg></span></div>')

TABBAR_PROFILE = (
    '<div class="tabbar">'
    '<button class="tabbar__i"><svg><use href="#i-home"/></svg><span>Home</span></button>'
    '<button class="tabbar__i"><svg><use href="#i-market"/></svg><span>Market</span></button>'
    '<button class="tabbar__i"><svg><use href="#i-portfolio"/></svg><span>Portfolio</span></button>'
    '<button class="tabbar__i"><svg><use href="#i-activity"/></svg><span>Activity</span></button>'
    '<button class="tabbar__i is-on"><svg><use href="#i-profile"/></svg><span>Profile</span></button></div>')


def dots(active):
    out = ['<span class="sr">Step %d of 3</span>' % active]
    for i in (1, 2, 3):
        if i == active:
            out.append('<span aria-hidden="true" style="width:24px;height:7px;'
                       'border-radius:var(--radius-pill);background:var(--brand)"></span>')
        else:
            out.append('<span aria-hidden="true" style="width:7px;height:7px;'
                       'border-radius:var(--radius-pill);background:var(--line-2)"></span>')
    return ''.join(out)


def kyc(step):
    """Stepper for the KYC flow.

    #11 puts its step labels inside .kyc__l, which the system defines as a 2px
    connector line - the text overflows it and collides with the heading below.
    The same three labels are set here in a nowrap span sized to fit the frame,
    so the new plates do not inherit that collision. No CSS rule was changed;
    fixing #11 itself would need a stylesheet edit, which is out of scope.
    """
    lab = ('font-size:11.5px;line-height:1.2;white-space:nowrap;letter-spacing:-.005em')
    labels = [('Identity', 1), ('Address', 2), ('Bank', 3)]
    cells = []
    for name, n in labels:
        if n < step:
            cells.append('<div class="kyc__s"><span class="kyc__d" style="background:var(--ok);color:#fff">'
                         '<svg width="13" height="13"><use href="#i-check"/></svg></span>'
                         '<span style="%s;font-weight:640;color:var(--muted)">%s &middot; '
                         '<b style="color:var(--ok)">Done</b></span></div>' % (lab, name))
        elif n == step:
            cells.append('<div class="kyc__s"><span class="kyc__d" style="background:var(--brand);'
                         'color:var(--on-brand)">%d</span>'
                         '<span style="%s;font-weight:700;color:var(--ink)">%s &middot; Now</span></div>'
                         % (n, lab, name))
        else:
            cells.append('<div class="kyc__s"><span class="kyc__d">%d</span>'
                         '<span style="%s;font-weight:640;color:var(--faint)">%s &middot; Pending</span>'
                         '</div>' % (n, lab, name))
    return ('<div class="pad" style="padding-bottom:4px"><div class="kyc" style="gap:6px">'
            + ''.join(cells) + '</div></div>')


PLATES = []

# ---------------------------------------------------------------- C-01
PLATES.append(dict(
    id='C-01', title='Onboarding, slide 1 of 3', tier=1,
    caption='<strong>The premise, before the mechanics.</strong> Slide 2 explains how ownership works; '
            'this one has to earn the right to explain it. It names the thing the reader already knows '
            '&mdash; that a herd is how value has been stored here for generations &mdash; and then names '
            'the single part Andry supplies. The price of entry is stated on the first screen rather than '
            'discovered three taps later.',
    tags=['Sits before #1', 'Anchor <b>Duolingo</b>'],
    frame='''<div class="phone">''' + ST + '''
<div class="vp">
<div class="appbar">
<span class="appbar__title" style="font-size:13px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);padding-left:8px">Andry</span>
<button class="btn btn--ghost" style="min-height:44px;padding:0 14px;font-size:14px">Skip</button>
</div>
<div class="scroll"><div class="pad pb stack g6">
<div class="thumb" style="aspect-ratio:5/4;background:linear-gradient(152deg,#2A2350 0%,var(--brand-lo) 38%,#8A6A2E 78%,var(--gold) 100%)" role="img" aria-label="Illustration: a white Fulani bull at dawn, a tag visible on its ear"></div>
<div class="stack g4">
<h2 style="margin:0;font-size:26px;line-height:1.18;letter-spacing:-.028em;font-weight:790">Cattle have always been savings. The farm was the hard part.</h2>
<p style="margin:0;font-size:15px;line-height:1.5;color:var(--ink-2)">The land, the feed, someone you trust to stand over the animal. Andry supplies all three.</p>
</div>
<div class="card card--plain stack g3">
<div class="row" style="gap:10px">
<svg width="20" height="20" style="color:var(--brand);flex:none"><use href="#i-wallet"/></svg>
<span class="grow" style="font-size:13.5px;font-weight:640">A unit starts at <span class="money money--sm">&#8358;2,450.00</span>, not the price of a bull</span>
</div>
<div class="row" style="gap:10px">
<svg width="20" height="20" style="color:var(--brand);flex:none"><use href="#i-users"/></svg>
<span class="grow" style="font-size:13.5px;font-weight:640">One animal is split between up to 400 owners</span>
</div>
<div class="row" style="gap:10px">
<svg width="20" height="20" style="color:var(--brand);flex:none"><use href="#i-map"/></svg>
<span class="grow" style="font-size:13.5px;font-weight:640">15 ranches across 6 states, none of them yours</span>
</div>
</div>
</div></div>
<div class="actionbar">
<div class="stack g4">
<div class="row" style="justify-content:center;gap:7px">''' + dots(1) + '''</div>
<button class="btn btn--primary btn--block">Next</button>
</div>
<div class="hi"></div>
</div>
</div></div>'''))

# ---------------------------------------------------------------- C-02
PLATES.append(dict(
    id='C-02', title='Onboarding, slide 3 of 3', tier=1,
    caption='<strong>The hand-off.</strong> Where #1 leaves the reader with <q>Next</q> and nothing to land on. '
            'Three slides is a small budget, so the last one spends itself on the two questions that decide '
            'whether someone signs up: what happens to my money in the gap between paying and owning, and how '
            'do I get out. It offers the market as an alternative to signing up, because a person who is not '
            'ready should not be cornered.',
    tags=['Sits after #1', 'Hands off to #2 or #6'],
    frame='''<div class="phone">''' + ST + '''
<div class="vp">
<div class="appbar">
<span class="appbar__title" style="font-size:13px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);padding-left:8px">Andry</span>
<button class="btn btn--ghost" style="min-height:44px;padding:0 14px;font-size:14px">Skip</button>
</div>
<div class="scroll"><div class="pad stack g5">
<div class="thumb" style="aspect-ratio:5/4;background:linear-gradient(200deg,var(--brand-hi) 0%,var(--brand-lo) 44%,#1F6B4C 92%)" role="img" aria-label="Illustration: a supervisor photographing a tagged animal at a pen gate"></div>
<div class="stack g4">
<h2 style="margin:0;font-size:26px;line-height:1.18;letter-spacing:-.028em;font-weight:790">Your money waits in escrow. Your units are yours to sell.</h2>
</div>
<div class="card card--plain stack g4">
<div class="stack g2">
<div class="row" style="gap:10px">
<svg width="20" height="20" style="color:var(--ok);flex:none"><use href="#i-lock"/></svg>
<span class="grow" style="font-size:14.5px;font-weight:700">Before you own it</span>
</div>
<p class="sub" style="margin:0">Held in escrow until the ranch confirms the animal and the tag is scanned. If it never comes, your money returns in full.</p>
</div>
<div class="stack g2">
<div class="row" style="gap:10px">
<svg width="20" height="20" style="color:var(--brand);flex:none"><use href="#i-swap"/></svg>
<span class="grow" style="font-size:14.5px;font-weight:700">When you want out</span>
</div>
<p class="sub" style="margin:0">Sell to another owner, or hold to sale weight for a share of the proceeds. No buyer is guaranteed.</p>
</div>
</div>
<p class="tiny" style="margin:0">Andry is not a bank. Units are not protected by the NDIC.</p>
</div></div>
<div class="actionbar">
<div class="stack g4">
<div class="row" style="justify-content:center;gap:7px">''' + dots(3) + '''</div>
<div class="stack g2">
<button class="btn btn--primary btn--block">Create an account</button>
<button class="btn btn--ghost btn--block">Look at the market first</button>
</div>
</div>
<div class="hi"></div>
</div>
</div></div>'''))

# ---------------------------------------------------------------- C-03
PLATES.append(dict(
    id='C-03', title='Bank transfer &mdash; account and reference', tier=1,
    caption='<strong>The screen #18 promises by name.</strong> <q>Send to the account number shown on the next '
            'screen</q> had no next screen. The account is generated per transfer and expires, which is why the '
            'countdown is given the same weight as the number itself. The reference is the only thing tying a '
            'payment to a wallet, so it is copyable and the consequence of omitting it is stated plainly rather '
            'than left as a warning triangle.',
    tags=['Sits after #18', 'Anchor <b>Wise</b>'],
    frame='''<div class="phone">''' + ST + '''
<div class="vp">
<div class="appbar">
<button class="appbar__btn" aria-label="Back to Add funds"><svg width="24" height="24"><use href="#i-back"/></svg></button>
<div class="appbar__title">Bank transfer</div>
</div>
<div class="scroll"><div class="pad pb stack g5">
<div class="card card--brand stack g2">
<span class="lbl">Send exactly</span>
<span class="money money--xl">&#8358;100,000.00</span>
<span class="fx" style="color:rgba(255,255,255,.72)">Sending a different amount is fine &mdash; we credit what arrives.</span>
</div>
<div class="verify">
<div class="verify__top" style="background:var(--brand-soft)">
<svg width="20" height="20" style="color:var(--brand);flex:none"><use href="#i-bank"/></svg>
<div class="grow">
<div style="font-size:13.5px;font-weight:700;color:var(--brand)">Providus Bank</div>
<div class="tiny" style="color:var(--brand)">Andry holds this account for you alone</div>
</div>
</div>
<div class="verify__row">
<span class="k">Account</span>
<span class="grow mono" style="font-size:17px;font-weight:700;letter-spacing:.06em;color:var(--ink)">9911447102</span>
<button class="btn btn--sm btn--secondary" style="min-height:40px">Copy</button>
</div>
<div class="verify__row">
<span class="k">Name</span>
<span class="grow v">ANDRY CUSTODY / TAIWO ADEKOLA</span>
</div>
<div class="verify__row">
<span class="k">Reference</span>
<span class="grow mono" style="font-size:14px;font-weight:700;color:var(--ink)">AND-TOP-4471-KX</span>
<button class="btn btn--sm btn--secondary" style="min-height:40px">Copy</button>
</div>
</div>
<div class="card card--plain stack g3">
<div class="spread">
<span class="row" style="gap:7px"><svg width="17" height="17" style="color:var(--warn);flex:none"><use href="#i-clock"/></svg><span class="tiny">This account closes at 12:04</span></span>
<span class="cd"><b>00</b><i>d</i><b>01</b><i>h</i><b>34</b><i>m</i></span>
</div>
<span class="tiny">The number is issued for this transfer only. After it closes, money sent to it is returned by the bank in 3 to 5 working days and you start again.</span>
</div>
<div class="sect" style="margin-top:2px">
<div class="sect__h"><h3>Two things that will hold it up</h3></div>
<div class="card card--plain stack g3">
<div class="row" style="gap:11px;align-items:flex-start">
<svg width="19" height="19" style="color:var(--risk);flex:none;margin-top:2px"><use href="#i-alert"/></svg>
<span class="sub"><b style="color:var(--ink)">Sending from an account in another name.</b> It is returned, not credited. Your bank account must read <b style="color:var(--ink)">Taiwo Adekola</b>, the name on your ID.</span>
</div>
<div class="row" style="gap:11px;align-items:flex-start">
<svg width="19" height="19" style="color:var(--risk);flex:none;margin-top:2px"><use href="#i-doc"/></svg>
<span class="sub"><b style="color:var(--ink)">Leaving out the reference.</b> Without it we cannot tell which wallet the money belongs to and it sits unmatched until you contact us.</span>
</div>
</div>
</div>
<div class="row" style="gap:7px"><svg width="16" height="16" style="color:var(--muted)"><use href="#i-clock"/></svg><span class="tiny">Most transfers clear in 2 to 10 minutes. You do not need to stay on this screen.</span></div>
</div></div>
<div class="actionbar">
<button class="btn btn--primary btn--block">I have sent the transfer</button>
<button class="btn btn--ghost btn--block" style="margin-top:6px">Cancel this top-up</button>
<div class="hi"></div>
</div>
</div></div>'''))

# ---------------------------------------------------------------- C-04
PLATES.append(dict(
    id='C-04', title='KYC verification, step 1 of 3 &mdash; identity', tier=1,
    caption='<strong>The step #11 marks <q>Done</q>.</strong> It is the first thing a regulator asks for and the '
            'first time Andry asks for something genuinely sensitive, so the reason is given before the request. '
            'Document choice is a list rather than a dropdown because the trade-offs differ per document, and the '
            'one that verifies instantly is said so &mdash; people will pick it, which is the point.',
    tags=['Sits before #11', 'Anchor <b>Wise</b>'],
    frame='''<div class="phone">''' + ST + '''
<div class="vp">
<div class="appbar">
<button class="appbar__btn" aria-label="Back"><svg width="24" height="24"><use href="#i-back"/></svg></button>
<div class="appbar__title">Verify your identity</div>
</div>
''' + kyc(1) + '''
<div class="scroll"><div class="pad">
<h3 style="margin:14px 0 6px;font-size:18px;font-weight:750">Step 1 of 3: who you are</h3>
<p class="sub">Andry holds money and moves it on your behalf, so the law requires us to know who you are before your wallet opens. Three steps, about six minutes.</p>
<div class="card" style="margin-top:16px"><span class="lbl">Your NIN</span>
<label class="field" style="margin-top:8px"><span class="sr">National Identification Number</span>
<input class="input mono" style="letter-spacing:.14em;font-size:17px" value="7014 2288 41"></label>
<p class="tiny" style="margin-top:8px">Dial <span class="mono">*346#</span> from the number registered to you if you do not know it. We check the name attached to it against <b style="color:var(--ink)">Taiwo Adekola</b>.</p>
</div>
<div class="sect"><div class="sect__h"><h3>Add a photo ID</h3></div>
<div class="list">
<button class="listitem"><span class="av av--sq av--md" style="background:var(--brand-soft);color:var(--brand)"><svg width="22" height="22"><use href="#i-card"/></svg></span>
<span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">NIN slip or card</span><span class="tiny">Verifies instantly &mdash; most people finish here</span></span>
<span class="badge badge--ok">Fastest</span>
<svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
<button class="listitem"><span class="av av--sq av--md" style="background:var(--surface-3);color:var(--muted)"><svg width="22" height="22"><use href="#i-doc"/></svg></span>
<span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">International passport</span><span class="tiny">Reviewed by a person, usually inside 1 working day</span></span>
<svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
<button class="listitem"><span class="av av--sq av--md" style="background:var(--surface-3);color:var(--muted)"><svg width="22" height="22"><use href="#i-card"/></svg></span>
<span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Driver&rsquo;s licence</span><span class="tiny">Reviewed by a person, usually inside 1 working day</span></span>
<svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
<button class="listitem"><span class="av av--sq av--md" style="background:var(--surface-3);color:var(--muted)"><svg width="22" height="22"><use href="#i-users"/></svg></span>
<span class="grow"><span style="display:block;font-size:14.5px;font-weight:680">Voter&rsquo;s card</span><span class="tiny">Reviewed by a person &mdash; worn cards are often rejected</span></span>
<svg width="20" height="20" style="color:var(--faint);flex:none"><use href="#i-chev"/></svg></button>
</div></div>
<p class="tiny" style="margin-top:16px;padding:11px 12px;background:var(--surface-2);border-radius:var(--radius)">Your document is encrypted in transit and at rest, seen only by our verification team, and never shown to hosts, supervisors or other owners. We delete it 90 days after your account closes. <a href="#">How we handle your data</a></p>
</div><div class="pb"></div></div>
<div class="actionbar"><button class="btn btn--primary btn--block">Continue</button>
<button class="btn btn--ghost btn--block" style="margin-top:6px">Do this later</button></div>
''' + TABBAR_PROFILE + '''
</div><div class="hi"></div></div>'''))

# ---------------------------------------------------------------- C-05
PLATES.append(dict(
    id='C-05', title='KYC verification, step 3 of 3 &mdash; bank', tier=1,
    caption='<strong>The step #11 marks <q>Pending</q>, and the one that prevents #90.</strong> Andry already draws '
            'a plate for a withdrawal blocked on a name mismatch; this is where that mismatch is caught while it is '
            'still cheap. Resolving the account name before the user commits turns a rule into a visible check, so '
            'the match is shown rather than asserted.',
    tags=['Sits after #11', 'Prevents #90'],
    frame='''<div class="phone">''' + ST + '''
<div class="vp">
<div class="appbar">
<button class="appbar__btn" aria-label="Back"><svg width="24" height="24"><use href="#i-back"/></svg></button>
<div class="appbar__title">Verify your identity</div>
</div>
''' + kyc(3) + '''
<div class="scroll"><div class="pad">
<h3 style="margin:14px 0 6px;font-size:18px;font-weight:750">Step 3 of 3: where money returns to</h3>
<p class="sub">Money can only leave Andry to an account in your own name. Setting that account now is what stops a withdrawal being blocked later, when you actually want the cash.</p>
<div class="sect"><div class="sect__h"><h3>Your bank account</h3></div>
<div class="stack g4">
<label class="field"><span class="field__l">Bank <span class="req">*</span></span>
<div class="row" style="gap:0"><input class="input" value="Guaranty Trust Bank" style="border-top-right-radius:0;border-bottom-right-radius:0"><button class="btn btn--secondary" style="min-height:50px;border-radius:0 var(--radius) var(--radius) 0;border-left:0;padding:0 14px"><svg width="18" height="18"><use href="#i-chev"/></svg></button></div></label>
<label class="field"><span class="field__l">Account number <span class="req">*</span></span>
<input class="input mono" style="letter-spacing:.1em" value="0148832041"></label>
</div>
</div>
<div class="verify" style="margin-top:16px">
<div class="verify__top">
<svg width="20" height="20" style="color:var(--ok);flex:none"><use href="#i-checkc"/></svg>
<div class="grow">
<div style="font-size:13.5px;font-weight:700;color:var(--ok)">The name matches your ID</div>
<div class="tiny" style="color:var(--ok)">Checked with the bank just now</div>
</div>
</div>
<div class="verify__row"><span class="k">On the account</span><span class="grow v">TAIWO ADEKOLA</span></div>
<div class="verify__row"><span class="k">On your ID</span><span class="grow v">Taiwo Adekola</span></div>
</div>
<div class="card card--plain stack g3" style="margin-top:16px">
<div class="row" style="gap:10px">
<svg width="19" height="19" style="color:var(--muted);flex:none"><use href="#i-info"/></svg>
<span class="grow" style="font-size:14px;font-weight:700">If the names differ</span>
</div>
<p class="sub" style="margin:0">A middle name or an abbreviation is fine and we accept it. A different person is not &mdash; joint accounts and a spouse&rsquo;s account cannot be used, even with permission. You can change this account later from Payment methods.</p>
</div>
<p class="tiny" style="margin-top:16px">You can still add funds and buy without this step, but you will not be able to withdraw until it is done.</p>
</div><div class="pb"></div></div>
<div class="actionbar"><button class="btn btn--primary btn--block">Finish verification</button></div>
''' + TABBAR_PROFILE + '''
</div><div class="hi"></div></div>'''))

# ---------------------------------------------------------------- C-06
PLATES.append(dict(
    id='C-06', title='Reset password &mdash; request', tier=1,
    caption='<strong>The entrance #9 assumes.</strong> The run had the confirmation but nowhere to type the address. '
            'The screen deliberately does not confirm whether an account exists at that address &mdash; that would '
            'tell a stranger who banks here &mdash; and it says so, because an unexplained non-answer reads as a bug.',
    tags=['Sits before #9', 'Serves #8 <q>Forgot password?</q>'],
    frame='''<div class="phone">''' + ST + '''
<div class="vp">
<div class="appbar">
<button class="appbar__btn" aria-label="Back to sign in"><svg width="24" height="24"><use href="#i-back"/></svg></button>
<span class="appbar__title">Reset password</span>
</div>
<div class="scroll"><div class="pad pb stack g5">
<div class="stack g3" style="margin-top:6px">
<h2 style="margin:0;font-size:23px;line-height:1.2;letter-spacing:-.026em;font-weight:780">Which address is on the account?</h2>
<p class="sub">We send a link that lets you set a new password. The link lasts 30 minutes.</p>
</div>
<label class="field"><span class="field__l">Email address <span class="req">*</span></span>
<input class="input" type="email" value="taiwo.adekola@gmail.com" autocomplete="username">
<span class="field__hint">Use the address you signed up with, not one you added later for receipts.</span></label>
<div class="card card--plain stack g3">
<div class="row" style="gap:10px">
<svg width="19" height="19" style="color:var(--muted);flex:none"><use href="#i-shield"/></svg>
<span class="grow" style="font-size:14px;font-weight:700">We will not say whether that address has an account</span>
</div>
<p class="sub" style="margin:0">The next screen looks the same either way. Confirming it would let anyone check who keeps money here, so the answer arrives in your inbox or not at all.</p>
</div>
<div class="sect" style="margin-top:2px">
<div class="sect__h"><h3>If you cannot reach that inbox</h3></div>
<div class="card card--plain stack g3">
<div class="row" style="gap:11px;align-items:flex-start">
<svg width="19" height="19" style="color:var(--brand);flex:none;margin-top:2px"><use href="#i-lock"/></svg>
<span class="sub"><b style="color:var(--ink)">You have two-factor turned on.</b> A recovery code will let you back in without the email. <a href="#">Use a recovery code</a></span>
</div>
<div class="row" style="gap:11px;align-items:flex-start">
<svg width="19" height="19" style="color:var(--brand);flex:none;margin-top:2px"><use href="#i-users"/></svg>
<span class="sub"><b style="color:var(--ink)">The address is gone for good.</b> Our team can move your account to a new one after an identity check. It takes 1 to 2 working days. <a href="#">Talk to support</a></span>
</div>
</div>
</div>
<p class="tiny" style="margin:0">Requesting a link does not sign you out anywhere or lock the account. Nothing changes until you set a new password.</p>
</div></div>
<div class="actionbar">
<button class="btn btn--primary btn--block">Send the link</button>
<p class="tiny" style="margin:9px 0 0;text-align:center">Remembered it? <a href="#">Back to sign in</a></p>
<div class="hi"></div>
</div>
</div></div>'''))

# ---------------------------------------------------------------- C-07
PLATES.append(dict(
    id='C-07', title='Reset password &mdash; set a new one', tier=1,
    caption='<strong>Where the emailed link lands.</strong> The exit the recovery journey never had. It reuses the '
            'strength meter from #6 so the rule a person met at sign-up is the rule they meet again, and it states '
            'the consequence most reset screens hide: every other signed-in device is dropped. Somebody resetting a '
            'password because they fear a stranger is in the account needs to be told that in advance.',
    tags=['Sits after #9', 'Reuses the meter from #6'],
    frame='''<div class="phone">''' + ST + '''
<div class="vp">
<div class="appbar">
<span class="appbar__title" style="padding-left:8px">Choose a new password</span>
</div>
<div class="scroll"><div class="pad pb stack g5">
<div class="card card--tight row" style="gap:10px;background:var(--brand-soft);border-color:transparent">
<svg width="19" height="19" style="color:var(--brand);flex:none"><use href="#i-checkc"/></svg>
<span class="grow tiny" style="color:var(--brand);font-weight:640">Link confirmed for t&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;a@example.com</span>
</div>
<div class="stack g4">
<label class="field"><span class="field__l">New password <span class="req">*</span></span>
<div class="inputwrap"><input class="input" type="password" value="riverbank-harmattan" autocomplete="new-password"><button class="reveal">Show</button></div>
<div class="pw"><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i></div>
<span class="field__hint">Strong. Two unrelated words and a mark beat one word with substitutions.</span></label>
<label class="field"><span class="field__l">Type it again <span class="req">*</span></span>
<div class="inputwrap"><input class="input" type="password" value="riverbank-harmattan" autocomplete="new-password"><button class="reveal">Show</button></div>
<span class="field__hint">Both entries match.</span></label>
</div>
<div class="card card--plain stack g3">
<div class="row" style="gap:10px">
<svg width="19" height="19" style="color:var(--warn);flex:none"><use href="#i-logout"/></svg>
<span class="grow" style="font-size:14px;font-weight:700">This signs out your other devices</span>
</div>
<p class="sub" style="margin:0">Two other sessions end when you save: an iPhone in Ibadan last used 04 Aug, and a Chrome browser last used 21 Jul. If one of those is not you, that is the point &mdash; save now and read the sign-in history afterwards.</p>
</div>
<p class="tiny" style="margin:0">Your money, units and open offers are untouched by a password change. Nothing is sold and no offer lapses.</p>
</div></div>
<div class="actionbar">
<button class="btn btn--primary btn--block">Save and sign in</button>
<div class="hi"></div>
</div>
</div></div>'''))
