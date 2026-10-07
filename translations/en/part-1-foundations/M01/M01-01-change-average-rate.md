---
id: "M01-01"
title: "Changes and average rates of change"
part: 1
stage: "M01"
status: "complete"
prerequisites:
  - "M00-02"
  - "M00-03"
  - "M00-04"
estimated_time: "85~105 minutes"
---

# M01-01. Changes and average rates of change

## Why this lesson matters

Differentiation measures how much an output changes when an input changes slightly. Its starting point is a finite change between two points. Before considering an instantaneous rate at one point, calculate how much loss decreases over 100 training steps or how much a logit changes when an input score changes by 0.2.

A change is the final value minus the initial value. An average rate of change divides the output change by the input change. Read the signs, units, and measurement interval together to interpret graph slopes and experimental results correctly.

## Learning objectives

After completing this lesson, you will be able to:

- Express changes between two values as $\Delta x$ and $\Delta y$.
- Formulate and calculate a function's average rate of change.
- Explain the sign and units of an average rate of change.
- Connect an average rate of change to a graph's secant slope.
- Distinguish an average over an interval from a rate near one point.

## Prerequisite check

- Prerequisite: [M00-02 Expressions, equalities, and equations](../M00/M00-02-expressions-equalities-equations.md)
- Prerequisite: [M00-03 Function inputs and outputs](../M00/M00-03-functions-input-output.md)
- Prerequisite: [M00-04 Coordinates and graphs](../M00/M00-04-coordinates-graphs.md)

Check that you can answer these questions.

1. For $f(x)=x^2$, can you calculate $f(1)$ and $f(3)$?
2. Can you write a point on a function's graph as $(x,f(x))$?
3. Can you distinguish horizontal and vertical changes between $(1,1)$ and $(3,9)$?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions and units |
|---|---|---|---|
| $\Delta$ | `delta` | A change between two values | Final value minus initial value |
| $\Delta x$ | `delta x` | Input change $x_2-x_1$ | The same units as $x$ |
| $\Delta y$ | `delta y` | Output change $y_2-y_1$ | The same units as $y$ |
| $\dfrac{\Delta y}{\Delta x}$ | `delta y over delta x` | Average rate of change | $\Delta x\ne0$ |
| Secant line | `secant line` | A line joining two distinct points on a graph | Requires two points |
| Slope | `slope` | Vertical change divided by horizontal change | Output units/input units |

## Core concept 1. A change is the final value minus the initial value

When an input changes from $x_1$ to $x_2$, define the input change as

\[
\Delta x=x_2-x_1
\]

The output of $y=f(x)$ changes from $f(x_1)$ to $f(x_2)$. The output change is

\[
\Delta y
=
f(x_2)-f(x_1)
\]

A change includes direction. For $x_1=2$ and $x_2=5$,

\[
\Delta x=5-2=3
\]

Reversing the order gives

\[
\Delta x=2-5=-3
\]

The same two values produce a change with the opposite sign when their initial and final roles are reversed.

### Distinguish a change from the final value

If $x$ changes from $4$ to $9$, its final value is $9$, but its change is

\[
\Delta x=9-4=5
\]

The change is the difference between two values, not the final value itself.

In the following figure, reversing the initial and final roles of the same two values reverses the arrow and the sign of the change. Also distinguish the value at the last vertical tick from the change written on the arrow.

<figure class="lesson-figure" markdown="1">

![Number lines show changes from two to five, five to two, and four to nine, separating signed change from endpoint value](../../figures/assets/M01/M01-01-directed-changes.svg)

<figcaption>Moving from 2 to 5 gives a change of +3; reversing the order gives −3. In a move from 4 to 9, the final value 9 differs from the change 5.</figcaption>
</figure>

## Core concept 2. An average rate of change is a ratio of changes

For $x_1\ne x_2$, the average rate of change of $f$ from $x_1$ to $x_2$ is

\[
\frac{\Delta y}{\Delta x}
=
\frac{f(x_2)-f(x_1)}{x_2-x_1}
\]

This expresses how much the output changed on average per unit change in input.

Comparing output changes alone ignores how much the input changed. Dividing by the input change expresses changes over intervals of different lengths on a per-input-unit basis. Here, “per unit” means that the total output change was divided by the input change. It does not mean that each unit within the interval produced the same actual change.

For example, suppose time $t$ changes from $2$ to $5$ seconds while position $s(t)$ changes from $10$ to $22$ meters. Then

\[
\Delta t=5-2=3\text{ seconds}
\]

\[
\Delta s=22-10=12\text{ meters}
\]

The average rate of change is

