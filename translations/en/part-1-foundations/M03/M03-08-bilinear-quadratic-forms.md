---
id: "M03-08"
title: "Bilinear forms and quadratic forms"
part: 1
stage: "M03"
status: "complete"
prerequisites:
  - "M03-03"
  - "M03-07"
  - "M02-12"
estimated_time: "120–145 minutes"
---

# M03-08. Bilinear forms and quadratic forms

## Why this lesson matters

Inner products, attention scores, and second-order approximations use expressions that send two vectors to a scalar, or insert one vector twice to produce a scalar. The matrix product $\mathbf x^\top\mathbf A\mathbf y$ represents a bilinear form in coordinates; $\mathbf x^\top\mathbf A\mathbf x$ represents a quadratic form.

The same matrix can represent a linear map or a bilinear form, but their change-of-basis laws differ. A linear operator's matrix follows a similarity transformation, whereas a bilinear form's matrix follows a congruence transformation. Determining an object's type from matrix entries alone misses this distinction.

## Learning objectives

After this lesson, you will be able to:

- Verify separate linearity in each input of a bilinear map or bilinear form.
- Calculate a bilinear form in a chosen basis as $\mathbf x^\top\mathbf A\mathbf y$.
- Distinguish symmetric bilinear forms from the additional requirements of inner products.
- Explain why only a matrix's symmetric part contributes to a quadratic form.
- Calculate a congruence transformation under a change of basis.
- Explain the scope of bilinear structure in attention scores and Hessian-based quadratic expressions.

## Prerequisite check

- Prerequisite: [M03-03 Change of basis and coordinate dependence](M03-03-change-of-basis-coordinate-dependence.md)
- Prerequisite: [M03-07 Dual spaces and covectors](M03-07-dual-spaces-covectors.md)
- Prerequisite: [M02-12 Symmetric matrices and the spectral theorem](../M02/M02-12-symmetric-matrices-spectral-theorem.md)
- Check: Can you explain a matrix's quadratic form and positive semidefiniteness?
- Check: Can you explain how a covector sends a vector to a scalar?
- Check: Can you read the direction of a change-of-basis matrix?

If quadratic forms or changes of basis are unclear, review the prerequisite lessons first.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Type |
|---|---|---|---|
| $B:V\times W\to\mathbb R$ | `B maps V cross W to R` | A function linear in each input | Bilinear map |
| $B:V\times V\to\mathbb R$ | `B maps V cross V to R` | A bilinear map taking two vectors from the same vector space | Bilinear form |
| $\mathbf A$ | `A` | A bilinear form's matrix in a chosen basis | $n\times n$ |
| $q:V\to\mathbb R$ | `q maps V to R` | A function satisfying $q(\mathbf x)=B(\mathbf x,\mathbf x)$ | Quadratic form |
| $\mathbf A_{\mathrm{sym}}$ | `A sub sym` | $\frac12(\mathbf A+\mathbf A^\top)$ | Symmetric part |
| congruence transformation | `congruence transformation` | A transformation relating matrices of a bilinear form in different bases | $\mathbf P^\top\mathbf A\mathbf P$ |

## Core concept 1. A bilinear map is linear in each input separately

A map

\[
B:V\times W\to\mathbb R
\]

is bilinear if fixing one input makes it a linear function of the other input.

The set $V\times W$ consists of ordered pairs whose first input belongs to $V$ and second input belongs to $W$. Here, $\times$ does not mean calculating a vector cross product. Even if the two input spaces are the same, the first and second slots are distinct.

For the first input,

\[
B(\alpha\mathbf u_1+\beta\mathbf u_2,\mathbf v)
=
\alpha B(\mathbf u_1,\mathbf v)
+
\beta B(\mathbf u_2,\mathbf v)
\]

and for the second input,

\[
B(\mathbf u,\alpha\mathbf v_1+\beta\mathbf v_2)
=
\alpha B(\mathbf u,\mathbf v_1)
+
\beta B(\mathbf u,\mathbf v_2)
\]

Scaling both inputs by the same scalar gives

\[
B(\alpha\mathbf u,\alpha\mathbf v)
=
\alpha B(\mathbf u,\alpha\mathbf v)
=
\alpha^2B(\mathbf u,\mathbf v)
\]

One factor comes from linearity in the first input, and another from linearity in the second. Thus, a bilinear map is generally not a linear function of the single vector formed by grouping the two inputs.

