---
id: "A09-GEO-04"
title: "Pullback metrics and Jacobians"
part: 4
stage: "A09-GEO"
status: "complete"
prerequisites: ["A09-GEO-03", "M03-11"]
estimated_time: "90–120 minutes"
---

# A09-GEO-04. Pullback metrics and Jacobians

## Why this lesson matters

Coordinate differences alone cannot tell us how strongly a small change in a latent variable appears in activations or outputs. When the Jacobian of a map transfers the output metric to the input space, we can interpret directional input sensitivities in terms of lengths and angles.

## Learning objectives

- Calculate a pullback metric using a Jacobian.
- Relate the singular values of a Jacobian to local length distortion.
- Explain why a loss of rank makes the metric degenerate.
- Distinguish the question answered by decoder-induced geometry.

## Prerequisite check

- Prerequisite lessons: [A09-GEO-03 Metrics and length](A09-GEO-03-metric-length.md), [M03-11 Jacobians](../../part-1-foundations/M03/M03-11-jacobian.md)
- Check question: How does a Jacobian relate small input changes to small output changes?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $F:Z\to X$ | `F from Z to X` | Representation or decoder map | smooth map |
| $J_F(z)$ | `the Jacobian of F at z` | Local linearization of $F$ | $n\times d$ |
| $F^*g$ | `the pullback of g by F` | Bilinear form transferring the metric on $X$ to $Z$ | a metric under full column rank |
| $G_Z(z)$ | `G sub Z of z` | Coordinate pullback metric | $d\times d$ |

## Core concepts

Fix the metric on $X$ to be the Euclidean inner product.

First send the input directions $u,v$ to the output velocities $J_F(z)u,J_F(z)v$, and then calculate their inner product in the output space. Rewriting this as an input-space calculation gives

$$
(J_F(z)u)^\top(J_F(z)v)
=u^\top\bigl(J_F(z)^\top J_F(z)\bigr)v
$$

Thus, the matrix representing the bilinear form on input tangent vectors is

$$
G_Z(z)=J_F(z)^\top J_F(z)
$$

For $v\in T_zZ$,

$$
\|v\|_{G_Z}^2=v^\top J_F(z)^\top J_F(z)v=\|J_F(z)v\|_2^2
$$

so the input tangent vector's length is measured by the norm of its instantaneous output velocity. This is distinct from a finite output change under a general nonlinear map. The diagonal entries of $G_Z$ are the squared norms of the Jacobian columns, and the off-diagonal entries are inner products between different columns. Together, these entries record how long the input coordinate-axis directions become in the output and how much they overlap.

Follow the sequence of sending two input directions to the output and then calculating their inner product.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two orthogonal input coordinate directions become nonorthogonal output directions under a shear Jacobian, and their output inner product equals the input pullback pairing](../../figures/assets/A09-GEO/A09-GEO-04-pullback-pairing.svg)

<figcaption>For the educational J=[[1,1],[0,1]], inputs u=(1,0), v=(0,1) have Euclidean inner product 0, but outputs Ju=(1,0), Jv=(1,1) have inner product 1. The input pairing calculated with G_Z=JᵀJ also gives the same value, 1.</figcaption>
</figure>

### Singular values and length multipliers

The right singular vectors of $J_F$ are its principal input directions, and a singular value is the local expansion factor in the corresponding direction. The SVD sends a unit right singular vector to $\sigma_i$ times the corresponding unit left singular vector. The output length of that input direction is therefore $\sigma_i$, and its squared length is $\sigma_i^2$. The same right singular vector is an eigenvector of $J_F^\top J_F$ with eigenvalue $\sigma_i^2$. To read a pullback metric eigenvalue as a length multiplier, take its square root.

Compare the unit input directions with the output ellipse produced by the Jacobian.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A unit input circle maps to an ellipse with output axis lengths two and one, while pullback eigenvalues are four and one](../../figures/assets/A09-GEO/A09-GEO-04-singular-stretch.svg)

<figcaption>The first unit direction maps to length 2 and the second to length 1. The singular values are (2,1), and the pullback eigenvalues are their squares, (4,1). The ellipse on the right is the image of the input Euclidean unit circle, not the unit-length boundary in the output.</figcaption>
</figure>

### When the pullback is a metric

If $J_F$ has full column rank, $G_Z$ is positive definite. No nonzero input vector becomes zero after passing through the Jacobian, so $v^\top G_Zv=\|J_Fv\|_2^2>0$. If $F$ is smooth and this condition holds at every point, the pullback is a Riemannian metric on the input space. This condition is not automatically guaranteed for an arbitrary $F$.

When the rank drops, some $v\ne0$ satisfies $J_Fv=0$, giving that direction zero length. The matrix is still positive semidefinite, but it fails the positive-definite condition for a metric defining a tangent vector norm. For example, if two columns are equal, $v=(1,-1)$ adds one column and subtracts the same column, giving zero output velocity.

What becomes indistinguishable here is the first-order change. The function $F(z)=z^3$ has derivative zero at $z=0$, but a small nonzero $z$ produces a nonzero output. A null direction therefore does not by itself imply identical outputs after a finite displacement or a complete loss of that information.

