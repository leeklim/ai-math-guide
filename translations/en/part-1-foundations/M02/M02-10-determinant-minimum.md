---
id: "M02-10"
title: "A minimal understanding of determinants"
part: 1
stage: "M02"
status: "complete"
prerequisites:
  - "M02-05"
  - "M02-06"
  - "M02-08"
estimated_time: "90~115 minutes"
---

# M02-10. A minimal understanding of determinants

## Why this lesson matters

A determinant is a scalar describing how a square matrix scales volume. A value of 0 means that a dimension collapses, preventing an inverse transformation. The sign records whether the orientation of the space is reversed.

Model interpretation does not often require computing determinants directly. Their meaning is nevertheless needed to read about invertibility, characteristic equations for eigenvalues, and local volume changes under a Jacobian. For a large matrix, one determinant alone must not be used to judge numerical stability or importance to a model.

## Learning objectives

By the end of this lesson, you should be able to:

- Compute a $2\times2$ determinant.
- Explain its absolute value as an area or volume factor.
- Connect the sign to orientation reversal.
- Connect a determinant of 0 to invertibility and rank.
- Compute changes in determinants under products, inverses, and elementary row operations.
- Explain why determinant magnitude alone does not establish numerical stability or model function.

## Prerequisite check

- Prerequisite lesson: [M02-05 Matrices as linear transformations](M02-05-matrix-as-linear-transformation.md)
- Prerequisite lesson: [M02-06 Linear systems and inverse matrices](M02-06-linear-systems-inverse.md)
- Prerequisite lesson: [M02-08 Kernel, image, and rank](M02-08-kernel-image-rank.md)
- Check question: Can you relate invertible matrices, singular matrices, and full-rank square matrices?
- Check question: Can you draw the parallelogram formed by the columns of a matrix?

Review the prerequisite lessons first if invertibility or rank is unclear.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| $\det(\mathbf A)$ | `the determinant of A` | The oriented volume factor of a square matrix | Scalar |
| $\lvert\det(\mathbf A)\rvert$ | `the absolute value of the determinant of A` | The volume factor without its sign | At least 0 |
| Orientation | `orientation` | Whether the ordered basis axes have right-handed or left-handed orientation | Related to the determinant sign |
| Triangular matrix | `triangular matrix` | A square matrix with all entries on one side of the diagonal equal to 0 | Its determinant is the product of the diagonal entries. |

## Core concept 1. A $2\times2$ determinant is the difference of the two diagonal products

For

\[
\mathbf A=
\begin{bmatrix}
a&b\\
c&d
\end{bmatrix}
\]

the determinant is

\[
\det(\mathbf A)
=
ad-bc
\]

This is the oriented area of the parallelogram formed by the two columns of $\mathbf A$. Its geometric area is

\[
|\det(\mathbf A)|
\]

Taking the columns $\mathbf u=(a,c)^\top$, $\mathbf v=(b,d)^\top$ as edges connects the formula to base times height. For $\mathbf u\ne\mathbf 0$, the base length is $\sqrt{a^2+c^2}$. One unit vector perpendicular to $\mathbf u$ is

\[
\frac{1}{\sqrt{a^2+c^2}}
\begin{bmatrix}-c\\a\end{bmatrix}
\]

Its inner product with $\mathbf v$ is $(ad-bc)/\sqrt{a^2+c^2}$. The absolute value is the length of the second edge's perpendicular component, namely the height. Multiplying base and height cancels $\sqrt{a^2+c^2}$ and gives $|ad-bc|$. If the first column is the zero vector, both the base and area are 0, and the formula also gives 0.

## Core concept 2. The absolute determinant is a volume factor

A square matrix $\mathbf A\in\mathbb R^{n\times n}$ transforms the unit cube into a parallelotope. The resulting $n$-dimensional volume is

\[
|\det(\mathbf A)|
\]

times the original volume. In 2 dimensions, a point in the unit square is $s\mathbf e_1+t\mathbf e_2$, with $s,t$ between 0 and 1. If the columns are $\mathbf a_1,\mathbf a_2$, the transformed point is $s\mathbf a_1+t\mathbf a_2$. These points fill the parallelogram with the two columns as edges. Since the original area is 1, the transformed area $|\det(\mathbf A)|$ is also the area factor. In higher dimensions, the same relation is read from the volume of the shape with the columns as edges.

This factor is not restricted to unit shapes. A shape's volume after the same linear transformation is its original volume times $|\det(\mathbf A)|$. The volume factor of a linear transformation does not vary with position.

- If $|\det(\mathbf A)|>1$, volume increases.
- If $0<|\det(\mathbf A)|<1$, volume decreases.
- If $\det(\mathbf A)=0$, volume becomes 0 as the shape collapses into a lower dimension.

The determinant summarizes one total volume factor. It does not separately show the expansion or contraction of each direction.

