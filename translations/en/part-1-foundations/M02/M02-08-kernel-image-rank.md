---
id: "M02-08"
title: "Kernel, image, and rank"
part: 1
stage: "M02"
status: "complete"
prerequisites:
  - "M02-05"
  - "M02-06"
  - "M02-07"
estimated_time: "115~140 minutes"
---

# M02-08. Kernel, image, and rank

## Why this lesson matters

A linear transformation can send some input directions to zero and produce only some directions in the output space. The kernel collects input directions that disappear, while the image collects all achievable outputs. Rank counts the independent directions that remain in the image.

Connecting these concepts determines whether a linear system has solutions and whether an input can be uniquely recovered from its output. For neural network weight matrices, we can similarly ask which representation directions are removed and which subspace constrains the outputs.

## Learning objectives

After completing this lesson, you will be able to:

- Define a linear transformation's kernel and image as sets.
- Find a matrix's kernel by solving a homogeneous linear system.
- Find its image as the span of its column vectors.
- Determine rank from the pivot count and apply the rank-nullity theorem.
- Determine existence and uniqueness of solutions to $\mathbf A\mathbf x=\mathbf b$ using the image and kernel.
- Distinguish structural conclusions directly supported by a weight matrix's rank from claims about model behavior.

## Prerequisite check

- Prerequisite lesson: [M02-05 Viewing matrices as linear transformations](M02-05-matrix-as-linear-transformation.md)
- Prerequisite lesson: [M02-06 Linear systems and inverses](M02-06-linear-systems-inverse.md)
- Prerequisite lesson: [M02-07 Linear independence, bases, and dimension](M02-07-linear-independence-basis-dimension.md)
- Check question: Can you find a basis of a homogeneous system's solution set from its free variables?
- Check question: Can you distinguish the span of a matrix's columns from a basis?

If homogeneous systems, span, or dimension are unclear, first review the prerequisite lessons.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| $\ker(T)$ | `the kernel of T` | Set of inputs that $T$ sends to zero | Subspace of the domain |
| $\operatorname{im}(T)$ | `the image of T` | Set of outputs actually produced by $T$ | Subspace of the codomain |
| $\operatorname{rank}(\mathbf A)$ | `the rank of A` | Dimension of the image of $\mathbf A$ | Equals the pivot count. |
| $\operatorname{nullity}(\mathbf A)$ | `the nullity of A` | Dimension of the kernel of $\mathbf A$ | Equals the number of free variables. |
| Column space | `column space` | Space spanned by a matrix's column vectors | Equals $\operatorname{im}(\mathbf A)$. |

## Core concept 1. The kernel collects inputs sent to zero

For a linear transformation $T:\mathbb R^n\to\mathbb R^m$,

\[
\ker(T)
=
\left\{
\mathbf x\in\mathbb R^n
\;\middle|\;
T(\mathbf x)=\mathbf 0
\right\}
\]

If $T(\mathbf x)=\mathbf A\mathbf x$, write

\[
\ker(\mathbf A)
=
\left\{
\mathbf x\in\mathbb R^n
\;\middle|\;
\mathbf A\mathbf x=\mathbf 0
\right\}
\]

Solve the homogeneous system to find vectors in the kernel.

The condition inside the set checks whether the output is zero. The objects satisfying it are input vectors, so the kernel lies in $\mathbb R^n$. It does not require particular input components to be 0. Contributions from several components can cancel, making the entire output zero.

Linearity gives $T(\mathbf 0)=\mathbf 0$, so the zero vector belongs to the kernel. For two kernel vectors $\mathbf u,\mathbf v$ and a real number $c$,

\[
T(\mathbf u+\mathbf v)=T(\mathbf u)+T(\mathbf v)=\mathbf 0,
\qquad
T(c\mathbf u)=cT(\mathbf u)=\mathbf 0
\]

Thus, the kernel is a subspace of the input space, closed under addition and scalar multiplication.

