---
id: "I07-05"
title: "Observation and Intervention"
part: 3
stage: "I07"
status: "complete"
prerequisites: ["I07-04", "M04-16"]
estimated_time: "90–120 minutes"
---

# I07-05. Observation and Intervention

## Why this lesson matters

Observing an activation change together with behavior is different from concluding that setting the activation changes behavior. Inside a model, the forward pass is known, so interventions that forcibly change node values can be implemented directly. The scope of their results remains tied to the selected inputs, nodes, replacement values, and metrics.

## Learning objectives

- Distinguish conditional observation from a $do$ intervention.
- Explain what cutting incoming edges means when intervening in a computation graph.
- Define a total effect using differences between paired runs.
- Distinguish internal interventions from causal claims about the external world.

## Prerequisite check

- Prerequisite lessons: [I07-04 Perturbation attribution](I07-04-perturbation-attribution.md), [M04-16 Correlation, prediction, and causation](../../part-1-foundations/M04/M04-16-correlation-causation.md)
- Check question: Why do $P(Y\mid H=h)$ and $P(Y\mid do(H=h))$ differ?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $H$ | `H` | Internal node to be intervened on | tensor |
| $do(H=h^*)$ | `do H equals h star` | Forcibly setting $H$ to $h^*$ | intervention |
| $Y_{do(H=h^*)}$ | `Y under do H equals h star` | Output of the intervened run | outcome |
| $\tau$ | `tau` | Mean difference between two intervention outcomes | scalar estimand |
| paired run | `paired run` | Runs applying two conditions to the same input | design |

## 1. Observation preserves the paths

If both $X\to H\to Y$ and $X\to Y$ are present, samples observed with $H=h$ can also have a different distribution of $X$. By contrast, $do(H=h^*)$ overwrites the original computation producing $H$ and reruns only the downstream computation.

When selecting samples with $H=h$ in an observation, the original equation generating $H$ remains valid. For example, in the lab's $H=2X$ and $Y=H+X$, observing $H=2$ implies $X=1$ and $Y=3$. Applying $do(H=2)$ to a run with $X=2$, however, replaces only the equation $H=2X$, giving $Y=2+2=4$. Cutting the $X\to H$ computation leaves the direct path $X\to Y$ intact.

After a node intervention, downstream nodes using that node's value are recomputed with their original equations. The total effect of manipulating the node includes these subsequent changes. In the formula below, $Y$ is a scalar to compare, such as a logit or behavioral metric, while $h_i^{(1)}$ and $h_i^{(0)}$ are the two replacement values applied to the same input $i$.

$$
\tau
=
\mathbb E_i\left[
Y_i\bigl(do(H=h_i^{(1)})\bigr)
-Y_i\bigl(do(H=h_i^{(0)})\bigr)
\right].
$$

Applying both conditions to the same input $i$ allows differences in input difficulty to be removed from the paired difference.

First calculate the difference between the two outcomes for each input, then average over the specified input population. This avoids composition differences arising from using different prompt sets in the two conditions, but variation in intervention effects across inputs remains. For a fixed input and replacement value in a deterministic model, each difference is determined by computation. Sample selection enters the mean and uncertainty used to generalize to other inputs.

The next four figures show the preserved computation paths, the overwritten path, the output differences being compared, and the paired average in sequence.

<figure class="lesson-figure" markdown="1">

![Observed computation X one feeds H two by the original twice X rule and also directly feeds Y three while H feeds Y with both incoming routes intact](../../figures/assets/I07/I07-05-observed-computation.svg)

<figcaption>Observing a run with H = 2 under the original equation H = 2X gives X = 1. Both X→H→Y and X→Y remain intact, giving Y = 2 + 1 = 3.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Intervened computation keeps X two and its direct route to Y cuts the twice X edge into H overrides H with two and recomputes Y as four](../../figures/assets/I07/I07-05-intervened-computation.svg)

<figcaption>The run with X = 2 receives do(H = 2). Only the X→H computation, marked with a gray dashed line and ×, is overwritten. Recomputing the addition along the direct X→Y path and H→Y gives Y = 4.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Original Y equals three X line and fixed H two Y equals X plus two line meet at X one Y three but differ at X two with original six and intervened four](../../figures/assets/I07/I07-05-observed-versus-fixed-h.svg)

<figcaption>The original computation gives Y = 3X, while do(H = 2) gives Y = X + 2. Changing X from 1 to 2 changes the original output by +3; the H intervention with X fixed at 2 gives a difference of 4 − 6 = −2.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Illustrative paired outcome lines for X one half one and two connect intact Y one point five three six to do H two outcomes two point five three four giving differences plus one zero minus two](../../figures/assets/I07/I07-05-paired-aggregation.svg)

