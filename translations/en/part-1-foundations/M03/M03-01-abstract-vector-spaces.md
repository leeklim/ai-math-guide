---
id: "M03-01"
title: "Abstract vector spaces"
part: 1
stage: "M03"
status: "complete"
prerequisites:
  - "M02-01"
  - "M02-02"
  - "M02-07"
estimated_time: "110–135 minutes"
---

# M03-01. Abstract vector spaces

## Why this lesson matters

So far, vectors have mainly been columns of numbers. But the rules of linear algebra do not apply only to numerical arrays. Polynomials, functions, and matrices can also be added and multiplied by real numbers. If these operations satisfy the same laws, we can treat them as elements of vector spaces.

This viewpoint is needed to distinguish a model's parameters, activations, and the model function itself. Parameters are stored in finite-dimensional coordinates, but a model is also a function that sends inputs to outputs. Even when both objects can be called vectors, we must first specify the spaces they belong to. Only then can we determine whether we mean the same addition and the same basis.

## Learning objectives

After this lesson, you will be able to:

- Explain the operations and core axioms of a real vector space.
- Identify zero vectors and scalar multiplication for column vectors, polynomials, functions, and matrices.
- Determine whether a given set is a vector space by checking closure under addition and scalar multiplication.
- Distinguish an abstract vector from its coordinate column.
- Apply linear combinations, span, basis, and dimension to general vector spaces.

## Prerequisite check

- Prerequisite: [M02-01 Vectors and vector operations](../M02/M02-01-vectors-vector-operations.md)
- Prerequisite: [M02-02 Linear combinations and span](../M02/M02-02-linear-combinations-span.md)
- Prerequisite: [M02-07 Linear independence, basis, and dimension](../M02/M02-07-linear-independence-basis-dimension.md)
- Check: Can you calculate addition and scalar multiplication for column vectors?
- Check: Can you explain why a basis is an independent spanning set that represents each vector with unique coefficients?

If linear combinations or bases are unclear, review the prerequisite lessons first.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Scope |
|---|---|---|---|
| $V$ | `V` | The set to which the vectors belong | A real vector space in this lesson |
| $\mathbf u,\mathbf v$ | `u and v` | Elements of $V$ | They need not be arrays. |
| $\alpha,\beta$ | `alpha and beta` | Scalars multiplying vectors | $\alpha,\beta\in\mathbb R$ |
| $\mathbf 0_V$ | `the zero vector in V` | The additive identity in $V$ | Its form differs between spaces. |
| $\mathcal P_2$ | `calligraphic P sub two` | The space of real-coefficient polynomials of degree at most 2 | $\{a+bt+ct^2:a,b,c\in\mathbb R\}$ |
| $[\,\mathbf v\,]_{\mathcal B}$ | `the coordinates of v in the basis B` | The column of coefficients relative to the basis $\mathcal B$ | A column vector in $\mathbb R^n$ |

## Core concept 1. A vector is an object on which the space's operations act

In an abstract vector space, a vector is not defined as an arrow or a column of numbers. A set $V$ is equipped with two operations:

- Vector addition: $\mathbf u+\mathbf v\in V$
- Scalar multiplication: $\alpha\mathbf v\in V$

In this lesson, the scalars are real numbers. If these operations satisfy the vector space axioms, we call $V$ a real vector space. Whether an object is a vector therefore depends on its space and operations rather than its appearance.

For example, adding the polynomials $p(t)=1+2t$ and $q(t)=t-t^2$ gives

\[
(p+q)(t)=1+3t-t^2
\]

and multiplying by the real number 3 gives

\[
(3p)(t)=3+6t
\]

The results are again real-coefficient polynomials, so the operations stay within the same space.

