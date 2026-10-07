---
id: "I07-02"
title: "Gradient-based attribution"
part: 3
stage: "I07"
status: "complete"
prerequisites: ["I07-01", "N05-26"]
estimated_time: "90–120 minutes"
---

# I07-02. Gradient-based attribution

## Why this lesson matters

A gradient provides sensitivities for many input coordinates in a single backward pass. But raw gradients, saliency, and gradient×input report different values and are affected by saturation, input units, and sign handling. Fast computation is separate from a valid explanation.

## Learning objectives

- Calculate raw gradients, saliency, and gradient×input.
- Distinguish the questions answered by signed values and absolute values.
- Explain how saturation and input scale affect gradient interpretation.
- Check an autograd result against a small hand calculation.

## Prerequisite check

- Prerequisite lessons: [I07-01 Sensitivity and attribution](I07-01-sensitivity-attribution.md), [N05-26 Activation gradients and intervention](../../part-2-neural-computation/N05/N05-26-gradient-collection-intervention-preparation.md)
- Check question: Why must you choose a scalar score to obtain a gradient with the input's shape after `backward()`?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $g_i=\frac{\partial s}{\partial x_i}$ | `g sub i equals partial s over partial x sub i` | Signed local sensitivity | scalar |
| $\lvert g_i\rvert$ | `the absolute value of g sub i` | Saliency magnitude | nonnegative scalar |
| $x_i g_i$ | `x sub i times g sub i` | Zero-baseline gradient×input | scalar |
| $\nabla_x s$ | `the gradient of s with respect to x` | The gradient over all coordinates | $\mathbb R^d$ |
| saturation | `saturation` | A region with a small local gradient despite a change in output | local property |

## 1. Three outputs

The raw gradient preserves increasing and decreasing directions through its sign. Saliency uses $|g_i|$, discarding direction and retaining only magnitude. Gradient×input is a first-order Taylor term that multiplies the gradient by the displacement from a zero baseline to the current input.

$$
s(x)-s(0)\approx \nabla_x s(x)^\top x=\sum_i x_i g_i
$$

Here the gradient is evaluated at the current point $x$, not at the baseline 0. The displacement from $x$ to 0 is $-x$, so the first-order approximation is $s(0)\approx s(x)-\nabla_xs(x)^\top x$. Rearranging gives the equation above. Each $x_i g_i$ is a coordinate's term within this linear approximation. If 0 is far from the current point, this single evaluation cannot capture how the gradient changes between them. For an affine function, the gradient is constant and the bias cancels in the difference, so the sum gives the exact score difference.

For a nonlinear function, it is only an approximation. A sum that differs from the actual score difference does not mean that autograd is wrong.

The two panels below show the information lost when signed gradients are converted to saliency.

<figure class="lesson-figure" markdown="1">

![The worked exercise score two x one minus x two squared at three two yields signed bars two and minus four but absolute saliency bars two and four](../../figures/assets/I07/I07-02-signed-versus-saliency.svg)

<figcaption>This uses the exercise's s = 2x₁ − x₂² at x = (3, 2). The upper panel retains the negative direction: increasing x₂ lowers the score. The lower panel loses that sign.</figcaption>

</figure>

## 2. Hand calculation

For $s=x_1x_2+x_3^2$ at $x=(2,3,1)$,

$$
\nabla_x s=(3,2,2),\qquad x\odot\nabla_xs=(6,6,2).
$$

The gradient×input sum is 14, whereas $s(x)-s(0)=7$. The duplicated coefficients from the product and the square prevent completeness.

At a general input, this sum is also $x_1x_2+x_2x_1+2x_3^2=2s(x)$. The first product term appears in the derivatives with respect to both coordinates, and differentiation gives the square term a coefficient of 2. Multiplying the current rate of change by the input does not remove these coefficients. Completeness requires the attributions to sum to the score difference from the baseline. Here that condition fails even though the gradient is exact.

The path diagram below compares the tangent extended from the current point to the baseline with the actual score curve.

<figure class="lesson-figure" markdown="1">

![Along the path t times two three one the score is seven t squared and the tangent at t one predicts minus seven at baseline zero instead of actual zero giving slope fourteen but total difference seven](../../figures/assets/I07/I07-02-current-tangent-gap.svg)

<figcaption>Along the path that scales the current input by t, s(tx) = 7t². The tangent slope of 14 at t = 1 is the gradient×input sum. Extending that tangent to t = 0 predicts −7, whereas the actual baseline score is 0 and the difference between the points is 7.</figcaption>

</figure>

## 3. Scale and saturation

Changing units to $x_i'=c x_i$ can rescale the raw gradient by $1/c$ through the chain rule. Check input units when comparing absolute gradients across features.

This comparison assumes $c>0$ and expresses the same physical input and function in new units. The derivative mapping the new coordinate back to the original coordinate is $1/c$, so the gradient measuring the same score per new unit becomes $g_i/c$. Then $x_i'g_i'=cx_i\cdot g_i/c=x_i g_i$, so gradient×input is invariant to this origin-preserving rescaling. Changing only the input numbers without transforming the model's function to preserve its meaning is an experiment that changes the actual input, not a comparison of units.

