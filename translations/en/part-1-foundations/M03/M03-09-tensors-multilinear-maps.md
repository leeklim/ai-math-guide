---
id: "M03-09"
title: "Tensors and multilinear maps"
part: 1
stage: "M03"
status: "complete"
prerequisites:
  - "M03-07"
  - "M03-08"
  - "M00-09"
estimated_time: "125~150 minutes"
---

# M03-09. Tensors and multilinear maps

## Why this lesson matters

Neural network code calls arrays with multiple axes tensors. Mathematics defines tensors through multilinear structures that can be interpreted as the same objects after a change of basis. A coordinate array stores tensor components, but its shape alone does not determine the input and output types or transformation law of a mathematical tensor.

Reading activations, attention scores, and higher derivatives requires tracking axis meanings and the indices being summed. A multilinear map is linear in each remaining input when the other inputs are fixed. This viewpoint connects matrix multiplication, bilinear scores, and tensor contraction through the same calculation rules.

## Learning objectives

After completing this lesson, you will be able to:

- Define a multilinear map through linearity in each input.
- Identify covectors and bilinear forms as tensors of low order.
- Construct tensor components in a basis and apply a small tensor to vectors.
- Distinguish tensor order, array shape, and matrix rank.
- Calculate the resulting shapes of tensor products and contractions.
- Track the roles of batch, token, and feature axes in neural network array operations.

## Prerequisite check

- Prerequisite lesson: [M03-07 Dual spaces and covectors](M03-07-dual-spaces-covectors.md)
- Prerequisite lesson: [M03-08 Bilinear forms and quadratic forms](M03-08-bilinear-quadratic-forms.md)
- Prerequisite lesson: [M00-09 Shapes of scalars, vectors, and matrices](../M00/M00-09-scalars-vectors-matrices-shape.md)
- Check: Can you distinguish the types of covectors and vectors?
- Check: Can you explain what it means for a bilinear map to be linear in each of its two inputs?
- Check: Can you identify the shared dimension in a matrix product?

Review the prerequisite lessons first if bilinear forms or shape tracking are unclear.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Type and shape |
|---|---|---|---|
| $T:V_1\times\cdots\times V_k\to\mathbb R$ | `T maps V one cross through V k to R` | A function linear in each input | A $k$-linear map |
| $\mathcal T$ | `calligraphic T` | A tensor object distinguished from its coordinates | Its type is specified in context |
| $T_{i_1\ldots i_k}$ | `T sub i one through i k` | Tensor components in the chosen basis | $k$ indices |
| $\alpha\otimes\beta$ | `alpha tensor beta` | An order-2 tensor constructed from two covectors | $(\alpha\otimes\beta)(\mathbf x,\mathbf y)=\alpha(\mathbf x)\beta(\mathbf y)$ |
| tensor order | `tensor order` | The number of vector or covector input slots of a tensor | Corresponds to the number of array axes in context |
| contraction | `contraction` | An operation reducing order by supplying an input or summing matching indices | Requires checking the resulting shape |

## Core concept 1. A multilinear map is linear in each input slot

Saying that

\[
T:V_1\times\cdots\times V_k\to\mathbb R
\]

is multilinear means that it is a linear function of each input separately when the other inputs are fixed.

In the $r$th input slot, it must satisfy

\[
T(\ldots,\alpha\mathbf u+\beta\mathbf v,\ldots)
=
\alpha T(\ldots,\mathbf u,\ldots)
+
\beta T(\ldots,\mathbf v,\ldots)
\]

For $k=1$, it is a covector; for $k=2$, a bilinear map; for $k=3$, a trilinear map taking three inputs. As in M03-08, the term bilinear form is used when both inputs belong to the same space.

A multilinear map with $k>1$ is generally not a linear function of one vector formed by grouping all inputs. Scaling every input by $\alpha$ gives

\[
T(\alpha\mathbf v_1,\ldots,\alpha\mathbf v_k)
=
\alpha^kT(\mathbf v_1,\ldots,\mathbf v_k)
\]

