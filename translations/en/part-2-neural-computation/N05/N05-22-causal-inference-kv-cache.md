---
id: "N05-22"
title: "Causal inference and the KV cache"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-21"
estimated_time: "120–150 minutes"
---

# N05-22. Causal inference and the KV cache

## Why this lesson matters

Autoregressive generation does not require recomputing earlier tokens' keys and values at every step. A KV cache stores past K and V separately for each layer and adds only the current token's projections. In this lesson, `inference` means running a causal language model, not causal inference about causal effects.

## Learning objectives

- Distinguish full recomputation without a cache from tokenwise cached inference.
- Calculate per-layer K and V cache shapes.
- Write the equation appending a new key and value along the sequence axis.
- Compare cached logits and full causal logits in the same model.
- Avoid confusing a cache with activation evidence or model memory.

## Prerequisite check

- Prerequisite lesson: [N05-21 Language model objective](N05-21-language-model-objective.md)
- Check question: Can you explain why a past position's representation does not depend on future tokens under a causal mask?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $K_{<t}^{(l)}$ | `cached keys before t at layer l` | Cache of past keys at layer $l$ | $B\times h_{kv}\times(t-1)\times d_h$ |
| $V_{<t}^{(l)}$ | `cached values before t at layer l` | Cache of past values at layer $l$ | Same cache shape |
| $q_t$ | `the query at time t` | Current token's query | $B\times h_q\times1\times d_h$ |
| prefill | `prefill` | Stage processing the entire prompt to create the initial cache | inference stage |
| decode step | `decode step` | Stage usually inputting one new token to obtain the next logits | inference stage |
| KV cache | `key-value cache` | Past keys and values stored per layer for reuse | runtime state |

## Core concept 1. Cache update

Let $k_t,v_t$ be the current projections at position $t$. Append them along the sequence axis:

\[
K_{\le t}=\operatorname{concat}(K_{<t},k_t),
\qquad
V_{\le t}=\operatorname{concat}(V_{<t},v_t)
\]

The current query requires only the computation

\[
\operatorname{Attention}(q_t,K_{\le t},V_{\le t})
\]

Maintain a separate cache for each layer.

The new $k_t,v_t$ each have sequence length 1, and concatenation brings the length to $t$. This does not add heads or features. The current query has one position, but it compares against $t$ past and current keys, so the two position axes of the per-head scores have shape $(1,t)$. Although past query outputs need not be recomputed, the current query's comparisons with past keys and its weighted sum of values remain.

The small two-feature vectors below show the direction in which the cache length grows.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Separate key and value arrays append a current two-feature vector after two past positions while keeping feature width two](../../figures/assets/N05/N05-22-cache-sequence-append.svg)

<figcaption>Appending the current position after two past positions increases the sequence lengths of K and V from 2 to 3. Each vector still has two features. The arrays are updated separately, not combined with each other.</figcaption>
</figure>

Applying the current query to the same key example produces three comparison results in one row.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A single current query one one compares with three cached keys and produces one score row with three columns](../../figures/assets/N05/N05-22-query-cached-key-row.svg)

<figcaption>Taking the dot product of the current q=(1,1) with each of three keys and dividing by √2 gives scores of approximately (0.707,0.707,1.414). The query length is 1, but there are three keys to compare, giving score shape (1,3). Softmax and a weighted sum of values are still required.</figcaption>
</figure>

Each layer creates K and V from different hidden states and projection weights. Do not reuse one layer's cache unchanged in another layer. The new token also does more than compute attention: it passes through that layer's residual and MLP computations to reach the next layer, where new K and V are also created and appended to the cache.

Distinguish the current hidden state passing between layers from the cache updated separately by each layer.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The current token crosses layer zero and layer one while each layer appends its own projected keys and values to a separate cache](../../figures/assets/N05/N05-22-layer-specific-cache.svg)

<figcaption>Downward arrows show the current token's input to the next layer. Rightward arrows show the addition of current K and V created at that layer to its cache. The cache does not store all residual and MLP activations.</figcaption>
</figure>

## Core concept 2. Full and cached results

With dropout disabled and matching position handling, masks, dtype, and weights, cached inference should compute the same mathematical function as the logits at each position in a full causal forward pass. Actual hardware and kernels can produce small floating-point differences due to operation order, so compare with a tolerance.

Past positions do not attend to future tokens, and normalization and MLP computations are applied per token. Thus, appending a token to the end of the same prefix does not change the past hidden states or each layer's K and V already computed. This dependency relationship allows the stored values to be reused. With attention that also looks at the future, a new token can change past representations, so the same argument does not apply.

The two runs being compared must receive the same token prefix. A cache created for a different prompt is not the same state even if its shape matches. With RoPE, the new token's position must also match the accumulated cache length. Resetting it to the first position of a short input every time computes a different rotation from the full forward pass.

The two runs below compare the last position of the same four tokens. Whether values are reused does not change the token positions.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Full recomputation and cached decoding use the same four token IDs and positions while only the current position recomputes its key and value in the cached run](../../figures/assets/N05/N05-22-full-cached-prefix.svg)

<figcaption>The upper run recomputes K and V for all four positions; the lower run reuses them for the three past positions. New token ID 7 is at position 3 in both runs. Check agreement of the last-position logits under matching execution conditions using a tolerance.</figcaption>
</figure>

## Core concept 3. Cache cost

For $L$ layers, $h_{kv}$ K and V heads, accumulated length $T$, head dimension $d_h$, batch size $B$, and $s$ bytes per element, the simple cache byte count is

\[
2LBTh_{kv}d_hs
\]

It grows linearly with sequence length. MQA and GQA reduce $h_{kv}$ to make the cache smaller.

