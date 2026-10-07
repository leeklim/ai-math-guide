---
id: "M03-10"
title: "Total derivative and differential"
part: 1
stage: "M03"
status: "complete"
prerequisites:
  - "M01-10"
  - "M01-12"
  - "M03-07"
estimated_time: "125~150 minutes"
---

# M03-10. Total derivative and differential

## Why this lesson matters

A partial derivative measures the rate of change when just one input coordinate moves. When several coordinates change together, one linear map describes the first-order change. This map is the total derivative.

A neural network layer maps vectors to vectors, passing small activation changes to small changes in the next layer. Understanding the total derivative as a function's local linear approximation lets us read the chain rule as composition of linear maps. The next lesson represents this map by a coordinate matrix, the Jacobian.

## Learning objectives

After completing this lesson, you will be able to:

- Define the total derivative as a local linear approximation with an error term.
- Explain the relationships among partial derivatives, directional derivatives, and the total derivative.
- Explain why the differential of a scalar-output function is a covector.
- Calculate first-order output changes for small input changes and compare them with actual changes.
- Calculate the multivariable chain rule as composition of linear maps.
- Distinguish local sensitivity claims supported by a local linear approximation from claims about global behavior.

## Prerequisite check

- Prerequisite lesson: [M01-10 Multiple variables and partial derivatives](../M01/M01-10-multivariable-partial-derivatives.md)
- Prerequisite lesson: [M01-12 Taylor approximation](../M01/M01-12-taylor-approximation.md)
- Prerequisite lesson: [M03-07 Dual spaces and covectors](M03-07-dual-spaces-covectors.md)
- Check: Can you calculate coordinatewise partial derivatives?
- Check: Can you explain what it means for the error in a single-variable first-order Taylor approximation to become small relative to the input change?
- Check: Can you distinguish the types of a differential and a gradient?

Review the prerequisite lessons first if partial derivatives or differentials are unclear.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Type and shape |
|---|---|---|---|
| $f:\mathbb R^n\to\mathbb R^m$ | `f maps R to the n into R to the m` | A function mapping vector inputs to vector outputs | Input dimension $n$, output dimension $m$ |
| $\mathbf x$ | `x` | The base point for linearization | $\mathbb R^n$ |
| $\mathbf h$ | `h` | A small displacement added to the base point | $\mathbb R^n$ |
| $Df(\mathbf x)$ | `D f at x` | The total derivative at $\mathbf x$ | A linear map $\mathbb R^n\to\mathbb R^m$ |
| $df_{\mathbf x}$ | `d f at x` | The differential | In this lesson, the same linear approximation as $Df(\mathbf x)$ |
| $\mathbf r(\mathbf h)$ | `r of h` | The error remaining after the first-order approximation | $\mathbb R^m$ |
| $o(\|\mathbf h\|)$ | `little o of the norm of h` | An error that shrinks faster than $\|\mathbf h\|$ | The ratio tends to 0 |

## Core concept 1. The total derivative is the best local linear approximation

A function $f:\mathbb R^n\to\mathbb R^m$ is differentiable at $\mathbf x$ if there exists a linear map

\[
L:\mathbb R^n\to\mathbb R^m
\]

such that

\[
f(\mathbf x+\mathbf h)
=
f(\mathbf x)+L(\mathbf h)+\mathbf r(\mathbf h)
\]

and

\[
\lim_{\mathbf h\to\mathbf 0}
\frac{\|\mathbf r(\mathbf h)\|}
{\|\mathbf h\|}
=
0
\]

This linear map $L$ is written as

\[
Df(\mathbf x)
\]

Fix the base point $\mathbf x$; the vector $\mathbf h$ is an input displacement from it. The value $L(\mathbf h)$ predicts an output change, not the output value itself. The residual is therefore $\mathbf r(\mathbf h)=f(\mathbf x+\mathbf h)-f(\mathbf x)-L(\mathbf h)$: the actual change minus the linear prediction.

For $\mathbf h\ne\mathbf 0$, divide the residual's magnitude by the input displacement's magnitude. A limit of 0 means that for any positive $\varepsilon$, all sufficiently small nonzero displacements satisfy $\|\mathbf r(\mathbf h)\|\le\varepsilon\|\mathbf h\|$. This does not merely check one line of approach or examine directions separately. The same error criterion must hold even as the approach direction varies. The notation $o(\|\mathbf h\|)$ abbreviates this relative-size condition.

Thus,

