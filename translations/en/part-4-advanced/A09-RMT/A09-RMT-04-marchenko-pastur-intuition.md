---
id: "A09-RMT-04"
title: "Intuition for the Marchenko–Pastur law"
part: 4
stage: "A09-RMT"
status: "complete"
prerequisites: ["M04-05", "A09-RMT-03"]
estimated_time: "90–120 minutes"
---

# A09-RMT-04. Intuition for the Marchenko–Pastur law

## Why this lesson matters

Sample eigenvalues obtained from an identity population covariance do not all concentrate at a single value. The Marchenko–Pastur law predicts the high-dimensional spectral bulk of an iid noise matrix. Before calling a prominent eigenvalue in an observed activation spectrum a signal, we need to compare it with this null bulk.

## Learning objectives

- Calculate the MP bulk edges from the aspect ratio and noise variance.
- Explain why zero eigenvalues occur when $\gamma>1$.
- List the iid, isotropy, and finite-variance assumptions of the MP null.
- Explain the limitations of comparing an empirical spectrum with a fitted null.

## Prerequisite check

- Prerequisite lessons: [M04-05 Common distributions](../../part-1-foundations/M04/M04-05-common-distributions.md), [A09-RMT-03 The spectrum of sample covariance](A09-RMT-03-sample-covariance-spectrum.md)
- Check question: If the population covariance is $\sigma^2I$, what are all the population eigenvalues?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $\gamma=d/n$ | `gamma equals d over n` | Asymptotic aspect ratio | Positive scalar |
| $\lambda_-$ | `lambda minus` | Lower edge of the MP bulk | Nonnegative scalar |
| $\lambda_+$ | `lambda plus` | Upper edge of the MP bulk | Nonnegative scalar |
| $\sigma^2(1\pm\sqrt\gamma)^2$ | `sigma squared times one plus or minus square root gamma, squared` | MP edges for isotropic noise | Scalar pair |

## Core concepts

### Which distribution converges?

Suppose the entries of $X\in\mathbb R^{n\times d}$ are drawn iid from the same fixed distribution with mean 0 and variance $\sigma^2>0$. We consider a regime in which $n,d$ grow together and $d/n\to\gamma\in(0,\infty)$. Independence of the entries and their common variance ensure that the population covariance of a row is $\sigma^2I_d$. An isotropic covariance alone does not imply iid entries, so these conditions are not interchangeable.

Under the normalization $S=X^\top X/n$, count all $d$ eigenvalues. For example, multiplying the number of eigenvalues at or below a threshold $t$ by $1/d$ gives the empirical cumulative distribution. The MP law predicts the distribution formed by these proportions in a large matrix. It does not describe the error distribution obtained by repeatedly sampling a single eigenvalue, nor does it assign meaning to eigenvectors. Under the iid finite-variance conditions above, this empirical distribution converges to the Marchenko–Pastur distribution.

Counting the values that form a distribution and checking the iid assumption answer different questions. First, distinguish how we count the values of one matrix from coordinate dependence that covariance alone cannot reveal.

<figure class="lesson-figure" markdown="1">

![A fixed illustrative list of ten eigenvalues produces an empirical cumulative distribution with six values at or below one.](../../figures/assets/A09-RMT/A09-RMT-04-empirical-cdf-from-all-values.svg)

<figcaption>In a fixed illustrative eigenvalue list, counting the six values at or below t=1 gives F(1)=6/10. This curve is an empirical distribution formed from all the eigenvalues of one matrix, not an error distribution from repeated runs of the largest eigenvalue. No new null simulation was run.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![A uniform distribution on the circle of radius square root two has covariance identity while its two coordinates satisfy a fixed squared norm constraint and are not independent.](../../figures/assets/A09-RMT/A09-RMT-04-isotropic-not-independent-coordinates.svg)

<figcaption>For illustration, x=√2(cosθ,sinθ) with a uniformly distributed angle has mean 0 and covariance I₂. However, the constraint x₁²+x₂²=2 couples the two coordinates, so the entries are not independent. The line is the distribution's support, and the marked points indicate directions; they are not actual draws or MP null samples.</figcaption>

</figure>

### The scale and width of the bulk edges

The edges of the nonzero bulk are

$$
\lambda_-=\sigma^2(1-\sqrt\gamma)^2,
\qquad
\lambda_+=\sigma^2(1+\sqrt\gamma)^2
$$

Even when the population spectrum is the single point $\sigma^2$, the sample spectrum spreads across this interval.

Dividing $X$ by $\sigma$ gives unit-variance entries and changes the covariance to $S/\sigma^2$. This is why the scale factor on the edges is not $\sigma$ but $\sigma^2$. Also, squaring the singular values of $X/\sqrt n$ gives the eigenvalues of $S$, which is why the edge factors $(1\pm\sqrt\gamma)$ are squared. The lower edge is always nonnegative. When $\gamma>1$, even though $1-\sqrt\gamma$ is negative, its square is positive.

