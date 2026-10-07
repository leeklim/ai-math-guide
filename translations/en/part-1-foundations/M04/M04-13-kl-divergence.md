---
id: "M04-13"
title: "KL divergence"
part: 1
stage: "M04"
status: "complete"
prerequisites:
  - "M04-03"
  - "M04-11"
  - "M04-12"
estimated_time: "140–165 minutes"
---

# M04-13. KL divergence

## Why this lesson matters

Cross entropy evaluates outcomes from target distribution $p$ using model distribution $q$. Subtracting the target's own entropy leaves the additional log-loss due to $q$ differing from $p$. This difference is Kullback-Leibler divergence (KL divergence).

KL divergence appears in maximum likelihood, variational inference, knowledge distillation, and representation-distribution comparisons. Reversing its direction changes the averaging distribution and the support mismatch receiving a strong penalty. Without symmetry or the triangle inequality, it cannot be interpreted as Euclidean distance.

## Learning objectives

After completing this lesson, you should be able to:

- Read KL-divergence formulas for discrete and continuous distributions.
- Distinguish the averaging and evaluation distributions in $D_{\mathrm{KL}}(p\Vert q)$.
- Calculate KL divergence for small categorical and Bernoulli distributions.
- Explain KL nonnegativity and the conditions for zero divergence.
- Check asymmetry and support mismatch using examples.
- Use the relationship between cross entropy, entropy, and KL divergence.
- Determine whether small output KL guarantees identical model internals or causal mechanisms.

## Prerequisite check

- Prerequisite lesson: [M04-03 Random variables and probability distributions](M04-03-random-variables-distributions.md)
- Prerequisite lesson: [M04-11 Likelihood and maximum likelihood estimation](M04-11-likelihood-maximum-likelihood.md)
- Prerequisite lesson: [M04-12 Entropy and cross entropy](M04-12-entropy-cross-entropy.md)
- Check: Can you explain which distribution averages and which supplies log-probabilities in $\mathrm H(p,q)$?
- Check: Can you explain what happens when negative log is applied to probability 0?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| $D_{\mathrm{KL}}(p\Vert q)$ | `K L divergence from p to q` | Log density ratio averaged under $p$ | Directional |
| $\log\frac{p(x)}{q(x)}$ | `log of p of x over q of x` | Relative log-density of $p$ and $q$ at outcome $x$ | $p(x),q(x)>0$ |
| absolute continuity | `absolute continuity` | Every event assigned probability 0 by $q$ also has probability 0 under $p$ | $p\ll q$ |
| forward KL | `forward KL` | $D_{\mathrm{KL}}(p\Vert q)$ with target $p$ first | Check the naming convention in context |
| reverse KL | `reverse KL` | $D_{\mathrm{KL}}(q\Vert p)$ with approximation $q$ first | Check the naming convention in context |

## Core concept 1. KL divergence is expected log density ratio

For discrete distributions $p,q$ on the same finite outcome set, define

\[
D_{\mathrm{KL}}(p\Vert q)
=\sum_x p(x)
\log\frac{p(x)}{q(x)}
\]

In expectation notation,

\[
D_{\mathrm{KL}}(p\Vert q)
=\mathbb E_{X\sim p}
\left[
\log\frac{p(X)}{q(X)}
\right]
\]

Draw outcomes from $p$ and calculate the difference between $p$ and $q$ log-probabilities at each outcome.

For continuous densities, replace the sum with an integral:

\[
D_{\mathrm{KL}}(p\Vert q)
=\int p(x)
\log\frac{p(x)}{q(x)}\,dx.
\]

Natural logarithms give units of nats.

The log ratio is $\log p(x)-\log q(x)$. If $q(x)$ is smaller than $p(x)$, that outcome's term is positive; if larger, the term can be negative. KL nonnegativity concerns the total weighted sum under $p$, not a claim that every outcome's term is positive. Below, terms with $p(x)=0$ are treated as 0, while $p(x)>0$ with $q(x)=0$ is considered separately.

Separating individual log ratios from their weighted sum distinguishes negative terms from nonnegative total KL.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Categorical masses signed log ratios and weighted forward and reverse KL terms with different positive sums](../../figures/assets/M04/M04-13-signed-contributions.svg)
  <figcaption>This calculates p=(0.5,0.5), q=(0.75,0.25). Upper-right log ratios are negative at the first outcome and positive at the second. Lower contributions use the first distribution's weights, summing to about 0.144 and 0.131 nats in the respective directions. Reversing direction changes the averaging weights as well as log-ratio signs.</figcaption>
