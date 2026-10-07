---
id: "M03-07"
title: "Dual spaces and covectors"
part: 1
stage: "M03"
status: "complete"
prerequisites:
  - "M03-02"
  - "M03-03"
  - "M01-11"
estimated_time: "125–150 minutes"
---

# M03-07. Dual spaces and covectors

## Why this lesson matters

A vector can represent a directional change. A covector is a linear function that takes a vector and returns a scalar. In differentiation, a differential sends an input change vector to a first-order change in function value. A gradient is the vector representation of that covector obtained using an inner product.

In Euclidean coordinates, differentials and gradients appear as the same list of numbers, making them easy to confuse. Changing the basis or inner product reveals their different coordinate-transformation laws; the gradient corresponding to the same differential can also change. This distinction is needed to read Jacobians, VJPs, and backpropagation.

## Learning objectives

After this lesson, you will be able to:

- Define a covector as a linear map from a vector space to the real numbers.
- Construct a dual space and dual basis in small examples.
- Calculate the scalar produced by a covector acting on a vector.
- Explain why vector and covector coordinates transform in opposite ways under a change of basis.
- Connect differentials and gradients using an inner product.
- Distinguish linear probe weights from representation directions.

## Prerequisite check

- Prerequisite: [M03-02 Linear maps and matrix representation](M03-02-linear-maps-matrix-representation.md)
- Prerequisite: [M03-03 Change of basis and coordinate dependence](M03-03-change-of-basis-coordinate-dependence.md)
- Prerequisite: [M01-11 Directional derivatives and gradients](../M01/M01-11-directional-derivative-gradient.md)
- Check: Can you distinguish the input and output spaces of a linear map?
- Check: Can you read a coordinate-transformation direction from its subscript?
- Check: Can you calculate a directional derivative as the inner product of a gradient and a direction vector?

If linear maps or changes of basis are unclear, review the prerequisite lessons first.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Type |
|---|---|---|---|
| $V^*$ | `V star` | The dual space consisting of all covectors on $V$ | Vector space |
| $\varphi:V\to\mathbb R$ | `phi maps V to R` | A linear function sending vectors to scalars | Covector |
| $\mathcal B=(\mathbf b_1,\ldots,\mathbf b_n)$ | `the basis B consisting of b one through b n` | An ordered basis of $V$ | Basis |
| $\mathcal B^*=(\beta^1,\ldots,\beta^n)$ | `the dual basis B star` | The basis satisfying $\beta^i(\mathbf b_j)=\delta_{ij}$ | A basis of $V^*$ |
| $\boldsymbol\omega^\top$ | `omega transpose` | A covector's coordinate row | $1\times n$ |
| $df_{\mathbf x}$ | `d f at x` | The differential sending change vectors to first-order changes in function value | Covector |
| $\nabla f(\mathbf x)$ | `the gradient of f at x` | The vector corresponding to $df_{\mathbf x}$ under a chosen inner product | Vector |

## Core concept 1. A covector is a linear function that measures vectors

A covector $\varphi$ on a vector space $V$ is a linear map

\[
\varphi:V\to\mathbb R
\]

It satisfies, for all $\mathbf u,\mathbf v\in V$ and $\alpha,\beta\in\mathbb R$,

\[
\varphi(\alpha\mathbf u+\beta\mathbf v)
=
\alpha\varphi(\mathbf u)+\beta\varphi(\mathbf v)
\]

Using standard coordinates on $V=\mathbb R^n$, a covector can be represented by a row vector:

\[
\varphi(\mathbf v)
=
\boldsymbol\omega^\top\mathbf v
\]

The shapes are

\[
\underbrace{\boldsymbol\omega^\top}_{1\times n}
\underbrace{\mathbf v}_{n\times1}
\in\mathbb R
\]

The row vector $\boldsymbol\omega^\top$ is a coordinate representation in a chosen basis; the covector itself is a linear function.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Covector two x minus y displayed by constant-value parallel lines measuring vector four two as scalar six](../../figures/assets/M03/M03-07-covector-measurement.svg)
  <figcaption>The lines show equal measurement values of φ(x,y)=2x−y from Example 2. The vector endpoint (4,2) lies on the line with value 6, so φ(v)=6. A covector reads a scalar rather than moving the arrow's endpoint to another vector.</figcaption>
