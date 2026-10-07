---
id: "M02-12"
title: "Symmetric matrices and the spectral theorem"
part: 1
stage: "M02"
status: "complete"
prerequisites:
  - "M02-09"
  - "M02-11"
estimated_time: "105~130 minutes"
---

# M02-12. Symmetric matrices and the spectral theorem

## Why this lesson matters

A real symmetric matrix has only real eigenvalues and admits a basis of mutually orthogonal eigenvectors. This removes the problems of complex eigenvalues, insufficient eigenvectors, and nonorthogonal eigenbases that can occur for general square matrices.

Covariance matrices and Hessians of differentiable scalar functions are often symmetric. The spectral theorem decomposes these matrices into scalar scaling factors along orthogonal directions, letting us read quadratic form signs and curvature from eigenvalues.

## Learning objectives

After completing this lesson, you will be able to:

- Determine real symmetry from a transpose condition.
- Explain why eigenvectors for distinct eigenvalues are orthogonal.
- Read the shapes and roles in spectral decomposition $\mathbf A=\mathbf Q\boldsymbol\Lambda\mathbf Q^\top$.
- Calculate vector transformations and quadratic forms in an orthonormal eigenbasis.
- Determine positive semidefiniteness from eigenvalues.
- Distinguish a symmetric matrix's spectrum from claims about model interpretation.

## Prerequisite check

- Prerequisite lesson: [M02-09 Orthogonal bases and projection](M02-09-orthogonal-basis-projection.md)
- Prerequisite lesson: [M02-11 Eigenvalues and eigenvectors](M02-11-eigenvalues-eigenvectors.md)
- Check question: Can you explain condition $\mathbf Q^\top\mathbf Q=\mathbf I$ for a matrix with orthonormal columns?
- Check question: Can you define eigenvalues, eigenspaces, and diagonalization?

If orthonormal bases or eigendecomposition are unclear, first review the prerequisite lessons.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| $\mathbf A=\mathbf A^\top$ | `A equals A transpose` | Real symmetric matrix condition | $\mathbf A\in\mathbb R^{n\times n}$ |
| $\mathbf Q$ | `Q` | Matrix with orthonormal eigenvectors as columns | $\mathbf Q^\top\mathbf Q=\mathbf Q\mathbf Q^\top=\mathbf I_n$ |
| $\boldsymbol\Lambda$ | `capital lambda` | Matrix with eigenvalues on the diagonal | $\boldsymbol\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)$ |
| $\mathbf x^\top\mathbf A\mathbf x$ | `x transpose A x` | Quadratic form of $\mathbf A$ | Scalar result |
| Positive semidefinite | `positive semidefinite` | Every quadratic form value is nonnegative. | $\mathbf x^\top\mathbf A\mathbf x\ge0$ |

## Core concept 1. Symmetric entries match across the main diagonal

A real square matrix $\mathbf A$ is symmetric if

\[
\mathbf A^\top=\mathbf A
\]

In terms of entries,

\[
a_{ij}=a_{ji}
\]

The matrix

\[
\begin{bmatrix}
2&-1&4\\
-1&3&0\\
4&0&5
\end{bmatrix}
\]

is symmetric. Reflecting entries above the main diagonal gives those below it.

The figure below pairs the entries selected by exchanging row and column indices. Symmetry requires matching values at corresponding positions, regardless of their magnitudes or signs.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A symmetric three-by-three matrix with matching off-diagonal entry pairs highlighted by their swapped row and column indices](../../figures/assets/M02/M02-12-mirrored-matrix-entries.svg)

<figcaption>Row 1, column 2 and row 2, column 1 both contain −1. Other off-diagonal entries match in the same way. Transposition exchanges these positions but leaves their values, and therefore the whole matrix, unchanged.</figcaption>
</figure>

## Core concept 2. Symmetric matrices have real eigenvalues

All eigenvalues of a real symmetric matrix are real, even when complex numbers are considered. The absence of real eigenvalues seen in M02-11's $90^\circ$ rotation matrix cannot occur for symmetric matrices.

This lesson focuses on the theorem's result and conditions rather than its full proof. Check $\mathbf A=\mathbf A^\top$ before using this conclusion.

## Core concept 3. Eigenvectors for distinct eigenvalues are orthogonal

Suppose

\[
\mathbf A\mathbf u=\lambda\mathbf u,
\qquad
\mathbf A\mathbf v=\mu\mathbf v
\]

