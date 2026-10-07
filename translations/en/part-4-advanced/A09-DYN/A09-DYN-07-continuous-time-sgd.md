---
id: "A09-DYN-07"
title: "Continuous-time approximation of SGD"
part: 4
stage: "A09-DYN"
status: "complete"
prerequisites: ["A09-DYN-06", "I08-04", "I08-05"]
estimated_time: "90–120 minutes"
---

# A09-DYN-07. Continuous-time approximation of SGD

## Why this lesson matters

Approximating SGD updates by an ODE or SDE allows analysis of the average behavior produced by learning rate, batch noise, and loss geometry. But removing momentum, adaptive state, finite steps, and non-Gaussian noise produces a model different from the actual optimizer.

## Learning objectives

- Decompose an SGD update into a mean gradient and noise.
- Distinguish the roles of gradient flow and diffusion approximations.
- Explain how learning rate and batch size affect the approximate noise scale.
- Propose measurements for diagnosing the validity of a continuous-time approximation.

## Prerequisite check

- Prerequisite lessons: [A09-DYN-06 Introduction to stochastic differential equations](A09-DYN-06-stochastic-differential-equations.md), [I08-04 SGD dynamics](../../part-3-interpretability/I08/I08-04-sgd-as-dynamics.md), [I08-05 Mini-batch noise](../../part-3-interpretability/I08/I08-05-minibatch-noise-optimizer-state.md)
- Check question: What random variable is the difference between a mini-batch gradient and the full gradient?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $g_B(\theta)$ | `g sub B of theta` | Mini-batch gradient | Parameter-shaped vector |
| $\xi_B(\theta)$ | `xi sub B of theta` | Gradient noise | Zero-mean under sampling assumptions |
| $C(\theta)$ | `C of theta` | Gradient-noise covariance | PSD matrix |
| $\eta$ | `eta` | Learning rate | Positive scalar |
| $S(\theta)$ | `S of theta` | Noise coefficient satisfying $SS^\top=C$ | $d\times d$ |
| $\Theta_t$ | `Theta sub t` | Random parameters of the continuous-time approximation | $d$-dimensional vector |

## Core concepts

### Decomposing the mean gradient and noise

Fix the loss $L$ and sampling rule, and write the mini-batch gradient as

$$
g_B(\theta)=\nabla L(\theta)+\xi_B(\theta)
$$

The difference $\xi_B=g_B-\nabla L$ can always be defined, but $\mathbb E_B[\xi_B\mid\theta]=0$ holds when the batch gradient is an unbiased estimator of the gradient of the same $L$. Uniform sampling with the average of sample losses is a typical example. Different weighting or sampling can change the mean gradient itself.

Plain SGD is $\theta_{k+1}=\theta_k-\eta\nabla L(\theta_k)-\eta\xi_k$. Define the gradient-noise covariance as $C(\theta)=\mathbb E_B[\xi_B\xi_B^\top\mid\theta]$. Under the zero-mean condition, the noise covariance of one update is $\eta^2C(\theta_k)$. Distinguishing noise in the gradient from noise in the parameter displacement prevents the squared learning-rate factor from being missed.

Distinguish the signs and magnitudes of gradient noise and parameter displacement on the coordinates below.

<figure class="lesson-figure" markdown="1">

![Illustrative scalar SGD starting parameter one with mean gradient three batch gradient five noise two and learning rate one tenth moves to zero point seven by mean drift then zero point five after additional negative noise displacement](../../figures/assets/A09-DYN/A09-DYN-07-gradient-update-components.svg)

<figcaption>For the existing gradient 3 and batch gradient 5, the noise is ξ = 2. Using illustrative θₖ = 1 and η = 0.1, adding mean displacement −0.3 and noise displacement −0.2 gives θₖ₊₁ = 0.5. Gradient noise ξ and actual parameter noise −ηξ differ in sign and units.</figcaption>

</figure>

### Time scale and gradient flow

For a constant learning rate $\eta$, assign each step duration $\eta$ and write $t_k=k\eta$. Dividing the update by this duration gives

$$
\frac{\theta_{k+1}-\theta_k}{\eta}
=-\nabla L(\theta_k)-\xi_k
$$

Removing noise and approximating continuous change at small step sizes gives gradient flow

$$
\dot\theta=-\nabla L(\theta)
$$

If the step index $k$ itself is used as time, the mean rate of change carries a factor $\eta$. The choice of time axis must therefore be stated. Nor does this mean that the expected parameters of a stochastic run satisfy this ODE exactly. For a nonlinear loss, generally $\mathbb E[\nabla L(\theta)]\ne\nabla L(\mathbb E[\theta])$.

Changing the order of averaging can give the two different target points below.

