---
id: "M04-14"
title: "Mutual information"
part: 1
stage: "M04"
status: "complete"
prerequisites:
  - "M04-02"
  - "M04-03"
  - "M04-12"
  - "M04-13"
estimated_time: "145–175 minutes"
---

# M04-14. Mutual information

## Why this lesson matters

Two variables can retain nonlinear dependence even when their correlation is zero. Mutual information compares their joint distribution with the product of their marginal distributions to measure all forms of statistical dependence. It can also be read as the average reduction in one variable's entropy after observing the other.

This concept appears in mutual information between a representation and a label, the data processing inequality describing information loss across layers, and information criteria for feature selection. High mutual information shows dependence. It does not, by itself, establish that a model functionally uses the information or that one variable causes the other.

## Learning objectives

After this lesson, you will be able to:

- Calculate joint entropy and conditional entropy.
- Express mutual information as KL divergence between a joint distribution and the product of its marginals.
- Use mutual information identities expressed as entropy differences.
- Calculate mutual information in independent, exact-copy, and noisy-copy examples.
- Explain symmetry, nonnegativity, and the equality condition for independence.
- Apply the data processing inequality to a representation map.
- Limit model-interpretation claims based on estimated mutual information.

## Prerequisite check

- Prerequisite lesson: [M04-02 Conditional probability and Bayes' rule](M04-02-conditional-probability-bayes-rule.md)
- Prerequisite lesson: [M04-03 Random variables and probability distributions](M04-03-random-variables-distributions.md)
- Prerequisite lesson: [M04-12 Entropy and cross entropy](M04-12-entropy-cross-entropy.md)
- Prerequisite lesson: [M04-13 KL divergence](M04-13-kl-divergence.md)
- Check: Can you distinguish joint, marginal, and conditional distributions?
- Check: Can you explain the condition on distributions under which KL divergence is zero?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions and scope |
|---|---|---|---|
| $\mathrm H(X,Y)$ | `H of X comma Y` | Entropy of the joint distribution | Discrete variables |
| $\mathrm H(X\mid Y)$ | `H of X given Y` | Average uncertainty in $X$ remaining after observing $Y$ | $\ge0$ for discrete variables |
| $I(X;Y)$ | `I of X semicolon Y` | KL divergence between the joint distribution and the marginal product | $\ge0$ |
| $p_Xp_Y$ | `p sub X times p sub Y` | $p_X(x)p_Y(y)$ | Independence model |
| pointwise mutual information | `pointwise mutual information` | Log density ratio for one outcome pair | Can be negative |
| Markov chain | `Markov chain` | Structure in which the two end variables are conditionally independent given the intermediate variable | $X\to Z\to Y$ |

## Core concept 1. Joint entropy measures uncertainty in a pair of variables

The entropy identities in this lesson are calculated for finite discrete random variables. The joint entropy of $X,Y$ is

\[
\mathrm H(X,Y)
=-\sum_{x,y}p_{X,Y}(x,y)
\log p_{X,Y}(x,y)
\]

It treats the pair $(X,Y)$ as a single categorical outcome and calculates its entropy.

Conditional entropy is

\[
\mathrm H(X\mid Y)
=-\sum_{x,y}p_{X,Y}(x,y)
\log p_{X\mid Y}(x\mid y)
\]

This is equivalent to calculating the conditional entropy of $X$ at each $Y=y$ and averaging these values with weights $p_Y(y)$.

\[
\mathrm H(X\mid Y)
=\sum_y p_Y(y)\mathrm H(X\mid Y=y).
\]

For values with $p_Y(y)>0$, substitute $p_{X,Y}(x,y)=p_Y(y)p_{X\mid Y}(x\mid y)$. The resulting expression first calculates entropy under each conditional distribution at $y$, then averages it using the probability $p_Y(y)$ of observing that $y$. Values with $p_Y(y)=0$ are excluded from the average; no undefined conditional probability is evaluated. The entropy at one condition, $\mathrm H(X\mid Y=y)$, is a different quantity from $\mathrm H(X\mid Y)$, which averages over all $y$.

Distinguish the distribution at each conditioning value from the weight used to average those distributions' entropies.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Unconditional and two conditional class distributions have different entropies whose marginal weighted average is conditional entropy](../../figures/assets/M04/M04-14-conditional-entropy-average.svg)
  <figcaption>This constructed joint table is ((0.72,0.08),(0.10,0.10)), with X along rows and Y along columns. Calculate the conditional entropies at Y=0 and Y=1 separately, then average them using the marginals 0.82 and 0.18. Entropy at the rare value Y=1 is higher than the original H(X), but the average H(X∣Y) is lower. A specific conditioning value and the overall average must be distinguished.</figcaption>
</figure>

## Core concept 2. Mutual information measures dependence through KL divergence

If $X$ and $Y$ are independent, their joint distribution factorizes as

\[
p_{X,Y}(x,y)=p_X(x)p_Y(y)
\]

Mutual information is the KL divergence between the actual joint distribution and this independence model.

\[
I(X;Y)
=D_{\mathrm{KL}}
\left(
p_{X,Y}\Vert p_Xp_Y
\right).
\]

Expanding the discrete form gives

\[
I(X;Y)
=\sum_{x,y}p_{X,Y}(x,y)
\log
\frac{p_{X,Y}(x,y)}
{p_X(x)p_Y(y)}.
\]

A pair whose joint probability is greater than the marginal product can make a positive contribution; a pair whose probability is lower can make a negative contribution. Mutual information, the overall average, is nonnegative.

The product $p_X(x)p_Y(y)$ is a joint distribution that sums to 1 over $x,y$. It is a comparison model with the same marginals as the actual joint distribution but with dependence between the two variables removed. If the actual $p_{X,Y}(x,y)>0$, both marginals are positive, so the denominator for that pair is nonzero. On a finite outcome set, this type of support mismatch cannot make MI infinite.

The two joint tables being compared keep the marginals fixed while changing how mass is distributed across pairs.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Noisy copy joint mass table differs from the independent marginal product table while all marginals remain one half](../../figures/assets/M04/M04-14-joint-product.svg)
  <figcaption>This joint table describes a fair bit copied with probability 0.8. Pairs with matching values have mass 0.4, and pairs with different values have mass 0.1. The marginal product on the right assigns 0.25 to every pair. Both tables have the same row and column sums. MI is the KL divergence with the left joint table as the first distribution.</figcaption>
