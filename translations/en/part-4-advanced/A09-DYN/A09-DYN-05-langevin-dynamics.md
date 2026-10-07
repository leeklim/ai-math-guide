---
id: "A09-DYN-05"
title: "Langevin dynamics"
part: 4
stage: "A09-DYN"
status: "complete"
prerequisites: ["A09-DYN-01", "A09-DYN-04", "M04-05"]
estimated_time: "90–120 minutes"
---

# A09-DYN-05. Langevin dynamics

## Why this lesson matters

Combining drift along the gradient direction with random fluctuations allows optimization noise and sampling to be compared in one mathematical framework. Langevin dynamics combines a force moving down an energy landscape with diffusion.

## Learning objectives

- Distinguish drift and diffusion in the overdamped Langevin equation.
- Explain how temperature affects the stationary density.
- Compute an Euler–Maruyama update.
- State the difference between SGD noise and isotropic Langevin noise.

## Prerequisite check

- Prerequisite lessons: [A09-DYN-01 Differential equations and flows](A09-DYN-01-odes-flows.md), [A09-DYN-04 Markov processes](A09-DYN-04-markov-process.md), [M04-05 Common distributions](../../part-1-foundations/M04/M04-05-common-distributions.md)
- Check question: What becomes of the next state when a Gaussian perturbation is added to a deterministic gradient step?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $U(x)$ | `U of x` | Potential or energy | Scalar |
| $T$ | `temperature T` | Noise scale | Positive scalar |
| $W_t$ | `W sub t` | Brownian motion | Stochastic process |
| $dX_t=-\nabla U(X_t)dt+\sqrt{2T}\,dW_t$ | `d X sub t equals minus the gradient of U at X sub t d t plus the square root of two T d W sub t` | Overdamped Langevin equation | Vector SDE |

## Core concepts

### The roles of drift and diffusion

Overdamped Langevin dynamics is

$$
dX_t=-\nabla U(X_t)dt+\sqrt{2T}\,dW_t
$$

Here $X_t\in\mathbb R^d$ is the random state, and $U:\mathbb R^d\to\mathbb R$ is the energy. This notation sets the friction and mobility constants to 1. Overdamped means that only changes in position are described, without tracking velocity as a separate state.

The first term, $-\nabla U$, is the drift determining mean motion toward lower energy at the current position. Removing the noise gives the gradient flow of the preceding lessons. The second term uses standard $d$-dimensional Brownian motion $W_t$ with independent coordinate processes. Over an interval of length $h$, the increment $W_{t+h}-W_t$ has mean 0 and covariance $hI$, so the displacement due to diffusion has covariance $2ThI$. It is isotropic in the sense that, for the same $T$, noise has the same magnitude in every direction. Brownian paths are not ordinary differentiable curves, so $dW_t$ must not be divided and interpreted as a finite instantaneous velocity.

Read the current energy and drift as different vertical values along the same state axis below.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Upper quadratic potential one half x squared and lower drift minus x share the same state axis with current state one having energy one half but velocity minus one pointing toward zero](../../figures/assets/A09-DYN/A09-DYN-05-potential-drift.svg)

<figcaption>This is the existing example U(x) = x²/2. Energy U(1) = 1/2 and drift −U′(1) = −1 are different quantities. The direction of motion is determined by the negative gradient at the current position, not just by saying that energy is high.</figcaption>

</figure>

### Temperature and the stationary density

For sufficiently smooth $U$, existence of the solution for all time, and appropriate boundary conditions, the stationary density is

$$
p_\infty(x)\propto e^{-U(x)/T}
$$

To use this as a probability density, $Z=\int_{\mathbb R^d}e^{-U(x)/T}\,dx$ must be finite, and normalization gives $p_\infty(x)=Z^{-1}e^{-U(x)/T}$. Confinement is a condition under which energy grows sufficiently far away to allow this normalization and stable behavior. For example, if $U=0$ throughout $\mathbb R^d$, a constant function cannot be normalized, so no stationary probability density of the displayed form exists.

