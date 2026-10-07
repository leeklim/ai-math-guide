---
id: "N05-01"
title: "Tensors and computation graphs"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "M00-09"
  - "M03-14"
estimated_time: "100–130 minutes"
---

# N05-01. Tensors and computation graphs

## Why this lesson matters

Neural-network code executes many tensor operations in sequence. Values alone show the final output, but tracing shape errors and gradient paths is difficult without knowing which operations needed which values. A computation graph records intermediate values together with dependencies between operations.

This lesson connects scalars, vectors, and matrices as tensors with different numbers of axes, rather than treating them as unrelated kinds of objects. We first calculate small products and sums by hand, then execute the same calculation in PyTorch.

## Learning objectives

After this lesson, you will be able to:

- Distinguish a tensor's axes, shape, dtype, and device.
- Represent operations as nodes and edges in a computation graph.
- Calculate intermediate values and shapes in order during a forward pass.
- Compare PyTorch tensor-operation outputs with hand calculations.
- Identify the operation-dependency paths connecting an output to its inputs.

## Prerequisite check

- Prerequisite lesson: [M00-09 Scalars, vectors, matrices, and shape](../../part-1-foundations/M00/M00-09-scalars-vectors-matrices-shape.md)
- Prerequisite lesson: [M03-14 Automatic differentiation and backpropagation](../../part-1-foundations/M03/M03-14-automatic-differentiation-backpropagation.md)
- Check: Can you explain how many positions each of the two axes has in a $2\times3$ matrix?
- Check: Can you identify the intermediate value on which $y$ depends in $y=f(g(x))$?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $x$ | `x` | Scalar or tensor element | Determined by context |
| $\mathbf x$ | `x` | Vector collecting elements along one axis | $\mathbf x\in\mathbb R^d$ |
| $\mathbf X$ | `X` | Example of a tensor with two or more axes | For example, $\mathbf X\in\mathbb R^{B\times d}$ |
| $\mathbf x\odot\mathbf w$ | `x elementwise times w` | Multiplication of elements at matching positions | Both inputs have the same shape |
| $\operatorname{shape}(\mathbf X)$ | `the shape of X` | Tuple listing the length of each axis | Tuple of nonnegative integers |
| dtype | `data type` | Numerical representation format of elements | For example, `float32` |
| device | `device` | Device where a tensor is stored and operated on | This book's required exercises use the CPU |
| computation graph | `computation graph` | Directed graph representing values and operation dependencies | Composed of nodes and edges |

## Core concept 1. From scalars to higher-dimensional tensors

A tensor is an object arranging numbers along multiple axes. The number of axes is sometimes called rank or number of dimensions, but code often uses `ndim` to avoid confusion with matrix rank.

| Object | Number of axes | Example shape |
|---|---:|---|
| Scalar | 0 | `()` |
| Vector | 1 | `(d,)` |
| Matrix | 2 | `(m, n)` |
| Higher-dimensional tensor | 3 or more | `(B, T, d)` |

Shape `(2, 3)` means two positions along the first axis and three along the second. There are $2\cdot3=6$ elements in total. Shape alone does not determine what the axes mean. The same `(2, 3)` could represent three features for each of two samples, or three-dimensional representations for each of two tokens.


In the array below, follow how a row index and a column index select one position.

<figure class="lesson-figure" markdown="1">

![Two indexed rows and three indexed columns select one of six tensor positions](../../figures/assets/N05/N05-01-indexed-axes.svg)

<figcaption>The first index selects a row, and the second selects a column. (1, 2) is the third position in the second row. Whether this position denotes a sample and feature or a token and dimension must be specified separately.</figcaption>

</figure>

## Core concept 2. Dtype and device are distinct from shape

Shape describes the arrangement of elements, dtype describes how each element is represented, and device specifies the storage and computation location. This does not mean all three properties must match. For example, two tensors of shape `(2,)` can have different dtypes: one can be `float32` and the other an integer type.

