---
id: "M03-04"
title: "불변량과 equivariance 입문"
part: 1
stage: "M03"
status: "완료"
prerequisites:
  - "M03-03"
  - "M02-03"
estimated_time: "115~140분"
---

# M03-04. 불변량과 equivariance 입문

## 이 단원이 필요한 이유

기저, 좌표 순서나 입력 위치를 바꾸면 어떤 수치는 달라지고 어떤 수치는 유지된다. 분석 결과를 비교하려면 먼저 허용할 변환을 정하고, 그 변환 아래 결과가 유지되는지 확인해야 한다. 변환을 밝히지 않은 채 “기저에 무관하다”거나 “대칭적이다”라고 쓰면 주장 범위를 판단할 수 없다.

모델의 출력이 입력 변환을 무시해야 하는 문제도 있고, 출력이 입력과 함께 변해야 하는 문제도 있다. 집합의 총합은 원소 순서를 무시해야 한다. 반면 각 원소에 붙인 예측은 원소 순서를 바꾸면 같은 순서로 이동해야 한다. 앞의 성질이 불변성(invariance), 뒤의 성질이 등변성(equivariance)이다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- 변환과 불변량을 변환 전후의 등식으로 정의할 수 있다.
- 불변성과 equivariance를 식과 작은 예제로 구분할 수 있다.
- 직교변환 아래 norm, 내적과 거리가 유지됨을 계산할 수 있다.
- 순열변환에 대한 합 연산의 불변성과 성분별 연산의 equivariance를 확인할 수 있다.
- 분석 방법이 어떤 변환 아래 같은 결론을 내는지 명시할 수 있다.
- 불변성이 정보 보존이나 모델 사용 증거를 뜻하지 않는 이유를 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [M03-03 기저변환과 좌표 의존성](M03-03-change-of-basis-coordinate-dependence.md)
- 선수 단원: [M02-03 내적, 길이와 각도](../M02/M02-03-inner-product-length-angle.md)
- 확인 질문: 수동적 좌표변경과 능동적 벡터변환을 구분할 수 있는가?
- 확인 질문: 직교행렬 $\mathbf Q$가 $\mathbf Q^\top\mathbf Q=\mathbf I$를 만족한다는 뜻을 설명할 수 있는가?

기저변환과 직교행렬이 불분명하면 선수 단원을 먼저 복습한다.

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | 범위 |
|---|---|---|---|
| $g$ | `g` | 입력에 적용하는 허용된 변환 | 회전, 반사, 순열 등 |
| $g\cdot\mathbf x$ | `g acting on x` | 변환 $g$를 적용한 입력 | 입력공간의 원소 |
| $I(\mathbf x)$ | `I of x` | 입력에서 계산한 불변량 후보 | scalar 또는 다른 요약 |
| $f$ | `f` | 입력을 출력으로 보내는 함수 | 모델이나 분석 함수 |
| $\rho(g)$ | `rho of g` | 출력공간에서 $g$에 대응하는 변환 | 출력 종류에 따라 다르다. |
| 불변성 | `invariance` | 입력을 변환해도 출력이 같은 성질 | $f(g\cdot\mathbf x)=f(\mathbf x)$ |
| equivariance | `equivariance` | 입력 변환에 맞춰 출력도 변하는 성질 | $f(g\cdot\mathbf x)=\rho(g)f(\mathbf x)$ |

이 단원에서는 변환들의 대수 구조를 깊게 다루지 않는다. 군(group)과 군 작용은 A09-SYM에서 정의한다.

## 핵심 개념 1. 불변량은 지정한 변환 아래 값이 유지된다

입력공간의 허용된 변환 $g$에 대해

\[
I(g\cdot\mathbf x)=I(\mathbf x)
\]

가 모든 허용 입력 $\mathbf x$에서 성립하면 $I$를 그 변환에 대한 불변량(invariant)이라고 한다.

불변량을 말하려면 두 항목을 함께 밝혀야 한다.

1. 어떤 대상을 변환하는가?
2. 어떤 변환을 허용하는가?

예를 들어 Euclidean norm은 직교변환에 대해 불변이다. 가역행렬 전체가 만드는 변환에 대해서는 불변이 아니다. $\mathbf x=(1,0)^\top$과

\[
\mathbf A=
\begin{bmatrix}
2&0\\
0&1
\end{bmatrix}
\]

