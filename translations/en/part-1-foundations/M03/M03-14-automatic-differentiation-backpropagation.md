---
id: "M03-14"
title: "Automatic differentiation and backpropagation"
part: 1
stage: "M03"
status: "complete"
prerequisites:
  - "M01-06"
  - "M03-10"
  - "M03-13"
estimated_time: "130–155 minutes"
---

# M03-14. Automatic differentiation and backpropagation

## Why this lesson matters

Neural network gradients are not obtained by expanding one enormous differentiation formula. We divide the program into small operations and connect their values and local derivatives through the chain rule. This procedure is automatic differentiation. In training problems with scalar outputs, reverse mode calculates gradients for many parameters in one backward propagation. This particular use is usually called backpropagation.

Understanding automatic differentiation connects implementation terms such as forward pass, backward pass, computation graph, gradient accumulation, detach, and checkpointing to mathematical expressions. It also prevents confusion between the roles of symbolic, numerical, and automatic differentiation when checking gradients.

## Learning objectives

After this lesson, you will be able to:

- Distinguish automatic differentiation from symbolic and numerical differentiation.
- Identify computation-graph nodes, edges, and local derivatives.
- Propagate primal values and tangents together in forward mode.
- Propagate cotangents in reverse order in reverse mode.
- Sum gradient contributions when a variable branches into multiple paths.
- Explain backpropagation as reverse-mode automatic differentiation of a scalar loss.
- Explain the tradeoff between stored memory and recomputation.

## Prerequisite check

- Prerequisite: [M01-06 Function composition and the chain rule](../M01/M01-06-composition-chain-rule.md)
- Prerequisite: [M03-10 Total derivative and differential](M03-10-total-derivative-differential.md)
- Prerequisite: [M03-13 JVPs and VJPs](M03-13-jvp-vjp.md)
- Check: Can you express the derivative of a composition as a product of local derivatives?
- Check: Can you distinguish the orders in which JVPs and VJPs traverse a computation graph?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning |
|---|---|---|
| primal | `primal` | A value calculated by the original program |
| tangent | `tangent` | A first-order change in a value along an input direction |
| cotangent | `cotangent` | A backward sensitivity for changes in a scalar output |
| $\dot z$ | `z dot` | The tangent of variable $z$ |
| $\bar z$ | `z bar` | The cotangent arriving at variable $z$; for a scalar loss, $\partial L/\partial z$ |
| local derivative | `local derivative` | A derivative between one operation's inputs and outputs |
| seed | `seed` | The tangent or cotangent that starts automatic differentiation propagation |
| tape | `tape` | A record of operation order and intermediate values needed for the reverse pass |

## Core concept 1. Automatic differentiation applies the chain rule to a program

Automatic differentiation uses a program built from differentiable elementary operations and the values produced by its execution. Each elementary operation, such as addition, multiplication, exponentiation, or matrix multiplication, has a differentiation rule. Composing these rules in the actual execution order gives the desired derivative product.

For example,

\[
a=xy,\qquad z=a+x,\qquad L=z^2
\]

can be divided into three local operations:

\[
(x,y)\mapsto a=xy,\qquad (a,x)\mapsto z=a+x,\qquad z\mapsto L=z^2.
\]

Each local differentiation rule is short:

\[
da=y\,dx+x\,dy,\qquad dz=da+dx,\qquad dL=2z\,dz.
\]

Here, $dx,dy$ are first-order input changes, and $da,dz,dL$ are their first-order effects through each operation. Substituting local rules at the current values $x,y,z$ gives

\[
dL=2z(da+dx)=2z\bigl((y+1)dx+x\,dy\bigr)
\]

The coefficients of $dx,dy$ are the full function's derivatives with respect to the corresponding inputs. Connecting local rules lets us calculate these coefficients without first expanding the full expression for $L$.

Automatic differentiation propagates these relationships in the required direction. A long closed-form derivative expression need not be constructed first.

## Core concept 2. Symbolic, numerical, and automatic differentiation serve different purposes

Symbolic differentiation transforms an expression into another expression. It suits obtaining human-readable derivative formulas such as $d(x^2)/dx=2x$, but repeated subexpressions can make formulas large for large computation graphs.

Numerical differentiation approximates a directional derivative for small $\varepsilon$ as

\[
\frac{L(\boldsymbol\theta+\varepsilon\mathbf v)-L(\boldsymbol\theta)}{\varepsilon}
\]

