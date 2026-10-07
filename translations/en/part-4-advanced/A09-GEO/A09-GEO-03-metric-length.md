---
id: "A09-GEO-03"
title: "Metrics and length"
part: 4
stage: "A09-GEO"
status: "complete"
prerequisites: ["A09-GEO-02", "M02-03"]
estimated_time: "90–120 minutes"
---

# A09-GEO-03. Metrics and length

## Why this lesson matters

Using the Euclidean norm of a coordinate difference as a representation distance can lead us to mistake a choice of coordinates for geometry. A Riemannian metric determines lengths and angles in each tangent space and provides the starting point for curve length and geodesic distance.

## Learning objectives

- Explain the positive-definite bilinear conditions for a Riemannian metric.
- Calculate a tangent norm using a coordinate metric matrix.
- Explain why curve length is invariant under reparameterization.
- State why the choice of metric changes the interpretation of activation distances.

## Prerequisite check

- Prerequisite lessons: [A09-GEO-02 Tangent spaces and cotangent spaces](A09-GEO-02-tangent-cotangent.md), [M02-03 Inner products, length, and angles](../../part-1-foundations/M02/M02-03-inner-product-length-angle.md)
- Check question: Why can a quadratic form defined by a positive-definite matrix not be negative?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $g_p(u,v)$ | `g at p of u comma v` | Tangent inner product at $p$ | scalar |
| $G(x)$ | `G of x` | Metric matrix in coordinates | $d\times d$ positive definite |
| $\|v\|_{g,p}$ | `the g norm of v at p` | Metric tangent norm | nonnegative scalar |
| $L_g(\gamma)$ | `the g length of gamma` | Metric length of a curve | nonnegative scalar |

## Core concepts

A Riemannian metric assigns a smoothly varying inner product $g_p$ to each point $p$.

An inner product is a function that is linear in each of its two tangent vectors, satisfies $g_p(u,v)=g_p(v,u)$, and gives $g_p(v,v)>0$ when $v\ne0$. Bilinear means that fixing either vector leaves a function that preserves sums and scalar multiples of the other vector. The positive-definite condition prevents a nonzero velocity from having zero length. Smooth variation means that, in a chosen chart, the metric coefficients vary smoothly with the coordinates of the point.

Compare the requirement of a positive value for every nonzero velocity in the following three quadratic forms.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A positive definite quadratic form has a closed unit ellipse while degenerate and indefinite forms give zero and negative values to a nonzero vertical velocity](../../figures/assets/A09-GEO/A09-GEO-03-positive-definite.svg)

<figcaption>G=diag(4,1) gives a positive squared norm to every nonzero velocity. For v=(0,1), however, diag(1,0) gives 0 and diag(1,−1) gives −1, so neither satisfies the positive-definite condition for a Riemannian metric. Each curve is the set Q(v)=1.</figcaption>
</figure>

Collecting the inner products of all pairs of coordinate basis vectors into the entries of $G(x)$ gives

$$
g_p(u,v)=u^\top G(x)v,
\qquad
\|v\|_{g,p}=\sqrt{v^\top G(x)v}.
$$

Here, $x$ is the coordinate representation of the current point $p$, while $u,v$ are velocity components at that point. Even if the arrays have the same dimension, point coordinates and tangent velocities play different roles. The matrix $G(x)$ is symmetric and positive definite. Its quadratic form calculates the inner product in the chosen basis through matrix multiplication. When changing charts, we must transform both the velocity components and the metric matrix to obtain the same length.

The rows and columns of the metric matrix identify pairs of coordinate basis vectors.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two chosen basis vectors two comma zero and one comma one produce the Gram metric matrix four two two two through pairwise Euclidean inner products](../../figures/assets/A09-GEO/A09-GEO-03-basis-gram-matrix.svg)