</figure>

## Core concept 2. The first distribution determines averaging and important regions

Each term in $D_{\mathrm{KL}}(p\Vert q)$ uses weight $p(x)$. Small $q(x)$ at an outcome receiving substantial probability from $p$ produces a large penalty. Outcomes with $p(x)=0$ make no direct contribution under the convention $0\log(0/q)=0$.

Omitting direction $p\Vert q$ hides which regions' errors are emphasized. State the direction when referring to “the KL of two distributions.”

## Core concept 3. Support mismatch can make KL infinite

If an outcome $x$ in a finite discrete distribution has

\[
p(x)>0,
\qquad q(x)=0
\]

use the convention

\[
p(x)\log\frac{p(x)}{q(x)}=+\infty
\]

Then $D_{\mathrm{KL}}(p\Vert q)=+\infty$, because $q$ assigns zero probability to an outcome possible under $p$.

For finite discrete distributions, finite KL requires $q$ to be positive at every outcome where $p$ is positive. In event terms, every event with probability 0 under $q$ must also have probability 0 under $p$. Measure theory calls this absolute continuity of $p$ with respect to $q$, written $p\ll q$.

For continuous densities, changing a density at one point need not change the distribution or integral. Do not conclude that KL is infinite solely because $p(x)>0,q(x)=0$ at one point. A problem occurs when the entire region where $q=0$ receives positive probability under $p$. Even with absolute continuity, a divergent log-ratio integral can give infinite KL. Distinguish support conditions from integrability.

As a small positive probability approaches 0, the two KL directions behave differently.

<figure class="lesson-figure" markdown="1">
  ![Forward KL diverges as model probability on a positive target outcome shrinks while reverse KL approaches log two](../../figures/assets/M04/M04-13-support-direction.svg)
  <figcaption>For p=(0.5,0.5) and q=(1−ε,ε), the second model mass ε decreases on a logarithmic horizontal scale. At ε=0, forward KL is infinite and reverse KL is log 2. The finite leftmost curve value corresponds to ε=10⁻⁶, not infinity represented at a finite height.</figcaption>
</figure>

For continuous distributions, distinguish changing density at a single point from omitting a region of positive probability.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Changing uniform density at a single null point leaves the distribution unchanged but deleting a positive mass interval causes infinite forward KL](../../figures/assets/M04/M04-13-null-point-positive-region.svg)
  <figcaption>On the left, the uniform [0,1] density is set to 0 only at x=0.5. The open point is the original height and the filled point is the changed value; all event probabilities stay unchanged. On the right, q is uniform on [0,0.5], omitting the entire interval (0.5,1] to which p assigns probability 1/2. Forward KL is infinite in that case.</figcaption>
</figure>

## Core concept 4. KL divergence is nonnegative and zero for identical distributions

Gibbs' inequality gives

\[
D_{\mathrm{KL}}(p\Vert q)\ge0
\]

If $p,q$ have the same support and $p=q$, each log ratio is $\log1=0$, so KL is 0.

A short nonnegativity check uses $-\log u\ge1-u$. On terms with $p(x)>0$, set $u=q(x)/p(x)$:

\[
\begin{aligned}
D_{\mathrm{KL}}(p\Vert q)
&=\sum_x p(x)
\left[-\log\frac{q(x)}{p(x)}\right]\\
&\ge\sum_x p(x)
\left[1-\frac{q(x)}{p(x)}\right]\\
&=1-\sum_{x:p(x)>0}q(x)\\
&\ge0
\end{aligned}
\]

On a common positive support, the final sum is 1.

The inequality is equivalent to $u-1-\log u\ge0$. For $u>0$, its derivative is $1-1/u$, so the expression decreases for $u<1$, increases for $u>1$, and has minimum 0 at $u=1$. Equality therefore occurs only at $u=1$. For equality throughout the KL calculation, $q(x)/p(x)=1$ must hold at every outcome with $p(x)>0$. The $q$ masses at these outcomes already sum to 1, leaving no mass for the remaining outcomes. For finite discrete distributions, KL is 0 only when probabilities agree at all outcomes. For continuous distributions, equality means equal densities almost everywhere, disregarding differences that do not affect the integral.

On the same $K$-outcome set, let $q(x)=1/K$. Then

\[
D_{\mathrm{KL}}(p\Vert q)
=\sum_x p(x)\log p(x)+\log K
=\log K-\mathrm H(p)\ge0
\]

