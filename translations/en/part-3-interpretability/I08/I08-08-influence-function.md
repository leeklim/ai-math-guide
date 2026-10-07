---
id: "I08-08"
title: "Influence function"
part: 3
stage: "I08"
status: "complete"
prerequisites: ["I08-07", "I08-06", "M04-11"]
estimated_time: "100–140 minutes"
---

# I08-08. Influence function

## Why this lesson matters

Determining the exact effect of a particular training example on a test prediction requires a counterfactual comparison with retraining after removing that example. An influence function approximates this retraining effect using an infinitesimal change in data weight near an optimum and the inverse Hessian. It offers faster computation but comes with locality, differentiability, and curvature conditions.

## Learning objectives

- Derive the parameter change from upweighting an example.
- Explain the sign and terms in the test-loss influence formula.
- Distinguish an HVP from an inverse-Hessian-vector product.
- Design validation of the approximation through leave-one-out retraining.

## Prerequisite check

- Prerequisite lessons: [I08-07 Loss landscape and mode connectivity](I08-07-loss-landscape-mode-connectivity.md), [I08-06 Hessian spectrum](I08-06-hessian-spectrum.md), [M04-11 Likelihood and maximum likelihood](../../part-1-foundations/M04/M04-11-likelihood-maximum-likelihood.md)
- Check question: Are $H^{-1}v$ and $Hv$ the same computation?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $z_i$ | `z sub i` | The $i$th training example | sample |
| $\hat\theta_\varepsilon$ | `theta hat sub epsilon` | Optimum after upweighting $z_i$ by $\varepsilon$ | $\mathbb R^p$ |
| $H_{\hat\theta}$ | `H sub theta hat` | Empirical-risk Hessian at the optimum | $p\times p$ |
| $H^{-1}v$ | `H inverse v` | Inverse-Hessian-vector product | $\mathbb R^p$ |
| leave-one-out | `leave one out` | Retraining comparison after removing one example | counterfactual procedure |

## 1. Change a data weight infinitesimally

Write the empirical risk as $L(\theta)$ and the original optimum as $\hat\theta$. The optimum after adding $\varepsilon\ell(z_i,\theta)$ is $\hat\theta_\varepsilon$. Positive $\varepsilon$ increases the loss weight of that example. The condition that the gradient is zero at this optimum is

$$
\nabla L(\hat\theta_\varepsilon)
+\varepsilon\nabla\ell(z_i,\hat\theta_\varepsilon)=0
$$

Differentiate this expression along a local branch where the optimum moves smoothly with $\varepsilon$. The chain rule for the first term gives the Hessian times the rate of change of the optimum. In the second term, differentiating $\varepsilon$ itself leaves a gradient, while the other term multiplied by $\varepsilon$ vanishes at 0. Thus,

$$
H_{\hat\theta}
\left.\frac{d\hat\theta_\varepsilon}{d\varepsilon}\right|_{\varepsilon=0}
+\nabla\ell(z_i,\hat\theta)=0.
$$

If the Hessian is invertible, solve this linear equation to obtain

$$
\left.\frac{d\hat\theta_\varepsilon}{d\varepsilon}\right|_{\varepsilon=0}
=-H_{\hat\theta}^{-1}\nabla_\theta\ell(z_i,\hat\theta).
$$

This is the direction in which the optimum moves enough to offset the added training gradient. Along a small positive-eigenvalue direction, the same gradient component requires a larger displacement, which is why inverse curvature enters.

Distinguish the two differentiated terms and where the inverse enters.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Chain and product rules differentiate a stationary optimum condition, then an invertible Hessian gives the negative inverse-curvature displacement.](../../figures/assets/I08/I08-08-stationary-implicit-derivative.svg)

<figcaption>Differentiate the stationary equation with respect to ε along a smooth local optimum branch. At ε=0, the ε-multiplied product-rule term vanishes, leaving the added training gradient. Solving H dθ̂_ε/dε=−∇ℓᵢ to offset it gives the inverse Hessian and negative sign.</figcaption>
</figure>

Consider an example in which inverse curvature changes the displacement direction.

<figure class="lesson-figure" markdown="1">

![A training gradient one one, its negative, and the inverse-Hessian displacement negative point two five negative one for diagonal curvature four one.](../../figures/assets/I08/I08-08-inverse-curvature-displacement.svg)

