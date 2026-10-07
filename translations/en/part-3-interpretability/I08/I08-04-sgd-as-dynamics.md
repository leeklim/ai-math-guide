---
id: "I08-04"
title: "Viewing SGD as dynamics"
part: 3
stage: "I08"
status: "complete"
prerequisites: ["I08-03", "N05-07", "M01-11"]
estimated_time: "90–120 minutes"
---

# I08-04. Viewing SGD as dynamics

## Why this lesson matters

A checkpoint sequence is a trajectory produced by an update rule, not a list of independent models. Viewing gradient descent as discrete dynamics helps explain how learning rate, curvature, and checkpoint spacing constrain the observed path. Continuous-time gradient flow is a useful approximation, but it is not the actual optimizer.

## Learning objectives

- Write a gradient descent update as a state transition.
- Connect discrete updates to gradient flow.
- Calculate the stable learning-rate condition for a quadratic loss.
- Explain the limits of the continuous-time approximation.

## Prerequisite check

- Prerequisite lessons: [I08-03 Representation alignment](I08-03-representation-alignment.md), [N05-07 Mini-batch gradient descent](../../part-2-neural-computation/N05/N05-07-gradient-descent-mini-batch.md), [M01-11 Directional derivative and gradient](../../part-1-foundations/M01/M01-11-directional-derivative-gradient.md)
- Check question: What is the shape of each term in $\theta_{k+1}=\theta_k-\eta\nabla L(\theta_k)$?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $\theta_{k+1}=\theta_k-\eta g_k$ | `theta sub k plus one equals theta sub k minus eta g sub k` | One discrete update | $\theta,g\in\mathbb R^p$ |
| $\dot\theta(t)$ | `theta dot of t` | Continuous-time parameter velocity | $\mathbb R^p$ |
| $\dot\theta=-\nabla L(\theta)$ | `theta dot equals minus the gradient of L of theta` | Gradient flow | ordinary differential equation |
| $\eta$ | `eta` | Learning rate | positive scalar |
| trajectory | `trajectory` | A sequence of states produced by updates | sequence or curve |

## 1. Discrete state transitions

Full-batch gradient descent is

$$
\theta_{k+1}=F(\theta_k)=\theta_k-\eta\nabla L(\theta_k)
$$

Given the initial value and a deterministic $F$, the entire trajectory is determined. Checkpoints are sparsely saved states along that trajectory.

Read an update's input state separately from its computed next state.

<figure class="lesson-figure" markdown="1">

![The existing one-step example sends parameter two through a gradient three times learning rate point one to next parameter one point seven](../../figures/assets/I08/I08-04-state-transition.svg)

<figcaption>In the exercise's single step, applying update −0.3 to the current parameter 2 gives 1.7. The next transition is computed again from this new state.</figcaption>
</figure>

## 2. Gradient flow

For small $\eta$, set $t=k\eta$. Then

$$
\frac{\theta_{k+1}-\theta_k}{\eta}\approx\dot\theta(t)
$$

gives $\dot\theta=-\nabla L(\theta)$. This approximation helps describe the direction field, but removes finite learning rates, momentum, adaptive state, and mini-batch noise.

Here $k$ counts updates, while $t=k\eta$ is a continuous-time coordinate assigning time $\eta$ between updates. The numerator is the parameter displacement over one step; dividing by $\eta$ gives the interval's average velocity. Substituting the update equation gives $-\nabla L(\theta_k)$ for this velocity. When the gradient varies smoothly and the step is sufficiently small, it approximates the instantaneous derivative. Do not compare the actual step count $k$ and flow time $t$ as though they were the same number.

Applying the chain rule along the flow of a differentiable loss gives $\frac{d}{dt}L(\theta(t))=\nabla L(\theta(t))^\top\dot\theta(t)=-\|\nabla L(\theta(t))\|_2^2$. Loss does not increase along this continuous trajectory. This property does not transfer directly to discrete updates with a finite learning rate.

For the quadratic loss $L(\theta)=\frac12\lambda\theta^2$ with $\lambda>0$, the gradient is $\lambda\theta$, giving

$$
\theta_{k+1}=(1-\eta\lambda)\theta_k.
$$

Repeated multiplication by the same constant gives $\theta_k=(1-\eta\lambda)^k\theta_0$. For a general nonzero initial value to converge to 0, this multiplier must have absolute value less than 1. Solving $|1-\eta\lambda|<1$ gives $0<\eta<2/\lambda$. A positive multiplier shrinks the value without changing its sign; a negative one shrinks it while alternating its sign. At the boundary $\eta=2/\lambda$, the multiplier is $-1$, so the amplitude does not shrink.

The flow solution for the same quadratic is $\theta(t)=\theta_0e^{-\lambda t}$. Differentiating it verifies $\dot\theta=-\lambda\theta$ and the initial condition. The exercise uses $\lambda=1$, $\theta_0=2$, and $\eta=0.1$, so the discrete value after 20 steps is $2(0.9)^{20}$, while the flow value at the corresponding time $t=2$ is $2e^{-2}$. Distinguish why the values approach each other for small steps from why they differ at a finite step size.

