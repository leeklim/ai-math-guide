---
id: "I08-09"
title: "feature emergence"
part: 3
stage: "I08"
status: "완료"
prerequisites: ["I08-08", "I08-03", "I07-12"]
estimated_time: "100~130분"
---

# I08-09. feature emergence

## 이 단원이 필요한 이유

feature가 “나타났다”는 말에는 여러 사건이 섞인다. activation geometry에서 방향이 생기는 시점, label을 복원할 수 있는 시점, 모델이 그 방향을 기능적으로 사용하는 시점과 행동 성능이 바뀌는 시점은 같지 않을 수 있다. 시간축 분석은 이 네 주장을 분리해야 한다.

## 학습 목표

- formation·recoverability·use·behavior를 별도 지표로 정의할 수 있다.
- checkpoint 사이 feature matching의 조건을 설명할 수 있다.
- threshold crossing과 uncertainty를 함께 보고할 수 있다.
- sparse 관측으로 순간적인 emergence를 단정하지 않을 수 있다.

## 선수지식 확인

- 선수 단원: [I08-08 influence function](I08-08-influence-function.md), [I08-03 representation alignment](I08-03-representation-alignment.md), [I07-12 necessity와 sufficiency](../I07/I07-12-necessity-sufficiency.md)
- 확인 질문: probe가 label을 복원한다는 결과가 모델의 정보 사용을 뜻하지 않는 이유는 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $F_t$ | `F sub t` | checkpoint $t$의 feature formation 지표 | scalar |
| $R_t$ | `R sub t` | held-out recoverability | $[0,1]$ 또는 score |
| $U_t$ | `U sub t` | intervention으로 잰 사용 효과 | signed scalar |
| $B_t$ | `B sub t` | 외부 행동 지표 | task-dependent |
| $\tau_R$ | `tau sub R` | recoverability threshold | scalar |

## 1. 네 사건을 분리한다

한 feature의 시간축 표를 다음처럼 설계한다.

| 질문 | 가능한 측정 | 허용되는 주장 |
|---|---|---|
| 형성됐는가 | variance, cluster separation, matched direction stability | 내부 구조가 관찰됐다 |
| 복원되는가 | held-out probe·decoder score | 정보가 읽힌다 |
| 사용되는가 | ablation·patching effect와 control | 정의한 행동에 기능적으로 관여한다 |
| 행동이 바뀌는가 | task accuracy, logit margin, calibration | 외부 metric이 변했다 |

한 열의 상승을 다른 열의 상승으로 대체하지 않는다.

## 2. 같은 feature를 추적하는 문제

좌표별 neuron ID는 checkpoint 사이 의미를 보장하지 않는다. activation profile, direction cosine, decoder vector와 maximal examples를 이용해 matching하고, one-to-one assignment 여부와 matching score를 기록한다. 낮은 score에서는 “같은 feature” 대신 “가장 가까운 후보”라고 쓴다.

## 3. Emergence time은 규칙에 의존한다

예를 들어

$$
t_R=\min\{t:R_t\ge\tau_R\}
$$

로 recoverability emergence를 정의할 수 있다. threshold, smoothing과 checkpoint grid를 바꾸면 $t_R$도 바뀐다. bootstrap interval이나 여러 seed의 crossing 분포를 함께 본다.

## 4. CPU 실습

<!-- I08_EXAMPLE: i08_09_feature_emergence -->

synthetic trajectory에서 recoverability는 checkpoint 3, intervention use와 행동은 checkpoint 4에 threshold를 넘는다. 같은 feature의 여러 증거가 다른 시점에 나타날 수 있음을 보인다.

## 흔한 오해

### 오해 1. probe accuracy가 chance를 넘은 순간 feature가 탄생했다

probe capacity, 표본 크기와 threshold에 의존한다. 약한 구조가 이전부터 있었을 수도 있다.

### 오해 2. 한 seed의 급상승이 보편적 phase transition이다

다른 seed와 더 촘촘한 checkpoint에서 위치와 폭을 확인해야 한다.

## 연습문제

### 1. 주장 분류

held-out linear probe accuracy가 0.9이다. 네 열 중 어느 증거인가?

<details><summary>해설 보기</summary>

recoverability 증거이다. 사용이나 행동 변화는 별도로 재야 한다.

</details>

### 2. 사용 증거

feature 방향 ablation이 target logit을 낮추고 random-direction control은 거의 변하지 않았다. 어떤 열의 증거인가?

<details><summary>해설 보기</summary>

정의한 개입과 행동에 대한 use 증거이다. off-manifold 여부와 반복 단위도 확인한다.

</details>

### 3. threshold

$R=(0.5,0.7,0.85)$이고 $\tau_R=0.8$이면 첫 crossing index는 얼마인가?

<details><summary>해설 보기</summary>

0-based index 2이다. 실제 step을 보고할 때는 해당 checkpoint step으로 바꾼다.

</details>

### 4. matching

checkpoint마다 neuron 번호가 같은 것만으로 feature identity를 주장할 수 없는 이유는 무엇인가?

<details><summary>해설 보기</summary>

unit의 기능과 activation profile이 학습 중 바뀔 수 있으며 permutation·superposition도 있기 때문이다.

</details>

### 5. 시간 해상도

step 10000과 50000 사이에서 score가 상승했다. emergence step을 50000이라고 단정할 수 있는가?

<details><summary>해설 보기</summary>

관측상 첫 crossing일 뿐 실제 변화는 두 checkpoint 사이 어느 때든 일어났을 수 있다.

</details>

### 6. 종합 해석

recoverability는 높지만 ablation effect가 0에 가깝다. 가장 보수적인 결론은 무엇인가?

<details><summary>해설 보기</summary>

정보는 지정 probe로 복원되지만 정의한 개입과 행동에서는 사용 증거가 관찰되지 않았다고 쓴다.

</details>

## 근거와 갱신 경계

Pythia가 checkpoint를 이용한 학습 동역학 연구를 가능하게 한 설계는 [Biderman et al. (2023)](https://proceedings.mlr.press/v202/biderman23a.html)을 기준으로 한다. feature emergence의 보편적 순서를 가정하지 않으며, 실제 feature identity는 측정법마다 다시 검증해야 한다.

## 단원 요약

- formation, recoverability, use와 behavior는 다른 사건이다.
- feature matching에는 좌표 ID보다 activation·direction 근거가 필요하다.
- emergence time은 threshold와 checkpoint grid에 의존한다.
- 여러 seed와 개입 control 없이 급격한 탄생을 단정하지 않는다.

## 통과 기준

- 네 종류의 증거를 별도 열로 설계할 수 있는가?
- feature matching 불확실성을 보고할 수 있는가?
- threshold crossing의 시간 해상도 한계를 설명할 수 있는가?

## 다음 단원

- [I08-10 grokking과 phase transition](I08-10-grokking-phase-transition.md)

## 집필자 점검표

- [x] feature의 네 사건을 구분했다.
- [x] matching과 threshold 의존성을 명시했다.
- [x] 모든 문제에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 주장 강도와 읽기 표기를 확인했다.
- [x] 내부 링크와 수식을 확인했다.
