---
id: "N05-27"
title: "Checkpoints and model state"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-26"
estimated_time: "120–150 minutes"
---

# N05-27. Checkpoints and model state

## Why this lesson matters

A checkpoint is more than a weight file. The model state needed to reproduce inference differs from the optimizer, scheduler, step, and random state needed to continue training. Specifying the wrong checkpoint for analysis can mean comparing different training points even under the same model name.

## Learning objectives

- Distinguish parameters, persistent buffers, and optimizer state.
- List the requirements for an inference checkpoint and a resumable training checkpoint.
- Load a `state_dict` strictly and check key mismatches.
- Record the checkpoint step and model revision in analysis provenance.
- Explain controls for training data, seeds, and architecture when comparing checkpoints.

## Prerequisite check

- Prerequisite lesson: [N05-26 Gradient collection and preparation for interventions](N05-26-gradient-collection-intervention-preparation.md)
- Check question: What computations use model parameters and AdamW's moment estimates, respectively?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| parameter | `parameter` | Module tensor learned through gradient updates | Model state |
| persistent buffer | `persistent buffer` | Tensor saved in a `state_dict` that is not a learned parameter | Module state |
| optimizer state | `optimizer state` | State needed for the next update, such as moments and steps | Training state |
| checkpoint | `checkpoint` | Artifact bundling items needed to reproduce a specific training point | Serialized state |
| revision | `revision` | Repository ref or commit identifying a particular checkpoint | Identifier |
| strict load | `strict load` | Loading that requires an exact match between expected and loaded keys | Validation rule |

## Core concept 1. Model state

A PyTorch module's `state_dict` contains parameters and persistent buffers. Parameters are learning targets updated by the optimizer, while buffers are nonparameter tensors that affect forward state, such as running statistics.

Distinguish the two kinds of tensors saved by the model from the slots stored separately by the optimizer.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The model state dictionary contains parameters and persistent buffers while a separate optimizer state dictionary holds step and first and second moment slots](../../figures/assets/N05/N05-27-state-dictionaries.svg)

<figcaption>The tiny decoder's model state contains 12 parameter tensors and 0 persistent buffers. After a step, the optimizer stores each parameter's step, exp_avg, and exp_avg_sq in a separate dictionary. Do not generalize the buffer count of 0 to other architectures.</figcaption>
</figure>

The instructional tiny decoder has 12 parameter tensors and 0 persistent buffers. Here, 12 counts named tensor entries, while summing the elements in all those tensors gives 300 learned scalars. Other architectures may register positional tables, running statistics, or masks as buffers, so do not assume their counts.

Counting the elements in each tensor's shape in the lab implementation shows how the two counts differ.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Twelve named parameter tensors in the tiny decoder have different shapes whose scalar element counts sum to three hundred](../../figures/assets/N05/N05-27-tensor-scalar-inventory.svg)

<figcaption>Each box is one named tensor entry. For example, the embedding shape 16×4 is one entry containing 64 scalars. The four attention weights, three MLP weights, three norm vectors, embedding, and unembedding together give 12 entries and 300 scalars.</figcaption>
</figure>

A `state_dict` associates these names with tensors to determine where they are loaded. Calling `state_dict()` does not, however, immediately create an independent checkpoint copy. Its returned tensors can reference the model's storage, so continuing training while keeping only that dictionary in memory can change the values intended for saving. The lab makes a deep copy of the state to separate values at the selected step from later updates.

Compare a copy fixed at the selected step with a reference that follows later updates.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A deep copied checkpoint keeps a toy weight value one at saved step k while the live model storage changes to two at step k plus one](../../figures/assets/N05/N05-27-step-snapshot.svg)

<figcaption>Suppose an example weight is 1 at step k and later becomes 2. An independently copied snapshot keeps the intended value 1 from step k. Keeping only a dictionary referencing live storage may instead expose the later value 2.</figcaption>
</figure>

## Core concept 2. State for resuming training

