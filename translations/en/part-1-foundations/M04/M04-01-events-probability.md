---
id: "M04-01"
title: "Events and probability"
part: 1
stage: "M04"
status: "complete"
prerequisites:
  - "M00-06"
  - "M00-07"
estimated_time: "120–145 minutes"
---

# M04-01. Events and probability

## Why this lesson matters

The probabilities a model outputs for classes, proportions observed in data, and chances of experimental success all use the numerical range $[0,1]$. Yet a calculation cannot be interpreted until you identify what those numbers are assigned to. Probability specifies a set of possible outcomes and provides a rule assigning numbers to events of interest within that set.

This lesson distinguishes sample spaces, outcomes, and events, then states the axioms probability must satisfy. Conditional probability, random variables, expectation, and information theory will build on this structure.

## Learning objectives

After completing this lesson, you should be able to:

- Distinguish a sample space, an outcome, and an event.
- Read unions, intersections, and complement events as probability statements.
- Explain the three probability axioms and apply them to a small finite sample space.
- Calculate probabilities using the complement and inclusion-exclusion formulas.
- Distinguish situations that allow an equal-probability assumption from those that do not.
- Distinguish empirical frequency from probability under a probability model.
- Limit the claims supported by a model's predicted probability.

## Prerequisite check

- Prerequisite lesson: [M00-06 Indices and summation](../M00/M00-06-indices-summation.md)
- Prerequisite lesson: [M00-07 Sets, conditions, and logic](../M00/M00-07-sets-conditions-logic.md)
- Check: Can you write a union, intersection, and complement in symbols?
- Check: Can you expand $\sum_i p_i$ into its individual terms?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Scope |
|---|---|---|---|
| $\Omega$ | `capital omega` | The sample space of all possible outcomes | Set |
| $\omega$ | `omega` | The outcome of one trial | $\omega\in\Omega$ |
| $A,B$ | `A and B` | Subsets of outcomes | $A,B\subseteq\Omega$ |
| $A^c$ | `A complement` | The outcomes where $A$ does not occur | $\Omega\setminus A$ |
| $A\cup B$ | `A union B` | The event that $A$ or $B$ occurs | Event |
| $A\cap B$ | `A intersection B` | The event that both $A$ and $B$ occur | Event |
| $\varnothing$ | `the empty set` | The impossible event containing no outcomes | Event |
| $P(A)$ | `P of A` | The number probability assigns to event $A$ | $0\le P(A)\le1$ |

## Core concept 1. A sample space specifies the possible outcomes

A sample space $\Omega$ is the set of all outcomes a probability model treats as possible. An individual result of one trial is an outcome, written $\omega\in\Omega$.

If you record only heads or tails from one coin toss, you can use

\[
\Omega=\{H,T\}
\]

as the sample space. If you toss a coin twice and record the order, it is

\[
\Omega=\{HH,HT,TH,TT\}
\]

The same experiment can have different sample spaces depending on what you observe and distinguish. This model does not assign probabilities to outcomes outside its sample space.

Following the records of the two trials shows why $HT$ and $TH$ are distinct outcomes. The branches below have no assigned probabilities.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A two-level coin-flip tree with distinct ordered leaves HH, HT, TH and TT, without assigned probabilities](../../figures/assets/M04/M04-01-ordered-outcome-tree.svg)

<figcaption>Joining the first and second records in order gives four outcomes. Listing the branches does not assume that these outcomes have equal probabilities.</figcaption>
</figure>

## Core concept 2. An event is a set of outcomes

An event $A$ is a subset of the sample space. For one die roll, let

\[
\Omega=\{1,2,3,4,5,6\}
\]

The event of an even result is $A=\{2,4,6\}$. If the observed result is $4$, then $\omega=4$ and $4\in A$, so event $A$ occurred.

Set operations express logical statements about events.

- $A\cup B$: $A$ or $B$ occurs, including the case where both occur.
- $A\cap B$: Both $A$ and $B$ occur.
- $A^c$: $A$ does not occur.
- $A\setminus B$: $A$ occurs and $B$ does not.

