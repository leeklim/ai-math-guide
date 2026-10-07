---
id: "M04-04"
title: "Expectation, variance, and covariance"
part: 1
stage: "M04"
status: "complete"
prerequisites:
  - "M01-08"
  - "M02-14"
  - "M04-03"
estimated_time: "145~170 minutes"
---

# M04-04. Expectation, variance, and covariance

## Why this lesson matters

A table or function specifying an entire probability distribution shows all possible values and their probabilities. Papers and experimental reports often summarize that distribution with a few numbers. Expectation describes its average location, variance describes its spread around that location, and covariance describes the direction in which two random variables vary together.

The mean and covariance matrix of activations, the mean and standard deviation of loss, and performance variation across seeds all use these summaries. Distributions with the same mean can differ in spread and covariation, so each summary must be read in terms of the information it retains and discards.

## Learning objectives

After completing this lesson, you should be able to:

- Calculate expectations of discrete and continuous random variables.
- Apply linearity of expectation and determine whether independence is needed.
- Calculate variance and standard deviation and distinguish their units.
- Convert between the two formulas for variance.
- Calculate covariance and correlation from a joint distribution.
- Distinguish being uncorrelated from being independent.
- Explain the limits of interpreting model representations from their mean and covariance alone.

## Prerequisite check

- Prerequisite: [M01-08 Integration and accumulation](../M01/M01-08-integration-accumulation.md)
- Prerequisite: [M02-14 Data matrices, covariance, and PCA](../M02/M02-14-covariance-pca.md)
- Prerequisite: [M04-03 Random variables and probability distributions](M04-03-random-variables-distributions.md)
- Check: Can you sum PMF probabilities and integrate a PDF over an interval?
- Check: Can you obtain marginal distributions from a joint PMF?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Scope and units |
|---|---|---|---|
| $\mathbb E[X]$ | `the expectation of X` | The distribution-weighted mean of $X$ | The same units as $X$ |
| $\mu_X$ | `mu sub X` | The population mean of $X$ | $\mu_X=\mathbb E[X]$ |
| $\operatorname{Var}(X)$ | `the variance of X` | The expectation of squared distance from the mean | The squared units of $X$ |
| $\sigma_X$ | `sigma sub X` | The standard deviation of $X$ | $\sqrt{\operatorname{Var}(X)}$ |
| $\operatorname{Cov}(X,Y)$ | `the covariance of X and Y` | The direction and magnitude of covariation between two centered variables | The product of the units of $X$ and $Y$ |
| $\rho_{X,Y}$ | `rho sub X Y` | Covariance divided by the product of standard deviations | $-1\le\rho_{X,Y}\le1$ |
| $\mathbf\Sigma$ | `capital sigma` | The covariance matrix of a random vector | A symmetric positive semidefinite matrix |

## Core concept 1. Expectation is a weighted mean determined by a distribution

The expectation of a discrete random variable $X$ is

\[
\mathbb E[X]
=\sum_x x\,p_X(x)
\]

Multiply each possible value by its probability and add the products. For a continuous random variable, replace the sum with an integral:

\[
\mathbb E[X]
=\int_{-\infty}^{\infty}x f_X(x)\,dx.
\]

For expectation to exist, the sum or integral must converge appropriately. An expectation can lie outside the set of possible values of the random variable. A fair die has expectation $3.5$, although $3.5$ cannot occur on a single roll.

When calculating a finite mean in this lesson, assume $\sum_x |x|p_X(x)<\infty$ or $\int |x|f_X(x)\,dx<\infty$. This condition prevents defining a mean by canceling infinite positive and negative contributions. Variables whose variance or covariance we calculate are also assumed to have finite second moments $\mathbb E[X^2]$. These conditions hold in examples with finitely many possible values, each of which is finite.

The illustrative distribution below assigns unequal masses to 0 and 2. Its mean is closer to the larger mass, but it need not be one of the possible values.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A number line with probability masses 0.25 at zero and 0.75 at two balancing at expectation 1.5, which is not a possible outcome](../../figures/assets/M04/M04-04-weighted-balance-point.svg)

<figcaption>Circle area represents probability mass, and horizontal position represents value. The balance point is where mass times distance agrees on the two sides of the mean. Here it is 1.5, which cannot occur as an observation from this distribution.</figcaption>
</figure>