</figure>

The numbers on the gray lines are measurement values; the green arrow is the input vector being measured.

## Core concept 2. The set of all covectors is also a vector space

Collect all covectors on $V$ into

\[
V^*
=
\{\varphi:V\to\mathbb R\mid\varphi\text{ is linear}\}
\]

This is called the dual space of $V$.

Addition and scalar multiplication of covectors are defined pointwise:

\[
(\varphi+\psi)(\mathbf v)
=
\varphi(\mathbf v)+\psi(\mathbf v)
\]

\[
(\alpha\varphi)(\mathbf v)
=
\alpha\varphi(\mathbf v)
\]

We must also check that the results are covectors. For two inputs $\mathbf u,\mathbf v$ and scalars $a,b$,

\[
(\varphi+\psi)(a\mathbf u+b\mathbf v)
=a\bigl(\varphi(\mathbf u)+\psi(\mathbf u)\bigr)
+b\bigl(\varphi(\mathbf v)+\psi(\mathbf v)\bigr)
\]

Applying each function's linearity and collecting the $\mathbf u$ and $\mathbf v$ terms shows that the sum is linear. Scalar multiplication likewise preserves linearity through distributivity. The zero vector is the zero function sending every $\mathbf v$ to 0, and the additive inverse of $\varphi$ is $-\varphi$. The remaining vector space laws follow from pointwise function operations.

If $V$ is finite-dimensional,

\[
\dim V^*=\dim V
\]

Equal dimensions do not make $V$ and $V^*$ the same space. Vectors are elements of $V$, whereas covectors are functions from $V$ to scalars. Establishing a correspondence between the spaces requires choosing additional structure, such as a basis or inner product.

<figure class="lesson-figure" markdown="1">
  ![One input vector four two measured by covectors two x minus y and y with outputs six and two added to eight](../../figures/assets/M03/M03-07-add-covectors.svg)
  <figcaption>In this small example, the same input is measured separately by φ(x,y)=2x−y and ψ(x,y)=y, and the results are added. This agrees with measuring it using the sum of the rules, (φ+ψ)(x,y)=2x.</figcaption>
</figure>

The objects being added are two measurement functions, not two input vectors. The single input vector is fixed at the top.

## Core concept 3. A dual basis reads basis coefficients one at a time

For a basis of $V$,

\[
\mathcal B=(\mathbf b_1,\ldots,\mathbf b_n)
\]

the dual basis

\[
\mathcal B^*=(\beta^1,\ldots,\beta^n)
\]

satisfies

\[
\beta^i(\mathbf b_j)=\delta_{ij}
\]

The value of $\delta_{ij}$ is 1 if $i=j$ and 0 otherwise.

If

\[
\mathbf v
=
v^1\mathbf b_1+\cdots+v^n\mathbf b_n
\]

then

\[
\beta^i(\mathbf v)=v^i
\]

The function $\beta^i$ reads coordinate $i$ in $\mathcal B$.

This function is defined through uniqueness of basis representations. One vector cannot have two different values for coefficient $i$. Because recording coordinates preserves linear combinations, reading one coefficient with $\beta^i$ is also linear. Moreover,

\[
\beta^i(\mathbf v)
=\sum_{j=1}^n v^j\beta^i(\mathbf b_j)
=\sum_{j=1}^n v^j\delta_{ij}
=v^i
\]

The factor $\delta_{ij}$ leaves only the term with $j=i$. The superscript $i$ in $v^i$ and $\beta^i$ indexes a coefficient and a function; it is not a power.

Every covector $\varphi\in V^*$ also has a unique representation

\[
\varphi
=
\omega_1\beta^1+\cdots+\omega_n\beta^n
\]

Then

\[
\varphi(\mathbf v)
=
\sum_{i=1}^{n}\omega_i v^i
\]