Here, $t$ is the input to a polynomial, whereas 3 is a scalar multiplying the entire polynomial. Adding polynomials means adding the coefficients of terms of the same degree. Adding polynomials of degree at most 2, or multiplying them by a scalar, cannot create terms of degree 3 or higher, so the results remain in $\mathcal P_2$. In contrast, if we collect only polynomials of degree exactly 2, $p+(-p)$ is the zero polynomial and falls outside that set. We must check not only that the objects are polynomials, but also which polynomials the set includes.

For a function space, we likewise specify the operations first. For real-valued functions $f,g$ with a common domain, define $(f+g)(t)=f(t)+g(t)$ and $(\alpha f)(t)=\alpha f(t)$. Adding values at the same input, or scaling those values, produces another function. These are called pointwise operations.

If we plot the preceding polynomials as curves, addition adds their heights at the same input position.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Pointwise addition of the polynomial curves one plus two t and t minus t squared at a common input](../../figures/assets/M03/M03-01-pointwise-addition.svg)
  <figcaption>At input t=1.5, adding p's value of 4 and q's value of −0.75 gives a sum of 3.25. Adding values at the same position for other inputs produces the green sum curve. The curve itself is one element of the function space.</figcaption>
</figure>

Scalar multiplication keeps the input fixed and multiplies the output value at every input by the same factor.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![The polynomial one plus two t and its scalar multiple three plus six t with output values three and nine at input one](../../figures/assets/M03/M03-01-scalar-multiplication.svg)
  <figcaption>At t=1, the height is 3 for p and 9 for 3p. The purple dashed segment connects the two heights at the same input. Tripling the input t is different from multiplying the entire polynomial by 3.</figcaption>
</figure>

## Core concept 2. The vector space axioms specify the rules of calculation

The following laws must hold for all $\mathbf u,\mathbf v,\mathbf w\in V$ and $\alpha,\beta\in\mathbb R$.

1. Commutativity of addition: $\mathbf u+\mathbf v=\mathbf v+\mathbf u$
2. Associativity of addition: $(\mathbf u+\mathbf v)+\mathbf w=\mathbf u+(\mathbf v+\mathbf w)$
3. Existence of a zero vector: $\mathbf v+\mathbf 0_V=\mathbf v$
4. Existence of additive inverses: $\mathbf v+(-\mathbf v)=\mathbf 0_V$
5. Distributivity over vector addition: $\alpha(\mathbf u+\mathbf v)=\alpha\mathbf u+\alpha\mathbf v$
6. Distributivity over scalar addition: $(\alpha+\beta)\mathbf v=\alpha\mathbf v+\beta\mathbf v$
7. Associativity of scalar multiplication: $\alpha(\beta\mathbf v)=(\alpha\beta)\mathbf v$
8. Action of the scalar 1: $1\mathbf v=\mathbf v$

Addition and scalar multiplication must produce results in $V$. This is called closure. Rather than checking every axiom each time, it is efficient to start with inclusion of the zero vector and closure under addition and scalar multiplication when the set is a subset of a known vector space.

This subspace test uses the operations of the original space without changing them. Commutativity, associativity, and distributivity hold in the original space, so they also hold for elements of the subset. If the subset contains the zero vector and is closed under scalar multiplication, $-\mathbf v=(-1)\mathbf v$ also belongs to it, satisfying the additive inverse requirement. Thus, checking these three conditions avoids proving the remaining axioms again. The test cannot be applied unchanged to a set with arbitrarily different operations.

The axioms also imply $0\mathbf v=\mathbf 0_V$. The left side of $(0+0)\mathbf v=0\mathbf v+0\mathbf v$ is $0\mathbf v$. Adding the additive inverse of $0\mathbf v$ to both sides gives $\mathbf 0_V=0\mathbf v$. This equation explains the relation between the scalar 0 and the zero vector while keeping them distinct.

## Core concept 3. Zero vectors take different forms in different spaces

A zero vector is the additive identity, not merely the number 0.

