---
id: "I07-07"
title: "Activation patching"
part: 3
stage: "I07"
status: "complete"
prerequisites: ["I07-06", "N05-25"]
estimated_time: "120–150 minutes"
---

# I07-07. Activation patching

## Why this lesson matters

Activation patching inserts an internal state from a clean run into the same location in a corrupt run and measures how much the behavior recovers. Unlike a probe, which reads information from a representation, patching changes the actual forward computation. Its results, however, are sensitive to the clean-corrupt pair, patch location, and metric. A single recovery ratio should not be interpreted as the universal importance of a component.

## Learning objectives

- Define the clean, corrupt, and patched runs precisely.
- Calculate the patch effect and normalized recovery.
- Distinguish module inputs, module outputs, and residual locations.
- State the local causal claims supported by a patching result.

## Prerequisite check

- Prerequisite lessons: [I07-06 Ablation](I07-06-ablation.md), [N05-25 Forward hooks and activation collection](../../part-2-neural-computation/N05/N05-25-hook-activation-collection.md)
- Check question: Why must you record whether a forward hook saved the module input or output?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and conditions |
|---|---|---|---|
| $x_c,x_r$ | `x clean and x corrupt` | Clean and corrupt inputs | Input pair |
| $h_j(x_c)$ | `h sub j of x clean` | Activation at node $j$ in the clean run | Node tensor |
| $m_c,m_r,m_p$ | `m clean, m corrupt, and m patched` | Behavioral metrics for the three runs | Scalars |
| $R_j$ | `R sub j` | Normalized recovery from patching node $j$ | Scalar |
| interchange intervention | `interchange intervention` | Replacement of an internal value with a value from another run | Intervention |

## 1. Three runs

1. Clean: Run $x_c$, which produces the desired behavior, to obtain $h_j(x_c)$ and $m_c$.
2. Corrupt: Run the contrasting input $x_r$ to obtain $m_r$.
3. Patched: During the run on $x_r$, overwrite $h_j$ with $h_j(x_c)$ to obtain $m_p$.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Clean corrupted and patched model runs aligned at one internal activation node](../../figures/assets/I07/I07-07-three-runs.svg)

<figcaption>The patched run retains the corrupt input and replaces only the activation at the specified layer, token, and component with its value from the clean run.</figcaption>
</figure>

All three runs must use the same model parameters and the same metric. The clean run supplies the replacement value and establishes a reference for the target behavior. The corrupt run is the pre-intervention baseline; its difference from the patched run measures the effect of the replacement. Comparing clean and patched runs directly shows how much behavior has recovered, but can obscure the amount of change from the pre-intervention baseline.

$$
R_j
=
\frac{m_p-m_r}{m_c-m_r}.
$$

When $R_j=1$, the chosen metric has recovered to the clean level; when it is 0, there is no change. A small denominator makes the ratio unstable, so report the raw metrics as well. Values below 0 or above 1 are also possible results.

If $m_c=m_r$, the denominator is 0 and recovery is undefined. The raw patch effect $m_p-m_r$ can still be calculated, but it cannot be expressed as a multiple of a baseline gap of 0.

Normalized recovery does not ask how important this node is in general. It asks how far exchanging the value of node $j$ moves the chosen metric across the gap between the two baselines in the selected clean-corrupt contrast. Changing the input pair, the scope of the node, or the metric changes the estimand.

For example, if $m_c=10,m_r=2$ and $m_p=6$, the raw patch effect is $m_p-m_r=4$ and recovery is $4/8=0.5$. The raw effect retains the metric's units, whereas recovery uses the clean-corrupt gap as a reference for comparisons between conditions. Reporting both distinguishes an experiment with a small denominator from one with a large actual change.

The next two figures compare the raw metric gap and the change in recovery caused by a small denominator.

<figure class="lesson-figure" markdown="1">

![Metric axis positions corrupt two patched six clean ten and overshoot twelve show patch distance four and clean-corrupt distance eight yielding recovery one half and overshoot one point two five](../../figures/assets/I07/I07-07-recovery-metric-span.svg)

