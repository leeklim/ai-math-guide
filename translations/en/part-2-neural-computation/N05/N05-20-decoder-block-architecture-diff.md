---
id: "N05-20"
title: "Decoder blocks and architecture diffs"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-19"
estimated_time: "150–180 minutes"
---

# N05-20. Decoder blocks and architecture diffs

## Why this lesson matters

The embeddings, attention, normalization, MLPs, and residual updates computed separately in earlier lessons can now be connected into a decoder-only model. At the same time, a model's configuration must be used to distinguish differences in block ordering and components among models called `Transformer`.

## Learning objectives

- Trace the tiny decoder's computation from token IDs to logits.
- Calculate the shapes of the main tensors within a block.
- Tabulate differences between the reference architecture and a public model configuration.
- Distinguish mathematical components from implementation optimizations.
- Avoid matching hook names directly across models with different architectures.

## Prerequisite check

- Prerequisite lesson: [N05-19 Dense MLPs, SwiGLU, and expert routing](N05-19-dense-mlp-swiglu-expert-routing.md)
- Check question: Can you write the order of the attention and MLP updates in a pre-norm residual block as equations?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\mathbf X^{(0)}$ | `X at layer zero` | First residual stream after token embedding | $\mathbb R^{B\times T\times d_{model}}$ |
| $\mathbf X^{(l+1)}$ | `X at layer l plus one` | Residual stream after block $l$ | Same residual shape |
| $\mathbf Z$ | `Z` | Output of final normalization | $\mathbb R^{B\times T\times d_{model}}$ |
| $\mathbf L$ | `L` | Vocabulary logits | $\mathbb R^{B\times T\times V}$ |
| architecture diff | `architecture diff` | Differences between two models' choices of components, ordering, and shapes | Comparison record |
| fused kernel | `fused kernel` | Implementation combining several operations into one execution path | Implementation detail |

## Core concept 1. The reference decoder path

The instructional reference model uses the following computation:

\[
\mathbf X^{(0)}=E[\text{input IDs}]
\]

At each block $l$, it computes

\[
\mathbf U^{(l)}=\mathbf X^{(l)}+
A_l(\operatorname{RMSNorm}(\mathbf X^{(l)}))
\]

\[
\mathbf X^{(l+1)}=\mathbf U^{(l)}+
M_l(\operatorname{RMSNorm}(\mathbf U^{(l)}))
\]

and finally produces vocabulary logits through

\[
\mathbf Z=\operatorname{RMSNorm}(\mathbf X^{(L)}),
\qquad
\mathbf L=\mathbf Z\mathbf W_U^\top
\]

Attention uses RoPE and causal MHA, and the MLP uses dense SwiGLU.

The tensor $\mathbf U^{(l)}$ is the stream after the first residual addition, not the attention output itself. The MLP receives a normalized version of this updated stream, and the skip term in the second addition also uses $\mathbf U^{(l)}$. Using the same symbol for each Norm does not imply that their learned scales are shared. The final Norm is a separate site that converts the final stream into the unembedding input without adding a new update.

Within the block, the Norm outputs, sublayer updates, and streams after addition are marked as distinct sites.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A serial decoder block separates raw skip states, normalized branch inputs, attention and MLP updates, and residual hook sites](../../figures/assets/N05/N05-20-block-hook-sites.svg)

<figcaption>The blue skip paths retain the unnormalized stream, while the upper branches pass through separate RMSNorms. U, obtained by adding the attention update, and the MLP update itself are different tensors. Equal shapes do not make their hook sites equivalent.</figcaption>
</figure>

Distinguish the layer count $L$ from bold $\mathbf L$. The tensor $\mathbf X^{(L)}$ is the stream after the last block, while $\mathbf L$ contains logits scoring each candidate token. Although embedding selects one vocabulary row at the input, the output scores all vocabulary candidates.

Read the full path of the one-layer lab model by tracking where the last axis changes.

<figure class="lesson-figure" markdown="1">

![Token IDs feed embedding, two residual updates, final norm, and unembedding with their exact tiny-decoder shapes](../../figures/assets/N05/N05-20-decoder-overview.svg)

<figcaption>The lab uses B=1, T=3, model dimension=4, and vocabulary=16. The block preserves the residual shape (1,3,4); unembedding changes only the last axis into scores for 16 candidates.</figcaption>
</figure>

