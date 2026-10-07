---
id: "A09-CAU-08"
title: "Capstone: circuit-level causal claims"
part: 4
stage: "A09-CAU"
status: "complete"
prerequisites: ["A09-CAU-01", "A09-CAU-02", "A09-CAU-03", "A09-CAU-04", "A09-CAU-05", "A09-CAU-06", "A09-CAU-07"]
estimated_time: "120–180 minutes"
---

# A09-CAU-08. Capstone: circuit-level causal claims

## Why this lesson matters

A high attribution score or a single ablation effect does not establish a circuit claim. Bind variables, graphs, interventions, counterfactuals, controls, and populations into one contract, and record evidence for necessity, sufficiency, mediation, and abstraction separately. This capstone provides a final framework for matching claim strength to measured results.

## Learning objectives

- Express a circuit hypothesis using an SCM and potential outcomes.
- Design node and path interventions with matched controls.
- Assign mediation and causal abstraction tests to held-out data.
- Write internal, behavioral, and external claims at the level supported by the evidence.

## Prerequisite check

- Prerequisite lessons: [CAU-01 SCMs](A09-CAU-01-structural-causal-models.md), [CAU-02 The do operator](A09-CAU-02-do-operator-interventions.md), [CAU-03 Identification](A09-CAU-03-confounding-identifiability.md), [CAU-04 Mediation](A09-CAU-04-mediation-assumptions.md), [CAU-05 Potential outcomes](A09-CAU-05-counterfactual-potential-outcomes.md), [CAU-06 Causal abstraction](A09-CAU-06-causal-abstraction.md), [CAU-07 External validity](A09-CAU-07-external-validity-internal-interventions.md)
- Check question: Why does showing both necessity and sufficiency of a component not establish it as the unique mechanism?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $C=(V_C,E_C)$ | `the circuit C with nodes V sub C and edges E sub C` | Circuit hypothesis to test | Directed graph |
| $Y_i(z)$ | `the outcome for prompt i under intervention z` | Prompt-level potential outcome | Scalar or vector |
| $\tau_C=E[Y(1)-Y(0)]$ | `the average intervention effect of circuit C` | Mean effect of a circuit intervention | Scalar or vector contrast |
| $\epsilon_{\mathrm{abs}}$ | `epsilon sub abs` | Discrepancy between high-level and low-level interventions | Nonnegative scalar |

## Analysis contract

First specify behavior $Y$ and the prompt as the experimental unit. Fix clean–corrupted prompt pairs, model, checkpoint, and token positions. Define circuit nodes as residual components or aligned subspaces, and edges as hypotheses about downstream information transfer. Separate the validation set used to select nodes from the final test set.

A graph hypothesizes a computational path; an intervention is a concrete operation testing that hypothesis. Drawing an edge between two nodes does not make it separately manipulable. For path patching, specify which source value is delivered to which receiver and which execution supplies the retained values on other paths. For a subspace node, also include how extracted coordinates are reconstructed into the original activation.

The 1 and 0 in $Y_i(1)$ and $Y_i(0)$ do not automatically mean “clean/corrupted” or “intervention/no intervention.” Specify both executions for every comparison. For example, a necessity contrast can assign 1 to ablation and 0 to an intact execution. A sufficiency contrast can assign 1 to patching the specified clean activation into a corrupted-input execution and 0 to the unpatched corrupted execution. These contrasts are different estimands even when they share the same formula form.

If higher outcomes mean better preservation of behavior, an ablation contrast can be negative and a recovery contrast positive. Do not silently change definitions to align their signs. Keep the model and background outside the intervention fixed across the two executions of one prompt, and summarize repeated token measurements within the prompt. Do not reuse the same test results for candidate selection, baseline selection, and final claim evaluation.

This capstone develops an analysis contract. It does not provide results showing that every test below was executed on a new model. Leave unexecuted items marked `unmeasured`, and write conclusions only for results actually obtained.

