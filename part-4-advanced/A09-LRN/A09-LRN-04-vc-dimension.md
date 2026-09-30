---
id: "A09-LRN-04"
title: "VC dimension"
part: 4
stage: "A09-LRN"
status: "완료"
prerequisites: ["A09-LRN-01", "M00-07"]
estimated_time: "90~120분"
---

# A09-LRN-04. VC dimension

## 이 단원이 필요한 이유

parameter 수만으로 binary classifier class의 표현력을 비교하기 어려울 때 shattering은 가능한 label pattern 전체를 기준으로 capacity를 정의한다. VC dimension은 distribution-free uniform generalization bound의 대표적 complexity measure다.

## 학습 목표

- shattering과 VC dimension을 정의할 수 있다.
- 간단한 threshold·interval class의 VC dimension을 구할 수 있다.
- growth function과 uniform convergence의 관계를 설명할 수 있다.
- VC bound의 worst-case 성격을 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-LRN-01 hypothesis class와 risk](A09-LRN-01-hypothesis-class-risk.md), [M00-07 집합과 논리](../../part-1-foundations/M00/M00-07-sets-conditions-logic.md)
- 확인 질문: $n$개 점의 binary label pattern은 모두 몇 개인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\operatorname{VCdim}(\mathcal H)$ | `the V C dimension of H` | 최대 shatter 가능한 점 수 | nonnegative integer or infinity |
| $\Pi_{\mathcal H}(n)$ | `the growth function of H at n` | $n$개 점에서 가능한 label 수의 최댓값 | integer |
| $S$ | `S` | finite input set | set of points |
| $2^n$ | `two to the n` | 모든 binary labeling 수 | positive integer |

## 핵심 개념

$S=\{x_1,\ldots,x_n\}$의 모든 $2^n$ binary labeling을 $\mathcal H$가 실현하면 $S$를 shatter한다고 한다. VC dimension은 shatter 가능한 가장 큰 $n$이다.

real line의 threshold class $h_a(x)=1[x\ge a]$는 한 점은 shatter하지만 두 점의 pattern $(1,0)$을 만들 수 없어 VC dimension이 1이다. interval indicator는 두 점을 shatter할 수 있지만 세 점의 $(1,0,1)$을 만들 수 없어 VC dimension이 2다.

finite VC dimension은 empirical risk가 class 전체에서 population risk에 uniform하게 가까워지는 bound를 준다. 다만 constant와 worst-case distribution 때문에 실제 deep model의 gap보다 매우 느슨할 수 있다.

## 작은 예제

세 점 $x_1<x_2<x_3$에 interval classifier는 $x_1,x_3$만 positive이고 가운데는 negative인 pattern을 만들 수 없다.

## 흔한 오해

- VC dimension이 크다고 특정 dataset에서 반드시 overfit하는 것은 아니다.
- VC bound가 느슨하다는 사실은 generalization 측정이 불필요하다는 뜻이 아니다.

## 연습문제

### 1. label 수
4개 점의 binary labeling은 몇 개인가?
<details><summary>해설 보기</summary>

$2^4=16$개다.
</details>

### 2. constant class
$\mathcal H=\{h_0,h_1\}$ 두 constant classifier의 VC dimension은 얼마인가?
<details><summary>해설 보기</summary>

한 점은 두 label을 모두 만들 수 있어 shatter하지만 두 점의 mixed label은 못 만들므로 1이다.
</details>

### 3. threshold 반례
두 정렬된 점에서 threshold가 만들 수 없는 pattern을 하나 쓰라.
<details><summary>해설 보기</summary>

왼쪽이 1이고 오른쪽이 0인 pattern은 $h_a(x)=1[x\ge a]$로 만들 수 없다.
</details>

### 4. probe capacity
linear probe와 MLP probe의 성능 차이를 VC dimension 하나로 설명하기 어려운 이유는 무엇인가?
<details><summary>해설 보기</summary>

실제 regularization·optimizer·data geometry·loss와 finite sample 선택이 effective capacity와 성능에 함께 작용하기 때문이다.
</details>

## 근거와 갱신 경계

shattering·VC dimension·growth function은 Vapnik–Chervonenkis theory의 표준 정의를 따른다. Sauer–Shelah lemma의 증명과 tight constant는 다루지 않는다.

## 단원 요약

- shattering은 finite set의 모든 binary labeling 실현을 뜻한다.
- VC dimension은 최대 shattering 크기다.
- finite VC dimension은 distribution-free uniform bound를 가능하게 한다.
- 실제 deep learning gap의 정밀 예측값으로 사용하지 않는다.

## 통과 기준

- threshold·interval class의 VC dimension을 설명할 수 있는가?
- worst-case capacity bound와 empirical evaluation을 구분할 수 있는가?

## 다음 단원

- [A09-LRN-05 Rademacher complexity](A09-LRN-05-rademacher-complexity.md)

## 집필자 점검표

- [x] shattering과 VC dimension을 반례로 설명했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
