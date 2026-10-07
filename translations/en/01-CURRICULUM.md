# Full curriculum

## How to read this curriculum

- Study `Required` lessons in the order shown.
- Choose `Optional` lessons according to your research interests.
- Lesson IDs are shared across filenames, progress records, exercises, and labs.
- The arrow `A → B` means that A is a direct prerequisite for B.

## Overall structure

```text
Part 1: Stages 0–4, mathematical foundations
  M00 Reading equations
   ↓
  M01 Change and calculus ─┐
   ↓                      ├→ M03 Abstract linear algebra and matrix calculus
  M02 Vectors and matrices ┘                      ↓
                               M04 Probability, statistics, and information theory
                                                 ↓
Part 2: N05 Neural network and Transformer computations
                                                 ↓
Part 3: I06 Representation analysis → I07 Causal and mechanistic analysis → I08 Learning dynamics
                                                 ↓
Part 4: A09 Optional advanced modules
```

## Part 1. Mathematical foundations for model interpretability

### Stage 0, M00. Reading equations

The goal is to read the structure and role of an equation before calculating with it.

| ID | Lesson | Main outcome |
|---|---|---|
| M00-01 | [Numbers, variables, and constants](part-1-foundations/M00/M00-01-numbers-variables.md) | Distinguish objects with fixed values from those whose values can vary. |
| M00-02 | [Expressions, equalities, and equations](part-1-foundations/M00/M00-02-expressions-equalities-equations.md) | Distinguish an expression from an equality that makes a true-or-false claim. |
| M00-03 | [Functions: inputs and outputs](part-1-foundations/M00/M00-03-functions-input-output.md) | Read $y=f(x)$ as a calculation rule and a correspondence. |
| M00-04 | [Coordinates and graphs](part-1-foundations/M00/M00-04-coordinates-graphs.md) | Read how changes in a function's input appear on its graph. |
| M00-05 | [Exponents and logarithms](part-1-foundations/M00/M00-05-exponents-logarithms.md) | Understand $\exp$, $\log$, and their inverse relationship. |
| M00-06 | [Indices and summation notation](part-1-foundations/M00/M00-06-indices-summation.md) | Read $x_i$, $\sum_i x_i$, and averages. |
| M00-07 | [Sets, conditions, and logic](part-1-foundations/M00/M00-07-sets-conditions-logic.md) | Distinguish elements, subsets, conditions, and necessary and sufficient conditions. |
| M00-08 | [Function composition and inverse functions](part-1-foundations/M00/M00-08-composition-inverse.md) | Read $f\circ g$ and the order of computation. |
| M00-09 | [Shapes of scalars, vectors, and matrices](part-1-foundations/M00/M00-09-scalars-vectors-matrices-shape.md) | Use shape to identify the type of an object and determine which operations are possible. |
| M00-10 | [Practice reading AI equations](part-1-foundations/M00/M00-10-ai-equation-reading.md) | Break down a loss function and read it symbol by symbol. |

Cumulative check equation:

\[
\mathcal L(\theta)
=
\frac{1}{N}\sum_{i=1}^{N}
\ell\bigl(f_\theta(x_i),y_i\bigr)
\]

You pass when you can explain each symbol and the roles of function composition, summation, and averaging.

### Stage 1, M01. Change and calculus

