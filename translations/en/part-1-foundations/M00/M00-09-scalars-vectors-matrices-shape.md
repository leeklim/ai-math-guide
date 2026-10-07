---
id: "M00-09"
title: "Shapes of scalars, vectors, and matrices"
part: 1
stage: "M00"
status: "complete"
prerequisites:
  - "M00-03"
  - "M00-06"
estimated_time: "105~125 minutes"
---

# M00-09. Shapes of scalars, vectors, and matrices

## Why this lesson matters

Neural-network equations combine single numbers, lists of values, and rectangular arrays in the same expression. Checking the shape of each symbol lets you decide, before calculating, whether addition is possible, whether the inner dimensions of a matrix product match, and which dimensions remain in the output.

\[
\mathbf y=\mathbf W\mathbf x+\mathbf b
\]

In this equation, the length of $\mathbf x$, the number of columns of $\mathbf W$, and the length of $\mathbf b$ must be compatible. Even when a paper omits shapes, you need to recover them from the surrounding definitions. Before studying the structure of linear algebra, this lesson introduces the types of mathematical objects and how to check their shapes.

## Learning objectives

After this lesson, you will be able to:

- Distinguish scalars, vectors, matrices, and multidimensional arrays by their notation and shape.
- Read $\mathbb R^n$ and $\mathbb R^{m\times n}$.
- Determine the shape conditions for addition, inner products, matrix–vector products, and matrix products.
- Assign compatible shapes to the objects in $\mathbf y=\mathbf W\mathbf x+\mathbf b$.
- Explain each symbol in an activation shape that includes batch and token axes.

## Prerequisite check

- Prerequisite lesson: [M00-03. Function inputs and outputs](M00-03-functions-input-output.md)
- Prerequisite lesson: [M00-06. Indices and summation notation](M00-06-indices-summation.md)

Check that you can read the following notation:

\[
x_i,\qquad a_{ij},\qquad \sum_{j=1}^{n}a_{ij}x_j
\]

$x_i$ is the $i$th value, while $a_{ij}$ uses two indices to identify a position. The last expression holds $i$ fixed and sums terms over $j$.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape |
|---|---|---|---|
| $x\in\mathbb R$ | `x is in R` | A scalar | A scalar; no axes |
| $\mathbf x\in\mathbb R^n$ | `x is in R to the n` | A vector with $n$ components | A column vector of shape $n\times1$ in theoretical equations |
| $\mathbf A\in\mathbb R^{m\times n}$ | `A is an m by n real matrix` | A matrix with $m$ rows and $n$ columns | $m\times n$ |
| $a_{ij}$ | `a sub i j` | The entry of $\mathbf A$ in row $i$, column $j$ | A scalar |
| $\mathbf A^\top$ | `A transpose` | A matrix with its rows and columns exchanged | $n\times m$ |
| $d$ | `d` | Vector or feature dimension | A positive integer |
| $B$ | `B` | Batch size | Number of samples |
| $T$ | `T` | Token or sequence length | Number of positions |

## Core concept 1. Scalars, vectors, and matrices

### Scalars

A scalar is a single number. Scalars are usually written with italic lowercase symbols, as in

\[
x=3.5,\qquad \alpha=-2
\]

A loss value, a learning rate, and a probability are examples of scalars.

### Vectors

In this lesson, a vector is represented as an ordered column of components.

\[
\mathbf x
=
\begin{bmatrix}
x_1\\
x_2\\
\vdots\\
x_n
\end{bmatrix}
\in\mathbb R^n
\]

$\mathbb R^n$ is the space of vectors with $n$ real-valued components. The dimension of $\mathbf x$ is $n$. Written out as a column, its shape is $n\times1$, but vector notation abbreviates this as $\mathbb R^n$.

Vectors are written with bold lowercase symbols such as $\mathbf x$. An individual component $x_i$ is a scalar.

### Matrices

A matrix is an object whose entries are arranged in rows and columns.

\[
\mathbf A
=
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n}\\
a_{21} & a_{22} & \cdots & a_{2n}\\
\vdots & \vdots & \ddots & \vdots\\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
\in\mathbb R^{m\times n}
\]

