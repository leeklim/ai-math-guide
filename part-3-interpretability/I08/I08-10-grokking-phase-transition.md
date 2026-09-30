---
id: "I08-10"
title: "grokking과 phase transition"
part: 3
stage: "I08"
status: "완료"
prerequisites: ["I08-09", "M04-03"]
estimated_time: "90~120분"
---

# I08-10. grokking과 phase transition

## 이 단원이 필요한 이유

grokking은 training 성능이 이미 포화된 뒤 test 성능이 늦게 상승하는 현상으로 보고됐다. 그러나 sparse evaluation, threshold와 축 선택은 완만한 변화를 갑작스러워 보이게 할 수 있다. “phase transition”이라는 표현을 쓰려면 관측 곡선, transition 폭과 대안 설명을 분리해야 한다.

## 학습 목표

- delayed generalization을 train·test curve로 정의할 수 있다.
- transition 위치와 폭을 측정할 수 있다.
- checkpoint 간격이 apparent abruptness에 미치는 영향을 설명할 수 있다.
- 한 toy task의 grokking을 일반 모델의 보편 법칙으로 확대하지 않을 수 있다.

## 선수지식 확인

- 선수 단원: [I08-09 feature emergence](I08-09-feature-emergence.md), [M04-03 확률변수와 분포](../../part-1-foundations/M04/M04-03-random-variables-distributions.md)
- 확인 질문: 두 측정점 사이의 곡선 모양을 두 점만으로 결정할 수 있는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $A_{train}(t)$ | `A train of t` | step $t$의 training accuracy | $[0,1]$ |
| $A_{test}(t)$ | `A test of t` | step $t$의 test accuracy | $[0,1]$ |
| $t_{fit}$ | `t fit` | training criterion을 처음 넘는 step | nonnegative integer |
| $t_{gen}$ | `t gen` | generalization criterion을 처음 넘는 step | nonnegative integer |
| transition width | `transition width` | 낮은 threshold에서 높은 threshold까지의 step 차이 | nonnegative scalar |

## 1. Delayed generalization

threshold $\tau_{fit},\tau_{gen}$을 정하고

$$
t_{fit}=\min\{t:A_{train}(t)\ge\tau_{fit}\},\qquad
t_{gen}=\min\{t:A_{test}(t)\ge\tau_{gen}\}
$$

로 정의한다. $t_{gen}\gg t_{fit}$이면 training fit 뒤 generalization이 지연됐다고 기술할 수 있다. threshold는 사전에 정하거나 sensitivity analysis를 한다.

## 2. 급격함을 측정한다

test accuracy가 0.2에서 0.8로 오르는 step 폭, local slope와 sigmoid fit 등을 사용할 수 있다. checkpoint 간격이 transition 폭보다 넓으면 실제 급격함을 식별할 수 없다.

linear 축과 log step 축은 같은 데이터를 다르게 보이게 한다. raw step 표와 평가 빈도를 함께 제공한다.

## 3. Phase transition이라는 말의 범위

물리학의 phase transition은 system size limit과 order parameter 같은 엄밀한 구조를 가진다. 기계학습 논문에서는 급격한 경험적 변화라는 느슨한 뜻으로도 쓴다. 이 교재에서는 “관측 지표의 급격한 전환”과 “이론적 phase transition”을 구분한다.

## 4. CPU 실습

<!-- I08_EXAMPLE: i08_10_grokking_transition -->

synthetic trace에서 training accuracy는 step 200에 0.99를 넘지만 test accuracy는 step 1600에 0.9를 넘는다. 1400-step 지연은 정의한 threshold와 grid에 대한 결과이다.

## 흔한 오해

### 오해 1. test curve가 늦게 오르면 내부 알고리즘이 갑자기 생겼다

행동 curve만으로 내부 mechanism을 알 수 없다. representation과 intervention 지표를 함께 추적해야 한다.

### 오해 2. 한 seed의 곡선이면 현상이 확정된다

transition 위치와 발생 여부가 initialization, data split과 regularization에 의존할 수 있다.

## 연습문제

### 1. 지연 계산

$t_{fit}=500$, $t_{gen}=4500$이면 delay는 얼마인가?

<details><summary>해설 보기</summary>

$4500-500=4000$ step이다.

</details>

### 2. transition 폭

test accuracy가 step 1000에 0.2, step 1400에 0.8을 넘었다. threshold 기반 폭은 얼마인가?

<details><summary>해설 보기</summary>

400 step이다. 실제 crossing은 관측 간격 안에 있으므로 이 값도 grid 근사이다.

</details>

### 3. log axis

log step 축을 사용할 때 raw step도 제공해야 하는 이유는 무엇인가?

<details><summary>해설 보기</summary>

시각적 거리가 변형되므로 독자가 실제 학습 예산과 transition 간격을 확인할 수 있어야 한다.

</details>

### 4. 내부 증거

grokking 시점의 mechanism 변화를 조사하려면 어떤 추가 측정을 할 수 있는가?

<details><summary>해설 보기</summary>

고정 probe, representation alignment, feature activation과 ablation effect를 checkpoint마다 함께 잰다.

</details>

### 5. 재현성

transition이 5개 seed 중 2개에서만 나타났다. 무엇을 보고해야 하는가?

<details><summary>해설 보기</summary>

발생 비율, 각 seed의 곡선과 transition 위치 분포를 모두 보고한다. 평균 곡선만으로 숨기지 않는다.

</details>

### 6. 주장 비판

“정확도가 두 checkpoint 사이에 0.2에서 0.9로 올라 phase transition이 증명됐다”를 비판하라.

<details><summary>해설 보기</summary>

중간 관측이 없어 전환 폭을 알 수 없고 이론적 phase transition 조건도 제시되지 않았다. 관측상 큰 변화라고만 말할 수 있다.

</details>

## 근거와 갱신 경계

작은 알고리즘 데이터에서 delayed generalization을 보고한 원 연구는 [Power et al. (2022)](https://arxiv.org/abs/2201.02177)이다. task·dataset size·regularization에 따라 현상이 달라질 수 있으므로 일반 언어모델의 필수 단계로 취급하지 않는다.

## 단원 요약

- grokking은 training fit 뒤 지연된 test generalization으로 측정할 수 있다.
- transition 위치와 폭은 threshold와 grid에 의존한다.
- 행동 급상승은 내부 mechanism 급변의 직접 증거가 아니다.
- 여러 seed와 더 촘촘한 관측으로 재현성을 평가한다.

## 통과 기준

- delayed generalization과 transition 폭을 계산할 수 있는가?
- sparse checkpoint의 한계를 지적할 수 있는가?
- 경험적 전환과 이론적 phase transition을 구분할 수 있는가?

## 다음 단원

- [I08-11 seed와 데이터 순서](I08-11-seed-data-order.md)

## 집필자 점검표

- [x] grokking의 측정 정의를 제시했다.
- [x] 급격함과 phase transition 주장을 제한했다.
- [x] 모든 문제에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 주장 강도와 읽기 표기를 확인했다.
- [x] 내부 링크와 수식을 확인했다.
