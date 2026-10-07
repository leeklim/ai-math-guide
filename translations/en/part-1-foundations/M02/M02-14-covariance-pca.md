---
id: "M02-14"
title: "Covariance and PCA"
part: 1
stage: "M02"
status: "complete"
prerequisites:
  - "M02-12"
  - "M02-13"
estimated_time: "120~145 minutes"
---

# M02-14. Covariance and PCA

## Why this lesson matters

An activation matrix contains feature directions that vary together across samples. A covariance matrix records individual feature variances and joint variation between feature pairs. Principal component analysis (PCA) finds orthogonal directions of large covariance to summarize data variation using fewer coordinates.

PCA chooses directions by variance and linear reconstruction error. A high-variance direction is not automatically a semantic feature or causal circuit in a model. Report data selection, centering, and feature scales together.

## Learning objectives

By the end of this lesson, you should be able to:

- Compute a mean vector and center data stored in rows.
- Compute a sample covariance matrix from centered data.
- Explain symmetry and positive semidefiniteness of covariance matrices.
- Obtain principal directions and explained variance ratios by eigendecomposition.
- Explain the relation between data SVD and PCA through shapes and equations.
- Compute principal component scores and rank-$k$ reconstructions and judge their interpretation scope.

## Prerequisite check

- Prerequisite lesson: [M02-12 Symmetric matrices and the spectral theorem](M02-12-symmetric-matrices-spectral-theorem.md)
- Prerequisite lesson: [M02-13 Singular value decomposition](M02-13-singular-value-decomposition.md)
- Check question: Can you explain eigenvalue signs and an orthonormal eigenbasis for a symmetric PSD matrix?
- Check question: Can you explain what it means for right singular vectors of centered data to lie in feature space?

Review the prerequisite lessons first if spectral decomposition or SVD is unclear.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and conditions |
|---|---|---|---|
| $\mathbf X$ | `X` | A data matrix storing samples in rows | $\mathbf X\in\mathbb R^{N\times d}$ |
| $\boldsymbol\mu$ | `mu` | The vector of sample means for each feature | $\boldsymbol\mu\in\mathbb R^d$ |
| $\mathbf X_c$ | `X sub c` | Centered data with the mean subtracted | $N\times d$ |
| $\mathbf S$ | `S` | The sample covariance matrix | $\mathbf S=\frac{1}{N-1}\mathbf X_c^\top\mathbf X_c$ |
| $\mathbf v_i$ | `v sub i` | The $i$th principal direction | A unit vector in feature space |
| $\lambda_i$ | `lambda sub i` | The sample variance along principal direction $i$ | $\lambda_1\ge\cdots\ge0$ |
| $\mathbf Z$ | `Z` | The matrix of principal component scores | $\mathbf Z=\mathbf X_c\mathbf V_k$ |

## Core concept 1. PCA starts with mean-subtracted data

Store $N$ samples $\mathbf x_1,\ldots,\mathbf x_N\in\mathbb R^d$ in rows:

\[
\mathbf X=
\begin{bmatrix}
\mathbf x_1^\top\\
\vdots\\
\mathbf x_N^\top
\end{bmatrix}
\in\mathbb R^{N\times d}
\]

The mean vector is

\[
\boldsymbol\mu
=
\frac{1}{N}\sum_{n=1}^{N}\mathbf x_n
\]

Subtracting the mean from every row gives

\[
\mathbf X_c
=
\mathbf X-\mathbf 1\boldsymbol\mu^\top
\]

$\mathbf 1$ is an $N$-component column vector with every entry 1. Thus every row of $\mathbf 1\boldsymbol\mu^\top$ is the transpose of the same mean vector, and each sample has the same feature means subtracted. This differs from averaging features within one sample and subtracting that average.

The centered samples sum to $\sum_n\mathbf x_n-N\boldsymbol\mu=\mathbf 0$, so each feature column also sums to 0. The origin of these data represents the sample mean, not the zero vector of the original coordinates. Each centered row gives deviation from that mean. Without centering, PCA can identify a large direction due to a mean far from the origin rather than due to variation.