## Core concept 2. The expectation of a function can be calculated from the original distribution

If $Y=g(X)$, we can calculate

\[
\mathbb E[g(X)]
=\sum_x g(x)p_X(x)
\]

without first constructing the distribution of $Y$. In the continuous case,

\[
\mathbb E[g(X)]
=\int_{-\infty}^{\infty}g(x)f_X(x)\,dx
\]

This rule applies to averages of transformations such as $g(X)=X^2$, loss $\ell(X)$, and indicators.

In the discrete case, several values of $x$ satisfying $g(x)=y$ may map to the same value $y$ of $Y$. The probability of that value is the sum of the probabilities of those $x$ values. Thus, calculating the expectation of $Y$ by its possible values gives

\[
\sum_y y\,p_Y(y)
=\sum_y y\sum_{x:g(x)=y}p_X(x)
=\sum_x g(x)p_X(x)
\]

The expression on the right skips the intermediate grouping of equal outputs and instead multiplies each transformed output by the probability of its original input. Here too, assume $\mathbb E[|g(X)|]<\infty$ so that the expectation is finite.

Define the indicator of an event $A$ by

\[
\mathbf 1_A=
\begin{cases}
1,&A\text{ occurs},\\
0,&A\text{ does not occur}
\end{cases}
\]

Then

\[
\mathbb E[\mathbf 1_A]=P(A)
\]

Accuracy can also be expressed as the average of an indicator of correct prediction for each sample.

An indicator takes only the values 1 and 0, so its expectation is $1\cdot P(A)+0\cdot P(A^c)=P(A)$. This relation expresses an event's probability as the average of a numerical function.

Under squaring, different original values can map to the same output. The two calculations below differ only in whether equal outputs are grouped first.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Values minus two and two with mass one quarter each mapped by squaring to four with mass one half, while value one with mass one half stays one, yielding expectation 2.5](../../figures/assets/M04/M04-04-transform-before-average.svg)

<figcaption>Transforming the values retains their original probability weights. Grouping the probabilities that map to output 4 first gives the same expectation as multiplying each of the three transformed values by its original probability and adding.</figcaption>
</figure>

## Core concept 3. Expectation is linear

For constants $a,b,c$ and random variables $X,Y$,

\[
\mathbb E[aX+bY+c]
=a\mathbb E[X]+b\mathbb E[Y]+c
\]

This property does not require $X$ and $Y$ to be independent. The mean of a sum is the sum of its terms' means.

In the discrete case, use the same joint distribution as the weights:

\[
\mathbb E[aX+bY+c]
=\sum_x\sum_y (ax+by+c)p_{X,Y}(x,y)
\]

Expand the parentheses. Summing over $y$ in the first term gives $p_X(x)$, and summing over $x$ in the second gives $p_Y(y)$. The constant term is multiplied by the total probability 1. No step factors the joint probability into a product of marginal probabilities.

In contrast, factoring the expectation of a product as

\[
\mathbb E[XY]=\mathbb E[X]\mathbb E[Y]
\]

requires an additional condition, such as independence. Linearity of expectation and factoring a product are different rules.

## Core concept 4. Variance is the mean squared distance from the mean

Let $\mu_X=\mathbb E[X]$. Variance is

\[
\operatorname{Var}(X)
=\mathbb E\left[(X-\mu_X)^2\right]
\]

Squaring prevents positive and negative deviations from the mean from canceling. Variance is nonnegative and equals 0 when $X$ is constant with probability 1.

Expanding the expression gives a form convenient for calculation:

\[
\begin{aligned}
\operatorname{Var}(X)
&=\mathbb E[X^2-2\mu_X X+\mu_X^2]\\
&=\mathbb E[X^2]-2\mu_X\mathbb E[X]+\mu_X^2\\
&=\mathbb E[X^2]-\mu_X^2.
\end{aligned}
\]

The standard deviation is

\[
\sigma_X=\sqrt{\operatorname{Var}(X)}
\]

Variance has the squared units of $X$, whereas standard deviation has the same units as $X$.

Squaring the deviations on either side of the mean 1 in Example 1 turns the two oppositely signed distances into positive contributions.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Head-count values zero, one and two centered at mean one with signed deviations minus one, zero and plus one transformed into squared deviations one, zero and one](../../figures/assets/M04/M04-04-squared-deviations.svg)

