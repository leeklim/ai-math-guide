---
id: "N05-04"
title: "Activation functions and gating"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-03"
  - "M01-03"
estimated_time: "120~150 minutes"
---

# N05-04. Activation functions and gating

## Why this lesson matters

Composing several affine layers without other operations gives another single affine map. Neural networks insert activation functions between layers to produce slopes and output forms that depend on the input. Transformer feed-forward blocks go a step further: they use a gate whose value on one path modulates another path.

This lesson compares ReLU, sigmoid, GELU, and SiLU at the same inputs, then calculates the elementwise gates in GLU and SwiGLU. Examining function values alongside local derivatives connects forward activations with gradient flow.

## Learning objectives

After this lesson, you should be able to:

- Calculate the outputs of ReLU, sigmoid, GELU, and SiLU at small inputs.
- Distinguish an activation function's value from its local derivative.
- Calculate how an elementwise gate modulates the content path.
- Distinguish the gate functions in GLU and SwiGLU.
- Separate facts supported by activation differences from interpretive hypotheses.

## Prerequisite check

- Prerequisite lesson: [N05-03 MLP forward pass](N05-03-mlp-forward-pass.md)
- Prerequisite lesson: [M01-03 Derivatives and instantaneous rates of change](../../part-1-foundations/M01/M01-03-derivative-instantaneous-rate.md)
- Check question: Can you explain why an elementwise function preserves a tensor's shape?
- Check question: Can you explain the role of a local derivative in the chain rule?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $x$ | `x` | Scalar input to an activation function | $x\in\mathbb R$ |
| $\sigma(x)$ | `sigma of x` | Logistic sigmoid | $(0,1)$ |
| $\Phi(x)$ | `capital phi of x` | Standard normal cumulative distribution function | $(0,1)$ |
| $\operatorname{GELU}(x)$ | `G E L U of x` | Activation defined as $x\Phi(x)$ | $\mathbb R\to\mathbb R$ |
| $\operatorname{SiLU}(x)$ | `SiLU of x` | Activation defined as $x\sigma(x)$ | $\mathbb R\to\mathbb R$ |
| $\mathbf c$ | `c` | Content vector modulated by the gate | $\mathbb R^d$ |
| $\mathbf g$ | `g` | Gate pre-activation vector | $\mathbb R^d$ |
| $\odot$ | `elementwise product` | Hadamard product multiplying corresponding positions | The two operands have the same shape |

## Core concept 1. An activation function interrupts affine composition

Combining two affine maps without an activation gives another single affine map:

\[
\mathbf W_2(\mathbf W_1\mathbf x+\mathbf b_1)+\mathbf b_2
=\mathbf W'\mathbf x+\mathbf b'
\]

Inserting an elementwise function $\phi$ between them gives

\[
\mathbf y=\mathbf W_2\phi(\mathbf W_1\mathbf x+\mathbf b_1)+\mathbf b_2
\]

For a general nonlinear $\phi$, this expression cannot be reduced to a single affine map.

Above, $\mathbf W'=\mathbf W_2\mathbf W_1$ and $\mathbf b'=\mathbf W_2\mathbf b_1+\mathbf b_2$ are fixed independently of the input. With ReLU inserted, however, even the same unit passes its input or returns 0 depending on the input. Being expressible as an affine equation within one region is different from applying the same affine equation to all inputs.


The scalar curves below show the difference between an affine equation within one region and an affine equation valid over the entire input range.

<figure class="lesson-figure" markdown="1">

![A single affine line and a ReLU composite agree on one region but differ across the breakpoint](../../figures/assets/N05/N05-04-affine-composition.svg)

<figcaption>This scalar example illustrates the relationship. While 2(3x + 1) − 1 is a single straight line, 2ReLU(3x + 1) − 1 changes slope at x = −1/3. The affine equation for the region on the right does not hold for all inputs.</figcaption>

</figure>

## Core concept 2. Values and slopes of four activation functions

ReLU is

\[
\operatorname{ReLU}(x)=\max(0,x)
\]

It passes positive inputs through and returns 0 for negative inputs. PyTorch sets its derivative at $x=0$ to 0.

The sigmoid is

\[
\sigma(x)=\frac{1}{1+e^{-x}},
\qquad
\sigma'(x)=\sigma(x)(1-\sigma(x))
\]

