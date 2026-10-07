---
id: "A09-CAU-04"
title: "Assumptions for mediation"
part: 4
stage: "A09-CAU"
status: "complete"
prerequisites: ["M04-16", "I07-13", "A09-CAU-03"]
estimated_time: "90–120 minutes"
---

# A09-CAU-04. Assumptions for mediation

## Why this lesson matters

To claim that a treatment effect is transmitted through an internal component, we must define total, direct, and indirect effects. A regression coefficient obtained by conditioning on a mediator does not by itself provide a path-specific causal effect. Natural effects combine potential outcomes from different intervention worlds and therefore require strong assumptions.

## Learning objectives

- Express total, natural direct, and natural indirect effects using potential outcomes.
- Distinguish conditioning on a mediator from intervening on it.
- Explain the assumptions required to identify natural effects.
- Diagnose interaction and off-manifold issues in neural mediation results.

## Prerequisite check

- Prerequisite lessons: [M04-16 Correlation and causation](../../part-1-foundations/M04/M04-16-correlation-causation.md), [I07-13 Mediation and counterfactuals](../../part-3-interpretability/I07/I07-13-mediation-counterfactual.md), [A09-CAU-03 Confounding and identifiability](A09-CAU-03-confounding-identifiability.md)
- Check question: In $A\to M\to Y$, why does conditioning on an observed value of $M$ differ from replacing the equation for $M$?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $M(a)$ | `M under treatment a` | Mediator potential outcome under treatment $a$ | Mediator-valued |
| $Y(a,m)$ | `Y under treatment a and mediator m` | Outcome with both treatment and mediator set | Outcome-valued |
| $\operatorname{NDE}$ | `the natural direct effect` | Direct effect with the mediator kept in the baseline world | Scalar expectation |
| $\operatorname{NIE}$ | `the natural indirect effect` | Effect of changing the mediator world with treatment fixed | Scalar expectation |
| $C$ | `C` | Set of pretreatment adjustment covariates | Excludes treatment descendants |

## Core concepts

### Compare two worlds of the same unit

Consider binary treatment $A\in\{0,1\}$, mediator $M$, and outcome $Y$. The value $M(a)$ is the mediator naturally computed when treatment $a$ is set for a unit. The value $Y(a,m)$ is the outcome when the same unit's treatment and mediator are jointly set to $a$ and $m$. This comparison retains the unit's background conditions. Values of $M(a)$ and $Y(a,m)$ can differ across units, and $E$ averages over units in the specified population.

The total effect is

$$
\operatorname{TE}
=E[Y(1,M(1))-Y(0,M(0))]
$$

One compatible decomposition is

$$
\operatorname{NDE}
=E[Y(1,M(0))-Y(0,M(0))],
$$

$$
\operatorname{NIE}
=E[Y(1,M(1))-Y(1,M(0))]
$$

For the NDE, change only treatment while retaining each unit's baseline mediator $M(0)$. For the NIE, keep treatment at 1 while changing the mediator from $M(0)$ to $M(1)$. The value $M(0)$ is not the population's mean mediator or a value drawn arbitrarily from another unit.

Adding the NDE and NIE cancels the intermediate term $Y(1,M(0))$, giving $\operatorname{TE}=\operatorname{NDE}+\operatorname{NIE}$. This equality requires neither an additive outcome model nor a no-interaction assumption. In contrast, fixing the NDE's mediator at $M(1)$ while also defining the NIE at treatment 1 does not cancel the same intermediate term. With interaction, specify the reference world in which each effect is defined.

The quantity $Y(1,M(0))$ is a cross-world counterfactual: the outcome computation under treatment 1 receives the mediator that would have arisen under treatment 0. These worlds are not two different people or prompts; they combine values from two settings of the same unit.

First fix the source of the same unit's mediator, then compare the three worlds.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three aligned computation worlds use the same unit: baseline A0 with M0, treatment A1 with M1, and the hybrid A1 with the baseline M0 copied from the first world.](../../figures/assets/A09-CAU/A09-CAU-04-same-unit-cross-world.svg)

