---
id: "A09-CAU-01"
title: "Structural causal models"
part: 4
stage: "A09-CAU"
status: "complete"
prerequisites: ["M04-02", "M04-16", "I07-11"]
estimated_time: "90–120 minutes"
---

# A09-CAU-01. Structural causal models

## Why this lesson matters

A correlation graph depicts statistical connections between variables, but it does not determine intervention outcomes. A structural causal model defines each endogenous variable as a function of its parents and exogenous noise. Before using causal language for a model circuit, specify its nodes, equations, and intervention targets.

## Learning objectives

- Distinguish exogenous variables, endogenous variables, and structural equations in an SCM.
- Draw a causal graph from structural equations.
- Explain how equations and a noise distribution generate an observational distribution.
- Explain the variable choices needed to interpret a neural network computation graph as an SCM.

## Prerequisite check

- Prerequisite lessons: [M04-02 Conditional probability and Bayes' rule](../../part-1-foundations/M04/M04-02-conditional-probability-bayes-rule.md), [M04-16 Correlation and causation](../../part-1-foundations/M04/M04-16-correlation-causation.md), [I07-11 Representing a circuit as a graph](../../part-3-interpretability/I07/I07-11-circuit-graph.md)
- Check question: Does knowing a joint distribution alone uniquely determine the distribution after an intervention that changes an equation?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $\mathcal M=(U,V,F,P_U)$ | `the structural causal model M` | A collection of exogenous and endogenous variables, equations, and a noise distribution | model object |
| $X=f_X(\operatorname{pa}_X,U_X)$ | `X equals f sub X of the parents of X and U sub X` | The structural equation for $X$ | assignment |
| $\operatorname{pa}_X$ | `the parents of X` | Variables with direct incoming edges into $X$ in the graph | set of variables |
| $G_{\mathcal M}$ | `the causal graph induced by M` | The directed graph determined by the structural equations | graph |

## Core concepts

### Variables and the rules that generate their values

In an SCM $\mathcal M=(U,V,F,P_U)$, $U$ is the collection of exogenous variables whose generating processes are not explained within the model, and $V$ is the collection of endogenous variables whose values are determined by structural equations. Exogenous does not mean that a variable has no causes in the real world. It marks the boundary between what the researcher explains computationally and what is taken as given background. Each $X\in V$ has an equation

$$
X=f_X(\operatorname{pa}_X,U_X)
$$

Here, $\operatorname{pa}_X$ denotes the endogenous parents used directly to compute $X$, and $U_X$ denotes the exogenous variables entering that computation. Several equations may share the same exogenous variable. $F$ is the collection of these functions. Fixing the function and all its input values also fixes $X$. Even in an SCM with noise, randomness can therefore be represented through variation in $U$, without separately making the functions themselves random.

A structural equation specifies the direction of assignment. Algebraically solving $Y=2X+U_Y$ as $X=(Y-U_Y)/2$ does not change the original model into one that generates $X$ from $Y$. This assignment direction also determines which generating rule an intervention replaces.

The two flows below distinguish the direction of assignment from solving backward for the same numerical values.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Forward structural assignment computes Y from X and background noise, while algebraic inversion solves the same numbers without changing the causal mechanism.](../../figures/assets/A09-CAU/A09-CAU-01-assignment-and-inverse.svg)

<figcaption>Y=2X+U_Y is a rule that takes X and U_Y and assigns Y. The inverse calculation below solves for X=1 from the already given values Y=3 and U_Y=1. Solving the same numerical relation backward does not change the rule that generates X or the equation replaced by an intervention.</figcaption>

</figure>

### From equations to a graph

Place an edge $Z\to X$ in the graph if changing the endogenous variable $Z$ can change the value of $f_X$ while its other inputs are held fixed. A variable listed as a function argument but unused in the computation does not count as a parent. An edge means that direct influence is possible for some permitted inputs, not that a change appears in every sample. At particular inputs, another factor in a product may be zero, or a nonlinear function may be saturated, so the change has no effect.

This directed graph summarizes parent relationships. Numerical coefficients, functional forms, and noise distributions are needed separately. Dependence among exogenous variables must also be included in $P_U$. Endogenous directed edges alone do not represent that confounding if the exogenous dependence is omitted.

