---
id: "M02-05"
title: "Matrices as linear transformations"
part: 1
stage: "M02"
status: "complete"
prerequisites:
  - "M02-02"
  - "M02-04"
estimated_time: "105~130 minutes"
---

# M02-05. Matrices as linear transformations

## Why this lesson matters

Viewing a matrix only as a table of numbers may teach you how to multiply it, but can obscure what the computation does to space. A matrix $\mathbf A$ represents a function that sends an input vector to an output vector:

\[
T(\mathbf x)=\mathbf A\mathbf x
\]

Its columns show where the input coordinate axes go, and matrix multiplication represents the composition of successive transformations.

Neural-network weight matrices also mix, expand, or contract directions in an input representation. Adding a bias and a nonlinear function gives the full layer properties different from those of a linear transformation.

## Learning objectives

By the end of this lesson, you should be able to:

- Read a matrix as a function from $\mathbb R^n$ to $\mathbb R^m$.
- Test whether a transformation preserves vector addition and scalar multiplication.
- Interpret matrix columns as the images of standard basis vectors.
- Apply scaling, reflection, rotation, and projection matrices to small vectors.
- Connect matrix multiplication order to the order of composition.
- Distinguish linear transformations, affine transformations, and nonlinear operations.

## Prerequisite check

- Prerequisite lesson: [M02-02 Linear combinations and span](M02-02-linear-combinations-span.md)
- Prerequisite lesson: [M02-04 Matrices and matrix multiplication](M02-04-matrices-matrix-multiplication.md)
- Check question: Can you express $\mathbf A\mathbf x$ as a linear combination of the columns of $\mathbf A$?
- Check question: Can you explain why reversing the order of two matrices can change their product?

Review the prerequisite lessons first if linear combinations or matrix multiplication are unclear.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| $T:\mathbb R^n\to\mathbb R^m$ | `T maps R to the n into R to the m` | A transformation mapping input vectors to output vectors | Input dimension $n$, output dimension $m$ |
| $T(\mathbf x)=\mathbf A\mathbf x$ | `T of x equals A x` | A linear transformation represented by the matrix $\mathbf A$ | $\mathbf A\in\mathbb R^{m\times n}$ |
| $\mathbf e_j$ | `e sub j` | The standard basis vector with 1 only in component $j$ | $\mathbf e_j\in\mathbb R^n$ |
| $S\circ T$ | `S composed with T` | A transformation that applies $T$ and then $S$ | The output dimension must match the next input dimension. |
| Affine transformation | `affine transformation` | A linear transformation followed by addition of a fixed vector | $\mathbf x\mapsto\mathbf A\mathbf x+\mathbf b$ |

## Core concept 1. A matrix sends input vectors to output vectors

For $\mathbf A\in\mathbb R^{m\times n}$, define the transformation

\[
T:\mathbb R^n\to\mathbb R^m,
\qquad
T(\mathbf x)=\mathbf A\mathbf x
\]

The column count $n$ of $\mathbf A$ is the input dimension, and the row count $m$ is the output dimension.

The matrix need not be square. When $m<n$, the output has fewer coordinates; when $m>n$, it has more. A change in coordinate count alone does not determine how much information is preserved. Kernel and rank, introduced in M02-08, will let us assess that question.

## Core concept 2. A linear transformation preserves linear combinations

A transformation $T$ is linear if, for all vectors $\mathbf u,\mathbf v$ and all scalars $\alpha,\beta$,

\[
T(\alpha\mathbf u+\beta\mathbf v)
=
\alpha T(\mathbf u)+\beta T(\mathbf v)
\]

The left side first combines the inputs using the coefficients and then transforms the result. The right side first transforms each vector and then combines the results with the same coefficients. The two orders must agree for every choice of inputs and coefficients. Equality for one particular vector or one pair of coefficients does not establish linearity.

$T(\mathbf x)=\mathbf A\mathbf x$ satisfies this condition because matrix multiplication is distributive:

\[
\mathbf A(\alpha\mathbf u+\beta\mathbf v)
=
\alpha\mathbf A\mathbf u+\beta\mathbf A\mathbf v
\]

For the $i$th component, distributivity of real numbers gives

\[
\sum_j a_{ij}(\alpha u_j+\beta v_j)
=\alpha\sum_j a_{ij}u_j
+\beta\sum_j a_{ij}v_j
\]

This equality holds for every output component, so a matrix transformation preserves linear combinations. In particular,

