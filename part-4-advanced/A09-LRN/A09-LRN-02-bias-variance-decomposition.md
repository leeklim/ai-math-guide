---
id: "A09-LRN-02"
title: "bias–variance decomposition"
part: 4
stage: "A09-LRN"
status: "완료"
prerequisites: ["A09-LRN-01", "M04-07"]
estimated_time: "90~120분"
---

# A09-LRN-02. bias–variance decomposition

## 이 단원이 필요한 이유

training set을 바꾸었을 때 predictor가 얼마나 흔들리는지와 평균 predictor가 target에서 얼마나 벗어나는지는 다른 오차 원인이다. squared-loss bias–variance decomposition은 이 둘과 irreducible noise를 분리한다.

## 학습 목표

- pointwise squared prediction error를 bias·variance·noise로 분해할 수 있다.
- estimator bias와 model misspecification을 구분할 수 있다.
- decomposition의 loss·sampling 가정을 설명할 수 있다.
- seed variance와 data-sampling variance를 분리할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-LRN-01 hypothesis class와 risk](A09-LRN-01-hypothesis-class-risk.md), [M04-07 추정의 bias와 variance](../../part-1-foundations/M04/M04-07-estimation-bias-variance.md)
- 확인 질문: estimator의 expectation은 무엇에 대한 반복을 뜻하는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\hat f_D(x)$ | `f hat trained on D evaluated at x` | dataset $D$로 학습한 predictor | scalar |
| $\bar f(x)$ | `f bar of x` | dataset 평균 predictor | scalar |
| $\operatorname{Bias}(x)$ | `the bias at x` | $\bar f(x)-f^*(x)$ | scalar |
| $\operatorname{Var}(x)$ | `the variance at x` | predictor의 dataset 변동 | nonnegative scalar |

## 핵심 개념

$Y=f^*(X)+\varepsilon$, $E[\varepsilon\mid X]=0$, $\operatorname{Var}(\varepsilon\mid X=x)=\sigma^2(x)$에서

$$
E_{D,Y\mid x}[(\hat f_D(x)-Y)^2]
=\operatorname{Bias}(x)^2+\operatorname{Var}(x)+\sigma^2(x).
$$

bias와 variance는 training dataset sampling에 대한 양이다. 같은 data에서 initialization만 바꾸는 실험은 algorithmic seed variance를 재지만 전체 sampling variance는 아니다.

classification 0–1 loss나 cross entropy에는 같은 단순한 additive decomposition이 그대로 적용되지 않는다. decomposition을 사용할 때 loss와 expectation source를 적는다.

## 작은 예제

$\bar f(x)-f^*(x)=1$, predictor variance가 4, noise variance가 2이면 expected squared error는 $1+4+2=7$이다.

## 흔한 오해

- regularization이 언제나 bias를 늘리고 variance를 줄인다는 설명은 모든 regime의 theorem이 아니다.
- seed variance가 작다고 dataset shift에 안정적인 것은 아니다.

## 연습문제

### 1. 합산
bias가 $-2$, variance가 3, noise variance가 1이면 expected squared error는 얼마인가?
<details><summary>해설 보기</summary>

$(-2)^2+3+1=8$이다.
</details>

### 2. noise
irreducible noise가 learner를 바꾸어도 남는 이유는 무엇인가?
<details><summary>해설 보기</summary>

같은 $X=x$에서도 $Y$가 조건부로 변하는 data-generating randomness이기 때문이다.
</details>

### 3. 반복 단위
data split을 고정하고 probe initialization만 20번 바꾸면 어떤 variance를 주로 측정하는가?
<details><summary>해설 보기</summary>

고정 data에서 optimizer·initialization에 따른 algorithmic variance를 측정한다.
</details>

### 4. 적용 범위
accuracy에 squared-loss decomposition 숫자를 그대로 붙이면 안 되는 이유는 무엇인가?
<details><summary>해설 보기</summary>

0–1 loss는 quadratic expansion의 교차항 소거 구조를 그대로 갖지 않기 때문이다.
</details>

## 근거와 갱신 경계

squared-loss bias–variance decomposition은 regression의 표준 항등식이다. modern overparameterized regime의 double descent는 이 항등식만으로 설명하지 않는다.

## 단원 요약

- squared error는 bias squared, variance와 noise로 분해된다.
- expectation이 반복하는 data·seed source를 명시한다.
- seed stability와 sampling stability는 다르다.
- 다른 loss에는 같은 식을 자동 적용하지 않는다.

## 통과 기준

- 주어진 bias·variance·noise에서 error를 계산할 수 있는가?
- probe 반복 설계가 어떤 variance를 측정하는지 말할 수 있는가?

## 다음 단원

- [A09-LRN-03 generalization gap](A09-LRN-03-generalization-gap.md)

## 집필자 점검표

- [x] decomposition의 loss와 반복 단위를 명시했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