를 사용하면 $\|\mathbf x\|_2=1$이지만 $\|\mathbf A\mathbf x\|_2=2$다.

## 핵심 개념 2. 직교변환은 내적 구조를 보존한다

$\mathbf Q\in\mathbb R^{d\times d}$가

\[
\mathbf Q^\top\mathbf Q=\mathbf I_d
\]

를 만족하면 $\mathbf Q$는 직교행렬이다. 두 벡터 $\mathbf x,\mathbf y\in\mathbb R^d$에 대해

\[
\langle\mathbf Q\mathbf x,\mathbf Q\mathbf y\rangle
=
(\mathbf Q\mathbf x)^\top(\mathbf Q\mathbf y)
=
\mathbf x^\top\mathbf Q^\top\mathbf Q\mathbf y
=
\mathbf x^\top\mathbf y
\]

이다. 따라서 norm도 유지된다.

\[
\|\mathbf Q\mathbf x\|_2^2
=
\langle\mathbf Q\mathbf x,\mathbf Q\mathbf x\rangle
=
\langle\mathbf x,\mathbf x\rangle
=
\|\mathbf x\|_2^2
\]

거리도 벡터 차이의 norm이므로

\[
\|\mathbf Q\mathbf x-\mathbf Q\mathbf y\|_2
=
\|\mathbf Q(\mathbf x-\mathbf y)\|_2
=
\|\mathbf x-\mathbf y\|_2
\]

이다. 각도는 내적과 norm으로 계산하므로 유지된다.

## 핵심 개념 3. 불변 함수는 입력 변환을 출력에서 지운다

함수 $f:X\to Y$가 변환 $g$에 대해 불변이라는 말은

\[
f(g\cdot\mathbf x)=f(\mathbf x)
\]

가 성립한다는 뜻이다. 변환된 입력과 원래 입력이 같은 출력을 만든다.

예를 들어 $\mathbf x\in\mathbb R^n$의 성분을 바꾸는 순열행렬을 $\mathbf P$라 하자. 성분의 합

\[
s(\mathbf x)=\sum_{i=1}^{n}x_i
\]

은

\[
s(\mathbf P\mathbf x)=s(\mathbf x)
\]

를 만족한다. 순열은 성분의 위치만 바꾸므로 합은 달라지지 않는다.

불변 함수는 변환으로 생긴 차이를 출력에서 구분하지 않는다. 이 성질은 필요한 정보를 버릴 수도 있다. 상수함수 $f(\mathbf x)=0$은 모든 입력 변환에 대해 불변이지만 입력에 관한 정보를 제공하지 않는다.

## 핵심 개념 4. equivariant 함수는 변환을 출력으로 운반한다

함수 $f:X\to Y$가 equivariant라는 말은

\[
f(g\cdot\mathbf x)
=
\rho(g)f(\mathbf x)
\]

가 성립한다는 뜻이다. 입력을 먼저 변환한 뒤 $f$를 적용한 결과와, $f$를 먼저 적용한 뒤 대응하는 출력변환 $\rho(g)$를 적용한 결과가 같다.

입력과 출력이 같은 종류이고 같은 변환을 쓰면

\[
f(g\cdot\mathbf x)=g\cdot f(\mathbf x)
\]

로 줄여 쓴다.

성분별 제곱함수

\[
f(\mathbf x)
=
\begin{bmatrix}
x_1^2\\
\vdots\\
x_n^2
\end{bmatrix}
\]

는 순열에 대해 equivariant다.

\[
f(\mathbf P\mathbf x)=\mathbf P f(\mathbf x)
\]

순서를 먼저 바꾸든 각 성분을 제곱한 뒤 순서를 바꾸든 같은 결과가 나온다.

## 핵심 개념 5. 불변성과 equivariance는 출력의 역할에 따라 고른다

입력 전체에 label 하나를 붙이는 함수는 순서나 회전을 무시해야 할 수 있다. 이 경우 불변성이 맞는 요구다. 각 입력 요소에 출력을 하나씩 붙이는 함수는 입력 요소가 이동할 때 해당 출력도 이동해야 한다. 이 경우 equivariance가 맞다.

다음 표는 두 조건의 차이를 정리한다.

