---
id: "I06-05"
title: "PCA and SVD analysis"
part: 3
stage: "I06"
status: "complete"
prerequisites: ["I06-04", "M02-13", "M02-14"]
estimated_time: "110~140 minutes"
---

# I06-05. PCA and SVD analysis

## Why this lesson matters

Activations have hundreds of dimensions, so tables of individual coordinates make their variation hard to see. PCA finds orthogonal directions with large variation in the sample, and SVD provides a stable way to compute them. A high-variance direction is not necessarily meaningful or used by the model.

## Learning objectives

- Center an activation matrix and compute its SVD.
- Explain the shapes of singular values, principal directions, and scores.
- Compute explained variance and rank-$k$ reconstruction error.
- Distinguish the information a PCA plot preserves from the information it discards.

## Prerequisite check

- Prerequisite lessons: [I06-04 Neuron-level analysis](I06-04-neuron-level-analysis.md), [M02-13 Singular value decomposition](../../part-1-foundations/M02/M02-13-singular-value-decomposition.md), [M02-14 Covariance and PCA](../../part-1-foundations/M02/M02-14-covariance-pca.md)
- Check question: What can attract the first singular direction if the data are not centered?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $X_c$ | `X centered` | A matrix obtained by subtracting the sample mean from each activation row | $n\times d$ |
| $X_c=U\Sigma V^T$ | `X centered equals U Sigma V transpose` | SVD of centered activations | matrix factorization |
| $v_k$ | `the k-th right singular vector` | Principal direction $k$ | $\mathbb R^d$ |
| $X_cv_k$ | `X centered times v sub k` | Principal score $k$ for each sample | $\mathbb R^n$ |
| explained variance ratio | `explained variance ratio` | The fraction of total squared variation accounted for by a component | $[0,1]$ |
| rank-$k$ approximation | `rank k approximation` | An approximation retaining only the top $k$ singular triplets | $n\times d$ |

## 1. What rows and columns mean

Write the activation dataset as

\[
X=\begin{bmatrix}a_1^T\\ \vdots\\ a_n^T\end{bmatrix}\in\mathbb R^{n\times d}
\]

Rows are input observation units, and columns are activation coordinates. Subtract the mean vector $\bar a$ to form

\[
X_c=X-\mathbf 1\bar a^T
\]

Without centering, the direction from the origin to the mean can appear to be a direction of variation.

Subtracting the same mean from both rows leaves the difference between the points unchanged; only the location of their mean changes.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The prerequisite vectors one zero and three four move by subtracting their common mean two two; the centered pair has zero mean.](../../figures/assets/I06/I06-05-centering-two-vectors.svg)

<figcaption>The two vectors from the prerequisite lesson illustrate centering. Subtracting the same mean (2,2) from both rows gives (−1,−2) and (1,2), moving the new mean to the origin.</figcaption>
</figure>

## 2. Read PCA from the SVD

In

\[
X_c=U\Sigma V^T
\]

the columns of $V$ are orthogonal directions in activation space. The score matrix is

\[
Z=X_cV=U\Sigma
\]

Plotting the first two scores in a scatter plot projects each input onto the two directions with the largest variation.

In a thin SVD, $U$ has shape $n\times\min(n,d)$, $\Sigma$ has shape $\min(n,d)\times\min(n,d)$, and $V$ has shape $d\times\min(n,d)$. A full SVD extends $U$ and $V$ to complete orthogonal bases with shapes $n\times n$ and $d\times d$, respectively. This lesson uses $Z=U\Sigma$ for scores in the thin form. The rows of the returned $V^T$ in the implementation are the principal directions. For example, if $n=100$ and $d=768$, thin $V$ is $768\times100$, whereas full $V$ is $768\times768$.

Score $k$ is the component of each centered input along $v_k$. Since $X_cv_k=\sigma_ku_k$ and the squared norm of $u_k$ is 1, the sum of squared scores is $\sigma_k^2$. The sample covariance also satisfies

\[
\frac{X_c^TX_c}{n-1}=V\frac{\Sigma^2}{n-1}V^T
\]