<figcaption>The three columns are settings of the same unit, not different people. The middle column uses treatment 1 but replaces its mediator input with that unit's baseline M(0) to compute Y(1,M(0)). The red lateral arrow marks the source of the cross-world mediator.</figcaption>

</figure>

### Selecting a mediator versus setting it

The quantity $E[Y\mid A=a,M=m]$ is the mean among units actually observed with that treatment and mediator. The quantity $E[Y(a,m)]$ is the mean after setting treatment and mediator for units in the population. If mediator and outcome have a common cause, selecting $M=m$ also changes the proportions of that background, so the two means can differ.

The controlled direct effect fixes the mediator to the same $m$ for every unit and changes treatment: $E[Y(1,m)-Y(0,m)]$. The NDE instead retains each unit's $M(0)$. This distinction prevents us from reading the treatment coefficient in a regression with the mediator as a covariate directly as an NDE. First check which intervention outcome the regression estimates and which functional form and identification assumptions it uses.

Conditioning versus setting, and a controlled value versus a natural baseline value, are separate distinctions.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two illustrative units have baseline mediators 1 and 3; the natural comparison holds each own value while the controlled comparison sets the common mediator 2 in both units.](../../figures/assets/A09-CAU/A09-CAU-04-controlled-versus-natural-mediator.svg)

<figcaption>For illustration, units 1 and 2 have baseline mediators 1 and 3. The NDE changes A while retaining each unit's M(0), whereas the controlled direct effect changes A after assigning the same chosen m=2 to both units. These baseline values illustrate the definition separately from the numerical example M(a)=a below.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![At fixed treatment a, a common cause U affects mediator and outcome; conditioning on M selects U, whereas setting M removes U to M but keeps U to Y.](../../figures/assets/A09-CAU/A09-CAU-04-mediator-selection-versus-setting.svg)

<figcaption>This graph isolates the mediator–outcome common cause U after fixing A=a. Selecting observations with M=m can select background according to P(U|M=m,A=a), whereas M:=m replaces only the mediator mechanism and retains U→Y. The same mediator number does not guarantee equal means.</figcaption>

</figure>

### Conditions for identifying natural effects from observations

Defining a quantity and knowing its value from observational data are separate matters. Baseline covariates $C$ must control treatment–outcome and treatment–mediator confounding, and mediator–outcome confounding must also be sufficiently controlled after treatment and $C$ are fixed. Randomizing treatment alone does not randomize the mediator.

