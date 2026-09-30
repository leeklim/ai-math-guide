---
id: "I06-10"
title: "superposition"
part: 3
stage: "I06"
status: "완료"
prerequisites: ["I06-09", "M02-02"]
estimated_time: "110~140분"
---

# I06-10. superposition

## 이 단원이 필요한 이유

feature 수가 representation dimension보다 많으면 모든 feature를 서로 직교한 좌표에 하나씩 놓을 수 없다. 입력마다 소수 feature만 활성화된다면 여러 feature direction을 같은 공간에 겹쳐 넣고 간섭을 감수하는 해가 유용할 수 있다. 이 관점은 neuron과 feature가 일대일이 아닐 수 있는 수학적 이유를 준다.

## 학습 목표

- overcomplete feature dictionary와 sparse coefficient를 구분할 수 있다.
- feature 수가 차원보다 많을 때 직교 배치가 불가능함을 설명할 수 있다.
- Gram matrix로 feature direction 사이 간섭을 계산할 수 있다.
- toy model의 superposition 결과를 실제 LLM의 확정 사실로 과장하지 않을 수 있다.

## 선수지식 확인

- 선수 단원: [I06-09 feature visualization](I06-09-feature-visualization.md), [M02-02 선형결합과 생성공간](../../part-1-foundations/M02/M02-02-linear-combinations-span.md)
- 확인 질문: 2차원 공간에 서로 직교한 nonzero vector를 세 개 둘 수 있는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $D=[d_1,\ldots,d_m]$ | `dictionary D with columns d one through d m` | feature direction을 열로 둔 dictionary | $d\times m$ |
| $z$ | `sparse feature vector z` | 입력에서 활성화된 feature coefficient | $\mathbb R^m$ |
| $a=Dz$ | `a equals D z` | feature 조합으로 만든 representation | $\mathbb R^d$ |
| overcomplete dictionary | `overcomplete dictionary` | 열 수가 ambient dimension보다 많은 dictionary | $m>d$ |
| $G=D^TD$ | `Gram matrix D transpose D` | feature direction 사이 내적 | $m\times m$ |
| interference | `feature interference` | 다른 feature가 dot-product decoding에 섞이는 효과 | scalar 또는 vector |

## 1. feature와 neuron을 분리한다

feature를 입력의 의미 있는 속성, neuron을 representation의 좌표라고 부르자. feature coefficient $z$가 sparse이고 dictionary $D$가 있으면

\[
a=Dz
\]

로 dense activation을 만들 수 있다. $m>d$이면 feature가 coordinate보다 많다. 각 feature를 별도 coordinate에 놓는 monosemantic 배치는 불가능하지만, 동시에 활성화되는 feature가 적다면 비직교 방향으로 저장할 수 있다.

## 2. Gram matrix와 간섭

dictionary column이 unit norm일 때 $G=D^TD$의 대각은 1이다. 비대각 $G_{jk}=d_j^Td_k$는 두 feature direction의 겹침이다. 단순 dot-product decoder는

\[
D^Ta=D^TDz=Gz
\]

를 낸다. $G=I$이면 정확하지만 overcomplete dictionary에서는 모든 비대각을 0으로 만들 수 없다. $Gz-z$가 간섭을 보여준다.

## 3. sparsity가 주는 여지

모든 feature가 항상 동시에 활성화되면 간섭이 누적된다. 각 입력에서 소수 feature만 켜지면 동시에 충돌하는 방향 수가 줄어든다. feature importance, sparsity와 상관구조에 따라 어떤 direction을 거의 직교하게 둘지 달라질 수 있다.

이 설명은 최적화된 toy model에서 관찰되는 geometry를 이해하기 위한 것이다. 실제 model에서 superposition을 입증하려면 feature 정의와 대안 가설, 재현 실험이 필요하다.

## 4. privileged basis

ReLU처럼 coordinate-wise nonlinearity가 있으면 neuron basis가 계산에서 특별한 역할을 갖는다. 그렇더라도 입력 feature가 반드시 개별 neuron과 일치하지는 않는다. `기저 의존적이다`와 `실제 기저가 중요하지 않다`는 다른 문장이다.

