---
id: "A09-GEO-01"
title: "Manifolds and local coordinates"
part: 4
stage: "A09-GEO"
status: "complete"
prerequisites: ["M01-10", "M02-02", "M03-01"]
estimated_time: "90–120 minutes"
---

# A09-GEO-01. Manifolds and local coordinates

## Why this lesson matters

The language of manifolds can express the hypothesis that high-dimensional activations actually lie near a structure with only a few degrees of freedom. A manifold is not simply a curved picture: it is a space whose neighborhood around each point can be described in Euclidean coordinates. We need to distinguish the global embedding dimension from the local intrinsic dimension.

## Learning objectives

- Explain the local Euclidean condition for a manifold.
- Distinguish a chart from a coordinate map.
- Explain why a single global chart is insufficient for a sphere.
- List the assumptions needed when calling an activation cloud a manifold.

## Prerequisite check

- Prerequisite lessons: [M01-10 Multivariable functions and partial derivatives](../../part-1-foundations/M01/M01-10-multivariable-partial-derivatives.md), [M02-02 Linear combinations and span](../../part-1-foundations/M02/M02-02-linear-combinations-span.md), [M03-01 Abstract vector spaces](../../part-1-foundations/M03/M03-01-abstract-vector-spaces.md)
- Check question: How does a subset of $\mathbb R^D$ differ from a $d$-dimensional coordinate space?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\mathcal M$ | `M calligraphic` | Manifold | topological or smooth space |
| $(U,\varphi)$ | `U comma phi` | Chart and coordinate map | $\varphi:U\to\mathbb R^d$ |
| $d$ | `d` | Intrinsic dimension | nonnegative integer |
| $D$ | `capital D` | Ambient dimension | $D\ge d$ |

## Core concepts

### What it means to describe a space in local coordinates

The local Euclidean condition for a $d$-dimensional manifold means that, for each point $p$, there is an open region $U$ containing that point and a one-to-one correspondence between that region and an open set in $\mathbb R^d$. Both the correspondence and its inverse must be continuous. Such a correspondence, which assigns coordinates and maps them back without disrupting the connections among nearby points, is called a homeomorphism. Here, the requirement that $U$ be open is a condition within the manifold. An open arc of a circle is open within the circle, but it is not a region containing a small disk in $\mathbb R^2$.

This condition says that nearby points can be described by $d$ numbers. It does not say that lengths and angles in that region are the same as in Euclidean space. The metric used to compare lengths is defined separately in GEO-03.

In the following figure, match each point on the open semicircle to its coordinate value in the open interval.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An open upper semicircle maps bijectively to an open interval using its x coordinate, with point zero point six comma zero point eight mapped to zero point six](../../figures/assets/A09-GEO/A09-GEO-01-open-arc-coordinate.svg)

<figcaption>The blue open arc is an open region within the circle. The hollow circles at the two ends mark excluded points, and p=(0.6,0.8) corresponds to coordinate u=0.6. This correspondence alone does not establish preservation of lengths or angles.</figcaption>
</figure>

### Charts and coordinate values

A chart is the pair $(U,\varphi)$ consisting of a region and its mapping; the coordinate map is the function $\varphi$ in that pair. The value $\varphi(p)$ consists of the $d$ coordinates obtained by applying this function to a point. Different charts can therefore give different coordinate values for the same point.

When two charts $(U,\varphi)$ and $(V,\psi)$ overlap, we use the transition map $\psi\circ\varphi^{-1}$ to change the coordinates of the same point. First, $\varphi^{-1}$ reconstructs the point on the manifold from its first coordinates. Applying $\psi$ to that point then gives its second coordinates. The domain of this calculation is $\varphi(U\cap V)$, the coordinates of the overlap, and the resulting coordinates lie in $\psi(U\cap V)$.

