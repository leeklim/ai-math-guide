---
id: "M03-15"
title: "Introduction to reparameterization and model symmetries"
part: 1
stage: "M03"
status: "complete"
prerequisites:
  - "M03-03"
  - "M03-06"
  - "M03-13"
  - "M03-14"
estimated_time: "145~175 minutes"
---

# M03-15. Introduction to reparameterization and model symmetries

## Why this lesson matters

Different neural network parameters might seem to imply different model functions. Yet reordering hidden units or scaling a ReLU unit's incoming and outgoing weights reciprocally can leave the input–output function unchanged. Interpreting a function by fixing the meaning of one parameter coordinate or one neuron's value can therefore give different explanations of the same model.

Reparameterization expresses the same object or function family using different parameters. Model symmetries are transformations that change parameters while preserving the model function. This distinction is needed when studying loss landscapes, neuron matching, model merging, representation comparisons, and identifiability.

## Learning objectives

After completing this lesson, you will be able to:

- Distinguish reparameterization from model symmetry.
- Express gradient transformations under reparameterization as VJPs.
- Define an equivalence relation on parameters representing the same model function.
- Calculate how a linear hidden change of basis preserves function outputs.
- Verify hidden-unit permutation and ReLU positive scaling symmetries.
- Explain why an arbitrary change of basis is not a symmetry of an elementwise nonlinear layer.
- Explain the limitations that parameter nonidentifiability places on model interpretation and comparison.

## Prerequisite check

- Prerequisite lesson: [M03-03 Change of basis and coordinate dependence](M03-03-change-of-basis-coordinate-dependence.md)
- Prerequisite lesson: [M03-06 Equivalence relations and quotient spaces](M03-06-equivalence-relations-quotient-spaces.md)
- Prerequisite lesson: [M03-13 JVP and VJP](M03-13-jvp-vjp.md)
- Prerequisite lesson: [M03-14 Automatic differentiation and backpropagation](M03-14-automatic-differentiation-backpropagation.md)
- Check: Can you distinguish a similarity transformation from a coordinate change?
- Check: Can you explain how an equivalence relation groups multiple representations into one class?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning |
|---|---|---|
| $f_{\boldsymbol\theta}$ | `f sub theta` | The model function specified by parameters $\boldsymbol\theta$ |
| $r(\boldsymbol\phi)=\boldsymbol\theta$ | `r of phi equals theta` | A reparameterization map from new parameters to existing parameters |
| $\boldsymbol\theta\sim\boldsymbol\theta'$ | `theta is equivalent to theta prime` | The equivalence relation that two parameter settings represent the same model function |
| symmetry transformation | `symmetry transformation` | A parameter transformation preserving the model function |
| orbit | `orbit` | The set reachable from one parameter setting through specified symmetry transformations |
| identifiability | `identifiability` | The property that observable functions or distributions uniquely determine the parameters |
| $\mathbf P$ | `P` | An invertible matrix changing or permuting hidden units |
| $\mathbf D$ | `D` | A positive diagonal scaling matrix |

## Core concept 1. Reparameterization changes the parameter representation

Let $\boldsymbol\theta$ denote existing parameters and $\boldsymbol\phi$ new parameters. Using a map

\[
\boldsymbol\theta=r(\boldsymbol\phi)
\]

to represent the same model family as

\[
f_{r(\boldsymbol\phi)}
\]

is a reparameterization. The map $r$ may be a one-to-one coordinate change or a redundant representation in which multiple $\boldsymbol\phi$ map to the same $\boldsymbol\theta$.

“The same model family” means that every function in the original family can be represented by at least one new parameter setting. If the range of $r$ represents only some functions, it restricts the family rather than merely expressing the same family differently. Because several parameter settings may represent one function, covering all original parameter points and representing all model functions are also distinct conditions.

If the existing parameters are $\boldsymbol\theta\in\mathbb R^p$ and the new parameters are $\boldsymbol\phi\in\mathbb R^q$, then $\mathbf J_r(\boldsymbol\phi)$ has shape $p\times q$. A differentiable $r$ maps a new displacement to a first-order change in the existing parameters, and the loss differential measures that change as a scalar.

Writing the loss as $\widetilde L(\boldsymbol\phi)=L(r(\boldsymbol\phi))$, the chain rule gives

