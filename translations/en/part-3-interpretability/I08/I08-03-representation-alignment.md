---
id: "I08-03"
title: "Representation alignment"
part: 3
stage: "I08"
status: "complete"
prerequisites: ["I08-02", "I06-08", "M02-13"]
estimated_time: "90–120 minutes"
---

# I08-03. Representation alignment

## Why this lesson matters

Even two representations containing the same information can fail a coordinate-wise comparison when their axes are rotated or their units permuted. To track checkpoint features over time, decide which transformations count as the same representation, pair rows for the same inputs, and then align them.

## Learning objectives

- Distinguish row correspondence from feature-axis alignment.
- Explain the orthogonal Procrustes objective.
- Compute and interpret errors before and after alignment and CKA.
- Explain why alignment does not prove feature identity.

## Prerequisite check

- Prerequisite lessons: [I08-02 Parameter distance and function distance](I08-02-parameter-function-distance.md), [I06-08 CCA, CKA, and RSA](../I06/I06-08-cca-cka-rsa.md), [M02-13 Singular value decomposition](../../part-1-foundations/M02/M02-13-singular-value-decomposition.md)
- Check question: Why does an orthogonal matrix preserve vector lengths and inner products?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $X_t$ | `X sub t` | Centered activations at checkpoint $t$ | $n\times d$ |
| $Q^\star$ | `Q star` | Optimal orthogonal alignment | $d\times d$ |
| $\|X_s-X_tQ\|_F$ | `the Frobenius norm of X sub s minus X sub t Q` | Coordinate error after alignment | scalar |
| Procrustes | `Procrustes` | Problem of matching two matrices through rotation and reflection | optimization problem |
| correspondence | `correspondence` | Condition that the same row of each matrix represents the same input | one-to-one pairing |

## 1. Input correspondence comes first

The $i$th rows of $X_s$ and $X_t$ must represent the same prompt and token location. If row orders differ, even a good feature-axis alignment matches the wrong samples. Define correspondence rules first when tokens are missing or tokenizers differ.

Centered activations in the table mean that each column's sample mean has been subtracted at each checkpoint. Alignment therefore compares relative arrangements among inputs, while mean activation shifts across checkpoints are measured separately. Right multiplication by $Q$ applies the same feature-axis transformation to every row. It does not replace the operation of reordering different input rows.

Distinguish the order of the two alignment operations using sample IDs and feature axes.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Sample rows A B C reorder by input identity before one common orthogonal feature map applies to all rows](../../figures/assets/I08/I08-03-row-feature-axes.svg)

<figcaption>First pair rows for the same prompts and tokens, then apply the same Q to every row. Q changes feature axes; it does not correct the wrong order of sample rows.</figcaption>
</figure>

Subtracting column means removes a common translation as in the following example.

<figure class="lesson-figure" markdown="1">

![Subtracting one column-mean vector translates every row of an analytic triangle while preserving relative positions](../../figures/assets/I08/I08-03-centering-removes-mean.svg)

<figcaption>In the explicit three-row example, subtract the column mean (3,2) from every row. Purple shows the mean shift, while the two triangles have the same relative arrangement. Mean shifts across checkpoints must be measured separately from centered alignment.</figcaption>
</figure>

## 2. Orthogonal Procrustes

When the two representations have the same dimension, solve

$$
Q^\star=\arg\min_{Q^\top Q=I}\|X_s-X_tQ\|_F
$$

Because $Q$ is a square orthogonal matrix, $X_tQ$ preserves each row's length. Expanding the squared objective gives

$$
\|X_s-X_tQ\|_F^2
=\|X_s\|_F^2+\|X_t\|_F^2
-2\operatorname{tr}(Q^\top X_t^\top X_s).
$$

The first two terms do not depend on $Q$. Minimizing the error is therefore equivalent to maximizing the final trace. Insert the full SVD $X_t^\top X_s=U\Sigma V^\top$ and use the cyclic property of the trace; the quantity to maximize becomes $\operatorname{tr}(V^\top Q^\top U\Sigma)$. Because $V^\top Q^\top U$ is also orthogonal, each diagonal entry is at most 1, and the diagonal entries of $\Sigma$ are nonnegative. The trace cannot exceed the sum of singular values. This bound is attained when $V^\top Q^\top U=I$, so one solution is

$$
Q^\star=UV^\top
$$

The orthogonal constraint preserves lengths and angles. It removes less structure than an alignment that allows general invertible transformations.

This condition allows both rotations and reflections. Directions with zero singular values contribute nothing to the trace, so the optimal alignment may not be unique. Distinguish a small alignment error from the claim that a unique coordinate correspondence has been determined.

The next three coordinate systems compare rotation and alignment of the same input rows.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Analytic input rows A B C rotate together and a common Procrustes map returns them to their reference coordinates](../../figures/assets/I08/I08-03-orthogonal-alignment.svg)

<figcaption>This mathematical example rotates the same rows A, B, and C, then aligns them again with one orthogonal Q. Compare the operation that reduces coordinate error while preserving lengths and angles. These are not measured model values.</figcaption>
</figure>

Follow the shapes in the exercise from the cross matrix to Q.

<figure class="lesson-figure" markdown="1">

![Two one-hundred by sixty-four representations form a sixty-four by sixty-four cross matrix whose full SVD gives the square orthogonal alignment](../../figures/assets/I08/I08-03-procrustes-shapes.svg)

