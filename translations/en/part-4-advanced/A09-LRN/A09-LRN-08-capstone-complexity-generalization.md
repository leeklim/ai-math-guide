---
id: "A09-LRN-08"
title: "Capstone: complexity and generalization"
part: 4
stage: "A09-LRN"
status: "complete"
prerequisites: ["A09-LRN-01", "A09-LRN-02", "A09-LRN-03", "A09-LRN-04", "A09-LRN-05", "A09-LRN-06", "A09-LRN-07"]
estimated_time: "120–180 minutes"
---

# A09-LRN-08. Capstone: complexity and generalization

## Why this lesson matters

Applying complexity theory to interpretation experiments requires more than attaching a theorem name: fix the class, norm constraints, sample unit, selection procedure, and target population. This capstone combines a probe capacity ladder and multiple generalization splits in one contract.

## Learning objectives

- Design a probe capacity ladder and nested evaluation.
- Separate empirical gaps, random-label controls, and complexity bounds.
- Record prompt, template, and model generalization together.
- Write a recoverability claim that matches the results.

## Prerequisite check

- Prerequisite lessons: [A09-LRN-01–07](A09-LRN-07-probe-interpretation-generalization.md)
- Check question: Why is a higher training score from a more complex probe an expected possibility?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $c\in\mathcal C$ | `c in the capacity set C` | probe capacity setting | discrete index |
| $G_c$ | `G sub c` | Generalization gap for each capacity | scalar |
| $A_{\mathrm{null}}$ | `null-control accuracy` | Random-label and random-feature score | scalar |
| $R_{\mathrm{shift}}$ | `risk under distribution shift` | shifted population risk | scalar |

## Analysis contract

Use constant, linear, norm-constrained linear, and small MLP probes on the same activation dataset. Treat prompts as the highest-level experimental units and separate training, validation, iid test, and template-shift test data. Finish selecting layers, capacities, and regularization within validation.

Order the capacity ladder according to the actual function sets and constraints. A norm-constrained linear class is a subset of the linear class with that constraint removed, but the constant baseline and a particular MLP do not automatically form a single chain of inclusions with them. Record whether an intercept is permitted, the norm type and bound, and the MLP width and activation to specify which class $c$ denotes. Also distinguish the objective computed by the optimizer from the evaluation loss, and calculate train/test risks using the same evaluation loss.

Group token and paraphrase rows from each prompt so they cannot cross split boundaries, and choose a token average or prompt average. An iid test of new prompts sharing the same templates and a shift test excluding entire templates target different populations. Lock the outer test, then perform all preprocessing and candidate selection inside training/validation. If training and validation will be combined for refitting after final selection, specify that procedure in advance and update the record of which data define training risk. Choosing candidates again after seeing the final test no longer provides independent evaluation.

First fix the actual class-inclusion relationships and the branches to evaluation populations after selection.

<figure class="lesson-figure" markdown="1">

![A bounded weight disk is a subset of the full linear weight plane, while constant and MLP classes are kept as separately specified families.](../../figures/assets/A09-LRN/A09-LRN-08-norm-class-subset-not-universal-ladder.svg)

<figcaption>For linear classes with the same feature map and intercept rule fixed, the weight disk with norm bound B=1 is a subset of the full weight space. This relationship alone does not automatically include the constant class and a particular MLP. The weight points are illustrative, not learned probes.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A frozen selection protocol branches to IID test, template-shift test, and an independently trained model evaluation.](../../figures/assets/A09-LRN/A09-LRN-08-frozen-protocol-population-branches.svg)

<figcaption>Freeze the protocol selected within training/validation, then separate IID, template-shift, and independent model-seed evaluations. Decide in advance whether to refit on each model or transfer the existing probe. This is an experimental design, not a display of measured scores.</figcaption>

</figure>

## Measurement procedure