If two events cannot occur together, $A\cap B=\varnothing$, and they are mutually exclusive.

The outcome $4$ is one element of the even-result event, not the entire event.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Die outcomes inside sample space Omega, with even event A containing 2, 4 and 6 and observed outcome 4 highlighted](../../figures/assets/M04/M04-01-outcome-event-containment.svg)

<figcaption>The outer boundary is the sample space, and the inner boundary is the event. The event occurs when the observed outcome lies inside the inner boundary.</figcaption>
</figure>

## Core concept 3. Probability is a rule assigning numbers to events

Probability $P$ assigns numbers in $[0,1]$ to the allowed events and satisfies these axioms.

1. Nonnegativity:

\[
P(A)\ge0.
\]

2. Total probability:

\[
P(\Omega)=1.
\]

3. Countable additivity: For disjoint events $A_1,A_2,\ldots$,

\[
P\left(\bigcup_{i=1}^{\infty}A_i\right)
=\sum_{i=1}^{\infty}P(A_i).
\]

In a finite sample space, begin with adding finitely many disjoint events. The axioms prevent probabilities from being assigned independently and arbitrarily: assigning a value to one event constrains the values of related events.

In a finite sample space, every subset is treated as an event. Even the probability of one outcome $\omega$ is the value assigned to the event $\{\omega\}$ containing only that outcome. $P$ is neither an outcome nor a set; it is a rule that takes an event as input and returns a number.

The empty set is disjoint from every event, so $P(\Omega)=P(\Omega)+P(\varnothing)$ gives $P(\varnothing)=0$. Applying additivity to $\Omega=A\cup A^c$ also gives $1=P(A)+P(A^c)$. Both terms are nonnegative, so $P(A)\le1$. The range $[0,1]$ therefore agrees with the axioms.

Representing the probabilities in Example 3 by bar widths shows that selecting an event collects the mass belonging to its outcomes.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A total probability mass bar split into a with mass 0.6, b with mass 0.3 and c with mass 0.1, with event b and c totaling 0.4](../../figures/assets/M04/M04-01-event-mass-assignment.svg)

<figcaption>The whole bar has probability 1. Distinct outcomes have disjoint masses, so adding the widths belonging to an event gives its probability.</figcaption>
</figure>

## Core concept 4. Complements and inclusion-exclusion correct the counting

$A$ and $A^c$ are disjoint and together form $\Omega$. Thus,

\[
P(A^c)=1-P(A)
\]

For events such as “at least once,” it is often shorter to calculate the opposite event, where nothing occurs, first.

Adding only $P(A)+P(B)$ to calculate the probability of $A\cup B$ counts the intersection twice. Inclusion-exclusion subtracts one copy of the overlap:

\[
P(A\cup B)=P(A)+P(B)-P(A\cap B).
\]

If $A$ and $B$ are mutually exclusive, $P(A\cap B)=0$, so their probabilities can be added without a correction.

The axioms also justify this correction. Split $A\cup B$ into the disjoint events $A$ and $B\setminus A$ to obtain $P(A\cup B)=P(A)+P(B\setminus A)$. Meanwhile, $B$ splits into $B\setminus A$ and $A\cap B$, so $P(B\setminus A)=P(B)-P(A\cap B)$. Substitution into the first equation gives inclusion-exclusion.

## Core concept 5. Set inclusion orders probabilities

If $A\subseteq B$, $B$ contains every outcome in $A$. Then

\[
P(A)\le P(B)
\]

Splitting $B$ into the disjoint events $A$ and $B\setminus A$ gives

\[
P(B)=P(A)+P(B\setminus A)
\]

The second term is nonnegative, which gives the inequality above. This property is monotonicity.

Below, $A=\{c\}$ and $B=\{b,c\}$. The larger event only adds mass; it removes none of the original mass.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Nested events A containing c and B containing b and c, with nonnegative additional mass 0.3 increasing probability from 0.1 to 0.4](../../figures/assets/M04/M04-01-monotonic-added-mass.svg)

