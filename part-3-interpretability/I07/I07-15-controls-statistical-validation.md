---
id: "I07-15"
title: "대조군과 통계 검증"
part: 3
stage: "I07"
status: "완료"
prerequisites: ["I07-14", "M04-17"]
estimated_time: "120~150분"
---

# I07-15. 대조군과 통계 검증

## 이 단원이 필요한 이유

한 prompt와 한 component에서 큰 patch effect를 얻는 것은 재현 가능한 circuit 증거가 아니다. 입력이 experimental unit인지, seed가 반복인지, token별 값이 독립 표본인지 먼저 정해야 한다. Matched control, paired design, 불확실성과 다중비교를 개입 설계에 연결한다.

## 학습 목표

- 개입 실험의 experimental unit을 정의할 수 있다.
- random·matched·resampled control을 목적별로 설계할 수 있다.
- paired effect의 평균, bootstrap interval과 sign-flip 검정을 해석할 수 있다.
- 위치 탐색과 confirmatory 평가를 분리할 수 있다.

## 선수지식 확인

- 선수 단원: [I07-14 off-manifold intervention](I07-14-off-manifold-intervention.md), [M04-17 실험 설계와 재현성](../../part-1-foundations/M04/M04-17-experimental-design-reproducibility.md)
- 확인 질문: 한 prompt 안의 여러 token effect를 독립 표본처럼 세면 pseudoreplication이 되는 이유는 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $d_i=y_i^{(1)}-y_i^{(0)}$ | `d sub i equals y sub i one minus y sub i zero` | unit $i$의 paired effect | scalar |
| $\bar d$ | `d bar` | paired effect 평균 | scalar |
| $H_0:\mathbb E[d]=0$ | `H naught: the expectation of d equals zero` | 평균 개입 효과가 0이라는 귀무가설 | hypothesis |
| sign-flip test | `sign flip test` | paired 차이 부호를 무작위화하는 검정 | randomization test |
| family-wise search | `family-wise search` | 여러 node·edge를 함께 탐색하는 분석 | comparison family |

## 1. 분석 단위

Prompt가 독립적으로 표집됐다면 같은 prompt의 intact와 patched metric 차이

$$
d_i=m_i^{\mathrm{patched}}-m_i^{\mathrm{base}}
$$

가 분석 단위다. 한 prompt의 20개 token을 20개 독립 unit로 세면 공통 입력과 forward state를 무시한다. Seed 반복도 독립 데이터 표본과 같지 않다.

## 2. control의 역할

- random location: 어디를 바꿔도 생기는 일반 교란과 비교
- magnitude-matched: activation 규모 차이와 비교
- resampled source: 특정 clean pair의 우연한 일치를 검사
- sham intervention: hook·복사 과정 자체의 변화를 검사
- label permutation: 행동 metric과 component 선택의 연결을 끊음

Control도 task condition과 같은 tuning budget을 사용한다.

## 3. 불확실성과 검정

Paired bootstrap은 unit index를 재표집해 $\bar d$ interval을 만든다. Sign-flip test는 귀무 아래 각 paired difference의 부호가 대칭이라는 가정으로 null distribution을 만든다. 입력 수가 적을 때 정규근사 p-value만 보고하지 않는다.

## 4. 다중비교와 holdout

Layer×token×component를 훑어 peak를 찾았다면 그 전체가 selection family다. Discovery set에서 후보를 고르고 confirmatory set에서 위치와 metric을 고정해 평가한다. 같은 데이터를 여러 번 보며 후보를 바꾸면 holdout이 아니다.

## 5. CPU 실습

<!-- I07_EXAMPLE: i07_15_controls_statistics -->

8개 독립 unit의 task effect와 matched control을 paired하게 빼고 bootstrap 95% interval과 sign-flip p-value를 계산한다. 이 예제의 unit 수는 8이며 effect vector의 내부 숫자를 독립 표본으로 늘리지 않는다.

## 흔한 오해

### 오해 1. token 수가 많으면 표본 수도 많다

같은 prompt와 실행에서 나온 token은 강하게 의존한다. 표집 단위와 개입 배정 단위를 기준으로 experimental unit을 정한다.

### 오해 2. p-value가 작으면 circuit이 맞다

검정은 정의한 effect가 null과 양립하는지 평가할 뿐, graph의 완전성·타당성·일반화를 보장하지 않는다.

## 연습문제

### 1. paired effect

세 prompt의 patched metric이 $(3,4,5)$, base metric이 $(1,3,2)$일 때 $d_i$와 평균을 구하라.

<details>
<summary>해설 보기</summary>

$d=(2,1,3)$이고 평균은 2이다.

</details>

### 2. pseudoreplication

10개 prompt마다 20개 token effect가 있을 때 독립 unit이 자동으로 200개가 아닌 이유를 설명하라.

<details>
<summary>해설 보기</summary>

같은 prompt의 token은 입력, model state와 corruption을 공유한다. 독립 표집 단위가 prompt라면 기본 unit 수는 10이다.

</details>

### 3. matched control

큰 activation norm의 head를 선택한 실험에 적절한 control을 제시하라.

<details>
<summary>해설 보기</summary>

같은 layer에서 norm이나 output variance가 비슷한 head를 무작위 선택해 동일 개입을 적용한다.

</details>

### 4. sign flip

모든 paired difference의 부호를 뒤집어도 된다는 null 가정은 무엇을 뜻하는가?

<details>
<summary>해설 보기</summary>

귀무 아래 effect distribution이 0을 중심으로 대칭이라 양·음 부호가 교환 가능하다는 뜻이다.

</details>

### 5. selection family

12 layer×20 token×2 component를 탐색했다면 후보 검정 수는 얼마인가?

<details>
<summary>해설 보기</summary>

$12\times20\times2=480$이다. peak 하나만 보고해도 선택은 480개 family에서 일어났다.

</details>

### 6. 결과 해석

Effect interval이 0을 제외하지만 random control도 같은 크기다. 어떤 결론이 적절한가?

<details>
<summary>해설 보기</summary>

개입은 재현 가능한 변화를 만들었지만 선택 component에 특이적인 효과라는 증거는 없다. 일반적인 교란 또는 규모 효과를 배제하지 못했다고 쓴다.

</details>

## 근거와 갱신 경계

Activation patching의 metric·corruption 선택 민감성은 [Zhang and Nanda (2023)](https://arxiv.org/abs/2309.16042), circuit의 held-out 정량 검증은 [Wang et al. (2022)](https://arxiv.org/abs/2211.00593)을 기준으로 한다. 통계 검정은 실험 설계의 결함을 대체하지 않는다.

## 단원 요약

- 분석 단위는 표집·개입 배정 단위로 정한다.
- random·matched·resampled·sham control은 서로 다른 교란을 검사한다.
- paired bootstrap과 sign-flip test는 unit-level effect에 적용한다.
- 탐색 family와 confirmatory holdout을 분리해야 한다.

## 통과 기준

- experimental unit과 paired effect를 정의할 수 있는가?
- 목적이 다른 control을 설계할 수 있는가?
- selection family와 held-out 검증을 설명할 수 있는가?

## 다음 단원

- [I07-16 CoT faithfulness 평가](I07-16-cot-faithfulness.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] experimental unit과 pseudoreplication을 구분했다.
- [x] control·paired design·다중비교를 연결했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
