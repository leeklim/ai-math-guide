---
id: "A09-SYM-04"
title: "Permutation symmetry"
part: 4
stage: "A09-SYM"
status: "complete"
prerequisites: ["A09-SYM-02", "M03-15"]
estimated_time: "90–120 minutes"
---

# A09-SYM-04. Permutation symmetry

## Why this lesson matters

The order of hidden units and attention heads may serve only as labels. Ignoring compensated permutations can make two models performing the same computation look entirely different coordinate by coordinate, causing neuron matching and parameter averaging to fail.

## Learning objectives

- Write the permutation compensation formula for a two-layer network.
- Track permutations of activations and weights.
- Explain the conditions under which a head permutation is allowed.
- Distinguish matching scores from functional equivalence.

## Prerequisite check

- Prerequisite lessons: [A09-SYM-02 Orbits and stabilizers](A09-SYM-02-orbits-stabilizers.md), [M03-15 Model symmetries](../../part-1-foundations/M03/M03-15-reparameterization-model-symmetries.md)
- Check question: What is preserved when hidden coordinates are changed and the inverse is applied in the next layer?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $P$ | `P` | Permutation matrix | Orthogonal binary matrix |
| $W_1'=PW_1$ | `W sub one prime equals P W sub one` | Reordering hidden rows | Matrix |
| $W_2'=W_2P^{-1}$ | `W sub two prime equals W sub two P inverse` | Compensation in the next layer | Matrix |
| $\pi\in S_m$ | `pi in S sub m` | Permutation of $m$ units | Group element |
| $B$ | `B` | Block permutation of head outputs | Square permutation matrix |

## Core concepts

### Hidden-unit labels and connecting weights

For $f(x)=W_2\phi(W_1x)$, suppose that the same scalar activation is applied to every hidden unit. The rows of $W_1$ contain each hidden unit's input weights, while the columns of $W_2$ contain its weights to the output. Left multiplication by $P$ reorders the rows of $W_1$. Applying the same reordering to the activations and compensating in the output connections gives

$$
W_2P^{-1}\phi(PW_1x)
=W_2P^{-1}P\phi(W_1x)=f(x).
$$

The equation $\phi(Pz)=P\phi(z)$ says that reordering and activation computation can be exchanged when the same function is applied to each component. Then $P^{-1}P=I$ cancels the hidden reordering at the output. A permutation does not turn activations into new values; it changes the labels of the values and their connecting weights together.

Compare the pairing of hidden rows and subsequent readout columns in the original and reordered arrangements below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Original and swapped hidden rows stay paired with their corresponding readout columns, preserving output 41.](../../figures/assets/A09-SYM/A09-SYM-04-hidden-row-column-pair.svg)

<figcaption>When rows of W₁ are swapped, the hidden values and corresponding columns of W₂ move together. Applying the same scalar activation to every unit and following the same order for biases preserves the original output 41.</figcaption>

</figure>

### Activations and biases must follow the same order

With biases in $h=\phi(W_1x+b_1)$ and $y=W_2h+b_2$, set $W_1'=PW_1$, $b_1'=Pb_1$, $W_2'=W_2P^{-1}$, and $b_2'=b_2$. The new preactivation is $P(W_1x+b_1)$, and the new hidden activation is $h'=Ph$. The output bias is unchanged because it is not a hidden coordinate. Leaving the hidden bias in its original order connects row weights and biases to different units.

With several hidden layers, each intermediate weight matrix must compensate for the preceding layer's reordering on its input side and apply its own layer's reordering on its output side. The matrices cannot be reordered independently. With residual branches or shared parameters, connections using the same hidden coordinates must have their order matched together.

Check separately whether biases and residual connections use the same hidden coordinates.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Swapping preactivation rows and bias together yields 5,2; leaving bias in the original order yields 3,4 and changes the output.](../../figures/assets/A09-SYM/A09-SYM-04-bias-coordinate-pair.svg)

