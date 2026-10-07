---
id: "M03-03"
title: "Change of basis and coordinate dependence"
part: 1
stage: "M03"
status: "complete"
prerequisites:
  - "M03-01"
  - "M03-02"
  - "M02-07"
estimated_time: "120–145 minutes"
---

# M03-03. Change of basis and coordinate dependence

## Why this lesson matters

The same vector has different numerical columns in different bases. The same linear map also has different matrices when its input and output bases change. Ignoring this dependence when analyzing coordinates or matrix entries can lead us to mistake a difference in representation for a difference in the object itself.

In model interpretation, a neuron is one coordinate axis defined by the implementation. A large activation of a particular neuron is a clear fact in that coordinate system, but mixing the basis of the representation space can distribute the same abstract vector across multiple coordinates. We must distinguish coordinate-dependent claims from claims that remain valid after a change of basis.

## Learning objectives

After this lesson, you will be able to:

- Convert coordinates of the same vector between two bases using a change-of-basis matrix.
- Explain the columns and subscript direction of a change-of-basis matrix.
- Relate two matrix representations of the same linear map through a change-of-basis formula.
- Derive the similarity transformation formula with its convention stated.
- Distinguish coordinate-dependent quantities from properties preserved under a change of basis.
- Distinguish passive coordinate changes from active transformations that change a vector itself.

## Prerequisite check

- Prerequisite: [M03-01 Abstract vector spaces](M03-01-abstract-vector-spaces.md)
- Prerequisite: [M03-02 Linear maps and matrix representation](M03-02-linear-maps-matrix-representation.md)
- Prerequisite: [M02-07 Linear independence, basis, and dimension](../M02/M02-07-linear-independence-basis-dimension.md)
- Check: Can you distinguish a vector from its basis coordinates?
- Check: Can you explain why each column of a matrix representation contains output coordinates of a domain basis vector?

If matrix-representation subscripts are unclear, review M03-02 first.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape |
|---|---|---|---|
| $\mathcal B=(\mathbf b_1,\ldots,\mathbf b_n)$ | `the basis B consisting of b one through b n` | The old basis of $V$ | An ordered basis |
| $\mathcal C=(\mathbf c_1,\ldots,\mathbf c_n)$ | `the basis C consisting of c one through c n` | The new basis of $V$ | An ordered basis |
| $\mathbf P_{\mathcal C\leftarrow\mathcal B}$ | `the change-of-basis matrix from B coordinates to C coordinates` | The matrix converting $\mathcal B$ coordinates to $\mathcal C$ coordinates | $n\times n$ |
| $[T]_{\mathcal B}$ | `the matrix of T in the basis B` | A representation using $\mathcal B$ for both domain and codomain | $n\times n$ |
| similarity transformation | `similarity transformation` | A transformation relating matrices of the same linear operator in different bases | Of the form $\mathbf P^{-1}\mathbf A\mathbf P$ |
| Coordinate dependence | `coordinate dependence` | Numerical representations depend on the chosen basis | Coordinates, matrix entries, and related quantities |

## Core concept 1. A coordinate transformation changes the numerical representation of the same vector

Let $\mathcal B$ and $\mathcal C$ be two bases of $V$. The change-of-basis matrix

\[
\mathbf P_{\mathcal C\leftarrow\mathcal B}
\]

converts the $\mathcal B$ coordinates of the same vector $\mathbf v$ to its $\mathcal C$ coordinates:

\[
[\mathbf v]_{\mathcal C}
=
\mathbf P_{\mathcal C\leftarrow\mathcal B}
[\mathbf v]_{\mathcal B}
\]

A coordinate transformation does not change $\mathbf v$ itself. It changes only the numerical column describing $\mathbf v$.

The reverse transformation uses the inverse matrix:

\[
\mathbf P_{\mathcal B\leftarrow\mathcal C}
=
\mathbf P_{\mathcal C\leftarrow\mathcal B}^{-1}
\]

\[
[\mathbf v]_{\mathcal B}
=
\mathbf P_{\mathcal B\leftarrow\mathcal C}
[\mathbf v]_{\mathcal C}
\]

