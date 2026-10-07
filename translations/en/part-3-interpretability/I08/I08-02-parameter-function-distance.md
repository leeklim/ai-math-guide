---
id: "I08-02"
title: "Parameter distance and function distance"
part: 3
stage: "I08"
status: "complete"
prerequisites: ["I08-01", "M02-15"]
estimated_time: "90–120 minutes"
---

# I08-02. Parameter distance and function distance

## Why this lesson matters

Large weight movement between checkpoints does not mean that model behavior changed substantially. Hidden-unit permutations and scaling symmetries represent the same function with different parameters. Conversely, even small parameter movements can produce large output differences on sensitive inputs.

## Learning objectives

- Define parameter distance and function distance as separate estimands.
- Calculate an example in which a hidden-unit permutation changes parameter distance.
- Explain how function distance depends on the input distribution.
- Avoid claiming feature learning from weight movement alone.

## Prerequisite check

- Prerequisite lessons: [I08-01 Checkpoint study design](I08-01-checkpoint-study-design.md), [M02-15 Norms and condition numbers](../../part-1-foundations/M02/M02-15-norm-condition-number.md)
- Check question: Why are the Euclidean distance between two vectors and the output difference between two functions different kinds of objects?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $d_\theta(s,t)$ | `d theta of s comma t` | Parameter distance between two checkpoints | nonnegative scalar |
| $d_f(s,t;P)$ | `d f of s comma t on P` | Function distance under distribution $P$ | nonnegative scalar |
| $\|\theta_t-\theta_s\|_2$ | `the L two norm of theta sub t minus theta sub s` | Euclidean weight distance before alignment | scalar |
| $P_X$ | `P sub X` | Input distribution for comparing the functions | probability distribution |
| symmetry | `symmetry` | Transformation that preserves the function but changes parameters | permutation, scaling, etc. |

## 1. Write the two distances separately

The simplest parameter distance is

$$
d_\theta(s,t)=\|\theta_t-\theta_s\|_2
$$

Here, flatten the weights of models with the same structure in the same order and stack them into one vector. The corresponding coordinates must match for subtraction to be defined. Squaring each coordinate difference, summing, and taking the square root measures how differences accumulate across parameters. For example, define function distance by

$$
d_f^2(s,t;P_X)=\mathbb E_{x\sim P_X}
\left[\|f_{\theta_t}(x)-f_{\theta_s}(x)\|_2^2\right]
$$

The second value includes the input distribution. Differences in unobserved input regions do not appear in a sample-based estimate.

Compute the squared error between output vectors for each input, average over the distribution, and use its square root as $d_f$. If estimated by a sample mean over $n$ inputs, divide the sum of squared errors by $n$. Because output differences are squared before averaging, positive and negative differences across inputs do not cancel. A distance of 0 means that the two outputs are equal almost surely under the chosen distribution, not that the functions are also equal outside it.

Flatten the exercise's parameters in the same order to compute coordinate differences.

<figure class="lesson-figure" markdown="1">

![The fixed toy networks flatten corresponding weights to vectors with squared distance fifty](../../figures/assets/I08/I08-02-weight-coordinate-distance.svg)

<figcaption>Subtract parameters at corresponding positions. The two weight vectors in the exercise differ coordinate by coordinate and have an L2 distance of √50, but this alone does not reveal their output differences.</figcaption>
</figure>

Below, compare the outputs of the same two networks for each input.

<figure class="lesson-figure" markdown="1">

![The original and jointly permuted two-unit ReLU networks give identical output curves on the fixed input grid](../../figures/assets/I08/I08-02-same-output-grid.svg)

<figcaption>The overlapping solid and dashed lines are outputs from the exercise's original and permuted networks. Their output differences are 0 at the five orange inputs, so the sample function RMSE is also 0.</figcaption>
</figure>

The shaded interval shows how the input distribution enters function distance.

<figure class="lesson-figure" markdown="1">

![Two analytic functions coincide inside shaded input-distribution support but differ outside it](../../figures/assets/I08/I08-02-distribution-support.svg)

<figcaption>If the input distribution is confined to the shaded interval, the two functions have zero output difference under that distribution. Differences outside the interval do not enter this distance calculation. This is an illustrative function example, not model results.</figcaption>
</figure>

## 2. Permutation symmetry

For a hidden layer with

$$
f(x)=W_2\sigma(W_1x)
$$

and a permutation matrix $P$, we have

$$
W_2P^{-1}\sigma(PW_1x)=W_2\sigma(W_1x)
$$

This equality holds when $\sigma$ applies the same activation function to each coordinate. Applying the coordinate-wise activation after reordering is the same as reordering the result after applying the activation, giving $\sigma(PW_1x)=P\sigma(W_1x)$. The subsequent $W_2P^{-1}$ reverses this order, so $P^{-1}P$ cancels.

