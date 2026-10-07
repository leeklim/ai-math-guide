---
id: "I08-09"
title: "Feature emergence"
part: 3
stage: "I08"
status: "complete"
prerequisites: ["I08-08", "I08-03", "I07-12"]
estimated_time: "100–130 minutes"
---

# I08-09. Feature emergence

## Why this lesson matters

Saying that a feature “emerged” mixes several events. The time when a direction forms in activation geometry, when a label becomes recoverable, when the model uses that direction functionally, and when behavioral performance changes need not be the same. An analysis over time must separate these four claims.

## Learning objectives

- Define formation, recoverability, use, and behavior as separate metrics.
- Explain the conditions for matching features across checkpoints.
- Report threshold crossings together with uncertainty.
- Avoid claiming instantaneous emergence from sparse observations.

## Prerequisite check

- Prerequisite lessons: [I08-08 Influence function](I08-08-influence-function.md), [I08-03 Representation alignment](I08-03-representation-alignment.md), [I07-12 Necessity and sufficiency](../I07/I07-12-necessity-sufficiency.md)
- Check question: Why does a probe's recovery of labels not imply that the model uses the information?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $F_t$ | `F sub t` | Feature-formation metric at checkpoint $t$ | scalar |
| $R_t$ | `R sub t` | Held-out recoverability | $[0,1]$ or score |
| $U_t$ | `U sub t` | Usage effect measured through intervention | signed scalar |
| $B_t$ | `B sub t` | External behavioral metric | task-dependent |
| $\tau_R$ | `tau sub R` | Recoverability threshold | scalar |

## 1. Separate the four events

Design a feature's table over time as follows.

| Question | Possible measurement | Supported claim |
|---|---|---|
| Has it formed? | Variance, cluster separation, matched-direction stability | Internal structure was observed |
| Is it recoverable? | Held-out probe or decoder score | Information can be read out |
| Is it used? | Ablation or patching effects with controls | It contributes functionally to the defined behavior |
| Does behavior change? | Task accuracy, logit margin, calibration | An external metric changed |

Do not substitute a rise in one column for a rise in another.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Formation recoverability use and behavior curves crossing a measurement threshold at different training steps](../../figures/assets/I08/I08-09-evidence-timeline.svg)

<figcaption>Even for the same candidate feature, structural formation, probe recovery, intervention effects, and behavioral changes can be observed at different checkpoints.</figcaption>
</figure>

The four curves are a conceptual diagram showing that different measurements need not cross thresholds at the same time, not actual measurements claiming a universal order of emergence. Even if a formation metric changes first, a probe may need more training to read that structure reliably. After recoverability rises, intervention evidence that the model uses the feature in its behavior may appear later or never be observed.

Each column has its own measurement error and controls. Formation needs null geometry; recoverability needs label permutation and held-out evaluation; use needs random or norm-matched interventions; behavior needs a task baseline. A plot normalizing the four scores onto one axis summarizes timing, rather than directly comparing absolute values with different units.

Compare observed crossings of different metrics on their own axes.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The CPU synthetic recoverability, ablation-effect, and behavior trajectories have separate scales and thresholds, with first observed crossings three, four, and four.](../../figures/assets/I08/I08-09-separate-observed-events.svg)

<figcaption>The existing synthetic CPU values first cross R's threshold of 0.8 at index 3, the ablation-effect threshold of 0.1 at index 4, and the behavior threshold of 0.8 at index 4. Each metric has its own axis and criterion. Dotted lines between points are visual connections, not actual values at unmeasured checkpoints.</figcaption>
</figure>

## 2. Tracking the same feature

Coordinate-wise neuron IDs do not guarantee meaning across checkpoints. Match features using activation profiles, direction cosines, decoder vectors, and maximal examples, and record whether assignment is one-to-one along with matching scores. With a low score, write “nearest candidate” rather than “the same feature.”