1. Calculate training, iid test, and shift test risk for each capacity.
2. Use prompt bootstrap to obtain intervals for gaps and model differences.
3. Repeat the same selection pipeline with label permutations and matched random features.
4. For linear classes, record weight and input norms and the empirical Rademacher upper bound.
5. Repeat the selected probe protocol unchanged on independent model seeds.
6. Perform selected-direction interventions as separate functional tests.

For each $c$, the observed gap $G_c$ is iid test risk minus the corresponding training risk. Shift risk minus training risk also includes a distribution change, so do not call it the same $G_c$. When comparing two models or probes, resample loss differences on the same test prompts; to report a difference in gaps, also subtract the training-risk difference. Test bootstrap describes evaluation uncertainty for a fixed learning outcome. Including variability in learning and selection requires repeating those inner procedures within each resample.

First specify which relationship the null breaks in each random-label or random-feature control. Exchangeable units differ depending on whether labels are prompt-level or token-level. Rerun preprocessing and validation selection under the same rules for each control, without using testing for selection. Although the two controls may be recorded with the same accuracy symbol, they use different nulls; do not combine their results as though they were one control.

For a linear class, $B/n\sqrt{\sum_i\|x_i\|_2^2}$ is an upper bound on empirical Rademacher complexity for the fixed sample. That number itself is not a high-probability risk-gap bound. Loss Lipschitz and boundedness conditions and concentration terms must be added, and the sampling unit represented by $n$ must match the theorem. Do not insert a count of dependent token rows for $n$ and claim a stronger prompt-generalization guarantee. Analyze a probe with one independent input defined per prompt, or construct the bound for a class of prompt-average loss functions. Without those conditions, existing row-level complexity values should be recorded only as conditional class comparisons.

For independent model seeds, repeat a protocol with fixed selection rules, split-generation rules, and hook/label definitions. Distinguish fitting new probes for each model from transferring an existing probe unchanged; do not claim transfer success when the experiment did not require the latter. Direction interventions measure output effects separately from probe evaluation. Do not assume that the same feature index denotes the same direction in a new model. This capstone designs and records these procedures; it does not require running new models or generating new results.

The following figures distinguish the comparisons, nulls, guarantees, and interval scopes associated with each measurement.

<figure class="lesson-figure" markdown="1">

![Illustrative train, IID-test, and shifted-test risks separate the IID gap zero point zero four from a shift-containing contrast zero point one five.](../../figures/assets/A09-LRN/A09-LRN-08-iid-gap-versus-shift-contrast.svg)

<figcaption>With illustrative risks of 0.10 for training, 0.14 for IID testing, and 0.25 for shift testing, the IID gap is 0.04. The contrast shift−train=0.15 also contains distribution change and is not the same IID gap. This small calculation matches the observed gap 0.04 in the text; it is not an actual probe experiment.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Three paired feature-label layouts distinguish real pairing, permissible label permutation, and matched random features before rerunning selection.](../../figures/assets/A09-LRN/A09-LRN-08-different-control-null-relations.svg)

<figcaption>Random-label controls change label correspondences within the declared exchangeable units; random-feature controls change relationships on the feature side. Both rerun the same preprocessing and selection rules but represent different nulls. The connecting lines show data pairing, not causal paths within the model.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![A gate separates the sample-conditional complexity upper bound from a high-probability risk bound requiring loss, concentration, and sampling conditions.](../../figures/assets/A09-LRN/A09-LRN-08-complexity-to-risk-bound-gate.svg)

<figcaption>B/n·√Σ‖xᵢ‖² bounds class complexity on a fixed sample. Connecting it to a risk-gap bound requires verified loss conditions, concentration terms, and independent sampling units that match the theorem. Replacing independent n with a count of dependent token rows invalidates this connection.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Two resampling routes contrast test-only uncertainty for a fixed predictor with repeating fitting and selection before evaluation.](../../figures/assets/A09-LRN/A09-LRN-08-conditional-versus-pipeline-interval.svg)

