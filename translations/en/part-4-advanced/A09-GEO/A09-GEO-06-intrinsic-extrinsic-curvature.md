---
id: "A09-GEO-06"
title: "Intrinsic and extrinsic curvature"
part: 4
stage: "A09-GEO"
status: "complete"
prerequisites: ["A09-GEO-05"]
estimated_time: "90–120 minutes"
---

# A09-GEO-06. Intrinsic and extrinsic curvature

## Why this lesson matters

Observing that a representation looks bent in a high-dimensional space can blur two kinds of curvature. Intrinsic curvature is measured using only the manifold's internal metric. Extrinsic curvature measures how the manifold sits in an ambient space.

## Learning objectives

- Distinguish intrinsic curvature from extrinsic curvature.
- Explain the distinction using a plane and a cylinder.
- State what sectional curvature measures.
- Avoid treating visible bending of an embedding as a conclusion about intrinsic geometry.

## Prerequisite check

- Prerequisite lesson: [A09-GEO-05 Geodesics and connections](A09-GEO-05-geodesic-connection.md)
- Check question: Can the curvature of a metric be determined from coordinate lines looking bent alone?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $R(X,Y)Z$ | `R of X comma Y applied to Z` | Riemann curvature operator | Tangent vector |
| $K(\sigma)$ | `the sectional curvature of sigma` | Curvature of the tangent two-plane $\sigma$ | Scalar |
| $\mathrm{II}(u,v)$ | `the second fundamental form of u comma v` | Bending in the ambient normal direction | Normal vector |
| $K_G$ | `Gaussian curvature` | Intrinsic curvature of a surface | Scalar |

## Core concepts

Riemann curvature measures the extent to which the order of covariant differentiation generally fails to commute.

$$
R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z.
$$

The first two terms are the difference from reversing the order of covariant differentiation of $Z$ in two directions. But the direction fields $X,Y$ themselves can vary with position. $[X,Y]$ is the direction field defined on scalar functions $f$ by $[X,Y]f=X(Yf)-Y(Xf)$. Here $X(Yf)$ means differentiating along $X$ the scalar function obtained by differentiating along $Y$. The last term subtracts the difference due to this change in direction fields, leaving the connection's curvature within the difference in differentiation order. Coordinate basis directions commute, giving $[X,Y]=0$, but the first two covariant derivatives can still fail to commute in a curved space.

### The internal metric and ambient bending

Intrinsic curvature is computed from the specified metric and its Levi–Civita connection. It can be defined without knowing how the manifold is drawn in another space. The second fundamental form, by contrast, differentiates a tangent vector along the surface in the external space and retains the component perpendicular to the current tangent space. It separates changes within the surface from bending toward the external space. This depends on the chosen ambient embedding and its metric.

Compare ambient shapes and Gaussian curvature separately for the three surfaces below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Plane and cylinder both have zero Gaussian curvature despite different ambient bending while the sphere has positive Gaussian curvature](../../figures/assets/A09-GEO/A09-GEO-06-plane-cylinder-sphere.svg)

<figcaption>The plane and cylinder both have Gaussian curvature 0 under their internal metrics. The cylinder and sphere both appear bent in the ambient space, but the sphere has positive Gaussian curvature. Visible external bending alone cannot classify internal curvature.</figcaption>
</figure>

### What sectional curvature is assigned to

Sectional curvature assigns an intrinsic curvature to each tangent two-plane at a point. A two-plane here is a 2-dimensional linear subspace of the tangent space, spanned by two linearly independent vectors at that point. It does not mean an arbitrary plane drawn in the ambient space or a small planar patch on the manifold. Changing the basis of the same two-plane does not change $K(\sigma)$. In dimensions 3 and above, the value can differ between two-planes selected at the same point. On a 2-dimensional surface, the tangent space itself is the only two-plane, and its sectional curvature is Gaussian curvature.

