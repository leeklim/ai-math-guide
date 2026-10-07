---
id: "M04-07"
title: "Estimation, bias, and variance"
part: 1
stage: "M04"
status: "complete"
prerequisites:
  - "M04-04"
  - "M04-06"
estimated_time: "145–170 minutes"
---

# M04-07. Estimation, bias, and variance

## Why this lesson matters

Means, accuracies, and probe scores calculated from data change when the sample changes. Researchers use these statistics to estimate population parameters or future performance. An estimator's position around its target under repeated sampling and the extent of its variation must be evaluated separately.

Statistical bias is the difference between an estimator's mean and its target; its variance describes fluctuation across samples. Mean squared error connects both properties in one error criterion. This distinction is needed when interpreting results across seeds, small probe datasets, or selected checkpoints.

## Learning objectives

After completing this lesson, you should be able to:

- Distinguish an estimator from an observed estimate.
- Calculate estimator bias and variance from a sampling distribution.
- Decompose mean squared error into variance and squared bias.
- Explain the sample mean's unbiasedness and variance.
- Compare the bias of variance estimators with denominators $n$ and $n-1$.
- Calculate a shrinkage example that allows bias to reduce MSE.
- Examine estimation targets and selection bias in model-interpretability results.

## Prerequisite check

- Prerequisite lesson: [M04-04 Expectation, variance, and covariance](M04-04-expectation-variance-covariance.md)
- Prerequisite lesson: [M04-06 Samples, populations, and sampling distributions](M04-06-samples-populations-sampling-distributions.md)
- Check: Can you distinguish a parameter from a statistic?
- Check: Can you calculate the expectation and variance of a sample mean?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Role |
|---|---|---|---|
| $\theta$ | `theta` | The population parameter to estimate | Fixed target |
| $\widehat\theta$ | `theta hat` | An estimator that is a function of a random sample | Random variable |
| $\hat\theta$ | `theta hat` | An estimate calculated from an observed sample | Fixed number |
| $\operatorname{Bias}(\widehat\theta)$ | `the bias of theta hat` | The difference between the estimator's mean and its target | $\mathbb E[\widehat\theta]-\theta$ |
| $\operatorname{Var}(\widehat\theta)$ | `the variance of theta hat` | Fluctuation under repeated sampling | Sampling variance |
| $\operatorname{MSE}(\widehat\theta)$ | `the mean squared error of theta hat` | The mean squared error between the target and estimator | Accounts for variance and bias |
| consistency | `consistency` | An estimator's approach to its target as sample size grows | Asymptotic property |

## Core concept 1. An estimator is a rule; an estimate is its observed result

An estimator of parameter $\theta$ is a function of a random sample:

\[
\widehat\theta=T(X_1,\ldots,X_n).
\]

Before sampling, $\widehat\theta$ has a sampling distribution. Substituting observations $x_1,\ldots,x_n$ gives the estimate

\[
\hat\theta=T(x_1,\ldots,x_n)
\]

To evaluate an estimator, examine the distribution this rule produces across other possible samples, rather than only the current estimate.

The estimation target must also be specified mathematically. For test accuracy, $\theta$ differs depending on whether the target is the mean over a particular finite benchmark or the probability of a correct prediction on future inputs.

## Core concept 2. Bias is a systematic difference in the estimator's mean

An estimator's bias is

\[
\operatorname{Bias}(\widehat\theta)
=\mathbb E[\widehat\theta]-\theta
\]

The expectation is taken over the sampling distribution obtained by repeating the same sampling procedure.

If

\[
\mathbb E[\widehat\theta]=\theta
\]

then $\widehat\theta$ is an unbiased estimator. Unbiasedness does not mean that one observed estimate equals the target. It means that estimates average to the target under repeated sampling.

Statistical bias differs from a neural network affine layer's bias vector. The former is a repeated-sampling property of an estimation rule; the latter is a model parameter.

## Core concept 3. Estimator variance describes sensitivity to changing samples

An estimator's variance is

\[
\operatorname{Var}(\widehat\theta)
=\mathbb E\left[
(\widehat\theta-\mathbb E[\widehat\theta])^2
\right]
\]

It describes how much estimates fluctuate when new samples are drawn from the same population.

For two estimators with the same bias, the one with lower variance is more stable. Low variance can coexist with large bias, so stability alone does not establish closeness to the target.

Changing the center and width of sampling distributions separately on axes with the same target distinguishes these properties.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Four illustrative Gaussian estimator sampling densities with fixed target zero, biases zero or one and variances one or 0.16](../../figures/assets/M04/M04-07-bias-variance.svg)

