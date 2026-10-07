---
id: "M04-05"
title: "Common distributions"
part: 1
stage: "M04"
status: "complete"
prerequisites:
  - "M00-05"
  - "M04-04"
estimated_time: "145~170 minutes"
---

# M04-05. Common distributions

## Why this lesson matters

A distribution family gives a name to a set of possible values and a probability rule. Bernoulli distributions are often used for binary labels, categorical distributions for a label selecting one of several classes, and Gaussian distributions for errors in continuous measurements. Choosing a distribution lets us calculate its support, parameters, mean, and variance using a common set of rules.

A neural network's sigmoid or softmax output can be read as parameters of a conditional distribution. A regression model that outputs a mean and variance can define a conditional Gaussian distribution. The choice of distribution expresses assumptions the model makes about data, so its support and dependence conditions must be checked.

## Learning objectives

After completing this lesson, you should be able to:

- Explain the supports and parameters of Bernoulli, categorical, binomial, and Gaussian distributions.
- Read each distribution's PMF or PDF and calculate probabilities in small examples.
- Calculate expectations and variances of Bernoulli and binomial distributions.
- Distinguish a categorical probability vector from a one-hot observation.
- Standardize a Gaussian distribution and read interval probability notation.
- Select a distribution family whose support matches the prediction target.
- Limit claims about data or representations justified by a distributional assumption.

## Prerequisite check

- Prerequisite: [M00-05 Exponents and logarithms](../M00/M00-05-exponents-logarithms.md)
- Prerequisite: [M04-04 Expectation, variance, and covariance](M04-04-expectation-variance-covariance.md)
- Check: Can you distinguish a PMF from a PDF and calculate probability by summation or integration?
- Check: Can you use the definitions of expectation and variance?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Support and conditions |
|---|---|---|---|
| $X\sim\operatorname{Bernoulli}(p)$ | `X follows a Bernoulli distribution with parameter p` | One binary trial | $X\in\{0,1\}$, $0\le p\le1$ |
| $Y\sim\operatorname{Categorical}(\boldsymbol\pi)$ | `Y follows a categorical distribution with parameter pi` | A distribution selecting one of $K$ categories | $Y\in\{1,\ldots,K\}$ |
| $S\sim\operatorname{Binomial}(n,p)$ | `S follows a binomial distribution with parameters n and p` | The number of successes in $n$ independent Bernoulli trials | $S\in\{0,\ldots,n\}$ |
| $X\sim\mathcal N(\mu,\sigma^2)$ | `X is normally distributed with mean mu and variance sigma squared` | A bell-shaped continuous distribution | $X\in\mathbb R$, $\sigma>0$ |
| $\boldsymbol\pi$ | `pi` | Categorical class probabilities | $\pi_k\ge0$, $\sum_k\pi_k=1$ |
| $\binom ns$ | `n choose s` | The number of ways to choose $s$ successful positions among $n$ positions | $0\le s\le n$ |

## Core concept 1. A Bernoulli distribution represents one binary outcome

If $X\sim\operatorname{Bernoulli}(p)$,

\[
P(X=1)=p,
\qquad
P(X=0)=1-p.
\]

The two cases can be written as a single expression:

\[
p_X(x)=p^x(1-p)^{1-x},
\qquad x\in\{0,1\}
\]

Substituting $x=1$ gives $p$, and substituting $x=0$ gives $1-p$.

This power expression combines the two cases for $0<p<1$. At the boundaries $p=0$ and $p=1$, use the original two probabilities $p,1-p$ rather than evaluating $0^0$. These distributions always produce 0 and always produce 1, respectively, and both have variance 0.

The expectation and variance are

\[
\mathbb E[X]=p,
\qquad
\operatorname{Var}(X)=p(1-p)
\]

Since $X^2=X$, we have $\mathbb E[X^2]=p$ and obtain $p-p^2=p(1-p)$. An event indicator is also a Bernoulli random variable.

Changing the success probability leaves the possible values at 0 and 1. It changes only the mass assigned to those two values.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three Bernoulli PMFs with success probabilities 0.1, 0.5 and 0.9, always supported only at zero and one](../../figures/assets/M04/M04-05-bernoulli-mass.svg)

<figcaption>The left and right bars always sum to 1. Probability mass shifts between the same two values; parameter p does not create a new observed value.</figcaption>
</figure>

