---
id: "A09-DYN-05"
title: "Langevin dynamics"
part: 4
stage: "A09-DYN"
status: "완료"
prerequisites: ["A09-DYN-01", "A09-DYN-04", "M04-05"]
estimated_time: "90~120분"
---

# A09-DYN-05. Langevin dynamics

## 이 단원이 필요한 이유

gradient 방향의 drift와 random fluctuation을 함께 쓰면 optimization noise와 sampling을 같은 수학적 틀에서 비교할 수 있다. Langevin dynamics는 energy landscape를 따라 내려가는 힘과 diffusion을 결합한다.

## 학습 목표

- overdamped Langevin equation의 drift와 diffusion을 구분할 수 있다.
- temperature가 stationary density에 미치는 영향을 설명할 수 있다.
- Euler–Maruyama update를 계산할 수 있다.
- SGD noise와 isotropic Langevin noise의 차이를 말할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-DYN-01 미분방정식과 흐름](A09-DYN-01-odes-flows.md), [A09-DYN-04 Markov process](A09-DYN-04-markov-process.md), [M04-05 주요 분포](../../part-1-foundations/M04/M04-05-common-distributions.md)
- 확인 질문: deterministic gradient step에 Gaussian perturbation을 더하면 다음 state는 무엇이 되는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $U(x)$ | `U of x` | potential 또는 energy | scalar |
| $T$ | `temperature T` | noise scale | positive scalar |
| $W_t$ | `W sub t` | Brownian motion | stochastic process |
| $dX_t=-\nabla U(X_t)dt+\sqrt{2T}\,dW_t$ | `d X t equals minus grad U of X t d t plus square root two T d W t` | overdamped Langevin equation | vector SDE |

## 핵심 개념

overdamped Langevin dynamics는

$$
dX_t=-\nabla U(X_t)dt+\sqrt{2T}\,dW_t
$$

이다. 첫 항은 낮은 energy로 이동시키는 drift이고 둘째 항은 확산이다. 적절한 regularity와 confinement 아래 stationary density는

$$
p_\infty(x)\propto e^{-U(x)/T}
$$

가 된다. $T$가 작으면 낮은 energy 부근에 더 집중한다.

step $h$의 Euler–Maruyama update는

$$
X_{k+1}=X_k-h\nabla U(X_k)+\sqrt{2Th}\,\xi_k,
\qquad \xi_k\sim\mathcal N(0,I)
$$

이다. discretization은 stationary distribution에 bias를 만들 수 있다.

## 작은 예제

$U(x)=x^2/2$이면 drift는 $-x$이고 stationary density는 variance $T$인 Gaussian이다.

## 흔한 오해

- mini-batch SGD noise는 일반적으로 constant isotropic Gaussian이 아니다.
- finite-step Langevin update가 정확히 $e^{-U/T}$를 sampling한다고 단정할 수 없다.

## 연습문제

### 1. drift
$U(x)=2x^2$의 Langevin drift를 구하라.
<details><summary>해설 보기</summary>

$\nabla U=4x$이므로 drift는 $-4x$이다.
</details>

### 2. noise scale
$T=0.5$, $h=0.01$에서 update noise coefficient $\sqrt{2Th}$를 구하라.
<details><summary>해설 보기</summary>

$\sqrt{0.01}=0.1$이다.
</details>

### 3. temperature
$T$가 작아지면 $p_\infty(x)\propto e^{-U(x)/T}$는 어떻게 변하는가?
<details><summary>해설 보기</summary>

높은 energy가 더 강하게 억제되어 minimum 부근에 집중한다.
</details>

### 4. SGD 비교
SGD를 Langevin dynamics로 근사할 때 noise covariance를 측정해야 하는 이유는 무엇인가?
<details><summary>해설 보기</summary>

SGD noise는 parameter 위치와 batch 구성에 따라 anisotropic·state-dependent일 수 있어 isotropic temperature 하나로 표현되지 않을 수 있기 때문이다.
</details>

## 근거와 갱신 경계

overdamped Langevin equation과 Gibbs stationary density는 stochastic dynamics의 표준 결과를 따른다. Metropolis correction과 underdamped dynamics는 다루지 않는다.

## 단원 요약

- Langevin dynamics는 gradient drift와 Brownian diffusion을 결합한다.
- temperature는 stationary density의 집중 정도를 조절한다.
- Euler–Maruyama noise는 $\sqrt h$ scale이다.
- SGD noise를 Langevin noise와 같다고 두려면 covariance 가정이 필요하다.

## 통과 기준

- quadratic potential의 drift와 stationary variance를 설명할 수 있는가?
- finite-step·SGD 근사의 한계를 말할 수 있는가?

## 다음 단원

- [A09-DYN-06 확률미분방정식 입문](A09-DYN-06-stochastic-differential-equations.md)

## 집필자 점검표

- [x] drift·diffusion·temperature를 구분했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
