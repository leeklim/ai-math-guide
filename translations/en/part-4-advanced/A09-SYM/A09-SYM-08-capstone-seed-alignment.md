---
id: "A09-SYM-08"
title: "Capstone exercise: representation alignment across seeds"
part: 4
stage: "A09-SYM"
status: "complete"
prerequisites: ["A09-SYM-01", "A09-SYM-02", "A09-SYM-03", "A09-SYM-04", "A09-SYM-05", "A09-SYM-06", "A09-SYM-07"]
estimated_time: "120–180 minutes"
---

# A09-SYM-08. Capstone exercise: representation alignment across seeds

## Why this lesson matters

Representation alignment across seeds cannot be interpreted without the same inputs, the same checkpoint criterion, an explicit symmetry class, and held-out evaluation. This exercise separates raw differences, symmetry-aligned differences, and functional differences into three levels.

## Learning objectives

- Design a paired activation dataset and alignment splits.
- Compare permutation and orthogonal baselines fairly.
- Evaluate alignment stability and function preservation.
- Limit feature-identity claims to the scope supported by the evidence.

## Prerequisite check

- Prerequisite lessons: [A09-SYM-01–07](A09-SYM-07-model-alignment-equivalence-classes.md)
- Check question: Why is providing the same prompts to both models necessary for sample correspondence?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $X^{(a)},X^{(b)}$ | `X superscript a and X superscript b` | Paired activations from two seeds | $n\times d$ |
| $g_{\mathrm{train}}$ | `g fit on the training split` | Fitted alignment | Transformation |
| $E_{\mathrm{heldout}}$ | `held-out alignment error` | Residual on unseen inputs | Nonnegative scalar |
| $S_{\mathrm{boot}}$ | `bootstrap stability score` | Alignment reproducibility | Score or interval |
| $u^{(a)},u^{(b)}$ | `u superscript a and u superscript b` | Intervention directions matched across two seeds | Unit vectors in $\mathbb R^d$ |

## Analysis contract

Compare independent seeds of the same architecture and training recipe. Match checkpoints by processed token count and use the same prompts, token positions, layers, and normalization. Limit the transformation classes to three levels: identity, permutation, and orthogonal.

Equal processed token counts provide a criterion for matching training progress, not a condition that both models have the same loss or state. Test which differences between independently trained models can be explained by coordinate changes. Distinguish this from re-expressing one model's parameters through a symmetry action.

Identity compares the original feature coordinates. Permutation allows differences in unit order, and orthogonal alignment also allows coordinate mixing that preserves lengths and angles. Good activation agreement under the last transformation does not imply a parameter symmetry of the fixed architecture. First interpret it as a comparison of representation geometry and separate the functional evidence.

The flow below distinguishes independent seeds from the contract of a shared training clock.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two independent seeds follow the same training recipe to checkpoints with equal processed-token count, then paired activations are compared without assuming equal states.](../../figures/assets/A09-SYM/A09-SYM-08-independent-seed-contract.svg)

<figcaption>Independent seeds are trained under the same architecture and recipe, and checkpoints are selected at matching processed token counts T. This is a training-clock criterion, not an assumption of equal loss or state. Distinguish a copy re-expressing one model's parameters by symmetry from activation alignment between two independently trained models.</figcaption>

</figure>

## Measurement procedure

1. Create training and held-out splits at the prompt level.
2. Fit neuron assignment and orthogonal Procrustes separately on the training split.
3. Compute Frobenius residuals, CKA and RSA, and downstream output differences on held-out data.
4. Measure matching and subspace stability with a prompt bootstrap.
5. Use random orthogonal transformations and input-row correspondence shuffling as null controls.
6. Repeat aligned-direction interventions in both seeds and compare effect signs and magnitudes.

### Compute residuals with the same inputs and a frozen transformation

Match each row's prompt ID and token position, and fix the activation extraction point. Even with the same layer name, activations before and after normalization are different objects. Prompt-level splitting prevents related tokens from one prompt from appearing on both sides. Freeze centering and scaling estimates and the alignment matrix from fitting, then apply them to held-out data.

This lesson fits in the direction $X^{(a)}g_{\mathrm{train}}\approx X^{(b)}$. Held-out residuals measure the difference in the same direction. With $n$ evaluation rows, RMSE obtained by dividing the Frobenius norm by $\sqrt{nd}$ can put errors on a per-entry scale. Use the same rows, preprocessing, and normalization rules for raw, permutation, and orthogonal comparisons. Do not reduce held-out error by refitting the transformation there.

Linear CKA is invariant to orthogonal transformations, so its value may be unchanged by alignment. The Procrustes residual measures error in coordinate correspondence, while CKA summarizes sample relationships; they are not two demonstrations of the same improvement. For RSA, also fix the distance used to form the relationship matrix. Downstream output is a separate observable that can be compared without hidden alignment. Record which output differences were measured on which input set.