Variance does not increase monotonically with the success probability. If either 0 or 1 is nearly certain, the observations have little spread.

<figure class="lesson-figure" markdown="1">

![Bernoulli variance p times one minus p peaking at 0.25 when p is 0.5 and becoming zero at both parameter endpoints](../../figures/assets/M04/M04-05-bernoulli-variance.svg)

<figcaption>At the curve's two endpoints, the distribution always produces the same value. At the center, both values have equal probability and the spread is largest. For p=0.7 in Example 1, variance is 0.21.</figcaption>
</figure>

## Core concept 2. A categorical distribution selects one of several categories

For $Y\sim\operatorname{Categorical}(\boldsymbol\pi)$ with $K$ classes,

\[
P(Y=k)=\pi_k,
\qquad
\pi_k\ge0,
\qquad
\sum_{k=1}^{K}\pi_k=1.
\]

An observation of $Y$ can be recorded as a class index $k$. Recorded as a one-hot vector $\mathbf Z\in\mathbb R^K$, it has 1 at the observed class and 0 elsewhere. In this representation,

\[
\mathbb E[\mathbf Z]=\boldsymbol\pi.
\]

The probability vector $\boldsymbol\pi$ and a one-hot observation $\mathbf z$ have different roles. The former assigns probabilities to all possible classes; the latter records the class obtained in one trial.

The $k$th one-hot component $Z_k$ is the indicator of the event $\{Y=k\}$. The indicator expectation from the preceding lesson gives $\mathbb E[Z_k]=P(Y=k)=\pi_k$. Collecting these componentwise equalities gives the mean vector above. Exactly one component of an observation must be 1, whereas several components of the mean vector can be positive. Those components describe the expected proportions of the classes.

Separating the probability vector in Example 2 from an observed class 2 shows the distinct roles of a distribution parameter and a recorded value.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Categorical class masses 0.5, 0.3 and 0.2 above one illustrative observed class-two draw recorded as the one-hot vector zero one zero](../../figures/assets/M04/M04-05-probability-one-hot.svg)

<figcaption>The upper bars show probabilities of all possibilities, whereas the lower vector records only the class observed in one trial. The expected proportion of each component connects to the probability vector when considering the mean of one-hot observations over multiple trials.</figcaption>
</figure>

## Core concept 3. A binomial distribution counts Bernoulli successes

Let $X_1,\ldots,X_n$ be independent Bernoulli random variables with the same success probability $p$, and let

\[
S=\sum_{i=1}^{n}X_i
\]

Then $S\sim\operatorname{Binomial}(n,p)$, with

\[
P(S=s)
=\binom ns p^s(1-p)^{n-s},
\qquad s=0,1,\ldots,n
\]

Here $p^s(1-p)^{n-s}$ is the probability of one particular arrangement of successes and failures, and $\binom ns$ counts the arrangements of successful positions.

Read this power calculation first for $0<p<1$. At the boundaries, assign probability 1 to $S=0$ when $p=0$ and to $S=n$ when $p=1$.

Independence makes an arrangement's probability the product of its trialwise success or failure probabilities. With a common $p$, all arrangements with $s$ successes have probability $p^s(1-p)^{n-s}$ regardless of the successful positions. Different arrangements are disjoint events, so add this same probability once for each arrangement.

For $s\ge1$, choosing $s$ successful positions in order gives $n(n-1)\cdots(n-s+1)$ possibilities. A given set of positions can be ordered in $s(s-1)\cdots1$ ways, so dividing gives

\[
\binom ns=\frac{n(n-1)\cdots(n-s+1)}{s(s-1)\cdots1}
\]

For $s=0$, exactly one arrangement chooses no successful positions, so $\binom n0=1$. In Example 3, two successful positions can be chosen in $3\cdot2$ ordered ways. Counting the two orderings of each pair as one gives $\binom32=3$.

Using linearity of expectation and independence gives

\[
\mathbb E[S]=np,
\qquad
\operatorname{Var}(S)=np(1-p)
\]

Without independence, the variance of the success count includes covariances between trials.

Since $\mathbb E[S]=\sum_i\mathbb E[X_i]=np$, the mean requires only the same success probability, not independence. Adding $n$ copies of $p(1-p)$ for the variance uses independence to eliminate covariances between different trials. Linearity of the mean alone does not give the full binomial distribution or the variance formula above.

