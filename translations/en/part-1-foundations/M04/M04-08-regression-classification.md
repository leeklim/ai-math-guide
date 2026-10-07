---
id: "M04-08"
title: "Regression and classification"
part: 1
stage: "M04"
status: "complete"
prerequisites:
  - "M02-09"
  - "M04-02"
  - "M04-05"
  - "M04-07"
estimated_time: "150–175 minutes"
---

# M04-08. Regression and classification

## Why this lesson matters

Regression and classification are statistical problems predicting target $Y$ from input $X$. Regression predicts numerical targets; classification predicts categorical targets or their conditional probabilities. The same linear layers or neural networks can serve either task, but their output spaces, losses, and evaluation criteria differ.

In model interpretability, probes are also formulated as regression or classification problems. Interpreting a high probe score requires knowing the target, the loss minimized, and the data split used for evaluation.

## Learning objectives

After completing this lesson, you should be able to:

- Distinguish regression and classification by target support and prediction output.
- Read population risk and empirical risk mathematically.
- Explain why the optimal regression function under squared loss is the conditional mean.
- Determine a Bayes classifier under 0-1 loss from conditional class probabilities.
- Calculate outputs of linear, logistic, and softmax regression.
- Calculate regression and classification metrics from a small table and assess class imbalance.
- Limit the representation claims supported by probe performance.

## Prerequisite check

- Prerequisite lesson: [M02-09 Orthogonal bases and projection](../M02/M02-09-orthogonal-basis-projection.md)
- Prerequisite lesson: [M04-02 Conditional probability and Bayes' rule](M04-02-conditional-probability-bayes-rule.md)
- Prerequisite lesson: [M04-05 Common distributions](M04-05-common-distributions.md)
- Prerequisite lesson: [M04-07 Estimation, bias, and variance](M04-07-estimation-bias-variance.md)
- Check: Can you explain a least-squares solution as a projection?
- Check: Can you read Bernoulli and categorical conditional distributions?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $X$ | `X` | Predictor or feature | $X\in\mathcal X$ |
| $Y$ | `Y` | The numerical value or class to predict | Regression: $\mathbb R$; classification: $\{1,\ldots,K\}$ |
| $f$ | `f` | A function mapping inputs to predictions or scores | Output depends on the task |
| $\ell(y,f(x))$ | `ell of y and f of x` | A scalar function comparing target and prediction | Often $\ell\ge0$ |
| $R(f)$ | `R of f` | Expected loss in the target population | $\mathbb E[\ell(Y,f(X))]$ |
| $\widehat R_n(f)$ | `R hat sub n of f` | Mean loss over the observed sample | $n^{-1}\sum_i\ell(y_i,f(x_i))$ |
| $\eta_k(x)$ | `eta sub k of x` | $P(Y=k\mid X=x)$ | $\sum_k\eta_k(x)=1$ |
| residual | `residual` | Observed target minus regression prediction | $e_i=y_i-\hat y_i$ |

## Core concept 1. Regression and classification have different target value spaces

Regression predicts a numerical value when $Y$ is real-valued or a real vector. Examples include temperature, distance traveled the next day, and a particular activation component.

Classification predicts a class label or conditional class probabilities when $Y$ belongs to a finite class set. Binary classification has $Y\in\{0,1\}$; multiclass classification has $Y\in\{1,\ldots,K\}$.

Interpret outputs using both the task and output parameterization. A regression model producing one scalar might predict a conditional mean, whereas one producing a mean and variance might represent a conditional Gaussian distribution. A classifier's logits are not probabilities; sigmoid or softmax converts them to a probability vector.

## Core concept 2. Learning minimizes an approximation to population risk

Given prediction function $f$ and loss $\ell$, population risk is

\[
R(f)=\mathbb E_{(X,Y)\sim P}
\left[\ell(Y,f(X))\right]
\]

Expectation is taken over the target population's joint distribution $P$. Since this distribution is not fully known, empirical risk is calculated from an observed sample:

\[
\widehat R_n(f)
=\frac1n\sum_{i=1}^{n}
\ell(y_i,f(x_i)).
\]

Empirical risk minimization chooses

\[
\widehat f
\in\operatorname*{argmin}_{f\in\mathcal F}
\widehat R_n(f)
\]

from candidate function class $\mathcal F$. Low training risk means low loss on that sample. Population risk is also affected by the function class, optimization, and differences between training and test distributions.

Using presampling random variables $X_i,Y_i$ in the formula makes empirical risk a function of a random sample. For a function $f$ fixed in advance and samples from the same distribution $P$, each loss has expectation $R(f)$, so mean loss also has expectation $R(f)$. However, $\widehat f$ chosen by comparing losses on those data depends on the sample. Distinguish estimating a fixed function's mean loss from evaluating performance after selecting a function from the data.

The finite-population example below calculates losses for the same two candidate functions on the observed sample and target population separately.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two candidate prediction functions compared on observed training pairs zero zero and one one and on four equally weighted population pairs including two zero and three one](../../figures/assets/M04/M04-08-empirical-selection.svg)

