---
id: "I08-10"
title: "Grokking and phase transitions"
part: 3
stage: "I08"
status: "complete"
prerequisites: ["I08-09", "M04-03"]
estimated_time: "90–120 minutes"
---

# I08-10. Grokking and phase transitions

## Why this lesson matters

Grokking has been reported as a late rise in test performance after training performance has already saturated. But sparse evaluation, thresholds, and axis choices can make gradual changes look abrupt. Using the term “phase transition” requires distinguishing observed curves, transition widths, and alternative explanations.

## Learning objectives

- Define delayed generalization through training and test curves.
- Measure transition location and width.
- Explain how checkpoint spacing affects apparent abruptness.
- Avoid extending grokking in one toy task into a universal law for models.

## Prerequisite check

- Prerequisite lessons: [I08-09 Feature emergence](I08-09-feature-emergence.md), [M04-03 Random variables and distributions](../../part-1-foundations/M04/M04-03-random-variables-distributions.md)
- Check question: Can two measurements alone determine the shape of the curve between them?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $A_{train}(t)$ | `A train of t` | Training accuracy at step $t$ | $[0,1]$ |
| $A_{test}(t)$ | `A test of t` | Test accuracy at step $t$ | $[0,1]$ |
| $t_{fit}$ | `t fit` | First step meeting the training criterion | nonnegative integer |
| $t_{gen}$ | `t gen` | First step meeting the generalization criterion | nonnegative integer |
| transition width | `transition width` | Step difference between a low and high threshold | nonnegative scalar |

## 1. Delayed generalization

Choose thresholds $\tau_{fit},\tau_{gen}$ and define

$$
t_{fit}=\min\{t\in C:A_{train}(t)\ge\tau_{fit}\},\qquad
t_{gen}=\min\{t\in C:A_{test}(t)\ge\tau_{gen}\}
$$

If $t_{gen}\gg t_{fit}$, generalization can be described as delayed after training fit. Predefine thresholds or perform a sensitivity analysis.

$C$ is the set of evaluated checkpoints. The two times are observed steps at which the respective accuracies first reach their criteria. If a curve never reaches its criterion, its crossing time and the difference between the times are undefined. Report their difference as the delay, but also check whether training performance stays high throughout that interval. Two first-crossing values from curves that rise above a criterion and then fall do not establish delayed generalization after sustained training fit.

In the CPU exercise, training accuracy reaches 0.99 at step 200 and stays high afterward. Test accuracy first reaches 0.9 at step 1,600, giving an observed delay of $1600-200=1400$ steps. This difference is relative to the specified criteria and observation grid, not the exact crossing time at unobserved steps.

Check what is maintained between the observed training and test crossings.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The existing synthetic train trace reaches the fit criterion at step two hundred and remains high, while test first reaches its criterion at sixteen hundred, a delay of fourteen hundred.](../../figures/assets/I08/I08-10-observed-generalization-delay.svg)

<figcaption>In the existing synthetic CPU values, training accuracy reaches 0.99 at step 200 and stays high. Test accuracy first meets the 0.9 criterion at step 1600, giving an observed delay of 1400 steps. This is a result for the specified grid and criteria, not the exact unobserved first-crossing time.</figcaption>
</figure>

Compare a case where first crossings are not enough.

<figure class="lesson-figure" markdown="1">

![A hypothetical training curve first reaches point nine nine, then dips before a late test improvement; first crossing times alone do not establish maintained training fit.](../../figures/assets/I08/I08-10-transient-fit-counterexample.svg)

<figcaption>This mathematical counterexample has training accuracy exceed 0.99 first but drop to 0.5 in between. It is not a new CPU trace result; it shows why two first crossings do not establish that high training performance was maintained.</figcaption>
</figure>

## 2. Measure abruptness

Possible measures include the step width for test accuracy to rise from 0.2 to 0.8, a local slope, or a sigmoid fit. If checkpoint spacing is wider than the transition, its actual abruptness cannot be identified.

The difference between the observed low- and high-threshold crossing times gives a threshold-based width. The interval's average slope is the accuracy difference divided by the step difference. A large change and a short transition width are separate pieces of information; report both. Accuracy on a fixed set of $N$ test questions also moves by $1/N$ whenever one answer changes correctness. If small output-margin changes flip several questions at once, accuracy may move sharply. Compare it with loss or margins to avoid mistaking the metric's decision boundary for a discontinuity in internal structure.

Linear and logarithmic step axes make the same data look different. Provide a raw-step table and evaluation frequency as well.

If the metric is approximated by a differentiable continuous curve $A(t)$ and the horizontal coordinate is changed to $\log t$ for positive $t$, the chain rule gives $dA/d(\log t)=t\,dA/dt$. The same rate per step can look steeper later on a logarithmic axis. This is a coordinate change for the curve approximation, not differentiation of the discrete accuracy observations themselves. The logarithm of step 0 is undefined; if it is omitted or another transformation is used, record the rule.

