---
id: "M02-07"
title: "Linear independence, bases, and dimension"
part: 1
stage: "M02"
status: "complete"
prerequisites:
  - "M02-02"
  - "M02-06"
estimated_time: "105~130 minutes"
---

# M02-07. Linear independence, bases, and dimension

## Why this lesson matters

Even when several vectors generate the same span, some may be replaceable by linear combinations of the others. Removing this redundancy leaves only the independent directions needed to generate the space. A set of independent directions that spans the entire space is a basis.

A basis lets us record an abstract vector using coordinates. Dimension is not the length of a particular array, but the number of basis vectors needed to represent a space. When interpreting neural network representations coordinate by coordinate, check how the chosen basis affects the conclusions.

## Learning objectives

After completing this lesson, you will be able to:

- Determine linear independence and dependence from coefficient conditions.
- Find and remove redundant vectors from a generating set.
- Explain a basis as a linearly independent generating set.
- Find coordinates relative to a basis and check their uniqueness.
- Calculate the dimensions of spaces and subspaces.
- Explain why coordinatewise model interpretations depend on the choice of basis.

## Prerequisite check

- Prerequisite lesson: [M02-02 Linear combinations and span](M02-02-linear-combinations-span.md)
- Prerequisite lesson: [M02-06 Linear systems and inverses](M02-06-linear-systems-inverse.md)
- Check question: Can you use coefficient equations to determine whether a target vector belongs to the span of given vectors?
- Check question: Can you find solutions to the homogeneous system $\mathbf A\mathbf c=\mathbf 0$ using row elimination?

If span or solving linear systems is unclear, first review the prerequisite lessons.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| Linear independence | `linear independence` | The only linear combination yielding the zero vector is the trivial one. | All coefficients must be 0. |
| Linear dependence | `linear dependence` | A nonzero coefficient combination yields the zero vector. | There are redundant directions among the vectors. |
| $\mathcal B=(\mathbf b_1,\ldots,\mathbf b_k)$ | `the basis B consisting of b one through b k` | Ordered list of linearly independent vectors spanning a space | Determines coordinate order |
| $[\mathbf v]_{\mathcal B}$ | `the coordinates of v in the basis B` | Coefficient vector expressing $\mathbf v$ using basis vectors | $k$-dimensional column vector |
| $\dim V$ | `the dimension of V` | Number of vectors in a basis of $V$ | Defined for finite-dimensional spaces |

## Core concept 1. Define linear independence using coefficients that produce zero

Vectors $\mathbf v_1,\ldots,\mathbf v_k$ are linearly independent if the only coefficients satisfying

\[
c_1\mathbf v_1+\cdots+c_k\mathbf v_k=\mathbf 0
\]

are

\[
c_1=\cdots=c_k=0
\]

If a solution includes even one nonzero coefficient, the vectors are linearly dependent. In a dependent set, at least one vector can be expressed as a linear combination of the others.

Setting every coefficient to 0 gives the zero vector for any list of vectors. Independence asks whether there is another way to make the sum 0 besides this common solution. Dependence does not require every coefficient to be nonzero. Even one nonzero coefficient makes the coefficient vector as a whole nonzero.

In a dependent combination, choose a coefficient $c_j\ne0$. Keep that term on one side, move the others to the opposite side, and divide by $c_j$.

\[
\mathbf v_j
=-\sum_{i\ne j}\frac{c_i}{c_j}\mathbf v_i
\]

This expresses that vector using the other vectors. Conversely, if one vector is a linear combination of the others, moving all terms to one side produces a nonzero coefficient combination yielding zero. In Example 2's $\mathbf v_3=\mathbf v_1+\mathbf v_2$, $(1,1,-1)$ is such a combination. Knowing that no pair among three vectors consists of multiples is not enough to determine independence of the entire list.

The figure below shows how three pairwise nonparallel vectors can still form a dependent list. Nonzero coefficients label a path whose sum returns to the origin.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three pairwise nonparallel vectors forming a closed head-to-tail path with coefficients one one minus one](../../figures/assets/M02/M02-07-nontrivial-zero.svg)

<figcaption>Adding the first two vectors and subtracting the third returns to the start. The coefficients (1,1,−1) are not all zero, so the three vectors are dependent. Checking only whether pairs are multiples cannot detect this redundancy.</figcaption>
</figure>

