---
id: "M00-07"
title: "Sets, conditions, and logic"
part: 1
stage: "M00"
status: "complete"
prerequisites:
  - "M00-01"
  - "M00-02"
  - "M00-03"
estimated_time: "95~115 minutes"
---

# M00-07. Sets, conditions, and logic

## Why this lesson matters

Mathematical definitions collect objects into sets and use logical symbols to state the conditions those objects must satisfy. Papers also use phrases such as “for every input,” “for some layer,” and “if condition A holds, then result B follows.” Missing the scope or direction of these phrases can lead you to read a stronger conclusion than the author proved.

In model interpretability, confusing necessary and sufficient conditions changes how you interpret experiments. Removing a component and observing lower performance tests a different condition from restoring a function using that component alone. Sets and logic provide the grammar for reading later mathematics and a way to manage the strength of claims.

## Learning objectives

After completing this lesson, you will be able to:

- Read notation for elements, subsets, unions, and intersections.
- Interpret set-builder notation using conditions.
- Distinguish negation, conjunction, and disjunction.
- Distinguish an implication $P\Rightarrow Q$ from its converse.
- Determine necessary, sufficient, and necessary-and-sufficient conditions in examples.
- Read the scope of universal and existential propositions and explain the role of a counterexample.

## Prerequisite check

- Prerequisite: [M00-01 Numbers, variables, and constants](M00-01-numbers-variables.md)
- Prerequisite: [M00-02 Expressions, equalities, and equations](M00-02-expressions-equalities-equations.md)
- Prerequisite: [M00-03 Function inputs and outputs](M00-03-functions-input-output.md)

Check that you can distinguish the following statements.

- $x>0$: a condition that $x$ may or may not satisfy
- $x=3$: depending on context, a specification of a value or an equality
- $f:\mathbb R\to\mathbb R$: a declaration of a function's input and output sets

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Examples |
|---|---|---|---|
| $x\in A$ | `x is in A` | $x$ belongs to the set $A$ | $2\in\{1,2,3\}$ |
| $x\notin A$ | `x is not in A` | $x$ does not belong to $A$ | $4\notin\{1,2,3\}$ |
| $A\subseteq B$ | `A is a subset of B` | Every element of $A$ also belongs to $B$ | $\{1,2\}\subseteq\{1,2,3\}$ |
| $\varnothing$ | `the empty set` | A set with no elements | $\{x\in\mathbb R:x^2=-1\}=\varnothing$ |
| $A\cup B$ | `A union B` | The set of elements belonging to $A$ or $B$ | List repeated elements only once |
| $A\cap B$ | `A intersection B` | The set of elements belonging to both $A$ and $B$ | Shared elements |
| $\neg P$ | `not P` | The negation of the proposition $P$ | Reverses truth and falsehood |
| $P\land Q$ | `P and Q` | Both $P,Q$ are true | Conjunction |
| $P\lor Q$ | `P or Q` | At least one of the two is true | Disjunction |
| $P\Rightarrow Q$ | `P implies Q` | If $P$ is true, then $Q$ is true | Implication |
| $P\Leftrightarrow Q$ | `P if and only if Q` | The implication holds in both directions | Equivalence |
| $\forall$ | `for all` | For each object within a specified set | Universal quantifier |
| $\exists$ | `there exists` | At least one object satisfies the condition | Existential quantifier |

## Core concept 1. Sets collect objects as elements

A set is a collection of distinguishable objects. You can list its elements inside braces.

\[
A=\{1,2,3\}
\]

$2$ is an element of $A$, so write

\[
2\in A
\]

$5$ does not belong to $A$, so write

\[
5\notin A
\]

Listing the same element more than once still counts it as one element. The order of the listing also does not change the set itself.

\[
\{1,2,2,3\}=\{3,2,1\}
\]

Both sets contain the elements $1,2,3$. If you need to preserve order, use a sequence or ordered pair.

### Describing a set by a condition

When listing every element is difficult, state the condition its elements must satisfy.

\[
A=\{x\in\mathbb R:x>0\}
\]

Read this as “the set of real $x$ satisfying $x>0$.” The condition after the colon selects elements. Using a vertical bar instead gives the same meaning.

\[
A=\{x\in\mathbb R\mid x>0\}
\]

$x\in\mathbb R$ sets the overall range from which elements are chosen, and $x>0$ selects which ones remain. You are not fixing $x$ at one particular value; you collect every value satisfying the condition into the set $A$. The same notation is used to restrict a function's domain by a condition.

