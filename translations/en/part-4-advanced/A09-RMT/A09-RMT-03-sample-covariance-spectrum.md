---
id: "A09-RMT-03"
title: "The sample covariance spectrum"
part: 4
stage: "A09-RMT"
status: "complete"
prerequisites: ["M02-12", "M02-14", "M04-06"]
estimated_time: "90–120 minutes"
---

# A09-RMT-03. The sample covariance spectrum

## Why this lesson matters

Interpreting activation covariance eigenvalues as population variance directions requires accounting for finite-sample noise. When dimension $d$ is comparable to sample count $n$, sample eigenvalues spread widely even if population covariance is the identity.

## Learning objectives

- Calculate sample covariance from a centered data matrix.
- Explain how sample count and dimension limit covariance rank.
- Explain how aspect ratio affects spectral noise.
- Specify experimental units when comparing activation covariances.

## Prerequisite check

- Prerequisite lessons: [M02-12 Symmetric matrices and the spectral theorem](../../part-1-foundations/M02/M02-12-symmetric-matrices-spectral-theorem.md), [M02-14 Covariance and PCA](../../part-1-foundations/M02/M02-14-covariance-pca.md), [M04-06 Samples, populations, and sampling distributions](../../part-1-foundations/M04/M04-06-samples-populations-sampling-distributions.md)
- Check question: For centered data matrix $X\in\mathbb R^{n\times d}$, what is the shape of $X^\top X$?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $X_c$ | `X sub c` | Data matrix with each feature's sample mean subtracted | $n\times d$ |
| $S=\frac1nX_c^\top X_c$ | `S equals one over n times X sub c transpose X sub c` | Sample covariance convention | $d\times d$ |
| $\gamma=d/n$ | `gamma equals d over n` | Dimension-to-sample aspect ratio | positive scalar |
| $\lambda_j(S)$ | `lambda sub j of S` | Sample variance eigenvalue | nonnegative scalar |

## Core concepts

### Centering and the directional meaning of covariance

In a data matrix with samples as rows and features as columns, subtract the mean $\bar x_j=n^{-1}\sum_i x_{ij}$ of column $j$. Thus, $(X_c)_{ij}=x_{ij}-\bar x_j$, and each column sums to zero across rows. For centered matrix $X_c$, define sample covariance as

$$
S=\frac1nX_c^\top X_c
$$

Entry $S_{jk}=n^{-1}\sum_i(x_{ij}-\bar x_j)(x_{ik}-\bar x_k)$ measures how two features vary together across samples. Choosing a unit direction $v\in\mathbb R^d$ that combines features gives

$$
v^\top Sv=\frac1n\lVert X_cv\rVert^2
=\frac1n\sum_i\bigl((x_i-\bar x)^\top v\bigr)^2
$$

This is the sample variance of values projected onto that direction and is always nonnegative. The expression establishes that $S$ is PSD. For a unit eigenvector $v_j$, $v_j^\top Sv_j=\lambda_j(S)$, letting us read eigenvalues as directional variances.

The $1/(n-1)$ convention is also used, so report the denominator. If i.i.d. rows have population covariance $\Sigma$, the expression above with a subtracted sample mean and factor $1/n$ gives $E[S]=(n-1)\Sigma/n$. For $n>1$, the expression with factor $1/(n-1)$ is unbiased. Changing only the denominator for the same data preserves eigenvectors and multiplies eigenvalues by $n/(n-1)$. Directly comparing spectra with different normalizations can mistake a scale difference for a structural difference.

The next figures separately trace mean subtraction, variance along unit directions, and denominator changes for the same small dataset.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three illustrative data points have mean three two and translate to centered points minus one minus one one minus one zero two.](../../figures/assets/A09-RMT/A09-RMT-03-sample-mean-centering.svg)

<figcaption>The three illustrative rows (2,1), (4,1), and (3,4) have sample mean (3,2). On the right, subtracting this mean from the same rows gives (−1,−1), (1,−1), and (0,2), with each column summing to zero. Translation does not change relative positions between points.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![For the centered three row example covariance diagonal two thirds two the sample variance along a unit direction changes with its angle and reaches eigenvalues at coordinate directions.](../../figures/assets/A09-RMT/A09-RMT-03-unit-direction-variance.svg)

<figcaption>The preceding centered rows give S=diag(2/3,2). For unit direction v=(cosθ,sinθ), projected variance vᵀSv is 2/3 at 0° and 180° and 2 at 90°. It is always nonnegative and equals the corresponding eigenvalue along an eigenvector direction.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![The same coordinate eigenvectors have covariance eigenvalues two thirds two with denominator three and one three with denominator two.](../../figures/assets/A09-RMT/A09-RMT-03-denominator-eigenvalue-rescaling.svg)

