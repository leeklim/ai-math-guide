---
id: "M01-05"
title: "Derivatives of sums, products, and quotients"
part: 1
stage: "M01"
status: "complete"
prerequisites:
  - "M01-03"
  - "M01-04"
estimated_time: "100~120 minutes"
---

# M01-05. Derivatives of sums, products, and quotients

## Why this lesson matters

The definition using a difference quotient explains what differentiation means. Recalculating the limit whenever a function expression becomes longer, however, repeats the same algebra. Rules for differentiating sums, products, and quotients let us combine known derivatives to find new ones.

Neural network losses also consist of sums and averages of multiple terms. To apply the rules correctly, first identify which functions are added and which are multiplied. In particular, multiplying the individual derivatives for a product, or omitting the denominator condition for a quotient, changes the calculation.

## Learning objectives

After completing this lesson, you will be able to:

- Apply the constant multiple, sum, and difference rules.
- Explain how changes in both factors contribute to the product rule.
- Apply the quotient rule and check its denominator condition.
- Find derivatives of positive integer powers.
- Differentiate sums and averages of sample losses with respect to a scalar parameter.

## Prerequisite check

- Prerequisite lesson: [M01-03 Differentiation and instantaneous rates of change](M01-03-derivative-instantaneous-rate.md)
- Prerequisite lesson: [M01-04 Derivatives and graphs](M01-04-derivative-and-graphs.md)
- Check question: Can you explain what $f'(x)$ represents at each input of the function $f$?
- Check question: Can you expand $(x+h)^2$ to find the derivative of $x^2$ from the definition?

If the distinction between a difference quotient and a derivative is difficult, first review M01-03.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| $u(x),v(x)$ | `u of x and v of x` | Two functions depending on the same input $x$ | Assume differentiability at the required points. |
| $(uv)'$ | `u v prime` | Derivative of the product $u(x)v(x)$ | Calculate it as $u'v+uv'$. |
| $\left(\frac{u}{v}\right)'$ | `u over v prime` | Derivative of a quotient of two functions | Requires $v(x)\ne0$. |
| Product rule | `product rule` | Rule for differentiating a product of two functions | Add both contributions. |
| Quotient rule | `quotient rule` | Rule for differentiating one function divided by another | The denominator is squared. |

## Core concept 1. Differentiation acts linearly on sums and constant multiples

Let $c$ be a constant independent of $x$. The constant multiple rule is

\[
\frac{d}{dx}\bigl[c\,u(x)\bigr]
=
c\,u'(x)
\]

Keep the constant unchanged and multiply it by the function's rate of change.

For sums and differences, differentiate each term separately.

\[
\frac{d}{dx}\bigl[u(x)+v(x)\bigr]
=
u'(x)+v'(x)
\]

\[
\frac{d}{dx}\bigl[u(x)-v(x)\bigr]
=
u'(x)-v'(x)
\]

This is the sum rule. The same rule applies to a finite sum of multiple terms.

\[
\frac{d}{dx}
\sum_{i=1}^{N}u_i(x)
=
\sum_{i=1}^{N}u_i'(x)
\]

Assume $N$ is a fixed, finite integer. The rule follows because the output change of the whole sum equals the sum of the changes in the individual terms. For a sum of two functions, the difference quotient is

\[
\frac{[u(x+h)+v(x+h)]-[u(x)+v(x)]}{h}
=
\frac{u(x+h)-u(x)}{h}
+
\frac{v(x+h)-v(x)}{h}
\]

If both functions are differentiable, the terms on the right have limits $u'(x)$ and $v'(x)$, which we add. For a constant multiple, both the output change and the difference quotient are multiplied by $c$, so the limit is also multiplied by $c$. Here, “constant” means holding $c$ fixed while varying the input $x$. If $c$ also varies with $x$, use the product rule below.

## Core concept 2. A product includes the changes in both functions

Suppose both $u$ and $v$ vary with $x$. Abbreviate their values at the reference input as $u=u(x)$ and $v=v(x)$. Define their changes when the input becomes $x+h$ as $\Delta u=u(x+h)-u(x)$ and $\Delta v=v(x+h)-v(x)$. The change in their product is

\[
(u+\Delta u)(v+\Delta v)-uv
\]

Expanding gives

\[
u\Delta v+v\Delta u+\Delta u\Delta v
\]

The first two terms are contributions from changing only one function at a time. The final term is an additional contribution from changing both together. Differentiation divides this output change by the input change $h$. We can write the final cross term as

\[
\frac{\Delta u\Delta v}{h}
=
\frac{\Delta u}{h}\,\Delta v
\]

If $u$ is differentiable, $\Delta u/h$ approaches the finite value $u'(x)$. Since $v$ is also differentiable, it is continuous, and $\Delta v$ approaches $0$. The cross term therefore has limit $0$. The limits of the remaining two terms divided by $h$ are $uv'$ and $vu'$. Adding them gives the product rule.