## Core concept 2. Assemble column vectors into a matrix to test independence

Set

\[
\mathbf A=
\begin{bmatrix}
\mathbf v_1&\cdots&\mathbf v_k
\end{bmatrix}
\]

Then

\[
\mathbf A\mathbf c=\mathbf 0
\]

is the same as

\[
c_1\mathbf v_1+\cdots+c_k\mathbf v_k=\mathbf 0
\]

If row elimination leaves a pivot in every coefficient column, only $\mathbf c=\mathbf 0$ is possible, so the columns are linearly independent. A free variable allows a nonzero solution, so the columns are linearly dependent.

The figure below compares whether each coefficient column in an eliminated homogeneous system has a pivot. On the right, freely choosing the third coefficient determines the other two accordingly.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Reduced augmented matrices comparing a pivot in every coefficient column with a nonpivot free column](../../figures/assets/M02/M02-07-pivots-and-free-column.svg)

<figcaption>Every coefficient on the left is determined to be 0. Choosing the free coefficient t=1 on the right gives the nonzero coefficient vector (−1,−1,1). With only two rows, there also cannot be pivots in all three coefficient columns.</figcaption>
</figure>

## Core concept 3. Zero vectors and too many vectors produce dependence

If a list contains $\mathbf 0$, setting only that vector's coefficient to 1 gives zero, so the list is linearly dependent.

More than $n$ vectors in $\mathbb R^n$ are linearly dependent. A matrix with more than $n$ columns cannot have a pivot in every column and therefore has free variables.

Having at most $n$ vectors, however, does not guarantee independence. Two vectors that are multiples are dependent even in $\mathbb R^n$.

## Core concept 4. A basis satisfies both independence and spanning

A vector list

\[
\mathcal B=(\mathbf b_1,\ldots,\mathbf b_k)
\]

is a basis of a space $V$ if it satisfies both conditions:

1. $\mathbf b_1,\ldots,\mathbf b_k$ are linearly independent.
2. $\operatorname{span}\{\mathbf b_1,\ldots,\mathbf b_k\}=V$.

Spanning alone may include unnecessary vectors. Independence alone may not generate the entire space.

The standard basis of $\mathbb R^n$,

\[
\mathcal E=(\mathbf e_1,\ldots,\mathbf e_n)
\]

satisfies both conditions.

A linear combination of the standard basis is $\sum_i c_i\mathbf e_i=(c_1,\ldots,c_n)^\top$. If this sum is zero, every component $c_i$ is 0, establishing independence. Choosing any target coordinates as coefficients produces that target vector, so the basis also spans the whole space.

The figure below fixes $\mathbb R^2$ as the target space and checks independence and spanning separately. Pale green shows the span obtainable from the chosen vectors.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three coordinate panels distinguishing independence alone, spanning alone, and both basis conditions](../../figures/assets/M02/M02-07-two-basis-conditions.svg)

<figcaption>One nonzero vector is independent but cannot span the whole plane. Adding a diagonal vector to the two standard basis vectors spans the plane but introduces redundancy. Keeping only the two standard basis vectors satisfies both conditions.</figcaption>
</figure>

## Core concept 5. Choosing a basis determines unique coordinates

If $\mathcal B=(\mathbf b_1,\ldots,\mathbf b_k)$ is a basis of $V$, every $\mathbf v\in V$ has an expression

\[
\mathbf v
=
c_1\mathbf b_1+\cdots+c_k\mathbf b_k
\]

The vector

\[
[\mathbf v]_{\mathcal B}
=
\begin{bmatrix}
c_1\\
\vdots\\
c_k
\end{bmatrix}
\]

is the coordinate vector of $\mathbf v$ relative to $\mathcal B$.

Spanning ensures at least one coefficient representation exists. Independence restricts it to one. If the same vector has coefficient lists $(c_1,\ldots,c_k)$ and $(d_1,\ldots,d_k)$, subtracting their representations gives

\[
\mathbf 0
=\sum_{i=1}^k(c_i-d_i)\mathbf b_i
\]

Independence of the basis vectors requires every difference $c_i-d_i$ to be 0. All corresponding coefficients agree, so the coordinates are unique. Spanning guarantees existence; independence guarantees uniqueness.