</figure>

## Core concept 3. Pointwise mutual information describes the relation at one pair

The pointwise mutual information (PMI) of an outcome pair $(x,y)$ is

\[
\operatorname{PMI}(x,y)
=\log
\frac{p_{X,Y}(x,y)}
{p_X(x)p_Y(y)}
\]

It is positive when this pair occurs together more often than the independence model predicts and negative when it occurs less often.

Mutual information averages PMI under the joint distribution.

\[
I(X;Y)=\mathbb E_{(X,Y)\sim p_{X,Y}}
[\operatorname{PMI}(X,Y)].
\]

There is no contradiction between a negative individual PMI and nonnegative overall MI.

Compare the sign of PMI and its contribution after weighting by joint probability at the same pair position.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Positive and negative pointwise mutual information values become joint weighted contributions whose sum is nonnegative mutual information](../../figures/assets/M04/M04-14-pmi-weighted-terms.svg)
  <figcaption>In the same noisy-copy table, diagonal pairs have PMI log 1.6≈0.470, while the other pairs have PMI log 0.4≈−0.916. The right table multiplies each value by its joint mass, 0.4 or 0.1. The four contributions sum to approximately 0.193, the MI. Color helps indicate the sign on both sides, and the actual values are written directly in the cells.</figcaption>
</figure>

## Core concept 4. Mutual information is a reduction in entropy

