---
id: "A09-KER-03"
title: "Feature maps and the kernel trick"
part: 4
stage: "A09-KER"
status: "complete"
prerequisites: ["M02-02", "M02-03", "A09-KER-02"]
estimated_time: "90–120 minutes"
---

# A09-KER-03. Feature maps and the kernel trick

## Why this lesson matters

A positive semidefinite kernel can be represented as an inner product in a feature space. An algorithm using kernel values without explicitly constructing feature coordinates can compute even in a high-dimensional or infinite-dimensional space. This computational saving is the kernel trick.

## Learning objectives

- Calculate the corresponding kernel from an explicit feature map.
- Explain how to replace inner-product calculations using only a Gram matrix.
- Explain why feature maps producing the same kernel are not unique.
- Specify units of computation and controls for kernel-similarity analysis.

## Prerequisite check

- Prerequisite lessons: [M02-02 Linear combinations and span](../../part-1-foundations/M02/M02-02-linear-combinations-span.md), [M02-03 Inner products, length, and angles](../../part-1-foundations/M02/M02-03-inner-product-length-angle.md), [A09-KER-02 Positive definite kernels](A09-KER-02-positive-definite-kernel.md)
- Check question: If you can calculate an inner product without knowing every coordinate of two feature vectors, which algorithms can you still run?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\phi:\mathcal X\to\mathcal H$ | `phi maps X to H` | Map taking inputs to a feature space | function |
| $k(x,x')=\langle\phi(x),\phi(x')\rangle_{\mathcal H}$ | `k of x and x prime equals the inner product of phi of x and phi of x prime in H` | Kernel represented by a feature inner product | scalar |
| $\Phi$ | `capital phi` | Sample feature matrix | $n\times d_\phi$ |
| $K=\Phi\Phi^\top$ | `K equals Phi Phi transpose` | Feature Gram matrix | $n\times n$ |

## Core concepts

### Map an input to a feature vector

A feature map $\phi$ takes input $x$ to a vector in inner-product space $\mathcal H$. The map itself need not be linear in the input. Defining the inner product of two feature vectors as

$$
k(x,x')=\langle\phi(x),\phi(x')\rangle_{\mathcal H}
$$

gives a PSD kernel: for arbitrary coefficients, its quadratic form is $\|\sum_i c_i\phi(x_i)\|_{\mathcal H}^2$. Conversely, a PSD kernel has a Hilbert feature space and a map realizing this inner-product relationship. This does not imply that the map is directly computable or finite-dimensional.

In the figure below, scalar inputs are mapped to two feature coordinates.

<figure class="lesson-figure" markdown="1">

![The nonlinear feature map (x,x squared) sends scalar inputs minus one, zero, and one onto three points of a parabola in a two-dimensional feature plane](../../figures/assets/A09-KER/A09-KER-03-feature-parabola.svg)

<figcaption>The horizontal and vertical axes are two feature components, not two axes of the input space. A single scalar input can determine a position on a nonlinear feature curve.</figcaption>
</figure>

For finite feature dimension $d_\phi$, take $\phi(x_i)$ as a column vector and stack its transpose as a row to form $\Phi\in\mathbb R^{n\times d_\phi}$. Entry $(i,j)$ of $\Phi\Phi^\top$ is the inner product of two rows, so $K=\Phi\Phi^\top$. Even in an infinite-dimensional feature space, kernel values form a finite $n\times n$ Gram matrix. In that case, however, do not assume that $\Phi$ has been constructed as an ordinary numerical array of finite width.

The next figure shows a product that sums over the feature index and leaves two sample indices.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A three-by-two feature matrix with rows (0,0),(1,1),(2,4) multiplies its transpose to form a three-by-three sample Gram matrix](../../figures/assets/A09-KER/A09-KER-03-gram-factorization.svg)

<figcaption>Multiplying and adding across the two feature columns of Φ produces one sample-pair entry of K. The feature width is 2, but the number of Gram entries is 3²=9.</figcaption>
</figure>