\[
\nabla_{\boldsymbol\phi}\widetilde L
=\mathbf J_r(\boldsymbol\phi)^\top
\nabla_{\boldsymbol\theta}L
\]

The gradient in the new coordinates is thus the VJP of the existing gradient through the reparameterization map. Even for the same loss, Euclidean gradient components and norms may depend on parameter coordinates.

The gradient of $L$ is evaluated at the existing point $\boldsymbol\theta=r(\boldsymbol\phi)$. The first-order loss change for a new displacement $\Delta\boldsymbol\phi$ is $\nabla_{\boldsymbol\theta}L^\top\mathbf J_r\Delta\boldsymbol\phi$. Reading this as a row acting on $\Delta\boldsymbol\phi$ and transposing gives the $q$-dimensional gradient above. This column representation uses standard Euclidean inner products in both parameter spaces. The chain rule remains valid even when $r$ is not invertible.

## Core concept 2. A model symmetry is an active transformation preserving the function

If an invertible parameter transformation $T$ satisfies

\[
f_{T(\boldsymbol\theta)}(\mathbf x)=f_{\boldsymbol\theta}(\mathbf x)
\]

for every allowed input $\mathbf x$, $T$ is a symmetry transformation of the model. It is treated as active here because it changes numerical values within parameter space. This differs from a passive coordinate change that writes the same vector in different coordinates.

An equivalence relation between parameter settings can be defined by

\[
\boldsymbol\theta\sim\boldsymbol\theta'
\quad\Longleftrightarrow\quad
f_{\boldsymbol\theta}(\mathbf x)=f_{\boldsymbol\theta'}(\mathbf x)
\text{ for all }\mathbf x
\]

When the object of interpretation is the function, this equivalence class may be more fundamental than an individual parameter point.

Function equality is reflexive, symmetric, and transitive, so this is an equivalence relation. The set reached by applying specified symmetry transformations to a point is its orbit. Each transformation preserves the function, so the orbit lies within the class representing that function. But the chosen permutations or scalings need not connect every parameter setting with the same function. Distinguish a function equivalence class from the orbit of a particular transformation class.

## Core concept 3. Linear hidden layers have change-of-basis symmetries

Suppose no nonlinear function separates two linear layers:

\[
\mathbf h=\mathbf W_1\mathbf x,\qquad
\mathbf y=\mathbf W_2\mathbf h.
\]

For an invertible matrix $\mathbf P$, changing the weights to

\[
\mathbf W_1'=\mathbf P\mathbf W_1,
\qquad
\mathbf W_2'=\mathbf W_2\mathbf P^{-1}
\]

gives

\[
\mathbf W_2'\mathbf W_1'
=\mathbf W_2\mathbf P^{-1}\mathbf P\mathbf W_1
=\mathbf W_2\mathbf W_1
\]

The hidden coordinates change to $\mathbf h'=\mathbf P\mathbf h$, but the input–output function remains the same. This is one reason individual coordinates of a linear hidden representation are difficult to interpret as having independently fixed meanings.

The following structure shows the next layer compensating for changed hidden coordinates through the inverse transformation.

<figure class="lesson-figure" markdown="1">

![The first linear weight inserts P and the second inserts P inverse so the two compensate and preserve the output](../../figures/assets/M03/M03-15-linear-basis-compensation.svg)

<figcaption>Between two linear layers, P and P⁻¹ are adjacent and cancel. Although hidden values Ph change, the final value read by W2 remains the same. Inserting a nonlinear function between them prevents this cancellation from being applied directly.</figcaption>

</figure>

## Core concept 4. Elementwise nonlinear layers allow fewer transformations

For a nonlinear layer

\[
\mathbf h=\sigma(\mathbf W_1\mathbf x+\mathbf b_1),
\qquad
\mathbf y=\mathbf W_2\mathbf h+\mathbf b_2
\]

using the same prescription as for linear layers, $\mathbf W_1'=\mathbf P\mathbf W_1$, $\mathbf b_1'=\mathbf P\mathbf b_1$, and $\mathbf W_2'=\mathbf W_2\mathbf P^{-1}$, as a function-preserving transformation for all parameters requires

\[
\sigma(\mathbf P\mathbf z)=\mathbf P\sigma(\mathbf z)
\]

for every $\mathbf z$. A general elementwise nonlinear function and arbitrary $\mathbf P$ do not satisfy this condition. Thus, not every hidden change of basis available in linear layers can be applied unchanged to nonlinear neural networks.

Write the original preactivation as $\mathbf z=\mathbf W_1\mathbf x+\mathbf b_1$. The new preactivation is $\mathbf P\mathbf z$, and the new output is $\mathbf W_2\mathbf P^{-1}\sigma(\mathbf P\mathbf z)+\mathbf b_2$. When $\sigma(\mathbf P\mathbf z)=\mathbf P\sigma(\mathbf z)$, the two middle matrices cancel to give the original output. Unlike the preceding section, an intervening nonlinear function prevents direct cancellation of $\mathbf P^{-1}\mathbf P$.

A permutation matrix $\mathbf P$, however, commutes with an elementwise function.

\[
\sigma(\mathbf P\mathbf z)=\mathbf P\sigma(\mathbf z).
\]

Thus,

\[
\mathbf W_1'=\mathbf P\mathbf W_1,\quad
\mathbf b_1'=\mathbf P\mathbf b_1,\quad
\mathbf W_2'=\mathbf W_2\mathbf P^{-1}
\]

only reorders hidden units and preserves the function.

A permutation moves each component to another position without adding components together. If the same scalar function $\sigma$ is applied to every unit, calculating after reordering gives the same result as reordering after calculation. This transformation also permutes hidden biases, while retaining the output bias as $\mathbf b_2'=\mathbf b_2$.

Examine separately a counterexample where general mixing fails and a permutation that is actually allowed.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An invertible shear sends one minus two through ReLU to zero while ReLU first then shear gives one zero](../../figures/assets/M03/M03-15-relu-mixing-failure.svg)