\[
\frac{\Delta s}{\Delta t}
=
\frac{12\text{ meters}}{3\text{ seconds}}
=
4\text{ meters/second}
\]

In this context, it is average velocity.

The following figure marks time and position changes separately over the same interval. Divide the units, meters and seconds, along with the values on the two arrows.

<figure class="lesson-figure" markdown="1">

![Time increases from two to five seconds while position changes from ten to twenty-two meters, giving twelve meters divided by three seconds](../../figures/assets/M01/M01-01-average-speed-units.svg)

<figcaption>Dividing the position change of 12 meters by the time change of 3 seconds gives an average velocity of 4 meters/second. The figure shows only the endpoints and does not specify positions at intermediate times.</figcaption>
</figure>

### A zero denominator is not allowed

If $x_1=x_2$, then

\[
\Delta x=0
\]

Because division by zero is undefined, this formula does not define an average rate when the two points coincide. Later lessons define a rate at one point using a limit in which two distinct points approach each other.

## Core concept 3. Signs indicate the direction of change

Suppose $x_2>x_1$, so $\Delta x>0$.

- If $\Delta y>0$, the average rate is positive. The output increased as the input increased.
- If $\Delta y<0$, the average rate is negative. The output decreased as the input increased.
- If $\Delta y=0$, the average rate is $0$. The endpoint outputs are equal.

An average rate of $0$ does not mean that the function was unchanged throughout the interval. It can rise and fall back to the same value at both endpoints.

For example, choosing $x=-1$ and $x=1$ for $f(x)=x^2$ gives

\[
f(-1)=f(1)=1
\]

so

\[
\frac{f(1)-f(-1)}{1-(-1)}
=
\frac{1-1}{2}
=0
\]

Yet $f(0)=0$ inside the interval differs from the endpoint value.

Reversing the initial and final points together changes the signs of both $\Delta x$ and $\Delta y$. Their ratio remains $(-\Delta y)/(-\Delta x)=\Delta y/\Delta x$, so the average rate between the same two points does not change. Do not interpret the sign of a change and the sign of an average rate in the same way.

Comparing the horizontal secant with the middle of the curve below shows why a zero average rate does not imply constancy within the interval.

<figure class="lesson-figure" markdown="1">

![The parabola x squared has equal values at minus one and one but a lower midpoint, while its horizontal secant has zero slope](../../figures/assets/M01/M01-01-zero-net-change.svg)

<figcaption>Both endpoints have height 1, so the secant slope is 0. Within the interval, the curve falls to height 0 and then rises again.</figcaption>
</figure>

## Core concept 4. An average rate of change has units

The units of

\[
\frac{\Delta y}{\Delta x}
\]

are

\[
\frac{\text{output units}}{\text{input units}}
\]

For training loss versus step, if the horizontal axis is step and the loss on the vertical axis is dimensionless, the average rate has units of “loss per step.” If input length is a token count and the output is execution time in seconds, the units are “seconds per token.”

Two studies reporting the same numerical slope cannot be compared as the same rate if their axis units differ.

## Core concept 5. On a graph, the average rate is a secant slope

A line joining two points on a function's graph,

\[
P=(x_1,f(x_1))
\]

\[
Q=(x_2,f(x_2))
\]

is called a secant line.

Its horizontal change is

\[
x_2-x_1
\]

and its vertical change is

\[
f(x_2)-f(x_1)
\]

Thus, its slope equals the function's average rate of change.

\[
\text{secant slope}
=
\frac{f(x_2)-f(x_1)}{x_2-x_1}
\]

A secant is a straight line joining the endpoints, whereas the function's graph between them may be curved. They meet at the two selected points but need not agree at every intermediate point. An average rate gives this secant's constant slope, not a constant rate of actual change inside the interval.

Narrowing the interval between the two points can bring the secant slope closer to the tangent slope at one point. Applying a limit to this process defines differentiation.

Follow the right triangle formed by horizontal change 2 and vertical change 8 in the following figure to read the secant slope 4. Also compare the secant and curve heights at $x=2$.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A secant through one comma one and three comma nine has run two and rise eight, and differs from x squared at input two](../../figures/assets/M01/M01-01-secant-triangle.svg)

<figcaption>The secant slope is 4: vertical change 8 divided by horizontal change 2. At x=2 between the endpoints, the secant has height 5 while the function value is 4, so the secant is not the function's actual graph.</figcaption>
</figure>

## Example 1. Average rate of a quadratic function

### Problem

Find the average rate of change of

\[
f(x)=x^2
\]

from $x=1$ to $x=3$.

### Solution

The input change is

\[
\Delta x=3-1=2
\]

The outputs are

