---
id: "M01-07"
title: "Derivatives of exponential and logarithmic functions"
part: 1
stage: "M01"
status: "complete"
prerequisites:
  - "M00-05"
  - "M01-06"
estimated_time: "100~120 minutes"
---

# M01-07. Derivatives of exponential and logarithmic functions

## Why this lesson matters

Softmax turns logits into positive values using exponentials, while negative log-likelihood and cross-entropy apply logarithms to probabilities. Knowing these functions' rates of change lets us calculate how changes in scores propagate to probabilities and losses.

The natural exponential function is its own derivative, and the derivative of the natural logarithm is the reciprocal of its input. Applying the chain rule lets us divide even long probability-model derivative calculations into intermediate functions. A logarithm requires a positive input, so check its domain along with its derivative expression.

## Learning objectives

After completing this lesson, you will be able to:

- Find derivatives of the natural exponential function and general exponential functions.
- Explain the derivative and domain of the natural logarithm.
- Apply the chain rule to $\exp(g(x))$ and $\log(g(x))$.
- Calculate the rate of change of a negative log loss.
- Explain the relationship between a single-variable derivative of log-sum-exp and a softmax probability.

## Prerequisite check

- Prerequisite lesson: [M00-05 Exponents and logarithms](../M00/M00-05-exponents-logarithms.md)
- Prerequisite lesson: [M01-06 Composite functions and the chain rule](M01-06-composition-chain-rule.md)
- Check question: Can you explain why $\log(\exp(x))=x$ and state the domain of $\log x$?
- Check question: Can you calculate the derivative of $f(g(x))$ as $f'(g(x))g'(x)$?

If the inverse relationship between exponentials and logarithms is unclear, first review M00-05.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| $e$ | `e` | Natural constant that is the base of the natural exponential function | $e\approx2.71828$ |
| $\exp(x)$ | `the exponential of x` | Natural exponential function $e^x$ | Positive for every real $x$. |
| $\log x$ | `log of x` | Natural logarithm used in this textbook | $x>0$ |
| $a^x$ | `a to the x` | Exponential function with base $a$ | $a>0$, and usually $a\ne1$ |
| $\prod_{i=1}^{N}u_i$ | `product over i from one to N of u sub i` | Product notation for $u_1u_2\cdots u_N$ | $N$ is a positive integer. |
| Log-sum-exp | `log sum exp` | Function that takes the logarithm of a sum of exponentials | The logarithm's input must be positive. |

## Core concept 1. The natural exponential function is its own derivative

The natural constant $e$ is the base chosen so that the exponential function's instantaneous rate of change equals its value. Thus,

\[
\frac{d}{dx}e^x=e^x
\]

Writing the same result in $\exp$ notation gives

\[
\frac{d}{dx}\exp(x)=\exp(x)
\]

The difference quotient shows the role of the base. Applying the exponent rule $e^{x+h}=e^xe^h$ gives

\[
\frac{e^{x+h}-e^x}{h}
=
e^x\frac{e^h-1}{h}
\]

With reference input $x$ fixed, $e^x$ is independent of $h$. For the natural constant $e$, the limit of $(e^h-1)/h$ as $h\to0$ is $1$, so the entire limit is $e^x$. Separating the function value $e^x$ at the input from the rate coefficient determined by the base, this is the case in which the coefficient is $1$.

At $x=0$, $e^0=1$, so the tangent slope is also $1$. As $x$ increases and the function value grows, the derivative value grows by the same amount. The natural exponential function is positive at every real input, so its derivative is positive and the function increases.

In the figure below, the function's height and its tangent slope are both 1 at input zero.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The exponential curve passes through zero comma one and has a tangent of slope one there, matching the function value with its derivative](../../figures/assets/M01/M01-07-exp-height-slope.svg)

<figcaption>At x=0, the green curve's height is 1, and the purple tangent's slope is also 1. The natural exponential function's value and derivative value also agree at other inputs.</figcaption>
</figure>

## Core concept 2. A general exponential function has a factor of $\log a$

For $a>0$, write

\[
a^x=e^{x\log a}
\]

Applying the exponential function to the logarithm identity $\log(a^x)=x\log a$ recovers the original positive value $a^x$. The inner function here is $x\log a$. Holding base $a$ fixed makes $\log a$ constant, so the inner derivative is $\log a$. Applying the chain rule gives

\[
\frac{d}{dx}a^x
=
e^{x\log a}\log a
\]

and therefore

\[
\frac{d}{dx}a^x
=
a^x\log a
\]

