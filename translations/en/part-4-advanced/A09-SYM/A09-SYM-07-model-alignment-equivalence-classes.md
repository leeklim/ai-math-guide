---
id: "A09-SYM-07"
title: "Model alignment and equivalence classes"
part: 4
stage: "A09-SYM"
status: "complete"
prerequisites: ["A09-SYM-02", "A09-SYM-04", "A09-SYM-05", "I08-03"]
estimated_time: "90–120 minutes"
---

# A09-SYM-07. Model alignment and equivalence classes

## Why this lesson matters

Directly comparing neurons, subspaces, or weights of models with different seeds can mistake symmetry-induced coordinate differences for differences in learning outcomes. Alignment finds correspondences within an allowed transformation class, while the quotient perspective reveals uncertainty remaining after alignment.

## Learning objectives

- Specify the alignment objective and transformation class.
- Distinguish permutation, orthogonal, and general linear alignment.
- Separate alignment fitting from held-out evaluation.
- State the conditions needed to interpret residual mismatch as a functional difference.

## Prerequisite check

- Prerequisite lessons: [A09-SYM-02 Orbits and stabilizers](A09-SYM-02-orbits-stabilizers.md), [A09-SYM-04 Permutation symmetry](A09-SYM-04-permutation-symmetry.md), [A09-SYM-05 Gauge freedom](A09-SYM-05-scaling-rotation-gauge.md), [I08-03 Representation alignment](../../part-3-interpretability/I08/I08-03-representation-alignment.md)
- Check question: Why is training alignment error easier to reduce when the transformation class is expanded?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $X,Y$ | `X and Y` | Paired activation matrices | $n\times d$ |
| $\mathcal G$ | `the transformation class G` | Allowed alignment set | Set of maps |
| $\hat g=\arg\min_{g\in\mathcal G}\|Xg-Y\|_F$ | `g hat minimizes the Frobenius norm of X g minus Y over g in G` | Fitted alignment | Map |
| $d_{\mathcal G}(X,Y)$ | `the G aligned distance between X and Y` | Minimum alignment residual under the chosen norm | Nonnegative scalar |
| $X_{\mathrm{test}},Y_{\mathrm{test}}$ | `X sub test and Y sub test` | Paired activations not used for fitting | $n_{\mathrm{test}}\times d$ |

## Core concepts

### What is treated as equivalent?

Alignment specifies the objects, sample correspondence, centering and scaling, and transformation class together. Here $X,Y\in\mathbb R^{n\times d}$ are activation matrices whose corresponding rows come from the same input and position. A $d\times d$ matrix $g$ multiplying on the right applies the same feature-coordinate transformation to every row. Distinguish choosing row correspondences from aligning feature axes.

A permutation changes only coordinate identities, an orthogonal map preserves inner products, and a general invertible map removes more geometry from the comparison. A permutation moves each column's observations to another column position. Orthogonal alignment can mix columns while preserving each sample's Euclidean length, angles, and distances between samples. General invertible alignment can also absorb scale and shear. Choose the class according to whether the question concerns the coordinates containing the same information or also requires the original sample geometry to agree.

While maintaining paired-row correspondence, inspect what each allowed feature transformation changes below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three paired activation rows each undergo the same feature-column swap while the sample row identities remain fixed.](../../figures/assets/A09-SYM/A09-SYM-07-paired-rows-common-map.svg)

<figcaption>Corresponding rows of X and Y refer to the same input and position. The same right-side g=P swaps both feature components in every row to give Xg=Y without changing the rows themselves. Choosing sample correspondence and aligning feature coordinates are separate tasks.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three panels apply a feature permutation, an orthogonal rotation and an invertible shear to the same two sample points and compare preserved geometry.](../../figures/assets/A09-SYM/A09-SYM-07-transformation-geometries.svg)

<figcaption>A permutation, orthogonal rotation, and invertible shear act on the same two row vectors by right multiplication. The first two preserve lengths and distances between samples, but shear changes the triangle's geometry. Circle and square markers distinguish sample correspondences; reordering coordinates and mixing coordinates are also different operations.</figcaption>

</figure>

### The objective and allowed set

$$
d_{\mathcal G}(X,Y)=\min_{g\in\mathcal G}\|Xg-Y\|_F
$$

This is the minimum residual obtained by transforming $X$ within the allowed class and comparing it with $Y$. A minimum exists for the permutation set and the square orthogonal set. For the general invertible set, there may be only an infimum with no $\hat g$ attaining it. In that case, do not report an argmin or an obtained optimum. If the actual algorithm finds only a candidate, record that candidate's residual.

