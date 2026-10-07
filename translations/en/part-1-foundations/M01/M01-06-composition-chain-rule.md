---
id: "M01-06"
title: "Composite functions and the chain rule"
part: 1
stage: "M01"
status: "complete"
prerequisites:
  - "M00-08"
  - "M01-05"
estimated_time: "105~125 minutes"
---

# M01-06. Composite functions and the chain rule

## Why this lesson matters

A neural network passes one function's output into the next function. Finding the rate of change from input to loss requires connecting the local rates along the path. The chain rule expresses this connection as a product.

Differentiating only the outer function of a composite omits how much the inner function changes its input. Writing the calculation as separate stages lets us use the same rule for nested expressions and small computation graphs.

## Learning objectives

After completing this lesson, you will be able to:

- Identify the inner and outer functions in a composite function.
- Write the chain rule using function notation and intermediate variables.
- Calculate derivatives of two-stage and three-stage composite functions.
- Multiply local derivatives along a path in a computation graph.
- Explain the scope of model-interpretation claims supported by a rate of change obtained using the chain rule.

## Prerequisite check

- Prerequisite lesson: [M00-08 Function composition and inverse functions](../M00/M00-08-composition-inverse.md)
- Prerequisite lesson: [M01-05 Derivatives of sums, products, and quotients](M01-05-sum-product-quotient-rules.md)
- Check question: Can you explain which function is evaluated first in $(f\circ g)(x)$?
- Check question: Can you differentiate $x^n$, sums of functions, and products of functions?

If the order of function evaluation is unclear, first review M00-08.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| $(f\circ g)(x)$ | `f composed with g at x` | Function that first calculates $g(x)$, then applies $f$ to the result | $g(x)$ must lie in the domain of $f$. |
| $u=g(x)$ | `u equals g of x` | Intermediate value in the composition | $u$ depends on $x$. |
| $\frac{dy}{du}$ | `d y over d u` | Rate of change of output $y$ with respect to the outer function's input $u$ | Requires differentiability at the point concerned. |
| $\frac{du}{dx}$ | `d u over d x` | Rate of change of intermediate value $u$ with respect to input $x$ | Requires differentiability at the point concerned. |
| Chain rule | `chain rule` | Rule for finding a composite function's derivative as a product of local derivatives | The functions in the composition must be differentiable at the required points. |
| Local derivative | `local derivative` | Derivative of one calculation stage's output with respect to that stage's input | Corresponds to an edge of a computation graph. |

## Core concept 1. A composite function passes through an intermediate value

In

\[
y=f(g(x))
\]

$g$ is the inner function, and $f$ is the outer function. Introducing the intermediate variable

\[
u=g(x)
\]

gives the full calculation

\[
x\longmapsto u\longmapsto y
\]

with

\[
y=f(u)
\]

A change in input first changes $u$, and the change in $u$ changes $y$. The overall rate of change must include both stages.

## Core concept 2. The chain rule multiplies the rates at each stage

If $u=g(x)$ and $y=f(u)$ are differentiable at the required points,

\[
\frac{dy}{dx}
=
\frac{dy}{du}
\frac{du}{dx}
\]

In function notation,

\[
\frac{d}{dx}f(g(x))
=
f'(g(x))g'(x)
\]

The value $f'(g(x))$ is the derivative of the outer function $f$ evaluated at the intermediate value $g(x)$. The value $g'(x)$ is the rate at which the inner function converts an input change into an intermediate-value change.

Let a small input change be $\Delta x$. By the meaning of a derivative at a point, the intermediate change is $\Delta u\approx g'(x)\Delta x$. For the outer function, $\Delta y\approx f'(u)\Delta u$. Substituting the first relation gives

\[
\Delta y\approx f'(g(x))g'(x)\Delta x
\]

