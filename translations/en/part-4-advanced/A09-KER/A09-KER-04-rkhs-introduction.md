---
id: "A09-KER-04"
title: "Introduction to RKHS"
part: 4
stage: "A09-KER"
status: "complete"
prerequisites: ["A09-KER-01", "A09-KER-02", "A09-KER-03"]
estimated_time: "90–120 minutes"
---

# A09-KER-04. Introduction to RKHS

## Why this lesson matters

A positive semidefinite kernel determines a Hilbert space of functions. In this space, point evaluation can be expressed as an inner product. Understanding the reproducing property and RKHS norm explains why a kernel regression solution can be written as a sum of kernel sections centered on training samples.

## Learning objectives

- Write the reproducing property of an RKHS.
- Explain the role of the kernel section $k(x,\cdot)$.
- Explain the RKHS norm as a kernel-dependent complexity measure.
- Express the representer theorem's conclusion as a finite expansion.

## Prerequisite check

- Prerequisite lessons: [A09-KER-01 Function spaces and operators](A09-KER-01-function-spaces-operators.md), [A09-KER-02 Positive definite kernel](A09-KER-02-positive-definite-kernel.md), [A09-KER-03 Feature maps and the kernel trick](A09-KER-03-feature-map-kernel-trick.md)
- Check question: For a vector $v$, why is the inner product $\langle w,v\rangle$ a linear functional of $w$?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $\mathcal H_k$ | `the R K H S associated with k` | Reproducing kernel Hilbert space determined by kernel $k$ | function space |
| $k_x(\cdot)=k(x,\cdot)$ | `the kernel section at x` | Function representing evaluation | element of $\mathcal H_k$ |
| $f(x)=\langle f,k_x\rangle_{\mathcal H_k}$ | `f of x equals the inner product of f and k sub x in H sub k` | reproducing property | scalar identity |
| $\lVert f\rVert_{\mathcal H_k}$ | `the R K H S norm of f` | Function complexity relative to the kernel | nonnegative scalar |

## Core concepts

### What bounded evaluation means

A Hilbert space is a complete vector space whose norm comes from an inner product: limits of Cauchy sequences in that norm remain in the space. A Cauchy sequence is one whose sufficiently late terms have arbitrarily small norm distances from one another. This lesson uses a space formed by giving functions an inner product, without proving completeness. In an RKHS (reproducing kernel Hilbert space) $\mathcal H_k$, each fixed $x$ has a bounded linear evaluation functional $f\mapsto f(x)$. That is, a finite constant for that $x$ bounds $|f(x)|$ in proportion to $\|f\|_{\mathcal H_k}$. This condition means that functions close in norm also have close evaluation values at that point.

Continuous here refers to continuity of evaluation as $f$ changes in norm. It does not define continuity as the input $x$ changes for every $f(x)$; that property requires additional conditions on the kernel or other objects. The Riesz representation expresses a bounded linear functional on a Hilbert space as an inner product with a vector in the space. Thus, there is a function $k_x\in\mathcal H_k$ representing evaluation, with

$$
f(x)=\langle f,k_x\rangle_{\mathcal H_k}
$$

The section $k_x$ fixes the specified location $x$ and returns values at other inputs. Distinguish it from the point $x$ itself and the scalar $k(x,x)$.

The next figure places functions in a coefficient plane to show one case where evaluation is an inner product.

<figure class="lesson-figure" markdown="1">

![For the kernel 1+xz, the coefficient vectors of f(z)=1+2z and the section at one are (1,2) and (1,1), whose inner product reproduces f(1)=3](../../figures/assets/A09-KER/A09-KER-04-reproducing-coordinates.svg)

<figcaption>The blue and purple arrows are function coefficients, not input points. This kernel's inner product is the coefficient inner product, so the arrows' inner product 3 returns f(1).</figcaption>
</figure>

### Kernel sections and the reproducing property

