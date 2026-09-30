---
id: "M04-14"
title: "mutual information"
part: 1
stage: "M04"
status: "완료"
prerequisites:
  - "M04-02"
  - "M04-03"
  - "M04-12"
  - "M04-13"
estimated_time: "145~175분"
---

# M04-14. mutual information

## 이 단원이 필요한 이유

두 변수의 correlation이 0이어도 비선형 의존성이 남을 수 있다. mutual information은 joint distribution을 두 marginal distribution의 곱과 비교해 모든 형태의 statistical dependence를 측정한다. 한 변수를 관측했을 때 다른 변수의 entropy가 평균적으로 얼마나 줄어드는지로도 읽을 수 있다.

representation과 label 사이 mutual information, layer를 지날 때 정보가 줄어드는 data processing inequality, feature selection의 information criterion이 이 개념을 사용한다. 높은 mutual information은 dependence를 보여 주지만 모델이 해당 정보를 기능적으로 사용하거나 한 변수가 다른 변수의 원인이라는 결론까지 주지는 않는다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- joint entropy와 conditional entropy를 계산할 수 있다.
- mutual information을 joint distribution과 marginal product 사이 KL로 쓸 수 있다.
- entropy 차이 형태의 mutual information identities를 사용할 수 있다.
- 독립·완전복사·noisy-copy 예제의 mutual information을 계산할 수 있다.
- symmetry, nonnegativity와 independence equality 조건을 설명할 수 있다.
- data processing inequality를 representation map에 적용할 수 있다.
- estimated mutual information이 허용하는 모델 해석 주장을 제한할 수 있다.

## 선수지식 확인

- 선수 단원: [M04-02 조건부확률과 Bayes 규칙](M04-02-conditional-probability-bayes-rule.md)
- 선수 단원: [M04-03 확률변수와 확률분포](M04-03-random-variables-distributions.md)
- 선수 단원: [M04-12 entropy와 cross entropy](M04-12-entropy-cross-entropy.md)
- 선수 단원: [M04-13 KL divergence](M04-13-kl-divergence.md)
- 확인 질문: joint·marginal·conditional distribution을 구분할 수 있는가?
- 확인 질문: KL divergence가 0이 되는 distribution 조건을 설명할 수 있는가?

## 기호와 용어

| 표기·용어 | 읽는 법 | 의미 | 조건·범위 |
|---|---|---|---|
| $\mathrm H(X,Y)$ | 엑스 와이의 joint entropy | joint distribution의 entropy | discrete variables |
| $\mathrm H(X\mid Y)$ | 와이가 주어진 엑스의 conditional entropy | $Y$를 관측한 뒤 남는 $X$의 평균 uncertainty | $\ge0$ for discrete variables |
| $I(X;Y)$ | 엑스와 와이의 mutual information | joint distribution과 marginal product 사이 KL | $\ge0$ |
| $p_Xp_Y$ | marginal product | $p_X(x)p_Y(y)$ | independence model |
| pointwise mutual information | 점별 상호정보량 | 한 outcome pair의 log density ratio | 값은 음수일 수 있음 |
| Markov chain | 마르코프 연쇄 | 중간변수를 알면 양 끝 변수가 조건부독립인 구조 | $X\to Z\to Y$ |

## 핵심 개념 1. joint entropy는 변수 쌍의 uncertainty를 센다

이산 확률변수 $X,Y$의 joint entropy는

\[
\mathrm H(X,Y)
=-\sum_{x,y}p_{X,Y}(x,y)
\log p_{X,Y}(x,y)
\]

이다. 변수 쌍 $(X,Y)$를 하나의 categorical outcome으로 보고 entropy를 계산한 값이다.

conditional entropy는

\[
\mathrm H(X\mid Y)
=-\sum_{x,y}p_{X,Y}(x,y)
\log p_{X\mid Y}(x\mid y)
\]

이다. 각 $Y=y$에서 $X$의 conditional entropy를 계산하고 $p_Y(y)$로 평균한 값과 같다.

\[
\mathrm H(X\mid Y)
=\sum_y p_Y(y)\mathrm H(X\mid Y=y).
\]

## 핵심 개념 2. mutual information은 dependence를 KL로 측정한다

$X$와 $Y$가 독립이면 joint distribution은

\[
p_{X,Y}(x,y)=p_X(x)p_Y(y)
\]

로 분해된다. mutual information은 실제 joint distribution과 이 independence model 사이 KL divergence이다.

