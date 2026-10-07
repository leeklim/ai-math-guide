---
id: "N05-15"
title: "Causal scaled dot-product attention"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-14"
estimated_time: "120–150 minutes"
---

# N05-15. Causal scaled dot-product attention

## Why this lesson matters

A single QK score does not determine the attention output. The scores must be scaled by the head dimension, future positions excluded by a causal mask, the remaining scores normalized with softmax, and the values combined in a weighted sum. Knowing this order lets you distinguish an attention map from the actual output when interpreting the model.

## Learning objectives

- Calculate scaled dot-product attention in the correct order.
- Mark the score positions blocked by a causal mask.
- Check the row sums of the attention weights and the output shape.
- Distinguish claims about attention weights from claims about the value-weighted output.
- Identify code that applies the mask at the wrong stage.

## Prerequisite check

- Prerequisite lesson: [N05-14 Query, key, and value](N05-14-query-key-value.md)
- Check question: Can you explain which positions the rows and columns of QK transpose represent?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and conditions |
|---|---|---|---|
| $d_k$ | `d sub k` | Dimension of one key or query head | Positive integer |
| $S_{ij}$ | `S sub i j` | Scaled attention score | Scalar |
| $M_{ij}$ | `M sub i j` | Additive mask indicating whether a position is allowed | $0$ or $-\infty$ |
| $A_{ij}$ | `A sub i j` | Attention weight that query $i$ assigns to value $j$ | $[0,1]$ |
| $\mathbf O$ | `O` | Attention output obtained by a weighted sum of values | $\mathbb R^{T\times d_v}$ |

## Core concept 1. Scaling

The scores for one head are

\[
\mathbf S=\frac{\mathbf Q\mathbf K^\top}{\sqrt{d_k}}
\]

Scaling reduces the tendency for dot products to grow in magnitude as $d_k$ increases. The denominator uses the query-key dimension of this head, not the model dimension $d_{model}$.

Consider the simplifying assumption that all query and key components have mean 0 and variance 1 and are mutually independent. The product of one query component and one key component has mean 0, and the expected square of the product is the product of their expected squares, which is 1. Summing $d_k$ independent products gives a dot-product variance of $d_k$. Dividing the score by $\sqrt{d_k}$ divides its variance by the square of that quantity, $d_k$, leaving a variance of 1. This calculation uses a reference assumption to motivate scaling. It does not claim that learned components are exactly independent.

Without scaling, excessively large differences between scores within a row can cause softmax to put almost all its weight on one position. Where probabilities approach 0 or 1, the local derivative of softmax with respect to the scores becomes small. Adding the same large constant to every score does not change softmax, so absolute score magnitudes alone do not determine how concentrated the weights are. Scaling adjusts the scale of score differences; it does not make a head's weights uniform.

The figure below compares the weights for the same query's four scores before and after division by 4.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two bar charts compare softmax weights for one four-key score row before and after division by the square root of sixteen](../../figures/assets/N05/N05-15-score-scale-weights.svg)

<figcaption>This constructed calculation allows all four keys. With scores (0,2,4,6), the last key has a weight of about 0.865; after division by √16=4, its weight is about 0.455. Both row sums are 1, and scaling still does not make the four weights equal.</figcaption>
</figure>

With only two keys, the local rate of change with respect to the score difference decreases as a weight approaches either extreme.

<figure class="lesson-figure" markdown="1">

![The two-key softmax derivative p times one minus p peaks at one half and approaches zero near extreme attention weights](../../figures/assets/N05/N05-15-binary-softmax-sensitivity.svg)

<figcaption>If g is the difference between the two key scores, one weight is p=exp(g)/(1+exp(g)), with derivative p(1−p). The derivative reaches its maximum of 0.25 at p=0.5 and falls to 0.0099 at p=0.01 or 0.99. This figure shows only the two-key case, not the full Jacobian for multiple keys.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Five stages of causal scaled dot product attention with matrix shapes](../../figures/assets/N05/N05-15-attention-pipeline.svg)

