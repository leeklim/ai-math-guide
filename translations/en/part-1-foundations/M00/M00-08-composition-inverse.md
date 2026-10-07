---
id: "M00-08"
title: "Function composition and inverse functions"
part: 1
stage: "M00"
status: "complete"
prerequisites:
  - "M00-03"
  - "M00-07"
estimated_time: "90~110 minutes"
---

# M00-08. Function composition and inverse functions

## Why this lesson matters

A neural network applies functions in sequence. The output of the first layer becomes the input to the next, and this process continues through the final layer. Function composition expresses the structure of the whole model and the positions of intermediate activations in one formula.

\[
f=f_L\circ f_{L-1}\circ\cdots\circ f_1
\]

Misreading the order of the composition symbols reverses the actual computation. Inverse functions require similar care. To recover an input from an output, a function must not merge different inputs into the same output, and the output range must also be appropriate.

## Learning objectives

After this lesson, you should be able to:

- Read $(f\circ g)(x)=f(g(x))$ in the order of computation.
- Check the input and output ranges required for two functions to compose.
- Show by calculation that changing composition order can change the result.
- Explain the differences among injective, surjective, and bijective functions.
- Find the inverse of a simple function and check it by composing in both directions.
- Express neural-network layer computations as function composition.

## Prerequisite check

- Prerequisite lesson: [M00-03 Function inputs and outputs](M00-03-functions-input-output.md)
- Prerequisite lesson: [M00-07 Sets, conditions, and logic](M00-07-sets-conditions-logic.md)

Check whether you can answer these questions.

1. Can you state the roles of $A$ and $B$ in $f:A\to B$?
2. Can you explain why $P\Rightarrow Q$ and $Q\Rightarrow P$ are different claims?

The conditions for an inverse function involve its domain, codomain, and correspondences in both directions.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| $f\circ g$ | `f composed with g` | A function that applies $g$ and then $f$ | The output of $g$ must be an input allowed by $f$ |
| $(f\circ g)(x)$ | `f composed with g at x` | $f(g(x))$ | Calculate the rightmost function first |
| $\operatorname{id}_A$ | `the identity on A` | A function returning its input unchanged | $\operatorname{id}_A(x)=x$ |
| $f^{-1}$ | `f inverse` | A function returning the output of $f$ to the original input | The function must be bijective on the specified domain and codomain |
| injective | `injective` | Different inputs have different outputs | Also called one-to-one |
| surjective | `surjective` | Every element of the codomain occurs as an output | The range equals the codomain |
| bijective | `bijective` | Both injective and surjective | An inverse function exists |

## Core concept 1. Composition feeds one output into the next function

Suppose the two functions are

\[
g:A\to B,\qquad f:B\to C
\]

The function $g$ takes an input from $A$ to a value in $B$, and $f$ takes that value to a value in $C$. Combining these steps into one function gives

\[
f\circ g:A\to C
\]

The definition is

\[
(f\circ g)(x)=f(g(x))
\]

Calculation proceeds from right to left.

1. Apply $g$ to the input $x$.
2. Apply $f$ to the result $g(x)$.

The reading order of the symbols may seem different from the calculation order, so calculate from the innermost parentheses outward.

### Calculate with small numbers

Let

\[
g(x)=x+1,\qquad f(x)=2x
\]

For $x=3$,

\[
g(3)=4
\]

and

\[
f(g(3))=f(4)=8
\]

Therefore,

\[
(f\circ g)(3)=8
\]

In the next figure, the intermediate value 4 becomes the input to the next function, f.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Input three goes through g adding one to become four, then through f multiplying by two to become eight](../../figures/assets/M00/M00-08-composition-flow.svg)

<figcaption>From left to right, calculate g first and then f. Although f is written first in the composition expression, it is the final computational step.</figcaption>
</figure>

## Core concept 2. Composition requires compatible ranges

To pass the output of $g:A\to B$ to $f:C\to D$, the value $g(x)$ must belong to $C$, the domain of $f$. Typically, if

\[
B\subseteq C
\]

then $f(g(x))$ can be calculated for every $x\in A$.

