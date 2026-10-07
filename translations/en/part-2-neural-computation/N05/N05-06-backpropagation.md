---
id: "N05-06"
title: "Backpropagation"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-05"
  - "M03-14"
estimated_time: "120~150 minutes"
---

# N05-06. Backpropagation

## Why this lesson matters

Even when one loss depends on millions of parameters, each path consists of compositions of small operations. Backpropagation propagates derivatives starting at a scalar loss through the computation graph in reverse order. Each node uses values saved during the forward pass together with its own local derivative.

This lesson differentiates one scalar graph by hand and compares the result with PyTorch autograd. The goal is to understand gradient calculation as a separate stage preceding the optimizer update.

## Learning objectives

After this lesson, you should be able to:

- Calculate intermediate values in a forward graph in order.
- Propagate gradients by multiplying an upstream gradient by a local derivative.
- Explain why gradients must be added when one value is used along multiple paths.
- Explain how gradient storage differs between leaf and intermediate tensors.
- Distinguish backpropagation from parameter updates.

## Prerequisite check

- Prerequisite lesson: [N05-05 Logits, softmax, and cross entropy](N05-05-logits-softmax-cross-entropy.md)
- Prerequisite lesson: [M03-14 Automatic differentiation and backpropagation](../../part-1-foundations/M03/M03-14-automatic-differentiation-backpropagation.md)
- Check question: Can you apply the chain rule for a composition to scalar expressions?
- Check question: Can you distinguish partial derivatives from total derivatives?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $x$ | `x` | Scalar input | $\mathbb R$ |
| $w,b,v,c$ | `w, b, v, and c` | Parameters of the computation graph | $\mathbb R$ |
| $z$ | `z` | Intermediate value of the first affine operation | $\mathbb R$ |
| $h$ | `h` | Intermediate value after the square activation | $\mathbb R$ |
| $\hat y$ | `y hat` | Prediction | $\mathbb R$ |
| $\mathcal L$ | `script L` | Squared-error loss | $[0,\infty)$ |
| $\bar z$ | `z bar` | Adjoint abbreviating $\partial\mathcal L/\partial z$ | $\mathbb R$ |
| VJP | `V J P` | Vector-Jacobian product | A basic operation of reverse mode |

## Core concept 1. The forward pass saves values

Use the following scalar graph:

\[
z=wx+b,
\qquad
h=z^2,
\qquad
\hat y=vh+c,
\qquad
\mathcal L=(\hat y-y)^2
\]

The forward pass calculates $z$, $h$, $\hat y$, and $\mathcal L$ in order. The backward pass uses forward values needed for local derivatives. For example, evaluating the local derivative $2z$ of $h=z^2$ requires the $z$ obtained during the forward pass.

Backward computation is not an inverse-function calculation recovering inputs from outputs. It calculates derivatives at the same evaluation point defined by the inputs and parameters already used. Although $h=z^2$ loses the sign of $z$, retaining the forward $z$ makes it possible to determine the local derivative's sign correctly. This is why both forward values and connection information are used.


Trace the forward values and the point where the loss target joins the computation below.

<figure class="lesson-figure" markdown="1">

![Scalar forward chain computes z one h one prediction three and loss four with fixed input parameters and target](../../figures/assets/N05/N05-06-forward-values.svg)

<figcaption>The figure uses the example's x = 2, w = 1, b = −1, v = 3, c = 0 in order. Although forward values z = 1 and h = 1 are numerically equal, they result from different operations and determine different local derivatives during backward computation.</figcaption>

</figure>


In the next figure, compare tangents at two inputs corresponding to the same h.

<figure class="lesson-figure" markdown="1">

![A square curve has value one at stored inputs minus one and plus one but tangent slopes minus two and plus two](../../figures/assets/N05/N05-06-stored-square-input.svg)

<figcaption>Both z = −1 and z = 1 produce h = 1, but their tangent slopes are −2 and 2. Instead of recovering z from h, backward computation substitutes the stored z into 2z to determine the local derivative.</figcaption>

</figure>

## Core concept 2. Reverse mode proceeds from the loss toward the inputs

Starting from the loss gives

\[
\frac{\partial\mathcal L}{\partial\hat y}
=2(\hat y-y)
\]

