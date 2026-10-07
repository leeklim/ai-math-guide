---
id: "N05-03"
title: "MLP forward pass"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-02"
  - "M02-04"
estimated_time: "120–150 minutes"
---

# N05-03. MLP forward pass

## Why this lesson matters

Actual neural networks do not calculate neurons one by one in a Python loop. They stack multiple neurons' weights in a matrix and multiple samples along a batch axis, then perform the same operation together. Reading this representation lets us match code's `matmul`, weight shapes, and hidden activations to equations.

This lesson calculates a two-layer multilayer perceptron (MLP) directly through tensor operations, without high-level `torch.nn` modules. At every stage, we check the shapes of inputs, pre-activations, hidden activations, and outputs.

## Learning objectives

After this lesson, you will be able to:

- Arrange multiple neurons' weights in one matrix.
- Distinguish batch, input, hidden, and output axes.
- Calculate a two-layer MLP's forward pass using matrix expressions.
- Explain where the activation function is applied elementwise.
- Check the shapes of intermediate activations and parameter gradients.

## Prerequisite check

- Prerequisite lesson: [N05-02 A single neuron](N05-02-single-neuron.md)
- Prerequisite lesson: [M02-04 Matrices and matrix multiplication](../../part-1-foundations/M02/M02-04-matrices-matrix-multiplication.md)
- Check: Can you find the product shape of a $(2\times3)$ matrix and a $(3\times4)$ matrix?
- Check: Can you identify the batch axis when two sample vectors are stacked as rows?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\mathbf X$ | `X` | Input batch with samples stacked as rows | $\mathbb R^{B\times d_{\mathrm{in}}}$ |
| $\mathbf W_1$ | `W sub one` | First-layer weight matrix | $\mathbb R^{d_{\mathrm{hidden}}\times d_{\mathrm{in}}}$ |
| $\mathbf b_1$ | `b sub one` | Bias for each first-layer neuron | $\mathbb R^{d_{\mathrm{hidden}}}$ |
| $\mathbf Z_1$ | `Z sub one` | First-layer pre-activation batch | $\mathbb R^{B\times d_{\mathrm{hidden}}}$ |
| $\mathbf H$ | `H` | Hidden activation after elementwise activation | $\mathbb R^{B\times d_{\mathrm{hidden}}}$ |
| $\mathbf W_2$ | `W sub two` | Output-layer weight matrix | $\mathbb R^{d_{\mathrm{out}}\times d_{\mathrm{hidden}}}$ |
| $\mathbf Y$ | `Y` | MLP output batch | $\mathbb R^{B\times d_{\mathrm{out}}}$ |
| MLP | `M L P` | Feed-forward network connecting affine layers and nonlinearities | Two layers in this lesson |

## Core concept 1. Stack neurons as matrix rows

Suppose there are $d_{\mathrm{hidden}}$ hidden neurons, each receiving an input of length $d_{\mathrm{in}}$. Stacking their weight vectors as rows gives

\[
\mathbf W_1\in
\mathbb R^{d_{\mathrm{hidden}}\times d_{\mathrm{in}}}
\]

Writing the input as a column vector, the first layer for one sample is

\[
\mathbf z_1=\mathbf W_1\mathbf x+\mathbf b_1
\]

The $j$th row calculates the $j$th neuron's dot product.

In components, $z_{1j}=\sum_{k=1}^{d_{\mathrm{in}}}(W_1)_{jk}x_k+(b_1)_j$. Summation consumes input index $k$ and retains neuron index $j$, giving output length $d_{\mathrm{hidden}}$. Each row mixes multiple input components, while different rows apply different weights and biases to the same input.


Each row of W₁ uses the same input to produce a different hidden position.

<figure class="lesson-figure" markdown="1">

![One input vector feeds three distinct weight rows each computing its own dot product and bias](../../figures/assets/N05/N05-03-neuron-rows.svg)

<figcaption>Apply each of W₁'s three rows to the same input (1, 2). Each row sums two input features to produce one z value, so the three rows correspond to three hidden positions. The numbers match the first sample in the example below.</figcaption>

</figure>

## Core concept 2. A batch stacks samples as rows

Stacking $B$ inputs as rows gives

\[
\mathbf X\in\mathbb R^{B\times d_{\mathrm{in}}}
\]

The batch expression applying the same weights to every sample is

\[
\mathbf Z_1=\mathbf X\mathbf W_1^\top+\mathbf b_1
\]

The bias vector is added to each row. In this case, PyTorch broadcasts `(d_hidden,)` over the rows of `(B, d_hidden)`.

