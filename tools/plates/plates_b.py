# -*- coding: utf-8 -*-
"""Plates C-08 to C-13 — payment instruments and the document viewer."""
from plates_a import ST, TABBAR_PROFILE

PLATES = []

# ---------------------------------------------------------------- C-08
PLATES.append(dict(
    id='C-08', title='Add a bank account', tier=1,
    caption='<strong>The form three plates offer and none shows.</strong> #19, #87 and #90 all reach for it. '
            'The account name is resolved from the bank and shown back before anything is saved, so the '
            'name-match rule stops being a rule the user is told about and becomes one they can see passing. '
            'The distinction Andry actually enforces &mdash; middle names fine, different person never &mdash; '
            'is stated where it is needed rather than in a help article.',
    tags=['Serves #19, #87, #90', 'May be shared by B and C'],
    frame='''<div class="phone">''' + ST + '''
<div class="vp">
<div class="appbar">
<button class="appbar__btn" aria-label="Back to payment methods"><svg width="24" height="24"><use href="#i-back"/></svg></button>
<div class="appbar__title">Add a bank account</div>
</div>
<div class="scroll"><div class="pad pb stack g5">
<p class="sub" style="margin:0">This is where money leaves Andry. It must be an account in your own name, <b style="color:var(--ink)">Taiwo Adekola</b>, the name we verified against your ID.</p>
<div class="stack g4">
<label class="field"><span class="field__l">Bank <span class="req">*</span></span>
<div class="row" style="gap:0"><input class="input" value="Zenith Bank" style="border-top-right-radius:0;border-bottom-right-radius:0"><button class="btn btn--secondary" style="min-height:50px;border-radius:0 var(--radius) var(--radius) 0;border-left:0;padding:0 14px"><svg width="18" height="18"><use href="#i-chev"/></svg></button></div></label>
<label class="field"><span class="field__l">Account number <span class="req">*</span></span>
<input class="input mono" style="letter-spacing:.1em" value="2088314417">
<span class="field__hint">Ten digits, the NUBAN on your card or statement.</span></label>
</div>
<div class="verify">
<div class="verify__top">
<svg width="20" height="20" style="color:var(--ok);flex:none"><use href="#i-checkc"/></svg>
<div class="grow">
<div style="font-size:13.5px;font-weight:700;color:var(--ok)">Name matches</div>
<div class="tiny" style="color:var(--ok)">Returned by Zenith Bank a moment ago</div>
</div>
</div>
<div class="verify__row"><span class="k">Account</span><span class="grow v">TAIWO A ADEKOLA</span></div>
<div class="verify__row"><span class="k">Your ID</span><span class="grow v">Taiwo Adekola</span></div>
<div class="verify__row" style="align-items:flex-start">
<svg width="18" height="18" style="color:var(--muted);flex:none;margin-top:2px"><use href="#i-info"/></svg>
<span class="grow tiny">The extra initial is accepted. A middle name, an initial or a different word order all pass; a different person does not.</span>
</div>
</div>
<label class="check">
<input type="checkbox" checked>
<span>Make this my default payout account, replacing Guaranty Trust Bank &bull;&bull;&bull;&bull;&bull;&bull;8032.</span>
</label>
<div class="card card--plain stack g3">
<div class="row" style="gap:10px">
<svg width="19" height="19" style="color:var(--warn);flex:none"><use href="#i-clock"/></svg>
<span class="grow" style="font-size:14px;font-weight:700">A new account waits 24 hours</span>
</div>
<p class="sub" style="margin:0">Withdrawals to an account added today are held until 05 Aug, 10:30. It is a delay on the account, not on your money, and it exists so a stolen sign-in cannot be turned into a payout the same afternoon. Your existing account keeps working throughout.</p>
</div>
</div></div>
<div class="actionbar"><button class="btn btn--primary btn--block">Save this account</button></div>
''' + TABBAR_PROFILE + '''
</div><div class="hi"></div></div>'''))

