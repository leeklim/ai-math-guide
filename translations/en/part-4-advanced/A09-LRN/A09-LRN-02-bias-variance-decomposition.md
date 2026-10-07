---
id: "A09-LRN-02"
title: "Bias–variance decomposition"
part: 4
stage: "A09-LRN"
status: "complete"
prerequisites: ["A09-LRN-01", "M04-07"]
estimated_time: "90–120 minutes"
---

# A09-LRN-02. Bias–variance decomposition

## Why this lesson matters

How much a predictor varies across training sets and how far its average prediction lies from the target are different sources of error. The squared-loss bias–variance decomposition separates these two sources from irreducible noise.

## Learning objectives

- Decompose pointwise squared prediction error into bias, variance, and noise.
- Distinguish estimator bias from model misspecification.
- Explain the loss and sampling assumptions of the decomposition.
- Separate seed variance from data-sampling variance.

## Prerequisite check

- Prerequisite lessons: [A09-LRN-01 Hypothesis classes and risk](A09-LRN-01-hypothesis-class-risk.md), [M04-07 Estimation, bias, and variance](../../part-1-foundations/M04/M04-07-estimation-bias-variance.md)
- Check question: What is repeatedly varied when an estimator's expectation is taken?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\hat f_D(x)$ | `f hat trained on D evaluated at x` | Predictor trained on dataset $D$ | scalar |
| $\bar f(x)$ | `f bar of x` | Predictor averaged over datasets | scalar |
| $\operatorname{Bias}(x)$ | `the bias at x` | $\bar f(x)-f^*(x)$ | scalar |
| $\operatorname{Var}(x)$ | `the variance at x` | Predictor variation across datasets | nonnegative scalar |
| $f^*(x)$ | `f star of x` | Regression target $E[Y\mid X=x]$ | scalar |

## Core concepts

### What is repeatedly varied at one input?

First fix the input $x$ at which predictions will be evaluated. $f^*(x)=E[Y\mid X=x]$ is the conditional mean of labels observable at that input. Resampling the training dataset $D$ and applying the same learning procedure changes $\hat f_D(x)$. $\bar f(x)=E_D[\hat f_D(x)]$ is the mean prediction across these repetitions, not the prediction of one trained predictor.

Here, $\operatorname{Bias}(x)=\bar f(x)-f^*(x)$ and $\operatorname{Var}(x)=E_D[(\hat f_D(x)-\bar f(x))^2]$. Bias is the discrepancy of the mean prediction, whereas variance measures how individual predictions vary around that mean. Note that variance is centered on the mean predictor $\bar f(x)$, not the target $f^*(x)$.

Use the centers and distances of the two distributions below to distinguish bias, variance, and noise.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![At a fixed illustrative input two equally probable dataset-trained predictions minus one three center at one with variance four and bias one relative to target zero while independent labels plus minus square root two center at target zero with noise variance two](../../figures/assets/A09-LRN/A09-LRN-02-prediction-and-label-centers.svg)

<figcaption>To illustrate the existing bias 1, predictor variance 4, and noise variance 2, set f* = 0 and assign equal probabilities to predictions −1 and 3 and, independently, to labels ±√2. The predictor's center is 1, and the labels' center is 0. Predictor variance is not calculated around target 0.</figcaption>

</figure>

### The calculation that separates three terms

Suppose $Y=f^*(X)+\varepsilon$, $E[\varepsilon\mid X]=0$, and $\operatorname{Var}(\varepsilon\mid X=x)=\sigma^2(x)$, and the test label is independent of the training dataset. If each term has a finite second moment,

$$
E_{D,Y\mid x}[(\hat f_D(x)-Y)^2]
=\operatorname{Bias}(x)^2+\operatorname{Var}(x)+\sigma^2(x).
$$

To see why only three terms remain, separate prediction error as follows:

$$
\hat f_D(x)-Y
=\bigl(\hat f_D(x)-\bar f(x)\bigr)
+\bigl(\bar f(x)-f^*(x)\bigr)-\varepsilon.
$$