The next four figures track subspace reconstruction, paired-execution contrasts, prompt units, and data-separation contracts.

<figure class="lesson-figure" markdown="1">

![An illustrative two-coordinate activation changes only its first subspace coefficient from two to minus one while the second coefficient remains one; the full activation is reconstructed before downstream rerun.](../../figures/assets/A09-CAU/A09-CAU-08-subspace-reconstruction-coordinate.svg)

<figcaption>Replacing first-coordinate subspace coefficient 2 with −1 in illustrative h=(2,1)ᵀ reconstructs h′=(−1,1)ᵀ. The full activation is sent downstream with second coefficient 1 retained. This illustrates the coordinate contract of a subspace patch, not a measured circuit effect.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Necessity compares ablation to intact under one background; sufficiency compares clean patch in a corrupted run to the unpatched corrupted run, so the same equation has different policies and estimands.](../../figures/assets/A09-CAU/A09-CAU-08-necessity-sufficiency-execution-pairs.svg)

<figcaption>In this example, necessity assigns 1 and 0 to ablation and intact execution; sufficiency assigns 1 and 0 to a clean patch in the corrupted execution and its unpatched counterpart. The form Yᵢ(1)−Yᵢ(0) is the same, but different backgrounds and policies define different estimands. The sign statements describe possible directions, not measurements.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Thirty dots denote token measurements inside one prompt, which are summarized into one paired prompt contrast before across-prompt uncertainty analysis.](../../figures/assets/A09-CAU/A09-CAU-08-prompt-token-paired-unit.svg)

<figcaption>The 30 dots are repeated token measurements within one prompt. Summarize outcomes from its two executions into a paired contrast, then analyze uncertainty at the prompt level. Token count is not the number of top-level experimental units.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Localization proposes candidates, validation selects and freezes nodes and policies, then final testing supplies paired effects and uncertainty without recycling test results for selection.](../../figures/assets/A09-CAU/A09-CAU-08-selection-final-test-boundary.svg)

<figcaption>Localization proposes candidates, and validation selects and freezes the node and baseline contracts. Do not use final test results to select candidates again. This capstone designs execution; tests not actually performed remain unmeasured.</figcaption>

</figure>

## Measurement procedure

1. Select candidates using observational activations and attribution, but record these results only as localization evidence.
2. Calculate prompt-level paired necessity and sufficiency effects using node ablation and activation patching.
3. Measure candidate-edge effects through path patching and compare with same-norm random-path controls.
4. Calculate total, direct, and indirect contrasts using mediator patches, and check interaction.
5. Evaluate robustness by varying source pairing, zero, mean, and resample baselines, and off-manifold distance.
6. Measure causal abstraction error between high-level variables and low-level interventions on held-out operations.
7. Repeat aligned-circuit effects on new templates and model seeds to bound external validity.

### What necessity and sufficiency compare

A score decrease after ablation is evidence that the specified removal operation affects that behavior. The stronger phrase “strictly necessary” also requires behavior-success criteria, tolerances, a baseline, and consideration of compensation by other paths. If zero replacement damages the overall computation, it has not isolated the necessity of specific information. Matched controls compare general disruption at the same layer, position, dimension, or norm with candidate-specific effects. Matching norm alone does not match every property of the operation.

Sufficiency under patching is not a sufficient condition independent of the surrounding model. It measures how much behavior is recovered by changing a specified source and component while retaining the rest of the corrupted computation. Limit the claim to “sufficient for recovery under this background and patch rule.” Whether another circuit can recover behavior under the same conditions requires a separate test.

The following coordinate figure shows directional differences that remain despite matched perturbation norms.

<figure class="lesson-figure" markdown="1">

![Two illustrative perturbation directions one, zero and 0.6, 0.8 lie on the same unit circle but differ in direction; matched norm therefore does not match all intervention properties.](../../figures/assets/A09-CAU/A09-CAU-08-same-norm-different-direction-control.svg)

