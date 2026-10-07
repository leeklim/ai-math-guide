---
id: "I07-01"
title: "Sensitivity and attribution"
part: 3
stage: "I07"
status: "complete"
prerequisites: ["I06-15", "M03-11"]
estimated_time: "90–120 minutes"
---

# I07-01. Sensitivity and attribution

## Why this lesson matters

The fact that a model's output changes with its input or internal state is different from assigning shares of that output to particular elements as an explanation. Differentiation gives sensitivity to small changes at a point. Attribution additionally requires a baseline, a target output, and an allocation rule. Without this distinction, the magnitude of a gradient can be mistaken for a cause or a contribution.

## Learning objectives

- State local sensitivity and attribution as different questions.
- Specify the scalar output, the analysis site, and the baseline.
- Calculate and compare the gradient and feature-removal effects of a small function.
- Limit claims to what an attribution result supports.

## Prerequisite check

- Prerequisite lessons: [I06-15 Capstone exercise: a representation report](../I06/I06-15-capstone-representation-report.md), [M03-11 Jacobian](../../part-1-foundations/M03/M03-11-jacobian.md)
- Check question: At which point is the gradient of $f:\mathbb R^d\to\mathbb R$ defined, and what is its shape?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $s=f(x)$ | `s equals f of x` | The scalar score to explain | $s\in\mathbb R$ |
| $S_i(x)=\frac{\partial f}{\partial x_i}(x)$ | `S sub i of x equals partial f over partial x sub i at x` | Local sensitivity in the $x_i$ direction | scalar |
| $\phi_i(x;x')$ | `phi sub i of x relative to x prime` | Attribution to feature $i$ relative to baseline $x'$ | scalar |
| target | `target` | The logit, probability, loss, or other output to explain | scalar function |
| baseline | `baseline` | A reference input or state | $x'\in\mathbb R^d$ |

## 1. Fix the question first

Sensitivity asks how much the score changes when $x_i$ changes by a very small amount at the current point $x$.

$$
f(x+\varepsilon e_i)
=
f(x)+\varepsilon S_i(x)+o(\varepsilon)
$$

$e_i$ is the basis vector whose $i$th component is 1 and whose other components are 0. Thus, $x+\varepsilon e_i$ increases only $x_i$ by $\varepsilon$, holding the other coordinates fixed. $S_i(x)$ is the rate of score change per unit change in the input; the actual small change is approximated by $\varepsilon S_i(x)$. The remainder $o(\varepsilon)$ denotes an error that approaches 0 when divided by $\varepsilon$. This is a local approximation at a point where the function is differentiable, not a formula that applies the same rate to a large displacement.

Attribution usually aims to allocate $f(x)$ or $f(x)-f(x')$ among features. The function alone does not determine which allocation is correct. A baseline, a feature unit, and a rule for handling interactions are needed.

## 2. The same function, different answers

$$
f(x_1,x_2,x_3)=x_1x_2+x_3^2
$$

At $x=(2,3,1)$, the gradient is $(3,2,2)$. By contrast, the score decreases from setting each coordinate to 0 are $(6,6,1)$. The gradient is an infinitesimal rate of change, whereas removal measures a finite difference over a move to the distant reference value 0. There is no reason for the values to agree.

The first two partial derivatives are $x_2$ and $x_1$, respectively, and the third is $2x_3$, giving $(3,2,2)$ at this point. The original score is $2\cdot3+1^2=7$. Setting either the first or the second coordinate to 0 removes the entire product term, leaving a score of 1 and a decrease of 6. Setting the third coordinate to 0 leaves a score of 6, a decrease of 1.

The three removal effects sum to 13, but setting all coordinates to 0 together decreases the score by 7. Each individual removal of the first or second coordinate counts the interaction term $x_1x_2$. Listing the effects of removing each coordinate is therefore different from choosing an attribution rule that allocates the total score difference without double counting.

In the linear slice below, read the rate of change and the finite score decrease on different scales.

<figure class="lesson-figure" markdown="1">

![With other coordinates fixed the slice three times x one plus one has slope three at input two while moving the input from two to zero decreases the score from seven to one by six](../../figures/assets/I07/I07-01-linear-coordinate-change.svg)

<figcaption>This slice holds x₂ = 3 and x₃ = 1 fixed. The slope at the current x₁ = 2 is 3, but the displacement to 0 is −2, so the actual score decrease is 6. The rate and the total change also have different units.</figcaption>
</figure>

The quadratic curve below shows the error from extending the current tangent to a distant baseline.

<figure class="lesson-figure" markdown="1">

![Quadratic slice six plus x three squared and tangent at x three one agree at score seven but at zero the actual score is six and the tangent predicts five](../../figures/assets/I07/I07-01-quadratic-local-finite.svg)

<figcaption>Here x₁ = 2 and x₂ = 3 are fixed. The local gradient at x₃ = 1 is 2, but removing this coordinate by setting it to 0 decreases the score by 1. Extending the tangent to 0 predicts 5, differing from the curve's actual score of 6.</figcaption>
</figure>

The two panels below compare the three coordinates while keeping the units of a rate and a score difference separate.

<figure class="lesson-figure" markdown="1">

![Separate vertical panels show local gradient three two two in score per input unit and zero-baseline removal effects six six one in score units with different ties](../../figures/assets/I07/I07-01-gradient-removal-units.svg)

<figcaption>The upper panel shows sensitivity per unit input change at the current point; the lower panel shows the score difference from setting each coordinate to 0. The gradient for x₁ exceeds that for x₂, but both removal effects are 6. Do not combine values with different units as though they were one score.</figcaption>
</figure>

The branching diagram below shows where both removals count the same interaction term.

<figure class="lesson-figure" markdown="1">

![Six unit cells of the interaction x one times x two feed both individual removals with effects six and six while one square-term unit feeds effect one so the individual effects double count the same interaction](../../figures/assets/I07/I07-01-overlapping-removals.svg)

<figcaption>Both removal paths start from the same six cells representing the product term 6. Setting either x₁ or x₂ to 0 removes this entire term, so each removal counts a decrease of 6. The actual original score is 7: the product term 6 plus the square term 1.</figcaption>
</figure>

## 3. Analysis contract

Record at least the following alongside an attribution result.

- The scalar to explain: a particular token logit, the logit difference between two tokens, a loss, or another score
- The feature unit: an input coordinate, token, neuron, head, or subspace
- The evaluation point and baseline
- Whether to preserve the sign or use the absolute value
- The data and unit of replication
- Whether the result is attribution or an actual intervention effect

A softmax probability also depends on the other logits. Sensitivity of a particular logit and sensitivity of that token's probability are different questions.

The two target curves below compare these questions for the same class.

<figure class="lesson-figure" markdown="1">

![Illustrative two-class example holds logit A at one while increasing logit B lowers probability A from sigmoid one to one half and lower through the softmax denominator](../../figures/assets/I07/I07-01-target-softmax-coupling.svg)

<figcaption>This illustrative two-class calculation holds z_A = 1 fixed and varies only z_B. The upper target logit does not change, but the lower target probability changes through its denominator. Even for the same class, the question depends on which scalar is measured.</figcaption>
</figure>

## 4. CPU exercise

<!-- I07_EXAMPLE: i07_01_sensitivity_attribution -->

The code calculates a central-difference gradient and zero-baseline removal effects for the same function. Their difference reflects different questions, not an implementation error.

## Common misconceptions

### Misconception 1. A large gradient means the feature produced the output

A gradient is a local rate of change at the current point. It does not establish whether the input actually used that path or whether the behavior survives its removal.

### Misconception 2. Attribution is an objective decomposition built into the model

Changing the baseline or feature grouping can change the values. Attribution is a result that includes the analyst's rules.

## Exercises

### 1. Classify the question

Is “How much does the logit change when $x_i$ increases by $0.01$?” a sensitivity question or an attribution question?

<details>
<summary>Show solution</summary>

It concerns a small change at the current point, so it is a sensitivity question. Allocating explanatory shares among features additionally requires a baseline and an allocation rule.

</details>

### 2. Calculate a gradient

For $f(x_1,x_2)=x_1x_2$, find the gradient at $x=(2,4)$.

<details>
<summary>Show solution</summary>

Since $\partial f/\partial x_1=x_2$ and $\partial f/\partial x_2=x_1$, the gradient is $(4,2)$.

</details>

### 3. Removal effects

For the same function, find the score decrease from setting each coordinate to 0.

<details>
<summary>Show solution</summary>

The original score is 8. Setting either coordinate to 0 makes the score 0, so both removal effects are 8. They differ from the gradient $(4,2)$.

</details>

### 4. Choose a target

Why is explaining the logit for class A different from explaining its probability in a classification model?

<details>
<summary>Show solution</summary>

Through the softmax denominator, the probability depends on all class logits. Even if the A logit stays the same, changing other logits changes the A probability.

</details>

### 5. Critique a claim

Critique the statement “The token with high saliency caused the answer.”

<details>
<summary>Show solution</summary>

Saliency may be the magnitude of the local gradient of a specified score. A causal claim requires an intervention on the token or internal state, controls, and a change in behavior.

</details>

### 6. Analysis contract

List three items that must be fixed when attributing a next-token prediction.

<details>
<summary>Show solution</summary>

For example, fix a target-minus-foil logit, a feature unit such as tokens or embedding coordinates, and a baseline input. Recording the data and sign-handling rule also improves reproducibility.

</details>

## Evidence and update boundaries

Use [Simonyan et al. (2013)](https://arxiv.org/abs/1312.6034) as an early study visualizing input gradients and [Sundararajan et al. (2017)](https://proceedings.mlr.press/v70/sundararajan17a.html) as a reference for axiomatic attribution with a baseline. Do not promote a particular attribution method to a causal explanation.

## Lesson summary

- Sensitivity is a local rate of change at a point; attribution allocates explanatory shares under specified rules.
- Changing the target, feature unit, or baseline changes the question.
- Gradients and finite removal effects generally differ.
- Attribution values alone do not establish functional use or causality.

## Pass criteria

- Can you distinguish sensitivity from attribution in one sentence each?
- Can you separately calculate a small function's gradient and removal effects?
- Can you write an attribution analysis contract?

## Next lesson

- [I07-02 Gradient-based attribution](I07-02-gradient-attribution.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Sensitivity and attribution are distinguished as questions.
- [x] The target, baseline, and feature unit are specified.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is implicitly required.
- [x] Internal links and math rendering have been checked.