One scaling factor emerges each time linearity is applied to an input slot, so scaling all $k$ slots multiplies $k$ factors. Distinguish linearity when scaling one slot from the scaling obtained when changing all slots simultaneously.

Track the scaling of each slot separately starting from the value 72 in Example 1.

<figure class="lesson-figure" markdown="1">
  ![Three separate input slots each contribute one factor of two so output seventy two becomes one hundred forty four for one scaled slot and five hundred seventy six for all three](../../figures/assets/M03/M03-09-slot-scaling.svg)
  <figcaption>Doubling one slot gives 144, but doubling all three gives 2³×72=576. This difference could not occur for a single linear function of the three inputs grouped together.</figcaption>
</figure>

## Core concept 2. A tensor has a multilinear structure and a transformation law

A real-valued covariant tensor of order $k$ on a vector space $V$ can be defined as a multilinear map

\[
\mathcal T:V^k\to\mathbb R
\]

Here, $V^k$ means $V\times\cdots\times V$, taking $k$ vectors from $V$ in order. Expanding each input in a basis determines how tensor components are calculated.

- An order 0 tensor is a scalar.
- A covariant order 1 tensor is a covector.
- A covariant order 2 tensor is a bilinear form.

A vector is classified as a contravariant order 1 tensor. Fixing a vector $\mathbf v$ defines a linear measurement $\varphi\mapsto\varphi(\mathbf v)$ on covectors $\varphi$. From this perspective, vectors take covectors as inputs, whereas the covariant tensors above take vectors as inputs. More general tensors can combine vector and covector input slots. This lesson focuses on covariant tensors and coordinate arrays.

A tensor object is independent of the basis. Changing the basis changes its component array according to a specified law while preserving the scalar obtained by applying the tensor to vectors.

## Core concept 3. A basis expresses a tensor as a multiaxis component array

Let $\mathcal B=(\mathbf b_1,\ldots,\mathbf b_n)$ be a basis of $V$. Components of a covariant tensor of order $k$ are

\[
T_{i_1\ldots i_k}
=
\mathcal T(
\mathbf b_{i_1},\ldots,\mathbf b_{i_k}
)
\]

Writing each input vector as

\[
\mathbf v_r
=
\sum_{i_r=1}^{n}v_r^{i_r}\mathbf b_{i_r}
\]

and using multilinearity gives

\[
\mathcal T(\mathbf v_1,\ldots,\mathbf v_k)
=
\sum_{i_1=1}^{n}\cdots\sum_{i_k=1}^{n}
T_{i_1\ldots i_k}
v_1^{i_1}\cdots v_k^{i_k}
\]

For order 2,

\[
\mathcal T(\mathbf x,\mathbf y)
=
\sum_{i=1}^{n}\sum_{j=1}^{n}
T_{ij}x^iy^j
=
\mathbf x^\top\mathbf T\mathbf y
\]

giving the matrix representation of a bilinear form.

In the general evaluation formula, $v_r^{i_r}$ is the $i_r$th basis coefficient of the $r$th input vector, not a power. Expanding the first input as a linear combination produces a sum over $i_1$. Expanding the second input in each term produces a sum over $i_2$. Repeating this for every input slot sums over all combinations of one basis vector chosen per slot. Each combination contributes its tensor component multiplied by the $k$ chosen input coefficients.

If all input spaces are the same $n$-dimensional $V$, the component array has shape $n\times\cdots\times n$ and $n^k$ components. For different input spaces, each space's basis size determines its index range. Thus, shape $2\times3\times4$ can record a multilinear map on three input spaces of dimensions 2, 3, and 4.

## Core concept 4. Every tensor index participates in a change of basis

Covector components transform inversely to vector coordinates. A covariant tensor has several vector input slots; fixing all but one gives a covector acting on that slot. Each index therefore receives one transformation of its corresponding covector components.

For an order 2 bilinear form, the law from M03-08 is

