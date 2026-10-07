---
id: "M02-03"
title: "Inner products, length, and angles"
part: 1
stage: "M02"
status: "complete"
prerequisites:
  - "M02-01"
  - "M02-02"
estimated_time: "100~125 minutes"
---

# M02-03. Inner products, length, and angles

## Why this lesson matters

The inner product of two vectors tells us how aligned their directions are, whether they are orthogonal, and how much of one vector lies along the other direction. Vector length and the distance between two points also come from inner products.

Neural networks use the same calculations for embedding similarity, attention scores, and orthogonal projection. Inner products depend on vector lengths and coordinate scales, so check the calculation conditions as well.

## Learning objectives

After completing this lesson, you will be able to:

- Calculate an inner product as a sum of corresponding component products.
- Find Euclidean norms and distances from inner products.
- Use the inner product's sign and cosine to determine the angle between vectors.
- Check orthogonality and project one vector orthogonally onto another.
- Distinguish the similarity shown by cosine similarity from model use that it does not establish.

## Prerequisite check

- Prerequisite lesson: [M02-01 Vectors and vector operations](M02-01-vectors-vector-operations.md)
- Prerequisite lesson: [M02-02 Linear combinations and span](M02-02-linear-combinations-span.md)
- Check question: Can you add equal-dimensional vectors componentwise and multiply them by scalars?
- Check question: Can you describe the span of all real multiples of one vector?

If vector operations or span are unclear, first review the prerequisite lessons.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| $\langle\mathbf u,\mathbf v\rangle$ | `the inner product of u and v` | Scalar sum of corresponding component products | $\mathbf u,\mathbf v\in\mathbb R^n$ |
| $\mathbf u^\top\mathbf v$ | `u transpose v` | Matrix notation for the standard Euclidean inner product | The result is a scalar. |
| $\|\mathbf v\|_2$ | `the L two norm of v` | Euclidean length of a vector | Nonnegative |
| $d(\mathbf x,\mathbf y)$ | `the distance between x and y` | $\|\mathbf x-\mathbf y\|_2$ | Same dimension |
| $\theta$ | `theta` | Angle between two nonzero vectors | $0\le\theta\le\pi$ |
| $\operatorname{proj}_{\mathbf v}\mathbf u$ | `the projection of u onto v` | Component of $\mathbf u$ along $\mathbf v$ | $\mathbf v\ne\mathbf 0$ |

## Core concept 1. An inner product adds corresponding component products

The standard Euclidean inner product of $\mathbf u,\mathbf v\in\mathbb R^n$ is

\[
\langle\mathbf u,\mathbf v\rangle
=
\mathbf u^\top\mathbf v
=
\sum_{i=1}^{n}u_i v_i
\]

It takes two vectors and produces one scalar.

For example,

\[
\begin{bmatrix}1\\2\\-1\end{bmatrix}^{\top}
\begin{bmatrix}3\\0\\4\end{bmatrix}
=
1\cdot3+2\cdot0+(-1)\cdot4
=
-1
\]

In the figure below, check the matching component products row by row, then add them. Distinguish the list of rowwise products from the final scalar.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three matching component products are added to produce one scalar inner product of minus one](../../figures/assets/M02/M02-03-inner-product-reduction.svg)

<figcaption>The elementwise product leaves three components (3,0,-4)ᵀ, whereas the inner product adds them and outputs only −1.</figcaption>
</figure>

## Core concept 2. Length comes from a vector's inner product with itself

The Euclidean norm of $\mathbf v$ is

\[
\|\mathbf v\|_2
=
\sqrt{\mathbf v^\top\mathbf v}
=
\sqrt{\sum_{i=1}^{n}v_i^2}
\]

Square each component, add the squares, then take the square root.

\[
\|\mathbf v\|_2\ge0
\]

The norm $\|\mathbf v\|_2=0$ only when $\mathbf v=\mathbf 0$. Each squared component is nonnegative, so their sum can be 0 only if every component is 0. In $\mathbb R^2$, the norm is the hypotenuse length given by the Pythagorean theorem.

Multiplying by a scalar $\alpha$ multiplies each component's square by $\alpha^2$. Thus,

\[
\|\alpha\mathbf v\|_2
=\sqrt{\alpha^2\sum_i v_i^2}
=|\alpha|\,\|\mathbf v\|_2
\]

Length cannot be negative, so use $|\alpha|$ rather than $\alpha$. The formula separates the sign's effect on direction from the scaling of length.

