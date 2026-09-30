---
id: "I06-12"
title: "sparse autoencoder"
part: 3
stage: "I06"
status: "완료"
prerequisites: ["I06-11", "N05-07"]
estimated_time: "130~160분"
---

# I06-12. sparse autoencoder

## 이 단원이 필요한 이유

sparse autoencoder는 activation에서 sparse latent를 직접 추론하는 encoder와 원래 activation을 복원하는 decoder를 함께 학습한다. 많은 latent를 사용해 overcomplete dictionary를 만들 수 있지만, reconstruction과 sparsity 사이 tradeoff, dead feature와 해석 안정성을 모두 검사해야 한다.

## 학습 목표

- SAE encoder·decoder의 shape와 목적함수를 설명할 수 있다.
- $L_1$ SAE와 TopK SAE의 sparsity 통제를 구분할 수 있다.
- reconstruction, $L_0$, dead feature와 downstream fidelity를 계산할 수 있다.
- SAE latent를 ground-truth concept로 취급하면 안 되는 이유를 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [I06-11 sparse coding](I06-11-sparse-coding.md), [N05-07 mini-batch gradient descent](../../part-2-neural-computation/N05/N05-07-gradient-descent-mini-batch.md)
- 확인 질문: reconstruction MSE가 낮아도 모든 latent가 사용된다고 보장되는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $f=\operatorname{ReLU}(W_ea+b_e)$ | `f equals ReLU of W e a plus b e` | activation을 sparse latent로 encode | $\mathbb R^m$ |
| $\hat a=W_df+b_d$ | `a hat equals W d f plus b d` | latent에서 activation을 reconstruct | $\mathbb R^d$ |
| reconstruction loss | `reconstruction loss` | $a$와 $\hat a$의 차이 | nonnegative scalar |
| mean $L_0$ | `mean L zero` | 표본당 활성 latent 수의 평균 | $[0,m]$ |
| dead feature | `dead feature` | 평가 구간에서 한 번도 활성화되지 않은 latent | latent status |
| loss recovered | `loss recovered` | SAE reconstruction이 원 model loss를 얼마나 보존하는지 나타내는 지표 | normalized statistic |

## 1. 구조와 shape

$a\in\mathbb R^d$를 $m$개 latent로 encode한다. 보통 $m>d$인 overcomplete 설정을 쓴다.

\[
f=\operatorname{ReLU}(W_ea+b_e),\qquad
\hat a=W_df+b_d.
\]

$W_e\in\mathbb R^{m\times d}$, $W_d\in\mathbb R^{d\times m}$다. decoder column은 latent 하나가 activation 공간에 더하는 direction으로 볼 수 있다.

## 2. 목적함수

ReLU SAE의 한 기본형은

\[
\mathcal L=\mathbb E\lVert a-\hat a\rVert_2^2+\lambda\mathbb E\lVert f\rVert_1
\]

이다. TopK SAE는 각 표본에서 가장 큰 $k$개 latent만 남겨 $L_0$를 직접 통제한다. 두 방식은 같은 sparsity notion이 아니므로 숫자를 그대로 비교하지 않는다.

## 3. 필수 평가 묶음

SAE 하나를 다음 네 숫자만으로 평가할 수는 없지만, 최소 gate로 사용한다.

1. reconstruction MSE 또는 explained variance
2. mean $L_0$와 activation magnitude 분포
3. dead feature 수와 firing frequency
4. reconstructed activation을 model에 넣었을 때 downstream loss 또는 행동 보존

추가로 seed·width·sparsity가 바뀔 때 dictionary와 subspace 안정성을 본다. feature explanation score도 sampling과 evaluator에 의존한다.

## 4. dead feature

ReLU latent가 모든 관찰에서 0이면 gradient와 initialization에 따라 다시 살아나기 어렵다. dead threshold는 dataset 크기와 관찰 window를 포함해 정의한다. 희귀하지만 의미 있는 feature를 짧은 sample에서 dead로 잘못 분류할 수 있다.

## 5. feature 해석과 기능

latent의 top activating context에서 일관된 주제가 보여도 다음을 분리한다.

- **coherence**: 상위 예가 하나의 설명과 맞는가?
- **sensitivity**: 설명에 맞는 새 예에서 실제로 켜지는가?
- **specificity**: hard negative에서 꺼지는가?
- **causal effect**: latent intervention이 행동을 선택적으로 바꾸는가?

reconstruction과 sparsity는 이 질문의 대체물이 아니다.

## CPU 실습

