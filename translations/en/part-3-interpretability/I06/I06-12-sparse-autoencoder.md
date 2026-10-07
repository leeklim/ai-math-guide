---
id: "I06-12"
title: "Sparse autoencoder"
part: 3
stage: "I06"
status: "complete"
prerequisites: ["I06-11", "N05-07"]
estimated_time: "130~160 minutes"
---

# I06-12. Sparse autoencoder

## Why this lesson matters

A sparse autoencoder jointly learns an encoder that directly infers sparse latents from activations and a decoder that reconstructs the original activations. Many latents can form an overcomplete dictionary, but the reconstruction–sparsity tradeoff, dead features, and interpretive stability must all be checked.

## Learning objectives

- Explain the shapes and objective of an SAE encoder and decoder.
- Distinguish sparsity control in $L_1$ SAEs from that in TopK SAEs.
- Compute reconstruction, $L_0$, dead features, and downstream fidelity.
- Explain why SAE latents should not be treated as ground-truth concepts.

## Prerequisite check

- Prerequisite lessons: [I06-11 Sparse coding](I06-11-sparse-coding.md), [N05-07 Mini-batch gradient descent](../../part-2-neural-computation/N05/N05-07-gradient-descent-mini-batch.md)
- Check question: Does low reconstruction MSE guarantee that every latent is used?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $f=\operatorname{ReLU}(W_ea+b_e)$ | `f equals ReLU of W e a plus b e` | Encode an activation into sparse latents | $\mathbb R^m$ |
| $\hat a=W_df+b_d$ | `a hat equals W d f plus b d` | Reconstruct an activation from latents | $\mathbb R^d$ |
| reconstruction loss | `reconstruction loss` | The difference between $a$ and $\hat a$ | nonnegative scalar |
| mean $L_0$ | `mean L zero` | The average number of active latents per sample | $[0,m]$ |
| dead feature | `dead feature` | A latent that never activates during the evaluation window | latent status |
| loss recovered | `loss recovered` | A metric of how much SAE reconstruction preserves the original model loss | normalized statistic |

## 1. Structure and shapes

Encode $a\in\mathbb R^d$ into $m$ latents. An overcomplete setting with $m>d$ is common.

\[
f=\operatorname{ReLU}(W_ea+b_e),\qquad
\hat a=W_df+b_d.
\]

The parameter shapes are $W_e\in\mathbb R^{m\times d}$ and $W_d\in\mathbb R^{d\times m}$. A decoder column can be viewed as the direction that a latent adds in activation space.

Encoder row $j$ reads a weighted sum from input $a$, then applies a bias and ReLU to produce coefficient $f_j$. The decoder sums vectors formed by multiplying each column $j$ by its coefficient and adds $b_d$. A latent's value is therefore different from its decoder direction. The value varies by sample, while the columns of a trained decoder are fixed. Encoder rows and decoder columns need not be transposes of each other or orthogonal.

I06-11 found a sparse code by iterative computation for each new input. An SAE learns an encoder and decoder to produce good codes and reconstructions across inputs, then obtains a new input's code in a single encoder forward pass. This code is not guaranteed to minimize a fixed dictionary's sparse coding objective exactly for every input.

Distinguish the roles of code values, encoder rows, and decoder columns.

<figure class="lesson-figure" markdown="1">

![The existing six-coordinate CPU input passes a twelve by six encoder and ReLU to twelve latent values, then a six by twelve decoder reconstructs six coordinates.](../../figures/assets/I06/I06-12-encoder-decoder-shapes.svg)

<figcaption>The existing CPU exercise has shape 6→12→6. After training, the SAE obtains a new code with one encoder computation, but it is not guaranteed to find the exact sparse coding minimum for every input.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An actual twelve by six encoder schematic highlights one row j, while a six by twelve decoder highlights column j; the former reads a scalar and the latter supplies its fixed direction.](../../figures/assets/I06/I06-12-encoder-row-decoder-column.svg)

<figcaption>Latent j is read by a row in the encoder and supplied with a direction by a column in the decoder. The value f_j varies by sample, while the trained decoder direction is fixed. The two matrices are not transposes of each other.</figcaption>
</figure>

## 2. Objective

A basic ReLU SAE objective is

\[
\mathcal L=\mathbb E\lVert a-\hat a\rVert_2^2+\lambda\mathbb E\lVert f\rVert_1
\]

The first term penalizes reconstruction error in activation space; the second penalizes coefficient magnitudes used in latent space. ReLU outputs are nonnegative, so $\lVert f\rVert_1=\sum_j f_j$. This sum differs from $L_0$, the number of nonzeros. Several small values and one large value can have the same sum, so choosing $\lambda$ does not fix the exact number of active latents for every sample.

