---
id: "M02-15"
title: "Norms and condition numbers"
part: 1
stage: "M02"
status: "complete"
prerequisites:
  - "M02-06"
  - "M02-13"
  - "M02-14"
estimated_time: "120~145 minutes"
---

# M02-15. Norms and condition numbers

## Why this lesson matters

Describing vector or matrix size requires specifying a norm. The same vector has different values under the L1, Euclidean, and maximum norms. For matrices, distinguish the overall size of the entries from the largest possible amplification of an input.

A condition number describes how much input error in an invertible linear system can be amplified in its solution. Even with a nonzero determinant, a large condition number allows small measurement and rounding errors to substantially change the solution.

## Learning objectives

After completing this lesson, you will be able to:

- Calculate L1, L2, and infinity norms and explain their differences.
- Connect Frobenius and spectral norms to singular values.
- Bound $\|\mathbf A\mathbf x\|_2$ using a matrix norm.
- Calculate the 2-norm condition number of an invertible square matrix.
- Explain relative error amplification bounds using condition numbers.
- Distinguish the questions answered by rank, determinant, norm, and condition number.

## Prerequisite check

- Prerequisite lesson: [M02-06 Linear systems and inverses](M02-06-linear-systems-inverse.md)
- Prerequisite lesson: [M02-13 Singular value decomposition](M02-13-singular-value-decomposition.md)
- Prerequisite lesson: [M02-14 Covariance and PCA](M02-14-covariance-pca.md)
- Check question: Can you explain an invertible matrix's inverse and the solution of a linear system?
- Check question: Can you explain how the largest and smallest singular values describe directional amplification?

If inverses or SVD are unclear, first review the prerequisite lessons.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| $\|\mathbf x\|_1$ | `the L one norm of x` | Sum of absolute component values | L1 norm |
| $\|\mathbf x\|_2$ | `the L two norm of x` | Square root of the sum of squared components | Euclidean norm |
| $\|\mathbf x\|_\infty$ | `the L infinity norm of x` | Largest absolute component value | Maximum norm |
| $\|\mathbf A\|_F$ | `the Frobenius norm of A` | Square root of the sum of all squared entries | Frobenius norm |
| $\|\mathbf A\|_2$ | `the L two norm of A` | Maximum amplification of a unit input | Spectral norm |
| $\kappa_2(\mathbf A)$ | `the L two condition number of A` | Ratio of largest to smallest directional amplification | Invertible square matrix; rectangular extension in Core concept 8 |
| Relative error | `relative error` | Error magnitude divided by reference magnitude | The reference must be nonzero. |

## Core concept 1. A norm specifies a rule for vector size

A vector norm is a function satisfying:

1. $\|\mathbf x\|\ge0$, and $\|\mathbf x\|=0$ only for $\mathbf x=\mathbf 0$.
2. $\|\alpha\mathbf x\|=|\alpha|\|\mathbf x\|$.
3. $\|\mathbf x+\mathbf y\|\le\|\mathbf x\|+\|\mathbf y\|$.

The third condition is the triangle inequality. Different norms all measure size but combine coordinates in different ways.

## Core concept 2. Three common vector norms emphasize different quantities

For $\mathbf x=(x_1,\ldots,x_n)^\top$,

\[
\|\mathbf x\|_1
=
\sum_{i=1}^{n}|x_i|
\]

\[
\|\mathbf x\|_2
=
\sqrt{\sum_{i=1}^{n}x_i^2}
\]

\[
\|\mathbf x\|_\infty
=
\max_i|x_i|
\]

The L1 norm adds all absolute component values. The L2 norm measures Euclidean length; the infinity norm measures the largest component magnitude. When comparing errors or regularization in papers, check the norm used.

The figure below omits Example 1's zero third component and normalizes a vector in the same direction using each norm. Different unit boundaries require different divisors to give the same vector size 1.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The same vector direction normalized onto the L one diamond L two circle and infinity norm square](../../figures/assets/M02/M02-15-unit-norm-boundaries.svg)