<figcaption>Swapping W₁x=(1,2)ᵀ and b₁=(1,3)ᵀ together gives hidden values (5,2)ᵀ. Leaving the bias in place gives (3,4)ᵀ and produces 33 rather than 41, even with the same compensated readout (7,3). The output bias b₂ is unchanged.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Swapping both residual branches preserves the permuted sum, while swapping only one branch produces a different vector.](../../figures/assets/A09-SYM/A09-SYM-04-residual-shared-order.svg)

<figcaption>Swapping the original sum (3,9)ᵀ gives (9,3)ᵀ. Both branches must be swapped to obtain this result; swapping only one gives (6,6)ᵀ. Connections sharing coordinates cannot be reordered independently.</figcaption>

</figure>

### Attention heads move as entire blocks

Stack equal-sized head outputs into a column vector $c$ and write the output as $W_Oc$. Applying a block permutation $B$ that changes only the head order gives $c'=Bc$. Setting $W_O'=W_OB^{-1}$ then gives $W_O'c'=W_Oc$. In a row-vector implementation that reorders the concatenated matrix by right multiplication, the multiplication directions change accordingly.

To reorder head outputs in the actual computation, move that head's query, key, and value parameters as one group. In the output projection, compensate for the entire block corresponding to its output. Reordering components within one head and reordering multiple heads are different actions. This lesson compares the latter.

Head-specific masks, routing, or parameter tying can reduce the allowed symmetry. Check whether masks and other settings belong to the head and can move with it, or are architectural constraints fixed to particular positions. Only permutations preserving these constraints allow the calculation above to establish function preservation for the entire model. Reordering attention heads must also be distinguished from reordering tokens.

Distinguishing head-block movement from token-row movement makes the connections requiring compensation identifiable.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Swapping two two-coordinate attention-head blocks and their entire readout blocks preserves scalar output 19.](../../figures/assets/A09-SYM/A09-SYM-04-head-output-blocks.svg)

<figcaption>Head outputs move by blocks, not individual components. The output of c=[1,2|3,4] and Wₒ=[2,1|1,3] is 19; swapping both blocks and their corresponding output-weight blocks preserves 19. The actual heads' Q, K, and V must move together, and architectural constraints must be preserved.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A token-by-head grid shows a head-block column swap separately from a token-row swap, with fixed head constraints stated beside it.](../../figures/assets/A09-SYM/A09-SYM-04-head-token-axes.svg)

<figcaption>Changing head order moves block columns within each token row; changing token order moves rows. If head-specific masks or routing are fixed to positions, only swaps preserving those constraints are allowed.</figcaption>

</figure>

### Matching selects candidate correspondences

Matching can be formulated as an assignment problem that maximizes correlation or minimizes weight distance. A high matching score is not sufficient for functional equivalence.

After defining similarity between neurons $i,j$ in two models, match each neuron to one distinct neuron in the other model. Using correlation as similarity maximizes the sum; using distance as cost minimizes the sum. Selecting each row and column exactly once implements the one-to-one constraint of a permutation. Independently choosing each neuron's highest-scoring counterpart can select the same target multiple times and fail to produce a permutation.

Applying the selected $P$ consistently to one model can preserve that model's own function. But good activation agreement with the other model does not prove that the two functions are identical. Correlation on limited data can miss biases, scales, or differences on unobserved inputs. Parameter averaging after alignment is a separate model computation, so function and performance preservation must be checked again.

The one-to-one constraint in matching and guarantees about functional equivalence or an averaged model are different questions.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Both rows prefer target B1 individually, but the optimal one-to-one assignment chooses the off-diagonal with total 1.75.](../../figures/assets/A09-SYM/A09-SYM-04-assignment-bijection.svg)

