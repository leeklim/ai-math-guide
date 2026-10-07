---
id: "M03-02"
title: "Linear maps and matrix representation"
part: 1
stage: "M03"
status: "complete"
prerequisites:
  - "M03-01"
  - "M02-04"
  - "M02-08"
estimated_time: "115–140 minutes"
---

# M03-02. Linear maps and matrix representation

## Why this lesson matters

A matrix is a tool for calculating a linear transformation, but it is not always the same object as the transformation itself. There are also linear maps whose inputs and outputs are not numerical columns, such as differentiation between spaces of functions or polynomials. Choosing bases lets us represent these maps as matrices.

This distinction matters when comparing weights or representations in different models. Even for the same linear map, matrix entries change when the input and output bases change. Before interpreting an individual entry as an intrinsic meaning of the map, check whether the bases are fixed.

## Learning objectives

After this lesson, you will be able to:

- Explain the definition of a linear map through preservation of addition and scalar multiplication.
- Determine whether a map between abstract vector spaces is linear.
- Construct a matrix representation using ordered domain and codomain bases.
- Calculate with the coordinate equation $[T(\mathbf v)]_{\mathcal C}=[T]_{\mathcal C\leftarrow\mathcal B}[\mathbf v]_{\mathcal B}$.
- Connect composition, kernel, and image for a map with those of its matrix representation.

## Prerequisite check

- Prerequisite: [M03-01 Abstract vector spaces](M03-01-abstract-vector-spaces.md)
- Prerequisite: [M02-04 Matrices and matrix multiplication](../M02/M02-04-matrices-matrix-multiplication.md)
- Prerequisite: [M02-08 Kernel, image, and rank](../M02/M02-08-kernel-image-rank.md)
- Check: Can you distinguish an abstract vector from its basis coordinates?
- Check: Can you explain why each column of a matrix is the transformed standard basis vector?

If basis coordinates or matrix multiplication are unclear, review the prerequisite lessons first.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| $T:V\to W$ | `T maps V to W` | A map sending vectors in the domain $V$ to vectors in the codomain $W$ | A linear map in this lesson |
| $\mathcal B=(\mathbf b_1,\ldots,\mathbf b_n)$ | `the basis B consisting of b one through b n` | An ordered basis of $V$ | $\dim V=n$ |
| $\mathcal C=(\mathbf c_1,\ldots,\mathbf c_m)$ | `the basis C consisting of c one through c m` | An ordered basis of $W$ | $\dim W=m$ |
| $[T]_{\mathcal C\leftarrow\mathcal B}$ | `the matrix of T from the basis B to the basis C` | The matrix representation of $T$ in the chosen bases | $\mathbb R^{m\times n}$ |
| $\ker T$ | `the kernel of T` | The set of inputs satisfying $T(\mathbf v)=\mathbf 0_W$ | A subspace of $V$ |
| $\operatorname{im}T$ | `the image of T` | The set of all possible outputs | A subspace of $W$ |

The arrow $\mathcal C\leftarrow\mathcal B$ means that input coordinates use $\mathcal B$ and output coordinates use $\mathcal C$.

## Core concept 1. A linear map preserves linear combinations

A map $T:V\to W$ is linear if, for all $\mathbf u,\mathbf v\in V$ and $\alpha,\beta\in\mathbb R$,

\[
T(\alpha\mathbf u+\beta\mathbf v)
=
\alpha T(\mathbf u)+\beta T(\mathbf v)
\]

This equation expresses two conditions at once:

\[
T(\mathbf u+\mathbf v)=T(\mathbf u)+T(\mathbf v)
\]

\[
T(\alpha\mathbf v)=\alpha T(\mathbf v)
\]

