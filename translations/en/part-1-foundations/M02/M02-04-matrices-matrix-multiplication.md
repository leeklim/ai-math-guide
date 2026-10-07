---
id: "M02-04"
title: "Matrices and matrix multiplication"
part: 1
stage: "M02"
status: "complete"
prerequisites:
  - "M00-09"
  - "M02-02"
  - "M02-03"
estimated_time: "110~135 minutes"
---

# M02-04. Matrices and matrix multiplication

## Why this lesson matters

A matrix combines several vector computations in one expression. Neural-network weights, collections of token activations, and attention scores are stored as matrices, and most of a forward pass is expressed through matrix multiplication.

Matrix multiplication does not multiply corresponding entries element by element. It takes the inner product of a row and a column; at the same time, it forms linear combinations of the columns of a matrix. Learning both views helps you identify shape errors and follow the computations in neural-network equations.

## Learning objectives

By the end of this lesson, you should be able to:

- Read the rows, columns, entries, and shape of a matrix from its notation.
- Compute a matrix–vector product using row inner products and column linear combinations.
- Determine the shape conditions under which two matrices can be multiplied and the shape of the result.
- Compute small products using the entrywise formula for matrix multiplication.
- Explain associativity, identity matrices, and order dependence in matrix multiplication.
- Distinguish the column-vector convention from the convention of storing samples in rows.

## Prerequisite check

- Prerequisite lesson: [M00-09 Shapes of scalars, vectors, and matrices](../M00/M00-09-scalars-vectors-matrices-shape.md)
- Prerequisite lesson: [M02-02 Linear combinations and span](M02-02-linear-combinations-span.md)
- Prerequisite lesson: [M02-03 Inner products, length, and angles](M02-03-inner-product-length-angle.md)
- Check question: Can you compute the inner product of two vectors and a linear combination of several vectors?
- Check question: Can you identify the numbers of rows and columns from a matrix shape $(m,n)$?

Review the prerequisite lessons first if inner products, linear combinations, or shapes are unclear.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\mathbf A=[a_{ij}]$ | `A equals the matrix with entries a sub i j` | A matrix whose entries are $a_{ij}$ | $\mathbf A\in\mathbb R^{m\times n}$ |
| $a_{ij}$ | `a sub i j` | The entry in row $i$, column $j$ of $\mathbf A$ | Scalar |
| $\mathbf A_{i:}$ | `row i of A` | The $i$th row vector | $1\times n$ |
| $\mathbf A_{:j}$ | `column j of A` | The $j$th column vector | $m\times1$ |
| $\mathbf I_n$ | `I sub n` | A matrix with diagonal entries 1 and all other entries 0 | $n\times n$ |
| $\mathbf C=\mathbf A\mathbf B$ | `C equals A B` | A matrix product formed from row–column inner products | The inner dimensions must match. |

## Core concept 1. A matrix is an array of numbers with rows and columns

A matrix with $m$ rows and $n$ columns is written as

\[
\mathbf A
=
\begin{bmatrix}
a_{11}&a_{12}&\cdots&a_{1n}\\
a_{21}&a_{22}&\cdots&a_{2n}\\
\vdots&\vdots&\ddots&\vdots\\
a_{m1}&a_{m2}&\cdots&a_{mn}
\end{bmatrix}
\in\mathbb R^{m\times n}
\]

The first index $i$ identifies the row, and the second index $j$ identifies the column.

The shape lists the number of rows before the number of columns. A matrix in $\mathbb R^{2\times3}$ has 2 rows, 3 columns, and 6 entries.

The figure below locates the second row and third column of the matrix in Exercise 1. Their intersection is the entry $a_{23}$.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Row two and column three intersect at entry five in a two by three matrix](../../figures/assets/M02/M02-04-rows-columns-entry.svg)

<figcaption>The first index selects the row, and the second selects the column. Here a₂₃=5. The shape (2,3) gives the total numbers of rows and columns, not the location of this entry.</figcaption>
</figure>

## Core concept 2. A matrix–vector product consists of row inner products

