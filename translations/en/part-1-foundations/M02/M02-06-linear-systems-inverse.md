---
id: "M02-06"
title: "Linear systems and inverse matrices"
part: 1
stage: "M02"
status: "complete"
prerequisites:
  - "M02-04"
  - "M02-05"
estimated_time: "110~135 minutes"
---

# M02-06. Linear systems and inverse matrices

## Why this lesson matters

Combining several linear equations into the matrix equation

\[
\mathbf A\mathbf x=\mathbf b
\]

connects solving a system to the properties of a linear transformation. A solution exists when the transformation $\mathbf A$ has an input that produces the target $\mathbf b$. Whether there is one solution, several, or none depends on how the matrix preserves input directions or maps them onto one another.

An inverse matrix reverses the transformation of an invertible square matrix. Not every matrix has an inverse, and numerical computation does not require explicitly forming an inverse to solve a linear system.

## Learning objectives

By the end of this lesson, you should be able to:

- Express a system of linear equations as $\mathbf A\mathbf x=\mathbf b$.
- Solve a small system by applying elementary row operations to an augmented matrix.
- Distinguish one solution, no solution, and infinitely many solutions in row echelon form.
- Explain the definition of an inverse matrix and the conditions for its existence.
- Find a $2\times2$ inverse and check a solution.
- Interpret an inverse as reversing a transformation and judge when it applies.

## Prerequisite check

- Prerequisite lesson: [M02-04 Matrices and matrix multiplication](M02-04-matrices-matrix-multiplication.md)
- Prerequisite lesson: [M02-05 Matrices as linear transformations](M02-05-matrix-as-linear-transformation.md)
- Check question: Can you expand a matrix–vector product into component equations?
- Check question: Can you explain why an identity matrix leaves a vector unchanged?

Review the prerequisite lessons first if matrix multiplication or linear transformations are unclear.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| $\mathbf A\mathbf x=\mathbf b$ | `A x equals b` | A system of linear equations in an unknown vector | $\mathbf A\in\mathbb R^{m\times n}$ |
| $[\mathbf A\mid\mathbf b]$ | `the augmented matrix A bar b` | The coefficient matrix and right-hand side placed side by side | $m\times(n+1)$ |
| pivot | `pivot` | The position of the first entry that is not 0 in a row of a row echelon form | Indicates a constraint on the solution. |
| Free variable | `free variable` | An unknown in a column without a pivot | Its value can be chosen freely. |
| $\mathbf A^{-1}$ | `A inverse` | A matrix reversing the linear transformation of $\mathbf A$ | Exists only for an invertible square matrix |
| Singular matrix | `singular matrix` | A square matrix with no inverse | Some input directions overlap or disappear. |

## Core concept 1. A system of equations becomes a matrix equation

The system

\[
\begin{aligned}
a_{11}x_1+\cdots+a_{1n}x_n&=b_1\\
\vdots\qquad\quad&\ \vdots\\
a_{m1}x_1+\cdots+a_{mn}x_n&=b_m
\end{aligned}
\]

is equivalent to

\[
\mathbf A\mathbf x=\mathbf b
\]

The inner product of row $i$ of $\mathbf A$ with $\mathbf x$ equals $b_i$.

From the column view,

\[
x_1\mathbf a_1+\cdots+x_n\mathbf a_n=\mathbf b
\]

Solving the system means finding coefficients that combine the columns of $\mathbf A$ into $\mathbf b$.

## Core concept 2. Elementary row operations preserve the solution set

The augmented matrix

\[
[\mathbf A\mid\mathbf b]
\]

allows three operations.

1. Swap two rows.
2. Multiply a row by a scalar other than 0.
3. Add a scalar multiple of another row to a row.

Apply each operation to the entire row, including the right-hand side, not just the coefficients. Swapping rows changes only the equation order. Multiplication by a number other than 0 can be reversed by dividing by that number. After adding a multiple of another row, that other row is still present, so subtracting the same multiple restores the original row. Each operation is reversible, so the original and transformed equations have the same solutions. Multiplication by 0 would erase an equation irreversibly and is not allowed.

In row echelon form, rows whose entries are all 0 are placed at the bottom, and the first entry that is not 0 in each lower row lies to the right of the first entry that is not 0 in the row above it. That first entry is a pivot, and entries below it in the same column are 0. In this form, solve for pivot unknowns starting at the bottom and substitute into the rows above. This procedure is Gaussian elimination.

The figure below compares the row elimination in Example 1 through the intersection of two lines. The second equation's line changes, but the point satisfying it together with the first equation stays the same.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Coordinate plots before and after row elimination sharing the solution thirteen sevenths, eleven sevenths](../../figures/assets/M02/M02-06-row-operation-intersection.svg)