\[
\frac{d}{dx}\bigl[u(x)v(x)\bigr]
=
u'(x)v(x)+u(x)v'(x)
\]

In abbreviated form,

\[
(uv)'=u'v+uv'
\]

The first term is the contribution from changing $u$, and the second is the contribution from changing $v$.

The product of the individual derivatives, $u'v'$, is not the derivative of the product. For example, if $u(x)=v(x)=x$, the derivative of $uv=x^2$ is $2x$, but $u'v'=1$.

The area diagram below uses two positive lengths and positive changes to divide the change in their product into three pieces.

<figure class="lesson-figure" markdown="1">

![Growing a rectangle in two directions adds strips v delta u and u delta v plus a corner delta u delta v](../../figures/assets/M01/M01-05-product-area.svg)

<figcaption>The right strip contributes the change in u, and the top strip contributes the change in v. The corner ΔuΔv is part of a finite change, but it disappears after division by h and passage to the limit.</figcaption>
</figure>

The next graph compares the correct derivative with the product of the individual derivatives when both functions are x.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The correct derivative two x of x times x differs from the constant one obtained by multiplying the two individual derivatives](../../figures/assets/M01/M01-05-product-rule-versus-wrong.svg)

<figcaption>The derivative of x² is 2x, so it varies with the input. The incorrect calculation x′·x′=1 does not represent this variation.</figcaption>
</figure>

## Core concept 3. A quotient subtracts the denominator's contribution

Let

\[
q(x)=\frac{u(x)}{v(x)},
\qquad v(x)\ne0
\]

Applying the product rule to the identity $qv=u$ gives

\[
q'v+qv'=u'
\]

Substitute $q=u/v$ and solve for $q'$.

\[
q'
=
\frac{u'-qv'}{v}
=
\frac{u'}{v}-\frac{uv'}{v^2}
\]

Put both terms over the common denominator $v^2$.

\[
q'
=
\frac{u'v-uv'}{v^2}
\]

Thus, the quotient rule is

\[
\frac{d}{dx}
\left(\frac{u(x)}{v(x)}\right)
=
\frac{u'(x)v(x)-u(x)v'(x)}{[v(x)]^2}
\]

The squared denominator comes from the division $u/v$ already present in $q$ and the further division by $v$ used to find $q'$. The subtraction comes from moving $qv'$ to the right side of $q'v+qv'=u'$. Subtracting the denominator's contribution makes the rate of change of the product $qv$ equal to that of the numerator $u$.

The numerator's order is `derivative of the numerator times the denominator, minus the numerator times the derivative of the denominator`. Reversing this order changes the overall sign. At points with $v(x)=0$, this formula cannot assign a value to either the original function or its derivative.

The figure below holds a positive numerator fixed and increases only the denominator. Dividing the same total into more shares makes each share smaller.

<figure class="lesson-figure" markdown="1">

![A fixed total of six is divided into two shares of three or three shares of two, illustrating a positive denominator increasing while the quotient decreases](../../figures/assets/M01/M01-05-denominator-effect.svg)

<figcaption>With numerator u=6 fixed, increasing denominator v from 2 to 3 decreases quotient q from 3 to 2. This shows a case in which a change in the denominator acts in the opposite direction on the quotient.</figcaption>
</figure>

## Core concept 4. Derivatives of positive integer powers

For a positive integer $n$, the function $x^n$ is the product of $n$ factors of $x$. Repeated application of the product rule produces $n$ terms, each differentiating the $x$ in one position.

In each term, the differentiated factor $x$ becomes $1$, and the remaining $n-1$ factors of $x$ stay unchanged. Each term is therefore $x^{n-1}$, and adding $n$ identical terms gives $nx^{n-1}$. This product structure explains both why the exponent decreases by one and why $n$ appears in front.

\[
\frac{d}{dx}x^n
=
nx^{n-1}
\]

This is the power rule. For example,

\[
\frac{d}{dx}x^3=3x^2,
\qquad
\frac{d}{dx}x^5=5x^4
\]

The function $x^0=1$ is constant, so its derivative is $0$. The power rule can be extended to negative integer and fractional exponents, but their domain conditions differ. In this lesson, we use cases that can be handled directly as polynomials and quotients.

In the figure below, differentiating each of the three factors of a cube produces the same term three times.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three product-rule contributions each replace one of the three x factors by one and leave x squared, producing three x squared](../../figures/assets/M01/M01-05-power-factors.svg)

<figcaption>The purple 1 in each row is the derivative of the x in that position. The remaining two factors form x²; adding the three rows gives 3x².</figcaption>
</figure>

## Core concept 5. Read the expression's structure before applying a rule

