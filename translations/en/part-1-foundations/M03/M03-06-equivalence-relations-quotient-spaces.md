---
id: "M03-06"
title: "Equivalence relations and quotient spaces"
part: 1
stage: "M03"
status: "complete"
prerequisites:
  - "M03-01"
  - "M03-02"
  - "M03-05"
estimated_time: "120~145 minutes"
---

# M03-06. Equivalence relations and quotient spaces

## Why this lesson matters

Treating different representations as the same object requires a criterion for “the same.” An equivalence relation groups elements into disjoint equivalence classes. In a vector space, grouping vectors that differ only along a specified subspace produces a quotient space.

This structure appears when ignoring particular nuisance directions in model representations or grouping parameters that represent the same function because of parameter symmetries. Without specifying which differences are discarded, we cannot determine what information a quotient space preserves or loses.

## Learning objectives

After completing this lesson, you will be able to:

- Test for an equivalence relation using reflexivity, symmetry, and transitivity.
- Distinguish equivalence classes from representatives and explain why the classes partition a set.
- Define $\mathbf v\sim\mathbf w$ using a subspace $U$ and verify the three conditions.
- Calculate elements, addition, and scalar multiplication in a quotient space $V/U$.
- Determine the kernel of a quotient map and the dimension of a quotient space.
- Distinguish a quotient from orthogonal projection and parameter symmetries.

## Prerequisite check

- Prerequisite lesson: [M03-01 Abstract vector spaces](M03-01-abstract-vector-spaces.md)
- Prerequisite lesson: [M03-02 Linear maps and matrix representations](M03-02-linear-maps-matrix-representation.md)
- Prerequisite lesson: [M03-05 Subspaces, direct sums, and decomposition](M03-05-subspaces-direct-sums-decomposition.md)
- Check: Can you explain closure of a subspace under addition and scalar multiplication?
- Check: Can you calculate the kernel and image of a linear map?

Review the prerequisite lessons first if subspaces or kernels are unclear.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Scope |
|---|---|---|---|
| $x\sim y$ | `x is equivalent to y` | Treating two elements as the same under a specified criterion | Requires an equivalence relation |
| $[x]$ | `the equivalence class of x` | The set of all elements equivalent to $x$ | $x$ is a representative |
| $\mathbf v+U$ | `v plus U` | The set obtained by adding every vector in $U$ to $\mathbf v$ | A coset of $U$ |
| $V/U$ | `V mod U` | The set of equivalence classes ignoring differences along $U$ | A quotient space |
| $\pi:V\to V/U$ | `pi maps V to V mod U` | The quotient map sending each vector to its equivalence class | $\pi(\mathbf v)=\mathbf v+U$ |
| representative | `representative` | An element chosen to denote an equivalence class | A class has multiple representatives |

## Core concept 1. An equivalence relation specifies which elements are treated as the same

For a relation $\sim$ on a set $X$ to be an equivalence relation, it must satisfy these conditions for all $x,y,z\in X$:

1. Reflexivity: $x\sim x$
2. Symmetry: If $x\sim y$, then $y\sim x$
3. Transitivity: If $x\sim y$ and $y\sim z$, then $x\sim z$

On the integers, the definition

\[
a\sim b
\quad\Longleftrightarrow\quad
a-b\text{ is a multiple of }3
\]

gives an equivalence relation. Each integer belongs to one of three classes with remainders 0, 1, and 2.

Reflexivity uses $a-a=0=3\cdot0$. For symmetry, if an integer $k$ satisfies $a-b=3k$, then $b-a=3(-k)$ is also a multiple of 3. For transitivity, adding $a-b=3k$ and $b-c=3\ell$ gives $a-c=3(k+\ell)$. The criterion therefore remains consistent when elements in one class are exchanged for comparison.

If even one condition is missing, the classes may fail to form consistent groups. For example, $x\le y$ on the real numbers is reflexive and transitive but not symmetric.

## Core concept 2. An equivalence class groups equivalent elements together

The equivalence class of $x\in X$ is defined as

\[
[x]
=
\{y\in X:y\sim x\}
\]

The element $x$ is one representative of the class.

If $x\sim y$, then

\[
[x]=[y]
\]

If $x$ and $y$ are not equivalent, their classes are disjoint. The classes therefore divide $X$ into disjoint subsets, forming a partition.

A representative is not unique. Any element of the same equivalence class denotes the same group.

