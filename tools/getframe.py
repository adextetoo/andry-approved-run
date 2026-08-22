# -*- coding: utf-8 -*-
import re, io, sys
h = io.open('run.html', encoding='utf-8').read()
body = h[h.index('<div class="doc">'):]
def balanced(s, start):
    i, depth = start, 0
    tag = re.compile(r'</?div\b', re.I)
    while True:
        m = tag.search(s, i)
        if m.group(0).lower() == '<div': depth += 1
        else: depth -= 1
        i = s.index('>', m.end()) + 1
        if depth == 0: return s[start:i], i
want = set(int(x) for x in sys.argv[1:])
for m in re.finditer(r'<div class="(plate|fx-item--desk)">', body):
    blk, _ = balanced(body, m.start())
    cap = re.search(r'<h4><b>#(\d+)</b>\s*(.*?)</h4>', blk, re.S)
    n = int(cap.group(1))
    if n in want:
        ci = blk.rfind('<div class="run-cap')
        frame = blk[blk.index('>') + 1:ci]
        print('=' * 78)
        print('### PLATE #%d  %s' % (n, re.sub('<[^>]+>', '', cap.group(2))))
        print('=' * 78)
        print(frame.strip())
        print()