<figcaption>Choosing only the maximum in each row matches both neurons to B1, so it is not a permutation. Under the one-to-one constraint, the off-diagonal correspondence has sum 1.75, exceeding the diagonal sum 1.60. This score does not prove functional equivalence.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Two scalar activations hA=x and hB=x+5 have correlation one but distinct identity-readout outputs.](../../figures/assets/A09-SYM/A09-SYM-04-correlation-not-output.svg)

<figcaption>For data in which x varies, hA=x and hB=x+5 have correlation 1, but their identity-readout outputs always differ by 5. This mathematical example distinguishes activation similarity on limited data from equality of functions.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Permutation-equivalent two-unit ReLU models share the same V-shaped function, but their unaligned parameter average produces zero.](../../figures/assets/A09-SYM/A09-SYM-04-unaligned-weight-average.svg)

<figcaption>Swapping the hidden units of fA=ReLU(x)+2ReLU(−x) gives fB with the same function. Averaging the unmatched input weights (1,−1) and (−1,1) makes both 0, so the averaged model outputs 0. Averaging after alignment preserves the original function in this example, but does not guarantee performance for arbitrary model merging.</figcaption>

</figure>

## Small example

Swap hidden activation $h=(2,5)$ to $(5,2)$ and the following weight $(3,7)$ to $(7,3)$. Both dot products are $41$.

The original calculation is $3\times2+7\times5=41$, and the compensated calculation is $7\times5+3\times2=41$. Swapping only the activation gives $3\times5+7\times2=29$. Output preservation depends on maintaining the correspondence between values and output weights, not on reordering alone.

## Common misconceptions

- Matching neuron indices across seeds does not imply the same feature.
- Not every permutation is a symmetry; architectural connectivity must be preserved.

## Exercises

### 1. Compensation calculation
Apply the swap permutation simultaneously to $h=(1,4)$ and $w=(2,3)$, and show that the dot product is preserved.
<details><summary>Show solution</summary>

The original value is $14$, and the permuted value is $(3,2)\cdot(4,1)=14$.
</details>

### 2. Bias
In $h=\phi(Wx+b)$, how does $b$ change when units are permuted?
<details><summary>Show solution</summary>

It is permuted as $b'=Pb$ to follow the same unit order.
</details>

### 3. Assignment
Why use one-to-one matching for the neuron correlation matrix of two seeds?
<details><summary>Show solution</summary>

It prevents several neurons from being matched to the same target and maintains the bijection constraint of a permutation.
</details>

### 4. Averaged model
Why can averaging the weights of two networks without permutation alignment reduce performance?
<details><summary>Show solution</summary>

Component-wise mixing of coordinates with different hidden-unit roles can destroy the symmetry-equivalent structures of the two functions.
</details>

## Evidence and update boundaries

Hidden-unit permutation symmetry follows directly from feed-forward network reparameterization. Symmetry must be checked case by case for architecture-specific routing and normalization.

- [Ainsworth et al., Git Re-Basin, §§2–3](https://arxiv.org/pdf/2209.04836): A research example distinguishing function-preserving permutations from data- or weight-based matching. It is not used as a theorem generally guaranteeing model equivalence or merging performance after matching.
- [Vaswani et al., Attention Is All You Need, §3.2.2](https://arxiv.org/pdf/1706.03762): Provides the head-concatenation and output-projection formulas. The block compensation in the text was derived directly from that computation.

## Lesson summary

- A hidden permutation can preserve the function when paired with an inverse permutation in the next layer.
- Biases and output projections are changed to match.
- Matching is a constrained assignment problem.
- Distinguish matching indices or correlations from functional equivalence.

## Pass criteria

- Can you expand the two-layer permutation compensation formula?
- Can you state the architectural conditions for a head permutation?

## Next lesson

- [A09-SYM-05 Scaling, rotation, and gauge freedom](A09-SYM-05-scaling-rotation-gauge.md)

## Author checklist

- [x] Permutation compensation and architectural conditions are explained.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
