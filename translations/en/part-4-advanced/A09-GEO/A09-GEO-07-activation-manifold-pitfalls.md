---
id: "A09-GEO-07"
title: "Pitfalls in activation manifold analysis"
part: 4
stage: "A09-GEO"
status: "complete"
prerequisites: ["A09-GEO-01", "A09-GEO-06", "I06-08"]
estimated_time: "90–120 minutes"
---

# A09-GEO-07. Pitfalls in activation manifold analysis

## Why this lesson matters

Assuming that finite activation samples lie near a low-dimensional manifold can be useful, but the assumption is not automatically true. Estimates of dimension and curvature can change substantially with the neighborhood, metric, noise, and estimator. An analysis contract and null controls are therefore needed.

## Learning objectives

- Explain the difference between the manifold hypothesis and observed data.
- Explain how neighborhood scale affects geometric estimates.
- Diagnose projection artifacts and ambient noise.
- Design controls needed for claims about activation geometry.

## Prerequisite check

- Prerequisite lessons: [A09-GEO-01 Manifolds and local coordinates](A09-GEO-01-manifold-local-coordinate.md), [A09-GEO-06 Intrinsic and extrinsic curvature](A09-GEO-06-intrinsic-extrinsic-curvature.md), [I06-08 CCA, CKA, and RSA](../../part-3-interpretability/I06/I06-08-cca-cka-rsa.md)
- Check question: Does a finite point cloud itself guarantee a smooth manifold?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $\mathcal{N}_k(x)$ | `the k nearest neighborhood of x` | Local samples around $x$ | Finite set |
| $\hat d(x)$ | `d hat of x` | Estimated local dimension | Nonnegative scalar |
| $\varepsilon$ | `epsilon` | Neighborhood radius or noise scale | Positive scalar |
| $P_r$ | `P sub r` | Rank-$r$ projection | Linear map |

## Core concepts

Local PCA on activation samples $x_1,\ldots,x_n\in\mathbb R^D$ uses the leading eigenspace of the covariance around $x$ as an approximation to the tangent space. But a neighborhood that is too small is sensitive to insufficient samples and noise, while one that is too large mixes curvature and different branches into a single plane.

The same three points below belong to two candidate spaces with different dimensions.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The same three finite observations lie on a one-dimensional circle and in a two-dimensional plane so they do not uniquely identify a manifold](../../figures/assets/A09-GEO/A09-GEO-07-finite-samples-not-manifold.svg)

<figcaption>The three observations belong both to the circle S¹ and to the plane R². The dashed circle and plane are different candidate spaces, but the blue samples are identical. The arrangement of finitely many points alone cannot uniquely determine the smooth manifold that generated them or its dimension.</figcaption>
</figure>

### What local PCA actually computes

Center the samples in $\mathcal N_k(x)$ using the neighborhood mean, then compute their covariance. A unit eigenvector is an axis along which variation is measured, and its eigenvalue is the variance on that axis. The leading eigenspace collects the directions of selected large eigenvalues into a subspace. In a small region of a smooth space, variation first appears along tangent directions, so this subspace can approximate the tangent space. This requires low noise and neighborhood samples that sufficiently cover those directions. Computing the samples' dominant directions of variation does not itself prove that a smooth manifold exists.

The rank of a centered data matrix with $k$ samples is at most $\min(D,k-1)$. Centering creates a linear relation: the rows sum to 0. Thus, a covariance matrix with at most 4 nonzero eigenvalues in a neighborhood with $k=5$ does not rule out a high intrinsic dimension. This can be a sample-count limitation. Dimension estimates also depend on eigenvalue cutoffs or cumulative-variance criteria, so distinguish covariance rank from $\hat d(x)$.

Inspect the dominant variance direction after centering the synthetic arc samples below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Centering a small arc neighborhood moves its mean to the origin and reveals dominant vertical variance with a much smaller horizontal eigenvalue](../../figures/assets/A09-GEO/A09-GEO-07-pca-centering.svg)

<figcaption>Subtracting the orange sample mean places the same arc samples near the origin, as shown on the right. Vertical variance is larger than horizontal variance here. The green and purple arrows show unit eigenvector directions at 1/4 scale; their displayed lengths are not eigenvalues.</figcaption>
</figure>

Read the linear relation between rows created by centering directly in the matrix below.

<figure class="lesson-figure" markdown="1">

![Three centered rows in five ambient coordinates sum to zero and impose a rank ceiling of two without ruling out unobserved tangent directions](../../figures/assets/A09-GEO/A09-GEO-07-sample-rank-ceiling.svg)

