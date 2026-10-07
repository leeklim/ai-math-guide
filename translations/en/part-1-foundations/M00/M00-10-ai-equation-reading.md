---
id: "M00-10"
title: "AI formula reading practice"
part: 1
stage: "M00"
status: "complete"
prerequisites:
  - "M00-03"
  - "M00-05"
  - "M00-06"
  - "M00-09"
estimated_time: "120~150 minutes"
---

# M00-10. AI formula reading practice

## Why this lesson matters

Formulas in papers use the symbols from earlier lessons together. Function inputs and outputs, sample and class indices, exponentials and logarithms, means, and vector and matrix shapes can all appear on one line. Reading the symbols from left to right alone can obscure the role of each term and the order of computation.

This lesson reads a classification model's mean loss in three stages.

\[
\mathbf x_n
\longmapsto
\mathbf z_n
\longmapsto
p_\theta(c\mid\mathbf x_n)
\longmapsto
-\log p_\theta(y_n\mid\mathbf x_n)
\longmapsto
\mathcal L(\theta)
\]

You will learn a procedure for identifying the symbols, ranges, shapes, order of computation, and scope of conclusions in an unfamiliar formula.

## Learning objectives

After completing this lesson, you will be able to:

- Organize the symbols and indices in an AI formula into a table.
- Explain the order of computation for an affine classifier, softmax, and mean loss.
- Check the shape of each intermediate value and the bounds of each sum.
- Calculate probabilities and mean loss from a small set of logits.
- Distinguish what a decrease in loss directly supports from claims requiring further evidence.
- Apply the same reading procedure to a knowledge-distillation loss.

## Prerequisite check

- [M00-03 Function inputs and outputs](M00-03-functions-input-output.md)
- [M00-05 Exponents and logarithms](M00-05-exponents-logarithms.md)
- [M00-06 Indices and summation notation](M00-06-indices-summation.md)
- [M00-09 Shapes of scalars, vectors, and matrices](M00-09-scalars-vectors-matrices-shape.md)

Check that you can answer these four questions.

1. What roles do $\mathbf x$ and $\theta$ play in $f_\theta(\mathbf x)$?
2. What condition must $a$ satisfy for $\exp(\log a)=a$ to hold?
3. What does $\frac1N\sum_{n=1}^{N}\ell_n$ calculate?
4. For $\mathbf W\in\mathbb R^{C\times d}$ and $\mathbf x\in\mathbb R^d$, what is the dimension of $\mathbf W\mathbf x$?

## Formulas used in this lesson

Let $\mathbf x_n$ be the input for sample $n$ and $y_n$ its correct class. The classification model first computes logits.

\[
\mathbf z_n
=
\mathbf W\mathbf x_n+\mathbf b
\]

It computes each class probability using softmax.

\[
p_\theta(c\mid\mathbf x_n)
=
\frac{\exp(z_{n,c})}
{\displaystyle\sum_{j=1}^{C}\exp(z_{n,j})}
\]

The dataset's mean loss is the mean negative logarithm of the correct-class probability.

\[
\mathcal L(\theta)
=
-\frac1N
\sum_{n=1}^{N}
\log p_\theta(y_n\mid\mathbf x_n)
\]

The parameters are collected as

\[
\theta=(\mathbf W,\mathbf b)
\]

The loss formula is the cross entropy used in multiclass classification, written using the correct-class index.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $N$ | `N` | Number of samples | A positive integer |
| $C$ | `C` | Number of classes | A positive integer |
| $d$ | `d` | Input feature dimension | A positive integer |
| $n$ | `n` | Sample index | $1,\ldots,N$ |
| $c,j$ | `c and j` | Class indices | $1,\ldots,C$ |
| $\mathbf x_n$ | `x sub n` | The $n$th input | $\mathbb R^d$ |
| $y_n$ | `y sub n` | The $n$th correct-class index | $\{1,\ldots,C\}$ |
| $\mathbf W$ | `W` | Weight matrix | $\mathbb R^{C\times d}$ |
| $\mathbf b$ | `b` | Bias vector | $\mathbb R^C$ |
| $\mathbf z_n$ | `z sub n` | Logit vector for the $n$th sample | $\mathbb R^C$ |
| $z_{n,c}$ | `z sub n c` | The logit for class $c$ on sample $n$ | A scalar |
| $p_\theta(c\mid\mathbf x_n)$ | `p sub theta of c given x sub n` | The model probability assigned to class $c$ | $0<p_\theta\le1$ |
| $\mathcal L(\theta)$ | `L of theta` | Mean loss over $N$ samples | A scalar |

