---
id: "A09-CAU-06"
title: "Causal abstraction"
part: 4
stage: "A09-CAU"
status: "complete"
prerequisites: ["M03-02", "I07-11", "A09-CAU-02"]
estimated_time: "90–120 minutes"
---

# A09-CAU-06. Causal abstraction

## Why this lesson matters

A mechanistic interpretation claims that low-level neuron and activation computations implement a high-level algorithm expressed through variables and rules. Matching observational predictions alone does not establish this implementation relation. A causal abstraction claim requires corresponding interventions to produce the same results at both levels.

## Learning objectives

- Define an abstraction map connecting low-level and high-level states.
- Express the correspondence between low-level and high-level interventions.
- Explain the intervention commuting condition.
- Design approximate abstraction errors and held-out interventions.

## Prerequisite check

- Prerequisite lessons: [M03-02 Linear maps and matrix representations](../../part-1-foundations/M03/M03-02-linear-maps-matrix-representation.md), [I07-11 Representing circuits as graphs](../../part-3-interpretability/I07/I07-11-circuit-graph.md), [A09-CAU-02 The do operator and interventions](A09-CAU-02-do-operator-interventions.md)
- Check question: Why is a one-to-one correspondence between a high-level variable and a single low-level neuron unnecessary?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $\tau:\mathcal L\to\mathcal H$ | `tau maps the low-level state space L to the high-level state space H` | Map summarizing a low-level state as a high-level state | Function |
| $i_L$ | `i sub L` | Low-level intervention and subsequent recomputation | Operation |
| $i_H$ | `i sub H` | High-level intervention and subsequent recomputation | Operation |
| $\epsilon_{\mathrm{abs}}$ | `epsilon sub abs` | Output discrepancy between the two intervention paths | Nonnegative scalar |

## Core concepts

### A state-summary map and computation rules

Map a low-level model state $l\in\mathcal L$ to a high-level state $h=\tau(l)\in\mathcal H$. The state $l$ can contain many activation values, while $h$ contains a few interpretable variables such as subject number. The map $\tau$ groups several numerical states into the same abstract state rather than renaming neurons. It therefore requires neither a one-to-one correspondence nor an inverse.

However, specifying a state space and decoder does not complete a high-level *causal model*. Rules computing downstream outputs from abstract variables must also be specified. A probe that accurately decodes `plural` provides evidence that this information can be read from activations. Whether changing the information also changes verb predictions according to the high-level rule is a separate question.

The following coordinate plane shows a decoder grouping several states under one label.

<figure class="lesson-figure" markdown="1">

![A sign decoder partitions a two-dimensional low-level state plane into many states with abstract label plus one and many with minus one, with a zero-score boundary.](../../figures/assets/A09-CAU/A09-CAU-06-many-states-one-label.svg)

<figcaption>The illustrative τ(l)=sign(l₁) maps many different low-level states to the same +1 or −1 label. The gray l₁=0 boundary must be excluded or handled by a separate tie rule. This partition summarizes the decoder; it does not define downstream computation rules.</figcaption>

</figure>

### Intervention pairs and two paths

For every high-level intervention $i_H$, specify a corresponding low-level intervention $i_L$. This correspondence is a prespecified operation rule stating which component receives which value, not a label assigned after observing outputs. A coordinated intervention can be used if one abstract variable is distributed across multiple heads. If the same coordinates also represent another variable, check how well that variable is preserved.

Here, we compare deterministic executions with inputs and random draws fixed. In the formulas, $i_L(l)$ and $i_H(h)$ include not only the instant of overwriting values but also **the results after recomputing downstream according to each model's rules**. Both paths must start from $l$ and $h=\tau(l)$ corresponding to the same input and background to interpret their difference as a difference in intervention correspondence.

The following numerical operation tracks both changed and retained parts across components.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three illustrative two-coordinate head states change their first coordinate from one to minus one while second coordinates two, three, and four stay fixed, feeding one coordinated low-level intervention.](../../figures/assets/A09-CAU/A09-CAU-06-coordinated-components.svg)

<figcaption>In the illustrative heads H₁=(1,2), H₂=(1,3), H₃=(1,4), the first coordinates change together from 1→−1 while second coordinates 2,3,4 remain fixed. This joint i_L can correspond to one i_H, but preservation of other variables in shared coordinates must be checked separately. The numerical operation alone does not establish causal abstraction.</figcaption>

</figure>

### What the commuting condition compares

Exact causal abstraction requires the two paths to produce the same abstract outcome over all specified allowed states and intervention pairs.

$$
\tau\bigl(i_L(l)\bigr)
=i_H\bigl(\tau(l)\bigr)
$$