and $\lambda\ne\mu$. Symmetry gives

\[
\mathbf u^\top\mathbf A\mathbf v
=
(\mathbf A^\top\mathbf u)^\top\mathbf v
=
(\mathbf A\mathbf u)^\top\mathbf v
\]

The transpose rule for matrix products gives the first equality, and $\mathbf A^\top=\mathbf A$ gives the second. Substituting the eigenvalue equations for $\mathbf A\mathbf v$ on the left and $\mathbf A\mathbf u$ on the right gives

\[
\mu\mathbf u^\top\mathbf v
=
\lambda\mathbf u^\top\mathbf v
\]

Thus,

\[
(\mu-\lambda)\mathbf u^\top\mathbf v=0
\]

Since $\mu-\lambda\ne0$,

\[
\mathbf u^\top\mathbf v=0
\]

If the eigenvalues are equal, $\mu-\lambda=0$, so this argument does not establish orthogonality. Vectors within one eigenspace are not automatically all orthogonal. However, applying Gram-Schmidt to a basis of that space selects an orthonormal basis. The process combines vectors for the same eigenvalue linearly, so the results stay in that eigenspace.

The figure below draws the orthogonal directions for Example 1's two distinct eigenvalues. Read the right angle between eigendirections separately from the scaling along each direction.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Perpendicular normalized eigenvectors of a symmetric matrix, with eigenvalue three stretching one and eigenvalue one preserving the other](../../figures/assets/M02/M02-12-orthogonal-eigenvectors.svg)

<figcaption>The first eigendirection stretches by 3, and the second stays unchanged, while the directions are orthogonal. This does not mean every pair of vectors within a repeated eigenvalue's space is orthogonal; an orthonormal basis is chosen within it.</figcaption>
</figure>

## Core concept 4. The spectral theorem guarantees an orthonormal eigenbasis

A real symmetric matrix $\mathbf A\in\mathbb R^{n\times n}$ has orthonormal eigenvectors

\[
\mathbf q_1,\ldots,\mathbf q_n
\]

Collecting them as columns gives

\[
\mathbf Q=
\begin{bmatrix}
\mathbf q_1&\cdots&\mathbf q_n
\end{bmatrix}
\]

with

\[
\mathbf Q^\top\mathbf Q=\mathbf I_n
\]

Placing the corresponding eigenvalues in diagonal matrix $\boldsymbol\Lambda$ gives

\[
\mathbf A
=
\mathbf Q\boldsymbol\Lambda\mathbf Q^\top
\]

This is the spectral decomposition of a real symmetric matrix.

The transpose $\mathbf Q^\top$ replaces $\mathbf V^{-1}$ from general diagonalization. Here, the square matrix has $n$ orthonormal columns, so both $\mathbf Q^\top\mathbf Q=\mathbf I_n$ and $\mathbf Q\mathbf Q^\top=\mathbf I_n$ hold. Its inverse is therefore its transpose. Unlike M02-09's subspace basis with $k<n$ columns, this basis reads and reconstructs all coordinates of the entire space.

## Core concept 5. Transformation separates into orthogonal coordinate changes and axiswise scaling

Reading

\[
\mathbf A\mathbf x
=
\mathbf Q\boldsymbol\Lambda\mathbf Q^\top\mathbf x
\]

from right to left gives these calculations:

1. $\mathbf Q^\top\mathbf x$: obtain eigenbasis coordinates.
2. $\boldsymbol\Lambda$: multiply each eigendirection component by $\lambda_i$.
3. $\mathbf Q$: return to the original standard coordinates.

The first and last stages read and reconstruct coordinates and are inverses of each other. Applying only these two gives $\mathbf Q\mathbf Q^\top\mathbf x=\mathbf x$. The middle eigenvalue scaling supplies the actual transformation effect.

In orthogonal coordinates, a symmetric matrix scales components without mixing directions. Orthogonal coordinate changes preserve lengths and angles but can include reflections as well as rotations. Calling the three stages only rotation, scaling, and inverse rotation is therefore not generally accurate. The example's eigenbasis is used after checking orthonormality; its determinant need not be positive.

The figure below tracks Example 2's spectral decomposition using coordinate values and norms. Reading and reconstructing eigenbasis coordinates leave the norm unchanged; only the middle scaling creates the transformation effect.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Four spectral-decomposition coordinate plots with equal norms before and after the eigenvalue-scaling stage](../../figures/assets/M02/M02-12-spectral-coordinate-stages.svg)

