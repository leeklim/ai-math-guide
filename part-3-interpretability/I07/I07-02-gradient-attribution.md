---
id: "I07-02"
title: "gradient 기반 귀인"
part: 3
stage: "I07"
status: "완료"
prerequisites: ["I07-01", "N05-26"]
estimated_time: "90~120분"
---

# I07-02. gradient 기반 귀인

## 이 단원이 필요한 이유

gradient는 역전파 한 번으로 많은 입력 좌표의 민감도를 동시에 계산한다. 하지만 raw gradient, saliency와 gradient×input은 서로 다른 값을 보고하며 saturation, 입력 단위와 부호 처리에 영향을 받는다. 계산이 빠르다는 사실과 설명이 타당하다는 주장을 분리해야 한다.

## 학습 목표

- raw gradient, saliency와 gradient×input을 계산할 수 있다.
- 부호와 절댓값이 답하는 질문을 구분할 수 있다.
- saturation과 입력 scale이 gradient 해석에 미치는 영향을 설명할 수 있다.
- autograd 결과를 작은 손계산으로 검산할 수 있다.

## 선수지식 확인

- 선수 단원: [I07-01 민감도와 귀인](I07-01-sensitivity-attribution.md), [N05-26 activation gradient와 intervention](../../part-2-neural-computation/N05/N05-26-gradient-collection-intervention-preparation.md)
- 확인 질문: scalar score를 선택해야 `backward()` 뒤 입력과 같은 shape의 gradient를 얻는 이유는 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $g_i=\frac{\partial s}{\partial x_i}$ | `g sub i equals partial s over partial x sub i` | signed local sensitivity | scalar |
| $\lvert g_i\rvert$ | `the absolute value of g sub i` | saliency magnitude | nonnegative scalar |
| $x_i g_i$ | `x sub i times g sub i` | zero-baseline gradient×input | scalar |
| $\nabla_x s$ | `the gradient of s with respect to x` | 모든 좌표의 gradient | $\mathbb R^d$ |
| saturation | `saturation` | 출력 변화에 비해 국소 gradient가 작은 영역 | local property |

## 1. 세 가지 출력

raw gradient는 증가 방향과 감소 방향을 부호로 보존한다. saliency는 $|g_i|$로 방향을 버리고 크기만 본다. gradient×input은 zero baseline에서 현재 입력까지의 변위를 곱한 일차 Taylor 항이다.

$$
s(x)-s(0)\approx \nabla_x s(x)^\top x=\sum_i x_i g_i
$$

비선형 함수에서는 근사일 뿐이다. 항의 합이 실제 score 차이와 같지 않아도 autograd가 틀린 것은 아니다.

## 2. 손계산

$s=x_1x_2+x_3^2$, $x=(2,3,1)$이면

$$
\nabla_x s=(3,2,2),\qquad x\odot\nabla_xs=(6,6,2).
$$

gradient×input 합은 14이고 $s(x)-s(0)=7$이다. 곱과 제곱의 중복 계수 때문에 completeness가 성립하지 않는다.

## 3. scale과 saturation

단위를 $x_i'=c x_i$로 바꾸면 raw gradient는 chain rule에 따라 $1/c$ 배 변할 수 있다. 서로 다른 feature의 gradient 절댓값을 비교할 때 입력 단위를 확인해야 한다.

sigmoid처럼 포화되는 함수는 출력이 baseline과 크게 달라도 현재 점의 gradient가 거의 0일 수 있다. 이는 해당 feature가 역사적으로 중요하지 않았다는 뜻이 아니다.

## 4. CPU 실습

<!-- I07_EXAMPLE: i07_02_gradient_attribution -->

PyTorch가 계산한 gradient $(3,2,2)$를 손계산과 대조한다. `gradient_times_input_sum`은 score 차이와 같지 않으며 그 차이를 숨기지 않는다.

## 흔한 오해

### 오해 1. 절댓값을 취해도 정보가 줄지 않는다

절댓값은 score를 올리는 방향과 내리는 방향을 합친다. 질문이 방향을 포함하면 signed gradient를 보존해야 한다.

### 오해 2. gradient×input은 언제나 완전한 분해다

선형 동차 함수 등 특정 조건에서는 맞지만 일반 비선형 함수에는 보장되지 않는다.

## 연습문제

### 1. raw gradient

$s=2x_1-x_2^2$에서 $x=(3,2)$의 gradient를 구하라.

<details>
<summary>해설 보기</summary>

$\partial s/\partial x_1=2$, $\partial s/\partial x_2=-2x_2=-4$이므로 $(2,-4)$이다.

</details>

### 2. saliency

앞 문제의 saliency와 raw gradient가 잃고 보존하는 정보를 설명하라.

<details>
<summary>해설 보기</summary>

saliency는 $(2,4)$이며 두 번째 좌표가 더 민감하다는 크기는 보존하지만, 그 좌표를 늘리면 score가 감소한다는 부호는 잃는다.

</details>

### 3. gradient×input

앞 함수와 점에서 gradient×input을 계산하라.

<details>
<summary>해설 보기</summary>

$(3,2)\odot(2,-4)=(6,-8)$이다. 합은 $-2$이고 실제 $s(3,2)-s(0,0)=2$와 다르다.

</details>

### 4. saturation

sigmoid 출력이 거의 1인 점에서 gradient가 작은 이유를 설명하라.

<details>
<summary>해설 보기</summary>

sigmoid 도함수는 $\sigma(z)(1-\sigma(z))$이다. $\sigma(z)\approx1$이면 두 번째 인자가 거의 0이므로 국소 gradient가 작다.

</details>

### 5. 단위 변경

meter 입력을 centimeter로 바꿀 때 raw gradient 크기가 달라질 수 있는 이유는 무엇인가?

<details>
<summary>해설 보기</summary>

같은 물리량을 $x'=100x$로 쓰면 $\partial s/\partial x'=(1/100)\partial s/\partial x$이다. 숫자 크기 비교에는 입력 단위가 포함된다.

</details>

### 6. 주장 범위

높은 gradient를 발견한 뒤 기능적 사용을 확인하려면 무엇을 추가해야 하는가?

<details>
<summary>해설 보기</summary>

해당 입력 또는 내부 상태를 조작하고 동일 입력의 출력 변화를 paired하게 측정해야 한다. 현실적인 baseline과 무작위·matched control도 필요하다.

</details>

## 근거와 갱신 경계

입력 gradient 기반 시각화는 [Simonyan et al. (2013)](https://arxiv.org/abs/1312.6034)을 출발점으로 삼는다. 이 단원은 gradient를 local sensitivity로 다루며 이후 개입 결과와 동일시하지 않는다.

## 단원 요약

- raw gradient는 부호 있는 국소 민감도이고 saliency는 그 절댓값이다.
- gradient×input은 zero-baseline 일차 근사이며 일반적으로 완전한 분해가 아니다.
- saturation과 입력 단위가 결과를 바꾼다.
- 빠른 계산은 인과 타당성을 보장하지 않는다.

## 통과 기준

- 세 gradient 기반 값을 손으로 계산할 수 있는가?
- saturation과 scale 문제를 설명할 수 있는가?
- autograd 결과를 손계산과 대조할 수 있는가?

## 다음 단원

- [I07-03 integrated gradients와 baseline](I07-03-integrated-gradients-baseline.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] raw gradient·saliency·gradient×input을 구분했다.
- [x] saturation과 scale 한계를 포함했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
