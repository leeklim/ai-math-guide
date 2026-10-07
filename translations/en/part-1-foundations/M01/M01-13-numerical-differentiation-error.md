---
id: "M01-13"
title: "Numerical differentiation and error"
part: 1
stage: "M01"
status: "complete"
prerequisites:
  - "M01-03"
  - "M01-11"
  - "M01-12"
estimated_time: "115~140 minutes"
---

# M01-13. Numerical differentiation and error

## Why this lesson matters

When a derivative formula is unavailable, or when checking an implemented gradient, evaluating a function at two nearby points can approximate its rate of change. This is numerical differentiation. A finite interval introduces error from terms omitted in a Taylor approximation, while an excessively small interval makes floating-point subtraction unstable.

Numerical differentiation helps check automatic-differentiation implementations and estimate a black-box function's local sensitivity. Because it gives an approximation, report the difference method, interval, and noise in function evaluations together.

## Learning objectives

After this lesson, you will be able to:

- Apply forward, backward, and central difference formulas.
- Distinguish why truncation error and roundoff error arise.
- Explain the problems caused by an interval $h$ that is too large or too small.
- Calculate a coordinatewise numerical gradient of a multivariable function.
- Assess how nondifferentiable points and noise affect the interpretation of numerical derivatives.

## Prerequisite check

- Prerequisite lesson: [M01-03. Differentiation and instantaneous rates of change](M01-03-derivative-instantaneous-rate.md)
- Prerequisite lesson: [M01-11. Directional derivatives and the gradient](M01-11-directional-derivative-gradient.md)
- Prerequisite lesson: [M01-12. Taylor approximation](M01-12-taylor-approximation.md)
- Check question: Can you explain the difference between a difference quotient and the limit defining a derivative?
- Check question: Can you explain how terms omitted from a first-order Taylor approximation become error?

Review the prerequisites first if difference quotients or Taylor remainders are unclear.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| $h$ | `h` | The interval from the reference point to an evaluation point ahead or behind it | Take $h>0$. The central difference evaluation points are $2h$ apart |
| Forward difference | `forward difference` | A derivative approximation using $x$ and $x+h$ | Only one evaluation point moves forward |
| Backward difference | `backward difference` | A derivative approximation using $x-h$ and $x$ | Only one evaluation point moves backward |
| Central difference | `central difference` | A derivative approximation using symmetric points $x-h$ and $x+h$ | Requires two function evaluations |
| Truncation error | `truncation error` | Error from omitting higher-order Taylor terms | Usually decreases as $h$ shrinks |
| Roundoff error | `roundoff error` | Error from storing and operating on numbers with finite precision | Can increase when $h$ is too small |
| Gradient check | `gradient check` | Comparing an analytical or automatic-differentiation gradient with numerical differences | Use the same function and point |

## Core concept 1. Approximate a derivative using a finite interval

The derivative is defined by

\[
f'(x)
=
\lim_{h\to0}
\frac{f(x+h)-f(x)}{h}
\]

A computer does not directly perform the limiting process with $h=0$. Instead, choose a small positive $h$ and use the difference quotient as an approximation.

The forward difference is

\[
f'(x)
\approx
\frac{f(x+h)-f(x)}{h}
\]

It requires two function values, $f(x)$ and $f(x+h)$.

The numbers from Example 1 show the two points selected by a forward difference and the output change between them.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Forward finite difference of x squared using inputs two and two point one with width zero point one and output change zero point four one](../../figures/assets/M01/M01-13-forward-points.svg)
  <figcaption>The orange points are reference input 2 and right-hand evaluation input 2.1. Dividing the vertical dashed length 0.41 by the horizontal length 0.1 gives 4.1. This is the average rate between the two points, not the exact derivative 4 at the reference point.</figcaption>
</figure>

## Core concept 2. A backward difference uses the other side

The backward difference is

\[
f'(x)
\approx
\frac{f(x)-f(x-h)}{h}
\]

Moving from the left point $x-h$ to the reference point $x$ changes the input by $x-(x-h)=h$. The output difference is therefore also taken in the order $f(x)-f(x-h)$. This average rate aligns the numerator and denominator's movement directions. Forward differences use a finite interval on the right, while backward differences use one on the left.

