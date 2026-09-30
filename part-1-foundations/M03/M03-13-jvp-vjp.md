---
id: "M03-13"
title: "JVP와 VJP"
part: 1
stage: "M03"
status: "완료"
prerequisites:
  - "M03-07"
  - "M03-11"
  - "M03-12"
estimated_time: "120~145분"
---

# M03-13. JVP와 VJP

## 이 단원이 필요한 이유

입력 dimension과 출력 dimension이 큰 함수에서는 Jacobian 전체를 저장하기 어렵다. 많은 계산은 Jacobian 자체보다 Jacobian과 vector의 곱만 필요로 한다. 입력 방향의 변화가 출력으로 어떻게 전달되는지 묻는 계산이 JVP이고, 출력의 scalar 측정이 입력 쪽으로 어떻게 당겨지는지 묻는 계산이 VJP다.

forward-mode 자동미분은 JVP를 계산 그래프의 진행 방향으로 전달한다. reverse-mode 자동미분과 역전파는 VJP를 반대 방향으로 전달한다. 두 연산의 타입과 shape을 구분하면 자동미분 API와 gradient 계산을 같은 연쇄법칙으로 읽을 수 있다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- JVP와 VJP의 수식, 입력 타입과 출력 shape을 설명할 수 있다.
- 주어진 Jacobian에서 JVP와 VJP를 계산할 수 있다.
- adjoint identity로 두 계산의 일관성을 확인할 수 있다.
- 합성함수에서 JVP의 forward 순서와 VJP의 reverse 순서를 추적할 수 있다.
- scalar 출력 gradient를 VJP로 계산할 수 있다.
- 입력·출력 dimension에 따라 forward mode와 reverse mode의 사용 조건을 비교할 수 있다.
- JVP·VJP 결과가 나타내는 국소 주장 범위를 제한할 수 있다.

## 선수지식 확인

- 선수 단원: [M03-07 쌍대공간과 covector](M03-07-dual-spaces-covectors.md)
- 선수 단원: [M03-11 Jacobian](M03-11-jacobian.md)
- 선수 단원: [M03-12 Hessian](M03-12-hessian.md)
- 확인 질문: Jacobian의 출력 행·입력 열 convention과 shape을 설명할 수 있는가?
- 확인 질문: covector가 vector에 작용해 scalar를 만든다는 뜻을 설명할 수 있는가?
- 확인 질문: Hessian-vector product를 계산할 수 있는가?

Jacobian과 covector가 불분명하면 선수 단원을 먼저 복습한다.

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape |
|---|---|---|---|
| $\mathbf J_f(\mathbf x)$ | `the Jacobian of f at x` | $\mathbf x$에서의 total derivative 행렬 | $m\times n$ |
| $\mathbf v$ | `v` | 입력공간의 tangent 방향 | $n\times1$ |
| $\mathbf J_f(\mathbf x)\mathbf v$ | `the Jacobian of f at x times v` | Jacobian-vector product | $m\times1$ |
| $\mathbf u$ | `u` | 출력공간에서 scalar 측정을 정하는 covector의 열 표현 | $m\times1$ |
| $\mathbf J_f(\mathbf x)^\top\mathbf u$ | `the Jacobian of f at x transpose times u` | vector-Jacobian product의 열 표현 | $n\times1$ |
| tangent | `tangent` | forward mode가 전달하는 일차 변화 | vector |
| cotangent | `cotangent` | reverse mode가 전달하는 covector | 열 좌표로 저장 가능 |

일부 프레임워크는 VJP를 행 covector $\mathbf u^\top\mathbf J_f$로 쓴다. 이 교재는 열벡터 표기에 맞춰 그 전치인 $\mathbf J_f^\top\mathbf u$를 사용한다.

## 핵심 개념 1. JVP는 입력 방향을 출력 방향으로 보낸다

\[
f:\mathbb R^n\to\mathbb R^m
\]

의 Jacobian이

\[
\mathbf J_f(\mathbf x)\in\mathbb R^{m\times n}
\]

일 때 입력 방향 $\mathbf v\in\mathbb R^n$에 대한 JVP는

\[
\operatorname{JVP}_f(\mathbf x;\mathbf v)
=
\mathbf J_f(\mathbf x)\mathbf v
\in\mathbb R^m
\]

이다.

곡선