This is a sufficient condition ensuring that $f$ accepts any value that $g$ produces. What is required is that the range, the actual outputs of $g$, lies in $C$. Even if the entire declared codomain $B$ is not contained in $C$, composition is possible if all actual outputs of $g$ belong to $C$. If only some outputs belong to $C$, restrict the composition's domain to the inputs producing those outputs.

For example, let

\[
g:\mathbb R\to\mathbb R,\qquad g(x)=x-2
\]

\[
f:(0,\infty)\to\mathbb R,\qquad f(u)=\log u
\]

The expression $f(g(x))=\log(x-2)$ is defined only when

\[
x-2>0
\]

The composition's domain is therefore restricted to

\[
x>2
\]

Rather than merely joining formulas, check whether each intermediate output is an allowed input to the next function.

The next figure aligns x with the intermediate value u obtained by subtracting 2, using a number line below it.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Subtracting two aligns the boundary x equal two with u equal zero, and only x greater than two produces positive inputs allowed by log](../../figures/assets/M00/M00-08-composition-compatible-range.svg)

<figcaption>Working backward from log's allowed inputs u&gt;0 gives the original input range x&gt;2. The boundary x=2 produces u=0 and is excluded.</figcaption>
</figure>

## Core concept 3. Changing composition order changes the function

For

\[
g(x)=x+1,\qquad f(x)=2x
\]

we have

\[
(f\circ g)(x)=f(x+1)=2(x+1)=2x+2
\]

Reversing the order gives

\[
(g\circ f)(x)=g(2x)=2x+1
\]

The results differ. In this example,

\[
f\circ g\ne g\circ f
\]

Function composition is not commutative in general.

The next figure passes the same input 3 through both calculation orders and compares the intermediate values and results.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Adding one then multiplying by two sends three through four to eight, but multiplying by two then adding one sends three through six to seven](../../figures/assets/M00/M00-08-composition-order-comparison.svg)

<figcaption>Changing the order changes the intermediate value. On the left, 4 is multiplied by 2; on the right, 1 is added to 6. The results are 8 and 7, respectively.</figcaption>
</figure>

For a composition of three functions, changing the grouping of parentheses gives the same result as long as the application order stays the same.

\[
h\circ(f\circ g)=(h\circ f)\circ g
\]

This is the associative law. Both sides apply the functions in the order $g$, $f$, $h$.

Expanding both expressions at an input $x$ gives $h(f(g(x)))$. Moving the parentheses changes which two functions we name as a single composite function, without changing the order in which the functions are applied to each input.

## Core concept 4. An identity function returns its input unchanged

The identity function on a set $A$ is defined by

\[
\operatorname{id}_A:A\to A
\]

\[
\operatorname{id}_A(x)=x
\]

For $f:A\to B$,

\[
\operatorname{id}_B\circ f=f
\]

\[
f\circ\operatorname{id}_A=f
\]

An identity function does not alter how the composed function acts.

In the first expression, the output of $f$ belongs to $B$, so $\operatorname{id}_B$ returns that output unchanged. In the second, $\operatorname{id}_A$ passes the input $x$ unchanged to $f$. The subscript identifies the set containing the values that the identity function preserves.

In the next figure, check which set supplies the value to the identity function depending on whether it is before or after f.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Identity on A preserves x before applying f, and identity on B preserves f of x after applying f](../../figures/assets/M00/M00-08-identity-placement.svg)

<figcaption>The identity function on the upper path passes on an input from A unchanged; the one on the lower path passes on an output in B unchanged. Both paths produce the same value as the original f.</figcaption>
</figure>

## Core concept 5. An inverse function reverses inputs and outputs

The inverse of $f:A\to B$ is a function

\[
f^{-1}:B\to A
\]

satisfying both conditions

\[
f^{-1}\circ f=\operatorname{id}_A
\]

\[
f\circ f^{-1}=\operatorname{id}_B
\]

The first says that applying $f$ to an input in $A$ and then applying $f^{-1}$ returns the original input.

\[
f^{-1}(f(x))=x
\]

The second says that applying $f^{-1}$ to a value in $B$ and then applying $f$ returns the original value.

\[
f(f^{-1}(y))=y
\]

Check both directions before calling a function an inverse on the specified domain and codomain.