\[
T(\mathbf 0)=\mathbf 0
\]

Setting both coefficients to 0 in the definition gives $T(\mathbf 0)$ on the left and the zero vector on the right. A transformation that sends the zero vector elsewhere is not linear. Conversely, fixing the zero vector alone does not guarantee linearity. The function $f(x)=x^2$ satisfies $f(0)=0$, but $f(1+1)=4$ differs from $f(1)+f(1)=2$.

The figure below compares adding two inputs before transforming them with transforming each input before adding the results. Both orders produce the same green output vector.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Adding two inputs before a matrix transformation reaches the same endpoint as adding their transformed images](../../figures/assets/M02/M02-05-preserved-combination.svg)

<figcaption>The input (1,1)ᵀ maps to (3,3)ᵀ. Adding the transformed directions (2,0)ᵀ and (1,3)ᵀ gives the same vector. This example illustrates preservation of a linear combination; the definition requires it for all inputs and coefficients.</figcaption>
</figure>

## Core concept 3. Matrix columns are the images of standard basis vectors

Let $\mathbf e_1,\ldots,\mathbf e_n$ be the standard basis vectors of $\mathbb R^n$, and let $\mathbf a_j$ be column $j$ of $\mathbf A$. Then

\[
T(\mathbf e_j)
=
\mathbf A\mathbf e_j
=
\mathbf a_j
\]

Only component $j$ of $\mathbf e_j$ is 1. In the column linear combination, only $\mathbf a_j$ remains; every other column is multiplied by 0.

Any input can be written as

\[
\mathbf x=x_1\mathbf e_1+\cdots+x_n\mathbf e_n
\]

Linearity gives

\[
T(\mathbf x)
=
x_1T(\mathbf e_1)+\cdots+x_nT(\mathbf e_n)
=
x_1\mathbf a_1+\cdots+x_n\mathbf a_n
\]

Knowing the images of the standard basis vectors determines the output for every input.

An input line $\mathbf x=t\mathbf v$ maps to $t\mathbf A\mathbf v$. If $\mathbf A\mathbf v\ne\mathbf 0$, these outputs form a line; if $\mathbf A\mathbf v=\mathbf 0$, the entire input line maps to the origin. A linear transformation does not bend a line's direction differently at different positions, but it can eliminate directions or map several directions onto one another.

### Visual intuition: the images of basis vectors determine the whole transformation

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two input basis vectors mapped to the columns of a matrix and recombined into the output](../../figures/assets/M02/M02-05-basis-transformation.svg)

<figcaption>When the input basis vectors e₁ and e₂ map to the matrix columns a₁ and a₂, any input x maps to the combination of those columns using the same coefficients.</figcaption>
</figure>

The blue and orange arrows each show the image of a basis vector. There is no need to memorize a separate transformation rule for the green input vector. By linearity, the input coefficients $x_1,x_2$ are reused to combine the two columns in the output.

The images of the standard basis vectors determine more than two arrows. Every point of the integer grid is a linear combination of $\mathbf e_1,\mathbf e_2$, so the images of the entire grid are determined as well.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A square coordinate grid mapped to a slanted grid by two matrix columns](../../figures/assets/M02/M02-05-grid-from-basis.svg)

<figcaption>The horizontal and vertical grid directions in the input map to the directions of the columns a₁ and a₂. The origin stays fixed, and parallel lines remain parallel after the transformation.</figcaption>
</figure>

The blue direction of the output grid follows the first column $\mathbf a_1$, and the orange direction follows the second column $\mathbf a_2$. Any input point $(x_1,x_2)$ is placed at $x_1\mathbf a_1+x_2\mathbf a_2$ in the output. Knowing the two matrix columns lets you predict the whole deformation without computing every grid point separately.

A linear transformation performed by one fixed matrix sends a line through the origin to a line or a point. When no direction disappears, as in this grid example, the straight grid is retained. A nonlinear function can change its transformation rule with position and send an input line to a curve. The Jacobian will later help us distinguish the transformation near one point from the whole mapping.

## Core concept 4. A diagonal matrix scales each coordinate axis

If

\[
\mathbf D=
\begin{bmatrix}
s_x&0\\
0&s_y
\end{bmatrix}
\]

then

\[
\mathbf D
\begin{bmatrix}x\\y\end{bmatrix}
=
\begin{bmatrix}s_xx\\s_yy\end{bmatrix}
\]