## Reading step 1. Separate the outputs defined by each equality

The three formulas define outputs at different stages.

\[
\mathbf z_n
=
\mathbf W\mathbf x_n+\mathbf b
\]

maps an input vector to a logit vector.

\[
p_\theta(c\mid\mathbf x_n)
=
\frac{\exp(z_{n,c})}
{\sum_{j=1}^{C}\exp(z_{n,j})}
\]

uses every component of the logit vector to compute the probability of one class of interest. The numerator selects one class's score, but the denominator uses the scores of all classes for the same sample.

\[
\mathcal L(\theta)
=
-\frac1N
\sum_{n=1}^{N}
\log p_\theta(y_n\mid\mathbf x_n)
\]

combines the per-sample probabilities into one loss.

Before combining the formulas into a single line, identify the object on the left of each equality. $\mathbf z_n$ is a vector, $p_\theta(c\mid\mathbf x_n)$ is a scalar, and $\mathcal L(\theta)$ is also a scalar.

## Reading step 2. Record the role and range of each index

These formulas use both sample and class indices.

- $n$: specifies which sample is being evaluated.
- $c$: specifies the class whose probability is being read.
- $j$: a dummy index summing over all classes in the softmax denominator.

$c$ and $j$ can range over the same values $1,\ldots,C$, but they play different roles. $c$ remains on the left of the formula to indicate which probability was computed. $j$ changes only inside the sum and disappears after summation.

In the mean-loss sum, $n$ is a dummy index.

\[
\sum_{n=1}^{N}
\log p_\theta(y_n\mid\mathbf x_n)
\]

For each sample, this selects its correct-class probability and adds the logarithms.

## Reading step 3. Check shapes

Start with the logit formula. Because

\[
\mathbf W\in\mathbb R^{C\times d},
\qquad
\mathbf x_n\in\mathbb R^d
\]

the matrix-vector product has shape

\[
(C\times d)(d\times1)
\longrightarrow
(C\times1)
\]

Thus,

\[
\mathbf W\mathbf x_n\in\mathbb R^C
\]

and $\mathbf b\in\mathbb R^C$, so the two vectors can be added.

\[
\mathbf z_n\in\mathbb R^C
\]

The logit component $z_{n,c}$ is one entry of the vector, so it is a scalar. The probability $p_\theta(c\mid\mathbf x_n)$ computed using exponentiation and summation is also a scalar.

The final loss formula adds $N$ scalars and divides by $N$, so its output is a scalar.

## Reading step 4. Expand the softmax numerator and denominator

Let $C=3$. The probability of class $2$ is

\[
p_\theta(2\mid\mathbf x_n)
=
\frac{\exp(z_{n,2})}
{\exp(z_{n,1})+\exp(z_{n,2})+\exp(z_{n,3})}
\]

The numerator is the exponentiated score of the class of interest. The denominator sums the exponentiated scores of all classes. Exponentiation produces positive values, so each probability is positive.

For a fixed sample $n$, every class probability has the same denominator. Dividing each positive score by the same total gives each class's share of that total. Using this common denominator makes the shares of all classes sum to 1.

Summing every class probability gives

\[
\sum_{c=1}^{C}
p_\theta(c\mid\mathbf x_n)
=
\frac{
\sum_{c=1}^{C}\exp(z_{n,c})
}{
\sum_{j=1}^{C}\exp(z_{n,j})
}
=1
\]

Although the numerator and denominator use different dummy-index letters, both sum over the same range of classes.

### Adding a common constant leaves the probabilities unchanged

Adding the same constant $a$ to every logit gives

\[
\frac{\exp(z_{n,c}+a)}
{\sum_{j=1}^{C}\exp(z_{n,j}+a)}
\]

Applying the exponent rule gives

\[
=
\frac{\exp(a)\exp(z_{n,c})}
{\exp(a)\sum_{j=1}^{C}\exp(z_{n,j})}
\]

The common factor $\exp(a)$ cancels, so the softmax probabilities do not change.

This property means that differences between class logits, rather than their absolute level, determine the probabilities.

The following figure adds log 3 to every logit, multiplying every exponentiated score by 3. The three segments in each bar retain the same class order.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three class scores two one one become six three three under common scaling, but dividing by their own totals preserves probabilities one half one quarter one quarter](../../figures/assets/M00/M00-10-softmax-common-scaling.svg)

