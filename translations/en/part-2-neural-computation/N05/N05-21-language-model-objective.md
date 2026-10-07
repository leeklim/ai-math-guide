---
id: "N05-21"
title: "The language model objective"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-20"
estimated_time: "120–150 minutes"
---

# N05-21. The language model objective

## Why this lesson matters

A decoder may produce vocabulary logits at every position, but a learning problem also requires specifying which labels to compare them with. Causal language modeling predicts the next token from the tokens seen so far. During training, the ground-truth prefix is supplied all at once, allowing losses at multiple positions to be computed in parallel.

## Learning objectives

- Factor a sequence probability into a product of conditional probabilities.
- Mark the shift between input logits and next-token labels.
- Calculate tokenwise negative log-likelihood and mean loss.
- Distinguish teacher forcing from autoregressive generation.
- Avoid equating a decrease in loss with an explanation of internal mechanisms.

## Prerequisite check

- Prerequisite lesson: [N05-20 Decoder blocks and architecture diffs](N05-20-decoder-block-architecture-diff.md)
- Check question: For logits of shape `(B,T,V)`, which axis produces the vocabulary distribution at one position?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $x_{<t}$ | `x before t` | Token prefix before position $t$ | Token sequence |
| $p_\theta(x_t\mid x_{<t})$ | `p theta of x t given x before t` | Model probability of the next token given a prefix | $[0,1]$ |
| $\ell_t$ | `loss at position t` | Negative log-likelihood comparing the logit at position $t$ with the next-token target | Nonnegative scalar |
| teacher forcing | `teacher forcing` | Training procedure using the ground-truth prefix as model input | Training procedure |
| label shift | `label shift` | Alignment of the logit at position $t$ with the label for token $t+1$ | One-token offset |

## Core concept 1. Autoregressive factorization

The model probability of token sequence $x_1,\ldots,x_T$ is factored by the chain rule:

\[
p_\theta(x_1,\ldots,x_T)
=\prod_{t=1}^{T}p_\theta(x_t\mid x_{<t})
\]

The handling of a start token or the first token can vary with the dataset convention.

In the first factor, $x_{<1}$ is an empty prefix; a separate start token can also be used as a condition. This product does not assume that the tokens are independent. It factors the joint probability by conditioning on all previously observed tokens. Taking a logarithm converts the product into a sum of conditional log probabilities, so negative log-likelihood training can sum the losses at individual prediction positions.

In the small token tree below, the same next token receives different probabilities depending on the prefix.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A token tree conditioned on prefix A multiplies continuation probabilities and shows different probabilities for C after AB and AD](../../figures/assets/N05/N05-21-conditional-token-paths.svg)

<figcaption>This conditional example assumes that A has already been given. C has probability 0.25 after AB and 0.90 after AD, so independence is not assumed. The continuation probability of path ABC is 0.5×0.25=0.125, and the four leaf probabilities sum to 1.</figcaption>
</figure>

## Core concept 2. Shifted cross entropy

For input `[1, 4, 2, 7]`, compare the logits at the first three positions with labels `[4, 2, 7]`. The logit at the last input position is excluded from this short example's loss because no next label outside the sequence has been supplied.

For each target,

\[
\ell_t=-\log p_\theta(x_{t+1}\mid x_{\le t})
\]

and the mean loss over $N$ valid tokens is

\[
\mathcal L=\frac1N\sum_{t\in\mathcal I}\ell_t
\]

Padding or ignored labels are excluded from $\mathcal I$.

The preceding section indexed probabilities by the position $t$ of the token being predicted; this section indexes losses by the position $t$ producing the logit. The tokens $x_{\le t}$ read through the current position condition the next token $x_{t+1}$, requiring a one-position shift. Using an input ID as the target at that same position would create a different learning problem: predicting a token already seen in the input.

Follow the arrows from logit rows to the next labels to check the one-position offset.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The first three logits of a four-token input align with the next three token IDs while the last logit has no supplied next label](../../figures/assets/N05/N05-21-next-token-shift.svg)

<figcaption>Positions in this figure start at 0, as in the code. logits[0], logits[1], and logits[2] are compared with labels 4, 2, and 7, respectively. The last logit is excluded from the loss because no next label outside this input is provided.</figcaption>
</figure>

The set $\mathcal I$ contains valid prediction positions with labels, and $N=|\mathcal I|>0$. Excluding a position's loss does not automatically delete an axis from the input tensor. Averaging over all valid tokens in a batch gives longer sequences more terms in the average. This has different weighting from averaging each sequence's mean with equal weight.

Even for the same loss values, the result depends on the unit being averaged.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three valid losses across two padded sequences yield a token mean of two but an equally weighted sequence mean of two point five](../../figures/assets/N05/N05-21-valid-token-reduction.svg)

<figcaption>In this separate example, sequence A has valid losses 1 and 1, while B has valid loss 4. The mean over all valid tokens is 2, but the equally weighted mean of the sequence means is 2.5. Excluding ignored positions from the loss leaves all three positions in each tensor.</figcaption>
</figure>

## Core concept 3. Teacher forcing

During training, each position receives preceding ground-truth tokens. The causal mask prevents access to future labels, while forward computation for all positions can proceed in parallel.

During generation, no ground-truth next token is available. A token selected by the model is appended to the sequence, and the next distribution is computed again. Distinguish the training input distribution from the model-generated prefixes encountered during generation; they can differ.

The training input contains later ground-truth tokens, but the causal mask prevents them from entering the computation of the logit at position $t$. Computing later positions simultaneously differs from allowing an earlier position to use later information. Because ground-truth prefixes are known in advance, multiple rows can be computed together during training. During generation, a newly selected token becomes the input to the next row.

