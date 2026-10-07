---
id: "M03-05"
title: "Subspaces, direct sums, and decomposition"
part: 1
stage: "M03"
status: "complete"
prerequisites:
  - "M03-01"
  - "M02-08"
  - "M02-09"
estimated_time: "120~145 minutes"
---

# M03-05. Subspaces, direct sums, and decomposition

## Why this lesson matters

When separating a representation space into components, check whether each component is a subspace, whether they overlap, and whether the original vector can be recovered uniquely. Two subspaces may sum to the original space without providing a unique decomposition. A direct sum, with no nonzero overlap, guarantees this uniqueness.

Model interpretation may decompose an activation into a particular feature subspace and a remaining component, or analyze the residual after projection onto a low-rank subspace. The decomposition depends on the chosen subspace and inner product. Recovering information from a subspace alone does not establish that the model uses that subspace functionally.

## Learning objectives

After completing this lesson, you will be able to:

- Define the sum and intersection of two subspaces and calculate them in small examples.
- Use the intersection to determine whether a subspace sum is direct.
- Explain uniqueness of vector decomposition in a direct sum.
- Calculate the dimension of a subspace sum using the dimension formula.
- Use an orthogonal complement and orthogonal projection to decompose a vector into a signal component and residual.
- Distinguish claims supported by a model representation's subspace decomposition from those it does not support.

## Prerequisite check

- Prerequisite lesson: [M03-01 Abstract vector spaces](M03-01-abstract-vector-spaces.md)
- Prerequisite lesson: [M02-08 Kernel, image, and rank](../M02/M02-08-kernel-image-rank.md)
- Prerequisite lesson: [M02-09 Orthogonal bases and orthogonal projection](../M02/M02-09-orthogonal-basis-projection.md)
- Check: Can you identify a subspace by the presence of the zero vector and closure under the operations?
- Check: Can you project a vector orthogonally onto a subspace using an orthonormal basis?

Review the prerequisite lessons first if subspaces or orthogonal projection calculations are unclear.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| $U,W$ | `U and W` | Subspaces of a vector space $V$ | $U,W\le V$ |
| $U+W$ | `U plus W` | The subspace of vectors of the form $\mathbf u+\mathbf w$ | $\mathbf u\in U,\mathbf w\in W$ |
| $U\cap W$ | `U intersection W` | The space of vectors belonging to both subspaces | Contains at least the zero vector |
| $U\oplus W$ | `U direct sum W` | A subspace sum whose intersection is the zero subspace | Each vector has a unique decomposition |
| $U^\perp$ | `U perp` | The space of vectors orthogonal to every vector in $U$ | Requires a specified inner product |
| $\operatorname{proj}_U\mathbf x$ | `the projection of x onto U` | The vector in $U$ closest to $\mathbf x$ | With respect to the Euclidean inner product |

## Core concept 1. A subspace sum adds components from two spaces

The notation $U,W\le V$ means that $U,W$ are subspaces of $V$. Their sum is defined by

\[
U+W
=
\{\mathbf u+\mathbf w:\mathbf u\in U,\ \mathbf w\in W\}
\]

The sum $U+W$ differs from $U\cup W$. It also includes linear combinations mixing vectors from both spaces.

Both $U,W$ contain the zero vector, so $\mathbf u=\mathbf u+\mathbf 0$ and $\mathbf w=\mathbf 0+\mathbf w$ belong to the sum. It therefore contains both subspaces. Moreover, $\alpha\mathbf u\in U$ and $\beta\mathbf w\in W$, so combinations with coefficients, such as $\alpha\mathbf u+\beta\mathbf w$, satisfy the same definition. Neither term $\mathbf u$ nor $\mathbf w$ is restricted to a single generating vector.

The sum $U+W$ is a subspace of $V$. The zero vector can be written as $\mathbf 0_U+\mathbf 0_W$. Adding two elements

\[
\mathbf x=\mathbf u_1+\mathbf w_1,
\qquad
\mathbf y=\mathbf u_2+\mathbf w_2
\]

gives

\[
\mathbf x+\mathbf y
=
(\mathbf u_1+\mathbf u_2)+(\mathbf w_1+\mathbf w_2)
\]

