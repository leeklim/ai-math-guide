---
id: "M01-11"
title: "Directional derivatives and the gradient"
part: 1
stage: "M01"
status: "complete"
prerequisites:
  - "M00-09"
  - "M01-10"
estimated_time: "105~125 minutes"
---

# M01-11. Directional derivatives and the gradient

## Why this lesson matters

A partial derivative measures change along one coordinate axis. In practice, several input or parameter coordinates may change together. A directional derivative measures how a scalar-valued function changes when moving in a selected direction, while the gradient collects all coordinate partial derivatives into one vector.

Gradients appear repeatedly in backpropagation, optimization, and input-sensitivity analysis. Their magnitude and direction depend on coordinates and units, so a large component should not be read directly as causal importance.

## Learning objectives

After this lesson, you will be able to:

- Distinguish a direction vector from a unit vector.
- Define a directional derivative as a single-variable derivative along a path.
- Calculate the gradient by collecting partial derivatives into a column vector.
- Calculate a directional derivative as the inner product of the gradient and a direction vector.
- Explain directions of steepest ascent and descent and the limitations of gradients.

## Prerequisite check

- Prerequisite lesson: [M00-09. Shapes of scalars, vectors, and matrices](../M00/M00-09-scalars-vectors-matrices-shape.md)
- Prerequisite lesson: [M01-10. Multiple variables and partial derivatives](M01-10-multivariable-partial-derivatives.md)
- Check question: Can you explain why the inner product of two vectors is a scalar?
- Check question: Can you calculate both partial derivative functions of $f(x,y)$?

Review the prerequisites first if vector shapes or partial derivatives are unclear.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and conditions |
|---|---|---|---|
| $\mathbf x$ | `x` | A column vector of input coordinates | $\mathbf x\in\mathbb R^n$ |
| $\mathbf v$ | `v` | A column vector specifying a direction of movement in the input space | $\mathbf v\in\mathbb R^n$ |
| $\|\mathbf v\|_2$ | `the L two norm of v` | The Euclidean length of the direction vector | For a unit direction, $\|\mathbf v\|_2=1$ |
| $D_{\mathbf v}f(\mathbf x)$ | `the directional derivative of f at x along v` | The rate of change at point $\mathbf x$ along direction $\mathbf v$ | This lesson mainly uses unit vectors |
| $\nabla_{\mathbf x}f$ | `the gradient of f with respect to x` | A column vector of coordinate partial derivatives | $\nabla_{\mathbf x}f\in\mathbb R^n$ |
| $\nabla f(\mathbf x)^\top\mathbf v$ | `the gradient of f at x transpose times v` | The inner product of the gradient and direction vector | The result is a scalar |

## Core concept 1. A direction vector sets the relative changes of coordinates

Moving from point

\[
\mathbf x=
\begin{bmatrix}
x_1\\
x_2
\end{bmatrix}
\]

by parameter amount $t$ along direction

\[
\mathbf v=
\begin{bmatrix}
v_1\\
v_2
\end{bmatrix}
\]

gives the new point

\[
\mathbf x+t\mathbf v
=
\begin{bmatrix}
x_1+tv_1\\
x_2+tv_2
\end{bmatrix}
\]

Here $v_1$ and $v_2$ set the relative changes of the two coordinates.

A vector of length $1$ is called a unit vector.

\[
\|\mathbf v\|_2
=
\sqrt{v_1^2+v_2^2}
=1
\]

Using unit vectors for directional derivatives separates direction from movement speed. A vector of length $2$ moves twice as far per unit of $t$, even along the same direction.

Collinear arrows with different lengths give different travel distances for the same t.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Collinear vectors of lengths one and two with the unit vector ending on a unit circle](../../figures/assets/M01/M01-11-unit-and-speed.svg)
  <figcaption>The green vector (0.6,0.8) has length 1, and the blue vector (1.2,1.6) has length 2. Their direction is the same, but increasing t by 1 moves twice as far along the blue path. The gray dashed circle marks the endpoints of vectors of length 1.</figcaption>
