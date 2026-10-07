---
id: "I06-03"
title: "Distributions and Basic Statistics"
part: 3
stage: "I06"
status: "complete"
prerequisites:
  - "I06-02"
estimated_time: "120–150 minutes"
---

# I06-03. Distributions and Basic Statistics

## Why this lesson matters

Looking at a single activation in a plot or reading its largest coordinate does not tell us how a group of inputs is represented. We first need to examine the sample's center, variation, outliers, and differences between conditions. These checks are simpler than elaborate interpretations, but they help us judge whether later PCA, probe, or SAE results are driven by a few samples or differences in scale.

## Learning objectives

- Calculate coordinatewise means and sample variances of activation vectors.
- Distinguish the distribution of vector norms from the mean vector.
- Use z-scores and robust statistics to find potential outliers.
- Relate differences between conditions to effect size, uncertainty, and the analysis unit.
- Explain why raw activations from models with different hidden sizes cannot be compared directly.

## Prerequisite check

- Prerequisite lesson: [I06-02 activation dataset](I06-02-activation-dataset.md)
- Check question: Is the mean of $n$ vectors the same quantity as the mean of their individual norms?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\bar a$ | `a bar` | Coordinatewise sample mean of activations | $\mathbb R^d$ |
| $s_j^2$ | `s squared sub j` | Sample variance of coordinate $j$ | nonnegative scalar |
| $r_i=\lVert a_i\rVert_2$ | `r sub i equals the L two norm of a sub i` | Euclidean norm of activation $i$ | nonnegative scalar |
| $z_i$ | `z score sub i` | Position relative to the center, measured in standard-deviation units | scalar |
| outlier | `outlier` | Observation far from other samples under a specified criterion | flagged observation |
| robust statistic | `robust statistic` | Statistic relatively insensitive to extreme values | scalar or vector |

## 1. Coordinatewise means and variances

The sample mean of $n$ activations $a_1,\ldots,a_n\in\mathbb R^d$ is

\[
\bar a=\frac{1}{n}\sum_{i=1}^{n}a_i
\]

The sample variance of coordinate $j$ is

\[
s_j^2=\frac{1}{n-1}\sum_{i=1}^{n}(a_{ij}-\bar a_j)^2
\]

The denominator $n-1$ is the convention used when estimating a population variance from a sample. If the aim is to describe the mean squared deviation of the current fixed dataset itself, the denominator $n$ can also be used. State which definition you use.

Addition in the mean formula is coordinatewise. The variance formula also fixes $j$ and varies only the input index $i$, so $s_j^2$ describes variation in one coordinate, not a single variance for the entire vector. Sample variance requires $n>1$. The unbiasedness property of the $n-1$ estimator holds under assumptions such as independent sampling from the same population. Collecting several tokens from the same sentence and changing the denominator to $n-1$ does not make them independent samples.

For two activations $a_1=(1,0)$ and $a_2=(3,4)$,

\[
\bar a=(2,2),\qquad s^2=(2,8)
\]

The second coordinate varies more across these two samples. With only two samples, we cannot draw a general conclusion about the distribution.

Examine the center and coordinatewise spread of these two vectors separately.

<figure class="lesson-figure" markdown="1">

![The points one zero and three four have coordinatewise mean two two at their geometric midpoint.](../../figures/assets/I06/I06-03-coordinate-mean.svg)

<figcaption>Averaging corresponding coordinates gives the midpoint (2,2). This point represents the center; it need not occur as the activation of any actual input.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![The first coordinate values one and three deviate one unit from their mean; second coordinates zero and four deviate two units, giving sample variances two and eight.](../../figures/assets/I06/I06-03-coordinate-variance.svg)

<figcaption>For the same two inputs, the first-coordinate deviations are ±1 and the second-coordinate deviations are ±2. Dividing each coordinate's sum of squared deviations by n−1=1 gives variances of 2 and 8.</figcaption>
</figure>

## 2. Norm distributions and the mean vector