The figure below places a kernel line in the input space, where two components' contributions cancel. Points on the line have different components but satisfy the same output condition.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A kernel line in the input plane whose every point maps to zero in a separate output plane](../../figures/assets/M02/M02-08-kernel-input-line.svg)

<figcaption>For A(x,y)=(x+2y,0), all inputs with x+2y=0 produce zero output. The kernel is the entire input line on the left, not the output origin on the right. Individual input components need not be 0.</figcaption>
</figure>

## Core concept 2. The kernel determines whether inputs can be distinguished

Suppose two inputs $\mathbf x_1,\mathbf x_2$ produce the same output. If

\[
\mathbf A\mathbf x_1=\mathbf A\mathbf x_2
\]

then

\[
\mathbf A(\mathbf x_1-\mathbf x_2)=\mathbf 0
\]

Their difference $\mathbf x_1-\mathbf x_2$ belongs to the kernel.

If

\[
\ker(\mathbf A)=\{\mathbf 0\}
\]

two distinct inputs cannot produce the same output, so the transformation is one-to-one. Conversely, if a vector $\mathbf z\ne\mathbf 0$ belongs to the kernel,

\[
\mathbf A(\mathbf x+\mathbf z)
=\mathbf A\mathbf x+\mathbf A\mathbf z
=\mathbf A\mathbf x
\]

The inputs $\mathbf x$ and $\mathbf x+\mathbf z$ differ but their outputs agree. Every multiple of a kernel vector also belongs to the kernel, so moving any amount in this direction leaves the output unchanged.

The figure below compares distinct input lines parallel to the kernel. Movement within one line leaves the output fixed; moving to a different line changes the output.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Parallel translated kernel lines in the input plane mapped to distinct fixed points in the output plane](../../figures/assets/M02/M02-08-parallel-input-fibres.svg)

<figcaption>Each input line consists of one particular input x₀ plus every kernel vector. Differences between inputs on the same line belong to the kernel and cannot be distinguished in the output. Matching colors and line styles indicate the output correspondences.</figcaption>
</figure>

## Core concept 3. The image collects achievable outputs

The image of a linear transformation $T$ is

\[
\operatorname{im}(T)
=
\left\{
T(\mathbf x)
\;\middle|\;
\mathbf x\in\mathbb R^n
\right\}
\]

Writing the columns of $\mathbf A$ as $\mathbf a_1,\ldots,\mathbf a_n$ gives

\[
\mathbf A\mathbf x
=
x_1\mathbf a_1+\cdots+x_n\mathbf a_n
\]

Therefore,

\[
\operatorname{im}(\mathbf A)
=
\operatorname{span}\{\mathbf a_1,\ldots,\mathbf a_n\}
\]

In one direction, every output is a linear combination of the columns. In the other, choosing the coefficients of any column combination as components of input $\mathbf x$ makes that combination an actual output. Equality of the two sets includes both directions.

The image is the matrix's column space and a subspace of codomain $\mathbb R^m$. Unlike the kernel, it collects outputs reachable by varying inputs, not inputs themselves. A vector in the codomain need not belong to the image: an input must exist that produces it.

The figure below draws Example 3's image within the output space. Belonging to the codomain differs from being achievable as an actual output.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A line of reachable outputs in R three and an unreachable target displaced in its third component](../../figures/assets/M02/M02-08-image-and-unreachable-target.svg)

<figcaption>Both columns of B are multiples of (1,2,0), so its image is the green line. Target (1,2,1) lies in the same codomain R³, but its third component 1 places it off that line. No input produces this target.</figcaption>
</figure>

## Core concept 4. Rank counts independent output directions

A matrix's rank is the dimension of its image.

\[
\operatorname{rank}(\mathbf A)
=
\dim\operatorname{im}(\mathbf A)
\]

