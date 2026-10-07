---
id: "M03-04"
title: "Introduction to invariants and equivariance"
part: 1
stage: "M03"
status: "complete"
prerequisites:
  - "M03-03"
  - "M02-03"
estimated_time: "115~140 minutes"
---

# M03-04. Introduction to invariants and equivariance

## Why this lesson matters

Changing a basis, coordinate order, or input position changes some quantities while leaving others unchanged. To compare analysis results, first specify the allowed transformations and check whether the results are preserved under them. Claims such as “basis-independent” or “symmetric” have no clear scope unless the transformations are stated.

Some tasks require a model's output to ignore input transformations; others require the output to transform with the input. The sum of a set's elements should ignore their order. Predictions attached to individual elements, however, should move in the same order when the elements are reordered. The first property is invariance, and the second is equivariance.

## Learning objectives

After completing this lesson, you will be able to:

- Define a transformation and an invariant using an equality between quantities before and after transformation.
- Distinguish invariance from equivariance using equations and small examples.
- Calculate how orthogonal transformations preserve norms, inner products, and distances.
- Verify the invariance of summation and the equivariance of componentwise operations under permutations.
- State under which transformations an analysis method reaches the same conclusion.
- Explain why invariance does not imply information preservation or evidence of model use.

## Prerequisite check

- Prerequisite lesson: [M03-03 Change of basis and coordinate dependence](M03-03-change-of-basis-coordinate-dependence.md)
- Prerequisite lesson: [M02-03 Inner product, length, and angle](../M02/M02-03-inner-product-length-angle.md)
- Check: Can you distinguish a passive coordinate change from an active vector transformation?
- Check: Can you explain what it means for an orthogonal matrix $\mathbf Q$ to satisfy $\mathbf Q^\top\mathbf Q=\mathbf I$?

Review the prerequisite lessons first if change of basis or orthogonal matrices are unclear.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Scope |
|---|---|---|---|
| $g$ | `g` | An allowed transformation applied to the input | Rotation, reflection, permutation, and so on |
| $g\cdot\mathbf x$ | `g acting on x` | The input after applying transformation $g$ | An element of the input space |
| $I(\mathbf x)$ | `I of x` | A candidate invariant calculated from the input | A scalar or another summary |
| $f$ | `f` | A function mapping inputs to outputs | A model or analysis function |
| $\rho(g)$ | `rho of g` | The transformation corresponding to $g$ in the output space | Depends on the output type |
| invariance | `invariance` | The property that the output remains unchanged when the input is transformed | $f(g\cdot\mathbf x)=f(\mathbf x)$ |
| equivariance | `equivariance` | The property that the output transforms in accordance with the input transformation | $f(g\cdot\mathbf x)=\rho(g)f(\mathbf x)$ |

This lesson does not examine the algebraic structure of transformations in depth. Groups and group actions are defined in A09-SYM.

## Core concept 1. An invariant retains its value under specified transformations

For an allowed transformation $g$ of the input space, if

\[
I(g\cdot\mathbf x)=I(\mathbf x)
\]

holds for every allowed input $\mathbf x$, then $I$ is called an invariant under that transformation.

Here, $g\cdot\mathbf x$ denotes applying the specified transformation, not multiplying by a scalar. If several transformations are allowed, the equality must hold for each of them and for every input in the allowed domain. Finding equal values by coincidence for one input checks that input; it does not prove invariance of the entire function.

An invariant must be specified together with two things:

1. What object is being transformed?
2. What transformations are allowed?

For example, the Euclidean norm is invariant under orthogonal transformations. It is not invariant under all transformations defined by invertible matrices. With $\mathbf x=(1,0)^\top$ and

\[
\mathbf A=
\begin{bmatrix}
2&0\\
0&1
\end{bmatrix}
\]

