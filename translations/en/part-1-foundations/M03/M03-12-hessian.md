---
id: "M03-12"
title: "Hessian"
part: 1
stage: "M03"
status: "complete"
prerequisites:
  - "M01-12"
  - "M03-08"
  - "M03-11"
estimated_time: "125~150 minutes"
---

# M03-12. Hessian

## Why this lesson matters

The gradient describes a scalar function's first-order change at a point. Understanding how the gradient changes with the input requires second derivatives. The Hessian collects a scalar function's second partial derivatives into a matrix, describing second-order curvature near a point.

The Hessian of a training loss is used to investigate curvature along parameter directions, flat directions, and saddle structure. Its entries and eigenvalues depend on parameter coordinates and scaling. A Hessian at one point does not establish the shape of the entire loss landscape or the training path.

## Learning objectives

After completing this lesson, you will be able to:

- Construct a scalar function's Hessian as a matrix of second partial derivatives.
- Explain Hessian symmetry under continuity of mixed partial derivatives.
- Connect the second differential to the bilinear form represented by the Hessian.
- Calculate second-order Taylor approximations and directional curvature.
- Use Hessian eigenvalues at critical points to assess minimum, maximum, and saddle candidates.
- Calculate a Hessian-vector product and explain its role for large Hessians.
- Limit Hessian-based claims according to coordinate and base-point dependence.

## Prerequisite check

- Prerequisite lesson: [M01-12 Taylor approximation](../M01/M01-12-taylor-approximation.md)
- Prerequisite lesson: [M03-08 Bilinear forms and quadratic forms](M03-08-bilinear-quadratic-forms.md)
- Prerequisite lesson: [M03-11 Jacobian](M03-11-jacobian.md)
- Check: Can you calculate a scalar function's gradient?
- Check: Can you evaluate a quadratic form $\mathbf v^\top\mathbf A\mathbf v$ and interpret the eigenvalue signs of a symmetric matrix?
- Check: Can you explain that the Jacobian represents a vector-valued function's total derivative as a matrix?

Review the prerequisite lessons first if gradients, quadratic forms, or Jacobians are unclear.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape |
|---|---|---|---|
| $f:\mathbb R^n\to\mathbb R$ | `f maps R to the n into R` | A scalar-output function | A loss, for example |
| $\mathbf H_f(\mathbf x)$ | `the Hessian of f at x` | The matrix of second partial derivatives of $f$ | $n\times n$ |
| $H_{ij}$ | `H sub i j` | $\partial^2f/\partial x_i\partial x_j$ | Scalar |
| $d^2f_{\mathbf x}$ | `the second differential of f at x` | A bilinear form mapping two displacement vectors to a scalar | Order 2 |
| $\mathbf v^\top\mathbf H_f\mathbf v$ | `v transpose H sub f v` | The second-order rate of change along $\mathbf v$ | Scalar |
| HVP | `H V P` | Hessian-vector product | $\mathbf H_f(\mathbf x)\mathbf v$ |

When needed to distinguish it from an activation matrix, $\mathbf H_f$ is explicitly labeled as the Hessian in the text.

## Core concept 1. The Hessian is the Jacobian of the gradient

For a twice-differentiable scalar function

\[
f:\mathbb R^n\to\mathbb R
\]

define its Hessian by

\[
\mathbf H_f(\mathbf x)
=
\left[
\frac{\partial^2f}
{\partial x_i\partial x_j}
(\mathbf x)
\right]
\in\mathbb R^{n\times n}
\]

Writing the gradient as

\[
\nabla f(\mathbf x)
=
\begin{bmatrix}
\dfrac{\partial f}{\partial x_1}\\
\vdots\\
\dfrac{\partial f}{\partial x_n}
\end{bmatrix}
\]

gives

\[
\mathbf H_f(\mathbf x)
=
\mathbf J_{\nabla f}(\mathbf x)
\]

The Hessian's $i$th row describes how the gradient's $i$th component changes with each input coordinate.

