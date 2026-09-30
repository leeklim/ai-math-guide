---
id: "I06-13"
title: "feature 안정성과 identifiability"
part: 3
stage: "I06"
status: "완료"
prerequisites: ["I06-12", "M03-15"]
estimated_time: "120~150분"
---

# I06-13. feature 안정성과 identifiability

## 이 단원이 필요한 이유

SAE나 dictionary learning을 다시 학습했을 때 같은 feature가 나오지 않으면 개별 latent에 붙인 설명의 재현성이 약하다. permutation, sign과 scale처럼 예측 가능한 대칭을 정렬한 뒤에도 feature가 달라질 수 있다. 개별 direction이 불안정해도 그들이 span하는 subspace는 안정적일 수 있다.

## 학습 목표

- dictionary 비교 전에 permutation·sign·scale 모호성을 정렬할 수 있다.
- cosine matching과 one-to-one assignment를 구분할 수 있다.
- 개별 feature 안정성과 subspace 안정성을 별도로 평가할 수 있다.
- empirical stability와 mathematical identifiability를 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [I06-12 sparse autoencoder](I06-12-sparse-autoencoder.md), [M03-15 재매개화와 model symmetry](../../part-1-foundations/M03/M03-15-reparameterization-model-symmetries.md)
- 확인 질문: dictionary column 순서만 바뀐 두 SAE를 다른 feature set이라고 해야 하는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $d_j^{(1)}$ | `feature direction j from run one` | 첫 학습 실행의 decoder direction | $\mathbb R^d$ |
| $M_{jk}$ | `matching score M sub j k` | 두 실행 feature direction의 유사도 | $[0,1]$ for absolute cosine |
| assignment | `one-to-one assignment` | feature를 중복 없이 대응시키는 matching | permutation |
| feature stability | `feature stability` | 독립 학습에서 비슷한 feature가 다시 나타나는 정도 | empirical property |
| subspace stability | `subspace stability` | feature 묶음의 span이 유지되는 정도 | empirical property |
| identifiability | `identifiability` | 관찰 분포와 가정에서 parameter를 유일하게 정할 수 있는 성질 | theoretical property |

## 1. 대칭을 먼저 제거한다

dictionary column 순서는 loss에 영향을 주지 않는다. encoder·decoder scale을 반대로 바꾸어 같은 reconstruction을 만들 수도 있다. signed feature에서는 부호도 함께 바꿀 수 있다. 따라서 raw column index 비교는 안정성 검사가 아니다.

normalized direction에 대해

\[
M_{jk}=\left|\frac{(d_j^{(1)})^Td_k^{(2)}}{\lVert d_j^{(1)}\rVert\lVert d_k^{(2)}\rVert}\right|
\]

를 계산하고 one-to-one assignment의 총 score를 최대화한다. absolute value를 쓸지는 activation의 부호 의미에 따라 정한다.

## 2. greedy matching과 assignment

각 feature가 가장 가까운 상대를 독립적으로 고르면 여러 feature가 같은 column에 몰릴 수 있다. dictionary 전체 대응을 원하면 Hungarian algorithm 같은 one-to-one assignment가 필요하다. unmatched feature 비율도 결과다.

matching threshold는 결과를 본 뒤 정하지 않는다. null dictionary나 random direction에서 나오는 cosine 분포를 기준으로 false match를 확인할 수 있다.

## 3. feature와 subspace 안정성

두 실행에서 개별 direction이 다르지만 모두 같은 저차원 span 안에 있을 수 있다. 이때 principal angle, projection matrix 거리나 CKA로 subspace 안정성을 본다. 개별 feature가 identifiable하다는 주장은 못 하지만 representation region이 재현된다는 증거는 남는다.

## 4. identifiability는 더 강한 말이다

여러 seed에서 비슷한 feature가 나온 empirical stability는 유용하지만, 가능한 모든 solution 중 유일하다는 증명은 아니다. mathematical identifiability에는 데이터 생성 가정, dictionary incoherence, sparsity와 충분한 표본 같은 조건이 필요하다.

반대로 이론적으로 identifiable한 설정도 finite sample, optimization failure와 local minimum 때문에 실험에서 불안정할 수 있다.