<figcaption>The denominator increases by the same factor, from 4 to 12. The upper two bars show the unnormalized scores, while the lower bar shows probability shares summing to 1. Whichever class is selected, the total of its score bar is the common denominator.</figcaption>
</figure>

## Reading step 5. Read the per-sample loss

Define the $n$th sample's loss as

\[
\ell_n
=
-\log p_\theta(y_n\mid\mathbf x_n)
\]

Because $y_n$ is the correct-class index,

\[
p_\theta(y_n\mid\mathbf x_n)
\]

is the probability the model assigns to the correct class.

$y_n$ is substituted into the probability formula's class-index position $c$. First calculate every class probability for sample $n$, then select the entry at the correct-class index and take its logarithm. Changing the target changes the selected probability and loss even for the same logit vector.

If the correct-class probability is close to $1$, $\ell_n$ is close to $0$. If the correct-class probability is close to $0$, the negative logarithm is large.

For example,

\[
-\log0.9\approx0.105
\]

\[
-\log0.1\approx2.303
\]

The prediction assigning $0.1$ to the correct class has the larger loss.

Softmax outputs positive probabilities, satisfying the logarithm's input condition

\[
p_\theta(y_n\mid\mathbf x_n)>0
\]

In the following graph, use the correct-class probability p as the logarithm's input and read the per-sample loss on the vertical axis.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Negative log loss falls toward zero as correct-class probability approaches one, with probabilities point one and point nine giving losses about two point three zero three and point one zero five](../../figures/assets/M00/M00-10-negative-log-loss.svg)

<figcaption>The same probability difference produces a larger loss difference near 0. The value p=0 is not a valid input to the logarithm; the graph includes only positive probabilities.</figcaption>
</figure>

## Reading step 6. Identify what is being averaged

The total loss is

\[
\mathcal L(\theta)
=
\frac1N\sum_{n=1}^{N}\ell_n
\]

It averages the per-sample losses with equal weights.

A decrease in the mean does not establish that every $\ell_n$ decreased. Some samples' losses can increase while others decrease by more. The mean summarizes the distribution of per-sample values as one scalar.

In the notation $\mathcal L(\theta)$, the input and target dataset for this mean is fixed, and the parameters appear explicitly as the function's input. Changing $\theta$ can change each sample's predicted probabilities and therefore the mean loss. Summing over sample index $n$ and changing parameters $\theta$ serve different purposes.

Changing the dataset can change the mean loss even with the same $\theta$. When reading a paper, check whether the calculation uses training, validation, or test data.

The following graph is an illustrative example showing that a decrease in mean loss differs from improvement on every sample. It is not a model experiment result.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two losses change from two and two to three and point five, so the first sample worsens even though their mean decreases from two to one point seven five](../../figures/assets/M00/M00-10-mean-loss-tradeoff.svg)

<figcaption>The green dashed line shows the sample mean. Sample 1's loss increases from 2 to 3, but the larger decrease for sample 2 lowers the mean from 2 to 1.75.</figcaption>
</figure>

## A complete calculation example

### Setup

Set the sample count and class count to

\[
N=2,\qquad C=2
\]

The targets are

\[
y_1=1,\qquad y_2=2
\]

and the logits are

\[
\mathbf z_1=
\begin{bmatrix}
\log3\\
0
\end{bmatrix},
\qquad
\mathbf z_2=
\begin{bmatrix}
\log3\\
0
\end{bmatrix}
\]

### The first sample

Because

\[
\exp(\log3)=3,\qquad \exp(0)=1
\]

we have

\[
p_\theta(1\mid\mathbf x_1)
=
\frac{3}{3+1}
=
\frac34
\]

The first sample's correct class is $1$, so

\[
\ell_1
=
-\log\frac34
\]

### The second sample

The logits are the same, so the class probabilities are also the same.

\[
p_\theta(2\mid\mathbf x_2)
=
\frac{1}{3+1}
=
\frac14
\]

The second sample's correct class is $2$, so

\[
\ell_2
=
-\log\frac14
\]

### The mean loss

\[
\mathcal L(\theta)
=
\frac12(\ell_1+\ell_2)
\]

\[
=
-\frac12
\left(
\log\frac34+\log\frac14
\right)
\]

Using the logarithm's product rule gives

\[
=
-\frac12\log\frac{3}{16}
\]

\[
=
\frac12\log\frac{16}{3}
\approx0.837
\]

The two samples received the same logits, but their different correct classes produced different correct-class probabilities and per-sample losses.

