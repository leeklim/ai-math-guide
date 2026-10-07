---
id: "I06-13"
title: "Feature Stability and Identifiability"
part: 3
stage: "I06"
status: "complete"
prerequisites: ["I06-12", "M03-15"]
estimated_time: "120–150 minutes"
---

# I06-13. Feature Stability and Identifiability

## Why this lesson matters

If retraining an SAE or a dictionary-learning model does not produce the same features, descriptions attached to individual latents have weak reproducibility. Features can differ even after predictable symmetries such as permutation, sign, and scaling are aligned. Individual directions can be unstable while the subspace they span remains stable.

## Learning objectives

- Align permutation, sign, and scale ambiguities before comparing dictionaries.
- Distinguish cosine matching from one-to-one assignment.
- Evaluate individual feature stability separately from subspace stability.
- Distinguish empirical stability from mathematical identifiability.

## Prerequisite check

- Prerequisite lessons: [I06-12 Sparse autoencoder](I06-12-sparse-autoencoder.md), [M03-15 Reparameterization and model symmetries](../../part-1-foundations/M03/M03-15-reparameterization-model-symmetries.md)
- Check question: Should two SAEs whose dictionary columns differ only in order be treated as different feature sets?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $d_j^{(1)}$ | `feature direction j from run one` | Decoder direction from the first training run | $\mathbb R^d$ |
| $M_{jk}$ | `matching score M sub j k` | Similarity between feature directions from two runs | $[0,1]$ for absolute cosine |
| assignment | `one-to-one assignment` | Matching that pairs features without reuse | permutation |
| feature stability | `feature stability` | Extent to which similar features reappear in independent training runs | empirical property |
| subspace stability | `subspace stability` | Extent to which the span of a feature group is preserved | empirical property |
| identifiability | `identifiability` | Property of parameters being uniquely determined by an observation distribution and assumptions | theoretical property |

## 1. Remove symmetries first

Dictionary column order does not affect the loss. Inversely changing encoder and decoder scales can also produce the same reconstruction. For signed features, signs can be changed together as well. Comparing raw column indices is therefore not a stability test.

These symmetries change not only the decoder column but also the code multiplying it. If columns are reordered, reorder the code in the same way; if a column is multiplied by a positive factor, divide its code by that factor. Each column-code product remains the same, preserving their sum, the reconstruction. However, the $L_1$ cost or decoder-norm constraints are not always preserved. Distinguish symmetries of the reconstruction function from symmetries of the training objective.

For normalized directions, calculate

\[
M_{jk}=\left|\frac{(d_j^{(1)})^Td_k^{(2)}}{\lVert d_j^{(1)}\rVert\lVert d_k^{(2)}\rVert}\right|
\]

and maximize the total score of a one-to-one assignment. Whether to take the absolute value depends on what activation signs mean.

Dividing by the two norms removes differences in positive scale, leaving a comparison of directions. Cosine is undefined for a column with norm 0, so classify such columns separately. With signed codes, jointly reversing the column and code signs preserves their product. ReLU codes cannot be negative, however, so there is no basis for treating opposite directions as the same feature. In that case, retain signed cosine and check activation patterns on the same inputs alongside high direction scores.

Check the symmetries that jointly transform directions and codes before finding column correspondences.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Five original direction code pairs are jointly permuted and signed in the existing synthetic lab order, preserving each product before added noise; ReLU codes do not admit the same sign flip.](../../figures/assets/I06/I06-13-paired-symmetries.svg)

<figcaption>The figure removes noise from the existing lab's permutation and sign sequence to show the symmetries themselves. Jointly transforming directions and codes preserves the sum of contributions. Do not directly apply the sign symmetry of signed codes to ReLU codes.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![The exact five by five absolute cosine matrix of the existing seven by five signed fixture has optimal one-to-one assignments outlined off the raw diagonal, with numbers in each cell.](../../figures/assets/I06/I06-13-cosine-assignment.svg)

