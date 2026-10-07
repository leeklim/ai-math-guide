---
id: "N05-02"
title: "A single neuron"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-01"
  - "M01-06"
estimated_time: "110–140 minutes"
---

# N05-02. A single neuron

## Why this lesson matters

A single neuron adds a bias to a weighted sum of its inputs, then applies an activation function. Decomposing this calculation lets us distinguish weights from activations and choose where to save or change a value.

This lesson does not describe a neuron as a model of a biological cell. It treats it as the smallest computational unit of the affine transformations and elementwise nonlinearities repeated in a neural network.

## Learning objectives

After this lesson, you will be able to:

- Calculate pre-activation from inputs, weights, and a bias.
- Distinguish affine transformations from linear transformations.
- Distinguish pre-activation from post-activation.
- Calculate a ReLU neuron's forward value and gradients by hand.
- Match directly written PyTorch tensor operations to each term in the equations.

## Prerequisite check

- Prerequisite lesson: [N05-01 Tensors and computation graphs](N05-01-tensors-computation-graphs.md)
- Prerequisite lesson: [M01-06 Composition and the chain rule](../../part-1-foundations/M01/M01-06-composition-chain-rule.md)
- Check: Can you calculate the dot product of two vectors of length 2?
- Check: Can you differentiate $L=(a-1)^2$ with respect to $a$?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\mathbf x$ | `x` | Input vector to the neuron | $\mathbf x\in\mathbb R^d$ |
| $\mathbf w$ | `w` | Weight vector collecting coefficients of input components | $\mathbf w\in\mathbb R^d$ |
| $b$ | `b` | Bias added to the dot product | $b\in\mathbb R$ |
| $z=\mathbf w^\top\mathbf x+b$ | `z equals w transpose x plus b` | Pre-activation before the activation function | $z\in\mathbb R$ |
| $a=\phi(z)$ | `a equals phi of z` | Post-activation after the activation function | $a\in\mathbb R$ |
| $\operatorname{ReLU}(z)$ | `ReLU of z` | Activation function defined as $\max(0,z)$ | $\mathbb R\to\mathbb R$ |
| $\mathcal L$ | `script L` | Scalar loss to be reduced in this example | $\mathcal L\in\mathbb R$ |

## Core concept 1. Weighted sum and bias

Adding a bias to the dot product of input $\mathbf x=(x_1,\ldots,x_d)$ and weight $\mathbf w=(w_1,\ldots,w_d)$ gives

\[
z=\mathbf w^\top\mathbf x+b
=\sum_{i=1}^{d}w_ix_i+b
\]

We call $z$ the pre-activation. Each $w_i$ controls the sign and magnitude of the corresponding input component's contribution to $z$. The bias $b$ shifts the entire sum without being multiplied by the input.

Input and weight vectors must have the same length to define each matching product. Summing all products leaves no feature index, so $z$ is a scalar. An actual contribution is $w_ix_i$, so its sign cannot be inferred from the weight's sign alone. Fixing other inputs and parameters and changing only $x_i$ gives $\Delta z=w_i\Delta x_i$. Thus, $w_i$ is also the coefficient of input change under these conditions.


The vertical layout shows calculation order, while the shared horizontal scale shows the sign and magnitude of each contribution.

<figure class="lesson-figure" markdown="1">

![Signed number line accumulation moves from zero to three then back to two and a half and two](../../figures/assets/N05/N05-02-signed-contributions.svg)

<figcaption>The first term adds 1.5 × 2 = 3. The second adds 0.5 × (−1) = −0.5, moving back. Adding bias −0.5 once more gives z = 2. Arrow lengths are proportional to the magnitudes of the contributions.</figcaption>

</figure>

## Core concept 2. An affine transformation includes a bias

$\mathbf w^\top\mathbf x$ is a linear map in $\mathbf x$. If $b\ne0$,

\[
f(\mathbf x)=\mathbf w^\top\mathbf x+b
\]

does not send the origin to the origin, so it is not a linear map. This form is called an affine transformation. Even if neural-network code calls a layer `Linear`, its mathematical function is affine when bias is enabled.

