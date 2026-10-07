---
id: "I06-02"
title: "Activation dataset"
part: 3
stage: "I06"
status: "complete"
prerequisites:
  - "I06-01"
estimated_time: "120–150 minutes"
---

# I06-02. Activation dataset

## Why this lesson matters

Collecting only activation vectors makes it easy to lose track of the inputs, models, layers, and tokens that produced them. An activation dataset pairs tensors with their measurement conditions in the same rows. This structure allows conditional statistics, probes, and intervention candidates to be reproduced.

This lesson treats one input as the basic observation unit and builds a minimal schema connecting input metadata to selected activations. It does not create a dump of all layers and tokens.

## Learning objectives

- Define what one row of an activation dataset represents.
- Record the input, model revision, module, layer, token, and condition label together.
- Verify the token-selection rule using tokenizer output.
- Set splits and analysis plans before collection to reduce leakage.
- Calculate artifact size and store only the necessary slices.

## Prerequisite check

- Prerequisite lesson: [I06-01 Designing behavioral and representation questions](I06-01-behavior-representation-question-design.md)
- Check question: Are `the last word` and `the last token` always the same?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $D_A$ | `activation dataset D sub A` | Dataset pairing activations with measurement metadata | $n$ rows |
| $a_i$ | `activation a sub i` | Activation selected from input $i$ | $\mathbb R^d$ |
| $c_i$ | `condition c sub i` | Predefined condition of input $i$ | finite label set |
| $t_i$ | `token index t sub i` | Position selected from tokenizer output | $0,\ldots,T_i-1$ |
| provenance | `provenance` | Record of the model, input, code, and location that produced a value | metadata |
| leakage | `data leakage` | Evaluation information entering training or selection | design failure |

## 1. One row of the dataset

For a fixed model and hook location, write the activation dataset as

\[
D_A=\{(i,x_i,c_i,l,t_i,a_i)\}_{i=1}^{n},
\qquad a_i\in\mathbb R^d.
\]

Actual rows require more provenance than this equation shows.

| Field | Example | Reason |
|---|---|---|
| `sample_id` | `place-01` | Reconnects the input and activation. |
| `text` or input hash | Prompt or SHA-256 | Identifies the exact input. |
| `condition` | `place` | Defines comparison groups in advance. |
| `model_id` | `EleutherAI/pythia-160m-deduped` | Fixes the weight family. |
| `resolved_sha` | immutable commit SHA | Prevents changes associated with a branch name. |
| `module` | `gpt_neox.layers.5.mlp.dense_4h_to_h` | Fixes the computation location. |
| `token_index` | `6` | Records the selected tensor position. |
| `token_id` | tokenizer output | Verifies string-token alignment. |
| `activation` | A vector of length 768 | Is the analysis target. |
| `dtype` | `float32` artifact | Records storage precision. |

Values shared across the dataset must still be recorded at least once in the manifest. Repeating them in each row or storing them in a separate table is a storage-format choice.

Converting the equation to a matrix produces an $n\times d$ activation array. Row index $i$ refers to an input, and columns refer to coordinates in the same internal space. Reordering rows requires reordering conditions and sample IDs together. Even if the vector values remain unchanged, changing their correspondence to labels produces different analysis data. Token indices $t_i$ can differ by input, but if they were selected using the same rule, such as the last real token, that rule defines what comparisons across rows mean.

Placing matrix rows and metadata at matching heights shows what must be aligned together.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Eight input rows keep sample identifiers, condition labels, and activation coordinates aligned in an eight by 768 matrix.](../../figures/assets/I06/I06-02-row-metadata-alignment.svg)

<figcaption>Each row of the 8×768 activation array corresponds to one input. Moving a row requires moving its sample ID and condition with it to retain the same observations.</figcaption>
</figure>

## 2. Fixing inputs and conditions first

Do not assign condition labels after examining activations. For example, when comparing four place sentences with four animal sentences, fix the sentence list, labels, and exclusion criteria before collection. If sentence length, grammatical structure, and the last token also differ by condition, it is difficult to isolate whether activation differences reflect meaning or form.

For paired inputs, match sentence form as far as possible except for the factor being compared. The following sentences provide concrete animal and place conditions.

```text
The animal near the river is a salmon.
The city near the river is Berlin.
```

Equal word counts do not necessarily give equal tokenizer token counts, however. Record the actual tokenization results.

The two sentences differ not only in their subjects but also in the final names and articles. They are therefore not a completely matched pair changing only one semantic condition. Pairing two inputs and controlling differences outside the condition are separate judgments. Record factors that change together across conditions to define the interpretation scope of activation differences.

Mark the parts that change together in the two inputs to check the comparison conditions.

<figure class="lesson-figure" markdown="1">

![The paired animal and city sentences differ in the subject, article, and final name; pairing alone does not isolate a single semantic change.](../../figures/assets/I06/I06-02-paired-versus-matched.svg)

