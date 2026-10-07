---
id: "N05-11"
title: "Tokens and tokenizers"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-10"
estimated_time: "120~150 minutes"
---

# N05-11. Tokens and tokenizers

## Why this lesson matters

A language model does not put strings directly into a matrix. A tokenizer splits a string into a token sequence and maps it to integer IDs in a vocabulary. Even the same sentence can have a different sequence length and token boundaries under different tokenizers.

This lesson converts `deep learning math` into six tokens using a fixed toy vocabulary. Instead of reproducing the training algorithm of an actual tokenizer, it clarifies segmentation, special tokens, unknown tokens, and the limits of decoding.

## Learning objectives

- Distinguish text, tokens, token IDs, and a vocabulary.
- Convert a string into a token sequence using fixed rules.
- Explain the roles of special tokens and unknown tokens.
- Explain why token counts differ from character and word counts.
- Avoid extending token-level analysis results into claims about strings as a whole.

## Prerequisite check

- Prerequisite lesson: [N05-10 Autograd, JVP, and VJP](N05-10-autograd-jvp-vjp.md)
- Check question: Can you distinguish a sequence position from a token ID?
- Check question: Can you map elements of a finite set to integer indices?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\mathcal V$ | `script V` | Tokenizer vocabulary | A finite set |
| $V$ | `V` | Vocabulary size | $V=\lvert\mathcal V\rvert$ |
| $t_i$ | `t sub i` | Token at position $i$ | $t_i\in\mathcal V$ |
| $a_i$ | `a sub i` | Integer ID of token $t_i$ | $\{0,\ldots,V-1\}$ |
| $T$ | `T` | Token sequence length | A positive integer |
| attention mask | `attention mask` | Indicator distinguishing actual tokens from padding positions | $\{0,1\}^T$ |

## Core concept 1. A tokenizer specifies rules between strings and IDs

Write an encoder as

\[
\operatorname{encode}(s)=(a_1,\ldots,a_T)
\]

$T$ is not the same as the string length. A frequent string fragment can become one token, while an unfamiliar string can be split into several tokens.

Decoding maps IDs to token strings and combines them according to the tokenizer's rules. Normalization and unknown mappings mean that a perfect inverse is not guaranteed for every tokenizer.

Segmentation, which splits a string into fragments, and lookup, which maps each fragment to an ID, are different stages. Token $t_i$ is a fragment registered in the vocabulary; $a_i$ is its row number, while $i$ is its position in the current sequence. If the same token appears twice, its ID is the same but its positions differ. Consistently renumbering vocabulary IDs does not change segmentation itself.

Finding a registered token from an ID may be possible, but recovering the input string is a separate problem. Mapping distinct unregistered fragments to the same `<unk>` already loses the information distinguishing them. Performing encoding and decoding in opposite directions therefore does not itself guarantee recovery of the original text.

In the diagram below, examine how two positions point to the same vocabulary entry.

<figure class="lesson-figure" markdown="1">

![Toy sequence BOS deep deep EOS contains token ID three at positions one and two while both positions look up the same vocabulary entry](../../figures/assets/N05/N05-11-repeat-token-position.svg)

<figcaption>The text's repeated-token distinction is illustrated with deep deep. The two deep tokens after BOS occupy positions 1 and 2 but both have vocabulary ID 3. A position is a location in a sequence; an ID is a row number to look up in a table.</figcaption>
</figure>

In the merging diagram below, identify where the information distinguishing unregistered strings is lost.

<figure class="lesson-figure" markdown="1">

![Ocean and another unregistered word merge to the same unknown token ID zero and decoding returns the unknown marker not either original word](../../figures/assets/N05/N05-11-unknown-merger.svg)

<figcaption>Both ocean and another unregistered word merge into the same unknown marker. ID 0 can be used to find the registered token &lt;unk&gt;, but not to determine which original word it was.</figcaption>
</figure>

## Core concept 2. Special tokens are vocabulary elements too

`<bos>` and `<eos>` mark sequence boundaries. `<unk>` represents a fragment absent from the vocabulary. The model receives these tokens as IDs and looks up their embedding rows, just as for other tokens.

Padding and attention masks are separate concepts. Even when a padding ID exists, the mask determines which positions to exclude from computation. Some decoder-only models do not define a padding token.

BOS and EOS occupy sequence positions separately from the original word count. Counting the length of an ID sequence includes these positions. Decoding that removes special tokens may omit their strings from the original text. Likewise, `<unk>` is not storage for the unregistered string; it marks that the fragment cannot be distinguished.

To make sequences of different lengths into a batch of the same length, padding IDs can be added after shorter sequences. This lesson's binary mask assigns 1 to actual positions and 0 to padding positions, representing length and valid positions separately. An ID value of 0 does not imply a mask value of 0. This mask indicates whether a token is actual; it is also distinct from the causal mask learned later, which specifies allowed past/future relationships.

In the positionwise arrays below, compare positions where the same ID 0 has different mask values.

<figure class="lesson-figure" markdown="1">

![Deep ocean padded to length six has IDs one three zero two zero zero while binary mask one one one one zero zero distinguishes the real unknown position from padded positions despite identical zero IDs](../../figures/assets/N05/N05-11-unknown-versus-padding.svg)

<figcaption>The toy's deep ocean is padded to length 6 using padding ID 0. The actual &lt;unk&gt; at position 2 also has ID 0, but its mask is 1. The final two padding positions have the same ID but mask 0. This mask does not specify past/future causal relationships.</figcaption>
</figure>

## Example. Encoding with a fixed vocabulary

Use the following toy vocabulary:

| token | ID |
|---|---:|
| `<unk>` | 0 |
| `<bos>` | 1 |
| `<eos>` | 2 |
| `deep` | 3 |
| `learn` | 4 |
| `ing` | 5 |
| `math` | 6 |

