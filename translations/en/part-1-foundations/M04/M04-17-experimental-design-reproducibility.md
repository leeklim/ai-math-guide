---
id: "M04-17"
title: "Experimental design and reproducibility"
part: 1
stage: "M04"
status: "complete"
prerequisites:
  - "M04-06"
  - "M04-07"
  - "M04-09"
  - "M04-10"
  - "M04-16"
estimated_time: "170–210 minutes"
---

# M04-17. Experimental design and reproducibility

## Why this lesson matters

Even a good statistic cannot rescue a design with an unclear question or experimental unit. Counting thousands of tokens from the same model checkpoint as independent replicates makes uncertainty appear small. Choosing a method after inspecting the test set and then reporting that test score as final performance makes performance appear optimistic.

Experimental design connects the claim, estimand, experimental unit, treatment, control, outcome, and analysis rule before looking at the data. Reproducible reporting requires more than saving code and a seed. Data versions, splits, preprocessing, the environment, exclusion rules, and results from every run are also needed for others to check the same calculation and test the claim under different conditions.

## Learning objectives

After this lesson, you will be able to:

- Turn a research claim into an estimand and a measurable outcome.
- Distinguish an experimental unit from an observation row.
- Explain the roles of treatment, control, random assignment, and blocking.
- Distinguish the roles of training, validation, and test splits from leakage.
- Choose an analysis unit appropriate for seed repetitions and a paired design.
- Separate exploratory analysis from confirmatory testing.
- Report effect estimates, uncertainty, and multiple-comparison information together.
- Design negative, positive, and specificity controls for AI model-interpretation experiments.

## Prerequisite check

- Prerequisite lesson: [M04-06 Samples, populations, and sampling distributions](M04-06-samples-populations-sampling-distributions.md)
- Prerequisite lesson: [M04-07 Estimation, bias, and variance](M04-07-estimation-bias-variance.md)
- Prerequisite lesson: [M04-09 Confidence intervals and bootstrap](M04-09-confidence-intervals-bootstrap.md)
- Prerequisite lesson: [M04-10 Hypothesis testing and multiple comparisons](M04-10-hypothesis-testing-multiple-comparisons.md)
- Prerequisite lesson: [M04-16 Correlation and causation](M04-16-correlation-causation.md)
- Check: Can you explain why a sampling unit and a sample row can differ?
- Check: Can you distinguish an effect estimate from a p-value?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions and scope |
|---|---|---|---|
| $i$ | `i` | Experimental unit index | Basic unit of independent assignment |
| $T_i$ | `T sub i` | Treatment assignment for unit $i$ | Binary or multiple arms |
| $Y_i$ | `Y sub i` | Prespecified outcome | Includes the measurement time |
| $\Delta$ | `delta` | Target treatment contrast | For example, a mean difference |
| holdout set | `holdout set` | Evaluation data reserved from method selection | Repeated inspection can contaminate it |
| seed | `seed` | Initial state of a pseudorandom sequence | Distinct from independent data |
| preregistration | `preregistration` | Recording hypotheses and an analysis plan before examining results | Does not prohibit exploration |
| pseudoreplication | `pseudoreplication` | Counting dependent rows as independent replicates | Distorts standard errors |

## Core concept 1. Turn a claim into an estimand and measurement

“Method A is better” is not enough to construct an experiment. At minimum, specify:

- Target population: Which tasks, prompts, models, and deployment conditions does the claim generalize to?
- Treatment: Exactly what differs between A and B?
- Outcome: What is measured—accuracy, log loss, or an intervention effect—and at what time?
- Estimand: What is being estimated—a mean of unit-level differences, a population risk difference, or a subgroup effect?

Define the two methods' scores on the same prompt $i$ as $Y_i(A),Y_i(B)$. The paired mean-difference estimand is

\[
\Delta
=\mathbb E_i[Y_i(A)-Y_i(B)]
\]

Changing the target prompt population or the score definition changes the quantity $\Delta$.

## Core concept 2. The experimental unit is the entity receiving independent assignment

An experimental unit is the smallest unit to which treatment is assigned independently or at which a replicate is generated independently. Tokens from 1000 prompts produced by one model seed are not 1000 independent model training runs.

Counting multiple rows within a unit as independent samples creates pseudoreplication, inflating the effective sample size. Tokens within a prompt, images within a patient, and checkpoints within a model seed have a cluster structure. Analysis and bootstrap must reflect the independent unit to which the claim is intended to generalize.

