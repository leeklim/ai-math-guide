---
id: "A09-DYN-06"
title: "Introduction to stochastic differential equations"
part: 4
stage: "A09-DYN"
status: "complete"
prerequisites: ["A09-DYN-05", "M04-04"]
estimated_time: "90–120 minutes"
---

# A09-DYN-06. Introduction to stochastic differential equations

## Why this lesson matters

Brownian paths are not differentiable in the ordinary sense, so dynamics with random forcing cannot be handled using ordinary derivatives alone. A stochastic differential equation defines drift and diffusion through rules for infinitesimal increments.

## Learning objectives

- Read the drift and diffusion coefficients of an Itô SDE.
- Explain the scale of a Brownian increment.
- Compute the quadratic variation term in Itô's formula.
- Distinguish an Euler–Maruyama simulation from the continuous SDE.

## Prerequisite check

- Prerequisite lessons: [A09-DYN-05 Langevin dynamics](A09-DYN-05-langevin-dynamics.md), [M04-04 Expectation, variance, and covariance](../../part-1-foundations/M04/M04-04-expectation-variance-covariance.md)
- Check question: What is the scale of the standard deviation of a Gaussian increment whose variance is proportional to time?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $dX_t=b(X_t,t)dt+\sigma(X_t,t)dW_t$ | `d X sub t equals b of X sub t and t d t plus sigma of X sub t and t d W sub t` | Itô SDE | Stochastic increment |
| $b$ | `b` | Drift coefficient | Vector |
| $\sigma$ | `sigma` | Diffusion coefficient | Matrix |
| $[W]_t=t$ | `the quadratic variation of W at t equals t` | Brownian quadratic variation | Scalar |

## Core concepts

### SDE coefficients and the integral meaning of the notation

For $X_t\in\mathbb R^d$ and $W_t\in\mathbb R^m$, the drift $b(X_t,t)$ is a $d$-dimensional vector, and the diffusion coefficient $\sigma(X_t,t)$ is a $d\times m$ matrix. The matrix $\sigma$ maps noise input directions to directions of change in the state. Over a small step with position and time held fixed, the covariance of the noise displacement corresponds to $\sigma\sigma^\top\Delta t$. The coefficient $\sigma$ itself is not the covariance.

SDE notation is shorthand for the integral relation

$$
X_t=X_0+\int_0^t b(X_s,s)\,ds
+\int_0^t\sigma(X_s,s)\,dW_s.
$$

The first integral is an ordinary time integral, and the second is an Itô stochastic integral. The latter is defined by summing products of the coefficient known at the start of each short interval and the Brownian increment over that interval. With this choice, the coefficient is not selected by looking ahead at future noise. This relation is used under coefficient conditions ensuring existence of the solution and integrability; the rigorous construction of the integral is not covered here.

Read the mapping of noise directions and the order of coefficient evaluation separately below.

<figure class="lesson-figure" markdown="1">

![Illustrative two-state one-noise coefficient sigma column two one maps every scalar increment to vector two delta W delta W lying on a line and gives covariance matrix four two two one times the interval](../../figures/assets/A09-DYN/A09-DYN-06-diffusion-line-support.svg)

<figcaption>This illustration uses d = 2, m = 1, and σ = (2, 1)ᵀ. The scalar ΔW maps to ΔX = (2ΔW, ΔW), so noise displacements lie on one line. The coefficient σ is a 2×1 mapping, while the covariance is the 2×2 matrix σσᵀΔt = [[4, 2], [2, 1]]Δt.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Illustrative coefficient sigma of x equals x is frozen at known starting state one before a later increment zero point two is observed so noise displacement uses starting coefficient one rather than a future state](../../figures/assets/A09-DYN/A09-DYN-06-left-point-coefficient.svg)

<figcaption>The illustration uses σ(x) = x and starting state Xₖ = 1. The coefficient 1 is chosen before the new increment 0.2 is known, then multiplied by it. This is one increment showing the left-point evaluation order of an Itô sum, not an exact solution of the entire SDE.</figcaption>

</figure>

### Brownian increments and quadratic variation

For standard one-dimensional Brownian motion, an increment over time $\Delta t$ satisfies

$$
\Delta W\sim\mathcal N(0,\Delta t),
$$

