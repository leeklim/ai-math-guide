---
id: "M04-12"
title: "Entropy and cross entropy"
part: 1
stage: "M04"
status: "complete"
prerequisites:
  - "M00-05"
  - "M00-10"
  - "M04-04"
  - "M04-11"
estimated_time: "145~175 minutes"
---

# M04-12. Entropy and cross entropy

## Why this lesson matters

Observing a low-probability outcome gives a large negative log-probability. Entropy averages this surprisal under the same distribution to summarize its uncertainty. Cross entropy evaluates outcomes from a target distribution using another distribution's log-probabilities.

Cross-entropy loss in classification, token NLL in language models, and soft-target loss in knowledge distillation use these definitions. To avoid conclusions about model accuracy, knowledge, or causal mechanisms based only on entropy, specify what is evaluated and which distribution supplies the averaging weights.

## Learning objectives

After completing this lesson, you should be able to:

- Explain self-information and entropy through the expectation of negative log-probability.
- Calculate entropy of small discrete distributions in nats and bits.
- Compare the entropies of deterministic and uniform distributions.
- Distinguish the roles of the two distributions in cross entropy $\mathrm H(p,q)$.
- Calculate why one-hot cross entropy equals categorical NLL.
- Calculate soft-target cross entropy and language-model perplexity.
- Explain what predictive entropy does not guarantee about accuracy or model knowledge.

## Prerequisite check

- Prerequisite: [M00-05 Exponents and logarithms](../M00/M00-05-exponents-logarithms.md)
- Prerequisite: [M00-10 Reading AI equations](../M00/M00-10-ai-equation-reading.md)
- Prerequisite: [M04-04 Expectation, variance, and covariance](M04-04-expectation-variance-covariance.md)
- Prerequisite: [M04-11 Likelihood and maximum likelihood estimation](M04-11-likelihood-maximum-likelihood.md)
- Check: Can you explain the natural logarithm's product rule and how $-\log p$ changes?
- Check: Can you calculate categorical NLL as the negative log-probability of the observed class?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Units and conditions |
|---|---|---|---|
| $I_p(x)$ | `I sub p of x` | The surprisal of outcome $x$ | $-\log p(x)$ |
| $\mathrm H(p)$ | `H of p` | Expected self-information under $p$ | Nats with natural logarithms |
| $\mathrm H(p,q)$ | `H of p comma q` | An average evaluating outcomes from $p$ using $q$'s log-probabilities | Directional |
| $D_{\mathrm{KL}}(p\Vert q)$ | `K L divergence from p to q` | The difference between cross entropy and entropy | Developed in M04-13 |
| $q_\theta(y\mid x)$ | `q sub theta of y given x` | The probability assigned to class $y$ at input $x$ | Sums to 1 |
| perplexity | `perplexity` | Exponentiated mean NLL | $\exp(\text{mean NLL})$ |

## Core concept 1. Self-information increases as probability decreases

Define the self-information, or surprisal, of an outcome $x$ under distribution $p$ as

\[
I_p(x)=-\log p(x)
\]

If $0<p(x)\le1$, then $I_p(x)\ge0$. An outcome with probability 1 has surprisal 0, and surprisal grows as probability approaches 0.

If the joint probability of independent outcomes $x,y$ is $p(x,y)=p(x)p(y)$, then

\[
I_p(x,y)
=-\log[p(x)p(y)]
=I_p(x)+I_p(y)
\]

Using logarithms makes joint surprisal additive for independent outcomes.

Natural logarithms give units of nats; base-2 logarithms give bits. This project uses natural logarithms unless stated otherwise.

The surprisal curve shows its behavior as probability approaches 0 and its reference value at probability 1.

<figure class="lesson-figure" markdown="1">

  ![Negative log probability increases toward rare positive probabilities and equals zero at probability one](../../figures/assets/M04/M04-12-surprisal-curve.svg)

  <figcaption>This is the natural-log −log p curve. At the marked probabilities p=1/4, 1/2, and 1, surprisal is about 1.386, 0.693, and 0 nats. There is no finite function value at p=0; the plotted left endpoint is only a small positive probability.</figcaption>
</figure>

## Core concept 2. Entropy averages surprisal under the same distribution

For a finite discrete distribution $p$, entropy is

\[
\mathrm H(p)
=\mathbb E_{X\sim p}[-\log p(X)]
=-\sum_x p(x)\log p(x)
\]

By continuity, set a term with $p(x)=0$ to $0\log0=0$.

Entropy is the distribution's average surprisal before observing an outcome. It depends on the number of possible outcomes and how probability is spread across them. It does not use distances or meanings of outcome values.

