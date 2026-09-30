---
id: "I07-17"
title: "종합 실습: 작은 circuit"
part: 3
stage: "I07"
status: "완료"
prerequisites: ["I07-16"]
estimated_time: "180~240분"
---

# I07-17. 종합 실습: 작은 circuit

## 이 단원이 필요한 이유

귀인 heatmap, patch effect와 component 목록을 따로 모아서는 circuit 보고서가 되지 않는다. 하나의 행동을 정의하고 node·edge 가설, discovery, necessity·sufficiency, off-manifold 진단, 대조군과 통계를 한 계약으로 연결해야 한다. 이 단원은 I07 전체를 재현 가능한 작은 circuit 보고서로 묶는다.

## 학습 목표

- 행동·입력 모집단·outcome을 사전 정의할 수 있다.
- node·edge graph와 각 개입의 estimand를 연결할 수 있다.
- necessity·sufficiency·faithfulness 검사를 held-out 데이터에 적용할 수 있다.
- 결과와 한계를 manifest·표·bounded claim으로 보고할 수 있다.

## 선수지식 확인

- 선수 단원: [I07-16 CoT faithfulness 평가](I07-16-cot-faithfulness.md)
- 확인 질문: discovery set에서 고른 peak effect를 같은 데이터의 confirmatory effect로 쓰면 왜 과대평가되는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $G_C=(V_C,E_C)$ | `G sub C equals V sub C E sub C` | 후보 circuit graph | directed graph |
| $m(x)$ | `m of x` | 행동 outcome | scalar |
| $N_C$ | `N sub C` | circuit necessity effect | scalar |
| $S_C$ | `S sub C` | circuit sufficiency effect | scalar |
| $F_C$ | `F sub C` | circuit-only faithfulness score | scalar |
| claim ledger | `claim ledger` | 증거·control·범위를 잇는 표 | report artifact |

## 1. 보고서 질문

예시 질문은 다음 형식을 따른다.

> 고정된 입력 모집단에서 target-minus-foil logit을 만드는 데 후보 copy path와 gate path가 기능적으로 관여하는가?

행동 성공률만 쓰지 않고 연속 logit metric, 포함·제외 기준과 experimental unit을 함께 적는다.

## 2. 단계별 계약

### A. 행동과 데이터

- 입력 source, group과 held-out split
- target·foil tokenization
- primary outcome과 실패 threshold
- 독립 experimental unit

### B. 후보 발견

- gradient·perturbation은 search 도구로 사용
- activation tracing으로 node 후보 선택
- path patching으로 edge 후보 선택
- discovery 데이터 밖에서 후보를 바꾸지 않음

### C. circuit 검증

- necessity: intact에서 $C$ 제거
- sufficiency: 사전 정의 baseline에 $C$ 복원
- faithfulness: $C$만 유지한 계산과 intact 비교
- minimality: node·edge를 하나씩 제거
- off-manifold distance와 matched control

### D. 통계와 주장

- unit별 paired effect와 interval
- random graph·magnitude-matched control
- 탐색 family와 multiplicity 처리
- 성공·실패한 gate 모두 보고
- 지원되는 입력·모델 범위만 claim에 포함

## 3. 합성 circuit

CPU 실습의 행동은

$$
m(x)=x_0+x_0x_1
$$

이다. Copy path는 $x_0$, gate path는 $x_0x_1$을 전달한다. 두 path의 합이 정의한 전체 그래프를 정확히 재현하지만, 이는 구조를 알고 만든 합성 예제의 ground truth다.

<!-- I07_EXAMPLE: i07_17_circuit_report -->

64개 독립 합성 입력에서 copy·gate·joint ablation과 random control을 계산한다. 결론은 이 합성 행동의 두 지정 경로가 인과적으로 관여한다는 범위로 제한한다.

## 4. Pythia 파일럿 연결

I07-07의 Pythia 결과는 실제 모델 개입 pipeline을 검증한다. Layer 5 MLP patch recovery 0.0625만으로 작은 circuit을 발견했다고 하지 않는다. 실제 circuit 연구로 확장하려면 다음이 추가로 필요하다.

- 여러 독립 prompt pair와 held-out split
- layer·token discovery와 confirmatory 분리
- attention·MLP node와 edge별 patch
- necessity·sufficiency와 random graph control
- manifold 진단, bootstrap interval과 실패 사례

## 5. claim ledger

