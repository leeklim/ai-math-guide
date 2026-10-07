---
id: "M01-02"
title: "Intuition for limits"
part: 1
stage: "M01"
status: "complete"
prerequisites:
  - "M00-03"
  - "M00-04"
  - "M01-01"
estimated_time: "90~110 minutes"
---

# M01-02. Intuition for limits

## Why this lesson matters

Calculating an instantaneous rate requires narrowing the gap between two points. Making input change $\Delta x$ smaller changes both the numerator and denominator of the average rate. Directly substituting $\Delta x=0$ would divide by zero, so consider which value the ratios approach while the gap remains nonzero.

A limit describes the value approached by a function's output as its input approaches a specified value. A limit can exist even if the function is undefined at that point or has a different value there. This distinction matters when reading definitions of derivatives, numerical approximations, and local changes in neural networks.

## Learning objectives

After completing this lesson, you will be able to:

- Explain $\lim_{x\to a}f(x)=L$ in an English sentence.
- Distinguish the function value $f(a)$ from the limit as $x\to a$.
- Estimate and calculate limits from tables and simple expressions.
- Compare left-hand and right-hand limits to determine whether a two-sided limit exists.
- Explain the introductory relationships between limits, continuity, and differentiation.

## Prerequisite check

- Prerequisite: [M00-03 Function inputs and outputs](../M00/M00-03-functions-input-output.md)
- Prerequisite: [M00-04 Coordinates and graphs](../M00/M00-04-coordinates-graphs.md)
- Prerequisite: [M01-01 Changes and average rates of change](M01-01-change-average-rate.md)

Check that you can calculate the following expression.

\[
\frac{x^2-1}{x-1}
\]

For $x\ne1$, factor the numerator.

\[
\frac{(x-1)(x+1)}{x-1}=x+1
\]

The original denominator is zero at $x=1$, so the expression is undefined there. The limit considers nearby values excluding $x=1$.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Cautions |
|---|---|---|---|
| $x\to a$ | `x approaches a` | $x$ approaches $a$ through values different from $a$ | Does not mean $x=a$ |
| $\lim_{x\to a}f(x)$ | `the limit of f of x as x approaches a` | The value approached by $f(x)$ as $x$ approaches $a$ | May not exist |
| $L$ | `L` | The limit value | Here, a finite real value |
| $x\to a^-$ | `x approaches a from the left` | Approach through values smaller than $a$ | Left-hand limit |
| $x\to a^+$ | `x approaches a from the right` | Approach through values larger than $a$ | Right-hand limit |
| Continuous | `continuous` | The limit equals the function value | The function must be defined at $a$ |

## Core concept 1. A limit describes approach

\[
\lim_{x\to a}f(x)=L
\]

means “as $x$ approaches $a$, $f(x)$ approaches $L$.”

$x$ need not equal $a$. In considering a limit, use other values near $a$. Approach through values smaller and larger than $a$ and check whether the outputs approach one value.

“Approaches” means that for a chosen output-error tolerance, restricting the input sufficiently close to $a$ places the output within that tolerance of $L$ for every admissible input in the restricted range. Requiring a smaller output error must allow a corresponding tighter input range. Exclude the single point $x=a$ in this process. A function value coming close to $L$ once does not determine a limit.

For example, for

\[
f(x)=2x+1
\]

as $x$ approaches $3$, $f(x)$ approaches $7$.

\[
\lim_{x\to3}(2x+1)=7
\]

Directly substituting $x=3$ gives the same value for this function. Not every limit can be calculated by substitution alone.

The following figure shows how restricting inputs around 3 also restricts outputs around 7. Read the blue input range together with the green output range.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A blue input window around three maps through two x plus one into a green output window around seven](../../figures/assets/M01/M01-02-approach-window.svg)

<figcaption>Inputs between 2.75 and 3.25 give outputs between 6.5 and 7.5. A limit considers the outputs of nearby inputs excluding the central point, rather than the value at that point alone.</figcaption>
</figure>

## Core concept 2. A function value and a limit answer different questions

Consider

\[
f(x)=\frac{x^2-1}{x-1},
\qquad x\ne1
\]

