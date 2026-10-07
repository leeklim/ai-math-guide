---
id: "A09-LRN-06"
title: "PAC learning"
part: 4
stage: "A09-LRN"
status: "complete"
prerequisites: ["A09-LRN-04", "M04-10"]
estimated_time: "90–120 minutes"
---

# A09-LRN-06. PAC learning

## Why this lesson matters

To discuss learnability, specify how small an error is achieved, with what probability, and how the required sample size grows. The PAC framework expresses sample complexity by separating accuracy $\varepsilon$ from confidence $1-\delta$.

## Learning objectives

- Read the probability statement of a PAC guarantee.
- Distinguish realizable and agnostic settings.
- Explain the roles of $\varepsilon,\delta$ in sample complexity.
- Distinguish a theorem's guarantee from one empirical result.

## Prerequisite check

- Prerequisite lessons: [A09-LRN-04 VC dimension](A09-LRN-04-vc-dimension.md), [M04-10 Hypothesis testing and multiple comparisons](../../part-1-foundations/M04/M04-10-hypothesis-testing-multiple-comparisons.md)
- Check question: Is probability $1-\delta$ a prediction probability for one test example, or a probability over repeated training samples?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $\varepsilon$ | `epsilon` | Permitted excess risk | positive scalar |
| $\delta$ | `delta` | failure probability | $(0,1)$ |
| $m_{\mathcal H}(\varepsilon,\delta)$ | `the sample complexity of H at epsilon and delta` | Required sample size | positive integer |
| $R(\hat h)\le\inf_{h\in\mathcal H}R(h)+\varepsilon$ | `the risk of h hat is at most the best risk in H plus epsilon` | agnostic target | inequality |

## Core concepts

### The two levels of the probability statement

A typical agnostic PAC guarantee for a training sample $S\sim P^n$ has the form

$$
P_S\left(
R(\hat h_S)\le \inf_{h\in\mathcal H}R(h)+\varepsilon
\right)\ge1-\delta
$$

Here, $P^n$ means sampling from the same distribution $P$, with $n$ observations drawn independently. Inside the parentheses, $R(\hat h_S)$ is the loss averaged over fresh observations while holding that training outcome fixed. Outside the parentheses, $P_S$ is the probability that the risk inequality holds when the training sample is drawn again and the learner is retrained. Distinguish the fresh-example average within the risk from the outer repetition of training. For a randomized learner's guarantee, seed randomness is also included in the outer probability.

The risk difference $\varepsilon$ specifies how much worse than the best in class is permitted. The value $\delta$ bounds the probability of training repetitions in which this inequality fails. Under 0–1 loss, $\varepsilon$ is a difference in error rates, and $1-\delta$ is not the confidence of an individual prediction produced by the model. If best-in-class risk is high, an outcome within $\varepsilon$ of it may also have high risk. Distinguish an excess-risk guarantee from an absolute performance guarantee.

Read the averaging within the risk separately from the calculation of the outer probability.

<figure class="lesson-figure" markdown="1">

![A nested diagram separates retraining over samples from averaging fresh-example losses for one fixed trained predictor.](../../figures/assets/A09-LRN/A09-LRN-06-nested-risk-training-probability.svg)

<figcaption>The outer probability concerns repeatedly drawing training samples. The risk for each repetition averages fresh-example loss with the learned function fixed. Neither is the model's confidence in an individual prediction or a finite test error rate.</figcaption>

</figure>

### Benchmarks in realizable and agnostic settings

For binary 0–1 loss, the realizable setting assumes that the class contains a target with population risk 0. Best-in-class risk is then 0, so the goal reduces to $R(\hat h_S)\le\varepsilon$. Observing training error 0 does not establish realizability: a class may memorize the observed sample's labels yet make errors on new inputs.

The agnostic setting does not assume a zero-risk target. It controls excess risk relative to $\inf_{h\in\mathcal H}R(h)$. Even the best function in the class may have positive risk because of label noise or representational constraints. Labels that vary randomly for the same input provide one example of this distinction. Realizability is an assumption about the population, not a statement about how far the optimizer reduced training loss.

The benchmark for permitted risk and the assumption of zero population risk are different conditions.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Two risk axes compare a zero-risk class benchmark with best-in-class risk zero point one two and the same tolerance zero point zero three.](../../figures/assets/A09-LRN/A09-LRN-06-risk-target-realizable-agnostic.svg)