The following figure separates selection of an entry along the class axis from averaging along the sample axis.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two identical class-probability rows select different entries according to targets one and two, producing losses about point two eight eight and one point three eight six and mean about point eight three seven](../../figures/assets/M00/M00-10-class-selection-sample-mean.svg)

<figcaption>Select the probability at the correct-class index in each row to obtain a scalar loss. Then average the two row losses into one scalar. Correct-class selection and sample summation operate along different axes.</figcaption>
</figure>

## Reading the same calculation in batch notation

Stacking inputs as rows gives

\[
\mathbf X
\in
\mathbb R^{N\times d}
\]

The logit matrix can be written as

\[
\mathbf Z
=
\mathbf X\mathbf W^\top
+
\mathbf 1\mathbf b^\top
\in
\mathbb R^{N\times C}
\]

- Row $n$: sample $n$
- Column $c$: class $c$
- Entry $z_{n,c}$: the logit for class $c$ on sample $n$

Applying softmax along the class axis of each row gives the probability matrix

\[
\mathbf P\in\mathbb R^{N\times C}
\]

Each row sums to $1$. The phrase “apply softmax” can omit which axis is normalized, so check both shape and axis.

## A reusable procedure for reading formulas

When you encounter an unfamiliar AI formula, read it in this order.

1. Identify the object newly defined on the left of each equality.
2. Record the meanings and ranges of symbols and indices in a table.
3. Mark the shapes of scalars, vectors, matrices, and tensors.
4. Expand sums over a small range to identify dummy indices.
5. Work outward from the inner parentheses to identify the order of function composition.
6. Check domain conditions for logarithms, division, and inverse functions.
7. Substitute small numbers to check numerical values and output ranges.
8. Separate claims directly supported by the calculation from claims requiring further experiments.

You can apply this procedure without knowing the formula's name. Even if later lessons cover the underlying theory, you can first identify the objects and the structure of the operations.

## Reading a knowledge-distillation loss with the same notation

Let the teacher's class distribution be $p_T(c\mid\mathbf x_n)$ and the student's be $p_S(c\mid\mathbf x_n)$. One form of a knowledge-distillation loss for matching output distributions is

\[
\mathcal L_{\mathrm{KD}}
=
-\frac1N
\sum_{n=1}^{N}
\sum_{c=1}^{C}
p_T(c\mid\mathbf x_n)
\log p_S(c\mid\mathbf x_n)
\]

Read the symbols in the following order.

1. Select one sample $n$.
2. For each class $c$, use the teacher's probability as a weight.
3. Calculate the logarithm of the class probability assigned by the student.
4. Sum over all classes and change the sign to obtain a per-sample loss.
5. Average over all samples.

The inner sum is a weighted mean of the student's class losses $-\log p_S(c\mid\mathbf x_n)$, using the teacher's probabilities as weights. The teacher's probabilities are nonnegative and sum to 1 over all classes. A loss calculated from one correct-class index selects a single class term. This formula instead evaluates several class terms together according to the shares assigned by the teacher. If the teacher assigns probability 1 to one class and 0 to the others, only that class's negative log loss remains.

The following figure illustrates one sample with teacher probabilities (3/4, 1/4) and student probabilities (1/4, 3/4).

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Teacher probabilities three quarters and one quarter weight the student's class losses negative log one quarter and negative log three quarters, and the two contributions sum to about one point one one two](../../figures/assets/M00/M00-10-kd-class-weighting.svg)

<figcaption>Multiply each teacher weight by the student loss for the same class. Add the two class terms weighted by the teacher. The full distillation loss then averages these per-sample values.</figcaption>
</figure>

This formula uses only teacher and student output distributions, so it can be computed without access to the teacher's internal activations. If the teacher's per-class probabilities are available, it can implement black-box distillation. An API providing only the final class index does not supply enough information to compute this formula as written.

White-box distillation can add terms matching intermediate representations or attention in the teacher and student. For example,

\[
\mathcal L_{\mathrm{total}}
=
\mathcal L_{\mathrm{KD}}
+
\lambda\mathcal L_{\mathrm{rep}}
\]

combines an output loss with a representation loss. $\lambda$ is a hyperparameter setting the two terms' relative weights.

A small representation loss means that the two intermediate values are close under the chosen representations and alignment method. Concluding that the student uses the same internal algorithm as the teacher requires further interventions and functional checks.

In the following figure, solid lines mark output-distribution comparison, while dashed lines mark the additional comparison of intermediate representations.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The same input passes through teacher and student hidden representations to output distributions, solid links compare outputs and optional dashed links compare hidden representations in a separate loss](../../figures/assets/M00/M00-10-distillation-access-paths.svg)