<figcaption>Dividing (3,−4) by 7, 5, and 4, respectively, reaches the unit boundary of each norm. The diamond, circle, and square represent different size rules. The arrows are normalized vectors, not the original vector.</figcaption>
</figure>

## Core concept 3. The Frobenius norm measures the overall size of matrix entries

For

\[
\mathbf A=[a_{ij}]\in\mathbb R^{m\times n}
\]

the Frobenius norm is

\[
\|\mathbf A\|_F
=
\sqrt{\sum_{i=1}^{m}\sum_{j=1}^{n}a_{ij}^2}
\]

It equals the Euclidean norm obtained by flattening the matrix into a long vector.

In terms of SVD singular values,

\[
\|\mathbf A\|_F
=
\sqrt{\sum_i\sigma_i^2}
\]

It adds squared magnitudes across all singular directions.

## Core concept 4. The spectral norm is the largest directional amplification

The induced matrix 2-norm is

\[
\|\mathbf A\|_2
=
\max_{\mathbf x\ne\mathbf 0}
\frac{\|\mathbf A\mathbf x\|_2}{\|\mathbf x\|_2}
=
\sigma_{\max}(\mathbf A)
\]

Normalizing a nonzero input as $\mathbf u=\mathbf x/\|\mathbf x\|_2$ makes $\mathbf u$ a unit vector, with

\[
\frac{\|\mathbf A\mathbf x\|_2}{\|\mathbf x\|_2}
=\|\mathbf A\mathbf u\|_2
\]

Comparing amplification factors for nonzero inputs therefore equals comparing output norms for unit inputs. The maximum occurs along the largest right singular direction from M02-13.

For every $\mathbf x$,

\[
\|\mathbf A\mathbf x\|_2
\le
\|\mathbf A\|_2\|\mathbf x\|_2
\]

For nonzero inputs, multiply the statement that the amplification cannot exceed its maximum by $\|\mathbf x\|_2$. For zero input, both sides are 0, so the inequality still holds. It gives a worst-case upper bound on output size from input size.

The figure below distinguishes the spectral norm bound from the Frobenius norm sum for Example 2's matrix. The left shows the outputs actually produced by unit inputs; square areas on the right represent squared singular values.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A transformed unit circle fits inside the spectral norm bound while two squares visualize the sum of squared singular gains for the Frobenius norm](../../figures/assets/M02/M02-15-matrix-norm-geometry.svg)

<figcaption>The output ellipse's longest radius, 3, is the spectral norm. Combining squared gains 9 and 1 gives Frobenius norm √10, which is not the maximum output length for a unit input.</figcaption>
</figure>

## Core concept 5. Condition numbers measure imbalance in directional scaling

The 2-norm condition number of an invertible square matrix $\mathbf A$ is

\[
\kappa_2(\mathbf A)
=
\|\mathbf A\|_2\|\mathbf A^{-1}\|_2
\]

In singular values,

\[
\kappa_2(\mathbf A)
=
\frac{\sigma_{\max}(\mathbf A)}
{\sigma_{\min}(\mathbf A)}
\]

All singular values of an invertible matrix are positive. Undoing the SVD input and output transformations in reverse order gives gains $1/\sigma_i$ along singular directions. The largest inverse gain is $1/\sigma_{\min}$, so $\|\mathbf A^{-1}\|_2=1/\sigma_{\min}$. Substituting into the norm product gives the singular value ratio.

\[
\kappa_2(\mathbf A)\ge1
\]

An orthogonal matrix preserving length in every direction has condition number 1. Equal singular values also give ratio 1, so uniform scaling can have condition number 1 as well. This determines uniformity of directional gains, not preservation of length. For singular matrices, $\sigma_{\min}=0$, there is no finite inverse, and the condition number is treated as infinite.

For scalar $c\ne0$,

\[
\kappa_2(c\mathbf A)=\kappa_2(\mathbf A)
\]

Multiplying the whole matrix by $c$ multiplies every singular value by $|c|$, canceling in numerator and denominator. Condition number measures the ratio of directional gains, not overall matrix size.

