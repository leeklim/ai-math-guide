---
id: "I08-05"
title: "Mini-batch noise and optimizer state"
part: 3
stage: "I08"
status: "complete"
prerequisites: ["I08-04", "N05-08", "M04-04"]
estimated_time: "90–120 minutes"
---

# I08-05. Mini-batch noise and optimizer state

## Why this lesson matters

Different mini-batch orders produce different gradient sequences even with the same data and initial weights. With momentum or Adam-family optimizers, the optimizer state retains past gradients, so current weights alone cannot reproduce the next update. Studying checkpoint dynamics requires distinguishing this hidden state.

## Learning objectives

- Decompose a mini-batch gradient into the full gradient and a noise term.
- Calculate how momentum state makes a path depend on its history.
- Distinguish a checkpoint for resuming training from a weight snapshot for analysis.
- Separate seed effects from data-order effects experimentally.

## Prerequisite check

- Prerequisite lessons: [I08-04 Viewing SGD as dynamics](I08-04-sgd-as-dynamics.md), [N05-08 Momentum and AdamW](../../part-2-neural-computation/N05/N05-08-momentum-adamw-optimizer-state.md), [M04-04 Expectation, variance, and covariance](../../part-1-foundations/M04/M04-04-expectation-variance-covariance.md)
- Check question: What is the expectation of an unbiased mini-batch gradient?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $g_{B_k}(\theta_k)$ | `g sub B sub k of theta sub k` | Gradient for batch $B_k$ | $\mathbb R^p$ |
| $\xi_k$ | `xi sub k` | Difference from the full gradient | $\mathbb R^p$ |
| $v_k$ | `v sub k` | Momentum state | $\mathbb R^p$ |
| $v_{k+1}=\beta v_k+g_k$ | `v sub k plus one equals beta v sub k plus g sub k` | Momentum accumulation | vector recurrence |
| RNG state | `R N G state` | State determining the next random numbers | implementation-specific |

## 1. Gradient noise

Write the mini-batch gradient as

$$
g_{B_k}(\theta_k)=\nabla L(\theta_k)+\xi_k
$$

Here $\xi_k$ is defined as the difference between the batch gradient and the full gradient at the same current weights. If $L$ is the mean of the per-example losses and examples are freshly sampled with equal probability from the entire dataset while holding the current weights fixed, the batch gradient's mean is the full gradient. Under these conditions, $\mathbb E[\xi_k\mid\theta_k]=0$, but an individual batch's $\xi_k$ need not be 0.

The expectation averages over many batch selections. The next position follows a move along the selected batch gradient, so the weights where the next gradient is evaluated also vary across runs. Unbiasedness at each step therefore does not imply that the mean noisy trajectory equals the full-batch trajectory. Sampling sequentially within an epoch while excluding previously used examples can link the current weights to the remaining data, so do not automatically assume the same conditional mean.

When independent example gradients are averaged, the noise covariance decreases inversely with batch size. This relation assumes independent samples and the same sampling rule. With within-batch correlation or a different sampling method, batch size alone does not determine the covariance.

Compare the vector relation between gradients and noise at the same current weights.

<figure class="lesson-figure" markdown="1">

![The existing batch gradient two one decomposes into full gradient one point five one point two and noise point five minus point two](../../figures/assets/I08/I08-05-gradient-noise-decomposition.svg)

<figcaption>The exercise's batch and full gradients are compared at the same θ. The purple difference ξ is not 0. Conditional mean 0 refers to repeated sampling under the rule specified in the text.</figcaption>
</figure>

Read the effect of batch size on an independent average in the following curve.

<figure class="lesson-figure" markdown="1">

![The normalized one over batch size variance curve assumes independent identically sampled example gradients at fixed parameters](../../figures/assets/I08/I08-05-iid-noise-scaling.svg)

<figcaption>The curve shows relative noise variance 1/B for an average of independent example gradients sampled by the same rule at fixed θ. It is not a measured relation under changed correlation or sampling conditions.</figcaption>
</figure>

## 2. Weights alone are not the full state

The momentum update is

$$
v_{k+1}=\beta v_k+g_{B_k}(\theta_k),\qquad
\theta_{k+1}=\theta_k-\eta v_{k+1}
$$

At the same $\theta_k$, different $v_k$ produce different next weights. AdamW additionally needs first and second moments and a step counter.

Starting from $v_0=0$ and applying gradients in order $g_1$, $g_2$ gives $v_1=g_1$ and $v_2=\beta g_1+g_2$. Because the first weight displacement also uses $g_1$, the weights after two steps are $\theta_0-\eta[(1+\beta)g_1+g_2]$. Reversing the order gives $\theta_0-\eta[(1+\beta)g_2+g_1]$. The gradient sum is unchanged, but the coefficients assigned to the gradients in the accumulated displacement differ. The exercise isolates this order effect by inserting a given gradient list into the recurrence. In actual training, changed weights can also change subsequent gradient values.

Exact resumption requires model parameters, buffers, optimizer state, scheduler state, data-loader position, and RNG state. Weights and a tokenizer may suffice for representation analysis, but that does not imply training can be resumed exactly.

