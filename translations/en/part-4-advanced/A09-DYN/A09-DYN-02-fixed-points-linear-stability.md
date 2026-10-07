---
id: "A09-DYN-02"
title: "Fixed points and linear stability"
part: 4
stage: "A09-DYN"
status: "complete"
prerequisites: ["A09-DYN-01", "M02-11", "M03-11"]
estimated_time: "90–120 minutes"
---

# A09-DYN-02. Fixed points and linear stability

## Why this lesson matters

To understand which states learning or recurrent computation remains near, we need to examine fixed points and whether perturbations around them grow or shrink. Jacobian eigenvalues assess the local stability of nonlinear dynamics through a first-order approximation.

## Learning objectives

- Write the fixed-point conditions for continuous and discrete systems.
- Calculate a Jacobian linearization.
- Assess the local stability of a hyperbolic fixed point using eigenvalues.
- Explain why linearization cannot settle stability in a non-hyperbolic case.

## Prerequisite check

- Prerequisite lessons: [A09-DYN-01 Differential equations and flows](A09-DYN-01-odes-flows.md), [M02-11 Eigenvalues](../../part-1-foundations/M02/M02-11-eigenvalues-eigenvectors.md), [M03-11 Jacobians](../../part-1-foundations/M03/M03-11-jacobian.md)
- Check question: How do eigenvalue magnitudes affect repeated application of a matrix through its powers?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $x^*$ | `x star` | Fixed point | state |
| $A=Df(x^*)$ | `A equals D f at x star` | Linearization matrix | $d\times d$ |
| $\lambda_i(A)$ | `lambda sub i of A` | Eigenvalue of $A$ | complex scalar |
| $\delta x$ | `delta x` | Perturbation around a fixed point | vector |

## Core concepts

### Fixed points and perturbations

A fixed point of a continuous system $\dot x=f(x)$ satisfies $f(x^*)=0$. Its velocity is zero, so the constant function $x(t)=x^*$ is a solution. For a discrete map $x_{k+1}=F(x_k)$, the condition $F(x^*)=x^*$ plays the same role. In a continuous system, check that the rate of change is zero; in a discrete system, check that the state is unchanged after an update.

Finding a fixed point and assessing its stability are different tasks. Local asymptotic stability means that solutions from sufficiently close initial values remain near the point and converge to it over time. The condition that a state placed exactly at the point stops does not tell us whether nearby solutions converge.

The two intersections below express different stopping conditions for continuous and discrete systems.

<figure class="lesson-figure" markdown="1">

![Upper axes find the zero of velocity minus three x while lower axes find the intersection of discrete map one half x with the identity line; both stop at state zero but use different tests](../../figures/assets/A09-DYN/A09-DYN-02-fixed-point-checks.svg)

<figcaption>The upper plot finds zero velocity in the existing −3x example; the lower plot finds the intersection of the existing 0.5x map with the identity. Both give x* = 0, but the continuous system checks for vertical value 0, while the discrete system checks for a vertical value equal to the input. These are stopping conditions; convergence nearby is assessed separately.</figcaption>

</figure>

### Jacobian linearization

Write $x=x^*+\delta x$, where $\delta x$ is the displacement from the fixed point. Since $x^*$ does not move with time, $\dot{\delta x}=\dot x$. Assuming that $f$ has continuous second partial derivatives in a neighborhood, its Taylor expansion gives

$$
\dot{\delta x}=Df(x^*)\delta x+O(\|\delta x\|^2).
$$

The term $f(x^*)$ vanishes by the fixed-point condition. With $A=Df(x^*)$, the remaining first-order expression is $\dot{\delta x}\approx A\delta x$. The notation $O(\|\delta x\|^2)$ means that the magnitude of the omitted terms is bounded in a neighborhood by a constant times $\|\delta x\|^2$. If $f$ has only continuous first partial derivatives, use a first-order approximation whose remainder, divided by the displacement magnitude, tends to zero, rather than this quadratic-order bound.

Compare the results of adding the same displacement to each fixed point in the local coordinates below.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Three displacement plots for x minus x cubed around fixed states minus one zero and one compare exact velocities with local lines minus two delta x delta x and minus two delta x](../../figures/assets/A09-DYN/A09-DYN-02-cubic-localization.svg)