Here $m$ is the number of rows, and $n$ is the number of columns. The shape is written with the row count first:

\[
m\times n
\]

In the entry $a_{ij}$, $i$ identifies the row and $j$ the column.

The next figure shows both the values in an array and the axes used to identify their positions.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A scalar has one value without axes, a column vector has three component positions, and a two by three matrix has two rows and three columns with element a sub two three equal six highlighted](../../figures/assets/M00/M00-09-scalar-vector-matrix.svg)

<figcaption>A single value has no row or column axis. The column vector places three components in one column, while the matrix uses two axes to identify positions. The 6 on the right is the entry in row 2, column 3.</figcaption>
</figure>

## Core concept 2. Shape restricts which operations are possible

### Addition

Two vectors must have the same dimension to be added.

\[
\mathbf x,\mathbf y\in\mathbb R^n
\quad\Rightarrow\quad
\mathbf x+\mathbf y\in\mathbb R^n
\]

Matrices must also have the same shape for entrywise addition.

\[
\mathbf A,\mathbf B\in\mathbb R^{m\times n}
\quad\Rightarrow\quad
\mathbf A+\mathbf B\in\mathbb R^{m\times n}
\]

A $2\times3$ matrix and a $3\times2$ matrix have the same number of entries, but their positions are organized differently, so they cannot be added as they are.

Addition pairs components at matching positions. For vectors, the $i$th result is $x_i+y_i$; for matrices, it adds the two values at the same row and column position. Each result requires a matching pair, so the size of each axis must agree, not just the total number of entries.

In the next figure, both arrays have the same number of entries, but the position in row 1, column 3 on the left does not exist on the right.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A two by three array and a three by two array contain six values each, but position row one column three exists only in the first array](../../figures/assets/M00/M00-09-addition-position-match.svg)

<figcaption>Adding the arrays as they are requires pairing values at the same row and column position. Flattening both arrays to match their six entries is a different operation from adding the original matrices.</figcaption>
</figure>

### Scalar multiplication

Multiplying every entry of a vector or matrix by a scalar $\alpha$ preserves its shape.

\[
\alpha\mathbf x\in\mathbb R^n
\]

\[
\alpha\mathbf A\in\mathbb R^{m\times n}
\]

### Vector inner products

The inner product of two $n$-dimensional vectors is

\[
\mathbf x^\top\mathbf y
=
\sum_{i=1}^{n}x_i y_i
\]

and its result is a scalar.

Multiplying components with the same index gives $n$ terms, and summing those terms leaves a single value. Scalar multiplication preserves the list of components, whereas an inner product combines two lists into one value.

\[
\mathbf x^\top\mathbf y\in\mathbb R
\]

In terms of shapes,

\[
(1\times n)(n\times1)=1\times1
\]

and the result is interpreted as a scalar.

The next figure compares scalar multiplication, which preserves the components, with an inner product, which sums componentwise products.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Scaling vector one two three by two keeps three components, but pairing it with vector four minus one two and summing products gives the scalar eight](../../figures/assets/M00/M00-09-scalar-multiply-vs-inner-product.svg)

<figcaption>On the left, only the value at each position changes, leaving three components. On the right, the products of matching components, 4, −2, and 6, are summed to give one scalar.</figcaption>
</figure>

## Core concept 3. Matrix–vector multiplication requires matching inner dimensions

If

\[
\mathbf A\in\mathbb R^{m\times n},
\qquad
\mathbf x\in\mathbb R^n
\]

then we can calculate

\[
\mathbf y=\mathbf A\mathbf x
\]

and the result satisfies

\[
\mathbf y\in\mathbb R^m
\]

Writing only the shapes gives

\[
(m\times n)(n\times1)
\longrightarrow
(m\times1)
\]

The inner dimensions $n$ must match, while the outer dimension $m$ remains as the output dimension.

The $i$th output component is

\[
y_i
=
\sum_{j=1}^{n}a_{ij}x_j
\]

This calculation multiplies the entries in row $i$ of the matrix by all the components of the input vector and sums the products.

The $n$ coefficients in a row must pair with the $n$ input components, so the number of matrix columns must equal the input length. Summing over $j$ gives that row's single output $y_i$. With $m$ rows, there are $m$ such outputs. Both the inner-dimension requirement and the output dimension follow from the componentwise calculation.