<figcaption>Absolute cosines from the existing 7×5 signed fixture are rounded to two decimal places. Orange outlines mark the one-to-one assignment with the largest total score, which differs from the raw diagonal. Recovering this synthetic transformation does not prove actual SAE feature stability or theoretical identifiability.</figcaption>
</figure>

## 2. Greedy matching and assignment

If each feature independently selects its closest counterpart, several features can converge on the same column. Matching entire dictionaries requires a one-to-one assignment, such as the Hungarian algorithm. The proportion of unmatched features is also a result.

Independent nearest-neighbor selection chooses each row's maximum separately. A one-to-one assignment maximizes the total score subject to not using the same target column twice. Some features can therefore be paired with a counterpart other than their highest-scoring one. Even if the dictionaries have equal sizes, formally matching every column does not make the matches good. Count only correspondences passing a predefined threshold as valid matches, and report unmatched columns when dictionary sizes differ.

Do not choose the matching threshold after seeing the results. Cosine distributions from null dictionaries or random directions can help check false matches.

Use the same column count, dimension, and matching procedure for the null as for the actual comparison. Using only the cosine distribution of an arbitrary single pair as the reference omits the effect of selecting the best value from many candidates.

Choosing individual maxima and finding a global correspondence without reuse impose different constraints.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two greedy source features select the same target B one while a one-to-one assignment routes them to distinct targets, possibly using a lower individual similarity.](../../figures/assets/I06/I06-13-many-to-one-assignment.svg)

<figcaption>The left panel shows the possible failure of two sources independently choosing the same target. The right panel shows the constraint against reusing targets. It does not assign arbitrary actual scores or an optimal assignment result; report threshold and coverage together.</figcaption>
</figure>

## 3. Feature stability and subspace stability

Individual directions can differ across two runs while their groups span the same low-dimensional subspace. In that case, evaluate subspace stability using principal angles or distances between projection matrices. This does not support a claim that individual features are identifiable, but evidence of a reproducible subspace remains.

If $U$ is an orthonormal basis of the subspace spanned by the columns, its projection matrix is $P=UU^T$. This matrix projects input vectors onto the subspace and remains unchanged when the basis undergoes an orthogonal rotation within the same subspace. Asking whether the two runs have similar $P$ matrices is therefore different from asking whether their individual basis directions match. Principal angles also measure directional differences between subspaces. First fix which feature groups will be compared. If both full dictionaries span the entire input space, both $P$ matrices are the identity, so this test cannot detect differences even when individual features differ.

CKA from I06-08 can compare the Gram structures of activation arrays obtained on the same sample. It is not generally invariant to transformations that scale different columns differently, however, so it is not a pure subspace metric. Distinguish using CKA to examine representational similarity from comparing the decoder spans themselves.

Because bases can differ within the same plane, compare directions separately from projections.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two perpendicular bases at different orientations lie in the same shaded plane and produce equal projection matrices; full ambient span makes both projections identity regardless of feature matching.](../../figures/assets/I06/I06-13-subspace-basis-stability.svg)

<figcaption>Two bases spanning the same plane have the same projection matrix even if their individual directions differ. Spanning the entire ambient space gives P=I, so this test cannot distinguish feature differences. The figure conceptually illustrates rotation between bases.</figcaption>
</figure>

## 4. Identifiability is a stronger statement

Empirical stability across seeds is useful, but similar features across multiple seeds do not prove uniqueness among all possible solutions. Mathematical identifiability asks whether parameters other than those related by permitted symmetries can produce the same assumed observation distribution. Even when claiming uniqueness up to symmetries, specify which symmetries are being excluded.

Dictionary learning studies uniqueness under conditions such as data-generation assumptions, dictionary incoherence, and sparsity. Exact conditions differ by theorem, and listing these items alone does not prove identifiability. Whether that dictionary can actually be recovered with sufficiently many finite samples is a separate estimation problem. Being uniquely determined by a population distribution is not the same as being found exactly from the currently observed sample.

Conversely, even a theoretically identifiable setting can be unstable in experiments because of finite samples, optimization failures, and local minima.

Distinguish repeatedly obtained solutions from uniqueness that rules out all equivalent alternatives.