Here the gradient uses the standard Euclidean inner product. It is a vector-valued function from $\mathbb R^n$ to $\mathbb R^n$, so its Jacobian has $n$ output and $n$ input positions. Hessian entry $(i,j)$ differentiates the gradient's $i$th component, $\partial f/\partial x_i$, once more with respect to $x_j$. Unlike a general vector-output Jacobian, it examines the rate of change of the same scalar function twice, even when the two input coordinates differ. The next section gives conditions for exchanging the order of mixed partial derivatives.

## Core concept 2. A sufficiently smooth function has a symmetric Hessian

If the second mixed partial derivatives are continuous in a neighborhood of the point, Clairaut's theorem gives

\[
\frac{\partial^2f}
{\partial x_i\partial x_j}
=
\frac{\partial^2f}
{\partial x_j\partial x_i}
\]

Thus,

\[
\mathbf H_f(\mathbf x)^\top
=
\mathbf H_f(\mathbf x)
\]

Existence of mixed partial derivatives alone does not guarantee symmetry in every pathological case. The main examples in this textbook use functions with continuous second partial derivatives.

A symmetric Hessian has real eigenvalues and an orthonormal eigenbasis. Its eigenvectors give principal directions of local curvature, with the corresponding eigenvalues specifying second-order rates of change along those directions.

The Hessian in Example 1 has two orthogonal eigendirections with positive but different curvatures.

<figure class="lesson-figure" markdown="1">

![Positive quadratic loss contours with two orthogonal Hessian eigenvector directions of curvature three minus square root two and three plus square root two](../../figures/assets/M03/M03-12-principal-curvature-directions.svg)

<figcaption>The contours are f=1,4,9 from Example 1, and the arrows indicate the two eigenvector directions. Equal arrow lengths do not mean equal curvature: the purple direction has curvature 3−√2, and the green direction has curvature 3+√2.</figcaption>

</figure>

## Core concept 3. The second differential is a bilinear form

At $\mathbf x$, the second differential is the bilinear form taking two displacement vectors $\mathbf u,\mathbf v$ and returning

\[
d^2f_{\mathbf x}(\mathbf u,\mathbf v)
=
\mathbf u^\top
\mathbf H_f(\mathbf x)
\mathbf v
\]

The first differential $df_{\mathbf x}$ takes one displacement vector and calculates a first-order rate of change. Now fix $\mathbf u$ and investigate how that rate changes as the base point moves in direction $\mathbf v$. That is,

\[
d^2f_{\mathbf x}(\mathbf u,\mathbf v)
=\left.\frac{d}{dt}\left[df_{\mathbf x+t\mathbf v}(\mathbf u)\right]\right|_{t=0}
=\mathbf u^\top\mathbf H_f(\mathbf x)\mathbf v
\]

The first slot specifies the first-order direction being measured; the second specifies how its base point moves. Fixing the Hessian at the base point makes $\mathbf H_f\mathbf v$ linear in $\mathbf v$, while measurement by $\mathbf u^\top$ is linear in $\mathbf u$. Linearity therefore holds separately in both slots.

Using the same direction twice gives the quadratic form

\[
d^2f_{\mathbf x}(\mathbf v,\mathbf v)
=
\mathbf v^\top
\mathbf H_f(\mathbf x)
\mathbf v
\]

This equals the second derivative of the curve

\[
\phi(t)=f(\mathbf x+t\mathbf v)
\]

\[
\phi''(0)
=
\mathbf v^\top\mathbf H_f(\mathbf x)\mathbf v
\]

The first derivative along the path is $\phi'(t)=\nabla f(\mathbf x+t\mathbf v)^\top\mathbf v$. Differentiate only the changing gradient, not the fixed $\mathbf v$, to obtain the second derivative above. Scaling $\mathbf v$ by $\alpha$ contributes a factor in both slots, multiplying the second-order rate by $\alpha^2$. This rate is with respect to path parameter $t$. To compare directions per unit distance, normalize each nonzero $\mathbf v$ to a unit vector.

## Core concept 4. The Hessian supplies the second-order Taylor term

If the function is twice continuously differentiable around the base point, then for a small displacement $\mathbf h$,