\[
I(X;Y)
=D_{\mathrm{KL}}
\left(
p_{X,Y}\Vert p_Xp_Y
\right).
\]

이산형으로 펼치면

\[
I(X;Y)
=\sum_{x,y}p_{X,Y}(x,y)
\log
\frac{p_{X,Y}(x,y)}
{p_X(x)p_Y(y)}.
\]

joint probability가 marginal product보다 큰 pair는 positive contribution을, 작은 pair는 negative contribution을 줄 수 있다. 전체 평균인 mutual information은 음수가 아니다.

## 핵심 개념 3. pointwise mutual information은 한 pair의 관계를 나타낸다

outcome pair $(x,y)$의 pointwise mutual information(PMI)은

\[
\operatorname{PMI}(x,y)
=\log
\frac{p_{X,Y}(x,y)}
{p_X(x)p_Y(y)}
\]

이다. 이 pair가 independence model의 예상보다 자주 함께 나타나면 positive이고 덜 나타나면 negative이다.

mutual information은 PMI를 joint distribution으로 평균한다.

\[
I(X;Y)=\mathbb E_{(X,Y)\sim p_{X,Y}}
[\operatorname{PMI}(X,Y)].
\]

PMI 하나가 negative일 수 있다는 사실과 전체 MI가 nonnegative라는 사실은 모순이 아니다.

## 핵심 개념 4. mutual information은 entropy 감소량이다

joint distribution을 조건부분포로 분해하면 다음 identities를 얻는다.

\[
I(X;Y)
=\mathrm H(X)-\mathrm H(X\mid Y)
\]

\[
=\mathrm H(Y)-\mathrm H(Y\mid X)
\]

\[
=\mathrm H(X)+\mathrm H(Y)-\mathrm H(X,Y).
\]

첫 식은 $Y$를 관측한 뒤 $X$의 uncertainty가 평균적으로 얼마나 줄어드는지 나타낸다. 두 번째 식 때문에

\[
I(X;Y)=I(Y;X)
\]

인 symmetry가 성립한다.

## 핵심 개념 5. MI가 0인 조건은 independence이다

KL divergence의 nonnegativity로

\[
I(X;Y)\ge0
\]

이다. discrete variables에서

\[
I(X;Y)=0
\]

이면 joint distribution이 marginal product와 같으므로 $X,Y$는 독립이다. 독립이면 반대로 MI가 0이다.

correlation 0은 linear dependence가 없다는 조건이다. MI 0은 joint distribution 전체가 factorize한다는 더 강한 조건이다. finite-sample MI estimate가 0에 가깝다는 사실은 population independence의 증명이 아니며 estimator uncertainty를 함께 봐야 한다.

## 핵심 개념 6. deterministic copy는 output entropy만큼 정보를 가진다

$Y=g(X)$가 deterministic function이면 $X$를 알 때 $Y$가 정해지므로

\[
\mathrm H(Y\mid X)=0.
\]

따라서

\[
I(X;Y)=\mathrm H(Y).
\]

$g$가 bijection이면 $X$와 $Y$가 서로를 결정하므로

\[
I(X;Y)=\mathrm H(X)=\mathrm H(Y).
\]

discrete variable의 label 이름을 일대일로 바꾸어도 MI는 변하지 않는다. representation coordinate의 invertible relabeling 아래 정보량을 비교할 때 유용한 성질이다.

## 핵심 개념 7. data processing은 후처리가 정보를 늘리지 못하게 한다

$X\to Z\to Y$가 Markov chain이면 $X$와 $Y$는 $Z$가 주어졌을 때 조건부독립이다. data processing inequality는

\[
I(X;Y)\le I(X;Z)
\]

를 준다. $Z$에서 추가 연산으로 $Y$를 만들면 $X$에 관한 information이 새로 생기지 않는다는 뜻이다.

representation $H=f(X)$가 입력의 deterministic function이면 label $Y$와의 관계에서

\[
I(Y;H)\le I(Y;X)
\]

이다. equality나 information loss의 크기는 $f$와 joint distribution에 달려 있다. finite-sample estimator가 inequality를 어기면 estimation error나 가정 위반을 점검해야 한다.

## 핵심 개념 8. high-dimensional MI estimation은 estimator에 민감하다