The first parenthesized term has mean zero over repeated datasets, and the second is fixed. Their product therefore has expectation zero. Test noise also has mean zero and is independent of the training dataset, so the other cross terms have mean zero. Expanding the square and averaging leaves only the mean squares of the three terms. Bias is squared, but predictor variance and noise variance are already mean squares, so they are not squared again.

This is an identity at a fixed $x$. To obtain the overall population risk, also average over $X$ under the target distribution at the end. The calculation still works when noise variance depends on the input; it need not be the same constant at every input. In contrast, reusing a training label as a test label violates the independence condition, so the same cross-term cancellation cannot be claimed.

Check the cross-term cancellation using the actual products of independent combinations below.

<figure class="lesson-figure" markdown="1">

![Four equally likely independent combinations of centered predictor deviation minus two plus two and test noise minus square root two plus square root two yield cross-products plus two square root two minus two square root two minus two square root two plus two square root two summing to zero](../../figures/assets/A09-LRN/A09-LRN-02-independent-cross-products.svg)

<figcaption>For the two illustrative predictions above, r = f̂ − f̄ = ±2 and ε = ±√2. Each of the four independent combinations has probability 1/4, so E[rε] = 0. Because r and ε each have mean zero, their remaining cross terms with the fixed bias also have mean zero. An individual product need not be zero.</figcaption>

</figure>

### The relation between bias and class restrictions

Here, bias is the statistical bias of a prediction estimating $f^*(x)$. Its target and units may differ from those of bias in a parameter estimator. Model misspecification means that the class cannot express the target relationship. This bias, however, is the error of a mean prediction jointly determined by the class, learning procedure, and sample size. Even if the class contains $f^*$, regularization or finite-sample selection can leave bias. Zero bias at one input is not evidence that the class can express the entire target function.

The same simple additive decomposition does not apply directly to classification 0–1 loss or cross entropy. The calculation above relies on squaring and expanding a difference. For another loss, check definitions and a decomposition appropriate to that loss separately.

Read the following class-inclusion comparison and agreement at one point as answers to different questions.

<figure class="lesson-figure" markdown="1">

![Illustrative affine class contains target f star x equals x but a specified shrunken mean predictor one half x differs from the target except at zero showing representability alone does not fix mean algorithm selection](../../figures/assets/A09-LRN/A09-LRN-02-represented-target-biased-selection.svg)

<figcaption>The illustrative target f*(x) = x belongs to the affine class. If the learning procedure selects mean predictor f̄(x) = 0.5x within that class, bias remains at x ≠ 0. This compares representability with the procedure's mean selection; it does not prove a universal effect of a particular regularization method.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Illustrative nonlinear target x squared and mean predictor identically zero intersect at input zero with zero pointwise bias but differ at other inputs so affine-class global misspecification remains](../../figures/assets/A09-LRN/A09-LRN-02-pointwise-zero-global-mismatch.svg)

<figcaption>The illustrative target x² is compared with mean predictor 0 from an affine class. Bias is zero at x = 0, but the functions differ at other inputs. Agreement at one point does not mean that the affine class can express the entire target function x².</figcaption>

</figure>

### Repeated datasets and repeated seeds

The equation above takes repeated sampling of training datasets as the source of variation. To include learning randomness, define the expectation to repeat seeds as well. Overall predictor variation includes both seed variation within the same data and variation across datasets in the seed-averaged predictor. Changing only initialization 20 times on the same data mainly measures the former, not the total sampling variance that includes the latter. Specify which of the dataset and seed were held fixed and which were varied before comparing variance values.

The seed points and mean bars for each dataset below show the centers used across repetitions.

<figure class="lesson-figure" markdown="1">

![Illustrative two datasets each have two seed predictions minus two zero for first dataset two four for second so within-dataset variance one differs from variance four of dataset means minus one three and total prediction variance five](../../figures/assets/A09-LRN/A09-LRN-02-data-seed-nested-variation.svg)