</figure>

## Core concept 2. A directional derivative differentiates a single-variable path

For a scalar-valued function $f:\mathbb R^n\to\mathbb R$, fix point $\mathbf x$ and direction $\mathbf v$. Define the single-variable function

\[
g(t)=f(\mathbf x+t\mathbf v)
\]

Its derivative at $t=0$ is the directional derivative.

\[
D_{\mathbf v}f(\mathbf x)
\coloneqq
g'(0)
\]

In limit notation,

\[
D_{\mathbf v}f(\mathbf x)
=
\lim_{t\to0}
\frac{f(\mathbf x+t\mathbf v)-f(\mathbf x)}{t}
\]

The result is a scalar rate of change at the selected point and direction.

Because $g(0)=f(\mathbf x)$, $t=0$ is the starting point. Varying $t$ moves the entire input point along the path. Negative $t<0$ approaches from the side opposite to $\mathbf v$. The limit's denominator is the change $t$ in the path parameter, not an input vector. With a unit direction, the magnitude of $t$ equals the distance traveled; a general direction vector changes the travel speed by its length.

Drawing the input path from Example 1 and then plotting its output as a function of t shows which graph's slope is the directional derivative.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![A straight path through the two-dimensional input point one minus one above its scalar output curve with tangent slope minus three point six](../../figures/assets/M01/M01-11-input-path-and-rate.svg)
  <figcaption>The upper plot is a path in the input plane along which x and y change together. The lower plot is the output g(t) obtained by passing those inputs to f. Its slope −3.6 at starting point t=0 is the directional derivative, a different quantity from the upper arrow's coordinate components.</figcaption>
</figure>

## Core concept 3. The gradient is a column vector of coordinate partial derivatives

The gradient of $f:\mathbb R^n\to\mathbb R$ is

\[
\nabla_{\mathbf x}f(\mathbf x)
=
\begin{bmatrix}
\frac{\partial f}{\partial x_1}(\mathbf x)\\
\vdots\\
\frac{\partial f}{\partial x_n}(\mathbf x)
\end{bmatrix}
\in\mathbb R^n
\]

This textbook writes gradients as column vectors.

For a two-variable function,

\[
\nabla f(x,y)
=
\begin{bmatrix}
f_x(x,y)\\
f_y(x,y)
\end{bmatrix}
\]

Each gradient component is the rate of change along its corresponding coordinate axis.

Placing the two coordinate partial derivatives as vector components creates one arrow with a direction and length.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![A gradient vector with horizontal component three and vertical component four and Euclidean length five](../../figures/assets/M01/M01-11-gradient-components.svg)
  <figcaption>The gradient (3,4) from Example 2 is drawn in vector-component coordinates. The horizontal and vertical dashed lengths are the partial derivatives 3 and 4; the purple arrow has length 5. The origin anchors the vector's tail and is not the evaluation point of the original function.</figcaption>
</figure>

## Core concept 4. A directional derivative is the inner product of gradient and direction

If $f$ is differentiable at point $\mathbf x$, then

\[
D_{\mathbf v}f(\mathbf x)
=
\nabla f(\mathbf x)^\top\mathbf v
\]

For two variables, this expands to

\[
D_{\mathbf v}f(x,y)
=
f_x(x,y)v_1
+
f_y(x,y)v_2
\]

Differentiability in several variables means that one first-order expression approximates the output change for every small input change. The approximation error must become small even relative to the size of the input change. For two variables, this expression is

\[
\Delta f\approx f_x(x,y)\Delta x+f_y(x,y)\Delta y
\]

