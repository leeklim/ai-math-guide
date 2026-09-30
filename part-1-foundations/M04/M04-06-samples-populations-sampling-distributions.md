---
id: "M04-06"
title: "표본, 모집단과 표본분포"
part: 1
stage: "M04"
status: "완료"
prerequisites:
  - "M04-04"
  - "M04-05"
estimated_time: "145~175분"
---

# M04-06. 표본, 모집단과 표본분포

## 이 단원이 필요한 이유

연구자는 데이터셋에서 평균 loss, probe accuracy나 attribution 평균을 계산한다. 이 수들은 관측한 sample의 요약값이다. 연구 질문은 더 넓은 입력 집단이나 반복 실험에서의 성능을 묻는 경우가 많다. sample에서 계산한 수와 목표 population의 값을 구분해야 관측 오차와 일반화 범위를 말할 수 있다.

같은 population에서 sample을 다시 뽑으면 표본평균이나 정확도도 달라진다. 통계량의 이러한 변동을 나타내는 분포가 sampling distribution이다. 표준오차, 신뢰구간과 가설검정은 sampling distribution을 사용한다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- 목표 모집단, 확률표본과 관측 sample을 구분할 수 있다.
- iid 가정의 독립성과 동일분포 조건을 각각 설명할 수 있다.
- 통계량과 모수의 차이를 예로 설명할 수 있다.
- 표본평균, 표본분산과 경험분포를 계산할 수 있다.
- sampling distribution을 원자료 분포와 구분할 수 있다.
- iid 표본평균의 기댓값·분산·표준오차를 계산할 수 있다.
- 실험 단위의 의존성이 불확실성 평가에 주는 영향을 판단할 수 있다.

## 선수지식 확인

- 선수 단원: [M04-04 기댓값, 분산과 공분산](M04-04-expectation-variance-covariance.md)
- 선수 단원: [M04-05 주요 분포](M04-05-common-distributions.md)
- 확인 질문: 확률변수의 평균과 분산을 계산할 수 있는가?
- 확인 질문: Bernoulli와 Gaussian 분포의 support와 파라미터를 설명할 수 있는가?

## 기호와 용어

| 표기·용어 | 읽는 법 | 의미 | 범위 |
|---|---|---|---|
| $P$ | 모집단 분포 피 | 추론하려는 대상 집단의 확률분포 | target population |
| $X_1,\ldots,X_n$ | 확률표본 | 표본을 뽑기 전 random variables | 보통 $X_i\sim P$ |
| $x_1,\ldots,x_n$ | 관측 sample | 한 번 뽑아 얻은 값 | 고정된 데이터 |
| $\theta$ | 모수 세타 | 모집단 분포의 고정되지만 모르는 특성 | 예: $\mu$, $\sigma^2$ |
| $T=t(X_1,\ldots,X_n)$ | 통계량 티 | 확률표본의 함수 | random variable |
| $t=t(x_1,\ldots,x_n)$ | 관측 통계량 | 관측 sample에서 계산한 수 | 고정값 |
| $\bar X$ | 엑스 바 | 표본평균 통계량 | $n^{-1}\sum_iX_i$ |
| $s^2$ | 에스 제곱 | 관측 sample의 표본분산 | $(n-1)^{-1}\sum_i(x_i-\bar x)^2$ |
| $\operatorname{SE}(T)$ | 티의 표준오차 | 통계량 sampling distribution의 표준편차 | 통계량과 같은 단위 |

## 핵심 개념 1. 모집단은 추론 대상이고 표본은 관측한 일부이다

모집단(population)은 연구 질문이 대상으로 삼는 결과 전체나 그 결과를 생성하는 확률분포이다. 유한 데이터 목록을 모집단으로 정할 수도 있고, 앞으로 들어올 입력을 포함하는 분포 $P$로 정할 수도 있다.

표본(sample)은 모집단에서 관측한 $n$개 값이다. 표본을 뽑기 전에는

\[
X_1,\ldots,X_n
\]

을 확률변수로 쓰고, 관측 뒤에는

\[
x_1,\ldots,x_n
\]

