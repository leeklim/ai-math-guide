---
id: "M00-01"
title: "Numbers, variables, and constants"
part: 1
stage: "M00"
status: "complete"
prerequisites: []
estimated_time: "60~75 minutes"
---

# M00-01. Numbers, variables, and constants

## Why this lesson matters

Formulas in AI papers combine numbers and letters. The same letter can denote an input in one formula and a parameter to be learned by a model in another. Before calculating, you need to distinguish what can change from what is held fixed to follow the formula's meaning.

For example, you may encounter

\[
s=wx+b
\]

Here, $x$ may be an input, while $w$ and $b$ may be values learned by a model. When making a prediction, you vary $x$ while holding $w$ and $b$ fixed. When analyzing training, $w$ and $b$ also change. You therefore cannot identify variables and constants from the letters alone. First check which computation is being described.

## Learning objectives

After completing this lesson, you will be able to:

- Explain the differences between numbers, values, and symbols.
- Identify variables and constants in an expression and describe their roles.
- Evaluate a simple expression by substituting a particular value for a variable.
- Distinguish the contexts in which inputs, parameters, and hyperparameters vary or remain fixed.

## Prerequisite check

There are no prerequisite lessons. You can begin if you can perform:

- Integer addition and multiplication
- Basic arithmetic with negative numbers and fractions
- Evaluation of parenthesized expressions, starting inside the parentheses

If arithmetic is unfamiliar, follow the intermediate steps in each example.

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning in this lesson |
|---|---|---|
| $3$ | `three` | A numeral representing a particular number |
| $x$ | `x` | A variable that can represent multiple values |
| $c$ | `c` | A constant representing a value fixed within a context |
| $\theta$ | `theta` | A symbol often used for parameters learned by a model |
| $\eta$ | `eta` | A symbol often used for hyperparameters such as the learning rate |

A Greek letter is not necessarily a constant, and a Latin letter is not necessarily a variable. The definitions and context surrounding the formula determine a symbol's role.

## Core concepts

### Numbers, values, and symbols

A number is a mathematical object used to express counts, order, magnitude, and related notions. All of the following are numbers.

\[
3,\qquad -2,\qquad \frac12,\qquad 0.75
\]

The written form $3$ is a symbol representing a number. You can represent the same number in different ways, such as 3, 3.0, and $6/2$. Different expressions can represent the same value when their calculations give the same result.

A value is what a number or mathematical object currently represents. For example, if you substitute 3 for $x$, the value of $x$ is 3.

| Distinction | Content |
|---|---|
| Symbol | $x$ |
| Current value | 3 |

A symbol and its value are different. You can keep the symbol $x$ while changing its value to 3, 4, or -1.

The top of the following figure shows different expressions for the same value. The bottom shows different values substituted for the same symbol in separate calculations.

<figure class="lesson-figure" markdown="1">

![Three expressions share the value three, while the symbol x takes three different values in separate calculations](../../figures/assets/M00/M00-01-symbol-value.svg)

<figcaption>3, 3.0, and 6÷2 have the same value. The three rows below keep the symbol x while changing the value it represents.</figcaption>
</figure>

### Variables

A variable is a symbol that can represent one of several permitted values. Depending on the situation, a variable can have several roles.

- It can represent an unknown value.
- It can mark the input position of a function.
- It can represent a quantity varying with time or position.
- It can represent a model parameter updated during training.

Calling something a variable does not require its value to change over time. Even if you set $x=3$ for one calculation, $x$ is a variable if you use $x$ as a position that can take other values.

### Constants

A constant is a value held fixed within a specified context.

Consider

\[
2x+1
\]

Here, $x$ is a variable that can take different values. The numbers 2 and 1 are fixed in this expression, so they are constants.

A constant need not be written directly as a number. You can name it with a letter, as in

\[
cx+1
\]

If a problem specifies that “$c=2$ is fixed,” then $c$ is a constant in that context. If instead you learn $c$ or investigate different values of $c$, $c$ becomes a variable under analysis.

To distinguish variables from constants, ask the following question rather than relying on a letter's appearance.

> In the computation being described, can this value vary, or is it held fixed?

The following figure compares the same expression $cx+1$ in two contexts. The left fixes $c$; the right varies it.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The expression c x plus one fixes c at two while x varies on the left, and fixes x at three while c varies on the right](../../figures/assets/M00/M00-01-variable-constant-context.svg)

<figcaption>On the left, c is a constant fixed at 2. On the right, c is a variable investigated at 1, 2, and 3. Its role depends on what each comparison holds fixed.</figcaption>
</figure>

### Substituting values for variables

In this lesson, substituting a value means choosing a particular value for a variable and evaluating the expression. Substitute $x=3$ into

\[
2x+1
\]

Replace the position occupied by $x$ with 3.

\[
2\cdot3+1
\]

Performing multiplication first gives

\[
6+1=7
\]

Changing the value of $x$ can change the result.