Along the path in direction $\mathbf v$, we have $\Delta x=tv_1$ and $\Delta y=tv_2$, so the right-hand side becomes $t[f_xv_1+f_yv_2]$. Dividing by $t$ and taking the limit as $t\to0$ gives the directional-derivative formula. The existence of coordinate partial derivatives alone does not imply that this approximation holds for every small change, so the differentiability condition must be retained.

Multiply each partial derivative by that coordinate's contribution to the direction, then sum. Substituting the coordinate unit vectors

\[
\mathbf e_1=
\begin{bmatrix}1\\0\end{bmatrix},
\qquad
\mathbf e_2=
\begin{bmatrix}0\\1\end{bmatrix}
\]

gives $f_x$ and $f_y$, respectively. Partial derivatives are the coordinate-axis cases of directional derivatives.

## Core concept 5. The gradient indicates the direction of steepest ascent

Among unit vectors $\mathbf v$, the gradient direction maximizes the directional derivative

\[
\nabla f(\mathbf x)^\top\mathbf v
\]

If the gradient is not 0, the unit direction of steepest ascent is

\[
\frac{\nabla f(\mathbf x)}{\|\nabla f(\mathbf x)\|_2}
\]

and the maximum directional derivative is

\[
\|\nabla f(\mathbf x)\|_2
\]

Let $\mathbf u$ be the vector obtained by dividing the gradient at this point, which is not $0$, by its norm to give length $1$. For two unit vectors $\mathbf u,\mathbf v$, summing the squared coordinate differences gives

\[
0\le\|\mathbf u-\mathbf v\|_2^2
=2-2\mathbf u^\top\mathbf v
\]

Thus $\mathbf u^\top\mathbf v\le1$. The directional derivative is $\|\nabla f\|_2\mathbf u^\top\mathbf v$, so its maximum cannot exceed $\|\nabla f\|_2$. Choosing $\mathbf v=\mathbf u$ gives inner product $1$ and attains that maximum. Fixing unit length makes directions comparable; this differs from obtaining a large rate by freely increasing the vector's length.

The opposite direction

\[
-\frac{\nabla f(\mathbf x)}{\|\nabla f(\mathbf x)\|_2}
\]

is the direction of steepest descent. This is a local result under the chosen coordinates and Euclidean length.

Holding the vector length at 1 and rotating its direction through a full turn shows the inner product becoming positive, 0, and negative.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Directional derivative versus unit-vector angle for gradient three four with maximum five and minimum minus five](../../figures/assets/M01/M01-11-direction-angle.svg)
  <figcaption>For gradient (3,4), a unit vector in the same direction gives rate 5, while the opposite direction gives −5. Perpendicular directions between them give 0. The horizontal axis is the angle of the unit direction, not travel distance.</figcaption>
</figure>

## Core concept 6. Gradient descent moves in the opposite direction

Let $\boldsymbol\theta\in\mathbb R^n$ be a parameter vector and $\mathcal L(\boldsymbol\theta)$ its loss. The basic gradient-descent update is

\[
\boldsymbol\theta_{\mathrm{new}}
=
\boldsymbol\theta
-
\eta\nabla_{\boldsymbol\theta}\mathcal L(\boldsymbol\theta),
\qquad \eta>0
\]

Here $\eta$ is the learning rate.

Writing the current gradient as $\mathbf g=\nabla\mathcal L(\boldsymbol\theta)$ gives displacement $\Delta\boldsymbol\theta=-\eta\mathbf g$. Applying the preceding first-order change formula gives

\[
\Delta\mathcal L
\approx\mathbf g^\top\Delta\boldsymbol\theta
=-\eta\mathbf g^\top\mathbf g
=-\eta\|\mathbf g\|_2^2
\]

If $\eta>0$ and $\mathbf g\ne\mathbf0$, this first-order change is negative. Each coordinate moves with the opposite sign to its partial derivative, and the total displacement has length $\eta\|\mathbf g\|_2$. The update does not subtract the unit vector of steepest descent itself. The gradient's magnitude also determines the step size.

