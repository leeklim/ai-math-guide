---
id: "M04-11"
title: "Likelihood and maximum likelihood estimation"
part: 1
stage: "M04"
status: "complete"
prerequisites:
  - "M01-07"
  - "M04-02"
  - "M04-05"
  - "M04-07"
estimated_time: "150~180 minutes"
---

# M04-11. Likelihood and maximum likelihood estimation

## Why this lesson matters

A probability model $p_\theta(x)$ specifies the probability or density of data given a parameter $\theta$. After observing data, read the same expression as a function of $\theta$ to compare which parameters explain the observations well. This function is the likelihood.

Maximum likelihood estimation chooses parameters that maximize the likelihood of the observed data. Negative log-likelihood in classification, squared error in regression, and token loss in language models connect through this principle. Distinguishing what is held fixed in probability and likelihood is necessary for reading the direction of conditioning correctly.

## Learning objectives

After completing this lesson, you should be able to:

- Distinguish the objects held fixed in a probability model and a likelihood.
- Write an iid sample likelihood as a product and its log-likelihood as a sum.
- Derive the maximum likelihood estimator of a Bernoulli parameter.
- Calculate Gaussian mean and variance MLEs.
- Turn negative log-likelihood into an optimization loss.
- Explain the connections of Gaussian NLL to squared error and categorical NLL to cross entropy.
- Limit identifiability and generalization claims that MLE does not guarantee.

## Prerequisite check

- Prerequisite: [M01-07 Derivatives of exponential and logarithmic functions](../M01/M01-07-exponential-log-derivatives.md)
- Prerequisite: [M04-02 Conditional probability and Bayes' rule](M04-02-conditional-probability-bayes-rule.md)
- Prerequisite: [M04-05 Common distributions](M04-05-common-distributions.md)
- Prerequisite: [M04-07 Estimation, bias, and variance](M04-07-estimation-bias-variance.md)
- Check: Can you convert a log of a product into a sum and differentiate logarithms?
- Check: Can you explain the parameters of Bernoulli and Gaussian PMFs and PDFs?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Fixed and varying objects |
|---|---|---|---|
| $p_\theta(x)$ | `p sub theta of x` | A probability model specified by $\theta$ | $\theta$ fixed, $x$ varying |
| $L(\theta;x)$ | `L of theta given x` | $p_\theta(x)$ read as a function of $\theta$ with observed $x$ fixed | $x$ fixed, $\theta$ varying |
| $\ell(\theta;x)$ | `ell of theta given x` | The natural logarithm of likelihood | $\log L(\theta;x)$ |
| $\widehat\theta_{\mathrm{MLE}}$ | `theta hat sub M L E` | A parameter maximizing likelihood | argmax |
| NLL | `N L L` | The negative of log-likelihood | A minimization loss |
| $\mathcal D$ | `calligraphic D` | The observed sample | $\{x_1,\ldots,x_n\}$ |

## Core concept 1. Likelihood reads the same expression as a function of the parameter

A probability model holds parameter $\theta$ fixed and assigns probabilities or densities to possible data $x$:

\[
x\longmapsto p_\theta(x).
\]

After observing data $x$, define the likelihood function by

\[
L(\theta;x)=p_\theta(x)
\]

The numerical value is the same, but $\theta$ is now treated as the varying input.

In a discrete model, $p_\theta(x)$ is probability mass; in a continuous model, it is density. A continuous likelihood can exceed 1. Likelihood is not a probability distribution over $\theta$ and need not satisfy

\[
\int L(\theta;x)\,d\theta=1
\]

Even the same Bernoulli expression is read differently depending on the axis that varies.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Bernoulli masses at fixed p and likelihood over p for a fixed observed success](../../figures/assets/M04/M04-11-probability-likelihood.svg)
  <figcaption>The left holds p=0.75 fixed and shows probability mass for the two possible observations. The right holds observed x=1 fixed and shows L(p;1)=p. Its area along the p axis is 1/2, illustrating that likelihood need not be normalized in the parameter direction.</figcaption>
</figure>

## Core concept 2. An iid likelihood is a product of observation-level terms

If $X_1,\ldots,X_n\overset{\mathrm{iid}}{\sim}p_\theta$ and the observed values are $x_1,\ldots,x_n$, the joint likelihood is