In Example 3, specifying the two successful positions determines one arrangement. Listing the same two positions in a different order does not produce a new arrangement.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The three distinct success-position arrays 110, 101 and 011 for three independent equal-probability binary trials, each of mass one eighth and total mass three eighths](../../figures/assets/M04/M04-05-binomial-success-positions.svg)

<figcaption>Each row has a different pair of successful positions. Under the common success probability and independence assumptions, all three rows have the same probability. They are disjoint and their probabilities add.</figcaption>
</figure>

Recording the success count gives possible observations at the integers up to the number of trials. Even with the same five trials, changing the success probability changes the shape of the count distribution.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two binomial count PMFs for five independent trials with success parameters 0.2 and 0.5, supported on integer counts zero through five](../../figures/assets/M04/M04-05-binomial-mass.svg)

<figcaption>The horizontal axis records the count, not the order of successes. Small p concentrates mass at lower counts; p=0.5 places mass symmetrically around the middle counts of five trials.</figcaption>
</figure>

## Core concept 4. A Gaussian distribution uses mean and variance to set location and scale

The PDF of $X\sim\mathcal N(\mu,\sigma^2)$ is

\[
f_X(x)
=\frac{1}{\sqrt{2\pi\sigma^2}}
\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
\]

Parameter $\mu$ is the mean, and $\sigma^2$ is the variance:

\[
\mathbb E[X]=\mu,
\qquad
\operatorname{Var}(X)=\sigma^2.
\]

The density is symmetric about $\mu$ and spreads out as $\sigma$ increases. A Gaussian is a continuous distribution, so its point probability $P(X=x)$ is 0. Interval probabilities are calculated by integration.

In the exponent, the distance $x-\mu$ from the mean is divided by $\sigma$ and squared. At $x=\mu\pm\sigma$, one standard deviation from the mean, the exponent is $-1/2$ in both directions. Thus $\mu$ shifts the density's center, and $\sigma$ sets the distance unit for reaching the same relative position. As $\sigma$ increases, the leading coefficient $1/(\sqrt{2\pi}\sigma)$ decreases, widening the density while keeping its total area at 1.

Changing only the mean while holding variance fixed shifts the same curve horizontally.

<figure class="lesson-figure" markdown="1">

![Gaussian densities with means zero and two and common variance one, showing the same density shape translated horizontally](../../figures/assets/M04/M04-05-gaussian-mean-shift.svg)

<figcaption>The two curves have the same width and peak height. Changing the mean shifts only the location around which high probability density is concentrated.</figcaption>
</figure>

Changing the standard deviation while holding the mean fixed changes both width and peak height.

<figure class="lesson-figure" markdown="1">

![Centered normalized Gaussian densities with standard deviations 0.5, one and two and corresponding variances 0.25, one and four](../../figures/assets/M04/M04-05-gaussian-scale.svg)

<figcaption>Wider curves are lower and narrower curves are higher, keeping total area at 1. Distinguish the standard deviation in the legend from its square, the variance.</figcaption>
</figure>

## Core concept 5. Standardization transforms a Gaussian into a standard normal distribution

If $X\sim\mathcal N(\mu,\sigma^2)$ and $\sigma>0$, then

\[
Z=\frac{X-\mu}{\sigma}
\]

follows

\[
Z\sim\mathcal N(0,1)
\]

The z-score of an observation $x$,

\[
z=\frac{x-\mu}{\sigma}
\]

describes how many standard deviations $x$ lies from the mean. Standardization removes units; it does not make the original distribution Gaussian.

Linearity of expectation and the variance scaling rule give $\mathbb E[Z]=(\mu-\mu)/\sigma=0$ and $\operatorname{Var}(Z)=\sigma^2/\sigma^2=1$. These two calculations also apply to other distributions with a finite mean and positive variance. The standardized distribution is Gaussian because the original $X$ was Gaussian.

The same transformation can be checked in the density. Substituting $x=\mu+\sigma z$ makes the original interval width $\sigma$ times the standardized interval width. Multiplying the density by this width factor preserves the probability of corresponding intervals:

\[
f_Z(z)=\sigma f_X(\mu+\sigma z)
=\frac{1}{\sqrt{2\pi}}\exp\left(-\frac{z^2}{2}\right)
\]

The mean shift and positive scale disappear from the original Gaussian PDF, giving the standard normal PDF.

Since $\sigma>0$, transform intervals by the same rule without reversing the inequalities:

\[
P(a\le X\le b)
=P\left(\frac{a-\mu}{\sigma}\le Z\le\frac{b-\mu}{\sigma}\right).
\]

Subtracting the two endpoints' cumulative probabilities in the standard normal CDF $F_Z$ gives the original interval probability. Gaussian point probabilities are 0, so including or excluding an endpoint makes no difference here. The $z=1.5$ in Example 4 is a location to put into the CDF, not a probability itself.

Transforming the interval $[8,13]$ along with the distribution in Example 4 changes the units of the values but preserves the corresponding interval probability.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Gaussian density with mean ten and standard deviation two over interval eight to thirteen transformed into standard normal density over minus one to 1.5 with equal shaded probability area](../../figures/assets/M04/M04-05-gaussian-standardization.svg)

<figcaption>The lower horizontal axis records distance from the mean in standard deviations, rather than the original values. The interval width halves and the density height doubles, leaving the shaded probability area unchanged.</figcaption>
</figure>

## Core concept 6. A multivariate Gaussian uses a mean vector and covariance matrix

For a $d$-dimensional random vector $\mathbf X$, write

\[
\mathbf X\sim\mathcal N(\boldsymbol\mu,\mathbf\Sigma)
\]

where $\boldsymbol\mu\in\mathbb R^d$ is the mean vector and $\mathbf\Sigma\in\mathbb R^{d\times d}$ is the covariance matrix. When $\mathbf\Sigma$ is positive definite, the PDF is

\[
f_{\mathbf X}(\mathbf x)
=\frac{1}{(2\pi)^{d/2}|\mathbf\Sigma|^{1/2}}
\exp\left(
-\frac12(\mathbf x-\boldsymbol\mu)^\top
\mathbf\Sigma^{-1}
(\mathbf x-\boldsymbol\mu)
\right)
\]

Points with the same quadratic form value have the same density. Covariance sets the directions and scales of the equal-density surfaces.

Here $|\mathbf\Sigma|$ denotes the covariance matrix's determinant, which is positive under positive definiteness. This condition means that variance is positive in every nonzero direction and that the inverse exists. For $d=1$, $\mathbf\Sigma=[\sigma^2]$, so the determinant and inverse terms become $\sigma^2$ and $1/\sigma^2$, recovering the univariate PDF above.

In an orthogonal eigenbasis of covariance, let $\mathbf\Sigma=\mathbf Q\boldsymbol\Lambda\mathbf Q^\top$, with diagonal entries $\lambda_i>0$ in $\boldsymbol\Lambda$. In the centered coordinates $\mathbf z=\mathbf Q^\top(\mathbf x-\boldsymbol\mu)$, the exponent's quadratic form becomes

\[
(\mathbf x-\boldsymbol\mu)^\top\mathbf\Sigma^{-1}(\mathbf x-\boldsymbol\mu)
=\sum_{i=1}^{d}\frac{z_i^2}{\lambda_i}
\]

This sum divides distance in each eigendirection by its standard deviation $\sqrt{\lambda_i}$, squares the result, and adds the terms. Points with the same sum form an equal-density surface. Eigenvectors therefore set the surface's axis directions, and eigenvalues set its spread along each axis.

Specifying mean and covariance does not make an arbitrary distribution Gaussian. The two parameters determine the distribution only after adding the multivariate Gaussian assumption.

Covariance directions and scales can be read as equal-density ellipses only after assuming a Gaussian. Numbers on the curves below give the quadratic form values from the text.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Equal-density contours of a two-dimensional Gaussian centered at one and minus 0.5 with covariance one on the diagonal and 0.7 off-diagonal, and two covariance eigen-direction semiaxes](../../figures/assets/M04/M04-05-gaussian-covariance-contours.svg)

<figcaption>Along each numbered curve, the exponent is constant and so is the density. The two arrows are eigendirection semiaxes of the ellipse with value 4; each length is twice that direction's standard deviation. This is a property of the Gaussian model, not a conclusion about the shape of an arbitrary activation distribution.</figcaption>
</figure>

