---
id: "I07-12"
title: "Necessity and sufficiency"
part: 3
stage: "I07"
status: "complete"
prerequisites: ["I07-11"]
estimated_time: "90–120 minutes"
---

# I07-12. Necessity and sufficiency

## Why this lesson matters

Whether removing a component disrupts a behavior is different from whether restoring that component alone to a weak baseline produces the behavior. The former provides evidence of necessity; the latter provides evidence of sufficiency. A redundant path may be sufficient but not necessary. An element that must work with others may be necessary but not sufficient on its own.

## Learning objectives

- Define the intervention conditions for necessity and sufficiency separately.
- Calculate counterexamples involving redundancy and synergy.
- Explain the roles of empty and intact baselines.
- Design separate controls for the two claims.

## Prerequisite check

- Prerequisite lesson: [I07-11 Representing a circuit as a graph](I07-11-circuit-graph.md)
- Check question: How does a completeness test applying the same internal removal to the full model and circuit differ from a minimality test evaluating the necessity of elements within the circuit?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $Y_{\mathrm{intact}}$ | `Y intact` | Outcome of the original computation | scalar |
| $Y_{-C}$ | `Y with C removed` | Outcome after removing candidate $C$ | scalar |
| $Y_{+C\mid B}$ | `Y with C added to baseline B` | Outcome after restoring only $C$ to baseline $B$ | scalar |
| necessity | `necessity` | Removal weakens the behavior | intervention claim |
| sufficiency | `sufficiency` | Restoration produces the behavior | intervention claim |

## 1. Two effects

The necessity effect removes the candidate from the intact computation.

$$
N_C=Y_{\mathrm{intact}}-Y_{-C}.
$$

The sufficiency effect restores the candidate to a specified baseline $B$.

$$
S_C=Y_{+C\mid B}-Y_B.
$$

Sufficiency depends on what $B$ is. Mean-ablating the rest of the model and leaving it in a resampled state ask different questions.

The two equations start from different conditions. $N_C$ removes $C$ while retaining the rest of the intact computation; $S_C$ restores only $C$ while retaining a weakened baseline. Read the signs above under the convention that a larger outcome means stronger desired behavior. If $S_C$ is positive but the behavioral success criterion is not reached, distinguish improvement through restoration from a judgment of sufficiency on its own. Alongside the raw effects, report the outcomes after removal and restoration and the predefined success criterion.

The following figure shows how to read positive improvement separately from reaching the predefined success criterion.

<figure class="lesson-figure" markdown="1">

![Illustrative baseline outcome zero point one increases to zero point four after restoring C but both are below the fixed success threshold one even though effect zero point three is positive](../../figures/assets/I07/I07-12-improvement-versus-success.svg)

<figcaption>The illustrative outcome increases from baseline 0.1 to 0.4 after restoration, giving S_C = 0.3. If the predefined success criterion is at least 1, there is improvement but not success. These numbers are not actual model experiment results.</figcaption>

</figure>

## 2. Redundancy and synergy

For $Y=\max(A,B)$ with $A=B=1$, neither A nor B is individually necessary, but each is sufficient from an empty baseline. In contrast, for $Y=A\cdot B$ with both values equal to 1, each element is necessary but not sufficient on its own.

In this section, $A,B$ are component values. Removal means setting a value to 0, and success means obtaining $Y=1$. For max, the intact value 1 equals the outcome after removing A, $\max(0,1)=1$, so the necessity effect is 0. Restoring only A from an empty state gives $\max(1,0)-\max(0,0)=1$ and succeeds. For the product, removing A gives $0\cdot1=0$, an effect of 1, but restoring only A from an empty state still gives $1\cdot0=0$. Restoration of a single element fails because the two must be present together.

The following state diagrams compare the starting states and changes in Y for removal above and restoration below.

<figure class="lesson-figure" markdown="1">

![Binary max state graph has output zero only at zero zero and output one at the other three states with top arrow removing A from intact one one and bottom arrow restoring A from empty zero zero](../../figures/assets/I07/I07-12-redundancy-two-starts.svg)

<figcaption>The number in each circle is Y, and the axes are component values A and B. The upper red arrow removes A from intact (1,1) to reach (0,1), leaving Y = 1. The lower purple arrow restores A to empty (0,0), reaching (1,0) and changing Y from 0→1.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Binary product state graph has output one only at one one with top A removal changing one to zero and bottom restoration from empty keeping output zero](../../figures/assets/I07/I07-12-synergy-two-starts.svg)

