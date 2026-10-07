---
id: "A09-RMT-08"
title: "Capstone: null models for spectra"
part: 4
stage: "A09-RMT"
status: "complete"
prerequisites: ["A09-RMT-01", "A09-RMT-02", "A09-RMT-03", "A09-RMT-04", "A09-RMT-05", "A09-RMT-06", "A09-RMT-07"]
estimated_time: "120–180 minutes"
---

# A09-RMT-08. Capstone: null models for spectra

## Why this lesson matters

To identify bulk and outliers in an activation spectrum, the observed matrix and null generator must be part of the same analysis contract. This exercise starts from the MP edge, then checks prompt dependence, marginal variance, split stability, and task relevance in stages.

## Learning objectives

- Design a null hierarchy for activation covariance.
- Compare an analytic MP edge with a simulated null quantile.
- Assess the stability of an outlier subspace across splits and seeds.
- Report variance signals separately from task and causal signals.

## Prerequisite check

- Prerequisite lessons: [A09-RMT-01–07](A09-RMT-07-weight-activation-hessian-spectra.md)
- Check question: What are two conditions under which an iid Gaussian MP null can fail for actual activations?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $S_{\mathrm{obs}}$ | `the observed covariance S` | Actual activation sample covariance | $d\times d$ |
| $\lambda_{+,\mathrm{MP}}$ | `the Marchenko Pastur upper edge` | Upper bulk edge of the fitted iid null | Scalar |
| $q_{0.95}^{\mathrm{sim}}$ | `the ninety-fifth percentile of the simulated null` | Simulated largest-eigenvalue threshold | Scalar |
| $r_{\mathrm{stable}}$ | `the number of stable spectral directions` | Subspace dimension passing both null and split criteria | Nonnegative integer |

## Analysis contract

Collect activations by prompt under a fixed model, layer, and token rule. Treat prompts as independent experimental units, and set feature-wise centering and scaling rules on the training split. Use two model seeds and prompt splits. Do not use test labels to select spectral components.

This lesson is an exercise in writing an analysis contract. If activations are not already available, specify the required inputs, expected shapes, and decision rules; do not record new model runs or simulation results as if they had been produced. First define the roles of prompt splits, training/validation for spectral selection, and testing for final task evaluation. Two model seeds repeat observations at two checkpoints; two observations alone do not represent the whole population of model seeds.

Distinguish centering from scaling. Set feature units and scales on the training split and apply them unchanged to other splits, but subtract each split's own sample mean for its covariance. The Gram matrix of a held-out matrix with only the training mean subtracted can include a held-out mean shift and should not itself be called centered covariance. Prespecify the rule for excluding features with variance 0, and record the actual remaining dimension $d$.

The following calculation separates the roles of a scale fixed on training data and a split mean removed for covariance.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![An illustrative train feature with values zero two has mean one and scale one while held out values three five have mean four yielding train transformed mean three Gram ten and split centered covariance one.](../../figures/assets/A09-RMT/A09-RMT-08-train-scale-split-mean-distinction.svg)

<figcaption>The illustrative training values (0,2) set mean 1 and scale 1, which are applied to held-out values (3,5). Each × marks a mean. The Gram mean of (2,4), obtained by subtracting only the training mean, is 10. Subtracting that split's mean 3 again gives (−1,1), with covariance 1. The difference 10=1+3² is a mean shift, separating scale fitting from split centering.</figcaption>

</figure>

### Fix rows, prompts, and covariance

Write the observed row count as $n$ and use $S_{\mathrm{obs}}=H_c^\top H_c/n$. If tokens are stacked as rows, the prompt count differs from $n$. Use the actual $d/n$ for the spectrum's aspect ratio and prompt units for splitting and bootstrap. Also specify whether longer prompts receive greater weight or whether the same fixed number of positions is collected from every prompt. These choices change the observed distribution even if the representation itself is unchanged.

First record n, which counts matrix rows, separately from the prompt count, which counts independent resampling units.

<figure class="lesson-figure" markdown="1">

