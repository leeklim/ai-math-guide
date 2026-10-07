---
id: "A09-RMT-05"
title: "Spiked covariance model"
part: 4
stage: "A09-RMT"
status: "complete"
prerequisites: ["M02-11", "M04-04", "A09-RMT-04"]
estimated_time: "90–120 minutes"
---

# A09-RMT-05. Spiked covariance model

## Why this lesson matters

Adding a low-rank signal to isotropic noise does not ensure that sample PCA recovers the signal direction. Spectral separation has a threshold determined by signal strength and aspect ratio. The spiked covariance model separates detection of a large eigenvalue from recovery of its eigenvector.

## Learning objectives

- Calculate the population eigenvalues of a rank-one spiked covariance.
- Relate the spectral separation threshold to the aspect ratio.
- Distinguish an outlier eigenvalue from eigenvector alignment.
- Limit claims about weak components in activation PCA.

## Prerequisite check

- Prerequisite lessons: [M02-11 Eigenvalues and eigenvectors](../../part-1-foundations/M02/M02-11-eigenvalues-eigenvectors.md), [M04-04 Expectation, variance, and covariance](../../part-1-foundations/M04/M04-04-expectation-variance-covariance.md), [A09-RMT-04 Intuition for the Marchenko–Pastur law](A09-RMT-04-marchenko-pastur-intuition.md)
- Check question: For a unit vector $u$, in which direction does $uu^\top$ have eigenvalue 1?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $\Sigma=I+\beta uu^\top$ | `Sigma equals I plus beta u u transpose` | Rank-one spiked population covariance | $d\times d$ |
| $\lambda_{\mathrm{pop}}=1+\beta$ | `the population spike equals one plus beta` | Population eigenvalue in the signal direction | Scalar greater than 1 |
| $\beta>\sqrt\gamma$ | `beta is greater than square root gamma` | Unit-noise spectral separation condition | Asymptotic condition |
| $\lvert\hat u^\top u\rvert^2$ | `the squared alignment between u hat and u` | Alignment of sample and population directions | Number in $[0,1]$ |

## Core concepts

### The rank-one term and population spectrum

For a unit vector $u$ and signal strength $\beta>0$, consider

$$
\Sigma=I+\beta uu^\top
$$

Since $uu^\top v=u(u^\top v)$, the operator $uu^\top$ retains only the component parallel to $u$. We have $\Sigma u=(1+\beta)u$, and if $u^\top v=0$, then $\Sigma v=v$. The population spectrum therefore consists of one eigenvalue $1+\beta$ and $d-1$ eigenvalues equal to 1. The term with rank 1 is the added term $\beta uu^\top$, not the full covariance. The matrix $\Sigma$ is full rank, with positive variance in every direction.

Using mean-zero Gaussian noise $g\sim\mathcal N(0,I_d)$ and an independent scalar $a\sim\mathcal N(0,1)$, we can write $x=g+\sqrt\beta\,a u$. Because $a$ varies across samples, the signal is extra variance in one direction, not a common mean. Independence makes the cross-covariance 0, and the covariance of the added term is $\beta uu^\top$. This lesson uses the Gaussian rank-one model with iid samples and $S=X^\top X/n$ as its reference case.

Compare the action of the added covariance term, the full spectrum, and the increase in variance without a change in mean, in that order.

<figure class="lesson-figure" markdown="1">

![In a coordinate example with beta two and signal direction e one the covariance maps one one to three one while the rank one additional term maps it to two zero.](../../figures/assets/A09-RMT/A09-RMT-05-rank-one-covariance-action.svg)

<figcaption>For the existing rank-one condition β=2, take u=e₁ and v=(1,1)ᵀ for illustration. The added term βuuᵀv=(2,0)ᵀ lies only in the first direction, whereas the full Σv=(3,1)ᵀ retains the second component. Distinguish the added term's rank 1 from the full rank of the covariance.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![The original five dimensional beta two exercise has one population eigenvalue three and four population eigenvalues one.](../../figures/assets/A09-RMT/A09-RMT-05-one-spike-full-population-spectrum.svg)

<figcaption>In the existing exercise with d=5 and β=2, the population eigenvalues are one 3 and four 1s. All values are positive, so the full covariance is full rank. The term rank-one applies only to the added term.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Three exact zero centered Gaussian densities compare noise variance one independent signal variance two and their sum variance three.](../../figures/assets/A09-RMT/A09-RMT-05-zero-mean-extra-variance.svg)

<figcaption>These exact densities compare Gaussian noise in direction u, the independent term √2a, and their sum. For β=2, all three means are 0, and the variances are 1,2,3. The signal is added variance rather than a common mean shift; other directions do not receive this added term.</figcaption>

</figure>

### The population threshold and sample bulk edge