The function $k_x(\cdot)=k(x,\cdot)$ is called a kernel section. Substituting $f=k_{x'}$ in the inner product above gives $k(x',x)=\langle k_{x'},k_x\rangle_{\mathcal H_k}$. In particular, $\|k_x\|_{\mathcal H_k}^2=k(x,x)$. Cauchy–Schwarz gives

$$
|f(x)|\le\|f\|_{\mathcal H_k}\sqrt{k(x,x)}
$$

which identifies a finite constant for evaluation. Reproducing means recovering a function value through an inner product. Every PSD kernel has a corresponding RKHS with this property. The construction starts by giving finite linear combinations of kernel sections the inner product $\langle k_x,k_z\rangle=k(x,z)$ and completing the space to include limits in that norm. The construction's detailed proof is outside this lesson's scope.

The next two figures show the shape of a section as a function and the geometry of the evaluation bound separately.

<figure class="lesson-figure" markdown="1">

![Gaussian kernel sections centered at zero and one are functions of the free argument z, with their centers fixed and their values changing across z](../../figures/assets/A09-KER/A09-KER-04-kernel-sections.svg)

<figcaption>Fixing the location at 0 or 1 gives different sections. Each curve is a function defined across z, not just the value at its peak.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![A unit-norm function coefficient vector (0.6,0.8) has evaluation 1.4 against the section vector (1,1), bounded by square root two](../../figures/assets/A09-KER/A09-KER-04-evaluation-bound.svg)

<figcaption>The dashed circle is the boundary for function norm 1. The inner product 1.4 of the blue function and purple section is no larger than the section's length √2.</figcaption>
</figure>

### Regularization removes directions outside the finite span

Consider the regularized empirical risk

$$
\min_{f\in\mathcal H_k}
\frac1n\sum_{i=1}^n \ell(f(x_i),y_i)+\lambda\lVert f\rVert_{\mathcal H_k}^2
$$

Assume $\lambda>0$ and that a function attaining the minimum exists. The loss depends only on the training values $f(x_i)$. Every minimizer then has the form

$$
\hat f(\cdot)=\sum_{i=1}^n\alpha_i k(x_i,\cdot)
$$

To see why, decompose $f$ into a part parallel to the span of the training sections and a part orthogonal to that span. The orthogonal part has inner product 0 with every $k_{x_i}$, so the reproducing property gives value 0 at every training point. Removing that part therefore leaves training predictions and loss unchanged. In an orthogonal decomposition, however, the squared norm is the sum of the two parts' squared norms. If the orthogonal part is not 0, removing it reduces the penalty. A minimizer with $\lambda>0$ cannot retain this part.

This is the representer theorem's finite-expansion conclusion. It does not guarantee existence of a solution, coefficient values, or performance on an independent test set. If the sections are linearly dependent, different $\alpha$ may represent the same function. If the loss also depends on function values at other inputs, derivatives, or similar quantities, the argument using only these training sections does not apply unchanged.

The next two figures distinguish changes in norm from changes in training values when the component orthogonal to the training sections is removed.

<figure class="lesson-figure" markdown="1">

![For kernel 1+xz and the training input zero, function coefficients (2,1) decompose into a horizontal training-span part (2,0) and an orthogonal part (0,1)](../../figures/assets/A09-KER/A09-KER-04-representer-projection.svg)

<figcaption>The span of the training section k₀=(1,0) is the horizontal axis. Removing the purple orthogonal component reduces the squared norm from 5 to 4.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![Functions 2+z and its training-section projection 2 both predict 2 at the training input zero, although they differ elsewhere](../../figures/assets/A09-KER/A09-KER-04-training-values-preserved.svg)

<figcaption>At training input 0, both curves have value 2. Removing the orthogonal component leaves training loss unchanged, although values at other inputs may change.</figcaption>
</figure>

### RKHS norm versus coefficient norm

For $f=\sum_i\alpha_i k_{x_i}$, expanding the inner product gives $\|f\|_{\mathcal H_k}^2=\sum_{i,j}\alpha_i\alpha_j k(x_i,x_j)=\alpha^\top K\alpha$. This is not the squared Euclidean norm of $\alpha$: it incorporates the kernel Gram geometry. A small norm constrains complexity in the function space defined by that kernel. It does not mean low average prediction error or simplicity from every perspective.

When changing the kernel, first check whether the same function belongs to the new RKHS. Even if it belongs to both, its norm and the interpretation of smoothness may differ. This is why norms for Gaussian kernels with different bandwidths should not be compared as though they shared one absolute scale.

The next figure shows the same function x with different norms under two kernels.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The same function f(x)=x uses feature x with coefficient one for kernel xz, or feature 2x with coefficient one half for kernel 4xz, giving squared RKHS norms one and one quarter](../../figures/assets/A09-KER/A09-KER-04-kernel-relative-norm.svg)

