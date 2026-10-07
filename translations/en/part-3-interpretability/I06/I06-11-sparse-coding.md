---
id: "I06-11"
title: "Sparse coding"
part: 3
stage: "I06"
status: "complete"
prerequisites: ["I06-10", "M01-04"]
estimated_time: "110~140 minutes"
---

# I06-11. Sparse coding

## Why this lesson matters

Sparse coding approximates a dense activation using a small number of dictionary features. Minimizing reconstruction error alone can use many coefficients, so a sparsity penalty is added. Do not assume that the dictionary and code are unique.

## Learning objectives

- Interpret an objective that combines reconstruction and sparsity.
- Iteratively update a sparse code for a fixed dictionary.
- Evaluate reconstruction error, active fraction, and dictionary coherence.
- Explain nonuniqueness and scale ambiguity in sparse solutions.

## Prerequisite check

- Prerequisite lessons: [I06-10 Superposition](I06-10-superposition.md), [M01-04 Derivatives and graphs](../../part-1-foundations/M01/M01-04-derivative-and-graphs.md)
- Check question: Does reconstruction change if a dictionary column is doubled and its coefficient is halved?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $\hat z$ | `z hat` | A sparse code estimated from a given activation | $\mathbb R^m$ |
| $\lVert a-Dz\rVert_2^2$ | `the squared reconstruction error` | Squared error between the original activation and its reconstruction | nonnegative scalar |
| $\lVert z\rVert_1$ | `the L one norm of z` | Sum of absolute coefficient values | nonnegative scalar |
| $\lambda$ | `lambda` | The tradeoff between reconstruction and sparsity | nonnegative scalar |
| soft thresholding | `soft thresholding` | A proximal operation that reduces small coefficients to 0 | elementwise map |
| $S_\tau(u)$ | `soft thresholding of u at tau` | A function that shrinks scalar $u$ at threshold $\tau$ | $\mathbb R\to\mathbb R$, $\tau\ge0$ |
| $\eta$ | `eta` | The reconstruction gradient step size | positive scalar |
| dictionary coherence | `dictionary coherence` | The maximum absolute inner product between distinct normalized columns | $[0,1]$ |

## 1. Find a code for a fixed dictionary

Given an activation $a$ and dictionary $D$, solve

\[
\hat z=\arg\min_z\frac12\lVert a-Dz\rVert_2^2+\lambda\lVert z\rVert_1
\]

The first term favors reconstruction, and the second favors sparse coefficients. With $\lambda=0$, only reconstruction is fitted; an excessively large value can make every code value 0.

The vector $Dz$ is the estimated activation, while $a-Dz$ is the residual left in input space. In contrast, $\lVert z\rVert_1$ sums absolute coefficients in feature space. Candidates with the same reconstruction can therefore have different costs if they use more or larger coefficients. This penalty does not directly count nonzeros. Specify separately the criterion for an active feature to interpret and the threshold below which a numerically small coefficient is treated as 0.

First, distinguish the spaces in which the two terms calculate their penalties.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An eight-feature code branches to an L1 magnitude cost and through a five by eight dictionary to a five-coordinate reconstruction and residual.](../../figures/assets/I06/I06-11-loss-spaces.svg)

<figcaption>The existing exercise's 8 features and 5 activation coordinates distinguish the spaces of the two costs. L₁ sums feature-coefficient magnitudes, while the residual remains in activation space. Do not read L₁ as a nonzero count.</figcaption>
</figure>

## 2. ISTA

The reconstruction term's gradient is

\[
\nabla_z\frac12\lVert a-Dz\rVert_2^2=D^T(Dz-a)
\]

Applying soft thresholding after a gradient step gives

\[
z^{(k+1)}=S_{\eta\lambda}\left(z^{(k)}-\eta D^T(Dz^{(k)}-a)\right)
\]

