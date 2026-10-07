---
id: "M04-02"
title: "Conditional probability and Bayes' rule"
part: 1
stage: "M04"
status: "complete"
prerequisites:
  - "M04-01"
estimated_time: "135–160 minutes"
---

# M04-02. Conditional probability and Bayes' rule

## Why this lesson matters

New information restricts the possible outcomes. Knowing that a classifier returned a positive result, that a particular token was given, or that an activation fell in a certain interval can change the probability of an event of interest. Conditional probability provides a rule for calculating this change.

Bayes' rule expresses the probability of $A$ given $B$ using the probability of $B$ given $A$ and the base rate. Reading this formula is necessary to avoid reversing the conditioning direction when interpreting test performance, classification results, or probe scores.

## Learning objectives

After completing this lesson, you should be able to:

- Interpret the numerator and denominator of conditional probability as events.
- Calculate probabilities using the multiplication rule and law of total probability.
- Derive Bayes' rule and calculate it from a small table or tree.
- Distinguish independence from mutual exclusivity.
- Distinguish event independence from conditional independence.
- Keep the likelihood and posterior directions distinct.
- Determine whether a high conditional probability implies functional use or causation.

## Prerequisite check

- Prerequisite lesson: [M04-01 Events and probability](M04-01-events-probability.md)
- Check: Can you read the intersection $A\cap B$ and complement event $A^c$ in words?
- Check: Can you calculate the probability of two events' union using inclusion-exclusion?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Conditions |
|---|---|---|---|
| $P(A\mid B)$ | `P of A given B` | The probability of $A$ under the condition that $B$ occurred | $P(B)>0$ |
| prior | `prior` | The probability of the event of interest before incorporating new evidence | $P(A)$ in the relevant context |
| likelihood | `likelihood` | The probability of evidence $B$ under cause or hypothesis $A$ | $P(B\mid A)$ in event notation |
| posterior | `posterior` | The probability of event $A$ after incorporating evidence $B$ | $P(A\mid B)$ |
| partition | `partition` | A collection of disjoint events whose union is the sample space | $A_i\cap A_j=\varnothing$ |
| independence | `independence` | A relation in which knowing one event does not change the probability of the other | $P(A\cap B)=P(A)P(B)$ |

## Core concept 1. Conditional probability measures a proportion within the conditioning event

For $P(B)>0$, define conditional probability by

\[
P(A\mid B)
=\frac{P(A\cap B)}{P(B)}
\]

The denominator $P(B)$ is the total probability satisfying the condition. The numerator $P(A\cap B)$ is the probability within it that also satisfies $A$.

Conditioning excludes outcomes outside $B$ and divides the remaining probabilities within $B$ by $P(B)$ so that their total becomes 1. Indeed, $P(\Omega\mid B)=P(B)/P(B)=1$. Dividing each outcome's probability within $B$ by the same number preserves their probability ratios. Conditioning does not make the remaining outcomes equally probable. If $P(B)=0$, this division cannot define conditional probability.

For a fair die, $A=\{2,4,6\}$ is the even-result event and $B=\{4,5,6\}$ is the event of a result at least 4. Knowing that $B$ occurred restricts the possible outcomes to $\{4,5,6\}$. The even outcomes among them are $\{4,6\}$, so

\[
P(A\mid B)
=\frac{P(\{4,6\})}{P(\{4,5,6\})}
=\frac{2/6}{3/6}
=\frac23
\]

$P(A\mid B)$ and $P(B\mid A)$ condition on different events, so their values can differ. The event to the right of the vertical bar is the condition currently known.

Starting from the previous lesson's mass assignment $0.6,0.3,0.1$, retain only $B=\{b,c\}$. Dividing by the same denominator preserves the ratio of the two masses.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Original outcome masses 0.6, 0.3 and 0.1 filtered to b and c and rescaled by their total 0.4 into conditional masses 0.75 and 0.25](../../figures/assets/M04/M04-02-conditioning-renormalizes.svg)

<figcaption>Mass outside the condition is excluded, and the retained bar expands to total probability 1. The same scale factor applies to both retained outcomes, so they do not become equally probable.</figcaption>
</figure>

## Core concept 2. The multiplication rule breaks an intersection into an ordered calculation

Multiplying both sides of the conditional-probability definition by $P(B)$ gives

\[
P(A\cap B)=P(A\mid B)P(B)
\]

Conditioning in the other direction gives

\[
P(A\cap B)=P(B\mid A)P(A)
\]