### A small calculation

If

\[
\mathbf A=
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}
5\\
6
\end{bmatrix}
\]

then

\[
\mathbf A\mathbf x
=
\begin{bmatrix}
1\cdot5+2\cdot6\\
3\cdot5+4\cdot6
\end{bmatrix}
=
\begin{bmatrix}
17\\
39
\end{bmatrix}
\]

In the next figure, the two coefficients in one row pair with the two input components to produce one output.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two columns of matrix A match the two input vector entries five and six, and each of its two rows produces one output entry seventeen or thirty-nine](../../figures/assets/M00/M00-09-matrix-vector-row-output.svg)

<figcaption>The highlighted first row produces 17. Multiplying the same input by the second row's coefficients and summing gives 39. Two rows therefore produce two output components.</figcaption>
</figure>

## Core concept 4. The output shape of a matrix product

If

\[
\mathbf A\in\mathbb R^{m\times n},
\qquad
\mathbf B\in\mathbb R^{n\times p}
\]

then

\[
\mathbf A\mathbf B\in\mathbb R^{m\times p}
\]

The shape calculation reads

\[
(m\times n)(n\times p)
\longrightarrow
(m\times p)
\]

The number of columns of the first matrix must equal the number of rows of the second.

Treat each column of $\mathbf B$ as an input vector of length $n$. Multiplication by $\mathbf A$ produces a vector of length $m$. Because $\mathbf B$ has $p$ columns, we obtain $p$ such output vectors; collecting them as columns gives an $m\times p$ matrix. The output shape of a matrix product comes from applying the same matrix–vector product to each column.

If we reverse the order, the inner dimensions of

\[
\mathbf B\mathbf A
\]

are $p$ and $m$. Unless $p=m$, this product is undefined. Even if both products are defined, their output shapes and values may differ.

M02 develops matrix multiplication and its interpretation as a linear transformation in detail. Here, we first learn to determine whether an operation is possible and what its output shape will be.

In the next figure, the highlighted column of the second matrix contains three input components, and the corresponding column of the product contains two output components.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A two by three matrix acts on each length-three column of a three by two matrix and produces two length-two columns, so the output shape is two by two](../../figures/assets/M00/M00-09-matrix-product-shape.svg)

<figcaption>A acts on each column of B. The length of each column changes from 3 to 2, while the number of input columns, 2, is preserved. The inner dimension 3 is used in the sum for each column.</figcaption>
</figure>

## Core concept 5. Transposition exchanges rows and columns

The transpose of

\[
\mathbf A\in\mathbb R^{m\times n}
\]

is

\[
\mathbf A^\top\in\mathbb R^{n\times m}
\]

The entries are related by

\[
(\mathbf A^\top)_{ij}=a_{ji}
\]

For example, if

\[
\mathbf A=
\begin{bmatrix}
1&2&3\\
4&5&6
\end{bmatrix}
\]

then

\[
\mathbf A^\top=
\begin{bmatrix}
1&4\\
2&5\\
3&6
\end{bmatrix}
\]

The shape of $\mathbf A$ is $2\times3$, and that of $\mathbf A^\top$ is $3\times2$.

The transpose $\mathbf x^\top$ of a column vector $\mathbf x\in\mathbb R^n$ is a row vector of shape $1\times n$.

The next figure follows the three values in the first row into the first column of the transposed matrix.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The first row one two three of a two by three matrix becomes the first column of its three by two transpose while all six values remain unchanged](../../figures/assets/M00/M00-09-transpose-row-column.svg)

<figcaption>The values 1, 2, and 3 retain their order, but the horizontal row becomes a vertical column. The 6 originally in row 2, column 3 moves to row 3, column 2 after transposition.</figcaption>
</figure>

## Core concept 6. Shapes in an affine layer

An affine layer with input dimension $d_{\mathrm{in}}$ and output dimension $d_{\mathrm{out}}$ is written as

\[
\mathbf y=\mathbf W\mathbf x+\mathbf b
\]

Here $\mathbf W$ is the weight matrix, and $\mathbf b$ is the bias vector.

The shapes of the objects are

