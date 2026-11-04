---
title: "Reinventing the Twist"
subtitle: "How you could have discovered the matrix exponential, Lie algebras, screw axes, and Chasles' theorem yourself"
summary: "Starting from one question about moving a book, we reinvent the matrix exponential, the Lie bracket, Rodrigues' formula, twists, Plücker coordinates and dual numbers, and arrive at Chasles' theorem: every rigid motion is a screw."
date: 2026-10-27
draft: false

authors:
  - me

tags:
  - Lie Groups
  - Differential Geometry
  - Robotics
  - Mathematics
---

{{< toc mobile_only=true is_open=true >}}

## The question

A book lies on a desk. You pick it up, wave it around, and put it down somewhere else in a new orientation. Forget the path your hand took and look only at the two poses, before and after.

> **Is there a *simplest* motion that takes the first pose to the second?**

"Simplest" is vague on purpose. Here is one candidate meaning: a motion you could perform with your hand held *perfectly steady*, repeating the same instantaneous movement over and over until you arrive. A pure rotation about a hinge is like that. So is a pure slide. Is every change of pose like that?

The answer is yes, and the steady motion always has a specific shape: **turn about one fixed line in space while sliding along that same line**, like a bolt driven into a nut. This is Chasles' theorem (1830).

This post is an attempt to reach that answer the way you might if nobody had told you. Every tool we use (the matrix exponential, the Lie bracket, Rodrigues' formula, twists, Plücker coordinates, dual numbers) will show up because we need it, at the moment the naive approach fails. The goal is that by the end, each of them feels less like a definition and more like something you would have written down yourself.

## 1. What is a motion?

Before asking about the simplest motion, we need to say what a motion is. All we know about a rigid body is that **distances between its points don't change**. So a rigid displacement is a map $g : \mathbb{R}^3 \to \mathbb{R}^3$ with

{{< math >}}
$$
|g(p) - g(q)| = |p - q| \quad \text{for all } p, q.
$$
{{< /math >}}

What can such a map look like? Let $d = g(0)$ and $R(p) = g(p) - d$. Then $R$ fixes the origin and preserves distances, so it preserves lengths $|R(p)| = |p|$. Expanding $|R(p) - R(q)|^2 = |p - q|^2$ shows it also preserves dot products. A map that preserves dot products sends an orthonormal basis to an orthonormal basis and preserves every coordinate, so it is linear. So:

{{< math >}}
$$
g(p) = Rp + d, \qquad R^\top R = I.
$$
{{< /math >}}

A physical body can't turn itself into its mirror image, so $\det R = +1$. Call the set of these maps $SE(3)$.

Two things to notice right away.

**Motions compose.** Doing $g_2$ and then $g_1$ gives

{{< math >}}
$$
(R_1, d_1)\cdot(R_2, d_2) = (R_1 R_2,\; d_1 + R_1 d_2).
$$
{{< /math >}}

The rotation parts multiply, but the translation parts get tangled up with rotation. We can untangle the bookkeeping with a trick: append a 1 to every point, $p \mapsto (p, 1)$. Then the motion becomes a single matrix,

{{< math >}}
$$
g = \begin{pmatrix} R & d \\ 0 & 1 \end{pmatrix}, \qquad g \begin{pmatrix} p \\ 1 \end{pmatrix} = \begin{pmatrix} Rp + d \\ 1 \end{pmatrix},
$$
{{< /math >}}

and composition becomes matrix multiplication. Now $SE(3)$ is a group of $4 \times 4$ matrices, six-dimensional: three numbers for the rotation, three for the translation.

**Rotations and translations are not on equal footing.** Conjugate a translation by any motion and you get another translation. But conjugate a rotation about the origin by a translation and you get a rotation about *a different point*. Translations are canonical. A rotation needs a center, and nothing in space tells you where the center should be.

Hold on to that asymmetry. The whole answer to our question is hiding in it.

## 2. Holding the hand steady: reinventing the exponential

### Velocities

What does it mean to "hold your hand steady"? It means the *velocity* of the motion doesn't change. So first we need to know what a velocity of a motion is.

Take a curve of motions $g(t)$ with $g(0) = I$ (no motion yet). Its velocity at the start is the matrix $X = \dot g(0)$. Which matrices $X$ can occur? Differentiate whatever constraint defines the group. For example, for a curve of rotations, differentiating $R(t)^\top R(t) = I$ at $t = 0$ gives

{{< math >}}
$$
\dot R(0)^\top + \dot R(0) = 0.
$$
{{< /math >}}

So the velocities of rotations are exactly the **skew-symmetric** matrices. This recipe (*differentiate the constraint at the identity*) works for any group defined by equations, and it always gives a *vector space* of velocities, even when the group itself is curved. That vector space is called the **Lie algebra** of the group. We'll find out what it looks like for rigid motions in Section 4.

### Steady motion is compound interest

Now hold the velocity $X$ fixed. "Steady" should mean the motion looks the same at every instant, relative to where you currently are: the change over the next short time $\Delta t$ is always $I + X\Delta t$, applied on top of the current pose. Approximate time $1$ by $n$ such steps:

{{< math >}}
$$
g(1) \approx \left(I + \frac{X}{n}\right)^n.
$$
{{< /math >}}

This is exactly the compound-interest limit, now with a matrix instead of an interest rate. Expanding with the binomial theorem (legal, since $X$ commutes with itself) and letting $n \to \infty$, the $k$-th term tends to $X^k/k!$:

{{< math >}}
$$
\lim_{n \to \infty}\left(I + \frac{X}{n}\right)^n = \sum_{k \ge 0} \frac{X^k}{k!} =: e^X.
$$
{{< /math >}}

So the **matrix exponential is not a formal analogy with $e^x$**. It is the unique answer to "what happens if I repeat the same infinitesimal motion forever". Equivalently, $x(t) = e^{tX}x_0$ solves $\dot x = Xx$: the matrix $X$ is a velocity rule assigning a velocity $Xx$ to each state $x$, and $e^{tX}$ is the result of following it.

<div class="post-demo post-demo-flow not-prose">
  <iframe src="/demos/flow-explorer.html" title="Interactive explorer: a 2×2 matrix X as the velocity field x ↦ Xx and its flow e^{tX}" loading="lazy"></iframe>
  <p>Grey arrows: the velocity <em>Xx</em> at each point. The orange curve is the orbit of a point you can drag, and the teal arrow is its velocity, always tangent to the orbit. The shaded shape is the unit square after <em>e<sup>tX</sup></em>. <a href="/demos/flow-explorer.html" target="_blank" rel="noopener">Open full screen ↗</a></p>
</div>

Because steadiness means "the next step looks like the previous one", the curve $t \mapsto e^{tX}$ automatically satisfies

{{< math >}}
$$
e^{(s+t)X} = e^{sX}\, e^{tX}.
$$
{{< /math >}}

A curve with this property is a **one-parameter subgroup**. So our vague question now has a precise form:

> **Is every rigid motion $g$ of the form $e^X$ for some velocity $X$?**

Before answering it, let's see what goes wrong when two velocities are combined.

### Two velocities: discovering the bracket

If $e^{X+Y}$ were always $e^X e^Y$, the exponential would turn the vector space of velocities into the group with no loss of information. Let's test it with the cheapest experiment there is. Move a small amount along $X$, then $Y$, then back along $X$, then back along $Y$:

{{< math >}}
$$
e^{tX}\, e^{tY}\, e^{-tX}\, e^{-tY}.
$$
{{< /math >}}

If motions commuted, this would return you exactly to the start. Expand each factor to second order and multiply. Every first-order term cancels, the squares cancel, and what is left is

{{< math >}}
$$
e^{tX}\, e^{tY}\, e^{-tX}\, e^{-tY} = I + t^2 (XY - YX) + O(t^3).
$$
{{< /math >}}

The gap left by walking around a small rectangle is second order, and its direction is the matrix

{{< math >}}
$$
[X, Y] = XY - YX.
$$
{{< /math >}}

We didn't define the **Lie bracket**. We measured it, as the failure of a small loop to close. (If you know some differential geometry: this is exactly how curvature shows up, as the failure of parallel transport around a small loop to return a vector to itself.)

The Baker–Campbell–Hausdorff formula goes all the way. $\log(e^X e^Y)$ equals $X + Y + \tfrac12[X,Y] + \cdots$, where every further term is built from iterated brackets. So near the identity, **the vector space of velocities, together with the bracket, contains the entire multiplication of the group.** That is why it pays to understand the velocities first.

## 3. Rotations, by thinking about what they do

### Counting

A skew-symmetric $3\times 3$ matrix has three free entries. Write them as a vector $\omega$:

{{< math >}}
$$
\hat\omega = \begin{pmatrix} 0 & -\omega_3 & \omega_2 \\ \omega_3 & 0 & -\omega_1 \\ -\omega_2 & \omega_1 & 0 \end{pmatrix}.
$$
{{< /math >}}

Multiply it by a vector and you find $\hat\omega\, p = \omega \times p$. So the velocity rule $\dot p = \hat\omega p$ is the familiar velocity field of something spinning with angular velocity $\omega$ about an axis through the origin.

It is worth pausing on *why* a velocity of rotation looks like a vector. In $n$ dimensions, skew matrices have $\binom{n}{2}$ entries, one per coordinate plane. An angular velocity really specifies a **plane of rotation** and a rate. Only for $n = 3$ is $\binom{n}{2} = n$, so that a plane can be traded for its normal vector. The cross product is the shadow of that coincidence. Check, by multiplying out, that the bracket becomes the cross product:

{{< math >}}
$$
[\hat a, \hat b] = \widehat{a \times b}.
$$
{{< /math >}}

So the reason "rotations don't commute" and the reason "$a \times b \neq 0$" are the same reason.

### Rodrigues' formula, without summing a series

We want $e^{\theta\hat\omega}$ for a unit vector $\omega$. Don't expand the series yet. Instead ask: *what does $\hat\omega$ do?*

- On the axis, it does nothing: $\omega \times \omega = 0$.
- On the plane perpendicular to $\omega$, it turns every vector by $90°$ (and keeps its length, since $|\omega| = 1$).

Turning by $90°$ twice gives $-1$. So on that plane, $\hat\omega$ behaves exactly like the imaginary unit $i$. Now we don't need to compute anything:

- On the axis, $e^{\theta\hat\omega}$ is $e^0 = 1$: the axis is fixed.
- On the plane, $e^{\theta\hat\omega}$ is $e^{\theta i} = \cos\theta + i\sin\theta$: a rotation by $\theta$.

To write this as one formula, we need the projections. The projection onto the plane is $-\hat\omega^2$ (turn by $90°$ twice, negate), and the projection onto the axis is $I + \hat\omega^2$. Assembling the pieces:

{{< math >}}
$$
e^{\theta\hat\omega} = \underbrace{(I + \hat\omega^2)}_{\text{axis}} + \cos\theta\,\underbrace{(-\hat\omega^2)}_{\text{plane}} + \sin\theta\, \underbrace{\hat\omega}_{\text{“}i\text{”}} = I + \sin\theta\,\hat\omega + (1 - \cos\theta)\,\hat\omega^2.
$$
{{< /math >}}

This is **Rodrigues' formula**. Seen this way it is Euler's formula, applied on the one plane where $\hat\omega$ acts like $i$.

### Every rotation is steady

Is every rotation $R$ of the form $e^{\theta\hat\omega}$? We need an axis: a vector $R$ fixes. The eigenvalues of $R$ have modulus 1, come in complex-conjugate pairs, and multiply to $\det R = 1$. In three dimensions there are three of them, so at least one is real. If it is $-1$, the other two multiply to $-1$, so they are real too, namely $1$ and $-1$. Either way, $1$ is an eigenvalue. Rotate about that axis, and Rodrigues takes care of the rest.

So for rotations alone, the answer to our question is yes. Notice that the argument used the **oddness of the dimension**. In four dimensions, a typical rotation turns two perpendicular planes by two different angles and fixes no direction at all.

## 4. Velocities of rigid motions

### Differentiate again

Apply the same recipe to $SE(3)$. A curve $g(t) = \begin{pmatrix} R(t) & d(t) \\ 0 & 1 \end{pmatrix}$ through the identity has velocity

{{< math >}}
$$
\hat\xi = \begin{pmatrix} \hat\omega & v \\ 0 & 0 \end{pmatrix}, \qquad \xi = (v, \omega),
$$
{{< /math >}}

with $\hat\omega$ skew (from the rotation part) and $v$ arbitrary. This is a **twist**. Acting on a point $(p, 1)$, it gives a velocity

{{< math >}}
$$
X_\xi(p) = v + \omega \times p.
$$
{{< /math >}}

So a twist is not an arrow attached to the body. **It is a velocity field on all of space**: a rule that tells every point how to move. $\omega$ is the angular velocity, the same at every point. $v$ is the velocity of whatever happens to be at the origin right now.

### You could have guessed the twist without matrices

Here is a way to arrive at the same formula from scratch, without any matrices at all. Which velocity fields $X$ preserve distances, at least instantaneously? We need

{{< math >}}
$$
\frac{d}{dt}|p - q|^2 = 2\,\big(X(p) - X(q)\big)\cdot(p - q) = 0 \quad\text{for all } p, q.
$$
{{< /math >}}

Subtract off the velocity of the origin: let $Y(p) = X(p) - X(0)$. Then $Y$ satisfies the same condition and $Y(0) = 0$. Taking $q = 0$ gives $Y(p)\cdot p = 0$ for every $p$. Expanding the general condition and cancelling those terms leaves

{{< math >}}
$$
Y(p)\cdot q = -\,p\cdot Y(q).
$$
{{< /math >}}

The right side is linear in $p$. So for each fixed $q$, $p \mapsto Y(p)\cdot q$ is linear, which means $Y$ itself is linear. And the identity says that this linear map is skew-symmetric. We have shown:

{{< math >}}
$$
X(p) = v + Ap, \qquad A^\top = -A.
$$
{{< /math >}}

That is the twist, rediscovered from nothing but "distances don't change". In differential geometry, such fields are called **Killing fields**: the infinitesimal symmetries of a space. So the Lie algebra of $SE(3)$ is the space of infinitesimal symmetries of Euclidean space, and we could have defined it that way. Note that we never assumed smoothness, or even continuity; the condition alone forced $X$ to be affine.

## 5. Looking for the center, and failing

### The naive idea

Here is the most natural guess for the "simplest motion". Every steady rigid motion is a rotation about some center. Find the center, and you're done.

What would the center be? A point that doesn't move. So try to solve

{{< math >}}
$$
X_\xi(p) = v + \omega \times p = 0.
$$
{{< /math >}}

Take $\omega \neq 0$. The term $\omega \times p$ is always perpendicular to $\omega$, whatever $p$ is. So this equation can only be solved if $v$ is perpendicular to $\omega$ too. In general it isn't.

**The naive idea fails, and the way it fails is the answer.** Split $v$ into the part along $\omega$ and the part across it:

{{< math >}}
$$
v = v_\parallel + v_\perp.
$$
{{< /math >}}

The $v_\perp$ part can be cancelled by choosing $p$ well. The $v_\parallel$ part can't be cancelled by anything.

### Moving the origin

Let's say the same thing in a way that will generalize. "Where is the origin?" was an arbitrary choice. If we move it to the point $d$, the new coordinates are $p' = p - d$, and the field becomes

{{< math >}}
$$
X(p) = v + \omega \times (p' + d) = \underbrace{(v + \omega \times d)}_{v'} + \omega \times p'.
$$
{{< /math >}}

So changing the origin leaves $\omega$ alone and changes $v$ by $\omega \times d$, which is always perpendicular to $\omega$. Two consequences:

1. **We can make $v'$ parallel to $\omega$**, by choosing $d$ with $\omega \times d = -v_\perp$. The solutions are
{{< math >}}
$$
d = q + t\,\omega, \qquad q = \frac{\omega \times v}{|\omega|^2}, \qquad t \in \mathbb{R}.
$$
{{< /math >}}
They form a **line**, parallel to $\omega$. This is the **screw axis**.

2. **We can never change $\omega \cdot v$.** It is the same in every frame. Normalized by $|\omega|^2$, it is the **pitch**
{{< math >}}
$$
h = \frac{\omega\cdot v}{|\omega|^2},
$$
{{< /math >}}
the distance slid along the axis per radian of turning.

With the origin placed on the axis, the field reads $X(p) = \omega \times p + h\,\omega$: a spin about the axis plus a constant slide along it. Those two motions commute (the slide is along the rotation axis), so following the field for time $\theta$ just does both. Every steady motion is a screw:

{{< math >}}
$$
e^{\theta\hat\xi}\,p = e^{\theta\hat\omega}(p - q) + q + h\theta\,\omega \qquad (|\omega| = 1).
$$
{{< /math >}}

Translate the axis to the origin, rotate, translate back, slide.

This is the asymmetry from Section 1 paying off. Rotations need a center. A twist *chooses* its center, up to sliding along a line, and the part of the motion that no center can absorb is the pitch.

### What every observer agrees on

We just found an invariant by asking what a change of origin cannot affect. Let's do this systematically. Moving a twist by a rigid motion $(R, d)$, carrying its whole velocity field along, acts on it as

{{< math >}}
$$
(v, \omega) \mapsto (Rv + d \times R\omega,\; R\omega).
$$
{{< /math >}}

(This is the **adjoint action**, $\hat\xi \mapsto g\,\hat\xi\, g^{-1}$. Re-describing a fixed twist in a new frame is the inverse operation, which is why moving the origin to $d$ in Section 5 gave $v + \omega \times d$ rather than $v + d \times \omega$.) The angular velocity just rotates. $v$ picks up $d \times R\omega$, so $v$ behaves like the **moment** of a force: it depends on the point you measure it about.

There are exactly two independent quantities every observer agrees on:

{{< math >}}
$$
\omega \cdot \omega \qquad \text{and} \qquad \omega \cdot v.
$$
{{< /math >}}

You can confirm the count. A twist has 6 numbers. The frame changes that fix a given twist are rotations about its axis and slides along it, which is 2 dimensions. So a twist can be moved within a $6 - 2 = 4$ dimensional family, and $6 - 4 = 2$ numbers are left over that no frame change can alter.

## 6. A twist is a line

### Which four-dimensional family?

Fix $|\omega|$ and the pitch. The twists that remain form a 4-dimensional family, and rigid motions move freely within it. Can you think of a natural 4-dimensional space of geometric objects that rigid motions shuffle around?

**Oriented lines in space.** Two numbers pick a direction, and two more pick where the line crosses the plane perpendicular to it. So a twist is, in essence, a line, together with a rate and a pitch. That line is the screw axis.

### Reinventing Plücker coordinates

How would you describe a line by numbers? A first idea is a point on it plus a direction, $(q, \omega)$. But $q$ isn't unique; any point on the line works. We want numbers that depend only on the line.

Here's a fix. Use the direction $\omega$ and the **moment** $m = q \times \omega$. Sliding $q$ along the line changes $q$ by a multiple of $\omega$, which doesn't change $q\times\omega$. So $(\omega, m)$ depends only on the line. These are **Plücker coordinates**. They always satisfy $\omega \cdot m = 0$, and conversely any pair with $\omega \ne 0$ and $\omega\cdot m = 0$ describes exactly one line.

Now look again at the twist, with $|\omega| = 1$ and $q$ on its axis:

{{< math >}}
$$
v = q \times \omega + h\,\omega = m + h\,\omega.
$$
{{< /math >}}

**The coordinates of a twist are the Plücker coordinates of its axis, plus pitch times the direction.** In particular, a twist is a pure rotation about a line exactly when its pitch is zero, that is when $\omega \cdot v = 0$, which is exactly the Plücker condition. Lines are precisely the twists with zero pitch.

Twists with $\omega = 0$ (pure translations) fit too. Their axis $q = \omega \times v / |\omega|^2$ runs off to infinity as $\omega \to 0$. A translation is a rotation about a line at infinity.

### Reinventing dual numbers

Write out the bracket of two twists by multiplying their $4\times 4$ matrices:

{{< math >}}
$$
[(v_1, \omega_1), (v_2, \omega_2)] = (\omega_1 \times v_2 + v_1 \times \omega_2,\;\; \omega_1 \times \omega_2).
$$
{{< /math >}}

The angular part is the cross product, as for rotations. The linear part looks like a *product rule*: differentiate $\omega_1 \times \omega_2$, letting each factor vary in turn. Product rules come from a formal symbol $\varepsilon$ with $\varepsilon^2 = 0$, because

{{< math >}}
$$
(a + \varepsilon a')(b + \varepsilon b') = ab + \varepsilon(a'b + ab').
$$
{{< /math >}}

So try packing a twist into one "dual vector", $\Omega = \omega + \varepsilon v$. Then

{{< math >}}
$$
\Omega_1 \times \Omega_2 = \omega_1 \times \omega_2 + \varepsilon\,(\omega_1 \times v_2 + v_1 \times \omega_2),
$$
{{< /math >}}

which is exactly the twist bracket. Twists *are* angular velocities with coefficients in the **dual numbers** $\mathbb{D} = \mathbb{R}[\varepsilon]/(\varepsilon^2)$. Rigid motions are rotations over $\mathbb{D}$: the real part rotates and the infinitesimal part translates.

This gives a powerful shortcut, the **transference principle** of Study and Kotelnikov. Statements about rotations become statements about rigid motions if you replace real numbers with dual numbers. For example:

- For rotations, the only invariant of $\omega$ is $\omega\cdot\omega$. Transferred, the only invariant of $\Omega$ is the dual number $\Omega \cdot \Omega = |\omega|^2 + 2\varepsilon\,(\omega\cdot v)$. Both invariants we found in Section 5, packaged as one.
- A rotation is a turn by an angle $\theta$ about a unit vector. Transferred: a rigid motion is a turn by a **dual angle** $\theta + \varepsilon c$ about a **dual unit vector**, which (by the Plücker discussion) is a line. The real part of the dual angle is how far you turn, and the dual part is how far you slide. That is a screw.

## 7. Chasles' theorem

We are ready to answer the original question.

> **Theorem (Chasles).** Every rigid motion $g(p) = Rp + d$ is a screw motion: a rotation about some line, combined with a translation along that same line. Equivalently, every $g \in SE(3)$ equals $e^{\hat\xi}$ for some twist $\xi$.

### Why this is not automatic

It's tempting to think "every group element is the exponential of something" is a general fact. For rotations it was true, but we used an argument specific to three dimensions. And it can genuinely fail. In the group $SL(2, \mathbb{R})$ of $2\times2$ matrices with determinant 1, the matrix $\operatorname{diag}(-2, -\tfrac12)$ is not $e^X$ for any real $X$: the exponential of a real traceless $2\times 2$ matrix has eigenvalues that are either both positive or a complex-conjugate pair of modulus 1. So Chasles' theorem says something specific about Euclidean space.

### Proof

Do what we did in Section 5, but for a finite motion instead of a velocity field: look for the center, and accept a line when a point isn't available.

If $R = I$, then $g$ is a translation, a screw with its axis at infinity.

Otherwise, Section 3 gives $R$ an axis: $R = e^{\theta\hat\omega}$ with $|\omega| = 1$ and $\theta \in (0, \pi]$. Split the translation into its components along and across that axis:

{{< math >}}
$$
d = d_\parallel + d_\perp.
$$
{{< /math >}}

First we try to find a point $q$, perpendicular to the axis, that the motion would fix if we ignored $d_\parallel$:

{{< math >}}
$$
Rq + d_\perp = q \quad\Longleftrightarrow\quad (I - R)\,q = d_\perp.
$$
{{< /math >}}

On the plane perpendicular to the axis, $R$ is a rotation by a nonzero angle, which fixes no nonzero vector. So $I - R$ is invertible on that plane, and $q$ exists. Substituting $d_\perp = q - Rq$:

{{< math >}}
$$
g(p) = R(p - q) + q + d_\parallel.
$$
{{< /math >}}

That is a rotation by $\theta$ about the line through $q$ in direction $\omega$, followed by a slide of $d_\parallel$ along that line. $\blacksquare$

### What the proof was doing

Each step is one of the things we reinvented:

- **$R$ has an axis** because the dimension is odd (Section 3).
- **The planar step** is the 2D version of the theorem: a motion of the plane that genuinely rotates has a fixed point, so it is a rotation about that point.
- **$d_\parallel$ cannot be absorbed** by any choice of center. It is the finite version of the invariant $\omega\cdot v$, and the dual part of the dual angle.

Viewed from far enough away, this is a decomposition of a group element into two **commuting** pieces of different natures: a rotation (which repeats periodically) and a translation along its axis (which never repeats). Every rigid motion splits that way, uniquely when it actually rotates.

In four dimensions the argument changes character. A generic rotation of $\mathbb{R}^4$ fixes no direction, so $I - R$ is invertible on *all* of $\mathbb{R}^4$, and a generic rigid motion has a fixed point: it is a pure "double rotation", with no slide at all. The screw is a three-dimensional phenomenon, inherited from the fact that rotations in three dimensions have axes.

## 8. The same story for forces

Forces and torques pair with velocities to give power. A **wrench** $(f, \tau)$, a force together with a torque about the origin, pairs with a twist $(v, \omega)$ as

{{< math >}}
$$
\text{power} = f \cdot v + \tau \cdot \omega.
$$
{{< /math >}}

Moving the reference point to $d$ changes the torque but not the force: $\tau \mapsto \tau + f \times d$. Compare $v \mapsto v + \omega \times d$ from Section 5. It is the same rule, with the roles swapped: $f$ plays the role of $\omega$, and $\tau$ plays the role of $v$. So everything above applies to forces.

In particular, the analogue of Chasles' theorem is **Poinsot's theorem**: every system of forces on a rigid body is equivalent to one force along some line, plus a torque about that same line. Two screws are called **reciprocal** when a wrench along one does no work on a twist about the other. That relation is the backbone of Ball's *Theory of Screws* (1900), and it is still how engineers decide which forces a joint or a grasp can resist.

## 9. Explore

The explorer below follows a constant twist $\xi = (v, \omega)$. It draws the velocity field $X_\xi$ on a grid, the screw axis, and the helices traced by points of a body. In the screw tab, you choose the twist the way Section 6 suggests: as a line, a pitch, and a rate.

<div class="post-demo not-prose">
  <iframe src="/demos/twist-explorer.html" title="Interactive twist explorer" loading="lazy"></iframe>
  <p><a href="/demos/twist-explorer.html" target="_blank" rel="noopener">Open the explorer full screen ↗</a></p>
</div>

Some experiments, each tied to an idea above:

- **$v$ is a moment.** Load "Rotation, offset axis". The motion is a pure rotation, yet $v \ne 0$. It is the moment $q \times \omega$ of the axis (Section 6).
- **Only $\omega\cdot v$ matters.** With $\omega = (0, 0, 1)$, change $v_z$: the pitch changes. Change $v_x$ or $v_y$: only the axis moves, and the kind of motion stays the same (Section 5).
- **Axes at infinity.** Shrink $|\omega|$ toward zero with $v$ fixed. The axis runs away, and the helices straighten into parallel lines (Section 6).

## 10. Looking back

Here is the path we took, compressed:

1. *Rigid* means distances are preserved. That forced motions to be $p \mapsto Rp + d$.
2. *Steady* means the same infinitesimal step repeated. That forced the exponential, as a compound-interest limit.
3. *Combining* two steady motions fails to commute, and the failure of a small loop to close is the bracket.
4. *Velocities* of rigid motions are the fields $v + \omega \times p$. We found them twice: by differentiating the group, and from distance preservation alone.
5. *Looking for a fixed point* fails. What can be fixed is a line, and what can't is the pitch.
6. *Describing that line* invariantly gives Plücker coordinates, and *noticing a product rule* gives dual numbers.
7. *Chasles' theorem* is the finite version of step 5.

None of these steps needed a definition handed down in advance. At each stage there was a question, an obvious first attempt, and a specific way that attempt broke. The tool was whatever fixed it.

## References

- R. M. Murray, Z. Li, and S. S. Sastry, *A Mathematical Introduction to Robotic Manipulation*, CRC Press, 1994. Chapter 2. The explorer follows their ordering $\xi = (v, \omega)$.
- K. M. Lynch and F. C. Park, *Modern Robotics*, Cambridge University Press, 2017. Chapter 3. They order twists as $(\omega, v)$.
- J. M. Selig, *Geometric Fundamentals of Robotics*, 2nd ed., Springer, 2005. Adjoint orbits, the Klein quadric, and dual numbers.
- B. C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer, 2015. One-parameter subgroups, the BCH formula, and surjectivity of the exponential.
- R. S. Ball, *A Treatise on the Theory of Screws*, Cambridge University Press, 1900.
