---
id: "N05-08"
title: "Momentum, AdamW, and optimizer state"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-07"
estimated_time: "120–150 minutes"
---

# N05-08. Momentum, AdamW, and optimizer state

## Why this lesson matters

Gradient descent uses only the current gradient. Momentum accumulates previous gradient directions in a buffer, while Adam stores estimates of the gradient's first and second moments for each parameter. AdamW separates weight decay from the loss-gradient update.

A training checkpoint therefore requires more than weights. Even when resuming from the same weights, different optimizer states and steps produce different next updates. This lesson calculates the first momentum and AdamW steps for one scalar parameter.

## Learning objectives

After this lesson, you will be able to:

- Update a momentum buffer and calculate the parameter update.
- Calculate Adam's first and second moments and bias correction.
- Distinguish AdamW's adaptive update from decoupled weight decay.
- Explain the storage difference between parameters and optimizer state.
- Determine when steps and optimizer state are needed in checkpoint comparisons.

## Prerequisite check

- Prerequisite lesson: [N05-07 Gradient descent and mini-batches](N05-07-gradient-descent-mini-batch.md)
- Check: Can you numerically calculate $\theta_{t+1}=\theta_t-\eta g_t$?
- Check: Can you explain how an exponential moving average combines previous state and a new value?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $g_t$ | `g sub t` | Gradient at step $t$ | Same shape as the parameter |
| $u_t$ | `u sub t` | Momentum buffer | Same shape as the parameter |
| $m_t$ | `m sub t` | Adam first-moment estimate | Same shape as the parameter |
| $v_t$ | `v sub t` | Adam second raw-moment estimate | Same shape as the parameter; nonnegative |
| $\hat m_t$ | `m hat sub t` | Bias-corrected first moment | Same shape as the parameter |
| $\hat v_t$ | `v hat sub t` | Bias-corrected second moment | Same shape as the parameter |
| $\beta_1,\beta_2$ | `beta one and beta two` | Adam decay coefficients | $[0,1)$ |
| $\lambda$ | `lambda` | Weight-decay coefficient | $\lambda\ge0$ |

## Core concept 1. Momentum stores gradient history as state

This lesson uses the momentum convention

\[
u_t=\mu u_{t-1}+g_t,
\qquad
\theta_t=\theta_{t-1}-\eta u_t
\]

The buffer $u_t$ combines the previous buffer with the current gradient. Libraries differ in their $(1-\mu)$ factors, dampening, and placement of Nesterov calculations, so check equations together with implementations.

Here $u_0=0$, $0\le\mu<1$, and $g_t$ is calculated at the pre-update $\theta_{t-1}$. Expanding two steps gives $u_2=\mu g_1+g_2$. Older gradients receive more repeated factors of $\mu$, reducing their influence. Even when the current gradient is negative, the parameter can keep decreasing if a larger retained positive contribution makes the buffer positive. The momentum buffer is not the current gradient itself.


Distinguish the current gradient's sign from the actual buffer and parameter displacement.

<figure class="lesson-figure" markdown="1">

![Positive retained momentum contribution one point eight plus current negative gradient minus one yields positive buffer zero point eight and a negative parameter step](../../figures/assets/N05/N05-08-momentum-sign.svg)

<figcaption>With u_prev = 2, μ = 0.9, and g = −1, adding −1 to the retained contribution 1.8 gives u = 0.8. The parameter scale below shows update −0.08 for θ = 5 and η = 0.1. The gradient and parameter scales have different units.</figcaption>

</figure>


Compare the weights on older gradients with those on recent gradients.

<figure class="lesson-figure" markdown="1">

![At step five exponential history weights increase from the oldest gradient mu to the fourth to the newest gradient weight one](../../figures/assets/N05/N05-08-momentum-history.svg)

<figcaption>These are the weights obtained by expanding five steps from u₀ = 0. The horizontal axis is the step at which each gradient was calculated. At current step 5, older values carry more factors of μ. This explains why the buffer cannot be identified with one current gradient.</figcaption>

</figure>