To find an image basis, choose columns that are independent and span the remaining columns. In row echelon form after elimination, pivot columns have distinct leading positions and are independent. The remaining columns are linear combinations of the pivot columns. Matching coefficients from the lowest pivot row upward matches every nonzero row's component; zero rows leave no additional components to match. Thus, rank equals the number of pivot columns.

Elementary row operations are reversible, so they preserve linear-combination relationships among columns. The coefficient combinations that sum the original columns to zero remain the same after elimination. Choosing the original matrix's columns at the pivot column indices therefore gives a basis of the original column space.

Do not use the reduced columns themselves as a basis of the original image. Row operations change column components, which are coordinates of output vectors. The independent direction count and relationships between columns stay the same, but the actual image need not remain the same set.

For $\mathbf A\in\mathbb R^{m\times n}$,

\[
\operatorname{rank}(\mathbf A)
\le
\min(m,n)
\]

Outputs lie in $\mathbb R^m$, so there can be at most $m$ independent output directions. The space is also spanned by $n$ columns, so there can be at most $n$ independent column directions.

The figure below shows that row elimination preserves which columns are multiples without necessarily preserving the image's location. After finding pivot column indices, return to the corresponding original columns.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Original and row-reduced matrices with rank one but different output lines and matching pivot column index](../../figures/assets/M02/M02-08-original-pivot-column.svg)

<figcaption>In both matrices, the second column is twice the first, and the first column is the pivot column. After elimination the image becomes horizontal, so choose original first column (1,2), not reduced column (1,0), for a basis of the original image.</figcaption>
</figure>

## Core concept 5. Rank-nullity counts directions retained and lost

Nullity is the dimension of the kernel.

\[
\operatorname{nullity}(\mathbf A)
=
\dim\ker(\mathbf A)
\]

For $\mathbf A\in\mathbb R^{m\times n}$,

\[
\operatorname{rank}(\mathbf A)
+
\operatorname{nullity}(\mathbf A)
=
n
\]

The input dimension $n$ is the sum of the independent directions retained in the image and those lost in the kernel.

We can check this dimension relationship using free variables in a homogeneous system. Choosing free variable values determines the pivot variables through back-substitution. Construct one solution for each free variable by setting it to 1 and all other free variables to 0. Every solution is a linear combination of these solutions. Their free-variable components also establish independence. Thus, the free variable count equals the number of kernel basis vectors, or nullity.

Rank counts pivot variables. All $n$ unknowns divide into pivot and free variables, so the counts sum to $n$. This equation connects input dimension with output image dimension. It does not say that the kernel and image are two parts of one space: the kernel lies in $\mathbb R^n$, while the image lies in $\mathbb R^m$.

The figure below selects three independent input directions from Example 1 and compares their outputs. Count the directions lost and retained while distinguishing the spaces containing the kernel and image.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three independent directions in input R three mapping to two output basis directions and zero in R two](../../figures/assets/M02/M02-08-rank-nullity-directions.svg)

<figcaption>Inputs e₁ and e₃ map to two independent output directions; input (−2,1,0) maps to zero. Rank 2 plus nullity 1 equals input dimension 3. Even though every output is reachable, this nonzero kernel direction prevents unique input recovery.</figcaption>
</figure>

## Core concept 6. The image determines existence; the kernel determines uniqueness

The system

\[
\mathbf A\mathbf x=\mathbf b
\]

has a solution if and only if

\[
\mathbf b\in\operatorname{im}(\mathbf A)
\]

because the image contains exactly the achievable outputs.

Suppose one solution $\mathbf x_0$ exists. Every solution has the form

\[
\mathbf x
=
\mathbf x_0+\mathbf z,
\qquad
\mathbf z\in\ker(\mathbf A)
\]

Indeed,

\[
\mathbf A(\mathbf x_0+\mathbf z)
=
\mathbf b+\mathbf 0
=
\mathbf b
\]

Conversely, any solution $\mathbf x$ satisfies

\[
\mathbf A(\mathbf x-\mathbf x_0)
=\mathbf b-\mathbf b
=\mathbf 0
\]

