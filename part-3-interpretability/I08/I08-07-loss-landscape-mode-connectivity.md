---
id: "I08-07"
title: "loss landscape와 mode connectivity"
part: 3
stage: "I08"
status: "완료"
prerequisites: ["I08-06", "M01-11"]
estimated_time: "90~120분"
---

# I08-07. loss landscape와 mode connectivity

## 이 단원이 필요한 이유

두 checkpoint의 loss가 낮아도 그 사이가 낮은지는 별도 질문이다. 직선 보간의 barrier와 최적화된 곡선 경로는 서로 다른 증거를 준다. loss landscape 시각화는 고차원 함수를 선택한 저차원 단면으로 보는 것이므로 전체 지형으로 해석하면 안 된다.

## 학습 목표

- parameter path 위의 loss profile을 정의할 수 있다.
- straight interpolation barrier를 계산할 수 있다.
- low-loss curve와 실제 학습 궤적을 구분할 수 있다.
- 좌표와 normalization이 landscape 그림에 미치는 영향을 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [I08-06 Hessian spectrum](I08-06-hessian-spectrum.md), [M01-11 방향미분과 gradient](../../part-1-foundations/M01/M01-11-directional-derivative-gradient.md)
- 확인 질문: 국소 Hessian 정보만으로 먼 두 minima 사이의 loss를 알 수 없는 이유는 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\gamma(\alpha)$ | `gamma of alpha` | 두 지점을 잇는 parameter path | $[0,1]\to\mathbb R^p$ |
| $\gamma_{\mathrm{lin}}(\alpha)$ | `gamma lin of alpha` | straight interpolation | $\mathbb R^p$ |
| $B(\gamma)$ | `B of gamma` | endpoint 대비 최대 loss barrier | nonnegative scalar |
| mode connectivity | `mode connectivity` | 낮은 loss 경로로 해들이 연결되는 현상 | path property |
| basin | `basin` | 선택한 optimization·좌표에서 낮은 loss 주변 영역 | informal region |

## 1. 경로를 먼저 정한다

두 파라미터 $\theta_a,\theta_b$의 직선 경로는

$$
\gamma_{\mathrm{lin}}(\alpha)=(1-\alpha)\theta_a+\alpha\theta_b,
\qquad 0\le\alpha\le1
$$

이다. barrier를

$$
B(\gamma)=\max_\alpha L(\gamma(\alpha))-
\max\{L(\theta_a),L(\theta_b)\}
$$

로 정의할 수 있다. 평가 데이터와 $\alpha$ grid를 고정해야 값이 재현된다.

## 2. 직선 실패는 연결 실패가 아니다

직선에 높은 barrier가 있어도 굽은 low-loss path가 존재할 수 있다. 반대로 선택한 곡선 하나가 낮다고 모든 점이나 모든 모델이 연결된다는 뜻은 아니다. mode connectivity는 경로 존재에 관한 주장이다.

## 3. 대칭과 정렬

hidden-unit permutation을 정렬하지 않으면 기능적으로 같은 두 모델의 직선 중간이 unit을 섞어 높은 loss를 낼 수 있다. 따라서 connectivity 비교 전에 가능한 symmetry alignment를 기록한다.

loss 단면 그림도 방향 vector의 scale과 filter normalization에 따라 모양이 바뀐다. 그림은 정의한 slice의 측정 결과이다.

## 4. CPU 실습

<!-- I08_EXAMPLE: i08_07_loss_path -->

$L(x,y)=(x^2+y^2-1)^2$의 원 위 두 점을 잇는다. 원점을 지나는 직선은 barrier가 있지만 반원 경로는 loss 0을 유지한다.

## 흔한 오해

### 오해 1. low-loss path가 실제 학습 경로다

연결 경로는 사후에 찾은 존재 증거일 수 있다. optimizer가 그 길을 지나갔다는 증거는 저장된 trajectory가 따로 필요하다.

### 오해 2. 2D contour가 전체 landscape다

고차원 공간에서 선택한 두 방향의 단면일 뿐이다. 다른 방향의 barrier와 flatness는 보이지 않는다.

## 연습문제

### 1. 중점

$\theta_a=0$, $\theta_b=2$인 1차원 직선 경로의 $\alpha=0.25$ 지점은 얼마인가?

<details><summary>해설 보기</summary>

$(1-0.25)0+0.25\times2=0.5$이다.

</details>

### 2. barrier

endpoint loss가 둘 다 0.1이고 경로 최대 loss가 0.7이면 barrier는 얼마인가?

<details><summary>해설 보기</summary>

$0.7-0.1=0.6$이다.

</details>

### 3. grid 오차

$\alpha$를 0, 0.5, 1에서만 평가하면 어떤 문제가 생길 수 있는가?

<details><summary>해설 보기</summary>

그 사이의 좁은 높은 barrier를 놓쳐 최대 loss를 과소평가할 수 있다.

</details>

### 4. 대칭

permutation alignment가 직선 barrier를 낮출 수 있는 이유를 설명하라.

<details><summary>해설 보기</summary>

같은 역할의 unit끼리 대응시켜 중간 weight가 서로 다른 기능을 부정확하게 섞는 일을 줄이기 때문이다.

</details>

### 5. 존재와 경로

낮은 곡선 하나를 찾으면 SGD가 그 경로를 지났다고 결론낼 수 있는가?

<details><summary>해설 보기</summary>

결론낼 수 없다. 실제 update와 checkpoint를 추적해야 한다.

</details>

### 6. 데이터 의존성

train loss 경로가 낮아도 test loss 경로를 별도로 재야 하는 이유는 무엇인가?

<details><summary>해설 보기</summary>

train objective가 같아도 일반화 행동은 경로에서 달라질 수 있다. 두 metric의 estimand가 다르다.

</details>

## 근거와 갱신 경계

mode connectivity의 기계론적 분석은 [Lubana et al. (2023)](https://proceedings.mlr.press/v202/lubana23a.html)을 참고한다. 이 단원은 curve optimization algorithm을 구현하지 않고 경로별 주장 차이를 다룬다.

## 단원 요약

- loss profile은 선택한 parameter path와 데이터에 의존한다.
- 직선 barrier가 곡선 경로의 부재를 뜻하지 않는다.
- low-loss path는 실제 optimizer trajectory가 아니다.
- symmetry alignment와 grid 해상도를 기록한다.

## 통과 기준

- path와 barrier를 정의하고 계산할 수 있는가?
- 직선 보간과 mode connectivity를 구분할 수 있는가?
- landscape slice의 한계를 설명할 수 있는가?

## 다음 단원

- [I08-08 influence function](I08-08-influence-function.md)

## 집필자 점검표

- [x] 경로와 barrier를 정의했다.
- [x] 실제 trajectory와 사후 경로를 구분했다.
- [x] 모든 문제에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 주장 강도와 읽기 표기를 확인했다.
- [x] 내부 링크와 수식을 확인했다.
