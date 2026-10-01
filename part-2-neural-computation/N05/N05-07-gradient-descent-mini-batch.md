---
id: "N05-07"
title: "gradient descent와 mini-batch"
part: 2
stage: "N05"
status: "완료"
prerequisites:
  - "N05-06"
  - "M04-06"
estimated_time: "120~150분"
---

# N05-07. gradient descent와 mini-batch

## 이 단원이 필요한 이유

backpropagation은 현재 parameter에서 loss gradient를 계산한다. 학습은 그 gradient로 parameter를 갱신하고 새 batch에서 계산을 반복한다. 전체 dataset 대신 일부 sample을 고르면 계산량이 줄지만 update마다 다른 gradient를 얻는다.

이 단원은 sample 두 개의 mean squared error를 계산한다. per-sample gradient의 평균이 mini-batch gradient와 같음을 확인하고 gradient descent step 하나를 적용한다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- empirical risk와 mini-batch loss를 식으로 구분할 수 있다.
- mean reduction에서 batch gradient를 계산할 수 있다.
- learning rate를 적용해 parameter를 한 step 갱신할 수 있다.
- sum과 mean reduction이 gradient scale에 미치는 영향을 설명할 수 있다.
- batch sampling, seed와 data order를 재현성 기록에 포함할 수 있다.

## 선수지식 확인

- 선수 단원: [N05-06 backpropagation](N05-06-backpropagation.md)
- 선수 단원: [M04-06 표본, 모집단과 표본분포](../../part-1-foundations/M04/M04-06-samples-populations-sampling-distributions.md)
- 확인 질문: scalar loss의 parameter gradient를 계산할 수 있는가?
- 확인 질문: sample 값의 산술평균을 구할 수 있는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\theta$ | `theta` | 학습할 parameter vector | $\mathbb R^P$ |
| $\ell_i(\theta)$ | `ell sub i of theta` | sample $i$의 loss | $[0,\infty)$ |
| $\mathcal B_t$ | `script B sub t` | step $t$에서 선택한 mini-batch index 집합 | $\lvert\mathcal B_t\rvert=B$ |
| $L_{\mathcal B_t}$ | `L sub script B sub t` | mini-batch mean loss | scalar |
| $\eta$ | `eta` | learning rate | $\eta>0$ |
| $g_t$ | `g sub t` | step $t$의 mini-batch gradient | $\mathbb R^P$ |

## 핵심 개념 1. 전체 평균과 mini-batch 평균

$N$개 sample의 empirical risk는

\[
L(\theta)=\frac{1}{N}\sum_{i=1}^{N}\ell_i(\theta)
\]

이다. step $t$에서 $B$개 index만 선택하면

\[
L_{\mathcal B_t}(\theta)
=\frac{1}{B}\sum_{i\in\mathcal B_t}\ell_i(\theta)
\]

를 계산한다. mini-batch gradient는

\[
g_t=\nabla_\theta L_{\mathcal B_t}(\theta_t)
=\frac{1}{B}\sum_{i\in\mathcal B_t}\nabla_\theta\ell_i(\theta_t)
\]

이다. 미분의 선형성 때문에 mean loss의 gradient는 per-sample gradient의 평균과 같다.

## 핵심 개념 2. gradient descent update

가장 단순한 update는

\[
\theta_{t+1}=\theta_t-\eta g_t
\]

이다. gradient는 loss가 증가하는 방향이므로 음의 방향으로 이동한다. learning rate $\eta$는 이동 크기를 조절한다.

한 batch에서 loss가 줄었다고 전체 dataset의 loss도 줄었다고 보장할 수 없다. gradient는 현재 parameter와 선택한 batch에서 계산됐고, 큰 step에서는 일차 근사가 맞지 않을 수 있다.

## 핵심 개념 3. mean과 sum reduction

mean 대신 sample loss를 합치면

\[
L^{\mathrm{sum}}_{\mathcal B_t}
=\sum_{i\in\mathcal B_t}\ell_i,
\qquad
\nabla L^{\mathrm{sum}}_{\mathcal B_t}=B g_t
\]

이다. 같은 learning rate를 사용하면 batch size가 update scale에 직접 들어간다. 실험을 재현할 때 loss definition과 reduction을 함께 기록해야 한다.

## 예제 1. 두 sample의 gradient

### 문제

모형 $\hat y=wx+b$에서 $(x,y)=(1,3),(2,5)$를 mini-batch로 사용한다. 초기값은 $w=b=0$이고 loss는 squared error의 평균이다. loss와 gradient를 계산하라.

### 풀이

초기 prediction은 $(0,0)$이고 residual은 $(-3,-5)$이다.

\[
L=\frac{(-3)^2+(-5)^2}{2}=17
\]

sample별 $w$ gradient는 $2(\hat y-y)x$이므로 $(-6,-20)$이다. $b$ gradient는 $2(\hat y-y)$이므로 $(-6,-10)$이다. 평균을 내면

\[
\frac{\partial L}{\partial w}=-13,
\qquad
\frac{\partial L}{\partial b}=-8
\]

이다.

## 예제 2. 한 step update

$\eta=0.1$이면

\[
w_1=0-0.1(-13)=1.3,
\qquad
b_1=0-0.1(-8)=0.8
\]

이다. 새 prediction은 $(2.1,3.4)$이고 같은 batch의 새 loss는

\[
\frac{(2.1-3)^2+(3.4-5)^2}{2}=1.685
\]

이다. 이 step에서는 batch loss가 17에서 1.685로 줄었다.

## 실행 실습

### 실행 환경과 원본

