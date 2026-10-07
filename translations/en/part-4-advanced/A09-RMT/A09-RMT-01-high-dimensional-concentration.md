---
id: "A09-RMT-01"
title: "Concentration in high-dimensional spaces"
part: 4
stage: "A09-RMT"
status: "complete"
prerequisites: ["M02-03", "M04-04", "M04-05"]
estimated_time: "90–120 minutes"
---

# A09-RMT-01. Concentration in high-dimensional spaces

## Why this lesson matters

Even when the coordinates of a high-dimensional random vector vary, aggregate quantities such as norms and pairwise inner products can concentrate within a narrow range. To interpret activation cosine similarity or a random baseline, first check what concentrates as dimension increases.

## Learning objectives

- Calculate the mean and variance of an isotropic Gaussian vector's squared norm.
- Explain the inner-product scale of independent random directions.
- Distinguish concentration from low-dimensional clustering.
- Specify a dimension-matched null model for activation geometry.

## Prerequisite check

- Prerequisite lessons: [M02-03 Inner products, length, and angles](../../part-1-foundations/M02/M02-03-inner-product-length-angle.md), [M04-04 Expectation, variance, and covariance](../../part-1-foundations/M04/M04-04-expectation-variance-covariance.md), [M04-05 Common distributions](../../part-1-foundations/M04/M04-05-common-distributions.md)
- Check question: Under what conditions do variances add for a sum of independent random variables?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $x\sim\mathcal N(0,I_d/d)$ | `x is Gaussian with mean zero and covariance I sub d over d` | Scaled isotropic vector with expected squared norm 1 | $d$-vector |
| $\lVert x\rVert_2^2$ | `the squared Euclidean norm of x` | Sum of squared coordinates | nonnegative scalar |
| $x^\top y$ | `x transpose y` | Inner product of two vectors | scalar |
| $d$ | `the ambient dimension d` | Ambient dimension containing the vector | positive integer |

## Core concepts

### From coordinate variance to squared-norm variance

$x_i\overset{\mathrm{iid}}\sim\mathcal N(0,1/d)$ means that each coordinate has mean zero and variance $1/d$, and the coordinates are independent. Because covariance is a scalar multiple of the identity, no direction receives greater variance. An isotropic vector is also commonly normalized to covariance $I_d$. Here, however, that vector is multiplied by $1/\sqrt d$ to give expected squared norm 1.

Using $E[Z^2]=1$ and $E[Z^4]=3$ for standard normal $Z$, $x_i=Z_i/\sqrt d$ gives

$$
E[x_i^2]=\frac1d,\qquad
\operatorname{Var}(x_i^2)
=E[x_i^4]-(E[x_i^2])^2
=\frac{3}{d^2}-\frac{1}{d^2}
=\frac{2}{d^2}
$$

The variance of $x_i$ and the variance of its square $x_i^2$ are different calculations. The squared coordinates are also independent, so no covariance terms remain in the variance of their sum:

$$
\lVert x\rVert_2^2=\sum_{i=1}^d x_i^2,
\qquad
E\lVert x\rVert_2^2=1,
\qquad
\operatorname{Var}(\lVert x\rVert_2^2)=\frac{2}{d}.
$$

The mean adds $d$ terms of $1/d$, and the variance adds $d$ terms of $2/d^2$. As dimension increases, the squared norm's standard deviation $\sqrt{2/d}$ decreases. Without this scaling, covariance $I_d$ gives mean $d$ and variance $2d$, so do not mix the two results without accounting for normalization.

Concentration means that the probability of falling outside a specified tolerance becomes small. For $S=\lVert x\rVert^2$, $|S-1|\geq\epsilon$ implies $(S-1)^2\geq\epsilon^2$, so $E[(S-1)^2]\geq\epsilon^2P(|S-1|\geq\epsilon)$. Thus, for $\epsilon>0$,

$$
P\bigl(|\lVert x\rVert^2-1|\geq\epsilon\bigr)
\leq\frac{2}{d\epsilon^2}
$$

At a fixed tolerance, this upper bound decreases as $d$ increases. It does not mean that every draw has norm exactly 1 or necessarily falls within one standard deviation.

The next two figures distinguish the width of the squared-norm distribution from an upper bound on a fixed-tolerance event. Do not read S on the first axis and the probability upper bound in the second figure as the same measurement.

<figure class="lesson-figure" markdown="1">

![Exact scaled chi square densities for dimensions fifty two hundred and eight hundred become narrower around squared norm one.](../../figures/assets/A09-RMT/A09-RMT-01-squared-norm-density.svg)