<figcaption>Subtracting 3 times the first row from the second makes the second line horizontal. The common intersection is preserved, so the solution computed from the new equations also satisfies both original equations.</figcaption>
</figure>

## Core concept 3. A linear system has three possible solution cases

If elimination produces a row

\[
\begin{bmatrix}
0&\cdots&0&\mid&c
\end{bmatrix},
\qquad
c\ne0
\]

then $0=c$ is a contradiction, so no solution exists.

With no contradiction, a pivot in every unknown column gives one solution. With no contradiction but an unknown column lacking a pivot, there is a free variable and infinitely many solutions.

Once the values of other unknowns in its row are chosen, a pivot unknown can be computed from that equation. With a pivot for every unknown, working upward from the last row determines each uniquely. With free variables, choose their values first and compute the remaining pivot unknowns. Distinct real values of a free variable give infinitely many distinct solutions when the system is consistent. The expressions $y=t$, $x=3-2t$ in Example 3 illustrate this case.

This classification concerns exact linear systems over the real numbers. Floating-point calculations require a tolerance for deciding whether a value close to 0 should be treated as 0.

The figure below represents the solution sets of two-variable equations as the common parts of lines. A free variable corresponds to being able to choose different solutions along the shared line, as on the right.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Intersecting, parallel, and coincident lines showing one, zero, and infinitely many common solutions](../../figures/assets/M02/M02-06-three-solution-sets.svg)

<figcaption>One intersection gives one solution; distinct parallel lines give none. If both equations describe the same line, every point on that line is a solution, and a parameter t can specify different points.</figcaption>
</figure>

## Core concept 4. An inverse gives the identity on both sides

For a square matrix $\mathbf A\in\mathbb R^{n\times n}$, if a matrix $\mathbf A^{-1}$ exists such that

\[
\mathbf A^{-1}\mathbf A
=
\mathbf A\mathbf A^{-1}
=
\mathbf I_n
\]

then $\mathbf A$ is called invertible.

If the inverse exists, multiplying both sides of

\[
\mathbf A\mathbf x=\mathbf b
\]

on the left by $\mathbf A^{-1}$ gives

\[
\mathbf x
=
\mathbf A^{-1}\mathbf b
\]

There is exactly one solution for every $\mathbf b\in\mathbb R^n$.

Associativity gives $\mathbf A^{-1}(\mathbf A\mathbf x)=(\mathbf A^{-1}\mathbf A)\mathbf x=\mathbf x$. Substituting the candidate $\mathbf A^{-1}\mathbf b$ into the original equation gives $\mathbf A(\mathbf A^{-1}\mathbf b)=\mathbf b$, so a solution does exist. Left multiplication by $\mathbf A^{-1}$ forces every solution to equal that candidate, proving uniqueness. The two identity relations guarantee input recovery and attainment of the output target, respectively.

The figure below applies the matrix from Example 4 and its inverse in succession using equally scaled coordinates. The second stage, returning from the output to the original input, illustrates $\mathbf A^{-1}\mathbf A=\mathbf I$.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Equal-scale coordinate plots showing input two one mapped to five three and restored by the inverse](../../figures/assets/M02/M02-06-inverse-round-trip.svg)

<figcaption>A sends the input (2,1) to (5,3), and A inverse restores (2,1). Applying an inverse to the middle output is another linear transformation, not simple division of components.</figcaption>
</figure>

## Core concept 5. A single scalar condition determines a $2\times2$ inverse

For

\[
\mathbf A=
\begin{bmatrix}
a&b\\
c&d
\end{bmatrix}
\]

if

\[
ad-bc\ne0
\]

then

\[
\mathbf A^{-1}
=
\frac{1}{ad-bc}
\begin{bmatrix}
d&-b\\
-c&a
\end{bmatrix}
\]

Multiplication by the numerator matrix gives

\[
\begin{bmatrix}a&b\\c&d\end{bmatrix}
\begin{bmatrix}d&-b\\-c&a\end{bmatrix}
=\begin{bmatrix}ad-bc&-ab+ba\\cd-dc&ad-bc\end{bmatrix}
=(ad-bc)\mathbf I_2
\]

The reverse multiplication order gives the same result. If $ad-bc\ne0$, dividing by this number therefore makes both products the identity.

