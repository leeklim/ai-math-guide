---
id: "A09-RMT-02"
title: "Random projection"
part: 4
stage: "A09-RMT"
status: "complete"
prerequisites: ["M02-04", "M02-09", "A09-RMT-01"]
estimated_time: "90–120 minutes"
---

# A09-RMT-02. Random projection

## Why this lesson matters

Even for high-dimensional representations, a lower-dimensional random embedding can preserve pairwise distances in a finite point set. Random projection serves as a visualization or compression control, separating the performance gained by a learned projection from the effect of dimension reduction itself.

## Learning objectives

- Write the scaling of a Gaussian random projection.
- Explain the target of the Johnson–Lindenstrauss guarantee.
- Explain how target dimension depends on point count and distortion.
- Design a random projection as a control for a learned projection.

## Prerequisite check

- Prerequisite lessons: [M02-04 Matrices and matrix multiplication](../../part-1-foundations/M02/M02-04-matrices-matrix-multiplication.md), [M02-09 Orthogonal bases and orthogonal projection](../../part-1-foundations/M02/M02-09-orthogonal-basis-projection.md), [A09-RMT-01 Concentration in high-dimensional spaces](A09-RMT-01-high-dimensional-concentration.md)
- Check question: What is the output shape when matrix $R\in\mathbb R^{m\times d}$ acts on a $d$-vector?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $R\in\mathbb R^{m\times d}$ | `R is an m by d matrix` | Random projection matrix | $m\times d$ |
| $z=Rx$ | `z equals R x` | Projected representation | $m$-vector |
| $\varepsilon$ | `epsilon` | Permitted relative squared-distance distortion | number in $(0,1)$ |
| $\delta$ | `delta` | Permitted overall failure probability | number in $(0,1)$ |
| $m=O(\varepsilon^{-2}\log n)$ | `m is on the order of epsilon to the minus two log n` | JL target-dimension scaling | positive integer order |

## Core concepts

### Scaling a Gaussian matrix

Draw $R_{ij}\sim\mathcal N(0,1/m)$ independently and set $z=Rx$. One row of $R$ combines input coordinates with different random coefficients to produce one output coordinate. For a fixed vector $v$, $(Rv)_i=\sum_j R_{ij}v_j$ has mean zero. Adding variances of independent coefficients gives

$$
\operatorname{Var}((Rv)_i)=\sum_{j=1}^d\frac{v_j^2}{m}
=\frac{\lVert v\rVert^2}{m}
$$

Because the mean is zero, this is also $E[(Rv)_i^2]$. Summing the squares of the $m$ output coordinates gives $E\lVert Rv\rVert^2=\lVert v\rVert^2$. This summation is why the variance is $1/m$, not $1/d$.

For $v\ne0$, Gaussian-sum properties make $\sqrt m(Rv)_i/\lVert v\rVert$ independent standard Gaussian variables. Thus, $\lVert Rv\rVert^2/\lVert v\rVert^2$ has the same distribution as the previous lesson's $m$-dimensional squared norm, with mean 1 and variance $2/m$. Preservation in expectation does not mean equal norms for every $R$. Concentration means that small relative error has high probability at large $m$.

Here, projection names a linear map into a lower-dimensional space. The rows of a Gaussian $R$ are usually not orthogonal. Unlike an orthogonal projection onto a subspace of the same space in M02-09, it need not satisfy $P^2=P$. For $m<d$, applying this expression to an $m\times d$ matrix $R$ is not even shape-compatible.

Below, read the sum of rowwise expected squares for one input separately from the norm-ratio distribution across draws of R with that input fixed.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A fixed three component input two zero zero is mapped by two Gaussian rows to random coordinates whose expected squared contributions each equal two.](../../figures/assets/A09-RMT/A09-RMT-02-output-row-scaling.svg)

<figcaption>The illustrative setting uses m=2, d=3, and v=(2,0,0)ᵀ. The expected squares of z₁=2r₁₁ and z₂=2r₂₁ are each 2, summing to the original ‖v‖²=4. This is preservation in expectation, not norm preservation for every drawn R. Neither RR nor P²=P is required of a 2×3 R.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Exact Gaussian projection squared norm ratios have mean one and progressively narrower densities for target dimensions ten fifty and two hundred.](../../figures/assets/A09-RMT/A09-RMT-02-fixed-vector-norm-ratio.svg)

<figcaption>For fixed v≠0, the distribution of T=‖Rv‖²/‖v‖² is compared at m=10, 50, and 200. All have mean 1 and variance 2/m. Here m is output dimension, not the original ambient d.</figcaption>

</figure>

### From one vector's length to distances between all point pairs

The Johnson–Lindenstrauss lemma states that, for a finite set of $n$ points, there exists a map into dimension $m=O(\varepsilon^{-2}\log n)$ preserving all pairwise squared distances approximately within

