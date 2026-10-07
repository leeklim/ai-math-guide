---
id: "A09-KER-06"
title: "Neural tangent kernel"
part: 4
stage: "A09-KER"
status: "complete"
prerequisites: ["M03-11", "N05-06", "A09-KER-03"]
estimated_time: "90–120 minutes"
---

# A09-KER-06. Neural tangent kernel

## Why this lesson matters

The neural tangent kernel measures local coupling between training samples through inner products of parameter gradients. Linearizing a network near initialization expresses squared-loss gradient flow as kernel dynamics. This approximation connects learning theory for wide networks with finite-model diagnostics.

## Learning objectives

- Calculate an empirical NTK from the model Jacobian.
- Write output dynamics for squared-loss gradient flow.
- Explain the assumptions of a fixed-kernel approximation.
- Distinguish NTK similarity from learned feature semantics.

## Prerequisite check

- Prerequisite lessons: [M03-11 Jacobian](../../part-1-foundations/M03/M03-11-jacobian.md), [N05-06 Backpropagation](../../part-2-neural-computation/N05/N05-06-backpropagation.md), [A09-KER-03 Feature maps and the kernel trick](A09-KER-03-feature-map-kernel-trick.md)
- Check question: What kind of vector is the parameter gradient of a scalar output $f_\theta(x)$, with length equal to the number of parameters?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $g_\theta(x)=\nabla_\theta f_\theta(x)$ | `g sub theta of x equals the parameter gradient of f sub theta of x` | Parameter gradient for each input | column $p$-vector for scalar output |
| $K_\theta(x,x')$ | `K sub theta of x and x prime` | neural tangent kernel | scalar |
| $K_\theta=JJ^\top$ | `K sub theta equals J J transpose` | Empirical NTK on training samples | $n\times n$ |
| $\dot f_t$ | `f dot at time t` | Time derivative of training outputs | $n$-vector |

## Core concepts

### Use parameter gradients as features

Fix an input $x$ and differentiate the scalar output $f_\theta(x)$ with respect to parameters $\theta\in\mathbb R^p$. The column gradient $g_\theta(x)$ has $a$th component $\partial f_\theta(x)/\partial\theta_a$. This is not an input gradient. It connects a small parameter change $\Delta\theta$ to the output change through $\Delta f(x)\approx g_\theta(x)^\top\Delta\theta$.

For a scalar-output network, the empirical NTK is

$$
K_\theta(x,x')=\nabla_\theta f_\theta(x)^\top\nabla_\theta f_\theta(x')
$$

It sums the overlap between parameter directions to which the two inputs' outputs are sensitive. Because it includes gradient lengths, it differs from cosine similarity. In the sample Jacobian $J\in\mathbb R^{n\times p}$, if row $i$ is $g_\theta(x_i)^\top$, then $K_\theta=JJ^\top$. For a coefficient vector $c$, therefore, $c^\top K_\theta c=\lVert J^\top c\rVert^2\geq0$. This does not require every entry to be positive.

The next two figures distinguish parameter-gradient directions from the sample matrix formed by their row inner products.

<figure class="lesson-figure" markdown="1">

![Three parameter gradient vectors on a two-dimensional parameter-coordinate grid](../../figures/assets/A09-KER/A09-KER-06-gradient-features.svg)
<figcaption>Compare the inner products of three gradients in a linear toy model. The oppositely directed g₁ and g₃ have NTK entry −1, while g₂ has self-inner-product 2.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A three-by-two sample Jacobian and its three-by-three sample Gram matrix with numerical entries](../../figures/assets/A09-KER/A09-KER-06-gradient-gram.svg)
<figcaption>J's columns index parameters; both indices of JJᵀ index samples. This Gram matrix is PSD despite its negative entries.</figcaption>
</figure>

Using only one sample $x_j$ with residual $r_j=f_\theta(x_j)-y_j$, update parameters by $\Delta\theta=-\eta r_jg_\theta(x_j)$. The change at another sample is $\Delta f(x_i)\approx-\eta r_jK_\theta(x_i,x_j)$. This relation gives NTK its meaning as coupling between samples. If $K_\theta(x_i,x_j)=0$, the first-order effect of this update is 0; it does not follow that the two inputs are semantically unrelated.