A one-sided difference may be needed at a domain boundary. For example, near $x=0$ for a function defined only at $x\ge0$, the point $x-h<0$ is outside the domain, so choose a forward difference.

A backward difference selects the interval to the left of the same reference point, so it subtracts output values in the order from that left point to the reference point.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Backward finite difference of x squared using inputs one point nine and two with width zero point one and output change zero point three nine](../../figures/assets/M01/M01-13-backward-points.svg)
  <figcaption>The evaluation points are 1.9 and 2. The output change corresponding to horizontal change 0.1 is 4−3.61=0.39, giving quotient 3.9. The reference point is the same as in the forward difference, but the interval examined differs.</figcaption>
</figure>

## Core concept 3. A central difference uses two symmetric points

The central difference is

\[
f'(x)
\approx
\frac{f(x+h)-f(x-h)}{2h}
\]

It uses points symmetrically on both sides of $x$. Their distance is $(x+h)-(x-h)=2h$, so the denominator is $2h$, not $h$. Averaging the two one-sided differences gives the same expression.

\[
\frac12\left(
\frac{f(x+h)-f(x)}{h}
+\frac{f(x)-f(x-h)}{h}
\right)
=\frac{f(x+h)-f(x-h)}{2h}
\]

The central value $f(x)$ cancels when the terms are added.

Using Taylor expressions,

\[
f(x+h)
\approx
f(x)+f'(x)h+\frac12f''(x)h^2+\cdots
\]

\[
f(x-h)
\approx
f(x)-f'(x)h+\frac12f''(x)h^2+\cdots
\]

Replacing $h$ with $-h$ reverses the first-order term's sign but preserves the second-order term's sign. Subtracting the expressions cancels the constant and second-order terms, leaving first-order term $2f'(x)h$. Dividing by $2h$ gives the desired $f'(x)$.

Differentiating the second derivative once more gives the third derivative. If derivatives through third order are continuous near the reference point, the leading term remaining after the second-order term has size $h^3$. A central difference divides this term by $2h$, giving leading error of size $h^2$. Forward and backward differences divide a numerator with a remaining second-order term by $h$, giving leading error of size $h$. This describes truncation error for small $h$; if the corresponding coefficient is 0, the error can be smaller or absent altogether.

A central difference joins the two points on either side rather than using the reference point itself. Their separation is twice the one-sided displacement.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Central finite difference of x squared between inputs one point nine and two point one spanning twice the one-sided interval](../../figures/assets/M01/M01-13-central-points.svg)
  <figcaption>The orange points are 2h=0.2 apart, with output difference 4.41−3.61=0.8. The quotient is 4. The slope is exact for this quadratic, but the secant joining these points need not pass through the function value at the reference point.</figcaption>
</figure>

## Core concept 4. A large $h$ increases truncation error

A finite difference approximates an instantaneous rate using the average rate over a short interval. A large $h$ mixes in the function's shape far from the reference point.

The Taylor expression for a forward difference is

\[
\frac{f(x+h)-f(x)}{h}
\approx
f'(x)+\frac12f''(x)h+\cdots
\]

A term multiplied by $h^2$ in the original function value remains after one division by $h$ in the quotient. Truncation error comes from omitting this term and treating the quotient as equal to $f'(x)$. The finite interval creates this difference even with infinitely precise function evaluations. Greater curvature can produce more error for the same $h$.

Comparing only truncation errors for a smooth function shows the effect of the terms removed by central-difference symmetry.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Log-scale forward and central truncation errors for the exponential at zero decreasing with first and second powers of interval h](../../figures/assets/M01/M01-13-truncation-orders.svg)
  <figcaption>The true derivative of eˣ at input 0 is 1. For small h, forward-difference error decreases with size h, while central-difference error decreases with size h². This compares truncation errors evaluated using stable expressions; it does not include subtraction instability at excessively small h.</figcaption>
</figure>

## Core concept 5. An excessively small $h$ can increase roundoff error

A computer stores real numbers using finitely many bits. For a very small $h$, stored values of $f(x+h)$ and $f(x)$ become almost identical. Subtracting similar numbers loses significant digits, and dividing that small difference by $h$ can amplify the error.