\[
\mathbf T_{\mathcal C}
=
\mathbf P_{\mathcal B\leftarrow\mathcal C}^\top
\mathbf T_{\mathcal B}
\mathbf P_{\mathcal B\leftarrow\mathcal C}
\]

An order 3 tensor changes three input coordinates, so three transformation factors act on its components.

This can be checked directly with basis vectors. Write $\mathbf P=\mathbf P_{\mathcal B\leftarrow\mathcal C}$. The $a$th new basis vector is $\mathbf c_a=\sum_iP_{ia}\mathbf b_i$. For order 3, inserting three new basis vectors and applying linearity in each input gives

\[
(\mathbf T_{\mathcal C})_{abc}
=\sum_i\sum_j\sum_k
P_{ia}P_{jb}P_{kc}(\mathbf T_{\mathcal B})_{ijk}
\]

The arrays $\mathbf T_{\mathcal B}$ and $\mathbf T_{\mathcal C}$ contain the components in their respective bases. Expanding each input in the old basis adds one component of $\mathbf P$, giving three factors. This $\mathbf P$ maps new coordinates to old ones. It is therefore consistent that vector coordinates transform from old to new by $\mathbf P^{-1}$ while covector components transform in the opposite direction.

An array representing tensor components must follow this transformation law when the basis changes. One stored numerical array does not reveal which indices are vector-type or covector-type. The mathematical meaning of the axes must also be defined.

Each index is linked to the basis of one input slot. Transforming only one axis therefore generally does not produce the new components of the same tensor.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Each of three old component indices passes through its own basis change factor before the weighted sum yields one new component](../../figures/assets/M03/M03-09-three-index-basis-change.svg)
  <figcaption>For an order-3 covariant tensor, all three inputs are expanded in the new basis. Even one new component sums over all old indices i,j,k, with one basis-change coefficient from each slot.</figcaption>
</figure>

## Core concept 5. A tensor product combines input slots

The tensor product of two covectors $\alpha\in V^*$ and $\beta\in W^*$ is

\[
\alpha\otimes\beta:V\times W\to\mathbb R
\]

defined by

\[
(\alpha\otimes\beta)(\mathbf x,\mathbf y)
=
\alpha(\mathbf x)\beta(\mathbf y)
\]

It is linear in each input, making it an order-2 tensor.

When the first input changes, $\beta(\mathbf y)$ is a fixed scalar, so linearity of $\alpha$ gives linearity in the first slot. For the second slot, fix $\alpha(\mathbf x)$ and use linearity of $\beta$. Multiplying the two outputs thus retains linearity in each input separately.

Suppose $\dim V=m$ and $\dim W=n$, and choose a basis for each space. If the coordinate columns of $\alpha,\beta$ are $\mathbf a,\mathbf b$, respectively, the component matrix is

\[
\mathbf a\mathbf b^\top
\]

This is called the outer product. Its shape is

\[
\underbrace{\mathbf a}_{m\times1}
\underbrace{\mathbf b^\top}_{1\times n}
\in\mathbb R^{m\times n}
\]

Its components are $a_i b_j$ because $\alpha(\mathbf x)\beta(\mathbf y)=(\sum_i a_i x^i)(\sum_j b_j y^j)=\sum_i\sum_j a_i b_jx^iy^j$. Each column of one outer product is a scalar multiple of $\mathbf a$. If both $\mathbf a,\mathbf b$ are nonzero, the matrix has rank 1; if either is the zero vector, it is the zero matrix.

Summing outer products on the same input spaces can represent a general order-2 tensor. For standard unit coefficient vectors $\mathbf e_i,\mathbf e_j$, the matrix $\mathbf e_i\mathbf e_j^\top$ has 1 only in component $(i,j)$. Multiplying each such matrix by its component value and summing reconstructs any component matrix. Being representable as one outer product is therefore stronger than having order 2.

In an outer product, each row coefficient combines with each column coefficient to produce one component. The matrix in Example 2 shows both this relationship and its rank.