Compare a graph with one input fixed against a graph with both inputs scaled to distinguish the two kinds of linearity.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Scalar bilinear map u times v with v fixed at two gives a straight line through the origin](../../figures/assets/M03/M03-08-one-slot-linear.svg)
  <figcaption>Fixing the second input at 2 gives output 2u as a function of the first input. Doubling the input in just one slot doubles the output.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Scaling both inputs of u times v by the same factor gives a quadratic curve rather than the dashed joint linear prediction](../../figures/assets/M03/M03-08-two-slots-quadratic.svg)
  <figcaption>Scaling both inputs (1,2) by a gives output 2a². Because both inputs change, the scale factor is multiplied twice.</figcaption>
</figure>

## Core concept 2. Choosing a basis represents a bilinear form as a matrix

Let $\mathcal B=(\mathbf b_1,\ldots,\mathbf b_n)$ be a basis of $V$. Define matrix entries of a bilinear form $B:V\times V\to\mathbb R$ by

\[
A_{ij}=B(\mathbf b_i,\mathbf b_j)
\]

Then

\[
B(\mathbf x,\mathbf y)
=
[\mathbf x]_{\mathcal B}^\top
\mathbf A_{\mathcal B}
[\mathbf y]_{\mathcal B}
\]

The shapes are

\[
\underbrace{[\mathbf x]_{\mathcal B}^\top}_{1\times n}
\underbrace{\mathbf A_{\mathcal B}}_{n\times n}
\underbrace{[\mathbf y]_{\mathcal B}}_{n\times1}
\in\mathbb R
\]

Column $j$ is related to the coordinates of the covector obtained by fixing $\mathbf y=\mathbf b_j$. Fixing one input of a bilinear form produces a covector acting on the other input.

The matrix representation follows by expanding both inputs in the basis. Write $x_i,y_j$ for the $\mathcal B$ coefficients of $\mathbf x,\mathbf y$, respectively. Then

\[
B(\mathbf x,\mathbf y)
=B\left(\sum_i x_i\mathbf b_i,\sum_j y_j\mathbf b_j\right)
=\sum_i\sum_j x_i y_jB(\mathbf b_i,\mathbf b_j)
=\sum_i\sum_j x_iA_{ij}y_j
\]

Expanding the first input gives a sum over $i$; expanding the second input in each term gives a sum over $j$. The final double sum is the matrix product above.

In particular, if $\mathbf y=\mathbf b_j$, then $B(\mathbf x,\mathbf b_j)=\sum_i x_iA_{ij}$. The coefficient column of this covector is column $j$ of the matrix, but its row representation acting on input coordinates is that column transposed. Distinguish the covector obtained by fixing one input from the output vector obtained by interpreting the matrix as a linear map.

The double sum in Example 1 adds the four contributions at the row–column intersections below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Four matrix cells show the products of row input coefficient matrix entry and column input coefficient summing to scalar twelve](../../figures/assets/M03/M03-08-weighted-matrix-pairing.svg)
  <figcaption>Each entry of A=[[2,4],[−2,3]] acts on a different pair xᵢ,yⱼ. The sum of the four contributions, 12, is B(x,y); the matrix itself is not the output.</figcaption>
</figure>

## Core concept 3. Symmetric bilinear forms and inner products have different requirements

A bilinear form is symmetric if

\[
B(\mathbf x,\mathbf y)=B(\mathbf y,\mathbf x)
\]

For its matrix in a basis, this is equivalent to

\[
\mathbf A^\top=\mathbf A
\]

Substituting basis vectors into symmetry gives $A_{ij}=B(\mathbf b_i,\mathbf b_j)=B(\mathbf b_j,\mathbf b_i)=A_{ji}$. Conversely, for a symmetric matrix, transposing the scalar $\mathbf x^\top\mathbf A\mathbf y$ gives $\mathbf y^\top\mathbf A^\top\mathbf x=\mathbf y^\top\mathbf A\mathbf x$, so exchanging the inputs leaves the value unchanged. Here, $\mathbf x,\mathbf y$ denote coordinate columns in the chosen basis.

An inner product on a real vector space is a bilinear form satisfying:

