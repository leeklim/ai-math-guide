---
id: "M04-09"
title: "Confidence intervals and bootstrap"
part: 1
stage: "M04"
status: "complete"
prerequisites:
  - "M04-05"
  - "M04-06"
  - "M04-07"
estimated_time: "150–180 minutes"
---

# M04-09. Confidence intervals and bootstrap

## Why this lesson matters

A single point estimate does not show sampling uncertainty. Even with mean accuracy 0.74, estimation precision depends on sample size and dependence among observations. A confidence interval is an interval-estimation procedure designed to include a parameter at a specified rate under repeated sampling.

When a statistic's sampling distribution is difficult to derive, bootstrap resampling from the observed sample can approximate its variation. The same principle applies to differences between two models' metrics, prompt-level attribution means, and probe scores. Specifying the resampling unit and interval interpretation makes the supported generalization scope clear.

## Learning objectives

After completing this lesson, you should be able to:

- Explain confidence level as repeated-sampling coverage.
- Calculate a point estimator's confidence interval using a normal approximation.
- Distinguish the conditions used by z and t intervals for a mean.
- Construct bootstrap resamples and replicates.
- Calculate bootstrap standard error and a percentile interval.
- Choose resampling units for paired or clustered data.
- Limit claims supported by an interval's width and inclusion of a reference value.

## Prerequisite check

- Prerequisite lesson: [M04-05 Common distributions](M04-05-common-distributions.md)
- Prerequisite lesson: [M04-06 Samples, populations, and sampling distributions](M04-06-samples-populations-sampling-distributions.md)
- Prerequisite lesson: [M04-07 Estimation, bias, and variance](M04-07-estimation-bias-variance.md)
- Check: Can you explain standard error as the standard deviation of a sampling distribution?
- Check: Can you distinguish an estimator, an estimate, and bias?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Scope and role |
|---|---|---|---|
| $1-\alpha$ | `one minus alpha` | Confidence level | For example, $0.95$ |
| $C(X_1,\ldots,X_n)$ | `C of X one through X n` | A random interval whose two endpoints come from the sample | Random before sampling |
| $z_{1-\alpha/2}$ | `z sub one minus alpha over two` | The value where the standard-normal CDF equals $1-\alpha/2$ | About 1.96 for 95% |
| $t_{\nu,1-\alpha/2}$ | `t sub nu comma one minus alpha over two` | A critical value of the t distribution with $\nu$ degrees of freedom | Mean interval with unknown population variance |
| $B$ | `B` | Number of bootstrap replicates | Positive integer |
| $\widehat\theta^{*(b)}$ | `theta hat star superscript b` | The statistic calculated on the $b$th bootstrap resample | $b=1,\ldots,B$ |
| $q_p^*$ | `q sub p star` | The replicate value at proportion $p$ | Used in a percentile interval |

## Core concept 1. A confidence interval is a random-interval procedure with coverage

Write a confidence interval procedure for parameter $\theta$ as

\[
C(X_1,\ldots,X_n)=[L(X_1,\ldots,X_n),U(X_1,\ldots,X_n)]
\]

A $100(1-\alpha)\%$ confidence interval is designed so that repeated sampling satisfies

\[
P_\theta\left(
\theta\in C(X_1,\ldots,X_n)
\right)=1-\alpha
\]

or satisfies this approximately. Before sampling, endpoints are random variables. After observing the sample, the calculated interval $[l,u]$ is fixed.

“95% confidence” means that repeating sampling and interval calculation under the same conditions produces intervals of which about 95% contain fixed $\theta$. Interpreting a particular observed interval as containing $\theta$ with probability 95% requires another framework, such as a Bayesian interval that places a probability distribution on the parameter.

Across repetitions, the sample and interval location change, not the parameter.

<figure class="lesson-figure" markdown="1">

![Twelve constructed possible intervals centered on different sample estimates with fixed parameter zero, ten covering the parameter and two missing it](../../figures/assets/M04/M04-09-interval-coverage.svg)