<figure class="lesson-figure" markdown="1">

![Illustrative gradient function theta squared at equally probable parameters minus one and plus one has mean gradient one but gradient at their mean parameter zero equals zero marked as distinct points](../../figures/assets/A09-DYN/A09-DYN-07-mean-gradient-nonlinearity.svg)

<figcaption>The illustrative loss L(θ) = θ³/3 has ∇L = θ², with θ = −1 and 1 each assigned probability 1/2. The mean parameter is 0, but the mean gradient is 1. Evaluating the gradient once at the mean parameter gives (0, 0), different from (0, 1), obtained by computing gradients first and then averaging.</figcaption>

</figure>

### Diffusion coefficients and batch size

A representative SDE that matches covariance over small steps is

$$
d\Theta_t=-\nabla L(\Theta_t)\,dt
+\sqrt\eta\,S(\Theta_t)\,dW_t,
\qquad S(\theta)S(\theta)^\top=C(\theta)
$$

The processes $\Theta_t,W_t$ can be taken as $d$-dimensional and $S$ as $d\times d$. Since $C$ is positive semidefinite, a matrix square root provides such an $S$. The covariance of a Brownian increment over duration $\eta$ is $\eta I$. Holding this SDE's coefficient fixed at the start of the step therefore gives noise displacement covariance $\eta\cdot\eta SS^\top=\eta^2C$. The negative sign of SGD noise is matched by changing the sign of a symmetric Gaussian increment.

This calculation explains why the local mean and covariance match. It does not imply that gradient noise is exactly Gaussian or that an individual SGD path is reproduced unchanged. A short-time weak approximation requires conditions on the regularity of the loss and coefficients, noise moments, and the temporal dependence of sampling. Higher accuracy may also require a drift correction.

When individual sample gradients are drawn independently and $B$ of them are averaged, batch noise covariance is $1/B$ times the individual sample covariance. Under this convention, the SDE diffusion covariance per unit time scales as $\eta C\propto\eta/B$, and the coefficient's magnitude scales as $\sqrt{\eta/B}$. The same formula cannot be applied unchanged to sampling without replacement, dependence across batches, or different loss-sum and loss-mean conventions. Learning rate and batch size alone are insufficient to determine the noise; the directional structure of $C$ is also needed.

Read per-step covariance, covariance per unit time, the two √η factors in the SDE, and batch-average scaling separately below.

<figure class="lesson-figure" markdown="1">

![Two panels for illustrative scalar gradient-noise covariance four plot per-step update variance four eta squared and covariance per unit continuous time four eta separately marking eta one tenth with zero point zero four versus zero point four](../../figures/assets/A09-DYN/A09-DYN-07-step-time-covariance.svg)

<figcaption>The illustrative scalar C = 4 is held fixed. With step duration η, update covariance is η²C, while covariance per unit time is (η²C)/η = ηC. The values 0.04 and 0.4 at η = 0.1 are not different calculations of the same quantity; they are two measurements with different time units.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Scalar learning rate one tenth and gradient covariance four give SGD noise standard deviation one fifth and SDE coefficient two times square root one tenth times Brownian interval standard deviation square root one tenth also one fifth so both step variances equal zero point zero four](../../figures/assets/A09-DYN/A09-DYN-07-local-covariance-match.svg)

<figcaption>This illustrative scalar calculation uses η = 0.1, C = 4, and S = 2. On the right, the increment over duration η and coefficient √ηS each contribute √η, giving step standard deviation ηS = 0.2. Only covariance is matched to −ηξ on the left. The calculation neither adds the two noise paths nor reproduces an individual SGD path.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Log axes for independent averaged samples with scalar covariance one plot diffusion variance per time eta over batch size for learning rates zero point one and zero point zero five and mark batch four at variance zero point zero two five](../../figures/assets/A09-DYN/A09-DYN-07-learning-rate-batch-scale.svg)

<figcaption>This illustrative calculation assumes individual sample gradient covariance 1 and independent batch averaging. Covariance per unit time is η/B, so doubling B halves it and doubling η doubles it. The noise coefficient is the square root of this covariance. The curve does not automatically apply to other sampling or loss conventions.</figcaption>

</figure>

### Diagnosing the validity of an approximation

Diagnostics include relative update norm, gradient-noise mean and covariance, autocorrelation, the learning-rate schedule, and momentum or Adam moments. Comparing gradients from several batches at the same parameters separates noise from drift. Pooling gradients from different checkpoints can count changes in the mean gradient due to parameter movement as noise.

