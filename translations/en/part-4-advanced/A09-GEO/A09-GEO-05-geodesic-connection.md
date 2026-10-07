---
id: "A09-GEO-05"
title: "Geodesics and connections"
part: 4
stage: "A09-GEO"
status: "complete"
prerequisites: ["A09-GEO-03", "A09-GEO-04"]
estimated_time: "90–120 minutes"
---

# A09-GEO-05. Geodesics and connections

## Why this lesson matters

Tangent vectors at different points belong to different vector spaces, so they cannot be subtracted directly. A connection provides a rule for comparing vectors along a manifold. A geodesic is a curve whose direction does not change under that rule.

## Learning objectives

- Explain why a connection is needed.
- Distinguish the roles of covariant differentiation and parallel transport.
- Read the terms in the geodesic equation.
- Distinguish a straight line in coordinates from a geodesic.

## Prerequisite check

- Prerequisite lessons: [A09-GEO-03 Metrics and length](A09-GEO-03-metric-length.md), [A09-GEO-04 Pullback metrics and Jacobians](A09-GEO-04-pullback-metric.md)
- Check question: What is missed by assuming that tangent vectors at different points belong to the same vector space?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $\nabla_XY$ | `the covariant derivative of Y along X` | Change in $Y$ along $X$ | Vector field |
| $\Gamma^k_{ij}$ | `Gamma k i j` | Coordinate connection coefficient | Scalar field |
| $\nabla_{\dot\gamma}\dot\gamma$ | `the covariant acceleration along gamma` | Intrinsic acceleration of the curve | Tangent vector |
| $\gamma$ | `gamma` | Curve on the manifold | $[a,b]\to M$ |

## Core concepts

### A rule for differentiating vectors at different points

A vector field $Y$ assigns a vector $Y(p)\in T_pM$ to each point $p$. To examine how $Y$ changes along a curve, we must account for the fact that vectors at different points belong to different tangent spaces. Differentiating only the coordinate components leaves out changes in the basis used to express them. A connection $\nabla$ handles these changes together, expressing the change in $Y$ along $X$ as a tangent vector at the current point.

In a coordinate basis, this is written as

$$
(\nabla_XY)^k
=\sum_{i=1}^d X^i\partial_iY^k
+\sum_{i=1}^d\sum_{j=1}^d\Gamma^k_{ij}X^iY^j
$$

Here $k$ indexes the output component being computed, and $i,j$ index the coordinate components being summed. $\partial_iY^k$ is the rate at which the $k$th component of $Y$ changes as the $i$th coordinate varies. The first term sums these component changes with the velocities in $X$. The second term accounts for basis changes through $\Gamma^k_{ij}$, the coefficient expressing, in the $k$th basis direction, the change in the $j$th basis vector along the $i$th direction.

A Riemannian metric has a unique metric-compatible, torsion-free connection, called the Levi–Civita connection. Metric compatibility means that differentiation of the inner product of two vectors follows the product rule using the covariant derivative of each vector. In a coordinate basis, the torsion-free condition is $\Gamma^k_{ij}=\Gamma^k_{ji}$. The discussion of length and geodesics in this lesson uses this Levi–Civita connection.

Compare the blue and purple basis directions at the two positions below.

<figure class="lesson-figure" markdown="1">

![Polar coordinate basis vectors at two points of a quarter-circle path rotate in the flat Euclidean plane](../../figures/assets/A09-GEO/A09-GEO-05-rotating-basis.svg)

<figcaption>The manifold here is the plane R², and the dashed circular arc is a path on it. At r=1, the directions of ∂r and ∂θ change with position. Even though Y=∂r has the same polar components (1,0), the visible vector direction in the plane differs.</figcaption>
</figure>

### Rates of change and parallel transport

A covariant derivative computes how much a specified vector changes along a curve. Parallel transport works in the opposite direction: given a starting vector, it continues the vector along the curve so that its covariant derivative is 0. Writing the vector along the curve as $V(t)$, the condition is $\nabla_{\dot\gamma}V=0$. This does not require the components to remain numerically constant. When the basis changes, the components must change as well for the rate of change under the same rule to remain 0.

Levi–Civita parallel transport preserves the metric length of a vector and the inner products of vectors transported together. But specifying two endpoints alone does not fully determine the comparison rule. In general, the path of transport also matters. GEO-06 connects this path dependence to curvature.

Read the same transport below as a Cartesian vector and as polar components.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Euclidean parallel transport preserves the Cartesian vector one zero while its polar components change along a quarter-circle path](../../figures/assets/A09-GEO/A09-GEO-05-transport-components.svg)

<figcaption>The green vector under the plane's Levi–Civita transport remains (1,0) in Cartesian form. In the rotating polar basis, however, its components change from (1,0) to (0,−1). Changing components does not contradict a covariant derivative of 0.</figcaption>
</figure>

### Comparing a curve's own velocity

A geodesic satisfies

$$
\nabla_{\dot\gamma}\dot\gamma=0,
\qquad
\ddot\gamma^k
+\sum_{i=1}^d\sum_{j=1}^d
\Gamma^k_{ij}\dot\gamma^i\dot\gamma^j=0
$$

This requires the curve to parallel-transport its own velocity along itself. $\ddot\gamma^k$ is the derivative of the coordinate velocity component, and the sum that follows accounts for changes in the basis expressing that velocity. $\Gamma^k_{ij}$ is evaluated at the current position $\gamma(t)$, and the equation applies to each $k=1,\ldots,d$. Even if coordinate acceleration is not 0, covariant acceleration is 0 when the two terms cancel.