Increments over disjoint intervals are independent and have mean 0. Since the variance is $\Delta t$, the standard deviation is $\sqrt{\Delta t}$. This describes a probabilistic scale, not a bound that every increment must satisfy.

Divide the time interval $[0,t]$ into $n$ intervals and sum the squared increments. Each term has mean $t/n$, and the sum has mean $t$. As the partition becomes finer, the probability that this sum differs from $t$ by more than a fixed positive amount tends to 0. This convergence in probability gives the quadratic variation $[W]_t=t$. For a continuously differentiable curve, displacement scales with the interval length, so the sum of squared displacements tends to 0. For Brownian motion, the accumulated squares of the noise remain.

Compare the two scales and the sums of squares below to identify the accumulated term absent from ordinary differentiation.

<figure class="lesson-figure" markdown="1">

![Log-log axes compare Brownian increment standard deviation square root h with smooth unit-velocity displacement h and mark h zero point zero four where the two scales are zero point two and zero point zero four](../../figures/assets/A09-DYN/A09-DYN-06-brownian-smooth-scale.svg)

<figcaption>At the existing Δt = 0.04, the Brownian standard deviation is 0.2, while the displacement of a smooth curve with velocity 1 is 0.04. The upper curve shows a probabilistic spread, not the maximum of all ΔW. The logarithmic axes compare the two scales at small h.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Three seeded nested Brownian increment examples over time zero to one have sums of squared increments approaching reference one as partitions refine while smooth curve x equals t has exact sum one over n approaching zero](../../figures/assets/A09-DYN/A09-DYN-06-quadratic-variation-comparison.svg)

<figcaption>Over [0, 1], 3 illustrative Brownian increment paths were generated with fixed seeds. Each coarse increment is a sum of the corresponding fine increments. The finite sums of squares are not exactly 1 every time, and this figure is not itself a proof of convergence in probability. For the smooth curve x(t) = t, the sum of squares is exactly 1/n.</figcaption>

</figure>

### The second-order term in Itô's formula

Now suppose that $X_t,W_t$ are scalar and that $f$ is a time-independent function with a continuous second derivative. The scalar Itô formula is

$$
df(X_t)=f'(X_t)dX_t+\frac12f''(X_t)\sigma(X_t,t)^2dt
$$

Substituting $dX_t=b\,dt+\sigma\,dW_t$ gives drift $f'b\,dt+\tfrac12f''\sigma^2dt$ and noise $f'\sigma\,dW_t$. Time- and position-dependent coefficients are evaluated at the current $(X_t,t)$.

The additional term comes from $\tfrac12 f''(X_t)(\Delta X)^2$ in the Taylor expansion. Squaring the noise component $\sigma\Delta W$ leaves a term on the time scale, so it cannot be discarded as in the ordinary chain rule. The common notation $(dW_t)^2=dt$ is a calculation rule expressing this accumulated quadratic variation. It is not an equality saying that the square of an individual finite increment is exactly $\Delta t$.

Do not confuse the finite square term of the parabola below with a dt equality for an individual increment.

<figure class="lesson-figure" markdown="1">

![Quadratic f of one plus delta equals one plus two delta plus delta squared lies above its first-order tangent by zero point zero nine at illustrative increments plus or minus zero point three](../../figures/assets/A09-DYN/A09-DYN-06-finite-square-remainder.svg)

<figcaption>The plot shows f(x) = x² at current state X = 1. At ΔX = ±0.3, the difference between the tangent and the actual squared value is (ΔX)² = 0.09. For example, a Brownian increment over h = 0.04 can be 0.3, and its square need not equal h. The dt term in Itô's formula arises from accumulating such squares.</figcaption>

</figure>

### Euler–Maruyama and the target of an accuracy comparison

At $t_k=kh$, Euler–Maruyama approximates the SDE by

$$
X_{k+1}=X_k+h\,b(X_k,t_k)
+\sigma(X_k,t_k)\sqrt h\,\xi_k,
\qquad \xi_k\sim\mathcal N(0,I_m)
$$

The coefficients are evaluated at the starting point, and the $\xi_k$ for different steps are independent. Changing the seed changes the noise path itself, so the difference between two runs cannot immediately be called numerical error.