Rows of $W_1$ are input weights for the hidden units, and columns of $W_2$ are weights sending those units to the output. Change the corresponding parts of both arrays together to preserve the function. Changing only $W_1$ can leave the new hidden-unit order mismatched with the original readout. Raw weight distance between checkpoints still compares both jointly changed arrays as different coordinate values, so it does not remove this symmetry.

Follow the permutation that moves corresponding parts of both arrays together in the next computation paths.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two ReLU hidden units swap input weights one and minus two together with output weights three and minus one](../../figures/assets/I08/I08-02-paired-hidden-permutation.svg)

<figcaption>Swapping the two hidden units on the left moves their input weights and corresponding output weights together. With the same ReLU applied coordinate-wise, the readout reverses the reordering and preserves the output.</figcaption>
</figure>

## 3. Match function distance to the question

Logit RMSE, KL divergence, accuracy disagreement, and generated-string agreement measure different behaviors. KL between probability distributions is sensitive to direction and support, while accuracy can hide most logit changes. Fix the metric before addressing the research question.

Adding the same constant to every vocabulary logit can increase logit distance while leaving softmax probabilities unchanged. Conversely, increasing the logit gap can change probability concentration even when the top-1 token stays the same. It is therefore not a contradiction for the same two checkpoints to have different distances under a logit metric, a probability metric, and top-1 agreement. What is compared depends on what is considered preserved in the output.

The mathematical example below changes the common offset and logit gap separately.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Softmax token probabilities preserve a common logit offset but change when the logit gap increases despite the same top one token](../../figures/assets/I08/I08-02-output-metric-invariances.svg)

<figcaption>A common offset leaves probabilities unchanged, whereas a larger logit gap changes probabilities even with the same top-1 token. The mathematical example distinguishes the differences compared by the three metrics.</figcaption>
</figure>

## 4. CPU exercise

<!-- I08_EXAMPLE: i08_02_parameter_function_distance -->

Evaluate a ReLU network with two hidden units swapped on the same input grid. The parameter L2 distance is positive, but the function RMSE is 0.

## Common misconceptions

### Misconception 1. A layer with more weight movement learned more

Optimizer scale, parameterization, and symmetries all enter the distance. Without considering behavioral and representation metrics alongside it, the distance does not reveal what was learned.

### Misconception 2. Function distance is uniquely determined

Changing the input distribution or output metric changes function distance. Closeness on OOD inputs is a separate question.

## Exercises

### 1. Calculation

For $\theta_s=(0,0)$ and $\theta_t=(3,4)$, find the parameter L2 distance.

<details><summary>Show solution</summary>

It is $\sqrt{3^2+4^2}=5$.

</details>

### 2. Input distribution

Two functions agree on the training support but differ outside it. What does function distance measured under the training distribution miss?

<details><summary>Show solution</summary>

It misses behavioral differences outside the training support. Function distance measures differences under the chosen distribution, not global equality of functions.

</details>

### 3. Permutation

How must $W_1$ and $W_2$ be changed together when swapping two hidden units?

<details><summary>Show solution</summary>

Permute the rows of $W_1$ and inversely permute the corresponding columns of $W_2$. Only the intermediate coordinate order changes, preserving the output.

</details>

### 4. Metric choice

Two language models have the same top-1 token but different logits. What is their accuracy disagreement?

<details><summary>Show solution</summary>

It is 0. This metric misses changes in confidence and in the ranking of the remaining vocabulary.

</details>

### 5. Critique a claim

Critique the statement, “$d_\theta$ rose abruptly, so a new capability emerged.”

<details><summary>Show solution</summary>

Parameter movement is not a capability metric. Measure function changes and task performance separately on fixed behavioral data.

</details>

### 6. Normalization

Why is it difficult to compare raw L2 weight distances directly between two models of different sizes?

<details><summary>Show solution</summary>

Different parameter counts and scales can make the summed distance structurally larger. Relative changes by layer or function-based metrics are needed.

</details>

## Sources and boundaries for updates

For symmetries in neural-network parameter space and low-loss connections, consult [Lubana et al. (2023)](https://proceedings.mlr.press/v202/lubana23a.html). This lesson addresses the limitations of interpreting raw distance, rather than proposing a distance on a full quotient by symmetries.

## Lesson summary

- Parameter distance and function distance are different estimands.
- Parameter symmetries can produce both a large weight distance and the same function.
- Function distance depends on the input distribution and output metric.
- Record the two kinds of change separately in training-dynamics reports.

## Pass criteria

- Can you define the two distances separately with equations?
- Can you explain an example of permutation symmetry?
- Can you avoid claiming behavioral change from weight movement alone?

## Next lesson

- [I08-03 Representation alignment](I08-03-representation-alignment.md)

## Author checklist

- [x] Parameter distance and function distance are distinguished.
- [x] The symmetry example has been calculated.
- [x] Every exercise has a solution.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Claim strength and prerequisites have been checked.
- [x] Internal links and equations have been checked.
