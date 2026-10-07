---
id: "I07-10"
title: "Residual and logit attribution"
part: 3
stage: "I07"
status: "complete"
prerequisites: ["I07-09", "N05-17"]
estimated_time: "90–120 minutes"
---

# I07-10. Residual and logit attribution

## Why this lesson matters

A Transformer's residual stream can be written as the sum of embeddings, attention updates, and MLP updates. At a point where the final logit readout is linear, inner products decompose the direct logit contributions of the residual components. This is a fast accounting tool, but it does not measure downstream nonlinear interactions or a component's necessity.

## Learning objectives

- Calculate the inner product of a residual component and a logit direction.
- Check that contributions sum to the full logit at a linear readout.
- Explain where LayerNorm or RMSNorm breaks an exact additive decomposition.
- Distinguish direct attribution from a causal effect.

## Prerequisite check

- Prerequisite lessons: [I07-09 Path patching](I07-09-path-patching.md), [N05-17 Residual stream](../../part-2-neural-computation/N05/N05-17-residual-stream.md)
- Check question: When residual updates accumulate by addition, how can the final residual vector be written as a sum of components?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $r=\sum_c r_c$ | `r equals the sum over c of r sub c` | Sum of residual components | $r,r_c\in\mathbb R^d$ |
| $u_y$ | `u sub y` | Unembedding direction for token $y$ | $\mathbb R^d$ |
| $a_{c,y}=u_y^\top r_c$ | `a sub c y equals u sub y transpose r sub c` | A component's direct logit contribution | scalar |
| logit difference | `logit difference` | Target logit minus foil logit | scalar |
| direct logit attribution | `direct logit attribution` | Linear contribution at a chosen readout | decomposition |

## 1. Linear readout

Applying unembedding to the post-normalization vector $z$ gives the logit for token $y$:

$$
\ell_y=u_y^\top z+b_y
$$

If $z$ is a component sum $\sum_c z_c$, then

$$
\ell_y-b_y=\sum_c u_y^\top z_c.
$$

$u_y$ and $z_c$ are vectors of the same length, and their inner product is a scalar. The inner product distributes over a vector sum, giving $u_y^\top\sum_c z_c=\sum_c u_y^\top z_c$. The bias is added once, outside the sum of component contributions. Attaching the same bias to every component would count it repeatedly in the full logit. The $z_c$ in this equality must be components that actually sum to the readout input $z$.

The logit difference between target $y$ and foil $q$ can be analyzed along a single direction, $u_y-u_q$.

Subtracting the two logit equations gives $\ell_y-\ell_q=(u_y-u_q)^\top z+(b_y-b_q)$. Thus, the component inner products decompose the contrast excluding the bias difference. Their sum alone gives the full logit difference only when there is no unembedding bias or the two biases are equal.

The following figures show inner-product additivity and the target-minus-foil direction at the same readout.

<figure class="lesson-figure" markdown="1">

![Coordinate arrows for residual parts one zero and zero two sum to one two and share the same readout direction three four with contributions three eight and eleven](../../figures/assets/I07/I07-10-readout-inner-products.svg)

<figcaption>The exercise's r₁ = (1,0), r₂ = (0,2), and u = (3,4) share one coordinate system. Contributions 3 and 8 sum to 11, the readout of the summed vector. If there is a bias, add it once, not once per component.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Target vector two one and foil vector one minus one have difference one two shown at the origin and translated between their tips](../../figures/assets/I07/I07-10-target-minus-foil.svg)

<figcaption>These are the exercise's u_y = (2,1) and u_q = (1,−1). The dashed arrow shows the difference between their tips; the purple vector at the origin is the same difference (1,2). An inner product along this direction calculates the target-minus-foil logit excluding the bias difference.</figcaption>

</figure>

## 2. The normalization boundary

If LayerNorm or RMSNorm maps the final residual $r$ to $z=N(r)$, generally

$$
N\left(\sum_c r_c\right)\ne\sum_c N(r_c).
$$

Normalizing each raw component independently and adding them is not the actual forward pass. If you use a fixed local linearization or a particular decomposition convention, specify its approximation and conditions.

For example, with $N(r)=r/\lVert r\rVert$, $r_1=(1,0)$, and $r_2=(0,2)$, normalizing the actual sum gives $(1,2)/\sqrt5$, whereas adding the independently normalized components gives $(1,1)$. However, fixing this run's total norm $\sqrt5$ and dividing both components by that shared denominator yields a sum equal to the actual $N(r)$. Additive accounting is therefore possible for this run. Removing a component changes the total norm in the new run, so do not use the same fixed-denominator decomposition directly to predict an intervention.

The coordinate diagrams below compare normalizing the total with normalizing the components, then separately show the shared-denominator case.

<figure class="lesson-figure" markdown="1">

![Normalizing raw sum one two gives one two divided by square root five on the unit circle while normalizing parts independently gives one one outside it](../../figures/assets/I07/I07-10-normalize-sum-or-parts.svg)

<figcaption>This is the example N(r) = r/‖r‖ from the text. Normalizing the sum gives (1,2)/√5 on the unit circle, while the sum of independently normalized components, (1,1), lies outside it. Different denominators produce different vectors.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Scaled component one zero divided by square root five plus translated zero two divided by that same square root five gives the normalized total one two divided by square root five](../../figures/assets/I07/I07-10-shared-scale-accounting.svg)

