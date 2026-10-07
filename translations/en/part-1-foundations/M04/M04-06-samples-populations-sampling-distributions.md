---
id: "M04-06"
title: "Samples, populations, and sampling distributions"
part: 1
stage: "M04"
status: "complete"
prerequisites:
  - "M04-04"
  - "M04-05"
estimated_time: "145~175 minutes"
---

# M04-06. Samples, populations, and sampling distributions

## Why this lesson matters

Researchers calculate mean loss, probe accuracy, or mean attribution from a dataset. These numbers summarize the observed sample. Research questions often concern performance on a broader population of inputs or across repeated experiments. Distinguishing numbers calculated from a sample from values in the target population makes it possible to describe observation error and the scope of generalization.

Drawing another sample from the same population changes quantities such as sample mean and accuracy. A sampling distribution describes this variation in a statistic. Standard errors, confidence intervals, and hypothesis tests use sampling distributions.

## Learning objectives

After completing this lesson, you should be able to:

- Distinguish the target population, a random sample, and an observed sample.
- Explain independence and identical distribution as separate parts of the iid assumption.
- Explain the difference between a statistic and a parameter with examples.
- Calculate a sample mean, sample variance, and empirical distribution.
- Distinguish a sampling distribution from the distribution of raw observations.
- Calculate the expectation, variance, and standard error of an iid sample mean.
- Assess how dependence between experimental units affects uncertainty evaluation.

## Prerequisite check

- Prerequisite: [M04-04 Expectation, variance, and covariance](M04-04-expectation-variance-covariance.md)
- Prerequisite: [M04-05 Common distributions](M04-05-common-distributions.md)
- Check: Can you calculate the mean and variance of a random variable?
- Check: Can you explain the supports and parameters of Bernoulli and Gaussian distributions?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Scope |
|---|---|---|---|
| $P$ | `P` | The probability distribution of the population about which we seek to infer | Target population |
| $X_1,\ldots,X_n$ | `X one through X n` | Random variables before the sample is drawn | Usually $X_i\sim P$ |
| $x_1,\ldots,x_n$ | `x one through x n` | Values obtained in one draw | Fixed data |
| $\theta$ | `theta` | A fixed but unknown property of the population distribution | Examples: $\mu$, $\sigma^2$ |
| $T=t(X_1,\ldots,X_n)$ | `T equals t of X one through X n` | A function of a random sample | A random variable |
| $t=t(x_1,\ldots,x_n)$ | `t equals t of x one through x n` | A number calculated from the observed sample | A fixed value |
| $\bar X$ | `X bar` | The sample mean statistic | $n^{-1}\sum_iX_i$ |
| $s^2$ | `s squared` | The variance calculated from the observed sample | $(n-1)^{-1}\sum_i(x_i-\bar x)^2$ |
| $\operatorname{SE}(T)$ | `the standard error of T` | The standard deviation of a statistic's sampling distribution | The same units as the statistic |

## Core concept 1. The population is the inferential target; a sample is an observed subset

A population is the set of all outcomes targeted by the research question, or the probability distribution generating those outcomes. It can be defined as a finite list of data or as a distribution $P$ that includes future inputs.

A sample consists of $n$ values observed from a population. Before sampling, write

\[
X_1,\ldots,X_n
\]

as random variables. After observation, write

\[
x_1,\ldots,x_n
\]

as fixed values. Researchers use the sample to estimate population properties. A vague target population such as “the evaluation data” leaves unclear which inputs and conditions the results generalize to.

The following process shows the distinction between holding the population fixed and drawing a new sample.

<figure class="lesson-figure" markdown="1">

![A fixed Bernoulli population parameter generating a random sample and one illustrative fixed observation with its statistic](../../figures/assets/M04/M04-06-sample-statistic-roles.svg)

<figcaption>Distinguish a statistic before sampling from its observed value. A sample mean that happens to equal the parameter in one sample does not mean that means from other samples will equal it too.</figcaption>
</figure>

## Core concept 2. iid assumes both independence and identical distribution

For an independent and identically distributed (iid) random sample, write

\[
X_1,\ldots,X_n\overset{\mathrm{iid}}{\sim}P
\]

Identically distributed means that each $X_i$ follows the same population distribution $P$. Independent means that knowing one observation does not change the distribution of another.

Independence is a condition on the entire sample's joint distribution. For a discrete iid sample, the probability of one list of values factors as $p(x_1)\cdots p(x_n)$, with every factor using the same PMF $p$. Having the same marginal distribution for each $X_i$ alone does not imply this product. Independence of several observations also requires checking their full joint relationship, not only pairwise relationships.

