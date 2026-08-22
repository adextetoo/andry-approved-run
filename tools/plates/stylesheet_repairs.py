# -*- coding: utf-8 -*-
"""Two repairs to the Andry stylesheet, applied wherever it is assembled.

Both defects are in the stylesheet the approved artifacts inherit. Neither is
fixed by editing a plate, and neither changes any plate's markup. Each repair
asserts the defect is present before touching anything, so a stylesheet that
has already been corrected upstream will fail loudly rather than be mangled.
"""
import re

# ---------------------------------------------------------------------------
# 1. The console frame rule is unreachable.
#
# The desktop token block lost its selector and its first two declarations
# upstream. What survives begins mid-comment:
#
#     /* queue row with two lines */
#       --d-rail:236px;
#       ...
#     }
#
# At top level a browser reads those orphaned declarations as the prelude of a
# qualified rule and keeps consuming until the next "{" - which belongs to
# ".desk". The console frame's whole declaration block is swallowed as the body
# of an invalid selector and dropped. Exactly one rule is lost, and it is the
# one that makes a console 1440 x 900, a two-column grid, and clipped.
#
# Every operator plate in the run renders with its rail stacked above the main
# pane at whatever height the content reaches. Restoring the selector and the
# two lost tokens makes the existing rule reachable. No rule is added.
# The pattern is anchored to a line start. After the repair the same comment
# survives at the end of a declaration line inside :root, so an unanchored
# match would fire a second time and nest another selector.
_DESK_ORPHAN = '\n/* queue row with two lines */\n  --d-rail:236px;'
_DESK_REPAIR = (
    '\n/* --- desktop tokens. The selector and the first two declarations were\n'
    '       lost upstream, which left these orphaned and swallowed the .desk\n'
    '       rule that follows. Restored. --- */\n'
    ':root{\n'
    '  --d-row:44px;          /* data row height */\n'
    '  --d-row-lg:56px;       /* queue row with two lines */\n'
    '  --d-rail:236px;')

# ---------------------------------------------------------------------------
# 2. The KYC stepper labels collide with the heading beneath them.
#
# .kyc__l was defined as a 2px connector line, but every stepper in the product
# puts its step label inside it - #11, #103 and #132. The text overflows a 2px
# box, wraps, and runs into the heading below. There is no separate connector
# element in the markup, so the label is what the class has to be.
#
# Typeset as a label: nowrap, ellipsis when a step is narrow, and no background
# so the line no longer prints behind the words. The is-done colour moves from
# background to text.
_KYC_OLD = ('.kyc__l{flex:1;height:2px;background:var(--line);}\n'
            '.kyc__s.is-done .kyc__l{background:var(--ok);}')
_KYC_NEW = (
    '/* --- .kyc__l carries the step label in every stepper in the product, so\n'
    '       it is typeset as a label. It was a 2px connector line, which left\n'
    '       the text overflowing and colliding with the heading beneath. --- */\n'
    '.kyc__l{flex:1;min-width:0;background:none;\n'
    '  font-size:11.5px;line-height:1.2;letter-spacing:-.005em;font-weight:640;\n'
    '  color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}\n'
    '.kyc__s{min-width:0;}\n'
    '.kyc__s.is-done .kyc__l{background:none;color:var(--ok);}')


def already_repaired(css):
    """True when a stylesheet has been through repair() before."""
    return bool(re.search(r'(?m)^\.desk\{', css)) and 'text-overflow:ellipsis' in (
        re.search(r'(?m)^\.kyc__l\{[^}]*\}', css) or type('', (), {'group': lambda s, n=0: ''})()
    ).group(0)


def repair(css, strict=True):
    """Return the stylesheet with both defects corrected. Idempotent."""
    if already_repaired(css):
        return css
    for name, old, new in (('desk frame rule', _DESK_ORPHAN, _DESK_REPAIR),
                           ('kyc stepper label', _KYC_OLD, _KYC_NEW)):
        n = css.count(old)
        if n != 1:
            if strict:
                raise AssertionError('%s: expected 1 occurrence of the defect, found %d' % (name, n))
            continue
        css = css.replace(old, new)

    # the .desk rule must now be reachable: a top-level rule whose selector is
    # exactly .desk, carrying the 1440 x 900 frame
    m = re.search(r'(?m)^\.desk\{[^}]*\}', css)
    assert m and 'height:900px' in m.group(0), 'desk rule still not well formed'
    assert 'height:2px' not in _KYC_NEW
    return css