so $\mathbf x-\mathbf x_0$ belongs to the kernel. Both statements hold: adding a kernel vector produces a solution, and every solution can be written this way.

If the kernel is $\{\mathbf 0\}$, any existing solution is unique. If it contains a nonzero vector, adding a kernel vector to one solution gives another.

## Core concept 7. Kernel, image, and rank determine invertibility

For a square matrix $\mathbf A\in\mathbb R^{n\times n}$, these conditions are equivalent:

- $\mathbf A$ is invertible.
- $\ker(\mathbf A)=\{\mathbf 0\}$.
- $\operatorname{im}(\mathbf A)=\mathbb R^n$.
- $\operatorname{rank}(\mathbf A)=n$.
- For every $\mathbf b\in\mathbb R^n$, $\mathbf A\mathbf x=\mathbf b$ has exactly one solution.

Rank-nullity gives nullity 0 when rank is $n$. The kernel contains only zero, and all columns are independent. For a square matrix, the output dimension is also $n$, so these $n$ independent columns form a basis of the entire output space. Every target output therefore has a unique solution. The inverse in M02-06 sends each output back to this unique input.

For rectangular matrices, input dimension $n$ and output dimension $m$ can differ, separating the two conditions. If $\operatorname{rank}(\mathbf A)=n$, nullity is 0 and the transformation is one-to-one. If $\operatorname{rank}(\mathbf A)=m$, the image is all of $\mathbb R^m$. For example, when $m<n$, rank is at most $m$, so nullity is at least $n-m$. Even if every output is achievable, unique input recovery may be impossible.

## Example 1. Find kernel, image, and rank together

Let

\[
\mathbf A=
\begin{bmatrix}
1&2&0\\
0&0&1
\end{bmatrix}
\]

To find the kernel, solve

\[
\begin{bmatrix}
1&2&0\\
0&0&1
\end{bmatrix}
\begin{bmatrix}x\\y\\z\end{bmatrix}
=
\begin{bmatrix}0\\0\end{bmatrix}
\]

The equations are

\[
x+2y=0,
\qquad
z=0
\]

Setting $y=t$ gives

\[
\begin{bmatrix}x\\y\\z\end{bmatrix}
=
t
\begin{bmatrix}-2\\1\\0\end{bmatrix}
\]

so

\[
\ker(\mathbf A)
=
\operatorname{span}
\left\{
\begin{bmatrix}-2\\1\\0\end{bmatrix}
\right\}
\]

and nullity is 1.

The first and third columns are independent, and the second is twice the first. Thus,

\[
\operatorname{im}(\mathbf A)
=
\operatorname{span}
\left\{
\begin{bmatrix}1\\0\end{bmatrix},
\begin{bmatrix}0\\1\end{bmatrix}
\right\}
=
\mathbb R^2
\]

Rank is 2, and the rank-nullity equation is $2+1=3$.

## Example 2. Express a solution set using a particular solution and the kernel

For Example 1's matrix, solving

\[
\mathbf A\mathbf x
=
\begin{bmatrix}5\\3\end{bmatrix}
\]

gives

\[
x+2y=5,
\qquad
z=3
\]

One solution is

\[
\mathbf x_0=
\begin{bmatrix}5\\0\\3\end{bmatrix}
\]

All solutions are

\[
\mathbf x
=
\begin{bmatrix}5\\0\\3\end{bmatrix}
+
t
\begin{bmatrix}-2\\1\\0\end{bmatrix},
\qquad
t\in\mathbb R
\]

Changing the input along the kernel direction preserves the output.

## Example 3. Targets outside the image are unreachable

Both columns of

\[
\mathbf B=
\begin{bmatrix}
1&2\\
2&4\\
0&0
\end{bmatrix}
\]

are multiples of

\[
\begin{bmatrix}1\\2\\0\end{bmatrix}
\]

Thus,

