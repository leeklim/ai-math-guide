---
id: "I07-09"
title: "Path patching"
part: 3
stage: "I07"
status: "complete"
prerequisites: ["I07-08"]
estimated_time: "120–150 minutes"
---

# I07-09. Path patching

## Why this lesson matters

Node patching changes all downstream paths receiving a component's output together. Path patching attempts to isolate a direct effect by changing only an edge or a restricted path from a sender to a particular receiver. Results cannot be reproduced unless the experiment specifies which edges were allowed to change and which run supplied the fixed values for the others.

## Learning objectives

- Distinguish node interventions from edge interventions.
- Compute the total effect and a specific path effect in a simple DAG.
- Write a contract specifying the sender, receiver, source, and base conditions.
- Avoid overstating a path effect as a complete explanation of a circuit.

## Prerequisite check

- Prerequisite lesson: [I07-08 Causal tracing](I07-08-causal-tracing.md)
- Check question: Why does patching one node change multiple downstream paths leaving that node together?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $A\to B$ | `A to B` | Edge from sender $A$ to receiver $B$ | directed edge |
| $Y_{A\to B\leftarrow a^*}$ | `Y with the A to B edge set to a star` | Outcome after changing a specific edge message | scalar |
| total effect | `total effect` | Effect through all paths leaving a node | scalar |
| direct path effect | `direct path effect` | Effect through only the selected edge or path | scalar |
| sender·receiver | `sender and receiver` | Components that send and receive a message | graph nodes |

## 1. Node and edge interventions

Consider a graph in which $A$ points to $B$ and $C$, and $C$ also points to $B$. Replacing the entire node $A$ with its clean value changes both $A\to B$ and $A\to C\to B$. Replacing only the $A\to B$ message keeps the indirect path at its base values.

$$
\Delta_{A\to B}
=
Y\bigl(do(M_{A\to B}=M_{A\to B}^{c})\bigr)-Y_r.
$$

The contract must state which run supplies the fixed messages on the other edges.

A message is an input read by the receiver, so that input can be replaced without changing the entire sender node. In the existing exercise, $C=2A$ and $B=3A+5C$. At the base value $A=-1$, we have $C=-2$ and $B=-13$. Replacing only the value read by $A\to B$ with the source value of 2 leaves $C$ at $-2$ and gives $B=3\cdot2+5\cdot(-2)=-4$, an effect of 9. Replacing node $A$ with 2 gives $C=4$ and $B=26$, an effect of 39. Even with the same source value, the result depends on which receivers are allowed to receive it.

The next three computation graphs compare the same source and base, changing only the paths allowed to transmit the replacement value.

<figure class="lesson-figure" markdown="1">

![Base A minus one reaches B directly with coefficient three and through C minus two with coefficients two then five producing B minus thirteen](../../figures/assets/I07/I07-09-base-two-paths.svg)

<figcaption>The existing exercise uses the base value A = −1. The direct term 3A = −3 and indirect term 5C = −10 sum to B = −13. The total coefficient is 3 + 2×5 = 13.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Edge-only patch preserves A minus one and C minus two but the direct message m into B is set to clean two yielding B minus four and effect nine](../../figures/assets/I07/I07-09-edge-only-patch.svg)

<figcaption>Node A and C retain their base values of −1 and −2. Only m, the message carried to B by the red direct edge, changes to 2. B = 3×2 + 5×(−2) = −4, an effect of 9 relative to the base.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Node patch sets A to clean two and recomputes C as four so both direct and indirect contributions reach B twenty six and produce total effect thirty nine](../../figures/assets/I07/I07-09-node-all-paths-patch.svg)

<figcaption>Replacing node A itself with 2 also recomputes C = 4. B = 3×2 + 5×4 = 26, giving a total effect of 39 relative to the base. This is a different intervention from changing only the direct edge, whose effect is 9.</figcaption>

</figure>

## 2. Edges in a Transformer

The residual stream is the sum of outputs from multiple components. Isolating the path that sends a sender head's output to a receiver's Q, K, V, or MLP input requires rules for freezing or recomputing the other receivers of that sender output. The counterfactual represented by “path patching” can differ across implementations.

For example, construct the residual sum read by the selected receiver by starting with the base sum, subtracting the sender's base update, and adding its source update. Do not apply the same change to other receivers. If normalization precedes the selected receiver, recompute normalization of the changed sum and the projection that follows it. Replacing the entire receiver output with its source value also replaces the effects of other inputs, so it is not equivalent to changing just one incoming edge from the sender.

