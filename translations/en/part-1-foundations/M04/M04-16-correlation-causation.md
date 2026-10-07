---
id: "M04-16"
title: "Correlation and causation"
part: 1
stage: "M04"
status: "complete"
prerequisites:
  - "M04-02"
  - "M04-04"
  - "M04-06"
  - "M04-08"
  - "M04-09"
  - "M04-10"
estimated_time: "160~190 minutes"
---

# M04-16. Correlation and causation

## Why this lesson matters

Observing that two variables change together does not establish that changing one variable will change the other. High probe accuracy can show that an activation contains label information, but it does not by itself show that the model uses that activation to compute its output. Correlation, prediction, and causation answer different questions.

A causal claim first needs a specified intervention, outcome, and population for the comparison. Causal graphs distinguish the roles of confounders, mediators, and colliders. Random assignment and appropriate adjustment provide conditions for identifying an intervention effect.

## Learning objectives

After this lesson, you should be able to:

- Distinguish association, prediction, and causal effects.
- Distinguish observational conditioning from intervention notation.
- Identify confounders, mediators, and colliders in a causal graph.
- Explain why confounder adjustment is needed and the conditions it requires.
- Explain an example in which conditioning on a collider creates an association.
- Define the average treatment effect using potential outcomes.
- Explain why random assignment establishes exchangeability.
- Distinguish the claims supported by activation observations and intervention evidence.

## Prerequisite check

- Prerequisite lesson: [M04-02 Conditional probability and Bayes' rule](M04-02-conditional-probability-bayes-rule.md)
- Prerequisite lesson: [M04-04 Expectation, variance, and covariance](M04-04-expectation-variance-covariance.md)
- Prerequisite lesson: [M04-06 Samples, populations, and sampling distributions](M04-06-samples-populations-sampling-distributions.md)
- Prerequisite lesson: [M04-08 Regression and classification](M04-08-regression-classification.md)
- Prerequisite lesson: [M04-09 Confidence intervals and bootstrap](M04-09-confidence-intervals-bootstrap.md)
- Prerequisite lesson: [M04-10 Hypothesis testing and multiple comparisons](M04-10-hypothesis-testing-multiple-comparisons.md)
- Check question: Can you distinguish conditional probability from marginal probability?
- Check question: Can you explain that a correlation coefficient summarizes linear association?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions and scope |
|---|---|---|---|
| $X\not\!\perp\!\!\!\perp Y$ | `X is not independent of Y` | Statistical dependence between $X,Y$ | Does not specify a direction |
| $\operatorname{do}(X=x)$ | `do X equals x` | An intervention that externally sets $X$ to $x$ | Distinct from observational conditioning |
| $Y(1),Y(0)$ | `Y of one and Y of zero` | The same unit's potential outcomes under two treatment states | Cannot both be observed at once |
| ATE | `A T E` | Average treatment effect | $\mathbb E[Y(1)-Y(0)]$ |
| confounder | `confounder` | A common cause of treatment and outcome | A candidate for adjustment |
| mediator | `mediator` | An intermediate variable through which a treatment effect passes | Requires care in total-effect analysis |
| collider | `collider` | A common outcome at which two arrows meet | Conditioning can open a path |
| exchangeability | `exchangeability` | A condition making treatment groups comparable in terms of their potential outcomes | An assumption in observational studies |

## Core concept 1. Association, prediction, and causation ask different questions

Association asks whether observing $X$ changes the distribution of $Y$.

\[
p(y\mid x)\ne p(y)
\]

Prediction asks how well observable features predict unseen outcomes. A strong association can be useful for prediction, but it does not determine the direction of causation.

Causation asks how $Y$ changes when $X$ is changed externally. One example of a population-level causal contrast is

\[
\mathbb E[Y\mid\operatorname{do}(X=1)]
-
\mathbb E[Y\mid\operatorname{do}(X=0)]
\]

This value generally differs from the observational contrast

\[
\mathbb E[Y\mid X=1]-\mathbb E[Y\mid X=0]
\]

## Core concept 2. A causal graph represents assumed directions of generation

In a directed acyclic graph (DAG), nodes are variables, and an arrow $X\to Y$ represents the structural assumption that $X$ is a direct cause of $Y$. A graph is not a diagram automatically determined by data alone. It is a model that makes domain knowledge and research design explicit.

A simple structural equation can be written as

\[
Y=f(X,U_Y)
\]

Here, $U_Y$ collects other causes not shown in the graph. The intervention $\operatorname{do}(X=x)$ means a new system in which the original mechanism generating $X$ is removed and $X=x$ is fixed.

Observational conditioning on $X=x$ selects units that have that value in the original system. This selection can also change the distributions of the causes of $X$ and of $U_Y$. An intervention, by contrast, removes incoming causal paths to $X$ while retaining the other structural equations, then substitutes the changed $X$ into the downstream equations. Even when the two expressions use the same $x$, the rule for selecting a population differs from the rule for changing the system, so the mean outcome can differ.

Using the same value X=1 does not make selecting an observed group equivalent to changing a generative path.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Observing a copy of a common fair bit selects that bit while intervention removes its incoming edge without changing the other copied outcome](../../figures/assets/M04/M04-16-condition-versus-do.svg)
  <figcaption>This example assumes a structure with a fair bit Z and X=Z, Y=Z. Observing X=1 selects units with Z=1, so Y is also 1. The intervention do(X=1) removes only the Z→X path, leaving the equation Y=Z and the distribution of Z unchanged, so the probability of Y=1 is 0.5. The observational contrast is 1, but the intervention contrast is 0. This deterministic example is not used as an example of positivity for adjustment.</figcaption>
