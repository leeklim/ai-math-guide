---
id: "A09-DYN-08"
title: "Capstone exercise: learning trajectory analysis"
part: 4
stage: "A09-DYN"
status: "complete"
prerequisites: ["A09-DYN-01", "A09-DYN-02", "A09-DYN-03", "A09-DYN-04", "A09-DYN-05", "A09-DYN-06", "A09-DYN-07"]
estimated_time: "120–180 minutes"
---

# A09-DYN-08. Capstone exercise: learning trajectory analysis

## Why this lesson matters

Joining a few checkpoints with lines does not explain learning dynamics. The time coordinate, state, distance, stochastic repetitions, and interpolation error must be fixed to separate claims about trajectories, stability, and transitions.

## Learning objectives

- Define state and time for learning trajectory analysis.
- Plan measurements of drift, noise, and local stability.
- Design controls that include paired seeds and checkpoint resolution.
- Judge the strength of claims supported by an observed trajectory.

## Prerequisite check

- Prerequisite lessons: [A09-DYN-01–07](A09-DYN-07-continuous-time-sgd.md)
- Check question: Why does the choice between optimizer steps and processed token counts as time change the result?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $z_k$ | `z sub k` | Checkpoint state summary | Vector |
| $\Delta z_k$ | `delta z sub k` | Successive displacement | Vector |
| $\hat b(z)$ | `b hat of z` | Empirical local drift | Vector |
| $\hat C(z)$ | `C hat of z` | Empirical update covariance | PSD matrix |

## Analysis contract

Limit the claim to: “Under a fixed training recipe, checkpoint summaries from paired seeds show reproducible patterns of drift and fluctuation.” Specify which elements of state the question requires: parameter projections, function metrics, representation statistics, or optimizer state.

Choose the time axis in advance from optimizer steps, processed tokens, or cumulative learning rate. Linear interpolation between checkpoints must not be described as an observation of the actual update path.

Write the chosen time values as $\tau_k$. The observed displacement is $\Delta z_k=z_{k+1}-z_k$, and the average movement per unit time corresponds to $\Delta z_k/(\tau_{k+1}-\tau_k)$. Records spaced equally in steps and records spaced equally in tokens do not measure drift in the same units. When using cumulative learning rate, compute the time interval by summing the learning rates of all updates performed between checkpoints. This time coordinate can itself differ across comparison conditions, so record it along with the recipe.

If $z_k$ is a parameter projection or a metric summary, it may not contain the entire original optimizer state. Even when the same $z$ is reached, hidden parameters or moments can differ, changing the distribution of the next movement. Report $\hat b(z)$ as an empirical mean measured under the chosen summary and conditions. Do not assume that $z$ alone gives closed Markov dynamics.

The time axes and augmented-state coordinates below show differences hidden by the same observations.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Illustrative observed states zero one two have equally spaced optimizer steps zero one two but tokens zero one hundred three hundred and cumulative learning rates zero one tenth fifteen hundredths so slopes differ under the three coordinates](../../figures/assets/A09-DYN/A09-DYN-08-time-coordinate-spacing.svg)

<figcaption>The same three illustrative observations z = 0, 1, 2 are plotted. Although each interval has Δz = 1, step spacing 1, token spacings 100 and 200, and cumulative learning-rate spacings 0.1 and 0.05 produce different rates. The lines are guides for comparing observed points.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Illustrative momentum states at identical observed parameter zero and moments plus one minus one update with factor zero point nine learning rate one tenth zero gradient to parameters minus zero point zero nine and plus zero point zero nine respectively](../../figures/assets/A09-DYN/A09-DYN-08-hidden-moment-state.svg)

<figcaption>The illustrative step uses v′ = 0.9v, θ′ = θ − 0.1v′, and gradient 0. Both starting states have observed z = θ equal to 0, but their hidden v = ±1 gives next θ′ = ∓0.09. Matching z alone does not give the same next-state law.</figcaption>

</figure>

## Measurement procedure

1. Create paired conditions sharing the same initialization and data order.
2. At fixed checkpoints, record loss, function distance, update norm, and summary state.
3. Estimate $\hat b$ and $\hat C$ using repeated micro-batch gradients.
4. Obtain stability measures using a local Jacobian or Hessian-vector product.
5. Perform sensitivity analysis with greater checkpoint density and a time-shuffle null.

