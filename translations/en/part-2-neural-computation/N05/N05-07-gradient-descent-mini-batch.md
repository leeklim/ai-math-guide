---
id: "N05-07"
title: "Gradient descent and mini-batches"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-06"
  - "M04-06"
estimated_time: "120–150 minutes"
---

# N05-07. Gradient descent and mini-batches

## Why this lesson matters

Backpropagation calculates the loss gradient at the current parameters. Training uses that gradient to update the parameters, then repeats the calculation on a new batch. Selecting some samples rather than the entire dataset reduces computation, but produces different gradients across updates.

This lesson calculates the mean squared error for two samples. We check that the average of per-sample gradients equals the mini-batch gradient, then apply one gradient descent step.

## Learning objectives

After this lesson, you will be able to:

- Distinguish empirical risk from mini-batch loss in equations.
- Calculate a batch gradient with mean reduction.
- Apply a learning rate to update parameters by one step.
- Explain how sum and mean reduction affect gradient scale.
- Include batch sampling, seeds, and data order in reproducibility records.

## Prerequisite check

- Prerequisite lesson: [N05-06 Backpropagation](N05-06-backpropagation.md)
- Prerequisite lesson: [M04-06 Samples, populations, and sampling distributions](../../part-1-foundations/M04/M04-06-samples-populations-sampling-distributions.md)
- Check: Can you calculate a scalar loss's parameter gradient?
- Check: Can you calculate the arithmetic mean of sample values?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\theta$ | `theta` | Parameter vector to be learned | $\mathbb R^P$ |
| $\ell_i(\theta)$ | `ell sub i of theta` | Loss for sample $i$ | $[0,\infty)$ |
| $\mathcal B_t$ | `script B sub t` | Set of mini-batch indices selected at step $t$ | $\lvert\mathcal B_t\rvert=B$ |
| $L_{\mathcal B_t}$ | `L sub script B sub t` | Mini-batch mean loss | Scalar |
| $\eta$ | `eta` | Learning rate | $\eta>0$ |
| $g_t$ | `g sub t` | Mini-batch gradient at step $t$ | $\mathbb R^P$ |

## Core concept 1. Full-data and mini-batch averages

The empirical risk for $N$ samples is

\[
L(\theta)=\frac{1}{N}\sum_{i=1}^{N}\ell_i(\theta)
\]

Selecting only $B$ indices at step $t$ gives

\[
L_{\mathcal B_t}(\theta)
=\frac{1}{B}\sum_{i\in\mathcal B_t}\ell_i(\theta)
\]

The mini-batch gradient is

\[
g_t=\nabla_\theta L_{\mathcal B_t}(\theta_t)
=\frac{1}{B}\sum_{i\in\mathcal B_t}\nabla_\theta\ell_i(\theta_t)
\]

By linearity of differentiation, the gradient of mean loss is the average of per-sample gradients.

All derivatives in this average are evaluated at the same $\theta_t$. Updating parameters after one sample and then calculating the next sample's gradient evaluates derivatives at different points, so it does not give the average above. We also consider losses in which each sample's loss does not depend on other samples. A loss that uses samples jointly within a batch requires accounting for those computational dependencies.


Compare the two sample gradients and their mean on the same component axes.

<figure class="lesson-figure" markdown="1">

![Two per-sample gradient vectors and their mean share the origin and fixed parameter evaluation point](../../figures/assets/N05/N05-07-sample-gradients.svg)

<figcaption>The component order is the derivatives with respect to (w, b). Both vectors, (−6, −6) and (−20, −10), are evaluated at (w, b) = (0, 0). Their componentwise mean is (−13, −8). The figure does not show displacement in parameter space.</figcaption>

</figure>


Distinguish keeping the evaluation point fixed from updating first.

<figure class="lesson-figure" markdown="1">

![At the same starting parameters both sample gradients are fixed while a first sample update changes parameters and the second sample gradient](../../figures/assets/N05/N05-07-fixed-versus-sequential.svg)

<figcaption>Calculating the two samples' mean uses θ = (0, 0) for both. In the comparison path, first updating with sample 1's gradient at η = 0.1 gives θ = (0.6, 0.6), changing sample 2's derivatives to (−12.8, −6.4).</figcaption>

</figure>

## Core concept 2. Gradient descent update

The simplest update is

\[
\theta_{t+1}=\theta_t-\eta g_t
\]

At the current point, the gradient gives the direction of greatest first-order loss increase, so we move in its negative direction. Learning rate $\eta$ controls the displacement magnitude.

For a fixed current batch, the first-order approximation to the loss change is $g_t^\top(\theta_{t+1}-\theta_t)=-\eta\|g_t\|_2^2$. This is negative when $g_t\ne0$, but the actual loss also contains higher-order changes. The update length is $\eta\|g_t\|_2$, so the same learning rate can produce different displacement distances depending on the gradient magnitude.