so the sample variance along $v_k$ is $\sigma_k^2/(n-1)$. This expression requires $n>1$.

The explained variance ratio for component $k$ is

\[
\rho_k=\frac{\sigma_k^2}{\sum_j\sigma_j^2}
\]

If the first two ratios sum to 0.8, those directions explain 80% of the sample's centered squared variation.

The common denominator $n-1$ cancels in the variance ratio, leaving a ratio of squared singular values. If all centered activations are 0, the sum of squares is also 0, and the ratio is undefined. Flipping a direction's sign leaves the sum of squared scores unchanged, so it does not change explained variance.

Check the number of directions separately from the squared variation each direction explains.

<figure class="lesson-figure" markdown="1">

![Singular values three two and one contribute squared amounts nine four and one, totaling fourteen and giving first explained variance nine fourteenths.](../../figures/assets/I06/I06-05-squared-singular-energy.svg)

<figcaption>The exercise's singular values 3,2,1 correspond to squared variations 9,4,1. The first component's ratio is 9/14, not 3/6.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![For a 100 by 768 centered matrix, the thin right singular basis has 768 by 100 shape while the full basis is 768 by 768, and thin scores have one row per input.](../../figures/assets/I06/I06-05-thin-full-directions.svg)

<figcaption>In the text's 100×768 example, thin V contains 100 directions, while full V contains a complete basis of 768 directions. Thin scores Z=UΣ have 100 rows, one for each input. Principal directions are the rows of Vᵀ returned by the implementation.</figcaption>
</figure>

## 3. Low-rank approximation and error

Keeping only the top $k$ components gives

\[
X_{c,k}=U_{:,1:k}\Sigma_{1:k,1:k}V_{:,1:k}^T
\]

This is the optimal rank-$k$ approximation in the Frobenius norm. Examine the relative error

\[
\frac{\lVert X_c-X_{c,k}\rVert_F}{\lVert X_c\rVert_F}
\]

to check the loss from compression.

Squared errors of orthogonal singular components add, so the error from the discarded components is

\[
\lVert X_c-X_{c,k}\rVert_F^2=\sum_{j>k}\sigma_j^2
\]

Thus, when $\lVert X_c\rVert_F>0$, the relative error is $\sqrt{1-\sum_{j=1}^k\rho_j}$. An explained variance of 80% means that 20% of the squared variation was discarded, not that the relative norm error itself is 20%. To approximate the original activations, add the subtracted mean $\mathbf 1\bar a^T$ back to $X_{c,k}$.

The following curve connects retained squared variation to norm error.

<figure class="lesson-figure" markdown="1">

![The exact relative norm error curve equals square root of one minus retained squared variation; retaining eighty percent gives about 0.447 norm error.](../../figures/assets/I06/I06-05-retained-variation-error.svg)

<figcaption>Retaining 80% of squared variation gives a relative norm error of √0.2≈0.447. Distinguish the discarded squared fraction 0.2 from the norm error. Add the mean back when approximating the original values.</figcaption>
</figure>

## 4. Limits of interpretation

PCA finds high-variance directions without looking at labels. If sentence length, token position, or norm scale produces the largest variation, the first component may reflect it. A low-variance direction can still matter for behavior.

A principal direction's sign is arbitrary. $v$ and $-v$ define the same axis. When seeds or samples change, individual directions associated with nearby singular values may rotate, so examine subspace stability as well.

Distinguish axis sign, large variation, and the stability of individual directions.

<figure class="lesson-figure" markdown="1">

![Opposite vectors v and minus v span the same line; flipping the direction flips scores but keeps squared variation unchanged.](../../figures/assets/I06/I06-05-direction-sign.svg)

<figcaption>v and −v define the same 1-dimensional axis. Flipping both the direction and score signs preserves the sum of squared scores and explained variance.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![A schematic point cloud has much wider horizontal variation than vertical label separation, so the largest variance direction need not be the label direction.](../../figures/assets/I06/I06-05-variance-label-direction.svg)