\[
L(\theta;\mathcal D)
=\prod_{i=1}^{n}p_\theta(x_i)
\]

This product comes from assuming independence of observations with the model's $\theta$ fixed. Identical distribution means using the same $p_\theta$ for every observation. For time series or clustered data, the joint density must reflect the dependence structure.

Multiplying many small probabilities can cause floating-point underflow. Taking natural logarithms gives

\[
\ell(\theta;\mathcal D)
=\log L(\theta;\mathcal D)
=\sum_{i=1}^{n}\log p_\theta(x_i)
\]

Since logarithm is increasing, the same $\theta$ maximizes likelihood and log-likelihood.

For a candidate with positive factors, the log of the product can be written as a sum of termwise logs. A candidate assigning probability mass or density 0 to an observation has likelihood 0 and is assigned log-likelihood $-\infty$. If any candidate has positive likelihood, such a zero-likelihood candidate cannot maximize it. Continuous models compare density at an observation, not point probability: $P(X=x)=0$ does not make all their log-likelihoods $-\infty$.

Calculating each observation's probability first lets you follow the conversion from a log of a product into a sum.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Four Bernoulli observation probabilities multiplied into likelihood then summed after taking logs](../../figures/assets/M04/M04-11-product-log-terms.svg)
  <figcaption>With observations (1,0,1,1) and candidate p=0.75 fixed, the four factors multiply to 0.10546875. Their logarithms sum to about −2.24934, the log of the same likelihood. Multiplying observation-level terms uses the iid model assumption.</figcaption>
</figure>

## Core concept 3. A maximum likelihood estimator maximizes data fit

Maximum likelihood estimation (MLE) is defined by

\[
\widehat\theta_{\mathrm{MLE}}
\in\operatorname*{argmax}_{\theta}
L(\theta;\mathcal D)
\]

or

\[
\widehat\theta_{\mathrm{MLE}}
\in\operatorname*{argmax}_{\theta}
\ell(\theta;\mathcal D)
\]

There can be several MLEs if there are several maxima. Parameter symmetries or identifiability problems can give different $\theta$ the same likelihood.

To implement maximization as minimization, use negative log-likelihood:

\[
\mathcal L_{\mathrm{NLL}}(\theta)
=-\ell(\theta;\mathcal D)
=-\sum_{i=1}^{n}\log p_\theta(x_i).
\]

Mean NLL divides this expression by $n$. A positive constant scaling does not change the minimizer, but it affects the numerical loss and gradient scales.

The entire rule that takes observed data and selects a maximizer is an estimator; the parameter selected from the current data is an estimate. Finding a derivative of 0 identifies only a candidate maximum. The boundaries of the allowed parameter range, existence of a maximum, and likelihoods of other candidates must also be checked. If the maximum value can be approached but not attained in the allowed range, the argmax above can be empty.

The three objectives have different values and optimization directions but the same optimal parameter location.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Bernoulli likelihood and log likelihood share a maximum while negative log likelihood has its minimum at the same p](../../figures/assets/M04/M04-11-likelihood-log-nll.svg)
  <figcaption>For observations (1,0,1,1), the maxima of L and log L and the minimum of −log L all occur at p=0.75. The vertical axes show different objective values, so compare the horizontal locations of the optima rather than the curve heights directly.</figcaption>
</figure>

## Core concept 4. The Bernoulli MLE is the observed success proportion

Let $x_i\in\{0,1\}$ and $X_i\overset{\mathrm{iid}}{\sim}\operatorname{Bernoulli}(p)$. The likelihood is

\[
L(p;\mathcal D)
=\prod_{i=1}^{n}p^{x_i}(1-p)^{1-x_i}
=p^{\sum_i x_i}(1-p)^{n-\sum_i x_i}
\]

First perform this power and logarithm calculation for $0<p<1$. Let $k=\sum_i x_i$. The log-likelihood is

\[
\ell(p)=k\log p+(n-k)\log(1-p).
\]

For $0<k<n$, differentiation gives

\[
\frac{d\ell}{dp}
=\frac{k}{p}-\frac{n-k}{1-p}.
\]

