---
id: "A09-LRN-07"
title: "Probes and generalization in interpretation"
part: 4
stage: "A09-LRN"
status: "complete"
prerequisites: ["A09-LRN-03", "A09-LRN-05", "I06-06", "I06-07"]
estimated_time: "90–120 minutes"
---

# A09-LRN-07. Probes and generalization in interpretation

## Why this lesson matters

A probe that works well on held-out rows does not necessarily generalize to new prompt templates, concept paraphrases, model seeds, or layers. Interpretation research involves several population axes and selection procedures, so splits must be designed to match the claim.

## Learning objectives

- Specify a probe's experimental unit and hypothesis class.
- Distinguish row, prompt, template, concept, and model splits.
- Design nested selection and control tasks.
- Distinguish recoverability from the model's functional use.

## Prerequisite check

- Prerequisite lessons: [A09-LRN-03 Generalization gap](A09-LRN-03-generalization-gap.md), [A09-LRN-05 Rademacher complexity](A09-LRN-05-rademacher-complexity.md), [I06-06 Linear probe](../../part-3-interpretability/I06/I06-06-linear-probe.md), [I06-07 Probe controls](../../part-3-interpretability/I06/I06-07-probe-controls-selectivity.md)
- Check question: What leakage arises if token rows from the same prompt are divided between training and testing?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $D_{\mathrm{train}},D_{\mathrm{test}}$ | `D train and D test` | Splits for independent evaluation | datasets |
| $\mathcal H_{\mathrm{probe}}$ | `the probe hypothesis class` | probe predictor family | function class |
| $s$ | `s` | Model seed or split seed | index |
| $\Delta_{\mathrm{sel}}$ | `selection optimism delta` | Optimistic bias caused by selection | scalar |

## Core concepts

### Predictor class and sampling unit

A probe is a separate learner that takes fixed activations as input and predicts labels. Its class $\mathcal H_{\mathrm{probe}}$ is specified by its linear or MLP form and permitted parameter and norm constraints; layer and preprocessing selection also change the final predictor. The relationships a probe can recover are relative to this class. Poor performance by a linear probe does not mean information is absent for every function class.

One activation row is not automatically an independent experimental unit. Tokens from the same prompt, paraphrases of the same source text, and sentences made from the same template may share information. Choose sampling units according to what was independently obtained, and group rows that must stay together across the train/test boundary. Model seeds, probe initialization seeds, and split seeds are also different repetitions; do not merge them under a single name $s$.

Even on the same activations, the form of a readout capable of recovering the label relationship depends on the class.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![Four fixed activation points illustrate crossing same-label segments for linear separation and a nonlinear quadrant readout.](../../figures/assets/A09-LRN/A09-LRN-07-class-relative-readout-geometry.svg)

<figcaption>For these four illustrative activations, the segment joining the two 1-label points crosses the segment joining the two 0-label points at the origin. No affine score can strictly separate the labels, because it would require different decisions at the same segment midpoint. The nonlinear readout 1[x₁x₂&gt;0] recovers all four points. This is a geometric example of class-relative recovery, not the result of training an actual MLP.</figcaption>

</figure>

### How split axes change generalization claims

Separate probe claims along the following axes.

- Row generalization: unseen activation rows from the same prompt population
- Prompt generalization: unseen prompts
- Template and concept generalization: held-out expression formats and semantic categories
- Model generalization: unseen training seeds and architectures

A row split evaluates unobserved rows, but if the same prompt appears on both sides, it does not evaluate a new prompt. A prompt split separates entire prompt groups. However, good recovery on a new prompt from the same template does not guarantee recovery on a new template. Template splits separate expression-format groups, while concept splits separate specified semantic-category groups; they answer different questions. Record which concepts were held out and how lexical overlap was restricted.

Model generalization requires evaluating models with genuinely different training seeds or architectures. Changing only the probe seed on the same model is not a substitute. Also distinguish training a new probe for each model from transferring a probe trained on one model without changing it. The former repeats recoverability evaluation for each model; the latter makes a predictor-transfer claim. Changing split axes changes the evaluation distribution, so do not combine every result into the same iid gap.