\[
f(\mathbf x+\mathbf h)
\approx
f(\mathbf x)+Df(\mathbf x)(\mathbf h)
\]

The approximation error shrinks faster than the size of the input change, a stronger condition than small absolute error alone.

Only one linear map satisfies this condition. If two candidates $L_1,L_2$ existed, fix a nonzero $\mathbf v$ and set $\mathbf h=t\mathbf v$. The difference between their residuals is $t(L_1-L_2)(\mathbf v)$. Since each residual's magnitude divided by $|t|$ tends to 0, we must have $(L_1-L_2)(\mathbf v)=\mathbf 0$. The candidates agree for every $\mathbf v$. “Best” in the heading therefore means uniquely determined by this first-order residual condition, not minimizing error over several samples.

Shrinking the displacement in Example 1 along the same direction shows why the ratio of error to input change matters, rather than just the error itself.

<figure class="lesson-figure" markdown="1">

![Relative approximation error for input changes proportional to point zero one minus point zero two decreases toward zero](../../figures/assets/M03/M03-10-relative-local-error.svg)

<figcaption>The difference between the actual output and first-order approximation for input change h=s(0.01,−0.02)ᵀ is divided by ‖h‖. That this ratio also decreases as s shrinks is the total derivative's condition.</figcaption>

</figure>

## Core concept 2. The total derivative is one linear map

For two input changes and scalars,

\[
Df(\mathbf x)(\alpha\mathbf h_1+\beta\mathbf h_2)
=
\alpha Df(\mathbf x)(\mathbf h_1)
+
\beta Df(\mathbf x)(\mathbf h_2)
\]

Even if $f$ is nonlinear, its total derivative at a point is linear. Changing the base point $\mathbf x$ may change the derivative.

Linearity concerns displacement vectors, not base points. The equation combines the first-order effects of $\mathbf h_1,\mathbf h_2$ at fixed $\mathbf x$; it does not add derivatives at different base points. The output prediction $f(\mathbf x)+Df(\mathbf x)(\mathbf h)$ is affine because it adds the constant output $f(\mathbf x)$. The change prediction $Df(\mathbf x)(\mathbf h)$ is linear.

The total derivative maps an input displacement to an output displacement.

\[
\underbrace{\mathbf h}_{n\times1}
\longmapsto
\underbrace{Df(\mathbf x)(\mathbf h)}_{m\times1}
\]

The next lesson represents this linear map in the chosen standard bases by an $m\times n$ Jacobian matrix.

## Core concept 3. Partial derivatives are the total derivative's outputs along coordinate axes

Let $\mathbf e_j$ be the $j$th standard basis vector of the input space. If $f$ is differentiable, then

\[
Df(\mathbf x)(\mathbf e_j)
=
\frac{\partial f}{\partial x_j}(\mathbf x)
\]

The right-hand side is a vector collecting the $x_j$ partial derivatives of the $m$ output components.

Insert $\mathbf h=t\mathbf e_j$ into the residual equation and use linearity, $Df(\mathbf x)(t\mathbf e_j)=tDf(\mathbf x)(\mathbf e_j)$, to obtain

\[
\frac{f(\mathbf x+t\mathbf e_j)-f(\mathbf x)}{t}
=Df(\mathbf x)(\mathbf e_j)+\frac{\mathbf r(t\mathbf e_j)}{t}
\]

Since $\|\mathbf e_j\|_2=1$, the residual magnitude divided by $|t|$ tends to 0. The left-hand side changes only $x_j$, so its difference quotient converges to the vector partial derivative. This derives the equality above.

For any displacement

\[
\mathbf h
=
\sum_{j=1}^{n}h_j\mathbf e_j
\]

linearity gives

\[
Df(\mathbf x)(\mathbf h)
=
\sum_{j=1}^{n}
h_j
\frac{\partial f}{\partial x_j}(\mathbf x)
\]

The total derivative forms a linear combination of the coordinatewise partial derivative outputs, weighted by changes $h_j$.

Existence of all partial derivatives at a point does not by itself guarantee a total derivative. Continuity of the partial derivatives in a neighborhood of that point is a sufficient condition for differentiability.

Coordinate-axis calculations move one input at a time, whereas the residual condition in the first section also covers simultaneous changes in several coordinates. In Example 4, all coordinate-axis rates are 0, yet the residual ratio along a diagonal does not shrink.

## Core concept 4. A directional derivative evaluates the total derivative on a direction

Define the directional derivative for a vector $\mathbf v$ by

