---
id: "M03-11"
title: "Jacobian"
part: 1
stage: "M03"
status: "complete"
prerequisites:
  - "M03-10"
  - "M02-08"
  - "M02-13"
estimated_time: "120–145 minutes"
---

# M03-11. Jacobian

## Why this lesson matters

The total derivative is a linear map from small input changes to small output changes. Once you choose bases, you can represent this map by a matrix. That matrix is the Jacobian.

In a neural network, the Jacobian calculates the first-order effect of an input perturbation on activations or logits. Without a fixed row and column convention, the order and shapes of matrix products can be reversed. This project places output components in rows and input components in columns.

## Learning objectives

By the end of this lesson, you should be able to:

- Construct the Jacobian of a vector-valued function with output rows and input columns.
- Relate the Jacobian's rows, columns, and shape to the function's inputs and outputs.
- Calculate directional output changes using a Jacobian-vector product.
- Calculate the Jacobian of a composition by multiplying matrices in the correct order.
- Find the Jacobians of an affine layer and an elementwise activation.
- Relate rank, kernel, and singular values to local sensitivity.
- Check a Jacobian calculation using finite differences.

## Prerequisite check

- Prerequisite lesson: [M03-10 Total derivative and differential](M03-10-total-derivative-differential.md)
- Prerequisite lesson: [M02-08 Kernel, image, and rank](../M02/M02-08-kernel-image-rank.md)
- Prerequisite lesson: [M02-13 Singular value decomposition](../M02/M02-13-singular-value-decomposition.md)
- Check question: Can you explain the total derivative as a linear map from an input displacement vector to an output displacement vector?
- Check question: Can you interpret a matrix's kernel, rank, and singular values in terms of amplification along different directions?

If the total derivative or SVD is unclear, review the prerequisite lessons first.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and conditions |
|---|---|---|---|
| $f:\mathbb R^n\to\mathbb R^m$ | `f maps R to the n into R to the m` | A function from an $n$-dimensional input to an $m$-dimensional output | $f=(f_1,\ldots,f_m)^\top$ |
| $\mathbf J_f(\mathbf x)$ | `the Jacobian of f at x` | The matrix of $Df(\mathbf x)$ in the standard bases | $m\times n$ |
| $J_{ij}$ | `J sub i j` | The partial derivative of output $f_i$ with respect to input $x_j$ | scalar |
| $\mathbf J_f(\mathbf x)\mathbf v$ | `the Jacobian of f at x times v` | The first-order output change in direction $\mathbf v$ | $m\times1$ |
| local sensitivity | `local sensitivity` | Output change due to a small input change near a base point | Specify the norm and direction |

## Core concept 1. The Jacobian is the coordinate matrix of the total derivative

Let

\[
f(\mathbf x)
=
\begin{bmatrix}
f_1(\mathbf x)\\
\vdots\\
f_m(\mathbf x)
\end{bmatrix}
\]

Throughout this lesson, assume that $f$ is differentiable at the base point $\mathbf x$. Collecting partial derivatives into an array and having that array represent the total derivative are distinct statements. The latter requires the full remainder condition from M03-10. In the standard bases, define the Jacobian by

\[
\mathbf J_f(\mathbf x)
=
\left[
\frac{\partial f_i}{\partial x_j}(\mathbf x)
\right]
\in\mathbb R^{m\times n}
\]

Writing out the rows gives

\[
\mathbf J_f(\mathbf x)
=
\begin{bmatrix}
\dfrac{\partial f_1}{\partial x_1}
&
\cdots
&
\dfrac{\partial f_1}{\partial x_n}
\\
\vdots
&
\ddots
&
\vdots
\\
\dfrac{\partial f_m}{\partial x_1}
&
\cdots
&
\dfrac{\partial f_m}{\partial x_n}
\end{bmatrix}_{\mathbf x}
\]