| Space | Example element | Zero vector |
|---|---|---|
| $\mathbb R^3$ | $(1,2,3)^\top$ | $(0,0,0)^\top$ |
| $\mathcal P_2$ | $1-2t+t^2$ | The zero polynomial $0+0t+0t^2$ |
| A space of real-valued functions | $f(t)=\sin t$ | The function that is 0 at every input |
| $\mathbb R^{2\times2}$ | A $2\times2$ real matrix | The $2\times2$ zero matrix |

The zero function and zero polynomial always have value 0, but they are elements of a function space and a polynomial space, respectively. Even if the same symbol 0 is used, check which space it belongs to.

A function $f$ being 0 at one input does not make $f$ the zero function. For example, $f(t)=t$ satisfies $f(0)=0$, but it need not be 0 at other inputs. A zero function must be 0 at every input in its domain. Only then does pointwise addition give $g+f=g$ for every function $g$.

A zero value at one point and the zero function can also be distinguished in a graph.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![A line f of t equals t sharing one zero value with the zero function but differing elsewhere](../../figures/assets/M03/M03-01-zero-value-zero-function.svg)
  <figcaption>The orange point shows a zero value of f(t)=t, but its height is not zero at other inputs. The green zero function has height zero at every input, so adding it pointwise to any function leaves that function's values unchanged.</figcaption>
</figure>

## Core concept 4. Familiar algebraic concepts do not depend on the type of object

A linear combination of $\mathbf v_1,\ldots,\mathbf v_k\in V$ is

\[
\alpha_1\mathbf v_1+\cdots+\alpha_k\mathbf v_k
\]

The set of all possible linear combinations is their span. The definition does not mention vector components.

The vectors are linearly independent if the only coefficients satisfying

\[
\alpha_1\mathbf v_1+\cdots+\alpha_k\mathbf v_k=\mathbf 0_V
\]

are $\alpha_1=\cdots=\alpha_k=0$. An ordered list of linearly independent vectors that spans $V$ is a basis.

For example,

\[
\mathcal B=(1,t,t^2)
\]

is a basis of $\mathcal P_2$. Every $p(t)=a+bt+ct^2$ has the unique representation

\[
p=a\cdot1+b\cdot t+c\cdot t^2
\]

Thus, $\dim\mathcal P_2=3$.

Consider the two basis requirements separately. By the definition of $\mathcal P_2$, every polynomial in the space can be written as a linear combination of $1,t,t^2$, so they span the space. Also, $a\cdot1+b\cdot t+c\cdot t^2$ being the zero polynomial means that all its coefficients are zero, so $a=b=c=0$. This establishes linear independence. We did not conclude that the list was a basis merely because we found a representation with three coefficients: we checked both spanning and independence.

If two coefficient lists represent the same polynomial, subtracting the representations gives the zero polynomial. Linear independence forces every coefficient difference to be zero, so the lists are identical. The argument for unique coordinates from M02 applies unchanged to polynomials.

Each of the three polynomial basis elements is itself a function that sends inputs to values.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![The three basis polynomial functions one t and t squared drawn on a shared input axis](../../figures/assets/M03/M03-01-polynomial-basis-curves.svg)
  <figcaption>The three elements of the basis (1,t,t²) are plotted separately. Multiplying them by coefficients and adding produces a polynomial of degree at most 2. Their different appearances do not prove independence; independence follows from the zero-polynomial coefficient argument above.</figcaption>
</figure>

## Core concept 5. A vector and its coordinate column are not the same object

Once a basis $\mathcal B=(\mathbf b_1,\ldots,\mathbf b_n)$ is fixed, collect the coefficients in

\[
\mathbf v
=
c_1\mathbf b_1+\cdots+c_n\mathbf b_n
\]

into the column

\[
[\mathbf v]_{\mathcal B}
=
\begin{bmatrix}
c_1\\
\vdots\\
c_n
\end{bmatrix}
\]

The vector $\mathbf v$ belongs to the original space $V$, whereas $[\mathbf v]_{\mathcal B}$ is a column vector in $\mathbb R^n$.

