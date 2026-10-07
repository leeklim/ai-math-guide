---
id: "A09-KER-05"
title: "Introduction to spectrum and compact operators"
part: 4
stage: "A09-KER"
status: "complete"
prerequisites: ["M02-11", "M02-12", "A09-KER-04"]
estimated_time: "90–120 minutes"
---

# A09-KER-05. Introduction to spectrum and compact operators

## Why this lesson matters

Gram matrix eigenvectors are defined only on a finite sample. Describing kernel geometry at the population level requires an integral operator defined with respect to a data distribution. The spectrum of a compact self-adjoint operator provides a route from matrix spectral decomposition to function spaces.

## Learning objectives

- Define a kernel integral operator.
- Distinguish operator eigenfunctions from matrix eigenvectors.
- Explain the roles of eigenvalues and eigenfunctions in a kernel expansion.
- Explain how an empirical spectrum depends on the sample and measure.

## Prerequisite check

- Prerequisite lessons: [M02-11 Eigenvalues and eigenvectors](../../part-1-foundations/M02/M02-11-eigenvalues-eigenvectors.md), [M02-12 Symmetric matrices and the spectral theorem](../../part-1-foundations/M02/M02-12-symmetric-matrices-spectral-theorem.md), [A09-KER-04 Introduction to RKHS](A09-KER-04-rkhs-introduction.md)
- Check question: How does a quadratic form decompose in a symmetric matrix's eigenvector basis?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $(T_kf)(x)$ | `T sub k applied to f at x` | Value of the output function $T_kf$ evaluated at $x$ | scalar |
| $T_k\psi_j=\lambda_j\psi_j$ | `T sub k applied to psi sub j equals lambda sub j psi sub j` | operator eigenfunction equation | function identity |
| $\mu$ | `mu` | Reference distribution on the input space | probability measure |
| $d_{\mathrm{eff}}(\tau)$ | `the effective dimension at tau` | Spectral dimension depending on the threshold | nonnegative scalar |
| $L^2(\mu)$ | `L two of mu` | Space of square-integrable functions | Equality of functions is also judged relative to $\mu$ |

## Core concepts

### The distribution used to measure function size

We consider functions satisfying $\int |f(x)|^2d\mu(x)<\infty$ and denote this space by $L^2(\mu)$. Its inner product is $\langle f,g\rangle_{L^2(\mu)}=\int f(x)g(x)d\mu(x)$, and its squared norm is $E_\mu[f(X)^2]$. Instead of summing componentwise as in matrix calculations, we average according to the distribution. Changing $\mu$ can therefore change norms and orthogonality even for the same functions.

In $L^2(\mu)$, two functions that differ only on a set of probability 0 are treated as the same element. This differs from an RKHS, where values at specific points remain distinguishable. For the pointwise expressions below, we also impose conditions allowing continuous representative functions.

The next figure shows a case where a difference at one point does not distinguish elements of L².

<figure class="lesson-figure" markdown="1">

![The zero function and a function differing only at the point zero have different point evaluations but represent the same L2 element under a uniform continuous measure](../../figures/assets/A09-KER/A09-KER-05-l2-point-change.svg)

<figcaption>The open and filled purple points indicate that g differs only at 0. That point has probability 0 under a uniform continuous distribution, so L² treats the two functions as the same element.</figcaption>
</figure>

### Kernel integral operators and compactness conditions

For a distribution $\mu$ and kernel $k$, define the integral operator by