The figure below uses the two columns in Example 1 as edges and compares the unit square before and after transformation. A height perpendicular to the base connects the area to the absolute determinant.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Equal-scale grids showing a unit square transformed into a parallelogram with base three, height two, and area six](../../figures/assets/M02/M02-10-unit-square-area.svg)

<figcaption>The first column (3,0) forms the base, and the second (1,2) forms the slanted edge. The height is the perpendicular component 2, not the length of the second edge. The area is 3×2=6, also a factor of 6 relative to the original area 1.</figcaption>
</figure>

## Core concept 3. The sign records orientation reversal

If $\det(\mathbf A)>0$, the transformation preserves the basis orientation; if $\det(\mathbf A)<0$, it reverses it.

In 2 dimensions, interpret this using the ordered pair of columns. The standard basis turns counterclockwise from $\mathbf e_1$ to $\mathbf e_2$. For two independent columns, a counterclockwise shorter turn from the first column to the second gives a positive determinant; a clockwise turn gives a negative one. Swapping the columns reverses the turn and changes the determinant's sign.

Orientation is different from the direction in which one vector points. Rotating both vectors together can preserve their orientation. When the determinant is 0, the columns do not form independent directions, so the sign does not distinguish preservation from reversal.

For example, the reflection across the $x$ axis,

\[
\mathbf R=
\begin{bmatrix}
1&0\\
0&-1
\end{bmatrix}
\]

satisfies

\[
\det(\mathbf R)=-1
\]

It preserves area but reverses orientation once.

A $90^\circ$ rotation has determinant 1, preserving both area and orientation.

The figure below marks the order from the first basis direction to the second. Rotation moves both directions together; reflection reverses their orientation.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Ordered basis images under identity, ninety-degree rotation, and reflection showing preserved or reversed orientation](../../figures/assets/M02/M02-10-orientation-order.svg)

<figcaption>The identity and a 90-degree rotation preserve the counterclockwise order from the first direction to the second. Reflection across the x axis makes that order clockwise. The area stays the same, but the determinant becomes negative.</figcaption>
</figure>

## Core concept 4. A determinant of 0 means loss of invertibility

For a square matrix $\mathbf A\in\mathbb R^{n\times n}$, the following conditions are equivalent.

\[
\det(\mathbf A)\ne0
\]

\[
\mathbf A\text{ is invertible}
\]

\[
\operatorname{rank}(\mathbf A)=n
\]

\[
\ker(\mathbf A)=\{\mathbf 0\}
\]

The $n$ independent columns form a shape with $n$-dimensional volume. Dependent columns place every edge in a lower-dimensional subspace, making the $n$-dimensional volume 0. Length or area can remain within that lower-dimensional space without any $n$-dimensional volume remaining.

Collecting the coefficient vector, which is not 0, of a column dependence into $\mathbf z$ gives $\mathbf A\mathbf z=\mathbf 0$. Thus the kernel contains an input direction other than 0. As M02-08 showed, different inputs separated along this direction reach the same output, preventing an inverse. Conversely, independent columns give rank $n$ and invertibility. Loss of volume and failure to distinguish inputs express the same column dependence.

The figure below shows all four square vertices in Example 2 mapping onto one line. Retaining a segment is different from retaining 2-dimensional area.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A unit square whose four transformed corners all lie on a single line under a rank-one matrix](../../figures/assets/M02/M02-10-area-collapse.svg)

<figcaption>The columns are multiples of the same direction, so their edges do not span an independent area. Length remains after transformation, but area is 0, corresponding to deficient rank and no inverse.</figcaption>
</figure>

## Core concept 5. Volume factors multiply under composition

For square matrices of the same size,

\[
\det(\mathbf A\mathbf B)
=
\det(\mathbf A)\det(\mathbf B)
\]

$\mathbf A\mathbf B$ applies $\mathbf B$ first. Ordinary volume is multiplied by $|\det(\mathbf B)|$ and then by $|\det(\mathbf A)|$. Signed determinants multiply the factors including orientation. If only one transformation reverses orientation, the composition reverses it; if both do, orientation is preserved, as with the product of two negative numbers. If either determinant is 0, the total volume is 0.

For invertible $\mathbf A$,

\[
\det(\mathbf A^{-1})
=
\frac{1}{\det(\mathbf A)}
\]

Indeed,

\[
1
=
\det(\mathbf I)
=
\det(\mathbf A\mathbf A^{-1})
=
\det(\mathbf A)\det(\mathbf A^{-1})
\]

The figure below applies horizontal and vertical scaling in succession using the same coordinate scale. The two stages' area factors multiply; they do not add.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A unit square scaled horizontally by two and then vertically by three, with successive areas one, two, and six](../../figures/assets/M02/M02-10-composed-area-scales.svg)