Its coefficients are $\omega_i=\varphi(\mathbf b_i)$. Linearity gives $\varphi(\mathbf v)=\sum_i v^i\varphi(\mathbf b_i)$, so the function $\sum_i\omega_i\beta^i$ formed from these coefficients agrees with $\varphi$ at every input. Also, if $\sum_i c_i\beta^i$ is the zero function, applying it to $\mathbf b_j$ gives $c_j=0$. Thus, the dual basis spans all covectors and is linearly independent. Its $n$ functions form a basis, giving $\dim V^*=n$.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![First dual basis measurement lines for one half x plus y reading coefficient three from vector four two and distinguishing the two basis vectors](../../figures/assets/M03/M03-07-dual-first-coefficient.svg)
  <figcaption>The first dual function in Example 1 is β¹(x,y)=(x+y)/2. It reads 1 on b₁ and 0 on b₂; on the green vector 3b₁+b₂, it reads the first coefficient, 3.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Second dual basis measurement lines for one half x minus y reading coefficient one from vector four two and exchanging zero and one on the two basis vectors](../../figures/assets/M03/M03-07-dual-second-coefficient.svg)
  <figcaption>The second dual function, β²(x,y)=(x−y)/2, reads 0 on b₁ and 1 on b₂. Applying it to the same green vector gives the second coefficient, 1.</figcaption>
</figure>

The two figures have the same input vector but different measurement rules. Compare the line values to see which basis coefficient each dual function selects.

## Core concept 4. Vector and covector coordinates transform in opposite ways

Suppose vector coordinates between bases $\mathcal B,\mathcal C$ transform as

\[
[\mathbf v]_{\mathcal C}
=
\mathbf P_{\mathcal C\leftarrow\mathcal B}
[\mathbf v]_{\mathcal B}
\]

Write the covector's two coordinate rows as

\[
\boldsymbol\omega_{\mathcal B}^\top,
\qquad
\boldsymbol\omega_{\mathcal C}^\top
\]

The same scalar value must be independent of the basis, so

\[
\boldsymbol\omega_{\mathcal B}^\top[\mathbf v]_{\mathcal B}
=
\boldsymbol\omega_{\mathcal C}^\top[\mathbf v]_{\mathcal C}
\]

Substituting the vector coordinate transformation gives

\[
\boldsymbol\omega_{\mathcal B}^\top[\mathbf v]_{\mathcal B}
=
\boldsymbol\omega_{\mathcal C}^\top
\mathbf P_{\mathcal C\leftarrow\mathcal B}
[\mathbf v]_{\mathcal B}
\]

and therefore

\[
\boldsymbol\omega_{\mathcal C}^\top
=
\boldsymbol\omega_{\mathcal B}^\top
\mathbf P_{\mathcal B\leftarrow\mathcal C}
\]

If vector coordinates transform by $\mathbf P$, covector row coordinates transform by $\mathbf P^{-1}$. These opposite transformations preserve the scalar obtained by multiplying the two coordinate representations.

The equality determining the row coordinates must hold for every $[\mathbf v]_{\mathcal B}$, not just one vector. Substituting the coordinate unit vectors in turn forces equality of every corresponding row coefficient, giving $\boldsymbol\omega_{\mathcal B}^\top=\boldsymbol\omega_{\mathcal C}^\top\mathbf P_{\mathcal C\leftarrow\mathcal B}$. Multiplying on the right by the inverse change-of-basis matrix yields the covector transformation law.

Writing covector coefficients as a column gives the equivalent equation

\[
\boldsymbol\omega_{\mathcal C}
=
\mathbf P_{\mathcal C\leftarrow\mathcal B}^{-\top}
\boldsymbol\omega_{\mathcal B}
\]

Here, $\mathbf P^{-\top}$ means $(\mathbf P^{-1})^\top$. Transposing the row-coordinate equation reverses the product order, placing the inverse transpose on the left. Even when the coefficients are stored as a column, the object represented by the array is still a covector.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Example vector columns and covector rows in E and B coordinates changing by inverse matrices while both pairings produce scalar six](../../figures/assets/M03/M03-07-pairing-coordinate-change.svg)
  <figcaption>The vector column in Example 2 changes from (4,2)ᵀ to (3,1)ᵀ, while the covector row changes from (2,−1) to (1,3). Applying the opposite transformations together leaves the resulting scalar 6 unchanged.</figcaption>
</figure>

The upper $\mathbf P$ acts on the left of the vector column. The lower $\mathbf P^{-1}$ multiplies the covector row on the right.

## Core concept 5. An inner product represents a covector as a gradient vector

Let a scalar function $f:V\to\mathbb R$ on a finite-dimensional real vector space $V$ be differentiable at $\mathbf x$. Its differential at this point,

