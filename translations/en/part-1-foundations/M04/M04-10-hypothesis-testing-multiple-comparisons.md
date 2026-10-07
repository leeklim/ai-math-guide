---
id: "M04-10"
title: "Hypothesis testing and multiple comparisons"
part: 1
stage: "M04"
status: "complete"
prerequisites:
  - "M04-06"
  - "M04-07"
  - "M04-09"
estimated_time: "155~185 minutes"
---

# M04-10. Hypothesis testing and multiple comparisons

## Why this lesson matters

Model interpretability experiments ask whether differences between condition means, a neuron's selectivity, or an ablation effect could arise from random sample variation. Hypothesis testing calculates how rare results at least as extreme as the observed statistic would be under a null hypothesis.

Testing hundreds of neurons or layers separately creates more opportunities for small p-values to occur by chance. Multiple-comparison procedures control the accumulation of false positives across the analysis. Read p-values alongside effect sizes and intervals to distinguish statistical detection from the magnitude of a research claim.

## Learning objectives

After completing this lesson, you should be able to:

- Distinguish null hypotheses, alternative hypotheses, and test statistics.
- Interpret one-sided and two-sided p-values as null-distribution tail probabilities.
- Decide whether to reject at a significance level and limit the strength of the conclusion.
- Explain Type I error, Type II error, and power.
- Compare the roles of effect size, confidence intervals, and p-values.
- Calculate Bonferroni corrections and the Benjamini-Hochberg procedure.
- Propose error control and controls appropriate for an exploratory search over many model components.

## Prerequisite check

- Prerequisite: [M04-06 Samples, populations, and sampling distributions](M04-06-samples-populations-sampling-distributions.md)
- Prerequisite: [M04-07 Estimation, bias, and variance](M04-07-estimation-bias-variance.md)
- Prerequisite: [M04-09 Confidence intervals and bootstrap](M04-09-confidence-intervals-bootstrap.md)
- Check: Can you explain sampling distributions and standard errors?
- Check: Can you interpret confidence interval coverage through repeated sampling?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Scope and role |
|---|---|---|---|
| $H_0$ | `H naught` | The reference model or no-effect hypothesis being tested | Null hypothesis |
| $H_1$ | `H one` | An effect or difference hypothesis compared with $H_0$ | Alternative hypothesis |
| $T$ | `T` | A statistic mapping a sample to a measure of extremeness | Has a null distribution |
| $t_{\mathrm{obs}}$ | `t sub obs` | The value of $T$ calculated in the current sample | A fixed number |
| $p$ | `p` | Under $H_0$, the probability of a statistic at least as extreme as the observed value | $0\le p\le1$ |
| $\alpha$ | `alpha` | A rejection threshold chosen in advance to control Type I error | A common example: 0.05 |
| $\beta$ | `beta` | The probability of failing to reject $H_0$ when a specified alternative is true | $0\le\beta\le1$ |
| $1-\beta$ | `one minus beta` | The probability of detecting a specified effect when it exists | Power |
| $m$ | `m` | The number of hypotheses considered together | A positive integer |

## Core concept 1. Hypothesis testing starts with a reference model and a statistic

Hypothesis testing specifies a null hypothesis $H_0$ and an alternative hypothesis $H_1$ about population parameters or distributions. For a two-sided question about a mean difference $\delta$, we can set

\[
H_0:\delta=0,
\qquad
H_1:\delta\ne0
\]

If only a positive effect is of interest, a one-sided alternative $H_1:\delta>0$ can be used. Choosing the direction after seeing the data can increase Type I error beyond the planned level, so the direction is specified before analysis.

A test statistic $T$ standardizes sample differences or summarizes them through ranks. Calculating the observed value's extremeness requires knowing the distribution of $T$ when $H_0$ is true.

## Core concept 2. A p-value is a tail probability under the null hypothesis

For a two-sided test using a symmetric test statistic, the p-value is

\[
p=P_{H_0}\left(
|T|\ge|t_{\mathrm{obs}}|
\right)
\]

It is the probability, assuming the null hypothesis, of a statistic equal to or more extreme than the observed value.

For a right-sided test, use

\[
p=P_{H_0}(T\ge t_{\mathrm{obs}})
\]

The definition of “more extreme” depends on $H_1$ and the test statistic.