</figure>

## Core concept 3. A confounder mixes another path into the observed difference

If $Z$ is a common cause of $X$ and $Y$, the graph is

\[
X\leftarrow Z\to Y
\]

The distribution of $Z$ can already differ between groups compared at different observed values of $X$. The observational association then mixes the effect of $X$ with differences caused by $Z$.

Under appropriate conditions, adjusting for a measured confounder $Z$ identifies the intervention mean as

\[
\mathbb E[Y\mid\operatorname{do}(X=x)]
=
\sum_z
\mathbb E[Y\mid X=x,Z=z]p(z)
\]

This equation requires exchangeability, meaning that all relevant confounders have been measured; positivity, meaning that both treatments can be observed at each possible $z$; and consistency, connecting the observed treatment with its potential outcome.

Here, we average over discrete $Z$ using a sum. Decomposing the observed group mean gives $\mathbb E[Y\mid X=x]=\sum_z\mathbb E[Y\mid X=x,Z=z]p(z\mid X=x)$. Instead of these group-specific weights, the adjustment formula uses $p(z)$ for a common target population. Under the condition that treatment comparisons are appropriate within the same $z$, we obtain each conditional mean and average them again using a common reference distribution.

Exchangeability assumes that potential outcomes do not differ systematically with treatment selection within the same $z$. Without positivity, the treatment mean for some $z$ cannot be calculated from the data. Without consistency, an observed outcome may not represent the defined intervention outcome. Merely including $Z$ in a regression equation does not establish these conditions.

Judge a variable's role by the assumed arrow directions, not by its name or position in the diagram.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Confounder fork with direct treatment effect mediator chain and collider converging arrows show three distinct variable roles](../../figures/assets/M04/M04-16-three-causal-roles.svg)
  <figcaption>On the left, Z is a common cause of treatment X and outcome Y, and there is also an X→Y path. In the middle, M lies on an intermediate path transmitting a change in X to Y. On the right, C is an outcome jointly produced by X and Y. Being a variable placed in the middle does not mean that all three should be controlled in the same way.</figcaption>
</figure>

Adjustment recombines conditional means using the proportions of the same target population.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Confounder distributions differ across observed treatment groups while common target weights reduce an observed outcome contrast to the adjusted causal contrast](../../figures/assets/M04/M04-16-adjustment-weights.svg)
  <figcaption>This construction has p(Z=1)=0.5 and treatment probabilities of 0.2 at Z=0 and 0.8 at Z=1. With outcome mean 0.1+0.2X+0.5Z, the observed means are 0.2 and 0.7. Averaging again with the same p(Z)=(0.5,0.5) gives 0.35 and 0.55. The contrast 0.2 is interpreted as an intervention effect under the conditions that both treatments are possible at both Z values and Z includes all common causes in this model.</figcaption>
