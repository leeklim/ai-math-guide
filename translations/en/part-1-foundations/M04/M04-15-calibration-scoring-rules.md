---
id: "M04-15"
title: "Calibration and scoring rules"
part: 1
stage: "M04"
status: "complete"
prerequisites:
  - "M04-03"
  - "M04-04"
  - "M04-06"
  - "M04-07"
  - "M04-08"
  - "M04-12"
estimated_time: "150~180 minutes"
---

# M04-15. Calibration and scoring rules

## Why this lesson matters

How often a classifier predicts the correct label is distinct from how reliable its output probabilities are. Among predictions with confidence $0.8$, about $80\%$ should be correct for that confidence to agree with empirical frequency. This property is called calibration.

Calibration alone does not determine the overall quality of probability predictions. A model reporting only the base rate can be calibrated over the population while failing to distinguish samples. Reliability diagrams and expected calibration error (ECE) summarize calibration gaps, whereas proper scoring rules such as log and Brier scores evaluate the quality of the entire predicted distribution.

## Learning objectives

After completing this lesson, you should be able to:

- Define binary calibration using conditional expectation.
- Distinguish accuracy from calibration.
- Calculate accuracy and confidence within a confidence bin.
- Interpret reliability diagrams and ECE.
- Explain the condition defining a proper scoring rule.
- Calculate log scores and Brier scores.
- Explain the relationships between sharpness, temperature scaling, and distribution shift.
- Limit model interpretation claims to what calibration results support.

## Prerequisite check

- Prerequisite: [M04-03 Random variables and probability distributions](M04-03-random-variables-distributions.md)
- Prerequisite: [M04-04 Expectation, variance, and covariance](M04-04-expectation-variance-covariance.md)
- Prerequisite: [M04-06 Samples, populations, and sampling distributions](M04-06-samples-populations-sampling-distributions.md)
- Prerequisite: [M04-07 Estimation, bias, and variance](M04-07-estimation-bias-variance.md)
- Prerequisite: [M04-08 Regression and classification](M04-08-regression-classification.md)
- Prerequisite: [M04-12 Entropy and cross entropy](M04-12-entropy-cross-entropy.md)
- Check: Can you distinguish a probability from an observed binary outcome?
- Check: Can you explain why a sample average is an estimate of a population quantity?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions and scope |
|---|---|---|---|
| $\widehat P$ | `P hat` | The model's output probability of the positive class | $0\le\widehat P\le1$ |
| $\widehat y_i$ | `y hat sub i` | The predicted class for sample $i$ | Can be multiclass |
| $\widehat c_i$ | `c hat sub i` | Confidence in the predicted class | $\max_k q_i(k)$ |
| $B_m$ | `B sub m` | A set of sample indices with confidence in a specified interval | Depends on binning |
| reliability diagram | `reliability diagram` | A comparison of confidence and accuracy within bins | A finite-sample estimate |
| ECE | `E C E` | A weighted average of binwise calibration gaps | Depends on binning |
| scoring rule | `scoring rule` | A rule assigning a loss to a probability prediction and outcome | Lower is better here |
| Brier score | `Brier score` | A probability score based on squared error | Binary or multiclass |
| sharpness | `sharpness` | How concentrated predicted distributions are | Separate from calibration |

## Core concept 1. Calibration asks whether probabilities agree with frequencies

Consider binary outcome $Y\in\{0,1\}$ and predicted probability $\widehat P$. The formal statement of perfect calibration is

\[
\mathbb E[Y\mid \widehat P]=\widehat P
\quad\text{almost surely}
\]

Intuitively, cases predicted at $\widehat P=p$ have actual positive frequency $p$:

\[
\mathbb P(Y=1\mid \widehat P=p)=p.
\]

For continuous $\widehat P$, observing exactly $p$ can have probability 0. Finite datasets therefore group nearby confidences into bins to estimate calibration.

Because $Y$ is an indicator of a positive outcome, its conditional expectation equals the positive-class probability under that condition. A model reporting $0.8$ does not mean the observed $Y$ is $0.8$. Each observation remains 0 or 1, and the comparison uses the mean of cases receiving the same probability. Almost surely means that the condition holds except on a set with probability 0 under the model output distribution. A conditional distribution for continuous outputs is also not defined by simply dividing event probabilities by $P(\widehat P=p)$.

Do not treat reported probability and individual observations as the same number.

