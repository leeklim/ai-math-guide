---
id: "A09-SYM-05"
title: "Scaling, rotation, and gauge freedom"
part: 4
stage: "A09-SYM"
status: "complete"
prerequisites: ["A09-SYM-02", "M03-03", "M03-15"]
estimated_time: "90–120 minutes"
---

# A09-SYM-05. Scaling, rotation, and gauge freedom

## Why this lesson matters

Parameters and hidden coordinates can have scale or basis freedom that leaves the function unchanged. Ignoring gauge freedom can lead to interpreting norms, angles, Hessians, and feature identities as coordinate-independent facts.

## Learning objectives

- Compute the scaling symmetry of a positive-homogeneous network.
- Write the compensating transformation for a hidden-basis rotation.
- Distinguish gauge-dependent quantities from invariant quantities.
- Explain the benefits and arbitrariness of gauge fixing.

## Prerequisite check

- Prerequisite lessons: [A09-SYM-02 Orbits and stabilizers](A09-SYM-02-orbits-stabilizers.md), [M03-03 Change of basis](../../part-1-foundations/M03/M03-03-change-of-basis-coordinate-dependence.md), [M03-15 Model symmetries](../../part-1-foundations/M03/M03-15-reparameterization-model-symmetries.md)
- Check question: How must the matrix representation change to preserve the linear map itself under a change of basis?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $c>0$ | `c greater than zero` | Positive scale | Scalar |
| $Q^\top Q=I$ | `Q transpose Q equals I` | Orthogonal basis change | Matrix identity |
| $h'=Qh$ | `h prime equals Q h` | Hidden-coordinate rotation | Vector |
| $[\theta]$ | `the equivalence class of theta` | Gauge orbit | Parameter class |
| $H$ | `H` | Parameter Hessian | Square matrix |

## Core concepts

### Scaling: adjacent layers exchange scale factors

ReLU applies $\phi(z)=\max(0,z)$ to each component. For $c>0$, the signs of $cz$ and $z$ agree, so $\phi(cz)=c\phi(z)$. Therefore,

$$
W_2\phi(W_1x)
=\frac1cW_2\phi(cW_1x)
$$

Multiplying $W_1$ by $c$ also multiplies the hidden activation by $c$, and multiplying $W_2$ by $1/c$ cancels this factor at the output. The function stays the same even as one layer's norm grows and the next layer's norm shrinks. A hidden bias must be scaled together with $W_1$ by $c$ so that the entire preactivation changes by the same factor.

The scale must be positive. A negative $c$ can change ReLU's active and inactive components, while $c=0$ cannot be inverted. Nor does this equation apply unchanged to activations such as GELU that lack degree-one positive homogeneity. Even with the same function, a training objective with a weight-norm penalty can change. Distinguish function preservation from preservation of the objective including its regularizer.

Compare the exchange of positive scale factors with the failure under negative scaling separately below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Positive scale four enlarges ReLU activation from two to eight while inverse readout scaling preserves output six.](../../figures/assets/A09-SYM/A09-SYM-05-positive-scale-exchange.svg)

<figcaption>With c=4, preactivation 2 becomes 8, and the ReLU output also grows by a factor of 4. Reducing the next weight from 3 to 0.75 keeps the output at 6. A hidden bias must be scaled by c together with W₁ to scale the entire preactivation by the same factor.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![For c=-1 the curves ReLU(-z) and -ReLU(z) disagree, illustrating why negative scaling does not obey positive homogeneity.](../../figures/assets/A09-SYM/A09-SYM-05-relu-scale-sign.svg)

<figcaption>For c=−1, ReLU(−z) and −ReLU(z) equal 0 on different sides and are not equal. Since c=0 has no inverse scale, it is not an invertible action. This comparison concerns ReLU and does not assume positive homogeneity for GELU.</figcaption>

</figure>

### Rotation: which hidden interfaces allow it?

At a linear hidden interface, the basis can be changed using $h'=Qh$ and $W'=WQ^{-1}$. Nonlinearities, normalization, or sparsity constraints can break arbitrary rotation symmetry.

These formulas express an already computed hidden vector in new coordinates and change the following linear map that reads it. Then $W'h'=WQ^{-1}Qh=Wh$. If $Q$ is orthogonal, $Q^{-1}=Q^\top$, and the scalar output $w^\top h$ corresponds to $w'=Qw$. Both $w$ and $h$ must change together to obtain the same value.

