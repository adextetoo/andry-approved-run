# -*- coding: utf-8 -*-
import re, io, json
B = io.open('artifact-de881528-1787405719-3b32.html', encoding='utf-8').read()
events = []
for m in re.finditer(r'<div class="trackbar" id="(\w+)"><b>(.*?)</b><span>(.*?)</span>', B):
    events.append((m.start(), 'track', m.group(1), m.group(2), m.group(3)))
for m in re.finditer(r'<div class="stagehead" id="(\w+)"><span class="code">(.*?)</span>\s*<h2>(.*?)</h2>\s*<span class="meta">(.*?)</span>', B, re.S):
    events.append((m.start(), 'stage', m.group(1), m.group(2), m.group(3), m.group(4)))
for m in re.finditer(r'<h4>#(\d+)\s*&middot;', B):
    events.append((m.start(), 'screen', int(m.group(1))))
events.sort()
cur_t = cur_s = None
out = {}
tracks, stages = [], []
for e in events:
    if e[1] == 'track':
        cur_t = dict(id=e[2], title=e[3], meta=e[4]); tracks.append(cur_t)
    elif e[1] == 'stage':
        cur_s = dict(id=e[2], code=e[3], title=e[4], meta=e[5], track=cur_t['id'] if cur_t else None)
        stages.append(cur_s)
    else:
        out[e[2]] = dict(track=cur_t['id'] if cur_t else None,
                         track_title=cur_t['title'] if cur_t else None,
                         stage=cur_s['id'] if cur_s else None,
                         stage_code=cur_s['code'] if cur_s else None,
                         stage_title=cur_s['title'] if cur_s else None)
print('tracks', len(tracks), [t['id'] for t in tracks])
print('stages', len(stages))
print('screens mapped', len(out))
missing = [n for n in range(1, 172) if n not in out or out[n]['stage'] is None]
print('unmapped:', missing)
json.dump(dict(map=out, tracks=tracks, stages=stages), io.open('sections.json', 'w', encoding='utf-8'))
for t in tracks: print(' ', t['id'], '|', t['title'], '|', t['meta'])