On the left, perform the low-level operation and recomputation first, then summarize with $\tau$. On the right, summarize the original state, then perform the high-level operation and recomputation. Commuting means **reaching the same abstract result despite computing at different levels**. If downstream output is part of the comparison, matching only an intermediate label does not satisfy the equality. Also specify how outputs at the two levels are mapped into the same value space.

For example, suppose $\tau(l_1)=\tau(l_2)$, but the summarized results differ after the corresponding low-level intervention. A single high-level state then cannot determine that intervention's result: discarded information affects the outcome of an allowed intervention. Including such states in scope requires changing the abstraction or intervention correspondence. Conversely, equality on one prompt does not prove equality over all untested states.

The next two figures show the path-matching condition and a coordinate counterexample where it fails.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A square starts at low state l and maps it to tau l; applying low intervention before abstraction is compared with high intervention after abstraction, including downstream recomputation in each route.](../../figures/assets/A09-CAU/A09-CAU-06-commuting-intervention-square.svg)

<figcaption>The upper route performs low-level intervention and recomputation first, then summarizes with τ. The route descending from the left obtains τ(l) first, then performs high-level intervention and recomputation. At the lower right, the results are compared under the same abstract outcome and output criterion. Matching only an intermediate label is insufficient.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![State A with coordinates two, one and state B with coordinates two, minus one share abstract plus one before a coordinate swap, then map to opposite labels because their discarded second coordinates differ.](../../figures/assets/A09-CAU/A09-CAU-06-discarded-coordinate-counterexample.svg)

<figcaption>For the illustrative τ(l)=sign(l₁), states A=(2,1)ᵀ and B=(2,−1)ᵀ both map to +1. Swapping the coordinates with i_L gives (1,2)ᵀ and (−1,2)ᵀ, whose τ results are +1 and −1. Because the original abstract label discards the second coordinate, one i_H result cannot explain both paths.</figcaption>

</figure>

### Approximate error and evaluation scope

For approximate abstraction, specify a distance $d_{\mathcal H}$ and measure

$$
\epsilon_{\mathrm{abs}}
=E\left[d_{\mathcal H}\left(\tau(i_L(L)),i_H(\tau(L))\right)\right]
$$

This formula fixes an intervention pair and averages over the distribution of evaluation states $L$. Evaluating multiple pairs together also requires a pair-sampling distribution. Counting categorical disagreements as 0 or 1 and measuring continuous score differences define different errors. Fix the variables and outputs being compared, distance, and weights in advance.

A small mean error means the two paths are generally close under that evaluation distribution. Rare prompts can have large errors, and unsampled interventions can fail. Even an expected nonnegative distance of exactly 0 does not guarantee success on states assigned weight 0 by the distribution.

The map $\tau$ can be a probe, sparse feature, subspace projection, or discrete decoder. Choosing the map and intervention direction using success rates on the same prompts reported as final results includes the effect of selecting a well-fitting combination. Learn the map on training data, select the correspondence rule on validation data, then freeze those choices and check held-out prompts and interventions. This provides generalization evidence within the specified evaluation scope, not a proof of exact abstraction over the full scope.

The following figures distinguish the mean, evaluation support, and held-out objects.

<figure class="lesson-figure" markdown="1">

![One hundred illustrative equally weighted states have distance zero in ninety-nine and distance ten in one, giving mean error 0.1 despite a large rare failure.](../../figures/assets/A09-CAU/A09-CAU-06-rare-error-large-distance.svg)

<figcaption>Assign weight 0.01 to each of 100 illustrative states, with distance 0 for 99 and distance 10 for the last. Then ε_abs is 0.1. A small mean does not mean a small distance at every state; these are not model error measurements.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An illustrative evaluation density is positive only on states from zero to one, where distance is zero; outside that support distance may be one without changing expected error zero.](../../figures/assets/A09-CAU/A09-CAU-06-zero-weight-outside-scope.svg)

<figcaption>The illustrative evaluation distribution assigns weight only to states s∈[0,1], where distance is 0. Distance 1 outside that range does not change expectation 0 when those states have weight 0. Zero expected nonnegative distance means almost-sure success under the evaluation distribution, not automatic proof of success at every allowed state.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Training fits tau, validation selects intervention correspondence, then both are frozen before evaluating a two-by-two grid of seen or held-out prompts and operations.](../../figures/assets/A09-CAU/A09-CAU-06-prompt-operation-heldout-grid.svg)

<figcaption>The top shows learning τ on training data, selecting intervention correspondence on validation data, then freezing both. The bottom axes are separate evaluation dimensions: new prompts and new operations. The lower right holds out both together. Success here supports generalization under the tested distribution, not exact universality.</figcaption>

</figure>

## Small example