![Three illustrative prompt packs with three two and one token observations contribute different row weights to a six row covariance while remaining three independent split or bootstrap units.](../../figures/assets/A09-RMT/A09-RMT-08-token-counts-and-prompt-units.svg)

<figcaption>For illustration, prompt packs P₁,P₂,P₃ contribute 3,2,1 token rows. The covariance has n=6, with row-based weights 3/6,2/6,1/6, but splitting and bootstrap use three prompt units. This figure does not replace a fixed-token-position contract; it shows why the actual sampling rule must be recorded.</figcaption>

</figure>

## Measurement procedure

1. Calculate the eigenvalues, participation ratio, and aspect ratio of $S_{\mathrm{obs}}$.
2. Find the MP edge of an iid Gaussian null matched in shape and global variance.
3. Generate a prompt-block permutation null that preserves each feature's marginal values and breaks cross-feature pairing.
4. Save the largest and rank-wise eigenvalues for each null replicate to obtain parallel-analysis quantiles.
5. Compare the leading subspace that exceeds the null across prompt splits and model seeds.
6. Evaluate held-out label prediction from the stable subspace and a dimension-matched random-subspace control.
7. Compare stable-subspace projection or ablation with random-subspace interventions.

### Eigenvalue summaries and the analytic reference

The participation ratio of a nonzero spectrum is $(\sum_j\lambda_j)^2/\sum_j\lambda_j^2$. For $r$ equal positive eigenvalues, it is $r$, and it is smaller when variance concentrates in a few directions. It is unchanged by an overall scale multiplier, but it is not the rank, the number of independent features, or the number of task signals. If every eigenvalue is 0, the denominator is 0, so record the ratio as undefined.

Set the global noise variance and $\gamma=d/n$, then calculate the analytic edge $\lambda_{+,\mathrm{MP}}=\sigma^2(1+\sqrt\gamma)^2$. The global variance is a single scale for assuming equal noise across features; it cannot account for feature-wise marginal differences or prompt dependence. Exceeding the analytic edge is an observation above a limiting reference, not itself a finite-size significance test. Record where the fitted variance was estimated, which eigenvalues were used, and the observed/null denominators.

PR summarizes spectral concentration; it is not a substitute for rank or the number of task signals.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Two exact positive four value spectra three three three three and nine one one one share rank four and total twelve but have participation ratios four and twelve over seven.](../../figures/assets/A09-RMT/A09-RMT-08-participation-ratio-not-rank.svg)

<figcaption>The illustrative spectra (3,3,3,3) and (9,1,1,1) both have rank 4 and total variance 12, but their participation ratios are 4 and 12/7. An overall multiplier cancels in the ratio, but concentration in the distribution remains. PR is not a count of task signals, and it is undefined when all values are 0.</figcaption>

</figure>

### Specify what the prompt-block null preserves

One block-permutation contract collects the same fixed token positions from every prompt, then reassigns each feature's whole prompt trajectory to another prompt. Use a different prompt permutation for each feature. This preserves feature-wise marginal values and token order and variation within a block, while breaking the pairing of different features that originally occurred in the same prompt.

Applying the same prompt permutation to every feature only reorders row groups and leaves the covariance spectrum unchanged. Conversely, shuffling individual tokens also removes the within-block dependence intended to be preserved. Match the token-position rule before combining prompts of different lengths rather than concatenating them arbitrarily. Specify any restriction requiring exchange within nuisance strata. This null is not a model preserving all joint dependence. Check whether the exchanged prompt blocks are exchangeable under the null, and name the preserved and removed structures precisely.

Apply the same centering, scale fitting, and eigenvalue sorting to each null replicate as to the observations. Prespecify whether decisions use a largest-eigenvalue threshold or rank-wise thresholds. If multiple ranks, layers, or seeds are examined, include multiple comparisons over that selection scope. If simulation repetitions have not actually been performed, leave $q_{0.95}^{\mathrm{sim}}$ unmeasured. Do not substitute the analytic edge in that field.