Because both lists are bases, the change-of-basis matrix must be invertible.

We can check this by going in both directions. Reconstruct the original vector from its $\mathcal B$ coordinates, read its $\mathcal C$ coordinates, and then read its $\mathcal B$ coordinates again. We return to the original coefficient column because basis representations are unique. The same holds in the opposite direction, so the product of the two change-of-basis matrices is the identity in either order. A coordinate transformation does not discard information as a projection does.

<figure class="lesson-figure" markdown="1">
  ![Vector four two assembled as four horizontal standard basis units and two vertical standard basis units on a coordinate grid](../../figures/assets/M03/M03-03-standard-coordinates.svg)
  <figcaption>Reconstructing the vector in Example 1 from the standard basis moves 4 units right and 2 units up. The vector shown by the green arrow has standard coordinates (4,2)ᵀ.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">
  ![Same vector four two assembled by three copies of basis one one and one copy of basis one minus one on the same coordinate grid](../../figures/assets/M03/M03-03-oblique-coordinates.svg)
  <figcaption>Reconstructing 3b₁+b₂ on the same coordinate grid leaves the green arrow's endpoint unchanged. The new column (3,1)ᵀ does not give standard coordinates of a different vector: it gives the coefficients specifying how many copies of each new basis vector to use.</figcaption>
</figure>

Comparing the green arrows in the two figures separates the object preserved by a passive coordinate change from the coefficients that change.

## Core concept 2. The columns record the starting basis vectors in the destination basis

Considering the identity map $\operatorname{Id}_V:V\to V$ gives

\[
\mathbf P_{\mathcal C\leftarrow\mathcal B}
=
[\operatorname{Id}_V]_{\mathcal C\leftarrow\mathcal B}
\]

By the matrix-representation rule from M03-02,

\[
\mathbf P_{\mathcal C\leftarrow\mathcal B}
=
\begin{bmatrix}
[\mathbf b_1]_{\mathcal C}
&
\cdots
&
[\mathbf b_n]_{\mathcal C}
\end{bmatrix}
\]

Each column thus records a vector from the starting basis $\mathcal B$ in the destination basis $\mathcal C$.

For $V=\mathbb R^n$, with standard basis $\mathcal E$, we can write

\[
\mathbf P_{\mathcal E\leftarrow\mathcal B}
=
\begin{bmatrix}
\mathbf b_1&\cdots&\mathbf b_n
\end{bmatrix}
\]

Here, each $\mathbf b_j$ is a standard-coordinate column.

To check a column's meaning, consider an input whose $\mathcal B$ coordinates are $\mathbf e_j$. Only coefficient $j$ is 1, so the original vector is $\mathbf b_j$. Recording it in $\mathcal C$ gives $[\mathbf b_j]_{\mathcal C}$, which must be column $j$ of the transformation matrix. Here, $\mathbf e_j$ is a standard basis vector in the space of coefficient columns; it is not necessarily the same vector as $\mathbf b_j$ in the original space.

If both basis lists are given in standard coordinates, first reconstruct the vector from its $\mathcal B$ coordinates and then read the $\mathcal C$ coefficients of that result. Hence,

\[
\mathbf P_{\mathcal C\leftarrow\mathcal B}
=\mathbf P_{\mathcal C\leftarrow\mathcal E}
\mathbf P_{\mathcal E\leftarrow\mathcal B}
=\mathbf P_{\mathcal E\leftarrow\mathcal C}^{-1}
\mathbf P_{\mathcal E\leftarrow\mathcal B}
\]

The matrix with destination basis vectors as standard-coordinate columns goes from $\mathcal C$ coordinates to standard coordinates. Reading $\mathcal C$ coefficients from standard coordinates therefore requires its inverse.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Basis vectors one one and one minus one assembled as ordered columns of the B to E coordinate matrix then weighted by three and one](../../figures/assets/M03/M03-03-coordinate-columns.svg)
  <figcaption>The two starting basis vectors in Example 1 are recorded in standard coordinates, the destination basis, and placed in columns. Multiplying by starting coefficients (3,1)ᵀ scales the columns by 3 and 1 and adds them, giving standard coordinates (4,2)ᵀ of the same vector.</figcaption>