<figcaption>P=[[1,1],[0,1]] is invertible, but ReLU(Pz) and P ReLU(z) differ. This one counterexample is enough to refute the claim that every invertible matrix commutes with ReLU.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Original hidden values one six with readout weights three four become six one with weights four three preserving output twenty seven](../../figures/assets/M03/M03-15-permutation-readout.svg)

<figcaption>Reordering the two units in Example 1 together with their readout weights preserves 27. Reordering the activations preserves the sum of squares 1²+6², but values at the same unit index may differ.</figcaption>

</figure>

## Core concept 5. ReLU has positive scaling symmetries

ReLU is positively homogeneous for positive $c$:

\[
\operatorname{ReLU}(cz)=c\operatorname{ReLU}(z),
\qquad c>0.
\]

For $c>0$, the sign of $z$ remains unchanged. Both sides are $cz$ for positive inputs and 0 for inputs at or below 0, giving the equality. The ReLU equality also holds for $c=0$, but this factor is not reversible and is therefore not used as an invertible scaling symmetry.

For a positive diagonal matrix $\mathbf D$,

\[
\operatorname{ReLU}(\mathbf D\mathbf z)
=\mathbf D\operatorname{ReLU}(\mathbf z).
\]

In a ReLU hidden layer,

\[
\mathbf W_1'=\mathbf D\mathbf W_1,\quad
\mathbf b_1'=\mathbf D\mathbf b_1,\quad
\mathbf W_2'=\mathbf W_2\mathbf D^{-1}
\]

therefore preserves the function. Negative diagonal entries of $\mathbf D$ generally invalidate this equality. Sigmoid and tanh do not share this same positive scaling symmetry.

The diagonal entry $d_i>0$ scales the $i$th row of $\mathbf W_1$ and $b_{1,i}$ by $d_i$, scaling that unit's preactivation and ReLU output by the same factor. Multiplication by $\mathbf W_2\mathbf D^{-1}$ scales the $i$th column reading that unit by $1/d_i$. The incoming factor and outgoing reciprocal cancel, preserving output at every input while potentially changing hidden activations and weight magnitudes.

Separating Example 2's scaling into activation and output graphs clarifies what changes and what is preserved.

<figure class="lesson-figure" markdown="1">

![Original and fourfold scaled hidden ReLU activation curves differ by a factor of four on the same input domain](../../figures/assets/M03/M03-15-scaled-hidden-activation.svg)

<figcaption>Multiplying the incoming weight and bias by 4 multiplies hidden values in the active region by 4 as well. Equal model functions do not justify expecting equal hidden activation magnitudes.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Original and compensated scaled ReLU output functions lie exactly on the same curve for all inputs](../../figures/assets/M03/M03-15-same-output-function.svg)

