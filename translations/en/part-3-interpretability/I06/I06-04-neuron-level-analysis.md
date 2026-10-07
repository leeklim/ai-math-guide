---
id: "I06-04"
title: "Neuron-level analysis"
part: 3
stage: "I06"
status: "complete"
prerequisites: ["I06-03", "M03-03"]
estimated_time: "100~130 minutes"
---

# I06-04. Neuron-level analysis

## Why this lesson matters

A coordinate of an activation vector is easy to analyze because the implementation exposes it directly. Calling a coordinate a distinct concept, however, requires checking its basis dependence and its selectivity across inputs. Rotating the same representation space preserves distances and inner products between vectors, but it can change which coordinate responds strongly.

## Learning objectives

- Define a neuron activation by its layer, token, and coordinate.
- Compute top-activating examples and distributions for specified conditions.
- Explain how an orthogonal change of basis affects coordinate interpretations and representation geometry.
- List checks that distinguish a polysemantic response from a measurement error.

## Prerequisite check

- Prerequisite lessons: [I06-03 Distributions and basic statistics](I06-03-distributions-basic-statistics.md), [M03-03 Change of basis and coordinate dependence](../../part-1-foundations/M03/M03-03-change-of-basis-coordinate-dependence.md)
- Check question: If every activation is rotated by an orthogonal matrix, do pairwise distances change?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $a_j(x)$ | `activation coordinate j for x` | Coordinate $j$ at the selected location for input $x$ | scalar |
| selectivity | `selectivity` | The extent to which a coordinate responds consistently more strongly under one condition than under others | statistic |
| preferred examples | `preferred examples` | Inputs with large activations | ranked samples |
| polysemantic neuron | `polysemantic neuron` | A coordinate that responds to several different patterns | coordinate-level description |
| $Q$ | `orthogonal matrix Q` | A change of basis that preserves lengths and inner products | $d\times d$ |
| basis dependence | `basis dependence` | The property that coordinate values and interpretations change with the basis | property |

## 1. Fix the analysis target

In neuron analysis, identify a coordinate with the following information.

```text
model@revision / module / layer / token rule / coordinate j
```

The same `coordinate 37` means different things in the residual stream, an MLP intermediate activation, and an MLP output. If you average over tokens, you have an aggregated coordinate statistic rather than a neuron activation for an individual token.

A basic report for coordinate $j$ on an input set $D$ includes:

- The minimum, median, mean, standard deviation, and maximum.
- Examples with large and small activations.
- Distributions under predefined conditions.
- Relationships with input length and token ID.
- Repeatability across seeds or paraphrases.

The three components with the same coordinate number are still different vectors.

<figure class="lesson-figure" markdown="1">

![Coordinate 37 is highlighted in separate residual, MLP intermediate, and MLP output vectors, whose component definitions and dimensions differ.](../../figures/assets/I06/I06-04-coordinate-location.svg)

<figcaption>The same coordinate 37 is a different measurement depending on the tensor selected. Fix the layer and token, then specify both the component and coordinate number.</figcaption>
</figure>

## 2. Top examples generate hypotheses

Ranking inputs by $a_j(x)$ can suggest hypotheses about the patterns that activate a coordinate. Looking only at top-ranked examples, however, loses the base rate. Even if `Paris` and `Berlin` rank highly, you must check whether the coordinate responds to all city sentences and whether it also responds to sentences that are not about cities.

Test the hypothesis with a positive set, a hard negative set, and counterexamples. Do not evaluate a description derived from top examples on those same examples.

Separate the examples that generated the hypothesis from the inputs used to test it next.

<figure class="lesson-figure" markdown="1">

![Top activation examples Paris and Berlin generate a city hypothesis that is tested on new positives, hard negatives, and counterexamples rather than on the ranked examples alone.](../../figures/assets/I06/I06-04-top-examples-to-tests.svg)

<figcaption>Top-activation examples generate a city-response hypothesis. Next, check the response on new positives, hard negatives, and counterexamples instead of reusing the original examples to confirm it.</figcaption>
</figure>

## 3. Basis dependence

Let $A$ be a matrix whose rows are activation vectors. For an orthogonal matrix $Q$, changing coordinates by

\[
A'=AQ
\]

preserves distances between rows.

\[
\lVert a_iQ-a_kQ\rVert_2=\lVert a_i-a_k\rVert_2.
\]

Because $Q$ multiplies the difference of the row vectors, expanding the squared norm gives

\[
\lVert(a_i-a_k)Q\rVert_2^2
=(a_i-a_k)QQ^\top(a_i-a_k)^\top
=\lVert a_i-a_k\rVert_2^2
\]

For a square orthogonal matrix, $QQ^\top=I$, so the rotation term disappears. In contrast, a column of $A'$ mixes the original coordinates using the coefficients in the corresponding column of $Q$. Distance preservation is a property of the entire vector; it does not mean that the magnitude of a particular column or its correlation with a label is preserved.

Under a general rotation, coordinate 0 of $A$ and coordinate 0 of $A'$ read different directions. A coordinate's correlation with a label can therefore change. Even when the learned architecture provides a privileged coordinate basis, as an MLP nonlinearity does, equating a single coordinate with a complete concept requires separate evidence.

Use the existing synthetic exercise to check coordinate correlations separately from preservation of the overall distances.

<figure class="lesson-figure" markdown="1">

![Exact correlations in the existing 60 by four synthetic lab fixture are redistributed over coordinates after an orthogonal rotation.](../../figures/assets/I06/I06-04-coordinate-correlations.svg)

<figcaption>These are the results of rotating the existing synthetic exercise's 60×4 activations without changing them otherwise. The signal remains, but the coordinate most strongly correlated with it changes.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![All 1770 pairwise distances among the 60 synthetic lab inputs lie on the equal distance line before and after orthogonal rotation.](../../figures/assets/I06/I06-04-pairwise-distance-invariance.svg)