When $ad-bc=0$, the problem is not merely that the formula's denominator cannot be used. If the first row $(a,b)$ is nonzero, $\mathbf A$ sends the nonzero input $(b,-a)^\top$ to the zero vector. If the first row is zero and the second row $(c,d)$ is nonzero, $(d,-c)^\top$ serves the same role. If every entry is 0, every input maps to the zero vector. In each case, different inputs reach the same output, so no inverse can recover them. M02-10 interprets $ad-bc$ as a determinant.

After using the formula, verify it by multiplying to check

\[
\mathbf A\mathbf A^{-1}=\mathbf I_2
\]

The figure below shows the singular matrix in Exercise 5 eliminating a nonzero input direction. The inability to distinguish two inputs from one output explains the absence of an inverse.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Singular matrix mapping distinct inputs zero and minus two one to the same zero output](../../figures/assets/M02/M02-06-singular-collapse.svg)

<figcaption>Matrix B sends both (−2,1) and the zero vector to the zero vector. The possible outputs also lie on one line. Equal input and output dimensions alone therefore do not guarantee input recovery.</figcaption>
</figure>

## Core concept 6. Invertibility means a linear transformation loses no information

If $T(\mathbf x)=\mathbf A\mathbf x$ is invertible, the output $\mathbf y$ uniquely determines the input through

\[
\mathbf x=\mathbf A^{-1}\mathbf y
\]

If two different inputs reach the same output, an inverse transformation cannot decide which input to return. The same issue arises when an input direction disappears into the zero vector. M02-08 treats the relation between kernel and invertibility precisely.

For invertible square matrices $\mathbf A,\mathbf B$ of the same size, undo the composition in reverse order:

\[
(\mathbf A\mathbf B)^{-1}
=
\mathbf B^{-1}\mathbf A^{-1}
\]

Undo $\mathbf A$, applied later, first; undo $\mathbf B$, applied first, last.

Multiplication checks this: $\mathbf A\mathbf B\mathbf B^{-1}\mathbf A^{-1}=\mathbf A\mathbf I\mathbf A^{-1}=\mathbf I$. The reverse product gives $\mathbf B^{-1}\mathbf A^{-1}\mathbf A\mathbf B=\mathbf I$ as well. This groups adjacent inverse pairs by associativity without exchanging the factor order.

The figure below retains the intermediate state and follows the same path backward. Undoing A, which was applied last, must come first to reach the intermediate vector Bx.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Forward coordinate stages under B then A and reverse arrows applying A inverse then B inverse](../../figures/assets/M02/M02-06-reverse-composition.svg)

<figcaption>The upper arrows apply B and then A; the lower arrows recover the input from right to left. The inverse of the composition AB therefore applies A inverse and then B inverse.</figcaption>
</figure>

## Core concept 7. Solving a linear system does not require forming the inverse

The expression

\[
\mathbf x=\mathbf A^{-1}\mathbf b
\]

shows what invertibility means. To compute $\mathbf x$, a computer can solve $\mathbf A\mathbf x=\mathbf b$ directly using Gaussian elimination or a factorization method. Forming the entire inverse and then multiplying can increase computation and error.

One right-hand side $\mathbf b$ requires one solution vector. In contrast, the columns of an inverse collect the solutions of $\mathbf A\mathbf x=\mathbf e_i$ for different standard right-hand sides. Solving one right-hand side does not require first constructing the inverse transformation for all of them.

A rectangular matrix has no two-sided inverse. A solution or a least-squares approximation may exist, but such a problem is not handled with the formula for a square inverse.

The figure below compares the outputs needed to solve one right-hand side with those needed to construct every column of an inverse.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two computational routes comparing a single right-hand-side solve with assembling every inverse column](../../figures/assets/M02/M02-06-one-right-hand-side.svg)

<figcaption>The upper route finds one solution x for the given b. The lower route collects solutions for all standard right-hand sides to form an inverse; that route is not required when the needed output is only one solution.</figcaption>
</figure>

## Example 1. Finding a unique solution by row elimination

The augmented matrix of

\[
\begin{aligned}
x+2y&=5\\
3x-y&=4
\end{aligned}
\]

is

\[
\left[
\begin{array}{cc|c}
1&2&5\\
3&-1&4
\end{array}
\right]
\]

Subtracting 3 times the first row from the second gives

\[
\left[
\begin{array}{cc|c}
1&2&5\\
0&-7&-11
\end{array}
\right]
\]

Thus

\[
y=\frac{11}{7}
\]

and substitution into the first equation gives

\[
x
=
5-\frac{22}{7}
=
\frac{13}{7}
\]

Both unknown columns have pivots, so the solution is unique.

## Example 2. No solution

For

\[
\begin{aligned}
x+y&=2\\
2x+2y&=5
\end{aligned}
\]

