---
id: "M00-06"
title: "Indices and summation notation"
part: 1
stage: "M00"
status: "complete"
prerequisites:
  - "M00-01"
  - "M00-02"
  - "M00-03"
estimated_time: "80~100 minutes"
---

# M00-06. Indices and summation notation

## Why this lesson matters

Papers use subscripts to distinguish values of the same kind. $x_1,x_2,\ldots,x_N$ can denote $N$ inputs or observations. Summation notation abbreviates repeated addition.

\[
\frac1N\sum_{n=1}^{N}\mathcal L_n
\]

This formula sums the losses of $N$ samples and divides by $N$ to obtain their mean. If you cannot read subscripts and summation bounds, you can lose track of which values are added, how many terms there are, and the unit over which the mean is computed.

## Learning objectives

After completing this lesson, you will be able to:

- Distinguish the name of a symbol from the role of its index in $x_i$.
- Identify the starting index, ending index, and summand in $\sum_{i=a}^{b}$.
- Expand summation notation into addition and abbreviate addition using summation notation.
- Calculate arithmetic means and weighted sums.
- Distinguish the roles of multiple indices, such as sample and feature indices.

## Prerequisite check

- Prerequisite: [M00-01 Numbers, variables, and constants](M00-01-numbers-variables.md)
- Prerequisite: [M00-02 Expressions, equalities, and equations](M00-02-expressions-equalities-equations.md)
- Prerequisite: [M00-03 Function inputs and outputs](M00-03-functions-input-output.md)

Check that you can perform the following addition and division.

\[
2+5+8=15
\]

\[
\frac{2+5+8}{3}=5
\]

Summation notation abbreviates the first calculation, while mean notation generalizes the structure of the second.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Cautions |
|---|---|---|---|
| $x_i$ | `x sub i` | The $i$th value among several $x$ values | Not the product of $x$ and $i$ |
| $i$ | `i` | An index distinguishing positions or objects | The starting value depends on context |
| $N$ | `N` | The number of terms or samples | A positive integer |
| $\sum$ | `sigma` | A symbol instructing you to add specified terms | An uppercase Greek letter |
| $\sum_{i=1}^{N}x_i$ | `sum over i from one to N of x sub i` | $x_1+\cdots+x_N$ | Read both the lower and upper bounds |
| $\bar x$ | `x bar` | The arithmetic mean of the $x_i$ values | Often used for a sample mean |
| $w_i$ | `w sub i` | The weight of the $i$th term | Used in a weighted sum |

## Core concept 1. Indices distinguish values

You can write three measurements as

\[
x_1=4,\qquad x_2=7,\qquad x_3=5
\]

The symbol $x$ indicates that the three values are of the same kind. The subscripts $1,2,3$ distinguish them.

In $x_i$, $i$ is an index specifying the position or object associated with a value. Setting $i=2$ gives

\[
x_i=x_2=7
\]

### Subscripts are neither multiplication nor exponentiation

\[
x_i,\qquad xi,\qquad x^i
\]

are different notations.

- $x_i$: the $i$th $x$
- $xi$: depending on context, the product of $x$ and $i$
- $x^i$: $x$ raised to the $i$th power, or a different kind of index in later lessons

Papers use subscripts to distinguish classes, token positions, layers, attention heads, and other objects. Check where the author defines each index's meaning.

### Context determines the starting index

Mathematical notation often starts at $1$, as in $x_1,\ldots,x_N$. Python arrays count positions from $0$. The first array element in code may correspond to $x_1$ in a formula.

Do not assume that an index starts at $0$ or at $1$. Read the summation bounds or the author's definition.

The following figure labels the same three values separately with mathematical indices and Python positions.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Mathematical indices one two three label values four seven five, while Python positions zero one two identify the same ordered values](../../figures/assets/M00/M00-06-index-selects-value.svg)

<figcaption>In the formula, x₂ is the middle value, 7. A Python array storing the same values in order has 7 at position 1. Check both the starting index and the ordering of the objects.</figcaption>
</figure>

