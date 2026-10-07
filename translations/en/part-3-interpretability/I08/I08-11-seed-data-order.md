---
id: "I08-11"
title: "Seeds and data order"
part: 3
stage: "I08"
status: "complete"
prerequisites: ["I08-10", "I08-05", "M04-17"]
estimated_time: "90–120 minutes"
---

# I08-11. Seeds and data order

## Why this lesson matters

Training trajectories vary with initialization, data order, dropout, and kernel nondeterminism. If methods A and B run with different seeds, it is difficult to separate the effect of the method from a lucky trajectory. A paired design that shares random conditions reduces variation while retaining failed seeds in the record.

## Learning objectives

- List the sources of randomness in training.
- Distinguish paired seed designs from unpaired designs.
- Inspect trajectories for individual seeds before averaging them.
- Distinguish reproducibility from replaying identical results.

## Prerequisite check

- Prerequisite lessons: [I08-10 Grokking and phase transitions](I08-10-grokking-phase-transition.md), [I08-05 Mini-batch noise and optimizer state](I08-05-minibatch-noise-optimizer-state.md), [M04-17 Experimental design and reproducibility](../../part-1-foundations/M04/M04-17-experimental-design-reproducibility.md)
- Check question: How does a paired comparison remove shared variation at the experimental-unit level?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $Y_{r,A}(t)$ | `Y sub r A of t` | Metric over time for seed $r$ and method A | Scalar trajectory |
| $\Delta_r(t)$ | `delta sub r of t` | Paired difference for the same seed | Scalar trajectory |
| $\bar\Delta(t)$ | `delta bar of t` | Mean paired difference across seeds | Scalar trajectory |
| initialization seed | `initialization seed` | Source of randomness for the initial parameters | Integer; RNG state |
| shuffle seed | `shuffle seed` | Source of randomness for data order | Integer; RNG state |

## 1. A seed is not a single cause

Even if one integer initializes every library, the sources of randomness serve different roles. A research manifest should record at least the following separately.

- Model initialization
- Dataset splitting and shuffling
- Dropout and augmentation
- Probe and SAE initialization
- Bootstrap and permutation tests
- Deterministic kernel settings and hardware

The same seed integer does not establish that the same random numbers served the same purposes. If a change in method changes the number or order of random calls, subsequent shuffling or dropout may use different random numbers. To share initial weights and data order between models with the same architecture, the saved initial values and batch index sequences must correspond. If separate random streams are used, record the seed and state for each role separately.

Compare what happens when one extra random call is made with the same seed.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two methods initialized from the same random stream consume different numbers of calls, so shuffle receives random value three or four.](../../figures/assets/I08/I08-11-rng-call-order.svg)

<figcaption>This schematic shows how an extra augmentation call in method B shifts the random numbers assigned to later dropout and shuffle calls, even when the same RNG starts with the same seed. The u values represent call order, not actual experimental values. Save and match the initial weights and batch indices, or separate the streams and states by role.</figcaption>
</figure>

## 2. Paired design

Compare two methods with the same seed and data order to form

$$
\Delta_r(t)=Y_{r,A}(t)-Y_{r,B}(t)
$$

If shared seed-level difficulty cancels, the standard error of $\bar\Delta(t)$ decreases. Report the pairing explicitly, together with the unit of analysis.

Fix time $t$ and write the two outcomes across seed repetitions as $Y_A,Y_B$. Then $\operatorname{Var}(Y_A-Y_B)=\operatorname{Var}(Y_A)+\operatorname{Var}(Y_B)-2\operatorname{Cov}(Y_A,Y_B)$. If shared conditions make both methods perform well or poorly together, their positive covariance reduces the variance of the difference. Pairing does not automatically improve precision. With $n$ independent seeds, first compute the difference for each seed, then divide the sample standard deviation of those differences by $\sqrt n$ to estimate the standard error of the mean difference. Do not count multiple checkpoints from the same seed as new independent seeds.

Read the shared seed variation and the method difference on separate axes.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Eight synthetic paired outcomes share seed variation while the within-seed differences vary less than the raw outcomes.](../../figures/assets/I08/I08-11-paired-seed-outcomes.svg)

<figcaption>These are the 8 paired outcomes from the existing synthetic CPU experiment. The two outcomes for the same seed share variation that cancels when A−B is computed first. The 8 seeds on the left are independent repetitions; checkpoints from the same seed must not be counted as additional seeds.</figcaption>
</figure>

Compare calculations that use the pairing and calculations that ignore it, using the same outcomes.

<figure class="lesson-figure" markdown="1">

![The paired standard error and a standard error ignoring the pairing are computed from the same eight synthetic pairs.](../../figures/assets/I08/I08-11-paired-standard-error.svg)

<figcaption>Using the same 8 outcomes, compare the standard deviation of paired differences divided by √8 with the standard error based on the sum of the two variances when pairing is ignored. Positive covariance makes the paired value smaller in this synthetic example. This does not mean that every pairing automatically improves precision.</figcaption>
</figure>

