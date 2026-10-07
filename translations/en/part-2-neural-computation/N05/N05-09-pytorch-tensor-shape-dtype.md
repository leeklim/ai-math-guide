---
id: "N05-09"
title: "PyTorch tensors, shape, and dtype"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-08"
estimated_time: "120–150 minutes"
---

# N05-09. PyTorch tensors, shape, and dtype

## Why this lesson matters

Vectors and matrices in equations become tensors in code. Adding a batch axis or inserting a singleton axis changes operation rules even for the same symbol. Dtype determines how mathematical values are approximated and how much memory they occupy.

This lesson calculates an affine layer with `matmul`, transpose, and broadcasting. We change shapes with `unsqueeze` and compare cancellation in float32 and float64.

## Learning objectives

After this lesson, you will be able to:

- Match PyTorch tensor shapes and axis meanings to equations.
- Check the contracting dimension in matrix multiplication.
- Determine broadcasting compatibility using the trailing-axis rule.
- Distinguish the roles of `unsqueeze`, transpose, and reshape.
- Interpret rounding differences across dtypes.

## Prerequisite check

- Prerequisite lesson: [N05-08 Momentum, AdamW, and optimizer state](N05-08-momentum-adamw-optimizer-state.md)
- Check: Can you find the result shape of $(B,d)(d,h)$?
- Check: Can you explain why float32 cannot store every real number exactly?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| `shape` | `shape` | Tuple listing axis lengths in order | For example, `(B, d)` |
| `dtype` | `data type` | Numerical representation format of elements | For example, `float32` |
| $\mathbf X$ | `X` | Row-batch input | $\mathbb R^{B\times d_{\mathrm{in}}}$ |
| $\mathbf W$ | `W` | Weight matrix with output units stacked as rows | $\mathbb R^{d_{\mathrm{out}}\times d_{\mathrm{in}}}$ |
| $\mathbf b$ | `b` | Bias added along the output axis | $\mathbb R^{d_{\mathrm{out}}}$ |
| `unsqueeze` | `unsqueeze` | Operation inserting an axis of length 1 | Element count stays unchanged |
| broadcasting | `broadcasting` | Rule for operating on tensors expanded along compatible axes | Compare from trailing axes |

## Core concept 1. Read shape together with axis meanings

With inputs arranged as row batches, the affine layer is

\[
\mathbf Y=\mathbf X\mathbf W^\top+\mathbf b
\]

The shape flow is

\[
(B,d_{\mathrm{in}})(d_{\mathrm{in}},d_{\mathrm{out}})
\longrightarrow(B,d_{\mathrm{out}})
\]

In code's `inputs @ weight.T`, `.T` swaps the weight's two axes.

Along the contracting input axis, matching values are multiplied and summed, while batch and output axes remain. Even if $B$ and $d_{\mathrm{out}}$ happen to be the same number, their axes do not have the same meaning. In this expression, the first axis represents samples, and the second represents output units. After checking the shape's numbers, also check which input each axis came from.


Trace feature correspondences between a selected sample row and an output column.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Input sample row one two three and transposed weight column one zero minus one contract to result entry minus two while sample and output axes remain](../../figures/assets/N05/N05-09-contract-feature-axis.svg)

<figcaption>This is Example 1's matrix multiplication before adding bias. One sample row of X and one output column of Wᵀ match at three feature positions to produce −2. Result rows represent samples, and columns represent output units.</figcaption>

</figure>

## Core concept 2. Broadcasting aligns axes from the end

Adding bias of shape $(d_{\mathrm{out}},)$ to a tensor of shape $(B,d_{\mathrm{out}})$ matches the final axis. Since the bias has no batch axis, the same vector is added to every batch row.

Comparing axes from the end, broadcasting is possible when the sizes agree, one size is 1, or an axis is absent on one side. Broadcasting represents mathematical repetition, but the implementation need not make an actual data copy.

Treating absent leading axes as length 1 makes result-axis lengths easier to determine. Bias $(d_{\mathrm{out}},)$ aligns as $(1,d_{\mathrm{out}})$ and repeats along the batch direction. Conversely, adding one number per sample requires shape $(B,1)$, repeating along the output direction. Using only $(B,)$ aligns with the last axis, so when $B=d_{\mathrm{out}}$, the code can execute without performing the intended per-sample addition.


Compare repetition directions by rows and columns.

<figure class="lesson-figure" markdown="1">

![Row-shaped offsets repeat across samples while column-shaped offsets repeat across output positions](../../figures/assets/N05/N05-09-row-versus-column-offset.svg)

<figcaption>Assigning (0.25, −0.5) as output-specific numbers repeats the same row for each sample. Sample-specific numbers require (2, 1), repeating the same number within each row. Since B and d_out both equal 2, the wrong direction can also execute.</figcaption>