# ---------------------------------------------------------------- C-09
PLATES.append(dict(
    id='C-09', title='Add a card', tier=1,
    caption='<strong>The capture screen behind #19 and #20.</strong> Cards move money in only, and saying so on '
            'the card form prevents the wrong expectation forming at the moment it would form. The fee is shown '
            'against the free alternative rather than in isolation, because a number a person cannot compare is '
            'not disclosure.',
    tags=['Serves #19, #20', 'Anchor <b>Stripe</b>'],
    frame='''<div class="phone">''' + ST + '''
<div class="vp">
<div class="appbar">
<button class="appbar__btn" aria-label="Back to payment methods"><svg width="24" height="24"><use href="#i-back"/></svg></button>
<div class="appbar__title">Add a card</div>
</div>
<div class="scroll"><div class="pad pb stack g5">
<div class="card card--tight row" style="gap:10px">
<svg width="19" height="19" style="color:var(--muted);flex:none"><use href="#i-info"/></svg>
<span class="grow tiny">Cards add money to your wallet. Payouts always go to a bank account in your name &mdash; a card can never receive one.</span>
</div>
<div class="stack g4">
<label class="field"><span class="field__l">Card number <span class="req">*</span></span>
<div class="inputwrap"><input class="input mono" style="letter-spacing:.09em" value="5061 8412 7734 6218" autocomplete="cc-number">
<span class="reveal" style="pointer-events:none"><span class="badge badge--brand">Verve</span></span></div></label>
<div class="grid2">
<label class="field"><span class="field__l">Expires <span class="req">*</span></span>
<input class="input mono" value="09 / 28" autocomplete="cc-exp"></label>
<label class="field"><span class="field__l">CVV <span class="req">*</span></span>
<div class="inputwrap"><input class="input mono" type="password" value="512" autocomplete="cc-csc"><button class="reveal">Show</button></div></label>
</div>
<label class="field"><span class="field__l">Name on the card <span class="req">*</span></span>
<input class="input" value="TAIWO ADEKOLA" autocomplete="cc-name">
<span class="field__hint">Cards in another name are declined by the processor, not by us.</span></label>
</div>
<div class="verify">
<div class="verify__top" style="background:var(--surface-3)">
<svg width="20" height="20" style="color:var(--ink-2);flex:none"><use href="#i-scale"/></svg>
<div class="grow"><div style="font-size:13.5px;font-weight:700;color:var(--ink)">What a card costs you</div></div>
</div>
<div class="verify__row"><span class="k">Card</span><span class="grow v">1.4% + &#8358;100.00</span><span class="money money--sm" style="color:var(--warn)">&#8358;1,500.00</span></div>
<div class="verify__row"><span class="k">Transfer</span><span class="grow v">No fee</span><span class="money money--sm" style="color:var(--ok)">&#8358;0.00</span></div>
<div class="verify__row" style="align-items:flex-start">
<svg width="18" height="18" style="color:var(--muted);flex:none;margin-top:2px"><use href="#i-info"/></svg>
<span class="grow tiny">On a &#8358;100,000.00 top-up. A card lands in seconds; a transfer takes 2 to 10 minutes. Most owners keep a card for when a pool is closing and use transfers otherwise.</span>
</div>
</div>
<div class="row" style="gap:9px;padding:11px 12px;background:var(--surface-2);border-radius:var(--radius)">
<svg width="18" height="18" style="color:var(--ok);flex:none"><use href="#i-lock"/></svg>
<span class="tiny">Your card is stored by our processor, not by Andry. We keep the last four digits and the expiry date so you can recognise it, and nothing else.</span>
</div>
<p class="tiny" style="margin:0">Your bank may ask you to approve a &#8358;50.00 check with an OTP. It is refunded within the hour.</p>
</div></div>
<div class="actionbar"><button class="btn btn--primary btn--block">Save this card</button></div>
''' + TABBAR_PROFILE + '''
</div><div class="hi"></div></div>'''))