Equal Jacobian columns make two input directions overlap in the output.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two equal Jacobian columns send input basis directions to the same output vector so their nonzero difference maps to zero](../../figures/assets/A09-GEO/A09-GEO-04-null-collapse.svg)

<figcaption>The two columns of the educational J=[[1,1],[1,1]] are equal, so Je₁ and Je₂ are the same vector on the right. The orange input e₁−e₂=(1,−1) is nonzero, but its output velocity is 0, marked by the hollow orange circle, and its pullback squared length is also 0.</figcaption>
</figure>

A finite output change can remain even at a point with zero first-order change.

<figure class="lesson-figure" markdown="1">

![The cubic function has horizontal tangent and zero derivative at zero but maps a finite input zero point four to nonzero output zero point zero six four](../../figures/assets/A09-GEO/A09-GEO-04-cubic-first-order-null.svg)

<figcaption>The tangent to F(z)=z³ at z=0 is horizontal, and the Jacobian is 0. But F(0.4)−F(0)=0.064, so a first-order null direction does not establish identical outputs after a finite displacement.</figcaption>
</figure>

### The question answered by decoder-induced geometry

A decoder-induced metric asks how strongly the same latent velocity appears in the output through a specified decoder. It does not directly select directions of high latent sample variance or semantic importance. Changing the output units or choosing a different decoder also changes this length rule. When comparing two decoders, fix the correspondence between latent points and directions, together with the output metric and scale.

Changing a decoder's output scale changes the length rule even for the same latent direction.

<figure class="lesson-figure" markdown="1">

![Multiplying a decoder output by two doubles output velocity lengths and quadruples the pullback matrix for the same latent direction](../../figures/assets/A09-GEO/A09-GEO-04-decoder-output-scale.svg)

<figcaption>The educational F(z)=(2z₁,z₂) and 2F are compared in the same output coordinates with a Euclidean metric. For the same latent direction (1,0), the output length changes from 2 to 4, and the pullback matrix becomes 4 times as large. A large length does not mean semantic importance or latent variance.</figcaption>
</figure>

## Small example

If $F(z_1,z_2)=(2z_1,z_2,0)$, then $J_F=\operatorname{diag}(2,1)$ with an appended zero row, and $G_Z=\operatorname{diag}(4,1)$. A small displacement in the $z_1$ direction is doubled in the output.

The first column $(2,0,0)$ has squared norm 4, and the second column $(0,1,0)$ has squared norm 1. Their inner product is 0, so the off-diagonal entries of $G_Z$ are also 0. Although the output is three-dimensional, the input tangent vector is two-dimensional, so the pullback matrix is $2\times2$. This example is a linear map, so even a finite-step output change agrees exactly with the Jacobian calculation.

Distinguish the number of output rows in the Jacobian from the number of input axes in the pullback.

<figure class="lesson-figure" markdown="1">

![A three output by two input Jacobian with columns two zero zero and zero one zero produces a two by two diagonal pullback matrix four one](../../figures/assets/A09-GEO/A09-GEO-04-decoder-matrix-shape.svg)

<figcaption>The decoder in the text has a Jacobian with 3 output rows and 2 input columns. Placing the squared column norms 4 and 1 and the cross-column inner product 0 into the input-axis pairs gives a 2×2 G_Z. Despite the zero row, the two input columns are independent, so the pullback is positive definite.</figcaption>
</figure>

## Common misconceptions

- $J_F^\top J_F$ is not the unique input-space metric in every situation. It depends on the chosen map and output metric.
- A large singular value does not establish that a feature is semantically important.

## Exercises

### 1. Pullback calculation
Find $G_Z$ for $F(z_1,z_2)=(z_1+z_2,z_1-z_2)$.
<details><summary>Show solution</summary>

Since $J_F=\begin{bmatrix}1&1\\1&-1\end{bmatrix}$, we have $G_Z=J_F^\top J_F=2I$.
</details>

### 2. Singular values
If the singular values of $J_F$ are $(3,1)$, by what factor does the length change along each corresponding right singular vector?
<details><summary>Show solution</summary>

The factors are 3 and 1, respectively. The squared-length factors are 9 and 1.
</details>

### 3. Rank deficiency
If two columns of $J_F$ are equal, can $G_Z$ be positive definite?
<details><summary>Show solution</summary>

No. The columns are linearly dependent, so a null direction exists and its pullback length is 0.
</details>

### 4. Model interpretation
State two conditions to fix when comparing the pullback metrics of two decoders.
<details><summary>Show solution</summary>

The same latent points and directions and the same output metric are needed. Preprocessing and scale must also be fixed.
</details>

## Sources and update boundaries

The pullback metric and immersion conditions follow the standard definitions in differential geometry. This lesson does not cover the general formula for a non-Euclidean output metric or the pullback of a measure.

## Lesson summary

- A pullback metric records map-induced length changes in the input space.
- With a Euclidean output metric, it is calculated as $J_F^\top J_F$.
- Singular values are local directional expansion factors.
- A loss of rank produces locally indistinguishable directions.

## Pass criteria

- Can you calculate the pullback metric of a simple map?
- Can you distinguish and explain the Jacobian spectrum and local distortion?

## Next lesson

- [A09-GEO-05 Geodesics and connections](A09-GEO-05-geodesic-connection.md)

## Author checklist

- [x] Pullback metrics and Jacobians are connected.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
