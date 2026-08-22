# Andry — the approved run

Every Andry screen that carries an **`Approved in review`** tag in either of the two
source reviews, gathered into a single document with each plate's origin recorded.

**171 plates · 4 tracks · 38 stages · light and dark**

Open [`index.html`](index.html) in a browser, or serve the folder and visit it — the page
is fully self-contained (no scripts, no network requests, no external fonts or images).

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
- Two additions were necessary:
  - `--d-row` / `--d-row-lg` — the operator desk tables reference these tokens, but
    neither source defines them.
  - `color` stated explicitly on the ledger table, which does not inherit colour in
    quirks mode.
- Per-stage horizontal shelves were changed to a wrapping grid so a whole stage reads at
  once. Below 940px it falls back to a shelf rather than shrinking the frames — a
  402 × 874 mock is only honest at 402 × 874.
- Every non-ASCII character outside the stylesheet is written as a numeric character
  reference, so the markup does not depend on the served charset.

## Layout

```
index.html                  standalone page — open this
artifact/approved-run.html  the same document in Claude artifact form (no <html>/<head>)
tools/extract.py            parses both sources into structured records
tools/sections.py           maps every screen to its track and stage
tools/build.py              assembles the merged document
```

The two source artifacts are not included in this repository — they are private design
documents. `tools/` records how the merge was produced; to re-run it, place the two
source HTML files alongside the scripts and run them in the order above.

## Licence

No licence is granted. This is a private design record; all rights reserved.
