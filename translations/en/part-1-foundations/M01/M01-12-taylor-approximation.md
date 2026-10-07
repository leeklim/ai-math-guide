---
id: "M01-12"
title: "Taylor approximation"
part: 1
stage: "M01"
status: "complete"
prerequisites:
  - "M01-07"
  - "M01-11"
estimated_time: "105~125 minutes"
---

# M01-12. Taylor approximation

## Why this lesson matters

Derivatives and gradients give local rates of change at one point. Taylor approximation uses these rates to express nearby function values through a polynomial that is easy to calculate. The tangent is a first-order Taylor approximation; a second-order term accounts for changing slopes near the reference point.

The same principle applies when an input gradient is used to approximate an output change in model interpretation. The approximation depends on the reference point and displacement size, so the error between the first-order term and the actual finite change must be checked separately.

## Learning objectives

After this lesson, you will be able to:

- Connect a single-variable first-order Taylor approximation to a tangent equation.
- Explain the roles of the second derivative and a single-variable second-order Taylor approximation.
- Calculate a multivariable first-order approximation using a gradient inner product.
- Calculate the error between an actual function value and its approximation.
- Assess the scope of claims supported by a gradient-based linear approximation.

## Prerequisite check

- Prerequisite lesson: [M01-07. Derivatives of exponential and logarithmic functions](M01-07-exponential-log-derivatives.md)
- Prerequisite lesson: [M01-11. Directional derivatives and the gradient](M01-11-directional-derivative-gradient.md)
- Check question: Can you use $f'(a)$ to write the tangent equation at $x=a$?
- Check question: Can you explain why $\nabla f(\mathbf x)^\top\Delta\mathbf x$ is a scalar?

Review the prerequisites first if tangents or gradient inner products are unclear.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and conditions |
|---|---|---|---|
| $a$ | `a` | The reference point for the approximation | The function and its derivative must be defined |
| $h$ | `h` | A single-variable displacement from the reference point | $x=a+h$ |
| $\Delta\mathbf x$ | `delta x` | A small multivariable input-change vector | $\Delta\mathbf x\in\mathbb R^n$ |
| $f''(a)$ | `f double prime of a` | The second derivative value obtained by differentiating $f'$ again | Gives curvature information for a single-variable function |
| Taylor approximation | `Taylor approximation` | A polynomial approximating nearby function values from derivatives at one point | Used near the reference point |
| Remainder | `remainder` | The difference between the actual function value and the Taylor polynomial | Depends on the displacement |

## Core concept 1. A first-order Taylor approximation predicts values using a tangent

If $x=a+h$ is close to $a$ and $f$ is differentiable at $a$, then

\[
f(a+h)
\approx
f(a)+f'(a)h
\]

Using the new input $x$ rather than the expression $x=a+h$ gives

\[
f(x)
\approx
f(a)+f'(a)(x-a)
\]

The right-hand side is the tangent equation at $x=a$.

Here $f(a)$ is the reference height, and $f'(a)h$ is the predicted first-order change. At $h=0$, the approximate and actual values agree, and both expressions have the same slope at $a$.

Overlaying the square function and its tangent from Example 1 shows agreement in value and slope at the reference point, followed by a gap after moving away.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![A quadratic function around input three compared with its tangent approximation nine plus six h](../../figures/assets/M01/M01-12-tangent-and-square.svg)
  <figcaption>At the reference point h=0, both values are 9 and both slopes are 6. Moving to either side puts the actual square function h² above the tangent. The first-order expression remains a straight line, but the actual function's slope changes.</figcaption>
</figure>

## Core concept 2. The remainder is what the approximation leaves out

To express the first-order approximation as an equality, add a remainder $r(h)$.

\[
f(a+h)
=
f(a)+f'(a)h+r(h)
\]

Differentiability gives the property

\[
\lim_{h\to0}
\frac{r(h)}{|h|}
=0
\]

As $h$ becomes smaller, the remainder shrinks faster than $|h|$.

Connecting this to the derivative definition, for $h\ne0$ we have

\[
\frac{f(a+h)-f(a)}{h}-f'(a)
=\frac{r(h)}{h}
\]

