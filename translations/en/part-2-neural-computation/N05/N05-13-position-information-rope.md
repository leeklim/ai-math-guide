---
id: "N05-13"
title: "Position information and RoPE"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-12"
  - "M02-03"
estimated_time: "120–150 minutes"
---

# N05-13. Position information and RoPE

## Why this lesson matters

Self-attention calculations over a set of tokens alone have difficulty distinguishing sequence order. Models introduce order information by adding absolute embeddings or rotating queries and keys depending on position. The N05 reference model uses RoPE.

## Learning objectives

- Distinguish content representations from position information.
- Calculate a two-dimensional vector rotation.
- Explain how RoPE uses different frequencies for different feature pairs.
- Check that rotation preserves norms and same-position dot products.
- Distinguish the rotary fraction in Pythia's configuration from the full hidden dimension.

## Prerequisite check

- Prerequisite lesson: [N05-12 Embedding and unembedding](N05-12-embedding-unembedding.md)
- Prerequisite lesson: [M02-03 Inner product, length, and angle](../../part-1-foundations/M02/M02-03-inner-product-length-angle.md)
- Check: Can you multiply a two-dimensional rotation matrix by a vector?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $p$ | `p` | Token position | Nonnegative integer |
| $\omega_j$ | `omega sub j` | Angular frequency for feature pair $j$ | Positive scalar |
| $R(p\omega_j)$ | `R of p omega sub j` | Rotation matrix at position $p$ | $\mathbb R^{2\times2}$ |
| RoPE | `R o P E` | Rotary position embedding | Query-key pair rotation |
| rotary fraction | `rotary fraction` | Fraction of the head dimension to which RoPE is applied | $[0,1]$ |

## Core concept 1. Position information can enter in different ways

Learned absolute position embeddings add a position vector to the token embedding. Sinusoidal encoding adds a sine-cosine vector with fixed frequencies. RoPE rotates attention's query and key feature pairs.

All three represent position, but differ in parameters, extrapolation, and the path through which they enter attention scores.

In embedding lookup alone, the same token ID receives the same vector at every position. Absolute methods add a position-specific vector to change subsequent layers' inputs. Rather than adding a separate vector to the input embedding, RoPE applies position-dependent rotations to the vectors used in the query-key comparison introduced in a later lesson. Content values and the positions at which they are compared enter through different computations.

Compare where position information enters through addition or rotation along the calculation paths.

<figure class="lesson-figure" markdown="1">

![Absolute position vectors are added to token embeddings before later computation while rotary positions act on projected queries and keys before their dot product](../../figures/assets/N05/N05-13-position-paths.svg)

<figcaption>The upper absolute-position path sends the sum of embedding and position vectors to subsequent computation. The lower RoPE path inserts position-specific rotations after Q/K projection and before the dot product. This is not an architecture diagram instructing simultaneous use of both positional methods.</figcaption>
</figure>

## Core concept 2. RoPE rotates two-dimensional pairs

\[
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}
\]

For pair $\mathbf x_j$ at position $p$, apply $R(p\omega_j)\mathbf x_j$. Rotation satisfies

\[
\|R(\theta)\mathbf x\|_2=\|\mathbf x\|_2
\]

The rotated components of pair $\mathbf x_j=(a,b)$ are $(a\cos(p\omega_j)-b\sin(p\omega_j),\ a\sin(p\omega_j)+b\cos(p\omega_j))$. Rotation mixes the two coordinates within a pair, not coordinates from different pairs. Advancing position by one increases pair $j$'s angle by $\omega_j$; pairs with different frequencies rotate at different rates. This is not adding the same number to every vector component.

Since $R(\theta)^\top R(\theta)=I$, the squared length after rotation is $\mathbf x^\top R^\top R\mathbf x=\mathbf x^\top\mathbf x$. These results can be added over multiple pairs. Rotating only some dimensions while leaving others unchanged also preserves the full norm, although direction can change.

Follow which two components rotate together and which boundaries they do not cross.

<figure class="lesson-figure" markdown="1">

![Four input features one zero zero one split into pairs one zero and zero one rotate independently at angles one and zero point zero one and join as four output components without cross-pair mixing](../../figures/assets/N05/N05-13-independent-pairs.svg)

<figcaption>Split the example's four coordinates into two pairs, rotate each, then concatenate them in the same order. At p = 1, the first pair uses 1 rad and the second 0.01 rad. Components mix within each pair, but are not exchanged across the two pairs.</figcaption>
</figure>

