---
id: "A09-SYM-02"
title: "Orbits and stabilizers"
part: 4
stage: "A09-SYM"
status: "complete"
prerequisites: ["A09-SYM-01", "M03-06"]
estimated_time: "90–120 minutes"
---

# A09-SYM-02. Orbits and stabilizers

## Why this lesson matters

Parameters connected by symmetry transformations can be different coordinate descriptions of the same functional solution. An orbit collects all symmetry copies of an object, while a stabilizer collects the transformations leaving that object unchanged.

## Learning objectives

- Calculate orbits and stabilizers.
- Explain why orbits form equivalence classes.
- Apply the orbit–stabilizer relation to a finite example.
- Explain why a symmetry orbit can lead to a large parameter distance.

## Prerequisite check

- Prerequisite lessons: [A09-SYM-01 Groups and actions](A09-SYM-01-groups-actions.md), [M03-06 Equivalence relations and quotient spaces](../../part-1-foundations/M03/M03-06-equivalence-relations-quotient-spaces.md)
- Check question: What results when an equivalence relation groups objects that are treated as the same?

## Symbols and terms

| Symbol or term | Common spoken reading | Meaning | Shape and scope |
|---|---|---|---|
| $G\cdot x$ | `the G orbit of x` | Orbit of $x$ | subset of $X$ |
| $G_x$ | `the stabilizer of x` | Subgroup fixing $x$ | subgroup of $G$ |
| $X/G$ | `X modulo G` | Quotient of orbits | set of equivalence classes |
| $\lvert G\cdot x\rvert$ | `the size of the orbit of x` | Finite orbit cardinality | positive integer |

## Core concept 1. An orbit contains every result obtained by transforming an object

Let a group $G$ act on a set $X$. The orbit of $x\in X$ is

$$
G\cdot x
=
\{g\cdot x:g\in G\}
$$

Different group elements can reach the same orbit point. An orbit is the set of distinct **resulting objects**, not a list of transformations used.

Define $x\sim y$ when there is some $g$ such that $y=g\cdot x$. This is an equivalence relation: the identity ensures reflexivity, inverses ensure symmetry, and group products ensure transitivity. Thus, $X$ is partitioned into disjoint orbits.

We can check each condition through the action equations. Since $x=e\cdot x$, an object belongs to its own orbit. If $y=g\cdot x$, then $x=g^{-1}\cdot y$, reversing reachability. If $z=h\cdot y$, then $z=(hg)\cdot x$, so two successive transformations also stay in the same orbit. Consequently, if $x$ and $y$ meet in the same orbit even once, the entire orbits obtained by starting from either point are the same.

## Core concept 2. A stabilizer contains the transformations that do not move an object

The stabilizer of $x$ is

$$
G_x
=
\{g\in G:g\cdot x=x\}
$$

The identity always belongs to $G_x$, and both products and inverses of transformations fixing $x$ also fix $x$. Therefore, $G_x$ is a subgroup of $G$.

If $g\cdot x=h\cdot x=x$, then $(gh)\cdot x=g\cdot(h\cdot x)=x$. Applying $g^{-1}$ to both sides of $g\cdot x=x$ also gives $g^{-1}\cdot x=x$. These calculations show closure of the stabilizer for the specified object $x$. The same $g$ need not also fix a different object $y$. Reading elements of $G_x$ as “transformations that do nothing” therefore misses the object to which they apply.

A large stabilizer means that many group elements act on $x$ without creating a new position: they return the same $x$. An object with more symmetries can have a larger stabilizer.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Three points in an orbit and two stabilizer transformations that leave the original point fixed](../../figures/assets/A09-SYM/A09-SYM-02-orbit-stabilizer.svg)

<figcaption>The orbit on the left collects the distinct objects reachable from x. The stabilizer on the right collects cases where different transformations still leave the result at the same x.</figcaption>
</figure>

The number of arrows on the left need not equal the number of orbit points. If two different transformations send the object to the same point, a stabilizer element fixing $x$ explains their difference. This redundancy is why the size of the stabilizer reduces the size of the orbit.