\[
f(\mathbf x+\mathbf h)
\approx
f(\mathbf x)
+
\nabla f(\mathbf x)^\top\mathbf h
+
\frac12
\mathbf h^\top
\mathbf H_f(\mathbf x)
\mathbf h
\]

The three terms have the following roles.

| Term | Role |
|---|---|
| $f(\mathbf x)$ | Base function value |
| $\nabla f(\mathbf x)^\top\mathbf h$ | First-order change |
| $\frac12\mathbf h^\top\mathbf H_f(\mathbf x)\mathbf h$ | Second-order curvature correction |

Applying a single-variable Taylor expansion to $t\mapsto f(\mathbf x+t\mathbf h)$ gives first derivative $\nabla f(\mathbf x)^\top\mathbf h$ and second derivative $\mathbf h^\top\mathbf H_f(\mathbf x)\mathbf h$ at $t=0$. The factor $1/2$ multiplying the second derivative in the single-variable expansion therefore remains. This quadratic form multiplies components of $\mathbf h$ in pairs rather than merely adding squared terms from individual input coordinates, so it also includes cross terms between different coordinates.

Let $r(\mathbf h)$ be the omitted residual. Under the stated smoothness condition,

\[
\lim_{\mathbf h\to\mathbf 0}
\frac{|r(\mathbf h)|}{\|\mathbf h\|_2^2}=0
\]

The first-order approximation in M03-10 divided the residual by the input magnitude. Here, after subtracting terms through second order, the residual is divided by the squared input magnitude. The gradient and Hessian at the base point remain fixed as $\mathbf h$ shrinks. Including a quadratic term does not make the entire function quadratic.

At a critical point, $\nabla f(\mathbf x)=\mathbf 0$, so the Hessian's quadratic form may give the lowest-order change.

Normalize the eigendirections and move the same distance $t$ from the origin to compare the Hessian's two curvatures through function values.

<figure class="lesson-figure" markdown="1">

![Unit distance sections of the positive quadratic loss rise at different rates with one half times each Hessian eigenvalue](../../figures/assets/M03/M03-12-principal-direction-sections.svg)

<figcaption>The origin is a critical point with gradient 0, so this example has f(tq)=½λ t². A Hessian eigenvalue is a second-order rate of change; the actual quadratic Taylor term includes a factor of 1/2.</figcaption>

</figure>

## Core concept 5. Eigenvalue signs classify local shape at a critical point

As in the preceding section, consider a function twice continuously differentiable around the base point, with critical-point condition $\nabla f(\mathbf x)=\mathbf 0$. A strict local minimum has function values greater than the base value at every sufficiently close distinct point. A strict local maximum has values less than the base value at all such points.

Let $\mathbf q_i$ be orthonormal eigenvectors of the symmetric Hessian, with eigenvalues $\lambda_i$. Expanding $\mathbf h=\sum_i c_i\mathbf q_i$ gives

\[
\mathbf h^\top\mathbf H_f(\mathbf x)\mathbf h
=\sum_i\lambda_i c_i^2,
\qquad
\|\mathbf h\|_2^2=\sum_i c_i^2
\]

In the eigenbasis, cross terms between directions disappear, leaving a sum of squared directional displacements weighted by eigenvalues.

- If every eigenvalue is positive, the point is a strict local minimum.
- If every eigenvalue is negative, it is a strict local maximum.
- If positive and negative eigenvalues coexist, it is a saddle point.
- If an eigenvalue is 0, second-order information alone may be inconclusive.

If every eigenvalue is positive, the smallest one, $\lambda_{\min}>0$, bounds the quadratic form below by $\lambda_{\min}\|\mathbf h\|_2^2$. The second-order Taylor term has half this bound. Since the residual vanishes relative to $\|\mathbf h\|_2^2$, it cannot reverse the increase in function value for sufficiently small nonzero $\mathbf h$. With all eigenvalues negative, function values decrease instead. With mixed signs, nearby points along positive eigendirections increase the value while those along negative eigendirections decrease it, ruling out both a maximum and a minimum.