<figcaption>This schematic shows two groups with large horizontal variation. Even if PC1 summarizes that variation, the vertical direction separating the labels serves a different role. The schematic does not determine whether an actual model uses either direction.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![Two orthogonal pairs of directions form different bases of the same shaded plane; near-equal singular values make individual direction comparisons less stable than their span.](../../figures/assets/I06/I06-05-near-singular-subspace.svg)

<figcaption>The blue and purple directions are different orthogonal bases of the same plane. Equal singular values give the same reconstruction performance. When values are close, individual directions can be unstable to compare, so compare their span as well.</figcaption>
</figure>

## CPU exercise

Mix a 2-dimensional latent representation into 6 dimensions and add a small amount of noise. Check whether the top two singular values of the centered matrix explain most of the variation.

<!-- I06_EXAMPLE: i06_05_pca_svd -->

The result is good because the synthetic data were constructed to be low-rank. Do not assume actual activations will produce the same ratio.

## Common misconceptions

### Misconception 1. PC1 is the most important feature

PC1 is the direction with the largest variance in this sample. That criterion differs from behavioral importance or a human-assigned concept.

### Misconception 2. Overlapping groups in a two-dimensional plot mean there is no information

The discarded directions may contain label information. The plot is a projection.

### Misconception 3. A coordinate with a large loading is a cause

A loading expresses a principal direction in coordinates. It does not measure causal contribution.

## Exercises

### 1. Shape

If $X_c$ is $100\times768$, what are the shape of $V$ in a full SVD and the shape of the first score vector?

<details><summary>Show solution</summary>With full_matrices=False, $V$ typically contains 100 right singular vectors, giving shape $768\times100$, and the first score $X_cv_1$ has length 100. Distinguish this from the shape of $V^T$ returned by the implementation.</details>

### 2. Centering

The same vector $c$ is added to every activation. What happens to the centered PCA result?

<details><summary>Show solution</summary>The new mean also increases by $c$, so centering cancels the change. Apart from numerical error, the centered matrix and PCA remain the same.</details>

### 3. Explained variance

If the singular values are $3,2,1$, what is the first component's explained variance ratio?

<details><summary>Show solution</summary>It is $3^2/(3^2+2^2+1^2)=9/14$. Use the squared singular values, not the singular values themselves.</details>

### 4. Sign

Another run returns $-v_1$ in place of $v_1$. Is this a different axis?

<details><summary>Show solution</summary>It is the same 1-dimensional axis. The score sign also flips, so align signs before comparing.</details>

### 5. Interpret a plot

Two conditions separate in PC1 and PC2. Does this guarantee a linear probe will succeed on the test set?

<details><summary>Show solution</summary>No. The plot may have been made by examining the same sample, without held-out performance or controls. Evaluate the probe on a separate split.</details>

### 6. Nearby singular values

Why can comparing individual $v_2,v_3$ be unstable when $\sigma_2\approx\sigma_3$?

<details><summary>Show solution</summary>When the two values are equal or close, different orthogonal bases within the same 2-dimensional subspace produce similar reconstruction errors. Compare the span rather than individual directions.</details>

## Evidence and update boundaries

The mathematics of SVD and PCA follows the definitions in M02-13~14. The distinction between subspaces and invariances in representation comparisons connects to [Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html). Library-specific randomized SVD options are implementation details.

## Lesson summary

- Center the activation matrix, then obtain principal directions and scores from its SVD.
- Use squared singular values to compute explained variance.
- PCA summarizes large variation; it does not directly measure meaning, use, or causation.
- For nearby singular values, a subspace is more stable than individual directions.

## Pass criteria

- Can you explain the SVD factors' shapes and PCA scores?
- Can you compute explained variance and rank-$k$ error?
- Can you state claims that a PCA plot does not support?

## Next lesson

- [I06-06 Linear probe](I06-06-linear-probe.md)

## Author checklist

- [x] PCA and SVD computations are connected to their interpretive limits.
- [x] Every exercise has a solution.
- [x] The strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and mathematical rendering have been checked.