The two partition conditions—covering the whole set and having no overlap—can be checked separately. Reflexivity gives $x\in[x]$, so every element belongs to at least one class. If $x\sim y$ and $z\in[x]$, then $z\sim x\sim y$, giving $z\in[y]$. The reverse inclusion follows in the same way, so $[x]=[y]$.

If two classes share an element $z$, then $z\sim x$ and $z\sim y$. Symmetry and transitivity give $x\sim z\sim y$, so the entire classes are equal. Classes cannot overlap only partially: they are either the same group or disjoint groups.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Integers displayed in three disjoint remainder-modulo-three classes with one and four highlighted as representatives of the same class](../../figures/assets/M03/M03-06-mod-three-partition.svg)
  <figcaption>The displayed integers are divided into three rows by remainders 0, 1, and 2. The different numbers 1 and 4 represent the same class because their difference is a multiple of 3. Each row continues in both directions, and every integer belongs to exactly one row.</figcaption>
</figure>

One point is a representative; all elements in its row together form the equivalence class.

## Core concept 3. Differences along a subspace can define equivalence

Let $U\le V$. For two vectors $\mathbf v,\mathbf w\in V$, define

\[
\mathbf v\sim_U\mathbf w
\quad\Longleftrightarrow\quad
\mathbf v-\mathbf w\in U
\]

This is an equivalence relation.

Reflexivity follows from

\[
\mathbf v-\mathbf v=\mathbf 0\in U
\]

For symmetry, if $\mathbf v-\mathbf w\in U$, then

\[
\mathbf w-\mathbf v=-(\mathbf v-\mathbf w)\in U
\]

Transitivity follows from

\[
\mathbf v-\mathbf z
=
(\mathbf v-\mathbf w)+(\mathbf w-\mathbf z)\in U
\]

These steps use the fact that $U$ contains the zero vector and is closed under scalar multiplication and addition.

## Core concept 4. An equivalence class is a translated subspace

The equivalence class of $\mathbf v$ can be written as

\[
[\mathbf v]
=
\{\mathbf w\in V:\mathbf w-\mathbf v\in U\}
=
\mathbf v+U
\]

Here,

\[
\mathbf v+U
=
\{\mathbf v+\mathbf u:\mathbf u\in U\}
\]

is called a coset of $U$.

The sets in the first equation are equal because $\mathbf w-\mathbf v=\mathbf u\in U$ can be rewritten as $\mathbf w=\mathbf v+\mathbf u$. Conversely, a vector $\mathbf w=\mathbf v+\mathbf u$ has difference $\mathbf u\in U$. The equivalence class defined by differences and the coset defined by translation therefore contain the same elements.

If $\mathbf u_0\in U$, then $\mathbf v$ and $\mathbf v+\mathbf u_0$ denote the same coset.

\[
(\mathbf v+\mathbf u_0)+U
=
\mathbf v+U
\]

Thus, $\mathbf v$ is a representative used to name the class, not the class itself.

The translated set remains the same because $\mathbf u_0+U=U$. Closure of $U$ under addition gives one inclusion. Writing any $\mathbf u\in U$ as $\mathbf u_0+(\mathbf u-\mathbf u_0)$ gives the reverse inclusion. In particular, if $\mathbf v\in U$, then $\mathbf v+U=U$. If $\mathbf v\notin U$, its coset does not contain the zero vector and is not a subspace of the original space $V$. In the quotient space, each such set is treated as one new vector.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Horizontal cosets at heights zero three and four with horizontal displacement between two equivalent representatives and vertical displacement to a different class](../../figures/assets/M03/M03-06-parallel-cosets.svg)
  <figcaption>In Example 1, (2,3)ᵀ and (5,3)ᵀ lie on the same horizontal line. Their horizontal difference belongs to U, whereas the vertical difference to (2,4)ᵀ does not, placing that point in another class.</figcaption>
</figure>

The whole horizontal line is one coset. Only the line at height 0 is the subspace $U$ containing the origin; lines at other heights are its translations.

## Core concept 5. A quotient space uses equivalence classes as vectors

The set of all cosets is written as

\[
V/U
=
\{\mathbf v+U:\mathbf v\in V\}
\]

Define these operations on it:

\[
(\mathbf v+U)+(\mathbf w+U)
=
(\mathbf v+\mathbf w)+U
\]

\[
\alpha(\mathbf v+U)
=
(\alpha\mathbf v)+U
\]

Choosing different representatives must give the same resulting class. This is what it means for an operation to be well-defined.