Multiplying $\mathbf A\in\mathbb R^{m\times n}$ by $\mathbf x\in\mathbb R^n$ gives

\[
\mathbf y=\mathbf A\mathbf x\in\mathbb R^m
\]

The $i$th output component is

\[
y_i
=
\sum_{j=1}^{n}a_{ij}x_j
\]

This is the inner product of the $i$th row of $\mathbf A$ with $\mathbf x$.

The input dimension $n$ must equal the number of matrix columns. The output dimension is the number of rows, $m$.

In the figure below, each row uses the same input from Example 1. Each row inner product produces one component of the output vector.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Each matrix row is dotted with the same input four five to produce output components fourteen and eleven](../../figures/assets/M02/M02-04-row-inner-products.svg)

<figcaption>The first row produces y₁=14, and the second produces y₂=11. Each row computes one scalar; these scalars are collected into the output column vector.</figcaption>
</figure>

## Core concept 3. The same product is a linear combination of columns

Let the columns of $\mathbf A$ be $\mathbf a_1,\ldots,\mathbf a_n\in\mathbb R^m$. Then

\[
\mathbf A
=
\begin{bmatrix}
\mathbf a_1&\mathbf a_2&\cdots&\mathbf a_n
\end{bmatrix}
\]

and

\[
\mathbf A\mathbf x
=
x_1\mathbf a_1+\cdots+x_n\mathbf a_n
\]

The input component $x_j$ multiplies the $j$th column of $\mathbf A$, and summing all these contributions gives the output vector. Thus $\mathbf A\mathbf x$ belongs to the span of the columns of $\mathbf A$.

The $i$th component of this linear combination is $x_1a_{i1}+\cdots+x_na_{in}$. It sums the same terms as the row inner product $\sum_j a_{ij}x_j$ in the preceding section. The row view computes one output component, whereas the column view computes the whole output vector at once. These are two expressions of the same product, not two different operations.

The figure below multiplies the columns in the same example by input coefficients 4 and 5. Placing the two displacements end to end reaches $(14,11)$, the same result as the row inner products.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Four times the first matrix column followed by five times the second column reaches the output fourteen eleven](../../figures/assets/M02/M02-04-column-combination.svg)

<figcaption>4(1,-1)ᵀ+5(2,3)ᵀ=(14,11)ᵀ. Each grid interval represents two units. Compare the sum of the blue and purple displacements with the green output vector.</figcaption>
</figure>

## Core concept 4. Matrix multiplication sums over the inner dimension

If

\[
\mathbf A\in\mathbb R^{m\times n},
\qquad
\mathbf B\in\mathbb R^{n\times p}
\]

then

\[
\mathbf C=\mathbf A\mathbf B\in\mathbb R^{m\times p}
\]

The number of columns $n$ in the left matrix must equal the number of rows $n$ in the right matrix.

Each output entry is

\[
c_{ij}
=
\sum_{k=1}^{n}a_{ik}b_{kj}
\]

It is the inner product of row $i$ of $\mathbf A$ and column $j$ of $\mathbf B$. The inner index $k$ is summed over and does not remain in the output.

The figure below shows how to select the output entry $c_{22}$ in Example 2. The three entries in the second row on the left are paired with those in the second column on the right, multiplied, and summed.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The second row of a two by three matrix and second column of a three by two matrix yield output entry nine](../../figures/assets/M02/M02-04-row-column-product.svg)

<figcaption>The inner dimension being summed over is 3, and the outer dimensions remaining in the result are 2×2. The highlighted row–column inner product is −1+12−2=9, placed in row two, column two of the output.</figcaption>
</figure>

## Core concept 5. Matrix multiplication combines several matrix–vector products

If the columns of $\mathbf B$ are $\mathbf b_1,\ldots,\mathbf b_p$, then

\[
\mathbf A\mathbf B
=
\begin{bmatrix}
\mathbf A\mathbf b_1&
\mathbf A\mathbf b_2&
\cdots&
\mathbf A\mathbf b_p
\end{bmatrix}
\]

