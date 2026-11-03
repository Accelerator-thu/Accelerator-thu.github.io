#!/usr/bin/env python3
# Usage: python3 scripts/misc_thumbs.py assets/misc
"""Generate theme-aware thumbnails for the Misc page cards (assets/misc/*.svg).
Same .th-* colour classes as scripts/pub_thumbs.py, so they adapt to light/dark mode.
Rendered by layouts/shortcodes/misc-cards.html from entries in data/misc.yaml."""
import sys, pathlib
OUT = pathlib.Path(sys.argv[1])
HEAD = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" class="pub-svg" role="img" aria-hidden="true">'

def four_in_a_row():
    # Isometric 4x4x4 board: four stacked layers, a winning space diagonal (warm)
    # from the bottom-front corner to the top-back corner, plus a few other stones.
    a, b, h = 10.5, 4.8, 17.0          # half-cell width, half-cell height, layer rise
    cx, base = 60, 102                  # front vertex of bottom layer
    def P(i, j, k):                      # grid coords (0..4) -> screen
        return cx + (i - j) * a, base - (i + j) * b - k * h
    out = [HEAD]
    others = {0: [(2, 2, 'th-r1')], 1: [(2, 3, 'th-r1')], 2: [(1, 1, 'th-r1')], 3: [(3, 3, 'th-r1')]}
    win = [(k, 3 - k, k) for k in range(4)]   # space diagonal: sweeps left -> right while rising
    for k in range(4):
        pts = [P(0, 0, k), P(4, 0, k), P(4, 4, k), P(0, 4, k)]
        d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + ' Z'
        out.append(f'<path d="{d}" class="th-faint" style="fill:var(--th-bg);fill-opacity:.6" stroke-width="1.4" stroke-linejoin="round"/>')
        for t in (1, 2, 3):              # faint grid
            (x1, y1), (x2, y2) = P(t, 0, k), P(t, 4, k)
            (x3, y3), (x4, y4) = P(0, t, k), P(4, t, k)
            out.append(f'<path d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f} M{x3:.1f} {y3:.1f} L{x4:.1f} {y4:.1f}" class="th-faint" stroke-width=".6" opacity=".55" fill="none"/>')
        for i, j, c in others.get(k, []):
            x, y = P(i + .5, j + .5, k)
            out.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="5.2" ry="3.1" class="{c}"/>')
        i, j, _ = win[k]
        x, y = P(i + .5, j + .5, k)
        out.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="5.8" ry="3.4" class="th-warm-f"/>')
    (x0, y0), (x3, y3) = P(.5, 3.5, 0), P(3.5, .5, 3)
    out.append(f'<path d="M{x0:.1f} {y0:.1f} L{x3:.1f} {y3:.1f}" class="th-acc" stroke-width="1.6" stroke-dasharray="2.5 2.5" stroke-linecap="round" fill="none"/>')
    out.append('</svg>')
    return ''.join(out)

def photos():
    # Two tilted prints behind a front print with a mountain + sun motif.
    out = [HEAD]
    def frame(cx, cy, rot, inner):
        return (f'<g transform="rotate({rot} {cx} {cy})">'
                f'<rect x="{cx-30}" y="{cy-34}" width="60" height="68" rx="3" style="fill:var(--th-bg)" class="th-faint" stroke-width="1.6"/>'
                + inner + '</g>')
    out.append(frame(50, 58, -12, f'<rect x="26" y="30" width="48" height="44" rx="1.5" class="th-r3" opacity=".55"/>'))
    out.append(frame(70, 58, 10, f'<rect x="46" y="30" width="48" height="44" rx="1.5" class="th-r2" opacity=".55"/>'))
    inner = ('<rect x="36" y="30" width="48" height="44" rx="1.5" class="th-r1" opacity=".22"/>'
             '<circle cx="72" cy="41" r="5" class="th-warm-f"/>'
             '<path d="M36 74 L52 50 L62 63 L68 56 L84 74 Z" class="th-r1"/>'
             '<path d="M36 74 L52 50 L58 58" class="th-ink" stroke-width="1.2" fill="none" opacity=".5"/>')
    out.append(frame(60, 60, 0, inner))
    out.append('<path d="M44 86 h32" class="th-faint" stroke-width="1.6" stroke-linecap="round"/>')
    out.append('</svg>')
    return ''.join(out)

(OUT / 'four-in-a-row.svg').write_text(four_in_a_row())
(OUT / 'photos.svg').write_text(photos())
print('wrote', list(OUT.glob('*.svg')))
