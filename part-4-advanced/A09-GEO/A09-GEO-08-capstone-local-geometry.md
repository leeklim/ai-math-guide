---
id: "A09-GEO-08"
title: "종합 실습: 국소 표현 기하"
part: 4
stage: "A09-GEO"
status: "완료"
prerequisites: ["A09-GEO-01", "A09-GEO-02", "A09-GEO-03", "A09-GEO-04", "A09-GEO-05", "A09-GEO-06", "A09-GEO-07"]
estimated_time: "120~180분"
---

# A09-GEO-08. 종합 실습: 국소 표현 기하

## 이 단원이 필요한 이유

국소 표현 기하 분석은 dataset·layer·token·metric·neighborhood를 먼저 고정해야 재현할 수 있다. 이 실습은 local PCA, Jacobian, pullback metric과 경로 길이를 하나의 claim–estimand–measurement 구조로 묶는다.

## 학습 목표

- 국소 표현 기하 분석의 experimental unit을 정의할 수 있다.
- tangent space와 pullback metric의 추정 절차를 설계할 수 있다.
- bootstrap과 null control을 포함한 결과표를 만들 수 있다.
- 관측 결과에 맞는 주장 강도를 선택할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-GEO-01~07](A09-GEO-07-activation-manifold-pitfalls.md)
- 확인 질문: neighborhood size를 결과를 본 뒤 고르면 어떤 선택 편향이 생기는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $X_\ell$ | `X sub ell` | layer $\ell$의 activation matrix | $n\times D$ |
| $U_r(x)$ | `U sub r of x` | local PCA tangent basis | $D\times r$ |
| $J_h(x)$ | `the Jacobian of h at x` | downstream map의 Jacobian | matrix |
| $\widehat L(\gamma)$ | `L hat of gamma` | 이산 경로의 추정 길이 | nonnegative scalar |

## 분석 계약

claim은 “고정한 layer와 token 위치에서 condition별 activation은 반복 표본에서 안정적인 국소 tangent structure 차이를 보인다”로 제한한다. experimental unit은 독립 prompt이고, 같은 prompt의 token을 독립 반복으로 세지 않는다.

사전에 다음을 고정한다.

1. model checkpoint, prompt set, layer, token 위치와 normalization
2. Euclidean 또는 사전 지정 metric
3. neighborhood 후보와 선택 규칙
4. local dimension threshold와 bootstrap 횟수
5. random-label·matched Gaussian·random-subspace control

## 측정 절차

각 anchor $x$에서 neighborhood covariance를 만들고 leading eigenvector $U_r(x)$를 구한다. downstream map $h$가 미분 가능하면 $U_r^\top J_h^\top J_hU_r$로 tangent-restricted pullback metric을 계산한다. 이산 경로 $x_0,\ldots,x_T$의 길이는

$$
\widehat L(\gamma)=\sum_{t=0}^{T-1}
\sqrt{\Delta x_t^\top G(x_t)\Delta x_t}
$$

로 근사한다. prompt bootstrap으로 median과 interval을 보고하고, 같은 절차를 null data에 적용한다.

## 결과 기록표

| 항목 | estimand | measurement | control | 허용 주장 |
|---|---|---|---|---|
| local dimension | condition별 median $d$ | local PCA spectrum | Gaussian·shuffle | 기술적 차이 |
| tangent alignment | subspace similarity | principal angles | random subspace | 정렬 차이 |
| pullback sensitivity | tangent direction별 gain | restricted metric eigenvalue | matched norm | 국소 민감도 |
| path length | condition별 metric length | discrete sum | permuted path | 경로 구조 |

## 흔한 오해

- 작은 bootstrap interval은 systematic bias가 없다는 뜻이 아니다.
- tangent alignment와 causal feature reuse는 같은 주장이 아니다.

## 연습문제

### 1. experimental unit
prompt 하나에서 얻은 100개 token activation을 독립 표본 100개로 세도 되는가?
<details><summary>해설 보기</summary>

일반적으로 안 된다. 같은 prompt와 sequence의 token은 의존하므로 prompt 단위 bootstrap 또는 의존 구조를 반영한 resampling이 필요하다.
</details>

### 2. tangent comparison
두 $r$차원 tangent subspace의 정렬을 비교할 수 있는 측정량을 쓰라.
<details><summary>해설 보기</summary>

principal angles 또는 그 cosine인 singular value를 사용할 수 있다. 같은 preprocessing과 ambient inner product를 고정해야 한다.
</details>

### 3. metric ablation
Euclidean metric에서만 condition 차이가 보이고 whitening metric에서는 사라졌다. 무엇을 보고해야 하는가?
<details><summary>해설 보기</summary>

결론이 metric 선택에 민감하다고 보고하고 두 metric이 제거하거나 강조하는 변동을 설명한다. 한 결과만 선택해 일반화하지 않는다.
</details>

### 4. claim ledger
특정 tangent direction을 ablate하자 output이 변했다. 이것만으로 그 방향이 유일한 causal mechanism인가?
<details><summary>해설 보기</summary>

아니다. intervention effect의 증거이지만 off-manifold perturbation, 대체 경로와 비특이적 norm effect를 통제해야 유일성 주장을 강화할 수 있다.
</details>

## 근거와 갱신 경계

이 실습은 앞 단원의 표준 differential geometry와 point-cloud 추정 원칙을 재현 가능한 분석 계약으로 묶는다. 특정 모델에서의 수치 결과는 제공하지 않으며 model·dataset이 바뀌면 estimand와 control을 다시 검토한다.

## 단원 요약

- experimental unit과 geometry 선택을 분석 전에 고정한다.
- local PCA와 Jacobian은 tangent structure와 local sensitivity를 측정한다.
- bootstrap과 null control을 같은 pipeline에 적용한다.
- 기술적 차이·intervention effect·mechanism 주장의 강도를 구분한다.

## 통과 기준

- claim–estimand–measurement–control 표를 완성할 수 있는가?
- 결과가 metric과 neighborhood에 민감할 때 결론을 제한할 수 있는가?

## 다음 단원

- 다음 선택 모듈은 A09-DYN이다.

## 집필자 점검표

- [x] 국소 표현 기하 분석 계약을 완성했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