을 고정된 값으로 쓴다. 연구자는 표본을 사용해 모집단의 특성을 추정한다. 목표 모집단을 “평가 데이터”처럼 모호하게 두면 어떤 입력과 조건에 결과를 일반화하는지 알 수 없다.

## 핵심 개념 2. iid는 독립과 동일분포를 함께 가정한다

확률표본이 independent and identically distributed(iid)이면

\[
X_1,\ldots,X_n\overset{\mathrm{iid}}{\sim}P
\]

로 쓴다. identically distributed는 각 $X_i$가 같은 population distribution $P$를 따른다는 뜻이다. independent는 한 관측값을 아는 것이 다른 관측값의 분포를 바꾸지 않는다는 뜻이다.

같은 source에서 왔다는 사실만으로 독립이 성립하지는 않는다. 한 문서의 여러 token, 한 사용자의 반복 입력, 같은 학습 run의 여러 checkpoint는 묶음 안에서 의존할 수 있다. sampling distribution 공식을 적용하려면 연구 설계의 독립 단위를 먼저 정해야 한다.

## 핵심 개념 3. 모수와 통계량은 고정·무작위 역할이 다르다

모수(parameter) $\theta$는 population distribution의 특성이다. 빈도주의 표기에서는 $\theta$를 고정됐지만 모르는 값으로 둔다. 예를 들어

\[
\mu=\mathbb E_P[X],
\qquad
\sigma^2=\operatorname{Var}_P(X)
\]

는 모집단 모수이다.

통계량(statistic) $T=t(X_1,\ldots,X_n)$은 표본의 함수이며 모르는 모수를 입력으로 직접 사용하지 않는다. sample을 뽑기 전에는 $T$가 확률변수이고, 관측값을 넣은 $t=t(x_1,\ldots,x_n)$는 하나의 수이다. 표본평균 $\bar X$는 모평균 $\mu$를 추정하는 통계량이다.

## 핵심 개념 4. 표본평균·표본분산·경험분포는 데이터를 서로 다르게 요약한다

표본평균은

\[
\bar X=\frac1n\sum_{i=1}^{n}X_i
\]

이고 관측값에서는

\[
\bar x=\frac1n\sum_{i=1}^{n}x_i
\]

이다. 표본분산은 보통

\[
s^2=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar x)^2
\]

로 계산한다. 분모 $n-1$은 같은 sample에서 평균을 추정하며 잃은 자유도 하나를 반영한다. M04-07에서 이 선택과 불편성을 설명한다.

경험분포(empirical distribution)는 관측값 각각에 질량 $1/n$을 둔다. 사건 $A$의 경험확률은

\[
\widehat P_n(A)
=\frac1n\sum_{i=1}^{n}\mathbf 1\{x_i\in A\}
\]

이다. 표본평균은 위치를, 표본분산은 퍼짐을 요약한다. 경험분포는 관측값의 분포 형태를 더 많이 보존한다.

## 핵심 개념 5. sampling distribution은 통계량 자체의 분포이다

같은 population에서 크기 $n$의 sample을 반복해서 뽑는다고 생각하자. 각 sample마다 통계량 $T$를 계산하면 값이 달라진다. 이 반복 표집에서 생기는 $T$의 확률분포를 표본분포(sampling distribution)라고 한다.

세 분포를 구분해야 한다.

- population distribution: 한 관측값 $X$가 따르는 분포
- empirical distribution: 현재 관측 sample이 만든 분포
- sampling distribution: sample 전체의 함수 $T$가 따르는 분포

표본분포라는 한국어 표현은 “관측 sample 값들의 histogram”으로 오해하기 쉽다. 여기서는 statistic의 repeated-sampling distribution을 뜻한다.

## 핵심 개념 6. iid 표본평균의 변동은 sample size에 따라 줄어든다

$X_1,\ldots,X_n$이 평균 $\mu$, 분산 $\sigma^2$을 가진 iid 표본이면 기댓값의 선형성으로

\[
\mathbb E[\bar X]
=\frac1n\sum_{i=1}^{n}\mathbb E[X_i]
=\mu
\]