\[
df_{\mathbf x}:V\to\mathbb R
\]

sends a change vector $\mathbf v$ to a first-order change.

\[
df_{\mathbf x}(\mathbf v)
\]

is the directional derivative along $\mathbf v$. The differential is linear in $\mathbf v$, so it is a covector.

The point $\mathbf x$ stays fixed, and the input is the change vector $\mathbf v$. For a small scalar $\varepsilon$, the first-order change in $f(\mathbf x+\varepsilon\mathbf v)$ is $\varepsilon\,df_{\mathbf x}(\mathbf v)$. Even if $f$ itself is nonlinear, its first-order change rule at the point is linear in $\mathbf v$. M03-10 develops differentiability and the conditions for a total first-order approximation.

Choosing an inner product $\langle\cdot,\cdot\rangle$ determines one vector $\nabla f(\mathbf x)$ satisfying

\[
df_{\mathbf x}(\mathbf v)
=
\langle\nabla f(\mathbf x),\mathbf v\rangle
\]

for every $\mathbf v$. This vector is the gradient for the chosen inner product.

The requirement to produce the same value for every change vector determines the gradient uniquely. If the difference between two candidates is $\mathbf w$, then $\langle\mathbf w,\mathbf v\rangle=0$ for every $\mathbf v$. Taking $\mathbf v=\mathbf w$ gives $\langle\mathbf w,\mathbf w\rangle=0$, so $\mathbf w=\mathbf 0$.

For the standard Euclidean inner product on $V=\mathbb R^n$,

\[
df_{\mathbf x}(\mathbf v)
=
\nabla f(\mathbf x)^\top\mathbf v
\]

In these standard coordinates, applying the differential to unit vector $\mathbf e_i$ gives the partial derivative obtained by changing variable $i$ alone. Thus, the row coefficients of $df_{\mathbf x}$ are the partial derivatives, and the Euclidean gradient is the vector formed by placing those coefficients in a column.

Change the inner product to

\[
\langle\mathbf a,\mathbf b\rangle_{\mathbf G}
=
\mathbf a^\top\mathbf G\mathbf b
\]

with $\mathbf G$ symmetric positive definite. If the differential's coordinate column is $\boldsymbol\omega$, then

\[
\boldsymbol\omega^\top\mathbf v
=
\nabla_{\mathbf G}f(\mathbf x)^\top
\mathbf G\mathbf v
\]

so

\[
\nabla_{\mathbf G}f(\mathbf x)
=
\mathbf G^{-1}\boldsymbol\omega
\]

The differential remains the same linear function, but the gradient vector depends on the inner product.

Here, $\mathbf G$ records the inner product in the chosen coordinates. Symmetry means $\mathbf G^\top=\mathbf G$; positive definiteness means $\mathbf z^\top\mathbf G\mathbf z>0$ for nonzero $\mathbf z$. A nonzero vector satisfying $\mathbf G\mathbf z=\mathbf 0$ would violate this condition, so $\mathbf G$ is invertible.

Since the equality must hold for every $\mathbf v$, we have $\boldsymbol\omega^\top=\nabla_{\mathbf G}f(\mathbf x)^\top\mathbf G$. Transposing and using the symmetry of $\mathbf G$ gives $\boldsymbol\omega=\mathbf G\nabla_{\mathbf G}f(\mathbf x)$. Solving yields the inverse-matrix formula above. When changing the inner product, we keep the differential fixed and change the vector that represents its values through the inner product.

## Example 1. Read coordinates with a dual basis

### Problem

In $V=\mathbb R^2$, form a basis $\mathcal B$ from

\[
\mathbf b_1=
\begin{bmatrix}1\\1\end{bmatrix},
\qquad
\mathbf b_2=
\begin{bmatrix}1\\-1\end{bmatrix}
\]

Calculate dual basis functions $\beta^1,\beta^2$ as row vectors in standard coordinates.

### Solution

\[
\mathbf P_{\mathcal E\leftarrow\mathcal B}
=
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
\]

The matrix stacking the dual basis rows is the inverse of the basis matrix.