The left-hand side is the difference between the difference quotient and derivative, so it tends to 0 as $h\to0$. The ratio of the remainder's absolute value to the displacement $|h|$ therefore also tends to 0. The basis of the first-order approximation is not merely that the remainder is a small number, but that it becomes negligible relative to the displacement. Even if the first-order term $f'(a)h$ is 0, the remainder need not be 0. For the square function below, $h^2$ remains even when $a=0$.

This property concerns values near the reference point. For large $h$, the remainder may exceed the first-order term. State both the displacement size and actual error when using an approximation.

For the square function, plotting remainder and displacement together shows what it means to shrink faster than the displacement.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Quadratic residual magnitude h squared compared with the displacement magnitude absolute h as both approach zero](../../figures/assets/M01/M01-12-residual-rate.svg)
  <figcaption>As the input displacement magnitude approaches 0, h² becomes increasingly small relative to |h|. Their ratio is |h|, which tends to 0. Including the second-order term removes this square function's remainder completely.</figcaption>
</figure>

## Core concept 3. The second derivative measures change in slope

Differentiating the derivative function $f'(x)$ again gives the second derivative.

\[
f''(x)
=
\frac{d}{dx}f'(x)
\]

The value $f''(a)$ is the instantaneous rate of change of slope $f'$ with respect to the input. If $f''(a)>0$, the slope's rate of change at $a$ is positive; if $f''(a)<0$, it is negative. On a surrounding interval where the second derivative maintains the same sign, the slope increases or decreases, respectively. Distinguish the function's height from how quickly its slope changes.

For a function whose second derivative is continuous near the reference point, the single-variable second-order Taylor approximation is

\[
f(a+h)
\approx
f(a)+f'(a)h
+
\frac12f''(a)h^2
\]

The second-order term captures bending that the tangent misses.

The coefficient $1/2$ is needed to match the approximation polynomial's second derivative to the actual value. Write the second-order coefficient as $c$ and the polynomial in displacement $h$ as $f(a)+f'(a)h+c h^2$. At $h=0$, its value is $f(a)$ and its first derivative is $f'(a)$. Differentiating again gives second derivative $2c$, so set $2c=f''(a)$, or $c=f''(a)/2$. This matches value, slope, and rate of slope change at the same reference point. Under the continuity condition above, the remainder divided by $h^2$ tends to 0. Accuracy at distant points is not guaranteed.

## Core concept 4. A Taylor expansion can be exact for a polynomial

Consider

\[
f(x)=x^2
\]

near $a$. Since $f'(a)=2a$ and $f''(a)=2$,

\[
f(a+h)
=
a^2+2ah+h^2
\]

This exactly equals the second-order Taylor expression

\[
f(a)+f'(a)h+\frac12f''(a)h^2
\]

because the quadratic has no terms of degree three or higher.

Using only the first-order approximation leaves error $h^2$. For example, with $a=2$ and $h=0.1$, the actual value differs from its first-order approximation by $0.01$.

## Core concept 5. A multivariable first-order approximation is a gradient inner product

If $f:\mathbb R^n\to\mathbb R$ is differentiable at point $\mathbf x$ and $\Delta\mathbf x$ is small, then

\[
f(\mathbf x+\Delta\mathbf x)
\approx
f(\mathbf x)
+
\nabla f(\mathbf x)^\top\Delta\mathbf x
\]

For two variables, this expands to

\[
\Delta f
\approx
f_x(x,y)\Delta x
+
f_y(x,y)\Delta y
\]

Multiply each small coordinate change by its corresponding partial derivative and add the results.

This connects partial differentiation, where one coordinate varies, to changes in several coordinates together. Both partial derivatives are calculated at the same reference point $(x,y)$ before movement. Multiplying $f_x$ by $\Delta x$ and $f_y$ by $\Delta y$ gives predicted componentwise changes whose sum is the scalar $\Delta f$.

Changes not explained by the first-order expression enter the remainder. For the function in Example 3, $\Delta x^2+\Delta x\Delta y$ remains, revealing a square term and interaction between the coordinates. Differentiability alone does not imply that the remainder is necessarily a quadratic expression. It guarantees that the remainder's ratio to displacement magnitude tends to 0.

## Core concept 6. The chain rule gives the same first-order change

Moving along unit direction $\mathbf v$ with $\Delta\mathbf x=t\mathbf v$ gives