The axes below represent tangent-vector components at one point, not point coordinates on the manifold.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two different two-dimensional linear subspaces spanned by e one e two and e one e three lie in the same three-dimensional tangent space](../../figures/assets/A09-GEO/A09-GEO-06-tangent-two-planes.svg)

<figcaption>In the 3-dimensional tangent space at the same point p, σ₁₂=span(e₁,e₂) and σ₁₃=span(e₁,e₃) are different two-planes. The figure shows linear subspaces of a vector space, not ambient surface patches. There is no guarantee that their sectional curvatures are equal.</figcaption>
</figure>

Instead of changing the plane itself, change only the basis of the same plane below.

<figure class="lesson-figure" markdown="1">

![The pairs e one e two and u e one plus e two v minus e one plus e two span the same tangent two-plane](../../figures/assets/A09-GEO/A09-GEO-06-basis-same-plane.svg)

<figcaption>The blue and purple bases span the same σ, so K(σ) is unchanged. If the manifold is a surface, TₚM itself is 2-dimensional and there is only one such two-plane; its curvature is Gaussian curvature.</figcaption>
</figure>

A plane and a cylinder can be unfolded locally while preserving lengths, so both have Gaussian curvature 0. But the cylinder is extrinsically curved in 3-dimensional ambient space. A sphere has positive Gaussian curvature and therefore cannot be unfolded into a plane without distortion.

## Small example

Rolling paper into a cylinder does not change the lengths and angles of short line segments on the paper. The embedding bends while the intrinsic metric remains flat.

Represent a small region of a cylinder with radius $r>0$ by $F(s,z)=(r\cos(s/r),r\sin(s/r),z)$. Here $s$ is length along the circumference, and $z$ is height. The output velocities in the two coordinate directions are

$$
\partial_sF=(-\sin(s/r),\cos(s/r),0),
\qquad
\partial_zF=(0,0,1)
$$

The two vectors have length 1 and are perpendicular, so $J_F^\top J_F$ from GEO-04 is the identity. This explains why the cylinder has the same metric as the unfolded plane's coordinates $(s,z)$. Differentiating once more with respect to $s$, however, gives the normal vector $\partial_s^2F=(-\cos(s/r)/r,-\sin(s/r)/r,0)$, which is not 0. Thus the ambient embedding can be bent even when the intrinsic metric is flat.

This correspondence is local. A full turn around the circumference returns to the original point, so periodicity prevents a conclusion that the cylinder and plane are globally the same space.

Compare corresponding edges of the unfolded coordinate patch and the cylinder patch below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A unit square in arc-length and height coordinates maps to a curved cylinder patch while both tangent directions retain unit length and a right angle](../../figures/assets/A09-GEO/A09-GEO-06-unfold-cylinder.svg)

<figcaption>For a cylinder of radius 1, s is length along the circumference and z is height. Before and after unfolding, the blue and green edges each have length 1 and meet at a right angle. Even though the boundary looks bent in 3 dimensions, the metric in these coordinates is G=I.</figcaption>
</figure>

Check the direction of change in the unit tangent in the cross-section below.

<figure class="lesson-figure" markdown="1">

![At a point on the radius-one cylinder cross-section the unit tangent is vertical and its arc-length derivative is a nonzero inward normal vector](../../figures/assets/A09-GEO/A09-GEO-06-cylinder-normal-derivative.svg)

<figcaption>At s=0 in the z=0 cross-section, the blue ∂sF=(0,1,0) is a unit tangent. The orange ∂s²F=(−1,0,0) points in the cylinder's normal direction, so ambient bending is not 0. This is compatible with internal Gaussian curvature being 0.</figcaption>
</figure>

Check how different input coordinates return to the same point on the cylinder below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The unwrapped cylinder coordinates zero zero and two pi zero are distinct but map to the same cylinder point one zero zero](../../figures/assets/A09-GEO/A09-GEO-06-cylinder-periodicity.svg)

<figcaption>After a full turn around the circumference, F(0,0)=F(2π,0)=(1,0,0). The blue point and purple outlined point are separated in input coordinates but overlap in the output. Local length preservation does not imply a global one-to-one correspondence.</figcaption>
</figure>

