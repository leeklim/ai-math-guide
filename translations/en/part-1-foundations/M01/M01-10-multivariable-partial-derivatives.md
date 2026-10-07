---
id: "M01-10"
title: "Multiple variables and partial derivatives"
part: 1
stage: "M01"
status: "complete"
prerequisites:
  - "M00-09"
  - "M01-06"
  - "M01-07"
estimated_time: "105~125 minutes"
---

# M01-10. Multiple variables and partial derivatives

## Why this lesson matters

A model's output depends on multiple inputs and parameters. To ask how its loss changes when one parameter varies, you need a rate of change that holds the other inputs fixed. Partial differentiation separates this question by coordinate.

One partial derivative describes only a local change at a selected point in one coordinate direction. Describing the effect of several variables changing together, or overall sensitivity, requires organizing the coordinate partial derivatives further. This lesson calculates the rate of change in each coordinate and prepares to combine them as directional derivatives and a gradient in the next lesson.

## Learning objectives

After this lesson, you will be able to:

- Express a multivariable scalar-valued function and its input coordinates mathematically.
- Explain partial differentiation as finding an instantaneous rate of change while holding the other variables fixed.
- Read the $\partial$ symbol and calculate the partial derivative functions of simple functions.
- Evaluate a partial derivative at a point and interpret its sign and units.
- Assess the scope of model-interpretation claims supported by a partial derivative in one coordinate.

## Prerequisite check

- Prerequisite lesson: [M00-09. Shapes of scalars, vectors, and matrices](../M00/M00-09-scalars-vectors-matrices-shape.md)
- Prerequisite lesson: [M01-06. Composition and the chain rule](M01-06-composition-chain-rule.md)
- Prerequisite lesson: [M01-07. Derivatives of exponential and logarithmic functions](M01-07-exponential-log-derivatives.md)
- Check question: Can you distinguish the derivative function of $f(x)=x^2$ from $f'(2)$?
- Check question: Can you explain what it means for $z=f(x,y)$ to have two inputs and one output?

Review M00-09 first if the types of inputs and outputs are unclear.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and conditions |
|---|---|---|---|
| $f:\mathbb R^2\to\mathbb R$ | `f maps R squared into R` | A function mapping two real inputs to one scalar | Input $(x,y)$; output $f(x,y)$ |
| $\frac{\partial f}{\partial x}$ | `partial f over partial x` | The rate of change when only $x$ varies and $y$ is fixed | A scalar-valued function |
| $\frac{\partial f}{\partial y}$ | `partial f over partial y` | The rate of change when only $y$ varies and $x$ is fixed | A scalar-valued function |
| $f_x,f_y$ | `f sub x and f sub y` | Abbreviations for the two partial derivative functions | Check the definitions in the text |
| Partial differentiation | `partial differentiation` | Differentiating with respect to one input while fixing the others | State the selected coordinate |
| Partial derivative function | `partial derivative function` | A function assigning each point its partial derivative value in one coordinate direction | Its output is a scalar |

## Core concept 1. A multivariable function takes the whole input point

The function

\[
f(x,y)=x^2+xy
\]

takes two real numbers $x,y$ and returns one real number.

\[
f:\mathbb R^2\to\mathbb R
\]

Its input is the coordinate pair $(x,y)$. For example,

\[
f(2,3)=2^2+2\cdot3=10
\]

Whereas a single-variable function has a curve as its graph in a plane, the graph $z=f(x,y)$ of a two-variable function can be represented as a surface in three-dimensional coordinates. A partial derivative is the slope of a curve obtained by slicing this surface in one coordinate direction.

The input point $(x,y)$ lies in the input plane. To draw the graph, add the output height $z$ and plot $(x,y,f(x,y))$. Fixing $y=b$ gives graph points $(x,b,f(x,b))$. Only $x$ varies along this slice, so its rate of change with respect to $x$ can be read as the slope of a single-variable curve.

Drawing positions in the input plane together with output heights shows how a function of coordinate pairs creates a surface.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Surface of x squared plus x y with a highlighted slice fixing y at three and the point two three ten](../../figures/assets/M01/M01-10-surface-and-slice.svg)
  <figcaption>The green surface is z=x²+xy, and the blue curve is the slice at y=3. The output 10 for input (2,3) is the height of point (2,3,10) on the surface. Moving along the blue curve changes only input x.</figcaption>
</figure>

## Core concept 2. A partial derivative with respect to $x$ fixes the other variables