The two stages pass the input change along in sequence, so their rates are multiplied. This also explains why $f'$ is evaluated at $g(x)$ rather than $x$: the outer function receives the value produced by the inner function, not the original input directly. This explanation using changes is a local approximation under differentiability. It does not turn the two approximations into exact equalities over a finite interval.

The derivative notation appears to connect like fractions, but the relationship is guaranteed by the chain rule. Do not treat the appearance of the symbols as a rule allowing cancellation of $du$ in arbitrary expressions.

## Core concept 3. Separate the calculation stages to avoid missing factors

Suppose we differentiate

\[
y=(3x+1)^4
\]

Proceed in the following order.

1. Set the inner function to $u=3x+1$.
2. Write the outer function as $y=u^4$.
3. Find the local derivatives.

\[
\frac{dy}{du}=4u^3,
\qquad
\frac{du}{dx}=3
\]

4. Multiply them, then substitute $u=3x+1$ back in.

\[
\frac{dy}{dx}
=
4u^3\cdot3
=
12(3x+1)^3
\]

Differentiating only the outer function gives $4(3x+1)^3$, which omits the inner rate of change $3$.

## Core concept 4. Units of rates of change also multiply along the path

Suppose $x$ has units of seconds, intermediate value $u$ has units of meters, and output $y$ has units of score.

\[
\frac{du}{dx}
\quad\text{units: meters/second}
\]

\[
\frac{dy}{du}
\quad\text{units: score/meter}
\]

Multiplying the two rates gives

\[
\frac{dy}{du}\frac{du}{dx}
\quad\text{units: score/second}
\]

The intermediate unit, meters, connects the two rates, leaving the units of the overall output and input. Checking units helps find incorrect variable connections and missing stages. Scalar rates have the same product when their order is reversed, so units alone cannot determine the order of the computation path.

In the figure below, check where the intermediate value's unit appears in each local rate.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Input seconds connect through intermediate meters to output score, while meters per second and score per meter multiply to score per second](../../figures/assets/M01/M01-06-unit-chain.svg)

<figcaption>The rate from input to intermediate value is meters/second, and the rate from intermediate value to output is score/meter. Multiplying them connects the intermediate unit and leaves score/second.</figcaption>
</figure>

## Core concept 5. Multiply every derivative on paths with three or more stages

For

\[
x\longmapsto u=g(x)
\longmapsto v=h(u)
\longmapsto y=f(v)
\]

we have

\[
\frac{dy}{dx}
=
\frac{dy}{dv}
\frac{dv}{du}
\frac{du}{dx}
\]

In function notation,

\[
\frac{d}{dx}f(h(g(x)))
=
f'(h(g(x)))
h'(g(x))
g'(x)
\]

If one intermediate derivative is $0$, the entire product is $0$. If the absolute values of successive derivatives remain below $1$, their product can become small; if they remain above it, their product can grow. We will return to this product structure when studying vanishing and exploding gradients in deep neural networks.

The figure below compares products along one scalar path whose local rates are fixed at 0.5 or 2. The vertical axis uses a logarithmic scale to display the wide range of products.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Products of repeated local slopes one half shrink with stage count while products of repeated slope two grow](../../figures/assets/M01/M01-06-depth-products.svg)

<figcaption>At 8 stages, the product of 0.5 values is 1/256, while the product of 2 values is 256. The figure illustrates a scalar path's product structure; it is not a measurement of a whole neural network's gradient.</figcaption>
</figure>

## Core concept 6. Distinguish the chain rule from the product rule

The expression

\[
u(x)v(x)
\]

multiplies two function values. Use the product rule,

\[
u'v+uv'
\]

The expression

\[
f(g(x))
\]

passes one function's output into another. Use the chain rule,

\[
f'(g(x))g'(x)
\]

Both structures can occur in one expression. For example, in

\[
x^2(x+1)^3
\]

apply the product rule to the outer product and the chain rule when differentiating $(x+1)^3$.