The required N05 exercises use `float32` and the CPU. These are educational execution conditions. Choosing `float32` does not change the definition of a mathematical vector, but actual calculations can incur rounding error.

## Core concept 3. Nodes and edges in a computation graph

Consider the calculation

\[
\mathbf p=\mathbf x\odot\mathbf w,
\qquad
y=\sum_{i=1}^{2}p_i
\]

Both the values $\mathbf x,\mathbf w,\mathbf p,y$ and the operations—elementwise multiplication and summation—can be treated as nodes. A directed edge indicates a dependency: one node's output is used as an input to the next operation.

```text
x ─┐
   ├─ elementwise multiply ─ p ─ sum ─ y
w ─┘
```

An edge does not mean that the entire data array is copied. A computation graph represents mathematical dependencies. The framework's memory layout and kernel execution are separate matters.

In the representation above, with both values and operations as nodes, the multiplication node receives two input values and produces $\mathbf p$; the summation node receives $\mathbf p$ and produces $y$. If only values are drawn as nodes, the same dependencies can be written as $\mathbf x\to\mathbf p$, $\mathbf w\to\mathbf p$, and $\mathbf p\to y$, with operations indicated on the connections. Either representation requires an operation's inputs to be calculated before its next value can be obtained. Input-output connections, rather than the order in which nodes are placed in the drawing, determine the calculation order.


Follow the joins and arrows below to identify which inputs are needed first.

<figure class="lesson-figure" markdown="1">

![Two input vectors join at elementwise multiplication then product flows through sum to scalar eleven](../../figures/assets/N05/N05-01-forward-graph.svg)

<figcaption>Both x and w enter the multiplication to produce p. Summation executes after p has been calculated, so the arrows show which values must precede others.</figcaption>

</figure>

## Core concept 4. Forward values and intermediate values

A forward pass calculates values from input to output. With $\mathbf x=(1,2)$ and $\mathbf w=(3,4)$,

\[
\mathbf p=(1\cdot3,\;2\cdot4)=(3,8)
\]

and

\[
y=3+8=11
\]

The shapes change as follows.

\[
(2,)\ \text{and}\ (2,)
\longrightarrow
(2,)
\longrightarrow
()
\]

The final `()` is the shape of a scalar tensor. Containing one number is not the same as being a Python scalar rather than a tensor. A zero-dimensional PyTorch tensor also has shape `()`, a dtype, and a device.

Elementwise multiplication multiplies $x_i$ and $w_i$ at a specified $i$, so the result retains the same index $i$. By contrast, summing all elements combines both $p_i$ into one value, leaving no position to select with $i$. This is why one axis disappears from the shape. Shape `(1,)` also contains one number, but is a vector with an index, distinct from `()` obtained by summing over all axes.


The figure separates multiplication, which retains the two index positions, from summation, which removes the index.

<figure class="lesson-figure" markdown="1">

![Two elementwise products retain index positions before both feed a sum with no remaining index](../../figures/assets/N05/N05-01-reduction-axis.svg)

<figcaption>The products at i = 1 and i = 2 remain at separate positions. Summation combines them into one value. Even when each contains one number, [11], with an index remaining, and scalar 11 have different shapes.</figcaption>

</figure>

## Core concept 5. Dependency paths and gradients

$y$ depends on $p_1,p_2$, and each $p_i$ depends on $x_i,w_i$. The computation graph therefore has a forward path from $\mathbf x$ to $y$. Gradient calculation traces these dependencies backward from the output. Differentiating gives

\[
\frac{\partial y}{\partial x_i}=w_i
\]

so the gradient in this example is

\[
\nabla_{\mathbf x}y=(3,4)
\]

Graph connections alone do not determine gradient values. The function executed at each node and the forward values are also needed.