<figcaption>f performs better on the two observed points, but g has lower risk in the population assigning equal probability to four points. This is one constructed possible sample, not actual training results or general performance figures.</figcaption>
</figure>

## Core concept 3. The optimal regression function under squared loss is the conditional mean

Suppose regression uses squared loss

\[
\ell(y,a)=(y-a)^2
\]

Consider a specified conditional distribution at input $x$ with a finite conditional second moment. A single continuous-input point can have probability 0, so do not automatically insert this distribution into the previous lesson's formula dividing by event probability $P(X=x)$. Here, the input-specific conditional distribution is taken as given. Fix input $X=x$ and set $m(x)=\mathbb E[Y\mid X=x]$:

\[
\begin{aligned}
\mathbb E[(Y-a)^2\mid X=x]
&=\mathbb E[(Y-m(x)+m(x)-a)^2\mid X=x]\\
&=\operatorname{Var}(Y\mid X=x)
+(m(x)-a)^2.
\end{aligned}
\]

The conditional mean's definition makes the cross term 0. The first term is independent of $a$, and the second is minimized at $a=m(x)$, so

\[
f^*(x)=\mathbb E[Y\mid X=x]
\]

This justifies interpreting squared-loss regression predictions as conditional-mean predictions. The learned $f$ can differ from $f^*$ if its function class cannot represent this value or optimization is insufficient.

With $x$ fixed, $m(x)$ and candidate prediction $a$ are constants in the conditional expectation. The cross term's expectation is therefore $2(m(x)-a)\mathbb E[Y-m(x)\mid X=x]=0$. This is the same centering calculation as the previous lesson's MSE decomposition, now within one input's conditional distribution. Conditional variance is the remaining target variation and cannot be removed by changing the prediction. The reducible term is $(m(x)-a)^2$; minimizing it at each input also minimizes total risk weighted by the input distribution.

In Example 1's conditional distribution, moving the prediction adds squared distance from the center to variance 3, which cannot be removed.

<figure class="lesson-figure" markdown="1">

![Exact conditional squared risk three plus prediction-minus-three squared with minimum at mean three rather than most probable target four](../../figures/assets/M04/M04-08-conditional-squared-loss.svg)

<figcaption>The gray dashed line is irreducible conditional variance. Squared loss is lower at conditional mean 3 than at the most frequently observed value 4. The calculation is within one fixed input.</figcaption>
</figure>

## Core concept 4. The optimal classifier under 0-1 loss chooses the largest conditional probability

Let multiclass 0-1 loss be

\[
\ell(y,k)=\mathbf 1\{y\ne k\}
\]

At $X=x$, the conditional risk of predicting class $k$ is

\[
P(Y\ne k\mid X=x)=1-\eta_k(x)
\]

Minimize it by choosing a class with the largest $\eta_k(x)$:

\[
f^*(x)
\in\operatorname*{argmax}_{k}
P(Y=k\mid X=x).
\]

For binary classification with equal costs for the two errors, the threshold is $0.5$. Different false-negative and false-positive costs can change the optimal threshold.