| ID | Lesson | Main outcome |
|---|---|---|
| M01-01 | [Changes and average rates of change](part-1-foundations/M01/M01-01-change-average-rate.md) | Connect $\Delta x$ and $\Delta y$ to slope. |
| M01-02 | [Intuition for limits](part-1-foundations/M01/M01-02-limits-intuition.md) | Explain function values as the input approaches a point. |
| M01-03 | [Derivatives and instantaneous rates of change](part-1-foundations/M01/M01-03-derivative-instantaneous-rate.md) | Read $f'(x)$ and $\frac{df}{dx}$ and calculate small examples. |
| M01-04 | [Derivatives and graphs](part-1-foundations/M01/M01-04-derivative-and-graphs.md) | Connect increasing and decreasing behavior to tangent slopes. |
| M01-05 | [Sum, product, and quotient rules](part-1-foundations/M01/M01-05-sum-product-quotient-rules.md) | Apply the basic differentiation rules. |
| M01-06 | [Composite functions and the chain rule](part-1-foundations/M01/M01-06-composition-chain-rule.md) | Multiply the rates of change of the inner and outer functions. |
| M01-07 | [Derivatives of exponential and logarithmic functions](part-1-foundations/M01/M01-07-exponential-log-derivatives.md) | Prepare the derivatives needed for softmax and log-likelihood. |
| M01-08 | [Integration and accumulation](part-1-foundations/M01/M01-08-integration-accumulation.md) | Interpret an integral as a sum of small quantities. |
| M01-09 | [The fundamental theorem of calculus](part-1-foundations/M01/M01-09-fundamental-theorem-calculus.md) | Explain the relationship between rates of change and accumulation. |
| M01-10 | [Multiple variables and partial derivatives](part-1-foundations/M01/M01-10-multivariable-partial-derivatives.md) | Understand what it means to hold other variables fixed. |
| M01-11 | [Directional derivatives and the gradient](part-1-foundations/M01/M01-11-directional-derivative-gradient.md) | Connect directional rates of change to the gradient. |
| M01-12 | [Taylor approximation](part-1-foundations/M01/M01-12-taylor-approximation.md) | Approximate a nonlinear function near a point. |
| M01-13 | [Numerical differentiation and error](part-1-foundations/M01/M01-13-numerical-differentiation-error.md) | Examine approximation errors and instability in finite differences. |

The cumulative task is to calculate the gradient of a small composite function by hand and represent it as a computation graph.

### Stage 2, M02. Vectors and matrices

| ID | Lesson | Main outcome |
|---|---|---|
| M02-01 | [Vectors and vector operations](part-1-foundations/M02/M02-01-vectors-vector-operations.md) | Understand vector addition and scalar multiplication geometrically. |
| M02-02 | [Linear combinations and span](part-1-foundations/M02/M02-02-linear-combinations-span.md) | Explain the set of directions generated by given vectors. |
| M02-03 | [Inner products, lengths, and angles](part-1-foundations/M02/M02-03-inner-product-length-angle.md) | Connect similarity, orthogonal projection, and orthogonality. |
| M02-04 | [Matrices and matrix multiplication](part-1-foundations/M02/M02-04-matrices-matrix-multiplication.md) | Calculate a matrix product as multiple linear combinations. |
| M02-05 | [Matrices as linear transformations](part-1-foundations/M02/M02-05-matrix-as-linear-transformation.md) | Understand rotations, expansions, contractions, and projections through matrices. |
| M02-06 | [Linear systems and inverses](part-1-foundations/M02/M02-06-linear-systems-inverse.md) | Connect the existence of solutions to inverse transformations. |
| M02-07 | [Linear independence, bases, and dimension](part-1-foundations/M02/M02-07-linear-independence-basis-dimension.md) | Find the independent directions needed for a coordinate representation. |
| M02-08 | [Kernel, image, and rank](part-1-foundations/M02/M02-08-kernel-image-rank.md) | Distinguish directions that vanish from those that remain. |
| M02-09 | [Orthogonal bases and projection](part-1-foundations/M02/M02-09-orthogonal-basis-projection.md) | Calculate the closest representation in a subspace. |
| M02-10 | [A minimal understanding of the determinant](part-1-foundations/M02/M02-10-determinant-minimum.md) | Understand the determinant through volume scaling and invertibility. |
| M02-11 | [Eigenvalues and eigenvectors](part-1-foundations/M02/M02-11-eigenvalues-eigenvectors.md) | Explain axes whose directions are preserved and their amplification factors. |
| M02-12 | [Symmetric matrices and the spectral theorem](part-1-foundations/M02/M02-12-symmetric-matrices-spectral-theorem.md) | Understand the conditions for an orthogonal eigenbasis. |
| M02-13 | [Singular value decomposition](part-1-foundations/M02/M02-13-singular-value-decomposition.md) | Decompose a matrix into input directions, amplification factors, and output directions. |
| M02-14 | [Covariance and PCA](part-1-foundations/M02/M02-14-covariance-pca.md) | Find the principal directions of variation in data. |
| M02-15 | [Norms and condition numbers](part-1-foundations/M02/M02-15-norm-condition-number.md) | Distinguish magnitude, sensitivity, and numerical stability. |