This does not make numerous lower-level rows useless. Token or prompt observations help estimate variation within one checkpoint. They simply cannot each be counted as a new training run when they share that checkpoint. Comparing unit-level summaries or using an analysis that preserves the cluster structure uses information from lower-level observations without inflating the number of independent replicates. First decide which level of variation is being estimated.

Grouping rows by their independent run makes the rule for counting replicates explicit.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

  ![Three independent training runs each contain ten thousand dependent token rows without creating thirty thousand training replicates](../../figures/assets/M04/M04-17-clustered-runs.svg)

  <figcaption>The three training runs in Example 1 are shown as separate clusters. A run's 10,000 token rows provide more information within that checkpoint, but do not create new training replicates. There are 3 independent runs for generalization across training seeds. This does not prohibit token-level analysis.</figcaption>
</figure>

## Core concept 3. Controls prevent differences other than the treatment

A control condition is a comparison condition without the treatment or with a reference treatment. The two conditions should share the same code path, compute budget, data order, and evaluation procedure except for the intervention of interest.

Useful controls in AI experiments include:

- Negative control: A random direction, shuffled label, or unrelated task for which no effect is expected.
- Positive control: A condition checking whether the pipeline detects a known effect.
- Specificity control: An outcome checking whether general capabilities beyond the target behavior are also damaged.
- Sham intervention: A condition with the same intervention procedure but no change to the target component.

Without controls, it is difficult to distinguish an output change due to the target mechanism from one due to a generic perturbation.

Compare how the direction of interest and a norm-matched random direction change each task.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

  ![Two constructed ablation patterns compare target and norm matched random directions across target and unrelated task accuracy](../../figures/assets/M04/M04-17-control-specificity.svg)

  <figcaption>These are two constructed cases, not actual model measurements. On the left, target-accuracy damage is similar at −8 and −7 points, and both manipulations produce a −3-point change in unrelated-task accuracy, leaving generic damage as an explanation. On the right, only the target direction causes substantial damage, while unrelated-task performance is preserved—a more selective pattern. Even the latter is not proof of a mechanism before positive and sham controls, uncertainty across multiple units, and intervention validity are checked.</figcaption>
</figure>

## Core concept 4. Random assignment and blocking improve the fairness of comparisons

Random assignment prevents systematic connections between pretreatment variables and treatment assignment. If imbalance in an important variable is a concern in a small sample, assignment can be randomized within blocks.

For example, divide prompts into easy and hard difficulty blocks and randomize method order within each block. Preserve the block or paired structure in the analysis as well. Selecting only favorable seeds after randomization undermines, at the reporting stage, the comparability that assignment created.

When blinding is possible, keep annotators unaware of the condition to reduce bias in subjective ratings. Even with an automatic metric, condition-specific differences in preprocessing code can cause measurement bias.

Blocking does not make different difficulty levels identical. It divides the assignment scope so that treatments are compared within similar levels of difficulty. When combining within-block differences into an overall effect, account for each block's proportion in the target population. Collecting equal numbers of easy and hard prompts does not imply equal proportions in the target population. In a paired experiment, also distinguish randomizing method execution order from assigning treatment to units, according to which order effects are being controlled.

Read assignment within blocks separately from the target proportions across blocks.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

  ![One possible balanced assignment within easy and hard blocks differs from weighting their contrasts by target population proportions](../../figures/assets/M04/M04-17-blocked-assignment.svg)

  <figcaption>This is one possible assignment of each block's four units, two to A and two to B. With assumed block-level mean differences 0.1 and 0.2, averaging the two equally sized blocks gives 0.15. If the target's easy and hard proportions are 0.25 and 0.75, the target-weighted mean of the same differences is 0.175. A single assignment is not assumed to balance every cause exactly.</figcaption>
</figure>

## Core concept 5. Training, validation, and test sets serve different decisions

The training set is used to fit parameters, the validation set to select hyperparameters and methods, and the test set to evaluate the final selected procedure. Changing features, prompt templates, or stopping rules after inspecting test results turns the test set into validation data.

Data leakage occurs when information about evaluation outcomes enters training or selection. Examples include:

- Normalizing with all data before splitting.
- Placing near-duplicates of the same document in training and test sets.
- Adjusting prompts or thresholds after looking at test labels.
- Selecting a method family through repeated inspection of a test benchmark.

Use the final holdout, as far as possible, once after fixing the analysis plan. A benchmark repeatedly used during development can no longer be called an untouched test set.