### Replace inner products with kernel values

If an algorithm's input dependence is expressed through feature inner products and linear combinations of sample features, it can compute with kernel values instead of an explicit $\Phi$. For example, a predictor with $w=\sum_i\alpha_i\phi(x_i)$ is evaluated as

$$
\langle w,\phi(x)\rangle_{\mathcal H}
=\sum_i\alpha_i k(x_i,x)
$$

Its prediction vector on the training sample is $K\alpha$, and $\|w\|_{\mathcal H}^2=\alpha^\top K\alpha$. An objective using only predictions and this norm can be written in terms of coefficients $\alpha$ and the Gram matrix. This is the computational meaning of the kernel trick. An algorithm requiring an absolute-value penalty on individual feature coordinates or activation of a specified coordinate cannot immediately be replaced using the same Gram matrix alone.

The training Gram matrix alone does not determine predictions on new inputs. For a new $x$, additionally calculate $k(x_i,x)$. Distinguish the kernel function defined on all inputs from the Gram matrix stored during training at this step as well.

Below, the same predictor is evaluated using a sum of feature vectors and using kernel values for a new input.

<figure class="lesson-figure" markdown="1">

![The feature vectors phi(1) and half phi(2) add to w=(2,3), and a new input one half gives the same prediction 1.75 by a dot product or weighted kernel values](../../figures/assets/A09-KER/A09-KER-03-predictor-feature-sum.svg)

<figcaption>Adding the blue and purple vectors head to tail gives green w. Taking its inner product with the new feature or summing two weighted kernel values for the new input gives 1.75. The short gray vector is the new input's feature.</figcaption>
</figure>

### Polynomial feature scaling and non-uniqueness

For example, for scalar inputs with $k(x,z)=(1+xz)^2$, one possible choice is

$$
\phi(x)=(1,\sqrt2x,x^2)
$$

Indeed, $\phi(x)^\top\phi(z)=1+2xz+x^2z^2$. The middle coordinate's $\sqrt2$ is a scale multiplied twice in the inner product to produce $2xz$. Simply using $(1,x,x^2)$ makes the middle term $xz$ and gives a different kernel. Even through a nonlinear input map, a feature-space predictor can be calculated linearly in $w$.

Applying an orthogonal transformation $Q$ to obtain $Q\phi(x)$ gives the same inner products because $Q^\top Q=I$. The row feature matrix becomes $\tilde\Phi=\Phi Q^\top$ and retains $\tilde\Phi\tilde\Phi^\top=K$. Distinguish the inner-product geometry determined by the kernel from each feature coordinate's name or meaning. Maps producing the same kernel can also be non-unique through embeddings into spaces of different dimensions. Coordinate identity is therefore not fixed by this one orthogonal-transformation example.

The next figure compares coordinates and inner products when two features are rotated together.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A ninety-degree rotation changes feature coordinates (1,1),(2,4) to (-1,1),(-4,2) while preserving their dot product 6](../../figures/assets/A09-KER/A09-KER-03-orthogonal-features.svg)

<figcaption>Component values change, but the two vectors' lengths, angle, and inner product 6 are preserved. Obtaining the same kernel does not identify the coordinate names with one another.</figcaption>
</figure>

### Computational cost and units of comparison

The kernel trick changes the computational representation. A dense Gram matrix stores a value for each sample pair, so its entry count is $n^2$. Even if it avoids the cost of a large explicit feature dimension, storage and matrix operations become bottlenecks when the sample count is large. It does not automatically reduce every algorithm's cost.

When comparing kernels from two layers, row $i$ must refer to the same prompt, token, or consistently defined summary. Even with equal sample counts, differences in row order or sampling conditions prevent direct comparison of entries at the same array positions. Centering subtracts the sample mean from each feature; fix which sample and mean are used. After aligning evaluation units, define controls appropriate to the comparison, such as shuffled row correspondences or random features with the same dimension and scale. These comparisons concern similarity of geometry among samples, not coordinatewise feature identity.