## Core concept 2. Subsets describe inclusion between sets

\[
A\subseteq B
\]

means that every element of $A$ also belongs to $B$.

For

\[
A=\{1,2\},\qquad B=\{1,2,3\}
\]

we have

\[
A\subseteq B
\]

Distinguish membership from the subset relation.

\[
1\in A
\]

relates the number $1$ to the set $A$.

\[
\{1\}\subseteq A
\]

relates the set $\{1\}$ to the set $A$. Neither $1\subseteq A$ nor $\{1\}\in A$ expresses the intended relation in this example.

The left of the following figure shows a relation between a number and a set. The right shows one entire set included in another. The two panels define A differently.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A value two belongs to set A while five lies outside, and in a separate context set A containing one two is included inside set B containing one two three](../../figures/assets/M00/M00-07-membership-subset.svg)

<figcaption>The position of the element 2 on the left shows 2∈A. On the right, both elements of A lie in B, giving A⊆B. Distinguish an element from a whole set.</figcaption>
</figure>

### The empty set

A set with no elements is called the empty set and is written

\[
\varnothing
\]

The empty set is a subset of every set.

\[
\varnothing\subseteq A
\]

To check a subset relation, look for an element of the left-hand set that is absent from the right-hand set. The empty set has no elements to check, so it has none that violate inclusion. It therefore satisfies the condition for being a subset of any set.

The empty set itself differs from a set containing the empty set as an element.

\[
\varnothing\ne\{\varnothing\}
\]

The left has no elements. The right has one element: the empty set.

A set can itself be an element of another set. If an element is a set, count that set as one object. Thus, the fact that the element of $\{\varnothing\}$ is empty differs from saying that $\{\varnothing\}$ itself has no elements.

In the following figure, count the objects inside the outer boundary. The small empty set on the right is one object.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An empty outer set contains zero elements, while a second outer set contains one smaller empty set as an element](../../figures/assets/M00/M00-07-empty-set-element.svg)

<figcaption>The left has no elements. The right contains one small boundary representing an empty set, so it has one element.</figcaption>
</figure>

## Core concept 3. Unions and intersections

Consider the two sets

\[
A=\{1,2,3\},\qquad B=\{3,4\}
\]

Their union collects elements belonging to $A$ or $B$.

\[
A\cup B=\{1,2,3,4\}
\]

Here, “or” includes membership in both sets. The element $3$ belongs to both $A$ and $B$, and also belongs to their union.

Their intersection collects elements belonging to both sets.

\[
A\cap B=\{3\}
\]

The same structure appears when partitioning data by conditions or selecting samples satisfying several properties at once.

The following figure changes only the selected region within the same two sets. The middle element, 3, belongs to both.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Union selects all elements one two three four from two overlapping sets, while intersection selects only the shared element three](../../figures/assets/M00/M00-07-union-intersection.svg)

<figcaption>The union includes elements belonging to either set and counts 3 only once. The intersection selects only 3, which lies inside both boundaries.</figcaption>
</figure>

## Core concept 4. Propositions and logical operations

A proposition is a statement that can be judged true or false.

- “$2$ is even”: a true proposition
- “$3>5$”: a false proposition
- “$x>0$”: a condition until $x$ is specified

Let $P$ be “$x>0$” and $Q$ be “$x<10$.”

### Negation

\[
\neg P
\]

is the negation of $P$. If $P$ is “$x>0$,” then $\neg P$ is

\[
x\le0
\]

Writing only $x<0$ leaves out $x=0$ and is not the exact negation.

### And

\[
P\land Q
\]

is true only when both conditions are satisfied.

\[
x>0\land x<10
\]

is equivalent to $0<x<10$.

### Or

\[
P\lor Q
\]

is true when at least one of the two conditions is true. Mathematical “or” includes the case where both conditions are true.

To negate two conditions joined by “and,” select the cases where at least one is false. The condition $0<x<10$ means that both $x>0$ and $x<10$ hold, so its negation is $x\le0$ or $x\ge10$. Both endpoints fail the original condition and are therefore included in the negated range.

The following figure uses open and filled endpoints to distinguish exclusion from inclusion of boundary values.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The open interval between zero and ten excludes both endpoints, whereas its negation includes both outer ranges and the endpoints](../../figures/assets/M00/M00-07-logic-interval-negation.svg)

