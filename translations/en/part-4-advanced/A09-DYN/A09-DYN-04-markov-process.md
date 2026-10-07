---
id: "A09-DYN-04"
title: "Markov processes"
part: 4
stage: "A09-DYN"
status: "complete"
prerequisites: ["M04-02", "M04-03", "M02-11"]
estimated_time: "90–120 minutes"
---

# A09-DYN-04. Markov processes

## Why this lesson matters

Treating mini-batch sampling or noisy updates as stochastic state transitions makes it possible to study distribution changes that deterministic trajectories alone cannot explain. The Markov property is a modeling assumption: conditional on the present state, the future is independent of the past.

## Learning objectives

- Write the Markov property in terms of conditional probabilities.
- Propagate a distribution one step using a transition matrix.
- Distinguish stationary distributions from detailed balance.
- Explain why the definition of state affects the validity of a Markov assumption.

## Prerequisite check

- Prerequisite lessons: [M04-02 Conditional probability](../../part-1-foundations/M04/M04-02-conditional-probability-bayes-rule.md), [M04-03 Random variables](../../part-1-foundations/M04/M04-03-random-variables-distributions.md), [M02-11 Eigenvalues](../../part-1-foundations/M02/M02-11-eigenvalues-eigenvectors.md)
- Check question: Why does conditional independence depend on which variables are conditioned on?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $X_t$ | `X sub t` | Random state at time $t$ | State-space-valued |
| $P_{ij}$ | `P sub i j` | Probability of moving from $i$ to $j$ | $[0,1]$ |
| $\pi$ | `pi` | Stationary distribution | Probability vector |
| $\pi_iP_{ij}=\pi_jP_{ji}$ | `pi sub i P sub i j equals pi sub j P sub j i` | Detailed balance | Pairwise condition |

## Core concepts

### What conditioning on the present state means

First consider discrete times $t=0,1,\ldots$ and states $X_t$. The Markov property is

$$
P(X_{t+1}\mid X_t,\ldots,X_0)=P(X_{t+1}\mid X_t)
$$

Both sides represent conditional distributions of the next state. Once the present state $X_t$ is given, additional knowledge of the past states $X_{t-1},\ldots,X_0$ does not change the distribution of the next state. This does not mean that $X_t$ and $X_{t+1}$ themselves are independent. A process can be Markov even if its next state depends strongly on its present state.

Distinguish conditioning on the present state from adding information about the past in the probability bars below.

<figure class="lesson-figure" markdown="1">

![Two different histories ending in present state one lead to the same next-state probabilities zero point eight and zero point two while present state two instead gives zero point four and zero point six](../../figures/assets/A09-DYN/A09-DYN-04-conditioned-next-law.svg)

<figcaption>For the existing P, when Xₜ = 1, the next distribution is (0.8, 0.2), whether the past path was 2 → 1 or 1 → 1. But when the present state is 2, it is (0.4, 0.6). Not needing additional past information is different from the present state having no effect.</figcaption>

</figure>

### Transition matrices and distribution propagation

For a finite-state chain, define $P_{ij}=P(X_{t+1}=j\mid X_t=i)$ and consider a time-homogeneous system in which this value does not depend on $t$. Each row is the next-state distribution from one source state, so $P_{ij}\ge0$ and $\sum_jP_{ij}=1$. The Markov property and time homogeneity are separate conditions. A Markov process can have transition rules that change over time.

Writing the current distribution as a row vector $p_t$, the law of total probability gives

$$
p_{t+1}(j)=\sum_i p_t(i)P_{ij},\qquad p_{t+1}=p_tP
$$

This sums the probability entering state $j$ over every possible source state $i$. One run visits a single state, while $p_t$ describes state probabilities across possible runs. Under the row-distribution convention, the multiplication order is $p_tP$.

Use the two figures below to read outgoing probabilities in each row and the mass summed at each destination.

<figure class="lesson-figure" markdown="1">

![Two-state transition graph has self probabilities zero point eight and zero point six and cross probabilities zero point two from one to two and zero point four from two to one so outgoing probabilities from each source sum to one](../../figures/assets/A09-DYN/A09-DYN-04-transition-row-graph.svg)

<figcaption>An arrow's source is a row of P, and its destination is a column. The two outgoing probabilities from state 1 are 0.8 + 0.2; those from state 2 are 0.4 + 0.6. Each sum is 1. Returning to the same state is also part of the next-state distribution.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Illustrative equal source masses each one half split by transition rows into four edge masses zero point four zero point one zero point two zero point three whose destination sums are zero point six and zero point four](../../figures/assets/A09-DYN/A09-DYN-04-incoming-mass-sum.svg)

<figcaption>The illustrative pₜ = (0.5, 0.5) is propagated through the existing P. Next state 1 receives mass 0.4 from source 1 and mass 0.2 from source 2. Next state 2 also sums contributions 0.1 and 0.3 from the two sources. These are the component-wise sums in the row-vector product pₜP.</figcaption>

</figure>

### Stationarity and detailed balance

A stationary distribution is a probability vector $\pi$ satisfying $\pi=\pi P$. Starting from this distribution gives the same distribution at the next step; it does not mean that the chain actually stops. The overall distribution can remain unchanged while the chain moves between states.

Detailed balance requires $\pi_iP_{ij}=\pi_jP_{ji}$ for every pair of states. The left side is the probability of moving from $i$ to $j$ in one step under the stationary distribution, and the right side is the reverse probability. Summing over $i$ gives

$$
(\pi P)_j=\sum_i\pi_iP_{ij}
=\pi_j\sum_iP_{ji}=\pi_j
$$

