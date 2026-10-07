---
id: "A09-CAU-02"
title: "The do-operator and interventions"
part: 4
stage: "A09-CAU"
status: "complete"
prerequisites: ["M04-16", "I07-05", "A09-CAU-01"]
estimated_time: "90–120 minutes"
---

# A09-CAU-02. The do-operator and interventions

## Why this lesson matters

Conditioning selects an observed subset; an intervention changes a structural equation. To interpret activation ablation or patching as a causal experiment, specify which equation was replaced and what rule generates the replacement value.

## Learning objectives

- Distinguish $P(Y\mid X=x)$ from $P(Y\mid\operatorname{do}(X=x))$.
- Express a surgical intervention as equation replacement.
- Apply truncated factorization to a simple DAG.
- Specify the intervention policy for activation patching.

## Prerequisite check

- Prerequisite lessons: [M04-16 Correlation and causation](../../part-1-foundations/M04/M04-16-correlation-causation.md), [I07-05 Observation and intervention](../../part-3-interpretability/I07/I07-05-observation-intervention.md), [A09-CAU-01 Structural causal models](A09-CAU-01-structural-causal-models.md)
- Check question: Why is selecting only samples with $X=x$ different from replacing the $X$ equation of every unit with the constant $x$?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\operatorname{do}(X=x)$ | `do X equals x` | An intervention replacing the $X$ equation with the constant $x$ | operation |
| $P(Y\mid\operatorname{do}(X=x))$ | `the distribution of Y under do X equals x` | The interventional outcome distribution | probability distribution |
| $\mathcal M_x$ | `the intervened model M sub x` | The SCM after applying $\operatorname{do}(X=x)$ | model object |
| $\tau(s)$ | `tau of source s` | A patch policy determining the replacement activation value from a source | map |

## Core concepts

### Replacing one mechanism

The intervention $\operatorname{do}(X=x)$ replaces the original equation

$$
X=f_X(\operatorname{pa}_X,U_X)
$$

with $X:=x$, while preserving the other equations and the exogenous joint distribution $P_U$. The new equation no longer reads the original parents or $U_X$, so incoming edges into $X$ are removed. Downstream equations using $X$ stay in place and compute with the new value $x$. Removing outgoing edges as well, or holding downstream activations at their original values, is therefore a different operation.

Preserving the other mechanisms means preserving their functional forms. Their input and output values may change because of the intervention. This is why the downstream forward pass is recomputed after patching $X$.

The two figures distinguish removing incoming relationships into X from recomputing downstream values using the new X.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The do X equals x graph removes the incoming Z-to-X dependence while preserving Z-to-Y and X-to-Y, and replaces only the X equation.](../../figures/assets/A09-CAU/A09-CAU-02-surgical-edge-removal.svg)

<figcaption>On the right, the generating rule for X becomes the constant X:=x, removing Z→X. The new equation no longer reads U_X either. Z→Y and X→Y remain, so Y is recomputed from the new X and the original background. Gray dashed lines and red × marks show the removed relationships for comparison.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![For the same background Z equals zero, U sub X equals one and U sub Y equals zero, replacing X with two changes Y from one to two without changing its equation.](../../figures/assets/A09-CAU/A09-CAU-02-downstream-recalculation.svg)

<figcaption>With the same background Z=0, U_X=1, and U_Y=0, the original values are X=1 and Y=1. After X:=2, the function Y=X+Z+U_Y stays the same, but its changed input X gives a recomputed Y=2. Preserving the other mechanisms does not mean freezing downstream values at their original levels.</figcaption>

</figure>

### Selected units versus a changed mechanism

Conditioning $P(Y\mid X=x)$ selects units with $X=x$ in the original data-generating process. This selection can change the distribution of background variables from $P_U$ to $P_U(\cdot\mid X=x)$. Under intervention, units are still drawn from $P_U$, and only the $X$ mechanism is replaced. The difference between the two distributions lies less in the value of $X$ itself than in the process that produced that value.

For example, consider an acyclic model with $Z\to X$, $Z\to Y$, and $X\to Y$, and assume that the noise variables for its nodes are mutually independent. When the required $(x,z)$ combinations lie in the observational support, so that the conditional outcomes can be defined, observation and intervention for discrete variables can be compared as

$$
P(y\mid X=x)=\sum_zP(y\mid x,z)P(z\mid X=x),
\qquad
P(y\mid\operatorname{do}(X=x))=\sum_zP(y\mid x,z)P(z)
$$

The first expression averages using the proportions of $Z$ among selected units; the second uses the proportions of $Z$ in the original population. Even with the same conditional outcomes, different averaging weights can give different results. The results can also agree, for example when $X$ is already independent of the background variables affecting the outcome.

### Conditions and substitution for truncated factorization

