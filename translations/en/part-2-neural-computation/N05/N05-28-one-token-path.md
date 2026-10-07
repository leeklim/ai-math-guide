---
id: "N05-28"
title: "Integrated lab: The path of one token"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-27"
estimated_time: "180–240 minutes"
---

# N05-28. Integrated lab: The path of one token

## Why this lesson matters

The final goal of N05 is not to memorize component names but to reproduce the tensor path from a token ID to logits. This integrated lab connects forward activations, residual updates, an output target's gradient, and the inference cache using the same model and input.

## Learning objectives

- Trace the tensor path from a selected token's ID to vocabulary logits in order.
- Check shapes and residual equalities at each location.
- Collect the embedding gradient of a selected logit.
- Compare a full causal forward pass with cached inference.
- Classify observation, local sensitivity, intervention, and checkpoint evidence as different kinds of claims.

## Prerequisite check

- Prerequisite lesson: [N05-27 Checkpoints and model state](N05-27-checkpoint-model-state.md)
- Check question: Can you distinguish an activation hook, scalar target, gradient, KV cache, and model state in one sentence each?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $x_t$ | `the token at position t` | Selected input token ID | integer in $[0,V)$ |
| $\mathbf e_t$ | `the embedding at position t` | Vector looked up in the embedding table | $\mathbb R^{d_{model}}$ |
| $\Delta\mathbf r_{A,t}$ | `the attention update at position t` | Update that attention writes to the stream | $\mathbb R^{d_{model}}$ |
| $\Delta\mathbf r_{M,t}$ | `the MLP update at position t` | Update that the MLP writes to the stream | $\mathbb R^{d_{model}}$ |
| $\ell_{t,v}$ | `the logit for token v at position t` | Logit for the selected position and vocabulary token | scalar |
| $\nabla_{\mathbf e_t}\ell_{t,v}$ | `the gradient of the logit with respect to the embedding` | Local sensitivity of the selected logit to the embedding | $\mathbb R^{d_{model}}$ |

## Map of the full computation

Read the path at the selected token position $t$ in this order.

\[
x_t
\rightarrow \mathbf e_t
\rightarrow \operatorname{RMSNorm}
\rightarrow Q_t,K_{\le t},V_{\le t}
\rightarrow \Delta\mathbf r_{A,t}
\rightarrow \mathbf r_{mid,t}
\]

\[
\rightarrow \operatorname{RMSNorm}
\rightarrow \operatorname{SwiGLU}
\rightarrow \Delta\mathbf r_{M,t}
\rightarrow \mathbf r_{out,t}
\rightarrow \operatorname{RMSNorm}
\rightarrow \boldsymbol\ell_t
\]

The attention update depends not only on the current embedding at the same position but also on earlier tokens through the causal prefix's K and V. One token's path is not an independent line of computation; it is a selected slice of a graph connected to other positions.

Distinguish token IDs from positions to see which prefix position 2 reads in the lab.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Selected position two with token ID two forms a query while embeddings for positions zero one and two supply allowed keys and values and future position three is blocked](../../figures/assets/N05/N05-28-selected-prefix-attention.svg)

<figcaption>The input IDs are [1,4,2,7], and the selected position is 2. The current query is formed from E[2], but K and V also come from the embeddings at positions 0, 1, and 2. ID 7 at position 3 is in the future and does not enter this query's weighted sum.</figcaption>
</figure>

In the computation map, the first RMSNorm creates the attention input for each position. Projection of this input and RoPE create the Q and K used in attention. The prefix's K and V are also computed from the inputs at their respective positions. The second RMSNorm converts the stream after the attention update has been added into the MLP input. Thus, the streams entering normalization differ. Track the normalized branch input separately from the stream retained for residual addition.

Read the normalization input of each branch separately from the skip stream retained for addition.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The attention branch normalizes the original embedding and adds its update to that embedding while the later MLP branch normalizes residual mid and adds its update to residual mid before final normalization](../../figures/assets/N05/N05-28-two-residual-baselines.svg)