Between two linear layers, the producing matrix can be multiplied by $Q$ and the next matrix compensated by $Q^{-1}$. With a fixed elementwise activation between them, $\phi(Qz)=Q\phi(z)$ is also required. ReLU does not satisfy this identity for general rotations. The ability to express hidden vectors in different mathematical coordinates is different from the ability to implement the same computation within the original architecture by changing parameters alone.

A coordinate rotation preserving the readout differs from a rotation passing through a fixed activation.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Hidden vector and scalar-readout weight rotate together by ninety degrees, preserving their dot product five.](../../figures/assets/A09-SYM/A09-SYM-05-rotated-readout.svg)

<figcaption>Rotating h=(1,2)ᵀ and w=(3,1)ᵀ by 90° with the same orthogonal Q gives h′=(−2,1)ᵀ and w′=(−1,3)ᵀ. Both coordinate representations have dot product 5. This compensation concerns the next scalar linear readout, not rotation symmetry of a fixed nonlinearity.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A quarter-turn and fixed ReLU give different output vectors when applied in opposite orders.](../../figures/assets/A09-SYM/A09-SYM-05-relu-rotation-failure.svg)

<figcaption>Applying a 90° rotation first to z=(1,−1)ᵀ gives ReLU(Qz)=(1,1)ᵀ, while applying ReLU first gives QReLU(z)=(0,1)ᵀ. Compensation for coordinate changes at a linear interface does not justify arbitrary rotation symmetry across a fixed elementwise activation.</figcaption>

</figure>

### Which quantities depend on the gauge?

In this lesson, gauge refers to coordinate freedom representing the same observable function. First specify the allowed action, then check whether a quantity changes under it. Function outputs agree under a function-preserving action. Individual neuron labels or layer weight norms, however, can change under the allowed permutations or scaling transformations.

Dependence also varies with the transformation type. An orthogonal $Q$ preserves hidden Euclidean norms and angles, but a general invertible basis change does not. A scalar such as $w^\top h$ is preserved when the vector and its readout weights are compensated correctly. Comparisons minimized over an orbit also require checking compatibility between the norm and action. Without the distance conditions in [A09-SYM-02](A09-SYM-02-orbits-stabilizers.md), do not conclude that a comparison is gauge-invariant merely because it is orbit-minimized.

When interpreting Hessians, distinguish curved orbits from straight-line directions. Along a smooth parameter path $\theta(t)$, even if $L(\theta(t))$ is constant, differentiating twice gives

$$
0=\dot\theta^\top H\dot\theta
+\nabla L^\top\ddot\theta
$$

Here $H$ is the parameter Hessian of $L$. At a point where the gradient is not 0, the second term, corresponding to the orbit's curvature, can cancel the first. Constant loss along a function-preserving curve therefore does not by itself imply a zero Hessian eigenvalue at an arbitrary point. If a smooth symmetry preserves the entire objective and maps a stationary point to stationary points on the same orbit, differentiating $\nabla L=0$ along the orbit gives $H\dot\theta=0$. Under these conditions, a symmetry tangent is a Hessian null direction. Smooth-Hessian reasoning cannot be applied unchanged at nondifferentiable ReLU points.

Compare output invariance, coordinate geometry, and Hessian conditions separately below.

<figure class="lesson-figure" markdown="1">

![Two parameter points on the hyperbola ab=6 have different distances from the origin and different squared norms.](../../figures/assets/A09-SYM/A09-SYM-05-scale-orbit-norm.svg)

<figcaption>Both (2,3) and (8,0.75) lie on ab=6 and output 6x for every x. Their distances from the origin and squared norms differ, at 13 and 64.5625 respectively, so an objective including a norm penalty is not automatically preserved.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![An invertible diagonal basis change maps a unit circle to an ellipse and changes a right angle between two example vectors.](../../figures/assets/A09-SYM/A09-SYM-05-basis-geometry-change.svg)

<figcaption>The general invertible D=diag(2,0.5) maps the unit circle to an ellipse and changes the 90° angle between (1,1)ᵀ and (1,−1)ᵀ to approximately 28.1°. Orthogonal actions and general basis changes preserve different geometric quantities. Preserving a scalar readout requires separate inverse compensation.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The curve ab=6 preserves a smooth objective, while the tangent line gives objective 6-6s squared; a nonzero Hessian term cancels the curve-acceleration term.](../../figures/assets/A09-SYM/A09-SYM-05-curved-orbit-hessian.svg)

