---
id: "I07-11"
title: "Representing a circuit as a graph"
part: 3
stage: "I07"
status: "complete"
prerequisites: ["I07-10"]
estimated_time: "90–120 minutes"
---

# I07-11. Representing a circuit as a graph

## Why this lesson matters

A circuit claim is not a component list. It is a hypothesis about which behavior is explained by computations at particular nodes and edges. A graph makes the node granularity, edge messages, and untested gaps explicit. Distinguish the full model's computation graph from the analyst's proposed sparse circuit.

## Learning objectives

- Define the behavioral metric and input distribution first.
- Construct a directed graph specifying nodes, edges, and messages.
- Calculate a topological order and paths.
- Distinguish faithfulness, completeness, and minimality tests.

## Prerequisite check

- Prerequisite lesson: [I07-10 Residual and logit attribution](I07-10-residual-logit-attribution.md)
- Check question: Why does a component's direct logit contribution differ from the total effect of removing it?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $G=(V,E)$ | `G equals V E` | Circuit graph | directed graph |
| $v\in V$ | `v in V` | A node such as a neuron, head, MLP, or subspace | component |
| $(u,v)\in E$ | `the edge from u to v is in E` | A directed message path to test | edge |
| faithfulness | `faithfulness` | How well the proposed circuit reproduces the behavior | metric |
| completeness | `completeness` | How well the circuit retains the model's functional paths under removal tests | metric |
| minimality | `minimality` | Absence of unnecessary nodes or edges | property |

## 1. Behavior comes first

Instead of “a capital-city circuit,” write something like:

> Explain the behavior in which the target-minus-foil next-token logit is positive over a fixed prompt population.

Fix input inclusion and exclusion rules, tokenization, the outcome, and the success threshold to interpret the graph's test results.

## 2. Nodes and edges

Depending on the analysis granularity, a node can be a whole attention head, a head's output at a particular token, an MLP, a neuron, or a learned feature. An edge specifies which message from the source node enters which input of the receiver. Being in an earlier layer does not itself establish an edge.

$$
G_C=(V_C,E_C)\subseteq G_{\mathrm{model}}.
$$

The proposed circuit $G_C$ is a hypothesis about part of the full computation graph.

In a graph for a feed-forward execution, a sender's value must be computed before a receiver that reads it. A topological order lists nodes so that every edge respects this ordering. To obtain an order, repeatedly select a node with no incoming edges and remove its outgoing edges. If several nodes are available at once, more than one order may be possible. If nodes remain but none can be selected, that part of the graph has a directed cycle. This structural check verifies computation order; interventions must separately test whether each edge is functionally necessary for the target behavior.

The following figures trace dependencies and queue changes in the CPU DAG, then compare a graph with a cycle.

<figure class="lesson-figure" markdown="1">

![Four-node CPU DAG branches input into copy head and MLP gate then merges both at logit with no edge between the two middle nodes](../../figures/assets/I07/I07-11-cpu-dag-dependencies.svg)

<figcaption>These are the existing CPU exercise's four nodes and four edges. After input, copy_head and mlp_gate do not read each other's values, so their order can be exchanged; logit waits for both. This is a structural diagram, not proof of each edge's effect on the target behavior.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Four queue states start with input then copy and MLP then MLP then logit reflecting incoming edges removed by the CPU topological-order algorithm](../../figures/assets/I07/I07-11-topological-ready-queue.svg)

<figcaption>This follows the same CPU DAG's indegree-0 queue. Processing input makes copy and MLP ready together. After only copy is processed, logit still waits for MLP's input. The code's FIFO selection returns one of several possible orders.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Three vertical nodes A B C have forward edges and a red return edge from C to A making every node have an incoming edge and preventing any topological first node](../../figures/assets/I07/I07-11-cycle-no-ready-node.svg)

<figcaption>This adds C→A to the exercise's A→B→C. To choose the first node, A waits for C, B for A, and C for B, leaving no indegree 0 node. The failure concerns a directed cycle in the structure, not an effect test of which function matters.</figcaption>

</figure>

## 3. Three validation questions

- Faithfulness: How well is the original behavior reproduced when only the circuit is retained?
- Completeness: After removing the same internal part of the circuit, do the full model and the circuit continue to behave similarly?
- Minimality: Have you checked the conditions under which removing each node or edge changes the behavioral metric?

