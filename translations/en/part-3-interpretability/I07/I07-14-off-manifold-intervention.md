---
id: "I07-14"
title: "Off-manifold interventions"
part: 3
stage: "I07"
status: "complete"
prerequisites: ["I07-13", "I06-13"]
estimated_time: "90–120 minutes"
---

# I07-14. Off-manifold interventions

## Why this lesson matters

Setting a single neuron to 0 or mixing coordinates from different prompts can create an internal state that never occurred during training. The downstream model may produce arbitrary outputs on such a state. Even when a large intervention effect is found, first check how far the intervention state departs from the original activation distribution.

## Learning objectives

- Give operational definitions of an activation manifold and an off-manifold state.
- Compute manifold distance in a small example.
- Explain the tradeoffs of resampling, projection, and subspace interventions.
- Report intervention effects and intervention validity in separate tables.

## Prerequisite check

- Prerequisite lessons: [I07-13 Mediation and counterfactuals](I07-13-mediation-counterfactual.md), [I06-13 Feature stability and identifiability](../I06/I06-13-feature-stability-identifiability.md)
- Check question: Why can mixing some activation coordinates from two runs break the original covariance structure?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\mathcal M$ | `calligraphic M` | Set or approximate manifold containing observed activations | subset of $\mathbb R^d$ |
| $\tilde h$ | `h tilde` | Activation produced by an intervention | $\mathbb R^d$ |
| $d(\tilde h,\mathcal M)$ | `the distance from h tilde to calligraphic M` | Manifold distance of the intervention state | nonnegative scalar |
| on-manifold | `on manifold` | State compatible with the reference activation structure | validity label |
| off-manifold | `off manifold` | State outside the reference distribution | validity warning |

## 1. A simple counterexample

If observed activations always have the form $h=(z,z)$, the manifold is the line

$$
\mathcal M=\{(z,z):z\in\mathbb R\}
$$

The key is not which values each coordinate can take individually, but which relationship the two values satisfy in the same run. Both $(1,1)$ and $(-1,-1)$ lie on this line. Mixing the first coordinate from the first run with the second coordinate from the second run gives $(1,-1)$, which breaks the original relationship.

Compute distance to the line by finding the nearest point on it. For $(h_1,h_2)$, the nearest point $(z,z)$ has coordinates equal to the average $z=(h_1+h_2)/2$. Subtracting that point from the original point gives residual coordinates of $(h_1-h_2)/2$ and its negative. The Euclidean norm of the residual is therefore

$$
d((h_1,h_2),\mathcal M)=\frac{|h_1-h_2|}{\sqrt2}
$$

so the distance for $(1,-1)$ is $\sqrt2$.

Here, $\mathcal M$ is a geometric set expressing a coordinate relationship. It does not mean that every $z$ occurs equally often in actual activations. Even on the line, some values may almost never be produced by reference inputs, so zero distance must be distinguished from being common in the reference distribution. In an actual model, the entire activation set is unknown, and this relationship is estimated from observed samples or an approximation to them.

The following coordinate plots show where coordinate mixing breaks the line relationship and the residual to the nearest point.

<figure class="lesson-figure" markdown="1">

![Line h1 equals h2 contains clean one one and valid minus one minus one but mixing first coordinate one and second minus one places the mixed state off the line](../../figures/assets/I07/I07-14-coordinate-mixing.svg)

<figcaption>The clean state (1,1) and valid state (−1,−1) from the text lie on the line h₁ = h₂. The red point (1,−1) is a counterexample: each coordinate is an actual source value, yet their combination fails to satisfy the relationship. The dashed line compares a change to only the second coordinate while keeping the first fixed.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Mixed point one minus one has closest point zero zero on diagonal h1 equals h2 with perpendicular residual length square root two](../../figures/assets/I07/I07-14-perpendicular-distance.svg)