The partial derivative with respect to $x$ at point $(a,b)$ is

\[
\frac{\partial f}{\partial x}(a,b)
\coloneqq
\lim_{h\to0}
\frac{f(a+h,b)-f(a,b)}{h}
\]

It holds $y=b$ fixed and changes only $x$ from $a$ to $a+h$.

The partial derivative with respect to $y$ is

\[
\frac{\partial f}{\partial y}(a,b)
\coloneqq
\lim_{h\to0}
\frac{f(a,b+h)-f(a,b)}{h}
\]

This time, $x=a$ is fixed.

The corresponding partial derivative value exists when its limit is a finite real number. The first definition is equivalent to forming the single-variable function $g(x)=f(x,b)$ and finding $g'(a)$. Holding a variable fixed means using the same value of $b$ in both function evaluations, not replacing $b$ with $0$ or removing it from the expression. Changing $y$ together with $x$ would calculate the rate of change along a different path.

The two definitions measure different input directions. Their values and signs can differ even at the same point.

The input plane shows which input is fixed, even before looking at the output graph.

<figure class="lesson-figure" markdown="1">
  ![Horizontal and vertical input-coordinate moves from point two comma three holding the other coordinate fixed](../../figures/assets/M01/M01-10-input-directions.svg)
  <figcaption>The horizontal move holds y=3 fixed and changes only x. The vertical move holds x=2 fixed and changes only y. This figure shows input movement, not the function's height or its rate of change.</figcaption>
</figure>

## Core concept 3. Treat the remaining variables as constants when calculating

Consider

\[
f(x,y)=x^2y+3y^2
\]

When differentiating partially with respect to $x$, treat $y$ as a constant.

\[
\frac{\partial f}{\partial x}
=
2xy
\]

The term $3y^2$ does not depend on $x$, so its rate of change with respect to $x$ is $0$.

In $x^2y$, however, the fixed $y$ is a coefficient of $x^2$. The constant-multiple rule gives $y\cdot2x=2xy$. Distinguish a fixed variable that remains as a multiplicative coefficient from a term containing only that variable, whose derivative is $0$.

When differentiating partially with respect to $y$, treat $x$ as a constant.

\[
\frac{\partial f}{\partial y}
=
x^2+6y
\]

Both partial derivative functions can vary with the input $(x,y)$.

Whether a variable is treated as constant depends on the variable of differentiation. With respect to $y$, the factor $x^2$ in $x^2y$ remains as a coefficient, and the derivative of $y$ is $1$, giving first term $x^2$. Nor is it contradictory for $y$ to remain in the partial derivative with respect to $x$. After differentiating on one slice with $y$ fixed, examining a different slice can change the fixed value $y$.

Choosing different fixed values gives different single-variable slices. The fixed variable remains a coefficient in each slice.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Three x-direction slices of x squared y plus three y squared with fixed y values one two and three](../../figures/assets/M01/M01-10-fixed-slice-family.svg)
  <figcaption>Fixing y at 1, 2, and 3 gives slices x²+3, 2x²+12, and 3x²+27, respectively. Even at the same x=1, their slopes are 2, 4, and 6. Fixing y does not mean erasing it.</figcaption>
</figure>

## Core concept 4. Evaluation at a point gives a coordinate-direction slope

Substituting $(x,y)=(1,2)$ in the preceding function gives

\[
\frac{\partial f}{\partial x}(1,2)
=
2\cdot1\cdot2
=4
\]

and

\[
\frac{\partial f}{\partial y}(1,2)
=
1^2+6\cdot2
=13
\]

The first value is the local rate of change when $x$ increases with $y=2$ fixed. The second is the local rate of change when $y$ increases with $x=1$ fixed. Comparing their magnitudes requires checking the units and scales of $x$ and $y$ as well.

One input point has one output height, but its slice's tangent slope depends on which coordinate varies.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Two coordinate slices through input point one comma two with common output fourteen and tangent slopes four and thirteen](../../figures/assets/M01/M01-10-coordinate-slopes.svg)
  <figcaption>The orange points on both graphs represent output 14 at the original input (1,2). The upper graph holds y=2 fixed and has x-direction slope 4. The lower graph holds x=1 fixed and has y-direction slope 13. Their horizontal axes represent different inputs.</figcaption>
</figure>

## Core concept 5. $d$ and $\partial$ distinguish input structures

For a single-variable function $g(x)$, use

\[
\frac{dg}{dx}
\]

