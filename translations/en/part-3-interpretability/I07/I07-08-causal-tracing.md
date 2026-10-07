---
id: "I07-08"
title: "Causal tracing"
part: 3
stage: "I07"
status: "complete"
prerequisites: ["I07-07"]
estimated_time: "120–150 minutes"
---

# I07-08. Causal tracing

## Why this lesson matters

Causal tracing first disrupts a behavior through corruption, then restores individual layer and token locations to map where a clean state recovers that behavior. This map is a localization tool. Its peak should not immediately be interpreted as the single location where knowledge is stored or the optimal location for weight editing.

## Learning objectives

- Design a causal trace with corruption and restoration stages.
- Compute and read a layer-by-token recovery map.
- Distinguish localization claims from mechanism and editing claims.
- Explain multiple testing and location-selection bias.

## Prerequisite check

- Prerequisite lesson: [I07-07 Activation patching](I07-07-activation-patching.md)
- Check question: Why is normalized recovery unstable when its denominator is small?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $R_{\ell,t}$ | `R sub ell t` | Restoration effect at layer $\ell$, token $t$ | scalar |
| $H\in\mathbb R^{L\times T}$ | `H in R to the L by T` | Recovery heatmap | matrix |
| corruption | `corruption` | Input or state modification that weakens the target behavior | intervention |
| restoration | `restoration` | Restoring a clean activation at one location | patch |
| localization | `localization` | Finding locations with large effects | search result |

## 1. The algorithm

1. Cache all candidate activations from the clean run.
2. Corrupt the input or initial representation to lower the metric.
3. Restore one $(\ell,t)$ location at a time to its clean value.
4. Compute $R_{\ell,t}$ from each patched metric.

$$
H_{\ell,t}
=
\frac{m_{\ell,t}^{\mathrm{restore}}-m_r}{m_c-m_r}.
$$

Keep the same clean–corrupt pair rather than using different inputs for different candidates.

After evaluating one cell, start a fresh run from the corrupt state for the next candidate. If the restored value from the previous cell is retained, the measurement captures the cumulative effect of restoring several locations rather than the effect of one location. With noise corruption, use the same noise draw for every candidate within one repetition, and average and report repetitions with new draws separately. For a contrast with $m_c=m_r$, the normalization above is undefined and must be distinguished from the raw restoration difference.

The following candidate grids show the rule of restoring just one location at a time and restarting the execution state.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three independent candidate state grids each begin from the same corrupt baseline and restore exactly one clean cell while the other three cells remain corrupt](../../figures/assets/I07/I07-08-independent-cell-restoration.svg)

<figcaption>Three candidate locations from the algorithm are shown side by side. Each candidate starts fresh from the same corrupt state and restores only the red cell to the clean value h_c. Retaining the previous candidate's red cell in the next run would make the intervention cumulative.</figcaption>

</figure>

## 2. What the heatmap tells us

A high-valued cell means that the clean state at that location recovered the metric within the otherwise corrupt run. Without further experiments, it does not establish any of the following:

- Information is stored only at that location.
- That location is uniquely necessary in the original clean run.
- Editing the weights of that layer changes only the desired behavior.
- The same location generalizes to other prompts and models.

When the same information passes through several layers, restoring different locations may all produce effects. Restoring a later state may also bypass damage to the earlier computation that produced it. A high recovery value for one cell therefore describes the result of a run in which that location was changed; it does not also explain the original path that produced the state. Each cell is the result of a separate intervention, so the cell values should not be added and read as a decomposition of a single score.

The next two figures distinguish restoring a later state to bypass earlier damage from editing the weights themselves.

<figure class="lesson-figure" markdown="1">

![Two illustrative corrupted chain experiments restore early A or late B to one and both produce Y one while late restoration cuts the damaged A to B dependency and bypasses upstream damage](../../figures/assets/I07/I07-08-late-restoration-bypass.svg)

<figcaption>In the illustrative chain A = X, B = A, Y = B, the corrupt input is X = 0. Separate runs that restore either A or B to 1 both produce Y = 1. Restoring B bypasses damage to the earlier computation, so the two recovery locations alone cannot establish a unique storage location or the original computation path.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Activation restoration combines fixed weights with a new internal state for one run whereas weight editing replaces W by W prime and changes the computation for multiple inputs](../../figures/assets/I07/I07-08-state-versus-weight.svg)

<figcaption>Activation restoration changes the state h* of one run with W held fixed. Weight editing replaces W with W′, changing the function applied to multiple inputs. Successful state restoration at a location does not guarantee successful weight editing at that location.</figcaption>

</figure>

## 3. Separate search from validation