</figure>

Each colored column records one starting basis vector in the destination basis; it is not a new location of a coordinate axis.

## Core concept 3. Matrices of the same linear operator are related by similarity

Let $T:V\to V$ be a linear operator, using the same basis for domain and codomain. For the same vector,

\[
[T(\mathbf v)]_{\mathcal C}
=
\mathbf P_{\mathcal C\leftarrow\mathcal B}
[T(\mathbf v)]_{\mathcal B}
\]

Also,

\[
[T(\mathbf v)]_{\mathcal B}
=
[T]_{\mathcal B}[\mathbf v]_{\mathcal B}
\]

and

\[
[\mathbf v]_{\mathcal B}
=
\mathbf P_{\mathcal B\leftarrow\mathcal C}
[\mathbf v]_{\mathcal C}
\]

Combining the three equations gives

\[
[T(\mathbf v)]_{\mathcal C}
=
\mathbf P_{\mathcal C\leftarrow\mathcal B}
[T]_{\mathcal B}
\mathbf P_{\mathcal B\leftarrow\mathcal C}
[\mathbf v]_{\mathcal C}
\]

so

\[
[T]_{\mathcal C}
=
\mathbf P_{\mathcal C\leftarrow\mathcal B}
[T]_{\mathcal B}
\mathbf P_{\mathcal B\leftarrow\mathcal C}
\]

It is common to set $\mathbf P=\mathbf P_{\mathcal B\leftarrow\mathcal C}$, giving

\[
[T]_{\mathcal C}
=
\mathbf P^{-1}[T]_{\mathcal B}\mathbf P
\]

Memorizing the formula without stating which direction $\mathbf P$ converts coordinates makes it easy to put the inverse on the wrong side.

<figure class="lesson-figure" markdown="1">
  ![Similarity calculation route converts B coordinates to E applies T in E and converts the output back to B using the example vector](../../figures/assets/M03/M03-03-similarity-route.svg)
  <figcaption>To calculate the operator in Example 2 in the new basis, convert the input to familiar standard coordinates, apply T there, and record the output back in the new basis. Distinguish the two coordinate-changing end steps from the vector-changing middle step.</figcaption>
</figure>

The three matrices appear in the equation in the reverse order of the path. In this lesson's example, $(3,1)^\top$ ultimately becomes $(5,3)^\top$.

## Core concept 4. Numerical quantities are not all preserved in the same way

When representing the same vector or map in another basis, distinguish the following.

| Object | Under a general change of basis |
|---|---|
| Individual vector coordinates | Change. |
| Individual matrix entries | Change. |
| Whether a vector is zero | Preserved. |
| Linear independence | Preserved. |
| Subspace dimension | Preserved. |
| Rank and nullity of a linear map | Preserved. |
| Determinant, trace, and eigenvalues of a linear operator | Preserved under similarity. |
| Euclidean norm of a coordinate column | May not be preserved under an arbitrary change of basis. |

To preserve lengths and angles, we must transform the inner product as well, or use an orthogonal coordinate transformation between orthonormal bases. Singular values are not automatically preserved under a general similarity transformation either. The invariants depend on the transformation group allowed.

Zero vectors and linear independence are preserved because the coordinate transformation is invertible and preserves linear combinations. If $\mathbf P\mathbf x=\mathbf 0$, multiplying by the inverse gives $\mathbf x=\mathbf 0$. Also, if a linear combination of transformed vectors is zero, applying the inverse gives a zero linear combination of the original vectors with the same coefficients. Independent vectors therefore cannot become dependent because of a coordinate transformation. A subspace basis is carried to an independent spanning set of the same size, so dimension is preserved. The same reasoning applies to coordinates of the kernel and image.

