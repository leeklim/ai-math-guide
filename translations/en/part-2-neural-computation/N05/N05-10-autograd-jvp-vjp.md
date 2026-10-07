---
id: "N05-10"
title: "Autograd, JVP, and VJP"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-09"
  - "M03-13"
estimated_time: "150~180 minutes"
---

# N05-10. Autograd, JVP, and VJP

## Why this lesson matters

A full Jacobian lays out both input and output dimensions. In actual neural network analysis, JVPs that propagate specific input directions and VJPs that pull back specific output directions are often calculated instead of the Jacobian itself. Backpropagation is a VJP for a scalar loss.

This lesson calculates the Jacobian of a $\mathbb R^2\to\mathbb R^2$ function by hand and compares it with JVPs and VJPs from `torch.func`. It then checks the tensors, forward computation, loss, backward computation, and updates from N05-01~10 as one sequence.

## Learning objectives

- Explain the meanings of Jacobian rows and columns.
- Calculate a JVP from an input tangent.
- Calculate a VJP from an output cotangent.
- Explain criteria for choosing forward or reverse mode.
- Connect the computation stages from N05-01~10 into one training loop.

## Prerequisite check

- Prerequisite lesson: [N05-09 PyTorch tensors, shapes, and dtypes](N05-09-pytorch-tensor-shape-dtype.md)
- Prerequisite lesson: [M03-13 JVP and VJP](../../part-1-foundations/M03/M03-13-jvp-vjp.md)
- Check question: Can you multiply a $2\times2$ matrix by a vector?
- Check question: Can you explain that a gradient is the derivative of a scalar-output function?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $f$ | `f` | Vector-valued function | $\mathbb R^n\to\mathbb R^m$ |
| $J_f(\mathbf x)$ | `the Jacobian of f at x` | Derivative matrix connecting input changes to output changes | $\mathbb R^{m\times n}$ |
| $\mathbf r$ | `r` | Input tangent direction | $\mathbb R^n$ |
| $J_f\mathbf r$ | `J f times r` | Jacobian-vector product, JVP | $\mathbb R^m$ |
| $\mathbf u$ | `u` | Output cotangent | $\mathbb R^m$ |
| $\mathbf u^\top J_f$ | `u transpose times J f` | Vector-Jacobian product, VJP | $\mathbb R^n$ |
| autograd | `automatic differentiation` | A system calculating derivative products through a computation graph | A framework feature |

## Core concept 1. A Jacobian collects all first-order sensitivities

The Jacobian of $f:\mathbb R^n\to\mathbb R^m$ is

\[
J_f(\mathbf x)_{ij}=\frac{\partial f_i}{\partial x_j}
\]

Row $i$ is the input gradient of output $f_i$, while column $j$ collects the first-order changes in all outputs along input direction $x_j$.

At a current point where the function is differentiable, $f(\mathbf x+\Delta\mathbf x)-f(\mathbf x)\approx J_f(\mathbf x)\Delta\mathbf x$. Each row sums the changes in input components multiplied by their corresponding partial derivatives. The input index is therefore summed out, leaving the output index. A Jacobian collects change coefficients at the evaluation point, not function values.

## Core concept 2. A JVP propagates an input direction forward

The JVP for an input tangent $\mathbf r$ is

\[
J_f(\mathbf x)\mathbf r
\]

It starts in the input dimension and gives a directional derivative in the output dimension. Forward-mode products are useful when there are few input directions and many outputs.

Moving the input to $\mathbf x+\varepsilon\mathbf r$ and differentiating at $\varepsilon=0$ gives $\left.d f(\mathbf x+\varepsilon\mathbf r)/d\varepsilon\right|_{\varepsilon=0}=J_f(\mathbf x)\mathbf r$. This adds together the effects of moving several components of $\mathbf r$ at once. Doubling $\mathbf r$ doubles the JVP, so comparisons of direction alone also require matching length conditions. Supplying coordinate-axis directions one at a time gives the Jacobian's columns, but calculating one direction of interest does not require storing every column.