For a multivariable function $f(x,y)$, selecting one variable for differentiation gives

\[
\frac{\partial f}{\partial x},
\qquad
\frac{\partial f}{\partial y}
\]

The symbol $\partial$ indicates the presence of other independent variables. If all variables depend on one path parameter, the rate of change along the whole path involves both the partial derivatives and the rates of change of the individual variables. The next lesson combines them through directional derivatives.

## Core concept 6. Single-variable differentiation rules also apply to partial derivatives

After fixing the other variables, the sum, product, and chain rules still apply.

For

\[
f(x,y)=\exp(xy)
\]

treating $y$ as constant gives derivative $y$ for the inner function $xy$ with respect to $x$.

\[
\frac{\partial f}{\partial x}
=
y\exp(xy)
\]

Conversely, treating $x$ as constant gives

\[
\frac{\partial f}{\partial y}
=
x\exp(xy)
\]

Check the domain for logarithms as well. If $g(x,y)>0$, then

\[
\frac{\partial}{\partial x}\log g(x,y)
=
\frac{1}{g(x,y)}
\frac{\partial g}{\partial x}(x,y)
\]

## Core concept 7. Units depend on the selected input coordinate

Let $s(T,P)$ be a score depending on temperature $T$ and pressure $P$.

The units of

\[
\frac{\partial s}{\partial T}
\]

are `score/temperature`, while the units of

\[
\frac{\partial s}{\partial P}
\]

are `score/pressure`. Because the units differ, comparing only absolute numerical values cannot establish which variable is more important.

Rescaling an input also changes its partial derivative value. Using centimeters instead of meters changes coordinate numbers by a factor of 100, while the rate of change with respect to that coordinate changes inversely. Comparing sensitivities requires stating the units and allowed ranges of change.

Increasing a centimeter coordinate by $1$ is the same physical change as increasing a meter coordinate by $0.01$. Dividing the same output change by its size in centimeters gives a rate $1/100$ of the rate obtained using meters. The function's physical response has not changed; the input unit used to measure the change has.

Representing the same physical input in different units changes both the horizontal-axis scale and the numerical slope.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![The same score versus distance drawn once in meters and once in centimeters with slopes four and zero point zero four](../../figures/assets/M01/M01-10-rescaled-input.svg)
  <figcaption>The illustrative score has slope 4 when distance is expressed in meters and 0.04 when expressed in centimeters. Both orange points represent the same distance, 1m=100cm, and score 4. The output response has not changed; the input's numerical scale has.</figcaption>
</figure>

## Core concept 8. A partial derivative in one coordinate does not describe other directions

The statement

\[
\frac{\partial f}{\partial x}(a,b)=0
\]

means that the first-order rate of change in the $x$ direction, with $y=b$ fixed, is $0$. It does not determine the rate in the $y$ direction or a direction that changes $x$ and $y$ together.

Even with a partial derivative of $0$, the function value can change after a finite movement. For example, both partial derivatives of $f(x,y)=x^2+y^2$ are $0$ at the origin, but function values away from the origin are positive.

A first-order rate of change of 0 and an unchanged function value after finite movement are different claims.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![A quadratic slice of x squared plus y squared with zero tangent slope at the origin but positive values away from it](../../figures/assets/M01/M01-10-zero-local-slope.svg)
  <figcaption>Both partial derivatives at the origin are 0. On the slice y=0, the tangent at the origin is horizontal, but moving x by 1 gives function value 1. The tangent represents only the local first-order change.</figcaption>
</figure>

## Example 1. Partial derivative functions of a polynomial

For

\[
f(x,y)=3x^2y-2xy^2+5
\]

fix $y$ and differentiate with respect to $x$.

\[
\frac{\partial f}{\partial x}
=
6xy-2y^2
\]

Fixing $x$ and differentiating with respect to $y$ gives

\[
\frac{\partial f}{\partial y}
=
3x^2-4xy
\]

## Example 2. A slice with one fixed coordinate

For

\[
f(x,y)=x^2+xy
\]

fixing $y=3$ gives the single-variable slice

\[
g(x)=f(x,3)=x^2+3x
\]

Its derivative is

\[
g'(x)=2x+3
\]

Substituting $y=3$ into the original function's partial derivative also gives

\[
\frac{\partial f}{\partial x}(x,3)
=
2x+3
\]

## Example 3. Squared loss for a linear prediction

Fix input $x$ and target $y$, and define the prediction and loss for parameters $w,b$ as

