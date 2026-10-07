---
id: "N05-18"
title: "LayerNorm, RMSNorm, and residual order"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-17"
estimated_time: "120–150 minutes"
---

# N05-18. LayerNorm, RMSNorm, and residual order

## Why this lesson matters

The type and location of normalization change a block's equations, activation scales, and hook meanings. Treating `norm output`, `residual input`, and `block output` as the same thing leads to a misreading of the model structure.

## Learning objectives

- Calculate LayerNorm and RMSNorm for a small vector.
- Distinguish whether centering is performed and identify the learned parameters.
- Write pre-norm and post-norm block equations in computation order.
- Check the normalization axis and output shape.
- Explain the limitations of directly comparing activations at different normalization locations.

## Prerequisite check

- Prerequisite lesson: [N05-17 Residual stream](N05-17-residual-stream.md)
- Check question: Can you distinguish a sublayer output from the stream after residual addition?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\mu$ | `mu` | Feature mean of one token vector | scalar |
| $\sigma^2$ | `sigma squared` | Feature variance | nonnegative scalar |
| $\operatorname{RMS}(\mathbf x)$ | `the root mean square of x` | Square root of the feature mean square | nonnegative scalar |
| $\boldsymbol\gamma$ | `gamma` | Learned scale for each feature | $\mathbb R^{d_{model}}$ |
| pre-norm | `pre-norm` | An order applying normalization before the sublayer | architecture choice |
| post-norm | `post-norm` | An order applying normalization after residual addition | architecture choice |

## Core concept 1. LayerNorm

For a token vector $\mathbf x$ with feature dimension $d$, define

\[
\mu=\frac1d\sum_{j=1}^{d}x_j,
\qquad
\sigma^2=\frac1d\sum_{j=1}^{d}(x_j-\mu)^2
\]

Then

\[
\operatorname{LN}(\mathbf x)
=\boldsymbol\gamma\odot
\frac{\mathbf x-\mu\mathbf 1}{\sqrt{\sigma^2+\epsilon}}
+\boldsymbol\beta
\]

LayerNorm performs both centering and rescaling. The statistics are usually computed along the last feature axis of each token.

Here, $\boldsymbol\beta\in\mathbb R^d$ is a learned shift for each feature, and $\epsilon>0$ is a small constant protecting the denominator. The mean and variance are computed from the $d$ components of one token, without mixing values from other samples or tokens. The variance denominator $d$ means that the squared deviations of these components are averaged. This is not a problem of finding an unbiased estimator of a population variance, so do not replace it with $d-1$.

Below, the feature group enclosing each row shows the range over which statistics are computed.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two separate token rows compute their own feature mean and variance without mixing token statistics](../../figures/assets/N05/N05-18-token-feature-statistics.svg)

<figcaption>The three features of each token are grouped separately. The first row has mean 2 and the second has mean 4; their values are not mixed. With γ=1, β=0, and ε>0, the constant row becomes 0 after centering.</figcaption>
</figure>

The components of the centered vector sum to 0, and dividing by a common denominator leaves the mean at 0. Multiplying by feature-specific $\gamma_j$ and adding $\beta_j$ can change the final mean, however. If every input component is equal, both the centered vector and variance are 0, and the output of the equation above is $\boldsymbol\beta$. Distinguish the properties of the normalization intermediate from those after the learned affine transformation.

Isolating mean subtraction in two dimensions shows a displacement that removes the mean direction.

<figure class="lesson-figure" markdown="1">

![A two-coordinate vector projects to the zero-sum line by subtracting its mean in both coordinates](../../figures/assets/N05/N05-18-centering-projection.svg)

<figcaption>Subtracting μ=2 from both coordinates of x=(1,3) gives (−1,1). The purple arrow is the displacement (−2,−2), and the dashed line is where the two coordinates sum to 0. Variance rescaling has not yet been applied.</figcaption>
</figure>

## Core concept 2. RMSNorm

\[
\operatorname{RMS}(\mathbf x)
=\sqrt{\frac1d\sum_{j=1}^{d}x_j^2+\epsilon},
\qquad
\operatorname{RMSNorm}(\mathbf x)
=\boldsymbol\gamma\odot\frac{\mathbf x}{\operatorname{RMS}(\mathbf x)}
\]

Because the mean is not subtracted, the output mean is generally not 0. Whether a bias is used depends on the implementation, but the reference RMSNorm equation uses a learned scale.

The denominator above is a regularized RMS, with $\epsilon$ added to the mean square. When $\epsilon=0$, it equals the usual root mean square, and a nonzero input is required for division. In this case, before applying the learned scale, the output mean square is 1 and the Euclidean norm is $\sqrt d$. Adding a positive $\epsilon$ makes the mean square less than 1; after the learned scale, it also depends on the feature-specific multipliers. RMSNorm uses a common denominator for one vector without removing its mean.

