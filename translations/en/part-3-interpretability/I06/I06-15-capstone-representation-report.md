---
id: "I06-15"
title: "Capstone exercise: representation report"
part: 3
stage: "I06"
status: "complete"
prerequisites: ["I06-14"]
estimated_time: "180~240 minutes"
---

# I06-15. Capstone exercise: representation report

## Why this lesson matters

Representation analysis does not end with running activation collection, statistics, probes, and visualizations separately. For one question, connect the data definition to controls, uncertainty, and claim boundaries. This lesson brings all of I06 together in a short reproducible-report format.

## Learning objectives

- Write a behavioral or representation question as a single preregistered analysis contract.
- Report the provenance and quality checks of an activation dataset.
- Integrate descriptive statistics, probe controls, and stability results in one table.
- State which claims the results support and which they do not.
- Reproduce the report using code, manifests, and artifact hashes.

## Prerequisite check

- Prerequisite lesson: [I06-14 Writing representation claims](I06-14-writing-representation-claims.md)
- Check question: Why can a report's strongest claim remain `recoverable` even when probe accuracy is high?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| analysis contract | `analysis contract` | A prior specification of data, location, metrics, controls, and stopping criteria | protocol |
| primary estimand | `primary estimand` | The target quantity that the report primarily estimates | population quantity |
| primary metric | `primary metric` | The main evaluation value corresponding to the estimand | scalar or vector |
| sensitivity analysis | `sensitivity analysis` | A check of whether conclusions survive changes to reasonable choices | analysis set |
| artifact manifest | `artifact manifest` | A record linking input, code, model, and result hashes with resources | JSON document |
| bounded conclusion | `bounded conclusion` | A conclusion limited to the evidence and tested scope | report statement |

## 1. The report's question

An example question is:

> At the last token of the layer 5 MLP update in Pythia-160M `step143000`, is there linear information that distinguishes place and animal prompt conditions?

The primary estimand is the accuracy difference between a held-out linear probe and a matched control over a predefined prompt population. The pilot's 8 inputs validate the pipeline; they are not a sample for full statistical inference. A formal report needs a larger set of independent inputs and a group split.

$$
\Delta_{\mathrm{sel}}
=
\mathbb{E}[A_{\mathrm{task}}-A_{\mathrm{control}}]
$$

Here, $A_{\mathrm{task}}$ and $A_{\mathrm{control}}$ are held-out accuracies obtained with the same split and tuning budget. The difference computed from a sample is an estimate of $\Delta_{\mathrm{sel}}$, not the estimand itself.

When using an expectation, specify what is repeated and averaged. The target differs, for example, between repeatedly drawing training and test inputs and randomizing control labels under the same procedure, and changing only training seeds on fixed data. Within each repetition, match task and control splits, calculate their difference, and estimate uncertainty in that difference. Subtracting scores obtained from different input sets mixes input-composition differences into selectivity. Report task and control accuracy as well as the difference, so the performance levels underlying the same difference are visible.

Match task and control within each repetition before discussing their expectation.

<figure class="lesson-figure" markdown="1">

![Task and control accuracies arise from the same input split in repetition r and feed a paired difference, while the expectation depends on which inputs labels or seeds repeat.](../../figures/assets/I06/I06-15-paired-selectivity-estimand.svg)

<figcaption>Compute the task–control difference Δʳ on the same split within each repetition r. The target of the expectation depends on which inputs, control labels, and seeds are repeated. This diagram specifies a repetition contract; it does not create new accuracy results.</figcaption>
</figure>

## 2. Required report structure

### A. Data and measurement

- Input source, inclusion and exclusion criteria, and group IDs.
- Model and tokenizer repositories, requested revisions, and resolved SHAs.
- Module, layer, token, and component.
- Sample count, sequence lengths, and missing or duplicate entries.
- Activation shape, dtype, and artifact hash.

### B. Analysis plan

- Primary estimand and metric.
- The unit for training, validation, and test splits.
- Probe class, regularization, and tuning budget.
- Label and input-only controls.
- Number of seeds and uncertainty method.
- Selection rules when examining multiple layers or coordinates.

### C. Results

- Norm and coordinate distributions and outlier provenance.
- Effect sizes and confidence intervals.
- Task and control scores and selectivity.
- Auxiliary analyses needed for the question: PCA, CKA, RSA, or feature stability.
- Items that failed predefined criteria.

### D. Conclusion

- The supported claim level.
- Alternative explanations.
- The tested generalization scope.
- Intervention experiments needed next.

## 3. Failure gate

If any of the following occurs, do not write a strong conclusion; revise collection or design.

- The hook-call count does not match the number of input rows.
- The same original-text group appears in multiple splits.
- The test set was used to select layers or hyperparameters.
- Control and task have different tuning budgets.
- The artifact source hash differs from the current code.
- Results depend on one seed or a few outliers.

Do not cover up a failure with another analysis.

These failures are not all of the same kind. Broken row correspondence or overlapping splits violate the data or evaluation contract, so fix that collection or evaluation first. If collection and evaluation are valid but the result is sensitive to seeds or outliers, the sensitivity itself is a result to report. Adjust uncertainty and conclusion scope instead of selecting favorable seeds or removing outliers after seeing the results.

A broken contract and sensitivity in a valid analysis require different next steps.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Contract violations route to stopping and fixing collection or evaluation, whereas valid analyses with seed or outlier sensitivity route to reporting uncertainty and narrower claims.](../../figures/assets/I06/I06-15-failure-versus-sensitivity.svg)

