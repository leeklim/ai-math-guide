---
id: "A09-DYN-01"
title: "미분방정식과 흐름"
part: 4
stage: "A09-DYN"
status: "완료"
prerequisites: ["M01-03", "M01-06", "M03-10"]
estimated_time: "90~120분"
---

# A09-DYN-01. 미분방정식과 흐름

## 이 단원이 필요한 이유

학습을 parameter update의 목록으로만 보면 시간에 따른 구조를 놓친다. ordinary differential equation은 현재 state가 순간 변화율을 정하는 계를 기술하고, flow는 초기조건 전체가 시간에 따라 이동하는 map을 뜻한다.

## 학습 목표

- autonomous ODE의 state와 vector field를 구분할 수 있다.
- solution trajectory와 flow map을 구분할 수 있다.
- Euler discretization을 gradient descent와 연결할 수 있다.
- 존재·유일성 가정이 필요한 이유를 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [M01-03 미분](../../part-1-foundations/M01/M01-03-derivative-instantaneous-rate.md), [M01-06 연쇄법칙](../../part-1-foundations/M01/M01-06-composition-chain-rule.md), [M03-10 total derivative](../../part-1-foundations/M03/M03-10-total-derivative-differential.md)
- 확인 질문: derivative가 현재 state의 함수라는 말은 무엇을 뜻하는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\dot x=f(x)$ | `x dot equals f of x` | autonomous ODE | $x\in\mathbb R^d$ |
| $x(t;x_0)$ | `x at time t given x naught` | 초기값 $x_0$의 trajectory | vector |
| $\Phi_t(x_0)$ | `Phi sub t of x naught` | time-$t$ flow map | state to state |
| $h$ | `h` | discretization step | positive scalar |

## 핵심 개념

autonomous ODE

$$
\dot x(t)=f(x(t)),\qquad x(0)=x_0
$$

에서 $f$는 각 state에 velocity를 배정하는 vector field이다. 한 초기값의 해는 trajectory이고, 모든 초기값을 time $t$ 뒤로 보내는 map은 $\Phi_t$이다. 해가 유일하면 $\Phi_{t+s}=\Phi_t\circ\Phi_s$가 성립한다.

Euler method는

$$
x_{k+1}=x_k+h f(x_k)
$$

로 연속 trajectory를 근사한다. $f(\theta)=-\nabla L(\theta)$이면 gradient descent와 같은 모양이지만, finite step은 연속 flow와 정확히 같지 않다.

## 작은 예제

$\dot x=-ax$, $a>0$의 해는 $x(t)=x_0e^{-at}$이다. flow는 $\Phi_t(x_0)=e^{-at}x_0$이며 모든 초기값을 0으로 수축시킨다.

## 흔한 오해

- vector field는 trajectory 하나가 아니라 가능한 모든 state의 velocity 규칙이다.
- 작은 learning rate라도 discrete optimizer와 ODE가 자동으로 같은 장기 거동을 갖는 것은 아니다.

## 연습문제

### 1. 해 확인
$x(t)=x_0e^{2t}$가 $\dot x=2x$를 만족하는지 확인하라.
<details><summary>해설 보기</summary>

$\dot x=2x_0e^{2t}=2x(t)$이고 $x(0)=x_0$이므로 만족한다.
</details>

### 2. flow 성질
$\Phi_t(x)=e^{-t}x$에서 $\Phi_t(\Phi_s(x))=\Phi_{t+s}(x)$임을 보이라.
<details><summary>해설 보기</summary>

$e^{-t}(e^{-s}x)=e^{-(t+s)}x$이다.
</details>

### 3. Euler step
$\dot x=-x$, $x_0=1$, $h=0.1$에서 첫 step을 구하라.
<details><summary>해설 보기</summary>

$x_1=1+0.1(-1)=0.9$이다.
</details>

### 4. 학습 해석
optimizer log를 ODE trajectory로 해석하기 전에 기록할 두 항목을 쓰라.
<details><summary>해설 보기</summary>

실제 step size schedule과 optimizer state·update rule을 기록해야 한다. stochastic gradient의 sampling 규칙도 필요하다.
</details>

## 근거와 갱신 경계

ODE·flow·Euler method는 dynamical systems의 표준 정의를 따른다. 이 단원은 Picard–Lindelöf theorem의 증명을 다루지 않는다.

## 단원 요약

- vector field는 state별 velocity를 정한다.
- trajectory는 한 초기값의 해이고 flow는 초기값 전체의 이동 map이다.
- Euler method는 ODE를 discrete update로 근사한다.
- optimizer와 연속시간 모델의 일치는 가정과 오차 분석이 필요하다.

## 통과 기준

- ODE·trajectory·flow를 구분할 수 있는가?
- Euler update를 계산하고 근사의 한계를 말할 수 있는가?

## 다음 단원

- [A09-DYN-02 fixed point와 선형 안정성](A09-DYN-02-fixed-points-linear-stability.md)

## 집필자 점검표

- [x] ODE와 flow의 타입을 구분했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