The figure below represents $(3,4)^\top$ from Example 1 as a right triangle. Components give movements along the legs; the norm is the hypotenuse from the origin to the tip.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A vector with components three and four is the hypotenuse of a right triangle with length five](../../figures/assets/M02/M02-03-norm-triangle.svg)

<figcaption>The legs have lengths 3 and 4, and the vector has length √(3²+4²)=5. This combines two components into one length.</figcaption>
</figure>

## Core concept 3. Distance between two points is the length of their difference vector

Define Euclidean distance between $\mathbf x,\mathbf y\in\mathbb R^n$ as

\[
d(\mathbf x,\mathbf y)
=
\|\mathbf x-\mathbf y\|_2
\]

First find the difference vector $\mathbf x-\mathbf y$ from $\mathbf y$ to $\mathbf x$, then measure its length. The reverse movement is $\mathbf y-\mathbf x=-(\mathbf x-\mathbf y)$ and has the same length, so reversing the comparison order does not change distance.

Distance and dimension are different quantities. Dimension counts components, whereas distance expresses the difference between two vectors as a scalar.

The figure below connects the two positions in Exercise 2. Rather than measuring length from the origin, measure the difference vector from one endpoint to the other.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The difference between positions one minus two and four two has components minus three minus four and length five](../../figures/assets/M02/M02-03-distance-difference.svg)

<figcaption>The displacement from y to x is (-3,-4)ᵀ, and the distance is 5. Reversing direction leaves the squared components and length unchanged.</figcaption>
</figure>

## Core concept 4. Inner products connect length and angle

Let $\theta$ be the angle between nonzero vectors $\mathbf u,\mathbf v$.

Angles can be measured in radians: $\pi$ corresponds to $180^\circ$, and $\pi/2$ to $90^\circ$. The value $\cos\theta$ is the signed length obtained by projecting a unit-length direction onto the reference direction. For an acute angle, it equals the adjacent-leg length divided by the hypotenuse length in a right triangle. It is 1 for the same direction, 0 for a right angle, and -1 for opposite directions; it is negative for an obtuse angle.

The inner product satisfies

\[
\mathbf u^\top\mathbf v
=
\|\mathbf u\|_2\|\mathbf v\|_2\cos\theta
\]

Therefore,

\[
\cos\theta
=
\frac{\mathbf u^\top\mathbf v}
{\|\mathbf u\|_2\|\mathbf v\|_2}
\]

calculates the angle's cosine. Dividing the inner product by the product of both lengths removes the scaling due to length and leaves only the directional relationship. Conversely, the inner product itself multiplies the directional relationship by both vector lengths.

- A positive inner product means $0\le\theta<\frac{\pi}{2}$. At $\theta=0$, the directions agree; for $0<\theta<\frac{\pi}{2}$, the angle is acute.
- A zero inner product means $\theta=\frac{\pi}{2}$.
- A negative inner product means $\frac{\pi}{2}<\theta\le\pi$. At $\theta=\pi$, the directions are opposite; for $\frac{\pi}{2}<\theta<\pi$, the angle is obtuse.

The zero vector has no direction, so its angle and cosine similarity with another vector are undefined.

The three scenes below compare inner product signs with the same reference direction. Read the orange angle marks together with the inner product signs.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three vector pairs have positive zero and negative inner products corresponding to acute right and obtuse angles](../../figures/assets/M02/M02-03-angle-and-sign.svg)

<figcaption>Against reference vector (2,0)ᵀ, the inner product is positive for an acute angle, 0 for a right angle, and negative for an obtuse angle. This angle interpretation requires both vectors to be nonzero.</figcaption>
</figure>

## Core concept 5. A zero inner product means orthogonality

If

\[
\mathbf u^\top\mathbf v=0
\]

the vectors are orthogonal. If both are nonzero, their angle is $90^\circ$.

Orthogonality is stronger than linear independence. Nonzero orthogonal vectors are not multiples of each other and provide independent directions. We define linear independence precisely in M02-07.

The zero vector also has inner product 0 with any vector, so algebraically it is orthogonal to every vector. It has no direction, however, so neither the $90^\circ$ angle interpretation nor the claim of an independent direction applies to it.

The figure below shows the two directions in Example 2. Arrows need not align with the coordinate axes: cancellation of corresponding component products can still make their directions orthogonal.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The nonaxis vectors one two and two minus one meet at a right angle because their component products cancel](../../figures/assets/M02/M02-03-orthogonal-directions.svg)