<figcaption>Standard coordinates (2,0) and eigenbasis coordinates (√2,√2) both have norm 2. After eigenvalue scaling, the coefficients and reconstructed output (4,2) both have norm √20. The coordinate changes themselves did not increase length.</figcaption>
</figure>

## Core concept 6. A quadratic form adds contributions from eigendirections

Write

\[
\mathbf x=\mathbf Q\mathbf c
\]

with eigenbasis coordinates $\mathbf c=\mathbf Q^\top\mathbf x$. Then

\[
\mathbf x^\top\mathbf A\mathbf x
=
\mathbf c^\top\mathbf Q^\top
(\mathbf Q\boldsymbol\Lambda\mathbf Q^\top)
\mathbf Q\mathbf c
=
\mathbf c^\top\boldsymbol\Lambda\mathbf c
=
\sum_{i=1}^{n}\lambda_i c_i^2
\]

Replace $\mathbf Q^\top\mathbf Q$ on both sides with the identity to obtain the middle expression. Diagonal matrix $\boldsymbol\Lambda$ has no cross terms multiplying different coordinates, leaving only $c_i^2$ in the final sum.

Each eigenvalue weights the squared component along its eigendirection. If all eigenvalues are nonnegative,

\[
\mathbf x^\top\mathbf A\mathbf x\ge0
\]

holds for every $\mathbf x$, so $\mathbf A$ is positive semidefinite. If eigenvalue $\lambda_j$ is negative, choosing $\mathbf x=\mathbf q_j$ gives $c_j=1$ and all other coordinates 0, making the quadratic form $\lambda_j<0$. A positive result for one vector cannot establish PSD. PSD is a condition on every vector.

The figure below compares how quadratic form signs vary with direction in the eigenbasis coefficient plane. Determine PSD from the condition across all directions, not one positive observation.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Coefficient-plane sign regions for positive definite, semidefinite, and indefinite quadratic forms with zero directions marked](../../figures/assets/M02/M02-12-quadratic-form-signs.svg)

<figcaption>Two positive eigenvalues give a positive value in every nonzero direction. Allowing a zero eigenvalue gives zero along that direction and can still avoid negative values. One negative eigenvalue gives negative values, such as along the vertical direction on the right, so the matrix is not PSD.</figcaption>
</figure>

## Core concept 7. Spectral decomposition calculates matrix functions direction by direction

For an integer $k\ge0$,

\[
\mathbf A^k
=
\mathbf Q\boldsymbol\Lambda^k\mathbf Q^\top
\]

Applying a scalar function, such as the exponential, to eigenvalues can define a matrix function of the form

\[
f(\mathbf A)
=
\mathbf Q f(\boldsymbol\Lambda)\mathbf Q^\top
\]

Here, $f(\boldsymbol\Lambda)$ has diagonal entries $f(\lambda_i)$ and zero elsewhere. The function $f$ must be defined at each eigenvalue for this formula to apply. Distinguish this from applying a scalar function to every matrix entry.

If all eigenvalues are nonzero, the inverse is also

\[
\mathbf A^{-1}
=
\mathbf Q\boldsymbol\Lambda^{-1}\mathbf Q^\top
\]

The diagonal entries of $\boldsymbol\Lambda^{-1}$ are $1/\lambda_i$. Even one zero eigenvalue makes its direction unrecoverable and prevents using this inverse formula.

## Example 1. Eigenpairs of a symmetric matrix

The matrix

\[
\mathbf A=
\begin{bmatrix}
2&1\\
1&2
\end{bmatrix}
\]

has eigenvalues 3 and 1. We can choose corresponding orthonormal eigenvectors

\[
\mathbf q_1=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\1\end{bmatrix},
\qquad
\mathbf q_2=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\-1\end{bmatrix}
\]

They satisfy

\[
\mathbf A\mathbf q_1=3\mathbf q_1,
\qquad
\mathbf A\mathbf q_2=\mathbf q_2
\]

and $\mathbf q_1^\top\mathbf q_2=0$.

## Example 2. Transform using spectral decomposition

In Example 1,

\[
\mathbf Q=
\frac{1}{\sqrt2}
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix},
\qquad
\boldsymbol\Lambda=
\begin{bmatrix}
3&0\\
0&1
\end{bmatrix}
\]

Input