The two-sided expression adds the probabilities of both tails with absolute values at least $|t_{\mathrm{obs}}|$. For a continuous null distribution symmetric about 0, these tails have equal probabilities, so their sum can be calculated as twice the right-tail probability. The right-sided test instead counts only the positive direction. An observation far in the negative direction has a large absolute value without making the right-sided p-value small. This is why the direction counted as extreme must be specified first.

A p-value is not $P(H_0\mid\text{data})$. Calculating a posterior probability of the null requires a Bayesian model with a prior and likelihood.

Marking z=2 from Example 1 on the null distribution shows the two regions counted by the two-sided test.

<figure class="lesson-figure" markdown="1">

![Standard-normal null density with both tails beyond minus and plus two shaded for the observed z statistic two and two-sided p-value approximately 0.0455](../../figures/assets/M04/M04-10-two-sided-tail.svg)

<figcaption>The shaded area is a probability for the statistic under the null hypothesis. It counts both regions with absolute values at least as large as the observation, not the probability of the null hypothesis itself.</figcaption>
</figure>

In a right-sided test, equal absolute observed values can give very different areas depending on direction.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The same right-sided null-tail rule applied to observed z values plus two and minus two with p-values approximately 0.02275 and 0.97725](../../figures/assets/M04/M04-10-directional-tail.svg)

<figcaption>Both panels count the region to the right of the observed position. A large negative observation does not give a small p-value for a right-sided test of a positive alternative.</figcaption>
</figure>

## Core concept 3. The significance level sets the rejection rule

Choose a significance level $\alpha$ before analysis. Reject $H_0$ if

\[
p\le\alpha
\]

If $p>\alpha$, fail to reject $H_0$.

Failure to reject does not prove that $H_0$ is true. With a small sample or high noise, power can be too low to detect a meaningful effect. Conversely, large samples can give small p-values for small effects.

Report an effect estimate and confidence interval with the test conclusion. They describe the effect's magnitude and the precision of its estimation.

Before sampling, a p-value is itself a statistic calculated from a sample. A valid p-value satisfies the repeated-sampling condition $P_{H_0}(p\le\alpha)\le\alpha$ under $H_0$. Using $p\le\alpha$ as the rejection rule therefore keeps the probability of rejecting a true $H_0$ at most $\alpha$. This is an error rate across repeated samples when the null is true, not the probability that one already-rejected result is wrong.

## Core concept 4. Type I error, Type II error, and power count different outcomes

The test decision and true state can be organized as follows.

| True state | Reject $H_0$ | Fail to reject $H_0$ |
|---|---|---|
| $H_0$ true | Type I error | Correct decision |
| $H_1$ true | Correct detection | Type II error |

The probability of Type I error is

\[
P(\text{reject }H_0\mid H_0\text{ true})
\]

which a valid test controls at or below $\alpha$. Under a specified alternative, Type II error has probability $\beta$, and power is

\[
1-\beta
=P(\text{reject }H_0\mid H_1\text{ true})
\]

Power depends on effect size, sample size, variability, and $\alpha$. A smaller $\alpha$ reduces false positives but can lower power under the same other conditions.

Applying the same rejection region to distributions under two true states shows that Type I error and power are different conditional probabilities.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![One right-sided rejection cutoff 1.645 under a null normal distribution centered at zero and a specific alternative centered at 2.5, shading Type I error under the null and Type II error and power under the alternative](../../figures/assets/M04/M04-10-null-alternative-errors.svg)

<figcaption>The upper orange area is an error when the null is true; the lower orange area is a missed detection when this particular alternative is true. The same rejection rule is evaluated under different conditional distributions. The lower power value is not shared by all effect sizes.</figcaption>
</figure>

## Core concept 5. Statistical significance and effect size answer different questions

A p-value describes the extremeness of the observed result under $H_0$. Effect size describes the magnitude of the difference of interest. A confidence interval gives a range of plausible effects accounting for sampling uncertainty.

A mean difference of $0.001$ can give a small p-value in a large sample. A difference of $0.2$ can give a wide interval and a large p-value if the sample is small and variance is high. Whether a change in model behavior is meaningful must be assessed separately using the task metric and intervention cost.

In a mean-difference test, dividing the observed difference by its standard error expresses it in multiples of sampling variation. For a fixed observed difference, decreasing the standard error moves the standardized statistic farther from the null value and decreases the tail probability. Under repeated sampling with a fixed true effect, a smaller standard error also increases the chance of reaching the rejection region. This explains increased power without increasing the effect size in the original metric.

Separating differences in the original metric from multiples of standard error makes it possible to show a small significant effect and a large uncertain effect together.

