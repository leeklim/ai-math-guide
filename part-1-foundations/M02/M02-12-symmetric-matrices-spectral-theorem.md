---
id: "M02-12"
title: "대칭행렬과 스펙트럼 정리"
part: 1
stage: "M02"
status: "완료"
prerequisites:
  - "M02-09"
  - "M02-11"
estimated_time: "105~130분"
---

# M02-12. 대칭행렬과 스펙트럼 정리

## 이 단원이 필요한 이유

실수 대칭행렬은 고유값이 모두 실수이고 서로 직교하는 고유벡터들로 기저를 만들 수 있다. 일반 정사각행렬에서 생기던 복소 고유값, 부족한 고유벡터와 비직교 고유기저 문제가 사라진다.

공분산행렬과 미분 가능한 scalar 함수의 Hessian은 대칭행렬이 되는 경우가 많다. 스펙트럼 정리를 사용하면 이런 행렬을 직교 방향별 scalar 배율로 분해하고, quadratic form의 부호와 곡률을 고유값으로 읽을 수 있다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- 실수 대칭행렬을 전치 조건으로 판정할 수 있다.
- 서로 다른 고유값의 고유벡터가 직교함을 설명할 수 있다.
- 스펙트럼 분해 $\mathbf A=\mathbf Q\boldsymbol\Lambda\mathbf Q^\top$의 shape과 역할을 읽을 수 있다.
- 정규직교 고유기저에서 벡터 변환과 quadratic form을 계산할 수 있다.
- 고유값으로 양의 준정부호 여부를 판정할 수 있다.
- 대칭행렬의 스펙트럼과 모델 해석 주장의 범위를 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [M02-09 직교기저와 정사영](M02-09-orthogonal-basis-projection.md)
- 선수 단원: [M02-11 고유값과 고유벡터](M02-11-eigenvalues-eigenvectors.md)
- 확인 질문: 정규직교 행렬의 $\mathbf Q^\top\mathbf Q=\mathbf I$ 조건을 설명할 수 있는가?
- 확인 질문: 고유값, 고유공간과 대각화를 정의할 수 있는가?

정규직교기저나 고유값분해가 불분명하면 선수 단원을 먼저 복습한다.

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | 조건 |
|---|---|---|---|
| $\mathbf A=\mathbf A^\top$ | `A equals A transpose` | 실수 대칭행렬 조건 | $\mathbf A\in\mathbb R^{n\times n}$ |
| $\mathbf Q$ | `Q` | 정규직교 고유벡터를 열로 모은 행렬 | $\mathbf Q^\top\mathbf Q=\mathbf Q\mathbf Q^\top=\mathbf I_n$ |
| $\boldsymbol\Lambda$ | `capital lambda` | 고유값을 대각에 놓은 행렬 | $\boldsymbol\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)$ |
| $\mathbf x^\top\mathbf A\mathbf x$ | `x transpose A x` | $\mathbf A$의 quadratic form | 결과는 scalar |
| 양의 준정부호 | `positive semidefinite` | 모든 quadratic form 값이 0 이상인 성질 | $\mathbf x^\top\mathbf A\mathbf x\ge0$ |

## 핵심 개념 1. 대칭행렬은 주대각선을 기준으로 원소가 대응한다

실수 정사각행렬 $\mathbf A$가

\[
\mathbf A^\top=\mathbf A
\]

를 만족하면 대칭행렬이다. 원소로는

\[
a_{ij}=a_{ji}
\]

이다.

\[
\begin{bmatrix}
2&-1&4\\
-1&3&0\\
4&0&5
\end{bmatrix}
\]

는 대칭행렬이다. 주대각선 위의 원소를 뒤집어 아래쪽 원소를 얻는다.

## 핵심 개념 2. 대칭행렬의 고유값은 실수다

실수 대칭행렬은 복소수까지 고려해도 모든 고유값이 실수다. M02-11의 $90^\circ$ 회전행렬처럼 실수 고유값이 없는 경우가 대칭행렬에서는 생기지 않는다.