<figure class="lesson-figure" markdown="1">
  ![Outer product of column one two and row three minus one has its second row twice its first despite tensor order two](../../figures/assets/M03/M03-09-outer-product-grid.svg)
  <figcaption>Combining two input slots gives order 2. But the second row is twice the first, giving matrix rank 1. Order and matrix rank convey different information.</figcaption>
</figure>

## Core concept 6. Contraction supplies an input and sums an index

Inserting a vector $\mathbf z$ into the third input of an order-3 tensor with components $T_{ijk}$ gives

\[
S_{ij}
=
\sum_{k}T_{ijk}z^k
\]

The result is an order-2 tensor with two inputs remaining. This operation is a contraction over the third index.

For fixed $\mathbf z$, write $S(\mathbf x,\mathbf y)=\mathcal T(\mathbf x,\mathbf y,\mathbf z)$. Linearity of the original tensor in the first two slots remains, so $S$ is bilinear. Inserting basis vectors into those two slots and expanding only $\mathbf z$ gives the component equation for $S_{ij}$ above. The vector $\mathbf z$ must belong to the third input space; its basis coefficients are paired with the third index of $T$ in the sum.

Supplying all inputs gives the scalar

\[
\mathcal T(\mathbf x,\mathbf y,\mathbf z)
=
\sum_i\sum_j\sum_k
T_{ijk}x^iy^jz^k
\]

The matrix–vector product

\[
y_i=\sum_jA_{ij}x_j
\]

can also be read as contraction summing the shared index $j$. In implementations, notation such as einsum specifies which axes are summed and which remain.

In Example 3, supplying the third input forms a weighted sum of two $k$ slices. The first and second input slots still remain afterward.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Third index slices with entries one and two weighted by four and five produce a remaining matrix with entries four and ten](../../figures/assets/M03/M03-09-component-contraction.svg)
  <figcaption>Fixing w₁=4,w₂=5 multiplies the k=1 slice by 4 and the k=2 slice by 5 before adding them. The k index disappears, while i,j remain to form matrix [[4,0],[10,0]].</figcaption>
</figure>

## Core concept 7. Order, shape, and rank convey different information

Distinguish the following terms.

| Term | Question it answers | Example |
|---|---|---|
| tensor order | How many multilinear input slots are there? | $T_{ijk}$ has order 3 |
| Number of array axes | How many indices does the stored array have? | Shape $2\times3\times4$ has 3 axes |
| Dimension of each axis | How many values can each index take? | 2, 3, 4 |
| Matrix rank | How many independent row or column directions are there? | Calculated for an order-2 array |
| Tensor rank | How many rank-1 tensors are needed in a sum? | Requires a separate definition and calculation method |

A matrix is an order-2 array, but this does not mean its matrix rank is 2. Nor is the rank of an order-3 tensor equal to its number of axes, 3.

## Core concept 8. Machine learning tensors are multiaxis arrays with meaningful axes

Neural network implementations call multiaxis arrays tensors, including scalars, vectors, and matrices. For example, a Transformer activation can be stored as

\[
\mathbf H^{(\ell)}
\in
\mathbb R^{B\times T\times d_{\mathrm{model}}}
\]

- The first axis is batch.
- The second is token position.
- The third is feature coordinates.

Having three axes does not establish that this array is a covariant order-3 tensor mathematically. Batch and token axes may index samples, while only the feature axis may be subject to changes of basis.

For example, fix the batch and token and write the feature coordinates as a column vector $\mathbf h_{bt}\in\mathbb R^{d_{\mathrm{model}}}$. If $\mathbf P$ is the basis matrix assembling old feature coordinates from new coordinates, the new coordinates of the same representation vector are $\widetilde{\mathbf h}_{bt}=\mathbf P^{-1}\mathbf h_{bt}$. This applies the same feature coordinate change to each $(b,t)$. It does not change bases for the batch or token lists themselves and therefore differs from attaching covariant transformation factors to all three axes.

When reading array operations, first check shape and axis meanings. A coordinate-independent claim must also specify which changes of basis act on which axes.