10개 nonnegative sparse source를 6차원으로 섞은 128개 표본에 12-latent ReLU SAE를 50 step 학습한다. MSE, mean $L_0$와 dead feature를 동시에 출력한다.

<!-- I06_EXAMPLE: i06_12_sparse_autoencoder -->

작은 학습에서 dead feature가 생기는 것은 실패를 숨길 항목이 아니라 평가 결과다. step을 무한히 늘려 숫자를 좋게 만드는 대신 정한 자원 상한 안에서 보고한다.

## 흔한 오해

### 오해 1. latent가 sparse하면 monosemantic하다

sparsity는 동시에 켜지는 수를 제한한다. 각 latent가 하나의 인간 개념에 대응한다는 보장은 없다.

### 오해 2. width를 키우면 항상 더 좋은 feature가 나온다

reconstruction은 좋아질 수 있지만 dead feature, 계산비용과 stability가 달라진다. 여러 metric의 frontier를 본다.

### 오해 3. SAE reconstruction을 원 activation과 완전히 같은 것으로 써도 된다

오차가 downstream 계산에 미치는 영향을 측정해야 한다. 작은 MSE가 작은 행동 변화와 항상 같지는 않다.

## 연습문제

### 1. shape

$d=768$, $m=4096$이면 $W_e$와 $W_d$ shape는 무엇인가?

<details><summary>해설 보기</summary>$W_e$는 $4096\times768$, $W_d$는 $768\times4096$이다.</details>

### 2. sparsity

latent 100개 중 표본마다 평균 8개가 threshold 위라면 mean $L_0$와 active fraction은 얼마인가?

<details><summary>해설 보기</summary>mean $L_0$는 8, active fraction은 $8/100=0.08$이다.</details>

### 3. dead threshold

작은 dataset에서 한 번도 켜지지 않은 latent가 영구적으로 dead라고 단정할 수 있는가?

<details><summary>해설 보기</summary>없다. 희귀 feature일 수 있다. 관찰 dataset, token 수와 threshold를 함께 보고 더 넓은 표본에서 재검사한다.</details>

### 4. reconstruction

두 SAE의 MSE가 같고 하나의 mean $L_0$가 절반이다. 무조건 더 좋은가?

<details><summary>해설 보기</summary>더 sparse한 frontier 점이지만 dead feature, downstream fidelity, feature quality와 안정성도 비교해야 한다.</details>

### 5. TopK

TopK에서 $k=32$이면 모든 표본의 정확한 nonzero 수가 항상 32인가?

<details><summary>해설 보기</summary>구현이 정확히 상위 32개를 남기고 tie·mask 예외가 없다면 그렇다. ReLU $L_1$ SAE처럼 penalty로 간접 통제하는 방식과 다르다.</details>

### 6. 주장 범위

top context가 모두 코드와 관련됐다. `coding feature`라고 확정할 수 있는가?

<details><summary>해설 보기</summary>설명 가설은 강해지지만 독립 positive·hard negative, sensitivity·specificity와 개입을 확인해야 한다. 상위 예 coherence만 측정한 상태다.</details>

## 근거와 갱신 경계

SAE의 reconstruction·$L_1$ 구조는 [Towards Monosemanticity](https://transformer-circuits.pub/2023/monosemantic-features/)를, TopK·dead latent와 scaling metric은 [Scaling and Evaluating Sparse Autoencoders](https://arxiv.org/abs/2406.04093)를 참고했다. 2025년 SAEBench는 completeness·isolation 등 여러 metric이 서로 다른 품질을 측정함을 보여준다. 특정 architecture의 우열은 고정 결론으로 쓰지 않는다.

## 단원 요약

- SAE는 sparse encoder와 activation reconstruction decoder를 함께 학습한다.
- reconstruction, sparsity, dead feature와 downstream fidelity를 함께 평가한다.
- ReLU+$L_1$과 TopK는 sparsity 통제 방식이 다르다.
- SAE latent의 의미·안정성·인과 효과는 별도 검사다.

## 통과 기준

- SAE parameter shape와 loss 항을 설명할 수 있는가?
- MSE, mean $L_0$, dead feature와 downstream fidelity를 계산할 수 있는가?
- sparse latent에 허용되는 주장 범위를 쓸 수 있는가?

## 다음 단원

- [I06-13 feature 안정성과 identifiability](I06-13-feature-stability-identifiability.md)

## 집필자 점검표

- [x] reconstruction·sparsity·dead feature·stability를 함께 평가했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