<figcaption>Left and right panels differ in center; upper and lower panels differ in spread. A tightly concentrated distribution such as the lower-right one can still miss the target. These are illustrative estimator distributions, not neural-network bias parameters.</figcaption>
</figure>

## Core concept 4. MSE decomposes into variance and squared bias

Mean squared error (MSE) is

\[
\operatorname{MSE}(\widehat\theta)
=\mathbb E\left[(\widehat\theta-\theta)^2\right]
\]

Add and subtract $m=\mathbb E[\widehat\theta]$:

\[
\widehat\theta-\theta
=(\widehat\theta-m)+(m-\theta)
\]

After squaring and taking expectation, the cross term vanishes because $\mathbb E[\widehat\theta-m]=0$:

\[
\operatorname{MSE}(\widehat\theta)
=\operatorname{Var}(\widehat\theta)
+\operatorname{Bias}(\widehat\theta)^2.
\]

MSE compares variance and systematic deviation from the target in a common unit. An unbiased estimator has zero bias, so its MSE equals its variance.

The expansion's cross term is $2(m-\theta)(\widehat\theta-m)$. Since $m-\theta$ is fixed, its expectation is $2(m-\theta)\mathbb E[\widehat\theta-m]=0$. No independence assumption is needed for this cancellation. The first remaining squared term is variance around the estimator's own mean; the second is the squared distance between that mean and the target. These errors add under a finite second moment.

When two estimates occur with equal probability, a small example shows how the centered error and bias divide an individual error.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Illustrative estimator values one and three with equal masses, estimator mean two and target one, separating bias one from centered errors minus and plus one and cancelling their cross terms in expectation](../../figures/assets/M04/M04-07-mse-cross-term.svg)

<figcaption>The left estimate has total error 0 and the right one has total error 2. Only the cross term's mean vanishes. Variance around the center and squared bias each remain 1, giving MSE 2.</figcaption>
</figure>

## Core concept 5. The sample mean is an unbiased estimator of the population mean

For an iid sample $X_1,\ldots,X_n$ with mean $\mu$ and variance $\sigma^2$, define

\[
\widehat\mu=\bar X=\frac1n\sum_{i=1}^{n}X_i
\]

Linearity of expectation gives

\[
\mathbb E[\widehat\mu]=\mu
\]

so the bias is 0. Independence gives

\[
\operatorname{Var}(\widehat\mu)=\frac{\sigma^2}{n}
\]

Consequently,

\[
\operatorname{MSE}(\widehat\mu)=\frac{\sigma^2}{n}.
\]

Variance and MSE decrease as sample size grows. This result depends on iid sampling and finite variance.

## Core concept 6. The sample-variance denominator $n-1$ corrects bias

As in the preceding section, use an iid sample with mean $\mu$ and finite variance $\sigma^2$, and let $n\ge2$. Replacing the unknown population mean $\mu$ by the sample mean gives

\[
\sum_{i=1}^{n}(X_i-\bar X)^2
=\sum_{i=1}^{n}(X_i-\mu)^2
-n(\bar X-\mu)^2
\]

To obtain this identity, square and sum $X_i-\mu=(X_i-\bar X)+(\bar X-\mu)$. The sum of cross terms is $2(\bar X-\mu)\sum_i(X_i-\bar X)$, which vanishes because deviations from the sample mean sum to 0. The second deviation is shared by every $i$, so its square appears once in each term, giving $n(\bar X-\mu)^2$. Thus, the squared-deviation sum around the sample mean is smaller than the corresponding sum around the population mean by this amount.

Moving the center for one observed sample shows that the squared-deviation sum is minimized at the sample mean.

<figure class="lesson-figure" markdown="1">

![Squared-deviation sum of observed values two four six as a function of center, minimized at sample mean four with sum eight rather than eleven at an illustrative population mean three](../../figures/assets/M04/M04-07-fitted-center.svg)

<figcaption>For this sample, fitting the center from 3 to 4 reduces the sum by 3. A single sample's numbers do not prove unbiasedness; the next expectation calculation finds the mean reduction under the same sampling rule.</figcaption>
</figure>

Taking expectation on both sides gives

\[
\mathbb E\left[
\sum_{i=1}^{n}(X_i-\bar X)^2
\right]
=n\sigma^2-n\frac{\sigma^2}{n}
=(n-1)\sigma^2.
\]

The first sum on the original identity's right side consists of squared deviations from the population mean, each with expectation $\sigma^2$. Since $\bar X$ is unbiased for $\mu$, $\mathbb E[(\bar X-\mu)^2]=\operatorname{Var}(\bar X)=\sigma^2/n$. Estimating and fitting the center from the same data reduces the squared-deviation sum on average.