<figure class="lesson-figure" markdown="1">

![Illustrative 95 percent z intervals for effect 0.05 with standard error 0.01 and effect 0.20 with standard error 0.20 on the same effect axis](../../figures/assets/M04/M04-10-effect-precision.svg)

<figcaption>The upper difference is 0.05 with SE 0.01, placing it 5 standard errors from the null. The lower difference is 0.20 with SE 0.20, placing it 1 standard error away. The larger lower effect has the larger p-value. These are assumed illustrative numbers, not measured model effects.</figcaption>
</figure>

## Core concept 6. Multiple comparisons create more opportunities for false positives

Suppose all $m$ null hypotheses are true, each test has Type I error probability exactly $\alpha$, and the test results are independent. The family-wise error rate (FWER), the probability of at least one false positive, is

\[
1-(1-\alpha)^m
\]

For $m=20$ and $\alpha=0.05$,

\[
1-0.95^{20}\approx0.642
\]

Even without independence, interpreting one raw p-value after searching many tests must account for the entire selection procedure.

Each test has probability $1-\alpha$ of no false positive. Under independence, the probability of no errors in all $m$ tests is $(1-\alpha)^m$; its complement is the event of at least one error. If the actual error probabilities are only known to be at most $\alpha$, the expression above is an upper bound under independence, not necessarily an equality.

Bonferroni correction tests each hypothesis at level

\[
\alpha_{\mathrm{per\ test}}=\frac{\alpha}{m}
\]

It controls FWER at or below $\alpha$ regardless of dependence between hypotheses, but can lower power when $m$ is large.

The event of any error is the union of error events for the true null hypotheses. A union's probability is at most the sum of its events' probabilities. With at most $m$ true hypotheses and each error probability at most $\alpha/m$, the total error probability is at most $m(\alpha/m)=\alpha$. This bound does not use independence and provides the Bonferroni guarantee.

Under the text's assumption of independent tests with all nulls true, the family error probability can be compared exactly across numbers of tests.

<figure class="lesson-figure" markdown="1">

![Independent all-null family-wise error rate increasing with test count at raw per-test level 0.05 and staying below 0.05 at Bonferroni per-test level 0.05 divided by family size](../../figures/assets/M04/M04-10-family-error.svg)

<figcaption>The orange point is the uncorrected probability of about 0.642 at m=20. The green curve is the exact probability in this independent example. The general Bonferroni guarantee with dependence follows from the union bound in the text.</figcaption>
</figure>

## Core concept 7. FDR controls the false discovery fraction among rejected hypotheses

False discovery rate (FDR) controls the expected fraction of false positives among rejected hypotheses. The Benjamini-Hochberg (BH) procedure uses the following steps.

1. Sort the $m$ p-values as $p_{(1)}\le\cdots\le p_{(m)}$.
2. For target FDR $q$, find the largest $k$ satisfying $p_{(k)}\le kq/m$.
3. Reject the hypotheses corresponding to $p_{(1)},\ldots,p_{(k)}$.

This fraction is random because both the number of rejections and the number of false positives change across samples. Define the fraction as 0 if no hypotheses are rejected, and control its expectation over repeated analyses. Target $q$ is neither the exact false positive fraction in the current discoveries nor the probability of at least one false positive.

The BH threshold $kq/m$ increases with rank. Thus, do not stop at the first rank that fails its condition; find the largest passing $k$ among all ranks. If no rank passes, reject nothing. Once $k$ is found, all earlier p-values are at most $p_{(k)}$ and are rejected together under the single cutoff $kq/m$.

The BH FDR guarantee holds under independence or certain positive dependence conditions. Arbitrary dependence can require a different correction. Choose between FWER and FDR according to the research objective because they control different errors.

If two errors occur among five rejected hypotheses, the error fraction and the presence of any error are different quantities in that same analysis.

<figure class="lesson-figure" markdown="1">

![One illustrative rejected set of five hypotheses with three true and two false discoveries, yielding false-discovery fraction two fifths and any-false-discovery indicator one](../../figures/assets/M04/M04-10-error-fraction-indicator.svg)

<figcaption>This analysis has false discovery fraction 0.4 and an indicator of any error equal to 1. FDR and FWER take expectations of these different quantities over repeated analyses. The current fraction need not equal target q exactly.</figcaption>
</figure>