## Core concept 2. Summation notation abbreviates repeated addition

The parts of

\[
\sum_{i=1}^{4}x_i
\]

have the following roles.

- $\sum$: the operation of adding terms
- $i$: the index whose value changes during the summation
- $i=1$: the starting index
- $4$: the ending index
- $x_i$: the term added at each index

Expanding the sum gives

\[
\sum_{i=1}^{4}x_i
=
x_1+x_2+x_3+x_4
\]

If the index runs from $a$ to $b$ in steps of one, the number of terms is

\[
b-a+1
\]

$b-a$ counts the increments from the starting to the ending index. The term count must also include the first term, before any increment, so you add 1. To expand a sum, first list the indices including both endpoints, then substitute each index into the summand.

For example,

\[
\sum_{i=3}^{7}x_i
\]

uses $i=3,4,5,6,7$, so it has $5$ terms.

In the following figure, count the term selected by each index to distinguish the number of increments from the number of terms.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Inclusive indices three through seven each select one term, giving five terms despite four transitions between indices](../../figures/assets/M00/M00-06-inclusive-sum-range.svg)

<figcaption>Moving from 3 to 7 takes four increments. Including the starting term x₃ gives five terms to add.</figcaption>
</figure>

### When the summand is an expression

A summation can contain an expression or function, not only a single symbol.

Expanding

\[
\sum_{i=1}^{3}(2x_i+1)
\]

gives

\[
(2x_1+1)+(2x_2+1)+(2x_3+1)
\]

The entire parenthesized expression is one term repeated for each index.

The constant 1 has no index, but it occurs inside each pair of parentheses, so it is added three times. Collecting terms gives $2(x_1+x_2+x_3)+3$. The summation bounds determine the index range, while the parentheses determine the expression evaluated each time.

The following figure evaluates the entire parenthesized expression three times, using the earlier values 4, 7, and 5.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The full summand two x sub i plus one is evaluated for values four seven five, producing nine fifteen eleven with the constant one repeated three times](../../figures/assets/M00/M00-06-summand-scope.svg)

<figcaption>Each row replaces only xᵢ and evaluates all of 2xᵢ+1. The constant 1 appears in every row, so it contributes three times to the sum.</figcaption>
</figure>

## Core concept 3. The index inside a sum can be renamed

In

\[
\sum_{i=1}^{N}x_i
\]

$i$ changes only within the sum to specify term positions. Renaming it does not change the sum if the range and terms remain the same.

\[
\sum_{i=1}^{N}x_i
=
\sum_{j=1}^{N}x_j
\]

Both sides mean

\[
x_1+x_2+\cdots+x_N
\]

Such an index is called a dummy index.

When renaming an index, change both the letter in the lower bound and the letter representing that index in the summand. Replacing $i$ with $j$ still selects the same values, from the first through the $N$th. After summation, the result is a single value and does not depend on the name used for the dummy index.

If $i$ or $j$ already has a separate meaning outside the expression, check for a naming conflict before renaming it.

## Core concept 4. A mean divides a sum by the number of terms

The arithmetic mean of $N$ values $x_1,\ldots,x_N$ is

\[
\bar x
=
\frac1N\sum_{i=1}^{N}x_i
\]

Read this in the following order.

1. Sum $x_i$ for $i=1$ through $N$.
2. Divide the sum by the number of terms, $N$.

The mean is one value obtained by expressing the total as $N$ equal values. The sum of the original values must equal $\bar x$ added $N$ times, giving $N\bar x=x_1+\cdots+x_N$. Dividing both sides by $N$ yields the formula above. To calculate a mean, check both the total and the actual number of terms.

For $x_1=2$, $x_2=5$, and $x_3=8$,

\[
\bar x
=
\frac13\sum_{i=1}^{3}x_i
\]

\[
=
\frac13(x_1+x_2+x_3)
\]

\[
=
\frac13(2+5+8)
=5
\]

The following figure compares the sum of the original three values with the sum after replacing all three with the mean.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Columns of heights two five eight are replaced by three columns of height five, preserving the total fifteen](../../figures/assets/M00/M00-06-mean-equal-shares.svg)

