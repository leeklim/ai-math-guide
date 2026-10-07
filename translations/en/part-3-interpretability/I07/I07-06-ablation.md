---
id: "I07-06"
title: "Ablation"
part: 3
stage: "I07"
status: "complete"
prerequisites: ["I07-05"]
estimated_time: "90–120 minutes"
---

# I07-06. Ablation

## Why this lesson matters

Ablation removes the output of a neuron, attention head, or component, or replaces it with a reference value, then measures behavioral changes. Implementation is simple, but zeroing, mean replacement, and resampling are different interventions. With redundant paths, removing an individual component can have little effect, so “small effect” must also be distinguished from “not used.”

## Learning objectives

- Calculate single and joint ablation effects.
- Distinguish zero, mean, and resample ablation.
- Explain why redundancy and compensation complicate judgments of necessity.
- Design random-component and magnitude-matched controls.

## Prerequisite check

- Prerequisite lesson: [I07-05 Observation and intervention](I07-05-observation-intervention.md)
- Check question: Why must both the source value and base run be recorded in an experiment changing an internal node's value?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $Y$ | `Y` | Intact outcome | scalar metric |
| $Y_{-c}$ | `Y with component c ablated` | Outcome with component $c$ removed | scalar metric |
| $\Delta_c=Y-Y_{-c}$ | `delta sub c equals Y minus Y sub minus c` | Ablation effect | scalar |
| joint ablation | `joint ablation` | Removing several components together | intervention set |
| redundancy | `redundancy` | Other components can provide the same function | circuit property |

## 1. What is removed?

Replacing a component output $h_c$ with baseline $b_c$ gives

$$
\Delta_c(x;b_c)=Y(x)-Y\bigl(x;do(h_c=b_c)\bigr).
$$

Zero ablation uses $b_c=0$, mean ablation uses a reference-data mean, and resample ablation uses a value from another run. Because of LayerNorm or the residual stream, 0 need not mean “absent.”

If $h_c$ is an update added to the residual, the original sum $r+h_c$ becomes $r+b_c$. Zero ablation removes only that update, leaving the existing stream $r$ intact. This differs from setting the entire residual after addition to 0. Downstream LayerNorm recalculates the mean and variance of the modified sum, so replacing one update can also change values in multiple later coordinates.

The next two figures show the retained residual path and the recomputation of downstream normalization separately.

<figure class="lesson-figure" markdown="1">

![Residual stream feeds a component whose output is overwritten by zero while an intact skip path feeds the residual sum so the sum is r before downstream LayerNorm is recomputed](../../figures/assets/I07/I07-06-zero-update-skip.svg)

<figcaption>Only the component output h_c is overwritten with 0. The blue skip path retains r, which enters the sum to give r + 0 = r. LayerNorm recalculates its statistics from this modified sum. This differs from setting the entire residual sum to 0.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Illustrative three-coordinate residual changes from two zero minus one to one zero minus one when one update coordinate is zeroed but standardization changes all three normalized coordinates](../../figures/assets/I07/I07-06-layernorm-propagation.svg)

<figcaption>This illustration uses r = (1, 0, −1) and h_c = (1, 0, 0). Removing the update changes only the sum's first coordinate, but normalization with a recalculated mean and standard deviation changes all three coordinates. The displayed calculation has positive variance, ε = 0, and no affine terms.</figcaption>

</figure>

## 2. Necessity and redundancy

A large individual ablation effect provides evidence that the component is necessary under those conditions. A small effect can have any of the following explanations.

- The component is barely involved in the original behavior.
- Another component provides a redundant function.
- The metric fails to capture its role.
- Downstream computation compensates for the ablation value.

Examine joint ablation and restoration experiments together.

Judge necessity against a behavioral criterion specified first. If the logit decreases but the correct choice remains unchanged, there is an effect on the score, but not evidence that the correct answer could not be produced without the component. Even when behavior survives a single removal, the outcome of removing a set can differ. In the exercise's $Y=\max(h_1,h_2)$ with both values equal to 1, replacing one with 0 leaves the other at 1, while replacing both with 0 gives $Y=0$.

Ablation in a fixed model does not retrain the weights. Downstream compensation here is the response of the existing computation to changed activations. Performance recovery obtained by retraining after component removal is a different training experiment.

The next two comparisons separate joint removal of redundant paths from the boundary defined by the behavioral criterion.

<figure class="lesson-figure" markdown="1">

![Diamond state graph for max of two components has intact one one output one and both single-zero states zero one and one zero output one while the joint zero zero state outputs zero](../../figures/assets/I07/I07-06-redundant-max-paths.svg)

<figcaption>This is the max example in the text. A path with value 1 remains after either single removal, but removing both gives an outcome of 0. Individual effects of 0 do not mean that the two components lack a function.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Illustrative score-margin bars two zero point two and minus zero point one show a large reduction with the positive decision retained followed by crossing zero and losing the decision](../../figures/assets/I07/I07-06-margin-versus-decision.svg)

<figcaption>The illustrative margins are 2, 0.2, −0.1, with a positive margin selecting the correct answer. The large score decrease 2→0.2 retains the choice, whereas 0.2→−0.1 crosses the boundary at 0 and changes the choice.</figcaption>