Its output range $(0,1)$ makes it convenient for gating. As $|x|$ grows, its derivative approaches 0.

Differentiating the denominator gives $\sigma'(x)=e^{-x}/(1+e^{-x})^2$, which can be written as the product of $\sigma(x)$ and $1-\sigma(x)$. For a large positive input, the output is close to 1 but the slope is small. A large function value is not the same as sensitivity to a small input change.

GELU is

\[
\operatorname{GELU}(x)=x\Phi(x)
\]

It also passes negative inputs through as small negative values. SiLU is

\[
\operatorname{SiLU}(x)=x\sigma(x)
\]

Both are smooth, with derivative $1/2$ at $x=0$.

Applying the product rule to SiLU gives $\operatorname{SiLU}'(x)=\sigma(x)+x\sigma(x)(1-\sigma(x))$. Similarly, $\operatorname{GELU}'(x)=\Phi(x)+x\Phi'(x)$. At 0, the second term vanishes, leaving $\sigma(0)=\Phi(0)=1/2$. Both functions have output 0 there, but their slopes are not 0. The sigmoid's output $1/2$ must also be distinguished from its slope $1/4$.


Compare the negative-input and large-positive-input regions in the output curves below.

<figure class="lesson-figure" markdown="1">

![ReLU sigmoid exact GELU and SiLU curves distinguish negative outputs and bounded sigmoid outputs](../../figures/assets/N05/N05-04-activation-values.svg)

<figcaption>Solid and dashed line patterns and the legend distinguish the four functions. ReLU stays at 0 for negative inputs, whereas GELU and SiLU produce small negative values. Sigmoid stays below 1 even as the input grows.</figcaption>

</figure>


The next figure displays local derivatives at the same inputs on a separate vertical axis.

<figure class="lesson-figure" markdown="1">

![Local derivative curves include ReLU discontinuity and smooth GELU SiLU sigmoid slopes with explicit PyTorch zero convention](../../figures/assets/N05/N05-04-activation-derivatives.svg)

<figcaption>The vertical axis here is slope, not output value. At x = 0, GELU and SiLU have output 0 but slope 0.5. ReLU's open point marks the right-hand slope 1; the filled point marks the convention 0 used in backward computation.</figcaption>

</figure>


Aligning the two curves below at the same x reveals regions where a large function value coexists with a small slope.

<figure class="lesson-figure" markdown="1">

![Sigmoid value rises toward one while its derivative falls toward zero at large positive inputs](../../figures/assets/N05/N05-04-sigmoid-saturation.svg)

<figcaption>Read the value and slope curves at the same x. At x = 4, the value is about 0.982 but the local derivative is about 0.0177, so a large activation value must be distinguished from high sensitivity.</figcaption>

</figure>

## Core concept 3. A gate multiplies content by a modulating value

Write the smallest GLU form as

\[
\operatorname{GLU}(\mathbf c,\mathbf g)
=\mathbf c\odot\sigma(\mathbf g)
\]

Each element of $\sigma(\mathbf g)$ lies between 0 and 1, reducing or preserving the content magnitude at the corresponding position.

SwiGLU uses SiLU instead of a sigmoid gate:

\[
\operatorname{SwiGLU}(\mathbf c,\mathbf g)
=\mathbf c\odot\operatorname{SiLU}(\mathbf g)
\]

Because SiLU can return negative values, a SwiGLU gate is not merely a proportion or a probability. An actual Transformer block makes two affine projections from the same hidden state and then calculates this elementwise product.

Writing one GLU position as $u=c\sigma(g)$ gives $\partial u/\partial c=\sigma(g)$ and $\partial u/\partial g=c\sigma'(g)$. Sensitivity to changing the content differs from sensitivity to changing the gate input. If $c=0$, changing only the gate leaves this position's output unchanged, but the derivative with respect to content remains. If both paths originate from the same hidden state, its gradient includes the sum of contributions from both paths.

The product multiplies corresponding positions only; it does not directly mix different features. Interactions between different features arise in the preceding projections. For finite input, a sigmoid gate is a positive coefficient that reduces the content's absolute value. A SiLU gate, by contrast, can reverse its sign with a negative value or increase its magnitude with a value greater than 1.


In the c = 0 calculation below, examine the output value and the two local derivatives separately.

<figure class="lesson-figure" markdown="1">

