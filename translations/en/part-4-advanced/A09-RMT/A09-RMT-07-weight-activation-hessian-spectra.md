---
id: "A09-RMT-07"
title: "Weight, activation, and Hessian spectra"
part: 4
stage: "A09-RMT"
status: "complete"
prerequisites: ["M02-13", "M03-12", "I06-03", "A09-RMT-06"]
estimated_time: "90–120 minutes"
---

# A09-RMT-07. Weight, activation, and Hessian spectra

## Why this lesson matters

AI papers examine the spectra of weights, activation covariances, and Hessians, but these three matrices have different indices and units. Comparing their eigenvalues directly just because they share spectral terminology mixes structure, data distribution, and loss curvature.

## Learning objectives

- Distinguish weight singular values from covariance and Hessian eigenvalues.
- Specify the index space and normalization of each spectrum.
- Design a null model for each object.
- Write model-interpretation claims appropriate to spectral observations.

## Prerequisite check

- Prerequisite lessons: [M02-13 Singular value decomposition](../../part-1-foundations/M02/M02-13-singular-value-decomposition.md), [M03-12 Hessian](../../part-1-foundations/M03/M03-12-hessian.md), [I06-03 Distributions and basic statistics](../../part-3-interpretability/I06/I06-03-distributions-basic-statistics.md), [A09-RMT-06 Signal and noise eigenvalues](A09-RMT-06-signal-noise-eigenvalues.md)
- Check question: What is the relation between the singular values of a rectangular matrix itself and the eigenvalues of $W^\top W$?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $W=U\Sigma V^\top$ | `W equals U Sigma V transpose` | Singular value decomposition of a weight matrix | Rectangular matrix factorization |
| $C_h=H_c^\top H_c/n$ | `C sub h equals H sub c transpose H sub c over n` | Centered activation covariance | $d_h\times d_h$ |
| $\nabla_\theta^2L$ | `the Hessian of L with respect to theta` | Parameter-space loss curvature | $p\times p$ |
| $\rho(A)$ | `the spectral radius of A` | Largest absolute eigenvalue of a square matrix | Nonnegative scalar |

## Core concepts

### Weight spectra describe amplification from input to output

For a weight matrix $W\in\mathbb R^{d_{\mathrm{out}}\times d_{\mathrm{in}}}$, use the singular spectrum. A right singular vector $v_j$ is a direction in input coordinates, and a left singular vector $u_j$ is a direction in output coordinates. Feeding in unit $v_j$ gives $Wv_j=s_ju_j$, so the singular value $s_j$ describes length amplification by the linear map.

Since $W^\top W=V\Sigma^\top\Sigma V^\top$, its nonzero eigenvalues are $s_j^2$. The matrix $W^\top W$ acts in input space, whereas $WW^\top$ acts in output space. Their nonzero eigenvalues are the same, but their shapes and counts of zeros can differ. Calling this Gram matrix an activation covariance requires a separate sample-matrix interpretation and normalization.

Eigenvalues and spectral radius are not defined for rectangular $W$ itself. Even for a square matrix, $\rho(W)$ and the largest singular value generally differ. For example, $W=\begin{pmatrix}0&3\\0&0\end{pmatrix}$ has all eigenvalues equal to 0 but maps $(0,1)^\top$ to a vector of length 3. Small eigenvalues alone do not mean small amplification in every input direction.

Changing the scaling or parameterization also changes the weight spectrum. The transformation $W\mapsto aW$ multiplies singular values by $|a|$ and Gram eigenvalues by $a^2$. For $a\ne0$, the product of two linear layers $W_2W_1$ can preserve the full function under $W_1\mapsto aW_1$ and $W_2\mapsto W_2/a$. Do not infer a functional change from one layer's spectrum alone.

Distinguish the input/output map and its two Gram matrices, amplification that eigenvalues alone miss, and compensating scales between layers, in that order.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A deterministic three by two weight matrix maps the unit input circle to an output plane ellipse with semiaxes three and one while output coordinate three stays zero.](../../figures/assets/A09-RMT/A09-RMT-07-weight-map-circle-to-ellipse.svg)