Apply $\mathbf A$ to each column of the right matrix, and collect the results as columns of a new matrix.

Viewed another way, each column of $\mathbf A\mathbf B$ is a linear combination of the columns of $\mathbf A$. Its coefficients come from the corresponding column of $\mathbf B$.

The figure below applies the same matrix to the two input columns in Example 2. Collecting the output columns in the input order gives the entire matrix product.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two input columns pass through the same numeric matrix and become the two corresponding output columns](../../figures/assets/M02/M02-04-column-batch.svg)

<figcaption>b₁ becomes (2,3)ᵀ, and b₂ becomes (9,9)ᵀ. Computing the columns separately gives the same result as computing AB at once.</figcaption>
</figure>

## Core concept 6. Matrix multiplication is associative, but order cannot generally be reversed

When the shapes are compatible,

\[
(\mathbf A\mathbf B)\mathbf C
=
\mathbf A(\mathbf B\mathbf C)
\]

Matrix multiplication is associative.

This can also be checked entry by entry. With intermediate indices $k,r$, the $i,j$ entry of $(\mathbf A\mathbf B)\mathbf C$ and the $i,j$ entry of $\mathbf A(\mathbf B\mathbf C)$ are equal:

\[
\sum_r\left(\sum_k a_{ik}b_{kr}\right)c_{rj}
=\sum_k a_{ik}\left(\sum_r b_{kr}c_{rj}\right)
\]

Both sides sum $a_{ik}b_{kr}c_{rj}$ over all pairs of intermediate indices. Distributivity and associativity of finite sums change the grouping, while the matrix order $\mathbf A,\mathbf B,\mathbf C$ stays the same.

In general,

\[
\mathbf A\mathbf B\ne\mathbf B\mathbf A
\]

Only one product may be defined; even when both are defined, their values or shapes may differ. Matrix order determines the order of operations in a neural-network computation.

For a column vector, $(\mathbf A\mathbf B)\mathbf x=\mathbf A(\mathbf B\mathbf x)$ applies the rightmost matrix $\mathbf B$ first and then applies $\mathbf A$ to the result. Reversing the order to $\mathbf B\mathbf A$ changes the first computation. Associativity changes only the grouping of intermediate products.

The figure below applies the two matrices in Example 3 to the input $(1,1)^\top$. Reversing their order changes even the intermediate vector.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Applying scale B then shear A produces five three while applying shear A then scale B produces four three](../../figures/assets/M02/M02-04-multiplication-order.svg)

<figcaption>ABx first applies B to obtain (2,3)ᵀ, then produces the final output (5,3)ᵀ. The reverse order produces (4,3)ᵀ. Changing the grouping and reversing the order are different operations.</figcaption>
</figure>

## Core concept 7. The identity matrix leaves vectors and matrices unchanged

The $n\times n$ identity matrix is

\[
\mathbf I_n
=
\begin{bmatrix}
1&0&\cdots&0\\
0&1&\cdots&0\\
\vdots&\vdots&\ddots&\vdots\\
0&0&\cdots&1
\end{bmatrix}
\]

It satisfies

\[
\mathbf I_n\mathbf x=\mathbf x
\]

and, for $\mathbf A\in\mathbb R^{m\times n}$,

\[
\mathbf I_m\mathbf A=\mathbf A,
\qquad
\mathbf A\mathbf I_n=\mathbf A
\]

The size of the identity matrix must match its position in the product.

In the $i$th component of $\mathbf I_n\mathbf x$, only the $i$th coefficient is 1; the others are 0, so only $x_i$ remains. The same selection applies to matrices. $\mathbf I_m\mathbf A$ leaves the rows unchanged, and $\mathbf A\mathbf I_n$ leaves the columns unchanged. When the row count $m$ differs from the column count $n$, the identities on the left and right have different sizes as well.

In the figure below, each diagonal 1 retains the corresponding input component, while the other 0 entries remove contributions from the remaining components. The row inner products reproduce the input vector.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The diagonal ones of the identity matrix select each matching component and preserve the input column four five six](../../figures/assets/M02/M02-04-identity-selection.svg)

