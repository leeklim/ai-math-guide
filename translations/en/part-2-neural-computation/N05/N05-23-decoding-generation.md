---
id: "N05-23"
title: "Decoding and generation"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-22"
estimated_time: "120–150 minutes"
---

# N05-23. Decoding and generation

## Why this lesson matters

The same model and prompt can produce different strings depending on the token-selection rule. Distinguish logits, probability distributions, candidate truncation, and actual samples to avoid confusing model changes with decoding randomness.

## Learning objectives

- Calculate greedy decoding and categorical sampling.
- Explain how temperature affects probability entropy.
- Construct top-k and top-p candidate sets and renormalize them.
- Record the seed, prompt, and decoding parameters as reproduction conditions.
- Avoid overinterpreting generation differences as evidence of changes inside the model.

## Prerequisite check

- Prerequisite lesson: [N05-22 Causal inference and the KV cache](N05-22-causal-inference-kv-cache.md)
- Check question: Can you explain which axis converts the last position's logits into vocabulary probabilities?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\tau$ | `temperature` | A positive quantity adjusting logit scale | $\tau>0$ |
| $\arg\max_i z_i$ | `arg max over i of z sub i` | Token index of the largest logit | discrete index |
| top-k | `top k` | Truncation retaining only the $k$ tokens with the largest logits | $1\le k\le V$ |
| top-p | `top p` | Truncation retaining the smallest leading set whose cumulative probability reaches the threshold | $0<p\le1$ |
| categorical sample | `a categorical sample` | An index drawn from normalized token probabilities | random variable |

## Core concept 1. Greedy decoding and sampling

Greedy decoding selects

\[
x_{t+1}=\operatorname*{argmax}_i z_i
\]

It is deterministic with the same logits and tie-breaking rule. Sampling draws a token according to

\[
x_{t+1}\sim\operatorname{Categorical}(\mathbf p)
\]

Even the token with the largest probability is not guaranteed to be selected every time.

Greedy decoding selects the largest next-token probability at the current prefix. It does not compare all subsequent prefixes and probability products, so it is not guaranteed to find the string with the highest full-sequence probability. With sampling, the selected token enters the next prefix and can also change the subsequent distribution. Even with the same weights, a different initial random draw can lead to a different generation path.

Laying out probabilities as interval lengths shows the difference between maximum selection and random sampling.

<figure class="lesson-figure" markdown="1">

![Four token probability intervals give greedy token zero while a possible uniform draw of zero point seven falls in token one](../../figures/assets/N05/N05-23-greedy-sample-interval.svg)

<figcaption>The example probabilities are laid out in order as interval lengths. Greedy decoding selects the widest interval, token 0. In contrast, a draw u=0.70 between 0 and 1 falls in token 1's interval. This draw is an illustration of the rule.</figcaption>
</figure>

Selecting the current step's maximum also differs from comparing the products along entire paths.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A two step probability tree starts with greedy branch A at zero point six but the largest complete path lies under branch B with probability zero point three nine six](../../figures/assets/N05/N05-23-local-global-choice.svg)

<figcaption>In this small distribution, A's initial probability of 0.60 exceeds B's 0.40. However, each path under A has probability 0.60×0.50=0.300, while the largest path under B has probability 0.40×0.99=0.396. The first greedy choice alone does not guarantee the highest probability for the full path.</figcaption>
</figure>

## Core concept 2. Temperature

\[
p_i(\tau)=
\frac{\exp(z_i/\tau)}{\sum_j\exp(z_j/\tau)}
\]

When $0<\tau<1$, logit differences are amplified, making the distribution more concentrated. When $\tau>1$, it becomes flatter. A positive temperature does not change the logit ordering, so the greedy argmax itself stays the same.

The probability ratio is $p_i(\tau)/p_j(\tau)=\exp((z_i-z_j)/\tau)$. Dividing a positive logit difference by a higher temperature brings the ratio closer to 1, reducing relative differences among candidates. For a fixed finite logit vector, softmax entropy does not decrease as temperature increases. If all logits are equal, the distribution is already uniform and does not change. As $\tau$ tends to infinity, the distribution approaches uniformity; as it approaches 0, the mass concentrates on the maximum-logit candidates. If multiple candidates tie for the maximum, the mass is split among them.

