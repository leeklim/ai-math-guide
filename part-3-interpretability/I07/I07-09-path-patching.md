---
id: "I07-09"
title: "path patching"
part: 3
stage: "I07"
status: "완료"
prerequisites: ["I07-08"]
estimated_time: "120~150분"
---

# I07-09. path patching

## 이 단원이 필요한 이유

Node patching은 한 component의 출력이 가는 모든 downstream 경로를 함께 바꾼다. Path patching은 sender에서 특정 receiver로 전달되는 edge 또는 제한된 경로만 바꾸어 직접 효과를 분리하려 한다. 어떤 edge를 열고 나머지를 어느 실행 값으로 고정했는지 명시하지 않으면 결과를 재현할 수 없다.

## 학습 목표

- node intervention과 edge intervention을 구분할 수 있다.
- 간단한 DAG에서 total effect와 특정 path effect를 계산할 수 있다.
- sender·receiver·source·base 조건을 포함한 계약을 쓸 수 있다.
- path effect를 회로의 완전한 설명으로 과장하지 않을 수 있다.

## 선수지식 확인

- 선수 단원: [I07-08 causal tracing](I07-08-causal-tracing.md)
- 확인 질문: 한 node를 patch하면 그 node에서 나가는 여러 downstream 경로가 함께 바뀌는 이유는 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $A\to B$ | `A to B` | sender $A$에서 receiver $B$로 가는 edge | directed edge |
| $Y_{A\to B\leftarrow a^*}$ | `Y with the A to B edge set to a star` | 특정 edge message를 바꾼 outcome | scalar |
| total effect | `total effect` | node에서 나가는 모든 경로를 통한 효과 | scalar |
| direct path effect | `direct path effect` | 선택 edge·path만을 통한 효과 | scalar |
| sender·receiver | `sender and receiver` | message를 보내고 받는 component | graph nodes |

## 1. node와 edge 개입

$A$가 $B$와 $C$로 가고 $C$도 $B$로 가는 그래프를 생각한다. $A$ node 전체를 clean 값으로 바꾸면 $A\to B$와 $A\to C\to B$가 모두 변한다. $A\to B$ message만 바꾸면 간접 경로는 base 값으로 유지된다.

$$
\Delta_{A\to B}
=
Y\bigl(do(M_{A\to B}=M_{A\to B}^{c})\bigr)-Y_r.
$$

여기서 다른 edge의 message는 어느 실행 값으로 고정했는지 계약에 적어야 한다.

## 2. Transformer의 edge

Residual stream은 여러 component 출력의 합이다. sender head의 output을 receiver의 Q·K·V 또는 MLP 입력에 전달하는 경로를 분리하려면 sender output을 받는 다른 receiver를 freeze하거나 recompute하는 규칙이 필요하다. 구현에 따라 “path patching”이 나타내는 counterfactual이 달라질 수 있다.

## 3. 회로 탐색과 검증

많은 edge 중 큰 효과를 고르는 것은 discovery다. 고정된 edge 집합의 faithfulness, completeness와 minimality는 별도 입력에서 평가한다. edge 하나의 큰 효과만으로 회로가 완성됐다고 하지 않는다.

## 4. CPU 실습

<!-- I07_EXAMPLE: i07_09_path_patching -->

$A\to B$의 직접 계수는 3, $A\to C\to B$의 간접 계수는 $2\times5=10$이다. edge patch는 직접 경로만, node patch는 둘 다 바꾸므로 효과가 다르다.

## 흔한 오해

### 오해 1. path effect는 고유한 값이다

상호작용이 있는 비선형 그래프에서는 다른 경로를 어느 조건에 고정하는지에 따라 값이 달라진다.

### 오해 2. 큰 edge 몇 개면 circuit이 완성된다

누락 edge, 중복 경로와 입력별 다른 전략을 검사해야 한다.

## 연습문제

### 1. 직접·간접 계수

$C=2A$, $B=3A+5C$에서 $A$가 $B$에 미치는 직접 계수와 총 계수를 구하라.

<details>
<summary>해설 보기</summary>

직접 계수는 3이다. 간접 계수는 $2\times5=10$이고 총 계수는 13이다.

</details>

### 2. edge patch

base $A=-1$, source $A=2$일 때 $A\to B$ edge만 source 값으로 바꾸면 $B$가 얼마나 변하는가?

<details>
<summary>해설 보기</summary>

edge message 변화는 $2-(-1)=3$이고 직접 계수는 3이므로 $B$는 9 변한다. $C$ 경로는 base에 고정한다.

</details>

### 3. node patch

같은 조건에서 $A$ node 전체를 source 값으로 바꾸면 $B$ 변화는 얼마인가?

<details>
<summary>해설 보기</summary>

총 계수 13에 입력 변화 3을 곱해 39이다. 직접·간접 경로가 모두 바뀐다.

</details>

### 4. 계약 항목

path patch 실험에서 sender와 receiver 외에 고정해야 할 세 항목을 적어라.

<details>
<summary>해설 보기</summary>

source와 base 입력, 다른 edge의 freeze·recompute 규칙, outcome metric을 고정한다. layer·token 위치도 필요하다.

</details>

### 5. 비선형성

receiver가 ReLU를 포함하면 path effect가 base 조건에 의존하는 이유는 무엇인가?

<details>
<summary>해설 보기</summary>

다른 경로의 합이 ReLU threshold 어느 쪽에 있는지에 따라 같은 edge message도 출력에 미치는 효과가 달라진다.

</details>

### 6. 회로 주장

한 edge의 held-out 효과가 반복됐다. 무엇을 추가해야 완전한 circuit 주장에 가까워지는가?

<details>
<summary>해설 보기</summary>

후보 edge 집합을 함께 유지했을 때 행동을 재현하는 faithfulness, 나머지 edge를 제거해도 되는 completeness와 불필요 edge를 뺀 minimality를 평가한다.

</details>

## 근거와 갱신 경계

Transformer의 edge-level intervention과 회로 검증 사례는 [Wang et al. (2022)](https://arxiv.org/abs/2211.00593)을 기준으로 한다. 구현별 freeze 규칙이 다를 수 있으므로 논문 이름만으로 같은 estimand라고 가정하지 않는다.

## 단원 요약

- node patch는 모든 downstream 경로를, path patch는 선택 edge·경로를 바꾼다.
- 다른 경로를 어느 조건에 고정하는지가 path effect를 결정한다.
- 비선형 상호작용 때문에 path effect는 base 조건에 의존할 수 있다.
- edge discovery와 circuit 검증은 별도 단계다.

## 통과 기준

- 작은 DAG의 direct·total effect를 계산할 수 있는가?
- path patch 계약을 작성할 수 있는가?
- 큰 edge 효과와 완전한 circuit 주장을 구분할 수 있는가?

## 다음 단원

- [I07-10 residual·logit attribution](I07-10-residual-logit-attribution.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] node·edge intervention을 구분했다.
- [x] freeze 규칙과 비선형성 한계를 포함했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