<figcaption>The upper route addresses only test-sampling uncertainty for an already fixed predictor. To include learning and selection variability in the lower route, repeat the inner fit and selection in every trial. Record separately which row, prompt, or model units were resampled.</figcaption>

</figure>

## Results table

| Evidence | Question it answers | Question it does not answer |
|---|---|---|
| iid test risk | Prediction in the same population | distribution shift |
| shift risk | Transfer under the specified shift | All domains |
| random-label control | pipeline memorization | causal use |
| complexity bound | Upper bound on uniform deviation | Exact observed gap |
| intervention | Output effect of the specified manipulation | A unique mechanism |

Attach the loss, class, selected layer, fit data, number of independent units, and evaluation population to values in the table. For a bound, specify which quantity it bounds and under which theorem conditions. For an interval, state whether it includes only test sampling or also retraining. Leave unmeasured cells unmeasured; do not fill them with theoretical values or numbers from another split.

For example, if the observed gap is 0.04 and the theoretical upper bound is 0.8, the small measured value does not contradict the large upper bound. But this alone does not make the bound tight or establish a gap of 0.04 in another population. Separate iid, template-shift, and model-seed results, concluding recoverability within the scope checked and output effects confirmed by separate interventions.

Read the bound alongside the measurement, and keep conclusions within the populations and model scope checked.

<figure class="lesson-figure" markdown="1">

![A gap magnitude zero point zero four lies well inside an upper limit zero point eight without asserting the bound is tight.](../../figures/assets/A09-LRN/A09-LRN-08-loose-bound-observed-gap.svg)

<figcaption>The text's 0.04 and upper bound 0.8 are shown on a common axis. A small measurement below a large upper bound is neither a contradiction nor evidence that the bound is tight. Record separately whether the bound's theorem conditions and uncertainty scope were actually checked.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![The lesson exercise scenario limits a recoverability claim to one model after prompt and template success but failure on a new model seed, with intervention unmeasured.](../../figures/assets/A09-LRN/A09-LRN-08-recoverability-claim-boundary.svg)

<figcaption>This visualizes the scenario in existing exercise 4. Record prompt and template generalization for that model separately from failure on a new model seed. If separate interventions were not measured, do not fill the gaps with claims of functional use or generalization across all models. The figure does not generate new results.</figcaption>

</figure>

## Common misconceptions

- The probe with the highest test score is not the representation's uniquely correct explanation.
- A loose bound and good empirical generalization are not contradictory.

## Exercises

### 1. Selection
After choosing one of four capacities using validation, on which split should the final iid score be reported?
<details><summary>Show solution</summary>

Report it on an independent iid test split not used for capacity selection.
</details>

### 2. Null
What should you suspect if both real-label and random-label scores are high?
<details><summary>Show solution</summary>

Suspect memorization due to excessive probe capacity, leakage, or non-independent splits.
</details>

### 3. Bound
Why is an observed gap of 0.04 not contradictory when the theoretical upper bound is 0.8?
<details><summary>Show solution</summary>

An upper bound gives the worst-case permitted range and need not be tight for the actual data and algorithm.
</details>

### 4. Claim
The probe works well on iid and template-shift tests but fails on an unseen model seed. How should you conclude?
<details><summary>Show solution</summary>

Limit the conclusion: prompt and template generalization were observed for that model, but representation generalization across seeds was not confirmed.
</details>

## Evidence and update boundaries

This capstone connects the roles of VC, Rademacher, and PAC theory to an empirical probe protocol. Do not change the class or norms post hoc to fit a theoretical bound.

## Lesson summary

- Separate capacity selection from final evaluation.
- Record iid, shift, and model generalization as separate risks.
- Null controls and complexity bounds serve different roles.
- Treat interventions as functional evidence separate from recoverability.

## Pass criteria

- Can you complete a class–sample–selection–risk–control contract?
- Can you distinguish bounds, empirical gaps, and functional use?

## Next lesson

- The next optional module is A09-KER.

## Author checklist

- [x] The analysis contract for complexity and multiple generalization axes is complete.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