Parameters alone are insufficient to continue AdamW from the same update. A checkpoint commonly includes:

- Model `state_dict`
- Optimizer `state_dict`
- Scheduler and mixed-precision scaler state
- Global step, epoch, and data position
- Random number generator state
- Model configuration, tokenizer, and code revision

Reproducing inference alone may not require optimizer state. In contrast, omitting these items can change the result when analyzing a training trajectory or resuming it exactly.

AdamW's next update depends on moments formed from past gradients and the accumulated step count, not only the current gradient. Even with identical weights, restarting moments at 0 can produce a different update from continued training. The scheduler determines the next learning rate, while the data position determines the input for the next gradient computation. RNG state preserves the current position in a random sequence, which differs from specifying the original seed again. Exact resumption continues the state needed for the next computation; it does not start new training from the same weights.

The dependencies entering the next step show why weights alone are insufficient.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Model weights optimizer moments and step schedule and data position and random draw state separately feed the next training computation](../../figures/assets/N05/N05-27-resume-dependencies.svg)

<figcaption>The four paths represent different states needed for the next computation. Identical weights can lead to different subsequent computations when moments, learning rates, the next batch, or the random sequence position differ. The requirement for optimizer state differs between reproducing fixed inference and resuming training exactly.</figcaption>
</figure>

## Core concept 3. Validating a load

The call `load_state_dict(..., strict=True)` checks that loaded keys exactly match the keys expected by the model. Ignoring missing or unexpected keys can leave some parameters at fresh initial values.

If the same state is loaded into the same architecture and configuration, with matching forward conditions such as input, eval mode, and dtype, the outputs should agree within a specified tolerance. Check forward equivalence as well as key agreement.

Key checks verify which names receive tensors, but do not prove that the forward code using those names is the same. Even when weights of the same shapes are loaded, different residual ordering or normalization computations give a different function. Loading state also does not set evaluation mode, so the lab applies `eval()` separately to the original and reloaded models before comparing them. Output agreement on a few inputs checks the loading procedure; it does not prove functional equality for all inputs.

Perform the key-mismatch check and forward-output comparison separately.

<figure class="lesson-figure" markdown="1">

![A strict load rejects missing key B and unexpected key C before a separate matched condition numerical forward check can be performed](../../figures/assets/N05/N05-27-load-checks.svg)

<figcaption>The key names A, B, and C illustrate a mismatch. If expected B is missing and C is added, resolve the strict-load issue before analysis. Even when keys and shapes match, compare outputs separately under the same configuration, forward code, inputs, eval mode, and dtype.</figcaption>
</figure>

## Example

After one AdamW step, the lab copies model and optimizer state in memory. There are 12 model parameter entries and 0 buffers, and the optimizer has `step`, `exp_avg`, and `exp_avg_sq` for each of the 12 parameters. After strict loading into a new model, the maximum logit difference is 0.

## Hands-on lab

### Environment and source files

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Checked on: 2026-10-01
- Component classification: PyTorch-specific serialization contract
- Shared implementation: `labs/N05/tiny_decoder.py`
- Example ID: `n05_27_checkpoint_state`
- Code source: `labs/N05/n05_27_checkpoint_state.py`
- Tests: `tests/N05/test_n05_27.py`
- Run command: `.venv\Scripts\python.exe -m labs.N05.n05_27_checkpoint_state`

### Resource budget

The lab runs only one training step with batch size 1 and sequence length 4 on a model with 300 parameters. No checkpoint file is written to disk.

### Actual code and execution results

<!-- N05_EXAMPLE: n05_27_checkpoint_state -->

### Checks

The tests check the model-state key count, parameter and buffer counts, strict-loading results, agreement of reloaded logits, and optimizer slots and steps.

## Reading Pythia checkpoints

The Pythia main suite publishes initialization at step 0, closely spaced early checkpoints, and later checkpoints at 1,000-step intervals. The official repository states that final `step143000` corresponds to `main` in each model repository. For analysis, record the requested revision and resolved commit SHA rather than only the model ID.

