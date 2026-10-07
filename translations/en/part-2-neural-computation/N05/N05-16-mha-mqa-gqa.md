---
id: "N05-16"
title: "MHA, MQA, and GQA"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-15"
estimated_time: "120–150 minutes"
---

# N05-16. MHA, MQA, and GQA

## Why this lesson matters

Attention does not always have the same number of query, key, and value heads. MQA and GQA share key-value heads to reduce the KV cache and memory bandwidth during generation. Understanding this difference lets you read model configurations, cached tensor shapes, and per-head activations correctly.

## Learning objectives

- Distinguish the numbers of query and key-value heads in MHA, MQA, and GQA.
- Calculate the Q, K, and V shapes for each variant.
- Show how key-value heads are assigned to query heads.
- Compare KV cache element counts.
- Avoid confusing head sharing with head importance.

## Prerequisite check

- Prerequisite lesson: [N05-15 Causal scaled dot-product attention](N05-15-causal-scaled-dot-product-attention.md)
- Check question: Can you calculate the query-key scores and weighted sum of values for one attention head?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $h_q$ | `h sub q` | Number of query heads | positive integer |
| $h_{kv}$ | `h sub k v` | Number of key-value heads | $h_{kv}\mid h_q$ |
| $d_h$ | `d sub h` | Head dimension | positive integer |
| MHA | `multi-head attention` | A structure using a separate K and V head for each query head | $h_{kv}=h_q$ |
| MQA | `multi-query attention` | A structure in which all query heads share one K and V head | $h_{kv}=1$ |
| GQA | `grouped-query attention` | A structure sharing a K and V head within each group of query heads | $1<h_{kv}<h_q$ |

## Core concept 1. The head axis

In batch-first notation, the tensors after projection and reshaping are

\[
\mathbf Q\in\mathbb R^{B\times h_q\times T\times d_h},
\qquad
\mathbf K,\mathbf V\in\mathbb R^{B\times h_{kv}\times T\times d_h}
\]

To obtain the K and V head used by each query head, repeat the key-value heads along the head axis or broadcast the same storage.

This lesson uses the same head dimension $d_h$ for keys and values. The last feature dimension of the Q projection has length $h_qd_h$. Split it into head-specific groups of length $d_h$, then move the head axis before the token axis. Apply the same procedure to K and V, starting from $h_{kv}d_h$. Distinguish a reshape that preserves the element count from a transpose that changes the axis order.

The indexed example below shows that the element values do not change: feature groups belonging to the same token move into head-specific positions.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

  ![Two token rows of eight indexed features split into four two-feature heads while preserving token membership](../../figures/assets/N05/N05-16-feature-to-head-axes.svg)
  <figcaption>This example projection contains the numbers 0–15 in order. Splitting features into pairs and moving the head axis to the front does not mix the elements of the first and second tokens within any head.</figcaption>
</figure>

Each query head computes a $T\times T$ attention-weight array and a $T\times d_h$ output for that head. Concatenate the outputs of multiple heads along the feature dimension for each token, then pass them to the output projection. Sharing K and V does not remove the per-query-head computations or output positions.

Concatenation also collects the head outputs for a fixed token into the same row.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

  ![Four two-coordinate head outputs for one fixed token concatenate into eight feature slots before output projection](../../figures/assets/N05/N05-16-head-output-concat.svg)
  <figcaption>Illustrative numbers represent the head outputs for one token. Concatenating the two coordinates from each of four heads produces a feature row of length 8, which is then passed to the output projection.</figcaption>
</figure>

## Core concept 2. Three sharing schemes

For $h_q=4$, the assignments are as follows.

- MHA: Assign K and V heads `0, 1, 2, 3` to query heads `0, 1, 2, 3`, respectively.
- MQA: All four query heads share K and V head `0`.
- GQA with $h_{kv}=2$: Query heads `0, 1` use K and V head `0`, while query heads `2, 3` use K and V head `1`.

The group size in GQA is $g=h_q/h_{kv}$. This assignment can be expressed as simple contiguous groups when the number of query heads is divisible by the number of key-value heads.