<figcaption>The values m_c = 10, m_r = 2, and m_p = 6 from the text lie on one metric axis. The purple change of 4 is the numerator, and the green baseline gap of 8 is the denominator. The overshoot at m_p = 12 is retained as 1.25 rather than clipped at 1.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Illustrative inverse curve recovery equals zero point one divided by baseline gap grows from zero point one at gap one to one at gap zero point one and ten at gap zero point zero one](../../figures/assets/I07/I07-07-small-denominator.svg)

<figcaption>The illustrative raw patch effect is fixed at 0.1. For clean−corrupt gaps of 1, 0.1, and 0.01, recovery is 0.1, 1, and 10. At a gap of 0, the ratio represented by this curve is undefined.</figcaption>

</figure>

## 2. Patch location

In a Transformer, saying only that "layer 5 was patched" is insufficient.

- Layer input or output in the residual stream
- Attention or MLP input or output
- Entire token tensor or a specific token
- Entire hidden vector, a neuron coordinate, or a subspace
- Before or after normalization

Different locations change different sets of edges and downstream computations.

The patch location determines the meaning of the intervention, not just a tensor address. Replacing the entire residual stream changes the accumulated outputs of multiple components up to that point. Replacing only a particular attention head's output changes a narrower update, while leaving intact the way subsequent residual addition and MLP computation read that value. When replacing a single neuron or a subspace, also record the chosen coordinate system and projection definition.

Let $h_c,h_r$ be the clean and corrupt hidden vectors at the same location, and let $P$ be the orthogonal projection onto the selected subspace. A partial replacement can be constructed as $h_r+P(h_c-h_r)$. Components in the selected subspace take their clean values, while those in its orthogonal complement retain their corrupt values. If $P$ is the identity, the entire vector is replaced; if it projects onto selected coordinates, only those coordinates are replaced. In every case, the downstream computation after this value resumes from the patched state.

The following coordinate plot shows the corrupt component retained by a partial projection replacement.

<figure class="lesson-figure" markdown="1">

![Illustrative coordinate vectors corrupt one one clean three two and partial-patched three one show a horizontal projection replacing only the first coordinate and preserving the second corrupt component](../../figures/assets/I07/I07-07-subspace-partial-patch.svg)

<figcaption>This illustration uses h_r = (1, 1), h_c = (3, 2), and a projection P onto the first coordinate. Adding P(h_c − h_r) = (2, 0) gives (3, 1), leaving the second corrupt component, 1, unchanged. This differs from replacing the entire vector with (3, 2).</figcaption>

</figure>

## 3. Clean-corrupt pairs

The two inputs should differ only in the target feature, with length, format, and difficulty matched as closely as possible. If corruption changes multiple kinds of information at once, what the patch restores becomes ambiguous. Calculate paired effects and uncertainty over multiple input pairs.

Check alignment at the positions produced by tokenization, not just by counting characters in the sentences. A word at the same location can split into multiple tokens in one input, and the same tensor index can refer to different contexts. Specify the source position that supplies the clean value and the destination position replaced in the corrupt run. Equal shapes alone do not establish a correspondence in meaning.

The following token arrays distinguish equal shapes from source and destination positions aligned in meaning.

<figure class="lesson-figure" markdown="1">

![Illustrative three-token clean sequence A B C and corrupt sequence A sub one A sub two B have the same shape but clean B at index two corresponds to corrupt B at index three rather than index two](../../figures/assets/I07/I07-07-source-destination-indices.svg)

<figcaption>This is an illustrative token split, not an actual tokenizer result. Both tensors have length 3, but B at clean index 2 corresponds to corrupt index 3. Exchanging index 2 mechanically would insert B at A₂, producing a different intervention.</figcaption>

</figure>

## 4. CPU lab

<!-- I07_EXAMPLE: i07_07_activation_patching -->

In this synthetic example, replacing the small MLP's entire hidden vector with its clean value gives recovery of 1. Because the entire vector is replaced, this result does not establish the role of any individual neuron.

The next hidden-coordinate plot shows how the full-vector replacement in the CPU lab affects the fixed readout.

<figure class="lesson-figure" markdown="1">

![CPU toy MLP hidden space shows corrupt tanh hidden near minus zero point eight five zero moved fully to clean hidden near zero point nine four zero point nine one then the same fixed linear readout yields the same clean and patched score](../../figures/assets/I07/I07-07-cpu-full-vector-patch.svg)