## Example

Each layer's cache in the lab has shape `(1,1,T,4)`. Inputting tokens one at a time increases the sequence-axis length through `1, 2, 3, 4`. At length 4, the combined element count of K and V is $2\times1\times1\times4\times4=32$.

Stacking the elements added separately by K and V shows the linear growth.

<figure class="lesson-figure" markdown="1">

![Stacked key and value counts grow from eight to thirty two stored elements as cached sequence length increases from one to four](../../figures/assets/N05/N05-22-cache-growth.svg)

<figcaption>This setting stores four elements in K and four in V per position, increasing the total by eight each time. The 32 at length 4 is an element count, not a byte count. If each element occupies 4 bytes, this simple cache occupies 128 bytes.</figcaption>
</figure>

## Executable lab

### Environment and source

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Verification date: 2026-10-01
- Component category: `Common modern variant`
- Shared implementation: `labs/N05/tiny_decoder.py`
- Example ID: `n05_22_kv_cache`
- Source code: `labs/N05/n05_22_kv_cache.py`
- Tests: `tests/N05/test_n05_22.py`
- Run command: `.venv\Scripts\python.exe -m labs.N05.n05_22_kv_cache`

### Resource budget

The lab uses batch size 1, sequence length 4, one layer, one head, dimension 4, and 300 parameters. It runs only one full forward pass and four tokenwise forward passes.

### Actual code and execution results

<!-- N05_EXAMPLE: n05_22_kv_cache -->

### Checks

The tests check numerical agreement between cached and full causal logits, growth in cache length, and the final K and V shapes.

## Prefill and decode

A long prompt is usually processed in one prefill pass to populate K and V. Subsequent decode steps input only the new token and update the cache. A cache does not eliminate attention's reading of past K and V. It avoids recomputing past tokens' projections.

Cache APIs may have dynamic, static, sliding-window, and quantized forms. For a mathematical comparison, first check that the stored position range, mask, and position IDs match.

## Connection to model interpretability

A KV cache contains attention projections stored during inference. It is not long-term memory or the learned parameters themselves. Changing the prompt or clearing the cache also changes the runtime state.

When comparing activations in cached and full runs, distinguish the current token's residual from the K and V cache. Patching the cache changes a past-information path at a particular layer, so it is not the same operation as simply removing an input token.

## Common misconceptions

### Misconception 1. The KV cache stores all past activations

A basic cache stores keys and values for reuse in attention separately for each layer. It does not store the entire residual stream or all MLP activations.

### Misconception 2. Using a cache eliminates attention computation

Scores between the current query and accumulated K, softmax, and the weighted sum of V are still computed.

### Misconception 3. A cache should always be enabled during training too

Teacher-forced training computes the entire sequence in parallel, and caching is generally an inference optimization. Careless reuse during training can cause problems with the gradient graph and sequence handling.

## Exercises

### 1. Cache shape

Determine the K cache shape of one layer when $B=2$, $h_{kv}=4$, $T=10$, $d_h=8$.

<details><summary>Show solution</summary>The shape is $(2,4,10,8)$.</details>

### 2. Element count

Calculate the combined element count of K and V in one layer under the preceding conditions.

<details><summary>Show solution</summary>The count is $2\times2\times4\times10\times8=1{,}280$.</details>

### 3. Update axis

Determine the axis along which a new key is appended to the cache.

<details><summary>Show solution</summary>It is the sequence-length axis, the second-to-last axis in the notation `(B,h,T,d_h)`.</details>

### 4. Query shape

Determine the usual query sequence length for a one-token decode step.

<details><summary>Show solution</summary>It is 1. The K and V sequence length is the accumulated length of the past and current tokens.</details>

### 5. Diagnose a result mismatch

What should you check first when cached logits differ substantially from full logits?

<details><summary>Show solution</summary>First check the position offset, causal mask, axis along which K and V were appended, and agreement of the model's evaluation mode and weights.</details>

### 6. Interpretation scope

Is setting one layer's values to 0 in the cache the same as deleting an input token?

<details><summary>Show solution</summary>No. It changes only the past-value transmission path in that layer's attention. Information may remain in other layers' caches and the current residual.</details>

## Sources and update boundaries

The basic causal-attention equation is based on [Attention Is All You Need](https://arxiv.org/abs/1706.03762). Current cache shapes and update contracts were checked against the [Hugging Face Transformers caching documentation](https://huggingface.co/docs/transformers/v5.6.0/cache_explanation). Cache classes and APIs change with library versions, so treat them separately from the mathematical state described here.

## Lesson summary

- A KV cache stores past keys and values along the sequence axis separately for each layer.
- A decode step uses the current query and accumulated K and V.
- Cached inference should numerically agree with a full causal forward pass under matching conditions.
- Cache memory grows linearly with length, layer count, K and V head count, and head dimension.
- A KV cache is runtime state, not learned long-term memory or a full activation dump.

## Pass criteria

- Can you distinguish full recomputation from cached inference?
- Can you calculate the cache shape and byte count?
- Can you write the cache-update equation?
- Can you compare full and cached logits within a tolerance?
- Can you explain the scope of a cache intervention?

## Next lesson

- [N05-23 Decoding and generation](N05-23-decoding-generation.md)

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] Full causal inference and the KV cache are compared.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretability claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Knowledge beyond the prerequisites is not required without explanation.
- [x] Internal links and equation rendering are checked.
- [x] Executable code is not manually duplicated in Markdown.
- [x] Source-code and test paths, resource budgets, and the verification date are recorded.
- [x] Tests for cache shape, length, and logit equivalence are provided.
