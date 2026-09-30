---
id: "A09-SYM-02"
title: "orbit와 stabilizer"
part: 4
stage: "A09-SYM"
status: "완료"
prerequisites: ["A09-SYM-01", "M03-06"]
estimated_time: "90~120분"
---

# A09-SYM-02. orbit와 stabilizer

## 이 단원이 필요한 이유

대칭변환으로 서로 이동할 수 있는 parameter는 같은 기능적 해의 여러 coordinate 표현일 수 있다. orbit는 한 대상의 모든 대칭 복사본을 모으고 stabilizer는 그 대상을 그대로 두는 변환을 모은다.

## 학습 목표

- orbit와 stabilizer를 계산할 수 있다.
- orbit가 동치류를 만드는 이유를 설명할 수 있다.
- orbit–stabilizer 관계를 finite example에 적용할 수 있다.
- parameter distance가 symmetry orbit 때문에 커질 수 있음을 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-SYM-01 group과 action](A09-SYM-01-groups-actions.md), [M03-06 동치관계와 몫공간](../../part-1-foundations/M03/M03-06-equivalence-relations-quotient-spaces.md)
- 확인 질문: 동치관계로 같은 것으로 볼 대상을 묶으면 무엇이 생기는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $G\cdot x$ | `the G orbit of x` | $x$의 orbit | subset of $X$ |
| $G_x$ | `the stabilizer of x` | $x$를 고정하는 subgroup | subgroup of $G$ |
| $X/G$ | `X modulo G` | orbit들의 quotient | set of equivalence classes |
| $|G\cdot x|$ | `the size of the orbit of x` | finite orbit cardinality | positive integer |

## 핵심 개념

$$
G\cdot x=\{g\cdot x:g\in G\},
\qquad
G_x=\{g\in G:g\cdot x=x\}.
$$

같은 orbit에 속한다는 관계는 동치관계이며 quotient $X/G$는 coordinate redundancy를 제거한 대상을 나타낸다. finite group에서는

$$
|G\cdot x|=\frac{|G|}{|G_x|}
$$

이다. stabilizer가 크면 서로 다른 orbit point 수가 줄어든다.

model parameter $\theta$의 orbit가 같은 function을 나타낸다면 raw $\|\theta_1-\theta_2\|$는 기능적 차이와 symmetry displacement를 섞는다.

## 작은 예제

$S_3$가 vector $(1,1,2)$의 coordinate를 permute하면 orbit에는 $(1,1,2),(1,2,1),(2,1,1)$ 세 개가 있다. 같은 두 1을 바꾸는 두 permutation이 stabilizer를 이룬다.

## 흔한 오해

- stabilizer는 orbit와 반대 개념이 아니라 orbit 크기를 결정하는 subgroup이다.
- quotient를 취했다고 각 동치류의 canonical representative가 자동으로 정해지지 않는다.

## 연습문제

### 1. orbit
부호 group $\{+1,-1\}$이 실수에 곱셈으로 작용할 때 $x=3$의 orbit를 구하라.
<details><summary>해설 보기</summary>

$\{3,-3\}$이다.
</details>

### 2. stabilizer
같은 action에서 $x=0$의 stabilizer를 구하라.
<details><summary>해설 보기</summary>

두 element 모두 0을 고정하므로 group 전체다.
</details>

### 3. orbit–stabilizer
$|G|=24$, $|G_x|=6$이면 orbit 크기는 얼마인가?
<details><summary>해설 보기</summary>

$24/6=4$이다.
</details>

### 4. checkpoint 비교
두 checkpoint의 raw parameter distance가 큰데 같은 orbit일 수 있다면 무엇을 추가로 계산해야 하는가?
<details><summary>해설 보기</summary>

허용한 group action에 대해 $\min_g\|\theta_1-g\cdot\theta_2\|$ 같은 symmetry-aligned distance나 function distance를 계산한다.
</details>

## 근거와 갱신 경계

orbit·stabilizer·quotient action은 group theory의 표준 정의를 따른다. continuous group에서의 measure와 orbit geometry는 다루지 않는다.

## 단원 요약

- orbit는 한 대상의 모든 symmetry copy다.
- stabilizer는 대상을 고정하는 subgroup이다.
- quotient는 orbit를 하나의 동치류로 본다.
- raw parameter distance는 orbit 방향 이동을 기능 차이로 셀 수 있다.

## 통과 기준

- finite action의 orbit와 stabilizer를 구할 수 있는가?
- symmetry-aligned 비교가 필요한 이유를 설명할 수 있는가?

## 다음 단원

- [A09-SYM-03 invariant와 equivariant](A09-SYM-03-invariant-equivariant.md)

## 집필자 점검표

- [x] orbit·stabilizer·quotient를 연결했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
