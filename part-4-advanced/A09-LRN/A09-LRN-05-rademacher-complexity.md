---
id: "A09-LRN-05"
title: "Rademacher complexity"
part: 4
stage: "A09-LRN"
status: "완료"
prerequisites: ["A09-LRN-03", "M04-04"]
estimated_time: "90~120분"
---

# A09-LRN-05. Rademacher complexity

## 이 단원이 필요한 이유

VC dimension은 class의 worst-case combinatorial capacity를 보지만 실제 sample geometry는 반영하지 않는다. empirical Rademacher complexity는 주어진 sample에서 random sign을 얼마나 잘 맞출 수 있는지로 function class의 data-dependent richness를 잰다.

## 학습 목표

- empirical Rademacher complexity의 각 random source를 설명할 수 있다.
- 작은 finite class의 값을 계산할 수 있다.
- contraction과 norm constraint의 역할을 설명할 수 있다.
- random-label control과 learning-theory complexity를 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-LRN-03 generalization gap](A09-LRN-03-generalization-gap.md), [M04-04 기댓값과 분산](../../part-1-foundations/M04/M04-04-expectation-variance-covariance.md)
- 확인 질문: independent random sign의 평균과 분산은 얼마인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\sigma_i$ | `sigma i` | independent Rademacher sign | $\{-1,+1\}$ |
| $\hat{\mathfrak R}_S(\mathcal F)$ | `the empirical Rademacher complexity of F on S` | sample-dependent complexity | nonnegative scalar |
| $\sup_{f\in\mathcal F}$ | `the supremum over f in F` | random signs에 가장 잘 맞는 function | operator |
| $B$ | `B` | norm bound | positive scalar |

## 핵심 개념

sample $S=(x_1,\ldots,x_n)$에서

$$
\hat{\mathfrak R}_S(\mathcal F)
=E_\sigma\left[\sup_{f\in\mathcal F}
\frac1n\sum_{i=1}^n\sigma_i f(x_i)\right].
$$

class가 arbitrary random sign을 잘 맞추면 complexity가 크다. bounded linear class $f_w(x)=w^\top x$, $\|w\|\le B$에서는 dual norm으로 supremum을 계산해 input norm과 $B$에 의존하는 bound를 얻는다.

Lipschitz loss를 합성하면 contraction inequality로 loss class complexity를 제어할 수 있다. 이는 random-label probe를 실제로 학습시키는 empirical control과 관련은 있지만 같은 절차나 같은 숫자는 아니다.

## 작은 예제

$\mathcal F=\{f,-f\}$이면 fixed signs에서 supremum은 $|n^{-1}\sum_i\sigma_if(x_i)|$이고 sign expectation을 취한다.

## 흔한 오해

- empirical Rademacher complexity는 training label을 randomize한 accuracy와 동일하지 않다.
- unconstrained real-valued linear class는 scale을 무한히 키울 수 있어 유용한 finite bound가 없다.

## 연습문제

### 1. singleton class
$\mathcal F=\{f_0\}$이고 $f_0(x)=0$이면 complexity는 얼마인가?
<details><summary>해설 보기</summary>

모든 sign 합이 0이므로 0이다.
</details>

### 2. constant pair
$n=1$, $\mathcal F=\{f_+,f_-\}$, $f_+(x)=1$, $f_-(x)=-1$이면 complexity는 얼마인가?
<details><summary>해설 보기</summary>

sign이 어느 쪽이든 맞는 constant를 골라 supremum이 1이므로 expectation도 1이다.
</details>

### 3. norm constraint
linear class의 weight norm bound를 두 배로 늘리면 표준 upper bound는 어떻게 변하는가?
<details><summary>해설 보기</summary>

다른 조건이 같으면 $B$에 선형이므로 두 배가 된다.
</details>

### 4. probe control
random-label accuracy와 Rademacher bound를 함께 쓰면 각각 무엇을 알려주는가?
<details><summary>해설 보기</summary>

random-label accuracy는 실제 pipeline의 memorization control이고 Rademacher bound는 지정 class·sample의 uniform deviation capacity를 이론적으로 제어한다.
</details>

## 근거와 갱신 경계

empirical Rademacher complexity와 contraction은 learning theory의 표준 정의를 따른다. deep network의 최신 norm-based bound 비교는 다루지 않는다.

## 단원 요약

- Rademacher complexity는 sample 위 random sign 적합 능력을 잰다.
- supremum과 sign expectation을 구분한다.
- norm constraint와 input geometry가 finite bound를 만든다.
- random-label 실험과 이론 complexity를 같은 값으로 보지 않는다.

## 통과 기준

- 작은 function class의 empirical complexity를 계산할 수 있는가?
- norm bound와 random-label control의 역할을 설명할 수 있는가?

## 다음 단원

- [A09-LRN-06 PAC learning](A09-LRN-06-pac-learning.md)

## 집필자 점검표

- [x] Rademacher random source와 supremum을 구분했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