The output dimension $m$ is the number of rows, and the input dimension $n$ is the number of columns.

The subscript $\mathbf x$ below the matrix means that all partial derivatives are evaluated at the same base point. In $J_{ij}$, the index $i$ selects what you observe and $j$ selects what you vary. There are therefore $n$ columns, each containing the rates of change of all $m$ outputs with respect to one input coordinate.

## Core concept 2. Each row is the differential of an output component

The differential of the $i$th output $f_i:\mathbb R^n\to\mathbb R$ is a covector. Its row representation in standard coordinates is

\[
\begin{bmatrix}
\dfrac{\partial f_i}{\partial x_1}
&
\cdots
&
\dfrac{\partial f_i}{\partial x_n}
\end{bmatrix}
\]

The Jacobian stacks the $m$ output differentials as rows.

The $j$th column contains the rates of change of all output components when only input coordinate $x_j$ varies.

\[
\mathbf J_f(\mathbf x)\mathbf e_j
=
\frac{\partial f}{\partial x_j}(\mathbf x)
\in\mathbb R^m
\]

A row measures one scalar output; a column records the vector output change associated with one input direction.

For an arbitrary input change $\Delta\mathbf x$, the $i$th row calculates

\[
d(f_i)_{\mathbf x}(\Delta\mathbf x)
=\sum_{j=1}^n J_{ij}(\mathbf x)\Delta x_j
=\bigl(\mathbf J_f(\mathbf x)\Delta\mathbf x\bigr)_i
\]

One row takes the full input change and calculates the first-order change of one output component. Stacking these values in the order of output index $i$ gives the full output displacement vector. Conversely, setting $\Delta\mathbf x=\mathbf e_j$ gives $\Delta x_j=1$ with all other coefficients zero, leaving only the $j$th column.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A two-dimensional input, a three-by-two Jacobian, and a three-dimensional output with rows and columns highlighted](../../figures/assets/M03/M03-11-jacobian-rows-columns.svg)

<figcaption>A column represents the full output change due to one input direction. A row represents how one output component measures an input change.</figcaption>
</figure>

The blue first column collects the changes of all three output components when you move in direction $\mathbf e_1$. The orange first row reads how output $f_1$ alone changes under the same input change. Reading this array by columns gives changes of a vector-valued output; reading it by rows gives the differentials of scalar outputs.

## Core concept 3. The Jacobian calculates a local linearization

If $f$ is differentiable at $\mathbf x$, then

\[
f(\mathbf x+\Delta\mathbf x)
\approx
f(\mathbf x)
+
\mathbf J_f(\mathbf x)\Delta\mathbf x
\]

The shapes are

\[
\underbrace{\Delta\mathbf y}_{m\times1}
\approx
\underbrace{\mathbf J_f(\mathbf x)}_{m\times n}
\underbrace{\Delta\mathbf x}_{n\times1}
\]

The actual output change is $\Delta\mathbf y=f(\mathbf x+\Delta\mathbf x)-f(\mathbf x)$. The matrix product calculates the first-order term of this difference. To obtain the new output value, you must add the base output $f(\mathbf x)$. The expression does not mean that $\mathbf J_f(\mathbf x)\mathbf x$ equals the base output.

Writing the remainder as $\mathbf r_{\mathbf x}(\Delta\mathbf x)=\Delta\mathbf y-\mathbf J_f(\mathbf x)\Delta\mathbf x$, differentiability means that

\[
\lim_{\Delta\mathbf x\to\mathbf 0}
\frac{\|\mathbf r_{\mathbf x}(\Delta\mathbf x)\|_2}
{\|\Delta\mathbf x\|_2}=0
\]

In this limit, the base point and Jacobian remain fixed while the displacement shrinks. Changing the base point tests a different remainder condition. Differentiability at one point therefore does not provide a common allowable displacement size for all points. This condition alone also does not imply that the remainder is proportional to the square of the displacement size.