<figure class="lesson-figure" markdown="1">
  ![Ten binary outcomes share reported probability point eight and average eight observed positives rather than fractional outcomes](../../figures/assets/M04/M04-15-probability-binary-outcomes.svg)
  <figcaption>The figure shows possible outcomes for ten cases all receiving P̂=0.8. Each Y is 0 or 1; only the group average is 8/10=0.8. This agreement in one sample neither establishes perfect population calibration nor requires exactly eight positives in every group of ten cases.</figcaption>
</figure>

## Core concept 2. Accuracy and calibration ask different questions

Accuracy asks how often predicted labels are correct. Calibration asks whether predicted probabilities agree with observed frequencies among cases receiving the same probability.

Two models giving identical predicted labels on the same evaluation sample have identical accuracy. But if one assigns confidence $0.7$ to each predicted class and the other $0.99$, those confidences have different meanings. If the second model is not correct $99\%$ of the time, it is overconfident.

Conversely, when population positive rate is $0.7$, a model outputting $0.7$ for every sample can be calibrated over that population. It cannot distinguish risk between samples. Calibration does not replace discrimination or usefulness.

Compare different reported confidences while keeping the predicted labels the same.

<figure class="lesson-figure" markdown="1">
  ![Two models with identical labels and seven out of ten correct predictions report confidence point seven and point nine nine](../../figures/assets/M04/M04-15-same-accuracy-confidence.svg)
  <figcaption>Both models give the same labels to the same ten samples, with seven correct. Accuracy is 0.7 for both, but reporting top confidence as 0.7 or 0.99 gives different gaps from the observed frequency. A finite sample alone cannot determine population calibration.</figcaption>
</figure>

## Core concept 3. A reliability diagram shows binwise gaps

For multiclass prediction $q_i(k)$, define predicted label and confidence by

\[
\widehat y_i=\arg\max_k q_i(k),
\qquad
\widehat c_i=\max_k q_i(k)
\]

Form index sets $B_1,\ldots,B_M$ by confidence intervals and calculate in each bin

\[
\operatorname{conf}(B_m)
=\frac{1}{|B_m|}
\sum_{i\in B_m}\widehat c_i
\]

and

\[
\operatorname{acc}(B_m)
=\frac{1}{|B_m|}
\sum_{i\in B_m}
\mathbf 1\{y_i=\widehat y_i\}
\]

A reliability diagram compares $\operatorname{conf}(B_m)$ and $\operatorname{acc}(B_m)$ for each bin.

If $\operatorname{conf}(B_m)>\operatorname{acc}(B_m)$, the bin suggests overconfidence; the opposite suggests underconfidence. Bins with few samples have greater sampling uncertainty in both quantities.

Choose one class in a tie using a prespecified rule. Assign each observation to exactly one bin, and do not calculate either mean for an empty bin. With mean confidence on the horizontal axis and accuracy on the vertical axis, bins with matching values lie on the diagonal. Points below the diagonal have confidence higher than actual correctness frequency. This top-label diagram measures whether the predicted class is correct, which conditions on a different object than the positive-class frequency in Core concept 1.

Each point pairs two averages from the same bin: confidence and correctness.

<figure class="lesson-figure" markdown="1">
  ![Two reliability points lie below and above the equal accuracy confidence diagonal with opposite calibration gaps](../../figures/assets/M04/M04-15-reliability-gaps.svg)
  <figcaption>The two equal-sized bins from Example 1 are shown. Filled points give (mean confidence,accuracy), and open points mark the diagonal locations where accuracy would equal that confidence. The first bin lies below the diagonal and the second above; both gaps have magnitude 0.1. These axes use top-label correctness, not positive-class frequency.</figcaption>
</figure>

## Core concept 4. ECE summarizes binwise calibration gaps in one number

For $n$ samples, a widely used ECE is

\[
\operatorname{ECE}
=\sum_{m=1}^{M}
\frac{|B_m|}{n}
\left|
\operatorname{acc}(B_m)
-\operatorname{conf}(B_m)
\right|
\]

Larger bins give their gaps more weight.

ECE depends on bin boundaries and the number of bins. Overconfidence and underconfidence within a bin can cancel in its average. Small top-label ECE can coexist with poor classwise or subgroup calibration. ECE alone does not prove calibration of the full predicted distribution.

