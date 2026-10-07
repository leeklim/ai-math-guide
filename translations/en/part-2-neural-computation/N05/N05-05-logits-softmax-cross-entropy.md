---
id: "N05-05"
title: "Logits, softmax, and cross entropy"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-04"
  - "M04-12"
estimated_time: "120~150 minutes"
---

# N05-05. Logits, softmax, and cross entropy

## Why this lesson matters

The final layer of a classifier or language model produces a real-valued score for each class or token. This score is a logit. Softmax turns a logit vector into a distribution summing to 1, and cross entropy turns the probability assigned to a target into a scalar loss.

Mixing these three computations can lead to confusing probabilities with scores or applying softmax twice. This lesson calculates stabilization, probabilities, loss, and gradients from beginning to end using one logit vector, $[2,1,0]$.

## Learning objectives

After this lesson, you should be able to:

- Distinguish logits from probabilities.
- Calculate stable softmax using max subtraction.
- Calculate cross entropy for a one-hot target as a negative log-probability.
- Calculate the logit gradient of softmax cross entropy.
- Distinguish differences in output distributions from differences in internal computation.

## Prerequisite check

- Prerequisite lesson: [N05-04 Activation functions and gating](N05-04-activation-functions-gating.md)
- Prerequisite lesson: [M04-12 Entropy and cross entropy](../../part-1-foundations/M04/M04-12-entropy-cross-entropy.md)
- Check question: Can you use $e^{a+c}=e^ce^a$?
- Check question: Can you explain why $-\log p$ grows as $p$ becomes smaller?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\mathbf z$ | `z` | Vector of class logits | $\mathbb R^K$ |
| $z_k$ | `z sub k` | Logit for class $k$ | $\mathbb R$ |
| $p_k$ | `p sub k` | Probability of class $k$ assigned by softmax | $(0,1)$ |
| $\operatorname{softmax}(\mathbf z)_k$ | `softmax of z, component k` | The $k$th component of the softmax output | $(0,1)$ |
| $y$ | `y` | Correct class index | $\{1,\ldots,K\}$ |
| $\mathcal L$ | `script L` | Cross-entropy loss for one sample | $[0,\infty)$ |
| $\mathbf e_y$ | `e sub y` | One-hot vector with 1 only at the target class | $\{0,1\}^K$ |

## Core concept 1. A logit is a score before normalization

Here, we consider $K\ge2$ with all logits finite and real. A logit $z_k$ has no sum-to-1 constraint. Logits may be negative, and adding the same constant to all of them leaves class order unchanged. Softmax produces probabilities as

\[
p_k
=\operatorname{softmax}(\mathbf z)_k
=\frac{e^{z_k}}{\sum_{j=1}^{K}e^{z_j}}
\]

Each $p_k$ is positive, and $\sum_k p_k=1$.

Taking the ratio for two classes cancels the common denominator, giving $p_k/p_j=e^{z_k-z_j}$. Thus, $z_k-z_j=\log(p_k/p_j)$, and a larger logit receives a relatively larger probability. The number in one logit is not itself a probability: score differences between classes determine probability ratios. For a batch, this normalization is applied separately along each sample's class axis.


First distinguish the vertical axes in the two bar charts below, then compare values for the same class.

<figure class="lesson-figure" markdown="1">

![Three raw logits two one zero and their normalized probabilities appear on separate labeled scales](../../figures/assets/N05/N05-05-logit-probability.svg)

<figcaption>The upper panel shows logits (2, 1, 0), and the lower panel shows the same vector's softmax probabilities. The two vertical axes have different units; the sum-to-1 constraint applies only to the probabilities below.</figcaption>

</figure>

## Core concept 2. Max subtraction leaves probabilities unchanged

Subtracting $m=\max_j z_j$ from every logit gives