Do not mix the `v0` series with the revised main suite: their training setups differ. Pin the model and tokenizer to the same repository and revision contract as well.

## Connection to model interpretability

Activation differences between checkpoints are associated with changes during training, but the effect of step alone cannot be isolated if data order, optimizer state, seed, and code also differ. Even for a suite such as Pythia that provides a common data order and multiple checkpoints, specify the comparison question and metric in advance.

The same neuron index across checkpoints does not guarantee the same feature. Measure representation alignment and function-level behavior separately.

## Common misconceptions

### Misconception 1. A `state_dict` contains only parameters

It also contains persistent buffers. Optimizer state is held in the optimizer's separate `state_dict`.

### Misconception 2. Loading weights is enough to resume training exactly

Without optimizer moments, scheduler, step, RNG state, and data position, the update trajectory can change.

### Misconception 3. The same model name identifies the same checkpoint

Revisions, commits, and training steps can differ.

## Exercises

### 1. Classification

Classify AdamW's `exp_avg` as a model parameter, buffer, or optimizer state.

<details><summary>Show solution</summary>It is optimizer state, used in calculating the next update.</details>

### 2. Buffers

Determine whether a BatchNorm running mean is normally a learned parameter or a persistent buffer.

<details><summary>Show solution</summary>It is a persistent buffer. It is not learned directly through gradients but is saved in the `state_dict`.</details>

### 3. Inference

Determine whether AdamW state is needed to reproduce only a fixed model's eval outputs.

<details><summary>Show solution</summary>It is not. Inference requires model state and forward conditions such as configuration, tokenizer, input, and dtype.</details>

### 4. Resumption

Name two kinds of state needed in addition to weights to resume AdamW training exactly.

<details><summary>Show solution</summary>Examples include optimizer moments and steps, scheduler, gradient scaler, RNG state, and data position; name at least two.</details>

### 5. Strict loading

Determine whether an unexpected key can be ignored so that analysis can proceed.

<details><summary>Show solution</summary>First resolve the cause of the mismatch in architecture, naming, or checkpoint. Arbitrarily ignoring keys leaves it unclear which state was applied.</details>

### 6. Comparing training points

When comparing steps 10,000 and 50,000, identify what must at least be fixed in addition to the model ID.

<details><summary>Show solution</summary>Fix the suite, seed, architecture, data order, tokenizer, input dataset, and metric, and record each revision and resolved SHA.</details>

## Sources and update boundaries

The `state_dict` contract for parameters and persistent buffers and the contents of training checkpoints were checked against the [PyTorch serialization documentation](https://docs.pytorch.org/docs/stable/notes/serialization) and the [official saving and loading tutorial](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html). Pythia checkpoint intervals and the final revision follow the [official Pythia repository](https://github.com/EleutherAI/pythia).

## Lesson summary

- A model's `state_dict` contains parameters and persistent buffers.
- Optimizer state and global training state are separate from model state.
- Resumable checkpoints require more items than a weight file.
- Validate loading through strict key checks and forward equivalence.
- Checkpoint comparisons require provenance for revisions, steps, seeds, data, and code.

## Pass criteria

- Can you classify the three kinds of state?
- Can you separate inference requirements from training-resumption requirements?
- Can you validate a strict load?
- Can you record a checkpoint revision?
- Can you explain the control variables in a comparison of training points?

## Next lesson

- [N05-28 Integrated lab: the path of one token](N05-28-one-token-path.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Model, buffer, optimizer, and global state are distinguished.
- [x] Every exercise has a solution.
- [x] Model interpretability claims are distinguished by strength of evidence.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and mathematical rendering have been checked.
- [x] Executable code has not been manually duplicated in Markdown.
- [x] Code sources, test paths, resource budgets, and the check date are recorded.
- [x] State, strict-load, and optimizer tests are provided.