For example, with scalar $X=1$ and $Y=0$, allowing $g$ to be any nonzero scalar gives residual $|g|$. Taking $g$ arbitrarily close to 0 makes the error arbitrarily small, but 0 itself is not invertible, so no optimal candidate exists. This is why a small residual and attainment of a minimum must be distinguished.

The permutation set is contained in the orthogonal set, which is contained in the invertible set. With the same data, preprocessing, and norm, expanding the allowed set cannot increase the minimum or infimum. This follows from having more candidates; it is not independent evidence that the two models have become more similar. Interpreting this residual as a representative-independent quotient metric when non-isometric transformations are allowed also requires checking the conditions in [A09-SYM-02](A09-SYM-02-orbits-stabilizers.md).

Check the inclusion relations among allowed sets separately from actual attainment of a minimum.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Nested permutation, orthogonal and invertible sets show decreasing minimum residuals for X identity and target two times a forty-five-degree rotation.](../../figures/assets/A09-SYM/A09-SYM-07-nested-feasible-sets.svg)

<figcaption>With the same X=I₂ and Y=2R₄₅ held fixed, the permutation minimum residual is √(10−4√2)≈2.084, the orthogonal minimum is √2≈1.414, and the invertible minimum is 0. More allowed candidates lower the optimum; this is not separate evidence that the two models have become more similar.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Residual absolute g approaches zero but an open point at g zero is excluded from the invertible scalar transformation class.](../../figures/assets/A09-SYM/A09-SYM-07-unattained-infimum.svg)

<figcaption>For X=1 and Y=0, the residual is |g| and allowed candidates satisfy g≠0. Sending g toward 0 approaches infimum 0, but the open point g=0 is excluded, so no argmin attains it. A small candidate residual differs from attainment of a minimum.</figcaption>

</figure>

### Freeze the fitted transformation for held-out evaluation

Fitting and evaluating $g$ on the same samples risks overfitting, so measure residuals and task-relevant behavior on held-out inputs. After choosing $\hat g$ on the fit split, apply the same transformation to separate inputs and measure $\|X_{\mathrm{test}}\hat g-Y_{\mathrm{test}}\|_F$. Finding a new $g$ on the test split does not test whether the fitted correspondence transfers to new inputs.

Centering and scaling are also part of the comparison. Fixing means and scales estimated on the fit split and applying them to test data evaluates transfer of that preprocessing and transformation. To recenter each split and compare only relative geometry, state this different measurement rule and examine mean shifts separately. When comparing residuals with different row counts, match normalization conventions, accounting for the fact that the squared Frobenius norm sums squared errors over observed entries.

The flow below freezes settings learned on the fit split for use on the test split.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Fit-paired activations estimate means, scales and alignment once; frozen settings transfer to held-out paired activations for evaluation without refitting.](../../figures/assets/A09-SYM/A09-SYM-07-fit-freeze-evaluate.svg)

<figcaption>Means, scales, and ĝ chosen on the fit split are frozen and applied to held-out paired activations. Refitting ĝ or preprocessing on the test split does not measure transfer of the existing correspondence. With different numbers of observed entries, also specify the normalization convention for the Frobenius residual.</figcaption>

</figure>

### Interpreting remaining differences and non-uniqueness

Stabilizers or unobserved directions can make optimal alignment non-unique. Identical columns of $X$ can be swapped without changing it, and null directions of $X$ may provide no observations distinguishing transformations. In such cases, report the observed subspace and uncertainty among possible correspondences rather than feature-by-feature identity.

In orthogonal Procrustes, zero singular values of the cross matrix $X^\top Y$ can leave freedom in the optimum. Non-uniqueness of SVD bases due to repeated positive singular values does not by itself imply non-uniqueness of the alignment matrix. In the full-SVD solution $UV^\top$ from [I08-03](../../part-3-interpretability/I08/I08-03-representation-alignment.md), jointly rotating both bases within the same repeated block leaves their product unchanged. When the cross matrix is nonsingular, the square orthogonal optimum is unique. With small singular values, distinguish estimation sensitivity from exact non-uniqueness.

A large residual means that the allowed class did not align the current activation observations well. Additional checks are needed to distinguish preprocessing differences, noise, optimization failure, and actual representational differences. Conversely, even a small residual does not prove equivalence of the entire model function without examining the next layer's readout. Compare held-out outputs, losses, and intervention effects using prespecified criteria to narrow the subject of the claim.