The derivative propagated one step earlier to $h$ is

\[
\frac{\partial\mathcal L}{\partial h}
=\frac{\partial\mathcal L}{\partial\hat y}
\frac{\partial\hat y}{\partial h}
=\frac{\partial\mathcal L}{\partial\hat y}v
\]

Next,

\[
\frac{\partial\mathcal L}{\partial z}
=\frac{\partial\mathcal L}{\partial h}
\frac{\partial h}{\partial z}
=\frac{\partial\mathcal L}{\partial h}2z
\]

Each step multiplies the upstream gradient by the local derivative.

Begin with the derivative of the scalar loss with respect to itself, 1, and proceed in reverse order. The upstream gradient measures how much a change in the current value affects the final loss. The local derivative measures how much a change immediately before this operation affects the current value. Multiplying them gives the first-order effect on the loss of a change one step earlier. This follows derivative dependencies backward rather than solving the forward equations in reverse.


In the figure below, propagate loss derivatives by multiplying local derivatives.

<figure class="lesson-figure" markdown="1">

![Reverse seed one multiplies squared error derivative four then affine factor three then square factor two to produce adjoints four twelve twenty four](../../figures/assets/N05/N05-06-reverse-chain.svg)

<figcaption>Start from loss seed 1 and multiply local derivatives 2(ŷ − y) = 4, v = 3, and 2z = 2 in order. The node labels 4, 12, 24 are derivatives of the loss, not forward values.</figcaption>

</figure>

## Core concept 3. Parameter and input gradients

For $z=wx+b$,

\[
\frac{\partial z}{\partial w}=x,
\qquad
\frac{\partial z}{\partial x}=w,
\qquad
\frac{\partial z}{\partial b}=1
\]

Thus,

\[
\frac{\partial\mathcal L}{\partial w}=\bar z x,
\qquad
\frac{\partial\mathcal L}{\partial x}=\bar z w,
\qquad
\frac{\partial\mathcal L}{\partial b}=\bar z
\]

Backpropagation can calculate gradients for both parameters and inputs. The optimizer updates values using gradients of the parameters registered for training.

The second affine operation similarly gives $\partial\mathcal L/\partial v=(\partial\mathcal L/\partial\hat y)h$ and $\partial\mathcal L/\partial c=\partial\mathcal L/\partial\hat y$. The target $y$ is fixed in this calculation. Whether the differentiation target is an input or a parameter determines the local derivative; whether it is registered with the optimizer determines the subsequent update target. Calculating an input gradient does not automatically train the input sample.


Select a different local factor for each differentiation target in the diagram below.

<figure class="lesson-figure" markdown="1">

![Adjoint twenty four branches to input weight bias derivatives while prediction adjoint four branches to output weight and bias derivatives](../../figures/assets/N05/N05-06-gradient-leaves.svg)

<figcaption>From z̄ = 24, three branches differentiate with respect to w, x, b; from ŷ̄ = 4, two branches differentiate with respect to v, c. The derivative for input x is calculated too, but only parameters registered with the optimizer are subsequent update targets.</figcaption>

</figure>

## Core concept 4. Gradients from branching paths are added

If one node $u$ is used in two subsequent computations $a(u)$ and $b(u)$, and the loss depends on both,

\[
\frac{d\mathcal L}{du}
=\frac{\partial\mathcal L}{\partial a}\frac{da}{du}
+\frac{\partial\mathcal L}{\partial b}\frac{db}{du}
\]

Reverse-mode autodiff accumulates contributions returning from each outgoing path at the same node. Backward computation for a residual connection follows this addition rule too.

A small change in $u$ changes both $a$ and $b$ at once. The loss's first-order change sums the contributions from changes in each subsequent value, so one should neither choose just one path nor multiply the two derivatives. Contributions of opposite signs can cancel. A summed gradient of 0 is therefore different from the absence of a downstream path.


In the figure below, add contributions multiplied along each path at their shared input.

<figure class="lesson-figure" markdown="1">

![For a u squared branch and a three u branch at u one their local derivative contributions two and three join by addition to five](../../figures/assets/N05/N05-06-branch-gradient-sum.svg)