The following expressions use similar symbols but have different structures.

\[
u(x)+v(x)
\]

\[
u(x)v(x)
\]

The first uses the sum rule; the second uses the product rule. An entire expression in parentheses can be one factor of a product.

For

\[
(x^2+1)(x-3)
\]

set $u(x)=x^2+1$ and $v(x)=x-3$. Find their individual derivatives first, then substitute them into

\[
u'v+uv'
\]

Expanding the expression and differentiating term by term should give the same result. Comparing the two calculations helps check for sign errors and missing terms.

## Core concept 6. The derivative of mean loss is the mean of sample derivatives

Let $\ell_i(\theta)$ be the loss of each sample for a scalar parameter $\theta$. The mean loss is

\[
\mathcal L(\theta)
=
\frac{1}{N}
\sum_{i=1}^{N}\ell_i(\theta)
\]

Suppose each $\ell_i$ is differentiable at the current $\theta$. The sample count $N$ is fixed and independent of $\theta$. Varying $\theta$ leaves the samples in the sum and the factor $1/N$ unchanged; only each sample's loss changes. Applying the constant multiple and sum rules therefore gives

\[
\mathcal L'(\theta)
=
\frac{1}{N}
\sum_{i=1}^{N}\ell_i'(\theta)
\]

The rate of change of the overall mean is thus the mean of the individual rates. A mean value of $0$ does not mean that every sample derivative is $0$. Positive and negative contributions can cancel.

## Example 1. Differentiate a polynomial

Differentiate

\[
f(x)=3x^4-2x^2+5x-7
\]

Apply the constant multiple, sum, and power rules to each term.

\[
f'(x)
=
3\cdot4x^3-2\cdot2x+5
\]

Therefore,

\[
f'(x)=12x^3-4x+5
\]

The constant term $-7$ has derivative $0$.

## Example 2. Differentiate a product

For

\[
f(x)=(x^2+1)(x-3)
\]

set

\[
u(x)=x^2+1,
\qquad
v(x)=x-3
\]

Then

\[
u'(x)=2x,
\qquad
v'(x)=1
\]

The product rule gives

\[
f'(x)
=
2x(x-3)+(x^2+1)
\]

Simplifying gives

\[
f'(x)=3x^2-6x+1
\]

Expanding the original expression to $x^3-3x^2+x-3$ and differentiating gives the same result.

## Example 3. Differentiate a quotient

Let

\[
g(x)=\frac{x^2+1}{x-1},
\qquad x\ne1
\]

With $u=x^2+1$ and $v=x-1$, we have $u'=2x$ and $v'=1$.

\[
g'(x)
=
\frac{2x(x-1)-(x^2+1)}{(x-1)^2}
\]

Simplifying the numerator gives

\[
g'(x)
=
\frac{x^2-2x-1}{(x-1)^2},
\qquad x\ne1
\]

The derivative expression also excludes $x=1$.

## Example 4. Cancellation of sample rates of change

Let $N=2$, and suppose that at the current parameter value,

\[
\ell_1'(\theta)=4,
\qquad
\ell_2'(\theta)=-4
\]

The derivative of the mean loss is

\[
\mathcal L'(\theta)
=
\frac{4+(-4)}{2}
=0
\]

The mean slope is $0$, but the two sample losses change in opposite directions. Do not infer from the mean alone that every sample's loss has stopped changing.

The figure below shows the two contributions before averaging alongside their calculated mean.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Sample derivatives plus four and minus four appear on opposite sides of zero while their average is zero](../../figures/assets/M01/M01-05-mean-cancellation.svg)

<figcaption>The two sample slopes have equal magnitudes and opposite directions, so they cancel in the mean. The purple mean of 0 does not mean that all orange sample slopes are 0.</figcaption>
</figure>

## Common misconceptions

### Misconception 1. The derivative of a product is $u'v'$

For a product, count the change in $u$ and the change in $v$ separately. The result is $u'v+uv'$.

### Misconception 2. The derivative of a quotient is $u'/v'$

A changing denominator affects the whole quotient through a squared denominator and a subtraction. Use $\frac{u'v-uv'}{v^2}$.

### Misconception 3. A constant term remains after differentiation

A constant function independent of the input $x$ has rate of change $0$.

### Misconception 4. A mean loss derivative of $0$ means every sample derivative is $0$

Positive and negative sample derivatives can cancel in the mean. Conclusions about individual samples require checking their individual values.

## Exercises

### 1. Differentiate a sum with constant multiples

Find the derivative of

\[
f(x)=4x^3-5x+9
\]

<details>
<summary>Show solution</summary>

Differentiate term by term.

\[
\frac{d}{dx}(4x^3)=12x^2,
\qquad
\frac{d}{dx}(-5x)=-5,
\qquad
\frac{d}{dx}9=0
\]

