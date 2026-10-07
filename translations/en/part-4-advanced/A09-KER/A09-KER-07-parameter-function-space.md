---
id: "A09-KER-07"
title: "Comparing parameter space and function space"
part: 4
stage: "A09-KER"
status: "complete"
prerequisites: ["M03-15", "N05-03", "A09-KER-06"]
estimated_time: "90–120 minutes"
---

# A09-KER-07. Comparing parameter space and function space

## Why this lesson matters

Neural network parameterizations have permutation and scaling symmetries. Parameter points representing the same function may have a large Euclidean distance. Conversely, a small parameter perturbation along a Jacobian direction with a large singular value can substantially change outputs. The kernel perspective connects local parameter displacement to function change.

## Learning objectives

- Distinguish what parameter distance and function distance measure.
- Approximate local function changes using Jacobian linearization.
- Explain how reparameterization can change the parameter metric and NTK.
- Specify the input distribution and output metric needed for model comparison.

## Prerequisite check

- Prerequisite lessons: [M03-15 Introduction to reparameterization and model symmetries](../../part-1-foundations/M03/M03-15-reparameterization-model-symmetries.md), [N05-03 MLP forward pass](../../part-2-neural-computation/N05/N05-03-mlp-forward-pass.md), [A09-KER-06 Neural tangent kernel](A09-KER-06-neural-tangent-kernel.md)
- Check question: Why is an MLP's output preserved when two hidden units are reordered consistently?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $\Delta\theta$ | `delta theta` | parameter displacement | $p$-vector |
| $J_\theta(x)\Delta\theta$ | `J sub theta of x times delta theta` | First-order approximation to local output change | output-shaped vector |
| $d_\Theta(\theta,\theta')$ | `d sub theta of theta and theta prime` | parameter-space distance | nonnegative scalar |
| $d_P(f,g)$ | `d sub P of f and g` | Function distance under distribution $P$ | nonnegative scalar |
| $B=Dg(\eta)$ | `B equals the derivative of g at eta` | Jacobian of the parameter coordinate change | $p\times p$ for a local reparameterization of the same dimension |

## Core concepts

### What objects are being compared?

One example of parameter distance is $d_\Theta(\theta,\theta')=\lVert\theta-\theta'\rVert_2$. It directly compares weight coordinates after fixing the parameter arrays, their order, and their units. Network symmetries can change coordinates while representing the same function, so this distance is not itself a behavioral difference.

Specify an input distribution $P$ and output metric to define a function distance, for example,

$$
d_P(f_\theta,f_{\theta'})^2
=E_{X\sim P}\left[\lVert f_\theta(X)-f_{\theta'}(X)\rVert_2^2\right]
$$

We consider cases where the mean squared difference on the right is finite. First calculate the squared norm of the output difference for the same input, then average under $P$. Rather than comparing raw parameters, this compares how much outputs differ on specified inputs.

A distance of 0 is also relative to $P$. If $P$ assigns probability only to a finite prompt set, it means agreement on that set; the functions may differ on other prompts. More generally, differences at inputs of $P$-probability 0 are not reflected. On functions that can differ over the full input domain, this is therefore a pseudometric rather than a metric. Grouping functions equal under $P$ into one element allows it to be treated as a metric.

Changing P changes the locations and weights used to average differences between the same two functions.

<figure class="lesson-figure" markdown="1">

![Two input probability distributions weighting the same output differences zero and two](../../figures/assets/A09-KER/A09-KER-07-distribution-weighting.svg)
<figcaption>Fix the output differences at the two inputs to 0 and 2. Under P, which observes both, the squared distance is 2; under Q, which observes only the first input, it is 0.</figcaption>
</figure>

### The Jacobian connects the two spaces locally

For a small displacement,

$$
f_{\theta+\Delta\theta}(x)-f_\theta(x)
\approx J_\theta(x)\Delta\theta
$$

For an output of dimension $q$, the Jacobian $J_\theta(x)$ has shape $q\times p$ and maps parameter directions to output directions. For a scalar output, it is the transpose of the column gradient in the preceding lesson. This is a first-order approximation at the current point; even if $J_\theta(x)\Delta\theta=0$, higher-order changes need not be 0.

If the remainder is sufficiently small on the inputs used and squared averaging is possible, inserting this approximation into the distance formula gives

$$
d_P(f_\theta,f_{\theta+\Delta\theta})^2
\approx\Delta\theta^\top
E_{X\sim P}[J_\theta(X)^\top J_\theta(X)]\Delta\theta
$$

The same parameter displacement can produce different function changes depending on how strongly the Jacobian amplifies or cancels it. Applying this formula at the population level also requires checking finiteness of the expectation and the approximation error.

For $n$ scalar-output samples, stack the rows in $J\in\mathbb R^{n\times p}$. The uniform empirical squared distance is approximated by $\lVert J\Delta\theta\rVert^2/n=\Delta\theta^\top J^\top J\Delta\theta/n$. The matrix $J^\top J$ describes sensitivity along parameter directions, whereas $JJ^\top$ describes NTK coupling between samples. Substituting the SVD $J=U\Sigma V^\top$ gives $V\Sigma^\top\Sigma V^\top$ and $U\Sigma\Sigma^\top U^\top$, respectively. Their nonzero eigenvalues are squares of the same singular values, but their directions lie in different spaces with different indices.

The next two figures separately show directional amplification and the index differences between the two Gram matrices.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Equal-length parameter directions mapped by a diagonal Jacobian to output directions of lengths three and one](../../figures/assets/A09-KER/A09-KER-07-jacobian-direction-gain.svg)
<figcaption>Mapping equal-length parameter displacements through J=diag(3,1) gives output lengths 3 or 1, depending on direction. The axes of the circle and ellipse show these local gains.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A two-by-three Jacobian and its parameter and sample Gram matrices sharing positive eigenvalues nine and one](../../figures/assets/A09-KER/A09-KER-07-two-gram-spaces.svg)
<figcaption>JᵀJ compares three parameter directions, and JJᵀ compares two sample directions. Their positive eigenvalues 9 and 1 agree, but there is no third sample coordinate corresponding to the third parameter's null direction.</figcaption>
</figure>

### Distinguish coordinate changes from metric choices

Consider a smooth local reparameterization of the same dimension, $\theta=g(\eta)$, with $B=Dg(\eta)$. Small displacements obey $\Delta\theta\approx B\Delta\eta$, and the chain rule gives $J_\eta=J_\theta B$. The same function change is expressed in the two coordinate systems as $J_\theta\Delta\theta\approx J_\eta\Delta\eta$.

Expressing the original parameters' squared Euclidean length in the new coordinates gives $\lVert\Delta\theta\rVert^2\approx\Delta\eta^\top B^\top B\Delta\eta$. Preserving the same length while changing only coordinates requires this transformation as well. By contrast, choosing the simple squared length $\lVert\Delta\eta\rVert^2$ in the new coordinates generally chooses a different metric.

The next figure plots both length rules in the same physical θ coordinates for comparison.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A physical parameter unit circle compared with an ellipse induced by choosing Euclidean length in rescaled coordinates](../../figures/assets/A09-KER/A09-KER-07-reparameterized-metric.svg)
<figcaption>Under θ=diag(2,1)η, the Euclidean unit circle in η becomes an ellipse in θ space. The rule preserving the original θ length uses ΔηᵀBᵀBΔη, so the two choices differ.</figcaption>
</figure>

Defining NTK using ordinary Euclidean gradients in each coordinate system gives

$$
K_\eta=J_\eta J_\eta^\top
=J_\theta BB^\top J_\theta^\top
$$

This generally differs from $K_\theta=J_\theta J_\theta^\top$. If $B$ is orthogonal, the kernels agree. Even with the same function values, defining Euclidean gradient descent anew in each coordinate system can change local output dynamics. Do not confuse coordinate independence of function values with coordinate dependence of the optimizer.

The next linear toy model has the same initial function but different output decay rates depending on the coordinates used to define ordinary gradients.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Identical initial linear functions in two coordinates with gradient-flow outputs decaying at rates one and four](../../figures/assets/A09-KER/A09-KER-07-reparameterized-flow.svg)
<figcaption>Representing the same function through θ=2η gives Euclidean parameter gradients 1 and 2 and NTKs 1 and 4. Under summed squared loss on one sample, the respective decays exp(−t) and exp(−4t) are exact linear calculations.</figcaption>
</figure>

### Match input and output comparison conventions

For language model comparisons, $P$ includes not only prompts but also token positions and their weights. Output coordinates must also match between models. For example, subtracting logit vectors directly when vocabulary orders differ does not compare the same tokens.

Squared raw-logit norm, centered-logit norm, and probability differences are different comparisons. Adding the same constant to every logit preserves softmax probabilities but changes raw-logit distance. If using KL divergence, specify its direction as well. KL is generally asymmetric, so do not call it the same kind of metric as the Euclidean norm distance above. Choose the comparison quantity to match the output property to be preserved.

The next comparison treats the same logit difference differently under different metrics.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Logits shifted by a common constant five alongside unchanged softmax probabilities for aligned token coordinates](../../figures/assets/A09-KER/A09-KER-07-logit-shift-metrics.svg)
<figcaption>Adding 5 to three logits gives raw distance √75, but differences in centered logits and probabilities are 0. Token coordinates are aligned identically for both comparisons.</figcaption>
</figure>

## Small example

In the two-layer scalar linear network $f_{a,b}(x)=abx$, both $(a,b)=(1,1)$ and $(10,0.1)$ agree for every $x$, producing the same function $f(x)=x$. Parameter distance is large, but function distance is 0.

The parameter distance is $\sqrt{9^2+(-0.9)^2}=\sqrt{81.81}$. Meanwhile, $J_{a,b}(x)=(bx,ax)$ gives scalar NTK $(a^2+b^2)xx'$, which is $2xx'$ and $100.01xx'$ at the two points, respectively. Agreement of the current output function does not imply the same Euclidean training geometry.

The next figure places the two parameter points beside their output functions.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Separated parameter points on the level set ab equals one with identical output lines f of x equals x](../../figures/assets/A09-KER/A09-KER-07-symmetry-distance.svg)
<figcaption>The points (1,1) and (10,0.1) are separated by √81.81 in parameter space, but both give f(x)=x. The same function does not imply the same Euclidean NTK at the two points.</figcaption>
</figure>