<figcaption>For smooth objective L(a,b)=ab and θ(t)=(2eᵗ,3e⁻ᵗ), L=6 is constant. But along the straight tangent θ₀+s(2,−3) at (2,3), L=6−6s². This example is not a stationary point: θ̇ᵀHθ̇=−12 and ∇Lᵀθ̈=12 cancel, so a constant orbit alone does not imply a Hessian null direction.</figcaption>

</figure>

### Gauge fixing selects a representative for comparison

Gauge fixing selects a representative from an orbit according to a comparison rule. For example, in the linear example below, $a>0$ allows $c=1/a$ to set $a'=1$. Parameters with the same product can be compared at a common scale, but this rule cannot be applied at $a=0$. State the domain of representative selection and any remaining symmetry.

Even after whitening sets covariance to the identity, orthogonal rotations preserve identity covariance. Choosing eigenvectors as an additional criterion can leave rotations within spaces with repeated eigenvalues. Rules fixing coordinates are choices that make comparisons reproducible, not evidence that the feature interpretation of a particular coordinate is unique.

Check the representative-selection rule separately from the freedom remaining afterward.

<figure class="lesson-figure" markdown="1">

![Three positive representatives on ab=6 are mapped to the rule a-prime equals one, selecting point one,six.](../../figures/assets/A09-SYM/A09-SYM-05-gauge-representative.svg)

<figcaption>Choosing the rule c=1/a for a&gt;0 aligns representatives on ab=6 at (a′,b′)=(1,6). This selects a representative for comparison and does not apply at a=0. State both the domain where the rule works and the selection criterion.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![A zero-mean four-point set with covariance I and its forty-five-degree rotation both retain covariance I.](../../figures/assets/A09-SYM/A09-SYM-05-whitening-remaining-rotation.svg)

<figcaption>The points ±√2e₁ and ±√2e₂ have mean 0 and covariance I when computed as 1/4 Σhhᵀ. The four points obtained by rotating them 45° have the same I. Fixing covariance by whitening leaves orthogonal coordinate freedom; when all eigenvalues agree, as here, the eigenbasis is not unique either.</figcaption>

</figure>

## Small example

For $f(x)=abx$, replacing $(a,b)$ with $(ca,b/c)$ preserves the product $ab$. But $a^2+b^2$ generally changes.

With $a=2,b=3,c=4$, the transformed parameters are $(a',b')=(8,0.75)$. For every $x$, both parameter settings output $6x$. The squared norm changes from 13 to 64.5625. Since this changes coordinate magnitudes for the same function, the norm alone does not establish greater function complexity.

## Common misconceptions

- A change in weight norm does not always mean a change in function complexity.
- Orthogonal freedom remains after whitening. If an eigenbasis is also chosen, check rotation freedom within degenerate eigenspaces.

## Exercises

### 1. Scaling
For $a=2,b=3,c=4$, compute $(ca,b/c)$ and the product.
<details><summary>Show solution</summary>

The parameters are $(8,0.75)$, and the product remains 6.
</details>

### 2. Norm dependence
Compare $a^2+b^2$ before and after the transformation above.
<details><summary>Show solution</summary>

It changes substantially from 13 to $64+0.5625$, showing gauge dependence.
</details>

### 3. Rotation
For $h'=Qh$, preserve the scalar output $w^\top h$ by finding $w'$.
<details><summary>Show solution</summary>

With $w'=Qw$, $w'^\top h'=w^\top Q^\top Qh=w^\top h$.
</details>

### 4. Interpreting a Hessian
Why can a Hessian eigenvalue be close to 0 in a parameter gauge direction?
<details><summary>Show solution</summary>

If movement in that direction leaves the function and loss unchanged, local curvature is absent or very small.
</details>

## Evidence and update boundaries

Scaling and basis symmetries are derived directly from positive homogeneity and linear coordinate changes. Gauge is used only in the restricted sense of an observable-preserving reparameterization.

## Lesson summary

- Positive homogeneity allows scale exchange between layers.
- A hidden-basis change requires compensation in the adjacent map.
- Parameter norms and Hessians have gauge-dependent components.
- Gauge fixing is a comparison rule, not a unique truth.

## Pass criteria

- Can you compute scaling and rotation compensation formulas?
- Can you distinguish gauge-dependent claims from invariant claims?

## Next lesson

- [A09-SYM-06 Introduction to representation theory](A09-SYM-06-representation-theory.md)

## Author checklist

- [x] Gauge freedom and observables are distinguished.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