The figure below compares uniform and direction-dependent scaling on the same length scale. The first and last scenes have equal determinants but different ellipse axis ratios.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Identity uniform scaling and anisotropic scaling produce circles or an ellipse with condition numbers one one and four](../../figures/assets/M02/M02-15-uniform-anisotropic-gains.svg)

<figcaption>2I doubles every direction but keeps the gain ratio 1. The matrix diag(2,1/2) preserves area while stretching one direction and shrinking the other, giving condition number 4.</figcaption>
</figure>

## Core concept 6. Condition numbers bound error amplification in linear systems

In

\[
\mathbf A\mathbf x=\mathbf b
\]

suppose $\mathbf A$ is invertible and exact, and only the right-hand side changes by $\delta\mathbf b$. The original right-hand side $\mathbf b$ is nonzero, so the original solution $\mathbf x$ is also nonzero. These conditions allow the denominators in both relative errors.

Subtracting the original equation from $\mathbf A(\mathbf x+\delta\mathbf x)=\mathbf b+\delta\mathbf b$ gives $\mathbf A\delta\mathbf x=\delta\mathbf b$. The solution change is therefore

\[
\delta\mathbf x
=
\mathbf A^{-1}\delta\mathbf b
\]

Apply the preceding norm bound to the inverse and original matrix, respectively:

\[
\|\delta\mathbf x\|_2
\le\|\mathbf A^{-1}\|_2\|\delta\mathbf b\|_2,
\qquad
\|\mathbf b\|_2\le\|\mathbf A\|_2\|\mathbf x\|_2
\]

Dividing the second inequality by positive denominators gives $1/\|\mathbf x\|_2\le\|\mathbf A\|_2/\|\mathbf b\|_2$. Use this bound for the relative error denominator in the first inequality to obtain

\[
\frac{\|\delta\mathbf x\|_2}{\|\mathbf x\|_2}
\le
\kappa_2(\mathbf A)
\frac{\|\delta\mathbf b\|_2}{\|\mathbf b\|_2}
\]

A large condition number allows a small relative input error to amplify into a large relative solution error.

This is a worst-direction upper bound, not a guarantee that any particular error amplifies that much. Errors in $\mathbf A$ itself require a separate perturbation bound.

The figure below applies equal-sized right-hand-side errors in two directions in a small comparison. Coordinates show only magnified changes, not the original right-hand side or solution. Both reference norms are 1, so error lengths also equal relative errors.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two equal magnitude right hand side errors mapped through an inverse to solution errors with amplification factors one and four](../../figures/assets/M02/M02-15-inverse-error-directions.svg)

<figcaption>The inverse of diag(1,1/4) preserves first-direction errors and multiplies second-direction errors by 4. Condition number 4 bounds possible relative amplification; the blue error does not reach that bound.</figcaption>
</figure>

## Core concept 7. Determinants and condition numbers provide different information

For a square matrix, the absolute determinant is the product of all singular values.

\[
|\det(\mathbf A)|
=
\prod_{i=1}^{n}\sigma_i
\]

The SVD orthogonal matrices $\mathbf U$ and $\mathbf V^\top$ preserve volume, so their absolute determinants are 1. Diagonal matrix $\boldsymbol\Sigma$ has determinant equal to the product of its singular values. The determinant product rule for composition gives the formula above. A condition number instead uses the largest-to-smallest ratio of these values, not their product.

For

\[
\mathbf A=
\begin{bmatrix}
100&0\\
0&0.01
\end{bmatrix}
\]

we have

\[
\det(\mathbf A)=1
\]

but

\[
\kappa_2(\mathbf A)
=
\frac{100}{0.01}
=
10^4
\]

Volume is preserved, but directional gains differ greatly.

## Core concept 8. Normal equations square the condition number

For a full column rank matrix $\mathbf A\in\mathbb R^{m\times n}$, the least-squares normal equations are

\[
\mathbf A^\top\mathbf A\widehat{\mathbf x}
=
\mathbf A^\top\mathbf b
\]

