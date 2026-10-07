---
id: "M02-01"
title: "Vectors and vector operations"
part: 1
stage: "M02"
status: "complete"
prerequisites:
  - "M00-04"
  - "M00-09"
estimated_time: "90~110 minutes"
---

# M02-01. Vectors and vector operations

## Why this lesson matters

Neural networks handle inputs, parameters, and intermediate activations as collections of numbers. Viewing these collections as vectors connects componentwise calculations with interpretations of the overall direction. Adding two representations in a residual connection or multiplying a gradient by a learning rate also uses basic vector operations.

This lesson develops vector addition and scalar multiplication through both coordinate calculations and movements represented by arrows. We study length, angles, and inner products in M02-03.

## Learning objectives

After completing this lesson, you will be able to:

- Distinguish a vector, its components, and its dimension.
- Add and subtract vectors of the same dimension componentwise.
- Explain how scalar multiplication affects a vector's direction and magnitude.
- Check the roles of the zero vector and additive inverse through calculations.
- Identify the shape conditions and scope of interpretation for vector addition in a neural network.

## Prerequisite check

- Prerequisite lesson: [M00-04 Coordinates and graphs](../M00/M00-04-coordinates-graphs.md)
- Prerequisite lesson: [M00-09 Shapes of scalars, vectors, and matrices](../M00/M00-09-scalars-vectors-matrices-shape.md)
- Check question: Can you state the two coordinates of $(2,-1)$ in order?
- Check question: Can you explain why arrays of shapes $(3,)$ and $(4,)$ cannot be added componentwise?

If coordinates and shapes are unclear, first review the prerequisite lessons.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $\mathbf v$ | `v` | Vector | Mainly $\mathbf v\in\mathbb R^n$ in this lesson |
| $v_i$ | `v sub i` | The $i$th component of $\mathbf v$ | $v_i\in\mathbb R$ |
| $n$ | `n` | Dimension of a vector | Positive integer |
| $\mathbf 0$ | `the zero vector` | Vector whose components are all 0 | Dimension appropriate to the context |
| $\alpha$ | `alpha` | Scalar multiplying a vector | $\alpha\in\mathbb R$ |
| $-\mathbf v$ | `minus v` | Additive inverse of $\mathbf v$ | Same dimension as $\mathbf v$ |

## Core concept 1. A vector is represented by ordered components

A vector with $n$ real components can be written as the column vector

\[
\mathbf v
=
\begin{bmatrix}
v_1\\
v_2\\
\vdots\\
v_n
\end{bmatrix}
\in\mathbb R^n
\]

Here, $v_i$ is the $i$th component, and $n$ is the dimension. Component order distinguishes their roles. For example, $\begin{bmatrix}2\\5\end{bmatrix}$ and $\begin{bmatrix}5\\2\end{bmatrix}$ are generally different vectors.

Coordinates are a list of numbers representing a vector. In M02-07 and M03-03, we will see that changing the basis can give different coordinates for the same vector. For now, we use standard coordinates.

In the figure below, associate the first component with the horizontal axis and the second with the vertical axis to see how reversing the components changes the movement.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two vectors with reversed component order reach different endpoints on the same coordinate grid](../../figures/assets/M02/M02-01-ordered-components.svg)

<figcaption>Both vectors have dimension 2, but (2,5)ᵀ and (5,2)ᵀ have different movements along each axis and reach different endpoints. The dotted lines connect each axis with the corresponding column-vector component.</figcaption>
</figure>

## Core concept 2. Vector equality compares corresponding components

The equation

\[
\mathbf u=\mathbf v
\]

means that the two vectors have the same dimension and satisfy $u_i=v_i$ for every $i$. If even one component differs, the vectors differ.

\[
\begin{bmatrix}1\\-2\\3\end{bmatrix}
\ne
\begin{bmatrix}1\\-2\\4\end{bmatrix}
\]

because their final components differ.

The figure below compares components in matching rows. Even though the first two components agree, the final comparison shows that the vectors are not equal.

<figure class="lesson-figure" markdown="1">

![Corresponding components match in the first two rows but differ in the third row of two column vectors](../../figures/assets/M02/M02-01-component-equality.svg)

