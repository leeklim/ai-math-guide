---
id: "A09-DYN-03"
title: "phase portrait와 bifurcation"
part: 4
stage: "A09-DYN"
status: "완료"
prerequisites: ["A09-DYN-02"]
estimated_time: "90~120분"
---

# A09-DYN-03. phase portrait와 bifurcation

## 이 단원이 필요한 이유

한 trajectory만 보면 초기조건과 parameter가 달라질 때 가능한 거동을 알기 어렵다. phase portrait는 state space 전체의 흐름을 요약하고, bifurcation은 parameter 변화로 fixed point나 안정성이 질적으로 바뀌는 지점을 나타낸다.

## 학습 목표

- phase line·phase portrait를 그릴 수 있다.
- basin of attraction을 정의할 수 있다.
- saddle-node·pitchfork bifurcation의 간단한 normal form을 분석할 수 있다.
- 제한된 checkpoint 변화와 phase transition 주장을 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-DYN-02 fixed point와 선형 안정성](A09-DYN-02-fixed-points-linear-stability.md)
- 확인 질문: fixed point 하나의 안정성과 state space 전체의 거동은 왜 다른 정보인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\mu$ | `mu` | control parameter | scalar |
| $\mathcal B(x^*)$ | `the basin of x star` | $x^*$로 수렴하는 초기값 집합 | subset of state space |
| $\dot x=\mu-x^2$ | `x dot equals mu minus x squared` | saddle-node normal form | scalar ODE |
| $\dot x=\mu x-x^3$ | `x dot equals mu x minus x cubed` | supercritical pitchfork form | scalar ODE |

## 핵심 개념

phase portrait는 vector field의 방향, fixed point, invariant set과 representative trajectory를 함께 표시한다. attractor의 basin은 그 attractor로 수렴하는 초기조건 집합이다.

saddle-node normal form $\dot x=\mu-x^2$는 $\mu<0$에서 fixed point가 없고, $\mu=0$에서 하나가 합쳐지며, $\mu>0$에서 $x=\pm\sqrt\mu$ 두 개가 생긴다. pitchfork form $\dot x=\mu x-x^3$는 $\mu$가 0을 지나며 0의 안정성이 바뀌고 대칭인 두 stable branch가 생긴다.

bifurcation은 단순한 값의 급변이 아니라 parameter에 따른 invariant structure의 질적 변화다. finite training checkpoints에서 metric이 꺾였다는 사실만으로 이를 확정할 수 없다.

## 작은 예제

$\dot x=x(1-x)$에서는 0과 1이 fixed point이다. $0<x_0<1$이면 velocity가 양수이고 $x_0>1$이면 음수이므로 양의 초기값은 1로 수렴한다.

## 흔한 오해

- loss curve의 elbow는 자동으로 dynamical bifurcation이 아니다.
- 2차원 projection의 phase portrait는 원래 고차원 dynamics의 topology를 보존하지 않을 수 있다.

## 연습문제

### 1. phase line
$\dot x=x(1-x)$에서 $x<0$, $0<x<1$, $x>1$의 흐름 방향을 적어라.
<details><summary>해설 보기</summary>

각각 음수, 양수, 음수이므로 왼쪽, 오른쪽, 왼쪽 방향이다.
</details>

### 2. saddle-node
$\mu=4$일 때 $\dot x=\mu-x^2$의 fixed point와 안정성을 구하라.
<details><summary>해설 보기</summary>

$x=\pm2$이고 derivative $-2x$에 따라 $-2$는 불안정, $2$는 안정하다.
</details>

### 3. pitchfork
$\mu<0$에서 $\dot x=\mu x-x^3$의 실수 fixed point와 0의 안정성을 구하라.
<details><summary>해설 보기</summary>

fixed point는 0뿐이며 derivative가 $\mu<0$이므로 안정하다.
</details>

### 4. phase transition 주장
checkpoint 세 개의 probe score가 $0.5,0.5,0.9$이면 bifurcation 증거로 충분한가?
<details><summary>해설 보기</summary>

아니다. 측정 오차·checkpoint 해상도·control parameter와 invariant structure를 확인하지 못했으므로 관측된 급변으로만 보고한다.
</details>

## 근거와 갱신 경계

phase portrait와 normal form은 dynamical systems의 표준 예를 따른다. 고차원 bifurcation classification과 chaos는 다루지 않는다.

## 단원 요약

- phase portrait는 가능한 state-space 거동을 요약한다.
- basin은 같은 attractor로 가는 초기값 집합이다.
- bifurcation은 parameter에 따른 질적 구조 변화다.
- sparse checkpoint의 metric 급변은 bifurcation의 충분한 증거가 아니다.

## 통과 기준

- 1차원 phase line과 normal form을 분석할 수 있는가?
- 학습 metric의 급변과 dynamical bifurcation을 구분할 수 있는가?

## 다음 단원

- [A09-DYN-04 Markov process](A09-DYN-04-markov-process.md)

## 집필자 점검표

- [x] phase portrait와 bifurcation의 증거 수준을 구분했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
