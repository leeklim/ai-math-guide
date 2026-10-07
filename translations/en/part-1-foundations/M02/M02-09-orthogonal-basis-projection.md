---
id: "M02-09"
title: "Orthogonal bases and orthogonal projection"
part: 1
stage: "M02"
status: "complete"
prerequisites:
  - "M02-03"
  - "M02-07"
  - "M02-08"
estimated_time: "115~140 minutes"
---

# M02-09. Orthogonal bases and orthogonal projection

## Why this lesson matters

When basis vectors are mutually orthogonal, inner products give a vector's coordinates without solving a linear system. If every basis vector also has length 1, each coordinate is the inner product with the corresponding direction.

An orthogonal basis lets us project a vector onto a subspace and compute its closest approximation. Representation analysis uses the same computation to project activations onto a chosen subspace or reconstruct the part explained by PCA components.

## Learning objectives

By the end of this lesson, you should be able to:

- Distinguish orthogonal sets, orthogonal bases, and orthonormal bases.
- Find coordinates in an orthonormal basis using inner products.
- Project onto a subspace spanned by several basis vectors.
- Verify symmetry and idempotence of an orthogonal projection matrix.
- Orthonormalize a small basis using the Gram-Schmidt process.
- Interpret least squares as orthogonal projection onto a column space.

## Prerequisite check

- Prerequisite lesson: [M02-03 Inner products, length, and angles](M02-03-inner-product-length-angle.md)
- Prerequisite lesson: [M02-07 Linear independence, bases, and dimension](M02-07-linear-independence-basis-dimension.md)
- Prerequisite lesson: [M02-08 Kernel, image, and rank](M02-08-kernel-image-rank.md)
- Check question: Can you test orthogonality and compute orthogonal projection onto one vector?
- Check question: Can you explain a basis, a coordinate vector, and a matrix's column space?

Review the prerequisite lessons first if inner products, bases, or column spaces are unclear.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| Orthogonal set | `orthogonal set` | A set whose distinct vectors have inner product 0 | The zero vector is not included in a basis. |
| Orthonormal set | `orthonormal set` | Mutually orthogonal vectors, each with norm 1 | $\mathbf q_i^\top\mathbf q_j=\delta_{ij}$ |
| $\mathbf Q$ | `Q` | A matrix collecting orthonormal column vectors | $\mathbf Q^\top\mathbf Q=\mathbf I$ |
| $\mathbf P=\mathbf Q\mathbf Q^\top$ | `P equals Q Q transpose` | The orthogonal projection matrix onto $\operatorname{im}(\mathbf Q)$ | $\mathbf P^\top=\mathbf P$, $\mathbf P^2=\mathbf P$ |
| $\widehat{\mathbf x}$ | `x hat` | An orthogonal projection onto a subspace, or an approximation | $\widehat{\mathbf x}=\mathbf P\mathbf x$ |
| Least squares | `least squares` | Minimizing the squared residual norm | Defined even when no exact solution exists |

## Core concept 1. An orthogonal basis uses directions that do not interfere

Vectors $\mathbf v_1,\ldots,\mathbf v_k$, none equal to 0, form an orthogonal set if

\[
\mathbf v_i^\top\mathbf v_j=0
\qquad
(i\ne j)
\]

If the set spans a space $V$, it is an orthogonal basis of $V$.

Orthogonal vectors, none equal to 0, are linearly independent. Indeed, multiplying both sides of

\[
c_1\mathbf v_1+\cdots+c_k\mathbf v_k=\mathbf 0
\]

by $\mathbf v_j^\top$ gives

\[
c_j\|\mathbf v_j\|_2^2=0
\]

so $c_j=0$.

## Core concept 2. Norms of 1 make the basis orthonormal

Dividing an orthogonal vector by its own norm gives a unit vector:

\[
\mathbf q_i
=
\frac{\mathbf v_i}{\|\mathbf v_i\|_2}
\]

Orthonormal vectors satisfy

\[
\mathbf q_i^\top\mathbf q_j
=
\begin{cases}
1,&i=j\\
0,&i\ne j
\end{cases}
\]

The right side is written $\delta_{ij}$ using the Kronecker delta.

Collecting orthonormal columns in

\[
\mathbf Q=
\begin{bmatrix}
\mathbf q_1&\cdots&\mathbf q_k
\end{bmatrix}
\in\mathbb R^{n\times k}
\]

gives

\[
\mathbf Q^\top\mathbf Q=\mathbf I_k
\]