| 질문 | 불변성 | equivariance |
|---|---|---|
| 변환 뒤 출력 | 그대로다. | 정해진 방식으로 변한다. |
| 대표 식 | $f(g\cdot\mathbf x)=f(\mathbf x)$ | $f(g\cdot\mathbf x)=\rho(g)f(\mathbf x)$ |
| 예 | 집합 원소의 합 | 원소별 예측 |
| 정보 효과 | 변환 방향 정보를 제거할 수 있다. | 변환 정보를 출력 위치에 보존할 수 있다. |

한 함수가 어떤 변환에 대해서는 불변이고 다른 변환에 대해서는 equivariant일 수 있다. 함수 이름만으로 성질을 판단하지 않고 입력·출력의 작용을 적어야 한다.

## 핵심 개념 6. 표현 비교는 허용 변환을 먼저 정한다

두 activation 행렬 $\mathbf H_1$과 $\mathbf H_2$가 있을 때 “같은 표현”이라는 문장은 기준이 부족하다. 다음 관계들은 서로 다른 허용 변환을 사용한다.

- 원소별 동일성: $\mathbf H_2=\mathbf H_1$
- 직교 정렬 뒤 동일성: $\mathbf H_2=\mathbf H_1\mathbf Q$
- 가역 선형 정렬 뒤 동일성: $\mathbf H_2=\mathbf H_1\mathbf A$

직교 정렬은 행 사이의 Euclidean 내적과 거리를 보존한다. 일반 가역 정렬은 선형독립과 차원은 보존하지만 Euclidean 거리와 각도를 바꿀 수 있다. 표현 유사도 지표를 해석할 때 그 지표가 어떤 변환에 불변인지 확인해야 한다.

## 예제 1. 회전 아래 norm과 내적 확인하기

### 문제

\[
\mathbf Q=
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}
3\\
4
\end{bmatrix},
\qquad
\mathbf y=
\begin{bmatrix}
1\\
-2
\end{bmatrix}
\]

라 하자. $\mathbf Q^\top\mathbf Q$, 두 norm과 변환 전후 내적을 계산하라.

### 풀이

\[
\mathbf Q^\top\mathbf Q
=
\begin{bmatrix}
0&1\\
-1&0
\end{bmatrix}
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}
=
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
\]

이므로 $\mathbf Q$는 직교행렬이다.

\[
\mathbf Q\mathbf x=
\begin{bmatrix}
-4\\
3
\end{bmatrix},
\qquad
\mathbf Q\mathbf y=
\begin{bmatrix}
2\\
1
\end{bmatrix}
\]

이다. norm은

\[
\|\mathbf x\|_2=5,
\qquad
\|\mathbf Q\mathbf x\|_2=\sqrt{(-4)^2+3^2}=5
\]

이고

\[
\|\mathbf y\|_2=\sqrt5,
\qquad
\|\mathbf Q\mathbf y\|_2=\sqrt5
\]

다. 내적은

\[
\mathbf x^\top\mathbf y
=
3\cdot1+4\cdot(-2)
=
-5
\]

\[
(\mathbf Q\mathbf x)^\top(\mathbf Q\mathbf y)
=
(-4)\cdot2+3\cdot1
=
-5
\]

다.

### 결과의 의미

$\mathbf Q$는 두 벡터를 90도 회전하지만 길이와 두 벡터 사이의 내적을 보존한다.

## 예제 2. 순열에 대한 불변성과 equivariance

### 문제

\[
\mathbf P=
\begin{bmatrix}
0&1\\
1&0
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}
2\\
-1
\end{bmatrix}
\]

라 하자. 합 $s(\mathbf x)=x_1+x_2$의 불변성과 성분별 제곱함수 $f$의 equivariance를 확인하라.

### 풀이

\[
\mathbf P\mathbf x
=
\begin{bmatrix}
-1\\
2
\end{bmatrix}
\]

이고

\[
s(\mathbf x)=2+(-1)=1,
\qquad
s(\mathbf P\mathbf x)=-1+2=1
\]

이다. 따라서 이 입력에서 합의 불변성을 확인했다.

\[
f(\mathbf x)
=
\begin{bmatrix}
4\\
1
\end{bmatrix}
\]

이고

\[
f(\mathbf P\mathbf x)
=
\begin{bmatrix}
1\\
4
\end{bmatrix}
=
\mathbf P
\begin{bmatrix}
4\\
1
\end{bmatrix}
=
\mathbf P f(\mathbf x)
\]