이다. 독립이므로 공분산 항이 0이고

\[
\operatorname{Var}(\bar X)
=\operatorname{Var}\left(\frac1n\sum_{i=1}^{n}X_i\right)
=\frac{1}{n^2}\sum_{i=1}^{n}\sigma^2
=\frac{\sigma^2}{n}
\]

이다. 따라서 표본평균의 표준오차는

\[
\operatorname{SE}(\bar X)
=\sqrt{\operatorname{Var}(\bar X)}
=\frac{\sigma}{\sqrt n}
\]

이다. sample size를 네 배로 늘리면 이 표준오차는 절반이 된다. 관측들이 양의 상관을 가지면 공분산 항이 남아 iid 공식보다 변동이 클 수 있다.

## 핵심 개념 7. 중심극한정리는 표본평균의 근사분포를 준다

적절한 조건과 유한한 분산 아래 iid 표본의 크기 $n$이 커지면

\[
\frac{\bar X-\mu}{\sigma/\sqrt n}
\]

의 분포가 표준정규분포에 가까워진다. 이를 중심극한정리(central limit theorem, CLT)라고 한다. 원래 population distribution이 Gaussian일 필요는 없다.

근사의 품질은 sample size와 원래 분포의 skewness, tail에 좌우된다. 작은 $n$이나 heavy-tailed data에서는 Gaussian 근사가 부정확할 수 있다. 의존 표본에는 iid CLT를 그대로 적용할 수 없다.

## 핵심 개념 8. 실험 단위가 sampling uncertainty를 결정한다

모델 해석 실험에서 token 10,000개를 관측했더라도 token들이 prompt 20개 안에 묶여 있다면 독립 단위가 10,000개인지 검토해야 한다. 같은 prompt의 token은 문맥과 model state를 공유한다. token을 독립 sample로 처리하면 표준오차를 작게 추정할 수 있다.

모델 seed, prompt, subject, document 중 무엇을 모집단에 일반화하려는지에 따라 sampling unit이 달라진다. sample size를 보고할 때는 관측 개수와 독립 실험 단위를 함께 밝혀야 한다.

## 예제 1. Bernoulli 표본평균의 sampling distribution

### 문제

$X_1,X_2\overset{\mathrm{iid}}{\sim}\operatorname{Bernoulli}(0.5)$이고

\[
\bar X=\frac{X_1+X_2}{2}
\]

이다. $\bar X$의 sampling distribution을 구한다.

### 풀이

가능한 표본과 표본평균은 다음과 같다.

| $(X_1,X_2)$ | 확률 | $\bar X$ |
|---|---:|---:|
| $(0,0)$ | $1/4$ | 0 |
| $(0,1)$ | $1/4$ | $1/2$ |
| $(1,0)$ | $1/4$ | $1/2$ |
| $(1,1)$ | $1/4$ | 1 |

따라서

\[
P(\bar X=0)=\frac14,
\quad
P\left(\bar X=\frac12\right)=\frac12,
\quad
P(\bar X=1)=\frac14.
\]

이 분포의 평균은 $1/2$이고 분산은

\[
\frac{p(1-p)}{n}
=\frac{(1/2)(1/2)}{2}
=\frac18
\]

이다.

### 결과의 의미

원자료 $X_i$는 0 또는 1을 가진다. 표본평균은 $0,1/2,1$을 가지며, 위 sampling distribution은 이 표본평균에 확률을 배정한다.

## 예제 2. 관측 sample의 평균과 분산

관측값이 $2,4,6$이면

\[
\bar x=\frac{2+4+6}{3}=4
\]

이다. 표본분산은

\[
s^2
=\frac{(2-4)^2+(4-4)^2+(6-4)^2}{3-1}
=\frac{8}{2}
=4
\]

이다. 이 수들은 관측 sample의 통계량이며 population mean과 variance 자체는 아니다.

## 예제 3. 정확도의 표준오차

sample별 정답 indicator가 성공확률 $p=0.7$인 iid Bernoulli이고 $n=100$이라 하자. 정확도 $\bar X$의 표준오차는