It is useful as an implementation check, but has truncation and floating-point errors and is expensive for gradients with many coordinates.

Automatic differentiation calculates derivative products at the executed point using the chain rule. Assuming correct differentiation rules for elementary operations, it introduces no finite-difference error. Rounding errors from floating-point arithmetic itself remain.

## Core concept 3. A computation graph records value dependencies

A computation-graph node is an input or intermediate value. A directed edge shows that a value is used by a subsequent operation. In the preceding example, $x$ is used in both paths through $a=xy$ and $z=a+x$. The final gradient with respect to $x$ must therefore include contributions from both paths.

The local inputs of $z=a+x$ are $a$ and $x$. Differentiating only this operation holds the other local input fixed, giving $\partial z/\partial a=1$ and $\partial z/\partial x=1$. The fact that $a$ itself depends on $x$ is accounted for separately by following the path $x\to a\to z$. Including the entire upstream path effect in the local derivative would count the same contribution twice.

The graph is not identical to the differentiable function itself. Different operation orders can implement the same function, with different intermediate nodes and memory use. Automatic differentiation applies rules to the chosen program path.

First check the primal values at the branch where the same input x is used by two nodes.

<figure class="lesson-figure" markdown="1">

![Input x two branches into a product with y three and an identity copy then both branches join at z eight and square to loss sixty four](../../figures/assets/M03/M03-14-primal-graph.svg)

<figcaption>The input x=2 enters both multiplication a=xy and the copy b=x. Adding those values gives z=8, whose square gives L=64. Arrows show value-use dependencies, not movement through a geometric space.</figcaption>

</figure>

## Core concept 4. Forward mode propagates primal values and tangents together

Once the input direction $(\dot x,\dot y)$ is specified, each operation calculates its value and tangent together.

The seeds $\dot x,\dot y$ specify the rate of change of the path $(x+t\dot x,y+t\dot y)$ at $t=0$. Dots on intermediate values likewise denote derivatives when this path is supplied to the program. Multiplication therefore adds both inputs' first-order effects through the product rule; squaring multiplies by the derivative $2z$ at the current value $z$.

\[
\begin{aligned}
a&=xy, & \dot a&=y\dot x+x\dot y,\\
z&=a+x, & \dot z&=\dot a+\dot x,\\
L&=z^2, & \dot L&=2z\dot z.
\end{aligned}
\]

This calculates the full function's JVP as a composition of local JVPs. One forward-mode execution propagates the effect of one input direction to every intermediate value and output. It is advantageous when few input directions are needed.

## Core concept 5. Reverse mode propagates cotangents in reverse order

For scalar $L$, use $\bar L=1$ as the seed. Using values from the forward pass, propagate cotangents in reverse operation order.

Other nodes' cotangents are initialized to 0, and arriving contributions are added. The cotangent $\bar z$ is the sensitivity multiplying an input change's effect through $z$ on $L$; it is not the value $z$ being sent back. Before propagating backward through a node, all contributions from output-side paths using it must have been collected.

\[
\bar z=\bar L\frac{\partial L}{\partial z},\qquad
\bar a=\bar z\frac{\partial z}{\partial a},\qquad
\bar x\mathrel{+}=\bar z\frac{\partial z}{\partial x}.
\]

Then propagate backward through $a=xy$:

\[
\bar x\mathrel{+}=\bar a\frac{\partial a}{\partial x},\qquad
\bar y\mathrel{+}=\bar a\frac{\partial a}{\partial y}.
\]

The notation $\mathrel{+}=$ means adding a new path's contribution to those already received. Reverse mode applies local VJPs successively. With one output and many inputs, one reverse pass can give gradients for all input coordinates.

Here, $x$ contributes once as a direct input of $z=a+x$ and again as an input of $a=xy$. The final results are $\bar x=\bar z+\bar a y$ and $\bar y=\bar a x$. Substituting $\bar z=2z$ and $\bar a=\bar z$ gives the coefficients $2z(y+1),2zx$ of $dx,dy$ from the first section. Overwriting the first path's contribution with the second would remove one term from this sum.

## Core concept 6. Backpropagation is reverse-mode automatic differentiation of a neural network loss

Neural network layers are also compositions of elementary operations such as matrix multiplication, bias addition, and activation functions. For a scalar loss $L$, start with $\bar L=1$ and apply each layer's local VJP from back to front. This calculation is backpropagation.