<figcaption>Changing the denominator from 3 to 2 for the same three rows multiplies eigenvalues by n/(n−1)=1.5. The e₁ and e₂ directions are unchanged; only values grow from 2/3 to 1 and from 2 to 3. Do not interpret this as a new direction of anisotropy.</figcaption>

</figure>

### Centering and rank limits

The columns of $X_c$ all lie in the subspace of $\mathbb R^n$ whose entries sum to zero. This subspace has dimension $n-1$, so $\operatorname{rank}(X_c)\le\min(d,n-1)$. Also, $Sv=0$ implies $v^\top Sv=\lVert X_cv\rVert^2/n=0$ and therefore $X_cv=0$; the reverse implication holds as well. The two matrices have the same feature-space null directions, and $\operatorname{rank}(S)=\operatorname{rank}(X_c)$.

Consequently, $d\ge n$ gives at least $d-n+1$ zero eigenvalues. Duplicate data or additional linear constraints can reduce rank further. A zero eigenvalue indicates a direction in which no variation was observed among the collected centered rows, not that new samples also cannot vary in that direction.

Writing the nonzero singular values of $X_c=U\Sigma_XV^\top$ as $s_j$ gives nonzero eigenvalues $s_j^2/n$ for $S$. Here $V$ gives feature directions and $U$ sample directions. $X_cX_c^\top/n$ has the same nonzero eigenvalues but is an $n\times n$ matrix. The two spectra differ in their zero counts and the meanings of their directions.

The figures below show dependence among centered rows and the nonzero spectrum shared by the two Gram matrices as different structures.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![In a three by two centered matrix the last row zero two equals the negative sum of the first rows minus one minus one and one minus one.](../../figures/assets/A09-RMT/A09-RMT-03-last-centered-row-dependent.svg)

<figcaption>In the same n=3, d=2 example, the last row (0,2) is the negative sum of the first two rows. Centering makes the row sum zero, determining one row from the other n−1 rows, so rank is at most min(d,n−1). Other dependencies can make it smaller.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A seeded centered forty by one hundred isotropic Gaussian matrix produces covariance with sixty one zero eigenvalues and sample Gram with one zero while sharing thirty nine positive eigenvalues.](../../figures/assets/A09-RMT/A09-RMT-03-feature-and-sample-gram-spectra.svg)

<figcaption>An illustrative i.i.d. Gaussian X with the existing n=40, d=100 specification is drawn and centered to obtain Xc. At centered rank 39, feature covariance has 61 zeros and the sample Gram matrix has 1, sharing the same 39 nonzero eigenvalues. Sample and feature directions differ. Numerical-error-level zeros are displayed as zero; they do not indicate a null space of population covariance I₁₀₀.</figcaption>

</figure>

### Entry errors and spectral errors

At a fixed small $d$, increasing the number of i.i.d. rows with finite second moments makes each sample covariance entry approach its population value. Because matrix size is fixed, entrywise convergence also gives spectral convergence. This is the classical regime.

In the high-dimensional regime $d/n\to\gamma>0$, matrix size grows as well. Small entrywise errors alone do not establish small errors across all directions. For example, even with $\Sigma=I_d$, finite-sample off-diagonal entries need not be exactly zero. Acting together, these entries spread eigenvalues around 1. When $\gamma$ stays fixed, the width of this spread generally does not vanish.

What remains is distortion between population eigenvalues and the sample spectrum, not persistent large random fluctuations of each sample eigenvalue. Under an i.i.d. isotropic null, the eigenvalue distribution of a large matrix can itself stabilize into a consistent bulk shape. The next lesson explains this distinction.

The illustrative samples below show that an identity population can still give a spread-out sample spectrum. Entry errors and eigenvalue distortion are not treated as the same value.

<figure class="lesson-figure" markdown="1">

![Two seeded illustrative isotropic samples with four hundred rows and dimensions twenty and two hundred have distinct sample eigenvalue spreads around population eigenvalue one.](../../figures/assets/A09-RMT/A09-RMT-03-aspect-ratio-sample-spread.svg)

<figcaption>Both illustrative Gaussian samples have population covariance I and n=400. Comparing d=20 with γ=0.05 and d=200 with γ=0.5 shows the sorted spread of sample eigenvalues. This pair of finite samples is neither a proof of an asymptotic law nor an observation from actual layers.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![The same two illustrative samples compare root mean squared off diagonal entries with the largest sample eigenvalue excess over one.](../../figures/assets/A09-RMT/A09-RMT-03-entrywise-versus-directional-error.svg)

