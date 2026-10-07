---
id: "N05-26"
title: "Gradient collection and preparation for interventions"
part: 2
stage: "N05"
status: "complete"
prerequisites:
  - "N05-25"
estimated_time: "120–150 minutes"
---

# N05-26. Gradient collection and preparation for interventions

## Why this lesson matters

Stored activations can show what a model represents, but they do not reveal how locally sensitive a particular output is to those activations. Specifying a scalar target and collecting activation gradients makes it possible to calculate a perturbation's first-order effect. Comparison with actual interventions is needed to avoid mistaking a gradient for a causal effect.

## Learning objectives

- Define an analysis question as a scalar target.
- Collect the gradient of a non-leaf activation.
- Calculate a first-order change using the inner product of a gradient and a perturbation.
- Distinguish read-only gradient measurement from an output-changing intervention.
- Explain the locality of gradient evidence and the off-manifold limitations of interventions.

## Prerequisite check

- Prerequisite lesson: [N05-25 Hooks and activation collection](N05-25-hook-activation-collection.md)
- Check question: Can you collect an MLP update's token vector and remove the hook handle?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $s(\mathbf a)$ | `s of a` | Scalar logit or loss target to analyze | Scalar |
| $\nabla_{\mathbf a}s$ | `the gradient of s with respect to a` | Local sensitivity of the target to the activation | Same shape as the activation |
| $\delta\mathbf a$ | `delta a` | Perturbation to apply to the activation | Same shape as the activation |
| $\nabla_{\mathbf a}s^\top\delta\mathbf a$ | `the gradient of s dot delta a` | First-order approximation of the target change | Scalar |
| intervention | `intervention` | Operation replacing a forward activation with specified values | Experimental operation |

## Core concept 1. Start with a scalar target

Always specify what quantity a gradient differentiates. For example, at token $t$, the logit difference between correct answer $y^+$ and alternative $y^-$ can be defined as

\[
s=\ell_{t,y^+}-\ell_{t,y^-}
\]

A single correct-answer logit, cross entropy, and sequence mean loss produce different cotangents, so choose a target suited to the question.

Here, a cotangent gives coordinatewise weights describing how small output changes affect the selected scalar. This logit difference weights the two logits by $+1$ and $-1$, respectively, so its activation gradient is also $\nabla_{\mathbf a}\ell_{t,y^+}-\nabla_{\mathbf a}\ell_{t,y^-}$. Cross entropy uses weights determined by the correct answer and predicted probabilities, while the mean loss over several tokens averages the gradients from each position. This explains why changing the target changes the sensitivity being measured even for the same observed activation.

Use two small linear logits to see how the +1 and −1 weights pass through to the gradient.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two toy linear logits have gradients two one and one two whose positive and negative combination gives target gradient one minus one](../../figures/assets/N05/N05-26-target-gradient-combination.svg)

<figcaption>In this example, the gradients of ℓ₀ and ℓ₁ are (2,1) and (1,2), respectively. Selecting target s=ℓ₀−ℓ₁ subtracts the gradients to give (1,−1). This measurement differs from using ℓ₀ alone as the target.</figcaption>
</figure>

## Core concept 2. Activation gradients

When an intermediate activation $\mathbf a$ is not a leaf tensor, PyTorch does not retain its `.grad` by default. Request `retain_grad()` before backward, or obtain the gradient directly with `torch.autograd.grad`.

Computing an intermediate gradient differs from storing that value in the tensor's `.grad`. Backpropagation computes the necessary derivatives as it passes through an activation, but it does not leave every intermediate gradient available for later reading. The call to `retain_grad()` requests retention of that value on the graph-connected activation. Making this request on a recording copy previously separated using `detach` as in the preceding lesson does not restore the original graph. The lab retains the gradient on the original module output and, after backward finishes, copies only the needed token's values and gradients.

Separate the paths of the original graph-connected activation and the observation copy.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Backward from a toy scalar target retains gradient one minus one on the original non leaf activation while a detached value record has no link to restore the original graph](../../figures/assets/N05/N05-26-gradient-retention-graph.svg)

<figcaption>Backward from the example target s=a₀−a₁ computes gradient (1,−1) at the original a. Requesting retain_grad before backward preserves that value in a.grad. A separate detached record of (1,2) does not provide a path to restore the original graph.</figcaption>
</figure>