A geodesic moving with velocity different from 0 is parameterized at constant metric speed and is stationary under length variations with fixed endpoints. Sufficiently short segments are shortest paths between their endpoints, but long segments need not be globally shortest. Length is preserved under the reparameterizations in GEO-03, whereas this equation requiring acceleration to be 0 also imposes a condition on the parameterization. Traversing the same path while speeding up and slowing down can fail to satisfy the equation, even if the path itself is a geodesic path.

Distinguish having the same path from having the same parameterization in the two scenes below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two parameterizations trace the same Euclidean line segment but only constant-speed affine time has zero acceleration](../../figures/assets/A09-GEO/A09-GEO-05-geodesic-parameter.svg)

<figcaption>Both x(t)=t and x(s)=(s+s²)/2 follow the line segment [0,1], with length 1. On the right, however, speed increases with time and Cartesian acceleration is 1. The velocity arrows are displayed at 1/4 of their actual vector scale.</figcaption>
</figure>

The two paths on the circle below connect the same endpoints but have different lengths.

<figure class="lesson-figure" markdown="1">

![Short and long constant-speed arcs on the unit circle are geodesic segments with the same endpoints but only the short arc is globally shortest](../../figures/assets/A09-GEO/A09-GEO-05-local-not-global-shortest.svg)

<figcaption>With the induced metric on the circle S¹, the two constant-speed arcs are geodesic segments. The short blue arc has length π/2; the long purple arc has length 3π/2. Even if each small segment of the long arc is locally shortest, the whole arc is not the shortest path between those endpoints.</figcaption>
</figure>

## Small example

In Cartesian coordinates on the Euclidean plane, $\Gamma^k_{ij}=0$, so the geodesic equation is $\ddot\gamma=0$. Its solutions are straight lines at constant velocity. In polar coordinates, the same straight line can have nonzero coordinate acceleration.

Writing $\gamma(t)=(t,1)$ in polar coordinates for $t>0$ gives $r(t)=\sqrt{t^2+1}$ and $\theta(t)=\arctan(1/t)$. Since $r''=1/r^3$, radial coordinate acceleration is not 0. But the radial geodesic equation in polar coordinates is $r''-r(\theta')^2=0$. Substituting $\theta'=-1/r^2$ gives $1/r^3-r/r^4=0$. This is the same motion along a Cartesian straight line expressed in different coordinates. Nonzero coordinate acceleration does not mean that the plane has become curved.

Read the path in the physical plane separately from the graph of its polar coordinate values below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The Cartesian straight path t one becomes a curved trace in radius-angle coordinates without introducing curvature in the Euclidean plane](../../figures/assets/A09-GEO/A09-GEO-05-straight-polar-trace.svg)

<figcaption>On the left, γ(t)=(t,1) is a straight line in the plane. The right panel plots the coordinate values (r,θ) of those same points and appears curved. The green velocity vectors have Cartesian value (1,0) and are displayed at 1/2 scale. Bending in the graph of coordinate values does not imply intrinsic curvature of the plane.</figcaption>
</figure>

Adding the two terms in the graph below shows the difference between coordinate acceleration and covariant acceleration.

<figure class="lesson-figure" markdown="1">

![Nonzero radial coordinate acceleration and the polar connection term cancel to zero covariant radial acceleration along the same Cartesian straight line](../../figures/assets/A09-GEO/A09-GEO-05-polar-acceleration-cancellation.svg)

<figcaption>Along the same straight line, the blue radial coordinate acceleration r″=1/r³ cancels the purple connection term −r(θ′)². At t=1 they are approximately 0.3536 and −0.3536, and their green sum is 0. Radial coordinate acceleration alone cannot determine whether a curve is a geodesic.</figcaption>
</figure>

## Common misconceptions

- Not every geodesic is a globally shortest path.
- Christoffel symbols are not tensors; changing coordinates can make them become 0 or appear.

## Exercises

### 1. Euclidean geodesic
Determine whether $\gamma(t)=p+tv$ is a geodesic in Cartesian Euclidean space.
<details><summary>Show solution</summary>

Since $\ddot\gamma=0$ and the connection coefficients are also 0, it satisfies the geodesic equation.
</details>

### 2. Comparison rule
What additional structure is needed to compare tangent vectors at two different points?
<details><summary>Show solution</summary>

A connection, or the parallel transport rule it determines, is needed.
</details>

### 3. Coordinate effect
Why can a straight line have coordinate acceleration different from 0 in polar coordinates?
<details><summary>Show solution</summary>

The coordinate basis varies with position, and the Christoffel term accounts for this change.
</details>

### 4. Representation path
State two conditions to check before calling an activation interpolation a geodesic.
<details><summary>Show solution</summary>

Specify the manifold and metric, and check whether the interpolation satisfies that metric's geodesic equation or length-minimization condition.
</details>

## Evidence and update boundaries

The definitions of connections, parallel transport, and geodesics follow standard Riemannian geometry. Their definitions and the Levi–Civita conditions can be found in Danny Calegari's [*Notes on Riemannian Geometry*, §§3.2–4.2](https://math.uchicago.edu/~dannyc/courses/riem_geo_2013/riem_geo_notes.pdf). Geodesic completeness and the global properties of the exponential map are not covered.

## Lesson summary

- A connection allows vectors in different tangent spaces to be compared.
- The Christoffel term accounts for changes in the coordinate basis.
- A geodesic is a curve with 0 covariant acceleration.
- A coordinate straight line must be distinguished from an intrinsic geodesic.

## Pass criteria

- Can you explain the two terms in the geodesic equation?
- Can you state the conditions needed to call an activation interpolation a geodesic?

## Next lesson

- [A09-GEO-06 Intrinsic and extrinsic curvature](A09-GEO-06-intrinsic-extrinsic-curvature.md)

## Author checklist

- [x] The roles of connections and geodesics are distinguished.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