Therefore,

\[
P(A\mid B)P(B)=P(B\mid A)P(A)
\]

The first direction requires $P(B)>0$; the reverse direction requires $P(A)>0$. When both conditional probabilities appear in one equation, check both denominator conditions. This calculation order does not imply that one event occurred earlier in time or caused the other. It specifies which condition is used first to calculate the same intersection.

For three events, a chain-form multiplication rule is available:

\[
P(A\cap B\cap C)
=P(C\mid A\cap B)P(B\mid A)P(A).
\]

Each factor gives the probability of the next event under the condition that the preceding events have occurred.

Use this chain form when $P(A\cap B)>0$. First write $P(A\cap B\cap C)=P(C\mid A\cap B)P(A\cap B)$, then apply the two-event multiplication rule to the final intersection to obtain three factors. When a conditioning event has probability 0, its conditional term cannot be calculated by this definition. Do not write the formula by multiplying an undefined term by 0.

In the illustrative model below, selecting either event first retains the same intersection mass $0.1$.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two proportional mass partitions selecting A then B given A or B then A given B, both retaining intersection mass 0.1](../../figures/assets/M04/M04-02-intersection-two-directions.svg)

<figcaption>The first bar selects one quarter of A's mass; the second selects one half of B's mass. The conditional proportions differ, but the intersection mass is the same. This selection order is neither temporal nor causal.</figcaption>
</figure>

## Core concept 3. The law of total probability adds the possible paths

Let $A_1,\ldots,A_K$ partition the sample space. To use the conditional terms below, first assume every $P(A_k)>0$. A partition piece with probability 0 also has probability 0 in its intersection with $B$, so omit that piece from the sum.

Event $B$ splits into disjoint pieces:

\[
B=(B\cap A_1)\cup\cdots\cup(B\cap A_K)
\]

Additivity and the multiplication rule give

\[
P(B)
=\sum_{k=1}^{K}P(B\cap A_k)
=\sum_{k=1}^{K}P(B\mid A_k)P(A_k)
\]

This is the law of total probability.

For the two paths $A$ and $A^c$,

\[
P(B)=P(B\mid A)P(A)+P(B\mid A^c)P(A^c)
\]

A classifier's positive output can arise from both actual-positive and actual-negative groups, so both terms must be calculated.

Multiply each path's conditional probability by that path's proportion, then add. If the groups differ in size, the two conditional probabilities must not be averaged with equal weights. In Example 1, $0.9$ and $0.2$ have weights $0.1$ and $0.9$, respectively, and those weights sum to 1.

Separating Example 1's positive results by their two starting groups shows where each group's proportion enters the multiplication.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two disjoint population paths with group masses 0.1 and 0.9 weighted by positive rates 0.9 and 0.2 to contribute 0.09 and 0.18 to total positive probability 0.27](../../figures/assets/M04/M04-02-total-probability-paths.svg)

<figcaption>Along each path, multiply the group's proportion by its positive rate. Across paths, add the disjoint contributions. A group with a lower positive rate can contribute more positive results if its starting population is larger.</figcaption>
</figure>

## Core concept 4. Bayes' rule reverses the conditioning direction

The multiplication rule gives

\[
P(A\cap B)=P(B\mid A)P(A)
\]

and the conditional-probability definition gives

\[
P(A\mid B)=\frac{P(A\cap B)}{P(B)}
\]

Substitute the first equation into the second:

\[
P(A\mid B)
=\frac{P(B\mid A)P(A)}{P(B)}
\]

Expanding the denominator by the law of total probability for two cases gives

\[
P(A\mid B)
=\frac{P(B\mid A)P(A)}
{P(B\mid A)P(A)+P(B\mid A^c)P(A^c)}
\]

$P(A)$ is the prior, $P(B\mid A)$ is the likelihood term, and $P(A\mid B)$ is the posterior. $P(B)$ is the total probability of evidence $B$ across all possible causal paths.

Use this formula when $P(B)>0$ and $P(A)>0$ so that the likelihood term is defined. The numerator $P(B\mid A)P(A)$ is the proportion of the entire population in which both $A$ and $B$ occur. Dividing by the entire proportion where $B$ occurs converts it to a proportion within the conditioning group. In Example 1, $0.09$ is this joint proportion and $0.27$ is the proportion defining the new reference group, giving $0.09/0.27=1/3$.