## Core concept 2. Adam stores two moment estimates

Adam updates its state through

\[
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t
\]

\[
v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2
\]

Here $g_t^2$ is an elementwise square. Moving averages initialized at zero are biased toward the initial value, so they are corrected as

\[
\hat m_t=\frac{m_t}{1-\beta_1^t},
\qquad
\hat v_t=\frac{v_t}{1-\beta_2^t}
\]

The adaptive part of the Adam update is

\[
\Delta_t^{\mathrm{Adam}}
=\eta\frac{\hat m_t}{\sqrt{\hat v_t}+\epsilon}
\]

Starting with $m_0=v_0=0$, expanding the first moment gives $m_t=(1-\beta_1)\sum_{s=1}^t\beta_1^{t-s}g_s$. Its gradient weights sum to $1-\beta_1^t$, so dividing by this value corrects the initially missing weight. The same reasoning gives $1-\beta_2^t$ for the second moment. In actual training, where the gradient distribution keeps changing, this correction does not guarantee an exact estimate of the current gradient.

$v_t$ averages squared gradients; it is not variance, which averages squared deviations from the mean. The adaptive ratio divides each coordinate's signed first moment by a scale derived from that coordinate's squared magnitude. The condition $\epsilon>0$ prevents a zero denominator. Because $m_t$ still contains past values, the current $g_t$'s sign alone does not determine the update direction.


Follow the first and second moments and their respective correction denominators in order.

<figure class="lesson-figure" markdown="1">

![Gradient three branches into first moment zero point three and second moment zero point zero zero nine then bias correction yields three and nine and adaptive displacement zero point one](../../figures/assets/N05/N05-08-adam-moments.svg)

<figcaption>This is the first step with m₀ = v₀ = 0, β₁ = 0.9, and β₂ = 0.999. The signed gradient and its square enter different states, each corrected with a different denominator. Ignoring small ε, the adaptive displacement magnitude is 0.1.</figcaption>

</figure>


Check how the sum of weights changes before and after correction.

<figure class="lesson-figure" markdown="1">

![First-moment gradient weights at step five sum to zero point four zero nine five one before correction and one after division by one minus beta to the fifth](../../figures/assets/N05/N05-08-bias-correction.svg)

<figcaption>This expands the first moment through five steps. The left bar at each step is the uncorrected weight; the right bar divides it by 1 − 0.9⁵. Their sum changes from 0.40951 to 1, but this does not make the gradients themselves equal.</figcaption>

</figure>

## Core concept 3. AdamW separates weight decay

A simplified AdamW step is

\[
\theta_t
=\theta_{t-1}
-\eta\frac{\hat m_t}{\sqrt{\hat v_t}+\epsilon}
-\eta\lambda\theta_{t-1}
\]

The last term acts directly on the parameter rather than being mixed into the loss gradient. For an adaptive optimizer, adding an $L_2$ penalty to the loss and applying decoupled weight decay do not give the same update.

Adding $\lambda\|\theta\|_2^2/2$ to the loss adds $\lambda\theta$ to the gradient, placing that term inside the moments and adaptive scaling. AdamW keeps it out of moment calculations and separates its effect as multiplication of the previous parameter by $1-\eta\lambda$. When $0<\eta\lambda<1$, the decay part alone shrinks the parameter toward zero. The full update also includes the gradient term, so not every parameter's absolute value must decrease.


Distinguish terms entering the moments from terms applied outside them.

<figure class="lesson-figure" markdown="1">

![L2 regularization adds lambda theta to the gradient before moments while AdamW sends only loss gradient through moments and applies decay separately to the parameter update](../../figures/assets/N05/N05-08-l2-versus-adamw.svg)

<figcaption>The upper L2 path adds λθ to the loss gradient before calculating moments and adaptive scaling. The lower AdamW path sends only the loss gradient into the moments and separately subtracts decay η times λθ in the parameter update. The same λ generally does not give the same result.</figcaption>

</figure>

## Core concept 4. Optimizer state is also part of a checkpoint