\[
\operatorname{SE}(\bar X)
=\sqrt{\frac{p(1-p)}{n}}
=\sqrt{\frac{0.7\cdot0.3}{100}}
\approx0.0458
\]

이다. 이는 repeated sampling에서 관측 정확도가 population accuracy 주변에서 변하는 scale이다. 실제 분석에서는 모르는 $p$를 관측 비율로 추정할 수 있다.

## 예제 4. 묶인 token을 독립으로 세는 문제

prompt 10개에서 각 100개 token의 attribution을 계산했다고 하자. $n=1000$을 iid sample size로 넣으면 같은 prompt 안의 공통 문맥을 무시한다. prompt별 평균을 분석하거나 cluster를 보존하는 재표집을 사용하면 prompt 수준 변동을 반영할 수 있다. 어떤 방법이 맞는지는 일반화 대상이 token인지 prompt인지에 달려 있다.

## 흔한 오해

### 오해 1. 모집단은 데이터셋보다 큰 유한 목록이다

모집단은 유한 목록으로 정의할 수도 있고 앞으로 관측할 입력을 생성하는 확률분포로 정의할 수도 있다. 연구자가 일반화하려는 대상을 명시해야 한다.

### 오해 2. sample을 한 번 관측하면 표본평균은 더 이상 확률변수가 아니다

관측한 $\bar x$는 고정값이다. 표본평균 통계량 $\bar X$는 가능한 다른 sample까지 고려하면 확률변수이며 sampling distribution을 가진다.

### 오해 3. 원자료가 Gaussian이어야 표본평균을 분석할 수 있다

표본평균의 기댓값과 분산 공식은 iid와 finite variance 조건에서 Gaussian population을 요구하지 않는다. Gaussian 근사를 사용하는 CLT에는 추가 조건과 근사 품질 점검이 필요하다.

### 오해 4. 관측 개수가 많으면 독립 sample size도 크다

같은 prompt, subject나 run 안의 관측은 의존할 수 있다. 독립 단위를 잘못 세면 standard error와 검정 결과가 과도하게 낙관적으로 보일 수 있다.

### 오해 5. sample size가 크면 sampling bias도 사라진다

큰 sample은 같은 sampling mechanism 아래의 무작위 변동을 줄인다. 특정 집단을 빠뜨리거나 선택 기준이 target population과 다르면 표본 수를 늘려도 그 편향은 남을 수 있다.

## 연습문제

### 1. 객체 구분

$X_1,\ldots,X_n$, $x_1,\ldots,x_n$, $\mu$와 $\bar X$를 확률표본, 관측 sample, 모수와 통계량으로 각각 분류하라.

<details>
<summary>해설 보기</summary>

$X_1,\ldots,X_n$은 표본을 뽑기 전의 확률표본이고 $x_1,\ldots,x_n$은 관측한 고정값이다. $\mu$는 population mean이라는 모수이며 $\bar X$는 확률표본의 함수인 통계량이다.

</details>

### 2. 표본 통계량 계산

관측 sample이 $1,3,5,7$이다. $\bar x$와 분모 $n-1$을 사용한 $s^2$을 구하라.

<details>
<summary>해설 보기</summary>

\[
\bar x=\frac{1+3+5+7}{4}=4.
\]

제곱편차 합은 $9+1+1+9=20$이므로

\[
s^2=\frac{20}{4-1}=\frac{20}{3}.
\]

</details>

### 3. 표본평균의 평균과 분산

iid 표본의 population mean이 $10$, variance가 $9$이고 $n=36$이다. $\mathbb E[\bar X]$, $\operatorname{Var}(\bar X)$와 $\operatorname{SE}(\bar X)$를 구하라.

<details>
<summary>해설 보기</summary>

\[
\mathbb E[\bar X]=10,
\qquad
\operatorname{Var}(\bar X)=\frac9{36}=\frac14,
\]

\[
\operatorname{SE}(\bar X)=\sqrt{\frac14}=\frac12.
\]

</details>

### 4. sampling distribution 열거

$X_1,X_2\overset{\mathrm{iid}}{\sim}\operatorname{Bernoulli}(0.25)$이다. $\bar X$가 가질 수 있는 값과 각 확률을 구하라.

