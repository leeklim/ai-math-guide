---
id: "A09-SYM-06"
title: "Introduction to representation theory"
part: 4
stage: "A09-SYM"
status: "complete"
prerequisites: ["A09-SYM-03", "M03-01", "M03-05"]
estimated_time: "90–120 minutes"
---

# A09-SYM-06. Introduction to representation theory

## Why this lesson matters

When a group action on a vector space is linear, it can be analyzed using matrices. Representation theory decomposes symmetry actions into invariant subspaces and irreducible components to explain which feature channels must transform together.

## Learning objectives

- Write the homomorphism condition for a linear representation.
- Distinguish invariant subspaces from irreducible representations.
- Decompose a simple permutation representation.
- State the checks needed to claim irreducible structure in a learned representation.

## Prerequisite check

- Prerequisite lessons: [A09-SYM-03 Invariance and equivariance](A09-SYM-03-invariant-equivariant.md), [M03-01 Vector spaces](../../part-1-foundations/M03/M03-01-abstract-vector-spaces.md), [M03-05 Subspaces](../../part-1-foundations/M03/M03-05-subspaces-direct-sums-decomposition.md)
- Check question: What does it mean for a family of linear maps to preserve a common subspace?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and range |
|---|---|---|---|
| $\rho:G\to GL(V)$ | `rho from G to G L of V` | Linear representation | Group homomorphism |
| $\rho(g_1g_2)=\rho(g_1)\rho(g_2)$ | `rho of g sub one g sub two equals rho of g sub one rho of g sub two` | Homomorphism condition | Matrix equality |
| $W\le V$ | `W is a subspace of V` | Candidate invariant subspace | Vector subspace |
| $V=\bigoplus_iV_i$ | `V is the direct sum of V sub i` | Component decomposition | Direct sum |
| $u_+,u_-$ | `u sub plus and u sub minus` | Symmetric and antisymmetric basis vectors for the swap | Vectors in $\mathbb R^2$ |

## Core concepts

### A representation specifies a linear action

This lesson considers representations on a finite-dimensional real vector space $V$. The group $GL(V)$ consists of invertible linear maps from $V$ to itself. The representation $\rho$ assigns one such map to each $g\in G$ and satisfies

$$
\rho(e)=I,
\qquad
\rho(g_1g_2)=\rho(g_1)\rho(g_2)
$$

This homomorphism condition preserves group multiplication as composition of linear maps. As a result, $g\cdot v=\rho(g)v$ defines a group action. Choosing a basis writes each map as a matrix, but the representation itself is not confined to particular matrix coordinates.

Different group elements can act by the same linear map. For example, mapping every $g$ to the identity also satisfies these equations. Distinguishing group elements and satisfying the homomorphism condition are separate requirements. A machine-learning hidden representation is an activation produced from input, whereas $\rho$ here specifies the rule by which such activations transform. Distinguish the object types despite their shared terminology.

Distinguish the mapping of group composition rules to linear maps from an activation vector below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The two-element swap group maps s squared to P squared equals identity, and sequential action returns vector three,one.](../../figures/assets/A09-SYM/A09-SYM-06-homomorphism-composition.svg)

<figcaption>For G={e,s} with s²=e, assigning ρ(s)=P gives P²=I=ρ(e). Applying P twice to (3,1)ᵀ and applying ρ(s·s) once return to the same point. The homomorphism condition preserves such composition rules for every pair of group elements.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Distinct group elements e and s both map to identity in a valid but nonfaithful linear representation.](../../figures/assets/A09-SYM/A09-SYM-06-nonfaithful-trivial-action.svg)

<figcaption>For the same G={e,s}, setting ρ(e)=ρ(s)=I still satisfies the identity and composition conditions. Faithfulness, requiring different group elements to act by different maps, is separate from the homomorphism condition. The map ρ(g) is a transformation rule; hidden activation h(x) is a vector on which that rule acts.</figcaption>

</figure>

### Invariant subspaces and irreducibility

A subspace $W\le V$ is invariant if, for every $g$, $\rho(g)W\subseteq W$. This requires every vector in $W$ to remain in $W$ after transformation, not that an individual vector remain fixed. Since inverse actions also exist, this condition gives $\rho(g)W=W$.

A representation with $V\ne\{0\}$ and no nonzero proper invariant subspace is irreducible. Proper means $W\ne V$. Since $\{0\}$ and $V$ itself are invariant in every representation, they must be excluded to distinguish decomposability. Finding an eigenvector of just one map in the family is insufficient. The same subspace must be preserved under every allowed group element.