## Core concept 3. A VJP pulls an output direction backward

The VJP for an output cotangent $\mathbf u$ is

\[
\mathbf u^\top J_f(\mathbf x)
\]

It equals the gradient obtained by differentiating the scalar combination $\mathbf u^\top f(\mathbf x)$ with respect to the input. For a scalar loss, $m=1$, so one reverse-mode pass gives gradients for many parameters.

Here, $\mathbf u$ contains output weights held fixed during differentiation. Weighting each output row's derivatives by $u_i$ and summing leaves a coefficient for each input component. The derivative in row form is $\mathbf u^\top J_f$; the gradient in column-vector form is $J_f^\top\mathbf u$. These arrange the same coefficients in different orientations and correspond to the gradient returned by a framework with the same shape as the input.

Selecting one output uses $\mathbf u$ with 1 only at that position. Selecting a difference between two outputs uses weights 1 and $-1$ at those positions. A VJP therefore does not invert an output vector into an input change. It propagates the derivative of the selected scalar measurement to the input.

## Example 1. Calculating a Jacobian by hand

Let

\[
f(x_1,x_2)=
\begin{bmatrix}
x_1x_2\\
x_1^2+x_2
\end{bmatrix}
\]

Its Jacobian is

\[
J_f(x_1,x_2)=
\begin{bmatrix}
x_2&x_1\\
2x_1&1
\end{bmatrix}
\]

At $(x_1,x_2)=(2,3)$, we obtain output $(6,7)$ and

\[
J_f=\begin{bmatrix}3&2\\4&1\end{bmatrix}
\]

In the matrix diagram below, distinguish the sensitivities grouped by an output row from those grouped by an input column.

<figure class="lesson-figure" markdown="1">

![Jacobian entries three two four one at input two three align output rows f one f two and input columns x one x two with first column three four highlighted](../../figures/assets/N05/N05-10-jacobian-indices.svg)

<figcaption>Output rows and input columns are separated at the evaluation point (2, 3). The first column (3, 4) gives the first-order rates of change of both outputs when only x₁ moves slightly. The first row (3, 2) gives f₁'s sensitivities to the two inputs.</figcaption>
</figure>

## Example 2. JVP and VJP

For $\mathbf r=(1,-1)$,

\[
J_f\mathbf r=(1,3)
\]

For $\mathbf u=(2,-1)$,

\[
\mathbf u^\top J_f=(2,3)
\]

Even if the two vectors happen to have similar numbers, they represent different spaces and directions.

In the coordinate plot below, compare the actual output path corresponding to the input path with its tangent.

<figure class="lesson-figure" markdown="1">

![Output path six plus epsilon minus epsilon squared seven plus three epsilon plus epsilon squared bends away from the tangent with derivative one three at output six seven](../../figures/assets/N05/N05-10-jvp-path.svg)

<figcaption>The figure shows the actual output path as the input moves along (2, 3) + ε(1, −1), together with its tangent at ε = 0. The tangent's change per ε is the JVP (1, 3). The actual path adds (−ε², ε²), creating a difference for finite movement.</figcaption>
</figure>

The next vector diagram adds Jacobian columns weighted by the input direction's two components.

<figure class="lesson-figure" markdown="1">

![In output derivative coordinates the first Jacobian column three four and negative second column minus two minus one add head to tail to product one three](../../figures/assets/N05/N05-10-jvp-column-sum.svg)

<figcaption>Multiply the first column (3, 4) by 1 and the second column (2, 1) by −1, then add head-to-tail. These coordinate axes are output rate-of-change components, not the original input point or positions of output function values.</figcaption>
</figure>

In the diagram below, follow how a fixed scalar measurement's derivative propagates to the input.

<figure class="lesson-figure" markdown="1">

![Fixed output weights two and minus one select scalar two f one minus f two and pull weighted rows six four and minus four minus one back to input gradient two three](../../figures/assets/N05/N05-10-vjp-measurement.svg)