The next figure shows how to reverse the calculations in the later linear-expression example f(x)=3x−2.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The forward path multiplies input two by three then subtracts two to produce four, while the inverse adds two to four then divides by three to recover two](../../figures/assets/M00/M00-08-inverse-reversed-operations.svg)

<figcaption>Undo the last forward operation, subtracting 2, first; undo the first operation, multiplying by 3, afterward. The starting and ending points also exchange roles as the original output and input.</figcaption>
</figure>

### $f^{-1}(x)$ is not a reciprocal

\[
f^{-1}(x)
\]

is a value of the inverse function.

\[
\frac1{f(x)}
\]

is the reciprocal of a function value. Both use a superscript $-1$, but their objects and operations differ.

The next figure separates returning output 7 to its original input from taking the reciprocal of 7.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![For f of x equal two x plus one, inverse maps output seven back to input three whereas taking the reciprocal gives one seventh](../../figures/assets/M00/M00-08-inverse-vs-reciprocal.svg)

<figcaption>For f(x)=2x+1, f⁻¹(7)=3 recovers the input. In contrast, 1/f(3)=1/7 treats the output as a number and takes its reciprocal.</figcaption>
</figure>

## Core concept 6. An inverse function requires a bijection

### Injective functions

Calling $f:A\to B$ injective means that different inputs do not merge into the same output. In logical notation,

\[
f(x_1)=f(x_2)\Rightarrow x_1=x_2
\]

Injectivity is necessary to identify a unique original input from an output.

### Surjective functions

Calling $f:A\to B$ surjective means that every element of the codomain $B$ occurs as an output.

\[
\forall y\in B,\quad
\exists x\in A:\ f(x)=y
\]

For a surjective function, the range equals the codomain. If a value in the codomain is never reached, $f^{-1}$ cannot be defined at that value.

### Bijective functions

A function that is both injective and surjective is bijective. If $f:A\to B$ is bijective, an inverse from all of $B$ to $A$ exists.

Injectivity ensures that no output corresponds to more than one input. Surjectivity ensures that each output in the codomain corresponds to at least one input. Together, they determine exactly one original input for each value in $B$. Taking that input as the output of the inverse satisfies the function requirement from M00-03: each allowed input must determine one output.

An injective function can be given an inverse by restricting its codomain to its range. Thus, state both the domain and codomain when discussing whether an inverse exists.

The next figure distinguishes two problems that arise when tracing a value backward to its original source.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A merged output has two possible sources, an unreached codomain value has no source, and a bijection gives every output exactly one source so all arrows can be reversed](../../figures/assets/M00/M00-08-bijection-inverse-conditions.svg)

<figcaption>At the top, output 4 has two sources, so uniqueness fails. In the middle, codomain element c has no source. At the bottom, every output has exactly one source, so the reverse correspondence is also a function.</figcaption>
</figure>

## Example 1. Find a composition formula

### Problem

For

\[
g(x)=x^2,\qquad f(u)=3u-1
\]

calculate $(f\circ g)(x)$.

### Solution

Apply $g$ first.

\[
g(x)=x^2
\]

Substitute the result into the input $u$ of $f$.

\[
f(g(x))
=
3g(x)-1
\]

\[
=
3x^2-1
\]

Therefore,

\[
(f\circ g)(x)=3x^2-1
\]

## Example 2. Find the inverse of a linear expression

### Problem

Find and check the inverse of

\[
f:\mathbb R\to\mathbb R,\qquad f(x)=3x-2
\]

### Solution

Write the output as $y$.

\[
y=3x-2
\]

Solve for $x$ in terms of $y$. Adding $2$ to both sides gives

\[
y+2=3x
\]

and dividing both sides by $3$ gives

\[
x=\frac{y+2}{3}
\]

Using $x$ as the input symbol again gives

\[
f^{-1}(x)=\frac{x+2}{3}
\]

In the last expression, $x$ names the value passed to the inverse; it occupies the place held by the original output $y$. Writing $f^{-1}(y)=(y+2)/3$ describes the same inverse. Renaming the input variable does not change its role of returning the original output to the original input.

Check the first direction.

\[
f^{-1}(f(x))
=
\frac{(3x-2)+2}{3}
=x
\]

Check the second direction as well.

\[
f(f^{-1}(y))
=
3\left(\frac{y+2}{3}\right)-2
=y
\]