<figcaption>The illustrative perturbation directions (1,0)ᵀ and (0.6,0.8)ᵀ both have norm 1 but different directions. Even when layer, position, and dimension are also matched, matching norm alone does not match all operation properties. This coordinate figure illustrates control conditions, not measured effect differences.</figcaption>

</figure>

### Interaction in paths and mediation

Changing an entire node and changing only its transmission to one receiver are different operations. Simply adding path effects can count the same information twice and miss interactions in downstream nonlinear operations. For a joint intervention on nodes A and B, write the outcomes under the same background and policy as $Y(0,0),Y(1,0),Y(0,1),Y(1,1)$. The interaction contrast is

$$
Y(1,1)-Y(1,0)-Y(0,1)+Y(0,0)
$$

If this is not 0, these four operation outcomes cannot be explained as the sum of two independent effects. Here, A and B name two intervention targets; they do not replace the treatment and mediator notation for natural effects.

In CAU-04, natural direct and indirect effects with compatible references sum to the total effect through cancellation of an intermediate term. That identity holds even with interaction. Calling the sum of individual node-patch effects a joint effect, in contrast, requires a separate additivity assumption. For a mediator patch, first specify whether it uses the same unit's natural mediator or an arbitrary source policy. Identifying natural effects from observational data requires the additional assumptions in that lesson.

The next three figures distinguish the path being manipulated, joint interaction, and the natural-contrast identity.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two circuit layouts compare replacing node A, which can change all outgoing uses, with patching only A to receiver R while another receiver S retains the stated baseline value.](../../figures/assets/A09-CAU/A09-CAU-08-node-versus-receiver-path-contract.svg)

<figcaption>The top replaces node A, potentially affecting all outgoing uses. The bottom defines a path patch replacing only transmission to receiver R with a specified value. Specify which baseline execution supplies retained values on the other path, shown as a gray dashed line. The edges are hypotheses, not evidence of implemented hooks or completed measurements.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An explicitly illustrative rule Y(a,b)=a+b+ab gives four outcomes zero, one, one and three; the joint effect exceeds the sum of single-target effects by one.](../../figures/assets/A09-CAU/A09-CAU-08-joint-intervention-interaction-contrast.svg)

<figcaption>For the illustrative rule Y(a,b)=a+b+ab, the outcomes are Y(0,0)=0, Y(1,0)=1, Y(0,1)=1, and Y(1,1)=3. The interaction contrast is 3−1−1+0=1, so the individual-effect sum 2 does not explain joint effect 3. These are not measurements from an actual model or this capstone.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three compatible natural outcomes form a telescoping NDE plus NIE identity, whereas isolated A and B node effects require a separate joint-interaction test before adding them.](../../figures/assets/A09-CAU/A09-CAU-08-natural-identity-versus-node-additivity.svg)

<figcaption>In the upper natural contrast, intermediate outcome Y(1,M(0)) with the same reference cancels, giving NDE+NIE=TE. This identity holds even with interaction. Calling the sum of individual node effects below a joint effect requires a separate additivity condition; the logic is different.</figcaption>

</figure>

### Follow-up checks for abstraction and transfer

A large patch effect does not by itself establish implementation of a high-level algorithm. Fix the high-level model's variables, rules, and intervention correspondence, then compare recomputed results at both levels. Record errors on prompts and operations not used for selection separately. For a new seed, evaluate prespecified component correspondences rather than numerical indices. If a new architecture has not been tested, exclude it from the conclusion's scope.

## Results record