Sharing a source does not establish independence. Tokens in one document, repeated inputs from one user, and checkpoints from the same training run can be dependent within their groups. Before applying sampling distribution formulas, identify the independent unit in the research design.

Two observations with the same marginal distributions can have different joint probabilities. On the right below, the second observation copies the first.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Independent and copied Bernoulli observations with the same half-half marginals but quarter masses everywhere versus half masses only on the diagonal](../../figures/assets/M04/M04-06-iid-versus-copy.svg)

<figcaption>All four sample combinations are possible on the left, but unequal values cannot occur on the right. Their sample means also have different variances, showing that equal marginals alone do not justify an iid standard error.</figcaption>
</figure>

## Core concept 3. Parameters and statistics have different fixed and random roles

A parameter $\theta$ is a property of a population distribution. In frequentist notation, $\theta$ is fixed but unknown. For example,

\[
\mu=\mathbb E_P[X],
\qquad
\sigma^2=\operatorname{Var}_P(X)
\]

are population parameters.

A statistic $T=t(X_1,\ldots,X_n)$ is a function of the sample that does not directly take unknown parameters as inputs. Before sampling, $T$ is a random variable. Substituting observed values gives the single number $t=t(x_1,\ldots,x_n)$. The sample mean $\bar X$ is a statistic estimating the population mean $\mu$.

## Core concept 4. Sample means, sample variances, and empirical distributions summarize data differently

The sample mean is

\[
\bar X=\frac1n\sum_{i=1}^{n}X_i
\]

and its observed value is

\[
\bar x=\frac1n\sum_{i=1}^{n}x_i
\]

For $n\ge2$, sample variance is usually calculated as

\[
s^2=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar x)^2
\]

The denominator $n-1$ reflects the loss of one degree of freedom from estimating the mean in the same sample. M04-07 explains this choice and unbiasedness.

The deviations from the mean satisfy $\sum_i(x_i-\bar x)=0$. Specifying the first $n-1$ deviations determines the last as the negative of their sum, so all $n$ deviations cannot be chosen freely. This constraint explains the one degree of freedom. The next lesson uses expectation to show why this denominator gives an unbiased estimator of population variance.

The empirical distribution assigns mass $1/n$ to each observation. Its probability for an event $A$ is

\[
\widehat P_n(A)
=\frac1n\sum_{i=1}^{n}\mathbf 1\{x_i\in A\}
\]

Sample mean summarizes location; sample variance summarizes spread. The empirical distribution retains more of the shape of the observed values' distribution.

If a value occurs more than once, its masses add once per occurrence. For example, two observations both equal to 4 each add $1/n$ at value 4. The empirical distribution has expectation $\bar x$ and variance $n^{-1}\sum_i(x_i-\bar x)^2$. Its denominator therefore differs from the $s^2$ above, which is used to estimate population variance. Distinguish the empirical distribution's role in summarizing current data from the role of $s^2$ in estimating a population parameter.

In the observations 2, 4, 4, 6, the value 4 is recorded twice, so its empirical probability combines two masses.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Four observed records two four four six merging quarter masses at repeated values and using different denominators for empirical and sample variance](../../figures/assets/M04/M04-06-empirical-duplicate-mass.svg)

<figcaption>Every record has the same mass, but records with equal values combine at one position. Even with the same squared-deviation sum, the variance of the current empirical distribution and the sample variance estimating population variance use different denominators.</figcaption>
</figure>

## Core concept 5. A sampling distribution is the distribution of the statistic itself

Consider repeatedly drawing samples of size $n$ from the same population. The statistic $T$ calculated in each sample varies. The probability distribution of $T$ under this repeated sampling is its sampling distribution.

Distinguish three distributions:

- Population distribution: the distribution of one observation $X$.
- Empirical distribution: the distribution formed by the current observed sample.
- Sampling distribution: the distribution of a function $T$ of the entire sample.

The term sampling distribution can be mistaken for “a histogram of the observed sample values.” Here it means the statistic's repeated-sampling distribution.

Plotting the population in Example 1, one observed sample (0, 1), and the means of all possible size-2 samples assigns probability to different objects.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Population and one observed empirical Bernoulli PMF supported at zero and one, compared with the exact size-two sample-mean PMF also supported at one half](../../figures/assets/M04/M04-06-three-distributions.svg)