Thus $\mathrm H(p)\le\log K$, with equality at $p=q$. This justifies the uniform entropy maximum in M04-12.

The logarithmic inequality used in Gibbs' inequality can be checked by where two curves meet.

<figure class="lesson-figure" markdown="1">
  ![Negative logarithm lies above its supporting line one minus u with equality only at ratio one](../../figures/assets/M04/M04-13-log-inequality.svg)
  <figcaption>For u&gt;0, −log u never falls below 1−u, meeting it only at u=1. The text substitutes u=q/p at each positive-p outcome and takes the p-weighted sum to obtain nonnegativity and equality conditions.</figcaption>
</figure>

## Core concept 5. KL divergence is not a symmetric distance

In general,

\[
D_{\mathrm{KL}}(p\Vert q)
\ne
D_{\mathrm{KL}}(q\Vert p).
\]

The first direction measures how low $q$ evaluates outcomes frequent under $p$. The reverse evaluates $p$ at outcomes frequent under $q$. Changing the averaging distribution changes the value.

KL also fails the triangle inequality, so it must not be called a metric distance between distributions. Nonnegativity and zero divergence for identical distributions alone do not make it a metric.

Separate from asymmetry, a small Bernoulli example also violates the triangle inequality.

<figure class="lesson-figure" markdown="1">
  ![Bernoulli KL from p to r exceeds the sum of KL from p to q and q to r](../../figures/assets/M04/M04-13-triangle-failure.svg)
  <figcaption>For p=Bernoulli(0.1), q=Bernoulli(0.5), r=Bernoulli(0.9), KL(p∥r)≈1.758 exceeds KL(p∥q)+KL(q∥r)≈0.879, violating a metric's triangle inequality. Bar lengths are KL values, not Euclidean distances between distributions.</figcaption>
</figure>

## Core concept 6. Cross entropy is entropy plus KL divergence

Expanding cross entropy gives

\[
\begin{aligned}
\mathrm H(p,q)
&=-\sum_x p(x)\log q(x)\\
&=-\sum_x p(x)\log p(x)
+\sum_x p(x)\log\frac{p(x)}{q(x)}\\
&=\mathrm H(p)+D_{\mathrm{KL}}(p\Vert q).
\end{aligned}
\]

With target $p$ fixed, $\mathrm H(p)$ is fixed too. Minimizing cross entropy over $q_\theta$ has the same optimizer as minimizing $D_{\mathrm{KL}}(p\Vert q_\theta)$.

In a discrete model, use the proportion of observed indices whose value is $x$ as empirical distribution $\widehat p_n(x)$. Grouping log-loss terms for observations with the same value gives

\[
\mathrm H(\widehat p_n,q_\theta)
=-\sum_x\widehat p_n(x)\log q_\theta(x)
=-\frac1n\sum_{i=1}^{n}\log q_\theta(x_i)
\]

This is M04-11's mean NLL, connecting MLE to empirical cross-entropy minimization. Mean NLL can also be calculated on continuous-model observations, but do not treat a point-mass empirical distribution as a continuous density and directly insert it into the discrete KL formula above.

Grouping observed log-loss by outcome reveals empirical-distribution weights.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Four observed categorical losses regroup by empirical frequencies into cross entropy and its entropy plus KL decomposition](../../figures/assets/M04/M04-13-empirical-loss-grouping.svg)
  <figcaption>For observations A,A,A,B and model probabilities 0.5 each, mean loss equals cross entropy weighted by frequencies 3/4 and 1/4. About 0.693 nats decomposes into empirical-target entropy about 0.562 and KL about 0.131. This is a discrete-mass calculation.</figcaption>
</figure>

## Core concept 7. KL direction changes approximation behavior

Suppose target $p$ has several separated modes. $D_{\mathrm{KL}}(p\Vert q)$ penalizes low probability from $q$ at each $p$ mode, creating pressure to cover multiple modes.

$D_{\mathrm{KL}}(q\Vert p)$ penalizes low $p$ where $q$ places probability. In a restricted approximation family, solutions can concentrate $q$ on one mode of $p$. “Mode-covering” and “mode-seeking” summarize these tendencies; actual outcomes depend on the distribution family and optimization.

Restricting the approximation family to one Gaussian can produce different directional results for the same target.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![A two mode Gaussian mixture is covered by the exact forward KL Gaussian while a reverse KL finite grid candidate concentrates on one mode](../../figures/assets/M04/M04-13-restricted-gaussian-approximation.svg)
  <figcaption>The target is an equal-weight mixture of Gaussians with means −3 and 3 and standard deviation 0.7. The left is the exact forward-KL minimum in the single-Gaussian family, covering both modes. The right is the candidate with lowest numerically integrated KL on the specified finite μ–σ grid, concentrating on one mode. The example does not guarantee mode-covering or mode-seeking in every family.</figcaption>