Applying the Jacobian to an input-change direction $\mathbf v$ gives

\[
\mathbf J_f(\mathbf x)\mathbf v
\]

This product is called a Jacobian-vector product (JVP). It gives the output rate of change in direction $\mathbf v$. M03-13 covers methods for calculating a JVP without constructing a large Jacobian.

For example, if the actual displacement is reduced to $t\mathbf v$, linearity gives the first-order output change $t\mathbf J_f(\mathbf x)\mathbf v$. Dividing by $t$ and taking the limit as $t\to0$ gives the rate of change $\mathbf J_f(\mathbf x)\mathbf v$. The finite difference in Example 4 checks this limit at a small nonzero $t$.

### Visual intuition: straightening a curved coordinate grid at one point

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A square input grid transformed into a curved output grid with one small neighborhood highlighted](../../figures/assets/M03/M03-11-nonlinear-grid.svg)

<figcaption>A nonlinear function can map a straight input grid to a curved grid. A small region around one point approaches a parallelogram.</figcaption>
</figure>

The equal-sized squares on the left bend in different directions and change size depending on their position on the right. A single matrix cannot represent the whole transformation. Within a sufficiently small neighborhood of the base point, such as the purple region, you can approximate the transformation by a linear map using only the first-order change of the curved boundary.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A nonlinear function and its Jacobian mapping a small input displacement to a local output displacement](../../figures/assets/M03/M03-11-local-linear-map.svg)

<figcaption>The actual function bends the two sides of the small input rectangle slightly. The Jacobian maps those sides to two sides of a parallelogram.</figcaption>
</figure>

The Jacobian maps the input rectangle's two sides $\mathbf e_1,\mathbf e_2$ to $\mathbf J_f(\mathbf x)\mathbf e_1$ and $\mathbf J_f(\mathbf x)\mathbf e_2$. The parallelogram formed by these two vectors is a first-order approximation of the small, curved output region. The Jacobian is a linear map between **changes** at the chosen base point $\mathbf x$, rather than a new model assigning output points to input points.

Changing the base point generally changes the Jacobian. You should therefore not interpret a collection of local linearizations at different points as one global matrix. Record both the point at which you calculate the Jacobian and the condition that $\Delta\mathbf x$ is sufficiently small.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two base points on a nonlinear curve with different tangent lines and a comparison of small and large displacement errors](../../figures/assets/M03/M03-11-basepoint-error.svg)

<figcaption>Different base points have different tangent lines and Jacobians. At a fixed base point, the error of the linear approximation grows as the displacement increases.</figcaption>
</figure>

The left panel shows that the same function has different slopes at base points $x_a$ and $x_b$. On the right, the tangent line and actual curve nearly coincide for a small displacement, while their difference becomes visible for a large displacement. Describing sensitivity using a Jacobian requires specifying both the base point and the change size.

## Core concept 4. A scalar function's Jacobian is the transpose of its gradient

When $m=1$, the Jacobian has shape $1\times n$.

\[
\mathbf J_f(\mathbf x)
=
\begin{bmatrix}
\dfrac{\partial f}{\partial x_1}
&
\cdots
&
\dfrac{\partial f}{\partial x_n}
\end{bmatrix}
\]

The gradient under the standard Euclidean inner product is a column vector, so

\[
\mathbf J_f(\mathbf x)
=
\nabla f(\mathbf x)^\top
\]

The Jacobian row contains the coordinates of the differential. The gradient column is the vector that represents this covector through the inner product.

## Core concept 5. The chain rule is a product of Jacobian matrices

Let

\[
f:\mathbb R^n\to\mathbb R^m,
\qquad
g:\mathbb R^m\to\mathbb R^p
\]

The Jacobian of the composition is

\[
\mathbf J_{g\circ f}(\mathbf x)
=
\mathbf J_g(f(\mathbf x))
\mathbf J_f(\mathbf x)
\]