\[
f(\mathbf x+t\mathbf v)
\approx
f(\mathbf x)
+
t\nabla f(\mathbf x)^\top\mathbf v
\]

The inner product is the directional derivative

\[
D_{\mathbf v}f(\mathbf x)
=
\nabla f(\mathbf x)^\top\mathbf v
\]

so

\[
f(\mathbf x+t\mathbf v)
\approx
f(\mathbf x)+tD_{\mathbf v}f(\mathbf x)
\]

For path function $g(t)=f(\mathbf x+t\mathbf v)$, we have $g(0)=f(\mathbf x)$, and the chain rule gives $g'(0)=\nabla f(\mathbf x)^\top\mathbf v$. The last expression therefore applies the single-variable first-order approximation $g(t)\approx g(0)+g'(0)t$ along the path. Because $\mathbf v$ is a unit vector, the travel distance is $|t|$. Multivariable first-order Taylor approximation expresses this directional tangent information using one gradient.

## Core concept 7. Reference-point approximations for exponentials and logarithms

Approximating $f(x)=e^x$ at $a=0$ gives

\[
f(0)=1,
\qquad
f'(0)=1
\]

so

\[
e^h\approx1+h
\]

Including the second-order term, with $f''(0)=1$, gives

\[
e^h
\approx
1+h+\frac12h^2
\]

Approximating $f(x)=\log x$ at $a=1$ gives

\[
f(1)=0,
\qquad
f'(1)=1
\]

so

\[
\log(1+h)\approx h
\]

The logarithm's domain requires $1+h>0$.

Overlaying different-order approximations to the exponential function shows the second-order term capturing bending near the reference point.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Exponential function near zero compared with first-order and second-order Taylor polynomials sharing value and slope at zero](../../figures/assets/M01/M01-12-exponential-orders.svg)
  <figcaption>All three expressions share value 1 and slope 1 at 0. The purple quadratic also matches the second derivative value 1, capturing more of the green exponential function's bending. Even the quadratic is not an exact equality over the exponential function's entire domain.</figcaption>
</figure>

Even near the reference point, a logarithmic approximation cannot discard the domain condition.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Log one plus h and its tangent h near zero with the excluded domain boundary at h equals minus one](../../figures/assets/M01/M01-12-log-domain.svg)
  <figcaption>Near h=0, log(1+h) is close to h. As h approaches −1, however, the actual logarithm decreases sharply, and it is undefined over the reals when h≤−1. Being able to substitute a number into the linear approximation does not enlarge the original function's domain.</figcaption>
</figure>

## Core concept 8. Model linearization approximates a neighborhood of a selected point

Let $s(\mathbf x)$ be a model score. Its first-order approximation for input change $\Delta\mathbf x$ is

\[
s(\mathbf x+\Delta\mathbf x)-s(\mathbf x)
\approx
\nabla s(\mathbf x)^\top\Delta\mathbf x
\]

The right-hand side is the change predicted by the gradient calculated at the current input. Its agreement with an actual finite change depends on the size of $\Delta\mathbf x$, model curvature, and whether the movement crosses a nondifferentiable point.

Assigning contributions through componentwise gradient products depends on coordinates and the reference point. Accurate first-order approximation does not automatically mean accurate causal explanation.

For a function containing ReLU, crossing a nondifferentiable point can invalidate the linear expression from the current region.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![ReLU and its linearization at a positive input diverging after a finite move crosses zero](../../figures/assets/M01/M01-12-relu-boundary.svg)
  <figcaption>The line formed from slope 1 at x=0.5 is exact in the positive-input region. Moving to x=−0.5 makes the line predict −0.5, while the actual ReLU output is 0. The blue vertical line marks the error for this movement.</figcaption>
</figure>

## Example 1. A first-order approximation to the square function

Approximate $f(x)=x^2$ at $a=3$.

\[
f(3)=9,
\qquad
f'(3)=6
\]

Therefore,

\[
f(3+h)\approx9+6h
\]

For $h=0.1$, the approximate value is $9.6$, while the actual value is

\[
3.1^2=9.61
\]

The first-order approximation error is $0.01$.

## Example 2. When a second-order term removes the error

For the same function, $f''(x)=2$. The second-order approximation is

