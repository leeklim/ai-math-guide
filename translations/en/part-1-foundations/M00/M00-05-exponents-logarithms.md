---
id: "M00-05"
title: "Exponents and logarithms"
part: 1
stage: "M00"
status: "complete"
prerequisites:
  - "M00-02"
  - "M00-03"
  - "M00-04"
estimated_time: "90~110 minutes"
---

# M00-05. Exponents and logarithms

## Why this lesson matters

Probability models and neural networks use exponents and logarithms throughout their computations. Softmax applies an exponential function to scores, and cross entropy uses the logarithm of predicted probabilities. Taking the logarithm of a product of probabilities lets us calculate a sum instead, which also simplifies likelihood expressions.

Memorizing symbols alone can lead to confusing $\log(x+y)$ with $\log x+\log y$, or trying to calculate $\log 0$. Establishing the inverse relationship between exponents and logarithms helps you check both the direction of a formula and its allowed inputs.

## Learning objectives

After this lesson, you should be able to:

- Calculate integer powers with positive bases and apply the exponent laws.
- Explain the basic properties of the exponential functions $a^x$ and $\exp(x)$.
- Convert between $\log_a y=x$ and $a^x=y$.
- Check the domain of logarithms and their main calculation rules.
- Read the roles of exponents and logarithms in softmax and negative log loss.

## Prerequisite check

- Prerequisite lesson: [M00-02 Expressions, equalities, and equations](M00-02-expressions-equalities-equations.md)
- Prerequisite lesson: [M00-03 Function inputs and outputs](M00-03-functions-input-output.md)
- Prerequisite lesson: [M00-04 Coordinates and graphs](M00-04-coordinates-graphs.md)

Check whether you can perform these calculations.

\[
2\cdot2\cdot2=8
\]

\[
\frac{1}{2^2}=\frac14
\]

We define the logarithm as the operation that reverses this repeated multiplication.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| $a^x$ | `a to the x` | The value with base $a$ and exponent $x$ | Usually $a>0$ for real exponents |
| $a$ | `a` | The number repeatedly multiplied, or the fixed base of an exponential function | For logarithms, $a>0$, $a\ne1$ |
| $x$ | `x` | An extension of the number of times the base is multiplied | Starts with integers and extends to real numbers |
| $\exp(x)$ | `the exponential of x` | The exponential function with base $e$, the natural constant | $\exp(x)=e^x$ |
| $\log_a y$ | `log base a of y` | The power to which $a$ must be raised to obtain $y$ | $y>0$ |
| $\log y$ | `log of y` | The natural logarithm in this textbook | $\log y=\log_e y$ |

## Core concept 1. Exponents begin with repeated multiplication

For a positive integer $n$,

\[
a^n
\]

is the product of $n$ copies of $a$.

\[
a^n=
\underbrace{a\cdot a\cdots a}_{n\text{ factors}}
\]

For example,

\[
2^4=2\cdot2\cdot2\cdot2=16
\]

We call $a$ the base and $n$ the exponent.

### Exponent 0 and negative integer exponents

For $a\ne0$, define exponent 0 by

\[
a^0=1
\]

This definition agrees with the rule for dividing powers with the same base.

\[
\frac{a^3}{a^3}=1
\]

Applying the exponent law also gives

\[
\frac{a^3}{a^3}=a^{3-3}=a^0
\]

so we set $a^0=1$.

For a positive integer $n$, define a negative exponent by

\[
a^{-n}=\frac{1}{a^n}
\]

For example,

\[
2^{-3}=\frac{1}{2^3}=\frac18
\]

Reducing the exponent one step at a time gives $2^3=8$, $2^2=4$, $2^1=2$, and $2^0=1$: each step divides the value by $2$. Continuing the same rule gives $2^{-1}=1/2$ and $2^{-2}=1/4$. A negative exponent does not change the sign of the base. It continues the division as the exponent decreases.

In the next figure, each decrease of one in the exponent divides the value on the right by 2. The same rule continues past exponent 0.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Exponents descend from three through zero to negative three while values halve from eight to one eighth and remain positive](../../figures/assets/M00/M00-05-negative-exponent-chain.svg)

<figcaption>At exponent 0, the value is 1. Continuing to divide gives 1/2, 1/4, and 1/8, so the values remain positive for negative exponents.</figcaption>
</figure>

### Main exponent laws

For $a>0$ and allowed exponents $x,y$, the following laws hold.

\[
a^x a^y=a^{x+y}
\]

\[
\frac{a^x}{a^y}=a^{x-y}
\]

\[
\left(a^x\right)^y=a^{xy}
\]