<figcaption>The illustrative W=[[3,0],[0,1],[0,0]] has the existing singular values (3,1). Two unit input directions acquire output lengths 3 and 1, and the figure shows the output plane y₃=0. This is length amplification by a linear map, not the variance of a point cloud.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![For the same three by two weight matrix the input Gram has eigenvalues nine one and the output Gram has nine one zero.](../../figures/assets/A09-RMT/A09-RMT-07-input-output-gram-zero-counts.svg)

<figcaption>For the illustrative 3×2 W, the input Gram WᵀW is 2×2 with eigenvalues (9,1), while the output Gram WWᵀ is 3×3 with (9,1,0). Their nonzero values are the same s², but their index spaces and zero counts differ. No sample interpretation as covariance or 1/n normalization has been added.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The original nilpotent matrix zero three zero zero sends the unit circle to the output segment from minus three to three although its spectral radius is zero.](../../figures/assets/A09-RMT/A09-RMT-07-zero-spectral-radius-nonzero-amplification.svg)

<figcaption>The image of the unit circle under the existing W=[[0,3],[0,0]] is a horizontal output segment. The vector v=(0,1)ᵀ maps to Wv=(3,0)ᵀ, and the largest singular value is 3, but the eigenvalues and spectral radius are 0. Do not judge amplification over all inputs from eigenvalues alone.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Scaling a diagonal first layer by two and dividing an identity second layer by two changes their largest singular values from three one to six one half while keeping the product value three.](../../figures/assets/A09-RMT/A09-RMT-07-compensated-layer-rescaling.svg)

<figcaption>This illustration uses W₁=diag(3,1), W₂=I₂, and a=2. The largest singular values of W₁'=2W₁ and W₂'=W₂/2 are 6 and 1/2, but W₂'W₁'=W₂W₁ retains singular values (3,1). This calculation concerns two linear layers, not an unconditional claim about entire nonlinear architectures.</figcaption>

</figure>

### Activation covariance describes variance over observed inputs

For an activation matrix $H_c\in\mathbb R^{n\times d_h}$, the covariance

$$
C_h=\frac1nH_c^\top H_c
$$

measures hidden-feature variance under a specified input distribution. Rows are input/token observations, and columns are hidden features. For a unit feature direction $v$, we have $v^\top C_hv=\lVert H_cv\rVert^2/n$, so a covariance eigenvalue is directional variance in the observed representation. It does not directly describe map amplification for arbitrary inputs as a weight singular value does.

Layer width, token sampling, centering, and normalization change the spectrum. Multiplying all hidden values by $a$ multiplies the eigenvalues by $a^2$, and using a sample mean instead of a sum introduces a factor of $1/n$. Feature-wise standardization applies different scales to different directions and can also change eigenvectors. State whether a comparison uses raw covariance or standardized covariance corresponding to correlation.

An activation spectrum is variance obtained by projecting observed rows onto directions. Feature-wise rescaling produces geometry different from a single overall multiplier.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Three centered illustrative hidden observations project onto feature direction e two with values minus one minus one two whose squared mean is two.](../../figures/assets/A09-RMT/A09-RMT-07-activation-values-and-directional-variance.svg)

<figcaption>The illustrative centered rows (−1,−1), (1,−1), (0,2) are plotted in hidden-feature coordinates, then their projections onto v=e₂ are collected. Since Hcv=(−1,−1,2)ᵀ, we have vᵀChv=6/3=2. This is variance under the observed distribution, not weight-map amplification for arbitrary inputs.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Exact covariance contours for a raw two feature covariance nine two two one and its standardized correlation covariance show different principal directions.](../../figures/assets/A09-RMT/A09-RMT-07-feature-standardization-rotates-axes.svg)

<figcaption>This illustration compares unit ellipses for raw covariance [[9,2],[2,1]] and covariance [[1,2/3],[2/3,1]] after division by feature standard deviations (3,1). Applying different feature scales changes the principal directions too. The lines describe covariance geometry, not actual sample density contours or model observations.</figcaption>

</figure>

### The Hessian describes loss curvature in parameter directions

The Hessian $\nabla_\theta^2L$ measures the curvature of a specified loss and dataset at a parameter point. If $L$ is twice continuously differentiable near that point, the Hessian is symmetric, and the expansion for a parameter perturbation $tv$ is

