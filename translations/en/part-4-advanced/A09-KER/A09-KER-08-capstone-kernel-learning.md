---
id: "A09-KER-08"
title: "Capstone: learning from the kernel perspective"
part: 4
stage: "A09-KER"
status: "complete"
prerequisites: ["A09-KER-01", "A09-KER-02", "A09-KER-03", "A09-KER-04", "A09-KER-05", "A09-KER-06", "A09-KER-07"]
estimated_time: "120–180 minutes"
---

# A09-KER-08. Capstone: learning from the kernel perspective

## Why this lesson matters

Kernel analysis does not end with plotting a Gram matrix. Connecting spectra to learning dynamics requires fixing input units, centering, normalization, targets, checkpoints, and the null model. This capstone establishes a contract for checking how well empirical NTK predictions match actual output changes.

## Learning objectives

- Design a checkpoint-wise empirical NTK analysis contract.
- Calculate kernel spectra and target alignment.
- Compare linearized predictions with actual training trajectories.
- Report results within the specified parameterization and sampled inputs.

## Prerequisite check

- Prerequisite lessons: [A09-KER-01–07](A09-KER-07-parameter-function-space.md)
- Check question: Why is it difficult to predict all of a finite network's training from the initialization NTK spectrum alone?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $K_t$ | `K at checkpoint t` | Empirical NTK at checkpoint $t$ | $n\times n$ |
| $\widetilde K_t$ | `the centered normalized kernel at checkpoint t` | Kernel preprocessed for comparison | $n\times n$ |
| $a_j=u_j^\top y$ | `a sub j equals u sub j transpose y` | Kernel eigenmode coefficient of the target | scalar |
| $e_{\mathrm{lin}}(t)$ | `the linearization error at time t` | Difference between linearized predictions and actual outputs | nonnegative scalar |
| $b_j=u_j^\top(y-f_0)$ | `b sub j equals u sub j transpose times the quantity y minus f at zero` | Mode coefficient of the initial target residual | scalar |

## Analysis contract

Write a contract for training a small scalar-output MLP with two seeds, the same data order, and the same optimizer settings. This lesson does not execute new training or assume results. Record the order of the fixed $n$ inputs, scalar target $y$, and initialization output $f_0$, then compare Jacobians at several checkpoints on those same inputs. Changing sample rows changes what kernel entries refer to, so preserve order across all checkpoints.

The prediction formulas below assume full-batch ordinary gradient descent, summed squared loss $\tfrac12\lVert f-y\rVert^2$, and no additional regularization. Also record the learning rate, parameter arrays, and dtype. Do not apply these formulas unchanged to results using mini-batches, adaptive optimizers, or other losses.

If transforming output scale, specify the rules for targets and outputs first and fix them across all checkpoints. Renormalizing outputs post hoc at each checkpoint and comparing them with the original Jacobian does not measure the same dynamics. Manage kernel centering and normalization separately as preprocessing for structural comparisons. For learning-speed predictions, use the original $K_t=J_tJ_t^\top$ and the loss normalization.

Samples are input-comparison units, whereas seeds repeat training with changed initialization. When using several tokens from the same prompt, make prompts the highest-level uncertainty units. Two seeds show differences between seeds, but that number alone does not guarantee a stable seed distribution or precise confidence intervals.

## Measurement procedure

1. Calculate $J_t\in\mathbb R^{n\times p}$ and $K_t=J_tJ_t^\top$ at each checkpoint. Check numerical symmetry, dtype, and a PSD tolerance appropriate to matrix scale.
2. For spectra and effective dimensions connected to a population operator, use $K_t/n$ and set $\tau$ on the same scale. For fixed-kernel dynamics, use the summed loss's $K_0$. Distinguish target coefficients from initial residual coefficients.
3. Record kernel drift for structural comparison separately from changes in the original kernel's scale.
4. Compare fixed $K_0$ predictions with actual outputs using the same initialization, targets, and learning rates. Distinguish this from Taylor predictions using the actual parameter path.
5. Distinguish a label-permutation alignment null from an input-order consistency control.
6. Define a hidden-unit permutation control that preserves the function and NTK, and examine changes in raw parameter distance.

### Target coefficients and learning residuals

Using an orthonormal eigenvector basis with $K_0u_j=\lambda_ju_j$, the coefficient $a_j=u_j^\top y$ describes the target itself. The difference learning must reduce is $y-f_0$, whose coefficient is $b_j=a_j-u_j^\top f_0$. If $f_0$ is not 0, do not interchange $a_j$ and $b_j$. Residuals in zero-eigenvalue modes persist under fixed-kernel flow. To infer fit from a spectrum, we also need to know which modes contain residuals and how much.

In the numerical figure below, a mode already fitted has initial residual 0 even though its target coefficient is nonzero.

<figure class="lesson-figure" markdown="1">