The largest-rank selection in BH can be checked using Example 4 and a comparison that changes only its first value.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two BH rank plots with four p-values and target q 0.05, both selecting maximum passing rank two, including a variant where the first p-value 0.014 fails its own rank threshold but is still rejected under the final cutoff 0.025](../../figures/assets/M04/M04-10-bh-step-up.svg)

<figcaption>Circles mark ranks that pass their conditions, and × marks failures. Rank two is the last passing rank, so the shaded first two hypotheses are rejected together. On the right, failure at the first rank does not stop the procedure. The point p₄=0.200 lies above the enlarged vertical range and is not visible; it fails the fourth condition.</figcaption>
</figure>

## Core concept 8. Mixing exploration and confirmation on the same data breaks error control

Selecting the smallest p-value among thousands of neurons and reporting it raw hides the selection process. Changing layers, prompt subsets, or metrics after seeing results also increases the actual number of comparisons.

Exploration can identify candidates and describe effect patterns. Confirmation uses independent data and prespecified hypotheses, metrics, and corrections. Replicating a discovered component on new prompts and seeds and testing it through interventions can assess functional claims stronger than statistical association.

Distinguish data used to select candidates from data used to confirm the fixed claim so that the selection procedure is accounted for in evaluation.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Data A used for searching candidate neurons layers and metrics, frozen choices passed to confirmation on new data B not used for selection with a prespecified correction](../../figures/assets/M04/M04-10-explore-confirm-separation.svg)

<figcaption>After exploration, fix the hypothesis, metric, and correction and confirm using new data. Reusing the lower data for candidate selection breaks this separation of roles. Independent confirmation alone does not prove the model's causal use of a component.</figcaption>
</figure>

## Example 1. A one-sample z test

### Problem

Test $H_0:\mu=1$ against $H_1:\mu\ne1$. The sample is iid Gaussian with known population standard deviation $\sigma=1$, $n=25$, and $\bar x=1.4$. Calculate the z statistic and two-sided p-value, and make a decision at $\alpha=0.05$. Write the standard normal CDF as $\Phi$ and use $\Phi(2)=0.97725$.

### Solution

The standard error is

\[
\frac{\sigma}{\sqrt n}
=\frac1{5}=0.2
\]

The test statistic is

\[
z=\frac{\bar x-1}{0.2}
=\frac{0.4}{0.2}
=2
\]

The two-sided p-value is

\[
p=2P(Z\ge2)
=2[1-\Phi(2)]
=2(1-0.97725)
=0.0455.
\]

Since $0.0455<0.05$, reject $H_0$.

### Meaning of the result

Under the null, the probability of a result with $|Z|\ge2$ is about 4.55%. This is not the probability that $H_0$ is true.

## Example 2. A confidence interval for the same test

The 95% z interval is

\[
1.4\pm1.96(0.2)
=1.4\pm0.392
=[1.008,1.792]
\]

Excluding the null value 1 corresponds to rejection in the two-sided $\alpha=0.05$ z test. This interval is for the mean $\mu$. If the effect is reported as the difference $\mu-1$ from the reference, the estimate is $0.4$. Subtracting 1 from both endpoints gives the difference interval $[0.008,0.792]$.

## Example 3. Bonferroni correction

To test 20 neurons while controlling overall FWER at $0.05$, set each test's threshold to

\[
\frac{0.05}{20}=0.0025
\]

A raw p-value of $0.01$ passes the single-test $0.05$ criterion but fails the Bonferroni criterion.

## Example 4. The BH procedure

Suppose the four p-values are

\[
0.001,\quad0.020,\quad0.040,\quad0.200
\]

and the target FDR is $q=0.05$. The BH thresholds are

\[
0.0125,\quad0.025,\quad0.0375,\quad0.050
\]

The first two p-values pass their conditions, and the third fails because $0.040>0.0375$. The largest $k$ is 2. Reject the first two hypotheses.

## Common misconceptions

### Misconception 1. A p-value is the probability that the null hypothesis is true

A p-value is a conditional probability assuming $H_0$. The conditioning directions in $P(\text{data extremity}\mid H_0)$ and $P(H_0\mid\text{data})$ differ.

### Misconception 2. $p>0.05$ means the two conditions are equal

Failure to reject means the data did not supply enough information to detect a difference. Claiming equivalence requires an acceptable range of differences and an appropriate test or interval.

### Misconception 3. A small p-value implies a large effect

A p-value depends on how an effect estimate compares with its standard error. In a large sample, a small effect can have a small p-value.

### Misconception 4. An effect that is not significant after correction does not exist

