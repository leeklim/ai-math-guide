---
id: "I08-06"
title: "Hessian spectrum"
part: 3
stage: "I08"
status: "complete"
prerequisites: ["I08-05", "M03-12", "M02-11"]
estimated_time: "100–130 minutes"
---

# I08-06. Hessian spectrum

## Why this lesson matters

A gradient gives the current slope, but not how the gradient changes along each direction. Hessian eigenvalues summarize local loss curvature at a chosen point and parameterization. For large models, part of the spectrum can be approximated using Hessian-vector products without constructing the full Hessian.

## Learning objectives

- Explain the relation between the Hessian and second directional derivatives.
- Interpret eigenvalue signs as local curvature.
- Distinguish Hessian-vector products from constructing the full matrix.
- Avoid equating sharpness directly with generalization.

## Prerequisite check

- Prerequisite lessons: [I08-05 Mini-batch noise and optimizer state](I08-05-minibatch-noise-optimizer-state.md), [M03-12 Hessian](../../part-1-foundations/M03/M03-12-hessian.md), [M02-11 Eigenvalues and eigenvectors](../../part-1-foundations/M02/M02-11-eigenvalues-eigenvectors.md)
- Check question: How are a symmetric matrix's eigenvalues related to its Rayleigh quotient?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $H(\theta)=\nabla^2L(\theta)$ | `H of theta equals the Hessian of L at theta` | Loss Hessian | $p\times p$ |
| $v^\top Hv$ | `v transpose H v` | Second-order curvature along $v$ | scalar |
| $Hv$ | `H v` | Hessian-vector product | $\mathbb R^p$ |
| $\lambda_{\max}$ | `lambda max` | Largest eigenvalue | scalar |
| spectrum | `spectrum` | Multiset of eigenvalues | $p$ real values for symmetric $H$ |

## 1. Local quadratic approximation

For a small $\delta$,

$$
L(\theta+\delta)\approx L(\theta)
+\nabla L(\theta)^\top\delta
+\frac12\delta^\top H(\theta)\delta.
$$

Use this approximation when the loss has continuous second derivatives near the point. Moving by $\delta=\varepsilon v$ along a unit vector $v$ gives linear term $\varepsilon\nabla L(\theta)^\top v$ and quadratic term $\frac12\varepsilon^2v^\top Hv$. Thus, $v^\top Hv$ is the second derivative in this direction. To compare vectors of different magnitudes, normalize $v$ or use the Rayleigh quotient $v^\top Hv/(v^\top v)$.

At a stationary point, the linear term vanishes. For a unit eigenvector, substituting $Hv=\lambda v$ gives $v^\top Hv=\lambda$, making the eigenvalue the curvature in that direction. A positive value makes the quadratic term increase the loss for a small move; a negative value decreases it. At a point where the gradient is not 0, the linear term must also be considered. An eigenvalue of 0 only removes the quadratic term; it does not ensure flatness at higher orders.

The sign of curvature can vary with direction at the same point.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three eigenvector cross-sections with eigenvalues four, one, and negative one half at a stationary point.](../../figures/assets/I08/I08-06-curvature-directions.svg)

<figcaption>These are quadratic terms ½λε² along the three unit eigenvectors of the existing CPU example's diagonal Hessian. With gradient 0, a small move in the negative-curvature direction lowers the loss. This is a mathematical local quadratic example, not an actual model's global landscape.</figcaption>
</figure>

Include the linear term when the gradient is not 0.

<figure class="lesson-figure" markdown="1">

![Positive quadratic curvature compared with the total change when a nonzero linear gradient term is included.](../../figures/assets/I08/I08-06-linear-term-matters.svg)

<figcaption>Even with positive H=4, gradient g=1 gives total change ε+2ε². For small negative ε, the linear term lowers the loss. The Hessian sign alone therefore does not determine changes at a nonstationary point.</figcaption>
</figure>

Compare two functions whose quadratic terms vanish.

<figure class="lesson-figure" markdown="1">