Entry $(i,j)$ of this product is $\mathbf q_i^\top\mathbf q_j$. Diagonal entries are squared column norms, each 1; off-diagonal entries are inner products of different columns, each 0. Normalization divides by a positive norm, preserving direction and span, and an inner product that was 0 remains 0.

The figure below compares orthogonal vectors before and after normalization on equally scaled grids. The right angle stays the same, while each arrow's endpoint moves to the unit circle.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Perpendicular vectors of length square root two and their normalized unit vectors on equal-scale coordinate grids](../../figures/assets/M02/M02-09-normalize-orthogonal-directions.svg)

<figcaption>(1,1) and (1,−1) are orthogonal but have length √2. Dividing each by √2 preserves direction and span while making the length 1, adding the unit-length condition to orthogonality.</figcaption>
</figure>

## Core concept 3. Coordinates in an orthonormal basis are inner products

Suppose $\mathcal Q=(\mathbf q_1,\ldots,\mathbf q_k)$ is an orthonormal basis of a subspace $V$ and $\mathbf x\in V$. Multiplying both sides of

\[
\mathbf x
=
c_1\mathbf q_1+\cdots+c_k\mathbf q_k
\]

by $\mathbf q_j^\top$ gives

\[
\mathbf q_j^\top\mathbf x=c_j
\]

The coordinate vector is therefore

\[
[\mathbf x]_{\mathcal Q}
=
\mathbf Q^\top\mathbf x
\]

and the original vector is reconstructed as

\[
\mathbf x=\mathbf Q\mathbf Q^\top\mathbf x
\]

The figure below converts the coefficients read along the two orthonormal directions in Example 1 back into directional components. The blue and purple components are perpendicular, and their sum is the original vector.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Vector three one reconstructed from perpendicular components two two and one minus one along an orthonormal basis](../../figures/assets/M02/M02-09-inner-product-coordinates.svg)

<figcaption>Multiplying the unit basis vectors by the inner-product coefficients 2√2 and √2 gives (2,2) and (1,−1). The coordinate coefficients describe the lengths of the directional components; summing those components reconstructs (3,1).</figcaption>
</figure>

## Core concept 4. Subspace projection adds the components along each basis direction

Even if $\mathbf x\in\mathbb R^n$ lies outside $V$, we can compute its coefficient along each orthonormal basis direction:

\[
c_i=\mathbf q_i^\top\mathbf x
\]

Its orthogonal projection onto $V$ is

\[
\operatorname{proj}_V(\mathbf x)
=
\sum_{i=1}^{k}
(\mathbf q_i^\top\mathbf x)\mathbf q_i
\]

Each term is one directional component of $\mathbf x$. Because the directions are orthogonal, the component along one basis direction does not enter the coefficient along another. The sum of the components lies in $V$; the next section shows that the residual is perpendicular to $V$.

In matrix form,

\[
\widehat{\mathbf x}
=
\mathbf Q\mathbf Q^\top\mathbf x
\]

Define the orthogonal projection matrix as

\[
\mathbf P=\mathbf Q\mathbf Q^\top
\]

Then $\widehat{\mathbf x}=\mathbf P\mathbf x$. $\mathbf Q^\top$ reads $k$ directional coefficients from an $n$-component vector, and $\mathbf Q$ combines those coefficients with basis vectors to produce an $n$-component vector. If $\mathbf x\in V$, this reconstructs the original vector. If $\mathbf x\notin V$, $\mathbf Q^\top\mathbf x$ gives coordinates of the projected vector, not of the whole $\mathbf x$. The $k$ coefficients do not contain the component outside $V$.

The figure below separates the two retained directional components and the discarded residual in the plane projection of Example 2. The two coefficients read by $\mathbf Q^\top$ reconstruct the approximation on the plane, not the entire input.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A three-dimensional vector decomposed into its coordinate-plane projection and a vertical orthogonal residual](../../figures/assets/M02/M02-09-plane-projection.svg)

<figcaption>The input (2,−1,4) projects to (2,−1,0), leaving the residual (0,0,4). The two coefficients within the green plane do not contain the residual component. Since the projection is already on the plane, projecting it again changes nothing.</figcaption>
</figure>

## Core concept 5. The residual is orthogonal to the subspace, and the projection is closest

Let the residual be

\[
\mathbf r
=
\mathbf x-\widehat{\mathbf x}
\]

Substituting the projection formula and $\mathbf Q^\top\mathbf Q=\mathbf I_k$ gives

