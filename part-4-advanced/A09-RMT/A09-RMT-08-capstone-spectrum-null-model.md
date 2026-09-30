---
id: "A09-RMT-08"
title: "종합 실습: spectrum의 null model"
part: 4
stage: "A09-RMT"
status: "완료"
prerequisites: ["A09-RMT-01", "A09-RMT-02", "A09-RMT-03", "A09-RMT-04", "A09-RMT-05", "A09-RMT-06", "A09-RMT-07"]
estimated_time: "120~180분"
---

# A09-RMT-08. 종합 실습: spectrum의 null model

## 이 단원이 필요한 이유

activation spectrum에서 bulk와 outlier를 찾으려면 관찰 matrix와 null generator를 한 분석 계약에 넣어야 한다. 이 실습은 MP edge를 출발점으로 사용하되 prompt dependence, marginal variance, split stability와 task relevance를 단계별로 검증한다.

## 학습 목표

- activation covariance용 null hierarchy를 설계할 수 있다.
- analytic MP edge와 simulated null quantile을 비교할 수 있다.
- outlier subspace의 split·seed 안정성을 평가할 수 있다.
- variance signal과 task·causal signal을 구분해 보고할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-RMT-01~07](A09-RMT-07-weight-activation-hessian-spectra.md)
- 확인 질문: iid Gaussian MP null이 실제 activation에서 실패할 수 있는 조건 두 가지는 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $S_{\mathrm{obs}}$ | `the observed covariance S` | 실제 activation sample covariance | $d\times d$ |
| $\lambda_{+,\mathrm{MP}}$ | `the Marchenko Pastur upper edge` | fitted iid null의 upper bulk edge | scalar |
| $q_{0.95}^{\mathrm{sim}}$ | `the ninety-fifth percentile of the simulated null` | simulated largest-eigenvalue threshold | scalar |
| $r_{\mathrm{stable}}$ | `the number of stable spectral directions` | null·split 기준을 함께 통과한 subspace dimension | nonnegative integer |

## 분석 계약

고정 model·layer·token rule에서 prompt별 activation을 모은다. prompt를 독립 experimental unit으로 두고 feature별 center와 scale 규칙을 train split에서 정한다. 두 model seed와 prompt split을 사용한다. spectrum 선별에는 test label을 사용하지 않는다.

## 측정 절차

1. $S_{\mathrm{obs}}$의 eigenvalue, participation ratio와 aspect ratio를 계산한다.
2. shape와 global variance를 맞춘 iid Gaussian null의 MP edge를 구한다.
3. feature별 marginal을 보존하고 cross-feature pairing을 깨는 prompt-block permutation null을 생성한다.
4. null replicate마다 largest eigenvalue와 rank별 eigenvalue를 저장해 parallel-analysis quantile을 구한다.
5. null을 넘은 leading subspace를 prompt split과 model seed 사이에서 비교한다.
6. stable subspace의 held-out label prediction과 dimension-matched random-subspace control을 평가한다.
7. stable subspace projection·ablation을 random-subspace intervention과 비교한다.

## 결과 기록표

| 단계 | 통과 기준 | 허용 claim |
|---|---|---|
| analytic null | MP edge 초과 | iid isotropic null과 불일치 |
| simulated null | null quantile 초과 | matched null과 불일치 |
| split·seed | subspace overlap 재현 | stable variance subspace |
| held-out task | control 대비 prediction | recoverable task signal |
| intervention | matched control 대비 effect | 지정 조작에서의 functional evidence |

## 흔한 오해

- analytic null과 simulated null 중 유리한 결과만 선택하면 selection bias가 생긴다.
- outlier 개수를 data를 본 뒤 threshold와 함께 조정하면 confirmatory claim을 할 수 없다.

## 연습문제

### 1. split
null threshold와 subspace dimension을 어느 split에서 정하고 task association을 어느 split에서 평가하는가?
<details><summary>해설 보기</summary>

train·validation data에서 threshold와 dimension을 정하고, 선택에 쓰지 않은 held-out test split에서 task association을 평가한다.
</details>

### 2. mismatch
MP edge는 3.0인데 matched permutation null의 95% quantile은 5.2이다. observed largest eigenvalue가 4.0이면 무엇을 결론내리는가?
<details><summary>해설 보기</summary>

iid MP null은 넘지만 dependence와 marginal을 더 보존한 permutation null은 넘지 않는다. matched null 기준 signal 주장은 보류한다.
</details>

### 3. rotation
leading eigenvalue 두 개가 거의 같고 split마다 eigenvector가 회전한다. 무엇을 비교하는가?
<details><summary>해설 보기</summary>

두 vector를 각각 맞추지 않고 leading two-dimensional subspace의 principal-angle overlap을 비교한다.
</details>

### 4. claim
stable outlier subspace가 label을 예측하지만 ablation 효과가 random subspace와 같다. 어떻게 보고하는가?
<details><summary>해설 보기</summary>

재현 가능한 variance subspace에서 label을 복원할 수 있지만 해당 subspace의 고유한 functional use는 확인되지 않았다고 쓴다.
</details>

## 근거와 갱신 경계

이 실습은 null hierarchy와 증거 순서를 고정한다. prompt-block permutation도 모든 dependence를 보존하지 않으므로 generator가 깨는 구조를 보고서에 명시한다.

## 단원 요약

- analytic MP와 matched simulation은 서로 다른 null을 제공한다.
- threshold 선택과 held-out task 평가는 분리한다.
- eigenvalue가 가까우면 vector보다 subspace 안정성을 본다.
- variance outlier, recoverability와 functional effect를 별도 claim으로 기록한다.

## 통과 기준

- matrix–unit–normalization–null–stability–task 계약을 완성할 수 있는가?
- null mismatch가 결론을 바꾸는 사례를 설명할 수 있는가?

## 다음 단원

- 다음 선택 모듈은 A09-CAU이다.

## 집필자 점검표

- [x] analytic·simulated null과 task·개입 검증을 분리했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