Therefore,

\[
S^2=\frac{1}{n-1}
\sum_{i=1}^{n}(X_i-\bar X)^2
\]

is unbiased for $\sigma^2$. Using denominator $n$ instead gives

\[
\widetilde S^2=\frac1n
\sum_{i=1}^{n}(X_i-\bar X)^2
\]

with

\[
\mathbb E[\widetilde S^2]
=\frac{n-1}{n}\sigma^2
\]

so it has downward bias. Denominator $n-1$ is not superior for every purpose. Another estimator can have lower MSE depending on the target and loss.

The denominators differ in their correction to the estimator's mean under repeated sampling, not in making one observed value exact.

<figure class="lesson-figure" markdown="1">

![Expected variance estimator divided by population variance across integer sample sizes, with denominator n below one and denominator n minus one exactly one under iid sampling](../../figures/assets/M04/M04-07-variance-correction.svg)

<figcaption>The vertical axis is the ratio of the estimator's expectation to population variance, not a variance calculated once. The difference between the two expectations shrinks as n grows, but denominator n produces more downward bias for small samples.</figcaption>
</figure>

## Core concept 7. Shrinkage can allow bias to reduce variance

Consider the population-mean estimation rule

\[
\widehat\mu_a=a\bar X,
\qquad 0\le a\le1
\]

Here $a$ is a constant chosen separately from the observations, and the estimator shrinks toward 0. Its bias and variance are

\[
\operatorname{Bias}(\widehat\mu_a)
=(a-1)\mu,
\]

\[
\operatorname{Var}(\widehat\mu_a)
=a^2\frac{\sigma^2}{n}
\]

Thus,

\[
\operatorname{MSE}(\widehat\mu_a)
=a^2\frac{\sigma^2}{n}
+(a-1)^2\mu^2.
\]

When $a<1$ and $\mu\ne0$, bias appears, while positive sampling variance decreases. The total MSE can decrease for particular $\mu,\sigma^2,n$. Normalization and regularization can produce a similar tradeoff while improving estimation stability.

Linearity gives $\mathbb E[a\bar X]=a\mu$, so subtracting target $\mu$ gives bias $(a-1)\mu$. Multiplication by a fixed scale factor multiplies variance by its square, giving sampling variance $a^2\sigma^2/n$. Substituting both into the MSE decomposition gives the formula above. If $a$ itself were estimated from the same sample, the fixed-constant scaling formula would not apply directly.

For the example's $a=1/2$, MSE is $\sigma^2/(4n)+\mu^2/4$. Comparing this with the original sample mean's MSE $\sigma^2/n$ shows improvement when $\mu^2<3\sigma^2/n$. The benefit therefore depends on how far the target lies from 0 and how much the current mean estimate fluctuates.

An illustrative Gaussian sampling distribution with Example 2's moments shows that a fixed factor of 1/2 both narrows the distribution and pulls its center toward 0.

<figure class="lesson-figure" markdown="1">

![Illustrative normal sampling densities for a mean estimator centered at one with variance one and its half-shrunken estimator centered at one half with variance one quarter](../../figures/assets/M04/M04-07-shrinkage-density.svg)

<figcaption>The narrower distribution's center is 0.5 below the target. The example's MSE calculation needs no Gaussian assumption; the figure selects one sampling distribution with those moments.</figcaption>
</figure>

With the same original variance, shrinkage's MSE benefit or cost changes with the target's distance from 0.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Variance bias squared and total MSE across fixed shrinkage coefficients for population means one and three with original mean variance one](../../figures/assets/M04/M04-07-shrinkage-mse.svg)

<figcaption>The green points compare coefficients 1/2 and 1. MSE falls from 1 to 0.5 above but rises from 1 to 2.5 below. Reduced variance alone does not establish improvement.</figcaption>
</figure>

## Core concept 8. Consistency concerns increasing sample size

An estimator sequence $\widehat\theta_n$ is consistent for $\theta$ if, for every $\varepsilon>0$,

\[
P\left(
|\widehat\theta_n-\theta|>\varepsilon
\right)\to0
\qquad(n\to\infty)
\]

As sample size grows, the probability of being more than a fixed distance from the target approaches 0.

Unbiasedness and consistency are different properties. An estimator biased in small samples can still be consistent if both its bias and variance approach 0 with $n$. An unbiased estimator need not be consistent if its variance does not decrease.

Outside a fixed $\varepsilon$, squared error is at least $\varepsilon^2$. That magnitude times the event probability cannot exceed the mean squared error, so

