---
id: "A09-KER-01"
title: "Function spaces and operators"
part: 4
stage: "A09-KER"
status: "complete"
prerequisites: ["M02-05", "M03-01", "M03-02"]
estimated_time: "90–120 minutes"
---

# A09-KER-01. Function spaces and operators

## Why this lesson matters

Neural network training moves a parameter vector, but researchers interpret the result as a change in the function relating inputs to outputs. Functions can also be added and multiplied by scalars to form vector spaces, and maps acting on functions can be treated as operators. This perspective is the starting point for kernel methods and the neural tangent kernel.

## Learning objectives

- Check the conditions under which a set of functions is a vector space.
- Distinguish linear operators from nonlinear operators.
- Write the inputs and outputs of evaluation operators and integral operators.
- Distinguish parameter-space changes from function-space changes.

## Prerequisite check

- Prerequisite lessons: [M02-05 Matrices as linear transformations](../../part-1-foundations/M02/M02-05-matrix-as-linear-transformation.md), [M03-01 Abstract vector spaces](../../part-1-foundations/M03/M03-01-abstract-vector-spaces.md), [M03-02 Linear maps and matrix representations](../../part-1-foundations/M03/M03-02-linear-maps-matrix-representation.md)
- Check question: If you know only the rules for adding two vectors and multiplying by a scalar, how can you test linearity without choosing coordinates?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\mathcal F$ | `the function space F` | Space of functions with the same domain and codomain | set of functions |
| $T:\mathcal F\to\mathcal G$ | `T maps F to G` | Operator mapping a function to another function or a value | map between spaces |
| $E_x(f)=f(x)$ | `the evaluation operator at x applied to f` | Operator extracting a function's value at a specified input | scalar or vector |
| $\lVert f\rVert_{\mathcal F}$ | `the norm of f in F` | Size of a function | nonnegative scalar |
| $T_K$ | `T sub K` | Integral operator defined by kernel $K$ | function-to-function map |

## Core concepts

### Treat one function as a vector

Consider a set of real-valued functions on the same set $\mathcal X$. For $f,g\in\mathcal F$ and scalars $a,b$, define pointwise operations by

$$
(af+bg)(x)=af(x)+bg(x)
$$

On the left, $af+bg$ is one function; evaluating it at input $x$ gives the real number on the right. Two functions with different domains cannot simply be added, so specify a common domain and a vector-space codomain. If the function set is nonempty and closed under all such linear combinations, it contains the zero function and additive inverses. The laws of real-number operations carry over pointwise, making it a vector space. An arbitrary subset of functions with the same domain is not automatically a vector space.

The space of polynomials of degree at most $d$ uses basis $(1,x,\ldots,x^d)$ to specify each function with $d+1$ coefficients. In contrast, the space of all continuous functions on $[0,1]$ contains polynomials of arbitrarily high degree, so no fixed finite basis can express them all. Even with a scalar input $x$, the space of functions can be infinite-dimensional. Dimension counts independently selectable function directions, not input components.

In the figure below, follow the pointwise combination of values at the same x across the entire curve.

<figure class="lesson-figure" markdown="1">

![The curves f=1+x and g=x squared combine pointwise into 3f minus 2g, with values 2,1,4 at x=1](../../figures/assets/A09-KER/A09-KER-01-pointwise-combination.svg)

<figcaption>Fixing input x=1 gives 3·2−2·1=4. Performing this calculation at every input produces the green curve, the function 3f−2g.</figcaption>
</figure>

### An operator's input and output

An operator $T$ is linear if it satisfies

$$
T(af+bg)=aT(f)+bT(g)
$$

Here, $aT(f)+bT(g)$ uses operations in the output space. Evaluation $E_x$ takes function $f$ as input and returns its value $f(x)$ at the specified point. With $x$ fixed, $E_x(af+bg)=aE_x(f)+bE_x(g)$ holds. Distinguish this from a separate rule that chooses the evaluation point depending on the function.

Differentiation is an example of an operator mapping functions to functions. On continuously differentiable functions, set $T(f)=f'$; the output is a continuous function. The input space must be specified so that derivatives exist. On this space, $(af+bg)'=af'+bg'$, so the operator is linear. The map $f\mapsto f^2$ is generally nonlinear: for $f(x)=1$, $T(2f)=4$ differs from $2T(f)=2$. Taking a function as input and being linear are separate conditions.

On the left below, the two curves coincide even when the order of operations is changed; on the right, the two outputs differ.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Differentiation of 3f minus 2g agrees with 3f prime minus 2g prime, while squaring twice a constant function gives 4 instead of 2](../../figures/assets/A09-KER/A09-KER-01-linear-versus-square.svg)

<figcaption>For differentiation, combining functions before or after the operation gives the same result. For the squaring operator, doubling the input differs from doubling the output.</figcaption>
</figure>

### An integral operator forms weighted sums of a function

For input function $f$, fixed kernel $K(x,z)$, and integration measure $\mu$, define the integral operator by

$$
(T_Kf)(x)=\int K(x,z)f(z)\,d\mu(z)
$$

The variable $z$ is integrated out, while $x$ remains as the input to the output function. At fixed $x$, $K(x,z)$ determines the weight assigned to $f(z)$ at each location. For a uniform measure on finitely many points, this integral can be read as an average such as $\sum_jK(x,z_j)f(z_j)/n$. Its domain consists of inputs for which the integral exists and the output belongs to the specified function space. Because $K$ and $\mu$ are fixed, linearity of integration gives $T_K(af+bg)=aT_Kf+bT_Kg$. If the kernel is redefined depending on $f$, the same linearity cannot be assumed.