Adam-family optimizers store $m_t$ and $v_t$ for each parameter element and record the step. For $P$ parameters, these two tensors alone add approximately $2P$ state elements. Mixed-precision training can also retain master weights or scaler state.

Weights are central to inference, but resuming training along the same trajectory requires the optimizer, scheduler, step, and random state.


Count the correspondence between parameter positions and the two state arrays.

<figure class="lesson-figure" markdown="1">

![Three parameter coordinates align with three first-moment and three second-moment state entries plus a separate step record](../../figures/assets/N05/N05-08-state-entries.svg)

<figcaption>This shows array positions for P = 3. Each parameter position corresponds to one first-moment and one second-moment position, adding 6 = 2P state elements. The step record is separate, and moments are not forward parameters.</figcaption>

</figure>

## Example 1. First momentum step

With $\theta_0=2$, target $0.5$, and $L=(\theta-0.5)^2$, the gradient is $g_1=3$. For $u_0=0$, $\mu=0.9$, and $\eta=0.1$,

\[
u_1=0.9\cdot0+3=3,
\qquad
\theta_1=2-0.1\cdot3=1.7
\]

There is no previous gradient at the first step, so the buffer equals the current gradient.

## Example 2. First AdamW step

With $\beta_1=0.9$ and $\beta_2=0.999$,

\[
m_1=0.1\cdot3=0.3,
\qquad
v_1=0.001\cdot9=0.009
\]

After bias correction, $\hat m_1=3$ and $\hat v_1=9$. If $\eta=0.1$, $\lambda=0.01$, and $\epsilon$ is small enough to ignore, the adaptive update is 0.1 and the decay update is 0.002.

\[
\theta_1^{\mathrm{AdamW}}=2-0.1-0.002=1.898
\]


Check the different enlarged scales before reading the two displacements.

<figure class="lesson-figure" markdown="1">

![Two explicitly labeled parameter scales show adaptive displacement minus one tenth and a zoomed decay displacement minus two thousandths ending at one point eight nine eight](../../figures/assets/N05/N05-08-adamw-displacements.svg)

<figcaption>The upper scale shows movement from 2 to 1.9 under the adaptive term. The lower scale zooms in around 1.9 to show decay 0.002. Its arrow appears long because it uses a different enlarged scale; the final value is 1.898.</figcaption>

</figure>

## Execution exercise

### Execution environment and sources

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Verification date: 2026-10-01
- Component category: `Stable core`
- Example ID: `n05_08_adamw_state`
- Source code: `labs/N05/n05_08_adamw_state.py`
- Test: `tests/N05/test_n05_08.py`
- Run command: `.venv\Scripts\python.exe -m labs.N05.n05_08_adamw_state`

### Resource budget

The example uses 1 scalar parameter and 1 update. Optimizer equations are implemented directly through tensor operations, with a hard timeout of 10 seconds.

### Actual code and execution results

The site build inserts the source code and actual execution results at the location below.

<!-- N05_EXAMPLE: n05_08_adamw_state -->

### State and update checks

Tests check gradient 3, momentum buffer 3, Adam moments, and bias correction. After separating adaptive update 0.1 from decay update 0.002, they verify the final parameter 1.898.

## What to check when reading an implementation

Do not infer an exact update from the optimizer's name alone. Check epsilon placement, weight-decay order, foreach or fused implementations, and the momentum convention. When the same mathematical expression is implemented with parallel kernels, test whether results agree within numerical tolerance.

## Connection to model interpretation

Weight differences between two training checkpoints do not reflect only gradients within that interval. Accumulated optimizer state from previous steps, the learning-rate schedule, and batch order also contribute.

Weight snapshots alone allow observation of representation changes when analyzing learning dynamics. Replaying why a particular update occurred additionally requires optimizer state and data order.


Compare the next values from two checkpoints with different buffers.

<figure class="lesson-figure" markdown="1">

![Two momentum resumes share parameter five and current gradient minus one but buffers zero and two produce next parameters five point one and four point nine two](../../figures/assets/N05/N05-08-same-weight-state.svg)

