---
id: "A09-RMT-06"
title: "Signal and noise eigenvalues"
part: 4
stage: "A09-RMT"
status: "complete"
prerequisites: ["M04-09", "I06-05", "A09-RMT-05"]
estimated_time: "90–120 minutes"
---

# A09-RMT-06. Signal and noise eigenvalues

## Why this lesson matters

Eigenvalue magnitude alone cannot separate signal from noise. Exceeding a null model, stability across splits and seeds, held-out target association, and intervention provide different kinds of evidence. A spectrum analysis should record them in stages rather than combine them into one decision rule.

## Learning objectives

- Explain the null threshold in parallel analysis.
- Distinguish eigenvalue separation from eigenvector stability.
- Design split-half subspace overlap measurements and bootstrap intervals.
- Write task-relevance claims for spectral components in stages.

## Prerequisite check

- Prerequisite lessons: [M04-09 Confidence intervals and bootstrap](../../part-1-foundations/M04/M04-09-confidence-intervals-bootstrap.md), [I06-05 PCA and SVD analysis](../../part-3-interpretability/I06/I06-05-pca-svd-analysis.md), [A09-RMT-05 Spiked covariance model](A09-RMT-05-spiked-covariance-model.md)
- Check question: Why can comparing the span of two directions with similar eigenvalues be preferable to comparing each direction separately?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $q_{1-\alpha}^{\mathrm{null}}$ | `the one minus alpha null quantile` | Upper quantile of the null largest eigenvalue | Scalar |
| $\hat\lambda_j$ | `lambda hat sub j` | Observed sample eigenvalue | Nonnegative scalar |
| $\widehat U_k$ | `U hat sub k` | Orthonormal basis of the leading subspace | $d\times k$ |
| $\lVert U_A^\top U_B\rVert_F^2/k$ | `the squared Frobenius norm of U sub A transpose U sub B, divided by k` | Split subspace overlap | Number in $[0,1]$ |

## Core concepts

### What parallel analysis compares

Parallel analysis repeatedly generates matrices of the same shape under a specified null and applies the same centering, normalization, and eigendecomposition to each. The eigenvalues are sorted in descending order each time. The null eigenvalue distribution at each rank, or a largest-eigenvalue quantile, is then compared with the observed eigenvalue. For example, if

$$
\hat\lambda_1>q_{1-\alpha}^{\mathrm{null}}
$$

we obtain evidence of leading variance larger than the specified null. The quantity $q_{1-\alpha}^{\mathrm{null}}$ is an upper quantile of the null largest-eigenvalue distribution. It has the same variance units as an eigenvalue and is not a probability. For a known continuous null distribution, the probability of exceeding this threshold is $\alpha$. A simulation quantile approximates it, so record the number of repetitions and the fitting procedure as well.

When comparing rank $j$, use the null's $j$th ordered eigenvalue. Applying several individual 95% thresholds does not make the overall false-positive rate 5%. Prespecify the ranks to test and the multiple-comparison criterion.

Also specify what the null preserves and what it removes. An iid Gaussian null assumes independent rows and isotropic noise. Permuting columns separately preserves marginal values but removes pairing between features and can also break dependence within a prompt. In contrast, applying the same row permutation to every column leaves $X^\top X$ unchanged, so it is not a noise control for the spectrum. If a dependence-preserving block null is needed, specify its generation contract separately. The aim is to distinguish the structure being tested from nuisance structure, not to preserve every condition unconditionally.

Examine the quantile's position, how values at the same ordered rank are collected, and the pairing removed by the null separately.

<figure class="lesson-figure" markdown="1">

![The original observed largest eigenvalue five and stated matched null quantile four point two lie on an eigenvalue number line while ninety five percent identifies how a quantile is selected.](../../figures/assets/A09-RMT/A09-RMT-06-quantile-and-observed-value.svg)

<figcaption>The existing observed value 5.0 and q₀.₉₅=4.2 from 1,000 matched nulls are used here. Both positions and their difference 0.8 have eigenvalue units; 95% is the probability level selecting the quantile. No actual null samples were supplied, so no new distribution or p-value was plotted.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Three fixed illustrative ordered null spectra place one value per run at each eigenvalue rank so thresholds would collect the same rank across runs.](../../figures/assets/A09-RMT/A09-RMT-06-ordered-ranks-across-null-runs.svg)

<figcaption>Three fixed illustrative spectra are sorted in descending order, collecting three values at each of ranks 1,2,3. These are not new null simulation results or quantile estimates; they show only where observed rank j is matched with null rank j. Using individual thresholds at multiple ranks is a separate multiple-comparison issue.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A small matrix and its common row permutation have identical centered Gram matrices while permuting only the second column preserves its marginal values and changes the centered cross product.](../../figures/assets/A09-RMT/A09-RMT-06-row-and-column-permutation-grams.svg)

