---
id: "M02-13"
title: "Singular value decomposition"
part: 1
stage: "M02"
status: "complete"
prerequisites:
  - "M02-08"
  - "M02-09"
  - "M02-12"
estimated_time: "120~145 minutes"
---

# M02-13. Singular value decomposition

## Why this lesson matters

Eigendecomposition applies to square matrices mapping a space to itself. Neural-network weight and activation matrices are often rectangular. Singular value decomposition (SVD) decomposes any real matrix into orthogonal input directions, directional amplification factors, and orthogonal output directions.

The same SVD reveals rank, maximum directional amplification, and optimal low-rank approximations. Representation analysis uses it to find major activation subspaces or investigate low-rank weight structure.

## Learning objectives

By the end of this lesson, you should be able to:

- Read the matrix shapes in full and compact SVD.
- Explain the roles of right singular vectors, singular values, and left singular vectors.
- Compute the relation between $\mathbf A^\top\mathbf A$ and singular values.
- Obtain rank and two matrix norms from singular values.
- Construct a low-rank approximation of a small matrix using truncated SVD.
- Distinguish low-rank structure from human-interpretable features or causal use.

## Prerequisite check

- Prerequisite lesson: [M02-08 Kernel, image, and rank](M02-08-kernel-image-rank.md)
- Prerequisite lesson: [M02-09 Orthogonal bases and orthogonal projection](M02-09-orthogonal-basis-projection.md)
- Prerequisite lesson: [M02-12 Symmetric matrices and the spectral theorem](M02-12-symmetric-matrices-spectral-theorem.md)
- Check question: Can you explain rank and orthonormal bases?
- Check question: Can you interpret eigenvalues and eigenvectors of a symmetric PSD matrix?

Review the prerequisite lessons first if rank, orthonormal bases, or the spectral theorem is unclear.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and conditions |
|---|---|---|---|
| $\mathbf A=\mathbf U\boldsymbol\Sigma\mathbf V^\top$ | `A equals U sigma V transpose` | A full SVD of $\mathbf A$ | $\mathbf A\in\mathbb R^{m\times n}$ |
| $\mathbf v_i$ | `v sub i` | The $i$th right singular vector | A unit vector in the input space $\mathbb R^n$ |
| $\sigma_i$ | `sigma sub i` | The $i$th singular value | $\sigma_1\ge\cdots\ge0$ |
| $\mathbf u_i$ | `u sub i` | The $i$th left singular vector | A unit vector in the output space $\mathbb R^m$ |
| $\mathbf A_k$ | `A sub k` | A rank-$k$ approximation using the leading $k$ singular components | $k\le\operatorname{rank}(\mathbf A)$ |
| $\|\mathbf A\|_2$ | `the L two norm of A` | The largest directional amplification factor | Spectral norm |
| $\|\mathbf A\|_F$ | `the Frobenius norm of A` | The square root of the sum of squared entries | Frobenius norm |

## Core concept 1. Full SVD factors a matrix into three matrices

For

\[
\mathbf A\in\mathbb R^{m\times n}
\]

a full SVD is

\[
\mathbf A
=
\mathbf U\boldsymbol\Sigma\mathbf V^\top
\]

The shapes are

\[
\mathbf U\in\mathbb R^{m\times m},
\qquad
\boldsymbol\Sigma\in\mathbb R^{m\times n},
\qquad
\mathbf V\in\mathbb R^{n\times n}
\]

$\mathbf U$ and $\mathbf V$ are orthogonal matrices:

\[
\mathbf U^\top\mathbf U=\mathbf I_m,
\qquad
\mathbf V^\top\mathbf V=\mathbf I_n
\]

$\boldsymbol\Sigma$ is a rectangular diagonal matrix with singular values on the main diagonal and 0 elsewhere. There are $\min(m,n)$ diagonal positions, so this many singular values can be listed, including 0 values. The product of the three factors has shapes $(m\times m)(m\times n)(n\times n)$ and reproduces the original $m\times n$ matrix. Separate input and output bases allow the factorization even when the dimensions differ.

The figure below shows the $3\times2$ matrix in Example 1 sending two input directions to a plane within three output coordinates. Distinguish the 3-dimensional output space from the actual image of dimension 2.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two input basis directions mapped into a rank two plane in three dimensional output space by a rectangular SVD](../../figures/assets/M02/M02-13-rectangular-singular-map.svg)