For example, let $\mathbf z=\mathbf W\mathbf x+\mathbf b$ with $\mathbf W\in\mathbb R^{m\times n}$ and output cotangent $\bar{\mathbf z}\in\mathbb R^m$. The contribution sent to input $\mathbf x$ is $\mathbf W^\top\bar{\mathbf z}$. Each weight entry $W_{ij}$ appears in output $z_i$ as $W_{ij}x_j$, so its gradient contribution is $\bar z_i x_j$. The contribution for bias entry $b_i$ is $\bar z_i$. If the weights and biases are used only in this operation, collecting the gradients into arrays gives

\[
\nabla_{\mathbf W}L=\bar{\mathbf z}\mathbf x^\top\in\mathbb R^{m\times n},
\qquad
\nabla_{\mathbf b}L=\bar{\mathbf z}\in\mathbb R^m
\]

If the same parameters are also used in other operations, add those path contributions to the affine operation's contribution. Backpropagation thus propagates input sensitivities while collecting derivative coefficients for the weights and biases to be learned. The cumulative assignment in M03-15 applies these rules to a small network.

Distinguish backpropagation from an optimizer update. Backpropagation calculates $\nabla_{\boldsymbol\theta}L$. SGD or Adam uses the calculated gradient to update $\boldsymbol\theta$. Calculating a gradient does not automatically change the parameters.

## Core concept 7. Reverse mode incurs intermediate-value storage costs

The backward rule for multiplication $a=xy$ needs forward values $x$ and $y$. The backward rule for ReLU needs to know which inputs were positive. Reverse mode therefore usually stores forward-pass intermediate values or information from which to recover them.

Storing every value makes the reverse pass fast but uses substantial memory. Storing only some values and recomputing the others reduces memory while increasing computation. Checkpointing adjusts this tradeoff. The issue is not changing the derivative formula's accuracy, but the computational and memory costs of obtaining the same derivative.

Obtaining the same derivative requires recomputed intermediate values to agree with the original forward pass. Changing parameters between passes, or using different random outcomes in stochastic operations, may propagate local derivatives at different values. Even when storage and recomputation choices change, preserve the original execution's inputs, parameters, selected path, and required random outcomes.

## Example 1. Forward mode on a computation graph

### Problem

For

\[
a=xy,\qquad b=x,\qquad z=a+b,\qquad L=z^2
\]

with $(x,y)=(2,3)$ and input direction $(\dot x,\dot y)=(1,-1)$, calculate $\dot L$.

### Solution

First calculate the primal values:

\[
a=6,\qquad b=2,\qquad z=8,\qquad L=64.
\]

Propagate tangents in the same order:

\[
\dot a=y\dot x+x\dot y=3-2=1,
\]

\[
\dot b=\dot x=1,\qquad \dot z=\dot a+\dot b=2,
\]

\[
\dot L=2z\dot z=2\cdot 8\cdot 2=32.
\]

### What the result means

Moving the input along direction $(1,-1)$ gives a first-order rate of change of $32$ for $L$. This must agree with the inner product of the full gradient and direction.

Recording primal values and tangents together in Example 1 keeps track of where each local differentiation rule is evaluated.

<figure class="lesson-figure" markdown="1">

![Each graph node records its primal and tangent with seeds one minus one combining to tangent two at z and thirty two at the loss](../../figures/assets/M03/M03-14-forward-graph.svg)

<figcaption>The multiplication tangent is 3×1+2×(-1)=1, and the copy path's tangent is 1. At z, their sum 2 is multiplied by the squaring derivative 16 at the current z, giving the loss tangent 32.</figcaption>

</figure>

## Example 2. Reverse mode on the same graph

Start with $\bar L=1$.

\[
\bar z=2z=16,
\]

\[
\bar a=16,\qquad \bar b=16.
\]

Adding contributions from $a=xy$ and $b=x$ gives

\[
\bar x=\bar a y+\bar b=16\cdot 3+16=64,
\]

\[
\bar y=\bar a x=16\cdot 2=32.
\]

Thus,

\[
\nabla L(2,3)=
\begin{bmatrix}
64\\32
\end{bmatrix}.
\]

Comparing with the forward-mode result gives