## Core concept 3. The attention dot product contains relative position

For a pair with the same frequency,

\[
(R(p\omega)\mathbf q)^\top(R(r\omega)\mathbf k)
=\mathbf q^\top R((r-p)\omega)\mathbf k
\]

The difference between the two absolute-position rotations enters the dot product. This is the central structure through which RoPE reflects relative displacement in attention scores.

A transposed rotation rotates by the opposite angle, so $R(p\omega)^\top=R(-p\omega)$. Composing it with the key's rotation gives $R(-p\omega)R(r\omega)=R((r-p)\omega)$. At the same query and key position, the difference is zero and the original dot product remains. At different positions, a relative angle remains. Preserving both vector norms alone does not preserve their dot product.

The statement that only relative position remains concerns this rotation term with content vectors $\mathbf q,\mathbf k$ fixed. Actual model queries and keys also vary with the input and preceding layers' computations. It does not mean the full attention score or model output is determined solely by the position difference.

## Example

Set the two pairs' frequencies to $(1,0.01)$ and rotate vector $(1,0,0,1)$ at positions 0 and 1. Position 0 leaves it unchanged; position 1 gives

\[
(\cos1,\sin1,-\sin0.01,\cos0.01)
\]

The norm is $\sqrt2$ at both positions. Rotating the two vectors at the same position preserves dot product 2; with a position difference of 1, it becomes approximately 1.5403.

Compare the first pair's direction and length on the unit circle.

<figure class="lesson-figure" markdown="1">

![Unit circle with grid shows pair one rotating from one zero to cosine one sine one while both arrows have length one](../../figures/assets/N05/N05-13-pair-one-rotation.svg)

<figcaption>The original first-pair vector and its rotation at p = 1 reach the same unit circle. Direction changes by 1 rad while the pair norm remains 1; the coordinates are approximately (0.5403, 0.8415).</figcaption>
</figure>

The two panels for the second pair use the same scale without exaggerating its small rotation angle.

<figure class="lesson-figure" markdown="1">

![Two vertically separated unit-circle panels show original zero one and rotated minus sine zero point zero one cosine zero point zero one with the true small angle and unchanged unit norm](../../figures/assets/N05/N05-13-pair-two-small-angle.svg)

<figcaption>Both panels use the same axis scale. The small 0.01 rad rotation is shown at its actual size, so the directions look almost identical. The second pair changes from (0, 1) to approximately (−0.0100, 0.99995), retaining pair norm 1.</figcaption>
</figure>

The projection reads a key at a different relative position along the query direction.

<figure class="lesson-figure" markdown="1">

![Unit query along the horizontal axis and key rotated one radian have a dashed projection at cosine one equal to zero point five four zero three showing dot product is not the norm](../../figures/assets/N05/N05-13-relative-dot-projection.svg)

<figcaption>Fix the first pair's content and compare query position 0 with key position 1. Both norms are 1, but the key's component along the query direction is cos 1 ≈ 0.5403. This differs from dot product 1 when both vectors rotate at the same position.</figcaption>
</figure>

Read each pair's dot-product contribution separately in the bars, then add them.

<figure class="lesson-figure" markdown="1">

![Grouped bars for two feature pairs compare same-position dot contributions one one against relative contributions cosine one and cosine zero point zero one which sum to one point five four zero three](../../figures/assets/N05/N05-13-pair-dot-contributions.svg)

<figcaption>The left bars show same-position contributions; the right bars show contributions at position difference 1. Summing the pairs' dot products gives 2 and cos 1 + cos 0.01 ≈ 1.5403. Equal vector norms √2 and preservation of their dot product are different conditions.</figcaption>
</figure>

## Execution exercise

### Execution environment and sources

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Verification date: 2026-10-01
- Component category: `Instructional reference`
- Example ID: `n05_13_rope`
- Source code: `labs/N05/n05_13_rope.py`
- Test: `tests/N05/test_n05_13.py`
- Run command: `.venv\Scripts\python.exe -m labs.N05.n05_13_rope`

### Resource budget

The example uses sequence length 2 and model dimension 4. It has 0 parameters and 0 training steps.

### Actual code and execution results

<!-- N05_EXAMPLE: n05_13_rope -->

### Checks

Tests check rotated values, norm preservation, same-position dot products, and relative-position dot products.

## Comparison with public configurations