\[
P(|\widehat\theta_n-\theta|>\varepsilon)
\le\frac{\operatorname{MSE}(\widehat\theta_n)}{\varepsilon^2}
\]

If bias and variance both approach 0, MSE does too, and the probability above approaches 0 for each fixed $\varepsilon>0$. This is one way to check the consistency just described. In contrast, repeatedly using only the first observation $X_1$ to estimate the mean of the preceding lesson's Bernoulli$(0.5)$ sample is unbiased, but increasing sample size leaves $|X_1-0.5|=0.5$. The probability of being outside $\varepsilon=0.25$ is 1, so the rule is not consistent.

For this Bernoulli counterexample, probabilities of remaining a fixed distance outside the target can be calculated exactly at each sample size.

<figure class="lesson-figure" markdown="1">

![Exact probabilities of deviating more than one quarter from the Bernoulli mean one half, declining for the full sample mean but staying one for the first-observation estimator](../../figures/assets/M04/M04-07-consistency-tail.svg)

<figcaption>The sample mean uses the full sample; the first-observation rule still uses one observation as more data arrive. Small irregularities in the blue curve come from finite discrete support and the strict inequality. Consistency does not require a monotone decrease at every n.</figcaption>
</figure>

## Example 1. Compare two estimators' bias and MSE

### Problem

$\bar X$ is unbiased for $\mu$ with $\operatorname{Var}(\bar X)=\sigma^2/n$. Calculate the bias, variance, and MSE of $\widehat\mu_{1/2}=\frac12\bar X$.

### Solution

Since

\[
\mathbb E[\widehat\mu_{1/2}]
=\frac12\mathbb E[\bar X]
=\frac12\mu
\]

the bias is

\[
\operatorname{Bias}(\widehat\mu_{1/2})
=-\frac12\mu.
\]

The variance is

\[
\operatorname{Var}(\widehat\mu_{1/2})
=\frac14\frac{\sigma^2}{n}
\]

and MSE is

\[
\operatorname{MSE}(\widehat\mu_{1/2})
=\frac{\sigma^2}{4n}+\frac{\mu^2}{4}
\]

### Meaning of the result

Halving the scale reduces sampling variance to one quarter but introduces bias toward 0. Comparing MSE requires $\mu$, $\sigma^2$, and $n$.

## Example 2. Compare shrinkage MSE numerically

Let $\mu=1$, $\sigma^2=4$, and $n=4$. The MSE of $\bar X$ is

\[
\frac{\sigma^2}{n}=1
\]

For $a=1/2$,

\[
\operatorname{Var}(\widehat\mu_{1/2})
=\frac14\cdot1=0.25
\]

and squared bias is also

\[
\left(-\frac12\right)^2=0.25
\]

Total MSE is $0.5$, so the shrinkage estimator has lower MSE in this parameter setting.

## Example 3. An accuracy estimator

Let $I_i$ indicate a correct prediction on the $i$th iid sample, with $P(I_i=1)=p$. Observed accuracy

\[
\widehat p=\frac1n\sum_{i=1}^{n}I_i
\]

is unbiased for $p$, with

\[
\operatorname{Var}(\widehat p)
=\frac{p(1-p)}{n}
\]

With class imbalance or cluster dependence, revisit the population accuracy used as the target and the iid condition.

## Example 4. Selection bias from choosing a checkpoint

Evaluating 100 checkpoints on the same validation set and reporting the highest score can select a checkpoint with unusually favorable noise. Its selection-set validation score can optimistically estimate the selected checkpoint's future performance. Checking this bias requires one evaluation on a separate test set or a repeated-sampling design that includes the entire selection procedure.

## Common misconceptions

### Misconception 1. An unbiased estimator is exact whenever observed

Unbiasedness concerns the sampling distribution's mean. An estimate from one sample can lie far from the target.

### Misconception 2. A low-variance estimator is close to the target

Estimates can cluster around a value whose center misses the target. Comparing target error requires both bias and variance.

### Misconception 3. A biased estimator cannot be used

Allowing small bias to substantially reduce variance can lower MSE. The comparison depends on the loss and target.

### Misconception 4. Large samples remove all bias

Increasing sample size can reduce sampling variance. Reducing selection bias, measurement bias, and target-population mismatch requires changing the sampling procedure or measurement design.

### Misconception 5. Averaging multiple seeds also captures data uncertainty

Seed variation measures fluctuation from initialization and training randomness. Variation from input samples, annotation, and model families requires separate sampling levels.

## Exercises

### 1. Estimator and estimate