<details>
<summary>해설 보기</summary>

$\bar X$의 가능한 값은 $0,1/2,1$이다.

\[
P(\bar X=0)=(0.75)^2=0.5625,
\]

\[
P\left(\bar X=\frac12\right)
=2(0.25)(0.75)=0.375,
\]

\[
P(\bar X=1)=(0.25)^2=0.0625.
\]

세 확률의 합은 1이다.

</details>

### 5. sample size와 표준오차

population standard deviation이 $12$이다. 표본평균의 표준오차를 3 이하로 만들기 위한 iid sample size의 최솟값을 구하라.

<details>
<summary>해설 보기</summary>

\[
\frac{12}{\sqrt n}\le3
\]

이어야 한다. 따라서 $\sqrt n\ge4$이고 $n\ge16$이다. 최솟값은 16이다.

</details>

### 6. iid 가정 점검

한 환자의 의료영상 500장을 잘라 만든 patch 50,000개를 독립 sample로 처리했다. 어떤 의존성이 생길 수 있으며 불확실성 평가를 어떻게 바꿔야 하는지 설명하라.

<details>
<summary>해설 보기</summary>

같은 환자의 patch는 해부학적 특성, 촬영 장비와 전처리를 공유하므로 강하게 의존할 수 있다. 환자 한 명만 관측했으므로 환자 population에 대한 독립 단위는 50,000개가 아니다. 환자 간 일반화를 평가하려면 여러 환자를 표집하고 환자 수준 분할과 cluster-aware 분석을 사용해야 한다.

</details>

### 7. 모델 해석 주장 비판

한 모델과 prompt 20개에서 attribution 평균이 양수로 관찰됐다. “다른 모델과 모든 prompt에서도 attribution이 양수이다”라는 결론을 평가하고 sampling unit을 제안하라.

<details>
<summary>해설 보기</summary>

관측 결과는 해당 모델과 20개 prompt에서 계산한 표본평균이다. 다른 모델과 prompt population으로 일반화하려면 모델 seed나 checkpoint와 prompt를 표집해야 한다. prompt 안의 token보다 prompt를 기본 cluster로 보고, 연구 질문이 모델 간 변동까지 포함하면 model run도 독립 단위로 설계할 수 있다.

</details>

## 단원 요약

- 모집단은 일반화하려는 대상이며 표본은 그 대상에서 관측한 일부이다.
- iid는 각 관측이 독립이고 같은 population distribution을 따른다는 두 조건을 포함한다.
- 모수는 모집단 특성이고 통계량은 확률표본의 함수이다.
- sampling distribution은 repeated sampling에서 통계량이 갖는 분포이다.
- iid 표본평균의 평균은 $\mu$, 분산은 $\sigma^2/n$, 표준오차는 $\sigma/\sqrt n$이다.
- 중심극한정리는 조건 아래 표본평균의 표준화 분포에 Gaussian 근사를 제공한다.
- 의존 관측을 독립으로 세면 sampling uncertainty를 작게 추정할 수 있다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- 모집단, 확률표본과 관측 sample을 구분할 수 있는가?
- iid의 두 조건을 각각 설명할 수 있는가?
- 모수와 통계량을 예로 구분할 수 있는가?
- 표본평균과 표본분산을 계산할 수 있는가?
- population·empirical·sampling distribution을 구분할 수 있는가?
- 표본평균의 기댓값·분산·표준오차를 계산할 수 있는가?
- 모델 해석 실험의 독립 sampling unit을 제안할 수 있는가?

## 다음 단원

- [M04-07 추정, 편향과 분산](M04-07-estimation-bias-variance.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] 모집단, 확률표본과 관측 sample을 구분했다.
- [x] iid의 독립성과 동일분포 조건을 설명했다.
- [x] 모수와 통계량의 고정·무작위 역할을 구분했다.
- [x] 표본평균·표본분산·경험분포를 정의했다.
- [x] sampling distribution과 표준오차를 계산했다.
- [x] 실험 단위와 의존성의 한계를 밝혔다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 구분자를 확인했다.