The figure below shows a product computation in which both functions receive the same input independently. Compare its paths with a composition, where one function's output becomes the next function's input.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Input three branches into x squared and two x plus one before multiplying their outputs nine and seven to obtain sixty-three](../../figures/assets/M01/M01-06-product-branches.svg)

<figcaption>The branch values 9 and 7 multiply to give 63. An input change affects both branches, so the derivative adds the contributions 6×7 and 9×2 to give 60.</figcaption>
</figure>

## Core concept 7. Separate forward values from local derivatives in a computation graph

Consider the computation graph

\[
x\longrightarrow u=2x+1
\longrightarrow y=u^2
\]

At $x=3$, the forward calculation gives

\[
u=2\cdot3+1=7,
\qquad
y=7^2=49
\]

The local derivatives on its edges are

\[
\frac{du}{dx}=2,
\qquad
\frac{dy}{du}=2u=14
\]

The derivative from input to output is

\[
\frac{dy}{dx}
=
14\cdot2
=28
\]

Backpropagation in neural networks starts at the output and multiplies these local derivatives in reverse order. On one scalar path, multiplication order does not affect the numerical value. When we later study vector and matrix derivatives, however, shapes and multiplication order must be respected.

In the figure below, distinguish the calculated values inside the boxes from the local rates between the boxes.

<figure class="lesson-figure" markdown="1">

![Forward values three seven and forty-nine pass through two stages while local derivatives two and fourteen multiply to the total derivative twenty-eight](../../figures/assets/M01/M01-06-values-and-derivatives.svg)

<figcaption>The forward values are 3→7→49, and the overall rate is 14×2=28. The outer square function's derivative 2u is evaluated at intermediate value u=7, not at the original input 3.</figcaption>
</figure>

## Core concept 8. The chain rule requires differentiability conditions

If $g$ is differentiable at $x=a$ and $f$ is differentiable at $u=g(a)$, then $f\circ g$ is differentiable at $a$, and the chain rule applies.

If an intermediate function has a corner, the formula cannot simply be applied mechanically. For example,

\[
y=\operatorname{ReLU}(2x)
\]

reaches ReLU's corner at $0$ when $x=0$. The mathematical derivative does not exist at that point. Even if a framework specifies a value to use at $0$, distinguish that choice from mathematical differentiability.

The conditions above are sufficient for applying the chain rule formula. A nondifferentiable stage does not imply that every resulting composition is nondifferentiable. For example, composing $g(x)=|x|$ with $f(u)=u^2$ gives $f(g(x))=x^2$, which is differentiable even at $0$. We cannot insert $g'(0)$ into the formula, but we can differentiate the composite function itself to find the answer.

Compare the corner of the inner absolute value function with the smooth origin of its squared composition in the figure below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The inner absolute value curve has a corner at zero while its square is the smooth parabola x squared](../../figures/assets/M01/M01-06-smooth-composite.svg)

<figcaption>|x| is not differentiable at the origin, but (|x|)²=x² is. Distinguish the inability to apply the formula where the inner derivative does not exist from the differentiability of the composite function itself.</figcaption>
</figure>

## Example 1. A linear function inside a quadratic function

For

\[
f(x)=(2x-3)^2
\]

set $u=2x-3$ and $f=u^2$. Since

\[
\frac{df}{du}=2u,
\qquad
\frac{du}{dx}=2
\]

we have

\[
f'(x)
=
2u\cdot2
=
4(2x-3)
\]

Expanding the original expression to $4x^2-12x+9$ and differentiating gives $8x-12$, which equals $4(2x-3)$.

## Example 2. A three-stage composition

For

\[
y=\bigl((x^2+1)^3-2\bigr)^2
\]

set

\[
u=x^2+1,
\qquad
v=u^3-2,
\qquad
y=v^2
\]

The local derivatives are

\[
\frac{du}{dx}=2x,
\qquad
\frac{dv}{du}=3u^2,
\qquad
\frac{dy}{dv}=2v
\]

Therefore,