A TopK SAE keeps only the $k$ positions with the largest values in each sample and sets the rest to 0. Selecting $k$ positions gives $L_0=k$ only if every retained value is nonzero. Selected values that are 0, or an additional ReLU that sets values to 0, make the actual nonzero count smaller than $k$. [TopK in Scaling and Evaluating Sparse Autoencoders](https://arxiv.org/html/2406.04093v1#S2.SS3) also applies ReLU in selection. Distinguish the number selected from the actual nonzero count, and do not compare an $L_1$ cost and TopK's $k$ as the same sparsity quantity.

Increasing a decoder column's magnitude and reducing its coefficient can preserve reconstruction while lowering only the $L_1$ cost. This is the dictionary-scale issue from I06-11, so read decoder-norm constraints together with the objective. The expression above sums squared components and absolute values before averaging over samples. Using component means in each space, as the exercise does, changes the dimension-dependent factors. The same numerical $\lambda$ therefore does not imply the same tradeoff.

Do not conflate the coefficient sum, selected-position count, and actual nonzero count.

<figure class="lesson-figure" markdown="1">

![Three positive latent bars of height t and one bar of height three t have equal total L1 magnitude but different nonzero counts three and one.](../../figures/assets/I06/I06-12-l1-versus-l0.svg)

<figcaption>For t>0, three small coefficients and one large coefficient can share L₁=3t. Their L₀ values are 3 and 1, so the L₁ cost does not fix the exact active count. This is a mathematical schematic.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![Thirty-two selected TopK positions all contain zero, so selected count thirty-two does not imply L0 thirty-two; additional latent positions are not shown.](../../figures/assets/I06/I06-12-topk-zero-selection.svg)

<figcaption>This schematic illustrates the exception described in the text. Even if the top 32 positions are selected, actual L₀ is 0 if all selected values are 0. Only selected positions are shown; the figure does not specify a new total latent count or an actual SAE result.</figcaption>
</figure>

## 3. Required evaluation checks

The following four quantities cannot fully evaluate an SAE, but they provide minimum checks.

1. Reconstruction MSE or explained variance.
2. Mean $L_0$ and the activation-magnitude distribution.
3. Dead-feature count and firing frequency.
4. Downstream loss or behavioral preservation when reconstructed activations are inserted into the model.

Reconstruction MSE summarizes the error vector's magnitude, not its direction. If the downstream computation reads $w^Ta$, replacing the activation with its reconstruction changes the readout by $w^T(\hat a-a)$. Errors of the same magnitude produce different values depending on whether they are perpendicular or parallel to $w$. Fix the input samples and insertion location, then directly compare downstream results from original and reconstructed activations. This checks how much the SAE-modified computation preserves the original model, separately from evaluating the meaning of new features.

Also examine dictionary and subspace stability as seed, width, and sparsity change. Feature explanation scores depend on sampling and the evaluator as well.

Even with error magnitude held fixed, the downstream effect depends on its direction.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two error vectors have the same length, but one is parallel and the other perpendicular to the downstream readout w, so their dot effects differ.](../../figures/assets/I06/I06-12-downstream-error-direction.svg)

<figcaption>Errors ε=â−a with the same norm produce different downstream score changes wᵀε depending on whether they are parallel or perpendicular to readout w. This schematic depicts error space; it is not a comparison of actual activation and model-loss values.</figcaption>
</figure>

## 4. Dead features

If a ReLU latent is 0 in every observation, gradients and initialization may make it difficult to revive. Define the dead threshold together with dataset size and observation window. A short sample can incorrectly classify a rare but meaningful feature as dead.

In this basic form, if a latent's ReLU input is negative for every training sample, its ReLU derivative is 0 on those samples. The reconstruction gradient to the corresponding encoder row is blocked at that point. A record that the latent never activated on evaluation samples, however, does not prove that its ReLU input is negative for every possible input. Distinguish the training gradient problem from a dead-feature judgment over the observed range.

Separate gradient blocking during training from dead-feature judgments in an evaluation window.

<figure class="lesson-figure" markdown="1">

![A negative preactivation goes through zero ReLU derivative to a zero latent, and the backward route to its encoder is marked blocked at the ReLU stage.](../../figures/assets/I06/I06-12-relu-gradient-block.svg)

<figcaption>For this training sample, a negative preactivation gives a ReLU derivative of 0, blocking the reconstruction gradient to the encoder. This does not claim that the feature is dead for every possible input.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![A bounded observation window contains only below-threshold zero readings, but unseen future inputs remain unknown; the report must specify the window and threshold.](../../figures/assets/I06/I06-12-dead-observation-window.svg)