\[
\operatorname{im}(\mathbf B)
=
\operatorname{span}
\left\{
\begin{bmatrix}1\\2\\0\end{bmatrix}
\right\}
\]

and rank is 1. The target

\[
\mathbf b=
\begin{bmatrix}1\\2\\1\end{bmatrix}
\]

has third component 1, so it does not belong to this image. Therefore, $\mathbf B\mathbf x=\mathbf b$ has no solution.

## Example 4. Kernel and image of neural network weights

If

\[
\mathbf W\in\mathbb R^{64\times128}
\]

then

\[
\operatorname{rank}(\mathbf W)\le64
\]

Rank-nullity gives

\[
\operatorname{nullity}(\mathbf W)
=
128-\operatorname{rank}(\mathbf W)
\ge64
\]

At least 64 independent input directions map to zero in the linear part.

This conclusion describes the structure of linear transformation $\mathbf W$. Whether actual data vary along kernel directions, how behavior changes after bias and nonlinear functions, and whether the model functionally uses particular directions require separate analyses.

## Common misconceptions

### Misconception 1. The kernel collects small matrix entries

The kernel is the set of input vectors satisfying $\mathbf A\mathbf x=\mathbf 0$, not a collection based on entry size.

### Misconception 2. The image equals the codomain

The image includes only outputs actually reached by the transformation. If rank is smaller than output dimension, the image is a proper subspace of the codomain.

### Misconception 3. Rank counts nonzero columns

Nonzero columns can be dependent. Rank counts independent column directions and is calculated from pivots.

### Misconception 4. Low rank necessarily means worse model performance

Low rank limits the output directions of a linear transformation. Its performance effects depend on the data distribution, subsequent computations, and task, so behavioral evaluation is necessary.

## Exercises

### 1. Find a kernel

Find a kernel basis and the nullity of