The first coordinate axis is scaled by $s_x$, and the second by $s_y$.

The off-diagonal entries are 0, so the new horizontal coordinate does not mix in the original vertical coordinate, nor does the new vertical coordinate mix in the original horizontal coordinate. The length factors along the axes are $|s_x|,|s_y|$, and the signs determine the directions of the corresponding axes. When the factors differ, a general vector's coordinate ratio can change, changing its direction. If a factor is 0, every value of that coordinate maps to 0, eliminating that direction in the output.

A negative $s_x$ or $s_y$ reverses the corresponding coordinate-axis direction. For example,

\[
\begin{bmatrix}
-1&0\\
0&1
\end{bmatrix}
\]

represents reflection across the $y$ axis.

The figure below shows a negative diagonal entry changing only the sign of the first coordinate. The two endpoints retain their vertical coordinate and lie on opposite sides of the reflection axis.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The diagonal matrix minus one one reflects three one to minus three one across the vertical coordinate axis](../../figures/assets/M02/M02-05-axis-reflection.svg)

<figcaption>(3,1)ᵀ becomes (-3,1)ᵀ. A negative factor reverses the corresponding axis direction. Here both absolute scale factors are 1, so length is preserved.</figcaption>
</figure>

## Core concept 5. Rotations and projections also have matrix representations

The matrix rotating the plane counterclockwise through angle $\theta$ is

\[
\mathbf R_\theta
=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}
\]

Rotating a horizontal direction of length 1 from the origin through $\theta$ places its endpoint at $(\cos\theta,\sin\theta)$. Cosine gives the horizontal coordinate and sine the vertical coordinate; their squares sum to 1. The vertical direction is $90^\circ$ ahead of the horizontal one, so its rotated image is $(-\sin\theta,\cos\theta)$. Placing these two images in columns gives the matrix above.

At $\theta=90^\circ$, cosine is 0 and sine is 1, giving

\[
\mathbf R_{90^\circ}
=
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}
\]

which sends $(x,y)$ to $(-y,x)$.

The matrix projecting onto the $x$ axis is

\[
\mathbf P_x
=
\begin{bmatrix}
1&0\\
0&0
\end{bmatrix}
\]

Since

\[
\mathbf P_x
\begin{bmatrix}x\\y\end{bmatrix}
=
\begin{bmatrix}x\\0\end{bmatrix}
\]

it removes the vertical component and retains the horizontal component.

Both columns of the rotation matrix have length 1 and inner product 0, preserving the lengths and orthogonality of the two standard directions. Expanding the squared length of the output also removes the cross term between the columns because their inner product is 0, leaving the original $x^2+y^2$. Projection retains the first column as $(1,0)^\top$ but sends the second to the zero vector. Inputs such as $(x,y_1)$ and $(x,y_2)$ that differ only vertically therefore map to the same $(x,0)$. The columns reveal the distinction between rotation, which mixes coordinates, and projection, which removes a coordinate.

Scaling, rotating, and projecting the same input vector change its length and direction in different ways.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![One vector scaled rotated and projected in three coordinate panels](../../figures/assets/M02/M02-05-standard-transforms.svg)

<figcaption>The dashed vector is the same input in each panel. A diagonal matrix changes lengths along the coordinate axes, a rotation matrix preserves lengths and angles, and a projection matrix removes the perpendicular component.</figcaption>
</figure>

Rotation mixes the two coordinates while preserving length. Projection discards a component in one direction, so several different inputs can reach the same output. Although all these transformations use matrices, the information preserved or lost differs between them.

The figure below sends two inputs differing only vertically to the same output. Applying the same projection again leaves the output unchanged because it is already on the horizontal axis.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two vectors with the same horizontal coordinate project to the same point and remain unchanged under a second projection](../../figures/assets/M02/M02-05-projection-collapse.svg)

<figcaption>Projecting (2,2)ᵀ and (2,-1)ᵀ onto the horizontal axis gives (2,0)ᵀ in both cases. Projecting this output again leaves it unchanged, illustrating Pₓ²=Pₓ in Example 3.</figcaption>
</figure>

## Core concept 6. A matrix product represents composition

Let

\[
T(\mathbf x)=\mathbf A\mathbf x,
\qquad
S(\mathbf y)=\mathbf B\mathbf y
\]

Applying $T$ first and then $S$ gives

\[
(S\circ T)(\mathbf x)
=
S(T(\mathbf x))
=
\mathbf B(\mathbf A\mathbf x)
=
(\mathbf B\mathbf A)\mathbf x
\]