For linear-operator invariants, similarity requires the same change of basis on the domain and codomain. Using $\mathbf A=[T]_{\mathcal B}$ and $\mathbf P=\mathbf P_{\mathcal B\leftarrow\mathcal C}$ from the preceding section, the new matrix is $\mathbf P^{-1}\mathbf A\mathbf P$. For a nonzero coordinate column $\mathbf z$ satisfying $\mathbf A\mathbf z=\lambda\mathbf z$,

\[
(\mathbf P^{-1}\mathbf A\mathbf P)(\mathbf P^{-1}\mathbf z)
=\mathbf P^{-1}\mathbf A\mathbf z
=\lambda\mathbf P^{-1}\mathbf z
\]

The column $\mathbf P^{-1}\mathbf z$ is also nonzero, so the same $\lambda$ is an eigenvalue in the new representation. The reverse direction gives the same conclusion, so eigenvalues are preserved. The product rule for determinants and $\det(\mathbf P^{-1})\det(\mathbf P)=1$ show that the determinant is preserved as well.

For the trace, two $n\times n$ matrices $\mathbf X,\mathbf Y$ satisfy

\[
\operatorname{tr}(\mathbf X\mathbf Y)
=\sum_{i=1}^n\sum_{j=1}^n X_{ij}Y_{ji}
=\sum_{j=1}^n\sum_{i=1}^n Y_{ji}X_{ij}
=\operatorname{tr}(\mathbf Y\mathbf X)
\]

This does not mean that matrix multiplication itself commutes; it means that the trace of the product agrees in these two orders. Setting $\mathbf X=\mathbf P^{-1}$ and $\mathbf Y=\mathbf A\mathbf P$ gives $\operatorname{tr}(\mathbf P^{-1}\mathbf A\mathbf P)=\operatorname{tr}(\mathbf A\mathbf P\mathbf P^{-1})=\operatorname{tr}\mathbf A$.

In contrast, distinguish the length of a coordinate column from the length of the original vector. In Example 1 below, $\mathbf b_1=(1,1)^\top$ has length $\sqrt2$ in standard coordinates, but its $\mathcal B$ coordinates are $(1,0)^\top$, whose Euclidean norm is 1. The vector's actual length has not changed. Rather, a coefficient attached to a basis vector of nonunit length was treated as a unit-length coordinate. Between orthonormal bases, the change-of-basis matrix $\mathbf Q$ satisfies $\mathbf Q^\top\mathbf Q=\mathbf I$, giving $\|\mathbf Q\mathbf x\|_2^2=\mathbf x^\top\mathbf Q^\top\mathbf Q\mathbf x=\|\mathbf x\|_2^2$.

Singular values also depend on the lengths used for coordinates. The matrices $\begin{bmatrix}1&1\\0&2\end{bmatrix}$ and $\begin{bmatrix}1&0\\0&2\end{bmatrix}$ in Exercise 4 below are related by similarity, but their squared Frobenius norms are 6 and 5, respectively. By M02-13, their sums of squared singular values differ, so their lists of singular values cannot be identical. Do not read preservation of eigenvalues as preservation of singular values.

<figure class="lesson-figure" markdown="1">
  ![Basis vector one one on a coordinate grid has geometric length square root of two although its B coefficient vector one zero has norm one](../../figures/assets/M03/M03-03-coordinate-norm.svg)
  <figcaption>The length of b₁ itself is √2, but its reconstruction coefficients in B are (1,0)ᵀ. Applying the ordinary Euclidean norm to that column gives 1, not the actual vector length in this non-orthonormal basis.</figcaption>
</figure>

The origin and endpoint do not move in the figure. The differing length calculations result from confusing basis-vector units with coefficient units, not from moving the vector.

## Core concept 5. Passive coordinate changes differ from active transformations

A passive coordinate change leaves the abstract vector $\mathbf v$ unchanged and changes only its coordinates:

\[
[\mathbf v]_{\mathcal B}
\longrightarrow
[\mathbf v]_{\mathcal C}
\]

An active transformation fixes the basis and applies a linear map $R$ to change the vector itself:

\[
\mathbf v
\longrightarrow
R(\mathbf v)
\]

The same-looking matrix may appear in both calculations, but they answer different questions. Are we changing the coordinate system and describing the same object again, or actually rotating or projecting the object?

The matrix $\begin{bmatrix}1&1\\1&-1\end{bmatrix}$ in Example 1 converts $\mathcal B$ coordinates $(3,1)^\top$ to standard coordinates $(4,2)^\top$. Its passive multiplication takes two different records of the same vector as input and output. But if the same array represents an active linear transformation in the fixed standard basis, it sends a vector with standard coordinates $(3,1)^\top$ to a different vector with standard coordinates $(4,2)^\top$. Even when the numbers in the multiplication are identical, their meaning depends on the input and output bases.

<figure class="lesson-figure" markdown="1">
  ![Fixed standard coordinate axes with an input vector three one actively transformed into vector four two with a visible endpoint movement](../../figures/assets/M03/M03-03-active-versus-passive.svg)
  <figcaption>Using the same array as an active map in the standard basis moves the endpoint from standard coordinates (3,1)ᵀ to (4,2)ᵀ. The earlier passive transformation only recorded a vector already at (4,2)ᵀ with different coefficients, so even the starting point has a different meaning.</figcaption>
</figure>

The two arrows here are different vectors. Compare this with the earlier basis-reconstruction figures, where the green arrow was the same vector.

## Example 1. Convert vector coordinates between two bases

### Problem

In $V=\mathbb R^2$, let $\mathcal E$ be the standard basis and let

\[
\mathcal B=
\left(
\begin{bmatrix}1\\1\end{bmatrix},
\begin{bmatrix}1\\-1\end{bmatrix}
\right)
\]

Calculate the $\mathcal B$ coordinates of $\mathbf v=(4,2)^\top$.

### Solution

Arranging the $\mathcal B$ basis vectors as standard-coordinate columns gives

\[
\mathbf P_{\mathcal E\leftarrow\mathcal B}
=
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
\]

Its inverse is

\[
\mathbf P_{\mathcal B\leftarrow\mathcal E}
=
\frac12
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
\]

Therefore,

\[
[\mathbf v]_{\mathcal B}
=
\mathbf P_{\mathcal B\leftarrow\mathcal E}
[\mathbf v]_{\mathcal E}
=
\frac12
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
\begin{bmatrix}
4\\
2
\end{bmatrix}
=
\begin{bmatrix}
3\\
1
\end{bmatrix}
\]

Checking by reconstruction gives

\[
3
\begin{bmatrix}1\\1\end{bmatrix}
+
1
\begin{bmatrix}1\\-1\end{bmatrix}
=
\begin{bmatrix}4\\2\end{bmatrix}
\]

### What the result means

Standard coordinates $(4,2)^\top$ and $\mathcal B$ coordinates $(3,1)^\top$ represent the same vector.

## Example 2. Change the matrix of the same linear operator

### Problem

The linear operator $T:\mathbb R^2\to\mathbb R^2$ has standard-basis matrix

\[
[T]_{\mathcal E}
=
\begin{bmatrix}
2&0\\
0&1
\end{bmatrix}
\]

Calculate $[T]_{\mathcal B}$ in the basis $\mathcal B$ from Example 1.

### Solution

Since

\[
[T]_{\mathcal B}
=
\mathbf P_{\mathcal B\leftarrow\mathcal E}
[T]_{\mathcal E}
\mathbf P_{\mathcal E\leftarrow\mathcal B}
\]

we obtain

\[
[T]_{\mathcal B}
=
\frac12
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
\begin{bmatrix}
2&0\\
0&1
\end{bmatrix}
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
=
\begin{bmatrix}
\frac32&\frac12\\
\frac12&\frac32
\end{bmatrix}
\]

Comparing trace and determinant gives

\[
\operatorname{tr}[T]_{\mathcal E}
=
\operatorname{tr}[T]_{\mathcal B}
=
3
\]

\[
\det[T]_{\mathcal E}
=
\det[T]_{\mathcal B}
=
2
\]