The bias cancels when comparing the difference between two inputs' outputs. For the same $\mathbf w,b$, $f(\mathbf x+\Delta\mathbf x)-f(\mathbf x)=\mathbf w^\top\Delta\mathbf x$. The linear part transforms the input change, while $b$ shifts the output's reference position. The classification as affine depends on inclusion of this constant shift, not on whether the output contains one number or several.


Compare the two lines to distinguish the shifted output reference from the shared slope.

<figure class="lesson-figure" markdown="1">

![Parallel linear and affine curves along the input ray show bias offset minus one half and equal slopes](../../figures/assets/N05/N05-02-affine-offset.svg)

<figcaption>Moving the input along x(s) = s(2, −1) gives linear output 2.5s and affine output 2.5s − 0.5 after adding bias. The lines have the same slope but different outputs at s = 0.</figcaption>

</figure>

## Core concept 3. Distinguish values before and after activation

With activation function $\phi$, the neuron output is

\[
a=\phi(z)=\phi(\mathbf w^\top\mathbf x+b)
\]

This lesson uses

\[
\operatorname{ReLU}(z)=\max(0,z)
\]

If $z>0$, then $a=z$; if $z\le0$, then $a=0$. The output at $z=0$ is also defined as 0. However, the left slope is 0 and the right slope is 1, so the ordinary derivative does not exist there. PyTorch uses 0 in the backward pass.

Calling both pre-activation $z$ and post-activation $a$ simply “activation” makes hook locations and gradient interpretation unclear. This book distinguishes them by name.

The two values agree in the positive region, but different negative $z$ values all map to the same $a=0$. Post-activation alone therefore cannot recover the magnitude of a negative pre-activation. Distinguishing storage locations is not merely giving them different names; it identifies what information remains before and after the nonlinear transformation.


On the ReLU curve, different negative values on the horizontal axis converge to output value 0.

<figure class="lesson-figure" markdown="1">

![ReLU curve shows pre-activation minus one half mapping to zero and pre-activation two mapping to two](../../figures/assets/N05/N05-02-relu-pre-post.svg)

<figcaption>Separate horizontal z and vertical a axes show z = −0.5 mapping to a = 0 and z = 2 mapping to a = 2. Along the horizontal segment in the negative region, multiple z values correspond to the same a.</figcaption>

</figure>

## Core concept 4. One hand calculation

Use the values

\[
\mathbf x=(2,-1),
\quad
\mathbf w=(1.5,0.5),
\quad
b=-0.5
\]

The pre-activation is

\[
z=1.5\cdot2+0.5\cdot(-1)-0.5=2
\]

Since $z>0$,

\[
a=\operatorname{ReLU}(2)=2
\]

Using the squared loss with target 1,

\[
\mathcal L=(a-1)^2
\]

gives $\mathcal L=1$.


The graph shows that z and a occupy different storage locations even when their numbers agree.

<figure class="lesson-figure" markdown="1">

![Weighted sum two passes through ReLU to activation two then target one gives squared loss one at distinct nodes](../../figures/assets/N05/N05-02-forward-loss.svg)

<figcaption>Although z and a both equal 2, they are different value nodes before and after ReLU. Target 1 enters the loss calculation; it is not added to the neuron's input or bias.</figcaption>

</figure>

## Core concept 5. Calculate gradients with the chain rule

Since $z=2>0$, $da/dz=1$ at the current point. Therefore,

\[
\frac{\partial\mathcal L}{\partial a}=2(a-1)=2,
\qquad
\frac{\partial\mathcal L}{\partial z}=2\cdot1=2
\]

Differentiating $z=\sum_iw_ix_i+b$ gives

\[
\frac{\partial\mathcal L}{\partial w_i}
=\frac{\partial\mathcal L}{\partial z}x_i,
\qquad
\frac{\partial\mathcal L}{\partial b}
=\frac{\partial\mathcal L}{\partial z}
\]

so we obtain

\[
\nabla_{\mathbf w}\mathcal L=(4,-2),
\qquad
\frac{\partial\mathcal L}{\partial b}=2
\]

The input gradient follows in the same way:

