---
id: "M00-03"
title: "Function inputs and outputs"
part: 1
stage: "M00"
status: "complete"
prerequisites:
  - "M00-01"
  - "M00-02"
estimated_time: "70–90 minutes"
---

# M00-03. Function inputs and outputs

## Why this lesson matters

Neural network papers often represent an entire model as a single function.

\[
y=f_\theta(x)
\]

Reading this expression requires more than knowing a formula for the calculation. You need to identify the input, the output, and what the subscript $\theta$ fixes. You also need to check which inputs the function can accept and which outputs it can produce.

Functions will provide a common language for function composition, differentiation, matrix transformations, probabilistic models, and neural networks. This lesson focuses on reading function notation and calculating small examples.

## Learning objectives

By the end of this lesson, you should be able to:

- Explain what it means for a function to assign an output to each input.
- Read $f(x)$ and $y=f(x)$ as English sentences.
- Distinguish the domain, codomain, and range in a finite example.
- Calculate a function value by substituting an input into a formula.
- Identify the input, output, function, and parameters in $y=f_\theta(x)$.

## Prerequisite check

- Prerequisite lesson: [M00-01 Numbers, variables, and constants](M00-01-numbers-variables.md)
- Prerequisite lesson: [M00-02 Expressions, equalities, and equations](M00-02-expressions-equalities-equations.md)

Check whether you can answer these two questions.

1. Can you distinguish the variable from the constants in $3x-2$?
2. Can you read the equals sign in $y=3x-2$ as “the values on the left and right are equal”?

If these questions are difficult, reread the sections on variables and equalities in the prerequisite lessons.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and conditions |
|---|---|---|---|
| $f$ | `f` | The name of a function | This lesson considers functions between real numbers or finite sets |
| $x$ | `x` | An input to the function | An element of the domain |
| $f(x)$ | `f of x` | The function value obtained by applying $f$ to $x$ | An element of the codomain |
| $y=f(x)$ | `y equals f of x` | The output $y$ equals the function value at $x$ | Fixing $x$ determines $y$ |
| $f:A\to B$ | `f maps A to B` | A function with domain $A$ and codomain $B$ | $A,B$ are sets |
| $\theta$ | `theta` | Parameters that determine how the function operates | Depending on the model, one number, a vector, or several matrices |

## Core concept 1. A function assigns one output to each input

### Intuition

A function $f$ takes an input and produces an output according to a specified rule. For example, the rule “multiply the input by 2, then add 1” can be written as

\[
f(x)=2x+1
\]

For input $3$, the output is $7$.

\[
f(3)=2\cdot 3+1=7
\]

You can view this calculation in two ways. On the left, input $3$ passes through the steps of the rule to produce output $7$. On the right, the input and output form the ordered pair $(3,7)$, which is plotted as one point on the graph. The calculation and the graph point represent the same correspondence.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A function evaluation from input three to output seven shown beside the matching graph point](../../figures/assets/M00/M00-03-c01-visual.svg)

<figcaption>Pairing the input and output in f(3)=7 on the left gives the point (3,7) on the graph on the right. Substitution into the formula and reading the graph express the same input–output correspondence in two ways.</figcaption>
</figure>

### Precise definition

A function from a set $A$ to a set $B$ is a rule that assigns exactly one element of $B$ to each element of $A$.

\[
f:A\to B
\]

This definition has two conditions.

1. Every input in $A$ must have an output.
2. Each input must have only one output.

The first condition means that an input declared valid for the function cannot be left without a result. The second means that this result must be uniquely determined. If the same function and input were assigned both $f(3)=7$ and $f(3)=9$, the notation $f(3)$ would not identify one value. Function notation requires the input to determine the function value.

Different inputs may have the same output. For example, if

\[
f(x)=x^2
\]

then $f(2)=4$ and $f(-2)=4$. The inputs $2$ and $-2$ have the same output $4$, which satisfies the definition of a function.

The conditions apply in the direction from input to output. If you know only the output $4$ and try to work backward to the input, you cannot distinguish $2$ from $-2$. Calculating a function value and recovering a unique input from that value are separate abilities.

### Scope of this lesson

This lesson considers deterministic functions, which give the same output for the same input. Later lessons represent probabilistic models using conditional distributions or by including random values as additional inputs. For now, focus on the basic structure of function notation.

## Core concept 2. $f(x)$ distinguishes a function from a function value

\[
f(x)
\]

Here, $f$ names the rule and $x$ is the input. The expression $f(x)$ is the output value obtained by applying the rule $f$ to the input $x$.

In $f(x)=2x+1$, the symbol $f$ refers to the whole rule, which can be applied to different inputs. The expression $f(3)$ refers to one value, at input $3$, and evaluates to $7$. Changing the input to $4$ gives $f(4)=9$ under the same rule. The function $f$ remains fixed; only the input at which you evaluate it changes.

