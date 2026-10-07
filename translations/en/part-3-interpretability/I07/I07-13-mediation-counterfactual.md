---
id: "I07-13"
title: "Mediation and counterfactuals"
part: 3
stage: "I07"
status: "complete"
prerequisites: ["I07-12", "M04-16"]
estimated_time: "120–150 minutes"
---

# I07-13. Mediation and counterfactuals

## Why this lesson matters

Mediation analysis asks how much of an input change's effect on the output flows through a particular internal mediator. Counterfactual activations can be overwritten inside a model, but the definitions of direct and indirect effects depend on which treatment states and mediator values are combined. A simple decomposition of differences is not the same as statistical identification.

## Learning objectives

- Mark the treatment, mediator, and outcome on a computation graph.
- Compute total, direct, and mediated effects in small structural equations.
- Explain how the interventions defining natural and controlled effects differ.
- Limit the scope of mediation results inside a model.

## Prerequisite check

- Prerequisite lessons: [I07-12 Necessity and sufficiency](I07-12-necessity-sufficiency.md), [M04-16 Correlation, prediction, and causation](../../part-1-foundations/M04/M04-16-correlation-causation.md)
- Check question: Which paths are affected differently by replacing an entire node with its source value versus replacing only a particular edge message?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $T$ | `T` | Treatment or input condition | binary or categorical |
| $M(t)$ | `M of t` | Mediator value under treatment $t$ | tensor |
| $Y(t,m)$ | `Y of t m` | Counterfactual outcome with treatment and mediator specified | scalar |
| total effect | `total effect` | Effect of the full treatment change | scalar |
| mediated effect | `mediated effect` | Effect transmitted through the mediator path | scalar |

## 1. Structure and counterfactuals

Suppose both $T\to M\to Y$ and $T\to Y$ are present.

Compare two runs for the same unit of analysis, changing the treatment while holding the other conditions fixed. $M(t)$ is the mediator produced by the original computation under treatment $t$. $Y(t,m)$ is the outcome computed after forcibly replacing only the mediator with $m$ in a run with treatment set to $t$.

The total effect is

$$
\operatorname{TE}=Y(1,M(1))-Y(0,M(0))
$$

The mediated effect that changes only the mediator from $M(0)$ to $M(1)$ while holding the treatment at 1 is

$$
\operatorname{ME}_1=Y(1,M(1))-Y(1,M(0))
$$

If the corresponding direct effect is defined as $Y(1,M(0))-Y(0,M(0))$, the two differences sum to TE. The intermediate value $Y(1,M(0))$ is added and then subtracted, so the identity itself does not require an additive structure.

The decomposition is not unique, however. TE can also be decomposed by pairing a direct effect with the mediator fixed at $M(1)$ and a mediated effect with the treatment fixed at 0. When $T$ and $M$ interact, the individual values differ between these two approaches. Distinguish the identity for the sum from the conditions under which a path effect is measured.

The following figures trace the two paths from the treatment and the sum of differences through an intermediate counterfactual. The interaction examples compare two different decompositions of the same total effect.

<figure class="lesson-figure" markdown="1">

![CPU treatment one reaches outcome seven via direct plus T route and mediator M equals two T then multiplied by three route](../../figures/assets/I07/I07-13-treatment-mediator-paths.svg)

<figcaption>The existing CPU structural equations are M = 2T and Y = T + 3M. At T = 1, the direct term is 1 and the mediator term is 3×2 = 6, giving Y = 7. Read the effect decomposition together with the counterfactual differences being compared below.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Counterfactual grid for additive CPU outcome zero one six seven follows treatment first at mediator zero then mediator change at treatment one with effects one and six](../../figures/assets/I07/I07-13-additive-via-t1.svg)

<figcaption>The numbers inside the circles are outcomes. The bottom T change is Y(1,0) − Y(0,0) = 1, and the right-hand M change is Y(1,2) − Y(1,0) = 6. Adding and subtracting the intermediate value of 1 gives the total effect of 7.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Illustrative product outcome grid zero zero zero two follows treatment first at mediator zero with effect zero then mediator change at treatment one with effect two](../../figures/assets/I07/I07-13-interaction-via-t1.svg)

<figcaption>The existing exercise's Y = T×M is evaluated with M(0) = 0 and M(1) = 2. Changing T first gives a direct effect of 0; changing M at T = 1 gives a mediated effect of 2. The total effect is 2.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![The same product outcome grid follows mediator first at treatment zero with effect zero then treatment change at mediator two with effect two](../../figures/assets/I07/I07-13-interaction-via-t0.svg)

<figcaption>For the same four outcomes, computing the left-hand M change first gives a mediated effect of 0. The T change with M fixed at 2 gives a direct effect of 2. The sum remains 2, but the individual values differ from the previous figure, so this does not mean that the decomposition is unique.</figcaption>

</figure>

## 2. Controlled and natural effects

A controlled direct effect fixes the mediator at the same $m$ for every unit. Natural effects use the $M(t)$ values that would naturally arise under each treatment, combining them across treatment conditions. The latter is a cross-world definition involving the values a single unit would have under two treatments, and identification from observational data requires additional assumptions.

A controlled comparison inserts the same specified value into both runs, as in $Y(1,m)-Y(0,m)$. The direct effect above instead inserts that unit's $M(0)$. Because $M(0)$ can differ across units, this is not the same as an experiment that assigns a single $m$ to every unit. Merely selecting groups of people or inputs by treatment in observational data does not directly reveal the same unit's cross-treatment outcome $Y(1,M(0))$.