Below, the difference among the three schemes is the number of K and V groups reached by the arrows, not the number of queries.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

  ![Four query heads connect to four separate KV heads in MHA, one shared KV head in MQA, or two grouped KV heads in GQA](../../figures/assets/N05/N05-16-sharing-assignment.svg)
  <figcaption>All four query heads remain. MHA uses a different K and V head for each, MQA uses one shared K and V head, and this GQA example uses the same K and V head for each pair of queries.</figcaption>
</figure>

Query heads in the same group compute dot products with the same keys, but their query vectors come from each head's own projection. Different queries can produce different scores and softmax weights for the same keys. Sharing values therefore does not make the head outputs identical. What is shared is the K and V values and their parameter paths; each query computes how much to attend to each position.

The small calculation below allows both key positions, isolating why sharing and identical outputs are different conditions.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

  ![Two distinct queries attending to the same identity keys and value vectors yield reversed attention weights and distinct weighted outputs](../../figures/assets/N05/N05-16-shared-kv-distinct-outputs.svg)
  <figcaption>The same K and V produce reversed weights across the two positions when the queries are (1,0) and (0,1). The outputs also differ, at approximately (1.34,0.66) and (0.66,1.34), respectively. This example omits a mask to isolate the sharing relationship.</figcaption>
</figure>

## Core concept 3. KV cache cost

The number of elements needed to store both K and V in one layer is

\[
2BT h_{kv}d_h
\]

With the same $B,T,d_h$, MQA stores $1/h_q$ as many K and V elements as MHA, and GQA stores $h_{kv}/h_q$ as many. Multiply this count by the bytes per element of the dtype to obtain the actual byte count.

The element count of K is the product of its four axis lengths, $BTh_{kv}d_h$. Storing V with the same shape doubles the count. This expression gives the cost when each shared K and V is stored once in the cache. If expanded copies are stored separately for computation, their storage is additional. Do not interpret this expression as reducing per-query-head score computation, other activations, or model-weight memory by the same ratio.

## Example

For $B=1$, $T=2$, $h_q=4$, $d_h=2$, the combined element counts of K and V are as follows.

| Scheme | $h_{kv}$ | Shape of K and V, each | K+V element count |
|---|---:|---|---:|
| MHA | 4 | $(1,4,2,2)$ | 32 |
| MQA | 1 | $(1,1,2,2)$ | 8 |
| GQA | 2 | $(1,2,2,2)$ | 16 |

During computation, sharing makes all three correspond to $(1,4,2,2)$. A logical expansion is needed, but it does not necessarily require copying memory.

Compare storage by counting the K and V heads stored separately, not the expanded logical shape.

<figure class="lesson-figure" markdown="1">

  ![Stacked key and value storage bars total 32, 8, and 16 elements for MHA, MQA, and GQA with the same four queries](../../figures/assets/N05/N05-16-cache-elements.svg)
  <figcaption>The example fixes B=1, T=2, and head dimension=2. The combined heights of blue K and green V are 32, 8, and 16, respectively; all three schemes have four query heads.</figcaption>
</figure>

## Executable lab

### Environment and source

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Verification date: 2026-10-01
- Component category: `Common modern variant`
- Example ID: `n05_16_attention_head_sharing`
- Source code: `labs/N05/n05_16_attention_head_sharing.py`
- Tests: `tests/N05/test_n05_16.py`
- Run command: `.venv\Scripts\python.exe -m labs.N05.n05_16_attention_head_sharing`

### Resource budget

The lab uses batch size 1, sequence length 2, four query heads, and head dimension 2. It performs no generation or training.

### Actual code and execution results

<!-- N05_EXAMPLE: n05_16_attention_head_sharing -->

### Checks

The tests check the logically expanded shapes of all three schemes, the sharing relationships in MQA and GQA, and the K+V element counts.

## Reading model configurations

Implementations record $h_q$ and $h_{kv}$ under names such as `num_attention_heads` and `num_key_value_heads`. Equal values indicate MHA, one key-value head indicates MQA, and an intermediate number indicates GQA. Field names and tensor-axis order can differ by architecture, so also check the model code.

## Connection to model interpretability