Suppose $\mathbf v'=\mathbf v+\mathbf u_1$ and $\mathbf w'=\mathbf w+\mathbf u_2$, with $\mathbf u_1,\mathbf u_2\in U$. Then

\[
(\mathbf v'+\mathbf w')-(\mathbf v+\mathbf w)
=
\mathbf u_1+\mathbf u_2\in U
\]

and therefore

\[
(\mathbf v'+\mathbf w')+U
=
(\mathbf v+\mathbf w)+U
\]

For scalar multiplication, $\alpha\mathbf v'-\alpha\mathbf v=\alpha\mathbf u_1\in U$ also makes the result the same coset after changing the representative. This includes $\alpha=0$.

Under these operations, the zero vector is $\mathbf 0+U=U$ itself. It is the additive identity because $(\mathbf v+U)+U=\mathbf v+U$. Adding $(-\mathbf v)+U$ gives $U$, so additive inverses also exist. Associativity of addition and the distributive laws follow from the original space by calculating with representatives and then taking classes. Because the result does not depend on the representatives chosen, laws checked with particular representatives also hold for the classes.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Two vector addition paths using different horizontal representatives reach different points on the same height-seven result coset](../../figures/assets/M03/M03-06-representative-independent-addition.svg)
  <figcaption>The solid path adds the representatives (2,3)ᵀ and (−1,4)ᵀ from Example 2. The dashed path adds different representatives, (5,3)ᵀ and (2,4)ᵀ, from the respective cosets. Their endpoints differ, but both reach the same line at height 7.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Representative vector two three doubled to four six with the input and result cosets shown as horizontal lines at heights three and six](../../figures/assets/M03/M03-06-coset-scalar-multiplication.svg)
  <figcaption>Placing two copies of the displacement represented by (2,3)ᵀ end to end reaches its double (4,6)ᵀ. The quotient-space result is not this single point, but the entire horizontal line at height 6.</figcaption>
</figure>

The figures distinguish calculations with representatives from the resulting equivalence classes. Changing the first coordinate does not change the resulting coset.

## Core concept 6. The quotient map has the discarded directions as its kernel

The quotient map

\[
\pi:V\to V/U,
\qquad
\pi(\mathbf v)=\mathbf v+U
\]

is linear. The quotient-space element corresponding to the zero vector is

\[
U=\mathbf 0+U
\]

Thus,

\[
\ker\pi
=
\{\mathbf v:\mathbf v+U=U\}
=
U
\]

The map $\pi$ sends directions in $U$ to the zero vector and sends vectors differing only along $U$ to the same output.

Linearity follows from the definitions of quotient-space operations.

\[
\pi(\alpha\mathbf v+\beta\mathbf w)
=(\alpha\mathbf v+\beta\mathbf w)+U
=\alpha(\mathbf v+U)+\beta(\mathbf w+U)
=\alpha\pi(\mathbf v)+\beta\pi(\mathbf w)
\]

In the kernel equation, $\mathbf v+U=U$ is equivalent to $\mathbf v\in U$. If $\mathbf v\in U$, the translation property above gives coset $U$. Conversely, if the coset is $U$, its representative $\mathbf v=\mathbf v+\mathbf 0$ also belongs to $U$. Every quotient-space element has the form $\mathbf v+U$, so its representative $\mathbf v$ is an input of the quotient map. This explains why the image is the entire quotient space.

In finite dimensions, applying the rank-nullity theorem gives

\[
\dim(V/U)
=
\dim V-\dim U
\]

because the quotient map's image is all of $V/U$ and its kernel is $U$.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Quotient map sends every point of each horizontal coset to one quotient class with the entire horizontal subspace mapping to the zero class](../../figures/assets/M03/M03-06-quotient-map-collapse.svg)
  <figcaption>Every point at a given height on the left maps to one coset on the right. Inputs mapping to the zero vector include the whole horizontal subspace U, not just the origin, so the quotient map's kernel is U.</figcaption>
</figure>

Each rectangle on the right represents a coset as an element, not one representative point. Even after horizontal differences are discarded, cosets at different heights remain distinct.

## Core concept 7. Quotienting by the kernel gives the same linear structure as the image

For a linear map $T:V\to W$, if

\[
\mathbf v-\mathbf w\in\ker T
\]

then

\[
T(\mathbf v)-T(\mathbf w)
=
T(\mathbf v-\mathbf w)
=
\mathbf 0
\]

so $T(\mathbf v)=T(\mathbf w)$. The map $T$ does not distinguish inputs belonging to the same kernel coset.