\[
f(3+h)
\approx
9+6h+\frac12\cdot2h^2
\]

Substituting $h=0.1$ gives

\[
9+0.6+0.01=9.61
\]

For a quadratic function, the second-order Taylor expression equals the actual value.

## Example 3. A multivariable first-order approximation

For

\[
f(x,y)=x^2+xy
\]

the gradient is

\[
\nabla f(x,y)
=
\begin{bmatrix}
2x+y\\
x
\end{bmatrix}
\]

At reference point $(1,2)$,

\[
f(1,2)=3,
\qquad
\nabla f(1,2)=
\begin{bmatrix}4\\1\end{bmatrix}
\]

For $\Delta\mathbf x=(0.1,-0.2)^\top$,

\[
\Delta f
\approx
\begin{bmatrix}4&1\end{bmatrix}
\begin{bmatrix}0.1\\-0.2\end{bmatrix}
=0.2
\]

so the new function value is approximated as $3.2$. The actual value is

\[
f(1.1,1.8)=1.21+1.98=3.19
\]

The error, defined as `actual value − approximate value`, is therefore $-0.01$.

Scaling the same two-coordinate displacement by t allows separate comparisons of the predicted first-order change and the remainder.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Actual and linearized output along a two-coordinate displacement above the negative quadratic interaction residual](../../figures/assets/M01/M01-12-multivariable-path-residual.svg)
  <figcaption>The example's displacement (0.1,−0.2) corresponds to t=1. The lower plot separates the small gap between predicted value 3.20 and actual value 3.19 as remainder −0.01. Along this path, Δx²+ΔxΔy=−0.01t², and increasing movement size in the same direction increases the error magnitude.</figcaption>
</figure>

## Example 4. Predicting a loss change

Suppose that at the current parameters,

\[
\nabla\mathcal L=
\begin{bmatrix}2\\-3\end{bmatrix},
\qquad
\Delta\boldsymbol\theta=
\begin{bmatrix}-0.1\\0.05\end{bmatrix}
\]

The first-order loss change is

\[
\Delta\mathcal L
\approx
\begin{bmatrix}2&-3\end{bmatrix}
\begin{bmatrix}-0.1\\0.05\end{bmatrix}
\]

\[
=
-0.2-0.15
=-0.35
\]

Whether the loss actually decreases by $0.35$ must be checked at the new parameters.

## Common misconceptions

### Misconception 1. A Taylor approximation is exact at every input

An approximation is built from local information near the reference point. A larger displacement can increase the influence of omitted terms.

### Misconception 2. $f(a+h)\approx f(a)+f'(a)$

The derivative must be multiplied by displacement $h$. The first-order change term is $f'(a)h$.

### Misconception 3. A large second derivative means a large function value

The second derivative describes the rate of slope change and curvature. The function value's magnitude is separate.

### Misconception 4. A gradient inner product gives the exact finite change

The gradient inner product is a first-order approximation. Its difference from the actual change depends on curvature and displacement.

### Misconception 5. Accurate first-order approximation establishes each input component's causal effect

Numerical approximation accuracy validates a prediction of local function change. Componentwise causal effects require intervention design and justification of the chosen reference point.

## Exercises

### 1. A first-order Taylor expression

Given $f(a)=5$ and $f'(a)=-2$, write a first-order approximation for $f(a+h)$ and calculate its value at $h=0.1$.

<details>
<summary>Show solution</summary>

\[
f(a+h)\approx f(a)+f'(a)h
=
5-2h
\]

For $h=0.1$,

\[
f(a+0.1)\approx5-0.2=4.8
\]

</details>

### 2. Approximating a square and calculating its error

Use a first-order approximation of $f(x)=x^2$ at $a=2$ to predict $f(2.05)$. Calculate the error as `actual value − approximate value`.

<details>
<summary>Show solution</summary>

We have $f(2)=4$, $f'(2)=4$, and $h=0.05$.

\[
f(2.05)\approx4+4(0.05)=4.2
\]

The actual value is

\[
2.05^2=4.2025
\]

so the error is

\[
4.2025-4.2=0.0025
\]

This equals $h^2$.

</details>

### 3. A second-order Taylor approximation

