---
id: "I08-06"
title: "Hessian spectrum"
part: 3
stage: "I08"
status: "완료"
prerequisites: ["I08-05", "M03-12", "M02-11"]
estimated_time: "100~130분"
---

# I08-06. Hessian spectrum

## 이 단원이 필요한 이유

gradient는 현재 기울기를 주지만 방향별 gradient 변화는 말하지 않는다. Hessian eigenvalue는 선택한 파라미터화와 지점에서 loss의 국소 곡률을 요약한다. 큰 모델에서는 Hessian 전체를 만들지 않고 Hessian-vector product로 일부 spectrum을 근사한다.

## 학습 목표

- Hessian과 방향 이차미분의 관계를 설명할 수 있다.
- eigenvalue 부호를 국소 곡률로 해석할 수 있다.
- Hessian-vector product를 전체 행렬 구성과 구분할 수 있다.
- sharpness와 generalization을 곧바로 동일시하지 않을 수 있다.

## 선수지식 확인

- 선수 단원: [I08-05 mini-batch noise와 optimizer state](I08-05-minibatch-noise-optimizer-state.md), [M03-12 Hessian](../../part-1-foundations/M03/M03-12-hessian.md), [M02-11 고유값과 고유벡터](../../part-1-foundations/M02/M02-11-eigenvalues-eigenvectors.md)
- 확인 질문: symmetric matrix의 eigenvalue와 Rayleigh quotient는 어떻게 연결되는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $H(\theta)=\nabla^2L(\theta)$ | `H of theta equals the Hessian of L at theta` | loss Hessian | $p\times p$ |
| $v^\top Hv$ | `v transpose H v` | $v$ 방향의 이차 곡률 | scalar |
| $Hv$ | `H v` | Hessian-vector product | $\mathbb R^p$ |
| $\lambda_{\max}$ | `lambda max` | 최대 eigenvalue | scalar |
| spectrum | `spectrum` | eigenvalue의 multiset | $p$ real values for symmetric $H$ |

## 1. 국소 이차 근사

작은 $\delta$에 대해

$$
L(\theta+\delta)\approx L(\theta)
+\nabla L(\theta)^\top\delta
+\frac12\delta^\top H(\theta)\delta.
$$

stationary point에서는 선형항이 사라진다. 양의 eigenvalue 방향은 국소적으로 위로 굽고, 음의 eigenvalue 방향은 loss를 낮출 수 있는 곡률 방향이다.

## 2. Spectrum이 주는 정보

$\lambda_{\max}$는 가장 큰 양의 곡률을 나타내며 gradient descent의 안정 step과 관련된다. 0에 가까운 eigenvalue가 많으면 국소적으로 평평한 방향이 많다는 뜻이다. 그러나 scale symmetry와 parameterization이 eigenvalue를 바꾸므로 모델 간 raw sharpness 비교는 조심해야 한다.

## 3. 전체 Hessian을 만들지 않는다

$p$가 크면 $p^2$개 원소를 저장할 수 없다. automatic differentiation으로 $Hv$를 계산하고 power iteration이나 Lanczos를 사용해 극단 eigenvalue와 density를 근사한다. 근사에는 iteration 수, tolerance, probe vector seed를 기록한다.

## 4. CPU 실습

<!-- I08_EXAMPLE: i08_06_hessian_spectrum -->

대각 Hessian $\operatorname{diag}(4,1,-0.5)$의 spectrum과 한 vector의 $Hv$, Rayleigh quotient를 계산한다. 음의 eigenvalue는 이 점이 모든 방향의 local minimum이 아님을 보인다.

## 흔한 오해

### 오해 1. 큰 eigenvalue면 반드시 일반화가 나쁘다

parameterization, scale과 측정 loss에 따라 sharpness가 달라진다. 일반화는 독립 test metric으로 측정해야 한다.

### 오해 2. Hessian spectrum이 전역 loss landscape다

Hessian은 한 점의 국소 이차 정보다. 먼 지점과 다른 basin의 구조는 직접 말하지 않는다.

## 연습문제

### 1. 방향 곡률

$H=\operatorname{diag}(3,-1)$, $v=(0,1)$일 때 $v^\top Hv$를 구하라.

<details><summary>해설 보기</summary>

$-1$이다. 두 번째 좌표 방향에는 음의 곡률이 있다.

</details>

### 2. shape

$\theta\in\mathbb R^p$일 때 $H$, $v$, $Hv$의 shape을 적어라.

<details><summary>해설 보기</summary>

$H$는 $p\times p$, $v$와 $Hv$는 길이 $p$ vector이다.

</details>

### 3. stationary point

gradient가 0이고 Hessian에 음의 eigenvalue가 있으면 strict local minimum인가?

<details><summary>해설 보기</summary>

아니다. 음의 곡률 방향으로 작은 이동을 하면 이차항이 loss를 낮춘다.

</details>

### 4. HVP

HVP가 전체 Hessian보다 메모리를 덜 쓰는 이유는 무엇인가?

<details><summary>해설 보기</summary>

$p^2$ 원소를 저장하지 않고 주어진 vector에 대한 곱 $p$개만 계산·보관하기 때문이다.

</details>

### 5. 최대 eigenvalue

power iteration이 주로 찾는 것은 무엇인가?

<details><summary>해설 보기</summary>

절댓값이 가장 큰 dominant eigenvalue와 그 eigenvector 방향이다. 조건에 따라 부호 해석을 함께 확인해야 한다.

</details>

### 6. 주장 비판

“checkpoint $t$의 $\lambda_{\max}$가 작으므로 더 잘 일반화한다”를 비판하라.

<details><summary>해설 보기</summary>

국소 곡률 하나와 일반화 사이에는 자동적인 함의가 없다. 같은 parameterization인지 확인하고 독립 test 성능을 측정해야 한다.

</details>

## 근거와 갱신 경계

신경망 학습 중 Hessian eigenvalue density의 수치 추정은 [Ghorbani, Krishnan and Xiao (2019)](https://proceedings.mlr.press/v97/ghorbani19b.html)을 기준으로 한다. 이 단원의 CPU 예제는 exact diagonal Hessian이며 대규모 spectrum 근사 정확도를 재현하지 않는다.

## 단원 요약

- Hessian은 loss의 국소 이차 변화를 나타낸다.
- eigenvalue 부호와 크기는 방향별 곡률을 준다.
- 큰 모델에서는 HVP로 spectrum 일부를 근사한다.
- sharpness와 일반화는 별도 지표로 검증한다.

## 통과 기준

- 이차 근사와 방향 곡률을 설명할 수 있는가?
- 작은 Hessian의 eigenvalue를 해석할 수 있는가?
- HVP 근사의 기록 항목과 주장 한계를 말할 수 있는가?

## 다음 단원

- [I08-07 loss landscape와 mode connectivity](I08-07-loss-landscape-mode-connectivity.md)

## 집필자 점검표

- [x] 국소 곡률과 전역 landscape를 구분했다.
- [x] HVP와 spectrum 근사를 설명했다.
- [x] 모든 문제에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 주장 강도와 읽기 표기를 확인했다.
- [x] 내부 링크와 수식을 확인했다.