Each parenthesized term remains in its respective subspace. Closure under scalar multiplication follows in the same way.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Horizontal and vertical subspaces with a mixed sum vector two one whose endpoint belongs to neither axis](../../figures/assets/M03/M03-05-sum-not-union.svg)
  <figcaption>Choosing (2,0)ᵀ from the horizontal subspace and (0,1)ᵀ from the vertical subspace gives (2,1)ᵀ. Its endpoint lies on neither axis, but it belongs to the subspace sum.</figcaption>
</figure>

The union contains only the two axes. The sum, which allows either component to have any magnitude, can reach every endpoint in the plane.

## Core concept 2. The intersection represents overlap between decomposition components

\[
U\cap W
=
\{\mathbf v\in V:\mathbf v\in U\text{ and }\mathbf v\in W\}
\]

Both subspaces contain the zero vector, so their intersection cannot be empty.

If the intersection contains a nonzero $\mathbf z$, the same vector can be separated in multiple ways. If $\mathbf x=\mathbf u+\mathbf w$, then

\[
\mathbf x
=
(\mathbf u+\mathbf z)+(\mathbf w-\mathbf z)
\]

is another decomposition of the same vector. Since $\mathbf z\in U$, we have $\mathbf u+\mathbf z\in U$; since $\mathbf z\in W$, we have $\mathbf w-\mathbf z\in W$.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![The horizontal subspace inside a whole-plane subspace with the same nonzero vector belonging to both and allowing two allocations](../../figures/assets/M03/M03-05-overlap-nonunique.svg)
  <figcaption>In Example 2, the whole plane W contains the horizontal line U. Assigning the displayed e₁ entirely to either the U component or the W component gives the same sum, so the decomposition is not unique.</figcaption>
</figure>

This overlap is not merely a shared origin. It is a shared nonzero direction that can be assigned to either component.

## Core concept 3. A direct sum guarantees a unique decomposition

The notation

\[
V=U\oplus W
\]

means that two conditions hold:

1. $V=U+W$
2. $U\cap W=\{\mathbf 0\}$

Under these conditions, every $\mathbf v\in V$ has a unique decomposition

\[
\mathbf v=\mathbf u+\mathbf w
\]

To prove uniqueness, suppose there are two decompositions:

\[
\mathbf v
=
\mathbf u_1+\mathbf w_1
=
\mathbf u_2+\mathbf w_2
\]

Then

\[
\mathbf u_1-\mathbf u_2
=
\mathbf w_2-\mathbf w_1
\]

The left-hand side belongs to $U$ and the right-hand side to $W$, so this vector belongs to $U\cap W$. If the intersection is the zero subspace, both differences are zero vectors, giving

\[
\mathbf u_1=\mathbf u_2,
\qquad
\mathbf w_1=\mathbf w_2
\]

## Core concept 4. The dimension formula subtracts shared directions once

For finite-dimensional subspaces,

\[
\dim(U+W)
=
\dim U+\dim W-\dim(U\cap W)
\]

Adding the dimensions of $U$ and $W$ counts the intersection's directions twice, so one copy is subtracted.

The basis-selection process explains this calculation. Let $k=\dim(U\cap W)$, $p=\dim U$, and $q=\dim W$. First choose a basis of $k$ vectors for the intersection. Extend it to a basis of $U$ by adding vectors outside the current span; this adds $p-k$ vectors. Extending the same intersection basis to a basis of $W$ adds $q-k$ vectors.

Taking the intersection basis once, together with the additional vectors from both sides, produces a spanning list for $U+W$. This list is also linearly independent.

Suppose a linear combination of the list equals 0. The combination of additional vectors from $U$ equals the negative of a combination of the common basis vectors and vectors from $W$. That vector therefore belongs to $U\cap W$. But the basis of $U$ includes both the common basis and its additional vectors. For a combination of the additional vectors to lie in the span of the common basis, all additional coefficients must be 0. Applying independence of the basis of $W$ to the remaining equation makes the remaining coefficients 0 as well.

The resulting basis has $k+(p-k)+(q-k)=p+q-k$ vectors. “Subtracting shared directions” thus means counting a basis of the common subspace only once, not finding identical columns in two arbitrarily chosen bases.

For a direct sum, $U\cap W=\{\mathbf 0\}$. The zero subspace has dimension 0, so

