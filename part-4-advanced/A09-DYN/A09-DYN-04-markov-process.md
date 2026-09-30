---
id: "A09-DYN-04"
title: "Markov process"
part: 4
stage: "A09-DYN"
status: "완료"
prerequisites: ["M04-02", "M04-03", "M02-11"]
estimated_time: "90~120분"
---

# A09-DYN-04. Markov process

## 이 단원이 필요한 이유

mini-batch sampling이나 noisy update를 확률적 state transition으로 보면 deterministic trajectory만으로는 설명하지 못하는 분포 변화를 다룰 수 있다. Markov property는 미래가 현재 state를 조건으로 과거와 독립이라는 모델링 가정이다.

## 학습 목표

- Markov property를 조건부확률로 쓸 수 있다.
- transition matrix로 분포를 한 step 전파할 수 있다.
- stationary distribution과 detailed balance를 구분할 수 있다.
- state 정의가 Markov 가정의 타당성을 바꾸는 이유를 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [M04-02 조건부확률](../../part-1-foundations/M04/M04-02-conditional-probability-bayes-rule.md), [M04-03 확률변수](../../part-1-foundations/M04/M04-03-random-variables-distributions.md), [M02-11 고유값](../../part-1-foundations/M02/M02-11-eigenvalues-eigenvectors.md)
- 확인 질문: 조건부독립은 어떤 변수를 조건으로 삼는지에 왜 의존하는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $X_t$ | `X sub t` | time $t$의 random state | state space-valued |
| $P_{ij}$ | `P i j` | $i$에서 $j$로 갈 확률 | $[0,1]$ |
| $\pi$ | `pi` | stationary distribution | probability vector |
| $\pi_iP_{ij}=\pi_jP_{ji}$ | `pi i P i j equals pi j P j i` | detailed balance | pairwise condition |

## 핵심 개념

Markov property는

$$
P(X_{t+1}\mid X_t,\ldots,X_0)=P(X_{t+1}\mid X_t)
$$

이다. finite state chain에서 row distribution $p_t$는 $p_{t+1}=p_tP$로 전파된다. stationary distribution은 $\pi=\pi P$를 만족한다.

detailed balance는 각 state pair 사이의 probability flow가 상쇄되는 더 강한 조건이다. 이를 만족하면 stationary이지만, 모든 stationary chain이 detailed balance를 만족하는 것은 아니다.

optimizer parameter만 state로 잡으면 momentum이나 Adam의 moment가 누락되어 Markov가 아닐 수 있다. parameter와 optimizer state를 함께 포함하면 transition model이 달라진다.

## 작은 예제

$P=\begin{bmatrix}0.8&0.2\\0.4&0.6\end{bmatrix}$의 stationary distribution은 $\pi=(2/3,1/3)$이다. 두 방향 flow는 모두 $2/15$라 detailed balance도 만족한다.

## 흔한 오해

- Markov라는 말은 state들이 독립이라는 뜻이 아니다.
- stationary distribution은 chain이 어느 초기분포에서나 빠르게 수렴한다는 뜻이 아니다.

## 연습문제

### 1. 한 step 전파
$p_0=(1,0)$과 위 $P$에서 $p_1$을 구하라.
<details><summary>해설 보기</summary>

$p_1=p_0P=(0.8,0.2)$이다.
</details>

### 2. stationary 확인
$\pi=(2/3,1/3)$에 $P$를 곱해 stationary임을 확인하라.
<details><summary>해설 보기</summary>

첫 성분은 $2/3\cdot0.8+1/3\cdot0.4=2/3$, 둘째는 $1/3$이다.
</details>

### 3. Markov state
momentum SGD에서 parameter만 기록하면 과거가 필요한 이유는 무엇인가?
<details><summary>해설 보기</summary>

다음 update가 누적 velocity에 의존하며 그 값은 parameter만으로 복원되지 않기 때문이다.
</details>

### 4. stationarity
$\pi P=\pi$만 확인해 convergence 속도를 알 수 있는가?
<details><summary>해설 보기</summary>

없다. irreducibility·aperiodicity와 transition spectrum 등 mixing 정보를 추가로 봐야 한다.
</details>

## 근거와 갱신 경계

Markov property·stationarity·detailed balance는 확률과정의 표준 정의를 따른다. 일반 state space의 measure-theoretic kernel은 다루지 않는다.

## 단원 요약

- Markov property는 현재 state가 과거 정보를 충분히 담는다는 가정이다.
- transition matrix는 state distribution을 전파한다.
- detailed balance는 stationarity보다 강하다.
- optimizer의 state 정의에는 moment와 schedule을 포함할 수 있다.

## 통과 기준

- transition matrix로 분포를 계산할 수 있는가?
- stationary·detailed balance·mixing을 구분할 수 있는가?

## 다음 단원

- [A09-DYN-05 Langevin dynamics](A09-DYN-05-langevin-dynamics.md)

## 집필자 점검표

- [x] Markov state와 optimizer state를 연결했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
