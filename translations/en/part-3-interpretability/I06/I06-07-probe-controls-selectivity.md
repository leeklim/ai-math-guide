---
id: "I06-07"
title: "Probe Controls and Selectivity"
part: 3
stage: "I06"
status: "complete"
prerequisites: ["I06-06"]
estimated_time: "100–130 minutes"
---

# I06-07. Probe Controls and Selectivity

## Why this lesson matters

A probe measures not only the representation but also the probe's own learning capacity. With high-dimensional activations and a small sample, it can memorize even arbitrary labels to some extent. A control task with the same capacity and training procedure puts performance on the actual task in context.

## Learning objectives

- Distinguish the purposes of label controls and representation controls.
- Apply the same probe protocol to the actual task and the control task.
- Calculate selectivity and interpret it together with uncertainty.
- Explain how seed and hyperparameter selection affect a control comparison.

## Prerequisite check

- Prerequisite lesson: [I06-06 Linear probe](I06-06-linear-probe.md)
- Check question: Is it a fair comparison to tune regularization only for the actual-label probe while leaving the control probe fixed?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $A_{task}$ | `task accuracy` | Held-out accuracy on actual labels | $[0,1]$ |
| $A_{control}$ | `control accuracy` | Held-out accuracy on control labels | $[0,1]$ |
| $S=A_{task}-A_{control}$ | `selectivity equals task accuracy minus control accuracy` | Difference between task and control performance | $[-1,1]$ |
| control task | `control task` | Comparison task measuring how much a probe can memorize | evaluation design |
| label permutation | `label permutation` | Random rearrangement that breaks the label-input relationship | randomized control |
| probe capacity | `probe capacity` | Ability of the probe's function class to fit data | model property |

## 1. What is being controlled?

A label permutation randomly changes the correspondence between the original labels and representations. Shuffle the training labels while retaining the same inputs, splits, dimension, probe class, and tuning budget as the actual task. Control test labels must also follow the same mapping rule.

In language probing, a control task assigning a fixed random label to each word type measures the probe's ability to memorize using type identity. This asks a different question from independently drawing a new label for each row.

In a type-level control, another occurrence of the same word receives the same random label. If a type seen during training also appears in the test set, the probe can reuse the memorized mapping. This control therefore reveals the ability to read type identity. With per-row random labels, even the same type can receive different labels, so there is no such mapping. The original paper uses the former control. [Hewitt and Liang's control task](https://aclanthology.org/D19-1275/)

This lesson's CPU lab permutes the entire label column once and retains the original train/test indices. It does not construct a word-type mapping, and a single shuffle can leave chance correlations between labels and activations. What was randomized determines what the control performance means.

Representation controls are also possible. Replace activations with random features, input length, token identity, or an untrained model's representations to compare which information sources produce the performance.

The control question changes with what is shuffled or replaced.

<figure class="lesson-figure" markdown="1">

![Four fixed representation rows retain their order while a toy label column is permuted, breaking its original row correspondence.](../../figures/assets/I06/I06-07-label-permutation.svg)

<figcaption>Change the label correspondence while retaining activation rows and the original split. The four rows illustrate rearrangement conceptually; they do not show actual control accuracy.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Repeated apple and pear contexts receive consistent labels under a fixed type control but may receive conflicting labels under per-row noise.](../../figures/assets/I06/I06-07-type-versus-row-control.svg)

<figcaption>A word-type control uses the same random label whenever apple occurs again. Per-row random labels can give the same word different labels, so they ask a different question from whether a memorized type mapping carries over to the test set.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![Alternate information sources feed the same probe protocol and held-out metric, changing representation input while preserving evaluation.](../../figures/assets/I06/I06-07-representation-control.svg)

<figcaption>A representation control changes the probe's input information source. Retaining the same split and evaluation rules allows a comparison of whether activation performance goes beyond sources such as length and identity.</figcaption>
</figure>

## 2. Selectivity

Using the same metric, define selectivity as

\[
S=A_{task}-A_{control}
\]

Higher task accuracy together with lower control accuracy strengthens the interpretation that the probe used the actual representation-label relationship.

Selectivity alone is not enough. Report both accuracies, class balance, and variation across seeds. The practical meaning of $S=0.2$ differs depending on whether it comes from $0.9-0.7$ or $0.6-0.4$.

Equal differences do not put the two performance values at the same levels.

<figure class="lesson-figure" markdown="1">

![Two accuracy intervals have the same 0.2 selectivity gap but lie at task control values 0.9 0.7 and 0.6 0.4.](../../figures/assets/I06/I06-07-selectivity-original-values.svg)

<figcaption>The two examples in the text have the same selectivity of 0.2 but different task and control performance levels. Report both original values together with class balance and variation across seeds.</figcaption>
</figure>

## 3. A contract for a fair comparison

Keep the following the same for the task and control.

- Train, validation, and test rows and group splits
- Probe architecture and parameter count
- Regularization candidates and number of tuning trials
- Optimizer, steps, and early stopping
- Metric and class weighting
- Number of seeds and reporting method

Giving only the control less tuning can artificially lower its performance. Conversely, state whether simply copying the task's hyperparameters to the control is equivalent to giving each task the same selection budget.

