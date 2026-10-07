---
id: "M03-13"
title: "JVPs and VJPs"
part: 1
stage: "M03"
status: "complete"
prerequisites:
  - "M03-07"
  - "M03-11"
  - "M03-12"
estimated_time: "120–145 minutes"
---

# M03-13. JVPs and VJPs

## Why this lesson matters

For functions with large input and output dimensions, storing the full Jacobian is difficult. Many calculations need only a product of the Jacobian and a vector, rather than the Jacobian itself. A JVP asks how a change along an input direction propagates to the output. A VJP asks how a scalar measurement of the output is pulled back to the input.

Forward-mode automatic differentiation propagates JVPs in the direction of the computation graph. Reverse-mode automatic differentiation and backpropagation propagate VJPs in the opposite direction. Distinguishing the types and shapes of the two operations lets us read automatic differentiation APIs and gradient calculations through the same chain rule.

## Learning objectives

After this lesson, you will be able to:

- Explain the formulas, input types, and output shapes of JVPs and VJPs.
- Calculate JVPs and VJPs from a given Jacobian.
- Check consistency between the calculations using the adjoint identity.
- Trace the forward order of JVPs and reverse order of VJPs in composed functions.
- Calculate a scalar-output gradient using a VJP.
- Compare when to use forward mode and reverse mode according to input and output dimensions.
- Limit the scope of local claims supported by JVP and VJP results.

## Prerequisite check

- Prerequisite: [M03-07 Dual spaces and covectors](M03-07-dual-spaces-covectors.md)
- Prerequisite: [M03-11 Jacobian](M03-11-jacobian.md)
- Prerequisite: [M03-12 Hessian](M03-12-hessian.md)
- Check: Can you explain the Jacobian's output-row, input-column convention and shape?
- Check: Can you explain what it means for a covector to act on a vector to produce a scalar?
- Check: Can you calculate a Hessian-vector product?

If Jacobians or covectors are unclear, review the prerequisite lessons first.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape |
|---|---|---|---|
| $\mathbf J_f(\mathbf x)$ | `the Jacobian of f at x` | The matrix of the total derivative at $\mathbf x$ | $m\times n$ |
| $\mathbf v$ | `v` | A tangent direction in input space | $n\times1$ |
| $\mathbf J_f(\mathbf x)\mathbf v$ | `the Jacobian of f at x times v` | Jacobian-vector product | $m\times1$ |
| $\mathbf u$ | `u` | A column representation of a covector defining a scalar measurement in output space | $m\times1$ |
| $\mathbf J_f(\mathbf x)^\top\mathbf u$ | `the Jacobian of f at x transpose times u` | The column representation of a vector-Jacobian product | $n\times1$ |
| tangent | `tangent` | A first-order change propagated by forward mode | Vector |
| cotangent | `cotangent` | A covector propagated by reverse mode | May be stored as column coordinates |

Some frameworks write a VJP as the row covector $\mathbf u^\top\mathbf J_f$. This textbook uses its transpose, $\mathbf J_f^\top\mathbf u$, to follow the column-vector convention.

## Core concept 1. A JVP sends an input direction to an output direction

For

\[
f:\mathbb R^n\to\mathbb R^m
\]

with Jacobian

\[
\mathbf J_f(\mathbf x)\in\mathbb R^{m\times n}
\]

the JVP for input direction $\mathbf v\in\mathbb R^n$ is

\[
\operatorname{JVP}_f(\mathbf x;\mathbf v)
=
\mathbf J_f(\mathbf x)\mathbf v
\in\mathbb R^m
\]

Supplying the curve

\[
\mathbf x(t)=\mathbf x+t\mathbf v
\]

to the function gives

\[
\left.
\frac{d}{dt}
f(\mathbf x+t\mathbf v)
\right|_{t=0}
=
\mathbf J_f(\mathbf x)\mathbf v
\]

A JVP pushes the input tangent $\mathbf v$ forward to an output tangent.

The Jacobian in Example 1 maps two input-direction coefficients to three output-change coefficients.

