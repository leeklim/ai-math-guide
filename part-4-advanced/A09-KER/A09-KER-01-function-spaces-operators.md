---
id: "A09-KER-01"
title: "함수공간과 operator"
part: 4
stage: "A09-KER"
status: "완료"
prerequisites: ["M02-05", "M03-01", "M03-02"]
estimated_time: "90~120분"
---

# A09-KER-01. 함수공간과 operator

## 이 단원이 필요한 이유

신경망 학습은 parameter vector를 움직이지만 연구자는 그 결과를 input과 output 사이의 함수 변화로 해석한다. 함수도 더하고 scalar를 곱할 수 있으므로 vector space를 이루며, 함수에 작용하는 map은 operator로 다룰 수 있다. 이 관점은 kernel method와 neural tangent kernel의 출발점이다.

## 학습 목표

- 함수 집합이 vector space가 되는 조건을 확인할 수 있다.
- linear operator와 nonlinear operator를 구분할 수 있다.
- evaluation operator와 integral operator의 입력·출력을 쓸 수 있다.
- parameter-space 변화와 function-space 변화를 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [M02-05 행렬을 선형변환으로 보기](../../part-1-foundations/M02/M02-05-matrix-as-linear-transformation.md), [M03-01 추상 벡터공간](../../part-1-foundations/M03/M03-01-abstract-vector-spaces.md), [M03-02 선형사상과 행렬 표현](../../part-1-foundations/M03/M03-02-linear-maps-matrix-representation.md)
- 확인 질문: 두 vector를 더하고 scalar를 곱하는 규칙만 알 때 좌표를 고르지 않고 linearity를 어떻게 검사하는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\mathcal F$ | `the function space F` | 같은 domain과 codomain을 가진 함수공간 | set of functions |
| $T:\mathcal F\to\mathcal G$ | `T maps F to G` | 함수를 다른 함수나 값으로 보내는 operator | map between spaces |
| $E_x(f)=f(x)$ | `the evaluation operator at x applied to f` | 지정 input에서 함수값을 꺼내는 operator | scalar or vector |
| $\lVert f\rVert_{\mathcal F}$ | `the norm of f in F` | 함수의 크기 | nonnegative scalar |

## 핵심 개념

같은 set $\mathcal X$에서 실수로 가는 함수들의 집합을 생각한다. $f,g\in\mathcal F$와 scalar $a,b$에 대해

$$
(af+bg)(x)=af(x)+bg(x)
$$

가 다시 $\mathcal F$에 속하면 함수들을 vector처럼 계산할 수 있다. polynomial degree를 $d$ 이하로 제한한 공간은 finite-dimensional이지만 continuous function 전체는 보통 infinite-dimensional이다.

operator $T$가

$$
T(af+bg)=aT(f)+bT(g)
$$

를 만족하면 linear operator이다. differentiation과 integration은 적절한 함수공간에서 linear하다. $f\mapsto f^2$은 일반적으로 linear하지 않다. 행렬은 좌표를 고른 finite-dimensional linear operator의 표현이다.

모델 $f_\theta$에서는 서로 다른 $\theta$가 같은 함수를 나타낼 수 있다. parameter distance가 커도 $f_\theta(x)$가 data distribution에서 거의 같을 수 있으므로 두 공간의 거리를 따로 기록해야 한다.

## 작은 예제

$\mathcal F=\operatorname{span}\{1,x\}$에서 $f(x)=a+bx$이다. evaluation operator $E_2$는 $E_2(f)=a+2b$를 반환한다. basis $(1,x)$를 쓰면 $E_2$는 row vector $(1,2)$처럼 작용한다.

## 흔한 오해

- 함수공간의 한 원소는 input vector가 아니라 함수 하나이다.
- operator를 행렬로 쓰려면 basis와 좌표가 필요하다.

## 연습문제

### 1. closure
$f(x)=1+x$와 $g(x)=x^2$가 degree 2 이하 polynomial 공간에 있을 때 $3f-2g$도 같은 공간에 있는지 확인하라.
<details><summary>해설 보기</summary>

$3f(x)-2g(x)=3+3x-2x^2$이므로 degree가 2 이하이고 같은 공간에 속한다.
</details>

### 2. linearity
$T(f)=f(0)+1$은 linear operator인가?
<details><summary>해설 보기</summary>

$T(0)=1$이므로 linear map이 만족해야 할 $T(0)=0$을 어긴다. affine operator이다.
</details>

### 3. evaluation
$f(x)=2-3x$일 때 $E_{-1}(f)$를 구하라.
<details><summary>해설 보기</summary>

$f(-1)=2+3=5$이다.
</details>

### 4. 모델 해석
두 checkpoint의 parameter distance가 큰데 모든 evaluation prompt에서 output 차이가 작다. 어느 공간의 변화가 작다고 말할 수 있는가?
<details><summary>해설 보기</summary>

측정한 prompt distribution에서 function-space 변화가 작다고 말할 수 있다. 측정하지 않은 input 전체나 parameter-space의 가까움을 주장할 수는 없다.
</details>

## 근거와 갱신 경계

이 단원은 vector space와 linear operator의 정의를 함수에 적용한다. topology, operator norm의 완전한 이론과 unbounded operator의 domain 문제는 다루지 않는다.

## 단원 요약

- 함수도 pointwise 연산 아래 vector space를 이룰 수 있다.
- operator는 함수를 입력으로 받는 map이다.
- 행렬은 basis를 고른 linear operator의 좌표 표현이다.
- parameter-space와 function-space 거리는 서로 다른 질문에 답한다.

## 통과 기준

- 함수공간의 closure와 operator의 linearity를 검사할 수 있는가?
- parameter 변화와 함수 변화를 구분해 서술할 수 있는가?

## 다음 단원

- [A09-KER-02 positive definite kernel](A09-KER-02-positive-definite-kernel.md)

## 집필자 점검표

- [x] 함수공간·operator·좌표 표현을 구분했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