The converse also holds. If $T(\mathbf v)=T(\mathbf w)$, linearity gives $T(\mathbf v-\mathbf w)=\mathbf 0$, placing the difference in the kernel. “Having the same output” and “belonging to the same kernel coset” are therefore exactly equivalent conditions.

We can accordingly define

\[
\widetilde T:V/\ker T\to\operatorname{im}T,
\qquad
\widetilde T(\mathbf v+\ker T)=T(\mathbf v)
\]

This is an injective and surjective linear map, so we write

\[
V/\ker T\cong\operatorname{im}T
\]

Removing the directions lost by a linear map through its kernel leaves an input structure corresponding to the actual output structure.

The map $\widetilde T$ is well-defined because choosing another representative of the same coset leaves the output $T(\mathbf v)$ unchanged. If two different cosets had the same output, the converse just proved would force those cosets to be equal, establishing injectivity. Every vector in $\operatorname{im}T$ is some $T(\mathbf v)$ and can be obtained from $\mathbf v+\ker T$, establishing surjectivity. Finally, linear combinations of cosets are calculated using their representatives. Since $T$ preserves those combinations, $\widetilde T$ is linear.

The symbol $\cong$ means a one-to-one correspondence preserving linear combinations, not literal equality of sets. Elements on the left are cosets of input vectors; elements on the right are actual output vectors. This correspondence alone does not imply preservation of lengths or angles.

## Example 1. Quotienting the plane by one direction

### Problem

Consider $V=\mathbb R^2$ and

\[
U=\operatorname{span}
\left\{
\begin{bmatrix}1\\0\end{bmatrix}
\right\}
\]

Calculate the equivalence class of $\mathbf v=(2,3)^\top$ and determine whether $(5,3)^\top$ and $(2,4)^\top$ belong to the same class.

### Solution

The subspace $U$ is the $x$ axis, so

\[
\mathbf v+U
=
\left\{
\begin{bmatrix}
2+a\\
3
\end{bmatrix}
:a\in\mathbb R
\right\}
\]

This is the horizontal line at height 3.

\[
\begin{bmatrix}5\\3\end{bmatrix}
-
\begin{bmatrix}2\\3\end{bmatrix}
=
\begin{bmatrix}3\\0\end{bmatrix}
\in U
\]

so $(5,3)^\top$ belongs to the same class.

\[
\begin{bmatrix}2\\4\end{bmatrix}
-
\begin{bmatrix}2\\3\end{bmatrix}
=
\begin{bmatrix}0\\1\end{bmatrix}
\notin U
\]

so $(2,4)^\top$ belongs to another class.

### Meaning of the result

In $V/U$, first-coordinate differences are ignored, and only second coordinates are distinguished. Each quotient-space element is a horizontal line, not a single point.

## Example 2. Calculating quotient-space operations

### Problem

For $U$ in Example 1 and

\[
\mathbf v=
\begin{bmatrix}2\\3\end{bmatrix},
\qquad
\mathbf w=
\begin{bmatrix}-1\\4\end{bmatrix}
\]

calculate $(\mathbf v+U)+(\mathbf w+U)$ and $2(\mathbf v+U)$.

### Solution

\[
(\mathbf v+U)+(\mathbf w+U)
=
(\mathbf v+\mathbf w)+U
=
\begin{bmatrix}
1\\7
\end{bmatrix}
+U
\]

This coset is the horizontal line at height 7.

\[
2(\mathbf v+U)
=
(2\mathbf v)+U
=
\begin{bmatrix}
4\\6
\end{bmatrix}
+U
\]

This is the horizontal line at height 6.

### Meaning of the result

The first coordinate may depend on the representative. The resulting classes are determined by the second coordinates 7 and 6.

## Example 3. Removing constant terms for a differentiation map

The differentiation map

\[
D:\mathcal P_2\to\mathcal P_1,
\qquad
D(p)=p'
\]

has the space of constant polynomials as its kernel:

\[
\ker D=\operatorname{span}\{1\}
\]

The polynomials $p(t)=2+3t+t^2$ and $q(t)=-5+3t+t^2$ differ only in their constant terms, so

\[
p-q=7\in\ker D
\]

and belong to the same class. Indeed,

\[
D(p)=3+2t=D(q)
\]

The quotient space $\mathcal P_2/\ker D$ ignores constant-term differences. Each class is distinguished by the two coefficients of $bt+ct^2$, so its dimension is 2.

\[
\dim(\mathcal P_2/\ker D)
=
3-1
=
2
\]