<figcaption>The first skip baseline is e₂, and the second is r_mid,₂. RMSNorm creates each branch's input; it does not replace the original stream on the skip path. After the attention and MLP updates are added, r_out,₂ is passed to the final RMSNorm and unembedding.</figcaption>
</figure>

## Shape ledger

The lab uses $B=1$, $T=4$, $d_{model}=4$, one head, one layer, and vocabulary size 16.

| Object | Full shape | Token $t=2$ slice |
|---|---|---|
| input IDs | $(1,4)$ | scalar ID |
| embedding, residual, update | $(1,4,4)$ | $(4,)$ |
| Q, K, V | $(1,1,4,4)$ | head-position slice $(4,)$ |
| attention score | $(1,1,4,4)$ | three allowed prefix positions |
| logits | $(1,4,16)$ | $(16,)$ |
| embedding gradient | $(1,4,4)$ | $(4,)$ |

Both sequence length and feature dimension are 4 in this lab, so the shape numbers alone do not distinguish the axes. The embedding's last axis is the feature axis, whereas the last two axes of attention scores are query and key positions, respectively. The score row for $t=2$ also has length 4, but only its three entries at positions 0, 1, and 2 are allowed; the last is masked. Vocabulary size 16 is the number of candidates on the final logit axis, not the number of tokens actually input.

Compare what the columns refer to in two arrays of the same size, 4×4.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A four by four stream array has feature columns while a four by four causal score array has key position columns and masks the last column in query row two](../../figures/assets/N05/N05-28-axis-meaning-comparison.svg)

<figcaption>On the left, rows are token positions and columns are features. On the right, rows are query positions and columns are key positions. Selecting row t=2 retains all four features on the left but allows only the first three of four key slots on the right. The subscripts on e and s describe positions, not measured values.</figcaption>
</figure>

## Checking residual equalities

At the selected position, the following must hold:

\[
\mathbf r_{mid,t}=\mathbf e_t+\Delta\mathbf r_{A,t}
\]

\[
\mathbf r_{out,t}=\mathbf r_{mid,t}+\Delta\mathbf r_{M,t}
\]

These equalities are basic checks for detecting an incorrectly placed component hook.

The baseline for the first addition is the original embedding, not the normalized attention input. The baseline for the second is $\mathbf r_{mid,t}$, not the normalized MLP input. Thus, the attention update can be compared with $\mathbf r_{mid,t}-\mathbf e_t$, and the MLP update with $\mathbf r_{out,t}-\mathbf r_{mid,t}$. Vectors with the same shape need not be at the same computation location. Collecting a norm output or a stream after addition as if it were an update may fail these relationships.

Add small illustrative vectors, then subtract the baseline of each addition to check the update.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two toy four dimensional residual additions recover their respective attention and MLP updates by subtracting the original embedding or residual mid baseline](../../figures/assets/N05/N05-28-residual-difference-checks.svg)

<figcaption>The upper calculation recovers the attention update from r_mid−e; the lower recovers the MLP update from r_out−r_mid. The numbers illustrate the baselines for the two checks, not activation outputs from the lab. Neither calculation subtracts the normalized branch input.</figcaption>
</figure>

## Output and gradient

At token index 2 in the lab, the greedy vocabulary index is 15. Fix the selected target as $\ell_{2,15}$ and use backward computation to obtain

\[
\nabla_{\mathbf e_2}\ell_{2,15}
\]

This gradient is the local sensitivity to an embedding perturbation at the reference point with the same weights and input. It is not a complete explanation of why token 15 was selected.

Here, index 15 selected in the forward pass is fixed before differentiating its logit. The integer `argmax` index itself is not differentiated. The logit at position 2 scores candidates for the next token, and the variable of the embedding gradient is the continuous vector after lookup, not the input token ID. Sensitivity to a small change in this vector is not the same as the finite change of replacing the input with another token ID. Also, increasing the selected logit alone and keeping it above alternative logits so that the selection is maintained are different questions.

