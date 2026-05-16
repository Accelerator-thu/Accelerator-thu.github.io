---
title: "Generalizing Buffon's Needle Problem to Polygons"
subtitle: "A geometric probability question from a CS70 discussion"
summary: "Extending Buffon's needle problem from line segments to polygons, through classic integral and expectation properties."
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

The classical Buffon's needle problem is a standard exercise in introductory probability: if a needle is dropped onto a ruled floor, what is the probability that it crosses a line?

The question came up while my advisor was teaching CS70. He mentioned that he was writing a solution to a related problem and asked what would happen if the thrown object were not a one-dimensional needle, but a two-dimensional convex polygon.

Moving from a line segment to a polygon introduces shape, orientation, and direction-dependent width. The probability should therefore depend on an intrinsic geometric quantity of the polygon, such as projected width, area, or perimeter. Under suitable assumptions, the relevant quantity turns out to be the perimeter. We derive this probability in two ways.

## The Classical Buffon's Needle Problem

First, establish the standard setup.

A plane is ruled with infinite, parallel lines spaced by a distance $d$. A needle of length $l$ is thrown onto this plane. The position of the needle's center is uniformly distributed modulo $d$, and its orientation $\theta$ is uniformly distributed over $[0, 2\pi)$.

When the needle is short enough to cross at most one line ($l \le d$), the crossing probability is:

{{< math >}}
$$
P(\text{crossing}) = \frac{2l}{\pi d}
$$
{{< /math >}}

## Reformulating the Problem

To generalize the problem to a polygon, we first identify what determines the crossing event.

For a rigid object with fixed orientation $\theta$, the probability of crossing one of the parallel horizontal lines is determined by its vertical span, or equivalently its projected width perpendicular to the lines. Denote this width by $w(\theta)$.

Assuming the object is small enough that $w(\theta) \le d$ for all $\theta$, the probability of intersection for a fixed orientation is:

{{< math >}}
$$
P(\text{crossing} \mid \theta) = \frac{w(\theta)}{d}
$$
{{< /math >}}

Because the orientation is chosen uniformly at random, the overall probability of a crossing is the expected value of this ratio over all possible angles:

{{< math >}}
$$
P(\text{crossing}) = \frac{\mathbb{E}_{\theta}[w(\theta)]}{d} = \frac{1}{2\pi d} \int_{0}^{2\pi} w(\theta) d\theta
$$
{{< /math >}}

The problem is therefore reduced to computing the average projected width of the polygon. We evaluate it using two approaches.

---

## Approach 1: The Geometric Projection

Start with a triangle, then generalize the argument to an arbitrary convex polygon.

Consider a triangle $T$ with edges $e_1, e_2, e_3$ of lengths $L_1, L_2, L_3$. When we project this triangle onto a vertical line, the projection is a line segment of length $w(\theta)$. 

Because the triangle is convex, its boundary maps onto the projection segment twice: one point from each of the two visible boundary chains maps to a typical interior point of the projection.

Thus, summing the vertical projections of the three edges counts the projected width twice. If $\phi_i$ denotes the appropriate edge-direction phase for $e_i$, the projected length of that edge at rotation $\theta$ is $L_i |\cos(\theta - \phi_i)|$. Therefore:

{{< math >}}
$$
2 w(\theta) = \sum_{i=1}^{3} L_i |\cos(\theta - \phi_i)|
$$
{{< /math >}}

To find the expected width over all orientations, we integrate over $\theta \in [0, 2\pi]$:

{{< math >}}
$$
\int_{0}^{2\pi} 2 w(\theta) d\theta = \sum_{i=1}^{3} L_i \int_{0}^{2\pi} |\cos(\theta - \phi_i)| d\theta
$$
{{< /math >}}

The integral of the absolute value of cosine over a full period is $4$, regardless of the phase shift $\phi_i$. Thus:

{{< math >}}
$$
2 \int_{0}^{2\pi} w(\theta) d\theta = \sum_{i=1}^{3} L_i (4) = 4 \sum_{i=1}^{3} L_i = 4P
$$
{{< /math >}}

where $P$ is the perimeter of the triangle. Dividing by 2, we get $\int w(\theta) d\theta = 2P$. The expected width is:

{{< math >}}
$$
\mathbb{E}_{\theta}[w(\theta)] = \frac{1}{2\pi} \int_{0}^{2\pi} w(\theta) d\theta = \frac{2P}{2\pi} = \frac{P}{\pi}
$$
{{< /math >}}

The same two-to-one projection argument holds for any convex polygon. Substituting the average width into the probability formula gives:

{{< math >}}
$$
P(\text{crossing}) = \frac{P}{\pi d}
$$
{{< /math >}}

---

## Approach 2: Linearity of Expectation

An alternative method uses linearity of expectation and avoids explicit integration.

Let $X$ be the total number of times the boundary of the convex polygon crosses the parallel lines. The perimeter consists of $n$ edges, $e_1, \dots, e_n$, with lengths $L_1, \dots, L_n$. 

Let $X_i$ be the number of times edge $e_i$ crosses a line, such that $X = \sum X_i$.

By the linearity of expectation, the expected total number of crossings is the sum of the expected crossings of each individual edge:

{{< math >}}
$$
\mathbb{E}[X] = \sum_{i=1}^{n} \mathbb{E}[X_i]
$$
{{< /math >}}

Each edge is a line segment. From the standard Buffon's needle computation, a segment of length $L_i$ has expected crossing count $\mathbb{E}[X_i] = \frac{2L_i}{\pi d}$. This expectation is unchanged by the fact that the segment is part of a polygon.

Summing these expectations gives:

{{< math >}}
$$
\mathbb{E}[X] = \sum_{i=1}^{n} \frac{2L_i}{\pi d} = \frac{2}{\pi d} \sum_{i=1}^{n} L_i = \frac{2P}{\pi d}
$$
{{< /math >}}

Next, relate the crossing count $X$ to the probability that the polygon intersects a line. If a convex polygon has maximum width strictly less than $d$, then whenever it crosses a line it intersects that line exactly twice, except for tangencies, which have probability zero.

Therefore, the random variable $X$ only takes the values $0$ or $2$. The expectation can be written as:

{{< math >}}
$$
\mathbb{E}[X] = 0 \cdot P(X = 0) + 2 \cdot P(X = 2) = 2 \cdot P(\text{crossing})
$$
{{< /math >}}

Equating the two expressions for $\mathbb{E}[X]$:

{{< math >}}
$$
2 \cdot P(\text{crossing}) = \frac{2P}{\pi d}
$$
{{< /math >}}

{{< math >}}
$$
P(\text{crossing}) = \frac{P}{\pi d}
$$
{{< /math >}}

Both methods yield the same conclusion: under the stated convexity and size assumptions, the crossing probability is determined by the perimeter $P$.

## Special Cases

The formula recovers several familiar cases.

### Line Segment
A line segment of length $l$ can be viewed as a degenerate convex polygon. Its boundary traverses the segment twice, so the effective perimeter is $P = 2l$. The formula gives $P(\text{crossing}) = \frac{2l}{\pi d}$, which is the classical Buffon's needle result.

### Rectangle
For a rectangle of dimensions $a \times b$, assuming $\sqrt{a^2 + b^2} \le d$, the perimeter is $P = 2(a+b)$. The crossing probability is $\frac{2(a+b)}{\pi d}$.

### Circle
As $n \to \infty$, a regular $n$-gon approaches a circle of radius $r$, with perimeter $P = 2\pi r$. The formula gives $P(\text{crossing}) = \frac{2\pi r}{\pi d} = \frac{2r}{d}$. Since $2r$ is the constant width (diameter) of the circle, it crosses a line whenever its center falls within $r$ of a line. Given the line spacing $d$, this exactly matches the probability $\frac{2r}{d}$.

## Subtleties and Assumptions

The formula above relies on several assumptions:

* **Convexity:** If the polygon is non-convex, the projection property in Approach 1 may fail, since a point in the projection can correspond to more than two boundary points. The assumption $X \in \{0, 2\}$ in Approach 2 can also fail. For the probability of hitting a line, the relevant width is determined by the convex hull, so the analogous formula involves the perimeter of the convex hull rather than the full boundary length of the non-convex polygon. The expected number of boundary crossings $\mathbb{E}[X] = \frac{2P}{\pi d}$ still holds for the original perimeter $P$; this is Buffon's noodle problem.
* **Size limitations:** We assumed the polygon's maximum width is strictly less than $d$. If the polygon can cross multiple lines simultaneously, then $P(X \ge 4)$ can be positive, and the relation $\mathbb{E}[X] = 2 P(\text{crossing})$ no longer holds.

## Closing Thoughts

Generalizing Buffon's needle to polygons shows how geometric quantities can arise from elementary probabilistic experiments. By reducing a two-dimensional shape to its one-dimensional boundary, the crossing probability becomes a function of perimeter under the assumptions above.

The second proof is also a useful reminder of the role of indicator functions. In probability, every event can be represented by an indicator:

{{< math >}}
$$
\mathbf{1}_A(\omega) =
\begin{cases}
1, & \omega \in A, \\
0, & \omega \notin A.
\end{cases}
$$
{{< /math >}}

This simple function is a fundamental building block. In measure theory, indicator functions play the role of elementary functions for measurable sets: more general integrable random variables can be approximated by linear combinations of indicators. Thus, when we write the crossing count as

{{< math >}}
$$
X = \sum_i \mathbf{1}\{\text{edge } i \text{ crosses a line}\}.
$$
{{< /math >}}

we decompose the experiment into elementary measurable events.

Linearity of expectation then reflects the linearity of counting. Taking expectation of an indicator measures the probability mass of the corresponding event:

{{< math >}}
$$
\mathbb{E}[\mathbf{1}_A] = P(A).
$$
{{< /math >}}

Adding indicators counts coverage with multiplicity. If two events overlap, outcomes in the overlap contribute to both indicators. This operation does not require the events to be disjoint or independent. Independence concerns factorization of probabilities of intersections; linearity of expectation concerns only addition of measurable functions.

In this sense, the Buffon polygon problem reduces to a basic principle: expectation is integration, indicators measure events, and sums of indicators count how many events cover each outcome. The geometry supplies the edges, the probability space supplies the random throws, and linearity converts local crossing events into a global expected count. The random experiment is therefore a way of measuring geometry through the linear structure of indicator functions.