Here, we extend $\kappa_2(\mathbf A)$ to rectangular matrices using the ratio of largest to smallest positive singular values, $\sigma_{\max}/\sigma_{\min}$. This does not use $\mathbf A^{-1}$ for a rectangular matrix lacking an ordinary inverse. Full column rank makes all $n$ singular values positive and $\mathbf A^\top\mathbf A$ invertible.

The matrix $\mathbf A^\top\mathbf A$ is symmetric PSD with eigenvalues $\sigma_i^2$. Its singular values equal those positive eigenvalues, so

\[
\kappa_2(\mathbf A^\top\mathbf A)
=
\kappa_2(\mathbf A)^2
\]

Taking the largest-to-smallest ratio gives $(\sigma_{\max}^2/\sigma_{\min}^2)=(\sigma_{\max}/\sigma_{\min})^2$.

The original least-squares optimum does not change, but the coefficient matrix used to solve the normal equations has a larger gain ratio. Forming normal equations directly for a poorly conditioned problem can therefore increase sensitivity to computational error. QR or SVD solutions can provide stable alternatives.

The figure below applies $\mathbf A$ and $\mathbf A^\top\mathbf A$ separately to the same unit circle. Comparing ellipse axis ratios shows how squaring singular values also squares the condition number.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A unit circle mapped separately by A and A transpose A gives ellipses whose axis ratios are two and four](../../figures/assets/M02/M02-15-normal-equation-gains.svg)

<figcaption>Gains 2 and 1 become 4 and 1 in the example, changing the ratio from 2 to 4. The coefficient matrix for the same least-squares problem has different sensitivity; the optimum itself has not changed.</figcaption>
</figure>

## Example 1. Compare three vector norms

For

\[
\mathbf x=
\begin{bmatrix}3\\-4\\0\end{bmatrix}
\]

we have

\[
\|\mathbf x\|_1=3+4=7
\]

\[
\|\mathbf x\|_2=\sqrt{3^2+(-4)^2}=5
\]

\[
\|\mathbf x\|_\infty=4
\]

The same vector has different size values depending on the norm.

## Example 2. Compare two matrix norms

The singular values of

\[
\mathbf A=
\begin{bmatrix}
3&0\\
0&1
\end{bmatrix}
\]

are 3 and 1. Thus,

\[
\|\mathbf A\|_2=3
\]

and

\[
\|\mathbf A\|_F
=
\sqrt{3^2+1^2}
=
\sqrt{10}
\]

The spectral norm gives the largest directional gain; the Frobenius norm combines squared magnitudes of both directions.

## Example 3. Condition number and solution sensitivity

For

\[
\mathbf A=
\begin{bmatrix}
1&0\\
0&0.001
\end{bmatrix},
\qquad
\mathbf b=
\begin{bmatrix}1\\0.001\end{bmatrix}
\]

the solution is

\[
\mathbf x=
\begin{bmatrix}1\\1\end{bmatrix}
\]

Singular values 1 and 0.001 give

\[
\kappa_2(\mathbf A)=1000
\]

Changing the right-hand side's second component from $0.001$ to $0.002$ changes the solution's second component from 1 to 2. A small absolute error was greatly amplified under the inverse along the small singular value direction.

## Example 4. Norms and model sensitivity

If a weight matrix $\mathbf W$ has

\[
\|\mathbf W\|_2=12
\]

then

\[
\|\mathbf W\delta\mathbf x\|_2
\le
12\|\delta\mathbf x\|_2
\]

This bounds worst-case amplification of an input perturbation in the linear output.

It does not reveal how actual data perturbations align with the worst singular direction. Behavioral sensitivity of the whole model, including bias, nonlinearities, and later layers, requires separate calculations.

## Common misconceptions

### Misconception 1. There is only one norm

L1, L2, and infinity norms use different size rules. Specify the norm when comparing results.

### Misconception 2. Frobenius and spectral norms measure the same matrix size

The Frobenius norm combines all singular values; the spectral norm considers only the largest.