<figcaption>The coordinates of (1,−1) average to 0, so its nearest point on the line is (0,0). The orange dashed line marks the residual (1,−1), whose length is √2. This is the orthogonal projection obtained by replacing both coordinates of the original point with their common average.</figcaption>

</figure>

## 2. Validity diagnostics

- Nearest-neighbor distance to reference activations
- PCA residual or covariance-based Mahalanobis distance
- Decoder reconstruction error
- Density-model score
- Downstream norm and normalization statistics
- Comparison with an actual source activation carrying the same meaning

Each metric measures a different mismatch. Nearest-neighbor distance asks whether a nearby state exists among the observed samples. Where reference samples are sparse, even a genuinely possible state can receive a large distance. A PCA residual measures the component outside the leading subspace. A state that travels too far within the subspace may be rare in the reference distribution even if its residual is small. Covariance-based distance reflects coordinate variances and relationships of co-occurrence, but covariance alone cannot represent an entire nonlinear relationship.

A small decoder reconstruction error means that the decoder reconstructs the state well. It does not guarantee that an actual input produces that state. Similarly, a downstream norm within the normal range does not establish that the combination of information is normal. Fix the reference inputs and locations used to construct the metric, and distinguish the relationships it checks from those it cannot check.

The next figure shows that geometric distance to the line and distance to observed reference samples answer different questions.

<figure class="lesson-figure" markdown="1">

![Illustrative reference samples occupy diagonal z between minus zero point five and zero point five while point minus three minus three stays on the line yet is two point five square root two from the nearest sample](../../figures/assets/I07/I07-14-on-line-but-rare.svg)

<figcaption>The illustrative reference samples are points on the line with z ∈ [−0.5,0.5]. The existing exercise's point (−3,−3) has zero distance to the line, but its distance to the nearest reference point (−0.5,−0.5) is 2.5√2. Satisfying the geometric relationship is different from being common in this reference distribution.</figcaption>

</figure>

## 3. Mitigation methods

- Resample activations obtained from other actual inputs.
- Move within a feature subspace and conditionally restore the remaining components.
- Use a reconstructed value obtained through a decoder.
- Conduct sensitivity analysis with multiple baselines and patch granularities.

Resampling a whole source activation brings along relationships among the source's internal coordinates. Other states in the receiving base run remain unchanged, however, so contextual mismatch between the two runs remains. A subspace intervention restricts the components being changed but does not automatically preserve their dependencies with the remaining components.

If projection or reconstruction changes the original intervention value, the reason for the changed output effect must also be distinguished. In the example above, orthogonally projecting $(1,-1)$ onto the line gives $(0,0)$. The distance has decreased, but both coordinates have changed, so this is not the same intervention as the original experiment that replaced only the first coordinate. Conditional restoration may also refill components associated with the information intended for removal. Report not just effects and distance metrics, but also which values were actually replaced before and after the correction.

The following figures show the coordinate changes before and after projection and the base context that remains even when a whole source activation is received.

<figure class="lesson-figure" markdown="1">

![Projection moves mixed state one minus one to zero zero changing both coordinates and CPU toy output from minus four to zero so the corrected operation is a new intervention](../../figures/assets/I07/I07-14-projection-changes-patch.svg)

<figcaption>Projecting the original patch (1,−1) to (0,0) changes both coordinates. The output of the existing CPU function Y = h₁ + h₂ + 4h₁h₂ also changes from −4 to 0. Reduced distance and changed effects can be checked, but this is not the same experiment as the original intervention that replaced only the first coordinate.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Source prompt A caches full activation one one; base prompt B originally has minus one minus one; patched execution copies both source coordinates but keeps prompt B context untested](../../figures/assets/I07/I07-14-whole-source-base-context.svg)

<figcaption>Copy the whole h = (1,1) from source A into h = (−1,−1) in base B. This brings along the coordinate relationships inside the source vector, but the rest of prompt B's context remains unchanged. Reducing coordinate-combination problems and verifying compatibility with the base context are separate tasks.</figcaption>