When dimension and sample size grow together with $d/n\to\gamma>0$ and $\beta$ fixed, the unit-noise rank-one model produces a sample outlier separated from the MP bulk if $\beta>\sqrt\gamma$. In terms of the population spike, this condition is $\ell=1+\beta>1+\sqrt\gamma$. Do not replace it with a direct comparison against the sample upper edge $(1+\sqrt\gamma)^2$. One is a condition on a population eigenvalue; the other is a reference for comparing sample eigenvalues.

Above the threshold, the sample outlier corresponding to the population spike $\ell=1+\beta$ approaches

$$
\hat\lambda
\to
\ell\left(1+\frac{\gamma}{\ell-1}\right)
$$

asymptotically. Apply this outlier formula only when $\beta>\sqrt\gamma$. The factor multiplying $\ell$ is greater than 1, so even a separated sample eigenvalue is not an exact estimate of the population eigenvalue. Substituting $\beta=\sqrt\gamma$ gives $(1+\sqrt\gamma)^2$, where the two branches meet at the edge.

For $0<\beta\le\sqrt\gamma$, the largest sample eigenvalue stays at the bulk edge. Extrapolating the outlier formula into this branch gives an incorrect prediction. In a finite sample, the transition need not appear as a sharp decision boundary, and this threshold does not itself provide a one-run p-value. At the same dimension, collecting more samples reduces $\gamma$, which can make weaker spikes easier to distinguish.

First plot the population and sample branches separately, then examine how increasing sample size lowers the threshold.

<figure class="lesson-figure" markdown="1">

![For aspect ratio one quarter the population spike increases as one plus beta while the leading sample limit sticks to two point two five until beta exceeds one half and then follows only its valid outlier branch.](../../figures/assets/A09-RMT/A09-RMT-05-population-spike-and-sample-branch.svg)

<figcaption>For γ=0.25, the population ℓ=1+β and the leading sample limit are shown separately. The sample branch stays at edge 2.25 for β≤0.5, and the outlier formula is used only for β&gt;0.5. At the existing β=1, population value 2 lies below the edge, but sample value 2.5 lies outside it. The lower branch does not prove β=0.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![A beta versus gamma diagram separates the region above square root gamma from the attached bulk region and marks thresholds one half and one quarter for aspect ratios one quarter and one sixteenth.](../../figures/assets/A09-RMT/A09-RMT-05-aspect-ratio-separation-region.svg)

<figcaption>The regions above and below the unit-noise asymptotic condition β&gt;√γ are separated. At fixed d, increasing n fourfold reduces γ from 0.25 to 0.0625 and the threshold from 0.5 to 0.25. The boundary is not a one-run p-value or a definitive finite-sample decision line.</figcaption>

</figure>

### Eigenvalue separation and direction recovery

Write the sample's leading unit eigenvector as $\hat u$. Then $\lvert\hat u^\top u\rvert^2$ is the squared cosine between the two directions. It is unchanged by a sign reversal, removing the eigenvector's sign ambiguity. A value of 1 means the same one-dimensional subspace; 0 means orthogonal directions. The outlier's magnitude alone cannot determine this value. In a synthetic model with known $u$, compare the two measurements separately.

In the Gaussian model with $0<\gamma<1$, the squared alignment above the threshold approaches

$$
\lvert\hat u^\top u\rvert^2\to
\frac{1-\gamma/\beta^2}{1+\gamma/\beta}
$$

Below the threshold and at the boundary, it approaches 0. Even on the upper branch, the value is less than 1 for fixed finite $\beta$ and positive $\gamma$. Obtaining nonzero alignment is therefore different from recovering the original direction without error. This lesson does not require a proof of the formula or alignment formulas for other noise models.

Read the outlier gap and direction alignment on separate axes, and remove eigenvector sign ambiguity by squaring.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Separate panels compare the limiting gap beyond the MP edge with squared eigenvector alignment in the Gaussian aspect quarter model with gap one quarter and alignment zero point six at beta one.](../../figures/assets/A09-RMT/A09-RMT-05-spectral-gap-versus-alignment.svg)

<figcaption>In the Gaussian model with γ=0.25, the outlier's gap above the edge and its squared alignment are shown on different y-axes. At the existing β=1, gap 0.25 and alignment 0.6 are different measurements. Nonzero alignment above the threshold is still not perfect recovery at 1. This alignment formula is restricted to the text's condition 0&lt;γ&lt;1.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![A deterministic unit direction with squared first coordinate zero point six and its sign reversal have identical squared alignment to e one.](../../figures/assets/A09-RMT/A09-RMT-05-alignment-sign-invariance.svg)

<figcaption>For illustration, the figure shows u=e₁, û=(√0.6,√0.4)ᵀ, and −û. The inner products have opposite signs, but both squares are 0.6. This coordinate example illustrates sign invariance; it is not a result from generating actual sample eigenvectors.</figcaption>

