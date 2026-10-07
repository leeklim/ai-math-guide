---
id: "M01-08"
title: "Integration and accumulation"
part: 1
stage: "M01"
status: "complete"
prerequisites:
  - "M00-06"
  - "M01-02"
estimated_time: "100~120 minutes"
---

# M01-08. Integration and accumulation

## Why this lesson matters

Differentiation finds a rate of change near a point. Integration divides an interval into small pieces and adds their quantities to find the total accumulation. We use this structure to find displacement from velocity over time or to summarize function values over a continuous interval in one number.

A definite integral is related to the area under a graph, but it is a signed accumulation that includes negative function values. Reading it only as geometric area misses contributions below the $x$-axis and the direction of integration. Starting with summation notation, we examine the limit approached by sums of small rectangles.

## Learning objectives

After completing this lesson, you will be able to:

- Read the interval, integrand, and variable of integration in definite integral notation.
- Partition an interval and construct a Riemann sum.
- Calculate definite integrals of simple functions using area and signs.
- Apply linearity and interval additivity of integration.
- Explain the scope of interpretations supported by an accumulation function and an interval total.

## Prerequisite check

- Prerequisite lesson: [M00-06 Indices and summation notation](../M00/M00-06-indices-summation.md)
- Prerequisite lesson: [M01-02 Intuition for limits](M01-02-limits-intuition.md)
- Check question: Can you expand $\sum_{i=1}^{4}a_i$ into a sum of four terms?
- Check question: Can you read a limit expression in which the width of a piece approaches $0$?

If summation notation and limits are difficult, first review both prerequisite lessons.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| $[a,b]$ | `the closed interval from a to b` | Input interval over which to calculate accumulation | Use $a<b$ for the basic explanation. |
| $\Delta x$ | `delta x` | Width of a small subinterval in a partition | For equal widths, it is $(b-a)/n$. |
| $x_i^*$ | `x sub i star` | Sample point chosen in the $i$th subinterval | Choose it within that subinterval. |
| Riemann sum | `Riemann sum` | Approximation that adds products of function values and small widths | Depends on the partition and sample points. |
| $\int_a^b f(x)\,dx$ | `the integral from a to b of f of x d x` | Signed accumulation of $f$ over $[a,b]$ | Assume that the integral exists. |
| Integrand | `integrand` | Function $f(x)$ to accumulate inside the integral | Keep the signs of the function values. |
| Variable of integration | `variable of integration` | Input variable along which small subintervals are formed | In the expression above, it is $x$. |

## Core concept 1. Add small quantities to approximate a total

Divide the interval $[a,b]$ into $n$ subintervals of equal width.

\[
\Delta x=\frac{b-a}{n}
\]

Choose one sample point $x_i^*$ in the $i$th subinterval. Multiplying the function value $f(x_i^*)$ by the width $\Delta x$ approximates that piece's accumulated quantity as a rectangle.

This approximation fixes the function value within each piece at the sampled value. The actual function may vary within the piece, but representing its height by a single value lets us calculate its quantity as height times width. The sample point is an input position chosen inside the piece, and $f(x_i^*)$ is the height at that position, so they have different roles.

\[
f(x_i^*)\Delta x
\]

Adding all the pieces gives a Riemann sum.

\[
S_n
=
\sum_{i=1}^{n}
f(x_i^*)\Delta x
\]

As $n$ increases, $\Delta x$ decreases. If the function satisfies appropriate conditions and the Riemann sums approach one value independent of sample-point choices, we define that value as the definite integral.

A function continuous on a closed, finite interval satisfies this condition. Narrower pieces allow the representative height and actual function values within each piece to differ less, reducing the overall approximation error. Even as the number of pieces grows, the total width $n\Delta x=b-a$ stays unchanged. This is therefore different from adding more function values without widths.

The figure below divides [0, 1] into four pieces and builds rectangles using the right-endpoint heights of x².

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Four right-end rectangles approximate x squared on zero to one, each using width one quarter and the sampled function height](../../figures/assets/M01/M01-08-riemann-four.svg)

<figcaption>The orange points' input positions determine the heights; multiply each height by width 1/4. Using right endpoints on an increasing curve makes the rectangles include regions above the curve.</figcaption>
</figure>