The shapes are

\[
\underbrace{\mathbf J_{g\circ f}}_{p\times n}
=
\underbrace{\mathbf J_g}_{p\times m}
\underbrace{\mathbf J_f}_{m\times n}
\]

The Jacobian of the function closest to the input appears on the right.

## Core concept 6. Jacobians of common layers

For the affine function

\[
f(\mathbf x)=\mathbf W\mathbf x+\mathbf b
\]

the Jacobian at every $\mathbf x$ is

\[
\mathbf J_f(\mathbf x)=\mathbf W
\]

The bias does not vary with the input, so it does not appear in the Jacobian.

Changing the input by $\Delta\mathbf x$ and subtracting the two outputs gives $\mathbf W(\mathbf x+\Delta\mathbf x)+\mathbf b-(\mathbf W\mathbf x+\mathbf b)=\mathbf W\Delta\mathbf x$. Here, the remainder after the linear prediction is zero. The differentiated quantity is the input, not the weights or bias.

For the elementwise function

\[
\sigma(\mathbf z)
=
\begin{bmatrix}
\sigma(z_1)\\
\vdots\\
\sigma(z_m)
\end{bmatrix}
\]

the Jacobian is

\[
\mathbf J_\sigma(\mathbf z)
=
\operatorname{diag}
\left(
\sigma'(z_1),\ldots,\sigma'(z_m)
\right)
\]

Here, assume that every $\sigma'(z_i)$ exists. Output $\sigma(z_i)$ depends only on $z_i$, so its derivative with respect to $z_j$ is zero when $i\ne j$ and $\sigma'(z_i)$ when $i=j$. The absence of cross-coordinate terms gives a diagonal matrix.

Thus, for

\[
\mathbf h(\mathbf x)
=
\sigma(\mathbf W\mathbf x+\mathbf b)
\]

the Jacobian is

\[
\mathbf J_{\mathbf h}(\mathbf x)
=
\operatorname{diag}
\left(
\sigma'(\mathbf W\mathbf x+\mathbf b)
\right)
\mathbf W
\]

Within the diagonal-matrix notation, the derivative is applied to each vector component.

The matrix $\mathbf W$ on the right maps input changes to pre-activation changes. The diagonal matrix on the left multiplies each output coordinate by its rate of change. In matrix terms, it multiplies the entire $i$th row of $\mathbf W$ by $\sigma'(z_i)$.

## Core concept 7. Rank and singular values describe local directions

At a fixed point $\mathbf x$, view the Jacobian as a linear transformation.

- Directions in $\ker\mathbf J_f(\mathbf x)$ produce no first-order output change.
- The image $\operatorname{im}\mathbf J_f(\mathbf x)$ contains output change directions reachable to first order.
- The rank $\operatorname{rank}\mathbf J_f(\mathbf x)$ counts the independent first-order output change directions.

In the SVD

\[
\mathbf J_f(\mathbf x)
=
\mathbf U\boldsymbol\Sigma\mathbf V^\top
\]

the right singular vectors are input perturbation directions, and the singular values are first-order amplification rates. The largest singular value is the maximum local amplification rate under the Euclidean norm.

Writing the corresponding unit singular vectors as $\mathbf v_i,\mathbf u_i$ gives $\mathbf J_f(\mathbf x)\mathbf v_i=\sigma_i\mathbf u_i$. Moving the actual input by $t\mathbf v_i$ therefore gives the first-order output change $t\sigma_i\mathbf u_i$. A singular value specifies the magnitude of the rate of change along a unit input direction. For a finite input displacement, the actual output change also contains the remainder from the preceding sections.

These quantities depend on the base point and coordinate scaling. Orthogonal basis changes preserve singular values, but a general invertible reparameterization can change them.

## Example 1. A Jacobian with a $2$-dimensional input and $3$-dimensional output

### Problem

Find the Jacobian of

