---
id: "A09-CAU-06"
title: "causal abstraction"
part: 4
stage: "A09-CAU"
status: "완료"
prerequisites: ["M03-02", "I07-11", "A09-CAU-02"]
estimated_time: "90~120분"
---

# A09-CAU-06. causal abstraction

## 이 단원이 필요한 이유

mechanistic interpretation은 neuron과 activation의 low-level computation이 variable·rule로 표현한 high-level algorithm을 구현한다고 주장한다. observational prediction이 맞는 것만으로 구현 관계를 정할 수 없다. 대응하는 intervention이 두 수준에서 같은 결과를 만들어야 causal abstraction claim이 성립한다.

## 학습 목표

- low-level state와 high-level state를 잇는 abstraction map을 정의할 수 있다.
- low-level intervention과 high-level intervention의 대응을 쓸 수 있다.
- intervention commuting condition을 설명할 수 있다.
- approximate abstraction error와 held-out intervention을 설계할 수 있다.

## 선수지식 확인

- 선수 단원: [M03-02 선형사상과 행렬 표현](../../part-1-foundations/M03/M03-02-linear-maps-matrix-representation.md), [I07-11 circuit을 그래프로 표현하기](../../part-3-interpretability/I07/I07-11-circuit-graph.md), [A09-CAU-02 do 연산과 intervention](A09-CAU-02-do-operator-interventions.md)
- 확인 질문: high-level variable 하나가 low-level neuron 하나와 일대일 대응하지 않아도 되는 이유는 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\tau:\mathcal L\to\mathcal H$ | `tau maps the low-level state space L to the high-level state space H` | low-level state를 high-level state로 요약하는 map | function |
| $i_L$ | `the low-level intervention i L` | model component에 적용하는 intervention | operation |
| $i_H$ | `the high-level intervention i H` | abstract variable에 적용하는 intervention | operation |
| $\epsilon_{\mathrm{abs}}$ | `epsilon sub abs` | 두 intervention path의 output discrepancy | nonnegative scalar |

## 핵심 개념

low-level model state $l\in\mathcal L$을 high-level state $h=\tau(l)\in\mathcal H$로 보낸다. high-level intervention $i_H$마다 대응 low-level intervention $i_L$를 정한다. exact causal abstraction은 허용 intervention에 대해 두 경로가 같은 abstract outcome을 만드는 조건을 요구한다.

$$
\tau\bigl(i_L(l)\bigr)
=i_H\bigl(\tau(l)\bigr)
$$

실제 동적 model에서는 intervention 뒤 downstream computation까지 포함한 outcome map으로 두 경로를 비교한다. approximate abstraction은 distance $d_{\mathcal H}$를 정하고

$$
\epsilon_{\mathrm{abs}}
=E\left[d_{\mathcal H}\left(\tau(i_L(L)),i_H(\tau(L))\right)\right]
$$

를 측정한다.

$\tau$는 probe, sparse feature, subspace projection이나 discrete decoder가 될 수 있다. training input에서 $\tau$를 선택하고 같은 intervention에서 평가하면 overfitting된다. abstraction map과 intervention correspondence를 validation에서 고른 뒤 held-out prompt·intervention에서 검사한다.

## 작은 예제

high-level variable가 `subject number`이고 low-level state가 residual subspace라면 $\tau$는 singular/plural score를 추출한다. high-level flip intervention에 대응해 low-level direction을 반전했을 때 downstream verb-number output도 예측대로 바뀌는지 검사한다.

## 흔한 오해

- high-level variable을 잘 decode하는 것만으로 causal abstraction이 성립하지 않는다.
- 한 intervention에서 commuting한 결과가 모든 high-level operation의 구현을 보장하지 않는다.

## 연습문제

### 1. map
$\tau(l)=\operatorname{sign}(w^\top l)$이면 high-level state space는 어떤 두 값으로 둘 수 있는가?
<details><summary>해설 보기</summary>

$\{-1,+1\}$ 또는 대응하는 두 symbolic label로 둘 수 있다.
</details>

### 2. commuting
low-level flip 뒤 $\tau$ 값은 바뀌었지만 downstream high-level output은 예측대로 변하지 않았다. causal abstraction이 통과하는가?
<details><summary>해설 보기</summary>

통과하지 않는다. state decoding만 바뀌고 intervention consequence가 high-level model과 일치하지 않는다.
</details>

### 3. selection
abstraction map을 고른 prompt와 같은 prompt에서 error를 보고하면 어떤 bias가 생기는가?
<details><summary>해설 보기</summary>

map과 intervention을 data에 맞춘 selection bias가 생긴다. held-out prompt와 operation이 필요하다.
</details>

### 4. 모델 해석
하나의 high-level variable이 여러 head에 분산돼 있다. low-level intervention을 어떻게 정의하는가?
<details><summary>해설 보기</summary>

해당 variable을 보존·변경하는 joint subspace 또는 여러 node의 coordinated intervention을 정의하고 dimension-matched control과 비교한다.
</details>

## 근거와 갱신 경계

이 단원은 intervention correspondence와 commuting condition을 실험 설계 수준에서 다룬다. category theory 기반 abstraction formalism의 완전한 정의는 범위 밖이다.

## 단원 요약

- causal abstraction은 low-level state를 high-level variable로 잇는다.
- 두 수준의 intervention이 대응 결과를 만들어야 한다.
- decoding accuracy와 intervention consistency는 다른 증거이다.
- abstraction map은 held-out prompt와 intervention에서 검증한다.

## 통과 기준

- abstraction map과 intervention pair를 정의할 수 있는가?
- observational decoding과 causal implementation claim을 구분할 수 있는가?

## 다음 단원

- [A09-CAU-07 내부 개입의 외적 타당성](A09-CAU-07-external-validity-internal-interventions.md)

## 집필자 점검표

- [x] abstraction map·intervention correspondence·held-out 검증을 설명했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