<figcaption>Fixing u = (2, −1) selects the scalar 2f₁ − f₂. At the example's point, weighting the output rows gives (6, 4) and (−4, −1). Adding at corresponding input positions gives (2, 3). This does not invert output values.</figcaption>
</figure>

In the two paths below, compare the scalar measurements along forward propagation and backward pullback.

<figure class="lesson-figure" markdown="1">

![Input direction one minus one pushed to output direction one three pairs with output weights two minus one to minus one while pulled-back input gradient two three pairs with input direction to the same scalar](../../figures/assets/N05/N05-10-dual-pairing.svg)

<figcaption>The upper path propagates the input direction to the output and measures it with u. The lower path pulls u back to an input derivative and measures it with r. Both give scalar −1. This does not mean that the intermediate vectors belong to the same space or are inverses of each other.</figcaption>
</figure>

## Executable lab

### Execution environment and sources

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Checked on: 2026-10-01
- Component classification: JVP and VJP mathematics are `Stable core`; the `torch.func` API is a framework interface
- Example ID: `n05_10_jvp_vjp`
- Code source: `labs/N05/n05_10_jvp_vjp.py`
- Test: `tests/N05/test_n05_10.py`
- Execution command: `.venv\Scripts\python.exe -m labs.N05.n05_10_jvp_vjp`

### Resource budget

The example uses only 2-dimensional inputs and outputs. The full Jacobian has 4 elements, and parameter and training step counts are both 0. The hard timeout is 10 seconds.

### Actual code and execution results

<!-- N05_EXAMPLE: n05_10_jvp_vjp -->

### Product checks

The tests compare the Jacobian from `jacrev` with hand-calculated values. They also compare the `jvp` and `vjp` results with their respective explicit matrix products.

## Why not materialize a full Jacobian?

For large inputs and outputs, the Jacobian has $mn$ elements. JVPs and VJPs calculate only products in directions of interest. In model interpretation, product forms such as a target logit's input gradient, the output effect of an activation direction, and Hessian-vector products reduce memory use.

Details of the `torch.func` API can change with framework versions. This book's CPU environment was tested with 2.13.0, and the definitions of `jvp`, `vjp`, and `jacrev` were checked again in the official current stable documentation on 2026-10-01.

In the array diagram below, compare the number of result positions in a full matrix and in direction-specific products.

<figure class="lesson-figure" markdown="1">

![A five by three full Jacobian grid has fifteen entries while one input direction yields five output entries and one output measurement yields three input entries](../../figures/assets/N05/N05-10-materialize-versus-product.svg)

<figcaption>The positions show shape n = 3, m = 5, as in Exercise 1. The full Jacobian contains 15 sensitivities, while a single-direction JVP gives 5 output entries and a single-measurement VJP gives 3 input entries. The figure does not assume that actual computational cost equals the element count.</figcaption>
</figure>

## Connection to model interpretation

The gradient used in input attribution is a VJP from the selected scalar output to the input. A local analysis propagating an activation steering direction to the next layer's output can be expressed as a JVP.

Both products are local linearizations at the current point. They can differ from actual output changes when a finite intervention is large or an activation passes through a saturation region.

## Common misconceptions

### Misconception 1. JVP and VJP are the same vector with different transpose notation

A JVP sends an input-space vector to output space; a VJP pulls an output-space covector back to the input. If input and output dimensions differ, their shapes already differ.

### Misconception 2. Autograd always constructs symbolic derivative expressions

PyTorch uses the graph of executed tensor operations and derivative rules to calculate numerical products. This does not mean it automatically stores a full symbolic expression or full Jacobian.

### Misconception 3. An intervention in the gradient direction exactly matches the actual change

A gradient gives a first-order approximation for small changes. Finite steps include curvature and nonlinear effects along other paths.

## Exercises

### 1. Jacobian shape

State the shapes of the Jacobian, JVP, and VJP for $f:\mathbb R^3\to\mathbb R^5$.

