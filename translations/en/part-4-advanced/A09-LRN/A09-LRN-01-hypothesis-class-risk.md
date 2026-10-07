---
id: "A09-LRN-01"
title: "Hypothesis classes and risk"
part: 4
stage: "A09-LRN"
status: "complete"
prerequisites: ["M04-06", "M04-08"]
estimated_time: "90–120 minutes"
---

# A09-LRN-01. Hypothesis classes and risk

## Why this lesson matters

A learning algorithm chooses a function that fits the data from a specified hypothesis class, not from every possible predictor. Distinguishing population risk from empirical risk lets us separate training fit, approximation error, and generalization.

## Learning objectives

- Distinguish a hypothesis class from a learning algorithm.
- Write population and empirical risk.
- Explain the objective and limitations of empirical risk minimization.
- Explain how the loss, data distribution, and class determine the estimand.

## Prerequisite check

- Prerequisite lessons: [M04-06 Samples and populations](../../part-1-foundations/M04/M04-06-samples-populations-sampling-distributions.md), [M04-08 Regression and classification](../../part-1-foundations/M04/M04-08-regression-classification.md)
- Check question: Why are average loss on a sample and expected loss on a new sample not the same random quantity?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\mathcal H$ | `the hypothesis class H` | Set of candidate predictors | set of functions |
| $R(h)$ | `the risk of h` | Population expected loss | scalar |
| $\hat R_n(h)$ | `the empirical risk of h on n samples` | Average loss on a sample | scalar |
| $\hat h$ | `h hat` | Hypothesis selected using the data | element of $\mathcal H$ |

## Core concepts

### Possible functions and the rule that selects one

A hypothesis class $\mathcal H$ is a set of functions mapping inputs to predictions. For example, the class of affine linear probes contains every $h(x)=w^\top x+b$ expressible using the permitted $w,b$. One particular training result is not the whole class. A learning algorithm is a rule that takes training data and selects a function from this set. If initialization or sampling is random, it can select different functions even from the same data.

Two algorithms with the same class need not produce the same predictor. The optimizer's starting point, stopping condition, tie-breaking rule, or regularization can change the selection. Distinguish the functions permitted by the class from the function selected by the actual procedure.

In the figure below, distinguish the candidate lines from the two marked selections.

<figure class="lesson-figure" markdown="1">

![Illustrative affine hypothesis class contains many straight-line predictors shown by gray candidates while two marked linear predictors one with slope one and another with slope one half intercept one are different possible algorithm selections from the same class](../../figures/assets/A09-LRN/A09-LRN-01-affine-candidates-selected.svg)

<figcaption>The gray lines show some members of an affine class. The illustrative selections h(x) = x for A and h(x) = 0.5x + 1 for B also belong to this class but are different selection results. The few gray lines do not represent the entire class, and neither selection is claimed to be an ERM solution.</figcaption>

</figure>

### The population average and the observed average

For data $Z=(X,Y)\sim P$ and loss $\ell$,

$$
R(h)=E_P[\ell(h(X),Y)],
\qquad
\hat R_n(h)=\frac1n\sum_{i=1}^n\ell(h(X_i),Y_i).
$$

$R(h)$ is the average loss when the predictor $h$ is fixed and a new $(X,Y)$ is drawn from the target distribution $P$. $\hat R_n(h)$ adds the losses on the $n$ observations actually obtained and divides by their count. Even for the same $h$, empirical risk changes when the sample changes. If the expected loss exists and the observations are drawn i.i.d. from $P$, then $E[\hat R_n(h)]=R(h)$ for an $h$ fixed in advance.

The learned $\hat h$ is a function selected using the training data. To evaluate $R(\hat h)$, hold the selected function fixed and average over new observations independent of the training data. $\hat R_n(\hat h)$ computed on those same training data incorporates the effect of function selection, so the equality above for a fixed $h$ cannot simply be applied to it.

Changing the loss or distribution changes the risk of the same predictor. For example, changing the relative weights of prompts changes how each prompt's loss contributes to the average. The class does not change the definition of risk for a fixed $h$, but it determines which functions can be compared or optimized. To interpret probe performance, specify not only what was predicted, but also the population, loss, and class within which it was evaluated.

The following separate figures show the effect of function selection and the effect of population weights.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Exact illustrative ten-sample binomial calculation at population label probability one half gives fixed constant-one empirical risk expected one half but choosing the better constant classifier on each sample yields expected training risk about zero point three seven seven while population risk remains one half](../../figures/assets/A09-LRN/A09-LRN-01-fixed-versus-selected-risk.svg)

<figcaption>For the illustrative setting p = 0.5 and n = 10, the exact probability of every label-count outcome is calculated. The mean empirical risk of fixed h₁ is 0.5, but selecting the better-fitting constant on each sample gives a mean training risk of about 0.377. Both constants have population risk 0.5, so population risk remains 0.5 after selection.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Illustrative fixed predictor with group A mean loss one tenth and group B mean loss nine tenths has population risk zero point nine minus zero point eight w as group A weight w varies so equal weights give risk one half and group A weight nine tenths gives risk zero point one eight](../../figures/assets/A09-LRN/A09-LRN-01-population-weighted-risk.svg)

<figcaption>This illustrative calculation fixes the predictor and group mean losses 0.1 and 0.9. Risk is 0.5 when A's population weight w is 0.5, and 0.18 when w = 0.9. The hypothesis class determines which functions can be compared; the weights in P directly change this fixed predictor's weighted risk.</figcaption>

