---
id: "I06-08"
title: "CCA, CKA, and RSA"
part: 3
stage: "I06"
status: "complete"
prerequisites: ["I06-07", "M02-14"]
estimated_time: "130–160 minutes"
---

# I06-08. CCA, CKA, and RSA

## Why this lesson matters

Activations from different layers, seeds, or models may have different numbers of coordinates and different bases. Instead of directly subtracting raw coordinates, decide which transformations the comparison should be invariant to. CCA, CKA, and RSA preserve different relationships and should not be grouped together under the same phrase, `representation similarity`.

## Learning objectives

- Check the row-alignment requirements of two representation matrices.
- Distinguish what CCA, linear CKA, and RSA compare.
- Calculate linear CKA and distance RSA on small matrices.
- Explain the limitations of overly strong invariance or small sample sizes.

## Prerequisite check

- Prerequisite lessons: [I06-07 Probe controls and selectivity](I06-07-probe-controls-selectivity.md), [M02-14 Covariance and PCA](../../part-1-foundations/M02/M02-14-covariance-pca.md)
- Check question: If the rows of $X$ and $Y$ place inputs in different orders, what must be done before calculating similarity?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $X\in\mathbb R^{n\times p}$ | `X in R n by p` | First representation of the same $n$ inputs | matrix |
| $Y\in\mathbb R^{n\times q}$ | `Y in R n by q` | Second representation of the same $n$ inputs | matrix |
| CCA | `canonical correlation analysis` | Analysis maximizing correlation between two linear projections | canonical correlations |
| CKA | `centered kernel alignment` | Degree of alignment between centered Gram matrices | $[0,1]$ for linear CKA |
| RSA | `representational similarity analysis` | Analysis comparing similarity or distance structure among input pairs | correlation statistic |
| invariance | `invariance` | Property of a comparison value remaining unchanged after a specified transformation | method property |

## 1. Align the rows first

Row $i$ in $X$ and $Y$ must represent the same input and the same token-selection rule. If token alignment changes with one tokenizer, redefine the comparison unit rather than relying on string positions. Low similarity caused by incorrectly aligned input orders is a join error, not a model difference.

Center each matrix columnwise. If model-specific scaling, whitening, or dimensionality reduction is applied, those choices are also part of the comparison method.

Before comparing, align the rows so that the same inputs occupy corresponding positions.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![X rows A B C and Y rows C A B are matched by input ID with distinct routed paths before geometry comparison.](../../figures/assets/I06/I06-08-input-row-join.svg)

<figcaption>Even with different numbers of coordinate columns, the same input IDs must occupy corresponding rows. A/B/C illustrate the join conceptually; token-selection rules must also define the same comparison unit.</figcaption>
</figure>

## 2. CCA

CCA selects projections $u,v$ to maximize

\[
\operatorname{corr}(Xu,Yv)
\]

and finds subsequent pairs under orthogonality conditions. It allows different numbers of coordinates and examines relationships between linear subspaces. However, when $p,q$ are much larger than $n$, correlations may be overestimated or solutions may be nonunique without regularization and dimensionality reduction.

