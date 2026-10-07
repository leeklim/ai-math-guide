---
id: "A09-DYN-01"
title: "Differential equations and flows"
part: 4
stage: "A09-DYN"
status: "complete"
prerequisites: ["M01-03", "M01-06", "M03-10"]
estimated_time: "90–120 minutes"
---

# A09-DYN-01. Differential equations and flows

## Why this lesson matters

Viewing learning as only a list of parameter updates misses its structure over time. An ordinary differential equation describes a system in which the current state determines the instantaneous rate of change. A flow is a map describing how the collection of initial conditions moves over time.

## Learning objectives

- Distinguish the state from the vector field of an autonomous ODE.
- Distinguish a solution trajectory from a flow map.
- Relate Euler discretization to gradient descent.
- Explain why existence and uniqueness assumptions are needed.

## Prerequisite check

- Prerequisite lessons: [M01-03 Derivatives](../../part-1-foundations/M01/M01-03-derivative-instantaneous-rate.md), [M01-06 The chain rule](../../part-1-foundations/M01/M01-06-composition-chain-rule.md), [M03-10 Total derivatives](../../part-1-foundations/M03/M03-10-total-derivative-differential.md)
- Check question: What does it mean for a derivative to be a function of the current state?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\dot x=f(x)$ | `x dot equals f of x` | Autonomous ODE | $x\in\mathbb R^d$ |
| $x(t;x_0)$ | `x at time t given x naught` | Trajectory with initial value $x_0$ | vector |
| $\Phi_t(x_0)$ | `Phi sub t of x naught` | Time-$t$ flow map | state to state |
| $h$ | `h` | Discretization step | positive scalar |

## Core concepts

### State and vector field

In the autonomous ODE

$$
\dot x(t)=f(x(t)),\qquad x(0)=x_0
$$

the vector $x(t)\in\mathbb R^d$ is the state at time $t$, and $\dot x(t)$ collects the instantaneous rates of change of its components. The vector field $f:\mathbb R^d\to\mathbb R^d$ determines the direction and speed of motion at a given state. It is called autonomous because the input to $f$ is the current state, not time itself. This does not mean that the system does not change over time. As $x(t)$ changes, $f(x(t))$ can change as well.

Solving the equation means finding a function $t\mapsto x(t)$ that starts at $x(0)=x_0$ and satisfies the rate-of-change condition at every time. The initial velocity $f(x_0)$ tells us the starting direction, but afterward we must reevaluate the velocity at the locations reached.

Read the state and velocity separately on the two axes below.

<figure class="lesson-figure" markdown="1">

![For dx over dt equals minus x the state axis has rightward velocity at minus two zero velocity at zero and leftward velocity at two while the lower function plot maps each state to its signed instantaneous velocity](../../figures/assets/A09-DYN/A09-DYN-01-state-velocity.svg)

<figcaption>On the upper state axis, −2 moves right and 2 moves left. The three points on f(x) = −x below show instantaneous velocities 2, 0, and −2 at those same states. The lower horizontal axis is also state x, not time t.</figcaption>

</figure>

### Trajectory and flow map

The solution $t\mapsto x(t;x_0)$ with one initial value fixed is a solution trajectory. Conversely, fixing time $t$ and varying the initial value gives the flow map $\Phi_t$, namely $x_0\mapsto x(t;x_0)$. A trajectory maps time to state; a flow map maps an initial state to a later state.

If the solution is unique and exists up to the required times, then

$$
\Phi_0(x_0)=x_0,\qquad
\Phi_{t+s}(x_0)=\Phi_t(\Phi_s(x_0))
$$

The right side first moves for time $s$, uses the resulting location as the new initial value, and moves for another time $t$. In an autonomous system, the velocity rule at the same location does not change with time, and uniqueness connects the two calculations to the same solution. Use this relation only within the time range where both sides are defined.

Compare varying time with varying the initial value in the figures below.

<figure class="lesson-figure" markdown="1">

