---
id: "I06-01"
title: "Designing behavioral and representation questions"
part: 3
stage: "I06"
status: "complete"
prerequisites:
  - "N05-25"
  - "M04-17"
estimated_time: "120–150 minutes"
---

# I06-01. Designing behavioral and representation questions

## Why this lesson matters

A model-interpretability experiment does not start by collecting activations. First specify which model behavior you want to explain, which internal quantity you will observe, and which comparison will connect them. Without these three decisions, you may collect large tensors and then attach explanations to conspicuous patterns.

This lesson divides a question into **the behavioral target, the internal target, and the comparison and claim**. This design is the common starting point for the probes, attribution methods, interventions, and circuit analyses introduced later.

## Learning objectives

- Express behavioral and representation questions using different measurements.
- Connect a claim, estimand, and measurement in one line.
- Specify the model, layer, token, component, and conditions to fix the internal target.
- Distinguish an observation unit from repeated measurements.
- Distinguish the strength of observational, recoverability, use, and causal claims.

## Prerequisite check

- Prerequisite lessons: [N05-25 Hooks and activation collection](../../part-2-neural-computation/N05/N05-25-hook-activation-collection.md), [M04-17 Experimental design and reproducibility](../../part-1-foundations/M04/M04-17-experimental-design-reproducibility.md)
- Check question: Can multiple token activations from the same sentence be counted as multiple independent samples?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $x_i$ | `input x sub i` | Input $i$ | token sequence |
| $b(x_i)$ | `b of x sub i` | Model behavior measured for the input | scalar or structured output |
| $a_{i,l,t}$ | `the activation for input i at layer l and token t` | Activation with the input, layer, and token fixed | $\mathbb R^d$ |
| $\Delta_b$ | `delta b` | Behavioral difference between two conditions | scalar or vector |
| estimand | `estimand` | Ideal target quantity required by the question | population quantity |
| measurement | `measurement` | Value actually recorded by the code | observed quantity |

## 1. Behavioral and representation questions

A behavioral question is defined between the model's inputs and outputs. Examples include the following.

- How much does the correct token's logit margin differ between factual and counterfactual sentences?
- Does classification accuracy remain unchanged when the prompt format changes?
- How much does the next-token probability change when a particular word is replaced?

Writing the behavioral value as $b(x)$, you can define the mean difference between conditions $C_1,C_0$ as

\[
\Delta_b=\mathbb E[b(X)\mid C_1]-\mathbb E[b(X)\mid C_0].
\]

Each expectation averages the same behavioral value $b$ over inputs belonging to that condition. Comparing the two conditions requires consistent definitions of the correct and alternative tokens, measurement position, and score. If input length and context also differ between conditions, their effects are mixed into $\Delta_b$. Subtracting conditional means alone does not isolate which factor changed the behavior.

A representation question includes an internal location. Even for the same input, changing layer $l$, token $t$, or component means observing a different tensor. Thus, `examine the intermediate representation` is not a question. At minimum, specify the following.

1. Model and checkpoint.
2. Module or component.
3. Layer index.
4. Rule for selecting the token position.
5. Input and control conditions.
6. Statistic to calculate from the activation.

Distinguish the internal observation and output measurement for the same prompt by their computation locations.

<figure class="lesson-figure" markdown="1">

![The same prompt is measured by an output logit margin and by a vector at a specified internal layer and token.](../../figures/assets/I06/I06-01-behavior-internal-measurements.svg)

<figcaption>Even with the same input, the behavioral value is computed at the output, while the representation value is read at a specified internal location. Retain each measurement definition when changing comparison conditions.</figcaption>
</figure>

## 2. Claim, estimand, and measurement

These three items are not interchangeable.

| Category | Example in this lesson |
|---|---|
| claim | The distribution of the layer 5 MLP update differs between place and animal contexts. |
| estimand | Difference between the means of the selected activation in the two input populations, $\mu_{place}-\mu_{animal}$ |
| measurement | Difference between sample means at the last token of eight fixed prompts |

For a measurement to approximate the estimand well, the input sample and measurement procedure must fit the question. Results from only eight sentences cannot be generalized to all languages, sentence formats, and checkpoints. Conversely, stating that an experiment is a narrow pilot makes even a small experiment useful for checking hook locations and analysis procedures.

The table's estimand selects only the mean difference from the full distributions. Different population means imply that the two distributions cannot be identical, but equal population means do not make the distributions identical. Variances or the proportions of values in different regions can differ. The sample-mean difference estimates this population-mean difference. To connect the result to the conclusion, narrow down which part of the distributional difference in the claim will be examined by the measurement.