In the figure, the same parameter update changes the outputs of three samples differently.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A negative parameter gradient update and output changes of minus one, minus two, and plus one across three samples](../../figures/assets/A09-KER/A09-KER-06-coupled-step.svg)
<figcaption>With ηr₂=1, the update is Δθ=−g₂, and output changes are (−1,−2,+1), the negative of the NTK's second column. This is exact for the linear toy model and a first-order relation for a general network.</figcaption>
</figure>

### Derive output dynamics with the chain rule

Use $f_t=(f_{\theta_t}(x_1),\ldots,f_{\theta_t}(x_n))^\top$ and a fixed label vector $y$. The squared loss $L=\tfrac12\lVert f-y\rVert^2$ is a sum of sample losses, not an average. Its gradient with respect to outputs is $f-y$. Applying the chain rule gives

$$
\nabla_\theta L=J^\top(f-y),\qquad
\dot\theta_t=-J_t^\top(f_t-y)
$$

Continuous-time gradient flow sets parameter velocity to the negative gradient. Differentiating outputs with respect to time again gives

$$
\dot f_t=J_t\dot\theta_t
=-J_tJ_t^\top(f_t-y)
$$

Thus, training outputs follow


$$
\dot f_t=-K_{\theta_t}(f_t-y)
$$

This equation itself holds for finite networks when the network is differentiable in its parameters and uses the loss above and Euclidean gradient flow. No fixed-kernel assumption has been used yet. Averaging the loss by $1/n$ adds a factor $1/n$ on the right. This matches the $K/n$ normalization of the empirical integral operator in the preceding lesson; align it when comparing decay rates across papers.

The next numerical flow shows the chain rule taking a sample vector through a parameter vector and back to a sample vector.

<figure class="lesson-figure" markdown="1">

![A two-sample residual mapped by negative Jacobian transpose to three parameter speeds and back to two output speeds](../../figures/assets/A09-KER/A09-KER-06-chain-rule-shapes.svg)
<figcaption>Mapping r=(1,2) through −Jᵀ gives parameter velocity (−3,−2,0). Multiplying by J again gives output velocity (−3,−5), equal to −Kr. The intermediate and final vectors have different lengths.</figcaption>
</figure>

### A fixed kernel is a separate approximation

A first-order model at initialization $\theta_0$ is

$$
f_\theta^{\mathrm{lin}}(x)
=f_{\theta_0}(x)+g_{\theta_0}(x)^\top(\theta-\theta_0)
$$

This model fixes gradient features at $g_{\theta_0}(x)$. It may be nonlinear in the input, but it is affine in parameter changes, and its NTK is fixed at $K_{\theta_0}$. Approximating the original network's dynamics this way requires checking whether its NTK remains sufficiently stable during training. A numerically small parameter change alone is not a substitute for this condition.

The following parameter sweep compares the original network's kernel with the affine approximation's kernel. It is not a measured training trajectory.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A quadratic network and its affine Taylor approximation alongside a changing neural tangent kernel and its frozen initial value](../../figures/assets/A09-KER/A09-KER-06-current-versus-fixed.svg)
<figcaption>For fθ(x)=θ²x, the affine approximation at θ₀=1 fixes the gradient at 2x. The original network's output retains a (Δθ)² term, and its current NTK at x=1 changes as 4θ².</figcaption>
</figure>

Let an exactly fixed kernel $K_0$ have orthonormal eigenvectors $q_j$ and eigenvalues $\lambda_j\geq0$. For residual $r_t=f_t-y$, the mode coefficient $a_j(t)=q_j^\top r_t$ satisfies

$$
\dot a_j(t)=-\lambda_j a_j(t),\qquad
a_j(t)=\exp(-\lambda_jt)a_j(0)
$$

For the same initial amplitude, a mode with a larger positive eigenvalue decays faster. A residual mode with eigenvalue zero does not decay. If the kernel is only approximately fixed, this fixed-mode solution is also approximate; the same equation cannot be applied unchanged while following changing eigenvectors.

With the same initial residual and only the eigenvalue changed, the next three curves result.

<figure class="lesson-figure" markdown="1">

![Residual mode decay curves for fixed kernel eigenvalues five, one, and zero with equal initial amplitude](../../figures/assets/A09-KER/A09-KER-06-mode-decay.svg)
<figcaption>The mode with λ=5 decays faster than the mode with λ=1, while the mode with λ=0 retains its initial value. The curves calculate gradient flow for a fixed kernel.</figcaption>
</figure>