The figure below depicts subtracting the same mean vector from three samples as a translation. Differences between samples are unchanged; only the mean's position moves to the origin.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three samples translated by the same feature wise mean into centered samples with unchanged pairwise displacements](../../figures/assets/M02/M02-14-centering-translation.svg)

<figcaption>Subtracting (3,4) from every sample moves the mean to (0,0). Subtracting feature-wise means translates each point by the same vector; it does not average the two features within one sample.</figcaption>
</figure>

## Core concept 2. A covariance matrix records joint feature variation

For $N\ge2$, define the sample covariance matrix as

\[
\mathbf S
=
\frac{1}{N-1}\mathbf X_c^\top\mathbf X_c
\in\mathbb R^{d\times d}
\]

Its entries are

\[
s_{ij}
=
\frac{1}{N-1}
\sum_{n=1}^{N}
(x_{ni}-\mu_i)(x_{nj}-\mu_j)
\]

Entry $(i,j)$ is the inner product of centered columns $i$ and $j$. It multiplies two components with the same sample index $n$ before summing, not features from different samples. At $i=j$, summing squared deviations gives the sample variance $s_{ii}$ of feature $i$.

Off the diagonal, deviations with matching signs contribute positive terms, and opposite signs contribute negative terms. Thus $s_{ij}$ summarizes whether the two features deviate to the same or opposite sides of their respective means. A sum of 0 means these linear co-variations cancel; it does not guarantee statistical independence in general.

The figure below shows centered samples and the products of their two deviations. On the right, positive and negative products cancel even though the features are related.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Centered sample sets with positive negative and zero covariance showing same sign products opposite sign products and cancellation](../../figures/assets/M02/M02-14-covariance-signs.svg)

<figcaption>The product of two deviations is positive in same-sign quadrants and negative in opposite-sign quadrants. Covariance 0 means these products sum to 0; it can occur even for samples with a nonlinear relation, as on the right.</figcaption>
</figure>

This lesson uses the convention of dividing sample covariance by $N-1$. A centered column sums to 0, so specifying $N-1$ deviations determines the last one. M04 covers the statistical basis for estimating sample variance. References that divide by $N$ give covariance eigenvalues at a different scale, but the same centered data yield the same principal directions and explained variance ratios.

## Core concept 3. A covariance matrix is symmetric and PSD

Since

\[
\mathbf S^\top
=
\left(
\frac{1}{N-1}\mathbf X_c^\top\mathbf X_c
\right)^\top
=
\mathbf S
\]

the covariance matrix is symmetric.

For any $\mathbf v\in\mathbb R^d$,

\[
\mathbf v^\top\mathbf S\mathbf v
=
\frac{1}{N-1}
\|\mathbf X_c\mathbf v\|_2^2
\ge0
\]

so it is PSD. Its eigenvalues are therefore all at least 0, and an orthonormal eigenbasis can be chosen.

## Core concept 4. The first principal component maximizes projected variance

The scores obtained by projecting each centered sample onto a unit direction $\mathbf v$ are

\[
\mathbf z=\mathbf X_c\mathbf v
\]

Their sample variance is

\[
\frac{1}{N-1}\|\mathbf X_c\mathbf v\|_2^2
=
\mathbf v^\top\mathbf S\mathbf v
\]

The sum of the scores is the inner product of the summed centered samples with $\mathbf v$, so it is 0. Their mean is therefore 0 as well, letting us use the sum of squares without another mean-subtraction term. The unit-direction condition separates direction choice from simple scaling. Without it, multiplying the same direction by a large scalar could increase the variance value alone.

Under the condition

\[
\|\mathbf v\|_2=1
\]

the maximizing direction is an eigenvector $\mathbf v_1$ of $\mathbf S$ corresponding to its largest eigenvalue $\lambda_1$. The quadratic form from M02-12 verifies this. Expressing a candidate in the orthonormal eigenbasis as $\mathbf v=\sum_i c_i\mathbf v_i$ gives $\sum_i c_i^2=1$ and