![Target, initial output, and target residual coefficients compared in a fixed identity eigenbasis](../../figures/assets/A09-KER/A09-KER-08-target-versus-residual.svg)
<figcaption>This calculation uses U=I, y=(2,1), and f₀=(1,1). The target has two modes, but the difference y−f₀ that must actually be reduced lies only in the first mode.</figcaption>
</figure>

An eigenvector's sign can change, and bases can change within an eigenspace with repeated eigenvalues. Rather than comparing only coefficient signs or individual axes, use squared coefficients and their sum within repeated-eigenvalue subspaces. Local alignment obtained by recomputing an eigenbasis at each checkpoint is a different record from residual decay tracked along fixed $u_j$.

The next basis rotation shows that individual coefficients of the same residual can change while its total amount within the subspace is preserved.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A fixed residual vector represented in two orthonormal bases of the same repeated-eigenvalue eigenspace](../../figures/assets/A09-KER/A09-KER-08-eigenspace-basis.svg)
<figcaption>Rotating the basis by 45° in the eigenspace of K=λI changes coefficients (1,0) to (1/√2,−1/√2). Neither the vector nor the squared-coefficient sum 1 changes.</figcaption>
</figure>

### Structural drift and scale drift

For example, center using $H=I-\mathbf1\mathbf1^\top/n$ and normalize with $\widetilde K_t=HK_tH/\lVert HK_tH\rVert_F$. If the denominator is 0, leave the normalized kernel undefined and record that fact. When calculating target alignment with a centered kernel, also match the target and residual by using $Hy$ and $H(y-f_0)$, respectively.

First examine a case where centering removes every component.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An all-ones sample kernel and its zero centered matrix with an undefined normalization denominator](../../figures/assets/A09-KER/A09-KER-08-zero-centered-kernel.svg)
<figcaption>If all samples have the same features and K's entries are 1, HKH is 0. The denominator is 0, so the normalized kernel cannot be defined. Do not record a 0 matrix as the normalization result.</figcaption>
</figure>

The quantity $\lVert\widetilde K_t-\widetilde K_0\rVert_F$ measures changes in the shape of centered geometry. If $K_t=cK_0$ with $c>0$, this drift may be 0 while the learning speed for summed loss changes by a factor of $c$. Record $\lVert K_t\rVert_F$ and raw drift as well. Use relative raw drift $\lVert K_t-K_0\rVert_F/\lVert K_0\rVert_F$ only when $\lVert K_0\rVert_F>0$.

The next two kernels have the same normalized shape but different raw eigenvalues and decay rates.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Raw eigenvalue scales of a centered kernel and three times that kernel compared with different residual decay rates](../../figures/assets/A09-KER/A09-KER-08-structure-versus-scale.svg)
<figcaption>Dividing K₀ and 3K₀ by their Frobenius norms gives the same matrix. But their positive-mode raw eigenvalues are 2 and 6, so the same initial residual decays at rates differing by a factor of three.</figcaption>
</figure>

### What is predicted along which path?

Let the eigenvectors $u_j$ be the columns of matrix $U$. The continuous-time reference is $\widehat f_t=y+U\operatorname{diag}(\exp(-\lambda_jt))U^\top(f_0-y)$. For comparison with actual full-batch steps, form the fixed-kernel prediction at iteration $s$ as

$$
\widehat f_{s+1}=\widehat f_s-\eta_sK_0(\widehat f_s-y),\qquad
\widehat f_0=f_0
$$

For averaged loss, replace the kernel with $K_0/n$. The same initial conditions and steps are needed to distinguish kernel approximation error from mismatched time or loss scales. Define $e_{\mathrm{lin}}(t)=\lVert\widehat f_t-f_t\rVert/\sqrt n$ as the per-sample root-mean-square difference for this prediction.

By contrast, $f_0+J_0(\theta_t-\theta_0)$ applies the initial Taylor formula along the actual parameter path. Comparing this with $f_t$ examines the first-order remainder along that path. A fixed-kernel model predicts its own update path, so do not combine these comparisons into the same error. When drift and the two errors behave differently, check scale, the loss/step contract, and the remainder separately.

The following analytic toy model shows that the two predictions are not the same curve. These are not new network experiment results.

<figure class="lesson-figure" markdown="1">

![Analytic nonlinear gradient flow compared with a fixed initial kernel prediction and a Taylor prediction along the actual parameter path](../../figures/assets/A09-KER/A09-KER-08-two-predictions.svg)
<figcaption>For fθ(1)=θ², θ₀=1, target 0, and loss ½f², the parameter path is θ(t)=1/√(1+4t). Distinguish the original output θ(t)², the fixed-K₀=4 prediction exp(−4t), and Taylor output 1+2(θ(t)−1) applied along the actual path.</figcaption>
</figure>

### Roles of null and symmetry controls

Fixing initial $K_0$ and shuffling the sample-to-label correspondence preserves the spectrum while changing only target/residual alignment. Interpreting this null as a statistical test requires assuming that labels are exchangeable within the relevant sampling units. Permutation with $K_t$ fixed after training on original labels is a conditional diagnostic of geometry that already reflects labels. It is not the null for the entire training pipeline; specify whether training is repeated with changed labels when designing a full-pipeline null.