If bins partition the sample without overlap, weights $|B_m|/n$ sum to 1. ECE can therefore be read as assigning each observation its bin's gap and averaging over the entire sample. Weighting differently sized bins equally produces a different summary. Merging Example 1's two bins makes mean confidence and accuracy both $0.8$, giving ECE 0. The original binwise gap $0.10$ disappears because opposite gaps cancel when averaging before taking the absolute value, not because any prediction changed.

The same predictions produce different bin summaries depending on the order of averaging and taking absolute values.

<figure class="lesson-figure" markdown="1">
  ![Opposite signed bin gaps cancel after merging despite a positive equal weighted sum of absolute gaps before merging](../../figures/assets/M04/M04-15-binning-cancellation.svg)
  <figcaption>The two equal-sized bins have signed gaps −0.1 and +0.1. Averaging absolute gaps separately gives ECE=0.1; merging them gives mean gap 0 and ECE=0. Predictions and labels have not improved: the binning creates cancellation.</figcaption>
</figure>

## Core concept 5. Multiclass calibration has several strengths

Write a model's multiclass probability output as random variable $\boldsymbol Q$ and its realized value as $\boldsymbol q=(q_1,\ldots,q_K)^\top$. Full calibration requires, for almost every prediction vector $\boldsymbol q$ under the output distribution,

\[
\mathbb P(Y=k\mid \boldsymbol Q=\boldsymbol q)=q_k
\]

for every class $k$. A prediction vector is a high-dimensional continuous value, making this difficult to verify directly in a finite sample.

Classwise calibration checks each class probability separately. Top-label calibration compares only confidence in the predicted class with correctness. Both are weaker conditions than full calibration. Stating only that a model is “calibrated,” without specifying the calibration metric, leaves the claim's scope unclear.

Full calibration matches the actual proportions of all classes simultaneously in the group receiving the same vector. A classwise check groups together vectors whose other class probabilities differ as long as $q_k$ agrees. A top-label check retains only the chosen class's correctness, without directly checking how mass is distributed among unchosen classes. Because less information is retained in conditioning, satisfying weaker calibration does not automatically imply the full-vector condition.

Agreement for one chosen class does not verify the mass allocation among the remaining classes.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Two fixed prediction vector groups have calibrated top class confidence but mismatched non top class frequencies](../../figures/assets/M04/M04-15-top-full-vector.svg)
  <figcaption>Each panel is a constructed group receiving the same displayed prediction vector. Both groups match top class 1 confidence to actual correctness at 0.6, but reported mass and actual frequency disagree for classes 2 and 3. Top-label calibration holds while full-vector calibration fails. Agreement for class 1 alone must not be generalized to calibration of every class.</figcaption>
</figure>

## Core concept 6. A proper scoring rule encourages truthful probabilities

Use scoring rule $S(q,y)$ as a loss where smaller is better. For true distribution $p$, $S$ is proper if every candidate distribution $q$ satisfies

\[
\mathbb E_{Y\sim p}[S(p,Y)]
\le
\mathbb E_{Y\sim p}[S(q,Y)]
\]

If equality holds only at $q=p$, the rule is strictly proper. This property gives a forecaster minimizing expected score a reason to report their true belief unchanged.

The log score is

\[
S_{\log}(q,y)=-\log q(y)
\]

Expected log score is cross entropy and increases by the KL divergence between the true and candidate distributions. It is therefore strictly proper under the support condition.

This definition fixes the outcome-generating $p$ and varies the reported $q$. For a proper rule, $q=p$ is one expected-loss minimizer; for a strictly proper rule, no other $q$ attains the same minimum. After seeing one outcome, assigning probability 1 to its class can reduce that observation's loss, but this is different from reporting a distribution before repeatedly observing outcomes from $p$. Using a proper score alone does not imply that a model trained on a finite sample learned correct probabilities or calibration.

With a fixed outcome distribution, both proper scores select the same truthful report in the repeated average.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Expected binary log and Brier score curves uniquely minimize at the true probability point seven](../../figures/assets/M04/M04-15-expected-proper-scores.svg)
  <figcaption>True Bernoulli probability p=0.7 is fixed while reported q varies. The two expected losses have different values and shapes, but both have a unique minimum at q=p. Green reference lines give target entropy and p(1−p)=0.21, respectively. This differs from choosing q after observing one outcome.</figcaption>
</figure>

## Core concept 7. Brier score squares probability error