Separate row groups, hold-out axes, and refitting versus transfer to a new model to clarify what each evaluation answers.

<figure class="lesson-figure" markdown="1">

![Two split layouts contrast mixing token rows from each prompt with keeping each prompt entirely on one side.](../../figures/assets/A09-LRN/A09-LRN-07-row-versus-prompt-split.svg)

<figcaption>Dividing some token rows from each prompt between training and testing repeats the prompt on both sides. A prompt split keeps all rows of a prompt on the same side. The four prompts and three rows in the diagram are illustrative abbreviations; they do not change the text's 100 prompts and 20 tokens.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Four panels highlight held-out prompt, template, concept, and model groups without implying those axes form one hierarchy.](../../figures/assets/A09-LRN/A09-LRN-07-held-out-group-axes.svg)

<figcaption>Changing the group held out changes the claim. Template and concept are different classification axes, not one automatic hierarchy. A model split needs new model training seeds or architectures; changing only probe initialization seeds is not a substitute.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Separate routes on model two either fit a new probe or reuse the frozen probe from model one.](../../figures/assets/A09-LRN/A09-LRN-07-model-refit-versus-transfer.svg)

<figcaption>Both routes evaluate a new model, but the upper route fits a new probe on that model, while the lower route transfers the existing predictor unchanged. Do not combine repeated recoverability across models and predictor transfer into the same success claim.</figcaption>

</figure>

### Select inside, evaluate outside

Select the layer, regularization, feature preprocessing, and probe class using validation, then use an independent test set. Validation data used to compare candidates are selection data. In nested resampling, split the data excluding the outer test into training and validation again, select candidates only inside that split, and then evaluate on the outer test. Repeat selection in each outer trial to evaluate the performance of the entire pipeline. Choosing a layer using all data before cross-validation does not preserve this independence.

Learned preprocessing such as means, scales, and projections must also be fitted on the training portion before evaluation and applied unchanged to the test portion. Even a fit that uses no labels must be distinguished from pure held-out evaluation if it uses information from the test distribution. Match the specified class, selection procedure, and data-size conditions for random-label controls as well. An MLP's performance gain jointly reflects recoverability by a richer function class and training/selection effects, so check controls and held-out gaps separately.

If prompts are the experimental units, obtain confidence intervals by resampling prompt groups. Design permutations to preserve the groups and label relationships that are exchangeable under the null. Simply replacing rowwise permutation with prompt permutation is not automatically valid. If there are token-level label structures or template groups, first determine what is exchangeable.

Check the selection boundary and the information path through preprocessing separately.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![An outer trial contains development-only fitting and validation selection followed by one locked-test evaluation outside the inner selection box.](../../figures/assets/A09-LRN/A09-LRN-07-nested-selection-boundary.svg)

<figcaption>Repeat candidate selection within training/validation in each outer trial, and do not use the outer test for selection. Preprocessing is included in the training fit. The figure shows a design boundary; it does not generate new resampling or training results.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Train points minus one and one give mean zero while pooling test points nine and eleven shifts the fitted mean to five.](../../figures/assets/A09-LRN/A09-LRN-07-preprocessing-test-information.svg)

<figcaption>The illustrative training inputs (−1,1) have mean 0; pooling the test inputs (9,11) changes the mean to 5. The test distribution changes the fitted transformation even without labels. In pure held-out evaluation, fit the rule on training data and apply it unchanged to testing.</figcaption>

</figure>

### Recovery, generalization, and use

A probe that performs well on an independent test set provides evidence that label-related information is recoverable within the specified class and evaluation population. Use controls to check whether label leakage or simple cues could yield the same performance. This result does not show that downstream computations within the model use the same function as the probe.

A functional-use claim requires output effects of ablation or patching that changes the relevant information, together with appropriate controls. Readout alignment may show a relationship between a direction and output computation, but it is not itself an intervention. An intervention may also change other features or create abnormal states, so limit claims to the scope in which matched-norm controls and intervention selectivity have been checked. Probe generalization and intervention effects complement each other but are not the same measurement.