we have $\|\mathbf x\|_2=1$ but $\|\mathbf A\mathbf x\|_2=2$.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Unit vector and its doubled horizontal image under diagonal scaling compared on one coordinate grid](../../figures/assets/M03/M03-04-scaling-breaks-norm.svg)
  <figcaption>The invertible matrix diag(2,1) in the text changes the horizontal vector's length from 1 to 2. Only the output arrow is shifted slightly upward to avoid overlapping the arrows; the purpose is to compare their directions and lengths.</figcaption>
</figure>

Invertibility means that a transformation can be reversed, not that it preserves length.

## Core concept 2. Orthogonal transformations preserve inner product structure

If $\mathbf Q\in\mathbb R^{d\times d}$ satisfies

\[
\mathbf Q^\top\mathbf Q=\mathbf I_d
\]

then $\mathbf Q$ is an orthogonal matrix. For two vectors $\mathbf x,\mathbf y\in\mathbb R^d$,

\[
\langle\mathbf Q\mathbf x,\mathbf Q\mathbf y\rangle
=
(\mathbf Q\mathbf x)^\top(\mathbf Q\mathbf y)
=
\mathbf x^\top\mathbf Q^\top\mathbf Q\mathbf y
=
\mathbf x^\top\mathbf y
\]

Thus, norms are also preserved.

\[
\|\mathbf Q\mathbf x\|_2^2
=
\langle\mathbf Q\mathbf x,\mathbf Q\mathbf x\rangle
=
\langle\mathbf x,\mathbf x\rangle
=
\|\mathbf x\|_2^2
\]

Distance is the norm of a vector difference, so

\[
\|\mathbf Q\mathbf x-\mathbf Q\mathbf y\|_2
=
\|\mathbf Q(\mathbf x-\mathbf y)\|_2
=
\|\mathbf x-\mathbf y\|_2
\]

If both vectors are nonzero, their angle is calculated from their inner product and norms and is therefore preserved. An angle involving the zero vector is not defined. These calculations apply the same $\mathbf Q$ to both vectors. Rotating only one vector while fixing the other does not justify concluding that their inner product is preserved.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Original example vectors three four and one minus two with a dashed segment connecting their endpoints](../../figures/assets/M03/M03-04-rotation-before.svg)
  <figcaption>The two input vectors in Example 1 and the distance between their endpoints are shown on the same coordinate grid. The vector lengths are 5 and √5, and the dashed segment has length √40.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Both example vectors after a ninety degree rotation with the same lengths and endpoint distance](../../figures/assets/M03/M03-04-rotation-after.svg)
  <figcaption>Applying the same 90-degree rotation to both vectors rotates the whole configuration while preserving both lengths, their distance, and their angle. The numerical coordinates change, but these geometric relationships remain the same.</figcaption>
</figure>

The coordinate tick spacing is the same in both figures. The comparison rotates both vectors and the dashed segment together, rather than rotating just one vector.

## Core concept 3. An invariant function removes the input transformation from the output

A function $f:X\to Y$ is invariant under a transformation $g$ when

\[
f(g\cdot\mathbf x)=f(\mathbf x)
\]

The transformed and original inputs produce the same output.

For example, let $\mathbf P$ be a permutation matrix that reorders the components of $\mathbf x\in\mathbb R^n$. Their sum,

\[
s(\mathbf x)=\sum_{i=1}^{n}x_i
\]

satisfies

\[
s(\mathbf P\mathbf x)=s(\mathbf x)
\]

A permutation changes only the positions of the components, so the sum does not change.

A permutation matrix has one 1 in each row and column and 0 everywhere else. Each row selects one input component; the condition that each column contains one 1 prevents any component from being omitted or repeated. Summing the components of $\mathbf P\mathbf x$ therefore adds every term of the original sum once, in a different order. Commutativity and associativity of addition give the same sum.

An invariant function does not distinguish transformation-induced differences in its output. This property may discard necessary information. The constant function $f(\mathbf x)=0$ is invariant under every input transformation but provides no information about the input.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Two input components exchange positions but both orderings map to the same scalar sum one](../../figures/assets/M03/M03-04-permutation-invariance.svg)
  <figcaption>Reordering the input components in Example 2 exchanges the positions of the blue 2 and orange −1. Both paths nevertheless output the sum 1, leaving no indication of which value came first.</figcaption>
