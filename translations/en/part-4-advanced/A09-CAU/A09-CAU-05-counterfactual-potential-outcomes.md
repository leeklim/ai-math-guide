---
id: "A09-CAU-05"
title: "Counterfactuals and potential outcomes"
part: 4
stage: "A09-CAU"
status: "complete"
prerequisites: ["M04-07", "M04-17", "A09-CAU-04"]
estimated_time: "90–120 minutes"
---

# A09-CAU-05. Counterfactuals and potential outcomes

## Why this lesson matters

A causal effect is defined as the difference between outcomes the same unit would have under different treatments, but only one world is observed in reality. A model can execute several internal interventions on the same stored input, making paired counterfactuals easier to compute. Whether the unit and interventions are consistently defined must still be checked separately.

## Learning objectives

- Express individual and average treatment effects.
- Explain the fundamental problem of causal inference.
- Distinguish the roles of consistency, no interference, and exchangeability.
- Explain abduction–action–prediction for SCM counterfactuals.

## Prerequisite check

- Prerequisite lessons: [M04-07 Estimation, bias, and variance](../../part-1-foundations/M04/M04-07-estimation-bias-variance.md), [M04-17 Experimental design and reproducibility](../../part-1-foundations/M04/M04-17-experimental-design-reproducibility.md), [A09-CAU-04 Assumptions for mediation](A09-CAU-04-mediation-assumptions.md)
- Check question: Why can we not observe a person's outcomes under treatments 0 and 1 at the same time?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $Y_i(1)$ | `the potential outcome for unit i under treatment one` | Treated outcome for unit $i$ | Scalar or vector |
| $Y_i(0)$ | `the potential outcome for unit i under treatment zero` | Control outcome for unit $i$ | Scalar or vector |
| $\tau_i=Y_i(1)-Y_i(0)$ | `tau sub i equals Y sub i under treatment one minus Y sub i under treatment zero` | Individual treatment effect | Scalar or vector contrast |
| $\operatorname{ATE}=E[Y(1)-Y(0)]$ | `the average treatment effect` | Population average causal effect | Scalar or vector contrast |

## Core concepts

### Individual effects and the population mean

For unit $i$, define potential outcomes $Y_i(1)$ and $Y_i(0)$. Its individual effect is

$$
\tau_i=Y_i(1)-Y_i(0)
$$

The two terms form a contrast retaining the same unit's background conditions and outcome definition. A difference between observed outcomes from two different units can include their background differences as well as treatment. Define the average treatment effect as $E[\tau]=E[Y(1)]-E[Y(0)]$. These expectations are assumed to exist; for vector outcomes, take the mean component by component.

A person cannot receive both treatments at the same time under the same background, so ordinary observational data reveal only one potential outcome. This is the fundamental problem of causal inference. Applying a different treatment later can involve a different time and background; its result is not automatically the other potential outcome at the original time.

The ATE is a difference between two marginal means, so estimating it does not require jointly knowing both outcomes for every unit. If consistency and no interference below hold, random assignment is independent of potential outcomes, and both treatments have positive probability, the observed group means can estimate the population means of the respective potential outcomes. Randomization does not exactly match the groups' backgrounds in a single finite sample. Assignment randomness remains, so report uncertainty in the mean difference too. Even knowing both marginal distributions does not determine the distribution of individual effects unless we know which $Y(1)$ and $Y(0)$ belong to the same person.

Distinguish which of the two defined worlds is observed, changes in time, and the pairing of marginals.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A fixed unit has two defined potential outcomes, but assignment A_i1 reveals only Y_i1 and leaves Y_i0 unobserved.](../../figures/assets/A09-CAU/A09-CAU-05-one-unit-one-revealed-world.svg)

<figcaption>Even when both potential outcomes of unit i are defined, assignment Aᵢ=1 reveals only Yᵢ(1). The gray box marks Yᵢ(0), unobserved at the same time and background, not a value of 0. The individual effect is the difference between two terms for the same unit, not a difference between two unrelated units.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An observed untreated outcome at time zero and a later treated outcome may use different backgrounds, so the later observation cannot automatically fill the missing treated outcome at time zero.](../../figures/assets/A09-CAU/A09-CAU-05-later-time-different-background.svg)

<figcaption>Applying treatment 1 to the same unit later can involve a different time and background. The lower box requires the outcome that would have occurred under A=1 at the original t₀ and u₀. This does not prohibit using later-time observations in general; it shows that additional conditions are needed to read the two values as one counterfactual pair.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two joint pairings of binary potential outcomes share the same 0.5 marginals and ATE zero, but one has all individual effects zero and the other has effects minus one and plus one.](../../figures/assets/A09-CAU/A09-CAU-05-same-marginals-different-pairing.svg)

<figcaption>In both cases, the marginals of Y(0) and Y(1) assign probability 0.5 each to 0 and 1, so the ATE is 0. In the first coupling, each unit has equal values and τ=0. In the second, they are opposite, with τ=−1 and 1 each occurring half the time. Marginals determine the mean difference, but the individual-effect distribution depends on their joint pairing.</figcaption>

