---
id: "A09-CAU-04"
title: "mediation의 가정"
part: 4
stage: "A09-CAU"
status: "완료"
prerequisites: ["M04-16", "I07-13", "A09-CAU-03"]
estimated_time: "90~120분"
---

# A09-CAU-04. mediation의 가정

## 이 단원이 필요한 이유

treatment effect가 내부 component를 거쳐 전달된다고 주장하려면 total effect와 direct·indirect effect를 정의해야 한다. mediator를 conditioning하는 회귀계수만으로 path-specific causal effect가 나오지 않는다. natural effect는 서로 다른 intervention world의 potential outcome을 함께 사용하므로 강한 가정을 요구한다.

## 학습 목표

- total, natural direct와 natural indirect effect를 potential outcome으로 쓸 수 있다.
- mediator conditioning과 mediator intervention을 구분할 수 있다.
- natural effect identification에 필요한 가정을 설명할 수 있다.
- neural mediation 결과에서 interaction과 off-manifold 문제를 진단할 수 있다.

## 선수지식 확인

- 선수 단원: [M04-16 상관관계와 인과관계](../../part-1-foundations/M04/M04-16-correlation-causation.md), [I07-13 mediation과 counterfactual](../../part-3-interpretability/I07/I07-13-mediation-counterfactual.md), [A09-CAU-03 confounding과 identifiability](A09-CAU-03-confounding-identifiability.md)
- 확인 질문: $A\to M\to Y$에서 $M$을 관찰값으로 조건화하는 것과 $M$ equation을 바꾸는 것은 왜 다른가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $M(a)$ | `M under treatment a` | treatment $a$ 아래 mediator potential outcome | mediator-valued |
| $Y(a,m)$ | `Y under treatment a and mediator m` | treatment와 mediator를 함께 정한 outcome | outcome-valued |
| $\operatorname{NDE}$ | `the natural direct effect` | mediator를 baseline world에 둔 direct effect | scalar expectation |
| $\operatorname{NIE}$ | `the natural indirect effect` | treatment를 고정하고 mediator world를 바꾼 effect | scalar expectation |

## 핵심 개념

binary treatment $A\in\{0,1\}$, mediator $M$, outcome $Y$를 생각한다. total effect는

$$
\operatorname{TE}
=E[Y(1,M(1))-Y(0,M(0))]
$$

이다. 한 가지 compatible decomposition은

$$
\operatorname{NDE}
=E[Y(1,M(0))-Y(0,M(0))],
$$

$$
\operatorname{NIE}
=E[Y(1,M(1))-Y(1,M(0))]
$$

이며 이 정의에서는 $\operatorname{TE}=\operatorname{NDE}+\operatorname{NIE}$이다. $Y(1,M(0))$는 treatment 1 world의 outcome에 treatment 0 world의 mediator를 넣는 cross-world counterfactual이다.

observational data에서 natural effect를 식별하려면 consistency와 positivity 외에 treatment–outcome, treatment–mediator, mediator–outcome 관계의 충분한 confounder control이 필요하다. treatment가 만든 mediator–outcome confounder가 있으면 standard mediation formula가 실패할 수 있다.

neural network에서 source prompt의 activation $M(0)$을 target computation에 patch하면 cross-world 조합을 실행할 수 있다. 이 state가 target context의 upstream·downstream relation과 맞지 않으면 off-manifold artifact가 생긴다. mediator set, source pairing과 normalization을 control해야 한다.

## 작은 예제

$Y(a,m)=a+2m$, $M(a)=a$이면 $\operatorname{TE}=3$, $\operatorname{NDE}=1$, $\operatorname{NIE}=2$이다. treatment–mediator interaction이 없어서 decomposition이 간단하다.

## 흔한 오해

- mediator를 regression covariate로 넣은 뒤 treatment coefficient가 direct effect가 되는 것은 아니다.
- indirect effect가 크다는 사실만으로 mediator가 유일한 mechanism이라고 말할 수 없다.

## 연습문제

### 1. effects
$Y(a,m)=2a+m$, $M(0)=1$, $M(1)=4$일 때 TE, NDE와 NIE를 구하라.
<details><summary>해설 보기</summary>

TE는 $Y(1,4)-Y(0,1)=6-1=5$, NDE는 $Y(1,1)-Y(0,1)=3-1=2$, NIE는 $Y(1,4)-Y(1,1)=6-3=3$이다.
</details>

### 2. cross-world
$Y(1,M(0))$가 cross-world quantity인 이유는 무엇인가?
<details><summary>해설 보기</summary>

treatment 1 아래 outcome equation에 treatment 0 아래 생성됐을 mediator value를 함께 사용하기 때문이다.
</details>

### 3. confounding
unobserved $Z$가 $M$과 $Y$를 함께 만든다면 mediator–outcome effect를 regression으로 식별할 수 있는가?
<details><summary>해설 보기</summary>

일반적으로 식별할 수 없다. $Z$를 충분히 control하거나 다른 identification 설계가 필요하다.
</details>

### 4. 모델 해석
single-head patch가 total logit effect의 70%를 복원했다. 무엇을 추가로 확인해야 mediation claim을 강화할 수 있는가?
<details><summary>해설 보기</summary>

source·target pairing, matched random-head patch, mediator interaction, off-manifold 진단과 다른 path를 함께 patch했을 때의 nonadditivity를 확인한다.
</details>

## 근거와 갱신 경계

natural effect notation은 binary treatment와 한 mediator를 기준으로 한다. stochastic intervention effect와 여러 mediator의 general identification은 다루지 않는다.

## 단원 요약

- total effect는 treatment world 전체의 outcome 차이이다.
- natural direct·indirect effect는 cross-world mediator value를 사용한다.
- mediation identification은 여러 no-confounding 가정을 요구한다.
- 내부 patching은 cross-world quantity를 실행해도 조작 타당성을 자동 보장하지 않는다.

## 통과 기준

- TE, NDE와 NIE를 potential outcome으로 계산할 수 있는가?
- neural mediation claim의 confounding·interaction·off-manifold 한계를 적을 수 있는가?

## 다음 단원

- [A09-CAU-05 counterfactual과 potential outcome](A09-CAU-05-counterfactual-potential-outcomes.md)

## 집필자 점검표

- [x] natural effect 정의와 cross-world identification 가정을 설명했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
