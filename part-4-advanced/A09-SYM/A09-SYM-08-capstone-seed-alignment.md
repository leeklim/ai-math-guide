---
id: "A09-SYM-08"
title: "종합 실습: seed 간 표현 정렬"
part: 4
stage: "A09-SYM"
status: "완료"
prerequisites: ["A09-SYM-01", "A09-SYM-02", "A09-SYM-03", "A09-SYM-04", "A09-SYM-05", "A09-SYM-06", "A09-SYM-07"]
estimated_time: "120~180분"
---

# A09-SYM-08. 종합 실습: seed 간 표현 정렬

## 이 단원이 필요한 이유

seed 간 표현 정렬은 같은 input, 같은 checkpoint 기준, 명시적 symmetry class와 held-out 평가가 없으면 결과를 해석할 수 없다. 이 실습은 raw 차이, symmetry-aligned 차이와 기능 차이를 세 단계로 분리한다.

## 학습 목표

- paired activation dataset과 alignment split을 설계할 수 있다.
- permutation·orthogonal baseline을 공정하게 비교할 수 있다.
- alignment 안정성과 기능 보존을 평가할 수 있다.
- feature identity 주장의 범위를 evidence에 맞게 제한할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-SYM-01~07](A09-SYM-07-model-alignment-equivalence-classes.md)
- 확인 질문: 같은 prompt를 두 모델에 넣는 것이 왜 sample correspondence에 필요한가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $X^{(a)},X^{(b)}$ | `X superscript a and X superscript b` | 두 seed의 paired activations | $n\times d$ |
| $g_{\mathrm{train}}$ | `g fit on the training split` | fitted alignment | transformation |
| $E_{\mathrm{heldout}}$ | `held-out alignment error` | unseen input residual | nonnegative scalar |
| $S_{\mathrm{boot}}$ | `bootstrap stability score` | alignment 재현성 | score or interval |

## 분석 계약

같은 architecture·training recipe의 독립 seed를 비교한다. checkpoint는 processed token 수로 맞추고, 동일 prompt·token 위치·layer·normalization을 사용한다. transformation class는 identity, permutation, orthogonal의 세 단계로 제한한다.

## 측정 절차

1. prompt 단위로 train·held-out split을 만든다.
2. train split에서 neuron assignment와 orthogonal Procrustes를 각각 fit한다.
3. held-out에서 Frobenius residual, CKA·RSA와 downstream output 차이를 계산한다.
4. prompt bootstrap으로 matching·subspace의 안정성을 측정한다.
5. random orthogonal·label-shuffled correspondence를 null control로 사용한다.
6. aligned direction intervention을 두 seed에서 반복해 effect의 sign·magnitude를 비교한다.

## 결과 기록표

| 비교 | 보존하는 구조 | held-out 지표 | 허용 주장 |
|---|---|---|---|
| identity | coordinate label | raw residual | 좌표 일치 |
| permutation | coordinate content | assignment residual | 순서까지의 일치 |
| orthogonal | inner product | Procrustes residual | subspace geometry 일치 |
| intervention | behavior effect | paired effect | 기능적 재사용 증거 |

## 흔한 오해

- orthogonal alignment 성공은 neuron 일대일 identity를 뜻하지 않는다.
- 한 seed pair의 결과를 training recipe 전체의 필연적 symmetry로 일반화할 수 없다.

## 연습문제

### 1. split 단위
token row를 무작위 분할하는 대신 prompt 단위로 나누는 이유는 무엇인가?
<details><summary>해설 보기</summary>

같은 prompt의 연관 token이 train과 held-out에 동시에 들어가는 leakage를 막기 위해서다.
</details>

### 2. nested class
permutation보다 orthogonal residual이 작을 때 무엇을 결론낼 수 있는가?
<details><summary>해설 보기</summary>

coordinate reorder만으로는 설명되지 않는 회전된 subspace 유사성이 있을 수 있다. 기능 동치는 별도 검사해야 한다.
</details>

### 3. stability
bootstrap마다 neuron matching이 달라지지만 subspace angle은 안정적이면 어떤 수준으로 보고하는가?
<details><summary>해설 보기</summary>

개별 neuron identity는 불안정하고 subspace-level equivalence만 안정적이라고 보고한다.
</details>

### 4. causal transfer
aligned direction ablation effect가 두 seed에서 비슷하면 무엇이 강화되는가?
<details><summary>해설 보기</summary>

해당 aligned subspace가 두 모델에서 유사한 기능에 사용된다는 증거가 강화된다. 유일한 mechanism이라는 뜻은 아니다.
</details>

## 근거와 갱신 경계

이 실습은 permutation matching, Procrustes, CKA·RSA와 intervention을 계층적 증거로 결합한다. nonlinear map으로 arbitrary fit을 허용하지 않으며 새 architecture에서는 symmetry class부터 다시 정한다.

## 단원 요약

- paired data와 prompt-level split을 사용한다.
- identity·permutation·orthogonal class를 계층적으로 비교한다.
- bootstrap으로 alignment unit의 안정성을 판정한다.
- intervention transfer로 geometry 유사성과 기능 유사성을 분리한다.

## 통과 기준

- seed alignment의 claim–class–split–metric–control을 설계할 수 있는가?
- neuron·subspace·function identity 주장을 구분할 수 있는가?

## 다음 단원

- 다음 선택 모듈은 A09-LRN이다.

## 집필자 점검표

- [x] seed 간 정렬의 계층적 증거 계약을 완성했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
