---
id: "M04-03"
title: "Random variables and probability distributions"
part: 1
stage: "M04"
status: "complete"
prerequisites:
  - "M00-03"
  - "M04-01"
  - "M04-02"
estimated_time: "140–165 minutes"
---

# M04-03. Random variables and probability distributions

## Why this lesson matters

When sample-space outcomes are strings, images, sentences, or experimental records, you cannot directly add or average the outcomes themselves. A random variable extracts the needed numerical or categorical value from each outcome. Its probability distribution describes which values it can take and how often.

Expectation, variance, likelihood, entropy, and a model's predictive distribution all use random variables and distributions. Distinguishing a random variable $X$, an observed value $x$, and a distribution $p_X(x)$ helps you track the roles of the same letter in a paper.

## Learning objectives

After completing this lesson, you should be able to:

- Explain a random variable as a function from a sample space to a value space.
- Distinguish the random variable $X$ from an observed value $x$.
- Construct and check a discrete random variable's probability mass function.
- Read a cumulative distribution function as an event probability and calculate it.
- Distinguish a continuous distribution's density from the probability at one point.
- Calculate marginal and conditional distributions from a joint distribution.
- Distinguish a model's predictive distribution from an observed label and limit the resulting claims.

## Prerequisite check

- Prerequisite lesson: [M00-03 Functions, inputs, and outputs](../M00/M00-03-functions-input-output.md)
- Prerequisite lesson: [M04-01 Events and probability](M04-01-events-probability.md)
- Prerequisite lesson: [M04-02 Conditional probability and Bayes' rule](M04-02-conditional-probability-bayes-rule.md)
- Check: Can you explain what it means for a function to assign one output to each input?
- Check: Can you calculate event probabilities and conditional probabilities?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Scope |
|---|---|---|---|
| $X$ | `X` | A function mapping outcomes to values | $X:\Omega\to\mathcal X$ |
| $x$ | `x` | An observed or possible value of $X$ | $x\in\mathcal X$ |
| $p_X(x)$ | `p sub X of x` | The probability that $X=x$ | $P(X=x)$ for discrete $X$ |
| $F_X(x)$ | `F sub X of x` | The probability that $X$ is at most $x$ | $P(X\le x)$ |
| $f_X(x)$ | `f sub X of x` | A density whose integral gives interval probabilities | Continuous $X$ |
| $p_{X,Y}(x,y)$ | `p sub X Y of x comma y` | The probability that $X=x$ and $Y=y$ occur together | Discrete $X,Y$ |
| distribution | `distribution` | A rule assigning probabilities to a random variable's values or intervals | Discrete or continuous |

## Core concept 1. A random variable is a function extracting a value from an outcome

A random variable $X$ is a function of the form

\[
X:\Omega\to\mathcal X
\]

Despite the word “variable,” once an outcome $\omega$ is given, $X(\omega)$ is a single determined value. Randomness comes from not knowing which $\omega$ will occur before the trial.

For the sample space of two coin tosses,

\[
\Omega=\{HH,HT,TH,TT\}
\]

define a random variable counting heads:

\[
X(HH)=2,
\quad X(HT)=X(TH)=1,
\quad X(TT)=0
\]

Multiple outcomes can map to the same value.

In a precise definition, conditions on $X$'s values must produce events to which probabilities can be assigned. In the finite and countable examples of this lesson, every subset is treated as an event, so this condition holds automatically.

Mapping the four outcomes to head counts sends two distinct outcomes to the same value $1$.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A head-count function mapping TT to zero, HT and TH to one, and HH to two, with observed HT recorded as lowercase x equals one](../../figures/assets/M04/M04-03-outcome-value-map.svg)

<figcaption>Each outcome has just one outgoing assignment, but a value can have multiple incoming assignments. The entire assignment rule is X; observing HT gives the single recorded value x=1.</figcaption>
</figure>

## Core concept 2. Uppercase random variables and lowercase observations have different roles

$X$ is a function with possible values and probabilities before the trial; $x$ is an observed value or one specified in a calculation. The expression

\[
P(X=x)
\]

means the probability of the event where random variable $X$ takes value $x$. If $X=1$ is observed, record lowercase $x=1$ in the data.

Machine-learning notation likewise distinguishes the input random variable $X$ and label random variable $Y$ from a sample's observations $x,y$. $p_\theta(y\mid x)$ is the probability the model assigns to a possible label value $y$ given observed input $x$.