Inside a model, values can be obtained from two forward passes and cross-patched. Whether the resulting hybrid state is a meaningful counterfactual still needs a separate check.

The next figure shows the assignments of a common m in a controlled comparison and each unit's own M(0) in a natural comparison side by side.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two illustrative units U and V have cached baseline mediator values zero and one; controlled comparisons assign mediator zero to both treatment states for both units while natural comparisons assign each unit its own cached mediator value](../../figures/assets/I07/I07-13-controlled-natural-assignment.svg)

<figcaption>The illustrative units U and V have M(0) values of 0 and 1, respectively. A controlled comparison assigns the same m = 0 to both treatment runs for every unit; a natural comparison uses each unit's own M(0) in both runs. Observational means from two groups do not mean that the same unit's hybrid outcome has been directly observed.</figcaption>

</figure>

## 3. Mediator granularity

A mediator can be defined as one neuron, a whole head, a token's residual vector, or a subspace. Small units are precise but can break relationships with other states, and more candidates increase the multiple-comparison burden. Large units change several paths together.

Replacing just one coordinate with its clean value leaves the other coordinates in the same vector at their base values. Replacing the whole vector retains its internal relationships from the source run, but compatibility with the base states at other layers and tokens remains a separate question. Neither a small intervention nor the use of a whole vector alone determines counterfactual validity.

The next figure compares the mediator components supplied by a one-coordinate replacement and a whole-vector replacement.

<figure class="lesson-figure" markdown="1">

![Illustrative source mediator vector two two and base zero zero yield partial patch two zero or whole patch two two while other layer and token states stay at base](../../figures/assets/I07/I07-13-mediator-coordinate-whole.svg)

<figcaption>The illustrative source is M = (2,2), and the base is M = (0,0). A one-coordinate replacement mixes source and base components, giving (2,0); a whole-vector replacement brings along the source's internal (2,2) relationship. Other layers and tokens remain at their base states, so neither choice automatically guarantees hybrid-state validity.</figcaption>

</figure>

## 4. CPU exercise

<!-- I07_EXAMPLE: i07_13_mediation_counterfactual -->

For $M=2T$ and $Y=T+3M$, compute a total effect of 7, a direct effect of 1, and a mediated effect of 6. The sum is an identity for the differences paired above. In this additive example, the treatment and mediator do not interact, so the mediated effect also does not differ according to the treatment value at which the mediator change is measured.

## Common misconceptions

### Misconception 1. A total effect always has a unique direct–indirect decomposition

The decomposition can change with interactions and effect definitions. The value at which the treatment is held fixed must also be specified.

### Misconception 2. If a mediator can be patched, the counterfactual is valid

Being technically able to insert a state is different from that state being meaningful under the training distribution.

## Exercises

### 1. Total effect

For $M=2T$ and $Y=T+3M$, find the total effect of $T:0\to1$.

<details>
<summary>Show solution</summary>

When $T=0$, $M=0,Y=0$; when $T=1$, $M=2,Y=7$. The total effect is therefore 7.

</details>

### 2. Mediated effect

Find the effect of changing the mediator from $M(0)=0$ to $M(1)=2$ while keeping $T=1$.

<details>
<summary>Show solution</summary>

It is $Y(1,2)-Y(1,0)=7-1=6$.

</details>

### 3. Direct effect

What is the effect of changing only the treatment from 0 to 1 while fixing the mediator at $M(0)=0$?

<details>
<summary>Show solution</summary>

It is $Y(1,0)-Y(0,0)=1-0=1$. In this additive example, the direct effect of 1 and mediated effect of 6 sum to the total effect of 7.

</details>

### 4. Interaction

If $Y=T\cdot M$, explain why the mediated effect depends on the fixed treatment value.

<details>
<summary>Show solution</summary>

With $T=0$ fixed, changing the mediator leaves the outcome at 0. At $T=1$, the mediator change appears directly in the outcome.

</details>

### 5. Model interventions

What validity problem can arise when cross-patching head outputs from two prompts?

<details>
<summary>Show solution</summary>

It can create a hybrid activation inconsistent with other downstream states. Match the source and base inputs, and check manifold distance or resampled controls.

</details>

### 6. Write a claim

A mediated effect through a particular head repeats. Write a cautious conclusion.

<details>
<summary>Show solution</summary>

State that evidence was obtained that the head's path mediated part of the measured effect for the defined treatment pair, mediator patch, and outcome. Do not generalize it to a universal mediator of a human concept.

</details>

## Sources and boundaries for updates

The application of causal mediation to internal language-model components follows [Vig et al. (2020)](https://proceedings.neurips.cc/paper_files/paper/2020/hash/92650b2e92217715fe312e6fa7b90d82-Abstract.html). Distinguish the identification assumptions for natural effects from the validity of hybrid states inside a model.

## Lesson summary

- Mediation asks which part of a treatment effect flows through an internal mediator.
- Direct and mediated effects depend on which values are fixed and combined across conditions.
- The paired differences sum to TE, but with interactions, their individual values differ across decompositions.
- An executable patch is different from a meaningful counterfactual.

## Pass criteria

- Can you compute the three effects in small structural equations?
- Can you distinguish controlled and natural effects?
- Can you describe mediator granularity and the limitations on validity?

## Next lesson

- [I07-14 Off-manifold interventions](I07-14-off-manifold-intervention.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Treatment, mediator, and outcome are defined.
- [x] Effect definitions and the limitations on identification are distinguished.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is implicitly required.
- [x] Internal links and equation rendering have been checked.
