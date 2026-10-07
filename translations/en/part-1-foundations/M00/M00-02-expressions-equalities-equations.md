---
id: "M00-02"
title: "Expressions, equalities, and equations"
part: 1
stage: "M00"
status: "complete"
prerequisites:
  - "M00-01"
estimated_time: "60~75 minutes"
---

# M00-02. Expressions, equalities, and equations

## Why this lesson matters

Before calculating with mathematical symbols, determine what the formula is doing. The following three expressions look similar but have different roles.

\[
2x+1
\]

\[
2+3=5
\]

\[
2x+1=7
\]

The first is an expression whose value can be calculated. The second claims that its left- and right-hand sides are equal. The third can be used to ask which $x$ makes the two sides equal. These distinctions help you determine whether a formula in a paper is a definition, a calculation result, or a condition to satisfy.

## Learning objectives

After completing this lesson, you will be able to:

- Distinguish expressions, equalities, and equations.
- Read $=$ as stating that both sides have the same value.
- Solve a simple linear equation by applying the same operation to both sides.
- Distinguish the definition symbol $\coloneqq$ from an ordinary equality sign.
- Use context to determine whether an equality in an AI formula gives a computation rule or a condition to satisfy.

## Prerequisite check

- [M00-01 Numbers, variables, and constants](M00-01-numbers-variables.md)
- You should be able to distinguish variables from constants.
- You should be able to evaluate an expression by substituting a given value for a variable.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning |
|---|---|---|
| $+$ | `plus` | Adds two values. |
| $-$ | `minus` | Subtracts the right-hand value from the left-hand value. |
| $=$ | `equals` | The two sides represent the same value. |
| $\neq$ | `is not equal to` | The two sides have different values. |
| $\coloneqq$ | `is defined as` | Defines the meaning of the left-hand symbol using the right-hand expression. |
| Left-hand side | `left-hand side` | The part to the left of the equality sign |
| Right-hand side | `right-hand side` | The part to the right of the equality sign |

## Core concepts

### Expressions

An expression combines numbers, variables, and operations.

\[
2x+1
\]

This expression contains the variable $x$, constants 2 and 1, multiplication, and addition. Once the value of $x$ is specified, you can calculate the value of the entire expression.

An expression by itself does not assert something true or false. You cannot judge $2x+1$ alone as correct or incorrect because it does not compare two objects.

### Equalities

An equality uses $=$ to state that the left- and right-hand sides have the same value.

\[
2+3=5
\]

The left side evaluates to 5, and the right side is also 5, so this equality is true.

In contrast,

\[
2+3=6
\]

is false because the left side is 5 and the right side is 6.

An equality sign is not an arrow saying “perform the next calculation.” It states that both sides represent the same value. Every part must therefore have the same value when you chain equalities as follows.

\[
2+3=5=10-5
\]

All three expressions evaluate to 5, so this notation is correct.

### Equalities containing letters

An equality containing letters can be true or false depending on the variable values.

\[
x+2=5
\]

Substituting $x=3$ gives

\[
3+2=5
\]

which is true. Substituting $x=1$ gives

\[
1+2=5
\]

which is false.

An equality is therefore not automatically an equation merely because it contains a letter. Check the purpose for which the equality is being used.

### Equations

An equation is an equality treated as a problem asking which values of an unknown make it true.

\[
2x+1=7
\]

Solving this equation means finding $x$ that makes its left- and right-hand sides equal.

A solution is a value that makes the equality true. The solution of the equation above is $x=3$.

\[
2\cdot3+1=7
\]

You can check it by calculating the left side, which gives 7.

The following figure distinguishes an expression to evaluate, a comparison of two values, and a question asking for an unknown. Use these distinctions to identify the roles of the symbols.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An expression computes a value, an equality compares five with five, and an equation asks for x that makes two x plus one equal seven](../../figures/assets/M00/M00-02-expression-equality-equation.svg)

<figcaption>An expression has no equality sign comparing two values. An equality compares both sides; an equation asks for an unknown that makes the comparison true.</figcaption>
</figure>

### Applying the same operation to both sides

To solve an equation, apply the same operation to both sides while preserving the equality.

The aim is to remove the quantities added to or multiplied by $x$, leaving $x$ alone. In $2x+1$, you multiply before adding 1, so subtract 1 first and then divide by 2. Changing only one side can destroy the equality, so apply the same operation to the right-hand side.

\[
2x+1=7
\]

First subtract 1 from both sides.

\[
2x+1-1=7-1
\]

Simplifying gives

\[
2x=6
\]

Now divide both sides by 2.

\[
\frac{2x}{2}=\frac{6}{2}
\]