\[
\mathbf v^\top\mathbf S\mathbf v
=\sum_i\lambda_i c_i^2
\le\lambda_1\sum_i c_i^2
=\lambda_1
\]

Choosing $\mathbf v=\mathbf v_1$ attains equality. Restricting the next direction to be orthogonal to $\mathbf v_1$ gives $c_1=0$, so the largest remaining eigenvalue $\lambda_2$ is the bound. Repeating this procedure selects later principal components.

The figure below projects a small centered sample set with the covariance in Example 2 onto two unit directions. A principal component is a direction in the feature space on the left; its scores are one scalar per sample, as on the right.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Four centered two dimensional samples projected onto two orthogonal principal directions giving score variances three and one](../../figures/assets/M02/M02-14-projected-variance.svg)

<figcaption>For the same four points, the score variance is 3 along the first direction and 1 along the orthogonal second direction. Their sum 4 is the total variance, so the first component explains 75%. Larger variance means the scores are more widely spread.</figcaption>
</figure>

## Core concept 5. Explained variance ratios measure the fraction retained

Order the covariance eigenvalues as

\[
\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_d\ge0
\]

The sum of diagonal entries of a square matrix is its trace:

\[
\operatorname{tr}(\mathbf S)
=
\sum_{j=1}^{d}s_{jj}
\]

The total variance is

\[
\operatorname{tr}(\mathbf S)
=
\sum_{i=1}^{d}\lambda_i
\]

In the spectral decomposition, diagonal entry $j$ sums each $\lambda_i$ times the square of component $j$ of $\mathbf v_i$. Summing over all $j$ leaves $\sum_i\lambda_i$, because each eigenvector's squared components sum to 1. The total variance in standard feature coordinates equals the total in orthonormal principal component coordinates.

The explained variance ratio of component $i$ is

\[
\frac{\lambda_i}
{\sum_{j=1}^{d}\lambda_j}
\]

and the cumulative ratio for the leading $k$ components is

\[
\frac{\sum_{i=1}^{k}\lambda_i}
{\sum_{j=1}^{d}\lambda_j}
\]

These ratios are undefined when the total data variance is 0.

## Core concept 6. PCA is equivalent to SVD of centered data

Let

\[
\mathbf X_c
=
\mathbf U\boldsymbol\Sigma\mathbf V^\top
\]

Then

\[
\mathbf S
=
\frac{1}{N-1}
\mathbf V\boldsymbol\Sigma^\top\boldsymbol\Sigma\mathbf V^\top
\]

The covariance eigenvectors are the right singular vectors of $\mathbf X_c$, with

\[
\lambda_i
=
\frac{\sigma_i^2}{N-1}
\]

Multiplying the $\mathbf X_c^\top\mathbf X_c$ decomposition from M02-13 by the common positive factor $1/(N-1)$ preserves eigenvectors and scales only the eigenvalues. If there are feature eigen-directions beyond the rectangular SVD's diagonal positions, their covariance eigenvalues are 0.

The right singular vectors here are feature directions with $d$ components. Computing $\mathbf X_c\mathbf v_i$ gives scores for the $N$ samples along that direction. When the sample count is much smaller than the feature count, PCA can be computed from the SVD of the centered $N\times d$ data without directly forming a $d\times d$ covariance matrix.

## Core concept 7. Scores and reconstruction give low-dimensional coordinates and approximations

Collect the leading $k$ principal components as columns in

\[
\mathbf V_k\in\mathbb R^{d\times k}
\]

The score matrix is

\[
\mathbf Z
=
\mathbf X_c\mathbf V_k
\in\mathbb R^{N\times k}
\]

Entry $(n,i)$ is the inner product of centered sample $n$ with principal direction $i$. Each row therefore contains that sample's $k$ directional coefficients, not the principal direction vectors themselves stored as data.

The rank-$k$ reconstruction of the centered data is