\[
\frac{e^{z_k-m}}{\sum_j e^{z_j-m}}
=\frac{e^{-m}e^{z_k}}{e^{-m}\sum_j e^{z_j}}
=\frac{e^{z_k}}{\sum_j e^{z_j}}
\]

The common factor cancels between numerator and denominator. The largest shifted logit becomes 0, avoiding unnecessarily large numbers during exponentiation.

For the same reason, any scalar $c$ satisfies

\[
\operatorname{softmax}(\mathbf z+c\mathbf 1)
=\operatorname{softmax}(\mathbf z)
\]

Softmax responds to relative logit differences rather than a common offset.

After max subtraction, every exponential is at most 1 and at least one is 1. This does not eliminate underflow of very small exponentials, so a mathematically positive probability can still round to 0 in finite-precision computation. Calculating the next section's loss directly from shifted logits and log-sum-exp, rather than calculating the target probability first and then taking its logarithm, reduces this problem.


In the converging paths below, removing the common offset brings both inputs to the same shifted logits.

<figure class="lesson-figure" markdown="1">

![Logit vectors two one zero and one hundred two one hundred one one hundred subtract their own maxima and converge to zero minus one minus two](../../figures/assets/N05/N05-05-offset-invariance.svg)

<figcaption>The two vectors differ only by the common offset 100. Subtracting their respective maxima 2 and 102 gives the same shifted logits (0, −1, −2), so the subsequent softmax probabilities and loss agree.</figcaption>

</figure>

## Core concept 3. Cross entropy uses the target's log-probability

In a one-hot problem with target class $y$,

\[
\mathcal L=-\log p_y
\]

Writing this in terms of logits gives

\[
\mathcal L
=-z_y+\log\sum_{j=1}^{K}e^{z_j}
\]

The first term lowers the loss as the target logit increases; the second jointly normalizes all class logits.

Substituting the one-hot target into the cross-entropy sum leaves only the target-position term, $-\log p_y$. Substituting softmax and turning the logarithm of a quotient into a difference gives the two terms above. Changing the target logit also changes the normalization term, so the first term alone does not determine the total change.

Using $m=\max_jz_j$, the same loss can be calculated as $(m-z_y)+\log\sum_j e^{z_j-m}$. Even if the target is the largest class, other classes retain probability mass, so the loss is greater than 0 for finite logits. Correctness and a loss evaluating target probability are different quantities.


On the curve below, the height corresponding to the target probability is the loss.

<figure class="lesson-figure" markdown="1">

![Negative natural logarithm curve decreases with target probability and marks probability zero point six six five two loss zero point four zero seven six](../../figures/assets/N05/N05-05-target-loss.svg)

<figcaption>With target probability on the horizontal axis, loss is the height on the −log p curve. For the example's p₁ ≈ 0.6652, loss ≈ 0.4076. Even when the target is the argmax, loss is not 0 for finite logits.</figcaption>

</figure>

## Core concept 4. The gradient subtracts the target from the probabilities

Composing softmax with one-hot cross entropy gives the derivative with respect to each logit:

\[
\frac{\partial\mathcal L}{\partial z_k}
=p_k-\mathbb 1[k=y]
\]

In vector form,

\[
\nabla_{\mathbf z}\mathcal L=\mathbf p-\mathbf e_y
\]

The gradient is negative at the target position and positive elsewhere. Treating logits themselves as independent variables, gradient descent moves in a direction that raises the target logit and lowers the other logits.

The derivative of the normalization term is $e^{z_k}/\sum_j e^{z_j}=p_k$, while the derivative of $-z_y$ is $-1$ only at the target position. Adding them gives the expression above. The components sum to $\sum_kp_k-1=0$, consistent with the loss being insensitive to changes in the common-offset direction.

Actual training changes shared network parameters, not the logits directly. This gradient is the starting value propagated to parameters by the chain rule, and one parameter can affect several logits. Its signs alone therefore do not establish that every sample's target logit must increase after an update.


In the bars below, check the 0 reference line together with the target position.