1. Symmetry: $\langle\mathbf x,\mathbf y\rangle=\langle\mathbf y,\mathbf x\rangle$
2. Positive definiteness: $\langle\mathbf x,\mathbf x\rangle>0$ for $\mathbf x\ne\mathbf 0$

A bilinear form need not be an inner product. It may be nonsymmetric, or it may give $B(\mathbf x,\mathbf x)\le0$ at a nonzero input.

Positive semidefiniteness can also be insufficient. For example, $\begin{bmatrix}1&0\\0&0\end{bmatrix}$ is symmetric and gives quadratic values $x_1^2\ge0$, but it gives 0 even at the nonzero vector $(0,1)^\top$. An inner product requires positivity for every nonzero input so that a nonzero vector cannot have zero squared length.

Level sets connect inputs with the same quadratic value. Compare whether only the origin, or an entire direction, gives value zero.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Positive definite quadratic form has closed positive value ellipses around its single zero at the origin](../../figures/assets/M03/M03-08-positive-definite.svg)
  <figcaption>For the positive definite matrix in Example 3, every input away from the origin has positive value. The level sets for 1, 4, and 9 surround the origin, but value 0 occurs only at the origin.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Semidefinite quadratic form x squared is constant along vertical lines and is zero on the whole vertical axis including a nonzero vector](../../figures/assets/M03/M03-08-positive-semidefinite.svg)
  <figcaption>In q(x,y)=x², changes in the y direction do not affect the value. Even the nonzero vector (0,1) gives value zero, so this expression cannot be squared length from an inner product.</figcaption>
</figure>

## Core concept 4. A quadratic form inserts the same vector into both inputs

Given a bilinear form $B$, the function defined by

\[
q(\mathbf x)=B(\mathbf x,\mathbf x)
\]

is called a quadratic form. In coordinates,

\[
q(\mathbf x)
=
\mathbf x^\top\mathbf A\mathbf x
\]

A quadratic form satisfies

\[
q(\alpha\mathbf x)=\alpha^2q(\mathbf x)
\]

under scalar multiplication. In general,

\[
q(\mathbf x+\mathbf y)
\ne
q(\mathbf x)+q(\mathbf y)
\]

In particular, unless $q$ is the zero function, $q(2\mathbf x)=4q(\mathbf x)$ is incompatible with the linearity requirement $q(2\mathbf x)=2q(\mathbf x)$, so it is not linear.

Expanding through linearity in both inputs reveals the difference under addition:

\[
q(\mathbf x+\mathbf y)
=B(\mathbf x+\mathbf y,\mathbf x+\mathbf y)
=q(\mathbf x)+B(\mathbf x,\mathbf y)+B(\mathbf y,\mathbf x)+q(\mathbf y)
\]

The two cross terms are added, so the result generally differs from $q(\mathbf x)+q(\mathbf y)$. Inserting the same vector into both slots means that scaling acts in both slots together.

Removing the cross term from the symmetric part in Example 2 also changes the equal-value level sets.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Level eighteen ellipse with cross term two x y differs from the dashed level eighteen ellipse omitting that term and point one two lies only on the full form](../../figures/assets/M03/M03-08-cross-term-level-set.svg)
  <figcaption>The green curve is 2x²+2xy+3y²=18; the orange dashed curve is 2x²+3y²=18. At input (1,2), the cross term adds 4, giving a full value of 18 rather than the value 14 obtained without it.</figcaption>
</figure>

## Core concept 5. Only the symmetric part contributes to a quadratic form

Decompose a matrix into symmetric and skew-symmetric parts:

\[
\mathbf A
=
\underbrace{\frac12(\mathbf A+\mathbf A^\top)}_{\mathbf A_{\mathrm{sym}}}
+
\underbrace{\frac12(\mathbf A-\mathbf A^\top)}_{\mathbf A_{\mathrm{skew}}}
\]

The skew-symmetric part satisfies $\mathbf A_{\mathrm{skew}}^\top=-\mathbf A_{\mathrm{skew}}$. Transposing the scalar

\[
s=\mathbf x^\top\mathbf A_{\mathrm{skew}}\mathbf x
\]

gives

\[
s
=
s^\top
=
\mathbf x^\top\mathbf A_{\mathrm{skew}}^\top\mathbf x
=
-\mathbf x^\top\mathbf A_{\mathrm{skew}}\mathbf x
=
-s
\]

so $s=0$. Thus,

