---
id: "I08-13"
title: "Capstone exercise: the lifecycle of a feature"
part: 3
stage: "I08"
status: "complete"
prerequisites: ["I08-01", "I08-03", "I08-09", "I08-11", "I08-12"]
estimated_time: "150–210 minutes"
---

# I08-13. Capstone exercise: the lifecycle of a feature

## Why this lesson matters

A report on training dynamics requires more than a list of metrics at each checkpoint. The same inputs and candidate features must be matched across time, with formation, recoverability, use, and behavioral evidence kept in separate columns. This lesson connects a CPU report format with local GPU measurements at six Pythia-160M checkpoints.

## Learning objectives

- Audit the provenance and comparison contract for six checkpoints.
- Construct a table of feature formation, recoverability, use, and behavior.
- Report uncertainty in change times and limitations across seeds.
- Combine observational, probe, intervention, and behavioral evidence in a claim ledger.

## Prerequisite check

- Prerequisite lessons: [I08-01 Checkpoint study design](I08-01-checkpoint-study-design.md), [I08-03 Representation alignment](I08-03-representation-alignment.md), [I08-09 Feature emergence](I08-09-feature-emergence.md), [I08-11 Seeds and data order](I08-11-seed-data-order.md), [I08-12 Introduction to data attribution](I08-12-data-attribution-introduction.md)
- Check question: Why should the time when recoverability scores increase be recorded separately from the time when intervention effects grow?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $T=(t_0,\ldots,t_5)$ | `T equals t sub zero through t sub five` | Sequence of six checkpoints | Ordered tuple |
| $q_t$ | `q sub t` | Matched feature direction | $\mathbb R^d$ |
| $R_t$ | `R sub t` | Held-out recoverability | $[0,1]$ |
| $U_t$ | `U sub t` | Margin change measured by zero-ablation | Signed scalar |
| $B_t$ | `B sub t` | Fixed-target first-token NLL | Nonnegative scalar |
| claim ledger | `claim ledger` | Table matching evidence to permitted claims | Structured report |

## 1. Fixed experimental contract

Measurements on the actual model keep the following conditions fixed.

- Model: `EleutherAI/pythia-160m-deduped`
- Revisions: `step0`, `step1000`, `step10000`, `step50000`, `step100000`, `step143000`
- Prompts: 4 place prompts and 4 animal prompts
- Location: layer 5 MLP down projection, last token
- Seed: 20261001
- Behavior: negative log probability of a fixed target's first token
- Recoverability: leave-one-out nearest-centroid condition accuracy from activations
- Use proxy: change in a fixed top-two logit margin after setting that MLP output to 0 for the first prompt

The six experiments run sequentially in separate processes, so only one checkpoint resides on the GPU at a time. Each revision's resolved SHA and artifact hash are recorded in a local manifest.

Check the fixed revision sequence and the loading of one checkpoint at a time.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The six pinned Pythia revisions run in separate sequential processes with one resident checkpoint, fixed inputs, and recorded resolved revision and artifact hashes.](../../figures/assets/I08/I08-13-sequential-checkpoint-provenance.svg)

<figcaption>This is the existing fixed execution sequence for step0,1000,10000,50000,100000,143000. After a checkpoint is measured, the GPU is released and the next checkpoint runs in a separate process. The figure explains the execution contract; it is not the result of a new model run performed for this revision. The six checkpoints are six times along one training path.</figcaption>
</figure>

## 2. Keep the four columns separate

Formation is examined through differences in activation means between the place and animal conditions and alignment across checkpoints. Recoverability is held-out classification performance. The use proxy is a zero-ablation effect; without random-position or random-direction controls, it provides limited intervention evidence. Behavioral NLL measures changes in the external output.

The formation value in the actual output is the L2 norm of the difference between two mean activation vectors: one averaged over the 4 place prompts and the other over the 4 animal prompts. This measures the magnitude of separation between conditions, not the presence or absence of a specific feature directly. It can also grow when the scale of all activations increases. Tracking the same feature direction, such as $q_t$, requires separate examination of alignment from I08-03 and matching from I08-09. The current mean-difference norm alone does not establish that directions have been matched across checkpoints.

$R_t$ is the accuracy from repeating the following procedure eight times: leave one prompt out, compute the place and animal means from the remaining prompts, and assign the held-out activation to the closer mean. The prompt under evaluation does not contribute to the means in that round. Since the result averages eight judgments, changing one judgment changes the value by $1/8$. Most prompts used to construct the means overlap across rounds, however, so the eight rounds must not be counted as eight independent training runs.