<figcaption>The first two panels happen to have the same bar heights for this sample, but their roles differ. The third assigns probabilities to means calculated under repeated sampling, rather than to individual observations.</figcaption>
</figure>

## Core concept 6. Variation in an iid sample mean decreases with sample size

If $X_1,\ldots,X_n$ form an iid sample with mean $\mu$ and variance $\sigma^2$, linearity of expectation gives

\[
\mathbb E[\bar X]
=\frac1n\sum_{i=1}^{n}\mathbb E[X_i]
=\mu
\]

Independence makes the covariance terms 0, so

\[
\operatorname{Var}(\bar X)
=\operatorname{Var}\left(\frac1n\sum_{i=1}^{n}X_i\right)
=\frac{1}{n^2}\sum_{i=1}^{n}\sigma^2
=\frac{\sigma^2}{n}
\]

Hence the standard error of the sample mean is

\[
\operatorname{SE}(\bar X)
=\sqrt{\operatorname{Var}(\bar X)}
=\frac{\sigma}{\sqrt n}
\]

Quadrupling sample size halves this standard error. If observations are positively correlated, covariance terms remain and variation can exceed the iid formula.

Here $\sigma$ is the spread of one observation, whereas $\sigma/\sqrt n$ is the spread of the mean calculated from a sample of size $n$. Drawing more observations from the same population does not change the raw data's $\sigma$. Averaging independent deviations reduces variation in the mean statistic.

Expanding the square without assuming independence gives, in general,

\[
\operatorname{Var}(\bar X)
=\frac{1}{n^2}\left(
\sum_{i=1}^{n}\operatorname{Var}(X_i)
+2\sum_{1\le i<j\le n}\operatorname{Cov}(X_i,X_j)
\right)
\]

Each product of two distinct deviations appears twice in the expansion, giving the factor 2 in the covariance sum. If the same random variable is copied to give $X_1=\cdots=X_n$, then $\bar X=X_1$ and its variance remains $\sigma^2$. Increasing only the list length to $n$ does not justify the $\sigma^2/n$ formula.

For a Gaussian population, the mean's distribution is also exactly Gaussian. This makes it possible to compare its narrowing directly while holding the raw data variance fixed.

<figure class="lesson-figure" markdown="1">

![Exact Gaussian sample-mean densities from an unchanged standard normal population for sample sizes one four and sixteen with standard errors one one half and one quarter](../../figures/assets/M04/M04-06-mean-spread.svg)

<figcaption>Each quadrupling of sample size halves the mean's standard error. One raw observation still follows N(0, 1); the distribution that narrows is the mean statistic's distribution.</figcaption>
</figure>

## Core concept 7. The central limit theorem gives an approximate distribution for the sample mean

For an iid sample with mean $\mu$ and variance $0<\sigma^2<\infty$, as sample size $n$ increases, the distribution of

\[
\frac{\bar X-\mu}{\sigma/\sqrt n}
\]

approaches the standard normal distribution. This is the central limit theorem (CLT). The original population distribution need not be Gaussian.

The numerator is the sample mean's deviation from the population mean; the denominator is that sample mean's standard error. By the preceding expectation and variance formulas, this ratio has mean 0 and variance 1 for each $n$. The CLT describes more than those two moments: it describes the shape of the standardized statistic's distribution as $n$ grows. It does not turn the raw observations $X_i$ into Gaussian variables. A small-sample mean can take only a few discrete values, as in Example 1.

Approximation quality depends on sample size and the original distribution's skewness and tails. Gaussian approximation can be inaccurate for small $n$ or heavy-tailed data. The iid CLT cannot be applied unchanged to dependent samples.

A Bernoulli sample mean still takes only discrete values at finite sample sizes, but the arrangement of mass at standardized values changes with sample size.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Exact standardized Bernoulli mean masses at sample sizes two eight and thirty-two compared with standard-normal probabilities over intervals centered on each discrete value](../../figures/assets/M04/M04-06-clt-discrete-means.svg)

<figcaption>Blue bars are exact discrete probabilities. Orange points are standard normal probabilities assigned to intervals centered at the same values and as wide as the spacing between neighboring values; they are not normal point probabilities. The comparison illustrates approximation shape without declaring any sample size universally sufficient.</figcaption>
</figure>

## Core concept 8. Experimental units determine sampling uncertainty

Even when a model interpretability experiment observes 10,000 tokens, tokens grouped within 20 prompts require checking whether there are truly 10,000 independent units. Tokens in the same prompt share context and model state. Treating tokens as independent samples can underestimate standard error.