<figcaption>Distances before and after rotation are compared for 1,770 input pairs from the same synthetic exercise. Each distance uses all four coordinates. This geometry is preserved even when the response of an individual coordinate changes.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Rotating a collected activation for analysis branches off an unchanged model path, whereas inserting a rotation into the model changes the downstream computation and needs compensation.](../../figures/assets/I06/I06-04-analysis-versus-rewiring.svg)

<figcaption>Q on the left changes the coordinates of collected activations for analysis. Inserting it into the model path, as on the right, also requires corresponding changes to downstream operations. An elementwise nonlinear function does not commute with an arbitrary rotation.</figcaption>
</figure>

## 4. Polysemanticity and alternative explanations

A coordinate's top examples may mix patterns involving grammar, topic, and punctuation. Several explanations are possible.

- Several features genuinely share the coordinate.
- A small sample highlights a chance commonality.
- Tokenization, position, or length confounds the response.
- A direction in a higher-dimensional space has been incorrectly reduced to a single coordinate.

Neuron analysis is an exploration that narrows down these possibilities. Subsequent interventions test causal function.

If meaning and sentence-final punctuation vary together, cross the two conditions in a test.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A two by two proposed input design crosses city versus noncity examples with terminal punctuation versus no punctuation and leaves all activations unmeasured.](../../figures/assets/I06/I06-04-city-punctuation-controls.svg)

<figcaption>This input design crosses the city condition with sentence-final punctuation. Each aⱼ is a value still to be measured. Such contrasts are needed to separate patterns that occurred together under one condition.</figcaption>
</figure>

## CPU exercise

Put a signal in coordinate 0 of synthetic activations, then rotate the entire space orthogonally. Pairwise distances are the same before and after rotation, but the coordinate most strongly correlated with the signal changes.

<!-- I06_EXAMPLE: i06_04_neuron_basis -->

This result does not mean that `coordinate interpretations are meaningless`. Record both facts: a coordinate may be an actual computational unit in the architecture, and its description depends on the basis.

## Common misconceptions

### Misconception 1. The highest-activation examples define the coordinate

Top examples are a sample used to generate a hypothesis. Evaluate the description's sensitivity and specificity on negatives and new samples.

### Misconception 2. A neuron is always a single feature

A coordinate may respond to several patterns, or a feature may be distributed across several coordinates.

### Misconception 3. Coordinates are useless because the model behaves the same after rotation

Rotating collected activation coordinates for analysis is different from changing the model's internal computation. If you change coordinates inside the model, the operations that read and write those coordinates must change correspondingly. Linear projections can be matched by changing the basis of their weights. Elementwise nonlinearities do not commute with general rotations, however, so changing weights alone does not guarantee the same function. Distinguish the geometry preserved in the thought experiment from coordinatewise computation in the actual architecture.

## Exercises

### 1. Specify the location

Name two pieces of information missing from `layer 5 neuron 10`.

<details><summary>Show solution</summary>The model and revision, component or module, and token-selection rule are missing. A layer contains several residual, attention, and MLP tensors.</details>

### 2. Top examples

After examining the top 20 inputs, you propose a `city neuron` hypothesis. What should the next test be?

<details><summary>Show solution</summary>Evaluate the response on city positives, noncity hard negatives, and minimal contrast inputs that were not used to generate the hypothesis. Specify the base rate and threshold as well.</details>

### 3. Orthogonal rotation

If $Q^TQ=I$, why is $\lVert aQ\rVert_2=\lVert a\rVert_2$?

<details><summary>Show solution</summary>Because $\lVert aQ\rVert_2^2=aQQ^Ta^T=aa^T=\lVert a\rVert_2^2$.</details>

### 4. Coordinate correlation

The coordinate most correlated with a label changes after rotation. Can you conclude that the representation lost information?

<details><summary>Show solution</summary>No. The information may have moved into a different combination of coordinates. Test linear recoverability or geometry in the full space separately.</details>

### 5. Polysemanticity

A coordinate responds to both city names and sentence-final periods. Name one possible confound.

<details><summary>Show solution</summary>If most city examples occur at the end of a sentence, position or punctuation effects may be mixed with city meaning. Position-matched controls are needed.</details>

### 6. Claim scope

Setting a coordinate to 0 lowers accuracy. Does this immediately make the coordinate a city concept?

<details><summary>Show solution</summary>No. The intervention effect shows functional relevance, but you must control for distribution shift, scale changes, and damage to other functions. The concept description requires separate validation on examples.</details>

## Evidence and update boundaries

The possibility that coordinates and features need not correspond one to one draws on [Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/index.html). Distance preservation under a change of basis follows from the linear algebra in M03. The neuron-basis circuit evidence from 2026 concerns particular models and circuits; it does not guarantee a single meaning for every coordinate.

## Lesson summary

- Identify a neuron by model, module, layer, token, and coordinate.
- Top examples provide hypotheses to test, not established descriptions.
- Coordinate responses depend on the basis, but the model's actual coordinatewise computation is also an analysis target.
- Do not assume a one-to-one relationship between coordinates and features.

## Pass criteria

- Can you specify every part of a neuron's analysis location?
- Can you distinguish what an orthogonal rotation preserves from what it changes?
- Can you write a procedure for testing a top-example hypothesis on independent data?

## Next lesson

- [I06-05 PCA and SVD analysis](I06-05-pca-svd-analysis.md)

## Author checklist

- [x] Coordinate analysis and basis dependence are explained together.
- [x] Every exercise has a solution.
- [x] The strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and mathematical rendering have been checked.
