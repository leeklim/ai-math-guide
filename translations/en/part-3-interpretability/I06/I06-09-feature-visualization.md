---
id: "I06-09"
title: "Feature Visualization"
part: 3
stage: "I06"
status: "complete"
prerequisites: ["I06-08"]
estimated_time: "100–130 minutes"
---

# I06-09. Feature Visualization

## Why this lesson matters

Looking at a feature direction or neuron as a single number makes it difficult to form a hypothesis about what it responds to. Ranking dataset examples by activation score or optimizing an input can reveal preferred patterns. The result is an observation about response conditions, not a feature's complete meaning or functional role.

## Learning objectives

- Define activation objectives for neurons and directions.
- Present top and bottom dataset examples together with a random baseline.
- Explain the role of regularization in activation maximization.
- Evaluate a description developed from visualization on independent inputs.

## Prerequisite check

- Prerequisite lesson: [I06-08 CCA, CKA, and RSA](I06-08-cca-cka-rsa.md)
- Check question: Can you identify false positives by looking only at top-activating examples?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $s_f(x)$ | `feature score s sub f of x` | Activation score of feature $f$ on input $x$ | scalar |
| top-$k$ examples | `top k examples` | The $k$ inputs with the highest scores | ranked subset |
| activation maximization | `activation maximization` | Method optimizing inputs to increase a score | optimization procedure |
| regularizer | `regularizer` | Term discouraging inputs from leaving the permitted range | objective term |
| hard negative | `hard negative` | Input resembling the description but to which the feature should not respond | test example |
| feature description | `feature description` | Response hypothesis developed from observed examples | human-readable hypothesis |

## 1. Define the score first

For a neuron, the score can be $s_f(x)=a_j(x)$. For a direction $v$, use the projection

\[
s_f(x)=v^Ta(x)
\]

With token-level activations, state whether the score uses a maximum, a mean, or a specified token. Examine both the top and bottom examples for directions whose signs matter.

If $v$ is a unit vector, the inner product is the signed component measured along that direction. Multiplying $v$ by the same positive factor preserves the input ranking but changes score magnitudes, so align norm conventions when comparing raw scores across directions. Even for activations pointing in the same direction, an input with a larger activation norm can have a larger score. Distinguish whether the comparison concerns the directional response or overall activation magnitude.

Examine how directional projection and token aggregation each define the score.

<figure class="lesson-figure" markdown="1">

![The problem activation two three is projected onto unit direction one zero; its horizontal signed component is two while its second coordinate does not contribute.](../../figures/assets/I06/I06-09-direction-projection.svg)

<figcaption>The exercise's unit direction v=(1,0) reads the first component, 2, of a=(2,3). Even along the same direction, changing the norm of v or the overall magnitude of a can change the score magnitude.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![Three token-level feature scores feed alternative maximum, mean, or selected-token reducers; the reducer is chosen before ranking inputs.](../../figures/assets/I06/I06-09-token-score-aggregation.svg)

<figcaption>Even with scores for each token, the maximum, mean, and specified-token score are different measurements. The figure illustrates the computational roles of three tokens; it does not assign arbitrary measured values.</figcaption>
</figure>

## 2. Dataset examples

Calculate scores on a fixed dataset and examine top-$k$, bottom-$k$, and random examples side by side. Showing only top examples can hide the overall base rate and a feature's lack of selectivity. Mark not only the input text but also the token at which the score was measured.

After developing a candidate description, evaluate the following on a separate validation set.

- Does the feature activate on positives that fit the description?
- Is activation low on similar hard negatives?
- Does the response persist under paraphrasing and position changes?
- Is it merely tracking a particular token ID or length?

The two ends of the ranking and the proportions in the full dataset provide different information.

<figure class="lesson-figure" markdown="1">

![Ten top-example cells contain eight question marks while a normalized dataset proportion has nine of ten bins marked questions, so eighty percent top is below ninety percent overall.](../../figures/assets/I06/I06-09-top-versus-base-rate.svg)

<figcaption>In the exercise, questions make up 80% of the top examples, below the overall 90%. The ten lower cells normalize the full dataset's proportions; they do not mean that the actual dataset contains only 10 examples.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The existing twenty-row synthetic fixture is ordered by its normalized direction score, with blue hatched bottom five and green top five on opposite signed ends; labels did not determine order.](../../figures/assets/I06/I06-09-signed-ranking.svg)

<figcaption>Scores are ranked using the same seed and direction as the existing 20×6 CPU inputs. The blue hatched bottom 5 and green top 5 show both ends of the axis. Labels were not used to select the ranking, and these are not inputs from an actual language model.</figcaption>
</figure>

## 3. Input optimization

For a differentiable input $x$, we can solve

\[
\max_x\ s_f(x)-\lambda R(x)
\]

$R(x)$ is a penalty quantifying a cost based on the norm, smoothness, or a natural-image prior, and $\lambda\ge0$ sets its weight. Without this term, optimization can produce artifacts to which the model responds strongly but which are rarely seen in the data distribution.

Optimization changes the input while keeping model weights fixed. When differentiation is possible, the gradient-ascent direction is $\nabla_x s_f(x)-\lambda\nabla_x R(x)$, incorporating both changes that increase activation and changes that reduce the penalty. A finite penalty is a soft constraint: a high score can be selected despite incurring a cost. To guarantee that the input stays within a permitted range, the optimization domain must also be explicitly restricted.

