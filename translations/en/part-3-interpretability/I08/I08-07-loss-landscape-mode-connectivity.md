---
id: "I08-07"
title: "Loss landscape and mode connectivity"
part: 3
stage: "I08"
status: "complete"
prerequisites: ["I08-06", "M01-11"]
estimated_time: "90–120 minutes"
---

# I08-07. Loss landscape and mode connectivity

## Why this lesson matters

Two checkpoints can both have low loss, but whether loss stays low between them is a separate question. A barrier along straight interpolation and an optimized curved path provide different evidence. Loss-landscape visualization views a high-dimensional function through a selected low-dimensional slice, so it should not be interpreted as the entire landscape.

## Learning objectives

- Define a loss profile along a parameter path.
- Compute a straight-interpolation barrier.
- Distinguish a low-loss curve from an actual training trajectory.
- Explain how coordinates and normalization affect a landscape plot.

## Prerequisite check

- Prerequisite lessons: [I08-06 Hessian spectrum](I08-06-hessian-spectrum.md), [M01-11 Directional derivatives and gradients](../../part-1-foundations/M01/M01-11-directional-derivative-gradient.md)
- Check question: Why does local Hessian information not determine the loss between two distant minima?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\gamma(\alpha)$ | `gamma of alpha` | Parameter path connecting two points | $[0,1]\to\mathbb R^p$ |
| $\gamma_{\mathrm{lin}}(\alpha)$ | `gamma lin of alpha` | Straight interpolation | $\mathbb R^p$ |
| $B(\gamma)$ | `B of gamma` | Maximum loss barrier relative to the endpoints | nonnegative scalar |
| mode connectivity | `mode connectivity` | Solutions connected by a low-loss path | path property |
| basin | `basin` | Region around low loss under selected optimization and coordinates | informal region |

## 1. Specify the path first

The straight path between two parameter vectors $\theta_a,\theta_b$ is

$$
\gamma_{\mathrm{lin}}(\alpha)=(1-\alpha)\theta_a+\alpha\theta_b,
\qquad 0\le\alpha\le1
$$

The barrier can be defined as

$$
B(\gamma)=\max_\alpha L(\gamma(\alpha))-
\max\{L(\theta_a),L(\theta_b)\}
$$

Fix the evaluation data and $\alpha$ grid to make the value reproducible.

This expression measures how much the path's highest loss exceeds the higher endpoint loss. Because the path includes both endpoints, the maximum along the continuous path cannot be below the endpoint maximum, so the barrier is nonnegative. A barrier of 0 does not mean that loss is constant along the path. The path can pass through lower losses or rise from the lower-loss endpoint to the higher-loss endpoint.

The maximum computed on an actual grid is the maximum among observations on that grid. Missing a peak between points on the continuous path underestimates the barrier. On the same path and data, adding finer grid points while retaining the existing points cannot decrease the observed maximum. Without measuring between grid points, do not report that the maximum over the entire continuous path has been found exactly.

Identify the height difference measured by the barrier.

<figure class="lesson-figure" markdown="1">

![A loss profile with endpoint maximum point one and peak point seven; their vertical difference is the barrier point six.](../../figures/assets/I08/I08-07-barrier-reference.svg)

<figcaption>This mathematical profile uses the existing exercise's endpoint loss of 0.1 and peak of 0.7. The barrier is not the absolute loss of 0.7, but the height of 0.6 above the higher endpoint loss.</figcaption>
</figure>

Even a zero-barrier path can have changing intermediate loss.

<figure class="lesson-figure" markdown="1">

![A curved loss profile dips below equal endpoint losses and has zero barrier despite nonconstant loss.](../../figures/assets/I08/I08-07-zero-barrier-nonconstant.svg)

<figcaption>This mathematical profile has loss 0.5 at both endpoints and 0.1 in the middle. Its maximum does not exceed the endpoint maximum, so B=0, although the path's loss is not constant.</figcaption>
</figure>

Distinguish the observed grid maximum from the continuous-path maximum.

<figure class="lesson-figure" markdown="1">

![A narrow loss peak lies between three coarse samples and is detected by a nested grid that retains the old sample positions.](../../figures/assets/I08/I08-07-grid-misses-peak.svg)

<figcaption>The coarse grid 0,0.5,1 misses the peak near α=0.25 in this continuous mathematical profile. A finer grid retaining the original points detects it. The continuous curve is an illustrative known profile, not evidence that actual measurements have supplied unobserved intermediate values.</figcaption>
</figure>

## 2. Failure of a straight path does not rule out connectivity

Even with a high barrier along a straight path, a curved low-loss path can exist. Conversely, low loss along one selected curve does not mean that all points or all models are connected. Mode connectivity is a claim about the existence of a path.

The exercise's two endpoints are $(1,0)$ and $(-1,0)$. The straight path $(1-2\alpha,0)$ passes through the origin at its midpoint, giving $L(0,0)=(0-1)^2=1$, while endpoint loss is 0. On the semicircular path $(\cos(\pi\alpha),\sin(\pi\alpha))$, the sum of squared coordinates is 1, so loss is 0 along the entire path. Even when the same endpoints are connected, the chosen path gives a barrier of either 1 or 0. Failure of one straight path is not evidence that every path fails.

