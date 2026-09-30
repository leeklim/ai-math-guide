---
id: "A09-SYM-06"
title: "representation theory 입문"
part: 4
stage: "A09-SYM"
status: "완료"
prerequisites: ["A09-SYM-03", "M03-01", "M03-05"]
estimated_time: "90~120분"
---

# A09-SYM-06. representation theory 입문

## 이 단원이 필요한 이유

group action이 vector space에서 linear하면 matrix로 분석할 수 있다. representation theory는 symmetry action을 invariant subspace와 irreducible component로 분해해 어떤 feature channel이 함께 변해야 하는지 설명한다.

## 학습 목표

- linear representation의 homomorphism 조건을 쓸 수 있다.
- invariant subspace와 irreducible representation을 구분할 수 있다.
- 간단한 permutation representation을 분해할 수 있다.
- learned representation에서 irreducible structure를 주장할 때 필요한 검증을 말할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-SYM-03 invariant와 equivariant](A09-SYM-03-invariant-equivariant.md), [M03-01 벡터공간](../../part-1-foundations/M03/M03-01-abstract-vector-spaces.md), [M03-05 부분공간](../../part-1-foundations/M03/M03-05-subspaces-direct-sums-decomposition.md)
- 확인 질문: 한 linear map family가 공통으로 보존하는 subspace는 무엇을 뜻하는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\rho:G\to GL(V)$ | `rho from G to G L of V` | linear representation | group homomorphism |
| $\rho(g_1g_2)=\rho(g_1)\rho(g_2)$ | `rho of g one g two equals rho of g one rho of g two` | homomorphism condition | matrix equality |
| $W\le V$ | `W is a subspace of V` | invariant subspace candidate | vector subspace |
| $V=\bigoplus_iV_i$ | `V is the direct sum of V i` | component decomposition | direct sum |

## 핵심 개념

representation은 group multiplication을 invertible linear map의 composition으로 보존한다. $W$가 모든 $g$에 대해 $\rho(g)W\subseteq W$이면 invariant subspace다. nonzero proper invariant subspace가 없는 representation을 irreducible이라 한다.

두 coordinate를 swap하는 representation은 $V=\mathbb R^2$를 $(1,1)$ span과 $(1,-1)$ span으로 분해한다. 첫 component는 swap에 unchanged이고 둘째는 sign이 바뀐다. equivariant linear map은 group action과 commute하며 이 component 구조의 제약을 받는다.

finite sample에서 특정 basis가 그럴듯하게 보인다는 사실만으로 irrep를 식별할 수 없다. group action, closure, subspace stability와 multiplicity를 확인해야 한다.

## 작은 예제

$P=\begin{bmatrix}0&1\\1&0\end{bmatrix}$는 $(1,1)$에 eigenvalue 1, $(1,-1)$에 eigenvalue $-1$로 작용한다.

## 흔한 오해

- representation은 machine-learning hidden representation과 같은 말이 아니다. 여기서는 group의 linear action이다.
- irreducible component가 항상 1차원인 것은 아니다.

## 연습문제

### 1. homomorphism
$\rho(n)=R_{n\theta}$가 integer addition group의 rotation representation임을 설명하라.
<details><summary>해설 보기</summary>

$R_{(m+n)\theta}=R_{m\theta}R_{n\theta}$이고 $R_0=I$이므로 homomorphism이다.
</details>

### 2. invariant subspace
swap matrix 아래 $\operatorname{span}(1,1)$이 invariant임을 보이라.
<details><summary>해설 보기</summary>

$P(1,1)=(1,1)$이므로 span 전체가 자신으로 간다.
</details>

### 3. component
$x=(3,1)$을 symmetric·antisymmetric component로 분해하라.
<details><summary>해설 보기</summary>

$(2,2)+(1,-1)$이다.
</details>

### 4. 모델 해석
activation subspace가 group component라고 주장하려면 어떤 intervention을 할 수 있는가?
<details><summary>해설 보기</summary>

입력을 group transform한 뒤 activation이 사전 지정한 $\rho(g)$에 따라 변하는지 held-out sample에서 검사한다.
</details>

## 근거와 갱신 경계

linear representation·invariant subspace·irreducibility는 representation theory의 표준 정의를 따른다. character theory와 noncompact group은 다루지 않는다.

## 단원 요약

- representation은 group을 invertible linear map으로 보낸다.
- invariant subspace는 모든 group action 아래 보존된다.
- irreducible decomposition은 symmetry-coupled channel을 드러낸다.
- learned activation의 irrep 주장은 transformation test가 필요하다.

## 통과 기준

- 간단한 representation을 invariant component로 분해할 수 있는가?
- algebraic representation과 hidden representation을 구분할 수 있는가?

## 다음 단원

- [A09-SYM-07 모델 정렬과 동치류](A09-SYM-07-model-alignment-equivalence-classes.md)

## 집필자 점검표

- [x] representation theory의 핵심 타입을 구분했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
