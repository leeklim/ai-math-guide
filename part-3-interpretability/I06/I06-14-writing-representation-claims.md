---
id: "I06-14"
title: "표현 주장 작성"
part: 3
stage: "I06"
status: "완료"
prerequisites: ["I06-13", "M04-16"]
estimated_time: "90~120분"
---

# I06-14. 표현 주장 작성

## 이 단원이 필요한 이유

같은 결과도 문장 하나 때문에 증거보다 강한 주장으로 바뀔 수 있다. activation 차이, probe, SAE feature와 intervention은 서로 다른 질문에 답한다. 결과·대안 설명·적용 범위를 한 문장 안에서 분리하는 습관이 필요하다.

## 학습 목표

- 관찰, 복원, 사용, 인과와 일반화 주장을 분류할 수 있다.
- evidence ledger에서 허용되는 최대 claim을 정할 수 있다.
- 결과 문장에 대상, 측정, 비교, 불확실성과 범위를 포함할 수 있다.
- 과도한 인과·의인화 표현을 검증 가능한 문장으로 고칠 수 있다.

## 선수지식 확인

- 선수 단원: [I06-13 feature 안정성과 identifiability](I06-13-feature-stability-identifiability.md), [M04-16 상관과 인과](../../part-1-foundations/M04/M04-16-correlation-causation.md)
- 확인 질문: probe가 label을 복원했다는 결과와 model이 label을 사용했다는 결과는 같은가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| evidence ledger | `evidence ledger` | 주장별로 필요한 검사와 결과를 기록한 표 | structured record |
| observational claim | `observational claim` | activation·통계에서 관찰된 차이에 관한 주장 | claim level |
| recoverability claim | `recoverability claim` | decoder가 held-out 자료에서 정보를 읽어낸다는 주장 | claim level |
| functional-use claim | `functional use claim` | model 계산이 그 정보를 이용한다는 주장 | claim level |
| causal claim | `causal claim` | 통제된 개입이 행동 차이를 만들었다는 주장 | claim level |
| generalization scope | `generalization scope` | 결과가 적용된다고 검증한 입력·model·seed 범위 | stated boundary |

## 1. 다섯 단계 주장

| 단계 | 필요한 최소 증거 | 권장 동사 |
|---|---|---|
| 관찰 | 사전 정의 통계와 비교 | `차이가 관찰됐다` |
| 복원 | held-out probe와 control | `선형적으로 복원할 수 있었다` |
| 사용 | downstream 기능 검사 | `model 계산이 이용한다는 증거가 있다` |
| 인과 | 통제된 개입과 대조군 | `개입이 행동값을 변화시켰다` |
| 일반화 | input·seed·checkpoint·model 반복 | `검증한 범위에서 재현됐다` |

아래 단계의 성공이 위 단계를 자동으로 포함하지는 않는다. 예를 들어 개입이 행동을 바꿔도 feature 설명이 틀렸다면 특정 개념의 인과 효과라고 부를 수 없다.

## 2. 결과 문장의 구성

좋은 결과 문장은 다음을 포함한다.

1. model·revision과 dataset
2. layer·token·component
3. 측정량과 대조 조건
4. effect와 uncertainty
5. control·selection 절차
6. 허용되는 해석과 남은 대안

예시는 다음과 같다.

> Pythia-160M `step143000`의 layer 5 MLP update 마지막 token에서 장소·동물 8개 문장의 평균 activation norm 차이를 관찰했다. 이 파일럿은 표본과 형식이 작아 개념의 기능적 사용이나 다른 prompt로의 일반화를 검사하지 않는다.

## 3. 피할 문장 고치기

`model이 도시를 생각하는 neuron을 발견했다`는 문장에는 주체 의인화, neuron-feature 동일시와 발견 범위 누락이 있다. 다음처럼 고친다.

> 고정 dataset에서 coordinate 214의 상위 activation 예에 도시 token이 많이 포함됐다. 별도 hard negative와 개입은 아직 평가하지 않았다.

`SAE가 진짜 feature를 복원했다`도 reconstruction, sparsity와 feature validity를 섞는다.

> SAE는 activation MSE 0.02와 mean $L_0$ 18을 보였다. latent 설명의 sensitivity·specificity와 seed 안정성은 별도 평가가 필요하다.