Read the edges from the equations, then examine a case where an edge has no effect in a particular sample.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Exogenous U sub X, U sub M and U sub Y feed endogenous X, M and Y; the equations imply X to M, M to Y and X to Y.](../../figures/assets/A09-CAU/A09-CAU-01-equations-to-graph.svg)

<figcaption>The blue U variables are background supplied from outside the model; the green X, M, and Y variables are determined by structural equations. The purple edges show the endogenous parents used in the equations: X→M, M→Y, and X→Y. The joint law of U is specified separately in P_U. Drawing three separate U variables does not assume their independence.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![The illustrative product f of z,t equals z times t changes with z when t equals one but stays zero at t equals zero despite a possible parent edge.](../../figures/assets/A09-CAU/A09-CAU-01-possible-edge-zero-sample.svg)

<figcaption>For the illustrative function f(z,t)=zt, changing z changes the value when t=1, but the output stays at zero under the same change in z when t=0. A parent edge is included when direct influence is possible at some permitted inputs. It does not guarantee a nonzero effect in every sample.</figcaption>

</figure>

### From a noise distribution to an observational distribution

$P_U$ is the joint distribution of all of $U$. Knowing each noise variable's marginal distribution is different from knowing their joint distribution. Independence allows the joint distribution to be written as the product of its marginals, but calling a model an SCM does not itself assume independence.

In an acyclic SCM, first draw a value $u$ from $P_U$, then execute all the equations in a topological order that computes parents before children. The result is one observational sample of the endogenous variables. Repeating this process gives the observational distribution. Noise independence is not required for this procedure. The probability factorization by parents in the next lesson, however, requires additional conditions.

Compare how two joint noise distributions with the same marginals produce different observational distributions.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two binary noise laws have identical marginals but independent joint draws generate Y values zero,one,two while perfectly paired draws generate only zero and two.](../../figures/assets/A09-CAU/A09-CAU-01-joint-noise-output-law.svg)

<figcaption>With X=U_X=0 fixed, both cases use the equation Y=U_M+U_Y. Each noise marginal assigns probability 0.5 to zero and one. The independent joint distribution on the left assigns probability 0.25 to each of the four combinations; the joint distribution on the right assigns probability 0.5 only to (0,0) and (1,1). Despite identical marginals, the probability masses of Y are (0.25,0.5,0.25) and (0.5,0,0.5).</figcaption>

</figure>

### Choosing nodes in a computation graph

A feed-forward neural network can be represented as an SCM under fixed parameters and evaluation settings, with inputs as exogenous variables and activations and outputs as endogenous variables. For a single run with fixed input, each activation is determined deterministically. A distribution over prompts also induces distributions over activations and outputs. If dropout or sampling is included, the corresponding random draws must be included in the background variables and execution contract.

The researcher chooses whether a node is a neuron, a head, a subspace, or a residual component. Treating a head output as a vector node allows an intervention replacing that vector. Treating just one coordinate within it as a node changes the intervention target. To treat overlapping subspaces as independent nodes, first specify how the remaining components are held fixed and how the original activation is reconstructed. Node grouping and reconstruction rules determine the permitted interventions and the scope of causal claims.

Below, distinguish a whole-vector intervention from a one-coordinate intervention, then examine the reconstruction problem caused by shared subspace components.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An illustrative head vector two,five becomes one,three under whole-vector replacement but one,five when only its first coordinate is replaced.](../../figures/assets/A09-CAU/A09-CAU-01-vector-coordinate-nodes.svg)

<figcaption>Start with the illustrative vector h=(2,5)ᵀ at the same hook. Replacing the vector node changes both components to (1,3)ᵀ. Defining only the first coordinate as the node preserves the other component, 5, and gives (1,5)ᵀ. Node grouping changes the unit of manipulation, so these interventions differ even with the same layer, token, and hook.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Orthogonal projections of vector two,one,one onto coordinate planes A and B both contain the shared e1 component two, so their sum four,one,one double-counts it.](../../figures/assets/A09-CAU/A09-CAU-01-shared-subspace-coordinate.svg)

<figcaption>Projecting the illustrative h=(2,1,1)ᵀ onto A=span{e₁,e₂} and B=span{e₁,e₃} gives (2,1,0)ᵀ and (2,0,1)ᵀ. Both projections contain the shared e₁ component, 2, so their sum is (4,1,1)ᵀ. When defining overlapping subspaces as nodes, specify preservation and reconstruction rules to avoid counting shared components twice.</figcaption>