Discrete tokens in a language model are difficult to optimize directly by gradient ascent. Embedding optimization, token search, and candidate generation with a generative model each define different permitted input spaces. Even if a result looks like natural language, it is not guaranteed to lie on the training distribution.

A value reached by moving an embedding vector continuously may match no row in the actual token table. Replacing it with a nearby token can change both the input and the score, so rescore the final token sequence. Dataset examples and optimized inputs differ even in the input spaces where responses were observed.

Distinguish changes to the input from the fixed weights, and check the step that returns a continuous embedding to an actual token.

<figure class="lesson-figure" markdown="1">

![A variable input goes through a fixed-weight model; feature-score ascent and negative penalty gradient jointly update the input, while hard bounds require an explicit domain.](../../figures/assets/I06/I06-09-input-optimization.svg)

<figcaption>The optimized object is the input x, not the model weights. The update combines the score gradient with a direction that reduces the penalty; a finite penalty alone does not guarantee that the permitted domain is respected.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![An optimized continuous embedding lies between three discrete token embeddings, then snapping to a token changes the point and requires rescoring.](../../figures/assets/I06/I06-09-embedding-to-token.svg)

<figcaption>The optimized continuous embedding x* need not equal a row in the token table. Rescore the final input after converting it to actual tokens. The coordinates illustrate this difference conceptually.</figcaption>
</figure>

## 4. Visualization and function

A feature's response to particular examples is an observation. Whether removing or amplifying the feature changes behavior as predicted is an intervention question. A visualization-based description can be used as an intervention target, but the two results should not be combined as the same evidence.

Separate the route that observes responses from the route that tests behavior through an intervention.

<figure class="lesson-figure" markdown="1">

![Observed activating examples support a reaction hypothesis; removing or amplifying a feature and comparing controlled behavior is a separate intervention route.](../../figures/assets/I06/I06-09-observation-intervention.svg)

<figcaption>Top and bottom examples generate a hypothesis about response conditions. Whether behavior changes after removal or amplification is a separate controlled-intervention question. Do not combine the two routes as the same evidence.</figcaption>
</figure>

## CPU lab

Calculate scores for a fixed direction in a synthetic representation and select the top and bottom five inputs. Labels are not used for sorting; inspect the label proportions among top examples after sorting.

<!-- I06_EXAMPLE: i06_09_feature_visualization -->

Even a high proportion of a label among top examples is an observation developed from the same data. Independent validation and hard negatives are the next step.

## Common misconceptions

### Misconception 1. What top examples have in common defines the feature

It is a candidate description. Test its predictive value on unselected inputs and counterexamples.

### Misconception 2. Strange optimized inputs mean the feature is fake

The optimization parameterization and regularizer can produce artifacts. Examine dataset examples and multiple parameterizations together.

### Misconception 3. A plausible human description is objective

Evaluator bias and ambiguity remain. Separate examples used to generate the description from those used for scoring, and record the evaluation rules.

## Exercises

### 1. Direction score

If $v=(1,0)$ and $a(x)=(2,3)$, what is $v^Ta(x)$?

<details><summary>Show solution</summary>It is 2. The second coordinate does not contribute to this direction score.</details>

### 2. Bottom examples

Why are bottom examples needed for a signed direction?

<details><summary>Show solution</summary>They show patterns in the opposite direction and asymmetry in the scores. Looking only at top examples observes just one side of the feature axis.</details>

### 3. Base rate

Eight of the top 10 examples are questions, while 90% of the entire dataset consists of questions. Does this establish selectivity?

<details><summary>Show solution</summary>The proportion of questions among top examples is actually lower than the overall proportion. Compare it with the overall base rate.</details>

### 4. Regularizer

Why include a smoothness penalty in activation maximization?

<details><summary>Show solution</summary>It discourages high-scoring inputs rarely seen in natural data, such as high-frequency artifacts. The penalty does not guarantee meaning.</details>

### 5. Independent evaluation

What problem arises if a description's accuracy is scored using the same top examples from which it was developed?

<details><summary>Show solution</summary>Hypothesis generation and evaluation use the same data, leading to overestimation. Score it on separate inputs and hard negatives.</details>

### 6. Causal claim

`Paris` had the highest score. Can we conclude that the feature caused the model to answer with a capital city?

<details><summary>Show solution</summary>No. This is only an observed response. Controlled ablation or patching and behavioral measurements are needed.</details>

## Sources and update boundaries

Dataset examples, activation maximization, and the limitations of regularization are explained using [Feature Visualization](https://distill.pub/2017/feature-visualization/). Natural-image priors and language token search are different implementation problems.

## Lesson summary

- Fix the feature score and token aggregation first.
- Examine top, bottom, and random examples together with the base rate.
- Optimized inputs depend on the regularizer and input parameterization.
- Validate visualization-based descriptions on independent data and distinguish them from causal evidence.

## Pass criteria

- Can you specify a feature score and a top-$k$ procedure?
- Can you explain the difference between dataset examples and activation maximization?
- Can you design positives and hard negatives to validate a description?

## Next lesson

- [I06-10 Superposition](I06-10-superposition.md)

## Author checklist

- [x] Visualization is separated into hypothesis generation and validation.
- [x] Every exercise has a solution.
- [x] The strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and mathematical rendering have been checked.