For $x\ne1$, this simplifies to

\[
f(x)=x+1
\]

As $x$ approaches $1$, $x+1$ approaches $2$.

\[
\lim_{x\to1}\frac{x^2-1}{x-1}=2
\]

Yet substituting $x=1$ into the original expression gives a zero denominator, so $f(1)$ is undefined.

\[
f(1)\text{ is undefined},
\qquad
\lim_{x\to1}f(x)=2
\]

Both statements hold. A limit asks about behavior near the point rather than the value at the point.

The simplified expression $x+1$ can be evaluated at $x=1$, but this does not newly define $f(1)$ for the original fraction. It is usable in calculating the limit because the two expressions agree at nearby inputs excluding $x=1$. If nearby values agree, the limits approaching that point agree even when the values at the point differ.

### Changing a point's value can leave its limit unchanged

Define $g$ as

\[
g(x)=
\begin{cases}
\dfrac{x^2-1}{x-1}, & x\ne1,\\
7, & x=1
\end{cases}
\]

Then

\[
g(1)=7
\]

but near $x=1$, its values match the previous function, so

\[
\lim_{x\to1}g(x)=2
\]

Changing the function value at one point does not change the limit approaching that point.

In the following figure, the open point marks the height approached by nearby values; the orange point marks the separately defined function value.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The line x plus one approaches an open point at one comma two while a separate filled point defines g of one as seven](../../figures/assets/M01/M01-02-hole-and-value.svg)

<figcaption>Following the line from either side approaches height 2. Adding the orange point g(1)=7 leaves the values near x=1 and the limit 2 unchanged.</figcaption>
</figure>

## Core concept 3. Inspect the trends on both sides in a table

Evaluate

\[
f(x)=\frac{x^2-1}{x-1},
\qquad x\ne1
\]

near $1$.

| $x$ | $f(x)$ |
|---:|---:|
| $0.9$ | $1.9$ |
| $0.99$ | $1.99$ |
| $0.999$ | $1.999$ |
| $1.001$ | $2.001$ |
| $1.01$ | $2.01$ |
| $1.1$ | $2.1$ |

As $x$ approaches $1$ from either side, $f(x)$ approaches $2$.

A table helps estimate a limit, but finitely many rows cannot check every nearby value. In this example, simplifying the expression to $x+1$ verifies the limit.

## Core concept 4. The left-hand and right-hand limits must agree

The left-hand limit approaches from the left and is written

\[
\lim_{x\to a^-}f(x)
\]

The right-hand limit approaches from the right and is written

\[
\lim_{x\to a^+}f(x)
\]

For the two-sided limit

\[
\lim_{x\to a}f(x)
\]

to exist, both one-sided limits must exist and agree.

If

\[
\lim_{x\to a^-}f(x)
=
\lim_{x\to a^+}f(x)
=L
\]

then

\[
\lim_{x\to a}f(x)=L
\]

A two-sided limit does not restrict approach to one direction. If nearby inputs from the left approach one output value while those from the right approach another, there is no single common value approached by all nearby inputs. Check not only whether each one-sided limit exists, but also whether the values agree.

### An example with different one-sided limits

Let

\[
s(x)=
\begin{cases}
0, & x<0,\\
1, & x\ge0
\end{cases}
\]

Approaching from below $0$ gives function value $0$, so

\[
\lim_{x\to0^-}s(x)=0
\]

Approaching from above $0$ gives function value $1$, so

\[
\lim_{x\to0^+}s(x)=1
\]

The two values differ, so

\[
\lim_{x\to0}s(x)
\]

does not exist.

The defined value $s(0)=1$ does not change whether the two-sided limit exists.

The horizontal lines on the left and right below have different heights. Defining the value at one point does not remove this difference.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A step function approaches zero from the left and one from the right with a filled value one at input zero](../../figures/assets/M01/M01-02-one-sided-jump.svg)

<figcaption>The left-hand limit is 0 and the right-hand limit is 1, so no common value is approached from both directions. The orange point marks s(0)=1.</figcaption>
</figure>