\[
\hat y=wx+b
\]

\[
\mathcal L(w,b)=(\hat y-y)^2
\]

Writing the error as

\[
e=wx+b-y
\]

gives $\mathcal L=e^2$. By the chain rule,

\[
\frac{\partial\mathcal L}{\partial w}
=
2e\frac{\partial e}{\partial w}
=
2ex
\]

and

\[
\frac{\partial\mathcal L}{\partial b}
=
2e\frac{\partial e}{\partial b}
=
2e
\]

If $x=2$, $y=5$, $w=1$, and $b=1$, then $e=2+1-5=-2$. Therefore,

\[
\frac{\partial\mathcal L}{\partial w}=-8,
\qquad
\frac{\partial\mathcal L}{\partial b}=-4
\]

Drawing two loss slices, each with the other parameter fixed, shows which slope each partial derivative represents.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Weight and bias slices of the same squared loss through parameter point one comma one with tangent slopes minus eight and minus four](../../figures/assets/M01/M01-10-loss-slices.svg)
  <figcaption>With the input and target fixed, the loss at (w,b)=(1,1) is 4. The upper graph fixes b and varies only w, with slope −8. The lower graph fixes w and varies only b, with slope −4. Both points come from the same parameter state.</figcaption>
</figure>

## Example 4. Different coordinate sensitivities in the same function

If

\[
s(x,y)=x+100y
\]

then

\[
\frac{\partial s}{\partial x}=1,
\qquad
\frac{\partial s}{\partial y}=100
\]

Judging only by these numbers, the $y$ direction appears more sensitive. But if the natural range of change for $x$ is $100$ and that for $y$ is $0.01$, comparing output changes over the allowed ranges gives a different result. Present partial derivative values together with input scales.

For this linear function, multiplying the slope by the actual input change gives the exact output change. Including allowed ranges changes the ranking obtained from numerical slopes alone.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Numeric partial slopes one and one hundred compared with output changes one hundred and one over stated input ranges](../../figures/assets/M01/M01-10-range-comparison.svg)
  <figcaption>Above, the y partial derivative of 100 is larger than the x value of 1. Below, changing x by 100 gives output change 100, larger than the change of 1 from changing y by 0.01. The quantities compared and the horizontal axes differ between the panels.</figcaption>
</figure>

## Common misconceptions

### Misconception 1. Partial differentiation with respect to $x$ sets the other variables to $0$

Treat the other variables as constants at their current values. This is not a rule for substituting $0$.

### Misconception 2. $\partial f/\partial x$ is one fixed number

A partial derivative function can vary with the input point. Evaluating it at a point, as in $\frac{\partial f}{\partial x}(a,b)$, gives a scalar value.

### Misconception 3. One partial derivative of $0$ means the function is unchanged near the point

Only the first-order rate of change in that coordinate direction is $0$. Changes in other directions and after finite movements may remain.

### Misconception 4. The coordinate with the largest absolute partial derivative is the most important cause

A partial derivative is a local sensitivity dependent on units and coordinate scale. Causal importance requires interventions and comparison conditions.

### Misconception 5. One partial derivative function also describes a vector output

This lesson concerns scalar-valued functions. Rates of change between every vector-output component and input coordinate are organized in a Jacobian.

## Exercises

### 1. Reading partial-derivative notation

Explain the following expression in an English sentence:

\[
\frac{\partial f}{\partial x}(2,-1)=3
\]

<details>
<summary>Show solution</summary>

At point $(2,-1)$, the instantaneous rate of change of $f$ is $3$ when only $x$ varies and $y=-1$ is held fixed. Equivalently, the tangent slope of the slice in the $x$ direction is $3$.

</details>

### 2. Calculating two partial derivative functions

Find the partial derivative functions with respect to $x$ and $y$ for

\[
f(x,y)=x^2+3xy+y^2
\]

<details>
<summary>Show solution</summary>

Treat $y$ as constant and differentiate with respect to $x$.

\[
\frac{\partial f}{\partial x}
=
2x+3y
\]

Treat $x$ as constant and differentiate with respect to $y$.

\[
\frac{\partial f}{\partial y}
=
3x+2y
\]

</details>

### 3. Evaluating at a point

Evaluate the partial derivative functions from Exercise 2 at $(x,y)=(1,2)$.

<details>
<summary>Show solution</summary>

\[
\frac{\partial f}{\partial x}(1,2)
=
2\cdot1+3\cdot2
=8
\]

and