<figcaption>The output loss on the right can be computed if teacher probabilities p_T are available. The representation loss on the left requires access to the teacher's internal h_T and suitable alignment. The two losses compare different observed objects.</figcaption>
</figure>

Distillation temperature, KL divergence, and representation alignment are covered in separate lessons after the prerequisites in M04 and later stages.

## Common misconceptions

### Misconception 1. $z_{n,c}$ is a probability

$z_{n,c}$ is a logit before softmax. It can be negative or greater than $1$, and the logits need not sum to $1$ over all classes.

### Misconception 2. The softmax denominator includes only the correct class

The denominator sums the exponentiated logits of all classes.

\[
\sum_{j=1}^{C}\exp(z_{n,j})
\]

The correct class is used when selecting $p_\theta(y_n\mid\mathbf x_n)$ for the loss.

### Misconception 3. The minus sign in $-\log p$ makes the probability negative

Compute the logarithm first, then change its sign. For $0<p\le1$, we have $\log p\le0$, so $-\log p\ge0$.

### Misconception 4. A low mean loss means every sample's loss is low

The mean summarizes several samples as one number. The distribution and maximum of per-sample losses require separate checks.

### Misconception 5. A low training loss means the model's explanation is true

Training loss evaluates how well predictions match their targets under the specified data and objective. The model's internal mechanism, the faithfulness of an explanation text, and generalization to external data require separate evidence.

## Exercises

### 1. Classify symbol roles

Identify the sample index, class index, vectors, matrix, and scalar outputs in the following formulas.

\[
\mathbf z_n=\mathbf W\mathbf x_n+\mathbf b,
\qquad
\mathcal L(\theta)
=
-\frac1N\sum_{n=1}^{N}
\log p_\theta(y_n\mid\mathbf x_n)
\]

<details>
<summary>Show solution</summary>

$n$ is the sample index. $y_n$ is the correct-class index, but no dummy index summing over classes appears explicitly in this formula.

$\mathbf x_n$, $\mathbf b$, and $\mathbf z_n$ are vectors. $\mathbf W$ is a matrix. $p_\theta(y_n\mid\mathbf x_n)$, the per-sample logarithms, and the final $\mathcal L(\theta)$ are scalars.

</details>

### 2. Expand a softmax denominator

For $C=4$, write the denominator of

\[
p_\theta(3\mid\mathbf x_n)
=
\frac{\exp(z_{n,3})}
{\sum_{j=1}^{4}\exp(z_{n,j})}
\]

without summation notation.

<details>
<summary>Show solution</summary>

\[
\sum_{j=1}^{4}\exp(z_{n,j})
=
\exp(z_{n,1})
+\exp(z_{n,2})
+\exp(z_{n,3})
+\exp(z_{n,4})
\]

The term for class $3$ is also included in the denominator.

</details>

### 3. Check shapes

Let $d=5$ and $C=3$, using the column-vector convention. Give the shapes of $\mathbf x_n$, $\mathbf W$, $\mathbf b$, and $\mathbf z_n$ that make the following calculation valid.

\[
\mathbf z_n=\mathbf W\mathbf x_n+\mathbf b
\]

<details>
<summary>Show solution</summary>

\[
\mathbf x_n\in\mathbb R^5
\]

\[
\mathbf W\in\mathbb R^{3\times5}
\]

\[
\mathbf b\in\mathbb R^3
\]

\[
\mathbf z_n\in\mathbb R^3
\]

The matrix-vector product has shape

\[
(3\times5)(5\times1)
\longrightarrow
(3\times1)
\]

The bias and output also have dimension $3$.

</details>

### 4. Calculate softmax

For one sample with logits

\[
\mathbf z=
\begin{bmatrix}
\log2\\
0\\
0
\end{bmatrix}
\]

find the softmax probabilities of all three classes.

<details>
<summary>Show solution</summary>

\[
\exp(\log2)=2,\qquad
\exp(0)=1
\]

The denominator is

\[
2+1+1=4
\]

so

\[
p(1)=\frac24=\frac12
\]

\[
p(2)=\frac14,\qquad
p(3)=\frac14
\]

The three probabilities sum to $1$.

</details>

### 5. Correct classes and per-sample losses

Use the probabilities from Exercise 4. Write the per-sample loss when the correct class is $1$ and when it is $2$, and determine which loss is larger.

<details>
<summary>Show solution</summary>

If the correct class is $1$, then