Even a small relative update can have substantial finite-step error along directions where the gradient changes rapidly. Lag autocorrelation helps identify memory omitted by an independent-Brownian-increment approximation, while optimizer moments help determine whether the state itself must be augmented. Compare approximation errors over the same time horizon and using the same observed statistics. Agreement of finite-horizon statistics does not guarantee accuracy for rare transitions or long-term stationary behavior.

Compare fixed-checkpoint measurements with pooling across moving checkpoints below.

<figure class="lesson-figure" markdown="1">

![Illustrative gradient populations at fixed parameters zero and one have the same three centered noise values minus zero point one zero zero point one but pooling the two means produces much larger variance](../../figures/assets/A09-DYN/A09-DYN-07-fixed-versus-pooled-gradients.svg)

<figcaption>With illustrative ∇L(θ) = θ, the three batch noise values at each fixed state are −0.1, 0, and 0.1. Each equally weighted set has variance approximately 0.0067. Pooling the two states with equal weight gives variance approximately 0.2567, which also includes the change in mean gradient from 0 to 1.</figcaption>

</figure>

## Small example

For the scalar quadratic $L(\theta)=a\theta^2/2$ with $a>0$, gradient flow is $\theta(t)=\theta_0e^{-at}$. Gradient descent gives $(1-\eta a)^k\theta_0$, while the flow at the same time $t_k=k\eta$ is $e^{-ak\eta}\theta_0$. Compare the one-step multipliers using $e^{-a\eta}\approx1-a\eta$.

The continuous solution always converges to 0, but the discrete update converges when $|1-\eta a|<1$, or $0<\eta a<2$. Within that range, $1<\eta a<2$ gives alternating signs, a behavior absent from the continuous solution. Satisfying the condition for long-term convergence is different from accurately approximating the shape of the continuous path.

The multiplier curves below distinguish conditions for discrete convergence from those for matching the continuous path.

<figure class="lesson-figure" markdown="1">

![Against dimensionless eta a the Euler multiplier one minus eta a crosses zero at one and negative one at two while exact flow multiplier exp of minus eta a stays positive and below one for every positive eta a](../../figures/assets/A09-DYN/A09-DYN-07-euler-multiplier-stability.svg)

<figcaption>The horizontal axis is q = ηa. Euler's multiplier has magnitude less than 1 for 0 &lt; q &lt; 2 and is negative for 1 &lt; q &lt; 2, reversing the sign. The exact one-step flow multiplier e⁻ᑫ is positive and less than 1 for every q &gt; 0. Points on the gray boundaries ±1 are not in the strict convergence range.</figcaption>

</figure>

## Common misconceptions

- Batch size alone does not uniquely determine SGD temperature.
- Writing AdamW as parameter-only gradient flow misses moment state and the separation of weight decay.

## Exercises

### 1. Noise decomposition
For $\nabla L=3$ and mini-batch gradient 5, what is $\xi_B$?
<details><summary>Show solution</summary>

It is $5-3=2$.
</details>

### 2. Quadratic flow
Find the gradient-flow solution for $L(\theta)=\theta^2$ and $\theta_0=2$.
<details><summary>Show solution</summary>

Since $\dot\theta=-2\theta$, the solution is $\theta(t)=2e^{-2t}$.
</details>

### 3. Euler stability
For gradient descent on $L(\theta)=a\theta^2/2$ to converge along the scalar direction, $|1-\eta a|<1$ is required. For $a>0$, find the range of $\eta$.
<details><summary>Show solution</summary>

Since $0<\eta a<2$, the range is $0<\eta<2/a$.
</details>

### 4. Diagnosing an approximation
What problem does large lag-1 autocorrelation in gradient noise pose for a white-noise SDE approximation?
<details><summary>Show solution</summary>

A continuous approximation assuming independent increments loses temporal correlation. Colored noise or an augmented state may be needed.
</details>

## Evidence and update boundaries

The continuous-time analyses of [Mandt et al.](https://www.jmlr.org/papers/v18/17-214.html) and [Li et al.](https://www.jmlr.org/papers/v20/17-526.html) provide the starting point for the assumptions and limitations of SGD diffusion approximations. These results are not automatically applied to every deep-network training regime.

## Lesson summary

- SGD can be decomposed into a mean gradient and sampling noise.
- Gradient flow is a continuous-time idealization of the mean drift.
- A diffusion approximation requires assumptions about noise covariance and scaling.
- Measurements of finite steps, state, and autocorrelation delimit the approximation's scope.

## Pass criteria

- Can you separate drift and noise in an SGD update?
- Can you name at least three diagnostics required for a continuous-time approximation?

## Next lesson

- [A09-DYN-08 Capstone exercise: learning trajectory analysis](A09-DYN-08-capstone-learning-trajectories.md)

## Author checklist

- [x] Application conditions and failure modes of continuous-time approximations are explained.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