$$
(T_kf)(x)=\int_{\mathcal X}k(x,x')f(x')\,d\mu(x')
$$

The output location $x$ remains, while $x'$ is integrated out. At each location, weight $f(x')$ by $k(x,x')$ and average to create the new function $T_kf$. With the kernel and distribution fixed, linearity of integration gives $T_k(af+bg)=aT_kf+bT_kg$.

In the next figure, a constant kernel turns the input function's average into the output function.

<figure class="lesson-figure" markdown="1">

![A constant kernel averages f of z equals one plus z under uniform measure from minus one to one, yielding the constant output function one](../../figures/assets/A09-KER/A09-KER-05-constant-average.svg)

<figcaption>The blue function has average 1. After averaging out z, the green output has the same value 1 at every x.</figcaption>
</figure>

A concrete sufficient condition is a continuous, symmetric, positive semidefinite kernel $k$ on a compact input domain in Euclidean space, with $\mu$ a probability measure. A continuous PSD kernel on a closed interval is one example. Then $T_k$ is a bounded linear operator on $L^2(\mu)$. Symmetry gives self-adjointness, $\langle f,T_kg\rangle=\langle T_kf,g\rangle$, and PSD gives positivity, $\langle f,T_kf\rangle\geq0$.

Compact does not mean bounded. Compactness means that when a norm-bounded sequence of functions is mapped through $T_k$, the outputs have a subsequence converging in norm. The identity operator in an infinite-dimensional space is bounded but not compact.

The spectrum of an operator is defined by failure of a bounded inverse for $T_k-\lambda I$: it is the set of all such $\lambda$. For matrices it equals the set of eigenvalues, but the distinction matters in infinite dimensions. Every nonzero spectral value of a compact self-adjoint operator is an eigenvalue, and each corresponding eigenspace is finite-dimensional. If there are infinitely many such values, their only possible accumulation point is 0. However, 0 can belong to the spectrum without being an eigenvalue. Do not automatically equate the entire spectrum with a list of eigenvalues.

### Eigenfunctions and kernel expansions

In $T_k\psi_j=\lambda_j\psi_j$, the function $\psi_j$ is not the zero function. Applying the operator preserves the function's shape and scales its magnitude by $\lambda_j$. A finite matrix transforms a vector with $n$ components; here the operator transforms a function defined over the entire input domain. An eigenfunction is normalized by $\int\psi_j(x)^2d\mu(x)=1$, and distinct orthogonal modes satisfy $\int\psi_i(x)\psi_j(x)d\mu(x)=0$. Distinguish this inner product from the RKHS inner product.

If, in addition to the sufficient conditions above, $\mu$ assigns positive probability to every open neighborhood in the input domain, continuous eigenfunction representatives allow the kernel expansion

$$
k(x,x')=\sum_{j:\lambda_j>0}\lambda_j\psi_j(x)\psi_j(x')
$$

This Mercer expansion holds for every input pair, and the series converges uniformly under these conditions. Spectral decomposition of a compact self-adjoint operator alone does not automatically guarantee such a pointwise kernel expansion.

Each term multiplies two evaluation values of the mode $\psi_j$, with weight $\lambda_j$. Connecting this to the preceding lesson's feature map, the $j$th feature can be $\sqrt{\lambda_j}\psi_j(x)$. Under this normalization, a large eigenvalue identifies a direction entering the kernel with a large weight. The expansion alone does not establish alignment with labels or a causal function within the model.

The next two figures distinguish an eigenfunction's domain from the contributions of modes to a kernel expansion.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![For kernel 1+xz, a continuous normalized eigenfunction sqrt(3)x has eigenvalue one third under uniform measure, while a five-entry empirical eigenvector has a different normalization and eigenvalue one half](../../figures/assets/A09-KER/A09-KER-05-eigenfunction-samples.svg)

<figcaption>The left panel shows a function over the entire interval; the right shows components on five samples. The uniform finite measure on the right differs from the continuous measure on the left, so distinguish the norm conventions and eigenvalues.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![The kernel section 1+0.5z is the sum of a constant Mercer mode and a linear mode weighted by eigenvalue one third with normalized eigenfunction sqrt(3)x](../../figures/assets/A09-KER/A09-KER-05-mercer-two-modes.svg)

<figcaption>Fixing x=0.5 in kernel 1+xz gives the sum of a constant contribution 1 and linear contribution 0.5z. The normalized eigenfunction's √3 combines with eigenvalue 1/3 to produce the actual kernel term.</figcaption>
</figure>

### Sample matrices and effective dimension

For $n$ points, assigning probability $1/n$ to each turns the integral into the average

$$
(T_{k,n}f)(x_i)=\frac{1}{n}\sum_{r=1}^{n}k(x_i,x_r)f(x_r)
$$

The matrix acting on the vector of function values at observed points is exactly $K/n$. Comparing eigenvalues of $K$ directly with population operator eigenvalues omits this average normalization. Sampling from a different distribution also changes the operator being approximated. Even with iid sampling from the same $\mu$, finite-sample eigenpairs are estimates, and individual directions associated with nearby eigenvalues may mix under small changes.

The next two figures show the effects of average normalization and distribution changes separately.

<figure class="lesson-figure" markdown="1">

![Eigenvalues 1.6 and 0.4 of a two-sample Gram matrix become 0.8 and 0.2 after division by two for a uniform empirical integral operator](../../figures/assets/A09-KER/A09-KER-05-gram-normalization.svg)

<figcaption>Averaging two points with mass 1/2 each halves both eigenvalues. Do not compare K's sum scale directly with K/n's average scale.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Changing probability masses on the same support {-1,0,1} changes the eigenvalue of kernel xz from two thirds to one fifth and changes the L2 norm of f(z)=z](../../figures/assets/A09-KER/A09-KER-05-measure-weighted-operator.svg)

<figcaption>Even with the kernel and input locations unchanged, changing the averaging masses changes Eμ[Z²] from 2/3 to 0.2. In this example, both the squared L² norm of function z and the operator eigenvalue are determined by that expectation.</figcaption>
</figure>

At regularization scale $\tau>0$, using

$$
d_{\mathrm{eff}}(\tau)=\sum_j\frac{\lambda_j}{\lambda_j+\tau}
$$

gives a dimension more sensitive to scale than hard rank. Modes with $\lambda_j\gg\tau$ contribute nearly 1; those with $\lambda_j\ll\tau$ contribute about $\lambda_j/\tau$. An eigenvalue of 0 contributes 0. This sums weights across directions rather than counting with a hard threshold, so a value such as 1.3 is possible.

