---
id: "M01-03"
title: "Differentiation and instantaneous rates of change"
part: 1
stage: "M01"
status: "complete"
prerequisites:
  - "M01-01"
  - "M01-02"
estimated_time: "95~115 minutes"
---

# M01-03. Differentiation and instantaneous rates of change

## Why this lesson matters

An average rate of change summarizes the change between two inputs in a single value. Questions about how sensitive a model output is near the input $x=2$, or how fast an object is moving at time $t=3$, require a rate of change at a single point.

Differentiation finds the limit of an average rate of change as the distance between the two points approaches $0$. The resulting instantaneous rate of change is the slope of the tangent line. It is also the starting point for gradients and backpropagation, which we will study later.

## Learning objectives

After completing this lesson, you will be able to:

- Explain the derivative at a point as the limit of an average rate of change.
- Read $f'(a)$ and $\left.\frac{df}{dx}\right|_{x=a}$.
- Calculate derivatives at a point for constant functions, linear functions, and $f(x)=x^2$ from the definition.
- Interpret the derivative at a point as a tangent slope and an instantaneous rate of change.
- Compare left-hand and right-hand derivatives to determine differentiability.

## Prerequisite check

- Prerequisite lesson: [M01-01 Changes and average rates of change](M01-01-change-average-rate.md)
- Prerequisite lesson: [M01-02 Intuition for limits](M01-02-limits-intuition.md)
- Check question: For $f(x)=x^2$, can you write the average rate of change from $x=2$ to $x=2+h$?
- Check question: Can you explain the difference between $h\to0$ and $h=0$?

If these questions are difficult, first review the definitions of change and a limit.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Range and conditions |
|---|---|---|---|
| $h$ | `h` | Change added to the reference input | Take the limit through values with $h\ne0$. |
| $f'(a)$ | `f prime of a` | Derivative at $x=a$ | The limit must exist as a finite real number. |
| $\left.\frac{df}{dx}\right\rvert_{x=a}$ | `d f over d x evaluated at x equals a` | Rate of change of $f$ with respect to $x$ at $x=a$ | The same value as $f'(a)$. |
| $\lvert r\rvert$ | `the absolute value of r` | Magnitude of a real number $r$, without its sign | $\lvert r\rvert\ge0$ |
| Differentiation | `differentiation` | Process of finding an instantaneous rate of change | Check that the limit exists. |
| Derivative at a point | `the derivative at a point` | Instantaneous rate of change at one point | A scalar value. |
| Tangent line | `tangent line` | Line representing the local direction of a curve at one point | Its slope is $f'(a)$ when the function is differentiable. |
| Differentiable | `differentiable` | Having a derivative at a point | The left-hand and right-hand rates of change must have the same finite value. |

## Core concept 1. The derivative at a point is the limit of average rates of change

Changing the input $x=a$ by $h$ gives the endpoint $a+h$. The average rate of change between the two points is

\[
\frac{f(a+h)-f(a)}{h},
\qquad h\ne0
\]

If this ratio approaches a single finite value as $h$ approaches $0$, we define that value as the derivative at $a$.

\[
f'(a)
\coloneqq
\lim_{h\to0}
\frac{f(a+h)-f(a)}{h}
\]

The numerator $f(a+h)-f(a)$ is the change in output, and the denominator $h$ is the change in input. The expression narrows the ratio of these changes to the neighborhood of a single point.

While taking the limit, we hold the reference point $a$ fixed and vary only the gap $h$. Values with $h>0$ examine the right side of $a$, while values with $h<0$ examine the left side. At a differentiable point, both the input change and the output change approach $0$, but their ratio need not approach $0$. The derivative does not ask whether the output disappears. It describes how much the output changes relative to the change in input.

We do not substitute $h=0$ into the fraction. We calculate the rate of change for each $h\ne0$, then examine where those values go as $h\to0$.

## Core concept 2. Derivative notation presents the same value from different perspectives

When $y=f(x)$, the following expressions can refer to the same derivative value:

