---
id: "N05-14"
title: "Query, key, and value"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-13"
estimated_time: "120~150 minutes"
---

# N05-14. Query, key, and value

## Why this lesson matters

Self-attention forms queries, keys, and values from the same hidden state using different linear projections. Query-key dot products produce scores for deciding which source positions to attend to, while values supply the content to be combined in a weighted sum.

## Learning objectives

- Calculate Q, K, and V projection shapes.
- Explain the rows and columns of a query-key score matrix.
- Distinguish the roles of values in score computation and output computation.
- Distinguish hook locations for Q, K, and V activations.
- Avoid equating a large attention score with an explanation.

## Prerequisite check

- Prerequisite lesson: [N05-13 Position information and RoPE](N05-13-position-information-rope.md)
- Check question: Can you calculate the shapes of a row-batch affine map?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\mathbf H$ | `H` | Token hidden states | $\mathbb R^{T\times d_{model}}$ |
| $\mathbf Q$ | `Q` | Query projection | $\mathbb R^{T\times d_k}$ |
| $\mathbf K$ | `K` | Key projection | $\mathbb R^{T\times d_k}$ |
| $\mathbf V$ | `V` | Value projection | $\mathbb R^{T\times d_v}$ |
| $S_{ij}$ | `S sub i j` | Raw score between query position $i$ and key position $j$ | Scalar |

## Core concept 1. Three projections

\[
\mathbf Q=\mathbf H\mathbf W_Q^\top,
\quad
\mathbf K=\mathbf H\mathbf W_K^\top,
\quad
\mathbf V=\mathbf H\mathbf W_V^\top
\]

Although all three use the same $\mathbf H$, they use different weights and therefore have distinct tensor roles. Their values may happen to agree for a particular input. This lesson omits bias.

The shapes of $\mathbf W_Q,\mathbf W_K$ are $(d_k,d_{model})$, while the shape of $\mathbf W_V$ is $(d_v,d_{model})$. Each projection sums over the model feature axis and retains the token position axis. This stage does not yet mix values across tokens; it applies the same projection weights at every position. Q and K must have the same feature length for their dot product, but V can have a different length.

A query evaluates what to attend to, a key is what gets evaluated, and a value is what is obtained from that source. These names do not refer to separate sets of tokens. Each hidden row produces all three vectors; the subsequent score calculation connects one query row with multiple key rows.

In the key paths below, expand the computation that reuses the same weights at each token row.

<figure class="lesson-figure" markdown="1">

![Hidden row one two and hidden row three four independently reuse the same key weight matrix one one one minus one producing key rows three minus one and seven minus one without crossing token paths](../../figures/assets/N05/N05-14-shared-weight-rows.svg)

<figcaption>The lab's key projection is expanded at each token row. Both paths use the same W_K, and each uses only its own hidden state's two features. There are no separate token-specific weights, nor are the two hidden states added together here.</figcaption>
</figure>

## Core concept 2. The score matrix

Raw scores are

\[
\mathbf S=\mathbf Q\mathbf K^\top,
\qquad
S_{ij}=\mathbf q_i^\top\mathbf k_j
\]

Row $i$ gives the evaluations by query position $i$ of every key position. Column $j$ gives the scores key position $j$ receives from multiple queries.

In $S_{ij}=\sum_{k=1}^{d_k}q_{ik}k_{jk}$, feature index $k$ is summed out, leaving the two position indices $i,j$. Thus, $(T,d_k)(d_k,T)$ gives shape $(T,T)$. The entries $S_{ij}$ and $S_{ji}$ are different comparisons with query and key roles exchanged, so they are not generally equal. Equality of the two in the small example below does not establish that score matrices are symmetric in general.

Raw scores can be negative, and a row need not sum to 1. A dot product also depends on both vectors' lengths, not just their angle, so it is not automatically cosine similarity. The next lesson applies scaling, masking, and softmax to turn scores into weights for a weighted sum.

