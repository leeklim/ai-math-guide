---
id: "A09-KER-02"
title: "Positive definite kernels"
part: 4
stage: "A09-KER"
status: "complete"
prerequisites: ["M02-03", "M02-12", "A09-KER-01"]
estimated_time: "90–120 minutes"
---

# A09-KER-02. Positive definite kernels

## Why this lesson matters

Kernel methods collect similarities between sample pairs into a Gram matrix. An arbitrary similarity function does not necessarily behave like an inner product. Checking positive semidefiniteness establishes the geometry needed for optimization and function-space interpretation.

## Learning objectives

- Construct a Gram matrix from a kernel function.
- Test positive semidefiniteness using a quadratic form.
- Compare properties of linear, polynomial, and Gaussian kernels.
- Distinguish kernel values from causal or semantic similarity.

## Prerequisite check

- Prerequisite lessons: [M02-03 Inner products, length, and angles](../../part-1-foundations/M02/M02-03-inner-product-length-angle.md), [M02-12 Symmetric matrices and the spectral theorem](../../part-1-foundations/M02/M02-12-symmetric-matrices-spectral-theorem.md), [A09-KER-01 Function spaces and operators](A09-KER-01-function-spaces-operators.md)
- Check question: What condition does positive semidefiniteness of a symmetric matrix impose on the quadratic form for every vector?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $k(x,x')$ | `k of x and x prime` | Kernel value between two inputs | scalar |
| $K_{ij}=k(x_i,x_j)$ | `K sub i j equals k of x sub i and x sub j` | Sample Gram matrix | $n\times n$ |
| $c^\top Kc$ | `c transpose K c` | Quadratic form of the Gram matrix | nonnegative scalar |
| $\lambda_{\min}(K)$ | `the smallest eigenvalue of K` | Smallest eigenvalue used to diagnose PSD | scalar |

## Core concepts

### A function and its sample matrix

A kernel function $k$ takes two inputs and returns one scalar. Choosing inputs $x_1,\ldots,x_n$ gives a Gram matrix collecting all pairs as $K_{ij}=k(x_i,x_j)$. $k$ is a function defined on all input pairs, whereas $K$ is an $n\times n$ array for the selected sample. Changing the sample gives a different matrix even with the same kernel. An interpretation as real inner-product geometry requires PSD as well as symmetry.

In the figure below, change the inputs to the same kernel and compare the correspondence between rows, columns, and entries.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two finite Gram matrices use the same linear kernel x times z but sample inputs (1,2) and (-1,1), producing different row-column products](../../figures/assets/A09-KER/A09-KER-02-gram-samples.svg)

<figcaption>Each entry is the product of the input for its row and the input for its column. The negative entries on the right also come from a linear kernel.</figcaption>
</figure>

A symmetric function $k:\mathcal X\times\mathcal X\to\mathbb R$ is a positive semidefinite kernel if, for every sample $x_1,\ldots,x_n$ and coefficient vector $c\in\mathbb R^n$,

$$
\sum_{i=1}^n\sum_{j=1}^n c_i c_j k(x_i,x_j)=c^\top Kc\ge 0
$$

The coefficients are not labels. They are arbitrary real weights for combining kernel relationships among inputs. This condition does not require each entry $k(x_i,x_j)$ to be positive. Even with negative inner products, the full quadratic form can be nonnegative. In particular, $n=1$ requires $k(x,x)\ge0$, but positive diagonal entries alone do not prove PSD.

The next figure checks the sign of the quadratic form as the coefficient direction makes a full turn.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Quadratic forms over unit coefficient directions remain nonnegative for two PSD matrices but become negative for a matrix whose entries are all positive](../../figures/assets/A09-KER/A09-KER-02-quadratic-signs.svg)

<figcaption>Although every entry in the middle matrix is positive, its curve falls below zero in some coefficient directions. Testing PSD is not an entrywise sign test.</figcaption>
</figure>

### The scope of tests for a PSD matrix and a PSD kernel

If every eigenvalue of a symmetric Gram matrix is nonnegative, then $c^\top Kc\ge0$ holds for every $c$ on that finite sample. In an eigenbasis, the calculation multiplies each squared coefficient by its eigenvalue and adds the results. The kernel definition, however, must hold for arbitrary sample sizes and locations. Passing a test on one sample does not prove that the entire kernel is PSD. Finding an actual negative quadratic form on one sample can refute the overall PSD claim.

The literature sometimes uses the name positive definite kernel to include the semidefinite condition. The basic condition in this lesson is $\ge0$. When strict positive definiteness is specified separately, it means that $c\ne0$ gives $c^\top Kc>0$ for distinct inputs. Repeating an input creates identical rows and columns, so this strict matrix condition no longer holds. When comparing terminology, check whether strictness is required and whether repeated inputs are permitted.

On the right below, repeating the same input creates identical rows and columns.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Repeating the scalar input one creates equal rows and columns in the linear Gram matrix, so coefficient (1,-1) has zero quadratic form](../../figures/assets/A09-KER/A09-KER-02-duplicate-input.svg)

<figcaption>For repeated inputs, coefficient vector (1,−1) cancels the contributions of the two identical rows. This is one reason to distinguish PSD from strict positivity.</figcaption>
</figure>

### The geometry determined by common kernels