\[
f'(x),
\qquad
\frac{df}{dx},
\qquad
\frac{dy}{dx}
\]

The notation $f'(x)$ emphasizes that this is the derivative of the function $f$. The notation $\frac{df}{dx}$ emphasizes the rate at which the output $f$ changes as the input $x$ changes. To evaluate it at a point $a$, we write

\[
f'(a)
=
\left.\frac{df}{dx}\right|_{x=a}
\]

The vertical bar on the right of $\left.\frac{df}{dx}\right|_{x=a}$ means to substitute $x=a$ into the derivative after calculating it. It does not mean to take an absolute value. First find the rate of change as a function of the input, then select the value at the reference point $a$.

Although $\frac{df}{dx}$ looks like an ordinary fraction, at this stage we read it as a single derivative notation. Later, the chain rule will introduce calculation rules that resemble operations on fractions. This does not allow us to cancel $df$ and $dx$ as if they were independent numbers in any expression.

## Core concept 3. The derivative at a point is the slope of the tangent line

The secant line through the two points on the curve

\[
(a,f(a)),
\qquad
(a+h,f(a+h))
\]

has slope

\[
\frac{f(a+h)-f(a)}{h}
\]

As $h$ approaches $0$, the second point approaches the first. If the limit of the secant slopes exists, we use it as the tangent slope.

The equation of the tangent line at $x=a$ is

\[
y-f(a)=f'(a)(x-a)
\]

Comparing a point $(x,y)$ on the tangent line with the reference point $(a,f(a))$, the horizontal change is $x-a$ and the vertical change is $y-f(a)$. On a straight line, the vertical change equals the slope times the horizontal change, which gives the equation above. Substituting $x=a$ gives $y=f(a)$, confirming that the tangent line passes through the reference point. Here, $y$ is the height on the tangent line; at other inputs, it need not equal the original function value $f(x)$.

The tangent line does not represent the entire curve. It represents the direction of the function as a straight line in a region close to $a$.

### Visual intuition: a secant line approaches a tangent line

<figure class="lesson-figure" markdown="1">

![A secant line approaching the tangent line on the curve f of x equals x squared](../../figures/assets/M01/M01-03-secant-to-tangent.svg)

<figcaption>As h becomes smaller, the slope of the orange secant through the two points approaches the slope of the blue tangent at the reference point a.</figcaption>
</figure>

The moving point in the figure is the second point, $(a+h,f(a+h))$. The reference point $(a,f(a))$ stays fixed, while the horizontal gap $h$ and the vertical gap $f(a+h)-f(a)$ shrink together. The two points do not merge in a way that lets us measure a slope directly. We ask whether the limit of secant slopes with $h\ne0$ converges to one value.

A tangent line therefore does not have to intersect the curve twice. It is a local linear model with the same first-order change as the function at a differentiable point. This perspective extends to Taylor approximation and the Jacobian in later lessons.

## Core concept 4. Differentiate $f(x)=x^2$ from the definition

Use a general reference point $x$ and calculate the difference quotient.

\[
\frac{f(x+h)-f(x)}{h}
=
\frac{(x+h)^2-x^2}{h}
\]

Expand the numerator.

\[
(x+h)^2-x^2
=
x^2+2xh+h^2-x^2
=
2xh+h^2
\]

For $h\ne0$,

\[
\frac{2xh+h^2}{h}
=
2x+h
\]

Now take the limit as $h\to0$.

\[
f'(x)
=
\lim_{h\to0}(2x+h)
=
2x
\]

The derivative at $x=a$ is therefore $f'(a)=2a$. The instantaneous rate of change varies with the reference point.

## Core concept 5. Constant and linear functions

For a constant function $f(x)=c$, changing the input does not change the output.

\[
\frac{f(x+h)-f(x)}{h}
=
\frac{c-c}{h}
=0
\]

Therefore,

\[
f'(x)=0
\]

For a linear function $f(x)=mx+b$,