<figcaption>The inner product of (1,2)ᵀ and (2,-1)ᵀ is 2−2=0. The right angle between these tilted directions agrees with the algebraic condition.</figcaption>
</figure>

## Core concept 6. Orthogonal projection extracts the component along one direction

For $\mathbf v\ne\mathbf 0$, the orthogonal projection of $\mathbf u$ onto the line generated by $\mathbf v$ is

\[
\operatorname{proj}_{\mathbf v}\mathbf u
=
\frac{\mathbf u^\top\mathbf v}
{\mathbf v^\top\mathbf v}
\mathbf v
\]

The fraction is the coefficient specifying how much to scale $\mathbf v$ to obtain the component of $\mathbf u$ along $\mathbf v$. The projection is a multiple of $\mathbf v$, so it belongs to $\operatorname{span}\{\mathbf v\}$.

Choose this coefficient to make the remaining displacement orthogonal to the line. With projection $c\mathbf v$, the residual is $\mathbf u-c\mathbf v$, and orthogonality requires

\[
(\mathbf u-c\mathbf v)^\top\mathbf v
=\mathbf u^\top\mathbf v-c\,\mathbf v^\top\mathbf v
=0
\]

Solving for $c$ gives $c=(\mathbf u^\top\mathbf v)/(\mathbf v^\top\mathbf v)$. For $\mathbf v\ne\mathbf 0$, the denominator is positive, determining one coefficient. The coefficient $c$ is a multiplier, while $c\mathbf v$ is the actual projection vector. Unless $\mathbf v$ has length 1, the multiplier itself is not the projection's signed length.

Define the residual vector as

\[
\mathbf r
=
\mathbf u-\operatorname{proj}_{\mathbf v}\mathbf u
\]

Then

\[
\mathbf r^\top\mathbf v=0
\]

The component left after projection is orthogonal to $\mathbf v$.

The figure below decomposes Example 3's blue vector into a green projection and a purple residual. The projection lies on the gray line, and the residual is orthogonal to that line.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Projection of three two onto the line spanned by one one gives five halves five halves and an orthogonal residual one half minus one half](../../figures/assets/M02/M02-03-projection-residual.svg)

<figcaption>Subtracting projection (5/2,5/2)ᵀ from u=(3,2)ᵀ leaves residual (1/2,-1/2)ᵀ. The coefficient 5/2, the projection vector, and its length are different quantities.</figcaption>
</figure>

## Core concept 7. Cosine similarity compares directions

For nonzero vectors, cosine similarity is

\[
\operatorname{cosim}(\mathbf u,\mathbf v)
=
\frac{\mathbf u^\top\mathbf v}
{\|\mathbf u\|_2\|\mathbf v\|_2}
\]

It ranges from $-1$ to $1$ and is unchanged by positive rescaling of the vectors.

\[
\operatorname{cosim}(2\mathbf u,5\mathbf v)
=
\operatorname{cosim}(\mathbf u,\mathbf v)
\]

The numerator's inner product acquires a factor $2\cdot5$, and the product of norms in the denominator acquires the same factor $2\cdot5$, which cancels. The two positive multipliers preserve directions. Euclidean distance, by contrast, changes with magnitude. Example 4's $\mathbf h=(1,1)^\top$ and $\mathbf a=(2,2)^\top$ point the same way and have cosine 1, but their endpoints differ, with distance $\sqrt2$. Directional similarity and distance similarity answer different questions.

Compare the tips of the two arrows pointing the same way below. Their endpoint distance, marked in orange, is nonzero, and the purple vector is orthogonal to both.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two vectors on the same ray have cosine one but nonzero endpoint distance while a third vector is perpendicular](../../figures/assets/M02/M02-03-cosine-versus-distance.svg)

<figcaption>h and a have cosine 1 but distance √2. h and b have cosine 0, so their directions are orthogonal.</figcaption>
</figure>

## Example 1. Calculate an inner product and norms

Let

\[
\mathbf u=
\begin{bmatrix}3\\4\end{bmatrix},
\qquad
\mathbf v=
\begin{bmatrix}2\\-1\end{bmatrix}
\]

Their inner product is

\[
\mathbf u^\top\mathbf v
=
3\cdot2+4(-1)
=
2
\]

Their norms are

\[
\|\mathbf u\|_2
=
\sqrt{3^2+4^2}
=
5
\]

and