Both compositions give the identity on their respective domains, confirming the inverse.

## Example 3. Obtain an inverse by restricting the domain

Consider

\[
f(x)=x^2
\]

as $f:\mathbb R\to[0,\infty)$. It is not injective.

\[
f(2)=f(-2)=4
\]

The output $4$ cannot determine whether its input was $2$ or $-2$, so no inverse exists.

Restricting the domain to $[0,\infty)$ removes the merging of different negative and positive inputs.

\[
f:[0,\infty)\to[0,\infty),\qquad f(x)=x^2
\]

This function is bijective, with inverse

\[
f^{-1}(y)=\sqrt y
\]

Restricting the domain selects part of a function. Even the same formula $x^2$ may or may not have an inverse depending on its domain and codomain.

## Example 4. Read a neural network as function composition

Suppose three layers are connected as follows.

\[
h_1=f_1(x)
\]

\[
h_2=f_2(h_1)
\]

\[
y=f_3(h_2)
\]

Substituting the intermediate variables gives

\[
y=f_3(f_2(f_1(x)))
\]

or, in composition notation,

\[
y=(f_3\circ f_2\circ f_1)(x)
\]

Apply $f_1$ to the input first and $f_3$ last. Activation $h_1$ is the first step's output in the overall composition, and $h_2$ is the second step's output.

If any layer sends multiple inputs to the same output, the whole model may fail to recover all information from before that step. The ReLU function

\[
\operatorname{ReLU}(x)=\max(0,x)
\]

sends every negative input to $0$, so it is not injective over all real numbers.

## Example 5. Distinguish reconstruction from an inverse function

Suppose a decoder $d$ reconstructs some properties of the input with high accuracy from dataset activations $h=f(x)$.

\[
d(f(x))\approx x
\]

may be observed on limited data. This result means that $d$ approximately reconstructed the input under the selected data and error criterion.

This observation alone does not establish $d=f^{-1}$. A global inverse requires checking composition in both directions, the output range, and uniqueness across the entire domain. Reconstructing some properties also differs from reconstructing the entire original input.

## Common misconceptions

### Misconception 1. $(f\circ g)(x)$ calculates $f$ first

The definition is

\[
(f\circ g)(x)=f(g(x))
\]

Calculate the inner expression $g(x)$ first.

### Misconception 2. Composition order can be exchanged as in multiplication

Composition order changes the intermediate value. Whether $f\circ g$ equals $g\circ f$ requires a separate calculation.

### Misconception 3. $f^{-1}(x)=1/f(x)$

$f^{-1}$ is a function reversing inputs and outputs. The expression $1/f(x)$ is the reciprocal of a function value and is undefined at $f(x)=0$.

### Misconception 4. Exchanging $x$ and $y$ in a formula automatically gives an inverse

After exchanging the variables, each output must still determine one input. For $f(x)=x^2$ over all real numbers, $y=4$ corresponds to two inputs, so no inverse exists.

### Misconception 5. Successful decoder reconstruction means the original function is invertible

Approximate reconstruction on limited data does not guarantee a global bijection. Check the error, data range, and compositions in both directions.

## Exercises

### 1. Calculate a composition value

For

\[
g(x)=x-2,\qquad f(u)=u^2+1
\]

calculate $(f\circ g)(5)$.

<details>
<summary>Show solution</summary>

Apply $g$ first.

\[
g(5)=5-2=3
\]

Pass the result to $f$.

\[
f(3)=3^2+1=10
\]

Therefore,

\[
(f\circ g)(5)=10
\]

</details>

### 2. Find composition formulas

For

\[
g(x)=2x+1,\qquad f(u)=u-4
\]

calculate $(f\circ g)(x)$ and $(g\circ f)(x)$.

<details>
<summary>Show solution</summary>

\[
(f\circ g)(x)
=
f(2x+1)
=
(2x+1)-4
=2x-3
\]

\[
(g\circ f)(x)
=
g(x-4)
=
2(x-4)+1
=2x-7
\]

The two composite functions differ.

</details>

### 3. Find a composition's domain

Let

\[
g(x)=x+3,\qquad f(u)=\sqrt u
\]

Find the formula and domain of $(f\circ g)(x)$ over the real numbers.