Saved momentum enters the next computation alongside the current weights.

<figure class="lesson-figure" markdown="1">

![At the same weight zero and gradient minus one momentum zero or two yields next weights point one or minus point zero eight](../../figures/assets/I08/I08-05-same-weight-different-state.svg)

<figcaption>This numerical example fixes the exercise's β=0.9 and gradient −1 and changes only the momentum state. Even with the same current weight 0, the next weight is 0.1 or −0.08.</figcaption>
</figure>

Compare the exercise's calculations with the same gradient list in different orders.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The existing four-gradient list in forward and reverse order makes different exact momentum and parameter trajectories](../../figures/assets/I08/I08-05-momentum-order-path.svg)

<figcaption>This uses the existing gradient list and β=0.8, η=0.1 unchanged. Reversing the list changes the momentum at each step and the accumulated weight displacement. These are not newly computed gradients from an actual training run.</figcaption>
</figure>

Trace how the states needed for resumption determine the next batch and update.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Loader and RNG state choose the next batch while weights buffers momentum and scheduler jointly determine the next update](../../figures/assets/I08/I08-05-restart-state-paths.svg)

<figcaption>The loader and RNG select the next batch, from which gradients are computed with the current weights and buffers. Momentum and the schedule must also be included to reproduce the next update.</figcaption>
</figure>

## 3. Design an order-effect comparison

To study initialization effects, fix the data order and change only the initialization seed. To study order effects, start from the same weights and change only the shuffle seed. Changing both at once prevents separation of their contributions to variation.

Check a design that changes one comparison factor at a time.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A two by two run design compares fixed initialization across data orders and fixed order across initializations](../../figures/assets/I08/I08-05-one-factor-order-design.svg)

<figcaption>Within a row, initial weights are fixed and only order changes. Within a column, order is fixed and only initialization changes. Retain the other optimizer, schedule, data, and random-source conditions throughout.</figcaption>
</figure>

## 4. CPU exercise

<!-- I08_EXAMPLE: i08_05_minibatch_optimizer_state -->

Apply momentum updates to the same gradient multiset in forward and reverse order. Although the sum is unchanged, older and newer gradients receive different weights, producing different final parameters.

## Common misconceptions

### Misconception 1. Recording one seed makes a run deterministic

Initialization, shuffle, dropout, and library kernels may have separate random sources. Record the environment and deterministic settings too.

### Misconception 2. Unbiased gradients give the full-batch path

Equal expectations do not imply equal sample paths. With a nonlinear loss, noise changes the next position and future gradients.

## Exercises

### 1. Define noise

Find $\xi$ for $g_B=(2,1)$ and full gradient $(1.5,1.2)$.

<details><summary>Show solution</summary>

It is $\xi=(0.5,-0.2)$.

</details>

### 2. One momentum step

What is $v_{k+1}$ if $v_k=2$, $g_k=-1$, and $\beta=0.9$?

<details><summary>Show solution</summary>

It is $0.9\times2-1=0.8$.

</details>

### 3. Resume training

The weights and optimizer state are saved, but the data-loader position is not. Why is exact resumption difficult?

<details><summary>Show solution</summary>

The next batch may differ, changing the next gradient and subsequent trajectory.

</details>

### 4. Conditional expectation

Does $\mathbb E[\xi_k\mid\theta_k]=0$ mean the actual $\xi_k=0$?

<details><summary>Show solution</summary>

No. The average over repeated sampling is 0; individual batch noise need not be 0.

</details>

### 5. Experimental design

What must be fixed to measure only the shuffle-order effect?

<details><summary>Show solution</summary>

Fix initial weights, the dataset, optimizer and schedule, augmentation, and other random sources. Change only the shuffle seed.

</details>

### 6. Critique a claim

Critique “The same final loss means the same training path.”

<details><summary>Show solution</summary>

Different paths and parameters can reach the same scalar loss. Compare intermediate checkpoints and functional and representation metrics.

</details>

## Evidence and update boundaries

Refer to [Li, Tai and E (2019)](https://www.jmlr.org/papers/v20/17-526.html) for the stochastic modified equation perspective on SGD. This lesson does not assume independent Gaussian noise or make claims about optimizer-specific long-term distributions.

## Lesson summary

- A mini-batch gradient decomposes into the full gradient and sample noise.
- Optimizer state retains path information absent from the weights.
- Exact resumption also requires data order and RNG state.
- Change initialization and order one at a time when separating their effects.

## Pass criteria

- Can you calculate gradient noise and the momentum recurrence?
- Can you distinguish a snapshot from a checkpoint for resuming training?
- Can you design an experiment separating seed and order effects?

## Next lesson

- [I08-06 Hessian spectrum](I08-06-hessian-spectrum.md)

## Author checklist

- [x] Mini-batch noise and state are distinguished.
- [x] Resumption conditions are specified.
- [x] Every exercise has a solution.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Claim strength and spoken readings have been checked.
- [x] Internal links and equations have been checked.