<figcaption>The exact Gaussian-example distributions of S=‖x‖² are plotted for d=50, 200, and 800. All have mean 1, with standard deviations 0.2, 0.1, and 0.05. This axis shows squared norm, not norm. A narrower curve does not make every draw equal to 1.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![The probability upper bound at squared norm tolerance zero point two decreases as dimension grows and is clipped to the trivial upper bound one.](../../figures/assets/A09-RMT/A09-RMT-01-fixed-tolerance-tail-bound.svg)

<figcaption>For an illustrative fixed ε=0.2, min(1, 2/(dε²)) is plotted. The upper bounds are 1 at d=50, 0.25 at d=200, and 0.0625 at d=800. The curve does not measure the actual departure probability or the maximum error across all draws.</figcaption>

</figure>

### The inner-product scale of independent vectors

For independent $x,y\sim\mathcal N(0,I_d/d)$, the mean of $x_i y_i$ is $E[x_i]E[y_i]=0$, and its mean square is $E[x_i^2]E[y_i^2]=1/d^2$. Products for different coordinates are also independent, so

$$
E[x^\top y]=0,\qquad
\operatorname{Var}(x^\top y)
=\sum_{i=1}^d\operatorname{Var}(x_i y_i)
=\frac1d
$$

Typical inner-product fluctuations have scale $1/\sqrt d$. Cosine divides by the product of the two norms, but because those norms concentrate near 1, it becomes small on the same scale. When Gaussian directions are normalized to unit vectors, the mean squared cosine of independent uniform directions is also exactly $1/d$. Nearly orthogonal means that cosine is near zero; it does not guarantee exact orthogonality at finite $d$. Nor should a scale for one independent pair be turned into a simultaneous guarantee for every pair in a large dataset.

For normalized unit directions, the distributions below compare cosine concentration across dimensions.

<figure class="lesson-figure" markdown="1">

![Exact cosine densities for independent uniform unit directions in dimensions four fifty and two hundred concentrate around zero without forcing every pair to be orthogonal.](../../figures/assets/A09-RMT/A09-RMT-01-unit-direction-cosine-density.svg)

<figcaption>The cosine distributions are plotted for two independent Gaussian vectors normalized to unit norm. At d=4, 50, and 200, the mean is zero and the mean squared cosine is 1/d. Taller curves indicate concentration near zero, not exact orthogonality of every pair at finite d.</figcaption>

</figure>

### Being near a sphere is not clustering

The result that $\lVert x\rVert$ is near 1 restricts only distance from the origin. Directions can still differ. For two independent vectors, squared distance is $\lVert x-y\rVert^2=\lVert x\rVert^2+\lVert y\rVert^2-2x^\top y$, so under this scaling it lies near 2, with distance near $\sqrt2$. Similar norms do not make the two points converge to the same location. Low-dimensional clustering describes additional structure, such as concentration near a particular subspace or a few centers.

The planar figures below separate radius from the distribution of directions and follow the distance calculation between two points of equal norm.

<figure class="lesson-figure" markdown="1">

![Two deterministic illustrative point sets share the unit circle while one spans directions and the other occupies a short arc.](../../figures/assets/A09-RMT/A09-RMT-01-same-radius-different-directions.svg)

<figcaption>These are illustrative two-dimensional points. The blue circles and green plus signs all have radius 1, but the blue points span several directions while the green points occupy a short arc. The same radial distribution alone does not determine directional clustering. This planar figure is not a simulation of high-dimensional Gaussian draws.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Two unit coordinate vectors form a right triangle whose point to point distance is square root two rather than zero.](../../figures/assets/A09-RMT/A09-RMT-01-unit-radii-pair-distance.svg)

<figcaption>This is an exact planar calculation for x=(1,0) and y=(0,1). Both norms are 1 and the inner product is zero, so ‖x−y‖²=1+1−0=2. It shows the relation used when norm≈1 and inner product≈0 in the high-dimensional example; the two points are not claimed to be random draws.</figcaption>

</figure>

### Conditions on observed geometry and the null

Concentration does not mean that every dataset is uniformly distributed on a sphere. Anisotropy, dependence, or low-dimensional signal changes norm and angle distributions. Interpret observations against a null distribution matched for dimension, marginal variance, and sample dependence.

When comparing cosines from layers of different widths, calculate the independent isotropic null scale for each $d$. That null alone is insufficient for activations with strongly anisotropic covariance. For a covariance-preserving null or a comparison after whitening, specify what is held fixed and what is removed. Tokens from the same prompt have a different sampling structure from independent Gaussian draws, so do not treat token count as the number of independent repetitions.

