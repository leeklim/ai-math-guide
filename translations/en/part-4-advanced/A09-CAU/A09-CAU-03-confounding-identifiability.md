---
id: "A09-CAU-03"
title: "Confounding and identifiability"
part: 4
stage: "A09-CAU"
status: "complete"
prerequisites: ["M04-02", "M04-16", "A09-CAU-02"]
estimated_time: "90–120 minutes"
---

# A09-CAU-03. Confounding and identifiability

## Why this lesson matters

A common cause introduces a noncausal-path contribution to the observed association between treatment and outcome. Computing a causal estimand from an observational distribution requires a graph and assumptions that permit an identification formula. Upstream input features can also act as common causes of internal activations and outputs.

## Learning objectives

- Distinguish a confounder, mediator, and collider in a graph.
- Apply the backdoor adjustment formula.
- Distinguish identifiability from statistical estimation.
- Distinguish the roles of direct execution and observational identification in internal interventions.

## Prerequisite check

- Prerequisite lessons: [M04-02 Conditional probability and Bayes' rule](../../part-1-foundations/M04/M04-02-conditional-probability-bayes-rule.md), [M04-16 Correlation and causation](../../part-1-foundations/M04/M04-16-correlation-causation.md), [A09-CAU-02 The do-operator and interventions](A09-CAU-02-do-operator-interventions.md)
- Check question: If $Z$ is a common cause of $X$ and $Y$, what noncausal path opens between $X$ and $Y$?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $Z\to X$ and $Z\to Y$ | `Z causes both X and Y` | A backdoor path created by $Z$ | graph pattern |
| $P(y\mid\operatorname{do}(x))$ | `the distribution of y under do x` | The interventional distribution to be identified | distribution |
| $\sum_zP(y\mid x,z)P(z)$ | `sum over z of P of y given x and z times P of z` | Discrete backdoor adjustment | probability |
| $Y\perp X\mid Z$ | `Y is independent of X given Z` | A conditional independence statement | relation |

## Core concepts

### Common causes, mediators, and colliders

In the graph $Z\to X$, $Z\to Y$, $X\to Y$, the path $X\leftarrow Z\to Y$ differs from a directed path transmitting a change in $X$ to $Y$. Variation in $Z$ changes both $X$ and $Y$, so the observed $X$–$Y$ association can also include this common cause's influence. In this relationship, $Z$ acts as a confounder.

In $X\to M\to Y$, $M$ is a mediator. A change in $X$ reaches $Y$ through $M$, so fixing $M$ when seeking the total effect blocks part of the causal path being measured. In $X\to C\leftarrow Y$, $C$ is a collider: both arrows meet at $C$. The collider blocks this path when neither $C$ nor its descendants are conditioned on, but conditioning can open it. A variable's role depends on the treatment, outcome, and path being compared.

For example, let independent binary $X,Y$ each take zero and one with equal probability, and let $C=X+Y$. Although $X,Y$ are originally independent, selecting only samples with $C=1$ gives $Y=1-X$. Selecting a common effect alone creates an association between the two causes. Conditioning on more variables therefore does not by itself mean better control of confounding.

Use arrow directions to identify node roles and changes in joint probabilities to examine the effect of collider selection.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three directed graphs distinguish a common cause fork, a mediator chain and a collider, with different effects of conditioning.](../../figures/assets/A09-CAU/A09-CAU-03-middle-node-roles.svg)

<figcaption>The two outgoing edges from Z form a backdoor fork; M lies on the X→Y causal chain. Arrows from X and Y meet at C, and selecting this collider can open the otherwise blocked path. The statements below compare the roles of conditioning or fixing within each path; they do not establish whether other paths exist.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Independent binary X and Y have four mass 0.25 cells; conditioning their sum C to 1 retains only the two off-diagonal cells with mass 0.5 each.](../../figures/assets/A09-CAU/A09-CAU-03-collider-selection-mass.svg)

<figcaption>The joint distribution of independent X and Y assigns probability 0.25 to each of four cells. Selecting samples with C=X+Y=1 leaves only (0,1) and (1,0), each with probability 0.5. The resulting relationship Y=1−X is an association created by selecting a common effect, not the result of intervening on X.</figcaption>

</figure>

### Backdoor sets and averaging weights

A backdoor path starts at $X$ with an edge whose arrow points into $X$. An adjustment set $Z$ satisfies the backdoor criterion if it contains no descendants of $X$ and blocks all such paths. Blocking a path here means conditioning on a non-collider along it to close the path, or applying conditions that do not open a collider. Unobserved common causes must also be represented as latent nodes when needed. A set is not sufficient merely because no path appears in a graph containing only measured variables.

Under these conditions and the required observational support, the causal distribution can be identified as

$$
P(y\mid\operatorname{do}(x))
=\sum_z P(y\mid x,z)P(z)
$$