Matching first requires fixing the space to be compared. If neuron bases at two checkpoints can differ by permutation or rotation, apply representation alignment before matching directions rather than comparing coordinates directly. If one checkpoint's feature splits into two at the next checkpoint, or multiple features merge, a one-to-one assignment may itself be inappropriate.

Record identity uncertainty as well as scores in a feature trajectory. An abrupt score change within a low-matching-score interval may reflect a connection to a different candidate rather than an actual feature change.

Follow feature correspondence separately from neuron numbers.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Candidate feature A and B move between neuron one and two; solid high-score matches are distinguished from dashed uncertain later matches.](../../figures/assets/I08/I08-09-candidate-feature-tracks.svg)

<figcaption>This schematic shows that candidate feature correspondences can change even when neuron numbers stay the same. Solid lines show correspondences selected with high scores; dashed lines and question marks show uncertain identities. These are not actual measurements or established feature trajectories. Record the matching evidence after aligning to the same space.</figcaption>
</figure>

Inspect correspondence structures that are difficult to pair one-to-one.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Schematic split and merge candidate relationships have one-to-many and many-to-one correspondences instead of a one-to-one assignment.](../../figures/assets/I08/I08-09-split-merge-correspondence.svg)

<figcaption>The panels separate a correspondence to two candidates at the next checkpoint from several candidates corresponding to one. Dashed lines mark candidate relationships to be checked; they do not prove actual feature splits or merges. In such cases, check the one-to-one matching assumption first.</figcaption>
</figure>

## 3. Emergence time depends on the rule

For example, recoverability emergence can be defined as

$$
t_R=\min\{t\in C:R_t\ge\tau_R\}
$$

Because $C$ is the set of observed checkpoints, this is the first observed time meeting the criterion. If the criterion is never met, the set is empty and $t_R$ is undefined. Do not substitute the last checkpoint as the emergence time; record that the criterion was not reached within the observation window. Changing the threshold, smoothing, or checkpoint grid changes $t_R$ as well. Consider bootstrap intervals or crossing distributions across seeds alongside it.

If consecutive observed checkpoints satisfy $t_1<t_2$ and $R_{t_1}<\tau_R\le R_{t_2}$, the observation changed from below the criterion to at or above it within this interval. For $t_2$ to be the first observed crossing, all earlier observed values must also be below the criterion. Even then, the first-ever attainment during training is not necessarily within $(t_1,t_2]$. The metric may have briefly exceeded the threshold and fallen back in an earlier unmeasured interval. With the additional condition that the metric increases monotonically, its first attainment can be narrowed to this interval. A statement such as `it emerged abruptly at step $t_2$` requires denser observations to check the width and persistence of the change.

When estimating crossing uncertainty with a bootstrap, resample each prompt's measurements across all checkpoints together. This preserves correspondence over time so that crossings can be computed on new trajectories. Retain trajectories that do not meet the criterion in a repetition; averaging crossing times only among repetitions that cross can bias the result toward early-attainment cases.

Choosing a favorable threshold after inspecting the results introduces selection bias into emergence time. Set threshold and smoothing rules before analysis, or report sensitivity analysis showing how conclusions change across reasonable settings.

Distinguish the first observed crossing from the first-ever attainment during training.

<figure class="lesson-figure" markdown="1">

![The same three observed points admit an earlier unmeasured threshold excursion or a monotone delayed crossing.](../../figures/assets/I08/I08-09-observed-versus-first-ever.svg)

<figcaption>Two mathematical paths share the same observations at t=0,2,4. Observed points alone cannot rule out a brief threshold excursion in an earlier unmeasured interval, as shown by the dashed path. The additional condition of monotonic increase is needed to narrow first attainment to between t=2 and 4.</figcaption>
</figure>

Changing the threshold rule changes the time even for the same values.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The same six recoverability values first cross thresholds point seven and point eight at index three, point nine at four, and never reach point nine five.](../../figures/assets/I08/I08-09-threshold-rule-sensitivity.svg)

