---
id: "N05-19"
title: "Dense MLPs, SwiGLU, and expert routing"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-18"
estimated_time: "120–150 minutes"
---

# N05-19. Dense MLPs, SwiGLU, and expert routing

## Why this lesson matters

A Transformer's tokenwise feed-forward computation may use a dense MLP whose parameters are shared by all tokens, or a sparse MoE that runs only the experts selected by a router. Referring to both a SwiGLU gate and an MoE router as a `gate` can obscure the difference between their computations.

## Learning objectives

- Calculate the forward expressions and shapes of a dense MLP and SwiGLU.
- Distinguish the roles of SwiGLU's two input projections.
- Calculate the probabilities and selected expert in top-1 expert routing.
- Distinguish the dense parameter count from the expert parameters activated per token.
- Distinguish observations of router scores from an expert's causal contribution.

## Prerequisite check

- Prerequisite lesson: [N05-18 LayerNorm, RMSNorm, and residual ordering](N05-18-layernorm-rmsnorm-residual-order.md)
- Check question: Can you calculate the shapes of a tokenwise linear projection and an elementwise activation?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $d_{ff}$ | `d sub f f` | Feed-forward hidden dimension | Positive integer |
| $\operatorname{SiLU}$ | `sigh-loo` | Activation defined by $z\,\sigma(z)$ | Elementwise |
| $\odot$ | `elementwise product` | Product of corresponding entries in tensors of the same shape | Shape-preserving |
| $p_e(\mathbf x)$ | `the routing probability for expert e` | Probability assigned by the router to expert $e$ | $[0,1]$ |
| top-1 routing | `top-one routing` | Rule selecting the single highest-scoring expert for each token | Discrete selection |
| expert | `expert` | Feed-forward subnetwork executed selectively in an MoE | Architecture-specific |

## Core concept 1. Dense MLPs

A basic feed-forward layer applies the same parameters to each token:

\[
\operatorname{MLP}(\mathbf x)
=\mathbf W_{down}\,\phi(\mathbf W_{up}\mathbf x+\mathbf b_{up})
+\mathbf b_{down}
\]

Under a row-vector convention, the positions of the weight transposes change. The input and output have dimension $d_{model}$, and the intermediate activation has dimension $d_{ff}$. Here, `dense` means that every token uses the full set of parameters in the same MLP.

The shapes of $\mathbf W_{up}$ and $\mathbf W_{down}$ are $(d_{ff},d_{model})$ and $(d_{model},d_{ff})$, respectively. The first projection mixes model coordinates to form hidden features, the activation applies at each hidden position, and the second projection mixes the hidden features back into stream coordinates. This expression does not directly sum across other token positions. Even with the same weights, different input vectors can produce different hidden values and updates for each token.

The example below computes two tokens with the same weights; no arrows connect the token rows.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two tokens independently use the same up and down weights through a three-feature hidden layer](../../figures/assets/N05/N05-19-dense-token-sharing.svg)

<figcaption>This separate toy MLP uses ReLU and has no biases. The two tokens share the up and down weights but have different hidden values and outputs. The model dimension goes from 2 to a hidden dimension of 3 and then back to 2.</figcaption>
</figure>

## Core concept 2. SwiGLU

SwiGLU forms its intermediate representation by multiplying two projections elementwise:

\[
\mathbf h=\operatorname{SiLU}(\mathbf W_g\mathbf x)
\odot(\mathbf W_u\mathbf x),
\qquad
\mathbf y=\mathbf W_d\mathbf h
\]

The $\mathbf W_g$ path produces a gate through SiLU, while the $\mathbf W_u$ path produces the content that the gate modulates. Both projection outputs must have dimension $d_{ff}$.

Multiplying the two numbers at each hidden position forms $\mathbf h$, and $\mathbf W_d$ maps it back to $d_{model}$. Excluding biases, the gate and content projections each have $d_{model}d_{ff}$ weights, and the down projection has the same number, giving $3d_{model}d_{ff}$ in total. This already differs from the parameter count of an ordinary MLP with two projections. SwiGLU is not obtained merely by replacing the scalar activation in an MLP of the same width.

A gate may make a value at one position 0, but this does not select and skip experts within the dense projection itself. Multiplication that modulates featurewise content differs from the subnetwork selection in the next section.

For the first token in the lab, the two projections are multiplied at corresponding hidden positions.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A SiLU gate and content vector multiply corresponding coordinates into a SwiGLU hidden vector without expert selection](../../figures/assets/N05/N05-19-swiglu-gate-product.svg)