ISTA stands for iterative shrinkage-thresholding algorithm. Multiplying the residual $Dz-a$ by $D^T$ expresses how to reduce the error along each dictionary direction as a gradient in code space. The factor $1/2$ cancels the 2 from differentiating the square.

For a scalar, soft thresholding is

\[
S_\tau(u)=\operatorname{sign}(u)\max(\lvert u\rvert-\tau,0)
\]

Apply it coordinatewise to a vector. Values whose absolute magnitudes are at or below the threshold become 0; the rest shrink while keeping their signs. Each step therefore has two computations: move in a direction that reduces reconstruction error, then shrink coefficients by $\eta\lambda$. Since $L_1$ is not differentiable at 0, this threshold operation replaces a step formed by simply adding ordinary gradients of the two terms.

For a fixed dictionary with $D\ne0$, the spectral norm of $D^TD$ is the maximum rate at which the reconstruction gradient changes. Choosing $0<\eta\le1/\lVert D^TD\rVert_2$ permits a standard ISTA step for this convex objective. A larger $\eta$ increases both the penalty threshold and movement along the error direction, so do not choose the step by its threshold alone.

Examine the two stages of an iteration separately from the scalar threshold curve.

<figure class="lesson-figure" markdown="1">

![The current code takes a reconstruction gradient step and then an eta lambda soft threshold; the new code loops back under fixed activation and dictionary.](../../figures/assets/I06/I06-11-ista-two-step.svg)

<figcaption>An ISTA iteration applies an ηλ threshold after the reconstruction gradient step. Read both effects of η: it changes the gradient movement as well as the threshold.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![The exact tau point two soft-threshold curve has a zero plateau and shrinks positive and negative inputs; problem points map point one to zero, point five to point three, and minus point four to minus point two.](../../figures/assets/I06/I06-11-soft-threshold-curve.svg)

<figcaption>The curve uses the exercise's τ=0.2. The central interval becomes 0, while values on either side shrink without changing sign. The gray dashed line S(u)=u provides a comparison with no change.</figcaption>
</figure>

## 3. When the dictionary is learned too

Code and dictionary can be updated alternately. Constrain dictionary column norms to prevent scale ambiguity. Column permutations and sign or scale transformations can produce the same reconstruction, so feature IDs do not align automatically across training runs.

Increasing column $d_j$ and decreasing $z_j$ by the same factor leaves $d_jz_j$ unchanged but lowers the $L_1$ cost. Without constraints on column magnitude, this cost can be reduced without actually using fewer features. Finding a code with fixed $D$ also differs from learning both variables together. Alternating updates need not give the same dictionary or feature IDs across seeds.

Compare how changing scale alone can lower the cost of the same contribution.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Doubling a dictionary direction and halving its coefficient leaves their product unchanged while halving that coefficient's L1 cost; both direction lengths share a schematic grid.](../../figures/assets/I06/I06-11-dictionary-scale-cost.svg)

<figcaption>As in the exercise, doubling d_j and halving z_j preserves the contribution but lowers this coefficient's L₁ cost. Without a column-norm constraint, changing scale can reduce the cost without making the code sparser.</figcaption>
</figure>

## 4. Evaluation

At minimum, examine the following together.

- Reconstruction MSE or explained variance.
- The number of nonzeros $L_0$ per sample.
- The coefficient-magnitude distribution.
- Dictionary columns that are rarely used.
- Dictionary coherence.
- Stability across seeds, dictionary sizes, and $\lambda$.

Low reconstruction error alone does not establish that the features are interpretable.

Check reconstruction, code support, and the distinguishability of dictionary directions separately.

<figure class="lesson-figure" markdown="1">

![Two almost parallel normalized dictionary directions point into similar regions, making attribution to one or the other code ambiguous even when reconstruction is good.](../../figures/assets/I06/I06-11-coherent-columns.svg)