For example, suppose both function values are about 1 and differ by $10^{-8}$. If each evaluation has storage or calculation error of roughly $10^{-12}$, the difference itself may also have error of roughly $10^{-12}$. Dividing by $h=10^{-8}$ introduces error of roughly $10^{-4}$ into the derivative approximation. Even error small relative to each function value can become difficult to ignore in the quotient. Further reducing the interval may cause the computer to store $x+h$ as the same value as $x$, or round both function values to the same number.

Reducing $h$ therefore does not continually reduce error. Across several choices of $h$, truncation error usually decreases first, followed by increasing roundoff error at small $h$. Check whether several digits agree over a stable range.

Error within a small difference is amplified when that difference is divided by h. The amplification factor is separate from whether the error originates in storage precision or noisy function evaluation.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![A fixed difference error of one e minus twelve divided by varying h producing larger quotient error for smaller intervals](../../figures/assets/M01/M01-13-error-amplification.svg)
  <figcaption>This illustrative relationship fixes the numerator difference's error at 10⁻¹². Dividing by h=10⁻⁸ gives error 10⁻⁴ in the approximate rate. It does not assume that actual roundoff error or noise is constant for every h.</figcaption>
</figure>

Direct float64 subtraction in differences of the exponential function shows large and very small h producing errors for different reasons.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Actual NumPy float64 derivative errors of the exponential across interval sizes with rounding error dominating very small intervals](../../figures/assets/M01/M01-13-float64-error.svg)
  <figcaption>Forward and central differences of eˣ at input 1 were computed using NumPy float64 and compared with the true value e. Large h on the right shows truncation error; very small h on the left shows increasing numerical error. The smallest h is not the best choice, and curve details depend on the numerical implementation.</figcaption>
</figure>

## Core concept 6. Apply differences coordinatewise to a multivariable function

For $f:\mathbb R^n\to\mathbb R$, let $\mathbf e_i$ be the $i$th coordinate unit vector. The central-difference approximation to the $i$th partial derivative is

\[
\frac{\partial f}{\partial x_i}(\mathbf x)
\approx
\frac{f(\mathbf x+h\mathbf e_i)-f(\mathbf x-h\mathbf e_i)}{2h}
\]

The vector $\mathbf e_i$ has component 1 at index $i$ and 0 elsewhere. Thus $\mathbf x\pm h\mathbf e_i$ changes only coordinate $i$ by $\pm h$ while fixing the others. Both evaluations directly apply the condition of holding other variables fixed for partial differentiation.

Repeating this calculation for every coordinate gives a numerical gradient.

\[
\nabla f(\mathbf x)
\approx
\begin{bmatrix}
\dfrac{f(\mathbf x+h\mathbf e_1)-f(\mathbf x-h\mathbf e_1)}{2h}\\
\vdots\\
\dfrac{f(\mathbf x+h\mathbf e_n)-f(\mathbf x-h\mathbf e_n)}{2h}
\end{bmatrix}
\]

Two evaluations per coordinate make this expensive for high-dimensional inputs.

The central differences in Example 2 create separate evaluation-point pairs for each coordinate around the same input point.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Two coordinate slices with symmetric sample pairs around input point one comma two producing numerical gradient eight three](../../figures/assets/M01/M01-13-coordinate-samples.svg)
  <figcaption>Above, y=2 is fixed, and the output difference 1.6 between two x inputs is divided by 0.2 to give 8. Below, x=1 is fixed, and output difference 0.6 between two y inputs is divided by the same width to give 3. The two results form the gradient at the same evaluation point, (1,2).</figcaption>
</figure>

## Core concept 7. A gradient check compares the same function at the same point

Let $g_{\mathrm{ana}}$ be the value obtained by automatic differentiation or hand calculation, and let $g_{\mathrm{num}}$ be the central-difference value. One comparison measure is

\[
\operatorname{err}
=
\frac{|g_{\mathrm{ana}}-g_{\mathrm{num}}|}
{\max(1,|g_{\mathrm{ana}}|,|g_{\mathrm{num}}|)}
\]