\[
\|\mathbf v\|_2
=
\sqrt{2^2+(-1)^2}
=
\sqrt5
\]

## Example 2. Check orthogonality

For

\[
\mathbf u=
\begin{bmatrix}1\\2\end{bmatrix},
\qquad
\mathbf v=
\begin{bmatrix}2\\-1\end{bmatrix}
\]

we have

\[
\mathbf u^\top\mathbf v
=
1\cdot2+2(-1)
=
0
\]

The two vectors are orthogonal.

## Example 3. Project onto a vector

Let

\[
\mathbf u=
\begin{bmatrix}3\\2\end{bmatrix},
\qquad
\mathbf v=
\begin{bmatrix}1\\1\end{bmatrix}
\]

Since

\[
\mathbf u^\top\mathbf v=5,
\qquad
\mathbf v^\top\mathbf v=2
\]

the projection is

\[
\operatorname{proj}_{\mathbf v}\mathbf u
=
\frac52
\begin{bmatrix}1\\1\end{bmatrix}
=
\begin{bmatrix}5/2\\5/2\end{bmatrix}
\]

The residual is

\[
\mathbf r
=
\begin{bmatrix}3\\2\end{bmatrix}
-
\begin{bmatrix}5/2\\5/2\end{bmatrix}
=
\begin{bmatrix}1/2\\-1/2\end{bmatrix}
\]

and $\mathbf r^\top\mathbf v=0$.

## Example 4. Cosine similarity of embeddings

Let three embeddings be

\[
\mathbf h=
\begin{bmatrix}1\\1\end{bmatrix},
\qquad
\mathbf a=
\begin{bmatrix}2\\2\end{bmatrix},
\qquad
\mathbf b=
\begin{bmatrix}1\\-1\end{bmatrix}
\]

Then

\[
\operatorname{cosim}(\mathbf h,\mathbf a)=1
\]

and

\[
\operatorname{cosim}(\mathbf h,\mathbf b)=0
\]

The vector $\mathbf a$ points in the same direction as $\mathbf h$, while $\mathbf b$ is orthogonal to it.

This observation describes directional relationships in the selected representation. Concluding that two tokens have the same meaning or that the model uses the direction for predictions requires additional behavioral evaluations or intervention evidence.

## Common misconceptions

### Misconception 1. An inner product is an elementwise vector product

An elementwise product outputs a vector. An inner product adds all elementwise products to output a scalar.

### Misconception 2. A large inner product means the directions are close

An inner product also depends on both vector lengths. To compare only directions, divide by their norms to obtain cosine similarity.

### Misconception 3. Orthogonality means statistical independence

Orthogonality is a geometric relationship: the angle under the chosen inner product is $90^\circ$. Independence of random variables is a condition on a joint distribution.

### Misconception 4. High cosine similarity means the model treats the vectors as the same concept

High cosine similarity is an observation that the two measured directions are close. Conceptual identity and functional use require separate experiments.

## Exercises

### 1. Calculate an inner product

For

\[
\mathbf u=
\begin{bmatrix}2\\-1\\3\end{bmatrix},
\qquad
\mathbf v=
\begin{bmatrix}4\\2\\0\end{bmatrix}
\]

find $\mathbf u^\top\mathbf v$.

<details>
<summary>Show solution</summary>

\[
\mathbf u^\top\mathbf v
=
2\cdot4+(-1)\cdot2+3\cdot0
=
6
\]

This is the scalar sum of corresponding component products.

</details>

### 2. Norm and distance

For

\[
\mathbf x=
\begin{bmatrix}1\\-2\end{bmatrix},
\qquad
\mathbf y=
\begin{bmatrix}4\\2\end{bmatrix}
\]

find $\|\mathbf x\|_2$ and $d(\mathbf x,\mathbf y)$.

<details>
<summary>Show solution</summary>

\[
\|\mathbf x\|_2
=
\sqrt{1^2+(-2)^2}
=
\sqrt5
\]

The difference vector is

\[
\mathbf x-\mathbf y
=
\begin{bmatrix}-3\\-4\end{bmatrix}
\]

so

\[
d(\mathbf x,\mathbf y)
=
\sqrt{(-3)^2+(-4)^2}
=
5
\]

</details>

### 3. Angle ranges

Describe the angle ranges between two nonzero vectors when their inner product is positive, zero, or negative. Include the endpoints for the same and opposite directions.

<details>
<summary>Show solution</summary>

In