\[
\frac{f(x+h)-f(x)}{h}
=
\frac{m(x+h)+b-(mx+b)}{h}
=
\frac{mh}{h}
=m
\]

so

\[
f'(x)=m
\]

The slope of a straight line is the same at every point.

Compare the horizontal line and the sloping line below. Moving the reference point leaves the slope of each line unchanged.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A constant function has slope zero at every point and a linear function two x plus one has slope two at every point](../../figures/assets/M01/M01-03-constant-and-linear.svg)

<figcaption>Two output values of a constant function are always equal, so the change is 0. For a linear function, the ratio of output change to input change is constant regardless of the reference point.</figcaption>
</figure>

## Core concept 6. Differentiability implies continuity

Suppose $f'(a)$ exists. For $h\ne0$, we can write the change in output as

\[
f(a+h)-f(a)
=
\frac{f(a+h)-f(a)}{h}\,h
\]

As $h\to0$, the first factor approaches the finite value $f'(a)$, and the second factor $h$ approaches $0$. Therefore,

\[
f(a+h)-f(a)\to0
\]

and $f(a+h)\to f(a)$. Thus, $f$ is continuous at $a$.

The converse does not hold. A continuous function can have a corner or a sharp point at which no single tangent slope can be assigned.

## Core concept 7. Compare left-hand and right-hand derivatives

The rate of change obtained by approaching from the left with $h\to0^-$ is the left-hand derivative. Approaching from the right with $h\to0^+$ gives the right-hand derivative.

\[
f'_-(a)
=
\lim_{h\to0^-}
\frac{f(a+h)-f(a)}{h}
\]

\[
f'_+(a)
=
\lim_{h\to0^+}
\frac{f(a+h)-f(a)}{h}
\]

The derivative $f'(a)$ exists when these values are the same finite number.

Let ReLU be $r(x)=\max(0,x)$. We have $r(0)=0$. For $h<0$, $r(h)=0$, so

\[
\frac{r(h)-r(0)}{h}=0
\]

For $h>0$, $r(h)=h$, so

\[
\frac{r(h)-r(0)}{h}=1
\]

The left-hand derivative is $0$ and the right-hand derivative is $1$, so ReLU is not differentiable at $0$.

A neural network implementation chooses a value to use for backpropagation at ReLU's $0$. This is a rule chosen by the implementation, not evidence that a mathematical derivative exists there.

In the figure below, check the connection between the function values separately from the slopes of the two line segments.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![ReLU joins continuously at zero while the left slope is zero and the right slope is one](../../figures/assets/M01/M01-03-relu-corner.svg)

<figcaption>The function values on both sides approach 0, so ReLU is continuous. The left slope of 0 and the right slope of 1 differ, however, so there is no derivative at the origin.</figcaption>
</figure>

## Core concept 8. The derivative at a point describes local sensitivity

Let the model score be $s(x)$. If $s'(a)=4$, a small change $\Delta x$ in the input near $a$ produces an output change of approximately $4\Delta x$. We will study the precise approximation formula in the lesson on Taylor approximation.

This interpretation follows from the definition: the average rate of change approaches $4$. If the ratio of output change to input change is approximately $4$, the output change is approximately the input change multiplied by $4$. Conversely, $s'(a)=0$ means that this ratio approaches $0$, not that the function is constant nearby. For $s(x)=x^2$, we have $s'(0)=0$, but the output differs at inputs other than $0$.

Compare the horizontal tangent and the upward-curving graph below to distinguish what a derivative value of 0 says about the function.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The parabola x squared has a horizontal tangent at zero but nonzero neighboring outputs at inputs plus or minus one half](../../figures/assets/M01/M01-03-zero-slope-not-constant.svg)

<figcaption>The tangent slope at the origin is 0, but the function value at x=±0.5 is 0.25. A derivative value of 0 does not mean that the entire nearby function is a horizontal line.</figcaption>
</figure>

The units of a derivative are the output units divided by the input units. If the input is a temperature in degrees Celsius and the output is a score, $s'(a)$ has units of `score/degree Celsius`.