Preprocessing that estimates parameters from data is also part of fitting. In an independent holdout evaluation, estimate normalization means and standard deviations from the training split and apply those same values to validation and test data. Calculating them from all data before splitting introduces the test feature distribution into the training procedure. When observations are dependent, split by units such as documents or patients, so that the test set does not effectively revisit another row from the same unit.

Split boundaries are boundaries on information passed to fitting, selection, and evaluation.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

  ![Training fitting validation selection and frozen test evaluation form distinct decision roles while test feedback to selection breaks the holdout boundary](../../figures/assets/M04/M04-17-split-decision-boundaries.svg)

  <figcaption>Training fits parameters, and validation selects candidates and settings. Test evaluation follows after the procedure is fixed. Feeding test results back into selection, as in the dashed path below, removes the untouched-holdout role even if the file is still named test.</figcaption>
</figure>

Preprocessing that estimates values from training data must respect the same boundary.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

  ![A normalizer fitted only on training values has different parameters and held out transform than a normalizer fitted after mixing the test value](../../figures/assets/M04/M04-17-preprocessing-fit-boundary.svg)

  <figcaption>Using the empirical population standard deviation for training values [0,2] gives μ=1 and σ=1, so test value 8 has z=7. Including the test value in [0,2,8] changes these to μ≈3.333 and σ≈3.399, giving z≈1.373. In an independent holdout evaluation, the fitting on the right uses test feature information in preprocessing. This constructed calculation uses variance with denominator n for each dataset, distinct from the n−1 denominator in sample variance.</figcaption>
</figure>

Track source documents as well to check whether dependent rows cross the split boundary.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

  ![A row level split places dependent chunks from every document on both sides whereas a document level split keeps each source group together](../../figures/assets/M04/M04-17-group-versus-row-split.svg)

  <figcaption>A1 and A2, B1 and B2, and C1 and C2 are pairs of dependent chunks from the same respective documents. On the left, every document appears in both training and test data. On the right, assigning whole documents prevents that leakage path. A document-level split alone does not remove every other type of leakage.</figcaption>
</figure>

## Core concept 6. A seed records a source of variation

Seeds are needed to replay initialization, data order, dropout, or sampling sequences. A result from one seed does not capture an algorithm's random variation. Run multiple independent training runs and report every run-level result.

Repetitions that change only the decoding seed for the same trained model measure a different uncertainty from repetitions that change model initialization onward. The replicate unit depends on whether the generalization target is “stochastic output from this checkpoint” or “models produced by this training procedure.”

Report run-level values, sample size, and dispersion or confidence intervals, not just a mean. Selecting the best seed and hiding the others introduces selection bias.

Equal output counts do not imply equal replicate levels: the level depends on where computation was restarted.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

  ![Three decoding repeats of one fixed checkpoint differ from outputs of three separately trained checkpoints despite equal output counts](../../figures/assets/M04/M04-17-training-decoding-levels.svg)

  <figcaption>The left changes the decoding seed three times at the same θ. The right uses θ1, θ2, and θ3 from three runs differing from training randomness onward, including initialization and data order. Despite the same three outputs, the left reflects decoding variation within that checkpoint; the right includes training-run variation. Recording seeds does not itself create independent data or independent training replicates.</figcaption>
</figure>

## Core concept 7. A paired design removes shared difficulty

When methods A and B can be compared on the same prompts, dataset splits, and seed conditions, analyze the unit-level differences

\[
D_i=Y_i(A)-Y_i(B)
\]

The estimated mean difference is

\[
\widehat\Delta
=\frac1n\sum_{i=1}^{n}D_i
\]

Variation shared by both methods, such as prompt difficulty, can cancel in the difference.

If the design is paired, permutation tests or bootstrap must move the pairs together. Shuffling or resampling A and B observations separately loses the original pairing.

For $n\ge2$ independent pairs from the same distribution with finite variance, estimate the standard error of the mean difference by dividing the sample standard deviation of the $D_i$ values by $\sqrt n$. Use variation in differences from the same units, rather than the two scores' separate standard deviations. As in M04-09, positive covariance can reduce shared variation in the difference's variance, but pairing does not always improve precision. If pairs belong to the same training run, dependence within that higher-level cluster remains.

