---
id: "A09-LRN-06"
title: "PAC learning"
part: 4
stage: "A09-LRN"
status: "완료"
prerequisites: ["A09-LRN-04", "M04-10"]
estimated_time: "90~120분"
---

# A09-LRN-06. PAC learning

## 이 단원이 필요한 이유

학습 가능성을 말하려면 얼마나 작은 error를 얼마나 높은 probability로 달성하며 sample 수가 어떻게 증가하는지를 정해야 한다. PAC framework는 accuracy $\varepsilon$와 confidence $1-\delta$를 분리해 sample complexity를 표현한다.

## 학습 목표

- PAC guarantee의 probability statement를 읽을 수 있다.
- realizable·agnostic setting을 구분할 수 있다.
- sample complexity에서 $\varepsilon,\delta$의 역할을 설명할 수 있다.
- theorem guarantee와 한 번의 empirical result를 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-LRN-04 VC dimension](A09-LRN-04-vc-dimension.md), [M04-10 가설검정](../../part-1-foundations/M04/M04-10-hypothesis-testing-multiple-comparisons.md)
- 확인 질문: 확률 $1-\delta$는 test example 하나의 예측 확률인가, training sample 반복의 확률인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\varepsilon$ | `epsilon` | 허용 excess risk | positive scalar |
| $\delta$ | `delta` | failure probability | $(0,1)$ |
| $m_{\mathcal H}(\varepsilon,\delta)$ | `the sample complexity of H at epsilon and delta` | 필요한 sample 수 | positive integer |
| $R(\hat h)\le\inf_{h\in\mathcal H}R(h)+\varepsilon$ | `the risk of h hat is at most the best risk in H plus epsilon` | agnostic target | inequality |

## 핵심 개념

agnostic PAC guarantee의 전형적 형태는 sample $S\sim P^n$에 대해

$$
P_S\left(
R(\hat h_S)\le \inf_{h\in\mathcal H}R(h)+\varepsilon
\right)\ge1-\delta
$$

이다. probability는 training sample의 반복에 대한 것이다.

realizable setting은 class 안에 zero-risk target이 있다고 가정한다. agnostic setting은 그러지 않으며 best-in-class와의 excess risk를 제어한다. finite VC dimension이나 Rademacher complexity는 sample complexity bound를 제공한다.

PAC learnable이라는 사실은 bound가 실무 sample size에서 tight하다는 뜻도, optimization이 효율적이라는 뜻도 아니다.

## 작은 예제

$\delta=0.05$는 동일한 data-generating process에서 training sample을 반복했을 때 guarantee가 실패할 확률을 5% 이하로 제한한다는 뜻이다.

## 흔한 오해

- $1-\delta$를 개별 prediction confidence로 읽으면 안 된다.
- PAC guarantee는 distribution shift 뒤에도 자동 유지되지 않는다.

## 연습문제

### 1. confidence
$\delta=0.01$이면 guarantee probability는 얼마인가?
<details><summary>해설 보기</summary>

$1-0.01=0.99$다.
</details>

### 2. excess risk
best-in-class risk가 0.12, $\varepsilon=0.03$이면 허용 upper bound는 얼마인가?
<details><summary>해설 보기</summary>

$0.15$다.
</details>

### 3. realizability
label noise가 있고 deterministic classifier class만 쓰면 realizable assumption이 실패할 수 있는 이유는 무엇인가?
<details><summary>해설 보기</summary>

같은 input에 서로 다른 label이 생기면 class 안 어떤 deterministic function도 population error 0을 달성하지 못할 수 있다.
</details>

### 4. 모델 해석
probe 하나의 test accuracy가 PAC learnability를 증명하지 않는 이유는 무엇인가?
<details><summary>해설 보기</summary>

PAC는 sample size에 따른 uniform probability guarantee이며 한 split의 point estimate는 class·algorithm 전체의 guarantee가 아니다.
</details>

## 근거와 갱신 경계

PAC·realizable·agnostic learning은 computational learning theory의 표준 정의를 따른다. computational efficiency와 online learning은 다루지 않는다.

## 단원 요약

- PAC는 accuracy와 confidence를 분리한다.
- probability는 training sample 반복에 대한 것이다.
- agnostic setting은 best-in-class excess risk를 제어한다.
- 이론 sample bound와 한 번의 empirical accuracy를 구분한다.

## 통과 기준

- PAC probability statement를 말로 풀 수 있는가?
- realizable·agnostic·distribution shift를 구분할 수 있는가?

## 다음 단원

- [A09-LRN-07 probe와 해석의 일반화](A09-LRN-07-probe-interpretation-generalization.md)

## 집필자 점검표

- [x] PAC의 두 probability 수준을 혼동하지 않았다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
