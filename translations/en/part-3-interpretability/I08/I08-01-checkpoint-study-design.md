---
id: "I08-01"
title: "Checkpoint study design"
part: 3
stage: "I08"
status: "complete"
prerequisites: ["N05-27", "I07-15"]
estimated_time: "90–120 minutes"
---

# I08-01. Checkpoint study design

## Why this lesson matters

Studying training dynamics is not a comparison of two finished models. First specify checkpoints as samples along the time axis, fixed inputs, identical measurement locations, and behavioral metrics. Without this contract, differences caused by measuring different data or tokens at each checkpoint can be mistaken for changes during training.

## Learning objectives

- Specify the unit of analysis and the objects being compared in a checkpoint study.
- Record revisions, data, seeds, and metrics in a reproducible manifest.
- Distinguish absolute steps from training progress.
- Distinguish exploratory observations from prespecified tests.

## Prerequisite check

- Prerequisite lessons: [N05-27 Checkpoints and model state](../../part-2-neural-computation/N05/N05-27-checkpoint-model-state.md), [I07-15 Controls and statistical validation](../I07/I07-15-controls-statistical-validation.md)
- Check question: What state must be recorded to confirm that two checkpoints are different times in the same training run?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\theta_t$ | `theta sub t` | Model parameters at step $t$ | $\mathbb R^p$ |
| $C=\{t_0,\ldots,t_K\}$ | `C equals the set of t sub zero through t sub K` | Set of selected checkpoint steps | $K+1$ steps |
| $m(\theta_t;D)$ | `m of theta sub t on D` | Metric measured on fixed data $D$ | scalar or vector |
| revision | `revision` | Model state referenced by the repository | branch name or commit SHA |
| manifest | `manifest` | Structured record of run conditions and results | JSON object |

## 1. Fix the samples along the time axis

This textbook's actual-model exercise uses the following six Pythia-160M checkpoints:

$$
C=\{0,1000,10000,50000,100000,143000\}.
$$

Their spacing is not uniform. These six points alone therefore cannot establish that a change is linear or occurred abruptly within a particular interval. Unmeasured changes may have occurred between two observed checkpoints.

The difference in a metric between two times is the total change over that interval. Dividing it by the step difference gives the interval's average rate of change, but does not reveal when the change occurred within the interval. For example, even if the changes over steps 1,000–10,000 and 100,000–143,000 are equal, the latter accumulated over a longer period of training. Connecting two points with a line does not add measurements at unobserved times.

Read the checkpoint spacing by distinguishing the full time axis from the separate zoom of the early steps.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Six Pythia checkpoints on a proportional step axis with a separate early-step zoom](../../figures/assets/I08/I08-01-checkpoint-spacing.svg)

<figcaption>The full axis shows the long intervals late in training; the separate zoom shows the early spacing at steps 0, 1,000, and 10,000. The two axes have different horizontal scales.</figcaption>
</figure>

Compare the changes and average rates for the two intervals separately below.

<figure class="lesson-figure" markdown="1">

![Equal symbolic metric changes across nine thousand and forty-three thousand steps have different average rates](../../figures/assets/I08/I08-01-interval-rate.svg)

<figcaption>Compare average rates obtained by dividing the same positive change Δ by 9,000 steps and 43,000 steps. The lines show the difference in interval averages, not a measured trajectory within either interval.</figcaption>
</figure>

## 2. Measure the same thing again

Write the measurement at checkpoint $t$ as

$$
y_t=m(\theta_t;D,\ell,j,s)
$$

Here, $D$ is the input set, $\ell$ the layer, $j$ the token location, and $s$ the seed. Change only $t$ and hold everything else fixed to connect differences in $y_t$ to the training time.

Measuring the same prompts at multiple times gives a time trajectory for each prompt. Even when comparing checkpoint means, it must be possible to compute differences for the same prompts first, so preserve sample IDs and their correspondence. Multiple checkpoints are not independently trained models. This trajectory shows changes in the specified training run; whether those changes repeat with other training seeds requires a separate comparison across runs.

A minimal manifest includes:

- The repository, requested revision, and resolved commit SHA
- Prompt and label hashes and the sample count
- Layer, component, and token locations
- Seed, dtype, library version, and device
- Metric definition and direction
- Artifact hash, runtime, and resource limits

The row-wise connections below show correspondence over time for the same prompts.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Prompt A B and C each keep one row across four symbolic checkpoints](../../figures/assets/I08/I08-01-sample-time-pairing.svg)

<figcaption>A connected horizontal row is repeated measurement of the same prompt. Preserve correspondence over time by sample ID before comparing checkpoint means.</figcaption>
</figure>

Distinguish a training run from its checkpoints as follows.

<figure class="lesson-figure" markdown="1">

![Several dependent snapshots belong to one training run while a second seed gives a separate run](../../figures/assets/I08/I08-01-run-versus-checkpoints.svg)

<figcaption>Multiple checkpoints from one run belong to a single training trajectory. Generalization across seeds is a question about comparing separate training runs.</figcaption>
</figure>