\[
\nabla_{\mathbf x}\mathcal L
=2\mathbf w=(3,1)
\]

In this example, $\partial z/\partial w_i=x_i$, $\partial z/\partial x_i=w_i$, and $\partial z/\partial b=1$. Differentiating with respect to a weight leaves the observed input as the coefficient; differentiating with respect to an input leaves the weight. Input and weight gradients multiply the same upstream derivative $\partial\mathcal L/\partial z$ by different local derivatives, according to the differentiation target. At particular values, the two vectors can have identical numbers while remaining derivatives with respect to different objects.

Here the loss depends on $z$ through $a$. If $z<0$, ReLU's local derivative is zero, so the gradient along this path is zero too. Changing the bias to give $a=0$, as in Example 1, leaves the loss against target 1 at 1 but blocks gradient transmission. Conversely, even in the positive region, the total gradient is zero if $a$ equals the target and the outer loss derivative is zero. The activation region and the loss error supply distinct factors in the chain rule.


In the branching diagram, choose the differentiation target first, then multiply by its local derivative.

<figure class="lesson-figure" markdown="1">

![Upstream derivative two branches to input derivatives multiplied by weights and parameter derivatives multiplied by inputs plus bias derivative](../../figures/assets/N05/N05-02-gradient-targets.svg)

<figcaption>Starting from the same dL/dz = 2, differentiating with respect to weights leaves x as the local derivative; differentiating with respect to inputs leaves w. The bias's local derivative is 1. Follow where the three differentiation targets branch apart.</figcaption>

</figure>


Comparing loss and local slopes in both cases identifies the cause of a zero gradient.

<figure class="lesson-figure" markdown="1">

![Two ReLU cases share loss one but pre-activation two has upstream derivative two while pre-activation minus one half has zero derivative](../../figures/assets/N05/N05-02-zero-gradient-loss.svg)

<figcaption>The original bias gives a = 2, while the other bias gives a = 0. Both have squared loss 1 against target 1. However, the latter's ReLU slope is zero, making dL/dz zero when multiplied by the outer derivative −2.</figcaption>

</figure>

## Example 1. Comparing the role of bias

### Problem

Keep $\mathbf x,\mathbf w$ above and change $b=-3$. What happens to $z$ and $a$?

### Solution

The dot product is $1.5\cdot2+0.5\cdot(-1)=2.5$. Thus, $z=2.5-3=-0.5$ and $a=\operatorname{ReLU}(-0.5)=0$.

### Meaning of the result

The bias moved the activation boundary without changing the weights. The same input can now lie in a different ReLU region, positive or negative.

## Example 2. Finding this calculation in a model

MLP and attention projections combine multiple neurons' affine transformations into one matrix operation. Observing an individual neuron's $z$ shows its value before the activation function; observing $a$ shows the value after the nonlinear transformation. A neuron's large $a$ may relate to a concept, but one large value alone does not establish that the model uses that concept.

## Execution exercise

### Execution environment and sources

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Verification date: 2026-10-01
- Component category: `Stable core`
- Example ID: `n05_02_single_neuron`
- Source code: `labs/N05/n05_02_single_neuron.py`
- Test: `tests/N05/test_n05_02.py`
- Run command: `.venv\Scripts\python.exe -m labs.N05.n05_02_single_neuron`

### Resource budget

This example uses an input of length 2, 3 trainable scalars, and 0 training steps. Each CPU thread count is 1, and the hard timeout is 10 seconds.

### Actual code and execution results

The site build inserts the `.py` source and actual execution results at the location below.

<!-- N05_EXAMPLE: n05_02_single_neuron -->

### Interpreting the results

The execution results `pre_activation=2.0`, `activation=2.0`, and `loss=1.0` match the hand calculation. `weight.grad=[4.0, -2.0]`, `bias.grad=2.0`, and `x.grad=[3.0, 1.0]` also agree with the chain-rule calculation.

This check goes beyond confirming that autograd produced values. Expected gradients are written independently and compared using `torch.testing.assert_close`.

## Common misconceptions

### Misconception 1. A transformation is linear even with a bias