\[
\mathbf x^\top\mathbf A\mathbf x
=
\mathbf x^\top\mathbf A_{\mathrm{sym}}\mathbf x
\]

With distinct inputs in $\mathbf x^\top\mathbf A\mathbf y$, the skew-symmetric part does not disappear.

For a symmetric bilinear form, we can recover the original form from its quadratic form:

\[
B(\mathbf x,\mathbf y)
=
\frac12
\left(
q(\mathbf x+\mathbf y)-q(\mathbf x)-q(\mathbf y)
\right)
\]

This is called the polarization identity.

Subtracting $q(\mathbf x)$ and $q(\mathbf y)$ from the addition expansion in the preceding section leaves $B(\mathbf x,\mathbf y)+B(\mathbf y,\mathbf x)$. Symmetry makes the two terms equal, so dividing by 2 gives $B(\mathbf x,\mathbf y)$. Without symmetry, this calculation recovers the symmetric part, not the entire original form.

When the same vector is inserted in both slots, both cross terms share the same $x_1x_2$. In the skew part of Example 2, the coefficients have opposite signs and cancel as follows.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Skew symmetric matrix off diagonal terms on input one two contribute positive six and negative six which cancel to zero](../../figures/assets/M03/M03-08-skew-cross-term-cancellation.svg)
  <figcaption>The skew part [[0,3],[−3,0]] is not the zero matrix. But its cross terms 6 and −6 for the same input (1,2) cancel, so it contributes nothing to the quadratic value.</figcaption>
</figure>

## Core concept 6. A bilinear form's matrix changes by congruence

Let $\mathcal B,\mathcal C$ be two bases, with

\[
[\mathbf x]_{\mathcal B}
=
\mathbf P_{\mathcal B\leftarrow\mathcal C}
[\mathbf x]_{\mathcal C}
\]

Applying the same relation to $\mathbf y$ gives

\[
B(\mathbf x,\mathbf y)
=
[\mathbf x]_{\mathcal C}^\top
\mathbf P_{\mathcal B\leftarrow\mathcal C}^\top
\mathbf A_{\mathcal B}
\mathbf P_{\mathcal B\leftarrow\mathcal C}
[\mathbf y]_{\mathcal C}
\]

Thus,

\[
\mathbf A_{\mathcal C}
=
\mathbf P_{\mathcal B\leftarrow\mathcal C}^\top
\mathbf A_{\mathcal B}
\mathbf P_{\mathcal B\leftarrow\mathcal C}
\]

This is called a congruence transformation.

Its form differs from a linear operator's similarity transformation,

\[
\mathbf P^{-1}\mathbf A\mathbf P
\]

A bilinear form changes both input coordinates, so a transpose appears on the left.

Below, the two input coordinates are transformed separately. Congruence leaves the $\mathbf P$ from each slot on the corresponding side of the matrix.

<figure class="lesson-figure" markdown="1">
  ![Both bilinear input coordinate columns pass through P and the matrix changes by P transpose A P while scalar two is preserved](../../figures/assets/M03/M03-08-two-slot-congruence.svg)
  <figcaption>The calculation uses P=[[1,1],[0,1]] and A_B=diag(2,1). Transforming both inputs before calculating or constructing A_C=PᵀA_BP first gives the same scalar 2.</figcaption>
</figure>

## Core concept 7. Bilinear expressions appear in attention scores and curvature

For column-vector inputs $\mathbf x,\mathbf y\in\mathbb R^d$, let

\[
\mathbf q=\mathbf W_Q\mathbf x,
\qquad
\mathbf k=\mathbf W_K\mathbf y
\]

Here, $\mathbf W_Q,\mathbf W_K\in\mathbb R^{d_k\times d}$ are matrices of fixed linear maps, with no bias. The dot-product score of their outputs $\mathbf q,\mathbf k\in\mathbb R^{d_k}$ is

\[
\mathbf q^\top\mathbf k
=
\mathbf x^\top
\mathbf W_Q^\top\mathbf W_K
\mathbf y
\]

It is bilinear in $\mathbf x$ and $\mathbf y$. The full attention operation, applying softmax to scores and taking a weighted sum of values, is not bilinear.

An inner product is calculated in query–key space, but the form's matrix in input space is $\mathbf W_Q^\top\mathbf W_K\in\mathbb R^{d\times d}$. Different query and key maps do not guarantee a symmetric matrix. Swapping the two input vectors swaps which vector enters each map, so the score may change.