<figcaption>Score calculation, scaling, blocking future positions, row-wise normalization, and value mixing are distinct operations performed in a fixed order.</figcaption>
</figure>

The first four stages handle $T\times T$ relationships between sequence positions. Only at the final stage are the attention weights multiplied by the values to produce a $T\times d_v$ output. The mask therefore changes the scores before softmax; it does not delete value vectors.

## Core concept 2. Causal mask

In a decoder that generates from left to right, query position $i$ cannot attend to future key positions $j>i$. Define the additive mask as

\[
M_{ij}=\begin{cases}
0,&j\le i,\\
-\infty,&j>i
\end{cases}
\]

The masked scores are $\widetilde{\mathbf S}=\mathbf S+\mathbf M$. Positions set to $-\infty$ before softmax receive probability 0.

Row $i$ is the query position that receives information, and column $j$ is the key position it refers to. The allowed region is therefore the lower triangle, including the main diagonal. Reversing this row-column convention can produce the opposite mask, blocking the past and allowing the future, so first check the implementation with a small $3\times3$ matrix.

Sending a forbidden score to $-\infty$ makes its exponential approach 0 in the limit. The softmax denominator then contains only exponentials of allowed scores, and forbidden positions receive weight 0. Setting a forbidden score to 0 does not block it, because its exponential is $e^0=1$.

Floating-point implementations sometimes use a very small finite value instead of $-\infty$. The exponential of a finite value is mathematically positive. To ensure that a position is blocked, check whether its exponential becomes numerically zero or whether the implementation excludes it separately. For a row with at least one allowed position, the reference mask must give forbidden positions weight 0 and allowed positions weights that sum to 1.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three token-labeled matrices showing raw scores causal masked scores and row-wise attention weights](../../figures/assets/N05/N05-15-causal-mask-matrices.svg)

<figcaption>Rows are queries and columns are keys. In the sat row, the future key down changes from an ordinary score of 0.4 to a masked score of −∞, then to an attention weight of 0.</figcaption>
</figure>

The purple border follows the row for query `sat` through the three stages. In this row, `The`, `cat`, and `sat` remain because they are past or current positions; `down` is in the future and is hatched. Forbidden positions are distinguished not just by color but also by hatching and the numerical labels $-\infty$ and 0. Including token names and the meanings of rows and columns makes it possible to see why the lower triangle is the allowed region.

## Core concept 3. Softmax and the weighted sum of values

\[
A_{ij}=\frac{\exp(\widetilde S_{ij})}
{\sum_{r=1}^{T}\exp(\widetilde S_{ir})},
\qquad
\mathbf O=\mathbf A\mathbf V
\]

Softmax is computed within each query row, so $\sum_j A_{ij}=1$. Output row $\mathbf o_i$ is a convex combination of the allowed value rows.

Keep row $i$ fixed and sum only over the key index. Each exponential is divided by the same sum for that row, making the weights sum to 1. Scores from other query rows do not enter this normalization. In causal self-attention without padding, each query can attend to its own position, leaving at least one positive term in the denominator. This formula cannot define a probability distribution for a row in which every position is forbidden, so an implementation that also uses padding must specify how it handles such rows.

Writing the output for query position $i$ directly gives

\[
\mathbf o_i
=
\sum_{j\le i} A_{ij}\mathbf v_j
\]

Even with the same attention weights, different $\mathbf v_j$ produce different outputs. Conversely, a large value vector does not enter this query's output if its position has weight 0. This is why the attention pattern and the attention output must be distinguished.

A convex combination is a weighted sum whose coefficients are nonnegative and sum to 1. If all value rows are identical, the output is that shared vector regardless of the weight distribution. In the matrix product, the key/value position axis is summed out, leaving the query position and value feature axes: $(T,T)(T,d_v)$ gives $(T,d_v)$. The weights collect the same feature coordinates from different source positions rather than transform the feature coordinates themselves.

Plotting the same weighted sum in a two-feature coordinate plane shows the output inside the triangle formed by the values.

<figure class="lesson-figure" markdown="1">

