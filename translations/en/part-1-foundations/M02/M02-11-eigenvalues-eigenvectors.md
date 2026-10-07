---
id: "M02-11"
title: "Eigenvalues and eigenvectors"
part: 1
stage: "M02"
status: "complete"
prerequisites:
  - "M02-06"
  - "M02-07"
  - "M02-10"
estimated_time: "110~135 minutes"
---

# M02-11. Eigenvalues and eigenvectors

## Why this lesson matters

A linear transformation mixes vector directions, but certain special directions remain on the same line. Vectors representing those directions are eigenvectors, and their scaling factors are eigenvalues.

Finding eigendirections lets us analyze repeated applications of a matrix, linear dynamics, and curvature matrices direction by direction. Eigenvalues apply to square matrices. We must also consider the limitation that a nonsymmetric matrix may not have enough real eigenvectors.

## Learning objectives

After completing this lesson, you will be able to:

- Define eigenvalues and eigenvectors using $\mathbf A\mathbf v=\lambda\mathbf v$.
- Find eigenvalues of small matrices from the characteristic equation.
- Calculate each eigenvalue's eigenspace as a kernel.
- Interpret an eigenvalue's sign and magnitude as a transformation along its direction.
- Calculate how matrix powers affect eigendirections.
- Explain diagonalization when an eigenvector basis exists and distinguish cases where it fails.

## Prerequisite check

- Prerequisite lesson: [M02-06 Linear systems and inverses](M02-06-linear-systems-inverse.md)
- Prerequisite lesson: [M02-07 Linear independence, bases, and dimension](M02-07-linear-independence-basis-dimension.md)
- Prerequisite lesson: [M02-10 A minimal understanding of determinants](M02-10-determinant-minimum.md)
- Check question: Can you find a kernel basis from a homogeneous system?
- Check question: Can you connect determinant 0 with noninvertibility of a square matrix?

If kernels, bases, or determinants are unclear, first review the prerequisite lessons.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| $\lambda$ | `lambda` | Scaling factor along an eigendirection | Scalar |
| $\mathbf v$ | `v` | Eigenvector corresponding to eigenvalue $\lambda$ | $\mathbf v\ne\mathbf 0$ |
| $\mathbf A\mathbf v=\lambda\mathbf v$ | `A v equals lambda v` | Condition for remaining on the same line after transformation | $\mathbf A$ is square. |
| $\det(\mathbf A-\lambda\mathbf I)=0$ | `the determinant of A minus lambda I equals zero` | Characteristic equation for finding eigenvalues | Equation in $\lambda$ |
| $E_\lambda$ | `E sub lambda` | Space containing eigenvectors for $\lambda$ and the zero vector | $\ker(\mathbf A-\lambda\mathbf I)$ |
| Diagonalization | `diagonalization` | Representing a matrix as diagonal in an eigenvector basis | Requires enough independent eigenvectors. |

## Core concept 1. An eigenvector is a nonzero vector that stays on its line

For a square matrix $\mathbf A\in\mathbb R^{n\times n}$, if

\[
\mathbf A\mathbf v=\lambda\mathbf v,
\qquad
\mathbf v\ne\mathbf 0
\]

then $\mathbf v$ is an eigenvector and $\lambda$ is its corresponding eigenvalue.

If $\lambda>0$, the vector scales by $|\lambda|$ in the same direction. If $\lambda<0$, it reverses direction and scales by $|\lambda|$. If $\lambda=0$, the eigenvector is a kernel direction and maps to zero.

The zero vector satisfies the equation for every $\lambda$, so it is excluded from eigenvectors.

The figure below applies Example 1's matrix to two eigenvectors and one general vector. Even for a negative eigenvalue, the same-line condition holds.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A diagonal matrix stretching the first eigenvector, reversing the second, and changing the line of a general input vector](../../figures/assets/M02/M02-11-eigen-and-general-directions.svg)

