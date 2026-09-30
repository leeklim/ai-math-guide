---
id: "A09-DYN-06"
title: "확률미분방정식 입문"
part: 4
stage: "A09-DYN"
status: "완료"
prerequisites: ["A09-DYN-05", "M04-04"]
estimated_time: "90~120분"
---

# A09-DYN-06. 확률미분방정식 입문

## 이 단원이 필요한 이유

Brownian path는 보통의 의미로 미분할 수 없으므로 random forcing이 있는 dynamics는 ordinary derivative만으로 다룰 수 없다. stochastic differential equation은 drift와 diffusion을 infinitesimal increment의 규칙으로 정의한다.

## 학습 목표

- Itô SDE의 drift와 diffusion coefficient를 읽을 수 있다.
- Brownian increment의 scale을 설명할 수 있다.
- Itô formula의 quadratic variation term을 계산할 수 있다.
- Euler–Maruyama simulation과 연속 SDE를 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-DYN-05 Langevin dynamics](A09-DYN-05-langevin-dynamics.md), [M04-04 기댓값과 분산](../../part-1-foundations/M04/M04-04-expectation-variance-covariance.md)
- 확인 질문: variance가 시간에 비례하는 Gaussian increment의 표준편차는 어떤 scale인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $dX_t=b(X_t,t)dt+\sigma(X_t,t)dW_t$ | `d X t equals b of X t comma t d t plus sigma of X t comma t d W t` | Itô SDE | stochastic increment |
| $b$ | `b` | drift coefficient | vector |
| $\sigma$ | `sigma` | diffusion coefficient | matrix |
| $[W]_t=t$ | `the quadratic variation of W at t equals t` | Brownian quadratic variation | scalar |

## 핵심 개념

작은 $\Delta t$에서 Brownian increment는

$$
\Delta W\sim\mathcal N(0,\Delta t),
$$

이므로 magnitude가 $O(\!\sqrt{\Delta t})$이다. 그 제곱은 $O(\!\Delta t)$라 Taylor expansion에서 사라지지 않는다. scalar Itô formula는

$$
df(X_t)=f'(X_t)dX_t+\frac12f''(X_t)\sigma(X_t,t)^2dt
$$

이다. ordinary chain rule에 없는 두 번째 항이 quadratic variation의 효과다.

Euler–Maruyama는 $\Delta W_k=\sqrt h\,\xi_k$로 sampling해 SDE를 근사한다. seed와 step size를 바꾸면 한 path는 달라지며, weak·strong convergence는 서로 다른 정확도 질문이다.

## 작은 예제

$dX_t=\sigma dW_t$와 $f(x)=x^2$에 Itô formula를 적용하면 $d(X_t^2)=2X_t\sigma dW_t+\sigma^2dt$이다. 따라서 $E[X_t^2]$는 시간에 따라 $\sigma^2t$만큼 증가한다.

## 흔한 오해

- $dW_t/dt$를 보통의 finite random variable처럼 다루면 안 된다.
- SDE trajectory 하나가 distribution-level dynamics를 대표하지 않는다.

## 연습문제

### 1. increment scale
$\Delta t=0.04$일 때 표준 Brownian increment의 표준편차를 구하라.
<details><summary>해설 보기</summary>

$\sqrt{0.04}=0.2$이다.
</details>

### 2. Itô term
$dX_t=dW_t$, $f(x)=x^2$에서 $df$를 구하라.
<details><summary>해설 보기</summary>

$df=2X_t dW_t+dt$이다.
</details>

### 3. Euler–Maruyama
$dX=-Xdt+dW$, $X_0=1$, $h=0.01$, $\xi_0=0$이면 $X_1$은 얼마인가?
<details><summary>해설 보기</summary>

$X_1=1-0.01=0.99$이다.
</details>

### 4. 분석 단위
서로 다른 seed의 SDE path를 비교할 때 paired design이 가능한 경우를 설명하라.
<details><summary>해설 보기</summary>

두 조건에 같은 Brownian increment sequence를 사용하면 common-random-number pairing으로 dynamics 차이의 variance를 줄일 수 있다.
</details>

## 근거와 갱신 경계

Itô SDE·quadratic variation·Itô formula는 stochastic calculus의 표준 정의를 따른다. measure-theoretic construction과 Stratonovich integral은 다루지 않는다.

## 단원 요약

- Brownian increment의 크기는 $\sqrt{dt}$ scale이다.
- 그 제곱은 $dt$ scale이라 Itô correction을 만든다.
- Euler–Maruyama는 연속 SDE의 finite-step 근사다.
- path-level과 distribution-level 주장을 구분한다.

## 통과 기준

- Brownian increment와 Itô correction을 계산할 수 있는가?
- SDE simulation의 step·seed 의존성을 설명할 수 있는가?

## 다음 단원

- [A09-DYN-07 SGD의 연속시간 근사](A09-DYN-07-continuous-time-sgd.md)

## 집필자 점검표

- [x] Itô calculus가 ordinary calculus와 다른 지점을 밝혔다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
