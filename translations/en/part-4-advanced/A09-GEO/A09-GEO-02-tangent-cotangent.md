---
id: "A09-GEO-02"
title: "Tangent space and cotangent space"
part: 4
stage: "A09-GEO"
status: "complete"
prerequisites: ["A09-GEO-01", "M03-10"]
estimated_time: "90–120 minutes"
---

# A09-GEO-02. Tangent space and cotangent space

## Why this lesson matters

Points on a manifold generally cannot be added to one another, but the possible instantaneous velocities at one point form a vector space. A differential is a cotangent vector that maps these tangent vectors to scalar rates of change. A gradient can be obtained from the differential only after a metric has been chosen.

## Learning objectives

- Define a tangent vector through the velocity of a curve.
- Calculate the pairing of a tangent vector and a cotangent vector.
- Distinguish a differential from a gradient.
- Use a decoder Jacobian to map a latent tangent vector to an ambient direction.

## Prerequisite check

- Prerequisite lessons: [A09-GEO-01 Manifolds and local coordinates](A09-GEO-01-manifold-local-coordinate.md), [M03-10 Total derivative and differential](../../part-1-foundations/M03/M03-10-total-derivative-differential.md)
- Check question: What kind of value does a linear functional assign to a vector?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and conditions |
|---|---|---|---|
| $T_p\mathcal M$ | `the tangent space of M at p` | Possible velocities at $p$ | $d$-dimensional vector space |
| $T_p^*\mathcal M$ | `the cotangent space of M at p` | Linear functionals on tangent vectors | Dual space |
| $df_p$ | `d f at p` | Differential of $f$ | $T_p\mathcal M\to\mathbb R$ |
| $\langle df_p,v\rangle$ | `the pairing of d f at p and v` | Rate of change in direction $v$ | Scalar |

## Core concept 1. A tangent vector is a possible instantaneous velocity, not a point

Consider a curve on a manifold $\mathcal M$,

$$
\gamma:(-\epsilon,\epsilon)\to\mathcal M,
\qquad
\gamma(0)=p
$$

Its velocity $\dot\gamma(0)$ at $t=0$ represents one possible motion through $p$ while remaining on the manifold. Curves passing through the same point $p$ represent the same tangent vector if they give the same directional derivative for every smooth function. The set of all velocities obtained this way is $T_p\mathcal M$.

A tangent vector is not a displacement from $p$ to another point $q$. The tangent spaces $T_p\mathcal M$ and $T_q\mathcal M$ at different points are separate vector spaces. Comparing two such tangent vectors directly requires an additional comparison rule, such as a chart, connection, or ambient embedding.

Compare a possible tangential velocity at a point on a circle with the radial direction pointing away from the circle.

<figure class="lesson-figure" markdown="1">

![At the circle point one comma zero the vertical tangent velocity belongs to the tangent space while the horizontal radial direction does not](../../figures/assets/A09-GEO/A09-GEO-02-circle-velocity.svg)

<figcaption>At p=(1,0), possible velocities lie on the vertical tangent line. The blue arrow (0,1) and its scalar multiples are tangent vectors, whereas the orange radial direction (1,0) is not an instantaneous velocity of a curve on the circle.</figcaption>
</figure>

The instantaneous velocity of a curve and a finite chord between two points are different objects.

<figure class="lesson-figure" markdown="1">

![The circle velocity at time zero is vertical but the chord to the point at time zero point seven has a nonzero inward horizontal component](../../figures/assets/A09-GEO/A09-GEO-02-velocity-not-chord.svg)

<figcaption>The blue instantaneous velocity is (0,1), whereas the green chord is γ(0.7)−γ(0)≈(−0.235,0.644). The endpoint of a tangent arrow need not be another point on the circle.</figcaption>
</figure>

The next two tangent lines are drawn in the same ambient plane but belong to different base points.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The tangent space at the rightmost circle point is vertical while the tangent space at the top point is horizontal, displayed using a chosen ambient embedding](../../figures/assets/A09-GEO/A09-GEO-02-point-specific-tangents.svg)

<figcaption>The tangent lines at p=(1,0) and q=(0,1) have different directions. A chosen embedding lets us display them in one ambient space; this does not automatically identify tangent spaces at different points of an abstract manifold.</figcaption>
</figure>

## Core concept 2. Coordinates provide the components of a tangent vector

For local coordinates $x^1,\ldots,x^d$, the tangent basis can be written as

$$
\frac{\partial}{\partial x^1}\bigg|_p,
\ldots,
\frac{\partial}{\partial x^d}\bigg|_p
$$

A tangent vector $v$ can be expressed through its coordinate components $v^i$ as

$$
v
=
\sum_{i=1}^d v^i
\frac{\partial}{\partial x^i}\bigg|_p
$$

When the chart changes, the components and basis change together, but the geometric tangent vector still represents the same object.