<figcaption>The squares on the two sides represent equal squared distances. The middle deviation is 0 and contributes nothing. Multiply each squared distance by its original probability to calculate variance.</figcaption>
</figure>

## Core concept 5. Translation and scaling affect variance differently

For constants $a,b$,

\[
\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)
\]

Adding $b$ shifts every value and the mean together, leaving deviations from the mean unchanged. Multiplying by $a$ multiplies deviations by $a$ and squared deviations by $a^2$.

The variance of a sum of two random variables includes a covariance term:

\[
\operatorname{Var}(X+Y)
=\operatorname{Var}(X)+\operatorname{Var}(Y)
+2\operatorname{Cov}(X,Y).
\]

Independent $X,Y$ have covariance 0, so in that case their two variances add.

The sum has mean $\mu_X+\mu_Y$, so its centered value is $(X-\mu_X)+(Y-\mu_Y)$. Squaring this deviation gives

\[
(X-\mu_X)^2+(Y-\mu_Y)^2
+2(X-\mu_X)(Y-\mu_Y)
\]

Taking expectations gives the two variances in the first two terms and twice the covariance in the last. The variance of a sum therefore includes both the spread of each variable and whether their deviations tend to have matching or opposite signs.

Shifting or stretching the positions of the values while retaining the same probability masses shows how their distances from the mean change.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three distributions on a shared number-line scale showing X with mean one and variance 0.5, X plus three with unchanged variance, and twice X with variance two](../../figures/assets/M04/M04-04-affine-variance.svg)

<figcaption>In the translated row, the points and their mean shift together. In the doubled row, distances from the mean double, so the mean squared distance increases by a factor of four.</figcaption>
</figure>

Even with the same individual variances, the sum's spread depends on whether the two variables move in the same or opposite directions.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two equally weighted joint outcomes aligned along Y equals X or opposed along Y equals minus X, producing sum distributions of variance four or zero despite equal marginal variances](../../figures/assets/M04/M04-04-covariance-sum.svg)

<figcaption>On the left, deviations reinforce each other and move the sum farther from its mean. On the right, deviations of equal magnitude cancel. Both sums have mean 0 but different variances. The upper points show the two possible joint outcomes in each case.</figcaption>
</figure>

## Core concept 6. Covariance describes the direction of covariation between centered variables

Covariance is

\[
\operatorname{Cov}(X,Y)
=\mathbb E\left[(X-\mu_X)(Y-\mu_Y)\right]
\]

Expanding gives

\[
\operatorname{Cov}(X,Y)
=\mathbb E[XY]-\mathbb E[X]\mathbb E[Y]
\]

Positive covariance means that the variables tend to be above or below their respective means together. Negative covariance means that when one is above its mean, the other tends to be below its mean. Covariance 0 means no linear covariation.

The expectation of the four expanded terms is $\mathbb E[XY]-\mu_Y\mathbb E[X]-\mu_X\mathbb E[Y]+\mu_X\mu_Y$. Substituting the definitions of the means combines the middle two terms and the last into $-\mu_X\mu_Y$. A product of deviations is positive when the deviations have the same sign and negative when they have opposite signs. Covariance sums these products with probability weights, so a result of 0 can also arise from cancellation between positive and negative contributions.

Covariance depends on the variables' units and scales. The correlation coefficient standardizes it:

\[
\rho_{X,Y}
=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y},
\qquad \sigma_X,\sigma_Y>0.
\]

Correlation does not determine nonlinear dependence or causal direction either.

Subtracting a variable's mean and dividing by its standard deviation gives mean 0 and variance 1. Averaging the product of the two standardized variables gives $\rho_{X,Y}$. For any real $t$, the expected square of one standardized variable minus $t$ times the other is $1-2t\rho_{X,Y}+t^2\ge0$. Setting $t=\rho_{X,Y}$ gives $1-\rho_{X,Y}^2\ge0$, so correlation lies in $[-1,1]$. If a standard deviation is 0, this standardization and the correlation coefficient are undefined.

Subtracting the means in Example 2 shows which side of each mean the four joint outcomes occupy. Each point contributes the product of its deviations multiplied by its probability.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Four centered binary joint outcomes in positive and negative deviation-product quadrants with weighted contributions 0.09, minus 0.04, minus 0.03 and 0.08 totaling covariance 0.10](../../figures/assets/M04/M04-04-covariance-products.svg)