The first says that adding the inputs before applying $T$ gives the same result as applying $T$ to each input and then adding the outputs. The second says that multiplying the input by a scalar before applying the map gives the same result as multiplying the output. Setting $\alpha=\beta=1$ in the linear-combination equation gives the first condition; setting $\beta=0$ gives the second. Conversely, if both conditions hold, then $T(\alpha\mathbf u+\beta\mathbf v)=T(\alpha\mathbf u)+T(\beta\mathbf v)=\alpha T(\mathbf u)+\beta T(\mathbf v)$, giving the linear-combination equation. The two definitions express the same requirement.

A linear map must send the zero vector to the zero vector. Indeed,

\[
T(\mathbf 0_V)
=
T(0\mathbf v)
=
0T(\mathbf v)
=
\mathbf 0_W
\]

Thus, if $T(\mathbf 0_V)\ne\mathbf 0_W$, we can immediately conclude that the map is not linear.

However, sending zero to zero alone does not guarantee linearity. The function $F(x)=x^2$ satisfies $F(0)=0$, but $F(2\cdot1)=4\ne2F(1)$, so it does not preserve scalar multiplication. The zero-vector condition is necessary, not sufficient: its failure rules out linearity.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Graph of x squared comparing the actual output F two equals four with the scaling requirement two times F one equals two](../../figures/assets/M03/M03-02-zero-is-not-linearity.svg)
  <figcaption>A curve can pass through the origin without being linear. Doubling input 1 gives an actual output of 4, whereas doubling output 1 gives 2, so the two paths do not agree.</figcaption>
</figure>

The orange square in the graph is not an actual function value. It marks the value that linearity would require.

## Core concept 2. A linear map is determined by the outputs of basis vectors

Let $\mathcal B=(\mathbf b_1,\ldots,\mathbf b_n)$ be a basis of $V$. Every $\mathbf v\in V$ has a unique representation

\[
\mathbf v
=
v_1\mathbf b_1+\cdots+v_n\mathbf b_n
\]

Linearity gives

\[
T(\mathbf v)
=
v_1T(\mathbf b_1)+\cdots+v_nT(\mathbf b_n)
\]

Thus, knowing the outputs of the $n$ basis vectors is enough to know $T$ on every input.

This gives the matrix representation. Write each $T(\mathbf b_j)$ in coordinates of the codomain basis $\mathcal C$ and arrange those columns as

\[
[T]_{\mathcal C\leftarrow\mathcal B}
=
\begin{bmatrix}
[T(\mathbf b_1)]_{\mathcal C}
&
\cdots
&
[T(\mathbf b_n)]_{\mathcal C}
\end{bmatrix}
\]

Column $j$ records where the domain's $j$th basis vector goes, in codomain coordinates.

The independence of input basis vectors is different from a claim that their outputs are independent. Different basis vectors may have the same output or may be sent to zero. The input representation is unique, so overlapping outputs create no ambiguity in determining $T(\mathbf v)$. They may, however, prevent unique recovery of the input from the output.

## Core concept 3. A matrix calculates between coordinates

For $\mathbf v\in V$,

\[
[T(\mathbf v)]_{\mathcal C}
=
[T]_{\mathcal C\leftarrow\mathcal B}
[\mathbf v]_{\mathcal B}
\]

The shapes are

\[
\underbrace{[T(\mathbf v)]_{\mathcal C}}_{m\times1}
=
\underbrace{[T]_{\mathcal C\leftarrow\mathcal B}}_{m\times n}
\underbrace{[\mathbf v]_{\mathcal B}}_{n\times1}
\]

The left side is not the abstract output $T(\mathbf v)$, but its $\mathcal C$ coordinates. The matrix on the right is likewise not $T$ itself, but a numerical representation obtained by choosing two bases.

This coordinate equation follows from the preceding section's linear combination. If $\mathbf v=\sum_j v_j\mathbf b_j$, then $T(\mathbf v)=\sum_j v_jT(\mathbf b_j)$. As established in M03-01, recording coordinates in the same basis preserves linear combinations. Hence,

\[
[T(\mathbf v)]_{\mathcal C}
=\sum_{j=1}^n v_j[T(\mathbf b_j)]_{\mathcal C}
\]

