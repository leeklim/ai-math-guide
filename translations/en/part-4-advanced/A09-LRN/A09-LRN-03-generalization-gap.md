---
id: "A09-LRN-03"
title: "Generalization gap"
part: 4
stage: "A09-LRN"
status: "complete"
prerequisites: ["A09-LRN-01", "M04-09"]
estimated_time: "90–120 minutes"
---

# A09-LRN-03. Generalization gap

## Why this lesson matters

The difference between training performance and performance on unseen data reveals a learned predictor's sample dependence. The generalization gap is one measurement; a small gap alone guarantees neither low population risk nor robustness to distribution shift.

## Learning objectives

- Distinguish expected and observed generalization gaps.
- Explain the difference between a fixed hypothesis and a data-dependent hypothesis.
- Explain why reusing validation data biases gap estimation.
- Design a confidence interval and a paired comparison.

## Prerequisite check

- Prerequisite lessons: [A09-LRN-01 Hypothesis classes and risk](A09-LRN-01-hypothesis-class-risk.md), [M04-09 Confidence intervals](../../part-1-foundations/M04/M04-09-confidence-intervals-bootstrap.md)
- Check question: Why does it matter that the learned $\hat h$ is a function of the training sample?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $R(\hat h)-\hat R_n(\hat h)$ | `the generalization gap of h hat` | Population risk minus training risk | scalar |
| $\hat R_{\mathrm{test}}(\hat h)$ | `the test risk of h hat` | Held-out risk estimate | scalar |
| $E_S$ | `expectation over samples S` | Expectation over repeated datasets | operator |
| $\Delta_i$ | `delta sub i` | Paired loss difference | scalar |

## Core concepts

### One gap and its mean across repetitions

The generalization gap of $\hat h_S$ learned from sample $S$ is

$$
R(\hat h_S)-\hat R_S(\hat h_S)
$$

The subscript $S$ in $\hat R_S$ identifies the training sample over which losses are averaged, whereas the subscript in $\hat h_S$ identifies the sample used to select the predictor. Resampling $S$ and retraining changes both the predictor and its training average. The expected generalization gap is $E_S$ of this entire difference, not the difference obtained from one training result. To repeat seeds as well, include that randomness in the expectation.

Population risk $R$ is unknown. Replacing it with the average over an independent test sample not used for selection gives the observed gap. With the training result fixed, this test average estimates risk under the same target distribution. A finite test set leaves test-sampling error between the observed gap and the population-minus-training gap. An interval obtained by bootstrapping only test prompts concerns uncertainty conditional on this training result; it does not include variation from resampling training data and retraining.

In the figure below, distinguish each training result's population target from its finite-test observation.

<figure class="lesson-figure" markdown="1">

![Four equally probable illustrative training outcomes have population-minus-training gaps one tenth five hundredths five hundredths five hundredths averaging zero point zero six two five but separate finite-test observed gaps one tenth four zero seven hundredths four hundredths differ from those population targets](../../figures/assets/A09-LRN/A09-LRN-03-retraining-versus-observed-gaps.svg)

<figcaption>The four training outcomes are assigned equal probabilities in an illustrative law. Population-minus-training gaps 0.10, 0.05, 0.05, and 0.05 average to 0.0625. The open circles show observed gaps 0.14, 0, 0.07, and 0.04, which include the errors of their finite test sets. This is not an actual retraining experiment, nor does it identify an empirical test average with a theoretical expectation.</figcaption>

</figure>

### Why the law for a fixed function cannot simply be transferred

If the expected loss exists and $S$ is an i.i.d. sample, then $E_S[\hat R_S(h)]=R(h)$ for an $h$ fixed before the sample is seen. That function's expected gap is therefore zero. In contrast, $\hat h_S$ is selected after seeing the sample, so the function inside the averaging operation changes with $S$. The sample-mean law for a function fixed in advance alone does not imply that this selection result's expected gap is zero.

The gap does not specify the level of risk itself. If training and test errors under the same loss are both 0.45, the difference is small, but whether prediction is good is a separate question. The gap is not defined to be always positive either. Test-sampling error can make the observed gap negative, and differences in the compared training and test losses or augmentation conditions also contribute to the difference. To interpret it as a learning-theory gap, compare under the same loss and target distribution.