<figcaption>The horizontal axis of each panel is δx from its own x*, not the original x. The exact f(x* + δx) and the tangent Aδx meet at the origin, with A = −2 at ±1 and A = 1 at 0. Farther away, the difference between the first-order expression and the actual curve becomes visible.</figcaption>

</figure>

### Continuous and discrete stability criteria

In an eigenvector direction of a continuous linear system, the perturbation coefficient $c(t)$ satisfies $\dot c=\lambda c$, so $c(t)=c(0)e^{\lambda t}$. The imaginary part of a complex eigenvalue corresponds to rotation or oscillation, while its real part determines exponential growth or decay in magnitude. If every eigenvalue has negative real part, the fixed point of the nonlinear system is also locally asymptotically stable. If any eigenvalue has positive real part, the fixed point is unstable. This local assessment assumes that $f$ is continuously differentiable in a neighborhood.

For a discrete map, likewise assume that $F$ is continuously differentiable near the fixed point. With $B=DF(x^*)$, we have $\delta x_{k+1}\approx B\delta x_k$. The coefficient in an eigenvector direction is multiplied by $\lambda$ on each iteration, giving $c_k=\lambda^kc_0$. Thus, if every eigenvalue has magnitude less than 1, the fixed point is locally asymptotically stable; if any has magnitude greater than 1, it is unstable. This criterion concerns long-term convergence. For a general matrix, it does not mean that the Euclidean norm decreases at every step: some perturbations can grow before converging.

A fixed point is called hyperbolic if no eigenvalue has real part zero in the continuous case, or magnitude 1 in the discrete case. Under this condition, linearization can identify stable and unstable directions. A single Jacobian calculated nearby does not determine the behavior of distant initial values.

Read the time multipliers, assessment regions in the complex plane, and initial norm changes separately below.

<figure class="lesson-figure" markdown="1">

![Starting coefficient one evolves as exp of minus t for eigenvalue minus one and exp of two t for eigenvalue two showing decaying and growing continuous modes](../../figures/assets/A09-DYN/A09-DYN-02-continuous-eigenmodes.svg)

<figcaption>The two eigenmodes in the existing diag(−1, 2) exercise are compared with c(0) = 1 for each. The first direction decays as e⁻ᵗ, while the second grows as e²ᵗ. Assessing stability of the full state requires checking all directions, not just one decaying direction.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Illustrative discrete eigenmodes with multipliers one half minus one half and one point two show monotone decay alternating decay and growing amplitude from the same initial coefficient one](../../figures/assets/A09-DYN/A09-DYN-02-discrete-eigenmodes.svg)

<figcaption>The illustrative multipliers 0.5, −0.5, and 1.2 are iterated from the same c₀ = 1. Even a negative multiplier produces decay with alternating signs if its magnitude is less than 1. The mode with 1.2 grows because its magnitude exceeds 1, not because it is positive.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Complex eigenvalue plane shades the open left half plane for continuous decay and marks the imaginary axis as the zero-real-part boundary rather than part of the strict stability region](../../figures/assets/A09-DYN/A09-DYN-02-continuous-stability-region.svg)

<figcaption>The horizontal axis is Re λ, and the vertical axis is Im λ. The green region Re λ &lt; 0 gives exponential decay in the magnitude of a continuous eigenmode; the dashed axis Re λ = 0 is excluded from this sufficient condition. A nonzero imaginary part does not prevent decay in the left half-plane.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Complex multiplier plane shades the open unit disk for discrete decay with dashed radius-one boundary and a marked multiplier zero point five plus zero point five i inside the disk](../../figures/assets/A09-DYN/A09-DYN-02-discrete-stability-region.svg)

<figcaption>For a discrete system, check whether the distance |λ| from the origin is less than 1. The example λ = 0.5 + 0.5i has positive real part but |λ| = √0.5 &lt; 1, so its mode decays. The dashed unit circle is the boundary of the strict criterion.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Illustrative nonnormal matrix with rows one half three and zero one half iterated from vector zero one makes Euclidean norm grow from one to about three before eventually decaying despite both eigenvalues one half](../../figures/assets/A09-DYN/A09-DYN-02-transient-norm-growth.svg)

