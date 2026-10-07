---
id: "A09-GEO-08"
title: "Capstone exercise: local representation geometry"
part: 4
stage: "A09-GEO"
status: "complete"
prerequisites: ["A09-GEO-01", "A09-GEO-02", "A09-GEO-03", "A09-GEO-04", "A09-GEO-05", "A09-GEO-06", "A09-GEO-07"]
estimated_time: "120–180 minutes"
---

# A09-GEO-08. Capstone exercise: local representation geometry

## Why this lesson matters

Reproducible analysis of local representation geometry requires fixing the dataset, layer, token, metric, and neighborhood first. This exercise combines local PCA, Jacobians, pullback metrics, and path length within a single claim–estimand–measurement structure.

## Learning objectives

- Define the experimental unit for local representation geometry analysis.
- Design procedures for estimating tangent spaces and pullback metrics.
- Construct a results table that includes bootstrap and null controls.
- Choose a claim strength supported by the observations.

## Prerequisite check

- Prerequisite lessons: [A09-GEO-01–07](A09-GEO-07-activation-manifold-pitfalls.md)
- Check question: What selection bias arises if neighborhood size is chosen after seeing the results?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $X_\ell$ | `X sub ell` | Activation matrix at layer $\ell$ | $n\times D$ |
| $U_r(x)$ | `U sub r of x` | Local PCA tangent basis | $D\times r$ |
| $J_h(x)$ | `the Jacobian of h at x` | Jacobian of the downstream map | Matrix |
| $\widehat L(\gamma)$ | `L hat of gamma` | Estimated length of a discrete path | Nonnegative scalar |

## Analysis contract

Limit the claim to: “At the fixed layer and token position, condition-specific activations show stable differences in local tangent structure across repeated samples.” The experimental unit is an independent prompt. Do not count tokens from the same prompt as independent repetitions.

Fix the following in advance.

1. Model checkpoint, prompt set, layer, token position, and normalization
2. Euclidean or another prespecified metric
3. Candidate neighborhoods and the selection rule
4. Local dimension threshold and number of bootstrap repetitions
5. Random-label, matched Gaussian, and random-subspace controls

The bootstrap below resamples prompt IDs while keeping the analyzed token position fixed.

<figure class="lesson-figure" markdown="1">

![Prompt-level bootstrap duplicates whole prompt groups P2 P2 P1 while retaining the same selected token position and keeping dependent tokens together](../../figures/assets/A09-GEO/A09-GEO-08-prompt-bootstrap.svg)

<figcaption>Each row is an independent prompt, and tokens in the same row form one dependent group. The green t2 is the fixed analysis position. If P2 is drawn twice in the bootstrap, that prompt's group enters twice. This differs from scattering and independently resampling tokens as if they were independent repetitions.</figcaption>
</figure>

## Measurement procedure

At each anchor $x$, compute the neighborhood covariance and its leading eigenvectors $U_r(x)$. The columns of $U_r(x)$ are $r$ mutually orthogonal unit eigenvectors that form a basis for the selected local tangent approximation. Interpreting this as the actual tangent space still requires the sample, noise, and scale conditions in GEO-07.

If the downstream map $h:\mathbb R^D\to\mathbb R^m$, with other inputs and model state fixed, is differentiable and the output metric is Euclidean, the tangent-restricted pullback metric is $U_r^\top J_h^\top J_hU_r$. Tangent coordinates $c\in\mathbb R^r$ map to the ambient direction $U_rc$, which then maps to output velocity $J_hU_rc$. Thus,

$$
\|J_hU_rc\|_2^2
=c^\top\bigl(U_r^\top J_h^\top J_hU_r\bigr)c
$$

$J_h$ has shape $m\times D$, and the restricted matrix has shape $r\times r$; both are evaluated at the same anchor. For an eigenvector $c$ with Euclidean norm 1 in PCA coordinates, its eigenvalue is the squared output gain, and the length gain is its square root. If the question concerns gain for a direction with length 1 under another input metric, that metric's input norm must also be accounted for. The restricted matrix is positive definite only when $J_hU_r$ has full column rank. If some directions in the tangent approximation vanish in the output to first order, it is semidefinite.