## CPU 실습

첫 dictionary를 permutation·sign change하고 작은 noise를 더해 둘째 dictionary를 만든다. raw diagonal cosine과 optimal one-to-one matching 뒤 cosine을 비교한다.

<!-- I06_EXAMPLE: i06_13_feature_stability -->

높은 matched score는 이 합성 변환을 복원했다는 뜻이다. 실제 SAE에서는 unmatched, split·merge와 subspace-only correspondence를 함께 보고한다.

## 흔한 오해

### 오해 1. index가 같아야 같은 feature다

latent permutation은 기본 대칭이다. direction과 activation pattern을 정렬해야 한다.

### 오해 2. cosine이 높은 pair가 많으면 전체 dictionary가 안정적이다

여러 source feature가 한 target에 몰릴 수 있다. one-to-one coverage와 unmatched 비율을 본다.

### 오해 3. seed 두 개가 일치하면 identifiable하다

그 두 최적화 실행의 안정성 증거다. 유일성에 관한 수학적 결론은 아니다.

## 연습문제

### 1. permutation

두 dictionary가 column 순서만 다르면 reconstruction model은 달라졌는가?

<details><summary>해설 보기</summary>encoder latent와 decoder column을 같은 permutation으로 바꾸면 함수는 같다. raw index 차이는 feature 차이가 아니다.</details>

### 2. absolute cosine

왜 absolute cosine을 쓸 수 있으며 언제 부적절할 수 있는가?

<details><summary>해설 보기</summary>부호를 함께 뒤집어도 같은 signed direction으로 볼 때 사용한다. ReLU nonnegative feature처럼 부호가 기능적으로 비대칭이면 절댓값이 다른 feature를 합칠 수 있다.</details>

### 3. many-to-one

greedy nearest neighbor가 안정성을 과대평가하는 경우를 설명하라.

<details><summary>해설 보기</summary>첫 dictionary의 여러 feature가 둘째 dictionary의 같은 feature를 가장 가깝다고 고르면 높은 pair score가 반복된다. one-to-one assignment와 coverage가 이를 막는다.</details>

### 4. subspace

개별 match는 낮지만 projection matrix가 비슷하다. 어떤 주장이 가능한가?

<details><summary>해설 보기</summary>개별 basis direction은 불안정하지만 그 feature 묶음이 span하는 subspace는 재현될 수 있다는 주장이다.</details>

### 5. null match

matching threshold를 random dictionary와 비교하는 이유는 무엇인가?

<details><summary>해설 보기</summary>고차원·많은 후보에서는 우연히 높은 최대 cosine이 생긴다. null 분포가 false match의 기준을 준다.</details>

### 6. identifiability

세 seed에서 같은 feature가 나왔다. `유일하게 식별됐다`고 써도 되는가?

<details><summary>해설 보기</summary>경험적 재현성은 높아졌지만 모든 동등 solution을 배제한 것은 아니다. 가정 아래 identifiability 증명과 구분한다.</details>

## 근거와 갱신 경계

SAE dictionary의 seed 불안정성은 [Archetypal SAE](https://openreview.net/forum?id=9v1eW8HgMU)와 2026년 preprint [Unstable Features, Reproducible Subspaces](https://arxiv.org/abs/2606.12138)를 확인했다. 후자는 최신 preprint이므로 개별 결론을 확정된 일반 법칙으로 사용하지 않고 feature·subspace 안정성을 분리해야 할 근거로만 쓴다.

## 단원 요약

- dictionary 비교 전에 permutation·sign·scale 대칭을 처리한다.
- one-to-one assignment, coverage와 null match를 함께 본다.
- 개별 feature와 subspace의 안정성은 다를 수 있다.
- empirical stability는 mathematical identifiability보다 약한 주장이다.

## 통과 기준

- 두 dictionary를 symmetry-aware matching으로 비교할 수 있는가?
- feature와 subspace 안정성을 구분할 수 있는가?
- stability 결과를 identifiability로 과장하지 않을 수 있는가?

## 다음 단원

- [I06-14 표현 주장 작성](I06-14-writing-representation-claims.md)

## 집필자 점검표

- [x] feature·subspace 안정성과 identifiability를 분리했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