</figure>


Determine each axis length after aligning from the right.

<figure class="lesson-figure" markdown="1">

![Trailing axis alignment compares shapes two one four and padded one three four yielding broadcast output two three four](../../figures/assets/N05/N05-09-trailing-broadcast.svg)

<figcaption>Pad the second tensor's absent leading axis with 1 to compare it as (1, 3, 4). In each column, equal sizes or a size 1 permit using the larger length, giving result (2, 3, 4). This is not a rule comparing total element counts alone.</figcaption>

</figure>

## Core concept 3. Shape operations interpret element arrangements

`unsqueeze(1)` changes $(B,d)$ into $(B,1,d)$. The new axis has length 1, with the same element count. Transpose changes axis order. Reshape groups the same elements into different axis lengths while preserving their total count.

Identical shape does not make axis meanings identical. `(B, T, d)` and `(T, B, d)` have the same element count, but swap batch and token positions.

Even if transpose and reshape produce the same shape, they need not place the same values at the same positions. Transposing a matrix whose rows are $(1,2,3)$ and $(4,5,6)$ gives first row $(1,4)$. Regrouping the six row-ordered values into $(3,2)$ instead gives first row $(1,2)$. Distinguish exchanging axis roles from regrouping elements listed in order.


Read the same elements again after inserting a new index of length 1.

<figure class="lesson-figure" markdown="1">

![A two by three tensor becomes two batches each containing one row of three unchanged values under unsqueeze one](../../figures/assets/N05/N05-09-unsqueeze-index.svg)

<figcaption>Insert an intermediate axis of length 1 at each of the two existing batch positions. Its only index is 0; value 3 at (0, 2) is now read at (0, 0, 2). No elements are duplicated.</figcaption>

</figure>


Compare the positions occupied by the same number 4 after the two shape operations.

<figure class="lesson-figure" markdown="1">

![Source values one through six map to transposed rows one four two five three six versus reshaped rows one two three four five six](../../figures/assets/N05/N05-09-transpose-reshape.svg)

<figcaption>Track 4, originally in the first position of the source's second row. Transpose places it in the second position of the first row; row-ordered reshape places it in the second position of the second row. Even with matching shape (3, 2), position correspondences differ.</figcaption>

</figure>

## Core concept 4. Dtype affects numerical results

Float32 and float64 approximate the same real numbers with different precision. Calculating with large and small numbers together can lose small values to rounding. Operation order also affects results.

Do not interpret dtype differences as differences in a model's concepts. First check whether the same mathematical function agrees within tolerance.

Floating-point representation does not store numbers at a constant absolute spacing regardless of their magnitude. Near large numbers, adjacent representable values are also farther apart, allowing a small increment to round back to the same value. Subtracting those values later cancels the large part without recovering the small increment. Casting a value already lost in float32 to float64 cannot restore it. Higher precision can reduce rounding when used from the start of the calculation, but still does not perform exact real-number arithmetic.


Distinguish the intended increment from the spacing between representable neighbors.

<figure class="lesson-figure" markdown="1">

![Float32 representable neighbors at offsets minus eight zero eight surround requested offset plus one which rounds to zero offset](../../figures/assets/N05/N05-09-float-neighbors.svg)

<figcaption>Actual float32 neighbors of 10⁸ are spaced by 8. The orange mark is the intended increment +1; blue points are representable values. After adding +1, the nearest stored value is still the original 10⁸, so the increment is lost.</figcaption>

</figure>

## Example 1. Affine shapes and values

With

\[
\mathbf X=\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix},
\quad
\mathbf W=\begin{bmatrix}1&0&-1\\0.5&0.5&0.5\end{bmatrix},
\quad
\mathbf b=(0.25,-0.5)
\]

the shape of $\mathbf X\mathbf W^\top$ is $(2,2)$. Broadcasting the bias gives

\[
\mathbf Y=\begin{bmatrix}-1.75&2.5\\-1.75&7.0\end{bmatrix}
\]

## Example 2. Cancellation

Adding $(10^8,1,-10^8)$ in order gives 0 in the float32 example and 1 in the float64 example. In float32, 1 is lost when $10^8+1$ is stored. This example shows that real addition's associative law does not carry over unchanged to finite-precision calculation.


Check when rounding occurs and the results of later casting and subtraction.

<figure class="lesson-figure" markdown="1">

![Float32 rounds one hundred million plus one back to one hundred million then subtracts to zero while float64 from the start retains the increment and yields one](../../figures/assets/N05/N05-09-cancellation-cast.svg)

<figcaption>The same addition is stored as 10⁸ in float32, but as 100000001 when calculated in float64 from the start. Subsequent subtraction of 10⁸ gives 0 and 1, respectively. Casting the rounded float32 value 10⁸ to float64 later leaves the stored value unchanged.</figcaption>