The following example preserves token order within blocks while changing only cross-feature prompt pairing.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two feature matrices before and after distinct prompt permutations preserve each two token feature trajectory intact while changing which feature trajectories share a prompt block.](../../figures/assets/A09-RMT/A09-RMT-08-feature-wise-whole-trajectory-permutation.svg)

<figcaption>This illustration collects the same two token positions for two features from three prompts. Feature 1 uses order P₃,P₁,P₂, and feature 2 uses P₂,P₃,P₁, moving each whole two-token trajectory. Marginal values and within-trajectory order remain, but cross-feature prompt pairing changes. This is not a new null replicate result or a generator preserving all joint dependence.</figcaption>

</figure>

### The coordinate contract for comparing the same subspace

For two prompt splits of the same checkpoint, use the same feature coordinates and the same $k$, refit the leading subspace separately, and calculate the overlap from RMT-06. The value of $k$ cannot exceed either split's rank; also record the eigenvalue gap at the selection boundary. If the selected ranks differ across splits, report overlap at a common $k$ separately from the selected rank in each split. Do not append arbitrary vectors to the lower-rank side to make the dimensions appear equal.

Hidden coordinates can be permuted or rotated across model seeds. Equal layer widths do not justify directly calculating $U_A^\top U_B$. The basic report checks whether within-seed split stability, null exceedance, and held-out results reproduce across seeds. If geometric overlap across seeds is added, determine coordinate alignment on calibration inputs separate from held-out evaluation and specify the transformation and objects being aligned. Without alignment, direct overlap is unmeasured and must be distinguished from reproducibility of result patterns.

Record within-seed coordinate comparisons and cross-seed result-pattern comparisons along different paths.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Two checkpoint branches each refit prompt split bases in their own hidden coordinates then compare evidence patterns while direct cross seed geometric overlap remains unmeasured without alignment.](../../figures/assets/A09-RMT/A09-RMT-08-within-seed-stability-before-cross-seed-geometry.svg)

<figcaption>The basic contract refits prompt-split bases within each seed, then compares whether patterns of null exceedance, stability, and held-out results reproduce. The same d alone does not make coordinates equal across seeds. Do not calculate direct U_AᵀU_B without separate calibration alignment; leave that overlap unmeasured.</figcaption>

</figure>

### Evaluate task prediction and intervention separately

Choose the basis and probe using training/validation data, then apply them unchanged to the test set. For a random-subspace control of the same dimension, refit the probe and use the same selection and test rules. Compare predictions on the same test prompts to reduce dataset differences, and record uncertainty at the prompt-unit level. Recovering labels from a subspace selected by variance does not establish that the model's internal readout uses that information.

For projection or ablation, specify the layer and tokens, subspace to remove, mean to retain, and metric. If the basis was fitted in scaled coordinates, specify the operation on the original activations, including how scaling is reversed. Compare against random-subspace interventions matched not only in $k$ but also in amount removed and norm damage. Even for a subspace with good predictive performance, if its intervention effect matches the control, record recoverability separately from component-specific functional evidence.

Fit the chosen and control probes separately. If intervention uses a scaled basis, also specify the calculation returning to the original coordinates.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Selected and dimension matched random subspaces each fit and select a separate probe on train validation before fixed evaluation on the same untouched test prompt packs.](../../figures/assets/A09-RMT/A09-RMT-08-separate-probe-fits-shared-test.svg)

<figcaption>Probes are refitted and selected separately for chosen U_k and dimension-matched random V_k, then used unchanged for evaluation on the same untouched test prompts. Do not transfer the chosen probe unchanged to the control coordinates or select the subspace using test labels. This comparison design distinguishes recoverability from functional use; it is not a new prediction result.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![With fixed mean zero scale matrix three one and direction one one over root two a raw vector three zero becomes one zero is ablated to one half minus one half and returns to raw one point five minus one half not naive raw one point five minus one point five.](../../figures/assets/A09-RMT/A09-RMT-08-scaled-coordinate-ablation-backtransform.svg)