The right side multiplies matrix column $j$ by input coordinate $v_j$ and adds the results: it is matrix–column-vector multiplication. Each column contains $m$ output-basis coefficients, and there are $n$ input basis vectors, so the matrix has shape $m\times n$. Constructing the matrix means storing output coefficient columns, not placing abstract outputs themselves in an array.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Commuting square from a polynomial to its derivative and from three input coefficients to two output coefficients through the derivative matrix](../../figures/assets/M03/M03-02-map-coordinate-square.svg)
  <figcaption>The polynomial in Example 1 is differentiated directly along the upper path; along the lower path, its coefficient column is multiplied by a matrix. The results are the same derivative and its coordinates, but the polynomial itself must be distinguished from the numerical column.</figcaption>
</figure>

Three input coefficients become two output coefficients, so the matrix is $2\times3$. The next example constructs the lower-path matrix from the derivatives of the basis elements.

## Core concept 4. Composition is represented by matrix multiplication

Suppose

\[
T:V\to W,
\qquad
S:W\to U
\]

are linear, with ordered bases $\mathcal B,\mathcal C,\mathcal D$ for the respective spaces. Then

\[
[S\circ T]_{\mathcal D\leftarrow\mathcal B}
=
[S]_{\mathcal D\leftarrow\mathcal C}
[T]_{\mathcal C\leftarrow\mathcal B}
\]

The right matrix first takes input coordinates in $\mathcal B$ and calculates the $\mathcal C$ coordinates of $T(\mathbf v)$. The left matrix takes that result and calculates the $\mathcal D$ coordinates of $S(T(\mathbf v))$. This applies two maps in sequence rather than merely changing coordinates of the same vector.

Indeed,

\[
[S(T(\mathbf v))]_{\mathcal D}
=[S]_{\mathcal D\leftarrow\mathcal C}[T(\mathbf v)]_{\mathcal C}
=[S]_{\mathcal D\leftarrow\mathcal C}
[T]_{\mathcal C\leftarrow\mathcal B}[\mathbf v]_{\mathcal B}
\]

Thus, the matrix of $T$, the map applied first, appears on the right in the matrix for the composition.

Matching matrix dimensions and matching intermediate bases are different requirements. If one matrix outputs numbers in one basis of $W$ and the next interprets them as coordinates in another basis, matching dimensions still permit multiplication, but the product does not represent the composition above. Match the intermediate output and subsequent input bases in the same order, or insert a coordinate transformation between them.

<figure class="lesson-figure" markdown="1">
  ![Vertical composition path showing input basis B through T into middle basis C and then through S into output basis D with rightmost matrix acting first](../../figures/assets/M03/M03-02-composition-order.svg)
  <figcaption>Along the calculation path, the intermediate coordinates after T become the input to S. When the two matrices are written side by side, the right matrix, closest to the input column, acts first.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Two interpretations of the same middle coordinate array in bases one t and t one producing different polynomials and derivatives](../../figures/assets/M03/M03-02-middle-basis-mismatch.svg)
  <figcaption>The same numerical column (−3,8)ᵀ represents −3+8t in the basis (1,t), but −3t+8 in the basis (t,1). Subsequent differentiation gives 8 and −3, respectively. This is why intermediate bases must be checked even when dimensions match.</figcaption>
</figure>

To pass the same polynomial along the second path, change the numbers to $(8,-3)^\top$ according to the basis order rather than passing them unchanged.

## Core concept 5. Kernel and image describe the structure of a map

The kernel and image of a linear map $T:V\to W$ are

\[
\ker T
=
\{\mathbf v\in V:T(\mathbf v)=\mathbf 0_W\}
\]

\[
\operatorname{im}T
=
\{T(\mathbf v):\mathbf v\in V\}
\]

After choosing bases, we can calculate them using coordinates in the matrix's null space and column space.