The 0-1 loss indicator is 1 when incorrect and 0 when correct, so its conditional expectation is error probability. In the binary case, if class 1 has probability $p$, predicting class 1 or class 0 gives risks $1-p$ and $p$, respectively. Solving $1-p\le p$ gives $p\ge0.5$, the equal-cost threshold. Equal risks or tied multiclass probabilities can give multiple optimal classes, which is why the formula uses $\in$.

Plotting the binary risks on the same axes makes the threshold the intersection of the two error probabilities.

<figure class="lesson-figure" markdown="1">

![Conditional error risks p for predicting zero and one minus p for predicting one intersecting at one half under equal error costs](../../figures/assets/M04/M04-08-binary-conditional-risk.svg)

<figcaption>Given probability p, choose the class corresponding to the lower line. At p=0.5, both choices have equal risk. With different error costs, the two lines themselves must be recalculated.</figcaption>
</figure>

## Core concept 5. Linear regression approximates the conditional mean by a linear combination of features

For $\mathbf x\in\mathbb R^d$, linear regression uses

\[
f_{\beta_0,\boldsymbol\beta}(\mathbf x)
=\beta_0+\boldsymbol\beta^\top\mathbf x
\]

Minimizing squared loss on the observed sample gives ordinary least squares (OLS).

$\beta_0$ is a scalar intercept independent of the input, and $\boldsymbol\beta\in\mathbb R^d$ contains feature coefficients. Stack observed features as rows and prepend a column of constant 1s to combine intercept and coefficient calculations in one matrix expression. Finding the prediction vector closest to the target vector within this matrix's column space is the least-squares projection problem of M02-09. The positive loss multiplier $1/n$ does not change the optimal coefficients.

\[
(\widehat\beta_0,\widehat{\boldsymbol\beta})
\in\operatorname*{argmin}_{\beta_0,\boldsymbol\beta}
\frac1n\sum_{i=1}^{n}
\left(y_i-\beta_0-\boldsymbol\beta^\top\mathbf x_i\right)^2.
\]

The residual is

\[
e_i=y_i-f_{\widehat\beta_0,\widehat{\boldsymbol\beta}}(\mathbf x_i)
\]

Interpreting a coefficient's sign as a causal effect requires additional research-design and confounder conditions. OLS coefficients describe conditional linear relationships for the selected features and sample.

In projection, the residual vector is orthogonal to the selected column space. Including the constant-1 column makes the residuals sum to 0. This condition follows from minimizing squared error on the sample; it does not mean future residuals are 0. Linearly dependent columns can also allow multiple coefficient combinations with the same prediction vector.

A residual is the vertical difference between observation and prediction at the same input, not a distance along the input axis.

<figure class="lesson-figure" markdown="1">

![Illustrative ordinary least-squares fitted line one point five plus one half x with observed targets one three two at inputs zero one two and signed vertical residual arrows](../../figures/assets/M04/M04-08-ols-residuals.svg)

<figcaption>Orange arrows run from predictions to observations. Residuals are −0.5, 1, and −0.5; they sum to 0 and have zero inner product with the input vector. These sample orthogonality conditions do not mean all future targets are predicted correctly.</figcaption>
</figure>

## Core concept 6. Logistic and softmax regression parameterize conditional class probabilities

Binary logistic regression feeds the logit

\[
z=\mathbf w^\top\mathbf x+b
\]

into sigmoid:

\[
p_\theta(Y=1\mid\mathbf x)
=\sigma(z)
=\frac{1}{1+e^{-z}}.
\]

Thus,

\[
\log\frac{p_\theta(Y=1\mid\mathbf x)}
{1-p_\theta(Y=1\mid\mathbf x)}
=\mathbf w^\top\mathbf x+b
\]

The feature combination specifies log-odds, and sigmoid converts them to probability.

Writing sigmoid as $p=e^z/(1+e^z)$ gives $1-p=1/(1+e^z)$. Their odds ratio is $p/(1-p)=e^z$, whose logarithm is $z$. The linear quantity is therefore log-odds, not probability itself.

Placing Example 2's logit on the sigmoid curve shows the conversion from a real-valued score to probability.