</figure>

## Core concept 4. A mediator lies on a path through which an effect passes

In the structure

\[
X\to M\to Y
\]

$M$ is a mediator. There is an indirect path: $X$ changes $M$, and $M$ changes $Y$. If there is also a direct arrow from $X$ to $Y$, the total effect includes both the direct path and the mediated path.

Simply controlling the mediator $M$ when the target is the total effect blocks part of the $X\to M\to Y$ path. To separate direct and indirect effects, specify which interventions are being compared and the additional identification assumptions. The rule “include every relevant variable in the regression” is not safe.

In the two interventions defining a total effect, $M$ is allowed to change as a result of changing $X$. If the comparison fixes $M$ at the same value, that change cannot propagate to $Y$, so the comparison asks a different question. Conditioning on people with the same observed $M$ generally also differs from an intervention that actually fixes $M$. Calling a coefficient obtained by including a mediator in a regression a direct effect requires identification conditions that connect these different comparisons.

Compare letting the mediator follow the treatment with fixing it externally, using the same generative equations.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Treatment changes propagate through a deterministic mediator but fixing that mediator removes the propagation and changes the intervention contrast](../../figures/assets/M04/M04-16-mediator-fixed-versus-following.svg)
  <figcaption>In the assumed structure M=2X, Y=M, changing X from 0 to 1 changes M and Y from 0 to 2. The lower panel shows a different intervention, do(M=0), which removes the X→M path. Changing X alone then leaves Y at 0. This is not a diagram of a regression result obtained by selecting units with observed M=0.</figcaption>
</figure>

## Core concept 5. Conditioning on a collider can create an association

In the structure

\[
X\to C\leftarrow Y
\]

$C$ is a collider. Even if $X,Y$ are marginally independent, selecting on their common outcome $C$ can create dependence.

For example, suppose that both skill $X$ and luck $Y$ increase the chance of admission $C$. Among admitted applicants, someone with low skill is more likely to have compensated with high luck. A negative association between skill and luck can appear because admission, a selection variable, has been fixed. Collider adjustment can create new bias rather than reduce bias.

Calculate the structure in Example 3 using two independent fair bits. If $C=1$ whenever either $X$ or $Y$ is 1, the four original pairs each have probability $1/4$. Conditioning on $C=1$ excludes $(0,0)$ and renormalizes the remaining three pairs to $1/3$ each. Thus, $P(Y=1\mid C=1)=2/3$, but $P(Y=1\mid X=0,C=1)=1$. Within the conditional group, the independence condition that knowing $X$ leaves the probability of $Y$ unchanged no longer holds.

Check directly which pair selection removes and how the remaining pairs are renormalized.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Conditioning independent fair bits on their OR outcome removes one pair and renormalizes three remaining pairs causing dependence](../../figures/assets/M04/M04-16-collider-selection.svg)
  <figcaption>This is the C=X OR Y example from the text. The four original pairs each have probability 1/4. Conditioning on C=1 excludes (0,0) and gives each remaining pair probability 1/3. As a result, P(Y=1∣C=1)=2/3 differs from P(Y=1∣X=0,C=1)=1, so independence no longer holds within the conditional group.</figcaption>
</figure>

## Core concept 6. Potential outcomes define the causal effect to be compared

Let the binary treatment be $T\in\{0,1\}$. The potential outcomes for unit $i$ are

\[
Y_i(1),\qquad Y_i(0)
\]

The individual causal effect is $Y_i(1)-Y_i(0)$, but only one of these two outcomes is observed for each unit. This is called the fundamental problem of causal inference.

The population average treatment effect is

\[
\operatorname{ATE}
=\mathbb E[Y(1)-Y(0)]
\]

A causal question must include the treatment version, the outcome measurement time, and the target population for this estimand to be clear.