이다.

### 결과의 의미

합은 어느 성분이 첫째인지에 관한 정보를 없앤다. 성분별 제곱은 각 출력이 대응하는 입력 성분을 따라 이동하게 한다.

## 예제 3. 모델 분석에서 변환 범위 적기

두 모델의 같은 층에서 표본별 activation을 행으로 쌓아

\[
\mathbf H_1,\mathbf H_2\in\mathbb R^{N\times d}
\]

를 얻었다고 하자. $\mathbf H_2=\mathbf H_1\mathbf Q$이고 $\mathbf Q^\top\mathbf Q=\mathbf I_d$이면 표본 사이 Gram 행렬은 같다.

\[
\mathbf H_2\mathbf H_2^\top
=
\mathbf H_1\mathbf Q\mathbf Q^\top\mathbf H_1^\top
=
\mathbf H_1\mathbf H_1^\top
\]

따라서 표본 사이 내적과 Euclidean 거리를 사용하는 분석은 같은 결과를 낸다. 개별 feature 좌표는 달라질 수 있다. 이 계산만으로 두 모델이 같은 내부 알고리즘을 사용한다고 결론 내릴 수는 없다.

## 흔한 오해

### 오해 1. 불변량은 모든 변환에서 유지된다

불변량은 지정한 변환 집합에 상대적인 개념이다. Euclidean norm은 직교변환에서 유지되지만 일반 가역변환에서는 달라질 수 있다.

### 오해 2. 불변성과 equivariance는 같은 말이다

불변 함수는 변환 뒤에도 같은 출력을 낸다. equivariant 함수는 입력 변환에 대응해 출력도 정해진 방식으로 바꾼다.

### 오해 3. 불변성이 클수록 표현이 좋다

불변성은 변환 관련 정보를 제거한다. 과제에 필요한 방향이나 위치까지 제거하면 예측에 불리하다. 어떤 변화를 무시해야 하는지 과제가 정한다.

### 오해 4. 불변 지표가 같으면 두 모델의 계산도 같다

불변 지표는 허용 변환으로 생긴 차이를 구분하지 않는다. 같은 지표값은 해당 지표가 보는 구조가 같다는 증거이며, 내부 계산 경로나 기능적 사용까지 보장하지 않는다.

## 연습문제

### 1. 정의 읽기

\[
f(g\cdot\mathbf x)=\rho(g)f(\mathbf x)
\]

를 한국어 문장으로 설명하라.

<details>
<summary>해설 보기</summary>

입력에 변환 $g$를 적용한 뒤 $f$를 계산한 결과가, 원래 입력에서 $f$를 계산한 뒤 출력공간의 대응 변환 $\rho(g)$를 적용한 결과와 같다는 뜻이다. 이 등식은 $f$의 equivariance를 나타낸다.

</details>

### 2. 불변 함수 판정

$\mathbf x=(x_1,x_2)^\top$의 두 성분을 바꾸는 순열에 대해 다음 함수 중 불변인 것을 고르라.

\[
f_1(\mathbf x)=x_1+x_2,
\qquad
f_2(\mathbf x)=x_1,
\qquad
f_3(\mathbf x)=\max(x_1,x_2)
\]

<details>
<summary>해설 보기</summary>

$f_1$과 $f_3$는 두 성분의 순서를 바꿔도 값이 같다. $f_2$는 첫 성분을 고르므로 일반적으로 값이 달라진다. 예를 들어 $(1,3)^\top$에서는 $f_2=1$이고 순열 뒤에는 3이다.

</details>

### 3. 직교 불변량 계산

\[
\mathbf Q=
\begin{bmatrix}
0&1\\
-1&0
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}
1\\
2
\end{bmatrix}
\]

일 때 $\|\mathbf x\|_2$와 $\|\mathbf Q\mathbf x\|_2$를 비교하라.

<details>
<summary>해설 보기</summary>

\[
\mathbf Q\mathbf x=
\begin{bmatrix}
2\\
-1
\end{bmatrix}
\]

이므로

\[
\|\mathbf x\|_2=\sqrt{1^2+2^2}=\sqrt5
\]

\[
\|\mathbf Q\mathbf x\|_2=\sqrt{2^2+(-1)^2}=\sqrt5
\]