<figcaption>The first row retains only 4, the second only 5, and the third only 6. This selection structure explains why the identity matrix leaves a vector unchanged.</figcaption>
</figure>

## Core concept 8. Row-wise data require a transpose

With each input represented as a column vector,

\[
\mathbf y=\mathbf W\mathbf x,
\qquad
\mathbf W\in\mathbb R^{d_{\mathrm{out}}\times d_{\mathrm{in}}}
\]

If the transposes of $N$ inputs are collected as rows,

\[
\mathbf X
=
\begin{bmatrix}
\mathbf x_1^\top\\
\vdots\\
\mathbf x_N^\top
\end{bmatrix}
\in\mathbb R^{N\times d_{\mathrm{in}}}
\]

the same computation becomes

\[
\mathbf Y=\mathbf X\mathbf W^\top
\in\mathbb R^{N\times d_{\mathrm{out}}}
\]

Write the entry in row $i$, column $j$ of $\mathbf W$ as $w_{ij}$. In the original column-vector expression, output $i$ for sample $n$ is $\sum_j w_{ij}(x_n)_j$. The corresponding entry in the row-data product computes $\sum_j X_{nj}(W^\top)_{ji}$. Since $X_{nj}=(x_n)_j$ and $(W^\top)_{ji}=w_{ij}$, every output component agrees. The transpose places each output's weight row in the column position read by matrix multiplication. Do not mix the theoretical column-vector convention with the data convention of storing samples in rows.

The figure below computes the same weights and input under both storage conventions. The two values in the upper output column vector appear in the same order in the first row of the lower output matrix.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The same sample produces the same output under column multiplication W x and row stacked multiplication X W transpose](../../figures/assets/M02/M02-04-row-data-transpose.svg)

<figcaption>The upper calculation gives Wx₁=(2,1)ᵀ. The lower calculation stores two inputs in rows and multiplies by Wᵀ; its first output row is also (2,1). The sample count remains 2, while the feature count changes from 3 to 2.</figcaption>
</figure>

## Example 1. A matrix–vector product

Let

\[
\mathbf A=
\begin{bmatrix}
1&2\\
-1&3
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}
4\\
5
\end{bmatrix}
\]

Using row inner products gives

\[
\mathbf A\mathbf x
=
\begin{bmatrix}
1\cdot4+2\cdot5\\
-1\cdot4+3\cdot5
\end{bmatrix}
=
\begin{bmatrix}
14\\
11
\end{bmatrix}
\]

Using a linear combination of columns gives the same result:

\[
\mathbf A\mathbf x
=
4
\begin{bmatrix}1\\-1\end{bmatrix}
+
5
\begin{bmatrix}2\\3\end{bmatrix}
=
\begin{bmatrix}14\\11\end{bmatrix}
\]

## Example 2. A product of two matrices

Let

\[
\mathbf A=
\begin{bmatrix}
1&2&0\\
-1&3&1
\end{bmatrix},
\qquad
\mathbf B=
\begin{bmatrix}
2&1\\
0&4\\
5&-2
\end{bmatrix}
\]

Their shapes are $2\times3$ and $3\times2$, so the product has shape $2\times2$.

\[
\mathbf A\mathbf B
=
\begin{bmatrix}
1\cdot2+2\cdot0+0\cdot5&
1\cdot1+2\cdot4+0(-2)\\
-1\cdot2+3\cdot0+1\cdot5&
-1\cdot1+3\cdot4+1(-2)
\end{bmatrix}
=
\begin{bmatrix}
2&9\\
3&9
\end{bmatrix}
\]

## Example 3. Multiplication order changes the result

For

\[
\mathbf A=
\begin{bmatrix}
1&1\\
0&1
\end{bmatrix},
\qquad
\mathbf B=
\begin{bmatrix}
2&0\\
0&3
\end{bmatrix}
\]

we obtain