\[
f(1)=1,\qquad f(3)=9
\]

so the output change is

\[
\Delta y=9-1=8
\]

The average rate is

\[
\frac{\Delta y}{\Delta x}
=
\frac82
=4
\]

### Meaning of the result

Over the interval in which $x$ changes from $1$ to $3$, $f(x)$ increases by an average of $4$ per input unit. This summarizes the whole interval; it is not the instantaneous rate at either $x=1$ or $x=3$.

## Example 2. Narrowing the interval

For $f(x)=x^2$, fix the starting point at $x_1=1$ and vary the endpoint.

| $x_2$ | $\Delta x=x_2-1$ | $\Delta y=x_2^2-1$ | Average rate of change |
|---:|---:|---:|---:|
| $3$ | $2$ | $8$ | $4$ |
| $2$ | $1$ | $3$ | $3$ |
| $1.5$ | $0.5$ | $1.25$ | $2.5$ |
| $1.1$ | $0.1$ | $0.21$ | $2.1$ |

As $x_2$ approaches $1$, the average rate approaches $2$. The next lesson expresses this approach using limit notation.

The table shows a trend, but a few rows do not prove a limit. For $f(x)=x^2$, simplifying the formula verifies the same result generally.

\[
\frac{x_2^2-1}{x_2-1}
=
\frac{(x_2-1)(x_2+1)}{x_2-1}
=
x_2+1
\]

Cancellation is valid for $x_2\ne1$, and as $x_2$ approaches $1$, $x_2+1$ approaches $2$.

The following figure plots the table's final input $x_2$ horizontally and the average rate vertically. The open point marks the zero denominator of the original fraction at $x_2=1$.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Average slopes for x squared from input one are two point one, two point five, three, and four at end inputs one point one, one point five, two, and three](../../figures/assets/M01/M01-01-shrinking-intervals.svg)

<figcaption>As the final input moves from 3 through 2, 1.5, and 1.1 toward the starting point 1, the secant slope changes from 4 through 3, 2.5, and 2.1. The open point (1, 2) marks the approached value, not an average rate calculated at x₂=1.</figcaption>
</figure>

## Example 3. Average change in a learning curve

Suppose a model's training loss is recorded as follows.

| Training step $t$ | Loss $L(t)$ |
|---:|---:|
| $100$ | $1.8$ |
| $300$ | $1.2$ |

The changes are

\[
\Delta t=300-100=200
\]

\[
\Delta L=1.2-1.8=-0.6
\]

The average rate is

\[
\frac{\Delta L}{\Delta t}
=
\frac{-0.6}{200}
=
-0.003
\]

Training loss decreased by an average of $0.003$ per step over this interval. Using only the endpoints does not establish that loss decreased by the same amount at each intermediate step.

The dotted line and gray path below join the same endpoints. The gray line illustrates possible intermediate changes and is not an actual measurement.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two loss observations at steps one hundred and three hundred share a secant and a different illustrative intermediate path, so the average does not determine each step](../../figures/assets/M01/M01-01-loss-endpoints.svg)

<figcaption>The observations are the two orange points. The purple secant summarizes −0.003 loss/step. A varying intermediate path such as the gray curve can have the same endpoints and average rate.</figcaption>
</figure>

## Example 4. Input perturbations and output changes

Simplify a model score to a scalar function $s(x)$. Changing input feature $x$ from $2.0$ to $2.2$ changes the score from $0.7$ to $0.82$.

\[
\Delta x=2.2-2.0=0.2
\]

\[
\Delta s=0.82-0.7=0.12
\]

The average rate is

\[
\frac{\Delta s}{\Delta x}
=
\frac{0.12}{0.2}
=0.6
\]

This measures average sensitivity between the two selected inputs. Whether another interval or a smaller perturbation yields the same value requires separate measurement.

## Common misconceptions

### Misconception 1. $\Delta x$ is the product of $x$ and $\Delta$

$\Delta x$ is one notation for the change in input $x$. In this lesson, $\Delta$ denotes the operation of subtracting the initial value from the final value.

### Misconception 2. A change is the positive difference between the larger and smaller values

A change subtracts the initial value from the final value. A decrease gives a negative change. Taking only its absolute value loses the direction of change.

### Misconception 3. An average rate is the mean of two function values

The average rate is

\[
\frac{f(x_2)-f(x_1)}{x_2-x_1}
\]

It differs from the arithmetic mean of the function values,

\[
\frac{f(x_1)+f(x_2)}2
\]

### Misconception 4. An average rate of $0$ means the function is constant throughout the interval

An average rate of $0$ means that the endpoint outputs are equal. Changes inside the interval require further checks.