\[
\mathbf Q^\top\mathbf r
=\mathbf Q^\top\mathbf x
-\mathbf Q^\top\mathbf Q\mathbf Q^\top\mathbf x
=\mathbf Q^\top\mathbf x-\mathbf Q^\top\mathbf x
=\mathbf 0
\]

Each component being 0 means that the residual is orthogonal to each basis vector. Every vector of $V$ is a linear combination of these basis vectors, so its inner product with the residual is also 0. The residual is therefore perpendicular to all of $V$.

For any $\mathbf y\in V$,

\[
\mathbf x-\mathbf y
=
\mathbf r+(\widehat{\mathbf x}-\mathbf y)
\]

The terms are orthogonal: the second is the difference of two vectors in $V$ and thus lies in $V$, while the first is orthogonal to $V$. Expanding the squared norm as an inner product gives a cross term of 0, yielding the Pythagorean relation

\[
\|\mathbf x-\mathbf y\|_2^2
=
\|\mathbf r\|_2^2
+
\|\widehat{\mathbf x}-\mathbf y\|_2^2
\ge
\|\mathbf r\|_2^2
\]

The second squared norm on the right cannot be negative and is 0 only when $\mathbf y=\widehat{\mathbf x}$. Thus $\widehat{\mathbf x}$ is the closest vector in $V$ to $\mathbf x$, and it is unique.

The figure below places the projection and another candidate together, comparing the two terms in the squared distance as the legs of a right triangle.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A right triangle showing the perpendicular residual distance and the extra in-subspace distance to another candidate](../../figures/assets/M02/M02-09-closest-point-triangle.svg)

<figcaption>The shortest distance from (2,3) to the horizontal subspace is 3. Moving the candidate from (2,0) to (4,0) adds an in-subspace distance of 2, increasing the squared distance from 9 to 13.</figcaption>
</figure>

## Core concept 6. An orthogonal projection matrix is symmetric and idempotent

If

\[
\mathbf P=\mathbf Q\mathbf Q^\top
\]

then

\[
\mathbf P^\top
=
(\mathbf Q\mathbf Q^\top)^\top
=
\mathbf Q\mathbf Q^\top
=
\mathbf P
\]

Also,

\[
\mathbf P^2
=
\mathbf Q\mathbf Q^\top\mathbf Q\mathbf Q^\top
=
\mathbf Q\mathbf I_k\mathbf Q^\top
=
\mathbf P
\]

A projected vector is already in the subspace, so applying the same projection again leaves it unchanged.

## Core concept 7. The Gram-Schmidt process orthonormalizes a basis

Start with linearly independent vectors $\mathbf v_1,\ldots,\mathbf v_k$. Normalize the first:

\[
\mathbf q_1
=
\frac{\mathbf v_1}{\|\mathbf v_1\|_2}
\]

Subtract the $\mathbf q_1$ component from the second vector:

\[
\mathbf u_2
=
\mathbf v_2
-
(\mathbf q_1^\top\mathbf v_2)\mathbf q_1
\]

Then normalize it:

\[
\mathbf q_2
=
\frac{\mathbf u_2}{\|\mathbf u_2\|_2}
\]

An inner product shows why the component was subtracted:

\[
\mathbf q_1^\top\mathbf u_2
=\mathbf q_1^\top\mathbf v_2
-(\mathbf q_1^\top\mathbf v_2)(\mathbf q_1^\top\mathbf q_1)
=0
\]

If $\mathbf u_2=\mathbf 0$, then $\mathbf v_2$ is a multiple of $\mathbf q_1$, hence of $\mathbf v_1$. The initial independence assumption excludes this, so division by the norm is possible.

$\mathbf u_2$ is a linear combination of the two original vectors. Conversely, $\mathbf v_2$ is a linear combination of $\mathbf u_2$ and $\mathbf q_1$. Subtraction and normalization therefore preserve their span. For each later vector, subtract its components along all preceding $\mathbf q_i$. A residual of 0 would mean the vector lay in the span of the earlier vectors, so independent inputs give a residual different from 0 at every step.

This process constructs an orthonormal basis while preserving the span. Modified Gram-Schmidt or QR factorization improves stability in numerical computation.

The figure below subtracts the component along the existing direction from the second vector in Example 3, then normalizes what remains. Removing the component and setting the length to 1 have different roles.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Gram Schmidt stages subtracting the projection from one zero and normalizing the remaining one half minus one half vector](../../figures/assets/M02/M02-09-gram-schmidt-stages.svg)