A positive semidefinite Hessian alone does not guarantee a strict minimum. For example, $f(x)=x^4$ has Hessian 0 at the origin, yet the origin is a strict minimum. The function $f(x)=-x^4$ has the same Hessian 0 there but a strict maximum.

The curves below distinguish mixed signs from cases where zero eigenvalues leave the classification unresolved.

<figure class="lesson-figure" markdown="1">

![Saddle loss x squared minus y squared rises along the x axis and falls along the y axis from the same origin](../../figures/assets/M03/M03-12-saddle-sections.svg)

<figcaption>From the origin in Example 2, function values rise in the x direction and fall in the y direction. The origin with mixed signs in its quadratic term is therefore neither a minimum nor a maximum.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Positive and negative fourth power functions both have zero Hessian at the origin but opposite minimum and maximum outcomes](../../figures/assets/M03/M03-12-zero-hessian-quartics.svg)

<figcaption>Both functions have gradient and Hessian 0 at the origin. But a positive order-4 term gives a minimum and a negative order-4 term a maximum, so Hessian 0 does not complete the classification.</figcaption>

</figure>

## Core concept 6. A Hessian-vector product calculates directional curvature

The Hessian-vector product is

\[
\mathbf H_f(\mathbf x)\mathbf v
\]

Multiplying once more by $\mathbf v^\top$ gives directional curvature:

\[
\mathbf v^\top
\left(
\mathbf H_f(\mathbf x)\mathbf v
\right)
\]

Treat the gradient as a vector-valued function and apply the JVP from M03-11:

\[
\left.\frac{d}{dt}\nabla f(\mathbf x+t\mathbf v)\right|_{t=0}
=\mathbf J_{\nabla f}(\mathbf x)\mathbf v
=\mathbf H_f(\mathbf x)\mathbf v
\]

The HVP itself is a vector rate of gradient change as the point moves in a direction. Measuring that vector again along the same $\mathbf v$ gives a scalar second-order rate. The calculation combines Hessian columns linearly with weights $v_j$, so obtaining the product does not necessarily require storing every column separately. The gradient finite difference in Example 4 checks this rate of change.

For a model with $P$ parameters, the Hessian has shape $P\times P$, with storage cost proportional to $P^2$. HVPs are used in algorithms that calculate products along particular directions without storing the entire matrix. M03-14 returns to HVPs through automatic differentiation.

## Core concept 7. The Hessian depends on coordinates and the base point

Under a linear reparameterization

\[
\mathbf x=\mathbf P\mathbf z
\]

with $g(\mathbf z)=f(\mathbf P\mathbf z)$,

\[
\mathbf H_g(\mathbf z)
=
\mathbf P^\top
\mathbf H_f(\mathbf x)
\mathbf P
\]

This is a congruence transformation. If $\mathbf P$ is not orthogonal, Hessian eigenvalue magnitudes may change.

For this reparameterization, $\mathbf P$ is a fixed invertible matrix. A new displacement $\mathbf h_z$ corresponds to $\mathbf h_x=\mathbf P\mathbf h_z$ in the old coordinates. Evaluating the same quadratic term gives

\[
\mathbf h_x^\top\mathbf H_f\mathbf h_x
=\mathbf h_z^\top(\mathbf P^\top\mathbf H_f\mathbf P)\mathbf h_z
\]

The coordinate change enters both input slots of a bilinear form, placing $\mathbf P$ and $\mathbf P^\top$ on the two sides. This is not multiplication by $\mathbf P^{-1}$ as in similarity of a linear operator. Even when numerical eigenvalues change, corresponding displacement vectors give the same scalar quadratic term.

A nonlinear reparameterization also adds terms involving second derivatives of the coordinate change and the gradient. Comparing numerical Hessian spectra directly across parameterizations therefore requires controlling coordinate correspondence and scaling.

The single-variable chain rule also shows this extra term. If both functions in $g(z)=f(x(z))$ are twice differentiable, then