$U_t$ is the margin difference before and after setting the entire MLP output for the first prompt to 0. The two token IDs selected in the baseline are retained after ablation. Selecting new top-two tokens after ablation would subtract different output contrasts. Across checkpoints, however, the baseline top-two tokens can differ, so changes in $U_t$ over time do not always compare support for the same token pair. This intervention also does not remove only the $q_t$ direction and therefore does not establish use of that single feature.

$B_t$ averages the negative log probability of each prompt's fixed target first token over eight prompts. As target probability increases, NLL decreases. The probability can change even if the top-1 token remains the same, and an improvement in first-token probability does not mean that the entire completion has become correct. Do not combine this value, activation separation, classification accuracy, and margin changes into a single scale.

The six checkpoints are selected times along one training path, not six independent seeds. They therefore do not estimate a universal emergence step or phase transition.

Separate the magnitude of the mean difference from activation scale.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two mathematical eight-point condition datasets differ only by doubling every activation vector; the mean-difference norm doubles while angular geometry remains unchanged.](../../figures/assets/I08/I08-13-condition-mean-scale.svg)

<figcaption>This mathematical 2D example has 4 points each for place and animal; these are not actual Pythia activations. Doubling the same points increases the norm of the difference between condition means from √13 to 2√13. This increase alone establishes neither a new semantic feature nor direction matching across checkpoints.</figcaption>
</figure>

Check where the prompt under evaluation is excluded from the mean calculation.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Holding Paris out leaves three place and four animal activation vectors for centroids, then the held-out activation is assigned to the nearer centroid.](../../figures/assets/I08/I08-13-leave-one-out-centroids.svg)

<figcaption>This shows one round with Paris excluded from the existing eight prompts. The place mean uses the remaining 3 prompts and the animal mean uses 4; the activation under evaluation contributes to neither mean. Repeating the judgment for every prompt gives accuracy in units of 1/8, but the overlapping training folds are not 8 independent seeds. The figure does not generate new probe results.</figcaption>
</figure>

Fix the extent of the vector intervention and the token pair used for comparison.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Baseline and whole-MLP zero-ablation compare logits for the same baseline-selected token IDs A and B; the entire output vector is replaced by zeros.](../../figures/assets/I08/I08-13-whole-mlp-fixed-token-ablation.svg)

<figcaption>The actual implementation sets the entire last-token MLP output at layer 5 to 0. It retains the two baseline-selected token IDs after ablation to compute U=m_base−m_ablated. This intervention does not erase only the q_t direction, and the baseline token pair can differ across checkpoints.</figcaption>
</figure>

Check which direction represents an improvement in behavior alongside its probability.

<figure class="lesson-figure" markdown="1">

![Negative log target probability decreases as that fixed first-token probability rises; the report averages this quantity over eight prompts.](../../figures/assets/I08/I08-13-first-token-nll.svg)

<figcaption>This shows the mathematical relationship between the probability p of a fixed target first token and −log p. The actual value averages first-token NLL across eight prompts, with a decrease indicating improvement. Even if the top-1 token is unchanged, p can change; a higher first-token probability does not guarantee that the whole completion is correct.</figcaption>
</figure>

## 3. CPU report format

<!-- I08_EXAMPLE: i08_13_feature_lifecycle -->

The numbers in the CPU example are synthetic. Their purpose is to check a report structure that keeps the four claims in separate columns of the same table and can be populated from an actual GPU manifest.

The change from 0.49 to 0.87 in the CPU table's `behavior` values is not a calculation of actual target NLL. Do not concatenate these numbers with actual NLL to form a single curve. When inserting actual results, match not only the column name but also the formula, units, and direction of improvement. Actual behavioral NLL improves by decreasing, so there is no rule that all four columns must increase.

A shared report format does not imply shared metric units.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A synthetic behavior-score series and actual mean first-token NLL have incompatible contracts and may replace a validated report column but must not be concatenated.](../../figures/assets/I08/I08-13-synthetic-real-metric-contracts.svg)

<figcaption>The existing CPU behavior values from 0.49 to 0.87 are not actual NLL. When replacing them with actual local results, check the source, formula, units, and direction of improvement before replacing the column. Do not concatenate two numerical series with the same name into a single time series.</figcaption>
</figure>

## 4. Running the actual Pythia checkpoints

<!-- GPU_EXPERIMENT: pythia_160m_step0_feature_lifecycle -->

<!-- GPU_EXPERIMENT: pythia_160m_step1000_feature_lifecycle -->

<!-- GPU_EXPERIMENT: pythia_160m_step10000_feature_lifecycle -->

<!-- GPU_EXPERIMENT: pythia_160m_step50000_feature_lifecycle -->

<!-- GPU_EXPERIMENT: pythia_160m_step100000_feature_lifecycle -->