<figure class="lesson-figure" markdown="1">

![Three signed logit-gradient bars show negative target derivative and positive other derivatives that sum to zero](../../figures/assets/N05/N05-05-logit-gradient.svg)

<figcaption>Compare the first class's derivative −0.3348 and the other classes' positive derivatives against the 0 reference line. Descent treating logits themselves as independent variables moves opposite these derivatives. Actual parameter updates require the additional chain rule.</figcaption>

</figure>

## Example 1. Stable softmax for $[2,1,0]$

### Problem

Calculate the softmax probabilities for $\mathbf z=(2,1,0)$.

### Solution

Subtracting the maximum 2 gives $(0,-1,-2)$. Exponentiation and summation give

\[
(1,e^{-1},e^{-2})\approx(1,0.3679,0.1353),
\qquad
Z\approx1.5032
\]

Thus,

\[
\mathbf p\approx(0.6652,0.2447,0.0900)
\]

### What the result means

The first class receives the largest probability, but not probability 1. Logit differences determine the probability mass remaining on other classes.


The calculation path below preserves class indices while showing the order of division by the common sum.

<figure class="lesson-figure" markdown="1">

![Shifted scores zero minus one minus two exponentiate to one zero point three six seven nine zero point one three five three then divide by their sum](../../figures/assets/N05/N05-05-stable-softmax-flow.svg)

<figcaption>Exponentiate each shifted-logit position, add all three values to obtain Z ≈ 1.5032, and divide each by Z. Although the first class is largest, the other classes' exponential values remain, so p₁ is not 1.</figcaption>

</figure>

## Example 2. Loss and gradient

If the first class is the target,

\[
\mathcal L=-\log(0.6652)\approx0.4076
\]

The one-hot vector is $(1,0,0)$, so

\[
\nabla_{\mathbf z}\mathcal L
\approx(-0.3348,0.2447,0.0900)
\]

The three gradients sum to 0. Adding the same value to all logits leaves softmax probabilities and loss unchanged.

## Executable lab

### Execution environment and sources

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Checked on: 2026-10-01
- Component classification: `Stable core`
- Example ID: `n05_05_softmax_cross_entropy`
- Code source: `labs/N05/n05_05_softmax_cross_entropy.py`
- Test: `tests/N05/test_n05_05.py`
- Execution command: `.venv\Scripts\python.exe -m labs.N05.n05_05_softmax_cross_entropy`

### Resource budget

The example uses one logit vector with 3 classes. Its trainable parameter and training step counts are both 0, with a hard timeout of 10 seconds.

### Actual code and execution results

The site build inserts the source code and actual execution results at the following location.

<!-- N05_EXAMPLE: n05_05_softmax_cross_entropy -->

### Numerical and gradient checks

The tests check the sum of probabilities, loss, logit gradients, and translation invariance. They also compare the softmax results for the original logits and those with 100 added.

## Connection to model interpretation

Next-token analysis in language models considers logits over the entire vocabulary. A change in one token's logit is not the same as a change in its probability. One token's probability also depends on every other token's logit.

Two prompts can produce the same top-1 token while differing in logit margins and distributions. When comparing output behavior, state whether the measured quantity is argmax, target logit, logit difference, probability, or loss.


Compare the largest class and the target probability separately in the two distributions below.

<figure class="lesson-figure" markdown="1">

![Two softmax distributions with the same top class compare different target probabilities and negative log losses](../../figures/assets/N05/N05-05-same-argmax.svg)

<figcaption>Both comparison logits (2, 1, 0) and (1, 0.5, 0) have the first class as their maximum. However, the losses for the first-class target are about 0.4076 and 0.6803, so agreement in argmax must be distinguished from agreement in distribution.</figcaption>

</figure>

## Common misconceptions

### Misconception 1. The largest logit is a probability

A logit is a real-valued score before normalization. Probabilities summing to 1 are obtained only after applying softmax.