## Core concept 7. Selecting a distribution includes support and generative assumptions

A conditional Bernoulli distribution is natural for a binary label $Y\in\{0,1\}$, and a conditional categorical distribution for one of $K$ classes. A conditional Gaussian distribution can be used for real-valued regression targets, but it also assumes properties of error symmetry and tails.

Check a distribution family with the following questions.

- Does its set of possible values match the target's support?
- Does it require assumptions such as independence, equal success probabilities, or Gaussian errors?
- Does the model use fixed variance, or also predict input-dependent variance?
- Can the family represent extreme values and multiple modes?

A softmax vector can supply categorical parameters, and a sigmoid scalar can supply a Bernoulli parameter. The output form alone does not show that the distribution fits the data well.

## Example 1. Bernoulli mean and variance

### Problem

Let $X\sim\operatorname{Bernoulli}(0.7)$. Calculate the probabilities of the two possible values, the expectation, and the variance.

### Solution

\[
P(X=1)=0.7,
\qquad
P(X=0)=0.3.
\]

Thus,

\[
\mathbb E[X]=0.7
\]

and

\[
\operatorname{Var}(X)
=0.7(1-0.7)
=0.21
\]

### Meaning of the result

The mean of a 0-or-1 indicator equals its success probability. Variance decreases as $p$ approaches 0 or 1.

## Example 2. Probability of a categorical event

Let $Y\sim\operatorname{Categorical}(0.5,0.3,0.2)$. The probability that $Y$ is class 1 or class 3 is the sum of the probabilities of these mutually exclusive classes:

\[
P(Y\in\{1,3\})=0.5+0.2=0.7
\]

An observation of class 2 has one-hot vector $(0,1,0)^\top$.

## Example 3. Calculate a binomial probability

For $S\sim\operatorname{Binomial}(3,0.5)$, the probability of exactly two successes is

\[
P(S=2)
=\binom32(0.5)^2(0.5)^1
=3\cdot\frac18
=\frac38
\]

The three possible arrangements of successful positions are $110,101,011$.

## Example 4. Standardize a Gaussian observation

For $X\sim\mathcal N(10,4)$, we have $\mu=10$ and $\sigma=2$. The z-score of observation $x=13$ is

\[
z=\frac{13-10}{2}=1.5
\]

The value $13$ lies $1.5$ standard deviations above the mean. Obtaining a tail probability from this value requires an additional standard normal CDF calculation.

## Example 5. Neural network outputs and distribution parameters

If a binary classifier gives sigmoid output $p_\theta(x)=0.8$ at input $x$, it can be interpreted as

\[
Y\mid X=x\sim\operatorname{Bernoulli}(0.8)
\]

For a three-class softmax output $(0.2,0.5,0.3)$,

\[
Y\mid X=x\sim\operatorname{Categorical}(0.2,0.5,0.3)
\]

These expressions describe conditional distributions specified by the model.

## Common misconceptions

### Misconception 1. Bernoulli and binomial describe the same random variable

Bernoulli describes one binary outcome. Binomial counts successes across several independent Bernoulli trials with the same success probability.

### Misconception 2. A categorical probability vector is a one-hot label

$\boldsymbol\pi$ assigns probabilities to all classes. A one-hot vector records the single class observed in one trial.

### Misconception 3. The second Gaussian parameter is standard deviation

In the notation $\mathcal N(\mu,\sigma^2)$, the second parameter is variance. Check the API to see whether a library takes $\sigma$ as scale or $\sigma^2$ as variance.

### Misconception 4. Knowing mean and variance establishes that a distribution is Gaussian

Different distributions can have the same mean and variance. The Gaussian family assumption is needed for $\mu$ and $\sigma^2$ to determine the distribution.

### Misconception 5. A bell-shaped activation histogram proves the Gaussian assumption

A finite-sample histogram's shape depends on bin width and sample size. Assessing Gaussian fit requires checking tails, skewness, and fit on independent samples.

## Exercises

### 1. Bernoulli calculation

Let $X\sim\operatorname{Bernoulli}(0.2)$. Calculate $P(X=0)$, $\mathbb E[X]$, and $\operatorname{Var}(X)$.

<details>
<summary>Show solution</summary>