For positive integer exponents, we can verify these laws by counting the factors. In $a^3a^2$, three copies and two copies of $a$ give five in total, hence $a^{3+2}$. In $(a^3)^2$, two groups of three copies of $a$ are multiplied, giving six copies of $a$. We therefore multiply the exponents and write $a^{3\cdot2}$ in this case. When dividing powers with the same base, canceling factors in the numerator and denominator leaves the difference of the exponents.

We retain these laws when extending exponents beyond integers. The first law applies to products with the same base; it cannot be applied unchanged to $a^x b^y$, whose bases differ.

Counting the copies of base 2 in the next figure distinguishes when to add exponents from when to multiply them.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Multiplying two cubed by two squared joins groups of three and two factors, while squaring two cubed repeats a three-factor group twice](../../figures/assets/M00/M00-05-exponent-factor-groups.svg)

<figcaption>The upper row joins 3 factors and 2 factors to give 5. The lower row multiplies two groups of 3 factors to give 6. Adding and multiplying exponents come from different group structures.</figcaption>
</figure>

## Core concept 2. An exponential function takes the exponent as its input

Fixing the base $a$ and treating the exponent $x$ as the input gives the function

\[
f(x)=a^x
\]

We call this an exponential function when $a>0$ and $a\ne1$.

The exponent changes, not the base. Substituting $x=3$ into $f(x)=2^x$ means calculating $2^3$, not $3^2$, the product of two copies of $3$. In $x^2$, we multiply two copies of the input; in $2^x$, the input specifies the exponent of the fixed base $2$.

The next figure places the input in different positions and compares the two calculations.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Input three follows arrows into the base position of x squared or the exponent position of two to the x, producing nine and eight](../../figures/assets/M00/M00-05-input-base-or-exponent.svg)

<figcaption>For x=3, x² is 9 and 2ˣ is 8. Even if the values coincide for some inputs, the rules differ according to whether the input is the base or the exponent.</figcaption>
</figure>

For noninteger inputs, counting repeated multiplications alone cannot determine the value, so we extend the definition in agreement with the exponent laws. For example, an input of $1/2$ must satisfy

\[
\left(2^{1/2}\right)^2=2^{(1/2)\cdot2}=2
\]

Thus $2^{1/2}$ is the positive number whose square is $2$, approximately $1.414$. We also define real powers to have positive values. This lesson does not cover the rigorous construction of real powers.

If $a>1$, then $a^x$ increases as $x$ increases. If $0<a<1$, then $a^x$ decreases as $x$ increases.

In either case, for real $x$,

\[
a^x>0
\]

The exponential graph never reaches the $x$-axis. At $x=0$,

\[
a^0=1
\]

so it passes through $(0,1)$.

The next figure compares bases above and below 1. Neither curve reaches the x-axis.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Increasing and decreasing exponential curves share point zero comma one and stay above the horizontal axis on a labeled coordinate grid](../../figures/assets/M00/M00-05-base-growth-comparison.svg)

<figcaption>With base 2, the value increases as the input increases; with base 1/2, it decreases. Both functions have value 1 at input 0.</figcaption>
</figure>

### The natural constant $e$ and $\exp$

Calculus and probability often use the natural constant

\[
e\approx2.71828
\]

as a base. The natural exponential function has two notations.

\[
\exp(x)=e^x
\]

The notation $\exp(x)$ makes a long or fractional exponent easier to read.

\[
\exp\left(-\frac{x^2}{2}\right)
=
e^{-x^2/2}
\]

The two expressions represent the same value.

## Core concept 3. A logarithm recovers an exponent

For $a>0$, $a\ne1$, and $y>0$,

\[
\log_a y=x
\]

means the same as

\[
a^x=y
\]

In words, $\log_a y$ answers the question, "To what power must $a$ be raised to obtain $y$?"

If we know the base $a$ and result $y$ in $a^x=y$ and want to find the exponent $x$, we write the answer as $\log_a y$. The exponential function takes $x$ and produces $y$; the logarithmic function takes $y$ and produces $x$. The whole expression $\log_a y$ is one value, and the subscript $a$ specifies the base whose exponent we seek.

For example,

\[
2^3=8
\]

so

\[
\log_2 8=3
\]

Also,

\[
10^{-2}=0.01
\]

so

\[
\log_{10}0.01=-2
\]

The condition $a\ne1$ is necessary to recover a unique exponent. With base $1$, different exponents all give $1^x=1$, so the result $1$ cannot determine the exponent. The exponential function is strictly increasing for $a>1$ and strictly decreasing for $0<a<1$, so different exponents give different positive values. In both cases, each positive output determines one exponent.