\[
f(x,y)
=
\begin{bmatrix}
x^2y\\
\sin x\\
x+y
\end{bmatrix}
\]

and calculate the first-order change at $(1,2)$ in direction $\mathbf v=(1,-1)^\top$.

### Solution

Taking the partial derivative of each output component with respect to each input gives

\[
\mathbf J_f(x,y)
=
\begin{bmatrix}
2xy&x^2\\
\cos x&0\\
1&1
\end{bmatrix}
\]

At $(1,2)$, this becomes

\[
\mathbf J_f(1,2)
=
\begin{bmatrix}
4&1\\
\cos1&0\\
1&1
\end{bmatrix}
\]

Multiplying by the direction vector gives

\[
\mathbf J_f(1,2)
\begin{bmatrix}
1\\-1
\end{bmatrix}
=
\begin{bmatrix}
3\\
\cos1\\
0
\end{bmatrix}
\]

### Meaning of the result

As the input moves in direction $(1,-1)$, the first-order rates of change of the three output components are $3$, $\cos1$, and 0.

## Example 2. The Jacobian of a ReLU layer

Let

\[
\mathbf W=
\begin{bmatrix}
1&2\\
-1&1
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}
2\\1
\end{bmatrix},
\qquad
\mathbf b=\mathbf 0
\]

and

\[
\mathbf h(\mathbf x)
=
\operatorname{ReLU}(\mathbf W\mathbf x)
\]

The pre-activation is

\[
\mathbf z
=
\mathbf W\mathbf x
=
\begin{bmatrix}
4\\-1
\end{bmatrix}
\]

Since $z_1>0$ and $z_2<0$,

\[
\mathbf J_{\operatorname{ReLU}}(\mathbf z)
=
\begin{bmatrix}
1&0\\
0&0
\end{bmatrix}
\]

The chain rule gives

\[
\mathbf J_{\mathbf h}(\mathbf x)
=
\begin{bmatrix}
1&0\\
0&0
\end{bmatrix}
\begin{bmatrix}
1&2\\
-1&1
\end{bmatrix}
=
\begin{bmatrix}
1&2\\
0&0
\end{bmatrix}
\]

The second output remains inactive under small changes near this point, while the first output transmits a first-order change. ReLU has no classical derivative at $z_i=0$, so a separate convention is needed there.

In Example 2, each ReLU slope multiplies an entire weight row. You can then compare the input and output directions that remain.

<figure class="lesson-figure" markdown="1">

![Positive ReLU preactivation four passes the first weight row one two while negative preactivation minus one zeros the second row](../../figures/assets/M03/M03-11-relu-row-gates.svg)

<figcaption>Because z₁>0, the first row remains unchanged. Because z₂<0, the second row becomes zero. This Jacobian gives local rates of change with respect to the input; a zero row does not mean that a feature is unused globally.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Unit input circle with amplified direction one two over square root five and kernel direction minus two one over square root five](../../figures/assets/M03/M03-11-relu-input-directions.svg)

<figcaption>The green and orange directions both have unit length, but the Jacobian maps them to different outputs. Along the orange direction, h₁+2h₂=0, so the first-order output change cancels.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![All unit inputs map to a segment on the first output axis with amplified green direction ending at square root five and orange kernel at zero](../../figures/assets/M03/M03-11-relu-rank-one-image.svg)

<figcaption>Under this Jacobian, the green input direction has output length √5, while the orange direction maps to the zero vector. Every first-order output change lies on the first output axis, so the rank is 1.</figcaption>

</figure>

## Example 3. Shape and values of a composition's Jacobian

Let

\[
f(x,y)
=
\begin{bmatrix}
x+y\\
xy
\end{bmatrix},
\qquad
g(u,v)=u^2+v
\]

Writing the expressions calculated in M03-10 in Jacobian notation gives

\[
\mathbf J_f(1,2)
=
\begin{bmatrix}
1&1\\
2&1
\end{bmatrix}
\]