<figcaption>The illustrative B = [[0.5, 3], [0, 0.5]] is iterated from δx₀ = (0, 1). The first resulting state is (3, 0.5), so the norm grows from 1 to about 3.04. Both eigenvalues are 0.5, and convergence follows later. The spectral criterion differs from Euclidean norm contraction at every step.</figcaption>

</figure>

### Boundary eigenvalues and higher-order terms

Along a boundary-eigenvalue direction, linearization may not determine whether a perturbation decays or grows. For example, both $\dot x=-x^3$ and $\dot x=x^3$ have derivative zero at 0. In the first system, positive states decrease and negative states increase toward 0, while the second system moves away from 0 on both sides. The same first-order expression can thus lead to different stability depending on the sign of higher-order terms.

Even with a boundary eigenvalue, another direction with positive real part or magnitude greater than 1 can establish instability on its own. Judgment needs to be withheld only when linearization does not settle stability. In gradient flow, $Df=-\nabla^2 L$, so a zero Hessian eigenvalue corresponds to such a boundary direction.

The state axes below show how the same zero derivative can coexist with different neighboring flows.

<figure class="lesson-figure" markdown="1">

![Two state phase lines show minus x cubed pointing toward zero from both sides and plus x cubed pointing away from zero while both have derivative zero at the fixed state](../../figures/assets/A09-DYN/A09-DYN-02-boundary-cubic-directions.svg)

<figcaption>Both systems have derivative zero at 0. The upper −x³ flows toward 0 from both sides, while the lower x³ flows outward on both sides. The same first-order information, boundary eigenvalue 0, cannot distinguish these two higher-order behaviors.</figcaption>

</figure>

## Small example

For $\dot x=x-x^3$, solving $f(x)=x(1-x^2)=0$ gives fixed points $-1,0,1$. Since $f'(x)=1-3x^2$, perturbations near $0$ grow according to $\dot{\delta x}\approx\delta x$, while those near $\pm1$ shrink according to $\dot{\delta x}\approx-2\delta x$. Thus, $0$ is unstable and $\pm1$ are locally asymptotically stable.

## Common misconceptions

- A zero loss gradient alone does not guarantee a minimum or a stable point.
- Jacobian eigenvalues do not tell us the size of a global basin.

## Exercises

### 1. Continuous stability
Find the fixed point and its stability for $\dot x=-3x$.
<details><summary>Show solution</summary>

The fixed point is $x^*=0$. Since its derivative is $-3<0$, it is locally asymptotically stable.
</details>

### 2. Discrete stability
Find the fixed point and multiplier for $x_{k+1}=0.5x_k$.
<details><summary>Show solution</summary>

The fixed point is $x^*=0$, and the multiplier is $0.5$. Its magnitude is less than 1, so the point is stable.
</details>

### 3. Saddle
Is 0 stable in the linear system with $A=\operatorname{diag}(-1,2)$?
<details><summary>Show solution</summary>

No. The second-direction eigenvalue is positive, so perturbations grow exponentially in that direction: the point is a saddle.
</details>

### 4. Interpreting learning
Why is it difficult to settle gradient-flow stability by linearization alone at a stationary point with a singular Hessian?
<details><summary>Show solution</summary>

There is no first-order change in a zero-eigenvalue direction, so higher-order loss geometry can determine its behavior.
</details>

## Sources and update boundaries

Fixed-point linearization and the hyperbolic stability criterion follow standard results in dynamical systems. Center manifold theory is outside the scope of this lesson.

## Lesson summary

- A fixed point is a state where the dynamics stop.
- The Jacobian gives a first-order approximation to perturbation dynamics near a fixed point.
- Continuous systems use real parts; discrete systems use magnitudes.
- Boundary eigenvalues require higher-order analysis.

## Pass criteria

- Can you find the fixed points and assess stability in a simple nonlinear system?
- Can you distinguish the continuous and discrete assessment criteria?

## Next lesson

- [A09-DYN-03 Phase portraits and bifurcations](A09-DYN-03-phase-portrait-bifurcation.md)

## Author checklist

- [x] The conditions and limits of linear stability analysis are stated.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