If the high-level variable is `subject number` and the low-level state is a residual subspace, $\tau$ extracts a singular/plural score. For a high-level flip intervention, reverse the corresponding low-level direction and check whether downstream verb-number output also changes as predicted.

Distinguish score from label. If the score is $w^\top l$ and the label is $\operatorname{sign}(w^\top l)$, a scope using just two labels must exclude states with score 0 or specify a tie-breaking rule. When $\|w\|=1$, the transformation $l'=l-2(w^\top l)w$ reverses the component along $w$ while retaining perpendicular components. Thus $w^\top l'=-w^\top l$, but this calculation alone does not guarantee reversal of downstream verb prediction.

If the high-level rule replaces `is` with `are` in its prediction after the number flip, compare the recomputed low-level result under the same criterion. If only the decoder label changes to `plural` while the verb output stays unchanged, the state operation succeeds but causal implementation of that rule has not been established.

The following coordinate figure and failure case distinguish score reversal from agreement in downstream output.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An illustrative low-level flip decodes as plural but recomputed verb stays is, while the high-level rule predicts are; decoded-label success therefore does not establish causal implementation.](../../figures/assets/A09-CAU/A09-CAU-06-decoder-versus-output-rule.svg)

<figcaption>This is the text's failure condition, not an actual experiment result. The decoder label changes to plural, but the low-level downstream verb stays is while the high-level rule requires are. Successful label manipulation and successful causal implementation of the rule compare different objects.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![In a two-dimensional illustrative state with unit direction w along the first axis, reflecting state 2,1 to minus2,1 flips the score while preserving its perpendicular coordinate one.](../../figures/assets/A09-CAU/A09-CAU-06-reflection-preserves-perpendicular.svg)

<figcaption>With w=(1,0)ᵀ satisfying ||w||=1, applying l′=l−2(wᵀl)w to l=(2,1)ᵀ gives l′=(−2,1)ᵀ. The first-coordinate score changes from 2→−2, while perpendicular component 1 remains. Even when this numerical reflection changes the decoder sign, reversal of downstream verb output requires a separate computation.</figcaption>

</figure>

## Common misconceptions

- Accurate decoding of a high-level variable does not by itself establish causal abstraction.
- Commuting in one intervention does not guarantee implementation of every high-level operation.

## Exercises

### 1. Map
If $\tau(l)=\operatorname{sign}(w^\top l)$, which two values can form the high-level state space?
<details><summary>Show solution</summary>

Use $\{-1,+1\}$ or two corresponding symbolic labels.
</details>

### 2. Commuting
After a low-level flip, the value of $\tau$ changes, but the downstream high-level output does not change as predicted. Does causal abstraction pass?
<details><summary>Show solution</summary>

No. Only state decoding changes; the intervention consequence does not match the high-level model.
</details>

### 3. Selection
Which bias arises when error is reported on the same prompts used to choose the abstraction map?
<details><summary>Show solution</summary>

Fitting the map and intervention to the data creates selection bias. Held-out prompts and operations are needed.
</details>

### 4. Model interpretation
One high-level variable is distributed across several heads. How should the low-level intervention be defined?
<details><summary>Show solution</summary>

Define a joint subspace or coordinated intervention across multiple nodes that retains or changes the variable, and compare with a dimension-matched control.
</details>

## Evidence and update boundaries

This lesson treats intervention correspondence and the commuting condition at the level of experimental design. Full definitions of category-theoretic abstraction formalisms are outside its scope.

- [Geiger et al., *Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability* (2025), §2.3–2.4](https://www.jmlr.org/papers/volume26/23-0058/23-0058.pdf): Intervention correspondence and exact/approximate transformations in deterministic models. The text's state-level formulas are simplified notation including recomputation after intervention; they do not replace the map and intervention-structure conditions required by the paper's full definition.
- [Rubenstein et al., *Causal Consistency of Structural Equation Models* (2017), §4.2–4.3](https://arxiv.org/pdf/1707.00819): In stochastic SEMs, compare post-intervention distributions after transporting them through the abstraction map. Do not replace the fixed-execution equality above with equality of mean outputs alone and call it the definition of stochastic exact abstraction.

## Lesson summary

- Causal abstraction connects low-level states to high-level variables.
- Interventions at both levels must produce corresponding results.
- Decoding accuracy and intervention consistency provide different evidence.
- Validate the abstraction map on held-out prompts and interventions.

## Pass criteria

- Can you define an abstraction map and intervention pair?
- Can you distinguish observational decoding from a causal implementation claim?

## Next lesson

- [A09-CAU-07 External validity of internal interventions](A09-CAU-07-external-validity-internal-interventions.md)

## Author checklist

- [x] Abstraction maps, intervention correspondence, and held-out validation are explained.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