<figcaption>Input e₁ maps to 3u₁, and e₂ maps to u₂; every output's third component is 0. Compact SVD removes unused output-basis columns while preserving the original transformation exactly.</figcaption>
</figure>

## Core concept 2. SVD changes input coordinates, scales axes, and changes output coordinates

Reading

\[
\mathbf A\mathbf x
=
\mathbf U\boldsymbol\Sigma\mathbf V^\top\mathbf x
\]

from right to left gives these computations.

1. $\mathbf V^\top\mathbf x$: express the input in the right-singular-vector basis.
2. $\boldsymbol\Sigma$: multiply each coordinate by its singular value and change dimension if needed.
3. $\mathbf U$: map to the left-singular-vector directions in the output.

For a positive singular value,

\[
\mathbf A\mathbf v_i=\sigma_i\mathbf u_i
\]

A unit input in the $\mathbf v_i$ direction maps to the $\mathbf u_i$ direction with length multiplied by $\sigma_i$.

Since $\mathbf V^\top\mathbf v_i=\mathbf e_i$, this input has only coordinate $i$ equal to 1 in the singular-vector basis. $\boldsymbol\Sigma$ multiplies it by $\sigma_i$, and $\mathbf U$ combines it with the corresponding output basis vector. A general input is a sum of these directional components, so its output is the sum of their outputs.

Dimension changes also occur in $\boldsymbol\Sigma$. If $m<n$, input coordinates beyond the diagonal positions contribute nothing to the output. If $m>n$, output-basis coordinates beyond the diagonal positions are 0. In either case, input components corresponding to singular value 0 disappear from the output. $\mathbf U$ and $\mathbf V^\top$ themselves are length-preserving orthogonal coordinate changes and can include reflections as well as rotations.

### Visual intuition: three stages turn a unit circle into an ellipse

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A unit circle transformed by V transpose Sigma and U into a rotated ellipse](../../figures/assets/M02/M02-13-svd-three-stage.svg)

<figcaption>Vᵀ aligns the input with right-singular-vector coordinates; Σ changes the length along each axis; U places the resulting ellipse along the left singular vectors in output space.</figcaption>
</figure>

Considering all inputs on the unit circle at once clarifies the SVD geometry. $\mathbf V^\top$ leaves the circle's shape unchanged while determining which input direction is read along each singular axis. $\boldsymbol\Sigma$ scales axis $i$ by $\sigma_i$, producing an ellipse with axis lengths $\sigma_i$. Finally, $\mathbf U$ places the ellipse in output space without changing lengths.

A singular value of $0$ means that the corresponding ellipse axis vanishes completely. A very small singular value means input differences in that direction are barely visible in the output. This describes directional amplification by a linear transformation; it does not establish that a leading axis is a semantic feature that a person can name.

## Core concept 3. Singular values come from eigenvalues of symmetric matrices

If

\[
\mathbf A
=
\mathbf U\boldsymbol\Sigma\mathbf V^\top
\]

then

\[
\mathbf A^\top\mathbf A
=
\mathbf V\boldsymbol\Sigma^\top\mathbf U^\top
\mathbf U\boldsymbol\Sigma\mathbf V^\top
=
\mathbf V\boldsymbol\Sigma^\top\boldsymbol\Sigma\mathbf V^\top
\]

Transposition reverses factor order, after which $\mathbf U^\top\mathbf U=\mathbf I_m$ applies. The diagonal of $\boldsymbol\Sigma^\top\boldsymbol\Sigma$ contains squared singular values. Thus each $\mathbf v_i$ corresponding to a diagonal position is an eigenvector of $\mathbf A^\top\mathbf A$, with

\[
\mathbf A^\top\mathbf A\mathbf v_i
=
\sigma_i^2\mathbf v_i
\]

Similarly,

\[
\mathbf A\mathbf A^\top\mathbf u_i
=
\sigma_i^2\mathbf u_i
\]

$\mathbf A^\top\mathbf A$ has shape $n\times n$ and $\mathbf A\mathbf A^\top$ has shape $m\times m$, so they describe input-space and output-space directions, respectively. Their positive eigenvalues are the same $\sigma_i^2$, but different dimensions can give different numbers of eigenvalues equal to 0.

