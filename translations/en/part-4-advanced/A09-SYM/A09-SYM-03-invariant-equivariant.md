---
id: "A09-SYM-03"
title: "Invariance and equivariance"
part: 4
stage: "A09-SYM"
status: "complete"
prerequisites: ["A09-SYM-01", "M03-04"]
estimated_time: "90–120 minutes"
---

# A09-SYM-03. Invariance and equivariance

## Why this lesson matters

Whether an output should stay unchanged or change correspondingly when the input is transformed depends on the task. Distinguishing invariance from equivariance lets us state the assumptions behind data augmentation, architectural constraints, and representation metrics precisely.

## Learning objectives

- Write the equations for invariant and equivariant maps.
- Specify the input and output actions.
- Explain how averaging constructs an invariant.
- Distinguish empirical invariance from an architectural guarantee.

## Prerequisite check

- Prerequisite lessons: [A09-SYM-01 Groups and actions](A09-SYM-01-groups-actions.md), [M03-04 Invariants and equivariance](../../part-1-foundations/M03/M03-04-invariants-equivariance.md)
- Check question: When rotating an image, how should its class label and segmentation mask each change?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $f(g\cdot x)=f(x)$ | `f of g acting on x equals f of x` | Invariance | unchanged output |
| $f(g\cdot x)=\rho(g)f(x)$ | `f of g acting on x equals rho of g acting on f of x` | Equivariance | transformed output |
| $\rho(g)$ | `rho of g` | Output-space action | linear or nonlinear map |
| $\bar f(x)$ | `f bar of x` | Group-averaged function | invariant summary |

## Core concepts

### Specify input and output actions separately

For $f:X\to Y$, the notation $g\cdot x$ is an action on $X$, while $\rho(g)$ specifies how the same group element acts on $Y$. If the output action is linear, read $\rho(g)f(x)$ as matrix multiplication; for a general map, read it as function application $\rho(g)(f(x))$. The two spaces need not have the same dimension, and the matrices of their actions need not be the same.

An invariant map satisfies $f(g\cdot x)=f(x)$ for every permitted $g,x$. Because it assigns the same value throughout an input orbit, it defines a function on the quotient that assigns $f(x)$ to $[x]$. This is possible because replacing representative $x$ with another point in the same orbit does not change the function value.

An equivariant map satisfies $f(g\cdot x)=\rho(g)f(x)$. Calculating after transforming the input agrees with transforming the output after calculating. An image transformation meant to preserve a class label can require an unchanged output; a transformation meant to move a segmentation mask correspondingly requires the appropriate output action. The task must first determine which transformations change the meaning of the label.

Distinguish the output actions required for the same input transformation.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Swapping vector (1,3) changes identity-map output to (3,1) but leaves the scalar sum at four, with distinct output-space actions.](../../figures/assets/A09-SYM/A09-SYM-03-input-output-action-types.svg)

<figcaption>Under the same input swap, the sum function keeps scalar output 4, while the identity map changes its vector output from (1,3) to (3,1). The first output action is the identity and the second is P. Input and output need not have the same type or dimension.</figcaption>
</figure>

### Equivariance is not the same as information preservation

With the identity as the output action, the equivariance equation becomes the invariance equation. General equivariant features can retain components that move with a transformation, followed by invariant pooling to produce the task output. Equivariance itself does not, however, guarantee that $f$ is one-to-one or that the original input can be reconstructed. Under a linear output action, even the zero map is equivariant. Check the transformation correspondence and the amount of information loss separately.

For a linear map $f(x)=Ax$ with input and output permutations, the two calculation routes are $A P_{\mathrm{in}}x$ and $P_{\mathrm{out}}Ax$. Agreement for every $x$ requires $AP_{\mathrm{in}}=P_{\mathrm{out}}A$. If the same $P$ is used for input and output, this reduces to $AP=PA$.

Check agreement between the two routes separately from preservation of input information.

<figure class="lesson-figure" markdown="1">

![The zero map sends (1,3) and its coordinate-swap to the same zero vector, which the output permutation fixes, despite losing all input information.](../../figures/assets/A09-SYM/A09-SYM-03-equivariant-zero-map.svg)

<figcaption>The zero map sends every input to (0,0), which the output permutation also leaves unchanged. It satisfies f(Px)=Pf(x), but cannot reconstruct the input. Transformation correspondence and one-to-one mapping are different conditions.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![For A=diag(2,1), input swap then A yields (6,1), while A then output swap yields (3,2), so the two paths fail to commute.](../../figures/assets/A09-SYM/A09-SYM-03-linear-commutation-failure.svg)

<figcaption>For A=diag(2,1) with the same input and output swap P, the two routes differ, giving (6,1) and (3,2). To have APx=PAx for every x, we need AP=PA. With different input and output actions, the general condition is AP_in=P_out A.</figcaption>
</figure>

### Why a group average produces the same value

For a finite group, consider a function $f$ taking scalar values or values in the same vector space. If addition and averaging are defined in that space, then

$$
\bar f(x)=\frac1{|G|}\sum_{g\in G}f(g\cdot x)
$$

is invariant. Applying another group element $h$ to the input gives

$$
\bar f(h\cdot x)
=\frac1{|G|}\sum_{g\in G}f((gh)\cdot x)
=\bar f(x).
$$