The matrix of the transformation applied first is on the right. Geometrically, $\mathbf A\mathbf B$ and $\mathbf B\mathbf A$ differ because they apply the transformations in different orders.

The figure below applies the rotation and scaling from Example 2 in succession using the same coordinate scale. Checking each intermediate vector reveals the right-to-left computation order in the composite matrix $\mathbf D\mathbf R$.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three matched coordinate grids follow one three through ninety degree rotation to minus three one and doubling to minus six two](../../figures/assets/M02/M02-05-composition-stages.svg)

<figcaption>First rotate (1,3)ᵀ to obtain (-3,1)ᵀ, then double it to obtain (-6,2)ᵀ. Rotation preserves length; the subsequent scaling doubles it.</figcaption>
</figure>

## Core concept 7. Adding a bias gives an affine transformation

A neural-network layer's pre-activation has the form

\[
\mathbf z=\mathbf W\mathbf x+\mathbf b
\]

$\mathbf W\mathbf x$ is a linear transformation, and $\mathbf b$ translates every input by the same vector.

If $\mathbf b\ne\mathbf 0$, then

\[
T(\mathbf 0)=\mathbf b
\]

so the full transformation does not satisfy the conditions for linearity. It is called an affine transformation.

Addition of inputs also exposes the difference. Write $F(\mathbf x)=\mathbf W\mathbf x+\mathbf b$. The bias appears once in $F(\mathbf u+\mathbf v)$ but twice in $F(\mathbf u)+F(\mathbf v)$. For $\mathbf b\ne\mathbf 0$, these results differ, so linear combinations are not preserved. Adding the same fixed translation to every input is distinct from satisfying linearity.

Adding an activation function such as ReLU gives

\[
\mathbf h=\operatorname{ReLU}(\mathbf W\mathbf x+\mathbf b)
\]

which is generally a nonlinear function. The description of a matrix changing space linearly applies to the $\mathbf W\mathbf x$ part.

ReLU itself fixes the origin but does not preserve addition. For scalars, $\operatorname{ReLU}(1+(-1))=0$, whereas $\operatorname{ReLU}(1)+\operatorname{ReLU}(-1)=1$. Following the same linear rule on some interval does not make it a linear transformation over the whole input domain.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Linear affine and nonlinear maps compared through transformed coordinate grids](../../figures/assets/M02/M02-05-linear-affine-nonlinear.svg)

<figcaption>A linear transformation fixes the origin and sends a straight grid to straight lines. An affine transformation translates the same grid, whereas a nonlinear function can change grid directions differently at different positions.</figcaption>
</figure>

The left and middle grids both retain straight lines and parallelism. They differ in the image of the origin. On the right, the transformation's direction varies with position, so no single fixed matrix represents the whole mapping. This distinction explains why a Jacobian is later computed at each reference point.

## Example 1. Reading a transformation from matrix columns

Let

\[
\mathbf A=
\begin{bmatrix}
2&1\\
0&3
\end{bmatrix}
\]

The images of the standard basis vectors are

\[
T(\mathbf e_1)
=
\begin{bmatrix}2\\0\end{bmatrix},
\qquad
T(\mathbf e_2)
=
\begin{bmatrix}1\\3\end{bmatrix}
\]

These are the first and second columns of $\mathbf A$.

Since

\[
\mathbf x=
\begin{bmatrix}4\\-1\end{bmatrix}
=
4\mathbf e_1-\mathbf e_2
\]

we have

\[
T(\mathbf x)
=
4T(\mathbf e_1)-T(\mathbf e_2)
=
\begin{bmatrix}7\\-3\end{bmatrix}
\]

## Example 2. Rotation followed by scaling

Let the $90^\circ$ rotation matrix and the matrix scaling by two be

\[
\mathbf R=
\begin{bmatrix}0&-1\\1&0\end{bmatrix},
\qquad
\mathbf D=
\begin{bmatrix}2&0\\0&2\end{bmatrix}
\]

Rotating $\mathbf x=\begin{bmatrix}1\\3\end{bmatrix}$ first and then scaling gives

\[
\mathbf R\mathbf x
=
\begin{bmatrix}-3\\1\end{bmatrix}
\]

\[
\mathbf D(\mathbf R\mathbf x)
=
\begin{bmatrix}-6\\2\end{bmatrix}
\]

The composite matrix is