<figure class="lesson-figure" markdown="1">

![Two component input tangent three minus one maps through a three by two Jacobian to output tangent five five four](../../figures/assets/M03/M03-13-jvp-direction-map.svg)

<figcaption>The input and output directions belong to different spaces and have different numbers of components. Jv=(5,5,4)ᵀ is the output rate of change at the specified input point.</figcaption>

</figure>

## Core concept 2. A VJP pulls an output covector back to the input

Let a covector measure an output change $\Delta\mathbf y\in\mathbb R^m$ as the scalar

\[
\mathbf u^\top\Delta\mathbf y
\]

Locally,

\[
\Delta\mathbf y
\approx
\mathbf J_f(\mathbf x)\Delta\mathbf x
\]

so

\[
\mathbf u^\top\Delta\mathbf y
\approx
\mathbf u^\top
\mathbf J_f(\mathbf x)
\Delta\mathbf x
\]

The column coordinates of the covector acting on input changes are

\[
\operatorname{VJP}_f(\mathbf x;\mathbf u)
=
\mathbf J_f(\mathbf x)^\top\mathbf u
\in\mathbb R^n
\]

A VJP pulls a covector in output space back to a covector in input space. In Euclidean coordinates, storing its coefficients as a column makes it look like a vector, but its transformation role is that of a covector.

Fixing output measurement $\mathbf u$, the coefficient attached to input coordinate $j$ is $\sum_{i=1}^m u_iJ_{ij}$. It collects the rates $J_{ij}$ at which one input coordinate changes each output, weighted by output-measurement coefficients $u_i$. Stacking these coefficients as a column gives $\mathbf J_f^\top\mathbf u$. This differs from using $\mathbf u$ as an actual output displacement.

We can also read the same relationship as function composition. Appending the fixed linear measurement $s(\mathbf y)=\mathbf u^\top\mathbf y$ after $f$ gives the scalar function $s\circ f$, whose differential is $d(s\circ f)_{\mathbf x}(\mathbf v)=\mathbf u^\top\mathbf J_f(\mathbf x)\mathbf v$. Thus, the scalar function's standard Euclidean gradient equals the VJP's column representation. Pullback means composing a measurement, not finding the inverse of $f$.

A VJP moves the rule that measures output changes back to the input, rather than moving a direction vector.

<figure class="lesson-figure" markdown="1">

![Three component output measurement one minus two three pulls back through the transpose Jacobian to input measurement one minus four](../../figures/assets/M03/M03-13-vjp-measurement-map.svg)

<figcaption>The three coefficients of output measurement u weight the respective output changes. The VJP result (1,−4)ᵀ gives measurement coefficients to apply to input changes; it does not recover the original input values.</figcaption>

</figure>

## Core concept 3. The adjoint identity connects the two products through the same scalar

JVPs and VJPs satisfy

\[
\mathbf u^\top
\left(
\mathbf J_f\mathbf v
\right)
=
\left(
\mathbf J_f^\top\mathbf u
\right)^\top
\mathbf v
\]

The transpose rule gives $(\mathbf J_f^\top\mathbf u)^\top=\mathbf u^\top\mathbf J_f$, and associativity of matrix multiplication lets us change where the products are grouped. Together, these two rules give the identity. The Jacobian need not be square or invertible.

The left side sends the input direction to the output and then measures it with $\mathbf u$. The right side pulls $\mathbf u$ back to the input and applies it to $\mathbf v$. Both paths produce the same scalar.

This identity can check hand calculations or implementation results. If the values differ, a transpose, axis, or multiplication order may be wrong.

Comparing both calculations in Example 1 shows that measuring in either space gives the same scalar, 7.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Input tangent pushes forward on the top route and output measurement pulls back on the middle route with both final pairings equal to seven](../../figures/assets/M03/M03-13-adjoint-two-routes.svg)

<figcaption>On the right, u measures output change (5,5,4); on the left, the pulled-back measurement (1,−4) measures input change (3,−1). The adjoint identity ensures that moving the covector preserves the scalar being measured.</figcaption>

