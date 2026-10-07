---
id: "I06-10"
title: "Superposition"
part: 3
stage: "I06"
status: "complete"
prerequisites: ["I06-09", "M02-02"]
estimated_time: "110~140 minutes"
---

# I06-10. Superposition

## Why this lesson matters

When there are more features than representation dimensions, each feature cannot occupy its own orthogonal coordinate. If only a few features are active for each input, overlapping feature directions in the same space and accepting interference may be useful. This view gives a mathematical reason why neurons and features need not correspond one to one.

## Learning objectives

- Distinguish an overcomplete feature dictionary from sparse coefficients.
- Explain why an orthogonal arrangement is impossible when the number of features exceeds the dimension.
- Compute interference between feature directions using a Gram matrix.
- Avoid presenting toy-model superposition results as established facts about actual LLMs.

## Prerequisite check

- Prerequisite lessons: [I06-09 Feature visualization](I06-09-feature-visualization.md), [M02-02 Linear combinations and span](../../part-1-foundations/M02/M02-02-linear-combinations-span.md)
- Check question: Can a 2-dimensional space contain three mutually orthogonal nonzero vectors?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $D=[d_1,\ldots,d_m]$ | `dictionary D with columns d one through d m` | A dictionary with feature directions as columns | $d\times m$ |
| $z$ | `sparse feature vector z` | Coefficients of the features active for an input | $\mathbb R^m$ |
| $a=Dz$ | `a equals D z` | A representation formed by combining features | $\mathbb R^d$ |
| overcomplete dictionary | `overcomplete dictionary` | A dictionary with more columns than the ambient dimension | $m>d$ |
| $G=D^TD$ | `Gram matrix D transpose D` | Inner products between feature directions | $m\times m$ |
| interference | `feature interference` | The contribution of other features to dot-product decoding | scalar or vector |

## 1. Separate features from neurons

Call a meaningful property of an input a feature, and a representation coordinate a neuron. Given sparse feature coefficients $z$ and a dictionary $D$, we can form dense activations as

\[
a=Dz
\]

If $m>d$, there are more features than coordinates. A monosemantic arrangement with a separate coordinate for each feature is impossible, but nonorthogonal directions can store them if few features are active simultaneously.

A column of $D$ is a feature's direction, and $z_j$ is its contribution along that direction. A neuron coordinate sums the corresponding coordinate components of the active directions, so a sparse $z$ can produce a dense $a$. Mutually orthogonal nonzero directions are linearly independent; a $d$-dimensional space can therefore contain at most $d$ of them. A dictionary with $m>d$ has linear dependence, so an unconstrained $z$ cannot be recovered uniquely from $a$. Sparsity is an additional condition that restricts which combinations to consider among these candidates.

Use the same toy example to distinguish coefficient positions from coordinates of the resultant vector.

<figure class="lesson-figure" markdown="1">

![The existing toy code one zero point eight uses two of three features in a two-coordinate dictionary, yielding a dense two-coordinate activation.](../../figures/assets/I06/I06-10-feature-coordinate-shapes.svg)

<figcaption>The existing CPU code z=(1,0,0.8) uses two of three features, but both neuron coordinates have values. Sparsity of feature coefficients and sparsity of activation coordinates are different properties.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The existing 120-degree dictionary has three directions with two active contributions; head-to-tail one d one plus point eight d three produces the two-coordinate activation.](../../figures/assets/I06/I06-10-weighted-vector-sum.svg)

<figcaption>These are the directions and resultant vector of the same CPU dictionary. The coefficient of d₂ is 0, and d₁+0.8d₃ forms a. A sparse feature combination can produce dense neuron coordinates.</figcaption>
</figure>

## 2. Gram matrix and interference

When dictionary columns have unit norm, the diagonal of $G=D^TD$ is 1. An off-diagonal entry $G_{jk}=d_j^Td_k$ measures overlap between two feature directions. A simple dot-product decoder produces

\[
D^Ta=D^TDz=Gz
\]

It is exact when $G=I$, but an overcomplete dictionary cannot have all off-diagonal entries equal to 0. The difference $Gz-z$ shows interference.

Under the unit-column condition, expanding decoder output $j$ gives

\[
(D^Ta)_j=z_j+\sum_{k\ne j}G_{jk}z_k
\]

The first term is the coefficient being read; the remaining terms mix in other active features. Even a feature with $z_j=0$ may receive an output other than 0 because of these terms. Thus, $D^Ta$ reads responses along directions. It is not the same as exact sparse-coefficient recovery for a general overcomplete dictionary.

The Gram matrix's off-diagonal entries create the difference between the true code and the simple decoder's output.

<figure class="lesson-figure" markdown="1">

![The actual three by three Gram matrix of the 120-degree unit dictionary has diagonal one and all off-diagonals minus half; inactive feature two receives response minus point nine.](../../figures/assets/I06/I06-10-gram-interference.svg)

<figcaption>All Gram off-diagonal entries for the three unit directions are −0.5. Even with z₂=0, contributions from the two active features give dot-product response₂=−0.9. This is not exact sparse-coefficient recovery.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![Grouped bars compare the actual toy true coefficients one zero point eight with naive dot responses point six minus point nine point three, exposing a nonzero response to an inactive feature.](../../figures/assets/I06/I06-10-dot-response-vs-code.svg)

<figcaption>The toy's true coefficients and dot responses are compared on the same axis. The second feature is inactive but receives a negative response, and the other two values decrease as well. Recovering the active support differs from reading simple inner-product responses.</figcaption>
</figure>

## 3. What sparsity allows