<figcaption>Counting unit cells gives a total of 15 on both sides. One of its three equal shares, 5, is the arithmetic mean.</figcaption>
</figure>

### Check the denominator of a mean

\[
\sum_{i=0}^{N}x_i
\]

contains $N+1$ terms, from $x_0$ through $x_N$. Its mean must therefore also use $N+1$ in the denominator.

\[
\frac1{N+1}\sum_{i=0}^{N}x_i
\]

Missing the starting index can lead to an incorrect denominator.

## Core concept 5. A weighted sum gives each term its own coefficient

A weighted sum multiplies each term $x_i$ by a weight $w_i$ and adds the results.

\[
\sum_{i=1}^{N}w_i x_i
\]

For $N=3$, this is

\[
w_1x_1+w_2x_2+w_3x_3
\]

If the weights satisfy

\[
\sum_{i=1}^{N}w_i=1
\]

and $w_i\ge0$, you can interpret the weighted sum as a weighted mean.

Each $w_i$ multiplies the $x_i$ with the same index. A weighted mean uses nonnegative weights to set the share of each value and normalizes the total share to 1. An arithmetic mean is also a weighted mean, with every weight set to $w_i=1/N$. The $N$ weights then sum to 1 and give each value an equal share. A general weighted sum need not have weights summing to 1, so distinguish a weighted sum from a weighted mean.

For example, if $x_1=10$, $x_2=20$, $w_1=0.25$, and $w_2=0.75$,

\[
\sum_{i=1}^{2}w_i x_i
=
0.25\cdot10+0.75\cdot20
=17.5
\]

The second value receives more weight, so the result lies closer to $20$.

The following figure calculates each contribution and then compares the weighted mean's position with the two input values.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Weights one quarter and three quarters applied to ten and twenty yield seventeen point five, marked nearer twenty on a number line](../../figures/assets/M00/M00-06-weighted-mean-position.svg)

<figcaption>The contributions 2.5 and 15 sum to 17.5. In this example, the nonnegative weights sum to 1, so the result lies between 10 and 20 and closer to the more heavily weighted value, 20.</figcaption>
</figure>

## Core concept 6. Multiple indices distinguish different axes

A symbol can have two subscripts, as in

\[
x_{n,i}
\]

Machine learning often uses them as follows.

- $n$: sample index
- $i$: feature index

$x_{3,2}$ denotes the second feature of the third sample. The comma distinguishes the roles of the two indices.

Summing over both indices gives

\[
\sum_{n=1}^{N}\sum_{i=1}^{d}x_{n,i}
\]

The inner sum adds features for a fixed sample $n$. The outer sum adds those results across all samples.

For $N=2$ and $d=3$,

\[
\sum_{n=1}^{2}\sum_{i=1}^{3}x_{n,i}
\]

\[
=
(x_{1,1}+x_{1,2}+x_{1,3})
+
(x_{2,1}+x_{2,2}+x_{2,3})
\]

In this lesson, only indices explicitly named by summation symbols are summed. Later linear algebra lessons also state the summation bounds when expressing matrix multiplication with indices.

Calculating only the inner sum gives one feature total per sample, leaving $n$ to distinguish the samples. Only after the outer sum do these sample totals become one value. The example adds three terms for each sample, twice, giving $2\cdot3=6$ terms in total. Identifying which index each sum varies keeps the computation clear even when you read both sums together.

The following figure fills six cells with values from 1 to 6 and calculates the feature sums followed by the sample sum.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A two-sample three-feature table first sums each row to six and fifteen, then sums those sample totals to twenty one](../../figures/assets/M00/M00-06-two-index-reduction.svg)

<figcaption>The inner sum adds three features per sample to obtain 6 and 15. The outer sum combines those sample totals into one value, 21.</figcaption>
</figure>

## Example 1. Expanding summation notation

### Problem

Expand the following into addition and calculate the result.

\[
\sum_{k=2}^{5}(k+1)
\]

### Solution

