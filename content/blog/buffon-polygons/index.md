---
title: "Generalizing Buffon's Needle Problem to Polygons"
subtitle: "When you throw a convex polygon onto a ruled floor, the crossing probability depends only on the perimeter"
summary: "Extending Buffon's needle problem from line segments to convex polygons — a clean result that falls out of two independent arguments: direct integration and linearity of expectation."
date: 2026-05-06
draft: false

authors:
  - me

tags:
  - Probability
  - Brain Teaser
  - Random
---

{{< toc mobile_only=true is_open=true >}}

## Motivation

The classical Buffon's needle problem asks: if a needle is dropped onto a ruled floor, what is the probability that it crosses a line? It is a standard exercise, with a clean answer involving $\pi$.

The question came up while my advisor was teaching CS70. He asked what happens if the thrown object is not a one-dimensional needle but a two-dimensional convex polygon.

The answer is clean: the crossing probability depends only on the perimeter. Not the area, not the shape — just the total boundary length. We derive this two ways.

## The Classical Setup

A plane is ruled with infinite parallel lines spaced distance $d$ apart. A needle of length $l \le d$ is thrown at random: its center uniform modulo $d$, its orientation $\theta$ uniform over $[0, 2\pi)$. The crossing probability is:

{{< math >}}
$$
P(\text{crossing}) = \frac{2l}{\pi d}
$$
{{< /math >}}

## Reducing to Average Width

For any rigid object at orientation $\theta$, the relevant quantity is its projected width $w(\theta)$ perpendicular to the lines. If $w(\theta) \le d$ for all $\theta$, the conditional crossing probability is $w(\theta)/d$. Averaging over the uniform orientation:

{{< math >}}
$$
P(\text{crossing}) = \frac{\mathbb{E}_{\theta}[w(\theta)]}{d} = \frac{1}{2\pi d} \int_{0}^{2\pi} w(\theta)\, d\theta
$$
{{< /math >}}

Everything reduces to computing the average projected width of the polygon.

---

## Approach 1: Direct Integration

Consider a convex polygon with edges $e_1, \dots, e_n$ of lengths $L_1, \dots, L_n$ and edge-direction phases $\phi_1, \dots, \phi_n$.

For a convex shape, the boundary covers each point of the projection exactly twice — once from each visible side. So summing the edge projections counts $w(\theta)$ twice:

{{< math >}}
$$
2 w(\theta) = \sum_{i=1}^{n} L_i |\cos(\theta - \phi_i)|
$$
{{< /math >}}

Integrating over $\theta \in [0, 2\pi]$: the absolute cosine integrates to $4$ over a full period regardless of phase, so:

{{< math >}}
$$
2 \int_{0}^{2\pi} w(\theta)\, d\theta = \sum_{i=1}^{n} 4L_i = 4P
$$
{{< /math >}}

where $P$ is the perimeter. Therefore the average width is $P/\pi$, and:

{{< math >}}
$$
P(\text{crossing}) = \frac{P}{\pi d}
$$
{{< /math >}}

---

## Approach 2: Linearity of Expectation

Let $X$ count how many times the polygon's boundary crosses a line, and let $X_i$ count crossings for edge $e_i$, so $X = \sum_i X_i$.

Each edge is just a needle. By the standard Buffon result, $\mathbb{E}[X_i] = \frac{2L_i}{\pi d}$, independently of the rest of the polygon. Summing:

{{< math >}}
$$
\mathbb{E}[X] = \sum_{i=1}^{n} \frac{2L_i}{\pi d} = \frac{2P}{\pi d}
$$
{{< /math >}}

Now use the convexity assumption. If the polygon's maximum width is less than $d$, it can cross at most one line at a time, and a convex shape crosses any line either zero times or twice (tangencies have probability zero). So $X \in \{0, 2\}$ and:

{{< math >}}
$$
\mathbb{E}[X] = 2\cdot P(\text{crossing})
$$
{{< /math >}}

Equating the two expressions:

{{< math >}}
$$
P(\text{crossing}) = \frac{P}{\pi d}
$$
{{< /math >}}

Both approaches give the same answer. The geometry is doing the same work in both cases — one makes it explicit through integration, the other hides it inside the needle formula.

## Sanity Checks

**Line segment.** A segment of length $l$ traverses its boundary twice, giving effective perimeter $P = 2l$. The formula returns $\frac{2l}{\pi d}$ — exactly the classical result.

**Rectangle.** A rectangle $a \times b$ has perimeter $P = 2(a+b)$, giving crossing probability $\frac{2(a+b)}{\pi d}$.

**Circle.** A circle of radius $r$ has perimeter $P = 2\pi r$, giving $P(\text{crossing}) = \frac{2r}{d}$. This is also immediate geometrically: a circle crosses a line iff its center falls within $r$ of it, which happens with probability $2r/d$. The formula agrees.

## Where the Assumptions Matter

**Convexity** is load-bearing in both proofs. In Approach 1, a non-convex boundary can project more than two-to-one, breaking the identity. In Approach 2, $X \in \{0, 2\}$ can fail for non-convex shapes. The crossing probability then involves the convex hull's perimeter, not the original boundary length. (The expected crossing count $\frac{2P}{\pi d}$ still holds for the original $P$ — this is Buffon's noodle problem.)

**Size** must satisfy maximum width $< d$. If the polygon can span multiple lines, the two-crossing argument breaks down and the formula no longer gives the intersection probability.

## Closing Thoughts

The result is clean: throw a convex polygon at a ruled floor, and only the perimeter determines whether it crosses a line. Shape, area, and number of sides are irrelevant.

What makes both proofs satisfying is that they arrive at the same answer through different decompositions of the same randomness. The first integrates a global quantity directly. The second writes a global event as a sum of independent local ones and lets linearity do the work:

{{< math >}}
$$
X = \sum_i \mathbf{1}\{\text{edge } i \text{ crosses a line}\}
$$
{{< /math >}}

Linearity of expectation requires no independence between the terms — just that expectation is linear. That is what makes it powerful here: the edges are geometrically correlated, but their expected contributions add regardless.