### Misconception 3. Invertibility guarantees numerical stability

Invertibility means the smallest singular value is nonzero. If small relative to the largest, it gives a large condition number, making the inverse problem potentially sensitive to relative error. Scaling all singular values down together reduces overall size but leaves their ratio unchanged.

### Misconception 4. A large condition number guarantees a large change for a particular model input

A condition number bounds amplification of right-hand-side relative error into solution relative error in an inverse problem with the exact matrix fixed. Distinguish this from forward absolute error gain, given by the spectral norm. Actual changes for a given perturbation and the whole nonlinear model must be measured directly.

## Exercises

### 1. Vector norms

Find the L1, L2, and infinity norms of

\[
\mathbf x=
\begin{bmatrix}-2\\1\\2\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

\[
\|\mathbf x\|_1=2+1+2=5
\]

\[
\|\mathbf x\|_2
=
\sqrt{(-2)^2+1^2+2^2}
=
3
\]

\[
\|\mathbf x\|_\infty=2
\]

</details>

### 2. Frobenius norm

Find the Frobenius norm of

\[
\mathbf A=
\begin{bmatrix}
1&-2\\
2&1
\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

\[
\|\mathbf A\|_F
=
\sqrt{1^2+(-2)^2+2^2+1^2}
=
\sqrt{10}
\]

</details>

### 3. A spectral norm bound

Suppose $\|\mathbf A\|_2=5$ and $\|\mathbf x\|_2=3$. Bound $\|\mathbf A\mathbf x\|_2$ and determine whether the actual value must equal the bound.

<details>
<summary>Show solution</summary>

\[
\|\mathbf A\mathbf x\|_2
\le
\|\mathbf A\|_2\|\mathbf x\|_2
=
15
\]

The bound is reached when the input aligns with the largest right singular direction. Other directions can give a smaller value.

</details>

### 4. Calculate a condition number

An invertible matrix has singular values $8,2,0.5$. Find its 2-norm condition number.

<details>
<summary>Show solution</summary>

\[
\kappa_2(\mathbf A)
=
\frac{\sigma_{\max}}{\sigma_{\min}}
=
\frac{8}{0.5}
=
16
\]

</details>

### 5. A relative error bound

Suppose $\kappa_2(\mathbf A)=200$, and the right-hand side has relative error $10^{-5}$. Bound the solution's relative error when the matrix itself has no error.

<details>
<summary>Show solution</summary>

\[
\frac{\|\delta\mathbf x\|_2}{\|\mathbf x\|_2}
\le
200\cdot10^{-5}
=
2\times10^{-3}
\]

This is a worst-direction bound, not a statement that the actual error equals it.

</details>

### 6. Distinguish four concepts

For a square matrix, write one sentence for the question answered by each of rank, determinant, spectral norm, and condition number.

<details>
<summary>Show solution</summary>

Rank counts independent output directions retained by the transformation. Determinant gives the overall oriented volume scaling factor.

Spectral norm gives the largest amplification of a unit input. Condition number is the largest-to-smallest gain ratio and describes worst-case relative sensitivity of the inverse problem.

</details>

### 7. M02 cumulative task: SVD and low-rank approximation of an activation matrix

Suppose the centered activation matrix is

\[
\mathbf H_c=
\begin{bmatrix}
2&0\\
-1&1\\
-1&-1
\end{bmatrix}
\in\mathbb R^{3\times2}
\]

Perform these tasks:

1. Check that each feature column has mean 0.
2. Find $\mathbf H_c^\top\mathbf H_c$ and the sample covariance matrix.
3. Find the singular values and right singular vectors.
4. Find rank-1 SVD approximation $\mathbf H_{c,1}$.
5. Find the retained squared Frobenius norm ratio and reconstruction error.
6. Distinguish supported representation claims from unsupported functional claims.

<details>
<summary>Show solution</summary>

The first column sums to $2-1-1=0$; the second sums to $0+1-1=0$. Both feature means are 0.

\[
\mathbf H_c^\top\mathbf H_c
=
\begin{bmatrix}
6&0\\
0&2
\end{bmatrix}
\]

With $N=3$, the sample covariance matrix is

\[
\mathbf S
=
\frac{1}{2}
\mathbf H_c^\top\mathbf H_c
=
\begin{bmatrix}
3&0\\
0&1
\end{bmatrix}
\]

The eigenvalues of $\mathbf H_c^\top\mathbf H_c$ are 6 and 2, so the singular values are

\[
\sigma_1=\sqrt6,
\qquad
\sigma_2=\sqrt2
\]

We can choose right singular vectors

\[
\mathbf v_1=
\begin{bmatrix}1\\0\end{bmatrix},
\qquad
\mathbf v_2=
\begin{bmatrix}0\\1\end{bmatrix}
\]

Keeping only the first singular component removes the second column, giving

\[
\mathbf H_{c,1}
=
\begin{bmatrix}
2&0\\
-1&0\\
-1&0
\end{bmatrix}
\]

The total squared Frobenius norm is

\[
\|\mathbf H_c\|_F^2
=
\sigma_1^2+\sigma_2^2
=
8
\]

and the rank-1 approximation retains 6. The retained ratio is

\[
\frac68=0.75
\]

The reconstruction error is

\[
\|\mathbf H_c-\mathbf H_{c,1}\|_F
=
\sigma_2
=
\sqrt2
\]

For these three samples, 75% of activation variation measured by squared norm lies along the first feature direction, and the rank-1 approximation is optimal in the Frobenius norm. These calculations alone do not establish whether the first direction means a particular human concept, whether the model uses it for predictions, or whether the same subspace appears in other data.

</details>

## Lesson summary

- A norm measures vector or matrix size; different norms emphasize different structures.
- The Frobenius norm combines all singular values; the spectral norm is the largest singular value.
- The inequality $\|\mathbf A\mathbf x\|_2\le\|\mathbf A\|_2\|\mathbf x\|_2$ gives a worst-case output size bound.
- A condition number is the largest-to-smallest singular value ratio and describes relative sensitivity of an inverse problem.
- Even an invertible matrix can be numerically sensitive if its condition number is large.
- Determinant, rank, norm, and condition number measure different matrix properties.

## Pass criteria

You pass if you can answer these questions without consulting the material:

- Can you calculate three vector norms and explain their differences?
- Can you calculate Frobenius and spectral norms from singular values?
- Can you bound output size using a matrix norm?
- Can you calculate condition numbers as singular value ratios?
- Can you interpret a linear system's relative error bound?
- Can you distinguish rank, determinant, norm, and condition number?

## M02 stage pass criteria

You pass stage M02 if you can perform these tasks without consulting the material:

- Calculate vector addition, scalar multiplication, inner products, and norms.
- Connect linear combinations, span, linear independence, bases, and dimension.
- Calculate matrix products using row inner products and column linear combinations, and interpret them as linear transformations.
- Solve linear systems and explain existence and uniqueness using kernels, images, and rank.
- Construct orthogonal bases and calculate subspace projections and least-squares solutions.
- Distinguish determinants, eigendecomposition, and spectral decomposition of symmetric matrices.
- Use SVD to find input directions, singular values, and output directions and construct low-rank approximations.
- Calculate covariance and PCA, limiting claims according to data, coordinates, and intervention evidence.
- Use condition numbers to assess numerical sensitivity of linear systems.

## Next lesson

The next lesson is [M03-01 Abstract vector spaces](../M03/M03-01-abstract-vector-spaces.md). It extends the operation laws learned for numeric column vectors to general vector spaces containing functions, polynomials, and matrices.

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Three vector norms and two matrix norms are distinguished.
- [x] Condition numbers are connected to singular values and relative error bounds.
- [x] Differences among determinant, rank, and condition number are explained.
- [x] The M02 cumulative task and stage pass criteria are included.
- [x] Every exercise has a solution.
- [x] Numerical sensitivity is distinguished from actual model-behavior claims.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