</figure>

### ERM and three sources of error

Empirical risk minimization (ERM) chooses $\hat h\in\arg\min_{h\in\mathcal H}\hat R_n(h)$. This notation assumes that a function attaining the minimum exists. An actual optimizer may not reach it, and a procedure minimizing a regularized loss generally solves a different problem from ERM for the original loss.

To distinguish sources of error, separate their comparison targets. Approximation error is the difference between the predictor with the smallest population risk among all permitted predictors and the best predictor within $\mathcal H$. Missing the population optimum within the class because a function is selected from a finite sample is related to estimation error. Optimization error is the difference left when computation does not reach the minimum of the specified training objective. This explanation assumes that optima exist; when they do not, compare infima instead of minimum values. These distinctions alone do not yield an exact decomposition of an arbitrary training result into the sum of three nonnegative terms.

If the class is too restrictive, approximation error may remain even as more data are collected. Conversely, a rich class can lower empirical risk by following chance patterns in the training sample. ERM aims to minimize the training average. Whether its result also performs well on new samples is a separate generalization question.

The two objective axes below show the comparison targets used for each source of error.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Illustrative population-risk axis compares best unrestricted predictor zero point one best in class zero point two and selected predictor zero point three five separately from training-objective axis comparing attainable minimum zero point zero five with optimizer value zero point zero eight so the optimization difference is not added as a third population-risk term](../../figures/assets/A09-LRN/A09-LRN-01-error-comparison-targets.svg)

<figcaption>The illustrative population-risk axis above places the unrestricted optimum at 0.1, the within-class optimum at 0.2, and the selected result at 0.35. The optimization comparison below uses a separate training objective with minimum 0.05 and actual value 0.08. Differences on these two axes are not arbitrarily combined into a sum of three nonnegative terms.</figcaption>

</figure>

## Small example

In the constant classifier class $\mathcal H=\{h_0,h_1\}$, if 7 of 10 labels are 1, empirical 0–1 risk is $\hat R(h_1)=0.3$ and $\hat R(h_0)=0.7$.

$h_1$ always predicts 1, so it is wrong only on the three observations labeled 0. ERM selects $h_1$ on this sample. But if the population probability of label 1 is $p$, then $R(h_1)=1-p$ and $R(h_0)=p$. Distinguish the observed proportion $7/10$ from the unknown population probability $p$: training risk $0.3$ cannot immediately be called population risk.

Read the sample loss calculation separately from the risk curves as a function of population p.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Ten observed labels with seven ones and three zeros produce three unit losses for the constant-one classifier and seven unit losses for the constant-zero classifier giving empirical risks zero point three and zero point seven](../../figures/assets/A09-LRN/A09-LRN-01-constant-classifier-losses.svg)

<figcaption>For illustration, the existing example's 10 labels are ordered as seven ones followed by three zeros. In a loss row, 1 means an incorrect prediction and 0 a correct prediction. Dividing the loss sums 3 for h₁ and 7 for h₀ by 10 shows ERM's selection on this sample.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Against population probability p of label one constant-zero risk p increases and constant-one risk one minus p decreases crossing at p one half while the observed training fraction seven tenths does not determine the unknown population p](../../figures/assets/A09-LRN/A09-LRN-01-population-label-probability.svg)

<figcaption>The horizontal axis is the unknown population p, not the sample proportion 7/10. The population risks of h₀ and h₁ are p and 1 − p, so their ordering changes at p = 1/2. The training risk 0.3 of the selected h₁ does not determine which p applies on these curves.</figcaption>

</figure>

## Common misconceptions

- The size of a hypothesis class alone does not determine the effective class explored by the actual optimizer.
- Repeatedly selecting hypotheses using the test set also makes test risk optimistically biased.

## Exercises

### 1. Empirical risk
Find the empirical risk if the losses are $(0,1,0,1)$.
<details><summary>Show solution</summary>

The average is $2/4=0.5$.
</details>

### 2. Class
What is restricted when a linear probe's hypothesis class is limited to $h(x)=w^\top x+b$?
<details><summary>Show solution</summary>

The form of the decision function recovering labels from activations is restricted to an affine linear map.
</details>

### 3. Approximation
If the Bayes predictor is not in $\mathcal H$, what can remain even with infinitely many empirical observations?
<details><summary>Show solution</summary>

Approximation error between the within-class optimum and Bayes risk can remain.
</details>

### 4. Model interpretation
How should the distribution be specified to interpret probe test accuracy as a population claim?
<details><summary>Show solution</summary>

Specify the target population, including sampling of prompts, labels, tokens, and layers, and the train/test sampling protocol.
</details>

## Sources and update boundaries

Hypothesis classes, risk, and ERM follow standard definitions in statistical learning theory. Detailed analysis of optimization error is outside this lesson's scope.

## Lesson summary

- A hypothesis class is a set of possible predictors.
- Population risk and empirical risk are different quantities.
- ERM minimizes sample loss but does not automatically guarantee generalization.
- The loss and target distribution determine the target of a learning claim.

## Pass criteria

- Can you calculate population and empirical risk?
- Can you distinguish approximation, estimation, and optimization problems?

## Next lesson

- [A09-LRN-02 Bias–variance decomposition](A09-LRN-02-bias-variance-decomposition.md)

## Author checklist

- [x] Hypothesis classes, algorithms, and risk are distinguished.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
