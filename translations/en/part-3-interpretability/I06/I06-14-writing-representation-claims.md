---
id: "I06-14"
title: "Writing representation claims"
part: 3
stage: "I06"
status: "complete"
prerequisites: ["I06-13", "M04-16"]
estimated_time: "90~120 minutes"
---

# I06-14. Writing representation claims

## Why this lesson matters

A single sentence can turn a result into a claim stronger than its evidence supports. Activation differences, probes, SAE features, and interventions answer different questions. Practice separating the result, alternative explanations, and scope within a result statement.

## Learning objectives

- Classify claims of observation, recovery, use, causation, and generalization.
- Determine the strongest supported claim from an evidence ledger.
- Include the target, measurement, comparison, uncertainty, and scope in a result statement.
- Replace excessive causal or anthropomorphic wording with testable statements.

## Prerequisite check

- Prerequisite lessons: [I06-13 Feature stability and identifiability](I06-13-feature-stability-identifiability.md), [M04-16 Correlation and causation](../../part-1-foundations/M04/M04-16-correlation-causation.md)
- Check question: Is a result showing that a probe recovers a label the same as a result showing that the model uses the label?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| evidence ledger | `evidence ledger` | A table recording required checks and results for each claim | structured record |
| observational claim | `observational claim` | A claim about differences observed in activations or statistics | claim level |
| recoverability claim | `recoverability claim` | A claim that a decoder reads information from held-out data | claim level |
| functional-use claim | `functional use claim` | A claim that the model's computation uses the information | claim level |
| causal claim | `causal claim` | A claim that a controlled intervention changed behavior | claim level |
| generalization scope | `generalization scope` | The range of inputs, models, and seeds over which applicability was tested | stated boundary |

## 1. Five claim levels

| Level | Minimum evidence required | Recommended wording |
|---|---|---|
| Observation | Predefined statistics and comparisons | `a difference was observed` |
| Recovery | A held-out probe and controls | `could be recovered linearly` |
| Use | Downstream functional tests | `there is evidence that the model's computation uses it` |
| Causation | A controlled intervention and controls | `the intervention changed the behavioral measure` |
| Generalization | Repetition across inputs, seeds, checkpoints, and models | `was replicated within the tested scope` |

Success at a lower level does not automatically establish a higher one. For example, even if an intervention changes behavior, an incorrect feature description prevents attributing the causal effect to that particular concept.

Do not read the table as a single ladder that every study must climb in order. Generalization, in particular, is a scope that can be checked separately for an observational, recovery, or intervention result. Repeated observational differences across models do not establish causal use of those differences. A controlled intervention effect on one input does not establish applicability to other inputs. Record claim kind and tested scope separately in the evidence ledger.

Claim kind and tested scope can be placed on different axes.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A two-axis matrix separates claim kind observed recoverable used causal from replication scope one setting new inputs new models; A is repeated observation and B is a single-setting intervention.](../../figures/assets/I06/I06-14-claim-kind-scope.svg)

<figcaption>A is an observation repeated across models; B is an intervention in one setting. A does not automatically establish causal use, nor does B establish generalization to new inputs. The axes distinguish the concepts in the text's examples; they are not a table of measured results.</figcaption>
</figure>

## 2. Components of a result statement

A good result statement includes:

1. The model, revision, and dataset.
2. The layer, token, and component.
3. The measured quantity and control condition.
4. The effect and uncertainty.
5. The control and selection procedures.
6. The supported interpretation and remaining alternatives.

For example:

> At the last token of the layer 5 MLP update in Pythia-160M `step143000`, we observed a difference in mean activation norm across 8 place and animal sentences. This pilot's small sample and limited formats do not test functional use of the concept or generalization to other prompts.

## 3. Revise statements to avoid

The statement `we found a neuron where the model thinks about cities` anthropomorphizes the model, equates a neuron with a feature, and omits the scope of the finding. Revise it as follows.

> On the fixed dataset, many top-activation examples for coordinate 214 contained city tokens. Separate hard negatives and interventions have not yet been evaluated.

The statement `the SAE recovered the true features` also conflates reconstruction, sparsity, and feature validity.

> The SAE achieved activation MSE of 0.02 and mean $L_0$ of 18. Sensitivity and specificity of latent descriptions, along with stability across seeds, require separate evaluation.

## 4. Report negative results too

High performance on a probe control or unstable feature matching is not a failure to delete. These results lower the ceiling on supported conclusions. Disclosing predefined criteria, exclusions, and stopping rules reduces selective reporting.