categorical joint table에서는 empirical count로 MI를 계산할 수 있다. sample이 적고 category 수가 많으면 empty cell과 plug-in bias가 커진다. continuous·high-dimensional representation에서는 density estimation, binning, k-nearest-neighbor bound와 variational bound가 서로 다른 bias를 가진다.

probe accuracy가 높으면 representation $H$와 label $Y$ 사이 dependence를 시사하지만 exact $I(H;Y)$ 값을 바로 주지는 않는다. 높은 MI도 모델이 $H$의 label information을 output computation에 사용한다는 intervention evidence가 아니다.

deterministic continuous network에서는 $I(X;H)$가 density assumptions와 injected noise에 따라 infinite하거나 ill-defined해질 수 있다. estimator가 출력한 finite number를 intrinsic property로 해석하기 전에 변수 정의와 noise model을 밝혀야 한다.

## 예제 1. 독립인 두 fair bit

$X,Y$가 독립이며 각각 Bernoulli$(1/2)$라고 하자. 모든 pair의 joint probability는 $1/4$이고 marginal product도 $1/4$이다.

\[
I(X;Y)
=\sum_{x,y}\frac14\log\frac{1/4}{1/4}
=0.
\]

## 예제 2. 완전복사된 fair bit

$X\sim\operatorname{Bernoulli}(1/2)$이고 $Y=X$라 하자. joint distribution은 $(0,0)$과 $(1,1)$에 각각 $1/2$을 둔다.

\[
\begin{aligned}
I(X;Y)
&=\frac12\log\frac{1/2}{(1/2)(1/2)}
+\frac12\log\frac{1/2}{(1/2)(1/2)}\\
&=\log2
\approx0.693\ \text{nats}.
\end{aligned}
\]

$Y$가 $X$를 그대로 복사하므로 MI는 fair bit entropy와 같다.

## 예제 3. noisy copy

$X$가 fair bit이고 $Y$가 probability $0.8$로 $X$를 복사하며 probability $0.2$로 뒤집힌다고 하자. joint probabilities는

\[
p(0,0)=p(1,1)=0.4,
\qquad
p(0,1)=p(1,0)=0.1
\]

이고 두 marginal은 uniform이다. 따라서

\[
\begin{aligned}
I(X;Y)
&=2(0.4)\log\frac{0.4}{0.25}
+2(0.1)\log\frac{0.1}{0.25}\\
&=0.8\log1.6+0.2\log0.4\\
&\approx0.193\ \text{nats}.
\end{aligned}
\]

noise 때문에 완전복사의 $\log2\approx0.693$보다 MI가 작다.

## 예제 4. entropy identity 사용하기

$\mathrm H(X)=0.9$, $\mathrm H(Y)=0.8$, $\mathrm H(X,Y)=1.2$ nats이면

\[
I(X;Y)
=0.9+0.8-1.2
=0.5\ \text{nats}.
\]

또한

\[
\mathrm H(X\mid Y)
=\mathrm H(X)-I(X;Y)
=0.4\ \text{nats}.
\]

## 흔한 오해

### 오해 1. MI는 correlation의 다른 이름이다

correlation은 linear relation을 요약한다. MI는 joint distribution이 independence model에서 벗어난 모든 형태를 측정한다.

### 오해 2. PMI와 MI는 둘 다 nonnegative이다

개별 pair의 PMI는 negative일 수 있다. joint distribution으로 평균한 MI는 KL divergence이므로 nonnegative이다.

### 오해 3. 높은 MI는 한 변수가 다른 변수의 원인임을 뜻한다

MI는 symmetric dependence measure이다. causal direction과 intervention effect를 정하지 않는다.

### 오해 4. representation-label MI가 높으면 모델이 label 정보를 사용한다

dependence나 decodability는 기능적 사용과 구분해야 한다. activation을 조절했을 때 output이 변하는지 확인하는 intervention이 필요하다.

### 오해 5. neural representation의 MI는 estimator와 관계없는 고정된 수이다

continuous variable 정의, noise, binning과 estimator family가 결과에 영향을 준다. finite-sample estimate에는 bias와 variance도 있다.

## 연습문제

### 1. independence와 MI

$p_{X,Y}(x,y)=p_X(x)p_Y(y)$가 모든 pair에서 성립한다. $I(X;Y)$를 구하라.

<details>
<summary>해설 보기</summary>

각 log ratio가

\[
\log\frac{p_{X,Y}(x,y)}{p_X(x)p_Y(y)}=\log1=0
\]

이므로 $I(X;Y)=0$이다.

</details>