For large values, the denominator measures relative discrepancy; when both values are near 0, it prevents the denominator from becoming excessively small.

Match these conditions when performing a gradient check:

- Use the same input, parameters, and scalar output.
- Fix variation from operations such as dropout or random sampling.
- Find a range of several $h$ values over which the results stabilize.

A small error shows that the calculations are close. It does not check whether both methods differentiated the same incorrect function.

## Core concept 8. Nondifferentiable points and noise alter difference results

Apply differences to ReLU $r(x)=\max(0,x)$ at $x=0$.

\[
\frac{r(h)-r(0)}{h}=1
\]

The forward difference is therefore $1$.

\[
\frac{r(0)-r(-h)}{h}=0
\]

The backward difference is $0$. The central difference is

\[
\frac{r(h)-r(-h)}{2h}
=
\frac12
\]

These three values differ, and none establishes the existence of a mathematical derivative. The left and right derivatives are unequal.

Noise in function evaluations can obscure the small numerator difference. Interpreting numerical derivatives requires recording repeated-evaluation variability, the seed, and the averaging method as well.

At the ReLU origin, each selected point pair gives a different secant slope. The central-difference number does not resolve the mismatch between left and right slopes.

<figure class="lesson-figure lesson-figure--wide" markdown="1">
  ![Forward backward and central secants at the ReLU corner yielding slopes one zero and one half](../../figures/assets/M01/M01-13-relu-three-rates.svg)
  <figcaption>The right-hand pair has slope 1, and the left-hand pair has slope 0. The purple central secant joining points on both sides has slope 0.5. The figure uses h=0.5, and each of these three difference values remains unchanged for any positive h. The mathematical derivative at the origin does not exist.</figcaption>
</figure>

## Example 1. Comparing three differences for a square function

Let $f(x)=x^2$, $x=2$, and $h=0.1$. The exact derivative is $f'(2)=4$.

The forward difference is

\[
\frac{f(2.1)-f(2)}{0.1}
=
\frac{4.41-4}{0.1}
=4.1
\]

The backward difference is

\[
\frac{f(2)-f(1.9)}{0.1}
=
\frac{4-3.61}{0.1}
=3.9
\]

The central difference is

\[
\frac{f(2.1)-f(1.9)}{0.2}
=
\frac{4.41-3.61}{0.2}
=4
\]

For a quadratic, the second-order term cancels in the symmetric difference, giving the exact value.

## Example 2. A multivariable central difference

Apply differences to

\[
f(x,y)=x^2+3xy
\]

at point $(1,2)$ with $h=0.1$.

The $x$-direction function values are

\[
f(1.1,2)=7.81,
\qquad
f(0.9,2)=6.21
\]

so

\[
\frac{\partial f}{\partial x}(1,2)
\approx
\frac{7.81-6.21}{0.2}
=8
\]

The $y$-direction function values are

\[
f(1,2.1)=7.3,
\qquad
f(1,1.9)=6.7
\]

so

\[
\frac{\partial f}{\partial y}(1,2)
\approx
\frac{7.3-6.7}{0.2}
=3
\]

These agree with $(8,3)^\top$, obtained by substituting $(1,2)$ into the analytical gradient $(2x+3y,3x)^\top$.

## Example 3. Checking stability across interval sizes

Suppose the true derivative is unknown. Central differences give the following results:

| $h$ | Approximation |
|---:|---:|
| $10^{-1}$ | $1.046$ |
| $10^{-2}$ | $1.0005$ |
| $10^{-3}$ | $1.0000$ |
| $10^{-6}$ | $1.0000$ |
| $10^{-12}$ | $0.9984$ |

The value stabilizes between $10^{-3}$ and $10^{-6}$. At $10^{-1}$, truncation error is large; at $10^{-12}$, roundoff error may be suspected. Do not trust all reported digits from one interval alone.

## Example 4. Finite differences of a black-box score

Suppose internal model derivatives are inaccessible, but the input score $s(x)$ can be queried. The central difference

\[
\frac{s(x+h)-s(x-h)}{2h}
\]

approximates local sensitivity in the $x$ direction.

