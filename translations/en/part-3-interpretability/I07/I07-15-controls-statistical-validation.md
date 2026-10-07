---
id: "I07-15"
title: "Controls and statistical validation"
part: 3
stage: "I07"
status: "complete"
prerequisites: ["I07-14", "M04-17"]
estimated_time: "120–150 minutes"
---

# I07-15. Controls and statistical validation

## Why this lesson matters

A large patch effect for one prompt and one component is not reproducible evidence for a circuit. First decide whether inputs are experimental units, whether seeds are repetitions, and whether token-level values are independent samples. Connect matched controls, paired designs, uncertainty, and multiple comparisons to the intervention design.

## Learning objectives

- Define the experimental unit in an intervention experiment.
- Design random, matched, and resampled controls for different purposes.
- Interpret the mean of paired effects, a bootstrap interval, and a sign-flip test.
- Separate location search from confirmatory evaluation.

## Prerequisite check

- Prerequisite lessons: [I07-14 Off-manifold interventions](I07-14-off-manifold-intervention.md), [M04-17 Experimental design and reproducibility](../../part-1-foundations/M04/M04-17-experimental-design-reproducibility.md)
- Check question: Why does counting multiple token effects within one prompt as independent samples create pseudoreplication?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $d_i=y_i^{(1)}-y_i^{(0)}$ | `d sub i equals y sub i one minus y sub i zero` | Paired effect for unit $i$ | scalar |
| $\bar d$ | `d bar` | Mean paired effect | scalar |
| $H_0:\mathbb E[d]=0$ | `H naught: the expectation of d equals zero` | Null hypothesis that the mean intervention effect is zero | hypothesis |
| sign-flip test | `sign flip test` | Test that randomizes the signs of paired differences | randomization test |
| family-wise search | `family-wise search` | Analysis searching multiple nodes or edges together | comparison family |

## 1. Unit of analysis

If prompts were independently sampled, compute the difference between intact and patched metrics for the same prompt,

$$
d_i=m_i^{\mathrm{patched}}-m_i^{\mathrm{base}}
$$

for each prompt. Here, the unit is the prompt, and $d_i$ is the measurement obtained for that unit. Subtracting the base result from the patched result for the same input first avoids mixing differences in the original difficulty of different prompts into the intervention effect. With $n$ independent prompts, the mean $\bar d=\frac1n\sum_{i=1}^n d_i$ gives every prompt the same weight.

Counting 20 tokens from one prompt as 20 independent units ignores their shared input and forward state. When multiple corruption seeds are applied to the same prompt, estimating the mean effect across inputs still requires averaging the seeds within each prompt first or treating the within-prompt repetitions as a group. More seeds measure the random intervention effect on the same input in greater detail; they do not sample new inputs.

The following figures compare pairs within the same prompt first, then distinguish within-prompt token and seed repetitions from independent units.

<figure class="lesson-figure" markdown="1">

![Three prompt dumbbell comparisons connect base metrics one three two to patched metrics three four five with paired differences two one three and mean two](../../figures/assets/I07/I07-15-prompt-paired-differences.svg)

<figcaption>The existing exercise's base values (1,3,2) and patched values (3,4,5) are connected within each prompt. First compute d = (2,1,3), then calculate the mean of 2 with equal weights for the prompts. These are not differences connecting different prompts.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three displayed prompt clusters out of ten each contain token one through twenty and seed repeats but each cluster produces only one prompt-level unit summary so independent count remains ten not two hundred](../../figures/assets/I07/I07-15-prompt-clusters.svg)

<figcaption>P1, P2, and P10 represent three of the existing exercise's 10 independent prompts. The 20 tokens and seed repetitions within each prompt share an input and forward state. If prompts are the sampling units, grouping these repetitions leaves 10 independent units, not 200.</figcaption>

</figure>

## 2. Roles of controls

- Random location: compare with general disruption that occurs regardless of where the change is made.
- Magnitude-matched: compare against differences in activation scale.
- Resampled source: check for a coincidental match in a particular clean pair.
- Sham intervention: check for changes caused by the hook or copying process itself.
- Label permutation: break the connection between the behavioral metric and component selection.

