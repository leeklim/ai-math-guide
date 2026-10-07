---
id: "A09-LRN-04"
title: "VC dimension"
part: 4
stage: "A09-LRN"
status: "complete"
prerequisites: ["A09-LRN-01", "M00-07"]
estimated_time: "90–120 minutes"
---

# A09-LRN-04. VC dimension

## Why this lesson matters

When parameter count alone makes it difficult to compare the expressive capacity of binary classifier classes, shattering defines capacity in terms of all possible label patterns. VC dimension is a standard complexity measure for distribution-free uniform generalization bounds.

## Learning objectives

- Define shattering and VC dimension.
- Find the VC dimensions of simple threshold and interval classes.
- Explain the relationship between the growth function and uniform convergence.
- Explain the worst-case nature of VC bounds.

## Prerequisite check

- Prerequisite lessons: [A09-LRN-01 Hypothesis class and risk](A09-LRN-01-hypothesis-class-risk.md), [M00-07 Sets, conditions, and logic](../../part-1-foundations/M00/M00-07-sets-conditions-logic.md)
- Check question: How many binary label patterns are there on $n$ points?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $\operatorname{VCdim}(\mathcal H)$ | `the V C dimension of H` | Largest number of points that can be shattered | nonnegative integer or infinity |
| $\Pi_{\mathcal H}(n)$ | `the growth function of H at n` | Maximum number of labelings realizable on $n$ points | integer |
| $S$ | `S` | finite input set | set of points |
| $2^n$ | `two to the n` | Number of all binary labelings | positive integer |

## Core concepts

### The two quantifiers in shattering

For $S=\{x_1,\ldots,x_n\}$, if all $2^n$ binary labelings can be realized by $\mathcal H$, then $S$ is said to be shattered. Fix distinct input points. For every $(y_1,\ldots,y_n)\in\{0,1\}^n$, the condition $h(x_i)=y_i$ for every $i$ must be satisfied by some $h\in\mathcal H$. A different $h$ may be chosen for each label pattern. One function does not have to output several patterns simultaneously.

VC dimension is the largest number of points that can be shattered. A size is achievable if even one configuration of that many points can be shattered; not every configuration has to be shattered. Conversely, to prove that the VC dimension is $d$, show an example of $d$ points that can be shattered and show that no set of $d+1$ points can be shattered. If arbitrarily large finite sets can be shattered, the dimension is infinity.

Start with one fixed point and choose different functions to see the order of function selection in shattering.

<figure class="lesson-figure" markdown="1">

![Two thresholds on the real line realize both labels at one fixed point.](../../figures/assets/A09-LRN/A09-LRN-04-threshold-one-point.svg)

<figcaption>Fix the same point x₁=1 and vary the threshold a to realize labels 0 and 1. A different function is chosen for each labeling; one function does not produce both labels simultaneously.</figcaption>

</figure>

### Label order for thresholds and intervals

For the threshold class $h_a(x)=1[x\ge a]$ on the real line, $1[\cdot]$ is an indicator: it returns 1 when the condition is true and 0 when it is false. At one point $x_1$, choosing $a\le x_1$ gives label 1, and choosing $a>x_1$ gives label 0. But for two points $x_1<x_2$, if the left point has label 1, the right point must also have label 1. No threshold location can produce $(1,0)$, so the VC dimension is 1. Do not confuse this class with a different class that also permits thresholds with the opposite orientation.

An interval indicator returns 1 only within a single interval. For two ordered points, choose intervals that include both, either one individually, or neither to realize all four patterns. For three ordered points, an interval containing both endpoints also contains the middle point, so $(1,0,1)$ is impossible. This ordering argument applies to every set of three points, giving VC dimension 2.

The next two figures compare thresholds and intervals by trying every labeling on the same two points.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Three realizable threshold patterns and the impossible one-zero pattern on two ordered points.](../../figures/assets/A09-LRN/A09-LRN-04-threshold-two-point-patterns.svg)

<figcaption>On the two points (1,2), thresholds realize 00, 01, and 11, but not 10. Read the colors together with the numerical labels to see the constraint that the positive region extends to the right.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Four intervals realize all four binary labelings on the same two points.](../../figures/assets/A09-LRN/A09-LRN-04-interval-two-point-shattering.svg)

<figcaption>Keep the points (1,2) fixed and change only the interval to realize all four labelings. Moving the interval away from both points gives 00, excluding both.</figcaption>

</figure>

### From the growth function to uniform convergence

The growth function $\Pi_{\mathcal H}(n)$ is the maximum number of distinct label vectors that the class produces on $n$ inputs. Even if there are infinitely many functions, functions with the same outputs on those $n$ points count as one vector. Always, $\Pi_{\mathcal H}(n)\le 2^n$; equality means that some set of $n$ points can be shattered. For the fixed-orientation thresholds above, the boundary can move only between ordered points or beyond either end, so $\Pi_{\mathcal H}(n)=n+1$.

For binary classifiers, 0–1 loss, and i.i.d. sampling from the same population, finite VC dimension controls uniform convergence. Uniform does not mean choosing just one function in advance and comparing its averages. It means that, with high probability, $\sup_{h\in\mathcal H}|R(h)-\hat R_n(h)|$ becomes small. When this event holds, the same upper bound on the difference applies to $\hat h$ chosen after observing the sample. With finite dimension, the growth in the number of possible label vectors is controlled for sufficiently large $n$. This provides a way to account simultaneously for chance training fit across the entire class. We assume the usual measurability conditions here and do not cover their technical details or prove the growth bound.