Which claim becomes weaker depends on which check failed. High accuracy on both task and control weakens evidence for representation-specific recovery. It does not show that the label cannot be read. Poor matching of individual features does not rule out subspace stability. Do not extend a negative conclusion beyond the target of the failed check.

Detecting no change after an intervention also does not immediately imply a complete absence of functional use. Report the measured effect size and uncertainty together with intervention location, strength, and input scope. Failing to distinguish a small effect because uncertainty is wide differs from measuring precisely enough to rule out effects in a specified range.

Saying that no change was detected does not tell us which effect sizes were ruled out.

<figure class="lesson-figure" markdown="1">

![Two schematic intervals centered on zero share reference effect thresholds minus delta and plus delta; the wide interval includes relevant effects while the narrow interval excludes effects beyond those thresholds.](../../figures/assets/I06/I06-14-null-effect-uncertainty.svg)

<figcaption>For the same result centered on 0, wide uncertainty leaves relevant effects of size ±δ possible, while sufficiently narrow uncertainty can rule out effects beyond that range. The value δ is a predefined effect criterion. The figure does not establish an effect of exactly 0 or a complete absence of functional use.</figcaption>
</figure>

## CPU exercise

Enter evidence flags in a ledger and compute the strongest supported claim. Held-out probe and control checks pass, but functional tests and interventions are absent, so the claim stops at `recoverable`.

<!-- I06_EXAMPLE: i06_14_claim_ledger -->

Actual paper statements are more complex than an automated rule, but a ledger provides a check that exposes missing evidence.

## Common misconceptions

### Misconception 1. Using `suggests` makes a strong claim safe

A claim's logical structure matters more than a cautious verb. If the evidence is only observational, do not attach causal nouns to it.

### Misconception 2. Limitations belong only in the discussion

State scope and alternative explanations alongside the main result so readers do not misinterpret it.

### Misconception 3. Replication means the code ran again

Distinguish computational reproducibility from empirical replication that maintains the result across independent seeds, datasets, or models.

## Exercises

### 1. Classify the level

What claim level does `a held-out probe predicted parts of speech with 92% accuracy` represent?

<details><summary>Show solution</summary>It is a recoverability claim. With appropriate controls and baselines, state that part-of-speech information could be read out.</details>

### 2. Revise a statement

Revise `layer 8 determined the correct answer` for a situation in which only activation differences were observed.

<details><summary>Show solution</summary>Write, for example, `a difference in selected activation statistics at layer 8 was observed between the fixed correct-answer and incorrect-answer conditions`. Remove wording about determination or causes.</details>

### 3. Intervention

Performance decreases after ablation. Name one additional control needed for a causal claim.

<details><summary>Show solution</summary>Use random-direction ablation with the same norm and distribution, an activation-magnitude-preserving control, or a sham intervention to distinguish general damage from a target-specific effect.</details>

### 4. Generalization

A result repeats on one checkpoint and English prompts. Can you claim generalization to other languages and models?

<details><summary>Show solution</summary>No. Limit the scope to the tested checkpoint, language, and prompts.</details>

### 5. Negative result

Probe task and control accuracy are both high. What should you report?

<details><summary>Show solution</summary>Report low selectivity, since probe capacity or identity memorization may explain the result. Weaken the representation-specific recovery claim.</details>

### 6. SAE

Only reconstruction and sparsity were measured. Write a supported statement.

<details><summary>Show solution</summary>Write that `on the specified dataset, this SAE achieved the reported reconstruction error and sparsity`. Do not claim latent interpretability, stability, or causal effects.</details>

## Evidence and update boundaries

The claim distinctions follow the project's style and notation rules and the causal distinctions in M04-16. Terminology may differ by field, but the principle of separating measurement, recovery, and intervention evidence remains.

## Lesson summary

- Observation, recovery, use, causation, and generalization are distinct claim levels.
- Include the target, measurement, comparison, uncertainty, and scope in result statements.
- A cautious verb does not resolve insufficient evidence.
- Negative results set the ceiling on supported claims.

## Pass criteria

- Can you classify a given result by claim level?
- Can you revise an excessive statement to match its measurement?
- Can you identify missing controls in an evidence ledger?

## Next lesson

- [I06-15 Capstone exercise: representation report](I06-15-capstone-representation-report.md)

## Author checklist

- [x] Observation, recovery, use, causation, and generalization are distinguished.
- [x] Every exercise has a solution.
- [x] The strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and mathematical rendering have been checked.
