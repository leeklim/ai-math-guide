---
id: "A09-LRN-05"
title: "Rademacher complexity"
part: 4
stage: "A09-LRN"
status: "complete"
prerequisites: ["A09-LRN-03", "M04-04"]
estimated_time: "90–120 minutes"
---

# A09-LRN-05. Rademacher complexity

## Why this lesson matters

VC dimension describes a class's worst-case combinatorial capacity but does not account for the geometry of the actual sample. Empirical Rademacher complexity measures a function class's data-dependent richness by how well it can fit random signs on a given sample.

## Learning objectives

- Explain each source of randomness in empirical Rademacher complexity.
- Calculate its value for a small finite class.
- Explain the roles of contraction and norm constraints.
- Distinguish random-label controls from learning-theory complexity.

## Prerequisite check

- Prerequisite lessons: [A09-LRN-03 Generalization gap](A09-LRN-03-generalization-gap.md), [M04-04 Expectation, variance, and covariance](../../part-1-foundations/M04/M04-04-expectation-variance-covariance.md)
- Check question: What are the mean and variance of an independent random sign?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $\sigma_i$ | `sigma sub i` | independent Rademacher sign | $\{-1,+1\}$ |
| $\hat{\mathfrak R}_S(\mathcal F)$ | `the empirical Rademacher complexity of F on S` | sample-dependent complexity | nonnegative scalar |
| $\sup_{f\in\mathcal F}$ | `the supremum over f in F` | Function that best fits the random signs | operator |
| $B$ | `B` | norm bound | positive scalar |

## Core concepts

### Fix the sample and repeat the signs

Fix a sample $S=(x_1,\ldots,x_n)$ and a real-valued function class $\mathcal F$. Each $\sigma_i$ is an independent random sign, taking $+1,-1$ with equal probability. These signs are random variables introduced by the complexity definition, distinct from training labels or optimizer seeds. Empirical Rademacher complexity is defined as

$$
\hat{\mathfrak R}_S(\mathcal F)
=E_\sigma\left[\sup_{f\in\mathcal F}
\frac1n\sum_{i=1}^n\sigma_i f(x_i)\right].
$$

First draw one sign vector, then find the function in the class that makes $\sum_i\sigma_i f(x_i)/n$ largest for those signs. Average that supremum over sign vectors. Because function selection may adapt to the signs, the order of $E_\sigma[\sup_f]$ and $\sup_f E_\sigma$ cannot be reversed. For each $f$ fixed in advance, the sign average is 0, but the value obtained by choosing the best $f$ after seeing the signs is generally not 0.

This lesson uses a convention with no absolute value in the sum and normalization by $1/n$. Match definitions when comparing numbers with sources that use an absolute value or $2/n$. Assuming a nonempty class and a finite expectation, the supremum includes the value for any fixed function, so its sign average is at least 0. Empirical means that $S$ is fixed; distinguish this from expected Rademacher complexity, which also averages over resampled $S$.

Read the two averaging and selection routes side by side to locate where function selection depends on the signs.

<figure class="lesson-figure" markdown="1">

![Two vertical routes contrast adapting the function to each sign before averaging with fixing the function before sign averaging.](../../figures/assets/A09-LRN/A09-LRN-05-expectation-supremum-order.svg)

<figcaption>Both routes use the same sample and the same {f,−f}. The upper route changes the function after observing the signs; the lower route fixes each function first. The two calculations are generally unequal.</figcaption>

</figure>

### How a norm constraint bounds the supremum

For the bounded linear class $f_w(x)=w^\top x$, $\|w\|\le B$, the sign sum is $w^\top\sum_i\sigma_i x_i/n$. For fixed signs, aligning $w$ with this sum can increase the value, but the norm constraint prevents its magnitude from growing without limit. For a general norm, the dual norm gives the largest inner product over the unit ball. With the Euclidean norm, Cauchy–Schwarz and a choice of $w$ in the same direction give

$$
\hat{\mathfrak R}_S(\mathcal F)
=\frac Bn E_\sigma\left\|\sum_i\sigma_i x_i\right\|_2
\le\frac Bn\sqrt{\sum_i\|x_i\|_2^2}
$$