<!-- GPU_EXPERIMENT: pythia_160m_step143000_feature_lifecycle -->

If top tokens differ across checkpoints in the local results, first check target tokenization and prompt lengths. A change in activation norm can reflect a change in representation scale; do not equate it with feature formation.

## 5. Claim ledger

| Observation | What can be claimed | What else is needed |
|---|---|---|
| The condition mean difference grows | Separation increases in the specified activation dataset | Independent prompts and alignment stability |
| The held-out score rises | Condition information becomes more recoverable | Probe controls and repetitions across seeds |
| The margin changes under zero-ablation | The component is involved in the specified margin | Random controls and interventions at other locations |
| Target NLL decreases | Prediction of the specified completion improves | Broader tasks and independent evaluation |

The prediction improvement in the NLL row is limited to the fixed first token defined earlier. Even if the other three rows change together, separate evidence is needed to link the feature to improvement of the entire completion.

Report temporal order within the observed checkpoint set as well. If all earlier observations are below the criterion and the value first rises above it at step50000, the first observed crossing is step50000. Bounding the actual first crossing between step10000 and step50000 requires the condition that the value did not exceed the criterion and fall back below it before step10000. If sparse observations cannot establish this condition, report that the observed value changed from low to high between the two checkpoints and leave the actual first-crossing time unresolved.

## Common misconceptions

### Misconception 1. If the four metrics rise together, one feature is the cause

A shared temporal trend does not prove a causal chain involving the same feature. Matching and intervention specificity are required.

### Misconception 2. The difference between step0 and the final checkpoint explains every stage of learning

Intermediate checkpoints can reveal nonmonotonic changes and transient features. Even six points are coarser than the full set of 154 checkpoints.

## Exercises

### 1. Classifying evidence

Leave-one-out probe accuracy rises from 0.5 to 0.9. Which column does this support?

<details><summary>Show solution</summary>

The recoverability column. It does not directly imply functional use by the model.

</details>

### 2. Intervention sign

After zero-ablation, the top-two margin changes from 2.0 to 1.2. If the effect supporting the original margin is defined as $m_{base}-m_{ablated}$, what is its value?

<details><summary>Show solution</summary>

It is $2.0-1.2=0.8$. The positive value suggests that this component supported the original margin.

</details>

### 3. Scale

Activation norms double for every prompt, but the cosine geometry is unchanged. What requires caution?

<details><summary>Show solution</summary>

Do not interpret the increase in norm as the formation of a new semantic feature. Examine geometry that is invariant to normalization alongside behavioral evidence.

</details>

### 4. Temporal location

A low use effect is observed at step10000 and a high one at step50000. How should the emergence step be reported?

<details><summary>Show solution</summary>

The first observed crossing is step50000. Also report the range: the actual transition is between 10000 and 50000.

</details>

### 5. Controls

Give two controls that could strengthen a claim of use based on zero-ablation.

<details><summary>Show solution</summary>

Possible controls include ablation of a random direction with the same norm or a random layer or token, and a matched clean/corrupt input control.

</details>

### 6. Final claim

The four metrics increase in sequence in single-seed Pythia results. What is the strongest permitted conclusion?

<details><summary>Show solution</summary>

You can report the observed temporal order of the four metrics in the fixed model run, prompts, and layer. Generalizing across seeds or concluding that the feature caused the behavioral change requires more repetitions and specific interventions.

</details>

## Evidence and update boundaries

Pythia's public training trajectories are described by [Biderman et al. (2023)](https://proceedings.mlr.press/v202/biderman23a.html). For the comparison framework of checkpoint-based data influence, see [Pruthi et al. (2020)](https://proceedings.neurips.cc/paper/2020/hash/e6385d39ec9394f2f3a354d9d2b88eec-Abstract.html). The actual local numbers apply only to this textbook's eight prompts and single seed.

## Lesson summary

- Track a feature's lifecycle through separate columns for formation, recoverability, use, and behavior.
- Load the six actual Pythia checkpoints one at a time and record their provenance.
- Distinguish synthetic CPU results from actual GPU results.
- Limit generalization from single-seed, sparse-checkpoint results.

## Pass criteria

- Can you match the four kinds of metrics to permitted claims?
- Can you audit the revision, data, seed, and metric in a checkpoint manifest?
- Can you write a report that includes limitations in change times and intervention evidence?

## Next lesson

- Choose modules in Part 4, Stage 9's optional advanced study according to your research question.

## Author checklist

- [x] The six checkpoints and execution order are fixed.
- [x] The four kinds of feature evidence are separated.
- [x] The status of CPU and GPU results is distinguished.
- [x] Every exercise has a solution.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Claim strength and spoken readings have been checked.
- [x] Internal links and equations have been checked.
