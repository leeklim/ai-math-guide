---
id: "M00-04"
title: "Coordinates and graphs"
part: 1
stage: "M00"
status: "complete"
prerequisites:
  - "M00-02"
  - "M00-03"
estimated_time: "75~90 minutes"
---

# M00-04. Coordinates and graphs

## Why this lesson matters

Papers often show changes in a function through graphs rather than tables. Loss over training steps, activation versus input magnitude, and performance versus the amount of data all appear in graphs. Reading a graph requires identifying what its axes mean, which two values each point pairs, and whether a line represents observations or interpolation.

A curved function graph alone does not establish that the input space or representation space is curved. A graph places a function's inputs and outputs in one coordinate plane. Claims about the geometry of a space require a separate definition of structures such as distance or curvature.

## Learning objectives

After this lesson, you should be able to:

- Plot an ordered pair $(x,y)$ as a point in the coordinate plane.
- Explain the graph of $y=f(x)$ as the collection of points $(x,f(x))$.
- Obtain coordinates from a table and draw the graph of a simple function.
- Read function values, intercepts, and increasing or decreasing trends from a graph.
- Assess how axis scales and the way points are connected affect graph interpretation.

## Prerequisite check

- Prerequisite lesson: [M00-02 Expressions, equalities, and equations](M00-02-expressions-equalities-equations.md)
- Prerequisite lesson: [M00-03 Function inputs and outputs](M00-03-functions-input-output.md)

Check whether you can answer these questions.

1. Can you distinguish the input from the output in $y=2x+1$?
2. If $f(x)=x^2$, can you calculate $f(-2)$ and $f(2)$?

Both answers to the second question are $4$. The two inputs give different points on the graph.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Scope |
|---|---|---|---|
| $(x,y)$ | `the ordered pair x comma y` | A point with horizontal coordinate $x$ and vertical coordinate $y$ | Reversing the order may give a different point |
| $x$-axis | `the x-axis` | The horizontal reference line | Usually used for inputs |
| $y$-axis | `the y-axis` | The vertical reference line | Usually used for outputs |
| origin | `origin` | The point where the two axes meet | $(0,0)$ |
| graph | `graph` | Points representing the correspondence between inputs and outputs | Function graphs in this lesson |
| intercept | `intercept` | Where a graph meets a coordinate axis | An $x$-intercept or a $y$-intercept |

## Core concept 1. Ordered pairs preserve the roles of two values

### The coordinate plane

The coordinate plane represents positions using two perpendicular number lines. The horizontal axis is the $x$-axis, and the vertical axis is the $y$-axis. They meet at the origin $(0,0)$.

To plot $(3,2)$, move $3$ horizontally and $2$ vertically from the origin. The first number determines the horizontal position, and the second determines the vertical position.

Read each coordinate relative to $0$ on its axis. A horizontal coordinate of $3$ means a position $3$ to the right of the $y$-axis; a vertical coordinate of $2$ means a position $2$ above the $x$-axis. Because coordinates determine a point's position, moving vertically first and then horizontally reaches the same point. The order in an ordered pair identifies which axis each number belongs to, not the order of the moves.

\[
(3,2)\ne(2,3)
\]

The two points use the same numbers but have different positions. The order records the role of each value.

Read negative coordinates in the same way.

- $(-2,3)$: $2$ left and $3$ up from the origin
- $(2,-3)$: $2$ right and $3$ down from the origin
- $(-2,-3)$: $2$ left and $3$ down from the origin

You can read an ordered pair by moving horizontally according to the first value and then vertically according to the second. In the figure below, $(3,2)$ and $(2,3)$ use the same two numbers but exchange the horizontal and vertical distances, reaching different points.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two coordinate planes trace different horizontal and vertical moves for the ordered pairs three comma two and two comma three](../../figures/assets/M00/M00-04-c01-visual.svg)

<figcaption>On the left, moving 3 horizontally and 2 vertically reaches (3,2). On the right, moving 2 horizontally and 3 vertically reaches (2,3). Coordinate order determines the axis assigned to each number.</figcaption>
</figure>

Negative coordinates lie to the left or below 0 on the corresponding axis, as the next figure shows. Dashed lines connect each point's horizontal and vertical positions to the axes.

