---
id: "I07-17"
title: "Capstone exercise: a small circuit"
part: 3
stage: "I07"
status: "complete"
prerequisites: ["I07-16"]
estimated_time: "180–240 minutes"
---

# I07-17. Capstone exercise: a small circuit

## Why this lesson matters

Collecting attribution heatmaps, patch effects, and component lists separately does not produce a circuit report. Define one behavior and connect node-and-edge hypotheses, discovery, necessity and sufficiency, off-manifold diagnostics, controls, and statistics in a single contract. This lesson brings I07 together in a small reproducible circuit report.

## Learning objectives

- Predefine the behavior, input population, and outcome.
- Connect the node-and-edge graph with each intervention's estimand.
- Apply necessity, sufficiency, and faithfulness tests to held-out data.
- Report results and limitations through a manifest, tables, and bounded claims.

## Prerequisite check

- Prerequisite lesson: [I07-16 Evaluating CoT faithfulness](I07-16-cot-faithfulness.md)
- Check question: Why is using the peak effect selected on a discovery set as a confirmatory effect on the same data an overestimate?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $G_C=(V_C,E_C)$ | `G sub C equals V sub C E sub C` | Candidate circuit graph | directed graph |
| $m(x)$ | `m of x` | Behavioral outcome | scalar |
| $N_C$ | `N sub C` | Circuit necessity effect | scalar |
| $S_C$ | `S sub C` | Circuit sufficiency effect | scalar |
| $F_C$ | `F sub C` | Circuit-only faithfulness score | scalar |
| claim ledger | `claim ledger` | A table connecting evidence, controls, and scope | report artifact |

## 1. The report's question

An example question follows this form:

> In a fixed input population, are the candidate copy and gate paths functionally involved in producing the target-minus-foil logit?

Report a continuous logit metric, inclusion and exclusion criteria, and the experimental unit, not just a behavioral success rate.

## 2. A step-by-step contract

### A. Behavior and data

- Input sources, groups, and held-out split
- Target and foil tokenization
- Primary outcome and failure threshold
- Independent experimental unit

### B. Candidate discovery

- Use gradients and perturbations as search tools
- Select candidate nodes through activation tracing
- Select candidate edges through path patching
- Do not revise candidates using data outside the discovery set

### C. Circuit validation

- Necessity: remove $C$ from the intact computation
- Sufficiency: restore $C$ to a predefined baseline
- Faithfulness: compare the computation retaining only $C$ with intact
- Completeness: apply the same internal circuit removal to the full model and $C$, then compare
- Minimality: check node- and edge-level contributions; with redundancy, also test conditions that remove some other paths
- Off-manifold distance and matched controls

Necessity asks what is lost by removing a candidate from a previously functioning computation. Sufficiency asks what is gained by restoring it to a weakened baseline. Because their starting states differ, do not treat the two values as positive and negative effects of the same cause. Even a candidate that passes faithfulness may fail to reproduce auxiliary paths retained in the full model after an internal path is removed. Completeness checks that omission. A graph list alone does not specify the baseline and removal/restoration rules for each comparison.

### D. Statistics and claims

- Unit-level paired effects and intervals
- Random-graph and magnitude-matched controls
- The search family and multiplicity handling
- Report all passed and failed gates
- Include only supported input and model scopes in the claim

## 3. A synthetic circuit

The CPU exercise's behavior is

$$
m(x)=x_0+x_0x_1
$$

The copy path transmits $x_0$ and the gate path transmits $x_0x_1$. Their sum exactly reproduces the defined full graph, but this is ground truth in a synthetic example constructed with a known structure.

<!-- I07_EXAMPLE: i07_17_circuit_report -->

Calculate copy, gate, and joint ablations and a random control on 64 independent synthetic inputs. Limit the conclusion to causal involvement of the two specified paths in this synthetic behavior.

Each input coordinate in the exercise is $-1$ or $1$. Removing copy leaves only $x_0x_1$; removing gate leaves only $x_0$. Removing both paths gives output 0. For example, at $x=(1,-1)$ the intact output is $1-1=0$, the output without copy is $-1$, and the output without gate is $1$. Each path changes the output, but they cancel in the original state. Thus, the joint removal effect need not equal the sum of the individual removal magnitudes.

The exercise takes the absolute intact-versus-ablated output difference for each input, then averages. This measures how much the output changes, a different metric from the mean decrease in the target-minus-foil logit. In a signed mean, increases and decreases can cancel; in a mean absolute difference, they do not. These results alone do not determine whether each path is necessary for reaching a behavioral success threshold.

The code's `complete_for_defined_graph` flag checks whether the intact output equals the sum of the two path contributions. It checks the decomposition of a known synthetic formula, not the full completeness procedure for testing omitted paths in a general model. `random_control` is also a comparison condition in the code: swap the two input coordinates and exclude copy. Because swapping coordinates leaves the product $x_0x_1$ unchanged, this condition equals gate-only. Do not interpret it as a specificity test using a separately sampled random graph.

The following figures trace cancellation and removal outcomes along the known synthetic paths. Distinguish effect signs from magnitudes for the same input and check which term the code's swapped-input control actually retains.

<figure class="lesson-figure" markdown="1">

![Known synthetic input one minus one branches x0 into copy one and gate minus one while x1 feeds the gate and both updates sum to output zero](../../figures/assets/I07/I07-17-known-copy-gate-graph.svg)

<figcaption>This is the text's x = (1,−1). The value x₀ travels through copy as 1 and is also multiplied by x₁ to form gate value −1. The two paths sum to intact output 0. This is a ground-truth diagram of a known synthetic structure, not a circuit discovered in an actual model.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![For known input one minus one synthetic score zero changes to minus one without copy plus one without gate and zero without both so individual absolute changes one one do not add to joint zero](../../figures/assets/I07/I07-17-cancelling-path-removals.svg)