First connect the two scores from each prompt, then place their differences on a separate axis.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

  ![Four prompt matched score pairs share large prompt variation while their differences form the lesson example with mean point zero five](../../figures/assets/M04/M04-17-paired-differences.svg)

  <figcaption>A is constructed by adding the differences D=(0.10,0.04,−0.02,0.08) from Example 3 to B=(0.7,0.6,0.4,0.2). Each line on the left connects a pair from the same prompt; the right shows their differences. The sample mean difference is 0.05. These four observations alone do not establish the target population's Δ. Bootstrap must also preserve pairs and any required higher-level clusters.</figcaption>
</figure>

## Core concept 8. Separate exploration from confirmation

Exploratory analysis finds patterns and generates new hypotheses. Confirmatory analysis evaluates prespecified hypotheses, primary outcomes, exclusion rules, sample sizes, and tests.

Preregistration or a timestamped analysis plan records decisions made before seeing results. It is not a prohibition on exploration, but a way for readers to distinguish planned analyses from those added after examining results.

Searching many layers, heads, prompts, and metrics creates more opportunities for false discoveries. Specify the primary test and either apply multiplicity correction to the others or identify them as exploratory results. A hypothesis selected on exploration data can be evaluated again on an independent confirmation set.

The point at which the candidate and analysis rules are fixed separates the two datasets' roles.

<figure class="lesson-figure" markdown="1">

  ![Candidate head screening on discovery data is followed by a frozen candidate and analysis rule then independent confirmation without reselection](../../figures/assets/M04/M04-17-discovery-confirmation-boundary.svg)

  <figcaption>Fix j*, selected from exploration across 24 heads, before confirmation. Evaluate that head and the prespecified outcome, controls, and analysis on new data. Reselecting a head based on confirmation scores also uses those data for selection. The procedure distinguishes data roles rather than prohibiting exploration.</figcaption>
</figure>

## Core concept 9. Report effect size together with uncertainty

“Statistically significant” alone does not tell us an effect's size or usefulness. A report should include:

- The estimand and point estimate.
- A confidence interval or sampling uncertainty.
- The experimental unit and number of units.
- The treatment, control, and assignment procedure.
- All planned outcomes and correction rules.
- Raw data or unit-level summaries and a record of exclusions.

An effect can be small despite a small p-value. Even with a large p-value, a wide interval may fail to rule out a meaningful effect. Prespecifying a practical threshold separates statistical detectability from substantive importance.

Comparing zero and the practical threshold on the same effect axis separates the questions an interval answers.

<figure class="lesson-figure" markdown="1">

  ![Three illustrative normal mean effect intervals differ in precision exclusion of zero and comparison to a prespecified practical threshold](../../figures/assets/M04/M04-17-practical-effect-threshold.svg)

  <figcaption>With known standard deviation 0.1 for independent normal units, the constructed observed means 0.02, 0.04, and 0.2 use n=1600, 4, and 25, respectively. Their 95% intervals are calculated as mean±1.96×0.1/√n. The first excludes zero but lies below threshold 0.1. The second contains both zero and the threshold. The third lies above the threshold. These are not actual experimental data or results from separate p-value calculations.</figcaption>
</figure>

## Core concept 10. Reproducibility preserves the state needed for execution

Usage of reproducibility and replication varies across fields, so state their operational definitions in the report. This book distinguishes them as follows:

- Repeatability: The same team reruns the calculation with the same code, data, and environment.
- Computational reproducibility: Another person reproduces the same result using the provided code, data, and environment.
- Replication: The scientific claim is tested again with an independent implementation, new data, or a new model.

Preserved artifacts include the code commit, dependency and hardware versions, data sources, licenses and hashes, split indices, model checkpoints, preprocessing, prompts, seeds, commands, configuration, and expected output. Saving only a notebook's last cell output makes the computational path difficult to reconstruct.

## Core concept 11. Model-interpretation experiments connect observations to interventions

An interpretation experiment can be designed with the following structure:

1. Claim: Which component is claimed to be necessary or sufficient for which behavior?
2. Observational screen: Find candidates using activations, attribution, or probes.
3. Intervention: Choose ablation, patching, or steering to match the claim.
4. Controls: Include random and norm-matched controls, unrelated behaviors, and a sham condition.
5. Analysis: Specify the unit, primary outcome, paired contrast, and uncertainty.
6. Validation: Measure the effect again on held-out prompts and across model seeds, sizes, and datasets.

Using the same data for candidate discovery and confirmation produces a winner's curse. Separate the data used to select a head from the data used to evaluate its causal effect.