<figcaption>The gray vertical line is the fixed parameter; each horizontal line is one possible sample's interval. This constructed illustration does not force the covering proportion among 12 intervals to be 95%. The 95% refers to the procedure over all possible repeated samples, not an exact proportion in a short list.</figcaption>
</figure>

## Core concept 2. A normal-form interval uses an estimate and standard error

If an estimator's sampling distribution satisfies

\[
\frac{\widehat\theta-\theta}
{\operatorname{SE}(\widehat\theta)}
\approx\mathcal N(0,1)
\]

an approximate $100(1-\alpha)\%$ interval is

\[
\hat\theta
\pm
z_{1-\alpha/2}
\widehat{\operatorname{SE}}(\widehat\theta)
\]

For 95%, use $z_{0.975}\approx1.96$.

Leaving $\alpha/2$ in each standard-normal tail gives probability $1-\alpha$ between the critical values. For positive standard error, solving

\[
-z_{1-\alpha/2}
\le\frac{\widehat\theta-\theta}{\operatorname{SE}(\widehat\theta)}
\le z_{1-\alpha/2}
\]

for $\theta$ gives $\widehat\theta-z_{1-\alpha/2}\operatorname{SE}(\widehat\theta)\le\theta\le\widehat\theta+z_{1-\alpha/2}\operatorname{SE}(\widehat\theta)$. The event that a random variable falls between two bounds has been rewritten as the event that a parameter lies in a random interval. In practice, unknown standard error is estimated too, so both the standardized estimator's normal approximation and standard-error estimation must be appropriate. Substantial remaining bias can invalidate this centering condition even with an accurately calculated standard deviation.

Interval width is proportional to standard error and the critical value. If greater sample size reduces standard error, the interval narrows at the same confidence level. Raising the confidence level increases the critical value and widens the interval.

Retaining a central probability in standardized error and calculating endpoints around an observed estimate are corresponding but distinct steps.

<figure class="lesson-figure" markdown="1">

![Standard normal density with approximately 0.95 central area between minus and plus 1.96 and equal 0.025 probability tails](../../figures/assets/M04/M04-09-normal-central-mass.svg)

<figcaption>The shaded region is area for the standardized random variable. Solving the event of being between the critical values as inequalities for the parameter produces an interval around the observation.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![Observed estimate ten and standard error one giving fixed interval endpoints eight point zero four and eleven point nine six on a numeric axis](../../figures/assets/M04/M04-09-interval-endpoints.svg)

<figcaption>Example 1's endpoints subtract and add the same margin to the same estimate. This observed interval is already fixed; the figure does not draw a new probability density for the parameter.</figcaption>
</figure>

## Core concept 3. Mean z and t intervals differ in their population-variance conditions

If $X_1,\ldots,X_n\overset{\mathrm{iid}}{\sim}\mathcal N(\mu,\sigma^2)$ and $\sigma>0$ is known,

\[
\bar X
\pm
z_{1-\alpha/2}
\frac{\sigma}{\sqrt n}
\]

is an exact confidence interval for $\mu$.

If $\sigma$ is unknown and replaced by sample standard deviation $S$, then

\[
\frac{\bar X-\mu}{S/\sqrt n}
\]

has a t distribution with $n-1$ degrees of freedom under a Gaussian population. The interval is

\[
\bar X
\pm
t_{n-1,1-\alpha/2}
\frac{S}{\sqrt n}
\]

For small samples, the t distribution reflects uncertainty in estimating population variance with heavier tails than the standard normal. Large-sample means can use approximate intervals based on the CLT and estimated standard error, but skewness, heavy tails, and dependence must be checked.

$S$ is the square root of M04-06's sample variance with denominator $n-1$, and this t procedure requires $n\ge2$. Unlike the z statistic with known $\sigma$, the t statistic's denominator also varies with the sample. A smaller estimated denominator makes the same mean deviation a larger ratio, so a t critical value is used instead of the standard-normal one. This is an exact distributional result under the iid Gaussian conditions above. Merely replacing $\sigma$ by $S$ does not give an exact t interval for every population.