| 증거 | 직접 지원하는 주장 | 아직 지원하지 않는 주장 |
|---|---|---|
| gradient·DLA | target score와의 국소·직접 정렬 | component necessity |
| activation patch | 지정 patch의 국소 causal effect | 유일한 저장 위치 |
| ablation | 지정 baseline 아래 necessity | sufficiency |
| restore | 지정 baseline 아래 sufficiency | 다른 입력 일반화 |
| held-out paired test | 입력 모집단 안의 반복성 | 다른 모델 일반화 |

## 흔한 오해

### 오해 1. 여러 방법이 같은 component를 고르면 circuit이 증명된다

방법들이 같은 metric과 corruption을 공유하면 오류도 공유할 수 있다. 독립 control과 held-out 개입이 필요하다.

### 오해 2. synthetic ground truth에서 맞았으니 실제 모델도 맞다

합성 예제는 구현 검산이다. 실제 모델의 분산 표현, 중복과 off-manifold 문제를 제거하지 않는다.

## 연습문제

### 1. 행동 정의

“복사 회로를 찾는다”를 관찰 가능한 질문으로 바꿔라.

<details>
<summary>해설 보기</summary>

예: 고정된 repeated-token prompt 모집단에서 source token과 같은 next token의 target-minus-foil logit을 높이는 node·edge 집합을 찾고 held-out prompt에서 검증한다고 쓴다.

</details>

### 2. node와 edge

Copy head를 node로 제안했다. edge 가설에 더 필요한 것은 무엇인가?

<details>
<summary>해설 보기</summary>

어느 source token의 어떤 head output이 어떤 receiver의 Q·K·V 또는 residual 입력으로 전달되는지 명시한다.

</details>

### 3. necessity·sufficiency

후보를 ablate하면 metric이 떨어지지만 empty baseline에 후보만 복원해도 회복되지 않았다. 무엇을 뜻하는가?

<details>
<summary>해설 보기</summary>

정의한 조건에서 necessity 증거는 있지만 단독 sufficiency 증거는 없다. 다른 보조 component가 필요할 수 있다.

</details>

### 4. control 실패

후보 graph와 random graph의 effect가 비슷했다. 보고서 결론은 어떻게 바뀌는가?

<details>
<summary>해설 보기</summary>

제안 graph의 특이성이 입증되지 않았다고 쓴다. 탐색 규칙이나 개입 규모가 일반적인 교란을 고른 가능성을 검토한다.

</details>

### 5. held-out 실패

Discovery prompt에서는 effect가 컸지만 held-out에서는 0에 가까웠다. 정당한 결론을 써라.

<details>
<summary>해설 보기</summary>

후보가 discovery 표본에는 맞았지만 사전 정의한 모집단으로 일반화되지 않았다고 쓴다. 최종 circuit 주장 조건을 통과하지 못했다.

</details>

### 6. 최종 claim

필요성·충분성·held-out control을 모두 통과했을 때도 남겨야 할 범위 제한 세 가지를 적어라.

<details>
<summary>해설 보기</summary>

모델 revision, 입력 모집단과 행동 metric, 사용한 ablation·restore baseline을 남긴다. Graph가 유일하거나 모든 모델에 일반화된다는 주장은 별도다.

</details>

## 근거와 갱신 경계

End-to-end circuit의 faithfulness·completeness·minimality 평가는 [Wang et al. (2022)](https://arxiv.org/abs/2211.00593), patching 설계 민감성은 [Zhang and Nanda (2023)](https://arxiv.org/abs/2309.16042)을 기준으로 한다. 새로운 자동 circuit discovery 방법이 나와도 이 보고서 gate를 생략하지 않는다.

## 단원 요약

- 작은 circuit 보고서는 행동, graph, 개입, control과 통계를 한 계약으로 연결한다.
- 귀인·localization은 discovery이고 necessity·sufficiency·held-out 검증이 뒤따른다.
- Off-manifold 진단과 random graph control이 개입 특이성을 제한한다.
- 실제 모델 claim은 model revision·입력·metric·baseline 범위에 묶인다.

## 통과 기준

- 행동부터 circuit graph까지 재현 가능한 계획을 쓸 수 있는가?
- necessity·sufficiency·faithfulness gate를 구분할 수 있는가?
- 실패한 control과 held-out 결과를 포함해 bounded claim을 쓸 수 있는가?

## 다음 단계

I08에서는 여러 checkpoint를 비교해 feature와 행동이 언제 형성되는지 추적한다.

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] 행동·node·edge·개입·control·통계를 연결했다.
- [x] necessity·sufficiency·faithfulness를 구분했다.
- [x] off-manifold와 held-out failure gate를 포함했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