Under consistency, the observed outcome can be written as $Y=TY(1)+(1-T)Y(0)$. This leaves $Y(1)$ for a unit with $T=1$ and $Y(0)$ for a unit with $T=0$. The ATE averages the difference between two states of the same unit over the population, so by linearity it equals $\mathbb E[Y(1)]-\mathbb E[Y(0)]$. Whether the difference between the means of distinct observed groups represents these two potential-outcome means requires separate checks of assignment and identification conditions.

Distinguish a unit's two potential states from the one observed value selected by its actual treatment.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![A constructed four unit potential outcome schedule highlights only the treatment selected observed outcome while unobserved counterfactual cells remain dashed](../../figures/assets/M04/M04-16-potential-outcome-selection.svg)
  <figcaption>This is a constructed schedule of four units with both potential outcomes specified for explanation. Only one blue cell is observed for each unit according to the actual treatment T; the other cell is counterfactual. Each unit's effect is 2, but the observed difference in means for this assignment, which treats the high-baseline units 3 and 4, is 6. This does not mean that both states were observed simultaneously in actual data.</figcaption>
</figure>

## Core concept 7. Random assignment creates comparable groups

In a randomized experiment, assigning treatment $T$ independently of the potential outcomes gives

\[
T\perp\!\!\!\perp (Y(1),Y(0))
\]

In a sufficiently large sample, treatment and control groups become similar on average in measured and unmeasured pretreatment causes.

Under consistency, no interference between units, and an appropriate random assignment design with neither group empty, the difference in means estimates the average treatment effect.

\[
\widehat{\operatorname{ATE}}
=\overline Y_{T=1}-\overline Y_{T=0}.
\]

Random sampling concerns generalization to a population. Random assignment concerns causal comparisons between groups. Neither substitutes for the other.

Independent assignment and consistency give $\mathbb E[Y\mid T=t]=\mathbb E[Y(t)\mid T=t]=\mathbb E[Y(t)]$ for each $t=0,1$. The first equality connects the observed outcome to the outcome under the corresponding state. The second uses the condition that assignment does not select potential outcomes. The difference between the two population group means therefore equals the ATE. Random assignment establishes this probabilistic comparability, but it does not mean that all pretreatment variables are exactly balanced in a realized small sample.

In a design that fixes positive treatment and control group sizes within a fixed enrolled sample and draws uniformly from the possible assignments, the sample difference in means above is unbiased for that sample's average causal effect. Unbiasedness for the target population's ATE and generalization also depend on how the sample was selected. Distinguish the stages at which sampling and assignment randomization are used.

Holding the enrolled units fixed and repeating the possible assignments separates assignment uncertainty from the sample causal effect.

<figure class="lesson-figure" markdown="1">
  ![All six uniform two treated assignments of four fixed units give a mean contrast distribution centered on the sample average treatment effect](../../figures/assets/M04/M04-16-random-assignment-distribution.svg)
  <figcaption>All six assignments that select two of the preceding four units for treatment are calculated with equal probability. The observed differences in means are −2,0,2,4,6, with 2 occurring in two assignments. The mean of the assignment distribution is the sample ATE=2, but an individual assignment does not guarantee balance or the exact effect value. Generalization to the target population has not been established separately here.</figcaption>
</figure>

## Core concept 8. A regression coefficient is not a causal effect without a design

In the regression equation

\[
Y=\beta_0+\beta_1X+\boldsymbol\gamma^\top\boldsymbol Z+\varepsilon
\]

$\beta_1$ represents a conditional association that depends on the model and the adjustment set. Interpreting it as a causal effect requires assumptions about temporal order, confounding control, correct functional form, measurement, and selection.

High predictive accuracy has the same limitation. A feature that predicts a future outcome well need not be a manipulable cause. A disease marker can be useful for diagnosis without implying that changing the marker itself will treat the disease.

## Core concept 9. Model interpretation separates observational evidence from intervention evidence

If a concept $C$ can be decoded well from an activation $H$, this shows an association or available information between $H$ and $C$. Concluding that the model output $Y$ uses this information requires an intervention on $H$.