Write the matrix representation as $\mathbf A=[T]_{\mathcal C\leftarrow\mathcal B}$. All basis coefficients are zero if and only if the vector is zero. The coordinate equation therefore gives

\[
\mathbf v\in\ker T
\quad\Longleftrightarrow\quad
\mathbf A[\mathbf v]_{\mathcal B}=\mathbf 0
\]

A column in the matrix's null space is not the original kernel vector itself, but its $\mathcal B$ coordinates. Using those coefficients to combine the basis vectors gives an element of $\ker T$.

Likewise, as input coordinates $\mathbf x\in\mathbb R^n$ range over all columns, $\mathbf A\mathbf x$ ranges over the entire column space. Columns in the column space are therefore coordinates of elements of $\operatorname{im}T$ in the basis $\mathcal C$. In each space, recording coordinates and reconstructing vectors gives a one-to-one correspondence that preserves linear combinations. Spanning and linear independence are therefore preserved, so kernel and image dimensions can be calculated as matrix nullity and rank, respectively.

Changing bases changes the coordinates of kernel vectors and image vectors. But which abstract vectors belong to the kernel, and the dimension of the image, are properties of the map itself.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Three input polynomials differing only by constants plotted as vertical shifts](../../figures/assets/M03/M03-02-kernel-lost-constants.svg)
  <figcaption>The polynomial p(t) in Example 1 and the polynomials formed by adding or subtracting the constant 2 are different inputs. Their vertical shifts show differences in the constant direction, which differentiation removes.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![One derivative curve shared by all three vertically shifted input polynomials](../../figures/assets/M03/M03-02-kernel-shared-output.svg)
  <figcaption>The derivatives of all three inputs overlap at −3+8t. If the difference between inputs belongs to the kernel, they can have the same output, so this output alone cannot recover the original constant term.</figcaption>
</figure>

The two figures separate the different inputs from their shared output. What disappears is the difference in the constant direction, not all input information.

## Example 1. Matrix representation of polynomial differentiation

### Problem

Consider the differentiation map

\[
D:\mathcal P_2\to\mathcal P_1,
\qquad
D(p)=p'
\]

Choose the domain basis

\[
\mathcal B=(1,t,t^2)
\]

and codomain basis

\[
\mathcal C=(1,t)
\]

Calculate $[D]_{\mathcal C\leftarrow\mathcal B}$ and use the matrix to calculate the derivative of $p(t)=2-3t+4t^2$.

### Solution

Differentiating the domain basis vectors gives

\[
D(1)=0,
\qquad
D(t)=1,
\qquad
D(t^2)=2t
\]

Their $\mathcal C$ coordinates are

\[
[D(1)]_{\mathcal C}
=
\begin{bmatrix}0\\0\end{bmatrix},
\quad
[D(t)]_{\mathcal C}
=
\begin{bmatrix}1\\0\end{bmatrix},
\quad
[D(t^2)]_{\mathcal C}
=
\begin{bmatrix}0\\2\end{bmatrix}
\]

Thus,

\[
[D]_{\mathcal C\leftarrow\mathcal B}
=
\begin{bmatrix}
0&1&0\\
0&0&2
\end{bmatrix}
\]

Since

\[
[p]_{\mathcal B}
=
\begin{bmatrix}
2\\
-3\\
4
\end{bmatrix}
\]

we obtain

\[
[D(p)]_{\mathcal C}
=
\begin{bmatrix}
0&1&0\\
0&0&2
\end{bmatrix}
\begin{bmatrix}
2\\
-3\\
4
\end{bmatrix}
=
\begin{bmatrix}
-3\\
8
\end{bmatrix}
\]

Therefore, $D(p)(t)=-3+8t$.

### What the result means