Use the risk coordinates and diagonal below to read gap size separately from error level.

<figure class="lesson-figure" markdown="1">

![Train-error versus observed-test-error plane has zero-gap diagonal and marks original pair zero point one zero point one six above it high-error pair zero point four five zero point four five on it and illustrative negative observed gap pair zero point two five zero point two below it](../../figures/assets/A09-LRN/A09-LRN-03-risk-level-versus-gap.svg)

<figcaption>The existing example 0.10, 0.16 lies 0.06 above the diagonal. The pair 0.45, 0.45 has gap 0 despite both errors being high. The illustrative pair 0.25, 0.20 has observed gap −0.05. The test averages in this figure are not asserted to equal population risk.</figcaption>

</figure>

### The learning procedure includes validation-based selection

When hyperparameters, layers, or probe types are repeatedly selected using validation results, the entire selection process becomes the learner. Each candidate's validation error has sampling error, and choosing the best observed value can select a candidate that happened to receive a favorable error. Reporting that validation average again as the selected model's performance on the population ignores the selection effect. Evaluate the final selection on a test set not used for selection, and record which candidates were considered and the rule used to choose among them.

An independent test within the same template and a test on a new template have different targets. The former evaluates risk under the same sampling distribution; the latter evaluates risk under a new target distribution. Subtracting training risk from the latter mixes learning-sample dependence with a distribution difference, so do not interpret it as the same quantity as an i.i.d. gap.

The figures below separate validation-based candidate selection from a change in the evaluation population.

<figure class="lesson-figure" markdown="1">

![Four illustrative candidate population risks all one fifth have observed validation errors twenty three eighteen eleven twenty five hundredths so minimum selection chooses candidate C with validation eleven hundredths although its population risk remains one fifth](../../figures/assets/A09-LRN/A09-LRN-03-validation-minimum-selection.svg)

<figcaption>The four illustrative candidates all have population risk 0.20, but their observed validation errors differ: 0.23, 0.18, 0.11, and 0.25. Selecting C also selects the most favorably lowered observation, 0.11. This example illustrates one possible selection path; it measures neither a universal magnitude of bias nor a test result.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Illustrative fixed predictor has group-specific errors one tenth nine tenths while source and same-population evaluation have group A probability nine tenths but shifted evaluation has probability one fifth giving population risks eighteen hundredths and seventy four hundredths without a change in predictor](../../figures/assets/A09-LRN/A09-LRN-03-same-and-shifted-populations.svg)

<figcaption>Fix illustrative group errors 0.1 and 0.9 for the same h. In source P and the same evaluation population, A's weight is 0.9 and risk is 0.18. If A's weight in Q is 0.2, risk becomes 0.74. This compares population targets; it is not an i.i.d. gap involving observed training risk.</figcaption>

</figure>

### Paired comparison on the same test examples

When comparing probes A and B on the same test examples, set $\Delta_i=\ell_A(i)-\ell_B(i)$. The mean of these differences estimates the difference between their population risks. To retain shared variation from how easy or difficult an example is, use examples or independent prompt clusters as the units of a paired bootstrap rather than resampling A's and B's losses separately. Pairing can reduce comparison uncertainty when shared variation is large, but greater precision is not guaranteed.

To find the difference between two generalization gaps, also subtract the difference between their training risks from the mean test-loss difference. In an interval that holds the two trained probes and training risks fixed, this training difference is a constant. Comparing the learning procedures themselves requires a separate design that also repeats training data and seeds. Resampling tokens from the same prompt as if they were independent samples cannot replace those repetitions.

The linked observations and training-difference adjustment below show the target of the paired comparison.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Illustrative losses of probe A one tenth four tenths nine tenths and B two tenths five tenths one on the same three examples differ by minus one tenth for every paired example while independently mixing A and B draws gives varied differences](../../figures/assets/A09-LRN/A09-LRN-03-paired-example-differences.svg)