<figcaption>Pairing the sentences does not remove their differences in animal/city, final name, and article. Do not confuse the colored and underlined differences with the effect of one condition.</figcaption>
</figure>

## 3. Fixing the layer, token, and component

Exploring multiple locations in the same input rapidly increases the number of comparisons. In a confirmatory experiment, use one of the following approaches.

- Fix the layer and component in advance using theory or prior findings.
- Select a location on an exploration split and evaluate on a separate confirmation split.
- When reporting all locations, disclose multiple comparisons and the selection procedure together.

To select the last token, calculate the last valid position in the attention mask, rather than using the string's last whitespace boundary. With padding, the tensor's last column may differ from the last real token.

Subtracting 1 from the valid-token count works when tokens are contiguous from the beginning and padding is appended at the end. With left padding or other layouts, the valid count does not identify the tensor index. Define the rule as the last index whose attention-mask value is 1, and also check the token ID at that position.

Examine padding locations separately from the separation of exploration and confirmation.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Right-padded and left-padded masks have three valid tokens but different last valid indices; selection uses the last one-valued mask index.](../../figures/assets/I06/I06-02-padding-index-rules.svg)

<figcaption>Two masks with the same valid-token count can have different last valid indices. Only with right padding can count−1 be used directly as the index.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![An exploration split selects a layer and component, after which a disjoint confirmation split evaluates the fixed selection without feeding back into it.](../../figures/assets/I06/I06-02-explore-confirm-split.svg)

<figcaption>Select a location on the exploration split, then evaluate on a separate confirmation split. Using the confirmation result to select the location again removes the separation between the two stages.</figcaption>
</figure>

## 4. Gradients and storage lifetime during collection

For observation alone, `detach` the required slice and move it to the CPU. In an experiment requiring gradients, retain the hook output's connection to the selected target. Mixing these purposes in the same collection loop can retain unnecessary graphs for too long.

This project's 160M experiment calculates a selected activation gradient only for the first input. It replaces the hook output with a detached leaf at that location and computes only the downstream gradient, creating neither model-parameter gradients nor optimizer state. The remaining seven inputs are collected under `no_grad`.

This leaf passes the same values as the original output downstream, but serves as a differentiation variable disconnected from the earlier computation graph. Its gradient thus describes how a small change in that internal quantity changes the selected target with the weights and input fixed. Its target differs from a gradient traced back to the original token embedding or upstream parameters. Unlike a detached copy stored only for observation, this leaf must actually participate in the downstream computation.

Compare the connections of a storage copy and a downstream differentiation variable.

<figure class="lesson-figure" markdown="1">

![An observed activation is detached and copied to a CPU artifact; the stored copy has no upstream gradient path.](../../figures/assets/I06/I06-02-detach-observation.svg)

<figcaption>The observation copy is detached and stored on the CPU. Its storage lifetime is separated from the lifetime of the forward computation graph.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A same-valued detached leaf activation participates in the downstream model; a target gradient returns to that leaf but stops before upstream parameters.](../../figures/assets/I06/I06-02-downstream-leaf-gradient.svg)

<figcaption>The leaf passes the same values as the original activation downstream. The gradient returning from the target ends at this leaf, so its target differs from upstream-parameter gradients.</figcaption>
</figure>

## 5. Calculating storage size

Storing one $d$-dimensional float32 activation for each of $n$ inputs gives a raw array size of

\[
4nd\ \text{bytes}
\]

For $n=8$, $d=768$, this is

\[
4\times8\times768=24{,}576\ \text{bytes}
\]

A compressed artifact adds metadata but can be smaller than the raw size when values repeat.

In contrast, storing all 12 layers and 128 tokens creates $12\times128=1{,}536$ times as many coordinates. If the question concerns one location, this increase is not information but unnecessary storage and opportunities for selection.

Compare the number of arrays at one location with the number across all layers and tokens.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A selected eight by 768 activation slab is contrasted with twelve layers times 128 token slabs, showing a 1536-fold storage multiplier.](../../figures/assets/I06/I06-02-selected-slice-storage.svg)

<figcaption>An 8×768 float32 array at one location occupies 24,576 bytes. Storing the same-sized array at each of 12 layers and 128 token positions multiplies the coordinate count by 1,536.</figcaption>
</figure>

## 6. Splits and leakage

If you plan to train a probe, define the units for train, validation, and test splits before collecting activations. Paraphrases from the same original input placed in different splits can leak sentence content. Randomly splitting token rows also creates leakage when different tokens from the same sentence appear on both sides.

With group IDs, split by original input, document, speaker, or generation template. Selecting a layer from test activations and reporting final performance on the same test means that the test was used for model selection.

Check whether variants sharing an original input cross split boundaries.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Paraphrases from one source input leak when divided across train and test, whereas grouping keeps all variants together and tests on another input group.](../../figures/assets/I06/I06-02-group-split-leakage.svg)