<figure class="lesson-figure" markdown="1">

![Sigmoid mapping an unrestricted real logit to probability with the exact example logit log three mapped to probability three quarters](../../figures/assets/M04/M04-08-sigmoid-logit.svg)

<figcaption>The horizontal axis is log-odds; the vertical axis is probability. Equal logit increments do not produce equal probability changes everywhere. Dashed lines mark the correspondence between log(3) and 0.75.</figcaption>
</figure>

Multiclass softmax regression calculates

\[
\mathbf z=\mathbf W\mathbf x+\mathbf b
\in\mathbb R^K
\]

and produces categorical probabilities by

\[
p_\theta(Y=k\mid\mathbf x)
=\frac{e^{z_k}}{\sum_{j=1}^{K}e^{z_j}}
\]

Adding the same constant to every logit leaves softmax probabilities unchanged.

Each exponential is positive, and the denominator is their sum, so probabilities are positive and sum to 1. Adding a constant $c$ to every logit gives $e^{z_k+c}=e^c e^{z_k}$, and multiplies every denominator term by $e^c$ as well. Canceling the common factor leaves the original probabilities. Probabilities therefore reflect differences between classes rather than a common logit shift.

A common logit shift becomes a common scale factor on all exponentials, which cancels in normalization.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Logits zero log two log three and a common log-five shift giving exponentials one two three and five ten fifteen which normalize to the same one-sixth two-sixths three-sixths class masses](../../figures/assets/M04/M04-08-softmax-common-shift.svg)

<figcaption>The upper exponential vectors differ in values and totals, but each component has the same share of its total. The lower bar widths show probabilities of three classes, not probabilities of logits themselves.</figcaption>
</figure>

## Core concept 7. Evaluation metrics summarize different kinds of error

Regression mean squared error gives large residuals a squared penalty; mean absolute error uses absolute values:

\[
\operatorname{MSE}
=\frac1n\sum_{i=1}^{n}(y_i-\hat y_i)^2,
\]

\[
\operatorname{MAE}
=\frac1n\sum_{i=1}^{n}|y_i-\hat y_i|.
\]

Calculating squared and absolute values for the same residual shows the different penalties assigned to large errors.

<figure class="lesson-figure" markdown="1">

![Squared and absolute per-observation penalties plotted against a dimensionless signed residual](../../figures/assets/M04/M04-08-residual-penalties.svg)

<figcaption>Each curve is a penalty for one observation. Averaging over observations gives regression MSE or MAE, respectively. For targets with physical units, the metrics also have different units, so their numerical magnitudes should not be compared directly.</figcaption>
</figure>

A binary-classification confusion matrix counts true positives (TP), false positives (FP), false negatives (FN), and true negatives (TN):

\[
\operatorname{accuracy}
=\frac{TP+TN}{TP+FP+FN+TN},
\]

\[
\operatorname{precision}
=\frac{TP}{TP+FP},
\qquad
\operatorname{recall}
=\frac{TP}{TP+FN}.
\]

With substantial class imbalance, predicting only the majority class can yield high accuracy. Choose metrics according to the errors to reduce and the class base rates.

$TP+FP$ counts all predicted positives; $TP+FN$ counts all actual positives. Precision is the correct proportion in the first group, while recall is the identified proportion in the second. A zero denominator leaves the ratio undefined by these formulas, so report the handling rule used in evaluation.

This section's regression MSE is mean loss over observed target-prediction pairs. M04-07's estimator MSE was the repeated-sampling mean squared error between an estimator and a fixed parameter. Both average squared errors, but the objects and distributions averaged over differ.

Example 3's confusion matrix shows which group serves as the denominator for the same TP count.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The same confusion matrix counts thirty true positives twenty false negatives ten false positives and forty true negatives, selecting the predicted-positive column for precision and actual-positive row for recall](../../figures/assets/M04/M04-08-confusion-denominators.svg)

<figcaption>The blue column is predicted positives; the orange row is actual positives. Dividing the same TP count of 30 by 40 or 50 gives different precision and recall. Cell areas do not represent counts; the numbers give observation counts.</figcaption>
</figure>