Natural effects also require a coupling between a mediator and outcome from different worlds. One sufficient assumption is that, conditional on $C$, $Y(a,m)$ and $M(a')$ are independent across worlds, including $a\ne a'$. This independence cannot be checked by observing both values together in the same unit. An appropriate independent-noise SCM or corresponding strong sequential ignorability assumptions must justify it. Small observational correlations in the individual relationships cannot replace this assumption.

Under these no-confounding and cross-world conditions, consistency, and positivity for the required treatment and mediator values, the standard mediation formula for discrete $C,M$ is

$$
E[Y(a,M(a'))]
=\sum_{c,m}E[Y\mid A=a,M=m,C=c]
P(M=m\mid A=a',C=c)P(C=c)
$$

The outcome mean uses treatment $a$, while the mediator weights use the distribution under treatment $a'$. Finally, average using the original population proportions of $C$. Substituting $(a,a')=(1,0),(0,0),(1,1)$ and subtracting the corresponding means gives the NDE, NIE, and TE above. The required mediator values must also lie in the observed support of the treatment group used to evaluate the outcome. For continuous variables, replace the sums with integrals.

Consistency requires the observed outcome under the received treatment and natural mediator to equal the outcome represented by this notation. If the way a mediator value is produced has an additional effect, $Y(a,m)$ alone does not sufficiently define the operation. Also, if a treatment-generated variable $L$ is a common cause of mediator and outcome, baseline $C$ alone may not satisfy these assumptions. Adding $L$ to a regression does not automatically restore the standard natural-effect formula.

Examine separately where the mediation formula matches values and where treatment-created confounding occurs.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![For a fixed baseline stratum c, outcome terms from treatment a are matched by mediator value with weights from treatment a-prime, then summed and population-weighted.](../../figures/assets/A09-CAU/A09-CAU-04-mediation-formula-value-routing.svg)

<figcaption>Each row matches the same mediator value m, multiplying an outcome-arm mean at treatment a by a mediator-arm probability at treatment a′. The illustrative rows m=0 and 1 are summed, then averaged with population proportions of C. This shows only value routing; observed arrows alone do not validate cross-world independence or the other identification assumptions.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Treatment A generates L, which then causes both mediator M and outcome Y, so L is a post-treatment mediator-outcome common cause rather than a baseline covariate.](../../figures/assets/A09-CAU/A09-CAU-04-treatment-created-confounder.svg)

<figcaption>L arises after A and is a common cause of M and Y. In this structure, the assumptions of the standard mediation formula adjusting for baseline C may fail. The figure locates how treatment affects the confounding structure; it does not indicate that adding L to a regression solves the problem.</figcaption>

</figure>

### The counterfactual represented by an internal patch

In a neural network, define treatment 0 and 1 variants of the same base prompt. Under the same model and evaluation conditions, patch $M(0)$ into the treatment 1 computation to execute $Y(1,M(0))$ directly. Computing this low-level outcome does not require an observational identification formula as a substitute. If the source is another base prompt or information other than treatment also changes, the result is the effect of the specified source policy, not automatically the natural effect defined above.

Specify the mediator's layer, token, head, or coordinate range, and retain the unchanged computation and downstream recomputation rules. If scale correction or normalization is added, include it in the outcome definition. Do not insert a value other than the original $M(0)$ and report the same natural effect. The resulting hybrid state can fall outside the joint activation relations of natural executions. This does not mean the numerical outcome cannot be executed; it means additional evidence is needed to interpret that outcome as a natural concept change or a unique mechanism.

Trace the path that takes the mediator from the same base prompt and inserts it at the specified hook.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A baseline run of base prompt b caches M_b0, and treatment one of the same base prompt receives that value at a fixed hook before downstream recomputation.](../../figures/assets/A09-CAU/A09-CAU-04-same-base-neural-hybrid.svg)

<figcaption>M_b(0), stored under treatment 0 of the same base prompt b, is inserted at the specified hook under treatment 1 before downstream recomputation. A different base prompt changes the source policy, and scale correction inserts a value different from the original M_b(0). An executable hybrid does not establish a natural concept change or a unique mechanism.</figcaption>

</figure>

## Small example

For $Y(a,m)=a+2m$ and $M(a)=a$, we have $M(0)=0$ and $M(1)=1$. The three required outcomes are $Y(0,0)=0$, $Y(1,0)=1$, and $Y(1,1)=3$. Thus $\operatorname{TE}=3-0=3$, $\operatorname{NDE}=1-0=1$, and $\operatorname{NIE}=3-1=2$.

Adding an interaction term $am$ to the same equation gives $Y(1,1)=4$: the TE is 4, the NDE at the reference above is 1, and the NIE is 3. The equality of their sum is preserved. The direct effect retaining the mediator at $M(1)$ becomes $Y(1,1)-Y(0,1)=4-2=2$. It must be paired with the indirect effect fixed at treatment 0, $Y(0,1)-Y(0,0)=2$, to sum to 4.

This example is calculated directly from known equations. Natural observations contain only $M=A$, so there is no positivity for $(A=1,M=0)$. It is therefore not an example of identifying the cross-world outcome from observational conditional means.

Compare the three outcomes from the known equations and the two reference paths directly.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Baseline, hybrid and treated outcome values are 0, 1, 3 in the additive model and 0, 1, 4 with an interaction, so the same intermediate outcome divides total effect into compatible direct and indirect intervals.](../../figures/assets/A09-CAU/A09-CAU-04-compatible-decomposition-steps.svg)

<figcaption>The three positions are baseline Y(0,M(0)), hybrid Y(1,M(0)), and treated Y(1,M(1)). The additive model's 0→1→3 gives NDE 1 and NIE 2; the interaction model's 0→1→4 gives NDE 1 and NIE 3. Because both intervals use the same intermediate outcome, they sum to the TE even with interaction.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![In the interaction model the four outcomes 0,1,2,4 allow two compatible paths: treatment first yields differences 1 and 3, mediator first yields differences 2 and 2.](../../figures/assets/A09-CAU/A09-CAU-04-interaction-reference-paths.svg)

<figcaption>The four outcomes of Y(a,m)=a+2m+am are 0,1,2,4. Changing treatment first gives 1+3, and changing mediator first gives 2+2; both total differences are 4. Changing the reference changes the terms, so do not arbitrarily mix direct and indirect values from different paths.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Natural states in M(a)=a occur at A0M0 and A1M1 only, while the hybrid A1M0 is computable from the known outcome equation but absent from observational support.](../../figures/assets/A09-CAU/A09-CAU-04-natural-support-and-hybrid.svg)