## Core concept 2. A definite integral is the limit of Riemann sums

For equal-width partitions, write the definite integral as

\[
\int_a^b f(x)\,dx
\coloneqq
\lim_{n\to\infty}
\sum_{i=1}^{n}
f(x_i^*)\Delta x
\]

Read its parts as follows.

- $a$ and $b$ are the lower and upper limits of integration.
- $f(x)$ is the integrand.
- $dx$ indicates that we use $x$ as the variable of integration and accumulate over small widths.

While taking $n\to\infty$ in the definition, the widths in each partition remain $\Delta x>0$. We neither substitute the number $0$ for $dx$ nor omit the widths and add only function values. Whatever sample points we choose, finer partitions must approach the same value. A single Riemann sum with a particular choice of sample points cannot establish the integral's existence or exact value.

The result of a definite integral is a scalar summarizing the entire interval. Like a dummy summation index, $x$ has a role only inside the integral, so

\[
\int_a^b f(x)\,dx
=
\int_a^b f(t)\,dt
\]

The figure below divides the same interval into 16 pieces. Although the rectangle count increases, the entire interval still has width 1.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Sixteen narrower right-end rectangles follow x squared more closely over the same unit interval](../../figures/assets/M01/M01-08-riemann-refinement.svg)

<figcaption>Rectangles of width 1/16 follow the curve more closely than the four-piece partition. A finite partition remains an approximation; the definite integral is the limit as partition widths decrease.</figcaption>
</figure>

## Core concept 3. A definite integral is signed area

On an interval where $f(x)\ge0$, the definite integral equals the area between the graph and the $x$-axis. Regions with $f(x)<0$ contribute negatively.

\[
\int_a^b f(x)\,dx
=
\text{area above the $x$-axis}
-
\text{area below the $x$-axis}
\]

An integral of $0$ therefore does not mean that the function is $0$ throughout the interval. Positive and negative areas can cancel.

To count all geometric areas positively, use

\[
\int_a^b |f(x)|\,dx
\]

Distinguish a definite integral from the integral of the absolute value.

For the basic direction $a<b$, each piece has positive width, so its contribution takes the sign of its height $f(x_i^*)$. To find geometric area, first take the absolute value of each height and count every piece positively. Taking the absolute value of an integral after its positive and negative contributions have canceled is a different calculation. In Example 3 below, the integral is $0$, and its absolute value is also $0$, but the total geometric area is $1$.

## Core concept 4. Interval direction and splitting follow consistent rules

Starting and ending at the same point gives an accumulation interval of length $0$.

\[
\int_a^a f(x)\,dx=0
\]

Swapping the endpoints reverses the direction and changes the sign.

\[
\int_b^a f(x)\,dx
=
-\int_a^b f(x)\,dx
\]

This changes the direction in which we read the interval, not the signs of the function values. The rule assigns negative widths when accumulating in the direction of decreasing input. To calculate, integrate from the smaller endpoint to the larger endpoint, then negate the whole value if the requested direction is reversed.

For $a<c<b$, split the interval at $c$ and add.

\[
\int_a^b f(x)\,dx
=
\int_a^c f(x)\,dx
+
\int_c^b f(x)\,dx
\]

This is interval additivity. We can calculate accumulated values over separate intervals and combine them.

The figure below reads the same function over the same interval in two directions. The sign change comes from the integration direction, not the function's height.

<figure class="lesson-figure" markdown="1">

![The same triangular area two under x from zero to two gives positive two in the forward integration direction and negative two in reverse](../../figures/assets/M01/M01-08-direction-sign.svg)

<figcaption>Reading from 0 to 2 gives accumulation +2; reading from 2 to 0 gives −2. The green graph and the geometric area 2 are identical in both cases.</figcaption>
</figure>

## Core concept 5. Integration acts linearly on sums and constant multiples

For constants $\alpha$ and $\beta$,

\[
\int_a^b
\bigl[\alpha f(x)+\beta g(x)\bigr]\,dx
=
\alpha\int_a^b f(x)\,dx
+
\beta\int_a^b g(x)\,dx
\]

This follows because a Riemann sum can separate its terms and move constants outside the sum.