$$
L(\theta+tv)=L(\theta)+t\nabla L(\theta)^\top v
+\frac{t^2}{2}v^\top\nabla_\theta^2L\,v+o(t^2)
$$

When the gradient is 0, the quadratic term along a unit eigenvector is proportional to its eigenvalue. A negative eigenvalue means negative loss curvature, not negative covariance variance. At a point where the gradient is not 0, the first-order term must also be considered.

Symmetry and overparameterization can create zero or near-zero directions, but they do not guarantee them in every large model. Even if the loss is constant along a function-preserving curve, the curve's bending and the gradient term can contribute. Do not call its tangent a Hessian null vector without checking whether the point is stationary.

Changing the loss from a sum to a mean also multiplies the Hessian by $1/n$. Under a linear reparameterization $\theta=B\eta$, we have $\nabla_\eta^2L=B^\top(\nabla_\theta^2L)B$, so nonorthogonal rescaling changes the eigenvalues. Do not read sharpness as a coordinate-independent property of the same model function. The Hessian is indexed by $p$ parameter coordinates, not hidden features, and its units are loss/parameter squared.

A Hessian-vector product avoids storing the full $p\times p$ matrix and, for a specified $v$, computes $\nabla_\theta^2L\,v$. Methods that repeat these products estimate some extreme eigenvalues; this does not mean they recover the full spectrum. For an indefinite Hessian, simple power iteration can track the eigenvalue with the largest absolute value, which must be distinguished from the largest positive eigenvalue. We run no eigensolver or new model computation here.

First examine signed loss curvature and the coordinate and stationarity conditions. Then distinguish a specified HVP and some extreme directions from the full spectrum.

<figure class="lesson-figure" markdown="1">

![At a stationary parameter point exact quadratic directional loss changes with eigenvalues two zero and minus one curve upward stay flat and curve downward.](../../figures/assets/A09-RMT/A09-RMT-07-stationary-loss-curvature-signs.svg)

<figcaption>The illustrative directional quadratics ΔL(t)=λt²/2 with gradient 0 are compared for λ=2,0,−1. The downward curve is negative loss curvature, not negative activation variance. Only the quadratic term at the stationary point specified in this lesson is shown.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![For the exact illustrative loss theta two minus theta one squared the constant zero loss parabola has horizontal tangent at zero while the Hessian tangent action is minus two e one.](../../figures/assets/A09-RMT/A09-RMT-07-constant-loss-curve-nonnull-tangent.svg)

<figcaption>For the illustrative L(θ₁,θ₂)=θ₂−θ₁², the curve (t,t²) always has loss 0. Its tangent at the origin is e₁, but gradient=(0,1)ᵀ and Hessian e₁=−2e₁, so the tangent is not a null vector. The figure separates the conditions involving both curve bending and gradient.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![The same loss written as theta squared over two and after theta equals two eta as two eta squared has coordinate Hessians one and four.](../../figures/assets/A09-RMT/A09-RMT-07-coordinate-rescaling-changes-curvature.svg)

<figcaption>Rewriting the illustrative L(θ)=θ²/2 with θ=2η gives L(η)=2η² and changes the Hessian from 1 to 4. The number 1 on a θ or η axis does not represent the same physical perturbation. Do not interpret the sharpness of the same function as coordinate-independent.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Two exact diagonal Hessians with spectra minus four two and minus four ten give the same product minus four e one for e one although their positive spectra differ.](../../figures/assets/A09-RMT/A09-RMT-07-one-hvp-does-not-fix-the-spectrum.svg)

<figcaption>The illustrative H₁=diag(−4,2) and H₂=diag(−4,10) both give He₁=−4e₁ but have different other eigenvalues. This distinguishes a single HVP from knowledge of the full spectrum. No eigensolver or model Hessian computation was run.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![For a fixed diagonal Hessian minus four two the algebraic normalized powers of a vector one one increasingly align with the negative four direction rather than positive two.](../../figures/assets/A09-RMT/A09-RMT-07-power-magnitude-versus-positive-eigenvalue.svg)