Tracking shapes alone gives

\[
(B,d_{\mathrm{in}})
(d_{\mathrm{in}},d_{\mathrm{hidden}})
\longrightarrow
(B,d_{\mathrm{hidden}})
\]

The second factor is the shape of $\mathbf W_1^\top$.

Transposing the result calculated for one column-vector sample gives $\mathbf z_1^\top=\mathbf x^\top\mathbf W_1^\top+\mathbf b_1^\top$. The batch expression stacks this row calculation $B$ times. Summation runs over the input-feature axis, leaving the batch axis. Thus, one row's output in this layer does not use another row's input. Samples share the same parameters rather than receiving new weights for each sample.


The two solid paths keep samples separate; dashed paths indicate use of shared parameters.

<figure class="lesson-figure" markdown="1">

![Two sample rows pass through a shared weight and bias layer without a connection between sample lanes](../../figures/assets/N05/N05-03-batch-shared-weights.svg)

<figcaption>The two sample rows use the same W₁ and b₁ without mixing with one another. Blue solid lines show sample-value flow; purple dashed lines indicate reuse of the same parameters in each calculation. Both batch positions remain in the output.</figcaption>

</figure>


The array shows the direction in which the same bias is added to each batch row.

<figure class="lesson-figure" markdown="1">

![A single bias vector is reused for each sample row before addition yields the two by three pre-activation matrix](../../figures/assets/N05/N05-03-bias-broadcast.svg)

<figcaption>Add b₁ = (0.5, −0.5, 0) to each of the two sample rows. The two bias rows below represent repeated values in the calculation, not two independent sets of bias parameters.</figcaption>

</figure>

## Core concept 3. Apply the activation function elementwise

Applying ReLU to the first-layer pre-activation gives

\[
\mathbf H=\operatorname{ReLU}(\mathbf Z_1)
\]

Since the same scalar function is applied to each element, the shape does not change.

\[
\mathbf Z_1,\mathbf H
\in\mathbb R^{B\times d_{\mathrm{hidden}}}
\]

Values and gradient paths do change. Negative pre-activations become zero, and ReLU's local derivatives at those positions are also zero.

An element set to zero still occupies its position in the tensor. ReLU does not delete hidden units or shrink the batch. Which positions become zero also depends on each sample's pre-activations. The same neuron can lie in the positive region for one sample and the negative region for another.


Compare matching positions in the before-and-after arrays: positions remain even when their values become zero.

<figure class="lesson-figure" markdown="1">

![Two by three matrices before and after ReLU retain all positions while three negative cells turn to zeros](../../figures/assets/N05/N05-03-relu-cell-map.svg)

<figcaption>Only the three negative positions become zero; row and column positions stay unchanged. In particular, the first hidden unit keeps 1.5 for the first sample but becomes zero for the second, showing that gate states vary by sample.</figcaption>

</figure>

## Core concept 4. The second affine layer

For output dimension $d_{\mathrm{out}}$,

\[
\mathbf Y=\mathbf H\mathbf W_2^\top+\mathbf b_2,
\qquad
\mathbf W_2\in\mathbb R^{d_{\mathrm{out}}\times d_{\mathrm{hidden}}}
\]

The full two-layer MLP is

\[
\operatorname{MLP}(\mathbf X)
=\operatorname{ReLU}(\mathbf X\mathbf W_1^\top+\mathbf b_1)
\mathbf W_2^\top+\mathbf b_2
\]

Here “two-layer” counts two trainable affine transformations.

The second layer receives first-layer hidden activations as input features, not the original inputs. Its bias $\mathbf b_2$ has length $d_{\mathrm{out}}$ and, as in the first layer, is added to each sample row. No further ReLU is applied to this example's output. Thus, $\mathbf Y$ can contain negative values even when all of $\mathbf H$ is nonnegative.

Removing the intermediate ReLU gives a single sample's output as $\mathbf W_2\mathbf W_1\mathbf x+\mathbf W_2\mathbf b_1+\mathbf b_2$, which combines into one affine map. With the intermediate activation, some hidden values become zero depending on the input, so this combined expression cannot be used unchanged over the entire input space. Increasing hidden dimension and introducing a nonlinear transformation serve different roles.


The two readouts show how signed output-layer weights can produce a negative output even from nonnegative hidden activations.

<figure class="lesson-figure" markdown="1">

![Two nonnegative hidden rows produce positive and negative outputs through signed output weights two minus one and one half](../../figures/assets/N05/N05-03-output-readout.svg)