For a smooth manifold, we choose charts that cover the entire space and require transition maps on overlaps, as well as their reverse maps, to be smooth. Here, smooth means that partial derivatives of all orders exist and are continuous in coordinate space. Even when the numerical representations in individual charts differ, this compatibility condition lets us carry differentiation across charts. It adds a smooth structure to the local Euclidean condition alone.

The following figure shows the sequence of reconstructing a point on the circle from coordinate 0.6 and then reading its other coordinate, 0.8.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A transition map restores the first quadrant circle point from x coordinate zero point six and then reads its y coordinate zero point eight](../../figures/assets/A09-GEO/A09-GEO-01-overlap-transition.svg)

<figcaption>In the first-quadrant overlap of the upper arc U and the right arc V, the two coordinate values represent the same point p. The transition is the composition that reconstructs a point from u and reads v; on this overlap, v=√(1−u²).</figcaption>
</figure>

The circle $S^1\subset\mathbb R^2$ has ambient dimension 2 but intrinsic dimension 1. A single angle can describe most of it, but the coordinates break at one point, so multiple charts are needed.

A point on the circle has two ambient coordinates, but those coordinates cannot change independently as the point moves along the circle. They must satisfy $x^2+y^2=1$. Within one open arc, a single angle determines the point, so the intrinsic dimension is 1. However, if we cut the angles of the entire circle into a single range, numbers near the two ends of that range represent points that are close together on the circle. This is why one chart cannot distinguish all of the points continuously.

Compare the two points near the cut on the circle with the two ends of the angle interval.

<figure class="lesson-figure" markdown="1">

![Two nearby points on the circle lie on opposite sides of an angle coordinate cut and therefore have values near zero and two pi](../../figures/assets/A09-GEO/A09-GEO-01-angle-cut.svg)

<figcaption>Points p and q are close on the circle, but they lie near opposite ends of the angle representation between 0 and 2π. One continuous coordinate region cannot cover the entire circle, including the cut point (1,0).</figcaption>
</figure>

Activation samples $x_1,\ldots,x_n\in\mathbb R^D$ form a finite point cloud. These samples alone do not prove the existence of a smooth manifold. The hypothesis concerns a structure in which the distribution that produced the samples lies near some low-dimensional smooth space, rather than the samples themselves. The same samples can appear to have different local dimensions depending on the chosen neighborhood and the treatment of noise. Specify the noise scale, sampling density, neighborhood, and dimension estimator.

Even for the same samples, changing the neighborhood radius changes which points enter the analysis.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The same noisy circle samples are selected by two different neighborhood radii, while a dashed circle marks a proposed latent structure rather than a proven manifold](../../figures/assets/A09-GEO/A09-GEO-01-cloud-neighborhoods.svg)

<figcaption>In this educational noisy cloud, only the radius of the orange circle changes, from 0.18 to 0.65. The range of blue samples selected changes. The dashed circle is an assumed latent structure, not a manifold proved by the samples. This figure does not present a dimension estimate.</figcaption>
</figure>

## Small example

On the upper semicircle, we can use $x\in(-1,1)$ as a coordinate and reconstruct the point with $y=\sqrt{1-x^2}$. The coordinate map extracts $x$ from $(x,y)$, and the inverse maps $x$ to $(x,\sqrt{1-x^2})$. As we approach either endpoint, the magnitude of $dy/dx=-x/\sqrt{1-x^2}$ diverges, so this chart does not extend smoothly to those points. Near the right endpoint of the circle, we can instead use $y$ as a coordinate and reconstruct $x=\sqrt{1-y^2}$. The failure of one coordinate description does not mean that the circle itself is not smooth.

Represent the same point in two charts and compare the derivatives of their inverse maps near the right endpoint.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The same circle point near its right endpoint has a steep inverse x chart derivative but a small inverse y chart derivative](../../figures/assets/A09-GEO/A09-GEO-01-switch-chart.svg)