![Three exact trajectories for dx over dt equals minus x start from two one and minus one on a time axis and approach zero without crossing the equilibrium](../../figures/assets/A09-DYN/A09-DYN-01-trajectory-time.svg)

<figcaption>Choose one x₀ and read its curve along the horizontal time axis t. For example, the blue curve with x₀ = 2 is x(t) = 2e⁻ᵗ. The other two curves are solutions with other initial conditions, not later positions of the same run.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![At fixed time one the exact flow maps every initial state x naught to e to the minus one times x naught with points minus two to minus zero point seven three six zero to zero and two to zero point seven three six](../../figures/assets/A09-DYN/A09-DYN-01-fixed-time-flow-map.svg)

<figcaption>Time is fixed at t = 1. The horizontal axis is now the initial value x₀, and the vertical axis is the state reached one time unit later from that value. The map with slope e⁻¹ contracts both positive and negative initial values toward 0.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Two successive time-one contractions take initial state two to about zero point seven three six then about zero point two seven one while a direct time-two route arrives at the same final state](../../figures/assets/A09-DYN/A09-DYN-01-flow-composition.svg)

<figcaption>The two routes are compared with s = t = 1 and x₀ = 2. The left route inserts the first destination as a new initial value; the right route applies Φ₂ once to the original state. Reaching the same final box expresses the flow composition relation.</figcaption>

</figure>

### The Euler method and gradient descent

The Euler method approximates a continuous trajectory by

$$
x_{k+1}=x_k+h f(x_k)
$$

This follows by substituting $\dot x(t)=f(x(t))$ into the first-order derivative approximation $x(t+h)\approx x(t)+h\dot x(t)$. The Euler method holds velocity at its starting value $f(x_k)$ throughout one step. In the actual solution, velocity can change at intermediate locations, so a finite step is not the same as the exact flow.

If $f(\theta)=-\nabla L(\theta)$, the update becomes $\theta_{k+1}=\theta_k-h\nabla L(\theta_k)$, identifying $h$ with the learning rate of gradient descent. This correspondence is for updates using the exact gradient of the same loss. Optimizers with momentum or stochastic sampling require separate treatment of their state and noise.

The curve and tangent below show the different endpoints of one Euler step and the exact solution.

<figure class="lesson-figure" markdown="1">

![Exact solution e to the minus t and the initial tangent one minus t meet at time zero but at step h one half the Euler state one half lies below the exact state about zero point six zero seven](../../figures/assets/A09-DYN/A09-DYN-01-euler-tangent-step.svg)

<figcaption>This illustrative step uses a = 1, x₀ = 1, and h = 0.5. Euler holds the initial velocity at −1 and reaches x₁ = 0.5, but the exact solution reaches e⁻⁰·⁵ ≈ 0.607. The two calculations share their starting point and tangent slope, not their finite-step endpoint.</figcaption>

</figure>

### Existence, uniqueness, and the time domain

For a flow map to have a single well-defined output, a solution starting at the initial value must exist and be unique. A standard sufficient condition is that $f$ be locally Lipschitz near the initial value. This means that there is a finite $K$ such that $\|f(u)-f(v)\|_2\le K\|u-v\|_2$ for two states $u,v$ in that neighborhood. It limits how much the velocity difference can increase relative to a small state difference. A function $f$ with continuous first partial derivatives satisfies this local condition.

This condition guarantees existence and uniqueness for a short time, not existence for all time. For example, the solution $x(t)=x_0/(1-x_0t)$ of $\dot x=x^2$ with $x_0>0$ diverges at $t=1/x_0$. When using $\Phi_t$, therefore, also check that the solution from the specified initial value exists up to time $t$.

The time boundary below distinguishes local existence from existence for all time.

<figure class="lesson-figure" markdown="1">

![For initial state one the exact solution one divided by one minus t of dx over dt equals x squared grows without bound as time approaches one and the plot marks time one as outside the forward solution domain](../../figures/assets/A09-DYN/A09-DYN-01-finite-time-boundary.svg)