\[
g''(z)=f''(x(z))\bigl(x'(z)\bigr)^2+f'(x(z))x''(z)
\]

The first term multiplies the original function's second-order rate by two factors of the coordinate change's first-order scaling. The second arises because the coordinate path itself changes at second order. It vanishes for a linear transformation, where $x''(z)=0$.

The Hessian gives second-order information at one point. Studying a training trajectory or the loss shape over a broad region requires evaluating loss at multiple points and along actual paths.

## Example 1. A positive definite Hessian

### Problem

Calculate the gradient and Hessian of

\[
f(x,y)=x^2+xy+2y^2
\]

and classify the origin. Also calculate the second-order rate along $\mathbf v=(1,-1)^\top$.

### Solution

\[
\nabla f(x,y)
=
\begin{bmatrix}
2x+y\\
x+4y
\end{bmatrix}
\]

The origin is therefore a critical point. The Hessian is

\[
\mathbf H_f
=
\begin{bmatrix}
2&1\\
1&4
\end{bmatrix}
\]

The characteristic equation is

\[
\det
\begin{bmatrix}
2-\lambda&1\\
1&4-\lambda
\end{bmatrix}
=
\lambda^2-6\lambda+7
=
0
\]

with eigenvalues

\[
\lambda_1=3+\sqrt2,
\qquad
\lambda_2=3-\sqrt2
\]

Both are positive, so the origin is a strict local minimum. The function is a positive definite quadratic form, making the origin a global minimum as well.

The directional second-order rate is

\[
\mathbf v^\top\mathbf H_f\mathbf v
=
\begin{bmatrix}
1&-1
\end{bmatrix}
\begin{bmatrix}
2&1\\
1&4
\end{bmatrix}
\begin{bmatrix}
1\\-1
\end{bmatrix}
=
4
\]

### Meaning of the result

Positive second-order rates in every direction make the function value increase near the origin.

## Example 2. A saddle point

For

\[
f(x,y)=x^2-y^2
\]

the gradient and Hessian are

\[
\nabla f(x,y)
=
\begin{bmatrix}
2x\\-2y
\end{bmatrix}
\]

\[
\mathbf H_f
=
\begin{bmatrix}
2&0\\
0&-2
\end{bmatrix}
\]

The origin is a critical point with Hessian eigenvalues 2 and $-2$. Function values increase along the $x$ axis and decrease along the $y$ axis, making the origin a saddle point.

## Example 3. The Hessian of a least-squares loss

Consider parameters

\[
\boldsymbol\theta=
\begin{bmatrix}
\theta_1\\\theta_2
\end{bmatrix}
\]

and loss

\[
\mathcal L(\boldsymbol\theta)
=
\frac12
(\theta_1+2\theta_2-3)^2
\]

Writing $\mathbf a=(1,2)^\top$ and $r=\mathbf a^\top\boldsymbol\theta-3$ gives

\[
\nabla\mathcal L
=
r\mathbf a
\]

and

\[
\mathbf H_{\mathcal L}
=
\mathbf a\mathbf a^\top
=
\begin{bmatrix}
1&2\\
2&4
\end{bmatrix}
\]

This Hessian is positive semidefinite with rank 1. For direction

\[
\mathbf v=
\begin{bmatrix}
2\\-1
\end{bmatrix}
\]

we have

\[
\mathbf a^\top\mathbf v=0
\]

and therefore

\[
\mathbf H_{\mathcal L}\mathbf v
=
\mathbf a(\mathbf a^\top\mathbf v)
=
\mathbf 0
\]

Changing parameters along this direction preserves $\theta_1+2\theta_2$, leaving the loss unchanged.

The zero-curvature direction in Example 3 moves along a straight line of constant loss.

<figure class="lesson-figure" markdown="1">

![Least squares loss contours with zero loss line theta one plus two theta two equals three and direction two minus one moving along that line](../../figures/assets/M03/M03-12-least-squares-flat-direction.svg)

<figcaption>Moving from (1,1) by (2,−1) reaches (3,0); both satisfy θ₁+2θ₂=3. Here, loss is 0 along the entire line, so zero curvature corresponds to an actual flat direction.</figcaption>

</figure>

## Example 4. Checking HVPs with finite differences

If the gradient is differentiable, then

\[
\mathbf H_f(\mathbf x)\mathbf v
\approx
\frac{
\nabla f(\mathbf x+\varepsilon\mathbf v)
-
\nabla f(\mathbf x)
}{
\varepsilon
}
\]

The function in Example 1 is quadratic with

\[
\nabla f(\mathbf x)=\mathbf H_f\mathbf x
\]

Thus,

\[
\nabla f(\mathbf x+\varepsilon\mathbf v)
-
\nabla f(\mathbf x)
=
\varepsilon\mathbf H_f\mathbf v
\]

and the finite difference equals the HVP exactly for $\varepsilon\ne0$.

An HVP first produces a vector rate of gradient change. Measuring it again along the same direction gives scalar curvature. Separately compare what happens when the coordinate scaling changes.

<figure class="lesson-figure" markdown="1">

![Input direction one minus one maps to gradient change one minus three and a second measurement gives scalar curvature four](../../figures/assets/M03/M03-12-hvp-versus-curvature.svg)

<figcaption>For direction v=(1,−1)ᵀ in Example 1, the HVP is (1,−3)ᵀ, while the directional second-order rate is 4. For this quadratic function, gradient finite differences give exactly the same HVP.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Loss x squared and its parameterization x equals two z have Hessian values two and eight while matching points retain the same loss](../../figures/assets/M03/M03-12-coordinate-scaled-curvature.svg)