![At content zero and gate input zero GLU output is zero while derivative with respect to content is one half and gate-input derivative is zero](../../figures/assets/N05/N05-04-gate-zero-content.svg)

<figcaption>Evaluating the text's c = 0 condition at g = 0 gives gate 0.5 and output 0. Differentiation with respect to c leaves the gate 0.5; differentiation with respect to g multiplies by c = 0 and therefore gives 0.</figcaption>

</figure>

## Example 1. Comparing four activation functions

### Problem

Calculate ReLU, sigmoid, GELU, and SiLU at $x=(-1,0,1)$.

### Solution

To four decimal places, the values are:

| $x$ | ReLU | sigmoid | GELU | SiLU |
|---:|---:|---:|---:|---:|
| $-1$ | $0$ | $0.2689$ | $-0.1587$ | $-0.2689$ |
| $0$ | $0$ | $0.5$ | $0$ | $0$ |
| $1$ | $1$ | $0.7311$ | $0.8413$ | $0.7311$ |

ReLU removes negative values. GELU and SiLU transform negative inputs into small negative outputs.

### What the result means

The choice of function changes both the forward value and the local derivative for the same pre-activation. These differences affect both the next layer's input and the gradient propagated backward.

## Example 2. GLU and SwiGLU

Let $\mathbf c=(2,-1,0.5)$ and $\mathbf g=(-1,0,1)$. The sigmoid gate is

\[
\sigma(\mathbf g)\approx(0.2689,0.5,0.7311)
\]

so

\[
\mathbf c\odot\sigma(\mathbf g)
\approx(0.5379,-0.5,0.3655)
\]

The SiLU gate is $(-0.2689,0,0.7311)$, and the SwiGLU output is

\[
(-0.5379,0,0.3655)
\]

The first component has a different sign because the SiLU gate allows negative values.


In the comparison of the first component below, the sign changes at the choice of gate function.

<figure class="lesson-figure" markdown="1">

![Gate input minus one branches to positive sigmoid and negative SiLU gates then multiplies the same content two to produce opposite signed outputs](../../figures/assets/N05/N05-04-gate-sign.svg)

<figcaption>The figure enlarges only the first position in the example. The same g₁ = −1 produces a positive sigmoid gate and a negative SiLU gate. Multiplying by the same content c₁ = 2 gives outputs with opposite signs.</figcaption>

</figure>

## Executable lab

### Execution environment and sources

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Checked on: 2026-10-01
- Component classification: activations are `Stable core`; SwiGLU is a `Common modern variant`
- Example ID: `n05_04_activation_gating`
- Code source: `labs/N05/n05_04_activation_gating.py`
- Test: `tests/N05/test_n05_04.py`
- Execution command: `.venv\Scripts\python.exe -m labs.N05.n05_04_activation_gating`

### Resource budget

The example uses only vectors of length 3. Its trainable parameter and training step counts are both 0, with a hard timeout of 10 seconds.

### Actual code and execution results

The site build inserts the source code and actual execution results at the following location.

<!-- N05_EXAMPLE: n05_04_activation_gating -->

### Numerical and gradient checks

The tests compare the four functions' outputs with fixed numerical values. SiLU's derivative at $x=(-1,0,1)$ is approximately $(0.0723,0.5,0.9277)$. The gate tests check the GLU and SwiGLU elementwise products separately.

## Connection to model interpretation

When collecting activations, distinguish pre-activations, values after the activation function, and values after the gated product. Even under the same unit name, different hook locations give different tensors.

Holding the same content fixed at a value other than 0 and comparing sigmoid gates, a larger gate value gives a larger output absolute value. Comparing only gate values across different inputs does not immediately determine the gated product's magnitude, because the content may also differ. Concluding that the component is necessary for model behavior requires interventions on the gate or content path and a comparison of outputs.


In the path below, distinguish feature mixing in the projections from positionwise multiplication at the gate.

<figure class="lesson-figure" markdown="1">

![One hidden state branches to content and gate affine projections then transformed gate and content join in an elementwise product](../../figures/assets/N05/N05-04-shared-hidden-gate.svg)

<figcaption>The projections that form content and gate inputs from the hidden state can mix features. The elementwise product where the two paths meet multiplies corresponding positions only. The pre-activation, gate output, and product are different observation locations in this arrangement.</figcaption>