Call the matrix of stacked dual basis rows $\mathbf R$. Entry $(i,j)$ of $\mathbf R\mathbf P_{\mathcal E\leftarrow\mathcal B}$ is $\beta^i(\mathbf b_j)=\delta_{ij}$. The product is therefore the identity, making $\mathbf R$ the inverse of the basis matrix. This calculates rows that read basis coefficients, rather than merely turning basis vectors into rows.

\[
\mathbf P_{\mathcal E\leftarrow\mathcal B}^{-1}
=
\frac12
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
\]

Hence,

\[
\beta^1(\mathbf v)
=
\frac12
\begin{bmatrix}
1&1
\end{bmatrix}
\mathbf v
\]

\[
\beta^2(\mathbf v)
=
\frac12
\begin{bmatrix}
1&-1
\end{bmatrix}
\mathbf v
\]

Checking gives

\[
\beta^1(\mathbf b_1)=1,
\quad
\beta^1(\mathbf b_2)=0,
\quad
\beta^2(\mathbf b_1)=0,
\quad
\beta^2(\mathbf b_2)=1
\]

### What the result means

The functions $\beta^1$ and $\beta^2$ read the first and second $\mathcal B$ coefficients, respectively.

## Example 2. Covector coordinates in different bases

### Problem

In standard coordinates, a covector is given by

\[
\varphi(\mathbf v)
=
\begin{bmatrix}
2&-1
\end{bmatrix}
[\mathbf v]_{\mathcal E}
\]

Calculate the row coordinates of $\varphi$ in the basis $\mathcal B$ from Example 1.

### Solution

Since

\[
[\mathbf v]_{\mathcal E}
=
\mathbf P_{\mathcal E\leftarrow\mathcal B}
[\mathbf v]_{\mathcal B}
\]

we have

\[
\varphi(\mathbf v)
=
\begin{bmatrix}
2&-1
\end{bmatrix}
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
[\mathbf v]_{\mathcal B}
\]

The matrix product is

\[
\begin{bmatrix}
2&-1
\end{bmatrix}
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
=
\begin{bmatrix}
1&3
\end{bmatrix}
\]

so

\[
\boldsymbol\omega_{\mathcal B}^\top
=
\begin{bmatrix}
1&3
\end{bmatrix}
\]

If $[\mathbf v]_{\mathcal B}=(3,1)^\top$, then

\[
\varphi(\mathbf v)
=
\begin{bmatrix}
1&3
\end{bmatrix}
\begin{bmatrix}
3\\1
\end{bmatrix}
=
6
\]

The standard coordinates of the same vector are $(4,2)^\top$, giving

\[
\begin{bmatrix}
2&-1
\end{bmatrix}
\begin{bmatrix}
4\\2
\end{bmatrix}
=
6
\]

the same scalar.

### What the result means

Both vector and covector coordinates change, but the scalar produced by the covector acting on the vector is preserved.

## Example 3. A differential and two gradients

### Problem

For

\[
f(x,y)=x^2+3xy
\]

calculate the differential at $\mathbf x=(1,2)^\top$ and apply it to the change vector $\mathbf v=(-1,2)^\top$. Calculate the gradients for the Euclidean inner product and the inner product defined by

\[
\mathbf G=
\begin{bmatrix}
4&0\\
0&1
\end{bmatrix}
\]

### Solution

The partial derivatives are

\[
\frac{\partial f}{\partial x}=2x+3y,
\qquad
\frac{\partial f}{\partial y}=3x
\]

At $(1,2)$, the differential's row coordinates are

\[
\boldsymbol\omega^\top
=
\begin{bmatrix}
8&3
\end{bmatrix}
\]

Thus,

\[
df_{\mathbf x}(\mathbf v)
=
\begin{bmatrix}
8&3
\end{bmatrix}
\begin{bmatrix}
-1\\2
\end{bmatrix}
=
-8+6
=
-2
\]

The Euclidean gradient is

\[
\nabla f(\mathbf x)
=
\begin{bmatrix}
8\\3
\end{bmatrix}
\]

The gradient for the $\mathbf G$ inner product is

\[
\nabla_{\mathbf G}f(\mathbf x)
=
\mathbf G^{-1}\boldsymbol\omega
=
\begin{bmatrix}
\frac14&0\\
0&1
\end{bmatrix}
\begin{bmatrix}
8\\3
\end{bmatrix}
=
\begin{bmatrix}
2\\3
\end{bmatrix}
\]