<figcaption>In probability terms, inclusion adds the outer region's mass to the smaller event's mass. The two probabilities can be equal if the outer region has probability 0.</figcaption>
</figure>

## Core concept 6. Equal probabilities require an additional assumption

If each outcome in a finite sample space can be assumed to have the same probability, calculate

\[
P(A)=\frac{|A|}{|\Omega|}
\]

The even-result event for a fair die contains three outcomes, so $P(A)=3/6=1/2$.

The denominator tells you how many equal shares divide the total probability 1. If $|\Omega|=K$ and each outcome has probability $p$, then $Kp=1$, giving $p=1/K$. Event $A$ contains $|A|$ disjoint single-outcome events, so adding their probabilities gives $|A|/K$.

Counting outcomes works only under the equal-probability assumption. A misshapen die or data with unequal class proportions can assign different probabilities to different outcomes. In that case, add the probabilities of the individual outcomes.

In a finite sample space $\Omega=\{\omega_1,\ldots,\omega_K\}$, if

\[
P(\{\omega_k\})=p_k,
\qquad p_k\ge0,
\qquad \sum_{k=1}^{K}p_k=1
\]

then

\[
P(A)=\sum_{\omega_k\in A}p_k
\]

Selecting the same two elements can give different probabilities when their assigned masses differ.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Equal-width and unequal-width probability partitions on the same three outcomes, where selecting b and c gives two thirds or 0.4 respectively](../../figures/assets/M04/M04-01-equal-unequal-mass.svg)

<figcaption>Both bars have three elements and the same selected event. In the upper bar, count two equal widths. In the lower bar, add the two selected parts' unequal masses.</figcaption>
</figure>

## Core concept 7. Probability and empirical frequency are related but distinct objects

If event $A$ occurs $n_A$ times in $n$ observations, its empirical frequency is

\[
\widehat P_n(A)=\frac{n_A}{n}
\]

This value is calculated from an observed sample. $P(A)$ is the value the chosen probability model assigns to the event. Under stable conditions for repeated observations, empirical frequency can approach probability, but they can differ in a finite sample.

Collecting observations again under the same model can change $n_A$ and therefore $\widehat P_n(A)$. Observing the event in 8 of 10 observations means that this sample's frequency is $0.8$, not that the model's probability must be $0.8$. Collecting data from the same distribution so that previous observations do not change the next observation's event probability is a basic condition connecting frequency and model probability. The sampling lesson will return to this condition.

A neural network output $p_\theta(y\mid x)=0.8$ is also a prediction depending on the model, parameters $\theta$, and input $x$. The number $0.8$ alone does not establish that 80 of 100 similar inputs will be predicted correctly. That conclusion requires further evaluation of the data distribution and calibration.

Even with model probability fixed, the count of an event can vary across observation sequences. The sequences below were constructed to illustrate this difference; they are not experimental results.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A fixed model probability 0.7 above two illustrative ten-trial sequences with eight and six successes and empirical frequencies 0.8 and 0.6](../../figures/assets/M04/M04-01-model-frequency.svg)

<figcaption>Model probability and sample frequency are determined from different inputs. The upper number is the probability model's assignment; the lower numbers divide the event counts observed in each sequence by the sequence length.</figcaption>
</figure>

## Example 1. Calculate die-event probabilities

### Problem

Roll a fair six-sided die once. Let $A$ be the event of an even result and $B$ the event of a result at least 4. Calculate $P(A)$, $P(B)$, $P(A\cap B)$, and $P(A\cup B)$.

### Solution

\[
\Omega=\{1,2,3,4,5,6\},
\quad A=\{2,4,6\},
\quad B=\{4,5,6\}.
\]

The outcomes have equal probabilities, so

\[
P(A)=\frac36=\frac12,
\qquad
P(B)=\frac36=\frac12.
\]