In the expectation sum, multiply each outcome's surprisal $-\log p(x)$ by its frequency weight $p(x)$. A rare outcome has high surprisal when observed but also receives a small weight because it occurs rarely. The rarest outcome's surprisal and the entire distribution's entropy are therefore different numbers. An outcome with probability 0 contributes nothing to this average, so the convention sets its term to 0.

Apply probability weights to the individual surprisals when calculating the average.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Outcome probability weights and surprisal combine into weighted contributions that sum to entropy](../../figures/assets/M04/M04-12-weighted-surprisal.svg)
  <figcaption>For p=(0.75,0.25), the rarer second outcome has larger surprisal but receives weight 0.25 in the average. The two bars on the right sum to entropy, about 0.562. Vertical-axis quantities and ranges differ across panels; an individual surprisal is not the entropy value.</figcaption>
</figure>

## Core concept 3. A deterministic distribution has entropy 0

If probability 1 is assigned to an outcome $x_0$,

\[
\mathrm H(p)
=-1\log1
=0
\]

The outcome is determined before observation and has no surprisal.

A uniform distribution assigning probability $1/K$ to each of $K$ outcomes has

\[
\mathrm H(p)
=-\sum_{k=1}^{K}\frac1K\log\frac1K
=\log K
\]

Among distributions on the same $K$ outcomes, the uniform distribution maximizes entropy. M04-13 explains this property again using KL divergence.

In the uniform expression, every outcome has surprisal $\log K$. Averaging the same value with weights totaling 1 gives $\log K$ again. Conversely, every entropy term is nonnegative, and an outcome with $0<p(x)<1$ contributes a positive term. Entropy 0 for a finite discrete distribution therefore means that all mass is on one outcome. Comparing against the uniform maximum holds the same set of $K$ outcomes fixed. Enlarging that set changes the maximum being compared.

Distinguish comparisons on a fixed outcome set from comparisons that change the number of outcomes.

<figure class="lesson-figure" markdown="1">

  ![Entropy of a fixed two outcome distribution is zero at deterministic endpoints and maximal at equal masses](../../figures/assets/M04/M04-12-binary-entropy.svg)

  <figcaption>Assigning (p,1−p) to the same two outcomes gives deterministic distributions with entropy 0 at both endpoints. The uniform choice p=1/2 gives maximum log 2. Terms with probability 0 at the endpoints use the convention 0 log 0=0.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">
  ![Uniform entropy grows as the number of equally probable outcomes increases](../../figures/assets/M04/M04-12-uniform-outcome-count.svg)
  <figcaption>This compares only uniform distributions with probability 1/K at each K. Increasing K increases maximum entropy log K. The connecting line illustrates the increasing trend; outcome count K is an integer.</figcaption>
</figure>

## Core concept 4. Cross entropy evaluates target $p$'s outcomes with model $q$

For two discrete distributions $p,q$, define cross entropy by

\[
\mathrm H(p,q)
=\mathbb E_{X\sim p}[-\log q(X)]
=-\sum_x p(x)\log q(x)
\]

Distribution $p$ supplies the average, and distribution $q$ supplies the log-probabilities. Swapping their roles can change the value.

If an outcome with $p(x)>0$ receives $q(x)=0$, cross entropy is infinite. The model has assigned zero probability to an outcome that can occur under the target.

An outcome with $p(x)=0$ contributes nothing to the target average and can be omitted from the sum. A term where both $p$ and $q$ are 0 is also treated as 0. Unlike entropy, the averaging weight $p(x)$ and the probability $q(x)$ used in surprisal come from different distributions. Decreasing $q(x)$ increases that outcome's log-loss, but $p(x)$ still determines its weight in the average.

Cross entropy decomposes as

\[
\mathrm H(p,q)
=\mathrm H(p)+D_{\mathrm{KL}}(p\Vert q)
\]

In a learning problem with fixed $p$, $\mathrm H(p)$ is independent of model parameters, connecting cross-entropy minimization to $D_{\mathrm{KL}}(p\Vert q)$ minimization.

Substituting $q=p$ gives the target's own entropy. While learning only $q$ with the target unchanged, $\mathrm H(p)$ is a fixed reference value and the KL term is the part of the decomposition that changes. With positive target entropy, matching the distributions need not make cross entropy 0. The next lesson establishes KL's definition and nonnegativity.

Swapping the roles of the two distributions also changes outcomes' contributions to the average.