The differentiation map's image, $\mathcal P_1$, also has dimension 2. The map sending $p+\ker D$ to $p'$ connects the two spaces.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Two example polynomials differing only by the constant seven and their shared derivative three plus two t](../../figures/assets/M03/M03-06-derivative-class-image.svg)
  <figcaption>The two input curves differ by the constant 7, but share one green derivative curve. One input coset grouping constant differences corresponds to one actual output polynomial.</figcaption>
</figure>

The blue and purple curves show only two representatives of the coset. Changing the constant term to any value leaves the same coset and derivative.

## Example 4. Ignoring a nuisance subspace in a representation

Suppose an analyst specifies a subspace $U$ of nuisance directions in activation space $V=\mathbb R^d$. The quotient representation

\[
\mathbf h+U
\]

treats $\mathbf h$ and $\mathbf h+\mathbf u$ as the same element for every $\mathbf u\in U$.

A quotient space does not automatically choose a representative. The Euclidean inner product can be used to select

\[
\operatorname{proj}_{U^\perp}\mathbf h
\]

as a representative, but this additionally selects an orthogonal complement and a metric. The quotient itself specifies only the equivalence relation that ignores differences along $U$.

In the orthogonal decomposition $\mathbf h=\mathbf h_U+\mathbf h_\perp$ from M03-05, $\mathbf h-\mathbf h_\perp=\mathbf h_U\in U$, so $\mathbf h_\perp$ represents the same coset. If a coset had two representatives in $U^\perp$, their difference would belong to both $U$ and $U^\perp$, making it the zero vector. Thus, fixing this inner product allows a unique orthogonal residual to be chosen from each coset.

An incorrectly chosen nuisance subspace can also eliminate task-relevant information within the equivalence classes. Using quotient results requires reporting both the basis for choosing $U$ and task performance before and after removal.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Whole height-three quotient class with the Euclidean perpendicular complement selecting its single representative zero three](../../figures/assets/M03/M03-06-quotient-versus-representative.svg)
  <figcaption>Forming a quotient that groups the whole horizontal line and projecting onto the vertical Euclidean orthogonal complement to select (0,3)ᵀ are different steps. The selected point is a representative of the same coset, not the coset itself.</figcaption>
</figure>

## Common misconceptions

### Misconception 1. A relation based on apparent similarity is an equivalence relation

An equivalence relation must satisfy reflexivity, symmetry, and transitivity. Being within a distance threshold may fail transitivity.

### Misconception 2. An equivalence class is one representative

A representative is an element used to denote a class. The class is the set of all elements equivalent to that representative.

### Misconception 3. $V/U$ divides vectors componentwise

$V/U$ is not scalar division. It is a new vector space formed by grouping vectors differing along $U$ into the same element.

### Misconception 4. A quotient is the same as orthogonal projection

A quotient uses equivalence classes as elements. Orthogonal projection is one way to select a particular representative of each class using an inner product and a complement.

### Misconception 5. Every quotient by model symmetries is a vector space

A quotient defined by additive differences in a subspace is a vector space. Classes arising from neuron permutations or nonlinear reparameterizations may not form an ordinary vector-space quotient.

## Exercises

### 1. Testing an equivalence relation

On the integers, define

\[
a\sim b
\quad\Longleftrightarrow\quad
a-b\text{ is even}
\]

Verify reflexivity, symmetry, and transitivity.

<details>
<summary>Show solution</summary>

Since $a-a=0$ is even, the relation is reflexive. If $a-b$ is even, then $b-a=-(a-b)$ is also even, giving symmetry. If $a-b$ and $b-c$ are even, their sum $a-c$ is even, giving transitivity. Thus, this is an equivalence relation.

</details>

### 2. Finding equivalence classes

Describe $[0]$ and $[1]$ for the relation in Exercise 1.

<details>
<summary>Show solution</summary>

$[0]$ is the set of all even integers, whose differences from 0 are even. $[1]$ is the set of all odd integers, whose differences from 1 are even. The two classes are disjoint, and every integer belongs to one of them.

</details>

### 3. Identifying a coset

For $V=\mathbb R^3$ and $U=\operatorname{span}\{\mathbf e_1,\mathbf e_2\}$, determine whether

\[
\mathbf v=
\begin{bmatrix}1\\2\\3\end{bmatrix},
\qquad
\mathbf w=
\begin{bmatrix}5\\-1\\3\end{bmatrix}
\]

denote the same coset.

<details>
<summary>Show solution</summary>