\[
\mathbf A\mathbf B
=
\begin{bmatrix}
2&3\\
0&3
\end{bmatrix}
\]

and

\[
\mathbf B\mathbf A
=
\begin{bmatrix}
2&2\\
0&3
\end{bmatrix}
\]

The two matrices have the same shape, but reversing their multiplication order changes the values.

## Example 4. Applying a linear layer to a token matrix

Given $T$ token activations stored as rows,

\[
\mathbf H\in\mathbb R^{T\times d_{\mathrm{in}}}
\]

and weights

\[
\mathbf W\in\mathbb R^{d_{\mathrm{out}}\times d_{\mathrm{in}}}
\]

we have

\[
\mathbf Z=\mathbf H\mathbf W^\top
\in\mathbb R^{T\times d_{\mathrm{out}}}
\]

The $T$ axis is preserved, and each token's feature dimension changes from $d_{\mathrm{in}}$ to $d_{\mathrm{out}}$.

Tracking shapes checks whether the computation is defined. Further analysis is needed to determine whether an output coordinate represents a particular concept.

## Common misconceptions

### Misconception 1. Matrix multiplication multiplies entries at matching positions

One entry of a matrix product is the inner product of a row on the left and a column on the right. This differs from the Hadamard product, which multiplies only entries at matching positions.

### Misconception 2. Two matrices can be multiplied if they have the same total number of entries

The left column count must equal the right row count. The total number of entries is not the condition that defines a matrix product.

### Misconception 3. If $\mathbf A\mathbf B$ is defined, so is $\mathbf B\mathbf A$

The inner-dimension conditions differ for the two products. Even when both are defined, they need not have the same result.

### Misconception 4. Compatible shapes guarantee the right meaning

Shapes check formal compatibility for computation. You must also check what the rows and columns represent and whether the same sample and feature orders are used.

## Exercises

### 1. Matrix entries and shape

Find the shape, $a_{12}$, and $a_{23}$ of

