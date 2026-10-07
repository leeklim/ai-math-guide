---
id: "N05-12"
title: "Embedding and unembedding"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-11"
estimated_time: "120~150 minutes"
---

# N05-12. Embedding and unembedding

## Why this lesson matters

A token ID is a categorical index. An embedding table maps each ID to a continuous vector, and unembedding maps the final hidden vector to vocabulary logits. Knowing the rows and columns of these two matrices precisely connects token activations with logits.

## Learning objectives

- Express a token ID lookup as row selection from an embedding matrix.
- Check embedding and unembedding shapes.
- Calculate vocabulary logits from a hidden state.
- Distinguish weight tying from untied weights.
- Explain gradient sparsity for selected embedding rows.

## Prerequisite check

- Prerequisite lesson: [N05-11 Tokens and tokenizers](N05-11-token-tokenizer.md)
- Check question: Can you select a matrix row using an integer index?
- Check question: Can you determine the result shape of $(T,d)(d,V)$?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\mathbf E$ | `E` | Embedding matrix | $\mathbb R^{V\times d}$ |
| $a_t$ | `a sub t` | Token ID at position $t$ | $\{0,\ldots,V-1\}$ |
| $\mathbf h_t$ | `h sub t` | Token embedding or hidden state | $\mathbb R^d$ |
| $\mathbf U$ | `U` | Unembedding matrix | $\mathbb R^{V\times d}$ |
| $\mathbf z_t$ | `z sub t` | Vocabulary logit vector | $\mathbb R^V$ |
| weight tying | `weight tying` | The choice to share parameters between $\mathbf U$ and $\mathbf E$ | An architecture option |

## Core concept 1. Embedding is a row lookup

The embedding for token ID $a_t$ is

\[
\mathbf h_t=\mathbf E[a_t]
\]

If the sequence ID tensor has shape $(B,T)$, the embedding output has shape $(B,T,d)$. The numeric magnitude of an ID does not indicate vector magnitude or semantic order.

Let a length-$V$ one-hot vector $\mathbf e_{a_t}$ have 1 only at ID $a_t$. In column-vector notation, the lookup equals $\mathbf h_t=\mathbf E^\top\mathbf e_{a_t}$. In practice, the corresponding row can be selected without constructing the entire one-hot vector. This selects a category rather than multiplying a weight by the numeric ID. The same ID receives the same row at this stage; contextual changes arise in subsequent computation.

Rows not selected along the lookup path do not enter the output and have direct gradient 0. If the same ID appears at several positions, the gradients returning from those positions are added at one row. Activations exist separately at each position, but the training parameter is one shared row.

In the diagram below, locate where gradients from different hidden positions combine at one lookup row.

<figure class="lesson-figure" markdown="1">

![Two separate sequence positions with ID two look up the same embedding row and their separate gradient vectors accumulate into that single parameter row while unselected lookup rows receive zero](../../figures/assets/N05/N05-12-repeat-row-gradients.svg)

<figcaption>Suppose ID 2 appears at two positions. Each position has a separate hidden activation, but the lookup parameter is just row 2 of E. The two returning gradients combine at that row; the other rows have direct lookup contribution 0.</figcaption>
</figure>

## Core concept 2. Unembedding maps hidden states to logits

\[
\mathbf z_t=\mathbf U\mathbf h_t+\mathbf b
\]

In row-batch notation, this is $\mathbf H\mathbf U^\top+\mathbf b$. The output's final axis has length equal to vocabulary size $V$. Softmax is applied afterward.

With $\mathbf b\in\mathbb R^V$, the score for token candidate $k$ is $z_{tk}=\sum_{j=1}^d U_{kj}h_{tj}+b_k$. Summing over hidden component $j$ leaves vocabulary candidate $k$. While embedding selects one row for one ID, unembedding compares the same hidden state with every candidate row to produce $V$ scores. These scores are neither probabilities nor recovered original tokens.