Factorizing the joint distribution using a conditional distribution gives the following identities.

\[
I(X;Y)
=\mathrm H(X)-\mathrm H(X\mid Y)
\]

\[
=\mathrm H(Y)-\mathrm H(Y\mid X)
\]

\[
=\mathrm H(X)+\mathrm H(Y)-\mathrm H(X,Y).
\]

The first expression gives the average reduction in the uncertainty of $X$ after observing $Y$. The second expression implies symmetry:

\[
I(X;Y)=I(Y;X)
\]

To derive the first identity, use $p_{X,Y}(x,y)=p_Y(y)p_{X\mid Y}(x\mid y)$ to rewrite the log ratio as $\log p_{X\mid Y}(x\mid y)-\log p_X(x)$. The joint average of the first logarithm is $-\mathrm H(X\mid Y)$. Summing over $y$ in the second logarithm leaves $p_X(x)$, so the negative of its average is $\mathrm H(X)$. Combining the two terms gives the first identity.

Putting the logarithm of the same multiplication rule into the joint entropy gives $\mathrm H(X,Y)=\mathrm H(Y)+\mathrm H(X\mid Y)$. This separates the uncertainty of the pair into the uncertainty of $Y$ itself and the uncertainty remaining in $X$ after knowing $Y$. Substitution also gives the third identity. The entropy reduction is an average over all observations of $Y$. It does not mean that the conditional entropy at a specific observed $y$ must always be lower than the original entropy.

Decomposing the two marginal entropies and the joint entropy on the same information scale identifies the corresponding terms in these identities.

<figure class="lesson-figure" markdown="1">
  ![Joint and marginal entropy bars decompose into two conditional entropies and shared mutual information for a noisy copy](../../figures/assets/M04/M04-14-entropy-identity.svg)
  <figcaption>For a fair bit copied with probability 0.8, H(X)=H(Y)=log 2, and both conditional entropies are approximately 0.500. The purple interval, approximately 0.193, is MI. The joint bar is the sum of conditional X, MI, and conditional Y. The horizontal starting position of the H(Y) bar aligns corresponding intervals; its total entropy is the sum of the lengths of its colored intervals.</figcaption>
</figure>

## Core concept 5. MI is zero exactly when the variables are independent

Nonnegativity of KL divergence gives

\[
I(X;Y)\ge0
\]

For discrete variables, if

\[
I(X;Y)=0
\]

then the joint distribution equals the marginal product, so $X,Y$ are independent. Conversely, independence implies zero MI.

For numerical variables with finite, positive variances, zero correlation means zero covariance. It says that one number—the average product of the two centered values—is zero. It does not say that the entire joint distribution factorizes into independent parts. Zero MI is the stronger condition that the entire joint distribution factorizes. A finite-sample MI estimate close to zero is not proof of population independence; estimator uncertainty must also be considered.

Dependence can remain in the joint distribution even in a nonlinear relation with zero correlation.

<figure class="lesson-figure" markdown="1">
  ![Three equiprobable points with Y equal X squared have zero correlation but positive mutual information](../../figures/assets/M04/M04-14-uncorrelated-dependence.svg)
  <figcaption>This finite distribution assigns probability 1/3 to each of X=−1,0,1, with Y=X². Correlation is zero, but X determines Y, so MI=H(Y)≈0.637 nats. The faint curve shows only the function rule; it does not assign probability mass to intermediate coordinates.</figcaption>
</figure>

## Core concept 6. A deterministic copy carries information equal to the output entropy

If $Y=g(X)$ is a deterministic function, knowing $X$ determines $Y$, so

\[
\mathrm H(Y\mid X)=0.
\]

Therefore,

\[
I(X;Y)=\mathrm H(Y).
\]

If $g$ is a bijection, $X$ and $Y$ determine each other, so

\[
I(X;Y)=\mathrm H(X)=\mathrm H(Y).
\]

Changing a discrete variable's labels one-to-one does not change MI. This property is useful when comparing information under invertible relabeling of representation coordinates.