If all features are always active together, interference accumulates. When only a few features are active per input, fewer directions collide simultaneously. Feature importance, sparsity, and correlations can affect which directions are arranged nearly orthogonally.

This explanation helps us understand geometry observed in optimized toy models. Establishing superposition in an actual model requires feature definitions, alternative hypotheses, and replication experiments.

### Visual intuition: share more directions than coordinate axes

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two orthogonal feature directions compared with four nonorthogonal sparse feature directions in two dimensions](../../figures/assets/I06/I06-10-superposition.svg)

<figcaption>On the left, two features align with neuron axes. On the right, four feature directions share the same 2-dimensional space nonorthogonally.</figcaption>
</figure>

Having more features than dimensions on the right does not by itself make the representation useful. If two coactive directions are nearly parallel, reading one feature's coefficient mixes in a large contribution from the other. Training may increase the angles between important or frequently cooccurring features, while allowing features that rarely cooccur to share more interference.

For example, if only unit directions $d_1,d_2$ are active, with $z_1=z_2=1$, the simple decoder output along $d_1$ is

\[
d_1^\top a
=
1+d_1^\top d_2
\]

If the directions are orthogonal, the second term is 0. If their inner product is $-0.5$, the read value is $0.5$. Interference is expressed numerically by the Gram matrix's off-diagonal entries, which quantify the overlap shown in the figure.

## 4. Privileged basis

A coordinatewise nonlinearity such as ReLU gives the neuron basis a special computational role. Input features still need not correspond to individual neurons. `It depends on the basis` and `the actual basis does not matter` are different statements.

An arbitrary orthogonal rotation can sometimes be canceled between linear layers. Inserting it in the same way around a coordinatewise ReLU, however, generally does not preserve the original function. When analyzing representations, distinguish basis-free subspace claims from sparsity and gating claims that hold only in the actual neuron coordinates.

Compare the output vectors of the two operation orders directly to see the difference.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Applying a 120-degree rotation after coordinate ReLU keeps a negative first component, while ReLU after rotation zeros it; the outputs differ.](../../figures/assets/I06/I06-10-relu-basis-order.svg)

<figcaption>This mathematical comparison of operation order uses the toy's d₁ and a 120° rotation. The first component of Q ReLU(a) is −0.5, whereas ReLU(Qa) sets it to 0. Coordinatewise operations in the neuron basis do not commute with a general rotation.</figcaption>
</figure>

## CPU exercise

Place three unit feature directions at 120-degree intervals on a 2-dimensional circle. Activate two of the three features and compute interference in simple dot-product decoding.

<!-- I06_EXAMPLE: i06_10_superposition -->

The Gram matrix's off-diagonal value $-0.5$ shows that the directions are not orthogonal. This construction is a toy example illustrating the principle, not an estimate of actual model features.

## Common misconceptions

### Misconception 1. A hidden dimension of 768 means at most 768 features

There can be at most 768 mutually orthogonal directions, but sparse, nonorthogonal representations can hold more feature candidates.

### Misconception 2. All nonorthogonal directions are errors

They may reflect a tradeoff between interference and capacity. Decoders and nonlinear computations can make use of this arrangement.

### Misconception 3. Many SAE features prove superposition

An SAE learns a dictionary for a chosen objective. Its number of latents does not establish the original model's number of ground-truth features.

## Exercises

### 1. Dimension

In a dictionary with $d=3$ and $m=5$, can all five columns be mutually orthogonal?

<details><summary>Show solution</summary>No. A 3-dimensional space can contain at most 3 linearly independent nonzero orthogonal vectors.</details>

### 2. Gram matrix

In a unit dictionary, what does $G_{12}=0$ imply about the two feature directions?

<details><summary>Show solution</summary>They are orthogonal. Reading one coefficient by a dot product receives no linear interference from the other.</details>

### 3. Decoding

If $G=I$, what is $D^Ta$?

<details><summary>Show solution</summary>Since $D^Ta=Gz=z$, the simple dot-product decoder recovers the coefficients exactly.</details>

### 4. Sparsity

Why does having few active features per input make nonorthogonal storage easier?

<details><summary>Show solution</summary>Fewer directions interfere simultaneously for an input. If conflicting features rarely activate together, average loss can remain low.</details>

### 5. Basis

Why does coordinatewise ReLU make the neuron basis special?

<details><summary>Show solution</summary>An arbitrary rotation generally does not commute with ReLU. The computational structure that applies a nonlinearity to each coordinate makes that basis privileged.</details>

### 6. Evidence

A neuron's top examples cover several topics. Does this alone establish superposition?

<details><summary>Show solution</summary>No. Sampling, confounds, or a failed description are also possible. Systematically test feature directions, sparsity, interference, and alternative explanations.</details>

## Evidence and update boundaries

The treatment of feature sparsity, importance, and superposition geometry in toy models follows [Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/index.html). Distinguish constructions in toy models from claims about what features exist in actual LLMs.

## Lesson summary

- A feature direction and a neuron coordinate are different concepts.
- An overcomplete dictionary has more nonorthogonal directions than dimensions.
- Gram off-diagonal entries express linear interference.
- Sparsity changes the tradeoff between capacity and interference.

## Pass criteria

- Can you distinguish features, coefficients, and neuron coordinates in $a=Dz$?
- Can you compute interference using a Gram matrix?
- Can you limit the scope of claims from toy superposition results?

## Next lesson

- [I06-11 Sparse coding](I06-11-sparse-coding.md)

## Author checklist

- [x] Superposition is explained through dictionaries, sparsity, and interference.
- [x] Every exercise has a solution.
- [x] The strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and mathematical rendering have been checked.