Linearity lets us calculate the accumulations of multiple signals or loss terms separately. Since positive and negative integrals can cancel, the overall value alone does not reveal the magnitudes of individual contributions.

The figure below separates the area contributions of f(x)=1 and g(x)=x into layers when they are added.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The area under one plus x on zero to two splits into a rectangle contributed by one and a triangle contributed by x](../../figures/assets/M01/M01-08-linearity-areas.svg)

<figcaption>The constant 1 contributes a rectangle of area 2, and x contributes a triangle of area 2, giving total area 4 under 1+x. Integrating the sum and adding the separate integrals give the same result.</figcaption>
</figure>

## Core concept 6. Integral units multiply function-value units by input-width units

Each piece of an integral is

\[
f(x_i^*)\Delta x
\]

so its units are also a product of the two units. If velocity is measured in meters/second and the time width in seconds, the integral is measured in meters.

\[
\frac{\text{meters}}{\text{seconds}}
\times
\text{seconds}
=
\text{meters}
\]

If the function value has units of loss and the horizontal axis is training time, the integral has units of `loss·time`. This differs from final loss or mean loss.

## Core concept 7. An accumulation function varies the endpoint of an integral

Fixing the starting point $a$ and varying the endpoint $x$ gives the accumulation function

\[
A(x)
=
\int_a^x f(t)\,dt
\]

The variable $t$ is used inside the integral, while $x$ is the accumulation endpoint.

For one chosen endpoint $x$, $A(x)$ is a number summarizing accumulation over that interval. Associating each endpoint with this number produces the function $A$. Although $A(x)$ and $f(x)$ use the same input, they are different quantities: accumulation from the starting point and the function value at the endpoint, respectively. Interval additivity gives

\[
A(x+h)-A(x)
=
\int_x^{x+h}f(t)\,dt
\]

Subtracting cancels the common accumulation from the starting point to $x$, leaving only the accumulation between the two endpoints. Renaming the variable of integration $t$ leaves this value unchanged, but changing endpoint $x$ changes the actual accumulation interval.

When $x$ increases slightly, $A(x)$ gains the accumulation over the newly added short interval. The next lesson uses the fundamental theorem of calculus to connect this rate of change to $f(x)$.

In the two graphs below, distinguish the function value at the endpoint from the accumulated value from the starting point.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The integrand t has a common area from zero to one and an added area from one to two, while the accumulation function increases from one half to two](../../figures/assets/M01/M01-08-moving-endpoint.svg)

<figcaption>The starting point 0 stays fixed as the endpoint moves from 1 to 2. Accumulation changes from 0.5 to 2; the difference 1.5 is the area over the new interval [1, 2].</figcaption>
</figure>

## Core concept 8. Distinguish discrete sums from continuous integrals

To add the losses of $N$ samples, use

\[
\sum_{i=1}^{N}\ell_i
\]

To accumulate over an interval of continuous variable $x$ by dividing it into small widths, use

\[
\int_a^b f(x)\,dx
\]

An integral resembles a sum, but each term includes a factor corresponding to the width $dx$. Converting a discrete sum to an integral requires stating which continuous variable the data sample and which interval width or weight each term represents. A large sample count alone does not permit the conversion.

## Example 1. Displacement at a constant velocity

Suppose velocity is constant at $3$ meters per second from $0$ to $4$ seconds.

\[
\int_0^4 3\,dt
\]

is the area of a rectangle with height $3$ and width $4$.

\[
\int_0^4 3\,dt
=
3\cdot4
=12
\]

The signed displacement is therefore $12$ meters.

In the figure below, multiplying the velocity height by the time interval's width also changes the units.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Constant velocity three meters per second over four seconds forms a rectangle whose accumulated displacement is twelve meters](../../figures/assets/M01/M01-08-constant-speed.svg)

<figcaption>The vertical axis is meters/second and the horizontal axis is seconds, so the rectangle's accumulated quantity has units of meters. Velocity 3 and accumulated displacement 12 are different quantities.</figcaption>
</figure>

## Example 2. Calculate an integral using triangular area

For

\[
\int_0^2 x\,dx
\]

the region between $y=x$ and the $x$-axis is a right triangle with base $2$ and height $2$.

\[
\int_0^2 x\,dx
=
\frac12\cdot2\cdot2
=2
\]