For binary outcome $y\in\{0,1\}$ and positive-class probability $q$, the Brier score is

\[
S_{\mathrm{Brier}}(q,y)=(q-y)^2
\]

For multiple classes, use a one-hot target:

\[
S_{\mathrm{Brier}}(\boldsymbol q,y)
=\sum_{k=1}^{K}
\left(q_k-\mathbf 1\{k=y\}\right)^2
\]

Log score strongly penalizes predictions assigning very small probability to the realized class. Brier score uses bounded squared error. Both scores are strictly proper, but their penalties for individual samples have different shapes.

For binary true probability $p$, expected Brier score is

\[
\mathbb E[(q-Y)^2]
=p(1-q)^2+(1-p)q^2
=p(1-p)+(q-p)^2
\]

The first term is the fixed outcome variance; the second is the reported probability's squared deviation from truth. The minimum therefore occurs only at $q=p$. For multiple classes, each indicator has mean $p_k$, giving the decomposition $\sum_k p_k(1-p_k)+\sum_k(q_k-p_k)^2$ and the same conclusion. The binary expression and the multiclass sum for two classes differ by a scale factor, so specify the sum or average convention used when reporting scores.

Distinguish the expected score's optimum from the penalty applied to one realized outcome.

<figure class="lesson-figure" markdown="1">
  ![For a realized positive outcome log loss diverges at small reported probability while binary Brier remains bounded](../../figures/assets/M04/M04-15-realized-score-penalties.svg)
  <figcaption>Here realized y=1 is fixed. Log loss grows as q approaches 0, while binary Brier approaches 1. These curves show loss for this single observation, not expectations over the outcome distribution. Infinite log loss at q=0 is not plotted at a finite height.</figcaption>
</figure>

## Core concept 8. Evaluate calibration together with sharpness

Sharpness describes how concentrated an individual probability forecast is on some outcomes. In binary prediction, probabilities closer to $0$ or $1$ describe more concentrated distributions. Calibration conditions on predictions and compares actual outcome frequencies; sharpness examines the predicted distribution itself without using actual outcomes. Concentration alone does not establish that samples are distinguished correctly or that useful information is supplied.

A model reporting the base rate for every sample can satisfy aggregate calibration without distinguishing samples. If the base rate itself is near 0 or 1, this forecast is also concentrated, so sharpness and discrimination are different properties. Conversely, a model reporting extreme probabilities can appear sharp while poorly calibrated. Good probability forecasting evaluates useful discrimination and sharpness alongside maintained calibration.

Concentration of prediction distributions and discrimination between samples should not be read as the same property on one axis.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Constant and stratified calibrated forecasts have different concentration and ranking while an extreme base rate predictor is sharp without ranking](../../figures/assets/M04/M04-15-sharpness-discrimination.svg)
  <figcaption>These constructed populations have actual positive rates matching each reported probability. The first two panels compare constant 0.7 with equally weighted risk groups 0.5 and 0.9 in the same population with prevalence 0.7. The last shows constant 0.99 in a different population with prevalence 0.99: it is sharp but cannot rank samples. The horizontal axis gives reported probability, and vertical height is the proportion receiving that prediction.</figcaption>
</figure>

## Core concept 9. Temperature scaling adjusts logit magnitude

Applying temperature $T>0$ to logit vector $\boldsymbol z$ gives

\[
q_T(k\mid x)
=\frac{\exp(z_k/T)}
{\sum_j\exp(z_j/T)}
\]

For $T>1$, the distribution softens and confidence decreases. For $0<T<1$, it becomes sharper.

A positive temperature preserves logit order, so predicted classes and accuracy stay the same. Usually $T$ is fitted to decrease negative log-likelihood on a held-out validation set. This does not guarantee calibration in a new population.

The probability ratio of two classes is $q_T(k\mid x)/q_T(j\mid x)=\exp((z_k-z_j)/T)$. Dividing by the same positive $T$ preserves the sign of a logit difference. Increasing $T$ reduces its magnitude, making the ratio approach 1. This reduces probability contrast while retaining class order. Keep the same tie-breaking rule if logits tie. Scaling adjusts confidence with one scalar parameter and does not supply the freedom to satisfy every class and subgroup calibration condition separately.

Dividing logits by a common positive temperature changes probability contrast while preserving their order.

<figure class="lesson-figure" markdown="1">