\[
\frac{dy}{dx}
=
2v\cdot3u^2\cdot2x
\]

Substituting the intermediate variables back in gives

\[
\frac{dy}{dx}
=
12x(x^2+1)^2
\bigl((x^2+1)^3-2\bigr)
\]

## Example 3. Use the product rule and chain rule together

For

\[
p(x)=x^2(x+1)^3
\]

set $a(x)=x^2$ and $b(x)=(x+1)^3$. The chain rule gives

\[
b'(x)=3(x+1)^2
\]

Applying the product rule gives

\[
p'(x)
=
2x(x+1)^3
+
x^2\,3(x+1)^2
\]

Factoring gives

\[
p'(x)
=
x(x+1)^2(5x+2)
\]

## Example 4. A path from a parameter to a loss

For a scalar parameter $\theta$, let

\[
z=3\theta-1,
\qquad
\mathcal L=z^2
\]

The local derivatives are

\[
\frac{dz}{d\theta}=3,
\qquad
\frac{d\mathcal L}{dz}=2z
\]

The chain rule gives

\[
\frac{d\mathcal L}{d\theta}
=
2z\cdot3
=
6(3\theta-1)
\]

At $\theta=1$, $z=2$, and the loss derivative is $12$.

This value is a local rate for the specified computation path and point. It does not directly establish a causal role for the parameter in the data-generating process or provide rates of change at other inputs.

## Common misconceptions

### Misconception 1. Differentiating only the outer function is enough

Multiply the outer function's derivative by the inner function's derivative. Do not omit the factor $3$ in $(3x+1)^4$.

### Misconception 2. $f'(g(x))$ and $f'(x)$ are equal

Evaluate the outer function's derivative at the intermediate value $g(x)$. Unless $g(x)$ is specified to equal $x$, the two values differ.

### Misconception 3. A composite function and a product of functions use the same rule

Apply the chain rule to $f(g(x))$ and the product rule to $f(x)g(x)$. First check the outermost operation.

### Misconception 4. The overall rate can remain nonzero even if one path derivative is $0$

On a single path, the chain rule is a product of local derivatives. If one factor is $0$, that path's overall rate is also $0$. When several paths merge, examine each path's contribution separately.

### Misconception 5. A framework returning a derivative value establishes mathematical differentiability

A framework can specify a calculation rule at a point without a derivative, such as ReLU's corner. Distinguish the returned value from the existence of a derivative.

## Exercises

### 1. Identify the inner and outer functions

For

\[
y=(x^2+4)^5
\]

write the inner and outer functions and explain the order of calculation.

<details>
<summary>Show solution</summary>

The inner function is

\[
u=g(x)=x^2+4
\]

and the outer function is

\[
y=f(u)=u^5
\]

First calculate $u$ from $x$, then raise $u$ to the fifth power to obtain $y$.

</details>

### 2. Differentiate the square of a linear function

Find the derivative of

\[
f(x)=(5x-2)^2
\]

<details>
<summary>Show solution</summary>

Setting $u=5x-2$ gives $f=u^2$. Since

\[
\frac{df}{du}=2u,
\qquad
\frac{du}{dx}=5
\]

we have

\[
f'(x)
=
2u\cdot5
=
10(5x-2)
\]

</details>

### 3. Restore a missing inner derivative

For $g(x)=(x^2+1)^3$, a calculation gives $g'(x)=3(x^2+1)^2$. Identify and correct the error.

<details>
<summary>Show solution</summary>

The outer cube was differentiated, but the result was not multiplied by the derivative $2x$ of the inner function $x^2+1$.

\[
g'(x)
=
3(x^2+1)^2\cdot2x
=
6x(x^2+1)^2
\]

</details>

### 4. A three-stage chain rule

Find the derivative of

\[
y=\bigl((2x+1)^2+3\bigr)^4
\]

<details>
<summary>Show solution</summary>

Set

\[
u=2x+1,
\qquad
v=u^2+3,
\qquad
y=v^4
\]