</figure>

## Core concept 4. JVPs of composed functions flow in forward order

For

\[
f:\mathbb R^n\to\mathbb R^m,
\qquad
g:\mathbb R^m\to\mathbb R^p
\]

we have

\[
\mathbf J_{g\circ f}(\mathbf x)
=
\mathbf J_g(f(\mathbf x))
\mathbf J_f(\mathbf x)
\]

The JVP for input tangent $\mathbf v$ is calculated in the order

\[
\mathbf v
\longmapsto
\mathbf J_f(\mathbf x)\mathbf v
\longmapsto
\mathbf J_g(f(\mathbf x))
\left(
\mathbf J_f(\mathbf x)\mathbf v
\right)
\]

Each operation sends its current value and tangent together to the next node. This is the structure of forward-mode automatic differentiation.

We must first calculate $f(\mathbf x)$ to determine where to evaluate the Jacobian of $g$. The tangent $\mathbf J_f(\mathbf x)\mathbf v$ is a rate of change around that intermediate value, not the value itself. Forward mode therefore maintains both the path that calculates function values and the path that propagates derivatives evaluated at those values. The tangent spaces follow the sequence $\mathbb R^n\to\mathbb R^m\to\mathbb R^p$.

## Core concept 5. VJPs of composed functions flow in reverse order

Starting with output cotangent $\mathbf u\in\mathbb R^p$ gives

\[
\mathbf J_{g\circ f}(\mathbf x)^\top\mathbf u
=
\mathbf J_f(\mathbf x)^\top
\mathbf J_g(f(\mathbf x))^\top
\mathbf u
\]

The calculation order is

\[
\mathbf u
\longmapsto
\mathbf J_g^\top\mathbf u
\longmapsto
\mathbf J_f^\top
\left(
\mathbf J_g^\top\mathbf u
\right)
\]

If the forward pass applies $f$ and then $g$, the reverse pass applies the local VJP of $g$ and then the local VJP of $f$.

Transposing the composite Jacobian product reverses its order: $(\mathbf J_g\mathbf J_f)^\top=\mathbf J_f^\top\mathbf J_g^\top$. Since the right matrix acts first on a column seed, we first pull the measurement through $g$ to the output space of $f$, then through $f$ to the original input space. The cotangent spaces follow $\mathbb R^p\to\mathbb R^m\to\mathbb R^n$. This does not recover original input values, so neither function needs to be invertible.

## Core concept 6. One VJP gives the gradient of a scalar output

If $f:\mathbb R^n\to\mathbb R$, the Jacobian has shape $1\times n$. Using scalar 1 as the output-space seed gives

\[
\mathbf J_f(\mathbf x)^\top
\begin{bmatrix}1\end{bmatrix}
=
\nabla f(\mathbf x)
\]

Seed 1 measures the scalar output change unchanged. Multiplying the Jacobian's row coefficients by 1 and placing them in a column gives the derivative coefficients for all input coordinates together. A different scalar seed $a$ gives $a\nabla f(\mathbf x)$, measuring $a$ times the output change. In this equality, the gradient uses the standard Euclidean inner product; the VJP itself calculates the input differential.

In training with many parameters and one loss, a single VJP produces the gradient for all parameters. This is why reverse mode suits neural network training.

If there are multiple outputs and changes along many input directions are needed, we can calculate multiple JVPs. Choose the calculation direction according to whether fewer input directions or output covectors are needed.

## Core concept 7. Products can be calculated without the full Jacobian

To obtain the full Jacobian, we can calculate JVPs in standard input-basis directions $n$ times, or VJPs with standard output-basis seeds $m$ times.

\[
\mathbf J_f\mathbf e_j
\]

is column $j$ of the Jacobian, and

\[
\mathbf J_f^\top\mathbf e_i
\]

is row $i$ written as a column.

If only one direction or the gradient of one scalar loss is needed, we need not construct the full matrix. Automatic differentiation uses local derivatives of the computation graph to calculate the desired product.