<figcaption>This illustrative example uses two features in three rows. Applying the same row permutation to all columns preserves their pairing and centered Gram matrix. Cyclically permuting only the second column preserves its marginal values but changes the pairing and cross product. This example does not claim to provide a prompt-dependence-preserving null.</figcaption>

</figure>

### Eigenvector and subspace stability

Next, split the data by independent unit and calculate leading subspace overlap. When eigenvalue gaps are small, a subspace can remain stable even if individual vectors have unstable signs or rotations. Bootstrap measurements show sampling uncertainty in eigenvalues and overlap.

Use the same feature coordinates in the two splits, and estimate $U_A,U_B\in\mathbb R^{d\times k}$ with orthonormal columns in each. The value of $k$ must also match and cannot exceed the observed rank in either split. The overlap

$$
O=\frac{\lVert U_A^\top U_B\rVert_F^2}{k}
=\frac1k\sum_{i=1}^k\sum_{j=1}^k
\bigl((u_i^A)^\top u_j^B\bigr)^2
$$

averages the squared projection of one side's basis vectors into the other subspace. Each vector's projection length is at most 1, so $0\le O\le1$. A value of 1 means the two spans are equal; 0 means they are orthogonal. Changing the orthonormal basis within a subspace preserves the Frobenius norm, so the value does not depend on signs or internal rotations. However, when the gap between the eigenvalues at ranks $k$ and $k+1$ is small, the boundary of the selected subspace can itself be unstable.

This value alone does not determine whether individual directions within the same span are stable. Also, if $k$ is close to $d$, even unrelated subspaces can overlap substantially, so compare against a dimension-matched overlap null. Directly multiplying feature coordinates from different models is outside this contract as well; coordinate alignment is required.

Overlap is an average squared projection onto the full span, not a match between vectors at corresponding indices. Examine the effects of basis rotation and large k separately.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![In a deterministic two dimensional subspace example one basis direction is shared and the other has projected length one half giving overlap one plus one quarter divided by two.](../../figures/assets/A09-RMT/A09-RMT-06-overlap-as-average-projection.svg)

<figcaption>This illustrative example in R³ uses orthonormal bases U_A=[e₁,e₂] and U_B=[e₁,½e₂+(√3/2)e₃]. The first squared projection is 1 and the second is 1/4, giving O=(1+1/4)/2=5/8. These are not actual split overlap or uncertainty estimates.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Squared entries of the cross basis matrix for a thirty degree rotation are three quarters and one quarter with total two giving subspace overlap one despite smaller diagonal overlaps.](../../figures/assets/A09-RMT/A09-RMT-06-rotation-invariant-overlap-matrix.svg)

<figcaption>These are the squared entries of an illustrative cross-basis matrix for bases rotated by 30° in the same plane. Averaging only the two diagonal values gives 3/4, but including the off-diagonal entries and dividing by k=2 gives O=1. Comparing the full spans does not depend on signs or rotations within a basis.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Within eight coordinate directions first k and last k coordinate spans have no overlap at k two overlap two thirds at k six and complete overlap at k eight.](../../figures/assets/A09-RMT/A09-RMT-06-large-subspaces-overlap-without-matching.svg)

<figcaption>For illustration with d=8, A spans the first k coordinates and B the last k coordinates. At k=2, O=0; at k=6, four shared axes give O=4/6; and at k=8, O=1. This figure does not calculate a null distribution of independent random subspaces; it shows why a dimension-matched reference is needed.</figcaption>

</figure>

### The comparisons created by splitting and bootstrap

Mixing tokens from the same prompt across both splits can inflate apparent independent reproducibility. Split by prompt, then redo centering and PCA basis estimation separately. Fix the shared preprocessing and feature definitions so both splits compare the same object. Fitting PCA on all the data first and then splitting only the rows does not measure the stability of re-estimating the basis.

For bootstrap as well, resample independent units such as prompts and re-estimate the covariance and basis in every repetition. An eigenvalue interval describes uncertainty in magnitude; an overlap interval describes uncertainty in the selected subspace comparison. Specify the reference: is the overlap between the original and bootstrap bases, or between two independent splits? Do not interpret these two intervals as the same measurement.

Fix the workflow by specifying which units are split or resampled, where the basis is refit, and which reference is used for comparison.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Whole prompt packs split into two groups which each perform centering and a separate PCA fit before their bases meet in an overlap calculation.](../../figures/assets/A09-RMT/A09-RMT-06-prompt-split-and-separate-basis-refits.svg)

<figcaption>This comparison contract assigns each whole prompt pack to only one split and performs centering and PCA fitting separately on both sides. The feature coordinate definitions are shared, but a single basis fitted first on all the data is not split for reuse. This is not a result from running a new split or PCA.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![An illustrative prompt bootstrap resamples a pack twice refits covariance and PCA and branches into eigenvalues and overlap to an explicitly fixed reference basis.](../../figures/assets/A09-RMT/A09-RMT-06-bootstrap-refit-and-two-measurements.svg)