![A two-dimensional output at point zero five four comma zero six six lies inside the triangle formed by three value vectors with nonnegative normalized attention weights](../../figures/assets/N05/N05-15-convex-value-output.svg)

<figcaption>This constructed example assigns coefficients 0.40, 0.27, and 0.33 to v₁=(0,0), v₂=(2,0), and v₃=(0,2). The output is (0.54,0.66), inside the blue triangle. The axes are the two feature coordinates of the value vectors, not token positions.</figcaption>
</figure>

When all the values are identical, different attention rows can produce the same output.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two distinct normalized attention rows both yield the vector one comma one when all three shared value rows equal that vector](../../figures/assets/N05/N05-15-identical-value-collapse.svg)

<figcaption>All three values are fixed at (1,1). The coefficients in each of two different weight rows sum to 1, so both outputs are (1,1). In this case, observing identical outputs does not let you recover which attention row was used.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The attention row for sat multiplying allowed value vectors and summing to one output vector](../../figures/assets/N05/N05-15-value-mixing.svg)

<figcaption>The attention row for sat supplies the coefficients for three allowed value vectors. The value at the future position down contributes nothing to the output because its weight is 0.</figcaption>
</figure>

Here, $0.40,0.27,0.33$ are scalar coefficients multiplying different value vectors, not vector coordinates. Adding the three weighted vectors gives one output row for query `sat`. An attention map shows which positions are attended to and with what weights, but identifying the directions of information added to the output also requires examining the value vectors.

## Example

Using Q, K, and V from N05-14 gives scaled scores of approximately

\[
\mathbf S=
\begin{bmatrix}
0.7071&3.5355\\
3.5355&12.0208
\end{bmatrix}
\]

Masking the first query's future score gives the first attention row $(1,0)$. The second query can attend to both keys, giving approximately $(0.000206,0.999794)$. The output is therefore

\[
\mathbf O\approx
\begin{bmatrix}
2&1\\
5.9992&1.9998
\end{bmatrix}
\]

## Executable lab

### Environment and source files

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Date checked: 2026-10-01
- Component category: `Stable core`
- Example ID: `n05_15_causal_attention`
- Code source: `labs/N05/n05_15_causal_attention.py`
- Test: `tests/N05/test_n05_15.py`
- Run command: `.venv\Scripts\python.exe -m labs.N05.n05_15_causal_attention`

### Resource budget

The lab uses sequence length 2, head dimension 2, and one head. It does not download or train a model.

### Actual code and execution results

<!-- N05_EXAMPLE: n05_15_causal_attention -->

### Checks

The test checks $-\infty$ in the masked scores, the attention row sums, the first query's future probability, and the output values.

## Other mask representations in implementations

An implementation may pass a Boolean mask to `masked_fill`, add a very small finite value to the scores, or use a fused kernel with a causal option. Mask strings alone do not establish equivalence to the reference formula. Check the forbidden weights and row sums in rows with at least one allowed key. Depending on the dtype and score range, a finite substitute can leave a small positive weight at a forbidden position.

A padding mask excludes invalid tokens in a sequence, whereas a causal mask restricts temporal order. They can be applied together, but they are distinct concepts.

Apply both conditions to the keys that the same query can attend to, retaining only positions that satisfy both.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![For query sat the causal filter blocks a future down key and the padding filter blocks an earlier PAD key so their intersection allows only The and sat](../../figures/assets/N05/N05-15-causal-padding-intersection.svg)

<figcaption>This example fixes a single query row. For sat at i=2, PAD is excluded because it is invalid despite being in the past, and down is excluded because it is in the future despite being valid. The last row shows the intersection of the two allowed-position conditions. The figure does not cover the handling of rows that use PAD itself as the query.</figcaption>
</figure>

## Connection to model interpretability

Attention weight $A_{ij}$ is the coefficient with which query $i$ mixes in value position $j$. Its effect on the final logit, however, depends on the value vector, output projection, residual addition, and subsequent layers. A large attention weight is an observation about connection strength, not a complete causal explanation.