The backdoor conditions justify using the observed outcome $P(y\mid x,z)$ within a stratum $z$ as the outcome of setting $x$ in that stratum. Then average using the original $P(z)$ to obtain the result for the population in which every unit is assigned $x$. Using the observed treatment group's $P(z\mid x)$ would instead calculate the result for that selected group again.

For discrete $Z$, positivity requires $P(X=x\mid Z=z)>0$ in each required stratum with $P(z)>0$. If this value is zero, the conditional outcome probability cannot be read from the data. Even when it is positive, a very small value may leave few samples in that combination and make estimation unstable. For continuous variables, replace the sum with an integral and interpret positivity in terms of support or density around the required values, rather than probability at a point.

A sufficient adjustment set and the required treatment support are separate conditions.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Conditioning a measured common cause Z blocks its fork; a different graph with latent L retains an open X-left-L-right-Y path despite adjustment for measured Z.](../../figures/assets/A09-CAU/A09-CAU-03-measured-and-latent-backdoor.svg)

<figcaption>Adjusting for Z on the left blocks the displayed backdoor path X←Z→Y. On the right, latent L is a common cause of X and Y, while measured Z is only a parent of X, so adjusting for Z alone leaves X←L→Y open. Both examples preserve the directed path X→Y. They show why a list of measured variables alone does not establish a sufficient adjustment set.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![An illustrative conditional treatment table has positive X=0 probability in Z=0 but no X=0 support in Z=1, so that stratum cannot supply the needed outcome conditional.](../../figures/assets/A09-CAU/A09-CAU-03-positivity-missing-stratum.svg)

<figcaption>In the illustrative treatment probabilities, stratum Z=0 allows both X=0 and X=1, but Z=1 allows only X=1. The red empty cell shows why observational data cannot supply the Z=1 outcome needed to average under an X=0 intervention. The probabilities of X in this table are not outcome probabilities.</figcaption>

</figure>

### Identification before estimation

Identifiability asks whether all models satisfying the given causal assumptions and generating the same observational distribution assign the same value to the target causal estimand. If they do, the estimand can be expressed as a function of the observational distribution. Estimation then uses finite data to estimate conditional probabilities, population weights, and other quantities needed to evaluate that function. An identifiable estimand can still have large estimation error because of small samples, unbalanced strata, or an unsuitable estimator.

Compare a case where the observational distribution is not enough. Let $U$ take zero and one with equal probability. In model A, set $X=U$, $Y=X$; in model B, set $X=U$, $Y=U$. Both models generate only $(X,Y)=(0,0)$ and $(1,1)$, with equal probability in the observational data. After $\operatorname{do}(X=1)$, however, A gives $Y=1$, while B still gives $P(Y=1)=0.5$. Assumptions allowing both causal structures do not identify the effect. Increasing the observational sample size does not change the fact that their distributions are identical.

Compare the equations generating the same observational joint distribution and the results after replacing an equation.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Model A routes U through X into Y while Model B uses U as a common cause of X and Y; their observed pairs match but intervened Y equations differ.](../../figures/assets/A09-CAU/A09-CAU-03-same-law-distinct-mechanisms.svg)

<figcaption>In A, U→X→Y; in B, U is a common cause of X and Y. Original execution gives X=Y=U in both models. After X:=1, A's Y=X becomes 1, whereas B's Y=U retains the original background. If both belong to the permitted model class, the observational joint distribution alone does not determine this intervention outcome.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Exact observational joint tables are identical for models A and B, but intervention X equals 1 puts Y mass 1 on 1 in A and splits mass equally in B.](../../figures/assets/A09-CAU/A09-CAU-03-matched-observation-distinct-intervention.svg)

<figcaption>The two joint distributions above show the same observational probabilities. Below are the distributions obtained by applying do(X=1) to the known equations: P(Y=1)=1 in A and P(Y=1)=0.5 in B. More observational samples can estimate the joint distribution above more accurately, but cannot remove the causal difference between these two permitted structures.</figcaption>

</figure>

### Direct execution of internal interventions

In a neural network, the same input property can determine both activation $H$ and output $Y$. Estimating the effect of $H$ from the observed $H$–$Y$ correlation therefore raises an identification problem requiring upstream influence to be distinguished. If, instead, a fixed model can be executed with $H$ replaced at a specified hook, the outcome of that low-level intervention is obtained by execution. There is no need to calculate the intervention indirectly from observational conditional probabilities.

Pair the original and intervened runs under the same prompt and evaluation settings, and record their difference as the effect for that prompt. A claim about the mean over a prompt population requires specifying which prompts were sampled and in what proportions. It also requires that an intervention on one prompt does not change another prompt's execution. If shared-state changes affect later runs, or batches are dependent, redefine the unit. Direct execution supports measurement of the specified internal operation; equating that operation with a change in a human-level concept requires separate evidence.

