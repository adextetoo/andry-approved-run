# Andry — the approved run

Every Andry screen that carries an **`Approved in review`** tag in either of the two
source reviews, gathered into a single document with each plate's origin recorded.

**171 plates · 4 tracks · 38 stages · light and dark**

Open [`index.html`](index.html) in a browser, or serve the folder and visit it — the page
is fully self-contained (no scripts, no network requests, no external fonts or images).

## Four documents

| | What it is | Screens |
| --- | --- | ---: |
| [`/`](index.html) | **The approved run** — every screen tagged `Approved in review` in either source review | 171 |
| [`/audit/`](audit/index.html) | **The closing 42** — the register of screens the run pointed at but never drew, all now closed | 42 |
| [`/closers/`](closers/index.html) | **The thirteen** — the flow-blocking gaps, drawn as plates | 13 |
| [`/closers-2/`](closers-2/index.html) | **The twenty-nine** — the named destinations, drawn. Closes the register | 29 |

The register is now closed: 42 of 42 drawn, and every labelled affordance in the run points at
a screen that exists.

## Two stylesheet defects, found and fixed

Both surfaced while matching new plates to existing ones. Neither was introduced here. Both are
fixed in [`tools/stylesheet_repairs.py`](tools/stylesheet_repairs.py), which every build applies —
**in the stylesheet, never in a plate.** No plate markup was edited to fix either one, and the
repair is idempotent and asserts each defect is present before touching anything.

**The operator consoles had no frame.** The desktop token block lost its selector upstream, so it
began mid-comment with orphaned declarations. A browser reads those as the prelude of a rule and
consumes until the next `{` — which belongs to `.desk` — so the console frame's whole declaration
block was swallowed and dropped. Exactly one rule was lost, and it was the one that makes a console
1440 × 900, a two-column grid, and clipped. All 19 operator plates were rendering with the rail
stacked above the main pane at whatever height the content reached. The repair restores the
selector and the two lost tokens (`--d-row`, `--d-row-lg`); the existing rule is now reachable and
all 19 measure 1440 × 900.

**The KYC stepper labels collided with the heading.** `.kyc__l` was defined as a 2px connector
line, but every stepper in the product puts its step label inside it — `#11`, `#103` and `#132`.
The text overflowed a 2px box, wrapped, and ran into the heading below. There is no separate
connector element in the markup, so the label is what the class had to be: it is now typeset as
one, with `nowrap` and an ellipsis for narrow steps, and the done state moved from background to
text colour. All three steppers measure 26px with no collision and no clipping.

The audit was produced by parsing the run for every interactive element and checking each
labelled destination against the screens that exist. The count was verified against the live
DOM: 1,296 buttons and 35 links across 171 plates. The thirteen closers are built on the
Andry design system with no rule added to it, and nothing in the approved 171 was altered.

---

## What was extracted

Both source artifacts were read for screens tagged `Approved in review`, and only those
screens were kept:

| Source review | Screens tagged `Approved in review` |
| --- | ---: |
| *Andry — the complete product, 171 screens* (`complete-171`) | 66 |
| *Andry — the approved 171* (`approved-171`) | 105 |
| **Combined** | **171** |

### The two approved sets are exactly complementary

This is the part worth knowing. The sets do not overlap at a single screen, and together
they cover the run end to end:

- Every screen `complete-171` approved is one `approved-171` had marked *Carried over*.
- Every screen `approved-171` approved is one `complete-171` had not yet signed off.

The two documents also line up screen-for-screen — verified across all 171 positions — so
the intersection is empty and the union is the whole product. A merge of the approved
tags is therefore the complete 171, not a subset.

### The split by track

| Track | Screens | from `complete-171` | from `approved-171` | Surface |
| --- | ---: | ---: | ---: | --- |
| A · The owner | 100 | 32 | 68 | 402 × 874 |
| B · The supervisor | 30 | 9 | 21 | 402 × 874 |
| C · The host | 22 | 6 | 16 | 402 × 874 |
| D · The operator | 19 | 19 | 0 | 1440 × 900 |
| **All four tracks** | **171** | **66** | **105** | 38 stages |

