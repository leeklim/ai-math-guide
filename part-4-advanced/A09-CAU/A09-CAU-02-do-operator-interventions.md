---
id: "A09-CAU-02"
title: "do 연산과 intervention"
part: 4
stage: "A09-CAU"
status: "완료"
prerequisites: ["M04-16", "I07-05", "A09-CAU-01"]
estimated_time: "90~120분"
---

# A09-CAU-02. do 연산과 intervention

## 이 단원이 필요한 이유

conditioning은 관찰한 subset을 고르고 intervention은 structural equation을 바꾼다. activation ablation이나 patching을 causal experiment로 해석하려면 어떤 equation을 어떤 값 생성 규칙으로 교체했는지 적어야 한다.

## 학습 목표

- $P(Y\mid X=x)$와 $P(Y\mid\operatorname{do}(X=x))$를 구분할 수 있다.
- surgical intervention을 equation replacement로 표현할 수 있다.
- truncated factorization을 간단한 DAG에 적용할 수 있다.
- activation patching의 intervention policy를 명시할 수 있다.

## 선수지식 확인

- 선수 단원: [M04-16 상관관계와 인과관계](../../part-1-foundations/M04/M04-16-correlation-causation.md), [I07-05 관찰과 개입](../../part-3-interpretability/I07/I07-05-observation-intervention.md), [A09-CAU-01 구조적 인과모형](A09-CAU-01-structural-causal-models.md)
- 확인 질문: $X=x$인 sample만 고르는 일과 모든 unit의 $X$ equation을 constant $x$로 바꾸는 일은 왜 다른가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\operatorname{do}(X=x)$ | `do X equals x` | $X$ equation을 constant $x$로 교체하는 intervention | operation |
| $P(Y\mid\operatorname{do}(X=x))$ | `the distribution of Y under do X equals x` | interventional outcome distribution | probability distribution |
| $\mathcal M_x$ | `the intervened model M x` | $\operatorname{do}(X=x)$를 적용한 SCM | model object |
| $\tau(h\mid s)$ | `the intervention policy tau of h given source s` | source에 따라 activation 값을 정하는 patch policy | map |

## 핵심 개념

intervention $\operatorname{do}(X=x)$는 원래 equation

$$
X=f_X(\operatorname{pa}_X,U_X)
$$

를 $X:=x$로 교체하고 나머지 equation은 유지한다. 따라서 $X$로 들어오던 edge는 잘린다. observational factorization이 $P(v)=\prod_iP(v_i\mid\operatorname{pa}_i)$이면 intervened distribution은

$$
P(v\setminus x\mid\operatorname{do}(x))
=\prod_{i:V_i\ne X}P(v_i\mid\operatorname{pa}_i)
$$

로 factor를 하나 제거한다.

conditioning $P(Y\mid X=x)$는 원래 data-generating process에서 $X=x$를 관찰한 unit을 선택한다. common cause가 있으면 선택된 unit의 background distribution도 달라진다. intervention은 background unit을 유지하고 $X$ mechanism만 바꾼다.

activation patching에서 $H:=h$로 고정할 수도 있고 source prompt $s$에서 얻은 $h(s)$를 넣을 수도 있다. 후자는 $H:=\tau(s)$라는 policy intervention이다. source selection, token alignment와 scale correction도 intervention 정의에 포함한다.

## 작은 예제

$Z=U_Z$, $X=Z+U_X$, $Y=X+Z+U_Y$에서 $X=2$를 관찰하면 $Z$ distribution이 선택된다. $\operatorname{do}(X=2)$에서는 $X$ equation을 끊으므로 $Z$가 원래 marginal distribution을 유지한다.

## 흔한 오해

- activation을 저장해 보는 것은 observation이며 intervention이 아니다.
- 여러 node를 동시에 patch한 효과를 각 node의 개별 effect 합으로 볼 수는 없다.

## 연습문제

### 1. edge removal
$Z\to X$, $Z\to Y$, $X\to Y$ graph에서 $\operatorname{do}(X=x)$ 뒤 제거되는 edge는 무엇인가?
<details><summary>해설 보기</summary>

$X$로 들어오는 $Z\to X$가 제거된다. $X\to Y$와 $Z\to Y$는 유지된다.
</details>

### 2. factorization
$P(z,x,y)=P(z)P(x\mid z)P(y\mid x,z)$에서 $\operatorname{do}(X=x)$ 뒤 factorization을 쓰라.
<details><summary>해설 보기</summary>

$P(z,y\mid\operatorname{do}(x))=P(z)P(y\mid x,z)$이다.
</details>

### 3. policy
clean prompt의 layer 5 activation을 corrupted prompt에 넣는 intervention을 한 줄로 표현하라.
<details><summary>해설 보기</summary>

$H_5(\text{corrupted}):=H_5(\text{clean})$처럼 source와 target을 함께 적는다.
</details>

### 4. 모델 해석
zero ablation과 mean ablation의 effect가 다르면 무엇을 결론내리는가?
<details><summary>해설 보기</summary>

effect가 intervention value에 민감하다는 뜻이다. component의 단일한 causal effect로 합치지 말고 각 intervention policy의 effect를 따로 보고한다.
</details>

## 근거와 갱신 경계

do 연산은 modular structural equation replacement를 가정한다. 실제 neural intervention은 off-manifold state와 downstream normalization을 만들 수 있으므로 조작 타당성을 별도로 진단한다.

## 단원 요약

- conditioning은 unit 선택이고 do intervention은 equation replacement이다.
- surgical intervention은 target node로 들어오는 edge를 끊는다.
- truncated factorization은 intervention target의 conditional factor를 제거한다.
- patching은 source·target·alignment를 포함한 policy로 정의한다.

## 통과 기준

- conditioning과 intervention distribution을 구분할 수 있는가?
- 내부 patch를 재현 가능한 equation replacement로 쓸 수 있는가?

## 다음 단원

- [A09-CAU-03 confounding과 identifiability](A09-CAU-03-confounding-identifiability.md)

## 집필자 점검표

- [x] do 연산·truncated factorization·patch policy를 연결했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