## Core concept 5. Continuity connects limits to function values

A function $f$ is continuous at $a$ when three conditions hold.

1. $f(a)$ is defined.
2. $\lim_{x\to a}f(x)$ exists.
3. $\lim_{x\to a}f(x)=f(a)$.

The polynomial $f(x)=x^2+1$ is continuous at every real input. Its limit can therefore be calculated by substitution.

\[
\lim_{x\to a}(x^2+1)=a^2+1
\]

The earlier expression

\[
\frac{x^2-1}{x-1}
\]

is undefined at $x=1$ and therefore is not continuous there. Defining its value to be the limit $2$ fills the hole and makes the extended function continuous.

The following figure adds a function value at the height of the limit to the earlier open point.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Filling the missing point at one comma two makes the extended x plus one function continuous at input one](../../figures/assets/M01/M01-02-continuity-repair.svg)

<figcaption>The newly defined f(1)=2 equals the limit 2 of nearby values. All three conditions hold: the function value exists, the limit exists, and the two agree.</figcaption>
</figure>

## Core concept 6. Unbounded growth

For

\[
f(x)=\frac1{x^2}
\]

as $x$ approaches $0$, $x^2$ approaches $0$ while remaining positive. Its reciprocal grows without bound. Write

\[
\lim_{x\to0}\frac1{x^2}=+\infty
\]

$+\infty$ is not a real number. This notation indicates that the function values can exceed any arbitrarily large positive number. Read it as “the function values grow without bound in the positive direction,” rather than “the limit is the real number $+\infty$.”

For a chosen large threshold, every nonzero input sufficiently close to $0$ must have a function value above it. Increasing the threshold must still allow a tighter input range satisfying this condition. Obtaining large values at some inputs alone does not establish this limit.

The clipping at the top of the following plot is not an upper bound on the function. Approaching closer to 0 yields values beyond the plotted range.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The reciprocal of x squared rises beyond the plotting window from both sides as nonzero input approaches zero](../../figures/assets/M01/M01-02-unbounded-square.svg)

<figcaption>1/x² grows while remaining positive on both sides. No function value is plotted at input 0, and the graph continues upward beyond the figure.</figcaption>
</figure>

For

\[
\frac1x
\]

the values approach $+\infty$ as $x\to0^+$ and $-\infty$ as $x\to0^-$. The different behavior on the two sides means there is no single two-sided real limit.

The following figure shows the sign difference between the left and right sides of the reciprocal without squaring.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The reciprocal of x falls without bound on the left of zero and rises without bound on the right](../../figures/assets/M01/M01-02-unbounded-reciprocal.svg)

<figcaption>1/x is unbounded in the negative direction to the left of 0 and in the positive direction to the right. It does not have the same two-sided behavior as 1/x².</figcaption>
</figure>

## Core concept 7. Make the interval of an average rate approach zero

Starting at $x=a$ and changing the input by $h$ gives endpoint $a+h$.

\[
\Delta x=h
\]

\[
\Delta y=f(a+h)-f(a)
\]

The average rate is

\[
\frac{f(a+h)-f(a)}{h}
\]

At $h=0$, the denominator is zero, so it cannot be evaluated. Instead, consider the limit as $h$ approaches zero while remaining nonzero.

Keep the starting point $a$ fixed and vary only the gap $h$. Each $h\ne0$ gives one average rate, so the average rate itself can be viewed as a function of $h$. For $h>0$, the endpoint is to the right of $a$; for $h<0$, it is to the left. Check whether both directions approach the same value.

\[
\lim_{h\to0}
\frac{f(a+h)-f(a)}{h}
\]

If this limit exists as a finite real number, it defines an instantaneous rate at $a$. The next lesson expresses this value using derivative notation.

The following figure plots the average rate of x² at the fixed base input 1 as a function of h. Check whether the ratios from the left and right approach the same height.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![For x squared at base input one the difference quotient two plus h approaches two from both sides with an open point at h zero](../../figures/assets/M01/M01-02-difference-quotient.svg)

<figcaption>Whether h is negative or positive, the average rate 2+h approaches 2 as h approaches 0. The open point marks that the original difference quotient cannot be evaluated at h=0.</figcaption>
</figure>