<figcaption>The record shows no above-threshold activation within one observation window. It does not rule out rare activations over a broader range of inputs. This timeline illustrates the judgment's conditions; it is not an actual firing trace.</figcaption>
</figure>

## 5. Feature interpretation and function

Even if a latent's top-activating contexts share a consistent topic, distinguish the following questions.

- **Coherence**: Do top examples fit a single description?
- **Sensitivity**: Does the latent actually activate on new examples that fit the description?
- **Specificity**: Does it remain inactive on hard negatives?
- **Causal effect**: Does intervening on the latent selectively change behavior?

Reconstruction and sparsity do not substitute for these questions.

## CPU exercise

Train a 12-latent ReLU SAE for 50 steps on 128 samples formed by mixing 10 nonnegative sparse sources into 6 dimensions. Print MSE, mean $L_0$, and dead features together.

<!-- I06_EXAMPLE: i06_12_sparse_autoencoder -->

Dead features in a small training run are an evaluation result, not a failure to hide. Report within the fixed resource limit instead of increasing steps indefinitely to improve the numbers.

## Common misconceptions

### Misconception 1. Sparse latents are monosemantic

Sparsity limits simultaneous activation. It does not guarantee that each latent corresponds to a single human concept.

### Misconception 2. Increasing width always produces better features

Reconstruction may improve, but dead features, computational cost, and stability change. Examine a frontier across metrics.

### Misconception 3. SAE reconstruction can be treated as identical to the original activation

Measure how error affects downstream computation. Small MSE does not always mean a small behavioral change.

## Exercises

### 1. Shape

If $d=768$ and $m=4096$, what are the shapes of $W_e$ and $W_d$?

<details><summary>Show solution</summary>$W_e$ is $4096\times768$, and $W_d$ is $768\times4096$.</details>

### 2. Sparsity

Of 100 latents, an average of 8 are above threshold per sample. What are mean $L_0$ and active fraction?

<details><summary>Show solution</summary>Mean $L_0$ is 8, and active fraction is $8/100=0.08$.</details>

### 3. Dead threshold

Can a latent that never activated on a small dataset be declared permanently dead?

<details><summary>Show solution</summary>No. It may be a rare feature. Report the observed dataset, token count, and threshold together, and test again on a broader sample.</details>

### 4. Reconstruction

Two SAEs have the same MSE, but one has half the mean $L_0$. Is it necessarily better?

<details><summary>Show solution</summary>It is a sparser frontier point, but dead features, downstream fidelity, feature quality, and stability must also be compared.</details>

### 5. TopK

With $k=32$ in TopK, is the exact nonzero count always 32 for every sample?

<details><summary>Show solution</summary>Yes, if the implementation retains exactly the top 32 entries and has no tie or mask exceptions. This differs from indirect control through a penalty, as in a ReLU $L_1$ SAE.</details>

### 6. Claim scope

All top contexts concern code. Can you establish that this is a `coding feature`?

<details><summary>Show solution</summary>The description hypothesis becomes stronger, but independent positives and hard negatives, sensitivity, specificity, and interventions must be checked. Only coherence of top examples has been measured so far.</details>

## Evidence and update boundaries

The reconstruction–$L_1$ structure of SAEs draws on [Towards Monosemanticity](https://transformer-circuits.pub/2023/monosemantic-features/), and TopK, dead latents, and scaling metrics draw on [Scaling and Evaluating Sparse Autoencoders](https://arxiv.org/abs/2406.04093). SAEBench in 2025 shows that metrics such as completeness and isolation measure different aspects of quality. Do not treat one architecture's superiority as a fixed conclusion.

## Lesson summary

- An SAE jointly learns a sparse encoder and an activation-reconstruction decoder.
- Evaluate reconstruction, sparsity, dead features, and downstream fidelity together.
- ReLU+$L_1$ and TopK control sparsity differently.
- Meaning, stability, and causal effects of SAE latents require separate tests.

## Pass criteria

- Can you explain SAE parameter shapes and loss terms?
- Can you compute MSE, mean $L_0$, dead features, and downstream fidelity?
- Can you state the scope of claims supported for sparse latents?

## Next lesson

- [I06-13 Feature stability and identifiability](I06-13-feature-stability-identifiability.md)

## Author checklist

- [x] Reconstruction, sparsity, dead features, and stability are evaluated together.
- [x] Every exercise has a solution.
- [x] The strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and mathematical rendering have been checked.
