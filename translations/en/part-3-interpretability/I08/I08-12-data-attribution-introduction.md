---
id: "I08-12"
title: "Introduction to data attribution"
part: 3
stage: "I08"
status: "complete"
prerequisites: ["I08-11", "I08-08", "I07-02"]
estimated_time: "100–130 minutes"
---

# I08-12. Introduction to data attribution

## Why this lesson matters

Feature attribution asks which parts of the current input relate to the output. Data attribution asks which training examples influenced the current prediction and the training path. TracIn approximates this relationship by summing the alignment between training and test gradients at several checkpoints.

## Learning objectives

- Distinguish feature attribution from data attribution.
- Compute a TracIn checkpoint score.
- Interpret the sign of a gradient dot product.
- Avoid equating an attribution ranking with a retraining effect.

## Prerequisite check

- Prerequisite lessons: [I08-11 Seeds and data order](I08-11-seed-data-order.md), [I08-08 Influence functions](I08-08-influence-function.md), [I07-02 Gradient-based attribution](../I07/I07-02-gradient-attribution.md)
- Check question: What does a positive inner product between two gradients mean about their update directions?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $z$ | `z` | Candidate training example | Sample |
| $z'$ | `z prime` | Test example to explain | Sample |
| $g_t(z)$ | `g sub t of z` | Loss gradient for $z$ at checkpoint $t$ | $\mathbb R^p$ |
| $I_{\mathrm{TracIn}}(z,z')$ | `I TracIn of z comma z prime` | Sum of checkpoint gradient alignments | Signed scalar |
| proponent | `proponent` | Example aligned with a direction that reduces test loss | Convention-dependent |

## 1. The questions concern different objects

Input token attribution concerns elements of the current input in the inference graph. Data attribution concerns examples in the training set and includes the learning algorithm as part of the explanation. A sentence being in the current prompt is different from that sentence having had a large influence during past training.

Distinguish where training inputs and inference inputs enter the computation.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Past training examples affect learned parameters through optimizer history, whereas current prompt elements enter inference in a fixed model.](../../figures/assets/I08/I08-12-training-and-inference-targets.svg)

<figcaption>The upper row shows the path from training examples through the optimizer to learned parameters. The lower row shows the inference path from the current prompt into a fixed model. Input token attribution and attribution to past data ask about different inputs. A large gradient score for a candidate alone does not establish that it was actually used in past training.</figcaption>
</figure>

## 2. The TracIn checkpoint approximation

A simple score over a selected checkpoint set $C$ is

$$
I_{\mathrm{TracIn}}(z,z')
=\sum_{t\in C}\eta_t
\nabla_\theta\ell(z,\theta_t)^\top
\nabla_\theta\ell(z',\theta_t)
$$

Both gradients are computed using the parameters at the same checkpoint, arranged in the same order. If the vectors come from different times or noncorresponding parameter coordinates, their inner product does not support the update interpretation of this equation.

The sign follows from an order-1 approximation to the loss. For an ordinary SGD update using one training example, the parameter change is $-\eta_t g_t(z)$. The effect of this small change on test loss is

$$
\ell(z',\theta_t-\eta_t g_t(z))-\ell(z',\theta_t)
\approx-\eta_t g_t(z')^\top g_t(z)
$$

Thus, a positive inner product means that the training example's update points in a direction that reduces test loss, while a negative inner product means it points in a direction that increases it. The TracIn score above assigns a positive sign to a loss **decrease**. This differs from I08-08, where positive influence denotes an **increase** in test loss due to upweighting. Rather than comparing signs alone, check which change is defined as positive.

This derivation approximates a small update in ordinary SGD. The actual updates in momentum or Adam include accumulated state and coordinate-wise scaling, so a raw gradient inner product cannot be treated as an exact calculation of the update's contribution.

Read the signs of the gradient alignment and the actual SGD movement together.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Positive, negative, and zero train-test gradient inner products produce first-order decreases, increases, and zero changes in test loss under a negative-gradient SGD update.](../../figures/assets/I08/I08-12-sgd-dot-product-sign.svg)

<figcaption>This mathematical example holds the test gradient at (1,0). Because the update points opposite to the training gradient, a positive inner product corresponds to a decrease in test loss. A positive TracIn score refers to this decrease, unlike the influence convention that assigns a positive sign to the loss increase from upweighting.</figcaption>
</figure>

Inspect the directions of two gradients paired at the same checkpoint.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three pairs of the existing CPU training and test gradients have inner products point eight, point five, and point eight eight, each computed at one matched checkpoint.](../../figures/assets/I08/I08-12-checkpoint-gradient-pairs.svg)

<figcaption>The two gradients from the existing CPU practice are plotted on the same coordinate axes at each matched checkpoint. Their inner products are 0.8, 0.5, and 0.88, respectively. Inner products that mix checkpoints or noncorresponding parameter coordinates do not have this update interpretation.</figcaption>
</figure>

Compare how each inner product and learning rate determine its contribution to the sum.

<figure class="lesson-figure" markdown="1">

![The three existing learning-rate-weighted checkpoint contributions are point zero eight, point zero two five, and point zero one seven six, summing to point one two two six.](../../figures/assets/I08/I08-12-weighted-checkpoint-sum.svg)

<figcaption>Multiplying the inner products by their learning rates of 0.1,0.05,0.02 gives contributions of 0.08,0.025,0.0176, summing to 0.1226. This small checkpoint approximation has positive terms throughout. It is not an actual removal-and-retraining result or an exact sum of the total loss decrease.</figcaption>
</figure>

## 3. Choosing checkpoints and layers

Because not every step is stored, TracInCP sums over only some checkpoints. The selected steps, learning rates, and parameter subset affect the score. An approximation using only the last layer reduces computation but is not the same as full-network influence.

The checkpoint approximation does not simply sum the loss decreases at every update where each example was actually used. It recomputes gradients at saved parameters to approximate relationships during training, so there is no guarantee that the sum of scores equals the actual total loss decrease. The same calculation can be performed for candidates that were not in the training set. A high score for such a candidate is not evidence that it was actually used in past training.

Duplicate examples can share influence, and large gradient norms can dominate rankings more than semantic relevance does. When neither gradient is 0, their inner product equals the product of their norms multiplied by the cosine of the angle between them. An example with a small gradient can therefore have a small raw score even when its direction is similar. Cosine normalization removes this magnitude information, so a cosine-normalized score and a raw dot product are different estimands.

Check which gradient coordinates have been retained.

<figure class="lesson-figure" markdown="1">

![Training and test gradient coordinate blocks match by layer, but selecting only the last-layer block excludes early-layer terms from their full dot product.](../../figures/assets/I08/I08-12-parameter-subset-blocks.svg)

<figcaption>The same parameter blocks in the two gradients must correspond. Taking the inner product only within the orange p_L block omits contributions from the earlier p₁,p₂ blocks. Report this as a score for the last-layer subset, not as full-network influence.</figcaption>
</figure>

A large candidate gradient and a better-aligned candidate gradient can receive different rankings.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A large diagonal gradient candidate has a higher raw dot score, while a smaller perfectly aligned candidate has a higher cosine score.](../../figures/assets/I08/I08-12-norm-versus-cosine-ranking.svg)