Count identical sample outputs only once. A uniform event covers the entire class, not just the selected function.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Several threshold locations share the same three-point labeling, leaving four distinct output patterns.](../../figures/assets/A09-LRN/A09-LRN-04-duplicate-threshold-outputs.svg)

<figcaption>Moving the boundary on the three points (1,2,3) produces only four distinct output vectors. The thresholds a=0.25 and a=0.75 define different functions, but both produce 111 on this sample, so that output is counted once.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![The threshold growth function n plus one compared with all two-to-the-n binary labelings.](../../figures/assets/A09-LRN/A09-LRN-04-threshold-growth-counts.svg)

<figcaption>Fixed-orientation thresholds produce n+1 patterns. This equals the number of all labelings at n=1, but is smaller than 2ⁿ from n=2 onward, so sets of those sizes cannot be shattered.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Illustrative absolute gaps for five hypotheses lie below one common upper bound, including the selected fourth hypothesis.](../../figures/assets/A09-LRN/A09-LRN-04-uniform-event-selected-function.svg)

<figcaption>These illustrative values show the inclusion relationship within a uniform event; they are not a computed VC bound. If the differences for all h are below a common upper bound, h₄ selected after observing the sample is included. The upper bound 0.12 is neither a claim that the actual gap is 0.12 nor a lower bound.</figcaption>

</figure>

### Worst-case capacity and actual learning outcomes

VC dimension does not count only the points that actually appeared during training. It maximizes over point configurations and labels the class can represent. A distribution-free bound holds across the specified family of distributions rather than choosing a favorable population. It can therefore be looser than an analysis that accounts for data geometry or constraints on the function actually selected by the optimizer. Even with the same class, regularization and the selection procedure can change the observed gap.

Do not apply the binary 0–1-loss guarantee from finite VC dimension directly to an unbounded regression loss. A large upper bound is also not a lower bound saying that the actual gap is large. Even when a bound does not yield a practically useful number, independent test evaluation still provides evidence about actual performance.

## Small example

On three points $x_1<x_2<x_3$, an interval classifier cannot produce a pattern in which only $x_1,x_3$ are positive and the middle point is negative.

For example, with $(x_1,x_2,x_3)=(1,2,3)$ and requested labels $(1,0,1)$, any single interval containing 1 and 3 also contains 2. The failure is not that the optimizer could not find an interval: no such function exists in the class. All four patterns are possible on two points, but this missing pattern on three points prevents shattering.

The three-point counterexample follows from the connectedness of the positive interval.

<figure class="lesson-figure" markdown="1">

![An interval covering one and three also covers two and cannot realize the requested one-zero-one labels.](../../figures/assets/A09-LRN/A09-LRN-04-interval-three-point-obstruction.svg)

<figcaption>Compare the requested 101 with the actual 111 of the interval [1,3]. A single interval containing both endpoints also contains the middle point, so the failure comes from the class constraint, not the optimizer.</figcaption>

</figure>

## Common misconceptions

- Large VC dimension does not imply inevitable overfitting on a particular dataset.
- A loose VC bound does not make generalization measurement unnecessary.

## Exercises

### 1. Number of labelings
How many binary labelings are there on 4 points?
<details><summary>Show solution</summary>

There are $2^4=16$.
</details>

### 2. Constant class
What is the VC dimension of the class $\mathcal H=\{h_0,h_1\}$ containing two constant classifiers?
<details><summary>Show solution</summary>

One point can be shattered because both labels can be realized. Mixed labels on two points cannot be realized, so the dimension is 1.
</details>

### 3. Threshold counterexample
Give one pattern that a threshold cannot produce on two ordered points.
<details><summary>Show solution</summary>

A pattern with label 1 on the left and 0 on the right cannot be produced by $h_a(x)=1[x\ge a]$.
</details>

### 4. Probe capacity
Why is it difficult to explain the performance difference between a linear probe and an MLP probe using VC dimension alone?
<details><summary>Show solution</summary>

Actual regularization, the optimizer, data geometry, loss, and finite-sample selection jointly affect effective capacity and performance.
</details>

## Evidence and update boundaries

Shattering, VC dimension, and the growth function follow the standard definitions of Vapnik–Chervonenkis theory. The proof of the Sauer–Shelah lemma and tight constants are outside this lesson's scope.

- [Cornell CS4783 Lecture 4, §2](https://www.cs.cornell.edu/courses/cs4783/2022sp/notes04.pdf): Used to check what the growth function maximizes over and the relationship between shattering and finite-dimension bounds.

## Lesson summary

- Shattering means realizing every binary labeling of a finite set.
- VC dimension is the maximum size of a shattered set.
- Finite VC dimension makes distribution-free uniform bounds possible.
- Do not use it as a precise prediction of the actual deep learning gap.

## Pass criteria

- Can you explain the VC dimensions of threshold and interval classes?
- Can you distinguish a worst-case capacity bound from empirical evaluation?

## Next lesson

- [A09-LRN-05 Rademacher complexity](A09-LRN-05-rademacher-complexity.md)

## Author checklist

- [x] Shattering and VC dimension are explained through counterexamples.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