\[
\mathbf J_g(f(1,2))
=
\begin{bmatrix}
6&1
\end{bmatrix}
\]

Therefore,

\[
\mathbf J_{g\circ f}(1,2)
=
\begin{bmatrix}
6&1
\end{bmatrix}
\begin{bmatrix}
1&1\\
2&1
\end{bmatrix}
=
\begin{bmatrix}
8&7
\end{bmatrix}
\]

In the matrix product in Example 3, the two components of the intermediate displacement vector must match the two columns of the next Jacobian.

<figure class="lesson-figure" markdown="1">

![Input change two by one passes through a two by two inner Jacobian then a one by two outer Jacobian producing a scalar change and combined row eight seven](../../figures/assets/M03/M03-11-chain-shape-route.svg)

<figcaption>The 2×2 Jacobian on the right first maps the input change to an intermediate change. The 1×2 Jacobian on the left then gives a scalar change. Their composition is a 1×2 row acting on the two original input components.</figcaption>

</figure>

## Example 4. Checking a JVP using finite differences

In Example 1, for a small $\varepsilon>0$,

\[
\frac{
f(\mathbf x+\varepsilon\mathbf v)-f(\mathbf x)
}{
\varepsilon
}
\approx
\mathbf J_f(\mathbf x)\mathbf v
\]

At $\mathbf x=(1,2)^\top$ with $\mathbf v=(1,-1)^\top$, the first output is

\[
f_1(1+\varepsilon,2-\varepsilon)
=(1+\varepsilon)^2(2-\varepsilon)
\]

Expanding gives

\[
(1+2\varepsilon+\varepsilon^2)(2-\varepsilon)
=
2+3\varepsilon-\varepsilon^3
\]

so

\[
\frac{f_1(\mathbf x+\varepsilon\mathbf v)-f_1(\mathbf x)}
{\varepsilon}
=
3-\varepsilon^2
\to3
\]

This agrees with the first component, 3, calculated by the Jacobian.

## Common misconceptions

### Misconception 1. Every source uses the same Jacobian row and column convention

Publications and software may use different conventions. This project places output components in rows and input components in columns.

### Misconception 2. A scalar function's Jacobian and gradient have the same shape

The Jacobian is a $1\times n$ row, and the Euclidean gradient is an $n\times1$ column. They are transposes of one another.

### Misconception 3. A zero Jacobian entry means that the feature is unused throughout the model

A zero entry means that, at the specified point, the first-order rate of change of that output component with respect to that input coordinate is zero. Effects may occur at other points, under finite changes, or through other output paths.

### Misconception 4. One large singular value proves global instability

A singular value gives a Euclidean local amplification rate at a specified point. Assessing global stability requires evidence across the input region and under finite perturbations.

## Exercises

### 1. Jacobian shape

State the shape of the Jacobian of $f:\mathbb R^4\to\mathbb R^3$ and explain the meaning of $J_{2,4}$.

<details>
<summary>Show solution</summary>

The output dimension is the number of rows, and the input dimension is the number of columns, so the shape is $3\times4$.

\[
J_{2,4}
=
\frac{\partial f_2}{\partial x_4}
\]

This is the local rate of change of the second output component with respect to the fourth input coordinate.

</details>

### 2. Calculating a Jacobian

Find the Jacobian of