</figure>

### What the three assumptions connect

Consistency requires the observed outcome of a unit that receives $A=a$ to equal the defined $Y(a)$. Applying it requires a sufficiently specific treatment definition. Mixing zero, mean, and source replacements under the same ablation name assigns outcomes from different policies to one $Y(1)$. Treat each policy as a separate treatment or include the policy-selection rule in its definition.

No interference means one unit's treatment does not change another unit's outcome. Without it, writing $Y_i(a)$ with only unit $i$'s treatment is insufficient, because other units' treatments also affect the result. If batch normalization statistics or shared state change other prompt executions, the contract treating one prompt as an independent intervention unit must change.

In an observational study, conditional exchangeability can be assumed given measured pretreatment covariates $Z$: $A\perp(Y(0),Y(1))\mid Z$. Within the same $z$ stratum, treatment selection does not additionally select the distribution of potential outcomes. Together with consistency, this connects $E[Y(a)\mid Z=z]=E[Y\mid A=a,Z=z]$. If positivity also holds in the required strata, averaging these means with the original $P(z)$ gives the population effect. Balance in a few observed covariates does not establish exchangeability of unmeasured backgrounds.

Distinguish paths that change treatment versions from paths transmitting effects between units.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A shared original activation branches into zero, mean and source replacement policies, which define distinct intervention versions rather than one automatically consistent treatment.](../../figures/assets/A09-CAU/A09-CAU-05-treatment-policy-versions.svg)

<figcaption>The three branches from the same original H into zero, mean, and source replacement use different value-generation rules. Calling all of them ablation does not combine them into one Yᵢ(1). To apply consistency, distinguish the policies as separate treatments or include their selection rule in the treatment definition.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A replacement in prompt i changes a shared batch statistic or state that then feeds prompt j's outcome, demonstrating cross-unit interference.](../../figures/assets/A09-CAU/A09-CAU-05-shared-state-interference.svg)

<figcaption>The red path shows prompt i's treatment affecting prompt j's outcome through a shared batch statistic or mutable state. In that case, Yⱼ(Aⱼ) does not sufficiently specify the setting; other units' treatments also affect the result. This illustrates a structure violating no interference, not a claim that a particular Transformer uses batch normalization.</figcaption>

</figure>

### Abduction–action–prediction

To compute an SCM counterfactual for a unit with observed evidence $e$, use these three steps.

1. Abduction: Infer $P(U\mid e)$ from the original equations and evidence. If the evidence uniquely determines exogenous values, obtain a single $u$. If several backgrounds can produce the same observation, retain their posterior distribution.
2. Action: Replace the structural equation for the desired treatment. Do not force the original evidence to fit the new equations again at this stage.
3. Prediction: Insert the same $u$, or each $u$ from the same posterior, into the new equations to compute the outcome. If multiple $u$ remain, average their outcomes using the posterior weights.

A population-wide intervention averages with $P_U$. A counterfactual for a unit with observed evidence averages with $P(U\mid e)$, so the two questions can differ. Drawing fresh noise from its original marginal after abduction discards that unit's background information.

For example, with $X=U_X$ and $Y=2X+U_Y$, observing $X=1,Y=5$ gives $U_X=1,U_Y=3$ by abduction. Set $X:=0$ through action, then retain the same $U_Y=3$ during prediction to obtain counterfactual $Y=3$. Also keeping the original $Y=5$ fixed would not recompute the downstream outcome. If the population has $E[U_Y]=0$, its mean outcome under $\operatorname{do}(X=0)$ is 0, different from this unit's counterfactual.

Compare an example where evidence determines one noise value with one retaining several posterior values.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Observed X1 Y5 in X=U_X and Y=2X+U_Y infer U_X1 U_Y3; setting X0 while keeping that inferred noise predicts Y3, rather than resampling population background.](../../figures/assets/A09-CAU/A09-CAU-05-abduction-action-prediction.svg)

<figcaption>In the text's equations, observing X=1 and Y=5 gives U_X=1 and U_Y=3. Setting X:=0 then computes Y=3 with the same U_Y=3. Forcing the original Y=5 to remain after action is not downstream prediction. The population intervention mean 0 under E[U_Y]=0 and this unit's counterfactual 3 average over different backgrounds.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A toy model with two independent Bernoulli quarter-probability noises and evidence Y1 retains two equally weighted backgrounds; after setting X0 the evidence-conditioned outcome has mass one half on each binary value unlike the population mass.](../../figures/assets/A09-CAU/A09-CAU-05-nonpoint-background-posterior.svg)

<figcaption>In the illustrative SCM X=U_X, Y=X+U_Y, let the independent noises each have P(1)=0.25 and observe only Y=1. The possible (U_X,U_Y)=(1,0) and (0,1) both have prior mass 0.1875, so each posterior weight is 0.5. After X:=0, Y=U_Y gives 0 and 1 equally under the posterior, whereas the population has P(Y=1)=0.25. This illustrates evidence not determining one noise point; it is not an actual model result.</figcaption>