이 단원에서는 정리의 전체 증명보다 결과와 사용 조건을 다룬다. 조건 $\mathbf A=\mathbf A^\top$을 먼저 확인해야 이 결론을 사용할 수 있다.

## 핵심 개념 3. 서로 다른 고유값의 고유벡터는 직교한다

\[
\mathbf A\mathbf u=\lambda\mathbf u,
\qquad
\mathbf A\mathbf v=\mu\mathbf v
\]

이고 $\lambda\ne\mu$라고 하자. 대칭성을 사용하면

\[
\mathbf u^\top\mathbf A\mathbf v
=
(\mathbf A\mathbf u)^\top\mathbf v
\]

이다. 양쪽에 고유값 식을 대입하면

\[
\mu\mathbf u^\top\mathbf v
=
\lambda\mathbf u^\top\mathbf v
\]

이므로

\[
(\mu-\lambda)\mathbf u^\top\mathbf v=0
\]

이다. $\mu-\lambda\ne0$이므로

\[
\mathbf u^\top\mathbf v=0
\]

이다.

고유값이 반복되는 고유공간 안에서도 직교기저를 선택할 수 있다.

## 핵심 개념 4. 스펙트럼 정리는 정규직교 고유기저를 보장한다

실수 대칭행렬 $\mathbf A\in\mathbb R^{n\times n}$에는 정규직교 고유벡터

\[
\mathbf q_1,\ldots,\mathbf q_n
\]

가 존재한다. 이 벡터들을 열로 모아

\[
\mathbf Q=
\begin{bmatrix}
\mathbf q_1&\cdots&\mathbf q_n
\end{bmatrix}
\]

로 두면

\[
\mathbf Q^\top\mathbf Q=\mathbf I_n
\]

이다. 대응 고유값을 대각행렬 $\boldsymbol\Lambda$에 놓으면

\[
\mathbf A
=
\mathbf Q\boldsymbol\Lambda\mathbf Q^\top
\]

이다. 이것이 실수 대칭행렬의 스펙트럼 분해다.

일반 대각화의 $\mathbf V^{-1}$ 자리에 $\mathbf Q^\top$이 놓인다. 정규직교 행렬의 역이 전치이기 때문이다.

## 핵심 개념 5. 변환은 회전, 축별 배율, 역회전으로 나뉜다

\[
\mathbf A\mathbf x
=
\mathbf Q\boldsymbol\Lambda\mathbf Q^\top\mathbf x
\]

를 오른쪽부터 읽으면 다음 계산을 한다.

1. $\mathbf Q^\top\mathbf x$: 고유기저 좌표를 구한다.
2. $\boldsymbol\Lambda$: 각 고유방향 성분에 $\lambda_i$를 곱한다.
3. $\mathbf Q$: 원래 표준 좌표로 돌아온다.

대칭행렬은 직교 좌표계를 선택하면 방향을 섞지 않고 좌표별로 배율만 적용한다.

## 핵심 개념 6. quadratic form은 고유방향별 기여의 합이다

\[
\mathbf x=\mathbf Q\mathbf c
\]

로 고유기저 좌표 $\mathbf c=\mathbf Q^\top\mathbf x$를 쓰면

\[
\mathbf x^\top\mathbf A\mathbf x
=
\mathbf c^\top\boldsymbol\Lambda\mathbf c
=
\sum_{i=1}^{n}\lambda_i c_i^2
\]

이다.

각 고유값은 해당 고유방향 성분의 제곱에 붙는 계수다. 모든 고유값이 0 이상이면

\[
\mathbf x^\top\mathbf A\mathbf x\ge0
\]

이므로 $\mathbf A$는 양의 준정부호다. 고유값이 하나라도 음수이면 그 고유벡터 방향에서 quadratic form이 음수가 된다.

## 핵심 개념 7. 스펙트럼 분해는 행렬함수를 방향별로 계산한다