<figcaption>The original condition selects only values between 0 and 10. Its negation joins the two outer ranges with “or” and includes the endpoints 0 and 10.</figcaption>
</figure>

## Core concept 5. The direction of an implication

\[
P\Rightarrow Q
\]

is read as “if $P$, then $Q$.” $P$ is the assumption, and $Q$ is the conclusion.

$P$: “The integer $n$ is a multiple of $4$.”

$Q$: “The integer $n$ is even.”

Then

\[
P\Rightarrow Q
\]

holds. A multiple of $4$ can be written as $4k=2(2k)$, so it is even.

Reversing the direction gives

\[
Q\Rightarrow P
\]

which is called the converse of the original proposition. “If an integer is even, then it is a multiple of $4$” is false. $n=2$ is a counterexample.

The truth of an implication does not imply that its converse is true.

A case violating $P\Rightarrow Q$ must have $P$ true and $Q$ false. For objects where $P$ is false, the original implication does not restrict whether $Q$ is true or false. In the example, $n=2$ is even but not a multiple of $4$, so it is a counterexample to the converse. It is not a counterexample to the original implication because it does not satisfy the assumption of being a multiple of $4$.

### The contrapositive

The contrapositive of

\[
P\Rightarrow Q
\]

is

\[
\neg Q\Rightarrow\neg P
\]

The original proposition and its contrapositive have the same truth value.

To violate the contrapositive, $\neg Q$ must be true and $\neg P$ false. This means that $Q$ is false and $P$ true, the same case that violates the original implication. Because the two implications are false in the same case, their truth values agree.

The contrapositive of the example is “if an integer is not even, then it is not a multiple of $4$.” It is true because an odd integer cannot be a multiple of $4$.

## Core concept 6. Necessary and sufficient conditions

When

\[
P\Rightarrow Q
\]

holds, we say:

- $P$ is a sufficient condition for $Q$.
- $Q$ is a necessary condition for $P$.

Being a multiple of $4$ implies being even, so being a multiple of $4$ is sufficient for being even. Being even is necessary for being a multiple of $4$. A multiple of $4$ must be even, but not every even integer is a multiple of $4$.

If the implication holds in both directions, write

\[
P\Leftrightarrow Q
\]

and say that $P$ and $Q$ are equivalent.

\[
n\text{ is even}
\Leftrightarrow
n=2k\text{ for some integer }k
\]

This is the definition of being even, so both directions hold.

In the following figure, check the inclusion of region P in region Q and the element 2, which belongs only to Q.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Multiples of four form a nested subset of even integers, but the even integer two lies outside the multiples of four and disproves the converse](../../figures/assets/M00/M00-07-implication-inclusion.svg)

<figcaption>Membership in P implies membership in Q, so P is sufficient for Q. Q is necessary when P holds, but the even integer 2 shows that Q alone does not guarantee P.</figcaption>
</figure>

### The logic of removal and restoration

Consider a model component $C$ and a function $F$.

- If removing $C$ impairs $F$, the result supports the necessity of $C$ under those experimental conditions.
- If retaining only $C$ restores $F$, the result supports the sufficiency of $C$ under those experimental conditions.

Necessity and sufficiency require different interventions. Removal results alone do not establish sufficiency, and restoration results alone do not establish necessity. Controls and the scope of intervention also limit the scope of the conclusion.

## Core concept 7. Distinguish universality from the existence of one case

### The universal quantifier

\[
\forall x\in A,\ P(x)
\]

is read as “$P(x)$ holds for every $x$ in the set $A$.”

One element violating the condition is enough to show that a universal proposition is false. Such an element is called a counterexample.

For example,

\[
\forall x\in\mathbb R,\ x^2>x
\]

is false. At $x=0$, $0^2>0$ does not hold.

### The existential quantifier

\[
\exists x\in A,\ P(x)
\]

is read as “there exists at least one $x$ in $A$ satisfying $P(x)$.”

\[
\exists x\in\mathbb R,\ x^2=4
\]

is true because $x=2$ or $x=-2$ satisfies the condition.

One example satisfying a condition supports an existential proposition but does not prove a universal proposition.

The following figure distinguishes a number used as a counterexample to a universal proposition from a number witnessing an existential proposition.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Among a few real inputs shown, highlighted zero refutes the universal claim x squared greater than x and highlighted two witnesses the existence of a real number whose square is four](../../figures/assets/M00/M00-07-quantifier-counterexample-witness.svg)