The gradients differ, but

\[
\nabla f(\mathbf x)^\top\mathbf v=-2
\]

and

\[
\nabla_{\mathbf G}f(\mathbf x)^\top
\mathbf G\mathbf v
=
\begin{bmatrix}
2&3
\end{bmatrix}
\begin{bmatrix}
-4\\2
\end{bmatrix}
=
-2
\]

represent the same differential value.

### What the result means

A differential is the first-order change rule at a point. A gradient represents that rule as a vector through a chosen inner product.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Fixed differential eight delta x plus three delta y with Euclidean gradient eight three and metric gradient two three alongside direction minus one two](../../figures/assets/M03/M03-07-metric-gradient-pair.svg)
  <figcaption>In Example 3, the green vector (8,3)ᵀ represents the differential through the Euclidean inner product; the purple vector (2,3)ᵀ represents it through the inner product G=diag(4,1). Pairing each with the blue change vector through its respective inner product gives −2.</figcaption>
</figure>

The axes show change-vector coordinates, not the location of the base point itself. The gray lines show values of the fixed $df_{(1,2)}(\Delta x,\Delta y)=8\Delta x+3\Delta y$. This measurement function does not change when the gradient changes.

## Example 4. View a linear readout as a covector

Suppose a scalar score is calculated from activation $\mathbf h\in\mathbb R^d$ as

\[
s(\mathbf h)=\mathbf w^\top\mathbf h+b
\]

Removing the bias gives the covector

\[
\mathbf h\longmapsto\mathbf w^\top\mathbf h
\]

Calling $\mathbf w$ a “score direction” assumes a correspondence between covectors and vectors through the Euclidean inner product.

High accuracy of a linear probe shows that label-related information can be recovered from activations using this covector. Concluding that the model uses the same covector in its internal computation requires additional intervention or circuit evidence.

## Common misconceptions

### Misconception 1. A covector is a vector written horizontally

A row vector gives coordinates of a covector in a chosen basis. The covector itself is a linear function sending vectors to scalars.

### Misconception 2. $V$ and $V^*$ have the same dimension, so they are the same space

Their elements have different types. Choosing an inner product or basis lets us construct a correspondence, but the choice must not be omitted.

### Misconception 3. A differential and a gradient are always the same object

A differential is a covector. A gradient is the vector corresponding to that differential through a chosen inner product.

### Misconception 4. A probe weight is a basis-independent feature direction

Probe-weight coordinates depend on the activation basis and feature scaling. Interpreting them as a direction also requires stating the inner product and preprocessing used.

## Exercises

### 1. Test for a covector

Let $\varphi:\mathbb R^2\to\mathbb R$ be given by

\[
\varphi(x,y)=3x-2y
\]

Verify linearity and write its row representation in standard coordinates.

<details>
<summary>Show solution</summary>

Substituting coordinate-wise linear combinations of two vectors $\mathbf u,\mathbf v$ with scalars $\alpha,\beta$ gives

\[
\varphi(\alpha\mathbf u+\beta\mathbf v)
=
\alpha\varphi(\mathbf u)+\beta\varphi(\mathbf v)
\]

Its row representation is

\[
\boldsymbol\omega^\top=
\begin{bmatrix}
3&-2
\end{bmatrix}
\]

</details>

### 2. Calculate a covector's action

Given

\[
\boldsymbol\omega^\top=
\begin{bmatrix}
1&-3&2
\end{bmatrix},
\qquad
\mathbf v=
\begin{bmatrix}
2\\1\\-1
\end{bmatrix}
\]

calculate $\boldsymbol\omega^\top\mathbf v$.

<details>
<summary>Show solution</summary>

\[
\boldsymbol\omega^\top\mathbf v
=
1\cdot2+(-3)\cdot1+2\cdot(-1)
=
-3
\]

A covector acting on a vector produces a scalar.

</details>

### 3. Standard dual basis

State how the dual basis $\varepsilon^1,\varepsilon^2,\varepsilon^3$ of the standard basis of $\mathbb R^3$ acts on $(a,b,c)^\top$.

<details>
<summary>Show solution</summary>

\[
\varepsilon^1(a,b,c)^\top=a,
\qquad
\varepsilon^2(a,b,c)^\top=b,
\qquad
\varepsilon^3(a,b,c)^\top=c
\]