\[
D_{\mathbf v}f(\mathbf x)
=
\lim_{t\to0}
\frac{f(\mathbf x+t\mathbf v)-f(\mathbf x)}{t}
\]

If $f$ is differentiable at $\mathbf x$, then

\[
D_{\mathbf v}f(\mathbf x)
=
Df(\mathbf x)(\mathbf v)
\]

To verify this, insert $\mathbf h=t\mathbf v$ into the residual equation. Linearity gives $Df(\mathbf x)(t\mathbf v)/t=Df(\mathbf x)(\mathbf v)$. For $\mathbf v\ne\mathbf 0$,

\[
\frac{\|\mathbf r(t\mathbf v)\|}{|t|}
=\frac{\|\mathbf r(t\mathbf v)\|}{\|t\mathbf v\|}\,\|\mathbf v\|
\to0
\]

No residual remains in the limit of the directional difference quotient. For $\mathbf v=\mathbf 0$, both the difference quotient and linear output are 0. If $\mathbf v$ is not a unit vector, this rate is per unit of path parameter $t$, not per unit of distance traveled.

Knowing one total derivative allows all directional derivatives to be calculated. Conversely, even if directional derivatives exist separately in several directions, a total derivative may fail to exist if their dependence on direction cannot be expressed by one linear map.

## Core concept 5. A scalar-output differential is a covector

If $m=1$, then

\[
Df(\mathbf x):\mathbb R^n\to\mathbb R
\]

so the total derivative is a covector. In this case, write

\[
df_{\mathbf x}(\mathbf h)
=
Df(\mathbf x)(\mathbf h)
\]

In standard Euclidean coordinates,

\[
df_{\mathbf x}(\mathbf h)
=
\nabla f(\mathbf x)^\top\mathbf h
\]

The left-hand side is the scalar produced by a covector acting on a displacement vector. The right-hand side expresses the same action through the Euclidean inner product.

For vector outputs, $Df(\mathbf x)(\mathbf h)\in\mathbb R^m$. Stacking the differentials of the output components $f_i$ produces the vector change.

## Core concept 6. The chain rule composes linear approximations

Let

\[
f:\mathbb R^n\to\mathbb R^m,
\qquad
g:\mathbb R^m\to\mathbb R^p
\]

and suppose $f$ is differentiable at $\mathbf x$ and $g$ at the intermediate point $f(\mathbf x)$. The composite function is

\[
g\circ f:\mathbb R^n\to\mathbb R^p
\]

with total derivative

\[
D(g\circ f)(\mathbf x)
=
Dg(f(\mathbf x))
\circ
Df(\mathbf x)
\]

The input change $\mathbf h$ first becomes the intermediate output change

\[
Df(\mathbf x)(\mathbf h)
\]

which then becomes the final output change

\[
Dg(f(\mathbf x))
\left(
Df(\mathbf x)(\mathbf h)
\right)
\]

The chain rule follows the same function-application order as the forward pass.

The errors discarded in the composition must also satisfy the first-order residual condition. Write $A=Df(\mathbf x)$ and $B=Dg(f(\mathbf x))$. Let $\mathbf r_f$ be the residual from linearizing $f$ at $\mathbf x$, and $\mathbf r_g$ the residual from linearizing $g$ at the intermediate point $f(\mathbf x)$. With actual intermediate change $\boldsymbol\delta=f(\mathbf x+\mathbf h)-f(\mathbf x)=A(\mathbf h)+\mathbf r_f(\mathbf h)$,

\[
g(f(\mathbf x+\mathbf h))-g(f(\mathbf x))
=B(A(\mathbf h))+B(\mathbf r_f(\mathbf h))+\mathbf r_g(\boldsymbol\delta)
\]

The fixed linear map $B$ changes residual magnitudes by at most a constant factor, so the second term vanishes relative to $\|\mathbf h\|$. The intermediate change $\boldsymbol\delta$, being a linear term plus a small residual, is also bounded in magnitude by a constant multiple of $\|\mathbf h\|$. The residual of $g$ shrinks faster than this intermediate change, so the last term also vanishes relative to $\|\mathbf h\|$. If the intermediate change is 0, the residual of $g$ is 0 as well. The remaining first-order map is $B\circ A$.

## Example 1. First-order change of a vector-valued function

### Problem

Given

\[
f(x,y)
=
\begin{bmatrix}
x^2+xy\\
e^y
\end{bmatrix}
\]

with base point and displacement