<figcaption>This small calculation uses a = u², b = 3u, L = a + b at u = 1. Multiplying each path's upstream derivative 1 by its local derivative gives 2 and 3; add the two contributions returning as derivatives with respect to the same u.</figcaption>

</figure>


In the next figure, identify where the two paths' signs cancel.

<figure class="lesson-figure" markdown="1">

![Two nonzero local derivative contributions plus one and minus one join to total zero without removing either path](../../figures/assets/N05/N05-06-path-cancellation.svg)

<figcaption>To illustrate cancellation, let a = u, b = −u, L = a + b. Each path retains its derivative, 1 or −1, but their sum is 0. Distinguish an absent path from canceling contributions.</figcaption>

</figure>

## Example 1. Calculating forward values

### Problem

Calculate all intermediate values and the loss for $x=2$, $w=1$, $b=-1$, $v=3$, $c=0$, $y=1$.

### Solution

\[
z=1\cdot2-1=1,
\qquad
h=1^2=1
\]

and

\[
\hat y=3\cdot1+0=3,
\qquad
\mathcal L=(3-1)^2=4
\]

### What the result means

Forward values are fixed before the backward calculation. Even in the same graph, changing the forward input or parameters changes the evaluation values of local derivatives.

## Example 2. Calculating backward values

Starting from the loss gives

\[
\bar{\hat y}=2(3-1)=4
\]

In order, we obtain

\[
\bar h=4\cdot3=12,
\qquad
\bar z=12\cdot2\cdot1=24
\]

The leaf values' gradients are

\[
\bar w=24\cdot2=48,
\quad
\bar x=24\cdot1=24,
\quad
\bar b=24,
\quad
\bar v=4\cdot1=4,
\quad
\bar c=4
\]

## Executable lab

### Execution environment and sources

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Checked on: 2026-10-01
- Component classification: `Stable core`
- Example ID: `n05_06_backpropagation`
- Code source: `labs/N05/n05_06_backpropagation.py`
- Test: `tests/N05/test_n05_06.py`
- Execution command: `.venv\Scripts\python.exe -m labs.N05.n05_06_backpropagation`

### Resource budget

The example uses scalar tensors and 4 parameters. There is no optimizer or training step, and the hard timeout is 10 seconds.

### Actual code and execution results

The site build inserts the source code and actual execution results at the following location.

<!-- N05_EXAMPLE: n05_06_backpropagation -->

### Forward and gradient checks

The tests first check $z=1$, $h=1$, $\hat y=3$, $\mathcal L=4$. Next, they compare intermediate gradients and the gradients of $x,w,b,v,c$ with hand-calculated values. Separate assertions check that the code ran and that the derivatives are correct.

## Viewing intermediate gradients in PyTorch

A leaf tensor with `requires_grad=True` has a `.grad` after backward computation. Intermediate tensors do not preserve `.grad` by default, even though gradients are needed along their graph connections. For educational checks, the example calls `retain_grad()` on $z$, $h$, and $\hat y$.

Retaining every intermediate gradient in an actual model increases memory use. Specify the layers and tokens to analyze first, and collect only the tensors needed.


In the figure below, distinguish derivative propagation from optional storage.

<figure class="lesson-figure" markdown="1">

![Intermediate adjoint is used to propagate to the input regardless of whether its optional grad storage is retained](../../figures/assets/N05/N05-06-intermediate-grad-storage.svg)

<figcaption>The solid line propagating z's derivative toward the input is separate from the choice to save it in z.grad. Backward computation proceeds even when z.grad is None under the default behavior. Calling retain_grad() requests storage of this intermediate derivative.</figcaption>

</figure>

## Connection to model interpretation

Gradient attribution measures a selected scalar output's sensitivity to inputs or activations using local derivatives. A gradient of 0 means its first-order change is 0 at the current input point. It does not establish that the component is useless for all inputs.

Gradients depend on model parameters, the forward input, and the selected target scalar. An analysis report must record which logit or logit difference was used as the backward starting point.

## Common misconceptions

### Misconception 1. Calling backward updates parameters

Backward calculates gradients and accumulates them in `.grad`. The optimizer's `step()` performs the parameter update.

### Misconception 2. `.grad` automatically becomes 0 on each call

PyTorch accumulates leaf gradients. Repeated training requires a step clearing gradients before the next backward computation.