</figure>

## Small example

$$
X=U_X,
\qquad M=2X+U_M,
\qquad Y=M+X+U_Y
$$

The graph contains $X\to M$, $M\to Y$, and $X\to Y$. For one sample with $(U_X,U_M,U_Y)=(1,0,0)$, compute $X=1$, $M=2$, and $Y=3$ in that order. Substitution gives $Y=3U_X+U_M+U_Y$, so the distribution of $Y$ depends on the joint distribution of the three noise variables. Drawing independent noise and drawing correlated noise can produce different observational distributions under the same equations.

Changing the coefficient in the equation for $M$ from 2 to 4 leaves the directed edges unchanged but changes the computation. Holding the same background values fixed, increasing $X$ by one unit increases $Y$ by 3 in the original model and by 5 in the modified model. This is why the graph alone does not determine the numerical effect.

Follow the execution order for one background draw, then compare the outcomes of two models that differ only in the coefficient.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A joint background draw of one,zero,zero generates X equals one, M equals two and Y equals three in topological order, with X also entering Y directly.](../../figures/assets/A09-CAU/A09-CAU-01-topological-sample.svg)

<figcaption>Draw (U_X,U_M,U_Y)=(1,0,0) once, then compute X=1, M=2, and Y=3 in order. The bypass line below shows that X enters the equation for Y directly, in addition to its contribution through M. The resulting (X,M,Y) is one observational sample.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![With all noise zero, the same X-to-M-to-Y graph and direct X-to-Y path produce Y equals three X or five X after changing the M coefficient.](../../figures/assets/A09-CAU/A09-CAU-01-same-graph-different-effect.svg)

<figcaption>In the small example with U_M=U_Y=0, M=2X gives Y=3X, whereas M=4X gives Y=5X. The directed parent relationships stay the same, but a one-unit change in X changes Y by 3 or 5. The graph's shape alone does not determine the numerical effect.</figcaption>

</figure>

## Common misconceptions

- Directed edges cannot automatically be read from observed correlations.
- An edge in a computation graph does not mean that its component causes a human-level concept.

## Exercises

### 1. Graph
List the directed edges for $A=U_A$, $B=A+U_B$, and $C=AB+U_C$.
<details><summary>Show solution</summary>

The edges are $A\to B$, $A\to C$, and $B\to C$.
</details>

### 2. Exogenous variables
Which of $U_A,U_B,U_C$ and $A,B,C$ are endogenous variables in the model above?
<details><summary>Show solution</summary>

$A,B,C$ are endogenous variables because their values are determined by structural equations.
</details>

### 3. Same graph
If two SCMs have the same graph, must their numerical intervention effects also be the same?
<details><summary>Show solution</summary>

They need not be. Different structural functions and exogenous distributions can change the magnitude and form of the effect.
</details>

### 4. Model interpretation
To define one attention head as a causal node, what output and downstream edges must be specified?
<details><summary>Show solution</summary>

Specify which token position's head output is used, whether it is the vector added to the residual stream, and which downstream computation is measured as the outcome.
</details>

## Sources and update boundaries

This lesson uses acyclic SCMs. Cyclic equilibrium models and the detailed theory of latent variable identification are outside its scope.

The definitions of structural assignment and exogenous dependence were checked against Sections 3.1–3.2 of [Pearl, An Introduction to Causal Inference](https://ftp.cs.ucla.edu/pub/stat_ser/r354-reprint-corrected.pdf). The numerical calculations in the text directly substitute values into the equations of the example above.

## Lesson summary

- An SCM collects variables, structural equations, and an exogenous distribution.
- A causal graph represents the parent relationships in the equations.
- An observational distribution alone does not automatically determine the result of replacing an equation.
- Causal nodes in a neural circuit must be defined for the purpose of the analysis.

## Pass criteria

- Can you identify the graph and variable types from equations?
- Can you specify the unit of manipulation when treating an internal component as a causal node?

## Next lesson

- [A09-CAU-02 The do-operator and interventions](A09-CAU-02-do-operator-interventions.md)

## Author checklist

- [x] Explained SCM variables, equations, graphs, and the choice of internal nodes.
- [x] All four exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Checked prerequisites and links.