Follow how the tangent columns of U pass through the ambient columns of J in the numerical matrices below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A three by two tangent basis and two by three Jacobian compose into a two by two restricted Jacobian whose Gram matrix has squared gains four and one](../../figures/assets/A09-GEO/A09-GEO-08-restricted-shape.svg)

<figcaption>In this synthetic example, U selects two tangent directions in R³, and J maps directions in R³ to output velocities in R². Rows of JU are output coordinates; columns are tangent coordinates. Both axes of the restricted metric are tangent coordinates. For c=(1,0), the output velocity (2,0) gives squared gain 4 and length gain 2.</figcaption>
</figure>

Hold J fixed below and change only the selected tangent-approximation subspace.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The same downstream Jacobian yields positive definite restricted gains two and one on one subspace but gains two and zero on a subspace containing its null direction](../../figures/assets/A09-GEO/A09-GEO-08-restricted-gain-rank.svg)

<figcaption>For U=[e₁,e₂], JU distinguishes both directions, giving restricted eigenvalues 4,1 and length gains 2,1. For U=[e₁,e₃], the second direction vanishes in the output to first order, giving eigenvalues 4,0. Check full column rank of the actual selected JU, not just the rank of ambient J.</figcaption>
</figure>

For a discrete path $x_0,\ldots,x_T$, set $\Delta x_t=x_{t+1}-x_t$ and approximate its length by

$$
\widehat L(\gamma)=\sum_{t=0}^{T-1}
\sqrt{\Delta x_t^\top G(x_t)\Delta x_t}
$$

Between the $T+1$ points there are $T$ intervals, and each displacement is measured using the metric at the interval's starting point. For sufficiently small intervals in the same coordinate representation, this sum approximates the integral of metric speed. If intervals are long or the metric changes substantially, compare results after subdividing more finely. A sum connecting arbitrary activation points does not automatically equal the length of an actual path on the manifold or the shortest distance between two points.

Locate where each interval's starting-point metric is applied along the same path below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The same piecewise path has start-metric length estimates two and two point two five when its horizontal part is divided into one or two intervals](../../figures/assets/A09-GEO/A09-GEO-08-start-metric-sum.svg)

<figcaption>The path (0,0)→(1,0)→(1,1) is measured under the synthetic metric G(x,y)=diag((1+x)²,1). On the left, the interval-length estimate is 1+1=2. On the right, splitting the horizontal part in two applies the metrics at x=0 and x=0.5, giving 0.5+0.75+1=2.25. There are 2 intervals for 3 points and 3 intervals for 4 points.</figcaption>
</figure>

Compare estimates after further subdividing the same synthetic path below.

<figure class="lesson-figure" markdown="1">

![Left-endpoint metric length sums for the same synthetic path approach the integral length two point five as the horizontal subdivision count increases](../../figures/assets/A09-GEO/A09-GEO-08-path-refinement.svg)

<figcaption>Dividing the previous figure's horizontal part into n equal intervals gives L̂ₙ=2.5−1/(2n). As intervals shrink, the estimate approaches the integral length 2.5 of that same path. This numerically checks a synthetic metric; it does not establish that connections between arbitrary activation points are manifold paths or geodesics.</figcaption>
</figure>

Report the median and intervals from prompt-level bootstrap, and apply the same procedure to null data. Treat activations from the same prompt as a single resampling group. Record whether neighborhood covariances and tangent bases were also reestimated or whether only previously computed anchor-level measurements were resampled. The intervals from these two approaches include different sources of estimation variation.

## Results table

| Item | estimand | measurement | control | Permitted claim |
|---|---|---|---|---|
| local dimension | Condition-specific median $d$ | Local PCA spectrum | Gaussian; shuffle | Descriptive difference |
| tangent alignment | Subspace similarity | Principal angles | Random subspace | Alignment difference |
| pullback sensitivity | Gain in each tangent direction | Square root of a restricted metric eigenvalue | Matched norm | Local sensitivity |
| path length | Condition-specific metric length | Discrete sum | Permuted path | Path structure |