The figure below distinguishes known ground-truth prefixes from prefixes formed by previously selected tokens.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Ground-truth prefixes stay fixed for parallel teacher-forcing rows while illustrative generated choices are appended to later input prefixes](../../figures/assets/N05/N05-21-teacher-forcing-generation.svg)

<figcaption>The left side uses prefixes of the ground-truth sequence [1,4,2,7]; the rows can be computed together under a causal mask. The choices 5 and 9 on the right are illustrative, showing that the next prefix is known only after a new token is selected. They are not actual model-generation results.</figcaption>
</figure>

## Example

If the correct token probabilities at two positions are 0.5 and 0.25, the mean negative log-likelihood is

\[
-\frac12(\log 0.5+\log 0.25)
=-\log\sqrt{0.125}
\approx1.0397
\]

A correct token with lower probability contributes a larger loss.

## Hands-on lab

### Environment and source files

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Checked on: 2026-10-01
- Component classification: `Stable core`
- Shared implementation: `labs/N05/tiny_decoder.py`
- Example ID: `n05_21_language_model_objective`
- Code source: `labs/N05/n05_21_language_model_objective.py`
- Tests: `tests/N05/test_n05_21.py`
- Run command: `.venv\Scripts\python.exe -m labs.N05.n05_21_language_model_objective`

### Resource budget

The lab runs one forward and backward pass on a model with batch size 1, sequence length 4, dimension 4, vocabulary size 16, and 300 parameters.

### Actual code and execution results

<!-- N05_EXAMPLE: n05_21_language_model_objective -->

### Checks

The tests check label shifting, prediction-logit shapes, mean cross entropy, and whether embedding gradients are finite.

## Reduction and comparison conditions

The `sum` and `mean` losses have different gradient scales. Even when using a mean, record the denominator if sequences have different numbers of valid tokens. Perplexity is usually the exponential of mean token NLL, so values from different tokenizers or evaluation corpora should not be compared directly.

## Connection to model interpretability

A single token's loss or a logit difference makes the analysis target explicit. For gradient attribution, choosing a mean loss over the entire sequence versus a logit at a particular position changes the starting cotangent.

A decrease in loss is evidence that the model has optimized the objective better. Determining which circuits or representations it used requires additional checks of activations, interventions, and controls.

## Common misconceptions

### Misconception 1. An input ID is used as the label at the same position

The causal next-token objective aligns the current position's logit with the next token's label.

### Misconception 2. Teacher forcing lets attention see future tokens

The ground-truth sequence is supplied as input, but the causal mask blocks future positions at each position.

### Misconception 3. Low cross entropy guarantees good generated sentences

Mean token likelihood and the usefulness or accuracy of a particular generation are different evaluation targets.

## Exercises

### 1. Label shift

Determine the labels used in the loss for input IDs `[3, 8, 5]`.

<details><summary>Show solution</summary>The labels are `[8, 5]`, aligned with the logits at the first two positions.</details>

### 2. Logit-slice shape

Determine the prediction-logit shape after excluding the last position from logits of shape `(2,6,100)`.

<details><summary>Show solution</summary>The shape is `(2,5,100)`.</details>

### 3. Token loss

Calculate the negative log-likelihood when the correct token has probability 0.1.

<details><summary>Show solution</summary>It is $-\log 0.1\approx2.3026$.</details>

### 4. Mean loss

Calculate the mean of valid token losses 1, 2, and 3.

<details><summary>Show solution</summary>The mean is $(1+2+3)/3=2$.</details>

### 5. Teacher forcing

Determine whether the training input prefix at position 3 contains a token that the model previously predicted incorrectly.

<details><summary>Show solution</summary>Standard teacher forcing does not use that prediction. It uses the dataset's ground-truth prefix.</details>

### 6. Interpretability target

To analyze evidence for a particular correct token, determine which target is more direct: the sequence mean loss or the logit at that position.

<details><summary>Show solution</summary>The correct token's logit at that position, or a correct-minus-alternative logit difference, is more direct. State the question answered by the selected target.</details>

## Sources and update boundaries

Causal factorization and decoder masking were checked against [Attention Is All You Need](https://arxiv.org/abs/1706.03762), and public autoregressive model architectures against [GPT-NeoX-20B](https://arxiv.org/abs/2204.06745). Padding labels, reductions, and vocabulary conventions are implementation details that vary by dataset and framework.

## Lesson summary

- A causal LM expresses sequence probability as a product of prefix-conditioned next-token probabilities.
- Logits and labels are shifted by one token.
- Token NLLs are summed or averaged over an explicitly specified valid set.
- Teacher forcing uses ground-truth prefixes while retaining the causal mask.
- Record the loss target and interpretability target explicitly.

## Pass criteria

- Can you write the autoregressive factorization?
- Can you shift logits and labels correctly?
- Can you calculate token NLLs and mean loss?
- Can you distinguish training prefixes from generation prefixes?
- Can you choose a scalar target suited to the analysis question?

## Next lesson

- [N05-22 Causal inference and the KV cache](N05-22-causal-inference-kv-cache.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Factorization, label shifting, and teacher forcing are connected.
- [x] Every exercise has a solution.
- [x] Model interpretability claims are distinguished by strength of evidence.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and mathematical rendering have been checked.
- [x] Executable code has not been manually duplicated in Markdown.
- [x] Code sources, test paths, resource budgets, and the check date are recorded.
- [x] Shift, loss, and gradient tests are provided.