Squared norms show why these matrices are PSD:

\[
\mathbf x^\top\mathbf A^\top\mathbf A\mathbf x
=(\mathbf A\mathbf x)^\top(\mathbf A\mathbf x)
=\|\mathbf A\mathbf x\|_2^2
\ge0
\]

For $\mathbf A\mathbf A^\top$, applying $\mathbf A^\top$ to a vector in output space gives the same conclusion through its squared norm. Both matrices are symmetric as well, so the spectral theorem from M02-12 applies. Square roots of the positive eigenvalues give singular values. Having chosen a right singular vector, set $\mathbf u_i=\mathbf A\mathbf v_i/\sigma_i$ to obtain the corresponding left direction. Since $\|\mathbf A\mathbf v_i\|_2^2=\sigma_i^2$ in the relation above, this vector has length 1. Do not use this division for a singular value of 0.

The figure below applies $\mathbf A$ and then $\mathbf A^\top$ along input singular directions for $\mathbf A=\operatorname{diag}(3,1)$. The first transformation's factor 3 becomes 9 in the composition, but the original matrix factors summarized by the two norms are still 3 and 1.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Singular direction arrows with gains three and one followed by squared gains nine and one under A transpose A](../../figures/assets/M02/M02-13-gram-squared-gains.svg)

<figcaption>Arrow lengths in each row compare amplification along the same singular direction. Eigenvalues of AᵀA are squared amplification factors. The spectral norm summarizes the largest factor, and the Frobenius norm summarizes the sum of squared factors.</figcaption>
</figure>

## Core concept 4. Compact SVD retains only components with singular values other than 0

Let $\operatorname{rank}(\mathbf A)=r$. Keeping only columns corresponding to positive singular values gives

\[
\mathbf A
=
\mathbf U_r\boldsymbol\Sigma_r\mathbf V_r^\top
\]

The shapes are

\[
\mathbf U_r\in\mathbb R^{m\times r},
\qquad
\boldsymbol\Sigma_r\in\mathbb R^{r\times r},
\qquad
\mathbf V_r\in\mathbb R^{n\times r}
\]

Written as a sum, compact SVD is

\[
\mathbf A
=
\sum_{i=1}^{r}
\sigma_i\mathbf u_i\mathbf v_i^\top
\]

Applying each term to an input gives

\[
(\sigma_i\mathbf u_i\mathbf v_i^\top)\mathbf x
=\sigma_i\mathbf u_i(\mathbf v_i^\top\mathbf x)
\]

It reads one input directional coefficient and sends it along one output direction, so each positive singular component has rank 1. The matrix image is spanned by these $r$ vectors $\mathbf u_i$, and each orthogonal direction can be produced by input $\mathbf v_i$. Hence the number of positive singular values is the rank.

A term with singular value 0 contributes nothing for any input. Compact SVD removes such terms and is an exact representation, not an approximation. Although some entries have been omitted, the three-factor product is still $m\times n$. The zero matrix has no positive singular components, and its sum is the zero matrix.

## Core concept 5. Singular values describe matrix size and amplification

Let the input's singular-basis coordinates be $\mathbf c=\mathbf V^\top\mathbf x$. Orthogonal transformations preserve norms, so a unit input has $\sum_{i=1}^{n}c_i^2=1$. The output is a sum along mutually orthogonal $\mathbf u_i$, giving

\[
\|\mathbf A\mathbf x\|_2^2
=\sum_{i=1}^{r}\sigma_i^2c_i^2
\le\sigma_1^2\sum_{i=1}^{n}c_i^2
=\sigma_1^2
\]

Choosing $\mathbf x=\mathbf v_1$ retains only the largest-amplification term and attains equality. For the zero matrix, every input produces an output norm of 0. Thus the largest singular value is the greatest length factor applied to a unit vector:

\[
\|\mathbf A\|_2
=
\max_{\|\mathbf x\|_2=1}
\|\mathbf A\mathbf x\|_2
=
\sigma_1
\]

The Frobenius norm is the square root of the sum of squared singular values:

\[
\|\mathbf A\|_F
=
\sqrt{\sum_{i,j}a_{ij}^2}
=
\sqrt{\sum_{i=1}^{r}\sigma_i^2}
\]

Left multiplication by an orthogonal matrix preserves each column norm; right multiplication preserves each row norm. Either way, the sum of all squared entries stays the same. Thus $\mathbf U$ and $\mathbf V^\top$ in SVD do not change the Frobenius norm; only the squares of the diagonal entries of $\boldsymbol\Sigma$ other than 0 need to be summed.

The two norms answer different questions. The spectral norm summarizes maximum directional amplification, whereas the Frobenius norm summarizes the squared size of all matrix entries.

## Core concept 6. Truncated SVD gives an optimal low-rank approximation

Order the singular values from largest to smallest and retain only the leading $k$ components:

\[
\mathbf A_k
=
\sum_{i=1}^{k}
\sigma_i\mathbf u_i\mathbf v_i^\top
\]

If $1\le k\le r$, there are $k$ positive components, so $\mathbf A_k$ has rank $k$. Unlike compact SVD, this discards positive components; for $k<r$, it is an approximation different from the original matrix.

The Eckart-Young theorem states that $\mathbf A_k$ is closest to $\mathbf A$ in the spectral or Frobenius norm among all matrices of rank at most $k$. The residual $\mathbf A-\mathbf A_k$ contains only discarded singular components. Applying the two norm formulas above to the residual gives

\[
\|\mathbf A-\mathbf A_k\|_2
=
\sigma_{k+1}
\]

\[
\|\mathbf A-\mathbf A_k\|_F^2
=
\sum_{i=k+1}^{r}\sigma_i^2
\]

When $k=r$, all positive components are retained and the residual is 0. In that case, set $\sigma_{r+1}$ in the spectral-error formula to 0 to indicate that no positive singular value remains. Optimality here concerns error in the specified matrix norms; it does not mean optimal performance on an arbitrary task.

The figure below compares two rank-1 components reading the input $(1,2)^\top$ and summing their outputs with the result after discarding the second component. The norm of the discarded matrix differs from the residual length for a particular input.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two rank one singular components produce perpendicular output vectors and rank one truncation removes the second component](../../figures/assets/M02/M02-13-singular-components-truncation.svg)

<figcaption>Each component reads one input coefficient and sends it along one output direction. Retaining only the first removes (0,2) from the output (3,2). Its length 2 is the discarded singular value 1 multiplied by this input's second coefficient 2.</figcaption>
</figure>

## Core concept 7. Singular-vector signs and repeated singular values have freedom

In

\[
\sigma_i\mathbf u_i\mathbf v_i^\top
\]

changing both $\mathbf u_i$ and $\mathbf v_i$ signs leaves the matrix unchanged. Singular-vector signs therefore have no fixed meaning by themselves.

For a repeated positive singular value, changing the orthonormal bases of the corresponding input and output subspaces by the same orthogonal transformation also gives an SVD. Collect these columns into $\mathbf U_*$ and $\mathbf V_*$, and denote the common singular value by $\sigma$. This part is $\sigma\mathbf U_*\mathbf V_*^\top$. Changing both bases using an orthogonal matrix $\mathbf R$ of the same size gives

\[
\sigma(\mathbf U_*\mathbf R)(\mathbf V_*\mathbf R)^\top
=\sigma\mathbf U_*\mathbf R\mathbf R^\top\mathbf V_*^\top
=\sigma\mathbf U_*\mathbf V_*^\top
\]

The input–output correspondence changes together; directions are not chosen independently at will. If truncation cuts within repeated singular values, different retained directions can give the same optimal error. Interpreting individual singular vectors as features requires checking stability across seeds, samples, and repeated singular values.

The figure below shows that changing input and output singular bases together for $\mathbf A=2\mathbf I_2$ leaves the output of the same input unchanged. Dashed arrows are outputs of the selected singular directions; the solid arrow is the output of the fixed comparison input $(1,0)^\top$.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Paired singular bases rotate together for twice the identity while the same input still maps to the same output](../../figures/assets/M02/M02-13-paired-basis-freedom.svg)

<figcaption>Basis directions can change within a repeated-singular-value subspace. The directions used in the factorization change, but the matrix and the output of a fixed input do not.</figcaption>
</figure>