A deterministic mapping does not necessarily allow $X$ to be recovered from $Y$. If different $x$ values map to the same $g(x)$, uncertainty about the original $X$ remains after observing $Y$. Thus, even when $\mathrm H(Y\mid X)=0$, $\mathrm H(X\mid Y)$ can be positive. A bijection has no such merging, and both conditional entropies are zero. Preserving information is also distinct from having identical coordinate values or identical computations.

One-to-one mappings and mappings that merge several values leave different amounts of uncertainty in the reverse direction.

<figure class="lesson-figure" markdown="1">
  ![A bijective relabeling maps three uniform input values to three distinct output labels without losing mutual information](../../figures/assets/M04/M04-14-bijective-relabeling.svg)
  <figcaption>The uniform values X=0,1,2 are simply renamed A,B,C, respectively. Knowing Y uniquely determines X, so both entropies and MI equal log 3. Labels do not need identical values for information to be preserved.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">
  ![Four uniform input values merge into parity labels leaving one bit of input ambiguity despite a deterministic output](../../figures/assets/M04/M04-14-many-to-one-mapping.svg)
  <figcaption>This deterministic mapping retains only the parity of uniform X=0,1,2,3. Knowing X determines Y, but observing even does not distinguish 0 from 2. I(X;Y)=H(Y)=log 2, and H(X∣Y)=log 2 remains.</figcaption>
</figure>

## Core concept 7. Data processing prevents postprocessing from increasing information

If $X\to Z\to Y$ is a Markov chain, $X$ and $Y$ are conditionally independent given $Z$. The data processing inequality gives

\[
I(X;Y)\le I(X;Z)
\]

Producing $Y$ through further computation on $Z$ cannot create new information about $X$.

If a representation $H=f(X)$ is a deterministic function of the input, its relation to the label $Y$ satisfies

\[
I(Y;H)\le I(Y;X)
\]

Equality and the amount of information loss depend on $f$ and the joint distribution. If a finite-sample estimator violates the inequality, check for estimation error or violated assumptions.

The Markov condition means $p(y\mid x,z)=p(y\mid z)$ for possible $x,z$. Once $Z$ is known, also knowing $X$ cannot change the distribution of the next output. Thus, $Y$ receives no extra information about $X$ through a separate path. The arrows here indicate this conditional structure; they do not, by themselves, establish a causal direction. In the representation example, a fixed $f$ takes only $X$ to produce $H$, so the condition $Y\to X\to H$ holds. If postprocessing also receives an input such as the label, the same assumption does not automatically apply.

Postprocessing that does not separately receive the source cannot add information lost at an earlier stage.

<figure class="lesson-figure" markdown="1">
  ![Two independent noisy fair bit copying stages reduce source mutual information with a total flip probability point three two](../../figures/assets/M04/M04-14-noisy-copy-data-processing.svg)
  <figcaption>The two channels independently flip a bit with probability 0.2 each. Two flips restore the original value, so the final flip probability is 0.8×0.2+0.2×0.8=0.32. Information decreases from I(X;Z)≈0.193 to I(X;Y)≈0.066, and the arrows indicate this conditional channel structure. The figure does not measure causal evidence about a representation.</figcaption>
</figure>

## Core concept 8. High-dimensional MI estimation is sensitive to the estimator

MI in a categorical joint table can be calculated from empirical counts. With few samples and many categories, empty cells and plug-in bias become substantial. For continuous, high-dimensional representations, density estimation, binning, k-nearest-neighbor bounds, and variational bounds have different biases.

High probe accuracy suggests dependence between a representation $H$ and a label $Y$, but does not directly give the exact value of $I(H;Y)$. High MI is also not intervention evidence that the model uses label information in $H$ during its output computation.

In deterministic continuous networks, $I(X;H)$ can be infinite or ill-defined depending on density assumptions and injected noise. Before interpreting an estimator's finite output as an intrinsic property, specify the variables and the noise model.