The final upper bound uses the fact that cross terms involving different signs have mean 0 in the expectation of the squared norm. If all input norms are at most $C$, the upper bound is $BC/\sqrt n$. Input scale changes the value as well as weight magnitude, so feature scaling must be specified. If at least one $x_i$ differs from 0 and $w$ is unrestricted, the supremum can grow without limit for some sign vectors, so the complexity is not finite.

Directional alignment in the Euclidean ball, sample geometry, and changes in norm bounds address different questions. Examine them separately in the following figures.

<figure class="lesson-figure" markdown="1">

![A Euclidean unit circle constrains the weight vector to align with a sign sum at coordinates two and one.](../../figures/assets/A09-LRN/A09-LRN-05-unit-ball-sign-alignment.svg)

<figcaption>For the illustrative sign sum s=(2,1) and B=1, the optimal weight is s/‖s‖₂=(2/√5,1/√5), and the largest inner product is √5. The geometry allows the weight to grow in the direction of s but not beyond the unit ball. Complexity divides this maximum by n and averages over signs.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Possible sign sums for two aligned unit inputs and two orthogonal unit inputs yield complexities one half and square root two over two.](../../figures/assets/A09-LRN/A09-LRN-05-equal-norm-different-geometry.svg)

<figcaption>This illustrative example fixes B=1, n=2, and input norms of 1. For two aligned inputs, the mean norm of the sign sum is 1, giving complexity 1/2. For orthogonal inputs, every sum has norm √2, giving √2/2. Their common upper bound is 1/√2, which also distinguishes the bound from the actual value.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![The bound B C over square root n falls with sample size and doubles if either the weight or input norm bound doubles.](../../figures/assets/A09-LRN/A09-LRN-05-norm-scale-sample-bound.svg)

<figcaption>The curves show the upper bound BC/√n from the text, not estimates of actual complexity. Doubling B or C doubles the bound at the same n. When increasing n, keep the class and norm conditions unchanged.</figcaption>

</figure>

### From the predictor class to the loss class

Controlling risk generalization requires not only prediction functions but also the class of loss functions $(x,y)\mapsto\ell(f(x),y)$. With each label $y_i$ fixed, if the loss is $L$-Lipschitz in its prediction argument, a difference between two predictions can increase by at most a factor of $L$ in the loss. The contraction inequality applies this restriction to the random-sign supremum, controlling the loss class's empirical complexity by $L$ times the predictor class's complexity. This uses the no-absolute-value convention in this lesson; verify the Lipschitz condition for the loss and prediction range in use. Squared loss is not globally Lipschitz without restrictions on predictions and labels.

A complexity value alone does not give a risk bound for any arbitrary loss. Check conditions such as boundedness needed for concentration, the sample's i.i.d. assumption, and how the class was specified. If the class is selected using the same sample, a theorem for a fixed class may no longer apply directly.

Before passing to the loss class, check the prediction range on which the Lipschitz condition holds.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Squared loss with label zero and its absolute slope show a slope bound two only within the prediction interval minus one to one.](../../figures/assets/A09-LRN/A09-LRN-05-squared-loss-bounded-slope.svg)

<figcaption>For squared loss t² with label 0 fixed, the slope magnitude is at most 2 on the prediction range [−1,1]. The same L=2 cannot be used unchanged outside that range, and the global slope is unbounded. This figure checks a condition needed before contraction; it does not prove a risk bound.</figcaption>

</figure>

### How this differs from learning random labels

A random-label control randomizes labels, runs an actual optimizer, regularization, and selection pipeline, and measures performance. Rademacher complexity averages the supremum over the entire specified class for each sign vector, not the function found by a particular training algorithm. An actual optimizer may not reach that optimum, and accuracy and sign-weighted real output use different measurement scales. Random-label accuracy is therefore an empirical control for a pipeline's ability to memorize, not an estimate of the same value as the complexity.

Compare what is selected and averaged in the theoretical definition and the empirical control.

<figure class="lesson-figure" markdown="1">