When a scalar function is twice continuously differentiable around $\mathbf x$, its second-order approximation includes

\[
\frac12
\Delta\mathbf x^\top
\mathbf H_f(\mathbf x)
\Delta\mathbf x
\]

The Hessian's quadratic form describes second-order curvature along small change directions. M03-12 covers the Hessian's definition and calculation.

In this expression, the base point $\mathbf x$ is fixed and the change vector $\Delta\mathbf x$ is inserted in both slots. The second-order term with the Hessian fixed at that point is a quadratic form; this does not mean that the entire original function is quadratic.

## Example 1. Calculate bilinear and quadratic forms

### Problem

Given

\[
\mathbf A=
\begin{bmatrix}
2&4\\
-2&3
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}
1\\2
\end{bmatrix},
\qquad
\mathbf y=
\begin{bmatrix}
-1\\1
\end{bmatrix}
\]

calculate $B(\mathbf x,\mathbf y)=\mathbf x^\top\mathbf A\mathbf y$, $B(\mathbf y,\mathbf x)$, and $q(\mathbf x)$.

### Solution

Since

\[
\mathbf A\mathbf y
=
\begin{bmatrix}
2\\5
\end{bmatrix}
\]

we have

\[
B(\mathbf x,\mathbf y)
=
\begin{bmatrix}
1&2
\end{bmatrix}
\begin{bmatrix}
2\\5
\end{bmatrix}
=
12
\]

Also,

\[
\mathbf A\mathbf x
=
\begin{bmatrix}
10\\4
\end{bmatrix}
\]

so

\[
B(\mathbf y,\mathbf x)
=
\begin{bmatrix}
-1&1
\end{bmatrix}
\begin{bmatrix}
10\\4
\end{bmatrix}
=
-6
\]

The values differ, so $B$ is not symmetric.

\[
q(\mathbf x)
=
\mathbf x^\top\mathbf A\mathbf x
=
\begin{bmatrix}
1&2
\end{bmatrix}
\begin{bmatrix}
10\\4
\end{bmatrix}
=
18
\]

### What the result means

Even with the same matrix, exchanging the inputs can give different bilinear values. A quadratic form inserts one vector into both slots.

## Example 2. Keep only the symmetric part

For the matrix in Example 1,

\[
\mathbf A_{\mathrm{sym}}
=
\frac12
\left(
\begin{bmatrix}
2&4\\
-2&3
\end{bmatrix}
+
\begin{bmatrix}
2&-2\\
4&3
\end{bmatrix}
\right)
=
\begin{bmatrix}
2&1\\
1&3
\end{bmatrix}
\]

Thus,

\[
\mathbf x^\top\mathbf A_{\mathrm{sym}}\mathbf x
=
\begin{bmatrix}
1&2
\end{bmatrix}
\begin{bmatrix}
4\\7
\end{bmatrix}
=
18
\]

gives the same value as the original quadratic form.

The skew-symmetric part is

\[
\mathbf A_{\mathrm{skew}}
=
\begin{bmatrix}
0&3\\
-3&0
\end{bmatrix}
\]

and

\[
\mathbf x^\top\mathbf A_{\mathrm{skew}}\mathbf x=0
\]

## Example 3. A positive definite bilinear form

Consider the form defined by

\[
\mathbf G=
\begin{bmatrix}
2&1\\
1&2
\end{bmatrix}
\]

as

\[
\langle\mathbf x,\mathbf y\rangle_{\mathbf G}
=
\mathbf x^\top\mathbf G\mathbf y
\]

The matrix $\mathbf G$ is symmetric. For $\mathbf x=(x_1,x_2)^\top$,

\[
\mathbf x^\top\mathbf G\mathbf x
=
2x_1^2+2x_1x_2+2x_2^2
\]

and

\[
2x_1^2+2x_1x_2+2x_2^2
=
x_1^2+x_2^2+(x_1+x_2)^2
\]

If $\mathbf x\ne\mathbf 0$, this value is positive. Thus, $B_{\mathbf G}$ is an inner product.

## Example 4. The bilinear matrix of an attention score

Let

\[
\mathbf W_Q=
\begin{bmatrix}
1&0\\
1&1
\end{bmatrix},
\qquad
\mathbf W_K=
\begin{bmatrix}
1&1\\
0&1
\end{bmatrix}
\]

