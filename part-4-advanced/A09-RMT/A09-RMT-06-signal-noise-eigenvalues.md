---
id: "A09-RMT-06"
title: "signal과 noise eigenvalue"
part: 4
stage: "A09-RMT"
status: "완료"
prerequisites: ["M04-09", "I06-05", "A09-RMT-05"]
estimated_time: "90~120분"
---

# A09-RMT-06. signal과 noise eigenvalue

## 이 단원이 필요한 이유

eigenvalue 크기 하나만으로 signal과 noise를 나눌 수 없다. null model 초과, split·seed 안정성, held-out target association과 intervention은 서로 다른 증거를 제공한다. spectrum 분석은 이 증거들을 한 판정 규칙으로 합치지 않고 단계별로 기록해야 한다.

## 학습 목표

- parallel analysis의 null threshold를 설명할 수 있다.
- eigenvalue separation과 eigenvector stability를 구분할 수 있다.
- split-half subspace overlap과 bootstrap interval을 설계할 수 있다.
- spectral component의 task relevance claim을 단계별로 작성할 수 있다.

## 선수지식 확인

- 선수 단원: [M04-09 신뢰구간과 bootstrap](../../part-1-foundations/M04/M04-09-confidence-intervals-bootstrap.md), [I06-05 PCA와 SVD 분석](../../part-3-interpretability/I06/I06-05-pca-svd-analysis.md), [A09-RMT-05 spiked covariance model](A09-RMT-05-spiked-covariance-model.md)
- 확인 질문: eigenvalue가 비슷한 두 direction을 각각 비교하는 것보다 두 direction의 span을 비교하는 편이 나은 이유는 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $q_{1-\alpha}^{\mathrm{null}}$ | `the one minus alpha null quantile` | null largest eigenvalue의 upper quantile | scalar |
| $\hat\lambda_j$ | `lambda j hat` | observed sample eigenvalue | nonnegative scalar |
| $\widehat U_k$ | `U k hat` | leading $k$-dimensional sample subspace | $d\times k$ |
| $\lVert U_A^\top U_B\rVert_F^2/k$ | `the normalized squared Frobenius overlap of U A and U B` | split subspace overlap | number in $[0,1]$ |

## 핵심 개념

parallel analysis는 observed matrix와 shape·marginal·dependence 조건을 맞춘 null matrix를 여러 번 생성한다. 각 rank의 null eigenvalue distribution이나 largest-eigenvalue quantile을 구해 observed eigenvalue와 비교한다. 예를 들어

$$
\hat\lambda_1>q_{1-\alpha}^{\mathrm{null}}
$$

이면 지정 null보다 큰 leading variance가 있다는 증거를 얻는다. 이 판정은 null이 맞을 때만 해석할 수 있다.

다음으로 data를 independent unit 기준으로 나누고 leading subspace overlap을 계산한다. eigenvalue gap이 작으면 vector별 sign·rotation이 불안정해도 subspace는 안정적일 수 있다. bootstrap은 eigenvalue와 overlap의 sampling uncertainty를 보여준다.

task relevance는 held-out label association이나 prediction으로 평가한다. functional use는 component projection·ablation 뒤 behavior change로 별도 확인한다. null 초과, reproducibility, recoverability와 causal use를 각각 기록한다.

## 작은 예제

observed largest eigenvalue가 5.0이고 1,000개 matched null의 95% quantile이 4.2이면 null exceedance는 확인된다. split overlap이 0.15라면 stable direction이라는 주장은 보류한다.

## 흔한 오해

- null threshold 초과와 false-positive probability를 같은 값으로 읽을 수 없다.
- stable high-variance component가 label이나 behavior에 관련된다는 보장은 없다.

## 연습문제

### 1. parallel analysis
observed eigenvalue가 3.1이고 null 95% quantile이 3.4이면 $\alpha=0.05$ 기준으로 null을 넘는가?
<details><summary>해설 보기</summary>

넘지 않는다. 지정 null에서 noise-compatible한 값으로 남는다.
</details>

### 2. overlap
두 split이 같은 one-dimensional direction을 sign만 반대로 추정했다. squared subspace overlap은 얼마인가?
<details><summary>해설 보기</summary>

sign은 span을 바꾸지 않으므로 overlap은 1이다.
</details>

### 3. hierarchy
null 초과와 split 안정성은 통과했지만 held-out label association이 없다. 어떤 claim까지 가능한가?
<details><summary>해설 보기</summary>

지정 null을 넘는 재현 가능한 variance direction이라고 말할 수 있다. task-relevant signal이라는 주장은 보류한다.
</details>

### 4. 모델 해석
한 component ablation이 behavior를 바꿨지만 random direction ablation도 같은 크기의 효과를 냈다. 무엇을 결론내리는가?
<details><summary>해설 보기</summary>

개입 효과의 component specificity가 확인되지 않았다. norm과 subspace dimension을 맞춘 control distribution에서 비교해야 한다.
</details>

## 근거와 갱신 경계

parallel analysis는 null generator의 타당성에 의존한다. 여러 eigenvalue를 동시에 선별할 때는 family-wise error나 false discovery control을 별도로 정한다.

## 단원 요약

- null exceedance는 spectral signal 판정의 첫 단계이다.
- split 안정성은 eigenvector나 subspace의 재현성을 평가한다.
- held-out association과 intervention은 task relevance와 기능을 다룬다.
- 네 증거를 하나의 signal label로 압축하지 않는다.

## 통과 기준

- matched null과 subspace stability 검사를 설계할 수 있는가?
- variance·reproducibility·prediction·causal use claim을 구분할 수 있는가?

## 다음 단원

- [A09-RMT-07 weight·activation·Hessian spectrum](A09-RMT-07-weight-activation-hessian-spectra.md)

## 집필자 점검표

- [x] null 초과·안정성·task association·기능을 분리했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