Since $y=p_1+p_2$, the derivative $\partial y/\partial p_i$ with respect to each intermediate value is 1. In $p_i=x_iw_i$, differentiating with respect to $x_i$ while fixing $w_i$ leaves $w_i$; $p_j$ at another position does not depend on $x_i$. Multiplying the two local derivatives by the chain rule gives $1\cdot w_i$, producing the gradient above. If $w_i=0$, the graph connection still exists but that derivative is zero. Distinguish the existence of a dependency path from how much change is transmitted at the current input.


In the reverse-direction figure, multiply the summation's local derivative by the multiplication's local derivative in turn.

<figure class="lesson-figure" markdown="1">

![A scalar output seed of one splits through the sum then multiplies by weights three and four to give input derivatives](../../figures/assets/N05/N05-01-reverse-local-derivatives.svg)

<figcaption>The output derivative seed 1 passes through summation as 1 to each input. At each product, multiplying by the saved w₁ = 3 or w₂ = 4 gives the two derivatives with respect to x: 3 and 4.</figcaption>

</figure>


In the next figure, the calculation path remains even when multiple inputs map to the same zero.

<figure class="lesson-figure" markdown="1">

![A connected multiplication by zero maps all shown input values to the same product zero while its local derivative is zero](../../figures/assets/N05/N05-01-connected-zero-gradient.svg)

<figcaption>With wᵢ = 0 fixed, multiple values of xᵢ all connect to pᵢ = 0. The calculation path remains, but both the local derivative at this position and the final derivative are zero.</figcaption>

</figure>

## Example 1. Trace shapes and values by hand

### Problem

For $\mathbf x=(1,2)$ and $\mathbf w=(3,4)$, calculate $\mathbf p=\mathbf x\odot\mathbf w$ and $y=p_1+p_2$, and state every shape.

### Solution

Both inputs are vectors of length 2, so both have shape `(2,)`. Elementwise multiplication multiplies the two elements at each matching position.

\[
\mathbf p=(1\cdot3,2\cdot4)=(3,8),
\qquad
\operatorname{shape}(\mathbf p)=(2,)
\]

Summing the two elements gives $y=11$ with shape `()`.

### Meaning of the result

The elementwise-multiplication node preserved the axis, while the summation node removed it. Recording values alongside shapes identifies the operation at which a dimension disappears.

## Example 2. Finding these operations in a model

A neural network's affine transformations, activations, attention, and loss can all be represented as computation-graph nodes. Saving a particular activation in model interpretation usually means recording a value produced by an intermediate graph node. Observing an intermediate value alone does not establish that it causes the output. Causal claims require interventions and control conditions.

## Execution exercise

### Execution environment and sources

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Verification date: 2026-10-01
- Component category: `Stable core`
- Example ID: `n05_01_tensor_graph`
- Source code: `labs/N05/n05_01_tensor_graph.py`
- Test: `tests/N05/test_n05_01.py`
- Run command: `.venv\Scripts\python.exe -m labs.N05.n05_01_tensor_graph`

### Resource budget

This example uses tensors of length 2, 0 parameters, and 0 training steps. Intra-op and inter-op CPU thread counts are each 1, and the hard timeout is 10 seconds.

### Actual code and execution results

The site build inserts source code and actual execution results at the location below. Execution code is not duplicated in the Markdown source.

<!-- N05_EXAMPLE: n05_01_tensor_graph -->

### Interpreting the results

`product=[3.0, 8.0]` and `output=11.0` match the hand calculation. The shape of `product` is `[2]`, while `output`, which sums all elements, has shape `[]`. An empty shape list in JSON corresponds to `torch.Size([])` for a PyTorch scalar tensor.

`x.grad=[3.0, 4.0]` confirms $\nabla_{\mathbf x}y=\mathbf w$. The test compares values and gradients, rather than strings, using `rtol=10^{-6}` and `atol=10^{-7}`.

## Common misconceptions

### Misconception 1. The number of axes is the same as matrix rank

In code, tensor rank sometimes means the number of axes. In linear algebra, matrix rank is the maximum number of independent rows or columns. This book prefers `ndim` for the number of axes to avoid confusion.