<figcaption>Scaling horizontally by 2 and then vertically by 3 changes area as 1→2→6. The total determinant is 3×2, and the inverse multiplies the total area by 1/6 to restore its original size.</figcaption>
</figure>

## Core concept 6. Track the effects of elementary row operations

Elementary row operations on a square matrix change its determinant as follows.

1. Swapping two rows changes the sign.
2. Multiplying one row by a scalar $c$ other than 0 multiplies the determinant by $c$.
3. Adding a scalar multiple of another row leaves the determinant unchanged.

A row operation can also be read as an elementary transformation of output coordinates. Swapping rows swaps output axes; scaling a row scales one output coordinate. Adding a multiple of another row is a shear that shifts one coordinate according to another and preserves volume. All three operations were reversible in M02-06, but not all preserve the determinant value.

These rules allow determinant computation by reducing the matrix to triangular form. For a triangular matrix,

\[
\det(\mathbf U)
=
\prod_{i=1}^{n}u_{ii}
\]

In a $2\times2$ upper-triangular matrix, $c=0$, so $ad-bc=ad$ leaves only the product of diagonal entries. Higher-dimensional triangular matrices also use the diagonal product. Whether the determinant of the triangular matrix $\mathbf U$ produced by elimination equals the original determinant depends on the row-operation record.

If there are $s$ row swaps and the product of all nonzero row-scaling factors is $p$, then

\[
\det(\mathbf U)=(-1)^s p\det(\mathbf A)
\]

With no row scaling, $p=1$. To recover the original determinant, divide $\det(\mathbf U)$ by $(-1)^s p$, undoing the row-operation effects. The number of additions of multiples of other rows does not affect this factor.

The figure below applies the three elementary operations separately to the identity matrix. Although all are invertible, their effects on area and orientation differ.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Transformed unit squares under row swap, row scaling, and row addition with determinant multipliers minus one, two, and one](../../figures/assets/M02/M02-10-row-operation-shapes.svg)

<figcaption>A row swap reverses axis order and changes the sign; scaling one row by 2 scales area by 2. A shear that adds one row to another tilts the shape while preserving area and orientation.</figcaption>
</figure>

## Core concept 7. One determinant does not show directional sensitivity

For

\[
\mathbf A=
\begin{bmatrix}
1000&0\\
0&0.001
\end{bmatrix}
\]

we have

\[
\det(\mathbf A)=1
\]

Area is preserved, but the first direction expands by 1000 and the second contracts to 1/1000 of its length. The inverse can greatly amplify small errors in the second output direction.

Thus $|\det(\mathbf A)|$ being close to 1 does not guarantee numerical stability. Singular values and condition numbers describe directional amplification; M02-13 and M02-15 cover them.

The figure below uses milder factors of 10 and 0.1 to make the effect distinguishable on screen. The same relation between area preservation and different directional factors holds for the 1000 and 0.001 factors in the text.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A unit square and a ten-by-one-tenth thin rectangle with equal area but different directional scales](../../figures/assets/M02/M02-10-same-area-different-scales.svg)

<figcaption>On the same coordinate scale, a thin rectangle of width 10 and height 0.1 also has area 1. Total area alone does not reveal expansion in one direction and contraction in the other.</figcaption>
</figure>

## Example 1. Computing an area factor

For

\[
\mathbf A=
\begin{bmatrix}
3&1\\
0&2
\end{bmatrix}
\]

we have

\[
\det(\mathbf A)
=
3\cdot2-1\cdot0
=
6
\]

The unit square maps to a parallelogram of area 6. The positive sign means orientation is preserved.

## Example 2. A collapsing transformation

For

\[
\mathbf B=
\begin{bmatrix}
1&2\\
2&4
\end{bmatrix}
\]

we have

\[
\det(\mathbf B)
=
1\cdot4-2\cdot2
=
0
\]

The second column is 2 times the first, so two independent directions collapse onto one line. The rank is 1, and there is no inverse.

## Example 3. The determinant of a composition

For

\[
\mathbf A=
\begin{bmatrix}
2&0\\
0&3
\end{bmatrix},
\qquad
\mathbf R=
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}
\]

we have

\[
\det(\mathbf A)=6,
\qquad
\det(\mathbf R)=1
\]

Therefore,

\[
\det(\mathbf A\mathbf R)=6
\]

Rotation first preserves area, and subsequent scaling along the two axes multiplies it by 6.

## Example 4. A preview of the Jacobian determinant

A nonlinear function $f:\mathbb R^n\to\mathbb R^n$ can also be approximated linearly near a point using its Jacobian $\mathbf J_f(\mathbf x)$. Then

\[
|\det(\mathbf J_f(\mathbf x))|
\]

describes how a small volume near that point changes.

This concerns local volume change, not whether the function learned a particular concept or whether a coordinate causes behavior. M03-11 computes Jacobians.