<figcaption>This is an intermediate calculation from the lab for x=(2,−1). The SiLU gate, approximately (1.762,−0.269), is multiplied coordinatewise by the content (1,3). A gate can be negative; there is no step that selects an expert index.</figcaption>
</figure>

## Core concept 3. Expert routing

With $E$ experts, the router computes

\[
\mathbf p(\mathbf x)=\operatorname{softmax}(\mathbf W_r\mathbf x),
\qquad
e^*=\operatorname*{argmax}_e p_e(\mathbf x)
\]

In a simple top-1 example, only the selected expert's output is used:

\[
\mathbf y=p_{e^*}(\mathbf x)F_{e^*}(\mathbf x)
\]

An actual MoE may have additional rules for capacity, load balancing, dropped tokens, and communication.

A SwiGLU gate performs featurewise multiplication within one MLP, whereas an MoE router determines the execution path among several parameterized subnetworks.

The router matrix has shape $(E,d_{model})$ and produces one logit per expert. Softmax probabilities sum to 1 over all experts, but the toy expression above uses only the probability of the selected expert. That coefficient is generally less than 1; selection does not automatically turn it into 1. The coefficient applied to the selected expert's output, including any renormalization, is a separate design choice.

Within an input region where the expert does not change, the selected index remains fixed while the probability and expert output vary with the input. At a boundary where the highest-scoring candidate changes, the hard selection changes. Obtaining the same expert index and obtaining the same forward value are different facts. To reproduce the computation, the rule for selecting an index in a tie must also be specified.

When the router weights are the coordinate axes, the selection boundary is the line where the two logits are equal.

<figure class="lesson-figure" markdown="1">

![Two identity-router experts occupy opposite sides of the equal-logit diagonal with two token examples and a tie point](../../figures/assets/N05/N05-19-routing-plane.svg)

<figcaption>In this example, W_r=I₂. The region x₀>x₁ selects expert 0, and x₁>x₀ selects expert 1. The point (1,1) is a tie and requires a tie-breaking rule.</figcaption>
</figure>

## Example

Set the router weights for two experts to the coordinate axes. For token $(2,-1)$, the logits are $(2,-1)$, giving softmax probabilities of approximately $(0.9526,0.0474)$ and selecting expert 0. Token $(-1,2)$ selects expert 1 instead. Tokens in the same batch can take different paths.

Follow the lab's computation through to the output, retaining the probability coefficient after selection.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two example tokens route to opposite identity and negative-identity experts with the selected softmax probability retained](../../figures/assets/N05/N05-19-selected-expert-weight.svg)

<figcaption>The lab uses F₀(x)=x and F₁(x)=−x. Multiplying the selected expert's output by approximately 0.9526 makes the final routed output different from the expert output itself. The coefficient is not changed to 1 merely because that expert was selected.</figcaption>
</figure>

## Hands-on lab

### Environment and source files

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Checked on: 2026-10-01
- Component classification: dense SwiGLU is a `Common modern variant`; expert routing is `Architecture-specific`
- Example ID: `n05_19_mlp_routing`
- Code source: `labs/N05/n05_19_mlp_routing.py`
- Tests: `tests/N05/test_n05_19.py`
- Run command: `.venv\Scripts\python.exe -m labs.N05.n05_19_mlp_routing`

### Resource budget

The lab uses 3 tokens, model dimension 2, hidden dimension 2, and 2 experts. It performs no training or dispatch communication.

### Actual code and execution results

<!-- N05_EXAMPLE: n05_19_mlp_routing -->

### Checks

The tests check SwiGLU shapes and values, router probability row sums, top-1 expert indices, and routed outputs.

## Distinguishing parameters from computation

An MoE stores all of its expert parameters but may activate only some experts for each token. The total parameter count therefore differs from the number of parameters executed per token. When comparing a dense MLP with an MoE, record parameters, FLOPs, memory traffic, communication, and quality separately.

The figure below shows the execution path of one token among four stored experts.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Four stored experts remain in memory while a single token executes only its selected expert](../../figures/assets/N05/N05-19-expert-storage-active.svg)

<figcaption>Each of the four experts in this concept diagram has P weights. All 4P expert weights are stored, but this token executes only the P weights of expert 2. The router and other model parameters are excluded from this comparison.</figcaption>
</figure>

The index selected by a hard `argmax` is locally constant in regions without ties and may be discontinuous at selection boundaries. The index alone does not provide a continuous gradient for adjusting the router. Actual training uses mechanisms such as the selected gate probability and auxiliary losses to train the router. This lesson's toy routing does not reproduce the full training algorithm.