In the array below, choosing a batch and token selects one feature vector. A feature change of basis acts on its coordinates; it does not turn the batch or token itself into a basis vector.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Two batch panels each contain three token rows and four feature columns distinguishing selection axes from feature coordinates](../../figures/assets/M03/M03-09-ml-array-axes.svg)
  <figcaption>Even for the same 2×3×4 shape, the axes have different roles. The hᵢⱼ notation denotes feature coordinate j of token i within each batch, not actual model measurements.</figcaption>
</figure>

## Example 1. Evaluating an order-3 tensor

### Problem

On $V=\mathbb R^2$, define the trilinear form

\[
\mathcal T(\mathbf u,\mathbf v,\mathbf w)
=
u_1v_1w_1+2u_2v_1w_2
\]

Calculate its value for

\[
\mathbf u=
\begin{bmatrix}1\\2\end{bmatrix},
\quad
\mathbf v=
\begin{bmatrix}3\\-1\end{bmatrix},
\quad
\mathbf w=
\begin{bmatrix}4\\5\end{bmatrix}
\]

### Solution

Substitution into the definition gives

\[
\mathcal T(\mathbf u,\mathbf v,\mathbf w)
=
1\cdot3\cdot4
+
2\cdot2\cdot3\cdot5
\]

\[
=
12+60
=
72
\]

The only components other than 0 are

\[
T_{111}=1,
\qquad
T_{212}=2
\]

### Meaning of the result

The component array has shape $2\times2\times2$, but only two components are nonzero. Fixing one of the three inputs gives a bilinear map on the remaining inputs.

## Example 2. Tensor product and outer product

### Problem

Suppose two covectors have standard-basis coordinates

\[
\mathbf a=
\begin{bmatrix}1\\2\end{bmatrix},
\qquad
\mathbf b=
\begin{bmatrix}3\\-1\end{bmatrix}
\]

Calculate the component matrix of $\alpha\otimes\beta$ and evaluate it at

\[
\mathbf x=
\begin{bmatrix}1\\1\end{bmatrix},
\qquad
\mathbf y=
\begin{bmatrix}2\\-1\end{bmatrix}
\]

### Solution

The component matrix is the outer product

\[
\mathbf a\mathbf b^\top
=
\begin{bmatrix}
1\\2
\end{bmatrix}
\begin{bmatrix}
3&-1
\end{bmatrix}
=
\begin{bmatrix}
3&-1\\
6&-2
\end{bmatrix}
\]

We have

\[
\alpha(\mathbf x)
=
\begin{bmatrix}1&2\end{bmatrix}
\begin{bmatrix}1\\1\end{bmatrix}
=
3
\]

and

\[
\beta(\mathbf y)
=
\begin{bmatrix}3&-1\end{bmatrix}
\begin{bmatrix}2\\-1\end{bmatrix}
=
7
\]

so

\[
(\alpha\otimes\beta)(\mathbf x,\mathbf y)
=
3\cdot7
=
21
\]

The matrix expression also gives

\[
\mathbf x^\top
\begin{bmatrix}
3&-1\\
6&-2
\end{bmatrix}
\mathbf y
=
21
\]

### Meaning of the result

A tensor product multiplies two linear measurements to form a bilinear form taking two inputs.

## Example 3. Contracting one index

Insert $\mathbf w=(4,5)^\top$ into the third input of the tensor in Example 1.

\[
S_{ij}
=
\sum_{k=1}^{2}T_{ijk}w^k
\]

Using the components other than 0,

\[
S_{11}=T_{111}w^1=4
\]

\[
S_{21}=T_{212}w^2=10
\]

The remaining components are 0, so

\[
\mathbf S=
\begin{bmatrix}
4&0\\
10&0
\end{bmatrix}
\]

Evaluating on the remaining two inputs recovers the full value:

\[
\mathbf u^\top\mathbf S\mathbf v
=
\begin{bmatrix}1&2\end{bmatrix}
\begin{bmatrix}
4&0\\
10&0
\end{bmatrix}
\begin{bmatrix}3\\-1\end{bmatrix}
=
72
\]