Compare the selected pilot sample with the input populations from which it is drawn.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two input populations contain a selected four place and four animal prompts; population mean difference and sample mean difference are distinct targets.](../../figures/assets/I06/I06-01-population-pilot.svg)

<figcaption>The population-mean difference and the sample-mean difference from four selected prompts per condition are different quantities. Extending the pilot's sample result to a difference in the full distributions requires examining sample selection and measurement scope.</figcaption>
</figure>

## 3. Analysis units and repeated measurements

Measuring 12 layers and 20 tokens in one input sentence does not create 240 independent samples. Measurements from the same input share common causes. If the input is the experimental unit, layers and tokens are repeated measurements within it.

A paired design can first compute a difference for each input pair. Given an original $x_i$ and minimally modified control $x'_i$, calculate

\[
d_i=b(x_i)-b(x'_i)
\]

for each pair, then analyze the distribution of $d_i$. This partly offsets differences in difficulty across sentences.

Use the figures to distinguish repeated measurements within an input from differences within input pairs.

<figure class="lesson-figure" markdown="1">

![A single input encloses a layer by token measurement grid; its twelve layers and twenty tokens give 240 repeated measurements but one experimental unit.](../../figures/assets/I06/I06-01-repeated-measurements.svg)

<figcaption>The 240 measurements across 12 layers and 20 tokens are grouped within one input. Counting grid cells as independent inputs ignores within-sentence dependence.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![An original prompt and its minimally modified control produce two behavioral measurements whose difference is computed before pooling input pairs.](../../figures/assets/I06/I06-01-paired-inputs.svg)

<figcaption>First pair the original prompt with its minimally modified control and calculate the behavioral difference dᵢ. When analyzing multiple pairs, retain the relationship between the two measurements from each pair.</figcaption>
</figure>

## 4. Specifying an internal location by its computational meaning

A module name alone is insufficient. `MLP output` can mean the update before residual addition or the block output, which are different quantities. The path used in the Pythia experiment,

```text
gpt_neox.layers.0.mlp.dense_4h_to_h
```

is the down-projection output of the first block's MLP. At the last token, this output is the MLP update immediately before residual addition, not the entire residual stream.

Define the token from the tokenizer output, not from a position in the string. This lesson's smoke test tokenizes the prompt and selects the last real token indicated by the attention mask.

Check the computation location of the observed update separately from the token-selection rule.

<figure class="lesson-figure" markdown="1">

![A hook reads the MLP down projection output before its update is added to the previous residual stream, distinguishing the update from the block output.](../../figures/assets/I06/I06-01-update-versus-stream.svg)

<figcaption>The down-projection output read by the hook is the MLP update before addition. Adding it to the residual produces a different internal quantity. The actual block output also incorporates other updates in that structure.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An attention mask with real tokens followed by padding identifies the last one-valued mask position rather than the final array position for activation selection.](../../figures/assets/I06/I06-01-last-real-token.svg)

<figcaption>The last real token is the last position whose attention-mask value is 1. In an array with trailing padding, this can differ from selecting the final slot.</figcaption>
</figure>

## 5. A ladder of claims

Write model-interpretability conclusions according to their evidence level.

1. **Observation**: Activation statistics differed between two conditions.
2. **Recoverability**: Labels could be predicted from activations.
3. **Use**: There is evidence that the information is functionally used in the behavioral computation.
4. **Causality**: A controlled intervention changed the behavioral value.
5. **Generalization**: The result persisted across other inputs, seeds, checkpoints, or models.

A result at level 1 does not support a sentence at level 3 or 4. An activation difference shows the possibility of information being present in the representation, but does not guarantee that the model uses that difference in its output.

This list does not mean that every result must climb all five steps in sequence. Generalization can also be asked separately of an observational or recoverability result. Nor does identifying a component's effect through an intervention establish that the effect came from using particular label information. Match the claim to the computations connecting the observed quantity, recovered information, and intervention target.

Mark the path tested by each kind of evidence on the model computation.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A model representation connects to an observational statistic, an external label decoder, and an intervention on the model path; generalization evaluates these results on new conditions separately.](../../figures/assets/I06/I06-01-evidence-routes.svg)

<figcaption>Observational statistics, label recovery by an external decoder, and interventions on the model path test different computations. Generalization is the separate question of evaluating these results on other inputs, seeds, or checkpoints.</figcaption>
</figure>

## 6. Writing a one-line question specification

Complete the following sentence before the experiment.

> In `[model@revision]`, use `[input population and control conditions]` to measure `[behavioral value]` and `[internal quantity at a layer, token, and component]`, and estimate `[comparison quantity]` with `[analysis unit]` as the unit of analysis.

For example:

> In `pythia-160m-deduped@step143000`, use four place sentences and four animal sentences to measure the last-token prediction and layer 5 MLP update, and calculate the difference between conditional means with input sentences as the unit of analysis.

