# N05 architecture and source baseline

## 1. Purpose

N05 does not describe a particular product or a single latest model. After completing this stage, learners should be able to read the configuration and computation graph of an open model and distinguish shared computations from model-specific choices.

This document defines the N05 reference architecture, component categories, source selection, and update rules. The initial review date is 2026-10-01. At the start of each N05 lesson batch, the original papers and public configurations are checked again and the review date is updated.

## 2. Component categories

| Category | Criteria | Treatment in the text |
|---|---|---|
| Stable core | Required to compute the path from tokens to logits or to trace the backward pass. Multiple architectures share the same mathematical structure. | Include definitions, shapes, hand calculations, and executable labs. |
| Instructional reference | A choice fixed by the project to connect the Stable core within one model. | Use the same choice in all cumulative labs. |
| Common modern variant | Used in multiple open model families and changes tensor shapes, information paths, or stored state. | Compare what remains unchanged and what differs from the reference computation. |
| Architecture-specific | A choice made for the performance or efficiency of a particular family, which is difficult to treat as a common assumption. | Separate it into an architecture profile or optional reading. |
| Implementation optimization | Computes the same mathematical function using different memory access patterns or kernels. | Distinguish mathematical outputs from execution methods. |

A new component may be promoted to Common modern variant or a higher category when all of the following conditions hold.

1. The original paper or an official technical report specifies the computation.
2. Tensor shapes and data flow can be checked in a public configuration or implementation.
3. The difference matters when learners interpret activations, gradients, the residual stream, or model state.
4. Use has been confirmed in at least two independent open model families, or the component is essential to a later interpretability lesson even if it occurs in only one family.

Publication date, leaderboard rank, and product recognition alone do not justify promotion.

## 3. Instructional reference architecture

The cumulative N05 labs implement a small decoder-only causal language model directly. The reference model uses the following choices.

| Location | Reference choice | Comparison |
|---|---|---|
| Block order | Pre-norm decoder block | Post-norm |
| Normalization | RMSNorm | LayerNorm |
| Positional information | RoPE | Learned absolute embeddings, sinusoidal encoding |
| Attention | Causal multi-head attention | MQA, GQA |
| MLP | Dense SwiGLU feed-forward network | ReLU, GELU, ordinary GLU, MoE |
| Residual | Residual addition of attention and MLP outputs | Model-specific arrangements such as parallel residual |
| Output | Explicit unembedding and softmax | Input-output weight tying |
| Training | Cross entropy and AdamW | Optimizer and schedule variants |
| Inference state | Causal mask and KV cache | Full recomputation without a cache |

Using multi-head attention and a dense MLP as the reference makes head- and token-specific computation paths directly traceable. After understanding the reference computation, learners study GQA and MoE through their differences in head sharing and conditional routing.

Labs first use instructional matrix operations. When introducing a fused kernel or FlashAttention, outputs and gradients for the same inputs are compared with those of the reference implementation.

## 4. Current component classification

| Component | Category | N05 treatment |
|---|---|---|
| Tensor shapes, affine maps, activations, softmax, cross entropy | Stable core | N05-01–05 |
| Backpropagation, mini-batches, optimizer state, autograd | Stable core | N05-06–10 |
| Tokenization, embedding, unembedding | Stable core | N05-11–12 |
| Causal scaled dot-product attention and residual addition | Stable core | N05-14–17 |
| RoPE, RMSNorm, SwiGLU | Instructional reference | Compare with simpler preceding approaches in the same lessons. |
| MHA | Instructional reference | Specify the queries, keys, and values of every head. |
| MQA and GQA | Common modern variant | Calculate key-value head sharing and changes in cache shape. |
| KV cache | Common modern variant | Distinguish training computations from autoregressive inference state. |
| FlashAttention and fused attention kernels | Implementation optimization | Separate them from the definition of attention. |
| MoE and expert routing | Architecture-specific | Require only the differences in computation paths from a dense MLP. |
| MLA, sparse and linear attention, SSMs, hybrid blocks | Architecture-specific | Record in architecture profiles; do not require as shared prerequisites. |
| Quantization and speculative decoding | Architecture-specific | Place in optional lessons on numerical representations or systems optimization. |

## 5. Lab models and external models

Required labs use a tiny decoder that can run on a CPU. The lesson text does not treat a library's high-level Transformer block as the definitive implementation.

The execution environment and resource limits follow the [N05 execution environment](N05-ENVIRONMENT.md). Code sources are `.py` files in `labs/N05`, and tests and site builds import or execute the same files. This path was verified in the N05-01–N05-03 pilot, and later lessons extend the same approach.

External models are used for only two purposes.