Moving straight from $(1,1)$ with displacement $(t,-t)$ gives first-order change $x(t-t)=0$. The actual output is $(1+t)(1-t)x=(1-t^2)x$, leaving change $-t^2x$. Moving along the symmetry curve $(c,1/c)$ preserves the product exactly at 1, but moving in a straight line along that curve's tangent is not the same operation.

Distinguish the curved symmetry path from the straight path along its tangent in the figure.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A hyperbolic symmetry path and its tangent line compared with zero and quadratic output changes](../../figures/assets/A09-KER/A09-KER-07-tangent-versus-symmetry.svg)
<figcaption>The paths share the same tangent at (1,1). The curve preserves ab=1, while the straight line leaves an output change of −t².</figcaption>
</figure>

## Common misconceptions

- Small weight distance alone does not establish similar behavior.
- Function distance 0 on a finite prompt set does not establish the same function over the full input space.

## Exercises

### 1. Symmetry
For $f_{a,b}(x)=abx$, give another parameter pair producing the same function as $(a,b)=(2,3)$.
<details><summary>Show solution</summary>

Any product of 6 suffices. For example, $(a,b)=(1,6)$ produces the same function.
</details>

### 2. Linearization
For $J=(2,1)$ and $\Delta\theta=(0.1,-0.2)^\top$, find the first-order output change.
<details><summary>Show solution</summary>