<figcaption>Reducing the outgoing weight from 3 to 3/4 cancels the hidden scaling factor 4. The curves do not merely meet at a few samples: the equation makes them equal at every allowed input.</figcaption>

</figure>

## Core concept 6. Symmetry affects identifiability and loss geometry

If different parameter settings represent the same function, observing the function alone cannot uniquely select one setting. The parameters are then nonidentifiable. Comparing neuron indices or weight coordinates directly across two models may mistake differences in permutation or scaling for functional differences.

If a continuous symmetry path $\boldsymbol\theta(t)$ preserves the function, the data loss is constant along that path. The first-order change in the symmetry tangent direction is therefore 0. At a stationary point, with suitable differentiability conditions, such directions may appear as zero-curvature directions of the Hessian. Numerical Hessians may not have exact 0 values because of regularization, finite precision, nondifferentiable points, or approximate symmetries.

To check this with derivatives, suppose the fixed data loss $L$ and the symmetry path are twice continuously differentiable. Since $\ell(t)=L(\boldsymbol\theta(t))$ is constant,

\[
0=\ell'(t)=\nabla L(\boldsymbol\theta(t))^\top\boldsymbol\theta'(t)
\]

Differentiating once more gives

\[
0=\ell''(t)
=\boldsymbol\theta'(t)^\top\mathbf H_L(\boldsymbol\theta(t))\boldsymbol\theta'(t)
+\nabla L(\boldsymbol\theta(t))^\top\boldsymbol\theta''(t)
\]

The second-order change along a curved path includes both the Hessian term and a term from curvature of the path itself. At a stationary point, the gradient is 0, removing the second term. A nonzero symmetry tangent then has quadratic curvature 0 along its direction. Constant loss along a path alone does not imply straight-line tangent curvature of 0 at a point whose gradient is not 0.

Replacing the same symmetry curve with its straight tangent may change the preservation conditions.

<figure class="lesson-figure" markdown="1">

![Exact exponential ReLU scaling parameter curve keeps loss at four point five while the straight tangent line through the same parameters changes the loss](../../figures/assets/M03/M03-15-symmetry-curve-versus-tangent.svg)

<figcaption>Using Example 2's parameters, the loss is L=½f(0)² for input 0 and target 0. The green curve θ(t)=(2eᵗ,eᵗ,3e⁻ᵗ) preserves function and loss. Orange path θ(0)+t(2,1,-3) shares the first-order tangent but is not exact scaling. Since the gradient here is not 0, the straight direction's second-order curvature need not be 0 either.</figcaption>

</figure>

## Core concept 7. Interpretation claims must specify what symmetry preserves

Exact symmetries preserve the input–output function, predictions, and data loss. A particular hidden neuron's index, weight magnitude, or coordinatewise activation may nevertheless change under permutations or scalings. Interpretation methods depending on these quantities are difficult to compare directly across models without symmetry alignment or normalization.

This does not mean hidden representations are meaningless. It means choosing whether the interpretation unit is an individual coordinate or a more stable object such as a subspace, span, pairwise relationship, or functional effect. Whatever object is chosen, the allowed transformation class must be stated first.

For example, a hidden vector's Euclidean norm is preserved under permutations because only the order of squared terms changes. Positive diagonal scaling changes component magnitudes differently and generally does not preserve that norm. Rather than assuming an observable preserved under one transformation class is preserved under another, substitute the actual transformation into the quantity being compared.

## Example 1. Changing a linear hidden basis preserves the output

\[
\mathbf W_1=
\begin{bmatrix}
1&0\\
0&2
\end{bmatrix},
\qquad
\mathbf W_2=
\begin{bmatrix}
3&4
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}
1\\3
\end{bmatrix}.
\]

The original hidden vector and output are

\[
\mathbf h=
\begin{bmatrix}
1\\6
\end{bmatrix},
\qquad y=3+24=27
\]

Choose the permutation exchanging the two hidden coordinates as

\[
\mathbf P=
\begin{bmatrix}
0&1\\
1&0
\end{bmatrix}
\]

Then $\mathbf P^{-1}=\mathbf P$, and

\[
\mathbf W_1'=
\begin{bmatrix}
0&2\\
1&0
\end{bmatrix},
\qquad
\mathbf W_2'=
\begin{bmatrix}
4&3
\end{bmatrix}.
\]

The new hidden vector is $\mathbf h'=(6,1)^\top$, but the output is

