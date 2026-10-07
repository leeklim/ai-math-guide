---
id: "M01-09"
title: "The fundamental theorem of calculus"
part: 1
stage: "M01"
status: "complete"
prerequisites:
  - "M01-05"
  - "M01-07"
  - "M01-08"
estimated_time: "105~125 minutes"
---

# M01-09. The fundamental theorem of calculus

## Why this lesson matters

Differentiation finds a local rate of change, while integration accumulates a quantity over an interval. The fundamental theorem of calculus connects these operations. Integrating a continuous function from a starting point to the current point creates an accumulation function whose derivative is the original function. Knowing an antiderivative also lets you calculate a definite integral as the difference between its values at the endpoints.

This connection lets you calculate definite integrals of polynomials and exponential functions without finding the limit of a Riemann sum each time. The theorem has conditions involving continuity and differentiability, so read its formulas together with their scope of application.

## Learning objectives

After this lesson, you will be able to:

- Explain why an accumulation function's derivative equals its integrand.
- Distinguish an antiderivative from an indefinite integral and include the constant of integration.
- Calculate a definite integral using an antiderivative.
- Interpret the integral of a rate of change as the total change.
- Explain the scope of claims supported by accumulating local rates of change along a path.

## Prerequisite check

- Prerequisite lesson: [M01-05. Sum, product, and quotient rules](M01-05-sum-product-quotient-rules.md)
- Prerequisite lesson: [M01-07. Derivatives of exponential and logarithmic functions](M01-07-exponential-log-derivatives.md)
- Prerequisite lesson: [M01-08. Integration and accumulation](M01-08-integration-accumulation.md)
- Check question: Can you distinguish the roles of $t$ and $x$ in $A(x)=\int_a^x f(t)\,dt$?
- Check question: Can you find the derivatives of $x^n$ and $e^x$?

Review M01-08 first if accumulation functions and signed area are unclear.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| $A(x)=\int_a^x f(t)\,dt$ | `A of x equals the integral from a to x of f of t d t` | An accumulation function from starting point $a$ to endpoint $x$ | Part 1 of the fundamental theorem assumes that $f$ is continuous |
| $F'(x)=f(x)$ | `F prime of x equals f of x` | The relation stating that $F$ is an antiderivative of $f$ | Must hold on the interval in question |
| $\int f(x)\,dx$ | `the integral of f of x d x` | Notation for all antiderivatives of $f$ | Includes the constant of integration $C$ |
| $C$ | `C` | A constant of integration whose derivative is $0$ | An arbitrary real constant |
| $[F(x)]_a^b$ | `F of x evaluated from a to b` | An abbreviation for $F(b)-F(a)$ | Both endpoints must lie in the domain of $F$ |

## Core concept 1. A small change in accumulation is a thin strip

Suppose $f$ is continuous and

\[
A(x)=\int_a^x f(t)\,dt
\]

Moving the endpoint from $x$ to $x+h$ changes the accumulated value by

\[
A(x+h)-A(x)
=
\int_x^{x+h}f(t)\,dt
\]

The rate of change is

\[
\frac{A(x+h)-A(x)}{h}
=
\frac{1}{h}
\int_x^{x+h}f(t)\,dt
\]

For small $h$, the values $f(t)$ over the short interval are close to $f(x)$. The integral approaches the area of a thin rectangle of height $f(x)$ and width $h$.

\[
\int_x^{x+h}f(t)\,dt
\approx
f(x)h
\]

The rate of change therefore approaches $f(x)$. Taking the limit as $h\to0$ gives an exact equality.

For a rightward step with $h>0$, dividing the integral by the width $h$ gives the average height over the short interval. By continuity, all heights in that interval can be made as close to $f(x)$ as desired, so their average lies within the same range. The error after dividing the area by $h$ therefore also tends to $0$. When $h<0$, the integration direction and the denominator's sign both reverse, giving the average height over a short interval on the left. Both limits equal $f(x)$, determining the derivative of the accumulation function.

Dividing the thin strip's area by its width gives the average height over the interval. The next figure shows this average approaching the height at the starting point for a small positive width.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![A thin strip under t plus one compared with its starting-height rectangle and average height](../../figures/assets/M01/M01-09-thin-strip-average.svg)
  <figcaption>With starting point 1 and width 0.3, the actual area is 0.645 and the average height is 2.15. The dashed rectangle has height 2, the function value at the starting point. As the width shrinks, the average height approaches this value.</figcaption>