In an acyclic SCM with mutually independent exogenous noise for its nodes, the joint distribution can be written as a product of conditional probabilities given parents. The distribution after replacing the $X$ equation is obtained by removing the factor for $X$ and substituting $X=x$ into the parent values of the remaining factors. To read these conditional probabilities from the observational distribution, assume that the parent combinations needed after intervention also have observational support. Writing $V_{-X}$ for the collection of endogenous variables other than $X$ gives

$$
P(V_{-X}=v_{-X}\mid\operatorname{do}(X=x))
=\left.\prod_{i:V_i\ne X}P(v_i\mid\operatorname{pa}_i)\right|_{X=x}
$$

To include $X$ itself in the joint distribution, add a factor assigning probability 1 to $X=x$. In the $Z,X,Y$ example, only $P(x\mid z)$ is removed from $P(z)P(x\mid z)P(y\mid x,z)$, leaving $P(z)P(y\mid x,z)$. Summing over $z$ gives the distribution of $Y$.

An arbitrary factorization obtained from the probability chain rule does not justify this equation replacement. If observed variables have a hidden common cause, do not simply use the conditional factors of a DAG that omits it. Moreover, the conditional outcome at an unobserved $(x,z)$ combination cannot be estimated from observational data alone. Computing this expression from the observational distribution therefore also requires checking support for those combinations.

Compare factor removal separately from the support of parent combinations required by the intervention.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The causal product P z times P x given z times P y given x,z loses only the X factor after do X equals x; the fixed value remains in the Y factor.](../../figures/assets/A09-CAU/A09-CAU-02-truncated-factorization.svg)

<figcaption>Remove P(x|z) from the three factors of the original causal factorization, then substitute the fixed value x for parent X in the remaining Y factor. The resulting expression, P(z)·P(y|x,z), is the joint distribution of Z and Y, excluding X. Calculating it from observational conditionals requires both the acyclic SCM with independent noise and support for the required parent combinations.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![The binary SCM joint support lacks the required cell X equals two and Z equals zero, so its observational conditional cannot supply the intervention outcome even though a known equation can compute it.](../../figures/assets/A09-CAU/A09-CAU-02-missing-parent-support.svg)

<figcaption>The cell X=2, Z=0 has probability zero in the observational joint distribution. Z=0 remains possible after do(X=2), so the outcome for that combination is needed, but the data cannot supply the observational conditional P(Y|X=2,Z=0). The small example in the text directly computes this combination using the known Y equation, distinguishing that calculation from observational identification.</figcaption>

</figure>

### A policy that generates patch values

Activation patching may hold $H:=h$ fixed, or insert $H:=\tau(s)$ by applying alignment and scale correction to an activation obtained from source prompt $s$. With $s$ fixed in a single run, this is a constant replacement. In an experiment averaging over multiple sources, however, the source selection distribution and pairing with the target are also part of the policy. Different source draws measure different effects even at the same target node.

Fix the token position, layer, head, and the time when the hook is applied, then recompute downstream of the replaced node. If the policy also reads other variables from the target run, specify those dependencies. Its new equation may introduce new incoming dependencies, so the description of constant do as removing all incoming edges cannot simply be carried over. If only some coordinates are replaced, the intervention specification must also include the rule for preserving the others.

The generation of patch values, new parent dependencies, and the source selection distribution answer different questions.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An illustrative source activation two,four is reordered to four,two and scaled to two,one before replacing target activation nine,eight through tau of s.](../../figures/assets/A09-CAU/A09-CAU-02-source-alignment-scale-policy.svg)

<figcaption>The illustrative policy τ reorders source activation (2,4)ᵀ into (4,2)ᵀ, then multiplies it by 0.5 to insert (2,1)ᵀ at the target hook. This is an example of including alignment and scale correction in τ, not a result from a particular model in this lesson. Specify the source prompt, target pairing, and hook where recomputation starts as well.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A fixed H equals h replacement has no incoming parent use, while a policy tau of source S and target variable T introduces S-to-H and T-to-H dependencies.](../../figures/assets/A09-CAU/A09-CAU-02-constant-and-conditional-policy.svg)

<figcaption>The constant replacement on the left does not read the original parent values. On the right, a policy reading source S and target-run variable T to produce H:=τ(S,T) introduces incoming dependencies S→H and T→H. Rather than carrying over the constant-do description of removing all incoming edges, specify the policy inputs in the graph and equation.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Illustrative source selection probabilities three-quarters and one-quarter induce a first patched-coordinate distribution with values two and four under the same tau map.](../../figures/assets/A09-CAU/A09-CAU-02-source-mixture-patch-values.svg)