## Core concept 2. The shape ledger

For the lab with $B=1$, $T=3$, $d_{model}=4$, 1 head, and a vocabulary of 16, the main shapes are:

| Site | Shape |
|---|---|
| input IDs | $(1,3)$ |
| Embedding and residual stream | $(1,3,4)$ |
| Q, K, V | $(1,1,3,4)$ |
| Attention scores | $(1,1,3,3)$ |
| Attention and MLP updates | $(1,3,4)$ |
| logits | $(1,3,16)$ |

The two tensors at each residual addition have the same shape. Only the last axis changes to the vocabulary size at unembedding.

Three arrays can have the same token rows while their columns refer to different objects.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three token rows have four residual-feature columns, three attention-key columns, or sixteen vocabulary-candidate columns](../../figures/assets/N05/N05-20-score-vocabulary-axes.svg)

<figcaption>These are entry slots with batch and head dimensions omitted. The three attention-score columns refer to input key positions; the sixteen logit columns refer to vocabulary candidates. Empty slots indicate axes and sizes, not actual values or whether a mask permits an entry.</figcaption>
</figure>

## Core concept 3. Reading an architecture diff

When comparing models, check the following items separately:

1. Decoder-only versus encoder-decoder
2. Normalization type and placement
3. Number of attention heads and key-value heads
4. Positional information and its scope of application
5. MLP activation and dense versus expert structure
6. Serial versus parallel residual ordering
7. Embedding-unembedding weight tying
8. Cache layout and fused kernels

Do not place choices that change the mathematical function in the same column as implementations that compute the same function faster.

In the reference serial residual structure, the MLP reads the intermediate stream changed by attention. In a parallel residual structure, both branches can form updates from the same block input and then add their results. The latter MLP does not receive the intermediate stream with the attention update added. The difference concerns dependencies between functions, not just whether a computer executes the two branches simultaneously.

Even a numerical toy example that isolates the dependency produces different serial and parallel results.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Serial and parallel residual toy blocks yield 4.5 and 3.5 because the MLP reads an attention-updated stream or the original input](../../figures/assets/N05/N05-20-serial-parallel-dependency.svg)

<figcaption>This separate example omits Norm and uses A(z)=z/2, M(z)=2z, and x=1. The serial MLP reads U=1.5, while the parallel MLP reads x=1. Blue bypass lines are the skip terms entering each addition.</figcaption>
</figure>

By contrast, a fused kernel that computes the same attention result for the same Q, K, V, and mask can combine execution steps and memory accesses. Even when intermediate tensors are not stored separately, the mathematical roles of QK scores and the weighted sum of values remain. Distinguish actual tensors observable through a hook from intermediate values defined in equations.

The figure below separates the role of a mathematical intermediate from whether its tensor is exposed in execution.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Explicit attention stores full score and weight tensors while a fused path can compute the same output without exposing those full buffers](../../figures/assets/N05/N05-20-fused-intermediates.svg)

<figcaption>These implementation paths compute the same attention function for the same inputs and mask. A fused path can perform the roles of scoring, softmax, and value mixing without separately storing the full (T,T) intermediate tensors or exposing them to hooks.</figcaption>
</figure>

## Comparing the Pythia configuration

The public Pythia-160M training configuration specifies 12 layers, hidden size 768, 12 attention heads, a RoPE fraction of 0.25, `gpt-j-residual: true`, `no-weight-tying: true`, and FlashAttention. The instructional reference uses 1 layer, dimension 4, full-dimension RoPE, serial residuals, and explicit untied unembedding.

The instructional model is therefore not a scaled-down replica of Pythia. It provides a reference for verifying common computations with small numbers before reading the differences in actual models.

## Hands-on lab

### Environment and source files

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Checked on: 2026-10-01
- Component classification: the reference block is an `Instructional reference`; architecture diffs are `Architecture-specific`
- Shared implementation: `labs/N05/tiny_decoder.py`
- Example ID: `n05_20_decoder_block`
- Code source: `labs/N05/n05_20_decoder_block.py`
- Tests: `tests/N05/test_n05_20.py`
- Run command: `.venv\Scripts\python.exe -m labs.N05.n05_20_decoder_block`

### Resource budget