<details>
<summary>Show solution</summary>

\[
(f\circ g)(x)=\sqrt{x+3}
\]

A real square root requires a nonnegative input, so

\[
x+3\ge0
\]

The domain is therefore

\[
x\ge-3
\]

</details>

### 4. Determine injectivity and surjectivity

Let $A=\{1,2,3\}$ and $B=\{a,b,c\}$. A function $f:A\to B$ is given by

\[
f(1)=a,\qquad f(2)=b,\qquad f(3)=b
\]

Determine whether it is injective and whether it is surjective.

<details>
<summary>Show solution</summary>

Since $f(2)=f(3)=b$, different inputs $2,3$ have the same output. The function is not injective.

No input produces codomain element $c$. The range is $\{a,b\}$, which differs from the codomain $B$, so the function is not surjective either.

</details>

### 5. Find an inverse function

Find the inverse of

\[
f:\mathbb R\to\mathbb R,\qquad f(x)=5x+10
\]

<details>
<summary>Show solution</summary>

Starting from

\[
y=5x+10
\]

subtract $10$ from both sides to get

\[
y-10=5x
\]

Then divide both sides by $5$.

\[
x=\frac{y-10}{5}
\]

Therefore,

\[
f^{-1}(x)=\frac{x-10}{5}
\]

Checking gives

\[
f^{-1}(f(x))
=
\frac{(5x+10)-10}{5}
=x
\]

</details>

### 6. Assess a domain restriction

For

\[
f(x)=x^2
\]

select which of the following functions has an inverse and explain why.

\[
f_1:\mathbb R\to[0,\infty)
\]

\[
f_2:(-\infty,0]\to[0,\infty)
\]

<details>
<summary>Show solution</summary>

$f_1$ is not injective. Since $f_1(1)=f_1(-1)=1$, it has no inverse.

$f_2$ allows only negative inputs or $0$. On this domain, different inputs do not have the same square, and each $y\ge0$ in the codomain has input $-\sqrt y$. The function is therefore bijective, with inverse

\[
f_2^{-1}(y)=-\sqrt y
\]

</details>

### 7. Model composition and reconstruction claims

A model is given by

\[
h=f_1(x),\qquad y=f_2(h)
\]

1. Express the whole model as a composite function.
2. A decoder $d$ satisfies $d(h)\approx x$ on some data. Determine whether this result alone establishes $d=f_1^{-1}$.

<details>
<summary>Show solution</summary>

The whole model is

\[
y=(f_2\circ f_1)(x)
\]

Apply $f_1$ first and then $f_2$.

Approximate reconstruction on some data alone does not establish $d=f_1^{-1}$. Claiming an inverse requires checking whether $f_1$ is bijective on the specified domain and codomain and whether

\[
d(f_1(x))=x
\]

and

\[
f_1(d(h))=h
\]

hold over those ranges. Approximate equalities also require an error criterion and evaluation range.

</details>

## Lesson summary

- $(f\circ g)(x)=f(g(x))$, with $g$ applied first.
- For composition, check whether the preceding function's output belongs to the next function's domain.
- Composition order cannot be exchanged in general.
- An inverse exists when the function is bijective on the specified domain and codomain.
- Approximate reconstruction on limited data does not guarantee a global inverse.

## Pass criteria

You pass if you can answer these questions without consulting the lesson.

- Can you state the application order in $f\circ g$?
- Can you find the domain of a composition from the conditions on its intermediate outputs?
- Can you distinguish injective, surjective, and bijective functions?
- Can you find and check the inverse of a simple linear expression?
- Can you distinguish approximate decoder reconstruction from an inverse function?

## Next lesson

The next lesson is [M00-09 Shapes of scalars, vectors, and matrices](M00-09-scalars-vectors-matrices-shape.md). It distinguishes types and dimensions of mathematical objects and uses shape to check whether an operation is defined.

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Every new symbol is defined before use.
- [x] Composition order and range conditions are explicit.
- [x] Both compositions defining an inverse are explained.
- [x] Compositions and inverses in the examples have been checked.
- [x] Every exercise has a solution.
- [x] Approximate reconstruction and global invertibility are distinguished.
- [x] Terminology and notation follow the glossary and style rules.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