\[
\mathbf x\in\mathbb R^{d_{\mathrm{in}}}
\]

\[
\mathbf W\in
\mathbb R^{d_{\mathrm{out}}\times d_{\mathrm{in}}}
\]

\[
\mathbf b,\mathbf y\in
\mathbb R^{d_{\mathrm{out}}}
\]

In $\mathbf W\mathbf x$, the inner dimensions $d_{\mathrm{in}}$ match, and the result is a $d_{\mathrm{out}}$-dimensional vector. Adding $\mathbf b$, which has the same dimension, gives the output $\mathbf y$.

### A numerical example

Let

\[
\mathbf W=
\begin{bmatrix}
1&0&-1\\
2&1&0
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}
3\\
4\\
5
\end{bmatrix},
\qquad
\mathbf b=
\begin{bmatrix}
1\\
-2
\end{bmatrix}
\]

Their shapes are

\[
\mathbf W:2\times3,\qquad
\mathbf x:3\times1,\qquad
\mathbf b:2\times1
\]

Since

\[
\mathbf W\mathbf x
=
\begin{bmatrix}
1\cdot3+0\cdot4-1\cdot5\\
2\cdot3+1\cdot4+0\cdot5
\end{bmatrix}
=
\begin{bmatrix}
-2\\
10
\end{bmatrix}
\]

we obtain

\[
\mathbf y
=
\mathbf W\mathbf x+\mathbf b
=
\begin{bmatrix}
-1\\
8
\end{bmatrix}
\]

In the next figure, the bias matches the matrix product's output length of 2, not the input length of 3.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A two by three weight matrix produces two values minus two and ten, and a two-entry bias one minus two adds at matching positions to give minus one and eight](../../figures/assets/M00/M00-09-affine-bias-matching.svg)

<figcaption>The first components of Wx and b are added together, as are their second components. The bias has the same length as the output, 2, so a value can be assigned to both positions.</figcaption>
</figure>

## Core concept 7. A batch may stack samples as rows

In theoretical equations, we have treated each individual vector as a column vector. Code and data matrices often use the convention of stacking each sample as a row.

\[
\mathbf X\in\mathbb R^{B\times d_{\mathrm{in}}}
\]

Here $B$ is the batch size, and each row is the transpose $\mathbf x_b^\top$ of one sample.

A row of $\mathbf W$, used to calculate an individual output component, contains the coefficients that multiply each input feature. When samples are stacked as rows, each sample row must be multiplied by these coefficients and the products summed. Transposing $\mathbf W$ places the coefficients in the columns of the matrix on the right. The roles of samples and features are unchanged; only their orientation in the array differs.

Applying the same weight matrix to every row gives

\[
\mathbf Y
=
\mathbf X\mathbf W^\top
+
\mathbf 1\mathbf b^\top
\]

Since

\[
\mathbf W^\top
\in
\mathbb R^{d_{\mathrm{in}}\times d_{\mathrm{out}}}
\]

the shapes are

\[
(B\times d_{\mathrm{in}})
(d_{\mathrm{in}}\times d_{\mathrm{out}})
\longrightarrow
(B\times d_{\mathrm{out}})
\]

The vector $\mathbf 1\in\mathbb R^B$ has all its components equal to $1$. The product $\mathbf 1\mathbf b^\top$ repeats the bias $\mathbf b^\top$ across $B$ rows, producing a $B\times d_{\mathrm{out}}$ matrix.

Deep-learning libraries use broadcasting to express the same calculation compactly. In a mathematical expression, the shapes make explicit the axis along which values are repeated.

The first figure below applies W from the numerical example to two different sample rows. It shows the result before adding the bias.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two sample rows with three features each pass independently through the same three by two weight transpose to produce two output features per sample](../../figures/assets/M00/M00-09-batch-shared-weight.svg)

<figcaption>The two rows are different samples. Both use the same Wᵀ, but the rows are not mixed, so the sample count remains 2 while the feature count changes from 3 to 2.</figcaption>
</figure>

The second figure repeats the bias in each sample row to create an array that can be added to the output.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The column bias one minus two is transposed to a row and repeated twice across the sample axis to form a two by two bias array](../../figures/assets/M00/M00-09-batch-bias-repetition.svg)