![The fourth-power curve and a constant zero function have the same zero first and second derivatives at zero but differ away from zero.](../../figures/assets/I08/I08-06-zero-curvature-fourth-order.svg)

<figcaption>Both ε⁴ and constant 0 have gradient and Hessian 0 at the origin, but differ away from it. Eigenvalue 0 means the quadratic term vanishes, not that the function is flat at every order.</figcaption>
</figure>

## 2. What the spectrum tells you

$\lambda_{\max}$ is the largest eigenvalue and the maximum Rayleigh quotient over unit directions. Decomposing a vector in an orthogonal eigenbasis makes its Rayleigh quotient a weighted average of the eigenvalues. Each weight is the squared coefficient of that component, and the weights sum to 1, so the quotient cannot exceed the largest eigenvalue. Even the largest eigenvalue may be negative; do not always call it the largest positive value.

For a quadratic with positive eigenvalues, the displacement from the minimum can be decomposed along eigenvectors. Gradient descent multiplies each displacement component by $1-\eta\lambda$. Satisfying I08-04's stability condition in every direction requires $0<\eta<2/\lambda_{\max}$. In a general neural network, the Hessian changes as the parameters move, so a spectrum at one point does not guarantee stability along the entire training trajectory.

Many eigenvalues near 0 mean many flat directions in the quadratic approximation. However, scale symmetries and parameterization change the eigenvalues, so compare raw sharpness across models cautiously.

Normalized squared components supply the weights for directional curvature.

<figure class="lesson-figure" markdown="1">

![Squared component weights one sixth, four sixths, and one sixth average the Hessian eigenvalues four, one, and negative one half.](../../figures/assets/I08/I08-06-rayleigh-weights.svg)

<figcaption>Dividing the squared components of the existing CPU vector v=(1,2,−1) by their sum 6 gives the weights. Their weighted eigenvalue sum is Rayleigh quotient 1.25, between the smallest value −0.5 and largest value 4.</figcaption>
</figure>

A learning rate is not equally safe for every eigenmode.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two positive quadratic eigenmodes remain bounded with learning rate point four but the eigenvalue four mode diverges with learning rate point six.](../../figures/assets/I08/I08-06-eigenmode-step-size.svg)

<figcaption>For the mathematical quadratic H=diag(4,1), each displacement component is multiplied by 1−ηλ. Both decay at η=0.4, but the λ=4 component alternates signs and grows at η=0.6. Do not extend such a pointwise condition into global stability for a general neural network.</figcaption>
</figure>

## 3. Avoid constructing the full Hessian

For large $p$, storing $p^2$ entries is difficult. For a fixed vector $v$, differentiating the scalar $\nabla L(\theta)^\top v$ again with respect to the parameters gives $H(\theta)^\top v$. Under the smoothness conditions above, the Hessian is symmetric, so this is $Hv$. Automatic differentiation computes this scalar derivative to obtain a length-$p$ product instead of the full matrix. The computation graph and intermediate values still require memory.

Power iteration repeatedly computes $Hv$ and normalizes its length. Repeated multiplication weights the initial vector's eigenvector components by powers of the eigenvalues. If a unique eigenvalue has the largest absolute value and the initial vector has a component along its eigenvector, that direction becomes dominant. With a large negative eigenvalue, this may differ from the direction of largest positive curvature.

Lanczos computes the spectrum of a small matrix in a subspace constructed from several HVPs. The density estimate in [Ghorbani et al. (2019)](https://proceedings.mlr.press/v97/ghorbani19b/ghorbani19b.pdf) uses multiple random probes and weights from the Lanczos results. Estimating a single dominant eigenvalue and estimating the full density are different outputs. Record the iteration count, tolerance, probe-vector seed, and the loss and data being measured.

Trace which scalar is differentiated again instead of constructing the full Hessian.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Differentiate the scalar loss, dot its gradient with a fixed vector, then differentiate the resulting scalar to obtain a vector Hessian product.](../../figures/assets/I08/I08-06-hvp-differentiation-route.svg)