<figcaption>With the same ε=0.03, best-in-class risk 0 gives a target risk of 0.03, whereas the agnostic example in the text gives 0.12+0.03=0.15. Equal excess-risk allowances do not imply equal absolute risks.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![A fixed input has stochastic labels with probabilities zero point seven and zero point three, so each deterministic output leaves positive error mass.](../../figures/assets/A09-LRN/A09-LRN-06-same-input-label-noise.svg)

<figcaption>In this illustrative population, the same input has label 0 with probability 0.7 and label 1 with probability 0.3. Always outputting 0 or always outputting 1 leaves error mass 0.3 or 0.7, respectively. Realizability of this population is separate from how well the training sample is fitted.</figcaption>

</figure>

### What the required sample size means

PAC learnability is stronger than success at one $P$ and one $n$. For the specified class and loss, a sample-size criterion must be available for every permitted $\varepsilon,\delta$, and the learner must satisfy the probability guarantee above for every target distribution once that criterion is met. The realizable definition considers distributions with a zero-risk target in the class. Distribution-free sample complexity does not separately choose a favorable sample size for each unknown $P$.

Also distinguish the exact minimum required sample size from a theorem's upper bound on a sufficient sample size. For example, fix $N$ binary classifiers in advance and use 0–1 loss on i.i.d. data. In the realizable case, $n\ge(\log N+\log(1/\delta))/\varepsilon$ suffices for consistent ERM. This follows because a fixed function with risk greater than $\varepsilon$ fits all $n$ observations with probability at most $(1-\varepsilon)^n$, and the probability that any of the $N$ candidates does so is at most $Ne^{-n\varepsilon}$. Here, log is the natural logarithm.

For an agnostic finite class, controlling uniform risk error to at most $\varepsilon/2$ controls ERM's excess risk to at most $\varepsilon$. Hoeffding's inequality and a union bound over candidates give the sufficient condition $n\ge 2\log(2N/\delta)/\varepsilon^2$. The factor 2 arises from selecting an empirical minimizer and adding the risk-estimation errors on both sides. For both formulas, round sample size upward to an integer; these are not tight necessary conditions. Reducing $\varepsilon$ requires greater risk precision, and reducing $\delta$ requires a lower failure probability, so each increases the sufficient sample size.

To see this factor 2, compare ERM with any $h\in\mathcal H$. On the uniform event, $R(\hat h)\le\hat R_n(\hat h)+\varepsilon/2$. By ERM, $\hat R_n(\hat h)\le\hat R_n(h)$. Applying the uniform event again gives $\hat R_n(h)\le R(h)+\varepsilon/2$. Chaining these three inequalities yields $R(\hat h)\le R(h)+\varepsilon$. Since this holds for every $h$, we can compare with the best-in-class infimum.

Follow how the failure bound for training consistency gives a sufficient sample criterion, and how the two estimation errors are linked through ERM.

<figure class="lesson-figure" markdown="1">

![Consistency probability for one bad predictor and the finite-class union upper bound decay with sample count and cross a failure target.](../../figures/assets/A09-LRN/A09-LRN-06-bad-hypothesis-consistency-bound.svg)

<figcaption>The training-consistency probability for an illustrative fixed function with risk 0.12 is 0.88ⁿ. For ε=0.10 and N=10, the upper bound across candidates is min(1,10e⁻⁰·¹ⁿ), not necessarily the actual failure probability. A sufficient integer n for δ=0.05 is 53. The union bound does not require independence between candidate events.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Finite-class sufficient sample ceilings grow as inverse epsilon in the realizable setting and inverse epsilon squared in the agnostic setting.](../../figures/assets/A09-LRN/A09-LRN-06-sample-bound-epsilon.svg)

<figcaption>With N=10 and δ=0.05 fixed, the two sufficient conditions in the text are rounded upward to integers. At ε=0.10, 53 samples suffice in the realizable setting and 1,199 in the agnostic setting. These are not exact minimum sample requirements or actual training times.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Sufficient sample counts in separate realizable and agnostic panels rise as the target failure probability decreases.](../../figures/assets/A09-LRN/A09-LRN-06-sample-bound-delta.svg)

<figcaption>Here N=10 and ε=0.10 are fixed. A smaller δ requires a higher probability of success across repetitions, so both sufficient-sample upper bounds grow. Read the settings in separate panels with different vertical scales, and do not confuse ε's precision with δ's probability.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Three inequality steps connect true risk of the empirical minimizer to true risk of any comparator using two half-epsilon deviations.](../../figures/assets/A09-LRN/A09-LRN-06-erm-two-deviation-steps.svg)