The axes below are representation coefficients $c_1,c_2$, not components of the original vector. On the left, the two component conditions for the target determine one coefficient pair. On the right, redundant generators leave freedom in the coefficients.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Coefficient-space plots showing a unique intersection for a basis and a line of coefficient pairs for redundant generators](../../figures/assets/M02/M02-07-coordinate-uniqueness.svg)

<figcaption>The basis (1,1), (1,−1) gives just one coefficient pair (3,1) for target (4,2). With redundant vectors (1,0), (2,0), the coefficients producing target (4,0) fill a line. This compares uniqueness of representation coefficients, not the positions of different targets.</figcaption>
</figure>

## Core concept 6. Dimension counts basis vectors

Every basis of a finite-dimensional space $V$ has the same number of vectors. Call that number

\[
\dim V
\]

We have

\[
\dim\mathbb R^n=n
\]

A line through the origin in $\mathbb R^3$ has one basis vector and dimension 1. A plane through the origin has two basis vectors and dimension 2.

Array shape and space dimension are related, but distinguish their contexts. If data in $\mathbb R^{100}$ all lie on one line through the origin and include a nonzero sample, the ambient space has dimension 100, while the subspace spanned by the data has dimension 1. Each sample uses 100 components for storage, but choosing one nonzero vector on the line as a basis represents each sample with one multiplier. If all samples are zero, there is no independent direction, and their span has dimension 0.

The figure below compares the independent directions needed for a line and a plane within the same ambient space $\mathbb R^3$. The perspective indicates containment of spaces; do not measure angles in this schematic drawing.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Schematic three-dimensional views of a one-dimensional line and a two-dimensional coordinate plane inside R three](../../figures/assets/M02/M02-07-subspace-dimensions.svg)

<figcaption>A vector on the line is a multiple of one nonzero basis vector; a vector in the coordinate plane uses coefficients of two independent basis vectors. Both require three stored components, but the subspaces have dimensions 1 and 2, respectively.</figcaption>
</figure>

## Core concept 7. Changing the basis changes coordinates

In $\mathbb R^2$,

\[
\mathcal E=
\left(
\begin{bmatrix}1\\0\end{bmatrix},
\begin{bmatrix}0\\1\end{bmatrix}
\right)
\]

and

\[
\mathcal B=
\left(
\begin{bmatrix}1\\1\end{bmatrix},
\begin{bmatrix}1\\-1\end{bmatrix}
\right)
\]

are different bases. The vector

\[
\mathbf v=
\begin{bmatrix}4\\2\end{bmatrix}
\]

has standard-basis coordinates

\[
[\mathbf v]_{\mathcal E}
=
\begin{bmatrix}4\\2\end{bmatrix}
\]

Relative to $\mathcal B$,

\[
\mathbf v
=
3
\begin{bmatrix}1\\1\end{bmatrix}
+
1
\begin{bmatrix}1\\-1\end{bmatrix}
\]

so

\[
[\mathbf v]_{\mathcal B}
=
\begin{bmatrix}3\\1\end{bmatrix}
\]

The vector stays the same; its coordinates change.

The first component 3 of $[\mathbf v]_{\mathcal B}$ is the coefficient of $\mathbf b_1=(1,1)^\top$, not the first standard coordinate. The second component 1 multiplies $\mathbf b_2=(1,-1)^\top$. Combining these generators again gives $(4,2)^\top$. Thus, coordinate vector $(3,1)^\top$ does not mean that the original vector moved to standard-coordinate point $(3,1)$. The same vector has been recorded with different generators and coefficients. Even reordering the basis vectors reorders the corresponding coefficients, so coordinates also require an ordered basis.

The figure below draws the same standard coordinate system twice, keeping the vector's endpoint fixed while changing the basis used to decompose it. The (3,1) on the right gives coefficients for the two basis vectors, not a shifted endpoint.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The identical vector four two decomposed as four e one plus two e two and as three b one plus b two](../../figures/assets/M02/M02-07-same-vector-new-coordinates.svg)

<figcaption>The green vector points toward (4,2) in both panels. The decomposition coefficients are (4,2) on the left and (3,1) on the right, but combining them with their respective basis vectors yields the same result.</figcaption>
</figure>

## Example 1. Determine independence of two vectors

For

\[
\mathbf v_1=
\begin{bmatrix}1\\2\end{bmatrix},
\qquad
\mathbf v_2=
\begin{bmatrix}3\\1\end{bmatrix}
\]

writing