subtracting 2 times the first equation from the second gives

\[
0=1
\]

The augmented matrix has a row

\[
\begin{bmatrix}0&0&\mid&1\end{bmatrix}
\]

The left-hand sides require the same line relation, but the right-hand sides are inconsistent, so there is no solution.

## Example 3. Infinitely many solutions

In

\[
\begin{aligned}
x+2y&=3\\
2x+4y&=6
\end{aligned}
\]

the second equation is 2 times the first. Elimination makes the second row all 0. Taking $y=t$ as a free variable gives

\[
x=3-2t
\]

and hence

\[
\begin{bmatrix}x\\y\end{bmatrix}
=
\begin{bmatrix}3\\0\end{bmatrix}
+
t
\begin{bmatrix}-2\\1\end{bmatrix},
\qquad
t\in\mathbb R
\]

The solution set is a line through one point, extending in one direction.

## Example 4. Checking a solution using an inverse

Let

\[
\mathbf A=
\begin{bmatrix}
2&1\\
1&1
\end{bmatrix},
\qquad
\mathbf b=
\begin{bmatrix}5\\3\end{bmatrix}
\]

Since $ad-bc=2\cdot1-1\cdot1=1$,

\[
\mathbf A^{-1}
=
\begin{bmatrix}
1&-1\\
-1&2
\end{bmatrix}
\]

Then

\[
\mathbf x
=
\mathbf A^{-1}\mathbf b
=
\begin{bmatrix}
1&-1\\
-1&2
\end{bmatrix}
\begin{bmatrix}5\\3\end{bmatrix}
=
\begin{bmatrix}2\\1\end{bmatrix}
\]

Substituting into the original equation gives

\[
\mathbf A\mathbf x
=
\begin{bmatrix}5\\3\end{bmatrix}
=
\mathbf b
\]

so the solution is correct.

## Common misconceptions

### Misconception 1. Every square matrix has an inverse

Being square is necessary for an inverse. A square matrix is singular if column directions overlap or an input direction disappears.

### Misconception 2. Equal numbers of equations and unknowns guarantee one solution

Redundant or contradictory equations can give infinitely many solutions or none. Check the pivot structure.

### Misconception 3. $\mathbf A\mathbf x=\mathbf b$ is always solved as $\mathbf x=\mathbf A^{-1}\mathbf b$

$\mathbf A^{-1}$ exists only for an invertible square matrix. Numerical computation uses algorithms that solve the linear system directly.

### Misconception 4. Equal output and input dimensions guarantee information preservation

A singular matrix with equal dimensions can send different inputs to the same output. Shape alone does not determine invertibility.

## Exercises

### 1. Writing a matrix equation

Express the following system as $\mathbf A\mathbf x=\mathbf b$.

\[
\begin{aligned}
2x-y&=1\\
x+3y&=8
\end{aligned}
\]

<details>
<summary>Show solution</summary>

\[
\begin{bmatrix}
2&-1\\
1&3
\end{bmatrix}
\begin{bmatrix}x\\y\end{bmatrix}
=
\begin{bmatrix}1\\8\end{bmatrix}
\]

The coefficients of each equation form one matrix row.

</details>

### 2. Row elimination

Solve the system in Exercise 1 by row elimination.

<details>
<summary>Show solution</summary>

The augmented matrix is

\[
\left[
\begin{array}{cc|c}
2&-1&1\\
1&3&8
\end{array}
\right]
\]

Swap the first and second rows, then subtract 2 times the new first row from the second:

\[
\left[
\begin{array}{cc|c}
1&3&8\\
0&-7&-15
\end{array}
\right]
\]

Therefore,

\[
y=\frac{15}{7},
\qquad
x=8-3\cdot\frac{15}{7}
=
\frac{11}{7}
\]

</details>

### 3. Determining the number of solutions

Determine whether the system represented by this row echelon augmented matrix has one solution, no solution, or infinitely many solutions.

\[
\left[
\begin{array}{ccc|c}
1&0&2&3\\
0&1&-1&4\\
0&0&0&0
\end{array}
\right]
\]

<details>
<summary>Show solution</summary>

There is no contradictory row, and the third unknown column has no pivot. Thus $x_3$ can be a free variable, giving infinitely many solutions.

Setting $x_3=t$ gives

\[
x_1=3-2t,
\qquad
x_2=4+t
\]

</details>

### 4. A $2\times2$ inverse

Find the inverse of

\[
\mathbf A=
\begin{bmatrix}
3&1\\
2&1
\end{bmatrix}
\]

and verify $\mathbf A\mathbf A^{-1}=\mathbf I_2$.