\[
\mathbf A=
\begin{bmatrix}
1&1&0\\
0&1&1
\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

The equations are

\[
x+y=0,
\qquad
y+z=0
\]

Setting $y=t$ gives $x=-t$ and $z=-t$, so

\[
\begin{bmatrix}x\\y\\z\end{bmatrix}
=
t
\begin{bmatrix}-1\\1\\-1\end{bmatrix}
\]

Thus,

\[
\ker(\mathbf A)
=
\operatorname{span}
\left\{
\begin{bmatrix}-1\\1\\-1\end{bmatrix}
\right\}
\]

and nullity is 1.

</details>

### 2. Find image and rank

Find an image basis and the rank of the matrix in Exercise 1.

<details>
<summary>Show solution</summary>

The columns are

\[
\mathbf a_1=
\begin{bmatrix}1\\0\end{bmatrix},
\quad
\mathbf a_2=
\begin{bmatrix}1\\1\end{bmatrix},
\quad
\mathbf a_3=
\begin{bmatrix}0\\1\end{bmatrix}
\]

The vectors $\mathbf a_1$ and $\mathbf a_2$ are independent, and $\mathbf a_3=\mathbf a_2-\mathbf a_1$. Thus, one image basis is $(\mathbf a_1,\mathbf a_2)$, and rank is 2.

</details>

### 3. Check rank-nullity

Check the rank-nullity theorem for the matrix in Exercise 1.

<details>
<summary>Show solution</summary>

The input dimension is the column count, 3. Exercise 1 gives nullity 1, and Exercise 2 gives rank 2, so

\[
\operatorname{rank}(\mathbf A)
+
\operatorname{nullity}(\mathbf A)
=
2+1
=
3
\]

</details>

### 4. Existence of solutions

For

\[
\mathbf B=
\begin{bmatrix}
1&2\\
2&4\\
3&6
\end{bmatrix}
\]

determine whether the following vectors belong to $\operatorname{im}(\mathbf B)$.

\[
\mathbf b_1=
\begin{bmatrix}2\\4\\6\end{bmatrix},
\qquad
\mathbf b_2=
\begin{bmatrix}1\\2\\4\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

The image of $\mathbf B$ is

\[
\operatorname{span}
\left\{
\begin{bmatrix}1\\2\\3\end{bmatrix}
\right\}
\]

The target $\mathbf b_1$ is twice this generator, so it belongs to the image. For $\mathbf b_2$, matching the first component requires coefficient 1, but the third component is 4 rather than 3, so it does not belong to the image.

Thus, $\mathbf B\mathbf x=\mathbf b_1$ has a solution, but $\mathbf B\mathbf x=\mathbf b_2$ does not.

</details>

### 5. Uniqueness of solutions

Suppose $\mathbf A\mathbf x=\mathbf b$ has one solution $\mathbf x_0$ and

\[
\ker(\mathbf A)
=
\operatorname{span}\{\mathbf z_1,\mathbf z_2\}
\]

Write all solutions and determine whether the solution is unique.

<details>
<summary>Show solution</summary>

All solutions are

\[
\mathbf x
=
\mathbf x_0+s\mathbf z_1+t\mathbf z_2,
\qquad
s,t\in\mathbb R
\]

The kernel has two independent directions, so varying coefficients $s,t$ produces multiple solutions. The solution is not unique.

</details>

### 6. Determine invertibility

Find the rank of

\[
\mathbf C=
\begin{bmatrix}
1&0&2\\
0&1&-1\\
0&0&3
\end{bmatrix}
\]

and determine whether it is invertible.

<details>
<summary>Show solution</summary>

Each of the three rows and columns has a pivot, so

\[
\operatorname{rank}(\mathbf C)=3
\]

The matrix $\mathbf C$ is square, with shape $3\times3$ and rank 3. Its kernel is $\{\mathbf 0\}$, and its image is $\mathbb R^3$. It is therefore invertible.

</details>

### 7. Critique a model interpretation claim

Suppose a weight matrix $\mathbf W$ has rank 20 and input dimension 64.

1. Find its nullity.
2. State how many independent input directions disappear in the linear part.
3. Determine whether this alone establishes that the model uses only 20 human-interpretable features.

<details>
<summary>Show solution</summary>

Rank-nullity gives

\[
\operatorname{nullity}(\mathbf W)
=
64-20
=
44
\]

The kernel has dimension 44, so the linear part sends 44 independent input directions to zero.

Rank 20 counts independent directions in the image. It does not say whether these correspond one-to-one to human-named features, whether data use these directions, or whether later layers use them for behavior. Feature interpretation and functional use require data analyses and intervention experiments.

</details>

## Lesson summary

- The kernel is a subspace of inputs sent to zero and determines whether inputs can be distinguished.
- The image is the subspace of achievable outputs, equal to the span of the matrix's columns.
- Rank is image dimension; nullity is kernel dimension.
- Rank-nullity states that their dimensions sum to the input dimension.
- For $\mathbf A\mathbf x=\mathbf b$, existence follows from whether $\mathbf b$ belongs to the image; uniqueness is determined by the kernel.
- A weight matrix's rank describes linear structure, not direct evidence of feature meanings or model behavior.

## Pass criteria

You pass if you can answer these questions without consulting the material:

- Can you define the kernel and image using set notation?
- Can you find a kernel basis from a homogeneous system?
- Can you find an image basis from the original matrix's pivot columns?
- Can you calculate rank and nullity and check the theorem?
- Can you explain existence and uniqueness of solutions using the image and kernel?
- Can you distinguish algebraic rank claims from model-function claims?

## Next lesson

- [M02-09 Orthogonal bases and projection](M02-09-orthogonal-basis-projection.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Kernel and image are defined as subspaces of the domain and codomain.
- [x] The relationship between image and column space is explained.
- [x] Rank-nullity is connected to pivots and free variables.
- [x] Solution existence, uniqueness, and invertibility are connected.
- [x] Every exercise has a solution.
- [x] The scope of rank and model-feature claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