---

## How to read a plate

Each caption carries the screen number, its name, the design note from the source
caption, and two chips:

- <kbd>✓ Approved in review</kbd> — the tag this page selected on. All 171 carry it.
- <kbd>complete-171</kbd> / <kbd>approved-171</kbd> — which review's tag the plate
  carries, and therefore which artifact the markup was lifted from.

Design notes from the source captions (*New*, *Reworked*, audit references such as
*W-07 missing states*) are kept as they were.

## One discrepancy, recorded

*Andry — the approved 171* also carries small `171-build:` chips reporting what the
older build had said about a screen. On **63 plates those chips read `approved` even
though the older build never tagged them**.

This page follows the tags, so those reference chips were dropped rather than left to
contradict the provenance chip beside them. The masthead says so on the page itself.
Nothing else was removed from any caption.

---

## Fidelity

- Plates are lifted from the artifact that approved them: 66 from the `complete-171`
  markup, 105 from the `approved-171` markup.
- The `approved-171` stylesheet is reused verbatim, so the plates render exactly as they
  do at source. All document chrome added here is namespaced to classes the Andry design
  system does not define (`.run-*`, `.ledger`, `.prov`), and overrides nothing.
- Two corrections were necessary, both in the stylesheet and neither in a plate: the
  malformed token block that made `.desk` unreachable, and `.kyc__l` being a connector
  line rather than the label it holds. See the section above.
- `color` is stated explicitly on the ledger table, which does not inherit colour in
  quirks mode.
- Per-stage horizontal shelves were changed to a wrapping grid so a whole stage reads at
  once. Below 940px it falls back to a shelf rather than shrinking the frames — a
  402 × 874 mock is only honest at 402 × 874.
- Every non-ASCII character outside the stylesheet is written as a numeric character
  reference, so the markup does not depend on the served charset.

## Layout

```
index.html                    the approved run — open this
audit/index.html              the closing 42, the gap register
closers/index.html            the thirteen flow-blockers, drawn
closers-2/index.html          the twenty-nine named destinations, drawn

artifact/approved-run.html    artifact form of the run (no <html>/<head>)
audit/closing.html            artifact form of the register
closers/thirteen.html         artifact form of the thirteen
closers-2/twentynine.html     artifact form of the twenty-nine

tools/stylesheet_repairs.py   the two stylesheet fixes, applied by every build
tools/extract.py              parses both sources into structured records
tools/sections.py             maps every screen to its track and stage
tools/build.py                assembles the merged run
tools/affordances.py          inventories every affordance, per screen
tools/getframe.py             pulls a plate's markup out of the run by number
tools/update_closing.py       marks the register closed once the 42 were drawn
tools/plates/plates_a.py      closers C-01 to C-07
tools/plates/plates_b.py      closers C-08 to C-13
tools/plates/build_closers.py assembles the thirteen
tools/plates/plates_c.py      closers C-14 to C-26, track A
tools/plates/plates_d.py      closers C-27 to C-39, tracks B and C
tools/plates/plates_e.py      closers C-40 to C-42, the operator consoles
tools/plates/build_tier2.py   assembles the twenty-nine
```

The two source artifacts are not included in this repository — they are private design
documents. `tools/` records how the merge was produced; to re-run it, place the two
source HTML files alongside the scripts and run them in the order above.

## Licence

[MIT](LICENSE). Copyright (c) 2026 adextetoo.

Two things the licence does not do, worth stating since this repository is mostly design
rather than code:

- **It grants no trademark rights.** "Andry" and any marks, logos or brand elements shown
  in the plates are not licensed by MIT and are not covered here.
- **It is a software licence.** It fits the build tooling in `tools/` cleanly. If you would
  rather the plates, written content and design system carried different terms from the
  code, the usual pairing is MIT for `tools/` and something like CC BY 4.0 for the rest.