The notation $\mathbf J_f\mathbf v$ defines the result; it does not instruct us to first store $\mathbf J_f$ as an array. Feeding the current tangent to each local JVP in a composition gives the final product's $m$ components without the full Jacobian. Local VJPs give the chosen measurement's $n$ input coefficients. Distinguish collecting the full Jacobian's $mn$ entries from calculating one desired product. Storing intermediate values for the reverse pass is a separate requirement, covered in M03-14.

## Example 1. Calculate a JVP and VJP from the same Jacobian

### Problem

Given

\[
\mathbf J=
\begin{bmatrix}
2&1\\
2&1\\
1&-1
\end{bmatrix},
\qquad
\mathbf v=
\begin{bmatrix}
3\\-1
\end{bmatrix},
\qquad
\mathbf u=
\begin{bmatrix}
1\\-2\\3
\end{bmatrix}
\]

calculate the JVP, VJP, and the two scalars in the adjoint identity.

### Solution

The JVP is

\[
\mathbf J\mathbf v
=
\begin{bmatrix}
2&1\\
2&1\\
1&-1
\end{bmatrix}
\begin{bmatrix}
3\\-1
\end{bmatrix}
=
\begin{bmatrix}
5\\5\\4
\end{bmatrix}
\]

The VJP is

\[
\mathbf J^\top\mathbf u
=
\begin{bmatrix}
2&2&1\\
1&1&-1
\end{bmatrix}
\begin{bmatrix}
1\\-2\\3
\end{bmatrix}
=
\begin{bmatrix}
1\\-4
\end{bmatrix}
\]

Measuring on the output side gives

\[
\mathbf u^\top(\mathbf J\mathbf v)
=
1\cdot5+(-2)\cdot5+3\cdot4
=
7
\]

Measuring on the input side gives

\[
(\mathbf J^\top\mathbf u)^\top\mathbf v
=
\begin{bmatrix}
1&-4
\end{bmatrix}
\begin{bmatrix}
3\\-1
\end{bmatrix}
=
7
\]

### What the result means

The JVP and VJP produce vector coordinate arrays in different spaces, but calculate the same bilinear pairing.

## Example 2. Compare propagation directions in a composed function

Suppose the Jacobians of two functions at a point are

\[
\mathbf J_f=
\begin{bmatrix}
1&2\\
0&3
\end{bmatrix},
\qquad
\mathbf J_g=
\begin{bmatrix}
4&-1
\end{bmatrix}
\]

Propagating input tangent

\[
\mathbf v=
\begin{bmatrix}
2\\-1
\end{bmatrix}
\]

forward gives

\[
\mathbf J_f\mathbf v
=
\begin{bmatrix}
0\\-3
\end{bmatrix}
\]

and

\[
\mathbf J_g
\begin{bmatrix}
0\\-3
\end{bmatrix}
=
3
\]

Reverse propagation starts with output seed 1:

\[
\mathbf J_g^\top
\begin{bmatrix}1\end{bmatrix}
=
\begin{bmatrix}
4\\-1
\end{bmatrix}
\]

\[
\mathbf J_f^\top
\begin{bmatrix}
4\\-1
\end{bmatrix}
=
\begin{bmatrix}
4\\5
\end{bmatrix}
\]

The inner product of the input gradient and direction is

\[
\begin{bmatrix}
4&5
\end{bmatrix}
\begin{bmatrix}
2\\-1
\end{bmatrix}
=
3
\]

matching the forward directional derivative.

Forward and reverse propagation in Example 2 use the same local Jacobians with different orders and types.

<figure class="lesson-figure" markdown="1">

![Input tangent two minus one moves first through inner Jacobian to zero minus three then through outer Jacobian to scalar three](../../figures/assets/M03/M03-13-forward-chain.svg)

<figcaption>The forward path propagates one input direction to an intermediate direction and then a final direction. An intermediate tangent of (0,−3) does not mean that the intermediate function value is that vector.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Scalar output seed one pulls back first to middle covector four minus one and then to input gradient four five](../../figures/assets/M03/M03-13-reverse-chain.svg)