### Visual intuition: Conditioning changes the reference group

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A prior population filtered into true positives and false positives that form the observed positive group](../../figures/assets/M04/M04-02-bayes-population.svg)

<figcaption>Given observation B, the new denominator is the group producing B, rather than the whole population. It contains both true positives from A and false positives from A's complement.</figcaption>
</figure>

The left side shows the population before observation, so the proportion of $A$ is the prior $P(A)$. The two middle boxes show the paths producing $B$ from each group. On the right, collecting only cases producing $B$ makes the proportion of $A\cap B$ within that group the posterior $P(A\mid B)$.

Do not read only the numerator. Even with high sensitivity $P(B\mid A)$, much of the right-hand group can come from $A^c$ if the $A^c$ group is much larger or the false-positive rate is large enough. This is why Bayes' rule's denominator $P(B)$ counts the base rate and all alternative paths together.

## Core concept 5. Independence means that knowing one event does not change the other's probability

If events $A$ and $B$ are independent,

\[
P(A\cap B)=P(A)P(B)
\]

For $P(B)>0$, this condition can also be written

\[
P(A\mid B)=P(A)
\]

Knowing that $B$ occurred does not change the probability of $A$.

Substitute the intersection product into the conditional-probability definition to obtain $P(A\mid B)=P(A)P(B)/P(B)=P(A)$. Conversely, if the conditional probability equals $P(A)$, multiply both sides by $P(B)$ to recover the definition of independence. The intersection and product of marginal probabilities are unchanged when $A,B$ are exchanged, so independence is symmetric. The conditional expression applies only to a positive denominator, whereas the product definition also applies to probability-zero events.

Independence differs from mutual exclusivity. Mutually exclusive events with positive probabilities have $P(A\cap B)=0$ but $P(A)P(B)>0$, so they are not independent. Knowing that one occurs makes the other impossible.

Putting the two cases in Example 3 side by side separates two questions: whether events can occur together, and whether knowing one preserves the other's probability.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Four equal-probability coin outcomes with an independent overlapping event pair compared with disjoint die singleton events whose conditional probability becomes zero](../../figures/assets/M04/M04-02-independent-exclusive.svg)

<figcaption>The independent events above can occur together at HH. For the mutually exclusive events below, knowing one makes the other's probability 0, changing it from its original positive probability.</figcaption>
</figure>

## Core concept 6. Conditional independence holds with a common condition fixed

For $P(C)>0$, events $A$ and $B$ are conditionally independent given $C$ if

\[
P(A\cap B\mid C)
=P(A\mid C)P(B\mid C)
\]

Two related events in the whole population can be independent within subgroup $C$. Conversely, events independent in the whole population can become related when the population is divided by some condition.

A conditional-independence claim must specify the conditioning event. $A\perp B$ and $A\perp B\mid C$ are different claims.

The equation applies the previous section's independence definition after remeasuring probability within $C$. If $P(B\cap C)>0$, it can also be expressed as

\[
P(A\mid B\cap C)
=\frac{P(A\cap B\cap C)}{P(B\cap C)}
=\frac{P(A\cap B\mid C)}{P(B\mid C)}
=P(A\mid C)
\]

The middle fraction divides its numerator and denominator by the same $P(C)$. The final step substitutes the conditional-independence product and cancels $P(B\mid C)$. Thus, once $C$ is known, learning $B$ does not change the probability of $A$. This does not assert the same equality for probabilities without $C$ fixed.

The illustrative model below mixes $C$ and its complement in equal proportions. Independence within each group does not necessarily preserve the same product in the pooled population.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two independent conditional probability mosaics with event rates 0.8 and 0.2 pooled equally into a dependent joint distribution with intersection probability 0.34 instead of 0.25](../../figures/assets/M04/M04-02-conditional-independence-pooling.svg)

<figcaption>Within each group, B occupies the same height whether A is known or not. In the pooled group, B's heights on the A and complement sides differ. The four cell areas are joint probabilities; distinguish a claim with a fixed condition from one about the whole population.</figcaption>
</figure>

## Core concept 7. Conditional probability describes observation, not causation by itself

A high $P(A\mid B)$ means that $A$ often occurs in the group where $B$ was observed. This value alone does not determine how $A$ changes when $B$ is changed externally. A common cause or a selection condition can relate the two events.

In model interpretability, high $P(C\mid H)$ likewise suggests that concept label $C$ can be recovered from hidden pattern $H$. Claiming that the model used $H$ to generate its output requires interventions changing $H$ and appropriate controls.