<figcaption>Deviations with the same sign contribute positively; deviations with opposite signs contribute negatively. Circle area represents an outcome's probability. Covariance's sign depends on the sum of these weighted contributions, not merely the number of points in each region.</figcaption>
</figure>

Restricting $Y=X^2$ from Misconception 4 to three possible values shows that a functional dependence can remain even when the two sides' contributions cancel.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three equally likely outcomes on Y equals X squared with negative and positive weighted covariance contributions canceling to zero despite deterministic dependence](../../figures/assets/M04/M04-04-uncorrelated-dependent.svg)

<figcaption>The three purple points are the possible joint outcomes, each with probability 1/3. The gray curve indicates the function rule; it does not assign probability to every point on the curve. Knowing X determines Y even though covariance is 0.</figcaption>
</figure>

## Core concept 7. A covariance matrix collects second-order covariation in a random vector

For a random vector $\mathbf X\in\mathbb R^d$ with mean vector

\[
\boldsymbol\mu=\mathbb E[\mathbf X]
\]

the covariance matrix is

\[
\mathbf\Sigma
=\mathbb E\left[(\mathbf X-\boldsymbol\mu)
(\mathbf X-\boldsymbol\mu)^\top\right]
\in\mathbb R^{d\times d}
\]

Its diagonal entries are component variances, and its off-diagonal entries are covariances between component pairs. For any direction $\mathbf v$,

\[
\operatorname{Var}(\mathbf v^\top\mathbf X)
=\mathbf v^\top\mathbf\Sigma\mathbf v\ge0
\]

so $\mathbf\Sigma$ is positive semidefinite.

Expectation is applied componentwise to a vector or matrix. Thus $\Sigma_{ij}=\mathbb E[(X_i-\mu_i)(X_j-\mu_j)]$, and commutativity of scalar multiplication gives $\Sigma_{ij}=\Sigma_{ji}$. This explains both the interpretation as a collection of component-pair covariances and the matrix's symmetry.

The direction $\mathbf v$ consists of fixed coefficients, and $\mathbf v^\top\mathbf X$ is a scalar random variable. Its centered value is $\mathbf v^\top(\mathbf X-\boldsymbol\mu)$, whose square is $\mathbf v^\top(\mathbf X-\boldsymbol\mu)(\mathbf X-\boldsymbol\mu)^\top\mathbf v$. Taking the fixed coefficients outside expectation gives the variance formula above. It has the same outer product structure as the covariance matrix formed by summing centered data vectors in M02-14. Here a distributional expectation replaces the observed sum.

Activation covariance depends on the chosen data distribution and coordinates. Distributions can agree in mean and covariance while differing in higher-order structure, so these two summaries do not establish that entire representations are identical.

Forming a centered vector from one joint outcome in Example 2 shows which components are multiplied in each row and column of the outer product.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Centered vector 0.5 and 0.4 forming a two-by-two outer product with diagonal squared deviations and symmetric off-diagonal component products, labeled as one outcome contribution rather than the full covariance matrix](../../figures/assets/M04/M04-04-outer-product-entries.svg)

<figcaption>The matrix formed from one outcome contains all component-pair products. The covariance matrix is not this single matrix: it is the average of the matrices for all possible outcomes, weighted by their original probabilities.</figcaption>
</figure>

Even for the same covariance matrix, the spread of the scalar projection changes with the unit direction onto which values are projected.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Exact centered binary joint probabilities projected onto the two unit directions one-one and one-minus-one, yielding direction variances 0.345 and 0.145](../../figures/assets/M04/M04-04-direction-variance.svg)

<figcaption>The bars show the probabilities of possible projected values in each direction. Both projections have mean 0 but different mean squared distances. The covariance matrix's quadratic form calculates exactly this variance.</figcaption>
</figure>

Matching mean and variance does not make distributions identical. The two scalar distributions below have the same first- and second-order summaries but different possible values and mass assignments.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two distinct discrete distributions with mean zero and variance one, one supported on minus one and one and the other on minus square root two, zero and square root two](../../figures/assets/M04/M04-04-same-moments.svg)