The superscript $i$ here labels a coordinate component; it is not a power. If a curve represents $v$, then $v^i$ is the velocity obtained by differentiating the coordinate value $x^i(\gamma(t))$ at $t=0$. The basis vector $\partial/\partial x^i|_p$ corresponds to motion that changes only coordinate $i$ at unit speed while keeping the other coordinates fixed. Acting on a function, it first expresses that function in the chart's coordinates and then takes the partial derivative with respect to coordinate $i$. The sum above therefore combines the velocities along the coordinate axes to represent the same instantaneous motion.

With a different coordinate system, express the new coordinate values as functions of the old ones and apply the chain rule to transform the velocity components. The basis changes accordingly, so comparing only the component numbers can make the same vector appear to have changed.

Changing the coordinates and basis together reconstructs the same vector even when the component numbers differ.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The same tangent vector has components one comma one in x y coordinates and two comma one in coordinates u equals two x and v equals y, with the new u basis halved](../../figures/assets/A09-GEO/A09-GEO-02-coordinate-components.svg)

<figcaption>On this illustrative plane, changing coordinates to u=2x, v=y changes the components from (1,1) to (2,1). However, eᵤ=(1/2,0), so 2eᵤ+eᵥ is still the same vector (1,1). Both panels use the same ambient display axes for comparison.</figcaption>
</figure>

On an embedded surface, a tangent vector can be drawn as an ambient vector. This picture relies on the chosen embedding. An ambient space is not required to define a tangent vector on an abstract manifold.

## Core concept 3. A cotangent vector reads a velocity as a rate of change

The cotangent space $T_p^*\mathcal M$ is the dual of the tangent space. A covector $\omega_p$ is a linear functional

$$
\omega_p:T_p\mathcal M\to\mathbb R
$$

The differential of a smooth function $f:\mathcal M\to\mathbb R$ is a representative covector, defined by

$$
df_p(v)
=
\left.\frac{d}{dt}f(\gamma(t))\right|_{t=0}
$$

Here, $\dot\gamma(0)=v$. The input is a tangent vector, and the output is the scalar rate at which $f$ changes when moving with that velocity.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A tangent vector and a metric dependent gradient both lie in a two dimensional tangent coordinate plane, while a separate covector functional maps the vector to a scalar rate](../../figures/assets/A09-GEO/A09-GEO-02-tangent-cotangent.svg)

<figcaption>The blue v and the red gradient are both vectors in the two-dimensional tangent space at p. The covector df_p in the separate box reads v as a scalar rate of change. Choosing a metric lets us express the same information as a gradient vector.</figcaption>
</figure>

In the figure, the tangent vector and covector are different types of objects, not different styles of arrows. The pairing $df_p(v)$ is defined without additional coordinates or a metric. By contrast, drawing a `direction indicated by a covector` requires a rule that converts a covector into a vector.

Compare the action of a covector on a velocity along a level set and on one crossing a level set.

<figure class="lesson-figure" markdown="1">

![For the scalar function two x minus y a velocity one comma two follows a level set and has zero covector pairing, while velocity one comma one has pairing one](../../figures/assets/A09-GEO/A09-GEO-02-covector-levels.svg)

<figcaption>For the illustrative function f(x,y)=2x−y, v=(1,1) gives df(v)=1, whereas w=(1,2) follows a level set and gives df(w)=0. A covector is this scalar-reading rule, not a directional arrow.</figcaption>
</figure>

## Core concept 4. The gradient depends on the metric

Choosing a metric $g_p$ at point $p$ determines, for every covector $df_p$, a unique gradient vector $\operatorname{grad}f$ satisfying

$$
df_p(v)
=
g_p\bigl(\operatorname{grad} f,v\bigr)
\qquad
\text{for every }v\in T_p\mathcal M
$$

In Euclidean coordinates, the metric matrix is the identity, so the components of the differential and gradient appear identical. For a general metric matrix $\mathbf G$, column-coordinate notation requires the transformation

$$
\operatorname{grad}f
=
\mathbf G^{-1}(df)
$$

The differential is therefore determined by the function and point, whereas the gradient's length and direction depend on the choice of metric.

Here, $(df)$ is a column array of coefficients in the chosen dual basis; it does not mean that the covector itself is a tangent vector. Let this array be $a$ and the gradient's coordinate array be $w$. Then $df_p(v)=a^\top v$ and $g_p(w,v)=w^\top\mathbf Gv$. Because the metric matrix is symmetric, the latter equals $(\mathbf Gw)^\top v$. Equality for every $v$ requires $\mathbf Gw=a$, giving $w=\mathbf G^{-1}a$. The metric's positive-definiteness ensures that the inverse exists and the solution is unique.

For example, in the same coordinates, replacing the identity metric with a positive multiple $c$ of it preserves the differential's coefficients but scales the gradient components by $1/c$. A general metric can also change the direction. The function's rate of change $df_p(v)$ remains unchanged when the metric changes.