![Softmax probabilities for fixed ordered logits approach each other with increasing temperature but retain their class ordering](../../figures/assets/M04/M04-15-temperature-order.svg)

<figcaption>This is the actual calculation of qₜ(k) for fixed logits (2,1,0). As T increases, the three values approach the uniform reference 1/3, while class 1 remains largest. Dashed and solid lines, color, and the legend distinguish classes. This change alone does not establish improved calibration in any population.</figcaption>
</figure>

## Core concept 10. Calibration depends on the evaluation population

Calibration is a property of the joint distribution of inputs, labels, and predictions. Changing class prevalence, input distribution, or the labeling process can change the same model's calibration.

Small ECE over the entire dataset can hide large gaps in particular subgroups. Deployment reports should record the separation of calibration and test sets, binning rules, subgroup results, proper scores, and distribution shift conditions together.

Changing subgroup proportions changes the frequency compared with the same model probability.

<figure class="lesson-figure" markdown="1">
  ![Fixed reported probability point eight matches an equal mixture of subgroup positive rates but not a shifted three to one mixture](../../figures/assets/M04/M04-15-subgroup-population-shift.svg)
  <figcaption>Every sample receives P̂=0.8, and subgroups A and B have actual positive rates 0.6 and 1. A 1:1 mixture has overall rate 0.8, but a 3:1 mixture has rate 0.7. The same model's aggregate calibration changes with population proportions. Even the original mixture's agreement does not guarantee agreement within each subgroup.</figcaption>
</figure>

## Example 1. ECE for two bins

Suppose two bins each contain half the entire sample.

| bin | confidence | accuracy |
|---|---:|---:|
| $B_1$ | $0.70$ | $0.60$ |
| $B_2$ | $0.90$ | $1.00$ |

ECE is

\[
\operatorname{ECE}
=\frac12|0.60-0.70|
+\frac12|1.00-0.90|
=0.10
\]

The first bin is overconfident and the second underconfident. Using absolute gaps prevents them from canceling.

## Example 2. Binary Brier score

With positive-class probability $q=0.8$, an outcome $y=1$ gives

\[
(0.8-1)^2=0.04
\]

An outcome $y=0$ gives

\[
(0.8-0)^2=0.64
\]

A prediction reporting high positive-class probability receives low loss on a positive outcome and high loss on a negative outcome.

## Example 3. Log score

Report $q=0.8$ as the positive-class probability. For $y=1$, the log score is

\[
-\log0.8\approx0.223
\]

and for $y=0$,

\[
-\log(1-0.8)
=-\log0.2
\approx1.609
\]

The second case, assigning a smaller probability to the realized outcome, receives a larger penalty.

## Example 4. A calibrated model that cannot discriminate

Suppose the population positive rate is $0.7$ and every sample receives $\widehat P=0.7$. In a sufficiently large sample, the group with $\widehat P=0.7$ also has positive frequency $0.7$, matching aggregate calibration.

All samples have the same score, however, so positives and negatives cannot be ranked. This illustrates why calibration alone cannot evaluate discrimination.

## Common misconceptions

### Misconception 1. High accuracy implies calibrated probabilities

Models with the same predicted labels and accuracy can have different confidences. Calibration checks frequencies at each confidence separately.

### Misconception 2. Small ECE implies calibration in every class and subgroup

Top-label ECE is one summary based on bin averages. It does not guarantee classwise, subgroup, or full-vector calibration.

### Misconception 3. A calibrated model is informative

A base-rate-only predictor can satisfy aggregate calibration. Discrimination and sharpness require separate evaluation.

### Misconception 4. Temperature scaling improves model accuracy

A positive scalar temperature preserves logit order. Predicted classes and accuracy stay unchanged; only probability concentration changes.

### Misconception 5. Calibration on one test set persists in deployment

Calibration depends on the evaluation population. It must be evaluated again if prevalence or input distribution changes.

## Exercises

### 1. Interpret perfect calibration

A binary model produces many cases with $\widehat P=0.6$. Under perfect calibration, what positive proportion is expected among these cases?

<details>
<summary>Show solution</summary>

The calibration definition requires

\[
\mathbb P(Y=1\mid \widehat P=0.6)=0.6
\]

The observed proportion in a finite sample can differ from exactly $0.6$ because of sampling variation.

</details>

### 2. Bin accuracy and confidence

A bin contains four predictions with confidences $0.7,0.8,0.9,0.8$ and correctness indicators $1,1,0,1$. Calculate bin confidence and accuracy.