The observed association could have a common-cause explanation such as the one below. The figure presents a possible alternative, not an estimated structure of an actual model.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A possible common factor U pointing to hidden pattern H and concept label C, with a dashed undirected observational association and no inferred H-to-C causal arrow](../../figures/assets/M04/M04-02-common-cause-alternative.svg)

<figcaption>H and C occurring together does not establish direct functional use between them. The dashed line is observational association; the common cause shown by arrows is a possible alternative to examine.</figcaption>
</figure>

## Example 1. Test results and the base rate

### Problem

Actual positives make up 10% of the sample. A test returns positive for 90% of actual positives and also for 20% of actual negatives. Calculate the probability of an actual positive given a positive test result.

### Solution

Let $A$ be the actual-positive event and $B$ the test-positive event. Then

\[
P(A)=0.1,
\quad P(B\mid A)=0.9,
\quad P(B\mid A^c)=0.2.
\]

The law of total probability gives

\[
P(B)=0.9\cdot0.1+0.2\cdot0.9=0.09+0.18=0.27
\]

Apply Bayes' rule:

\[
P(A\mid B)
=\frac{0.9\cdot0.1}{0.27}
=\frac13.
\]

### Meaning of the result

Despite the test's true-positive rate of $0.9$, only $1/3$ of positive results are actual positives. The actual-negative group is large, and its false-positive rate is $0.2$.

## Example 2. Check the same calculation in a 100-case table

For 100 samples, 10 are actual positives, of which 9 test positive. The other 90 are actual negatives, of which 18 test positive.

| Actual status | Test positive | Test negative | Total |
|---|---:|---:|---:|
| positive | 9 | 1 | 10 |
| negative | 18 | 72 | 90 |
| Total | 27 | 73 | 100 |

Among 27 positive tests, 9 are actual positives, so $9/27=1/3$. The table shows which groups the numerator and denominator of Bayes' rule count.

Reading sensitivity and the posterior in the same dot grid shows that the same 9 true positives are divided by different groups.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A 100-case grid with nine true positives and eighteen false positives showing sensitivity nine of ten actual positives versus posterior nine of twenty-seven positive tests](../../figures/assets/M04/M04-02-bayes-two-denominators.svg)

<figcaption>The 10 actual positives in the first row are sensitivity's denominator. The posterior's denominator includes all 27 colored positive results, including the 18 from the actual-negative group.</figcaption>
</figure>

## Example 3. Compare independence and mutual exclusivity

Toss a fair coin twice. Let $A$ be heads on the first toss and $B$ heads on the second. As in the previous lesson's coin example, assume the four ordered outcomes each have probability $1/4$. Then

\[
P(A)=P(B)=\frac12,
\qquad
P(A\cap B)=\frac14=P(A)P(B)
\]

so the events are independent. They occur together at $HH$, so they are not mutually exclusive.

In contrast, for one die roll, $C=\{1\}$ and $D=\{2\}$ are mutually exclusive. They are not independent because $P(C\cap D)=0$ but $P(C)P(D)=1/36$.

## Example 4. A next token's conditional distribution

In a language model's

\[
p_\theta(y\mid x)
\]

$x$ is the current context and $y$ is the next token. Changing context changes the conditioning event, so next-token probabilities can change. This notation does not assert causal relations in training-data generation or that tokens cause meaning.

## Common misconceptions

### Misconception 1. $P(A\mid B)$ and $P(B\mid A)$ are equal

Their denominators differ. Test sensitivity $P(B\mid A)$ and positive predictive value $P(A\mid B)$ can differ substantially because of the base rate.

### Misconception 2. A high likelihood implies a high posterior

The posterior uses both likelihood and prior. If the event of interest has a low base rate, a high likelihood alone does not guarantee a high posterior.

### Misconception 3. Mutually exclusive events are independent

For mutually exclusive events with positive probabilities, one excludes the other. This information changes the other's probability to 0, so they are not independent.

### Misconception 4. Independence means there is no relationship of any kind between two events

Independence is the mathematical condition that the intersection factors into a product under the chosen probability distribution. The relationship can differ under another distribution or within a conditioned subgroup.

### Misconception 5. High conditional probability proves a causal effect

Conditional probability describes the distribution under an observed condition. Claiming an intervention effect requires a causal design specifying what changes and what is held fixed.

## Exercises

### 1. Read the conditioning direction