## Example 3. Cancellation of positive and negative regions

Integrate

\[
f(x)=x-1
\]

over $[0,2]$. On $[0,1]$, the graph lies below the $x$-axis with area $1/2$. On $[1,2]$, it lies above the $x$-axis with area $1/2$.

\[
\int_0^2(x-1)\,dx
=
-\frac12+\frac12
=0
\]

The total geometric area, however, is

\[
\frac12+\frac12=1
\]

In the figure below, count the triangles above and below the x-axis with their signs.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![For x minus one on zero to two the negative area minus one half and positive area plus one half cancel despite nonzero geometric area](../../figures/assets/M01/M01-08-signed-area.svg)

<figcaption>The hatched region contributes −1/2, and the green region contributes +1/2, canceling in the definite integral. Counting all areas positively gives 1, which differs from taking the absolute value of the integral 0.</figcaption>
</figure>

## Example 4. Construct a Riemann sum with four right endpoints

Divide $[0,1]$ into four subintervals for $f(x)=x^2$.

\[
\Delta x=\frac14
\]

Using right endpoints gives

\[
x_1^*=\frac14,
\quad
x_2^*=\frac24,
\quad
x_3^*=\frac34,
\quad
x_4^*=1
\]

The Riemann sum is

\[
S_4
=
\left[
\left(\frac14\right)^2
+
\left(\frac24\right)^2
+
\left(\frac34\right)^2
+1^2
\right]\frac14
\]

\[
=
\frac{1+4+9+16}{64}
=
\frac{30}{64}
=0.46875
\]

This is an approximation using four rectangles. As the subinterval count increases, the right-endpoint Riemann sum approaches the definite integral.

## Example 5. Interpret accumulated values of a training curve

Let $\mathcal L(t)$ be loss at training time $t\in[0,T]$.

\[
\int_0^T\mathcal L(t)\,dt
\]

is loss accumulated over time, with units of `loss·time`. Even two runs with the same final loss can have different integrals if their earlier loss curves differ.

A smaller value alone does not establish better generalization or a better learned internal mechanism. Comparisons require matching the time interval, recording interval, loss definition, and data conditions.

The figure below compares two illustrative loss functions with the same endpoint value. It does not show actual model training results.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two illustrative loss curves end at zero but one has an additional shaded area over time and therefore greater accumulated loss](../../figures/assets/M01/M01-08-same-final-different-area.svg)

<figcaption>Both curves have final loss 0, but A has the extra accumulation in the hatched region. The final function value and the integral over the entire time interval are different comparison criteria.</figcaption>
</figure>

## Common misconceptions

### Misconception 1. A definite integral is positive

Function values below the $x$-axis contribute negatively. A definite integral is a signed accumulation.

### Misconception 2. An integral of $0$ means the function is $0$ throughout the interval

Positive and negative regions can cancel. The integral of $f(x)=x-1$ over $[0,2]$ is an example.

### Misconception 3. $dx$ is decorative

The notation $dx$ indicates the variable of integration and small input widths. The integral's units also include the input-width units.

### Misconception 4. One Riemann sum is the exact definite integral

A Riemann sum over a finite partition is an approximation. The definite integral is the limit approached as partition widths decrease.

### Misconception 5. Enough data lets us replace a discrete sum with an integral

Specify how the continuous variable is partitioned and the width or weight of each term. Sample count alone does not create an integral structure.

## Exercises

### 1. Read integral notation

For

\[
\int_{-1}^{3}f(x)\,dx
\]

state the interval, integrand, and variable of integration, and explain the expression in an English sentence.

<details>
<summary>Show solution</summary>

The interval is $[-1,3]$, the integrand is $f(x)$, and the variable of integration is $x$. Read it as "integrate the function $f(x)$ with respect to $x$ from $x=-1$ to $x=3$." The result is the signed accumulation of $f$ over that interval.

</details>

### 2. Integrate a constant function

Calculate

\[
\int_2^7 4\,dx
\]

using area, and explain its units. Suppose $x$ is measured in seconds and the function values in watts.

<details>
<summary>Show solution</summary>

The height is $4$, and the interval width is $7-2=5$.

\[
\int_2^7 4\,dx
=
4\cdot5
=20
\]