<figcaption>The solution in the existing example with x₀ = 1 is x(t) = 1/(1 − t). Although f(x) = x² is smooth, the forward solution for this initial value does not exist up to t = 1. The dashed line marks a finite-time boundary, not a state reached by the solution.</figcaption>

</figure>

## Small example

The solution of $\dot x=-ax$ with $a>0$ is $x(t)=x_0e^{-at}$. Differentiating gives $\dot x(t)=-ax_0e^{-at}=-ax(t)$, and $x(0)=x_0$, so it satisfies both the ODE and the initial value. The flow is $\Phi_t(x_0)=e^{-at}x_0$, which contracts every initial value toward 0 for $t>0$.

The Euler step for the same system is $x_{k+1}=(1-ah)x_k$. Comparing this with the exact one-step multiplier $e^{-ah}$ shows the first-order approximation $e^{-ah}\approx1-ah$. The continuous solution's multiplier is positive, but if $ah>1$, the Euler multiplier is negative and the sign alternates. Correspondence between small-step formulas must be distinguished from agreement in long-term behavior.

Compare the continuous solution and the sign changes of Euler on the same time axis below.

<figure class="lesson-figure" markdown="1">

![Exact positive exponential decay is compared with Euler points at step one point five whose multiplier minus one half makes states one minus one half one quarter and minus one eighth alternate around zero](../../figures/assets/A09-DYN/A09-DYN-01-euler-alternating-sign.svg)

<figcaption>For a = 1 and h = 1.5, the Euler multiplier is 1 − ah = −0.5. Its states change sign through 1, −0.5, 0.25, and −0.125, while the exact e⁻ᵗ is always positive. In this example, the Euler magnitudes also decrease; this does not mean that every large step diverges.</figcaption>

</figure>

## Common misconceptions

- A vector field is the velocity rule for all possible states, not a single trajectory.
- Even a small learning rate does not automatically give a discrete optimizer and an ODE the same long-term behavior.

## Exercises

### 1. Checking a solution
Check that $x(t)=x_0e^{2t}$ satisfies $\dot x=2x$.
<details><summary>Show solution</summary>

It does, since $\dot x=2x_0e^{2t}=2x(t)$ and $x(0)=x_0$.
</details>

### 2. Flow property
For $\Phi_t(x)=e^{-t}x$, show that $\Phi_t(\Phi_s(x))=\Phi_{t+s}(x)$.
<details><summary>Show solution</summary>

We have $e^{-t}(e^{-s}x)=e^{-(t+s)}x$.
</details>

### 3. Euler step
Find the first step for $\dot x=-x$, $x_0=1$, and $h=0.1$.
<details><summary>Show solution</summary>

It is $x_1=1+0.1(-1)=0.9$.
</details>

### 4. Interpreting learning
State two items to record before interpreting an optimizer log as an ODE trajectory.
<details><summary>Show solution</summary>

Record the actual step size schedule and the optimizer state and update rule. The sampling rule for stochastic gradients is also needed.
</details>

## Sources and update boundaries

The ODE, flow, and Euler method follow standard definitions in dynamical systems. The local Lipschitz condition and the definition of a local flow were checked against [CMU's lecture notes on existence and uniqueness](https://www.math.cmu.edu/~gautam/c/2026-632/notes/existence.html). This lesson does not cover the proof of the Picard–Lindelöf theorem.

## Lesson summary

- A vector field determines velocity at each state.
- A trajectory is the solution for one initial value; a flow is the map moving the collection of initial values.
- The Euler method approximates an ODE with discrete updates.
- Agreement between an optimizer and a continuous-time model requires assumptions and error analysis.

## Pass criteria

- Can you distinguish an ODE, a trajectory, and a flow?
- Can you calculate an Euler update and state the limits of the approximation?

## Next lesson

- [A09-DYN-02 Fixed points and linear stability](A09-DYN-02-fixed-points-linear-stability.md)

## Author checklist

- [x] The types of ODEs and flows are distinguished.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
