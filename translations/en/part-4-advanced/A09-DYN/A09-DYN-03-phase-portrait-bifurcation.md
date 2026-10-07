---
id: "A09-DYN-03"
title: "Phase portraits and bifurcations"
part: 4
stage: "A09-DYN"
status: "complete"
prerequisites: ["A09-DYN-02"]
estimated_time: "90–120 minutes"
---

# A09-DYN-03. Phase portraits and bifurcations

## Why this lesson matters

A single trajectory makes it difficult to see the behaviors possible under different initial conditions and parameters. A phase portrait summarizes the flow throughout state space, while a bifurcation marks a qualitative change in fixed points or stability as a parameter changes.

## Learning objectives

- Draw a phase line and a phase portrait.
- Define a basin of attraction.
- Analyze simple normal forms for saddle-node and pitchfork bifurcations.
- Distinguish changes at a limited number of checkpoints from a claim of a phase transition.

## Prerequisite check

- Prerequisite lesson: [A09-DYN-02 Fixed points and linear stability](A09-DYN-02-fixed-points-linear-stability.md)
- Check question: Why are the stability of one fixed point and the behavior throughout state space different kinds of information?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\mu$ | `mu` | Control parameter | scalar |
| $\mathcal B(x^*)$ | `the basin of x star` | Set of initial values converging to $x^*$ | subset of state space |
| $\dot x=\mu-x^2$ | `x dot equals mu minus x squared` | Saddle-node normal form | scalar ODE |
| $\dot x=\mu x-x^3$ | `x dot equals mu x minus x cubed` | Supercritical pitchfork form | scalar ODE |

## Core concepts

### Phase lines and phase portraits

For a one-dimensional system $\dot x=f(x)$, first mark the fixed points satisfying $f(x)=0$ on the state axis. Between those points, $f(x)>0$ means that $x$ increases, so the flow points right; $f(x)<0$ means that it points left. This is a phase line. The horizontal axis shows possible state values, not time. When solutions are unique, a trajectory does not pass through a fixed point to the other side, so read the flow in each interval together with its boundary points.

In two or more dimensions, a phase portrait displays vector-field directions, fixed points, invariant sets, and representative trajectories together. An invariant set is a set in which a solution remains if it starts there. A single fixed point is one such set. Looking at solutions from multiple initial values lets us compare where they remain or what they approach. This displays different information from a graph of one trajectory against time.

Read the directions on the state axis separately from the two-dimensional curves with different initial values below.

<figure class="lesson-figure" markdown="1">

![State phase line for x times one minus x points left for negative states right between zero and one and left above one with unstable zero open stable one filled and a marked positive-state basin](../../figures/assets/A09-DYN/A09-DYN-03-logistic-phase-line.svg)

<figcaption>The horizontal axis is state x, not time. States left of 0 flow left, while positive states on both sides of 1 flow toward 1. The open point at 0 marks a boundary where a solution starting exactly at that point remains. The initial values leading to 1 are x₀ &gt; 0.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Illustrative planar field dx over dt equals minus x dy over dt equals minus two y contains representative exact trajectories converging to zero and the horizontal axis as an invariant set](../../figures/assets/A09-DYN/A09-DYN-03-two-dimensional-portrait.svg)

<figcaption>This illustrative linear system is ẋ = −x, ẏ = −2y. The curves are exact trajectories with different initial conditions, and the small arrows show field directions. A solution starting on the dashed x-axis keeps y = 0, so that axis is an invariant set. Both axes are state components; time is not a separate axis here.</figcaption>

</figure>

### Basin of attraction

The basin of an attractor is the set of initial conditions converging to it. For a fixed point $x^*$, we write

$$
\mathcal B(x^*)=\{x_0:\ x(t;x_0)\to x^*\text{ as }t\to\infty\}
$$

This definition includes the condition that solutions exist for all positive time. Local stability concerns convergence from sufficiently close initial values; the basin describes how far away initial values can be and still approach the same point. The eigenvalues of one Jacobian cannot locate the basin boundary by themselves.

The time graph below compares several initial values within the basin with a different solution on the boundary.