\[
c_1\mathbf v_1+c_2\mathbf v_2=\mathbf 0
\]

gives

\[
\begin{aligned}
c_1+3c_2&=0\\
2c_1+c_2&=0
\end{aligned}
\]

The first equation gives $c_1=-3c_2$; substituting into the second gives $-5c_2=0$. Thus, $c_2=0$ and $c_1=0$, so the vectors are linearly independent.

## Example 2. Remove a dependent vector

If

\[
\mathbf v_1=
\begin{bmatrix}1\\0\\1\end{bmatrix},
\qquad
\mathbf v_2=
\begin{bmatrix}0\\1\\1\end{bmatrix},
\qquad
\mathbf v_3=
\begin{bmatrix}1\\1\\2\end{bmatrix}
\]

then

\[
\mathbf v_3=\mathbf v_1+\mathbf v_2
\]

The three vectors are linearly dependent, and removing $\mathbf v_3$ leaves their span unchanged.

## Example 3. A subspace's basis and dimension

Let

\[
V=
\left\{
\begin{bmatrix}x\\y\\z\end{bmatrix}
\in\mathbb R^3
\;\middle|\;
x+y+z=0
\right\}
\]

Since $z=-x-y$,

\[
\begin{bmatrix}x\\y\\z\end{bmatrix}
=
x
\begin{bmatrix}1\\0\\-1\end{bmatrix}
+
y
\begin{bmatrix}0\\1\\-1\end{bmatrix}
\]

The two generating vectors are not multiples, so they are independent. Thus,

\[
\mathcal B=
\left(
\begin{bmatrix}1\\0\\-1\end{bmatrix},
\begin{bmatrix}0\\1\\-1\end{bmatrix}
\right)
\]

is a basis of $V$, and $\dim V=2$.

## Example 4. Representation coordinates and model interpretation

Suppose the $j$th coordinate of an activation $\mathbf h\in\mathbb R^d$ is large. Changing the basis mixes coordinates of the same vector and can also change the $j$th value.

Linking a single coordinate to a concept requires specifying the chosen basis. Subspace-level results that persist across multiple bases or model reparameterizations are a different kind of evidence from results about one coordinate. Neither establishes the model's functional use without interventions.

## Common misconceptions

### Misconception 1. Different vectors are linearly independent

Two distinct vectors are still dependent if one is a multiple of the other.

### Misconception 2. Every list spanning a space is a basis

A generating set with redundant vectors fails independence. A basis requires both spanning and independence.

### Misconception 3. A vector's coordinates are fixed numbers belonging to the object itself

Coordinates depend on the chosen basis. Changing the basis gives the same vector a different coefficient list.

### Misconception 4. Ambient dimension equals the number of independent directions in the data

Even when data are stored in $\mathbb R^d$, the subspace they span can have dimension smaller than $d$.

## Exercises

### 1. Apply the definition

Determine whether

\[
\mathbf v_1=
\begin{bmatrix}1\\2\end{bmatrix},
\qquad
\mathbf v_2=
\begin{bmatrix}2\\4\end{bmatrix}
\]

are linearly independent. If dependent, find nonzero coefficients yielding the zero vector.

<details>
<summary>Show solution</summary>

Since $\mathbf v_2=2\mathbf v_1$,

\[
2\mathbf v_1-\mathbf v_2=\mathbf 0
\]

The coefficients $(2,-1)$ are not both zero, so the vectors are linearly dependent.

</details>

### 2. Independence of three vectors

Determine whether

\[
\mathbf v_1=
\begin{bmatrix}1\\0\\0\end{bmatrix},
\quad
\mathbf v_2=
\begin{bmatrix}0\\1\\0\end{bmatrix},
\quad
\mathbf v_3=
\begin{bmatrix}1\\1\\0\end{bmatrix}
\]

are linearly independent.

<details>
<summary>Show solution</summary>

Since

\[
\mathbf v_3=\mathbf v_1+\mathbf v_2
\]

we have a nonzero coefficient combination

\[
\mathbf v_1+\mathbf v_2-\mathbf v_3=\mathbf 0
\]

Thus, the three vectors are linearly dependent.

</details>

### 3. Determine whether a list is a basis

Determine whether

\[
\mathcal B=
\left(
\begin{bmatrix}1\\1\end{bmatrix},
\begin{bmatrix}1\\-1\end{bmatrix}
\right)
\]