Comparing the t distribution with 9 degrees of freedom to the standard normal shows how tail differences, rather than center height, directly relate to the changed critical value.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Standard normal and Student t with nine degrees of freedom densities in a full view and an enlarged right tail with 97.5 percent cutoffs 1.96 and 2.262](../../figures/assets/M04/M04-09-t-normal-tails.svg)

<figcaption>The lower panel enlarges the right tail. To leave the same right-tail probability, the t critical value lies farther right. This distributional comparison applies when S is estimated under the text's iid Gaussian conditions, not as an exact t-coverage guarantee for arbitrary data.</figcaption>
</figure>

## Core concept 4. Bootstrap draws another sample from the empirical distribution

Let the observed sample be $x_1,\ldots,x_n$ and the statistic of interest be

\[
\hat\theta=T(x_1,\ldots,x_n)
\]

The nonparametric bootstrap proceeds as follows.

1. Draw $n$ observations with replacement from the $n$ observed values to form bootstrap sample $x_1^*,\ldots,x_n^*$.
2. Calculate the same statistic $\widehat\theta^*=T(x_1^*,\ldots,x_n^*)$.
3. Repeat $B$ times to obtain $\widehat\theta^{*(1)},\ldots,\widehat\theta^{*(B)}$.

Sampling with replacement allows an observation to appear multiple times or be absent from a resample. Bootstrap uses empirical distribution $\widehat P_n$ as a substitute for the population distribution to approximate estimator sampling variation.

Specifically, choose among original sample indices $1,\ldots,n$ with probability $1/n$ each, independently $n$ times. A value present at multiple indices has selection probability equal to the sum of those indices' probabilities. Resample size $n$ preserves the sample size used for the original estimator. In contrast, $B$ counts simulations of this size-$n$ sampling experiment. Once the observed sample is fixed, new randomness comes only from resample selection. The resulting distribution is not necessarily identical to the true sampling distribution under the unknown population.

In Example 3, indices of the two observed records are chosen anew each time, so one record can be drawn twice.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![All four ordered size-two bootstrap resamples from fixed observed records one and three, each with probability one quarter and mapped to mean replicates one two two three](../../figures/assets/M04/M04-09-bootstrap-index-draws.svg)

<figcaption>Each box is a resample of size n=2; its number below is a replicate calculated by the same rule. The figure lists every possible resample. Replicate count B and original sample size n are different quantities.</figcaption>
</figure>

## Core concept 5. Replicates give bootstrap standard error and percentile intervals

Let the bootstrap-replicate mean be

\[
\overline{\theta^*}
=\frac1B\sum_{b=1}^{B}\widehat\theta^{*(b)}
\]

Bootstrap standard error is

\[
\widehat{\operatorname{SE}}_{\mathrm{boot}}
=\sqrt{
\frac{1}{B-1}
\sum_{b=1}^{B}
\left(
\widehat\theta^{*(b)}-\overline{\theta^*}
\right)^2
}
\]

The percentile interval uses replicate quantiles at $\alpha/2$ and $1-\alpha/2$:

\[
[q^*_{\alpha/2},q^*_{1-\alpha/2}]
\]

For $B\ge2$, this standard error is the replicates' sample standard deviation. Each replicate simulates one sampling instance for the original estimator, so between-replicate spread estimates the estimator's variation. Dividing again by $\sqrt B$ gives a different quantity: the replicate mean's Monte Carlo standard error. Increasing $B$ does not increase original data size $n$ and does not reduce the original estimator's sampling uncertainty by that factor.

The percentile interval sorts replicates and chooses two positions leaving proportion $\alpha/2$ below and $\alpha/2$ above. For finite $B$, the desired proportion's index need not be an integer, so quantile-selection or interpolation rules are used. State the quantile rule to make endpoints reproducible even for the same replicates. Whether this empirical central interval achieves the desired parameter coverage depends on the bootstrap approximation's quality.

The percentile interval is short to calculate, but coverage can be inaccurate with estimator bias, skewness, or small samples. Bootstrap-t and bias-corrected intervals use additional corrections. This lesson covers the principles of standard error and percentile intervals.