<figcaption>This illustration uses mean 0, D=diag(3,1), U=(1,1)ᵀ/√2, and h=(3,0)ᵀ. Starting from z=D⁻¹h gives (I−UUᵀ)z=(0.5,−0.5)ᵀ; restoring D gives h'=(1.5,−0.5)ᵀ. This differs from (1.5,−1.5)ᵀ obtained by applying the same U directly to raw h. The analysis contract must specify mean retention, restoration of the original scale, and removal-amount controls. No behavioral effect was measured.</figcaption>

</figure>

## Results table

| Stage | Pass criterion | Supported claim |
|---|---|---|
| Analytic null | Compare the MP edge with the observed position | Difference in position relative to an iid isotropic limiting reference |
| Simulated null | Exceed a prespecified null quantile | Exceedance of the matched null at the specified criterion |
| Splits and seeds | Within-seed split stability and reproducibility of result patterns | Stable variance subspace under the specified coordinate and split conditions |
| Held-out task | Prediction compared with a control | Recoverable task signal |
| Intervention | Effect compared with a matched control | Functional evidence under the specified operation |

For example, the exercise value 4.0 is above analytic edge 3.0 but below simulated 95% quantile 5.2. Both conclusions must be recorded together. Exceeding only the analytic edge does not reject the finite-size matched null. Keep variance, stability, task, and intervention fields marked as unmeasured where appropriate, rather than substitute a pass at an earlier stage for evidence at the next.

Placing the numbers from two nulls on the same axis does not give their pass criteria the same meaning.

<figure class="lesson-figure" markdown="1">

![The original exercise places analytic MP edge three observed largest eigenvalue four and matched simulated null ninety fifth percentile five point two on one eigenvalue axis.](../../figures/assets/A09-RMT/A09-RMT-08-analytic-observed-simulated-order.svg)

<figcaption>The existing exercise values 3.0&lt;4.0&lt;5.2 are shown on one eigenvalue axis. The observed value exceeds the analytic limiting edge but not the matched finite-size null quantile. Do not replace the simulated field with the analytic value or choose only the favorable criterion. These three values are from the existing stipulated case; no simulation was run here.</figcaption>

</figure>

## Common misconceptions

- Choosing only the favorable result between the analytic and simulated nulls creates selection bias.
- Adjusting the outlier count together with the threshold after inspecting the data does not support a confirmatory claim.

## Exercises

### 1. Split
On which split are the null threshold and subspace dimension set, and on which split is task association evaluated?
<details><summary>Show solution</summary>

Set the threshold and dimension on training/validation data and evaluate task association on a held-out test split not used for selection.
</details>

### 2. Mismatch
The MP edge is 3.0, but the 95% quantile of a matched permutation null is 5.2. What can you conclude if the observed largest eigenvalue is 4.0?
<details><summary>Show solution</summary>

It exceeds the iid MP null but not the permutation null that preserves more dependence and marginal structure. Withhold a signal claim under the matched-null criterion.
</details>

### 3. Rotation
Two leading eigenvalues are nearly equal, and eigenvectors rotate across splits. What should be compared?
<details><summary>Show solution</summary>

Compare principal-angle overlap of the leading two-dimensional subspace rather than match the two vectors individually.
</details>

### 4. Claim
A stable outlier subspace predicts labels, but its ablation effect matches that of a random subspace. How should this be reported?
<details><summary>Show solution</summary>

Labels can be recovered from a reproducible variance subspace, but functional use specific to that subspace has not been established.
</details>

## Evidence and update boundaries

This exercise fixes the null hierarchy and order of evidence. Even prompt-block permutation does not preserve all dependence, so the report must specify which structures the generator breaks.

## Lesson summary

- Analytic MP and matched simulation provide different nulls.
- Separate threshold selection from held-out task evaluation.
- When eigenvalues are close, examine subspace stability rather than individual vectors.
- Record variance outliers, recoverability, and functional effects as separate claims.

## Pass criteria

- Can you complete a matrix–unit–normalization–null–stability–task contract?
- Can you explain a case in which null mismatch changes the conclusion?

## Next lesson

- The next optional module is A09-CAU.

## Author checklist

- [x] Analytic and simulated nulls are separated from task and intervention validation.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
