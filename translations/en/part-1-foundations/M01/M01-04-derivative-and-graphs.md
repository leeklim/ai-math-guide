---
id: "M01-04"
title: "Derivatives and graphs"
part: 1
stage: "M01"
status: "complete"
prerequisites:
  - "M00-04"
  - "M01-03"
estimated_time: "90~110 minutes"
---

# M01-04. Derivatives and graphs

## Why this lesson matters

Knowing the derivative at one point tells you in which direction and how quickly a function changes there. Collecting these values across the input domain helps identify intervals where the function increases or decreases and points where its direction changes.

The derivative function assigns the derivative value $f'(x)$ to each input $x$. Reading the original function's graph, which shows its height, alongside the derivative graph lets you distinguish the direction in which a loss decreases from the intervals in which an activation function responds to input changes.

## Learning objectives

After this lesson, you will be able to:

- Distinguish a derivative value at one point from the derivative function.
- Use the sign of the derivative to identify intervals of increase and decrease.
- Distinguish critical points from stationary points and identify candidates for extrema.
- Use changes in the derivative's sign to identify local maxima and minima.
- Relate a function graph to its derivative graph.

## Prerequisite check

- Prerequisite lesson: [M00-04. Coordinates and graphs](../M00/M00-04-coordinates-graphs.md)
- Prerequisite lesson: [M01-03. Differentiation and instantaneous rates of change](M01-03-derivative-instantaneous-rate.md)
- Check question: Can you explain what $f'(a)>0$, $f'(a)<0$, and $f'(a)=0$ mean for the tangent slope?

Review M01-03 first if the relationship between tangent slope and the derivative at a point is unclear.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Scope and conditions |
|---|---|---|---|
| $f'$ | `f prime` | The derivative function assigning the derivative value $f'(x)$ to each $x$ | Defined at inputs where the function is differentiable |
| Increasing | `increasing` | Function values become larger as the input increases | State the interval |
| Decreasing | `decreasing` | Function values become smaller as the input increases | State the interval |
| Critical point | `critical point` | A point $c$ in the domain where $f'(c)=0$ or $f'(c)$ does not exist | A candidate for an extremum, not a guarantee of one |
| Stationary point | `stationary point` | A point $c$ where $f'(c)=0$ | One type of critical point |
| Local maximum | `local maximum` | The largest function value in a neighborhood of a point | Requires a surrounding interval for comparison |
| Local minimum | `local minimum` | The smallest function value in a neighborhood of a point | Requires a surrounding interval for comparison |

## Core concept 1. The derivative is itself a function

The derivative $f'(a)$ at one point $a$ is a scalar value. Calculating the derivative as the input $x$ varies gives a new function:

\[
x\longmapsto f'(x)
\]

This is called the derivative function.

For $f(x)=x^2$,

\[
f'(x)=2x
\]

For example,

\[
f'(-2)=-4,
\qquad
f'(0)=0,
\qquad
f'(3)=6
\]

The vertical coordinate on the derivative graph is not the height of the original function. It is the tangent slope of that function at the same $x$.

Following a vertical dashed line at the same input across the two graphs below separates the function height from the derivative value.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Aligned graphs of x squared and its derivative two x show the original heights and slopes at the same input coordinates](../../figures/assets/M01/M01-04-function-and-slopes.svg)

<figcaption>The height on the upper graph is the function value; the height on the lower graph is the tangent slope of the upper curve. At x=−2, 0, and 3, the slopes are −4, 0, and 6, respectively.</figcaption>
</figure>

## Core concept 2. The derivative's sign indicates the direction of change

A function is increasing on an interval if comparing any two inputs $x_1<x_2$ in that interval gives $f(x_1)<f(x_2)$. It is decreasing if the same input order gives $f(x_1)>f(x_2)$. Distinguish reading a slope at one point from comparing two inputs across an interval.

If $f'(x)>0$ on an interval, the tangent slope is positive. The function values change in the increasing direction as the input increases. If this condition holds throughout the interval, the function is increasing there.

If $f'(x)<0$ on an interval, the function is decreasing. If $f'(x)=0$, the tangent at that point is horizontal.