$u$ is a $p$-dimensional weight vector and $v$ a $q$-dimensional weight vector, while $Xu,Yv$ are columns of scalar scores for the same $n$ inputs. Both scores must have positive variance for the correlation to be defined. The orthogonality condition for subsequent pairs does not mean Euclidean orthogonality of $u,v$ themselves. It requires the new scores to be uncorrelated with previously obtained scores within each representation. With many features, it becomes easier to find projections yielding the same scores in the sample, so a high correlation need not persist on new inputs. [Sample-size and invariance limits of CCA](https://proceedings.mlr.press/v97/kornblith19a.html)

After projection, different coordinate counts still leave two score columns with the same number of inputs.

<figure class="lesson-figure" markdown="1">

![Two representations with n aligned rows but different p and q coordinates are projected by u and v to two length n score columns whose correlation is maximized.](../../figures/assets/I06/I06-08-cca-score-columns.svg)

<figcaption>Although u,v read different coordinate spaces, Xu,Yv are score columns for the same n inputs. Correlation between scores with positive variance is maximized, and subsequent scores are required to be uncorrelated with existing scores.</figcaption>
</figure>

## 3. Linear CKA

For centered $X,Y$, linear CKA can be calculated as

\[
\operatorname{CKA}(X,Y)=
\frac{\lVert X^TY\rVert_F^2}
{\lVert X^TX\rVert_F\lVert Y^TY\rVert_F}
\]

It is invariant to orthogonal transformations and isotropic scaling, but not to every invertible linear transformation. This restriction is a choice to retain differences in representational geometry.

Although $X^TY$ is a $p\times q$ cross-matrix, the same calculation can be written as a comparison of Gram matrices over inputs.

\[
\operatorname{CKA}(X,Y)=
\frac{\langle XX^T,YY^T\rangle_F}
{\lVert XX^T\rVert_F\lVert YY^T\rVert_F}.
\]

Both Gram matrices are $n\times n$, and each entry is the inner product of two centered inputs. The Frobenius inner product multiplies corresponding entries and sums them all, so the formula compares the similarity structure of the same input pairs. CKA is undefined if the denominator is 0.

For a square orthogonal matrix $Q$, $(XQ)(XQ)^T=XQQ^TX^T=XX^T$, leaving the Gram matrix unchanged. Multiplying the entire matrix by a nonzero scalar multiplies the Gram matrix by that scalar squared, which cancels in the normalized ratio. Different multipliers for different coordinates remove this common factor, so the value can change.

Examine corresponding Gram entries separately from the geometry changes the comparison is intended to ignore.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Different coordinate dimensions produce two n by n Gram matrices; one highlighted i j entry in each corresponds to the same input pair.](../../figures/assets/I06/I06-08-cka-gram-pairs.svg)

<figcaption>XXᵀ and YYᵀ contain inner products of the same input pairs, not hidden dimensions. The calculation normalizes the Frobenius alignment of all corresponding entries, including the green entries for pair (i,j).</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An analytic unit circle under orthogonal rotation, uniform scale three, and unequal coordinate scales becomes a rotated circle, larger circle, and ellipse; CKA ignores the first two types but not all unequal scaling.](../../figures/assets/I06/I06-08-invariance-geometry.svg)

<figcaption>This is a mathematical illustration based on a unit circle. Orthogonal rotation preserves the Gram matrix, and isotropic scaling cancels through normalization. Scaling coordinates differently can change geometry, much as it changes a circle into an ellipse. These are not actual model data or CKA measurements.</figcaption>
</figure>

## 4. RSA

RSA constructs a matrix of input-pair distances or dissimilarities within each representation. It unfolds the upper triangle into a vector and calculates the Pearson or Spearman correlation between the two vectors. Specify both the metric and the correlation type.

RSA can compare input-pair structure even when hidden dimensions differ. However, when $n$ is small, the $n(n-1)/2$ pairs share inputs and are not fully independent observations.

The diagonal contains distances from inputs to themselves, and the lower and upper triangles repeat the same pairs, so only one triangle is used. The same index in the two vectors must refer to the same input pair. Pearson compares linear relationships between distance values; Spearman compares relationships between their orderings. Correlation is undefined if either distance vector has zero variation, and even a high correlation does not imply a one-to-one correspondence between individual features.

Check both the pair order when unfolding the triangle and the inputs shared across pairs.

<figure class="lesson-figure" markdown="1">

![A symmetric four-input distance matrix keeps the six strictly upper-triangle pairs and discards diagonal and mirrored lower entries before vectorizing in shared order.](../../figures/assets/I06/I06-08-rsa-upper-triangle.svg)

<figcaption>Exclude the diagonal and duplicated lower triangle, then unfold the upper triangle in the same pair order. The six pairs from four inputs illustrate the structure conceptually; the eight inputs in the text have 28 pairs.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![Distances AB and AC both depend on input A, showing why pair counts are not counts of independent inputs.](../../figures/assets/I06/I06-08-pair-dependence.svg)

<figcaption>AB and AC share A. More pairs do not create that many more independent inputs, so preserve the input unit when evaluating uncertainty.</figcaption>
</figure>

## 5. Which method should you choose?

| Question | Suitable starting point |
|---|---|
| Do linear subspaces correspond? | Regularized CCA or SVCCA |
| Should overall geometry be compared while ignoring orthogonal rotation and isotropic scaling? | Linear CKA |
| Are the orderings of input-pair distances similar? | RSA |