\[
\mathbf x(t)=\mathbf x+t\mathbf v
\]

를 함수에 넣으면

\[
\left.
\frac{d}{dt}
f(\mathbf x+t\mathbf v)
\right|_{t=0}
=
\mathbf J_f(\mathbf x)\mathbf v
\]

이다. JVP는 입력 tangent $\mathbf v$를 출력 tangent로 밀어 보낸다.

## 핵심 개념 2. VJP는 출력 covector를 입력 쪽으로 당긴다

출력 변화 $\Delta\mathbf y\in\mathbb R^m$를 scalar로 측정하는 covector를

\[
\mathbf u^\top\Delta\mathbf y
\]

로 쓰자. 국소적으로

\[
\Delta\mathbf y
\approx
\mathbf J_f(\mathbf x)\Delta\mathbf x
\]

이므로

\[
\mathbf u^\top\Delta\mathbf y
\approx
\mathbf u^\top
\mathbf J_f(\mathbf x)
\Delta\mathbf x
\]

이다. 입력 변화에 작용하는 covector의 열 좌표는

\[
\operatorname{VJP}_f(\mathbf x;\mathbf u)
=
\mathbf J_f(\mathbf x)^\top\mathbf u
\in\mathbb R^n
\]

이다.

VJP는 출력공간의 covector를 입력공간의 covector로 pullback한다. Euclidean 좌표에서 covector 계수를 열로 저장하므로 vector처럼 보이지만 변환 역할은 covector다.

## 핵심 개념 3. adjoint identity는 두 곱을 같은 scalar로 연결한다

JVP와 VJP는

\[
\mathbf u^\top
\left(
\mathbf J_f\mathbf v
\right)
=
\left(
\mathbf J_f^\top\mathbf u
\right)^\top
\mathbf v
\]

를 만족한다.

왼쪽은 입력 방향을 출력으로 보낸 뒤 $\mathbf u$로 측정한다. 오른쪽은 $\mathbf u$를 입력 쪽으로 당긴 뒤 $\mathbf v$에 적용한다. 두 경로는 같은 scalar를 만든다.

이 식은 손계산이나 구현 결과를 점검하는 데 사용할 수 있다. 두 값이 다르면 transpose, 축 또는 행렬곱 순서를 잘못 잡았을 가능성이 있다.

## 핵심 개념 4. 합성함수의 JVP는 forward 순서로 흐른다

\[
f:\mathbb R^n\to\mathbb R^m,
\qquad
g:\mathbb R^m\to\mathbb R^p
\]

일 때

\[
\mathbf J_{g\circ f}(\mathbf x)
=
\mathbf J_g(f(\mathbf x))
\mathbf J_f(\mathbf x)
\]

이다. 입력 tangent $\mathbf v$의 JVP는

\[
\mathbf v
\longmapsto
\mathbf J_f(\mathbf x)\mathbf v
\longmapsto
\mathbf J_g(f(\mathbf x))
\left(
\mathbf J_f(\mathbf x)\mathbf v
\right)
\]

순서로 계산한다.

각 연산은 현재 값과 tangent를 함께 다음 node로 보낸다. 이 구조가 forward-mode 자동미분이다.

## 핵심 개념 5. 합성함수의 VJP는 reverse 순서로 흐른다

출력 cotangent $\mathbf u\in\mathbb R^p$에서 시작하면

\[
\mathbf J_{g\circ f}(\mathbf x)^\top\mathbf u
=
\mathbf J_f(\mathbf x)^\top
\mathbf J_g(f(\mathbf x))^\top
\mathbf u
\]

이다. 계산 순서는

\[
\mathbf u
\longmapsto
\mathbf J_g^\top\mathbf u
\longmapsto
\mathbf J_f^\top
\left(
\mathbf J_g^\top\mathbf u
\right)
\]

이다.

forward pass에서 $f$ 다음 $g$를 적용했다면 reverse pass에서는 $g$의 local VJP 다음 $f$의 local VJP를 적용한다.

## 핵심 개념 6. scalar 출력의 gradient는 VJP 하나로 얻는다

$f:\mathbb R^n\to\mathbb R$이면 Jacobian shape은 $1\times n$이다. 출력공간의 seed를 scalar 1로 두면

\[
\mathbf J_f(\mathbf x)^\top
\begin{bmatrix}1\end{bmatrix}
=
\nabla f(\mathbf x)
\]