- 환경: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- 확인일: 2026-10-01
- 구성요소 등급: `Stable core`
- 예제 ID: `n05_07_minibatch_gradient_descent`
- 코드 원본: `labs/N05/n05_07_minibatch_gradient_descent.py`
- 테스트: `tests/N05/test_n05_07.py`
- 실행 명령: `.venv\Scripts\python.exe -m labs.N05.n05_07_minibatch_gradient_descent`

### 자원 예산

예제는 batch 2, scalar input, parameter 2개와 update 1회를 사용한다. hard timeout은 10초다.

### 실제 코드와 실행 결과

site build는 아래 위치에 원본 코드와 실제 실행 결과를 삽입한다.

<!-- N05_EXAMPLE: n05_07_minibatch_gradient_descent -->

### 수치와 gradient 검사

테스트는 per-sample gradient의 평균과 autograd가 계산한 batch gradient를 비교한다. update 뒤 $w=1.3$, $b=0.8$과 loss 1.685도 손계산 값에 대조한다.

## sampling과 재현성

mini-batch gradient를 전체 gradient의 estimate로 해석하려면 sampling scheme을 명시해야 한다. uniform sampling에서는 조건에 따라 기대 mini-batch gradient가 full-data gradient와 일치한다. class-balanced sampling, sequence packing과 중복 sample은 다른 estimand를 만들 수 있다.

seed만 기록해도 충분하지 않다. dataset version, sample order, sampler 설정, batch size와 reduction을 함께 저장해야 같은 update sequence를 재생할 수 있다.

## 모델 해석과의 연결

per-example gradient는 어떤 training example이 현재 parameter update에 기여하는지 분석하는 재료다. gradient similarity나 influence 근사는 parameter 위치, loss definition과 checkpoint에 의존한다.

한 batch에서 큰 gradient를 낸 sample을 전체 학습의 원인으로 부를 수 없다. 여러 step의 sampling과 optimizer state가 실제 trajectory를 결정한다.

## 흔한 오해

### 오해 1. mini-batch gradient는 full gradient와 같다

특정 batch의 gradient는 full gradient의 estimate다. dataset 전체를 batch로 사용하거나 각 sample gradient가 우연히 같을 때만 값이 일치한다.

### 오해 2. batch size를 바꿔도 update가 같다

mean reduction은 직접적인 $B$ 배율을 제거하지만 gradient noise와 sample 구성이 달라진다. sum reduction은 gradient scale도 $B$에 따라 달라진다.

### 오해 3. 한 step에서 loss가 줄면 학습이 성공했다

현재 batch의 즉시 감소만 확인했다. 다른 batch, validation data와 후속 step의 안정성을 따로 검사해야 한다.

## 연습문제

### 1. mean gradient

두 sample의 scalar gradient가 4와 10이면 mean-reduced batch gradient는 얼마인가?

<details>
<summary>해설 보기</summary>

$(4+10)/2=7$이다.

</details>

### 2. sum reduction

앞 문제에서 sum-reduced gradient는 얼마인가?

<details>
<summary>해설 보기</summary>

$4+10=14$다. mean gradient의 batch size 2배다.

</details>

### 3. update 방향

$\theta=3$, $g=-4$, $\eta=0.2$일 때 다음 parameter를 구하라.

<details>
<summary>해설 보기</summary>

$\theta'=3-0.2(-4)=3.8$이다. 음의 gradient에서는 parameter가 증가한다.

</details>

### 4. batch size 1

$B=1$이면 mini-batch gradient는 무엇과 같은가?

<details>
<summary>해설 보기</summary>

선택한 sample 하나의 gradient와 같다. full-data gradient와 같다는 뜻은 아니다.

</details>

### 5. 재현성 기록

seed와 batch size만 기록한 학습을 정확히 재생할 수 없는 이유 두 가지를 적어라.

<details>
<summary>해설 보기</summary>

dataset version과 sample order 또는 sampler 구현이 다를 수 있다. loss reduction, preprocessing과 checkpoint 상태도 update를 바꾼다.

</details>

### 6. 주장 비판

한 sample의 gradient norm이 가장 크므로 최종 모델 행동을 그 sample이 만들었다는 결론을 평가하라.

<details>
<summary>해설 보기</summary>

한 checkpoint의 local gradient norm만으로 전체 training trajectory의 인과 기여를 정할 수 없다. sample이 선택된 step, 다른 gradient와 optimizer state, 후속 update를 함께 봐야 한다.

</details>

## 단원 요약

- mini-batch mean gradient는 batch 안 per-sample gradient의 평균이다.
- gradient descent는 negative gradient 방향으로 parameter를 갱신한다.
- sum과 mean reduction은 batch size에 따른 gradient scale이 다르다.
- batch loss의 한 step 감소는 전체 학습 성공을 보장하지 않는다.
- 재현에는 data order와 sampler를 포함한 update sequence 정보가 필요하다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- full-data loss와 mini-batch loss를 구분할 수 있는가?
- per-sample gradient에서 batch gradient를 계산할 수 있는가?
- learning rate를 적용해 update를 계산할 수 있는가?
- mean과 sum reduction의 차이를 설명할 수 있는가?
- mini-batch gradient에 근거한 주장의 범위를 제한할 수 있는가?

## 다음 단원

- [N05-08 momentum, AdamW와 optimizer state](N05-08-momentum-adamw-optimizer-state.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] full-data와 mini-batch loss를 구분했다.
- [x] mean과 sum reduction을 구분했다.
- [x] update 전후 수치와 gradient를 검산했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
- [x] Markdown에 실행 코드를 손으로 복제하지 않았다.
- [x] 코드 원본·테스트 경로·자원 예산·확인일을 기록했다.
- [x] shape·수치·gradient test가 있다.