<figure class="lesson-figure" markdown="1">

![Three points with negative coordinate components lie to the left of the y-axis or below the x-axis on a labeled grid](../../figures/assets/M00/M00-04-signed-coordinates.svg)

<figcaption>The sign of the first coordinate determines left or right; the sign of the second determines up or down. (-2,3) and (2,-3) differ in their positions along both axes.</figcaption>
</figure>

## Core concept 2. A function graph is a collection of points $(x,f(x))$

The graph of a function $f$ plots the point

\[
(x,f(x))
\]

in the coordinate plane for each input $x$ in the domain.

For example, if

\[
f(x)=2x+1
\]

and we consider only $x=-1,0,1,2$, we obtain this table.

| Input $x$ | Output $f(x)=2x+1$ | Point on the graph |
|---:|---:|:---:|
| $-1$ | $-1$ | $(-1,-1)$ |
| $0$ | $1$ | $(0,1)$ |
| $1$ | $3$ | $(1,3)$ |
| $2$ | $5$ | $(2,5)$ |

Each row corresponds to one point on the graph. The input determines the horizontal position, and the output determines the vertical position.

When transferring a table to a graph, keep each input paired with its output. Combine $x$ and $f(x)$ from the same row into the ordered pair $(x,f(x))$, then plot the point at $x$ on the horizontal axis and $f(x)$ on the vertical axis. Labels A through D in the figure below connect the four table rows to their four points.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A value table for two x plus one maps labeled input-output pairs to four points on the matching line graph](../../figures/assets/M00/M00-04-c02-visual.svg)

<figcaption>Each table row forms one ordered pair (x,f(x)). Labels A, B, C, and D let you trace that pair to its point on the graph.</figcaption>
</figure>

### Reading function values from a graph

To read $f(2)$ from the graph:

1. Find $x=2$ on the $x$-axis.
2. Find the point on the graph at that horizontal position.
3. Read the point's $y$-coordinate.

In this example, the point is $(2,5)$, so

\[
f(2)=5
\]

Fixing the input at $2$ means looking up or down at the horizontal position $2$. A function assigns one output to this input, so two points at different heights cannot share that horizontal coordinate. The input must belong to the domain for a point to exist there.

Conversely, to find $x$ satisfying $f(x)=3$, look along the height $y=3$ and read the $x$-coordinate where it meets the graph. For this function, $x=1$.

Fixing an output and looking for its inputs may give several points at the same height. For example, the graph of $f(x)=x^2$ contains both $(-2,4)$ and $(2,4)$. Their inputs differ, so these points satisfy the definition of a function, and two inputs produce the output $4$. Reading the value for a given input and finding the inputs for a given value are different tasks.

In the next figure, the vertical dashed line fixes the input at 2, and the horizontal dashed line fixes the output at 4. They meet the graph at different numbers of points.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A vertical guide at input two intersects the parabola once, while a horizontal guide at output four intersects at inputs negative two and two](../../figures/assets/M00/M00-04-graph-reading-directions.svg)

<figcaption>At x=2, there is one function value, 4. Conversely, inputs -2 and 2 both produce the output 4. The curve represents the input-output relation, while the coordinate axes remain straight.</figcaption>
</figure>

## Core concept 3. Check the domain before connecting points

If the domain is all real numbers and $f(x)=2x+1$, the inputs between the plotted values also have outputs. At $x=0.5$,

\[
f(0.5)=2
\]

is also defined. In this case, connecting the calculated points with a straight line can represent the whole graph.

We can draw that line because the rule $2x+1$ also applies to the inputs between the points. Substituting $0.5$, between $x=0$ and $x=1$, gives the output $2$, between $1$ and $3$. Calculating intermediate inputs with the same rule places them all on that line. A few visible points alone do not justify drawing a straight line. For a general function, the graph between two points may curve or have a break.

If the domain consists of only a few values, such as $\{-1,0,1,2\}$, inputs between the four points are not allowed. Connecting the points may suggest outputs for inputs where the function has not been defined.

The same issue arises in experimental graphs. If researchers measure values only at epochs $1,2,3$, the line segments help display trends between measurements. Not every point on the line was observed.