<figcaption>First check that the dimensions agree, then compare every corresponding component. The third-component difference 3≠4 determines that the vectors differ.</figcaption>
</figure>

## Core concept 3. Calculate vector addition and subtraction componentwise

For $\mathbf u,\mathbf v\in\mathbb R^n$,

\[
\mathbf u+\mathbf v
=
\begin{bmatrix}
u_1+v_1\\
u_2+v_2\\
\vdots\\
u_n+v_n
\end{bmatrix}
\]

The dimensions must agree so that corresponding components can be identified.

Subtraction adds the additive inverse.

\[
\mathbf u-\mathbf v
=
\mathbf u+(-\mathbf v)
\]

Here, $-\mathbf v$ reverses every component's sign.

If the two vectors are arrows starting at the same origin, $\mathbf u-\mathbf v$ is the displacement from the tip of $\mathbf v$ to the tip of $\mathbf u$. Since $\mathbf v+(\mathbf u-\mathbf v)=\mathbf u$, adding this difference to the current position vector $\mathbf v$ reaches the target position vector $\mathbf u$. Reversing the subtraction order reverses the movement's direction.

The two scenes below show the difference vector in Example 1. On the left, move from the tip of $\mathbf v$ to the tip of $\mathbf u$. On the right, follow $\mathbf u$ from the origin, then attach $-\mathbf v$ to its tip.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The difference from the tip of v to the tip of u equals the vector obtained by adding minus v after u](../../figures/assets/M02/M02-01-vector-difference.svg)

<figcaption>(2,-1)ᵀ−(-3,4)ᵀ=(5,-5)ᵀ. The green arrow on the left does not start at the origin, but it represents the same displacement (5,-5)ᵀ as the green arrow on the right.</figcaption>
</figure>

## Core concept 4. Addition joins movements head to tail

Represent vectors in $\mathbb R^2$ as arrows. Moving by $\mathbf v$ from the tip of $\mathbf u$ gives the total movement $\mathbf u+\mathbf v$. If both arrows start at the same point, the diagonal of their parallelogram is the sum vector.

Moving the second arrow in the drawing does not change the components of $\mathbf v$. Components are coordinate changes from the tail to the tip, not the tip's absolute position. Joining $\mathbf u=(2,-1)^\top$ and $\mathbf v=(-3,4)^\top$ from Example 1 first moves from the origin to $(2,-1)$. Decreasing the first coordinate by 3 and increasing the second by 4 then reaches $(-1,3)$. Componentwise addition and the composition of movements describe the same result.

The purple dashed arrows below are translated to the other arrows' tips. Both orders of movement reach the same parallelogram vertex, and the green diagonal shows the total movement.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Translated copies of u and v form a parallelogram whose diagonal reaches their sum minus one three](../../figures/assets/M02/M02-01-vector-addition.svg)

<figcaption>Whether v follows u or u follows v, the sum ends at (-1,3). A translated arrow changes position but keeps its components.</figcaption>
</figure>

Vector addition satisfies the following laws.

\[
\mathbf u+\mathbf v=\mathbf v+\mathbf u
\]

\[
(\mathbf u+\mathbf v)+\mathbf w
=
\mathbf u+(\mathbf v+\mathbf w)
\]

The first equation says that reversing the addition order leaves the final movement unchanged. The second says that regrouping three movements does not change the result.

## Core concept 5. Scalar multiplication applies the same number to every component

For $\alpha\in\mathbb R$ and $\mathbf v\in\mathbb R^n$,

\[
\alpha\mathbf v
=
\begin{bmatrix}
\alpha v_1\\
\alpha v_2\\
\vdots\\
\alpha v_n
\end{bmatrix}
\]

The following descriptions of direction apply when $\mathbf v\ne\mathbf 0$.

- If $\alpha>1$, the vector grows in the same direction.
- If $0<\alpha<1$, it shrinks in the same direction.
- If $\alpha<0$, its direction reverses, and it grows or shrinks according to $|\alpha|$.
- If $\alpha=0$, it becomes the zero vector.

For $\alpha=1$, the vector stays unchanged. Multiplying every component by the same number changes the overall magnitude while preserving the proportions of movements along the coordinates. For example, multiplying $(1,-2)^\top$ by 3 triples both components to give $(3,-6)^\top$. Changing just one component can also change direction, unlike this scalar multiplication.