The next two figures distinguish the selected receiver's recomputation scope from a nonlinear receiver's dependence on the base context.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two receiver pipelines contrast selected receiver input base residual minus base sender update plus clean sender update followed by recomputed normalization and projection with an untouched other receiver at base residual](../../figures/assets/I07/I07-09-receiver-specific-residual.svg)

<figcaption>This contract constructs only the selected receiver's input as r_r − h_r + h_c. It recomputes normalization and the projection/MLP from the changed sum, while other receivers retain the original base sum. The figure does not replace the entire receiver output with its clean value.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Three illustrative ReLU of message plus other-path base plots compare bases minus two zero and two while the same message change zero to one has effects zero one and one](../../figures/assets/I07/I07-09-relu-base-context.svg)

<figcaption>For the illustrative receiver Y = ReLU(m + d), m changes from 0→1 while d, the sum from other paths, is fixed. With d = −2 the input remains below the threshold, giving an effect of 0; with d = 0 or 2, the effect is 1. Even the same edge change depends on the conditions at which other paths are held fixed.</figcaption>

</figure>

## 3. Circuit discovery and validation

Selecting large effects among many edges is discovery. Evaluate the faithfulness, completeness, and minimality of a fixed edge set on separate inputs. A large effect for one edge does not establish a complete circuit.

## 4. CPU exercise

<!-- I07_EXAMPLE: i07_09_path_patching -->

The direct coefficient along $A\to B$ is 3, and the indirect coefficient along $A\to C\to B$ is $2\times5=10$. An edge patch changes only the direct path, whereas a node patch changes both, so their effects differ.

## Common misconceptions

### Misconception 1. A path effect has a unique value

In a nonlinear graph with interactions, the value depends on the conditions at which other paths are held fixed.

### Misconception 2. A few large-effect edges make a complete circuit

Missing edges, redundant paths, and input-dependent strategies need to be checked.

## Exercises

### 1. Direct and indirect coefficients

For $C=2A$ and $B=3A+5C$, find the direct and total coefficients of the effect of $A$ on $B$.

<details>
<summary>Show solution</summary>

The direct coefficient is 3. The indirect coefficient is $2\times5=10$, and the total coefficient is 13.

</details>

### 2. Edge patch

With base $A=-1$ and source $A=2$, how much does $B$ change if only the $A\to B$ edge is replaced with its source value?

<details>
<summary>Show solution</summary>

The edge message changes by $2-(-1)=3$, and the direct coefficient is 3, so $B$ changes by 9. Keep the $C$ path fixed at the base.

</details>

### 3. Node patch

Under the same conditions, how much does $B$ change if the entire node $A$ is replaced with its source value?

<details>
<summary>Show solution</summary>

Multiply the total coefficient of 13 by the input change of 3 to obtain 39. Both the direct and indirect paths change.

</details>

### 4. Contract items

List three items, other than the sender and receiver, that must be fixed in a path-patching experiment.

<details>
<summary>Show solution</summary>

Fix the source and base inputs, the freeze/recompute rules for other edges, and the outcome metric. Layer and token locations are also needed.

</details>

### 5. Nonlinearity

Why does a path effect depend on the base conditions when the receiver contains a ReLU?

<details>
<summary>Show solution</summary>

The output effect of the same edge message changes depending on which side of the ReLU threshold the sum from other paths lies.

</details>

### 6. Circuit claims

An edge's effect repeats on held-out inputs. What additional evaluations would bring the evidence closer to a complete-circuit claim?

<details>
<summary>Show solution</summary>

Evaluate faithfulness, whether retaining the candidate edges together reproduces the behavior; completeness, whether the remaining edges can be removed; and minimality, removing unnecessary edges.

</details>

## Sources and boundaries for updates

Examples of edge-level interventions and circuit validation in Transformers follow [Wang et al. (2022)](https://arxiv.org/abs/2211.00593). Freeze rules can differ across implementations, so a paper's name alone does not justify assuming the same estimand.

## Lesson summary

- A node patch changes all downstream paths; a path patch changes selected edges or paths.
- The conditions at which other paths are held fixed determine the path effect.
- Nonlinear interactions can make a path effect depend on the base conditions.
- Edge discovery and circuit validation are separate stages.

## Pass criteria

- Can you compute direct and total effects in a small DAG?
- Can you write a path-patching contract?
- Can you distinguish a large edge effect from a complete-circuit claim?

## Next lesson

- [I07-10 Residual and logit attribution](I07-10-residual-logit-attribution.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Node and edge interventions are distinguished.
- [x] Freeze rules and the limitations due to nonlinearity are included.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is implicitly required.
- [x] Internal links and equation rendering have been checked.
