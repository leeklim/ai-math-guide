---
id: "I07-04"
title: "Perturbation Attribution"
part: 3
stage: "I07"
status: "complete"
prerequisites: ["I07-03"]
estimated_time: "90–120 minutes"
---

# I07-04. Perturbation Attribution

## Why this lesson matters

Perturbation attribution masks features or replaces them with other values, then measures the output difference. It requires no differentiation and answers questions about finite changes, but its results depend on the replacement values and the order in which interactions are disrupted. In natural language, deleting a token can itself change grammar and length.

## Learning objectives

- Calculate the effect of perturbing a single feature.
- Explain the differences between zero, mean, and resampled baselines.
- Construct an example where interactions make the sum of individual effects differ from the overall effect.
- Propose checks for whether an input has moved outside the distribution.

## Prerequisite check

- Prerequisite lesson: [I07-03 Integrated gradients and baselines](I07-03-integrated-gradients-baseline.md)
- Check question: Why does changing the baseline change which score difference is being explained?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $x^{(i\leftarrow b_i)}$ | `x with coordinate i replaced by b sub i` | Input with feature $i$ replaced by its baseline | $\mathbb R^d$ |
| $\Delta_i$ | `delta sub i` | Score difference from a single perturbation | scalar |
| occlusion | `occlusion` | Intervention masking or replacing a feature | operation |
| resampling | `resampling` | Method drawing replacement values from a reference distribution | stochastic operation |
| interaction | `interaction` | Property of feature effects not adding together | joint effect |

## 1. The basic effect

$$
\Delta_i(x;b_i)
=
f(x)-f\bigl(x^{(i\leftarrow b_i)}\bigr).
$$

The two runs retain the same function and all other coordinates, changing only coordinate $i$. This is a finite difference obtained by evaluating the function again on the replacement input, not an approximation formed by multiplying a derivative by a displacement. The formula subtracts the score after replacement from the original score. If replacement raises the score, $\Delta_i$ is therefore negative.

If $\Delta_i>0$, the original feature increased the score under that replacement rule. This does not mean that the feature has a context-independent value.

The following slice compares finite differences for different replacement values relative to the original score.

<figure class="lesson-figure" markdown="1">

![Worked exercise score two x one plus four has original input three score ten while replacing x one by zero two or four yields score four eight or twelve and signed original minus replacement effects six two or minus two](../../figures/assets/I07/I07-04-replacement-comparisons.svg)

<figcaption>The original x₁ = 3 is fixed in the exercise's f = 2x₁ + x₂ with x₂ = 4. Replacements of 0 and 2 give effects of 6 and 2. Replacing it with the illustrative comparison value 4 raises the replacement score and gives an effect of −2.</figcaption>

</figure>

## 2. Replacement values define the question

- Zero: Simple to calculate, but it may not be an actual input.
- Mean: Compares with an average state, but it can be unrepresentative in a multimodal distribution.
- Marginal resampling: Follows the marginal distribution, but it can break relationships with other features.
- Conditional resampling: Attempts to preserve context, but it requires a separate generative model.

Token deletion, a mask token, whitespace, and replacement with another token are different interventions.

Marginal resampling draws from a feature's marginal distribution without examining the rest of the input. Conditional resampling draws from its conditional distribution with the other features fixed as in the current input. Even when changing the same feature, the two methods create different joint states. Using a conditional distribution does not guarantee that the same information as in the original input is removed. Which information remains after replacement depends on dependencies with other features.

With random replacement, the same input can yield a different score difference on each draw. Averaging across draws gives the mean effect under the specified replacement distribution. Distinguish this from independent repetitions used to assess generalization across different inputs.

The next two figures show different joint states arising from conditioning the replacement distribution and changing token positions.

<figure class="lesson-figure" markdown="1">

![Illustrative correlated input cloud near the x two equals x one diagonal contrasts marginal replacement x one values spread along fixed x two one point five with conditional replacement values concentrated near the compatible cloud](../../figures/assets/I07/I07-04-marginal-conditional-draws.svg)

<figcaption>The illustrative distribution has x₂ ≈ x₁, with x₂ fixed at 1.5. The upper marginal draws ignore x₂ and can move far from the joint distribution. The lower conditional draws sample x₁ near values compatible with this x₂. These are not observations from an actual model or input dataset.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Illustrative token sequence I like this book loses the third token on deletion and book shifts from position four to three while a mask replacement keeps four positions](../../figures/assets/I07/I07-04-token-delete-replace.svg)

<figcaption>The comparison uses four illustrative tokens. Deletion moves the following token book from position 4 to 3, while replacement retains position 3. Being able to use the replacement symbol [mask] does not guarantee that the model was trained with that token.</figcaption>

</figure>

## 3. Interactions

For $f(x_1,x_2)=x_1x_2$, the score at $(1,1)$ is 1. Replacing either coordinate with 0 gives an effect of 1, so the sum of individual effects is 2. This exceeds the overall effect of 1 from removing both together. The same interaction has been counted twice.