### Misconception 5. An average rate over a short interval equals the instantaneous rate

A shorter interval can improve the approximation, but the two rates have different definitions. An instantaneous rate is defined by a limit as interval length approaches zero.

## Exercises

### 1. Calculate a change

$x$ changes from $7$ to $2$. Calculate $\Delta x$ and explain its sign.

<details>
<summary>Show solution</summary>

\[
\Delta x=2-7=-5
\]

The negative sign indicates that $x$ decreased: the final value is smaller than the initial value.

</details>

### 2. Calculate a function's output change

For

\[
f(x)=3x-1
\]

calculate $\Delta x$ and $\Delta y$ from $x=2$ to $x=5$.

<details>
<summary>Show solution</summary>

\[
\Delta x=5-2=3
\]

Because

\[
f(2)=5,\qquad f(5)=14
\]

we have

\[
\Delta y=14-5=9
\]

</details>

### 3. Calculate an average rate

Find the average rate for the function and interval in Exercise 2.

<details>
<summary>Show solution</summary>

\[
\frac{\Delta y}{\Delta x}
=
\frac93
=3
\]

$f(x)=3x-1$ is a straight line whose output changes by $3$ per input unit, so any two points give an average rate of $3$.

</details>

### 4. Interpret a negative average rate

For

\[
g(t)=10-2t
\]

calculate and interpret the average rate from $t=1$ to $t=4$.

<details>
<summary>Show solution</summary>

Because

\[
g(1)=8,\qquad g(4)=2
\]

we have

\[
\Delta g=2-8=-6
\]

and

\[
\Delta t=4-1=3
\]

The average rate is

\[
\frac{-6}{3}=-2
\]

Over this interval, $g(t)$ decreases by an average of $2$ per unit increase in $t$.

</details>

### 5. Interpret units

Let input $n$ be a token count and output $T(n)$ be execution time in seconds. At $n=100$, $T=0.4$; at $n=300$, $T=1.0$. Find the average rate and its units.

<details>
<summary>Show solution</summary>

\[
\Delta n=300-100=200\text{ token}
\]

\[
\Delta T=1.0-0.4=0.6\text{ seconds}
\]

so

\[
\frac{\Delta T}{\Delta n}
=
\frac{0.6}{200}
=0.003\text{ seconds/token}
\]

Within the measured interval, execution time increases by an average of $0.003$ seconds per additional token.

</details>

### 6. Interpret an average rate of $0$

Find the average rate of

\[
h(x)=(x-2)^2
\]

from $x=1$ to $x=3$, and determine whether the function is constant throughout the interval.

<details>
<summary>Show solution</summary>

Because

\[
h(1)=1,\qquad h(3)=1
\]

we have

\[
\frac{h(3)-h(1)}{3-1}
=
\frac{1-1}{2}
=0
\]

But

\[
h(2)=0
\]

so the function changes inside the interval. An average rate of $0$ means only that the endpoint outputs are equal.

</details>

### 7. Evaluate a claim

At training steps $100$ and $200$, loss is $1.0$ and $0.8$, respectively. A researcher says, “Loss decreased by $0.002$ at every step in this interval.” Calculate the average rate and evaluate the claim.

<details>
<summary>Show solution</summary>

\[
\frac{0.8-1.0}{200-100}
=
\frac{-0.2}{100}
=-0.002
\]

This is the average rate over the whole interval. Two endpoints do not establish that every step's change was $-0.002$. Intermediate loss records are needed to check whether the per-step change was constant.

</details>

## Lesson summary

- A change is the final value minus the initial value; its sign depends on direction.
- An average rate is $\Delta y/\Delta x$, requiring $\Delta x\ne0$.
- Its units are output units divided by input units.
- On a function's graph, the average rate is the slope of the secant joining two points.
- An interval average does not determine an instantaneous rate or the detailed changes within the interval.

## Pass criteria

You pass if you can answer these questions without consulting the material.

- Can you express $\Delta x$ and $\Delta y$ using initial and final values?
- Can you calculate a function's average rate of change?
- Can you explain the sign and units of a rate?
- Can you connect an average rate to a secant slope?
- Can you give one conclusion that cannot be drawn from an interval average?

## Next lesson

The next lesson is [M01-02 Intuition for limits](M01-02-limits-intuition.md). You will read how function values and average rates approach a value as the distance between two distinct points decreases.

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] The $\Delta$ symbol and subtraction order are defined.
- [x] The denominator condition and units of an average rate are stated.
- [x] Numerical examples and table values have been checked.
- [x] Every exercise has a solution.
- [x] Claims about interval averages and instantaneous rates are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