</figure>

## Core concept 2. Part 1 differentiates accumulation

If $f$ is continuous on $[a,b]$ and

\[
A(x)=\int_a^x f(t)\,dt
\]

then, for $a<x<b$,

\[
A'(x)=f(x)
\]

This is Part 1 of the fundamental theorem of calculus.

The $t$ inside the integral is a dummy variable. The variable of differentiation is the upper endpoint $x$. These two expressions describe the same accumulation function:

\[
\int_a^x f(t)\,dt
=
\int_a^x f(u)\,du
\]

At the starting point $a$, the accumulation function satisfies $A(a)=0$. The integral selects the antiderivative with this initial value.

Aligning the integrand and accumulation function from Example 1 at the same input shows the upper graph's height becoming the lower graph's slope.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An integrand t squared plus two above its accumulation function with tangent slope six at upper endpoint two](../../figures/assets/M01/M01-09-accumulation-derivative.svg)

<figcaption>On the upper graph, the height at input 2 is 6. The lower accumulation function is 0 at starting point 1, and its tangent slope at input 2 is the same value, 6. The accumulated value itself, 13/3, is a different quantity from this slope.</figcaption>

</figure>

## Core concept 3. An antiderivative differentiates to the integrand

A function $F$ satisfying

\[
F'(x)=f(x)
\]

on an interval is an antiderivative of $f$.

Because a constant has derivative $0$, if $F$ is an antiderivative, then $F+C$ is another antiderivative.

\[
\frac{d}{dx}[F(x)+C]
=
f(x)
\]

An indefinite integral denotes all the antiderivatives as follows:

\[
\int f(x)\,dx
=
F(x)+C
\]

An indefinite integral is not a scalar with fixed endpoints. It is a family of functions differing only by their constants of integration. A definite integral, by contrast, has a lower and upper endpoint and gives a scalar.

For another antiderivative $G$, we have $(G-F)'=f-f=0$. A function whose derivative is $0$ at every point of an interval is constant there, so $G-F=C$. Thus $F+C$ describes all antiderivatives on the same interval, not just some of them. Differentiation cannot distinguish a constant vertical shift, so recovering the original height requires an additional condition, such as a value at one point.

Shifting an antiderivative's height does not change its slope at the same input. Specifying an initial value selects one member of the family.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Three vertically shifted parabolas with equal tangent slopes and the zero initial value selecting x squared minus one](../../figures/assets/M01/M01-09-antiderivative-family.svg)
  <figcaption>All three functions differentiate to 2x. Their short tangents at input 1 are parallel, with slope 2. The condition that the accumulated value at starting point 1 is 0 selects x²−1.</figcaption>
</figure>

## Core concept 4. Part 2 calculates a definite integral from endpoint values

If $f$ and $F$ are continuous on $[a,b]$ and $F'(x)=f(x)$ in its interior, then

\[
\int_a^b f(x)\,dx
=
F(b)-F(a)
\]

This is Part 2 of the fundamental theorem of calculus. Its abbreviated notation is

\[
\int_a^b f(x)\,dx
=
[F(x)]_a^b
\]

The accumulation function $A$ from Part 1 also satisfies $A'=f$, so $F-A$ is constant. At the starting point, $A(a)=0$, so this constant is $F(a)$. Therefore,

\[
A(x)=F(x)-F(a)
\]

Substituting $x=b$ gives the endpoint-difference formula. The calculation concerns how much the antiderivative's height changes from the starting point to the endpoint, not the height itself.

Adding a constant of integration $C$ to the antiderivative gives

\[
[F(x)+C]_a^b
=
[F(b)+C]-[F(a)+C]
=
F(b)-F(a)
\]

so the definite integral is unchanged.

## Core concept 5. Check basic antiderivatives by differentiation

If $n\ne-1$, the power is real-valued on the interval in question, and the power rule applies there, then

\[
\int x^n\,dx
=
\frac{x^{n+1}}{n+1}+C
\]

Differentiating the right-hand side gives