Therefore,

\[
x=3
\]

You can think of a balance scale: adding or removing the same objects on both sides preserves balance. The addition, subtraction, and division by a nonzero number used here can be reversed. A value satisfying the original equation therefore also satisfies the transformed equation, and a solution of the transformed equation also satisfies the original. This is why each step preserves the same solution. Division by 0 is undefined and cannot be used in this process.

The two columns in the following figure receive the same operations. Following them downward while preserving the middle equality sign leaves $x$ alone.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Both sides of two x plus one equals seven subtract one and divide by two, preserving equality until x equals three](../../figures/assets/M00/M00-02-balanced-operations.svg)

<figcaption>Subtract 1 from both sides, then divide both sides by 2. Every row is an equality with the same solution, x=3.</figcaption>
</figure>

### Equalities holding for every value

Consider

\[
2(x+1)=2x+2
\]

This remains true at $x=0$, $x=3$, and $x=-1$. By the distributive law, it holds for every permitted $x$. An equality holding for every permitted value of its variables is called an identity.

The distinction between an equation and an identity is as follows.

| Type | Question |
|---|---|
| Equation | For which values is the equality true? |
| Identity | Is the equality true for every permitted value? |

For this lesson, you only need to recognize the distinction. You will work with transformations of identities repeatedly in later lessons.

### A symbol for definitions

You can use the following symbol to define the meaning of a new symbol.

\[
s\coloneqq wx+b
\]

Read this as “$s$ is defined as $wx+b$.” From this point onward, $s$ denotes the result of computing $wx+b$.

Many papers also use an ordinary equality sign for definitions.

\[
s=wx+b
\]

When reading a formula, check the surrounding sentences rather than relying on one symbol.

- “We define” or “let” often introduces a definition.
- “Satisfies” may introduce a condition to be satisfied.
- “Solve” or “find” may indicate an equation used to find an unknown.

## Example 1. Distinguishing three kinds of expression

### Problem

Classify the following as an expression, an equality, or an equation.

1. $3x-4$
2. $3+4=7$
3. Find $x$ in $3x-4=8$.

### Solution

The first has no equality sign. It is an expression consisting of numbers, a variable, and operations.

The second has an equality sign stating that both sides represent the same value. It is an equality.

The third is also an equality, but its stated purpose is to find $x$. It is therefore being used as an equation in the unknown $x$.

### What the result means

An equation does not use a completely different kind of symbol from an equality. It is an equality used to find the value of an unknown.

## Example 2. Solving a linear equation

### Problem

Solve the following equation and check the solution by substitution into the original expression.

\[
3x+4=19
\]

### Solution

Subtract 4 from both sides.

\[
3x+4-4=19-4
\]

\[
3x=15
\]

Divide both sides by 3.

\[
\frac{3x}{3}=\frac{15}{3}
\]

\[
x=5
\]

Substituting the solution into the original expression gives

\[
3\cdot5+4=15+4=19
\]

so the two sides are equal.

### What the result means

$x=5$ is more than a computation result: it is a value making the original equality $3x+4=19$ true.

## Example 3. Reading equality signs in AI formulas

Consider

\[
s=wx+b
\]

If the surrounding text defines $s$ as the model's output score, this equality gives the rule for computing $s$. Usually, you are not treating $s$ as an unknown and solving an equation. Given the input $x$ and parameters $w$ and $b$, you evaluate the right-hand side to obtain $s$.

If instead the question asks you to find an input $x$ that makes the output score $s$ equal to 7, you can use

\[
wx+b=7
\]

as an equation in $x$. The same form of equality can have different roles depending on the question.

The following figure compares computing an output from a known input with finding an input for a specified output.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Defining s as two x plus one computes a score from input three, whereas requiring score seven asks for the input that satisfies the equation](../../figures/assets/M00/M00-02-definition-vs-condition.svg)

<figcaption>The left defines the computation rule for s and calculates s from a given x. The right asks for x satisfying the target score 7. Read the surrounding question to identify what is given and what must be found.</figcaption>
</figure>

## Common misconceptions

### Misconception 1. An equality sign indicates computation order

An equality sign states that both sides have the same value. To show computation order, use separate lines of equalities or arrows as appropriate.

Incorrect example:

\[
2+3=5+4=9
\]

The first equality sign claims that $2+3$ equals $5+4$. These evaluate to 5 and 9, respectively, so the claim is false.

You can separate the correct calculations as follows.

\[
2+3=5
\]

\[
5+4=9
\]

### Misconception 2. Every equality is an equation

$2+3=5$ is not a problem asking for an unknown. It is a true equality. Depending on the context, $s=wx+b$ can also define an output.