\[
\ell_{y=1}
=
-\log\frac12
\]

If the correct class is $2$, then

\[
\ell_{y=2}
=
-\log\frac14
\]

Because

\[
\frac14<\frac12
\]

and the negative logarithm gives larger values to smaller probabilities,

\[
-\log\frac14>-\log\frac12
\]

The loss is larger when class $2$ is correct.

</details>

### 6. Calculate mean loss

Suppose the correct-class probabilities of three samples are

\[
\frac12,\qquad \frac14,\qquad 1
\]

Write their mean negative log loss as a sum of logarithms and simplify it.

<details>
<summary>Show solution</summary>

\[
\mathcal L
=
-\frac13
\left(
\log\frac12+\log\frac14+\log1
\right)
\]

Since $\log1=0$, applying the logarithm's product rule gives

\[
\mathcal L
=
-\frac13\log\left(\frac12\cdot\frac14\right)
\]

\[
=
-\frac13\log\frac18
=
\frac13\log8
\]

Because $\log8=3\log2$,

\[
\mathcal L=\log2
\]

</details>

### 7. Find an incorrect formula

Using the column-vector convention, someone specifies

\[
\mathbf x_n\in\mathbb R^d,
\qquad
\mathbf W\in\mathbb R^{d\times C},
\qquad
\mathbf b\in\mathbb R^C
\]

and computes

\[
\mathbf z_n=\mathbf W\mathbf x_n+\mathbf b
\]

Find and correct the shape error.

<details>
<summary>Show solution</summary>

With the given shapes,

\[
(d\times C)(d\times1)
\]

has mismatched inner dimensions $C$ and $d$. To multiply the input from the left, the weight matrix must have shape

\[
\mathbf W\in\mathbb R^{C\times d}
\]

Then

\[
(C\times d)(d\times1)
\longrightarrow
(C\times1)
\]

and the result can be added to $\mathbf b\in\mathbb R^C$.

</details>

### 8. Interpret a distillation formula and its claims

For

\[
\mathcal L_{\mathrm{KD}}
=
-\frac1N
\sum_{n=1}^{N}
\sum_{c=1}^{C}
p_T(c\mid\mathbf x_n)
\log p_S(c\mid\mathbf x_n)
\]

explain:

1. The ranges of the two sums
2. The roles of teacher and student probabilities
3. Whether a small value of this loss alone establishes that the teacher and student use the same internal mechanism

<details>
<summary>Show solution</summary>

The outer sum runs over $N$ samples, and the inner sum runs over $C$ classes.

$p_T(c\mid\mathbf x_n)$ provides a weight for each class. $p_S(c\mid\mathbf x_n)$ is the probability the student assigns to class $c$ and appears inside the logarithm. The formula evaluates the student distribution against the teacher distribution and then computes the sample mean.

A small loss shows that the two output distributions are close under this metric on the evaluated inputs. It does not support the conclusion that internal activations, circuits, or algorithms are the same. Comparing internal mechanisms requires interventions and functional checks in addition to representation alignment.

</details>

## Lesson summary

- Read a complex formula by separating the output of each equality, indices, shapes, and order of computation.
- An affine classifier maps inputs to $C$-dimensional logits, and softmax maps logits to class probabilities.
- Mean negative log loss is a scalar averaging the evaluation of each sample's correct-class probability.
- A decrease in mean loss does not guarantee improvement on every sample, generalization, or a particular internal mechanism.
- The same reading procedure distinguishes output-distribution terms from representation-alignment terms in a distillation loss.

## M00 stage pass criteria

You pass M00 if you can answer these questions without consulting the material.

- Can you classify every symbol in a formula as an input, output, parameter, index, or constant?
- Can you expand a sum over a small range?
- Can you check the domain conditions for logarithms and division?
- Can you check the shapes of vector and matrix operations?
- Can you explain the order of function composition?
- Can you distinguish claims directly supported by numerical results from claims requiring further evidence?

## Next stage

The next lesson is [M01-01 Changes and average rates of change](../M01/M01-01-change-average-rate.md). You will compare changes between two inputs and begin calculating graph slopes using formulas.

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] All symbols, indices, and shapes are defined before use.
- [x] The softmax denominator and the sum used for the mean are explicitly expanded.
- [x] Probabilities and losses in the complete numerical example have been checked.
- [x] Every exercise has a solution.
- [x] Claims about training loss, generalization, and internal mechanisms are distinguished.
- [x] The information-access requirements of black-box and white-box knowledge distillation are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