Therefore,

\[
f'(x)=12x^2-5
\]

</details>

### 2. Differentiate a product

Use the product rule to find the derivative of

\[
f(x)=x^2(x+2)
\]

<details>
<summary>Show solution</summary>

With $u=x^2$ and $v=x+2$, we have $u'=2x$ and $v'=1$.

\[
f'(x)
=
u'v+uv'
=
2x(x+2)+x^2
\]

Therefore,

\[
f'(x)=3x^2+4x
\]

Expanding to $f(x)=x^3+2x^2$ and differentiating gives the same result.

</details>

### 3. Find an error in differentiating a product

For $u(x)=x^2$ and $v(x)=x^3$, a learner calculates $(uv)'=u'v'=6x^3$. Correct the error and find the derivative.

<details>
<summary>Show solution</summary>

The product rule is $u'v+uv'$.

\[
(uv)'
=
(2x)(x^3)+(x^2)(3x^2)
\]

\[
=
2x^4+3x^4
=5x^4
\]

The original product is $x^5$, so the power rule also gives $5x^4$.

</details>

### 4. Differentiate a quotient

Find the derivative and the allowed range of $x$ for

\[
g(x)=\frac{x}{x+1}
\]

<details>
<summary>Show solution</summary>

With $u=x$ and $v=x+1$, we have $u'=1$ and $v'=1$.

\[
g'(x)
=
\frac{1\cdot(x+1)-x\cdot1}{(x+1)^2}
=
\frac{1}{(x+1)^2}
\]

The value $x=-1$ makes the original denominator $0$ and is excluded. The domain is therefore $x\ne-1$.

</details>

### 5. Choose a rule

For each function, state which derivative rule applies first to its outermost operation.

1. $a(x)=x^3+x$
2. $b(x)=(x^2+1)(x-4)$
3. $c(x)=\frac{x^2}{x+2}$

<details>
<summary>Show solution</summary>

1. The two terms are added, so use the sum rule.
2. The two parenthesized expressions are multiplied, so use the product rule.
3. The numerator is divided by the denominator, so use the quotient rule. Exclude $x=-2$ from the domain.

Identifying the outermost operation determines which rule to choose.

</details>

### 6. Differentiate a mean loss

Let

\[
\mathcal L(\theta)
=
\frac{1}{3}
\bigl[\ell_1(\theta)+\ell_2(\theta)+\ell_3(\theta)\bigr]
\]

At the current point, $\ell_1'=3$, $\ell_2'=-1$, and $\ell_3'=4$. Find $\mathcal L'(\theta)$.

<details>
<summary>Show solution</summary>

Apply the sum and constant multiple rules.

\[
\mathcal L'(\theta)
=
\frac{1}{3}(3-1+4)
=
\frac{6}{3}
=2
\]

At the current point, the mean loss has a local slope in the increasing direction as $\theta$ increases.

</details>

### 7. Evaluate a claim about a mean slope

For the mean loss over all training data, $\mathcal L'(\theta)=0$. A researcher claims, "Every training sample's loss is insensitive to parameter $\theta$." Critique this conclusion and identify the values to check.

<details>
<summary>Show solution</summary>

A mean derivative of $0$ supports the statement that the sum of the sample derivatives is $0$. It does not tell us whether each $\ell_i'(\theta)$ is $0$. Positive and negative values may have canceled.

To claim insensitivity at the sample level, check each sample's $\ell_i'(\theta)$ or their distribution. This scalar mean alone also gives no conclusion about other parameter directions or evaluation data.

</details>

## Lesson summary

- For a constant multiple, keep the constant and differentiate the function. Differentiate sums and differences term by term.
- The product rule is $(uv)'=u'v+uv'$.
- The quotient rule is $\left(\frac{u}{v}\right)'=\frac{u'v-uv'}{v^2}$, with condition $v\ne0$.
- For a positive integer $n$, $\frac{d}{dx}x^n=nx^{n-1}$.
- The derivative of mean loss is the mean of the sample derivatives. A mean can hide individual values.

## Pass criteria

You pass if you can answer these questions without consulting the material:

- Can you write the sum and constant multiple rules as equations?
- Can you explain why the product rule has two terms?
- Can you write the quotient rule and check its denominator condition?
- Can you calculate derivatives of simple polynomials, products, and quotients?
- Can you explain the relationship between the derivative of mean loss and the sample derivatives?

## Next lesson

- [M01-06 Composite functions and the chain rule](M01-06-composition-chain-rule.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Sum, product, and quotient rules and their conditions are explained before use.
- [x] Product and quotient examples have been checked using alternative expansions.
- [x] Every exercise has a solution.
- [x] The scope of claims about mean loss and individual sample losses is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Neither the chain rule nor derivatives of exponentials and logarithms are required as prerequisites.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