Strong convergence asks whether the difference between the approximate state and the continuous solution shrinks when both use the same Brownian path. Weak convergence asks whether distributional statistics, such as $\mathbb E[f(X_t)]$ measured across many paths, become closer. For a paired comparison of paths with different step sizes, sum the fine-step increments to obtain the coarse-step increments. Merely using the same seed number while generating Gaussian arrays of different sizes does not guarantee the same Brownian path.

Match the coarse noise to the same path by summing fine increments, as shown below.

<figure class="lesson-figure" markdown="1">

![Illustrative observed Brownian values at four fine intervals of length zero point zero one have increments zero point one minus zero point two zero point three zero point zero five summing to coarse increment zero point two five over length zero point zero four](../../figures/assets/A09-DYN/A09-DYN-06-paired-coarse-fine-increments.svg)

<figcaption>The illustrative fine increments 0.1, −0.2, 0.3, and 0.05 sum to the coarse ΔW = 0.25. This grouping shares the same endpoints; it does not draw a separate new coarse Gaussian increment. The lines are guides joining stored points, not observations of the actual Brownian path between them.</figcaption>

</figure>

## Small example

For $dX_t=\sigma dW_t$, suppose that $\sigma$ and $X_0$ are constant. With $f(x)=x^2$, the derivatives are $f'=2x$ and $f''=2$, so substitution into Itô's formula gives $d(X_t^2)=2X_t\sigma dW_t+\sigma^2dt$. Integrating and taking expectations gives $\mathbb E[X_t^2]=X_0^2+\sigma^2t$, because the stochastic integral has expectation 0. The mean of $X_t=X_0+\sigma W_t$ is $X_0$ and its variance is $\sigma^2t$, confirming the same result through a probability calculation. Dropping the correction term misses this increase in variance.

The time axis below shows the increase in the second moment recovered by the correction term.

<figure class="lesson-figure" markdown="1">

![For constant initial value one and diffusion one exact second moment of X t equals one plus time while dropping the Ito correction would incorrectly predict a constant second moment one](../../figures/assets/A09-DYN/A09-DYN-06-ito-second-moment.svg)

<figcaption>The existing example with constant X₀ and σ uses X₀ = 1 and σ = 1. The correct E[Xₜ²] increases as 1 + t; dropping the correction term misses the increase t. The vertical axis is the expectation of X², not the mean of X.</figcaption>

</figure>

## Common misconceptions

- Do not treat $dW_t/dt$ as an ordinary finite random variable.
- A single SDE trajectory does not represent distribution-level dynamics.

## Exercises

### 1. Increment scale
Find the standard deviation of a standard Brownian increment for $\Delta t=0.04$.
<details><summary>Show solution</summary>

It is $\sqrt{0.04}=0.2$.
</details>

### 2. Itô term
For $dX_t=dW_t$ and $f(x)=x^2$, find $df$.
<details><summary>Show solution</summary>

It is $df=2X_t dW_t+dt$.
</details>

### 3. Euler–Maruyama
For $dX=-Xdt+dW$, $X_0=1$, $h=0.01$, and $\xi_0=0$, what is $X_1$?
<details><summary>Show solution</summary>

It is $X_1=1-0.01=0.99$.
</details>

### 4. Unit of analysis
Describe when a paired design is possible when comparing SDE paths with different seeds.
<details><summary>Show solution</summary>

Using the same Brownian increment sequence under both conditions gives common-random-number pairing, which can reduce the variance of differences in dynamics.
</details>

## Evidence and update boundaries

Itô SDEs, quadratic variation, and Itô's formula were checked against Section 1.3 and Sections 3.2–3.4 of [Pavliotis's author-provided manuscript](https://www.ma.imperial.ac.uk/~pavl/PavliotisBook.pdf). Measure-theoretic construction and the Stratonovich integral are not covered.

## Lesson summary

- Brownian increments have scale $\sqrt{dt}$.
- Their squares have scale $dt$ and produce the Itô correction.
- Euler–Maruyama is a finite-step approximation to a continuous SDE.
- Distinguish path-level claims from distribution-level claims.

## Pass criteria

- Can you compute Brownian increment scales and Itô corrections?
- Can you explain the step-size and seed dependence of an SDE simulation?

## Next lesson

- [A09-DYN-07 Continuous-time approximation of SGD](A09-DYN-07-continuous-time-sgd.md)

## Author checklist

- [x] The distinction between Itô calculus and ordinary calculus is explained.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