After fixing prompt bundles and hook locations, read coordinate residuals and sample-relationship measures separately below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Whole prompt token bundles stay within fit or held-out splits; a contrasting token-level split leaks one prompt across both.](../../figures/assets/A09-SYM/A09-SYM-08-prompt-level-split.svg)

<figcaption>Token bundles A and B belong to the fit split, and C and D to the held-out split. Splitting tokens of the same prompt A across both, as below, lets related context cross the split boundary. Token-row counts and independent-prompt counts are different units of analysis.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two seed computation chains distinguish matching pre-normalization hooks from comparing pre-normalization with post-normalization activations.](../../figures/assets/A09-SYM/A09-SYM-08-paired-hook-location.svg)

<figcaption>Even with the same layer name, pre-normalization and post-normalization activations are different measurement objects. Match hooks by prompt ID, token position, layer, and normalization side. The figure explains hook-selection relationships, not actual model activations.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A four-sample coordinate rotation changes raw RMSE but preserves the sample Gram matrix and linear CKA; fitted rotation removes the coordinate residual.](../../figures/assets/A09-SYM/A09-SYM-08-cka-and-coordinate-residual.svg)

<figcaption>This mathematical example applies Y=XR₄₅ to the four mean-0 rows X={(1,0),(−1,0),(0,1),(0,−1)}. Paired raw RMSE is approximately 0.541, but fitting g=R₄₅ makes it 0. The sample Gram matrix is unchanged, so linear CKA is 1 both before and after alignment. The two metrics do not demonstrate the same improvement twice.</figcaption>

</figure>

### Distinguish the roles of bootstrap and null controls

To examine matching stability, bootstrap fit prompts and refit the transformation in each resample. Keep tokens bundled with their prompts to avoid counting tokens as independent samples. Comparing these transformations' residuals and correspondence variation on a fixed held-out set measures sensitivity to changes in the fit data. Distinguish unstable individual matches with a stable observed subspace from cases where both are unstable. Bootstrapping within one seed pair does not replace evaluation over repeated independent training seeds.

A random orthogonal control compares the fitted rotation with an arbitrary one. A correspondence shuffle disrupts the pairing between input rows of one model and those of the other, then applies the same fitting procedure. Relabeling classes or jointly reordering both matrices' rows does not break correspondence. Preserve correctly paired rows in held-out evaluation and state what the shuffle destroys. Do not automatically interpret this control as a test that features are absent.

The objects resampled by the bootstrap differ from the correspondences broken by the null control.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two prompt-bundle bootstrap resamples refit separate alignment maps and transfer them to the same fixed held-out prompts.](../../figures/assets/A09-SYM/A09-SYM-08-prompt-bootstrap-refit.svg)

<figcaption>Resample fit-prompt bundles with repetitions and refit ĝ for each resample. Tokens move with their prompts, while held-out prompts stay fixed. This variation measures fit-data sensitivity; a bootstrap within one seed pair is not counted as repeated independent training seeds.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Joint row reordering keeps prompt pairs intact, while a one-sided reordering of Y fit rows creates mismatched A-to-B, B-to-C and C-to-A pairs.](../../figures/assets/A09-SYM/A09-SYM-08-one-sided-row-shuffle.svg)

<figcaption>Reordering both matrices as B,C,A retains paired rows and is not a correspondence null. Pairing X's A,B,C with Y's B,C,A breaks input correspondence through a one-sided row shuffle. The null mispairs fit rows and refits using the same procedure, while held-out evaluation retains the correct pairs.</figcaption>

</figure>

### Intervention directions follow the direction of the alignment equation

Choose unit column vector $u^{(a)}$ as an activation direction in seed $a$. For row-vector alignment $x^{(a)}g_{\mathrm{train}}\approx x^{(b)}$, define the corresponding column direction in seed $b$ as $u^{(b)}=g_{\mathrm{train}}^\top u^{(a)}$. This converts the row displacement $(u^{(a)})^\top$, transformed on the right to $(u^{(a)})^\top g_{\mathrm{train}}$, back into a column. Permutation and orthogonal $g$ preserve this direction's length.

The length and direction refer to the coordinate convention used for alignment. With feature-wise scaling in preprocessing, undo each seed's scaling before intervening at the hook to return the direction to original activation coordinates, then match intervention strength in those coordinates. Do not treat unit norm in preprocessed coordinates as equal magnitude at the original hook.

Use the same hook location, prompts and tokens, intervention strength, and output metric in both seeds. Compare changes relative to each model's original output. Adding a direction and ablation are different interventions, so use one consistent intervention rule. Do not add mean coordinate shifts from centering to directional displacements. Similar effects support similar use of the tested direction in the tested task, not equality of the entire models or mechanisms for every feature.