The difference between the two edges is $4\sigma^2\sqrt\gamma$. If $d/n$ tends to 0, both edges narrow toward $\sigma^2$. If it remains a positive constant, the width remains as well. The interval midpoint is $\sigma^2(1+\gamma)$, which differs from the mean eigenvalue $\sigma^2$. The bulk density is not uniform, so there is no reason for its midpoint to equal its mean.

Separating the density's mean, the interval midpoint, and the movement of the edges makes it easier to see which parts of the formula γ and σ² change.

<figure class="lesson-figure" markdown="1">

![The unit variance MP density at aspect ratio one quarter has support one quarter to two point two five with mean one and interval midpoint one point two five.](../../figures/assets/A09-RMT/A09-RMT-04-mp-mean-and-midpoint.svg)

<figcaption>This is the limiting MP density for the existing example σ²=1, γ=0.25. The support [0.25,2.25] has midpoint 1.25, but the mean is 1. These positions are not equal because the density is not uniform. This mean does not assert that the finite-sample mean is exactly 1.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Unit variance MP lower and upper edge curves meet the population scale as aspect ratio tends to zero while the lower edge touches zero at one and becomes positive above one.](../../figures/assets/A09-RMT/A09-RMT-04-aspect-ratio-bulk-edges.svg)

<figcaption>The curves show λ₋=(1−√γ)² and λ₊=(1+√γ)² for σ²=1. The lower edge is 0 at γ=1 and becomes positive again for γ&gt;1. These curves bound the nonzero bulk; they do not remove the zero mass for γ&gt;1.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![For the same aspect ratio one quarter the nonzero bulk interval changes from one quarter two point two five to one half four point five when noise variance doubles.](../../figures/assets/A09-RMT/A09-RMT-04-noise-variance-bulk-rescaling.svg)

<figcaption>With γ=0.25 fixed, the intervals [0.25,2.25] for σ²=1 and [0.5,4.5] for σ²=2 are compared on the same eigenvalue axis. The covariance and edges are proportional to σ², not σ. The two intervals do not represent uniform densities.</figcaption>

</figure>

### Nonzero bulk and zero mass

When $\gamma>1$, we have $d>n$, so the rank of the $d\times d$ covariance cannot exceed $n$. The asymptotic spectrum has zero mass of proportion $1-1/\gamma$. Centering can reduce the finite-sample rank by one more.

This means that, among the $d$ eigenvalues, approximately $d-n$ are exactly 0. The remaining approximately $n$ eigenvalues have proportion $1/\gamma$ and form the nonzero bulk. A positive lower edge and zero mass are therefore compatible when $\gamma>1$. The edge marks the beginning of the nonzero part, and the interval between 0 and the lower edge can be empty. At $\gamma=1$, the lower edge touches 0, but the limiting zero mass is 0. Distinguish the single finite-sample zero introduced by centering from a positive proportion of zero mass.

The centering operation from the previous lesson gives $X_c^\top X_c/n=X^\top X/n-\bar x\bar x^\top$. The subtracted term has rank at most 1, so it does not change the limiting bulk of proportions of all eigenvalues. It can, however, affect finite-sample rank and comparisons of extreme eigenvalues. A centered null must undergo the same processing.

The following two figures separately count a positive proportion of mass at zero and a single finite-sample zero.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![At aspect ratio two half the eigenvalues belong to a zero atom and the other half to a positive bulk whose conditional density starts above zero.](../../figures/assets/A09-RMT/A09-RMT-04-positive-bulk-and-zero-mass.svg)

<figcaption>For γ=2, the full eigenvalue measure consists of mass 1/2 at 0 and positive bulk mass 1/2. The right panel shows the density conditioned on positive eigenvalues, normalized to integrate to 1. A positive lower edge of about 0.172 is compatible with the zero atom on the left. Mass 1/2 is not a density height of 1/2.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![For a square Gaussian matrix uncentered zero fraction is zero while the one centering induced zero has fraction one over dimension tending to zero.](../../figures/assets/A09-RMT/A09-RMT-04-gamma-one-finite-centering-zero.svg)

<figcaption>In this illustrative square Gaussian null, full rank before centering and rank d−1 afterward hold almost surely. The proportion 1/d of this single zero tends to 0. Distinguish the limiting zero mass of 0 at γ=1 from one finite-sample zero. Additional rank restrictions, such as duplicate rows, are outside this example's contract.</figcaption>

</figure>

### Limiting bulk and finite-size decisions

Convergence of the distribution does not mean that every eigenvalue lies inside the edges in a finite sample. Even if one or two of the $d$ values lie outside, their proportion can tend to 0. The stronger claim that the largest eigenvalue approaches the upper edge must be checked separately under a null with well-controlled tails, such as a Gaussian null, or sufficient moment conditions. Finite variance alone does not justify adding this claim.

The MP bulk is a reference null. Dependence among activation rows or unequal feature variances differs from the iid isotropic model specified here. Finite-variance heavy tails can substantially change extreme eigenvalues even when a limiting bulk exists. An uncentered mean structure can create a large eigenvalue, but applying the same centering removes the common mean.