![Separate vertical pipelines distinguish a mathematical class supremum from running an actual optimizer on randomized labels.](../../figures/assets/A09-LRN/A09-LRN-05-class-supremum-pipeline-control.svg)

<figcaption>The supremum over the entire class and the result found by an actual optimizer are different selection targets. The expected sign-weighted real score and random-label accuracy are also different quantities, so do not read the empirical control as the same value as theoretical complexity.</figcaption>

</figure>

## Small example

If $\mathcal F=\{f,-f\}$, the supremum for fixed signs is $|n^{-1}\sum_i\sigma_if(x_i)|$, and we take its sign expectation.

Consider two points with $f(x_1)=f(x_2)=1$. When the signs are $(+,+)$ or $(-,-)$, choosing one of the two functions gives an average of 1. For $(+,-)$ or $(-,+)$, the sum is 0. The four cases are equally probable, so the complexity is $(1+1+0+0)/4=1/2$. The absolute value here comes from selecting the larger value between $f$ and $-f$, not from adding it to the original definition.

Calculate each function's score and the score after selection for all four sign cases.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Sign-weighted scores for f and minus f followed by the per-sign maximum and its mean one half.](../../figures/assets/A09-LRN/A09-LRN-05-finite-sign-suprema.svg)

<figcaption>All four sign vectors are calculated for f(x₁)=f(x₂)=1 from the text. Each fixed function has mean score 0, but choosing the larger value for each sign vector and then averaging gives 1/2. The absolute value results from choosing between ±f.</figcaption>

</figure>

## Common misconceptions

- Empirical Rademacher complexity is not accuracy obtained by randomizing training labels.
- An unconstrained real-valued linear class can increase scale without limit, leaving no useful finite bound.

## Exercises

### 1. Singleton class
If $\mathcal F=\{f_0\}$ and $f_0(x)=0$, what is the complexity?
<details><summary>Show solution</summary>

Every sign sum is 0, so the complexity is 0.
</details>

### 2. Constant pair
If $n=1$, $\mathcal F=\{f_+,f_-\}$, $f_+(x)=1$, and $f_-(x)=-1$, what is the complexity?
<details><summary>Show solution</summary>

For either sign, selecting the matching constant gives supremum 1, so the expectation is also 1.
</details>

### 3. Norm constraint
How does the standard upper bound change if the weight norm bound of the linear class is doubled?
<details><summary>Show solution</summary>

With other conditions unchanged, it doubles because it is linear in $B$.
</details>

### 4. Probe control
When random-label accuracy and a Rademacher bound are used together, what does each tell us?
<details><summary>Show solution</summary>

Random-label accuracy controls for memorization by the actual pipeline. A Rademacher bound theoretically controls the specified class and sample's capacity for uniform deviation.
</details>

## Evidence and update boundaries

Empirical Rademacher complexity and contraction follow standard learning-theory definitions. This lesson does not compare the latest norm-based bounds for deep networks.

- [Cornell CS4783 Lecture 6, §§2–3](https://www.cs.cornell.edu/courses/cs4783/2022sp/notes06.pdf): Used to check Lipschitz contraction and the calculation for a linear class with a Euclidean norm constraint. Distinguish each source's absolute-value convention from the definition in the text.
- [UBC CPSC532D Rademacher complexity, §3.1](https://www.cs.ubc.ca/~dsuth/532D/23w1/notes/5-rademacher.pdf): Used to check coordinatewise Lipschitz contraction under the same no-absolute-value convention as the text.

## Lesson summary

- Rademacher complexity measures the ability to fit random signs on a sample.
- Distinguish the supremum from the sign expectation.
- Norm constraints and input geometry yield finite bounds.
- Do not treat random-label experiments and theoretical complexity as the same value.

## Pass criteria

- Can you calculate empirical complexity for a small function class?
- Can you explain the roles of norm bounds and random-label controls?

## Next lesson

- [A09-LRN-06 PAC learning](A09-LRN-06-pac-learning.md)

## Author checklist

- [x] Rademacher randomness and the supremum are distinguished.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