\[
\nabla L(2,3)^\top
\begin{bmatrix}
1\\-1
\end{bmatrix}
=64-32=32=\dot L
\]

This confirms that both modes calculate the same derivative in different propagation directions.

The reverse path starts with loss seed 1 and sums both contributions to x.

<figure class="lesson-figure" markdown="1">

![Loss cotangent seed one travels backward through the graph and the product and copy contributions forty eight and sixteen sum to input cotangent sixty four](../../figures/assets/M03/M03-14-reverse-graph.svg)

<figcaption>The multiplication path sends 16×3=48 to x, and the copy path sends 16. The cotangent at x is therefore 64. Overwriting either contribution with the other loses the full gradient.</figcaption>

</figure>

## Example 3. Check implementation results with finite differences

The function is

\[
L(x,y)=x^2(y+1)^2
\]

so the gradient at $(2,3)$ is $(64,32)$. The central difference along direction $\mathbf v=(1,-1)^\top$ is

\[
\frac{L((2,3)+\varepsilon\mathbf v)-L((2,3)-\varepsilon\mathbf v)}{2\varepsilon}
\]

It approaches $32$ for suitably small $\varepsilon$. An overly large $\varepsilon$ increases approximation error; an overly small $\varepsilon$ can increase rounding and cancellation errors. Finite differences independently check automatic differentiation results; they are not the default way to calculate gradients during training.

Calculating this central difference in float64 can show increasing error again for extremely small steps.

<figure class="lesson-figure" markdown="1">

![Actual float64 central difference error decreases then rises as the step becomes extremely small compared with derivative thirty two](../../figures/assets/M03/M03-14-difference-error.svg)

<figcaption>The reference directional derivative is 32. Approximation error at large steps and rounding/cancellation error at very small steps occur in different regions. Errors calculated as exactly zero are omitted because they cannot be shown on a logarithmic axis.</figcaption>

</figure>

## Example 4. Why gradients add at a branch

In $z=x^2+x$, the input $x$ branches into a squaring path and an identity path. Reverse mode combines the contributions as

\[
\bar x=\bar z\cdot 2x+\bar z\cdot 1
\]

If $\bar z=1$, then $dz/dx=2x+1$. Keeping only one path calculates only part of the variable's effect, not its total effect.

Calculating gradients, changing parameters, and storing intermediate values serve different roles.

<figure class="lesson-figure" markdown="1">

![Forward pass computes loss backward pass computes gradients and only the separate optimizer step changes parameters](../../figures/assets/M03/M03-14-gradient-versus-update.svg)

<figcaption>After backpropagation, gradients at the current parameters are ready. Updating parameters using an optimizer such as SGD or Adam is a separate step.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A sequence stores every intermediate value in one row while the second row checkpoints alternate values and recomputes the others](../../figures/assets/M03/M03-14-checkpoint-storage.svg)

<figcaption>The upper row stores every intermediate value; the lower stores some and recomputes the rest. Obtaining the same derivative requires matching inputs, parameters, and required random outcomes even when the amounts of storage and recomputation change.</figcaption>

</figure>

## Common misconceptions

### Misconception 1. Automatic differentiation automatically performs numerical differentiation

Automatic differentiation does not repeatedly evaluate function values for finite differences. It applies elementary differentiation rules and the chain rule along the executed path.

### Misconception 2. Backpropagation and gradient descent are the same process

Backpropagation calculates gradients; gradient descent updates parameters using them. The processes may run consecutively, but their roles differ.

### Misconception 3. A branching variable needs only the first gradient contribution to arrive

All directed paths through which the variable affects the output must contribute to the sum. Omitting any calculates derivatives of only some paths, not the total derivative.

### Misconception 4. Reverse mode turns the original function into its inverse

“Reverse” refers to cotangent propagation order. Individual operations need not be inverted; reverse-mode rules can also be applied to operations such as ReLU that have no inverse function.

### Misconception 5. Automatic differentiation gradients have a uniquely determined meaning at every point

At nondifferentiable points such as ReLU at 0, the library returns its chosen convention. Executed branches, detach, and in-place modifications can also affect results. Check program differentiability and implementation rules.

## Exercises

### 1. Distinguish three differentiation methods

What are the names for simplifying the derivative of $f(x)=\sin(x^2)$ into a formula, calculating $[f(x+\varepsilon)-f(x)]/\varepsilon$, and composing local derivatives of the executed $x^2$ and $\sin$ operations, respectively?