Below is a constructed list of B=20 replicates using Example 3's possible mean values. Standard deviation and quantiles are calculated separately from this list.

<figure class="lesson-figure" markdown="1">

![Twenty illustrative sorted bootstrap mean replicates with five ones ten twos and five threes, linear-interpolated 2.5 and 97.5 percent quantiles one and three and replicate sample standard deviation about 0.725](../../figures/assets/M04/M04-09-sorted-replicates.svg)

<figcaption>The horizontal axis is sorted replicate rank, not original-data index. Linear-interpolated quantiles give percentile interval [1, 3], which includes every listed value because of ties. Replicate standard deviation with denominator B−1 is about 0.725 and is not divided again by √B. A finite list's value can differ from Example 3's exact bootstrap-distribution standard deviation of about 0.707.</figcaption>
</figure>

## Core concept 6. Paired comparisons resample observation units together

If metrics $A_i,B_i$ for two models are calculated on the same prompt $i$, the statistic of interest can be the mean of differences

\[
D_i=A_i-B_i
\]

Paired bootstrap resamples prompt indices and takes both $A_i,B_i$ for each selected prompt. This preserves prompt-level correlations between the model results.

Resampling $A$ and $B$ separately loses pairing and can misestimate difference sampling variation. With clusters such as tokens within a document or images within a patient, consider resampling independent clusters or using a hierarchical bootstrap preserving the levels.

M04-04 gave difference variance $\operatorname{Var}(A-B)=\operatorname{Var}(A)+\operatorname{Var}(B)-2\operatorname{Cov}(A,B)$. If prompt difficulty moves both scores together, the covariance term also affects difference variation. Selecting both scores with one prompt index preserves the observed pairs, whereas choosing two separate indices loses the original pair covariance. Pairing means that each $A_i,B_i$ comes from the same observation unit, not merely that sample sizes are equal.

Preserving three prompts' score pairs and choosing model-specific indices separately produce different possible joint results.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three illustrative paired prompt scores with constant difference 0.1 compared with nine cross-prompt combinations produced by separately drawing model scores, along with their exact single-draw difference PMFs](../../figures/assets/M04/M04-09-paired-resampling.svg)

<figcaption>The left selects only the three observed pairs; the right creates new pairs across prompts. Lower bars show single-draw difference distributions, not mean-difference distributions for whole resamples. All observed differences coincide in this example, not in paired data generally.</figcaption>
</figure>

## Core concept 7. Bootstrap does not repair sampling-design defects

Bootstrap relies on the observed empirical distribution adequately representing the target population and on independent resampling units. Missing groups, measurement error, and data leakage persist when the same sample is resampled.

If a small sample misses a rare event, its bootstrap resamples also miss that event. Applying iid bootstrap to time-series or spatial data can break dependence. Methods appropriate to the structure, such as block or cluster bootstrap, are needed.

Finite $B$ also introduces Monte Carlo error into bootstrap results. Record the random seed and check endpoint stability as $B$ increases.

Sampling with replacement cannot produce values absent from the empirical distribution.

<figure class="lesson-figure" markdown="1">

![Illustrative population assigning positive probability to outcome c but a possible observed sample containing only a and b, so every bootstrap resample excludes c regardless of replicate count](../../figures/assets/M04/M04-09-unseen-outcome.svg)

<figcaption>c is possible in this population but absent from the observed sample. Increasing B still draws from the same empirical support and provides no new information about the missing event.</figcaption>
</figure>

## Core concept 8. Report the interval's target and generalization scope

“The 95% CI is $[0.02,0.08]$” leaves out the target statistic, sampling unit, data split, and interval method. Identical numbers have different interpretations for a prompt-level mean difference and a token-level mean difference.

A narrow confidence interval means small estimator randomness under the chosen sampling model. It does not imply small measurement bias, model misspecification, or distribution shift. Looking only at whether an interval includes 0 discards effect size and width, preventing assessment of both magnitude and precision.

Even intervals with the same point estimate give different information about precision through their widths.

<figure class="lesson-figure" markdown="1">