Repeat batches while holding the checkpoint fixed. Several gradients at the same parameters estimate the gradient mean and covariance, but this is not immediately the update covariance of summary $z$. A plain SGD parameter update multiplies the gradient by $-\eta$, so its covariance is multiplied by $\eta^2$. For a linear projection $z=A\theta$, projected update covariance is $\eta^2ACA^\top$. For nonlinear metric summaries or momentum and Adam updates, restore the same checkpoint parameters and optimizer state in a copy before every trial, apply a one-step update, and compute the actual $\Delta z$. Advancing the optimizer sequentially measures a moving path, not repeated noise under fixed conditions.

Distinguish the reference state of restored repetitions from the covariance projection calculation below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three one-step replicas each start by restoring the same parameter and optimizer state checkpoint then use batches A B C and record displacements relative to that checkpoint whereas sequential updates move state zero to state one then state two](../../figures/assets/A09-DYN/A09-DYN-08-restore-one-step-replicates.svg)

<figcaption>On the left, the same parameters and optimizer state are restored before each batch, measuring Δz from the same reference. On the right, one run advances sequentially and changes the starting state. The numbers 0, 1, and 2 are state indices, not actual measured values.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Illustrative gradient covariance matrix four one one one with learning rate one tenth gives parameter-update covariance one hundredth times that matrix and linear summary delta z equals delta theta one plus delta theta two has variance zero point zero seven with projected covariance-ellipse extrema plus minus square root zero point zero seven](../../figures/assets/A09-DYN/A09-DYN-08-projected-update-covariance.svg)

<figcaption>The illustrative values are C = [[4, 1], [1, 1]], η = 0.1, and A = (1, 1). The upper contour is an ellipse of update covariance η²C, and the linear summary Δz = Δθ₁ + Δθ₂ has variance η²ACAᵀ = 0.07. Below, ±√0.07 is a covariance scale, not a probabilistic bound containing every update.</figcaption>

</figure>

For local stability, also specify which update is linearized. In parameter-only gradient flow, the negative loss Hessian is the drift Jacobian; in plain gradient descent, the update Jacobian is $I-\eta H$. An optimizer with moments requires linearization of the augmented-state update. A single JVP or HVP gives only the response in the chosen direction. To report a leading rate, specify an eigenvalue estimation procedure and its error as well. Do not equate local sensitivity at a moving training checkpoint with the long-term stability of a fixed point.

Comparing the responses in two directions below reveals the scope of a single JVP measurement.

<figure class="lesson-figure" markdown="1">

![Illustrative discrete update Jacobian diagonal zero point nine zero point six maps selected direction e two to zero point six e two but an unmeasured e one direction has larger multiplier zero point nine shown on the same two-dimensional axes](../../figures/assets/A09-DYN/A09-DYN-08-one-direction-jvp.svg)

<figcaption>For illustrative H = diag(1, 4) and η = 0.1, the discrete Jacobian is J = diag(0.9, 0.6). The JVP for e₂ gives response 0.6e₂ in the chosen direction, but the multiplier 0.9 of the other direction e₁ is larger. Do not generalize this figure's J and checkpoint to the actual optimizer's long-term stability.</figcaption>

</figure>

Sensitivity analysis with reduced checkpoint spacing compares states actually saved more densely, not additional interpolated points. When a metric changes abruptly, first report a candidate change-point interval between adjacent observation times. Time shuffling is a control that removes the ordering information in recorded values. For temporally correlated data, an arbitrary permutation is not automatically a valid significance-test null. Distinguish a control for order dependence from a test, and state the null assumptions for the latter.

Read actual observations, interpolated points, and the reordered control separately below.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Three panels compare illustrative observed metric values one half one half nine tenths at steps zero ten twenty with hollow interpolated points on their connecting line and actual extra observations at step fourteen one half step fifteen nine tenths narrowing the candidate change interval to fourteen fifteen](../../figures/assets/A09-DYN/A09-DYN-08-dense-observed-checkpoints.svg)