Setting it to 0 gives

\[
k(1-p)=(n-k)p
\]

and hence

\[
\widehat p_{\mathrm{MLE}}=\frac{k}{n}=\bar x
\]

For $k=0$ or $k=n$, the maximum is at boundary $p=0$ or $p=1$.

Putting the derivative over a common denominator gives $(k-np)/(p(1-p))$. The denominator is positive, so log-likelihood increases for $p<k/n$ and decreases for $p>k/n$. This stationary point is therefore a maximum for $0<k<n$. For $k=0$, all observations are 0 and likelihood is $(1-p)^n$. For $k=n$, all are 1 and likelihood is $p^n$. Maximizing these two expressions directly gives the boundary solutions without evaluating $0^0$ or $0\log0$ literally.

When all observations agree, check the allowed interval's endpoints rather than an interior stationary point.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

  ![All failures and all successes produce Bernoulli likelihood maxima at opposite parameter boundaries](../../figures/assets/M04/M04-11-boundary-maxima.svg)

  <figcaption>Data consisting only of 0 have likelihood (1−p)⁴, and data consisting only of 1 have likelihood p⁴. Allowing p in [0,1] gives maxima at 0 and 1, respectively. If only the open interval 0&lt;p&lt;1 is allowed, the endpoint values can be approached but no parameter attains the maximum.</figcaption>
</figure>

## Core concept 5. Gaussian MLEs are the sample mean and variance with denominator $n$

Let $X_i\overset{\mathrm{iid}}{\sim}\mathcal N(\mu,\sigma^2)$ with $\sigma^2>0$. First consider a sample whose observations are not all equal. The log-likelihood, including constants, is

\[
\ell(\mu,\sigma^2)
=-\frac n2\log(2\pi)
-\frac n2\log\sigma^2
-\frac{1}{2\sigma^2}
\sum_{i=1}^{n}(x_i-\mu)^2.
\]

Maximizing over $\mu$ gives

\[
\widehat\mu_{\mathrm{MLE}}=\bar x
\]

and maximizing over $\sigma^2$ gives

\[
\widehat{\sigma^2}_{\mathrm{MLE}}
=\frac1n\sum_{i=1}^{n}(x_i-\bar x)^2
\]

This variance MLE has downward bias in finite samples. Its objective differs from that of the unbiased sample variance with denominator $n-1$. MLE comes from the likelihood-maximization criterion.

The partial derivative with respect to the mean is

\[
\frac{\partial\ell}{\partial\mu}
=\frac1{\sigma^2}\sum_i(x_i-\mu)
=\frac n{\sigma^2}(\bar x-\mu)
\]

It is positive for $\mu<\bar x$ and negative for $\mu>\bar x$, so $\bar x$ maximizes over the mean for any positive variance. Differentiating with respect to variance as the single variable $\sigma^2$ gives

\[
\frac{\partial\ell}{\partial(\sigma^2)}
=-\frac n{2\sigma^2}
+\frac{\sum_i(x_i-\mu)^2}{2(\sigma^2)^2}
\]

Substituting $\mu=\bar x$ and setting the numerator to 0 gives $n\sigma^2=\sum_i(x_i-\bar x)^2$. Log-likelihood increases below this positive solution and decreases above it. M04-07 showed that the same squared-deviation sum has expectation $(n-1)\sigma^2$, so the estimator with denominator $n$ has expectation $(n-1)\sigma^2/n$. This calculation explains both its downward bias and its difference from the unbiased estimator with denominator $n-1$.

If all observations are equal, squared deviations are 0 at $\mu=\bar x$. Decreasing $\sigma^2$ toward 0 then makes log-likelihood increase without bound, so no maximum exists over positive variances. A formula that gives 0 does not establish the existence of an MLE with variance 0 in the ordinary Gaussian PDF model.

Varying mean and variance together finds the combination that assigns the highest density to the data.

<figure class="lesson-figure" markdown="1">
  ![Gaussian log likelihood contours over mean and positive variance for observations one two three](../../figures/assets/M04/M04-11-gaussian-likelihood.svg)
  <figcaption>These are log-likelihood contours for observations (1,2,3). Values are equal along a contour, and the central maximum is (μ,σ²)=(2,2/3). The figure shows fit in parameter space, not a probability density for μ and σ².</figcaption>