이다.

파라미터가 많고 loss가 하나인 학습에서는 VJP 한 번이 모든 파라미터에 대한 gradient를 만든다. reverse mode가 신경망 학습에 맞는 이유다.

출력이 여러 개이고 많은 입력 방향에 대한 변화가 필요하면 JVP를 여러 번 계산할 수 있다. 필요한 입력 방향 수와 출력 covector 수가 어느 쪽이 적은지에 따라 계산 방향을 고른다.

## 핵심 개념 7. 전체 Jacobian 없이 곱을 계산할 수 있다

Jacobian 전체를 얻으려면 표준기저 방향의 JVP를 $n$번 계산하거나 출력 표준기저의 VJP를 $m$번 계산할 수 있다.

\[
\mathbf J_f\mathbf e_j
\]

는 Jacobian의 $j$번째 열이고

\[
\mathbf J_f^\top\mathbf e_i
\]

는 Jacobian의 $i$번째 행을 열로 세운 값이다.

한 방향이나 한 scalar loss의 gradient만 필요하면 전체 행렬을 구성할 필요가 없다. 자동미분 시스템은 계산 그래프의 local derivative를 사용해 원하는 곱을 계산한다.

## 예제 1. 같은 Jacobian에서 JVP와 VJP 계산하기

### 문제

\[
\mathbf J=
\begin{bmatrix}
2&1\\
2&1\\
1&-1
\end{bmatrix},
\qquad
\mathbf v=
\begin{bmatrix}
3\\-1
\end{bmatrix},
\qquad
\mathbf u=
\begin{bmatrix}
1\\-2\\3
\end{bmatrix}
\]

일 때 JVP, VJP와 adjoint identity의 두 scalar를 계산하라.

### 풀이

JVP는

\[
\mathbf J\mathbf v
=
\begin{bmatrix}
2&1\\
2&1\\
1&-1
\end{bmatrix}
\begin{bmatrix}
3\\-1
\end{bmatrix}
=
\begin{bmatrix}
5\\5\\4
\end{bmatrix}
\]

이다.

VJP는

\[
\mathbf J^\top\mathbf u
=
\begin{bmatrix}
2&2&1\\
1&1&-1
\end{bmatrix}
\begin{bmatrix}
1\\-2\\3
\end{bmatrix}
=
\begin{bmatrix}
1\\-4
\end{bmatrix}
\]

이다.

출력 쪽에서 측정하면

\[
\mathbf u^\top(\mathbf J\mathbf v)
=
1\cdot5+(-2)\cdot5+3\cdot4
=
7
\]

이다. 입력 쪽에서 측정하면

\[
(\mathbf J^\top\mathbf u)^\top\mathbf v
=
\begin{bmatrix}
1&-4
\end{bmatrix}
\begin{bmatrix}
3\\-1
\end{bmatrix}
=
7
\]

이다.

### 결과의 의미

JVP와 VJP는 서로 다른 공간의 vector를 내놓지만 같은 bilinear pairing을 계산한다.

## 예제 2. 합성함수에서 두 전달 방향 비교하기

어떤 점에서 두 함수의 Jacobian이

\[
\mathbf J_f=
\begin{bmatrix}
1&2\\
0&3
\end{bmatrix},
\qquad
\mathbf J_g=
\begin{bmatrix}
4&-1
\end{bmatrix}
\]

라고 하자. 입력 tangent

\[
\mathbf v=
\begin{bmatrix}
2\\-1
\end{bmatrix}
\]

를 forward로 보내면

\[
\mathbf J_f\mathbf v
=
\begin{bmatrix}
0\\-3
\end{bmatrix}
\]

이고

\[
\mathbf J_g
\begin{bmatrix}
0\\-3
\end{bmatrix}
=
3
\]

이다.

reverse에서는 출력 seed 1에서 시작한다.

\[
\mathbf J_g^\top
\begin{bmatrix}1\end{bmatrix}
=
\begin{bmatrix}
4\\-1
\end{bmatrix}
\]

\[
\mathbf J_f^\top
\begin{bmatrix}
4\\-1
\end{bmatrix}
=
\begin{bmatrix}
4\\5
\end{bmatrix}
\]

이다. 입력 gradient와 방향의 내적은

\[
\begin{bmatrix}
4&5
\end{bmatrix}
\begin{bmatrix}
2\\-1
\end{bmatrix}
=
3
\]