### Misconception 2. Probabilities should be supplied to softmax

Softmax takes logits as input. Supplying values that already sum to 1 to softmax again changes the distribution into a different one.


The paired bars below distinguish one application of softmax from two applications.

<figure class="lesson-figure" markdown="1">

![Probability bars before and after an incorrect second softmax show reduced class one mass and increased lower-class mass](../../figures/assets/N05/N05-05-second-softmax.svg)

<figcaption>For each class, the blue bar on the left shows the original probability; the purple bar on the right shows the result of applying softmax again to that probability vector. The second operation does not reuse the original logits. In this example, it reduces differences between classes and produces a different distribution.</figcaption>

</figure>

### Misconception 3. Cross entropy and accuracy are the same metric

Accuracy checks whether the argmax equals the target. Cross entropy evaluates the target probability as a continuous quantity. Even with the same predicted class, different confidence gives a different loss.

## Exercises

### 1. Adding the same constant

Use an equation to explain why $(2,1,0)$ and $(7,6,5)$ have the same softmax probabilities.

<details>
<summary>Show solution</summary>

The second vector adds 5 to every component of the first. The common factor $e^5$ introduced by exponentiation cancels between numerator and denominator, so the probabilities agree.

</details>

### 2. Uniform logits

If all $K$ logits are 0, find the softmax probabilities and cross entropy for one target.

<details>
<summary>Show solution</summary>

Each probability is $1/K$. The loss is $-\log(1/K)=\log K$.

</details>

### 3. Gradient sign

Find $\partial\mathcal L/\partial z_y$ when target class $y$ has probability 0.8.

<details>
<summary>Show solution</summary>

It is $p_y-1=0.8-1=-0.2$. A gradient descent update moves this logit upward.

</details>

### 4. Logit difference

In a two-class problem, how does $p_1$ change as $z_1-z_2$ increases?

<details>
<summary>Show solution</summary>

Since $p_1=1/(1+e^{z_2-z_1})$, $p_1$ increases as $z_1-z_2$ grows. A common offset has no effect.

</details>

### 5. Choosing a measurement

An intervention leaves the correct token's rank unchanged but reduces its probability from 0.7 to 0.4. Is it acceptable to report that “the output did not change”?

<details>
<summary>Show solution</summary>

The top-1 token is unchanged, but the distribution has changed. Distinguish the measurements and report that “the argmax was preserved and the target probability decreased by 0.3.”

</details>

### 6. Critiquing a claim

Evaluate the conclusion that two models have the same internal representations because their target probabilities are equal.

<details>
<summary>Show solution</summary>

This conclusion does not follow. Different logit vectors and internal computations can give the same target probability. Equality of internal representations requires activation alignment and additional analysis.

</details>

## Lesson summary

- Logits are scores before normalization; softmax outputs are probabilities.
- Max subtraction preserves softmax values while reducing the range used in exponentiation.
- One-hot cross entropy is the target class's negative log-probability.
- The logit gradient is $\mathbf p-\mathbf e_y$.
- Equal output distributions do not establish equal internal representations.

## Pass criteria

You pass if you can answer these questions without consulting the material.

- Can you distinguish logits from probabilities?
- Can you calculate stable softmax by hand?
- Can you calculate cross entropy from a target probability?
- Can you interpret the sign of a logit gradient?
- Can you explain the differences between argmax, logit, and probability measurements?

## Next lesson

- [N05-06 Backpropagation](N05-06-backpropagation.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Logits and probabilities are distinguished.
- [x] Stable softmax invariance is derived.
- [x] Loss and logit gradients are checked.
- [x] Every exercise has a solution.
- [x] The strength of model interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and math rendering have been checked.
- [x] Executable code is not manually duplicated in Markdown.
- [x] Code sources, test paths, resource budgets, and check dates are recorded.
- [x] Shape, numerical, and gradient tests are provided.
