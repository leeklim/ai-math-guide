---
id: "A09-CAU-07"
title: "External validity of internal interventions"
part: 4
stage: "A09-CAU"
status: "complete"
prerequisites: ["M04-17", "I07-14", "I07-15", "A09-CAU-05"]
estimated_time: "90–120 minutes"
---

# A09-CAU-07. External validity of internal interventions

## Why this lesson matters

An internal intervention effect measured with one prompt template and model checkpoint is a result for that experiment's population. Transporting the effect to other prompts, languages, model seeds, or architectures requires checking effect heterogeneity and support overlap. Extending a causal effect inside a model to a human reasoning mechanism requires separate bridging assumptions.

## Learning objectives

- Distinguish source-population effects from target-population effects.
- Explain the conditions for transport weighting under covariate shift.
- Analyze effect heterogeneity across prompts, seeds, and checkpoints.
- Bound the external claims supported by internal intervention results.

## Prerequisite check

- Prerequisite lessons: [M04-17 Experimental design and reproducibility](../../part-1-foundations/M04/M04-17-experimental-design-reproducibility.md), [I07-14 Off-manifold interventions](../../part-3-interpretability/I07/I07-14-off-manifold-intervention.md), [I07-15 Controls and statistical validation](../../part-3-interpretability/I07/I07-15-controls-statistical-validation.md), [A09-CAU-05 Counterfactuals and potential outcomes](A09-CAU-05-counterfactual-potential-outcomes.md)
- Check question: Can two datasets with the same average intervention effect have different subgroup effects?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $P_S$ | `P sub S` | Source distribution where interventions are executed | Distribution |
| $P_T$ | `P sub T` | Target distribution to which a claim is transported | Distribution |
| $\tau(x)$ | `tau of x` | Conditional intervention effect in context $x$ | Scalar or vector contrast |
| $w(x)=p_T(x)/p_S(x)$ | `w of x equals p sub T of x over p sub S of x` | Covariate-shift transport weight | Nonnegative scalar |

## Core concepts

### Average the same contrast over different populations

Distinguish the source and target populations' average effects as

$$
\tau_S=E_{X\sim P_S}[Y^1-Y^0],
\qquad
\tau_T=E_{X\sim P_T}[Y^1-Y^0]
$$

The term $Y^1-Y^0$ contrasts two interventions on the same unit; $S$ and $T$ indicate the population over which that contrast is averaged. This notation assumes that the intervention rules and outcome definitions correspond across populations. If one uses zero ablation and the other mean replacement, they are not the same effect with only the population changed.

Even within context $X=x$, there can be multiple prompts or background values. A conditional effect such as $\tau_S(x)=E_S[Y^1-Y^0\mid X=x]$ is therefore a mean within that context. Define $\tau_T(x)$ for the target too. If the two conditional effects are equal, we can use a common function $\tau(x)$. Equal subgroup effects can still produce different overall means when subgroup proportions change. Conversely, coincidentally equal overall means do not imply equal conditional effects.

The following figures distinguish a shared contrast contract from the limits of equal means.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two populations share the same Y1 minus Y0 policy and outcome contract but differ in context proportions; zero ablation versus mean replacement would instead change the operation.](../../figures/assets/A09-CAU/A09-CAU-07-matched-contrast-contract.svg)

<figcaption>Averaging the same Y¹−Y⁰ in source and target populations requires corresponding intervention policies and outcome definitions. Distinguish a change in population proportions from a change in operation, such as zero ablation→mean replacement.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Two equally mixed illustrative populations have conditional effects 1 and 3 versus 3 and 1; their mean is two in both while the subgroup effects differ.](../../figures/assets/A09-CAU/A09-CAU-07-same-mean-different-conditional-effects.svg)

<figcaption>The illustrative source effects in A and B are 1 and 3, while target effects are 3 and 1. Both populations have proportions 0.5 and 0.5. Both means are 2, but conditional effects differ in each context. Equal overall means alone do not establish transportability.</figcaption>

</figure>

### How transport weights change the proportions in a mean

If the conditional effect $\tau(x)$ is stable across populations and target support lies within source support, reweight as

$$
\tau_T=E_{P_S}[w(X)\tau(X)],
\qquad
w(x)=\frac{p_T(x)}{p_S(x)}
$$

Here, $p_S,p_T$ are probability mass functions on the same context space or densities defined with respect to the same reference. For discrete contexts, the intermediate calculation is

$$
\tau_T
=\sum_x p_T(x)\tau(x)
=\sum_{x:p_S(x)>0}p_S(x)\frac{p_T(x)}{p_S(x)}\tau(x)
$$

Multiply the proportion $p_S(x)$ already present in the source mean by $w(x)$ to obtain the target proportion $p_T(x)$. Use integrals instead of sums for continuous contexts. The required means must be finite, and the source must not omit regions assigned positive probability by the target. A context absent from the source has denominator 0 and cannot be recovered by this method.

