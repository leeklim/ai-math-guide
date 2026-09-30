---
id: "A09-RMT-04"
title: "Marchenko–Pastur 법칙의 직관"
part: 4
stage: "A09-RMT"
status: "완료"
prerequisites: ["M04-05", "A09-RMT-03"]
estimated_time: "90~120분"
---

# A09-RMT-04. Marchenko–Pastur 법칙의 직관

## 이 단원이 필요한 이유

identity population covariance에서 얻은 sample eigenvalue도 하나의 값에 모이지 않는다. Marchenko–Pastur 법칙은 iid noise matrix의 high-dimensional spectral bulk를 예측한다. 관찰한 activation spectrum에서 눈에 띄는 eigenvalue를 signal로 부르기 전에 이 null bulk와 비교해야 한다.

## 학습 목표

- aspect ratio와 noise variance에서 MP bulk edge를 계산할 수 있다.
- $\gamma>1$일 때 zero eigenvalue가 생기는 이유를 설명할 수 있다.
- MP null의 iid·isotropy·finite-variance 가정을 열거할 수 있다.
- empirical spectrum과 fitted null을 비교하는 한계를 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [M04-05 주요 분포](../../part-1-foundations/M04/M04-05-common-distributions.md), [A09-RMT-03 표본 공분산의 spectrum](A09-RMT-03-sample-covariance-spectrum.md)
- 확인 질문: population covariance가 $\sigma^2I$이면 모든 population eigenvalue는 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\gamma=d/n$ | `gamma equals d over n` | asymptotic aspect ratio | positive scalar |
| $\lambda_-$ | `lambda minus` | MP bulk의 lower edge | nonnegative scalar |
| $\lambda_+$ | `lambda plus` | MP bulk의 upper edge | nonnegative scalar |
| $\sigma^2(1\pm\sqrt\gamma)^2$ | `sigma squared times one plus or minus square root gamma, squared` | isotropic noise의 MP edges | scalar pair |

## 핵심 개념

$X\in\mathbb R^{n\times d}$의 entry가 독립이고 mean 0, variance $\sigma^2$이며 $d/n\to\gamma$라고 하자. normalization $S=X^\top X/n$에서 eigenvalue의 empirical distribution은 조건 아래 Marchenko–Pastur distribution으로 수렴한다. nonzero bulk의 edge는

$$
\lambda_-=\sigma^2(1-\sqrt\gamma)^2,
\qquad
\lambda_+=\sigma^2(1+\sqrt\gamma)^2
$$

이다. population spectrum이 한 점 $\sigma^2$이어도 sample spectrum은 이 interval에 퍼진다.

$\gamma>1$이면 $d>n$이므로 $d\times d$ covariance의 rank가 $n$을 넘지 못한다. asymptotic spectrum에는 비율 $1-1/\gamma$의 zero mass가 생긴다. centering은 finite sample rank를 하나 더 줄일 수 있다.

MP bulk는 reference null이다. activation row의 dependence, unequal feature variance, heavy tails와 low-rank mean structure가 있으면 edge 공식이 맞지 않을 수 있다. empirical variance로 $\sigma^2$를 맞춘 뒤에도 가정 진단과 simulated null을 함께 사용한다.

## 작은 예제

$\sigma^2=1$, $\gamma=0.25$이면 $\sqrt\gamma=0.5$이므로 bulk는 $[0.25,2.25]$이다. noise만 있어도 largest sample eigenvalue가 1보다 훨씬 클 수 있다.

## 흔한 오해

- MP upper edge를 넘은 eigenvalue가 곧 task signal이라는 뜻은 아니다. null misspecification도 outlier를 만든다.
- empirical spectrum에 MP curve를 맞춘 그림만으로 iid 가정이 검증되지는 않는다.

## 연습문제

### 1. edges
$\sigma^2=2$, $\gamma=1$일 때 MP bulk edge를 구하라.
<details><summary>해설 보기</summary>

$\lambda_-=2(1-1)^2=0$, $\lambda_+=2(1+1)^2=8$이다.
</details>

### 2. aspect ratio
$n=400$, $d=100$이면 unit-variance MP upper edge는 얼마인가?
<details><summary>해설 보기</summary>

$\gamma=0.25$이므로 $(1+0.5)^2=2.25$이다.
</details>

### 3. zero mass
$\gamma=2$인 uncentered null covariance에서 asymptotic zero eigenvalue 비율은 얼마인가?
<details><summary>해설 보기</summary>

$1-1/\gamma=1-1/2=0.5$이다.
</details>

### 4. 모델 해석
activation eigenvalue 하나가 fitted MP edge를 조금 넘었다. 어떤 진단을 더 하는가?
<details><summary>해설 보기</summary>

prompt-cluster dependence, feature variance와 tail을 확인하고 matched simulated null, split stability와 bootstrap interval을 함께 계산한다.
</details>

## 근거와 갱신 경계

edge 공식은 iid isotropic finite-variance null과 $1/n$ covariance normalization을 기준으로 한다. finite-size largest-eigenvalue correction과 Tracy–Widom 검정은 다루지 않는다.

## 단원 요약

- isotropic population도 high-dimensional sample에서 spectral bulk를 만든다.
- MP edge는 noise variance와 aspect ratio에 의존한다.
- $d>n$이면 rank deficiency가 zero mass를 만든다.
- MP 비교는 가정을 점검하는 null analysis로 사용한다.

## 통과 기준

- $\sigma^2$와 $\gamma$에서 bulk edge를 계산할 수 있는가?
- MP edge 초과와 task signal을 구분할 수 있는가?

## 다음 단원

- [A09-RMT-05 spiked covariance model](A09-RMT-05-spiked-covariance-model.md)

## 집필자 점검표

- [x] MP bulk edge·zero mass·null 가정을 함께 설명했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