Differentiation is an abstract operation sending polynomials to polynomials. Once we choose bases, we can calculate it with a $2\times3$ matrix.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Derivative images of basis polynomials one t and t squared aligned with their coordinate columns in a two by three matrix](../../figures/assets/M03/M03-02-basis-images-columns.svg)
  <figcaption>Differentiating each of the three input basis elements gives 0,1,2t, recorded as coefficients in the output basis (1,t). Arranging these coefficient columns in input-basis order produces the differentiation matrix. Its zero first column means the constant basis element goes to the zero polynomial.</figcaption>
</figure>

Within each column, the upper number is the coefficient of the constant basis element; the lower is the coefficient of the $t$ basis element. Read the column order and row meanings together.

## Example 2. Determine whether a map is nonlinear

### Problem

For

\[
F:\mathbb R^2\to\mathbb R^2,
\qquad
F(\mathbf x)=\mathbf A\mathbf x+\mathbf b
\]

determine whether $F$ is linear when $\mathbf b\ne\mathbf 0$.

### Solution

\[
F(\mathbf 0)
=
\mathbf A\mathbf 0+\mathbf b
=
\mathbf b
\ne
\mathbf 0
\]

A linear map must send zero to zero, so $F$ is not linear.

### What the result means

The neural network layer $\mathbf W\mathbf x+\mathbf b$ is affine when its bias is nonzero. Even if an implementation calls it a linear layer, it may mathematically be affine.

## Example 3. Read a model weight matrix as a representation

Let the activation space be $V=\mathbb R^d$ and the next layer's pre-activation space be $W=\mathbb R^m$. Define the map without bias as

\[
T(\mathbf h)=\mathbf W\mathbf h
\]

Using standard bases gives $[T]_{\mathcal E_W\leftarrow\mathcal E_V}=\mathbf W$.

Column $j$ of $\mathbf W$ contains the output coordinates of input standard basis vector $\mathbf e_j$.

\[
T(\mathbf e_j)=\mathbf W\mathbf e_j
\]

Thus, one column records the response to one chosen input coordinate direction. Its meaning depends on both input and output bases. Distinguish the linear map $T$ from the array $\mathbf W$ stored in particular standard bases.

## Common misconceptions

### Misconception 1. Every linear map is a matrix from the outset

A linear map is a function between vector spaces. In finite-dimensional spaces, choosing input and output bases lets us represent it as a matrix.

### Misconception 2. Column $j$ of a matrix is always $T(\mathbf e_j)$

This notation is valid when the domain basis is the standard basis and the codomain coordinates also use the standard basis. In general, column $j$ is $[T(\mathbf b_j)]_{\mathcal C}$.

### Misconception 3. $T(\mathbf x)=\mathbf A\mathbf x+\mathbf b$ is always linear

If $\mathbf b\ne\mathbf 0$, it does not send zero to zero. It is an affine map, not a linear map.

### Misconception 4. The identity map has the identity matrix for every pair of bases

The matrix of the identity map is $\mathbf I$ when the domain and codomain use the same ordered basis. With different bases, its matrix is a coordinate transformation matrix.

## Exercises

### 1. Test linearity

Determine whether

\[
T:\mathcal P_2\to\mathbb R,
\qquad
T(p)=p(1)
\]

is linear.

<details>
<summary>Show solution</summary>

For $p,q\in\mathcal P_2$ and $\alpha,\beta\in\mathbb R$,

\[
T(\alpha p+\beta q)
=(\alpha p+\beta q)(1)
=\alpha p(1)+\beta q(1)
=\alpha T(p)+\beta T(q)
\]

Thus, it is linear. It is called the evaluation map at point $1$.

</details>

### 2. A nonlinear function

Use one counterexample to show that

\[
F:\mathbb R\to\mathbb R,
\qquad
F(x)=x^2
\]

is not linear.

<details>
<summary>Show solution</summary>

Although $F(2\cdot1)=F(2)=4$, we have $2F(1)=2$. The function does not preserve scalar multiplication, so it is not linear.

</details>

### 3. Construct a matrix representation

The map $T:\mathbb R^2\to\mathbb R^2$ is given by

\[
T(x,y)^\top=(x+y,x-y)^\top
\]