<figcaption>Gray dashed arrows are inputs; green arrows are outputs. e₁ scales by 4, and e₂ reverses and scales by 2, but each stays on its own line. Output (4,−2) is not a scalar multiple of input (1,1), so that input is not an eigenvector.</figcaption>
</figure>

## Core concept 2. Find eigenvalues from the characteristic equation

Rearranging

\[
\mathbf A\mathbf v=\lambda\mathbf v
\]

gives

\[
(\mathbf A-\lambda\mathbf I)\mathbf v=\mathbf 0
\]

Writing the right side's $\lambda\mathbf v$ as $\lambda\mathbf I\mathbf v$ allows us to factor out the same vector. In $\mathbf A-\lambda\mathbf I$, only diagonal entries decrease by $\lambda$; off-diagonal entries stay unchanged.

A nonzero solution $\mathbf v$ exists when this matrix's kernel is not $\{\mathbf 0\}$. In M02-10, this was equivalent to singularity, with determinant 0. Thus, find $\lambda$ satisfying

\[
\det(\mathbf A-\lambda\mathbf I)=0
\]

The expression

\[
p_{\mathbf A}(\lambda)
=
\det(\mathbf A-\lambda\mathbf I)
\]

is the characteristic polynomial. The alternative convention $\det(\lambda\mathbf I-\mathbf A)$ has the same roots and also appears in the literature.

## Core concept 3. Find eigenvectors in each eigenvalue's kernel

After finding an eigenvalue $\lambda$, solve

\[
(\mathbf A-\lambda\mathbf I)\mathbf v=\mathbf 0
\]

The space

\[
E_\lambda
=
\ker(\mathbf A-\lambda\mathbf I)
\]

is the eigenspace for $\lambda$. An eigenspace includes zero, while its eigenvectors are the nonzero vectors within it.

Any nonzero scalar multiple of an eigenvector is another eigenvector for the same eigenvalue. The entire eigenspace describes the transformation's directional structure, rather than just one eigenvector's list of numbers.

The figure below draws the kernels obtained by substituting Example 2's eigenvalues in the original input space. Distinguish calculating one eigenvector from finding the eigenspace containing its multiples.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two eigenspace lines computed as kernels for eigenvalues two and three, with zero marked as excluded from eigenvectors](../../figures/assets/M02/M02-11-eigenspaces-as-kernels.svg)

<figcaption>The kernel for eigenvalue 2 is horizontal; the kernel for eigenvalue 3 is diagonal. Nonzero vectors on each line are the corresponding eigenvectors. The origin belongs to both eigenspaces but is excluded from eigenvectors.</figcaption>
</figure>

## Core concept 4. Repeated application raises eigenvalues to powers

If

\[
\mathbf A\mathbf v=\lambda\mathbf v
\]

then

\[
\mathbf A^2\mathbf v
=
\mathbf A(\lambda\mathbf v)
=
\lambda^2\mathbf v
\]

and, generally,

\[
\mathbf A^k\mathbf v
=
\lambda^k\mathbf v
\]

For the second application, linearity moves scalar $\lambda$ outside the matrix, and the remaining $\mathbf A\mathbf v$ is replaced again by $\lambda\mathbf v$. Each application contributes one more factor of $\lambda$.

- If $|\lambda|>1$, the component along this direction grows with repetition.
- If $|\lambda|<1$, that component shrinks.
- If $\lambda<0$, the direction alternates with the application count.

For $|\lambda|=1$, magnitude along the eigendirection is preserved, but other components of a nondiagonalizable matrix can grow. Do not determine all repeated behavior of a general matrix from eigenvalue magnitudes alone.

The figure below compares repeated multiplication by one scaling factor along an eigendirection. Arrow lengths share a scale within each row; starting lengths differ between rows to fit the display.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Four repeated eigenvalue scalings showing growth, shrinkage, and alternating shrinking directions along an eigenline](../../figures/assets/M02/M02-11-eigenvalue-powers.svg)

