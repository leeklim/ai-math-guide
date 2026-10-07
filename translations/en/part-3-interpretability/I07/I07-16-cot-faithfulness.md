---
id: "I07-16"
title: "Evaluating CoT faithfulness"
part: 3
stage: "I07"
status: "complete"
prerequisites: ["I07-15", "N05-24"]
estimated_time: "120–150 minutes"
---

# I07-16. Evaluating CoT faithfulness

## Why this lesson matters

Chain-of-thought (CoT) is a language string output by a model. A correct answer with a plausible reason does not ensure that this string faithfully reports the internal computation that produced the answer. Assess faithfulness through observable tests, such as how an answer changes when its rationale is altered or removed, or whether the explanation reflects a hidden bias, rather than through sentence quality alone.

## Learning objectives

- Distinguish plausibility from faithfulness.
- Define a metric for answer dependence on rationale interventions.
- Explain the scope of truncation, paraphrase, and error-insertion tests.
- Avoid treating CoT and internal activation evidence as the same thing.

## Prerequisite check

- Prerequisite lessons: [I07-15 Controls and statistical validation](I07-15-controls-statistical-validation.md), [N05-24 The observational status of chain-of-thought](../../part-2-neural-computation/N05/N05-24-chain-of-thought-observation-status.md)
- Check question: Why is an output rationale not the same object as the internal computation that generated it?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $R$ | `R` | Output rationale string | token sequence |
| $A$ | `A` | Final answer | token or label |
| $do(R=r')$ | `do R equals r prime` | An experiment replacing the rationale with $r'$ | intervention |
| $D_R$ | `D sub R` | Answer dependence on rationale interventions | scalar metric |
| plausibility | `plausibility` | How plausible the explanation seems to a person | judgment |
| faithfulness | `faithfulness` | How well the explanation reflects factors producing the answer | claim family |

## 1. Two evaluation axes

Plausibility evaluates whether the sentences are logical and readable. Faithfulness evaluates how they relate to the model's answer-generation process. Both a plausible post-hoc explanation and an awkward scratchpad actually used to compute the answer are possible.

## 2. Intervention tests

For example, the answer-change rate between conditions retaining and modifying a rationale can be measured as

$$
D_R
=
\frac1N\sum_{i=1}^{N}
\mathbf 1\left[A_i(r_i)\ne A_i(r_i')\right]
$$

$A_i(r_i)$ is the answer to question $i$ obtained using the original rationale as context. $A_i(r_i')$ is the answer generated again for the same question using the modified rationale. The indicator is 1 if the answers differ and 0 if they agree. Dividing its sum by the number of questions $N$ gives the proportion of changed answers. Define in advance whether equality compares surface strings or normalized answer labels.

This intervention does not edit only the explanation while keeping an already generated answer unchanged. Replace the rationale tokens before answer generation and recompute what follows. Reusing the original rationale's KV cache after a changed token compares internal states that differ from those obtained by actually reading the new string. Match model weights, questions, answer-extraction rules, and decoding conditions. With sampling, answers can change even when the same rationale is supplied twice, so also compare against repeated conditions with an unchanged rationale.

A high $D_R$ means the answer is sensitive to that intervention, not that every sentence of the original rationale truthfully explains the internal process. Conversely, a low $D_R$ under a meaning-preserving paraphrase may be expected because the same answer should be retained. Interpret the score in terms of what content the experiment changed.

Test types include:

- Truncation: retain only a prefix or remove the text after an intermediate point
- Paraphrase: change wording while preserving meaning
- Error insertion: insert a controlled error into an intermediate step
- Bias cue: introduce a surface feature that steers the answer and check whether the explanation mentions it
- Counterfactual rationale: provide a rationale supporting a different answer

Replacing an intermediate sentence and appending the original suffix is also different from regenerating the remaining rationale from the replacement point. The former measures an effect with the rest of the string held fixed; the latter includes changes in subsequent reasoning. The error-insertion test in [Lanham et al. (2023)](https://arxiv.org/html/2307.13702v1#S2.SS4) regenerates the rationale after the changed step. Specify which subsequent computations are fixed to compare results from tests with the same name.

The following figures locate the edit before answer generation, show the scope of recomputation, and illustrate the question-level answer changes counted by the indicator.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Original token and state row P R1 R2 R3 A contrasts edited row P R1 R2 prime R3 prime A prime with prefix cache reused only for P and R1 while the changed token and suffix are recomputed](../../figures/assets/I07/I07-16-edited-context-cache.svg)

<figcaption>P is the question, and R₁–R₃ are illustrative rationale-token positions. If R₂ changes before answer generation, the unchanged P and R₁ prefix can be reused, but states from R₂′ onward and the answer must be computed from the changed context. This is not a comparison that reuses the original KV cache from R₂ onward.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two pipelines share edited rationale prefix then one retains old suffix R3 while the other regenerates R3 prime before both generate their new answers](../../figures/assets/I07/I07-16-fixed-versus-regenerated-suffix.svg)

<figcaption>After the same R₂′, the left pipeline appends the original R₃ and the right generates a new R₃′. The left measures an effect with the other text held fixed; the right includes changes in the subsequent rationale. The diagram assumes neither agreement nor disagreement between their answers.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Twenty question indicator cells group five changed-answer ones and fifteen same-answer zeros whose sum five divided by twenty gives dependence zero point two five](../../figures/assets/I07/I07-16-answer-change-indicators.svg)

<figcaption>The five changed answers among the exercise's 20 questions are grouped in the upper row. Each cell is an indicator under the predefined answer-comparison rule; their sum is 5. Dividing by 20 gives D_R = 0.25. The arrangement does not show which actual questions changed in their original order.</figcaption>

</figure>

## 3. Confounders and controls

Changing a rationale can also change its length, token probabilities, and prompt format. Include length- and style-matched irrelevant text, meaning-preserving paraphrases, and equal-token-budget controls. Also distinguish a model's ability to follow an externally supplied rationale from the faithfulness of its self-generated CoT.

If an inserted error leaves the answer unchanged, the final label alone cannot distinguish ignoring the sentence from recognizing and correcting the error. Check that a meaning-preserving control truly retains the same claim. If a final sentence stating the answer is retained while only the earlier explanation is paraphrased, a path that simply copies that answer can remain. Match controls not only by token count but also by where answer cues remain.

The counterexample below asks whether an unchanged answer distinguishes ignoring an erroneous sentence from correcting it.

<figure class="lesson-figure" markdown="1">

![Illustrative edited arithmetic rationale two plus two equals five can be ignored using hidden correct four or repaired to two plus two equals four and both pathways produce answer four](../../figures/assets/I07/I07-16-null-answer-ignore-repair.svg)

<figcaption>These are two illustrative ways answer 4 could persist after the erroneous sentence “2 + 2 = 5.” The left ignores the sentence and reads an already available correct answer; the right corrects the error and computes the answer. The same final label cannot distinguish them. This is not evidence that these paths were identified in an actual model.</figcaption>

</figure>

## 4. Relation to internal evidence

CoT intervention is a behavioral test. Activation patching and circuit analysis test internal nodes. Agreement can provide stronger triangulation, but mapping CoT tokens one-to-one to particular internal features requires a separate alignment hypothesis and interventions.

## 5. CPU exercise

<!-- I07_EXAMPLE: i07_16_cot_faithfulness -->

Compare two synthetic models that output the same original rationale. One uses the rationale signal for its answer; the other answers from a hidden signal and then appends the rationale. Changing the rationale changes only the first model's answer.

Initially, both signals in the exercise are 1, so the models give the same answer. Setting only the rationale signal to 0 makes the function reading it answer 0, while the function reading the hidden signal still answers 1. This synthetic counterexample shows that observing the same original string and answer cannot distinguish these dependencies. This binary-signal example alone does not measure the linguistic faithfulness of actual CoT.

The following figure compares the post-intervention dependencies of the two CPU synthetic models, which originally have the same signals and answer.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two CPU binary-signal models both originally have hidden one rationale one answer one; after rationale alone becomes zero rationale-reading model answers zero while hidden-reading model still answers one](../../figures/assets/I07/I07-16-cpu-rationale-hidden-dependence.svg)

<figcaption>Both existing CPU synthetic models initially have H = R = 1 and answer 1. After only R changes to 0, the left function reading the rationale answers 0; the right function reading H answers 1. This counterexample shows that their original strings and answers cannot distinguish the dependencies; it is not a score of actual linguistic faithfulness.</figcaption>

</figure>

## Common misconceptions

### Misconception 1. A correct CoT is faithful

Post-hoc rationalization can agree with the correct answer. Interventions must test the relationship to the factors generating the answer.

### Misconception 2. An unchanged answer after changing the rationale means unfaithfulness

Other internal paths may preserve the same information, or the intervention may be weak. Check the null result's statistical power and whether meaning was preserved.

## Exercises

### 1. Evaluation axes

Is a grammatically perfect explanation generated after the answer plausible, faithful, or both?

<details>
<summary>Show solution</summary>

It may seem plausible to a person. If it was not used to generate the answer, there is no evidence of process faithfulness.

</details>

### 2. Calculate dependence

Of 20 questions, 5 answers changed after a rationale intervention. What is $D_R$?

<details>
<summary>Show solution</summary>

It is $5/20=0.25$.

</details>

### 3. Paraphrase control

Why is a meaning-preserving paraphrase condition needed alongside an error-insertion condition?

<details>
<summary>Show solution</summary>

It helps distinguish a change caused by the error's meaning from one caused merely by wording or length changes.

</details>

### 4. Truncation limits

Removing the second half of a CoT left the answer unchanged. Give two possible interpretations.

<details>
<summary>Show solution</summary>

The second half may not have been needed for the answer, or the necessary information may already have been in the prefix or hidden state. This does not establish that the entire CoT is unfaithful.

</details>

### 5. Bias cue

The answer changes with option order, but the CoT does not mention that order. What does this suggest?

<details>
<summary>Show solution</summary>

An observable cue affecting the answer is omitted from the explanation. This supports the possibility that the CoT does not fully report the factors determining the answer.

</details>

### 6. Internal connection

What else is needed to identify a CoT sentence with a particular attention head?

<details>
<summary>Show solution</summary>

An alignment hypothesis relating sentence content to the head state, held-out recovery, and evidence that intervening on the head selectively changes that CoT content and the answer are needed.

</details>

## Evidence and update boundaries

Use [Turpin et al. (2023)](https://arxiv.org/abs/2305.04388) for results in which biasing features are omitted from CoT explanations and [Lanham et al. (2023)](https://arxiv.org/abs/2307.13702) for truncation, error, and paraphrase tests. Differences across models and tasks are substantial, so do not treat a single test score as a universal faithfulness measure.

## Lesson summary

- CoT is an observable output string, not an assumed direct record of internal computation.
- Plausibility and faithfulness are different evaluation axes.
- Rationale intervention tests answer dependence but does not ensure a complete process explanation.
- Connecting behavioral and internal intervention evidence requires an additional alignment hypothesis.

## Pass criteria

- Can you distinguish plausibility from faithfulness?
- Can you design a rationale-dependence experiment and its controls?
- Can you bound the interpretation of null and positive results?

## Next lesson

- [I07-17 Capstone exercise: a small circuit](I07-17-capstone-small-circuit.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] CoT observations and internal computation are distinguished.
- [x] Rationale interventions and controls are included.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretation claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is implicitly required.
- [x] Internal links and math rendering have been checked.