</figure>

When observations are all equal, even the same model has a different answer to whether a maximum exists.

<figure class="lesson-figure" markdown="1">
  ![Coincident observations give increasing Gaussian log likelihood as positive variance approaches zero](../../figures/assets/M04/M04-11-no-positive-variance-maximum.svg)
  <figcaption>For observations (2,2,2) with μ=2, decreasing positive variance increases log-likelihood. The horizontal axis is logarithmic; the smallest displayed variance is not the optimum. There is no finite maximum in the range σ²&gt;0.</figcaption>
</figure>

## Core concept 6. Gaussian NLL connects to squared error

Suppose a regression model assumes

\[
Y\mid X=\mathbf x
\sim\mathcal N(f_\theta(\mathbf x),\sigma^2)
\]

with fixed $\sigma^2$. The NLL for one sample is

\[
-\log p_\theta(y\mid\mathbf x)
=\frac12\log(2\pi\sigma^2)
+\frac{(y-f_\theta(\mathbf x))^2}{2\sigma^2}.
\]

The first term and $1/(2\sigma^2)$ are independent of $\theta$, so minimizing NLL over $\theta$ has the same solutions as minimizing squared error.

If the model also predicts $\sigma^2_\theta(\mathbf x)$, both the log-variance term and the scaled squared-error term affect training. Increasing variance alone to allow a larger residual also increases the log-variance penalty.

Taking the logarithm and changing the sign turns the negative squared deviation in the Gaussian density's exponent into a positive squared-error term. The normalization factor $1/\sqrt{2\pi\sigma^2}$ gives $\tfrac12\log(2\pi\sigma^2)$. When every sample uses the same fixed positive variance, total NLL is also the squared-error sum times a positive constant plus a parameter-independent constant. Different fixed variances across samples give different squared-error weights; learned variance makes both terms parameter-dependent. The fixed-common-variance equivalence therefore cannot be carried over unchanged.

The terms participating in optimization differ for fixed and learned variance.

<figure class="lesson-figure" markdown="1">
  ![Squared error and Gaussian negative log likelihood with fixed variance minimize at the same predicted mean](../../figures/assets/M04/M04-11-fixed-variance-loss.svg)
  <figcaption>For target y=3 and common fixed variance σ²=2, NLL is a positively scaled and shifted squared-error curve. Both minima occur at predicted mean=3, but the minimum loss values themselves differ.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">
  ![Log normalization increases while scaled residual decreases as learned Gaussian variance grows](../../figures/assets/M04/M04-11-learned-variance-loss.svg)
  <figcaption>This example holds residual at 2 and varies only variance. Increasing variance decreases the squared-error term but increases log normalization; total NLL is minimized at σ²=4. When variance is learned too, decreasing the squared-error term alone cannot replace the full calculation.</figcaption>
</figure>

## Core concept 7. Categorical NLL uses the observed class's log-probability

For target class $y$ in one sample and model categorical probabilities $p_\theta(k\mid\mathbf x)$, NLL is

\[
\mathcal L_{\mathrm{NLL}}
=-\log p_\theta(y\mid\mathbf x)
\]

With one-hot target $q_k=\mathbf 1\{k=y\}$,

\[
-\sum_{k=1}^{K}q_k\log p_\theta(k\mid\mathbf x)
=-\log p_\theta(y\mid\mathbf x)
\]

This is categorical cross entropy for a one-hot target. M04-12 extends it to general target distributions.

Language models calculate the same NLL for the observed next token at each position, then sum or average over positions and batches.

The 0 entries in the one-hot target remove unobserved classes' log terms from this sample's sum.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![One hot target selects only the observed class contribution to categorical negative log likelihood](../../figures/assets/M04/M04-11-observed-class-nll.svg)
  <figcaption>For observed class 2 and p=(0.1,0.8,0.1), the target is q=(0,1,0). Among the classwise −qₖ log pₖ terms on the right, only the second contributes, at about 0.223. Another sample selects its own observed class.</figcaption>
</figure>

## Core concept 8. MLE depends on model, sampling, and optimization assumptions