\[
\mathbf A=
\begin{bmatrix}
2&-1&4\\
0&3&5
\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

There are 2 rows and 3 columns, so $\mathbf A\in\mathbb R^{2\times3}$. The entry in row one, column two is $a_{12}=-1$; the entry in row two, column three is $a_{23}=5$.

</details>

### 2. A matrix–vector product

Find $\mathbf A\mathbf x$ for

\[
\mathbf A=
\begin{bmatrix}
2&1\\
0&-1\\
3&2
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}4\\-2\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

\[
\mathbf A\mathbf x
=
\begin{bmatrix}
2\cdot4+1(-2)\\
0\cdot4+(-1)(-2)\\
3\cdot4+2(-2)
\end{bmatrix}
=
\begin{bmatrix}6\\2\\8\end{bmatrix}
\]

A $3\times2$ matrix multiplies a vector of dimension 2 to produce a vector of dimension 3.

</details>

### 3. A linear combination of columns

Recompute $\mathbf A\mathbf x$ in Exercise 2 as a linear combination of the two columns of $\mathbf A$.

<details>
<summary>Show solution</summary>

The two columns of $\mathbf A$ are

\[
\mathbf a_1=
\begin{bmatrix}2\\0\\3\end{bmatrix},
\qquad
\mathbf a_2=
\begin{bmatrix}1\\-1\\2\end{bmatrix}
\]

Therefore,

\[
\mathbf A\mathbf x
=
4\mathbf a_1-2\mathbf a_2
=
\begin{bmatrix}8\\0\\12\end{bmatrix}
-
\begin{bmatrix}2\\-2\\4\end{bmatrix}
=
\begin{bmatrix}6\\2\\8\end{bmatrix}
\]

</details>

### 4. Checking shapes

For the following matrices, determine whether each product is defined. If it is, give its output shape.

\[
\mathbf A\in\mathbb R^{3\times4},
\qquad
\mathbf B\in\mathbb R^{4\times2},
\qquad
\mathbf C\in\mathbb R^{3\times2}
\]

1. $\mathbf A\mathbf B$
2. $\mathbf B\mathbf A$
3. $\mathbf A^\top\mathbf C$

<details>
<summary>Show solution</summary>

$\mathbf A\mathbf B$ is defined because both inner dimensions are 4, and its shape is $3\times2$.

$\mathbf B\mathbf A$ is not defined: the inner dimensions of $4\times2$ and $3\times4$ are 2 and 3, respectively, and do not match.

Since $\mathbf A^\top\in\mathbb R^{4\times3}$, $\mathbf A^\top\mathbf C$ is defined and has shape $4\times2$.

</details>

### 5. Computing a matrix product

Find $\mathbf A\mathbf B$ for

\[
\mathbf A=
\begin{bmatrix}
1&2\\
3&0
\end{bmatrix},
\qquad
\mathbf B=
\begin{bmatrix}
-1&4\\
2&1
\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

\[
\mathbf A\mathbf B
=
\begin{bmatrix}
1(-1)+2\cdot2&1\cdot4+2\cdot1\\
3(-1)+0\cdot2&3\cdot4+0\cdot1
\end{bmatrix}
=
\begin{bmatrix}
3&6\\
-3&12
\end{bmatrix}
\]

</details>

### 6. Comparing orders

For the matrices in Exercise 5, also compute $\mathbf B\mathbf A$ and compare it with $\mathbf A\mathbf B$.

<details>
<summary>Show solution</summary>

\[
\mathbf B\mathbf A
=
\begin{bmatrix}
-1\cdot1+4\cdot3&-1\cdot2+4\cdot0\\
2\cdot1+1\cdot3&2\cdot2+1\cdot0
\end{bmatrix}
=
\begin{bmatrix}
11&-2\\
5&4
\end{bmatrix}
\]

The values differ from $\mathbf A\mathbf B$, so these two matrices do not commute.

</details>

### 7. The shape of a data matrix

Let $N=32$, $d_{\mathrm{in}}=128$, $d_{\mathrm{out}}=64$, with

\[
\mathbf X\in\mathbb R^{32\times128},
\qquad
\mathbf W\in\mathbb R^{64\times128}
\]

1. Find the shape of $\mathbf X\mathbf W^\top$.
2. Explain what one row of the result represents.
3. Decide whether shapes alone determine the meaning of the output coordinates.

<details>
<summary>Show solution</summary>

Since $\mathbf W^\top\in\mathbb R^{128\times64}$,

\[
\mathbf X\mathbf W^\top
\in
\mathbb R^{32\times64}
\]

Each row is a 64-dimensional output obtained by applying the same linear computation to the 128-dimensional vector of one input sample.

The shape identifies the structure: rows are samples, and columns are output features. It does not determine the meaning of each feature or how that feature contributes to model behavior.

</details>

## Lesson summary

- An $m\times n$ matrix has $m$ rows and $n$ columns; the first index identifies the row.
- A matrix–vector product consists of row inner products and can also be read as a linear combination of matrix columns.
- $\mathbf A\mathbf B$ is defined when the left column count equals the right row count.
- Matrix multiplication is associative, but reversing multiplication order can change the result.
- When samples are stored in rows, transposing the weights in the column-vector expression represents the same computation.

## Pass criteria

You pass if you can answer these questions without consulting the material.

- Can you identify the row and column of a matrix entry $a_{ij}$?
- Can you compute a matrix–vector product from both views?
- Can you determine whether a matrix product is defined and find its output shape?
- Can you compute the entries of a small matrix product directly?
- Can you distinguish associativity from multiplication order?
- Can you convert between the column-vector and row-wise data conventions?

## Next lesson

- [M02-05 Matrices as linear transformations](M02-05-matrix-as-linear-transformation.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Rows, columns, entries, and shapes are defined.
- [x] Both row inner products and column linear combinations are explained.
- [x] Matrix-product shapes and the entry formula are given.
- [x] The column-vector and row-wise data conventions are distinguished.
- [x] Every exercise has a solution.
- [x] Shapes are distinguished from interpretations of meaning.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
