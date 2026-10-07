---
id: "N05-17"
title: "Residual stream"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-16"
estimated_time: "120–150 minutes"
---

# N05-17. Residual stream

## Why this lesson matters

Rather than creating a new hidden state from scratch, the attention and MLP sublayers of a Transformer block add updates to the same residual stream. To specify which activation you observed or changed, distinguish the block input, sublayer output, and stream after addition.

## Learning objectives

- Calculate residual updates while tracking tensor shapes.
- Trace the order in which attention and MLP outputs are added to the stream.
- Identify the skip path's contribution to the gradient in an equation.
- Distinguish locations in the residual stream from activations inside a sublayer.
- Distinguish observations of a stream decomposition from causal claims.

## Prerequisite check

- Prerequisite lesson: [N05-16 MHA, MQA, and GQA](N05-16-mha-mqa-gqa.md)
- Check question: Can you explain why the last dimension of an attention output must match that of the residual input?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\mathbf R^{(l)}$ | `R at layer l` | Residual stream at the entrance to layer $l$ | $\mathbb R^{B\times T\times d_{model}}$ |
| $\Delta\mathbf R_A$ | `attention update` | Update that the attention sublayer adds to the stream | Same shape as the residual |
| $\Delta\mathbf R_M$ | `MLP update` | Update that the MLP sublayer adds to the stream | Same shape as the residual |
| skip path | `skip path` | A path that passes through identically without going through the sublayer | identity map |
| residual addition | `residual addition` | Elementwise addition of the stream and an update | shape-preserving |

## Core concept 1. Adding in the same space

Temporarily omitting the normalization locations, one block can be written as

\[
\mathbf R_{mid}=\mathbf R_{in}+A(\mathbf R_{in}),
\qquad
\mathbf R_{out}=\mathbf R_{mid}+M(\mathbf R_{mid})
\]

Here, $A$ is the attention sublayer and $M$ is the MLP sublayer. For the two updates to be added, the final output dimension of both $A$ and $M$ must be $d_{model}$.

`residual stream` refers to the representation path along which updates accumulate between blocks, rather than to a separate module name.

Addition combines two values at the same sample, token, and feature position. Unlike concatenation, it does not increase axis lengths; the batch and token axes of the final update must also match the stream. Attention may concatenate multiple heads internally, and the MLP may use a wider hidden dimension, but a projection returns them to $d_{model}$ coordinates before they write to the stream. Distinguish the width of the internal computation from the width of the residual stream.

The addition below connects only elements with matching rows and columns.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two token-feature matrices add matching entries to produce a matrix of the same shape](../../figures/assets/N05/N05-17-same-coordinate-addition.svg)

<figcaption>This is the attention addition in the example. At feature 1 of token 0, adding −1 and 0.5 gives −0.5 without taking values from other rows or columns. Both the token count and feature count remain unchanged.</figcaption>
</figure>

## Core concept 2. Following the updates

Observing $\mathbf R_{mid}$ does not mean observing only the attention output. It means observing the sum of the previous stream and the attention update. Similarly, $\mathbf R_{out}$ is the accumulated result of the input, attention update, and MLP update. The MLP update itself depends on $\mathbf R_{mid}$, however, so do not treat these three terms as independent, fixed vectors.

### Visual intuition: Reading a shared space and writing back to it

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Attention and MLP branches reading a shared residual stream and adding updates back into it](../../figures/assets/N05/N05-17-residual-stream.svg)

<figcaption>The thick horizontal line is the residual stream, which retains the same d_model space. Attention and the MLP read the current stream, calculate updates, and add them back into that space.</figcaption>
</figure>

The horizontal path bypassing attention and the MLP in the figure is the skip path. The upper branch does not erase the previous stream and replace it with a new state. It adds the computed $\Delta\mathbf R$ to the existing state. Thus, whether a hook is named `attention output` or `residual post` changes the meaning of the tensor being observed.

After the computation is complete, the output of one block can be written as

\[
\mathbf R_{out}
=
\mathbf R_{in}
+
\Delta\mathbf R_A
+
\Delta\mathbf R_M
\]

However, $\Delta\mathbf R_M=M(\mathbf R_{in}+\Delta\mathbf R_A)$, so changing the attention update generally also changes the MLP update. This equation shows the additive relationship in the final tensor, not independence among the components.