<figcaption>The residual (½,−½) on the left is already orthogonal to the first basis direction. On the right, dividing it by its length makes it a unit vector. The plane spanned by the first and new directions is the span of the original two vectors.</figcaption>
</figure>

## Core concept 8. Least squares is orthogonal projection onto a column space

When $\mathbf A\mathbf c=\mathbf b$ has no exact solution, solve

\[
\min_{\mathbf c}
\|\mathbf A\mathbf c-\mathbf b\|_2^2
\]

to make $\mathbf A\mathbf c$ close to $\mathbf b$. Every $\mathbf A\mathbf c$ belongs to $\operatorname{im}(\mathbf A)$, and every vector in that column space can be obtained with some $\mathbf c$. Varying coefficients is therefore equivalent to comparing candidate vectors within the column space. By the closest-vector property above, the optimal approximation is the orthogonal projection of $\mathbf b$ onto the column space. The same minimization is defined when an exact solution exists; then the minimum residual is 0.

The optimal residual

\[
\mathbf r=\mathbf b-\mathbf A\widehat{\mathbf c}
\]

is orthogonal to every column, so

\[
\mathbf A^\top\mathbf r=\mathbf 0
\]

This gives the normal equations:

\[
\mathbf A^\top\mathbf A\widehat{\mathbf c}
=
\mathbf A^\top\mathbf b
\]

The difference between the target and approximation must be perpendicular to every column direction. Satisfying this residual-orthogonality condition allows the preceding distance decomposition, so it guarantees optimality.

The optimal output $\mathbf A\widehat{\mathbf c}$ is unique, but uniqueness of the coefficients $\widehat{\mathbf c}$ is a separate question. Adding a vector other than 0 in the kernel of $\mathbf A$ to the coefficients gives the same optimal output. If the columns are independent, the kernel is $\{\mathbf 0\}$, so the coefficients are unique too.

The figure below shows a least-squares problem where changing one coefficient moves the output along the column-space line. A target outside the line cannot be reached exactly, so the closest output is chosen instead.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Least squares on a diagonal column-space line with target three one, projected output two two, and perpendicular residual one minus one](../../figures/assets/M02/M02-09-least-squares-column-line.svg)

<figcaption>A=(1,1)ᵀ produces only outputs (c,c). The closest output to the target (3,1) is (2,2) at c=2; the residual (1,−1) is orthogonal to the column of A.</figcaption>
</figure>

## Example 1. Coordinates in an orthonormal basis

The vectors

\[
\mathbf q_1=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\1\end{bmatrix},
\qquad
\mathbf q_2=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\-1\end{bmatrix}
\]

form an orthonormal basis of $\mathbb R^2$. For $\mathbf x=\begin{bmatrix}3\\1\end{bmatrix}$, the coordinates are

\[
c_1
=
\mathbf q_1^\top\mathbf x
=
\frac{4}{\sqrt2}
=
2\sqrt2
\]

\[
c_2
=
\mathbf q_2^\top\mathbf x
=
\frac{2}{\sqrt2}
=
\sqrt2
\]

Thus

\[
[\mathbf x]_{\mathcal Q}
=
\begin{bmatrix}
2\sqrt2\\
\sqrt2
\end{bmatrix}
\]

## Example 2. Projection onto a plane

The vectors

\[
\mathbf q_1=
\begin{bmatrix}1\\0\\0\end{bmatrix},
\qquad
\mathbf q_2=
\begin{bmatrix}0\\1\\0\end{bmatrix}
\]

span a plane $V$. The orthogonal projection of

\[
\mathbf x=
\begin{bmatrix}2\\-1\\4\end{bmatrix}
\]

onto that plane is

\[
\widehat{\mathbf x}
=
(\mathbf q_1^\top\mathbf x)\mathbf q_1
+
(\mathbf q_2^\top\mathbf x)\mathbf q_2
=
\begin{bmatrix}2\\-1\\0\end{bmatrix}
\]

The residual is

\[
\mathbf r=
\begin{bmatrix}0\\0\\4\end{bmatrix}
\]

and is orthogonal to both basis vectors.

## Example 3. A Gram-Schmidt computation

Start with

\[
\mathbf v_1=
\begin{bmatrix}1\\1\end{bmatrix},
\qquad
\mathbf v_2=
\begin{bmatrix}1\\0\end{bmatrix}
\]

Then

\[
\mathbf q_1
=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\1\end{bmatrix}
\]

Subtracting the $\mathbf q_1$ component from the second vector gives