\[
\mathbf x=
\begin{bmatrix}2\\0\end{bmatrix}
\]

has eigenbasis coordinates

\[
\mathbf c=\mathbf Q^\top\mathbf x
=
\begin{bmatrix}\sqrt2\\\sqrt2\end{bmatrix}
\]

Multiplying by the eigenvalues gives

\[
\boldsymbol\Lambda\mathbf c
=
\begin{bmatrix}3\sqrt2\\\sqrt2\end{bmatrix}
\]

Returning to standard coordinates gives

\[
\mathbf A\mathbf x
=
\mathbf Q\boldsymbol\Lambda\mathbf c
=
\begin{bmatrix}4\\2\end{bmatrix}
\]

## Example 3. Determine PSD

The matrix

\[
\mathbf B=
\begin{bmatrix}
2&-2\\
-2&2
\end{bmatrix}
\]

has eigenvalues 4 and 0. Both are nonnegative, so $\mathbf B$ is positive semidefinite.

\[
\mathbf x^\top\mathbf B\mathbf x
=
2(x_1-x_2)^2
\ge0
\]

The quadratic form is 0 along direction $\begin{bmatrix}1\\1\end{bmatrix}$, corresponding to eigenvalue 0.

## Example 4. Hessians and covariance matrices

For a twice continuously differentiable scalar function, when the conditions for exchanging mixed partial derivatives hold, the Hessian is symmetric. Eigenvectors are local curvature directions; eigenvalues describe second-order rates of change along them.

Covariance matrices are also symmetric and positive semidefinite. Eigenvectors describe directions of data variation, and eigenvalues relate to variances along those directions. M02-14 calculates these using PCA.

These interpretations describe structure at the given point or in the given data distribution. One large eigenvalue cannot determine feature meaning or causal importance for model behavior.

## Common misconceptions

### Misconception 1. Every square matrix has an orthonormal eigenbasis

The spectral theorem applies to real symmetric matrices. General nonsymmetric matrices may have nonorthogonal eigenvectors or lack an eigenvector basis.

### Misconception 2. A repeated eigenvalue has only one eigenvector

A repeated eigenvalue's eigenspace can have multiple dimensions. For symmetric matrices, an orthonormal basis can be selected within each eigenspace.

### Misconception 3. Every eigenvalue of a PSD matrix is positive

Positive semidefiniteness allows zero eigenvalues. When all eigenvalues are positive, the matrix is positive definite.

### Misconception 4. The largest eigenvalue direction automatically gives the most important model feature

The largest eigenvalue has the greatest algebraic value among directional coefficients. It need not be positive or largest in absolute value. Human interpretability and functional use by the model require further data and intervention evidence.

## Exercises

### 1. Determine symmetry

Select all symmetric matrices.