An observed candidate effect combines the actual effect and sampling error. Selecting the largest observed effect among many candidates tends to select not only candidates with large actual effects, but also candidates whose errors were favorable in this sample. Reporting that candidate's effect again on the same data treats the selected error as part of the effect once more. On separate confirmation data, measure the effect under new sampling variation while keeping the selected candidate and analysis rules fixed. This distinguishes the discovery-stage maximum from the confirmation-stage estimate.

Even when candidates have equal actual effects, the maximum selected during exploration can differ from the estimate on new data.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

  ![A fixed seed simulation of twenty four equally effective candidates selects a high discovery estimate then evaluates that same candidate on independent confirmation noise](../../figures/assets/M04/M04-17-winner-selection.svg)

  <figcaption>This constructed case uses a fixed seed, with actual effect 0.02 for every candidate and independent normal estimation noise with standard deviation 0.04. Head 12, selected during exploration, has an estimate of approximately 0.093; its independent confirmation estimate is approximately 0.034. This is not a neural-model run, nor does it imply that confirmation values always decrease. It illustrates that selected discovery error does not persist unchanged in new data.</figcaption>
</figure>

## Example 1. Mistakenly counting token rows as replicates

Suppose activations for 10,000 tokens are obtained from each of 3 model seeds. If the claim is that an effect persists across changes in training seed, the number of independent runs is 3, not 30,000.

Token-level variation describes uncertainty within each run, but does not replace seed-level generalization. More model runs are needed, or the claim must be limited to the three checkpoints.

## Example 2. Test-set leakage

A researcher inspects test accuracy while comparing 20 learning rates and 10 prompt templates, then reports the best combination using the same test score. The test set was used to select among $200$ candidates, so the reported maximum contains selection bias.

Use validation data for candidate selection, then evaluate the selected procedure once on an untouched test set.

## Example 3. A paired prompt comparison

Suppose the score differences between methods A and B on four prompts are

\[
(0.10,0.04,-0.02,0.08)
\]

The paired mean difference is

\[
\widehat\Delta
=\frac{0.10+0.04-0.02+0.08}{4}
=0.05
\]

To estimate uncertainty, resample prompt pairs as units.

## Example 4. Controls for activation ablation

Suppose removing a particular direction reduces target-task accuracy by $8$ percentage points. If random directions of the same norm also reduce it by $7$ points on average, evidence for target specificity is weak.

Evidence is closer to a mechanism claim if only the target direction causes substantial damage, unrelated-task performance remains intact, and an activation patch restores the behavior. Still report effect estimates and intervals across multiple prompts and model seeds.

## Common misconceptions

### Misconception 1. Many observations mean many independent samples

Rows from the same cluster can share common causes. The experimental unit and dependence structure determine effective sample size.

### Misconception 2. Recording the seed makes one run sufficient

Recording a seed helps rerun that one run. Estimating seed variation in the training procedure requires independent runs.

### Misconception 3. A public benchmark is always a test set

A benchmark becomes selection data when its scores are used to repeatedly revise methods. Even if named a test set, it no longer serves as an untouched holdout.

### Misconception 4. A negative result is a failure of reproduction

Results can differ because of changes in the population, implementation, or power. Check protocol fidelity and uncertainty before revising the claim's scope.

### Misconception 5. Releasing code alone makes an experiment reproducible

Without data versions, checkpoints, preprocessing, the environment, and execution configuration, the same code can produce different results.

## Exercises

### 1. Experimental unit

Each of 20 patients provides 50 images, and treatment is assigned at the patient level. State the experimental unit and the number of image rows.

<details>
<summary>Show solution</summary>

The experimental units are the 20 patients, to whom treatment is independently assigned. There are 1,000 image rows, but images from the same patient form a cluster. Counting all 1,000 as independent treatment replicates is pseudoreplication.

</details>

### 2. Designing controls

Ablating a particular activation direction lowers answer accuracy. Propose two controls for checking whether the effect is target-specific.

<details>
<summary>Show solution</summary>

A negative control can remove a random direction of the same norm or a shuffled target direction. A specificity control measuring unrelated-task accuracy is also needed. A sham operation that follows the ablation procedure without changing the activation checks for code-path effects.

</details>

### 3. The roles of splits

Explain the roles of validation and test sets, and state what changes if a threshold is adjusted after inspecting the test score.

<details>
<summary>Show solution</summary>

Validation data are used to select hyperparameters and decision rules; test data evaluate the selected procedure. Adjusting a threshold based on test scores also uses the test set for selection, so it is no longer an untouched final evaluation set.

</details>

### 4. Seeds and replicates