<figcaption>This mathematical example has H=diag(4,1) and training gradient g=(1,1). Ignoring curvature gives −g, whose direction differs from the actual rate of change −H⁻¹g=(−0.25,−1). The direction with positive curvature 1 needs a larger displacement to offset the same gradient than the direction with curvature 4.</figcaption>
</figure>

## 2. Influence on test loss

The rate of change in loss for test example $z_{test}$ is

$$
I_{\mathrm{up,loss}}(z_i,z_{test})
=-\nabla\ell(z_{test},\hat\theta)^\top
H_{\hat\theta}^{-1}\nabla\ell(z_i,\hat\theta).
$$

Test loss changes through the optimum $\hat\theta_\varepsilon$. The chain rule gives the expression above by taking the inner product of the test gradient with the optimum's rate of change. First transform the training gradient through the inverse Hessian, then take its inner product with the test gradient to read the change in test loss. Under this upweighting definition, a positive value means increasing test loss and a negative value means decreasing test loss.

The loss difference for a small weight change is approximated by $\varepsilon I_{\mathrm{up,loss}}$. For a simple average of $n$ losses without regularization, removing one example corresponds to $\varepsilon=-1/n$, eliminating its original weight of $1/n$. The sign of the removal approximation is opposite to that for upweighting. If retraining also changes the mean's normalization and regularization, include those objective changes; do not use the same coefficient solely because the procedure is called removal.

Even the same parameter change gives different loss influences depending on the test gradient.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three different test gradients have negative, positive, or zero inner products with the same inverse-curvature parameter displacement.](../../figures/assets/I08/I08-08-test-gradient-projection.svg)

<figcaption>Taking inner products of the same rate of change dθ/dε=(−0.25,−1) with test gradients (1,1), (−1,−1), and (1,−0.25) gives −1.25, 1.25, and 0, respectively. These signs describe first-order changes in test loss under positive upweighting; the last case does not mean that higher-order changes are absent.</figcaption>
</figure>

Do not assign the upweighting sign directly to removal.

<figure class="lesson-figure" markdown="1">

![The same negative upweight-loss influence gives opposite approximate test-loss changes under positive and negative example-weight perturbations.](../../figures/assets/I08/I08-08-upweight-removal-sign.svg)

<figcaption>Holding I_up,loss=−1.25 fixed and changing ε from +0.1 to −0.1 reverses the sign of ε I. Using ε=−1/n as a removal approximation assumes a simple mean objective without regularization. If a normalized refit and regularization differ, include those objective changes in the calculation.</figcaption>
</figure>

## 3. Conditions and validation

The classical derivation uses a smooth loss, an invertible Hessian, and a well-defined local optimum. In deep networks, the Hessian can be singular or indefinite, and training may not reach an exact optimum. Damping and iterative solvers enable computation but do not automatically restore the assumptions.

Computing $H^{-1}v$ means finding an unknown vector $u$ satisfying $Hu=v$. An HVP maps a given $u$ to $Hu$, while an inverse-Hessian solver uses this product repeatedly to approximate the equation's solution. There is no need to construct the whole inverse. If damping is added and $(H+\lambda I)u=v$ is solved, this uses different curvature from the original $Hu=v$, so record $\lambda$ and the numerical residual. A small residual means that the selected linear equation was solved well, not that the approximation error for a finite retraining effect is also small.

In small models, compare influence rankings with actual leave-one-out retraining rankings. Use multiple seeds and fix the prediction target.

Distinguish multiplication of a given vector from an iterative solve for an unknown vector.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An iterative solver sends a candidate vector through a Hessian-vector product, checks v minus H times the candidate, and either returns it or tries another candidate.](../../figures/assets/I08/I08-08-inverse-solve-residual-loop.svg)

<figcaption>An HVP maps a given candidate uⱼ to H uⱼ. An inverse solve repeatedly uses this product to find the unknown u in Hu=v. Even with a small residual, the accuracy of the local approximation to finite retraining effects needs separate validation.</figcaption>
</figure>

The damping value changes not just numerical stability but also the inverse response.

<figure class="lesson-figure" markdown="1">

![Increasing damping decreases the inverse response along eigenvalue one and four directions of a positive diagonal Hessian.](../../figures/assets/I08/I08-08-damping-changes-response.svg)

<figcaption>For H=diag(4,1) and v=(1,1), each inverse-response magnitude is 1/(λ_i+λ). Adding damping changes displacement, especially in low-curvature directions. Record λ rather than calling this an unchanged solution to the original Hu=v.</figcaption>
</figure>

## 4. CPU exercise

<!-- I08_EXAMPLE: i08_08_influence_function -->