<figcaption>The first and last steps each use uniform error ε/2; the middle step uses ERM's empirical-minimum property. The comparator h is arbitrary in the class, so the final comparison can use the best-in-class infimum. Read this chain on the same uniform event.</figcaption>

</figure>

### A theorem versus one experiment

For infinite classes, finite VC dimension or an appropriate Rademacher complexity bound can also control sample complexity. Each theorem's conditions on loss, norms, sampling, and the class must hold. Do not substitute parameter count for $N$ in the finite-class formulas above. PAC learnability does not mean that a bound is tight at practical sample sizes or that optimization is efficient.

Test accuracy on one split estimates performance for that training outcome. It cannot by itself prove the quantifiers over all distributions, sufficiently large sample sizes, and repeated training. Nor does a theorem's original guarantee automatically extend to shifts that violate its same-distribution condition for training and testing.

Distinguish the scope of one evaluation from the scope a theorem requires.

<figure class="lesson-figure" markdown="1">

![A scope diagram places one evaluated trained predictor inside one population and contrasts it with a guarantee over the declared distribution family.](../../figures/assets/A09-LRN/A09-LRN-06-one-run-guarantee-scope.svg)

<figcaption>Independent test evaluation of one training outcome estimates performance for that predictor and population. A PAC claim additionally needs a target family of distributions, a sufficient sample criterion, and a probability over training repetitions. Do not extend it to unspecified shifts or guarantees for all domains.</figcaption>

</figure>

## Small example

The value $\delta=0.05$ means that, across repeated training samples from the same data-generating process, the probability of guarantee failure is limited to at most 5%.

This does not mean the model has accuracy 95%. For example, if best-in-class risk is 0.12 and $\varepsilon=0.03$, then under a sufficient sample size and the theorem's conditions, at least 95% of training repetitions produce a predictor with risk at most 0.15. This does not mean that the remaining repetitions have risk exactly 0.15, or that the observed error rate on a test sample must be at most 0.15.

Read the 95% in the text as the probability of an event over training outcomes, not the risk of an individual predictor.

<figure class="lesson-figure" markdown="1">

![An explicitly illustrative law of twenty equiprobable training outcomes has nineteen risks below the zero point one five target and one above it.](../../figures/assets/A09-LRN/A09-LRN-06-ninety-five-percent-training-law.svg)

<figcaption>This is an illustrative probability law with 20 equally probable training outcomes, not 20 actual experiments. If 19 outcomes have risk at most 0.15, the event has probability 95%. Individual predictors have risks around 0.12; the figure does not mean accuracy 95%. Nor does this arbitrary law alone prove an actual theorem's guarantee.</figcaption>

</figure>

## Common misconceptions

- Do not read $1-\delta$ as confidence in an individual prediction.
- A PAC guarantee does not automatically persist after distribution shift.

## Exercises

### 1. Confidence
If $\delta=0.01$, what is the guarantee probability?
<details><summary>Show solution</summary>

It is $1-0.01=0.99$.
</details>

### 2. Excess risk
If best-in-class risk is 0.12 and $\varepsilon=0.03$, what is the permitted upper bound?
<details><summary>Show solution</summary>

It is $0.15$.
</details>

### 3. Realizability
Why can label noise cause the realizable assumption to fail when only a deterministic classifier class is used?
<details><summary>Show solution</summary>

If different labels occur for the same input, no deterministic function in the class may be able to attain population error 0.
</details>

### 4. Model interpretation
Why does the test accuracy of one probe not prove PAC learnability?
<details><summary>Show solution</summary>

PAC is a uniform probability guarantee depending on sample size. A point estimate from one split is not a guarantee for the entire class and algorithm.
</details>

## Evidence and update boundaries

PAC, realizable, and agnostic learning follow the standard definitions of computational learning theory. Computational efficiency and online learning are outside this lesson's scope.

- [Cornell CS4783 Lecture 1, §2.1](https://www.cs.cornell.edu/courses/cs4783/2022sp/notes01.pdf): Used to check the failure bound for a finite realizable class and the interpretation of probability over training samples.

## Lesson summary

- PAC separates accuracy from confidence.
- The probability concerns repeated training samples.
- The agnostic setting controls best-in-class excess risk.
- Distinguish theoretical sample bounds from one empirical accuracy result.

## Pass criteria

- Can you express a PAC probability statement in words?
- Can you distinguish realizable and agnostic settings from distribution shift?

## Next lesson

- [A09-LRN-07 Probes and generalization in interpretation](A09-LRN-07-probe-interpretation-generalization.md)

## Author checklist

- [x] The two probability levels in PAC are not confused.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