The units are watt-seconds, the product of watts and seconds.

</details>

### 3. Calculate using a triangle

Calculate

\[
\int_0^3 2x\,dx
\]

using the area of the triangle under the graph.

<details>
<summary>Show solution</summary>

The line $y=2x$ joins $(0,0)$ and $(3,6)$. On $[0,3]$, it forms a triangle of base $3$ and height $6$.

\[
\int_0^3 2x\,dx
=
\frac12\cdot3\cdot6
=9
\]

</details>

### 4. Signed area

A function $f$ forms area $3$ above the $x$-axis on $[0,1]$ and area $5$ below the $x$-axis on $[1,2]$. Find $\int_0^2 f(x)\,dx$ and $\int_0^2|f(x)|\,dx$.

<details>
<summary>Show solution</summary>

The definite integral counts the area below the axis negatively.

\[
\int_0^2 f(x)\,dx
=
3-5
=-2
\]

Integrating the absolute value counts both areas positively.

\[
\int_0^2|f(x)|\,dx
=
3+5
=8
\]

</details>

### 5. Interval additivity and direction

Given

\[
\int_0^2 f(x)\,dx=4,
\qquad
\int_2^5 f(x)\,dx=-1
\]

find $\int_0^5 f(x)\,dx$ and $\int_5^0 f(x)\,dx$.

<details>
<summary>Show solution</summary>

Interval additivity gives

\[
\int_0^5 f(x)\,dx
=
4+(-1)
=3
\]

Reversing the integration direction changes the sign.

\[
\int_5^0 f(x)\,dx=-3
\]

</details>

### 6. Construct a Riemann sum

Divide $[0,2]$ into two equal-width subintervals for $f(x)=x$, and find the Riemann sum using right endpoints.

<details>
<summary>Show solution</summary>

The width is

\[
\Delta x=\frac{2-0}{2}=1
\]

The right endpoints are $1$ and $2$.

\[
S_2
=
f(1)\cdot1+f(2)\cdot1
=
1+2
=3
\]

This approximation exceeds the actual triangular area, $2$, because we used right endpoints for an increasing function.

</details>

### 7. Evaluate a claim about accumulated loss

In two models' training runs, model A has a smaller $\int_0^T\mathcal L(t)\,dt$. A researcher concludes, "Model A learned better internal representations and performs better on evaluation data." Explain what the integral directly shows and what further evidence is needed.

<details>
<summary>Show solution</summary>

If the calculations use matched conditions, the integral shows that model A had smaller accumulated training loss over the specified time interval.

The quality of internal representations and performance on evaluation data do not follow directly from this accumulated value. Check that the loss definition, time scale, and recording procedure are the same, then separately measure evaluation-data metrics and conduct representation-analysis experiments.

</details>

## Lesson summary

- A definite integral is the limit of Riemann sums that add products of function values and small interval widths.
- $\int_a^b f(x)\,dx$ is the signed accumulation of $f$ over $[a,b]$.
- Regions below the $x$-axis contribute negatively, so a definite integral can differ from geometric area.
- Integration is linear, and integrals over adjacent intervals can be added.
- The next lesson connects the rate of change of the accumulation function $A(x)=\int_a^x f(t)\,dt$ to $f(x)$.

## Pass criteria

You pass if you can answer these questions without consulting the material:

- Can you read a definite integral's lower limit, upper limit, integrand, and variable of integration?
- Can you construct a Riemann sum for an equal-width partition?
- Can you distinguish signed area from actual geometric area?
- Can you apply linearity, interval additivity, and reversal of integration direction?
- Can you explain an integral's units using the function-value units and input units?

## Next lesson

The next lesson is [M01-09 The fundamental theorem of calculus](M01-09-fundamental-theorem-calculus.md). You will learn why differentiation and integration connect through accumulation and rates of change.

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Partitions, Riemann sums, and definite integral notation are defined before use.
- [x] Area and Riemann sum examples have been checked.
- [x] Signed accumulation is distinguished from actual geometric area.
- [x] Every exercise has a solution.
- [x] Accumulated training loss is distinguished from claims about model quality.
- [x] The glossary and notation rules are followed.
- [x] The fundamental theorem of calculus is not required as a prerequisite.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