Reproducing a measurement requires linking the revision name, the actual object, and the execution contract.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A requested step revision resolves to an immutable SHA and both bind the fixed measurement contract and artifact hash](../../figures/assets/I08/I08-01-provenance-contract.svg)

<figcaption>Record the step name and resolved SHA together, and link them to the artifact produced with the same inputs, measurement locations, and metric.</figcaption>
</figure>

## 3. A step is not a complete time coordinate

The same step in different training runs need not mean that the runs have seen the same number of tokens. Batch size, sequence length, gradient accumulation, and the learning-rate schedule can change training progress. When comparing different suites, also record tokens seen, examples processed, or the fraction of the total budget.

The token count processed in one optimizer step is the sum of actual token counts in the accumulated micro-batches. With padding or variable-length inputs, the product of maximum sequence length and batch size alone does not give the valid token count. Likewise, 50% of the total budget matches a relative position in each run, but does not mean the same amount of training if the total budgets differ. Record which time coordinate was matched along with the remaining training conditions.

In the following calculation, valid tokens are summed across micro-batches before one update is performed.

<figure class="lesson-figure" markdown="1">

![Valid token counts from accumulated micro-batches sum within one optimizer update excluding padding](../../figures/assets/I08/I08-01-microbatch-token-count.svg)

<figcaption>The valid token count for one optimizer step is the sum of actual token counts across accumulated micro-batches. Distinguish it from the maximum size including padding.</figcaption>
</figure>

Compare the total token budgets separately even when relative progress is matched between two runs.

<figure class="lesson-figure" markdown="1">

![Two half-filled training-budget bars represent half of different total token budgets](../../figures/assets/I08/I08-01-relative-budget.svg)

<figcaption>Matching the 50% positions of two runs does not match processed token counts when their total budgets differ.</figcaption>
</figure>

## 4. CPU exercise

<!-- I08_EXAMPLE: i08_01_checkpoint_design -->

The code prints one contract containing the six revisions and the data, seed, layer, and metric to be fixed. This output is a design document to review before execution, not actual GPU results.

## Common misconceptions

### Misconception 1. More checkpoints establish causation

Dense observations narrow down when a change occurred, but concluding that the optimizer or data caused it requires controlled experiments.

### Misconception 2. Selection based on the final checkpoint is unbiased

Selecting only interesting prompts or features after inspecting the final results creates selection bias. Confirm exploratory results on independent data or a separate run.

## Exercises

### 1. Comparison contract

List four items other than $t$ to hold fixed when comparing activation norms at two checkpoints.

<details><summary>Show solution</summary>

Fix the input data, layer and component, token location, and dtype. Also record the seed, preprocessing, and norm definition.

</details>

### 2. Unequal spacing

Why should the change between $1000$ and $10000$ not be compared directly with the change between $100000$ and $143000$?

<details><summary>Show solution</summary>

The step intervals differ: 9000 versus 43000. To compare rates of change, divide by the step difference or use a coordinate matched to the training budget.

</details>

### 3. Revision

Explain why both `step10000` and the resolved commit SHA are recorded.

<details><summary>Show solution</summary>

The branch name gives a human-readable training time, while the SHA identifies the immutable object actually downloaded. Recording both preserves meaning and reproducibility.

</details>

### 4. Unit of analysis

If the same 100 prompts are measured at six checkpoints, are there 600 independent samples?

<details><summary>Show solution</summary>

No. The same prompts are measured repeatedly, so prompts are paired experimental units. Treating the 600 checkpoint measurements as independent samples creates pseudoreplication.

</details>

### 5. Discovery and confirmation

The layer with the greatest separation is selected at the final checkpoint, then tested for significance on the same data. What is the problem?

<details><summary>Show solution</summary>

The same data were used for both selection and testing. Account for multiple comparisons in layer selection or use independent confirmation data.

</details>

### 6. Missing state

Why is a comparison risky when model weights match but tokenizer revisions differ?

<details><summary>Show solution</summary>

The same string can become different token IDs and locations. The input itself changes, so checkpoint effects cannot be separated from tokenizer effects.

</details>

## Sources and boundaries for updates

Pythia's public checkpoint system and shared data order follow [Biderman et al. (2023)](https://proceedings.mlr.press/v202/biderman23a.html). This textbook's six checkpoints are an educational sample, not assumed to represent all checkpoints that Pythia provides.

## Lesson summary

- Training-dynamics measurements are repeated measurements with conditions other than the checkpoint held fixed.
- Record revision names and resolved SHAs together.
- Uneven checkpoints limit the temporal resolution of the observed trajectory.
- Confirm features selected during discovery under independent conditions.

## Pass criteria

- Can you list the required items in a checkpoint-study manifest?
- Can you distinguish paired units from checkpoint measurements?
- Can you identify causal claims that an observed trajectory does not support?

## Next lesson

- [I08-02 Parameter distance and function distance](I08-02-parameter-function-distance.md)

## Author checklist

- [x] The checkpoint, data, seed, and metric contract is specified.
- [x] The six Pythia revisions are fixed.
- [x] Every exercise has a solution.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Internal links and equation delimiters have been checked.