Read the parameter value and accumulated .grad value separately in the figure below.

<figure class="lesson-figure" markdown="1">

![Two identical backward contributions forty eight accumulate in weight gradient from zero to forty eight to ninety six while parameter weight remains one without optimizer steps](../../figures/assets/N05/N05-06-gradient-accumulation.svg)

<figcaption>Suppose w.grad is initially 0 and the example's forward computation is rebuilt to add the same derivative contribution 48 twice. Without clearing gradients in between, w.grad accumulates from 48 to 96. Without an optimizer step, parameter w = 1 remains unchanged.</figcaption>

</figure>

### Misconception 3. A large gradient guarantees a large causal effect

A gradient is first-order sensitivity to an infinitesimal perturbation at the current point. With large finite interventions, nonlinear saturation, or out-of-distribution inputs, the actual change can differ from the linear approximation.

## Exercises

### 1. Recalculating the forward pass

If only $x$ changes to 3 in the example, find $z,h,\hat y,\mathcal L$.

<details>
<summary>Show solution</summary>

$z=1\cdot3-1=2$, $h=4$, $\hat y=12$, $\mathcal L=(12-1)^2=121$.

</details>

### 2. Local derivative

Find $dh/dz$ for $h=z^2$ at $z=-2$.

<details>
<summary>Show solution</summary>

Since $dh/dz=2z$, it is $-4$. The value of $h$ is 4, but the derivative is negative.

</details>

### 3. Upstream gradient

If $\partial\mathcal L/\partial h=5$, $h=z^2$, and $z=3$, find $\partial\mathcal L/\partial z$.

<details>
<summary>Show solution</summary>

Multiplying upstream gradient 5 by local derivative $2z=6$ gives 30.

</details>

### 4. Adding paths

Find $d\mathcal L/du$ for $a=u^2$, $b=3u$, $\mathcal L=a+b$.

<details>
<summary>Show solution</summary>

The $a$ path contributes $2u$ and the $b$ path contributes 3. Adding the paths gives $d\mathcal L/du=2u+3$.

</details>

### 5. Gradient accumulation

Two `backward()` calls on the same graph each contribute 4 to $w$, without clearing gradients between them. Find the final `w.grad`.

<details>
<summary>Show solution</summary>

It is 8 because PyTorch accumulates leaf gradients. To retain only the second contribution, the previous gradient would need to be cleared.

</details>

### 6. Critiquing a claim

Evaluate the conclusion that a neuron is unnecessary for the model because its activation gradient is 0 at one input.

<details>
<summary>Show solution</summary>

This establishes only that the local gradient is 0 for the current input and target scalar. It does not establish the neuron's overall necessity without checking other inputs, finite interventions, and path interactions.

</details>

## Evidence and update boundaries

Reverse differentiation through a computation graph follows the classical construction in [Learning representations by back-propagating errors](https://www.nature.com/articles/323533a0) and reverse-mode automatic differentiation. This lesson covers a scalar graph and PyTorch's public autograd behavior without assuming a particular optimizer or large-model implementation.

## Lesson summary

- The forward pass produces intermediate values needed for local derivatives during backward computation.
- Reverse mode propagates gradients from a scalar loss through the graph in reverse order.
- At each edge, the upstream gradient is multiplied by the local derivative.
- Gradients from multiple paths returning to one node are added.
- Backward gradient calculation and optimizer parameter updates are separate stages.

## Pass criteria

You pass if you can answer these questions without consulting the material.

- Can you calculate a scalar graph's forward values in order?
- Can you distinguish upstream gradients from local derivatives?
- Can you calculate every leaf gradient in the example by hand?
- Can you explain why gradients are added at branching paths?
- Can you limit claims based on local gradient observations?

## Next lesson

- [N05-07 Gradient descent and mini-batches](N05-07-gradient-descent-mini-batch.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Forward values and backward gradients are distinguished.
- [x] Upstream gradients and local derivatives are connected.
- [x] Path addition and gradient accumulation are explained.
- [x] Every exercise has a solution.
- [x] The strength of model interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and math rendering have been checked.
- [x] Executable code is not manually duplicated in Markdown.
- [x] Code sources, test paths, resource budgets, and check dates are recorded.
- [x] Shape, numerical, and gradient tests are provided.