The next figure shows how the domain determines whether the graph includes points between the plotted values, even with the same computational rule.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Four discrete points for two x plus one are contrasted with the continuous line that also contains input zero point five and output two](../../figures/assets/M00/M00-04-discrete-continuous-domain.svg)

<figcaption>On the left, only four inputs are allowed, so the points are not connected. On the right, real inputs are allowed, so the intermediate point (0.5,2) also belongs to the graph.</figcaption>
</figure>

## Core concept 4. Read intercepts and increasing or decreasing behavior

### The $y$-intercept

The $y$-intercept is the $y$-coordinate where the graph meets the $y$-axis. On the $y$-axis, $x=0$, so find the function's $y$-intercept from $f(0)$.

A point on the vertical axis has no horizontal displacement from the origin, so its horizontal coordinate is $0$. This is why we substitute $x=0$ to find the $y$-intercept. Conversely, a point on the horizontal axis has vertical coordinate $0$, so to find the $x$-intercept, set the output $y=f(x)$ to $0$. The name $y$-intercept does not mean that we substitute $y=0$.

If

\[
f(x)=2x+1
\]

then

\[
f(0)=1
\]

so the $y$-intercept is $1$, and the intersection point is $(0,1)$.

### The $x$-intercept

The $x$-intercept is the $x$-coordinate where the graph meets the $x$-axis. On the $x$-axis, $y=0$, so find $x$ satisfying

\[
f(x)=0
\]

\[
2x+1=0
\]

Subtracting $1$ from both sides gives

\[
2x=-1
\]

and dividing both sides by $2$ gives

\[
x=-\frac12
\]

The $x$-intercept is therefore $-\frac12$, and the intersection point is $\left(-\frac12,0\right)$.

In the next figure, identifying the axis of intersection tells you which coordinate to set to 0.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The line two x plus one crosses the x-axis at negative zero point five comma zero and the y-axis at zero comma one](../../figures/assets/M00/M00-04-axis-intercepts.svg)

<figcaption>At an intersection with the x-axis, the vertical coordinate y is 0. At an intersection with the y-axis, the horizontal coordinate x is 0. Distinguish the intercept's name from the coordinate set to 0.</figcaption>
</figure>

### Increasing and decreasing behavior

On an interval where $f(x)$ increases as $x$ increases, the graph rises as you move to the right. On an interval where $f(x)$ decreases as $x$ increases, it falls as you move to the right.

Increasing or decreasing behavior differs from whether the output is positive or negative. In the table above, as the input increases from $-1$ to $0$, the output increases from $-1$ to $1$. This change is an increase even though the starting output is negative. Compare the heights of the two points rather than only noting which side of an axis the graph lies on.

These descriptions compare changes between two inputs. Later calculus lessons measure the rate of change near a point using a derivative.

The next figure compares whether the points become higher or lower as you move to the right.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An increasing segment rises from output negative one to one, whereas a decreasing segment falls from one to negative one](../../figures/assets/M00/M00-04-increase-decrease.svg)

<figcaption>On the left, the output starts at a negative value, -1, but increases to 1. On the right, it starts at a positive value, 1, but decreases to -1. Judge increasing or decreasing behavior by the difference between two values, not their signs.</figcaption>
</figure>

## Core concept 5. Graph shape and the geometry of a space are different claims

The graph of

\[
f(x)=x^2
\]

is a curve. This curve plots the relation between a real input $x$ and the output $f(x)$ in a plane.

The input $x$ itself is a position on the real line, and the output $x^2$ is also a value on the real line. To draw the graph, we pair these values as $(x,x^2)$ and plot one point in the plane. The curved shape comes from the arrangement of points that record inputs together with outputs. The horizontal axis for inputs and the vertical axis for outputs remain straight.

In the earlier figure on reading function values, the parabola is curved, but the x-axis used for inputs and the y-axis used for outputs are straight. Distinguish the curve from the shape of the axes in the figure.

Observing a curved graph alone does not establish that the real line containing the inputs is itself curved. Nor does the fact that a nonlinear neural-network function produces a curved graph directly define curvature in the representation space.

To treat a claim that a space is curved mathematically, define how to measure lengths and angles in that space, then calculate curvature under that structure. Part 4 covers this in differential geometry.

## Example 1. Obtain points to plot from a table

### Problem

If

\[
g(x)=x^2-1
\]