All the arrows in the figure above show $X$'s rule; the observation record at the bottom shows the role of lowercase $x$.

## Core concept 3. A distribution specifies how a random variable takes values

Once random variable $X$ and probability $P$ on the sample space are specified, $X$'s distribution is determined. For a set of values $S\subseteq\mathcal X$,

\[
P(X\in S)
=P\bigl(\{\omega\in\Omega:X(\omega)\in S\}\bigr)
\]

The set on the right is the preimage: the outcomes $X$ maps into $S$.

To calculate, specify a condition on values, collect the outcomes satisfying it, then apply the original probability $P$. For example, the condition of one head has preimage $\{HT,TH\}$. A preimage is not an inverse function recovering one outcome, so $X$ need not be one-to-one. When several outcomes map to the same value, their probabilities are collected at that value.

Different random variables on the same sample space can have different distributions. For two coin tosses, head count $X$ and indicator $Z$ for whether the two results agree have different values and produce different distributions.

Starting from the value condition $X=1$ and finding all corresponding outcomes shows that the preimage is a set, not a single outcome. Below, each of the four outcomes has probability $1/4$.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The value condition X equals one selecting preimage outcomes HT and TH, each with probability one quarter and total probability one half](../../figures/assets/M04/M04-03-preimage-mass.svg)

<figcaption>Add the original probabilities of both outcomes satisfying the value condition. Following the arrows backward finds all corresponding outcomes; it does not recover just one original outcome as an inverse function would.</figcaption>
</figure>

## Core concept 4. A discrete random variable is represented by a probability mass function

A discrete random variable's probability mass function (PMF) is

\[
p_X(x)=P(X=x)
\]

A valid PMF satisfies

\[
p_X(x)\ge0,
\qquad
\sum_{x\in\mathcal X}p_X(x)=1
\]

For two distinct values $x_1,x_2$, the events $\{X=x_1\}$ and $\{X=x_2\}$ are disjoint because $X$ cannot give two values at the same outcome. The union of all possible-value events is $\Omega$, so additivity gives the PMF's total of 1. For the same reason, adding terms for a value set $S$ gives its event probability.

Calculate the probability of a value set $S$ by

\[
P(X\in S)=\sum_{x\in S}p_X(x)
\]

As in the previous lesson's coin example, assume the four ordered outcomes each have probability $1/4$. The PMF of head count $X$ is then

| $x$ | 0 | 1 | 2 |
|---:|---:|---:|---:|
| $p_X(x)$ | $1/4$ | $1/2$ | $1/4$ |

The value $1$ collects two outcomes, $HT$ and $TH$, so its probability is $1/2$.

The height of a PMF bar is the probability collected at that value. Empty space between bars does not mean that intermediate values have assigned probability.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A head-count PMF with bars at zero, one and two of heights 0.25, 0.50 and 0.25, labeling the outcomes collected at each value](../../figures/assets/M04/M04-03-head-count-pmf.svg)

<figcaption>The middle bar collects the mass of two outcomes, making it taller than the bars on either side. There are three possible values, but they are not equally probable.</figcaption>
</figure>

## Core concept 5. A cumulative distribution function gives the probability of being at or below a threshold

For both discrete and continuous real-valued random variables, the cumulative distribution function (CDF) is

\[
F_X(x)=P(X\le x)
\]

As $x$ increases, the event $\{X\le x\}$ includes more values, so the CDF does not decrease. Also,

\[
\lim_{x\to-\infty}F_X(x)=0,
\qquad
\lim_{x\to\infty}F_X(x)=1
\]

In the coin example,

\[
F_X(0)=\frac14,
\qquad
F_X(1)=\frac34,
\qquad
F_X(2)=1
\]

A discrete CDF increases in steps at values carrying probability mass.

For a discrete distribution, add PMF terms for possible values $t$ at or below the threshold: $F_X(x)=\sum_{t\le x}p_X(t)$. Here, $x$ can be a real comparison threshold rather than an observed value. In the coin example, $x=0.5$ is not a possible value of $X$, but 0 is the only value included in $X\le0.5$, so $F_X(0.5)=1/4$. Moving the threshold between 0 and 1 includes no new mass, leaving the CDF unchanged.

For $a<b$, $\{X\le b\}$ splits into the disjoint events $\{X\le a\}$ and $\{a<X\le b\}$. Thus,

\[
P(a<X\le b)=F_X(b)-F_X(a)
\]