The density ratio at two positions is $p_\infty(x)/p_\infty(y)=e^{-(U(x)-U(y))/T}$. Even for the same energy difference, a smaller $T$ suppresses relative density at higher energy more strongly. Stationary means that starting in this distribution preserves it. It does not mean that one sample path stops at a minimum or that every initial distribution reaches it quickly.

Distinguish normalized density, relative density, and nonnormalizable weights below.

<figure class="lesson-figure" markdown="1">

![Normalized zero-mean Gaussian stationary densities for quadratic potential have variance one quarter or one when temperature is one quarter or one respectively with narrower and wider peaks](../../figures/assets/A09-DYN/A09-DYN-05-quadratic-temperature-density.svg)

<figcaption>For U = x²/2, compare T = 0.25 and T = 1. Both densities integrate to 1 and have variance T. The higher peak and narrower width at lower T describe the shape of a normalized distribution, not a sample path stopping at the origin.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Relative stationary density exp of minus energy difference over temperature decays faster at temperature one quarter than at temperature one and marks energy difference one half with ratios about zero point one three five and zero point six zero seven](../../figures/assets/A09-DYN/A09-DYN-05-energy-density-ratio.svg)

<figcaption>The horizontal axis is ΔU = U(x) − U(y), and the vertical axis is p∞(x)/p∞(y). At ΔU = 0.5, T = 0.25 gives e⁻² ≈ 0.135, while T = 1 gives e⁻⁰·⁵ ≈ 0.607. The normalizing constant Z cancels in this ratio.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Constant unnormalized weight one over state windows minus one to one and minus three to three has shaded integrals two and six so enlarging the window increases mass rather than approaching a finite normalizer](../../figures/assets/A09-DYN/A09-DYN-05-unconfined-window-mass.svg)

<figcaption>If U = 0, then exp(−U/T) = 1. The weight integrates to 2 over the window [−1, 1] and grows to 6 over [−3, 3]. Expanding the window indefinitely gives no finite Z. The height 1 here is not a normalized probability density.</figcaption>

</figure>

### An Euler–Maruyama step

The Euler–Maruyama update with step $h$ is

$$
X_{k+1}=X_k-h\nabla U(X_k)+\sqrt{2Th}\,\xi_k,
\qquad \xi_k\sim\mathcal N(0,I)
$$

The drift is held fixed at the start of the step and multiplied by $h$. The Brownian increment is expressed as $\sqrt h\,\xi_k$, with a new independent standard Gaussian vector $\xi_k$ drawn at every step. Noise is therefore multiplied not by $h$ but by $\sqrt h$. In this update, the conditional mean of the next state is $X_k-h\nabla U(X_k)$, and its conditional covariance is $2ThI$.

This is a numerical approximation to the continuous SDE. Holding drift fixed throughout the step can bias the stationary distribution at finite $h$. An excessively large $h$ can also produce unstable behavior unlike that of the continuous system. The quadratic example below computes this difference.

Inspect the mean movement and noise spread separately in the one-step distribution below.

<figure class="lesson-figure" markdown="1">

![Illustrative next-state Gaussian density from X k one in quadratic potential with temperature one half and step zero point zero one is centered at zero point nine nine with standard deviation zero point one and shaded one-standard-deviation interval](../../figures/assets/A09-DYN/A09-DYN-05-conditional-noise-law.svg)

<figcaption>This illustrative step uses Xₖ = 1, U = x²/2, T = 0.5, and h = 0.01. The mean after drift is 0.99, and the noise coefficient is 0.1 from the existing calculation. The shaded interval 0.89–1.09 is one standard deviation around the mean, not a bound containing all noise realizations.</figcaption>

</figure>

### Differences from mini-batch SGD

The Langevin update explicitly adds Gaussian noise with position-independent covariance $2ThI$. Mini-batch SGD noise arises from the difference between batch gradients and the mean gradient, so its variance in different directions can depend on parameters and sample composition. Having noise with mean 0 in common does not make the two systems identical. To judge whether a scalar temperature can represent SGD noise, check whether its covariance is nearly isotropic, whether it stays constant with position, and whether batches are dependent.