<figcaption>For the exercise's 100×64 representations, the cross matrix, U, Σ, and Vᵀ from its full SVD, and the final Q are all 64×64. Q matches the feature dimension, not the input row count.</figcaption>
</figure>

Consider an example in which two alignments give the same error along directions without data.

<figure class="lesson-figure" markdown="1">

![Identity and reflection fit three data rows on the first axis equally but send an unobserved second-axis direction oppositely](../../figures/assets/I08/I08-03-unobserved-axis-freedom.svg)

<figcaption>In this explicit 2-dimensional example, data lie only on the first axis. Both the identity and reflection of the second axis fit the data exactly, but their correspondences for directions absent from the data differ. This shows nonuniqueness along zero-singular-value directions.</figcaption>
</figure>

## 3. Use metrics that do not require alignment alongside it

Linear CKA is invariant to isotropic scaling and orthogonal transformations. Procrustes error is useful for constructing an actual coordinate correspondence, whereas CKA summarizes representation relationships as a scalar. The two metrics do not answer the same question.

Doubling every coordinate of the same nonzero representation leaves linear CKA unchanged. However, orthogonal $Q$ cannot reduce lengths, so the scale difference remains in the Procrustes error. A single CKA value does not provide an actual alignment matrix either. Choose a metric by distinguishing which transformations should count as equivalent and whether coordinate correspondence is needed.

Training a separate probe at each checkpoint mixes in the probe's own rotation and overfitting. Record transfer of a fixed probe, recoverability with a retrained probe, and alignment metrics separately.

Even the same two representations give different results depending on the metric.

<figure class="lesson-figure" markdown="1">

![Doubling a centered analytic triangle preserves linear CKA one but leaves a positive minimum orthogonal alignment error](../../figures/assets/I08/I08-03-cka-versus-scale-error.svg)

<figcaption>For the centered example X and 2X, linear CKA is 1. An orthogonal transformation cannot halve lengths, so a minimum Frobenius error of 2 remains. The two numbers answer different questions.</figcaption>
</figure>

Compare a fixed probe with a newly trained probe along the following paths.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A probe fit at checkpoint s transfers unchanged to checkpoint t while an independently refit probe measures recoverability instead](../../figures/assets/I08/I08-03-probe-transfer-contract.svg)

<figcaption>Distinguish the score obtained by holding the previously trained W_s fixed and transferring it to the next checkpoint from the recovery score obtained by training a new W_t. Preserve input correspondence and split conditions for evaluation along either path.</figcaption>
</figure>

## 4. CPU exercise

<!-- I08_EXAMPLE: i08_03_representation_alignment -->

Rotate a random representation with an orthogonal matrix. Raw RMSE is large, but RMSE after Procrustes alignment is at numerical-error level, and linear CKA is close to 1.

## Common misconceptions

### Misconception 1. Alignment establishes the same features

Matching the overall sample geometry does not establish that individual features have the same meaning or usage paths. Feature-level correspondence needs additional activation examples and intervention evidence.

### Misconception 2. The most flexible alignment is the fairest

A transformation with many degrees of freedom can erase actual differences. Choose only the invariances allowed by the research question.

## Exercises

### 1. Shape

If $X_s,X_t\in\mathbb R^{100\times64}$, what is the shape of $Q$?

<details><summary>Show solution</summary>

$X_tQ$ must be $100\times64$, so $Q\in\mathbb R^{64\times64}$.

</details>

### 2. Row correspondence

Only the prompt order differs between two checkpoints. What should be done first?

<details><summary>Show solution</summary>

Reorder the rows to pair identical prompts and tokens. Feature alignment comes next.

</details>

### 3. Orthogonal condition

List two quantities preserved by $Q^\top Q=I$.

<details><summary>Show solution</summary>

It preserves a vector's L2 norm and the inner product of two vectors. It therefore also preserves angles and Euclidean distances.

</details>

### 4. CKA

If $Y=XQ$ with orthogonal $Q$, why is high linear CKA expected?

<details><summary>Show solution</summary>

An orthogonal transformation preserves sample Gram geometry, so relationships in the centered representations do not change.

</details>

### 5. Overly flexible alignment

Explain a problem that can arise when arbitrary invertible transformations are allowed.

<details><summary>Show solution</summary>

They can absorb scaling and shear, removing meaningful geometry differences between checkpoints.

</details>

### 6. Design a claim

What evidence beyond alignment is needed to claim that “a feature was preserved”?

<details><summary>Show solution</summary>

Check activation patterns on independent data, matching stability, probe transfer, and intervention effects on the relevant direction together.

</details>

## Sources and boundaries for updates

Invariances in representation comparison and CKA follow [Kornblith et al. (2019)](https://proceedings.mlr.press/v97/kornblith19a.html). This lesson focuses on same-dimensional orthogonal alignment and does not cover general alignment across different dimensions.

## Lesson summary

- Pair rows for the same inputs first.
- Procrustes minimizes coordinate error under orthogonal transformations.
- Alignment error and CKA answer different questions.
- Successful alignment alone does not establish persistence of feature meaning or function.

## Pass criteria

- Can you write the Procrustes objective and shapes?
- Can you distinguish row alignment from feature-axis alignment?
- Can you explain why the allowed invariances change the results?

## Next lesson

- [I08-04 SGD as dynamics](I08-04-sgd-as-dynamics.md)

## Author checklist

- [x] The objects being aligned and the invariances are specified.
- [x] The SVD solution and CKA are connected.
- [x] Every exercise has a solution.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Claim strength and spoken readings have been checked.
- [x] Internal links and equations have been checked.