Compare which objects the same transformation fixes.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The swap of slots one and two fixes (1,1,2) but changes (1,2,3), even though the same permutation acts in both panels.](../../figures/assets/A09-SYM/A09-SYM-02-object-specific-stabilizer.svg)

<figcaption>The permutation (12) swaps two component positions. The object x is unchanged because both values are 1, but y changes to (2,1,3). An element of Gₓ need not also fix another object y.</figcaption>
</figure>

## Core concept 3. Orbit size is the number of stabilizer cosets

For a finite group, consider the map $g\mapsto g\cdot x$. Two elements $g_1,g_2$ produce the same orbit point exactly when

$$
g_1\cdot x=g_2\cdot x
\quad\Longleftrightarrow\quad
g_2^{-1}g_1\in G_x
$$

In other words, group elements in the same left coset produce the same result at $x$. The number of distinct orbit points therefore equals the number of stabilizer cosets, giving

$$
|G\cdot x|
=
\frac{|G|}{|G_x|}
$$

This is not simply a formula to memorize by dividing the number of group elements by the number of results. It is a counting statement: each collection of transformations producing the same result has size $|G_x|$.

The left coset $g_2G_x$ is $\{g_2h:h\in G_x\}$. The condition above is equivalent to the existence of a stabilizer element $h$ such that $g_1=g_2h$. Since $(g_2h)\cdot x=g_2\cdot x$, all elements of one coset produce the same destination. Conversely, equal destinations mean that $h=g_2^{-1}g_1$ fixes $x$. Also, the correspondence $h\mapsto g_2h$ is one-to-one, so each coset contains $|G_x|$ elements. Distinct cosets do not overlap, so divide $|G|$ by this collection size. Finiteness is needed for this final division of sizes.

Group redundant transformations by the destination of each left coset.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![The six S3 permutations form three left cosets of {identity,(12)}, each pair sending (1,1,2) to one of three distinct orbit vectors.](../../figures/assets/A09-SYM/A09-SYM-02-s3-coset-orbit-fibers.svg)

<figcaption>For x=(1,1,2) in the text, Gₓ={e,(12)}. The cosets (23)Gₓ={(23),(132)} and (13)Gₓ={(13),(123)} each produce the same destination vector within their pair. The orbit is 3 distinct results, not a list of 6 transformations. Three collections of size 2 explain 6/2=3.</figcaption>
</figure>

## Core concept 4. A quotient groups symmetry directions into single elements

The quotient $X/G$ is the set treating each orbit as one element. If a parameter-symmetry orbit represents the same function throughout, one point of the quotient can correspond to one functional solution. Taking a quotient does not, however, automatically choose a representative parameter from each orbit.

A quotient element is an equivalence class $[x]=G\cdot x$, not a single coordinate vector. Writing this set down does not automatically supply addition, a distance, or a group operation. If a parameter action preserves the function, parameters in the same orbit represent the same function, but parameters in other orbits can also represent that function. It is a separate assumption that the chosen symmetries account for every source of functional equivalence.

If the orbit of model parameter $\theta$ represents the same function, the raw distance

$$
\|\theta_1-\theta_2\|
$$

counts both functional differences and motion along a symmetry orbit. Under a permitted group $G$, we can compare a symmetry-aligned distance such as

$$
d_G(\theta_1,\theta_2)
=
\min_{g\in G}
\|\theta_1-g\cdot\theta_2\|
$$

For a finite group, a minimum exists among all candidates. For a general infinite group, a minimum might not be attained, so distinguish it from an infimum. To interpret this expression as a quotient distance independent of representative coordinates, we must also check conditions such as whether the action preserves distances in the chosen norm. Permutations with the Euclidean norm satisfy this condition, but general scaling does not.

Which $G$ was permitted and whether the minimum was actually found are part of the result. Demonstrating that parameters belong to exactly the same orbit under a function-preserving action also establishes functional equivalence. By contrast, a small distance after alignment means that the parameters are close under the chosen transformations. How strongly that small difference affects outputs requires separate evaluation.