Do not read $f(x)$ as the product of $f$ and $x$. Multiplication would usually be written as $fx$ or $f\cdot x$. In function notation, the parentheses specify the input.

In the following figure, distinguish the rule named $f$ from the values $f(3)$ and $f(4)$ calculated at particular inputs.

<figure class="lesson-figure" markdown="1">

![One fixed rule named f yields value seven at input three and value nine at input four](../../figures/assets/M00/M00-03-function-vs-value.svg)

<figcaption>The symbol f names the rule applied to both inputs. The expressions f(3) and f(4) are the values obtained by applying that rule to each input.</figcaption>
</figure>

Consider the expression

\[
y=f(x)
\]

The symbols have these meanings.

- $x$: the input
- $f$: the function that maps an input to an output
- $f(x)$: the function value at input $x$
- $y$: the name assigned to the output value

In words, “the value obtained by applying the function $f$ to $x$ is $y$.” This expression can be used in solving an equation, but more often it states a function's input–output relationship.

If you are given $x=3$ and calculate $y=f(x)$, you know the input and seek the output. If you instead solve $f(x)=7$, you seek an input that gives the output $7$. The function is the same in both expressions, but the known and unknown quantities differ.

## Core concept 3. A function is more general than a formula

At first, you learn functions through formulas such as $f(x)=2x+1$. A formula is one way to represent a function. A table, an algorithm, or a neural network also defines a function if it assigns one output to each input.

The following table defines a function.

| Input $x$ | Output $f(x)$ |
|---:|---:|
| 1 | 4 |
| 2 | 4 |
| 3 | 7 |

Each input $1,2,3$ has one output. The inputs $1$ and $2$ may share the output $4$.

If this table specifies the entire function, the permitted inputs are $1,2,3$. This information does not determine an output for $4$, which is absent from the table. To permit another input, you must specify its output too. Distinguish a table that records a few evaluations from one that specifies every input–output correspondence of a function.

The following correspondence is not a function.

| Input $x$ | Output |
|---:|---:|
| 1 | 4 |
| 1 | 6 |
| 2 | 7 |

Input $1$ has both outputs $4$ and $6$. There is no unique value to write as $f(1)$.

In the following figure, count the arrows leaving each input. Distinguish several inputs reaching the same output from one input branching to two outputs.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three finite mappings contrast a valid many-to-one function with an input having two outputs and an input having no output](../../figures/assets/M00/M00-03-function-conditions.svg)

<figcaption>On the left, inputs 1 and 2 may share output 4. In the middle, input 1 has two outputs. On the right, domain element 3 has no output. The middle and right correspondences do not satisfy the conditions for a function.</figcaption>
</figure>

## Core concept 4. Domain, codomain, and range

Reading a function requires checking its input and output sets as well as its rule.

\[
f:A\to B
\]

- Domain $A$: the set of all inputs permitted for the function
- Codomain $B$: the set declared to contain the outputs
- Range: the set of outputs obtained from the permitted inputs

Consider the following function.

\[
A=\{1,2,3\},\qquad B=\{a,b,c,d\}
\]

| Input $x$ | $f(x)$ |
|---:|:---:|
| 1 | $a$ |
| 2 | $a$ |
| 3 | $c$ |

Its domain is $\{1,2,3\}$, its codomain is $\{a,b,c,d\}$, and its range is $\{a,c\}$. The codomain elements $b,d$ never occur as outputs.

You specify the domain and codomain when defining the function. You determine its range by collecting the values it produces. A function need not produce every codomain element, but every value obtained from a domain input must belong to the codomain. The absence of $b,d$ from the outputs is allowed. Assigning an output $e$ outside the codomain would contradict the declaration that this is a function from $A$ to $B$.

The range is therefore contained in the codomain.

\[
\text{range}\subseteq \text{codomain}
\]

The two sets may be equal, but they need not be.

In the following figure, distinguish the full codomain from the elements reached by arrows to identify the range.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Domain elements one and two map to a and three maps to c inside codomain a b c d, so only a and c belong to the range](../../figures/assets/M00/M00-03-domain-codomain-range.svg)

<figcaption>The codomain B contains a, b, c, d. Only a and c occur as outputs and belong to the range. Dashed markers identify the output elements reached by the arrows.</figcaption>
</figure>

### The same formula can define different functions with different domains

The formula

\[
f(x)=x^2
\]

does not by itself specify which inputs are permitted. You might choose all real numbers as the domain, or restrict the domain to real numbers greater than or equal to $0$. These input sets differ, so the two choices define different functions mathematically.

This is why papers specify both input and output spaces, as in $f:\mathbb R^d\to\mathbb R^C$. A formula or neural network architecture alone does not fully specify a function's input and output sets.