and $x=-2,-1,0,1,2$, calculate the points to plot on the graph.

### Solution

Calculate the function value for each input.

\[
g(-2)=(-2)^2-1=3
\]

\[
g(-1)=(-1)^2-1=0
\]

\[
g(0)=0^2-1=-1
\]

\[
g(1)=1^2-1=0
\]

\[
g(2)=2^2-1=3
\]

These results give the following table.

| $x$ | $g(x)$ | Point |
|---:|---:|:---:|
| $-2$ | $3$ | $(-2,3)$ |
| $-1$ | $0$ | $(-1,0)$ |
| $0$ | $-1$ | $(0,-1)$ |
| $1$ | $0$ | $(1,0)$ |
| $2$ | $3$ | $(2,3)$ |

### Meaning of the result

Although $g(-2)=g(2)$, the graph points $(-2,3)$ and $(2,3)$ differ. They share a vertical height but have different horizontal positions.

## Example 2. Identify a formula from graph information

Suppose a straight-line graph passes through $(0,-2)$ and $(2,4)$. As $x$ increases by $2$ from $0$ to $2$, $y$ increases by $6$ from $-2$ to $4$.

The change in output for an input increase of $1$ is

\[
\frac{4-(-2)}{2-0}=\frac62=3
\]

Since the line passes through $(0,-2)$, its output at $x=0$ is $-2$. We can express this line as

\[
y=3x-2
\]

This example uses the line's constant change per unit input. M01 covers the general definition and calculation of slope.

## Example 3. Read a learning curve

Suppose the following values were recorded while training a model.

| Training step $t$ | Loss $L_t$ |
|---:|---:|
| $0$ | $2.4$ |
| $100$ | $1.5$ |
| $200$ | $1.1$ |
| $300$ | $1.0$ |

The horizontal axis shows training steps, and the vertical axis shows loss. The point $(200,1.1)$ means that the loss recorded at step 200 was $1.1$.

Loss decreased over the range shown in the table. It fell by $0.9$ between steps $0$ and $100$, and by $0.1$ between steps $200$ and $300$. The decrease was smaller in the later interval.

This graph alone does not establish that a particular optimizer or model architecture caused the decrease. Comparing causes requires controlled experiments that hold other conditions fixed. A decrease in training loss also does not guarantee improved performance on validation data.

## A checklist for reading graphs

When reading a graph in a paper, check:

1. The variables represented by the horizontal and vertical axes
2. Axis units and tick spacing
3. The statistics represented by points, lines, and shading
4. The observed range and any range omitted from the graph
5. Whether points were connected or smoothing was applied
6. The claims the graph directly supports and those requiring further experiments

Also check whether an axis uses a logarithmic scale. Equal spacing may not mean equal differences. The next lesson covers logarithmic scales.

## Common misconceptions

### Misconception 1. The two numbers in $(x,y)$ can be exchanged

The first number determines the horizontal position, and the second the vertical position. $(1,3)$ and $(3,1)$ are different points.

### Misconception 2. Points from a table must always be connected

If the domain is discrete, inputs between the points may not be defined. A line connecting experimental values also visually interpolates unobserved intervals.

### Misconception 3. A steeper graph always means a larger change

The visual steepness depends on the axis scales and aspect ratio. Read the axis values as well when assessing numerical changes.

### Misconception 4. A curved function graph means a curved input space

The curved shape of a function graph represents the input-output relation. Curvature of a space is defined separately after specifying a distance structure.

### Misconception 5. A falling loss curve means that every aspect of model performance improves

The graph provides information only about the displayed loss and data split. Other evaluation metrics, validation data, and external data require separate checks.

## Exercises

### 1. Read coordinates

Write the horizontal and vertical coordinates of $A=(-3,2)$ and $B=(2,-3)$, and determine whether the points are the same.

<details>
<summary>Show solution</summary>

The horizontal coordinate of $A$ is $-3$, and its vertical coordinate is $2$. The horizontal coordinate of $B$ is $2$, and its vertical coordinate is $-3$.

Ordered pairs preserve order, so

\[
(-3,2)\ne(2,-3)
\]

The two points differ.

</details>

### 2. Obtain points from a function table

If

\[
f(x)=x+2
\]

and $x=-2,0,3$, calculate the function values and the points to plot on the graph.