### Bending of a path versus curvature of a space

A bent path within a space must be distinguished from the intrinsic curvature of that space. A circular path drawn in a plane is bent, but the plane's intrinsic curvature is 0. The shape of a single activation trajectory likewise does not directly determine the curvature of an entire manifold. Applying a 2-dimensional projection can also change lengths and angles, so visible bending cannot be read as metric curvature in the original space.

The circle below is one path in a plane, not the entire manifold.

<figure class="lesson-figure" markdown="1">

![A circular curved path lies in a Cartesian plane whose Euclidean metric and Gaussian curvature remain flat](../../figures/assets/A09-GEO/A09-GEO-06-path-not-space.svg)

<figcaption>The purple circular path bends, but the manifold here is the plane R². Its Euclidean metric is G=I and its Gaussian curvature is 0. A path's shape and a space's curvature provide information about different objects.</figcaption>
</figure>

The same green direction in the projection below shows that the displayed image does not preserve the original length.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Orthogonal projection of a unit circle in a tilted flat plane produces an ellipse and shrinks an original unit tangent direction to length one quarter](../../figures/assets/A09-GEO/A09-GEO-06-projection-distortion.svg)

<figcaption>The tilted plane on the left is intrinsically flat, and the blue circle is a unit circle under its induced metric. Projection onto x,y produces the purple ellipse and reduces the displayed length of the unit direction (0,1/4,√15/4) to 1/4. Without checking the original metric, the projected shape or distances cannot be used directly as geometric estimates.</figcaption>
</figure>

## Common misconceptions

- A bent-looking 2-dimensional projection is not a curvature estimate for the original representation manifold.
- The image of a nonlinear map does not necessarily have nonzero intrinsic curvature.

## Exercises

### 1. Cylinder
Explain a cylinder's Gaussian curvature and extrinsic bending separately.
<details><summary>Show solution</summary>

Its Gaussian curvature is 0, but it bends in the normal direction in the ambient 3-dimensional space.
</details>

### 2. Sphere
Use curvature to explain why a sphere cannot be unfolded into a plane while preserving lengths.
<details><summary>Show solution</summary>

A sphere has positive intrinsic Gaussian curvature, while a plane has curvature 0, so the whole sphere cannot be unfolded through a local isometry.
</details>

### 3. Coordinate lines
Using polar coordinates on a flat plane makes coordinate lines curved. Does intrinsic curvature appear too?
<details><summary>Show solution</summary>

No. The coordinate representation changes, but the plane's intrinsic curvature remains 0.
</details>

### 4. Model interpretability
State two additional checks needed for a curvature claim when a class trajectory looks bent in a PCA plot.
<details><summary>Show solution</summary>

Control projection distortion, and check the stability of the curvature estimator with respect to the metric and neighborhood defined in the original space.
</details>

## Evidence and update boundaries

The distinctions among the Riemann tensor, sectional curvature, and second fundamental form follow standard differential geometry. Definitions can be found in Danny Calegari's [*Notes on Riemannian Geometry*, §§3.4, 5.1, 5.3](https://math.uchicago.edu/~dannyc/courses/riem_geo_2013/riem_geo_notes.pdf). The Gauss equation and component calculations for the curvature tensor are outside the scope.

## Lesson summary

- Intrinsic curvature is determined by the manifold's internal metric.
- Extrinsic curvature depends on the ambient embedding.
- A cylinder is intrinsically flat but extrinsically curved.
- Bending in a representation plot must not be interpreted directly as curvature.

## Pass criteria

- Can you explain the curvature differences among a plane, cylinder, and sphere?
- Can you state the checks needed to move from visible bending to an intrinsic claim?

## Next lesson

- [A09-GEO-07 Pitfalls in activation manifold analysis](A09-GEO-07-activation-manifold-pitfalls.md)

## Author checklist

- [x] Intrinsic and extrinsic curvature are distinguished.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