Compare three distributions with the same four logits, changing only the temperature.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The same four logits give concentrated or flatter probabilities at temperatures zero point two five one and four while retaining the same token ordering](../../figures/assets/N05/N05-23-temperature-distributions.svg)

<figcaption>Tokens 0 through 3 have the same ordering in all three cases. Their mass concentration differs, however, so the same top-p=0.75 retains one, two, or three candidates. The 0.00 above a small bar is rounded; it does not mean that the exact probability is 0.</figcaption>
</figure>

Summarizing the change in concentration with entropy gives the following curve.

<figure class="lesson-figure" markdown="1">

![Softmax entropy of a fixed four logit vector increases with positive temperature and approaches the uniform entropy log four](../../figures/assets/N05/N05-23-temperature-entropy.svg)

<figcaption>Entropy for the fixed logits=(2,1.5,0,−1) is shown in natural-log units. As temperature increases, it approaches log 4, the entropy of a uniform distribution over four candidates. The horizontal axis uses a logarithmic scale.</figcaption>
</figure>

## Core concept 3. Top-k and top-p

Top-k retains a fixed number of candidates. Top-p, or nucleus sampling, adds the original probabilities in descending order and retains the smallest set whose cumulative mass is at least $p$. Both schemes set excluded logits to $-\infty$, then renormalize the remaining candidates for sampling.

For the retained candidate set $\mathcal C$, the new probability inside the set is the original $p_i$ divided by $\sum_{j\in\mathcal C}p_j$; outside the set, it is 0. The two candidates in the example have an original mass of approximately 0.8966. Dividing by this denominator makes the sum 1. The top-p threshold $p$ is a lower bound on the original mass to retain, not the sum of the final sampling probabilities. The last token that crosses the threshold is included, so the retained mass can exceed it.

A positive temperature preserves the ordering and hence the top-k candidates, but changes the probability masses. Thus, when top-p is applied after temperature, determine the cumulative set from the probabilities at that temperature.

The first point where the cumulative-mass curve crosses the threshold determines how many candidates to retain.

<figure class="lesson-figure" markdown="1">

![Original cumulative probability first crosses the top p threshold zero point seven five after retaining the first two tokens](../../figures/assets/N05/N05-23-nucleus-cumulative.svg)

<figcaption>The first token's mass of approximately 0.558 is below the threshold of 0.75. Adding the second token gives approximately 0.897 and crosses it for the first time, so both tokens are retained. The second token that crosses the threshold is not discarded.</figcaption>
</figure>

## Example

For logits $(2,1.5,0,-1)$, softmax gives approximately

\[
(0.5581,0.3385,0.0755,0.0278)
\]

The greedy token has index 0. Top-k with $k=2$ retains only the first two tokens. Top-p with $p=0.75$ also retains the second token because the first token's mass alone is insufficient. After renormalization, both distributions are approximately $(0.6225,0.3775,0,0)$.

Compare the retained mass and renormalized probabilities in two rows.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Keeping the first two of four candidates and dividing their probabilities by the retained mass changes them to zero point six two two five and zero point three seven seven five](../../figures/assets/N05/N05-23-candidate-renormalization.svg)

<figcaption>Only the original mass of tokens 0 and 1, approximately 0.8966, is retained. Dividing each probability by that mass gives approximately 0.6225 and 0.3775, summing to 1. Excluded tokens 2 and 3 have final sampling probabilities of 0.</figcaption>
</figure>

## Executable lab

### Environment and source

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Verification date: 2026-10-01
- Component category: `Stable core` and decoding-specific policy
- Example ID: `n05_23_decoding`
- Source code: `labs/N05/n05_23_decoding.py`
- Tests: `tests/N05/test_n05_23.py`
- Run command: `.venv\Scripts\python.exe -m labs.N05.n05_23_decoding`

### Resource budget

The lab uses only one logit vector over a vocabulary of 4. It performs no model forward pass or repeated generation.

### Actual code and execution results

<!-- N05_EXAMPLE: n05_23_decoding -->

### Checks