Different results do not establish that one method is wrong. The methods use different invariances and summaries.

## CPU lab

Construct an aligned representation $Y=XQ+$ small noise and an independent random representation. Check whether CKA and distance RSA assign higher similarity to the aligned pair.

<!-- I06_EXAMPLE: i06_08_similarity -->

## Real Pythia model-size comparison

Collect activations from Pythia 410M layer 11 for the same eight prompts used with Pythia 160M in I06-02. The matrices have shapes $8\times768$ and $8\times1024$, respectively, so raw-coordinate subtraction is not performed. Run 410M in inference-only mode and calculate linear CKA and distance RSA against the 160M artifact.

<!-- GPU_EXPERIMENT: pythia_410m_scale_smoke -->

With only eight samples, these results are a pilot checking the runner and comparison contract. They do not support a causal conclusion that model size caused the similarity or generalization to other prompt populations.

## Common misconceptions

### Misconception 1. A similarity of 1 means two models perform the same computation

First state which relationship the selected method summarizes. CCA projection correlations, linear CKA Gram alignment, and RSA distance correlations are different quantities. A value of 1 does not establish identical downstream algorithms or behavior.

### Misconception 2. Every RSA pair is an independent sample

The pairs are dependent because one input appears in multiple pairs. Bootstrapping should also use inputs as the unit.

### Misconception 3. The metric giving the highest value is the best metric

The metric is not the goal. First specify which invariances the question requires.

## Exercises

### 1. Row alignment

The rows of $X$ are ordered by prompt ID, while the rows of $Y$ are ordered by length. Can CKA be calculated immediately?

<details><summary>Show solution</summary>No. Join the matrices so that the same prompt IDs occupy corresponding rows, check for duplicates and missing inputs, and then calculate it.</details>

### 2. Orthogonal transformation

If $Y=XQ$ and $Q^TQ=I$, what is linear CKA in the absence of noise?

<details><summary>Show solution</summary>It is 1. $Q$ preserves Gram geometry, and linear CKA is invariant to orthogonal transformations.</details>

### 3. Scaling

What happens to linear CKA when $Y=3X$?

<details><summary>Show solution</summary>It is 1. Scaling cancels between the numerator and denominator, giving invariance to isotropic scaling.</details>

### 4. Number of RSA pairs

How many distinct pairs are in the upper triangle for eight inputs?

<details><summary>Show solution</summary>There are $8\times7/2=28$ pairs. These 28 pairs share inputs, however, and should not be treated as 28 independent samples.</details>

### 5. Dimension

Why can RSA be applied to 768-dimensional and 1,024-dimensional representations?

<details><summary>Show solution</summary>It calculates scalar distances for the same input pairs within each space, then compares their distance structure. Raw-coordinate correspondence is unnecessary.</details>

### 6. Scope of the claim

CKA between 160M and 410M was high. Can the result be described as `they learned the same features`?

<details><summary>Show solution</summary>Not as stated. It is evidence that the specified geometry was similar on the fixed sample. Correspondence between individual features and their functional roles requires further analysis.</details>

## Sources and update boundaries

The CKA definition and choice of invariances follow [Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html). [Williams 2024](https://proceedings.mlr.press/v285/williams24a.html) was consulted for subsequent accounts of the relationships among CKA, RSA, and CCA. Centering and the choice of an unbiased estimator may differ across library implementations, so record the formula used.

## Lesson summary

- Align rows in the two matrices by the same inputs and measurement units.
- CCA compares linear subspaces, CKA compares centered geometry, and RSA compares pairwise structure.
- Each method permits different invariances.
- High similarity on a small sample is not evidence of identical computations or generalization.

## Pass criteria

- Can you distinguish what CCA, CKA, and RSA compare?
- Can you check the input shapes for linear CKA and RSA?
- Can you select invariances that fit the question and state the limitations?

## Next lesson

- [I06-09 Feature visualization](I06-09-feature-visualization.md)

## Author checklist

- [x] Representation-comparison methods are connected to their invariances.
- [x] The sample-size limitations of the 160M–410M comparison are specified.
- [x] Every exercise has a solution.
- [x] The strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and mathematical rendering have been checked.