Even in a small joint table, observed counts cannot be treated as population probabilities.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Two possible four sample count tables from independent fair bits yield different empirical mutual information values despite zero population mutual information](../../figures/assets/M04/M04-14-empirical-mi.svg)
  <figcaption>The population consists of independent fair bits with probability 1/4 for every pair. The middle table is a possible n=4 count table, ((2,0),(0,2)), with empirical MI log 2. When all counts are 1, as on the right, empirical MI is zero. These are constructed possible samples, not an actual sampling experiment or results from a test of population independence.</figcaption>
</figure>

## Example 1. Two independent fair bits

Let $X,Y$ be independent, each with a Bernoulli$(1/2)$ distribution. Every pair has joint probability $1/4$, and every marginal product is also $1/4$.

\[
I(X;Y)
=\sum_{x,y}\frac14\log\frac{1/4}{1/4}
=0.
\]

## Example 2. An exactly copied fair bit

Let $X\sim\operatorname{Bernoulli}(1/2)$ and $Y=X$. The joint distribution assigns $1/2$ to each of $(0,0)$ and $(1,1)$.

\[
\begin{aligned}
I(X;Y)
&=\frac12\log\frac{1/2}{(1/2)(1/2)}
+\frac12\log\frac{1/2}{(1/2)(1/2)}\\
&=\log2
\approx0.693\ \text{nats}.
\end{aligned}
\]

Because $Y$ copies $X$ exactly, MI equals the entropy of a fair bit.

## Example 3. A noisy copy

Let $X$ be a fair bit, and suppose $Y$ copies $X$ with probability $0.8$ and flips it with probability $0.2$. The joint probabilities are

\[
p(0,0)=p(1,1)=0.4,
\qquad
p(0,1)=p(1,0)=0.1
\]

and both marginals are uniform. Therefore,

\[
\begin{aligned}
I(X;Y)
&=2(0.4)\log\frac{0.4}{0.25}
+2(0.1)\log\frac{0.1}{0.25}\\
&=0.8\log1.6+0.2\log0.4\\
&\approx0.193\ \text{nats}.
\end{aligned}
\]

Noise makes MI smaller than $\log2\approx0.693$ for an exact copy.

## Example 4. Using an entropy identity

If $\mathrm H(X)=0.9$, $\mathrm H(Y)=0.8$, and $\mathrm H(X,Y)=1.2$ nats, then

\[
I(X;Y)
=0.9+0.8-1.2
=0.5\ \text{nats}.
\]

Also,

\[
\mathrm H(X\mid Y)
=\mathrm H(X)-I(X;Y)
=0.4\ \text{nats}.
\]

## Common misconceptions

### Misconception 1. MI is another name for correlation

Correlation summarizes a linear relation. MI measures all forms of departure of the joint distribution from the independence model.

### Misconception 2. Both PMI and MI are nonnegative

PMI at an individual pair can be negative. MI averaged under the joint distribution is KL divergence and is therefore nonnegative.

### Misconception 3. High MI means one variable causes the other

MI is a symmetric measure of dependence. It does not determine causal direction or intervention effects.

### Misconception 4. High representation-label MI means the model uses label information

Dependence or decodability must be distinguished from functional use. An intervention is needed to check whether changing the activation changes the output.

### Misconception 5. MI in a neural representation is a fixed number independent of the estimator

The definition of continuous variables, noise, binning, and estimator family affect the result. Finite-sample estimates also have bias and variance.

## Exercises

### 1. Independence and MI

Suppose $p_{X,Y}(x,y)=p_X(x)p_Y(y)$ holds for every pair. Find $I(X;Y)$.

<details>
<summary>Show solution</summary>

Each log ratio is

\[
\log\frac{p_{X,Y}(x,y)}{p_X(x)p_Y(y)}=\log1=0
\]

so $I(X;Y)=0$.

</details>

### 2. An exact copy