\[
\frac{d}{dx}
\left(\frac{x^{n+1}}{n+1}+C\right)
=
x^n
\]

which recovers the original integrand.

Increasing the exponent by one causes differentiation to bring down the factor $n+1$, so dividing by $n+1$ cancels it. In this lesson's polynomial calculations, $n$ is an integer at least $0$. When $n=-1$, the quantity $n+1$ is $0$, so this formula cannot be used; use the logarithmic antiderivative below instead.

The basic exponential and logarithmic antiderivatives are

\[
\int e^x\,dx=e^x+C
\]

\[
\int \frac1x\,dx
=
\log|x|+C,
\qquad x\ne0
\]

For $1/x$, use an interval that does not cross $0$. When $x>0$, we have $\log|x|=\log x$.

When $x<0$, $|x|=-x$, so $\log|x|=\log(-x)$. Differentiating with the chain rule gives $(1/(-x))(-1)=1/x$. The expression is therefore an antiderivative on both positive and negative intervals, but it is not a formula for calculating across a single integration interval containing $0$.

For the logarithmic antiderivative, the domain is split at 0 even though both curves use the same formula.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Separate negative and positive branches of log absolute x with zero excluded from the domain](../../figures/assets/M01/M01-09-log-branches.svg)
  <figcaption>Both branches of log|x| differentiate to 1/x. The function is undefined at 0, marked by the vertical dashed line, so this antiderivative formula cannot be used to calculate a definite integral crossing 0.</figcaption>
</figure>

## Core concept 6. Integrating a rate of change gives the net change

Suppose $Q$ is differentiable and $Q'$ satisfies the conditions for integrability. By the fundamental theorem,

\[
\int_a^b Q'(x)\,dx
=
Q(b)-Q(a)
\]

This is called the net change theorem.

Integrating velocity $v(t)=p'(t)$ over time gives the net change in position.

\[
\int_{t_0}^{t_1}v(t)\,dt
=
p(t_1)-p(t_0)
\]

Intervals of negative velocity contribute negatively to the position change. To obtain the total distance traveled, integrate $|v(t)|$ instead.

Net change in position and total distance differ when the motion reverses direction.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![A sign-changing velocity above a position curve that returns to its starting value](../../figures/assets/M01/M01-09-net-change.svg)
  <figcaption>Accumulating the illustrative velocity v(t)=t−1 from 0 to 2 makes the position first decrease and then return to its initial value. Signed accumulation is 0, but adding the magnitudes of travel over the negative and positive intervals gives total distance 1.</figcaption>
</figure>

## Core concept 7. Accumulating local path derivatives gives the endpoint output difference

Let $\alpha\in[0,1]$ be a scalar path parameter, and let $s(\alpha)$ be a model score. If $s$ satisfies the necessary conditions, then

\[
s(1)-s(0)
=
\int_0^1 s'(\alpha)\,d\alpha
\]

This equality states that accumulating local rates of change along one path gives the difference between its endpoint scores. Dividing this contribution among several input components requires specifying the path and decomposition rule as well. The equality on one path alone does not establish each component's causal effect or guarantee the same decomposition on another path.

Accumulation of the rate of change gives $s(1)-s(0)$, not $s(1)$ alone. Calculating the endpoint score itself also requires the starting score $s(0)$. Just as an antiderivative has an arbitrary constant of integration, rates of change alone cannot determine the score curve's overall height.

Different rate-of-change curves can produce the same endpoint difference. The next comparison uses illustrative functions to show why an equality of output differences does not determine the intermediate computation.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Different constant and linear score derivatives integrating to equal endpoint changes with different intermediate score curves](../../figures/assets/M01/M01-09-same-integral-paths.svg)
  <figcaption>Both rates, 2 and 4α, integrate to 2 over [0,1]. With the starting value set to 0, their score curves are 2α and 2α²: the endpoints agree, but the intermediate scores and local rates differ. This is not a measurement of an actual model's internal computation.</figcaption>
</figure>

## Core concept 8. Distinguish the theorem's two directions

Part 1 differentiates an accumulation function.

\[
\frac{d}{dx}
\int_a^x f(t)\,dt
=
f(x)
\]

Part 2 uses an antiderivative to calculate a definite integral.