\[
\dim(U\oplus W)
=
\dim U+\dim W
\]

Matching dimensions alone does not establish a direct sum. Check both that the sum spans the entire space and that the intersection is the zero subspace.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Basis membership diagram with U directions e1 e2 and W directions e2 e3 sharing e2 so the sum has three independent directions](../../figures/assets/M03/M03-05-shared-basis-count.svg)
  <figcaption>In this small coordinate example, U=span{e₁,e₂} and W=span{e₂,e₃} share direction e₂. It appears only once in a basis of the sum, leaving three independent directions.</figcaption>
</figure>

The overlapping rectangles indicate which spaces contain each basis direction. They do not depict actual subspaces as finite rectangular regions.

## Core concept 5. A complement supplies the remaining directions of the whole space

A subspace $W$ satisfying $V=U\oplus W$ is called a complement of $U$. A subspace generally has multiple complements.

For example, with $V=\mathbb R^2$ and $U=\operatorname{span}\{(1,0)^\top\}$, both

\[
W_1=\operatorname{span}\{(0,1)^\top\}
\]

and

\[
W_2=\operatorname{span}\{(1,1)^\top\}
\]

are complements of $U$. Each line meets $U$ only at the zero vector and spans $\mathbb R^2$ together with $U$.

Decomposing the same vector $(a,b)^\top$ using these two complements gives

\[
\begin{bmatrix}a\\b\end{bmatrix}
=\underbrace{\begin{bmatrix}a\\0\end{bmatrix}}_{\in U}
+\underbrace{\begin{bmatrix}0\\b\end{bmatrix}}_{\in W_1}
=\underbrace{\begin{bmatrix}a-b\\0\end{bmatrix}}_{\in U}
+\underbrace{\begin{bmatrix}b\\b\end{bmatrix}}_{\in W_2}
\]

The decomposition is unique once either complement is fixed, but changing the complement may also change the $U$ component. A complement is therefore a subspace chosen for the decomposition, not a remainder automatically determined by the vector. A direct sum does not require orthogonality; $W_2$ is not orthogonal to $U$ under the Euclidean inner product.

Once an inner product is specified, the orthogonal complement can be chosen:

\[
U^\perp
=
\{\mathbf v\in V:\langle\mathbf v,\mathbf u\rangle=0
\text{ for every }\mathbf u\in U\}
\]

In a finite-dimensional inner product space,

\[
V=U\oplus U^\perp
\]

Membership in $U^\perp$ requires orthogonality to every vector of $U$, not just one. In calculations, it suffices to check that the inner product with every basis vector of $U$ is 0. Every $\mathbf u\in U$ is a linear combination of those basis vectors, so linearity of the inner product gives 0 for all remaining vectors as well. Changing the inner product changes this test and may therefore change the orthogonal complement.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Vector three two decomposed into a horizontal U component and vertical W1 component on a coordinate grid](../../figures/assets/M03/M03-05-vertical-complement.svg)
  <figcaption>Substituting (3,2) for (a,b) in the text, the vertical complement W₁ gives the U component (3,0)ᵀ and W₁ component (0,2)ᵀ.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![The same vector three two decomposed into horizontal component one zero and diagonal complement component two two](../../figures/assets/M03/M03-05-diagonal-complement.svg)
  <figcaption>Choosing the diagonal complement W₂ changes the same vector's U component to (1,0)ᵀ. Even in a direct sum whose subspaces meet only at the origin, the two components need not be orthogonal.</figcaption>
</figure>

The green vector is the same in both figures, but the blue component differs. Uniqueness is a property that holds after one complement is fixed.

## Core concept 6. Orthogonal projection calculates the two components of an orthogonal direct sum

In Euclidean space $\mathbb R^n$, let $\mathbf P_U$ be the matrix of orthogonal projection onto $U$. Then

\[
\mathbf x
=
\underbrace{\mathbf P_U\mathbf x}_{\mathbf x_U\in U}
+
\underbrace{(\mathbf I-\mathbf P_U)\mathbf x}_{\mathbf x_\perp\in U^\perp}
\]

The two components are orthogonal.

\[
\langle\mathbf x_U,\mathbf x_\perp\rangle=0
\]