\[
y'=4\cdot6+3\cdot1=27
\]

The first hidden coordinate changes while the function output does not.

## Example 2. Scaling symmetry of one ReLU unit

In

\[
f(x)=w_2\operatorname{ReLU}(w_1x+b_1)
\]

let $(w_1,b_1,w_2)=(2,1,3)$. Using $c=4$ to change the parameters to

\[
(w_1',b_1',w_2')=(8,4,3/4)
\]

gives

\[
\frac34\operatorname{ReLU}(8x+4)
=\frac34\cdot4\operatorname{ReLU}(2x+1)
=3\operatorname{ReLU}(2x+1)
\]

Parameters and hidden activation scale change, but the function is the same for every input.

## Example 3. Gradient changes under reparameterization

Let $L(\theta)=\theta^2$ and $\theta=r(\phi)=2\phi$. At $\phi=1$, we have $\theta=2$ and

\[
\frac{dL}{d\theta}=2\theta=4,
\qquad
\frac{d\theta}{d\phi}=2.
\]

Thus,

\[
\frac{d\widetilde L}{d\phi}
=\frac{d\theta}{d\phi}\frac{dL}{d\theta}
=8.
\]

The same loss value is represented, but gradient components change with coordinate scale. This example shows why gradient magnitudes should not be compared directly across parameterizations.

The same loss point in Example 3 has different tangent slopes in the two coordinate systems.

<figure class="lesson-figure" markdown="1">

![Original loss theta squared has value four and tangent gradient four at theta two](../../figures/assets/M03/M03-15-old-coordinate-gradient.svg)

<figcaption>At original coordinate θ=2, the loss is 4, and the orange tangent has slope 4. The gradient measures the rate of change per unit of this coordinate.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Reparameterized loss four phi squared has the same value four and tangent gradient eight at phi one](../../figures/assets/M03/M03-15-new-coordinate-gradient.svg)

<figcaption>The corresponding new coordinate φ=1 represents the same loss 4 but has slope 8. One unit in the new coordinate is two units in the original coordinate, introducing factor 2 into the gradient.</figcaption>

</figure>

## Common misconceptions

### Misconception 1. Different parameters necessarily imply different model functions

Exact symmetries, including permutations and ReLU positive scalings, allow different parameters to produce the same outputs for every input.

### Misconception 2. Any linear-layer change of basis applies to every neural network hidden layer

Elementwise nonlinear functions do not commute with general invertible matrices. Only transformations allowed by the architecture and activation are symmetries.

### Misconception 3. Two parameter settings with equal loss represent the same function

Equal loss on finite data means equality of a scalar value computed on observed samples. This is weaker than exact functional equivalence, which requires equality for every input.

### Misconception 4. Symmetry makes hidden representations uninterpretable

Symmetry does not directly imply that interpretation is impossible. It requires specifying under which transformations the interpretation is invariant or which alignment is needed before comparison.

### Misconception 5. All small Hessian eigenvalues arise from model symmetries

Exact continuous symmetries can create flat directions, but small curvature can also arise from insufficient data, saturation, scale, approximate symmetries, and numerical errors. One eigenvalue does not determine the cause.

## Exercises

### 1. Reparameterization gradient

Let $L(\theta)=(\theta-1)^2$ and $\theta=3\phi$. Calculate $d\widetilde L/d\phi$ at $\phi=1$.

<details>
<summary>Show solution</summary>

We have $\theta=3$ and $dL/d\theta=2(3-1)=4$. Since $d\theta/d\phi=3$,

\[
\frac{d\widetilde L}{d\phi}=3\cdot4=12
\]

</details>

### 2. Functional equivalence and sample equivalence

Two models give the same predictions on training samples. Is this alone sufficient to conclude $\boldsymbol\theta\sim\boldsymbol\theta'$?

<details>
<summary>Show solution</summary>

Equivalence as defined here requires equal functions at every allowed input. Equal predictions only on training samples are weaker: the models may differ at unobserved inputs.

</details>

### 3. Proving a linear change-of-basis symmetry

For $\mathbf y=\mathbf W_2\mathbf W_1\mathbf x$, use an invertible matrix $\mathbf P$ to define $\mathbf W_1'=\mathbf P\mathbf W_1$ and $\mathbf W_2'=\mathbf W_2\mathbf P^{-1}$. Prove $\mathbf y'=\mathbf y$.

