---
id: "I06-09"
title: "feature visualization"
part: 3
stage: "I06"
status: "완료"
prerequisites: ["I06-08"]
estimated_time: "100~130분"
---

# I06-09. feature visualization

## 이 단원이 필요한 이유

feature direction이나 neuron을 숫자 하나로만 보면 무엇에 반응하는지 가설을 만들기 어렵다. dataset example을 activation score로 정렬하거나 입력을 최적화하면 선호 패턴을 볼 수 있다. 이 결과는 feature의 완전한 의미나 기능적 역할이 아니라 반응 조건에 대한 관찰이다.

## 학습 목표

- neuron과 direction에 대한 activation objective를 정의할 수 있다.
- top·bottom dataset example과 random baseline을 함께 제시할 수 있다.
- activation maximization에서 regularization의 역할을 설명할 수 있다.
- visualization에서 만든 설명을 독립 입력으로 평가할 수 있다.

## 선수지식 확인

- 선수 단원: [I06-08 CCA, CKA와 RSA](I06-08-cca-cka-rsa.md)
- 확인 질문: top activating example만 보면 false positive를 알 수 있는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $s_f(x)$ | `feature score s sub f of x` | 입력 $x$에서 feature $f$의 activation score | scalar |
| top-$k$ examples | `top k examples` | score가 가장 큰 $k$개 입력 | ranked subset |
| activation maximization | `activation maximization` | score를 크게 만드는 입력을 최적화하는 방법 | optimization procedure |
| regularizer | `regularizer` | 입력이 허용 범위를 벗어나는 것을 억제하는 항 | objective term |
| hard negative | `hard negative` | 설명과 비슷하지만 feature가 반응하지 않아야 하는 입력 | test example |
| feature description | `feature description` | 관찰 예에서 만든 반응 가설 | human-readable hypothesis |

## 1. score를 먼저 정의한다

neuron이면 $s_f(x)=a_j(x)$로 둘 수 있다. direction $v$이면

\[
s_f(x)=v^Ta(x)
\]

로 projection을 사용한다. token별 activation이라면 max, mean, 특정 token 중 무엇을 score로 썼는지 적는다. 부호가 중요한 direction에서는 top과 bottom을 모두 본다.

## 2. dataset example

고정 dataset에서 score를 계산해 top-$k$, bottom-$k$와 무작위 예를 나란히 본다. 상위 예만 제시하면 전체 base rate와 feature의 비선택성을 숨길 수 있다. 입력 text뿐 아니라 어느 token에서 score가 측정됐는지 표시한다.

설명 후보를 만든 뒤 별도 validation set에서 다음을 평가한다.

- 설명에 맞는 positive에서 activation하는가?
- 비슷한 hard negative에서 낮은가?
- paraphrase와 position 변경에 유지되는가?
- 특정 token ID나 길이만 추적한 것은 아닌가?

## 3. 입력 최적화

미분 가능한 입력 $x$에서는

\[
\max_x\ s_f(x)-\lambda R(x)
\]

를 풀 수 있다. $R(x)$는 natural image prior, norm, smoothness 같은 제약이다. 제약이 없으면 model이 강하게 반응하지만 데이터 분포에서는 보기 어려운 artifact가 나올 수 있다.

언어 model의 discrete token은 직접 gradient ascent하기 어렵다. embedding 최적화, token search와 생성 model을 이용한 후보 생성은 각각 다른 허용 입력 공간을 만든다. 결과가 자연어처럼 보여도 훈련 분포 위에 있다는 보장은 없다.

## 4. visualization과 기능

feature가 특정 예에 반응한다는 사실은 관찰이다. 해당 feature를 제거하거나 증폭했을 때 행동이 예측대로 바뀌는지는 개입 질문이다. visualization 설명을 개입 target으로 사용할 수 있지만 두 결과를 같은 증거로 합치지 않는다.

## CPU 실습

합성 representation에서 고정 direction의 score를 계산하고 top·bottom 다섯 입력을 고른다. label은 정렬에 사용하지 않고, 정렬 뒤 상위 예의 label 비율을 확인한다.

<!-- I06_EXAMPLE: i06_09_feature_visualization -->

상위 label 비율이 높아도 같은 자료에서 만든 관찰이다. 독립 validation과 hard negative가 다음 단계다.

## 흔한 오해

### 오해 1. top example의 공통점이 feature의 정의다

설명 후보다. 선택하지 않은 입력과 counterexample에서 예측력을 검사해야 한다.

### 오해 2. 최적화 입력이 이상하면 feature도 가짜다

optimization parameterization과 regularizer가 artifact를 만들 수 있다. dataset example과 여러 parameterization을 함께 본다.

### 오해 3. 사람이 그럴듯한 설명을 붙이면 객관적이다

평가자 편향과 모호성이 있다. 설명 생성용 예와 scoring용 예를 분리하고 평가 규칙을 기록한다.

## 연습문제

### 1. direction score

$v=(1,0)$, $a(x)=(2,3)$이면 $v^Ta(x)$는 얼마인가?

<details><summary>해설 보기</summary>2다. 둘째 좌표는 이 direction score에 기여하지 않는다.</details>

### 2. bottom example

signed direction에서 bottom example이 필요한 이유는 무엇인가?

<details><summary>해설 보기</summary>반대 방향의 패턴과 score의 비대칭을 보여준다. top만 보면 feature 축의 한쪽만 관찰한다.</details>

### 3. base rate

top 10개 중 8개가 질문문이고 dataset 전체의 90%가 질문문이다. 선택적이라고 할 수 있는가?

<details><summary>해설 보기</summary>오히려 top의 질문문 비율이 전체보다 낮다. 전체 base rate와 비교해야 한다.</details>

### 4. regularizer

activation maximization에 smoothness penalty를 넣는 이유는 무엇인가?

<details><summary>해설 보기</summary>고주파 artifact처럼 score는 높지만 자연 자료에서 보기 어려운 입력을 억제하려는 것이다. penalty가 의미를 보장하지는 않는다.</details>

### 5. 독립 평가

설명을 만든 top example로 설명 정확도를 다시 채점하면 어떤 문제가 있는가?

<details><summary>해설 보기</summary>가설 생성과 평가가 같은 자료를 사용해 과대평가된다. 별도 입력과 hard negative에서 채점한다.</details>

### 6. 인과 주장

`Paris`가 최고 score였다. feature가 수도 답변을 만든 원인이라고 결론낼 수 있는가?

<details><summary>해설 보기</summary>없다. 반응 관찰일 뿐이다. 통제된 ablation·patching과 행동 측정이 필요하다.</details>

## 근거와 갱신 경계

dataset example, activation maximization과 regularization의 한계는 [Feature Visualization](https://distill.pub/2017/feature-visualization/)을 기준으로 설명했다. image의 natural prior와 언어 token search는 서로 다른 구현 문제다.

## 단원 요약

- feature score와 token aggregation을 먼저 고정한다.
- top·bottom·random example과 base rate를 함께 본다.
- 최적화 입력은 regularizer와 입력 parameterization에 의존한다.
- visualization 설명은 독립 자료로 검증하며 인과 증거와 구분한다.

## 통과 기준

- feature score와 top-$k$ 절차를 명세할 수 있는가?
- dataset example과 activation maximization의 차이를 설명할 수 있는가?
- 설명 검증용 positive·hard negative를 설계할 수 있는가?

## 다음 단원

- [I06-10 superposition](I06-10-superposition.md)

## 집필자 점검표

- [x] visualization을 가설 생성과 검증으로 나눴다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