<figure class="lesson-figure" markdown="1">

![Exact logistic time trajectories from positive states zero point two zero point eight and one point eight approach one from either side while the zero initial condition remains zero](../../figures/assets/A09-DYN/A09-DYN-03-logistic-basin-trajectories.svg)

<figcaption>In the same logistic system, x₀ = 0.2, 0.8, and 1.8 all approach 1. The dashed solution with x₀ = 0, however, stays at 0. These curves illustrate a few initial values; the full basin (0, ∞) was determined by checking all intervals on the preceding state axis.</figcaption>

</figure>

### Parameters and bifurcation branches

In a bifurcation analysis, we compare a family of systems $\dot x=f(x;\mu)$. Fix the control parameter $\mu$ for each trajectory, and examine how fixed points and their stability differ across values of $\mu$. The horizontal axis of a branch plotting $x^*(\mu)$ is the parameter, not time or state.

The fixed-point condition for the saddle-node normal form $\dot x=\mu-x^2$ is $x^2=\mu$. There are no real solutions when $\mu<0$; the two branches meet at 0 when $\mu=0$; and $x=\pm\sqrt\mu$ appear when $\mu>0$. The derivative is $-2x$, so the positive branch is stable and the negative branch is unstable. At $\mu=0$, the derivative is zero, so inspect the signs on the phase line directly. The flow $\dot x=-x^2$ points left on both sides: it approaches 0 from the right but moves away on the left.

The condition for the supercritical pitchfork form $\dot x=\mu x-x^3$ is $x(\mu-x^2)=0$. The state $x=0$ is a fixed point for every $\mu$, and its derivative is $\mu$. It is stable for $\mu<0$ and unstable for $\mu>0$. The additional points $x=\pm\sqrt\mu$ when $\mu>0$ have derivative $\mu-3\mu=-2\mu<0$, so both branches are stable. Exactly at $\mu=0$, confirm convergence to 0 from the signs of $\dot x=-x^3$. Do not equate a boundary case of linearization with an unstable point.

The two normal forms are worked examples in which the number or stability of fixed points changes with a parameter. A bifurcation means such a qualitative change in invariant structure, not merely a rapid change in an observed value.

Connect the branches on the parameter axis with directions on the state axis for a fixed parameter below.

<figure class="lesson-figure" markdown="1">

![Saddle-node diagram in parameter mu versus fixed state x star shows no real roots left of zero stable positive square-root branch solid and unstable negative square-root branch dashed meeting at zero](../../figures/assets/A09-DYN/A09-DYN-03-saddle-node-branches.svg)

<figcaption>The horizontal axis is control parameter μ, and the vertical axis is fixed state x*. For μ &gt; 0, the upper +√μ branch is stable and the lower −√μ branch is unstable. There are no real branches for μ &lt; 0. Do not read a curve as a trajectory over time.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Three state phase lines for saddle-node mu minus x squared at mu minus one zero and one show no root all left one-sided approach to zero and unstable minus one plus stable one respectively](../../figures/assets/A09-DYN/A09-DYN-03-saddle-node-phase-lines.svg)

<figcaption>Each row holds μ fixed. At μ = 0, f = −x² points left on both sides, so states right of 0 approach it and those on the left move away. The branch meeting therefore does not mark a point that is stable from both sides.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Supercritical pitchfork diagram shows stable zero branch for negative mu unstable zero branch for positive mu and two stable square-root branches for positive mu with nonlinear-stable critical zero marked at mu zero](../../figures/assets/A09-DYN/A09-DYN-03-pitchfork-branches.svg)

<figcaption>The 0 branch is stable for μ &lt; 0 and unstable for μ &gt; 0. Both new ±√μ branches for μ &gt; 0 are stable. Exactly at μ = 0, the derivative is zero; convergence is checked through the nonlinear directions on the next state axes.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Three state phase lines for mu x minus x cubed show all flow toward zero at mu minus one and zero but at mu one zero repels toward stable minus one and plus one](../../figures/assets/A09-DYN/A09-DYN-03-pitchfork-phase-lines.svg)

