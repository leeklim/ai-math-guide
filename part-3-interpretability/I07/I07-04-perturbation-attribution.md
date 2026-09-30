---
id: "I07-04"
title: "perturbation 기반 귀인"
part: 3
stage: "I07"
status: "완료"
prerequisites: ["I07-03"]
estimated_time: "90~120분"
---

# I07-04. perturbation 기반 귀인

## 이 단원이 필요한 이유

Perturbation 기반 귀인은 feature를 가리거나 다른 값으로 바꾼 뒤 출력 차이를 측정한다. 미분이 필요 없고 유한한 변화에 답하지만, 무엇으로 대체했는지와 상호작용을 어떤 순서로 끊었는지에 결과가 의존한다. 자연어에서는 token 삭제 자체가 문법과 길이를 바꿀 수 있다.

## 학습 목표

- 단일 feature perturbation effect를 계산할 수 있다.
- zero·mean·resampled baseline의 차이를 설명할 수 있다.
- 상호작용 때문에 단일 효과의 합이 전체 효과와 달라지는 예를 만들 수 있다.
- 입력이 분포 밖으로 이동했는지 검사할 항목을 제시할 수 있다.

## 선수지식 확인

- 선수 단원: [I07-03 integrated gradients와 baseline](I07-03-integrated-gradients-baseline.md)
- 확인 질문: baseline을 바꾸면 어떤 score 차이를 설명하는지가 왜 달라지는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $x^{(i\leftarrow b_i)}$ | `x with coordinate i replaced by b sub i` | $i$번째 feature를 baseline으로 바꾼 입력 | $\mathbb R^d$ |
| $\Delta_i$ | `delta sub i` | 단일 perturbation의 score 차이 | scalar |
| occlusion | `occlusion` | feature를 가리거나 대체하는 개입 | operation |
| resampling | `resampling` | 참조분포에서 대체값을 뽑는 방법 | stochastic operation |
| interaction | `interaction` | 여러 feature 효과가 더해지지 않는 성질 | joint effect |

## 1. 기본 효과

$$
\Delta_i(x;b_i)
=
f(x)-f\bigl(x^{(i\leftarrow b_i)}\bigr).
$$

$\Delta_i>0$이면 그 대체 규칙 아래 원래 feature가 score를 높였다는 뜻이다. feature 자체의 문맥 독립적 가치라는 뜻은 아니다.

## 2. 대체값이 질문을 만든다

- zero: 계산은 단순하지만 실제 입력이 아닐 수 있다.
- mean: 평균적인 상태와 비교하지만 다봉 분포에서는 대표성이 낮다.
- marginal resampling: 주변분포는 따르지만 다른 feature와의 관계를 깨뜨릴 수 있다.
- conditional resampling: 문맥을 보존하려 하지만 별도 생성모형이 필요하다.

token 삭제, mask token, 공백과 다른 token 치환은 서로 다른 개입이다.

## 3. 상호작용

$f(x_1,x_2)=x_1x_2$에서 $(1,1)$의 score는 1이다. 각 좌표를 0으로 바꾸면 효과가 각각 1이므로 단일 효과 합은 2이다. 둘을 함께 제거한 전체 효과 1보다 크다. 같은 상호작용을 두 번 센 결과다.

## 4. CPU 실습

<!-- I07_EXAMPLE: i07_04_perturbation_attribution -->

zero baseline과 mean-like baseline의 단일 feature 효과가 달라지는 것을 확인한다. 어느 쪽이 자동으로 정답인지는 결정하지 않는다.

## 흔한 오해

### 오해 1. perturbation은 gradient보다 항상 인과적이다

실제로 값을 바꾸지만 개입 대상, 대체 분포와 downstream 계산을 명확히 해야 한다. 분포 밖 입력의 출력 차이는 원하는 causal estimand와 다를 수 있다.

### 오해 2. 단일 feature 효과를 더하면 전체 설명이 된다

상호작용이 있으면 순서나 grouping 규칙 없이는 가산 분해가 성립하지 않는다.

## 연습문제

### 1. 단일 효과

$f(x)=2x_1+x_2$, $x=(3,4)$에서 $x_1$을 0으로 바꾼 효과를 구하라.

<details>
<summary>해설 보기</summary>

원래 score는 10, 대체 뒤 score는 4이므로 $\Delta_1=6$이다.

</details>

### 2. baseline 변경

앞 문제에서 $x_1$을 2로 바꾸면 효과는 얼마인가?

<details>
<summary>해설 보기</summary>

대체 score는 $2\cdot2+4=8$이므로 효과는 2이다. 같은 feature도 비교값에 따라 효과가 달라진다.

</details>

### 3. 상호작용

$f=x_1x_2$의 단일 제거 효과 합이 joint 제거 효과와 다른 이유를 설명하라.

<details>
<summary>해설 보기</summary>

곱 항은 두 feature가 함께 있을 때 한 번 생긴다. 각 단일 제거는 같은 곱 항 전체를 없애므로 둘을 더하면 상호작용을 두 번 센다.

</details>

### 4. 자연어 개입

token 삭제와 mask token 치환이 같은 실험이 아닌 이유는 무엇인가?

<details>
<summary>해설 보기</summary>

삭제는 뒤 token 위치와 sequence length를 바꾼다. mask 치환은 길이는 유지하지만 모델이 mask token을 학습하지 않았을 수 있다. 서로 다른 분포 이동을 만든다.

</details>

### 5. 대조군

특정 token을 바꿨을 때 큰 효과가 나왔다. 어떤 matched control을 둘 수 있는가?

<details>
<summary>해설 보기</summary>

같은 위치·빈도·품사처럼 교란 요인을 맞춘 다른 token을 같은 규칙으로 바꾼다. 단순 무작위 위치 control도 함께 보고할 수 있다.

</details>

### 6. 주장 범위

perturbation effect가 크면 해당 feature가 필요하다고 말할 수 있는가?

<details>
<summary>해설 보기</summary>

정의한 대체 개입 아래 출력이 변했다는 증거는 된다. 원래 feature만 제거한 현실적인 counterfactual인지, 다른 정보도 함께 파괴했는지 확인해야 necessity 주장을 제한할 수 있다.

</details>

## 근거와 갱신 경계

입력 일부를 가려 예측 변화를 보는 접근의 대표적 초기 사례는 [Zeiler and Fergus (2014)](https://arxiv.org/abs/1311.2901)이다. 이 단원은 특정 occlusion 값을 보편적 baseline으로 고정하지 않는다.

## 단원 요약

- perturbation effect는 원래 입력과 명시한 대체 입력의 score 차이다.
- 대체값과 resampling 분포가 질문을 결정한다.
- 상호작용이 있으면 단일 효과는 가산적이지 않다.
- 분포 이동과 matched control을 함께 검사해야 한다.

## 통과 기준

- 작은 perturbation effect를 계산할 수 있는가?
- 대체값 세 종류의 장단점을 설명할 수 있는가?
- 상호작용 반례와 대조군을 설계할 수 있는가?

## 다음 단원

- [I07-05 관찰과 개입](I07-05-observation-intervention.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] 대체값과 상호작용을 명시했다.
- [x] 분포 이동과 대조군을 포함했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