The tests check entropy ordering across temperatures, candidate counts and renormalization for top-k and top-p, and greedy and seeded sampling results.

## State during repeated generation

An actual generation loop adds the selected token to the input and updates the KV cache until the stopping condition is met. Reproduction requires the model revision, tokenizer, prompt bytes, chat template, seed, temperature, top-k, top-p, maximum token count, and stopping rule.

Substituting `temperature=0` directly into the softmax equation divides by 0. Whether a library accepts this expression as an alias for greedy decoding is an API rule. Mathematically, treat greedy decoding and positive-temperature sampling separately.

## Connection to model interpretability

A difference between two individual sampled completions is not evidence that the model probabilities changed. Random draws can differ even with the same logits. To compare before and after an intervention, fix the same prompt, seed, and decoding settings where possible, and also measure changes in logits or probabilities.

Even if the greedy outputs match, the logit margin relative to an alternative token can differ. Matching strings alone do not establish equivalence at the internal or distribution level.

## Common misconceptions

### Misconception 1. A model with higher temperature has less knowledge

Temperature is usually a setting transforming logits during decoding. It can be changed while keeping the same model weights.

### Misconception 2. Top-p always retains the same number of candidates

Nucleus size varies with the distribution's concentration.

### Misconception 3. The same seed guarantees the same string in every environment

The model, tokenizer, kernel, dtype, sampling implementation, and execution order must also match. The seed is one of the required conditions.

## Exercises

### 1. Greedy decoding

Calculate the greedy index for logits $(0.2,1.1,0.7)$.

<details><summary>Show solution</summary>It is index 1, whose logit 1.1 is the largest.</details>

### 2. Temperature and ordering

Determine whether dividing by a positive temperature changes the logit ordering.

<details><summary>Show solution</summary>It does not. Division by the same positive number preserves the argmax.</details>

### 3. Top-k

For vocabulary size 10 and $k=3$, determine the maximum number of tokens with positive probability immediately before sampling.

<details><summary>Show solution</summary>It is three. Check the implementation details for how equal logits at the boundary are handled.</details>

### 4. Top-p

Determine the smallest retained candidate set when the descending probabilities are $(0.6,0.25,0.1,0.05)$ and $p=0.8$.

<details><summary>Show solution</summary>It contains the first and second tokens. Their cumulative mass is $0.6+0.25=0.85$, reaching at least 0.8 for the first time.</details>

### 5. Reproduction records

List at least three items besides the seed to record when comparing sampling results.

<details><summary>Show solution</summary>Examples include the model revision, tokenizer and chat template, prompt, temperature, top-k and top-p, and stopping rule.</details>

### 6. Interpreting a result

Does one sampled answer changing after an intervention establish the intervention's causal effect?

<details><summary>Show solution</summary>No. Distinguishing it from sampling variation requires paired seeds, repeated samples or a distribution-level metric, and appropriate controls.</details>

## Sources and update boundaries

The definition and motivation of nucleus sampling are based on [The Curious Case of Neural Text Degeneration](https://arxiv.org/abs/1904.09751). Filter order, tie handling, and random generators in sampling APIs can differ with framework versions.

## Lesson summary

- Greedy decoding selects the maximum-logit index, while sampling draws a token from probabilities.
- Temperature changes the distribution's concentration.
- Top-k truncates by candidate count, and top-p by cumulative probability mass.
- Probabilities are renormalized after candidate truncation.
- Output comparisons require controlling both model conditions and decoding randomness.

## Pass criteria

- Can you calculate greedy decoding and sampling?
- Can you explain the relationship between temperature and entropy?
- Can you construct top-k and top-p candidate sets?
- Can you list generation reproduction conditions?
- Can you interpret output differences at the appropriate evidence level?

## Next lesson

- [N05-24 Observational status of chain-of-thought](N05-24-chain-of-thought-observation-status.md)

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] Greedy decoding, temperature, top-k, and top-p are calculated.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretability claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Knowledge beyond the prerequisites is not required without explanation.
- [x] Internal links and equation rendering are checked.
- [x] Executable code is not manually duplicated in Markdown.
- [x] Source-code and test paths, resource budgets, and the verification date are recorded.
- [x] Probability, entropy, and sampling tests are provided.
