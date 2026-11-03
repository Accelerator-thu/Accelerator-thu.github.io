#!/usr/bin/env python3
# Usage: python3 scripts/buffon_figure.py content/blog/buffon-polygons/setup.svg
"""Theme-aware setup figure for the Buffon-polygon post (uses the site's .th-* palette)."""
import math, sys
W, H = 640, 190
LINES = [42, 142]               # spacing d = 100
cx, cy, theta = 330.0, 104.0, math.radians(24)
# irregular convex pentagon in its own frame (angle deg, radius)
shape = [(0, 62), (78, 48), (150, 56), (215, 50), (290, 54)]
pts = []
for a, r in shape:
    t = math.radians(a) + theta
    pts.append((cx + r * math.cos(t), cy - r * math.sin(t)))
ys = [p[1] for p in pts]
top = min(range(5), key=lambda i: pts[i][1]); bot = max(range(5), key=lambda i: pts[i][1])
ymin, ymax = pts[top][1], pts[bot][1]
assert ymin > LINES[0] and ymax > LINES[1] > ymin, (ymin, ymax)
M = "font-family:KaTeX_Math,'Times New Roman',serif;font-style:italic"
o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" class="pub-svg post-svg" role="img" '
     'aria-label="A convex polygon on a plane ruled with parallel lines spaced d apart; its vertical extent w(theta) at orientation theta determines whether it crosses a line.">'
     '<defs><marker id="bf-a" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto-start-reverse">'
     '<path d="M0,0 L6,3 L0,6 z" class="th-ink-f"/></marker>'
     '<marker id="bf-c" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto-start-reverse">'
     '<path d="M0,0 L6,3 L0,6 z" class="th-acc-f"/></marker></defs>']
for y in LINES:
    o.append(f'<path d="M20 {y} H{W-20}" class="th-faint" stroke-width="2" fill="none" stroke-linecap="round"/>')
# d marker
o.append(f'<path d="M590 {LINES[0]+4} V{LINES[1]-4}" class="th-ink" stroke-width="1.6" fill="none" marker-start="url(#bf-a)" marker-end="url(#bf-a)"/>')
o.append(f'<text x="602" y="{(LINES[0]+LINES[1])/2+6}" class="th-ink-f" style="{M};font-size:20px">d</text>')
# projection guides + bracket
bx = 150
for i in (top, bot):
    o.append(f'<path d="M{pts[i][0]:.1f} {pts[i][1]:.1f} H{bx+6}" class="th-acc" stroke-width="1.4" stroke-dasharray="4 4" fill="none"/>')
o.append(f'<path d="M{bx} {ymin+3:.1f} V{ymax-3:.1f}" class="th-acc" stroke-width="2.2" fill="none" marker-start="url(#bf-c)" marker-end="url(#bf-c)"/>')
o.append(f'<text x="{bx-14}" y="{(ymin+ymax)/2+7:.1f}" text-anchor="end" class="th-acc-f" style="{M};font-size:20px">w(θ)</text>')
# polygon
poly = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
o.append(f'<polygon points="{poly}" class="th-r2 th-ink" style="fill-opacity:.45" stroke-width="2.2" stroke-linejoin="round"/>')
# crossing points with the middle line
xs = []
for i in range(5):
    (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % 5]
    if (y1 - LINES[1]) * (y2 - LINES[1]) < 0:
        xs.append(x1 + (LINES[1] - y1) * (x2 - x1) / (y2 - y1))
for x in xs:
    o.append(f'<circle cx="{x:.1f}" cy="{LINES[1]}" r="5" class="th-warm-f"/>')
# orientation: reference ray + body ray + arc
ref = 100
bx2, by2 = cx + ref * math.cos(theta), cy - ref * math.sin(theta)
o.append(f'<path d="M{cx} {cy} H{cx+ref+14}" class="th-faint" stroke-width="1.4" stroke-dasharray="3 4" fill="none"/>')
o.append(f'<path d="M{cx} {cy} L{bx2:.1f} {by2:.1f}" class="th-ink" stroke-width="1.6" fill="none" marker-end="url(#bf-a)"/>')
ar = 46
o.append(f'<path d="M{cx+ar} {cy} A{ar} {ar} 0 0 0 {cx+ar*math.cos(theta):.1f} {cy-ar*math.sin(theta):.1f}" class="th-ink" stroke-width="1.4" fill="none"/>')
o.append(f'<text x="{cx+ar+16}" y="{cy-4}" class="th-ink-f" style="{M};font-size:18px">θ</text>')
o.append(f'<circle cx="{cx}" cy="{cy}" r="3" class="th-ink-f"/>')
# crossing label
if xs:
    o.append(f'<text x="{max(xs)+12:.1f}" y="{LINES[1]+22}" class="th-warm-f" style="font-size:13px;font-weight:600">2 boundary crossings</text>')
o.append('</svg>')
open(sys.argv[1], 'w').write(''.join(o))
print('w =', round(ymax - ymin, 1), 'crossings', len(xs))