\[
\mathbf D\mathbf R
=
\begin{bmatrix}0&-2\\2&0\end{bmatrix}
\]

and produces the same output.

## Example 3. Applying the same projection twice gives the same result

If

\[
\mathbf P_x=
\begin{bmatrix}1&0\\0&0\end{bmatrix}
\]

then

\[
\mathbf P_x^2
=
\begin{bmatrix}1&0\\0&0\end{bmatrix}
\begin{bmatrix}1&0\\0&0\end{bmatrix}
=
\mathbf P_x
\]

The first projection already removes the $y$ component, so applying it again does not change the result.

## Example 4. Distinguishing a linear layer from its activation function

Let

\[
\mathbf W=
\begin{bmatrix}
1&-1\\
2&1
\end{bmatrix},
\qquad
\mathbf b=
\begin{bmatrix}1\\0\end{bmatrix}
\]

For $\mathbf x=\begin{bmatrix}2\\3\end{bmatrix}$,

\[
\mathbf W\mathbf x
=
\begin{bmatrix}-1\\7\end{bmatrix}
\]

and

\[
\mathbf z=\mathbf W\mathbf x+\mathbf b
=
\begin{bmatrix}0\\7\end{bmatrix}
\]

Applying ReLU gives

\[
\mathbf h=
\begin{bmatrix}0\\7\end{bmatrix}
\]

$\mathbf W$ represents a linear transformation. Including the bias makes the computation affine, and including ReLU makes the layer a nonlinear function.

## Common misconceptions

### Misconception 1. A matrix is only a table storing coordinates

A matrix represents a linear transformation in a particular basis. Its columns show the images of the input basis directions.

### Misconception 2. A linear transformation must have equal input and output dimensions

Linear transformations can be defined between spaces of different dimensions. The criterion is preservation of addition and scalar multiplication.

### Misconception 3. Calling $\mathbf W\mathbf x+\mathbf b$ linear leaves the conditions unchanged

If $\mathbf b\ne\mathbf 0$, the zero vector does not map to the zero vector. This computation is affine.

### Misconception 4. A nonlinear function automatically has a curved output space

A nonlinear function does not satisfy preservation of linear combinations. Discussing curvature of a space requires separate definitions of distance, coordinates, and manifold structure.

## Exercises

### 1. Input and output dimensions

For

\[
\mathbf A\in\mathbb R^{4\times3},
\qquad
T(\mathbf x)=\mathbf A\mathbf x
\]

give the domain and codomain of $T$ and state its input and output dimensions.

<details>
<summary>Show solution</summary>

The column count is the input dimension, and the row count is the output dimension.

\[
T:\mathbb R^3\to\mathbb R^4
\]

The input dimension is 3, and the output dimension is 4.

</details>

### 2. Testing linearity

Define $T:\mathbb R^2\to\mathbb R^2$ by

\[
T\left(
\begin{bmatrix}x\\y\end{bmatrix}
\right)
=
\begin{bmatrix}2x-y\\3y\end{bmatrix}
\]

Write its matrix and determine whether it is linear.

<details>
<summary>Show solution</summary>

\[
T\left(
\begin{bmatrix}x\\y\end{bmatrix}
\right)
=
\begin{bmatrix}
2&-1\\
0&3
\end{bmatrix}
\begin{bmatrix}x\\y\end{bmatrix}
\]

It is the product of a fixed matrix and a vector, so it preserves addition and scalar multiplication and is a linear transformation.

</details>

### 3. Images of standard basis vectors

For the transformation represented by

\[
\mathbf A=
\begin{bmatrix}
1&-2\\
3&4\\
0&5
\end{bmatrix}
\]

find $T(\mathbf e_1)$ and $T(\mathbf e_2)$.

<details>
<summary>Show solution</summary>

Multiplying by a standard basis vector selects the corresponding column:

\[
T(\mathbf e_1)
=
\begin{bmatrix}1\\3\\0\end{bmatrix},
\qquad
T(\mathbf e_2)
=
\begin{bmatrix}-2\\4\\5\end{bmatrix}
\]

</details>

### 4. Applying geometric transformations

For

\[
\mathbf R=
\begin{bmatrix}0&-1\\1&0\end{bmatrix},
\qquad
\mathbf P_x=
\begin{bmatrix}1&0\\0&0\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}2\\-3\end{bmatrix}
\]

find $\mathbf R\mathbf x$ and $\mathbf P_x\mathbf x$ and explain their geometric meanings.