<details>
<summary>Show solution</summary>

Bin confidence is

\[
\frac{0.7+0.8+0.9+0.8}{4}=0.8
\]

and accuracy is

\[
\frac{1+1+0+1}{4}=0.75
\]

Confidence is $0.05$ higher than accuracy in this bin.

</details>

### 3. Calculate ECE

Bins $B_1,B_2$ contain $40\%,60\%$ of the samples. Their $(\operatorname{acc},\operatorname{conf})$ pairs are $(0.7,0.8)$ and $(0.9,0.85)$. Calculate ECE.

<details>
<summary>Show solution</summary>

\[
\begin{aligned}
\operatorname{ECE}
&=0.4|0.7-0.8|
+0.6|0.9-0.85|\\
&=0.04+0.03\\
&=0.07.
\end{aligned}
\]

</details>

### 4. Compare Brier scores

For a sample with $y=1$, model A reports $q_A=0.9$ and model B reports $q_B=0.6$. Calculate and compare their Brier scores.

<details>
<summary>Show solution</summary>

\[
S_A=(0.9-1)^2=0.01,
\qquad
S_B=(0.6-1)^2=0.16.
\]

For this sample, model A assigns greater probability to the realized positive outcome and receives a lower score.

</details>

### 5. Compare log scores

For a binary sample with $y=0$, two predictions report positive-class probabilities $q=0.1$ and $q=0.8$. Calculate both log scores.

<details>
<summary>Show solution</summary>

The predicted probability of $y=0$ is $1-q$. Thus,

\[
-\log(1-0.1)=-\log0.9\approx0.105
\]

and

\[
-\log(1-0.8)=-\log0.2\approx1.609
\]

The second prediction assigns lower probability to the realized class and has higher loss.

</details>

### 6. Temperature scaling

An overconfident model is given $T>1$. Explain the changes to its probability distributions, predicted classes, and accuracy.

<details>
<summary>Show solution</summary>

Dividing logits by $T>1$ softens class probabilities and decreases top confidence. Dividing by a positive scalar preserves logit order, so predicted classes do not change. Accuracy on the same dataset is also unchanged.

</details>

### 7. Evaluate a calibration claim

A study concludes that “probabilities are reliable for all user groups” because test-set 10-bin top-label ECE is small. Explain the additional checks needed.

<details>
<summary>Show solution</summary>

ECE depends on bin boundaries and sample size and summarizes only top-label calibration. Check classwise reliability, calibration within subgroups, and confidence intervals. Report proper scores such as log or Brier score too, and evaluate on a held-out set not used for calibration. If the deployment distribution differs, remeasure calibration under prevalence and input shift.

</details>

## Lesson summary

- Binary calibration is expressed as $\mathbb E[Y\mid\widehat P]=\widehat P$.
- Accuracy asks about label correctness; calibration asks about agreement of probabilities and frequencies.
- A reliability diagram compares accuracy and confidence within confidence bins.
- ECE depends on binning and does not guarantee full, classwise, or subgroup calibration.
- A proper scoring rule makes reporting the true distribution minimize expected loss.
- Log and Brier scores are strictly proper scoring rules with different penalty shapes.
- Evaluate calibration together with sharpness and discrimination.
- Temperature scaling changes probability concentration while preserving predicted classes.
- Calibration results depend on the evaluation population.

## Pass criteria

You pass if you can answer the following without consulting the material.

- Can you express binary calibration using conditional expectation?
- Can you explain accuracy versus calibration with an example?
- Can you calculate bin confidence, accuracy, and ECE?
- Can you explain the limitations of top-label ECE?
- Can you write the condition defining a proper scoring rule?
- Can you calculate and compare log scores and Brier scores?
- Can you distinguish what temperature scaling changes and preserves?
- Can you explain why calibration must be evaluated again under distribution shift?

## Next lesson

- [M04-16 Correlation and causation](M04-16-correlation-causation.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Binary and multiclass calibration are distinguished.
- [x] Reliability diagrams and ECE are calculated.
- [x] ECE's binning and subgroup limitations are stated.
- [x] Proper scoring rules are defined.
- [x] Log and Brier scores are compared.
- [x] Calibration and sharpness are distinguished.
- [x] Temperature scaling and distribution shift are explained.
- [x] Every exercise has a solution.
- [x] The strength of model interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