Decreasing loss on one batch does not guarantee a decrease in the full dataset's loss. The gradient was calculated at the current parameters on the selected batch, and a large step can invalidate the first-order approximation.


Read loss contours together with the actual parameter displacement.

<figure class="lesson-figure" markdown="1">

![Loss contours for the exact two sample regression loss show parameter update from zero zero to one point three zero point eight](../../figures/assets/N05/N05-07-loss-step.svg)

<figcaption>The arrow on the grid is the actual update −0.1g = (1.3, 0.8), not a gradient vector. Gray lines show equal loss heights for this batch; the orange point (2, 1) gives parameters matching both targets. One step does not reach that point at once.</figcaption>

</figure>

## Core concept 3. Mean and sum reduction

Summing sample losses instead of averaging gives

\[
L^{\mathrm{sum}}_{\mathcal B_t}
=\sum_{i\in\mathcal B_t}\ell_i,
\qquad
\nabla L^{\mathrm{sum}}_{\mathcal B_t}=B g_t
\]

With the same learning rate, batch size enters the update scale directly. Record the loss definition and reduction together when reproducing an experiment.

For one ordinary gradient descent step on the same batch, reducing the sum-loss learning rate to $1/B$ of the mean-loss learning rate gives the same update. This relation compares the same samples at the same evaluation point. Changing batch composition or using an optimizer with gradient history means matching the reduction scale alone does not make the entire training path identical.


Compare the two displacement lengths for different reductions from the same starting point.

<figure class="lesson-figure" markdown="1">

![Mean and sum gradient steps from the same origin differ by batch size two while halving the sum learning rate gives the mean endpoint](../../figures/assets/N05/N05-07-reduction-step.svg)

<figcaption>With the same two samples and initialization, the sum gradient is twice the mean gradient. At η = 0.1, the displacement also doubles. Lowering the sum learning rate to 0.05 gives the same endpoint as the mean for this one step.</figcaption>

</figure>

## Example 1. Gradients for two samples

### Problem

Use $(x,y)=(1,3),(2,5)$ as a mini-batch for model $\hat y=wx+b$. Initialize $w=b=0$ and use mean squared error as the loss. Calculate the loss and gradients.

### Solution

The initial predictions are $(0,0)$ and residuals are $(-3,-5)$.

\[
L=\frac{(-3)^2+(-5)^2}{2}=17
\]

The per-sample $w$ gradients are $2(\hat y-y)x$, giving $(-6,-20)$. The $b$ gradients are $2(\hat y-y)$, giving $(-6,-10)$. Averaging gives

\[
\frac{\partial L}{\partial w}=-13,
\qquad
\frac{\partial L}{\partial b}=-8
\]

## Example 2. One-step update

With $\eta=0.1$,

\[
w_1=0-0.1(-13)=1.3,
\qquad
b_1=0-0.1(-8)=0.8
\]

The new predictions are $(2.1,3.4)$, and the new loss on the same batch is

\[
\frac{(2.1-3)^2+(3.4-5)^2}{2}=1.685
\]

This step reduces batch loss from 17 to 1.685.


Check the residuals between the fixed targets and new predictions.

<figure class="lesson-figure" markdown="1">

![Before zero prediction line and updated linear prediction line compare two fixed target points and residual gaps](../../figures/assets/N05/N05-07-updated-predictions.svg)

<figcaption>The two target points remain fixed while the prediction line changes from 0 to 1.3x + 0.8. Purple dashed lines show the gaps between new predictions and targets. Residuals become (−0.9, −1.6), giving loss 1.685 on the same batch.</figcaption>

</figure>

## Execution exercise

### Execution environment and sources

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Verification date: 2026-10-01
- Component category: `Stable core`
- Example ID: `n05_07_minibatch_gradient_descent`
- Source code: `labs/N05/n05_07_minibatch_gradient_descent.py`
- Test: `tests/N05/test_n05_07.py`
- Run command: `.venv\Scripts\python.exe -m labs.N05.n05_07_minibatch_gradient_descent`

### Resource budget

The example uses batch size 2, scalar inputs, 2 parameters, and 1 update. The hard timeout is 10 seconds.

### Actual code and execution results

The site build inserts the source code and actual execution results at the location below.

<!-- N05_EXAMPLE: n05_07_minibatch_gradient_descent -->

### Numerical-value and gradient checks

Tests compare the average of per-sample gradients with the batch gradient calculated by autograd. After the update, $w=1.3$, $b=0.8$, and loss 1.685 are also compared with the hand calculation.

## Sampling and reproducibility