and

\[
\mathbf x=
\begin{bmatrix}
1\\2
\end{bmatrix},
\qquad
\mathbf y=
\begin{bmatrix}
3\\-1
\end{bmatrix}
\]

Then

\[
\mathbf q=\mathbf W_Q\mathbf x=
\begin{bmatrix}
1\\3
\end{bmatrix},
\qquad
\mathbf k=\mathbf W_K\mathbf y=
\begin{bmatrix}
2\\-1
\end{bmatrix}
\]

so

\[
\mathbf q^\top\mathbf k=-1
\]

The bilinear matrix in input space is

\[
\mathbf W_Q^\top\mathbf W_K
=
\begin{bmatrix}
1&2\\
0&1
\end{bmatrix}
\]

and

\[
\mathbf x^\top
\mathbf W_Q^\top\mathbf W_K
\mathbf y
=
-1
\]

gives the same score.

This calculation describes only the bilinear structure of one pre-softmax score. Attention weights and final outputs also involve normalization and a weighted sum of values.

The two-projection calculation and the single-bilinear-matrix calculation in Example 4 give the same score.

<figure class="lesson-figure" markdown="1">
  ![Query input one two and key input three minus one are separately projected to one three and two minus one then dotted to score minus one before softmax](../../figures/assets/M03/M03-08-attention-score-pairing.svg)
  <figcaption>The dot product after separate query and key projections, −1, equals xᵀW_QᵀW_Ky. The bilinear path ends at the score; it does not make the full attention operation after softmax linear.</figcaption>
</figure>

## Common misconceptions

### Misconception 1. $\mathbf x^\top\mathbf A\mathbf y$ is a linear function of the two inputs jointly

Fixing one input gives linearity in the other. Scaling both inputs by $\alpha$ scales the output by $\alpha^2$.

### Misconception 2. Every symmetric bilinear form is an inner product

An inner product also requires positive definiteness. A symmetric matrix with a negative eigenvalue cannot define an inner product.

### Misconception 3. A quadratic form preserves all the matrix's information

A quadratic form uses only the symmetric part. The skew-symmetric part disappears from $\mathbf x^\top\mathbf A\mathbf x$.

### Misconception 4. A bilinear form's matrix also changes by similarity

A bilinear form changes both input coordinates together and therefore follows a congruence transformation.

### Misconception 5. The entire attention operation is bilinear

The query–key dot product can be written as bilinear in the input pair. Attention, including softmax and the subsequent weighted sum, is nonlinear.

## Exercises

### 1. Check bilinearity

Determine whether

\[
B(\mathbf x,\mathbf y)=x_1y_1+2x_2y_1
\]

is bilinear on $\mathbb R^2\times\mathbb R^2$.

<details>
<summary>Show solution</summary>

Fixing $\mathbf y$ gives $B(\mathbf x,\mathbf y)=y_1x_1+2y_1x_2$, which is linear in $\mathbf x$. Fixing $\mathbf x$ gives $B(\mathbf x,\mathbf y)=(x_1+2x_2)y_1+0y_2$, which is linear in $\mathbf y$. Thus, the map is bilinear.

</details>

### 2. Calculate with a matrix

Given

\[
\mathbf A=
\begin{bmatrix}
1&2\\
3&0
\end{bmatrix},
\quad
\mathbf x=
\begin{bmatrix}2\\-1\end{bmatrix},
\quad
\mathbf y=
\begin{bmatrix}1\\4\end{bmatrix}
\]

calculate $\mathbf x^\top\mathbf A\mathbf y$.

<details>
<summary>Show solution</summary>

Since

\[
\mathbf A\mathbf y
=
\begin{bmatrix}
9\\3
\end{bmatrix}
\]

we have

\[
\mathbf x^\top\mathbf A\mathbf y
=
\begin{bmatrix}
2&-1
\end{bmatrix}
\begin{bmatrix}
9\\3
\end{bmatrix}
=
15
\]

</details>

### 3. Test symmetry

Determine whether the bilinear form defined by

\[
\mathbf A=
\begin{bmatrix}
2&-1\\
-1&4
\end{bmatrix}
\]

is symmetric.

<details>
<summary>Show solution</summary>

Since $\mathbf A^\top=\mathbf A$,