Sequential removal changes the sum. Removing the first coordinate first lowers the score from $1\to0$; removing the second from that state leaves it at $0\to0$. The two differences sum to 1, but the allocated values are $(1,0)$. Reversing the order gives $(0,1)$. Successive score differences telescope to the overall difference, while how much is allocated to each feature depends on removal order.

The coordinate paths below show which feature first eliminates the score under each removal order.

<figure class="lesson-figure" markdown="1">

![Binary coordinate grid of product x one x two shows red removal of x one then x two and blue removal of x two then x one from one one to zero zero with scores one at the start and zero at other states](../../figures/assets/I07/I07-04-sequential-removal-paths.svg)

<figcaption>The two paths go from score 1 at (1, 1) to score 0 at (0, 0). The first removal eliminates the entire product term, so sequential allocation is (1, 0) or (0, 1), with a total decrease of 1 along each path. This differs from the sum of 2 obtained by measuring both single removals separately from the original point.</figcaption>

</figure>

## 4. CPU lab

<!-- I07_EXAMPLE: i07_04_perturbation_attribution -->

Check that the individual feature effects differ between a zero baseline and a mean-like baseline. Neither is automatically designated as the correct answer.

The following comparison changes only the replacement values in the lab function to obtain single-feature effects.

<figure class="lesson-figure" markdown="1">

![The lab score nine point two five at two three one has single-feature replacement effects nine six zero point two five for zero replacements and four point five four zero for mean-like one replacements](../../figures/assets/I07/I07-04-lab-baseline-effects.svg)

<figcaption>The lab function is 1.5x₁ + x₁x₂ + 0.25x₃² at x = (2, 3, 1), with score 9.25. Coordinatewise zero-replacement effects are (9, 6, 0.25), and mean-like replacements of 1 give (4.5, 4, 0). Each value comes from changing only one coordinate of the original input.</figcaption>

</figure>

## Common misconceptions

### Misconception 1. Perturbations are always more causal than gradients

Values are actually changed, but the intervention target, replacement distribution, and downstream computation must be clear. Output differences for out-of-distribution inputs can differ from the desired causal estimand.

### Misconception 2. Adding individual feature effects gives a complete explanation

With interactions, an additive decomposition does not hold without an ordering or grouping rule.

## Exercises

### 1. Single effect

For $f(x)=2x_1+x_2$ and $x=(3,4)$, calculate the effect of replacing $x_1$ with 0.

<details>
<summary>Show solution</summary>

The original score is 10 and the replacement score is 4, so $\Delta_1=6$.

</details>

### 2. Changing the baseline

What is the effect in the previous problem if $x_1$ is replaced with 2?

<details>
<summary>Show solution</summary>

The replacement score is $2\cdot2+4=8$, so the effect is 2. Even for the same feature, the effect depends on the comparison value.

</details>

### 3. Interaction

Explain why the sum of individual removal effects for $f=x_1x_2$ differs from the joint removal effect.

<details>
<summary>Show solution</summary>

The product term appears once when both features are present. Each individual removal eliminates the same entire product term, so adding them counts the interaction twice.

</details>

### 4. Natural-language intervention

Why are token deletion and replacement with a mask token different experiments?

<details>
<summary>Show solution</summary>

Deletion changes subsequent token positions and sequence length. Mask replacement retains length, but the model may not have been trained with a mask token. They produce different distribution shifts.

</details>

### 5. Controls

Changing a particular token produced a large effect. What matched control could be used?

<details>
<summary>Show solution</summary>

Change another token under the same rule, matching confounders such as position, frequency, and part of speech. A simple random-location control can also be reported.

</details>

### 6. Scope of the claim

Does a large perturbation effect support a claim that the feature is necessary?

<details>
<summary>Show solution</summary>

It provides evidence that the output changed under the specified replacement intervention. To limit a necessity claim, check whether this is a realistic counterfactual removing only the original feature or whether other information was destroyed as well.

</details>

## Sources and update boundaries

[Zeiler and Fergus (2014)](https://arxiv.org/abs/1311.2901) provide a representative early example of masking part of an input to examine prediction changes. This lesson does not fix a particular occlusion value as a universal baseline.

## Lesson summary

- A perturbation effect is the score difference between the original input and an explicitly specified replacement input.
- Replacement values and resampling distributions determine the question.
- Individual effects are not additive when interactions are present.
- Check distribution shifts and matched controls together.

## Pass criteria

- Can you calculate a small perturbation effect?
- Can you explain the advantages and disadvantages of three types of replacement values?
- Can you design an interaction counterexample and controls?

## Next lesson

- [I07-05 Observation and intervention](I07-05-observation-intervention.md)

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] Replacement values and interactions are specified.
- [x] Distribution shifts and controls are included.
- [x] Every exercise has a solution.
- [x] The strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and mathematical rendering have been checked.