\[
\mathbf v-\mathbf w
=
\begin{bmatrix}
-4\\3\\0
\end{bmatrix}
\]

is a linear combination of $\mathbf e_1,\mathbf e_2$ and therefore belongs to $U$. Thus, $\mathbf v\sim_U\mathbf w$ and $\mathbf v+U=\mathbf w+U$.

</details>

### 4. Quotient-space operations

For $U$ in Exercise 3, calculate

\[
\left(
\begin{bmatrix}1\\0\\2\end{bmatrix}
+U
\right)
+
\left(
\begin{bmatrix}0\\4\\-1\end{bmatrix}
+U
\right)
\]

<details>
<summary>Show solution</summary>

Adding the representatives gives

\[
\begin{bmatrix}1\\0\\2\end{bmatrix}
+
\begin{bmatrix}0\\4\\-1\end{bmatrix}
=
\begin{bmatrix}1\\4\\1\end{bmatrix}
\]

so the result is

\[
\begin{bmatrix}1\\4\\1\end{bmatrix}
+U
\]

This quotient ignores first- and second-coordinate differences, so all vectors with third coordinate 1 belong to the same coset.

</details>

### 5. Quotient-space dimension

Given $\dim V=8$ and $\dim U=3$, calculate $\dim(V/U)$.

<details>
<summary>Show solution</summary>

\[
\dim(V/U)
=
\dim V-\dim U
=
8-3
=
5
\]

The rank-nullity theorem gives the same value because the quotient map has kernel $U$ and image all of $V/U$.

</details>

### 6. Quotient and image

The map $T:\mathbb R^3\to\mathbb R^2$ is given by

\[
T(x,y,z)^\top=(x,y)^\top
\]

Calculate $\ker T$, $\operatorname{im}T$, and the dimension of $\mathbb R^3/\ker T$.

<details>
<summary>Show solution</summary>

\[
\ker T
=
\operatorname{span}
\left\{
\begin{bmatrix}0\\0\\1\end{bmatrix}
\right\}
\]

and $\operatorname{im}T=\mathbb R^2$. Hence,

\[
\dim(\mathbb R^3/\ker T)
=
3-1
=
2
\]

The quotient's classes ignore third-coordinate differences, and each corresponds one-to-one to the output $(x,y)^\top$.

</details>

### 7. Critiquing a model claim

Critique the claim: “Taking the quotient by nuisance subspace $U$ leaves only semantic information.”

<details>
<summary>Show solution</summary>

The quotient removes every difference along $U$, but does not guarantee that those directions contain only nuisance information. If $U$ also contains task-relevant information, that information is lost as well. The analyst must examine the procedure for estimating $U$, its stability on independent data, recovery and task performance before and after quotienting, and comparison subspaces.

</details>

## Lesson summary

- An equivalence relation satisfies reflexivity, symmetry, and transitivity and partitions elements into equivalence classes.
- Given a subspace $U$, vectors can be considered equivalent when $\mathbf v-\mathbf w\in U$.
- The class $\mathbf v+U$ is a translated subspace $U$; its representative is not unique.
- The quotient space $V/U$ uses cosets as elements and has operations independent of representatives.
- The quotient map's kernel is $U$, and in finite dimensions, $\dim(V/U)=\dim V-\dim U$.
- $V/\ker T$ has the same linear structure as $\operatorname{im}T$.
- A quotient forms equivalence classes; orthogonal projection selects representatives using an additional inner product.

## Pass criteria

You pass if you can answer the following without referring to the material:

- Can you test whether a relation satisfies reflexivity, symmetry, and transitivity?
- Can you distinguish an equivalence class from a representative?
- Can you verify that a relation defined by a subspace is an equivalence relation?
- Can you calculate cosets and quotient-space operations?
- Can you calculate the kernel of a quotient map and the dimension of a quotient space?
- Can you explain the correspondence between $V/\ker T$ and $\operatorname{im}T$?
- Can you distinguish a quotient from orthogonal projection?

## Next lesson

- [M03-07 Dual spaces and covectors](M03-07-dual-spaces-covectors.md)

## Author checklist

- [x] Learning objectives are expressed as observable actions.
- [x] The three conditions for an equivalence relation are verified.
- [x] Equivalence classes, representatives, and cosets are distinguished.
- [x] Well-defined quotient-space operations are explained.
- [x] The quotient map is connected to its kernel and image.
- [x] Differences from orthogonal projection and general model symmetries are stated.
- [x] Every exercise has a solution.
- [x] The strengths of model interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