Check the condition under which pairing improves precision.

<figure class="lesson-figure" markdown="1">

![With equal unit outcome variances, the variance of the paired difference equals two minus twice the correlation and increases when correlation is negative.](../../figures/assets/I08/I08-11-covariance-condition.svg)

<figcaption>In this mathematical example with Var(A)=Var(B)=1, the variance of the difference is 2−2ρ. Positive correlation reduces it, whereas negative correlation increases it. Check the sign of the covariance under the shared conditions and the actual differences across seeds.</figcaption>
</figure>

## 3. What the mean hides

When transition times differ across seeds, a pointwise mean curve can show a gradual transition that occurs in no individual seed. Inspect crossing times, whether a transition occurs, and trajectories for individual seeds first; then present the mean and intervals.

Suppose the metrics in two runs change from 0 to 1 at steps 1,000 and 5,000, respectively. Their mean between those steps is 0.5, but one individual run is at 1 and the other is at 0. The intermediate mean does not mean that both runs have changed halfway. Runs with no transition also contribute to the mean, so report the occurrence rate separately from the distribution of transition times among runs where it occurs.

Reproducibility is not limited to bitwise-identical results with the same seed. Assess whether the direction and magnitude of the conclusion remain stable across independent seeds and environments.

Without inspecting individual transitions, the intermediate mean can be misread.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Individual binary transitions at one thousand and five thousand steps yield a pointwise mean plateau of one half although no individual trajectory has that value.](../../figures/assets/I08/I08-11-mean-hides-transition.svg)

<figcaption>The two runs in the text change from 0 to 1 at steps 1000 and 5000, respectively. The pointwise mean of 0.5 between them is a mixture of different states, not a halfway change in each run. Inspect the trajectory and occurrence status for each seed before interpreting the mean.</figcaption>
</figure>

## 4. CPU practice

<!-- I08_EXAMPLE: i08_11_seed_data_order -->

Construct a synthetic paired experiment in which two methods share the same seed effect. The standard error of the paired difference is smaller than the value calculated as if the samples were independent.

## Common misconceptions

### Misconception 1. Fixing the seed eliminates uncertainty

A fixed seed is a measure for replaying one trajectory. The training procedure's sensitivity to seeds must be measured using multiple independent runs.

### Misconception 2. A method comparison remains valid if only good seeds are reported

Selecting seeds after seeing the results introduces selection bias. Report all runs from the prespecified set of seeds.

## Exercises

### 1. Paired differences

For the same three seeds, A gives $(0.8,0.7,0.9)$ and B gives $(0.7,0.65,0.82)$. Compute the paired differences.

<details><summary>Show solution</summary>

They are $(0.10,0.05,0.08)$.

</details>

### 2. Sources of randomness

What changes if the initialization seed is the same but the shuffle seed differs?

<details><summary>Show solution</summary>

Even if the initial weights are the same, the sequence of mini-batch gradients and the optimizer trajectory can differ.

</details>

### 3. Mean curve

If transitions occur at steps 1000 and 5000 for two seeds, how should a gradual rise in the mean curve be interpreted?

<details><summary>Show solution</summary>

It is not evidence that the individual runs changed gradually. Differences in transition times across seeds may have been mixed together in the mean.

</details>

### 4. Failed runs

What bias can arise from excluding seeds that produce an OOM error or divergence?

<details><summary>Show solution</summary>

Retaining only runs that succeed easily overestimates stability and performance. Report the failure rate and causes as well.

</details>

### 5. Bitwise reproduction

Can a conclusion be reproduced if the last decimal digit differs on another GPU?

<details><summary>Show solution</summary>

Yes. Scientific reproducibility can hold if the tolerance and statistical conclusion are maintained. Bitwise identity is a stronger execution requirement.

</details>

### 6. Design

How could a study be arranged to estimate method effects and initialization effects together?

<details><summary>Show solution</summary>

Apply both methods as a pair for each of several initialization seeds, and analyze seeds as blocks.

</details>

## Evidence and update boundaries

For seed-dependent churn in neural-network predictions and the sources of randomness, see [Nagarajan et al. (2021)](https://arxiv.org/abs/2102.03349). Whether deterministic execution is possible depends on the hardware and libraries, so prioritize environment records in the manifest.

## Lesson summary

- Record initialization, shuffling, and sources of randomness in analysis separately.
- A paired design with the same random conditions is useful for method comparisons.
- Inspect transitions for individual seeds before averaging.
- Bitwise replay and reproducibility of conclusions are different criteria.

## Pass criteria

- Can you list the sources of randomness and specify a paired design?
- Can you explain a case in which averaging across seeds blurs a transition?
- Can you establish reporting rules that include failed runs?

## Next lesson

- [I08-12 Introduction to data attribution](I08-12-data-attribution-introduction.md)

## Author checklist

- [x] Sources of randomness and pairing are distinguished.
- [x] Failed seeds and the limitations of means are explained.
- [x] Every exercise has a solution.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Claim strength and spoken readings have been checked.
- [x] Internal links and equations have been checked.