Compare the discrete points and continuous flow on the same time scale.

<figure class="lesson-figure" markdown="1">

![Twenty updates of the existing quadratic toy compare to gradient flow at matching time two](../../figures/assets/I08/I08-04-discrete-versus-flow.svg)

<figcaption>The existing quadratic example compares discrete step k=20 with flow time t=2. Even with the horizontal axis matched as t=0.1k, the finite-step values are not exactly equal.</figcaption>
</figure>

The four cases below vary only the learning rate for the same quadratic.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Four exact quadratic update sequences show same-sign decay alternating decay boundary oscillation and divergence](../../figures/assets/I08/I08-04-quadratic-stability-regimes.svg)

<figcaption>These mathematical examples vary the multiplier r=1−ηλ for the same λ=1 quadratic. Distinguish the two decaying cases with |r|&lt;1, the boundary |r|=1, and divergence with |r|&gt;1.</figcaption>
</figure>

## 3. Checkpoint spacing and aliasing

Checkpoints saved every 1000 steps cannot show oscillation or temporary overshoot between them. Equal metrics at two saved points do not imply the same intervening path. To claim an abrupt transition, check whether its interval is sufficiently wide relative to the observation spacing.

Compare different paths through the same two checkpoints.

<figure class="lesson-figure" markdown="1">

![A constant analytic metric and a sine excursion share two orange endpoint measurements a thousand steps apart](../../figures/assets/I08/I08-04-sparse-checkpoints-hide-path.svg)

<figcaption>Matching orange observations at steps 0 and 1,000 permit an intervening path that stays constant or changes and returns. The curves illustrate possibilities in the unobserved interval.</figcaption>
</figure>

## 4. CPU exercise

<!-- I08_EXAMPLE: i08_04_sgd_dynamics -->

For $L(\theta)=\theta^2/2$, compare the discrete trajectory at learning rate 0.1 with $2e^{-t}$ at matching times. They are close, not exactly equal.

## Common misconceptions

### Misconception 1. Gradient flow is the exact equation for AdamW

AdamW has moment state, coordinate-wise scaling, and weight decay. Simple gradient flow approximates only some of that structure.

### Misconception 2. Decreasing loss means a straight path

The gradient direction changes with location. Monotonic decrease in a scalar loss does not determine the geometry of the parameter path.

The following coordinates separate decreasing loss from path shape.

<figure class="lesson-figure" markdown="1">

![An exact two-dimensional quadratic gradient flow curves away from its straight endpoint interpolation while its loss decreases](../../figures/assets/I08/I08-04-decreasing-loss-curved-path.svg)

<figcaption>In this illustrative flow for L=(x²+4y²)/2, loss decreases while the path curves. The dashed line is an analytical straight connection between the endpoints; the blue curve is the actual flow.</figcaption>
</figure>

## Exercises

### 1. One step

Find the next $\theta$ when $\theta=2$, the gradient is $3$, and $\eta=0.1$.

<details><summary>Show solution</summary>

It is $2-0.1\times3=1.7$.

</details>

### 2. Stability condition

Find the range of stable constant learning rates for a quadratic with $\lambda=4$.

<details><summary>Show solution</summary>

It is $0<\eta<2/4=0.5$.

</details>

### 3. Oscillation

What happens to the trajectory if $1-\eta\lambda<0$ and its absolute value is less than 1?

<details><summary>Show solution</summary>

It alternates signs with decreasing amplitude and converges to 0.

</details>

### 4. Flow solution

Write the solution of $\dot\theta=-\theta$ with $\theta(0)=a$.

<details><summary>Show solution</summary>

It is $\theta(t)=ae^{-t}$.

</details>

### 5. Aliasing

If the metric is equal at steps 0 and 1000, can you say it was constant between them?

<details><summary>Show solution</summary>

No. It could have changed and returned. More densely saved checkpoints are needed.

</details>

### 6. Critique a claim

Critique “The straight interpolation between two checkpoints is the training path.”

<details><summary>Show solution</summary>

Straight interpolation is a path constructed by the analyst. The actual optimizer trajectory consists of the unsaved update sequence and is generally not straight.

</details>

## Evidence and update boundaries

Refer to [Li, Tai and E (2019)](https://www.jmlr.org/papers/v20/17-526.html) for continuous-time approximations of stochastic gradient algorithms. This lesson only illustrates the connection through a deterministic quadratic; it does not derive an exact SDE for modern optimizers.

## Lesson summary

- Gradient descent is discrete dynamics in parameter space.
- Gradient flow is a continuous-time approximation for small steps.
- Stability depends jointly on learning rate and curvature.
- Sparse checkpoints hide the intervening path.

## Pass criteria

- Can you connect updates to gradient flow?
- Can you calculate quadratic stability conditions?
- Can you explain the interpretive limits of checkpoint spacing?

## Next lesson

- [I08-05 Mini-batch noise and optimizer state](I08-05-minibatch-noise-optimizer-state.md)

## Author checklist

- [x] Discrete updates and flow are distinguished.
- [x] The stability condition has been checked.
- [x] Every exercise has a solution.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Claim strength and spoken readings have been checked.
- [x] Internal links and equations have been checked.