\[
\mathbf x=
\begin{bmatrix}
1\\0
\end{bmatrix},
\qquad
\mathbf h=
\begin{bmatrix}
0.01\\-0.02
\end{bmatrix}
\]

calculate the output change predicted by the total derivative and compare it with the actual change.

### Solution

The first output's partial derivatives are

\[
\frac{\partial f_1}{\partial x}=2x+y,
\qquad
\frac{\partial f_1}{\partial y}=x
\]

and the second output's are

\[
\frac{\partial f_2}{\partial x}=0,
\qquad
\frac{\partial f_2}{\partial y}=e^y
\]

The coordinate matrix of the derivative at the base point is

\[
\begin{bmatrix}
2&1\\
0&1
\end{bmatrix}
\]

so the first-order change is

\[
Df(\mathbf x)(\mathbf h)
=
\begin{bmatrix}
2&1\\
0&1
\end{bmatrix}
\begin{bmatrix}
0.01\\-0.02
\end{bmatrix}
=
\begin{bmatrix}
0\\-0.02
\end{bmatrix}
\]

The actual first output is

\[
(1.01)^2+(1.01)(-0.02)
=
1.0201-0.0202
=
0.9999
\]

giving a change of $-0.0001$. The second output change is

\[
e^{-0.02}-1
\approx
-0.0198013
\]

The first-order approximation error is approximately

\[
\begin{bmatrix}
-0.0001\\
0.0001987
\end{bmatrix}
\]

### Meaning of the result

The total derivative takes both input coordinate changes together and produces the first-order changes of both outputs. In this example, the remaining error is of the same order as the squared displacement magnitude.

The $D\mathbf f$ in Example 1 outputs a change. Approximating the actual output point requires adding the original function value.

<figure class="lesson-figure" markdown="1">

![An input change maps to predicted output change zero minus point zero two which is then added to base output one one](../../figures/assets/M03/M03-10-output-point-versus-change.svg)

<figcaption>A first-order change of 0 in the first output component does not mean the actual output point's first component is 0. Adding the base output (1,1) gives the predicted point (1,0.98), differing from the actual value by a small remainder.</figcaption>

</figure>

## Example 2. Scalar differential and gradient

Let

\[
\ell(x,y)=x^2y+\sin y
\]

Its partial derivatives are

\[
\frac{\partial\ell}{\partial x}=2xy,
\qquad
\frac{\partial\ell}{\partial y}=x^2+\cos y
\]

At $(1,0)$,

\[
d\ell_{(1,0)}(\mathbf h)
=
\begin{bmatrix}
0&2
\end{bmatrix}
\mathbf h
\]

The Euclidean gradient places the same coefficients in a column:

\[
\nabla\ell(1,0)
=
\begin{bmatrix}
0\\2
\end{bmatrix}
\]

For

\[
\mathbf h=
\begin{bmatrix}
0.1\\-0.05
\end{bmatrix}
\]

the first-order loss change is

\[
d\ell_{(1,0)}(\mathbf h)=-0.1
\]

This is a local prediction for the specified base point and small displacement.

## Example 3. Calculating the chain rule through map composition

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

At $(1,2)$, $f(1,2)=(3,2)^\top$.

The derivative matrix of $f$ is

\[
Df(1,2)
\longleftrightarrow
\begin{bmatrix}
1&1\\
2&1
\end{bmatrix}
\]

and the derivative row of $g$ is

\[
Dg(3,2)
\longleftrightarrow
\begin{bmatrix}
6&1
\end{bmatrix}
\]

The composite derivative is