Requiring the residual to belong to $U^\perp$ is stronger than requiring it to be orthogonal to the single vector $\mathbf x_U$. As in M02-09, stack an orthonormal basis of $U$ as columns of $\mathbf Q$. Then $\mathbf P_U=\mathbf Q\mathbf Q^\top$, and

\[
\mathbf Q^\top\mathbf x_\perp
=\mathbf Q^\top(\mathbf I-\mathbf Q\mathbf Q^\top)\mathbf x
=\mathbf Q^\top\mathbf x-\mathbf Q^\top\mathbf x
=\mathbf 0
\]

The residual has inner product 0 with every basis vector and is therefore orthogonal to every vector of $U$. Thus, every $\mathbf x$ belongs to $U+U^\perp$. Also, if $\mathbf z\in U\cap U^\perp$, it is orthogonal to itself: $\langle\mathbf z,\mathbf z\rangle=0$, implying $\mathbf z=\mathbf 0$. Together, these two conditions establish that the sum is direct.

Expanding the squared norm of the sum adds $2\langle\mathbf x_U,\mathbf x_\perp\rangle$ to the squared norms of the two components. Orthogonality makes this cross term 0, giving the Pythagorean relationship

\[
\|\mathbf x\|_2^2
=
\|\mathbf x_U\|_2^2+\|\mathbf x_\perp\|_2^2
\]

This decomposition is unique for a fixed subspace $U$ and inner product.

## Example 1. A direct sum of coordinate subspaces

### Problem

In $V=\mathbb R^3$, let

\[
U=\operatorname{span}
\left\{
\begin{bmatrix}1\\0\\0\end{bmatrix},
\begin{bmatrix}0\\1\\0\end{bmatrix}
\right\},
\qquad
W=\operatorname{span}
\left\{
\begin{bmatrix}0\\0\\1\end{bmatrix}
\right\}
\]

Verify $V=U\oplus W$ and decompose

\[
\mathbf x=
\begin{bmatrix}
2\\
-1\\
4
\end{bmatrix}
\]

### Solution

Vectors in $U$ have the form $(a,b,0)^\top$, and vectors in $W$ have the form $(0,0,c)^\top$. Only the zero vector has both forms, so

\[
U\cap W=\{\mathbf 0\}
\]

Every $(x_1,x_2,x_3)^\top$ can be written as

\[
\begin{bmatrix}
x_1\\x_2\\x_3
\end{bmatrix}
=
\begin{bmatrix}
x_1\\x_2\\0
\end{bmatrix}
+
\begin{bmatrix}
0\\0\\x_3
\end{bmatrix}
\]

so $U+W=V$. Hence, $V=U\oplus W$.

The given vector decomposes as

\[
\mathbf x
=
\underbrace{
\begin{bmatrix}
2\\-1\\0
\end{bmatrix}}_{\in U}
+
\underbrace{
\begin{bmatrix}
0\\0\\4
\end{bmatrix}}_{\in W}
\]

### Meaning of the result

$U$ contains the first two coordinate components, and $W$ contains the third. Because the two subspaces have no nonzero overlap, separating the three coordinates into these two components is unique.

## Example 2. A sum that is not direct

### Problem

In $V=\mathbb R^2$, let

\[
U=\operatorname{span}\{\mathbf e_1\},
\qquad
W=\mathbb R^2
\]

Calculate $U+W$ and $U\cap W$, and give two different decompositions of $\mathbf e_1$.

### Solution

Since $U\subset W$,

\[
U+W=W=\mathbb R^2
\]

and

\[
U\cap W=U
\]

The intersection contains the nonzero vector $\mathbf e_1$, so the sum is not direct.

\[
\mathbf e_1
=
\mathbf e_1+\mathbf 0
\]

and

\[
\mathbf e_1
=
\mathbf 0+\mathbf e_1
\]

are different decompositions, each with its first component in $U$ and second component in $W$.

### Meaning of the result

The condition that two subspaces span the entire space does not by itself give a unique component decomposition.

## Example 3. Decomposing an activation into a direction and residual

Let $U=\operatorname{span}\{\mathbf u\}$ be the subspace generated by the normalized direction

\[
\mathbf u
=
\frac{1}{\sqrt2}
\begin{bmatrix}
1\\
1\\
0
\end{bmatrix}
\]