<figcaption>The pairwise inner products of the educational basis b₁=(2,0), b₂=(1,1) populate G on the right. Coordinates c=(1,1) represent the ambient vector (3,1), and cᵀGc=10 equals its squared length.</figcaption>
</figure>

Even with the same velocity components, the length changes if the metric at the base point differs.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The same velocity one comma zero has metric norm one at base coordinate zero and square root of two at base coordinate one under the smooth field diagonal one plus x squared comma one](../../figures/assets/A09-GEO/A09-GEO-03-position-dependent-units.svg)

<figcaption>For the educational smooth metric G(x)=diag(1+x²,1), the gray unit boundary depends on the point coordinate x. The same velocity v=(1,0) has length 1 at x=0 and √2 at x=1. The panel axes show tangent velocity components, not point positions.</figcaption>
</figure>

Suppose a curve is piecewise differentiable with continuous velocity on each piece. Multiplying the instantaneous metric speed by a small time interval approximates the length traveled during that interval. Integrating over the entire path gives the curve length

$$
L_g(\gamma)=\int_a^b
\sqrt{\dot\gamma(t)^\top G(\gamma(t))\dot\gamma(t)}\,dt
$$

In this expression, $\gamma(t)$ and $\dot\gamma(t)$ are the position and velocity represented in the relevant chart. If the curve leaves one chart, add the lengths calculated over the separate coordinate segments. Different paths through the same points can have different lengths. The metric distance between two points connected by paths is the infimum of the lengths of paths joining them. This is distinct from the tangent norm at a single point.

Distinguish the two paths joining the same endpoints from the distance between those points.

<figure class="lesson-figure" markdown="1">

![A Euclidean straight path between zero comma zero and two comma zero has length two while an upper semicircular path has length pi, and the endpoint distance is two](../../figures/assets/A09-GEO/A09-GEO-03-path-versus-distance.svg)

<figcaption>In the plane with G=I, the straight path has length 2 and the upper semicircular path has length π. The distance between the points is 2, the infimum of path lengths; it cannot be equated with the length of an arbitrary path.</figcaption>
</figure>

### Why changing the speed leaves the length unchanged

Change time through a smooth one-to-one correspondence $t=\tau(s)$ between the new and original time intervals, and write $\widetilde\gamma(s)=\gamma(\tau(s))$. By the chain rule, the new velocity is $\dot\gamma(\tau(s))\tau'(s)$. A norm lets us factor out the absolute value of a scalar multiplier, so

$$
\|\widetilde\gamma'(s)\|_g
=\|\dot\gamma(\tau(s))\|_g\,|\tau'(s)|.
$$

For an increasing reparameterization, changing the integration variable with $dt=\tau'(s)ds$ returns the original length integral. For a decreasing reparameterization, the absolute value and the reversed integration limits also give the same length. These cases traverse the same path the same number of times, changing only the speed or direction of travel. Motion that goes back and forth over the same segment several times cannot be treated as a single one-to-one reparameterization.

Compare the spacing of points along the same path with the areas under the speed curves.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Uniform and nonlinear monotone time parameterizations visit the same unit line segment with different sampled spacing and speed curves but equal integrated length one](../../figures/assets/A09-GEO/A09-GEO-03-reparameterized-length.svg)

<figcaption>The educational straight path γ(t)=(t,0) is reparameterized by t=(s+s²)/2. Points at equal time intervals are spaced differently, and the speed changes from 1 to 0.5+s, but both speed curves enclose area 1. This time transformation is an increasing one-to-one correspondence between intervals [0,1].</figcaption>
</figure>

### Changing coordinates versus changing the metric

The Euclidean metric in activation space, a covariance whitening metric, and a decoder-induced metric answer different questions. Choosing a metric after inspecting which one makes the results look better introduces selection bias.