Controls use the same tuning budget as the task condition.

If the question concerns an effect specific to the selected component, the task effect relative to the base is not enough. Compute the task intervention effect and control intervention effect separately for the same prompt, then subtract them. If both effects use the same base, the base metric cancels, leaving the difference between task and control metrics. Even if both interventions greatly change the base output, a difference near 0 provides weak evidence that the selected component had a larger effect than the control.

The interpretation of matching depends on what was matched. Matching activation norms can reduce scale differences, but it does not equate downstream computations across layers or token roles. Fix the properties to compare and the replacement rules rather than changing them after seeing the results to favor a conclusion.

The next figure shows the existing CPU values for subtracting the matched-control effect from the task effect within the same unit.

<figure class="lesson-figure" markdown="1">

![Existing eight CPU units compare task and matched-control base-relative effects then subtract within each unit producing a mean difference zero point three two three seven five](../../figures/assets/I07/I07-15-task-matched-pairs.svg)

<figcaption>The upper panel compares the existing CPU exercise's 8 task effects with its matched-control effects; the lower panel shows their differences within the same units. The mean is 0.32375. Both values are already effects relative to the base, not the original raw metrics.</figcaption>

</figure>

## 3. Uncertainty and testing

A paired bootstrap samples $n$ indices with replacement from the $n$ unit indices and recomputes the mean from the selected units' $d_i$ values. Repeating this procedure approximates variation in the mean. Resampling base and patched values separately breaks their correspondence for the same input, so resample differences or bring along each original pair together. The exercise's percentile interval uses the 2.5% and 97.5% quantiles of the resampled means. Increasing the number of bootstrap repetitions does not increase the number of independent inputs.

In a sign-flip test, retain each unit's difference magnitude and assign a random positive or negative sign to generate null means. This requires the differences of independent units to be symmetric about 0 under the null. The $H_0$ statement that the mean is 0 alone does not imply that symmetry. A two-sided test uses the proportion of null means whose absolute values are at least as large as the absolute observed mean.

For example, with $d=(2,1,3)$, the observed mean is 2, and there are $2^3=8$ possible sign combinations. Only the all-positive and all-negative combinations have a mean with absolute value 2, so the two-sided p-value from enumerating all combinations is $2/8=0.25$. This illustrates how limited the possible null values are in a small sample. Rather than enumerating them all, the CPU exercise randomly samples 4,096 sign combinations and computes a corrected proportion.

The next figures distinguish a bootstrap, which resamples each pair together, from a sign-flip procedure, which retains the magnitudes of the differences.

<figure class="lesson-figure" markdown="1">

![Three original prompt base-to-patched pairs one to three three to four two to five are resampled using indices three one three so complete P3 P1 P3 pairs stay together and their differences three two three average eight thirds](../../figures/assets/I07/I07-15-paired-bootstrap-index.svg)

<figcaption>The existing three prompt pairs are sampled with replacement using the illustrative bootstrap indices [3,1,3]. Even when P3 is selected twice, its base value of 2 and patched value of 5 are brought along together, giving differences (3,2,3) and a resampled mean of 8/3. This procedure does not draw base and patched values separately to create new pairs.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Exact sign-flip null for fixed differences two one three has eight sign patterns with two extreme means minus two and plus two yielding exact two-sided p one quarter](../../figures/assets/I07/I07-15-exact-sign-flip.svg)

<figcaption>All 8 possible sign combinations for d = (2,1,3) in the text are computed. Each bar's height is the number of sign combinations producing that null mean; two combinations coincide at 0. Only the two extreme combinations have an absolute mean at least as large as the observed value of 2, giving p = 2/8 = 0.25. Distinguish this from the CPU's random approximation with 4,096 repetitions.</figcaption>

</figure>

## 4. Multiple comparisons and holdout

If a peak was found by searching across layers, tokens, and components, the entire search is the selection family. Choose candidates on a discovery set, then fix the location and metric for evaluation on a confirmatory set. Repeatedly examining the same data and changing candidates is not a holdout procedure.