<figcaption>Assign equal probabilities to illustrative seed predictions −2 and 0 for D₁ and 2 and 4 for D₂. Within-dataset variance is 1, the variance of dataset-specific seed means −1 and 3 is 4, and total variance is 5. Repeating seeds only on the same D₁ does not measure this between-dataset component 4.</figcaption>

</figure>

## Small example

If $\bar f(x)-f^*(x)=1$, predictor variance is 4, and noise variance is 2, expected squared error is $1+4+2=7$.

This 7 is not the squared error of one predictor on one label. It is the average over repeated evaluations of predictors trained on different datasets and independent new labels. The first term, 1, is the discrepancy of the mean predictor itself; the second, 4, is variation across predictors; and the third, 2, is variation in labels even at the same input.

The figures below separately show individual errors and the sum of the three expected contributions.

<figure class="lesson-figure" markdown="1">

![Four equally likely illustrative dataset label combinations have squared errors approximately zero point one seven two five point eight two eight nineteen point four eight five two point five one five whose mean seven is a horizontal reference not the value of each individual outcome](../../figures/assets/A09-LRN/A09-LRN-02-single-errors-and-mean.svg)

<figcaption>The four independent combinations of predictions −1 and 3 for D₁ and D₂ with labels −√2 and +√2 are calculated. In labels such as D₁−, the sign after the subscript is the label's sign. The individual squared errors differ, but their mean is 7. These are exact illustrative calculations, not results of repeated model experiments.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![A horizontal squared-error axis stacks squared bias one predictor variance four and noise variance two to reach expected squared error seven with segment boundaries zero one five seven](../../figures/assets/A09-LRN/A09-LRN-02-expected-error-components.svg)

<figcaption>The existing example's contributions 1, 4, and 2 are added on one axis in squared-error units. Squaring bias 1 gives the first term 1; variance 4 and noise variance 2 are already mean squares. The figure does not add 4² or 2².</figcaption>

</figure>

## Common misconceptions

- The claim that regularization always increases bias and decreases variance is not a theorem for every regime.
- Small seed variance does not imply stability under dataset shift.

## Exercises

### 1. Adding the terms
If bias is $-2$, variance is 3, and noise variance is 1, what is the expected squared error?
<details><summary>Show solution</summary>

It is $(-2)^2+3+1=8$.
</details>

### 2. Noise
Why does irreducible noise remain when the learner changes?
<details><summary>Show solution</summary>

It comes from data-generating randomness: $Y$ varies conditionally even at the same $X=x$.
</details>

### 3. Unit of repetition
If the data split is fixed and only probe initialization is changed 20 times, which variance is mainly measured?
<details><summary>Show solution</summary>

This measures algorithmic variance due to the optimizer and initialization on fixed data.
</details>

### 4. Scope of application
Why should numbers from the squared-loss decomposition not be attached directly to accuracy?
<details><summary>Show solution</summary>

0–1 loss does not have the same quadratic-expansion structure for cross-term cancellation.
</details>

## Sources and update boundaries

The squared-loss bias–variance decomposition is a standard regression identity. This identity alone is not used to explain double descent in modern overparameterized regimes.

- [Stanford CS229 Bias–Variance, pp. 40–45](https://cs229.stanford.edu/notes2022fall/bias-variance-annotated.pdf): The squared-error expansion over training sets and independent labels was checked against this source. The sign of bias follows this lesson's $\bar f-f^*$ convention.

## Lesson summary

- Squared error decomposes into squared bias, variance, and noise.
- Specify the data and seed sources varied by the expectation.
- Seed stability and sampling stability are different.
- Do not automatically apply the same equation to another loss.

## Pass criteria

- Can you calculate error from given bias, variance, and noise?
- Can you state which variance a repeated-probe design measures?

## Next lesson

- [A09-LRN-03 Generalization gap](A09-LRN-03-generalization-gap.md)

## Author checklist

- [x] The decomposition's loss and unit of repetition are specified.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