<figcaption>Expressing the same function with x=2z inserts scaling factor 2 into both displacement slots, multiplying the Hessian by 4. Corresponding points x=1,z=0.5 have equal function values but different numerical curvatures in their coordinates.</figcaption>

</figure>

## Common misconceptions

### Misconception 1. One Hessian matrix contains every second derivative of a vector-valued function

The Hessian in this lesson is an $n\times n$ matrix defined for a scalar function. Vector outputs have a Hessian for each output component, producing an order-3 structure.

### Misconception 2. A positive semidefinite Hessian implies a strict minimum

An eigenvalue of 0 leaves a direction that second-order terms cannot classify. Higher-order terms or nearby function values must be examined.

### Misconception 3. Hessian eigenvalues are independent of parameterization

Parameter scaling and reparameterization can change the Hessian matrix and eigenvalue magnitudes. Specify coordinate correspondence when making comparisons.

### Misconception 4. One checkpoint's Hessian spectrum explains all of training

A Hessian provides second-order information at one parameter point. Claims about training dynamics require investigating multiple checkpoints and actual update directions.

## Exercises

### 1. Hessian shape

State the Hessian shape of $f:\mathbb R^5\to\mathbb R$ and explain the meaning of $H_{2,4}$.

<details>
<summary>Show solution</summary>

The input dimension is 5, so the Hessian has shape $5\times5$.

\[
H_{2,4}
=
\frac{\partial^2f}
{\partial x_2\partial x_4}
\]

This describes how the gradient's second component changes with the fourth input coordinate.

</details>

### 2. Calculating a Hessian

Calculate the gradient and Hessian of

\[
f(x,y)=x^2+3xy+4y^2
\]

<details>
<summary>Show solution</summary>

\[
\nabla f(x,y)
=
\begin{bmatrix}
2x+3y\\
3x+8y
\end{bmatrix}
\]

so

\[
\mathbf H_f
=
\begin{bmatrix}
2&3\\
3&8
\end{bmatrix}
\]

</details>

### 3. Checking symmetry

For

\[
f(x,y)=x^2y+xy^2
\]

calculate both mixed partial derivatives and verify Hessian symmetry.

<details>
<summary>Show solution</summary>

\[
\frac{\partial f}{\partial x}
=
2xy+y^2
\]

gives

\[
\frac{\partial^2f}{\partial y\partial x}
=
2x+2y
\]

Also,

\[
\frac{\partial f}{\partial y}
=
x^2+2xy
\]

gives

\[
\frac{\partial^2f}{\partial x\partial y}
=
2x+2y
\]

The two mixed partial derivatives agree, making the off-diagonal Hessian entries symmetric.

</details>

### 4. Directional curvature