</figure>

The two crossing arrows show a permutation that changes positions without omitting or repeating a component.

## Core concept 4. An equivariant function carries the transformation to the output

A function $f:X\to Y$ is equivariant when

\[
f(g\cdot\mathbf x)
=
\rho(g)f(\mathbf x)
\]

Transforming the input before applying $f$ gives the same result as applying $f$ first and then the corresponding output transformation $\rho(g)$.

The rule $\rho(g)$ specifies how to transform the output in correspondence with the input transformation $g$. If the input and output have different types or sizes, the same array cannot be applied to both spaces, so the output rule is specified separately. If $\rho(g)$ is a matrix, the right-hand side is a matrix product. For a general transformation, it is shorthand for applying that transformation to the output $f(\mathbf x)$.

When the input and output have the same type and use the same transformation, this can be abbreviated as

\[
f(g\cdot\mathbf x)=g\cdot f(\mathbf x)
\]

The componentwise squaring function

\[
f(\mathbf x)
=
\begin{bmatrix}
x_1^2\\
\vdots\\
x_n^2
\end{bmatrix}
\]

is equivariant under permutations.

\[
f(\mathbf P\mathbf x)=\mathbf P f(\mathbf x)
\]

Reordering before squaring each component gives the same result as squaring first and then reordering.

Equivariance here does not mean linearity. Squaring does not preserve scaling, but it commutes with component reordering. More generally, suppose the same single-variable function $\phi$ is applied to every component. After a permutation, the $i$th output is $\phi$ applied to the original component moved to that position. Applying $\phi$ first and then reordering the output places the same component in that position. This conclusion does not automatically apply if different functions are used for different components.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Commuting component paths for swapping before squaring and squaring before swapping ending in the same reordered output one four](../../figures/assets/M03/M03-04-permutation-equivariance.svg)
  <figcaption>The path that swaps the input on the left and squares it at the bottom reaches the same (1,4)ᵀ as the path that squares at the top and swaps the output on the right. Colors identifying the same components also follow the exchange of output positions.</figcaption>
</figure>

The sum above preserved one output, whereas componentwise squaring reorders two output positions together with the input.

## Core concept 5. Choose invariance or equivariance according to the output's role

A function assigning one label to an entire input may need to ignore order or rotation. In that case, invariance is the appropriate requirement. A function assigning one output to each input element should move each output when its input element moves. Equivariance is appropriate in that case.

The table summarizes the difference between the two conditions.

| Question | Invariance | Equivariance |
|---|---|---|
| Output after transformation | Unchanged | The result of the specified output transformation |
| Representative equation | $f(g\cdot\mathbf x)=f(\mathbf x)$ | $f(g\cdot\mathbf x)=\rho(g)f(\mathbf x)$ |
| Example | Sum of set elements | Elementwise predictions |
| Effect on information | May remove information about the transformation direction | May preserve transformation information in output positions |

A function can be invariant under some transformations and equivariant under others. Its name alone does not determine these properties; the input and output actions must be stated.

The two conditions are not mutually exclusive. Choosing the identity transformation for $\rho(g)$ makes the equivariance equation the invariance equation. Nor does equivariance require output values to change after transformation. For example, an output whose components are all 0 remains unchanged under permutations. The equality requires agreement with the specified output rule, not a particular amount of change.

## Core concept 6. Representation comparisons first specify the allowed transformations

Given two activation matrices $\mathbf H_1$ and $\mathbf H_2$, the phrase “the same representation” lacks a comparison criterion. The following relationships use different allowed transformations.

Here, $\mathbf H_1,\mathbf H_2\in\mathbb R^{N\times d}$ contain the same samples as rows in the same order. The right-multiplying matrices $\mathbf Q$ and $\mathbf A$ are $d\times d$ and transform feature coordinates. This comparison must be distinguished from one that also changes the sample correspondence.