<figcaption>On three illustrative examples, A's losses are 0.1, 0.4, and 0.9, and B's are 0.2, 0.5, and 1. Same-example differences are all −0.1, but separately drawing from A and B mixes different example difficulties. Shared variation in this construction illustrates pairing's usefulness; it does not guarantee a variance reduction in every experiment.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Illustrative probe A train error one tenth test sixteen hundredths gap six hundredths and B train twelve hundredths test fifteen hundredths gap three hundredths give test difference one hundredth minus train difference negative two hundredths equals gap difference three hundredths](../../figures/assets/A09-LRN/A09-LRN-03-gap-difference-training-adjustment.svg)

<figcaption>A uses the existing training and test errors 0.10 and 0.16; illustrative B uses 0.12 and 0.15. Subtracting training difference −0.02 from test difference 0.01 gives gap difference 0.03. In a paired test interval holding A, B, and their training risks fixed, this training difference is constant.</figcaption>

</figure>

## Small example

If training error is 0.10 and independent test error is 0.16, the observed gap is 0.06. Report test-set uncertainty as well.

If both errors use the same 0–1 loss, $0.16-0.10$ is an error-rate difference of 6 percentage points. Without the test sample size and independent sampling unit, however, its precision is unknown. With the training result fixed and independent test examples, the standard error of the test error rate is approximately $\sqrt{\hat p(1-\hat p)/m}$, where $\hat p=0.16$ and $m$ is the number of test examples. If observations within prompts are dependent, do not simply substitute the total row count for $m$ in this expression.

Read the test-size comparison below as conditional sampling with the training result fixed.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Exact binomial illustrative independent test-error sampling at fixed trained predictor population error sixteen hundredths and fixed training error one tenth compares test sizes twenty five and four hundred with observed-gap distributions centered at six hundredths and smaller spread for the larger test](../../figures/assets/A09-LRN/A09-LRN-03-conditional-test-sampling.svg)

<figcaption>For illustration, fix the trained h, training error 0.10, and population test error 0.16. The exact binomial laws for i.i.d. test sizes 25 and 400 have different spreads around the same gap 0.06. This is test sampling for a fixed h; it does not include variation from retraining with different data or seeds.</figcaption>

</figure>

## Common misconceptions

- When training and test errors are both high, a small gap does not make the model good.
- A small i.i.d. gap does not guarantee generalization to another domain.

## Exercises

### 1. Gap
Find the observed gap for training loss 0.25 and test loss 0.31.
<details><summary>Show solution</summary>

It is $0.31-0.25=0.06$.
</details>

### 2. Negative gap
Can the observed gap be negative?
<details><summary>Show solution</summary>

Yes. Finite-sample variation, differences involving a regularized training objective, or augmentation can make the test estimate smaller than training loss.
</details>

### 3. Validation reuse
If the layer with the highest validation accuracy was selected from 100 layers, what should be recorded?
<details><summary>Show solution</summary>

Record the entire layer search as the selection procedure, and evaluate the selected layer once on an independent test set.
</details>

### 4. Shift
If held-out prompt templates are the same as training templates, which generalization is tested?
<details><summary>Show solution</summary>

This mainly tests i.i.d. generalization within that template population. Generalization to new templates or domains requires a separate split.
</details>

## Sources and update boundaries

Generalization gaps and held-out evaluation follow standard definitions in learning theory and experimental design. Quantitative bounds from adaptive data analysis are outside this lesson's scope.

- [Cornell CS4783 Lecture 2, §2](https://www.cs.cornell.edu/courses/cs4783/2022sp/notes02.pdf): The distinction between concentration for a fixed hypothesis and sample-dependent selection was checked against this source.

## Lesson summary

- The gap is the difference between population risk and training risk.
- Test risk is also a finite-sample estimate.
- A validation set used for model selection is not a final test set.
- Distinguish i.i.d. generalization from distribution shift.

## Pass criteria

- Can you calculate an observed gap and its uncertainty?
- Can you incorporate the selection procedure into the evaluation-split design?

## Next lesson

- [A09-LRN-04 VC dimension](A09-LRN-04-vc-dimension.md)

## Author checklist

- [x] The gap, test uncertainty, and selection bias are connected.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