A matrix represents a finite-dimensional linear operator after bases have been chosen. Collecting function values at finitely many input points also allows an integral operator to be calculated as a matrix-vector product, but that calculation concerns the selected points and integration approximation. Constructing a finite matrix does not make the original function space finite-dimensional.

Below, function values at z are collected with different weights at two output locations x.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three sampled function values are weighted by two fixed kernel rows and uniform one-third mass to produce outputs 1 and five thirds](../../figures/assets/A09-KER/A09-KER-01-integral-weighted-sum.svg)

<figcaption>After the values at z₁, z₂, and z₃ are summed, the output locations x₁ and x₂ remain. Arrows mark only terms with weight 1, and uniform mass 1/3 is applied to each output.</figcaption>
</figure>

### Changing parameters and changing a function

In a model $f_\theta$, different $\theta$ can represent the same function. Even with a large parameter distance, $f_\theta(x)$ may be nearly identical under the data distribution, so record distances in the two spaces separately.

Parameter-space comparisons concern differences in coefficients; function-space comparisons concern differences in outputs for the same input. For example, squaring the output difference between two checkpoints at each evaluation prompt and averaging gives the size of change on that prompt set. The value depends on which inputs were evaluated and their weights. To use a norm defined for all functions, first specify the function space and its norm. Zero difference on finitely many prompts does not imply that the functions are equal on unmeasured inputs.

The two figures below distinguish different parameters representing the same function from functions agreeing only at some inputs.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Parameters (1,2) and (2,1) have distance square root two but represent the same toy function f(x)=abx=2x](../../figures/assets/A09-KER/A09-KER-01-parameter-versus-output.svg)

<figcaption>The two distinct parameter points on the left represent the completely coinciding function 2x on the right. Parameter distance and the difference between output functions are separate quantities.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Functions zero and x times x minus one agree at test inputs 0 and 1 but differ by minus one quarter at input one half](../../figures/assets/A09-KER/A09-KER-01-finite-prompts-not-equality.svg)

<figcaption>The functions have the same values at evaluation inputs 0 and 1 but differ by −0.25 at the unmeasured input 0.5.</figcaption>
</figure>

## Small example

In $\mathcal F=\operatorname{span}\{1,x\}$, $f(x)=a+bx$. Evaluation operator $E_2$ returns $E_2(f)=a+2b$. In basis $(1,x)$, $E_2$ acts like row vector $(1,2)$.

The coordinates of function $f$ are column vector $(a,b)^\top$, and the matrix shape of $E_2$ is $1\times2$. The product $(1,2)(a,b)^\top$ gives scalar $a+2b$. The function itself, $a+bx$, its coordinates $(a,b)^\top$, and its value $a+2b$ at one point are different objects. Changing the basis changes both the coordinates and the operator's matrix, but the evaluation value of the same function is preserved.

In the figure below, distinguish the function's curve from the value extracted at one point.

<figure class="lesson-figure" markdown="1">

![The line f(x)=2 minus 3x is a function with coefficient coordinates (2,-3), while evaluation at minus one extracts the scalar 5](../../figures/assets/A09-KER/A09-KER-01-evaluation-not-function.svg)

<figcaption>Function 2−3x has coordinates (2,−3), and evaluation E₋₁ returns 5, the green point's height. Do not treat two coordinates and one evaluation value as the same object.</figcaption>
</figure>

## Common misconceptions

- One element of a function space is a function, not an input vector.
- Writing an operator as a matrix requires bases and coordinates.

## Exercises

### 1. Closure
If $f(x)=1+x$ and $g(x)=x^2$ are in the space of polynomials of degree at most 2, check whether $3f-2g$ belongs to the same space.
<details><summary>Show solution</summary>

Since $3f(x)-2g(x)=3+3x-2x^2$, its degree is at most 2 and it belongs to the same space.
</details>

### 2. Linearity
Is $T(f)=f(0)+1$ a linear operator?
<details><summary>Show solution</summary>

Since $T(0)=1$, it violates the requirement $T(0)=0$ for a linear map. It is an affine operator.
</details>

### 3. Evaluation
For $f(x)=2-3x$, find $E_{-1}(f)$.
<details><summary>Show solution</summary>

$f(-1)=2+3=5$.
</details>

### 4. Model interpretation
Two checkpoints have a large parameter distance but small output differences on all evaluation prompts. In which space can the change be described as small?
<details><summary>Show solution</summary>

The function-space change is small under the measured prompt distribution. This does not establish agreement on all unmeasured inputs or closeness in parameter space.
</details>

## Sources and update boundaries

This lesson applies the definitions of vector spaces and linear operators to functions. Topology, the full theory of operator norms, and domain issues for unbounded operators are outside its scope.

## Lesson summary

- Functions can form a vector space under pointwise operations.
- An operator is a map that takes functions as inputs.
- A matrix is a coordinate representation of a linear operator after bases are chosen.
- Parameter-space and function-space distances answer different questions.

## Pass criteria

- Can you test closure of a function space and linearity of an operator?
- Can you distinguish parameter changes from function changes in your descriptions?

## Next lesson

- [A09-KER-02 Positive definite kernels](A09-KER-02-positive-definite-kernel.md)

## Author checklist

- [x] Function spaces, operators, and coordinate representations are distinguished.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
