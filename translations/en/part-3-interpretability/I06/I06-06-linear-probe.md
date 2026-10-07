---
id: "I06-06"
title: "Linear probe"
part: 3
stage: "I06"
status: "complete"
prerequisites: ["I06-05", "M04-08"]
estimated_time: "110~140 minutes"
---

# I06-06. Linear probe

## Why this lesson matters

A linear probe measures whether a label can be recovered linearly from activations. It uses a direction across coordinates rather than a single coordinate, and a more restricted function class than a complex nonlinear decoder. High held-out accuracy shows linear recoverability; it does not mean that the model uses the information to produce its output.

## Learning objectives

- Define a linear probe's inputs, target, and evaluation unit.
- Train a regularized probe after separating training and test data.
- Compare accuracy with majority and input-only baselines.
- Write a conclusion that distinguishes recoverability from functional use.

## Prerequisite check

- Prerequisite lessons: [I06-05 PCA and SVD analysis](I06-05-pca-svd-analysis.md), [M04-08 Regression and classification](../../part-1-foundations/M04/M04-08-regression-classification.md)
- Check question: If you select a layer after examining probe test labels, is the test split still an independent evaluation?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $h_i$ | `representation h sub i` | The frozen activation of input $i$ | $\mathbb R^d$ |
| $y_i$ | `label y sub i` | A predefined label to recover | finite class set |
| $w^Th_i+b$ | `w transpose h sub i plus b` | A binary linear probe's score | scalar |
| probe | `linear probe` | A linear predictor trained on frozen representations | auxiliary model |
| held-out accuracy | `held-out accuracy` | Accuracy on samples not used to select the probe | $[0,1]$ |
| decodability | `linear decodability` | The property that information can be recovered by a specified function class | evidence level |

## 1. What a probe asks

Train a linear function to predict label $y_i$ from a frozen activation $h_i$. In the binary case, its score is

\[
s_i=w^Th_i+b
\]

A threshold or logistic probability determines the class. The model weights remain unchanged; only the probe parameters are learned.

The inner product multiplies each activation coordinate by its coefficient in $w$ and sums the results. The probe therefore reads a linear combination of coordinates, not just one coordinate. When $w\ne0$, $w^Th+b=0$ is a hyperplane separating the two classes. A logistic probability is obtained by applying sigmoid to this score. Even though the probability transformation is nonlinear, thresholding at 0.5 gives the same hyperplane boundary. With a least-squares score, choose a threshold that matches the numerical encoding of the labels.

The question is narrower than `does the representation contain information?` It is: **Can the label be recovered on held-out samples using the selected sample, location, preprocessing, and linear function class?**

Considering the separate readout and the linear boundary clarifies what the probe measures.

<figure class="lesson-figure" markdown="1">

![A frozen activation branches to the original model readout and to a separately learned probe; only the probe parameters change.](../../figures/assets/I06/I06-06-external-readout.svg)

<figcaption>The original model and a separate probe read the same activation. Even if the probe recovers the label, this does not mean the original readout uses the same direction.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![In a two-dimensional schematic, a score-zero boundary separates positive and negative half-spaces and its normal vector w is perpendicular.](../../figures/assets/I06/I06-06-score-hyperplane.svg)

<figcaption>This schematic shows a 2-dimensional boundary. The vector w is perpendicular to the boundary, and the score's sign separates its two sides. Sigmoid's 0.5 boundary is the same score=0 boundary.</figcaption>
</figure>

## 2. Splits and preprocessing

Split the data by input group. Standardize using the training mean and standard deviation, then apply those values to validation and test data. Computing statistics on the entire dataset first lets test information enter preprocessing.

Choose the layer, regularization, and threshold using training and validation data. Use the test set once for final evaluation. If you compare layers by test accuracy, that test set becomes a selection set.

Apply the transformation fitted on training data unchanged, rather than fitting new statistics to each split.

<figure class="lesson-figure" markdown="1">

![Training groups fit mean and scale once, then the frozen preprocessing transforms train, validation, and test before their distinct roles.](../../figures/assets/I06/I06-06-train-only-preprocessing.svg)

<figcaption>Fit preprocessing statistics only on training data, then apply the same values to all three splits. Validation is for selection; test is for final evaluation. This diagram specifies a 3-split evaluation contract and does not change the CPU example's 2-split results.</figcaption>
</figure>

## 3. Regularization and probe capacity

Even a linear probe can memorize labels when $d$ is large and $n$ is small. A least-squares probe with a ridge penalty can be written as

\[
\hat w=\arg\min_w\sum_i(y_i-w^Th_i)^2+\lambda\lVert w\rVert_2^2
\]

The value of $\lambda$ affects probe capacity and numerical stability. A single performance value cannot separate the contributions of the representation and the probe.

The first term sums prediction errors on training samples; the second charges a cost for squared weight magnitude. The objective above omits the bias. If $\lambda=0$ and there are more features than samples, multiple weights may yield the same training error. For $\lambda>0$, $H^TH+\lambda I$ is positive definite, giving a unique weight solution for this least-squares problem. Each row of $H$ is a transposed training activation. The penalty restricts choices that reduce training error through large weights, but it may also weaken the label signal, so held-out evaluation is needed.

Ridge penalizes even directions that do not affect training predictions.

<figure class="lesson-figure" markdown="1">

![Along a unit null direction v of the training design, predictions do not change; from a minimum-norm base weight w zero orthogonal to v, the added ridge cost is lambda times t squared.](../../figures/assets/I06/I06-06-ridge-null-direction.svg)