Compare two paths connecting the same endpoints in parameter space and in their loss profiles.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A straight segment through the origin and an upper semicircle connect the same points; their loss profiles have barriers one and zero.](../../figures/assets/I08/I08-07-straight-and-curved-paths.svg)

<figcaption>For the existing exercise's L(x,y)=(x²+y²−1)², the straight path passes through the origin and gives a barrier of 1, while the semicircle lies on the unit circle and maintains loss 0. The left panel shows parameter paths; the right shows loss evaluated along those paths. This does not establish that the optimizer actually followed either connection path.</figcaption>
</figure>

## 3. Symmetry and alignment

Without hidden-unit permutation alignment, straight interpolation between two functionally identical models can mix units and produce high loss. Record possible symmetry alignment before comparing connectivity.

The appearance of a loss slice also changes with direction-vector scale and filter normalization. The plot is a measurement of the defined slice.

For example, given reference weights $\theta_0$ and directions $u,v$, a slice measures $L(\theta_0+au+bv)$. Doubling direction $u$ makes the same horizontal coordinate $a$ represent twice the weight movement. Normalization that matches direction magnitudes also changes this correspondence between coordinates and actual movement. The loss function has not changed, but the visible barrier width and slope can change. Movements outside those two directions are not visible in this slice.

Changing unit correspondence can also change the function at the interpolation midpoint.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A pair of jointly permuted ReLU networks has equal endpoint functions; unaligned straight interpolation raises loss while matching unit roles removes this example barrier.](../../figures/assets/I08/I08-07-permutation-interpolation.svg)

<figcaption>In this mathematical two-unit ReLU example, jointly reversing input weights (1,−2) and readout weights (3,−1) preserves the endpoint function. Without aligning corresponding units, the midpoint has a different function and an increased MSE relative to the endpoint function on fixed inputs −2,−1,0,1,2. Aligning both lists to their original order before interpolation removes this example's barrier.</figcaption>
</figure>

Direction scale changes the correspondence between coordinates and actual movement.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Contour slices of the same ring-shaped loss under x equals a and x equals twice a; doubling direction scale halves the horizontal coordinate width.](../../figures/assets/I08/I08-07-slice-axis-rescaling.svg)

<figcaption>For the same mathematical loss, plotting x=2a instead of x=a displays the same actual x movement at half the a coordinate. The contour's horizontal width changes without changing the loss function. In a general high-dimensional model, such a plot does not show the landscape outside the two selected directions.</figcaption>
</figure>

## 4. CPU exercise

<!-- I08_EXAMPLE: i08_07_loss_path -->

Connect two points on the circle for $L(x,y)=(x^2+y^2-1)^2$. The straight path through the origin has a barrier, but the semicircular path maintains loss 0.

## Common misconceptions

### Misconception 1. A low-loss path is the actual training path

A connection path can be evidence of existence found after training. Evidence that the optimizer followed it requires a separately recorded trajectory.

### Misconception 2. A 2D contour is the whole landscape

It is only a slice along two selected directions in a high-dimensional space. Barriers and flatness in other directions are not visible.

## Exercises

### 1. Midpoint

For a 1-dimensional straight path with $\theta_a=0$ and $\theta_b=2$, what is the point at $\alpha=0.25$?

<details><summary>Show solution</summary>

It is $(1-0.25)0+0.25\times2=0.5$.

</details>

### 2. Barrier

If both endpoint losses are 0.1 and the maximum loss on the path is 0.7, what is the barrier?

<details><summary>Show solution</summary>

It is $0.7-0.1=0.6$.

</details>

### 3. Grid error

What problem can arise if $\alpha$ is evaluated only at 0, 0.5, and 1?

<details><summary>Show solution</summary>

A narrow, high barrier between those points can be missed, underestimating the maximum loss.

</details>

### 4. Symmetry

Explain why permutation alignment can lower a straight-path barrier.

<details><summary>Show solution</summary>

Pairing units with the same roles reduces inaccurate mixing of different functions in the intermediate weights.

</details>

### 5. Existence and trajectory

Does finding one low-loss curve establish that SGD followed that path?

<details><summary>Show solution</summary>

No. Actual updates and checkpoints must be tracked.

</details>

### 6. Data dependence

Why must test loss be measured separately along a path even if its training loss stays low?

<details><summary>Show solution</summary>

Even with the same training objective, generalization behavior can change along the path. The two metrics have different estimands.

</details>

## Sources and boundaries for updates

For a mechanistic analysis of mode connectivity, consult [Lubana et al. (2023)](https://proceedings.mlr.press/v202/lubana23a.html). This lesson addresses differences between path-based claims without implementing a curve-optimization algorithm.

## Lesson summary

- A loss profile depends on the selected parameter path and data.
- A straight-path barrier does not imply the absence of a curved path.
- A low-loss path is not the actual optimizer trajectory.
- Record symmetry alignment and grid resolution.

## Pass criteria

- Can you define and compute a path and its barrier?
- Can you distinguish straight interpolation from mode connectivity?
- Can you explain the limitations of a landscape slice?

## Next lesson

- [I08-08 Influence function](I08-08-influence-function.md)

## Author checklist

- [x] The path and barrier are defined.
- [x] An actual trajectory is distinguished from a path found afterward.
- [x] Every exercise has a solution.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Claim strength and spoken readings have been checked.
- [x] Internal links and equations have been checked.