Selecting the maximum after searching hundreds of locations also selects noise peaks. Find the location on discovery inputs, then evaluate the effect of that fixed location again on held-out inputs. Distinguish a heatmap reporting all layers and tokens from the effect of a peak selected after inspecting the results.

In the following search procedure, location selection ends before held-out evaluation begins.

<figure class="lesson-figure" markdown="1">

![Illustrative discovery candidates A B C D lead to choosing C star then freezing the location before an independent held-out input set evaluates that same fixed location without another search](../../figures/assets/I07/I07-08-discovery-frozen-location.svg)

<figcaption>A–D are illustrative candidate identifiers. After selecting C* during discovery, freeze the location and evaluate that same C* on held-out inputs. Selecting the maximum cell again on the held-out inputs would not separate search from confirmation.</figcaption>

</figure>

## 4. CPU exercise

<!-- I07_EXAMPLE: i07_08_causal_tracing -->

Compute a recovery map for 2×2 candidate locations. The maximum in the synthetic graph is at layer 1, token 0, but this applies only to the defined graph and corruption.

The following map gives the recovery for each candidate within the recomputation scope specified in the exercise code.

<figure class="lesson-figure" markdown="1">

![Existing CPU implementation recovery matrix has layer zero row zero zero and layer one row two thirds one third with maximum layer one token zero while a note limits the map to late patching without recomputing layer one](../../figures/assets/I07/I07-08-cpu-recovery-map.svg)

<figcaption>The existing CPU code's clean score of 4, corrupt score of −0.5, and candidate outputs give recovery [[0, 0], [2/3, 1/3]]. Even the layer 0 patch is applied after states[1] has been computed, without recomputing states[1]. Given that implementation scope, the zeros in the first row are not evidence that the original input information was unused.</figcaption>

</figure>

## Common misconceptions

### Misconception 1. A trace peak is the address of knowledge

Restoration effects reflect information, causal bottlenecks, and downstream accessibility together. Do not reduce a distributed computation to a single address.

### Misconception 2. Finding a location also finds an editing location

Activation restoration and weight updates are different interventions. The correlation between localization and editing success needs separate validation.

## Exercises

### 1. Map shape

What is the shape of the recovery map when tracing all 12 layers and 20 tokens?

<details>
<summary>Show solution</summary>

It is $12\times20$. Separating component types adds another axis.

</details>

### 2. Compute recovery

If $m_c=4,m_r=0$ and the restored metric for one cell is 1, what is $H_{\ell,t}$?

<details>
<summary>Show solution</summary>

It is $(1-0)/(4-0)=0.25$.

</details>

### 3. Validate corruption

Why should tracing not proceed when the corrupt run's metric is almost the same as the clean metric?

<details>
<summary>Show solution</summary>

There is no behavioral difference to recover, and the recovery denominator is also small. First check that corruption sufficiently weakens the target behavior.

</details>

### 4. Selection bias

What problem arises when the largest cell is reported as the final effect on the same data used to select it?

<details>
<summary>Show solution</summary>

The procedure selects a location with a large contribution from noise and sample-specific variation, then reuses its value, overestimating the effect. Fix the location and reevaluate it on held-out inputs.

</details>

### 5. Localization and editing

Explain why a trace peak does not guarantee successful weight editing.

<details>
<summary>Show solution</summary>

An activation patch changes the state of one run, whereas a weight edit changes the function applied to all inputs. Their objectives, inputs, and side effects differ.

</details>

### 6. Write a claim

Restoration effects at the same layer and token repeat on held-out prompts. Write a justified conclusion.

<details>
<summary>Show solution</summary>

State that, within the prespecified input scope and corruption, the clean state at that layer and token consistently contributed to recovery of the target metric. Do not call it the unique storage location.

</details>

## Sources and boundaries for updates

Factual-recall localization using noise corruption and state restoration follows [Meng et al. (2022)](https://arxiv.org/abs/2202.05262). For counterexamples to equating localization with editing, also consult [Hase et al. (2023)](https://arxiv.org/abs/2301.04213).

## Lesson summary

- Causal tracing maps activation-restoration effects across multiple locations.
- A heatmap peak is a localization result under the defined corruption and metric.
- Discovery and held-out validation must be separated.
- Localization does not guarantee a complete mechanism or editing success.

## Pass criteria

- Can you explain the tracing procedure and map shape?
- Can you compute a recovery map?
- Can you identify overinterpretation of a peak and selection bias?

## Next lesson

- [I07-09 Path patching](I07-09-path-patching.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Corruption, restoration, and localization are distinguished.
- [x] Selection bias and held-out validation are included.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is implicitly required.
- [x] Internal links and equation rendering have been checked.