\[
\int_a^b f(x)\,dx
=
F(b)-F(a),
\qquad F'=f
\]

The first expression gives a function of $x$, while the second gives a scalar for a fixed interval. Do not conflate the two calculations.

## Example 1. Differentiating an accumulation function

In

\[
A(x)=\int_1^x(t^2+2)\,dt
\]

the integrand $t^2+2$ is continuous. By Part 1,

\[
A'(x)=x^2+2
\]

Replace the integration variable $t$ with the upper-endpoint variable $x$.

## Example 2. A definite integral of a polynomial

Calculate

\[
\int_0^2(3x^2-2x+1)\,dx
\]

One antiderivative is

\[
F(x)=x^3-x^2+x
\]

Differentiating gives $F'(x)=3x^2-2x+1$, checking the result.

\[
\int_0^2(3x^2-2x+1)\,dx
=
[x^3-x^2+x]_0^2
\]

\[
=
(8-4+2)-0
=6
\]

The definite integral's area and the antiderivative's endpoint difference represent the same value on different graphs, as shown below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Area six under a quadratic integrand above an antiderivative whose endpoint values differ by six](../../figures/assets/M01/M01-09-area-endpoints.svg)
  <figcaption>The integral value 6 in the upper figure equals the height difference F(2)−F(0)=6 on the lower antiderivative graph. The calculation subtracts endpoint heights rather than finding another area under the lower curve.</figcaption>
</figure>

## Example 3. A definite integral of an exponential function

In

\[
\int_0^{\log2}e^x\,dx
\]

an antiderivative of $e^x$ is $e^x$ itself.

\[
\int_0^{\log2}e^x\,dx
=
[e^x]_0^{\log2}
\]

\[
=
e^{\log2}-e^0
=
2-1
=1
\]

Because the exponential function is its own antiderivative, the area under its curve is obtained as the difference between two heights.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Shaded area one under the exponential between zero and log two with endpoint heights one and two](../../figures/assets/M01/M01-09-exponential-area.svg)
  <figcaption>At inputs 0 and log 2, the antiderivative eˣ has heights 1 and 2, respectively. The area under the green curve is their difference, 1, and is distinct from the base length log 2.</figcaption>
</figure>

## Example 4. Calculating an endpoint difference from a rate of change

Suppose a score has path derivative

\[
s'(\alpha)=2\alpha+1
\]

Its change from $\alpha=0$ to $1$ is

\[
s(1)-s(0)
=
\int_0^1(2\alpha+1)\,d\alpha
\]

An antiderivative is $\alpha^2+\alpha$, so

\[
s(1)-s(0)
=
[\alpha^2+\alpha]_0^1
=2
\]

## Common misconceptions

### Misconception 1. A definite integral also needs the constant $C$

A definite integral subtracts antiderivative values at the endpoints, so the constant cancels. Use $+C$ only for an indefinite integral.

### Misconception 2. $\int_a^b f(x)\,dx=F(x)+C$

The left-hand side is a scalar for a fixed interval. The result is $F(b)-F(a)$.

### Misconception 3. There is only one antiderivative

Antiderivatives differ by constants. An indefinite integral represents this family as $F(x)+C$.

### Misconception 4. Part 1 differentiates the integration variable $t$

$t$ is a dummy variable inside the integral. The accumulation function's input is the upper endpoint $x$, and differentiation is with respect to $x$.

### Misconception 5. Equal integrals of rates of change imply equal internal mechanisms

The same endpoint output difference can arise from different rate-of-change curves and paths. Equality of output differences alone does not establish identical internal computations.

## Exercises

### 1. Reading Part 1 of the fundamental theorem

Given

\[
A(x)=\int_2^x(t^2+1)\,dt
\]

find $A'(x)$ and explain the roles of $t$ and $x$.

<details>
<summary>Show solution</summary>

By Part 1,

\[
A'(x)=x^2+1
\]

Here $t$ is a dummy variable used only inside the integral, while $x$ is both the upper endpoint of accumulation and the input to $A$.

</details>

### 2. Antiderivatives and the constant of integration

Find

\[
\int(4x^3-2x)\,dx
\]

and check it by differentiation.

<details>
<summary>Show solution</summary>

Find the power antiderivative term by term.