\[
\mathbf x^\top\mathbf A\mathbf y
=
\mathbf y^\top\mathbf A\mathbf x
\]

holds for every $\mathbf x,\mathbf y$. Thus, the bilinear form is symmetric.

</details>

### 4. Calculate the symmetric part

Calculate the symmetric part of

\[
\mathbf A=
\begin{bmatrix}
1&5\\
-1&2
\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

\[
\mathbf A_{\mathrm{sym}}
=
\frac12(\mathbf A+\mathbf A^\top)
=
\frac12
\begin{bmatrix}
2&4\\
4&4
\end{bmatrix}
=
\begin{bmatrix}
1&2\\
2&2
\end{bmatrix}
\]

Using this symmetric matrix gives the same $\mathbf x^\top\mathbf A\mathbf x$.

</details>

### 5. Congruence transformation

Given

\[
\mathbf A_{\mathcal B}
=
\begin{bmatrix}
2&0\\
0&1
\end{bmatrix},
\qquad
\mathbf P_{\mathcal B\leftarrow\mathcal C}
=
\begin{bmatrix}
1&1\\
0&1
\end{bmatrix}
\]

calculate $\mathbf A_{\mathcal C}$.

<details>
<summary>Show solution</summary>

\[
\mathbf A_{\mathcal C}
=
\mathbf P^\top\mathbf A_{\mathcal B}\mathbf P
\]

and

\[
\mathbf A_{\mathcal B}\mathbf P
=
\begin{bmatrix}
2&2\\
0&1
\end{bmatrix}
\]

Thus,

\[
\mathbf A_{\mathcal C}
=
\begin{bmatrix}
1&0\\
1&1
\end{bmatrix}
\begin{bmatrix}
2&2\\
0&1
\end{bmatrix}
=
\begin{bmatrix}
2&2\\
2&3
\end{bmatrix}
\]

</details>

### 6. Read an attention score

Given $\mathbf q=\mathbf W_Q\mathbf x$ and $\mathbf k=\mathbf W_K\mathbf y$, write $\mathbf q^\top\mathbf k$ in the form $\mathbf x^\top\mathbf A\mathbf y$ and identify $\mathbf A$.

<details>
<summary>Show solution</summary>

\[
\mathbf q^\top\mathbf k
=
(\mathbf W_Q\mathbf x)^\top
(\mathbf W_K\mathbf y)
=
\mathbf x^\top
\mathbf W_Q^\top\mathbf W_K
\mathbf y
\]

Thus,

\[
\mathbf A=\mathbf W_Q^\top\mathbf W_K
\]

</details>

### 7. Critique a model claim

Critique the statement: “An attention score is a bilinear form, so the entire attention layer is linear.”

<details>
<summary>Show solution</summary>

A query–key score is a bilinear expression, linear in each input when the other is fixed. It is not linear as a function that changes both inputs jointly. An attention layer also includes score scaling, softmax, and a weighted sum of values. The score's bilinear structure alone does not establish linearity of the full layer.

</details>

## Lesson summary

- A bilinear map is linear in each input separately; a bilinear form takes two vectors from the same space.
- In a chosen basis, a bilinear form is represented as $\mathbf x^\top\mathbf A\mathbf y$.
- An inner product is a symmetric positive definite bilinear form.
- A quadratic form inserts the same vector twice and uses only the matrix's symmetric part.
- Matrices of a bilinear form in different bases are related by a congruence transformation.
- Bilinear and quadratic structures appear in query–key attention scores and Hessian-based second-order expressions.

## Pass criteria

You pass if you can answer the following without consulting the lesson.

- Can you write the two linearity requirements for a bilinear map?
- Can you calculate a bilinear form using its matrix representation?
- Can you distinguish symmetric bilinear forms from inner products?
- Can you explain why only the symmetric part remains in a quadratic form?
- Can you calculate a congruence transformation?
- Can you identify the bilinear matrix in an attention score?
- Can you distinguish a bilinear score from the full nonlinear layer?

## Next lesson

- [M03-09 Tensors and multilinear maps](M03-09-tensors-multilinear-maps.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Separate linearity in each input of a bilinear map is defined.
- [x] The matrix representation and shapes are specified.
- [x] The symmetric part is connected to the quadratic form.
- [x] Congruence is distinguished from similarity.
- [x] The scope of attention scores is distinguished from the full operation.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