Weighting changes **how often a context appears**. It does not fix a change in the effect itself within that context. If $\tau_S(x)$ is first estimated from observational data, the previous lesson's consistency, exchangeability, and positivity conditions are also needed separately. Directly executing paired model interventions does not automatically establish stability of the conditional effect in the target.

A large weight means that a context rare in the source contributes substantially to the target mean. Its estimation error can also be amplified. Finite-sample weights $w_i$ are generally not proportions summing to 1. Distinguish the normalized weights in $\sum_i w_i\widehat\tau_i/\sum_i w_i$, namely $w_i/\sum_j w_j$. Clipping weights for stability can produce a weighted mean different from the original target mean, so disclose the processing rule.

The next three figures separately track mass transformation, missing support, and the effects of weight processing.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Source masses 0.5 and 0.5 multiply by density ratios 0.4 and 1.6 to become target masses 0.2 and 0.8; density ratios differ from normalized sample weights.](../../figures/assets/A09-CAU/A09-CAU-07-density-ratio-mass-routing.svg)

<figcaption>Multiplying source mass p_S(x) by ratio p_T(x)/p_S(x) gives target mass p_T(x). The ratios 0.4 and 1.6 are not sample contribution proportions summing to 1; distinguish them from normalized weights wᵢ/Σⱼwⱼ.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![An illustrative third context has target mass 0.5 but zero source mass; a red missing-support region has no ratio or source effect to reweight.](../../figures/assets/A09-CAU/A09-CAU-07-missing-target-support.svg)

<figcaption>The illustrative context C has target mass 0.5 but source mass 0. Ratio weighting cannot create the effect of an absent context. This is why target support must lie within source support.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A rare illustrative source context has mass 0.05 and target mass 0.50 so ratio ten amplifies a conditional estimation error; clipping at four changes its weighted mass to 0.20 before any renormalization.](../../figures/assets/A09-CAU/A09-CAU-07-large-weight-amplification-and-clipping.svg)

<figcaption>In an illustrative rare context, source mass 0.05 and target mass 0.50 give ratio 10. The same conditional-effect estimation error has a larger weighted contribution. Clipping the ratio at 4 gives this context unnormalized mass 0.20 rather than the original target mass 0.50. Even after renormalization, check the resulting distribution again.</figcaption>

</figure>

### Effect heterogeneity and model correspondence

Internal intervention effects can vary with prompt topic, syntax, and token position. Divide contexts into subgroups and examine their contrasts and differences. Changing the layer or baseline value changes the intervention target or policy; record this separately from context differences under one intervention. Do not use an activation changed by intervention as a baseline context without explanation.

When model seed or checkpoint changes, redefine node correspondence too. Functions, subspaces, or circuit roles can provide alignment criteria instead of matching neuron indices directly. However, finding components with high activation similarity does not guarantee equal intervention effects. Select correspondence rules on selection data, then check intervention results on separate prompts. If tokenizers or output scales differ, also specify correspondences for token positions and outcomes.

The next two figures separate context comparisons, policy changes, and component correspondence across models.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two template contexts share layer and replacement under one policy, whereas changing layer or replacement is shown in a separate intervention-contract branch.](../../figures/assets/A09-CAU/A09-CAU-07-context-versus-policy-change.svg)

<figcaption>Comparing templates A and B under the same layer and replacement asks about context heterogeneity. Changing layer, baseline, or replacement also changes the intervention contract, so record it separately from population differences.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Same-index heads across seeds are not assumed equivalent; a role or subspace correspondence is selected separately and then intervention responses are checked on held-out prompts.](../../figures/assets/A09-CAU/A09-CAU-07-seed-role-heldout-correspondence.svg)

<figcaption>The same head index does not establish correspondence in causal role. This seed correspondence is illustrative, not an actual model-alignment result. After choosing role or subspace correspondence on selection data, check intervention responses and correspondence of token roles and output scales on separate prompts.</figcaption>

</figure>

### Tested transfer and external claims

Expand external validity in stages. Test transfer to held-out prompts from the same template, new templates, new data domains, new seeds, and new architectures, in that order. Claiming that a neural intervention effect acts through the same mechanism in human cognition or social outcomes requires a separate empirical bridge.

This order organizes the reporting of scope; it is not a law guaranteeing success at the next stage after success at the previous one. Report evaluation-prompt sampling rules, successful and failed subgroups, and model and intervention correspondences to judge how far the result transfers. Internal activation manipulations and interventions on humans or the real world have different targets and policies. Naming the same concept does not make their causal effects identical.

The following connections show transfer scopes to test, not automatic generalization guarantees.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A tested source branches separately to new template, domain, seed and architecture tests, while human mechanism claims require a distinct empirical bridge.](../../figures/assets/A09-CAU/A09-CAU-07-separate-transfer-evidence-scopes.svg)