The Euclidean metric measures differences in raw activation coordinates. A whitening metric adjusts directional differences according to the variation estimated from the chosen data. A decoder-induced metric measures how strongly a latent change appears in the output. When representing the same geometry in a different chart, transform the metric with the coordinates to preserve length. By contrast, assigning a different metric to the same coordinates changes the actual rule for measuring length, so different distances are not a contradiction.

Separate a coordinate change that preserves length from the assignment of a new metric to the same coordinates.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A coordinate change doubling the first component preserves length when the metric changes to diagonal one quarter comma one, while resetting that new coordinate metric to identity changes the length](../../figures/assets/A09-GEO/A09-GEO-03-coordinate-versus-metric.svg)

<figcaption>Representing (1,1) as (2,1) in coordinates u=2x, v=y and also changing G to diag(1/4,1) preserves length √2. Assigning G=I to those same new coordinates, as on the right, changes the measuring rule itself and gives √5.</figcaption>
</figure>

## Small example

For $G=\operatorname{diag}(4,1)$, the squared norm of $v=(1,2)$ is $4+4=8$, and its norm is $2\sqrt2$.

Expanding the matrix product gives $v^\top Gv=4v_1^2+v_2^2$. A unit velocity in the first coordinate is measured as length 2, and a unit velocity in the second as length 1. The diagonal entries are weights for the squared norm, not lengths, so we take a square root at the end.

Displaying the first component at twice its value lets us check this metric norm by a Euclidean length calculation.

<figure class="lesson-figure" markdown="1">

![Velocity one comma two under diagonal four comma one metric is displayed as weighted Euclidean vector two comma two, whose squared norm is eight and length is two square root of two](../../figures/assets/A09-GEO/A09-GEO-03-weighted-norm.svg)

<figcaption>The upper panel shows velocity (1,2) and the metric's unit boundary; the lower panel shows the weighted representation (2,2) used for calculation. The squared norm is 8 and the norm is 2√2. The weight 4 is not a length of 4.</figcaption>
</figure>

## Common misconceptions

- Here, a metric means a field of tangent inner products, not just a distance function between two points.
- Nonlinear coordinates alone do not create intrinsic curvature in a space.

## Exercises

### 1. Norm
Find the metric norm of $v=(1,0)$ for $G=\operatorname{diag}(9,1)$.
<details><summary>Show solution</summary>

It is $\sqrt9=3$.
</details>

### 2. Angle
Find the cosine when $G=I$, $u=(1,0)$, and $v=(1,1)$.
<details><summary>Show solution</summary>

It is $u^\top v/(\|u\|\|v\|)=1/\sqrt2$.
</details>

### 3. Position dependence
If $G(x)$ differs from point to point, can the length of the same coordinate velocity differ?
<details><summary>Show solution</summary>

Yes. The norm depends jointly on the velocity and the metric matrix at the current point.
</details>

### 4. Model interpretation
What should you fix first when comparing cosine distance and whitening distance?
<details><summary>Show solution</summary>

Fix the data, centering and normalization, the covariance estimation method, and the metric selection rule appropriate to the research question.
</details>

## Sources and update boundaries

The definitions of a metric and curve length follow standard Riemannian geometry. For the relationship between these definitions and path length, see Danny Calegari's [*Notes on Riemannian Geometry*, §3.1](https://math.uchicago.edu/~dannyc/courses/riem_geo_2013/riem_geo_notes.pdf). This lesson does not cover distance completeness or the Hopf–Rinow theorem.

## Lesson summary

- A metric supplies an inner product at each tangent space.
- Curve length is calculated from the metric matrix and velocity.
- The same coordinate difference can have different lengths under different metrics.
- In activation geometry, include the metric choice in the analysis contract.

## Pass criteria

- Can you calculate metric norms and curve lengths?
- Can you distinguish coordinates, metrics, and distances?

## Next lesson

- [A09-GEO-04 Pullback metrics and Jacobians](A09-GEO-04-pullback-metric.md)

## Author checklist

- [x] Metrics and coordinate distances are distinguished.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
