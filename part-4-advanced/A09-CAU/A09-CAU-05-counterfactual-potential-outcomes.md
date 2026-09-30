---
id: "A09-CAU-05"
title: "counterfactual과 potential outcome"
part: 4
stage: "A09-CAU"
status: "완료"
prerequisites: ["M04-07", "M04-17", "A09-CAU-04"]
estimated_time: "90~120분"
---

# A09-CAU-05. counterfactual과 potential outcome

## 이 단원이 필요한 이유

causal effect는 같은 unit에 서로 다른 treatment를 적용했을 outcome의 차이로 정의하지만 현실에서는 한 world만 관찰한다. model은 같은 stored input에 여러 internal intervention을 실행할 수 있어 paired counterfactual을 계산하기 쉽지만, unit과 intervention이 일관되게 정의됐는지는 별도로 확인해야 한다.

## 학습 목표

- individual treatment effect와 average treatment effect를 쓸 수 있다.
- fundamental problem of causal inference를 설명할 수 있다.
- consistency, no interference와 exchangeability의 역할을 구분할 수 있다.
- SCM counterfactual의 abduction–action–prediction 절차를 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [M04-07 추정, 편향과 분산](../../part-1-foundations/M04/M04-07-estimation-bias-variance.md), [M04-17 실험 설계와 재현성](../../part-1-foundations/M04/M04-17-experimental-design-reproducibility.md), [A09-CAU-04 mediation의 가정](A09-CAU-04-mediation-assumptions.md)
- 확인 질문: 한 사람에게 treatment 0과 1의 outcome을 같은 시점에 모두 관찰할 수 없는 이유는 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $Y_i(1)$ | `the potential outcome for unit i under treatment one` | unit $i$의 treated outcome | scalar or vector |
| $Y_i(0)$ | `the potential outcome for unit i under treatment zero` | unit $i$의 control outcome | scalar or vector |
| $\tau_i=Y_i(1)-Y_i(0)$ | `tau i equals Y i of one minus Y i of zero` | individual treatment effect | scalar or vector contrast |
| $\operatorname{ATE}=E[Y(1)-Y(0)]$ | `the average treatment effect` | population average causal effect | scalar or vector contrast |

## 핵심 개념

unit $i$의 potential outcome을 $Y_i(1)$과 $Y_i(0)$로 정의하면 individual effect는

$$
\tau_i=Y_i(1)-Y_i(0)
$$

이다. 한 unit에서는 둘 중 하나만 관찰하므로 $\tau_i$를 data에서 직접 볼 수 없다. randomized assignment는 treatment group과 control group의 potential outcome distribution을 평균적으로 맞춰 ATE를 추정하게 한다.

consistency는 실제로 $A=a$를 받은 unit의 observed outcome이 $Y(a)$와 같다는 조건이다. no interference는 한 unit의 treatment가 다른 unit의 outcome을 바꾸지 않는다는 조건이다. observational study에서는 measured covariate $Z$를 조건으로 $A\perp(Y(0),Y(1))\mid Z$ 같은 conditional exchangeability를 가정할 수 있다.

SCM counterfactual은 세 단계로 계산한다. abduction에서 observed evidence로 exogenous state를 추론하고, action에서 structural equation을 바꾸며, prediction에서 같은 exogenous state를 유지한 outcome을 계산한다.

deterministic model은 같은 prompt에 두 internal intervention을 실행해 paired outcome을 얻을 수 있다. prompt edit가 semantic content나 token alignment를 바꾸면 같은 unit의 treatment contrast인지 검토해야 한다.

## 작은 예제

10개 prompt마다 ablation 전후 target logit 차이 $\tau_i$를 계산하면 sample ATE는 $\hat\tau=10^{-1}\sum_i\tau_i$이다. token을 독립 unit으로 중복 세지 않고 prompt별 difference를 먼저 만든다.

## 흔한 오해

- model에서 두 forward pass를 실행할 수 있다는 사실이 현실 세계 counterfactual의 식별을 해결하지 않는다.
- average effect가 0이어도 positive·negative individual effect가 상쇄됐을 수 있다.

## 연습문제

### 1. individual effect
$Y_i(1)=5$, $Y_i(0)=2$이면 $\tau_i$를 구하라.
<details><summary>해설 보기</summary>

$\tau_i=5-2=3$이다.
</details>

### 2. ATE
세 unit의 paired effect가 $(2,-1,5)$이면 sample average effect는 얼마인가?
<details><summary>해설 보기</summary>

$(2-1+5)/3=2$이다.
</details>

### 3. interference
한 prompt의 intervention이 batch normalization statistic을 통해 다른 prompt output을 바꾸면 어떤 가정이 깨지는가?
<details><summary>해설 보기</summary>

unit 간 interference가 생긴다. prompt를 독립 unit으로 보는 no-interference 가정이 깨진다.
</details>

### 4. 모델 해석
clean prompt와 corrupted prompt의 token 수가 다르다. paired counterfactual patch를 위해 무엇을 고정해야 하는가?
<details><summary>해설 보기</summary>

unit의 semantic relation, target token position, source–target alignment rule과 outcome definition을 사전에 고정한다.
</details>

## 근거와 갱신 경계

potential outcome 표기는 binary treatment를 중심으로 설명한다. continuous treatment, interference network와 partial identification은 다루지 않는다.

## 단원 요약

- causal effect는 같은 unit의 potential outcome contrast로 정의한다.
- 현실 data에서는 두 potential outcome을 함께 관찰할 수 없다.
- ATE identification은 consistency, assignment와 interference 가정에 의존한다.
- model intervention에서도 unit·pairing·outcome 계약이 필요하다.

## 통과 기준

- individual effect와 ATE를 계산할 수 있는가?
- SCM counterfactual의 세 단계와 paired model intervention의 한계를 설명할 수 있는가?

## 다음 단원

- [A09-CAU-06 causal abstraction](A09-CAU-06-causal-abstraction.md)

## 집필자 점검표

- [x] potential outcome·ATE·SCM counterfactual과 model pairing을 연결했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