An intervention that changes the mask changes the information paths available to the model. This is a stronger manipulation than observing a particular attention weight, so report the original model's behavior separately from its behavior after the intervention.

## Common misconceptions

### Misconception 1. Multiplying by a mask after softmax gives the same result

Multiplying by 0 after softmax leaves the remaining weights with a sum other than 1. Without renormalization, this is a different operation.

Compare the two calculation paths side by side to see whether forbidden keys enter the normalization denominator.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Masking a forbidden key before softmax yields allowed weights one quarter and three quarters whereas zeroing its probability after softmax leaves total allowed mass point four](../../figures/assets/N05/N05-15-mask-order-mass.svg)

<figcaption>Setting the exponential for forbidden key 2 to 0 first gives a denominator of 1+3=4. Normalizing by the full sum 1+3+6=10 and then deleting the last weight leaves a total of 0.40. Dividing the two remaining values on the right by 0.40 again would reproduce the left-hand result, but without that additional operation the two paths differ.</figcaption>
</figure>

### Misconception 2. Scaling uses the sequence length

The denominator in the reference formula is $\sqrt{d_k}$.

### Misconception 3. An attention weight is a token's contribution

A weight is a coefficient before the values are mixed. A conclusion about contribution cannot omit the values and downstream paths.

## Exercises

### 1. Calculating the scale

For $d_k=16$, determine what the raw score is divided by.

<details><summary>Show solution</summary>It is divided by $\sqrt{16}=4$.</details>

### 2. Causal mask

For a sequence of length 3, identify the zero-based key index that query index 1 cannot attend to.

<details><summary>Show solution</summary>Index 2 is in the future. Indices 0 and 1 are allowed.</details>

### 3. First row

Determine the attention weights in the first query row of causal self-attention without padding.

<details><summary>Show solution</summary>Only the query's own position is allowed, so the first key receives weight 1 and all future keys receive weight 0.</details>

### 4. Output shape

For $A:(5,5)$ and $V:(5,8)$, determine the output shape.

<details><summary>Show solution</summary>$AV:(5,8)$.</details>

### 5. Diagnosing code

If a masked position has softmax probability 0.2, explain what should be checked first.

<details><summary>Show solution</summary>Check that the mask was applied to the scores before softmax and that its direction is correct.</details>

### 6. Evaluating a claim

Evaluate the claim that a token causes the prediction because a head assigns it weight 0.9.

<details><summary>Show solution</summary>An attention pattern has been observed, but the values, output projection, and downstream paths have not been examined, and no causal intervention has been performed. The observation does not justify a causal conclusion.</details>

## Sources and update boundaries

The scaled dot-product attention formula follows the definition in [Attention Is All You Need](https://arxiv.org/abs/1706.03762). Fused attention kernel APIs and mask representations can change, so consult the documentation for each implementation separately.

## Lesson summary

- Divide the QK scores by $\sqrt{d_k}$.
- A causal mask excludes future scores before softmax.
- Softmax turns each query row into a probability distribution.
- The attention output is the matrix product of the weights and values.
- Attention weights alone do not establish a causal contribution to the final prediction.

## Pass criteria

- Can you calculate scaled scores by hand?
- Can you mark the allowed region of a causal mask?
- Can you check attention row sums and the output shape?
- Can you identify an error in the order of mask application?
- Can you distinguish an attention pattern from a causal explanation?

## Next lesson

- [N05-16 MHA, MQA, and GQA](N05-16-mha-mqa-gqa.md)

## Author checklist

- [x] The learning objectives describe observable actions.
- [x] The order of scaling, masking, softmax, and the weighted sum of values is explained.
- [x] Every exercise has a solution.
- [x] Claim strengths in model interpretability are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No unannounced prerequisites are required.
- [x] Internal links and equation rendering have been checked.
- [x] Executable code has not been duplicated manually in Markdown.
- [x] Code sources, test paths, the resource budget, and the date checked are recorded.
- [x] Shape, numerical, and mask tests are provided.