<figcaption>Fix collection or evaluation first if the hook, row, or split contract is broken. If the contract is valid but results are sensitive to seeds or outliers, report that sensitivity and adjust uncertainty and claim scope. Do not treat both cases as the same failure.</figcaption>
</figure>

## 4. CPU capstone exercise

For an 80×8 synthetic representation, combine condition-specific mean differences, a held-out probe, a shuffled-label control, selectivity, and rotation CKA in one report object.

<!-- I06_EXAMPLE: i06_15_representation_report -->

The report's conclusion is limited to `the label was recovered linearly on this synthetic held-out sample`. Functional use and causal interventions were not tested.

## 5. Connect the Pythia pilots

Actual model results remain in the 160M activation dataset from I06-02 and the 410M scale-comparison manifest from I06-08. Instead of copying only numbers, link the following provenance in the report.

- 160M resolved SHA `c54a0e0b28cc667b6f278803024438d57f847b5d`
- 410M resolved SHA `c66f7467608ffee8fca0d28cf1f46a7574b53cec`
- Fixed prompt hash and source hash.
- Layer 5 and 11 MLP down projections, last token.
- Peak VRAM, run time, and artifact bytes.

These SHAs identify the current pilots. Do not assume that the `step143000` branch will always point to the same target. The local manifest is the reference for the actual reproduction record.

Keep the links identifying the inputs, models, hooks, and artifacts behind each value.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Shared prompt and source hashes feed the two resolved Pythia model and hook contracts, yielding eight by 768 and eight by 1024 local artifacts linked to local comparison and resource records.](../../figures/assets/I06/I06-15-pilot-provenance-links.svg)

<figcaption>Link the hash of the same eight prompts, each resolved SHA, and each hook location to activation artifacts and local manifests. The SHAs shown are prefixes of the full identifiers in the text. Do not rerun or add values and resource statistics to Git. Pilot provenance is not evidence of population generalization.</figcaption>
</figure>

## 6. Report assessment table

| Question | Pass criterion | Action on failure |
|---|---|---|
| Do the data represent the question? | A predefined population, controls, and group split | Revise the sample and scope |
| Is the location correct? | Check module path, shape, and hook-call count against each other | Stop collection and fix the hook |
| Is the effect stable? | Its direction persists across seeds, bootstrap, and sensitivity checks | Increase uncertainty or withhold the conclusion |
| Does the probe read information? | Improvement over held-out baselines and controls | Withhold the recovery claim |
| Does the model use it? | Functional tests or interventions | Test separately in I07 |

## Common misconceptions

### Misconception 1. More analyses make a report stronger

Analyses unrelated to the primary question may only increase selection opportunities. Distinguish the primary estimand from auxiliary analyses.

### Misconception 2. A manifest makes the research conclusion reproducible

A manifest supports computational provenance. Empirical replication of the conclusion on other samples or seeds is separate.

### Misconception 3. A capstone report can use a little causal language

Observational and recovery results in I06 alone do not support causal claims. Intervention designs from I07 are needed.

## Exercises

### 1. Primary estimand

Narrow `look at place information` to a single primary estimand.

<details><summary>Show solution</summary>For example, write `the difference between held-out linear-probe accuracy and matched shuffled-label control accuracy for the last-token activation at layer 5 over a predefined population of place and animal prompts`.</details>

### 2. Provenance

Only a model ID and `step143000` were recorded. What else is needed?

<details><summary>Show solution</summary>A resolved immutable SHA, tokenizer ID and SHA, source and input hashes, module, layer, token, dtype, seeds, and environment versions are needed.</details>

### 3. Failure gate

The hook fires twice per input. Should report computation continue?

<details><summary>Show solution</summary>Stop. Check for module reuse or duplicate registration, restore the correspondence between rows and inputs, and then collect again.</details>

### 4. Control

Task accuracy is 0.88 and control accuracy is 0.85. What is the conclusion?

<details><summary>Show solution</summary>Selectivity is small at 0.03, so probe capacity or identity memorization is difficult to rule out. Withhold the representation-specific recovery claim.</details>

### 5. Scope

Can results from 8 English prompts be generalized to Korean prompts?

<details><summary>Show solution</summary>No. Limit the scope to the English pilot and repeat separately with a Korean tokenizer and Korean inputs.</details>

### 6. Next experiment

What type of experiment is needed to test functional use after recoverability?

<details><summary>Show solution</summary>Controlled ablation, patching, or steering of the probe direction or related activations, with behavioral metrics and random or magnitude-matched controls, is needed. This is the scope of I07.</details>

## Evidence and update boundaries

The report structure integrates the measurement, statistics, control, and stability rules of I06-01~14. Actual Pythia values are checked in local manifests, not added to Git. A pilot with few prompts is a reproduction check for the environment and analysis path, not a population conclusion.

## Lesson summary

- A representation report connects its question, data, collection, statistics, controls, and claims in one contract.
- Distinguish the primary estimand from auxiliary analyses.
- Provenance and hashes check computational reproducibility; repeated seeds and datasets check conclusion stability.
- I06 results support observational and recovery claims; function and causation require separate experiments.

## Pass criteria

- Can you write a representation question as a complete analysis contract?
- Can you check the data, hook, probe, control, and stability gates?
- Can you distinguish the supported claim from the next intervention experiment?

## Next stage

- [I07-01 Sensitivity and attribution](../I07/I07-01-sensitivity-attribution.md)

## Author checklist

- [x] Data definition and claim scope are connected in one report.
- [x] 160M is the main model, and 410M is used only for scale comparison.
- [x] Every exercise has a solution.
- [x] The strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and mathematical rendering have been checked.