<details>
<summary>Show solution</summary>

\[
\mathbf R\mathbf x
=
\begin{bmatrix}3\\2\end{bmatrix}
\]

This rotates the original vector counterclockwise through $90^\circ$.

\[
\mathbf P_x\mathbf x
=
\begin{bmatrix}2\\0\end{bmatrix}
\]

This removes the $y$ component and projects onto the $x$ axis.

</details>

### 5. Composition order

For

\[
\mathbf A=
\begin{bmatrix}2&0\\0&1\end{bmatrix},
\qquad
\mathbf B=
\begin{bmatrix}1&1\\0&1\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}1\\2\end{bmatrix}
\]

compute $\mathbf B\mathbf A\mathbf x$ and $\mathbf A\mathbf B\mathbf x$ and explain the application order.

<details>
<summary>Show solution</summary>

$\mathbf B\mathbf A\mathbf x$ applies $\mathbf A$ first:

\[
\mathbf A\mathbf x=
\begin{bmatrix}2\\2\end{bmatrix},
\qquad
\mathbf B\mathbf A\mathbf x=
\begin{bmatrix}4\\2\end{bmatrix}
\]

$\mathbf A\mathbf B\mathbf x$ applies $\mathbf B$ first:

\[
\mathbf B\mathbf x=
\begin{bmatrix}3\\2\end{bmatrix},
\qquad
\mathbf A\mathbf B\mathbf x=
\begin{bmatrix}6\\2\end{bmatrix}
\]

Different application orders produce different outputs.

</details>

### 6. Identifying an affine transformation

Suppose

\[
F(\mathbf x)=\mathbf A\mathbf x+\mathbf b
\]

with $\mathbf b\ne\mathbf 0$. Compute $F(\mathbf 0)$ and explain why $F$ is not linear.

<details>
<summary>Show solution</summary>

\[
F(\mathbf 0)
=
\mathbf A\mathbf 0+\mathbf b
=
\mathbf b
\ne
\mathbf 0
\]

A linear transformation must send the zero vector to the zero vector. Thus $F$ with $\mathbf b\ne\mathbf 0$ is affine but not linear.

</details>

### 7. Distinguishing claims about a neural-network layer

For

\[
\mathbf h=\operatorname{ReLU}(\mathbf W\mathbf x+\mathbf b)
\]

do the following.

1. Identify the linear, affine, and nonlinear parts.
2. Determine whether a column of $\mathbf W$ is the transformation result associated with a particular input coordinate.
3. Determine whether that column alone establishes that the coordinate causes the model output.

<details>
<summary>Show solution</summary>

$\mathbf W\mathbf x$ is linear. $\mathbf W\mathbf x+\mathbf b$ is affine, and the full function including ReLU is nonlinear.

Column $j$ of $\mathbf W$ is the result of applying the linear part to the standard basis input $\mathbf e_j$, so the second statement is correct.

Column values alone do not establish functional causality. You must check how the input direction appears in actual data, whether later layers use the change, and what interventions show.

</details>

## Lesson summary

- An $m\times n$ matrix represents a linear transformation from inputs in $\mathbb R^n$ to outputs in $\mathbb R^m$.
- Linear transformations preserve linear combinations and send the zero vector to the zero vector.
- Column $j$ is the image of the $j$th standard basis vector.
- Scaling, reflection, rotation, and projection can be represented by matrices.
- In composition, the matrix applied first is on the right of the product.
- Adding a bias gives an affine computation; a layer including an activation function is generally nonlinear.

## Pass criteria

You pass if you can answer these questions without consulting the material.

- Can you read input and output dimensions from a matrix shape?
- Can you test linearity using preservation of linear combinations?
- Can you explain matrix columns as images of standard basis vectors?
- Can you apply small rotation, scaling, and projection matrices to vectors?
- Can you connect matrix multiplication order to composition order?
- Can you distinguish linear, affine, and nonlinear functions?

## Next lesson

- [M02-06 Linear systems and inverse matrices](M02-06-linear-systems-inverse.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] The domain, codomain, and shape of a linear transformation are connected.
- [x] Preservation of linear combinations and the zero-vector condition are explained.
- [x] Matrix columns are interpreted as images of standard basis vectors.
- [x] Geometric-transformation and composition examples have been checked.
- [x] Every exercise has a solution.
- [x] The linear part is distinguished from causal claims about the full model.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
