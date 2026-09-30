---
id: "A09-CAU-01"
title: "구조적 인과모형"
part: 4
stage: "A09-CAU"
status: "완료"
prerequisites: ["M04-02", "M04-16", "I07-11"]
estimated_time: "90~120분"
---

# A09-CAU-01. 구조적 인과모형

## 이 단원이 필요한 이유

correlation graph는 변수 사이의 통계적 연결을 그리지만 개입 결과를 정하지 않는다. structural causal model은 각 endogenous variable을 부모와 exogenous noise의 함수로 정의한다. model circuit에 causal language를 쓰려면 node, equation과 intervention target을 먼저 고정해야 한다.

## 학습 목표

- SCM의 exogenous variable, endogenous variable과 structural equation을 구분할 수 있다.
- structural equation에서 causal graph를 그릴 수 있다.
- observational distribution이 equation과 noise distribution에서 생성되는 방식을 설명할 수 있다.
- neural network computation graph를 SCM으로 읽을 때 필요한 변수 선택을 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [M04-02 조건부확률과 Bayes 규칙](../../part-1-foundations/M04/M04-02-conditional-probability-bayes-rule.md), [M04-16 상관관계와 인과관계](../../part-1-foundations/M04/M04-16-correlation-causation.md), [I07-11 circuit을 그래프로 표현하기](../../part-3-interpretability/I07/I07-11-circuit-graph.md)
- 확인 질문: joint distribution만 알아도 어떤 equation을 바꾼 intervention 뒤의 distribution이 유일하게 정해지는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\mathcal M=(U,V,F,P_U)$ | `the structural causal model M` | exogenous·endogenous variable, equation과 noise distribution의 묶음 | model object |
| $X=f_X(\operatorname{pa}_X,U_X)$ | `X equals f X of the parents of X and U X` | $X$의 structural equation | assignment |
| $\operatorname{pa}_X$ | `the parents of X` | graph에서 $X$로 직접 들어오는 변수 | set of variables |
| $G_{\mathcal M}$ | `the causal graph induced by M` | structural equation이 정한 directed graph | graph |

## 핵심 개념

SCM $\mathcal M=(U,V,F,P_U)$에서 $U$는 model 밖에서 주어지는 exogenous variable, $V$는 equation으로 정해지는 endogenous variable이다. 각 $X\in V$에는

$$
X=f_X(\operatorname{pa}_X,U_X)
$$

가 있다. $F$는 이 equation들의 집합이고 $P_U$는 exogenous variable의 joint distribution이다. acyclic SCM에서는 topological order대로 equation을 계산해 observational sample을 만든다.

equation $f_X$가 변수 $Z$를 argument로 사용하면 graph에 $Z\to X$ edge를 둔다. graph는 dependence를 요약하지만 함수 형태와 noise distribution 전체를 담지 않는다. 같은 graph도 다른 intervention effect를 만들 수 있다.

feed-forward neural network는 input을 exogenous variable로, activation과 output을 endogenous variable로 두면 deterministic SCM처럼 쓸 수 있다. neuron, head, subspace나 residual component 중 무엇을 node로 삼는지는 연구자가 정한다. node grouping이 바뀌면 허용 intervention과 causal claim도 바뀐다.

## 작은 예제

$$
X=U_X,
\qquad M=2X+U_M,
\qquad Y=M+X+U_Y
$$

이면 graph에는 $X\to M$, $M\to Y$, $X\to Y$가 있다. noise가 독립인지 correlated인지에 따라 observational distribution은 달라진다.

## 흔한 오해

- directed edge를 관찰 correlation에서 자동으로 읽을 수는 없다.
- computation graph edge가 있다고 그 component가 human-level concept의 원인이라는 뜻은 아니다.

## 연습문제

### 1. graph
$A=U_A$, $B=A+U_B$, $C=AB+U_C$에서 directed edge를 쓰라.
<details><summary>해설 보기</summary>

$A\to B$, $A\to C$, $B\to C$이다.
</details>

### 2. exogenous
위 model에서 $U_A,U_B,U_C$와 $A,B,C$ 중 endogenous variable은 무엇인가?
<details><summary>해설 보기</summary>

structural equation으로 정해지는 $A,B,C$가 endogenous variable이다.
</details>

### 3. same graph
두 SCM이 같은 graph를 가지면 intervention effect의 수치도 같은가?
<details><summary>해설 보기</summary>

같지 않을 수 있다. structural function과 exogenous distribution이 다르면 effect 크기와 형태가 달라진다.
</details>

### 4. 모델 해석
attention head 하나를 causal node로 정의하려면 어떤 output과 downstream edge를 명시해야 하는가?
<details><summary>해설 보기</summary>

어느 token position의 head output인지, residual stream에 더해지는 vector인지와 어떤 downstream computation을 결과로 측정하는지 명시한다.
</details>

## 근거와 갱신 경계

이 단원은 acyclic SCM을 사용한다. cyclic equilibrium model과 latent variable identification의 정밀 이론은 뒤 범위에 포함하지 않는다.

## 단원 요약

- SCM은 variable, structural equation과 exogenous distribution을 묶는다.
- causal graph는 equation의 parent relation을 나타낸다.
- observational distribution만으로 equation replacement 결과가 자동 정해지지 않는다.
- neural circuit의 causal node는 분석 목적에 맞게 정의해야 한다.

## 통과 기준

- equation에서 graph와 variable type을 구분할 수 있는가?
- 내부 component를 causal node로 삼을 때 조작 단위를 적을 수 있는가?

## 다음 단원

- [A09-CAU-02 do 연산과 intervention](A09-CAU-02-do-operator-interventions.md)

## 집필자 점검표

- [x] SCM의 변수·equation·graph와 내부 node 선택을 설명했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
