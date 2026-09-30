---
id: "A09-CAU-07"
title: "내부 개입의 외적 타당성"
part: 4
stage: "A09-CAU"
status: "완료"
prerequisites: ["M04-17", "I07-14", "I07-15", "A09-CAU-05"]
estimated_time: "90~120분"
---

# A09-CAU-07. 내부 개입의 외적 타당성

## 이 단원이 필요한 이유

한 prompt template와 model checkpoint에서 측정한 내부 intervention effect는 그 실험 population에 대한 결과이다. 다른 prompt, language, model seed나 architecture로 효과를 옮기려면 effect heterogeneity와 support overlap을 검사해야 한다. model 내부 인과효과를 인간의 reasoning mechanism으로 확장하는 주장에는 별도의 연결 가정이 필요하다.

## 학습 목표

- source population effect와 target population effect를 구분할 수 있다.
- covariate shift 아래 transport weighting의 조건을 설명할 수 있다.
- prompt·seed·checkpoint에 따른 effect heterogeneity를 분석할 수 있다.
- 내부 개입 결과가 허용하는 외적 claim의 범위를 정할 수 있다.

## 선수지식 확인

- 선수 단원: [M04-17 실험 설계와 재현성](../../part-1-foundations/M04/M04-17-experimental-design-reproducibility.md), [I07-14 off-manifold intervention](../../part-3-interpretability/I07/I07-14-off-manifold-intervention.md), [I07-15 대조군과 통계 검증](../../part-3-interpretability/I07/I07-15-controls-statistical-validation.md), [A09-CAU-05 counterfactual과 potential outcome](A09-CAU-05-counterfactual-potential-outcomes.md)
- 확인 질문: average intervention effect가 같은 두 dataset에서도 subgroup effect가 다를 수 있는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $P_S$ | `the source population P S` | intervention을 실행한 source distribution | distribution |
| $P_T$ | `the target population P T` | claim을 옮기려는 target distribution | distribution |
| $\tau(x)$ | `tau of x` | context $x$에서의 conditional intervention effect | scalar or vector contrast |
| $w(x)=p_T(x)/p_S(x)$ | `w of x equals p T of x over p S of x` | covariate-shift transport weight | nonnegative scalar |

## 핵심 개념

source와 target population의 average effect를

$$
\tau_S=E_{X\sim P_S}[Y^1-Y^0],
\qquad
\tau_T=E_{X\sim P_T}[Y^1-Y^0]
$$

로 구분한다. conditional effect $\tau(x)$가 population 사이에서 유지되고 target support가 source support 안에 있으면 covariate shift 아래

$$
\tau_T=E_{P_S}[w(X)\tau(X)],
\qquad
w(x)=\frac{p_T(x)}{p_S(x)}
$$

처럼 reweight할 수 있다. 큰 weight는 overlap 부족과 높은 variance를 알린다.

내부 intervention에서는 prompt topic, syntax, token position, layer와 baseline value가 effect modifier가 될 수 있다. model seed·checkpoint가 바뀌면 node correspondence도 다시 정의해야 한다. neuron index를 그대로 맞추는 대신 function, subspace나 circuit role을 alignment 기준으로 쓸 수 있다.

외적 타당성은 단계별로 확장한다. 같은 template의 held-out prompt, 새 template, 새 data domain, 새 seed, 새 architecture 순으로 transfer를 검사한다. neural intervention effect가 human cognition이나 사회적 outcome에 같은 mechanism으로 작용한다는 결론에는 별도 empirical bridge가 필요하다.

## 작은 예제

template A에서 head ablation의 평균 logit effect가 1.2이고 template B에서 0.1이면 pooled average만 보고하지 않는다. template별 effect와 interaction interval을 제시하고 target population의 template mixture를 명시한다.

## 흔한 오해

- 여러 prompt를 썼다는 사실만으로 target domain 전체의 대표성이 확보되지는 않는다.
- 같은 architecture의 다른 seed에서 neuron index가 같다고 causal role이 대응하는 것은 아니다.

## 연습문제

### 1. transport
$P_S$에서 두 context effect가 $(1,3)$이고 target weight가 normalized $(0.25,0.75)$이면 target average effect는 얼마인가?
<details><summary>해설 보기</summary>

$0.25(1)+0.75(3)=2.5$이다.
</details>

### 2. positivity
target에만 있는 language가 source experiment에 전혀 없으면 weighting으로 transport할 수 있는가?
<details><summary>해설 보기</summary>

없다. target support가 source support 밖에 있어 positivity가 깨진다.
</details>

### 3. heterogeneity
overall effect가 0이지만 두 template effect가 $+2$와 $-2$이다. 무엇을 보고해야 하는가?
<details><summary>해설 보기</summary>

template별 effect와 target mixture를 보고한다. pooled zero를 effect 부재로 해석하지 않는다.
</details>

### 4. 모델 해석
한 model seed의 head 7이 필요하다는 결과를 다른 seed로 옮길 때 어떤 correspondence를 먼저 정하는가?
<details><summary>해설 보기</summary>

activation similarity만이 아니라 input–output role, path effect와 held-out intervention response로 대응 circuit component를 정한다.
</details>

## 근거와 갱신 경계

transport weighting 식은 conditional effect transportability와 covariate shift를 가정한다. selection diagram과 general transport formula는 다루지 않는다.

## 단원 요약

- causal effect는 source population과 intervention policy에 상대적이다.
- transport에는 support overlap과 effect stability가 필요하다.
- prompt·template·seed·checkpoint는 effect modifier가 될 수 있다.
- model 내부 effect를 인간 수준 mechanism으로 옮기려면 별도 증거가 필요하다.

## 통과 기준

- source·target effect와 transport 가정을 적을 수 있는가?
- 내부 개입 claim을 확인한 domain과 model 범위에 한정할 수 있는가?

## 다음 단원

- [A09-CAU-08 종합 실습: circuit 수준 인과 주장](A09-CAU-08-capstone-circuit-causal-claims.md)

## 집필자 점검표

- [x] population transport·effect heterogeneity·model correspondence를 설명했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