The probe's separate readout and the model's native computation follow different paths even when they start from the same activation.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![An activation branches to a separate probe readout and the model output path, while an intervention changes the activation before measuring output effects.](../../figures/assets/A09-LRN/A09-LRN-07-readout-versus-functional-use.svg)

<figcaption>Successful recovery along the probe's separate label path does not imply that the model's downstream path uses the same information. Check functional use separately through output effects of selective activation interventions and matched-norm controls. Alignment alone or an intervention creating abnormal states does not remove this limitation.</figcaption>

</figure>

## Small example

Even with 20 tokens per sentence, 100 sentences give closer to 100 independent units for prompt-level generalization, not 2,000.

Assuming the 100 sentences are independent prompts and tokens within a sentence are dependent, a prompt split keeps the sentence's 20 rows on the same side. Prompt bootstrap also draws those 20 rows as a group. Decide whether to average token-level risk or average within each prompt first and then average those risks. With unequal lengths, these averages assign different weights. If prompts sharing a template or source text are also dependent, the 100 prompts cannot all be treated as independent; larger groups are needed.

Choose the prompt-pack resampling unit and the weights used to average loss separately.

<figure class="lesson-figure lesson-figure--tall" markdown="1">

![A schematic prompt bootstrap draws prompt packs two, one, two with replacement and preserves all rows within each pack.](../../figures/assets/A09-LRN/A09-LRN-07-prompt-bootstrap-packs.svg)

<figcaption>The illustrative draw samples prompts P₂, P₁, P₂ with replacement. Drawing a prompt draws its token rows together. The 20 tokens per prompt in the text include the omitted rows within each pack. Dependence through templates or source texts across prompts requires larger groups.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![Two illustrative prompts of lengths three and one yield token-mean risk zero point three and equal-prompt mean risk zero point five.](../../figures/assets/A09-LRN/A09-LRN-07-token-versus-prompt-weights.svg)

<figcaption>The two illustrative prompts have unequal lengths and mean losses 0.1 and 0.9. The token mean weights them by lengths 3 and 1, giving 0.3; the prompt mean weights the prompts equally, giving 0.5. Specify the target average together with the split and interval.</figcaption>

</figure>

## Common misconceptions

- High test accuracy may still rely on label leakage or template cues.
- A nonlinear probe's performance gain does not imply a simple, usable feature in the activations.

## Exercises

### 1. Split
What split is needed to examine paraphrase generalization?
<details><summary>Show solution</summary>

A template/paraphrase split must separate expression variants of the same meaning between training and testing and include a lexical-overlap control.
</details>

### 2. Nested selection
What goes wrong if the validation set used to choose the layer and regularization is reused to report final performance?
<details><summary>Show solution</summary>

The result includes optimistic bias from fitting selection noise. An independent test set or nested resampling is needed.
</details>

### 3. Complexity
What else should be reported when an MLP probe performs better than a linear probe?
<details><summary>Show solution</summary>

Report capacity, regularization, sample size, random-label controls, and held-out gaps together to distinguish memorization from nonlinear recoverability.
</details>

### 4. Evidence of use
What experiment strengthens the claim that the model uses a direction recovered by a probe?
<details><summary>Show solution</summary>

Selectively ablate or patch that direction and measure output effects together with matched-norm controls.
</details>

## Evidence and update boundaries

This lesson applies learning-theory splits and probe controls to model-interpretation claims. It does not establish a fixed ranking of probe architectures.

- [Hewitt and Liang (2019), Designing and Interpreting Probes with Control Tasks](https://aclanthology.org/D19-1275/): Provides the basis for controls distinguishing what a probe learns from information in a representation. Do not extend that control task into a guarantee for every split or evidence of causal use.

## Lesson summary

- Each generalization claim has its own independent unit and split axis.
- Select using validation and perform final evaluation on an independent test set.
- Consider probe capacity together with random-label controls.
- Recoverability and functional use are different kinds of evidence.

## Pass criteria

- Can you choose splits and units that match a probe claim?
- Can you distinguish recovery, generalization, and use claims?

## Next lesson

- [A09-LRN-08 Capstone: complexity and generalization](A09-LRN-08-capstone-complexity-generalization.md)

## Author checklist

- [x] The probe's generalization axes and causal limitations are stated.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