<figure class="lesson-figure" markdown="1">

![Three similar optimization run points sample a bounded parameter setting diagram while question marks denote unexcluded alternatives, distinguishing empirical repetition from theoretical uniqueness.](../../figures/assets/I06/I06-13-stability-versus-uniqueness.svg)

<figcaption>Similar results from three seeds do not rule out all other possible settings. The question marks denote alternatives not yet ruled out, not measurements establishing that other solutions actually exist. Identifiability asks about uniqueness under distributional assumptions and permitted symmetries.</figcaption>
</figure>

## CPU lab

Create a second dictionary by permuting the first dictionary, changing signs, and adding small noise. Compare raw diagonal cosines with cosines after optimal one-to-one matching.

<!-- I06_EXAMPLE: i06_13_feature_stability -->

A high matched score means this synthetic transformation was recovered. With actual SAEs, also report unmatched features, splits and merges, and correspondences that hold only at the subspace level.

## Common misconceptions

### Misconception 1. Features must have the same index to be the same feature

Latent permutation is a basic symmetry. Align directions and activation patterns.

### Misconception 2. Many high-cosine pairs mean the whole dictionary is stable

Several source features can converge on one target. Examine one-to-one coverage and the unmatched proportion.

### Misconception 3. Agreement between two seeds establishes identifiability

It is evidence of stability across those two optimization runs, not a mathematical conclusion about uniqueness.

## Exercises

### 1. Permutation

If two dictionaries differ only in column order, has the reconstruction model changed?

<details><summary>Show solution</summary>Applying the same permutation to encoder latents and decoder columns leaves the function unchanged. A difference in raw indices is not a feature difference.</details>

### 2. Absolute cosine

Why can absolute cosine be used, and when might it be inappropriate?

<details><summary>Show solution</summary>Use it when jointly reversing signs can be treated as the same signed direction. When signs are functionally asymmetric, as with nonnegative ReLU features, the absolute value can merge different features.</details>

### 3. Many-to-one matching

Explain a case where greedy nearest-neighbor matching overestimates stability.

<details><summary>Show solution</summary>If several features in the first dictionary select the same feature in the second dictionary as their closest counterpart, high pair scores are repeated. One-to-one assignment and coverage prevent this.</details>

### 4. Subspace

Individual match scores are low, but the projection matrices are similar. What claim is possible?

<details><summary>Show solution</summary>The individual basis directions are unstable, but the subspace spanned by the feature group may be reproducible.</details>

### 5. Null match

Why compare the matching threshold with a random dictionary?

<details><summary>Show solution</summary>With high dimensions and many candidates, a high maximum cosine can occur by chance. The null distribution provides a reference for false matches.</details>

### 6. Identifiability

The same feature appeared across three seeds. Can the result be described as `uniquely identified`?

<details><summary>Show solution</summary>Empirical reproducibility has increased, but not all equivalent solutions have been ruled out. Distinguish this from a proof of identifiability under assumptions.</details>

## Sources and update boundaries

Seed instability in SAE dictionaries was checked against [Archetypal SAE](https://openreview.net/forum?id=9v1eW8HgMU) and the 2026 preprint [Unstable Features, Reproducible Subspaces](https://arxiv.org/abs/2606.12138). The latter is a recent preprint, so its individual conclusions are not used as established general laws. It is used only as a basis for separating feature stability from subspace stability.

## Lesson summary

- Handle permutation, sign, and scale symmetries before comparing dictionaries.
- Examine one-to-one assignment, coverage, and null matches together.
- Individual features and subspaces can differ in stability.
- Empirical stability is a weaker claim than mathematical identifiability.

## Pass criteria

- Can you compare two dictionaries using symmetry-aware matching?
- Can you distinguish feature stability from subspace stability?
- Can you avoid overstating stability results as identifiability?

## Next lesson

- [I06-14 Writing representation claims](I06-14-writing-representation-claims.md)

## Author checklist

- [x] Feature stability, subspace stability, and identifiability are separated.
- [x] Every exercise has a solution.
- [x] The strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and mathematical rendering have been checked.