$$
(1-\varepsilon)\lVert x_i-x_j\rVert^2
\le
\lVert Rx_i-Rx_j\rVert^2
\le
(1+\varepsilon)\lVert x_i-x_j\rVert^2
$$

Linearity gives $Rx_i-Rx_j=R(x_i-x_j)$, so preserving distances amounts to preserving each difference vector's norm. The inequalities concern squared distance; ratios of distance itself lie between $\sqrt{1-\varepsilon}$ and $\sqrt{1+\varepsilon}$.

A guarantee for one pair does not guarantee every pair. There are at most $n(n-1)/2$ point pairs, and overall failure means that at least one pair fails. Summing their failure probabilities gives an upper bound on overall failure probability; the pair events need not be independent. At the same time, the same $R$ must be applied to every point to form one embedding.

The next figures distinguish squared-distance ratios from distance ratios and connect the pairs that must be preserved simultaneously within one point set.

<figure class="lesson-figure" markdown="1">

![Intervals for squared distance ratios zero point eight to one point two and distance ratios square root zero point eight to square root one point two are compared on one ratio axis.](../../figures/assets/A09-RMT/A09-RMT-02-squared-versus-distance-distortion.svg)

<figcaption>This illustrative comparison uses ε=0.2. Squared-distance ratios lie in [0.8,1.2], whereas distance ratios lie in [√0.8,√1.2]≈[0.894,1.095]. The two lines show differently squared ratios, not two repetitions of the same kind of distance.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Four fixed planar points have all six unordered pairs drawn with a common requirement that the same projection applies to every point.](../../figures/assets/A09-RMT/A09-RMT-02-all-pairs-one-embedding.svg)

<figcaption>The four illustrative points have six pairs. Lines mark the pairwise distances to compare, with the same R applied to every point. Any single failure is an overall failure, so summing failure probabilities gives an upper bound. Independence of the six events is not assumed.</figcaption>

</figure>

### Dimension and failure probability

For a fixed difference vector under Gaussian projection, the probability that relative squared-norm error exceeds $\varepsilon$ is bounded above by $2\exp(-c m\varepsilon^2)$. Here $0<\varepsilon<1$ and $c>0$ is a fixed constant. This exponential bound is not proved in this lesson, but its faster decay than the previous lesson's variance-based bound is the key to JL scaling. Summing over all pairs bounds failure probability by $n^2\exp(-c m\varepsilon^2)$. To make this at most $\delta$, a sufficient dimension has the form

$$
m\ge \frac{2\log n+\log(1/\delta)}{c\varepsilon^2}
$$

At fixed failure probability, the order $\varepsilon^{-2}\log n$ remains. This is the scaling of a sufficient dimension, not a formula for the exact minimum dimension or the dimension required by every dataset. Exact constants depend on the projection distribution and permitted failure probability.

Below, only the failure-budget term in the sufficient-dimension expression is isolated and compared as δ changes.

<figure class="lesson-figure" markdown="1">

![The failure probability contribution log one over delta grows as allowed failure probability decreases on a logarithmic axis.](../../figures/assets/A09-RMT/A09-RMT-02-failure-probability-log-term.svg)

<figcaption>The log(1/δ) term is normalized to 1 at illustrative δ=0.05. A smaller δ increases this term, which is added to 2log n in the sufficient condition for m. The plotted value shows the change in the failure-budget term, not the entire dimension.</figcaption>

</figure>

### A finite-set guarantee and a random control

Random projection concerns distance preservation on a specified finite set. It does not automatically guarantee anything about an unseen population, label separation, or the topology of a nonlinear manifold.

The probability concerns randomness in drawing $R$ for a fixed point set. Choosing a new point with maximal distortion after seeing $R$ changes the specification. In particular, if $m<d$, $R$ has a nonzero null vector, so distance in that direction collapses to zero. Distances of all possible inputs cannot be preserved simultaneously. The distinction is that preservation can hold on a finite set specified in advance that avoids such directions.

When comparing a learned projection with random projections, match input activations, output dimension, and preprocessing. Refit the probe for each random $R$ and evaluate using the same selection and test procedure. Applying a probe fitted in learned-representation coordinates unchanged to random coordinates mixes projection quality with readout mismatch. Multiple random seeds avoid using one luckily good matrix as the reference; those seeds alone do not identify the learned projection's mechanism.

The next two figures separately show a null direction outside the finite set and a control path that refits the readout for each projection.

<figure class="lesson-figure" markdown="1">

![A deterministic coordinate map preserves distances among three points with zero third coordinate while collapsing a new unit third coordinate point onto the origin.](../../figures/assets/A09-RMT/A09-RMT-02-finite-set-and-null-direction.svg)