For $a=e$, $\log e=1$, recovering the natural exponential formula. For $a>1$, $\log a>0$, so the derivative is positive. For $0<a<1$, $\log a<0$, so the derivative is negative and the function decreases.

Compare the directions of change for bases greater than and less than 1 in the figure below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Exponential functions with bases two and one half both equal one at zero but increase and decrease respectively](../../figures/assets/M01/M01-07-base-and-direction.svg)

<figcaption>2ˣ increases because log 2 is positive; 0.5ˣ decreases because log 0.5 is negative. Although both functions have the same value at x=0, their slopes have different directions.</figcaption>
</figure>

## Core concept 3. The derivative of the natural logarithm is $1/x$

Let $y=\log x$. The inverse relationship between exponentials and logarithms gives

\[
e^y=x
\]

Since $y$ is $\log x$ and varies with $x$, the left side is the composite function $\exp(y(x))$. Differentiating both sides with respect to $x$ multiplies the outer exponential's derivative $e^y$ by the inner derivative $dy/dx$. The derivative of $x$ on the right is $1$.

\[
e^y\frac{dy}{dx}=1
\]

Substituting $e^y=x$ gives

\[
x\frac{dy}{dx}=1
\]

so

\[
\frac{d}{dx}\log x
=
\frac1x,
\qquad x>0
\]

As $x$ approaches $0$ from the right, $1/x$ grows. The logarithm is sensitive to input changes in the small-positive-input region. The real natural logarithm is undefined for $x\le0$, so this formula does not apply there.

Read the logarithm's value and slope at the same input across the two graphs below. No logarithm curve is drawn for nonpositive inputs.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Aligned graphs of log x and its derivative one over x show steeper slopes at smaller positive inputs](../../figures/assets/M01/M01-07-log-and-slope.svg)

<figcaption>At x=0.2, 1, and 3, the logarithm's slopes are 5, 1, and 1/3, respectively. A decreasing logarithm height and an increasing slope are changes in different quantities.</figcaption>
</figure>

## Core concept 4. Apply the chain rule to composite exponentials and logarithms

Suppose $g$ is differentiable at the required point, and set $u=g(x)$. For a composite exponential,

\[
\frac{d}{dx}\exp(g(x))
=
\exp(g(x))g'(x)
\]

For a composite logarithm,

\[
\frac{d}{dx}\log(g(x))
=
\frac{g'(x)}{g(x)}
\]

First check the logarithm condition

\[
g(x)>0
\]

The logarithm derivative $g'(x)/g(x)$ connects to relative change with respect to the input value rather than absolute output change. Even for the same $g'(x)$, a smaller $g(x)$ produces a larger absolute rate of change in the logarithm.

Here, relative change means the change in $g$ divided by its current value $g(x)$. For small $\Delta x$, $\Delta g\approx g'(x)\Delta x$, so the relative change is approximately $[g'(x)/g(x)]\Delta x$. The logarithm's change has the same first-order approximation. Distinguish the denominator, which is the current logarithm input $g(x)$, from the original input $x$.

## Core concept 5. Logarithms express a product's derivative as a sum of relative rates

For $u(x)>0$ and $v(x)>0$,

\[
\log(u(x)v(x))
=
\log u(x)+\log v(x)
\]

Differentiating both sides gives

\[
\frac{u'v+uv'}{uv}
=
\frac{u'}u+\frac{v'}v
\]

The left side takes a logarithm of the product $uv$, so it divides the product's derivative $u'v+uv'$ by its current value $uv$. Splitting it into two terms gives $u'v/(uv)=u'/u$ and $uv'/(uv)=v'/v$. Thus, the product's relative rate of change equals the sum of its factors' relative rates. The logarithm identity and derivative rules calculate the same relationship in different orders.

The structure extends to products of multiple positive terms. Product notation means

\[
\prod_{i=1}^{N}u_i(x)
=
u_1(x)u_2(x)\cdots u_N(x)
\]

Therefore,

\[
\frac{d}{dx}
\log\left(\prod_{i=1}^{N}u_i(x)\right)
=
\sum_{i=1}^{N}
\frac{u_i'(x)}{u_i(x)}
\]

This explains why a product of probabilities is converted into a sum in the log-likelihood. Check that every term is positive.

## Core concept 6. Negative log loss has a large rate of change at small probabilities

Let $p$ be the probability the model assigns to the correct class. The negative log loss is

\[
\ell(p)=-\log p,
\qquad 0<p\le1
\]

Its derivative with respect to $p$ is

\[
\ell'(p)=-\frac1p
\]

The smaller $p$ is, the larger $|\ell'(p)|$ becomes. For example,

\[
\ell'(0.5)=-2,
\qquad
\ell'(0.01)=-100
\]

At a small correct-class probability, a small increase in probability produces a local rate that reduces loss more sharply.

If $p$ is itself a function of parameter $\theta$, the chain rule gives

\[
\frac{d\ell}{d\theta}
=
-\frac{1}{p(\theta)}p'(\theta)
\]

Multiply sensitivity with respect to probability by the rate at which the parameter changes that probability.

The figure below plots the absolute value of the negative log loss derivative with respect to probability. Both axes use logarithmic scales to show a wide range of small probabilities.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The magnitude one over p of the negative log loss derivative is one hundred at probability zero point zero one and two at probability one half](../../figures/assets/M01/M01-07-negative-log-sensitivity.svg)