Scalar multiplication here is a scalar times a vector. Distinguish it from an inner product, which maps two vectors to a scalar.

The figure below uses the same coordinate scale to compare $\mathbf v=(1,-2)^\top$ with four scalar multiples. Comparing the gray dashed arrows with the results shows what the multiplier's magnitude and sign each change.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Four equally scaled grids compare positive enlargement, positive shrinkage, negative reversal and the zero scalar applied to one vector](../../figures/assets/M02/M02-01-scalar-multiplication.svg)

<figcaption>3v is three times as large in the same direction, and (1/2)v is half as large in the same direction. −(1/2)v is half as large in the opposite direction; 0v is the zero vector with no direction.</figcaption>
</figure>

## Core concept 6. The zero vector and additive inverse undo movement

The zero vector is

\[
\mathbf 0
=
\begin{bmatrix}
0\\
\vdots\\
0
\end{bmatrix}
\]

For every $\mathbf v\in\mathbb R^n$, it satisfies

\[
\mathbf v+\mathbf 0=\mathbf v
\]

If $\mathbf v$ is nonzero, $-\mathbf v$ points in the opposite direction to $\mathbf v$, and

\[
\mathbf v+(-\mathbf v)=\mathbf 0
\]

This is like returning to the starting position by following one movement with its exact opposite.

The zero vector represents a movement of 0, so it has no direction. Multiplying it by any scalar leaves every component 0, and it is its own additive inverse.

In the figure below, following the blue movement and returning along the same segment in the purple dashed arrow's direction reaches the starting point. Adding the zero vector involves no movement that changes this starting or ending position.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A solid outward vector and its dashed additive inverse follow the same segment in opposite directions and give zero net displacement](../../figures/assets/M02/M02-01-zero-and-inverse.svg)

<figcaption>v+(−v)=0 means that the total displacement after the round trip is the zero vector. In v+0=v, no extra movement is added, leaving the original vector unchanged.</figcaption>
</figure>

## Core concept 7. Addition and scalar multiplication obey distributive laws

Vector operations satisfy

\[
\alpha(\mathbf u+\mathbf v)
=
\alpha\mathbf u+\alpha\mathbf v
\]

\[
(\alpha+\beta)\mathbf v
=
\alpha\mathbf v+\beta\mathbf v
\]

The $i$th component of the first equation is $\alpha(u_i+v_i)$ on the left and $\alpha u_i+\alpha v_i$ on the right. The real-number distributive law makes them equal. In the second equation, matching $i$th components agree as $(\alpha+\beta)v_i=\alpha v_i+\beta v_i$. Every corresponding component agrees, so the vector equalities hold. These laws let us consistently calculate linear combinations that multiply multiple vectors by coefficients and add them.

The figure below compares the two calculation orders in Exercise 5 using coordinates. Doubling the sum and doubling each vector before joining them give the same final displacement.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Doubling the sum and joining the doubled vectors both reach the endpoint eight two on matched coordinate grids](../../figures/assets/M02/M02-01-distributive-scaling.svg)

<figcaption>The left doubles (4,1)ᵀ to obtain (8,2)ᵀ. The right joins (2,4)ᵀ and (6,-2)ᵀ to reach the same endpoint.</figcaption>
</figure>

## Example 1. Vector addition and subtraction

Let

\[
\mathbf u=
\begin{bmatrix}2\\-1\end{bmatrix},
\qquad
\mathbf v=
\begin{bmatrix}-3\\4\end{bmatrix}
\]

Then

\[
\mathbf u+\mathbf v
=
\begin{bmatrix}
2+(-3)\\
-1+4
\end{bmatrix}
=
\begin{bmatrix}-1\\3\end{bmatrix}
\]

and

\[
\mathbf u-\mathbf v
=
\begin{bmatrix}
2-(-3)\\
-1-4
\end{bmatrix}
=
\begin{bmatrix}5\\-5\end{bmatrix}
\]

Both results are vectors in $\mathbb R^2$, like the inputs.

## Example 2. Direction under scalar multiplication

For

\[
\mathbf v=
\begin{bmatrix}1\\-2\end{bmatrix}
\]

the vector

\[
3\mathbf v
=
\begin{bmatrix}3\\-6\end{bmatrix}
\]