It is $J\Delta\theta=2(0.1)+1(-0.2)=0$.
</details>

### 3. Two Gram matrices
If $J$ has shape $n\times p$, give the shapes and indexed objects of $JJ^\top$ and $J^\top J$.
<details><summary>Show solution</summary>

The matrix $JJ^\top$ is an $n\times n$ sample Gram matrix, and $J^\top J$ is a $p\times p$ parameter sensitivity matrix.
</details>

### 4. Model interpretation
When comparing logits from two language models, what must be specified about $P$ and the output metric?
<details><summary>Show solution</summary>

Define $P$ through prompt and token-position sampling, and specify whether the output comparison uses raw logits, centered logits, probabilities, or KL divergence.
</details>

## Evidence and update boundaries

Jacobian linearization is a local approximation. Large displacements or changing activation patterns can increase the remainder. Natural gradient and quotient geometry are mentioned by name only, without development.

## Lesson summary

- Parameter distance and function distance measure different spaces.
- The Jacobian maps local parameter displacements to output changes.
- The matrices $JJ^\top$ and $J^\top J$ share the same nonzero singular spectrum but have different indices.
- Changing parameterization can change the Euclidean metric and NTK.

## Pass criteria

- Can you define distances in the two spaces separately?
- Can you explain why symmetries and input sampling limit comparison conclusions?

## Next lesson

- [A09-KER-08 Capstone: learning from the kernel perspective](A09-KER-08-capstone-kernel-learning.md)

## Author checklist

- [x] Parameter and function distances and Jacobian geometry are distinguished.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
