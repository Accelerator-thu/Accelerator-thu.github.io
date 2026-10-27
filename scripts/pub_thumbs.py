#!/usr/bin/env python3
# Usage: python3 scripts/pub_thumbs.py content/publications
"""Generate theme-aware publication thumbnails (thumb.svg) for the homepage.
Colors come from CSS classes (.th-*) defined in custom-styles.html, so the same
SVG adapts to light/dark mode. Each motif depicts the paper's core mechanism."""
import math, sys, pathlib
OUT = pathlib.Path(sys.argv[1])

def svg(body):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" '
            'class="pub-svg" role="img" aria-hidden="true">'
            '<defs><marker id="ah" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="3" markerHeight="3" orient="auto">'
            '<path d="M0,0 L6,3 L0,6 z" class="th-ink-f"/></marker>'
            '<marker id="aha" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="3" markerHeight="3" orient="auto">'
            '<path d="M0,0 L6,3 L0,6 z" class="th-acc-f"/></marker></defs>'
            + body + '</svg>')

def line(x1,y1,x2,y2,c='th-ink',w=2,extra=''):
    return f'<path d="M{x1} {y1} L{x2} {y2}" class="{c}" stroke-width="{w}" fill="none" stroke-linecap="round" {extra}/>'
def dot(x,y,r=3.2,c='th-ink-f'): return f'<circle cx="{x}" cy="{y}" r="{r}" class="{c}"/>'
def sq(x,y,c,s=8,extra=''): return f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="1.6" class="{c}" {extra}/>'

# ---------- PEINT: phylogram (width = branch length / time), dot nodes,
# residue squares at tips; substitutions accented, one insertion (no gaps).
def peint():
    b=[]
    root=(12,60)
    # internal nodes
    n1=(28,36); n2=(36,84)
    tips=[(56,22,['r1','r2','r3','r4']),
          (48,48,['r1','acc','r3','r4']),
          (60,74,['r1','r2','acc','r3','r4']),  # insertion -> 5 residues, no gaps
          (52,100,['r1','r2','r3','acc'])]
    # elbows
    for (px,py),(cx,cy) in [(root,n1),(root,n2),(n1,tips[0][:2]),(n1,tips[1][:2]),(n2,tips[2][:2]),(n2,tips[3][:2])]:
        b.append(f'<path d="M{px} {py} V{cy} H{cx}" class="th-ink" stroke-width="2" fill="none" stroke-linejoin="round"/>')
    b.append(line(5,60,12,60))
    for p in [root,n1,n2]: b.append(dot(*p))
    for x,y,res in tips:
        b.append(dot(x,y))
        for i,c in enumerate(res):
            cls={'r1':'th-r1','r2':'th-r2','r3':'th-r3','r4':'th-r4','acc':'th-warm-f'}[c]
            b.append(sq(x+6+i*9.6,y-4,cls))
    # ancestral sequence at root (above)
    return svg(''.join(b))

# ---------- Proactive: six capacities as a cycle (aware, anticipate, agenda,
# arbitrate, act, adapt); 'act' leaves the loop unprompted (accent arrow out).
def proactive():
    b=[]; cx,cy,R=54,62,32
    pts=[(cx+R*math.cos(math.radians(-90+60*i)),cy+R*math.sin(math.radians(-90+60*i))) for i in range(6)]
    for i in range(6):
        a0=-90+60*i+14; a1=-90+60*(i+1)-14
        x0,y0=cx+R*math.cos(math.radians(a0)),cy+R*math.sin(math.radians(a0))
        x1,y1=cx+R*math.cos(math.radians(a1)),cy+R*math.sin(math.radians(a1))
        b.append(f'<path d="M{x0:.1f} {y0:.1f} A{R} {R} 0 0 1 {x1:.1f} {y1:.1f}" class="th-faint" stroke-width="2" fill="none" marker-end="url(#ah)"/>')
    for i,(x,y) in enumerate(pts):
        b.append(dot(x,y,5.2,'th-warm-f' if i==4 else 'th-ink-f'))
    # agent at center
    b.append(dot(cx,cy,7,'th-acc-f'))
    # self-initiated action: from 'act' node outward
    ax,ay=pts[4]  # bottom-left? index4 -> angle 150deg
    ax,ay=pts[2]  # angle 30deg (right-lower)
    b=[x for x in b]
    b[-2:-1]=b[-2:-1]
    b.append(f'<path d="M{ax+7:.1f} {ay+2:.1f} Q{ax+22:.1f} {ay+6:.1f} {110} {ay+22:.1f}" class="th-acc" stroke-width="2.4" fill="none" marker-end="url(#aha)"/>')
    # recolor: make node 2 the accented 'act' node
    out=''.join(b).replace(f'cx="{pts[4][0]}" cy="{pts[4][1]}" r="5.2" class="th-warm-f"',f'cx="{pts[4][0]}" cy="{pts[4][1]}" r="5.2" class="th-ink-f"')
    out=out.replace(f'cx="{pts[2][0]}" cy="{pts[2][1]}" r="5.2" class="th-ink-f"',f'cx="{pts[2][0]}" cy="{pts[2][1]}" r="5.2" class="th-warm-f"')
    return svg(out)