Match not only the parameter count but also the opportunities to select a high value.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Thirty task candidates versus one control candidate give mismatched selection opportunities; a matched design gives both sides the same search and validation rule.](../../figures/assets/I06/I06-07-selection-budget.svg)

<figcaption>The exercise's 30-to-1 search opportunities show why equal probe capacity alone does not make a comparison fair. Give both tasks the same candidates and selection budget, and apply the same selection procedure in each control repetition.</figcaption>
</figure>

## 4. The permutation distribution

A single shuffle can be easy or difficult by chance. Obtaining $A_{control}^{(r)}$ from multiple permutations lets you examine the control distribution and where task performance lies relative to it. Record the split and permutation seeds in the manifest.

Only the label correspondence changes across repetitions; the original representation and comparison procedure remain fixed. With repeated measurements from the same sentence or type, decide whether to retain those groups and which units to shuffle. Independent row shuffling and a fixed mapping by group are different controls, so do not combine their results into one control distribution.

If all 12 layers, five labels, and three probes were explored, the controls must undergo the same selection procedure. Comparing only the best task score with the mean control score does not match selection opportunities.

When repeating a comparison, track what changes and what stays fixed.

<figure class="lesson-figure" markdown="1">

![Different label permutations pass through the same fixed representation split and selection protocol, producing control accuracies to compare as a distribution.](../../figures/assets/I06/I06-07-repeated-control-contract.svg)

<figcaption>Only label correspondence changes across repetitions; the rest of the contract remains fixed. The figure shows the procedure for producing a distribution, not actual measurements or significance results. Do not combine independent row shuffling and group mappings into the same distribution.</figcaption>
</figure>

## CPU lab

Train the same ridge probe on the same eight-dimensional representation as in I06-06. Calculate the difference in test accuracy between actual labels and labels shuffled with a fixed seed.

<!-- I06_EXAMPLE: i06_07_probe_control -->

This example is a pilot using only one control. An actual report should include the distribution across multiple shuffles and a confidence interval.

## Common misconceptions

### Misconception 1. Random-label accuracy is always at chance

A high-dimensional probe's ability to fit random training labels differs from its ability to predict independent test labels. If test labels are independent of inputs, training memorization alone does not support an expectation of systematic improvement on the test set, though accuracy can be high by chance on a small test set. In a fixed type-label control, identities shared between train and test can carry a memorized mapping over to the test set.

### Misconception 2. Positive selectivity means the model uses the information

It is evidence that task labels are more recoverable from the representation than control labels. It is not evidence of downstream use by the model.

### Misconception 3. Equal probe parameter counts make a comparison fair

Tuning budgets, steps, early stopping, and the number of selection opportunities must also match.

## Exercises

### 1. Calculation

What is the selectivity if $A_{task}=0.84$ and $A_{control}=0.57$?

<details><summary>Show solution</summary>It is $0.84-0.57=0.27$. Report both original accuracies as well.</details>

### 2. Interpretation

Which probe has greater selectivity: one with task accuracy 0.95 and control accuracy 0.90, or one with task accuracy 0.75 and control accuracy 0.50?

<details><summary>Show solution</summary>The first probe has selectivity 0.05, and the second has selectivity 0.25. Their task performance and purposes also differ, however, so selectivity alone does not settle which is preferable.</details>

### 3. Group control

Can assigning the same word type a different random label on every occurrence measure type memorization?

<details><summary>Show solution</summary>This control does not measure memorization of a consistent type-label mapping. Fix one random label for each word type.</details>

### 4. Tuning budget

Thirty hyperparameters were tested for the task but only one for the control. What bias does this introduce?

<details><summary>Show solution</summary>The task has more selection opportunities, which can increase the performance difference. Use the same search space and selection protocol.</details>

### 5. Multiple layers

How should controls be handled when selecting the layer with the highest selectivity?

<details><summary>Show solution</summary>Apply the same layer-selection procedure in each control repetition, or fix the layer using validation and then compare on the test set.</details>

### 6. Scope of the claim

Selectivity was consistently positive. What claim is supported?

<details><summary>Show solution</summary>Under the specified probe class and control protocol, the actual label relationship was more recoverable than the control mapping. Functional use and causality have not yet been tested.</details>

## Sources and update boundaries

Control tasks and selectivity are explained using [Designing and Interpreting Probes with Control Tasks](https://arxiv.org/abs/1909.03368). Control types and probe-selection protocols depend on the research question and should be specified in the report.

## Lesson summary

- A control measures the probe's ability to learn a mapping unrelated to the representation.
- Match splits, capacity, tuning, and selection budgets between the task and control.
- Selectivity is the difference between two performance values; examine the original values and the distribution across seeds together.
- Even a probe that passes a control does not establish functional use by the model.

## Pass criteria

- Can you design label and representation controls that fit the question?
- Can you calculate selectivity using the same probe protocol?
- Can you write a conclusion with a strength supported by the control results?

## Next lesson

- [I06-08 CCA, CKA, and RSA](I06-08-cca-cka-rsa.md)

## Author checklist

- [x] The comparison contract for controls and selectivity is specified.
- [x] Every exercise has a solution.
- [x] The strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and mathematical rendering have been checked.