The magnitude of each vector can be summarized as

\[
r_i=\lVert a_i\rVert_2
\]

But $\lVert\bar a\rVert_2$ and $\frac{1}{n}\sum_i\lVert a_i\rVert_2$ generally differ. Vectors pointing in opposite directions cancel in the mean, while their individual norms remain positive.

For example, if $a_1=(1,0)$ and $a_2=(-1,0)$, the norm of the mean vector is 0, while the mean norm is 1. Thus, a statement that `an activation is large` must specify whether it refers to a coordinate mean, a vector norm, or a projection onto a particular direction.

The figure shows why cancellation of directions affects the two statistics differently.

<figure class="lesson-figure" markdown="1">

![Opposite unit vectors have zero mean vector but each retains unit norm, distinguishing norm of the mean from mean of norms.](../../figures/assets/I06/I06-03-norm-cancellation.svg)

<figcaption>Activations in opposite directions cancel in the vector mean. Both individual norms are 1, so a norm of 0 for the mean vector and a mean norm of 1 are different summaries.</figcaption>
</figure>

## 3. Finding potential outliers

For norm values $1,3,5$, the sample mean is 3 and the sample standard deviation is 2. The z-scores calculated with the sample standard deviation are $-1,0,1$.

\[
z_i=\frac{r_i-\bar r}{s_r}.
\]

The numerator is the difference from the center, and the denominator measures variation among the norm values. Thus, $z_i=1$ means a position one standard deviation above the mean. If $s_r=0$, all norms are equal and this formula cannot perform the division, so that case requires separate handling.

A large z-score does not automatically indicate an error. It may result from a long sentence, a special token, an incorrect token index, a domain difference, or a genuinely rare input. Investigate the cause and record the inclusion and exclusion criteria.

When the mean and standard deviation themselves are sensitive to extreme values, also examine the median and median absolute deviation. A robust statistic does not determine what an outlier means for us.

The median absolute deviation is calculated by taking each value's absolute deviation from the median and then taking the median of those deviations. Unlike a mean, it does not let a few large deviations pull up the entire sum. However, it can also be 0 when many values are repeated. Using a robust center and scale is distinct from identifying collection errors.

Compare the units of a z-score with the behavior of robust summaries when an extreme value is moved.

<figure class="lesson-figure" markdown="1">

![Norm values one three and five become z scores minus one zero and one under mean three and sample standard deviation two.](../../figures/assets/I06/I06-03-z-score-scale.svg)

<figcaption>The norm values 1,3,5 lie −2,0,2 away from their mean of 3. Dividing by the sample standard deviation of 2 gives z-scores of −1,0,1. These scores do not determine whether the values are errors.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![In the illustrative norms one, three, and five, moving only the largest value to R at least five leaves the median at three and MAD at two while the mean moves.](../../figures/assets/I06/I06-03-robust-largest-value.svg)

<figcaption>This conceptual example moves only the largest of the values 1,3,5 to R≥5. The median remains 3 and the median absolute deviation remains 2, while the mean changes to (1+3+R)/3. These summaries alone do not determine whether a value is an error.</figcaption>
</figure>

## 4. Differences between conditions

The difference between the mean activations in two conditions is a vector.

\[
\Delta_a=\bar a_{C_1}-\bar a_{C_0}.
\]

$\lVert\Delta_a\rVert_2$ is a scalar summary, but it discards directional information. Distances can also be larger in layers with a larger overall activation scale. Cosine, whitened distance, and standardized effects provide different invariances, but none is automatically more correct. Choose a measure that matches the question in advance.

The mean-difference vector gives the direction and magnitude connecting the centers of the two groups. Within-condition variation measures how widely inputs spread around those centers. Even with the same mean difference, greater variation within the groups can make it harder to distinguish the condition of a new input. Multiplying all activations by the same positive factor multiplies the mean difference and Euclidean distances by that factor. A standardized comparison reads the difference relative to the amount of variation, but it must also specify which groups and coordinates were used to estimate that variation.