<figcaption>For the illustrative H=diag(−4,2) and v₀=(1,1)ᵀ/√2, the squared direction fractions of Hᵏv₀ are calculated from exact formulas. The fraction in the −4 direction grows as 1/(1+4⁻ᵏ), while that in direction 2 shrinks. This distinguishes the largest magnitude tracked by power iteration from the largest positive value; it is not a result from running a new eigensolver.</figcaption>

</figure>

### Different nulls and claims for different matrices

Weights need a random matrix matched in entry variance and row/column scales; activations need a covariance null matched in sample structure; Hessians need controls with labels, data, and checkpoint fixed. Do not reuse a single null for all three objects.

First fix map shape and scale for weights, row sampling and feature normalization for activations, and objective and parameter point for Hessians. Then specify which structure the null is intended to remove. Simply permuting weight rows or columns preserves the singular values, so it does not provide a random-noise null for the spectrum. A Hessian control that changes labels changes the loss itself and therefore asks a different question from curvature uncertainty for the original dataset.

Observing long tails in all three also does not establish a shared mechanism. A large weight $s_j$ describes map amplification; a large covariance $\lambda_j$ describes sampled variance; and a large positive Hessian $\lambda_j$ describes local curvature. A functional relation requires separately checking how input distribution, layer composition, and loss changes connect these objects.

## Small example

If $W$ has singular values $(3,1)$, the nonzero eigenvalues of $W^\top W$ are $(9,1)$. Comparing these numbers with activation covariance eigenvalues does not yield a functional conclusion, because the units and indices differ.

Reporting these $(9,1)$ as singular values of $W$ itself would incorrectly apply the square once more. The same eigenvalue 9 can mean variance in a hidden direction for activations and curvature in a parameter direction for the Hessian. Equal numbers do not mean that the same object was perturbed or observed.

## Common misconceptions

- Singular values, rather than eigenvalues, are the general comparison object for rectangular weight matrices.
- A sharp Hessian direction is not necessarily a frequently used activation feature.

## Exercises

### 1. Singular spectrum
If the singular values of $W$ are $(4,2,0)$, give the nonzero eigenvalues of $W^\top W$.
<details><summary>Show solution</summary>

Squaring the singular values gives $(16,4)$.
</details>

### 2. Activation covariance
If $H_c$ is $200\times64$, what are the shape of $C_h$ and its rank upper bound?
<details><summary>Show solution</summary>

The shape of $C_h$ is $64\times64$, and its rank is at most 64.
</details>

### 3. Hessian sign
If the Hessian has a negative eigenvalue, can the parameter point be a strict local minimum?
<details><summary>Show solution</summary>

No. There is second-order negative curvature in the corresponding eigenvector direction.
</details>

### 4. Model interpretation
The weight and activation spectra both appear heavy-tailed. Can this be called evidence of the same mechanism?
<details><summary>Show solution</summary>

No. The matrices, normalizations, and nulls differ, so each tail fit and the functional relation must be checked separately.
</details>

## Evidence and update boundaries

This lesson distinguishes the measurement objects of the three spectra. Heavy-tail exponent fitting, free probability, and the detailed theory of large-scale Hessian eigensolvers are outside its scope.

For the computation of Hessian-vector products without storing the full matrix, see §2–3 of [Pearlmutter, Fast Exact Multiplication by the Hessian](https://www.bcl.hamilton.ie/~barak/papers/nc-hessian.pdf). The other relations involving SVD, covariance, Taylor expansion, and linear reparameterization are developed from prerequisite formulas using this lesson's indices.

## Lesson summary

- Use the singular spectrum for weights.
- The activation covariance spectrum depends on the sampled input distribution.
- The Hessian spectrum describes loss curvature for the data at a parameter point.
- The three objects require different normalizations and null models.

## Pass criteria

- Can you specify the indices and units of each matrix's spectrum?
- Can you avoid overclaiming a common mechanism from one spectral pattern?

## Next lesson

- [A09-RMT-08 Capstone: null models for spectra](A09-RMT-08-capstone-spectrum-null-model.md)

## Author checklist

- [x] The objects described by weight, activation, and Hessian spectra are distinguished.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