</figure>

## 4. CPU exercise

<!-- I07_EXAMPLE: i07_14_off_manifold -->

Compare clean and valid counterfactual states on a synthetic manifold with a coordinate-mixing patch. Even if an off-manifold patch produces a very different downstream output, do not conclude that it is a meaningful counterfactual.

The next figure places the existing CPU example's outputs and manifold distances on separate axes.

<figure class="lesson-figure" markdown="1">

![CPU toy outcomes clean six valid two and coordinate-mixed minus four plot against manifold distances zero zero and square root two respectively](../../figures/assets/I07/I07-14-effect-and-validity.svg)

<figcaption>In the existing CPU function, the clean state (1,1) gives an output of 6, the valid state (−1,−1) gives 2, and the coordinate-mixed state (1,−1) gives −4. The first two points have zero distance to the line; only the mixed point has distance √2. Even a large output change of −10 relative to the clean state does not automatically establish the mixed point's counterfactual validity.</figcaption>

</figure>

## Common misconceptions

### Misconception 1. A large effect is strong causal evidence

It may be an abnormal response to an out-of-distribution state. Effect size and intervention validity are separate axes.

### Misconception 2. Coordinates taken from actual activations make the state on-manifold

If the coordinates come from different sources, their combination may be a state that has never been observed.

## Exercises

### 1. Compute distance

Find the distance from $h=(2,0)$ to $\mathcal M=\{(z,z)\}$.

<details>
<summary>Show solution</summary>

It is $|2-0|/\sqrt2=\sqrt2$.

</details>

### 2. Determine whether a point is on-manifold

Is $(-3,-3)$ on the manifold above?

<details>
<summary>Show solution</summary>

It can be written with $z=-3$, so it lies on the manifold and has distance 0.

</details>

### 3. Coordinate patch

Explain why combining the first coordinate from run A with the second coordinate from run B is risky.

<details>
<summary>Show solution</summary>

Even when each coordinate is an actual value, their combination can break the learned covariance and feature relationships.

</details>

### 4. Choose a diagnostic

Which off-manifold diagnostic can be used with a linear-subspace approximation?

<details>
<summary>Show solution</summary>

Use the norm of the residual after orthogonal projection onto the leading PCA subspace. Also state its limitations for nonlinear manifolds.

</details>

### 5. Resampling

What problem is reduced by patching an entire actual source activation, and what problems remain?

<details>
<summary>Show solution</summary>

It reduces unrealistic coordinate combinations. Contextual mismatch between source and base, and hybrid-state problems with downstream states, remain.

</details>

### 6. Reporting

A large effect and a large manifold distance occur together. How should the conclusion be limited?

<details>
<summary>Show solution</summary>

Report that the intervention changed the output substantially but was far from the reference activation distribution, making it difficult to interpret as evidence for a mechanism. Revalidate with a more realistic patch.

</details>

## Sources and boundaries for updates

Empirical evidence that activation-patching choices change localization follows [Zhang and Nanda (2023)](https://arxiv.org/abs/2309.16042). Conditions for aligned interventions in causal abstraction follow [Geiger et al. (2021)](https://arxiv.org/abs/2106.02997). Do not use a single manifold diagnostic as a universal proof of validity.

## Lesson summary

- Coordinate-wise interventions can break observed activation relationships.
- A large output effect and on-manifold validity are different evaluation axes.
- Consider multiple diagnostics, including distance, reconstruction, and resampling.
- Even an actual source activation can be incompatible with the base context.

## Pass criteria

- Can you compute a simple manifold distance?
- Can you construct an off-manifold counterexample?
- Can you report effects separately from validity?

## Next lesson

- [I07-15 Controls and statistical validation](I07-15-controls-statistical-validation.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Effect size and intervention validity are separated.
- [x] The limitations of multiple manifold diagnostics are included.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is implicitly required.
- [x] Internal links and equation rendering have been checked.