When reporting differences between conditions, include the following.

- The number of inputs in each condition and the input-selection rule
- Whether the design is paired and what the actual analysis unit is
- The mean difference and within-condition variation
- The confidence interval or bootstrap procedure
- The number of layers, tokens, and statistics examined
- Excluded outliers and exclusion criteria

In a pilot with four samples per condition, confidence intervals may be wide. The main purpose of these results is to check the collection and statistical procedures.

Examine within-condition variation, which the mean difference alone does not retain, separately from the effect of overall scale.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two schematic coordinate plots have equal mean separation vectors but small versus large within-condition spreads, so the same contrast hides different variation.](../../figures/assets/I06/I06-03-contrast-versus-spread.svg)

<figcaption>The two panels have the same mean difference Δa but different within-condition spreads. The points are a conceptual illustration, not actual model samples. A single distance does not retain this distributional difference.</figcaption>
</figure>

<figure class="lesson-figure" markdown="1">

![An activation scale multiplier alpha greater than one increases the length of the same raw mean-contrast vector to alpha times its original length.](../../figures/assets/I06/I06-03-contrast-scale.svg)

<figcaption>Multiplying all activations by the same positive α also changes the mean difference to αΔa. The figure shows the change in length for α>1; a longer raw distance does not imply a clearer distinction between conditions.</figcaption>
</figure>

## 5. Problems that arise when examining many coordinates

Testing differences between conditions separately in 768 coordinates increases the opportunities for a large value to occur by chance. Selecting the largest coordinate in a dataset and then reporting that coordinate's difference using the same data introduces selection bias.

Possible responses include the following.

- Use a projection or summary statistic specified in advance.
- Select coordinates on an exploratory split and evaluate them on a confirmatory split.
- Apply a multiple-comparison correction if all coordinates were tested.
- Report effect size and uncertainty together, rather than drawing a conclusion from a p-value alone.

## 6. Pitfalls in comparing model sizes

Pythia 160M has a hidden size of 768, while 410M has a hidden size of 1,024. Their activations differ not only in dimension but also in their learned bases and what their layers represent. Do not subtract their raw vectors or match coordinates by index.

To compare model sizes, first define what can be compared. Scalar summaries such as norm distributions can be compared, but differences in scale between models must be considered. Comparing representational structure requires methods with explicit invariances, such as CKA, CCA, or RSA, introduced in later lessons.

Even when the input rows are the same, the models' coordinate columns may not correspond.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Eight input rows from 160M have 768 coordinates while eight rows from 410M have 1024 coordinates; equal coordinate numbers do not align learned bases or layers.](../../figures/assets/I06/I06-03-model-coordinate-mismatch.svg)

<figcaption>Even with the same eight inputs, 160M and 410M have different numbers of columns and different learned bases. Matching coordinates by index or directly subtracting raw vectors is not a valid comparison.</figcaption>
</figure>

## Connection to the real-model lab

The 160M activation dataset in I06-02 records the mean and variance of the norms for eight inputs, along with the difference between condition means. These values are descriptive statistics for the fixed pilot sample. I06-08 collects activations for the same eight inputs from 410M as well, then compares them with CKA and RSA. It does not directly subtract raw vectors with different hidden sizes.

## Recommended basic report

When you receive an activation dataset, report the following in order.

1. Checks of the schema, missing values, duplicates, shape, and finite values
2. Input lengths and sample counts by condition
3. The minimum, median, mean, maximum, and distribution of activation norms
4. Summaries of coordinatewise means and standard deviations
5. A predefined condition contrast and its uncertainty
6. Checks of input and token provenance for potential outliers
7. A distinction between exploratory and confirmatory analyses

Proceed to dimensionality reduction or probing after this report passes its checks.

## Common misconceptions

### Misconception 1. The mean activation is a representative actual activation

The mean is a coordinatewise center and may never occur for any input. Examine the variance and distribution as well.