## Example 1. SVD of a rectangular diagonal matrix

Let

\[
\mathbf A=
\begin{bmatrix}
3&0\\
0&1\\
0&0
\end{bmatrix}
\in\mathbb R^{3\times2}
\]

One full SVD is

\[
\mathbf U=\mathbf I_3,
\qquad
\boldsymbol\Sigma=
\begin{bmatrix}
3&0\\
0&1\\
0&0
\end{bmatrix},
\qquad
\mathbf V=\mathbf I_2
\]

The singular values are $\sigma_1=3$, $\sigma_2=1$, and the rank is 2.

The first input coordinate direction maps to the first output coordinate direction with factor 3, and the second maps to the second with factor 1.

## Example 2. Checking singular values through $\mathbf A^\top\mathbf A$

In Example 1,

\[
\mathbf A^\top\mathbf A
=
\begin{bmatrix}
9&0\\
0&1
\end{bmatrix}
\]

Its eigenvalues are 9 and 1, with positive square roots 3 and 1. The right singular vectors are the standard basis vectors $\mathbf e_1,\mathbf e_2$.

## Example 3. A rank-1 approximation

Retaining only the largest singular component in Example 1 gives

\[
\mathbf A_1
=
3
\begin{bmatrix}1\\0\\0\end{bmatrix}
\begin{bmatrix}1&0\end{bmatrix}
=
\begin{bmatrix}
3&0\\
0&0\\
0&0
\end{bmatrix}
\]

Then

\[
\|\mathbf A-\mathbf A_1\|_2=1,
\qquad
\|\mathbf A-\mathbf A_1\|_F=1
\]

Only one singular value, 1, was discarded, so the two errors agree.

## Example 4. A low-rank approximation of an activation matrix

Apply SVD to centered activations from $N$ samples stored in rows:

\[
\mathbf H_c\in\mathbb R^{N\times d}
\]

The leading $k$ right singular vectors span the major variation subspace in feature space. $\mathbf H_{c,k}$ is the closest rank-$k$ activation matrix in the Frobenius norm.

A low reconstruction error shows that sample variation can be approximated by a small number of linear directions. Whether each direction represents a concept or is used by the model for prediction requires separate verification.

## Common misconceptions

### Misconception 1. SVD applies only to square matrices

SVD exists for every real matrix, including rectangular ones.

### Misconception 2. Singular values are eigenvalues

Singular values are at least 0 and are square roots of the eigenvalues of $\mathbf A^\top\mathbf A$. A general square matrix's eigenvalues can be negative or complex.

### Misconception 3. Right and left singular vectors belong to the same space

$\mathbf v_i$ lies in input space $\mathbb R^n$, and $\mathbf u_i$ in output space $\mathbb R^m$. For rectangular matrices, even the dimensions differ.

### Misconception 4. One leading singular vector is one semantic feature

SVD selects orthogonal directions according to variance and matrix norms. Semantic interpretation, basis stability, and functional use need separate evidence.

## Exercises

### 1. Full SVD shapes

Give the shapes of $\mathbf U$, $\boldsymbol\Sigma$, and $\mathbf V$ in a full SVD of

\[
\mathbf A\in\mathbb R^{5\times3}
\]

<details>
<summary>Show solution</summary>

\[
\mathbf U\in\mathbb R^{5\times5},
\qquad
\boldsymbol\Sigma\in\mathbb R^{5\times3},
\qquad
\mathbf V\in\mathbb R^{3\times3}
\]

The product $\mathbf U\boldsymbol\Sigma\mathbf V^\top$ has shape $5\times3$.

</details>

### 2. Compact SVD shapes

If $\mathbf A$ in Exercise 1 has rank 2, give the shapes of its three compact SVD factors.

<details>
<summary>Show solution</summary>

\[
\mathbf U_2\in\mathbb R^{5\times2},
\qquad
\boldsymbol\Sigma_2\in\mathbb R^{2\times2},
\qquad
\mathbf V_2\in\mathbb R^{3\times2}
\]

$\mathbf U_2\boldsymbol\Sigma_2\mathbf V_2^\top$ has shape $5\times3$.

</details>

### 3. Directional transformation