The next figure keeps base 2 fixed while showing how to recover the exponent from the result and the result from the exponent.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![With base two fixed, exponent three gives value eight and log base two of eight recovers exponent three](../../figures/assets/M00/M00-05-log-retrieves-exponent.svg)

<figcaption>Exponentiation takes 3 to 8. The logarithm takes the positive value 8 and recovers the exponent 3 that produced it.</figcaption>
</figure>

### The natural logarithm

A logarithm with base $e$ is called the natural logarithm.

\[
\log y=\log_e y
\]

In this textbook, $\log$ without a stated base means the natural logarithm. Some publications and calculators use $\log$ for base $10$, so check the author's notation. Many publications write the natural logarithm as $\ln y$.

### The domain of a logarithm

Over the real numbers, $\log y$ is defined only for $y>0$, because the natural exponential function $e^x$ has positive outputs.

\[
\log 0
\]

and real logarithms of negative numbers are not defined within this lesson's scope.

## Core concept 4. Exponential and logarithmic functions undo each other

Applying a logarithm to an exponential recovers the original exponent.

\[
\log_a(a^x)=x
\]

Taking the logarithm of a positive $y$ and then raising the same base to that power also recovers the original value.

\[
a^{\log_a y}=y
\]

For the natural exponential and natural logarithm, we have

\[
\log(\exp(x))=x
\]

\[
\exp(\log y)=y,\qquad y>0
\]

In the first expression, a real exponent $x$ is converted to a positive value, whose exponent we then recover, yielding the same real $x$. In the second, we first find the exponent that produces the positive value $y$, then calculate with that exponent to recover $y$. The starting values differ, so distinguish the conditions. In $\log(\exp(x))$, $\exp(x)$ is already positive and can be passed to the logarithm. In $\exp(\log y)$, the initial value must satisfy $y>0$ before we can calculate $\log y$.

The graphs of $y=a^x$ and $y=\log_a x$ are reflections across the line $y=x$. These inverse functions exchange the roles of input and output.

The natural exponential and natural logarithm have the same relationship. The point $(0,1)$ on the exponential graph pairs with $(1,0)$ on the logarithmic graph, and $(1,e)$ pairs with $(e,1)$. Each pair exchanges the horizontal and vertical coordinates. This exchange appears as reflection across $y=x$.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Exponential and logarithm curves reflected across y equals x with two pairs of swapped coordinates](../../figures/assets/M00/M00-05-c04-visual.svg)

<figcaption>Exchanging the input and output of y=exp(x) gives a point on y=log(x). The dashed connections between (0,1) and (1,0), and between (1,e) and (e,1), show how inverse functions exchange coordinates.</figcaption>
</figure>

## Core concept 5. Logarithms turn products into sums

For $u>0$ and $v>0$, the logarithm laws are

\[
\log(uv)=\log u+\log v
\]

\[
\log\left(\frac{u}{v}\right)=\log u-\log v
\]

\[
\log(u^r)=r\log u
\]

Here $r$ is a real exponent. We can verify the first law using exponents. Let $p=\log u$ and $q=\log v$ for positive $u,v$. The inverse relationship gives $u=e^p$ and $v=e^q$, hence

\[
uv=e^p e^q=e^{p+q}
\]

Taking the logarithm of both sides gives

\[
\log(uv)=p+q=\log u+\log v
\]

Multiplying powers adds their exponents, and the logarithm recovers that exponent. We can therefore write the logarithm of a product as a sum of logarithms. Division follows the same reasoning.

\[
\frac{u}{v}=\frac{e^p}{e^q}=e^{p-q}
\]

Thus $\log(u/v)=p-q=\log u-\log v$. For a power, $u^r=(e^p)^r=e^{pr}$, giving $\log(u^r)=pr=r\log u$. The three logarithm laws express the exponent laws learned earlier through logarithms.

Logarithms turn products into sums but do not split an addition into separate logarithms.

\[
\log(u+v)\ne\log u+\log v
\]

The inequality above holds in general. For example, if $u=v=1$, the left side is $\log2$, while the right side is $0$.

The next figure verifies the same product law with base-2 logarithms. Adding exponents 2 and 3 of the values 4 and 8 gives exponent 5 of their product 32.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Four and eight equal powers of two with exponents two and three, so their product has log base two equal to five and to the sum of the separate logs](../../figures/assets/M00/M00-05-log-product-sum.svg)

<figcaption>The logarithm of the product and the sum of the individual logarithms both equal 5. This figure explicitly uses base 2; log without a stated base in the main text means the natural logarithm.</figcaption>
</figure>