\[
\mathbf u^\top\mathbf v
=
\|\mathbf u\|_2\|\mathbf v\|_2\cos\theta
\]

both norms are positive. A positive inner product gives $0\le\theta<\frac{\pi}{2}$, with $\theta=0$ meaning the same direction. A zero inner product gives the right angle $\theta=\frac{\pi}{2}$. A negative inner product gives $\frac{\pi}{2}<\theta\le\pi$, with $\theta=\pi$ meaning opposite directions.

</details>

### 4. An unknown for orthogonality

Find $a$ so that

\[
\mathbf u=
\begin{bmatrix}1\\3\end{bmatrix},
\qquad
\mathbf v=
\begin{bmatrix}a\\2\end{bmatrix}
\]

are orthogonal.

<details>
<summary>Show solution</summary>

Orthogonality requires

\[
\mathbf u^\top\mathbf v
=
a+6
=
0
\]

Thus, $a=-6$.

</details>

### 5. Calculate a projection

For

\[
\mathbf u=
\begin{bmatrix}4\\3\end{bmatrix},
\qquad
\mathbf v=
\begin{bmatrix}1\\0\end{bmatrix}
\]

find $\operatorname{proj}_{\mathbf v}\mathbf u$ and the residual.

<details>
<summary>Show solution</summary>

Since

\[
\mathbf u^\top\mathbf v=4,
\qquad
\mathbf v^\top\mathbf v=1
\]

we have

\[
\operatorname{proj}_{\mathbf v}\mathbf u
=
4
\begin{bmatrix}1\\0\end{bmatrix}
=
\begin{bmatrix}4\\0\end{bmatrix}
\]

The residual is

\[
\begin{bmatrix}4\\3\end{bmatrix}
-
\begin{bmatrix}4\\0\end{bmatrix}
=
\begin{bmatrix}0\\3\end{bmatrix}
\]

Its inner product with $\mathbf v$ is 0.

</details>

### 6. Cosine and rescaling

For nonzero $\mathbf u,\mathbf v$ and $\alpha,\beta>0$, show algebraically that

\[
\operatorname{cosim}(\alpha\mathbf u,\beta\mathbf v)
=
\operatorname{cosim}(\mathbf u,\mathbf v)
\]

<details>
<summary>Show solution</summary>

The numerator is

\[
(\alpha\mathbf u)^\top(\beta\mathbf v)
=
\alpha\beta\mathbf u^\top\mathbf v
\]

and the denominator is

\[
\|\alpha\mathbf u\|_2\|\beta\mathbf v\|_2
=
\alpha\beta\|\mathbf u\|_2\|\mathbf v\|_2
\]

The factor $\alpha\beta$ cancels, leaving the original cosine similarity.

</details>

### 7. Scope of a similarity claim

Two activation vectors have observed cosine similarity $0.97$. Distinguish what follows from this result alone from what requires further evidence.

1. Their directions are close under the selected inner product.
2. The two inputs have the same meaning to the model.
3. Their Euclidean distance is small.
4. This direction causes output behavior.

<details>
<summary>Show solution</summary>

The first statement follows directly from cosine similarity's definition. The second requires a separate criterion for meaning. The third cannot be determined without vector lengths. The fourth requires interventions and controls.

</details>

## Lesson summary

- The Euclidean inner product adds corresponding component products to produce a scalar.
- A vector's inner product with itself gives its norm; the norm of a difference vector gives distance.
- Inner products connect both lengths with the angle, and an inner product of 0 means orthogonality.
- Orthogonal projection extracts a vector's component along a specified direction.
- Cosine similarity compares directions; it does not guarantee identical meaning or causal use.

## Pass criteria

You pass if you can answer these questions without consulting the material:

- Can you calculate inner products, norms, and distances for small vectors?
- Can you use an inner product's sign to identify the angle type?
- Can you write the orthogonality condition as an equation?
- Can you calculate a projection onto one vector and its orthogonal residual?
- Can you explain the scope of cosine similarity's interpretation?

## Next lesson

- [M02-04 Matrices and matrix multiplication](M02-04-matrices-matrix-multiplication.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Inner products, norms, distances, and angle conditions are defined.
- [x] The undefined angle and cosine for the zero vector are stated.
- [x] Projections and orthogonal residuals are calculated.
- [x] Every exercise has a solution.
- [x] Cosine observations are distinguished from model-use claims.
- [x] The glossary and notation rules are followed.
- [x] No matrix projection beyond the prerequisites is required.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