The cumulative task is to decompose a small activation matrix using SVD and explain the meaning of a low-dimensional approximation.

### Stage 3, M03. Abstract linear algebra and matrix calculus

| ID | Lesson | Main outcome |
|---|---|---|
| M03-01 | [Abstract vector spaces](part-1-foundations/M03/M03-01-abstract-vector-spaces.md) | Understand the common structure of vector spaces beyond arrays of numbers. |
| M03-02 | [Linear maps and matrix representations](part-1-foundations/M03/M03-02-linear-maps-matrix-representation.md) | Distinguish a map from its matrix in a particular basis. |
| M03-03 | [Changes of basis and coordinate dependence](part-1-foundations/M03/M03-03-change-of-basis-coordinate-dependence.md) | Identify what remains the same object when coordinates change. |
| M03-04 | [Introduction to invariants and equivariance](part-1-foundations/M03/M03-04-invariants-equivariance.md) | Distinguish quantities that remain unchanged under a transformation from those that transform along with it. |
| M03-05 | [Subspaces, direct sums, and decomposition](part-1-foundations/M03/M03-05-subspaces-direct-sums-decomposition.md) | Divide a representation space into meaningful components. |
| M03-06 | [Equivalence relations and quotient spaces](part-1-foundations/M03/M03-06-equivalence-relations-quotient-spaces.md) | Treat objects that differ only in representation as one equivalence class. |
| M03-07 | [Dual spaces and covectors](part-1-foundations/M03/M03-07-dual-spaces-covectors.md) | Understand the difference between a differential and a gradient. |
| M03-08 | [Bilinear and quadratic forms](part-1-foundations/M03/M03-08-bilinear-quadratic-forms.md) | Connect inner products, attention scores, and representations of curvature. |
| M03-09 | [Tensors and multilinear maps](part-1-foundations/M03/M03-09-tensors-multilinear-maps.md) | Read operations with multiple axes and multiple inputs. |
| M03-10 | [Total derivative and differential](part-1-foundations/M03/M03-10-total-derivative-differential.md) | Represent the total change in multiple variables through a linear approximation. |
| M03-11 | [Jacobian](part-1-foundations/M03/M03-11-jacobian.md) | Calculate the local linear transformation of a vector-valued function. |
| M03-12 | [Hessian](part-1-foundations/M03/M03-12-hessian.md) | Represent the local curvature of a scalar function. |
| M03-13 | [JVP and VJP](part-1-foundations/M03/M03-13-jvp-vjp.md) | Calculate products without constructing a large Jacobian. |
| M03-14 | [Automatic differentiation and backpropagation](part-1-foundations/M03/M03-14-automatic-differentiation-backpropagation.md) | Understand how a computation graph implements the chain rule. |
| M03-15 | [Introduction to reparameterization and model symmetries](part-1-foundations/M03/M03-15-reparameterization-model-symmetries.md) | Understand that different parameters can represent the same function. |

The cumulative task is to calculate the Jacobian and backpropagation of a small multilayer function by hand and compare them with automatic differentiation results.

### Stage 4, M04. Probability, statistics, and information theory