<figcaption>The reverse path starts with scalar output seed 1 and obtains gradients for both input coordinates together. Measuring this gradient along the original direction (2,−1) gives 3, the same as the forward result.</figcaption>

</figure>

## Example 3. The VJP of a linear readout

Calculating

\[
s(\mathbf h)=\mathbf w^\top\mathbf h+b
\]

from activation $\mathbf h\in\mathbb R^d$ gives

\[
\mathbf J_s(\mathbf h)=\mathbf w^\top
\]

The VJP with output seed $u=1$ is

\[
\mathbf J_s(\mathbf h)^\top u
=
\mathbf w
\]

This is why the activation gradient of the output score is $\mathbf w$.

The column $\mathbf w$ gives coordinates of the score differential at this point. Observing the gradient alone does not establish that the model uses this direction as a human-labeled concept.

## Example 4. View a Hessian-vector product as a JVP

For the gradient map of a scalar function $f$,

\[
g(\mathbf x)=\nabla f(\mathbf x)
\]

we have

\[
\mathbf J_g(\mathbf x)=\mathbf H_f(\mathbf x)
\]

Thus,

\[
\operatorname{JVP}_g(\mathbf x;\mathbf v)
=
\mathbf H_f(\mathbf x)\mathbf v
\]

An HVP can be calculated as a JVP of the gradient function.

Reconstructing the full Jacobian requires all standard-basis seeds from one side. Distinguish this reconstruction from a calculation needing only one product.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two input basis seeds select three component Jacobian columns while three output basis seeds select two component Jacobian rows](../../figures/assets/M03/M03-13-jacobian-basis-seeds.svg)

<figcaption>In this 3×2 example, two input basis seeds collect the two columns, or three output basis seeds collect the three rows. If only the product for one tangent or one output measurement is needed, collecting every component this way is unnecessary.</figcaption>

</figure>

## Common misconceptions

### Misconception 1. JVPs and VJPs have the same output, differing only in transpose notation

A JVP sends an input tangent to an output tangent with shape $m$. A VJP sends an output cotangent to an input cotangent with shape $n$.

### Misconception 2. VJP input $\mathbf u$ is an output perturbation

The column $\mathbf u$ gives coordinates of a covector measuring output changes as a scalar. Reverse mode pulls this measurement back to the input.

### Misconception 3. Obtaining a gradient requires constructing the full Jacobian first

For a scalar output, one VJP with seed 1 calculates the input gradient.

### Misconception 4. Forward mode is the forward pass, and reverse mode runs the model backward

The modes refer to the propagation direction of derivative information. Reverse mode also uses original forward values and local derivatives; it does not calculate an inverse of the original function.

## Exercises

### 1. Read shapes

For $f:\mathbb R^5\to\mathbb R^3$, state the shapes of the Jacobian and the inputs and outputs of a JVP and VJP.

<details>
<summary>Show solution</summary>

\[
\mathbf J_f\in\mathbb R^{3\times5}
\]

A JVP takes $\mathbf v\in\mathbb R^5$ and produces $\mathbf J_f\mathbf v\in\mathbb R^3$. A VJP takes $\mathbf u\in\mathbb R^3$ and produces $\mathbf J_f^\top\mathbf u\in\mathbb R^5$.

</details>

### 2. Calculate a JVP

Given

\[
\mathbf J=
\begin{bmatrix}
1&2\\
-1&3
\end{bmatrix},
\qquad
\mathbf v=
\begin{bmatrix}
2\\-1
\end{bmatrix}
\]

calculate the JVP.

<details>
<summary>Show solution</summary>

\[
\mathbf J\mathbf v
=
\begin{bmatrix}
1&2\\
-1&3
\end{bmatrix}
\begin{bmatrix}
2\\-1
\end{bmatrix}
=
\begin{bmatrix}
0\\-5
\end{bmatrix}
\]

</details>

### 3. Calculate a VJP

Calculate the VJP for $\mathbf J$ from Exercise 2 and