is three times as large in the same direction.

\[
-\frac12\mathbf v
=
\begin{bmatrix}-\frac12\\1\end{bmatrix}
\]

is half as large in the opposite direction. We learn exact length calculations in M02-03.

## Example 3. Points and displacement vectors

The displacement vector from point $P=(1,2)$ to point $Q=(4,-1)$ subtracts the start from the endpoint.

\[
\overrightarrow{PQ}
=
\begin{bmatrix}
4-1\\
-1-2
\end{bmatrix}
=
\begin{bmatrix}3\\-3\end{bmatrix}
\]

A point describes a position; a vector describes a movement. In standard coordinates, both can be written as ordered pairs of numbers, but their roles differ.

The blue points below are positions $P,Q$, and the green arrow is their displacement. Reading each coordinate change along the purple dashed lines verifies the difference between endpoint and start.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An arrow from P at one two to Q at four minus one has displacement three minus three with horizontal and vertical changes marked](../../figures/assets/M02/M02-01-point-displacement.svg)

<figcaption>Moving from P to Q increases the first coordinate by 3 and decreases the second by 3. Distinguish displacement (3,-3)ᵀ from the coordinates of P and Q.</figcaption>
</figure>

## Example 4. Vector addition in a residual connection

If a token's residual stream vector is $\mathbf h\in\mathbb R^d$ and a sublayer output is $\mathbf r\in\mathbb R^d$, write the residual connection as

\[
\mathbf h_{\mathrm{new}}
=
\mathbf h+\mathbf r
\]

The dimensions must agree to add the vectors in corresponding coordinates.

This equation alone does not reveal the meaning of each component or whether $\mathbf r$ causally produces behavior. It establishes the addition structure and shape condition.

## Common misconceptions

### Misconception 1. A vector is the arrow drawing itself

An arrow visualizes a vector in $\mathbb R^2$ or $\mathbb R^3$. Neural network vectors can have much higher dimensions and obey the same operation laws without drawings.

### Misconception 2. Equal component counts justify adding vectors with different meanings

Equal dimensions make the operation formally possible. For objects with different coordinate roles or units, such as temperature vectors and position vectors, a meaningful sum requires a separate definition.

### Misconception 3. A point and a vector are the same object

Even if their coordinate notation looks the same, a point is a position and a vector is a displacement. Choosing an origin associates a point with a position vector, but omitting that choice creates confusion.

### Misconception 4. Scalar multiplication is an inner product

The operation $\alpha\mathbf v$ takes a scalar and a vector and produces a vector. The inner product $\mathbf u^\top\mathbf v$ takes two vectors and produces a scalar.

## Exercises

### 1. Read notation

Read

\[
\mathbf v=
\begin{bmatrix}v_1\\v_2\\v_3\end{bmatrix}
\in\mathbb R^3
\]

symbol by symbol and state the dimension of $\mathbf v$.

<details>
<summary>Show solution</summary>

$\mathbf v$ is a column vector with three ordered real components $v_1,v_2,v_3$. It belongs to $\mathbb R^3$, so its dimension is 3.

</details>

### 2. Addition and subtraction

For

\[
\mathbf u=
\begin{bmatrix}4\\-2\\1\end{bmatrix},
\qquad
\mathbf v=
\begin{bmatrix}-1\\3\\5\end{bmatrix}
\]

find $\mathbf u+\mathbf v$ and $\mathbf u-\mathbf v$.

<details>
<summary>Show solution</summary>

Calculating with corresponding components gives

\[
\mathbf u+\mathbf v
=
\begin{bmatrix}3\\1\\6\end{bmatrix}
\]

and

\[
\mathbf u-\mathbf v
=
\begin{bmatrix}5\\-5\\-4\end{bmatrix}
\]

</details>

### 3. Scalar multiplication

For

\[
\mathbf v=
\begin{bmatrix}2\\-4\end{bmatrix}
\]

find $0\mathbf v$, $\frac12\mathbf v$, and $-2\mathbf v$, and explain their changes in direction.

<details>
<summary>Show solution</summary>