Non-uniqueness of alignment, non-uniqueness of SVD bases, and differences between functions are not the same problem.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Identity and a sign flip in an unobserved y direction align the same x-axis data equally, yet disagree on a y-axis probe.](../../figures/assets/A09-SYM/A09-SYM-07-unobserved-direction-freedom.svg)

<figcaption>If the only observed rows of X=Y are (1,0) and (2,0), both I and diag(1,−1) give residual 0. They give opposite results in the unobserved direction (0,1). The probe in the figure is a mathematical example illustrating this freedom, not a new model observation.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Identity and jointly rotated singular-vector bases both reconstruct cross matrix two identity and give the same alignment map identity.](../../figures/assets/A09-SYM/A09-SYM-07-paired-svd-basis-cancellation.svg)

<figcaption>An SVD of M=2I₂ can use either U=V=I or U′=V′=R₉₀. Jointly changing both bases gives U′V′ᵀ=R₉₀R₉₀ᵀ=I, the same alignment matrix. Basis freedom for repeated positive singular values differs from optimum freedom for zero singular values.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Activations related by an exact column swap have zero aligned residual, but unchanged first-coordinate readouts give functions x and two x.](../../figures/assets/A09-SYM/A09-SYM-07-zero-alignment-different-output.svg)

<figcaption>For X(x)=(x,2x) and Y(x)=(2x,x), X(x)P=Y(x), so the aligned residual is 0. But if both models read out the first coordinate, their outputs are x and 2x. Claiming preservation of the entire function also requires compensation in the next layer or separate functional validation.</figcaption>

</figure>

## Small example

With an exact column permutation $Y=XP$, raw $\|X-Y\|_F$ can be large, but the permutation-aligned distance is 0.

Since $g=P$ is an allowed candidate, $Xg-Y=0$. This establishes exact correspondence of activations on the observed inputs. Without a condition matching the two models' output weights to this order, the equation alone does not establish preservation of the entire function.

## Common misconceptions

- Alignment error 0 alone does not imply equality of the two models' entire functions.
- The most flexible alignment is not necessarily the best scientific comparison.

## Exercises

### 1. Choosing a class
If the question concerns coordinate-wise feature identity, why might permutation alignment be more appropriate than orthogonal alignment?
<details><summary>Show solution</summary>

A rotation can mix multiple coordinates and remove differences in feature identity, whereas a permutation preserves coordinate contents and changes only their order.
</details>

### 2. Held-out evaluation
Why separate alignment fitting and evaluation splits?
<details><summary>Show solution</summary>

It prevents mistaking the training error of a transformation fitted even to sample-specific noise for representation equivalence.
</details>

### 3. Non-uniqueness
What should be reported if several rotations within an isotropic subspace give the same objective?
<details><summary>Show solution</summary>

Report the subspace, principal angles, and uncertainty in alignment solutions rather than individual axes.
</details>

### 4. Functional validation
What behavioral checks should follow a small aligned distance?
<details><summary>Show solution</summary>

Compare prespecified function metrics, such as output distributions, loss, and intervention effects, on held-out inputs.
</details>

## Evidence and update boundaries

Procrustes alignment and quotient distances follow standard constructions in linear algebra and shape analysis. Nonlinear alignment changes interpretability and identifiability substantially and is excluded from this lesson.

- [Higham, What Is the Polar Decomposition?](https://nhigham.com/2020/07/28/what-is-the-polar-decomposition/): Provides the Procrustes solution and its uniqueness when the cross matrix is nonsingular. Distinguish singular-vector basis freedom for repeated singular values from freedom in the optimal matrix.
- [Kornblith et al., Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html): Research evidence that allowed invariance changes the question in representation comparison. This lesson's residual is not immediately interpreted as CKA or equivalence of the entire function.

## Lesson summary

- Specify the allowed transformation class before alignment.
- A broader class removes more structure from the comparison.
- Fit the transformation on training samples and evaluate it on held-out samples.
- With non-unique alignment, report subspace equivalence rather than feature equivalence.

## Pass criteria

- Can you choose an alignment class appropriate to the question?
- Can you distinguish aligned similarity from function equivalence?

## Next lesson

- [A09-SYM-08 Capstone exercise: representation alignment across seeds](A09-SYM-08-capstone-seed-alignment.md)

## Author checklist

- [x] Alignment classes, splits, and non-uniqueness are covered.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