Values do not enter these scores. After masking and softmax, attention weights combine value rows in a weighted sum.

Changing only V while holding Q and K fixed preserves the scores but changes the values to transmit. Changing H before projection, by contrast, can change all three paths together. The meaning of an intervention depends on what is held fixed. Even a position with a large weight can have a small output change if its value is small or cancels with values at other positions. Attention proportions and transmitted content therefore require separate checks.

In the coordinate plot below, compare dot products and cosines while keeping the key direction fixed and changing only its length.

<figure class="lesson-figure" markdown="1">

![Query one two key three minus one and doubled key six minus two on a coordinate grid show same key direction with doubled norm raw dot increasing one to two while cosine remains one over square root fifty](../../figures/assets/N05/N05-14-dot-versus-cosine.svg)

<figcaption>The lab's q₀, k₀ are shown together with 2k₀ for a length comparison. The key direction is unchanged, but its doubled norm increases the raw dot product from 1 to 2. Dividing by both norms gives the same cosine, 1/√50 ≈ 0.1414.</figcaption>
</figure>

In the separate value path below, examine the meaning of a comparison holding Q/K fixed.

<figure class="lesson-figure" markdown="1">

![Fixed query and key retain raw scores one five five seventeen and later form weights while replacing value by doubled rows four two twelve four changes the separate content path before weighted sum](../../figures/assets/N05/N05-14-value-bypasses-score.svg)

<figcaption>This comparison holds Q/K fixed and replaces only the lab's V with 2V. Raw S and the subsequent weight calculation are unchanged, but the value rows entering the weighted sum become (4, 2), (12, 4). An intervention on H could change Q/K/V together and would differ from this comparison.</figcaption>
</figure>

## Example

Applying the lab weights to

\[
\mathbf H=\begin{bmatrix}1&2\\3&4\end{bmatrix}
\]

gives

\[
\mathbf Q=\begin{bmatrix}1&2\\3&4\end{bmatrix},
\quad
\mathbf K=\begin{bmatrix}3&-1\\7&-1\end{bmatrix},
\quad
\mathbf V=\begin{bmatrix}2&1\\6&2\end{bmatrix}
\]

The raw scores are

\[
\mathbf Q\mathbf K^\top=
\begin{bmatrix}1&5\\5&17\end{bmatrix}
\]

In the three-projection diagram below, read the actual numbers from the lab weights down to the outputs.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Hidden rows one two and three four branch through identity query weights key sum difference weights and value scaling weights to query one two three four key three minus one seven minus one value two one six two](../../figures/assets/N05/N05-14-three-projections.svg)

<figcaption>Read the three sets of lab weights and their projection results from top to bottom. All receive the same H but perform different feature computations. The two result rows remain token positions 0 and 1; tokens have not yet been mixed.</figcaption>
</figure>

In the following score array, identify the cell where one query meets one key.

<figure class="lesson-figure" markdown="1">

![Raw score matrix one five five seventeen uses query positions as rows and key positions as columns with the query zero key one cell five selected and computed as one times seven plus two times minus one](../../figures/assets/N05/N05-14-score-indices.svg)

<figcaption>The orange cell compares query position 0 with key position 1. Summing the two features gives 1×7 + 2×(−1) = 5, leaving only the two position indices. Row 0 sums to 6, so it is not yet a row of attention weights summing to 1.</figcaption>
</figure>

## Executable lab

### Execution environment and sources

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Checked on: 2026-10-01
- Component classification: `Stable core`
- Example ID: `n05_14_qkv`
- Code source: `labs/N05/n05_14_qkv.py`
- Test: `tests/N05/test_n05_14.py`
- Execution command: `.venv\Scripts\python.exe -m labs.N05.n05_14_qkv`

### Resource budget

The example uses sequence length 2, model dimension 2, 1 head, and 12 projection parameters.

### Actual code and execution results

<!-- N05_EXAMPLE: n05_14_qkv -->

### Checks