![Two illustrative intervals centered on the same estimate 0.05, one from 0.02 to 0.08 and one from minus 0.10 to 0.20, with zero marked as a reference](../../figures/assets/M04/M04-09-interval-width-effect.svg)

<figcaption>The point estimates are identical, but precision about the possible effect range differs. Including 0 in the wide interval does not change the estimated effect to 0. Either interval requires a specified target and sampling unit for generalization.</figcaption>
</figure>

## Example 1. A mean z interval with known population standard deviation

### Problem

Given $\bar x=10$, population standard deviation $\sigma=4$, and iid sample size $n=16$, calculate a 95% confidence interval using $z_{0.975}=1.96$.

### Solution

Standard error is

\[
\frac{\sigma}{\sqrt n}
=\frac4{4}=1
\]

The margin of error is

\[
1.96\cdot1=1.96
\]

so the interval is

\[
10\pm1.96=[8.04,11.96]
\]

### Meaning of the result

Repeating this procedure on iid samples of size 16 from the same population produces intervals of which 95% contain $\mu$.

## Example 2. A mean t interval with unknown population variance

Let $\bar x=5$, $s=3$, $n=10$, and $t_{9,0.975}=2.262$. Estimated standard error is

\[
\frac{s}{\sqrt n}
=\frac3{\sqrt{10}}
\approx0.949
\]

and the margin is

\[
2.262\cdot0.949\approx2.146
\]

The 95% t interval is

\[
[5-2.146,5+2.146]
=[2.854,7.146]
\]

Exact coverage requires an iid Gaussian population.

## Example 3. Bootstrap distribution for two observations

Let the observed sample be $(1,3)$ and the statistic the sample mean. Possible ordered bootstrap samples of size 2 and their means are:

| Bootstrap sample | Probability | Mean |
|---|---:|---:|
| $(1,1)$ | $1/4$ | 1 |
| $(1,3)$ | $1/4$ | 2 |
| $(3,1)$ | $1/4$ | 2 |
| $(3,3)$ | $1/4$ | 3 |

The bootstrap mean assigns probabilities $1/4,1/2,1/4$ to $1,2,3$. Bootstrap variance is

\[
\frac14(1-2)^2+\frac12(2-2)^2+\frac14(3-2)^2
=\frac12
\]

giving bootstrap standard error $\sqrt{1/2}\approx0.707$.

## Example 4. Paired bootstrap for a model difference

For each prompt, calculate models A and B's accuracy contributions or scores together. Resample prompt indices with replacement, and calculate the mean difference in each resample:

\[
\widehat\Delta^*
=\frac1n\sum_{i=1}^{n}(A_i^*-B_i^*)
\]

The replicate distribution approximates sampling variation of the mean difference in the prompt population. A paired design cannot be used when the models have different prompt sets.

## Common misconceptions

### Misconception 1. A 95% confidence interval contains the parameter with 95% probability

In the frequentist framework, the parameter is fixed and the observed interval is fixed too. The 95% is the interval-generating procedure's repeated-sampling coverage.

### Misconception 2. A wide confidence interval means there is no effect

A wide interval means large sampling uncertainty in the estimate. Information about whether the effect is 0 or where its magnitude lies is limited; examine sample size and variability.

### Misconception 3. Bootstrap generates new population data

Bootstrap resamples the observed sample's empirical distribution. It does not introduce groups or rare patterns absent from the original sample.

### Misconception 4. Bootstrap just requires resampling rows

If independent sampling units differ from rows, row bootstrap breaks dependence. Preserve paired observations, clusters, and time blocks.

### Misconception 5. More bootstrap replicates remove small-sample problems

Increasing $B$ reduces resampling Monte Carlo error. The empirical distribution's coarse population approximation and sampling bias remain.

## Exercises

### 1. Interpret confidence

A 95% confidence interval $[0.4,0.6]$ was obtained. Give an accurate interpretation using repeated-sampling coverage.

<details>
<summary>Show solution</summary>

Repeating sampling and the same interval procedure under the same population and sampling design produces intervals of which about 95% contain the fixed target parameter. Claiming 95% probability that the parameter lies in this particular observed interval is not the frequentist interpretation.