<figcaption>Output weights (2, −1, 0.5) recombine the hidden components. For the second sample, 2.5 is multiplied by weight −1, so the output is −2.25 even after adding the final bias 0.25.</figcaption>

</figure>

## Example 1. Forward pass for two samples

### Problem

Use the following values.

\[
\mathbf X=
\begin{bmatrix}
1&2\\
-1&3
\end{bmatrix},
\quad
\mathbf W_1=
\begin{bmatrix}
1&0\\
0&1\\
1&-1
\end{bmatrix},
\quad
\mathbf b_1=(0.5,-0.5,0)
\]

\[
\mathbf W_2=
\begin{bmatrix}
2&-1&0.5
\end{bmatrix},
\qquad
\mathbf b_2=(0.25)
\]

Calculate $\mathbf Z_1$, $\mathbf H$, and $\mathbf Y$.

### Solution

The first affine layer is

\[
\mathbf Z_1
=\mathbf X\mathbf W_1^\top+\mathbf b_1
=
\begin{bmatrix}
1.5&1.5&-1\\
-0.5&2.5&-4
\end{bmatrix}
\]

Applying ReLU elementwise gives

\[
\mathbf H=
\begin{bmatrix}
1.5&1.5&0\\
0&2.5&0
\end{bmatrix}
\]

The output-layer calculation gives

\[
\mathbf Y
=
\begin{bmatrix}
1.75\\
-2.25
\end{bmatrix}
\]

### Meaning of the result

The shape changes from `(2, 2)` to `(2, 3)` as the hidden dimension increases, then decreases to `(2, 1)`. Batch size 2 remains unchanged through all layers. The third hidden neuron receives negative pre-activation for both samples and therefore has activation zero.

## Example 2. Counting parameters

The first layer has $3\times2$ weights and a bias of length 3, giving $6+3=9$ parameters. The second has $1\times3$ weights and a bias of length 1, giving 4. The total is

\[
9+4=13
\]

An activation tensor is a value produced during the forward pass, not a trainable parameter of this MLP.

## Execution exercise

### Execution environment and sources

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Verification date: 2026-10-01
- Component category: `Stable core`
- Example ID: `n05_03_mlp_forward`
- Source code: `labs/N05/n05_03_mlp_forward.py`
- Test: `tests/N05/test_n05_03.py`
- Run command: `.venv\Scripts\python.exe -m labs.N05.n05_03_mlp_forward`

### Resource budget

This example uses batch size 2, input dimension 2, hidden dimension 3, output dimension 1, and 13 parameters. It has 0 training steps and a hard timeout of 10 seconds.

### Actual code and execution results

The site build inserts the direct tensor-operation code and actual execution results at the location below.

<!-- N05_EXAMPLE: n05_03_mlp_forward -->

### Shape checks

In the execution results, `pre_activation` and `hidden` have shape `[2, 3]`, while `output` has shape `[2, 1]`. The first axis remains the batch axis; only the second changes according to each layer's output dimension.

### Gradient checks

The example uses $\mathcal L=\sum_{b=1}^{2}Y_{b1}$. Among the automatic-differentiation results, we can check

\[
\frac{\partial\mathcal L}{\partial\mathbf W_2}
=
\begin{bmatrix}
1.5&4&0
\end{bmatrix}
\]

This is the sum of both samples' hidden activations along the batch axis. Tests compare the first-layer weights and biases, second-layer weights and biases, and input gradients against hand-calculated values.


The joining paths show each sample's derivative contribution being added to the same shared W₂.

<figure class="lesson-figure" markdown="1">

![Two hidden activation rows each contribute to the shared output weight gradient and add componentwise to one point five four zero](../../figures/assets/N05/N05-03-batch-gradient-sum.svg)

<figcaption>For L = Y₁ + Y₂, each output's upstream derivative is 1. Add contributions (1.5, 1.5, 0) and (0, 2.5, 0) from the two samples using the same W₂ to obtain one weight gradient (1.5, 4, 0).</figcaption>

</figure>

## Connection to model interpretation

One row of $\mathbf H$ contains one sample's hidden activations; one column collects the values produced by one hidden unit across samples in the batch. Selecting the wrong axis in model-interpretation code swaps comparisons of samples and comparisons of neurons.

Recovering information from hidden activations shows a relation between the representation and the target. A claim that the output layer actually uses that information requires intervention evidence checking how $\mathbf Y$ changes when $\mathbf H$ is changed.


Row and column selections collect different objects.

<figure class="lesson-figure" markdown="1">

![The same hidden matrix is shown with a sample row outlined and a neuron column outlined to distinguish axis selections](../../figures/assets/N05/N05-03-hidden-row-column.svg)