is a basis of $\mathbb R^2$.

<details>
<summary>Show solution</summary>

The vectors are not multiples, so they are linearly independent. For any $\begin{bmatrix}x\\y\end{bmatrix}$, solving

\[
c_1+c_2=x,
\qquad
c_1-c_2=y
\]

gives

\[
c_1=\frac{x+y}{2},
\qquad
c_2=\frac{x-y}{2}
\]

They span every vector, so $\mathcal B$ is a basis of $\mathbb R^2$.

</details>

### 4. Find basis coordinates

For the basis $\mathcal B$ in Exercise 3, find the coordinate vector $[\mathbf v]_{\mathcal B}$ of

\[
\mathbf v=
\begin{bmatrix}5\\1\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

Solving

\[
c_1+c_2=5,
\qquad
c_1-c_2=1
\]

gives $c_1=3$ and $c_2=2$. Thus,

\[
[\mathbf v]_{\mathcal B}
=
\begin{bmatrix}3\\2\end{bmatrix}
\]

</details>

### 5. A basis of a subspace

Find one basis and the dimension of

\[
W=
\left\{
\begin{bmatrix}x\\y\\z\end{bmatrix}
\in\mathbb R^3
\;\middle|\;
x-2y=0
\right\}
\]

<details>
<summary>Show solution</summary>

We have $x=2y$. Setting $y=s$ and $z=t$ gives

\[
\begin{bmatrix}x\\y\\z\end{bmatrix}
=
s
\begin{bmatrix}2\\1\\0\end{bmatrix}
+
t
\begin{bmatrix}0\\0\\1\end{bmatrix}
\]

The two vectors are independent and span all of $W$. Thus, one basis is

\[
\left(
\begin{bmatrix}2\\1\\0\end{bmatrix},
\begin{bmatrix}0\\0\\1\end{bmatrix}
\right)
\]

and $\dim W=2$.

</details>

### 6. Too many vectors

Use the pivot count to explain why 6 vectors in $\mathbb R^4$ cannot be linearly independent.

<details>
<summary>Show solution</summary>

Placing the 6 vectors as columns gives a $4\times6$ matrix. Four rows allow at most 4 pivots. At least two columns lack pivots, leaving free variables in the homogeneous system. Thus, a nonzero coefficient combination yields zero, and the six vectors are linearly dependent.

</details>

### 7. Scope of coordinatewise interpretation

Representing the same activation vector in two bases $\mathcal E$ and $\mathcal B$ changes which coordinates are large. Explain:

1. Has the vector itself changed?
2. Why must a claim that one coordinate represents a particular concept specify the basis?
3. What additional evidence is needed to conclude that the model uses the direction?

<details>
<summary>Show solution</summary>

If only the basis changed, the vector itself remains the same. Coordinates are coefficients of basis vectors, so changing the basis changes their values and positions.

A claim about one coordinate is defined only in the chosen basis. To seek claims that persist across bases, investigate subspaces or invariants under basis changes.

To establish functional use, check whether intervening to remove or change the direction changes model behavior under appropriate controls.

</details>

## Lesson summary

- Linearly independent vectors produce zero only through the trivial coefficient combination.
- Removing redundant vectors from a dependent generating set can leave its span unchanged.
- A basis is a linearly independent vector list spanning the entire space.
- A basis uniquely determines each vector's coordinates.
- Dimension counts basis vectors; distinguish ambient dimension from the dimension of a data subspace.
- Coordinatewise interpretations depend on the basis, and functional use requires intervention evidence.

## Pass criteria

You pass if you can answer these questions without consulting the material:

- Can you define linear independence and dependence using coefficient conditions?
- Can you use row elimination to test column independence?
- Can you distinguish a generating set from a basis?
- Can you find coordinate vectors in a given basis?
- Can you find a subspace's basis and dimension?
- Can you explain why coordinatewise interpretations change with the basis?

## Next lesson

- [M02-08 Kernel, image, and rank](M02-08-kernel-image-rank.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Independence and dependence are defined using homogeneous linear systems.
- [x] Generating sets, bases, and dimension are distinguished.
- [x] Existence and uniqueness of basis coordinates are explained.
- [x] Subspace basis calculations are included.
- [x] Every exercise has a solution.
- [x] Coordinate dependence is distinguished from functional-use claims.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