\[
\mathbf u_2
=
\begin{bmatrix}1\\0\end{bmatrix}
-
\frac{1}{\sqrt2}\mathbf q_1
=
\begin{bmatrix}1/2\\-1/2\end{bmatrix}
\]

Since $\|\mathbf u_2\|_2=1/\sqrt2$,

\[
\mathbf q_2
=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\-1\end{bmatrix}
\]

## Example 4. Projecting onto a representation subspace

Suppose $\mathbf Q\in\mathbb R^{d\times k}$ has orthonormal columns representing an activation subspace. The component of an activation $\mathbf h\in\mathbb R^d$ in this subspace is

\[
\widehat{\mathbf h}
=
\mathbf Q\mathbf Q^\top\mathbf h
\]

and the remaining component is

\[
\mathbf r
=
\mathbf h-\widehat{\mathbf h}
\]

The ratio

\[
\frac{\|\widehat{\mathbf h}\|_2^2}
{\|\mathbf h\|_2^2}
\]

is the fraction of this vector's squared norm in the subspace when $\mathbf h\ne\mathbf 0$. Projection and residual are orthogonal, so the total squared norm is the sum of their squared norms, and the ratio lies between 0 and 1. For the zero vector, the denominator is also 0, so the ratio is undefined. This is a geometric decomposition. The subspace's meaning and functional use by the model require separate data comparisons and interventions.

## Common misconceptions

### Misconception 1. Every vector of an orthogonal basis has length 1

An orthogonal basis requires mutual orthogonality only. If each length is also 1, it is an orthonormal basis.

### Misconception 2. Orthonormal columns imply $\mathbf Q\mathbf Q^\top=\mathbf I$

For $\mathbf Q\in\mathbb R^{n\times k}$ with orthonormal columns, $\mathbf Q^\top\mathbf Q=\mathbf I_k$. If $k<n$, $\mathbf Q\mathbf Q^\top$ is a projection onto the $k$-dimensional column space, not the identity on all of $\mathbb R^n$.

### Misconception 3. Orthogonal projection sets some coordinates to 0

It looks this way only when standard coordinate axes form a basis of the subspace. For a general subspace, all standard coordinates can change together.

### Misconception 4. A large projected activation means the model uses that subspace

A large projection norm is an observation that the activation contains a large component along the subspace. Functional use must be assessed through interventions that remove or replace that component.

## Exercises

### 1. Orthogonality and orthonormality

Determine whether

\[
\mathbf v_1=
\begin{bmatrix}1\\1\\0\end{bmatrix},
\qquad
\mathbf v_2=
\begin{bmatrix}1\\-1\\0\end{bmatrix}
\]

are orthogonal, and normalize each.

<details>
<summary>Show solution</summary>

Since

\[
\mathbf v_1^\top\mathbf v_2=1-1=0
\]

they are orthogonal. Both norms are $\sqrt2$, giving

\[
\mathbf q_1=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\1\\0\end{bmatrix},
\qquad
\mathbf q_2=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\-1\\0\end{bmatrix}
\]

</details>

### 2. Orthonormal-basis coordinates

Find the coordinates of

\[
\mathbf x=
\begin{bmatrix}4\\2\\0\end{bmatrix}
\]

in the subspace spanned by $\mathbf q_1,\mathbf q_2$ in Exercise 1.

<details>
<summary>Show solution</summary>

\[
c_1=\mathbf q_1^\top\mathbf x
=
\frac{6}{\sqrt2}
=
3\sqrt2
\]

and

\[
c_2=\mathbf q_2^\top\mathbf x
=
\frac{2}{\sqrt2}
=
\sqrt2
\]

The coordinate vector is therefore

\[
\begin{bmatrix}3\sqrt2\\\sqrt2\end{bmatrix}
\]

</details>

### 3. Subspace projection

Project

\[
\mathbf y=
\begin{bmatrix}3\\1\\5\end{bmatrix}
\]

onto the subspace $V$ spanned by the two vectors in Exercise 1, and find the residual.

<details>
<summary>Show solution</summary>

$V$ is the plane $z=0$. Inner products give

\[
\mathbf q_1^\top\mathbf y=2\sqrt2,
\qquad
\mathbf q_2^\top\mathbf y=\sqrt2
\]

Therefore,

\[
\operatorname{proj}_V(\mathbf y)
=
2\sqrt2\mathbf q_1+\sqrt2\mathbf q_2
=
\begin{bmatrix}3\\1\\0\end{bmatrix}
\]