The sampling unit depends on whether generalization targets model seeds, prompts, subjects, or documents. Report both the number of observations and the independent experimental units when reporting sample size.

Showing which shared contexts contain the observation records helps distinguish record count from independent units.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two illustrative independently sampled prompt contexts each containing three token records, separating six observed records from two prompt-level units](../../figures/assets/M04/M04-06-prompt-clusters.svg)

<figcaption>Six recorded tokens still come from only two prompt contexts. This illustrates a design that samples prompts; it does not separately guarantee token-level independence or generalization to other models.</figcaption>
</figure>

## Example 1. Sampling distribution of a Bernoulli sample mean

### Problem

Let $X_1,X_2\overset{\mathrm{iid}}{\sim}\operatorname{Bernoulli}(0.5)$ and

\[
\bar X=\frac{X_1+X_2}{2}
\]

Find the sampling distribution of $\bar X$.

### Solution

The possible samples and sample means are:

| $(X_1,X_2)$ | Probability | $\bar X$ |
|---|---:|---:|
| $(0,0)$ | $1/4$ | 0 |
| $(0,1)$ | $1/4$ | $1/2$ |
| $(1,0)$ | $1/4$ | $1/2$ |
| $(1,1)$ | $1/4$ | 1 |

Therefore,

\[
P(\bar X=0)=\frac14,
\quad
P\left(\bar X=\frac12\right)=\frac12,
\quad
P(\bar X=1)=\frac14.
\]

This distribution has mean $1/2$ and variance

\[
\frac{p(1-p)}{n}
=\frac{(1/2)(1/2)}{2}
=\frac18
\]

### Meaning of the result

The raw observations $X_i$ take 0 or 1. The sample mean takes $0,1/2,1$. The sampling distribution above assigns probabilities to this sample mean.

## Example 2. Mean and variance of an observed sample

For observations $2,4,6$,

\[
\bar x=\frac{2+4+6}{3}=4
\]

The sample variance is

\[
s^2
=\frac{(2-4)^2+(4-4)^2+(6-4)^2}{3-1}
=\frac{8}{2}
=4
\]

These numbers are statistics of the observed sample, not the population mean and variance themselves.

## Example 3. Standard error of accuracy

Suppose the correctness indicators for individual samples are iid Bernoulli with success probability $p=0.7$, and $n=100$. The standard error of accuracy $\bar X$ is

\[
\operatorname{SE}(\bar X)
=\sqrt{\frac{p(1-p)}{n}}
=\sqrt{\frac{0.7\cdot0.3}{100}}
\approx0.0458
\]

This is the scale on which observed accuracy varies around population accuracy under repeated sampling. In practice, the unknown $p$ can be estimated by the observed proportion.

## Example 4. The problem with counting grouped tokens as independent

Suppose attribution is calculated for 100 tokens in each of 10 prompts. Using $n=1000$ as the iid sample size ignores the shared context within a prompt. Analyzing prompt means or resampling while retaining clusters can reflect prompt-level variation. The appropriate method depends on whether generalization targets tokens or prompts.

## Common misconceptions

### Misconception 1. A population is a finite list larger than the dataset

A population can be a finite list or a probability distribution generating future inputs. Researchers must specify the target of generalization.

### Misconception 2. After observing one sample, the sample mean is no longer a random variable

The observed $\bar x$ is fixed. The sample mean statistic $\bar X$ remains a random variable with a sampling distribution when other possible samples are considered.

### Misconception 3. Raw data must be Gaussian to analyze a sample mean

Under iid sampling and finite variance, the expectation and variance formulas for a sample mean do not require a Gaussian population. The CLT's Gaussian approximation requires conditions and assessment of approximation quality.

### Misconception 4. Many observations imply a large independent sample size

Observations within one prompt, subject, or run can be dependent. Miscounting independent units can make standard errors and test results look overly optimistic.

### Misconception 5. Large sample size eliminates sampling bias

A large sample reduces random variation under the same sampling mechanism. If that mechanism omits a group or uses selection criteria unlike the target population, increasing sample size can leave the bias intact.

## Exercises

### 1. Distinguish the objects

Classify $X_1,\ldots,X_n$, $x_1,\ldots,x_n$, $\mu$, and $\bar X$ as a random sample, observed sample, parameter, or statistic.

<details>
<summary>Show solution</summary>

$X_1,\ldots,X_n$ form the random sample before drawing it, and $x_1,\ldots,x_n$ are the fixed observed values. The population mean $\mu$ is a parameter, and $\bar X$ is a statistic that is a function of the random sample.

</details>