<figcaption>When B=2, bᵀ is placed in the same order in both rows. This does not add new features; it applies the same two bias values to each sample.</figcaption>
</figure>

## Core concept 8. Activations can have three or more axes

The activations of one Transformer layer can be represented as

\[
\mathbf H^{(\ell)}
\in
\mathbb R^{B\times T\times d_{\mathrm{model}}}
\]

- $B$: the number of samples in the batch
- $T$: the number of token positions in each sample
- $d_{\mathrm{model}}$: the hidden dimension of one token
- $\ell$: the layer index

The entry

\[
h^{(\ell)}_{b,t,i}
\]

is the scalar activation for batch item $b$, token position $t$, and feature $i$ in layer $\ell$.

Holding $b$ and $t$ fixed and varying only the feature index $i$ reads the $d_{\mathrm{model}}$ components of one token. Specifying $i$ as well selects a single value. The superscript $(\ell)$ labels the layer whose array is being described; it does not add another layer axis to this expression's shape.

In implementations, such multidimensional arrays are handled as tensors. The term “tensor” does not restrict the number of axes to three or more: scalars, vectors, and matrices can also be represented as tensors. M03 introduces the abstract definition of a tensor. For now, check what each axis counts and the order of the axes.

For example, if

\[
B=2,\qquad T=4,\qquad d_{\mathrm{model}}=3
\]

then the number of activation entries is

\[
2\cdot4\cdot3=24
\]

The next figure fills an array of this shape with illustrative numbers. First choose a batch item to select one table, then use the token and feature indices to narrow down the position.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two batch tables each have four token rows and three feature columns, the second batch third token row contains nineteen twenty twenty-one, and selecting its second feature gives scalar twenty](../../figures/assets/M00/M00-09-activation-three-axes.svg)

<figcaption>Selecting b=2 and t=3 leaves the feature vector 19, 20, 21. Specifying i=2 selects the single value 20. The two tables contain 24 entries in total, and the layer label ℓ distinguishes which array is shown.</figcaption>
</figure>

## Example 1. Identifying object types and shapes

Classify the following three objects:

\[
a=2
\]

\[
\mathbf x=
\begin{bmatrix}
1\\
0\\
-1
\end{bmatrix}
\]

\[
\mathbf A=
\begin{bmatrix}
1&2&3\\
4&5&6
\end{bmatrix}
\]

$a$ is a scalar. $\mathbf x$ is a vector of dimension $3$ and has shape $3\times1$ in column notation. $\mathbf A$ is a matrix with $2$ rows and $3$ columns, so its shape is $2\times3$.

## Example 2. Checking whether operations are possible

Suppose

\[
\mathbf A\in\mathbb R^{4\times3},
\quad
\mathbf B\in\mathbb R^{3\times2},
\quad
\mathbf C\in\mathbb R^{4\times2}
\]

The product

\[
\mathbf A\mathbf B
\]

can be calculated because the inner dimensions $3$ match, and its shape is $4\times2$. Therefore,

\[
\mathbf A\mathbf B+\mathbf C
\]

can also be calculated: both terms have shape $4\times2$.

By contrast, $\mathbf B\mathbf A$ is undefined because the inner dimensions $2$ and $4$ differ in

\[
(3\times2)(4\times3)
\]

## Example 3. Finding an invalid layer equation

Suppose the input dimension is $5$ and the output dimension is $2$. With the shapes

\[
\mathbf x\in\mathbb R^5,
\qquad
\mathbf W\in\mathbb R^{5\times2},
\qquad
\mathbf b\in\mathbb R^2
\]

we cannot calculate

\[
\mathbf W\mathbf x+\mathbf b
\]

because the inner dimensions $2$ and $5$ do not match in

\[
(5\times2)(5\times1)
\]

Under the column-vector convention, changing the weight shape to

\[
\mathbf W\in\mathbb R^{2\times5}
\]

gives

\[
(2\times5)(5\times1)
\longrightarrow
(2\times1)
\]

so the bias can be added.

## Common misconceptions

### Misconception 1. A vector's dimension and magnitude are the same thing