<figcaption>Fixing the same run's total norm √5 for both components lets the blue and purple components sum exactly to the green normalized vector. Because removal can change the total norm, this fixed-denominator accounting alone does not predict the intervention outcome.</figcaption>

</figure>

## 3. Direct and total effects

Direct logit attribution measures how a component vector aligns with the current readout direction. Removing that component recomputes downstream attention, MLPs, and normalization, so it is not the same as an ablation effect. A large direct contribution is not intervention evidence.

In a linear example that adds fixed vectors without downstream computation, the difference from zero-ablating a component equals its inner-product contribution. But when an intermediate component is removed, the other components measured in the original run cannot be assumed to stay unchanged. Direct contribution decomposes the original run's values; total effect compares that run with the one recomputed after the intervention.

The following figure compares the recomputed norm after removal with the fixed-denominator contribution in the original run.

<figure class="lesson-figure" markdown="1">

![For unit normalization and readout three four the fixed scale contribution of residual zero two is three point five seven eight but recomputing norm after removing it drops the logit only one point nine one nine](../../figures/assets/I07/I07-10-direct-versus-recomputed-removal.svg)

<figcaption>This combines the normalization example with the exercise's u = (3,4). The original logit is 11/√5 ≈ 4.919; after removing r₂, it is 3. The actual decrease of about 1.919 differs from r₂'s contribution 8/√5 ≈ 3.578 calculated with the original fixed denominator.</figcaption>

</figure>

## 4. CPU exercise

<!-- I07_EXAMPLE: i07_10_residual_logit_attribution -->

Check whether the inner products of three residual components sum to the logit of the full residual. The output explicitly states that the code includes no final nonlinearity.

The following accumulation diagram traces how the existing CPU exercise's three contributions form the full logit.

<figure class="lesson-figure" markdown="1">

![Existing CPU component contributions embedding plus zero point five attention plus three point five and MLP minus one point five form a waterfall ending at logit two point five without final normalization](../../figures/assets/I07/I07-10-cpu-contribution-waterfall.svg)

<figcaption>For the CPU exercise's u = (1,2,−1), the embedding, attention, and MLP inner products are 0.5, 3.5, and −1.5. Their upward and downward increments produce the logit 2.5 for the full residual (1.5,1,1). This is not an effect that includes final normalization or subsequent nonlinear computation.</figcaption>

</figure>

## Common misconceptions

### Misconception 1. A head with a large direct contribution is necessary

Other components may cancel or replace it, and removing the head changes downstream computation as well.

### Misconception 2. Projecting every layer's residual components directly onto the final logit is exact

Intermediate components pass through later layers and final normalization. Direct projection is a diagnostic under a specified convention.

## Exercises

### 1. Inner product

Find the direct contribution for $r_c=(1,2)$ and $u_y=(3,-1)$.

<details>
<summary>Show solution</summary>

It is $3\cdot1+(-1)\cdot2=1$.

</details>

### 2. Check the sum

For $r_1=(1,0)$, $r_2=(0,2)$, and $u=(3,4)$, find the component contributions and full logit.

<details>
<summary>Show solution</summary>

The contributions are 3 and 8, summing to 11. The inner product of the full residual $(1,2)$ with $u$ is also 11.

</details>

### 3. Logit difference

For target direction $u_y=(2,1)$ and foil direction $u_q=(1,-1)$, what is the difference direction?

<details>
<summary>Show solution</summary>

It is $u_y-u_q=(1,2)$. Its inner product with the residual gives the logit-difference contribution excluding bias.

</details>

### 4. Normalization

For $N(r)=r/\|r\|$, explain why $N(r_1+r_2)=N(r_1)+N(r_2)$ generally does not hold.

<details>
<summary>Show solution</summary>

The left denominator is the norm of the summed vector; the right side uses each vector's own norm. Normalization is not a linear operation.

</details>

### 5. Causal claim

An MLP has a large positive direct contribution to the target logit. What should be checked next?

<details>
<summary>Show solution</summary>

Ablate that MLP's output or apply a matched activation patch, then measure changes in the same logit difference and behavioral metric in paired comparisons.

</details>

### 6. Negative contribution

Why should a negative direct contribution not be labeled a “harmful component”?

<details>
<summary>Show solution</summary>

It only lowers the selected token contrast. The component may have roles needed for other tokens, calibration, or downstream computation. Assessing its overall function is a separate question.

</details>

## Evidence and update boundaries

Use [Elhage et al. (2021)](https://transformer-circuits.pub/2021/framework/index.html) for the framework that treats the residual stream as a communication channel and projects components onto readout directions. Always record both the computation site where the linear decomposition is exact and the normalization convention.

## Lesson summary

- At a linear readout, residual components' inner products additively decompose the logit.
- A logit difference uses the target-minus-foil direction.
- Normalization complicates a simple additive projection of raw residual components.
- Direct attribution and ablation or patching effects are different values.

## Pass criteria

- Can you calculate component logit contributions?
- Can you identify where additivity holds?
- Can you distinguish a direct contribution from a causal effect?

## Next lesson

- [I07-11 Representing a circuit as a graph](I07-11-circuit-graph.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] The linear readout and normalization boundary are distinguished.
- [x] Direct and causal effects are separated.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is implicitly required.
- [x] Internal links and math rendering have been checked.
