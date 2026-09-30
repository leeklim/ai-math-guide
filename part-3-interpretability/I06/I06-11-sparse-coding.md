---
id: "I06-11"
title: "sparse coding"
part: 3
stage: "I06"
status: "완료"
prerequisites: ["I06-10", "M01-04"]
estimated_time: "110~140분"
---

# I06-11. sparse coding

## 이 단원이 필요한 이유

sparse coding은 dense activation을 적은 수의 dictionary feature 조합으로 근사한다. reconstruction만 최소화하면 많은 coefficient를 사용할 수 있으므로 sparsity penalty를 함께 둔다. dictionary와 code가 유일하다고 가정하면 안 된다.

## 학습 목표

- reconstruction과 sparsity가 결합된 목적함수를 해석할 수 있다.
- 고정 dictionary에서 sparse code를 반복 갱신할 수 있다.
- reconstruction error, active fraction과 dictionary coherence를 평가할 수 있다.
- sparse solution의 비유일성과 scale 모호성을 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [I06-10 superposition](I06-10-superposition.md), [M01-04 도함수와 그래프](../../part-1-foundations/M01/M01-04-derivative-and-graphs.md)
- 확인 질문: dictionary column을 두 배하고 coefficient를 절반으로 만들면 reconstruction은 변하는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\hat z$ | `z hat` | 주어진 activation에서 추정한 sparse code | $\mathbb R^m$ |
| $\lVert a-Dz\rVert_2^2$ | `the squared reconstruction error` | 원 activation과 reconstruction의 제곱오차 | nonnegative scalar |
| $\lVert z\rVert_1$ | `the L one norm of z` | coefficient 절댓값 합 | nonnegative scalar |
| $\lambda$ | `lambda` | reconstruction과 sparsity의 tradeoff | nonnegative scalar |
| soft thresholding | `soft thresholding` | 작은 coefficient를 0으로 줄이는 proximal 연산 | elementwise map |
| dictionary coherence | `dictionary coherence` | 서로 다른 normalized column 내적의 최대 절댓값 | $[0,1]$ |

## 1. 고정 dictionary에서 code 찾기

activation $a$와 dictionary $D$가 주어졌을 때

\[
\hat z=\arg\min_z\frac12\lVert a-Dz\rVert_2^2+\lambda\lVert z\rVert_1
\]

을 푼다. 첫 항은 reconstruction, 둘째 항은 sparse coefficient를 선호한다. $\lambda=0$이면 reconstruction만 맞추고, 너무 크면 모든 code가 0이 될 수 있다.

## 2. ISTA

reconstruction 항의 gradient는

\[
\nabla_z\frac12\lVert a-Dz\rVert_2^2=D^T(Dz-a)
\]

다. gradient step 뒤 soft thresholding을 적용하면

\[
z^{(k+1)}=S_{\eta\lambda}\left(z^{(k)}-\eta D^T(Dz^{(k)}-a)\right)
\]

을 얻는다. step size는 $D^TD$의 spectral norm에 맞춰 정한다.

## 3. dictionary도 학습할 때

code와 dictionary를 번갈아 갱신할 수 있다. scale 모호성을 막기 위해 dictionary column norm을 제한한다. column permutation과 sign·scale 변환은 같은 reconstruction을 만들 수 있으므로 feature ID는 학습 실행 사이에서 자동으로 정렬되지 않는다.

## 4. 평가

최소한 다음을 함께 본다.

- reconstruction MSE 또는 explained variance
- 표본당 nonzero 수 $L_0$
- coefficient magnitude 분포
- 거의 사용되지 않는 dictionary column
- dictionary coherence
- seed·dictionary size·$\lambda$에 대한 안정성

낮은 reconstruction error만으로 해석 가능한 feature를 얻었다고 결론낼 수 없다.

## CPU 실습

5차원 activation을 8개 dictionary column 중 두 개의 조합으로 생성한다. 고정 dictionary에서 ISTA로 code를 추정하고 reconstruction과 active fraction을 기록한다.

<!-- I06_EXAMPLE: i06_11_sparse_coding -->

추정 code가 ground truth보다 덜 sparse할 수 있다. dictionary coherence와 penalty가 support recovery에 영향을 주기 때문이다.

## 흔한 오해

### 오해 1. sparse code는 언제나 유일하다

dictionary column이 비슷하거나 목적함수 조건이 부족하면 여러 code가 비슷한 reconstruction을 낼 수 있다.

### 오해 2. $L_1$은 정확한 $L_0$와 같다

$L_1$은 convex surrogate다. 작은 nonzero coefficient가 남을 수 있어 threshold를 명시한다.

### 오해 3. reconstruction이 좋으면 feature 의미도 좋다

재구성은 fidelity metric이다. human interpretability, stability와 downstream effect는 별도 평가다.

## 연습문제

### 1. tradeoff

$\lambda$를 크게 하면 일반적으로 reconstruction과 sparsity는 어떻게 변하는가?

<details><summary>해설 보기</summary>code가 더 작고 sparse해지는 대신 reconstruction error가 커질 수 있다. 둘의 frontier를 보고 선택한다.</details>

### 2. gradient

$f(z)=\frac12\lVert a-Dz\rVert^2$의 gradient는 무엇인가?

<details><summary>해설 보기</summary>$D^T(Dz-a)$다. residual을 dictionary direction으로 다시 투영한다.</details>

### 3. soft threshold

threshold가 0.2일 때 값 $0.1,0.5,-0.4$는 어떻게 되는가?

<details><summary>해설 보기</summary>$0,0.3,-0.2$가 된다. 절댓값에서 threshold를 빼고 0 아래는 제거한다.</details>

### 4. scale 모호성

$d_j$를 2배하고 해당 $z_j$를 절반으로 만들면 무엇이 유지되는가?

<details><summary>해설 보기</summary>$d_jz_j$와 reconstruction은 유지된다. 하지만 $L_1$ penalty는 달라지므로 column norm 제약이 필요하다.</details>

### 5. coherence

두 normalized column의 내적 절댓값이 0.99이면 support recovery가 어려운 이유는 무엇인가?

<details><summary>해설 보기</summary>두 방향이 거의 같아 어느 column이 activation을 설명했는지 구분하기 어렵다.</details>

### 6. 해석 주장

MSE가 거의 0이고 평균 $L_0$가 5다. 다섯 latent가 인간 개념이라고 결론낼 수 있는가?

<details><summary>해설 보기</summary>없다. reconstruction과 sparsity만 확인했다. activating example, 설명 평가, 안정성과 기능적 검사가 더 필요하다.</details>

## 근거와 갱신 경계

sparse coding 목적함수는 고전적 dictionary learning의 기본형이다. LLM activation에 적용한 modern SAE는 다음 단원에서 별도 model과 평가 지표로 다룬다. solver별 convergence 조건과 stopping rule은 구현 항목이다.

## 단원 요약

- sparse coding은 reconstruction error와 sparsity penalty를 함께 최소화한다.
- ISTA는 gradient step과 soft thresholding을 번갈아 적용한다.
- dictionary scale·permutation과 유사 column 때문에 feature가 비유일할 수 있다.
- reconstruction, sparsity, dead usage와 안정성을 함께 본다.

## 통과 기준

- sparse coding 목적함수의 두 항을 설명할 수 있는가?
- ISTA 한 step을 계산할 수 있는가?
- sparse code의 비유일성과 평가 한계를 쓸 수 있는가?

## 다음 단원

- [I06-12 sparse autoencoder](I06-12-sparse-autoencoder.md)

## 집필자 점검표

- [x] reconstruction·sparsity·비유일성을 연결했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