- Elementwise equality: $\mathbf H_2=\mathbf H_1$
- Equality after orthogonal alignment: $\mathbf H_2=\mathbf H_1\mathbf Q$
- Equality after invertible linear alignment: $\mathbf H_2=\mathbf H_1\mathbf A$

Orthogonal alignment preserves Euclidean inner products and distances between rows. General invertible alignment preserves linear independence and dimension but may change Euclidean distances and angles. When interpreting a representation similarity measure, check under which transformations it is invariant.

Column combinations also explain why invertible alignment preserves rank. Every column of $\mathbf H_1\mathbf A$ is a linear combination of the columns of $\mathbf H_1$. Conversely, $\mathbf H_1=\mathbf H_2\mathbf A^{-1}$, so every original column is a linear combination of the new columns. The two column spaces are therefore equal and have the same dimension.

The matrix collecting inner products between sample rows, however, is

\[
\mathbf H_2\mathbf H_2^\top
=\mathbf H_1\mathbf A\mathbf A^\top\mathbf H_1^\top
\]

For a general invertible matrix, the middle factor $\mathbf A\mathbf A^\top$ cannot be canceled as an identity matrix. The reasoning that proves rank preservation therefore does not establish preservation of Euclidean geometry.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Three matched sample rows A B C forming a right triangle in two feature coordinates](../../figures/assets/M03/M03-04-sample-geometry-original.svg)
  <figcaption>This small representation-comparison example shows sample rows A=(0,0), B=(2,0), and C=(0,1). The sample names retain the correspondence between the same rows even when coordinates change.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Same three matched samples after orthogonal feature rotation with every pair distance preserved](../../figures/assets/M03/M03-04-sample-geometry-orthogonal.svg)
  <figcaption>Right multiplication by the orthogonal matrix Q=[[0,1],[−1,0]] rotates the feature coordinates and changes each sample's coordinate values. All distances between points with the same names are preserved.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Same matched sample rows after invertible horizontal feature scaling with rank two retained but changed pair distances](../../figures/assets/M03/M03-04-sample-geometry-stretched.svg)
  <figcaption>Invertible right multiplication by A=diag(2,1) stretches the horizontal direction, changing distances AB and BC. Two independent feature directions and rank 2 are retained, but Euclidean geometry is not necessarily preserved.</figcaption>
</figure>

The three figures use the same scale. Distinguishing changed feature coordinate indices from unchanged sample names reveals which relationships remain equal under each allowed transformation.

## Example 1. Checking norms and inner products under rotation

### Problem

Let

\[
\mathbf Q=
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}
3\\
4
\end{bmatrix},
\qquad
\mathbf y=
\begin{bmatrix}
1\\
-2
\end{bmatrix}
\]

Calculate $\mathbf Q^\top\mathbf Q$, the two norms, and the inner product before and after transformation.

### Solution

\[
\mathbf Q^\top\mathbf Q
=
\begin{bmatrix}
0&1\\
-1&0
\end{bmatrix}
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}
=
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
\]

Thus, $\mathbf Q$ is orthogonal.

\[
\mathbf Q\mathbf x=
\begin{bmatrix}
-4\\
3
\end{bmatrix},
\qquad
\mathbf Q\mathbf y=
\begin{bmatrix}
2\\
1
\end{bmatrix}
\]

The norms are

\[
\|\mathbf x\|_2=5,
\qquad
\|\mathbf Q\mathbf x\|_2=\sqrt{(-4)^2+3^2}=5
\]

and

\[
\|\mathbf y\|_2=\sqrt5,
\qquad
\|\mathbf Q\mathbf y\|_2=\sqrt5
\]

The inner products are

\[
\mathbf x^\top\mathbf y
=
3\cdot1+4\cdot(-2)
=
-5
\]

\[
(\mathbf Q\mathbf x)^\top(\mathbf Q\mathbf y)
=
(-4)\cdot2+3\cdot1
=
-5
\]

### Meaning of the result

$\mathbf Q$ rotates both vectors by 90 degrees while preserving their lengths and inner product.

## Example 2. Invariance and equivariance under a permutation

### Problem

Let