The infinite sum must also be checked for finiteness. If $\sum_j\lambda_j<\infty$, then $\lambda_j/(\lambda_j+\tau)\leq\lambda_j/\tau$ makes the sum finite. Under the Mercer conditions above, $\sum_j\lambda_j=\int k(x,x)d\mu(x)<\infty$. Compactness alone or merely $\lambda_j\to0$ does not guarantee this finiteness. A finite Gram matrix has finitely many terms, but transferring the definition to infinite dimensions requires this condition.

The next figure shows each mode's contribution and their sum decreasing as τ increases.

<figure class="lesson-figure" markdown="1">

![Eigenvalues four and one contribute fractions 4/(4+tau) and 1/(1+tau) to effective dimension, summing to 1.3 at tau one](../../figures/assets/A09-KER/A09-KER-05-effective-dimension.svg)

<figcaption>At τ=1, the contributions are 0.8 and 0.5. Effective dimension 1.3 is a scale-dependent weighted sum, not a hard rank counting two directions.</figcaption>
</figure>

## Small example

Use a uniform measure on two points and $K=\begin{bmatrix}1&\rho\\\rho&1\end{bmatrix}$. PSD requires $|\rho|\leq1$. A function can be represented by its two evaluation values $(f(x_1),f(x_2))$, and the integral operator is $K/2$.

Multiplying the constant mode's value vector $(1,1)$ gives $\frac{1+\rho}{2}(1,1)$; multiplying the contrast mode $(1,-1)$ gives $\frac{1-\rho}{2}(1,-1)$. These functions have $L^2(\mu)$ norm $\sqrt{(1^2+1^2)/2}=1$ and are orthogonal. Their normalization differs from matrix eigenvectors $(1,\pm1)/\sqrt2$ normalized by Euclidean norm. When $\rho=1$, the constant mode has eigenvalue 1 and the contrast mode has eigenvalue 0. A mode with eigenvalue 0 is still a nonzero function; the zero function itself is not an eigenfunction.

The next figure shows the two modes scaled by 0.8 and 0.2 when ρ=0.6.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![On a two-point domain with correlation 0.6, the constant function values (1,1) scale by 0.8 and the contrast values (1,-1) scale by 0.2 under K/2](../../figures/assets/A09-KER/A09-KER-05-two-point-modes.svg)

<figcaption>The blue circles show the input function's two values, and the green squares show the values after applying the operator. Only the magnitude of the values changes; the constant or contrast mode shape is preserved.</figcaption>
</figure>

## Common misconceptions

- Gram matrix eigenvalues and population operator eigenvalues are not equal without accounting for normalization.
- Rapid spectral decay does not itself imply label prediction or a causal mechanism.

## Exercises

### 1. Operator
For $k(x,x')=1$ and a probability measure $\mu$, write $(T_kf)(x)$.
<details><summary>Show solution</summary>

It is $(T_kf)(x)=\int f(x')d\mu(x')=E_\mu[f(X)]$, a constant function independent of $x$.
</details>

### 2. Eigenmode
For the constant-kernel operator above, what eigenvalue do mean-zero functions have, apart from the normalized constant function with eigenvalue 1?
<details><summary>Show solution</summary>

A mean-zero function integrates to 0, so the operator maps it to the zero function, and it has eigenvalue 0.
</details>

### 3. Effective dimension
For eigenvalues $(4,1)$ and $\tau=1$, find $d_{\mathrm{eff}}(1)$.
<details><summary>Show solution</summary>

It is $4/(4+1)+1/(1+1)=0.8+0.5=1.3$.
</details>

### 4. Model interpretation
Why must prompt distributions be matched when comparing activation Gram spectra between two models?
<details><summary>Show solution</summary>

The integral operator itself depends on the reference distribution $\mu$. Different prompt distributions mix model differences with measure differences in the spectrum.
</details>

## Evidence and update boundaries

Spectral expansion requires regularity conditions on the kernel, domain, and measure. This lesson explains only the roles of those conditions, without proofs from functional analysis.

- [MIT 18.102, Compact operators](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/9eaaf363541d01d53c330ee7931fc715_MIT18_102s21_lec20.pdf): Used to check the definition of compactness, the identity counterexample, and the distinction between 0 in the spectrum and 0 as an eigenvalue.
- [MIT 18.102, Spectral theorem](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/57596554e180e442c9487f580303147b_MIT18_102s21_lec22.pdf): Used to check the nonzero spectrum and finite-dimensional eigenspace conditions for compact self-adjoint operators.
- [Duke STA941, RKHS fundamentals](https://www2.stat.duke.edu/~st118/sta941/rkhs-fundamentals.pdf): Used to check the $L^2$ operator and Mercer expansion conditions in §6. Finiteness of effective dimension is checked through the termwise inequality and diagonal integral in the text.

## Lesson summary

- A kernel integral operator includes the population distribution.
- An eigenfunction is a spectral direction in function space.
- A Gram spectrum is a finite-sample approximation and requires normalization.
- Effective dimension depends on the regularization scale.

## Pass criteria

- Can you write an integral operator and an eigenfunction equation?
- Can you distinguish an empirical spectrum from a population spectrum?

## Next lesson

- [A09-KER-06 Neural tangent kernel](A09-KER-06-neural-tangent-kernel.md)

## Author checklist

- [x] Gram matrices and population integral operators are distinguished.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