This update uses the Euclidean direction of fastest local loss decrease at the current point. A large learning rate can move beyond the range where local information is useful, and a point with gradient 0 is not guaranteed to be a minimum.

Even along the same descent direction, different learning rates can produce different losses at the destination.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![A quadratic single-parameter loss with small and large gradient steps producing lower and higher losses respectively](../../figures/assets/M01/M01-11-step-size-risk.svg)
  <figcaption>For the illustrative loss θ², the gradient at θ=1 is 2. Learning rate 0.2 moves to θ=0.6 and reduces the loss to 0.36. Rate 1.2 overshoots to θ=−1.4, giving loss 1.96. Both movements initially follow the negative-gradient direction.</figcaption>
</figure>

## Core concept 7. Gradient magnitude depends on coordinate units

Changing input coordinate $x_i$ to $z_i=cx_i$ expresses the same physical change using different numbers. Here $c$ is a fixed constant other than $0$. To express the same function in the new coordinate, substitute $z_i/c$ for $x_i$ in the original expression. The derivative of this inner function with respect to $z_i$ is $1/c$, so the chain rule gives

\[
\frac{\partial f}{\partial z_i}
=
\frac{1}{c}
\frac{\partial f}{\partial x_i}
\]

Changing coordinate scale $c$ therefore changes the gradient components and norm.

Comparing input components with different units using only absolute gradient values mixes in scale effects. State input standardization, allowed perturbation sizes, and the norm being used together.

## Core concept 8. The gradient is local first-order sensitivity

The gradient collects first-order information about small changes at a selected point. A large component means high local sensitivity in that coordinate direction.

This information does not determine the output after a finite change, behavior across the data distribution, or causal effects. If input components depend on one another, moving only one component may also leave the region of actual data.

## Example 1. Calculating a directional derivative

For

\[
f(x,y)=x^2+3y^2
\]

the gradient is

\[
\nabla f(x,y)
=
\begin{bmatrix}
2x\\
6y
\end{bmatrix}
\]

At point $(1,-1)$,

\[
\nabla f(1,-1)
=
\begin{bmatrix}
2\\
-6
\end{bmatrix}
\]

For the unit direction

\[
\mathbf v=
\begin{bmatrix}
3/5\\
4/5
\end{bmatrix}
\]

the directional derivative is

\[
D_{\mathbf v}f(1,-1)
=
\begin{bmatrix}2&-6\end{bmatrix}
\begin{bmatrix}3/5\\4/5\end{bmatrix}
=
\frac65-\frac{24}{5}
=
-\frac{18}{5}
\]

The function initially decreases when moving in this direction.

## Example 2. Directions of steepest ascent and descent

Suppose that at a point,

\[
\nabla f=
\begin{bmatrix}
3\\
4
\end{bmatrix}
\]

Its norm is

\[
\|\nabla f\|_2=5
\]

The unit direction of steepest ascent is

\[
\begin{bmatrix}
3/5\\
4/5
\end{bmatrix}
\]

The unit direction of steepest descent is its opposite. The steepest-ascent directional derivative is $5$.

## Example 3. A saddle point with gradient 0

The gradient of

\[
f(x,y)=x^2-y^2
\]

is

\[
\nabla f(x,y)
=
\begin{bmatrix}
2x\\
-2y
\end{bmatrix}
\]

At the origin, the gradient is 0. However, on the $x$-axis, $f(x,0)=x^2\ge0$, while on the $y$-axis, $f(0,y)=-y^2\le0$. The origin is neither a local minimum nor a local maximum. Such a point is called a saddle point.

Looking at both coordinate slices, rather than just their horizontal tangents at the origin, shows why a saddle point is not an extremum.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Upward and downward quadratic coordinate slices of a saddle function sharing zero tangent slopes at the origin](../../figures/assets/M01/M01-11-saddle-slices.svg)
  <figcaption>The x-axis slice rises to values above the origin, while the y-axis slice falls to values below it. Both have slope 0 at the origin. A gradient of 0 alone therefore cannot identify a minimum or maximum.</figcaption>