$X$ is uniform over three values, and $Y=X$. Find $I(X;Y)$ using the natural logarithm.

<details>
<summary>Show solution</summary>

Since $Y$ is a deterministic copy of $X$,

\[
I(X;Y)=\mathrm H(Y)=\log3\ \text{nats}.
\]

</details>

### 3. An entropy identity

Suppose $\mathrm H(X)=0.7$, $\mathrm H(Y)=0.8$, and $\mathrm H(X,Y)=1.1$ nats. Find $I(X;Y)$.

<details>
<summary>Show solution</summary>

\[
I(X;Y)=0.7+0.8-1.1=0.4\ \text{nats}.
\]

</details>

### 4. Conditional entropy

Suppose $\mathrm H(X)=1.0$ nat and $I(X;Y)=0.35$ nat. Find $\mathrm H(X\mid Y)$.

<details>
<summary>Show solution</summary>

\[
\mathrm H(X\mid Y)
=\mathrm H(X)-I(X;Y)
=1.0-0.35
=0.65\ \text{nat}.
\]

</details>

### 5. A deterministic mapping

$Y=g(X)$ is deterministic, and $\mathrm H(Y)=0.6$ nat. Find $I(X;Y)$.

<details>
<summary>Show solution</summary>

Since $X$ determines $Y$, $\mathrm H(Y\mid X)=0$. Therefore,

\[
I(X;Y)=\mathrm H(Y)-\mathrm H(Y\mid X)=0.6.
\]

</details>

### 6. Data processing

Suppose $Y\to X\to H$ is a Markov chain and $I(Y;X)=0.9$ nat. Determine whether an exact population value of $I(Y;H)=1.1$ nat is possible.

<details>
<summary>Show solution</summary>

The data processing inequality requires

\[
I(Y;H)\le I(Y;X)=0.9
\]

An exact population value of 1.1 is impossible. If an empirical estimate gives this result, check for estimator error or a violated Markov assumption.

</details>

### 7. Critiquing a model-interpretation claim

A study reports high estimated MI between an activation and a concept label, then concludes that “the model uses this concept.” Explain what else should be checked.

<details>
<summary>Show solution</summary>

First check the MI estimator's finite-sample bias, binning and noise settings, and stability on held-out data. High MI indicates statistical dependence, not necessarily functional use. To evaluate the use claim, ablate or patch concept-related activations and measure the relevant output effect alongside controls.

</details>

## Lesson summary

- Joint entropy is uncertainty in a pair of variables; conditional entropy is the average uncertainty remaining after observing one variable.
- Mutual information is KL divergence between the joint distribution and the marginal product.
- Mutual information is a reduction in entropy and is symmetric in $X,Y$.
- For discrete variables, MI is nonnegative and is zero exactly when the variables are independent.
- Under a deterministic mapping, input-output MI equals output entropy.
- The data processing inequality says postprocessing cannot increase information about the source.
- MI estimates in high-dimensional representations are sensitive to the definitions of variables, noise, and estimators, and do not establish functional use.

## Pass criteria

You pass when you can answer these questions without consulting the material:

- Can you define joint and conditional entropy?
- Can you express MI as KL divergence between the joint distribution and the marginal product?
- Can you calculate MI using entropy identities?
- Can you calculate MI in independence, copy, and noisy-copy examples?
- Can you explain symmetry and the equality condition for independence?
- Can you apply the data processing inequality to a representation?
- Can you explain the causal and functional-use claims that an MI estimate does not support?

## Next lesson

- [M04-15 Calibration and scoring rules](M04-15-calibration-scoring-rules.md)

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] Joint and conditional entropy are defined.
- [x] MI's KL and entropy identities are explained.
- [x] Independence, copy, and noise examples are checked.
- [x] The data processing inequality is applied.
- [x] Limits of MI estimation and model interpretation are stated.
- [x] Every exercise has a solution.
- [x] Strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and math delimiters are checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