Jacobians and NTKs may change in finite-width networks. The infinite-width fixed-NTK conclusion is a limit theorem with conditions on architecture, initialization, width scaling, and training, not a rule that automatically applies to every wide model. Also check learning rates and optimizers for finite models. A large learning rate in discrete steps does not guarantee the same stability as continuous-time decay, and adaptive optimizers or additional regularization change the parameter flow itself.

In the following discrete-mode calculation, step size changes the outcome even though the kernel is exactly fixed.

<figure class="lesson-figure" markdown="1">

![Stable and alternating growing discrete residual sequences at learning rates 0.1 and 0.5 for eigenvalue five](../../figures/assets/A09-KER/A09-KER-06-discrete-step-stability.svg)
<figcaption>For λ=5 and η=0.1, the per-step multiplier is 0.5, giving decay. For η=0.5, it is −1.5, giving alternating signs and growth. Continuous decay alone cannot determine discrete stability.</figcaption>
</figure>

### Distinguish learning modes from semantic features

An NTK eigenvector has sample-indexed components. It is neither a neuron's activation coordinate nor a vector in parameter space. The same kernel may have different coordinate representations of its gradient features. Even with a common fixed kernel, different initialization outputs or labels can produce different residual trajectories. In finite training, matching initialization NTKs does not establish matching trajectories; subsequent kernel changes must also be checked. NTK describes local training dynamics but does not determine the semantic identity of neurons or features.

## Small example

For the linear model $f_w(x)=w^\top x$, the parameter gradient is $\nabla_w f_w(x)=x$, so the NTK is $K(x,x')=x^\top x'$. The kernel stays fixed as parameters change, making kernel dynamics exact.

If sample matrix $X$ has rows $x_i^\top$, then $J=X$ and $K=XX^\top$. Distinguishing $p$ parameters from $n$ samples shows that output flow is $n$-dimensional while parameter flow is $p$-dimensional. Exactness here assumes the same squared loss and gradient flow; it does not cover arbitrary optimizers.

## Common misconceptions

- Matching initialization NTKs does not establish matching finite training trajectories throughout.
- An NTK eigenvector is a sample-level learning mode, not one feature in a neuron basis.

## Exercises

### 1. NTK
For the scalar model $f_w(x)=wx$, find the NTK between inputs $x=2$, $x'=3$.
<details><summary>Show solution</summary>

Since $\partial f/\partial w=x$, it is $K(2,3)=2\cdot3=6$.
</details>

### 2. Shape
With 10 samples and 100 parameters, what are the shapes of scalar-output Jacobian $J$ and $JJ^\top$?
<details><summary>Show solution</summary>

The shape of $J$ is $10\times100$, and the empirical NTK is $10\times10$.
</details>

### 3. Eigenmode
Which decays faster under gradient flow: a residual mode with fixed NTK eigenvalue 5 or one with eigenvalue 1?
<details><summary>Show solution</summary>

With the same initial amplitude, the mode with eigenvalue 5 decays faster because the decay rate is proportional to the eigenvalue.
</details>

### 4. Model interpretation
Ablating a layer substantially changes the NTK. Can you conclude that the layer represents a particular concept?
<details><summary>Show solution</summary>

This shows that the ablation changed local parameter-gradient geometry. A concept-representation claim additionally needs labeled behavior, representation controls, and intervention specificity.
</details>

## Evidence and update boundaries

The output dynamics equation is presented for continuous-time gradient flow and squared loss. Discrete optimizers, cross entropy, and multi-output kernels require modifications.

- [Jacot, Gabriel, Hongler, Neural Tangent Kernel](https://arxiv.org/html/1806.07572): Used to check the parameter-derivative kernel in §4, the width, smoothness, and training conditions in Theorem 2, and the least-squares mode dynamics in §5. The text directly expands the chain rule for scalar outputs and a sum-normalized loss.

## Lesson summary

- NTK is the Gram kernel of parameter-gradient features.
- Squared-loss output dynamics apply the current NTK to the residual.
- In a fixed-kernel regime, eigenvalues determine mode-specific learning speeds.
- A finite network's NTK can change during training.

## Pass criteria

- Can you calculate the empirical NTK and its shape from the Jacobian?
- Can you state the assumptions and interpretive limits of a fixed-NTK conclusion?

## Next lesson

- [A09-KER-07 Comparing parameter space and function space](A09-KER-07-parameter-function-space.md)

## Author checklist

- [x] The Jacobian Gram matrix and output dynamics are connected.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