### Misconception 3. A term changes sign by itself when moved to the other side

“Moving a term changes its sign” is shorthand for a calculation. You are applying the same addition or subtraction to both sides.

In

\[
x+2=5
\]

2 does not move to the right on its own. You subtract 2 from both sides.

\[
x+2-2=5-2
\]

### Misconception 4. Mathematical equality and program assignment are always the same

Mathematical $=$ usually states that both sides have the same value. An assignment statement in a programming language may be an instruction to store a value under a name or bind the name to it. Check the symbol's role in the language and context.

## Exercises

### 1. Classify expressions

First classify each item as an expression or equality. If it includes a question asking for an unknown, also identify it as an equation.

1. $4y+1$
2. $8-3=5$
3. Find $y$ in $4y+1=13$.

<details>
<summary>Show solution</summary>

1. $4y+1$ has no equality sign, so it is an expression.
2. $8-3=5$ is an equality stating that both sides have the same value.
3. $4y+1=13$ is an equality used to find $y$, so it is an equation.

</details>

### 2. Determine whether equalities are true or false

Determine whether each equality is true or false.

1. $7-2=5$
2. $3\cdot4=11$
3. $2+5=10-3$

<details>
<summary>Show solution</summary>

1. The left side is 5, and the right side is also 5, so the equality is true.
2. The left side is 12, and the right side is 11, so the equality is false.
3. The left side is 7, and the right side is also 7, so the equality is true.

Calculate the two sides separately and compare them across the equality sign.

</details>

### 3. Determine truth for different variable values

Substitute $x=5$ and $x=2$ into $x+3=8$ and determine whether each resulting equality is true or false.

<details>
<summary>Show solution</summary>

Substituting $x=5$ gives

\[
5+3=8
\]

which is true.

Substituting $x=2$ gives

\[
2+3=8
\]

The left side is 5, and the right side is 8, so this is false.

The same equality can be true or false depending on the variable value.

</details>

### 4. Solve an equation

Solve the following equation and check the solution by substitution into the original equality.

\[
4x-3=9
\]

<details>
<summary>Show solution</summary>

Add 3 to both sides.

\[
4x-3+3=9+3
\]

\[
4x=12
\]

Divide both sides by 4.

\[
x=3
\]

Substituting into the original expression gives

\[
4\cdot3-3=12-3=9
\]

so the solution is $x=3$.

</details>

### 5. Determine whether an equality is an identity

Determine whether the following equality holds for every $x$.

\[
2(x+3)=2x+6
\]

<details>
<summary>Show solution</summary>

Multiplying each term in the parentheses on the left by 2 gives

\[
2(x+3)=2x+6
\]

The expanded left-hand side equals the right-hand side, so the equality holds for every permitted $x$. It is therefore an identity.

Checking a few numerical values can provide intuition. The conclusion for every value, however, follows from the transformation using the distributive law.

</details>

### 6. Distinguish a definition from an equation

You read the following sentence in a paper.

> Define the output score $s$ as $wx+b$.

Write this as a formula and explain whether the equality sign here asks you to solve an equation.

<details>
<summary>Show solution</summary>

To emphasize the definition, write

\[
s\coloneqq wx+b
\]

An ordinary equality sign, $s=wx+b$, is also used. In this context, the formula defines how to calculate the output score $s$ from the input and parameters. It does not ask you to solve an equation for an unknown.

</details>

## Lesson summary

- An expression combines numbers, variables, and operations without itself asserting something true or false.
- An equality claims that both sides of the equality sign have the same value.
- An equation asks for values of an unknown that make an equality true.
- To solve an equation, apply the same operation to both sides.
- An identity holds for every permitted value of its variables.
- The same form of equality can serve as a definition, computation rule, or equation depending on the context.

## Pass criteria

You pass if you can answer the following questions without consulting the material.

- Can you explain the different roles of $2x+1$, $2+3=5$, and $2x+1=7$?
- Can you read an equality sign as stating that both sides have the same value?
- Can you solve $3x+4=19$ by applying the same operation to both sides?
- Can you explain the difference between an equation and an identity?
- Can you use the surrounding context to determine whether $s=wx+b$ is a definition or an equation?

## Next lesson

The next lesson is [M00-03 Function inputs and outputs](M00-03-functions-input-output.md). You will express substitution rules as functions and read the relations between inputs and outputs.

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] All new symbols are defined before use.
- [x] The roles of equality and definition symbols are distinguished.
- [x] Equation solutions have been checked in the original expressions.
- [x] Every exercise has a solution.
- [x] The glossary and notation rules are followed.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Display-math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