Calculate its matrix using standard bases for the domain and codomain.

<details>
<summary>Show solution</summary>

Since

\[
T(\mathbf e_1)
=
\begin{bmatrix}1\\1\end{bmatrix},
\qquad
T(\mathbf e_2)
=
\begin{bmatrix}1\\-1\end{bmatrix}
\]

arranging these outputs as columns gives

\[
[T]_{\mathcal E\leftarrow\mathcal E}
=
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
\]

</details>

### 4. Calculate with the coordinate equation

Use the preceding matrix and $\mathbf v=(3,2)^\top$ to calculate $T(\mathbf v)$.

<details>
<summary>Show solution</summary>

\[
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
\begin{bmatrix}
3\\
2
\end{bmatrix}
=
\begin{bmatrix}
5\\
1
\end{bmatrix}
\]

Direct substitution also gives $(3+2,3-2)^\top=(5,1)^\top$.

</details>

### 5. Kernel and image of differentiation

For $D:\mathcal P_2\to\mathcal P_1$ in Example 1, calculate $\ker D$ and $\operatorname{im}D$.

<details>
<summary>Show solution</summary>

The polynomials whose derivatives are zero polynomials are the constants. Hence,

\[
\ker D=\operatorname{span}\{1\}
\]

Every $a+bt\in\mathcal P_1$ can be obtained as

\[
D(at+\tfrac{b}{2}t^2)=a+bt
\]

so

\[
\operatorname{im}D=\mathcal P_1
\]

</details>

### 6. Matrix of a composition

Suppose

\[
\mathbf A=
\begin{bmatrix}
1&2\\
0&1
\end{bmatrix},
\qquad
\mathbf B=
\begin{bmatrix}
2&0\\
1&3
\end{bmatrix}
\]

represent $T$ and $S$, respectively, in standard bases. Calculate the matrix of $S\circ T$.

<details>
<summary>Show solution</summary>

Since $T$ is applied first,

\[
[S\circ T]=\mathbf B\mathbf A
=
\begin{bmatrix}
2&0\\
1&3
\end{bmatrix}
\begin{bmatrix}
1&2\\
0&1
\end{bmatrix}
=
\begin{bmatrix}
2&4\\
1&5
\end{bmatrix}
\]

Reversing the matrices generally represents a different composition.

</details>

### 7. Critique a model claim

Critique the claim: “A weight matrix entry is large, so it is an important feature connection independent of the basis.”

<details>
<summary>Show solution</summary>

Matrix entries are coordinate values obtained after choosing input and output bases. Changing bases gives the same linear map different entries. We can measure sensitivity or intervention effects in fixed implementation coordinates, but entry magnitude alone does not establish basis-independent feature importance.

</details>

## Lesson summary

- A linear map is a function between vector spaces that preserves all linear combinations.
- A finite-dimensional linear map is determined by the outputs of domain basis vectors.
- Each column of its matrix representation contains codomain coordinates of an input basis vector's output.
- A matrix takes input coordinates, not abstract inputs, and produces output coordinates.
- Composition is represented by matrix multiplication when the bases match.
- Kernel and image describe the map's structure and can be calculated in coordinates after choosing bases.

## Pass criteria

You pass if you can answer the following without consulting the lesson.

- Can you test linearity using the equation for preservation of linear combinations?
- Can you construct a matrix representation from basis-vector outputs?
- Can you read the matrix representation's subscript and shape?
- Can you calculate polynomial differentiation with a matrix?
- Can you determine the order of matrix multiplication for a composition?
- Can you distinguish a map from its matrix in particular bases?

## Next lesson

- [M03-03 Change of basis and coordinate dependence](M03-03-change-of-basis-coordinate-dependence.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Linear maps are distinguished from matrix representations.
- [x] Domain and codomain bases and matrix subscripts are used consistently.
- [x] The polynomial differentiation example is calculated explicitly.
- [x] Composition, kernel, and image are connected.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