The following figure compares two gradients while holding the differential's coefficients fixed and changing only the metric.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The differential coefficients two comma minus one yield gradient two comma minus one under identity metric and zero point five comma minus one under metric diagonal four comma one](../../figures/assets/A09-GEO/A09-GEO-02-metric-gradients.svg)

<figcaption>The coefficients a=(2,−1) are the same, but the gradient is (2,−1) for G=I and (0.5,−1) for G=diag(4,1). The gray boundaries represent unit length under each metric. In both cases, the test velocity v=(1,1) gives g(gradient,v)=df(v)=1.</figcaption>
</figure>

## Core concept 5. The Jacobian maps tangent vectors to the next space

The differential $dF_p$ of a smooth map $F:\mathcal M\to\mathcal N$ is a linear map

$$
dF_p:T_p\mathcal M\to T_{F(p)}\mathcal N
$$

Once coordinates are chosen, the matrix of this map is the Jacobian. For a decoder $F:\mathbb R^d\to\mathbb R^D$, the ambient tangent vector corresponding to a latent velocity $u$ is

$$
J_F(z)u\in\mathbb R^D
$$

Passing the latent curve $\gamma(t)=z+tu$ through the decoder gives output velocity $J_F(z)u$ at $t=0$ by the chain rule. The Jacobian thus transmits a coordinate velocity to a velocity in the next space. The column space of $J_F(z)$ is the set of first-order output directions obtained by mapping all possible latent velocities.

For a finite step, use the approximation $F(z+u)-F(z)\approx J_F(z)u$. Differentiability means that the remainder becomes small relative to $\|u\|$ as $u$ becomes small; it does not mean that exact equality holds for sufficiently small $u$. The difference equals the linear prediction exactly for an affine map, but a general nonlinear decoder leaves an approximation error.

The next figure shows one latent velocity passing through a decoder to become a two-component output velocity.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Decoder z maps to z comma z squared converts latent velocity zero point five at z zero point five into output tangent zero point five comma zero point five, different from its finite displacement](../../figures/assets/A09-GEO/A09-GEO-02-decoder-velocity.svg)

<figcaption>For the illustrative decoder F(z)=(z,z²), latent velocity u=0.5 at z=0.5 gives J_Fu=(0.5,0.5). Moving z a finite distance to 1 instead gives an output difference of (0.5,0.75). The difference between the orange chord and blue instantaneous velocity is the nonlinear remainder.</figcaption>
</figure>

## Small example

For the circle $\gamma(t)=(\cos t,\sin t)$,

$$
\dot\gamma(t)=(-\sin t,\cos t)
$$

so the tangent vector at $t=0$ is $(0,1)$. At $p=(1,0)$, the circle's tangent space is the one-dimensional vector space of all scalar multiples of $(0,1)$. The radial direction $(1,0)$ is not a velocity of a curve on the circle, so it does not belong to $T_pS^1$.

If $f(x,y)=y$, then $df_p(v_1,v_2)=v_2$. Pairing it with the tangent vector $v=(0,3)$ gives $df_p(v)=3$. This calculation is the action of a covector reading the second component of $v$; it can be performed without first determining a gradient vector.

## Common misconceptions

- A tangent vector need not be an arrow pointing to another point on the manifold.
- A differential and a gradient are different types of objects, even when their numerical components appear identical in Euclidean coordinates.

## Exercises

### 1. Tangent vector
Calculate the tangent vector of $\gamma(t)=(\cos t,\sin t)$ at $t=\pi/2$.
<details><summary>Show solution</summary>

Since $\dot\gamma(t)=(-\sin t,\cos t)$, the tangent vector is $(-1,0)$.
</details>

### 2. Pairing
In coordinates where $df=(2,-1)$ and $v=(3,4)$, calculate $df(v)$.
<details><summary>Show solution</summary>

$2\cdot3-1\cdot4=2$.
</details>

### 3. Object types
Explain why $df$ cannot be called a tangent vector without a metric.
<details><summary>Show solution</summary>

$df$ is a dual object that maps tangent vectors to scalars. Identifying it with a vector requires a metric.
</details>

### 4. Jacobian
For $J_F\in\mathbb R^{D\times d}$ and $u\in\mathbb R^d$, determine the shape of $J_Fu$.
<details><summary>Show solution</summary>

It is an ambient tangent vector in $\mathbb R^D$.
</details>

## Sources and update boundaries

Definitions through curve velocities and derivations are standard equivalent definitions on a smooth manifold. This lesson omits the formal construction of vector bundles.

## Lesson summary

- A tangent space is the vector space of possible curve velocities at one point.
- A cotangent vector is a linear functional acting on tangent vectors.
- A differential and a metric determine the gradient.
- A Jacobian transmits tangent vectors between the spaces of a map.

## Pass criteria

- Can you calculate a tangent vector from a curve?
- Can you distinguish the object types of a differential, gradient, and Jacobian?

## Next lesson

- [A09-GEO-03 Metric and length](A09-GEO-03-metric-length.md)

## Author checklist

- [x] The types of tangent and cotangent vectors are distinguished.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