\[
\widehat{\mathbf X}_c
=
\mathbf Z\mathbf V_k^\top
=
\mathbf X_c\mathbf V_k\mathbf V_k^\top
\]

Restoring the mean gives

\[
\widehat{\mathbf X}
=
\widehat{\mathbf X}_c
+
\mathbf 1\boldsymbol\mu^\top
\]

M02-09 wrote the projection of a column vector $\mathbf x_c$ as $\mathbf V_k\mathbf V_k^\top\mathbf x_c$. Here, samples are rows, so its transpose $\mathbf x_c^\top\mathbf V_k\mathbf V_k^\top$ is applied to each row. Combining scores with the basis reconstructs a vector in the original $d$-component space, but does not restore discarded directional components.

PCA reconstruction projects each sample onto the leading principal subspace. For centered data, it gives the same matrix as truncated SVD, minimizing Frobenius-norm reconstruction error. Variances are squared singular values multiplied by the common factor $1/(N-1)$, so the cumulative explained variance ratio equals the fraction of the centered data's squared Frobenius norm preserved by the approximation. Adding the mean in the last stage restores the original data's position.

The left panel below shows the scores and reconstruction in Example 3. The separate right panel uses a mean of $(2,3)^\top$ to illustrate mean restoration. The residual along the discarded direction is unchanged between the two scenes.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A scalar principal component score reconstructs a projected vector and adding an illustrative mean moves both the sample and projection to original locations](../../figures/assets/M02/M02-14-score-reconstruction.svg)

<figcaption>Multiplying the unit principal component by the score 2√2 gives (2,2) in centered space. Adding the mean returns the approximation to its original location, but does not recover the discarded component (1,−1).</figcaption>
</figure>

## Core concept 8. Feature scales and sample selection change PCA

Variance is proportional to the square of the measurement unit. Multiplying one feature by a scalar $c$ multiplies its deviations by $c$ and its variance by $c^2$. Its covariance with other features is multiplied by $c$. Since this does not multiply the entire covariance matrix by one common value, principal directions can change.

The figure below multiplies only the second feature of the same four samples in the projected-variance figure by 3. Sample correspondence is preserved, but the point geometry stretches vertically, changing the direction of largest variance.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The same centered samples stretched by three in the second feature change covariance and tilt the first principal direction toward that feature](../../figures/assets/M02/M02-14-feature-scale-direction.svg)

<figcaption>The second feature's variance is multiplied by 9, and the covariance of the two features by 3. The first principal direction shifts from 45 degrees toward the vertical direction, so changing feature units must not be read as retaining the same geometry.</figcaption>
</figure>

Standardizing each centered feature by its own standard deviation reduces unit differences but also changes the analysis question. Standard deviation is the square root of its variance; a constant feature with standard deviation 0 cannot be divided this way. Center only to study variation in the original magnitudes; consider standardization to study relative variation across features. Record the preprocessing with the results.

Principal directions also depend on the analyzed data distribution. Changing layer, token, input set, or sample weights can change the covariance and principal components.

A principal vector's sign is not uniquely determined. Using $-\mathbf v_i$ instead of $\mathbf v_i$ also changes the score signs, but the projection and reconstruction subspace are unchanged. When comparing components across runs, align signs and repeated-eigenvalue subspaces.

## Example 1. Data varying along only one axis

Let three samples be

\[
\mathbf x_1=
\begin{bmatrix}2\\0\end{bmatrix},
\qquad
\mathbf x_2=
\begin{bmatrix}0\\0\end{bmatrix},
\qquad
\mathbf x_3=
\begin{bmatrix}-2\\0\end{bmatrix}
\]

The mean is the zero vector, and

\[
\mathbf X_c=
\begin{bmatrix}
2&0\\
0&0\\
-2&0
\end{bmatrix}
\]

The covariance is

\[
\mathbf S
=
\frac{1}{2}
\mathbf X_c^\top\mathbf X_c
=
\begin{bmatrix}
4&0\\
0&0
\end{bmatrix}
\]