Dimension is the number of components. A vector's magnitude, or norm, is a scalar calculated from its component values. M02 treats these as distinct concepts.

### Misconception 2. In $m\times n$, $m$ is the number of columns

A matrix shape lists the number of rows first. Thus $m\times n$ means $m$ rows and $n$ columns.

### Misconception 3. Matrices can be added whenever they have the same number of entries

Shapes $2\times3$ and $3\times2$ each contain $6$ entries, but their corresponding row and column positions differ. Matrix addition requires the same shape.

### Misconception 4. A matrix product is an entrywise product

Matrix multiplication sums products between rows and columns. Deep-learning libraries implement entrywise multiplication and matrix multiplication with different operators.

### Misconception 5. Broadcasting in code means the shapes are mathematically equal

Broadcasting is an implementation rule that repeats values along specified axes. A mathematical expression should state the repetition or include an all-ones vector to make the resulting shape explicit.

## Exercises

### 1. Classifying objects

Identify each object as a scalar, vector, or matrix, and give its shape.

\[
c=-1
\]

\[
\mathbf v=
\begin{bmatrix}
2\\
3\\
4\\
5
\end{bmatrix}
\]

\[
\mathbf M=
\begin{bmatrix}
1&0\\
0&1\\
1&1
\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

$c$ is a scalar.

$\mathbf v$ is a vector of dimension $4$ and has shape $4\times1$ in column notation.

$\mathbf M$ is a matrix with $3$ rows and $2$ columns, so its shape is $3\times2$.

</details>

### 2. Reading matrix entries

Given

\[
\mathbf A=
\begin{bmatrix}
2&4&6\\
1&3&5
\end{bmatrix}
\]

find $a_{1,3}$ and $a_{2,1}$, and give the shape of $\mathbf A$.

<details>
<summary>Show solution</summary>

$a_{1,3}$ is the entry in row 1, column 3, so its value is $6$. $a_{2,1}$ is the entry in row 2, column 1, so its value is $1$.

$\mathbf A$ has 2 rows and 3 columns, so

\[
\mathbf A\in\mathbb R^{2\times3}
\]

</details>

### 3. Checking addition

Given

\[
\mathbf A\in\mathbb R^{2\times4},
\qquad
\mathbf B\in\mathbb R^{2\times4},
\qquad
\mathbf C\in\mathbb R^{4\times2}
\]

determine whether $\mathbf A+\mathbf B$ and $\mathbf A+\mathbf C$ can be calculated.

<details>
<summary>Show solution</summary>

$\mathbf A$ and $\mathbf B$ have the same shape, $2\times4$, so they can be added. The result also has shape $2\times4$.

$\mathbf A$ and $\mathbf C$ have shapes $2\times4$ and $4\times2$, respectively, so their shapes differ. Even though their entry counts are equal, their rows and columns are arranged differently, so they cannot be added.

</details>

### 4. Calculating an inner product

Given

\[
\mathbf x=
\begin{bmatrix}
1\\
2\\
3
\end{bmatrix},
\qquad
\mathbf y=
\begin{bmatrix}
4\\
-1\\
2
\end{bmatrix}
\]

calculate $\mathbf x^\top\mathbf y$ and identify the type of the result.

<details>
<summary>Show solution</summary>

\[
\mathbf x^\top\mathbf y
=
1\cdot4+2\cdot(-1)+3\cdot2
\]

\[
=4-2+6
=8
\]

The inner product of two vectors is a scalar.

</details>

### 5. A matrix–vector product

Given

\[
\mathbf A=
\begin{bmatrix}
1&2&0\\
-1&0&3
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}
2\\
1\\
4
\end{bmatrix}
\]

calculate $\mathbf A\mathbf x$.

<details>
<summary>Show solution</summary>

$\mathbf A$ has shape $2\times3$, and $\mathbf x$ has shape $3\times1$, so the result has shape $2\times1$.

\[
\mathbf A\mathbf x
=
\begin{bmatrix}
1\cdot2+2\cdot1+0\cdot4\\
-1\cdot2+0\cdot1+3\cdot4
\end{bmatrix}
\]

\[
=
\begin{bmatrix}
4\\
10
\end{bmatrix}
\]

</details>

### 6. Matrix-product shapes