Preservation of a span, fixation of an individual vector, and a condition shared by all actions are different requirements.

<figure class="lesson-figure" markdown="1">

![Swap sends vector one,minus-one to its negative while both remain on the same antisymmetric line.](../../figures/assets/A09-SYM/A09-SYM-06-invariant-span-not-fixed.svg)

<figcaption>Since P(1,−1)ᵀ=(−1,1)ᵀ, the vector is not fixed but remains in the span of u₋. An invariant subspace does not require every vector in it to stay in place; every allowed action must keep vectors inside the subspace.</figcaption>

</figure>

<figure class="lesson-figure" markdown="1">

![The candidate x-axis remains under identity but swap sends its unit vector to the y-axis, so it is not invariant under the entire swap group.](../../figures/assets/A09-SYM/A09-SYM-06-all-actions-subspace.svg)

<figcaption>Candidate W=span(1,0)ᵀ is preserved by the identity, but P sends (1,0)ᵀ to (0,1)ᵀ outside W. Finding an eigenvector of one action or testing only some transformations does not establish a common invariant subspace.</figcaption>

</figure>

### Decomposing the swap into two components

The representation swapping two coordinates decomposes $V=\mathbb R^2$ into the spans of $(1,1)$ and $(1,-1)$. The first component is unchanged by the swap, while the second changes sign. An equivariant linear map commutes with the group action and is constrained by this component structure.

Write $u_+=(1,1)^{\mathsf T}$ and $u_-=(1,-1)^{\mathsf T}$. Then $Pu_+=u_+$ and $Pu_-=-u_-$. Each span remains within itself, and their intersection is $\{0\}$. Every $x=(a,b)^{\mathsf T}$ also has the unique expression

$$
x=\frac{a+b}{2}u_++\frac{a-b}{2}u_-
$$

Thus, the direct sum of the two spans is the entire $V$. Each span is one-dimensional and has no nonzero proper subspace, so both restricted representations in this example are irreducible. A vector in the antisymmetric component changes sign under the swap, but its span is invariant.

An equivariant linear map $A$ between spaces with the same action satisfies $AP=PA$. For a vector with $Pv=v$, the equality $PAv=APv=Av$ keeps $Av$ in the symmetric span. For $Pv=-v$, likewise $PAv=-Av$, so the image lies in the antisymmetric span. Maps mixing these two components are not allowed in this example. In general, repeated copies of the same irreducible component may be mixed, so decomposition alone does not uniquely determine individual channels.

After decomposing the swap components, track their respective actions and the allowed component mixing below.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Vector three,one decomposes into symmetric two,two and antisymmetric one,minus-one; swap retains the first and reverses the second to reach one,three.](../../figures/assets/A09-SYM/A09-SYM-06-swap-direct-sum.svg)

<figcaption>In (3,1)ᵀ=(2,2)ᵀ+(1,−1)ᵀ, the symmetric component remains unchanged and only the antisymmetric component reverses sign, giving (1,3)ᵀ. The two 1D spans intersect at 0, and both coefficients are unique in this example. The translated component arrows represent the same vectors.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A commuting map acts separately on the symmetric and antisymmetric swap components, scaling coefficients two and one to four and three.](../../figures/assets/A09-SYM/A09-SYM-06-equivariant-component-blocks.svg)

<figcaption>An equivariant A between the same swap actions satisfies AP=PA and preserves the u₊ and u₋ spans separately. Example A=diag(2,3) maps coefficients 2 and 1 to 4 and 3 in this basis, producing Ax=(7,1)ᵀ. The diagonal notation here uses the (u₊,u₋) basis, not the original coordinates.</figcaption>

</figure>

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two identical plus-component copies mix through an invertible triangular matrix while the group action remains identity.](../../figures/assets/A09-SYM/A09-SYM-06-repeated-component-mixing.svg)

<figcaption>When the same + representation occurs twice, mixing its two coefficients with U=[1 1;0 1] still commutes with ρ(g)=I. Each is an invariant 1D copy, and their combined 2D space is reducible because it can be decomposed further. Knowing component types does not uniquely determine individual channel coordinates.</figcaption>

</figure>

### What to check in learned activations

A plausible-looking basis on finite samples does not identify irreducible representations. The group action, closure, subspace stability, and multiplicity must be checked.