A large $|s'(a)|$ is evidence that the output is sensitive in the selected input direction near the selected point. This value alone does not establish robustness over a broad input region, average behavior on real data, or the causal effect of that feature.

## Example 1. The tangent to a quadratic function at $x=3$

For $f(x)=x^2$, we have $f'(x)=2x$. At $x=3$,

\[
f(3)=9,
\qquad
f'(3)=6
\]

The tangent line satisfies

\[
y-9=6(x-3)
\]

so

\[
y=6x-9
\]

This line passes through $(3,9)$ and has slope $6$.

In the figure below, check that the tangent passes through the reference point while separating from the curve at other inputs.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The tangent six x minus nine touches x squared at three comma nine and differs from the curve away from that base point](../../figures/assets/M01/M01-03-tangent-at-three.svg)

<figcaption>The orange reference point (3, 9) and the slope of 6 determine the purple tangent. It has the same slope as the curve at that point but does not replace the entire curve.</figcaption>
</figure>

## Example 2. Instantaneous velocity

Suppose the position at time $t$ is

\[
p(t)=t^2
\]

in meters. The average velocity from $t=a$ to $t=a+h$ is

\[
\frac{p(a+h)-p(a)}{h}
=
2a+h
\]

As $h\to0$, the instantaneous velocity is

\[
p'(a)=2a
\]

in meters per second. At $a=3$ seconds, it is $6$ meters per second.

## Example 3. The rate of change of a loss with respect to a parameter

Let the loss for a scalar parameter $\theta$ be

\[
\mathcal L(\theta)=(\theta-2)^2
\]

Calculating the difference quotient from the definition gives

\[
\frac{\mathcal L(\theta+h)-\mathcal L(\theta)}{h}
=
\frac{(\theta+h-2)^2-(\theta-2)^2}{h}
\]

With $u=\theta-2$, the numerator is $(u+h)^2-u^2=2uh+h^2$. Therefore,

\[
\mathcal L'(\theta)
=
2(\theta-2)
\]

At $\theta=5$, we have $\mathcal L'(5)=6$. This provides local information: near $\theta=5$, the loss increases in the direction of increasing $\theta$.

## Common misconceptions

### Misconception 1. Substitute $h=0$ to find an instantaneous rate of change

Substituting $h=0$ into the difference quotient makes the denominator $0$. Calculate the expression for $h\ne0$, then take the limit as $h\to0$.

### Misconception 2. $f'(a)$ exists

If the left-hand and right-hand rates of change differ, or if the rate of change grows without bound, no finite derivative exists at that point.

### Misconception 3. Continuity implies differentiability

Continuity rules out a break in the function values. ReLU is continuous at $0$, but its different left and right slopes make it nondifferentiable there.

### Misconception 4. A large derivative value means that the input causes the output

A derivative value describes local sensitivity for a specified function and point. A causal claim requires a separately specified intervention target, control conditions, and data-generating process.

## Exercises

### 1. Read derivative notation

Explain

\[
f'(2)
=
\left.\frac{df}{dx}\right|_{x=2}
=-3
\]

in an English sentence.

<details>
<summary>Show solution</summary>

The derivative of the function $f$ at $x=2$ is $-3$. Near the point where the input is $2$, a small increase in $x$ gives a decrease in the output of approximately $3$ times the input change. On the graph, the tangent at $(2,f(2))$ has slope $-3$.

</details>

### 2. Differentiate a linear function from the definition

Find the derivative of $f(x)=3x+2$ using the definition of the difference quotient.

<details>
<summary>Show solution</summary>

\[
\frac{f(x+h)-f(x)}{h}
=
\frac{3(x+h)+2-(3x+2)}{h}
\]

\[
=
\frac{3h}{h}
=3,
\qquad h\ne0
\]

The value remains $3$ as $h\to0$, so

\[
f'(x)=3
\]

The original function is a straight line with slope $3$, so its instantaneous rate of change is the same at every point.

</details>