<figcaption>Adding t v along a unit direction with H v=0 leaves training predictions unchanged. Here the minimum-norm base weight w₀ is assumed orthogonal to v, so ⟨w₀,v⟩=0. Under this condition, the added ridge cost is λt², allowing comparison of the flat cost at λ=0 with t² at λ=1. For a general base weight w, the added cost is λ(2t⟨w,v⟩+t²). Strict convexity for λ>0 eliminates this nonuniqueness but does not guarantee held-out performance.</figcaption>
</figure>

## 4. Baselines and metrics

Accuracy alone is insufficient when classes are imbalanced. Examine the majority baseline, balanced accuracy, and confusion matrix together. If input length or token identity alone predicts the label, it is unclear whether an activation probe demonstrates additional information. An input-only baseline is also needed.

Accuracy pools all inputs, giving more influence to the class with more samples. Balanced accuracy averages per-class recall with equal weights. This distinguishes predicting only the majority class correctly from distinguishing both classes. To interpret a difference in recovery performance, the input-only baseline and activation probe must also use the same split and evaluation unit.

Compare an evaluation weighted by class frequency with one that weights the two classes equally.

<figure class="lesson-figure" markdown="1">

![A normalized 100-input grid has ninety majority examples predicted correctly and ten minority examples marked wrong; pooled accuracy is ninety percent but equal-weight class recall is fifty percent.](../../figures/assets/I06/I06-06-imbalance-weighting.svg)

<figcaption>The exercise's 90% majority class is normalized to a grid of 100 cells. Predicting only the majority class gives 90% accuracy, but the two class recalls are 100% and 0%, so balanced accuracy is 50%.</figcaption>
</figure>

## 5. Supported conclusions

After passing held-out test and baseline checks, write a conclusion such as:

> On this dataset and at this measurement location, the label was recoverable with a regularized linear probe.

The following statement is not yet supported.

> The model uses this direction to produce its answer.

A claim of use requires separate functional tests, such as interventions on the probe direction, alignment with downstream weights, or causal mediation.

## CPU exercise

Place a binary label signal in a combination of two coordinates of an 8-dimensional synthetic representation. Fix 60 training and 20 test samples, then evaluate a ridge linear probe.

<!-- I06_EXAMPLE: i06_06_linear_probe -->

High accuracy is expected because the synthetic generation process includes a linear signal. Do not use it as a performance standard for actual model results.

## Common misconceptions

### Misconception 1. A linear probe is too simple to memorize

With few samples in a high-dimensional space, even a linear classifier can separate arbitrary labels. A control task is needed.

### Misconception 2. High accuracy ranks representation quality

Accuracy depends on the dataset, labels, layer, probe capacity, and metric. Do not rank representations intended for different purposes by a single number.

### Misconception 3. Probe weights are the model's actual readout

The probe learns a new direction. Whether the model's downstream weights use the same direction is a separate question.

## Exercises

### 1. Shape

For a binary probe with $h_i\in\mathbb R^{768}$, what are the shapes of $w$ and the score?

<details><summary>Show solution</summary>$w\in\mathbb R^{768}$, and $w^Th_i+b$ for one input is a scalar. Scores for a batch of $n$ inputs form a vector of length $n$.</details>

### 2. Leakage

PCA was fitted on the entire dataset before splitting off the test set. Is there a problem?

<details><summary>Show solution</summary>Yes. The PCA directions used the test activation distribution. Split first, fit PCA on training data, and apply the same transformation to test data.</details>

### 3. Baseline

The positive class makes up 90% of the samples, and probe accuracy is 90%. What should you check?

<details><summary>Show solution</summary>A majority predictor also achieves 90%, so there is no improvement. Examine balanced accuracy, per-class recall, and the confusion matrix.</details>

### 4. Layer selection

You report the highest test accuracy among 12 layers. Why might this be an overestimate?

<details><summary>Show solution</summary>You used 12 selection opportunities on the test set. Select the layer on validation data and evaluate it on a separate test set, or report the multiple selection.</details>

### 5. Claim of use

Probe test accuracy is 100%. Can you conclude that the model uses the label?

<details><summary>Show solution</summary>No. This is evidence that information is available for the probe to read. Whether the model needs it in its actual computation requires an intervention or a downstream functional test.</details>

### 6. Regularization

What tradeoff generally arises when $\lambda$ increases?

<details><summary>Show solution</summary>Weight norm and variance decrease, but excessive weakening of the signal can increase bias and underfitting. Choose the value on validation data.</details>

## Evidence and update boundaries

The probe's question and limitations draw on [Probing Classifiers: Promises, Shortcomings, and Advances](https://arxiv.org/abs/2102.12452). The next lesson covers specific control and selectivity designs using [Hewitt and Liang](https://arxiv.org/abs/1909.03368) as its reference. A particular solver API is a library-version-specific implementation detail.

## Lesson summary

- A linear probe measures linear recoverability of labels from frozen activations.
- Complete splits, preprocessing, layer selection, and hyperparameter selection without using the test set.
- Evaluate probe capacity and baselines together.
- Decodability is not the model's functional use or a causal effect.

## Pass criteria

- Can you specify a probe's inputs, target, split, and metric?
- Can you write a leakage-free sequence of training, selection, and evaluation?
- Can you distinguish supported from unsupported claims based on high accuracy?

## Next lesson

- [I06-07 Probe controls and selectivity](I06-07-probe-controls-selectivity.md)

## Author checklist

- [x] Linear recoverability is separated from functional use.
- [x] Every exercise has a solution.
- [x] The strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and mathematical rendering have been checked.