<figcaption>The upper distribution has no mass at 0, whereas the lower assigns probability 1/2 there. Mean and variance do not record this difference. The same limitation applies when comparing entire vector distributions by their mean and covariance.</figcaption>
</figure>

## Example 1. Calculate mean and variance from a PMF

### Problem

Suppose $X$ has the following PMF.

| $x$ | 0 | 1 | 2 |
|---:|---:|---:|---:|
| $p_X(x)$ | $1/4$ | $1/2$ | $1/4$ |

Calculate $\mathbb E[X]$, $\operatorname{Var}(X)$, and $\sigma_X$.

### Solution

The expectation is

\[
\mathbb E[X]
=0\cdot\frac14+1\cdot\frac12+2\cdot\frac14
=1
\]

The second moment is

\[
\mathbb E[X^2]
=0^2\cdot\frac14+1^2\cdot\frac12+2^2\cdot\frac14
=\frac32
\]

Therefore,

\[
\operatorname{Var}(X)
=\mathbb E[X^2]-\mathbb E[X]^2
=\frac32-1
=\frac12
\]

and

\[
\sigma_X=\sqrt{\frac12}\approx0.707
\]

### Meaning of the result

The distribution is centered at 1, and its mean squared distance from the mean is $1/2$. Standard deviation expresses spread in the same units as the original values.

## Example 2. Calculate covariance from a joint PMF

Suppose the joint PMF is as follows.

| $p_{X,Y}(x,y)$ | $Y=0$ | $Y=1$ |
|---|---:|---:|
| $X=0$ | 0.30 | 0.20 |
| $X=1$ | 0.10 | 0.40 |

The marginal distributions give

\[
\mathbb E[X]=0.50,
\qquad
\mathbb E[Y]=0.60
\]

Only $(X,Y)=(1,1)$ gives $XY=1$, so

\[
\mathbb E[XY]=0.40.
\]

Hence,

\[
\operatorname{Cov}(X,Y)
=0.40-(0.50)(0.60)
=0.10.
\]

The two binary variables tend to take their above-mean value 1 together, giving positive covariance.

## Example 3. Mean and variance under a linear transformation

Let $\mathbb E[X]=3$, $\operatorname{Var}(X)=4$, and $Y=2X-5$. Then

\[
\mathbb E[Y]=2\cdot3-5=1
\]

and

\[
\operatorname{Var}(Y)=2^2\cdot4=16.
\]

The constant $-5$ shifts the mean but does not affect variance.

## Example 4. Express accuracy as an indicator average

Let $I_n$ be 1 if the prediction for the $n$th sample is correct and 0 otherwise. Accuracy on $N$ samples is

\[
\widehat{\mathrm{acc}}
=\frac1N\sum_{n=1}^{N}I_n
\]

Each $I_n$ has expectation equal to the probability of a correct prediction under that sample's conditions. Observed accuracy is a sample mean of indicators. Its difference from population accuracy is covered from M04-06 onward.

## Common misconceptions

### Misconception 1. Expectation is the most frequent value

Expectation is a probability-weighted mean. It can differ from the mode and can be a value the random variable cannot take.

### Misconception 2. Linearity of expectation requires independence

$\mathbb E[X+Y]=\mathbb E[X]+\mathbb E[Y]$ also holds for dependent variables. Independence is used to factor the expectation of a product or eliminate covariance from the variance of a sum.

### Misconception 3. Variance and standard deviation are the same number

Standard deviation is the square root of variance. Variance has squared units, whereas standard deviation has the original variable's units.

### Misconception 4. Covariance 0 implies independence

Independent variables have covariance 0 when the relevant expectations exist. The converse fails. For example, if $X$ is symmetric and $Y=X^2$, then $Y$ is determined by $X$, yet covariance can be 0.

### Misconception 5. High correlation proves that one variable causes the other

Correlation summarizes a linear relation in a joint distribution. Evaluating a causal effect requires a design with interventions and control conditions.

## Exercises

### 1. Calculate expectation

Let $p_X(-1)=0.2$, $p_X(0)=0.5$, and $p_X(2)=0.3$. Calculate $\mathbb E[X]$.

<details>
<summary>Show solution</summary>

\[
\mathbb E[X]
=(-1)(0.2)+0(0.5)+2(0.3)
=-0.2+0.6
=0.4.
\]

Each possible value is multiplied by its probability, and the products are added.

</details>