The left endpoint $a$ is excluded because subtracting $F_X(a)$ also subtracts the probability of $X=a$. Endpoint inequalities matter for discrete distributions with point probabilities.

Marking the jump locations and threshold $0.5$ shows that cumulative probability can be queried at a number that is not a possible observation.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A right-continuous head-count CDF stepping to 0.25 at zero, 0.75 at one and one at two, with threshold 0.5 on the first plateau](../../figures/assets/M04/M04-03-head-count-cdf.svg)

<figcaption>A closed point is the actual CDF value at that threshold; an open point marks the height before the jump. Moving the threshold between 0 and 1 adds no mass, so the height stays fixed.</figcaption>
</figure>

## Core concept 6. For a continuous distribution, integrate density over an interval

This lesson considers continuous distributions representable by a probability density function (PDF) $f_X$. Calculate interval probability by

\[
P(a\le X\le b)=\int_a^b f_X(x)\,dx
\]

The density satisfies

\[
f_X(x)\ge0,
\qquad
\int_{-\infty}^{\infty}f_X(x)\,dx=1
\]

$f_X(x)$ is not the probability at one point. For a distribution represented by a density,

\[
P(X=x)=0
\]

A point is an interval of width 0, so the density's integral over it is also 0. An interval with width can have positive probability. Zero point probability does not mean the value is excluded from the sample space.

A density value can exceed 1, but probability, the area under the density over an interval, lies in $[0,1]$. Converting density to probability also requires interval width. In Example 2 the density is 1, but an interval of width $0.3$ has probability $0.3$. For a distribution represented by a density, the CDF and density are related by

\[
F_X(x)=\int_{-\infty}^{x}f_X(t)\,dt
\]

In Example 2's uniform distribution, distinguish interval width from density height. The separately marked point $0.8$ also has density height 1 but point probability 0.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Uniform density one on zero to one with shaded interval 0.2 to 0.5 of area 0.3 and a single point 0.8 whose width and probability are zero](../../figures/assets/M04/M04-03-uniform-density-area.svg)

<figcaption>The green region has probability equal to width 0.3 times height 1. The orange point marks one location on the density; it has no width and contributes no area by itself.</figcaption>
</figure>

## Core concept 7. A joint distribution describes how multiple random variables vary together

The joint probability mass function of discrete random variables $X,Y$ is

\[
p_{X,Y}(x,y)=P(X=x,Y=y)
\]

Summing over all $Y$ values gives $X$'s marginal distribution.

With $X=x$ fixed, collecting all possible $Y$ values gives event $\{X=x\}$. Joint events for distinct $y$ values are disjoint, so additivity gives the sum below. Summing a table row discards the condition on $Y$, retaining only the value of $X$.

\[
p_X(x)=\sum_y p_{X,Y}(x,y).
\]

For $p_X(x)>0$, the conditional distribution is

\[
p_{Y\mid X}(y\mid x)
=\frac{p_{X,Y}(x,y)}{p_X(x)}
\]

The joint distribution contains each variable's marginal distribution and the way the variables occur together. M04-04 uses this distribution to calculate covariance.

To obtain the conditional distribution, divide the joint table's $X=x$ row by its row sum. Consequently, $\sum_y p_{Y\mid X}(y\mid x)=p_X(x)/p_X(x)=1$. Marginalization sums over all values of the other variable; conditioning restricts to one value and renormalizes the probabilities.

Conversely, row and column sums alone cannot reconstruct each cell. Replacing Example 3's first row with $(0.20,0.30)$ and its second with $(0.20,0.30)$ still gives row sums $0.50$ each and column sums $0.40,0.60$. The marginals are unchanged, but $P(Y=1\mid X=1)$ changes from $0.80$ to $0.60$. The same marginals can accompany different ways of occurring together.

To obtain a marginal distribution, add all cells along one direction. Row sums and column sums in Example 3 remove conditions on different variables.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A two-by-two joint probability table with row sums 0.50 and 0.50 and column sums 0.40 and 0.60 connected to their marginal distributions](../../figures/assets/M04/M04-03-joint-marginal-sums.svg)

<figcaption>Adding the two cells of a row gives the probability of that X value without a condition on Y. Adding the two cells of a column instead sums over X and retains only Y's probability.</figcaption>
</figure>

A conditional distribution retains one row instead of summing over all rows. That row's mass is $0.50$, which becomes the new denominator.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The selected X-one joint row with masses 0.10 and 0.40 rescaled by row total 0.50 to conditional Y probabilities 0.20 and 0.80](../../figures/assets/M04/M04-03-conditional-row-rescale.svg)