<figcaption>Both μ = −1 and μ = 0 flow toward 0 from both sides, but the latter is a boundary case with f′(0) = 0. At μ = 1, the directions near 0 turn outward, toward −1 and 1 on their respective sides. This comparison distinguishes a linearization boundary from instability.</figcaption>

</figure>

### Training checkpoints and structural changes

An increase in probe score during training is a change in a quantity measured along one optimizer path. It is not a comparison of possible trajectories and fixed points at separate fixed values of $\mu$. A bend in a metric at finite training checkpoints therefore does not establish a bifurcation. Even when comparing learning rates as a control parameter, maintain the same state and update definitions and check whether stability or attractor structure changes accordingly. A system whose schedule itself changes over time is distinct from the fixed-parameter normal forms above.

Distinguish the interpolation line from actual observations at the three points below.

<figure class="lesson-figure" markdown="1">

![Three observed probe scores zero point five zero point five and zero point nine at checkpoint indices one two and three are marked as dots while dashed interpolation is not an observed path and interval two to three contains the unlocalized change](../../figures/assets/A09-DYN/A09-DYN-03-sparse-checkpoint-observations.svg)

<figcaption>The three scores from the existing exercise are marked as observations. The dashed line only interpolates between those points; it does not observe every moment of the actual run. Only the change between the last two points is established, not invariant structure across control parameters or a bifurcation.</figcaption>

</figure>

## Small example

For $\dot x=x(1-x)$, the fixed points are 0 and 1. Velocity is positive when $0<x<1$ and negative when $x>1$, so positive initial values approach 1 from both sides. The initial value $x_0=0$ remains at 0. For $x_0<0$, velocity is negative and the solution does not approach 1. Thus, $\mathcal B(1)=(0,\infty)$. Obtaining this basin requires checking each interval on the state axis, not only the local stability of 1.

## Common misconceptions

- An elbow in a loss curve is not automatically a dynamical bifurcation.
- A phase portrait in a two-dimensional projection may not preserve the topology of the original high-dimensional dynamics.

## Exercises

### 1. Phase line
For $\dot x=x(1-x)$, state the flow directions in $x<0$, $0<x<1$, and $x>1$.
<details><summary>Show solution</summary>

The velocities are negative, positive, and negative, respectively, so the directions are left, right, and left.
</details>

### 2. Saddle-node
Find the fixed points and their stability for $\dot x=\mu-x^2$ at $\mu=4$.
<details><summary>Show solution</summary>

The fixed points are $x=\pm2$. From the derivative $-2x$, the point $-2$ is unstable and $2$ is stable.
</details>

### 3. Pitchfork
For $\mu<0$, find the real fixed points of $\dot x=\mu x-x^3$ and the stability of 0.
<details><summary>Show solution</summary>

The only fixed point is 0. Its derivative is $\mu<0$, so it is stable.
</details>

### 4. A phase-transition claim
Are probe scores $0.5,0.5,0.9$ at three checkpoints sufficient evidence for a bifurcation?
<details><summary>Show solution</summary>

No. Measurement error, checkpoint resolution, the control parameter, and invariant structure have not been checked, so report only the observed abrupt change.
</details>

## Sources and update boundaries

Phase portraits and normal forms were checked against the standard examples in [MIT's lecture notes on one-dimensional flows and bifurcations](https://ocw.mit.edu/courses/12-006j-nonlinear-dynamics-chaos-fall-2022/resources/mit12_006jf22_lec2-3/). This lesson does not cover high-dimensional bifurcation classification or chaos.

## Lesson summary

- A phase portrait summarizes possible state-space behaviors.
- A basin is the set of initial values approaching the same attractor.
- A bifurcation is a qualitative structural change with a parameter.
- A sharp metric change at sparse checkpoints is not sufficient evidence for a bifurcation.

## Pass criteria

- Can you analyze a one-dimensional phase line and a normal form?
- Can you distinguish a sharp change in a learning metric from a dynamical bifurcation?

## Next lesson

- [A09-DYN-04 Markov processes](A09-DYN-04-markov-process.md)

## Author checklist

- [x] The levels of evidence for phase portraits and bifurcations are distinguished.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