### 2. Expectation of a function

Calculate $\mathbb E[X^2]$ for the distribution in the preceding exercise.

<details>
<summary>Show solution</summary>

\[
\mathbb E[X^2]
=(-1)^2(0.2)+0^2(0.5)+2^2(0.3)
=0.2+1.2
=1.4.
\]

The calculation uses the original PMF of $X$, without constructing a separate distribution for $X^2$.

</details>

### 3. Linearity

Let $\mathbb E[X]=2$ and $\mathbb E[Y]=-1$. Calculate $\mathbb E[3X-2Y+4]$ without knowing whether $X,Y$ are independent.

<details>
<summary>Show solution</summary>

Linearity of expectation gives

\[
\mathbb E[3X-2Y+4]
=3(2)-2(-1)+4
=12
\]

This calculation does not require independence.

</details>

### 4. Calculate variance

Let $\mathbb E[X]=2$ and $\mathbb E[X^2]=7$. Calculate $\operatorname{Var}(X)$ and $\sigma_X$.

<details>
<summary>Show solution</summary>

\[
\operatorname{Var}(X)=7-2^2=3,
\qquad
\sigma_X=\sqrt3.
\]

Variance is nonnegative, and standard deviation is its square root.

</details>

### 5. Variance of a sum

Let $\operatorname{Var}(X)=4$, $\operatorname{Var}(Y)=9$, and $\operatorname{Cov}(X,Y)=-2$. Calculate $\operatorname{Var}(X+Y)$.

<details>
<summary>Show solution</summary>

\[
\operatorname{Var}(X+Y)
=4+9+2(-2)
=9.
\]

The negative covariance makes the sum's spread smaller than the sum of the two variances.

</details>

### 6. Uncorrelatedness and independence

Let $X$ take $-1,0,1$, each with probability $1/3$, and let $Y=X^2$. Calculate $\operatorname{Cov}(X,Y)$ and determine whether the variables are independent.

<details>
<summary>Show solution</summary>

We have $\mathbb E[X]=0$ and $\mathbb E[Y]=2/3$. Since $XY=X^3$, $\mathbb E[XY]=0$. Therefore,

\[
\operatorname{Cov}(X,Y)=0-0\cdot\frac23=0.
\]

The variables are dependent because specifying $X$ determines $Y$. Numerically, $P(Y=0)=1/3$, whereas $P(Y=0\mid X=0)=1$. The example shows that covariance 0 alone cannot establish independence.

</details>

### 7. Evaluate a claim about model representations

Two models' activations have the same mean vector and covariance matrix. Evaluate the conclusion, “The two models learned the same representation.”

<details>
<summary>Show solution</summary>

Mean and covariance match only first and second moments. Higher-order distributional structure, tokenwise correspondence, nonlinear relations, and the way the models use activations can differ. The comparison must also use the same data and coordinates. Claiming identical representations requires additional comparisons appropriate to the research question and evidence from interventions.

</details>

## Lesson summary

- Expectation is the mean obtained by probability-weighting possible values or integrating against a density.
- The expectation of a function can be calculated from the original random variable's distribution.
- Linearity of expectation does not require independence between random variables.
- Variance is expected squared distance from the mean; standard deviation is its square root.
- The variance of a sum includes a covariance term.
- Covariance and correlation summarize linear covariation and do not guarantee independence or causation.
- A covariance matrix collects component variances and covariances in a PSD matrix.

## Pass criteria

You pass if you can answer the following without consulting the material.

- Can you calculate expectation from a PMF or PDF?
- Can you explain $\mathbb E[g(X)]$ and the expectation of an indicator?
- Can you determine whether linearity of expectation requires independence?
- Can you connect the defining and computational formulas for variance?
- Can you distinguish the units of standard deviation and variance?
- Can you calculate covariance and correlation from a joint distribution?
- Can you limit the claims justified by representations with the same mean and covariance?

## Next lesson

- [M04-05 Common distributions](M04-05-common-distributions.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Discrete and continuous expectations are defined.
- [x] Linearity of expectation is distinguished from conditions requiring independence.
- [x] Variance formulas and units are explained.
- [x] Covariance and correlation are calculated.
- [x] The covariance matrix's shape and PSD property are stated.
- [x] Every exercise has a solution.
- [x] Strengths of model interpretability claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