</details>

### 2. Calculate a z interval

Given $\bar x=20$, $\sigma=4$, $n=64$, and $z_{0.975}=1.96$, calculate a 95% confidence interval.

<details>
<summary>Show solution</summary>

Standard error is $4/\sqrt{64}=0.5$ and the margin is $1.96(0.5)=0.98$, giving

\[
[20-0.98,20+0.98]=[19.02,20.98].
\]

</details>

### 3. Confidence level and width

Explain how interval width changes when confidence level increases from 95% to 99%, with estimate and standard error unchanged.

<details>
<summary>Show solution</summary>

The 99% interval uses a larger critical value and is wider. Achieving higher repeated-sampling coverage uses a procedure including more parameter values.

</details>

### 4. Calculate a t interval

Given $\bar x=12$, $s=2$, $n=25$, and $t_{24,0.975}=2.064$, calculate a 95% t interval.

<details>
<summary>Show solution</summary>

Estimated standard error is

\[
\frac2{\sqrt{25}}=0.4
\]

and the margin is $2.064(0.4)=0.8256$. The interval is

\[
[12-0.8256,12+0.8256]
=[11.1744,12.8256]
\]

</details>

### 5. A bootstrap resample

Give two examples of size-3 bootstrap samples from $(a,b,c)$. Explain why an observation can be absent or repeated.

<details>
<summary>Show solution</summary>

Examples are $(a,a,c)$ and $(b,c,b)$. Each position samples from $a,b,c$ with replacement, so an already selected value can be selected again. Some observations repeat while others can be absent from one resample.

</details>

### 6. Choose the resampling unit

Models A and B were evaluated on the same 50 prompts. Explain the unit and procedure for a bootstrap interval of their mean score difference.

<details>
<summary>Show solution</summary>

Sample 50 prompt indices with replacement and take both A and B scores for each selected prompt. Calculate the mean paired difference in each resample. Separately resampling scores loses paired correlation from prompt difficulty.

</details>

### 7. Critique a model-interpretability claim

Iid bootstrap of token rows from one dataset produces a very narrow interval for mean attribution. Evaluate “mean attribution is in the same range for all prompts and models.”

<details>
<summary>Show solution</summary>

If tokens are clustered within prompts, row bootstrap can ignore dependence and make the interval too narrow. An interval from one dataset and model does not include other prompt distributions or model variation. Resample prompts or documents as clusters; generalization across model seeds also requires repetitions at the model-run level.

</details>

## Lesson summary

- A confidence interval is a random-interval procedure with specified repeated-sampling coverage.
- A normal-form interval adds and subtracts critical value times estimated standard error from the estimate.
- For a Gaussian mean, use a z interval with known population variance and a t interval when population variance is estimated.
- Nonparametric bootstrap draws samples of size $n$ with replacement from the empirical distribution.
- Replicate standard deviations and quantiles give bootstrap standard error and percentile intervals.
- Paired and clustered data require resampling units preserving dependence structure.
- Bootstrap does not remove sampling bias, missing groups, or distribution shift.

## Pass criteria

You pass if you can answer these questions without consulting the material.

- Can you explain confidence level as coverage?
- Can you calculate an interval from an estimate, standard error, and critical value?
- Can you distinguish the conditions for z and t intervals?
- Can you construct a bootstrap resample and replicate?
- Can you explain bootstrap standard error and percentile intervals?
- Can you choose resampling units for paired and clustered data?
- Can you explain what a narrow interval does not guarantee?

## Next lesson

- [M04-10 Hypothesis testing and multiple comparisons](M04-10-hypothesis-testing-multiple-comparisons.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Confidence level is defined as repeated-sampling coverage.
- [x] Formulas and conditions for z and t intervals are distinguished.
- [x] Bootstrap procedures and standard error are explained.
- [x] Percentile intervals and their limitations are stated.
- [x] Paired and clustered resampling are explained.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretability claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] No prerequisites outside the stated scope are required implicitly.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