The final sum adds the entries of $P$ in row $j$, so it is 1. Detailed balance therefore guarantees stationarity. The converse does not hold. In a chain moving only in the cycle $1\to2\to3\to1$, the uniform distribution is stationary, but the probability flow from $1\to2$, for example, is $1/3$, whereas that from $2\to1$ is 0. Detailed balance fails.

Also distinguish the existence of a stationary distribution from convergence starting at another distribution. A chain that alternates between two states has stationary distribution $(1/2,1/2)$, but a distribution starting at $(1,0)$ repeats $(0,1)$ and $(1,0)$. A stationary equation alone does not justify claims about convergence or mixing speed.

The figures below separate distribution preservation, pairwise cancellation, and convergence from another initial distribution.

<figure class="lesson-figure" markdown="1">

![Two stationary state masses two thirds and one third exchange opposite nonzero probability fluxes two fifteenths in each direction while preserving the total state distribution](../../figures/assets/A09-DYN/A09-DYN-04-stationary-pair-flux.svg)

<figcaption>This uses π from the existing small example. Movement probabilities in the two directions are each 2/15, not 0, but cancel each other. Preserving the overall distribution is different from keeping the state of one run motionless.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Deterministic directed cycle from state one to two to three to one preserves uniform one-third state masses but all forward pair fluxes one third have reverse flux zero](../../figures/assets/A09-DYN/A09-DYN-04-stationary-directed-cycle.svg)

<figcaption>This is the 1 → 2 → 3 → 1 cycle in the text. Each state sends mass 1/3 out in one step and receives the same 1/3, preserving the uniform distribution. But each pair's reverse flow is 0, so detailed balance does not hold.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![For deterministic two-state alternation starting from distribution one zero the probability of state one alternates between one and zero at integer steps while the stationary probability one half is a separate constant line](../../figures/assets/A09-DYN/A09-DYN-04-periodic-distribution.svg)

<figcaption>The alternating two-state chain in the text starts at p₀ = (1, 0). State 1's probability alternates between 1 and 0 rather than converging to the stationary value 1/2. The green line is the invariant distribution obtained by choosing the different initial distribution π = (1/2, 1/2).</figcaption>

</figure>

### Defining the state of an optimizer

In momentum SGD, the next parameters depend on the current parameters and accumulated velocity. Two runs at the same parameters can make different next updates if their velocities differ. Recording only parameters can therefore leave the past with additional predictive information. Adam's two moments play the same role. Including parameters and the necessary optimizer state together allows the next update to be described from the current state.

The sampling rule must also be checked. Drawing batches independently at each step differs from shuffling so that each sample is visited once per epoch. In the latter case, remaining samples or their order can affect the next-batch distribution. If the schedule depends on the step number, describe time-dependent transitions or include the step number in the state. Adding optimizer moments alone does not account for all memory in sampling and schedules.

Inspect why the next update can differ at the same parameters in the augmented-state coordinates below.

<figure class="lesson-figure" markdown="1">

![Illustrative momentum update from two augmented states with parameter zero but velocity plus or minus one sends them to parameter minus or plus zero point zero nine and velocity plus or minus zero point nine](../../figures/assets/A09-DYN/A09-DYN-04-momentum-hidden-state.svg)

<figcaption>The illustrative update is v′ = 0.9v + g, θ′ = θ − 0.1v′, with θ = 0 and g = 0 in both runs. If v = 1, then θ′ = −0.09; if v = −1, then θ′ = 0.09. Matching parameters alone is insufficient to determine the next update.</figcaption>

</figure>

## Small example

For $P=\begin{bmatrix}0.8&0.2\\0.4&0.6\end{bmatrix}$, write $\pi=(q,1-q)$. Stationarity of the first component requires $q=0.8q+0.4(1-q)$. Solving $0.6q=0.4$ gives $q=2/3$, so $\pi=(2/3,1/3)$. The flow from $1\to2$ is $(2/3)(1/5)=2/15$, and that from $2\to1$ is $(1/3)(2/5)=2/15$, so detailed balance also holds. Check distribution preservation through the row-vector product and cancellation in the two directions through each pair's products.

## Common misconceptions

- Markov does not mean that states are independent.
- A stationary distribution does not mean that the chain converges quickly from every initial distribution.

## Exercises

### 1. One-step propagation
For $p_0=(1,0)$ and the $P$ above, compute $p_1$.
<details><summary>Show solution</summary>

It is $p_1=p_0P=(0.8,0.2)$.
</details>

### 2. Checking stationarity
Multiply $\pi=(2/3,1/3)$ by $P$ to check that it is stationary.
<details><summary>Show solution</summary>

The first component is $2/3\cdot0.8+1/3\cdot0.4=2/3$, and the second is $1/3$.
</details>

### 3. Markov state
Why can the past be needed in momentum SGD if only parameters are recorded?
<details><summary>Show solution</summary>

The next update depends on accumulated velocity, which cannot be recovered from parameters alone.
</details>

### 4. Stationarity
Can convergence speed be determined by checking only $\pi P=\pi$?
<details><summary>Show solution</summary>

No. Additional mixing information is needed, such as irreducibility, aperiodicity, and the transition spectrum.
</details>

## Evidence and update boundaries

The Markov property, stationarity, and detailed balance follow standard definitions in stochastic processes. Measure-theoretic kernels on general state spaces are not covered.

## Lesson summary

- The Markov property assumes that the present state contains sufficient information about the past.
- A transition matrix propagates a state distribution.
- Detailed balance is stronger than stationarity.
- The definition of optimizer state can include moments and schedules.

## Pass criteria

- Can you compute a distribution using a transition matrix?
- Can you distinguish stationarity, detailed balance, and mixing?

## Next lesson

- [A09-DYN-05 Langevin dynamics](A09-DYN-05-langevin-dynamics.md)

## Author checklist

- [x] Markov state and optimizer state are connected.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