For a small perturbation,

\[
s(\mathbf a+\delta\mathbf a)-s(\mathbf a)
\approx
\nabla_{\mathbf a}s^\top\delta\mathbf a
\]

This is a first-order approximation around the baseline activation.

The inner product multiplies each coordinate's change by its partial derivative and sums the results. A large gradient component can still yield a small target change if that coordinate changes very little or if other components cancel its effect. This approximation replaces the curved part of a downstream function differentiable at the baseline point with a tangent plane; it does not justify applying the same gradient unchanged at distant activations.

Plotting the coordinatewise products separately reveals how large components can still sum to a small change.

<figure class="lesson-figure" markdown="1">

![Gradient components three minus two multiplied by perturbation components zero point two zero point three give contributions positive zero point six and negative zero point six which sum to zero](../../figures/assets/N05/N05-26-component-cancellation.svg)

<figcaption>The first-order change in this example is 3×0.2+(−2)×0.3=0. The contributions 0.6 and −0.6 from the two coordinates cancel. Gradient magnitude alone does not establish a large target change for this perturbation.</figcaption>
</figure>

## Core concept 3. Comparing with interventions

Replacing an activation with 0 gives $\delta\mathbf a=-\mathbf a$. The gradient prediction is

\[
\Delta s_{linear}=-\nabla_{\mathbf a}s^\top\mathbf a
\]

Rerunning the actual forward computation measures $\Delta s_{actual}$. The difference between the two includes effects of nonlinearity, perturbation size, and downstream normalization.

In this comparison, $s(\mathbf a)$ denotes downstream computation with the model weights, input, and observation site fixed, treating only the activation entering that site as a variable. An actual intervention replaces that activation and reruns the subsequent computation. Changing only the numbers in a stored activation copy does not pass them to the model's forward computation and is therefore not an intervention. To compare the changes, replace the same coordinates at the same site and measure the same scalar target.

Editing an independent record and replacing a live activation follow different paths.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Editing an independent activation record leaves live downstream computation unchanged while replacing the live activation with zeros changes the input used by the rerun](../../figures/assets/N05/N05-26-record-versus-replacement.svg)

<figcaption>In the upper path, only the independent copy is changed to 0, so the forward computation still uses a=(1,2). In the lower path, the actual activation is replaced with 0 and downstream s(0,0) is recomputed. The change is compared with the same target's baseline s(1,2).</figcaption>
</figure>

The perturbation magnitude of zero ablation is $\|\mathbf a\|$. Although removal is a simple operation, it cannot therefore be assumed to be a small perturbation. Whether the gradient prediction is close to the actual change must be checked for this input and replacement rule; it is not guaranteed by the derivative expression alone.

Even for a one-dimensional downstream function, finite removal to 0 can disagree with the tangent prediction.

<figure class="lesson-figure" markdown="1">

![For the toy downstream target a squared zero ablation from activation one to zero changes the actual target by minus one while its tangent predicts minus two](../../figures/assets/N05/N05-26-finite-zero-ablation.svg)

<figcaption>For the illustrative function s=a², the baseline is (a,s)=(1,1). Replacing a with 0 reduces the actual s to 0, giving Δs=−1. Predicting with the gradient 2 at the same point gives Δs≈2×(−1)=−2. This small function example shows approximation error; its values differ from those in the lab below.</figcaption>
</figure>

## Example

The lab uses the MLP update at token index 2 and target `logit[0] - logit[1]`. Replacing the activation with 0 gives a first-order prediction of approximately $-0.03827$ and an actual target change of approximately $-0.03975$. These values are close but are not forced to be equal.

## Hands-on lab

### Environment and source files

- Environment: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- Checked on: 2026-10-01
- Component classification: PyTorch-specific gradient and intervention API
- Shared implementation: `labs/N05/tiny_decoder.py`
- Example ID: `n05_26_gradient_intervention`
- Code source: `labs/N05/n05_26_gradient_intervention.py`
- Tests: `tests/N05/test_n05_26.py`
- Run command: `.venv\Scripts\python.exe -m labs.N05.n05_26_gradient_intervention`

### Resource budget

The lab runs one forward and backward pass and one intervention forward pass with sequence length 4 on a model with 300 parameters.

### Actual code and execution results