정수 $k\ge0$에 대해

\[
\mathbf A^k
=
\mathbf Q\boldsymbol\Lambda^k\mathbf Q^\top
\]

이다. 지수함수처럼 scalar에 정의된 함수를 고유값에 적용해

\[
f(\mathbf A)
=
\mathbf Q f(\boldsymbol\Lambda)\mathbf Q^\top
\]

형태로 행렬함수를 정의할 수 있다.

고유값이 0이 아니면 역행렬도

\[
\mathbf A^{-1}
=
\mathbf Q\boldsymbol\Lambda^{-1}\mathbf Q^\top
\]

로 계산한다.

## 예제 1. 대칭행렬의 고유쌍

\[
\mathbf A=
\begin{bmatrix}
2&1\\
1&2
\end{bmatrix}
\]

의 고유값은 3과 1이다. 대응하는 정규직교 고유벡터를

\[
\mathbf q_1=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\1\end{bmatrix},
\qquad
\mathbf q_2=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\-1\end{bmatrix}
\]

로 고를 수 있다.

\[
\mathbf A\mathbf q_1=3\mathbf q_1,
\qquad
\mathbf A\mathbf q_2=\mathbf q_2
\]

이고 $\mathbf q_1^\top\mathbf q_2=0$이다.

## 예제 2. 스펙트럼 분해로 변환하기

예제 1에서

\[
\mathbf Q=
\frac{1}{\sqrt2}
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix},
\qquad
\boldsymbol\Lambda=
\begin{bmatrix}
3&0\\
0&1
\end{bmatrix}
\]

이다.

\[
\mathbf x=
\begin{bmatrix}2\\0\end{bmatrix}
\]

의 고유기저 좌표는

\[
\mathbf c=\mathbf Q^\top\mathbf x
=
\begin{bmatrix}\sqrt2\\\sqrt2\end{bmatrix}
\]

이다. 고유값을 곱하면

\[
\boldsymbol\Lambda\mathbf c
=
\begin{bmatrix}3\sqrt2\\\sqrt2\end{bmatrix}
\]

이고 표준 좌표로 돌아오면

\[
\mathbf A\mathbf x
=
\mathbf Q\boldsymbol\Lambda\mathbf c
=
\begin{bmatrix}4\\2\end{bmatrix}
\]

이다.

## 예제 3. PSD 판정

\[
\mathbf B=
\begin{bmatrix}
2&-2\\
-2&2
\end{bmatrix}
\]

의 고유값은 4와 0이다. 두 값이 모두 0 이상이므로 $\mathbf B$는 양의 준정부호다.

\[
\mathbf x^\top\mathbf B\mathbf x
=
2(x_1-x_2)^2
\ge0
\]

이다. 고유값 0에 대응하는 $\begin{bmatrix}1\\1\end{bmatrix}$ 방향에서는 quadratic form이 0이다.

## 예제 4. Hessian과 공분산행렬

두 번 연속 미분 가능한 scalar 함수에서 혼합편미분의 순서를 바꿀 수 있는 조건이 성립하면 Hessian은 대칭이다. 고유벡터는 국소 곡률 방향이고 고유값은 그 방향의 이차 변화율을 나타낸다.

공분산행렬도 대칭이며 양의 준정부호다. 고유벡터는 데이터 변동 방향, 고유값은 그 방향의 분산과 연결된다. M02-14에서 PCA로 계산한다.

이 해석은 주어진 점이나 데이터 분포에서의 구조를 말한다. 큰 고유값 하나만으로 feature 의미나 모델 행동의 인과적 중요성을 정할 수 없다.

## 흔한 오해

### 오해 1. 모든 정사각행렬은 정규직교 고유기저를 갖는다

스펙트럼 정리는 실수 대칭행렬에 적용한다. 일반 비대칭행렬은 고유벡터가 직교하지 않거나 기저를 이루지 못할 수 있다.