MLE maximizes training data likelihood within the chosen model family. If the true data distribution lies outside that family, MLE finds the best fit within a misspecified model. High training likelihood does not guarantee high likelihood on held-out data.

Nonidentifiable parameters can give several MLEs representing the same distribution. Local optima or optimization error can also make a computed parameter differ from a global MLE.

An objective with regularization differs from pure MLE. Interpreting a penalty as a prior's negative log-density can connect it to maximum a posteriori (MAP) estimation, but the prior-penalty correspondence must be explicit.

If several parameters represent the same distribution, the likelihood maximum need not specify one point.

<figure class="lesson-figure" markdown="1">
  ![Gaussian mean parameterized by a plus b produces a ridge of equally good likelihood maxima](../../figures/assets/M04/M04-11-identifiable-mean-ridge.svg)
  <figcaption>This Gaussian example parameterizes mean as μ=a+b and fixes variance at 1. For data (1,2,3), the entire green line a+b=2 has the same maximum likelihood. The different parameters (0,2), (1,1), and (2,0) represent the same fitted distribution.</figcaption>
</figure>

## Example 1. Calculate a Bernoulli likelihood

### Problem

The observed data are $(1,0,1,1)$. Write the Bernoulli likelihood and log-likelihood and find the MLE.

### Solution

The success count is $k=3$ and sample size is $n=4$.

\[
L(p)=p^3(1-p)
\]

and

\[
\ell(p)=3\log p+\log(1-p)
\]

The Bernoulli MLE formula gives

\[
\widehat p_{\mathrm{MLE}}
=\frac34=0.75.
\]

### Meaning of the result

The observed success proportion is the Bernoulli success probability maximizing likelihood. The MLE value varies across samples.

## Example 2. Compare two Bernoulli parameters

For the same data $(1,0,1,1)$,

\[
L(0.5)=(0.5)^4=0.0625
\]

and

\[
L(0.75)=(0.75)^3(0.25)=0.10546875
\]

Of these two candidates, $p=0.75$ gives higher likelihood.

## Example 3. Calculate Gaussian MLEs

For observations $(1,2,3)$,

\[
\widehat\mu_{\mathrm{MLE}}=2.
\]

The variance MLE is

\[
\widehat{\sigma^2}_{\mathrm{MLE}}
=\frac{(1-2)^2+(2-2)^2+(3-2)^2}{3}
=\frac23.
\]

The unbiased sample variance uses denominator 2 and equals 1. The two values come from different criteria.

## Example 4. Compare categorical NLLs

Suppose the true class is 2 and two models assign probabilities $0.8$ and $0.4$ to class 2. Their NLLs are

\[
-\log0.8\approx0.223,
\qquad
-\log0.4\approx0.916
\]

The first model, which assigns higher probability to the observed class, has lower NLL. Comparing the models overall also requires their other class probabilities and the full evaluation sample.

## Common misconceptions

### Misconception 1. Likelihood is the probability that a parameter is true

Likelihood evaluates parameters with data fixed and need not sum or integrate to 1 over parameters. Posterior probabilities require a prior and normalization.

### Misconception 2. Likelihood greater than 1 indicates an invalid model

A continuous likelihood is a density value and can exceed 1. Probabilities obtained by integrating over intervals must lie in $[0,1]$.

### Misconception 3. Maximizing log-likelihood gives a different estimator

Because logarithm is increasing, likelihood and log-likelihood have the same maximizers. Log scale converts products to sums and reduces numerical underflow.

### Misconception 4. MLEs are unbiased

MLE is defined by likelihood maximization. Some MLEs have finite-sample bias, including the Gaussian variance MLE.

### Misconception 5. The model with the smallest training NLL has found the true distribution

Training NLL measures fit within the chosen model family and observed training data. Held-out likelihood, distribution shift, and model misspecification require separate evaluation.

## Exercises

### 1. Probability and likelihood

Explain what is held fixed and what varies when reading $p_\theta(x)$ as a probability model versus reading it as $L(\theta;x)$.

<details>
<summary>Show solution</summary>

A probability model holds $\theta$ fixed and assigns probabilities or densities to possible $x$. Likelihood holds observed $x$ fixed, varies $\theta$, and compares the probability or density assigned to the observation.