## Example 1. Simplify an expression to find its limit

### Problem

Find

\[
\lim_{x\to2}
\frac{x^2-4}{x-2}
\]

### Solution

Direct substitution of $x=2$ gives $0/0$. At nearby inputs with $x\ne2$, factor the numerator.

\[
x^2-4=(x-2)(x+2)
\]

Thus,

\[
\frac{x^2-4}{x-2}
=
x+2,
\qquad x\ne2
\]

As $x$ approaches $2$, $x+2$ approaches $4$.

\[
\lim_{x\to2}
\frac{x^2-4}{x-2}
=4
\]

## Example 2. Compare a function value with a limit

Let

\[
g(x)=
\begin{cases}
x+2, & x\ne2,\\
100, & x=2
\end{cases}
\]

Then

\[
g(2)=100
\]

Near $x=2$, however, $g(x)=x+2$, so

\[
\lim_{x\to2}g(x)=4
\]

The function value differs from the limit, so $g$ is not continuous at $x=2$.

## Example 3. ReLU's limit and corner

The rectified linear unit, ReLU, is

\[
\operatorname{ReLU}(x)
=
\max(0,x)
\]

For $x<0$, its value is $0$, so

\[
\lim_{x\to0^-}\operatorname{ReLU}(x)=0
\]

For $x>0$, its value is $x$, so

\[
\lim_{x\to0^+}\operatorname{ReLU}(x)=0
\]

The one-sided limits agree, and $\operatorname{ReLU}(0)=0$, so ReLU is continuous at $0$.

Its graph has a corner at $0$. Continuity alone does not guarantee differentiability. The next lesson compares left-hand and right-hand rates.

## Example 4. Local stability of model outputs

Let $s(x)$ be a model score for scalar input $x$. If

\[
\lim_{x\to a}s(x)=s(a)
\]

then $s$ is continuous at $a$. Choosing inputs close to $a$ can make outputs close to $s(a)$.

This is a mathematical property of small changes near $a$. Evaluating an actual stability criterion requires numerical input-distance and output-error tolerances. Continuity at one point does not guarantee stability under large perturbations, in other data regions, or adversarial robustness.

## Common misconceptions

### Misconception 1. $x\to a$ means $x=a$

$x\to a$ describes $x$ approaching $a$ through nearby values. A limit can exist separately from the function value at $x=a$.

### Misconception 2. A limit is the result of substituting $a$ into the function

For a continuous function, substitution can calculate a limit. If the function is undefined at that point or its value differs from the nearby trend, the limit and function value differ.

### Misconception 3. A few converging table values prove a limit

A table is a tool for estimating a trend. Properties of the expression or a rigorous definition are needed to establish the behavior of nearby values not selected for the table.

### Misconception 4. One existing one-sided limit is enough for a two-sided limit

A two-sided limit requires both one-sided limits, and their values must agree.

### Misconception 5. Continuity implies differentiability

Continuity prevents a break in function values. A function such as ReLU can be continuous but not differentiable at a corner.

## Exercises

### 1. Read limit notation

Explain

\[
\lim_{x\to3}f(x)=5
\]

in an English sentence, and determine whether this formula alone implies $f(3)=5$.

<details>
<summary>Show solution</summary>

Read it as “as $x$ approaches $3$, $f(x)$ approaches $5$.”

The formula alone does not imply $f(3)=5$. The value $f(3)$ may be undefined or defined differently. Adding the condition that $f$ is continuous at $3$ gives $f(3)=5$.

</details>

### 2. Calculate a limit by substitution

Find

\[
\lim_{x\to2}(3x^2-x+1)
\]

<details>
<summary>Show solution</summary>

A polynomial is continuous at every real input, so substitute $x=2$.

\[
3\cdot2^2-2+1
=
12-2+1
=11
\]

The limit is $11$.

</details>

### 3. Calculate a limit using factorization

Find

\[
\lim_{x\to3}
\frac{x^2-9}{x-3}
\]

<details>
<summary>Show solution</summary>