## Common misconceptions

### Misconception 1. A determinant is defined for every matrix

This lesson defines determinants only for square matrices. Singular values analyze size changes under rectangular matrices.

### Misconception 2. A negative determinant means negative volume

Geometric volume uses $|\det(\mathbf A)|$. A negative sign records orientation reversal.

### Misconception 3. A small determinant means low rank

Only an exactly 0 determinant establishes deficient rank. A small value other than 0 means invertibility, though sensitivity can be high in particular directions.

### Misconception 4. A larger absolute determinant means a matrix is more important to the model

The determinant is a total volume factor. Model performance, feature meaning, and causal contribution are not determined by this one scalar.

## Exercises

### 1. A $2\times2$ calculation

Find the determinant of

\[
\mathbf A=
\begin{bmatrix}
4&-1\\
2&3
\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

\[
\det(\mathbf A)
=
4\cdot3-(-1)\cdot2
=
14
\]

</details>

### 2. Area and orientation

A $2\times2$ matrix with $\det(\mathbf B)=-5$ acts on a shape of area 3. Explain the transformed area and the change in orientation.

<details>
<summary>Show solution</summary>

Area is scaled by the absolute determinant:

\[
3\cdot|-5|=15
\]

The determinant is negative, so orientation is reversed.

</details>

### 3. Testing invertibility

Use the determinant to determine whether

\[
\mathbf C=
\begin{bmatrix}
2&6\\
1&3
\end{bmatrix}
\]

is invertible, and find its rank.

<details>
<summary>Show solution</summary>

\[
\det(\mathbf C)
=
2\cdot3-6\cdot1
=
0
\]

It is therefore not invertible. The second column is 3 times the first, so its rank is 1.

</details>

### 4. A triangular matrix

Find the determinant of

\[
\mathbf U=
\begin{bmatrix}
2&1&4\\
0&-3&5\\
0&0&6
\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

The determinant of a triangular matrix is the diagonal product:

\[
\det(\mathbf U)
=
2(-3)6
=
-36
\]

</details>

### 5. Elementary row operations

Suppose $\det(\mathbf A)=7$. Find the determinant after each operation.

1. Swap the first and second rows.
2. Multiply the first row by 4.
3. Add 3 times the first row to the second.

Apply each operation separately to the original $\mathbf A$.

<details>
<summary>Show solution</summary>

A row swap changes the sign, giving $-7$. Multiplying a row by 4 multiplies the determinant by 4, giving $28$. Adding a multiple of another row leaves the determinant unchanged, giving $7$.

</details>

### 6. The determinant of an inverse

For an invertible matrix with $\det(\mathbf A)=\frac14$, find $\det(\mathbf A^{-1})$.

<details>
<summary>Show solution</summary>

\[
\det(\mathbf A^{-1})
=
\frac{1}{\det(\mathbf A)}
=
4
\]

The inverse undoes the volume factor of the original transformation.

</details>

### 7. Critiquing a stability claim

Compute the determinant of

\[
\mathbf D=
\begin{bmatrix}
10^6&0\\
0&10^{-6}
\end{bmatrix}
\]

and determine whether that value alone establishes numerical stability.

<details>
<summary>Show solution</summary>

\[
\det(\mathbf D)
=
10^6\cdot10^{-6}
=
1
\]

Total area is preserved.

The first direction expands by $10^6$, and the second contracts by $10^{-6}$. The directional factors differ greatly, so determinant 1 does not establish stability. Check singular values and the condition number.

</details>

## Lesson summary

- A $2\times2$ determinant is $ad-bc$; the determinant of a square matrix is its oriented volume factor.
- Its absolute value gives the volume factor, and its sign records orientation preservation or reversal.
- A square matrix with determinant 0 has deficient rank and no inverse.
- The determinant of a composition is the product of the determinants.
- Elementary row operations and triangular-matrix properties allow determinant computation.
- One determinant does not show directional amplification, numerical stability, or functional importance to a model.

## Pass criteria

You pass if you can answer these questions without consulting the material.

- Can you compute a $2\times2$ determinant?
- Can you explain its absolute value and sign geometrically?
- Can you connect determinant 0 to invertibility and rank?
- Can you compute determinants of products and inverses?
- Can you explain how elementary row operations affect the determinant?
- Can you give an example showing why the determinant is insufficient as a stability measure?

## Next lesson

- [M02-11 Eigenvalues and eigenvectors](M02-11-eigenvalues-eigenvectors.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] The $2\times2$ formula is connected to volume scaling.
- [x] The relations among sign, invertibility, rank, and kernel are explained.
- [x] Product and elementary-row-operation properties are included.
- [x] A counterexample with hidden directional amplification is given.
- [x] Every exercise has a solution.
- [x] Determinants are distinguished from claims about model function.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