The polynomial

\[
p(t)=2-t+3t^2
\]

is itself a polynomial function. Its coordinates relative to $\mathcal B=(1,t,t^2)$ are

\[
[p]_{\mathcal B}
=
\begin{bmatrix}
2\\
-1\\
3
\end{bmatrix}
\]

Changing the basis changes the coordinate column, but it does not change the polynomial $p$.

Coordinates provide the information needed to reconstruct the original vector. Multiplying the three entries above by $1,t,t^2$, respectively, and adding recovers $p$. Each entry is a coefficient attached to a basis polynomial, not the polynomial's value at a particular input. The order of the basis must also be fixed so that we know which coefficient multiplies which polynomial.

In the same basis, suppose $\mathbf u=\sum_i a_i\mathbf b_i$ and $\mathbf v=\sum_i c_i\mathbf b_i$. Distributivity gives $\alpha\mathbf u+\beta\mathbf v=\sum_i(\alpha a_i+\beta c_i)\mathbf b_i$. Therefore,

\[
[\alpha\mathbf u+\beta\mathbf v]_{\mathcal B}
=\alpha[\mathbf u]_{\mathcal B}+\beta[\mathbf v]_{\mathcal B}
\]

Abstract vectors and coordinate columns are different objects, but recording coordinates in a fixed basis preserves linear combinations. This is why we can transfer calculations in an abstract space to calculations with column vectors.

Multiplying the coordinate coefficients by the actual basis functions reconstructs the original polynomial.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Weighted basis functions two minus t and three t squared summing to the polynomial two minus t plus three t squared](../../figures/assets/M03/M03-01-coefficient-reconstruction.svg)
  <figcaption>Adding the heights of the three curves formed by coefficients 2, −1, and 3 gives the green polynomial p. Its value at input 1 is 4, which differs from the second coordinate, −1. Coordinates are coefficients attached to a chosen basis; a function value is obtained by supplying an input to the reconstructed function.</figcaption>
</figure>

## Example 1. Determine whether a subset is a vector space

### Problem

Determine whether

\[
S=\{(x,y)^\top\in\mathbb R^2:x+y=0\}
\]

and

\[
A=\{(x,y)^\top\in\mathbb R^2:x+y=1\}
\]

are subspaces of $\mathbb R^2$.

### Solution

The set $S$ contains $(0,0)^\top$. If $\mathbf u=(u_1,u_2)^\top$ and $\mathbf v=(v_1,v_2)^\top$ belong to $S$, then

\[
u_1+u_2=0,
\qquad
v_1+v_2=0
\]

Hence,

\[
(u_1+v_1)+(u_2+v_2)=0
\]

so $\mathbf u+\mathbf v\in S$. Also, for $\alpha\in\mathbb R$,

\[
\alpha u_1+\alpha u_2=\alpha(u_1+u_2)=0
\]

so $\alpha\mathbf u\in S$. Therefore, $S$ is a subspace.

The set $A$ does not contain the zero vector: $0+0\ne1$. Thus, $A$ is not a subspace.

### What the result means

The set $S$ is a line through the origin, whereas $A$ is an affine set obtained by translating that line. Both look like lines, but a vector space must contain the zero vector.

On the line through the origin, addition and scalar multiplication also stay on the line. The following coordinates illustrate closure.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![A line x plus y equals zero containing two input vectors their sum and a negative scalar multiple](../../figures/assets/M03/M03-01-subspace-closure.svg)
  <figcaption>The sum of the two blue inputs and the result of multiplication by −2 both satisfy x+y=0 and lie on the same line. The orange origin also belongs to the line. These coordinates illustrate the general closure calculation above.</figcaption>
</figure>