The linear kernel is $k(x,x')=x^\top x'$. Its quadratic form is

$$
\sum_{i,j}c_ic_jx_i^\top x_j
=\left\|\sum_i c_i x_i\right\|_2^2\ge0
$$

so it is PSD on every sample. A large value reflects input norms as well as directional similarity. It is not numerically the same as cosine, which compares directions alone.

The polynomial kernel $(x^\top x'+b)^p$ is PSD when $b\ge0$ and $p$ is a nonnegative integer. For $p=0$, it is defined as the constant kernel 1. It corresponds to an inner product of features incorporating powers and a constant term, with products among input components depending on the degree. For Euclidean distance and $\sigma>0$, the Gaussian kernel is the PSD kernel defined by

$$
k(x,x')=\exp\left(-\frac{\lVert x-x'\rVert^2}{2\sigma^2}\right)
$$

With a smaller $\sigma$, the value decreases faster at the same distance, emphasizing nearby inputs. A larger bandwidth assigns large values over a wider range of inputs. These results are kernel properties under the stated parameter conditions, not rules for every arbitrary similarity function. The full proof that the Gaussian kernel is PSD is outside this lesson's scope.

The next two figures show differences between kernel types and differences in Gaussian bandwidth, respectively.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Linear, degree-two polynomial, and Gaussian kernels give different profiles as the second input varies around the fixed anchor one](../../figures/assets/A09-KER/A09-KER-02-kernel-profiles.svg)

<figcaption>Even with one input fixed at 1, the curve used to compare the second input depends on the kernel choice.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![Gaussian kernels with bandwidths one quarter and one both peak at zero displacement, while the narrower bandwidth decays more quickly](../../figures/assets/A09-KER/A09-KER-02-gaussian-bandwidth.svg)

<figcaption>Both curves have value 1 for identical inputs, but the curve with σ=0.25 decreases faster as the input difference increases.</figcaption>
</figure>

A kernel reflects the geometry of the specified input representation, scale, and parameters. A large kernel value between two activations is an observation that they are close by that calculation's criterion. Equality of label meaning, feature identity, and the model's causal dependence are not part of the value's definition, so they require separate evidence.

## Small example

For $x_1=1$ and $x_2=2$, the linear kernel gives

$$
K=\begin{bmatrix}1&2\\2&4\end{bmatrix}.
$$

Since $K=vv^\top$ with $v=(1,2)^\top$, $c^\top Kc=(v^\top c)^2\ge0$.

For $c=(c_1,c_2)^\top$, the value is therefore $(c_1+2c_2)^2$. Substituting $c=(2,-1)^\top$ gives zero even though $c\ne0$, so this matrix is PSD but not strictly positive definite. Its eigenvalues are 0 and 5. Even with two distinct scalar inputs, the Gram matrix need not have full rank because there is only one linear feature direction.

In the figure below, coefficients giving a zero quadratic form lie on one line.

<figure class="lesson-figure" markdown="1">

![Contours of (c1+2c2) squared surround a dashed null line, with the nonzero coefficient vector (2,-1) ending on that line](../../figures/assets/A09-KER/A09-KER-02-null-direction.svg)

<figcaption>On the dashed line, c₁+2c₂=0. The green arrow is a coefficient vector with nonzero length, but its quadratic form value is zero.</figcaption>
</figure>

## Common misconceptions

- The word kernel in a kernel function means something different from a linear map's null space.
- If finite-precision calculations give a very small negative eigenvalue, first check tolerance and matrix symmetrization.

## Exercises

### 1. Gram matrix
Apply the linear kernel to $x_1=(1,0)$ and $x_2=(1,1)$ to find $K$.
<details><summary>Show solution</summary>

Calculating inner products gives $K=\begin{bmatrix}1&1\\1&2\end{bmatrix}$.
</details>

### 2. PSD
Use eigenvalues to determine whether $K=\begin{bmatrix}1&-1\\-1&1\end{bmatrix}$ is PSD.
<details><summary>Show solution</summary>

Its eigenvalues are $0$ and $2$, both nonnegative, so it is PSD.
</details>

### 3. Symmetry
Can a function with $k(x,x')\ne k(x',x)$ be used directly as a real inner-product kernel?
<details><summary>Show solution</summary>

Not directly, because a real inner product is symmetric. Symmetrizing it alone does not automatically establish PSD either.
</details>

### 4. Model interpretation
Two prompts have a large activation kernel value. Can you immediately conclude that they use the same feature?
<details><summary>Show solution</summary>

This is evidence of high similarity according to the specified kernel. Feature identity or a causal mechanism requires additional alignment and intervention tests.
</details>

## Sources and update boundaries

This lesson concerns real-valued symmetric PSD kernels. Conditionally positive definite kernels and indefinite similarity methods are outside its scope.

- [Stanford CS229, Kernels](https://cs229.stanford.edu/summer2022/cs229-notes3.pdf): Symmetry and PSD conditions for every finite Gram matrix and the feature interpretation of polynomial and Gaussian kernels were checked against this source. Conditions for the existence of a PSD kernel are distinguished from Mercer expansions, which require additional continuity and integration conditions.

## Lesson summary

- A kernel compares sample pairs with a scalar.
- The PSD condition applies to the quadratic form of every finite Gram matrix.
- Kernel choice determines the analysis geometry.
- High kernel similarity alone does not establish functional identity.

## Pass criteria

- Can you construct a Gram matrix from a kernel and test PSD?
- Can you limit the scope of a claim based on kernel similarity?

## Next lesson

- [A09-KER-03 Feature maps and the kernel trick](A09-KER-03-feature-map-kernel-trick.md)

## Author checklist

- [x] The symmetric PSD condition is connected to finite Gram matrices.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