<figcaption>The two green points show the same input 0.5 and output 0.5. Changing feature scale together with the kernel changes the same function's squared norm from 1 to 1/4.</figcaption>
</figure>

## Small example

For $f=2k_{x_1}-k_{x_2}$, the reproducing property immediately gives

$$
f(z)=2k(x_1,z)-k(x_2,z)
$$

No separate coordinate representation is needed.

The coefficients 2 and $-1$ determine how much of each section is added or subtracted. To evaluate the function, evaluate each section at the new point $z$ and combine the values. The same function's squared norm is $4k(x_1,x_1)+k(x_2,x_2)-4k(x_1,x_2)$. The sum of evaluation values and the quadratic form for the function norm use the same kernel but are different calculations.

The next figure shows the weighted sum of two Gaussian sections as an entire function.

<figure class="lesson-figure" markdown="1">

![Twice the Gaussian section at zero minus the section at one forms a green function with value about 0.775 at z=0.5 and squared RKHS norm about 3.558](../../figures/assets/A09-KER/A09-KER-04-section-combination.svg)

<figcaption>Adding the blue and purple values at the same z gives the green function value. The squared norm below the figure is not a curve height; it is calculated from kernel inner products between sections.</figcaption>
</figure>

## Common misconceptions

- A function with a small RKHS norm cannot be called simple from every perspective. Simplicity is relative to the kernel.
- The representer theorem determines the solution's form under the chosen loss and regularizer; it does not automatically guarantee coefficient values or generalization.

## Exercises

### 1. Reproducing
For $f=3k_a+2k_b$, write $f(x)$ in terms of kernel values.
<details><summary>Show solution</summary>

It is $f(x)=3k(a,x)+2k(b,x)$.
</details>

### 2. Inner product
Find $\langle k_a,k_b\rangle_{\mathcal H_k}$.
<details><summary>Show solution</summary>

By the reproducing property, it is $k(a,b)$.
</details>

### 3. Finite expansion
With 20 training samples, how many kernel sections are needed at most in the representer form?
<details><summary>Show solution</summary>

At most 20, one for each training sample. Fewer may be needed if some coefficients are 0.
</details>

### 4. Model interpretation
Two representations use the same Gaussian kernel form but different bandwidths. Can their RKHS norms be compared directly?
<details><summary>Show solution</summary>

Kernels with different bandwidths define different function-space geometries. The norm scale and preferred functions differ, so match kernel parameters or perform separate calibration.
</details>

## Evidence and update boundaries

This lesson covers scalar-valued RKHSs and the representer form for quadratic norm regularization. Proofs of Hilbert-space completeness and vector-valued RKHSs are outside its scope.

- [Stanford STATS305C, RKHS](https://web.stanford.edu/class/stats305c/lectures/RKHS.html): Used to check the reproducing property, preservation of training values, and the representer argument for norm regularization through orthogonal projection.

## Lesson summary

- In an RKHS, evaluation is calculated as an inner product with a kernel section.
- A kernel section is a function centered on a sample location.
- The representer form writes the solution as a finite expansion based on training samples.
- The meaning of the RKHS norm depends on the kernel choice.

## Pass criteria

- Can you calculate function values and inner products using the reproducing property?
- Can you explain the RKHS norm as kernel-relative complexity?

## Next lesson

- [A09-KER-05 Introduction to spectrum and compact operators](A09-KER-05-spectrum-compact-operators.md)

## Author checklist

- [x] The reproducing property, kernel sections, and representer form are connected.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