\[
\int(4x^3-2x)\,dx
=
x^4-x^2+C
\]

Differentiating the right-hand side gives

\[
4x^3-2x
\]

which checks the result.

</details>

### 3. Calculating a definite integral

Use Part 2 to calculate

\[
\int_1^3 2x\,dx
\]

<details>
<summary>Show solution</summary>

An antiderivative of $2x$ is $x^2$.

\[
\int_1^3 2x\,dx
=
[x^2]_1^3
=
9-1
=8
\]

</details>

### 4. Distinguishing definite and indefinite integrals

Explain what type of object each expression gives, and calculate it.

\[
\int x^2\,dx
\]

\[
\int_0^2x^2\,dx
\]

<details>
<summary>Show solution</summary>

The indefinite integral gives a family of antiderivatives.

\[
\int x^2\,dx
=
\frac{x^3}{3}+C
\]

The definite integral gives a scalar value.

\[
\int_0^2x^2\,dx
=
\left[\frac{x^3}{3}\right]_0^2
=
\frac83
\]

</details>

### 5. Calculating net change

For velocity

\[
v(t)=3t^2-1
\]

find the net change in position from $t=0$ to $t=2$.

<details>
<summary>Show solution</summary>

The net change in position is the definite integral of velocity.

\[
\int_0^2(3t^2-1)\,dt
=
[t^3-t]_0^2
\]

\[
=
8-2
=6
\]

This accumulation includes intervals of negative velocity with their signs.

</details>

### 6. The initial value of an accumulation function

Given

\[
A(x)=\int_3^x f(t)\,dt
\]

find $A(3)$ and $A'(x)$. Assume $f$ is continuous.

<details>
<summary>Show solution</summary>

The starting point and endpoint coincide, so

\[
A(3)=\int_3^3f(t)\,dt=0
\]

By Part 1,

\[
A'(x)=f(x)
\]

The accumulation function selects the antiderivative satisfying $A(3)=0$.

</details>

### 7. Assessing a path-integral claim

Two models have the same endpoint scores and the same $\int_0^1s'(\alpha)\,d\alpha$ along one input path. A researcher claims, “The models perform the same computations along the intermediate part of the path and use each input component in the same way.” Critique this conclusion.

<details>
<summary>Show solution</summary>

The fundamental theorem confirms that both integrals agree with the same endpoint score difference. However, different $s'(\alpha)$ curves can give the same integral value.

Claims about intermediate path computations and the use of individual input components require comparisons of intermediate rates of change, internal activations, and results of componentwise interventions. Accumulation along one scalar path does not guarantee identical internal mechanisms.

</details>

## Lesson summary

- The accumulation function $A(x)=\int_a^x f(t)\,dt$ of a continuous function $f$ satisfies $A'(x)=f(x)$.
- A function $F$ satisfying $F'=f$ is an antiderivative of $f$, and the indefinite integral is written $F+C$.
- Part 2 calculates a definite integral as $\int_a^b f(x)\,dx=F(b)-F(a)$.
- Integrating a rate of change over an interval gives the difference between its endpoint function values.
- Integrating a path derivative explains an output difference but guarantees neither a unique internal computation nor causal use of input components.

## Pass criteria

You have passed this lesson if you can answer these questions without consulting the material:

- Can you explain the intuition for why an accumulation function's derivative equals its integrand?
- Can you distinguish antiderivatives, indefinite integrals, and definite integrals?
- Can you determine when a constant of integration $C$ is needed?
- Can you use antiderivatives to calculate definite integrals of polynomials and exponential functions?
- Can you connect the integral of a rate of change to the total change between endpoints?

## Next lesson

- [M01-10. Multiple variables and partial derivatives](M01-10-multivariable-partial-derivatives.md)

## Author checklist

- [x] The learning objectives describe observable actions.
- [x] The two parts of the fundamental theorem and their conditions are distinguished.
- [x] Antiderivatives, indefinite integrals, and constants of integration are defined.
- [x] The definite-integral and net-change examples have been checked.
- [x] Every exercise has a solution.
- [x] Path accumulation is distinguished from claims about internal mechanisms.
- [x] The glossary and notation rules are followed.
- [x] Multivariable integration and measure theory are not required.
- [x] Internal links and mathematical delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