The hidden state after embedding can change through multiple layers, and unembedding can be learned separately. Opposite prefixes in their names do not mean that the two computations are inverses. Even with $\mathbf U=\mathbf E$, composing the maps directly without bias or intermediate layers gives $\mathbf E\mathbf E^\top\mathbf e_{a_t}$. This collects dot products between rows; it is not generally an identity map returning the original one-hot vector.

In the composition path below, use the actual rows to see why applying the same table twice does not recover the one-hot vector.

<figure class="lesson-figure" markdown="1">

![One-hot zero selects embedding one zero zero and shared unembedding returns dot products one zero zero one because vocabulary row three one one zero also has dot product one](../../figures/assets/N05/N05-12-shared-not-inverse.svg)

<figcaption>This tying comparison also uses the lab's E as U, omitting bias and intermediate layers. Both rows 0 and 3 of E have first component 1, so hidden (1, 0, 0) gives both candidates logit 1. It does not return the original one-hot vector (1, 0, 0, 0).</figcaption>
</figure>

## Core concept 3. Tying is a choice to share parameters

Weight tying usually shares the unembedding weight with the embedding weight. Equal shapes do not automatically share parameters. Pythia's public configuration uses `tie_word_embeddings: false`, so the two weights are distinguished.

Initializing two independent parameters with the same numbers differs from using one parameter in two places. Independent parameters can diverge under different gradients. With tying, gradients from input lookup and output-score computation accumulate in the same table. Excluding bias, the weight element count decreases from $2Vd$ for untied weights to $Vd$ for tied weights.

A token absent from the input batch is still an output vocabulary candidate. Its lookup gradient can therefore be 0 while its unembedding-path gradient remains in a tied table. The statement that direct gradients collect only at selected rows is limited to the lookup path. Do not confuse this with the shared table's total gradient or optimizer update.

Compare the ownership of parameters accumulating gradients in the two paths below.

<figure class="lesson-figure" markdown="1">

![Untied embedding and output tables collect separate gradients whereas a tied table collects both lookup and all-candidate readout gradients so an unused lookup row can receive output contribution](../../figures/assets/N05/N05-12-tied-gradient-paths.svg)

<figcaption>The upper untied paths use distinct parameters despite matching shapes. In the lower paths, gradients from both accumulate in one table. A row unused at the input is still an output candidate, so its shared-table gradient need not be 0.</figcaption>
</figure>

## Example

Selecting IDs $(0,2)$ from a table with $V=4$, $d=3$ gives embedding rows 0 and 2 as hidden states. Applying the lab's unembedding gives logits

\[
\begin{bmatrix}1&0&0&-1\\0&0&1&0.5\end{bmatrix}
\]

The shape is $(2,4)$. This lab does not share embedding and unembedding or use the table along any other path. Backpropagating the target loss therefore gives gradient 0 for the unselected embedding rows 1 and 3.

In the lookup diagram below, connect the table rows selected by two IDs to their sequence positions.

<figure class="lesson-figure" markdown="1">

![Embedding table rows zero one zero zero and row two zero zero one are selected by sequence IDs zero two and placed in sequence order as two hidden rows](../../figures/assets/N05/N05-12-row-lookup.svg)

<figcaption>Rows selected by IDs (0, 2) are orange. The first hidden position below is row 0 of E; the second is row 2. The three row components were selected together, not multiplied by ID 2.</figcaption>
</figure>

In the following readout diagram, examine how the same hidden state scores every vocabulary candidate.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Hidden one zero zero is dotted with each of four unembedding candidate rows yielding logits one zero zero minus one with zero bias](../../figures/assets/N05/N05-12-all-candidate-readout.svg)

<figcaption>The lab's first hidden state (1, 0, 0) is supplied to every U row in the same way. Each row is one vocabulary candidate; summing three feature positions gives one logit. These four numbers are not probabilities.</figcaption>
</figure>

## Executable lab

### Execution environment and sources

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Checked on: 2026-10-01
- Component classification: `Stable core`; tying is an architecture option
- Example ID: `n05_12_embedding_unembedding`
- Code source: `labs/N05/n05_12_embedding_unembedding.py`
- Test: `tests/N05/test_n05_12.py`
- Execution command: `.venv\Scripts\python.exe -m labs.N05.n05_12_embedding_unembedding`