으로 forward directional derivative와 같다.

## 예제 3. 선형 readout의 VJP

activation $\mathbf h\in\mathbb R^d$에서

\[
s(\mathbf h)=\mathbf w^\top\mathbf h+b
\]

를 계산하면

\[
\mathbf J_s(\mathbf h)=\mathbf w^\top
\]

이다. 출력 seed $u=1$의 VJP는

\[
\mathbf J_s(\mathbf h)^\top u
=
\mathbf w
\]

이다. 출력 score에 대한 activation gradient가 $\mathbf w$가 되는 이유다.

$\mathbf w$는 이 점에서 score differential의 좌표다. gradient 관찰만으로 모델이 이 방향을 인간이 붙인 개념으로 사용한다고 결론 내릴 수는 없다.

## 예제 4. Hessian-vector product를 JVP로 보기

scalar 함수 $f$의 gradient map을

\[
g(\mathbf x)=\nabla f(\mathbf x)
\]

라고 하면

\[
\mathbf J_g(\mathbf x)=\mathbf H_f(\mathbf x)
\]

이다. 따라서

\[
\operatorname{JVP}_g(\mathbf x;\mathbf v)
=
\mathbf H_f(\mathbf x)\mathbf v
\]

이다. HVP는 gradient 함수에 대한 JVP로 계산할 수 있다.

## 흔한 오해

### 오해 1. JVP와 VJP는 transpose 표기만 다른 같은 출력이다

JVP는 입력 tangent를 출력 tangent로 보내고 shape이 $m$이다. VJP는 출력 cotangent를 입력 cotangent로 보내고 shape이 $n$이다.

### 오해 2. VJP의 입력 $\mathbf u$는 출력 perturbation이다

$\mathbf u$는 출력 변화를 scalar로 측정하는 covector의 좌표다. reverse mode는 이 측정을 입력 쪽으로 pullback한다.

### 오해 3. gradient를 얻으려면 Jacobian 전체를 먼저 만들어야 한다

scalar 출력에서는 seed 1의 VJP 한 번으로 입력 gradient를 계산할 수 있다.

### 오해 4. forward mode는 forward pass이고 reverse mode는 모델을 거꾸로 실행한다

두 mode는 derivative 정보를 전달하는 방향을 가리킨다. reverse mode도 원래 forward 값과 local derivative를 사용하며 원래 함수를 역함수로 계산하지 않는다.

## 연습문제

### 1. shape 읽기

$f:\mathbb R^5\to\mathbb R^3$일 때 Jacobian, JVP 입력·출력과 VJP 입력·출력의 shape을 적어라.

<details>
<summary>해설 보기</summary>

\[
\mathbf J_f\in\mathbb R^{3\times5}
\]

이다. JVP는 $\mathbf v\in\mathbb R^5$를 받아 $\mathbf J_f\mathbf v\in\mathbb R^3$을 만든다. VJP는 $\mathbf u\in\mathbb R^3$을 받아 $\mathbf J_f^\top\mathbf u\in\mathbb R^5$를 만든다.

</details>

### 2. JVP 계산

\[
\mathbf J=
\begin{bmatrix}
1&2\\
-1&3
\end{bmatrix},
\qquad
\mathbf v=
\begin{bmatrix}
2\\-1
\end{bmatrix}
\]

일 때 JVP를 구하라.

<details>
<summary>해설 보기</summary>

\[
\mathbf J\mathbf v
=
\begin{bmatrix}
1&2\\
-1&3
\end{bmatrix}
\begin{bmatrix}
2\\-1
\end{bmatrix}
=
\begin{bmatrix}
0\\-5
\end{bmatrix}
\]

이다.

</details>

### 3. VJP 계산

연습문제 2의 $\mathbf J$와

\[
\mathbf u=
\begin{bmatrix}
4\\1
\end{bmatrix}
\]

에 대해 VJP를 구하라.

<details>
<summary>해설 보기</summary>

\[
\mathbf J^\top\mathbf u
=
\begin{bmatrix}
1&-1\\
2&3
\end{bmatrix}
\begin{bmatrix}
4\\1
\end{bmatrix}
=
\begin{bmatrix}
3\\11
\end{bmatrix}
\]

이다.

</details>

### 4. adjoint identity