</figure>

## 3. Controls

- Ablate random components in the same layer.
- Use components with similar activation norms or output variances.
- Use randomly selected sets with the same number of nodes.
- Use a behavioral metric with shuffled input labels.
- Examine paired effects across multiple seeds and prompts.

Looking only at selected components while omitting the random-selection distribution introduces selection bias.

For magnitude matching, state which magnitude was matched. The norm of the original output $h_c$ can differ from the norm of the actual change $h_c-b_c$ in mean or resample ablation. Comparing actual change magnitudes in controls with the same replacement rule and component count helps distinguish the effect of target selection from the effect of a larger manipulation.

The coordinate plots below show how equal original activation magnitudes can still produce different manipulation magnitudes.

<figure class="lesson-figure" markdown="1">

![Three one-dimensional coordinate diagrams hold original activation three fixed while replacing it by zero two or minus three produces manipulation distances three one and six despite the same original norm three](../../figures/assets/I07/I07-06-change-norm-baselines.svg)

<figcaption>The illustrative original coordinate h = 3 always has norm 3. Replacements with b = 0, 2, −3 give different actual changes |h − b| of 3, 1, 6. Distinguish which norm was matched in the controls.</figcaption>

</figure>

## 4. CPU lab

<!-- I07_EXAMPLE: i07_06_ablation -->

Calculate the mean single effects of three components and the effect of removing the first two together. This synthetic example uses a linear sum, so the sum of the first two individual effects equals the joint effect. This is not guaranteed with nonlinear downstream computation.

The following bars compare the lab's single and joint ablation effects on the same three inputs.

<figure class="lesson-figure" markdown="1">

![Lab component mean effects zero point nine and fourteen fifteenths have a sum eleven sixths equal to the mean joint effect of ablating the first two under the stated linear downstream function](../../figures/assets/I07/I07-06-linear-lab-additivity.svg)

<figcaption>The lab uses Y = h₁ + h₂ + 0.2h₃ and three inputs. The first two mean single effects, 0.9 and approximately 0.9333, sum to approximately 1.8333, equal to the joint effect with the same baseline. This equality is restricted to the lab's linear downstream computation.</figcaption>

</figure>

## Common misconceptions

### Misconception 1. Zero ablation cleanly deletes a component

The model may never have encountered a state of 0 during training, and it can change normalization statistics.

### Misconception 2. A component with a small effect is outside the circuit

Redundant and compensating paths can hide individual necessity.

## Exercises

### 1. Single ablation

For $Y=h_1+2h_2$ and $(h_1,h_2)=(3,1)$, calculate the zero-ablation effect for $h_1$.

<details>
<summary>Show solution</summary>

The intact outcome is $Y=5$ and the ablated outcome is $Y=2$, so the effect is 3.

</details>

### 2. Mean ablation

In the same example, what is the effect of replacing $h_1$ with its mean value of 2?

<details>
<summary>Show solution</summary>

The replacement outcome is 4, so the effect is 1. This is a different estimand from zero ablation.

</details>

### 3. Redundancy

For $Y=\max(h_1,h_2)$ with both values equal to 1, calculate the outcomes of each single ablation and the joint ablation.

<details>
<summary>Show solution</summary>

Replacing only one with 0 leaves the other at 1, preserving the outcome. Replacing both with 0 gives an outcome of 0. An individual effect of 0 does not imply an absence of function.

</details>

### 4. Choosing controls

A head with a large norm was ablated. What control is needed?

<details>
<summary>Show solution</summary>

Ablate heads in the same layer with similar output norms or variances to distinguish a simple magnitude effect from the specificity of the selected head.

</details>

### 5. Choosing metrics

Explain a disadvantage of using accuracy alone as the ablation outcome.

<details>
<summary>Show solution</summary>

When the correct class remains unchanged, accuracy hides a large logit-margin change. Conversely, a small margin change crossing the threshold can change accuracy discontinuously. Examine a predefined continuous metric as well.

</details>

### 6. Writing a claim

Write a justified conclusion when only joint ablation disrupts the behavior.

<details>
<summary>Show solution</summary>

State that the specified component set showed set-level evidence of necessity under the intervention and metric. Do not claim that each component is individually necessary.

</details>

## Sources and update boundaries

[Wang et al. (2022)](https://arxiv.org/abs/2211.00593) provide examples of node removal and restoration evaluation in Transformer circuits. This lesson does not treat one type of ablation as a universal deletion operation.

## Lesson summary

- An ablation effect is the outcome difference between the intact run and an explicitly specified replacement intervention.
- Zero, mean, and resample ablation measure different questions.
- Small individual effects do not rule out redundancy and compensation.
- Joint ablation, restoration, and matched controls are needed.

## Pass criteria

- Can you calculate single and joint ablation effects?
- Can you explain the differences among the three baselines?
- Can you design a redundancy counterexample and controls?

## Next lesson

- [I07-07 Activation patching](I07-07-activation-patching.md)

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] Ablation baselines and redundancy are distinguished.
- [x] Joint interventions and controls are included.
- [x] Every exercise has a solution.
- [x] The strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and mathematical rendering have been checked.