The first principal direction is $\mathbf e_1$, with eigenvalue 4. The second eigenvalue is 0, so all variation lies along the first coordinate axis.

## Example 2. Rotated principal components

If

\[
\mathbf S=
\begin{bmatrix}
2&1\\
1&2
\end{bmatrix}
\]

then its eigenvalues are 3 and 1, with orthonormal eigenvectors

\[
\mathbf v_1=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\1\end{bmatrix},
\qquad
\mathbf v_2=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\-1\end{bmatrix}
\]

The first component is the direction in which the two features vary together with matching signs.

The explained variance ratios are

\[
\frac34
\qquad\text{and}\qquad
\frac14
\]

## Example 3. Reconstructing with one principal component

Use only the first component in Example 2. The score of the centered sample

\[
\mathbf x_c=
\begin{bmatrix}3\\1\end{bmatrix}
\]

is

\[
z_1
=
\mathbf x_c^\top\mathbf v_1
=
\frac{4}{\sqrt2}
=
2\sqrt2
\]

The reconstruction is

\[
\widehat{\mathbf x}_c
=
z_1\mathbf v_1
=
\begin{bmatrix}2\\2\end{bmatrix}
\]

The residual $\begin{bmatrix}1\\-1\end{bmatrix}$ is orthogonal to the first component.

## Example 4. Activation PCA

Collect activations at one layer and token position from $N$ inputs to form

\[
\mathbf H\in\mathbb R^{N\times d}
\]

Construct $\mathbf H_c$ by subtracting feature-wise sample means, not row means, and then apply SVD. The right singular vectors are principal directions in activation feature space.

A high explained variance ratio for the leading components shows that activation variation in the selected samples is concentrated in a low-dimensional linear subspace. Feature meaning, model use, and reproducibility on other data require further experiments.

## Common misconceptions

### Misconception 1. PCA finds directions relative to the origin, including the mean

Standard PCA subtracts each feature mean before finding directions of variation. Without centering, the mean location influences the result.

### Misconception 2. The first principal component is one of the original features

A principal component is a linear combination of the original features. Depending on covariance structure, its direction can differ from a coordinate axis.

### Misconception 3. Covariance 0 means two features are independent

Covariance 0 indicates no linear co-variation. Nonlinear dependence can remain.

### Misconception 4. A direction with high explained variance is a concept used by the model

Explained variance measures the geometric concentration of sample variation. Meaning and functional use require label comparisons, stability checks, and interventions.

## Exercises

### 1. Mean and centering

Find the mean vector and centered matrix $\mathbf X_c$ for