<figure class="lesson-figure" markdown="1">
  ![Stacked class contributions give different cross entropy totals when target and model roles are reversed](../../figures/assets/M04/M04-12-cross-entropy-direction.svg)
  <figcaption>For p=(0.75,0.25) and q=(0.5,0.5), the two colored heights are outcomes' weighted log-loss contributions. H(p)≈0.562, H(p,q)≈0.693, and H(q,p)≈0.837: exchanging the averaging weights and evaluation probabilities changes the sum.</figcaption>
</figure>

The target's own average surprisal remains even when the model distribution matches it.

<figure class="lesson-figure" markdown="1">
  ![Cross entropy over model probability has a positive minimum equal to the fixed target entropy](../../figures/assets/M04/M04-12-target-entropy-floor.svg)
  <figcaption>With target p=(0.75,0.25) fixed, q=(q₁,1−q₁) varies. The minimum at q=p is H(p)≈0.562, not 0. The blue difference above the target entropy reference is the KL term, whose nonnegativity is established in the next lesson.</figcaption>
</figure>

## Core concept 5. One-hot cross entropy is the observed class's NLL

If the target class is $y$ and its one-hot target distribution is

\[
p_k=\mathbf 1\{k=y\}
\]

then cross entropy with model distribution $q_\theta$ is

\[
\begin{aligned}
\mathrm H(p,q_\theta)
&=-\sum_{k=1}^{K}p_k\log q_\theta(k\mid x)\\
&=-\log q_\theta(y\mid x).
\end{aligned}
\]

This is the categorical NLL expression. Averaging over a dataset gives empirical cross-entropy loss:

\[
\widehat{\mathcal L}_{\mathrm{CE}}(\theta)
=-\frac1n\sum_{i=1}^{n}
\log q_\theta(y_i\mid x_i).
\]

When calculating this from softmax logits, use log-softmax or log-sum-exp implementations to reduce overflow and underflow.

## Core concept 6. Soft targets use probabilities across all classes

When target distribution $p=(p_1,\ldots,p_K)$ is not one-hot, multiple terms in

\[
\mathrm H(p,q_\theta)
=-\sum_{k=1}^{K}p_k\log q_{\theta,k}
\]

contribute to the loss. Label smoothing distributes some one-hot target mass to other classes. Knowledge distillation can use a teacher distribution $p_T$ as the target for evaluating student distribution $p_S$:

\[
\mathcal L_{\mathrm{KD}}
=-\sum_{k=1}^{K}p_{T,k}\log p_{S,k}.
\]

This loss trains the student to match the teacher's output distribution. It does not include a condition requiring the same internal computation or causal mechanism.

For example, a teacher distribution $(0.8,0.2)$ has the first class as its mode but retains coefficient $0.2$ for the second. If the student focuses only on getting the first class right and drives the second probability toward 0, the term $-0.2\log p_{S,2}$ increases. Turning only the teacher's argmax class into a hard label removes this term and changes the original soft-target objective. A soft target uses the proportions of mass across classes, beyond the correct class index.

Even for the same student, soft targets and argmax hard labels demand different optima.

<figure class="lesson-figure" markdown="1">
  ![Soft teacher target loss minimizes at student mass point eight while hard label loss minimizes at one](../../figures/assets/M04/M04-12-soft-hard-target-loss.svg)
  <figcaption>The loss using teacher (0.8,0.2) unchanged is minimized when the student's first-class probability is 0.8. The target (1,0), retaining only the teacher's argmax, favors probability 1. Removing the teacher's second-class mass changes the learning objective itself.</figcaption>
</figure>

## Core concept 7. Language-model cross entropy is mean token NLL

Suppose a model produces next-token distributions conditioned on earlier tokens in sequence $y_1,\ldots,y_T$. The sequence NLL is

\[
-\log q_\theta(y_{1:T})
=-\sum_{t=1}^{T}
\log q_\theta(y_t\mid y_{<t})
\]

If mean NLL per token is $\bar\ell$, perplexity is

\[
\operatorname{PPL}=e^{\bar\ell}
\]

With base-2 instead of natural logarithms, write $2^{\bar\ell_{\mathrm{bits}}}$.

The sequence expression takes the logarithm of the product rule $q_\theta(y_{1:T})=\prod_t q_\theta(y_t\mid y_{<t})$. Each token is evaluated conditional on earlier tokens, so iid tokens are not assumed. If all observed token probabilities are positive, exponentiating mean NLL gives

\[
\operatorname{PPL}
=\left(\prod_{t=1}^{T}q_\theta(y_t\mid y_{<t})\right)^{-1/T}
\]