<figcaption>The plot uses the tanh(W_IN x) coordinates calculated in the existing CPU lab. Replacing the full hidden vector with the clean point makes the fixed W_OUT read the same vector, so the patched score equals the clean score. This result alone does not show which neuron is individually necessary.</figcaption>

</figure>

## 5. Experiment with the actual Pythia-160M model

Use `The capital of France is` and `The capital of Germany is` as the clean-corrupt pair, and patch the last-token output of the layer 5 MLP down-projection. The metric is the next-token logit for `Paris` minus that for `Berlin`.

<!-- GPU_EXPERIMENT: pythia_160m_activation_patching -->

In the fixed run, the clean metric was 5.0, the corrupt metric was -3.0, and the patched metric was -2.5, giving recovery of 0.0625. This small recovery shows that patching this single node changed only part of the contrast. It does not identify another layer or component as the circuit, nor does it establish that Pythia stores facts in the same way.

## Common misconceptions

### Misconception 1. The location with the highest recovery is the only place where the information is stored

The patch effect includes the downstream path, corruption, and metric. With distributed representations and redundant paths, multiple locations can show an effect.

### Misconception 2. Recovery of 0 means that the component is not used

The receiver may be unable to use the patched value, or another path may have been damaged at the same time. A null result also requires checks of statistical power and intervention validity.

## Exercises

### 1. Calculating recovery

Calculate recovery for $m_c=10,m_r=2,m_p=6$.

<details>
<summary>Show solution</summary>

$(6-2)/(10-2)=4/8=0.5$.

</details>

### 2. Overshoot

For $m_p=12$, explain why recovery exceeds 1.

<details>
<summary>Show solution</summary>

The patched run exceeds the clean metric of 10. The ratio is $(12-2)/8=1.25$; it should not be clipped as a calculation error.

</details>

### 3. Unstable denominator

Explain the problem that arises when $m_c$ and $m_r$ are almost equal.

<details>
<summary>Show solution</summary>

Even a small measurement error can change the recovery ratio substantially. First check whether the clean-corrupt contrast separates the behavior sufficiently, and report the raw difference as well.

</details>

### 4. Location specification

List three additional pieces of location information needed to specify "attention head 3 was patched."

<details>
<summary>Show solution</summary>

Specify the layer, token position, and whether the patch affects the head's value, output, or residual contribution. Also state whether it is before or after normalization and whether it replaces the entire vector.

</details>

### 5. Pythia result

Write one sentence stating what can be concluded directly from recovery of 0.0625.

<details>
<summary>Show solution</summary>

For the fixed France/Germany prompt pair, patching the last-token output of the layer 5 MLP recovered 6.25% of the clean-corrupt gap in the Paris–Berlin logit contrast.

</details>

### 6. Controls

Propose two controls for testing the specificity of the selected node patch.

<details>
<summary>Show solution</summary>

You can patch a random token in the same layer or use a norm-matched activation. A resampled control can also take the clean source from a different, unrelated prompt.

</details>

## Sources and update boundaries

The causal framework for interchange interventions follows [Geiger et al. (2021)](https://arxiv.org/abs/2106.02997), and the effects of metric and corruption choices follow [Zhang and Nanda (2023)](https://arxiv.org/abs/2309.16042). Actual-model results are restricted to the fixed Pythia revision and the scope of the local manifest.

## Lesson summary

- Activation patching is an interchange intervention that inserts clean values into a corrupt forward pass.
- Consider normalized recovery alongside the raw clean, corrupt, and patched metrics.
- Module, layer, token, coordinates, and normalization location determine the estimand.
- A single patch result provides local causal evidence for the specified input and metric.

## Pass criteria

- Can you define the three runs and calculate recovery?
- Can you write a complete patch-location specification?
- Can you limit the scope of claims made from the Pythia result?

## Next lesson

- [I07-08 Causal tracing](I07-08-causal-tracing.md)

## Author checklist

- [x] The learning objectives describe observable actions.
- [x] The clean, corrupt, and patched runs are distinguished.
- [x] The actual Pythia result and its scope are specified.
- [x] Every exercise has a solution.
- [x] Claim strengths in model interpretability are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No unannounced prerequisites are required.
- [x] Internal links and equation rendering have been checked.