\[
\mathbf A=
\begin{bmatrix}1&2\\2&3\end{bmatrix},
\qquad
\mathbf B=
\begin{bmatrix}1&0\\4&1\end{bmatrix},
\qquad
\mathbf C=
\begin{bmatrix}5&-1\\-1&0\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

Since $\mathbf A^\top=\mathbf A$ and $\mathbf C^\top=\mathbf C$, both $\mathbf A$ and $\mathbf C$ are symmetric. For $\mathbf B$, $b_{12}=0$ differs from $b_{21}=4$, so it is not symmetric.

</details>

### 2. Orthogonal eigenvectors

For

\[
\mathbf A=
\begin{bmatrix}2&1\\1&2\end{bmatrix}
\]

check that

\[
\mathbf v_1=
\begin{bmatrix}1\\1\end{bmatrix},
\qquad
\mathbf v_2=
\begin{bmatrix}1\\-1\end{bmatrix}
\]

are eigenvectors for distinct eigenvalues and are orthogonal.

<details>
<summary>Show solution</summary>

\[
\mathbf A\mathbf v_1
=
\begin{bmatrix}3\\3\end{bmatrix}
=
3\mathbf v_1
\]

and

\[
\mathbf A\mathbf v_2
=
\begin{bmatrix}1\\-1\end{bmatrix}
=
\mathbf v_2
\]

The eigenvalues, 3 and 1 respectively, are distinct. Since

\[
\mathbf v_1^\top\mathbf v_2=1-1=0
\]

the eigenvectors are orthogonal.

</details>

### 3. Read a spectral decomposition

Suppose

\[
\mathbf A
=
\mathbf Q
\begin{bmatrix}5&0\\0&2\end{bmatrix}
\mathbf Q^\top
\]

and the columns of $\mathbf Q$ are $\mathbf q_1,\mathbf q_2$. Find $\mathbf A\mathbf q_1$ and $\mathbf A\mathbf q_2$.

<details>
<summary>Show solution</summary>

We have $\mathbf Q^\top\mathbf q_1=\mathbf e_1$ and $\mathbf Q^\top\mathbf q_2=\mathbf e_2$. Thus,

\[
\mathbf A\mathbf q_1=5\mathbf q_1,
\qquad
\mathbf A\mathbf q_2=2\mathbf q_2
\]

</details>

### 4. Calculate a quadratic form

Suppose orthonormal eigenbasis coordinates are

\[
\mathbf c=
\begin{bmatrix}2\\-1\end{bmatrix}
\]

and eigenvalues are $\lambda_1=3$ and $\lambda_2=-2$. Find $\mathbf x^\top\mathbf A\mathbf x$ and explain its sign.

<details>
<summary>Show solution</summary>

\[
\mathbf x^\top\mathbf A\mathbf x
=
\lambda_1c_1^2+\lambda_2c_2^2
=
3\cdot4+(-2)\cdot1
=
10
\]

The value is positive for this $\mathbf x$, but $\lambda_2<0$ means the matrix is not PSD. The quadratic form is negative along $\mathbf q_2$.

</details>

### 5. Determine PSD

A real symmetric matrix has eigenvalues $4,1,0$. Determine separately whether it is PSD and whether it is invertible.

<details>
<summary>Show solution</summary>

All eigenvalues are nonnegative, so it is PSD. The zero eigenvalue makes its kernel nontrivial, and there is no inverse.

</details>

### 6. Matrix powers

For

\[
\mathbf A=\mathbf Q
\begin{bmatrix}2&0\\0&-1\end{bmatrix}
\mathbf Q^\top
\]

write $\mathbf A^4$ in spectral decomposition form.

<details>
<summary>Show solution</summary>

\[
\mathbf A^4
=
\mathbf Q
\begin{bmatrix}2^4&0\\0&(-1)^4\end{bmatrix}
\mathbf Q^\top
=
\mathbf Q
\begin{bmatrix}16&0\\0&1\end{bmatrix}
\mathbf Q^\top
\]

</details>

### 7. Critique a spectral claim

Suppose an activation covariance matrix's largest eigenvalue exceeds the others. Distinguish:

1. A directly supported geometric fact
2. Data and preprocessing conditions to check
3. Model-function claims unsupported by this result alone

<details>
<summary>Show solution</summary>

For the given data and inner product, the first eigenvector direction has the largest sample variance.

Check the data sample, centering, feature scales, and outliers, since they can change the result.

One eigenvalue cannot establish whether the high-variance direction represents a human-interpreted concept, whether the model uses it for prediction, or whether it generalizes to other data. Meaning validation and intervention experiments are necessary.

</details>

## Lesson summary

- A real symmetric matrix equals its transpose and has only real eigenvalues.
- Eigenvectors for distinct eigenvalues are orthogonal.
- The spectral theorem guarantees an orthonormal eigenbasis for symmetric matrices.
- The decomposition $\mathbf A=\mathbf Q\boldsymbol\Lambda\mathbf Q^\top$ applies directional scaling in an eigenbasis.
- The quadratic form is $\sum_i\lambda_i c_i^2$, and eigenvalue signs determine PSD.
- A spectrum describes matrix structure; feature meanings and functional use require additional evidence.

## Pass criteria

You pass if you can answer these questions without consulting the material:

- Can you determine symmetry using entries and the transpose condition?
- Can you explain why eigenvectors for distinct eigenvalues are orthogonal?
- Can you read the shapes and roles of the three spectral decomposition matrices?
- Can you calculate transformations and quadratic forms in eigenbasis coordinates?
- Can you determine PSD and invertibility from eigenvalues?
- Can you explain the scope of interpreting a symmetric matrix's spectrum?

## Next lesson

- [M02-13 Singular value decomposition](M02-13-singular-value-decomposition.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Symmetry conditions and the scope of the spectral theorem are stated.
- [x] The key orthogonality calculation is presented.
- [x] Spectral decomposition is connected to quadratic forms.
- [x] PSD is determined from eigenvalues.
- [x] Every exercise has a solution.
- [x] Spectral structure is distinguished from model-function claims.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