| Derivative value | Tangent direction | Local behavior of the function |
|---:|---|---|
| $f'(x)>0$ | Slopes upward to the right | Increasing direction |
| $f'(x)<0$ | Slopes downward to the right | Decreasing direction |
| $f'(x)=0$ | Horizontal | This point alone does not determine increase or decrease |

The sign at one point indicates the direction near that point. To claim increase or decrease throughout an interval, check the derivative's sign within the interval.

If $f'(a)>0$, the difference quotient $[f(a+h)-f(a)]/h$ is also positive for sufficiently small $h\ne0$. When $h>0$, the output change is positive; when $h<0$, the output change is negative. Thus, values slightly to the right of the reference point are larger than $f(a)$, and values slightly to its left are smaller. This compares the reference point with nearby values. To claim increase between any two other points in a surrounding interval, their slopes must also be checked.

## Core concept 3. Critical points are candidates for extrema

A local maximum occurs when $f(c)$ is largest compared with function values in a sufficiently small surrounding interval. A local minimum occurs when $f(c)$ is smallest in the same comparison. The comparison concerns values near $c$; the value need not be largest or smallest over the entire domain.

A point $c$ in the domain is a critical point if

\[
f'(c)=0
\]

or if $f'(c)$ does not exist. A critical point $c$ with $f'(c)=0$ is a stationary point.

If a function is differentiable at an interior point $c$ of its domain and has a local maximum or minimum there, then $f'(c)=0$. At a corner, an extremum may occur where the derivative does not exist. Both cases therefore need to be investigated as candidates for extrema.

At a local maximum, $f(c+h)-f(c)\le0$ for small $h$. Dividing by positive $h$ gives a right-hand rate of change at most $0$; dividing by negative $h$ gives a left-hand rate of change at least $0$. Differentiability requires the two limits to equal the same finite value, which must therefore be $0$. At a local minimum, the inequality directions reverse, giving the same conclusion. This reasoning assumes an interior point that can be approached from both sides.

Being a critical point does not guarantee an extremum. For $f(x)=x^3$, we have $f'(0)=0$, but the function continues to increase on both sides of $x=0$.

The origin in the next figure is a stationary point: the tangent is horizontal, but the curve continues in the increasing direction.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The cubic x cubed passes through a horizontal tangent at zero while continuing to increase on both sides](../../figures/assets/M01/M01-04-stationary-cubic.svg)

<figcaption>The derivative at the origin is 0, but values on the left are below 0 and values on the right are above 0. The origin is therefore neither a local maximum nor a local minimum.</figcaption>
</figure>

## Core concept 4. Changes in derivative sign identify local extrema

Suppose a function is continuous at a critical point $c$ and differentiable on small intervals on both sides, excluding $c$ itself. Compare the derivative signs maintained on these intervals.

- If the sign changes from $+$ to $-$, the function increases and then decreases, so $f(c)$ is a local maximum.
- If the sign changes from $-$ to $+$, the function decreases and then increases, so $f(c)$ is a local minimum.
- If the derivative is positive on both sides or negative on both sides, the function passes through $c$ in the same direction, so there is no extremum.

This is the first derivative test. If the function is discontinuous at $c$, a sign change alone cannot determine whether $f(c)$ is larger or smaller than nearby values. Check continuity separately.

The sign change can be tested even when $f'(c)$ does not exist. For $f(x)=|x|$, the slope is $-1$ when $x<0$ and $1$ when $x>0$. The derivative does not exist at $0$, but its sign changes from $-$ to $+$, so $f(0)=0$ is a local minimum.

## Core concept 5. Read height and slope separately

$f(x)>0$ means that the function graph is above the $x$-axis. $f'(x)>0$ means that the graph is changing in the increasing direction. These statements provide different information.

For example, with $f(x)=x^2$ at $x=-1$,

\[
f(-1)=1>0
\]

but

\[
f'(-1)=-2<0
\]

The graph can be above the $x$-axis while decreasing.