# ---------------------------------------------------------------- document viewer
def doc(title, appbar_title, version, effective, minutes, chips, plain, sections, action, close_label):
    chiprow = ''.join('<button class="chip%s">%s</button>' % (' is-on' if i == 0 else '', c)
                      for i, c in enumerate(chips))
    plainrows = ''.join(
        '<div class="row" style="gap:11px;align-items:flex-start">'
        '<svg width="18" height="18" style="color:var(--brand);flex:none;margin-top:2px"><use href="#i-%s"/></svg>'
        '<span class="sub">%s</span></div>' % (ico, txt) for ico, txt in plain)
    body = ''.join(
        '<div class="sect"><div class="sect__h"><h3>%s</h3><span class="mono" style="color:var(--faint)">%s</span></div>'
        '%s</div>' % (h, ref, ''.join('<p style="margin:0 0 11px;font-size:14px;line-height:1.6;color:var(--ink-2)">%s</p>' % p
                                      for p in paras))
        for ref, h, paras in sections)
    return '''<div class="phone">''' + ST + '''
<div class="vp">
<div class="appbar">
<button class="appbar__btn" aria-label="%s"><svg width="24" height="24"><use href="#i-close"/></svg></button>
<div class="appbar__title">%s</div>
<button class="appbar__btn" aria-label="Download as PDF"><svg width="24" height="24"><use href="#i-download"/></svg></button>
</div>
<div class="pad" style="padding-bottom:10px">
<div class="spread" style="padding:9px 12px;background:var(--surface-2);border-radius:var(--radius)">
<span class="tiny"><b style="color:var(--ink)">Version %s</b> &middot; in force %s</span>
<span class="tiny mono">%s min read</span>
</div>
</div>
<div class="pad" style="padding-bottom:12px"><div class="chips">%s</div></div>
<div class="scroll"><div class="pad pb">
<div class="card stack g3">
<div class="row" style="gap:10px">
<svg width="19" height="19" style="color:var(--brand);flex:none"><use href="#i-eye"/></svg>
<span class="grow" style="font-size:14.5px;font-weight:730">In plain words</span>
</div>
%s
<p class="tiny" style="margin:0">This summary is not the agreement. Where the two differ, the numbered text below is what binds.</p>
</div>
%s
<p class="tiny" style="margin-top:20px;padding:11px 12px;background:var(--surface-2);border-radius:var(--radius)">Kept at <span class="mono">andry.ng/legal</span>. Every earlier version stays published, and we tell you 30 days before a change takes effect.</p>
</div></div>
%s
</div><div class="hi"></div></div>''' % (close_label, appbar_title, version, effective, minutes,
                                        chiprow, plainrows, body, action)


BACK_TO_SIGNUP = ('<div class="actionbar"><button class="btn btn--primary btn--block">Back to create account</button>'
                  '</div>')

# ---------------------------------------------------------------- C-10
PLATES.append(dict(
    id='C-10', title='Terms of Service', tier=1,
    caption='<strong>The document #6 asks you to accept.</strong> Account creation required agreeing to text the '
            'product never showed. The viewer opens on a plain-language summary and states outright that the '
            'summary does not bind &mdash; which is the honest version of the pattern, and cheaper than a reader '
            'who thinks the four bullets were the contract. Version and in-force date sit above the fold because '
            '#98 asks people to re-consent and they need to know what changed.',
    tags=['Serves #6, #7, #98', 'One viewer, four documents'],
    frame=doc(
        'Terms of Service', 'Terms of Service', '4.2', '01 Jul 2026', '11',
        ['Summary', 'Your account', 'What we do', 'Money', 'Ending it', 'Disputes'],
        [('i-users', '<b style="color:var(--ink)">You own units, we keep the record.</b> Andry is the register and the '
                     'escrow agent. We do not own your animal and cannot sell it without your instruction.'),
         ('i-shield', '<b style="color:var(--ink)">One account, one person.</b> The name on it must be the name on your '
                      'ID, and you may not hold units for someone else.'),
         ('i-wallet', '<b style="color:var(--ink)">Money in the wallet is yours.</b> It sits in a client account '
                      'separate from Andry&rsquo;s own money, and it is not lent out.'),
         ('i-logout', '<b style="color:var(--ink)">You can leave at any time.</b> Sell or hold to maturity; we cannot '
                      'close your account with less than 30 days&rsquo; notice unless the law requires it.')],
        [('1', 'Who we are',
          ['Andry Technologies Limited, RC 1884220, of 14 Awolowo Road, Ikoyi, Lagos, operates this service. Where these '
           'terms say <b style="color:var(--ink)">we</b> or <b style="color:var(--ink)">Andry</b>, they mean that company.',
           'We are not a bank, an insurer or a licensed investment adviser, and nothing in the service is advice about '
           'whether an animal is a good purchase for you.']),
         ('2', 'What a unit is',
          ['A unit is an undivided fractional interest in one identified animal, recorded against that animal&rsquo;s tag '
           'in our register. Buying 20 of 400 units in AND-4471-KX makes you the owner of 5% of that animal and of 5% of '
           'whatever it realises on sale, after the deductions set out in clause 6.',
           'A unit is not a share in Andry, not a debt owed to you by Andry, and not a deposit. If Andry ceased trading, '
           'your units would remain yours and the register would pass to the trustee named at clause 9.']),
         ('3', 'Your account',
          ['You must be 18 or over and resident in Nigeria, and you must complete identity verification before the wallet '
           'opens. You may hold one account only.',
           'Keep your sign-in details to yourself. Tell us within 24 hours if you think someone else has used your account; '
           'we will freeze it while we look.'])],
        BACK_TO_SIGNUP, 'Close and return to create account')))