<figcaption>The gray right-hand part of the upper bar is mass for another X value and falls outside the condition. Scaling the selected row to total probability 1 makes its Y values' probabilities a conditional distribution.</figcaption>
</figure>

Even if two joint tables have identical marginal sums, mass can be assigned differently among Y values within the selected row.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two joint probability tables with identical row and column marginals but different X-one conditional Y-one probabilities of 0.80 and 0.60](../../figures/assets/M04/M04-03-same-margins-different-joint.svg)

<figcaption>Both tables have the same row and column sums but different lower-right cell masses. Y's probability given the same X therefore differs; the two marginals cannot reconstruct the joint distribution.</figcaption>
</figure>

## Example 1. Construct a PMF from outcomes

### Problem

Toss a fair coin twice and define $X$ as the number of heads. Calculate the PMF of $X$.

### Solution

Each outcome has probability $1/4$. The preimages of $X$'s values are

\[
\{X=0\}=\{TT\},
\quad
\{X=1\}=\{HT,TH\},
\quad
\{X=2\}=\{HH\}
\]

Therefore,

\[
p_X(0)=\frac14,
\qquad
p_X(1)=\frac24=\frac12,
\qquad
p_X(2)=\frac14.
\]

The three values sum to 1, satisfying the PMF condition.

### Meaning of the result

The random variable groups four outcomes into three values. Adding the probabilities of outcomes in each group gives the distribution.

## Example 2. Interval probability for a continuous uniform distribution

Let $X$ be uniform on $[0,1]$, with

\[
f_X(x)=
\begin{cases}
1,&0\le x\le1,\\
0,&\text{otherwise}
\end{cases}
\]

Then

\[
P(0.2\le X\le0.5)
=\int_{0.2}^{0.5}1\,dx
=0.3
\]

In contrast, $P(X=0.2)=0$. Do not read density $f_X(0.2)=1$ as point probability.

## Example 3. Obtain marginals from a joint distribution

Suppose two discrete random variables have this joint PMF.

| $p_{X,Y}(x,y)$ | $Y=0$ | $Y=1$ |
|---|---:|---:|
| $X=0$ | 0.30 | 0.20 |
| $X=1$ | 0.10 | 0.40 |

Sum each row and column:

\[
p_X(0)=0.30+0.20=0.50,
\qquad
p_X(1)=0.10+0.40=0.50,
\]

\[
p_Y(0)=0.30+0.10=0.40,
\qquad
p_Y(1)=0.20+0.40=0.60
\]

Also,

\[
P(Y=1\mid X=1)=\frac{0.40}{0.50}=0.80
\]

## Example 4. Read a model's predictive distribution

A three-class classifier outputs

\[
p_\theta(y\mid x)=(0.10,0.65,0.25)
\]

for observed input $x$. This is the model-specified conditional distribution over the three possible values of label random variable $Y$. The argmax prediction is the second class, with probability $0.65$. The vector alone does not determine the actual observed label $y$.

## Common misconceptions

### Misconception 1. A random variable is an unknown whose value changes randomly

A random variable is a function mapping outcomes to values. Once an outcome is specified, its function value is determined. A distribution represents the uncertainty about which outcome will be observed.

### Misconception 2. $X$ and $x$ differ only in letter case

$X$ is a random variable with possible values and probabilities; $x$ is an observed or specified value. $p_X(x)$ makes both roles visible.

### Misconception 3. Probability density $f_X(x)$ equals $P(X=x)$

A point has probability 0 in a continuous distribution represented by a density. Integrating density over an interval gives probability.

### Misconception 4. Two marginals determine the joint distribution

Joint distributions can have identical marginals but different dependence between variables. Joint probabilities additionally describe how the variables occur together.

### Misconception 5. The class with the largest predicted probability is the actual label

Argmax is the model's prediction with the greatest assigned probability. The actual label is observed in data; agreement between them is evaluated.

## Exercises

### 1. Random variable and observation

Let $X$ count sentence length. One sentence was observed to have 12 tokens. Explain the distinct roles of $X$ and $x=12$.

<details>
<summary>Show solution</summary>

$X$ is a function taking a possible sentence and returning its token count. Together with the sentence distribution, it assigns probabilities to different lengths. $x=12$ is the value observed for one sentence.

</details>

### 2. Check a PMF

Determine whether $p_X(0)=0.2$, $p_X(1)=0.5$, and $p_X(2)=0.4$ form a valid PMF.