<details>
<summary>Show solution</summary>

\[
f(-2)=-2+2=0,\qquad f(0)=2,\qquad f(3)=5
\]

The points to plot are

\[
(-2,0),\qquad (0,2),\qquad (3,5)
\]

</details>

### 3. Interpret function values from a graph

The graph of a function $h$ passes through $(-1,4)$, $(0,2)$, and $(2,-2)$. Calculate $h(-1)$, $h(0)$, and $h(2)$.

<details>
<summary>Show solution</summary>

Points on a function graph have the form $(x,h(x))$. Therefore,

\[
h(-1)=4,\qquad h(0)=2,\qquad h(2)=-2
\]

</details>

### 4. Calculate intercepts

Calculate the $x$-intercept and $y$-intercept of

\[
y=-2x+4
\]

<details>
<summary>Show solution</summary>

To find the $y$-intercept, substitute $x=0$.

\[
y=-2\cdot0+4=4
\]

The $y$-intercept is $4$, and the point is $(0,4)$.

To find the $x$-intercept, set $y=0$.

\[
0=-2x+4
\]

Subtracting $4$ from both sides gives $-4=-2x$; dividing both sides by $-2$ gives $x=2$. The $x$-intercept is $2$, and the point is $(2,0)$.

</details>

### 5. Assess connected points

An experiment measured accuracy at batch sizes $16,32,64$. The researcher connected the three points with lines. Determine whether the accuracy on the line at batch size $40$ can be called a directly observed value.

<details>
<summary>Show solution</summary>

It cannot. The researcher measured accuracy only at batch sizes $16,32,64$. The value on the line at $40$ is an interpolated value produced by the way the points were connected.

A claim about accuracy at batch size $40$ requires either a direct measurement under that condition or a separate justification of the interpolation model and its error.

</details>

### 6. Critique axis scales

Two graphs show the same data. The first has a vertical-axis range from $0$ to $100$, and the second from $88$ to $92$. Explain why a change from $89$ to $91$ looks larger in the second graph, and state the actual change.

<details>
<summary>Show solution</summary>

The second graph uses a narrower vertical-axis range, so the same numerical difference occupies a greater visual distance. The actual change is

\[
91-89=2
\]

To assess a ratio or its importance, read the axis range and units as well as the graph's shape.

</details>

### 7. Assess a model interpretability claim

An activation plotted against input magnitude gives a curved graph. A researcher concludes, "The activation space has curvature." Explain what information this conclusion lacks.

<details>
<summary>Show solution</summary>

The curve may show that the relation between the selected input and activation value is nonlinear. This alone cannot define or calculate curvature in the activation space.

A claim about curvature requires specifying the points of the space, its distance or inner-product structure, its coordinate system, and the definition of curvature. The researcher must also report the curvature calculated under that structure and a reference for comparison.

</details>

## Lesson summary

- In an ordered pair $(x,y)$, the first value is the horizontal coordinate, and the second is the vertical coordinate.
- A function graph is the collection of points $(x,f(x))$ for each $x$ in the domain.
- Find the $y$-intercept from $f(0)$ and the $x$-intercept by solving $f(x)=0$.
- Connecting discrete observations does not turn unmeasured values into directly observed ones.
- A curved function graph and curvature of a space are different mathematical claims.

## Pass criteria

You pass if you can answer these questions without consulting the lesson.

- Can you explain the role of each value in $(x,y)$?
- Can you turn a function table into points of the form $(x,f(x))$?
- Can you read function values and intercepts from a graph?
- Can you explain the assumptions introduced when connecting discrete data points?
- Can you explain why a curved graph alone cannot establish curvature in a space?

## Next lesson

The next lesson is [M00-05 Exponents and logarithms](M00-05-exponents-logarithms.md). It represents repeated multiplication with exponents and introduces the inverse relationship between exponential and logarithmic functions.

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Every new symbol is defined before use.
- [x] Ordered pairs and function graphs are distinguished.
- [x] Function values and intercepts in the examples have been checked.
- [x] Every exercise has a solution.
- [x] Graph observations and causal claims are distinguished.
- [x] Claims about curvature of a space are limited to their stated scope.
- [x] Terminology and notation follow the glossary and style rules.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