$k$ takes the values $2,3,4,5$. Evaluate $k+1$ at each value.

\[
\sum_{k=2}^{5}(k+1)
=
(2+1)+(3+1)+(4+1)+(5+1)
\]

\[
=3+4+5+6
=18
\]

The number of terms is

\[
5-2+1=4
\]

## Example 2. Abbreviating addition with summation notation

### Problem

Express the following using summation notation.

\[
y_1^2+y_2^2+y_3^2+y_4^2
\]

### Solution

The index ranges from $1$ to $4$, and the repeated term is $y_i^2$. Therefore,

\[
y_1^2+y_2^2+y_3^2+y_4^2
=
\sum_{i=1}^{4}y_i^2
\]

The square applies to the whole $y_i$. This is different from $\left(\sum_i y_i\right)^2$.

## Example 3. Reading a mean loss

Suppose training samples are given as $(x_n,y_n)$, and define the $n$th sample's loss as

\[
\mathcal L_n
=
\mathcal L\bigl(f_\theta(x_n),y_n\bigr)
\]

The mean loss can be written as

\[
\bar{\mathcal L}
=
\frac1N\sum_{n=1}^{N}
\mathcal L\bigl(f_\theta(x_n),y_n\bigr)
\]

The symbols have the following meanings.

- $n$: sample index
- $N$: number of samples
- $x_n$: the $n$th input
- $y_n$: the $n$th ground-truth target
- $f_\theta(x_n)$: the model's prediction
- $\mathcal L$: a function taking a prediction and target to compute a loss

This formula computes a loss for each sample, sums the losses, and divides by the number of samples. Observing a lower mean loss does not establish that every sample's loss decreased. Decreases on some samples can offset increases on others.

## Example 4. Reading a weighted sum

Let three values be

\[
v_1=2,\qquad v_2=5,\qquad v_3=9
\]

with weights

\[
a_1=0.2,\qquad a_2=0.5,\qquad a_3=0.3
\]

Their weighted sum is

\[
\sum_{i=1}^{3}a_i v_i
\]

\[
=0.2\cdot2+0.5\cdot5+0.3\cdot9
\]

\[
=0.4+2.5+2.7
=5.6
\]

The weights sum to

\[
0.2+0.5+0.3=1
\]

so this calculation gives a weighted mean of the three values. Attention outputs also use a weighted-sum structure, multiplying values by attention weights and adding the results.

## Common misconceptions

### Misconception 1. $x_i$ is the product of $x$ and $i$

The subscript $i$ distinguishes several $x$ values. Multiplication is written as $xi$ or $x\cdot i$.

### Misconception 2. $\sum_{i=1}^{N}x_i$ has $N-1$ terms

Including both the starting and ending indices gives $N$ terms. In general, the integer indices from $i=a$ through $b$ give $b-a+1$ terms.

### Misconception 3. Only the first symbol after a summation sign is summed

In

\[
\sum_{i=1}^{N}(x_i-\bar x)^2
\]

the whole $(x_i-\bar x)^2$ is one term. Read the scope of the parentheses and exponent together.

### Misconception 4. If a mean decreases, every term decreased

A mean summarizes changes in multiple terms as one number. Some terms can increase while the mean decreases if other terms decrease more.

### Misconception 5. Indices always start at 1

The lower summation bound or definition determines the starting value. Counting from 0 is common in code.

## Exercises

### 1. Read indices

For $h_1=3$, $h_2=-1$, and $h_3=4$, find $h_2$ and the value of $h_i$ when $i=3$. Explain the role of the subscript $i$.

<details>
<summary>Show solution</summary>

\[
h_2=-1
\]

For $i=3$,

\[
h_i=h_3=4
\]

The subscript $i$ specifies which of several $h$ values is selected.

</details>

### 2. Expand a sum

Expand the following into addition and determine its number of terms.

\[
\sum_{i=2}^{5}x_i
\]

<details>
<summary>Show solution</summary>

Substituting $i=2,3,4,5$ in order gives

\[
\sum_{i=2}^{5}x_i
=
x_2+x_3+x_4+x_5
\]