## Example 4. The two contractions in attention

Omitting batch and head dimensions, let

\[
\mathbf Q,\mathbf K\in\mathbb R^{T\times d_k},
\qquad
\mathbf V\in\mathbb R^{T\times d_v}
\]

The score matrix has components

\[
S_{ts}
=
\sum_{i=1}^{d_k}Q_{ti}K_{si}
\]

Contracting the feature index $i$ gives $\mathbf S\in\mathbb R^{T\times T}$.

Given attention weights $\mathbf A\in\mathbb R^{T\times T}$, the output components are

\[
O_{tj}
=
\sum_{s=1}^{T}A_{ts}V_{sj}
\]

Contracting the token index $s$ gives

\[
\mathbf O\in\mathbb R^{T\times d_v}
\]

Distinguishing summed axes from remaining axes in each equation verifies the matrix product's shape.

The two contractions sum different axes. The small numerical arrays below illustrate this distinction.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Query and key feature coordinates are summed for each token pair to form a two by two score matrix](../../figures/assets/M03/M03-09-attention-score-contraction.svg)
  <figcaption>Forming scores multiplies and sums matching feature indices i. The remaining indices t,s denote query and key tokens, respectively, giving a token–token matrix.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Each output row is a weighted sum of two value rows with the source token index summed out](../../figures/assets/M03/M03-09-attention-value-contraction.svg)
  <figcaption>Combining values sums over source token index s. The second feature of the first output is 0.75×0+0.25×2=0.5. Query token t and feature j remain in the output.</figcaption>
</figure>

## Common misconceptions

### Misconception 1. Every three-axis array is the same type of mathematical order-3 tensor

Array shape describes storage structure. Defining a mathematical tensor's type requires stating which space each axis belongs to and how its components transform under changes of basis.

### Misconception 2. Tensor order and tensor rank are the same

Order counts input slots or indices. Tensor rank concerns representation as a sum of rank-1 tensors and has a separate definition.

### Misconception 3. A multilinear map is linear in all inputs grouped together

Multilinearity means linearity in each input while the others are fixed. Scaling all inputs by the same scalar yields a scaling factor raised to the order $k$.

### Misconception 4. Contraction arbitrarily adds array elements

Contraction pairs and sums indices from corresponding spaces. Specify which axes are summed and which remain.

### Misconception 5. Activation tensors with the same shape represent the same thing

Shape gives only axis sizes. Component values, feature bases, sample correspondence, and functional use by the model are separate information.

## Exercises

### 1. Testing multilinearity

Determine whether

\[
T(\mathbf u,\mathbf v,\mathbf w)=u_1v_2w_1
\]

is multilinear in its three inputs from $\mathbb R^2$.

<details>
<summary>Show solution</summary>

Fixing the other two inputs gives a function multiplying one coordinate of the remaining input by a fixed scalar. It preserves addition and scalar multiplication in each input, so it is trilinear.

</details>

### 2. Calculating a trilinear value

Given

\[
T(\mathbf u,\mathbf v,\mathbf w)=u_1v_1w_2+u_2v_2w_1
\]

and

\[
\mathbf u=
\begin{bmatrix}1\\2\end{bmatrix},
\quad
\mathbf v=
\begin{bmatrix}3\\4\end{bmatrix},
\quad
\mathbf w=
\begin{bmatrix}5\\6\end{bmatrix}
\]

calculate $T(\mathbf u,\mathbf v,\mathbf w)$.

<details>
<summary>Show solution</summary>

\[
T(\mathbf u,\mathbf v,\mathbf w)
=
1\cdot3\cdot6+2\cdot4\cdot5
=
18+40
=
58
\]

</details>

### 3. Order and component count

The index ranges of $T_{ijk}$ have sizes 2, 3, and 4, respectively. Calculate the array shape, order, and total component count.

<details>
<summary>Show solution</summary>

The shape is $2\times3\times4$. There are three indices, so the order is 3. The total number of components is