\[
P(X=0)=1-0.2=0.8,
\quad
\mathbb E[X]=0.2,
\quad
\operatorname{Var}(X)=0.2\cdot0.8=0.16.
\]

</details>

### 2. Categorical probability

Let $Y\sim\operatorname{Categorical}(0.1,0.4,0.3,0.2)$. Calculate $P(Y\ge3)$ and write the one-hot vector for $Y=4$.

<details>
<summary>Show solution</summary>

\[
P(Y\ge3)=P(Y=3)+P(Y=4)=0.3+0.2=0.5.
\]

The one-hot vector for $Y=4$ is $(0,0,0,1)^\top$.

</details>

### 3. Binomial calculation

Let $S\sim\operatorname{Binomial}(4,0.25)$. Calculate $P(S=1)$.

<details>
<summary>Show solution</summary>

\[
P(S=1)
=\binom41(0.25)^1(0.75)^3
=4\cdot0.25\cdot0.421875
=0.421875.
\]

</details>

### 4. Binomial mean and variance

Let $S\sim\operatorname{Binomial}(20,0.3)$. Calculate $\mathbb E[S]$ and $\operatorname{Var}(S)$.

<details>
<summary>Show solution</summary>

\[
\mathbb E[S]=20\cdot0.3=6,
\]

\[
\operatorname{Var}(S)=20\cdot0.3\cdot0.7=4.2.
\]

</details>

### 5. Gaussian standardization

Let $X\sim\mathcal N(50,100)$. Calculate the z-score of $x=65$.

<details>
<summary>Show solution</summary>

The variance is 100, so the standard deviation is $\sigma=10$. Therefore,

\[
z=\frac{65-50}{10}=1.5.
\]

</details>

### 6. Select distributions

Choose a distribution family to model each of the following at an input: binary correctness, a label selecting one of five topics, and a real-valued measurement error. Explain each support.

<details>
<summary>Show solution</summary>

Binary correctness can use a Bernoulli distribution supported on $\{0,1\}$. A five-topic label fits a categorical distribution supported on $\{1,\ldots,5\}$. A Gaussian supported on $\mathbb R$ can be chosen for real-valued measurement error, but its symmetry and tail assumptions must be checked against data.

</details>

### 7. Evaluate a model claim

A regression model outputs $Y\mid X=x\sim\mathcal N(\mu_\theta(x),\sigma_\theta^2(x))$. Evaluate the conclusion, “This model knows the true conditional distribution exactly.”

<details>
<summary>Show solution</summary>

The expression shows that the model uses a conditional Gaussian distribution. Whether the actual conditional distribution is Gaussian, and whether the predicted mean and variance are correct, must be evaluated on independent data through residual distributions, calibration, and tail fit. There is no guarantee that the same fit persists under distribution shift.

</details>

## Lesson summary

- Bernoulli represents one binary outcome with parameter $p$.
- Categorical generates one category using a probability vector for $K$ classes.
- Binomial is the distribution of the success count in independent Bernoulli trials with the same success probability.
- Gaussian uses mean $\mu$ and variance $\sigma^2$ to set location and scale.
- A standardized Gaussian random variable follows a standard normal distribution.
- A multivariate Gaussian uses a mean vector and covariance matrix.
- Choosing a distribution family includes assumptions about target support and data generation.

## Pass criteria

You pass if you can answer the following without consulting the material.

- Can you distinguish the supports of Bernoulli, categorical, binomial, and Gaussian distributions?
- Can you read each distribution's parameters and PMF or PDF?
- Can you calculate Bernoulli and binomial means and variances?
- Can you distinguish a categorical probability vector from a one-hot observation?
- Can you standardize a Gaussian observation?
- Can you choose a family for a prediction target and state its assumptions?
- Can you limit model claims justified by one distributional output?

## Next lesson

- [M04-06 Samples, populations, and sampling distributions](M04-06-samples-populations-sampling-distributions.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Supports and parameters of the four distributions are specified.
- [x] PMFs and PDFs are distinguished.
- [x] Bernoulli and binomial moments are calculated.
- [x] Gaussian standardization and multivariate notation are explained.
- [x] Model outputs are connected to distributional assumptions.
- [x] Every exercise has a solution.
- [x] Strengths of model interpretability claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