<!-- N05_EXAMPLE: n05_26_gradient_intervention -->

### Checks

The tests check the selected activation gradient's shape and values, the intervention's target change, and the first-order approximation error.

## Controls and preparation for interventions

Zero ablation is simple but can move outside the natural activation distribution. Consider mean replacement, matched random vectors, resampling, and patching as controls. An appropriate baseline depends on the question and the component's scale.

Before an intervention, fix the target module path, token, target, replacement rule, paired input, seed, and metric. Searching many layers and tokens and then reporting only the largest effect creates a multiple-comparisons problem.

## Connection to model interpretability

A gradient that is not 0 is local-sensitivity evidence that a small change at the baseline point can affect the target. It does not mean that the activation is necessary or sufficient for the behavior.

An actual intervention effect is also conditional on the selected replacement and input distribution. Moving from a large change in one example to a general circuit role requires a dataset, controls, and uncertainty estimates.

## Common misconceptions

### Misconception 1. A large gradient means the activation value is large

A gradient is the target's local rate of change, a different quantity from activation magnitude.

### Misconception 2. Gradient dot activation is the exact removal effect

It is a first-order Taylor approximation. Its error can be large for a large perturbation or nonlinear downstream computation.

### Misconception 3. Zero ablation is a neutral intervention

Check whether 0 is a natural baseline. Normalization and the distribution can make it an off-manifold input.

## Exercises

### 1. Selecting a target

Write a scalar target for analyzing a preference between answer tokens A and B.

<details><summary>Show solution</summary>A logit difference such as $s=\ell_A-\ell_B$ can be used. Specify the position as well.</details>

### 2. Gradient shape

Determine the gradient shape for a scalar target with respect to an activation of shape `(4,)`.

<details><summary>Show solution</summary>It is `(4,)`, the same as the activation.</details>

### 3. First-order change

Calculate the predicted change for gradient $(2,-1)$ and perturbation $(0.1,0.3)$.

<details><summary>Show solution</summary>It is $2(0.1)+(-1)(0.3)=-0.1$.</details>

### 4. Zero ablation

Determine $\delta a$ when activation $a=(1,-2)$ is replaced with 0.

<details><summary>Show solution</summary>It is $-a=(-1,2)$.</details>

### 5. Diagnosing a discrepancy

Explain what to investigate if the first-order prediction differs greatly from the actual intervention effect.

<details><summary>Show solution</summary>Check whether the perturbation is too large, whether downstream nonlinearities or normalization have large effects, and whether the target and hook site match.</details>

### 6. Scope of the claim

Zero ablation at one token greatly reduced a logit. Determine whether the component can be called necessary for all inputs.

<details><summary>Show solution</summary>No. The effect is specific to that input and intervention; dataset-level paired experiments and controls are needed.</details>

## Sources and update boundaries

Gradient retention for non-leaf tensors and hook contracts were checked against the [PyTorch Tensor documentation](https://docs.pytorch.org/docs/stable/tensors.html) and the [`nn.Module` documentation](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html). Hook execution and compatibility with compiled graphs are framework-version-specific implementation details.

## Lesson summary

- Specify the scalar target before collecting gradients.
- An activation gradient measures the target's local sensitivity.
- The inner product of a gradient and perturbation approximates the first-order change.
- Compare the approximation with an actual intervention forward pass.
- Record zero ablation's limitations concerning baselines, off-manifold values, and multiple comparisons.

## Pass criteria

- Can you express a question as a scalar target?
- Can you collect the gradient of a non-leaf activation?
- Can you calculate a first-order change?
- Can you distinguish read-only measurement from an intervention?
- Can you propose appropriate controls and limits on claims?

## Next lesson

- [N05-27 Checkpoints and model state](N05-27-checkpoint-model-state.md)

## Author checklist

- [x] Learning objectives are stated as observable actions.
- [x] Scalar targets, gradients, and interventions are connected.
- [x] Every exercise has a solution.
- [x] Model interpretability claims are distinguished by strength of evidence.
- [x] The glossary and notation rules are followed.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] No knowledge beyond the prerequisites is required without explanation.
- [x] Internal links and mathematical rendering have been checked.
- [x] Executable code has not been manually duplicated in Markdown.
- [x] Code sources, test paths, resource budgets, and the check date are recorded.
- [x] Activation-gradient and intervention tests are provided.