Conversely, when the function value is negative and the derivative is positive, the graph increases below the $x$-axis. Do not apply the same sign interpretation to a function value and its rate of change.

In the next figure, read the orange point's height separately from the direction of the purple tangent through it.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![At input minus one the parabola has positive height one while its tangent slopes downward with derivative minus two](../../figures/assets/M01/M01-04-height-versus-slope.svg)

<figcaption>At x=−1, the function value 1 indicates a position above the x-axis. The tangent slope −2 indicates the local decreasing direction as the input increases.</figcaption>
</figure>

## Core concept 6. Estimate a derivative graph from the function graph

Read the original graph from left to right and estimate its tangent slopes.

1. On increasing intervals, the derivative graph lies above the $x$-axis.
2. On decreasing intervals, the derivative graph lies below the $x$-axis.
3. At a horizontal tangent, the derivative graph meets the $x$-axis.
4. At a corner, the derivative graph may have a break or an undefined value.

A large absolute derivative value $|f'(x)|$ means that the original graph's tangent is steep. When $f'(x)$ is close to $0$, the tangent is shallow. Changing the graph's scale also changes its apparent steepness, so check the numerical values and axis units together.

## Core concept 7. Use a loss derivative to choose a direction of movement

Consider a loss $\mathcal L(\theta)$ for a scalar parameter $\theta$.

- If $\mathcal L'(\theta)>0$, the loss increases in the direction of increasing $\theta$. Within a small range, decreasing $\theta$ is a candidate direction for lowering the loss.
- If $\mathcal L'(\theta)<0$, the loss decreases in the direction of increasing $\theta$. Within a small range, increasing $\theta$ is a candidate direction.

Combining these cases gives the single-variable form of gradient descent:

\[
\theta_{\mathrm{new}}
=
\theta-\eta\mathcal L'(\theta),
\qquad \eta>0
\]

Here $\eta$ is the learning rate. The update moves opposite to the derivative's sign. A large learning rate can move beyond the range described by the local change information, so a single update does not guarantee a reduction in loss.

The parameter change in the update is $-\eta\mathcal L'(\theta)$. A positive derivative causes a positive quantity to be subtracted, reducing $\theta$; a negative derivative causes a negative quantity to be subtracted, increasing $\theta$. The size of the movement is $\eta|\mathcal L'(\theta)|$, so the learning rate controls the step size rather than its direction. When the derivative is $0$, this update also has a step of $0$, but the stationary-point counterexample above shows that this alone does not establish a minimum.

## Example 1. Increase, decrease, and the minimum of a quadratic

Consider

\[
f(x)=x^2-4x+3
\]

Expanding the difference quotient gives the derivative

\[
f'(x)=2x-4
\]

To find the critical point, solve

\[
2x-4=0
\]

Thus $x=2$ is a stationary point.

| Interval | Test input | Sign of $f'(x)$ | Behavior of $f$ |
|---|---:|---:|---|
| $x<2$ | $x=0$ | $-4<0$ | Decreasing |
| $x>2$ | $x=3$ | $2>0$ | Increasing |

The derivative's sign changes from $-$ to $+$, so there is a local minimum at $x=2$. Its function value is

\[
f(2)=4-8+3=-1
\]

Comparing the two sides of the minimum in the next figure shows the direction of the derivative's sign change.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The parabola x squared minus four x plus three decreases before input two and increases after it, reaching minus one at the minimum](../../figures/assets/M01/M01-04-sign-test-minimum.svg)

<figcaption>The derivative is negative to the left of x=2 and positive to its right. The curve decreases and then increases, reaching its minimum at (2, −1).</figcaption>
</figure>

## Example 2. A stationary point that is not an extremum

Expanding the difference quotient for $g(x)=x^3$ gives

\[
g'(x)=3x^2
\]

Since $g'(0)=0$, $x=0$ is a stationary point. However, for $x\ne0$,

\[
3x^2>0
\]

The derivative is positive on both sides of $0$ and does not change sign. The function increases on both sides, so $g(0)=0$ is neither a local maximum nor a local minimum.

## Example 3. A nondifferentiable minimum