Compare direction-dependent covariances through the coordinate geometry below.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Two noise-coordinate panels compare covariance identity with circular geometry and illustrative covariance diagonal four and one quarter with elliptical geometry whose coordinate standard deviations are two and one half](../../figures/assets/A09-DYN/A09-DYN-05-isotropic-anisotropic-covariance.svg)

<figcaption>The upper panel shows isotropic geometry with covariance I, while the lower shows the illustrative geometry diag(4, 0.25). The lower coordinate standard deviations are 2 and 0.5, giving different spreads by direction. It illustrates a possible covariance difference, not an actual SGD experiment or an assumption that SGD noise is Gaussian.</figcaption>

</figure>

## Small example

For $U(x)=x^2/2$, the drift is $-x$. Normalizing $e^{-x^2/(2T)}$ gives the stationary Gaussian density with mean 0 and variance $T$. The continuous system maintains a distribution that balances drift toward the origin with noise.

Euler–Maruyama gives $X_{k+1}=(1-h)X_k+\sqrt{2Th}\,\xi_k$. For $0<h<2$, denote the stationary variance by $v$. Adding the variance of the independent noise gives $v=(1-h)^2v+2Th$. Thus, $v=2Th/(2h-h^2)=T/(1-h/2)$. As $h\to0$, it approaches $T$, but at finite $h$ it exceeds the continuous system's variance. This is a concrete example of discretization bias.

The curve below shows finite-step variance bias and the range of applicable time steps.

<figure class="lesson-figure" markdown="1">

![For quadratic potential and temperature one the discrete stationary variance one divided by one minus half the step grows above continuous variance one and approaches divergence at step two within the stability range](../../figures/assets/A09-DYN/A09-DYN-05-finite-step-variance-bias.svg)

<figcaption>The existing variance formula is evaluated at T = 1. At h = 0.5, v = 4/3; at h = 1, v = 2. Both exceed the continuous variance 1. The curve is used as a stationary variance formula only for 0 &lt; h &lt; 2, with h = 2 at the boundary of that range.</figcaption>

</figure>

## Common misconceptions

- Mini-batch SGD noise is generally not constant isotropic Gaussian noise.
- A finite-step Langevin update cannot be assumed to sample exactly from $e^{-U/T}$.

## Exercises

### 1. Drift
Compute the Langevin drift for $U(x)=2x^2$.
<details><summary>Show solution</summary>

Since $\nabla U=4x$, the drift is $-4x$.
</details>

### 2. Noise scale
For $T=0.5$ and $h=0.01$, compute the update noise coefficient $\sqrt{2Th}$.
<details><summary>Show solution</summary>

It is $\sqrt{0.01}=0.1$.
</details>

### 3. Temperature
As $T$ decreases, how does $p_\infty(x)\propto e^{-U(x)/T}$ change?
<details><summary>Show solution</summary>

Higher energy is suppressed more strongly, concentrating the distribution near minima.
</details>

### 4. Comparison with SGD
Why must noise covariance be measured when approximating SGD by Langevin dynamics?
<details><summary>Show solution</summary>

SGD noise can be anisotropic and state-dependent as parameter positions and batch composition vary, so a single isotropic temperature may not represent it.
</details>

## Evidence and update boundaries

The overdamped Langevin equation and Gibbs stationary density were checked against Section 4.5 of [Pavliotis's author-provided manuscript](https://www.ma.imperial.ac.uk/~pavl/PavliotisBook.pdf). Metropolis correction and underdamped dynamics are not covered.

## Lesson summary

- Langevin dynamics combines gradient drift and Brownian diffusion.
- Temperature controls the concentration of the stationary density.
- Euler–Maruyama noise has scale $\sqrt h$.
- Equating SGD noise with Langevin noise requires covariance assumptions.

## Pass criteria

- Can you explain the drift and stationary variance of a quadratic potential?
- Can you state limitations of finite-step and SGD approximations?

## Next lesson

- [A09-DYN-06 Introduction to stochastic differential equations](A09-DYN-06-stochastic-differential-equations.md)

## Author checklist

- [x] Drift, diffusion, and temperature are distinguished.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