The $U$ component of the activation

\[
\mathbf h=
\begin{bmatrix}
3\\
1\\
2
\end{bmatrix}
\]

is

\[
\mathbf h_U
=
(\mathbf u^\top\mathbf h)\mathbf u
=
\frac{4}{\sqrt2}
\frac{1}{\sqrt2}
\begin{bmatrix}
1\\1\\0
\end{bmatrix}
=
\begin{bmatrix}
2\\2\\0
\end{bmatrix}
\]

The residual is

\[
\mathbf h_\perp
=
\mathbf h-\mathbf h_U
=
\begin{bmatrix}
1\\-1\\2
\end{bmatrix}
\]

The inner product of the two vectors is

\[
\mathbf h_U^\top\mathbf h_\perp
=
2\cdot1+2\cdot(-1)+0\cdot2
=
0
\]

Also,

\[
\|\mathbf h\|_2^2=14,
\qquad
\|\mathbf h_U\|_2^2=8,
\qquad
\|\mathbf h_\perp\|_2^2=6
\]

so the squared norms add as well.

This calculation determines an activation component along the chosen direction. Whether that direction represents a concept and whether the model uses the component for prediction require separate verification through data and interventions.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Three dimensional example activation h three one two split into its U projection two two zero and perpendicular residual one minus one two](../../figures/assets/M03/M03-05-activation-orthogonal-decomposition.svg)
  <figcaption>Adding the blue projection component and orange residual in Example 3 reaches the green activation. The dashed line shows the residual translated to the projection endpoint; the residual is orthogonal to the U direction.</figcaption>
</figure>

A right angle need not look like a right angle in a projected three-dimensional view. Verify orthogonality by calculating an inner product of 0 from the displayed coordinates.

<figure class="lesson-figure" markdown="1">
  ![Area partition with common height and widths proportional to eight and six representing orthogonal component squared lengths totaling fourteen](../../figures/assets/M03/M03-05-pythagorean-partition.svg)
  <figcaption>The two regions have the same height and areas proportional to the component squared norms 8 and 6. Orthogonality removes the cross term, giving total squared norm 14; this does not add the lengths themselves as 8 and 6.</figcaption>
</figure>

## Common misconceptions

### Misconception 1. $U+W$ is $U\cup W$

$U+W$ contains every result of choosing one vector from $U$ and another from $W$ and adding them. It may be larger than the union.

### Misconception 2. Two subspaces spanning the whole space form a direct sum

Spanning the whole space means $U+W=V$. A direct sum also requires $U\cap W=\{\mathbf 0\}$.

### Misconception 3. There is only one complement

There may be several general complements. Fixing an inner product determines the orthogonal complement $U^\perp$.

### Misconception 4. Subspace projection is independent of the basis and metric

Changing the chosen inner product can change orthogonality and orthogonal projection even for the same abstract subspace. When using coordinate matrices, check both the basis and the inner product.

## Exercises

### 1. A subspace sum

For subspaces $U=\operatorname{span}\{\mathbf e_1\}$ and $W=\operatorname{span}\{\mathbf e_2\}$ of $\mathbb R^2$, calculate $U+W$.

<details>
<summary>Show solution</summary>

Any $(a,b)^\top$ can be written as

\[
\begin{bmatrix}
a\\b
\end{bmatrix}
=
a\mathbf e_1+b\mathbf e_2
\]

The first term belongs to $U$ and the second to $W$, so $U+W=\mathbb R^2$.

</details>

### 2. Identifying a direct sum

For

\[
U=\operatorname{span}
\left\{
\begin{bmatrix}1\\1\end{bmatrix}
\right\},
\qquad
W=\operatorname{span}
\left\{
\begin{bmatrix}1\\-1\end{bmatrix}
\right\}
\]

determine whether $\mathbb R^2=U\oplus W$.

<details>
<summary>Show solution</summary>

The two generating vectors are not scalar multiples of one another, so they are linearly independent. The two lines therefore intersect only at the zero vector, and the two vectors span $\mathbb R^2$. Hence, $\mathbb R^2=U\oplus W$.

</details>

### 3. Calculating a direct-sum decomposition