### Misconception 2. An input with a larger norm is more important

The norm measures vector magnitude. It does not directly measure contribution to the output or causal importance.

### Misconception 3. The same layer number in two models denotes the same computational stage

When the number of layers, hidden size, and learned bases differ, numbering alone does not establish correspondence. Define the architecture comparison and comparison method separately.

## Exercises

### 1. Sample mean

Find the sample mean of $a_1=(1,2)$, $a_2=(3,0)$, and $a_3=(2,4)$.

<details><summary>Show solution</summary>Add corresponding coordinates and divide by 3. The first coordinate is $(1+3+2)/3=2$, and the second is $(2+0+4)/3=2$, so $\bar a=(2,2)$.</details>

### 2. Sample variance

Find the sample variance and sample standard deviation of the scalar values $1,3,5$.

<details><summary>Show solution</summary>The mean is 3, and the sum of squared deviations is $4+0+4=8$. Dividing by $n-1=2$ gives a sample variance of 4 and a sample standard deviation of 2.</details>

### 3. Mean norm

For $a_1=(1,0)$ and $a_2=(-1,0)$, find the norm of the mean vector and the mean norm.

<details><summary>Show solution</summary>The mean vector is $(0,0)$, so its norm is 0. Both individual vectors have norm 1, so the mean norm is 1. The two statistics answer different questions.</details>

### 4. Handling an outlier

One activation norm is very large. Should it be removed immediately?

<details><summary>Show solution</summary>No. Use provenance to check the input length, special tokens, token index, collection errors, and whether it is a genuinely rare case. Exclusion criteria should be specified before viewing the results, or identified explicitly as a post hoc decision.</details>

### 5. Multiple comparisons

The coordinate with the largest difference between conditions was selected from 768 coordinates using the same sample. Can its difference be reported as an independent confirmatory result?

<details><summary>Show solution</summary>Not as it stands. Because the same sample was used to select the coordinate, the value may be overestimated. A separate confirmatory split or inference that accounts for multiple comparisons is needed.</details>

### 6. Comparing model sizes

Can a 768-dimensional vector from 160M be subtracted coordinatewise from a 1,024-dimensional vector from 410M?

<details><summary>Show solution</summary>No. The dimensions differ, and the bases and layer meanings are not aligned. Use a scalar summary with the desired invariances or a representation-comparison method such as CCA, CKA, or RSA.</details>

## Sources and update boundaries

The foundations of means, sample variance, standardization, and multiple comparisons follow the probability and statistics definitions in M04. The Pythia architecture and checkpoints were checked in the [official Pythia repository](https://github.com/EleutherAI/pythia), and the 410M config and model revision were checked in the [Pythia-410M-deduped model card](https://huggingface.co/EleutherAI/pythia-410m-deduped) on 2026-10-01. Hidden sizes and module paths may change with the model config and Transformers implementation.

## Lesson summary

- The mean vector, coordinatewise variances, and distribution of vector norms are different statistics.
- Check provenance for potential outliers, then handle them according to predefined criteria.
- Do not interpret condition differences without within-condition variation, the analysis unit, and uncertainty.
- Exploring many coordinates introduces selection bias and multiple-comparison problems.
- Raw activation coordinates from different models should not be matched directly.

## Pass criteria

- Can you calculate coordinatewise means and sample variances of activations?
- Can you distinguish the norm of the mean vector from the mean norm?
- Can you explain the principles for handling outliers and multiple comparisons?
- Can you state the invariances needed for a comparison of model sizes?

## Next lesson

- I06-04 neuron-level analysis

## Author checklist

- [x] Learning objectives are written as observable actions.
- [x] Means, variances, norms, and outliers are distinguished.
- [x] Condition comparisons are connected to the analysis unit and uncertainty.
- [x] The limits of raw-coordinate comparisons between models are explained.
- [x] Every exercise has a solution.
- [x] The strengths of model-interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and mathematical rendering have been checked.