### 오해 2. 반복 고유값에는 고유벡터가 하나뿐이다

반복 고유값의 고유공간은 여러 dimension을 가질 수 있다. 대칭행렬에서는 각 고유공간 안에서 정규직교기저를 선택할 수 있다.

### 오해 3. PSD 행렬의 고유값은 모두 양수다

양의 준정부호에서는 0인 고유값을 허용한다. 모든 고유값이 양수인 경우는 양의 정부호다.

### 오해 4. 가장 큰 고유값 방향은 자동으로 가장 중요한 모델 feature다

가장 큰 고유값은 해당 행렬이 정한 양의 변화가 큰 방향이다. 인간 해석 가능성과 모델의 기능적 사용은 데이터와 개입 증거가 더 필요하다.

## 연습문제

### 1. 대칭성 판정

다음 행렬 중 대칭행렬을 모두 고르라.

\[
\mathbf A=
\begin{bmatrix}1&2\\2&3\end{bmatrix},
\qquad
\mathbf B=
\begin{bmatrix}1&0\\4&1\end{bmatrix},
\qquad
\mathbf C=
\begin{bmatrix}5&-1\\-1&0\end{bmatrix}
\]

<details>
<summary>해설 보기</summary>

$\mathbf A^\top=\mathbf A$이고 $\mathbf C^\top=\mathbf C$이므로 $\mathbf A$와 $\mathbf C$는 대칭행렬이다. $\mathbf B$는 $b_{12}=0$과 $b_{21}=4$가 달라 대칭이 아니다.

</details>

### 2. 직교하는 고유벡터

\[
\mathbf A=
\begin{bmatrix}2&1\\1&2\end{bmatrix}
\]

에서

\[
\mathbf v_1=
\begin{bmatrix}1\\1\end{bmatrix},
\qquad
\mathbf v_2=
\begin{bmatrix}1\\-1\end{bmatrix}
\]

가 서로 다른 고유값의 고유벡터이고 직교함을 확인하라.

<details>
<summary>해설 보기</summary>

\[
\mathbf A\mathbf v_1
=
\begin{bmatrix}3\\3\end{bmatrix}
=
3\mathbf v_1
\]

이고

\[
\mathbf A\mathbf v_2
=
\begin{bmatrix}1\\-1\end{bmatrix}
=
\mathbf v_2
\]

이다. 고유값은 각각 3과 1로 다르다.

\[
\mathbf v_1^\top\mathbf v_2=1-1=0
\]

이므로 두 고유벡터는 직교한다.

</details>

### 3. 스펙트럼 분해 읽기

\[
\mathbf A
=
\mathbf Q
\begin{bmatrix}5&0\\0&2\end{bmatrix}
\mathbf Q^\top
\]

이고 $\mathbf Q$의 열이 $\mathbf q_1,\mathbf q_2$라고 하자. $\mathbf A\mathbf q_1$과 $\mathbf A\mathbf q_2$를 구하라.

<details>
<summary>해설 보기</summary>

$\mathbf Q^\top\mathbf q_1=\mathbf e_1$이고 $\mathbf Q^\top\mathbf q_2=\mathbf e_2$다. 따라서

\[
\mathbf A\mathbf q_1=5\mathbf q_1,
\qquad
\mathbf A\mathbf q_2=2\mathbf q_2
\]

이다.

</details>

### 4. quadratic form 계산

정규직교 고유기저 좌표가

\[
\mathbf c=
\begin{bmatrix}2\\-1\end{bmatrix}
\]

이고 고유값이 $\lambda_1=3$, $\lambda_2=-2$라고 하자. $\mathbf x^\top\mathbf A\mathbf x$를 구하고 부호를 설명하라.

<details>
<summary>해설 보기</summary>

\[
\mathbf x^\top\mathbf A\mathbf x
=
\lambda_1c_1^2+\lambda_2c_2^2
=
3\cdot4+(-2)\cdot1
=
10
\]