## Example 1. Calculating function values

### Problem

Given

\[
f(x)=3x-2
\]

calculate $f(0)$, $f(2)$, and $f(-1)$.

### Solution

The value $f(0)$ is obtained by substituting $0$ for $x$.

\[
f(0)=3\cdot 0-2=-2
\]

For $f(2)$, substitute $2$ for $x$.

\[
f(2)=3\cdot 2-2=6-2=4
\]

For $f(-1)$, substitute $-1$ for $x$. Enclosing the negative input in parentheses helps you keep track of the sign.

\[
f(-1)=3\cdot(-1)-2=-3-2=-5
\]

Thus,

\[
f(0)=-2,\qquad f(2)=4,\qquad f(-1)=-5
\]

### Meaning of the result

The three calculations use different inputs with the same function. The function $f$ remains unchanged; its value depends on the input.

## Example 2. Finding the domain, codomain, and range

### Problem

A function $g:A\to B$ is given by

\[
A=\{-1,0,1,2\},\qquad B=\{0,1,2,3,4\}
\]

\[
g(x)=x^2
\]

Find the domain, codomain, and range.

### Solution

The declaration already specifies the domain and codomain.

\[
\text{domain}=A=\{-1,0,1,2\}
\]

\[
\text{codomain}=B=\{0,1,2,3,4\}
\]

To find the range, evaluate the function at every input in the domain.

| $x$ | $g(x)=x^2$ |
|---:|---:|
| $-1$ | $1$ |
| $0$ | $0$ |
| $1$ | $1$ |
| $2$ | $4$ |

Collect the distinct output values to obtain

\[
\text{range}=\{0,1,4\}
\]

The values $2$ and $3$ belong to the codomain but never occur as function values for this domain.

## Example 3. Reading model notation

The following expression represents a parameterized model as a function.

\[
y=f_\theta(x)
\]

- $x$: the input to the model
- $\theta$: parameters that determine the model's calculation
- $f_\theta$: the function determined by parameters $\theta$
- $y$: the output produced by the model

In words, “apply the model function with parameters $\theta$ to input $x$ to obtain output $y$.”

For a small example, let

\[
f_\theta(x)=wx+b,\qquad \theta=(w,b)
\]

If $\theta=(0.8,0.1)$ and $x=2$, then

\[
f_\theta(2)=0.8\cdot 2+0.1=1.7
\]

Changing $x$ gives the same model a different input. Changing $\theta$ changes the function's rule. Training can be viewed as adjusting $\theta$ to fit the data.

This example reduces the number and structure of a neural network's parameters to a small model. In a neural network, $\theta$ may refer to several matrices and vectors together.

## Common misconceptions

### Misconception 1. $f(x)$ is the product of $f$ and $x$

In function notation, parentheses specify the input. The expression $f(x)$ is the result of applying $f$ to $x$. It has a different role from $fx$, where a multiplication sign has been omitted.

### Misconception 2. Different inputs must have different outputs

The condition for a function is that each input has one output. Several inputs may share an output, as in $f(2)=f(-2)=4$.

### Misconception 3. Codomain and range mean the same thing

The codomain is the set declared in advance to contain the outputs. The range is the set of outputs the function produces. The range may be only part of the codomain.

### Misconception 4. A function must be written as a single formula

A table, an algorithm, or a neural network can represent a function if it assigns one output to each input. A formula is one way to express a function's rule.

### Misconception 5. $\theta$ in $f_\theta$ is an input that changes on every evaluation

When describing one inference step, you usually fix $\theta$ and vary $x$ as the input. When analyzing training, you also treat $\theta$ as something that changes over time. Check which process the context describes.

## Exercises

### 1. Reading function notation

Explain each symbol in

\[
z=h(u)
\]

and read the expression as one sentence.

<details>
<summary>Show solution</summary>

$u$ is the input, $h$ is the function, $h(u)$ is the function value at input $u$, and $z$ names the output value. The whole expression reads, “the value obtained by applying the function $h$ to $u$ is $z$.”

</details>

### 2. Calculating function values

Given

\[
p(t)=2t+5
\]

calculate $p(3)$, $p(0)$, and $p(-4)$.

<details>
<summary>Show solution</summary>

\[
p(3)=2\cdot 3+5=11
\]

\[
p(0)=2\cdot 0+5=5
\]

\[
p(-4)=2\cdot(-4)+5=-8+5=-3
\]

Thus, $p(3)=11$, $p(0)=5$, and $p(-4)=-3$.

</details>

### 3. Completing a table

Given

\[
q(x)=x^2+1
\]

complete the following table.

| $x$ | $-2$ | $-1$ | $0$ | $2$ |
|---:|---:|---:|---:|---:|
| $q(x)$ |  |  |  |  |