<details>
<summary>Show solution</summary>

\[
\mathbf y'
=\mathbf W_2'\mathbf W_1'\mathbf x
=\mathbf W_2\mathbf P^{-1}\mathbf P\mathbf W_1\mathbf x
=\mathbf W_2\mathbf W_1\mathbf x
=\mathbf y.
\]

Invertibility gives $\mathbf P^{-1}\mathbf P=\mathbf I$.

</details>

### 4. Permutation symmetry

The hidden activation is $(h_1,h_2,h_3)=(2,-1,5)$, and the output weights are $(4,7,-2)$. Exchange the first and third hidden units together with their weights. State the new activation and output weights, and verify preservation of the dot product.

<details>
<summary>Show solution</summary>

The new activation is $(5,-1,2)$, and the new output weights are $(-2,7,4)$. The original dot product is $8-7-10=-9$, and the new one is $-10-7+8=-9$. Changing activations without also changing output weights does not preserve it.

</details>

### 5. Conditions for ReLU scaling

For $c=-2$, give a counterexample showing that $\operatorname{ReLU}(cz)=c\operatorname{ReLU}(z)$ does not hold for every $z$.

<details>
<summary>Show solution</summary>

At $z=1$, the left side is $\operatorname{ReLU}(-2)=0$, and the right side is $-2\operatorname{ReLU}(1)=-2$. ReLU's homogeneous scaling symmetry therefore requires $c>0$.

</details>

### 6. Critiquing an interpretation claim

Comparing weights and activations of neurons with matching indices in two ReLU networks gives different values. Does this establish that the two neurons have different functions?

<details>
<summary>Show solution</summary>

Not directly. Hidden-unit permutations and positive scalings can represent the same function with different neuron indices and scales. First specify the allowed symmetries and check whether differences remain after unit alignment or scale normalization.

</details>

### 7. M03 cumulative assessment

Consider this network:

\[
\mathbf h=\mathbf W\mathbf x+\mathbf b,
\qquad
\mathbf a=\operatorname{ReLU}(\mathbf h),
\qquad
s=\mathbf v^\top\mathbf a,
\qquad
L=\frac12(s-y)^2,
\]

\[
\mathbf x=
\begin{bmatrix}
1\\2
\end{bmatrix},
\quad
\mathbf W=
\begin{bmatrix}
1&-1\\
2&1
\end{bmatrix},
\quad
\mathbf b=
\begin{bmatrix}
0\\0
\end{bmatrix},
\quad
\mathbf v=
\begin{bmatrix}
3\\-2
\end{bmatrix},
\quad y=1.
\]

Do the following:

1. Calculate forward values $\mathbf h,\mathbf a,s,L$.
2. Calculate $\mathbf J_{\mathbf a,\mathbf x}$ and $\mathbf J_{s,\mathbf x}$.
3. Use backpropagation to calculate $\nabla_{\mathbf x}L$, $\nabla_{\mathbf W}L$, $\nabla_{\mathbf b}L$, and $\nabla_{\mathbf v}L$.
4. Calculate $dL$ through the JVP for input direction $\mathbf p=(1,-1)^\top$, and compare it with $\nabla_{\mathbf x}L^\top\mathbf p$.
5. Tabulate the results an automatic differentiation library should return.

<details>
<summary>Show solution</summary>

The forward pass gives

\[
\mathbf h=
\begin{bmatrix}
-1\\4
\end{bmatrix},
\qquad
\mathbf a=
\begin{bmatrix}
0\\4
\end{bmatrix},
\qquad
s=-8,
\qquad
L=\frac12(-9)^2=40.5
\]

The ReLU derivative matrix at this point is

\[
\mathbf D=
\begin{bmatrix}
0&0\\
0&1
\end{bmatrix}
\]

so

\[
\mathbf J_{\mathbf a,\mathbf x}
=\mathbf D\mathbf W
=
\begin{bmatrix}
0&0\\
2&1
\end{bmatrix},
\]

\[
\mathbf J_{s,\mathbf x}
=\mathbf v^\top\mathbf D\mathbf W
=
\begin{bmatrix}
-4&-2
\end{bmatrix}.
\]

With $r=s-y=-9$, we have $\partial L/\partial s=r$. The cotangent reaching the hidden preactivation is

\[
\bar{\mathbf h}=r\mathbf D\mathbf v
=
\begin{bmatrix}
0\\18
\end{bmatrix}.
\]