The number of terms is

\[
5-2+1=4
\]

</details>

### 3. Calculate a sum with an expression as its summand

Expand and calculate

\[
\sum_{i=1}^{4}(2i-1)
\]

<details>
<summary>Show solution</summary>

\[
\sum_{i=1}^{4}(2i-1)
=
(2\cdot1-1)+(2\cdot2-1)+(2\cdot3-1)+(2\cdot4-1)
\]

\[
=1+3+5+7
=16
\]

</details>

### 4. Calculate a mean

For $x_1=4$, $x_2=6$, $x_3=8$, and $x_4=10$, calculate

\[
\bar x=\frac14\sum_{i=1}^{4}x_i
\]

<details>
<summary>Show solution</summary>

\[
\bar x
=
\frac14(4+6+8+10)
\]

\[
=
\frac14\cdot28
=7
\]

</details>

### 5. Calculate a weighted sum

For $v_1=1$, $v_2=4$, $v_3=10$, $w_1=0.5$, $w_2=0.25$, and $w_3=0.25$, calculate

\[
\sum_{i=1}^{3}w_i v_i
\]

Determine whether it can also be interpreted as a weighted mean.

<details>
<summary>Show solution</summary>

\[
\sum_{i=1}^{3}w_i v_i
=
0.5\cdot1+0.25\cdot4+0.25\cdot10
\]

\[
=0.5+1+2.5
=4
\]

All weights are nonnegative and satisfy

\[
0.5+0.25+0.25=1
\]

so this is also a weighted mean.

</details>

### 6. Expand a double sum

Expand the following so that every term is visible.

\[
\sum_{n=1}^{2}\sum_{i=1}^{2}x_{n,i}
\]

<details>
<summary>Show solution</summary>

First sum over $i=1,2$ in the inner sum.

\[
\sum_{n=1}^{2}\sum_{i=1}^{2}x_{n,i}
=
\sum_{n=1}^{2}(x_{n,1}+x_{n,2})
\]

Substituting $n=1,2$ into the outer sum gives

\[
=(x_{1,1}+x_{1,2})+(x_{2,1}+x_{2,2})
\]

There are $2\cdot2=4$ terms in total.

</details>

### 7. Evaluate a claim about means

Model A has per-sample losses $(1,1,8)$, while model B has $(3,3,3)$. Calculate the two mean losses and evaluate the claim: “The model with the smaller mean loss also has a smaller loss on every sample.”

<details>
<summary>Show solution</summary>

Model A's mean is

\[
\frac{1+1+8}{3}=\frac{10}{3}
\]

and model B's mean is

\[
\frac{3+3+3}{3}=3
\]

Model B has the smaller mean loss.

On the first and second samples, however, model A's loss of $1$ is smaller than model B's loss of $3$. Comparing means does not imply the same ordering on each sample.

</details>

## Lesson summary

- Subscripts distinguish multiple values of the same kind.
- $\sum_{i=a}^{b}$ sums the summand for indices from $i=a$ through $b$.
- Including both endpoints gives $b-a+1$ integer-indexed terms.
- An arithmetic mean divides a sum by its term count; a weighted sum multiplies each term by its weight before addition.
- Multiple indices distinguish roles such as sample, feature, and token.

## Pass criteria

You pass if you can answer the following questions without consulting the material.

- Can you distinguish $x_i$ from $x^i$?
- Can you identify a sum's lower bound, upper bound, and summand?
- Can you expand summation notation into addition?
- Can you calculate a mean and a weighted sum?
- Can you explain the two indices in $x_{n,i}$ separately?

## Next lesson

The next lesson is [M00-07 Sets, conditions, and logic](M00-07-sets-conditions-logic.md). You will use notation for elements and subsets and distinguish the directions of implications, necessary conditions, and sufficient conditions.

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] All new symbols are defined before use.
- [x] Summation bounds and term counts have been checked.
- [x] Numerical means and weighted sums have been checked.
- [x] Every exercise has a solution.
- [x] Observations about means are distinguished from claims about individual terms.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