다. 두 값이 같으며 $\mathbf Q$의 직교성이 일반적인 보존 이유다.

</details>

### 4. equivariance 확인

$f(x_1,x_2)^\top=(x_1+1,x_2+1)^\top$이 성분 순열에 대해 equivariant인지 확인하라.

<details>
<summary>해설 보기</summary>

순열행렬을 $\mathbf P$라 하면

\[
f(\mathbf P\mathbf x)
=
\mathbf P\mathbf x+
\begin{bmatrix}1\\1\end{bmatrix}
\]

이다. 한편

\[
\mathbf P f(\mathbf x)
=
\mathbf P\left(
\mathbf x+
\begin{bmatrix}1\\1\end{bmatrix}
\right)
=
\mathbf P\mathbf x+
\begin{bmatrix}1\\1\end{bmatrix}
\]

이다. 두 식이 같으므로 equivariant다.

</details>

### 5. 불변성과 정보 손실

상수함수 $f(\mathbf x)=0$이 모든 입력변환에 대해 불변임을 설명하고, 이 사실만으로 좋은 표현이라고 할 수 없는 이유를 적어라.

<details>
<summary>해설 보기</summary>

어떤 $g$와 $\mathbf x$를 택해도

\[
f(g\cdot\mathbf x)=0=f(\mathbf x)
\]

이므로 불변이다. 그러나 모든 입력이 같은 출력으로 가므로 입력을 구분하는 정보를 전혀 남기지 않는다. 필요한 변환만 무시하면서 과제 관련 정보를 유지하는지 따로 평가해야 한다.

</details>

### 6. 표현 비교 조건

$\mathbf H_2=\mathbf H_1\mathbf A$이고 $\mathbf A$가 가역이지만 직교행렬은 아니다. 반드시 유지되는 성질과 유지되지 않을 수 있는 성질을 하나씩 제시하라.

<details>
<summary>해설 보기</summary>

가역 오른쪽 곱은 열공간의 차원과 rank를 보존한다. 반면 표본 행 사이의 Euclidean 거리와 각도는 달라질 수 있다. 따라서 선형적으로 담긴 차원은 같을 수 있지만 Euclidean 기하가 같다고 결론 내릴 수 없다.

</details>

### 7. 주장 비판

“두 표현의 Gram 행렬이 같으므로 두 모델은 같은 feature를 같은 neuron에서 사용한다”는 문장을 비판하라.

<details>
<summary>해설 보기</summary>

Gram 행렬은 직교 feature 회전에 불변이다. 두 표현이 직교변환으로 연결되면 표본 사이 내적은 같지만 개별 neuron 좌표는 섞일 수 있다. Gram 행렬의 일치는 표본 관계의 일치를 보이며, neuron별 feature 대응이나 모델의 기능적 사용을 증명하지 않는다.

</details>

## 단원 요약

- 불변량은 지정한 입력변환 아래 값이 유지되는 함수다.
- 직교변환은 Euclidean 내적, norm, 거리와 각도를 보존한다.
- 불변 함수는 입력변환을 출력에서 지우고 equivariant 함수는 대응하는 출력변환으로 운반한다.
- 불변성은 과제에 불필요한 차이를 제거할 때 유용하며 필요한 정보도 없앨 수 있다.
- 표현 비교 지표를 해석하려면 그 지표가 허용하는 변환을 밝혀야 한다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- 불변량을 대상과 허용 변환을 포함해 정의할 수 있는가?
- 불변성과 equivariance의 식을 구분할 수 있는가?
- 직교변환이 내적과 norm을 보존함을 유도할 수 있는가?
- 순열에 대한 합과 성분별 함수의 성질을 확인할 수 있는가?
- 불변성의 정보 손실 가능성을 설명할 수 있는가?
- 표현 비교 지표의 불변성만으로 할 수 없는 주장을 구분할 수 있는가?

## 다음 단원

- [M03-05 부분공간, 직합과 분해](M03-05-subspaces-direct-sums-decomposition.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] 변환 집합을 밝힌 뒤 불변량을 정의했다.
- [x] 불변성과 equivariance를 식과 예제로 구분했다.
- [x] 직교변환의 보존 성질을 계산했다.
- [x] 정보 손실과 주장 범위를 설명했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 구분자를 확인했다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