Each covector reads one corresponding standard coordinate.

</details>

### 4. Change of basis and scalar preservation

Vector coordinates transform as $\mathbf v_{\mathcal C}=\mathbf P\mathbf v_{\mathcal B}$. Calculate $\boldsymbol\omega_{\mathcal C}^\top$ so that $\boldsymbol\omega_{\mathcal C}^\top\mathbf v_{\mathcal C}=\boldsymbol\omega_{\mathcal B}^\top\mathbf v_{\mathcal B}$.

<details>
<summary>Show solution</summary>

The equation

\[
\boldsymbol\omega_{\mathcal C}^\top
\mathbf P\mathbf v_{\mathcal B}
=
\boldsymbol\omega_{\mathcal B}^\top\mathbf v_{\mathcal B}
\]

must hold for every $\mathbf v_{\mathcal B}$, so

\[
\boldsymbol\omega_{\mathcal C}^\top\mathbf P
=
\boldsymbol\omega_{\mathcal B}^\top
\]

Thus,

\[
\boldsymbol\omega_{\mathcal C}^\top
=
\boldsymbol\omega_{\mathcal B}^\top\mathbf P^{-1}
\]

</details>

### 5. Calculate a differential

For

\[
f(x,y)=x^2+y^2
\]

calculate the row coordinates of $df_{\mathbf x}$ at $\mathbf x=(1,-2)^\top$ and apply it to $\mathbf v=(3,1)^\top$.

<details>
<summary>Show solution</summary>

The partial derivatives are $2x$ and $2y$, so

\[
df_{\mathbf x}
\longleftrightarrow
\begin{bmatrix}
2&-4
\end{bmatrix}
\]

Therefore,

\[
df_{\mathbf x}(\mathbf v)
=
\begin{bmatrix}
2&-4
\end{bmatrix}
\begin{bmatrix}
3\\1
\end{bmatrix}
=
2
\]

</details>

### 6. Gradient for a metric

The differential's coordinate column is

\[
\boldsymbol\omega=
\begin{bmatrix}
6\\2
\end{bmatrix}
\]

and

\[
\mathbf G=
\begin{bmatrix}
3&0\\
0&2
\end{bmatrix}
\]

Calculate the gradient for the $\mathbf G$ inner product.

<details>
<summary>Show solution</summary>

\[
\nabla_{\mathbf G}f
=
\mathbf G^{-1}\boldsymbol\omega
=
\begin{bmatrix}
\frac13&0\\
0&\frac12
\end{bmatrix}
\begin{bmatrix}
6\\2
\end{bmatrix}
=
\begin{bmatrix}
2\\1
\end{bmatrix}
\]

</details>

### 7. Critique a model claim

Critique the statement: “Probe weights and activation vectors are both columns in $\mathbb R^d$, so they are the same type of feature.”

<details>
<summary>Show solution</summary>

An activation is a vector in the representation space. Probe weights are coordinates of a covector sending activations to scores; choosing the Euclidean inner product lets us identify it with a column vector. Matching array shapes do not make their types and transformation laws identical.

</details>

## Lesson summary

- A covector is a linear function sending vectors to scalars; all covectors form the dual space $V^*$.
- A dual basis reads the original basis coefficients one at a time.
- Vector and covector coordinates follow opposite transformation laws to preserve the scalar pairing.
- A differential is a covector sending change vectors to first-order changes.
- A gradient is a vector representation of a differential using a chosen inner product.
- Interpreting linear readout weights as directions requires stating the basis, scaling, and inner product.

## Pass criteria

You pass if you can answer the following without consulting the lesson.

- Can you define a covector and a dual space?
- Can you explain how a dual basis reads basis coordinates?
- Can you calculate the action of a covector on a vector?
- Can you derive the coordinate transformation law for covectors?
- Can you distinguish differentials from gradients by type and inner product?
- Can you state the assumptions needed to interpret probe weights as a covector?

## Next lesson

- [M03-08 Bilinear forms and quadratic forms](M03-08-bilinear-quadratic-forms.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] A covector is defined as a linear function.
- [x] The dual basis and change of basis are calculated.
- [x] Differential and gradient types are distinguished.
- [x] Changes in the gradient with the metric are included.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