<details>
<summary>Show solution</summary>

Since

\[
ad-bc=3\cdot1-1\cdot2=1
\]

we have

\[
\mathbf A^{-1}
=
\begin{bmatrix}
1&-1\\
-2&3
\end{bmatrix}
\]

Multiplication gives

\[
\mathbf A\mathbf A^{-1}
=
\begin{bmatrix}
3&1\\
2&1
\end{bmatrix}
\begin{bmatrix}
1&-1\\
-2&3
\end{bmatrix}
=
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
\]

</details>

### 5. Identifying a singular matrix

Determine whether

\[
\mathbf B=
\begin{bmatrix}
1&2\\
2&4
\end{bmatrix}
\]

has an inverse, and find two different inputs that reach the same output.

<details>
<summary>Show solution</summary>

Since

\[
ad-bc=1\cdot4-2\cdot2=0
\]

there is no inverse.

\[
\mathbf B
\begin{bmatrix}0\\0\end{bmatrix}
=
\begin{bmatrix}0\\0\end{bmatrix}
\]

and

\[
\mathbf B
\begin{bmatrix}-2\\1\end{bmatrix}
=
\begin{bmatrix}0\\0\end{bmatrix}
\]

Different inputs reach the same output, so an inverse transformation cannot be defined.

</details>

### 6. The inverse of a composition

For invertible matrices $\mathbf A,\mathbf B$, use associativity of matrix multiplication to show

\[
(\mathbf A\mathbf B)(\mathbf B^{-1}\mathbf A^{-1})
=
\mathbf I
\]

<details>
<summary>Show solution</summary>

\[
\begin{aligned}
(\mathbf A\mathbf B)(\mathbf B^{-1}\mathbf A^{-1})
&=
\mathbf A(\mathbf B\mathbf B^{-1})\mathbf A^{-1}\\
&=
\mathbf A\mathbf I\mathbf A^{-1}\\
&=
\mathbf A\mathbf A^{-1}\\
&=
\mathbf I
\end{aligned}
\]

The reverse product is also the identity by the same argument, so $(\mathbf A\mathbf B)^{-1}=\mathbf B^{-1}\mathbf A^{-1}$.

</details>

### 7. Claims about recovering inputs from a model computation

Suppose the weights are $\mathbf W\in\mathbb R^{64\times128}$ and $\mathbf h=\mathbf W\mathbf x$.

1. Can $\mathbf W^{-1}$ be defined?
2. Can shape alone establish unique recovery of $\mathbf x$ from $\mathbf h$?
3. State the additional algebraic properties to investigate.

<details>
<summary>Show solution</summary>

$\mathbf W$ is not square, so the two-sided inverse $\mathbf W^{-1}$ cannot be defined.

The homogeneous system $\mathbf W\mathbf z=\mathbf 0$ has 128 unknowns and 64 equations. There are at most 64 pivots, so free variables exist and there is a solution $\mathbf z\ne\mathbf 0$. Hence $\mathbf W\mathbf x=\mathbf W(\mathbf x+\mathbf z)$, and it is impossible to recover every $\mathbf x$ uniquely from $\mathbf h$.

Investigate the kernel to find which directions disappear and the rank to find the number of possible output directions. M02-08 introduces both concepts.

</details>

## Lesson summary

- A linear system can be written as $\mathbf A\mathbf x=\mathbf b$, and its solutions give the coefficients of a column linear combination.
- Elementary row operations preserve the solution set and reveal pivots and free variables.
- Contradictory rows and pivot structure distinguish no solution, one solution, and infinitely many solutions.
- An inverse matrix reverses the linear transformation of an invertible square matrix.
- Numerical computation solves a linear system directly rather than forming the entire inverse.
- Rectangular and singular matrices have no two-sided inverse.

## Pass criteria

You pass if you can answer these questions without consulting the material.

- Can you convert between a system of equations and its augmented matrix?
- Can you solve a small system by row elimination?
- Can you determine the number of solutions from row echelon form?
- Can you explain the inverse definition and the conditions for its existence?
- Can you find and check a $2\times2$ inverse?
- Can you distinguish inverse matrices from practical linear-system solving?

## Next lesson

- [M02-07 Linear independence, bases, and dimension](M02-07-linear-independence-basis-dimension.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Linear systems, augmented matrices, and column linear combinations are connected.
- [x] The three solution cases are distinguished through examples.
- [x] The inverse definition and existence conditions are stated.
- [x] A $2\times2$ computation and verification are included.
- [x] Every exercise has a solution.
- [x] Recoverability is distinguished from claims based on shape alone.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