The matrix entries have changed, but the matrices represent the same linear operator, so their similarity invariants agree.

### What the result means

In the standard basis, the two coordinate axes are scaled by 2 and 1. In $\mathcal B$, the same operation appears as a matrix that mixes the two coordinates. Even whether a matrix is diagonal depends on the chosen basis.

## Example 3. Read coordinate dependence in model representations

Let a layer activation be $\mathbf h\in\mathbb R^d$ and define new coordinates using an invertible matrix $\mathbf P$:

\[
\widetilde{\mathbf h}
=
\mathbf P^{-1}\mathbf h
\]

This can be viewed as recording the same abstract representation vector in new basis coordinates, not removing $\mathbf h$ itself.

If the linear output is

\[
\mathbf y=\mathbf W\mathbf h
\]

then

\[
\mathbf h=\mathbf P\widetilde{\mathbf h}
\]

so

\[
\mathbf y
=
\mathbf W\mathbf P\widetilde{\mathbf h}
\]

The input-side weight representation in the new coordinates is $\widetilde{\mathbf W}=\mathbf W\mathbf P$. Changing only activation coordinates while keeping weights unchanged generally does not produce the same output.

This is a coordinate re-expression at a linear interface. If a nonlinear function lies between the components, whether arbitrary basis mixing can be absorbed in the same way must be checked separately.

## Common misconceptions

### Misconception 1. Changing the basis rotates the vector

In a passive change of basis, the vector stays the same and only its coordinates change. Distinguish this from an active transformation that rotates the vector itself.

### Misconception 2. Basis vectors can be placed in the columns in either transformation direction

The columns of $\mathbf P_{\mathcal C\leftarrow\mathcal B}$ are $[\mathbf b_j]_{\mathcal C}$. The starting and destination bases in the subscript determine what the columns mean.

### Misconception 3. The same linear map has the same matrix entries

Matrix entries depend on the bases. The same linear map is represented by different matrices in different bases.

### Misconception 4. The Euclidean norm has the same numerical value in every basis

A coordinate transformation between orthonormal bases preserves the Euclidean norm of the coordinate column. In an arbitrary nonorthogonal basis, that column's Euclidean norm may differ from the original length of the abstract vector.

## Exercises

### 1. Read matrix columns

Explain the two columns of

