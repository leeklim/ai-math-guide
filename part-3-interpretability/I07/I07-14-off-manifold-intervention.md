---
id: "I07-14"
title: "off-manifold intervention"
part: 3
stage: "I07"
status: "완료"
prerequisites: ["I07-13", "I06-13"]
estimated_time: "90~120분"
---

# I07-14. off-manifold intervention

## 이 단원이 필요한 이유

Neuron 하나만 0으로 만들거나 서로 다른 prompt의 좌표를 섞으면 학습 중 나타나지 않은 내부 상태를 만들 수 있다. Downstream model은 그런 상태에서 임의적인 출력을 낼 수 있다. 큰 intervention effect가 발견돼도 먼저 개입 상태가 원래 activation 분포와 얼마나 벗어났는지 확인해야 한다.

## 학습 목표

- activation manifold와 off-manifold 상태를 조작적으로 정의할 수 있다.
- 작은 예제에서 manifold distance를 계산할 수 있다.
- resample·projection·subspace intervention의 tradeoff를 설명할 수 있다.
- 개입 효과와 개입 타당성을 별도 표에 보고할 수 있다.

## 선수지식 확인

- 선수 단원: [I07-13 mediation과 counterfactual](I07-13-mediation-counterfactual.md), [I06-13 feature 안정성과 identifiability](../I06/I06-13-feature-stability-identifiability.md)
- 확인 질문: 두 실행의 activation 좌표를 일부씩 섞을 때 원래 공분산 구조가 깨질 수 있는 이유는 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\mathcal M$ | `calligraphic M` | 관찰 activation이 놓인 집합·근사 manifold | subset of $\mathbb R^d$ |
| $\tilde h$ | `h tilde` | 개입으로 만든 activation | $\mathbb R^d$ |
| $d(\tilde h,\mathcal M)$ | `the distance from h tilde to calligraphic M` | 개입 상태의 manifold 거리 | nonnegative scalar |
| on-manifold | `on manifold` | 참조 activation 구조와 양립하는 상태 | validity label |
| off-manifold | `off manifold` | 참조분포에서 벗어난 상태 | validity warning |

## 1. 간단한 반례

관찰 activation이 항상 $h=(z,z)$ 꼴이면 manifold는 직선

$$
\mathcal M=\{(z,z):z\in\mathbb R\}
$$

이다. 좌표 하나만 바꿔 $(1,-1)$을 만들면 이 점은 원래 관계를 깨뜨린다. 직선까지 거리는

$$
d((h_1,h_2),\mathcal M)=\frac{|h_1-h_2|}{\sqrt2}
$$

이므로 $(1,-1)$의 거리는 $\sqrt2$이다.

## 2. 타당성 진단

- 참조 activation의 nearest-neighbor distance
- PCA residual 또는 covariance Mahalanobis distance
- decoder reconstruction error
- density model score
- downstream norm·normalization 통계
- 동일 의미를 가진 실제 source activation과의 비교

고차원에서 한 metric만으로 manifold를 확정하지 않는다.

## 3. 완화 방법

- 다른 실제 입력에서 얻은 activation을 resample한다.
- feature subspace 안에서 이동하고 나머지는 조건부 복원한다.
- decoder를 거쳐 reconstruction한 값을 사용한다.
- 여러 baseline과 patch granularity로 sensitivity analysis를 한다.

이 방법도 완전한 on-manifold를 보장하지 않는다. 효과와 거리 지표를 함께 보고한다.

## 4. CPU 실습

<!-- I07_EXAMPLE: i07_14_off_manifold -->

합성 manifold 위의 clean·valid counterfactual과 좌표 혼합 patch를 비교한다. Off-manifold patch의 downstream output이 크게 달라도 의미 있는 counterfactual이라고 결론 내리지 않는다.

## 흔한 오해

### 오해 1. 큰 효과는 강한 causal evidence다

분포 밖 상태에 대한 비정상 반응일 수 있다. 효과 크기와 개입 타당성은 별도 축이다.

### 오해 2. 실제 activation에서 좌표를 가져왔으니 on-manifold다

좌표별 source가 다르면 결합이 한 번도 관찰되지 않은 상태일 수 있다.

## 연습문제

### 1. 거리 계산

$h=(2,0)$의 $\mathcal M=\{(z,z)\}$까지 거리를 구하라.

<details>
<summary>해설 보기</summary>

$|2-0|/\sqrt2=\sqrt2$이다.

</details>

### 2. on-manifold 판정

점 $(-3,-3)$은 위 manifold 위에 있는가?

<details>
<summary>해설 보기</summary>

$z=-3$으로 쓸 수 있으므로 manifold 위에 있고 거리는 0이다.

</details>

### 3. coordinate patch

실행 A의 첫 좌표와 실행 B의 둘째 좌표를 합치는 것이 위험한 이유를 설명하라.

<details>
<summary>해설 보기</summary>

각 좌표는 실제 값이어도 둘의 결합은 학습된 공분산과 feature 관계를 깨뜨릴 수 있다.

</details>

### 4. 진단 선택

선형 subspace 근사에서 사용할 수 있는 off-manifold 진단은 무엇인가?

<details>
<summary>해설 보기</summary>

PCA 상위 subspace에 정사영한 뒤 남는 residual norm을 사용할 수 있다. 비선형 manifold에는 제한적임을 함께 적는다.

</details>

### 5. resampling

실제 source activation 전체를 patch하면 어떤 문제를 줄이고 무엇은 남기는가?

<details>
<summary>해설 보기</summary>

좌표 조합의 비현실성은 줄인다. 그러나 source와 base의 문맥 불일치, downstream state와의 hybrid 문제는 남는다.

</details>

### 6. 보고 방식

큰 effect와 큰 manifold distance가 함께 나왔다. 결론을 어떻게 제한해야 하는가?

<details>
<summary>해설 보기</summary>

개입이 출력을 크게 바꿨지만 참조 activation 분포에서 멀어 mechanism 증거로 해석하기 어렵다고 보고한다. 더 현실적인 patch로 재검증한다.

</details>

## 근거와 갱신 경계

Activation patching 방법 선택이 localization을 바꾼다는 실증은 [Zhang and Nanda (2023)](https://arxiv.org/abs/2309.16042), causal abstraction의 aligned intervention 조건은 [Geiger et al. (2021)](https://arxiv.org/abs/2106.02997)을 기준으로 한다. Manifold 진단 하나를 보편적 타당성 증명으로 쓰지 않는다.

## 단원 요약

- 좌표별 개입은 관찰 activation 관계를 깨뜨릴 수 있다.
- 큰 output effect와 on-manifold 타당성은 다른 평가 축이다.
- 거리·reconstruction·resampling 등 여러 진단을 함께 본다.
- 실제 source activation도 base 문맥과 불일치할 수 있다.

## 통과 기준

- 간단한 manifold distance를 계산할 수 있는가?
- off-manifold 반례를 만들 수 있는가?
- 효과와 타당성을 분리해 보고할 수 있는가?

## 다음 단원

- [I07-15 대조군과 통계 검증](I07-15-controls-statistical-validation.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] 효과 크기와 개입 타당성을 분리했다.
- [x] 여러 manifold 진단의 한계를 포함했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