Distinguish the execution design that directly manipulates a hook from the sampling and unit conditions needed to average over prompts.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An upstream input fork contrasts with a fixed-prompt paired original and replaced-H execution, whose Y1 minus Y0 measures the specified internal operation.](../../figures/assets/A09-CAU/A09-CAU-03-observation-versus-executable-hook.svg)

<figcaption>On the left, the same input can change both H and Y. On the right, two runs hold the prompt, evaluation settings, and model fixed, manipulate only the specified H, and calculate Y₁−Y₀. This depicts a measurement design, not numerical results, and does not conclude that the low-level operation equals a change in a human-level concept.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Independent paired effects for three prompt units are weighted for a population mean, while state arrows between runs show how shared state can violate separation of units.](../../figures/assets/A09-CAU/A09-CAU-03-prompt-units-shared-state.svg)

<figcaption>The left separates each prompt's paired effect from its sampling weight and averages with wᵢ≥0 and Σwᵢ=1. The red arrows on the right show state passing from one run into the next, requiring the conditions for treating one prompt as an independent unit to be checked again. The displayed Δ symbols belong to the design; they are not experimentally measured values.</figcaption>

</figure>

## Small example

Let $Z$ be binary with $P(Z=1)=0.5$. Assume that the backdoor conditions and positivity hold. If $P(Y=1\mid X=x,Z=0)=0.2$ and $P(Y=1\mid X=x,Z=1)=0.8$, the post-intervention probability is $0.2\times0.5+0.8\times0.5=0.5$.

If the observed $X=x$ group instead has $P(Z=1\mid X=x)=0.9$, its observational probability is $0.2\times0.1+0.8\times0.9=0.74$. The stratum-specific outcomes are the same; only the averaging weights differ. Do not interpret 0.74 as the probability after setting $x$ throughout the population.

Representing stratum proportions as widths and conditional outcomes as heights lets the weighted average be read as an area.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two population mosaics have identical stratum success probabilities 0.2 and 0.8 but different widths for Z strata, yielding outcome masses 0.50 and 0.74.](../../figures/assets/A09-CAU/A09-CAU-03-stratum-weighted-areas.svg)

<figcaption>Each rectangle's width is the proportion of a Z stratum; its filled height is that stratum's outcome probability. Area is their product, so population weights 0.5 and 0.5 give 0.10+0.40=0.50, whereas the observed treatment group's weights 0.1 and 0.9 give 0.02+0.72=0.74. Only the averaging weights change; the stratum-specific outcome heights stay the same.</figcaption>

</figure>

## Common misconceptions

- Conditioning on every pre-treatment variable is not always appropriate. Collider conditioning can open a path.
- An effect's identifiability in a graph does not guarantee that its estimator has low variance.

## Exercises

### 1. Roles
In $X\to M\to Y$, is $M$ a confounder or a mediator?
<details><summary>Show solution</summary>

It is a mediator because it lies on the causal path transmitting the effect of $X$ to $Y$.
</details>

### 2. Adjustment
Expand the backdoor formula into two terms for binary $Z$.
<details><summary>Show solution</summary>

$P(y\mid x,z=0)P(z=0)+P(y\mid x,z=1)P(z=1)$.
</details>

### 3. Positivity
Only $X=1$ was observed in all units with $Z=1$. Can the outcome under $X=0$ in stratum $Z=1$ be estimated by standard adjustment?
<details><summary>Show solution</summary>

No. Positivity fails because $P(X=0\mid Z=1)=0$ in this stratum.
</details>

### 4. Model interpretation
The presence of a country token increases both a head activation and a capital-token logit. What should be done to check the head's causal effect?
<details><summary>Show solution</summary>

Hold the country-token condition fixed as a matched control, and ablate or patch the head activation to measure the logit effect. Report observational correlation separately from the intervention effect.
</details>

## Sources and update boundaries

Backdoor adjustment depends on the assumptions that the causal graph is correct and that the adjustment set is sufficient. This lesson does not cover the complete identification algorithm based on do-calculus.

The backdoor criterion and the definition of identifiability were checked against Section 3.1, Definitions 3–4, and Theorem 1 of [Pearl, Causal Diagrams for Empirical Research](https://ftp.cs.ucla.edu/pub/stat_ser/R218-B.pdf). The collider, weighted-average, and two-model examples were calculated directly from the specified variables and equations.

## Lesson summary

- Confounding arises from common causes of treatment and outcome.
- A backdoor set blocks noncausal paths and provides an adjustment formula.
- Identifiability is a structural question that precedes even the infinite-data limit.
- Executable internal interventions still require assumptions about the population and the validity of the operation.

## Pass criteria

- Can you distinguish a confounder, mediator, and collider in a graph?
- Can you distinguish identification from finite-sample estimation?

## Next lesson

- [A09-CAU-04 Assumptions for mediation](A09-CAU-04-mediation-assumptions.md)

## Author checklist

- [x] Connected confounding, backdoor adjustment, and identifiability with internal interventions.
- [x] All four exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Checked prerequisites and links.