| ID | Lesson | Main outcome |
|---|---|---|
| M04-01 | [Events and probability](part-1-foundations/M04/M04-01-events-probability.md) | Express the probability of an event numerically. |
| M04-02 | [Conditional probability and Bayes' rule](part-1-foundations/M04/M04-02-conditional-probability-bayes-rule.md) | Calculate how new information changes probabilities. |
| M04-03 | [Random variables and distributions](part-1-foundations/M04/M04-03-random-variables-distributions.md) | Distinguish values from the rules governing how likely they are. |
| M04-04 | [Expectation, variance, and covariance](part-1-foundations/M04/M04-04-expectation-variance-covariance.md) | Explain average behavior, spread, and joint variation. |
| M04-05 | [Common distributions](part-1-foundations/M04/M04-05-common-distributions.md) | Understand Bernoulli, categorical, and Gaussian distributions. |
| M04-06 | [Samples, populations, and sampling distributions](part-1-foundations/M04/M04-06-samples-populations-sampling-distributions.md) | Distinguish observed data from the target of inference. |
| M04-07 | [Estimation, bias, and variance](part-1-foundations/M04/M04-07-estimation-bias-variance.md) | Distinguish the accuracy and stability of estimators. |
| M04-08 | [Regression and classification](part-1-foundations/M04/M04-08-regression-classification.md) | Understand predictive models from a statistical perspective. |
| M04-09 | [Confidence intervals and bootstrap](part-1-foundations/M04/M04-09-confidence-intervals-bootstrap.md) | Express uncertainty in estimates. |
| M04-10 | [Hypothesis testing and multiple comparisons](part-1-foundations/M04/M04-10-hypothesis-testing-multiple-comparisons.md) | Distinguish chance findings from reproducible effects. |
| M04-11 | [Likelihood and maximum likelihood estimation](part-1-foundations/M04/M04-11-likelihood-maximum-likelihood.md) | Understand how model parameters are fitted to data. |
| M04-12 | [Entropy and cross entropy](part-1-foundations/M04/M04-12-entropy-cross-entropy.md) | Connect uncertainty to prediction loss. |
| M04-13 | [KL divergence](part-1-foundations/M04/M04-13-kl-divergence.md) | Read the directional difference between two distributions. |
| M04-14 | [Mutual information](part-1-foundations/M04/M04-14-mutual-information.md) | Explain the information one variable provides about another. |
| M04-15 | [Calibration and scoring rules](part-1-foundations/M04/M04-15-calibration-scoring-rules.md) | Evaluate the reliability of probability predictions. |
| M04-16 | [Correlation and causation](part-1-foundations/M04/M04-16-correlation-causation.md) | Distinguish observation, prediction, and causal claims. |
| M04-17 | [Experimental design and reproducibility](part-1-foundations/M04/M04-17-experimental-design-reproducibility.md) | Design controls, holdouts, seeds, and reporting criteria. |

The cumulative task is to evaluate probe results statistically and state the scope of claims those results support.

## Part 2. Stage 5: Actual neural network and Transformer computations

### Stage 5, N05. Neural network computation

Architecture and source selection follow the [N05 architecture and source baseline](05-N05-ARCHITECTURE-BASELINE.md). The required text covers stable computational structures; modern components are explained through their differences from the reference architecture.

| ID | Lesson | Main outcome |
|---|---|---|
| N05-01 | Tensors and computation graphs | Trace neural network computations through nodes and edges. |
| N05-02 | A single neuron | Calculate a linear combination, bias, and activation. |
| N05-03 | MLP forward pass | Combine multiple neurons into matrix computations. |
| N05-04 | Activation functions and gating | Compare the computations of ReLU, sigmoid, GELU, SiLU, and gated activations. |
| N05-05 | Logits, softmax, and cross entropy | Connect scores, probabilities, and classification loss. |
| N05-06 | Backpropagation | Calculate how the loss gradient travels backward through layers. |
| N05-07 | Gradient descent and mini-batches | Update parameters using batches of data. |
| N05-08 | Momentum, AdamW, and optimizer state | Distinguish update rules, weight decay, and stored state. |
| N05-09 | PyTorch tensors, shapes, and dtypes | Match tensor operations, axes, and numerical representations in code to equations. |
| N05-10 | Autograd, JVP, and VJP | Check automatic differentiation results. |
| N05-11 | Tokens and tokenizers | Understand how a string becomes token IDs. |
| N05-12 | Embedding and unembedding | Calculate the correspondence between token IDs, input representations, and output logits. |
| N05-13 | Positional information and RoPE | Compare how absolute and sinusoidal positional information and rotary transformations enter attention. |
| N05-14 | Query, key, and value | Calculate the three attention projections. |
| N05-15 | Causal scaled dot-product attention | Calculate the causal mask, attention scores, softmax, and weighted sum of values. |
| N05-16 | MHA, MQA, and GQA | Calculate how the numbers of query and key-value heads change shapes and sharing structures. |
| N05-17 | Residual stream | Trace how attention and MLP outputs are added to a shared stream. |
| N05-18 | LayerNorm, RMSNorm, and residual order | Compare normalization equations and pre-norm and post-norm blocks. |
| N05-19 | Dense MLPs, SwiGLU, and expert routing | Calculate token-wise dense and gated transformations and distinguish conditional paths in MoE. |
| N05-20 | Decoder blocks and architecture diff | Connect attention, normalization, residuals, and MLPs, and mark model-specific replacement points. |
| N05-21 | Language model objectives | Understand next-token prediction and teacher forcing. |
| N05-22 | Causal inference and KV cache | Distinguish full-sequence training computations from key-value reuse during generation. |
| N05-23 | Decoding and generation | Distinguish greedy decoding, sampling, temperature, and probability truncation. |
| N05-24 | The observational status of Chain-of-thought | Distinguish generated explanations from internal computations. |
| N05-25 | Hooks and activation collection | Save activations at selected layers and tokens. |
| N05-26 | Gradient collection and preparation for interventions | Use backward hooks and perform input interventions. |
| N05-27 | Checkpoints and model state | Distinguish parameters, buffers, optimizer state, and training time points. |
| N05-28 | Integrated lab: The path of one token | Trace shapes, residual paths, and cache state from an input token to logits. |

## Part 3. Stages 6–8: Model interpretability in practice

### Stage 6, I06. Representation analysis

| ID | Lesson | Main outcome |
|---|---|---|
| I06-01 | Designing questions about behavior and representations | Define the behavior to measure and the internal object to study first. |
| I06-02 | Activation datasets | Collect activations while controlling inputs, layers, tokens, and conditions. |
| I06-03 | Distributions and basic statistics | Examine means, variances, outliers, and differences between conditions. |
| I06-04 | Neuron-level analysis | Distinguish the advantages of interpreting individual coordinates from its basis dependence. |
| I06-05 | PCA and SVD analysis | Analyze the principal subspaces of variation and low-rank approximations. |
| I06-06 | Linear probes | Measure information that can be recovered linearly. |
| I06-07 | Probe controls and selectivity | Control probe capacity and chance recovery. |
| I06-08 | CCA, CKA, and RSA | Compare different representations at multiple levels of invariance. |
| I06-09 | Feature visualization | Find inputs and conditions that strongly activate a feature. |
| I06-10 | Superposition | Understand why features and neurons do not have a one-to-one correspondence. |
| I06-11 | Sparse coding | Approximate activations as combinations of sparse features. |
| I06-12 | Sparse autoencoders | Evaluate training, reconstruction, and sparsity. |
| I06-13 | Feature stability and identifiability | Examine whether features persist when the seed and dictionary change. |
| I06-14 | Writing claims about representations | Write conclusions that distinguish presence, recovery, use, and causation. |
| I06-15 | Integrated lab: A representation report | Study one concept from data collection through statistical validation. |

### Stage 7, I07. Attribution, causality, and mechanistic analysis

| ID | Lesson | Main outcome |
|---|---|---|
| I07-01 | Sensitivity and attribution | Distinguish local changes from explanations. |
| I07-02 | Gradient-based attribution | Calculate saliency and gradient×input. |
| I07-03 | Integrated gradients and baselines | Understand the effects of path and baseline choices. |
| I07-04 | Perturbation-based attribution | Change part of the input and measure the output change. |
| I07-05 | Observation and intervention | Distinguish correlation from interventions on internal nodes. |
| I07-06 | Ablation | Test the necessity of neurons, heads, and components. |
| I07-07 | Activation patching | Restore a corrupt run using activations from a clean run. |
| I07-08 | Causal tracing | Trace causal effects by layer and token. |
| I07-09 | Path patching | Restrict and test computation paths between components. |
| I07-10 | Residual and logit attribution | Decompose the direct logit contributions of residual components. |
| I07-11 | Representing circuits as graphs | Specify nodes, edges, and computation paths. |
| I07-12 | Necessity and sufficiency | Design removal and restoration experiments together. |
| I07-13 | Mediation and counterfactuals | Analyze the roles of intermediate variables and alternative runs. |
| I07-14 | Off-manifold interventions | Examine confusion caused by unrealistic internal states. |
| I07-15 | Controls and statistical validation | Design random interventions, matched controls, and repeated experiments. |
| I07-16 | Evaluating CoT faithfulness | Compare verbalized explanations with behavioral evidence and evidence from internal interventions. |
| I07-17 | Integrated lab: A small circuit | Work from defining behavior through validating a circuit. |

### Stage 8, I08. Learning dynamics

| ID | Lesson | Main outcome |
|---|---|---|
| I08-01 | Designing checkpoint studies | Define saved time points, metrics, and comparison targets. |
| I08-02 | Parameter distance and function distance | Understand that differences in parameters are not the same as differences in behavior. |
| I08-03 | Representation alignment | Align checkpoint representations while accounting for rotations and permutations. |
| I08-04 | SGD as dynamics | Connect discrete updates to gradient flow. |
| I08-05 | Mini-batch noise and optimizer state | Analyze stochastic path dependence. |
| I08-06 | Hessian spectrum | Approximate curvature directions near a point in training. |
| I08-07 | Loss landscapes and mode connectivity | Investigate changes in loss along a path. |
| I08-08 | Influence functions | Approximate the local effect of a single data point on training. |
| I08-09 | Feature emergence | Connect the time at which a feature appears to changes in behavior. |
| I08-10 | Grokking and phase transitions | Evaluate evidence for abrupt metric changes carefully. |
| I08-11 | Seeds and data order | Separate chance effects from reproducibility. |
| I08-12 | Introduction to data attribution | Investigate the relationship between training examples and model behavior. |
| I08-13 | Integrated lab: The life of a feature | Trace the formation and use of one feature across multiple checkpoints. |

## Part 4. Stage 9: Optional advanced study

Stage 9 consists of modules organized by research question rather than a sequential curriculum. Choose the modules you need for questions that arise in Part 3.

### A09-GEO. Differential geometry and representation spaces

Direct prerequisites: M01, M02, M03

| ID | Lesson |
|---|---|
| A09-GEO-01 | Manifolds and local coordinates |
| A09-GEO-02 | Tangent space and cotangent space |
| A09-GEO-03 | Metrics and length |
| A09-GEO-04 | Pullback metrics and the Jacobian |
| A09-GEO-05 | Geodesics and connections |
| A09-GEO-06 | Intrinsic and extrinsic curvature |
| A09-GEO-07 | Pitfalls in activation manifold analysis |
| A09-GEO-08 | Integrated lab: Local representation geometry |

### A09-DYN. Dynamical systems and stochastic processes

Direct prerequisites: M01, M03, M04, I08

| ID | Lesson |
|---|---|
| A09-DYN-01 | Differential equations and flows |
| A09-DYN-02 | Fixed points and linear stability |
| A09-DYN-03 | Phase portraits and bifurcations |
| A09-DYN-04 | Markov processes |
| A09-DYN-05 | Langevin dynamics |
| A09-DYN-06 | Introduction to stochastic differential equations |
| A09-DYN-07 | Continuous-time approximations of SGD |
| A09-DYN-08 | Integrated lab: Analyzing learning trajectories |

### A09-SYM. Group theory, symmetry, and representation alignment

Direct prerequisites: M02, M03, I06, I08

| ID | Lesson |
|---|---|
| A09-SYM-01 | Groups and group actions |
| A09-SYM-02 | Orbits and stabilizers |
| A09-SYM-03 | Invariant and equivariant |
| A09-SYM-04 | Permutation symmetry |
| A09-SYM-05 | Scaling, rotation, and gauge freedom |
| A09-SYM-06 | Introduction to representation theory |
| A09-SYM-07 | Model alignment and equivalence classes |
| A09-SYM-08 | Integrated lab: Representation alignment across seeds |

### A09-LRN. Statistical learning theory

Direct prerequisites: M04, N05, I06

| ID | Lesson |
|---|---|
| A09-LRN-01 | Hypothesis classes and risk |
| A09-LRN-02 | Bias–variance decomposition |
| A09-LRN-03 | Generalization gap |
| A09-LRN-04 | VC dimension |
| A09-LRN-05 | Rademacher complexity |
| A09-LRN-06 | PAC learning |
| A09-LRN-07 | Generalization of probes and interpretations |
| A09-LRN-08 | Integrated lab: Complexity and generalization |

### A09-KER. Kernels, function spaces, and operators

Direct prerequisites: M02, M03, M04, N05

| ID | Lesson |
|---|---|
| A09-KER-01 | Function spaces and operators |
| A09-KER-02 | Positive definite kernels |
| A09-KER-03 | Feature maps and the kernel trick |
| A09-KER-04 | Introduction to RKHS |
| A09-KER-05 | Introduction to spectra and compact operators |
| A09-KER-06 | Neural tangent kernel |
| A09-KER-07 | Comparing parameter space and function space |
| A09-KER-08 | Integrated lab: Learning from a kernel perspective |

### A09-RMT. Random matrices and high-dimensional statistics

Direct prerequisites: M02, M04, I06, I08

| ID | Lesson |
|---|---|
| A09-RMT-01 | Concentration in high-dimensional spaces |
| A09-RMT-02 | Random projections |
| A09-RMT-03 | Sample covariance spectra |
| A09-RMT-04 | Intuition for the Marchenko–Pastur law |
| A09-RMT-05 | Spiked covariance models |
| A09-RMT-06 | Signal and noise eigenvalues |
| A09-RMT-07 | Weight, activation, and Hessian spectra |
| A09-RMT-08 | Integrated lab: Null models for spectra |

### A09-CAU. Advanced causal inference

Direct prerequisites: M04, I07

| ID | Lesson |
|---|---|
| A09-CAU-01 | Structural causal models |
| A09-CAU-02 | The do operation and interventions |
| A09-CAU-03 | Confounding and identifiability |
| A09-CAU-04 | Mediation assumptions |
| A09-CAU-05 | Counterfactuals and potential outcomes |
| A09-CAU-06 | Causal abstraction |
| A09-CAU-07 | External validity of internal interventions |
| A09-CAU-08 | Integrated lab: Circuit-level causal claims |

### Recommended learning paths

#### Experiment-focused path

```text
M00 → M01·M02 → M03·M04 → N05 → I06 → I07
```

#### Research on learning processes

```text
Basic path → I08 → A09-DYN·A09-RMT·A09-SYM
```

#### Research on representation geometry

```text
Basic path → I06 → A09-GEO·A09-SYM·A09-RMT
```

#### Theory-focused research

```text
Basic path → A09-LRN·A09-KER·A09-DYN
```