Explain the roles of $\widehat\mu=n^{-1}\sum_iX_i$ and the estimate $\hat\mu=2.7$ obtained from observed data.

<details>
<summary>Show solution</summary>

$\widehat\mu$ is an estimator varying across possible samples and has a sampling distribution. $\hat\mu=2.7$ is the estimate obtained by applying it to one observed sample.

</details>

### 2. Calculate bias

Given $\mathbb E[\widehat\theta]=5.4$ and target $\theta=5$, calculate the bias and explain its direction.

<details>
<summary>Show solution</summary>

\[
\operatorname{Bias}(\widehat\theta)=5.4-5=0.4.
\]

This is upward bias: under repeated sampling, the estimator's mean exceeds the target by $0.4$.

</details>

### 3. MSE decomposition

Given $\operatorname{Var}(\widehat\theta)=0.9$ and bias $-0.2$, calculate MSE.

<details>
<summary>Show solution</summary>

\[
\operatorname{MSE}(\widehat\theta)
=0.9+(-0.2)^2
=0.94.
\]

MSE uses squared bias, so its sign disappears.

</details>

### 4. Compare sample means

Population variance is $16$. Calculate the sample mean's variance and standard error for iid sample sizes 4 and 64.

<details>
<summary>Show solution</summary>

For $n=4$,

\[
\operatorname{Var}(\bar X)=\frac{16}{4}=4,
\qquad
\operatorname{SE}(\bar X)=2.
\]

For $n=64$,

\[
\operatorname{Var}(\bar X)=\frac{16}{64}=0.25,
\qquad
\operatorname{SE}(\bar X)=0.5.
\]

</details>

### 5. A variance estimator's bias

For $n=5$ and population variance $\sigma^2=10$, calculate the expectation and bias of $\widetilde S^2$, which uses denominator $n$.

<details>
<summary>Show solution</summary>

\[
\mathbb E[\widetilde S^2]
=\frac{n-1}{n}\sigma^2
=\frac45\cdot10
=8.
\]

Bias is $8-10=-2$.

</details>

### 6. Compare shrinkage

For $\mu=0.5$ and $\sigma^2/n=1$, compare the MSE of $\bar X$ and $\widehat\mu_{1/2}=\bar X/2$.

<details>
<summary>Show solution</summary>

$\bar X$ is unbiased, so its MSE is 1. The shrinkage estimator has variance $1/4$ and bias

\[
\left(\frac12-1\right)0.5=-0.25
\]

Thus,

\[
\operatorname{MSE}(\widehat\mu_{1/2})
=0.25+0.25^2
=0.3125.
\]

The shrinkage estimator has lower MSE in this parameter setting.

</details>

### 7. Critique a model-interpretability design

A researcher compares 30 probe architectures on the same test set and reports only the highest accuracy. Explain the bias introduced and how to change the evaluation procedure.

<details>
<summary>Show solution</summary>

Repeated use of the test set for model selection introduces selection bias: the highest score also selects favorable test noise. Choose architectures with training and validation data, then evaluate final performance on a previously untouched test set. Variation across the entire selection procedure, including multiple seeds and dataset splits, can also be reported.

</details>

## Lesson summary

- An estimator is a function of a random sample; an estimate is its value on an observed sample.
- Bias is the difference between an estimator's mean and target; variance describes fluctuation across samples.
- MSE is estimator variance plus squared bias.
- An iid sample mean is unbiased for the population mean and has variance $\sigma^2/n$.
- Under iid sampling, sample variance with denominator $n-1$ is unbiased for population variance.
- Shrinkage can allow bias to reduce variance and MSE.
- Reporting the best result on the data used for selection can estimate performance optimistically.

## Pass criteria

You pass if you can answer these questions without consulting the material.

- Can you distinguish an estimator from an estimate?
- Can you calculate bias and variance from a sampling distribution?
- Can you derive the MSE decomposition?
- Can you explain the sample mean's bias and variance?
- Can you calculate why sample variance uses $n-1$?
- Can you calculate a shrinkage estimator's bias-variance tradeoff?
- Can you identify and correct an evaluation procedure introducing selection bias?

## Next lesson

- [M04-08 Regression and classification](M04-08-regression-classification.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Estimators and estimates are distinguished.
- [x] Bias, variance, and MSE are defined and decomposed.
- [x] Expectations of the sample mean and sample variance are calculated.
- [x] Shrinkage's bias-variance tradeoff has been checked numerically.
- [x] Consistency and unbiasedness are distinguished.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretability claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] No prerequisites outside the stated scope are required implicitly.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