| Value of $x$ | Value of $2x+1$ |
|---:|---:|
| 0 | 1 |
| 1 | 3 |
| 3 | 7 |
| -1 | -1 |

The structure of $2x+1$ remains the same in this table; only the value of $x$ changes.

In the following figure, distinguish the step replacing $x$ with 3 from the steps performing the arithmetic.

<figure class="lesson-figure" markdown="1">

![Replacing x by three in two x plus one is followed by multiplying two by three and adding one to obtain seven](../../figures/assets/M00/M00-01-substitution-steps.svg)

<figcaption>Replacing x with 3 leaves the constants 2 and 1 unchanged. Add 1 to the product 6 to obtain the expression's value, 7.</figcaption>
</figure>

### Roles change with context

Return to the simple model formula

\[
s=wx+b
\]

For now, it is enough to read this as “multiply $w$ by $x$, then add $b$ to obtain the score $s$.”

For a prediction, the roles can be described as follows.

| Symbol | Role | During a prediction |
|---|---|---|
| $x$ | Input | Can vary with new data. |
| $w$ | Learned parameter | Held fixed in the current model. |
| $b$ | Learned parameter | Held fixed in the current model. |
| $s$ | Output score | Computed from the input and parameters. |

During training, however, you change $w$ and $b$ to find better values. In this context, $w$ and $b$ are variables that change over training.

> For a prediction, hold the parameters fixed and compute the output for an input. During training, change the parameters to reduce the loss.

You will use this distinction repeatedly when interpreting model training.

The left of the following figure compares different inputs with the same parameters. The right compares different parameters with the same input. The values on the right illustrate the distinction between roles; they are not actual training results.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Prediction varies the input with fixed model parameters, while a separate parameter comparison varies w and b with the same input](../../figures/assets/M00/M00-01-prediction-training.svg)

<figcaption>A prediction holds the current w and b fixed. In a training analysis, those parameters are updated. The outputs in both tables are calculated by substituting the listed values into s=wx+b.</figcaption>
</figure>

## Example 1. Evaluating an expression by substitution

### Problem

Identify the variable and constants in the following expression, then calculate its value when $x=-2$.

\[
3x+4
\]

### Solution

$x$ is a variable because it can take different values. The numbers 3 and 4 are constants because they are fixed within the expression.

Substituting $x=-2$ gives

\[
3x+4
=
3\cdot(-2)+4
\]

Perform multiplication first.

\[
3\cdot(-2)=-6
\]

Therefore,

\[
-6+4=-2
\]

### What the result means

The expression's structure and its constants 3 and 4 did not change. Setting $x$ to -2 made the entire expression evaluate to -2.

## Example 2. Distinguishing roles in a model formula

### Problem

In the following model, let $w=0.8$, $b=0.1$, and $x=2$.

\[
s=wx+b
\]

Calculate the score $s$ and explain which quantity is the input and which are fixed parameters during a prediction.

### Solution

Substitute the given values.

\[
s
=
0.8\cdot2+0.1
\]

Multiplication gives

\[
0.8\cdot2=1.6
\]

so

\[
s=1.6+0.1=1.7
\]

For this prediction, $x$ is the input, while $w$ and $b$ are the current model's parameters. All three values are specified while you calculate this prediction, but $x$ changes when you supply a new input. Retraining the model can also change $w$ and $b$.

### What the result means

A letter's role does not depend solely on whether its numerical value is currently specified. Check the scope of the computation being described.

## Three common roles in AI formulas

### Inputs

An input is data supplied to a model. The symbol $x$ is commonly used. Actual inputs, such as images, sentences, or sensor measurements, can contain many numbers. For now, think of an input as a single value.

### Parameters

A parameter is a value adjusted by a model through learning. Common symbols include $w$, $b$, and $\theta$.

- For a prediction, hold the current parameters fixed.
- During training, update the parameters.

### Hyperparameters

A hyperparameter is usually a value chosen by a person before running a learning algorithm or selected through a separate search. The learning rate $\eta$ is a typical example.

You can hold $\eta$ fixed in one training run while varying $\eta$ across experiments to compare results. A hyperparameter is therefore not an absolute constant in every situation.

In the following figure, following one row shows a value held fixed within a run. Comparing the two rows shows a choice that differs between experiments.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Learning rate eta stays at zero point zero one throughout run A and at zero point zero two throughout run B, differing across the two experiments](../../figures/assets/M00/M00-01-hyperparameter-context.svg)

<figcaption>This example holds the learning rate fixed from the start to the end of each run. Comparing 0.01 in run A with 0.02 in run B shows that a value fixed within a run can vary between experiments.</figcaption>
</figure>

## Common misconceptions

### Misconception 1. Letters are variables, and numbers are constants

The numbers 2 and 3 directly represent fixed values, but a letter can also represent a constant. If you declare that $c=2$ is fixed, then $c$ is a constant in that context.