As the difference between two logits varies continuously, the probability and hard index respond differently.

<figure class="lesson-figure" markdown="1">

![Routing probability changes continuously with the logit difference while the selected expert index is piecewise constant and switches at zero](../../figures/assets/N05/N05-19-routing-confidence-index.svg)

<figcaption>The upper panel shows the probability of expert 0; the lower panel shows the selected index. The probability changes even within a region that keeps the same expert. This toy rule selects the first index, 0, in a tie; the figure does not depict the full process of training a router.</figcaption>
</figure>

## Connection to model interpretability

When analyzing SwiGLU hidden activations, distinguish the hook sites at the gate projection, the up projection, and the activation after the elementwise product. In an expert model, also distinguish router logits, routing probabilities, the selected index, and activations inside an expert.

Observing that an expert is often selected for certain tokens does not establish that the expert is necessary for that behavior. A causal claim requires changing the routing or intervening on the expert output while controlling load and including controls.

## Common misconceptions

### Misconception 1. SwiGLU selects experts

SwiGLU multiplies two dense projections featurewise within one MLP. It does not perform discrete expert selection.

### Misconception 2. MoE is fast because it has few parameters

The total parameter count can be very large. Computing only some experts per token provides conditional computation.

### Misconception 3. The expert with a high router probability exclusively owns a meaning

Selection frequency or probability alone does not reveal the expert's internal computation or its downstream causal effect.

## Exercises

### 1. SwiGLU shapes

Given $x:(7,8)$ and $W_g$ and $W_u$ each of shape `(16,8)`, determine the shapes of the two projections just before the elementwise product.

<details><summary>Show solution</summary>Both have shape `(7,16)` under the row-vector convention. Their shapes must match for an elementwise product.</details>

### 2. Output shape

Determine the output shape when $W_d:(8,16)$ is applied to the preceding result.

<details><summary>Show solution</summary>The shape is `(7,8)`. The projection returns to the model dimension so that the output can be added to the residual stream.</details>

### 3. Router probabilities

Calculate the two probabilities when the expert logits are $(0,0)$.

<details><summary>Show solution</summary>Softmax gives $(0.5,0.5)$.</details>

### 4. Ties

If two logits share the maximum in top-1 routing, determine whether the mathematical expression alone selects a unique expert.

<details><summary>Show solution</summary>It does not. The implementation needs a tie-breaking rule. PyTorch `argmax` returns the first index among equal maximum values.</details>

### 5. Interpreting the parameter count

If there are 8 experts and only 1 runs per token, determine whether only 1/8 of the total expert parameters need to be stored.

<details><summary>Show solution</summary>No. All 8 experts' parameters are generally stored, while only one expert is selected and computed in that token's forward pass.</details>

### 6. Critiquing a claim

Evaluate the claim that expert 3 causes mathematical ability because mathematical tokens are often routed to expert 3.

<details><summary>Show solution</summary>This is a correlational observation about selection frequency. Without checks of the input distribution and router confidence, interventions on expert outputs, and behavioral comparisons, it does not support a causal conclusion.</details>

## Sources and update boundaries

The Transformer feed-forward sublayer follows [Attention Is All You Need](https://arxiv.org/abs/1706.03762), the SwiGLU expression follows [GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202), and a representative top-1 routing design is given in [Switch Transformers](https://arxiv.org/abs/2101.03961). Expert capacity, auxiliary losses, and dispatch kernels vary by architecture and implementation.

## Lesson summary

- A dense MLP applies the same feed-forward parameters to all tokens.
- SwiGLU multiplies a SiLU gate projection and a content projection elementwise.
- An MoE router selects the expert to execute for each token.
- Total parameters differ from the parameters activated per token.
- Routing observations alone do not establish an expert's causal role.

## Pass criteria

- Can you calculate the shapes of a dense MLP and SwiGLU?
- Can you distinguish a SwiGLU gate from an expert router?
- Can you calculate top-1 routing by hand?
- Can you distinguish total parameters from active parameters?
- Can you choose a claim strength appropriate to a routing observation?

## Next lesson

- [N05-20 Decoder blocks and architecture diffs](N05-20-decoder-block-architecture-diff.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Dense MLPs, SwiGLU, and expert routing are distinguished.
- [x] Every exercise has a solution.
- [x] Model interpretability claims are distinguished by strength of evidence.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and mathematical rendering have been checked.
- [x] Executable code has not been manually duplicated in Markdown.
- [x] Code sources, test paths, resource budgets, and the check date are recorded.
- [x] Shape, numerical, and routing tests are provided.