When fitting $\sigma^2$ using empirical variance, state which eigenvalues and split were used. If the scale estimate averages in the observed large eigenvalues, signal candidates can also raise the null scale. A fitted curve that looks good does not replace an iid diagnostic. A simulated null that reproduces the actual $n,d$, centering, and scale fitting makes the conditions of the finite-size comparison explicit. Here, we specify only the comparison contract and run no new simulation.

The fraction of values outside the bulk and the maximum must be examined separately. When fitting the null scale, also make explicit whether candidate values are included.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Constructed eigenvalue sequences contain quantiles inside the unit variance aspect quarter MP bulk and one value ten whose fraction decreases while the maximum remains ten.](../../figures/assets/A09-RMT/A09-RMT-04-bulk-fraction-versus-maximum.svg)

<figcaption>This illustrative sequence places the remaining d−1 values at numerical quantiles of the γ=0.25 MP bulk and sets just one value to 10. The outside-bulk fraction shrinks as 1/d, but the maximum stays at 10. This is a nonrandom construction distinguishing distribution convergence from control of the maximum, not an iid noise matrix simulation or a finite-size decision cutoff.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A fixed list of nine unit eigenvalues and one candidate ten changes the fitted mean scale from one to one point nine and the aspect quarter MP upper edge from two point two five to four point two seven five.](../../figures/assets/A09-RMT/A09-RMT-04-candidate-affects-fitted-null-scale.svg)

<figcaption>For illustration, nine values of 1 and one candidate of 10 have overall mean 1.9; excluding the candidate gives mean 1. Using these as a simple scale fit raises the γ=0.25 upper edge from 2.25 to 4.275. This calculation makes explicit which values enter the fit. It does not propose a valid scale estimator or show that the candidate is a task signal.</figcaption>

</figure>

## Small example

With $\sigma^2=1$ and $\gamma=0.25$, we have $\sqrt\gamma=0.5$, so the bulk is $[0.25,2.25]$. The largest sample eigenvalue can be much greater than 1 even when there is only noise.

A limiting mean eigenvalue of 1 is not inconsistent with an upper edge of 2.25. Averaging the low and high eigenvalues together yields a value approaching 1, whereas the finite-sample mean need not be exactly 1. This $\gamma<1$ example has no positive limiting zero mass, and 2.25 is not an exact decision cutoff for the finite-size largest eigenvalue.

## Common misconceptions

- An eigenvalue above the MP upper edge is not necessarily a task signal. Null misspecification can also produce an outlier.
- Fitting an MP curve to an empirical spectrum does not by itself validate the iid assumption.

## Exercises

### 1. Edges
Find the MP bulk edges when $\sigma^2=2$ and $\gamma=1$.
<details><summary>Show solution</summary>

$\lambda_-=2(1-1)^2=0$ and $\lambda_+=2(1+1)^2=8$.
</details>

### 2. Aspect ratio
For $n=400$ and $d=100$, what is the unit-variance MP upper edge?
<details><summary>Show solution</summary>

Since $\gamma=0.25$, it is $(1+0.5)^2=2.25$.
</details>

### 3. Zero mass
What is the asymptotic proportion of zero eigenvalues in an uncentered null covariance with $\gamma=2$?
<details><summary>Show solution</summary>

It is $1-1/\gamma=1-1/2=0.5$.
</details>

### 4. Model interpretation
One activation eigenvalue slightly exceeds a fitted MP edge. What further diagnostics would you perform?
<details><summary>Show solution</summary>

Check prompt-cluster dependence, feature variances, and tails, and compute a matched simulated null, split stability, and bootstrap intervals together.
</details>

## Evidence and update boundaries

The edge formula describes the limiting bulk of an iid isotropic finite-variance null with the $1/n$ covariance normalization. Finite-size largest-eigenvalue corrections and Tracy–Widom tests are outside this lesson's scope. Bulk convergence alone does not imply convergence of extreme eigenvalues.

For the role of the MP bulk and the distinction between bulk convergence and control of every eigenvalue, see §1.2 and the remarks in §1.3 of [Bandeira, Ten Lectures in the Mathematics of Data Science](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-of-data-science-fall-2015/5f0f7205d1cf274e80d77345a7edbf2a_MIT18_S096F15_TenLec.pdf). The scale, width, zero-proportion, and centering-rank calculations in the text use this lesson's $n\times d$ convention.

The distinction between finite-variance bulk universality and additional moments needed for extreme singular values is discussed in §1 and Theorem 2.1 of [Rudelson–Vershynin, Non-asymptotic theory of random matrices](https://websites.umich.edu/~rudelson/papers/rv-ICM2010.pdf).

## Lesson summary

- Even an isotropic population produces a spectral bulk in a high-dimensional sample.
- The MP edges depend on noise variance and aspect ratio.
- When $d>n$, rank deficiency creates zero mass.
- Use MP comparisons as a null analysis that checks its assumptions.

## Pass criteria

- Can you calculate the bulk edges from $\sigma^2$ and $\gamma$?
- Can you distinguish exceeding the MP edge from being a task signal?

## Next lesson

- [A09-RMT-05 Spiked covariance model](A09-RMT-05-spiked-covariance-model.md)

## Author checklist

- [x] The MP bulk edges, zero mass, and null assumptions are explained together.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