### Resource budget

The example uses vocabulary size 4, sequence length 2, model dimension 3, and 28 parameters. There is no training update.

### Actual code and execution results

<!-- N05_EXAMPLE: n05_12_embedding_unembedding -->

### Checks

The tests check lookup rows, logit shapes, probability sums, and embedding gradient rows.

## Connection to model interpretation

Embedding geometry describes vector relationships in the input table. Claiming that it is the same space as representations later in the residual stream requires checking the bases and transformations.

A logit lens applies unembedding to an intermediate hidden state. This does not mean the original model directly predicted tokens at that point. It is a diagnostic omitting normalization and subsequent layers.

In the branching diagram below, identify the original forward path omitted by the diagnostic.

<figure class="lesson-figure" markdown="1">

![An intermediate hidden state branches through later layers and final readout for the real forward result while a separate diagnostic branch applies unembedding early and bypasses later computation](../../figures/assets/N05/N05-12-logit-lens-branch.svg)

<figcaption>The left path is the original route from an intermediate hidden state through later layers to final readout. The right path is a diagnostic branch applying U directly at the same point. Early logits omitting later layers and normalization do not mean that the original forward computation has finished deciding.</figcaption>
</figure>

## Common misconceptions

### Misconception 1. Nearby embedding IDs have nearby meanings

An ID is a row index. Vector distance is calculated between embedding rows.

### Misconception 2. Unembedding is the inverse of embedding

Unembedding is a learned linear map sending hidden states to logits. It is not a general matrix inverse.

### Misconception 3. Equal shapes mean shared weights

The implementation must share the parameter object, or the configuration must specify tying.

## Exercises

### 1. Shape

For $V=100$, $d=16$, and ID batch shape `(2,5)`, find the embedding output shape.

<details><summary>Show solution</summary>

It is `(2,5,16)`.

</details>

### 2. Parameter count

Find the parameter count without sharing embedding and unembedding and without bias.

<details><summary>Show solution</summary>

There are $2Vd=3200$ parameters.

</details>

### 3. Logit shape

For hidden shape `(2,5,16)` and $U\in\mathbb R^{100\times16}$, find the logit shape.

<details><summary>Show solution</summary>

It is `(2,5,100)`.

</details>

### 4. Gradient row

ID 7 never appears in a batch. What is embedding row 7's direct lookup gradient?

<details><summary>Show solution</summary>

It is 0 along that batch's lookup path. Tying or other uses can produce separate contributions.

</details>

### 5. Tying

State one advantage of weight tying and one caution for interpretation.

<details><summary>Show solution</summary>

It reduces the parameter count. Changes in input embeddings and the output classifier are coupled through the same parameter, making their roles difficult to interpret separately.

</details>

### 6. Critiquing a claim

Evaluate the conclusion that the model has already decided its answer because the top token from an intermediate logit lens is correct.

<details><summary>Show solution</summary>

This is the result of a diagnostic projection. Later layers can change representations and final logits, so it does not guarantee that the decision is complete.

</details>

## Lesson summary

- Embedding selects a matrix row using a token ID.
- Unembedding sends a hidden state to vocabulary logits.
- Weight tying is the choice to share parameters between the two maps.
- Lookup gradients collect directly at used rows.
- A logit lens is a diagnostic, not the same as an intermediate output of the original forward computation.

## Pass criteria

- Can you state embedding and unembedding shapes?
- Can you calculate lookups and logits with small tables?
- Can you check whether weights are tied in a configuration?
- Can you explain which rows accumulate gradients?
- Can you explain the limits of logit-lens claims?

## Next lesson

- [N05-13 Position information and RoPE](N05-13-position-information-rope.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Embedding and unembedding shapes are checked.
- [x] Tying is distinguished from an inverse.
- [x] Every exercise has a solution.
- [x] The strength of model interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and math rendering have been checked.
- [x] Executable code is not manually duplicated in Markdown.
- [x] Code sources, test paths, resource budgets, and check dates are recorded.
- [x] Shape, numerical, and gradient tests are provided.