It is the reciprocal of the geometric mean of observed token probabilities. Assigning probability $1/K$ to the observed token at every position gives perplexity $K$, but in general perplexity does not count the actual vocabulary size.

Lower perplexity means assigning higher probability, measured by the geometric mean, to observed tokens in the evaluation sequence. Direct numerical comparisons are difficult when tokenizers, evaluation corpora, or token averaging rules differ.

Following each observed token with its preceding context shows where the product of conditional probabilities comes from.

<figure class="lesson-figure" markdown="1">

  ![Observed tokens with growing contexts produce conditional probabilities then sequence and mean negative log likelihood and perplexity](../../figures/assets/M04/M04-12-conditional-token-loss.svg)

  <figcaption>The constructed sequence A,B,C has observed-token probabilities 0.5, 0.25, and 1. Their conditional product is 0.125; total NLL is log 8 and mean token NLL is log 2, so perplexity is 2. This calculation conditions on context and does not assume iid tokens or a vocabulary size of 2.</figcaption>
</figure>

## Core concept 8. Predictive entropy summarizes a distribution's spread

For a classifier's predictive distribution $q_\theta(y\mid x)$ at input $x$, predictive entropy is

\[
\mathrm H\bigl(q_\theta(\cdot\mid x)\bigr)
=-\sum_y q_\theta(y\mid x)
\log q_\theta(y\mid x)
\]

A large value means model probability is spread across classes; a small value means it is concentrated on some classes.

Low predictive entropy does not guarantee correctness. A model assigning high probability to a wrong class can have low entropy and an incorrect prediction. Entropy alone also cannot separate data uncertainty from parameter uncertainty.

Entropy calculated after binning activations depends on bin boundaries and coordinate choice. Low or high activation entropy should not be equated directly with feature count or semantic complexity.

An entropy calculation that does not compare against the correct label cannot capture a correctness difference between two predictions.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Two swapped high confidence class distributions have identical predictive entropy but opposite correctness for the same observed label](../../figures/assets/M04/M04-12-entropy-correctness.svg)
  <figcaption>With the same correct label A, predictions (0.9,0.1) and (0.1,0.9) both have entropy about 0.325 nats. The first model's modal class is correct; the second's is wrong. Low entropy describes concentrated mass, without guaranteeing that the concentration is on the correct class.</figcaption>
</figure>

## Example 1. Entropy of a binary distribution

### Problem

Calculate the entropy of $p=(1/2,1/2)$ using natural and base-2 logarithms.

### Solution

Using natural logarithms,

\[
\mathrm H(p)
=-2\left(\frac12\log\frac12\right)
=\log2
\approx0.693\ \text{nats}
\]

Using base-2 logarithms,

\[
\mathrm H_2(p)
=-2\left(\frac12\log_2\frac12\right)
=1\ \text{bit}
\]

### Meaning of the result

The same uncertainty is expressed in nats or bits depending on the logarithm base.

## Example 2. Compare target entropy and cross entropy

Let $p=(0.75,0.25)$ and $q=(0.5,0.5)$.

\[
\mathrm H(p)
=-0.75\log0.75-0.25\log0.25
\approx0.562
\]

The cross entropy is

\[
\mathrm H(p,q)
=-0.75\log0.5-0.25\log0.5
=-\log0.5
\approx0.693
\]

Because $q$ does not reflect $p$'s imbalance, it incurs additional log-loss.

## Example 3. One-hot cross entropy

If the true class is 2 and model probabilities are

\[
q=(0.1,0.7,0.2)
\]

then

\[
\mathcal L_{\mathrm{CE}}
=-\log0.7
\approx0.357
\]

Other classes' terms do not remain directly in the sum because their one-hot target coefficients are 0. All logits influence $q_2$ through softmax normalization.

## Example 4. Distillation cross entropy

Let the teacher distribution be $p_T=(0.8,0.2)$ and the student distribution be $p_S=(0.6,0.4)$.

\[
\begin{aligned}
\mathrm H(p_T,p_S)
&=-0.8\log0.6-0.2\log0.4\\
&\approx0.8(0.511)+0.2(0.916)\\
&\approx0.592.
\end{aligned}
\]

The teacher's probabilities for both classes contribute to the student loss.

## Common misconceptions

### Misconception 1. Entropy is the same as variance

Entropy averages surprisal of probability masses; variance uses squared distances between numerical values. Entropy can be calculated even for a categorical distribution without specified distances between labels.

### Misconception 2. High entropy means a model is wrong

High predictive entropy means class probabilities are spread out. Correctness requires comparing the prediction against the observed label.