Reproducing the behavior after removing everything outside the circuit does not pass both faithfulness and completeness. Consider I07-06's $Y=\max(h_1,h_2)$ with both values equal to 1 and zero ablation. A circuit retaining only $h_1$ also reproduces $Y=1$. But removing $h_1$ makes that circuit output 0, while the full model retains $h_2$ and still outputs 1. Different responses to the same internal removal reveal an omitted redundant path. [Wang et al.'s completeness test](https://arxiv.org/html/2211.00593v1#S4.SS1) checks this difference.

For minimality, which other components remain also matters. In the example, a circuit containing both paths has individual removal effects of 0, but after one path is removed, removing the other changes the behavior. Distinguish a conditional test that first removes redundancy from a single removal in the original circuit. A changed metric after removing one node does not prove that the smallest circuit among all possible graphs has been found.

These three quantities depend on the intervention method and baseline.

Record the removal sets tested and the input scope. Do not extend success on some sets into a guarantee for every possible removal. Here completeness concerns omitted functional paths, a different meaning from the attribution-sum equality in I07-03.

The next three figures compare behavior reproduction, responses to the same internal removal, and redundant-path conditions in the same max example.

<figure class="lesson-figure" markdown="1">

![Original max model with both hidden values one and a circuit keeping only first hidden value both output one despite an omitted redundant second path](../../figures/assets/I07/I07-11-faithfulness-spare-path.svg)

<figcaption>In the text's max example, h₁ and h₂ both equal 1, giving Y = 1 in the full model. A circuit that zero-ablates h₂ and retains only h₁ also reproduces Y = 1. Passing faithfulness alone does not establish that no redundant path was omitted.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Removing first hidden value leaves second hidden one in the full max model outputting one whereas the same removal from a circuit that omitted the second path outputs zero](../../figures/assets/I07/I07-11-completeness-matched-removal.svg)

<figcaption>The same h₁ removal is applied to both the full model and the proposed circuit. The full model stays at 1 because of h₂, but the circuit falls to 0. This difference under the same internal removal reveals an omitted functional path.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Two before-after panels remove first hidden value from one to zero while fixed second path one yields no max-output change and fixed second path zero yields a drop of one](../../figures/assets/I07/I07-11-conditional-minimality.svg)

<figcaption>The same h₁ removal from 1→0 is compared under two conditions. Retaining h₂ = 1 gives an effect of 0; first removing it by setting h₂ = 0 gives an effect of 1. Distinguish a single removal in the original circuit from a conditional test after removing a redundant path.</figcaption>

</figure>

## 4. CPU exercise

<!-- I07_EXAMPLE: i07_11_circuit_graph -->

Construct a DAG with four nodes and four edges and calculate a topological order. A structural check for an acyclic graph is not a causal sufficiency test.

## Common misconceptions

### Misconception 1. An attention pattern establishes an edge

A large attention weight does not ensure a large message or an output effect. An edge intervention is needed.

### Misconception 2. A sparse graph is automatically a good explanation

A graph that is too sparse may fail to reproduce the behavior or may fit only the selected data.

## Exercises

### 1. Identify a DAG

Do edges $A\to B$, $B\to C$, and $A\to C$ form a DAG?

<details>
<summary>Show solution</summary>

Yes, because there is no directed cycle. One topological order is $A,B,C$.

</details>

### 2. Cycle

What changes if $C\to A$ is added to the preceding graph?

<details>
<summary>Show solution</summary>

It creates the cycle $A\to B\to C\to A$, so no topological order exists. This does not fit a time-unrolled graph of an ordinary feed-forward pass.

</details>

### 3. Node granularity

Explain the tradeoff between using “layer 5” as a node and using “the last-token output of layer 5 head 2.”

<details>
<summary>Show solution</summary>

A layer node requires fewer experiments but mixes several computations. Head-and-token nodes are more specific but increase the number of candidates and the multiple-comparison burden.

</details>

### 4. Faithfulness

A model retaining only the proposed circuit reproduces 90% of the original logit difference. What can you state directly?

<details>
<summary>Show solution</summary>

State that the circuit reproduced 90% of this metric for the specified inputs and retention/removal rules. Do not generalize this to explanations of other behaviors.

</details>

### 5. Minimality

Removing an edge did not change the metric. Give two possible interpretations.

<details>
<summary>Show solution</summary>

The edge may be unnecessary, or another edge may provide a redundant function. The test could also have low power, or the metric could miss the edge's role.

</details>

### 6. Edge evidence

Propose a way to test an edge beyond its attention weight.

<details>
<summary>Show solution</summary>

Apply a path patch that replaces only the message from sender to receiver with its source value, then compare the outcome difference with a matched edge control.

</details>

## Evidence and update boundaries

Use [Elhage et al. (2021)](https://transformer-circuits.pub/2021/framework/index.html) for the framework treating Transformer circuits as computational hypotheses about nodes and edges, and [Wang et al. (2022)](https://arxiv.org/abs/2211.00593) for quantitative validation of an end-to-end circuit.

## Lesson summary

- A circuit is a sparse directed-graph hypothesis explaining a specified behavior.
- Specify node granularity and edge messages concretely.
- Faithfulness, completeness, and minimality ask different validation questions.
- A structural DAG check alone does not validate a causal circuit.

## Pass criteria

- Can you state the behavior and graph together?
- Can you calculate a topological order?
- Can you distinguish the three circuit-validation criteria?

## Next lesson

- [I07-12 Necessity and sufficiency](I07-12-necessity-sufficiency.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] The behavior, node, and edge definitions are connected.
- [x] The three circuit-validation criteria are distinguished.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is implicitly required.
- [x] Internal links and math rendering have been checked.