Using the example's linear block, compare how removing the attention update also requires recomputing the subsequent MLP update.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Keeping or removing an attention update changes the next MLP input and recomputed update in a toy residual block](../../figures/assets/N05/N05-17-dependent-mlp-update.svg)

<figcaption>The lab applies M(a,b)=(b/4,a/4) to the first token. Removing the attention update returns the MLP input to (1,−1), so the MLP update changes to (−0.25,0.25). The final stream in each row is the sum of R_mid and M(R_mid).</figcaption>
</figure>

## Core concept 3. The skip term in the gradient

The Jacobian of a simple residual map $\mathbf y=\mathbf x+F(\mathbf x)$ is

\[
\frac{\partial\mathbf y}{\partial\mathbf x}
=\mathbf I+J_F(\mathbf x)
\]

Backpropagation includes an identity-path term as well as the sublayer-Jacobian path. This does not guarantee that gradients are always stable, but the computation differs from a chain containing only $J_F$ with the skip path removed.

When multiple residual blocks are composed, the gradient involves a chain of each block's $\mathbf I+\mathbf J_{F_l}$. The identity term provides a path that transmits a change unchanged, but the sum with the remaining Jacobian can still cancel, and the product across multiple layers can still grow. Do not treat the existence of residual connections and stable optimization as the same claim.

Writing the gradient returning from the loss as a column vector gives $\nabla_{\mathbf x}\mathcal L=\nabla_{\mathbf y}\mathcal L+J_F(\mathbf x)^\top\nabla_{\mathbf y}\mathcal L$. The first term comes from the skip path and the second from the branch, following the rule of adding derivative contributions from branching paths. For example, when $F(\mathbf x)=-\mathbf x$, the two terms cancel, and the output is also 0. Adding the existing stream in the equation does not mean that its information is preserved unchanged in the output.

Following the sum of the two gradient paths numerically makes the identity term's location explicit.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An incoming two-coordinate gradient passes through identity and branch transposes and sums at the input](../../figures/assets/N05/N05-17-gradient-two-paths.svg)

<figcaption>This separate linear example uses F(x₀,x₁)=(2x₀,−0.5x₁). The incoming gradient (1,1) returns unchanged along the skip path and as (2,−0.5) along the branch. They sum to (3,0.5) at the input.</figcaption>
</figure>

In the cancellation counterexample, both paths exist, but the final function does not respond to changes in its input.

<figure class="lesson-figure" markdown="1">

![The identity line and its negative cancel to a flat zero residual output](../../figures/assets/N05/N05-17-skip-cancellation.svg)

<figcaption>When F(x)=−x, the blue skip value and purple branch value cancel for every input. The green output is the horizontal line y=0, and the derivative of the entire map is also 0.</figcaption>
</figure>

## Example

The lab adds a linear attention update and then an MLP update to a two-dimensional stream containing two tokens.

\[
\mathbf R_{in}=
\begin{bmatrix}1&-1\\2&0\end{bmatrix},
\quad
\Delta\mathbf R_A=
\begin{bmatrix}0.5&0.5\\1&0\end{bmatrix}
\]

This gives $\mathbf R_{mid}=\begin{bmatrix}1.5&-0.5\\3&0\end{bmatrix}$. After adding the MLP update, the final stream is

\[
\mathbf R_{out}=
\begin{bmatrix}1.375&-0.125\\3&0.75\end{bmatrix}
\]

Placing the first token's two additions in the same coordinate system shows each update as a displacement from the current position, not an operation that replaces it with a new vector.

<figure class="lesson-figure" markdown="1">

![One token moves from its input residual to the attention-updated point and then the MLP-updated point in one feature coordinate grid](../../figures/assets/N05/N05-17-token-update-trajectory.svg)

<figcaption>The first token moves from (1,−1) to (1.5,−0.5) by adding the attention update (0.5,0.5), then to (1.375,−0.125) by adding the MLP update (−0.125,0.375). The axes are two feature coordinates, not layers.</figcaption>
</figure>

## Executable lab

### Environment and source

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Verification date: 2026-10-01
- Component category: `Stable core`
- Example ID: `n05_17_residual_stream`
- Source code: `labs/N05/n05_17_residual_stream.py`
- Tests: `tests/N05/test_n05_17.py`
- Run command: `.venv\Scripts\python.exe -m labs.N05.n05_17_residual_stream`

### Resource budget