When matching the null, check both covariance geometry and sampling-group structure below. Equal total variance or equal row count alone does not make the nulls equivalent.

<figure class="lesson-figure" markdown="1">

![A unit covariance circle and a matched trace covariance ellipse have equal total variance but an illustrative coordinate variance ratio one hundred.](../../figures/assets/A09-RMT/A09-RMT-01-equal-trace-anisotropic-geometry.svg)

<figcaption>The illustrative two-dimensional covariance geometries I₂ and diag(200/101, 2/101) are compared. Both have trace 2, but the latter's coordinate variance ratio is 100, elongating it in a particular direction. The lines show principal-axis covariance scales, not an actual activation distribution or sample cloud.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Four token rows belong to two prompt packs whereas four independent null draws are shown as four ungrouped observations.](../../figures/assets/A09-RMT/A09-RMT-01-prompt-pack-versus-iid-rows.svg)

<figcaption>Four illustrative token rows are grouped into two prompt packs. Rows from one prompt are not guaranteed to be independent, so four rows are not counted as four i.i.d. prompts. Z₁ through Z₄ below follow the separate specification of independent null draws. Groups mark a shared prompt without assuming a particular covariance value.</figcaption>

</figure>

## Small example

For $d=200$, the squared norm's standard deviation is $\sqrt{2/200}=0.1$. Under the same scaling, the standard deviation of the inner product of independent vectors is $1/\sqrt{200}\approx0.071$.

The first value, 0.1, measures squared-norm fluctuations; the second, 0.071, measures inner-product fluctuations. Neither is the standard deviation of norm itself or an angle measured in degrees. Under the same normalization, increasing $d$ fourfold halves both standard deviations.

The figure below uses separate curves for the two standard deviations in the existing d=200 example and compares them as width changes.

<figure class="lesson-figure" markdown="1">

![Two different standard deviations scale with the inverse square root of dimension with marked values at dimension two hundred and eight hundred.](../../figures/assets/A09-RMT/A09-RMT-01-dimension-dependent-scales.svg)

<figcaption>The squared-norm standard deviation √(2/d) and the standard deviation 1/√d of the inner product of independent vectors measure fluctuations of different aggregates. The existing d=200 values 0.1 and approximately 0.071 are marked. Increasing d fourfold to 800 halves both, so use a null scale matched to each layer's width.</figcaption>

</figure>

## Common misconceptions

- Concentration of distances does not mean that every point has the same meaning.
- High dimension alone does not put an empirical sample in a population concentration regime. Check sample dependence and tail behavior.

## Exercises

### 1. Norm variance
For $d=50$, calculate the variance of $\lVert x\rVert^2$.
<details><summary>Show solution</summary>

It is $2/d=2/50=0.04$.
</details>

### 2. Inner-product scale
By what factor does the standard deviation of the inner product of independent vectors change when $d$ increases from 100 to 400?
<details><summary>Show solution</summary>

The scaling is $1/\sqrt d$, so it becomes $1/2$ as large.
</details>

### 3. Anisotropy
If one coordinate's variance is 100 times another's, can the angle prediction of an isotropic null be used unchanged?
<details><summary>Show solution</summary>

No. Covariance anisotropy makes a particular direction dominate, so a covariance-matched null or a comparison after whitening is needed.
</details>

### 4. Model interpretation
Which null should be reported alongside raw cosine histograms of activations from two layers with different widths?
<details><summary>Show solution</summary>

Report random-vector cosine distributions matched to each layer's dimension, norm or covariance, and sampling unit.
</details>

## Sources and update boundaries

The calculations are restricted to i.i.d. Gaussian examples. Constants in sub-Gaussian concentration inequalities and separate theory for heavy-tailed distributions are outside this lesson's scope.

- [Vershynin, High-Dimensional Probability](https://webapps.math.uci.edu/~rvershyn/papers/HDP-book/HDP-1.pdf): Norm concentration, isotropy, and independent-vector geometry in §§3.1–3.2 were checked against this source. This lesson calculates scales directly using Gaussian moments, sums of variances, and inequalities applied to terms on an error event.

## Lesson summary

- The variance of the isotropic Gaussian squared norm is $2/d$.
- The inner product of independent vectors has scale $1/\sqrt d$.
- Concentration is a random baseline, not evidence that semantic structure is absent.
- Null models must match dimension and covariance conditions.

## Pass criteria

- Can you calculate concentration scales for norms and inner products?
- Can you propose a null that separates observed geometry from dimension effects?

## Next lesson

- [A09-RMT-02 Random projection](A09-RMT-02-random-projection.md)

## Author checklist

- [x] Norm and inner-product concentration are connected to null models.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