이다. 이 $\mathbf x$에서는 양수지만 $\lambda_2<0$이므로 행렬은 PSD가 아니다. $\mathbf q_2$ 방향에서는 quadratic form이 음수다.

</details>

### 5. PSD 판정

실수 대칭행렬의 고유값이 $4,1,0$이라고 하자. PSD인지, 가역인지 각각 판단하라.

<details>
<summary>해설 보기</summary>

모든 고유값이 0 이상이므로 PSD다. 고유값 0이 있으므로 kernel이 0이 아니며 역행렬은 존재하지 않는다.

</details>

### 6. 행렬 거듭제곱

\[
\mathbf A=\mathbf Q
\begin{bmatrix}2&0\\0&-1\end{bmatrix}
\mathbf Q^\top
\]

일 때 $\mathbf A^4$를 스펙트럼 분해 형태로 쓰라.

<details>
<summary>해설 보기</summary>

\[
\mathbf A^4
=
\mathbf Q
\begin{bmatrix}2^4&0\\0&(-1)^4\end{bmatrix}
\mathbf Q^\top
=
\mathbf Q
\begin{bmatrix}16&0\\0&1\end{bmatrix}
\mathbf Q^\top
\]

이다.

</details>

### 7. 스펙트럼 주장 비판

어떤 activation 공분산행렬의 가장 큰 고유값이 나머지보다 크다고 하자. 다음을 구분해 설명하라.

1. 직접 말할 수 있는 기하학적 사실
2. 데이터와 전처리에 관해 확인할 조건
3. 이 결과만으로 말할 수 없는 모델 기능 주장

<details>
<summary>해설 보기</summary>

해당 데이터와 내적 아래에서 첫 고유벡터 방향의 표본 분산이 가장 크다고 말할 수 있다.

데이터 표본, 중심화, feature 스케일과 이상치가 결과를 바꿀 수 있으므로 이 조건들을 확인해야 한다.

분산이 큰 방향이 인간이 해석하는 개념인지, 모델이 예측에 그 방향을 사용하는지, 다른 데이터에도 일반화되는지는 고유값 하나로 알 수 없다. 의미 검증과 개입 실험이 필요하다.

</details>

## 단원 요약

- 실수 대칭행렬은 전치와 같으며 고유값이 모두 실수다.
- 서로 다른 고유값에 대응하는 고유벡터는 직교한다.
- 스펙트럼 정리는 대칭행렬에 정규직교 고유기저가 존재함을 보장한다.
- $\mathbf A=\mathbf Q\boldsymbol\Lambda\mathbf Q^\top$은 고유기저에서 방향별 배율을 적용하는 분해다.
- quadratic form은 $\sum_i\lambda_i c_i^2$이며 PSD 여부를 고유값 부호로 판정한다.
- 스펙트럼은 행렬의 구조를 설명하며 feature 의미와 기능적 사용은 추가 증거가 필요하다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- 대칭행렬을 원소와 전치 조건으로 판정할 수 있는가?
- 서로 다른 고유값의 고유벡터가 직교하는 이유를 설명할 수 있는가?
- 스펙트럼 분해의 세 행렬 shape과 역할을 읽을 수 있는가?
- 고유기저 좌표에서 변환과 quadratic form을 계산할 수 있는가?
- 고유값으로 PSD와 가역성을 판정할 수 있는가?
- 대칭행렬 스펙트럼의 해석 범위를 설명할 수 있는가?

## 다음 단원

- [M02-13 특이값분해](M02-13-singular-value-decomposition.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] 대칭 조건과 스펙트럼 정리의 적용 범위를 밝혔다.
- [x] 직교성의 핵심 계산을 제시했다.
- [x] 스펙트럼 분해와 quadratic form을 연결했다.
- [x] PSD를 고유값으로 판정했다.
- [x] 모든 문제에 해설이 있다.
- [x] 스펙트럼 구조와 모델 기능 주장을 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 내부 링크와 수식 구분자를 확인했다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