<figcaption>The natural states of M(a)=a occur only at (A,M)=(0,0) and (1,1). The required hybrid (1,0) is computable from the known outcome equation but absent from natural observational support. This shows the toy model's joint relation; it does not measure an actual model's activation manifold.</figcaption>

</figure>

## Common misconceptions

- Adding a mediator as a regression covariate does not make the treatment coefficient a direct effect.
- A large indirect effect does not establish the mediator as the unique mechanism.

## Exercises

### 1. Effects
Calculate the TE, NDE, and NIE for $Y(a,m)=2a+m$, $M(0)=1$, and $M(1)=4$.
<details><summary>Show solution</summary>

The TE is $Y(1,4)-Y(0,1)=6-1=5$, the NDE is $Y(1,1)-Y(0,1)=3-1=2$, and the NIE is $Y(1,4)-Y(1,1)=6-3=3$.
</details>

### 2. Cross-world
Why is $Y(1,M(0))$ a cross-world quantity?
<details><summary>Show solution</summary>

It combines the outcome equation under treatment 1 with the mediator value that would have been generated under treatment 0.
</details>

### 3. Confounding
If unobserved $Z$ generates both $M$ and $Y$, can regression identify the mediator–outcome effect?
<details><summary>Show solution</summary>

Not in general. Sufficient control of $Z$ or another identification design is needed.
</details>

### 4. Model interpretation
A single-head patch recovers 70% of the total logit effect. What additional checks can strengthen the mediation claim?
<details><summary>Show solution</summary>

Check source–target pairing, matched random-head patches, mediator interaction, off-manifold diagnostics, and nonadditivity when other paths are patched jointly.
</details>

## Evidence and update boundaries

Natural-effect notation here uses binary treatment and one mediator. Stochastic intervention effects and general identification with multiple mediators are outside this lesson's scope.

Natural and controlled effects and cross-world conditions follow §§3.2–3.4 of [Pearl, Direct and Indirect Effects](https://ftp.cs.ucla.edu/pub/stat_ser/R273-U.pdf). The compatible decomposition and sufficient assumptions for the standard mediation formula follow §§3.1–3.3 and Theorem 1 of [Imai, Keele, and Yamamoto](https://imai.fas.harvard.edu/research/files/mediation.pdf). The two outcome models above are calculated directly.

## Lesson summary

- The total effect is the outcome difference between complete treatment worlds.
- Natural direct and indirect effects use cross-world mediator values.
- Mediation identification requires several no-confounding assumptions.
- Executing a cross-world quantity through internal patching does not automatically validate the operation.

## Pass criteria

- Can you calculate the TE, NDE, and NIE using potential outcomes?
- Can you state the confounding, interaction, and off-manifold limitations of a neural mediation claim?

## Next lesson

- [A09-CAU-05 Counterfactuals and potential outcomes](A09-CAU-05-counterfactual-potential-outcomes.md)

## Author checklist

- [x] Natural-effect definitions and cross-world identification assumptions are explained.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