</details>

### 2. An iid likelihood

The observed values are $(x_1,x_2,x_3)$, each with density $p_\theta(x_i)$. Write the iid likelihood and log-likelihood.

<details>
<summary>Show solution</summary>

\[
L(\theta;\mathcal D)
=p_\theta(x_1)p_\theta(x_2)p_\theta(x_3),
\]

\[
\ell(\theta;\mathcal D)
=\log p_\theta(x_1)+\log p_\theta(x_2)+\log p_\theta(x_3).
\]

</details>

### 3. A Bernoulli MLE

The observed Bernoulli data are $(0,1,0,1,1)$. Find the MLE of $p$.

<details>
<summary>Show solution</summary>

There are 3 successes in a sample of size 5, so

\[
\widehat p_{\mathrm{MLE}}=\frac35=0.6.
\]

</details>

### 4. Gaussian MLEs

The observations are $(2,4)$, and both Gaussian mean and variance are to be estimated. Find the two MLEs.

<details>
<summary>Show solution</summary>

The mean MLE is

\[
\widehat\mu=\frac{2+4}{2}=3.
\]

The variance MLE is

\[
\widehat{\sigma^2}
=\frac{(2-3)^2+(4-3)^2}{2}
=1.
\]

</details>

### 5. Categorical NLL

The true class is 3 and the predicted probabilities are $(0.2,0.3,0.5)$. Calculate the sample NLL.

<details>
<summary>Show solution</summary>

The probability assigned to observed class 3 is $0.5$, so

\[
\mathcal L_{\mathrm{NLL}}
=-\log0.5
\approx0.693.
\]

</details>

### 6. Gaussian NLL and squared error

A Gaussian regression model with fixed variance $\sigma^2=2$ has predicted mean 3 and target 5. Calculate the parameter-dependent NLL term.

<details>
<summary>Show solution</summary>

The parameter-dependent squared-error term is

\[
\frac{(5-3)^2}{2\sigma^2}
=\frac4{4}
=1.
\]

The term $\frac12\log(2\pi\sigma^2)$ is constant with respect to the predicted-mean parameter.

</details>

### 7. Evaluate a model claim

A neural network achieves the highest likelihood on training data. Evaluate the conclusion, “This model recovered the true data-generating distribution and its internal mechanism.”

<details>
<summary>Show solution</summary>

High training likelihood means that, within the chosen model family, the model assigns high probability or density to observed training data. Assessing fit to the actual distribution requires checking held-out generalization and model misspecification. Different parameterizations or mechanisms can produce the same input-output distribution, so likelihood alone cannot identify an internal mechanism.

</details>

## Lesson summary

- A probability model holds parameters fixed and varies data; likelihood holds observed data fixed and varies parameters.
- An iid sample likelihood is a product of observation-level probabilities or densities; log-likelihood is a sum of log terms.
- MLE is an estimator maximizing likelihood or log-likelihood.
- The Bernoulli MLE is the observed success proportion.
- The Gaussian mean MLE is the sample mean; the variance MLE averages squared deviations with denominator $n$.
- Gaussian fixed-variance NLL connects to squared error, and categorical NLL connects to one-hot cross entropy.
- MLE does not guarantee identifiability, model correctness, or held-out generalization.

## Pass criteria

You pass if you can answer the following without consulting the material.

- Can you distinguish the fixed objects in probability and likelihood?
- Can you write an iid likelihood and log-likelihood?
- Can you derive the Bernoulli MLE by differentiation?
- Can you calculate Gaussian mean and variance MLEs?
- Can you read NLL as a minimization loss?
- Can you connect Gaussian and categorical NLLs to common losses?
- Can you explain claims that training likelihood does not guarantee?

## Next lesson

- [M04-12 Entropy and cross entropy](M04-12-entropy-cross-entropy.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] The fixed objects in probability and likelihood are distinguished.
- [x] Iid likelihood and log-likelihood are explained.
- [x] Bernoulli and Gaussian MLEs are derived.
- [x] NLL is connected to optimization loss.
- [x] Categorical NLL is connected to cross entropy.
- [x] Every exercise has a solution.
- [x] Strengths of model interpretability claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