\[
\frac{\partial f}{\partial y}(1,2)
=
3\cdot1+2\cdot2
=7
\]

The first is the $x$-direction rate of change with $y=2$ fixed; the second is the $y$-direction rate with $x=1$ fixed.

</details>

### 4. Partial derivatives of an exponential function

Find both partial derivative functions of

\[
g(x,y)=\exp(x+2y)
\]

<details>
<summary>Show solution</summary>

With respect to $x$, the inner function $x+2y$ has rate of change $1$.

\[
\frac{\partial g}{\partial x}
=
\exp(x+2y)
\]

With respect to $y$, its inner rate of change is $2$.

\[
\frac{\partial g}{\partial y}
=
2\exp(x+2y)
\]

</details>

### 5. Parameter partial derivatives of a squared loss

Find the partial derivative functions of

\[
\mathcal L(w,b)=(3w+b-4)^2
\]

with respect to $w$ and $b$.

<details>
<summary>Show solution</summary>

Setting $e=3w+b-4$ gives $\mathcal L=e^2$.

\[
\frac{\partial\mathcal L}{\partial w}
=
2e\cdot3
=
6(3w+b-4)
\]

and

\[
\frac{\partial\mathcal L}{\partial b}
=
2e\cdot1
=
2(3w+b-4)
\]

</details>

### 6. A point with a partial derivative of 0

For

\[
f(x,y)=x^2+y
\]

find $\frac{\partial f}{\partial x}(0,2)$ and determine whether this result alone implies that $f$ is constant in all directions around $(0,2)$.

<details>
<summary>Show solution</summary>

Since

\[
\frac{\partial f}{\partial x}=2x
\]

we have

\[
\frac{\partial f}{\partial x}(0,2)=0
\]

This means that the first-order rate in the $x$ direction, with $y=2$ fixed, is $0$. The partial derivative with respect to $y$ is $1$, so the function changes in the $y$ direction. The conclusion of constancy in all directions does not follow.

</details>

### 7. Assessing a coordinate-sensitivity claim

For two unstandardized inputs $x_1,x_2$, a researcher obtains

\[
\left|\frac{\partial s}{\partial x_1}\right|=50,
\qquad
\left|\frac{\partial s}{\partial x_2}\right|=2
\]

at one point and claims, “$x_1$ is 25 times more important than $x_2$ as a cause of the model output.” Critique the conclusion and state what information is needed.

<details>
<summary>Show solution</summary>

These values are local sensitivities when each coordinate is varied separately at the selected point. If input units and scales differ, the ratio of absolute values, $25$, cannot be interpreted as an importance ratio.

Check the allowed input ranges, units, and sensitivities at multiple data points. A causal claim also requires information about the data-generating process, controlled interventions, and comparison conditions.

</details>

## Lesson summary

- A multivariable scalar-valued function takes the whole input point $(x,y)$ and returns a scalar.
- $\partial f/\partial x$ is the local rate of change when only $x$ varies and the other variables are fixed.
- For partial differentiation, treat fixed variables as constants and apply single-variable differentiation rules.
- Partial derivative values depend on the point, coordinate direction, units, and scale.
- A partial derivative in one coordinate does not describe changes in other directions or causal effects.

## Pass criteria

You have passed this lesson if you can answer these questions without consulting the material:

- Can you explain the inputs and output of $f:\mathbb R^2\to\mathbb R$?
- Can you state which variables are fixed in a partial-derivative definition?
- Can you calculate both partial derivative functions of polynomials and composite functions?
- Can you evaluate a partial derivative at a point and interpret its sign and units?
- Can you distinguish what cannot be concluded when a partial derivative in one coordinate is $0$?

## Next lesson

The next lesson is [M01-11. Directional derivatives and the gradient](M01-11-directional-derivative-gradient.md). It collects coordinate partial derivatives into a vector and connects them to the rate of change in an arbitrary direction.

## Author checklist

- [x] The learning objectives describe observable actions.
- [x] Multivariable scalar-valued functions and partial-derivative notation are defined before use.
- [x] Examples demonstrate the calculation principle of holding other variables fixed.
- [x] Partial derivatives of polynomials, exponential functions, and squared losses have been checked.
- [x] Every exercise has a solution.
- [x] Coordinate sensitivity is distinguished from claims of causal importance.
- [x] The glossary and notation rules are followed.
- [x] Directional derivatives, gradients, and Jacobians are not required as prerequisites.
- [x] Internal links and mathematical delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