<figcaption>Nearly parallel columns can explain similar activations, making support difficult to distinguish. This schematic illustrates the angle between directions; it does not estimate the exercise's exact coherence of 0.99.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![The existing first synthetic input has two true nonzero coefficients but its fixed one hundred-step ISTA estimate spreads coefficients to additional directions, showing support need not match.](../../figures/assets/I06/I06-11-true-estimated-support.svg)

<figcaption>The true code for the first of the existing 24 CPU inputs is compared with its 100-step ISTA result. A good reconstruction approximation does not guarantee that the selected feature support matches the original code. Ground truth here is only the code used to generate synthetic inputs, not actual model features.</figcaption>
</figure>

## CPU exercise

Generate 5-dimensional activations from combinations of two of 8 dictionary columns. Estimate codes with ISTA for the fixed dictionary and record reconstruction and active fraction.

<!-- I06_EXAMPLE: i06_11_sparse_coding -->

Estimated codes may be less sparse than ground truth because dictionary coherence and the penalty affect support recovery.

## Common misconceptions

### Misconception 1. A sparse code is always unique

Similar dictionary columns or insufficient conditions on the objective can allow several codes to produce similar reconstructions.

### Misconception 2. $L_1$ is exactly the same as $L_0$

$L_1$ is a convex surrogate. Small nonzero coefficients may remain, so specify a threshold.

### Misconception 3. Good reconstruction means good feature meaning

Reconstruction is a fidelity metric. Human interpretability, stability, and downstream effects require separate evaluation.

## Exercises

### 1. Tradeoff

How do reconstruction and sparsity generally change as $\lambda$ increases?

<details><summary>Show solution</summary>The code becomes smaller and sparser, but reconstruction error may increase. Choose by examining their frontier.</details>

### 2. Gradient

What is the gradient of $f(z)=\frac12\lVert a-Dz\rVert^2$?

<details><summary>Show solution</summary>It is $D^T(Dz-a)$. The residual is projected back along dictionary directions.</details>

### 3. Soft threshold

With a threshold of 0.2, what happens to $0.1,0.5,-0.4$?

<details><summary>Show solution</summary>They become $0,0.3,-0.2$. Subtract the threshold from the absolute magnitude and remove values below 0.</details>

### 4. Scale ambiguity

What remains unchanged if $d_j$ is multiplied by 2 and the corresponding $z_j$ is halved?

<details><summary>Show solution</summary>$d_jz_j$ and reconstruction remain unchanged. The $L_1$ penalty changes, however, so a column-norm constraint is needed.</details>

### 5. Coherence

Why is support recovery difficult if the absolute inner product of two normalized columns is 0.99?

<details><summary>Show solution</summary>The two directions are nearly the same, making it difficult to distinguish which column explained the activation.</details>

### 6. Interpretive claim

MSE is nearly 0 and mean $L_0$ is 5. Can you conclude that the five latents are human concepts?

<details><summary>Show solution</summary>No. Only reconstruction and sparsity have been checked. Activating examples, explanation evaluation, stability, and functional tests are still needed.</details>

## Evidence and update boundaries

The sparse coding objective is a basic form of classical dictionary learning. The next lesson treats modern SAEs applied to LLM activations as a separate model with its own evaluation metrics. Solver-specific convergence conditions and stopping rules are implementation details.

## Lesson summary

- Sparse coding jointly minimizes reconstruction error and a sparsity penalty.
- ISTA alternates a gradient step and soft thresholding.
- Dictionary scale, permutations, and similar columns can make features nonunique.
- Examine reconstruction, sparsity, dead usage, and stability together.

## Pass criteria

- Can you explain both terms in the sparse coding objective?
- Can you compute one ISTA step?
- Can you state the nonuniqueness and evaluation limits of sparse codes?

## Next lesson

- [I06-12 Sparse autoencoder](I06-12-sparse-autoencoder.md)

## Author checklist

- [x] Reconstruction, sparsity, and nonuniqueness are connected.
- [x] Every exercise has a solution.
- [x] The strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and mathematical rendering have been checked.