For local dimension, label shuffling examines correspondence between the computed dimension and condition names. It does not validate the label-free neighborhood structure itself. Tangent alignment compares subspaces in the same ambient coordinates and metric, while pullback sensitivity measures output-velocity magnitude under a fixed downstream map. Do not combine these different measurements into evidence that a semantic feature is used.

A permuted path changes the order of points and creates a different path. A length difference therefore provides evidence about order-dependent path structure, not a direct determination of intrinsic manifold dimension or whether the path is a geodesic. Limit each row's permitted claim to the scope of its computed estimand and controls.

Distinguish what subspace alignment and output-velocity gain measure below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Orthogonal input subspaces have a principal angle of ninety degrees while a fixed anisotropic downstream Jacobian maps their unit directions to gains two and one](../../figures/assets/A09-GEO/A09-GEO-08-alignment-versus-gain.svg)

<figcaption>The principal angle of 90° on the left describes the directional relationship between two subspaces under the same ambient inner product. On the right, the fixed J=diag(2,1) produces output-velocity magnitudes of 2 and 1 for the unit directions. Alignment and gain are different measurements, neither of which establishes use of a semantic feature on its own.</figcaption>
</figure>

Keep the same points and endpoints below and change only the order of intermediate points.

<figure class="lesson-figure" markdown="1">

![Permuting the middle points of a square changes the path length from three to one plus two square root two while preserving the same points and endpoints](../../figures/assets/A09-GEO/A09-GEO-08-permuted-path.svg)

<figcaption>Under the Euclidean metric, A→B→C→D has length 3, while A→C→B→D has length 1+2√2. The sample point set and endpoints stay the same, but changing the order creates a different path. A length difference under this permutation does not determine intrinsic dimension or whether a path is a geodesic.</figcaption>
</figure>

## Common misconceptions

- A narrow bootstrap interval does not mean that systematic bias is absent.
- Tangent alignment and causal feature reuse are different claims.

## Exercises

### 1. Experimental unit
Can 100 token activations from one prompt be counted as 100 independent samples?
<details><summary>Show solution</summary>

Generally not. Tokens from the same prompt and sequence are dependent, so prompt-level bootstrap or resampling that accounts for the dependence structure is needed.
</details>

### 2. Tangent comparison
State a measurement that can compare alignment between two $r$-dimensional tangent subspaces.
<details><summary>Show solution</summary>

Principal angles or singular values equal to their cosines can be used. Fix the same preprocessing and ambient inner product.
</details>

### 3. Metric ablation
A condition difference appears only under the Euclidean metric and disappears under a whitening metric. What should be reported?
<details><summary>Show solution</summary>

Report that the conclusion is sensitive to metric choice, and explain which variation each metric removes or emphasizes. Do not select only one result and generalize from it.
</details>

### 4. Claim ledger
Ablating a particular tangent direction changes the output. Does this alone establish that the direction is the unique causal mechanism?
<details><summary>Show solution</summary>

No. It is evidence of an intervention effect, but off-manifold perturbations, alternative paths, and nonspecific norm effects must be controlled to strengthen a uniqueness claim.
</details>

## Evidence and update boundaries

This exercise combines the preceding lessons' standard differential geometry and point-cloud estimation principles into a reproducible analysis contract. It provides no numerical results for a specific model. Reconsider the estimands and controls when the model or dataset changes.

## Lesson summary

- Fix the experimental unit and geometric choices before analysis.
- Local PCA and Jacobians measure tangent structure and local sensitivity.
- Apply bootstrap and null controls through the same pipeline.
- Distinguish the strength of claims about descriptive differences, intervention effects, and mechanisms.

## Pass criteria

- Can you complete a claim–estimand–measurement–control table?
- Can you limit conclusions when results are sensitive to the metric and neighborhood?

## Next lesson

- The next optional module is A09-DYN.

## Author checklist

- [x] The analysis contract for local representation geometry is complete.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