<figcaption>A positive factor preserves direction while changing magnitude; a negative factor reverses direction at each application. Repeated multiplication gives powers of λ, so track both magnitude and sign.</figcaption>
</figure>

## Core concept 5. An eigenvector basis allows diagonalization

Suppose there are $n$ linearly independent eigenvectors $\mathbf v_1,\ldots,\mathbf v_n$ with corresponding eigenvalues $\lambda_1,\ldots,\lambda_n$. Set

\[
\mathbf V=
\begin{bmatrix}
\mathbf v_1&\cdots&\mathbf v_n
\end{bmatrix},
\qquad
\boldsymbol\Lambda=
\begin{bmatrix}
\lambda_1&&0\\
&\ddots&\\
0&&\lambda_n
\end{bmatrix}
\]

Then

\[
\mathbf A\mathbf V=\mathbf V\boldsymbol\Lambda
\]

The $i$th column on the left is $\mathbf A\mathbf v_i$, and the $i$th column on the right is $\lambda_i\mathbf v_i$, combining all eigenvector equations into one matrix equation. The $n$ independent columns form a basis of $\mathbb R^n$, so $\mathbf V$ is invertible. Multiplying both sides on the right by $\mathbf V^{-1}$ gives

\[
\mathbf A
=
\mathbf V\boldsymbol\Lambda\mathbf V^{-1}
\]

This is diagonalization.

Writing input $\mathbf x$ as $\mathbf x=\mathbf V\mathbf c$ gives eigenbasis coordinates $\mathbf c=\mathbf V^{-1}\mathbf x$. Since $\mathbf A\mathbf x=\mathbf V\boldsymbol\Lambda\mathbf c$, multiply each coordinate only by its eigenvalue, then use $\mathbf V$ to return to the original coordinates.

Applying the transformation twice cancels the intermediate $\mathbf V^{-1}\mathbf V$ to the identity. Repeating this gives the power formula

\[
\mathbf A^k
=
\mathbf V\boldsymbol\Lambda^k\mathbf V^{-1}
\]

With $n$ distinct real eigenvalues, we obtain $n$ independent eigenvectors. For two eigenvalues $\lambda_1\ne\lambda_2$, suppose $c_1\mathbf v_1+c_2\mathbf v_2=\mathbf 0$. Apply $\mathbf A$, then subtract $\lambda_2$ times the original equation to get

\[
c_1(\lambda_1-\lambda_2)\mathbf v_1=\mathbf 0
\]

Both the eigenvalue difference and $\mathbf v_1$ are nonzero, so $c_1=0$, and the original equation gives $c_2=0$. For more vectors, repeated application of $\mathbf A$ and subtraction of an eigenvalue multiple of the equation separates coefficients one by one. Repeated eigenvalues make the difference 0, so their eigenspaces must be checked separately for independent eigenvector counts.

The figure below expresses Example 3's input in Example 2's eigenbasis and transforms it once. The two middle panels use eigenbasis coefficients as axes; the first and last use standard coordinates.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Four coordinate stages converting a vector to eigenbasis coefficients, scaling them by eigenvalues, and reconstructing the output](../../figures/assets/M02/M02-11-diagonalization-coordinates.svg)

<figcaption>Input (3,1) has eigenbasis coefficients (2,1). Multiplying them by eigenvalues (2,3) gives coefficients (4,3), which reconstruct output (7,3) using the original eigenvectors. Coordinate conversion itself is not an extra movement of the physical vector.</figcaption>
</figure>

## Core concept 6. Not every square matrix is diagonalizable over the reals

The matrix

\[
\mathbf S=
\begin{bmatrix}
1&1\\
0&1
\end{bmatrix}
\]

has just one eigenvalue, 1. Its eigenspace is

\[
\ker(\mathbf S-\mathbf I)
=
\operatorname{span}
\left\{
\begin{bmatrix}1\\0\end{bmatrix}
\right\}
\]