Read $P(A\mid B)=0.7$ and $P(B\mid A)=0.4$ in words. Explain why their unequal values are not contradictory.

<details>
<summary>Show solution</summary>

The first states that, given $B$ occurred, the probability of $A$ is $0.7$. The second states that, given $A$ occurred, the probability of $B$ is $0.4$. Their denominators refer to different conditioning groups, so unequal values are not contradictory.

</details>

### 2. Conditional probability for a die

For a fair die, calculate the probability of a result at least 3 given an odd result.

<details>
<summary>Show solution</summary>

The odd event is $B=\{1,3,5\}$ and the at-least-3 event is $A=\{3,4,5,6\}$. Their intersection is $\{3,5\}$, so

\[
P(A\mid B)=\frac{2/6}{3/6}=\frac23.
\]

</details>

### 3. Multiplication rule

Given $P(A)=0.4$ and $P(B\mid A)=0.25$, calculate $P(A\cap B)$.

<details>
<summary>Show solution</summary>

\[
P(A\cap B)=P(B\mid A)P(A)=0.25\cdot0.4=0.1.
\]

</details>

### 4. Determine independence

Given $P(A)=0.5$, $P(B)=0.3$, and $P(A\cap B)=0.15$, determine whether the events are independent.

<details>
<summary>Show solution</summary>

\[
P(A)P(B)=0.5\cdot0.3=0.15=P(A\cap B)
\]

so $A$ and $B$ are independent under the given distribution.

</details>

### 5. Calculate total probability

Given $P(A)=0.3$, $P(B\mid A)=0.8$, and $P(B\mid A^c)=0.1$, calculate $P(B)$.

<details>
<summary>Show solution</summary>

Since $P(A^c)=0.7$,

\[
P(B)=0.8\cdot0.3+0.1\cdot0.7=0.24+0.07=0.31.
\]

</details>

### 6. Calculate using Bayes' rule

A particular error occurs in 5% of documents. A detector warns on 80% of erroneous documents and also on 10% of error-free documents. Calculate the probability that a document has the error given a warning.

<details>
<summary>Show solution</summary>

Let $A$ be the error event and $B$ the warning event. Then

\[
P(B)=0.8\cdot0.05+0.1\cdot0.95=0.135.
\]

Therefore,

\[
P(A\mid B)=\frac{0.8\cdot0.05}{0.135}
=\frac{0.04}{0.135}
\approx0.296.
\]

About $29.6\%$ of documents receiving a warning actually have the error.

</details>

### 7. Critique a model-interpretability claim

A high conditional probability of concept label $C$ was observed when hidden pattern $H$ appeared. Evaluate “the model uses $H$ to determine $C$,” and state what additional evidence is needed.

<details>
<summary>Show solution</summary>

High $P(C\mid H)$ shows an observational relation between $H$ and $C$, or the possibility of recovering $C$ from $H$. Claiming functional use requires removing, replacing, or adjusting $H$ and measuring whether the relevant output changes, alongside controls. A common cause producing both $H$ and $C$ must also be considered.

</details>

## Lesson summary

- Conditional probability is the proportion of the intersection within the conditioning event.
- The multiplication rule separates an intersection probability into a conditional probability and the conditioning event's probability.
- The law of total probability adds contributions from paths partitioning the sample space.
- Bayes' rule calculates a posterior from likelihood and prior.
- Independence requires the intersection probability to equal the product of marginal probabilities; it differs from mutual exclusivity.
- Conditional independence is independence with a specified condition fixed.
- High conditional probability alone does not establish functional use or a causal effect.

## Pass criteria

You pass if you can answer these questions without consulting the material.

- Can you explain the numerator and denominator of $P(A\mid B)$ as events?
- Can you calculate probabilities using the multiplication rule and law of total probability?
- Can you derive Bayes' rule and connect it to a table calculation?
- Can you distinguish $P(A\mid B)$ from $P(B\mid A)$?
- Can you use a counterexample to distinguish independence from mutual exclusivity?
- Can you write the conditions for independence and conditional independence?
- Can you limit the model-interpretability claims supported by conditional-probability evidence?

## Next lesson

- [M04-03 Random variables and probability distributions](M04-03-random-variables-distributions.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] The denominator condition for conditional probability is stated.
- [x] The multiplication rule and law of total probability are derived.
- [x] Bayes' rule has been checked using a table.
- [x] Independence, mutual exclusivity, and conditional independence are distinguished.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretability claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] No prerequisites outside the stated scope are required implicitly.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