The function $r(x)=|x|$ is not differentiable at $x=0$. Its slope is $-1$ when $x<0$ and $1$ when $x>0$.

\[
r'(x)
=
\begin{cases}
-1, & x<0,\\
1, & x>0
\end{cases}
\]

It decreases to the left of $0$ and increases to its right, so $r(0)=0$ is a local minimum. Looking only for points where $f'(x)=0$ would miss this candidate.

At the origin in the next figure, no single slope can be assigned, but the directions of decrease and increase on its two sides identify a minimum.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The absolute value function decreases with slope minus one and increases with slope plus one around its nondifferentiable minimum at zero](../../figures/assets/M01/M01-04-corner-minimum.svg)

<figcaption>The origin is a corner with no derivative, but its function value is lower than at nearby points on either side. Nondifferentiable critical points must also be considered as candidates for extrema.</figcaption>
</figure>

## Example 4. One parameter update

If

\[
\mathcal L(\theta)=(\theta-3)^2
\]

then

\[
\mathcal L'(\theta)=2(\theta-3)
\]

At $\theta=5$ with learning rate $\eta=0.1$,

\[
\mathcal L'(5)=4
\]

and the new parameter is

\[
\theta_{\mathrm{new}}
=
5-0.1\cdot4
=4.6
\]

Comparing the losses gives

\[
\mathcal L(5)=4,
\qquad
\mathcal L(4.6)=1.6^2=2.56
\]

The loss decreased in this example. This result cannot be generalized to other functions or large learning rates.

The next figure shows both the parameter's leftward movement and the decrease in its actual loss value.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A gradient step moves the parameter from five to four point six on the squared loss centered at three and lowers loss from four to two point five six](../../figures/assets/M01/M01-04-gradient-step.svg)

<figcaption>Moving 0.4 opposite to the current slope of 4 changes the parameter to 4.6. The loss at the new point is 2.56, below the original loss of 4.</figcaption>
</figure>

## Common misconceptions

### Misconception 1. $f'(x)>0$ means $f(x)>0$

$f'(x)>0$ indicates the increasing direction. Whether the function value lies above the $x$-axis is determined by the sign of $f(x)$.

### Misconception 2. $f'(c)=0$ guarantees an extremum at $c$

$f'(c)=0$ identifies a candidate for an extremum. Check whether the derivative changes sign across the point. The origin of $x^3$ is a counterexample.

### Misconception 3. The derivative must be $0$ at an extremum

If the function is differentiable at an interior extremum, its derivative must be $0$. Extrema can also occur at nondifferentiable points, such as the origin of $|x|$.

### Misconception 4. A large absolute derivative means a large function value

The derivative's absolute value indicates the steepness of change. Read the magnitude of the function value separately from the original function.

### Misconception 5. Moving opposite to the derivative guarantees that loss decreases

The derivative describes the neighborhood of the current point. With a large movement or a complicated function, a single update can increase the loss.

## Exercises

### 1. Distinguishing a derivative value from the derivative function

Given $f'(x)=2x+1$, explain what types of objects $f'$ and $f'(3)$ are, and calculate $f'(3)$.

<details>
<summary>Show solution</summary>

$f'$ is a function assigning a derivative value to each input $x$. The value $f'(3)$ is the scalar obtained by passing $3$ to that function.

\[
f'(3)=2\cdot3+1=7
\]

The original function therefore has tangent slope $7$ at $x=3$.

</details>

### 2. Reading intervals from the derivative's sign

Suppose a function has derivative $f'(x)=x-2$. Find the intervals where the function decreases and increases.

<details>
<summary>Show solution</summary>

When $x<2$, we have $x-2<0$, so the function decreases on $(-\infty,2)$. When $x>2$, we have $x-2>0$, so it increases on $(2,\infty)$. At $x=2$, we have $f'(2)=0$.

</details>

### 3. Identifying a local extremum

Determine what type of local extremum the function in Exercise 2 has at $x=2$.

<details>
<summary>Show solution</summary>

To the left of $x=2$, $f'(x)<0$; to the right, $f'(x)>0$. The function decreases and then increases, so it has a local minimum at $x=2$. Its function value cannot be calculated because neither the original function formula nor $f(2)$ is given.