Dividing by the RMS changes the length while preserving the direction from the origin.

<figure class="lesson-figure" markdown="1">

![RMS normalization scales a vector along the same ray to a circle of radius square root of two](../../figures/assets/N05/N05-18-rms-radius.svg)

<figcaption>This two-dimensional example uses γ=1 and ε=0. Dividing (1,3) by its RMS, √5, gives approximately (0.447,1.342). Its mean is not removed, and the result lies on the dashed circle of Euclidean norm √2, not 1.</figcaption>
</figure>

## Core concept 3. Residual order

Representative equations for one sublayer $F$ are

\[
\text{pre-norm:}\quad
\mathbf y=\mathbf x+F(\operatorname{Norm}(\mathbf x))
\]

\[
\text{post-norm:}\quad
\mathbf y=\operatorname{Norm}(\mathbf x+F(\mathbf x))
\]

Because the operation order differs, these generally are not the same function even with the same weights. The original Transformer used the post-norm equation, while pre-norm variants are also widely used in modern decoders. Check an actual model through its configuration and forward code.

In pre-norm, $F$ receives a normalized input, but the skip-path $\mathbf x$ is added without normalization. In post-norm, $F$ receives the original input, and the entire result of addition is normalized. Thus, the stream after addition in pre-norm need not be a normalized vector. The skip term in post-norm also passes through the final Norm, so its backward path cannot be read as just an identity term.

Applying both orders to the same toy sublayer changes both the location where the skip joins and the final numerical result.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Pre-norm and post-norm paths with the same half-scale sublayer yield different numeric outputs and different skip entry points](../../figures/assets/N05/N05-18-pre-post-norm.svg)

<figcaption>This example uses F(z)=z/2 and LayerNorm with γ=1, β=0, and ε small enough to ignore. In pre-norm, the original x bypasses Norm and is added at the end; in post-norm, the entire sum enters Norm.</figcaption>
</figure>

## Example

Let $\mathbf x=(1,2,3)$, $\gamma=1$, $\beta=0$, with only a small $\epsilon$. LayerNorm subtracts the mean of 2, giving approximately

\[
(-1.2247,0,1.2247)
\]

RMSNorm does not subtract the mean, giving approximately

\[
(0.4629,0.9258,1.3887)
\]

The two results have the same shape, but differ in the information they preserve and the basis for their scale.

Comparing the same feature coordinates in the example shows how centering appears in the signs and magnitudes.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Input, LayerNorm, and RMSNorm feature bars show the same three coordinates under different normalization operations](../../figures/assets/N05/N05-18-norm-components.svg)

<figcaption>The example's x=(1,2,3) is plotted on the same axis range. LayerNorm subtracts the mean of 2 and then scales, whereas RMSNorm divides the positive components by a common denominator. For comparison, γ=1, β=0, and ε=0 are idealized here.</figcaption>
</figure>

## Executable lab

### Environment and source

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Verification date: 2026-10-01
- Component category: `Common modern variant`
- Example ID: `n05_18_normalization_order`
- Source code: `labs/N05/n05_18_normalization_order.py`
- Tests: `tests/N05/test_n05_18.py`
- Run command: `.venv\Scripts\python.exe -m labs.N05.n05_18_normalization_order`

### Resource budget

The lab calculates only normalization and the order of a single sublayer, using batch size 1, two tokens, and model dimension 3.

### Actual code and execution results

<!-- N05_EXAMPLE: n05_18_normalization_order -->

### Checks

The tests check the LayerNorm output mean, the RMSNorm output mean square, and the difference between pre-norm and post-norm outputs.

## Epsilon and learned scale

$\epsilon$ prevents division by 0 when the variance or mean square is very small. Its default value and placement inside or outside the square root may differ across implementations, so numerical reproduction requires the exact equation. The RMS of the final output after applying $\gamma$ is generally not 1. The word `normalized` does not mean that every feature's absolute value or the norm is fixed.

Compare a learned affine transformation applied to the normalization intermediate separately from a case where ε is not small.

<figure class="lesson-figure" markdown="1">

![Different feature scales and shifts change the mean of an initially zero-mean LayerNorm vector](../../figures/assets/N05/N05-18-learned-affine.svg)

<figcaption>The normalization intermediate for x=(1,2,3) is transformed with γ=(1,1,2) and β=(1,0,0). The final mean, shown by the green dashed line, is approximately 0.742, not 0.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![Output mean square approaches one before learned scale but four after a common scale of two as input magnitude grows](../../figures/assets/N05/N05-18-epsilon-ratio.svg)