<figcaption>This example takes the unit vectors along the first three coordinate axes of R⁵ as samples and subtracts their mean. The three rows sum to 0, so the rank is at most 2. A bound imposed by sample count is not evidence that unobserved tangent directions do not exist.</figcaption>
</figure>

### Shrinking or expanding a neighborhood

Even with a fixed sample count $k$, neighbors in a low-density region can spread over a larger area. Conversely, a fixed radius gives different sample counts in different regions. Record both $k$ and the actual range of neighbor distances.

Near $(1,0)$ on a circle, a small angle $t$ gives $\sin t\approx t$ and $\cos t\approx1-t^2/2$. The tangential coordinate varies in proportion to the angle, while the normal coordinate varies on the scale of its square. Tangent variation dominates in a sufficiently small region. Expanding the region mixes this normal variation and the tangent directions that rotate from point to point into the covariance. Shrinking it too much, however, reduces the signal variation itself, which can then be obscured by noise and sampling error.

Compare what the same k and the same radius hold fixed below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Dense and sparse regions require different radii to collect four neighbors while a fixed radius contains four neighbors in one region and none in the other](../../figures/assets/A09-GEO/A09-GEO-07-k-versus-radius.svg)

<figcaption>Excluding the orange anchor, selecting k=4 gives a radius of 0.15 in the dense region and 0.60 in the sparse region. Fixing the radius at 0.20 instead gives neighbor counts of 4 and 0. The same k does not mean the same spatial extent.</figcaption>
</figure>

The three scales of synthetic arc samples below compare how noise and curvature enter the covariance.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Noisy circle samples at very small intermediate and large angular scales show noise-dominated spread tangent-dominated spread and mixed curved directions](../../figures/assets/A09-GEO/A09-GEO-07-scale-signal-noise.svg)

<figcaption>Each panel uses 31 synthetic samples on a circle with coordinate-wise noise σ=0.015. Noise is relatively large on the very small arc, tangent variance dominates on the intermediate arc, and rotating directions mix with bending on the large arc. The half-lengths of the variance axes are 2√λ, and coordinate-axis ranges differ across panels. These numbers are not actual model measurements.</figcaption>
</figure>

Major sources of failure include the following.

- A restricted prompt distribution leaves some directions unobserved.
- Mixing token positions, layers, or normalizations combines different populations.
- Ambient noise inflates small singular values.
- Near a self-intersection, a distant manifold branch can become a Euclidean nearest neighbor.
- Visual structure in projections such as PCA or UMAP is treated as structure in the original space.

Distinguish points close along the original curve from points close in ambient distance on the hairpin below.

<figure class="lesson-figure" markdown="1">

![A hairpin curve has points on different branches only zero point two four apart in ambient distance but about two point three eight apart along the curve](../../figures/assets/A09-GEO/A09-GEO-07-branch-neighbors.svg)

<figcaption>The purple point on the opposite branch lies within radius 0.25 of the orange anchor, but the blue point at distance 0.30 on the same branch is excluded. The distance along the curve to the purple point is approximately 2.38. Even without an actual self-intersection, nearby branches can make ambient nearest neighbors differ from local neighbors along the curve.</figcaption>
</figure>

### What noise and projection change

For example, if isotropic noise independent of the signal and with mean 0 adds variance $\sigma^2$ to each ambient coordinate, the population covariance is the signal covariance plus $\sigma^2I$. Originally small eigenvalues increase as well. Counting all of them as meaningful tangent directions can overestimate dimension. Actual finite-sample covariance also contains estimation error beyond this population relationship.

A low-dimensional orthogonal PCA projection removes differences in unselected directions. This is why points separated in the original space can become close after projection. With nonlinearly arranged coordinates such as UMAP's, there is also no guarantee that the distance between two plotted points equals their distance under the original metric. To check a separation seen in a plot, recompute neighbors or within- and between-condition distances for the same samples under their original metric.

Inspect how much noise adds to each eigenvalue in the population covariance example below.

<figure class="lesson-figure" markdown="1">

![Independent isotropic noise with variance zero point zero four raises the three population covariance eigenvalues from one zero point one zero to one point zero four zero point one four zero point zero four](../../figures/assets/A09-GEO/A09-GEO-07-noise-eigenvalues.svg)

<figcaption>Independent isotropic noise with variance 0.04 adds 0.04I to the signal covariance diag(1,0.1,0). The third positive eigenvalue, 0.04, is noise-induced variance in this example, not evidence of a new signal direction. Actual finite samples retain additional estimation error.</figcaption>
</figure>

Projection changes the nearest-neighbor ordering among the three points below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Dropping the z coordinate projects A and B onto the same point and changes the nearest neighbor of A from C to B](../../figures/assets/A09-GEO/A09-GEO-07-projection-neighbor-flip.svg)