</figure>

### What can be said about a weak component?

This model is a reference case for detecting a low-rank signal. If actual activation noise is anisotropic or several spikes are close together, analyze the signal subspace and a matched null rather than comparing individual eigenvectors.

Observing no outlier means this spectral method did not separate a spike; it does not prove $\beta=0$. Conversely, a variance spike's signal means only the added covariance structure in this model, not a feature needed for labels or model behavior. When eigenvalues are close, individual vectors can rotate across splits while their combined subspace remains stable. Distinguish comparing a sign-aligned single vector from comparing a subspace.

As the following figure shows, observing a change in vectors need not mean that the subspace they jointly span has changed.

<figure class="lesson-figure" markdown="1">

![Two orthonormal bases rotated thirty degrees span the same z zero plane inside three dimensional space even though corresponding vector squared overlaps are three quarters.](../../figures/assets/A09-RMT/A09-RMT-05-same-plane-rotated-bases.svg)

<figcaption>For illustration, two orthonormal bases are rotated by 30° within the z=0 plane in R³. The squared overlap of corresponding vectors is 3/4, but the plane spanned by the bases is the same. This shows why individual directions and subspaces should be compared separately when vectors differ across splits; it is not a measurement of actual split stability.</figcaption>

</figure>

## Small example

For $\gamma=0.25$, the threshold is $\beta>0.5$. With $\beta=1$, we have $\ell=2$, and the predicted sample outlier is $2(1+0.25)=2.5$. It is above the MP upper edge of 2.25.

Here, population spike 2 is below sample edge 2.25, but sample outlier 2.5 is outside the edge. Directly testing the population value against the sample edge would miss this case. Under the same conditions, the limiting squared alignment is $(1-0.25)/(1+0.25)=0.6$, so observing an outlier does not mean perfect direction recovery.

## Common misconceptions

- A population spike greater than 1 does not by itself ensure stable recovery of the sample eigenvector.
- Even an outlier above the threshold does not automatically establish task relevance or causal use.

## Exercises

### 1. Population spectrum
For $d=5$ and $\beta=2$, give the eigenvalues of $\Sigma=I+2uu^\top$.
<details><summary>Show solution</summary>

There is one eigenvalue of 3 in direction $u$ and four eigenvalues of 1 in orthogonal directions.
</details>

### 2. Threshold
For $\gamma=0.36$, what condition on $\beta$ gives spectral separation?
<details><summary>Show solution</summary>

Since $\sqrt{0.36}=0.6$, the condition in the asymptotic unit-noise model is $\beta>0.6$.
</details>

### 3. Outlier location
Find the predicted sample outlier location for $\gamma=0.5$ and $\beta=1$.
<details><summary>Show solution</summary>

With $\ell=2$, it is $2(1+0.5/1)=3$.
</details>

### 4. Model interpretation
PCA direction 1 aligns with a label in one data split but changes substantially in another. How would you report this?
<details><summary>Show solution</summary>

Because the sample eigenvector's stability has not been established, do not call it a reproducible signal direction. Report subspace overlap, the eigenvalue gap, and predictions for each split together.
</details>

## Evidence and update boundaries

The threshold and outlier formula use unit isotropic noise, a rank-one spike, and standard high-dimensional asymptotics. Finite-size p-values and spikes in general covariances are outside this lesson's scope.

The Gaussian spike assumptions, population/sample thresholds, and alignment for $0<\gamma<1$ follow §2.1 and Theorem 4 of [Paul (2007), Asymptotics of Sample Eigenstructure for a Large Dimensional Spiked Covariance Model](https://www3.stat.sinica.edu.tw/statistica/password.asp?art=18&num=4&vol=17). The notation is matched using $\beta=\ell-1$; the covariance action and the existing example's calculations are developed in the text.

The sample eigenvalue branches for all positive aspect ratios follow Theorems 1.1–1.3 of [Baik–Silverstein, Eigenvalues of Large Sample Covariance Matrices of Spiked Population Models](https://arxiv.org/pdf/math/0408165). The alignment formula is restricted to the Gaussian model with $0<\gamma<1$ stated earlier.

## Lesson summary

- A rank-one spike increases variance in one population direction.
- Sample separation depends on the relation between signal strength and aspect ratio.
- Below the threshold, recovery of the PCA direction can fail.
- For actual representations, a stable subspace can be more appropriate than an individual vector.

## Pass criteria

- Can you calculate the population spike and separation threshold?
- Can you distinguish an eigenvalue outlier from eigenvector properties and task relevance?

## Next lesson

- [A09-RMT-06 Signal and noise eigenvalues](A09-RMT-06-signal-noise-eigenvalues.md)

## Author checklist

- [x] Spike strength, outliers, and eigenvector recovery are distinguished.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