## Example 1. Calculate powers

### Problem

Calculate:

\[
2^3\cdot2^{-1}
\]

### Solution

The powers have the same base, so add the exponents.

\[
2^3\cdot2^{-1}=2^{3+(-1)}=2^2=4
\]

Converting the negative power to a fraction first gives the same result.

\[
2^3\cdot2^{-1}=8\cdot\frac12=4
\]

## Example 2. Convert a logarithmic equation to an exponential equation

### Problem

Convert

\[
\log_3 81=4
\]

to an exponential equation and check its value.

### Solution

$\log_a y=x$ means the same as $a^x=y$. Thus

\[
\log_3 81=4
\]

becomes

\[
3^4=81
\]

Indeed,

\[
3^4=3\cdot3\cdot3\cdot3=81
\]

so the equality holds.

## Example 3. Split a product using a logarithm law

### Problem

For $p_1,p_2,p_3>0$, express

\[
\log(p_1p_2p_3)
\]

as a sum of logarithms.

### Solution

Apply the product law twice.

\[
\log(p_1p_2p_3)
=
\log(p_1p_2)+\log p_3
\]

\[
=
\log p_1+\log p_2+\log p_3
\]

Taking the logarithm of a likelihood expressed as a product of probabilities gives a sum of the logarithms of its terms. Probability models use this property to calculate log-likelihood.

## Example 4. Read the exponential in softmax

Consider these expressions converting two scores $z_1,z_2$ into positive proportions.

\[
p_1
=
\frac{\exp(z_1)}
{\exp(z_1)+\exp(z_2)}
\]

\[
p_2
=
\frac{\exp(z_2)}
{\exp(z_1)+\exp(z_2)}
\]

The exponential function has positive outputs, so $p_1,p_2>0$. Adding the values gives

\[
p_1+p_2
=
\frac{\exp(z_1)+\exp(z_2)}
{\exp(z_1)+\exp(z_2)}
=1
\]

Let $z_1=\log3$ and $z_2=0$. The inverse relationship gives

\[
\exp(\log3)=3,\qquad \exp(0)=1
\]

so

\[
p_1=\frac{3}{3+1}=\frac34
\]

\[
p_2=\frac{1}{3+1}=\frac14
\]

Softmax extends this structure to multiple scores.

In the next figure, both terms are divided by the same denominator, 4. The final bar displays probabilities by dividing the total of 1 into four shares.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Softmax scores log three and zero exponentiate to weights three and one, then divide by total four to produce probabilities three quarters and one quarter](../../figures/assets/M00/M00-05-softmax-normalization.svg)

<figcaption>The positive weights 3 and 1 sum to 4. p₁ occupies three of the four shares and p₂ one share, so the probabilities sum to 1.</figcaption>
</figure>

## Example 5. Read negative log loss

Let $p$ be the predicted probability assigned to the correct answer, and consider the loss

\[
\mathcal L=-\log p
\]

For $0<p\le1$, we have $\log p\le0$, so $-\log p\ge0$. As the probability of the correct answer approaches $1$, the loss approaches $0$.

\[
-\log(0.8)\approx0.223
\]

\[
-\log(0.1)\approx2.303
\]

The second prediction, which assigns a lower probability to the correct answer, receives a larger loss. This expression alone cannot assess the model's overall quality; also check which data were used to calculate its average.

## Common misconceptions

### Misconception 1. $a^x a^y=a^{xy}$

When multiplying powers with the same base, add the exponents.

\[
a^x a^y=a^{x+y}
\]

Multiply exponents when raising a power to another power.

\[
(a^x)^y=a^{xy}
\]

### Misconception 2. $a^{-n}$ is negative

A negative exponent means the reciprocal.

\[
a^{-n}=\frac1{a^n}
\]

For $a>0$, the result is also positive.

### Misconception 3. $\log(u+v)=\log u+\log v$

Logarithms turn products into sums. There is no law that splits a sum into logarithms of its terms.

### Misconception 4. $\log 0=0$

No real $x$ satisfies $a^x=0$, so $\log_a0$ is not defined over the reals. Do not confuse this with $\log1=0$.

### Misconception 5. $\log$ has the same base in every publication

The meaning of $\log$ without a stated base can vary by field or tool. This textbook and many machine-learning publications use the natural logarithm. Check the publication's notation first.

## Exercises

### 1. Calculate integer powers

Calculate:

\[
5^0,\qquad 2^{-4},\qquad 3^2\cdot3^3
\]