## 4. negative result도 쓴다

probe control이 높거나 feature matching이 불안정한 결과는 삭제할 실패가 아니다. 가능한 결론의 상한을 낮춘다. 사전 기준, 제외와 중단 규칙을 공개하면 선택적 보고를 줄인다.

## CPU 실습

evidence flag를 ledger에 넣고 허용되는 최대 claim을 계산한다. held-out probe와 control은 통과했지만 기능 검사와 개입이 없으므로 `recoverable`에서 멈춘다.

<!-- I06_EXAMPLE: i06_14_claim_ledger -->

실제 논문 문장은 자동 규칙보다 복잡하지만, ledger는 빠진 증거를 드러내는 점검 장치다.

## 흔한 오해

### 오해 1. `suggests`를 쓰면 강한 주장도 안전하다

완곡한 동사보다 claim의 논리 구조가 중요하다. 증거가 관찰뿐이면 인과 명사를 붙이지 않는다.

### 오해 2. limitation은 토론 절에만 쓰면 된다

핵심 결과 바로 옆에 적용 범위와 대안 설명을 적어야 독자가 문장을 오해하지 않는다.

### 오해 3. 재현됐다는 말은 코드가 다시 실행됐다는 뜻이다

계산 재현과 독립 seed·dataset·model에서 결과가 유지되는 경험적 재현을 구분한다.

## 연습문제

### 1. 단계 분류

`held-out probe가 품사를 92% 정확도로 예측했다`는 어느 단계 주장인가?

<details><summary>해설 보기</summary>복원 가능성 주장이다. control과 baseline이 적절하다는 조건에서 품사 정보를 읽어낼 수 있었다고 쓴다.</details>

### 2. 문장 수정

`layer 8이 정답을 결정했다`를 activation 차이만 관찰한 상황에 맞게 고쳐라.

<details><summary>해설 보기</summary>`고정한 정답·오답 조건에서 layer 8의 선택 activation 통계 차이가 관찰됐다`처럼 쓴다. 결정·원인 표현을 제거한다.</details>

### 3. 개입

ablation 뒤 성능이 낮아졌다. causal claim에 더 필요한 control 하나를 적어라.

<details><summary>해설 보기</summary>같은 norm·분포를 가진 random direction ablation, activation magnitude 보존 control이나 sham intervention으로 일반 손상과 target-specific effect를 구분한다.</details>

### 4. 일반화

한 checkpoint와 영어 prompt에서 반복됐다. 다른 언어와 model로 일반화됐다고 할 수 있는가?

<details><summary>해설 보기</summary>없다. 검증한 checkpoint·언어·prompt 범위로 한정한다.</details>

### 5. negative result

probe task와 control accuracy가 모두 높았다. 무엇을 쓰는가?

<details><summary>해설 보기</summary>probe capacity나 identity memorization으로 결과를 설명할 수 있어 selectivity가 낮았다고 보고한다. representation-specific 복원 주장을 약화한다.</details>

### 6. SAE

reconstruction과 sparsity만 측정했다. 허용되는 문장을 써라.

<details><summary>해설 보기</summary>`정한 dataset에서 이 SAE가 보고한 reconstruction error와 sparsity를 달성했다`고 쓴다. latent의 해석 가능성·안정성·인과 효과는 주장하지 않는다.</details>

## 근거와 갱신 경계

claim 구분은 프로젝트의 문체와 표기 규칙, M04-16의 인과 구분을 따른다. 분야별 용어가 달라도 측정, 복원과 개입 증거를 분리하는 원칙은 유지한다.

## 단원 요약

- 관찰, 복원, 사용, 인과와 일반화는 별도 claim level이다.
- 결과 문장에 대상·측정·대조·불확실성과 범위를 포함한다.
- 완곡한 동사가 증거 부족을 해결하지 않는다.
- negative result는 허용되는 주장의 상한을 정한다.

## 통과 기준

- 주어진 결과를 claim level로 분류할 수 있는가?
- 과도한 문장을 측정에 맞게 고칠 수 있는가?
- evidence ledger에서 빠진 control을 찾을 수 있는가?

## 다음 단원

- [I06-15 종합 실습: 표현 보고서](I06-15-capstone-representation-report.md)

## 집필자 점검표

- [x] 관찰·복원·사용·인과·일반화를 분리했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