\[
f(x,y)
=
\begin{bmatrix}
x^2+y\\
xy
\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

The partial derivatives of the first output are $(2x,1)$, and those of the second output are $(y,x)$. Thus,

\[
\mathbf J_f(x,y)
=
\begin{bmatrix}
2x&1\\
y&x
\end{bmatrix}
\]

</details>

### 3. Calculating a JVP

For the function in Exercise 2, calculate the JVP at $(1,2)$ for $\mathbf v=(3,-1)^\top$.

<details>
<summary>Show solution</summary>

Since

\[
\mathbf J_f(1,2)
=
\begin{bmatrix}
2&1\\
2&1
\end{bmatrix}
\]

the JVP is

\[
\mathbf J_f(1,2)\mathbf v
=
\begin{bmatrix}
2&1\\
2&1
\end{bmatrix}
\begin{bmatrix}
3\\-1
\end{bmatrix}
=
\begin{bmatrix}
5\\5
\end{bmatrix}
\]

</details>

### 4. Affine Jacobian

Given

\[
f(\mathbf x)=\mathbf W\mathbf x+\mathbf b,
\qquad
\mathbf W\in\mathbb R^{5\times3}
\]

state the Jacobian and its shape.

<details>
<summary>Show solution</summary>

\[
\mathbf J_f(\mathbf x)=\mathbf W
\]

Its shape is $5\times3$. The bias does not change with the input, so it contributes nothing to the partial derivatives.

</details>

### 5. Elementwise function

Find the Jacobian of

\[
f(x_1,x_2)
=
\begin{bmatrix}
x_1^2\\
e^{x_2}
\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

Each output depends only on its corresponding input, so

\[
\mathbf J_f(\mathbf x)
=
\begin{bmatrix}
2x_1&0\\
0&e^{x_2}
\end{bmatrix}
\]

</details>

### 6. Composition shapes

For $f:\mathbb R^2\to\mathbb R^4$ and $g:\mathbb R^4\to\mathbb R^3$, state the shapes of $\mathbf J_f$, $\mathbf J_g$, and $\mathbf J_{g\circ f}$, and write the multiplication order.

<details>
<summary>Show solution</summary>

Since

\[
\mathbf J_f\in\mathbb R^{4\times2},
\qquad
\mathbf J_g\in\mathbb R^{3\times4}
\]

the composition has Jacobian

\[
\mathbf J_{g\circ f}
=
\mathbf J_g\mathbf J_f
\in
\mathbb R^{3\times2}
\]

</details>

### 7. Critiquing a model claim

Critique the statement, “The input Jacobian has low rank, so the model uses only meaningful features.”

<details>
<summary>Show solution</summary>

Low rank means that first-order output changes at the specified input point lie in a low-dimensional subspace. It does not determine whether those directions represent human-defined semantic features, whether the rank persists at other inputs, or whether finite perturbations exhibit the same structure. Validation using multiple inputs and interventions is needed.

</details>

## Lesson summary

- The Jacobian represents the total derivative as a matrix with output rows and input columns.
- Each row is the differential of one scalar output component; each column is a vector rate of change with respect to one input coordinate.
- Multiplying the Jacobian by an input displacement vector calculates a local output change.
- A composition's Jacobian is the product of the outer function's Jacobian and the inner function's Jacobian.
- An affine layer's Jacobian is its weight matrix, and an elementwise activation's Jacobian is diagonal.
- Kernel, rank, and singular values describe first-order sensitivity at a specified point.

## Pass criteria

You pass if you can answer the following questions without consulting the material.

- Can you determine a Jacobian's shape from the function's input and output dimensions?
- Can you calculate a Jacobian with output rows and input columns?
- Can you calculate directional output changes using a JVP?
- Can you determine the matrix multiplication order for a composition's Jacobian?
- Can you find the Jacobians of an affine layer and an elementwise activation?
- Can you interpret a Jacobian's kernel, rank, and singular values locally?
- Can you check the calculation using finite differences?

## Next lesson

- [M03-12 Hessian](M03-12-hessian.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] The output-row, input-column convention is fixed.
- [x] The Jacobian's rows, columns, and shape are explained.
- [x] A composition's Jacobian and JVPs are calculated.
- [x] Jacobians of neural network layers are included.
- [x] Local sensitivity is distinguished from global claims.
- [x] Every exercise has a solution.
- [x] The strength of model interpretability claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters are checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