This value uses only function-value changes near the queried point. How the model processes that feature internally, whether the change is plausible under the data distribution, and causal effects require separate experiments.

## Common misconceptions

### Misconception 1. Choosing the smallest possible $h$ gives the best accuracy

Small $h$ reduces truncation error but can increase roundoff error and subtraction instability. Compare multiple intervals.

### Misconception 2. A central-difference value establishes that a derivative exists

Central differences return numbers even at points without derivatives, such as the ReLU origin. Compare left and right differences.

### Misconception 3. Agreement between numerical gradients and automatic differentiation proves the entire implementation correct

The check validates a derivative implementation under the assumption that both calculations differentiate the same scalar-valued function. It does not automatically detect errors in data processing or objective definitions.

### Misconception 4. One difference between function evaluations is unaffected by noise

Stochastic models and random operations can give different values at the same input. Fix the seed and evaluation mode, and check repeated-evaluation variability.

### Misconception 5. Black-box finite differences reveal internal causal mechanisms

Finite differences measure local input–output changes. They do not directly reveal internal computational paths or causal use.

## Exercises

### 1. Calculating a forward difference

For $f(x)=x^2$, $x=3$, and $h=0.01$, calculate the forward difference.

<details>
<summary>Show solution</summary>

\[
\frac{f(3.01)-f(3)}{0.01}
=
\frac{9.0601-9}{0.01}
=6.01
\]

It differs from the exact derivative $f'(3)=6$ by $0.01$.

</details>

### 2. Calculating a central difference

For $f(x)=x^2$, $x=3$, and $h=0.01$, calculate the central difference.

<details>
<summary>Show solution</summary>

\[
f(3.01)=9.0601,
\qquad
f(2.99)=8.9401
\]

Therefore,

\[
\frac{9.0601-8.9401}{0.02}
=
\frac{0.12}{0.02}
=6
\]

A quadratic's central difference equals its exact derivative.

</details>

### 3. Comparing difference methods

For $f(x)=x^2$, $x=2$, and $h=0.1$ from Example 1, find the average of the forward and backward differences and compare it with the central difference.

<details>
<summary>Show solution</summary>

The forward difference is $4.1$ and the backward difference is $3.9$. Their average is

\[
\frac{4.1+3.9}{2}=4
\]

This equals central-difference value $4$. Combining symmetric-point information cancels the opposing errors of the one-sided differences.

</details>

### 4. Differences at the ReLU origin

For $r(x)=\max(0,x)$ and $h>0$, find the forward, backward, and central differences at $x=0$, and assess differentiability.

<details>
<summary>Show solution</summary>

The forward difference is

\[
\frac{r(h)-r(0)}h=1
\]

and the backward difference is

\[
\frac{r(0)-r(-h)}h=0
\]

The central difference is

\[
\frac{r(h)-r(-h)}{2h}=\frac12
\]

Because the left and right rates differ, the derivative does not exist at $x=0$.

</details>

### 5. Explaining interval selection

Explain the main errors arising in numerical differentiation when $h$ is too large and when it is too small.

<details>
<summary>Show solution</summary>

A large $h$ increases truncation error because the average rate over a finite interval differs from the instantaneous rate at the reference point. Higher-order terms and curvature are not removed sufficiently.

An excessively small $h$ causes subtraction of nearby function values to lose significant digits. Dividing that difference by a small $h$ can amplify roundoff error. Find a stable range across several choices of $h$.

</details>

### 6. Gradient-check error

For $g_{\mathrm{ana}}=2.0000$ and $g_{\mathrm{num}}=2.0002$, calculate

\[
\operatorname{err}
=
\frac{|g_{\mathrm{ana}}-g_{\mathrm{num}}|}
{\max(1,|g_{\mathrm{ana}}|,|g_{\mathrm{num}}|)}
\]

<details>
<summary>Show solution</summary>

The numerator is $0.0002$, and the denominator is $2.0002$.

\[
\operatorname{err}
=
\frac{0.0002}{2.0002}
\approx
9.999\times10^{-5}
\]

This is a normalized discrepancy of about $10^{-4}$. The tolerance must be chosen to suit the calculation precision and function smoothness.

</details>