Separate the step selecting an index from the step differentiating the scalar at that index.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The run selects vocabulary index fifteen from position two logits then fixes that logit as a scalar target for backward sensitivity to the continuous embedding vector rather than integer token IDs](../../figures/assets/N05/N05-28-fixed-logit-gradient.svg)

<figcaption>In this lab, the lookup vector for input ID 2 has shape (4,), and the logit vector at position 2 has shape (16,). The selected vocabulary index 15 is first fixed, then ℓ₂,₁₅ is differentiated. This does not differentiate an integer ID or the argmax index.</figcaption>
</figure>

## Cache comparison

The per-layer K and V shape in the full forward pass is `(1,1,4,4)`. Feeding the same four tokens one at a time, growing the cache, and concatenating each step's logits gives a maximum absolute difference from the full logits of approximately $1.19\times10^{-7}$. For this input, the outputs of the two computations agree within the tolerance.

The comparison uses the same given token sequence. The cached path must also receive the next token of the original input, not a newly selected token from the model, to compare the same prefix. The causal mask restricts what position $t$ sees on the full path to positions $0$ through $t$, allowing comparison with the cached path using the same position information. This checks computational reproduction for the specified input; matching cache shapes alone does not guarantee matching logits.

Concatenate the four logits obtained at cached steps along the position axis to compare with the full output.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Full causal logits for the given four token sequence are compared with four cached step logits concatenated along position under the same given input IDs](../../figures/assets/N05/N05-28-cache-stitched-logits.svg)

<figcaption>Both paths use the given IDs [1,4,2,7]. Concatenating the cached path's stepwise logits of shape (1,1,16) produces (1,4,16), matching the full output shape. The maximum difference at the bottom is the value reported by the lab in the text, a check of numerical reproduction for the same input.</figcaption>
</figure>

## Executable lab

### Environment and source

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Verification date: 2026-10-01
- Component category: N05 `Instructional reference` integrated lab
- Shared implementation: `labs/N05/tiny_decoder.py`
- Example ID: `n05_28_token_path`
- Source code: `labs/N05/n05_28_token_path.py`
- Tests: `tests/N05/test_n05_28.py`
- Run command: `.venv\Scripts\python.exe -m labs.N05.n05_28_token_path`

### Resource budget

The lab runs a full forward and backward pass with sequence length 4 and tokenwise cached forward passes in a model with 300 parameters. There is no model download or training.

### Actual code and execution results

<!-- N05_EXAMPLE: n05_28_token_path -->

### Checks

The tests check the shapes of nine activation and gradient slices, two residual equalities, the predicted token, a nonzero gradient, K and V cache shapes, and cached logit equivalence.

## Separating evidence levels

Distinguish the evidence covered in N05 as follows.

- Forward trace: Activations and shapes actually observed.
- Gradient: Local sensitivity near the reference point for a selected target.
- Intervention: A conditional effect measured after changing an activation.
- Checkpoint comparison: State and behavior differences between training times.

This integrated lab collects a forward trace and gradients and performs a cache comparison. It neither replaces activations nor compares different training checkpoints. Distinguish learning these evidence categories from measuring all four in this run.

Do not automatically promote a result at one level to a conclusion at another. For example, a nonzero gradient is not evidence that a feature is necessary, and a checkpoint difference is not the causal effect of a particular training example.

## Architecture boundaries

The instructional model uses full-dimension RoPE, causal MHA, serial pre-RMSNorm residuals, and dense SwiGLU. Pythia has partial RoPE, GPT-J parallel residuals, a GELU-family MLP, and a different normalization and implementation profile. In subsequent real-model experiments, module paths and tensor locations must be specified again to match Pythia's code.

The tiny decoder checks the shared mathematics and checking procedures. It does not mean that hook names and every intermediate value correspond unchanged across architectures.

## Common misconceptions

### Misconception 1. One token's path is confined to that token

Causal attention connects it to the K and V of past tokens.

### Misconception 2. The predicted token's gradient completely explains why it was generated