\[
\mathbf P_{\mathcal C\leftarrow\mathcal B}
=
\begin{bmatrix}
1&2\\
0&1
\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

The first column, $(1,0)^\top$, gives the $\mathcal C$ coordinates of $\mathbf b_1$, the first vector of $\mathcal B$. The second column, $(2,1)^\top$, gives the $\mathcal C$ coordinates of $\mathbf b_2$.

</details>

### 2. Convert coordinates

In the preceding exercise, calculate $[\mathbf v]_{\mathcal C}$ when $[\mathbf v]_{\mathcal B}=(3,-1)^\top$.

<details>
<summary>Show solution</summary>

\[
[\mathbf v]_{\mathcal C}
=
\begin{bmatrix}
1&2\\
0&1
\end{bmatrix}
\begin{bmatrix}
3\\
-1
\end{bmatrix}
=
\begin{bmatrix}
1\\
-1
\end{bmatrix}
\]

</details>

### 3. Reverse a coordinate transformation

Calculate the inverse of

\[
\mathbf P_{\mathcal C\leftarrow\mathcal B}
=
\begin{bmatrix}
1&2\\
0&1
\end{bmatrix}
\]

and convert $[\mathbf v]_{\mathcal C}=(1,-1)^\top$ back to $\mathcal B$ coordinates.

<details>
<summary>Show solution</summary>

\[
\mathbf P_{\mathcal B\leftarrow\mathcal C}
=
\begin{bmatrix}
1&-2\\
0&1
\end{bmatrix}
\]

Therefore,

\[
[\mathbf v]_{\mathcal B}
=
\begin{bmatrix}
1&-2\\
0&1
\end{bmatrix}
\begin{bmatrix}
1\\
-1
\end{bmatrix}
=
\begin{bmatrix}
3\\
-1
\end{bmatrix}
\]

</details>

### 4. Calculate a similarity transformation

Given

\[
\mathbf A_{\mathcal B}
=
\begin{bmatrix}
1&1\\
0&2
\end{bmatrix},
\qquad
\mathbf P_{\mathcal B\leftarrow\mathcal C}
=
\begin{bmatrix}
1&1\\
0&1
\end{bmatrix}
\]

calculate $\mathbf A_{\mathcal C}=\mathbf P^{-1}\mathbf A_{\mathcal B}\mathbf P$.

<details>
<summary>Show solution</summary>

\[
\mathbf P^{-1}
=
\begin{bmatrix}
1&-1\\
0&1
\end{bmatrix}
\]

and

\[
\mathbf A_{\mathcal B}\mathbf P
=
\begin{bmatrix}
1&2\\
0&2
\end{bmatrix}
\]

Hence,

\[
\mathbf A_{\mathcal C}
=
\begin{bmatrix}
1&-1\\
0&1
\end{bmatrix}
\begin{bmatrix}
1&2\\
0&2
\end{bmatrix}
=
\begin{bmatrix}
1&0\\
0&2
\end{bmatrix}
\]

</details>

### 5. Check invariants

Compare the trace, determinant, and eigenvalues of the two matrices in Exercise 4.

<details>
<summary>Show solution</summary>

Both have trace 3 and determinant 2. Both are triangular, so their eigenvalues are their diagonal entries, 1 and 2. These values agree because the matrices are representations of the same linear operator related by a similarity transformation.

</details>

### 6. Distinguish passive and active changes

Classify the following as passive coordinate changes or active transformations.

1. Record the same geographical location in coordinates of two rotated axes instead of east–west and north–south coordinates.
2. Keep the axes fixed and rotate an object 30 degrees around the origin.

<details>
<summary>Show solution</summary>

The first is a passive coordinate change: the object's location stays fixed and only its numerical representation changes. The second is an active transformation: the axes stay fixed while the object's location itself changes.

</details>

### 7. Critique a model claim

Critique the conclusion: “Concept information is concentrated in one neuron, so that concept is stored in one coordinate in every basis.”

<details>
<summary>Show solution</summary>

A neuron is one axis of the implementation's coordinate system. Invertible basis mixing can distribute information in the same abstract representation vector over multiple coordinates. We can present evidence that one neuron matters for prediction or intervention in the original coordinates, but this does not imply that concentration in one coordinate holds in every basis. We must also specify which transformations are allowed and how the model function is preserved.

</details>

## Lesson summary

- A coordinate transformation represents the same vector as a numerical column in another basis.
- The columns of $\mathbf P_{\mathcal C\leftarrow\mathcal B}$ are the $\mathcal C$ coordinates of $\mathcal B$ basis vectors.
- Two matrices of the same linear operator are related by a similarity transformation.
- Matrix entries and vector coordinates depend on the basis, but rank, dimension, and similarity invariants are preserved.
- The Euclidean norm of coordinates is not automatically preserved under arbitrary changes of basis.
- Passive coordinate changes and active vector transformations answer different questions.

## Pass criteria

You pass if you can answer the following without consulting the lesson.

- Can you explain the subscript and columns of a change-of-basis matrix?
- Can you convert one vector's coordinates between two bases in both directions?
- Can you derive the similarity transformation formula from coordinate equations?
- Can you calculate two matrix representations of the same linear map?
- Can you distinguish coordinate-dependent values from preserved properties?
- Can you distinguish passive coordinate changes from active transformations?

## Next lesson

- [M03-04 Introduction to invariants and equivariance](M03-04-invariants-equivariance.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Coordinate-transformation directions are specified in subscripts.
- [x] The similarity transformation is derived with its convention stated.
- [x] Passive coordinate changes are distinguished from active transformations.
- [x] Coordinate-dependent quantities are distinguished from preserved properties.
- [x] Example calculations have been checked.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
