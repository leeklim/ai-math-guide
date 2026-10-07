---
id: "A09-SYM-01"
title: "Groups and group actions"
part: 4
stage: "A09-SYM"
status: "complete"
prerequisites: ["M03-02", "M03-15"]
estimated_time: "90–120 minutes"
---

# A09-SYM-01. Groups and group actions

## Why this lesson matters

Permuting neurons or rotating a hidden basis can still leave a model representing the same function. A group describes the structure of symmetry transformations that can be composed. A group action specifies how those transformations actually act on parameters, activations, or inputs.

## Learning objectives

- Check the four group conditions.
- Distinguish a group from its action.
- Calculate examples of permutation and rotation actions.
- Specify the object on which an action defining model equivalence operates.

## Prerequisite check

- Prerequisite lessons: [M03-02 Linear maps](../../part-1-foundations/M03/M03-02-linear-maps-matrix-representation.md), [M03-15 Model symmetries](../../part-1-foundations/M03/M03-15-reparameterization-model-symmetries.md)
- Check question: What kind of transformation results from applying two invertible basis changes in succession?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $(G,\circ)$ | `the group G with operation composition` | Group and operation | algebraic structure |
| $e$ | `the identity element` | Identity | element of $G$ |
| $g^{-1}$ | `g inverse` | Inverse element | element of $G$ |
| $g\cdot x$ | `g acting on x` | Action of $G$ on $X$ | element of $X$ |
| $R_\alpha$ | `R sub alpha` | Planar rotation through angle $\alpha$ | $2\times2$ matrix |

## Core concepts

### Groups: rules for composing transformations

A group consists of a set $G$ and an operation combining two of its elements. In this lesson, the operation is composition, and we abbreviate $g_1\circ g_2$ as $g_1g_2$. Check the following four conditions.

- Closure: if $g_1,g_2\in G$, then $g_1g_2\in G$. Applying two permitted transformations in succession must produce another permitted transformation.
- Associativity: $(g_1g_2)g_3=g_1(g_2g_3)$. Changing the grouping of compositions does not change the result.
- Identity: there is an element $e$ such that $eg=ge=g$. The identity matrix plays this role in matrix multiplication.
- Inverses: for each $g$, there is an element $g^{-1}\in G$ satisfying $g^{-1}g=gg^{-1}=e$. The operation that reverses a transformation must belong to the same set.

Associativity does not permit changing the order. In general, $g_1g_2$ and $g_2g_1$ differ. Also, invertible matrices form a group under multiplication, but the set of all square matrices, including singular matrices, does not satisfy the inverse condition. When specifying a group, state both the set of elements and the operation.

Check the group conditions through integer addition and matrix transformations.

<figure class="lesson-figure" markdown="1">

![Adding three moves integer two to five and adding the inverse minus three returns to two, with identity and associativity examples.](../../figures/assets/A09-SYM/A09-SYM-01-integer-group-return.svg)

<figcaption>In integer addition, adding 3 to 2 gives 5, and adding the inverse −3 returns to 2. The sum is still an integer, and the identity is 0. The expressions in parentheses below change only the grouping, keeping the order of the three elements.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A quarter-turn R and horizontal-axis reflection S send the same point to different endpoints when their order is reversed.](../../figures/assets/A09-SYM/A09-SYM-01-noncommuting-actions.svg)

<figcaption>R is a counterclockwise quarter-turn, and S is reflection across the horizontal axis. Starting from the same x=(1,2), RSx applies S first and gives (2,1), while SRx applies R first and gives (−2,−1). The arrows connect calculation stages, not an actual continuous motion path. Associativity does not exchange this order.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![The singular matrix diag(1,0) maps two distinct vectors to the same image, preventing an inverse on the whole plane.](../../figures/assets/A09-SYM/A09-SYM-01-singular-map-collapse.svg)

<figcaption>A=diag(1,0) sends the distinct vectors (1,1) and (1,−1) to the same (1,0). No inverse can recover both inputs separately from this one result. The set of all square matrices, including singular ones, does not satisfy the inverse condition.</figcaption>
</figure>

### Actions: what the transformations apply to

An action takes a group element $g$ and an object $x\in X$ and returns an element of the same set $X$. In this lesson, a left action is a map $G\times X\to X$ satisfying

$$
e\cdot x=x,
\qquad
(g_1g_2)\cdot x=g_1\cdot(g_2\cdot x)
$$

The first equation says that the identity leaves the object unchanged. On the right side of the second equation, apply $g_2$ first and $g_1$ afterward. Multiplying the two elements within the group and then applying the result must agree with this sequential application. Thus, $g^{-1}\cdot(g\cdot x)=x$, and the action of each group element can be reversed.

The group defines the composition rules, while the action defines how they apply to particular objects. For example, a permutation applied to a coordinate vector reorders its components, while applying it to a matrix by left multiplication reorders the rows. Even for the same permutation, the action formula differs depending on whether $X$ is a set of vectors or a set of parameter matrices.

Check the two calculation routes for an action and the differences between the objects it acts on.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two successive quarter-turns of vector (2,1) and a single half-turn product both give (-2,-1), illustrating the left-action law.](../../figures/assets/A09-SYM/A09-SYM-01-action-composition-routes.svg)

<figcaption>The upper route applies the rightmost R first and then another R; the lower route applies the group product RR=R₁₈₀ once. Both routes reach the same vector (−2,−1). The group product forms a transformation, and the action applies that transformation to an object in X.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The same two-coordinate permutation swaps vector components under Ph and matrix rows under PW while the object domains remain different.](../../figures/assets/A09-SYM/A09-SYM-01-permutation-action-domains.svg)

<figcaption>The same P changes components for h∈R² and changes rows by left multiplication for W∈R²×². Each output remains in the object set specified by its action. To understand the role of P, first specify which X it acts on.</figcaption>
</figure>