<figcaption>The same axes and intervention directions are applied to Y = A×B. Removing A from intact changes Y from 1→0, establishing necessity, but restoring only A to empty leaves B = 0 and Y = 0. The two effects are calculated from different starting states.</figcaption>

</figure>

## 3. Set-level claims

A circuit set $C$, rather than an individual node, can be the unit of analysis. Evaluate set removal and restoration first, then analyze internal minimality separately. Reporting many component-level p-values does not establish a set effect.

The following figure checks which paths remain when A alone is removed versus when the entire set C is removed.

<figure class="lesson-figure" markdown="1">

![Two max circuit diagrams group A and B in set C and contrast removing A alone leaving B one and outcome one versus removing both in C yielding zero and effect one](../../figures/assets/I07/I07-12-joint-set-removal.svg)

<figcaption>The existing max circuit has intact outcome 1. Removing only A leaves path B and gives effect 0, whereas removing C = {A,B} together sets both values to 0 and gives effect 1. A set effect is a different analysis target from a list of independent node p-values or individual removal effects.</figcaption>

</figure>

## 4. CPU exercise

<!-- I07_EXAMPLE: i07_12_necessity_sufficiency -->

In a max circuit with two redundant paths, A is not individually necessary but is sufficient from an empty baseline. Joint ablation reveals redundancy.

## Common misconceptions

### Misconception 1. Sufficiency implies necessity

With redundant paths, one path can produce the behavior alone, yet another replaces it when it is removed.

### Misconception 2. Necessity and sufficiency use the same baseline

Necessity removes a candidate from intact; sufficiency restores it to a specified weakened baseline. Their starting conditions differ.

## Exercises

### 1. Redundancy

Find A's necessity effect for $Y=\max(A,B)$ with $A=B=1$.

<details>
<summary>Show solution</summary>

The intact outcome is 1. Setting A to 0 still gives outcome 1 because B is 1, so the necessity effect is 0.

</details>

### 2. Sufficiency

In the preceding circuit, what is the sufficiency effect of restoring only A to 1 from baseline $(A,B)=(0,0)$?

<details>
<summary>Show solution</summary>

The baseline outcome is 0 and the restored outcome is 1, so the effect is 1.

</details>

### 3. Synergy

For $Y=A\cdot B$ with $A=B=1$, is A necessary? Is it sufficient alone?

<details>
<summary>Show solution</summary>

Removing A gives outcome 0, so A is necessary. Restoring only A to an empty baseline with B=0 still gives outcome 0, so it is not sufficient alone.

</details>

### 4. Baseline dependence

Why can changing the baseline in a sufficiency experiment change the conclusion?

<details>
<summary>Show solution</summary>

The candidate may need auxiliary paths to work. The restoration effect depends on whether the baseline retains or removes those paths.

</details>

### 5. Circuit set

Explain why a set $C$ can be necessary even when each node's individual effect is small.

<details>
<summary>Show solution</summary>

If there is redundancy within the set, the remaining elements compensate when one is removed. Removing the whole set eliminates the shared function.

</details>

### 6. Reporting statement

A candidate circuit passed both necessity and sufficiency tests. Write a safe conclusion.

<details>
<summary>Show solution</summary>

State that, for the specified inputs, outcome, and removal/restoration baselines, evidence supports the circuit set's necessity for the behavior and its sufficiency from that baseline. Do not call it the unique mechanism for all inputs.

</details>

## Evidence and update boundaries

Refer to [Wang et al. (2022)](https://arxiv.org/abs/2211.00593) for circuit faithfulness, completeness, minimality, and intervention evaluation. Do not omit the baseline or input population used in necessity and sufficiency claims.

## Lesson summary

- Necessity removes a candidate from intact; sufficiency restores it to a weakened baseline.
- Redundancy can make a path sufficient but not necessary.
- Synergy can make an element necessary but not sufficient alone.
- Distinguish claims about nodes from those about circuit sets.

## Pass criteria

- Can you define the two effects as different experiments?
- Can you calculate counterexamples involving redundancy and synergy?
- Can you write a bounded conclusion specifying the baseline?

## Next lesson

- [I07-13 Mediation and counterfactuals](I07-13-mediation-counterfactual.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Necessity and sufficiency baselines are distinguished.
- [x] Redundancy and synergy counterexamples are included.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is implicitly required.
- [x] Internal links and math rendering have been checked.