<figcaption>For the same samples as above, the root mean square of off-diagonal entries is compared with max eigenvalue−1. These summarize different errors, showing why a large matrix's spectrum cannot be replaced by the magnitude of one of its small entries. No new general simultaneous bound or asymptotic fluctuation size is claimed.</figcaption>

</figure>

### Matrix rows and independent observational units

When activation rows are tokens, dependence among tokens from the same prompt can reduce effective sample size. Distinguish $n$ in a rank calculation from the count of independent units used for uncertainty.

Rank and $d/n$ calculations use the actual number of rows in the matrix. A prompt-level bootstrap resamples each prompt's token group together, retaining dependence. Substituting the independent prompt count for $n$ does not automatically make an MP formula valid. Using an i.i.d.-row model requires a separate check of that assumption; a null preserving row dependence may have a different spectral distribution.

The next figure places actual matrix row count and prompt-pack count on different calculation paths.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Twenty prompt packs containing fifty token rows each branch to matrix row count one thousand and prompt level bootstrap count twenty without changing the matrix aspect ratio by substitution.](../../figures/assets/A09-RMT/A09-RMT-03-matrix-rows-versus-bootstrap-packs.svg)

<figcaption>The existing exercise's 20 prompts with 50 tokens each give 1,000 matrix rows and 20 prompt-bootstrap packs. Selecting one pack selects its 50 rows together. This is not a rule for replacing n in the rank calculation with 20 or substituting 20 into an i.i.d. MP formula.</figcaption>

</figure>

## Small example

For centered data with $n=40$ and $d=100$, rank is at most 39. $S$ has at least 61 zero eigenvalues. Those zeros do not establish 61 exact null directions in population covariance.

The matrix is observed through at most 39 nonzero sample directions, leaving the other feature directions unresolved. The same rank limit applies even when population covariance is $I_{100}$. This example has $\gamma=100/40=2.5$, and changing the denominator to $n-1$ does not change the zero count.

## Common misconceptions

- Unequal sample eigenvalues alone do not prove population anisotropy.
- Treating token count directly as independent sample count can ignore prompt-level dependence.

## Exercises

### 1. Shape
If $X_c$ is $80\times300$, what is the shape of $S$?
<details><summary>Show solution</summary>

Since it is formed from $X_c^\top X_c$, $S$ is $300\times300$.
</details>

### 2. Rank
For centered data with $n=25$ and $d=60$, give an upper bound on covariance rank and a lower bound on the number of zero eigenvalues.
<details><summary>Show solution</summary>

Rank is at most $n-1=24$, and there are at least $60-24=36$ zero eigenvalues.
</details>

### 3. Aspect ratio
For $d=500$ and $n=1000$, what is $\gamma$?
<details><summary>Show solution</summary>

$\gamma=d/n=0.5$.
</details>

### 4. Model interpretation
You collect 20 prompts with 50 tokens each. What can be used as the covariance matrix's row count and the bootstrap unit, respectively?
<details><summary>Show solution</summary>

With conditions fixed, the matrix can use 1,000 token rows, while the top-level uncertainty-bootstrap units are the 20 prompts.
</details>

## Sources and update boundaries

Sample covariance uses normalization $1/n$. Dependent rows violate the next null model's i.i.d. assumption. Heavy-tailed rows can be i.i.d., but moment conditions and extreme-eigenvalue behavior must be checked separately.

The relation between centered Gram matrices and PCA directions follows [CMU, Once More with PCA](https://stat.cmu.edu/~cshalizi/dm/20/lectures/13/lecture-13.html). Centering's rank limit and normalization differences are developed directly in this lesson. High-dimensional bulk and finite-size eigenvalue fluctuations are distinguished with their assumptions in the next lesson.

## Lesson summary

- Sample covariance is the Gram operator of centered data.
- Rank is limited by the smaller of $d$ and $n-1$.
- In the high-dimensional regime, even an identity population gives a broad sample spectrum.
- Matrix row count and independent resampling-unit count can differ.

## Pass criteria

- Can you calculate sample covariance shape, rank, and aspect ratio?
- Can you explain why sample eigenvalue dispersion must be distinguished from population signal?

## Next lesson

- [A09-RMT-04 Intuition for the Marchenko–Pastur law](A09-RMT-04-marchenko-pastur-intuition.md)

## Author checklist

- [x] Covariance spectrum rank and high-dimensional noise are explained.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