\[
2\cdot3\cdot4=24
\]

Order 3 does not mean the component count is 3 or the tensor rank is 3.

</details>

### 4. Outer product

For

\[
\mathbf a=
\begin{bmatrix}2\\-1\end{bmatrix},
\qquad
\mathbf b=
\begin{bmatrix}3\\0\\4\end{bmatrix}
\]

calculate the shape and entries of $\mathbf a\mathbf b^\top$.

<details>
<summary>Show solution</summary>

The shape is $(2\times1)(1\times3)=2\times3$.

\[
\mathbf a\mathbf b^\top
=
\begin{bmatrix}
2\\-1
\end{bmatrix}
\begin{bmatrix}
3&0&4
\end{bmatrix}
=
\begin{bmatrix}
6&0&8\\
-3&0&-4
\end{bmatrix}
\]

</details>

### 5. Contraction shape

Given $T_{ijk}$ of shape $2\times3\times4$ and $\mathbf z\in\mathbb R^4$, calculate the shape and order of

\[
S_{ij}=\sum_{k=1}^{4}T_{ijk}z_k
\]

<details>
<summary>Show solution</summary>

Summation removes index $k$ and leaves $i,j$. Thus, $\mathbf S$ has shape $2\times3$ and order 2.

</details>

### 6. Tracking attention shapes

For

\[
\mathbf Q,\mathbf K\in\mathbb R^{5\times3},
\qquad
\mathbf V\in\mathbb R^{5\times4}
\]

calculate the shapes of $\mathbf Q\mathbf K^\top$ and $\mathbf A\mathbf V$. The matrix $\mathbf A$ is obtained by applying softmax to the scores.

<details>
<summary>Show solution</summary>

\[
(5\times3)(3\times5)=5\times5
\]

so $\mathbf Q\mathbf K^\top$ has shape $5\times5$. Thus, $\mathbf A\in\mathbb R^{5\times5}$, and

\[
(5\times5)(5\times4)=5\times4
\]

so $\mathbf A\mathbf V$ has shape $5\times4$.

</details>

### 7. Critiquing a model claim

Critique the statement: “Both models' activation tensors have shape $B\times T\times d$, so the models learned the same tensor representation.”

<details>
<summary>Show solution</summary>

Equal shapes show only that the batch, token, and feature axis sizes agree. They do not verify activation values, sample correspondence, feature bases, allowed alignments, information recovery, or functional use by the model. A claim of identical representations requires separate comparison criteria and transformation invariances.

</details>

## Lesson summary

- A multilinear map is separately linear in each input slot.
- A covariant tensor of order $k$ can be viewed as a multilinear map from $k$ vectors to a scalar.
- Choosing a basis represents a tensor as a multiaxis component array, with every index participating in changes of basis.
- A tensor product combines input slots; contraction sums indices to reduce order.
- Tensor order, array shape, matrix rank, and tensor rank convey different information.
- Interpreting a machine learning tensor requires stating the meaning of each axis and which axes are contracted.

## Pass criteria

You pass if you can answer the following without referring to the material:

- Can you explain linearity in each input of a multilinear map?
- Can you connect covectors and bilinear forms to tensor order?
- Can you calculate a small multilinear value from tensor components?
- Can you determine the resulting shapes of tensor products and contractions?
- Can you distinguish tensor order, the number of array axes, and rank?
- Can you identify summed and remaining axes in attention equations?
- Can you explain why array shape alone does not establish representation equality?

## Next lesson

- [M03-10 Total derivative and differential](M03-10-total-derivative-differential.md)

## Author checklist

- [x] Learning objectives are expressed as observable actions.
- [x] Multilinearity is defined separately for each input.
- [x] Tensor objects are distinguished from component arrays.
- [x] Tensor order, shape, and rank are distinguished.
- [x] Tensor products and contractions are calculated.
- [x] Neural network array axes are distinguished from mathematical tensor types.
- [x] Every exercise has a solution.
- [x] The strengths of model interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
