---
id: "N05-25"
title: "Hooks and activation collection"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-24"
estimated_time: "120–150 minutes"
---

# N05-25. Hooks and activation collection

## Why this lesson matters

White-box analysis starts by collecting the desired module's activations at the correct layer, token, and component. A hook allows intermediate outputs to be observed without rewriting the existing forward code. However, unspecified locations, lifetimes, gradient behavior, and storage amounts can lead to collecting the wrong tensors.

## Learning objectives

- Explain when a forward hook is called.
- Collect activations by specifying a module path, layer, and token index.
- Distinguish the purposes of `detach`, `clone`, and device transfer.
- Remove a hook handle and verify removal through the call count.
- Record activation shapes, dtypes, byte counts, and provenance.

## Prerequisite check

- Prerequisite lesson: [N05-24 The observational status of Chain-of-thought](N05-24-chain-of-thought-observation-status.md)
- Check question: Can you specify the computational site of the desired activation, distinguishing the residual stream, attention update, and MLP update?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| forward hook | `forward hook` | Callback invoked after a module's forward computation produces an output | Runtime callback |
| module path | `module path` | Name identifying a target module within a model | String |
| $a_{l,t}$ | `the activation at layer l and token t` | Activation vector at a specified layer and token | $\mathbb R^d$ |
| detach | `detach` | Operation separating a tensor from the current autograd graph | Tensor operation |
| handle | `hook handle` | Object used to remove a registered hook later | Removable handle |
| provenance | `provenance` | Record of an activation's model, input, location, and conditions | Metadata |

## Core concept 1. The forward-hook contract

A PyTorch module-specific forward hook is called after that module's `forward()` computes its output. The default callback receives the module, a tuple of positional inputs, and the output. Because returning a value can change the output, an observation-only hook returns nothing.

A hook attaches to a module object. It does not automatically attach to other instances of the same class. If a shared module is called repeatedly, its hook can run several times within one forward pass.

Separate the timing of an observation-only hook from the site of residual addition.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A forward hook records a toy MLP down update after it is computed and returns None before the unchanged update is added to the residual stream](../../figures/assets/N05/N05-25-hook-before-addition.svg)

<figcaption>In this small vector example, the hook observes the computed update u=(0.5,0.5). Returning None preserves u; adding it to residual r=(1,−1) produces stream (1.5,−0.5). The down output and the block output after addition are not the same observation.</figcaption>
</figure>

## Core concept 2. Storing only the needed activations

If the output has shape $(B,T,d)$ and only token $t$ from batch 0 is needed, store only

\[
a_t=\text{output}[0,t,:]
\]

A float32 vector requires $4d$ bytes. Storing every batch, sequence, and layer indiscriminately uses disk space and memory unrelated to the experimental question.

Use an array filled with consecutive numbers to identify the selected row and the features retained.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A batch one four token four feature array selects token row two and all four feature entries instead of storing the complete tensor](../../figures/assets/N05/N05-25-token-slice-storage.svg)

<figcaption>Selecting row t=2 from batch 0 retains all features 0, 1, 2, and 3. The full float32 tensor of shape (1,4,4) uses 64 bytes; the selected vector of shape (4,) uses 16 bytes. The numbers 0 through 15 illustrate the slice and are not actual model activations.</figcaption>
</figure>

An observation copy is commonly made with `output[...].detach().cpu().clone()`. The `detach` operation breaks the graph connection, `cpu` moves the tensor out of accelerator memory, and `clone` creates a copy independent of later storage changes.

These operations are not interchangeable. A tensor processed with `detach` shares storage with the original tensor, so the absence of a gradient connection does not protect the stored values from later changes. For a tensor already on the CPU, `cpu()` does not make a new copy. The final `clone()` copies the selected values into separate storage, preserving the observation at that moment. In contrast, `clone()` alone can copy the values while leaving the autograd connection intact.

Compare what happens when the storage of a tensor already on the CPU changes later.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A detached CPU tensor shares storage with its original while a clone made after detaching keeps an independent snapshot when the original storage later changes](../../figures/assets/N05/N05-25-detach-clone-storage.svg)

<figcaption>Breaking only the graph connection from storage A, initially containing (1,2), leaves the storage shared. If A's first value later becomes 9, the detached values also become (9,2). Storage B, cloned beforehand, keeps (1,2). This example explains storage sharing; it is not a procedure for modifying model activations in the lab.</figcaption>
</figure>

The detached copy is a record for analyzing values. It cannot be used to compute gradients back to the original activation. The next lesson's gradient collection distinguishes the original graph-connected activation from its recording copy.

## Core concept 3. Lifetime and provenance

Unless `remove()` is called on the handle returned at registration, the hook remains active in later forward passes. Record the following for each experiment:

- Model ID, revision, and weight hash
- Module path, layer, token, and component meaning
- Input IDs, attention mask, and positions
- Train/eval mode, dtype, device, and gradient mode
- Activation shape, dtype, byte count, and transformations used for storage
- Hook call count and whether the hook was removed

A module path identifies the observed object but does not identify which result among multiple calls was recorded. Reusing a shared module twice or calling the same module at several generation steps accumulates different activations under the same path. Call order and the corresponding inputs must therefore be recorded together to recover the meaning of the layer and token. In a cache-using step with an output of length 1, local token index 0 refers to the token currently processed, not the first token of the entire prefix.

Even the same path and local index refer to different tokens when the calls occur at different steps.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two decode calls use the same module path and local token index zero but refer to token IDs seven and nine at prefix positions three and four](../../figures/assets/N05/N05-25-call-token-provenance.svg)