Multiple-comparison correction strengthens error control and can reduce power. Report estimates and intervals together to assess the effect range supported by the data.

### Misconception 5. The same p-value in an independent dataset proves causation

Replicated association weakens an explanation based on chance sampling results. Causal effects require interventions and controls.

## Exercises

### 1. Specify hypotheses

You want a two-sided test of whether the mean accuracy difference $\delta$ between two models is 0. Write $H_0$ and $H_1$.

<details>
<summary>Show solution</summary>

\[
H_0:\delta=0,
\qquad
H_1:\delta\ne0.
\]

The test is two-sided, so both positive and negative differences count as extreme results.

</details>

### 2. Interpret a p-value

You obtain $p=0.03$. Explain it in terms of the null hypothesis and observed statistic.

<details>
<summary>Show solution</summary>

Assuming $H_0$ and the test assumptions hold, the probability of a result equal to or more extreme than the observed statistic is 3%. It does not mean that the null hypothesis itself has probability 3% of being true.

</details>

### 3. Type I and Type II errors

Name the error of concluding that an effect exists when it does not, and the error of failing to detect an effect when it exists.

<details>
<summary>Show solution</summary>

Rejecting the null when no effect exists and $H_0$ is true is a Type I error. Failing to reject $H_0$ when an effect exists and $H_1$ is true is a Type II error.

</details>

### 4. Change in power

Explain how increasing iid sample size affects power when effect size and variance are held fixed.

<details>
<summary>Show solution</summary>

Increasing sample size decreases the estimator's standard error, placing the same effect more standard errors from the null value. With other conditions unchanged, power increases.

</details>

### 5. Bonferroni threshold

You test 100 hypotheses and want to control FWER at $0.05$. Calculate the Bonferroni per-test threshold.

<details>
<summary>Show solution</summary>

\[
\alpha_{\mathrm{per\ test}}
=\frac{0.05}{100}
=0.0005.
\]

</details>

### 6. The BH procedure

The sorted p-values are $(0.004,0.018,0.070)$, with $q=0.06$. Determine which hypotheses the BH procedure rejects.

<details>
<summary>Show solution</summary>

Since $m=3$, the thresholds are

\[
0.02,\quad0.04,\quad0.06
\]

The first and second p-values are at most their respective thresholds; the third fails because $0.070>0.06$. The largest passing rank is $k=2$, so reject the first two hypotheses.

</details>

### 7. Design a model interpretability analysis

A researcher tests 12 layers with 500 neurons in each, then reports neurons with raw $p<0.05$ as “concept neurons.” Explain the problem and how to improve the analysis.

<details>
<summary>Show solution</summary>

Using a raw threshold across 6,000 tests accumulates false positives. State the hypothesis family tested and apply FWER or FDR correction. Recheck discoveries on an independent dataset. Beyond selectivity, use interventions such as ablation and patching to assess whether the model uses the component.

</details>

## Lesson summary

- Hypothesis testing specifies a null hypothesis, alternative hypothesis, test statistic, and null distribution.
- A p-value is the null-distribution tail probability of a statistic at least as extreme as the observation.
- The significance level sets a rejection threshold controlling Type I error; failure to reject does not prove the null.
- Power is the probability of rejecting the null when a specified effect exists.
- P-values, effect sizes, and confidence intervals provide different information.
- Bonferroni correction controls FWER, and BH controls FDR under its conditions.
- Hiding explored hypotheses and selection procedures breaks false positive control.

## Pass criteria

You pass if you can answer the following without consulting the material.

- Can you define $H_0$, $H_1$, and a test statistic?
- Can you read one-sided and two-sided p-values as null-tail probabilities?
- Can you distinguish Type I error, Type II error, and power?
- Can you distinguish statistical significance from effect size?
- Can you calculate a Bonferroni threshold?
- Can you identify the hypotheses rejected by BH?
- Can you design error control and replication for a search over many components?

## Next lesson

- [M04-11 Likelihood and maximum likelihood estimation](M04-11-likelihood-maximum-likelihood.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] P-values are defined as null-tail probabilities.
- [x] Type I error, Type II error, and power are distinguished.
- [x] Effect sizes and intervals are explained together.
- [x] Bonferroni and BH calculations are checked.
- [x] Data separation between exploration and confirmation is explained.
- [x] Every exercise has a solution.
- [x] Strengths of model interpretability claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] No knowledge beyond the prerequisites is silently required.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