\[
\mathbf u=
\begin{bmatrix}
4\\1
\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

\[
\mathbf J^\top\mathbf u
=
\begin{bmatrix}
1&-1\\
2&3
\end{bmatrix}
\begin{bmatrix}
4\\1
\end{bmatrix}
=
\begin{bmatrix}
3\\11
\end{bmatrix}
\]

</details>

### 4. Adjoint identity

Using the values from Exercises 2 and 3, compare $\mathbf u^\top(\mathbf J\mathbf v)$ and $(\mathbf J^\top\mathbf u)^\top\mathbf v$.

<details>
<summary>Show solution</summary>

\[
\mathbf u^\top(\mathbf J\mathbf v)
=
\begin{bmatrix}
4&1
\end{bmatrix}
\begin{bmatrix}
0\\-5
\end{bmatrix}
=
-5
\]

On the other side,

\[
\begin{bmatrix}
3&11
\end{bmatrix}
\begin{bmatrix}
2\\-1
\end{bmatrix}
=
6-11
=
-5
\]

The two values agree.

</details>

### 5. Scalar gradient

For $f:\mathbb R^4\to\mathbb R$, the Jacobian row is

\[
\mathbf J_f=
\begin{bmatrix}
2&-1&0&3
\end{bmatrix}
\]

Calculate the VJP with seed 1.

<details>
<summary>Show solution</summary>

\[
\mathbf J_f^\top
\begin{bmatrix}1\end{bmatrix}
=
\begin{bmatrix}
2\\-1\\0\\3
\end{bmatrix}
\]

In Euclidean coordinates, this column is $\nabla f$.

</details>

### 6. Composition propagation order

For $h=g\circ f$, state the order in which JVPs and VJPs apply the local Jacobians.

<details>
<summary>Show solution</summary>

The JVP order is

\[
\mathbf v
\longmapsto
\mathbf J_f\mathbf v
\longmapsto
\mathbf J_g(\mathbf J_f\mathbf v)
\]

The VJP starts with output cotangent $\mathbf u$ and follows

\[
\mathbf u
\longmapsto
\mathbf J_g^\top\mathbf u
\longmapsto
\mathbf J_f^\top(\mathbf J_g^\top\mathbf u)
\]

</details>

### 7. Critique a model claim

Critique the statement: “An activation's VJP for the loss is zero, so that activation is unnecessary for the model's computation.”

<details>
<summary>Show solution</summary>

A zero VJP means that a small change to the activation has zero first-order effect on the specified loss at the specified inputs and parameters. Saturation, cancellation, or local flatness can produce zero, while other inputs, outputs, or finite interventions may still reveal effects. A necessity claim requires interventions removing or changing the activation and appropriate controls.

</details>

## Lesson summary

- A JVP sends an input tangent to an output tangent; a VJP pulls an output cotangent back to an input cotangent.
- The adjoint identity shows that JVPs and VJPs calculate the same scalar pairing.
- In composed functions, JVPs propagate local Jacobian products in forward order and VJPs in reverse order.
- A scalar-output gradient is obtained with a VJP using seed 1.
- When only one direction or output measurement is needed, the product can be calculated without constructing the full Jacobian.
- JVPs and VJPs describe local first-order information at a specified point.

## Pass criteria

You pass if you can answer the following without consulting the lesson.

- Can you determine JVP and VJP input/output types and shapes?
- Can you calculate both products for small matrices?
- Can you verify the adjoint identity numerically?
- Can you trace both propagation directions in a composed function?
- Can you produce a scalar gradient using a VJP?
- Can you compare forward and reverse modes according to the number of directions needed?
- Can you limit the claims supported by a zero VJP?

## Next lesson

- [M03-14 Automatic differentiation and backpropagation](M03-14-automatic-differentiation-backpropagation.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] JVP and VJP types and shapes are distinguished.
- [x] The adjoint identity is calculated.
- [x] Forward and reverse orders for composed functions are explained.
- [x] Scalar gradients and HVPs are connected.
- [x] The purpose of calculating without a full Jacobian is stated.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