<figcaption>The illustrative sparse observations are 0.5, 0.5, and 0.9 at steps 0, 10, and 20. Adding the middle panel's hollow circles by interpolation does not narrow the candidate interval (10, 20]. With actual extra observations of 0.5 at step 14 and 0.9 at step 15, as in the lower panel, the candidate interval (14, 15] can be reported.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Two panels contain the same three low and three high illustrative metric values but original order groups lows followed by highs while a reordered control alternates high low values without establishing a valid significance-test null](../../figures/assets/A09-DYN/A09-DYN-08-time-order-shuffle.svg)

<figcaption>Both panels retain the same illustrative values: three instances of 0.5 and three of 0.9. Reordering changes the temporal structure of consecutive low and high values. This control figure alone does not establish a valid significance test or a p-value for temporally correlated data.</figcaption>

</figure>

## Results record

| Question | Estimand | Measurement | Main limitation |
|---|---|---|---|
| Mean movement | Empirical drift at a fixed state under fixed conditions | Matched-condition repetition mean $\Delta z/\Delta\tau$ | Projection and hidden state |
| Stochasticity | Update covariance at a fixed checkpoint | Batch-wise one-step $\Delta z$ from restored state | Sampling assumptions and omitted state |
| Local stability | Leading local rate | JVP or HVP | Linearization |
| Transition | Change-point interval | Dense checkpoints | Resolution and multiple testing |

A paired seed is the unit that pairs runs sharing initialization and data order when calculating differences between conditions. Do not count the multiple checkpoints within each run as independent seeds. Record the time interval used for drift and the number of batch repetitions used to measure covariance separately. Label stability measures as referring to continuous drift or a discrete update. These records preserve the fact that the table's four rows concern different estimands even when they examine the same trajectory.

The nested structure below distinguishes seed pairs used to calculate condition differences from checkpoints.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two distinct seed pairs each share initialization and data order across conditions A B with three nested observed checkpoints per run and one paired difference per seed so six checkpoints in each condition produce two independent seed pairs rather than six](../../figures/assets/A09-DYN/A09-DYN-08-paired-run-checkpoint-hierarchy.svg)

<figcaption>To illustrate the structure, the figure shows 2 seed pairs and 3 checkpoints within each run. Conditions A and B with the same seed share initialization and data order; checkpoints are nested within that run. The 6 points in each condition are not counted as 6 independent seeds. Condition differences are computed at the seed-pair level.</figcaption>

</figure>

## Common misconceptions

- A smooth plot does not mean that the underlying continuous path was observed.
- A trajectory averaged across seeds may not be a trajectory actually traversed by any individual run.

## Exercises

### 1. Time axis
When batch sizes differ across runs, is matching optimizer steps alone fair?
<details><summary>Show solution</summary>

Generally not. Also match processed examples or tokens and the learning-rate schedule, or include the differences in the estimand.
</details>

### 2. Interpolation
If loss is low along the straight line between two checkpoints, can one say that actual SGD followed that line?
<details><summary>Show solution</summary>

No. This measures a separate interpolation path and is not evidence of the actual update path.
</details>

### 3. Noise covariance
Why are gradients from several mini-batches needed at the same checkpoint?
<details><summary>Show solution</summary>

Repeated batch sampling is needed to estimate the conditional mean and covariance.
</details>

### 4. Transition claim
What conclusion is appropriate if the metric change point differs substantially across seeds?
<details><summary>Show solution</summary>

Report substantial variation in transition timing under the recipe, and avoid claiming a universal phase transition at a single step.
</details>

## Evidence and update boundaries

This exercise connects ODE and SDE approximations to checkpoint study design. It does not assume in advance that a particular optimizer follows a particular SDE; empirical residual diagnostics determine the approximation's scope.

## Lesson summary

- Fix state, time, and metrics first.
- Measure drift, noise, and stability as different estimands.
- Assess resolution and variance using dense checkpoints and paired seeds.
- Distinguish interpolation from actual learning paths.

## Pass criteria

- Can you write a claim–estimand–measurement–control specification for a learning trajectory?
- Can you propose diagnostics that identify possible failures of a continuous-time interpretation?

## Next lesson

- The next optional module is A09-SYM.

## Author checklist

- [x] The analysis contract and claim limitations for learning trajectories are included.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