<figcaption>This comparison changes only the threshold for the existing CPU R array. Thresholds 0.7 and 0.8 are reached at index 3, 0.9 at index 4, and 0.95 is not reached. Report sensitivity across settings rather than replacing a non-attainment case's crossing with the last index.</figcaption>
</figure>

Identify the unit that must be resampled together in the bootstrap.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A bootstrap draw samples prompt A twice and prompt C once, preserving every selected prompt's full checkpoint sequence.](../../figures/assets/I08/I08-09-paired-trajectory-bootstrap.svg)

<figcaption>This schematic represents one bootstrap draw selecting prompts A,A,C. Bring along each prompt's checkpoint measurements together to construct a new trajectory. This differs from drawing different prompts separately at each time, and non-attainment cases in the new trajectories are also retained.</figcaption>
</figure>

## 4. CPU exercise

<!-- I08_EXAMPLE: i08_09_feature_emergence -->

In the synthetic trajectory, recoverability crosses its threshold at checkpoint 3, while intervention-measured use and behavior cross at checkpoint 4. This shows that different kinds of evidence for the same feature can appear at different times.

## Common misconceptions

### Misconception 1. A feature is born the moment probe accuracy exceeds chance

This depends on probe capacity, sample size, and the threshold. A weak structure may have been present earlier.

### Misconception 2. A sharp rise in one seed is a universal phase transition

Check the location and width of the rise with other seeds and denser checkpoints.

## Exercises

### 1. Classify a claim

Held-out linear-probe accuracy is 0.9. Which of the four columns does this provide evidence for?

<details><summary>Show solution</summary>

It is evidence of recoverability. Use and behavioral changes must be measured separately.

</details>

### 2. Evidence of use

Ablating a feature direction lowered the target logit, while a random-direction control produced almost no change. Which column does this provide evidence for?

<details><summary>Show solution</summary>

It is evidence of use for the defined intervention and behavior. Also check for off-manifold states and the units of repetition.

</details>

### 3. Threshold

For $R=(0.5,0.7,0.85)$ and $\tau_R=0.8$, what is the first crossing index?

<details><summary>Show solution</summary>

It is 0-based index 2. To report an actual step, replace it with the corresponding checkpoint step.

</details>

### 4. Matching

Why does the same neuron number at each checkpoint not establish feature identity?

<details><summary>Show solution</summary>

A unit's function and activation profile can change during training, and permutation and superposition can also occur.

</details>

### 5. Temporal resolution

A score rose between steps 10000 and 50000. Can the emergence step be established as 50000?

<details><summary>Show solution</summary>

It is only the first observed crossing; the actual change could have happened at any time between the two checkpoints.

</details>

### 6. Combined interpretation

Recoverability is high, but the ablation effect is close to 0. What is the most conservative conclusion?

<details><summary>Show solution</summary>

State that the information is recoverable with the specified probe, but no evidence of use was observed under the defined intervention and behavior.

</details>

## Sources and boundaries for updates

Pythia's design enabling checkpoint-based training-dynamics research follows [Biderman et al. (2023)](https://proceedings.mlr.press/v202/biderman23a.html). No universal ordering of feature emergence is assumed, and actual feature identity must be revalidated for each measurement method.

## Lesson summary

- Formation, recoverability, use, and behavior are different events.
- Feature matching needs activation and direction evidence beyond coordinate IDs.
- Emergence time depends on the threshold and checkpoint grid.
- Do not claim abrupt birth without multiple seeds and intervention controls.

## Pass criteria

- Can you design separate columns for the four kinds of evidence?
- Can you report uncertainty in feature matching?
- Can you explain the temporal-resolution limits of threshold crossings?

## Next lesson

- [I08-10 Grokking and phase transitions](I08-10-grokking-phase-transition.md)

## Author checklist

- [x] The four feature events are distinguished.
- [x] Dependence on matching and thresholds is specified.
- [x] Every exercise has a solution.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Claim strength and spoken readings have been checked.
- [x] Internal links and equations have been checked.
