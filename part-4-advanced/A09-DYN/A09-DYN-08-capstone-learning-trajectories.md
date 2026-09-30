---
id: "A09-DYN-08"
title: "종합 실습: 학습 궤적 분석"
part: 4
stage: "A09-DYN"
status: "완료"
prerequisites: ["A09-DYN-01", "A09-DYN-02", "A09-DYN-03", "A09-DYN-04", "A09-DYN-05", "A09-DYN-06", "A09-DYN-07"]
estimated_time: "120~180분"
---

# A09-DYN-08. 종합 실습: 학습 궤적 분석

## 이 단원이 필요한 이유

checkpoint 몇 개를 선으로 잇는 것만으로 learning dynamics를 설명할 수 없다. time coordinate, state, distance, stochastic repetition과 interpolation error를 고정해야 trajectory·stability·transition 주장을 분리할 수 있다.

## 학습 목표

- 학습 궤적 분석의 state와 time을 정의할 수 있다.
- drift·noise·local stability의 측정 계획을 세울 수 있다.
- paired seed와 checkpoint resolution을 포함한 control을 설계할 수 있다.
- 관측된 궤적에서 허용되는 주장 강도를 판정할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-DYN-01~07](A09-DYN-07-continuous-time-sgd.md)
- 확인 질문: optimizer step과 processed token 수 중 어느 것을 time으로 쓸지는 왜 결과를 바꾸는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $z_k$ | `z sub k` | checkpoint state summary | vector |
| $\Delta z_k$ | `delta z sub k` | successive displacement | vector |
| $\hat b(z)$ | `b hat of z` | empirical local drift | vector |
| $\hat C(z)$ | `C hat of z` | empirical update covariance | PSD matrix |

## 분석 계약

claim은 “고정한 training recipe에서 paired seed의 checkpoint summary가 재현 가능한 drift와 변동 패턴을 보인다”로 제한한다. state에는 parameter projection, function metric, representation statistic와 optimizer state 중 질문에 필요한 항목을 명시한다.

time axis는 optimizer step, processed token, cumulative learning rate 중 하나를 사전에 선택한다. checkpoint 사이를 선형 interpolation할 때 실제 update path를 관측한 것으로 표현하지 않는다.

## 측정 절차

1. 같은 initialization과 data order를 공유하는 paired condition을 만든다.
2. 고정 checkpoint에서 loss, function distance, update norm과 summary state를 기록한다.
3. repeated micro-batch gradient로 $\hat b$와 $\hat C$를 추정한다.
4. local Jacobian 또는 Hessian-vector product로 안정성 지표를 구한다.
5. checkpoint density를 늘린 sensitivity analysis와 time-shuffle null을 수행한다.

## 결과 기록표

| 질문 | estimand | measurement | 주요 한계 |
|---|---|---|---|
| 평균 이동 | conditional drift | paired mean $\Delta z$ | projection bias |
| stochasticity | update covariance | repeated batches | nonstationarity |
| 국소 안정성 | leading local rate | JVP·HVP | linearization |
| transition | change point interval | dense checkpoints | resolution·multiple testing |

## 흔한 오해

- smooth한 plot은 underlying continuous path를 관측했다는 뜻이 아니다.
- seed 평균 trajectory는 개별 run이 실제로 지나간 trajectory가 아닐 수 있다.

## 연습문제

### 1. time axis
batch size가 run마다 다를 때 optimizer step만 맞추면 공정한가?
<details><summary>해설 보기</summary>

일반적으로 아니다. processed example·token과 learning-rate schedule을 함께 맞추거나 차이를 estimand에 포함해야 한다.
</details>

### 2. interpolation
두 checkpoint 사이의 straight line loss가 낮으면 실제 SGD가 그 선을 지났다고 말할 수 있는가?
<details><summary>해설 보기</summary>

없다. 이는 별도 interpolation path의 측정이며 실제 update path 증거가 아니다.
</details>

### 3. noise covariance
같은 checkpoint에서 여러 mini-batch gradient가 필요한 이유는 무엇인가?
<details><summary>해설 보기</summary>

conditional mean과 covariance를 추정하려면 batch sampling 반복이 필요하기 때문이다.
</details>

### 4. transition claim
metric change point가 seed마다 크게 다르면 어떤 결론이 적절한가?
<details><summary>해설 보기</summary>

recipe 아래 transition timing의 변동성이 크다고 보고하고 단일 step의 보편적 phase transition 주장을 피한다.
</details>

## 근거와 갱신 경계

이 실습은 ODE·SDE 근사를 checkpoint 연구 설계와 연결한다. 특정 optimizer가 특정 SDE를 따른다는 결론을 미리 두지 않으며 empirical residual 진단으로 근사 범위를 정한다.

## 단원 요약

- state·time·metric을 먼저 고정한다.
- drift·noise·stability를 서로 다른 estimand로 측정한다.
- dense checkpoint와 paired seed로 resolution·variance를 평가한다.
- interpolation과 실제 학습 path를 구분한다.

## 통과 기준

- 학습 궤적의 claim–estimand–measurement–control을 작성할 수 있는가?
- 연속시간 해석이 실패할 수 있는 진단을 제시할 수 있는가?

## 다음 단원

- 다음 선택 모듈은 A09-SYM이다.

## 집필자 점검표

- [x] 학습 궤적 분석 계약과 주장 한계를 포함했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