<figcaption>At p≈(0.98,0.199), reconstruction from x gives dy/dx≈−4.92, while reconstruction from y gives dx/dy≈−0.203. At the right endpoint (1,0), the first coordinate description fails, but the second remains usable.</figcaption>
</figure>

A single global chart cannot cover the entire sphere $S^2$ either. The reason is not limited to the problems of latitude and longitude at the poles. Compactness, the property possessed by closed and bounded sets in Euclidean space, is preserved under continuous images. The sphere is compact, so the image of a continuous coordinate map must also be compact. But a nonempty open set in $\mathbb R^2$ cannot be compact. We therefore cannot use the entire sphere as the domain of a chart while satisfying the requirement that its image be an open coordinate region. Covering it with several local charts does not conflict with this requirement.

Read the local patch on the sphere separately from the three coordinate axes containing the sphere.

<figure class="lesson-figure" markdown="1">

![A sphere sits in three ambient axes while a highlighted local patch can be located using two local parameters away from the poles](../../figures/assets/A09-GEO/A09-GEO-01-sphere-local-dimension.svg)

<figcaption>The sphere is represented by three ambient coordinates, but points within the blue patch are determined by two degrees of freedom. This does not mean that the latitude and longitude coordinates of this patch, away from the poles, extend to a global chart for the entire sphere.</figcaption>
</figure>

## Common misconceptions

- Curved coordinate lines are not the same as intrinsic curvature of the manifold itself.
- A low rank found by PCA does not by itself establish a nonlinear manifold.

For the crossing-point counterexample, compare the number of connected branches remaining after the center point is removed.

<figure class="lesson-figure" markdown="1">

![Removing the center of an interval leaves two branches whereas removing the crossing of two lines leaves four, revealing a failure of the one dimensional manifold condition](../../figures/assets/A09-GEO/A09-GEO-01-crossing-neighborhood.svg)

<figcaption>Removing the middle point of an open interval leaves two branches. Removing the crossing point of an X leaves four, so a neighborhood of that crossing cannot be assigned coordinates in the same way as one open interval.</figcaption>
</figure>

## Exercises

### 1. Dimensions
State the intrinsic and ambient dimensions of $S^2\subset\mathbb R^3$.
<details><summary>Show solution</summary>

The intrinsic dimension is 2, and the ambient dimension is 3.
</details>

### 2. Coordinates
Why is it not a contradiction for two charts to represent the same point with different numbers?
<details><summary>Show solution</summary>

Coordinates depend on the chart, and a transition map connects the two representations.
</details>

### 3. Counterexample
Explain why an X formed by two intersecting lines is not a one-dimensional manifold near the crossing.
<details><summary>Show solution</summary>

Removing the crossing leaves four branches, so the neighborhood is not topologically equivalent to a neighborhood in an open interval.
</details>

### 4. Model interpretation
State two items to record, beyond the point cloud itself, to support a claim about an activation manifold.
<details><summary>Show solution</summary>

Record the neighborhood scale, the intrinsic-dimension estimator, the sampling dataset, the noise model, and related choices.
</details>

## Sources and update boundaries

The definitions and chart conventions follow the usual definitions in John M. Lee's [*Introduction to Smooth Manifolds*, Chapter 1](https://sites.math.washington.edu/~lee/Books/ISM/c01.pdf). This lesson does not fully develop the separation and countability conditions for a topological manifold.

## Lesson summary

- A manifold has local coordinates in $\mathbb R^d$.
- Coordinates are a chart-dependent representation, not the point itself.
- Intrinsic dimension and ambient dimension differ.
- A finite activation cloud is only an observed sample for a manifold hypothesis.

## Pass criteria

- Can you distinguish charts, transition maps, and the two dimensions?
- Can you explain the crossing-point counterexample that is not a manifold?

## Next lesson

- [A09-GEO-02 Tangent spaces and cotangent spaces](A09-GEO-02-tangent-cotangent.md)

## Author checklist

- [x] Local coordinates and ambient space are distinguished.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