Ablation, activation patching, and steering are candidate interventions. If an intervention creates an off-distribution state or changes several features at once, however, the observed output change is difficult to interpret as the effect of the target concept alone. Matched control directions, dose-response, specificity, restoration, and checks across multiple inputs and models are needed.

A necessity claim asks whether removing a component impairs a function. A sufficiency claim asks whether the component or signal alone can restore that function. Correlation, necessity, and sufficiency provide different kinds of evidence.

The output effect of removing and restoring a readable coordinate depends on the actual computation path.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![The same readable hidden coordinate has no ablation effect in a function ignoring it but changes and restores output in a function using it](../../figures/assets/M04/M04-16-decodable-versus-used.svg)
  <figcaption>The same h=(a,b)=(1,2) is supplied to two known toy functions. The coordinate a is readable in both cases, but removing and restoring it leaves the output at 2 for y=b. For y=a+b, setting a to 0 changes the output from 3 to 2, and restoring it returns the output to 3. These are not measurements from an actual neural model and do not replace checks of intervention validity, specificity, and off-distribution effects in real settings.</figcaption>
</figure>

## Example 1. An association created by a common cause

Suppose temperature $Z$ increases both ice cream sales $X$ and swimming accidents $Y$.

\[
X\leftarrow Z\to Y
\]

Sales and accidents can increase together, but this does not establish that an intervention reducing ice cream sales will reduce accidents. Comparisons within temperature levels or an appropriate causal design are needed.

## Example 2. Observational and randomized contrasts

Suppose the treatment group's mean outcome is $8$ and the control group's is $5$. Under random assignment and consistency, the estimate is

\[
\widehat{\operatorname{ATE}}=8-5=3
\]

In an observational study in which patients choose treatment themselves, confounders such as severity can contribute to the group difference, so the same $3$ cannot immediately be called a causal effect.

## Example 3. Collider selection

Suppose selection $C=1$ occurs whenever either of two independent causes $X,Y$ is high. In the full population, $X,Y$ can be independent. Among people with $C=1$, however, a person with $X=0$ is more likely to need $Y=1$ to be selected. In a sample conditioned on selection, $X,Y$ can be negatively associated.

## Example 4. A probe and an activation intervention

Suppose a topic label is decoded from a layer activation with $95\%$ accuracy. This result supports the decodability of topic information. If removing the topic direction selectively worsens relevant answers while leaving unrelated control tasks intact, and patching the original activation restores performance, this provides stronger evidence of functional use.

It is still necessary to check whether the intervention direction also changes features other than topic and whether the effect holds across multiple prompts and seeds.

## Common misconceptions

### Misconception 1. Correlation of 0 means no causal effect

There may be a nonlinear relation or subgroup effects that cancel each other. Zero correlation is a result about linear marginal association.

### Misconception 2. A feature that predicts an outcome well causes that outcome

A predictive feature can be a consequence of a cause, an indicator of a common cause, or a selection artifact. Predictive performance alone does not determine an intervention effect.

### Misconception 3. Controlling more variables improves a causal estimate

Confounder adjustment can be necessary, but indiscriminately controlling mediators or colliders can block the target effect or create bias.

### Misconception 4. A randomized experiment generalizes to every population

Random assignment supports internal causal comparisons within the enrolled sample. Generalization to a target population requires separate consideration of sampling and effect heterogeneity.

### Misconception 5. An activation intervention that changes the output establishes the target concept's effect

An intervention can also change other features and the distribution. Specificity controls and intervention validity must be checked.

## Exercises

### 1. Observational and intervention conditions

Explain the difference between $\mathbb E[Y\mid X=1]$ and $\mathbb E[Y\mid\operatorname{do}(X=1)]$.

<details>
<summary>Show solution</summary>

The first term is a conditional mean obtained by observing units with $X=1$. The second is the mean in an intervention world where $X$ is externally set to 1. These values can differ under confounding or selection.

</details>

### 2. Finding a confounder

A graph has the arrows $Z\to X$, $Z\to Y$, and $X\to Y$. State the role of $Z$ when estimating the total effect of $X$.

<details>
<summary>Show solution</summary>