The tests compare Q, K, V, and score shapes and values with hand calculations.

## RoPE and projection order

The N05 reference computation projects Q and K before applying RoPE to feature pairs. V does not receive this rotation. When reading a public implementation, check the order of projection, head reshaping, and RoPE.

In the paths below, distinguish hook locations for tensors that pass through RoPE from those that do not.

<figure class="lesson-figure" markdown="1">

![Hidden state splits into query key projection and value projection with rotary transform only on query key before raw score and weights while value bypasses rotation to join later weighted sum](../../figures/assets/N05/N05-14-rope-hook-locations.svg)

<figcaption>H before projection, Q/K/V after projection, and Q/K after RoPE are different hook locations. On the left, rotation is applied only to Q/K before scores and weights. On the right, V bypasses that rotation and enters the later weighted sum.</figcaption>
</figure>

## Connection to model interpretation

Q, K, and V hooks answer different questions. Q and K concern score formation, while V concerns the content transmitted. Calling the residual state before projection Q or V misidentifies the intervention location.

A large raw score becomes a probability only after scaling, masking, and comparison with other key scores. A single score cannot determine its output contribution.

## Common misconceptions

### Misconception 1. A query is the current token and a key is a past token

Every position produces Q, K, and V. A causal mask only hides future keys; it does not assign projection roles to types of positions.

### Misconception 2. Values determine attention scores

In reference dot-product attention, scores are formed from Q and K. V supplies the values for the weighted sum after weights are formed.

### Misconception 3. Equal Q, K, and V shapes mean equal values

Separate weights define different linear maps.

## Exercises

### 1. Projection shape

For $H:(5,8)$ and $W_Q:(4,8)$, find the shape of Q.

<details><summary>Show solution</summary>It is $(5,4)$.</details>

### 2. Score shape

If Q and K both have shape `(5,4)`, find the score shape.

<details><summary>Show solution</summary>It is $(5,5)$.</details>

### 3. Score entry

Calculate the raw score for $q_i=(1,2)$ and $k_j=(3,-1)$.

<details><summary>Show solution</summary>It is $1\cdot3+2(-1)=1$.</details>

### 4. Row meaning

What does the second row of the score matrix collect?

<details><summary>Show solution</summary>It collects the scores given by the second query position to all key positions.</details>

### 5. Choosing a hook

Which tensor, Q or V, is the more direct intervention target for changing transmitted content?

<details><summary>Show solution</summary>V. Changing Q primarily changes the weight-selection path.</details>

### 6. Critiquing a claim

Evaluate the conclusion that the token with the largest QK score explains the output.

<details><summary>Show solution</summary>Without examining masking, softmax, V, and the output projection, no conclusion about output contribution follows.</details>

## Evidence and update boundaries

Projection and score definitions follow [Attention Is All You Need](https://arxiv.org/abs/1706.03762). A fused QKV implementation can calculate the same linear map in one kernel, but the mathematical roles remain separate.

## Lesson summary

- Q, K, and V are different projections of the same hidden state.
- Q times K transpose produces a position-by-position score matrix.
- A score row contains one query's evaluations of all keys.
- V supplies the content mixed by attention weights.
- Observing scores alone does not determine output contributions.

## Pass criteria

- Can you calculate Q, K, and V shapes?
- Can you calculate a score matrix by hand?
- Can you explain score rows and columns?
- Can you distinguish the QK path from the V path?
- Can you make claims appropriate to a hook's location?

## Next lesson

- [N05-15 Causal scaled dot-product attention](N05-15-causal-scaled-dot-product-attention.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Q, K, and V shapes and roles are distinguished.
- [x] Score values are checked.
- [x] Every exercise has a solution.
- [x] The strength of model interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and math rendering have been checked.
- [x] Executable code is not manually duplicated in Markdown.
- [x] Code sources, test paths, resource budgets, and check dates are recorded.
- [x] Shape, numerical, and gradient tests are provided.