Separate transfer from row alignment to column intervention from matching raw-hook scales and baselines below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A row alignment by a quarter-turn transfers column direction one,zero to zero,minus-one through g transpose, not g.](../../figures/assets/A09-SYM/A09-SYM-08-row-to-column-direction.svg)

<figcaption>In row equation x⁽ᵃ⁾g≈x⁽ᵇ⁾, if g=R₉₀ and u⁽ᵃ⁾=(1,0)ᵀ, then u⁽ᵇ⁾=gᵀu⁽ᵃ⁾=(0,−1)ᵀ. This rewrites (u⁽ᵃ⁾)ᵀg=(0,−1) as a column. The upward dashed arrow on the right shows, for comparison, the opposite direction obtained by applying g directly to the column.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Unit directions in scaled coordinates undo different diagonal feature scales to raw displacements with norms two and four, which must be normalized before equal raw steps.](../../figures/assets/A09-SYM/A09-SYM-08-inverse-scale-hook-direction.svg)

<figcaption>For column coordinates preprocessed as z=D⁻¹(h−μ), the raw directional displacement is Δh=Du. The figure's unit directions have raw norms 2 and 4, so they cannot be treated unchanged as equal-strength interventions. After seed-specific inverse scaling, normalize raw directions to match the same raw strength δ; do not add centering mean μ to directional displacements.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Two illustrative seeds have different baseline and patched metrics but identical within-seed changes of plus two.](../../figures/assets/A09-SYM/A09-SYM-08-seed-specific-baselines.svg)

<figcaption>In these illustrative numbers, seed a moves from baseline 10 to post-intervention 12, and seed b from 100 to 102, giving ΔM=+2 for both. Compare changes relative to each model's original output, not the difference between post-intervention absolute values 12 and 102. These are not actual exercise results, and similar effects are limited to evidence for the tested direction and task.</figcaption>

</figure>

## Results record

| Comparison | Preserved structure | Held-out measure | Permitted claim |
|---|---|---|---|
| Identity | Coordinate labels | Raw residual | Coordinate agreement |
| Permutation | Coordinate contents | Assignment residual | Agreement up to order |
| Orthogonal | Inner products | Procrustes residual | Subspace geometry agreement |
| Intervention | Behavioral effects | Paired effects | Evidence of functional reuse |

Read “agreement” in the table as limited to evaluated inputs and specified error criteria. Record the actual residual, its change relative to raw comparison, and bootstrap variation together. The broader orthogonal class makes a small fit residual easier to obtain, which relates to the reason for freezing the transformation applied to held-out data. Individual neurons, subspace geometry, outputs, and intervention effects are different claim subjects; no single measure replaces the others.

## Common misconceptions

- Successful orthogonal alignment does not imply one-to-one neuron identity.
- Results for one seed pair cannot be generalized to a necessary symmetry of the entire training recipe.

## Exercises

### 1. Split unit
Why split at the prompt level rather than randomly partitioning token rows?
<details><summary>Show solution</summary>

It prevents leakage from related tokens of the same prompt appearing in both training and held-out data.
</details>

### 2. Nested classes
What can be concluded when the orthogonal residual is smaller than the permutation residual?
<details><summary>Show solution</summary>

There may be rotated subspace similarity not explained by coordinate reordering alone. Functional equivalence requires a separate check.
</details>

### 3. Stability
At what level should results be reported if neuron matching varies across bootstrap samples but subspace angles remain stable?
<details><summary>Show solution</summary>

Report unstable individual-neuron identity and stability only of subspace-level equivalence.
</details>

### 4. Causal transfer
What evidence is strengthened when aligned-direction ablation effects are similar across two seeds?
<details><summary>Show solution</summary>

Evidence is strengthened that the aligned subspace is used for similar functions in both models. This does not imply a unique mechanism.
</details>

## Evidence and update boundaries

This exercise combines permutation matching, Procrustes, CKA and RSA, and interventions into a hierarchy of evidence. It does not permit arbitrary fitting with nonlinear maps; for a new architecture, specify the symmetry classes again first.

- [Kornblith et al. (2019), §§2–3](https://proceedings.mlr.press/v97/kornblith19a/kornblith19a.pdf): Provides orthogonal invariance of the representation metric. The alignment matrix direction was derived directly from the row-vector equation in the text.

## Lesson summary

- Use paired data and prompt-level splits.
- Compare identity, permutation, and orthogonal classes hierarchically.
- Judge the stability of alignment units with a bootstrap.
- Separate geometric similarity from functional similarity through intervention transfer.

## Pass criteria

- Can you design a claim–class–split–metric–control specification for seed alignment?
- Can you distinguish neuron, subspace, and function identity claims?

## Next lesson

- The next optional module is A09-LRN.

## Author checklist

- [x] The hierarchical evidence contract for alignment across seeds is complete.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