<figcaption>The failure at x=0 refutes the claim about all real numbers on the left. Success at x=2 establishes existence on the right but does not mean that every x satisfies the same condition.</figcaption>
</figure>

## Example 1. Set operations

### Problem

For

\[
A=\{1,2,3,4\},\qquad B=\{3,4,5\}
\]

find $A\cup B$ and $A\cap B$, and determine whether $\{3,4\}\subseteq A$.

### Solution

Collecting elements belonging to at least one of the two sets gives

\[
A\cup B=\{1,2,3,4,5\}
\]

The elements in both sets are $3,4$, so

\[
A\cap B=\{3,4\}
\]

Both $3$ and $4$ belong to $A$, so

\[
\{3,4\}\subseteq A
\]

holds.

## Example 2. Necessary and sufficient conditions

For an integer $n$, define two conditions.

- $P$: $n$ is a multiple of $6$.
- $Q$: $n$ is a multiple of $3$.

If $n=6k$, then

\[
n=3(2k)
\]

so $n$ is a multiple of $3$. Therefore,

\[
P\Rightarrow Q
\]

holds.

$P$ is sufficient for $Q$, and $Q$ is necessary for $P$. The converse, $Q\Rightarrow P$, does not hold. $n=3$ is a multiple of $3$ but not of $6$.

## Example 3. Reading quantifier order

Compare the following formulas.

\[
\forall x\in\mathbb R,\ \exists y\in\mathbb R,\ y>x
\]

\[
\exists y\in\mathbb R,\ \forall x\in\mathbb R,\ y>x
\]

The first says that after choosing any real $x$, you can find a larger real $y$. It is true: set $y=x+1$.

The second says that there exists one real $y$ larger than every real number. It is false: for any chosen $y$, $x=y+1$ is larger.

The same symbols make different claims when the order of $\forall$ and $\exists$ changes.

## Example 4. Checking a model-interpretability claim

Let $P$ be “the input label can be recovered from an activation with high accuracy,” and $Q$ be “the model uses that label information to compute its output.”

Observing $P$ through a probe experiment does not automatically establish

\[
P\Rightarrow Q
\]

An auxiliary model's ability to read information shows recoverability. To assess the claim that the original model uses that information, check whether intervening on the activation changes the output or function.

Concluding $Q$ from the probe result alone therefore leaves sufficiency unverified. I06 and I07 revisit this distinction together with experimental design.

## Common misconceptions

### Misconception 1. $x\in A$ and $\{x\}\subseteq A$ differ only in notation

The first states that the object $x$ is an element of $A$. The second states that the set containing only $x$ is a subset of $A$. The two formulas relate different kinds of object.

### Misconception 2. If “$P$ implies $Q$” is true, “$Q$ implies $P$” is also true

Check the converse separately. A multiple of $4$ is even, but the even integer $2$ is not a multiple of $4$.

### Misconception 3. A necessary condition is sufficient on its own

Saying that $Q$ is necessary for $P$ means that $Q$ must hold whenever $P$ holds. Whether $Q$ alone guarantees $P$ is a question of sufficiency.

### Misconception 4. Checking several examples proves every case

Finite examples can establish existence or help check a claim. A universal proposition over an infinite range requires a general argument. One counterexample can refute a universal proposition.

### Misconception 5. Logical “or” means exactly one of the two

$P\lor Q$ means that at least one of the two is true. It includes the case where both conditions are true.

## Exercises

### 1. Distinguish elements from subsets

For

\[
A=\{1,2,\{3\}\}
\]

determine whether the following propositions are true or false.

\[
2\in A,\qquad \{2\}\subseteq A,\qquad 3\in A,\qquad \{3\}\in A
\]

<details>
<summary>Show solution</summary>

$2$ is an element of $A$, so $2\in A$ is true. The sole element $2$ of $\{2\}$ belongs to $A$, so $\{2\}\subseteq A$ is also true.

The elements of $A$ are $1$, $2$, and $\{3\}$. The number $3$ itself is not an element, so $3\in A$ is false. The set $\{3\}$ is listed as an element of $A$, so $\{3\}\in A$ is true.

</details>

### 2. Calculate unions and intersections

For

\[
A=\{a,b,c\},\qquad B=\{b,c,d\}
\]

find $A\cup B$ and $A\cap B$.

<details>
<summary>Show solution</summary>

Collecting elements belonging to at least one set gives