### Misconception 2. A variable must keep changing over time

A variable is a symbol that can represent several possible values. Even if you calculate with $x=3$ in one problem, $x$ plays the role of a variable if its position can accept other values.

### Misconception 3. Parameters are always constants

Parameters are fixed when a trained model makes predictions. During training, however, they are repeatedly updated. The same object's role changes with the scope of the analysis.

### Misconception 4. Greek letters are constants

Some Greek letters, such as $\pi$, often denote constants. Others serve different roles: $\theta$ can denote model parameters, $\eta$ a learning rate, and $\lambda$ a regularization strength. A symbol's appearance does not determine its role.

## Exercises

### 1. Identify variables and constants

Distinguish the variable and constants in

\[
5x-2
\]

<details>
<summary>Show solution</summary>

$x$ is a variable because it can take different values. The values 5 and -2 are fixed within the expression, so they are constants.

5 is the fixed value multiplying $x$, and -2 is the fixed value added to the product. Despite their different positions and operations, both remain fixed in this expression.

</details>

### 2. Calculate by substitution

Substitute $x=-2$ into the following expression and calculate its value.

\[
5x-2
\]

<details>
<summary>Show solution</summary>

Replace $x$ with -2.

\[
5\cdot(-2)-2
\]

Performing multiplication first gives

\[
5\cdot(-2)=-10
\]

Therefore,

\[
-10-2=-12
\]

The answer is -12.

</details>

### 3. Substitute different values into the same expression

Evaluate $2x+1$ at $x=0$, $x=2$, and $x=-3$. Explain what remains unchanged as $x$ changes.

<details>
<summary>Show solution</summary>

For $x=0$,

\[
2\cdot0+1=1
\]

For $x=2$,

\[
2\cdot2+1=5
\]

For $x=-3$,

\[
2\cdot(-3)+1=-5
\]

The results differ: 1, 5, and -5. The expression's structure and the constants 2 and 1 remain unchanged. Only the value of $x$ changes.

</details>

### 4. Explain a model formula

Explain the roles of $x$, $w$, $b$, and $s$ during a prediction using

\[
s=wx+b
\]

<details>
<summary>Show solution</summary>

- $x$ is the input supplied to the model.
- $w$ is a learned parameter multiplying the input.
- $b$ is a learned parameter added to the product.
- $s$ is the output score computed from the input and parameters.

For a prediction, hold the current $w$ and $b$ fixed and calculate $s$ for $x$. During training, $w$ and $b$ become variables that are also updated.

</details>

### 5. Determine roles from context

Distinguish the roles of $\theta$, $x$, and $\eta$ in the following description.

> The model receives data $x$ as input. During training, it updates the parameters $\theta$. This training run keeps the learning rate $\eta=0.01$ unchanged until the end.

<details>
<summary>Show solution</summary>

- $x$ is input data. Its value can change with the training example.
- $\theta$ denotes learned parameters. They are variables in the training process because they are repeatedly updated.
- $\eta$ is a hyperparameter fixed at 0.01 for this run, so it is treated as a constant within the run.

Other experiments can vary $\eta$ for comparison. This does not mean that $\eta$ is an absolute constant in every context.

</details>

### 6. Evaluate a claim

Determine whether the following claim is correct, and explain your reasoning.

> Values written with Greek letters are constants, and values written with Latin letters are variables.

<details>
<summary>Show solution</summary>

The claim is false. The type of letter can suggest a convention but does not determine its role.

$\theta$ often denotes learned model parameters, so it can be a variable. Conversely, $c$, taken from the first letter of “constant,” often denotes a fixed value. Whether a symbol is a variable or constant depends on whether its value can vary in the context, not on its appearance.

</details>

## Lesson summary

- A number is a mathematical object representing a value; a symbol represents that number or another object.
- A variable can represent several possible values, while a constant is fixed within a specified context.
- To substitute a value, replace the variable's position with that value and evaluate the expression.
- Inputs, parameters, and hyperparameters have different roles.
- The same parameter can remain fixed during a prediction and vary during training.

## Pass criteria

You pass if you can answer the following questions without consulting the material.

- Can you explain the difference between a symbol and its value?
- Can you distinguish variables from constants using context rather than the appearance of letters?
- Can you evaluate $3x+2$ for a given value of $x$?
- Can you explain how parameters' roles differ between prediction and training?
- Can you refute the claim that Greek letters are constants?

## Next lesson

The next lesson is [M00-02 Expressions, equalities, and equations](M00-02-expressions-equalities-equations.md). You will distinguish a computational expression, a claim that two objects are equal, and a problem asking for an unknown value.

## Author checklist

- [x] Learning objectives describe observable actions.
- [x] All new symbols are defined before use.
- [x] Intuition is distinguished from precise definitions.
- [x] Example calculations have been checked.
- [x] Every exercise has a solution.
- [x] The glossary and notation rules are followed.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Display-math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