Pythia's public training configuration records `pos-emb: rotary` and `rotary-pct: 0.25`. The Hugging Face configuration also records `rotary_pct: 0.25` and base 10000. It would be incorrect to say that Pythia applies RoPE to the entire head dimension. The N05 tiny reference implementation rotates all four dimensions to simplify the calculation.

Count the rotary fraction as dimensions within the head.

<figure class="lesson-figure" markdown="1">

![Sixty-four cells for one attention head contain sixteen rotary cells and forty-eight unchanged cells so fraction one quarter counts within the head not whole hidden dimension](../../figures/assets/N05/N05-13-partial-head-dimensions.svg)

<figcaption>Showing the problem's head dimension 64 as position cells, fraction 0.25 corresponds to 16 dimensions, or 8 pairs. The remaining 48 dimensions do not receive this rotation. Highlighting the first 16 cells explains the count; it does not specify an actual pairing convention.</figcaption>
</figure>

## Connection to model interpretation

Query and key activations after RoPE contain both content and position-dependent rotation. Direct cosine comparison between vectors at different positions includes the rotation effect.

Analyses removing or aligning position effects need the RoPE convention, rotary dimension, and frequencies used. Norm preservation alone does not establish preservation of semantic content.

## Common misconceptions

### Misconception 1. RoPE adds a vector to token embeddings

Reference RoPE rotates query and key feature pairs. Its calculation location differs from absolute position embedding addition.

### Misconception 2. A norm-preserving rotation leaves the representation identical

The norm agrees, but direction and dot products with other vectors change.

### Misconception 3. Every model rotates every head dimension

Rotary fractions and pairing conventions vary across architectures. Check configuration and implementation.

## Exercises

### 1. Position 0

What is $R(0)\mathbf x$?

<details><summary>Show solution</summary>

$R(0)$ is the identity matrix, so the result is $\mathbf x$.

</details>

### 2. Quarter turn

Calculate $R(\pi/2)(1,0)$.

<details><summary>Show solution</summary>

It is $(0,1)$.

</details>

### 3. Norm

Explain why the norm is preserved after rotation.

<details><summary>Show solution</summary>

Since $R^\top R=I$, $\|R\mathbf x\|^2=\mathbf x^\top R^\top R\mathbf x=\|\mathbf x\|^2$.

</details>

### 4. Rotary dimension

For head dimension 64 and rotary fraction 0.25, how many dimensions rotate?

<details><summary>Show solution</summary>

$64\cdot0.25=16$ dimensions. The implementation requires an even dimension to form pairs.

</details>

### 5. Configuration comparison

How should the rotary-fraction difference between the tiny exercise and Pythia be recorded?

<details><summary>Show solution</summary>

Distinguish rotation of all 4 dimensions in the tiny exercise from rotation of 25% of the head dimension in Pythia.

</details>

### 6. Critiquing a claim

Evaluate the conclusion that attention scores agree because norms agree before and after RoPE.

<details><summary>Show solution</summary>

Scores are query-key dot products. Rotations at different positions change the relative angle, so scores can change even with identical norms.

</details>

## Sources and update boundaries

The definition and relative-position property follow [RoFormer](https://arxiv.org/abs/2104.09864). For the Pythia comparison, the rotary settings were checked in the [public training configuration](https://github.com/EleutherAI/pythia/blob/main/models/14M/pythia-14m.yml). This lesson only prepares to apply RoPE to queries and keys in the subsequent attention calculation.

## Lesson summary

- Position information introduces token order into the calculation.
- RoPE rotates feature pairs by position-dependent angles.
- Rotation preserves norms and same-position dot products.
- Query-key dot products contain relative displacement.
- Check rotary fractions and conventions in configuration.

## Pass criteria

- Can you distinguish where the three position methods act in the calculation?
- Can you calculate a two-dimensional RoPE rotation?
- Can you explain norm preservation and relative dot products?
- Can you obtain the number of affected dimensions from a rotary fraction?
- Can you explain cautions when comparing RoPE activations?

## Next lesson

- [N05-14 Query, key, and value](N05-14-query-key-value.md)

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] Absolute addition and rotary calculations are distinguished.
- [x] Norms and dot products are checked.
- [x] Differences between public configuration and the tiny exercise are recorded.
- [x] Every exercise has a solution.
- [x] Strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and math rendering are checked.
- [x] Execution code is not manually duplicated in Markdown.
- [x] Source-code and test paths, resource budgets, and verification dates are recorded.
- [x] Shape, numerical-value, and gradient tests are provided.