</details>

### 4. Signs of a function value and a rate of change

We have $f(-1)=5$ and $f'(-1)=-2$. Explain the graph's position and its direction of change separately.

<details>
<summary>Show solution</summary>

Since $f(-1)=5>0$, the point $(-1,5)$ lies above the $x$-axis. Since $f'(-1)=-2<0$, the graph slopes downward to the right at that point, indicating a decreasing direction. A positive function value and a decreasing function can occur together.

</details>

### 5. A stationary-point counterexample

We have $g'(x)=3x^2$ and $g(0)=0$. Explain why $x=0$ is stationary but is not a local extremum.

<details>
<summary>Show solution</summary>

Since

\[
g'(0)=0
\]

$x=0$ is stationary. For both $x<0$ and $x>0$, we have $3x^2>0$, so the derivative is positive on both sides. The function increases on both sides as it passes through $0$, so $g(0)$ is neither a local maximum nor a local minimum.

</details>

### 6. A gradient-descent update

Given $\mathcal L'(\theta)=-6$, current parameter $\theta=1$, and learning rate $\eta=0.05$, calculate

\[
\theta_{\mathrm{new}}
=
\theta-\eta\mathcal L'(\theta)
\]

and explain the movement direction.

<details>
<summary>Show solution</summary>

\[
\theta_{\mathrm{new}}
=
1-0.05(-6)
=1+0.3
=1.3
\]

The derivative is negative, so increasing $\theta$ is a local direction of decreasing loss. The update increased $\theta$ by $0.3$. Whether the loss actually decreased must be checked by calculating it at the new point.

</details>

### 7. Assessing a claim about training having stopped

Holding all other parameters fixed and varying only a scalar parameter $\theta$, a researcher observes $\mathcal L'(\theta)=0$. They conclude, “The model has finished training, and all parameters have reached optimal values.” Distinguish what this conclusion establishes from what remains unestablished.

<details>
<summary>Show solution</summary>

The observed value supports the statement that the local rate of change in the selected parameter direction $\theta$ is $0$ for the current data and parameter state.

The rates of change in other parameter directions, the loss on other data batches, whether the stationary point is a minimum, and generalization performance remain unestablished. Claiming that training is complete requires examining the full gradient, changes in loss, evaluation-data performance, and stopping criteria together.

</details>

## Lesson summary

- The derivative $f'$ is a function assigning a derivative value to each input.
- A function increases on intervals where its derivative is positive and decreases where it is negative.
- Critical points are points where $f'(c)=0$ or the derivative does not exist; they are candidates for extrema.
- A derivative sign change from $+$ to $-$ indicates a local maximum, while a change from $-$ to $+$ indicates a local minimum.
- A loss derivative identifies a local decreasing direction but guarantees neither the loss after a large movement nor overall optimality.

## Pass criteria

You have passed this lesson if you can answer these questions without consulting the material:

- Can you explain the difference between $f'$ and $f'(a)$?
- Can you identify intervals of increase and decrease from the derivative's sign?
- Can you distinguish critical points from stationary points?
- Can you give an example of a stationary point that is not an extremum?
- Can you use the first derivative test to identify local extrema?
- Can you connect the derivative's sign to the movement direction in a gradient-descent update?

## Next lesson

The next lesson is [M01-05. Sum, product, and quotient rules](M01-05-sum-product-quotient-rules.md). Rather than calculating limits from the definition each time, you will learn rules for combining the derivatives of several functions.

## Author checklist

- [x] The learning objectives describe observable actions.
- [x] Derivatives, critical points, and stationary points are defined before use.
- [x] Signs of function values and derivative values are distinguished.
- [x] The examples of increase, decrease, and extrema have been checked.
- [x] Every exercise has a solution.
- [x] A local rate of change in one coordinate is distinguished from a claim of overall optimality.
- [x] The glossary and notation rules are followed.
- [x] The exercises do not require differentiation rules beyond the prerequisites.
- [x] Internal links and mathematical delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