Direct substitution of $x=3$ gives $0/0$. Factor the numerator.

\[
x^2-9=(x-3)(x+3)
\]

At nearby inputs with $x\ne3$,

\[
\frac{x^2-9}{x-3}=x+3
\]

Therefore,

\[
\lim_{x\to3}
\frac{x^2-9}{x-3}
=6
\]

</details>

### 4. Compare a function value with a limit

For

\[
h(x)=
\begin{cases}
2x, & x\ne1,\\
-4, & x=1
\end{cases}
\]

find $h(1)$ and $\lim_{x\to1}h(x)$ separately, and determine whether the function is continuous at $x=1$.

<details>
<summary>Show solution</summary>

The definition gives

\[
h(1)=-4
\]

Near $x=1$, $h(x)=2x$, so

\[
\lim_{x\to1}h(x)=2
\]

The limit differs from the function value, so $h$ is not continuous at $x=1$.

</details>

### 5. Find one-sided limits

For

\[
q(x)=
\begin{cases}
-1, & x<2,\\
3, & x\ge2
\end{cases}
\]

find the left-hand, right-hand, and two-sided limits at $x=2$.

<details>
<summary>Show solution</summary>

Below $2$, the function value is $-1$, so

\[
\lim_{x\to2^-}q(x)=-1
\]

Above $2$, the function value is $3$, so

\[
\lim_{x\to2^+}q(x)=3
\]

The one-sided limits differ, so

\[
\lim_{x\to2}q(x)
\]

does not exist.

</details>

### 6. Prepare the expression for a derivative at a point

For

\[
f(x)=x^2
\]

and $a=2$, simplify

\[
\frac{f(a+h)-f(a)}h
\]

for $h\ne0$. Also find the value approached as $h\to0$.

<details>
<summary>Show solution</summary>

\[
\frac{f(2+h)-f(2)}h
=
\frac{(2+h)^2-4}{h}
\]

\[
=
\frac{4+4h+h^2-4}{h}
\]

\[
=
\frac{h(4+h)}h
=
4+h,
\qquad h\ne0
\]

As $h$ approaches $0$, $4+h$ approaches $4$.

\[
\lim_{h\to0}
\frac{f(2+h)-f(2)}h
=4
\]

</details>

### 7. Evaluate a model-stability claim

A model score $s(x)$ has been shown to be continuous at input $a$. A researcher concludes, “This model is robust at every input against perturbations of every size.” Critique the scope of the conclusion.

<details>
<summary>Show solution</summary>

Continuity at $a$ is a local property: sufficiently small input changes near $a$ can make output changes small.

It does not guarantee robustness at other inputs, against large perturbations, or under unspecified distance measures. A global robustness claim requires an input region, perturbation size, distance measure, and allowed output error, followed by evaluation over the entire specified range.

</details>

## Lesson summary

- $\lim_{x\to a}f(x)=L$ means that $f(x)$ approaches $L$ as $x$ approaches $a$.
- A limit can exist even if $f(a)$ is undefined or differs from the limit.
- A two-sided limit requires the left-hand and right-hand limits to agree.
- Continuity at $a$ requires the limit to exist and equal $f(a)$.
- An instantaneous rate is defined by the limit of average rates as the input gap approaches zero.

## Pass criteria

You pass if you can answer these questions without consulting the material.

- Can you distinguish $x\to a$ from $x=a$?
- Can you explain an example in which a function value differs from its limit?
- Can you use one-sided limits to determine whether a two-sided limit exists?
- Can you state the three conditions for continuity at a point?
- Can you explain how the limit of average rates leads to an instantaneous rate?

## Next lesson

The next lesson is [M01-03 Differentiation and instantaneous rates of change](M01-03-derivative-instantaneous-rate.md). You will express limits of average rates using $f'(x)$ and $\frac{df}{dx}$ and calculate derivatives of simple functions.

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Limit notation and approach directions are defined.
- [x] Function values, limits, and continuity are distinguished.
- [x] One-sided limit examples have been checked.
- [x] Every exercise has a solution.
- [x] The scope of continuity and robustness claims is limited.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