$Z$ is a confounder: a common cause of $X,Y$. It creates the backdoor path $X\leftarrow Z\to Y$. Under exchangeability, positivity, and consistency, and with $Z$ measured accurately, adjusting for $Z$ can block this path.

</details>

### 3. Controlling a mediator

The target is the total effect of $X$ in a graph containing only $X\to M\to Y$. Determine whether a comparison fixing $M$ gives the total effect.

<details>
<summary>Show solution</summary>

Fixing $M$ blocks the mediated path $X\to M\to Y$. Since the entire effect passes through that path in this graph, a comparison controlling $M$ removes the total effect. The direct effect and the total effect are different estimands.

</details>

### 4. Collider bias

Suppose $X\to C\leftarrow Y$ and $X,Y$ are marginally independent. Explain what can happen when the analysis conditions on $C$.

<details>
<summary>Show solution</summary>

$C$ is a collider. Conditioning on $C$ can open a previously closed path and create an association between $X,Y$. Thus, including $C$ as an adjustment variable cannot be assumed to reduce bias.

</details>

### 5. A randomized difference in means

In an experiment with random assignment, the treatment group's mean outcome is $0.72$ and the control group's is $0.65$. Find the estimated ATE and state the conditions needed for its interpretation.

<details>
<summary>Show solution</summary>

\[
\widehat{\operatorname{ATE}}=0.72-0.65=0.07.
\]

Random assignment, agreement between the assigned treatment and the received intervention, and no interference between units are needed. Generalization to a target population also requires a separate check of the sampling design.

</details>

### 6. Prediction and causation

A biomarker is found to predict a disease with $99\%$ accuracy. Evaluate whether this establishes that lowering the biomarker will reduce disease risk.

<details>
<summary>Show solution</summary>

It does not. The biomarker can be a consequence of a disease cause or an indicator of a common cause. Evaluating its causal effect requires an intervention that specifies biomarker manipulation and a design that controls confounding.

</details>

### 7. Critiquing a model interpretation claim

A linear probe classifies sentiment from an activation with high accuracy. The researcher claims, “This layer uses sentiment to produce its output.” Propose the next experiments needed.

<details>
<summary>Show solution</summary>

First, check whether decodability is stable on held-out data and control labels. Next, remove, replace, or adjust sentiment-related activations and measure the effects on relevant outputs. Use random directions or norm-matched directions as controls, and check damage to unrelated tasks. Dose-response, activation restoration, and repetition across multiple prompts and model seeds strengthen a functional-use claim.

</details>

## Lesson summary

- Association concerns observed dependence; causation concerns changes under intervention.
- Observational conditioning on $X=x$ generally differs from the intervention $\operatorname{do}(X=x)$.
- A confounder is a common cause of treatment and outcome and an appropriate adjustment target.
- A mediator lies on an effect path, and conditioning on a collider can create a new association.
- Potential outcomes specify the causal estimand to be compared.
- Random assignment makes treatment groups comparable in terms of their potential outcomes.
- Regression coefficients and predictive accuracy do not establish causal effects without design assumptions.
- Model interpretation must distinguish evidence of decodability, necessity, and sufficiency.

## Pass criteria

You pass if you can answer these questions without consulting the material.

- Can you distinguish association, prediction, and causation?
- Can you explain the difference between conditioning and intervention notation?
- Can you identify confounders, mediators, and colliders in a graph?
- Can you distinguish when adjustment is needed from when it is harmful?
- Can you define the ATE using potential outcomes?
- Can you distinguish the roles of random sampling and random assignment?
- Can you limit a claim to what a probe or intervention result supports?

## Next lesson

- [M04-17 Experimental design and reproducibility](M04-17-experimental-design-reproducibility.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Association, prediction, and causation are distinguished.
- [x] Conditioning and intervention are distinguished.
- [x] Confounders, mediators, and colliders are explained using graphs.
- [x] Potential outcomes and the ATE are defined.
- [x] The role of random assignment is stated.
- [x] Activation observations and intervention evidence are distinguished.
- [x] Every exercise has a solution.
- [x] The strength of model interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