<details>
<summary>Show solution</summary>

All values are nonnegative, but their sum is

\[
0.2+0.5+0.4=1.1
\]

Total probability must be 1, so this is not a valid PMF.

</details>

### 3. A random variable's distribution

Let $\omega$ be the outcome of a fair die roll and define

\[
X(\omega)=
\begin{cases}
1,&\omega\text{ is even},\\
0,&\omega\text{ is odd}
\end{cases}
\]

Calculate $p_X(0)$ and $p_X(1)$.

<details>
<summary>Show solution</summary>

The even outcomes are $\{2,4,6\}$ and the odd outcomes are $\{1,3,5\}$. Each set has probability $3/6$, so

\[
p_X(0)=\frac12,
\qquad
p_X(1)=\frac12.
\]

</details>

### 4. Calculate a CDF

Given $p_X(0)=0.2$, $p_X(1)=0.5$, and $p_X(2)=0.3$, calculate $F_X(0)$, $F_X(1)$, and $F_X(1.5)$.

<details>
<summary>Show solution</summary>

\[
F_X(0)=P(X\le0)=0.2,
\]

\[
F_X(1)=P(X\le1)=0.2+0.5=0.7.
\]

The possible values at most $1.5$ are also $0,1$, so $F_X(1.5)=0.7$.

</details>

### 5. Density and point probability

$X$ is uniform on $[0,2]$ with $f_X(x)=1/2$. Calculate $P(0.5\le X\le1.5)$ and $P(X=1)$.

<details>
<summary>Show solution</summary>

The interval has length 1, so

\[
P(0.5\le X\le1.5)
=\int_{0.5}^{1.5}\frac12\,dx
=\frac12.
\]

A point in a continuous distribution has area 0, so $P(X=1)=0$.

</details>

### 6. Joint and marginal distributions

Calculate $p_X(0)$ and $P(Y=1\mid X=0)$ from this joint PMF.

| $p_{X,Y}(x,y)$ | $Y=0$ | $Y=1$ |
|---|---:|---:|
| $X=0$ | 0.15 | 0.35 |
| $X=1$ | 0.25 | 0.25 |

<details>
<summary>Show solution</summary>

Summing the first row gives

\[
p_X(0)=0.15+0.35=0.50.
\]

Therefore,

\[
P(Y=1\mid X=0)=\frac{0.35}{0.50}=0.70.
\]

</details>

### 7. Critique a model claim

A classifier outputs $(0.05,0.90,0.05)$ for one input. Evaluate “the true probability of the second class being correct is 90%, and the model accurately knows its uncertainty.”

<details>
<summary>Show solution</summary>

The vector is the model-specified conditional predictive distribution for that input. The output alone cannot establish that it equals the conditional probability in the actual data-generating distribution. Measure accuracy and calibration on independent evaluation data, and check whether the input distribution differs from the training and evaluation conditions.

</details>

## Lesson summary

- A random variable maps sample-space outcomes to numerical or categorical values.
- Uppercase $X$ is a random variable; lowercase $x$ is a possible or observed value.
- A distribution is obtained by assigning sample-space probability to preimages of value sets.
- A discrete distribution is represented by a PMF, and cumulative probabilities by a CDF.
- A continuous distribution's PDF is integrated over intervals to give probabilities; density values are not point probabilities.
- Summing a joint distribution over one variable gives a marginal distribution.
- A model's predictive distribution must be distinguished from an observed label and the actual data distribution.

## Pass criteria

You pass if you can answer these questions without consulting the material.

- Can you define a random variable as a function and connect it to outcomes?
- Can you distinguish random variable $X$ from observed value $x$?
- Can you construct a PMF from outcome probabilities and check that it sums to 1?
- Can you read and calculate a CDF as $P(X\le x)$?
- Can you distinguish a PDF from a point probability?
- Can you calculate marginal and conditional distributions from a joint PMF?
- Can you limit the claims supported by a model's predictive distribution?

## Next lesson

- [M04-04 Expectation, variance, and covariance](M04-04-expectation-variance-covariance.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] A random variable is defined as a function.
- [x] Uppercase random variables and lowercase observations are distinguished.
- [x] The roles of PMFs, CDFs, and PDFs are distinguished.
- [x] Joint, marginal, and conditional distributions are calculated.
- [x] Small discrete and continuous examples have been checked.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretability claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] No prerequisites outside the stated scope are required implicitly.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