Applying a fixed rule that splits `learning` into `learn` and `ing` gives

\[
(\texttt{<bos>},\texttt{deep},\texttt{learn},\texttt{ing},\texttt{math},\texttt{<eos>})
\]

and IDs $(1,3,4,5,6,2)$. All six positions have attention mask 1.

In the diagram below, follow word boundaries and the correspondence between tokens, IDs, and positions.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three words deep learning math map to four word pieces with learning split to learn ing plus BOS and EOS producing six positions and vocabulary IDs one three four five six two](../../figures/assets/N05/N05-11-text-token-id.svg)

<figcaption>Follow the original words at the top down to the tokens in the middle. Splitting learning into two fragments and placing BOS/EOS at the ends gives length 6. The first number below each token is its vocabulary ID; the second is its 0-based position in the current sequence.</figcaption>
</figure>

In the decoding diagram below, separate special-token handling from fragment joining.

<figure class="lesson-figure" markdown="1">

![Toy decode drops BOS and EOS and joins adjacent learn and ing into learning while deep and math remain separate words](../../figures/assets/N05/N05-11-decode-word-join.svg)

<figcaption>This toy decoder removes BOS/EOS and attaches ing to the preceding word. The encoding example's learn and ing become learning, but this is this tokenizer's joining rule. It does not guarantee original-text recovery for every tokenizer.</figcaption>
</figure>

## Executable lab

### Execution environment and sources

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Checked on: 2026-10-01
- Component classification: `Stable core`; toy segmentation is an `Instructional reference`
- Example ID: `n05_11_toy_tokenizer`
- Code source: `labs/N05/n05_11_toy_tokenizer.py`
- Test: `tests/N05/test_n05_11.py`
- Execution command: `.venv\Scripts\python.exe -m labs.N05.n05_11_toy_tokenizer`

### Resource budget

The example uses vocabulary size 7, sequence length 6, and batch size 1. Model parameter and training step counts are both 0.

### Actual code and execution results

<!-- N05_EXAMPLE: n05_11_toy_tokenizer -->

### Checks

The tests check segmentation, IDs, decoding, and unknown tokens. The toy rules do not mimic BPE or unigram tokenizer training.

## Comparison with a public model

Pythia's public tokenizer configuration points to the GPT-NeoX tokenizer and sets `<|endoftext|>` as the BOS, EOS, and unknown token. This does not justify the toy vocabulary's choice of special tokens. Even the same roles use different IDs and strings across model families, so the model's tokenizer artifacts must be pinned together with the model.

## Connection to model interpretation

Comparing token activations requires saving the correspondence between text spans and token positions. Position 5 can represent different string fragments under two tokenizers.

Aggregating a token's attribution into attribution for an entire word requires an aggregation rule. Comparing expressions with different numbers of subwords by a simple sum or average changes the estimand.

## Common misconceptions

### Misconception 1. A token is a word

A token is an element of a tokenizer vocabulary. One word can split into several tokens, and spaces or punctuation can be part of a token.

### Misconception 2. Token ID magnitude has meaning

An ID is an index for looking up a vocabulary row. There is no semantic ordering in which ID 6 is greater in meaning than ID 3.

### Misconception 3. Decoding always recovers the original text

Normalization, unknown mappings, and special-token handling can lose information.

## Exercises

### 1. Length

State the number of words in the example sentence and the number of tokens including special tokens.

<details><summary>Show solution</summary>

There are 3 words and 6 tokens. `learning` splits into two fragments, and BOS and EOS are added.

</details>

### 2. Unknown token

What tokens result from encoding `deep ocean` with the toy tokenizer?

<details><summary>Show solution</summary>

They are `<bos>`, `deep`, `<unk>`, `<eos>`.

</details>

### 3. ID meaning

Can Euclidean distance between token IDs be used to evaluate semantic similarity?

<details><summary>Show solution</summary>

No. IDs are categorical indices. Semantic similarity should be defined using embeddings or other representations.

</details>

### 4. Mask

Two padding positions extend the sequence to length 8. What are the final two attention mask values?

<details><summary>Show solution</summary>

Under a convention that excludes padding, they are 0, 0. The preceding actual token positions have value 1.

</details>

### 5. Reproducibility

What problem arises if model weights are released without the tokenizer files?

<details><summary>Show solution</summary>

The text cannot be converted into the same ID sequence, so the meanings of input and output tokens cannot be reproduced.

</details>

### 6. Critiquing a claim

Evaluate the conclusion that two prompts have the same linguistic structure because they have the same token count.

<details><summary>Show solution</summary>

Token count is the result of tokenizer segmentation. It does not guarantee identical syntax or meaning.

</details>

## Lesson summary

- A tokenizer converts text into vocabulary tokens and an ID sequence.
- Token boundaries are not the same as word or character boundaries.
- Special tokens and unknown tokens also have vocabulary rows.
- Tokenizer artifacts are needed to reproduce model inputs.
- Token-level interpretation requires text-span correspondence.

## Pass criteria

- Can you distinguish text, tokens, and IDs?
- Can you encode and decode the toy example?
- Can you distinguish special tokens from masks?
- Can you explain why tokenizers change the unit of analysis?
- Can you critique excessive claims based on token counts?

## Next lesson

- [N05-12 Embedding and unembedding](N05-12-embedding-unembedding.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Text, tokens, IDs, and positions are distinguished.
- [x] The toy tokenizer's limitations are stated.
- [x] Every exercise has a solution.
- [x] The strength of model interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and math rendering have been checked.
- [x] Executable code is not manually duplicated in Markdown.
- [x] Code sources, test paths, resource budgets, and check dates are recorded.
- [x] Shape, numerical, and gradient tests are provided.
