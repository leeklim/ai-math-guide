---
id: "A09-SYM-07"
title: "모델 정렬과 동치류"
part: 4
stage: "A09-SYM"
status: "완료"
prerequisites: ["A09-SYM-02", "A09-SYM-04", "A09-SYM-05", "I08-03"]
estimated_time: "90~120분"
---

# A09-SYM-07. 모델 정렬과 동치류

## 이 단원이 필요한 이유

seed가 다른 모델의 neuron·subspace·weight를 직접 비교하면 symmetry가 만든 좌표 차이를 학습 결과 차이로 오해할 수 있다. alignment는 허용한 transformation class 안에서 대응을 찾고, quotient 관점은 alignment 뒤에도 남는 불확실성을 드러낸다.

## 학습 목표

- alignment objective와 transformation class를 명시할 수 있다.
- permutation·orthogonal·general linear alignment를 구분할 수 있다.
- train alignment와 held-out evaluation을 분리할 수 있다.
- residual mismatch를 기능 차이로 해석하기 위한 조건을 말할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-SYM-02 orbit와 stabilizer](A09-SYM-02-orbits-stabilizers.md), [A09-SYM-04 permutation](A09-SYM-04-permutation-symmetry.md), [A09-SYM-05 gauge freedom](A09-SYM-05-scaling-rotation-gauge.md), [I08-03 representation alignment](../../part-3-interpretability/I08/I08-03-representation-alignment.md)
- 확인 질문: transformation class를 넓힐수록 training alignment error는 왜 줄기 쉬운가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $X,Y$ | `X and Y` | paired activation matrices | $n\times d$ |
| $\mathcal G$ | `the transformation class G` | 허용 alignment 집합 | set of maps |
| $\hat g=\arg\min_{g\in\mathcal G}\|Xg-Y\|_F$ | `g hat minimizes the Frobenius norm of X g minus Y over g in G` | fitted alignment | map |
| $d_{\mathcal G}(X,Y)$ | `the G aligned distance between X and Y` | orbit-minimized distance | nonnegative scalar |

## 핵심 개념

alignment는 대상, sample correspondence, centering·scaling과 transformation class를 함께 정한다. permutation은 coordinate identity만 바꾸고, orthogonal map은 inner product를 보존하며, general invertible map은 더 많은 geometry를 지운다.

$$
d_{\mathcal G}(X,Y)=\min_{g\in\mathcal G}\|Xg-Y\|_F
$$

는 허용 transformation orbit 사이의 거리를 근사한다. 같은 sample로 $g$를 fit하고 평가하면 overfitting이 생기므로 held-out input에서 residual과 task-relevant behavior를 측정한다.

stabilizer나 repeated singular value 때문에 optimal alignment가 유일하지 않을 수 있다. 이 경우 feature-by-feature identity보다 subspace equivalence가 더 정직한 결론이다.

## 작은 예제

$Y=XP$인 정확한 column permutation이면 raw $\|X-Y\|_F$는 클 수 있지만 permutation-aligned distance는 0이다.

## 흔한 오해

- alignment error가 0이라는 사실만으로 두 모델의 전체 함수가 같다 할 수 없다.
- 가장 flexible한 alignment가 가장 좋은 과학적 비교인 것은 아니다.

## 연습문제

### 1. class 선택
coordinate별 feature identity가 질문이면 orthogonal alignment보다 permutation이 적절할 수 있는 이유는 무엇인가?
<details><summary>해설 보기</summary>

rotation은 여러 coordinate를 섞어 feature identity 차이를 지울 수 있지만 permutation은 coordinate의 내용은 유지한 채 순서만 바꾼다.
</details>

### 2. held-out
alignment fit·evaluation split이 필요한 이유는 무엇인가?
<details><summary>해설 보기</summary>

sample-specific noise까지 맞춘 transformation의 training error를 representation equivalence로 오해하지 않기 위해서다.
</details>

### 3. non-uniqueness
isotropic subspace 안에서 여러 rotation이 같은 objective를 주면 어떤 대상을 보고하는가?
<details><summary>해설 보기</summary>

개별 axis보다 subspace, principal angle과 alignment solution의 불확실성을 보고한다.
</details>

### 4. 기능 검증
작은 aligned distance 뒤에 추가할 behavior 검사는 무엇인가?
<details><summary>해설 보기</summary>

held-out input에서 output distribution·loss·intervention effect 같은 사전 지정 function metric을 비교한다.
</details>

## 근거와 갱신 경계

Procrustes alignment와 quotient distance는 linear algebra·shape analysis의 표준 구성을 따른다. nonlinear alignment는 해석 가능성과 identifiability가 크게 달라 이 단원에서 제외한다.

## 단원 요약

- alignment는 허용 transformation class를 먼저 정한다.
- 더 넓은 class는 더 많은 구조를 지운다.
- transformation은 train sample에서 fit하고 held-out에서 평가한다.
- non-unique alignment에서는 feature보다 subspace 동치를 보고한다.

## 통과 기준

- 질문에 맞는 alignment class를 선택할 수 있는가?
- aligned similarity와 function equivalence를 구분할 수 있는가?

## 다음 단원

- [A09-SYM-08 종합 실습: seed 간 표현 정렬](A09-SYM-08-capstone-seed-alignment.md)

## 집필자 점검표

- [x] alignment class·split·비유일성을 포함했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