Interpreting a mini-batch gradient as an estimate of the full gradient requires specifying the sampling scheme. Fix the current parameters and draw a fresh, uniformly selected subset of size $B$ from $N$ samples. Each sample has inclusion probability $B/N$. In the expectation of the average gradient, multiplying this probability by $1/B$ gives the full-data gradient's weight $1/N$. This does not mean any particular batch gives the same value. Class-balanced sampling, sequence packing, and duplicate samples can produce different estimands.

Recording a seed alone is insufficient. Save the dataset version, sample order, sampler settings, batch size, and reduction to replay the same update sequence.


Distinguish one sampling outcome from its expectation.

<figure class="lesson-figure" markdown="1">

![Uniformly selecting one of two samples gives different gradient outcomes with probability one half and expected gradient equal to the full two sample mean](../../figures/assets/N05/N05-07-sampling-expectation.svg)

<figcaption>Select one of the example's two samples uniformly with B = 1. A single gradient is one of the two vectors, while their expectation weighted by inclusion probability 1/2 equals the mean gradient over both samples.</figcaption>

</figure>

## Connection to model interpretation

Per-example gradients provide material for analyzing how training examples contribute to the current parameter update. Gradient similarity and influence approximations depend on the parameter location, loss definition, and checkpoint.

A sample producing a large gradient in one batch cannot be called the cause of the entire training process. Sampling over many steps and optimizer state determine the actual trajectory.

## Common misconceptions

### Misconception 1. The mini-batch gradient equals the full gradient

A particular batch's gradient estimates the full gradient under the sampling conditions. The values agree when the entire dataset is used as a batch. A subset's average can also happen to agree, but agreement is not generally guaranteed.

### Misconception 2. Changing batch size leaves the update unchanged

Mean reduction removes the direct $B$ multiplier, but gradient noise and sample composition change. With sum reduction, gradient scale also changes with $B$.

### Misconception 3. A one-step loss decrease means training succeeded

Only an immediate decrease on the current batch has been established. Other batches, validation data, and stability in later steps must be checked separately.

## Exercises

### 1. Mean gradient

Two samples have scalar gradients 4 and 10. What is the mean-reduced batch gradient?

<details>
<summary>Show solution</summary>

It is $(4+10)/2=7$.

</details>

### 2. Sum reduction

What is the sum-reduced gradient in the previous problem?

<details>
<summary>Show solution</summary>

It is $4+10=14$, twice the mean gradient because batch size is 2.

</details>

### 3. Update direction

For $\theta=3$, $g=-4$, and $\eta=0.2$, find the next parameter value.

<details>
<summary>Show solution</summary>

$\theta'=3-0.2(-4)=3.8$. A negative gradient increases the parameter.

</details>

### 4. Batch size 1

What does the mini-batch gradient equal when $B=1$?

<details>
<summary>Show solution</summary>

It equals the selected sample's gradient, not necessarily the full-data gradient.

</details>

### 5. Reproducibility records

Give two reasons why training recorded with only a seed and batch size cannot be replayed exactly.

<details>
<summary>Show solution</summary>

The dataset version, sample order, or sampler implementation can differ. Loss reduction, preprocessing, and checkpoint state also change updates.

</details>

### 6. Critiquing a claim

Evaluate the conclusion that a sample with the largest gradient norm created the final model behavior.

<details>
<summary>Show solution</summary>

A local gradient norm at one checkpoint does not determine causal contributions across the entire training trajectory. Consider the steps at which the sample was selected, other gradients, optimizer state, and later updates together.

</details>

## Lesson summary

- A mini-batch mean gradient is the average of per-sample gradients within the batch.
- Gradient descent updates parameters in the negative-gradient direction.
- Sum and mean reduction differ in how gradient scale depends on batch size.
- A one-step batch-loss decrease does not guarantee overall training success.
- Reproduction requires update-sequence information, including data order and the sampler.

## Pass criteria

You pass when you can answer these questions without consulting the material:

- Can you distinguish full-data loss from mini-batch loss?
- Can you calculate a batch gradient from per-sample gradients?
- Can you apply a learning rate to calculate an update?
- Can you explain the difference between mean and sum reduction?
- Can you limit the scope of claims based on mini-batch gradients?

## Next lesson

- [N05-08 Momentum, AdamW, and optimizer state](N05-08-momentum-adamw-optimizer-state.md)

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] Full-data and mini-batch losses are distinguished.
- [x] Mean and sum reduction are distinguished.
- [x] Numerical values and gradients before and after the update are checked.
- [x] Every exercise has a solution.
- [x] Strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and math rendering are checked.
- [x] Execution code is not manually duplicated in Markdown.
- [x] Source-code and test paths, resource budgets, and verification dates are recorded.
- [x] Shape, numerical-value, and gradient tests are provided.