<figcaption>The illustrative replacement resample P₁,P₁,P₃ is shown followed by covariance and basis re-estimation. Eigenvalues and overlap with a reference basis are collected as separate measurements. No actual interval was generated; this contract makes the reference and resampling unit explicit.</figcaption>

</figure>

### From variance to task association and intervention

Evaluate task relevance through held-out label association or prediction. Check functional use separately through behavior changes after component projection or ablation. Record null exceedance, reproducibility, recoverability, and causal use separately.

Do not reuse the samples used to fit and select the PCA basis and probe for held-out evaluation. Predicting a label provides evidence that information can be read from the representation, not that the model uses it. Defining projection ablation as $h\mapsto h-UU^\top h$ removes a particular subspace component, but can also change representation norm or distribution. Compare against random subspace controls matched in dimension and amount removed to distinguish general damage from a component-specific effect. Even this comparison supports conclusions only within the specified inputs, layer, metric, and intervention scope; it does not establish the causes of all model behavior.

Projections matched in dimension and amount removed can still leave different directions. The specificity of their behavioral effects must be measured separately from this geometric calculation.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![For an illustrative vector two one ablation along e one and a control direction point six point eight both remove norm two and retain norm one but leave different residual directions.](../../figures/assets/A09-RMT/A09-RMT-06-matched-amount-projection-ablations.svg)

<figcaption>For the illustrative h=(2,1)ᵀ, target u=e₁ is compared with control u=(0.6,0.8)ᵀ. Both rank-one projections remove norm 2 and retain norm 1, but their residual directions differ: (0,1)ᵀ and (0.8,−0.6)ᵀ. This control direction is fixed for the calculation; no random control distribution or behavioral effect was newly measured.</figcaption>

</figure>

## Small example

If the observed largest eigenvalue is 5.0 and the 95% quantile of 1,000 matched nulls is 4.2, null exceedance is established. If split overlap is 0.15, withhold the claim of a stable direction.

The difference between 5.0 and 4.2 is in eigenvalue units; do not interpret $5.0-4.2$ as a p-value. Interpreting overlap 0.15 also requires $k,d$ and a comparison reference. Rather than making this one number a stability cutoff for the entire textbook, the example withholds a stronger claim when stability evidence is insufficient.

## Common misconceptions

- Null threshold exceedance and false-positive probability cannot be read as the same value.
- A stable high-variance component need not be related to labels or behavior.

## Exercises

### 1. Parallel analysis
If an observed eigenvalue is 3.1 and the null 95% quantile is 3.4, does it exceed the null at $\alpha=0.05$?
<details><summary>Show solution</summary>

No. The value remains noise-compatible under the specified null.
</details>

### 2. Overlap
Two splits estimate the same one-dimensional direction with opposite signs. What is their squared subspace overlap?
<details><summary>Show solution</summary>

A sign change does not change the span, so the overlap is 1.
</details>

### 3. Hierarchy
Null exceedance and split stability pass, but there is no held-out label association. What claim is supported?
<details><summary>Show solution</summary>

It can be called a reproducible variance direction exceeding the specified null. Withhold the claim of a task-relevant signal.
</details>

### 4. Model interpretation
A component ablation changes behavior, but random-direction ablation produces an effect of the same magnitude. What can you conclude?
<details><summary>Show solution</summary>

Component specificity of the intervention effect has not been established. Compare against a control distribution matched in norm and subspace dimension.
</details>

## Evidence and update boundaries

Parallel analysis depends on the validity of the null generator. When selecting multiple eigenvalues simultaneously, specify family-wise error or false discovery control separately.

The use of parallel analysis as a null comparison for finite-sample bias and sampling variability is discussed in the abstract of [Buja–Eyuboglu (1992), Remarks on Parallel Analysis](https://pubmed.ncbi.nlm.nih.gov/26811132/). This lesson develops the overlap interpretation and row-permutation invariance through matrix calculations and runs no new null generation or bootstrap.

## Lesson summary

- Null exceedance is the first stage of assessing a spectral signal.
- Split stability assesses the reproducibility of eigenvectors or subspaces.
- Held-out association and intervention address task relevance and function.
- Do not compress these four kinds of evidence into a single signal label.

## Pass criteria

- Can you design matched null and subspace stability checks?
- Can you distinguish claims about variance, reproducibility, prediction, and causal use?

## Next lesson

- [A09-RMT-07 Weight, activation, and Hessian spectra](A09-RMT-07-weight-activation-hessian-spectra.md)

## Author checklist

- [x] Null exceedance, stability, task association, and function are separated.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