### Misconception 2. A computation-graph edge proves causation

An edge represents a calculation dependency within the specified program. A scientific claim that a particular activation causes a behavior requires intervention results and control conditions.

### Misconception 3. If code runs, the calculation is correct

Code finishing without errors confirms executability. Separate tests must check whether numerical values, shapes, and gradients match hand calculations.

## Exercises

### 1. Classifying tensors

For tensors of shape `()`, `(4,)`, `(2, 3)`, and `(2, 5, 8)`, state the number of axes and elements in each.

<details>
<summary>Show solution</summary>

The numbers of axes are 0, 1, 2, and 3, respectively. The numbers of elements are 1, 4, $2\cdot3=6$, and $2\cdot5\cdot8=80$, respectively.

</details>

### 2. Tracing shapes

All elements of $\mathbf A\in\mathbb R^{2\times3}$ are added to produce a scalar $s$. State the input and output shapes.

<details>
<summary>Show solution</summary>

$\mathbf A$ has shape `(2, 3)`, and $s$ has shape `()`, because both axes were summed over.

</details>

### 3. Computation graph

State the nodes and dependency edges of $a=x+1$, $b=a^2$, and $y=3b$ in order.

<details>
<summary>Show solution</summary>

Using value nodes, the graph is $x\to a\to b\to y$. The operations along the edges are adding 1, squaring, and multiplying by 3, respectively. $y$ depends indirectly on all of $b,a,x$.

</details>

### 4. Hand calculation and gradient

For $\mathbf x=(2,-1)$ and $\mathbf w=(5,3)$, find $y=\sum_i x_iw_i$ and $\nabla_{\mathbf x}y$.

<details>
<summary>Show solution</summary>

$y=2\cdot5+(-1)\cdot3=7$. Since $\partial y/\partial x_i=w_i$, $\nabla_{\mathbf x}y=(5,3)$.

</details>

### 5. Assessing dtype

Can a `float32` tensor and an integer tensor with the same shape be called the same mathematical object?

<details>
<summary>Show solution</summary>

Their array structures agree in the sense of having the same shape. However, their dtypes, permitted numerical operations, and rounding properties differ, so they are not identical execution objects. Distinguish the mathematical context from the implementation context.

</details>

### 6. Critiquing a claim

Evaluate the claim: “This activation causes the model's behavior because it has a graph path to the output.”

<details>
<summary>Show solution</summary>

A graph path shows a possible computational dependency, not evidence that the activation is necessary or sufficient for a particular behavior. Interventions changing the activation, appropriate controls, and behavioral measurements are needed.

</details>

## Lesson summary

- Scalars, vectors, matrices, and higher-dimensional arrays can be connected as tensors with different numbers of axes and shapes.
- Shape, dtype, and device are distinct execution properties.
- A computation graph represents node values and operation dependencies through directed edges.
- A forward pass calculates values and shapes from input to output.
- Code execution, numerical correctness, and interpretation claims require different forms of verification.

## Pass criteria

You pass when you can answer these questions without consulting the material:

- Can you assign meanings to the three axes in shape `(B, T, d)` and calculate the number of elements?
- Can you turn a small expression into nodes and edges?
- Can you trace each node's forward value and shape?
- Can you distinguish dtype and device from shape?
- Can you explain the difference between a graph path and causal evidence?

## Next lesson

- [N05-02 A single neuron](N05-02-single-neuron.md)

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] All new symbols are defined before use.
- [x] Vector and tensor shapes are consistent.
- [x] Intuition and exact definitions are distinguished.
- [x] Example calculations and gradients are checked.
- [x] Every exercise has a solution.
- [x] Strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and math rendering are checked.
- [x] Execution code is not manually duplicated in Markdown.
- [x] Source-code and test paths, resource budgets, and verification dates are recorded.
- [x] Shape, numerical-value, and gradient tests are provided.