and the residual is

\[
\begin{bmatrix}0\\0\\5\end{bmatrix}
\]

</details>

### 4. A projection matrix

Find the orthogonal projection matrix $\mathbf P=\mathbf q\mathbf q^\top$ onto the line spanned by

\[
\mathbf q=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\1\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

\[
\mathbf P
=
\frac12
\begin{bmatrix}1\\1\end{bmatrix}
\begin{bmatrix}1&1\end{bmatrix}
=
\frac12
\begin{bmatrix}
1&1\\
1&1
\end{bmatrix}
\]

It is symmetric, and direct multiplication verifies $\mathbf P^2=\mathbf P$.

</details>

### 5. The closest vector

For

\[
V=\operatorname{span}
\left\{
\begin{bmatrix}1\\0\end{bmatrix}
\right\},
\qquad
\mathbf x=
\begin{bmatrix}2\\3\end{bmatrix}
\]

find the closest vector in $V$ to $\mathbf x$ and the squared distance.

<details>
<summary>Show solution</summary>

$V$ is the $x$ axis, so the orthogonal projection is

\[
\widehat{\mathbf x}
=
\begin{bmatrix}2\\0\end{bmatrix}
\]

The residual is $\begin{bmatrix}0\\3\end{bmatrix}$, and the squared distance is

\[
\|\mathbf x-\widehat{\mathbf x}\|_2^2=9
\]

</details>

### 6. The orthogonality condition for least squares

Suppose $\widehat{\mathbf c}$ solves

\[
\min_{\mathbf c}
\|\mathbf A\mathbf c-\mathbf b\|_2^2
\]

Write the orthogonality condition satisfied by the residual $\mathbf r=\mathbf b-\mathbf A\widehat{\mathbf c}$ and the normal equations.

<details>
<summary>Show solution</summary>

The optimal approximation $\mathbf A\widehat{\mathbf c}$ is the orthogonal projection of $\mathbf b$ onto $\operatorname{im}(\mathbf A)$. The residual is orthogonal to every column of $\mathbf A$, so

\[
\mathbf A^\top\mathbf r=\mathbf 0
\]

Substituting $\mathbf r=\mathbf b-\mathbf A\widehat{\mathbf c}$ gives

\[
\mathbf A^\top\mathbf A\widehat{\mathbf c}
=
\mathbf A^\top\mathbf b
\]

</details>

### 7. Interpreting a representation subspace

Projecting activation $\mathbf h$ onto a subspace $V$ gives

\[
\frac{\|\operatorname{proj}_V(\mathbf h)\|_2^2}
{\|\mathbf h\|_2^2}
=
0.9
\]

State what this value directly supports and what requires further experiments.

<details>
<summary>Show solution</summary>

Under the chosen Euclidean inner product, 90% of the squared norm of $\mathbf h$ lies in its component along $V$. This is a geometric fact.

The value alone does not establish whether $V$ stably represents a human-labeled concept, whether the ratio persists on other data, or whether the model uses this component for prediction. Data comparisons, basis-stability checks, and interventions are needed.

</details>

## Lesson summary

- An orthogonal basis has mutually orthogonal vectors; an orthonormal basis also gives each vector norm 1.
- Orthonormal-basis coordinates are inner products with the basis vectors.
- $\mathbf Q\mathbf Q^\top\mathbf x$ projects $\mathbf x$ orthogonally onto $\operatorname{im}(\mathbf Q)$.
- The residual is orthogonal to the subspace, and the projection is the closest vector.
- Gram-Schmidt preserves the span of an independent basis and constructs an orthonormal one.
- A least-squares solution is connected to projection of the target onto the matrix's column space.

## Pass criteria

You pass if you can answer these questions without consulting the material.

- Can you distinguish orthogonal and orthonormal bases?
- Can you compute orthonormal-basis coordinates using inner products?
- Can you compute a subspace projection and its residual?
- Can you verify symmetry and idempotence of a projection matrix?
- Can you apply Gram-Schmidt to two vectors?
- Can you explain least squares as projection onto a column space?

## Next lesson

- [M02-10 A minimal understanding of determinants](M02-10-determinant-minimum.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Orthogonality and orthonormality are distinguished.
- [x] Orthonormal-basis coordinates and subspace projections are computed.
- [x] The closest-vector property is explained using an orthogonal residual.
- [x] Gram-Schmidt and its connection to least squares are included.
- [x] Every exercise has a solution.
- [x] Projection size is distinguished from claims of functional use.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