\[
\mathbf X=
\begin{bmatrix}
1&2\\
3&4\\
5&6
\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

The feature-wise means are

\[
\boldsymbol\mu=
\begin{bmatrix}3\\4\end{bmatrix}
\]

Subtracting the mean from each row gives

\[
\mathbf X_c=
\begin{bmatrix}
-2&-2\\
0&0\\
2&2
\end{bmatrix}
\]

Each column sums to 0.

</details>

### 2. A covariance matrix

Compute the sample covariance matrix from $\mathbf X_c$ in Exercise 1.

<details>
<summary>Show solution</summary>

Since $N=3$, we have $N-1=2$.

\[
\mathbf X_c^\top\mathbf X_c
=
\begin{bmatrix}
8&8\\
8&8
\end{bmatrix}
\]

Thus

\[
\mathbf S
=
\frac12
\begin{bmatrix}
8&8\\
8&8
\end{bmatrix}
=
\begin{bmatrix}
4&4\\
4&4
\end{bmatrix}
\]

</details>

### 3. Principal components and eigenvalues

Find the first principal direction and both eigenvalues of the covariance matrix in Exercise 2.

<details>
<summary>Show solution</summary>

\[
\mathbf S
\begin{bmatrix}1\\1\end{bmatrix}
=
\begin{bmatrix}8\\8\end{bmatrix}
=
8
\begin{bmatrix}1\\1\end{bmatrix}
\]

The first eigenvalue is therefore 8, and the normalized first component is

\[
\mathbf v_1=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\1\end{bmatrix}
\]

The orthogonal direction $\begin{bmatrix}1\\-1\end{bmatrix}$ has eigenvalue 0.

</details>

### 4. Explained variance ratios

For PCA eigenvalues $9,3,2,1$, find the explained variance ratio of the first component and the leading two components.

<details>
<summary>Show solution</summary>

Total variance is

\[
9+3+2+1=15
\]

The first component's ratio is

\[
\frac{9}{15}=0.6
\]

The cumulative ratio of the leading two is

\[
\frac{9+3}{15}=0.8
\]

</details>

### 5. PCA and SVD

Centered data with $N=101$ have singular values $\sigma_1=20$, $\sigma_2=10$. Find the corresponding covariance eigenvalues.

<details>
<summary>Show solution</summary>

We have

\[
\lambda_i
=
\frac{\sigma_i^2}{N-1}
\]

and $N-1=100$. Therefore,

\[
\lambda_1=\frac{400}{100}=4,
\qquad
\lambda_2=\frac{100}{100}=1
\]

</details>

### 6. Score and reconstruction shapes

Let

\[
\mathbf X_c\in\mathbb R^{200\times64},
\qquad
\mathbf V_5\in\mathbb R^{64\times5}
\]

Find the shapes of $\mathbf Z=\mathbf X_c\mathbf V_5$ and $\widehat{\mathbf X}_c=\mathbf Z\mathbf V_5^\top$.

<details>
<summary>Show solution</summary>

\[
\mathbf Z\in\mathbb R^{200\times5}
\]

and

\[
\widehat{\mathbf X}_c\in\mathbb R^{200\times64}
\]

Each sample is reduced to 5-dimensional scores, then reconstructed in the original 64-dimensional feature space.

</details>

### 7. Critiquing activation PCA claims

The first 8 principal components explain 90% of the activation variance at a particular model layer. Distinguish:

1. What is directly supported for these data.
2. Conditions to report for reproducibility.
3. Claims that cannot be made without interventions.

<details>
<summary>Show solution</summary>

For the selected activation samples, 90% of the total sample variance lies in the subspace of the leading 8 principal components.

Report model and checkpoint, layer and token position, input data, centering and standardization, sample count, and seed. Compare whether the principal subspace is maintained on other samples or models.

PCA alone does not establish that each component is one human-interpretable concept, that the model uses this subspace for prediction, or that 8 dimensions suffice for the task. Label-based verification and interventions are needed.

</details>

## Lesson summary

- PCA starts with samples stored in rows and feature means subtracted to center the data.
- Sample covariance is $\frac{1}{N-1}\mathbf X_c^\top\mathbf X_c$ and is symmetric PSD.
- Principal directions are orthonormal covariance eigenvectors, and eigenvalues are variances of projected scores.
- Explained variance ratios give each component's fraction of total variance.
- Right singular vectors of centered data are PCA directions, with $\lambda_i=\sigma_i^2/(N-1)$.
- PCA depends on data, preprocessing, and basis signs; it does not directly establish meaning or functional use.

## Pass criteria

You pass if you can answer these questions without consulting the material.

- Can you center a data matrix and compute covariance?
- Can you explain why covariance is symmetric PSD?
- Can you obtain principal components and explained variance ratios from an eigendecomposition?
- Can you explain the relation between PCA and SVD of centered data?
- Can you track the shapes of scores and rank-$k$ reconstructions?
- Can you explain PCA's dependence on preprocessing and data, and the scope of its claims?

## Next lesson

- [M02-15 Norms and condition numbers](M02-15-norm-condition-number.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] The row-wise data convention and centering are specified.
- [x] Covariance entries, symmetry, and PSD are explained.
- [x] PCA variance maximization and explained variance ratios are connected.
- [x] SVD, score shapes, and reconstruction shapes are given.
- [x] Every exercise has a solution.
- [x] Data and preprocessing dependence are distinguished from limits on functional claims.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
