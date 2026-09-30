---
id: "A09-CAU-03"
title: "confounding과 identifiability"
part: 4
stage: "A09-CAU"
status: "완료"
prerequisites: ["M04-02", "M04-16", "A09-CAU-02"]
estimated_time: "90~120분"
---

# A09-CAU-03. confounding과 identifiability

## 이 단원이 필요한 이유

common cause는 treatment와 outcome의 관찰 association에 causal path가 아닌 성분을 만든다. causal estimand를 observational distribution에서 계산하려면 graph와 가정이 identification formula를 허용해야 한다. 내부 activation과 output의 correlation에도 upstream input feature가 common cause로 작용할 수 있다.

## 학습 목표

- confounder, mediator와 collider를 graph에서 구분할 수 있다.
- backdoor adjustment formula를 적용할 수 있다.
- identifiability와 statistical estimation을 구분할 수 있다.
- 내부 intervention에서 direct execution과 observational identification의 역할을 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [M04-02 조건부확률과 Bayes 규칙](../../part-1-foundations/M04/M04-02-conditional-probability-bayes-rule.md), [M04-16 상관관계와 인과관계](../../part-1-foundations/M04/M04-16-correlation-causation.md), [A09-CAU-02 do 연산과 intervention](A09-CAU-02-do-operator-interventions.md)
- 확인 질문: $Z$가 $X$와 $Y$의 common cause이면 $X$와 $Y$ 사이에 어떤 noncausal path가 열리는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $Z\to X$ and $Z\to Y$ | `Z causes both X and Y` | $Z$가 만든 backdoor path | graph pattern |
| $P(y\mid\operatorname{do}(x))$ | `the distribution of y under do x` | 식별하려는 interventional distribution | distribution |
| $\sum_zP(y\mid x,z)P(z)$ | `the sum over z of P y given x z times P z` | discrete backdoor adjustment | probability |
| $Y\perp X\mid Z$ | `Y is independent of X given Z` | conditional independence statement | relation |

## 핵심 개념

$Z\to X$, $Z\to Y$, $X\to Y$ graph에서 path $X\leftarrow Z\to Y$는 causal effect와 observational association을 섞는다. $Z$가 모든 backdoor path를 막고 treatment의 descendant가 아니면

$$
P(y\mid\operatorname{do}(x))
=\sum_z P(y\mid x,z)P(z)
$$

로 causal distribution을 식별할 수 있다. continuous $Z$에서는 합을 적분으로 바꾼다. positivity는 필요한 $z$ stratum에서 treatment 값 $x$가 관찰될 확률이 0이 아니어야 한다는 조건이다.

identifiability는 causal estimand가 observational distribution의 함수로 유일하게 표현되는가를 묻는다. estimation은 finite data에서 그 함수를 얼마나 정확히 계산하는가를 묻는다. sample을 늘려도 graph와 가정이 effect를 식별하지 못하면 문제가 풀리지 않는다.

neural network에서는 같은 input property가 activation $H$와 output $Y$를 함께 결정할 수 있다. $H$–$Y$ correlation만으로 $H$ effect를 식별할 수 없다. model을 직접 실행해 $H$를 intervene하면 지정 internal intervention의 effect를 측정할 수 있지만, prompt population 평균에는 sampling과 interference 가정이 남는다.

## 작은 예제

$P(Z=1)=0.5$이고 $P(Y=1\mid X=x,Z=z)$를 안다고 하자. backdoor adjustment는 두 $z$ stratum의 conditional outcome을 treatment별 observed $P(z\mid x)$가 아니라 population weight $P(z)=0.5$로 평균한다.

## 흔한 오해

- 모든 pre-treatment variable을 조건화하면 되는 것은 아니다. collider conditioning은 path를 열 수 있다.
- graph에서 effect가 identifiable하다는 사실이 estimator의 low variance를 보장하지 않는다.

## 연습문제

### 1. roles
$X\to M\to Y$에서 $M$은 confounder인가 mediator인가?
<details><summary>해설 보기</summary>

$X$의 effect를 $Y$로 전달하는 causal path 위에 있으므로 mediator이다.
</details>

### 2. adjustment
$Z$가 binary일 때 backdoor formula를 두 항으로 펼쳐 쓰라.
<details><summary>해설 보기</summary>

$P(y\mid x,z=0)P(z=0)+P(y\mid x,z=1)P(z=1)$이다.
</details>

### 3. positivity
$Z=1$인 모든 unit에서 $X=1$만 관찰됐다. $Z=1$ stratum의 $X=0$ outcome을 standard adjustment로 추정할 수 있는가?
<details><summary>해설 보기</summary>

없다. 해당 stratum에서 $P(X=0\mid Z=1)=0$이므로 positivity가 깨진다.
</details>

### 4. 모델 해석
country token presence가 head activation과 capital-token logit을 함께 높인다. head의 causal effect를 확인하려면 무엇을 하는가?
<details><summary>해설 보기</summary>

country token 조건을 matched control로 고정하고 head activation을 ablate·patch해 logit effect를 측정한다. 관찰 correlation과 intervention effect를 따로 보고한다.
</details>

## 근거와 갱신 경계

backdoor adjustment는 causal graph가 맞고 adjustment set이 충분하다는 가정에 의존한다. do-calculus의 완전한 identification algorithm은 다루지 않는다.

## 단원 요약

- confounding은 treatment와 outcome의 common cause가 만든다.
- backdoor set은 noncausal path를 막아 adjustment formula를 제공한다.
- identifiability는 infinite data 이전의 구조 문제이다.
- executable internal intervention도 population과 조작 타당성 가정을 필요로 한다.

## 통과 기준

- graph에서 confounder·mediator·collider를 구분할 수 있는가?
- identification과 finite-sample estimation을 구분할 수 있는가?

## 다음 단원

- [A09-CAU-04 mediation의 가정](A09-CAU-04-mediation-assumptions.md)

## 집필자 점검표

- [x] confounding·backdoor·identifiability와 내부 개입을 연결했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