Thus,

\[
\nabla_{\mathbf x}L
=\mathbf W^\top\bar{\mathbf h}
=
\begin{bmatrix}
36\\18
\end{bmatrix},
\]

\[
\nabla_{\mathbf W}L
=\bar{\mathbf h}\mathbf x^\top
=
\begin{bmatrix}
0&0\\
18&36
\end{bmatrix},
\qquad
\nabla_{\mathbf b}L=
\begin{bmatrix}
0\\18
\end{bmatrix},
\]

\[
\nabla_{\mathbf v}L
=r\mathbf a
=
\begin{bmatrix}
0\\-36
\end{bmatrix}.
\]

Propagating direction $\mathbf p=(1,-1)^\top$ forward gives

\[
d\mathbf h=\mathbf W\mathbf p
=
\begin{bmatrix}
2\\1
\end{bmatrix},
\qquad
d\mathbf a=\mathbf D\,d\mathbf h
=
\begin{bmatrix}
0\\1
\end{bmatrix},
\]

\[
ds=\mathbf v^\top d\mathbf a=-2,
\qquad
dL=r\,ds=18.
\]

The reverse-mode gradient also gives

\[
\nabla_{\mathbf x}L^\top\mathbf p=36-18=18
\]

The automatic differentiation results should be:

| Target | Expected gradient or JVP |
|---|---|
| $\mathbf x$ | $(36,18)^\top$ |
| $\mathbf W$ | $\begin{bmatrix}0&0\\18&36\end{bmatrix}$ |
| $\mathbf b$ | $(0,18)^\top$ |
| $\mathbf v$ | $(0,-36)^\top$ |
| $dL$ along direction $\mathbf p$ | $18$ |

This exercise checks that computation graphs, Jacobians, JVPs, VJPs, and backpropagation are different expressions of the same chain rule.

</details>

## Lesson summary

- Reparameterization expresses the same model family with different parameters; gradients transform through the reparameterization map's VJP.
- Model symmetries change parameters while preserving the model function at every input.
- Linear hidden layers permit any invertible change of basis paired with its inverse across the two layers.
- Arbitrary changes of basis are generally not allowed in elementwise nonlinear layers.
- Hidden-unit permutations and ReLU positive scalings are representative exact symmetries.
- Symmetry affects parameter identifiability, flat directions of the loss, and model comparisons.
- Hidden representation interpretations must specify the allowed transformations and the objects they preserve.

## Pass criteria

You pass if you can answer the following without referring to the material:

- Can you distinguish reparameterization from model symmetry?
- Can you calculate gradients under reparameterization using VJPs?
- Can you distinguish functional equivalence from equal outputs on finite samples?
- Can you prove a linear hidden change-of-basis symmetry using equations?
- Can you calculate permutation and ReLU positive scaling symmetries?
- Can you explain why an arbitrary invertible matrix is not a symmetry of a nonlinear layer?
- Can you explain the limitations symmetry places on neuron comparisons and Hessian interpretation?

## M03 stage pass criteria

After completing M03, you should be able to connect and explain the following:

- Choose bases to represent abstract vectors and linear maps by coordinates and matrices.
- Distinguish components that change under coordinate transformations from geometric and algebraic objects that are preserved.
- Calculate with subspaces, quotients, duals, bilinear forms, and tensors according to their types.
- Express local first- and second-order structure using total derivatives, Jacobians, and Hessians.
- Connect JVPs, VJPs, and backpropagation through one chain rule.
- Limit the units of interpretation claims by considering equivalence and symmetries of model parameters.
- Calculate the cumulative assessment in M03-15 by hand and compare it with automatic differentiation results.

## Next lesson

- [M04-01 Events and probability](../M04/M04-01-events-probability.md)

## Author checklist

- [x] Learning objectives are expressed as observable actions.
- [x] Reparameterization is distinguished from symmetry transformations.
- [x] Gradient transformations are connected to VJPs.
- [x] Linear hidden changes of basis are proved.
- [x] Permutation and ReLU scaling symmetries are calculated.
- [x] Limitations involving identifiability and loss geometry are stated.
- [x] The M03 cumulative assessment is included.
- [x] Every exercise has a solution.
- [x] The strengths of model interpretation claims are distinguished.
- [x] The glossary and notation rules are followed.
- [x] Internal links and math delimiters have been checked.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