<figcaption>For the same x = (1,−1), outputs are −1 without copy, 1 without gate, and 0 without both paths. Their absolute differences from intact 0 are 1, 1, and 0, so the joint magnitude does not equal 1 + 1. This is not itself a necessity judgment about behavioral success.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Signed intact-minus-ablated means and mean absolute changes for copy gate and joint computed on exactly the same sixty four seeded synthetic inputs show cancellation versus change magnitude](../../figures/assets/I07/I07-17-signed-and-absolute-means.svg)

<figcaption>This calculates Δ = intact − ablated for 64 synthetic inputs with the existing CPU seed 20261001. The upper panel shows the signed mean; the lower shows the mean absolute difference used in the exercise. Directional cancellation and change magnitude are different metrics. Do not read these values as target-minus-foil decreases in an actual model.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Original input one minus one and swapped minus one one both exclude the copy path and yield identical gate product minus one because coordinate multiplication commutes rather than sampling a random graph](../../figures/assets/I07/I07-17-swapped-control-equivalence.svg)

<figcaption>The code's random_control swaps the coordinates and excludes copy. In this synthetic formula, x₀x₁ = x₁x₀, so both conditions produce gate-only output −1. This does not establish specificity through a separately sampled random graph.</figcaption>

</figure>

## 4. Connection to the Pythia pilot

The Pythia result in I07-07 validates an intervention pipeline on an actual model. Layer 5 MLP patch recovery of 0.0625 alone does not establish that a small circuit has been discovered. Extending this to actual circuit research additionally requires:

- Multiple independent prompt pairs and a held-out split
- Separate layer/token discovery and confirmatory evaluation
- Patches for attention and MLP nodes and individual edges
- Necessity, sufficiency, and random-graph controls
- Manifold diagnostics, bootstrap intervals, and failure cases

## 5. Claim ledger

| Evidence | Directly supported claim | Claim not yet supported |
|---|---|---|
| Gradient/DLA | Local or direct alignment with the target score | Component necessity |
| Activation patch | Local causal effect of the specified patch | Unique storage location |
| Ablation | Necessity under the specified baseline | Sufficiency |
| Restoration | Sufficiency under the specified baseline | Generalization to other inputs |
| Held-out paired test | Repeatability within the input population | Generalization to other models |

## Common misconceptions

### Misconception 1. Agreement across methods proves a circuit

Methods sharing a metric and corruption can share errors. Independent controls and held-out interventions are needed.

### Misconception 2. Success on synthetic ground truth establishes success in an actual model

A synthetic example checks implementation. It does not eliminate distributed representation, redundancy, or off-manifold problems in actual models.

## Exercises

### 1. Define the behavior

Turn “Find a copy circuit” into an observable question.

<details>
<summary>Show solution</summary>

For example, state that the study seeks a node-and-edge set that increases the target-minus-foil logit for a next token matching the source token in a fixed repeated-token prompt population, then validates it on held-out prompts.

</details>

### 2. Nodes and edges

A copy head has been proposed as a node. What else must an edge hypothesis specify?

<details>
<summary>Show solution</summary>

Specify which head output at which source token is transmitted to which receiver's Q, K, V, or residual input.

</details>

### 3. Necessity and sufficiency

Ablating the candidate lowered the metric, but restoring only that candidate to an empty baseline did not recover it. What does this mean?

<details>
<summary>Show solution</summary>

There is evidence of necessity under the specified conditions, but not of sufficiency alone. Other auxiliary components may be needed.

</details>

### 4. Failed control

The candidate graph and random graph had similar effects. How does the report's conclusion change?

<details>
<summary>Show solution</summary>

State that the proposed graph's specificity was not established. Consider whether the search rule or intervention magnitude selected a general disruption.

</details>

### 5. Held-out failure

The effect was large on discovery prompts but near 0 on held-out prompts. Write a justified conclusion.

<details>
<summary>Show solution</summary>

The candidate fit the discovery sample but did not generalize to the predefined population. It failed the conditions for a final circuit claim.

</details>

### 6. Final claim

List three scope limits to retain even after necessity, sufficiency, and held-out controls all pass.

<details>
<summary>Show solution</summary>

Retain the model revision, input population and behavioral metric, and ablation/restoration baselines. Uniqueness of the graph and generalization to all models are separate claims.

</details>

## Evidence and update boundaries

Use [Wang et al. (2022)](https://arxiv.org/abs/2211.00593) for faithfulness, completeness, and minimality evaluation of an end-to-end circuit, and [Zhang and Nanda (2023)](https://arxiv.org/abs/2309.16042) for sensitivity to patching design. New automated circuit-discovery methods do not remove the need for these report gates.

## Lesson summary

- A small circuit report connects behavior, graph, interventions, controls, and statistics in one contract.
- Attribution and localization serve discovery, followed by necessity, sufficiency, and held-out validation.
- Off-manifold diagnostics and random-graph controls limit claims about intervention specificity.
- Actual model claims are bounded by model revision, inputs, metric, and baseline.

## Pass criteria

- Can you write a reproducible plan from behavior to circuit graph?
- Can you distinguish the necessity, sufficiency, and faithfulness gates?
- Can you write a bounded claim that includes failed controls and held-out results?

## Next steps

Starting with [I08-01 Checkpoint study design](../I08/I08-01-checkpoint-study-design.md), compare multiple checkpoints to trace when features and behaviors form.

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Behavior, nodes, edges, interventions, controls, and statistics are connected.
- [x] Necessity, sufficiency, and faithfulness are distinguished.
- [x] Off-manifold and held-out failure gates are included.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is implicitly required.
- [x] Internal links and math rendering have been checked.