\[
\mathbf P=
\begin{bmatrix}
0&1\\
1&0
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}
2\\
-1
\end{bmatrix}
\]

Verify the invariance of the sum $s(\mathbf x)=x_1+x_2$ and the equivariance of the componentwise squaring function $f$.

### Solution

\[
\mathbf P\mathbf x
=
\begin{bmatrix}
-1\\
2
\end{bmatrix}
\]

and

\[
s(\mathbf x)=2+(-1)=1,
\qquad
s(\mathbf P\mathbf x)=-1+2=1
\]

This checks invariance of the sum for this input.

\[
f(\mathbf x)
=
\begin{bmatrix}
4\\
1
\end{bmatrix}
\]

and

\[
f(\mathbf P\mathbf x)
=
\begin{bmatrix}
1\\
4
\end{bmatrix}
=
\mathbf P
\begin{bmatrix}
4\\
1
\end{bmatrix}
=
\mathbf P f(\mathbf x)
\]

### Meaning of the result

Summation removes information about which component comes first. Componentwise squaring lets each output move with its corresponding input component.

## Example 3. Stating the transformation class in model analysis

Suppose the sample activations from the same layer of two models are stacked as rows to obtain

\[
\mathbf H_1,\mathbf H_2\in\mathbb R^{N\times d}
\]

If $\mathbf H_2=\mathbf H_1\mathbf Q$ and $\mathbf Q^\top\mathbf Q=\mathbf I_d$, the Gram matrices between samples are equal.

\[
\mathbf H_2\mathbf H_2^\top
=
\mathbf H_1\mathbf Q\mathbf Q^\top\mathbf H_1^\top
=
\mathbf H_1\mathbf H_1^\top
\]

Analyses using inner products and Euclidean distances between samples therefore give the same results. Individual feature coordinates may differ. This calculation alone does not establish that the two models use the same internal algorithm.

## Common misconceptions

### Misconception 1. An invariant is preserved under every transformation

An invariant is defined relative to a specified transformation set. The Euclidean norm is preserved under orthogonal transformations but may change under general invertible transformations.

### Misconception 2. Invariance and equivariance mean the same thing

An invariant function produces the same output after transformation. An equivariant function transforms its output in a specified way corresponding to the input transformation.

### Misconception 3. More invariance always makes a representation better

Invariance removes transformation-related information. Discarding directions or positions needed for a task can harm prediction. The task determines which changes should be ignored.

### Misconception 4. Equal invariant measures imply equal model computations

An invariant measure does not distinguish differences caused by allowed transformations. Equal values provide evidence that the structure measured by that measure is the same, not a guarantee of identical internal computational paths or functional use.

## Exercises

### 1. Reading a definition

Explain

\[
f(g\cdot\mathbf x)=\rho(g)f(\mathbf x)
\]

in an English sentence.

<details>
<summary>Show solution</summary>

Applying transformation $g$ to the input and then calculating $f$ gives the same result as calculating $f$ on the original input and then applying the corresponding transformation $\rho(g)$ in the output space. The equality expresses equivariance of $f$.

</details>

### 2. Identifying invariant functions

Determine which functions are invariant under the permutation exchanging the two components of $\mathbf x=(x_1,x_2)^\top$.

\[
f_1(\mathbf x)=x_1+x_2,
\qquad
f_2(\mathbf x)=x_1,
\qquad
f_3(\mathbf x)=\max(x_1,x_2)
\]

<details>
<summary>Show solution</summary>

$f_1$ and $f_3$ retain their values when the two components are exchanged. $f_2$ selects the first component, so its value generally changes. For example, at $(1,3)^\top$, $f_2=1$; after the permutation, it is 3.

</details>

### 3. Calculating an orthogonal invariant

For

\[
\mathbf Q=
\begin{bmatrix}
0&1\\
-1&0
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}
1\\
2
\end{bmatrix}
\]

compare $\|\mathbf x\|_2$ and $\|\mathbf Q\mathbf x\|_2$.

<details>
<summary>Show solution</summary>