<details>
<summary>Show solution</summary>

Since $5\ne0$,

\[
5^0=1
\]

A negative power gives a reciprocal, so

\[
2^{-4}=\frac1{2^4}=\frac1{16}
\]

When multiplying powers with the same base, add the exponents.

\[
3^2\cdot3^3=3^{2+3}=3^5=243
\]

</details>

### 2. Apply exponent laws

Calculate

\[
\frac{7^5}{7^2}
\]

and

\[
\left(2^3\right)^2
\]

<details>
<summary>Show solution</summary>

When dividing powers with the same base, subtract the exponents.

\[
\frac{7^5}{7^2}=7^{5-2}=7^3=343
\]

When raising a power to another power, multiply the exponents.

\[
\left(2^3\right)^2=2^{3\cdot2}=2^6=64
\]

</details>

### 3. Convert logarithmic equations to exponential equations

Convert these to exponential equations.

\[
\log_2 32=5
\]

\[
\log_{10}0.001=-3
\]

<details>
<summary>Show solution</summary>

$\log_a y=x$ is equivalent to $a^x=y$. The equations become

\[
2^5=32
\]

\[
10^{-3}=0.001
\]

</details>

### 4. Calculate logarithms

Calculate:

\[
\log_3 1,\qquad \log_3 27,\qquad \log_3\frac19
\]

<details>
<summary>Show solution</summary>

\[
3^0=1
\]

so $\log_3 1=0$.

\[
3^3=27
\]

so $\log_3 27=3$.

\[
\frac19=3^{-2}
\]

so

\[
\log_3\frac19=-2
\]

</details>

### 5. Determine the domain of logarithms

Select every expression defined over the real numbers and explain why.

\[
\log 4,\qquad \log1,\qquad \log0,\qquad \log(-2)
\]

<details>
<summary>Show solution</summary>

A real logarithm requires a positive input. Since $4>0$ and $1>0$, both $\log4$ and $\log1$ are defined. In particular, $\log1=0$.

Neither $0$ nor $-2$ is positive, so $\log0$ and $\log(-2)$ are not defined within this lesson's real-number scope.

</details>

### 6. Calculate softmax

Define the probabilities for two scores by

\[
p_1=\frac{\exp(z_1)}{\exp(z_1)+\exp(z_2)},
\qquad
p_2=\frac{\exp(z_2)}{\exp(z_1)+\exp(z_2)}
\]

Calculate $p_1,p_2$ for $z_1=0$ and $z_2=\log4$.

<details>
<summary>Show solution</summary>

\[
\exp(0)=1,\qquad \exp(\log4)=4
\]

so

\[
p_1=\frac{1}{1+4}=\frac15
\]

\[
p_2=\frac{4}{1+4}=\frac45
\]

The two probabilities sum to $1$.

</details>

### 7. Identify an incorrect logarithm law

Explain the error in this calculation.

\[
\log(1+1)=\log1+\log1=0
\]

<details>
<summary>Show solution</summary>

There is no logarithm law for splitting a sum into separate terms. The left side is

\[
\log(1+1)=\log2
\]

which is positive. The right side is

\[
\log1+\log1=0+0=0
\]

The values therefore differ.

The correct law, for positive $u,v$, is

\[
\log(uv)=\log u+\log v
\]

</details>

## Lesson summary

- $a^n$ begins with repeated multiplication and extends through $a^0=1$ and $a^{-n}=1/a^n$.
- Add exponents when multiplying powers with the same base; multiply exponents when raising a power to another power.
- $\log_a y=x$ means the same as $a^x=y$.
- Real logarithms are defined for positive inputs and are inverses of exponential functions.
- Logarithms turn products into sums, and softmax and log loss use these properties.

## Pass criteria

You pass if you can answer these questions without consulting the lesson.

- Can you calculate powers with exponent 0 or negative exponents?
- Can you distinguish the three exponent laws?
- Can you convert a logarithmic equation to an exponential equation?
- Can you explain why $\log0$ is not defined over the real numbers?
- Can you read how $\exp$ produces positive proportions in softmax?

## Next lesson

The next lesson is [M00-06 Indices and summation notation](M00-06-indices-summation.md). It distinguishes values with subscripts and represents repeated addition using $\sum$.

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Every new symbol is defined before use.
- [x] Conditions for the exponent and logarithm laws are stated.
- [x] The domain of logarithms is explicit.
- [x] Numerical values in the examples have been checked.
- [x] Every exercise has a solution.
- [x] Explanations of softmax and loss functions remain at an introductory level.
- [x] Terminology and notation follow the glossary and style rules.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