<figcaption>The two example decode calls produce shape (1,1,4) at the same path but have different token IDs and cumulative positions. Local index 0 alone does not identify the first token of the prompt. Record call order together with the input token.</figcaption>
</figure>

## Example

The lab attaches a hook to `blocks.0.mlp.down` and stores only the four entries of the vector at token index 2 from an output of shape `(1,4,4)`. In float32, this requires $4\times4=16$ bytes. After removing the hook, the same forward pass runs again to check that the call count remains at 1 and the logits remain unchanged.

Track the callback count through registration, invocation, and removal.

<figure class="lesson-figure" markdown="1">

![A registered forward hook is called once on the first forward then removed so a second forward leaves its call count at one](../../figures/assets/N05/N05-25-hook-lifetime.svg)

<figcaption>The callback count is 1 after the first forward pass. After removing its handle, the second forward pass should not increase this callback's count. Because the hook is observation-only, logit invariance is checked as well.</figcaption>
</figure>

## Hands-on lab

### Environment and source files

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Checked on: 2026-10-01
- Component classification: PyTorch-specific observation API
- Shared implementation: `labs/N05/tiny_decoder.py`
- Example ID: `n05_25_activation_hook`
- Code source: `labs/N05/n05_25_activation_hook.py`
- Tests: `tests/N05/test_n05_25.py`
- Run command: `.venv\Scripts\python.exe -m labs.N05.n05_25_activation_hook`

### Resource budget

The lab runs two forward passes with sequence length 4 on a model with 300 parameters and selects just 16 bytes of activations. Nothing is saved to disk.

### Actual code and execution results

<!-- N05_EXAMPLE: n05_25_activation_hook -->

### Checks

The tests check the full hook-output shape, the selected activation's shape, byte count, and gradient state, output invariance, and the call count after handle removal.

## Verifying a hook site

Do not rely only on a module's name; inspect the input and output shapes and the computation graph. An MLP's `down` output is an update before addition to the residual stream, while the entire block's output is the stream after addition. If an attention module returns a tuple, its hook output may also be a tuple.

Where possible, compare the hooked tensor against a manual forward calculation or trace on a small deterministic input. If a module is fused or compiled, check separately whether the expected Python hooks are preserved.

## Connection to model interpretability

Activation collection is observation. Predicting a class label from an activation, or finding a correlation with a direction, does not establish that the model uses that information in its behavior. Later lessons combine gradients and interventions.

Record token indices using the tokenizer's output and special tokens. The `third word` in a string and token index 2 in a tensor do not always refer to the same object.

## Common misconceptions

### Misconception 1. Attaching a hook automatically leaves the output unchanged

A callback can change the output by returning an output value. An observation-only hook avoids return values and in-place mutations and checks output invariance.

### Misconception 2. `detach` deletes the original model tensor

It breaks the collected copy's autograd connection; it does not remove the model's forward tensor itself.

### Misconception 3. Every layer and token must be stored for later analysis

First specify the slices and statistics needed for the question to control resources and multiple comparisons.

## Exercises

### 1. Byte count

Calculate the number of bytes for one token's float32 activation vector of dimension 768.

<details><summary>Show solution</summary>It requires $768\times4=3{,}072$ bytes.</details>

### 2. Hook timing

Determine whether a forward hook is normally called before or after the module output is computed.

<details><summary>Show solution</summary>After the output is computed. A forward pre-hook is used before computation.</details>

### 3. Call count

Determine how many times a hook can be called if the same hooked module is reused twice within one forward pass.

<details><summary>Show solution</summary>It can be called twice. Because it runs at each module invocation, the count must be checked.</details>

### 4. Detaching

Explain what to do when storing activations for analysis over a long period without retaining the entire backward graph.

<details><summary>Show solution</summary>Apply `detach` to the needed slice, move it to the CPU if needed, and clone it.</details>

### 5. Distinguishing sites

Determine whether an MLP down-projection output is the same as the block output after residual addition.

<details><summary>Show solution</summary>No. The former is an update to add to the stream; the latter is the sum of the previous stream and the update.</details>

### 6. Scope of the claim

Part-of-speech labels are recovered with 95% accuracy from activations collected by a hook. Determine whether this establishes that the model uses parts of speech.

<details><summary>Show solution</summary>This is evidence of recoverable information. Establishing functional use in behavior requires additional checks, such as control probes and interventions.</details>

## Sources and update boundaries

Hook timing, output changes through return values, and the removable-handle contract were checked against the [official PyTorch `nn.Module` documentation](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html). Module paths, compiled execution, and fused components are implementation details specific to model and framework versions.

## Lesson summary

- A forward hook runs after the target module computes its output.
- Specify the layer, token, and component to store only the needed activations.
- Detaching, CPU transfer, and cloning serve different purposes.
- Remove the handle and check the call count and output invariance.
- Observing an activation is not sufficient evidence of information use or causal contribution.

## Pass criteria

- Can you explain the hook's invocation contract?
- Can you collect an activation at a specified token?
- Can you distinguish detaching, cloning, and device transfer?
- Can you verify handle removal?
- Can you record provenance and byte counts?

## Next lesson

- [N05-26 Gradient collection and preparation for interventions](N05-26-gradient-collection-intervention-preparation.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Hook location, lifetime, storage amount, and provenance are connected.
- [x] Every exercise has a solution.
- [x] Model interpretability claims are distinguished by strength of evidence.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and mathematical rendering have been checked.
- [x] Executable code has not been manually duplicated in Markdown.
- [x] Code sources, test paths, resource budgets, and the check date are recorded.
- [x] Hook shape, lifecycle, and output-invariance tests are provided.