In 1-dimensional ridge regression, compare the code's Hessian-based removal approximation with actual leave-one-out refits. The output here is a scalar parameter change, not a test-loss change. The code's `rank_correlation_proxy` is a Pearson correlation computed with `np.corrcoef`, not a directly computed rank correlation coefficient.

The exercise adds $\lambda\theta^2/2$ to the mean of example losses $(\theta x_i-y_i)^2/2$, then recomputes the mean over the remaining $n-1$ examples when refitting. Under this normalization, the removal-induced gradient change at the original optimum includes the regularization gradient as well as the example gradient. Its first-order displacement is approximated by $(\nabla\ell(z_i,\hat\theta)+\lambda\hat\theta)/[(n-1)H]$. The existing code's approximation simplifies this by omitting the regularization term in the numerator. Preserve the original code and results, but do not interpret them as validation of the exact normalized leave-one-out influence formula.

Compare the exercise's original approximation and the formula including the normalization term against the same refit.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Existing five-point ridge inputs compare exact normalized refits with the simplified original approximation and with the first-order formula including the regularization term.](../../figures/assets/I08/I08-08-ridge-removal-comparison.svg)

<figcaption>These parameter changes use the existing exercise's five inputs and λ=0.2, computed with the same closed form. The left panel uses the original code's numerator omitting regularization; the right uses the first-order formula with λθ added for the normalization in the text. Approximation error for finite removal remains even on the right. The original exercise code and outputs are unchanged; this is not a plot of test loss or rank correlation.</figcaption>
</figure>

## Common misconceptions

### Misconception 1. Influence gives the exact causal effect of a training example

The approximation concerns a small weight change near a particular optimum. Finite removal and the full retraining path can differ.

### Misconception 2. A large value is due only to the example's content

Duplication, gradient norm, curvature, the target, and model state jointly determine the value.

## Exercises

### 1. Shape

For $\theta\in\mathbb R^p$, what is the shape of $H^{-1}\nabla\ell_i$?

<details><summary>Show solution</summary>

$H^{-1}$ is $p\times p$, and the gradient has length $p$, so the result is in $\mathbb R^p$.

</details>

### 2. Curvature

For the same gradient direction, what happens to the inverse-Hessian displacement when the Hessian eigenvalue is small?

<details><summary>Show solution</summary>

Its reciprocal is larger, so without damping the estimated displacement in that direction grows.

</details>

### 3. Singular Hessian

Why can a direct inverse not be used when the Hessian is singular?

<details><summary>Show solution</summary>

It has a zero eigenvalue, so the inverse does not exist. Record the change in estimand when using damping or a pseudoinverse.

</details>

### 4. Sign

What must be checked before interpreting the sign of loss influence as helpfulness?

<details><summary>Show solution</summary>

Check the upweighting or removal definition, whether the quantity is a loss or a score, and the implementation's negative-sign convention.

</details>

### 5. Validation

What is the most direct check of the approximation against ground truth on a small dataset?

<details><summary>Show solution</summary>

Remove each example and retrain under the same protocol, then compare changes in the test target.

</details>

### 6. Critique a claim

Critique the statement, “Model knowledge is stored in the highest-influence sentences.”

<details><summary>Show solution</summary>

High local gradient alignment does not imply a unique storage location for knowledge. Investigate duplicated data, training paths, and approximation error together.

</details>

## Sources and boundaries for updates

Influence approximations tracing deep-model predictions to training data follow [Koh and Liang (2017)](https://proceedings.mlr.press/v70/koh17a.html). The paper also distinguishes conditions in which the theory can fail due to nonconvexity or nondifferentiability, so this lesson does not call approximations retraining ground truth.

## Lesson summary

- An influence function is a local approximation for infinitesimal changes in data weight.
- It involves the training gradient, inverse Hessian, and test gradient together.
- For deep networks, record damping, numerical solutions, and theoretical conditions separately.
- Validate with leave-one-out retraining where feasible.

## Pass criteria

- Can you explain each term and shape in the influence formula?
- Can you distinguish an HVP from an inverse-Hessian solve?
- Can you design an experiment to validate the approximation?

## Next lesson

- [I08-09 Feature emergence](I08-09-feature-emergence.md)

## Author checklist

- [x] The conditions for the local approximation are specified.
- [x] It is distinguished from a retraining counterfactual.
- [x] Every exercise has a solution.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Claim strength and spoken readings have been checked.
- [x] Internal links and equations have been checked.