# ---------------------------------------------------------------- C-11
PLATES.append(dict(
    id='C-11', title='Privacy notice', tier=1,
    caption='<strong>Linked from five places, including the moment #11 asks for a passport.</strong> The retention '
            'row carries a number rather than <q>as long as necessary</q>, and the sharing section names the actual '
            'recipients &mdash; a supervisor sees your first name and nothing else. That specificity is the whole '
            'value of the screen; a vague privacy notice is worse than none because it teaches people not to read.',
    tags=['Serves #6, #7, #11, #19, #98', 'One viewer, four documents'],
    frame=doc(
        'Privacy notice', 'How we handle your data', '3.0', '01 Jul 2026', '8',
        ['Summary', 'What we hold', 'Why', 'Who sees it', 'How long', 'Your rights'],
        [('i-doc', '<b style="color:var(--ink)">Your ID is held for verification only.</b> It is encrypted, seen by our '
                   'verification team, and deleted 90 days after your account closes.'),
         ('i-users', '<b style="color:var(--ink)">Supervisors and hosts see very little.</b> Your first name and the units '
                     'you hold in the animal they work on. Not your address, your documents or your other holdings.'),
         ('i-revoke', '<b style="color:var(--ink)">We do not sell anything about you.</b> No advertising networks, no data '
                      'brokers, no sale of your activity.'),
         ('i-download', '<b style="color:var(--ink)">You can take it all with you.</b> Ask for an export and you get every '
                        'record we hold, in a readable file, inside 30 days.')],
        [('1', 'What we hold about you',
          ['<b style="color:var(--ink)">Identity:</b> your name, date of birth, address, NIN and the photo ID you upload. '
           '<b style="color:var(--ink)">Money:</b> your bank account and the last four digits of any card, plus every '
           'transaction on your wallet. <b style="color:var(--ink)">Activity:</b> what you viewed, bought, listed and '
           'messaged, and the device and rough location you signed in from.',
           'We do not hold your full card number. Our payment processor does, and we never see it.']),
         ('2', 'Why we hold it',
          ['Identity data is held because the Money Laundering (Prevention and Prohibition) Act requires us to know who '
           'our customers are. We could not open your wallet without it, and we cannot delete it on request while the '
           'account is open.',
           'Activity data is held to run the service and to spot fraud. Where we use it to suggest listings, you can turn '
           'that off in Notifications without losing anything else.']),
         ('3', 'How long we keep it',
          ['Photo ID: 90 days after closure. Transaction records: 7 years after closure, which the law fixes and we cannot '
           'shorten. Messages: 2 years. Sign-in history: 12 months. Everything else goes within 30 days of closure.'])],
        BACK_TO_SIGNUP, 'Close and return')))

# ---------------------------------------------------------------- C-12
PLATES.append(dict(
    id='C-12', title='Risk disclosure, in full', tier=1,
    caption='<strong>The policy #13 offers to show.</strong> The gate summarises three risks in cards; this is the '
            'text underneath, and it carries the numbers the gate can only gesture at &mdash; the actual loss rate by '
            'species, the actual spread of time-to-sell. A gate that asks for acknowledgement of a document nobody '
            'can open is a consent form with the consent missing.',
    tags=['Serves #13, #98', 'One viewer, four documents'],
    frame=doc(
        'Risk disclosure', 'Risk disclosure', '2.4', '01 Jul 2026', '9',
        ['Summary', 'Death', 'Price', 'Selling', 'Insurance', 'Counterparties'],
        [('i-alert', '<b style="color:var(--ink)">You can lose everything you pay.</b> An uninsured animal that dies '
                     'leaves its units worth nothing. This is not a remote possibility; it happened to 47 animals in the '
                     'past 12 months.'),
         ('i-scale', '<b style="color:var(--ink)">Prices fall as well as rise.</b> Cattle prices moved between &minus;14% '
                     'and +23% over the past two years.'),
         ('i-clock', '<b style="color:var(--ink)">You may wait to sell.</b> Half of listings clear in 9 days. One in '
                     'twenty takes more than 60.'),
         ('i-shield', '<b style="color:var(--ink)">Insurance is narrower than people assume.</b> It pays for death by named '
                      'causes, minus a 10% excess. It never pays for a fall in price.')],
        [('1', 'The animal can die',
          ['Across the herd, 2.1 animals in 100 were lost in the 12 months to 30 June 2026. The rate is not even: it was '
           '1.4% for cattle, 3.8% for goats and 4.1% for sheep, and it rises in the rainy season.',
           'Where the animal was insured and the cause is covered, the underwriter pays the last valued price less a 10% '
           'excess, and that money is divided between unit holders. Where it was not, or the cause is excluded, your units '
           'become worth nothing and no compensation is due from Andry.']),
         ('2', 'The price can fall',
          ['A unit&rsquo;s value follows the animal&rsquo;s valuation, which follows weight, breed, season and the market '
           'at the nearest trading centre. Feed cost, fuel price and demand around Sallah and Christmas all move it.',
           'Between July 2024 and June 2026 the median cattle unit moved between &minus;14% and +23% from its purchase '
           'price. Past movement does not predict future movement.']),
         ('3', 'You may not be able to sell when you want',
          ['Selling requires another owner to buy. Andry does not buy units back and does not guarantee a buyer. In the '
           'past year the median listing sold in 9 days, but 5% took more than 60 days and 1% did not sell at all before '
           'the animal reached maturity.',
           'Do not buy units with money you will need at a fixed date.'])],
        '<div class="actionbar"><button class="btn btn--secondary btn--block">Back to the risk gate</button></div>', 'Close and return to the risk gate')))