On a translated line, the same kinds of operations can leave the set.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![An affine line x plus y equals one containing two vectors but excluding their sum and the zero vector](../../figures/assets/M03/M03-01-affine-not-closed.svg)
  <figcaption>The points (1,0) and (0,1) lie on the line, but their sum (1,1) satisfies x+y=2 and lies outside it. The gray origin also fails x+y=1. Check inclusion of the zero vector and closure under the operations rather than the line's appearance.</figcaption>
</figure>

## Example 2. Calculate with polynomials as vectors

### Problem

In $\mathcal P_2$, let

\[
p(t)=1+t,
\qquad
q(t)=2-t+t^2
\]

Calculate $2p-q$ and its coordinates relative to the basis $\mathcal B=(1,t,t^2)$.

### Solution

\[
2p(t)-q(t)
=
2(1+t)-(2-t+t^2)
=
3t-t^2
\]

Therefore,

\[
[2p-q]_{\mathcal B}
=
\begin{bmatrix}
0\\
3\\
-1
\end{bmatrix}
\]

### What the result means

We used function addition and scalar multiplication, but the coefficient calculation is the same as a column-vector calculation. The basis translates the abstract vectors into numerical coordinates.

## Example 3. Distinguish different vector spaces in a model

A single token activation in a layer of width $d$ is usually represented as $\mathbf h\in\mathbb R^d$. A weight matrix in the same model belongs to $\mathbf W\in\mathbb R^{m\times d}$. Both objects can be regarded as elements of vector spaces, but they belong to different spaces.

\[
\mathbf W\mathbf h\in\mathbb R^m
\]

is defined, whereas $\mathbf W+\mathbf h$ is generally not. Calling both objects vectors in an abstract sense does not make them addable. Check the spaces they belong to and the input requirements of each operation.

If model functions $f$ and $g$ have the same types of inputs and outputs, pointwise addition can also be defined:

\[
(f+g)(\mathbf x)=f(\mathbf x)+g(\mathbf x)
\]

However, we generally cannot automatically conclude that the set of functions representable by a particular neural network architecture is closed under this addition. Distinguish the full function space from the family of functions represented by a particular architecture.

## Common misconceptions

### Misconception 1. A vector is an arrow or a column of numbers

Arrows and numerical columns are familiar representations of vectors. Polynomials, functions, and matrices can also be vectors when they satisfy the vector space axioms.

### Misconception 2. A subset that is a line or a plane is a subspace

An affine line or plane that does not pass through the origin is not a subspace because it does not contain the zero vector.

### Misconception 3. Any vectors can be added to one another

Addition is defined within the same vector space. An activation in $\mathbb R^d$ and a weight matrix in $\mathbb R^{m\times d}$ belong to different spaces.

### Misconception 4. Changing the coordinate column changes the vector

Representing the same vector in a different basis changes its coordinates. Distinguish the object itself from its coordinate representation.

## Exercises

### 1. Read an axiom

Explain the following in words:

\[
\alpha(\mathbf u+\mathbf v)=\alpha\mathbf u+\alpha\mathbf v
\]

<details>
<summary>Show solution</summary>

Adding two vectors and then multiplying by the scalar $\alpha$ gives the same result as multiplying each vector by $\alpha$ and then adding. This is the axiom that scalar multiplication distributes over vector addition.

</details>

### 2. Identify zero vectors

Describe the zero vector in $\mathcal P_3$, a space of real-valued functions, and $\mathbb R^{2\times3}$.

<details>
<summary>Show solution</summary>

In $\mathcal P_3$, it is the zero polynomial, with every coefficient equal to 0. In the function space, it is the zero function, which sends every input to 0. In $\mathbb R^{2\times3}$, it is the $2\times3$ zero matrix, with every entry equal to 0. The three objects look different, but each is the additive identity in its space.

</details>

### 3. Test for a subspace

Determine whether

\[
S=\{(x,y,z)^\top\in\mathbb R^3:x-2y+z=0\}
\]

is a subspace.

<details>
<summary>Show solution</summary>