It shows local sensitivity for one target. Alternative targets, nonlinear effects, and distributed paths remain.

### Misconception 3. Tiny-model hook paths can be used unchanged in Pythia

The architecture and implementation differ, so corresponding locations must be identified again from the configuration and forward code.

## Cumulative assessment

### 1. From ID to embedding

State the operation converting token ID 2 into an embedding vector and its output shape.

<details><summary>Show solution</summary>It is the embedding table's row lookup $E[2]$. The slice for one token has shape $(d_{model},)=(4,)$.</details>

### 2. Causal prefix

Determine which key positions the query at zero-based position 2 can see.

<details><summary>Show solution</summary>Positions 0, 1, and 2. Position 3 is in the future and is masked.</details>

### 3. Residual equality

Calculate the residual mid for embedding $(1,0)$ and attention update $(0.2,-0.3)$.

<details><summary>Show solution</summary>Elementwise addition gives $(1.2,-0.3)$.</details>

### 4. MLP path

Identify the two tensors that must have the same hidden shape in SwiGLU.

<details><summary>Show solution</summary>They are $\operatorname{SiLU}(W_gx)$ and $W_ux$, which are multiplied elementwise.</details>

### 5. Logit selection

Explain how to obtain the greedy token from logits of shape `(16,)`.

<details><summary>Show solution</summary>Take the `argmax` index along the vocabulary axis.</details>

### 6. Interpreting a gradient

State the most limited conclusion supported by a nonzero $\nabla_{e_t}\ell_{t,v}$.

<details><summary>Show solution</summary>It is local-sensitivity evidence that a small embedding change can change the selected logit to first order at the reference point.</details>

### 7. Cache check

Calculate the total element count of K and V for two layers, two K and V heads, length 8, head dimension 4, and batch size 1.

<details><summary>Show solution</summary>The count is $2\times L\times B\times h_{kv}\times T\times d_h=2\times2\times1\times2\times8\times4=256$.</details>

### 8. Transfer to a real model

List four additional items to check before performing the same analysis in Pythia.

<details><summary>Show solution</summary>Check the model and tokenizer revisions; the layer, head, RoPE, and residual structure in the configuration; exact module paths and hook output types; and dtype, device, and cache layout. Also fix the input token index and target.</details>

## Sources and update boundaries

Attention, residual, and decoder computations are based on [Attention Is All You Need](https://arxiv.org/abs/1706.03762). The instructional variants are based on [RMSNorm](https://arxiv.org/abs/1910.07467), [RoFormer](https://arxiv.org/abs/2104.09864), and [GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202). The boundaries of the correspondence to Pythia were checked against the [official Pythia repository and configurations](https://github.com/EleutherAI/pythia).

## Lesson summary

- One token's path connects its embedding, attention, two residual updates, final norm, and logits.
- A shape ledger and residual equalities check hook locations.
- A selected logit's gradient represents local sensitivity to the embedding.
- Cached inference should agree with full causal logits within a tolerance.
- Separate the tiny model's mathematical checking procedure from module correspondence in an actual model.

## Pass criteria

- Can you reproduce the path from token ID to logits?
- Can you check all major shapes and residual equalities?
- Can you collect the embedding gradient of a selected logit?
- Can you compare cached and full logits and K and V shapes?
- Can you choose a claim strength appropriate to each of the four evidence levels?

## Next steps

- [I06-01 Behavioral and representation questions](../../part-3-interpretability/I06/I06-01-behavior-representation-question-design.md)

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] The cumulative path from token ID to logits is connected.
- [x] Residuals, gradients, and the cache are checked for the same input.
- [x] The N05 cumulative assessment is included.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretability claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Knowledge beyond the prerequisites is not required without explanation.
- [x] Internal links and equation rendering are checked.
- [x] Executable code is not manually duplicated in Markdown.
- [x] Source-code and test paths, resource budgets, and the verification date are recorded.
- [x] Tests for shapes, residuals, gradients, and cache equivalence are provided.