</figure>

## Execution exercise

### Execution environment and sources

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Verification date: 2026-10-01
- Component category: Tensor calculation is `Stable core`; broadcasting implementation is framework semantics.
- Example ID: `n05_09_tensor_shape_dtype`
- Source code: `labs/N05/n05_09_tensor_shape_dtype.py`
- Test: `tests/N05/test_n05_09.py`
- Run command: `.venv\Scripts\python.exe -m labs.N05.n05_09_tensor_shape_dtype`

### Resource budget

The example uses batch size 2, input dimension 3, output dimension 2, and 8 parameters. It has 0 training steps and a hard timeout of 10 seconds.

### Actual code and execution results

<!-- N05_EXAMPLE: n05_09_tensor_shape_dtype -->

### Shape, numerical-value, and gradient checks

Tests check affine output $(2,2)$, `unsqueeze` output $(2,1,3)$, and the input gradient. Cancellation results are checked separately for each dtype.

## Connection to model interpretation

The most common error in activation analysis is swapping batch, token, head, and feature axes. When saving hook results, record an axis schema alongside the tensor name and shape.

If attribution values change after changing precision, first check numerical error and threshold sensitivity. A reproducible difference alone does not establish that the model uses a different feature.

## Common misconceptions

### Misconception 1. Equal element counts permit elementwise operations

PyTorch aligns axes by broadcasting rules. Shapes `(2,3)` and `(6,)` have equal element counts but are incompatible for elementwise addition.

### Misconception 2. `unsqueeze` duplicates values

`unsqueeze` inserts an axis of length 1. Both values and element count remain unchanged.

### Misconception 3. Higher-precision results are exact real-number values

Float64 is also a finite-precision approximation. It simply stores more significant digits than float32.

## Exercises

### 1. Matmul shape

For `X.shape=(4,3)` and `W.shape=(5,3)`, find the shape of `X @ W.T`.

<details><summary>Show solution</summary>

`W.T` has shape `(3,5)`, so the result is `(4,5)`.

</details>

### 2. Bias broadcasting

A tensor of shape `(4,5)` receives a bias of shape `(5,)`. Along which axis is the bias repeated?

<details><summary>Show solution</summary>

Length 5 matches the last axis, and the same bias is applied to four batch rows.

</details>

### 3. Unsqueeze

Starting with shape `(2,3)`, state the shapes obtained by applying `unsqueeze(0)` and `unsqueeze(1)` separately.

<details><summary>Show solution</summary>

They are `(1,2,3)` and `(2,1,3)`, respectively.

</details>

### 4. Assessing broadcasting

Are `(2,1,4)` and `(3,4)` compatible for broadcasting?

<details><summary>Show solution</summary>

Yes. From the end, 4 matches 4, one of 1 and 3 is 1, and the second tensor has no axis corresponding to the first tensor's 2. The result shape is `(2,3,4)`.

</details>

### 5. Dtype experiment

Does casting a float32 tensor to float64 restore information already lost?

<details><summary>Show solution</summary>

No. Casting moves the current float32 value into a wider representation. The original input must be created in float64 for the calculation to delay rounding.

</details>

### 6. Critiquing a claim

Evaluate the conclusion that two hook tensors have the same representation because their shapes agree.

<details><summary>Show solution</summary>

Shape describes only element arrangement. Hook locations, axis meanings, values, and bases can differ, so identical representation does not follow.

</details>

## Sources and update boundaries

Broadcasting decisions follow the trailing-axis rule in [PyTorch broadcasting semantics](https://docs.pytorch.org/docs/stable/notes/broadcasting.html). A mathematical affine map and a framework's memory layout are not the same concept.

## Lesson summary

- Read tensor shape together with axis meanings.
- Matrix multiplication contracts the matching dimension.
- Broadcasting checks compatibility from trailing axes.
- Shape transformations and dtype transformations are different operations.
- Finite precision introduces numerical error into values and gradients.

## Pass criteria

- Can you state every shape in an affine calculation?
- Can you determine broadcasting compatibility and result shape?
- Can you distinguish `unsqueeze`, transpose, and reshape?
- Can you explain the numerical effects of dtype differences?
- Can you critique an activation comparison lacking an axis schema?

## Next lesson

- [N05-10 Autograd, JVP, and VJP](N05-10-autograd-jvp-vjp.md)

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] Shape and axis meanings are distinguished.
- [x] Broadcasting rules are stated.
- [x] Numerical values for each dtype are checked.
- [x] Every exercise has a solution.
- [x] Strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and math rendering are checked.
- [x] Execution code is not manually duplicated in Markdown.
- [x] Source-code and test paths, resource budgets, and verification dates are recorded.
- [x] Shape, numerical-value, and gradient tests are provided.