<figcaption>Select sources s₁=(2,4)ᵀ and s₂=(4,8)ᵀ with probabilities 0.75 and 0.25, then apply the same reordering and 0.5 scaling to obtain patch values (2,1)ᵀ and (4,2)ᵀ. The figure shows only the probabilities for the first patch coordinate. This selection distribution is part of the policy in experiments averaging over multiple sources; the figure does not show an actual output effect.</figcaption>

</figure>

## Small example

Use $Z=U_Z$, $X=Z+U_X$, and $Y=X+Z+U_Y$. Let $U_Z,U_X$ be independent, each taking zero and one with equal probability, and set $U_Y=0$. Among units observed to have $X=2$, only $Z=1$, $U_X=1$ is possible, so $Y=3$.

Under $\operatorname{do}(X=2)$, $Z$ still takes zero and one with equal probability. Since $Y=2+Z$, the outcome is 2 or 3, with mean 2.5. The observational mean, 3, differs from the interventional mean, 2.5, because observational selection changes the proportions of $Z$. This model was calculated by replacing the actual $X$ equation, not by estimating the outcome for the absent combination $(X=2,Z=0)$ from observational data alone.

Compare conditioning and intervention in the same background coordinates, then calculate the outcome distributions.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Four equally likely binary background pairs generate the original process; conditioning on X equals two selects only one pair, while do X equals two retains all four backgrounds.](../../figures/assets/A09-CAU/A09-CAU-02-selected-versus-set-backgrounds.svg)

<figcaption>With independent binary U_Z and U_X, each assigning probability 0.5 to zero and one, the four original background combinations have probability 0.25 each. Observing X=2 retains only (1,1), whereas do(X=2) preserves all four backgrounds and replaces only the X equation. Y on the right takes values 2 and 3, calculated directly from the known SCM.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![The known binary SCM gives outcome Y equals three with probability one under observation X equals two, versus outcomes two and three with probability one-half under do X equals two.](../../figures/assets/A09-CAU/A09-CAU-02-conditional-intervention-outcomes.svg)

<figcaption>Selection by observing X=2 assigns probability 1 to Y=3, giving mean 3. do(X=2) preserves the original proportions of Z, assigning probability 0.5 each to Y=2 and Y=3, with mean 2.5. These numbers were calculated by changing an equation in the SCM in the text, not estimated from observational conditionals alone.</figcaption>

</figure>

## Common misconceptions

- Saving and inspecting activations is observation, not intervention.
- The effect of patching several nodes simultaneously cannot be taken as the sum of their individual effects.

## Exercises

### 1. Edge removal
Which edge is removed after $\operatorname{do}(X=x)$ in the graph $Z\to X$, $Z\to Y$, $X\to Y$?
<details><summary>Show solution</summary>

The incoming edge $Z\to X$ into $X$ is removed. $X\to Y$ and $Z\to Y$ remain.
</details>

### 2. Factorization
Starting from $P(z,x,y)=P(z)P(x\mid z)P(y\mid x,z)$, write the factorization after $\operatorname{do}(X=x)$.
<details><summary>Show solution</summary>

$P(z,y\mid\operatorname{do}(x))=P(z)P(y\mid x,z)$.
</details>

### 3. Policy
Express in one line an intervention that inserts the layer 5 activation from a clean prompt into a corrupted prompt.
<details><summary>Show solution</summary>

Specify both source and target, as in $H_5(\text{corrupted}):=H_5(\text{clean})$.
</details>

### 4. Model interpretation
What can you conclude if zero ablation and mean ablation have different effects?
<details><summary>Show solution</summary>

The effect is sensitive to the intervention value. Report the effect of each intervention policy separately rather than combining them into one causal effect of the component.
</details>

## Sources and update boundaries

The do-operator assumes modular replacement of structural equations. Actual neural interventions can produce off-manifold states and changes through downstream normalization, so intervention validity must be diagnosed separately.

Equation replacement and the independent-noise condition for truncated factorization were checked against Sections 3.2.1–3.2.3, particularly Corollary 1, of [Pearl, An Introduction to Causal Inference](https://ftp.cs.ucla.edu/pub/stat_ser/r354-reprint-corrected.pdf). The binary example above directly computes the specified SCM.

## Lesson summary

- Conditioning selects units; a do-intervention replaces an equation.
- A surgical intervention cuts incoming edges into the target node.
- Truncated factorization removes the intervention target's conditional factor.
- Patching is defined by a policy including source, target, and alignment.

## Pass criteria

- Can you distinguish conditional and interventional distributions?
- Can you express an internal patch as reproducible equation replacement?

## Next lesson

- [A09-CAU-03 Confounding and identifiability](A09-CAU-03-confounding-identifiability.md)

## Author checklist

- [x] Connected the do-operator, truncated factorization, and patch policies.
- [x] All four exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Checked prerequisites and links.