</figure>

## Core concept 8. Output KL does not determine internal representation differences

A distillation loss for teacher $p_T(y\mid x)$ and student $p_S(y\mid x)$ can use

\[
D_{\mathrm{KL}}(p_T\Vert p_S)
\]

A small value indicates close output distributions at the evaluated inputs.

Different hidden dimensions, bases, and computation graphs can produce the same output distribution. Output KL alone cannot establish hidden-representation alignment or identical reasoning mechanisms. Changing the input distribution or temperature can also change measured KL.

Calculating output equality does not uniquely determine hidden coordinates.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Two different hidden coordinate vectors yield the same summed score sigmoid output and zero output KL](../../figures/assets/M04/M04-13-same-output-different-hidden.svg)
  <figcaption>In the two constructed models, hidden coordinates (1,2) and (2,1) differ but their summed scores are both 3. Identical sigmoid outputs give output KL 0 at this input. This calculation does not establish hidden-coordinate correspondence or identical internal circuits.</figcaption>
</figure>

## Example 1. Calculate KL for two binary distributions

### Problem

Given $p=(0.5,0.5)$ and $q=(0.75,0.25)$, calculate $D_{\mathrm{KL}}(p\Vert q)$.

### Solution

\[
\begin{aligned}
D_{\mathrm{KL}}(p\Vert q)
&=0.5\log\frac{0.5}{0.75}
+0.5\log\frac{0.5}{0.25}\\
&=0.5\log\frac23+0.5\log2\\
&=0.5\log\frac43\\
&\approx0.144\ \text{nats}.
\end{aligned}
\]

### Meaning of the result

Averaging $p$'s two outcomes equally, using $q$ introduces additional log-loss of about $0.144$ nats.

## Example 2. Reverse the KL direction

For the same distributions,

\[
\begin{aligned}
D_{\mathrm{KL}}(q\Vert p)
&=0.75\log\frac{0.75}{0.5}
+0.25\log\frac{0.25}{0.5}\\
&=0.75\log1.5+0.25\log0.5\\
&\approx0.131\ \text{nats}.
\end{aligned}
\]

The directional values $0.144$ and $0.131$ differ.

## Example 3. Support mismatch

For $p=(0.5,0.5)$ and $q=(1,0)$, the second outcome has $p_2>0$ and $q_2=0$, giving

\[
D_{\mathrm{KL}}(p\Vert q)=+\infty.
\]

In the reverse direction,

\[
D_{\mathrm{KL}}(q\Vert p)
=1\log\frac1{0.5}
=\log2
\]

Direction changes how support mismatch is evaluated.

## Example 4. Obtain KL from cross entropy

If $\mathrm H(p)=0.50$ nats and $\mathrm H(p,q)=0.65$ nats,

\[
D_{\mathrm{KL}}(p\Vert q)
=\mathrm H(p,q)-\mathrm H(p)
=0.15\ \text{nats}
\]

## Common misconceptions

### Misconception 1. KL divergence is a distance between two distributions

KL is asymmetric and fails the triangle inequality. Call it a directional divergence.

### Misconception 2. $D_{\mathrm{KL}}(p\Vert q)$ and $D_{\mathrm{KL}}(q\Vert p)$ play similar roles

They average under different distributions. Their penalties for support mismatch and modes differ too.

### Misconception 3. Small KL means small probability differences at each outcome

KL is a log ratio averaged with $p$ weights. Large pointwise differences in low-probability regions can receive little weight in the average. Check errors separately in regions of interest.

### Misconception 4. KL estimated from a finite sample is exact population KL

Empirical probabilities and density estimators have sampling error and estimation bias. High-dimensional continuous KL estimation is sensitive to estimator choice.

### Misconception 5. Small teacher-student output KL means identical knowledge

Close output behavior is a result for the evaluated inputs and temperature. Hidden representations, causal circuits, and behavior under distribution shift require further analysis.

## Exercises

### 1. Read the direction

Explain which distribution averages outcomes in $D_{\mathrm{KL}}(p\Vert q)$ and which enters as the comparison distribution.

<details>
<summary>Show solution</summary>

Outcomes are averaged under $p$. The log ratio $p(x)/q(x)$ is calculated at each outcome, measuring how low $q$ evaluates $p$'s outcomes.