- Compare public configurations and actual tensor shapes with the reference model.
- Use reproduction materials in later lessons that require hooks, checkpoints, and learning-dynamics experiments.

Selecting an external model requires more than checking for open weights. Its configuration, tokenizer, forward implementation, license, and required computational resources are also checked. Models such as Pythia, which provide multiple training checkpoints and the data order, are candidates for I08 learning-dynamics labs. The required N05 computations must remain executable without downloading an external model.

## 6. Source priority

When checking architecture facts in a lesson, use sources in the following order.

1. Original papers
2. Official technical reports
3. Public configurations and forward implementations
4. Official model cards and training records
5. Reproduction papers

Surveys, lectures, and blogs may guide exploration but are not used as the sole evidence for core computations. For closed models, record only verifiable facts in the architecture profile.

The following primary sources were checked when establishing the initial baseline.

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [Root Mean Square Layer Normalization](https://arxiv.org/abs/1910.07467)
- [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864)
- [GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202)
- [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://arxiv.org/abs/2305.13245)
- [FlashAttention](https://arxiv.org/abs/2205.14135)
- [OpenELM](https://arxiv.org/abs/2404.14619)
- [Pythia](https://arxiv.org/abs/2304.01373)
- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

## 7. Per-lesson record format

N05 lessons addressing architecture components include the following items.

- Status: one of `Stable core`, `Instructional reference`, `Common modern variant`, `Architecture-specific`, or `Implementation optimization`
- Date checked: `YYYY-MM-DD`
- Reference computation: input and output shapes and the core equations
- Comparison: what is shared and what changes
- Interpretability impact: changes to activations, gradients, caches, or intervention locations
- Evidence: the original papers and the public configurations or implementations checked

N05 authors review this document and the component classification after completing N05-10, N05-20, and N05-28. A new paper alone does not justify revising a completed lesson. If an error in an existing explanation is found, or evidence accumulates for a change in component category, update both the lesson and its review date.

## 8. N05-10 review record

- Date checked: 2026-10-01
- Scope: N05-01–N05-10
- Result: retain the `Stable core` classification for tensors, activations, softmax, cross entropy, backpropagation, mini-batches, optimizer state, and automatic differentiation.
- API check: `torch.func.jvp`, `vjp`, and `jacrev` were run in local PyTorch 2.13.0+cpu and compared with their definitions in the current stable official documentation.
- Public configurations: N05-01–N05-10 cover model-independent computations, so no specific model configuration was added as evidence. Public configuration comparisons begin with N05-11 onward, where Transformer components are addressed.

## 9. N05-20 review record

- Date checked: 2026-10-01
- Scope: N05-11–N05-20
- Result: retain the classifications for tokenization, embedding, RoPE, causal attention, and residual addition. RMSNorm, SwiGLU, and serial pre-norm blocks are instructional reference choices, and the text distinguishes them from assumptions shared by all real models.
- Public configurations: the official Pythia-160M training configuration was checked for 12 layers, hidden size 768, 12 attention heads, a RoPE fraction of 0.25, GPT-J parallel residual, untied output, and FlashAttention.
- Comparison conclusion: the instructional tiny decoder uses full-dimension RoPE, RMSNorm, dense SwiGLU, and serial residual. Pythia is a target for later real-model analysis and is not described as a reduced version of the tiny decoder.
- Implementation verification: unit tests pin down the embedding, causal MHA, pre-RMSNorm residual, dense SwiGLU, final normalization, unembedding, and per-layer KV cache shapes in the 300-parameter CPU tiny decoder.

## 10. N05-28 review record

- Date checked: 2026-10-01
- Scope: N05-21–N05-28 and the full cumulative N05 lab
- Result: retain the `Stable core` classification for next-token cross entropy, the causal mask, residual addition, and the token-to-logit path. KV caching is a `Common modern variant` that changes inference state; hook and checkpoint APIs are treated separately as framework-specific implementations.
- Cumulative implementation: the 300-parameter tiny decoder was checked along a single path covering token IDs, embedding, full-dimension RoPE causal MHA, serial pre-RMSNorm residual, dense SwiGLU, final normalization, untied unembedding, gradients, and K and V caches.
- Real-model boundary: the Pythia main suite uses partial RoPE, GPT-J parallel residual, untied output, and a FlashAttention configuration. In Phase 3, build a separate runner suited to Pythia module paths and the Hugging Face cache API, and do not reuse tiny-decoder hook names.
- Phase 3 inputs: the tiny decoder's forward hooks, non-leaf activation gradients, strict model-state loading, and cached/full logit equivalence serve as reference tests for later real-model fixtures.