<figcaption>The inner product of the loss gradient with fixed v is a scalar. Differentiating it with respect to θ gives Hᵀv, which equals Hv under C² conditions because Hᵀ=H. This avoids storing a p×p matrix, but the autodiff graph and intermediate values still need memory.</figcaption>
</figure>

Follow repeated multiplication in an example where the maximum value differs from the maximum absolute value.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Normalized power iteration for diagonal eigenvalues three and negative five favors the negative eigenvalue with larger absolute magnitude.](../../figures/assets/I08/I08-06-power-absolute-dominance.svg)

<figcaption>This mathematical example applies power iteration to H=diag(3,−5). The negative direction with absolute value 5 dominates: the Rayleigh quotient approaches −5 while the vector alternates signs. Distinguish the maximum eigenvalue 3 from the eigenvalue of largest absolute value, −5.</figcaption>
</figure>

## 4. CPU exercise

<!-- I08_EXAMPLE: i08_06_hessian_spectrum -->

Calculate the spectrum of diagonal Hessian $\operatorname{diag}(4,1,-0.5)$, $Hv$ for one vector, and its Rayleigh quotient. The negative eigenvalue shows that this point is not a local minimum in every direction.

## Common misconceptions

### Misconception 1. A large eigenvalue necessarily means poor generalization

Sharpness depends on parameterization, scale, and the measured loss. Measure generalization with an independent test metric.

### Misconception 2. The Hessian spectrum is the global loss landscape

The Hessian gives local quadratic information at one point. It does not directly describe distant points or other basins.

## Exercises

### 1. Directional curvature

Find $v^\top Hv$ for $H=\operatorname{diag}(3,-1)$ and $v=(0,1)$.

<details><summary>Show solution</summary>

It is $-1$. The second-coordinate direction has negative curvature.

</details>

### 2. Shapes

For $\theta\in\mathbb R^p$, give the shapes of $H$, $v$, and $Hv$.

<details><summary>Show solution</summary>

$H$ is $p\times p$; $v$ and $Hv$ are length-$p$ vectors.

</details>

### 3. Stationary point

With gradient 0 and a negative Hessian eigenvalue, is the point a strict local minimum?

<details><summary>Show solution</summary>

No. A small move along the negative-curvature direction makes the quadratic term lower the loss.

</details>

### 4. HVP

Why does an HVP use less memory than the full Hessian?

<details><summary>Show solution</summary>

Instead of storing $p^2$ entries, it computes and stores only the $p$ entries of the product for a given vector.

</details>

### 5. Largest eigenvalue

What does power iteration mainly find?

<details><summary>Show solution</summary>

The dominant eigenvalue of largest absolute value and its eigenvector direction. Check the sign interpretation under the relevant conditions.

</details>

### 6. Critique a claim

Critique “Checkpoint $t$ has smaller $\lambda_{\max}$, so it generalizes better.”

<details><summary>Show solution</summary>

A single local curvature measure does not automatically imply generalization. Check that the parameterization is the same and measure independent test performance.

</details>

## Evidence and update boundaries

Use [Ghorbani, Krishnan and Xiao (2019)](https://proceedings.mlr.press/v97/ghorbani19b.html) for numerical estimation of Hessian eigenvalue density during neural-network training. This lesson's CPU example uses an exact diagonal Hessian; it does not reproduce large-scale spectrum approximation accuracy.

## Lesson summary

- The Hessian describes local second-order changes in loss.
- Eigenvalue signs and magnitudes give directional curvature.
- For large models, HVPs approximate part of the spectrum.
- Validate sharpness and generalization with separate metrics.

## Pass criteria

- Can you explain the quadratic approximation and directional curvature?
- Can you interpret the eigenvalues of a small Hessian?
- Can you state the records and claim limits needed for an HVP approximation?

## Next lesson

- [I08-07 Loss landscape and mode connectivity](I08-07-loss-landscape-mode-connectivity.md)

## Author checklist

- [x] Local curvature and the global landscape are distinguished.
- [x] HVPs and spectrum approximations are explained.
- [x] Every exercise has a solution.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Claim strength and spoken readings have been checked.
- [x] Internal links and equations have been checked.