so there is only one independent eigenvector. It cannot form an eigenvector basis of $\mathbb R^2$ and is not diagonalizable.

This matrix sends $(x,y)^\top$ to $(x+y,y)^\top$. Each repetition adds the second component to the first, giving $(x+ky,y)^\top$ after $k$ applications. For inputs with $y\ne0$, the first component can grow. Yet eigenvectors lie only in direction $y=0$, whose eigenvalue is 1. This shows why repeated scaling along eigendirections cannot determine behavior outside them.

The $90^\circ$ rotation matrix

\[
\begin{bmatrix}0&-1\\1&0\end{bmatrix}
\]

changes the direction of every nonzero real vector, so it has no real eigenvectors. Allowing complex numbers gives eigenvalues, but this lesson studies real spaces.

The figure below shows how repeated shear can grow an input outside the eigenspace even when 1 is the only eigenvalue. Distinguish invariance along the horizontal eigendirection from movement of other inputs.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Successive shear outputs zero one through three one outside the single horizontal eigenspace of eigenvalue one](../../figures/assets/M02/M02-11-defective-shear-iterates.svg)

<figcaption>Horizontal eigenvectors remain unchanged, but input (0,1) gains 1 in its first component at every repetition. One independent eigenvector cannot decompose the whole plane into an eigenbasis. Eigenvalue 1 alone does not establish preservation of every input's magnitude.</figcaption>
</figure>

The next figure shows a different failure: a 90-degree rotation sends the output perpendicular to the original line.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A nonzero real vector rotated ninety degrees to a perpendicular direction outside its original line](../../figures/assets/M02/M02-11-rotation-no-real-eigenvector.svg)

<figcaption>A 90-degree rotation sends every nonzero real vector off its own line. There are therefore no real eigenvectors, and characteristic equation λ²+1=0 has no real roots.</figcaption>
</figure>

## Core concept 7. Eigenvalues describe square transformations direction by direction

For a rectangular matrix, the two sides of

\[
\mathbf A\mathbf v=\lambda\mathbf v
\]

have different dimensions, so eigenvalues are not defined in the same way. SVD analyzes directional amplification for rectangular matrices or distinct input and output spaces.

A nonsymmetric square matrix may lack enough eigenvectors or have nonorthogonal eigenvectors. M02-12 introduces the spectral theorem, which gives real symmetric matrices an orthonormal eigenbasis.

## Example 1. Eigenvalues of a diagonal matrix

For

\[
\mathbf D=
\begin{bmatrix}
4&0\\
0&-2
\end{bmatrix}
\]

we have

\[
\mathbf D\mathbf e_1=4\mathbf e_1,
\qquad
\mathbf D\mathbf e_2=-2\mathbf e_2
\]

The vector $\mathbf e_1$ is an eigenvector for eigenvalue 4; $\mathbf e_2$ is an eigenvector for eigenvalue $-2$.

The first direction enlarges by 4. The second reverses and enlarges by 2.

## Example 2. $2\times2$ eigenvalues and eigenvectors

Let

\[
\mathbf A=
\begin{bmatrix}
2&1\\
0&3
\end{bmatrix}
\]

The characteristic equation is

\[
\det(\mathbf A-\lambda\mathbf I)
=
\det
\begin{bmatrix}
2-\lambda&1\\
0&3-\lambda
\end{bmatrix}
=
(2-\lambda)(3-\lambda)
=
0
\]

The eigenvalues are 2 and 3.

For $\lambda=2$, the equation

\[
(\mathbf A-2\mathbf I)\mathbf v=\mathbf 0
\]

requires the second component to be 0, so

\[
E_2
=
\operatorname{span}
\left\{
\begin{bmatrix}1\\0\end{bmatrix}
\right\}
\]

For $\lambda=3$, we have $-v_1+v_2=0$, so

\[
E_3
=
\operatorname{span}
\left\{
\begin{bmatrix}1\\1\end{bmatrix}
\right\}
\]

## Example 3. Repeated calculations in an eigenbasis