### 2. Calculate sample statistics

The observed sample is $1,3,5,7$. Calculate $\bar x$ and $s^2$ using denominator $n-1$.

<details>
<summary>Show solution</summary>

\[
\bar x=\frac{1+3+5+7}{4}=4.
\]

The squared-deviation sum is $9+1+1+9=20$, so

\[
s^2=\frac{20}{4-1}=\frac{20}{3}.
\]

</details>

### 3. Mean and variance of the sample mean

An iid sample has population mean $10$ and variance $9$, with $n=36$. Calculate $\mathbb E[\bar X]$, $\operatorname{Var}(\bar X)$, and $\operatorname{SE}(\bar X)$.

<details>
<summary>Show solution</summary>

\[
\mathbb E[\bar X]=10,
\qquad
\operatorname{Var}(\bar X)=\frac9{36}=\frac14,
\]

\[
\operatorname{SE}(\bar X)=\sqrt{\frac14}=\frac12.
\]

</details>

### 4. Enumerate a sampling distribution

Let $X_1,X_2\overset{\mathrm{iid}}{\sim}\operatorname{Bernoulli}(0.25)$. Find the possible values of $\bar X$ and their probabilities.

<details>
<summary>Show solution</summary>

The possible values of $\bar X$ are $0,1/2,1$.

\[
P(\bar X=0)=(0.75)^2=0.5625,
\]

\[
P\left(\bar X=\frac12\right)
=2(0.25)(0.75)=0.375,
\]

\[
P(\bar X=1)=(0.25)^2=0.0625.
\]

The three probabilities sum to 1.

</details>

### 5. Sample size and standard error

The population standard deviation is $12$. Find the smallest iid sample size that makes the sample mean's standard error at most 3.

<details>
<summary>Show solution</summary>

We require

\[
\frac{12}{\sqrt n}\le3
\]

Thus $\sqrt n\ge4$ and $n\ge16$. The minimum is 16.

</details>

### 6. Check the iid assumption

An analysis treats 50,000 patches cut from 500 medical images of one patient as independent samples. Explain possible dependence and how the uncertainty assessment should change.

<details>
<summary>Show solution</summary>

Patches from the same patient share anatomical characteristics, imaging equipment, and preprocessing, and can be strongly dependent. Only one patient was observed, so there are not 50,000 independent units for inference about a patient population. Evaluating generalization across patients requires sampling multiple patients, splitting at the patient level, and using cluster-aware analysis.

</details>

### 7. Evaluate a model interpretability claim

Mean attribution was positive for one model on 20 prompts. Evaluate the conclusion, “Attribution is positive for other models and all prompts too,” and propose a sampling unit.

<details>
<summary>Show solution</summary>

The observation is a sample mean calculated for that model and those 20 prompts. Generalization to other models and a prompt population requires sampling model seeds or checkpoints and prompts. Treat prompts as basic clusters rather than treating their tokens as independent units. If the question includes variation between models, model runs can also be designed as independent units.

</details>

## Lesson summary

- The population is the target of generalization; the sample is an observed subset of that target.
- iid includes both independence of observations and a common population distribution.
- A parameter is a population property; a statistic is a function of a random sample.
- A sampling distribution is the distribution of a statistic under repeated sampling.
- An iid sample mean has mean $\mu$, variance $\sigma^2/n$, and standard error $\sigma/\sqrt n$.
- Under its conditions, the CLT supplies a Gaussian approximation for the standardized sample mean's distribution.
- Counting dependent observations as independent can underestimate sampling uncertainty.

## Pass criteria

You pass if you can answer the following without consulting the material.

- Can you distinguish populations, random samples, and observed samples?
- Can you explain the two iid conditions separately?
- Can you distinguish parameters from statistics using examples?
- Can you calculate sample means and sample variances?
- Can you distinguish population, empirical, and sampling distributions?
- Can you calculate the expectation, variance, and standard error of a sample mean?
- Can you propose an independent sampling unit for a model interpretability experiment?

## Next lesson

- [M04-07 Estimation, bias, and variance](M04-07-estimation-bias-variance.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Populations, random samples, and observed samples are distinguished.
- [x] Independence and identical distribution in iid are explained.
- [x] The fixed and random roles of parameters and statistics are distinguished.
- [x] Sample means, sample variances, and empirical distributions are defined.
- [x] Sampling distributions and standard errors are calculated.
- [x] Experimental units and limitations from dependence are stated.
- [x] Every exercise has a solution.
- [x] Strengths of model interpretability claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