Reordering input rows with a permutation matrix $\Pi$ changes the kernel to $\Pi K\Pi^\top$, preserving the spectrum. Applying the same $\Pi$ to targets and initialization outputs also preserves alignment. This is an implementation consistency control. Changing inputs alone while leaving targets unchanged breaks correspondences and is a separate control; do not confuse the procedures.

The next figure compares shuffling labels alone with moving rows while preserving sample correspondences.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three sample kernels showing original labels, a label permutation with fixed kernel, and a matched row-and-label permutation](../../figures/assets/A09-KER/A09-KER-08-permutation-controls.svg)
<figcaption>Here f₀=0 and eigenvalues are ordered as (4,1). The label null moves target energy from (4,0) to (0,4), while the consistency control that reorders the kernel and labels together preserves (4,0).</figcaption>
</figure>

Hidden-unit permutation preserves the same function when incoming and outgoing weights and biases are all changed consistently. It is an orthogonal permutation of the full trainable parameter vector, so Euclidean NTK is preserved as well. Raw parameter distance may change, but output and NTK differences should remain within numerical tolerance. This conclusion concerns permutation controls; do not extend it to cases such as the preceding lesson's scaling symmetry, where the function is preserved but NTK can change.

## Results table

| Measurement | Question it answers | Interpretive limitation |
|---|---|---|
| NTK spectrum | Local learning modes on sampled inputs | feature semantics |
| target alignment | Which modes contain the label residual? | population generalization |
| kernel drift | How much does the fixed-kernel approximation change? | Cause of drift |
| linearization error | Predictive fit of $K_0$ dynamics | Other optimizer regimes |
| symmetry control | Non-identifiability of raw parameter distance | All reparameterizations |

Large NTK eigenvalues, large initial-residual coefficients, small structural drift, and small output-prediction error are observations that cannot substitute for one another. Identical normalized geometry can still have different scales, and stable geometry does not fit a residual in a zero mode. Report these connections with numbers, but do not fill unmeasured cells with expected results. Without evaluation on unseen inputs, limit conclusions to local geometry and fit on the sampled training inputs.

The figure shows why a common spectrum alone does not determine the two fitting outcomes.

<figure class="lesson-figure" markdown="1">

![Equal fixed kernel spectra with a decaying positive-mode residual and a persistent null-mode residual](../../figures/assets/A09-KER/A09-KER-08-spectrum-not-fit.svg)
<figcaption>Even with K=diag(4,0) fixed, initial residual (1,0) decays, whereas (0,1) persists. These are calculated training-mode outcomes, not performance on unseen inputs.</figcaption>
</figure>

## Common misconceptions

- Similar centered normalized kernels do not establish the same output function.
- High target alignment is not generalization evidence without checks on a test split and null labels.

## Exercises

### 1. Unit
You obtain 1,000 tokens from the same 20 prompts. What should be the highest-level resampling unit for uncertainty calculations?
<details><summary>Show solution</summary>

Tokens from the same prompt are dependent, so use prompts as the highest-level resampling units.
</details>

### 2. PSD
A numerically calculated $K$ has minimum eigenvalue $-10^{-10}$ and maximum eigenvalue $20$. What should you check first?
<details><summary>Show solution</summary>

Check whether $K$ was symmetrized as $(K+K^\top)/2$, along with dtype and relative tolerance. This magnitude may be floating-point error.
</details>

### 3. Drift
Kernel drift is small, but linearization error has grown. What should you check?
<details><summary>Show solution</summary>

Check whether kernel normalization hides scale changes, whether discrete learning rates and loss assumptions match, and the output offset and Jacobian linearization remainder.
</details>

### 4. Claim
Two seeds have high initial NTK target alignment and fast training, but unseen inputs were not evaluated. How should you limit the conclusion?
<details><summary>Show solution</summary>

State that initial tangent geometry aligned with the target residual on the measured training inputs and was observed alongside fast fit. Do not claim population generalization.
</details>

## Evidence and update boundaries

This capstone uses the squared-loss gradient-flow equation as a diagnostic reference for finite-step training. Change the prediction formulas if the optimizer or loss differs, and do not treat NTK results as the representation's unique explanation.

## Lesson summary

- NTK analysis needs a contract including input units and parameterization.
- Spectra, target alignment, and kernel drift are different quantities.
- Fixed-kernel predictions must be compared with actual output trajectories.
- Null labels and symmetry controls reveal interpretive limits.

## Pass criteria

- Can you complete an input–Jacobian–kernel–target–trajectory contract?
- Can you separate spectrum evidence from function-prediction evidence?

## Next lesson

- The next optional module is A09-RMT.

## Author checklist

- [x] The contract for checking kernel spectra against actual training trajectories is complete.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