<figcaption>In the original space, A=(0,0,0), B=(0,0,2), and C=(1,0,0), so C is closer to A. Dropping the z direction makes A and B overlap and changes the nearer point to B. Post-projection neighbor relationships cannot replace those in the original space.</figcaption>
</figure>

### The question answered by each control

Use scale sweeps, bootstrap, shuffled labels, matched random subspaces, repeated seeds, and held-out prompts together. Estimator stability and a manifold causing the actual computation are separate claims.

A scale sweep checks sensitivity to neighborhood extent; bootstrap checks variation at the selected sampling-unit level. If several tokens from the same prompt are dependent, uncertainty obtained by independently resampling all tokens does not justify generalization across prompts. Label shuffling examines the correspondence between condition names and geometric structure. A label-free local PCA dimension does not change when only labels are shuffled, so shuffling itself cannot validate intrinsic dimension. Held-out prompts and repeated seeds ask whether the observed structure persists in other samples or training runs.

In the label shuffle below, only conditions change; point coordinates stay fixed.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Condition labels are shuffled among unchanged point coordinates while label-free neighborhoods and covariance remain identical](../../figures/assets/A09-GEO/A09-GEO-07-label-shuffle.svg)

<figcaption>The assignments of circles A and squares B change, but the points do not move. Label-free neighborhoods and overall covariance stay the same. This control examines correspondence between geometric measurements and conditions, not intrinsic dimension itself.</figcaption>
</figure>

## Small example

In a very small neighborhood of points on a circle, the local PCA dimension is close to 1. Combining a whole semicircle can require two principal directions and lead to a dimension overestimate of 2.

For the three semicircle points $(-1,0),(0,1),(1,0)$, the mean is $(0,1/3)$, and the sample covariance with denominator 2 is $\operatorname{diag}(1,1/3)$. Both eigenvalues are positive, but the circle's intrinsic dimension is still 1. The dimension of a linear subspace needed to describe different local directions together is not the number of manifold coordinates needed near each point.

Distinguish the two PCA directions of the centered points below from the circle's coordinate dimension.

<figure class="lesson-figure" markdown="1">

![Three centered semicircle points produce two positive covariance eigenvalues although the assumed generating circle has one-dimensional local coordinates](../../figures/assets/A09-GEO/A09-GEO-07-semicircle-covariance.svg)

<figcaption>This shows the three points in the text after subtracting their mean (0,1/3). The eigenvalues corresponding to the green and purple unit eigenvectors are 1 and 1/3, giving sample covariance rank 2. Yet the circle generating the samples still has one local coordinate. Linear variance dimension across the whole interval and local manifold dimension are different quantities.</figcaption>
</figure>

## Common misconceptions

- A good 2-dimensional visualization is not evidence of low intrinsic dimension.
- A small local dimension does not mean that features are disentangled.

## Exercises

### 1. Scale sweep
If $k=5$ gives $\hat d=1$ and $k=200$ gives $\hat d=8$, which value should be selected as correct?
<details><summary>Show solution</summary>

Do not choose one arbitrarily. Evaluate a range of scales balancing sample stability and curvature bias using prespecified criteria and bootstrap.
</details>

### 2. Projection artifact
Two clusters look separated in a 2-dimensional UMAP plot. How can separation in the original space be checked?
<details><summary>Show solution</summary>

Compute held-out classification or within- and between-condition distances under the original metric, and compare them with random-label and random-projection controls.
</details>

### 3. Mixing populations
Why can combining different token positions increase local dimension?
<details><summary>Show solution</summary>

If positions have different means or tangent directions, their combined covariance counts variation between populations as additional dimensions.
</details>

### 4. Claim strength
Does a stable local-dimension estimate alone justify claiming that an activation manifold causally determines model outputs?
<details><summary>Show solution</summary>

No. It provides evidence of descriptive structure. A causal claim requires interventions on the relevant directions and appropriate controls.
</details>

## Evidence and update boundaries

This lesson summarizes general identification limits of local PCA and neighborhood-based point-cloud analysis. It does not fix current rankings or default hyperparameters of particular manifold-learning algorithms.

## Lesson summary

- Finite activation samples are not the manifold itself.
- Neighborhood scale and noise affect dimension and curvature estimates.
- Projected shapes are not direct evidence of geometry in the original space.
- Scale sweeps, bootstrap, null controls, and held-out validation are needed.

## Pass criteria

- Can you state at least three causes of failure in activation manifold analysis?
- Can you distinguish descriptive geometric claims from causal claims?

## Next lesson

- [A09-GEO-08 Capstone exercise: local representation geometry](A09-GEO-08-capstone-local-geometry.md)

## Author checklist

- [x] Identification limits of activation manifold analysis are explained.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