For $U,W$ in Exercise 2, decompose $\mathbf x=(4,2)^\top$ as $\mathbf u+\mathbf w$.

<details>
<summary>Show solution</summary>

From

\[
\begin{bmatrix}
4\\2
\end{bmatrix}
=a
\begin{bmatrix}
1\\1
\end{bmatrix}
+b
\begin{bmatrix}
1\\-1
\end{bmatrix}
\]

we obtain $a+b=4$ and $a-b=2$. Solving these equations gives $a=3$ and $b=1$. Thus,

\[
\mathbf u=
\begin{bmatrix}
3\\3
\end{bmatrix},
\qquad
\mathbf w=
\begin{bmatrix}
1\\-1
\end{bmatrix}
\]

</details>

### 4. The dimension formula

Given $\dim U=4$, $\dim W=3$, and $\dim(U\cap W)=2$, calculate $\dim(U+W)$.

<details>
<summary>Show solution</summary>

\[
\dim(U+W)
=
4+3-2
=
5
\]

The two common directions were counted twice, so one copy is subtracted.

</details>

### 5. Multiple complements

Give two lines that can complement $U=\operatorname{span}\{(1,0)^\top\}$ and one line that cannot.

<details>
<summary>Show solution</summary>

\[
\operatorname{span}\{(0,1)^\top\},
\qquad
\operatorname{span}\{(1,1)^\top\}
\]

are complements: each meets $U$ only at the zero vector and spans $\mathbb R^2$ together with it. The subspace $U$ itself cannot complement $U$, because their intersection is $U$.

</details>

### 6. Projection decomposition

Given $U=\operatorname{span}\{(1,0)^\top\}$ and $\mathbf x=(3,-2)^\top$, calculate $\mathbf x_U$ and $\mathbf x_\perp$.

<details>
<summary>Show solution</summary>

Orthogonal projection onto $U$ retains only the first coordinate, so

\[
\mathbf x_U=
\begin{bmatrix}
3\\0
\end{bmatrix}
\]

The residual is

\[
\mathbf x_\perp
=
\mathbf x-\mathbf x_U
=
\begin{bmatrix}
0\\-2
\end{bmatrix}
\]

The two components are orthogonal and sum to the original vector.

</details>

### 7. Critiquing a model claim

Critique the conclusion: “A concept probe achieved high accuracy from subspace $U$, so the model uses only $U$ for prediction.”

<details>
<summary>Show solution</summary>

The probe result provides evidence that concept information can be recovered from $U$. It does not establish whether the model uses $U$ functionally, whether $U^\perp$ contains redundant information, or whether removing $U$ changes prediction. Further interventions are needed, including removal of the $U$ component, comparison subspaces, and matched controls.

</details>

## Lesson summary

- $U+W$ is the subspace formed by adding vectors chosen from the two subspaces.
- A direct sum $U\oplus W$ has the zero subspace as its intersection and provides a unique decomposition of each vector.
- The dimension of a subspace sum is the sum of the two dimensions minus the dimension of the intersection.
- There may be multiple complements; a specified inner product allows an orthogonal complement to be chosen.
- Orthogonal projection uniquely separates a vector into a subspace component and an orthogonal residual.
- Information recovery from a subspace and functional use by a model are different claims.

## Pass criteria

You pass if you can answer the following without referring to the material:

- Can you define $U+W$ and $U\cap W$ and calculate them in examples?
- Can you determine whether a sum of two subspaces is direct?
- Can you explain why a direct-sum decomposition is unique?
- Can you apply the dimension formula?
- Can you distinguish a complement from an orthogonal complement?
- Can you calculate a projection component and residual?
- Can you limit claims to those supported by subspace analysis?

## Next lesson

- [M03-06 Equivalence relations and quotient spaces](M03-06-equivalence-relations-quotient-spaces.md)

## Author checklist

- [x] Learning objectives are expressed as observable actions.
- [x] A subspace sum is distinguished from a union.
- [x] The two direct-sum conditions and uniqueness are explained.
- [x] The dimension formula and orthogonal decomposition are calculated.
- [x] Nonuniqueness of complements is stated.
- [x] Every exercise has a solution.
- [x] The strengths of model interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] No knowledge beyond the prerequisites is implicitly required.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