### 7. M01 cumulative assessment: A composite function's gradient and numerical check

Consider the computation graph

\[
(x,y)
\longrightarrow
u=2x-y
\longrightarrow
\mathcal L=(u-1)^2
\]

At point $(x,y)=(2,1)$, perform the following tasks:

1. Calculate forward values $u$ and $\mathcal L$.
2. Use the chain rule to find $\nabla\mathcal L$.
3. Find the directional derivative along unit direction $\mathbf v=(3/5,4/5)^\top$.
4. Check the partial derivative with respect to $x$ using central differences.
5. State one model-interpretation claim that these results alone do not support.

<details>
<summary>Show solution</summary>

The forward calculation is

\[
u=2\cdot2-1=3
\]

\[
\mathcal L=(3-1)^2=4
\]

The local derivatives are

\[
\frac{\partial\mathcal L}{\partial u}=2(u-1)=4,
\qquad
\frac{\partial u}{\partial x}=2,
\qquad
\frac{\partial u}{\partial y}=-1
\]

By the chain rule,

\[
\frac{\partial\mathcal L}{\partial x}=4\cdot2=8,
\qquad
\frac{\partial\mathcal L}{\partial y}=4(-1)=-4
\]

so

\[
\nabla\mathcal L(2,1)
=
\begin{bmatrix}8\\-4\end{bmatrix}
\]

The directional derivative is

\[
D_{\mathbf v}\mathcal L
=
\begin{bmatrix}8&-4\end{bmatrix}
\begin{bmatrix}3/5\\4/5\end{bmatrix}
=
\frac{24}{5}-\frac{16}{5}
=
\frac85
\]

For $h>0$, holding $y=1$ fixed gives

\[
\mathcal L(2+h,1)=(2+2h)^2
\]

\[
\mathcal L(2-h,1)=(2-2h)^2
\]

The central difference is

\[
\frac{(2+2h)^2-(2-2h)^2}{2h}
=
\frac{16h}{2h}
=8
\]

which agrees with the analytical partial derivative.

The results check local rates of change for the selected function and point. They do not establish an actual model's generalization performance, sensitivities at other data points, or the causal importance of inputs $x,y$.

</details>

## Lesson summary

- Forward and backward differences approximate a derivative using function values on one side of the reference point.
- Central differences use symmetric-point values to reduce the leading truncation error for smooth functions.
- Large $h$ can increase truncation error; excessively small $h$ can increase roundoff error and subtraction instability.
- Coordinatewise central differences form a numerical gradient that can check automatic-differentiation results.
- Numerical differentiation approximates local input–output change. It does not guarantee differentiability or establish internal mechanisms or causal effects.

## Pass criteria

You have passed this lesson if you can answer these questions without consulting the material:

- Can you write forward, backward, and central difference formulas?
- Can you distinguish truncation error from roundoff error?
- Can you explain why several $h$ values should be compared?
- Can you calculate a numerical gradient using coordinatewise central differences?
- Can you explain why a difference value cannot be identified with a derivative at a nondifferentiable point?

## M01 stage pass criteria

You have passed M01 if you can perform the following tasks without consulting the material:

- Define a derivative as the limit of average rates of change.
- Differentiate composite functions using sum, product, quotient, and chain rules.
- Collect partial derivatives into a gradient and calculate directional derivatives.
- Approximate small changes using a first-order Taylor expression.
- Check an analytical gradient with central differences and explain sources of error.
- Distinguish local-sensitivity claims supported directly by derivatives from causal claims requiring additional evidence.

## Next lesson

- [M02-01. Vectors and vector operations](../M02/M02-01-vectors-vector-operations.md)

## Author checklist

- [x] The learning objectives describe observable actions.
- [x] The three finite differences and two error types are defined.
- [x] Single-variable and multivariable numerical-differentiation examples have been checked.
- [x] Cautions for nondifferentiable points and stochastic functions are explained.
- [x] Every exercise has a solution.
- [x] The M01 cumulative assessment and stage pass criteria are included.
- [x] Numerical sensitivity is distinguished from internal-mechanism and causal claims.
- [x] The glossary and notation rules are followed.
- [x] Internal links and mathematical delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