<details>
<summary>Show solution</summary>

Substitute each input for $x$.

\[
q(-2)=(-2)^2+1=5
\]

\[
q(-1)=(-1)^2+1=2
\]

\[
q(0)=0^2+1=1
\]

\[
q(2)=2^2+1=5
\]

The completed table is

| $x$ | $-2$ | $-1$ | $0$ | $2$ |
|---:|---:|---:|---:|---:|
| $q(x)$ | $5$ | $2$ | $1$ | $5$ |

The distinct inputs $-2$ and $2$ share the output $5$, which satisfies the conditions for a function.

</details>

### 4. Determining whether a correspondence is a function

For the domain $\{1,2,3\}$, identify every correspondence below that is a function and explain why.

- Correspondence A: $1\mapsto a,\ 2\mapsto b,\ 3\mapsto b$
- Correspondence B: $1\mapsto a,\ 1\mapsto c,\ 2\mapsto b,\ 3\mapsto a$
- Correspondence C: $1\mapsto a,\ 2\mapsto b$

<details>
<summary>Show solution</summary>

Correspondence A is a function. Each input in the domain has one output. The inputs $2$ and $3$ may share output $b$.

Correspondence B is not a function. Input $1$ has two outputs, $a$ and $c$.

Correspondence C is also not a function on the given domain. No output is specified for input $3$, which belongs to the domain.

</details>

### 5. Domain, codomain, and range

Let

\[
A=\{0,1,2,3\},\qquad B=\{0,1,2,3,4,5\}
\]

and let $r:A\to B$ be defined by

\[
r(x)=x+1
\]

Find the domain, codomain, and range.

<details>
<summary>Show solution</summary>

The declaration gives domain $A$ and codomain $B$.

\[
\text{domain}=\{0,1,2,3\}
\]

\[
\text{codomain}=\{0,1,2,3,4,5\}
\]

The function values at each input are

\[
r(0)=1,\quad r(1)=2,\quad r(2)=3,\quad r(3)=4
\]

so

\[
\text{range}=\{1,2,3,4\}
\]

The codomain elements $0$ and $5$ never occur as outputs.

</details>

### 6. Decoding model notation

Let

\[
\hat y=f_\theta(x),\qquad f_\theta(x)=wx+b,\qquad \theta=(w,b)
\]

Calculate $\hat y$ when $\theta=(2,-1)$ and $x=4$, and explain how the roles of $x$ and $\theta$ differ.

<details>
<summary>Show solution</summary>

Substitute $w=2$, $b=-1$, and $x=4$.

\[
\hat y=f_\theta(4)=2\cdot 4-1=7
\]

$x$ is an input to a fixed function. The parameters $\theta=(w,b)$ determine the function's rule. Changing only $x$ evaluates the same function at a different input. Changing $\theta$ changes the slope or intercept and therefore gives a different function.

</details>

### 7. Evaluating a claim

Someone makes the following claim.

> Since $s(1)=s(3)=5$, $s$ is not a function.

Determine whether the claim is correct and explain your reasoning using the definition of a function.

<details>
<summary>Show solution</summary>

The claim is incorrect. A function may map different inputs to the same output. The conditions to check are that input $1$ has one specified output and that input $3$ also has one specified output.

The assignments $s(1)=5$ and $s(3)=5$ do not violate the conditions for a function. You must still check whether any other domain input is missing an output or any input has two outputs.

</details>

## Lesson summary

- A function assigns one output in the codomain to each input in the domain.
- $f$ is the function; $f(x)$ is its value at input $x$.
- Different inputs may have the same output.
- The domain contains permitted inputs, the codomain is the specified output set, and the range contains the outputs produced.
- In $y=f_\theta(x)$, $x$ is the input and $\theta$ contains parameters that determine the function's rule.

## Pass criteria

You pass if you can answer the following questions without consulting the material.

- Can you state the two conditions for a function?
- Can you read $f(x)$ and distinguish it from multiplication?
- Can you calculate values of a function given by a small formula?
- Can you distinguish the domain, codomain, and range in a finite example?
- Can you explain the roles of $x$, $y$, $f_\theta$, and $\theta$ in $y=f_\theta(x)$?

## Next lesson

The next lesson is [M00-04 Coordinates and graphs](M00-04-coordinates-graphs.md). It represents input–output correspondences in the coordinate plane and explains how changes to a formula appear in the graph's shape.

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] All new symbols are defined before use.
- [x] The function and function value are distinguished.
- [x] The domain, codomain, and range are checked in finite examples.
- [x] Every exercise has a solution.
- [x] Model notation is restricted to an introductory scope.
- [x] The glossary and notation rules are followed.
- [x] No unannounced prerequisites beyond this lesson's scope are required.
- [x] Internal links and math delimiters are checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