Using Example 2's eigenvectors, let

\[
\mathbf x
=
2
\begin{bmatrix}1\\0\end{bmatrix}
+
1
\begin{bmatrix}1\\1\end{bmatrix}
\]

Then

\[
\mathbf A^k\mathbf x
=
2\cdot2^k
\begin{bmatrix}1\\0\end{bmatrix}
+
3^k
\begin{bmatrix}1\\1\end{bmatrix}
\]

As $k$ increases, the component for eigenvalue 3 grows faster than that for eigenvalue 2.

## Example 4. Reading eigendirections in model analysis

The eigenvectors of a symmetric Hessian represent orthogonal curvature directions in parameter space. Its eigenvalues relate to second-order rates of change along those directions. M03-12 develops this interpretation alongside differentiation.

If a weight matrix is rectangular, eigenvalue analysis does not directly apply. Even a square matrix, if nonsymmetric, may have unstable eigenvectors or fail to form an eigenbasis. Check the object's shape and symmetry first.

## Common misconceptions

### Misconception 1. An eigenvector keeps exactly the same values after transformation

An eigenvector stays on the same line. Its magnitude changes with the eigenvalue, and a negative eigenvalue reverses its direction.

### Misconception 2. The zero vector is also an eigenvector

The zero vector satisfies the equation for every $\lambda$ and cannot distinguish eigenvalues. The definition excludes it.

### Misconception 3. Repeated eigenvalues provide equally many independent eigenvectors

A repeated eigenvalue's eigenspace dimension can be smaller than its multiplicity. Diagonalizing an $n\times n$ matrix requires $n$ independent eigenvectors.

### Misconception 4. A large eigenvalue means an important model feature

Eigenvalue magnitude describes amplification along an eigendirection of the given transformation. Correspondence with human-interpreted features or causal importance for model behavior requires additional evidence.

## Exercises

### 1. Check an eigenpair

For

\[
\mathbf A=
\begin{bmatrix}
3&0\\
0&-1
\end{bmatrix},
\qquad
\mathbf v=
\begin{bmatrix}0\\2\end{bmatrix}
\]

check whether $\mathbf v$ is an eigenvector and find its eigenvalue.

<details>
<summary>Show solution</summary>

\[
\mathbf A\mathbf v
=
\begin{bmatrix}0\\-2\end{bmatrix}
=
-1
\begin{bmatrix}0\\2\end{bmatrix}
\]

Since $\mathbf v\ne\mathbf 0$ and its image is $-1$ times $\mathbf v$, the eigenvalue is $-1$.

</details>

### 2. Find eigenvalues

Find the characteristic equation and eigenvalues of

\[
\mathbf B=
\begin{bmatrix}
1&2\\
0&4
\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

\[
\det(\mathbf B-\lambda\mathbf I)
=
\det
\begin{bmatrix}
1-\lambda&2\\
0&4-\lambda
\end{bmatrix}
=
(1-\lambda)(4-\lambda)
\]

Setting the characteristic polynomial to 0 gives eigenvalues $\lambda=1,4$.

</details>

### 3. Find eigenspaces

Find a basis for the eigenspace of each eigenvalue in Exercise 2.

<details>
<summary>Show solution</summary>

For $\lambda=1$,

\[
\mathbf B-\mathbf I
=
\begin{bmatrix}0&2\\0&3\end{bmatrix}
\]

so $v_2=0$. Thus,

\[
E_1
=
\operatorname{span}
\left\{
\begin{bmatrix}1\\0\end{bmatrix}
\right\}
\]

For $\lambda=4$,

\[
\mathbf B-4\mathbf I
=
\begin{bmatrix}-3&2\\0&0\end{bmatrix}
\]

so $-3v_1+2v_2=0$. For example, choosing $\mathbf v=\begin{bmatrix}2\\3\end{bmatrix}$ gives

\[
E_4
=
\operatorname{span}
\left\{
\begin{bmatrix}2\\3\end{bmatrix}
\right\}
\]

</details>

### 4. Repeated application

If $\mathbf A\mathbf v=-2\mathbf v$, find $\mathbf A^5\mathbf v$ and explain the change in direction and magnitude.

<details>
<summary>Show solution</summary>

\[
\mathbf A^5\mathbf v
=
(-2)^5\mathbf v
=
-32\mathbf v
\]

Its magnitude grows by 32, and an odd number of negative factors leaves it opposite to the original direction.

</details>

### 5. Diagonalizability

Suppose a $3\times3$ matrix has three distinct eigenvalues. Determine whether it is diagonalizable and explain why.

<details>
<summary>Show solution</summary>

Eigenvectors for distinct eigenvalues are linearly independent. Thus, three independent eigenvectors form a basis of $\mathbb R^3$, and the matrix is diagonalizable.

</details>

### 6. Absence of real eigenvectors

Find the characteristic equation of

\[
\mathbf R=
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}
\]