The two figures below distinguish a change in sample order from removal of the feature mean.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Reordering the same samples from A,B,C to C,A,B moves Gram entries but preserves the value 6 for the pair B,C](../../figures/assets/A09-KER/A09-KER-03-row-alignment.svg)

<figcaption>The relationship between samples B and C has value 6 in both matrices. Comparing array positions alone compares different sample pairs.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Subtracting the mean (2,14/3) from three feature vectors moves their mean to the origin without reordering the samples](../../figures/assets/A09-KER/A09-KER-03-centering.svg)

<figcaption>The gray × marks the sample mean. Subtracting the same mean from every point moves the mean to the origin while preserving the correspondence of x₁, x₂, and x₃.</figcaption>
</figure>

## Small example

For $x=1$ and $z=2$, the polynomial kernel value is $(1+2)^2=9$. Explicit features give the same value: $(1,\sqrt2,1)\cdot(1,2\sqrt2,4)=1+4+4=9$.

The kernel calculation forms scalar $1+xz$ and then squares it, whereas the explicit calculation sums the products of three coordinates. The intermediate representations differ, but the final inner product is the same. Applying this equality across samples makes every entry of the explicit feature Gram matrix match the kernel Gram matrix. What can be calculated without using the feature map is this inner product, not the individual meanings of the three coordinates.

The figure below shows each coordinate product's contribution.

<figure class="lesson-figure" markdown="1">

![The explicit polynomial features at inputs one and two contribute coordinate products 1,4,4, whose sum 9 equals the degree-two polynomial kernel](../../figures/assets/A09-KER/A09-KER-03-polynomial-products.svg)

<figcaption>The middle component's √2 is multiplied on both sides to give contribution 4. Adding the three bar values gives 9, the same as the directly calculated kernel value.</figcaption>
</figure>

## Common misconceptions

- The kernel trick does not make every calculation cheap. Sample count can dominate cost instead of feature dimension.
- Two feature maps with the same kernel need not have the same coordinatewise meanings.

## Exercises

### 1. Feature map
Write the kernel corresponding to $\phi(x)=(x,x^2)$.
<details><summary>Show solution</summary>

$k(x,z)=xz+x^2z^2$.
</details>

### 2. Gram factorization
If $\Phi$ is $5\times3$, what is the shape of $K=\Phi\Phi^\top$?
<details><summary>Show solution</summary>

$K$ compares sample pairs, so its shape is $5\times5$.
</details>

### 3. Non-uniqueness
For orthogonal $Q$, show why $\tilde\phi(x)=Q\phi(x)$ gives the same kernel.
<details><summary>Show solution</summary>

$\tilde\phi(x)^\top\tilde\phi(z)=\phi(x)^\top Q^\top Q\phi(z)=\phi(x)^\top\phi(z)$.
</details>

### 4. Model interpretation
When comparing centered Gram matrices from two layers, can you directly compare matrices of the same shape if their token counts differ?
<details><summary>Show solution</summary>

No. Align the same experimental units or define summaries across units. Fix token sampling so that sampling differences are not mixed with representation differences.
</details>

## Sources and update boundaries

The feature-space representation of PSD kernels follows standard kernel theory. Measure conditions and convergence proofs for Mercer expansions are treated in a limited way in later lessons.

## Lesson summary

- Inner products of feature maps define a kernel.
- The kernel trick computes with a Gram matrix without explicit coordinates.
- Feature maps are non-unique, including under orthogonal transformations.
- The cost of Gram methods grows with sample count.

## Pass criteria

- Can you convert between an explicit feature map and a kernel?
- Can you explain why the same kernel does not determine coordinate identity?

## Next lesson

- [A09-KER-04 Introduction to RKHS](A09-KER-04-rkhs-introduction.md)

## Author checklist

- [x] Feature maps, Gram matrices, and the kernel trick are connected.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