This sentence is narrow but executable. `Explore how the model understands the concept of place` specifies neither targets nor measurements, so it cannot be executed as written.

## Real-model lab

### Role of the 70M smoke test

The 70M experiment is not a sample for drawing an interpretability conclusion. It is an instrumentation check that the tokenizer, fixed revision, module path, hook calls, last-token selection, and manifest records agree.

<!-- GPU_EXPERIMENT: pythia_70m_smoke -->

The experiment retains only a selected vector of shape `(1, hidden_size)`, not all activations. Passing provides evidence that the runner works, not that a particular feature was discovered.

## Common misconceptions

### Misconception 1. Once interesting activations are found, the question can be chosen later

Exploratory analysis is possible, but distinguish hypotheses generated during exploration from confirmatory experiments. Creating a hypothesis from data and confirming it on the same data introduces selection bias.

### Misconception 2. More layers and tokens automatically mean more samples

They are repeated measurements from the same input. Define independence assumptions and analysis units from the data-generating process.

### Misconception 3. A correlation between an internal quantity and behavior means causation

Common input factors can make them change together. Causal claims require further controls, interventions, and tests of alternative explanations.

## Exercises

### 1. Decompose a question

List at least three items missing from `Check whether the model understands negation`.

<details><summary>Show solution</summary>Missing items include the behavioral value, input and control conditions, model and revision, internal component, layer, token rule, analysis unit, and comparison statistic. For example, narrow the question to measuring paired differences in the correct token's logit margin and the layer 6 last-token activation between original and negated sentences.</details>

### 2. Estimand and measurement

The estimand is the mean activation difference for all English place sentences, but only four sentences were measured. Are the two quantities the same?

<details><summary>Show solution</summary>No. The former is a target quantity for the input population, while the latter is a sample measurement from four selected sentences. State sample selection and uncertainty.</details>

### 3. Analysis unit

Twelve layers were measured in each of ten sentences. If sentences are the independent sampling units, can the independent sample count be set to 120?

<details><summary>Show solution</summary>No. Layer measurements repeat within the same sentence, so the basic independent units are the ten sentences. Even a model including layers must account for within-sentence dependence.</details>

### 4. Distinguish components

Can the `dense_4h_to_h` output and block output be called the same representation?

<details><summary>Show solution</summary>No. The former is the MLP update before residual addition; the latter is the block output incorporating the previous residual and multiple updates. They occupy different computation locations.</details>

### 5. Claim strength

Place and animal labels were recovered from activations with 90% accuracy. State the most directly supported claim.

<details><summary>Show solution</summary>The labels were recoverable from the activations under the specified sample and evaluation procedure. Without additional interventions, this does not establish that the model uses the information in its behavior or that the activations cause it.</details>

### 6. Interpreting a smoke test

The 70M hook experiment passed. Can this alone establish that the layer 0 MLP stores factual knowledge?

<details><summary>Show solution</summary>No. The smoke test checks instrumentation: model loading, tokenization, hook locations, and storage work. There is no estimand or controlled experiment about knowledge.</details>

## Sources and update boundaries

Pythia model IDs and checkpoint organization were checked on 2026-10-01 against the [official EleutherAI Pythia repository](https://github.com/EleutherAI/pythia) and [Pythia-70M-deduped model card](https://huggingface.co/EleutherAI/pythia-70m-deduped). Hook call contracts follow the [PyTorch `nn.Module` documentation](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html). Module paths and library APIs are version-specific implementation details; the distinctions among behavior, representation, and analysis units do not depend on a particular library.

## Lesson summary

- Behavioral questions require output measurements; representation questions require internal model locations and statistics.
- Distinguishing claims, estimands, and measurements clarifies the scope of sample results.
- Layers and tokens can be repeated measurements within the same input.
- Observation, recoverability, use, causality, and generalization are claims of different strengths.
- Passing a smoke test supports the instrumentation procedure, not an interpretability conclusion.

## Pass criteria

- Can you decompose an interpretability question into a behavioral value and an internal quantity?
- Can you explain the difference between an estimand and an actual measurement?
- Can you specify the model, layer, token, component, and analysis unit?
- Can you write a conclusion of the appropriate strength for an observation?

## Next lesson

- [I06-02 Activation dataset](I06-02-activation-dataset.md)

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] Behavioral and representation questions are connected to claims, estimands, and measurements.
- [x] Experimental units and repeated measurements are distinguished.
- [x] Modules, layers, and tokens in the real-model experiment are specified.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretability claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Knowledge beyond the prerequisites is not required without explanation.
- [x] Internal links and equation rendering are checked.