| Evidence | Supported claim | Additional evidence needed |
|---|---|---|
| attribution | Candidate localization | Intervention |
| ablation | Effect of the specified operation and bounded evidence for necessity | Success criteria, redundancy, baseline controls |
| patching | Recovery and evidence for sufficiency under the specified source and background | Source specificity, off-manifold diagnostics |
| path effect | Effect of the specified graph edge | Alternate paths, interaction controls |
| mediation | Indirect effect of the defined contrast | Identification assumptions |
| abstraction | Implementation consistency for tested operations | Unseen operations and domains |
| seed transfer | Bounded replication of the aligned circuit | Architecture and population transfer |

These rows are not interchangeable scores. Attribution narrows localization, intervention checks an effect, and mediation and abstraction specify which path or rule is being claimed. Not every paper must make every claim in the table. If only a node effect was measured, stop the conclusion at the corresponding row.

Report each contrast's two policies, prompt sampling, outcome and sign, paired effect and uncertainty, and control results. If successful in two seeds, write “replicated in the two evaluated seeds.” Do not expand that statement into confirmation of all seeds, a unique circuit, or a human reasoning mechanism. Failures and `unmeasured` items also determine claim scope.

The following inclusion relation bounds conclusions by evidence actually obtained.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A conditional completed-test scope contains one architecture, specified prompts and two aligned seeds, while other architectures, uniqueness and human mechanism remain outside it without separate evidence.](../../figures/assets/A09-CAU/A09-CAU-08-bounded-final-claim-scope.svg)

<figcaption>This figure shows the bounded conclusion allowed if these tests have actually been completed. Generalization beyond the two evaluated seeds, prompt population, and architecture, circuit uniqueness, and a human mechanism are not established by that result alone. This lesson itself supplies no new experiment results.</figcaption>

</figure>

## Common misconceptions

- Passing several positive tests does not make them independent evidence if they reuse the same prompts and selection.
- Circuit completeness is relative to the observed behavior and intervention family.

## Exercises

### 1. Unit
One prompt yields 30 token effects. What is the top-level unit for paired uncertainty?
<details><summary>Show solution</summary>

Use the prompt as the top-level unit. Summarize token effects within the prompt or use clustered inference.
</details>

### 2. Sufficiency
Patching only the candidate circuit with clean activations recovers behavior, but an alternate circuit also shows the same recovery under full-model ablation. Which claim should be avoided?
<details><summary>Show solution</summary>

Avoid claiming that the candidate circuit is the unique sufficient mechanism. Redundant sufficient paths may exist.
</details>

### 3. Mediation
The effect of jointly patching nodes A and B exceeds the sum of their individual effects. How should path effects be treated?
<details><summary>Show solution</summary>

State the interaction and do not apply an additive mediation decomposition unchanged. Report the joint-intervention contrast as a separate estimand.
</details>

### 4. Final claim
Node and path effects replicate on held-out prompts and two seeds, but a new architecture has not been evaluated. Write the conclusion.
<details><summary>Show solution</summary>

State that aligned-circuit intervention effects replicated in the specified architecture's two seeds and evaluated prompt population. Do not claim generalization to other architectures.
</details>

## Evidence and update boundaries

This capstone provides an analysis contract and evidence ladder for circuit claims. It does not remove all latent confounding or prove uniqueness of a high-level algorithm.

- [Wang et al., *Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small*, §4](https://arxiv.org/pdf/2211.00593): Experimental validation distinguishes circuit performance recovery, completeness, and minimality. The necessity and sufficiency comparisons here do not directly reproduce that paper's scores or experimental results.

## Lesson summary

- Circuit claims are relative to a graph, intervention family, and population.
- Necessity, sufficiency, path effects, and mediation are different estimands.
- Causal abstraction tests high-level and low-level intervention correspondence.
- External validity expands through separate prompt, seed, and architecture stages.

## Pass criteria

- Can you complete a graph–unit–intervention–control–estimand–claim contract?
- Can you state positive results and untested scope together in one paragraph?

## Next lesson

- Proceed to the integrated audit of A09's 7 optional advanced modules.

## Author checklist

- [x] The evidence ladder and external scope for circuit-level causal claims are completed.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
