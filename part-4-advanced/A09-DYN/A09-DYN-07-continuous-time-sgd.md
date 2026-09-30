---
id: "A09-DYN-07"
title: "SGD의 연속시간 근사"
part: 4
stage: "A09-DYN"
status: "완료"
prerequisites: ["A09-DYN-06", "I08-04", "I08-05"]
estimated_time: "90~120분"
---

# A09-DYN-07. SGD의 연속시간 근사

## 이 단원이 필요한 이유

SGD update를 ODE나 SDE로 근사하면 learning rate, batch noise와 loss geometry가 만드는 평균적 거동을 분석할 수 있다. 그러나 momentum, adaptive state, finite step과 non-Gaussian noise를 지우면 실제 optimizer와 다른 모델이 된다.

## 학습 목표

- SGD update를 mean gradient와 noise로 분해할 수 있다.
- gradient flow와 diffusion approximation의 역할을 구분할 수 있다.
- learning rate·batch size가 근사 noise scale에 미치는 영향을 설명할 수 있다.
- 연속시간 근사의 타당성을 진단하는 측정 항목을 제시할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-DYN-06 확률미분방정식](A09-DYN-06-stochastic-differential-equations.md), [I08-04 SGD dynamics](../../part-3-interpretability/I08/I08-04-sgd-as-dynamics.md), [I08-05 mini-batch noise](../../part-3-interpretability/I08/I08-05-minibatch-noise-optimizer-state.md)
- 확인 질문: mini-batch gradient와 full gradient의 차이는 어떤 random variable인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $g_B(\theta)$ | `g sub B of theta` | mini-batch gradient | parameter-shaped vector |
| $\xi_B(\theta)$ | `xi sub B of theta` | gradient noise | zero-mean under sampling assumptions |
| $C(\theta)$ | `C of theta` | gradient-noise covariance | PSD matrix |
| $\eta$ | `eta` | learning rate | positive scalar |

## 핵심 개념

mini-batch gradient를

$$
g_B(\theta)=\nabla L(\theta)+\xi_B(\theta)
$$

로 쓰면 SGD는 $\theta_{k+1}=\theta_k-\eta\nabla L(\theta_k)-\eta\xi_k$이다. noise를 지우고 time scale을 맞추면 gradient flow

$$
\dot\theta=-\nabla L(\theta)
$$

를 얻는다. 작은 step, 적절한 mixing과 moment 조건 아래 noise covariance를 반영한 diffusion approximation을 만들 수 있지만 계수는 시간 scaling과 batch sampling convention에 의존한다.

실제 진단에는 relative update norm, gradient-noise mean·covariance, autocorrelation, learning-rate schedule, momentum·Adam moment를 포함한다. 근사는 finite horizon에서는 유용해도 rare transition이나 장기 stationary behavior를 틀릴 수 있다.

## 작은 예제

scalar quadratic $L(\theta)=a\theta^2/2$의 gradient flow는 $\theta(t)=\theta_0e^{-at}$이다. gradient descent는 $(1-\eta a)^k\theta_0$이므로 $\eta a$가 작을 때만 exponential과 가까워진다.

## 흔한 오해

- batch size만으로 SGD temperature가 유일하게 정해지는 것은 아니다.
- AdamW를 parameter-only gradient flow로 쓰면 moment state와 weight decay 분리를 놓친다.

## 연습문제

### 1. noise 분해
$\nabla L=3$, mini-batch gradient가 5이면 $\xi_B$는 얼마인가?
<details><summary>해설 보기</summary>

$5-3=2$이다.
</details>

### 2. quadratic flow
$L(\theta)=\theta^2$, $\theta_0=2$일 때 gradient flow 해를 구하라.
<details><summary>해설 보기</summary>

$\dot\theta=-2\theta$이므로 $\theta(t)=2e^{-2t}$이다.
</details>

### 3. Euler stability
$L(\theta)=a\theta^2/2$의 gradient descent가 scalar 방향에서 수렴하려면 $|1-\eta a|<1$이어야 한다. $a>0$일 때 $\eta$ 범위를 구하라.
<details><summary>해설 보기</summary>

$0<\eta a<2$이므로 $0<\eta<2/a$이다.
</details>

### 4. 근사 진단
gradient noise의 lag-1 autocorrelation이 크면 white-noise SDE 근사에 어떤 문제가 생기는가?
<details><summary>해설 보기</summary>

연속 근사가 독립 increment를 가정하면 시간 상관을 잃는다. colored noise나 확장 state가 필요할 수 있다.
</details>

## 근거와 갱신 경계

SGD diffusion 근사의 가정과 한계는 [Mandt et al.](https://www.jmlr.org/papers/v18/17-214.html)과 [Li et al.](https://www.jmlr.org/papers/v20/17-526.html)의 연속시간 분석을 출발점으로 삼는다. 이 결과를 모든 deep-network training regime에 자동 적용하지 않는다.

## 단원 요약

- SGD는 mean gradient와 sampling noise로 분해할 수 있다.
- gradient flow는 평균 drift의 연속시간 이상화다.
- diffusion approximation은 noise covariance와 scaling 가정이 필요하다.
- finite step·state·autocorrelation을 측정해 근사의 범위를 제한한다.

## 통과 기준

- SGD update에서 drift와 noise를 분리할 수 있는가?
- 연속시간 근사에 필요한 진단을 세 가지 이상 말할 수 있는가?

## 다음 단원

- [A09-DYN-08 종합 실습: 학습 궤적 분석](A09-DYN-08-capstone-learning-trajectories.md)

## 집필자 점검표

- [x] 연속시간 근사의 적용 조건과 실패 모드를 밝혔다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