<figcaption>As p decreases from 0.5 to 0.01, the magnitude of sensitivity to probability increases from 2 to 100. The actual derivative is negative, and a rate with respect to a parameter also requires dp/dθ.</figcaption>
</figure>

## Core concept 7. A softmax ratio appears in the derivative of log-sum-exp

Fix a constant $c$, and let

\[
F(x)=\log\left(e^x+e^c\right)
\]

Apply the chain rule and sum rule.

The inner function is $u(x)=e^x+e^c$. Since $c$ is fixed, the derivative of $e^c$ with respect to $x$ is $0$, so $u'(x)=e^x$. Multiplying this by the outer logarithm's derivative $1/u$ gives

\[
F'(x)
=
\frac{e^x}{e^x+e^c}
\]

The numerator is positive, and the denominator adds the positive quantity $e^c$, making it greater than the numerator. Thus,

\[
0<F'(x)<1
\]

This ratio equals the probability of the first class when softmax is applied to logits $x$ and $c$.

Here, we fixed $c$ and varied only $x$. We will study the full derivative of softmax when multiple logits vary together in multivariable differentiation and the Jacobian.

## Example 1. A composite natural exponential

For

\[
f(x)=\exp(3x-2)
\]

the inner function is $u=3x-2$, with $u'=3$. Therefore,

\[
f'(x)
=
\exp(3x-2)\cdot3
=
3\exp(3x-2)
\]

## Example 2. A composite logarithm

For

\[
g(x)=\log(x^2+1)
\]

we have $x^2+1>0$, so the function is defined for every real $x$. The chain rule gives

\[
g'(x)
=
\frac{2x}{x^2+1}
\]

## Example 3. A logarithm with a restricted domain

The function

\[
h(x)=\log(2x-1)
\]

is defined only when

\[
2x-1>0
\]

which requires $x>1/2$. Its derivative is

\[
h'(x)
=
\frac{2}{2x-1},
\qquad x>\frac12
\]

Do not write only the derivative and extend the domain to all real numbers.

## Example 4. Comparison with another logit held fixed

Setting $c=0$ gives

\[
F(x)=\log(e^x+1)
\]

and

\[
F'(x)=\frac{e^x}{e^x+1}
\]

At $x=0$,

\[
F'(0)=\frac{1}{2}
\]

The logits are equal, so softmax assigns equal probabilities to the two classes. This is a single-variable calculation with the other logit fixed at $0$.

The figure below separates the height of log-sum-exp from the softmax ratio at each input into upper and lower plots.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![With the other logit fixed at zero the derivative of log exp x plus one ranges between zero and one and equals one half at input zero](../../figures/assets/M01/M01-07-logsumexp-and-probability.svg)

<figcaption>The upper graph shows F, and the lower graph shows F′. The lower value is the first class's probability: 1/2 at x=0 and between 0 and 1 at other finite inputs.</figcaption>
</figure>

## Common misconceptions

### Misconception 1. The derivative of $e^x$ is $xe^{x-1}$

That expression incorrectly applies the power rule for $x^n$ to an exponential. The derivative of the natural exponential function is $e^x$.

### Misconception 2. The derivative of $\log x$ is $\log(1/x)$

The derivative of the natural logarithm is $1/x$. Do not apply another logarithm.

### Misconception 3. The derivative of $\log(g(x))$ is $1/g(x)$

The chain rule requires multiplication by the inner derivative $g'(x)$. The result is $g'(x)/g(x)$.

### Misconception 4. A finite logarithm derivative expression means the original logarithm is defined

The expression $\log(g(x))$ requires $g(x)>0$. An algebraic expression's form does not allow us to extend the domain.

### Misconception 5. A derivative with respect to one logit describes the whole softmax change

A single-variable rate with the other logits held fixed provides information in only one direction. Simultaneous changes in multiple logits require a derivative structure covering every input direction.

## Exercises