### Misconception 3. Cross entropy is symmetric

$\mathrm H(p,q)$ averages outcomes under $p$ and evaluates them with $q$'s log-probabilities. Exchanging these roles can change the value.

### Misconception 4. Cross-entropy loss 0 implies distributions are close

With a one-hot target, loss 0 means assigning probability 1 to the observed class. Loss on a finite dataset alone does not guarantee agreement with a population distribution or calibration.

### Misconception 5. Low distillation cross entropy makes the student's internals identical to the teacher's

A loss matching output distributions constrains input-output behavior. Different representations and computations can produce the same output distribution.

## Exercises

### 1. Self-information

Calculate self-information in nats and bits for an outcome with probability $1/4$.

<details>
<summary>Show solution</summary>

For natural logarithms,

\[
-\log\frac14=\log4\approx1.386\ \text{nats}.
\]

For base-2 logarithms,

\[
-\log_2\frac14=2\ \text{bits}.
\]

</details>

### 2. Deterministic entropy

Calculate the entropy of $p=(1,0,0)$.

<details>
<summary>Show solution</summary>

\[
\mathrm H(p)
=-1\log1-0\log0-0\log0
=0.
\]

Use the convention $0\log0=0$.

</details>

### 3. Categorical entropy

Calculate the entropy of $p=(0.5,0.25,0.25)$ in nats.

<details>
<summary>Show solution</summary>

\[
\begin{aligned}
\mathrm H(p)
&=-0.5\log0.5-2(0.25\log0.25)\\
&\approx0.3466+0.6931\\
&\approx1.0397\ \text{nats}.
\end{aligned}
\]

</details>

### 4. One-hot cross entropy

The true class is 1 and model probabilities are $(0.8,0.15,0.05)$. Calculate the cross-entropy loss.

<details>
<summary>Show solution</summary>

\[
\mathcal L_{\mathrm{CE}}
=-\log0.8
\approx0.223.
\]

With a one-hot target, only the negative log-probability of observed class 1 remains.

</details>

### 5. Soft-target cross entropy

The target is $p=(0.6,0.4)$ and the model is $q=(0.75,0.25)$. Calculate $\mathrm H(p,q)$.

<details>
<summary>Show solution</summary>

\[
\begin{aligned}
\mathrm H(p,q)
&=-0.6\log0.75-0.4\log0.25\\
&\approx0.6(0.288)+0.4(1.386)\\
&\approx0.727.
\end{aligned}
\]

</details>

### 6. Perplexity

Mean NLL per token is 2 nats. Calculate perplexity.

<details>
<summary>Show solution</summary>

\[
\operatorname{PPL}=e^2\approx7.39.
\]

Compare results using the same tokenizer and evaluation corpus.

</details>

### 7. Evaluate a model claim

Predictive entropy is very low for an input. Evaluate the conclusion, “The model understood this input and its prediction is correct.”

<details>
<summary>Show solution</summary>

Low entropy shows only that model probability is concentrated on some classes. Correctness requires comparison with an observed label, and assessing whether confidence is reliable requires calibration data. Claims about understanding or internal mechanisms need additional behavioral and intervention evidence.

</details>

## Lesson summary

- Self-information is an outcome's negative log-probability.
- Entropy averages self-information under the same distribution.
- A uniform distribution on $K$ outcomes has entropy $\log K$; a deterministic distribution has entropy 0.
- Cross entropy is the model $q$'s negative log-probability averaged under target $p$.
- One-hot cross entropy equals categorical NLL.
- Soft targets calculate cross entropy using probabilities across all classes.
- Language-model perplexity exponentiates mean NLL per token; predictive entropy summarizes the spread of class probabilities.

## Pass criteria

You pass if you can answer the following without consulting the material.

- Can you calculate self-information and entropy?
- Can you distinguish nats and bits by logarithm base?
- Can you compare deterministic and uniform distribution entropies?
- Can you distinguish target and model distributions in $\mathrm H(p,q)$?
- Can you connect one-hot cross entropy to NLL?
- Can you calculate soft-target loss and perplexity?
- Can you explain claims that predictive entropy does not guarantee?

## Next lesson

- [M04-13 KL divergence](M04-13-kl-divergence.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Self-information and entropy are defined.
- [x] Nats and bits are distinguished.
- [x] The roles of the two distributions in cross entropy are specified.
- [x] One-hot and soft-target losses are calculated.
- [x] Limitations of perplexity and predictive entropy are explained.
- [x] Every exercise has a solution.
- [x] Strengths of model interpretability claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