</figure>

## Example 4. A two-parameter loss update

Suppose the current parameters and loss gradient are

\[
\boldsymbol\theta=
\begin{bmatrix}1\\-2\end{bmatrix},
\qquad
\nabla\mathcal L=
\begin{bmatrix}4\\-1\end{bmatrix}
\]

and the learning rate is $\eta=0.1$.

\[
\boldsymbol\theta_{\mathrm{new}}
=
\begin{bmatrix}1\\-2\end{bmatrix}
-
0.1
\begin{bmatrix}4\\-1\end{bmatrix}
=
\begin{bmatrix}0.6\\-1.9\end{bmatrix}
\]

This calculation determines the update direction. Whether the loss decreased must be checked by evaluating it at the new point.

The parameter plane shows the signs of the coordinate updates and the combined displacement.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![A parameter-plane step from one minus two to zero point six minus one point nine with displacement minus zero point four plus zero point one](../../figures/assets/M01/M01-11-parameter-update.svg)
  <figcaption>The first coordinate decreases by 0.4, and the second increases by 0.1. The arrow shows their simultaneous update. No loss surface is drawn, so the figure does not show a decrease in loss between the starting and ending points.</figcaption>
</figure>

## Common misconceptions

### Misconception 1. The direction vector's length does not affect the directional derivative

Vector length changes the distance traveled per unit of $t$. Use unit vectors when comparing only directions.

### Misconception 2. The gradient is a scalar

The gradient of a scalar-valued function is a vector with as many components as input coordinates. A directional derivative is the scalar obtained by taking the inner product of the gradient and a direction vector.

### Misconception 3. A gradient of 0 means a local minimum

It only identifies a stationary point. The point may be a local maximum or a saddle point.

### Misconception 4. The largest gradient component is the most important cause

A gradient component is a local sensitivity dependent on coordinate units and the evaluation point. Causal importance requires intervention evidence.

### Misconception 5. The gradient gives the direction of steepest ascent even for a large movement

Steepest ascent is a property of the local first-order change at the current point. Curvature can alter the relationship between directions after moving farther away.

## Exercises

### 1. Checking a unit direction

Determine whether

\[
\mathbf v=
\begin{bmatrix}3/5\\4/5\end{bmatrix}
\]

is a unit vector.

<details>
<summary>Show solution</summary>

Since

\[
\|\mathbf v\|_2
=
\sqrt{(3/5)^2+(4/5)^2}
=
\sqrt{25/25}
=1
\]

it is a unit vector.

</details>

### 2. Calculating a gradient

Find the gradient of

\[
f(x,y)=x^2+2xy+4y^2
\]

<details>
<summary>Show solution</summary>

Since

\[
\frac{\partial f}{\partial x}=2x+2y,
\qquad
\frac{\partial f}{\partial y}=2x+8y
\]

we have

\[
\nabla f(x,y)
=
\begin{bmatrix}
2x+2y\\
2x+8y
\end{bmatrix}
\]

</details>

### 3. Calculating a directional derivative

For the function in Exercise 2, find the directional derivative at point $(1,0)$ along unit direction $\mathbf v=(0,1)^\top$.

<details>
<summary>Show solution</summary>

\[
\nabla f(1,0)
=
\begin{bmatrix}2\\2\end{bmatrix}
\]

Therefore,

\[
D_{\mathbf v}f(1,0)
=
\begin{bmatrix}2&2\end{bmatrix}
\begin{bmatrix}0\\1\end{bmatrix}
=2
\]

This is the $y$ coordinate-axis direction, so the result equals $f_y(1,0)$.

</details>

### 4. The unit direction of steepest ascent

At a point,

\[
\nabla f=
\begin{bmatrix}-6\\8\end{bmatrix}
\]