Text is generated from one checkpoint with 30 different decoding seeds. Determine whether this is sufficient to evaluate the claim that “the method's effect persists across different training seeds.”

<details>
<summary>Show solution</summary>

It is not sufficient. The 30 repetitions measure stochastic decoding variation within one checkpoint. Generalization across training seeds requires multiple independently trained checkpoints with different initializations and data orders.

</details>

### 5. Paired mean difference

On the same three prompts, A and B have scores $(0.8,0.6,0.9)$ and $(0.7,0.5,0.85)$, respectively. Find the paired mean difference for A minus B.

<details>
<summary>Show solution</summary>

The prompt-level differences are $(0.1,0.1,0.05)$. Therefore,

\[
\widehat\Delta
=\frac{0.1+0.1+0.05}{3}
=\frac{0.25}{3}
\approx0.0833.
\]

</details>

### 6. Multiple comparisons and confirmation

A researcher compares probe scores across 24 layers, selects the highest-scoring layer, and reports its p-value on the same data. How should the design change?

<details>
<summary>Show solution</summary>

Using the same data for layer selection and confirmatory testing gives a p-value that ignores selection. Select a layer on a discovery split, then evaluate a prespecified contrast on an independent confirmation split. If multiple layers are tested together on the same data, define the family, apply multiplicity correction, and identify the analysis as exploratory.

</details>

### 7. Cumulative M04 assessment

A new probe has higher concept-classification accuracy than a baseline, and target behavior decreases after ablating the probe direction. Write a one-page analysis plan for evaluating this study. Include the population, unit, estimand, splits, controls, uncertainty, and supported claims.

<details>
<summary>Show solution</summary>

An example plan includes the following elements:

- Population: The specified model family and held-out prompt distribution.
- Unit: Prompts as the basic paired units, with model seeds as independent training replicates.
- Estimand: The accuracy difference between probe and baseline on held-out prompts, and the target-score difference between ablation and sham conditions.
- Splits: Separate probe fitting and candidate discovery from confirmation prompts; do not use the final test for method selection.
- Controls: Label permutation, norm-matched random directions, sham ablation, and unrelated-behavior outcomes.
- Uncertainty: Report effect estimates and intervals separately for prompt-paired bootstrap and seed-level results; apply correction to layer exploration.
- Claims: Probe results alone support decodability, and controlled ablation supports scoped evidence of necessity. Do not claim sufficiency or generalization to other models or populations without separate patching or replication.

Also record data and checkpoint versions, preprocessing, seeds, exclusion rules, and the primary outcome in the analysis plan.

</details>

## Lesson summary

- Experiments start by turning a claim into a population, treatment, outcome, and estimand.
- Experimental units are units of independent assignment or replication and can differ from data rows.
- Negative, positive, specificity, and sham controls check alternative explanations.
- Random assignment, blocking, and blinding reduce bias in comparison and measurement.
- Training, validation, and test splits separate fitting, selection, and final evaluation.
- Define replicates according to the randomness represented by the seed and the generalization target.
- Separate exploratory discovery from confirmatory testing and record multiplicity.
- Report effect estimates, uncertainty, unit counts, and all runs together.
- Reproducible computation requires code, data, the environment, configuration, and splits.
- Model-interpretation experiments separate candidate discovery from confirmation through controlled interventions.

## Pass criteria

You pass when you can answer these questions without consulting the material:

- Can you turn a vague claim into an estimand and an outcome?
- Can you distinguish experimental units from rows?
- Can you design treatments and controls appropriate to a claim?
- Can you identify leakage across training, validation, and test data?
- Can you explain the uncertainty captured by seed repetitions?
- Can you account for paired design and cluster structure in the analysis?
- Can you distinguish exploratory and confirmatory analysis?
- Can you list the records needed for rerunning a calculation and for independent replication?
- Can you write an analysis plan for the statistical evaluation of probe results and the claims they support?

## Next lesson

- [N05-01 Tensors and computation graphs](../../part-2-neural-computation/N05/N05-01-tensors-computation-graphs.md)

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] Claims, estimands, and measurement are connected.
- [x] Experimental units and pseudoreplication are distinguished.
- [x] Controls, randomization, and blocking are explained.
- [x] Splits and leakage are distinguished.
- [x] Seeds, paired design, and multiple comparisons are connected to the analysis unit.
- [x] Artifacts needed for reproducibility are listed.
- [x] The cumulative M04 assessment is included.
- [x] Every exercise has a solution.
- [x] Strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and math delimiters are checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