In GQA, Q activations differ across query heads, but heads within the same group share K and V activations. Thus, the phrase `the value vector of attention head 2` may not refer to an independent value projection. First check whether the head axis of a hooked tensor indexes query heads or key-value heads.

Head ablation also requires distinguishing the Q path, attention weights, shared K and V paths, and output slices. Changing one shared K and V head affects multiple query heads at once, so it is not the same operation as intervening on a single query head.

With attention weights fixed, changing one shared value passes a change to each query that reads it, scaled by that query's own weight.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

  ![Changing one shared value from one zero to two zero shifts two query outputs by their fixed weights while another KV group remains unchanged](../../figures/assets/N05/N05-16-shared-value-intervention.svg)
  <figcaption>In this example, the value at token 0 in the first group changes from (1,0) to (2,0). With Q, K, and attention weights fixed, the two query outputs before output projection change by (0.25,0) and (0.75,0), respectively. The direct change in the other K and V group is 0.</figcaption>
</figure>

## Common misconceptions

### Misconception 1. GQA reduces the number of attention heads

It reduces the number of key-value heads while retaining the number of query heads.

### Misconception 2. Repeated K and V tensors come from different parameters

Logical repetition means that multiple query heads share the same K and V head.

### Misconception 3. MQA is always more accurate

MQA offers cache and bandwidth advantages, but quality and speed must be evaluated for the architecture, training, and implementation.

## Exercises

### 1. Identify the scheme

Determine which attention scheme has $h_q=8$ and $h_{kv}=8$.

<details><summary>Show solution</summary>There is one K and V head for each query head, so this is MHA.</details>

### 2. Group size

Calculate the group size of GQA with $h_q=16$, $h_{kv}=4$.

<details><summary>Show solution</summary>It is $16/4=4$. Four query heads share one K and V head.</details>

### 3. Shape

Determine the shape of K when $B=2$, $T=32$, $h_q=8$, $h_{kv}=2$, $d_h=64$.

<details><summary>Show solution</summary>The shape is $(2,2,32,64)$.</details>

### 4. Cache elements

Calculate the combined element count of K and V in one layer for the preceding exercise.

<details><summary>Show solution</summary>The count is $2\times BTh_{kv}d_h=2\times2\times32\times2\times64=16{,}384$.</details>

### 5. Assignment

Determine the index of the K and V head used by query head 6 when $h_q=8$, $h_{kv}=2$.

<details><summary>Show solution</summary>The group size is 4, so query heads 4–7 use K and V head 1. The answer is 1.</details>

### 6. Interpreting an intervention

Can you change one K and V head in GQA and report that you intervened on only one query head?

<details><summary>Show solution</summary>No. The score or value paths of the entire query-head group sharing that K and V head are affected.</details>

## Sources and update boundaries

The MHA definition follows [Attention Is All You Need](https://arxiv.org/abs/1706.03762). The GQA structure and evidence comparing quality and speed follow [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://arxiv.org/abs/2305.13245). Model-specific field names, fused kernels, and cache layouts are implementation details that can change substantially.

## Lesson summary

- MHA, MQA, and GQA differ in how much query heads share K and V heads.
- Read the numbers of Q heads and K and V heads as separate axes.
- KV cache size is proportional to $h_{kv}$.
- GQA groups multiple query heads under one K and V head.
- An intervention on shared K and V changes a broader path than an intervention on one query head.

## Pass criteria

- Can you identify MHA, MQA, and GQA from a configuration?
- Can you calculate the Q, K, and V shapes?
- Can you show the query-to-KV head assignment?
- Can you compare KV cache element counts?
- Can you explain the scope of a shared-head intervention?

## Next lesson

- [N05-17 Residual stream](N05-17-residual-stream.md)

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] The shapes and sharing structures of MHA, MQA, and GQA are distinguished.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretability claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Knowledge beyond the prerequisites is not required without explanation.
- [x] Internal links and equation rendering are checked.
- [x] Executable code is not manually duplicated in Markdown.
- [x] Source-code and test paths, resource budgets, and the verification date are recorded.
- [x] Shape, sharing-relationship, and resource tests are provided.