\[
\mathbf Q\mathbf x=
\begin{bmatrix}
2\\
-1
\end{bmatrix}
\]

so

\[
\|\mathbf x\|_2=\sqrt{1^2+2^2}=\sqrt5
\]

\[
\|\mathbf Q\mathbf x\|_2=\sqrt{2^2+(-1)^2}=\sqrt5
\]

The two values agree. Orthogonality of $\mathbf Q$ explains this preservation in general.

</details>

### 4. Checking equivariance

Check whether $f(x_1,x_2)^\top=(x_1+1,x_2+1)^\top$ is equivariant under component permutations.

<details>
<summary>Show solution</summary>

Writing the permutation matrix as $\mathbf P$,

\[
f(\mathbf P\mathbf x)
=
\mathbf P\mathbf x+
\begin{bmatrix}1\\1\end{bmatrix}
\]

Meanwhile,

\[
\mathbf P f(\mathbf x)
=
\mathbf P\left(
\mathbf x+
\begin{bmatrix}1\\1\end{bmatrix}
\right)
=
\mathbf P\mathbf x+
\begin{bmatrix}1\\1\end{bmatrix}
\]

The two expressions are equal, so the function is equivariant.

</details>

### 5. Invariance and information loss

Explain why the constant function $f(\mathbf x)=0$ is invariant under every input transformation and why this alone does not make it a good representation.

<details>
<summary>Show solution</summary>

For any $g$ and $\mathbf x$,

\[
f(g\cdot\mathbf x)=0=f(\mathbf x)
\]

so the function is invariant. Every input nevertheless maps to the same output, leaving no information that distinguishes inputs. Separately evaluate whether it ignores only the necessary transformations while retaining task-relevant information.

</details>

### 6. Conditions for comparing representations

Suppose $\mathbf H_2=\mathbf H_1\mathbf A$, where $\mathbf A$ is invertible but not orthogonal. Give one property that must be preserved and one that may not be preserved.

<details>
<summary>Show solution</summary>

Invertible right multiplication preserves the dimension of the column space and the rank. Euclidean distances and angles between sample rows may change. Thus, the linearly represented dimension may be the same, but this does not establish equal Euclidean geometry.

</details>

### 7. Critiquing a claim

Critique the statement: “The Gram matrices of the two representations are equal, so the two models use the same features in the same neurons.”

<details>
<summary>Show solution</summary>

A Gram matrix is invariant under orthogonal feature rotations. If two representations are related by an orthogonal transformation, inner products between samples remain equal while individual neuron coordinates may mix. Equal Gram matrices show agreement of sample relationships, not neuron-by-neuron feature correspondence or functional use by the model.

</details>

## Lesson summary

- An invariant is a function whose value is preserved under specified input transformations.
- Orthogonal transformations preserve Euclidean inner products, norms, distances, and angles.
- An invariant function removes the input transformation from the output; an equivariant function carries it to a corresponding output transformation.
- Invariance is useful for removing task-irrelevant differences but may also remove necessary information.
- Interpreting a representation comparison measure requires stating the transformations it allows.

## Pass criteria

You pass if you can answer the following without referring to the material:

- Can you define an invariant together with its object and allowed transformations?
- Can you distinguish the equations for invariance and equivariance?
- Can you derive preservation of inner products and norms under orthogonal transformations?
- Can you verify the properties of summation and componentwise functions under permutations?
- Can you explain how invariance may lose information?
- Can you identify claims that a representation comparison measure's invariance alone does not support?

## Next lesson

- [M03-05 Subspaces, direct sums, and decomposition](M03-05-subspaces-direct-sums-decomposition.md)

## Author checklist

- [x] Learning objectives are expressed as observable actions.
- [x] Invariants are defined after specifying the transformation set.
- [x] Invariance and equivariance are distinguished using equations and examples.
- [x] Preservation properties of orthogonal transformations are calculated.
- [x] Information loss and the scope of claims are explained.
- [x] Every exercise has a solution.
- [x] The strengths of model interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] No knowledge beyond the prerequisites is implicitly required.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