## Core concept 8. A probe provides supervised-prediction results

A probe predicting concept label $Y$ from activation $H$ is a regression or classification model. A high held-out probe score shows that the chosen probe class can recover information related to $Y$ from $H$.

This result does not provide intervention evidence that the original model uses that information. Report probe capacity, train-test split, class imbalance, and baselines together. Repeated input tokens or shared sources across splits can make scores reflect data leakage rather than representation information.

Drawing the probe as a separate branch from the original model's computational path shows where recovery results and model-use claims diverge.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Activation feeding an original model continuation and a separately fitted supervised probe on different branches with different outputs](../../figures/assets/M04/M04-08-probe-readout-branch.svg)

<figcaption>Even if the probe predicts concept labels well, this figure does not establish that the original model on the left uses that information. Evaluating use requires interventions on the original path and measurements of output changes.</figcaption>
</figure>

## Example 1. Check the conditional mean under squared loss

### Problem

At a fixed $x$, $Y=0$ has probability $0.25$ and $Y=4$ probability $0.75$. Calculate the conditional mean and compare expected squared losses for predictions $a=3$ and $a=4$.

### Solution

The conditional mean is

\[
\mathbb E[Y\mid X=x]
=0(0.25)+4(0.75)
=3
\]

The risk for $a=3$ is

\[
0.25(0-3)^2+0.75(4-3)^2
=2.25+0.75
=3
\]

For $a=4$,

\[
0.25(0-4)^2+0.75(4-4)^2
=4
\]

### Meaning of the result

The most frequent value is 4, but the optimal point prediction under squared loss is conditional mean 3.

## Example 2. Calculate a logistic probability

If $\mathbf w^\top\mathbf x+b=\log 3$,

\[
p_\theta(Y=1\mid\mathbf x)
=\frac{1}{1+e^{-\log3}}
=\frac{1}{1+1/3}
=\frac34.
\]

The odds are $3:1$, and the probability is $0.75$.

## Example 3. Calculate metrics from a confusion matrix

Let $TP=30$, $FP=10$, $FN=20$, and $TN=40$. The sample has 100 observations, so

\[
\operatorname{accuracy}=\frac{30+40}{100}=0.70.
\]

The correctness of positive predictions is

\[
\operatorname{precision}=\frac{30}{30+10}=0.75
\]

and the identified proportion of actual positives is

\[
\operatorname{recall}=\frac{30}{30+20}=0.60
\]

The three metrics have different denominators.

## Example 4. A majority-class baseline

Suppose evaluation data contain 95% class 0 and 5% class 1. Predicting class 0 on every input gives 95% accuracy but class-1 recall 0. Interpret probe accuracy alongside a majority-class baseline and class-specific metrics.

## Common misconceptions

### Misconception 1. Regression is a linear model and classification is a neural network

Regression and classification distinguish targets and prediction tasks. Both linear models and neural networks can perform either task.

### Misconception 2. Low training loss implies low population risk

Training loss is empirical risk on the observed training sample. New-data performance depends on sampling variation, overfitting, and distribution shift.

### Misconception 3. Linear-regression coefficients are feature causal effects

Coefficients describe conditional linear relationships with the target for the chosen features and sample. Causal interpretation requires interventions or a design addressing confounding.

### Misconception 4. A logit is a probability

A logit can take any real value. Sigmoid or softmax produces probabilities in $[0,1]$ satisfying the relevant sum condition.

### Misconception 5. High probe accuracy proves the model uses the concept

Probe accuracy is recovery evidence that labels can be predicted from a representation. Claiming functional use by the original model requires activation interventions and measurements of output effects.

## Exercises

### 1. Distinguish tasks

Classify these targets as regression or classification and give their supports: tomorrow's temperature, one of six document topics, and the number of objects in an image.

<details>
<summary>Show solution</summary>

Temperature is real-valued regression, with support in an appropriate range of $\mathbb R$. Topic is multiclass classification with support $\{1,\ldots,6\}$. Object count is count prediction on $\{0,1,2,\ldots\}$; it can be predicted numerically as in regression, or modeled with a count distribution.