### 3. The derivative of a quadratic function at a point

For $f(x)=x^2$, find $f'(-1)$ and interpret its sign.

<details>
<summary>Show solution</summary>

Since $f'(x)=2x$,

\[
f'(-1)=-2
\]

Near $x=-1$, increasing the input moves the function value in the decreasing direction. The tangent slope is also $-2$.

</details>

### 4. The equation of a tangent line

Find the equation of the tangent to $f(x)=x^2$ at $x=1$.

<details>
<summary>Show solution</summary>

The point has coordinates

\[
(1,f(1))=(1,1)
\]

and the tangent slope is

\[
f'(1)=2
\]

Substitute the point and slope into the tangent equation.

\[
y-1=2(x-1)
\]

Therefore,

\[
y=2x-1
\]

</details>

### 5. Differentiability of the absolute value function

Use the left-hand and right-hand derivatives to determine whether $g(x)=|x|$ is differentiable at $x=0$.

<details>
<summary>Show solution</summary>

We have $g(0)=0$. For $h<0$, $|h|=-h$, so

\[
\frac{g(h)-g(0)}{h}
=
\frac{-h}{h}
=-1
\]

The left-hand derivative is $-1$.

For $h>0$, $|h|=h$, so the difference quotient is $1$. The right-hand derivative is $1$. Since the two values differ, $g'(0)$ does not exist.

</details>

### 6. A derivative with units

Time $t$ is measured in seconds, and temperature $T(t)$ is measured in degrees Celsius. Explain the units and meaning of $T'(10)=-0.4$.

<details>
<summary>Show solution</summary>

The units are `degrees Celsius/second`. Near $t=10$ seconds, a small increase in time moves the temperature in the decreasing direction at a rate of $0.4$ degrees Celsius per second. This value alone does not establish that the temperature decreases at the same rate over a long period.

</details>

### 7. Evaluate a claim about model sensitivity

At one input $x=a$, the derivative of a model score is $s'(a)=20$. A researcher claims, "This input feature is the key cause of predictions across all data." Explain what the result directly supports and what additional evidence is needed.

<details>
<summary>Show solution</summary>

The value $s'(a)=20$ supports a large local rate of change in the score at the selected point $a$ and in the selected input direction. If the input units are specified, interpret the rate of change with its units as well.

This result does not directly support sensitivity at other data points, an average effect under the real data distribution, or a causal effect. Broader claims require evaluations at multiple inputs, specification of the features and scales being compared, and controlled interventions with control conditions.

</details>

## Lesson summary

- The derivative at a point is the limit of the average rate of change $\frac{f(a+h)-f(a)}{h}$ as $h\to0$.
- $f'(a)$ and $\left.\frac{df}{dx}\right|_{x=a}$ give the same instantaneous rate of change at $x=a$.
- On a graph, the derivative at a point is the tangent slope. Its units are the output units divided by the input units.
- Differentiability implies continuity, but not every continuous function is differentiable.
- A derivative value at a point describes local sensitivity. It does not guarantee global behavior or a causal effect.

## Pass criteria

You pass if you can answer these questions without consulting the material:

- Can you explain why we do not substitute $h=0$ directly into the derivative definition?
- Can you read $f'(a)$ and $\left.\frac{df}{dx}\right|_{x=a}$?
- Can you find the derivative of $f(x)=x^2$ from the definition?
- Can you write a tangent equation using the derivative at a point?
- Can you determine ReLU's differentiability by comparing left-hand and right-hand derivatives?

## Next lesson

- [M01-04 Derivatives and graphs](M01-04-derivative-and-graphs.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Derivatives at a point and derivative notation are defined before use.
- [x] The condition $h\ne0$ is stated for the difference quotient.
- [x] Calculations for quadratic functions, linear functions, and ReLU have been checked.
- [x] Every exercise has a solution.
- [x] Local sensitivity is distinguished from causal claims.
- [x] The glossary and notation rules are followed.
- [x] No derivative rules beyond the prerequisites are required.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