<figcaption>In this mathematical example, g_test=(1,0), candidate A=(10,10), and B=(1,0). The raw inner products are 10 for A and 1 for B, but the cosines are 1/√2 for A and 1 for B, reversing the ranking. A score that removes norms and a raw dot product are not the same estimand.</figcaption>
</figure>

## 4. CPU practice

<!-- I08_EXAMPLE: i08_12_data_attribution -->

Multiply the dot products of 2-dimensional training and test gradients at three checkpoints by their learning rates, then sum them. All terms are positive, but this value is not the result of actually removing an example and retraining.

## Common misconceptions

### Misconception 1. The top training example copied its content into the prediction

Gradient alignment is a local relationship between parameter updates. It does not separate duplicated content, joint effects of several examples, or nonlinear training paths.

### Misconception 2. More checkpoints always make the result more accurate

Adding low-quality or nearly identical checkpoints can increase costs without improving the result. Consider times with large changes in target loss and whether the selected checkpoints are representative.

## Exercises

### 1. Dot product

If $g(z)=(1,2)$ and $g(z')=(3,-1)$, what is their inner product?

<details><summary>Show solution</summary>

It is $1\times3+2\times(-1)=1$.

</details>

### 2. Learning rate

For the same dot product, what is the contribution of a checkpoint if $\eta_t$ is 0?

<details><summary>Show solution</summary>

It is 0. The approximation accounts for the actual update size.

</details>

### 3. Parameter subset

Explain the limitation of a score that uses only last-layer gradients.

<details><summary>Show solution</summary>

It omits influence through earlier layers. Report it as gradient similarity within the computed subset.

</details>

### 4. Duplication

Why can individual influence rankings be low if the same sentence appears ten times in the training set?

<details><summary>Show solution</summary>

Similar update contributions are distributed across several examples, and the remaining examples can compensate when one is removed.

</details>

### 5. Validation

The prediction did not change after the top proponent was removed and the model was retrained. Give two possible explanations.

<details><summary>Show solution</summary>

The TracIn approximation may have a large error, or duplicate or alternative training examples may have compensated for the effect.

</details>

### 6. Comparing methods

State one main difference between influence functions and TracIn.

<details><summary>Show solution</summary>

Influence functions use the Hessian inverse near an optimum, while TracIn sums gradient alignments across several training checkpoints.

</details>

## Evidence and update boundaries

This treatment of gradient-based data attribution using checkpoints follows [Pruthi et al. (2020)](https://proceedings.neurips.cc/paper/2020/hash/e6385d39ec9394f2f3a354d9d2b88eec-Abstract.html). The lesson covers small gradient calculations; storage and privacy issues in large-scale corpus search are outside its scope.

## Lesson summary

- Data attribution asks about the training relationship between training examples and predictions.
- TracIn sums checkpoint gradient dot products weighted by learning rates.
- Checkpoint, layer, and normalization choices affect rankings.
- A score is not an actual removal-and-retraining effect.

## Pass criteria

- Can you distinguish feature attribution from data attribution?
- Can you compute a small TracIn score?
- Can you design a retraining experiment to validate a ranking?

## Next lesson

- [I08-13 Capstone exercise: the lifecycle of a feature](I08-13-capstone-feature-lifecycle.md)

## Author checklist

- [x] The objects and approximations of data attribution are specified.
- [x] The TracIn equation and its limitations are explained.
- [x] Every exercise has a solution.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Claim strength and spoken readings have been checked.
- [x] Internal links and equations have been checked.