Suppose $\sigma_i=4$ and $\mathbf A\mathbf v_i=\sigma_i\mathbf u_i$. Find the output for input $-3\mathbf v_i$.

<details>
<summary>Show solution</summary>

Linearity gives

\[
\mathbf A(-3\mathbf v_i)
=
-3\mathbf A\mathbf v_i
=
-12\mathbf u_i
\]

The input has 3 times the length in the direction opposite to $\mathbf v_i$; the output has 12 times the length in the direction opposite to $\mathbf u_i$.

</details>

### 4. Rank and norms

Find the rank, spectral norm, and Frobenius norm of a matrix with singular values

\[
5,\ 2,\ 0,\ 0
\]

<details>
<summary>Show solution</summary>

There are two positive singular values, so the rank is 2.

\[
\|\mathbf A\|_2=5
\]

and

\[
\|\mathbf A\|_F
=
\sqrt{5^2+2^2}
=
\sqrt{29}
\]

</details>

### 5. Truncated SVD errors

A matrix with singular values

\[
8,\ 3,\ 1
\]

is approximated at rank 1. Find the spectral and Frobenius norm errors.

<details>
<summary>Show solution</summary>

The rank-1 approximation retains the first component and discards 3 and 1.

\[
\|\mathbf A-\mathbf A_1\|_2=3
\]

and

\[
\|\mathbf A-\mathbf A_1\|_F
=
\sqrt{3^2+1^2}
=
\sqrt{10}
\]

</details>

### 6. Sign freedom

For a rank-1 matrix

\[
\mathbf A
=
\sigma\mathbf u\mathbf v^\top
\]

show that negating both $\mathbf u$ and $\mathbf v$ leaves $\mathbf A$ unchanged.

<details>
<summary>Show solution</summary>

\[
\sigma(-\mathbf u)(-\mathbf v)^\top
=
\sigma(-\mathbf u)(-\mathbf v^\top)
=
\sigma\mathbf u\mathbf v^\top
\]

The two negative signs cancel. Singular-vector signs are therefore not uniquely determined.

</details>

### 7. The scope of low-rank interpretation

The leading 10 singular components of a centered activation matrix account for 95% of its squared Frobenius norm. Explain:

1. The approximation property directly supported.
2. Conditions to check in the data and computation.
3. Feature claims not supported by this result alone.

<details>
<summary>Show solution</summary>

The sampled activation matrix can be approximated by a rank-10 matrix using the leading 10 components while preserving 95% of its squared Frobenius norm.

Check sample selection, centering, token and layer, singular-value gaps, and subspace stability across seeds.

The result alone does not establish that the 10 directions are each one human-interpretable concept, that the model uses them for behavior, or that they generalize to other data.

</details>

## Lesson summary

- SVD decomposes any real matrix into an orthogonal input basis, singular values, and an orthogonal output basis.
- $\mathbf A\mathbf v_i=\sigma_i\mathbf u_i$ describes amplification along an input singular direction.
- Squared singular values are eigenvalues of $\mathbf A^\top\mathbf A$ and $\mathbf A\mathbf A^\top$.
- The number of positive singular values is the rank; the largest is the spectral norm.
- Truncated SVD gives optimal low-rank approximations in the spectral and Frobenius norms.
- Singular-vector signs and repeated-singular-value subspaces are nonunique; meaning and function require separate verification.

## Pass criteria

You pass if you can answer these questions without consulting the material.

- Can you give full and compact SVD shapes?
- Can you explain the three factors through input directions, scaling, and output directions?
- Can you explain the relation between singular values and eigenvalues of $\mathbf A^\top\mathbf A$?
- Can you compute rank and matrix norms from singular values?
- Can you compute a truncated SVD approximation and its errors?
- Can you distinguish low-rank structure from feature meaning and function?

## Next lesson

- [M02-14 Covariance and PCA](M02-14-covariance-pca.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Full and compact SVD shapes are specified.
- [x] Input directions, amplification factors, and output directions are distinguished.
- [x] The relation to symmetric-matrix eigenvalues is explained.
- [x] Rank, norms, and low-rank approximations are connected.
- [x] Every exercise has a solution.
- [x] Low-rank structure is distinguished from claims about meaning and function.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