<figcaption>New templates, domains, seeds, and architectures are separate transfer scopes. The connections identify additional tests; they do not automatically transmit success. Transporting a claim about internal model operations to a human mechanism requires a separate empirical bridge.</figcaption>

</figure>

## Small example

If the mean logit effect of head ablation is 1.2 in template A and 0.1 in template B, do not report only a pooled average. Present template-specific effects and an interaction interval, and specify the target population's template mixture.

If the source contains both templates equally, its mean is $0.5(1.2)+0.5(0.1)=0.65$. If conditional effects remain stable and target proportions are A 0.2 and B 0.8, the target mean is $0.2(1.2)+0.8(0.1)=0.32$. Density-ratio weights are $0.2/0.5=0.4$ for A and $0.8/0.5=1.6$ for B. Applying them in the source mean gives the same result, $0.5(0.4)(1.2)+0.5(1.6)(0.1)=0.32$.

The difference between template effects is $1.2-0.1=1.1$. Here, the interaction interval is an uncertainty interval for this difference. Rather than checking only whether the two means' intervals overlap, calculate an interval for the difference itself using the sampling unit. If values summing to 1 are given, as with the exercise's normalized weights, read them as contribution proportions used directly in the mean, not as density ratios.

The following areas and height difference show distinct quantities: a population mean and a subgroup contrast.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Rectangles have widths equal to source or target template mass and heights equal to stable effects 1.2 and 0.1, so their total areas change from 0.65 to 0.32.](../../figures/assets/A09-CAU/A09-CAU-07-mixture-weighted-effect-areas.svg)

<figcaption>The two template effects 1.2 and 0.1 from the text are heights; population proportions are widths. Even with stable conditional effects, changing A and B's widths from source proportions 0.5 and 0.5 to target proportions 0.2 and 0.8 changes total area from 0.65→0.32.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Two illustrative template effects 1.2 and 0.1 are connected by a difference bracket of 1.1; no confidence intervals or measured errors are invented.](../../figures/assets/A09-CAU/A09-CAU-07-subgroup-effect-difference.svg)

<figcaption>The template-effect difference in the text is 1.2−0.1=1.1. This figure shows only that calculation. Estimate its uncertainty interval separately using the actual sampling unit; overlap of the two mean intervals is not a substitute.</figcaption>

</figure>

## Common misconceptions

- Using multiple prompts does not by itself make them representative of the entire target domain.
- Equal neuron indices across seeds of the same architecture do not establish correspondence in causal role.

## Exercises

### 1. Transport
Under $P_S$, two context effects are $(1,3)$ and normalized target weights are $(0.25,0.75)$. What is the target average effect?
<details><summary>Show solution</summary>

It is $0.25(1)+0.75(3)=2.5$.
</details>

### 2. Positivity
If a language appears only in the target and is entirely absent from the source experiment, can weighting transport the effect?
<details><summary>Show solution</summary>

No. Target support extends beyond source support, violating positivity.
</details>

### 3. Heterogeneity
The overall effect is 0, but two template effects are $+2$ and $-2$. What should be reported?
<details><summary>Show solution</summary>

Report template-specific effects and the target mixture. Do not interpret the pooled zero as absence of an effect.
</details>

### 4. Model interpretation
To transport a finding that head 7 is necessary in one model seed to another seed, which correspondence should be specified first?
<details><summary>Show solution</summary>

Identify corresponding circuit components using input–output roles, path effects, and held-out intervention responses, not activation similarity alone.
</details>

## Evidence and update boundaries

The transport-weighting formula assumes conditional-effect transportability and covariate shift. Selection diagrams and general transport formulas are outside this lesson's scope.

- [Dahabreh et al., *Extending inferences from a randomized trial to a new target population*, §4 and §8](https://arxiv.org/pdf/1805.00550): Stability of conditional effects across populations, positivity, and large-weight issues. The trial's treatment contrast and a model's internal intervention are not thereby the same operation.
- [Sugiyama et al., *Covariate Shift Adaptation by Importance Weighted Cross Validation* (2007), §2.1–2.2](https://jmlr.org/papers/volume8/sugiyama07a/sugiyama07a.pdf): Importance weighting uses input density ratios to change the distribution underlying a mean. The operation itself does not supply causal identification conditions.

## Lesson summary

- A causal effect is relative to a source population and intervention policy.
- Transport requires support overlap and effect stability.
- Prompts, templates, seeds, and checkpoints can be effect modifiers.
- Transporting an internal model effect to a human-level mechanism requires separate evidence.

## Pass criteria

- Can you state source and target effects and transport assumptions?
- Can you limit an internal intervention claim to the tested domain and model scope?

## Next lesson

- [A09-CAU-08 Capstone: circuit-level causal claims](A09-CAU-08-capstone-circuit-causal-claims.md)

## Author checklist

- [x] Population transport, effect heterogeneity, and model correspondence are explained.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