</details>

### 2. Categorical KL

Given $p=(0.5,0.5)$ and $q=(0.25,0.75)$, write $D_{\mathrm{KL}}(p\Vert q)$ and calculate an approximation.

<details>
<summary>Show solution</summary>

\[
\begin{aligned}
D_{\mathrm{KL}}(p\Vert q)
&=0.5\log2+0.5\log\frac23\\
&=0.5\log\frac43\\
&\approx0.144.
\end{aligned}
\]

</details>

### 3. Asymmetry

For $p=(0.9,0.1)$ and $q=(0.5,0.5)$, write both directional KL formulas. Without numerical calculation, explain why their forms differ.

<details>
<summary>Show solution</summary>

\[
D_{\mathrm{KL}}(p\Vert q)
=0.9\log\frac{0.9}{0.5}
+0.1\log\frac{0.1}{0.5},
\]

\[
D_{\mathrm{KL}}(q\Vert p)
=0.5\log\frac{0.5}{0.9}
+0.5\log\frac{0.5}{0.1}.
\]

The first uses $p$ weights $0.9,0.1$; the second uses $q$ weights $0.5,0.5$.

</details>

### 4. Support condition

Determine $D_{\mathrm{KL}}(p\Vert q)$ for $p=(0.2,0.8)$ and $q=(0,1)$.

<details>
<summary>Show solution</summary>

The first outcome has $p_1=0.2>0$ but $q_1=0$. Since $p_1\log(p_1/q_1)=+\infty$, total KL is $+\infty$.

</details>

### 5. Entropy decomposition

Given $\mathrm H(p,q)=1.2$ nats and $\mathrm H(p)=0.9$ nats, calculate $D_{\mathrm{KL}}(p\Vert q)$.

<details>
<summary>Show solution</summary>

\[
D_{\mathrm{KL}}(p\Vert q)
=1.2-0.9
=0.3\ \text{nats}.
\]

</details>

### 6. Bernoulli KL

For $p=\operatorname{Bernoulli}(0.8)$ and $q=\operatorname{Bernoulli}(0.6)$, calculate $D_{\mathrm{KL}}(p\Vert q)$.

<details>
<summary>Show solution</summary>

\[
\begin{aligned}
D_{\mathrm{KL}}(p\Vert q)
&=0.8\log\frac{0.8}{0.6}
+0.2\log\frac{0.2}{0.4}\\
&=0.8\log\frac43+0.2\log\frac12\\
&\approx0.8(0.288)-0.2(0.693)\\
&\approx0.092\ \text{nats}.
\end{aligned}
\]

</details>

### 7. Critique a distillation claim

A student's teacher-output KL is very small on a test set. Evaluate “the student learned the same representation and reasoning circuits as the teacher.”

<details>
<summary>Show solution</summary>

Small KL is evidence of close output distributions at the specified test inputs and settings. Many hidden bases, features, and computations can produce the same output. Representation similarity, activation interventions, and distribution-shift evaluation are needed to assess claims of internal identity.

</details>

## Lesson summary

- KL divergence is $\log[p(x)/q(x)]$ averaged under $p$.
- If $q$ is 0 on support where $p$ is positive, $D_{\mathrm{KL}}(p\Vert q)$ is infinite.
- KL divergence is nonnegative and zero for identical distributions under the appropriate equality conditions.
- KL is asymmetric and fails a metric's triangle inequality.
- Cross entropy is target entropy plus forward KL.
- Forward and reverse KL use different averaging distributions and can produce different approximation behavior.
- Output KL does not guarantee identical hidden representations or causal mechanisms.

## Pass criteria

You pass if you can answer these questions without consulting the material.

- Can you read the discrete and continuous KL definitions?
- Can you explain direction $p\Vert q$ and the averaging distribution?
- Can you calculate small categorical and Bernoulli KL divergences?
- Can you explain nonnegativity and equality conditions?
- Can you illustrate support mismatch and asymmetry?
- Can you use the cross-entropy decomposition?
- Can you explain which internal-model claims output KL does not guarantee?

## Next lesson

- [M04-14 Mutual information](M04-14-mutual-information.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Discrete and continuous KL are defined.
- [x] Direction and support conditions are stated.
- [x] A calculation justifying nonnegativity is provided.
- [x] Asymmetry has been checked numerically.
- [x] The connection between cross entropy and MLE is explained.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretability claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] No prerequisites outside the stated scope are required implicitly.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