The local derivatives are

\[
\frac{du}{dx}=2,
\qquad
\frac{dv}{du}=2u,
\qquad
\frac{dy}{dv}=4v^3
\]

Therefore,

\[
\frac{dy}{dx}
=
4v^3\cdot2u\cdot2
=
16u v^3
\]

Substituting the intermediate variables back in gives

\[
\frac{dy}{dx}
=
16(2x+1)
\bigl((2x+1)^2+3\bigr)^3
\]

</details>

### 5. Distinguish a product from a composition

Find the derivative of

\[
p(x)=x(x^2+1)^2
\]

and explain the order in which you used the rules.

<details>
<summary>Show solution</summary>

The outermost operation multiplies $x$ by $(x^2+1)^2$, so apply the product rule first. The second factor is a composite function, so use the chain rule for it.

\[
p'(x)
=
1\cdot(x^2+1)^2
+
x\bigl[2(x^2+1)\cdot2x\bigr]
\]

Therefore,

\[
p'(x)
=
(x^2+1)^2+4x^2(x^2+1)
\]

</details>

### 6. Local derivatives in a computation graph

For

\[
x\longrightarrow u=4x-1
\longrightarrow y=u^3
\]

at $x=2$, find $u$, $y$, $\frac{du}{dx}$, $\frac{dy}{du}$, and $\frac{dy}{dx}$.

<details>
<summary>Show solution</summary>

The forward values are

\[
u=4\cdot2-1=7,
\qquad
y=7^3=343
\]

The local derivatives are

\[
\frac{du}{dx}=4,
\qquad
\frac{dy}{du}=3u^2=147
\]

The overall derivative is

\[
\frac{dy}{dx}
=
147\cdot4
=588
\]

</details>

### 7. Evaluate a claim about a path's rate of change

At one input and one parameter state, the product of derivatives along a computation path is $0$. A researcher claims, "This input is unrelated to the model output at other states as well." Distinguish what has been established from what needs further investigation.

<details>
<summary>Show solution</summary>

The calculation supports a local derivative of $0$ for the selected input, parameter state, output, and path. If one stage on the path has a local derivative of $0$, that path's first-order rate of change can be blocked.

Rates for other outputs or paths, other input points, and other parameter states have not been checked. Nor can one local derivative determine the effect of a finite input change on the output. Broader claims require specifying the target output and path and examining derivatives at multiple points or results of direct interventions.

</details>

## Lesson summary

- The composite function $f(g(x))$ passes through the intermediate value $u=g(x)$ to calculate output $f(u)$.
- The chain rule is $\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}$: it multiplies the local derivatives at each stage.
- With three or more stages, multiply every derivative along the path from input to output.
- The product rule applies to products of function values; the chain rule applies to function composition.
- A path derivative in a computation graph is a local rate at a selected point. It does not guarantee global influence or a causal effect.

## Pass criteria

You pass if you can answer these questions without consulting the material:

- Can you identify the inner and outer functions in a composite function?
- Can you write the chain rule using function notation and intermediate variables?
- Can you calculate derivatives of two-stage and three-stage composite functions?
- Can you choose between the product rule and the chain rule from an expression's structure?
- Can you calculate forward values and local derivatives separately in a computation graph?

## Next lesson

The next lesson is [M01-07 Derivatives of exponential and logarithmic functions](M01-07-exponential-log-derivatives.md). Use the chain rule to calculate rates of change that appear in softmax and log-likelihood.

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Composite functions, intermediate variables, and local derivatives are defined before use.
- [x] Two-stage and three-stage chain rule calculations have been checked.
- [x] The product rule is distinguished from the chain rule.
- [x] Every exercise has a solution.
- [x] Local path rates are distinguished from global and causal claims.
- [x] The glossary and notation rules are followed.
- [x] Neither derivatives of exponentials and logarithms nor multivariable differentiation are required as prerequisites.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