<figcaption>The momentum convention, θ = 5, g = −1, μ = 0.9, and η = 0.1 all match. Previous buffers 0 and 2 alone give new buffers −1 and 0.8 and next parameters 5.1 and 4.92. Weights alone cannot replay the next update.</figcaption>

</figure>

## Common misconceptions

### Misconception 1. Optimizer state is a trainable parameter

$m_t$ and $v_t$ are state used to calculate updates. They are distinct from forward-model parameters learned through gradients.

### Misconception 2. AdamW weight decay is the same as adding an $L_2$ penalty to Adam's loss

With Adam's adaptive scaling, the two updates generally differ. AdamW separates decay from the loss-gradient update.

### Misconception 3. A weight file is sufficient to resume training from the same point

It can give the same starting predictions. Reproducing the next update requires moments, the step, scheduler, and random state.

## Exercises

### 1. Momentum buffer

For $u_{t-1}=2$, $g_t=-1$, and $\mu=0.9$, find $u_t$.

<details>
<summary>Show solution</summary>

$u_t=0.9\cdot2-1=0.8$.

</details>

### 2. Momentum update

In the previous problem, find the new parameter if $\theta_{t-1}=5$ and $\eta=0.1$.

<details>
<summary>Show solution</summary>

$\theta_t=5-0.1\cdot0.8=4.92$.

</details>

### 3. First moment

For $m_0=0$, $g_1=4$, and $\beta_1=0.9$, find $m_1$ and $\hat m_1$.

<details>
<summary>Show solution</summary>

$m_1=0.1\cdot4=0.4$ and $\hat m_1=0.4/(1-0.9)=4$.

</details>

### 4. State size

A float tensor has 1000 parameters, with Adam first and second moments stored in the same dtype. How many moment-state elements are there?

<details>
<summary>Show solution</summary>

Each moment tensor has 1000 elements, totaling 2000. The step and framework-specific additional state are separate.

</details>

### 5. Checkpoint purpose

Explain why inference deployment and exact training resume need different artifacts.

<details>
<summary>Show solution</summary>

Inference uses model weights and configuration needed for the forward pass. Exact resume must determine the next update, so it also requires optimizer and scheduler state, the step, random state, and data order.

</details>

### 6. Critiquing a claim

Evaluate the conclusion that the layer with the largest weight change between two checkpoints received the largest gradients in that interval.

<details>
<summary>Show solution</summary>

Weight changes result from moments, adaptive scaling, weight decay, and learning rates as well as gradients. Gradient magnitude cannot be uniquely inferred without saved optimizer state and step-level records.

</details>

## Sources and update boundaries

Moment estimates and bias correction follow [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980), while decoupled decay follows [Decoupled Weight Decay Regularization](https://arxiv.org/abs/1711.05101). Actual library options and kernels can vary by version, so this lesson uses the specified equations as its reference calculation.

## Lesson summary

- Momentum accumulates previous gradient directions in a buffer.
- Adam stores first and second moments and the step as optimizer state.
- Bias correction adjusts the initial bias of moments started at zero.
- AdamW separates adaptive updates from weight decay.
- Training resume requires more state than weights alone.

## Pass criteria

You pass when you can answer these questions without consulting the material:

- Can you calculate a momentum buffer and parameter update?
- Can you calculate Adam's two moments and bias correction?
- Can you distinguish AdamW's two update terms?
- Can you relate optimizer-state size to the parameter count?
- Can you explain the interpretation limits of a weight-only checkpoint?

## Next lesson

- [N05-09 PyTorch tensors, shape, and dtype](N05-09-pytorch-tensor-shape-dtype.md)

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] The momentum convention is stated.
- [x] Adam moments and bias correction are separated.
- [x] AdamW's adaptive update and decay are separated.
- [x] Every exercise has a solution.
- [x] Strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and math rendering are checked.
- [x] Execution code is not manually duplicated in Markdown.
- [x] Source-code and test paths, resource budgets, and verification dates are recorded.
- [x] Shape, numerical-value, and gradient tests are provided.