</figure>

## Common misconceptions

### Misconception 1. A sigmoid output is the probability that a neuron is on

A sigmoid value is a number obtained from the specified computation. It can be interpreted as a probability only when defined as a parameter of a probabilistic model. A GLU gate value itself should not be called an event probability.

### Misconception 2. A smooth activation cannot have vanishing gradients

Sigmoid and SiLU derivatives can also become small in parts of the input range. Smoothness concerns the existence and continuity of derivatives; it does not guarantee gradient magnitude.

### Misconception 3. A large activation means an important feature

Activation magnitude depends on scale, normalization, and the next layer's weights. Evaluating its contribution to behavior requires checking downstream computation together with intervention results.

## Exercises

### 1. Calculating ReLU

Apply ReLU to $(-2,0,3)$ and state the local derivatives under the PyTorch convention.

<details>
<summary>Show solution</summary>

The output is $(0,0,3)$ and the derivative is $(0,0,1)$. PyTorch sets the ReLU derivative at 0 to 0.

</details>

### 2. Sigmoid derivative

Calculate $\sigma(0)$ and $\sigma'(0)$.

<details>
<summary>Show solution</summary>

$\sigma(0)=1/2$. Since $\sigma'(x)=\sigma(x)(1-\sigma(x))$, $\sigma'(0)=1/4$.

</details>

### 3. Gate shape

For $\mathbf c,\mathbf g\in\mathbb R^{B\times T\times d}$, what is the shape of $\mathbf c\odot\sigma(\mathbf g)$?

<details>
<summary>Show solution</summary>

The shape is $(B,T,d)$ because the product is elementwise. It multiplies corresponding positions along the three axes.

</details>

### 4. The sign of SwiGLU

If $c>0$ and $g<0$, determine the sign of $c\operatorname{SiLU}(g)$.

<details>
<summary>Show solution</summary>

Since $\sigma(g)>0$, $\operatorname{SiLU}(g)=g\sigma(g)<0$. Multiplying by $c>0$ gives a negative result as well.

</details>

### 5. Hook locations

One experiment stores affine outputs and another stores values after GELU. Can they be combined immediately into the same activation dataset?

<details>
<summary>Show solution</summary>

No. The first values are pre-activations, and the second are activations after a nonlinear transformation. Match the hook locations and tensor definitions, or record them as separate variables.

</details>

### 6. Critiquing a claim

For one prompt, a particular SwiGLU gate has the largest value. Evaluate the conclusion, “This gate caused the answer to be generated.”

<details>
<summary>Show solution</summary>

Magnitude observations alone do not establish causation. Distributions across other prompts and baselines, the interaction with downstream weights, and interventions changing the gate are needed.

</details>

## Evidence and update boundaries

The GELU definition follows [Gaussian Error Linear Units](https://arxiv.org/abs/1606.08415), GLU follows [Language Modeling with Gated Convolutional Networks](https://arxiv.org/abs/1612.08083), and Transformer GLU variants follow [GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202). This lesson covers function definitions and small tensor computations, without generalizing about their adoption rates in particular recent models.

## Lesson summary

- Activation functions insert nonlinear computation between affine layers.
- Function values and local derivatives play different roles in forward and backward computation.
- GLU multiplies content and a sigmoid gate elementwise.
- SwiGLU's SiLU gate allows negative values.
- Observing activation magnitude alone does not establish a component's causal importance.

## Pass criteria

You pass if you can answer these questions without consulting the material.

- Can you explain the definitions of the four activations and their differences near $x=0$?
- Can you distinguish local derivatives from activation values?
- Can you calculate GLU and SwiGLU on small vectors?
- Can you check a gate output's shape?
- Can you critique causal claims based on activation magnitude?

## Next lesson

- [N05-05 Logits, softmax, and cross entropy](N05-05-logits-softmax-cross-entropy.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Activation values and local derivatives are distinguished.
- [x] The gate definitions in GLU and SwiGLU are distinguished.
- [x] The actual example's numerical values and gradients are checked.
- [x] Every exercise has a solution.
- [x] The strength of model interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and math rendering have been checked.
- [x] Executable code is not manually duplicated in Markdown.
- [x] Code sources, test paths, resource budgets, and check dates are recorded.
- [x] Shape, numerical, and gradient tests are provided.