# ---------------------------------------------------------------- C-13
PLATES.append(dict(
    id='C-13', title='Ownership agreement', tier=1,
    caption='<strong>Offered on #31, one tap before money moves.</strong> It is the document that defines what a unit '
            'actually is, so it is shown with the specific purchase filled in rather than as a blank template &mdash; '
            'the animal, the units, the price, the date. The deduction waterfall is a table because that is the clause '
            'people come back to argue about, and prose hides arithmetic.',
    tags=['Serves #31', 'One viewer, four documents'],
    frame=doc(
        'Ownership agreement', 'Ownership agreement', '1.9', '01 Jul 2026', '6',
        ['Summary', 'This purchase', 'Your rights', 'Deductions', 'Maturity', 'Transfer'],
        [('i-portfolio', '<b style="color:var(--ink)">You own 20 of 400 units</b> in AND-4471-KX, a Sokoto Gudali bull at '
                         'Ayalar Ranch. That is 5% of the animal.'),
         ('i-lock', '<b style="color:var(--ink)">Nobody can sell it without you.</b> Not the ranch, not the supervisor, not '
                    'Andry &mdash; except at maturity or on veterinary grounds, both defined below.'),
         ('i-scale', '<b style="color:var(--ink)">Costs come off the sale, not your wallet.</b> You are never invoiced for '
                     'keep; it is deducted from proceeds in the order at clause 4.'),
         ('i-swap', '<b style="color:var(--ink)">Units are transferable.</b> You may sell to another verified owner at any '
                    'time without asking permission.')],
        [('1', 'What you are buying today',
          ['20 units in the animal tagged <span class="mono">AND-4471-KX</span>, a Sokoto Gudali bull, born approximately '
           'March 2024, held at Ayalar Ranch, Oyo State, at a price of <span class="money money--sm">&#8358;9,568.90</span> '
           'per unit, totalling <span class="money money--sm">&#8358;191,378.00</span> on 04 August 2026.',
           'Your money is held in escrow until Ayalar Ranch confirms the animal on site and a supervisor scans the tag. '
           'If confirmation does not arrive within 14 days, the escrow reverses in full.']),
         ('2', 'Deductions from proceeds',
          ['When the animal is sold, the gross price is applied in this order: veterinary costs incurred and evidenced; '
           'the host&rsquo;s keep at the rate agreed with that ranch; the supervisor&rsquo;s fee; Andry&rsquo;s commission '
           'of 4%; and the remainder divided between unit holders in proportion to units held.',
           'If proceeds do not cover the deductions, the shortfall is borne by Andry and the host, not by you. You cannot '
           'be asked for more money than you paid.']),
         ('3', 'Sale without your instruction',
          ['Two exceptions. At <b style="color:var(--ink)">maturity</b>, when the animal reaches the sale weight recorded '
           'at clause 1 of the herd schedule, we sell and distribute; you are told 14 days ahead and may buy other owners '
           'out instead. On <b style="color:var(--ink)">veterinary grounds</b>, where a licensed vet certifies the animal '
           'must be slaughtered to prevent suffering or disease spread, we act immediately and tell you the same day.'])],
        '<div class="actionbar"><button class="btn btn--secondary btn--block">Back to the purchase</button></div>', 'Close and return to the purchase')))
