---
id: "I08-02"
title: "파라미터 거리와 함수 거리"
part: 3
stage: "I08"
status: "완료"
prerequisites: ["I08-01", "M02-15"]
estimated_time: "90~120분"
---

# I08-02. 파라미터 거리와 함수 거리

## 이 단원이 필요한 이유

checkpoint 사이 weight가 멀리 이동했다는 사실은 모델 행동이 크게 바뀌었다는 뜻이 아니다. hidden unit의 순열이나 scale 대칭은 같은 함수를 다른 파라미터로 표현한다. 반대로 작은 파라미터 이동도 민감한 입력에서는 큰 출력 차이를 만들 수 있다.

## 학습 목표

- 파라미터 거리와 함수 거리를 별도 estimand로 정의할 수 있다.
- hidden-unit permutation이 파라미터 거리를 바꾸는 예를 계산할 수 있다.
- 함수 거리가 입력분포에 의존함을 설명할 수 있다.
- weight 이동만으로 feature 학습을 주장하지 않을 수 있다.

## 선수지식 확인

- 선수 단원: [I08-01 checkpoint 연구 설계](I08-01-checkpoint-study-design.md), [M02-15 norm과 condition number](../../part-1-foundations/M02/M02-15-norm-condition-number.md)
- 확인 질문: 두 벡터의 Euclidean distance와 두 함수의 출력 차이는 왜 다른 종류의 객체인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $d_\theta(s,t)$ | `d theta of s comma t` | 두 checkpoint의 파라미터 거리 | nonnegative scalar |
| $d_f(s,t;P)$ | `d f of s comma t on P` | 분포 $P$에서의 함수 거리 | nonnegative scalar |
| $\|\theta_t-\theta_s\|_2$ | `the L two norm of theta sub t minus theta sub s` | 정렬 전 Euclidean weight 거리 | scalar |
| $P_X$ | `P sub X` | 함수를 비교할 입력분포 | probability distribution |
| symmetry | `symmetry` | 함수는 보존하지만 파라미터는 바꾸는 변환 | permutation·scaling 등 |

## 1. 두 거리를 따로 쓴다

가장 단순한 파라미터 거리는

$$
d_\theta(s,t)=\|\theta_t-\theta_s\|_2
$$

이다. 함수 거리는 예를 들어

$$
d_f^2(s,t;P_X)=\mathbb E_{x\sim P_X}
\left[\|f_{\theta_t}(x)-f_{\theta_s}(x)\|_2^2\right]
$$

로 정의한다. 두 번째 값에는 입력분포가 들어간다. 관측하지 않는 입력 영역의 차이는 표본 기반 추정에 나타나지 않는다.

## 2. 순열 대칭

한 hidden layer가

$$
f(x)=W_2\sigma(W_1x)
$$

일 때 permutation matrix $P$에 대해

$$
W_2P^{-1}\sigma(PW_1x)=W_2\sigma(W_1x)
$$

이다. unit 순서를 바꾸면 weight 배열은 달라지지만 함수는 같다. checkpoint 사이 raw weight 거리는 이 대칭을 제거하지 않는다.

## 3. 함수 거리도 질문에 맞춰야 한다

logit RMSE, KL divergence, accuracy disagreement와 생성 문자열 일치율은 서로 다른 행동을 잰다. probability의 KL은 방향과 support에 민감하며, accuracy는 logit 변화 대부분을 숨길 수 있다. 연구 질문에 앞서 metric을 고정한다.

## 4. CPU 실습

<!-- I08_EXAMPLE: i08_02_parameter_function_distance -->

두 hidden unit을 맞바꾼 ReLU network를 같은 입력 grid에서 평가한다. 파라미터 L2 거리는 양수지만 함수 RMSE는 0이다.

## 흔한 오해

### 오해 1. weight가 많이 움직인 layer가 많이 학습했다

optimizer scale, parameterization과 대칭이 거리에 들어간다. 행동·표현 지표와 함께 보지 않으면 무엇을 학습했는지 알 수 없다.

### 오해 2. 함수 거리는 하나로 정해진다

입력분포와 출력 metric을 바꾸면 함수 거리도 바뀐다. OOD 입력에서 가까운지 여부는 별도 질문이다.

## 연습문제

### 1. 계산

$\theta_s=(0,0)$, $\theta_t=(3,4)$일 때 파라미터 L2 거리를 구하라.

<details><summary>해설 보기</summary>

$\sqrt{3^2+4^2}=5$이다.

</details>

### 2. 입력분포

두 함수가 train support에서는 같고 그 밖에서는 다르다. train distribution으로 잰 함수 거리는 무엇을 놓치는가?

<details><summary>해설 보기</summary>

train support 밖의 행동 차이를 놓친다. 함수 거리는 전역 함수 동일성이 아니라 선택한 분포에서의 차이이다.

</details>

### 3. 순열

hidden unit 두 개를 바꿀 때 $W_1$과 $W_2$를 어떻게 함께 바꿔야 하는가?

<details><summary>해설 보기</summary>

$W_1$의 행을 permutation하고 $W_2$의 대응 열을 역 permutation한다. 그러면 중간 좌표 순서만 바뀌고 출력은 보존된다.

</details>

### 4. metric 선택

두 언어모델의 top-1 token은 같지만 logit이 다르다. accuracy disagreement는 얼마인가?

<details><summary>해설 보기</summary>

0이다. 이 metric은 confidence와 나머지 vocabulary 순위 변화를 보지 못한다.

</details>

### 5. 주장 비판

“$d_\theta$가 갑자기 커졌으므로 새 능력이 생겼다”를 비판하라.

<details><summary>해설 보기</summary>

파라미터 이동은 능력 지표가 아니다. 고정 행동 데이터에서 함수 변화와 task 성능을 따로 측정해야 한다.

</details>

### 6. 정규화

크기가 다른 두 모델의 raw L2 weight 거리를 직접 비교하기 어려운 이유는 무엇인가?

<details><summary>해설 보기</summary>

파라미터 수와 scale이 다르므로 합산 거리가 구조적으로 커질 수 있다. layer별 상대 변화나 함수 기반 metric이 필요하다.

</details>

## 근거와 갱신 경계

신경망 파라미터 공간의 대칭과 low-loss 연결은 [Lubana et al. (2023)](https://proceedings.mlr.press/v202/lubana23a.html)을 참고한다. 이 단원은 대칭을 완전히 quotient한 거리를 제안하지 않고, raw distance 해석의 한계를 다룬다.

## 단원 요약

- 파라미터 거리와 함수 거리는 서로 다른 estimand이다.
- 파라미터 대칭은 큰 weight 거리와 같은 함수를 함께 만들 수 있다.
- 함수 거리는 입력분포와 출력 metric에 의존한다.
- 학습 동역학 보고서에는 두 종류의 변화를 분리해 기록한다.

## 통과 기준

- 두 거리를 수식으로 따로 정의할 수 있는가?
- permutation 대칭 예를 설명할 수 있는가?
- weight 이동만으로 행동 변화를 주장하지 않을 수 있는가?

## 다음 단원

- [I08-03 representation alignment](I08-03-representation-alignment.md)

## 집필자 점검표

- [x] parameter와 function distance를 구분했다.
- [x] 대칭 예제를 계산했다.
- [x] 모든 문제에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 주장 강도와 선수지식을 확인했다.
- [x] 내부 링크와 수식을 확인했다.