</details>

### 2. Empirical risk

Regression targets are $(1,2,4)$ and predictions $(2,2,3)$. Calculate MSE and MAE.

<details>
<summary>Show solution</summary>

Residuals are $(-1,0,1)$, so

\[
\operatorname{MSE}=\frac{1+0+1}{3}=\frac23,
\]

\[
\operatorname{MAE}=\frac{1+0+1}{3}=\frac23.
\]

The values coincide in this example, but the metrics assign different penalties when residual magnitudes differ.

</details>

### 3. Optimal regression prediction

$Y\mid X=x$ takes value 1 with probability $0.6$ and value 6 with probability $0.4$. Calculate the optimal point prediction under squared loss.

<details>
<summary>Show solution</summary>

The optimal squared-loss point prediction is the conditional mean:

\[
f^*(x)=1(0.6)+6(0.4)=0.6+2.4=3.
\]

</details>

### 4. Bayes classifier

At one input, conditional class probabilities are $(0.2,0.5,0.3)$. Calculate the predicted class and conditional error probability under equal-cost 0-1 loss.

<details>
<summary>Show solution</summary>

Predict class 2, with the largest probability $0.5$. Its correctness probability is $0.5$, so conditional error probability is

\[
1-0.5=0.5
\]

</details>

### 5. Logistic regression

For logit $z=0$, calculate $p(Y=1\mid x)$. State the predicted class with threshold $0.5$ and ties assigned to class 1.

<details>
<summary>Show solution</summary>

\[
\sigma(0)=\frac{1}{1+e^0}=\frac12.
\]

The specified tie rule predicts class 1.

</details>

### 6. Confusion-matrix metrics

Given $TP=18$, $FP=6$, $FN=2$, and $TN=24$, calculate accuracy, precision, and recall.

<details>
<summary>Show solution</summary>

The total is 50, so

\[
\operatorname{accuracy}=\frac{18+24}{50}=0.84.
\]

\[
\operatorname{precision}=\frac{18}{18+6}=0.75,
\qquad
\operatorname{recall}=\frac{18}{18+2}=0.90.
\]

</details>

### 7. Critique a probe claim

A linear probe predicting topic labels from activations achieves 99% training accuracy. State what this supports and what additional evaluation is needed.

<details>
<summary>Show solution</summary>

Training accuracy shows only that the probe fits the training activations and labels well. Assess information recovery by comparing held-out scores with baselines and checking that sources or documents do not overlap across splits. Claiming that the original model uses topic information additionally requires activation interventions and measurements of output changes.

</details>

## Lesson summary

- Regression predicts numerical targets; classification predicts categorical targets or conditional class probabilities.
- Population risk is expected loss under the target distribution; empirical risk is mean loss over the observed sample.
- The optimal regression function under squared loss is the conditional mean.
- A Bayes classifier under 0-1 loss chooses a class with the greatest conditional probability.
- Linear regression approximates the conditional mean with a linear function; logistic and softmax regression parameterize class probabilities.
- Metrics differ in the denominators used to count errors and in their penalties.
- High probe scores are evidence of information recovery, which must be distinguished from functional use.

## Pass criteria

You pass if you can answer these questions without consulting the material.

- Can you distinguish regression and classification by target support?
- Can you read population and empirical risk mathematically?
- Can you derive the optimal predictor under squared loss?
- Can you calculate a Bayes classifier under 0-1 loss?
- Can you distinguish linear, logistic, and softmax regression outputs?
- Can you calculate regression and classification metrics and examine class imbalance?
- Can you limit the claims supported by a probe score?

## Next lesson

- [M04-09 Confidence intervals and bootstrap](M04-09-confidence-intervals-bootstrap.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Regression and classification are distinguished by target support.
- [x] Population risk and empirical risk are defined.
- [x] Optimal predictors for squared loss and 0-1 loss are derived.
- [x] Linear, logistic, and softmax regression are explained.
- [x] Metrics and class imbalance are examined through calculations.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretability claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] No prerequisites outside the stated scope are required implicitly.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
