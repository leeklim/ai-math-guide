---
id: "I07-03"
title: "integrated gradients와 baseline"
part: 3
stage: "I07"
status: "완료"
prerequisites: ["I07-02", "M01-08"]
estimated_time: "120~150분"
---

# I07-03. integrated gradients와 baseline

## 이 단원이 필요한 이유

현재 점의 gradient가 saturation 때문에 작을 때, baseline에서 입력까지 이동하며 gradient를 누적할 수 있다. Integrated gradients(IG)는 이 경로 적분을 feature별 귀인값으로 만든다. completeness라는 유용한 성질이 있지만 baseline과 경로가 분석 질문의 일부라는 사실은 사라지지 않는다.

## 학습 목표

- IG 수식의 경로, gradient와 변위 항을 설명할 수 있다.
- 작은 함수의 IG를 계산하고 completeness를 확인할 수 있다.
- baseline을 바꿨을 때 귀인과 해석이 바뀌는 이유를 설명할 수 있다.
- 수치 적분 step과 근사 오차를 보고할 수 있다.

## 선수지식 확인

- 선수 단원: [I07-02 gradient 기반 귀인](I07-02-gradient-attribution.md), [M01-08 적분과 누적](../../part-1-foundations/M01/M01-08-integration-accumulation.md)
- 확인 질문: 선분 $\gamma(\alpha)=x'+\alpha(x-x')$에서 $\alpha=0,1$은 각각 어느 점인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $x'$ | `x prime` | baseline input | $\mathbb R^d$ |
| $\gamma(\alpha)$ | `gamma of alpha` | baseline과 입력을 잇는 경로 | $\alpha\in[0,1]$ |
| $\operatorname{IG}_i(x;x')$ | `integrated gradients sub i of x relative to x prime` | $i$번째 feature의 경로 적분 귀인 | scalar |
| $m$ | `m` | 수치 적분 step 수 | positive integer |
| completeness | `completeness` | 귀인 합이 score 차이와 같은 성질 | equality |

## 1. 정의

직선 경로 IG는 다음과 같다.

$$
\operatorname{IG}_i(x;x')
=
(x_i-x_i')
\int_0^1
\frac{\partial f(\gamma(\alpha))}{\partial x_i}
\,d\alpha,
\qquad
\gamma(\alpha)=x'+\alpha(x-x').
$$

앞의 변위는 feature가 baseline에서 얼마나 이동했는지 나타내고, 적분은 그 이동 동안의 평균 gradient를 모은다.

## 2. completeness

적절한 미분 가능성 조건 아래 모든 feature 귀인의 합은 경로 양 끝의 score 차이와 같다.

$$
\sum_i\operatorname{IG}_i(x;x')=f(x)-f(x').
$$

이는 baseline 대비 차이의 회계식이다. 각 feature 귀인이 현실 세계의 독립적 원인이라는 뜻은 아니다.

## 3. 수치 근사

실제 코드는 적분을 $m$개 점의 평균으로 근사한다.

$$
\widehat{\operatorname{IG}}_i
=
(x_i-x_i')\frac1m
\sum_{k=1}^{m}
\frac{\partial f}{\partial x_i}
\left(x'+\frac{k}{m}(x-x')\right).
$$

$m$을 늘려 completeness error가 충분히 작아지는지 확인한다. step 수를 결과를 좋게 보이도록 test 데이터에서만 선택하지 않는다.

## 4. baseline은 무정보와 동의어가 아니다

검은 이미지, zero embedding, padding token과 평균 activation은 서로 다른 counterfactual을 만든다. 자연어에서 embedding을 0으로 두는 상태가 실제 token 입력과 대응하지 않을 수 있다. 여러 정당한 baseline을 sensitivity analysis로 비교할 수 있지만 사후적으로 유리한 것만 보고하면 안 된다.

## 5. CPU 실습

<!-- I07_EXAMPLE: i07_03_integrated_gradients -->

같은 입력에 zero baseline과 one baseline을 사용한다. 두 경우 모두 completeness error는 작지만 feature별 귀인은 다르다.

## 흔한 오해

### 오해 1. completeness가 faithfulness를 증명한다

합계 보존은 정의한 baseline과 경로에 대한 수학적 성질이다. feature 의미, 현실적인 counterfactual과 모델의 인과 구조를 자동 검증하지 않는다.

### 오해 2. baseline은 구현 세부사항이다

귀인이 어떤 차이를 설명하는지 결정하므로 연구 질문의 일부다.

## 연습문제

### 1. 일차 함수

$f(x)=3x$, baseline $0$, 입력 $2$의 IG를 구하라.

<details>
<summary>해설 보기</summary>

gradient는 경로 전체에서 3이다. 변위는 2이므로 IG는 $2\times3=6$이고 $f(2)-f(0)=6$과 같다.

</details>

### 2. 제곱 함수

$f(x)=x^2$, baseline $0$, 입력 $2$의 IG를 적분으로 계산하라.

<details>
<summary>해설 보기</summary>

$\gamma(\alpha)=2\alpha$, gradient는 $2\gamma=4\alpha$이다. $2\int_0^1 4\alpha\,d\alpha=4$이며 score 차이도 4이다.

</details>

### 3. baseline 변경

앞 문제에서 baseline을 1로 바꾸면 IG는 얼마인가?

<details>
<summary>해설 보기</summary>

completeness에 따라 $f(2)-f(1)=4-1=3$이다. 직접 적분해도 같은 값이 나온다.

</details>

### 4. 수치 검사

IG 구현에서 가장 먼저 확인할 scalar 오차는 무엇인가?

<details>
<summary>해설 보기</summary>

$|\sum_i\widehat{\operatorname{IG}}_i-[f(x)-f(x')]|$인 completeness error를 확인한다. step을 늘렸을 때 감소하는지도 본다.

</details>

### 5. 자연어 baseline

zero embedding이 항상 좋은 baseline이 아닌 이유를 설명하라.

<details>
<summary>해설 보기</summary>

zero vector가 tokenizer가 만들 수 있는 실제 token embedding이 아닐 수 있다. 경로 중간점도 학습 분포 밖 상태일 수 있어 해석이 baseline 선택에 의존한다.

</details>

### 6. 주장 비판

“IG 합이 logit 차이와 같으므로 각 token의 인과 효과를 얻었다”가 왜 과한가?

<details>
<summary>해설 보기</summary>

completeness는 선택한 연속 경로의 gradient 회계식이다. token을 실제로 바꾸는 개입, 상호작용과 입력 타당성을 검증하지 않았으므로 인과 효과라고 부를 수 없다.

</details>

## 근거와 갱신 경계

정의, sensitivity·implementation invariance 공리와 completeness는 [Sundararajan, Taly and Yan (2017)](https://proceedings.mlr.press/v70/sundararajan17a.html)을 기준으로 한다. 이후 변형은 baseline·경로와 보장 조건이 달라질 수 있으므로 같은 이름으로 합치지 않는다.

## 단원 요약

- IG는 baseline에서 입력까지 gradient를 적분하고 feature 변위를 곱한다.
- 귀인 합은 baseline 대비 score 차이와 일치한다.
- baseline과 경로는 해석 질문의 일부다.
- completeness는 인과적 faithfulness의 충분조건이 아니다.

## 통과 기준

- 일변수 함수의 IG를 손으로 계산할 수 있는가?
- completeness error를 구현 검산에 사용할 수 있는가?
- baseline 선택을 분석 계약에 포함할 수 있는가?

## 다음 단원

- [I07-04 perturbation 기반 귀인](I07-04-perturbation-attribution.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] IG 정의와 completeness를 구분했다.
- [x] baseline·경로·수치오차를 포함했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