Given

\[
\mathbf A\in\mathbb R^{5\times3},
\qquad
\mathbf B\in\mathbb R^{3\times7},
\qquad
\mathbf C\in\mathbb R^{4\times5}
\]

determine whether each product below can be calculated and give its output shape when it is defined.

\[
\mathbf A\mathbf B,\qquad
\mathbf C\mathbf A,\qquad
\mathbf B\mathbf A
\]

<details>
<summary>Show solution</summary>

The inner dimensions match in

\[
(5\times3)(3\times7)
\]

so $\mathbf A\mathbf B$ can be calculated, with output shape $5\times7$.

The inner dimensions also match in

\[
(4\times5)(5\times3)
\]

so $\mathbf C\mathbf A$ can be calculated, with output shape $4\times3$.

In

\[
(3\times7)(5\times3)
\]

the inner dimensions $7$ and $5$ differ, so $\mathbf B\mathbf A$ cannot be calculated.

</details>

### 7. Affine-layer shapes

The input dimension is $d_{\mathrm{in}}=6$, and the output dimension is $d_{\mathrm{out}}=4$. In the column-vector equation

\[
\mathbf y=\mathbf W\mathbf x+\mathbf b
\]

give the shapes of $\mathbf x$, $\mathbf W$, $\mathbf b$, and $\mathbf y$.

<details>
<summary>Show solution</summary>

\[
\mathbf x\in\mathbb R^6
\]

\[
\mathbf W\in\mathbb R^{4\times6}
\]

\[
\mathbf b\in\mathbb R^4
\]

\[
\mathbf y\in\mathbb R^4
\]

The shape of the matrix–vector product is

\[
(4\times6)(6\times1)
\longrightarrow
(4\times1)
\]

and the bias and output also have dimension $4$.

</details>

### 8. Transformer activation shapes

Suppose

\[
\mathbf H^{(\ell)}
\in
\mathbb R^{B\times T\times d_{\mathrm{model}}}
\]

with $B=8$, $T=128$, and $d_{\mathrm{model}}=512$.

1. What type of value is $h^{(\ell)}_{3,10,20}$?
2. Calculate the number of activation entries.
3. Explain the role of $\ell$.

<details>
<summary>Show solution</summary>

$h^{(\ell)}_{3,10,20}$ is a scalar activation that specifies a particular batch item, token position, and feature.

The number of entries is

\[
8\cdot128\cdot512=524{,}288
\]

$\ell$ is the index that distinguishes layers. The parenthesized superscript in $\mathbf H^{(\ell)}$ indicates the layer, not a power.

</details>

## Lesson summary

- A scalar is a single value, a vector has $n$ components, and a matrix has $m$ rows and $n$ columns.
- A matrix shape is written $m\times n$, with the row count followed by the column count.
- Addition requires the same shape; matrix multiplication requires matching inner dimensions.
- Under the column-vector convention, $\mathbf W\in\mathbb R^{d_{\mathrm{out}}\times d_{\mathrm{in}}}$.
- Each axis of a Transformer activation counts a different kind of object, such as batch items, tokens, or features.

## Pass criteria

You have passed this lesson if you can answer these questions without consulting the material:

- Can you distinguish scalars, vectors, and matrices by their notation?
- Can you identify the row and column counts in $m\times n$?
- Can you determine whether a matrix product is defined and calculate its output shape?
- Can you assign shapes to the input, weights, bias, and output of an affine layer?
- Can you explain each axis of $B\times T\times d_{\mathrm{model}}$?

## Next lesson

The next lesson is [M00-10. AI formula reading practice](M00-10-ai-equation-reading.md). You will use variables, functions, sums, logarithms, and shapes to read a loss function from beginning to end.

## Author checklist

- [x] The learning objectives describe observable actions.
- [x] All new symbols and shapes are defined before use.
- [x] The column-vector and batch-matrix conventions are distinguished.
- [x] The inner dimensions of matrix products have been checked.
- [x] The numerical affine-layer example has been checked.
- [x] Every exercise has a solution.
- [x] Broadcasting in implementations is distinguished from mathematical notation.
- [x] The glossary and notation rules are followed.
- [x] Internal links and mathematical delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