<details><summary>Show solution</summary>

The Jacobian is $(5,3)$, the JVP has length 5, and the VJP has length 3.

</details>

### 2. Calculating a JVP

Find $Jr$ for $J=\begin{bmatrix}1&2\\3&4\end{bmatrix}$ and $r=(2,-1)$.

<details><summary>Show solution</summary>

It is $(1\cdot2+2(-1),3\cdot2+4(-1))=(0,2)$.

</details>

### 3. Calculating a VJP

Find $u^\top J$ for the preceding $J$ and $u=(1,-1)$.

<details><summary>Show solution</summary>

It is $(1,-1)J=(-2,-2)$.

</details>

### 4. Choosing a mode

Explain why reverse mode is appropriate for calculating the gradient of a scalar loss with respect to one million parameters.

<details><summary>Show solution</summary>

The output dimension is 1, so one VJP gives the gradients in all parameter directions. The full Jacobian row need not be materialized separately.

</details>

### 5. Choosing a target

In a language model, which scalar must be recorded as the backward starting point to reproduce gradient attribution?

<details><summary>Show solution</summary>

Specify the selected scalar, such as a target token logit, the logit difference between two tokens, or a loss. Different targets produce different VJPs.

</details>

### 6. Critiquing a claim

Evaluate the conclusion that a direction with a large JVP also produces the largest output change under a large finite intervention.

<details><summary>Show solution</summary>

A JVP is a local derivative at the current point. Step size, curvature, and path changes can alter the ranking of finite interventions.

</details>

## N05-01~10 cumulative checkpoint

Record the following sequence as one computation.

1. Declare the tensor shapes and dtypes of an affine model with batch size 2.
2. Calculate forward predictions and mean cross-entropy or squared-error loss.
3. Draw the dependency paths leading to the loss in the computation graph.
4. Compare parameter gradients from hand calculation and autograd.
5. Apply the learning rate to perform one update step.
6. Choose momentum or AdamW and state the optimizer state to be saved.
7. Calculate a JVP for one input tangent or a VJP for one output cotangent.
8. State the scope of the claim without extending an observed gradient into a causal effect.

Keep code execution, numerical assertions, shape assertions, and interpretation statements separate in the checkpoint record.

## Evidence and stage review

- The JVP, VJP, and `jacrev` definitions in the [torch.func API](https://docs.pytorch.org/docs/stable/func.api.html) were checked.
- Tensors, activations, losses, backpropagation, mini-batches, and optimizer states in N05-01~10 retain the `Stable core` classification.
- Framework APIs and kernels are separate from mathematical definitions. The current stable `torch.func` documentation states that APIs may change, so local pinned tests are retained alongside it as a reference for correctness.
- This scope does not require external model configurations. Public configuration comparisons apply from N05-11 onward, where Transformer components begin.

## Lesson summary

- A Jacobian collects all first-order sensitivities of a vector-valued function.
- A JVP sends an input tangent to a directional change in the output.
- A VJP pulls an output cotangent back to the input.
- Reverse-mode backpropagation is a VJP for a scalar loss.
- Product computation avoids materializing a full Jacobian.

## Pass criteria

- Can you state the shapes of a Jacobian, JVP, and VJP?
- Can you calculate both products for a small function by hand?
- Can you choose between forward and reverse mode?
- Can you compare `torch.func` results with explicit products?
- Can you explain the training computations from N05-01~10 as one sequence?

## Next lesson

- [N05-11 Tokens and tokenizers](N05-11-token-tokenizer.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] The directions and shapes of JVP and VJP are distinguished.
- [x] Full Jacobians and product computation are distinguished.
- [x] The N05-01~10 cumulative checkpoint is included.
- [x] Every exercise has a solution.
- [x] The strength of model interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and math rendering have been checked.
- [x] Executable code is not manually duplicated in Markdown.
- [x] Code sources, test paths, resource budgets, and check dates are recorded.
- [x] Shape, numerical, and gradient tests are provided.