# ---------- GraphSR: graph-structured system -> message-passing flow
# (edge functions as squares on edges, node aggregation) -> symbolic expression tree.
def graphsr():
    b=[]
    N=[(14,34),(42,20),(46,58),(18,84),(44,98)]
    E=[(0,1),(0,2),(1,2),(0,3),(3,4),(2,4)]
    for i,j in E:
        (x1,y1),(x2,y2)=N[i],N[j]; b.append(line(x1,y1,x2,y2,'th-faint',2))
        mx,my=(x1+x2)/2,(y1+y2)/2; b.append(sq(mx-3.2,my-3.2,'th-acc-f',6.4))
    for x,y in N: b.append(dot(x,y,4.6))
    b.append(line(58,60,72,60,'th-ink',2,'marker-end="url(#ah)"'))
    # expression tree:  (+) over (x) and leaf
    T={'r':(96,34),'a':(84,62),'b':(108,62),'c':(76,90),'d':(92,90)}
    for p,c in [('r','a'),('r','b'),('a','c'),('a','d')]:
        b.append(line(*T[p],*T[c],'th-ink',2))
    for k in ['r','a']: b.append(dot(*T[k],6.2,'th-warm-f'))
    for k in ['b','c','d']: b.append(dot(*T[k],3.6))
    # operator glyphs (+, x) drawn as strokes
    rx,ry=T['r']; b.append(line(rx-3,ry,rx+3,ry,'th-bg',1.6)+line(rx,ry-3,rx,ry+3,'th-bg',1.6))
    ax,ay=T['a']; b.append(line(ax-2.3,ay-2.3,ax+2.3,ay+2.3,'th-bg',1.6)+line(ax-2.3,ay+2.3,ax+2.3,ay-2.3,'th-bg',1.6))
    return svg(''.join(b))

# ---------- AutoRec: weight-sharing supernet (all candidate ops faint), one
# searched architecture highlighted, co-designed with a PIM hardware block.
def autorec():
    b=[]; cols=[12,36,60,84]; rows=[30,60,90]
    for ci in range(3):
        for r1 in rows:
            for r2 in rows: b.append(line(cols[ci],r1,cols[ci+1],r2,'th-faint',1.4))
    path=[(12,60),(36,30),(60,90),(84,60)]
    for (x1,y1),(x2,y2) in zip(path,path[1:]): b.append(line(x1,y1,x2,y2,'th-acc',2.8))
    for x in cols:
        for y in rows: b.append(dot(x,y,3.6,'th-acc-f' if (x,y) in path else 'th-ink-f'))
    # PIM chip
    b.append(line(88,60,96,60,'th-acc',2.8))
    b.append(f'<rect x="97" y="48" width="18" height="24" rx="3" class="th-warm-f"/>')
    for y in (53,60,67):
        b.append(line(115,y,118,y,'th-ink',1.6)); 
    for x in (101,106,111):
        b.append(line(x,45,x,48,'th-ink',1.6)+line(x,72,x,75,'th-ink',1.6))
    return svg(''.join(b))

# ---------- TSNAS / FGPS: candidate paths in architecture space; size ~ estimated
# quality. Farthest greedy sampling picks high-quality, mutually distant paths
# (accent, linked in selection order) instead of a clustered top-k.
def tsnas():
    import random; random.seed(7)
    pts=[]
    while len(pts)<34:
        x,y=random.uniform(12,108),random.uniform(12,108)
        if all((x-a)**2+(y-b_)**2>110 for a,b_,_ in pts): pts.append((x,y,random.random()))
    b=[]
    # greedy farthest selection among top-60% quality
    cand=[p for p in pts if p[2]>0.4]; sel=[max(cand,key=lambda p:p[2])]
    while len(sel)<5:
        sel.append(max([p for p in cand if p not in sel],key=lambda p:min((p[0]-s[0])**2+(p[1]-s[1])**2 for s in sel)*(0.5+p[2])))
    for p in pts:
        if p in sel: continue
        b.append(dot(p[0],p[1],1.6+2.4*p[2],'th-faint-f'))
    for i,p in enumerate(sel):
        r=2.4+2.6*p[2]
        b.append(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{r+4:.1f}" class="th-acc" stroke-width="1.4" fill="none"/>')
        b.append(dot(p[0],p[1],r,'th-warm-f' if i==0 else 'th-acc-f'))
    return svg(''.join(b))

for name,fn in [('peint',peint),('proactive-agents',proactive),('graphsr',graphsr),('autorec',autorec),('tsnas',tsnas)]:
    (OUT/name/'thumb.svg').write_text(fn())
print('ok')