A saturating function such as sigmoid can have a gradient near 0 at the current point even when its output differs substantially from the baseline. This does not mean the feature was historically unimportant.

For example, let $s(x)=\sigma(x)$ with baseline 0, whose score is 0.5. For large positive $x$, the score approaches 1, giving a difference of about 0.5, but the current gradient $\sigma(x)(1-\sigma(x))$ is near 0. A substantial change between two points and a flat neighborhood at the current point can coexist.

The next two figures show changing input units and entering a saturated region, respectively.

<figure class="lesson-figure" markdown="1">

![Illustrative identical score function has slope three per meter on the upper plot and zero point zero three per centimeter on the lower plot while the same physical point one meter or one hundred centimeters has score three](../../figures/assets/I07/I07-02-unit-rescaling.svg)

<figcaption>The same illustrative function s = 3x is expressed in meters and centimeters. At the same input, 1 m = 100 cm, the score is 3, but the gradients per unit are 3 and 0.03. Both representations give xg = 3.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Sigmoid curve rises from baseline probability one half at zero to near one at six while the local tangent at six is nearly horizontal and the score gap is nearly one half](../../figures/assets/I07/I07-02-sigmoid-saturation.svg)

<figcaption>The gap between σ(0) = 0.5 and σ(6) ≈ 0.9975 is about 0.4975, but the current slope at x = 6 is about 0.00247. The accumulated change from the baseline is separate from the rate of change near the current point.</figcaption>

</figure>

## 4. CPU exercise

<!-- I07_EXAMPLE: i07_02_gradient_attribution -->

Compare PyTorch's gradient $(3,2,2)$ with the hand calculation. `gradient_times_input_sum` differs from the score difference, and that discrepancy is reported rather than hidden.

## Common misconceptions

### Misconception 1. Taking absolute values loses no information

Absolute values merge directions that increase the score with those that decrease it. Preserve signed gradients when the question includes direction.

### Misconception 2. Gradient×input always gives a complete decomposition

It does under specific conditions, such as a linear homogeneous function, but not for a general nonlinear function.

## Exercises

### 1. Raw gradient

Find the gradient of $s=2x_1-x_2^2$ at $x=(3,2)$.

<details>
<summary>Show solution</summary>

Since $\partial s/\partial x_1=2$ and $\partial s/\partial x_2=-2x_2=-4$, the gradient is $(2,-4)$.

</details>

### 2. Saliency

Explain the information retained and lost by saliency compared with the raw gradient in the preceding exercise.

<details>
<summary>Show solution</summary>

Saliency is $(2,4)$. It retains the magnitude showing greater sensitivity to the second coordinate, but loses the sign indicating that increasing that coordinate decreases the score.

</details>

### 3. Gradient×input

Calculate gradient×input for the preceding function and point.

<details>
<summary>Show solution</summary>

It is $(3,2)\odot(2,-4)=(6,-8)$. The sum is $-2$, unlike the actual difference $s(3,2)-s(0,0)=2$.

</details>

### 4. Saturation

Explain why the gradient is small at a point where the sigmoid output is near 1.

<details>
<summary>Show solution</summary>

The sigmoid derivative is $\sigma(z)(1-\sigma(z))$. When $\sigma(z)\approx1$, the second factor is near 0, making the local gradient small.

</details>

### 5. Changing units

Why can the raw gradient's magnitude change when an input in meters is expressed in centimeters?

<details>
<summary>Show solution</summary>

Expressing the same physical quantity as $x'=100x$ gives $\partial s/\partial x'=(1/100)\partial s/\partial x$. Comparing numerical magnitudes involves input units.

</details>

### 6. Scope of a claim

After finding a large gradient, what else is needed to establish functional use?

<details>
<summary>Show solution</summary>

Manipulate the relevant input or internal state and measure the output change in a paired comparison for the same input. Realistic baselines and random or matched controls are also needed.

</details>

## Evidence and update boundaries

Use [Simonyan et al. (2013)](https://arxiv.org/abs/1312.6034) as a starting point for input-gradient visualization. This lesson treats gradients as local sensitivity, not as equivalent to subsequent intervention results.

## Lesson summary

- A raw gradient is signed local sensitivity; saliency is its absolute value.
- Gradient×input is a zero-baseline first-order approximation, not generally a complete decomposition.
- Saturation and input units change the results.
- Fast computation does not ensure causal validity.

## Pass criteria

- Can you calculate the three gradient-based values by hand?
- Can you explain the saturation and scale issues?
- Can you compare an autograd result with a hand calculation?

## Next lesson

- [I07-03 Integrated gradients and baseline](I07-03-integrated-gradients-baseline.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Raw gradients, saliency, and gradient×input are distinguished.
- [x] Saturation and scale limitations are included.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is implicitly required.
- [x] Internal links and math rendering have been checked.