\[
D(g\circ f)(1,2)
\longleftrightarrow
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

Direct composition gives

\[
(g\circ f)(x,y)
=(x+y)^2+xy
\]

with partial derivatives

\[
\frac{\partial(g\circ f)}{\partial x}
=
2(x+y)+y
\]

\[
\frac{\partial(g\circ f)}{\partial y}
=
2(x+y)+x
\]

These give 8 and 7 at $(1,2)$.

Example 3 first uses the function value to locate the intermediate point and then composes the derivatives at the corresponding points.

<figure class="lesson-figure" markdown="1">

![Forward function composition locates intermediate point three two before the local direction epsilon one zero maps to epsilon one two and then scalar eight epsilon](../../figures/assets/M03/M03-10-chain-basepoints.svg)

<figcaption>Dg is evaluated at intermediate point f(1,2)=(3,2), not at original input point (1,2). The 8ε on the lower displacement path is a first-order output change, not the actual function value 11.</figcaption>

</figure>

## Example 4. Partial derivatives without differentiability

Let

\[
f(x,y)
=
\begin{cases}
\dfrac{xy}{\sqrt{x^2+y^2}},
&
(x,y)\ne(0,0),\\
0,
&
(x,y)=(0,0)
\end{cases}
\]

The function is 0 on both coordinate axes, so

\[
\frac{\partial f}{\partial x}(0,0)=0,
\qquad
\frac{\partial f}{\partial y}(0,0)=0
\]

If a total derivative existed, the two partial derivatives would force the candidate linear map to be the zero map. But for $\mathbf h=(t,t)^\top$,

\[
f(t,t)
=
\frac{t^2}{\sqrt{2t^2}}
=
\frac{|t|}{\sqrt2}
\]

and

\[
\frac{|f(t,t)|}{\|(t,t)^\top\|_2}
=
\frac{|t|/\sqrt2}{\sqrt2|t|}
=
\frac12
\]

The ratio does not tend to 0, so the function is not differentiable at the origin.

Separating coordinate-axis approaches from diagonal approaches reveals the failure in Example 4.

<figure class="lesson-figure" markdown="1">

![Counterexample function is zero along both coordinate axes but equals absolute t divided by square root two along the diagonal](../../figures/assets/M03/M03-10-axis-versus-diagonal.svg)

<figcaption>The function is always 0 on both coordinate axes, giving partial derivatives of 0. Along diagonal (t,t), however, the change |t|/√2 cannot be explained by the same zero linear map.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Normalized error of the zero linear prediction along the diagonal stays at one half as the input approaches zero](../../figures/assets/M03/M03-10-diagonal-relative-error.svg)

<figcaption>The diagonal input has length √2|t|. The relative error of the zero linear approximation is therefore always 1/2 and does not converge to 0 as the input shrinks.</figcaption>

</figure>

## Example 5. Local changes in a neural network layer

Write a layer as

\[
\mathbf h^{(\ell+1)}
=
f_\ell(\mathbf h^{(\ell)})
\]

For a small change $\Delta\mathbf h^{(\ell)}$ in the current activation,

\[
\Delta\mathbf h^{(\ell+1)}
\approx
Df_\ell(\mathbf h^{(\ell)})
\left(
\Delta\mathbf h^{(\ell)}
\right)
\]

Across several layers, composing their derivatives calculates the first-order effect of an input change on later activations.

This approximation applies to small changes around the base activation. Higher-order terms may become large for substantial perturbations or interventions outside the activation distribution, requiring comparison with actual forward passes.

## Common misconceptions

### Misconception 1. The total derivative is a list of all partial derivatives

Partial derivatives give output changes along coordinate axes. The total derivative is one linear map from any small input displacement vector to an output displacement vector.

### Misconception 2. Existence of all partial derivatives implies differentiability

Partial derivatives at a point may exist without one linear approximation controlling errors for every approach direction.

### Misconception 3. A differential and a gradient have the same type

A scalar function's differential is a covector. Its gradient is a vector representing that covector through a chosen inner product.

### Misconception 4. A large derivative gives the same change at distant inputs

A derivative describes first-order sensitivity around a base point. Farther from that point, both the derivative itself and higher-order terms may change.

## Exercises

### 1. Reading a definition

Explain

\[
\lim_{\mathbf h\to\mathbf 0}
\frac{
\|f(\mathbf x+\mathbf h)-f(\mathbf x)-L(\mathbf h)\|
}{
\|\mathbf h\|
}
=
0
\]

in an English sentence.

<details>
<summary>Show solution</summary>

Subtract the linear prediction $L(\mathbf h)$ from the actual output change of $f$ and divide the error by the input change's magnitude. This ratio tends to 0 as $\mathbf h\to\mathbf 0$. The linear map $L$ satisfying this condition is the total derivative.

</details>

### 2. Scalar differential

Calculate the differential of

\[
f(x,y)=x^2y+\sin y
\]

at $(1,0)$ and apply it to $\mathbf h=(0.1,-0.05)^\top$.

<details>
<summary>Show solution</summary>

\[
\frac{\partial f}{\partial x}=2xy,
\qquad
\frac{\partial f}{\partial y}=x^2+\cos y
\]

The row coordinates at $(1,0)$ are therefore $(0,2)$, giving

\[
df_{(1,0)}(\mathbf h)
=
\begin{bmatrix}
0&2
\end{bmatrix}
\begin{bmatrix}
0.1\\-0.05
\end{bmatrix}
=
-0.1
\]

</details>

### 3. Derivative of a vector-valued function