Given $f(0)=1$, $f'(0)=2$, and $f''(0)=-4$, write the second-order Taylor approximation to $f(h)$ and evaluate it at $h=0.1$.

<details>
<summary>Show solution</summary>

\[
f(h)
\approx
1+2h+\frac12(-4)h^2
=
1+2h-2h^2
\]

For $h=0.1$,

\[
f(0.1)\approx1+0.2-0.02=1.18
\]

</details>

### 4. Approximating an exponential

Approximate $e^{0.02}$ using the first-order Taylor expression at $a=0$.

<details>
<summary>Show solution</summary>

Since $e^h\approx1+h$,

\[
e^{0.02}\approx1.02
\]

This is a first-order approximation for small positive $h$.

</details>

### 5. A multivariable first-order approximation

At point $\mathbf x$, we have $f(\mathbf x)=10$ and

\[
\nabla f(\mathbf x)=
\begin{bmatrix}1\\-2\end{bmatrix},
\qquad
\Delta\mathbf x=
\begin{bmatrix}0.3\\0.1\end{bmatrix}
\]

Find a first-order approximation to $f(\mathbf x+\Delta\mathbf x)$.

<details>
<summary>Show solution</summary>

\[
\nabla f(\mathbf x)^\top\Delta\mathbf x
=
1(0.3)+(-2)(0.1)
=0.1
\]

Therefore,

\[
f(\mathbf x+\Delta\mathbf x)
\approx
10+0.1
=10.1
\]

</details>

### 6. Approximation along a direction

At point $\mathbf x$, $D_{\mathbf v}f(\mathbf x)=-3$, and $\mathbf v$ is a unit vector. Approximate the function-value change to first order when moving by $t=0.04$ in that direction.

<details>
<summary>Show solution</summary>

Since

\[
f(\mathbf x+t\mathbf v)-f(\mathbf x)
\approx
tD_{\mathbf v}f(\mathbf x)
\]

we have

\[
\Delta f\approx0.04(-3)=-0.12
\]

The function value is predicted to decrease by approximately $0.12$.

</details>

### 7. Assessing a linearization claim

At one input, a gradient-based first-order approximation accurately predicts the actual output change under a small perturbation $\Delta\mathbf x$. A researcher claims, “This model is linear throughout the input space, and each gradient component is the causal effect of its feature.” Critique the conclusion.

<details>
<summary>Show solution</summary>

The result supports the statement that the first-order Taylor approximation was accurate at the selected input within the small perturbation range. Whether the same error holds at other inputs or under large perturbations remains unestablished.

Gradient components are coordinatewise local sensitivities. Causal-effect claims require separate investigation of feature interventions, comparison conditions, and the data-generating process.

</details>

## Lesson summary

- The first-order Taylor approximation $f(a+h)\approx f(a)+f'(a)h$ predicts nearby values using a tangent.
- The second-order term $\frac12f''(a)h^2$ accounts for curvature effects in a single-variable function.
- The multivariable first-order approximation is $f(\mathbf x+\Delta\mathbf x)\approx f(\mathbf x)+\nabla f(\mathbf x)^\top\Delta\mathbf x$.
- The remainder is the part omitted by the approximation and may become nonnegligible as displacement increases.
- Numerical linearization accuracy and a feature's causal importance are different claims.

## Pass criteria

You have passed this lesson if you can answer these questions without consulting the material:

- Can you write a single-variable first-order Taylor approximation as a tangent equation?
- Can you explain what it means for the remainder to become small near the reference point?
- Can you explain the roles of the second derivative and second-order Taylor term?
- Can you approximate a multivariable first-order change using a gradient inner product?
- Can you distinguish approximation error from causal-explanation claims?

## Next lesson

- [M01-13. Numerical differentiation and error](M01-13-numerical-differentiation-error.md)

## Author checklist

- [x] The learning objectives describe observable actions.
- [x] Reference points, displacements, second derivatives, and remainders are defined.
- [x] Single-variable and multivariable Taylor approximations are distinguished.
- [x] Square-function, exponential, and gradient approximations have been checked.
- [x] Every exercise has a solution.
- [x] Linearization accuracy is distinguished from causal claims.
- [x] The glossary and notation rules are followed.
- [x] Multivariable second-order Taylor expressions and Hessians are not required.
- [x] Internal links and mathematical delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