\[
0\mathbf v=\begin{bmatrix}0\\0\end{bmatrix},
\qquad
\frac12\mathbf v=\begin{bmatrix}1\\-2\end{bmatrix},
\qquad
-2\mathbf v=\begin{bmatrix}-4\\8\end{bmatrix}
\]

The vector $\frac12\mathbf v$ shrinks in the same direction, and $-2\mathbf v$ doubles in magnitude in the opposite direction.

</details>

### 4. Is the operation defined?

Determine whether the following addition is defined and explain why.

\[
\begin{bmatrix}1\\2\end{bmatrix}
+
\begin{bmatrix}3\\4\\5\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

The first vector belongs to $\mathbb R^2$, and the second to $\mathbb R^3$. Their different dimensions prevent assigning all corresponding components, so this vector addition is undefined.

</details>

### 5. Check the distributive law

For

\[
\mathbf u=
\begin{bmatrix}1\\2\end{bmatrix},
\qquad
\mathbf v=
\begin{bmatrix}3\\-1\end{bmatrix}
\]

calculate $2(\mathbf u+\mathbf v)$ and $2\mathbf u+2\mathbf v$ separately.

<details>
<summary>Show solution</summary>

Since

\[
\mathbf u+\mathbf v
=
\begin{bmatrix}4\\1\end{bmatrix}
\]

we have

\[
2(\mathbf u+\mathbf v)
=
\begin{bmatrix}8\\2\end{bmatrix}
\]

Meanwhile,

\[
2\mathbf u+2\mathbf v
=
\begin{bmatrix}2\\4\end{bmatrix}
+
\begin{bmatrix}6\\-2\end{bmatrix}
=
\begin{bmatrix}8\\2\end{bmatrix}
\]

The identical results verify the distributive law.

</details>

### 6. A displacement vector

Find the displacement vector $\overrightarrow{AB}$ from $A=(-2,1)$ to $B=(3,4)$. Then find its sum with the reverse displacement $\overrightarrow{BA}$.

<details>
<summary>Show solution</summary>

\[
\overrightarrow{AB}
=
\begin{bmatrix}
3-(-2)\\
4-1
\end{bmatrix}
=
\begin{bmatrix}5\\3\end{bmatrix}
\]

and

\[
\overrightarrow{BA}
=
\begin{bmatrix}-5\\-3\end{bmatrix}
=
-\overrightarrow{AB}
\]

Their sum is therefore the zero vector.

</details>

### 7. A model connection and the scope of claims

Let $\mathbf h,\mathbf r\in\mathbb R^{768}$ and $\mathbf h_{\mathrm{new}}=\mathbf h+\mathbf r$.

1. What is the output dimension?
2. Does observing that the 10th component of $\mathbf r$ is positive establish that the 10th coordinate causally handles a particular concept?

<details>
<summary>Show solution</summary>

Adding corresponding components gives $\mathbf h_{\mathrm{new}}\in\mathbb R^{768}$.

The second conclusion does not follow. A component's sign is an observation in a selected coordinate system. Its relationship to a particular concept, stability across inputs, and actual use by the model require separate analyses and interventions.

</details>

## Lesson summary

- A vector in $\mathbb R^n$ is represented by $n$ ordered real components.
- Vectors of equal dimension are added and subtracted componentwise.
- Scalar multiplication applies the same scalar to every component; its sign can reverse direction.
- The zero vector leaves addition unchanged, and the additive inverse undoes the original movement.
- Equal shapes establish that an operation is possible, not its meaning or causal role.

## Pass criteria

You pass if you can answer these questions without consulting the material:

- Can you distinguish a vector's components from its dimension?
- Can you calculate the sum and difference of two vectors componentwise?
- Can you explain scalar multiplication by positive, zero, and negative values geometrically?
- Can you explain the roles of the zero vector and additive inverse?
- Can you distinguish what equal shapes establish from what they do not?

## Next lesson

- [M02-02 Linear combinations and span](M02-02-linear-combinations-span.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Every new symbol is defined before use.
- [x] Vectors follow the column-vector notation rule.
- [x] Coordinate calculations are connected to geometric movements.
- [x] Example calculations have been checked.
- [x] Every exercise has a solution.
- [x] Shape conditions are distinguished from semantic interpretations.
- [x] The glossary and notation rules are followed.
- [x] No inner product or norm calculations beyond the prerequisites are required.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