연습문제 2와 3의 값으로 $\mathbf u^\top(\mathbf J\mathbf v)$와 $(\mathbf J^\top\mathbf u)^\top\mathbf v$를 비교하라.

<details>
<summary>해설 보기</summary>

\[
\mathbf u^\top(\mathbf J\mathbf v)
=
\begin{bmatrix}
4&1
\end{bmatrix}
\begin{bmatrix}
0\\-5
\end{bmatrix}
=
-5
\]

이다. 반대쪽은

\[
\begin{bmatrix}
3&11
\end{bmatrix}
\begin{bmatrix}
2\\-1
\end{bmatrix}
=
6-11
=
-5
\]

이다. 두 값이 같다.

</details>

### 5. scalar gradient

$f:\mathbb R^4\to\mathbb R$의 Jacobian 행이

\[
\mathbf J_f=
\begin{bmatrix}
2&-1&0&3
\end{bmatrix}
\]

일 때 seed 1의 VJP를 구하라.

<details>
<summary>해설 보기</summary>

\[
\mathbf J_f^\top
\begin{bmatrix}1\end{bmatrix}
=
\begin{bmatrix}
2\\-1\\0\\3
\end{bmatrix}
\]

이다. Euclidean 좌표에서 이 열이 $\nabla f$다.

</details>

### 6. 합성 전달 순서

$h=g\circ f$일 때 JVP와 VJP가 local Jacobian을 적용하는 순서를 각각 적어라.

<details>
<summary>해설 보기</summary>

JVP는

\[
\mathbf v
\longmapsto
\mathbf J_f\mathbf v
\longmapsto
\mathbf J_g(\mathbf J_f\mathbf v)
\]

순서다. VJP는 출력 cotangent $\mathbf u$에서 시작해

\[
\mathbf u
\longmapsto
\mathbf J_g^\top\mathbf u
\longmapsto
\mathbf J_f^\top(\mathbf J_g^\top\mathbf u)
\]

순서다.

</details>

### 7. 모델 주장 비판

“loss에 대한 한 activation의 VJP가 0이므로 그 activation은 모델 계산에 필요하지 않다”는 문장을 비판하라.

<details>
<summary>해설 보기</summary>

0인 VJP는 지정한 입력, 파라미터와 loss에서 그 activation의 작은 변화가 loss에 미치는 일차 효과가 0이라는 뜻이다. saturation, 상쇄나 국소 평탄성 때문에 0이 될 수 있으며 다른 입력·출력이나 유한한 개입에서는 효과가 나타날 수 있다. 필요성 주장은 activation을 제거하거나 바꾸는 개입과 대조군으로 검증해야 한다.

</details>

## 단원 요약

- JVP는 입력 tangent를 출력 tangent로 보내고 VJP는 출력 cotangent를 입력 cotangent로 pullback한다.
- adjoint identity는 JVP와 VJP가 같은 scalar pairing을 계산함을 보인다.
- 합성함수에서 JVP는 forward 순서, VJP는 reverse 순서로 local Jacobian 곱을 전달한다.
- scalar 출력 gradient는 seed 1의 VJP로 얻는다.
- 한 방향이나 한 출력 측정만 필요하면 전체 Jacobian을 만들지 않고 곱을 계산할 수 있다.
- JVP와 VJP는 지정한 점의 국소 일차 정보를 나타낸다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- JVP와 VJP의 입력·출력 타입과 shape을 정할 수 있는가?
- 작은 행렬에서 두 곱을 계산할 수 있는가?
- adjoint identity를 계산으로 확인할 수 있는가?
- 합성함수에서 두 전달 방향을 추적할 수 있는가?
- scalar gradient를 VJP로 만들 수 있는가?
- 필요한 방향 수에 따라 forward·reverse mode를 비교할 수 있는가?
- 0인 VJP가 허용하는 주장 범위를 제한할 수 있는가?

## 다음 단원

- [M03-14 자동미분과 역전파](M03-14-automatic-differentiation-backpropagation.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] JVP와 VJP의 타입·shape을 구분했다.
- [x] adjoint identity를 계산했다.
- [x] 합성함수의 forward·reverse 순서를 설명했다.
- [x] scalar gradient와 HVP를 연결했다.
- [x] 전체 Jacobian을 만들지 않는 계산 목적을 밝혔다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 내부 링크와 수식 구분자를 확인했다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