and determine whether it has real eigenvalues.

<details>
<summary>Show solution</summary>

\[
\det(\mathbf R-\lambda\mathbf I)
=
\det
\begin{bmatrix}
-\lambda&-1\\
1&-\lambda
\end{bmatrix}
=
\lambda^2+1
\]

No real $\lambda$ satisfies $\lambda^2+1=0$, so there are no real eigenvalues or real eigenvectors.

</details>

### 7. Choose an analysis method

For each matrix, decide whether eigendecomposition or SVD is the more appropriate starting point, and explain why.

1. A real symmetric Hessian $\mathbf H\in\mathbb R^{d\times d}$
2. A rectangular weight matrix $\mathbf W\in\mathbb R^{64\times128}$
3. A nonsymmetric square matrix $\mathbf A\in\mathbb R^{d\times d}$

<details>
<summary>Show solution</summary>

A symmetric Hessian has a real orthonormal eigenbasis, making eigendecomposition suitable for interpreting directional curvature.

A rectangular matrix does not map vectors from a space back to that same space, so the usual eigenvalue equation does not apply. SVD separates input directions, amplification factors, and output directions.

Eigenvalues are defined for a nonsymmetric square matrix, but it may lack enough real eigenvectors or have nonorthogonal ones. Eigenvalues can address questions about repeated dynamics. SVD may be more appropriate for stable directional amplification and low-rank structure.

</details>

## Lesson summary

- Eigenvectors are nonzero vectors staying on the same line after a linear transformation; eigenvalues are their scaling factors.
- Find eigenvalues from $\det(\mathbf A-\lambda\mathbf I)=0$; their eigenspaces are $\ker(\mathbf A-\lambda\mathbf I)$.
- Repeated matrix application multiplies eigendirection components by powers of eigenvalues.
- A matrix can be diagonalized if independent eigenvectors form a basis of its space.
- A real square matrix may lack real eigenvectors or fail to be diagonalizable.
- Eigenvalues describe directional transformation structure, not direct evidence of feature meanings or causal importance.

## Pass criteria

You pass if you can answer these questions without consulting the material:

- Can you define eigenvalues and eigenvectors in equations and words?
- Can you find eigenvalues from a $2\times2$ characteristic equation?
- Can you find an eigenspace basis for each eigenvalue?
- Can you explain why repeated application raises eigenvalues to powers?
- Can you determine how many independent eigenvectors diagonalization requires?
- Can you distinguish where eigendecomposition and SVD apply?

## Next lesson

- [M02-12 Symmetric matrices and the spectral theorem](M02-12-symmetric-matrices-spectral-theorem.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Eigenpairs, characteristic equations, and eigenspaces are defined.
- [x] Signs and magnitudes are connected to repeated application.
- [x] Diagonalization conditions and failure cases are included.
- [x] Analysis methods for square and rectangular matrices are distinguished.
- [x] Every exercise has a solution.
- [x] The scope of eigenvalues and model-feature claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