The map $g\mapsto gh$ is an invertible rearrangement: as $g$ runs through the entire group once, $gh$ does as well. Only the order of terms in the sum changes, leaving its value unchanged. The original $f$ need not be invariant. The essential condition is uniform averaging over the entire group. Averaging only selected augmentations or using unequal weights does not permit this calculation unchanged. For outputs such as class names, where addition is undefined, first specify what is to be averaged, such as scores.

Check how uniform averaging rearranges the terms and what the weight condition requires.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Averaging f(x) and f(-x) for f(z)=z+z² gives four at both x=2 and x=-2 because the same two values six and two are exchanged.](../../figures/assets/A09-SYM/A09-SYM-03-group-average-reindexing.svg)

<figcaption>For the mathematical example f(z)=z+z², the two group elements give values 6 and 2. Applying −1 to the input exchanges the two terms from the full group, but the sum remains unchanged and the average remains 4. This is a two-element instance of the argument that g↦gh rearranges the entire group.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![Uniform averaging of f(x)=x+x² over the sign group is even, while weights three-quarters and one-quarter give x²+x/2 and different values at x=2 and x=-2.](../../figures/assets/A09-SYM/A09-SYM-03-unequal-average.svg)

<figcaption>The uniform average is x², the same at x and −x, but changing the weights to 3/4 and 1/4 gives x²+x/2. This yields 3 at −2 and 5 at 2, so it is not invariant under the sign action. Check that the entire group is averaged with equal weights.</figcaption>
</figure>

### Empirical observations and structural guarantees

Observing only small changes on training data is approximate empirical invariance. This differs in evidential strength from an architecture-level identity for all group elements.

An empirical check measures the difference between $f(g\cdot x)$ and $f(x)$, or between $f(g\cdot x)$ and $\rho(g)f(x)$, for specified $x,g$. The latter comparison must put the outputs into corresponding coordinates. A small measured value describes the error within the tested range. An architecture-level guarantee requires evidence that layers and their composition rules satisfy the equation for all permitted inputs and transformations. Training with augmentation does not by itself establish this identity.

Distinguish checks on finitely many inputs from an identity for all inputs.

<figure class="lesson-figure" markdown="1">

![For f(x)=x(x²-1), the sign-invariance difference vanishes at checked inputs -1, zero, and one but is nonzero elsewhere.](../../figures/assets/A09-SYM/A09-SYM-03-finite-check-misses-violation.svg)

<figcaption>In this mathematical counterexample, f(−x)−f(x) is 0 at the three specified inputs x=−1,0,1, but differs at other inputs. These are not measurements from a trained model; the example shows that finite checks alone cannot prove an identity for all inputs.</figcaption>
</figure>

## Small example

Under the coordinate permutation group, $f(x)=\sum_i x_i$ is invariant and $f(x)=x$ is equivariant under the same permutation action.

Swapping the components of $x=(1,3)^{\mathsf T}$ gives $(3,1)^{\mathsf T}$, but the sum is 4 in both cases. The identity map's output reorders both components, so $f(Px)=Pf(x)$. Taking the sum loses the ability to distinguish this order difference. The same example thus shows the different output relationships required by the two equations.

## Common misconceptions

- Invariance is not always desirable. Ignoring even task-relevant transformations loses information.
- Augmentation does not guarantee exact equivariance.

## Exercises

### 1. Invariance
Show that $f(x)=\|x\|_2$ is invariant under the orthogonal group.
<details><summary>Show solution</summary>

We have $\|Qx\|_2^2=x^\top Q^\top Qx=\|x\|_2^2$.
</details>

### 2. Equivariance
What equation must $f(x)=Ax$ satisfy to be equivariant under a permutation $P$?
<details><summary>Show solution</summary>

With the same output action, $AP=PA$ must hold for every permitted $P$.
</details>

### 3. Group average
For the sign group, explain why $\bar f(x)=[f(x)+f(-x)]/2$ is an even function.
<details><summary>Show solution</summary>

We have $\bar f(-x)=[f(-x)+f(x)]/2=\bar f(x)$.
</details>

### 4. Model evaluation
If outputs change little under test augmentations, can this be called exact invariance?
<details><summary>Show solution</summary>

No. Report it as an approximate empirical result for the specified samples and transformations, distinct from an architectural proof.
</details>

## Sources and update boundaries

Invariance, equivariance, and group averaging are standard constructions in representation theory. This lesson does not cover infinite compact groups requiring Haar integration.

- [MIT 18.702, Summing over the group](https://math.mit.edu/classes/18.702/summary-feb24.pdf): A reference for why multiplication rearranges group elements when summing over the entire group. The function-average formula in the text was derived by applying this rearrangement to the input action.

## Lesson summary

- An invariant map assigns the same value to an entire orbit.
- An equivariant map carries an input action into an output action.
- Group averaging is one way to construct an invariant.
- Distinguish empirical robustness from an exact symmetry guarantee.

## Pass criteria

- Can you check invariance and equivariance for a given map?
- Can you explain which information is preserved or removed?

## Next lesson

- [A09-SYM-04 Permutation symmetry](A09-SYM-04-permutation-symmetry.md)

## Author checklist

- [x] The output actions for invariance and equivariance are specified.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