The intersection is $A\cap B=\{4,6\}$, giving

\[
P(A\cap B)=\frac26=\frac13.
\]

Apply inclusion-exclusion:

\[
P(A\cup B)
=\frac12+\frac12-\frac13
=\frac23.
\]

### Meaning of the result

$A$ and $B$ share the outcomes $4,6$, so adding their probabilities without a correction double-counts these outcomes.

The outcomes $4,6$ in the overlap are counted once for each event when the two events are counted separately.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Overlapping even and at-least-four die events with shared outcomes 4 and 6, showing the subtraction of one duplicated overlap](../../figures/assets/M04/M04-01-inclusion-exclusion-overlap.svg)

<figcaption>The union contains four distinct outcomes within its boundary. Adding the two event counts gives six, including two duplicated intersection outcomes, so subtract those two once.</figcaption>
</figure>

## Example 2. Use the complement to calculate “at least once”

Toss a fair coin twice. Let $C$ be the event of at least one head. $C^c$ is the event of two tails.

Here, assume that the four ordered outcomes $HH,HT,TH,TT$ each have probability $1/4$. Fairness of the individual trials alone does not determine their joint probabilities, so this assumption is stated explicitly.

The complement formula gives

\[
P(C)=1-P(C^c)=1-\frac14=\frac34
\]

Directly counting the four possible outcomes gives the same result because $C=\{HH,HT,TH\}$.

Under this example's equal-probability assumption, adding the three outcomes directly is equivalent to subtracting the remaining outcome's probability from the total.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Four equally likely coin outcomes partitioned into at least one head with three outcomes and no heads with only TT](../../figures/assets/M04/M04-01-complement-partition.svg)

<figcaption>The event of interest and its complement are disjoint and cover all four outcomes. Their probabilities therefore sum to 1.</figcaption>
</figure>

## Example 3. A sample space with unequal probabilities

Let $\Omega=\{a,b,c\}$, with

\[
P(\{a\})=0.6,
\qquad P(\{b\})=0.3,
\qquad P(\{c\})=0.1
\]

There is no equal-probability assumption in this sample space, so the element-count ratio $2/3$ does not apply. Event $A=\{b,c\}$ has probability

\[
P(A)=0.3+0.1=0.4
\]

## Example 4. Treat a set of classes as an event

Suppose a model outputs

\[
p_\theta(y\mid x)=(0.55,0.30,0.15)
\]

for three classes. The event “class 1 or class 3” has predicted probability

\[
0.55+0.15=0.70
\]

because the two classes are disjoint. This calculation adds probabilities the model assigns at this input. Agreement with actual frequencies is evaluated on separate data.

## Common misconceptions

### Misconception 1. An event is the outcome of one trial

An outcome $\omega$ is an element of the sample space; an event $A$ is a set of outcomes. The event occurs when the outcome belongs to that event.

### Misconception 2. The probabilities of two events can always be added

Adding overlapping events' probabilities counts their intersection twice. Inclusion-exclusion removes one copy of the overlap.

### Misconception 3. Three possible outcomes must each have probability $1/3$

The number of outcomes does not guarantee equal probabilities. An assumption such as fairness or symmetry is needed to give each outcome the same chance.

### Misconception 4. An event with probability 0 is logically impossible

In a finite sample space, this holds under the condition that every outcome has positive probability. In a continuous distribution, a point can have probability 0 even though its value belongs to the sample space. M04-03 distinguishes density from point probability.

### Misconception 5. A model's predicted probability is the true probability

Predicted probabilities are numbers determined by the model and training data. Calibration and generalization evaluation are needed to check agreement with actual frequencies and whether that agreement persists under distribution shift.

## Exercises

### 1. Distinguish an outcome from an event

In the sample space for one die roll, explain what $\omega=5$ and $A=\{1,3,5\}$ represent. Determine whether event $A$ occurs at outcome $5$.

<details>
<summary>Show solution</summary>

$\omega=5$ is an outcome, and $A$ is the event of an odd result. Since $5\in A$, event $A$ occurs when the result is 5.