### 2. 완전복사

$X$가 세 값에 uniform하고 $Y=X$이다. natural log를 사용할 때 $I(X;Y)$를 구하라.

<details>
<summary>해설 보기</summary>

$Y$는 $X$의 deterministic copy이므로

\[
I(X;Y)=\mathrm H(Y)=\log3\ \text{nats}.
\]

</details>

### 3. entropy identity

$\mathrm H(X)=0.7$, $\mathrm H(Y)=0.8$, $\mathrm H(X,Y)=1.1$ nats이다. $I(X;Y)$를 구하라.

<details>
<summary>해설 보기</summary>

\[
I(X;Y)=0.7+0.8-1.1=0.4\ \text{nats}.
\]

</details>

### 4. conditional entropy

$\mathrm H(X)=1.0$ nat이고 $I(X;Y)=0.35$ nat이다. $\mathrm H(X\mid Y)$를 구하라.

<details>
<summary>해설 보기</summary>

\[
\mathrm H(X\mid Y)
=\mathrm H(X)-I(X;Y)
=1.0-0.35
=0.65\ \text{nat}.
\]

</details>

### 5. deterministic mapping

$Y=g(X)$가 deterministic이고 $\mathrm H(Y)=0.6$ nat이다. $I(X;Y)$를 구하라.

<details>
<summary>해설 보기</summary>

$Y$를 $X$가 정하므로 $\mathrm H(Y\mid X)=0$이다. 따라서

\[
I(X;Y)=\mathrm H(Y)-\mathrm H(Y\mid X)=0.6.
\]

</details>

### 6. data processing

$Y\to X\to H$가 Markov chain이고 $I(Y;X)=0.9$ nat이다. $I(Y;H)=1.1$ nat이라는 exact population 값이 가능한지 판단하라.

<details>
<summary>해설 보기</summary>

data processing inequality에 따라

\[
I(Y;H)\le I(Y;X)=0.9
\]

이어야 한다. exact population 값 1.1은 가능하지 않다. empirical estimate가 이런 결과를 내면 estimator error나 Markov assumption 위반을 점검해야 한다.

</details>

### 7. 모델 해석 주장 비판

한 연구가 activation과 concept label 사이 MI estimate가 높다고 보고하며 “모델이 이 concept을 사용한다”고 결론 내렸다. 추가로 확인할 항목을 설명하라.

<details>
<summary>해설 보기</summary>

먼저 MI estimator의 finite-sample bias, binning·noise 설정과 held-out stability를 확인해야 한다. 높은 MI는 statistical dependence를 나타내며 기능적 사용을 보장하지 않는다. concept-related activation을 ablate하거나 patch한 뒤 relevant output effect를 대조군과 함께 측정해야 사용 주장을 평가할 수 있다.

</details>

## 단원 요약

- joint entropy는 변수 쌍의 uncertainty이고 conditional entropy는 한 변수를 관측한 뒤 남는 평균 uncertainty이다.
- mutual information은 joint distribution과 marginal product 사이 KL divergence이다.
- mutual information은 entropy 감소량이며 $X,Y$에 대해 symmetric하다.
- discrete variables에서 MI는 nonnegative이고 0일 조건은 independence이다.
- deterministic mapping에서는 input-output MI가 output entropy와 같다.
- data processing inequality는 후처리가 source에 관한 information을 늘릴 수 없음을 나타낸다.
- high-dimensional representation의 MI estimate는 variable·noise·estimator 정의에 민감하며 기능적 사용을 보장하지 않는다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- joint·conditional entropy를 정의할 수 있는가?
- MI를 joint와 marginal product 사이 KL로 쓸 수 있는가?
- entropy identities로 MI를 계산할 수 있는가?
- independence·copy·noisy-copy 예제의 MI를 계산할 수 있는가?
- symmetry와 independence equality 조건을 설명할 수 있는가?
- data processing inequality를 representation에 적용할 수 있는가?
- MI estimate가 허용하지 않는 인과·사용 주장을 설명할 수 있는가?

## 다음 단원

- [M04-15 calibration과 scoring rule](M04-15-calibration-scoring-rules.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] joint·conditional entropy를 정의했다.
- [x] MI의 KL·entropy identities를 설명했다.
- [x] independence·copy·noise 예제를 검산했다.
- [x] data processing inequality를 적용했다.
- [x] MI estimation과 모델 해석 한계를 밝혔다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 구분자를 확인했다.
