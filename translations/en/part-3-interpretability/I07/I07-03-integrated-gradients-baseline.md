---
id: "I07-03"
title: "Integrated gradients and baseline"
part: 3
stage: "I07"
status: "complete"
prerequisites: ["I07-02", "M01-08"]
estimated_time: "120–150 minutes"
---

# I07-03. Integrated gradients and baseline

## Why this lesson matters

When saturation makes the gradient small at the current point, gradients can be accumulated along a path from a baseline to the input. Integrated gradients (IG) converts this path integral into feature attributions. Its useful completeness property does not remove the baseline and path from the analysis question.

## Learning objectives

- Explain the path, gradient, and displacement terms in the IG formula.
- Calculate IG for a small function and check completeness.
- Explain why changing the baseline changes the attributions and their interpretation.
- Report numerical integration steps and approximation error.

## Prerequisite check

- Prerequisite lessons: [I07-02 Gradient-based attribution](I07-02-gradient-attribution.md), [M01-08 Integration and accumulation](../../part-1-foundations/M01/M01-08-integration-accumulation.md)
- Check question: On the line segment $\gamma(\alpha)=x'+\alpha(x-x')$, which points correspond to $\alpha=0,1$?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $x'$ | `x prime` | Baseline input | $\mathbb R^d$ |
| $\gamma(\alpha)$ | `gamma of alpha` | The path connecting the baseline and input | $\alpha\in[0,1]$ |
| $\operatorname{IG}_i(x;x')$ | `integrated gradients sub i of x relative to x prime` | Path-integral attribution to feature $i$ | scalar |
| $m$ | `m` | Number of numerical integration steps | positive integer |
| completeness | `completeness` | Attributions sum to the score difference | equality |

## 1. Definition

IG along a straight path is defined by

$$
\operatorname{IG}_i(x;x')
=
(x_i-x_i')
\int_0^1
\frac{\partial f(\gamma(\alpha))}{\partial x_i}
\,d\alpha,
\qquad
\gamma(\alpha)=x'+\alpha(x-x').
$$

The displacement factor describes how far the feature moves from the baseline. The integral collects its average gradient during that move.

Inside the integral, first differentiate $f$ with respect to input coordinate $i$, then evaluate that derivative at the point $\gamma(\alpha)$ on the path. This is not the derivative directly with respect to $\alpha$. Each coordinate's sensitivity is read while all coordinates move together from the baseline to the input. Because the integration interval has length 1, the integral is the average gradient over $\alpha$. Multiplying by the coordinate's total displacement gives a signed attribution. A coordinate with displacement 0 has IG equal to 0.

The following figure shows the intermediate path point and the joint movement of the input coordinates.

<figure class="lesson-figure" markdown="1">

![Projection of the straight path from zero to two three one shows x one and x two moving jointly through one one point five at alpha one half while the third coordinate is alpha](../../figures/assets/I07/I07-03-joint-input-path.svg)

<figcaption>The zero-baseline path γ(α) = (2α, 3α, α) is projected onto the x₁–x₂ plane. All coordinates move together through the intermediate point; the omitted third coordinate is x₃ = α.</figcaption>

</figure>

## 2. Completeness

Under appropriate differentiability conditions, the feature attributions sum to the score difference between the path's endpoints.

$$
\sum_i\operatorname{IG}_i(x;x')=f(x)-f(x').
$$

For example, if $f$ is continuously differentiable near the path, the chain rule gives

\[
\frac{d}{d\alpha}f(\gamma(\alpha))
=\sum_i\frac{\partial f}{\partial x_i}(\gamma(\alpha))(x_i-x_i')
\]

because each coordinate's rate of change along the straight path is $x_i-x_i'$. Integrating from 0 to 1 gives $f(\gamma(1))-f(\gamma(0))=f(x)-f(x')$ on the left, by the fundamental theorem of calculus. On the right, interchanging the finite sum and integral and taking the constant displacements outside the integrals gives the sum of the IG values. Accumulating change across the path, rather than using a gradient at the current point alone, produces a different sum from gradient×input in I07-02.

For the preceding lesson's $f=x_1x_2+x_3^2$ at $x=(2,3,1)$ with a zero baseline, the path is $(2\alpha,3\alpha,\alpha)$ and the gradient is $(3\alpha,2\alpha,2\alpha)$. Since $\int_0^1\alpha\,d\alpha=1/2$, the average gradient is $(1.5,1,1)$; multiplying by the displacements gives IG values $(3,3,1)$. Their sum is 7, matching the score difference. Comparing with gradient×input, $(6,6,2)$, shows that the rate averaged along this path is half the rate at the current point.

This is an accounting identity for a difference relative to the baseline. It does not mean each feature attribution is an independent real-world cause.

The next two figures separate finding the path-average gradient from multiplying by the displacements to obtain the total.

<figure class="lesson-figure" markdown="1">

![Shaded areas under gradients three alpha and two alpha over alpha zero to one are one point five and one whereas their endpoint values are three and two](../../figures/assets/I07/I07-03-average-gradient-area.svg)

<figcaption>The area under g₁ = 3α along the path is 1.5, and the area under g₂ = g₃ = 2α is 1. Because the interval has length 1, each area is the average gradient. This differs from using the endpoint gradient (3, 2, 2) directly.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Upper bars show coordinate attributions three three one after multiplying displacements two three one by average gradients one point five one one and lower stacked score strip totals seven](../../figures/assets/I07/I07-03-average-times-displacement.svg)

<figcaption>Multiplying the average gradient (1.5, 1, 1) by the displacements (2, 3, 1) gives IG = (3, 3, 1). The lower strip shows these terms decomposing the score difference 7. They are not bars of independent causal effects.</figcaption>

</figure>

## 3. Numerical approximation

In code, the integral is approximated by an average over $m$ points.

$$
\widehat{\operatorname{IG}}_i
=
(x_i-x_i')\frac1m
\sum_{k=1}^{m}
\frac{\partial f}{\partial x_i}
\left(x'+\frac{k}{m}(x-x')\right).
$$

This formula is a Riemann sum: divide $[0,1]$ into intervals of width $1/m$ and evaluate the gradient at each right endpoint $k/m$. The factor $1/m$ is both the averaging factor and the interval width. Simply summing the pointwise gradients omits that width and gives the wrong magnitude.

Increase $m$ to check whether the completeness error becomes sufficiently small. Do not choose the step count solely on test data to make the results look better.

Integration errors in individual coordinates can cancel in the sum, so a small completeness error does not establish the accuracy of every coordinate. Also check whether the attribution vector stabilizes as the step count increases, and record the point-selection rule. The exercise averages gradients at $m$ uniformly spaced points including both endpoints, so its points and weighting differ from the right-endpoint Riemann sum above.

The following figures show the rectangle width and the evaluation points used in the code separately.

<figure class="lesson-figure" markdown="1">

![Illustrative four-step right Riemann rectangles under gradient two alpha have width one quarter and heights one half one one point five two with approximate area one point two five rather than exact one](../../figures/assets/I07/I07-03-right-riemann-width.svg)

<figcaption>This illustrative approximation of g₃(α) = 2α uses m = 4. Multiplying by each rectangle's width 1/4 gives an area sum of 1.25, exceeding the actual integral 1. Adding only the four heights to obtain 5 is not integration.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Two alpha axes compare four right endpoint samples one quarter one half three quarters one against four endpoint-inclusive samples zero one third two thirds one with equal one quarter weights in each stated mean](../../figures/assets/I07/I07-03-sample-point-rules.svg)

<figcaption>Here m = 4 is illustrative. The formula samples 1/4, 1/2, 3/4, and 1; including both endpoints as in the exercise gives 0, 1/3, 2/3, and 1. The exercise averages the four values with equal weights of 1/4, not trapezoidal integration weights.</figcaption>

</figure>

## 4. A baseline is not synonymous with no information

A black image, zero embedding, padding token, and mean activation define different counterfactuals. In language, setting an embedding to 0 may not correspond to an actual token input. Several defensible baselines can be compared in a sensitivity analysis, but do not report only those that look favorable after seeing the results.

The following comparison shows the exercise's two baselines decomposing different score differences.

<figure class="lesson-figure" markdown="1">

![For input two three one the zero baseline has IG three three one and score gap seven while the one baseline has IG two three zero and score gap five because the third coordinate has zero displacement](../../figures/assets/I07/I07-03-baseline-attributions.svg)

<figcaption>The input is x = (2, 3, 1), as in the exercise. The zero baseline gives IG = (3, 3, 1) and a score difference of 7; the one baseline gives IG = (2, 3, 0) and a difference of 5. With the one baseline, x₃ has displacement 0, so its attribution is also 0.</figcaption>

</figure>

## 5. CPU exercise

<!-- I07_EXAMPLE: i07_03_integrated_gradients -->

Use a zero baseline and a one baseline for the same input. Both have small completeness errors, but their feature attributions differ.

## Common misconceptions

### Misconception 1. Completeness proves faithfulness

Preserving the sum is a mathematical property relative to the specified baseline and path. It does not automatically validate feature meaning, realistic counterfactuals, or the model's causal structure.

### Misconception 2. The baseline is an implementation detail

It determines which difference the attribution explains, so it is part of the research question.

## Exercises

### 1. A linear function

Find IG for $f(x)=3x$ with baseline $0$ and input $2$.

<details>
<summary>Show solution</summary>

The gradient is 3 throughout the path. The displacement is 2, so IG is $2\times3=6$, matching $f(2)-f(0)=6$.

</details>

### 2. A square function

Calculate IG by integration for $f(x)=x^2$ with baseline $0$ and input $2$.

<details>
<summary>Show solution</summary>

$\gamma(\alpha)=2\alpha$, and the gradient is $2\gamma=4\alpha$. Thus $2\int_0^1 4\alpha\,d\alpha=4$, and the score difference is also 4.

</details>

### 3. Change the baseline

What is IG if the baseline in the preceding exercise changes to 1?

<details>
<summary>Show solution</summary>

Completeness gives $f(2)-f(1)=4-1=3$. Direct integration gives the same value.

</details>

### 4. Numerical check

Which scalar error should you check first in an IG implementation?

<details>
<summary>Show solution</summary>

Check the completeness error, $|\sum_i\widehat{\operatorname{IG}}_i-[f(x)-f(x')]|$. Also check whether it decreases as the step count increases.

</details>

### 5. A language baseline

Explain why a zero embedding is not always a good baseline.

<details>
<summary>Show solution</summary>

The zero vector may not be an actual token embedding obtainable from the tokenizer. Intermediate path points may also lie outside the training distribution, making interpretation depend on the baseline choice.

</details>

### 6. Critique a claim

Why does “IG sums to the logit difference, so we have each token's causal effect” overstate the result?

<details>
<summary>Show solution</summary>

Completeness is a gradient accounting identity along the chosen continuous path. Actual token-change interventions, interactions, and input validity have not been checked, so the values cannot be called causal effects.

</details>

## Evidence and update boundaries

Use [Sundararajan, Taly and Yan (2017)](https://proceedings.mlr.press/v70/sundararajan17a.html) for the definition, the sensitivity and implementation-invariance axioms, and completeness. Later variants may use different baselines, paths, and guarantee conditions; do not collapse them under the same name.

## Lesson summary

- IG integrates gradients from a baseline to the input and multiplies by feature displacements.
- Attributions sum to the score difference relative to the baseline.
- The baseline and path are part of the interpretation question.
- Completeness is not sufficient for causal faithfulness.

## Pass criteria

- Can you calculate IG for a single-variable function by hand?
- Can you use completeness error to check an implementation?
- Can you include the baseline choice in the analysis contract?

## Next lesson

- [I07-04 Perturbation-based attribution](I07-04-perturbation-attribution.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] The IG definition and completeness are distinguished.
- [x] The baseline, path, and numerical error are included.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is implicitly required.
- [x] Internal links and math rendering have been checked.