<figcaption>The illustrative map is R(x₁,x₂,x₃)=(x₁,x₂). Distances among the prespecified A, B, and C are unchanged, but another point D=(0,0,1) maps to the same output as A. This is an exact linear calculation showing the distinction between a null direction at m&lt;d and the finite-set specification, not a Gaussian draw or an example of JL's probabilistic guarantee.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Learned and random sixty four dimensional projections start from the same activations and receive separately fitted probes under the same development and locked test protocol.](../../figures/assets/A09-RMT/A09-RMT-02-projection-probe-control-contract.svg)

<figcaption>Both paths use the same activations and output dimension 64. For each random Rₖ, a probe is refitted in its coordinates and evaluated under the same selection and test rules. This is neither a comparison that transfers the learned-space probe unchanged nor a claim that multiple seeds alone identify the learned mechanism.</figcaption>

</figure>

## Small example

Increasing point count by a factor of 100 changes the dimension bound's $\log n$ term to $\log(100n)$. In contrast, halving permitted distortion increases the required dimension order fourfold through $\varepsilon^{-2}$ scaling.

The logarithmic increase in the first sentence means $\log(100n)=\log n+\log100$. With the same constant and failure probability, changing $n=100$ to $10{,}000$ doubles the log term. Do not read a hundredfold increase in point count as a hundredfold increase in dimension. The second comparison holds other conditions fixed and changes only $\varepsilon$.

The two curves below separate the change in the log term of n from the change in the inverse-square term of ε to check the existing example's factors.

<figure class="lesson-figure" markdown="1">

![The logarithmic point count term normalized at one hundred doubles when point count reaches ten thousand.](../../figures/assets/A09-RMT/A09-RMT-02-point-count-log-term.svg)

<figcaption>The existing n=100→10,000 example is plotted relative to a common reference as log n/log100. Point count increases a hundredfold, but the log term doubles. The vertical axis is the log n term in the expression, not the entire sufficient m or minimum dimension.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![The inverse squared distortion term is normalized at epsilon zero point two and reaches four at epsilon zero point one.](../../figures/assets/A09-RMT/A09-RMT-02-distortion-inverse-square.svg)

<figcaption>With other conditions fixed, the ε⁻² term is normalized to 1 at ε=0.2. It is 4 at ε=0.1, relating halved distortion to a fourfold dimension order. The curve calculates neither hidden constants nor the exact minimum m.</figcaption>

</figure>

## Common misconceptions

- Random projection and PCA have different objectives. PCA uses data variance, whereas random projection uses a data-independent matrix.
- There is usually no guarantee that a two-dimensional visualization preserves pairwise distances well.

## Exercises

### 1. Scaling
Explain in one sentence why the variance of $R_{ij}$ is $1/m$.
<details><summary>Show solution</summary>

The scaling preserves the original squared norm when the expected squared contributions of the $m$ projected coordinates are added.
</details>

### 2. Distortion
By what factor does the JL dimension order change when $\varepsilon$ decreases from $0.2$ to $0.1$?
<details><summary>Show solution</summary>

It is proportional to $\varepsilon^{-2}$, so it increases fourfold.
</details>

### 3. Finite set
Does preservation of training-activation distances guarantee the same distortion on unseen prompts?
<details><summary>Show solution</summary>

No. Unseen points were not included in the finite set of the JL statement.
</details>

### 4. Model interpretation
Which random control should be used when evaluating probe accuracy for a learned 64-dimensional projection?
<details><summary>Show solution</summary>

Apply multiple random projection seeds to the same input activations and output dimension, repeating the same probe selection and test protocol.
</details>

## Sources and update boundaries

This lesson concerns Gaussian random projection and the role of JL scaling. Computational complexity of sparse transforms and optimal constants are outside its scope.

The simultaneous finite-set guarantee and summation of pairwise failure probabilities follow the theorem and proof structure in [Dasgupta–Gupta, An elementary proof of a theorem of Johnson and Lindenstrauss](https://cseweb.ucsd.edu/~dasgupta/papers/jl.pdf). Gaussian-row variance and the dimension expression are developed using this lesson's normalization.

## Lesson summary

- Gaussian projection is scaled to preserve expected squared norm.
- The JL lemma preserves pairwise distances in a finite point set at lower dimension.
- Required dimension grows with $\log n$ and $\varepsilon^{-2}$.
- Random projection is a data-independent control for learned compression.

## Pass criteria

- Can you write projection shape and scaling?
- Can you distinguish population questions that the JL guarantee does not answer?

## Next lesson

- [A09-RMT-03 The sample covariance spectrum](A09-RMT-03-sample-covariance-spectrum.md)

## Author checklist

- [x] The target of the JL guarantee, dimension scaling, and control role are distinguished.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