## CPU 실습

2차원 원 위에 120도 간격으로 세 unit feature direction을 둔다. 세 feature 중 두 개를 활성화하고 단순 dot-product decoding의 간섭을 계산한다.

<!-- I06_EXAMPLE: i06_10_superposition -->

Gram matrix의 비대각 $-0.5$는 세 방향이 직교하지 않음을 보여준다. 이 구성은 원리를 보이는 toy example이지 실제 model feature의 추정치가 아니다.

## 흔한 오해

### 오해 1. hidden dimension이 768이면 feature도 최대 768개다

서로 직교한 direction은 최대 768개지만 sparse·비직교 표현은 더 많은 feature 후보를 담을 수 있다.

### 오해 2. 비직교 direction은 모두 오류다

간섭과 capacity 사이 tradeoff일 수 있다. decoder와 nonlinear computation이 이를 이용할 수 있다.

### 오해 3. SAE feature가 많으면 superposition이 증명된다

SAE는 선택한 목적함수의 dictionary를 학습한다. latent 수 자체는 원래 model의 ground-truth feature 수를 증명하지 않는다.

## 연습문제

### 1. 차원

$d=3$, $m=5$인 dictionary에서 모든 다섯 column을 서로 직교하게 둘 수 있는가?

<details><summary>해설 보기</summary>없다. 3차원 공간의 서로 독립인 nonzero 직교 vector는 최대 3개다.</details>

### 2. Gram matrix

unit dictionary에서 $G_{12}=0$이면 두 feature direction의 관계는 무엇인가?

<details><summary>해설 보기</summary>서로 직교한다. 하나의 coefficient를 dot product로 읽을 때 다른 하나가 선형 간섭하지 않는다.</details>

### 3. decoding

$G=I$이면 $D^Ta$는 무엇인가?

<details><summary>해설 보기</summary>$D^Ta=Gz=z$이므로 단순 dot-product decoder가 coefficient를 정확히 복원한다.</details>

### 4. sparsity

왜 입력별 active feature 수가 적으면 비직교 저장이 쉬워지는가?

<details><summary>해설 보기</summary>한 입력에서 동시에 간섭하는 direction 수가 줄어든다. 서로 충돌하는 feature가 자주 함께 켜지지 않으면 평균 손실을 낮게 유지할 수 있다.</details>

### 5. basis

coordinate-wise ReLU가 neuron basis를 특별하게 만드는 이유는 무엇인가?

<details><summary>해설 보기</summary>임의 회전은 ReLU와 일반적으로 commute하지 않는다. 각 coordinate에 비선형성을 적용하는 계산 구조가 그 기저를 privileged하게 만든다.</details>

### 6. 증거

한 neuron의 top example이 여러 주제를 포함했다. 이것만으로 superposition을 입증했는가?

<details><summary>해설 보기</summary>아니다. 표본·교란·설명 실패도 가능하다. feature direction, sparsity, 간섭과 대안 설명을 체계적으로 검사해야 한다.</details>

## 근거와 갱신 경계

toy model의 feature sparsity·importance·superposition geometry는 [Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/index.html)을 기준으로 한다. toy model에서의 구성과 실제 LLM의 feature 존재론을 구분한다.

## 단원 요약

- feature direction과 neuron coordinate는 같은 개념이 아니다.
- overcomplete dictionary는 차원보다 많은 비직교 direction을 갖는다.
- Gram matrix의 비대각이 선형 간섭을 나타낸다.
- sparsity는 capacity와 interference의 tradeoff를 바꾼다.

## 통과 기준

- $a=Dz$에서 feature, coefficient와 neuron coordinate를 구분할 수 있는가?
- Gram matrix로 간섭을 계산할 수 있는가?
- toy superposition 결과의 주장 범위를 제한할 수 있는가?

## 다음 단원

- [I06-11 sparse coding](I06-11-sparse-coding.md)

## 집필자 점검표

- [x] superposition을 dictionary·sparsity·간섭으로 설명했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