First specify input transform $g$ and its corresponding activation transformation rule $\rho(g)$, and check identity, composition, and linearity. Then check whether every $\rho(g)$ keeps vectors of the candidate subspace within it. Approximate empirical agreement provides evidence only for the transformations and inputs tested, and must be distinguished from an exact algebraic identity.

After finding an invariant subspace, examine whether it can be decomposed into smaller common invariant subspaces before claiming irreducibility. Diagonalizing one action matrix or obtaining a small reconstruction error does not replace this step. With repeated components, allowed basis mixing can leave feature-channel labels unfixed. Without character calculations, this lesson covers only these distinctions and the swap decomposition above.

Testing learned activations starts by comparing vectors from two routes, but that comparison alone does not establish irreducibility.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Two routes transform input before encoding or apply a specified linear group action after encoding, then compare vectors on held-out inputs.](../../figures/assets/A09-SYM/A09-SYM-06-activation-action-test.svg)

<figcaption>First specify input transform g and activation transformation rule ρ(g), then compare h(g·x) with ρ(g)h(x) on held-out inputs. The figure is a test design, not an execution result. Even if some examples agree, identity, composition, linearity, subspace stability under all actions, and possible further decomposition require separate checks.</figcaption>

</figure>

## Small example

The matrix $P=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ acts on $(1,1)$ with eigenvalue 1 and on $(1,-1)$ with eigenvalue $-1$.

For $x=(3,1)^{\mathsf T}$, the symmetric coefficient is 2 and the antisymmetric coefficient is 1. Thus, $x=(2,2)^{\mathsf T}+(1,-1)^{\mathsf T}$, and after the swap it becomes $(2,2)^{\mathsf T}-(1,-1)^{\mathsf T}=(1,3)^{\mathsf T}$. This calculation tracks the same vector through the transformation rules of its two components.

## Common misconceptions

- Representation here is not synonymous with a machine-learning hidden representation. Here it is a group's linear action.
- An irreducible component need not be one-dimensional.

## Exercises

### 1. Homomorphism
Explain why $\rho(n)=R_{n\theta}$ is a rotation representation of the integer addition group.
<details><summary>Show solution</summary>

Since $R_{(m+n)\theta}=R_{m\theta}R_{n\theta}$ and $R_0=I$, it is a homomorphism.
</details>

### 2. Invariant subspace
Show that $\operatorname{span}(1,1)$ is invariant under the swap matrix.
<details><summary>Show solution</summary>

Since $P(1,1)=(1,1)$, the entire span maps to itself.
</details>

### 3. Components
Decompose $x=(3,1)$ into symmetric and antisymmetric components.
<details><summary>Show solution</summary>

The decomposition is $(2,2)+(1,-1)$.
</details>

### 4. Model interpretability
What intervention can test a claim that an activation subspace is a group component?
<details><summary>Show solution</summary>

Transform inputs by the group and test on held-out samples whether activations change according to the prespecified $\rho(g)$.
</details>

## Evidence and update boundaries

Linear representations, invariant subspaces, and irreducibility follow standard definitions in representation theory. Character theory and noncompact groups are not covered.

- [MIT Algebra II notes, Lecture 1: Representations](https://ocw.mit.edu/courses/res-18-012-algebra-ii-student-notes-spring-2022/mit18_702s22_lec1.pdf): Provides the connection between real linear representations and matrix or coordinate-free actions. The two-coordinate swap decomposition in the text was computed directly from the given matrix.
- [Lecture 2 of the same course, §§2.3–2.4](https://ocw.mit.edu/courses/res-18-012-algebra-ii-student-notes-spring-2022/mit18_702s22_lect2.pdf): Provides definitions of invariant subspaces and irreducibility for comparison with the swap direct sum. Character calculations are outside this lesson's scope.

## Lesson summary

- A representation maps a group to invertible linear maps.
- An invariant subspace is preserved under every group action.
- Irreducible decomposition reveals symmetry-coupled channels.
- Claims of irreducible structure in learned activations require transformation tests.

## Pass criteria

- Can you decompose a simple representation into invariant components?
- Can you distinguish algebraic representations from hidden representations?

## Next lesson

- [A09-SYM-07 Model alignment and equivalence classes](A09-SYM-07-model-alignment-equivalence-classes.md)

## Author checklist

- [x] The core object types in representation theory are distinguished.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