The lab uses batch size 1, sequence length 3, dimension 4, 1 layer, 1 head, vocabulary size 16, and 300 parameters.

### Actual code and execution results

<!-- N05_EXAMPLE: n05_20_decoder_block -->

### Checks

The tests check shapes from embedding to logits, both residual additions, and the parameter count.

## Connection to model interpretability

Record an activation's name together with its computational site. The label `layer 3 hidden state` alone does not identify whether the tensor is the block input, attention update, intermediate residual stream, MLP update, or block output.

Equal layer indices in two architectures can correspond to different computational depths and residual layouts. Before comparing representations, establish component correspondence rather than forcing unmatched sites into a correspondence.

## Common misconceptions

### Misconception 1. Decoder blocks have the same ordering in every model

Normalization, parallel residuals, attention variants, and MLP structures can differ.

### Misconception 2. FlashAttention introduces a new attention equation

The reference FlashAttention is an implementation optimization that computes exact attention in a memory-efficient way. Check execution conditions such as masks and numerical precision separately.

### Misconception 3. Equal parameter counts imply equal activation shapes

Internal shapes can differ with the number of heads, vocabulary size, number of layers, and parameter sharing.

## Exercises

### 1. Logit shape

Determine the logit shape for $B=2$, $T=5$, and a vocabulary of 100.

<details><summary>Show solution</summary>The shape is $(2,5,100)$.</details>

### 2. Residual requirements

Determine what is needed if concatenating the heads inside attention gives dimension 12 but the residual dimension is 8.

<details><summary>Show solution</summary>Before residual addition, an output projection must change the last dimension to 8.</details>

### 3. Tracing the order

Identify where the output of the first normalization goes in the reference block.

<details><summary>Show solution</summary>It enters the causal attention sublayer. The original residual remains in the skip path to be added to the attention update.</details>

### 4. Classifying a diff

Determine which changes the tensor-sharing structure: replacing MHA with GQA, or computing the same attention with a fused kernel.

<details><summary>Show solution</summary>The change from MHA to GQA does. A fused kernel computes the same mathematical function through a different execution strategy.</details>

### 5. Interpreting a configuration

Explain what `no-weight-tying: true` means for embedding and unembedding.

<details><summary>Show solution</summary>The two sites do not share the same parameter matrix.</details>

### 6. Comparing hooks

Explain why a serial residual model's `residual_mid` can be difficult to match one-to-one in a parallel residual model.

<details><summary>Show solution</summary>A parallel structure may have no equivalent intermediate stream formed by adding only the attention update and then used as the MLP input. First inspect the computation graph to determine whether a correspondence is possible.</details>

## Sources and update boundaries

The reference block's common attention and feed-forward structure follows [Attention Is All You Need](https://arxiv.org/abs/1706.03762). The public description of the GPT-NeoX family was checked against [GPT-NeoX-20B](https://arxiv.org/abs/2204.06745), and the Pythia values against the [official Pythia-160M configuration](https://github.com/EleutherAI/pythia/blob/main/models/160M/pythia-160m.yml). Public configurations and implementations can change, so use a pinned revision in actual experiments.

## Lesson summary

- The tiny decoder connects embedding, pre-norm attention, a pre-norm MLP, final normalization, and unembedding.
- The residual axis remains $d_{model}$ throughout the block.
- Read architecture diffs by separating components, ordering, sharing, and implementation.
- The instructional reference is a computational control, not a scaled-down replica of an actual model.
- Comparing hooks requires correspondence between precise computational sites.

## Pass criteria

- Can you draw the sequence from token IDs to logits?
- Can you calculate the main tensor shapes?
- Can you extract architecture differences from a configuration?
- Can you distinguish a component change from a kernel optimization?
- Can you identify hook sites without a correspondence?

## Next lesson

- [N05-21 The language model objective](N05-21-language-model-objective.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] The tiny decoder's full path is connected to architecture diffs.
- [x] The official Pythia configuration has been checked.
- [x] Every exercise has a solution.
- [x] Model interpretability claims are distinguished by strength of evidence.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and mathematical rendering have been checked.
- [x] Executable code has not been manually duplicated in Markdown.
- [x] Code sources, test paths, resource budgets, and the check date are recorded.
- [x] Shape, residual, and parameter tests are provided.