<figcaption>Read the same H by selecting its first row above and its first column below. A row contains all hidden values for one sample; a column contains values produced by one neuron across samples.</figcaption>

</figure>

## Common misconceptions

### Misconception 1. Weight-matrix shape is always input dimension by output dimension

This book stacks neurons' weights as rows, giving $\mathbf W\in\mathbb R^{d_{\mathrm{out}}\times d_{\mathrm{in}}}$. Multiplication with row batches uses $\mathbf X\mathbf W^\top$. Other implementation conventions are possible, so check equation shapes together with code shapes.

### Misconception 2. ReLU performs matrix multiplication

ReLU is applied independently to each element. Matrix multiplication in the surrounding affine layers mixes features.

### Misconception 3. Hidden dimension is batch size

The batch axis lists different samples; the hidden axis lists neuron outputs within one sample. Their meanings differ even though both are small integers in this example.

## Exercises

### 1. Tracing shapes

For $B=2$, $d_{\mathrm{in}}=4$, $d_{\mathrm{hidden}}=6$, and $d_{\mathrm{out}}=3$, state the shapes of $\mathbf X,\mathbf W_1,\mathbf Z_1,\mathbf H,\mathbf W_2,\mathbf Y$.

<details>
<summary>Show solution</summary>

They are $\mathbf X:(2,4)$, $\mathbf W_1:(6,4)$, $\mathbf Z_1:(2,6)$, $\mathbf H:(2,6)$, $\mathbf W_2:(3,6)$, and $\mathbf Y:(2,3)$.

</details>

### 2. Parameter count

How many parameters does the previous MLP have if both layers use bias?

<details>
<summary>Show solution</summary>

The first layer has $6\cdot4+6=30$, and the second has $3\cdot6+3=21$, for a total of 51. Batch size does not affect the parameter count.

</details>

### 3. Broadcasting

In $\mathbf Z_1=\mathbf X\mathbf W_1^\top+\mathbf b_1$, along which direction is the bias $\mathbf b_1$ of length $d_{\mathrm{hidden}}$ repeated?

<details>
<summary>Show solution</summary>

The same bias vector is added to each batch row. Biases can differ across hidden positions, but no separate bias parameters are assigned per sample.

</details>

### 4. Elementwise activation

If $\mathbf Z_1$ has shape `(5, 7)`, state the shape and maximum number of elements of $\mathbf H$ after elementwise ReLU.

<details>
<summary>Show solution</summary>

The shape remains `(5, 7)` with $5\cdot7=35$ elements. Turning a value into zero does not remove its position.

</details>

### 5. Interpreting one row

What do the first row and first column of $\mathbf H$ collect, respectively?

<details>
<summary>Show solution</summary>

The first row is a vector containing all hidden-unit activations for the first sample. The first column is a vector collecting the first hidden unit's activations across all samples in the batch.

</details>

### 6. Critiquing a claim

A probe recovers labels from $\mathbf H$ with high accuracy. Does it immediately follow that “the MLP output uses this information”?

<details>
<summary>Show solution</summary>

No. The probe result shows that label-related information can be recovered from $\mathbf H$. Whether the output functionally uses it must be tested separately through interventions on hidden activations, output changes, and appropriate controls.

</details>

## Lesson summary

- Stacking neurons' weights as rows lets one matrix multiplication calculate multiple neurons.
- The row-batch convention uses $\mathbf X\mathbf W^\top+\mathbf b$.
- Elementwise activation preserves shape but changes values and gradient paths.
- Hidden dimension and the batch axis have different meanings.
- Correctly identifying intermediate-activation axes is necessary for aggregating model-interpretation results appropriately.

## Pass criteria

You pass when you can answer these questions without consulting the material:

- Can you state every tensor shape in a two-layer MLP?
- Can you turn one neuron's equation into a batch matrix expression?
- Can you explain the direction of bias broadcasting?
- Can you distinguish parameters from intermediate activations?
- Can you explain what rows and columns of hidden activations mean?

## Next lesson

- [N05-04 Activation functions and gating](N05-04-activation-functions-gating.md)

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] All new symbols are defined before use.
- [x] Batch and feature axes are distinguished.
- [x] The weight-matrix convention is stated.
- [x] Forward calculations, parameter counts, and gradients are checked.
- [x] Every exercise has a solution.
- [x] Strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and math rendering are checked.
- [x] Execution code is not manually duplicated in Markdown.
- [x] Source-code and test paths, resource budgets, and verification dates are recorded.
- [x] Shape, numerical-value, and gradient tests are provided.