Even if candidate effects are dependent, selecting the largest observed value is still selection. Reporting only one location therefore does not make it a single prespecified test. If a candidate is selected again or the metric is changed on confirmatory inputs, those inputs have also been used for search. Record which choices were completed during discovery and which comparisons alone were performed during confirmation.

The next two grids show the entire search family behind a single selected location.

<figure class="lesson-figure" markdown="1">

![Two twelve-layer by twenty-token candidate grids show component one and two with one illustrative selected cell but all four hundred eighty candidates belonging to the selection family](../../figures/assets/I07/I07-15-candidate-family.svg)

<figcaption>The two grids show all 12 layers×20 tokens×2 components from the existing exercise. The purple cell is only an illustrative selection, not a measured effect. Even if only one peak is reported, the selection family contains 480 candidates. Selecting a location or metric again on confirmatory inputs also uses those inputs for search.</figcaption>

</figure>

## 5. CPU exercise

<!-- I07_EXAMPLE: i07_15_controls_statistics -->

Take paired differences between task effects and matched controls for 8 independent units, then compute a bootstrap 95% interval and a sign-flip p-value. The unit count in this example is 8; do not count the numbers inside the effect vector as additional independent samples.

## Common misconceptions

### Misconception 1. More tokens mean more samples

Tokens from the same prompt and run are strongly dependent. Define experimental units using the sampling units and intervention-assignment units.

### Misconception 2. A small p-value means the circuit is correct

A test only evaluates whether the defined effect is compatible with the null; it does not guarantee the graph's completeness, validity, or generalization.

## Exercises

### 1. Paired effect

For three prompts with patched metrics $(3,4,5)$ and base metrics $(1,3,2)$, find $d_i$ and its mean.

<details>
<summary>Show solution</summary>

$d=(2,1,3)$, and the mean is 2.

</details>

### 2. Pseudoreplication

Explain why 20 token effects for each of 10 prompts do not automatically give 200 independent units.

<details>
<summary>Show solution</summary>

Tokens within the same prompt share the input, model state, and corruption. If prompts are the independent sampling units, the basic unit count is 10.

</details>

### 3. Matched control

Propose an appropriate control for an experiment that selects a head with a large activation norm.

<details>
<summary>Show solution</summary>

Randomly select a head in the same layer with a similar norm or output variance, and apply the same intervention.

</details>

### 4. Sign flip

What does the null assumption permitting the signs of all paired differences to be flipped mean?

<details>
<summary>Show solution</summary>

Under the null, the effect distribution is symmetric about 0, so positive and negative signs are exchangeable.

</details>

### 5. Selection family

How many candidate tests are there if 12 layers×20 tokens×2 components were searched?

<details>
<summary>Show solution</summary>

There are $12\times20\times2=480$. Even if only one peak is reported, it was selected from a family of 480 candidates.

</details>

### 6. Interpret a result

An effect interval excludes 0, but the random control has the same magnitude. What conclusion is appropriate?

<details>
<summary>Show solution</summary>

The intervention produced a reproducible change, but there is no evidence that the effect is specific to the selected component. State that general disruption or scale effects have not been ruled out.

</details>

## Sources and boundaries for updates

Sensitivity to metric and corruption choices in activation patching follows [Zhang and Nanda (2023)](https://arxiv.org/abs/2309.16042); quantitative held-out circuit validation follows [Wang et al. (2022)](https://arxiv.org/abs/2211.00593). Statistical tests do not compensate for flaws in experimental design.

## Lesson summary

- Units of analysis are determined by sampling and intervention assignment.
- Random, matched, resampled, and sham controls check different sources of disruption.
- Apply paired bootstrap and sign-flip tests to unit-level effects.
- Separate the search family from the confirmatory holdout.

## Pass criteria

- Can you define an experimental unit and a paired effect?
- Can you design controls for different purposes?
- Can you explain a selection family and held-out validation?

## Next lesson

- [I07-16 Evaluating CoT faithfulness](I07-16-cot-faithfulness.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Experimental units and pseudoreplication are distinguished.
- [x] Controls, paired designs, and multiple comparisons are connected.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is implicitly required.
- [x] Internal links and equation rendering have been checked.