Express the total derivative of

\[
f(x,y)
=
\begin{bmatrix}
x+y\\
xy
\end{bmatrix}
\]

at $(1,2)$ as a coordinate matrix and apply it to $\mathbf h=(3,-1)^\top$.

<details>
<summary>Show solution</summary>

The first output's partial derivatives are $(1,1)$, and the second output's are $(y,x)$. Thus,

\[
Df(1,2)
\longleftrightarrow
\begin{bmatrix}
1&1\\
2&1
\end{bmatrix}
\]

Applying it gives

\[
Df(1,2)(\mathbf h)
=
\begin{bmatrix}
1&1\\
2&1
\end{bmatrix}
\begin{bmatrix}
3\\-1
\end{bmatrix}
=
\begin{bmatrix}
2\\5
\end{bmatrix}
\]

</details>

### 4. Checking a remainder

Linearize $f(x)=x^2$ at $x=2$ and verify that the remainder satisfies the differentiability condition.

<details>
<summary>Show solution</summary>

\[
f(2+h)
=(2+h)^2
=
4+4h+h^2
\]

The linear term is $L(h)=4h$, and the remainder is $r(h)=h^2$.

\[
\frac{|r(h)|}{|h|}
=
|h|
\to0
\]

This satisfies the definition of the total derivative.

</details>

### 5. Directional derivative

Suppose $Df(\mathbf x)$ has coordinate matrix

\[
\begin{bmatrix}
1&2\\
-1&3
\end{bmatrix}
\]

Calculate the vector rate of change in direction $\mathbf v=(2,-1)^\top$.

<details>
<summary>Show solution</summary>

\[
D_{\mathbf v}f(\mathbf x)
=
Df(\mathbf x)(\mathbf v)
=
\begin{bmatrix}
1&2\\
-1&3
\end{bmatrix}
\begin{bmatrix}
2\\-1
\end{bmatrix}
=
\begin{bmatrix}
0\\-5
\end{bmatrix}
\]

</details>

### 6. Chain rule

Given $Df(\mathbf x):\mathbb R^2\to\mathbb R^3$ and $Dg(f(\mathbf x)):\mathbb R^3\to\mathbb R$, state the composite derivative's input and output spaces and the order of the maps.

<details>
<summary>Show solution</summary>

The composite derivative is

\[
D(g\circ f)(\mathbf x)
=
Dg(f(\mathbf x))\circ Df(\mathbf x)
:
\mathbb R^2\to\mathbb R
\]

The displacement vector first passes through $Df(\mathbf x)$ to become a change in $\mathbb R^3$, then through $Dg(f(\mathbf x))$ to become a scalar change.

</details>

### 7. Critiquing a model claim

Critique the statement: “The derivative is small at one input, so the model is stable under every input perturbation.”

<details>
<summary>Show solution</summary>

The derivative at one point describes first-order sensitivity to small changes near that point. It may differ at other inputs; large perturbations may also involve higher-order terms and movement between regions. A stability claim requires specifying the input set, perturbation size, and norm and evaluating actual output changes at multiple points.

</details>

## Lesson summary

- The total derivative linearly approximates the actual function change, with an error that shrinks faster than the input change.
- A partial derivative is the output of the total derivative applied to a standard basis vector.
- For a differentiable function, directional derivatives are calculated by applying the total derivative to direction vectors.
- A scalar-output differential is a covector, while the gradient is its vector representation through an inner product.
- The multivariable chain rule composes the total derivatives of the functions.
- A local derivative alone does not establish behavior under large perturbations or global stability.

## Pass criteria

You pass if you can answer the following without referring to the material:

- Can you define the total derivative with its remainder condition?
- Can you explain the relationship between partial derivatives and the total derivative?
- Can you calculate the first-order output change from a displacement vector?
- Can you distinguish a differential from a gradient?
- Can you express the chain rule as composition of linear maps?
- Can you explain why partial derivatives alone do not guarantee differentiability?
- Can you limit the scope of local sensitivity claims?

## Next lesson

- [M03-11 Jacobian](M03-11-jacobian.md)

## Author checklist

- [x] Learning objectives are expressed as observable actions.
- [x] The total derivative is defined through the remainder condition.
- [x] Partial and directional derivatives are connected to the linear map.
- [x] The covector type of a scalar differential is stated.
- [x] The chain rule is calculated through map composition.
- [x] A counterexample with only partial derivatives is included.
- [x] Every exercise has a solution.
- [x] The strengths of model interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