The lab performs only the computation corresponding to batch size 1, sequence length 2, model dimension 2, and one block.

### Actual code and execution results

<!-- N05_EXAMPLE: n05_17_residual_stream -->

### Checks

The tests compare the values of both residual additions and the loss gradient with respect to the input stream against hand calculations.

## Connection to model interpretability

Projecting the residual stream onto a particular direction lets you observe how its component along that direction changes across layers. Differences between layers are related to the updates in that interval, but a single projection value does not automatically represent an independent unit of meaning.

Adding a vector to the stream or removing a component output is an intervention that changes an actual activation. In contrast, reading the stream only to make a plot is an observation. Do not report these two forms of evidence at the same strength.

Below, reading a value and changing an activation are shown side by side at the same hook location.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Reading one stream coordinate leaves activation unchanged while adding a vector changes the input to downstream computation](../../figures/assets/N05/N05-17-observation-intervention.svg)

<figcaption>An observation reads the first coordinate, 1, of r=(1,2) without changing the original run. An intervention adds (0.5,0), changing r to (1.5,2), then checks changes in downstream computation and the evaluation value. This figure assumes no numerical behavioral effect.</figcaption>
</figure>

## Common misconceptions

### Misconception 1. The residual stream is the attention output

The attention output is an update added to the stream. The stream after addition includes the previous-stream term, but it can cancel with the update, so preservation of the previous information is not automatically guaranteed.

### Misconception 2. It is enough to view the layer output only as a sum of fixed component vectors

A later component's update depends on the stream updated earlier. You must also follow the computation order.

### Misconception 3. An identity path makes vanishing gradients impossible

The Jacobian gains an identity term, but normalization, sublayer Jacobians, and loss curvature still affect the full network.

## Exercises

### 1. Shape condition

Determine the final shape of the attention output projection when the residual has shape `(2,5,8)`.

<details><summary>Show solution</summary>It must be added elementwise, so its shape is `(2,5,8)`.</details>

### 2. One update

Calculate the stream after addition when $r=(1,2)$ and the attention update is $(-0.5,1)$.

<details><summary>Show solution</summary>The result is $(0.5,3)$.</details>

### 3. Two updates

Add the MLP update $(2,-1)$ to the preceding result.

<details><summary>Show solution</summary>The result is $(2.5,2)$.</details>

### 4. Jacobian

Calculate $dy/dx$ when $F(x)=2x$ and $y=x+F(x)$.

<details><summary>Show solution</summary>It is $1+2=3$. The 1 is the derivative of the skip path.</details>

### 5. Hook location

To store only the update that attention writes to the stream, is it enough to store just one of the streams before or after addition?

<details><summary>Show solution</summary>Taking the difference between the two streams gives the update, but check that there is no normalization or other operation between them. The most direct location is after the attention output projection and before residual addition.</details>

### 6. Critique a claim

Evaluate the claim that an increase in the residual projection along a direction means that the feature causes the behavior.

<details><summary>Show solution</summary>A change in the directional component is an observation. Establishing a causal relationship to behavior requires manipulating that direction and examining output changes with appropriate controls.</details>

## Sources and update boundaries

Transformer blocks with residual connections are based on [Attention Is All You Need](https://arxiv.org/abs/1706.03762). The notation analyzing the residual stream as a shared space read and written by component updates follows [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html). Module names and hook locations differ across implementations.

## Lesson summary

- Attention and the MLP add updates to the same residual stream.
- A sublayer output and the stream after addition are different activations.
- A residual Jacobian includes an identity-path term.
- A later update depends on the stream updated earlier.
- Stream observations and stream interventions provide different evidence.

## Pass criteria

- Can you calculate residual updates while tracking their shapes?
- Can you mark stream locations inside a block in order?
- Can you explain the identity term in a residual Jacobian?
- Can you distinguish a component output from the stream?
- Can you distinguish observational and intervention claims?

## Next lesson

- [N05-18 LayerNorm, RMSNorm, and residual order](N05-18-layernorm-rmsnorm-residual-order.md)

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] Residual updates and gradient paths are connected.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretability claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Knowledge beyond the prerequisites is not required without explanation.
- [x] Internal links and equation rendering are checked.
- [x] Executable code is not manually duplicated in Markdown.
- [x] Source-code and test paths, resource budgets, and the verification date are recorded.
- [x] Shape, numerical-value, and gradient tests are provided.