Find the unit direction of steepest ascent and the maximum directional derivative.

<details>
<summary>Show solution</summary>

The gradient norm is

\[
\sqrt{(-6)^2+8^2}=10
\]

The unit direction of steepest ascent is

\[
\frac{1}{10}
\begin{bmatrix}-6\\8\end{bmatrix}
=
\begin{bmatrix}-3/5\\4/5\end{bmatrix}
\]

and the maximum directional derivative is $10$.

</details>

### 5. A gradient-descent update

Given

\[
\boldsymbol\theta=
\begin{bmatrix}2\\1\end{bmatrix},
\qquad
\nabla\mathcal L=
\begin{bmatrix}3\\-4\end{bmatrix},
\qquad
\eta=0.2
\]

calculate one gradient-descent update.

<details>
<summary>Show solution</summary>

\[
\boldsymbol\theta_{\mathrm{new}}
=
\begin{bmatrix}2\\1\end{bmatrix}
-
0.2
\begin{bmatrix}3\\-4\end{bmatrix}
\]

\[
=
\begin{bmatrix}2-0.6\\1+0.8\end{bmatrix}
=
\begin{bmatrix}1.4\\1.8\end{bmatrix}
\]

</details>

### 6. Interpreting a gradient of 0

Find the gradient of $f(x,y)=x^2-y^2$ at the origin and determine whether the origin is a minimum.

<details>
<summary>Show solution</summary>

Since

\[
\nabla f(x,y)=
\begin{bmatrix}2x\\-2y\end{bmatrix}
\]

we have $\nabla f(0,0)=\mathbf0$. However, moving along the $x$-axis gives positive function values, and moving along the $y$-axis gives negative ones. Both smaller and larger values occur near the origin, so it is not a minimum. The origin is a saddle point.

</details>

### 7. Assessing an input-gradient claim

For one image, a particular pixel has the largest input-gradient component. A researcher claims, “This pixel is the key cause of the prediction in every image.” Explain what the result supports and what further checks are needed.

<details>
<summary>Show solution</summary>

The result supports the statement that this coordinate has the largest absolute local sensitivity for the selected image and output at the current model state. Pixel units and the comparison criterion also need to be checked.

Behavior on other images, effects of finite pixel changes, and causal necessity remain unestablished. Further work requires examining the distribution across inputs, allowable perturbations, and pixel-intervention experiments.

</details>

## Lesson summary

- The directional derivative is the derivative of $g(t)=f(\mathbf x+t\mathbf v)$ at $t=0$.
- The gradient is a column vector of coordinate partial derivatives.
- For a differentiable function, $D_{\mathbf v}f=\nabla f^\top\mathbf v$.
- Among unit directions, the gradient gives local steepest ascent, and its opposite gives local steepest descent.
- The gradient is local first-order sensitivity dependent on coordinate scale and the evaluation point.

## Pass criteria

You have passed this lesson if you can answer these questions without consulting the material:

- Can you distinguish direction vectors from unit direction vectors?
- Can you define a directional derivative as a single-variable path derivative?
- Can you collect partial derivatives into a column-vector gradient?
- Can you calculate a directional derivative from the inner product of gradient and direction?
- Can you explain gradient-descent directions and the limitations of gradient-based importance claims?

## Next lesson

- [M01-12. Taylor approximation](M01-12-taylor-approximation.md)

## Author checklist

- [x] The learning objectives describe observable actions.
- [x] Direction vectors, directional derivatives, and gradients are defined before use.
- [x] Gradients are consistently written as column vectors.
- [x] Examples of directional derivatives, steepest directions, and updates have been checked.
- [x] Every exercise has a solution.
- [x] Local sensitivity is distinguished from claims of causal importance.
- [x] The glossary and notation rules are followed.
- [x] Hessians and Jacobians are not required as prerequisites.
- [x] Internal links and mathematical delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