</figure>

### The unit in paired model executions

A deterministic model can run two internal interventions on the same stored prompt to obtain paired outcomes. Fix parameters, hook position, evaluation mode, and outcome metric, and retain the same background other than treatment in both runs. For stochastic execution, specify which random draws are kept as common background and which are averaged over. Running two forward passes does not jointly observe two real-world potential outcomes; it computes two operations in a fixed computational model.

When treatment is a prompt edit, define what changes within the same base unit. If the edit also changes other task information or token count, include semantic pairing, target position, and source–target alignment in the contract. Directly subtracting outcomes whose coordinates and meanings differ does not measure the specified treatment effect.

Align semantic roles rather than token indices, and retain the same outcome coordinate.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Original four and edited six illustrative role positions map country position 1 to 2 and answer position 4 to 6, so paired outcomes require semantic alignment and a fixed output coordinate.](../../figures/assets/A09-CAU/A09-CAU-05-edited-prompt-semantic-alignment.svg)

<figcaption>The four and six boxes are illustrative role arrays with changing positions, not tokenizer outputs. First align the corresponding Country and Answer positions and retain the same outcome coordinate and logit contrast to obtain a meaningful paired difference. Computing two executions of the same stored model is distinct from jointly observing two real-world potential outcomes.</figcaption>

</figure>

## Small example

For each of 10 prompts, define $Y_i(1)$ as the target logit after ablation and $Y_i(0)$ as the original target logit. Then $\tau_i$ is the post-ablation value minus the original. The sample average effect is $\hat\tau=10^{-1}\sum_{i=1}^{10}\tau_i$. A negative value means the defined ablation lowered that logit. Check the order of the two treatments before interpreting the effect's sign.

This mean first describes those 10 prompts. It can be interpreted as an estimate of the population ATE if the independently sampled prompts represent the target population. Do not count several tokens from one prompt as separate independent units; form each prompt's difference first. If the result is close to 0, examine the distribution to determine whether effects are small in every prompt or positive and negative effects cancel.

Prompt-level differences can remain even in an illustrative set of paired effects with mean 0.

<figure class="lesson-figure" markdown="1">

![Ten illustrative paired prompt effects minus two minus one zero one two repeated have sample average zero despite several nonzero signed effects.](../../figures/assets/A09-CAU/A09-CAU-05-cancelling-prompt-effects.svg)

<figcaption>The illustrative 10 paired effects (−2,−1,0,1,2,−2,−1,0,1,2) have mean 0, but not every effect is 0. Each point is a prompt-level ablated−original difference; tokens do not increase the count of independent units. These are not logit results measured in an actual experiment.</figcaption>

</figure>

## Common misconceptions

- Being able to run two model forward passes does not resolve identification of real-world counterfactuals.
- An average effect of 0 can result from cancellation of positive and negative individual effects.

## Exercises

### 1. Individual effect
If $Y_i(1)=5$ and $Y_i(0)=2$, calculate $\tau_i$.
<details><summary>Show solution</summary>

$\tau_i=5-2=3$.
</details>

### 2. ATE
If three units have paired effects $(2,-1,5)$, what is the sample average effect?
<details><summary>Show solution</summary>

It is $(2-1+5)/3=2$.
</details>

### 3. Interference
Which assumption is violated if an intervention on one prompt changes another prompt's output through batch normalization statistics?
<details><summary>Show solution</summary>

There is interference between units. The no-interference assumption treating prompts as independent units is violated.
</details>

### 4. Model interpretation
The clean and corrupted prompts have different token counts. What must be fixed for a paired counterfactual patch?
<details><summary>Show solution</summary>

Prespecify the units' semantic relation, target token position, source–target alignment rule, and outcome definition.
</details>

## Evidence and update boundaries

Potential-outcome notation here centers on binary treatment. Continuous treatments, interference networks, and partial identification are outside this lesson's scope.

For the roles of exchangeability, consistency, positivity, and no interference, see [Hernán, Beyond Exchangeability](https://doi.org/10.1177/0962280211398037). For retaining the evidence-updated background distribution after intervention, see §§2–3 of [Balke and Pearl, Counterfactuals and Policy Analysis in Structural Models](https://arxiv.org/pdf/1302.4929). The linear-equation example in the text is computed by direct substitution.

## Lesson summary

- A causal effect is defined as a potential-outcome contrast for the same unit.
- Real-world data cannot jointly reveal both potential outcomes.
- ATE identification depends on consistency, assignment, and interference assumptions.
- Model interventions also require a unit, pairing, and outcome contract.

## Pass criteria

- Can you calculate individual effects and the ATE?
- Can you explain the three SCM counterfactual steps and the limitations of paired model interventions?

## Next lesson

- [A09-CAU-06 Causal abstraction](A09-CAU-06-causal-abstraction.md)

## Author checklist

- [x] Potential outcomes, the ATE, SCM counterfactuals, and model pairing are connected.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