</details>

### 2. Read a set operation

Let $A$ be “the prediction is correct” and $B$ be “the model's confidence is at least 0.9.” Explain $A\cap B^c$ in words.

<details>
<summary>Show solution</summary>

The event is that the prediction is correct but the model's confidence is below 0.9. $B^c$ specifies confidence below 0.9, and the intersection requires both conditions to hold.

</details>

### 3. Check the probability axioms

Assign $P(\{a\})=0.5$, $P(\{b\})=0.4$, and $P(\{c\})=0.3$ to $\Omega=\{a,b,c\}$. Determine whether this is a valid probability model.

<details>
<summary>Show solution</summary>

Each value is nonnegative, but their sum is

\[
0.5+0.4+0.3=1.2
\]

The probabilities of the three disjoint single-outcome events must sum to $P(\Omega)=1$, so the model is invalid.

</details>

### 4. Calculate using inclusion-exclusion

Given $P(A)=0.6$, $P(B)=0.5$, and $P(A\cap B)=0.2$, calculate $P(A\cup B)$.

<details>
<summary>Show solution</summary>

\[
P(A\cup B)=0.6+0.5-0.2=0.9.
\]

The intersection $0.2$ was added twice, so subtract it once.

</details>

### 5. Calculate a complement probability

A check has probability $0.08$ of an error occurring once. Calculate the probability that no error occurs.

<details>
<summary>Show solution</summary>

Let $E$ be the error event. No error is the event $E^c$, so

\[
P(E^c)=1-P(E)=1-0.08=0.92
\]

</details>

### 6. Critique an equal-probability assumption

Evaluate the claim that each class has probability $1/3$ because a dataset has three classes.

<details>
<summary>Show solution</summary>

Having three classes specifies only the number of possible labels. It does not establish that the data-generating process or model assigns equal probabilities to them. Class frequencies or an explicitly specified prior are needed.

</details>

### 7. Limit a model claim

A model outputs $0.9$ for the cat class on one image. Determine whether “this model correctly predicts 90% of cat images” is justified, and state what additional evaluation is needed.

<details>
<summary>Show solution</summary>

The predicted probability for one input does not determine accuracy across many cat images. Cat-class accuracy must be measured on separate evaluation data. To claim that about 90% of predictions assigned $0.9$ confidence are correct, calibration must also be evaluated by confidence bin.

</details>

## Lesson summary

- A sample space contains all outcomes the model treats as possible; an event is a subset of it.
- Probability assigns events numbers in $[0,1]$ and satisfies nonnegativity, total probability, and countable additivity.
- The complement formula subtracts the opposite event's probability from 1; inclusion-exclusion corrects duplicated intersections.
- Calculating probabilities from outcome counts requires an equal-probability assumption.
- Empirical frequency is calculated from a sample; probability is assigned to an event by a model.
- Agreement between a model's predicted probabilities and actual frequencies requires separate evaluation.

## Pass criteria

You pass if you can answer these questions without consulting the material.

- Can you distinguish a sample space, an outcome, and an event using an example?
- Can you read a union, intersection, and complement event as probability statements?
- Can you explain the three probability axioms?
- Can you calculate small probabilities using complements and inclusion-exclusion?
- Can you state when the equal-probability formula applies?
- Can you distinguish empirical frequency from model probability?
- Can you limit the claims supported by one predicted probability?

## Next lesson

- [M04-02 Conditional probability and Bayes' rule](M04-02-conditional-probability-bayes-rule.md)

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] Sample spaces, outcomes, and events are distinguished.
- [x] Probability axioms and their derived formulas are explained.
- [x] The conditions for an equal-probability assumption are stated.
- [x] Examples on small finite sample spaces have been checked.
- [x] Every exercise has a solution.
- [x] The strength of model-interpretability claims is distinguished.
- [x] The glossary and notation rules are followed.
- [x] No prerequisites outside the stated scope are required implicitly.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