The zero vector satisfies the equation. If $\mathbf u,\mathbf v\in S$, the left side is 0 for each vector, so the left side for their sum is also 0. For $\alpha\mathbf u$, the left side is the original left side, 0, multiplied by $\alpha$. The set contains the zero vector and is closed under addition and scalar multiplication, so it is a subspace.

</details>

### 4. A set that is not a vector space

Give one reason why

\[
C=\{(x,y)^\top\in\mathbb R^2:x\ge0,\ y\ge0\}
\]

is not a real vector space.

<details>
<summary>Show solution</summary>

Although $(1,1)^\top\in C$, multiplication by the scalar $-1$ gives $(-1,-1)^\top$, which is not in $C$. The set is not closed under real scalar multiplication, so it is not a real vector space.

</details>

### 5. Polynomial coordinates

Calculate the coordinates of $p(t)=4-2t+t^2$ in the basis $\mathcal B=(1,t,t^2)$. Also explain the difference between the coordinates and $p$ itself.

<details>
<summary>Show solution</summary>

\[
[p]_{\mathcal B}
=
\begin{bmatrix}
4\\
-2\\
1
\end{bmatrix}
\]

The object $p$ is a polynomial that sends input $t$ to a value; its coordinates are a column of coefficients for reconstructing $p$ in the chosen basis.

</details>

### 6. Basis and dimension

Explain why the following four matrices form a basis of $\mathbb R^{2\times2}$.

\[
\mathbf E_{11}=
\begin{bmatrix}1&0\\0&0\end{bmatrix},
\quad
\mathbf E_{12}=
\begin{bmatrix}0&1\\0&0\end{bmatrix},
\quad
\mathbf E_{21}=
\begin{bmatrix}0&0\\1&0\end{bmatrix},
\quad
\mathbf E_{22}=
\begin{bmatrix}0&0\\0&1\end{bmatrix}
\]

<details>
<summary>Show solution</summary>

Every $\mathbf A=\begin{bmatrix}a&b\\c&d\end{bmatrix}$ has the unique representation

\[
\mathbf A
=
a\mathbf E_{11}+b\mathbf E_{12}+c\mathbf E_{21}+d\mathbf E_{22}
\]

Thus, the four matrices span the space and are linearly independent. They form a basis, and $\dim\mathbb R^{2\times2}=4$.

</details>

### 7. Critique a model claim

Critique the statement: “Activations and weights are both vectors, so we can add them directly and analyze them as a single representation.”

<details>
<summary>Show solution</summary>

First specify the space in which each activation and weight is an element. Usually an activation is a column vector in $\mathbb R^d$ and a weight is a matrix in $\mathbb R^{m\times d}$, so direct addition is not defined. We could flatten or map them before adding, but we would then need to specify the new representation space and mapping rules.

</details>

## Lesson summary

- A vector space is a set equipped with vector addition and scalar multiplication that satisfy the axioms.
- Polynomials, functions, and matrices are also elements of vector spaces under suitable operations.
- A subspace must contain the zero vector and be closed under addition and scalar multiplication.
- Linear combination, span, linear independence, basis, and dimension can be defined without component representations.
- An abstract vector and its coordinate column in a chosen basis are different objects.

## Pass criteria

You pass if you can answer the following without consulting the lesson.

- Can you explain the two operations and core axioms of a real vector space?
- Can you identify the zero vectors in function spaces and matrix spaces?
- Can you use closure to determine whether a subset is a subspace?
- Can you calculate a polynomial's basis coordinates?
- Can you distinguish an abstract vector from its coordinate column?

## Next lesson

- [M03-02 Linear maps and matrix representation](M03-02-linear-maps-matrix-representation.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] The operations of a real vector space are distinguished from its axioms.
- [x] Examples include polynomials, functions, and matrices.
- [x] Abstract vectors are distinguished from coordinate columns.
- [x] Example calculations have been checked.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