### Calculating permutations and rotations

An element of the symmetric group $S_m$, which rearranges $m$ hidden units, can be represented by a permutation matrix $P$. Each row and column has exactly one 1, with 0 in the remaining entries. We have $P^{-1}=P^{\mathsf T}$, and a product of two permutation matrices also rearranges coordinates. This group's action on vectors is $h\mapsto Ph$.

Planar rotations also act on vectors. Writing the rotation through angle $\alpha$ as $R_\alpha$, we have $R_\alpha R_\beta=R_{\alpha+\beta}$, and the inverse is $R_{-\alpha}$. For example, $R_{\pi/2}=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ sends $(a,b)$ to $(-b,a)$. Here, composition corresponds to adding angles.

Follow the coordinates of the quarter-turn and its inverse.

<figure class="lesson-figure" markdown="1">

![A quarter-turn maps (2,1) to (-1,2), preserves length, and its inverse quarter-turn restores the original vector.](../../figures/assets/A09-SYM/A09-SYM-01-quarter-turn-inverse.svg)

<figcaption>Use the faint coordinate axes to check R(a,b)=(−b,a). The example (2,1) maps to (−1,2), and R⁻¹ returns it to (2,1). Distinguish the rotation as a group element from the calculation applying it to a vector.</figcaption>
</figure>

### Parameter actions and function preservation

Consider two layers $h=\phi(W_1x)$ and $y=W_2h$, with $W_1\in\mathbb R^{m\times d}$ and $W_2\in\mathbb R^{q\times m}$. Applying the same scalar function $\phi$ to each component gives $\phi(Pz)=P\phi(z)$, allowing the parameter action

$$
(W_1,W_2)\mapsto(PW_1,W_2P^{-1}),
\qquad
h\mapsto Ph.
$$

Reordering the rows of the first matrix relabels the hidden units. The second matrix compensates by applying the inverse change. The new output is $W_2P^{-1}\phi(PW_1x)=W_2P^{-1}P\phi(W_1x)=W_2\phi(W_1x)$, identical to the original output for every input. The object set $X$ for this action consists of parameter pairs; the input $x$ itself is unchanged. This is distinct from examining a model's response to an input rotation.

Applying two actions in succession multiplies $W_1$ on the left by $P_1P_2$ and $W_2$ on the right by $(P_1P_2)^{-1}=P_2^{-1}P_1^{-1}$. Thus, the application rule for parameter pairs also satisfies the action law. Function preservation follows from this compensation and compatibility with the activation. The existence of a permitted group alone does not give an arbitrary model symmetry under that group.

Move the hidden values together with their corresponding weights in the next layer.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Swapping hidden rows changes (2,5) to (5,2) and swapping the paired readout weights (3,7) to (7,3) keeps output 41.](../../figures/assets/A09-SYM/A09-SYM-01-parameter-compensation.svg)

<figcaption>In this small two-unit calculation, reordering the rows of W₁ changes hidden values (2,5) to (5,2). Also reordering the next weights (3,7) to (7,3) makes both 3×2+7×5 and 7×5+3×2 equal 41. This is row-and-column compensation in two layers with the same scalar activation, leaving input x unchanged.</figcaption>
</figure>

## Small example

The matrix $P=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ swapping two hidden units satisfies $P^2=I$, so it is its own inverse.

It gives $P(a,b)^{\mathsf T}=(b,a)^{\mathsf T}$, and applying it again restores $(a,b)^{\mathsf T}$. In the two-layer calculation, preserving the output requires swapping both rows of $W_1$ and both columns of $W_2$ together. Changing only one side alters the pairing between hidden units and output weights.

## Common misconceptions

- Having a set of transformations does not make it a group. Check inverses and closure.
- Representing the same function does not mean having the same parameter coordinates.

## Exercises

### 1. Checking a group
Do the integers form a group under addition?
<details><summary>Show solution</summary>

Yes. The identity is 0, the inverse of $n$ is $-n$, and closure and associativity hold.
</details>

### 2. Action law
Explain why matrix multiplication $g\cdot x=gx$ is an action of $GL(d)$ on $\mathbb R^d$.
<details><summary>Show solution</summary>

The equations $Ix=x$ and $(g_1g_2)x=g_1(g_2x)$ satisfy the two action laws.
</details>

### 3. Permutation
Find the result of applying the matrix $P$ above to vector $(a,b)$.
<details><summary>Show solution</summary>

The result is $(b,a)$.
</details>

### 4. Model interpretation
Why should you state the domain of a group action when comparing representations?
<details><summary>Show solution</summary>

The same transformation symbol preserves different quantities and has different meanings when acting on inputs, hidden coordinates, or parameters.
</details>

## Sources and update boundaries

Groups and group actions follow standard definitions in abstract algebra. This lesson does not cover the smooth structure of Lie groups.

- [Ackerman, Algebra lecture notes, §§0.3–0.4](https://people.math.harvard.edu/~nate/teaching/UPenn/2007/fall/math_371/lectures/week_1/lecture_1/lecture_1.pdf): A reference for the standard definitions of groups and actions. The matrix compensation in the text was calculated directly from the given two-layer equations.

## Lesson summary

- A group is the structure of composable, invertible symmetry transformations.
- An action is the rule by which group elements act on specified objects.
- Permutations can produce hidden-coordinate equivalence.
- For a model symmetry, state both the object acted on and the function preserved.

## Pass criteria

- Can you check the group conditions and action laws?
- Can you explain the compensating transformations for a neuron permutation?

## Next lesson

- [A09-SYM-02 Orbits and stabilizers](A09-SYM-02-orbits-stabilizers.md)

## Author checklist

- [x] The roles of groups and actions are distinguished.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