Do not use a large change and a short transition width interchangeably.

<figure class="lesson-figure" markdown="1">

![The exercise observations cross low and high test-accuracy thresholds at one thousand and fourteen hundred steps, giving a four-hundred-step width.](../../figures/assets/I08/I08-10-transition-width.svg)

<figcaption>The exercise's observed times for 0.2 and 0.8 differ by 400 steps, with average rate 0.6/400=0.0015. The dotted line joins the points for illustration; it is not a measured intervening trajectory or an exact continuous crossing.</figcaption>
</figure>

Compare the same data under a change of axis alone.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The same positive-step synthetic train and test observations appear on linear and logarithmic horizontal axes; step zero is omitted from both.](../../figures/assets/I08/I08-10-raw-and-log-step.svg)

<figcaption>Both panels use only the same positive-step observations. A logarithmic axis changes horizontal distances and visual slopes, not values or raw steps. Since log 0 is undefined, step 0 is omitted from both panels. This is not differentiation of discrete accuracy.</figcaption>
</figure>

Check the relation between continuous margins and discrete accuracy.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Five continuously shifting correct-class margins produce discrete one-fifth jumps in accuracy when they cross zero.](../../figures/assets/I08/I08-10-margin-and-quantized-accuracy.svg)

<figcaption>This mathematical N=5 example counts an answer as correct when its correct-class margin is positive. Even with continuously varying margins, accuracy moves by 1/5 when a correctness judgment flips. A sharp metric rise alone does not prove an internal structural discontinuity or a theoretical phase transition.</figcaption>
</figure>

## 3. The scope of “phase transition”

In physics, a phase transition has a rigorous structure involving a system-size limit and an order parameter. Machine-learning papers sometimes use it more loosely for an abrupt empirical change. This textbook distinguishes an abrupt transition in an observed metric from a theoretical phase transition.

## 4. CPU exercise

<!-- I08_EXAMPLE: i08_10_grokking_transition -->

In the synthetic trace, training accuracy reaches 0.99 at step 200 and test accuracy crosses 0.9 at step 1600. The 1400-step delay is relative to the defined thresholds and grid.

## Common misconceptions

### Misconception 1. A late test improvement means an internal algorithm appeared suddenly

A behavioral curve alone does not reveal the internal mechanism. Track representation and intervention metrics too.

### Misconception 2. One seed's curve establishes the phenomenon

Transition location and occurrence can depend on initialization, the data split, and regularization.

## Exercises

### 1. Calculate delay

Find the delay for $t_{fit}=500$ and $t_{gen}=4500$.

<details><summary>Show solution</summary>

It is $4500-500=4000$ steps.

</details>

### 2. Transition width

Test accuracy crosses 0.2 at step 1000 and 0.8 at step 1400. What is the threshold-based width?

<details><summary>Show solution</summary>

It is 400 steps. The actual crossings lie within observation intervals, so this value is also a grid approximation.

</details>

### 3. Logarithmic axis

Why should raw steps also be provided with a logarithmic step axis?

<details><summary>Show solution</summary>

The axis transforms visual distances. Readers need to check the actual training budget and transition intervals.

</details>

### 4. Internal evidence

What additional measurements could investigate mechanism changes around grokking?

<details><summary>Show solution</summary>

Measure a fixed probe, representation alignment, feature activations, and ablation effects together at each checkpoint.

</details>

### 5. Reproducibility

A transition appeared in only 2 of 5 seeds. What should be reported?

<details><summary>Show solution</summary>

Report the occurrence rate, each seed's curve, and the distribution of transition locations. Do not hide them behind only the average curve.

</details>

### 6. Critique a claim

Critique “Accuracy rose from 0.2 to 0.9 between two checkpoints, proving a phase transition.”

<details><summary>Show solution</summary>

Without intervening observations, the transition width is unknown, and theoretical phase-transition conditions have not been provided. Only a large observed change can be claimed.

</details>

## Evidence and update boundaries

The original report of delayed generalization on small algorithmic datasets is [Power et al. (2022)](https://arxiv.org/abs/2201.02177). The phenomenon may vary with task, dataset size, and regularization; do not treat it as a required stage for general language models.

## Lesson summary

- Grokking can be measured as delayed test generalization after training fit.
- Transition location and width depend on thresholds and the grid.
- A sharp behavioral rise is not direct evidence of an abrupt internal mechanism change.
- Evaluate reproducibility across seeds and with denser observations.

## Pass criteria

- Can you calculate delayed generalization and transition width?
- Can you identify the limits of sparse checkpoints?
- Can you distinguish an empirical transition from a theoretical phase transition?

## Next lesson

- [I08-11 Seeds and data order](I08-11-seed-data-order.md)

## Author checklist

- [x] A measurement definition of grokking is given.
- [x] Abruptness and phase-transition claims are bounded.
- [x] Every exercise has a solution.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Claim strength and spoken readings have been checked.
- [x] Internal links and equations have been checked.