<figcaption>The same toy function is run under both conditions for illustrative inputs X = 0.5, 1, 2. Each line joins paired runs for the same input. First calculating intervention−intact differences (+1, 0, −2), then averaging, gives −1/3. The mean for these three inputs is not generalized to another input population.</figcaption>

</figure>

## 2. Causality inside a model

An intervention effect can be measured even in a deterministic forward pass. It is the effect of manipulating a node on the output within a fixed model computation. It does not automatically extend to causal relationships involving training data, human concepts, or real-world variables.

## 3. The intervention contract

- The node's exact module, layer, token, and coordinates
- The source value and base run
- Overwrite timing: module input, module output, or after the residual sum
- Outcome and aggregation
- The relationship among clean, corrupt, and patched inputs
- Random, matched, and resampled controls

Experiments called “activation patching” measure different estimands when these items differ.

The following residual computation shows how intervention timing changes which tensor is actually modified.

<figure class="lesson-figure" markdown="1">

![Residual computation has module F and a skip path into a sum with three red overwrite positions at module input module output and after the residual sum representing distinct tensors](../../figures/assets/I07/I07-05-hook-timing.svg)

<figcaption>Position A is the input to F, B is its output, and C is the tensor after the residual sum. Overwriting B leaves r on the skip path intact, whereas C changes the entire combined tensor. Even in the same layer, these three locations define different interventions.</figcaption>

</figure>

## 4. CPU lab

<!-- I07_EXAMPLE: i07_05_observation_intervention -->

For $H=2X$ and $Y=H+X$, compare the observed difference from changing $X$ from 1 to 2 with the intervention effect of keeping $X=2$ and replacing only $H$ with its value from the $X=1$ run.

## Common misconceptions

### Misconception 1. Knowing the computation graph resolves every causal question

The graph gives the structure of model computation, but which intervention represents the research concept and which input population is being studied must be defined separately.

### Misconception 2. An internal-node intervention gives a causal effect in the external world

Counterfactual computation within a fixed model and the real-world data-generating process are different systems.

## Exercises

### 1. Observation and intervention

For $H=2X$ and $Y=H+X$, calculate the observed difference in $Y$ between $X=1$ and $X=2$.

<details>
<summary>Show solution</summary>

With $X=1$, $H=2,Y=3$; with $X=2$, $H=4,Y=6$. The observed difference is 3.

</details>

### 2. Node intervention

Keeping $X=2$ and fixing $H$ at 2, what is $Y$, and how does it differ from the original $X=2$ run?

<details>
<summary>Show solution</summary>

$Y=2+2=4$. This is a change of $-2$ from the original value of 6. The direct path from $X$ remains intact.

</details>

### 3. Cutting an edge

Explain which computation $do(H=2)$ cuts and which computations it preserves.

<details>
<summary>Show solution</summary>

It overwrites the $X\to H$ computation and preserves the $H\to Y$ and $X\to Y$ computations.

</details>

### 4. Paired design

What is the advantage of applying both intact and patched conditions to the same prompt?

<details>
<summary>Show solution</summary>

Prompt difficulty and baseline score enter both conditions in common. Calculating the condition difference within a prompt can reduce this variation.

</details>

### 5. Limiting scope

Write a justified conclusion when an attention-head intervention changes a logit.

<details>
<summary>Show solution</summary>

State that the intervention on that head's output changed the result for the specified input population, patch value, and logit metric. Do not generalize this to the head being a cause of a human concept.

</details>

### 6. Writing the contract

List three items besides location that should be recorded for an internal-node intervention.

<details>
<summary>Show solution</summary>

Record the source and base runs, overwrite timing, and outcome metric. Input pairs and controls must also be fixed.

</details>

## Sources and update boundaries

Interchange interventions between neural representations and interpretable variables follow [Geiger et al. (2021)](https://arxiv.org/abs/2106.02997). This lesson distinguishes interventions in internal model computation from real-world causal effects.

## Lesson summary

- Observation retains original generating paths; intervention overwrites the incoming computation at the selected node.
- Paired runs measure condition differences on the same input.
- Intervention location, value, timing, and metric determine the estimand.
- Do not extend internal model causal effects to causality in the external world.

## Pass criteria

- Can you distinguish conditional observation from a $do$ intervention?
- Can you calculate intervention outcomes in a small computation graph?
- Can you write an internal-intervention contract and limit the scope of its claims?

## Next lesson

- [I07-06 Ablation](I07-06-ablation.md)

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] Observation and intervention are distinguished using a computation graph.
- [x] Paired effects and scope restrictions are included.
- [x] Every exercise has a solution.
- [x] The strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and mathematical rendering have been checked.