Check the quotient map sending an entire orbit to one element.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Coordinate-swap orbits {(1,3),(3,1)}, {(2,4),(4,2)}, and {(2,2)} map to three distinct quotient classes without selecting representatives.](../../figures/assets/A09-SYM/A09-SYM-02-quotient-disjoint-orbits.svg)

<figcaption>In this coordinate-swap example, each point moves within its own orbit. The quotient map sends the two points of A to one class and the two points of B to another, while the fixed point (2,2) forms a separate class C. The notation [A] takes the entire orbit as an element; it does not automatically select one coordinate representation.</figcaption>
</figure>

Compare the raw distance with the distance after a permitted permutation.

<figure class="lesson-figure" markdown="1">

![Two vectors related by coordinate swap have raw Euclidean distance square root of eight but zero permutation-aligned distance.](../../figures/assets/A09-SYM/A09-SYM-02-raw-aligned-distance.svg)

<figcaption>Vectors (1,3) and (3,1) have raw Euclidean distance √8. Applying P to the second gives the first, making the aligned distance 0. This example uses the distance-preserving combination of a permutation and the Euclidean norm. For actual parameters, function preservation requires separately checking the action permitted by the model.</figcaption>
</figure>

## Small example

Let $S_3$ permute the coordinates of vector $(1,1,2)$. The group has size $|S_3|=6$, but the orbit contains only the three vectors

$$
(1,1,2),\quad(1,2,1),\quad(2,1,1)
$$

The first two coordinates both equal 1, so the identity and the permutation exchanging the positions of those two 1s leave the original vector unchanged. The stabilizer therefore has size 2, and

$$
|S_3\cdot(1,1,2)|
=
\frac{6}{2}
=3
$$

agrees with the actual orbit size. If all three coordinate values were different, only the identity would remain in the stabilizer, and the orbit would have size 6.

## Common misconceptions

- A stabilizer is not the opposite of an orbit; it is the subgroup determining orbit size.
- Taking a quotient does not automatically choose a canonical representative of each equivalence class.

## Exercises

### 1. Orbit
When the sign group $\{+1,-1\}$ acts on real numbers by multiplication, find the orbit of $x=3$.
<details><summary>Show solution</summary>

It is $\{3,-3\}$.
</details>

### 2. Stabilizer
For the same action, find the stabilizer of $x=0$.
<details><summary>Show solution</summary>

Both elements fix 0, so the stabilizer is the whole group.
</details>

### 3. Orbit–stabilizer
If $|G|=24$ and $|G_x|=6$, what is the orbit size?
<details><summary>Show solution</summary>

It is $24/6=4$.
</details>

### 4. Comparing checkpoints
If two checkpoints have a large raw parameter distance but might belong to the same orbit, what else should you calculate?
<details><summary>Show solution</summary>

Calculate a symmetry-aligned distance such as $\min_g\|\theta_1-g\cdot\theta_2\|$ under the permitted group action, or a function distance.
</details>

## Sources and update boundaries

Orbits, stabilizers, and quotient actions follow standard definitions in group theory. This lesson does not cover measures or orbit geometry for continuous groups.

- [MIT Algebra I notes, Lectures 17–18](https://ocw.mit.edu/courses/res-18-011-algebra-i-student-notes-fall-2021/mit18_701f21_full_lec_new.pdf): A standard reference for orbits, stabilizers, and the finite counting relation. The text distinguishes the conditions for distance comparisons in terms of the norm and action used.

## Lesson summary

- An orbit contains all symmetry copies of one object.
- A stabilizer is the subgroup fixing that object.
- A quotient treats an orbit as one equivalence class.
- Raw parameter distance can count motion along an orbit as a functional difference.

## Pass criteria

- Can you find the orbits and stabilizers of a finite action?
- Can you explain why symmetry-aligned comparison is needed?

## Next lesson

- [A09-SYM-03 Invariance and equivariance](A09-SYM-03-invariant-equivariant.md)

## Author checklist

- [x] Orbits, stabilizers, and quotients are connected.
- [x] All 4 exercises have solutions.
- [x] Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.
- [x] Prerequisites and links have been checked.
