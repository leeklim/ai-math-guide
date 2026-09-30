---
id: "A09-KER-08"
title: "종합 실습: kernel 관점의 학습"
part: 4
stage: "A09-KER"
status: "완료"
prerequisites: ["A09-KER-01", "A09-KER-02", "A09-KER-03", "A09-KER-04", "A09-KER-05", "A09-KER-06", "A09-KER-07"]
estimated_time: "120~180분"
---

# A09-KER-08. 종합 실습: kernel 관점의 학습

## 이 단원이 필요한 이유

kernel 분석은 Gram matrix 하나를 그리는 작업으로 끝나지 않는다. input unit, centering, normalization, target, checkpoint와 null model을 고정해야 spectrum과 learning dynamics를 연결할 수 있다. 이 실습은 empirical NTK가 실제 output 변화와 얼마나 맞는지 검증하는 계약을 만든다.

## 학습 목표

- checkpoint별 empirical NTK 분석 계약을 설계할 수 있다.
- kernel spectrum과 target alignment를 계산할 수 있다.
- linearized prediction과 실제 training trajectory를 비교할 수 있다.
- 결과를 parameterization과 sampled input에 한정해 보고할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-KER-01~07](A09-KER-07-parameter-function-space.md)
- 확인 질문: initialization NTK spectrum만으로 finite network의 training 전체를 예측하기 어려운 이유는 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $K_t$ | `K at checkpoint t` | checkpoint $t$의 empirical NTK | $n\times n$ |
| $\widetilde K_t$ | `the centered normalized kernel at checkpoint t` | 비교용으로 전처리한 kernel | $n\times n$ |
| $a_j=u_j^\top y$ | `a sub j equals u sub j transpose y` | target의 kernel eigenmode coefficient | scalar |
| $e_{\mathrm{lin}}(t)$ | `the linearization error at time t` | linearized prediction과 실제 output 차이 | nonnegative scalar |

## 분석 계약

작은 scalar-output MLP 두 seed를 같은 data order와 optimizer 설정으로 학습한다. 고정한 $n$개 input에서 initialization과 여러 checkpoint의 Jacobian을 계산한다. output scale을 맞춘 뒤 kernel centering·normalization 규칙을 모든 checkpoint에 동일하게 적용한다. 비교 단위는 input이며 seed는 독립 반복이다.

## 측정 절차

1. 각 checkpoint에서 $J_t$와 $K_t=J_tJ_t^\top$를 계산하고 PSD tolerance를 확인한다.
2. eigenvalue, effective dimension과 target coefficient $u_j^\top y$를 기록한다.
3. $\lVert\widetilde K_t-\widetilde K_0\rVert_F$로 kernel drift를 측정한다.
4. fixed $K_0$ dynamics가 예측한 output과 실제 output의 차이를 checkpoint별로 계산한다.
5. label permutation과 input permutation에서 같은 spectrum·alignment 절차를 반복한다.
6. hidden-unit permutation으로 함수는 유지한 채 raw parameter distance가 변하는 control을 실행한다.

## 결과 기록표

| 측정 | 답하는 질문 | 해석 제한 |
|---|---|---|
| NTK spectrum | sampled input의 local learning modes | feature semantics |
| target alignment | label residual이 어느 mode에 놓이는가 | population generalization |
| kernel drift | fixed-kernel 근사가 얼마나 변하는가 | drift의 원인 |
| linearization error | $K_0$ dynamics의 예측 적합도 | 다른 optimizer regime |
| symmetry control | raw parameter distance의 비식별성 | 모든 reparameterization |

## 흔한 오해

- centered normalized kernel이 비슷해도 output function이 같다고 결론낼 수 없다.
- target alignment가 높아도 test split과 null label에서 검증하지 않으면 generalization 증거가 아니다.

## 연습문제

### 1. unit
token 1,000개를 같은 prompt 20개에서 얻었다. uncertainty를 계산할 때 최상위 resampling unit을 무엇으로 두는가?
<details><summary>해설 보기</summary>

같은 prompt의 token이 의존하므로 prompt를 최상위 resampling unit으로 둔다.
</details>

### 2. PSD
수치 계산한 $K$의 최소 eigenvalue가 $-10^{-10}$이고 최대 eigenvalue가 $20$이다. 무엇을 먼저 확인하는가?
<details><summary>해설 보기</summary>

$K$를 $(K+K^\top)/2$로 대칭화했는지와 dtype·relative tolerance를 확인한다. 이 크기는 floating-point error일 수 있다.
</details>

### 3. drift
kernel drift는 작지만 linearization error가 커졌다. 어떤 항목을 점검하는가?
<details><summary>해설 보기</summary>

kernel normalization이 scale 변화를 숨겼는지, discrete learning rate와 loss 가정이 맞는지, output offset과 Jacobian linearization remainder를 점검한다.
</details>

### 4. claim
두 seed에서 초기 NTK target alignment가 높았고 training이 빨랐지만 unseen input을 평가하지 않았다. 결론을 어떻게 제한하는가?
<details><summary>해설 보기</summary>

측정한 training input에서 초기 tangent geometry가 target residual과 정렬되었고 빠른 fit과 함께 관찰됐다고 쓴다. population generalization은 주장하지 않는다.
</details>

## 근거와 갱신 경계

이 실습은 squared-loss gradient-flow 식을 finite-step training의 진단 기준으로 사용한다. optimizer와 loss가 다르면 예측식을 바꾸며, NTK 결과를 representation의 유일한 설명으로 쓰지 않는다.

## 단원 요약

- NTK 분석은 input unit과 parameterization을 포함한 계약이 필요하다.
- spectrum, target alignment와 kernel drift는 서로 다른 양이다.
- fixed-kernel prediction은 실제 output trajectory와 비교해야 한다.
- null label과 symmetry control이 해석 범위를 드러낸다.

## 통과 기준

- input–Jacobian–kernel–target–trajectory 계약을 완성할 수 있는가?
- spectrum 증거와 function prediction 증거를 분리할 수 있는가?

## 다음 단원

- 다음 선택 모듈은 A09-RMT이다.

## 집필자 점검표

- [x] kernel spectrum과 실제 학습 trajectory의 검증 계약을 완성했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