<details>
<summary>Show solution</summary>

They are symbolic differentiation, numerical differentiation, and automatic differentiation, respectively. All concern derivatives, but they differ in result form, errors, and computational purpose.

</details>

### 2. Forward-mode propagation

For $a=x^2$ and $z=\exp(a)$, let $x=1$ and $\dot x=3$. Calculate $a,z,\dot a,\dot z$.

<details>
<summary>Show solution</summary>

\[
a=1,\qquad z=e,
\]

\[
\dot a=2x\dot x=6,\qquad \dot z=\exp(a)\dot a=6e.
\]

</details>

### 3. Reverse-mode propagation

For $a=x^2$ and $L=3a$, let $x=-2$. Start with $\bar L=1$ and calculate $\bar a$ and $\bar x$.

<details>
<summary>Show solution</summary>

We have $\bar a=\bar L\,\partial L/\partial a=3$. Then

\[
\bar x=\bar a\frac{\partial a}{\partial x}=3(2x)=-12
\]

</details>

### 4. Gradient accumulation

Calculate $L=x^2+3x$ with the graph $a=x^2$, $b=3x$, $L=a+b$. At $x=2$, calculate each path's contribution to $\bar x$ and the final result.

<details>
<summary>Show solution</summary>

With $\bar L=1$, we have $\bar a=1$ and $\bar b=1$. The $a$ path contributes $2x=4$, and the $b$ path contributes $3$. Thus, $\bar x=4+3=7$.

</details>

### 5. Compare JVPs and VJPs

At one point of $f:\mathbb R^{1000}\to\mathbb R$, gradients for all input coordinates are needed. Which mode, forward or reverse, usually requires fewer seed executions?

<details>
<summary>Show solution</summary>

Reverse mode obtains gradients for $1000$ input coordinates with one output cotangent seed, $1$. Coordinate-wise forward mode requires up to $1000$ standard-basis directions. Actual costs also depend on operation structure and memory constraints.

</details>

### 6. Memory and recomputation

State which cost is reduced and which costs increase when some regions are recomputed instead of storing every activation needed for the reverse pass.

<details>
<summary>Show solution</summary>

The stored activation memory is reduced. Repeating some forward operations before the reverse pass increases computation and execution time. If the differentiated function is the same and recomputation is consistent, the target derivative remains the same.

</details>

### 7. Critique a model claim

Explain the problem with the claim: “Automatic differentiation returned an accurate gradient, so the explanation of the trained model is also accurate.”

<details>
<summary>Show solution</summary>

Automatic differentiation accuracy concerns the local derivative of the function calculated by a given program. Whether the gradient is a causal explanation of the model, stable outside the data, or based on an appropriate attribution definition are separate questions. Also check conventions at nondifferentiable points and whether the implemented graph represents the intended function.

</details>

## Lesson summary

- Automatic differentiation applies the chain rule to a program built from elementary operations.
- Forward mode propagates primal values and tangents in computation order to calculate JVPs.
- Reverse mode propagates cotangents in reverse order to calculate VJPs.
- When a variable is used along multiple paths, all backward contributions are added.
- Backpropagation is reverse-mode automatic differentiation applied to a scalar neural network loss.
- Backpropagation and optimizer updates are separate steps.
- Reverse-mode intermediate-value storage and recomputation involve a memory–compute tradeoff.

## Pass criteria

You pass if you can answer the following without consulting the lesson.

- Can you distinguish automatic differentiation from symbolic and numerical differentiation?
- Can you propagate primal values and tangents through a small computation graph?
- Can you start from $\bar L=1$ and calculate cotangents in reverse order?
- Can you sum gradient contributions at a branch?
- Can you distinguish the roles of backpropagation and optimizer updates?
- Can you compare seed counts for forward and reverse modes?
- Can you explain checkpointing's memory–compute tradeoff?

## Next lesson

- [M03-15 Introduction to reparameterization and model symmetries](M03-15-reparameterization-model-symmetries.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Automatic differentiation is distinguished from symbolic and numerical differentiation.
- [x] Computation graphs and local derivatives are explained.
- [x] Forward and reverse modes are compared using the same example.
- [x] Gradient accumulation at a branch is calculated.
- [x] Backpropagation is distinguished from optimizer updates.
- [x] The tradeoff between memory and recomputation is stated.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