<figcaption>On the left, variants from the same original input are split between train and test, creating content overlap. On the right, the original-input group stays together, and evaluation uses another group.</figcaption>
</figure>

## Real-model lab

### Fixed collection contract

This experiment collects one last-real-token activation from the layer 5 MLP down-projection output in Pythia 160M. Inputs are four place sentences and four animal sentences fixed in advance. The artifact contains only an 8×768 activation array and a gradient of length 768 for the first input.

<!-- GPU_EXPERIMENT: pythia_160m_activation_dataset -->

The local result's `sample_count`, `activation_shape`, `hook_calls`, and `sequence_lengths` check the collection contract. `condition_mean_difference_l2` is only a descriptive statistic showing a difference between two sample means, not proof of a condition's causal effect or concept use.

## Quality checks

Check the following immediately after collection.

1. Does the row count equal the input count?
2. Does the hook call count equal the expected number of forward passes?
3. Does each activation have shape $(d,)$, with all values finite?
4. Is the token index within the valid length of each input?
5. Do the model and tokenizer use the same repository and resolved SHA?
6. Are the artifact hash and byte count recorded in the manifest?
7. Was the hook handle removed?

Plausible value magnitudes alone do not detect a wrong module or token. Check shape, location, and provenance together.

## Common misconceptions

### Misconception 1. An activation array alone is a dataset

Without metadata reconnecting inputs and locations, you cannot tell which question the values measure. Preserve the array and provenance together.

### Misconception 2. Storing all activations is safer for later analysis

A full dump increases resource use and facilitates post-hoc selection. First specifying the layer, token, and component needed for the question makes the procedure verifiable.

### Misconception 3. It is enough not to use the test split to train the probe

Using test activations to select a layer, preprocessing, or hyperparameters also uses test information.

## Exercises

### 1. Minimal schema

Only activation vectors and condition labels were stored. List the additional essential provenance needed.

<details><summary>Show solution</summary>Record the input or input hash, model ID and resolved revision, tokenizer, module path, layer, token index and ID, dtype, code, and execution environment. These allow the same values to be collected again and their computation locations to be interpreted.</details>

### 2. Storage size

Calculate the raw size of one 1,024-dimensional float32 vector for each of 100 inputs.

<details><summary>Show solution</summary>It is $4\times100\times1{,}024=409{,}600$ bytes, approximately 0.391 MiB. File-format metadata is additional.</details>

### 3. Token selection

What problem can arise from using `output[:, -1, :]` in a batch with padding?

<details><summary>Show solution</summary>For a short input, the last column may be a padding position. Calculate each input's last-real-token index using its valid length from the attention mask.</details>

### 4. Leakage

Twenty token activations from one sentence were randomly divided between train and test. Explain the problem.

<details><summary>Show solution</summary>Tokens sharing the same sentence content and context enter both splits. This does not evaluate generalization to independent inputs, so split by sentence or a higher-level group.</details>

### 5. Hook calls

Eight inputs each received one forward pass, but the hook was called 16 times. Can analysis proceed immediately?

<details><summary>Show solution</summary>No. Investigate shared-module reuse, duplicate hook registration, or an unexpected forward path. Until the call contract matches, the correspondence between rows and inputs is uncertain.</details>

### 6. Condition difference

The distance between the place and animal activation means was 8.4. State what can be concluded.

<details><summary>Show solution</summary>You can describe the two sample means as differing by that distance for the fixed sample and measurement location. Statistical stability, confounding control, recoverability, and functional use have not yet been checked.</details>

## Sources and update boundaries

Using the same model and tokenizer revision and the Pythia checkpoints follow the [official Pythia repository](https://github.com/EleutherAI/pythia). Tokenizer and model-loading arguments were checked against the [official Transformers documentation](https://huggingface.co/docs/transformers/index), and hook tensor lifetimes against the [official PyTorch documentation](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html), on 2026-10-01. Specific module paths depend on Pythia and Transformers versions, while row observation units and split principles do not depend on the model type.

## Lesson summary

- An activation dataset preserves selected vectors together with input, location, and execution provenance.
- Define conditions, splits, layers, and token rules before examining activations.
- Distinguish the last part of a string from the last tokenizer token.
- Store only the required slices and check byte counts and hashes through the manifest.
- Conditional mean differences are descriptive statistics, not functional use or causal effects.

## Pass criteria

- Can you design one activation-dataset row and shared metadata?
- Can you verify the target token in tokenizer output?
- Can you explain split leakage at the input-group level?
- Can you calculate the difference between selected-slice storage and a full dump?

## Next lesson

- [I06-03 Distributions and basic statistics](I06-03-distributions-basic-statistics.md)

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] A schema for inputs, conditions, models, layers, tokens, and components is defined.
- [x] Splits and leakage are connected to analysis units.
- [x] Storage size and artifact quotas are calculated.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretability claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Knowledge beyond the prerequisites is not required without explanation.
- [x] Internal links and equation rendering are checked.