\[
A\cup B=\{a,b,c,d\}
\]

The elements shared by both sets are $b,c$, so

\[
A\cap B=\{b,c\}
\]

</details>

### 3. Negate a condition

For real $x$, give the exact negation of

\[
1<x\le5
\]

<details>
<summary>Show solution</summary>

The original condition requires both $x>1$ and $x\le5$. Outside this range, $x\le1$ or $x>5$.

\[
\neg(1<x\le5)
\quad\Longleftrightarrow\quad
x\le1\ \lor\ x>5
\]

Check whether the boundary values $1$ and $5$ are included. $x=1$ does not satisfy the original condition, while $x=5$ does.

</details>

### 4. State the converse and contrapositive

Write the converse and contrapositive of the following proposition and determine their truth values.

> If the integer $n$ is a multiple of $10$, then $n$ is a multiple of $5$.

<details>
<summary>Show solution</summary>

The original proposition is true. If $n=10k$, then $n=5(2k)$, so it is a multiple of $5$.

The converse is:

> If the integer $n$ is a multiple of $5$, then $n$ is a multiple of $10$.

It is false because $n=5$ is a counterexample.

The contrapositive is:

> If the integer $n$ is not a multiple of $5$, then $n$ is not a multiple of $10$.

The contrapositive has the same truth value as the original proposition, so it is true.

</details>

### 5. Determine necessary and sufficient conditions

For an integer $n$, let $P$ be “$n$ is a multiple of $12$” and $Q$ be “$n$ is a multiple of $4$.” Explain which condition is necessary or sufficient for the other.

<details>
<summary>Show solution</summary>

If $n=12k$, then

\[
n=4(3k)
\]

so

\[
P\Rightarrow Q
\]

holds. Therefore, $P$ is sufficient for $Q$, and $Q$ is necessary for $P$.

$n=4$ is a multiple of $4$ but not of $12$, so $Q\Rightarrow P$ does not hold. $Q$ is not sufficient for $P$.

</details>

### 6. Evaluate a universal proposition

Determine whether the following proposition is true. If it is false, provide one counterexample.

\[
\forall x\in\mathbb R,\quad x^2\ge x
\]

<details>
<summary>Show solution</summary>

The proposition is false. For example, if

\[
x=\frac12
\]

then

\[
x^2=\frac14<\frac12=x
\]

One counterexample refutes the claim about all real numbers.

</details>

### 7. Critique an interpretability claim

A researcher recovers a gender label from activations with 95% accuracy and concludes that “the model uses gender information for prediction.” Separate the observed proposition from the conclusion and explain what further evidence is needed.

<details>
<summary>Show solution</summary>

The observed proposition is “the gender label is recoverable with high accuracy under the selected activation and probe settings.” The conclusion is “the original model functionally uses that information to compute its output.”

Recoverability alone does not establish an implication of use. Assessing use requires a controlled intervention on the information or related activations, appropriate controls, and a metric measuring changes in the output or function. The generalization scope of a result from one dataset and one probe also requires separate evaluation.

</details>

## Lesson summary

- $x\in A$ describes membership, while $A\subseteq B$ describes inclusion between sets.
- A union collects elements belonging to at least one set; an intersection collects elements belonging to both.
- $P\Rightarrow Q$ and its converse $Q\Rightarrow P$ are separate propositions.
- If $P\Rightarrow Q$, then $P$ is sufficient for $Q$, and $Q$ is necessary for $P$.
- One counterexample can refute a universal proposition; one example of existence does not prove a universal proposition.

## Pass criteria

You pass if you can answer the following questions without consulting the material.

- Can you distinguish membership notation from subset notation?
- Can you calculate unions and intersections?
- Can you negate a condition with the correct inclusion of boundary values?
- Can you distinguish an implication, its converse, and its contrapositive?
- Can you explain the direction of necessary and sufficient conditions?
- Can you distinguish recoverability from a model's functional use of information in logical terms?

## Next lesson

The next lesson is [M00-08 Function composition and inverse functions](M00-08-composition-inverse.md). You will learn the order of successive function application and the conditions for an inverse function to recover inputs.

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] All new symbols are defined before use.
- [x] Membership is distinguished from the subset relation.
- [x] The directions of implications, converses, and contrapositives have been checked.
- [x] Necessary and sufficient conditions have been checked using the same example.
- [x] Every exercise has a solution.
- [x] The claim strengths of recovery, use, and causation are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