<figcaption>The RMSNorm denominator includes ε=0.01. When the input mean square is less than ε, the mean square after normalization is also much less than 1. Multiplying every feature by γ=2 then multiplies the mean square by four.</figcaption>
</figure>

## Connection to model interpretability

In a pre-norm model, a sublayer input hook sees a normalized activation, while a residual stream hook may see the stream before normalization. Their coordinates and scales differ, so do not compare them directly merely by calling both `hidden state`.

Changing one coordinate of a normalization input and recomputing Norm also changes the mean or common denominator, which can change other output coordinates. In contrast, directly patching one coordinate of the tensor after normalization does not recompute Norm. These interventions alter different computation locations, and the latter tensor may no longer satisfy the properties produced by the original normalization.

Below, compare the results of changing the same feature before and after normalization.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Patching a LayerNorm input and recomputing changes all output features whereas directly patching one output changes only that coordinate](../../figures/assets/N05/N05-18-norm-intervention.svg)

<figcaption>Starting from x=(1,2,3), changing the first input coordinate to 2 and recomputing LayerNorm changes all three output coordinates. In contrast, adding 1 to the first coordinate of the existing output leaves the other two unchanged and gives a mean of 0.333. This calculation uses γ=1, β=0, and ε=0.</figcaption>
</figure>

## Common misconceptions

### Misconception 1. RMSNorm also makes the mean 0

RMSNorm scales using the mean square but does not center.

### Misconception 2. Pre-norm and post-norm are just neater ways to write the same equation

The composition order of normalization and the nonlinear sublayer differs, changing the function and gradient paths.

### Misconception 3. Every token's Euclidean norm is always 1 after normalization

An RMS of approximately 1 before the learned scale is not the same as a Euclidean norm of 1. In dimension $d$, an RMS of 1 gives a norm of $\sqrt d$.

## Exercises

### 1. LayerNorm mean

Calculate the feature mean of $x=(2,4,6)$.

<details><summary>Show solution</summary>It is $(2+4+6)/3=4$.</details>

### 2. RMS

Calculate the RMS when $x=(3,4)$ and $\epsilon=0$.

<details><summary>Show solution</summary>It is $\sqrt{(9+16)/2}=\sqrt{12.5}$, which differs from the Euclidean norm of 5.</details>

### 3. Centering

Determine whether LayerNorm or RMSNorm subtracts the mean from $x=(1,2,3)$.

<details><summary>Show solution</summary>LayerNorm does.</details>

### 4. Pre-norm order

Write the pre-norm equation using only $x$, Norm, $F$, and addition symbols.

<details><summary>Show solution</summary>The equation is $y=x+F(\operatorname{Norm}(x))$.</details>

### 5. Diagnose the axis

For input shape `(batch, sequence, model)`, determine the statistics axis of per-token LayerNorm.

<details><summary>Show solution</summary>It is the last, model-feature axis. Batch and sequence values are not averaged together.</details>

### 6. Compare hooks

Can lower cosine similarity between the residual before normalization and the sublayer input after normalization establish that a feature has disappeared?

<details><summary>Show solution</summary>Not directly. Centering, rescaling, and the learned scale changed the coordinate values, so representations at the same location and behavior require additional examination.</details>

## Sources and update boundaries

The LayerNorm definition is based on [Layer Normalization](https://arxiv.org/abs/1607.06450), the original Transformer's residual order on [Attention Is All You Need](https://arxiv.org/abs/1706.03762), and the RMSNorm definition on [Root Mean Square Layer Normalization](https://arxiv.org/abs/1910.07467). Epsilon, bias, and normalization locations are architecture-specific details that must be checked in the model configuration and implementation.

## Lesson summary

- LayerNorm performs centering and rescaling.
- RMSNorm scales by the root mean square without subtracting the mean.
- Pre-norm and post-norm compute normalization at different locations.
- Epsilon and the learned scale prevent you from assuming idealized normalization properties unchanged.
- Check whether hook activations are before or after normalization before comparing them.

## Pass criteria

- Can you calculate both normalizations for a small vector?
- Can you explain whether centering is performed?
- Can you write the pre-norm and post-norm equations?
- Can you check the normalization axis and shape?
- Can you explain the limitations of comparing activations at different normalization locations?

## Next lesson

- [N05-19 Dense MLP, SwiGLU, and expert routing](N05-19-dense-mlp-swiglu-expert-routing.md)

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] LayerNorm, RMSNorm, and residual order are distinguished.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretability claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Knowledge beyond the prerequisites is not required without explanation.
- [x] Internal links and equation rendering are checked.
- [x] Executable code is not manually duplicated in Markdown.
- [x] Source-code and test paths, resource budgets, and the verification date are recorded.
- [x] Tests for normalization invariants and order are provided.