### 1. Differentiate a natural exponential

Find the derivative of

\[
f(x)=5e^x-2
\]

<details>
<summary>Show solution</summary>

The derivative of $e^x$ is $e^x$, and the constant term's derivative is $0$.

\[
f'(x)=5e^x
\]

</details>

### 2. Differentiate a general exponential

Find the derivative of

\[
g(x)=2^x
\]

and explain its sign.

<details>
<summary>Show solution</summary>

The general exponential formula gives

\[
g'(x)=2^x\log2
\]

Since $2^x>0$ and $\log2>0$, the derivative is positive for every real $x$. Thus, $2^x$ increases.

</details>

### 3. An exponential and the chain rule

Find the derivative of

\[
h(x)=\exp(-x^2)
\]

<details>
<summary>Show solution</summary>

The inner function $u=-x^2$ has derivative $u'=-2x$. The chain rule gives

\[
h'(x)
=
\exp(-x^2)(-2x)
=
-2x\exp(-x^2)
\]

</details>

### 4. A logarithm and its domain

Find the domain and derivative of

\[
q(x)=\log(3x+6)
\]

<details>
<summary>Show solution</summary>

The logarithm's input must be positive, so

\[
3x+6>0
\]

The domain is $x>-2$. The chain rule gives

\[
q'(x)
=
\frac{3}{3x+6}
=
\frac{1}{x+2},
\qquad x>-2
\]

</details>

### 5. Negative log loss

For

\[
\ell(p)=-\log p
\]

find $\ell'(0.2)$ and interpret its sign.

<details>
<summary>Show solution</summary>

Since

\[
\ell'(p)=-\frac1p
\]

we have

\[
\ell'(0.2)=-5
\]

Near $p=0.2$, increasing the correct-class probability $p$ moves the loss in the decreasing direction. This is a rate with respect to $p$; a rate with respect to a model parameter also requires $dp/d\theta$.

</details>

### 6. Differentiate log-sum-exp

Find the derivative of

\[
F(x)=\log(e^x+e^2)
\]

and calculate $F'(2)$.

<details>
<summary>Show solution</summary>

Apply the sum rule and chain rule.

\[
F'(x)=\frac{e^x}{e^x+e^2}
\]

At $x=2$, the exponential values are equal, so

\[
F'(2)
=
\frac{e^2}{e^2+e^2}
=
\frac12
\]

</details>

### 7. Evaluate a claim about a large rate at a small probability

A sample's correct-class probability is $p=0.001$, giving an absolute negative log loss derivative of $1000$ with respect to $p$. A researcher claims, "This sample produces the largest rate of change for every parameter." Critique the conclusion.

<details>
<summary>Show solution</summary>

The value $|d\ell/dp|=1000$ supports sensitivity of the loss to a change in correct-class probability $p$. For a parameter $\theta$,

\[
\frac{d\ell}{d\theta}
=
\frac{d\ell}{dp}
\frac{dp}{d\theta}
\]

so $dp/d\theta$ is also needed. For some parameters, the probability's rate of change may be small or $0$. Comparing magnitudes across samples also requires the same parameter, units, and evaluation conditions.

</details>

## Lesson summary

- The natural exponential function satisfies $\frac{d}{dx}e^x=e^x$.
- For a general exponential, $\frac{d}{dx}a^x=a^x\log a$.
- For the natural logarithm, $\frac{d}{dx}\log x=1/x$ on $x>0$.
- For composite functions, use $\frac{d}{dx}\exp(g)=\exp(g)g'$ and $\frac{d}{dx}\log(g)=g'/g$.
- Derivatives of negative log loss and log-sum-exp let us read changes in probability losses and softmax computations.

## Pass criteria

You pass if you can answer these questions without consulting the material:

- Can you write the derivatives of $e^x$, $a^x$, and $\log x$?
- Can you apply the chain rule to composite exponential and logarithmic functions?
- Can you check a logarithm's domain condition along with its derivative?
- Can you explain why negative log loss has a large rate of change at small probabilities?
- Can you calculate the derivative of log-sum-exp with the other logit held fixed?

## Next lesson

- [M01-08 Integration and accumulation](M01-08-integration-accumulation.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] The natural exponential function, natural logarithm, and domain are checked before use.
- [x] Exponential, logarithm, and chain rule examples have been checked.
- [x] Log-sum-exp is restricted to the single-variable setting.
- [x] Every exercise has a solution.
- [x] Claims about rates with respect to probability are distinguished from rates with respect to parameters.
- [x] The glossary and notation rules are followed.
- [x] Multivariable differentiation is not required as a prerequisite.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