For $b\ne0$, $\mathbf w^\top\mathbf x+b$ is an affine transformation. Distinguish framework class names from mathematical classifications.

### Misconception 2. Activation means both a function and an output value

Both uses occur in context, but tracing a calculation requires distinguishing activation function $\phi$ from activation value $a$. This book's glossary lists activation functions and activations separately.

### Misconception 3. A ReLU neuron's gradient is always its weight

In ReLU's positive region, $da/dz=1$, but in the negative region it is zero. The outer loss derivative must also be multiplied in, so the total gradient depends on the current input and loss.

## Exercises

### 1. Forward calculation

For $\mathbf x=(1,3)$, $\mathbf w=(2,-1)$, and $b=0.5$, calculate $z$ and the ReLU output $a$.

<details>
<summary>Show solution</summary>

$z=2\cdot1+(-1)\cdot3+0.5=-0.5$. Therefore, $a=0$.

</details>

### 2. Linear and affine

State the condition on $b$ for $f(\mathbf x)=\mathbf w^\top\mathbf x+b$ to be a linear map, and explain why.

<details>
<summary>Show solution</summary>

It requires $b=0$. A linear map must satisfy $f(\mathbf0)=0$, whereas this function has $f(\mathbf0)=b$.

</details>

### 3. Shape

If $\mathbf x,\mathbf w\in\mathbb R^5$ and $b\in\mathbb R$, what are the shapes of $z$ and $a$?

<details>
<summary>Show solution</summary>

The dot product $\mathbf w^\top\mathbf x$ and bias are scalars, so both $z$ and $a$ are scalar tensors with shape `()`.

</details>

### 4. Gradient

For a ReLU neuron with $z>0$ and $\mathcal L=(a-t)^2$, find $\partial\mathcal L/\partial b$.

<details>
<summary>Show solution</summary>

If $z>0$, $da/dz=1$ and $dz/db=1$. Therefore, $\partial\mathcal L/\partial b=2(a-t)$.

</details>

### 5. Negative region

Explain why $\partial\mathcal L/\partial\mathbf w$ is zero for a ReLU neuron with $z<0$ and a loss depending on $a$.

<details>
<summary>Show solution</summary>

For $z<0$, $a=0$ is constant, so $da/dz=0$. This factor enters the chain rule, making $\partial\mathcal L/\partial\mathbf w$ zero too. If another path connects the weights to the loss, that path's gradient must be added separately.

</details>

### 6. Interpretation claim

A neuron has a large activation on a particular word. Separate what this observation alone supports from what it does not.

<details>
<summary>Show solution</summary>

It supports saying that the neuron's post-activation was large for the specified input and model. It does not yet show that the neuron uniquely represents the word's concept or that the model uses this value to produce behavior. Comparison inputs, recoverability checks, and intervention evidence are also needed.

</details>

## Lesson summary

- A single neuron applies an activation function after an affine transformation.
- Weights are coefficients for input components, and the bias shifts the entire pre-activation.
- Pre-activation $z$ and post-activation $a$ are different graph nodes.
- ReLU's current region changes both the forward value and the gradient path.
- Autograd results should be compared with numerical values and gradients calculated by hand.

## Pass criteria

You pass when you can answer these questions without consulting the material:

- Can you expand $z=\mathbf w^\top\mathbf x+b$ into an elementwise sum?
- Can you distinguish linear transformations from affine transformations?
- Can you distinguish hook locations for pre-activation and post-activation?
- Can you calculate gradients in ReLU's positive and negative regions?
- Can you distinguish observing an activation from claiming the model functionally uses it?

## Next lesson

- [N05-03 MLP forward pass](N05-03-mlp-forward-pass.md)

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] All new symbols are defined before use.
- [x] Vector and scalar shapes are consistent.
- [x] Linear and affine transformations are distinguished.
- [x] Forward calculations and gradients are checked by hand.
- [x] Every exercise has a solution.
- [x] Strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and math rendering are checked.
- [x] Execution code is not manually duplicated in Markdown.
- [x] Source-code and test paths, resource budgets, and verification dates are recorded.
- [x] Shape, numerical-value, and gradient tests are provided.