Given

\[
\mathbf H=
\begin{bmatrix}
4&1\\
1&2
\end{bmatrix},
\qquad
\mathbf v=
\begin{bmatrix}
1\\-1
\end{bmatrix}
\]

calculate $\mathbf H\mathbf v$ and $\mathbf v^\top\mathbf H\mathbf v$.

<details>
<summary>Show solution</summary>

\[
\mathbf H\mathbf v
=
\begin{bmatrix}
3\\-1
\end{bmatrix}
\]

and

\[
\mathbf v^\top\mathbf H\mathbf v
=
\begin{bmatrix}
1&-1
\end{bmatrix}
\begin{bmatrix}
3\\-1
\end{bmatrix}
=
4
\]

</details>

### 5. Classifying critical points

State the second-order classification at a critical point with each set of Hessian eigenvalues:

1. $2,5$
2. $-1,-4$
3. $3,-2$
4. $0,4$

<details>
<summary>Show solution</summary>

1. Both are positive, so the point is a strict local minimum.
2. Both are negative, so it is a strict local maximum.
3. The signs are mixed, so it is a saddle point.
4. The Hessian is positive semidefinite but has an eigenvalue of 0, so second-order information alone is inconclusive.

</details>

### 6. Least-squares Hessian

Calculate the gradient and Hessian of

\[
\mathcal L(\boldsymbol\theta)
=
\frac12
(\mathbf a^\top\boldsymbol\theta-b)^2
\]

<details>
<summary>Show solution</summary>

Writing $r=\mathbf a^\top\boldsymbol\theta-b$ gives

\[
\nabla\mathcal L=r\mathbf a
\]

Differentiating once more with respect to $\boldsymbol\theta$ gives

\[
\mathbf H_{\mathcal L}
=
\mathbf a\mathbf a^\top
\]

For every $\mathbf v$,

\[
\mathbf v^\top\mathbf H_{\mathcal L}\mathbf v
=(\mathbf a^\top\mathbf v)^2\ge0
\]

so the matrix is positive semidefinite.

</details>

### 7. Critiquing a model claim

Critique the statement: “The trained model has a small largest Hessian eigenvalue, so it generalizes better than another model.”

<details>
<summary>Show solution</summary>

The largest eigenvalue describes local curvature in the chosen parameter coordinates at the chosen checkpoint. Parameter scaling and symmetry-based reparameterization can change it, and small curvature alone does not determine test performance. Control the coordinate convention, data, loss, and evaluation procedure, and compare independent test results as well.

</details>

## Lesson summary

- The Hessian is the Jacobian of a scalar function's gradient and an $n\times n$ matrix of second partial derivatives.
- Continuous second mixed partial derivatives give a symmetric Hessian.
- The second differential is the bilinear form represented by the Hessian; directional curvature is a quadratic form.
- The Hessian supplies the quadratic Taylor term and helps classify local shape at critical points.
- HVPs are used to calculate products along particular directions without storing the entire Hessian.
- The Hessian matrix and spectrum depend on the base point, parameter coordinates, and scaling.

## Pass criteria

You pass if you can answer the following without referring to the material:

- Can you calculate a scalar function's Hessian and determine its shape?
- Can you explain conditions for Hessian symmetry?
- Can you calculate the second differential and directional curvature?
- Can you identify the Hessian term in a second-order Taylor approximation?
- Can you classify local shape at a critical point using eigenvalue signs?
- Can you calculate an HVP and explain its uses?
- Can you limit Hessian spectrum claims according to coordinate and base-point dependence?

## Next lesson

- [M03-13 JVP and VJP](M03-13-jvp-vjp.md)

## Author checklist

- [x] Learning objectives are expressed as observable actions.
- [x] The Hessian convention and shape are specified.
- [x] Conditions for symmetry are stated.
- [x] The second differential is connected to the quadratic Taylor term.
- [x] Sufficient conditions for critical-point classification are distinguished from inconclusive cases.
- [x] HVPs and coordinate dependence are explained.
- [x] Every exercise has a solution.
- [x] The strengths of model interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
