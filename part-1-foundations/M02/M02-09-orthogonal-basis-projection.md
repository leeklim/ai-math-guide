---
id: "M02-09"
title: "직교기저와 정사영"
part: 1
stage: "M02"
status: "완료"
prerequisites:
  - "M02-03"
  - "M02-07"
  - "M02-08"
estimated_time: "115~140분"
---

# M02-09. 직교기저와 정사영

## 이 단원이 필요한 이유

기저 벡터들이 서로 직교하면 벡터의 좌표를 연립방정식 없이 내적으로 구할 수 있다. 각 기저 벡터의 길이까지 1이면 좌표는 해당 방향과의 내적이다.

직교기저를 사용하면 벡터를 부분공간에 정사영하고 가장 가까운 근사를 계산할 수 있다. 표현 분석에서는 activation을 특정 부분공간으로 투영하거나 PCA 성분이 설명하는 부분을 복원할 때 같은 계산을 사용한다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- 직교집합, 직교기저와 정규직교기저를 구분할 수 있다.
- 정규직교기저에서 좌표를 내적으로 구할 수 있다.
- 여러 기저 벡터가 만드는 부분공간으로 정사영할 수 있다.
- 정사영 행렬의 대칭성과 멱등성을 확인할 수 있다.
- Gram-Schmidt 과정으로 작은 기저를 정규직교화할 수 있다.
- 최소제곱 문제를 열공간 위의 정사영으로 해석할 수 있다.

## 선수지식 확인

- 선수 단원: [M02-03 내적, 길이와 각도](M02-03-inner-product-length-angle.md)
- 선수 단원: [M02-07 선형독립, 기저와 차원](M02-07-linear-independence-basis-dimension.md)
- 선수 단원: [M02-08 kernel, image와 rank](M02-08-kernel-image-rank.md)
- 확인 질문: 두 벡터의 직교 조건과 한 벡터 위의 정사영을 계산할 수 있는가?
- 확인 질문: 기저와 좌표벡터, 행렬의 열공간을 설명할 수 있는가?

내적, 기저나 열공간이 불분명하면 선수 단원을 먼저 복습한다.

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | 조건 |
|---|---|---|---|
| 직교집합 | `orthogonal set` | 서로 다른 벡터의 내적이 0인 집합 | 영벡터는 기저에 포함하지 않는다. |
| 정규직교집합 | `orthonormal set` | 서로 직교하고 각 norm이 1인 집합 | $\mathbf q_i^\top\mathbf q_j=\delta_{ij}$ |
| $\mathbf Q$ | `Q` | 정규직교 열벡터를 모은 행렬 | $\mathbf Q^\top\mathbf Q=\mathbf I$ |
| $\mathbf P=\mathbf Q\mathbf Q^\top$ | `P equals Q Q transpose` | $\operatorname{im}(\mathbf Q)$ 위의 정사영 행렬 | $\mathbf P^\top=\mathbf P$, $\mathbf P^2=\mathbf P$ |
| $\widehat{\mathbf x}$ | `x hat` | 부분공간 위의 정사영 또는 근삿값 | $\widehat{\mathbf x}=\mathbf P\mathbf x$ |
| 최소제곱 | `least squares` | 잔차 norm의 제곱을 최소화하는 문제 | 정확한 해가 없을 때도 정의 가능 |

## 핵심 개념 1. 직교기저는 서로 간섭하지 않는 방향을 사용한다

0이 아닌 벡터 $\mathbf v_1,\ldots,\mathbf v_k$가

\[
\mathbf v_i^\top\mathbf v_j=0
\qquad
(i\ne j)
\]

를 만족하면 직교집합이다. 직교집합이 공간 $V$를 생성하면 $V$의 직교기저다.

0이 아닌 직교 벡터들은 선형독립이다. 실제로

\[
c_1\mathbf v_1+\cdots+c_k\mathbf v_k=\mathbf 0
\]

의 양변에 $\mathbf v_j^\top$를 곱하면

\[
c_j\|\mathbf v_j\|_2^2=0
\]

이므로 $c_j=0$이다.

## 핵심 개념 2. norm까지 1이면 정규직교기저가 된다

직교 벡터를 자기 norm으로 나누면 단위벡터가 된다.

\[
\mathbf q_i
=
\frac{\mathbf v_i}{\|\mathbf v_i\|_2}
\]

정규직교 벡터들은

\[
\mathbf q_i^\top\mathbf q_j
=
\begin{cases}
1,&i=j\\
0,&i\ne j
\end{cases}
\]

를 만족한다. Kronecker delta를 사용하면 오른쪽을 $\delta_{ij}$라고 쓴다.

정규직교 열벡터를 모은

\[
\mathbf Q=
\begin{bmatrix}
\mathbf q_1&\cdots&\mathbf q_k
\end{bmatrix}
\in\mathbb R^{n\times k}
\]

는

\[
\mathbf Q^\top\mathbf Q=\mathbf I_k
\]

를 만족한다.

## 핵심 개념 3. 정규직교기저의 좌표는 내적이다

$\mathcal Q=(\mathbf q_1,\ldots,\mathbf q_k)$가 부분공간 $V$의 정규직교기저이고 $\mathbf x\in V$라고 하자.

\[
\mathbf x
=
c_1\mathbf q_1+\cdots+c_k\mathbf q_k
\]

의 양변에 $\mathbf q_j^\top$를 곱하면

\[
\mathbf q_j^\top\mathbf x=c_j
\]

이다. 따라서 좌표벡터는

\[
[\mathbf x]_{\mathcal Q}
=
\mathbf Q^\top\mathbf x
\]

이고 원래 벡터는

\[
\mathbf x=\mathbf Q\mathbf Q^\top\mathbf x
\]

로 복원된다.

## 핵심 개념 4. 부분공간 정사영은 각 기저 방향 성분을 더한다

$\mathbf x\in\mathbb R^n$이 $V$ 밖에 있어도 각 정규직교 기저 방향의 계수

\[
c_i=\mathbf q_i^\top\mathbf x
\]

를 구할 수 있다. $V$ 위의 정사영은

\[
\operatorname{proj}_V(\mathbf x)
=
\sum_{i=1}^{k}
(\mathbf q_i^\top\mathbf x)\mathbf q_i
\]

이다. 행렬로는

\[
\widehat{\mathbf x}
=
\mathbf Q\mathbf Q^\top\mathbf x
\]

이다.

정사영 행렬을

\[
\mathbf P=\mathbf Q\mathbf Q^\top
\]

로 두면 $\widehat{\mathbf x}=\mathbf P\mathbf x$다.

## 핵심 개념 5. 잔차는 부분공간과 직교하며 정사영은 가장 가깝다

잔차를

\[
\mathbf r
=
\mathbf x-\widehat{\mathbf x}
\]

라고 하자. 정규직교 기저 행렬에 대해

\[
\mathbf Q^\top\mathbf r=\mathbf 0
\]

이므로 잔차는 $V$의 모든 벡터와 직교한다.

임의의 $\mathbf y\in V$에 대해

\[
\mathbf x-\mathbf y
=
\mathbf r+(\widehat{\mathbf x}-\mathbf y)
\]

이고 두 항은 직교한다. 피타고라스 정리에 따라

\[
\|\mathbf x-\mathbf y\|_2^2
=
\|\mathbf r\|_2^2
+
\|\widehat{\mathbf x}-\mathbf y\|_2^2
\ge
\|\mathbf r\|_2^2
\]

이다. 따라서 $\widehat{\mathbf x}$는 $V$에서 $\mathbf x$와 가장 가까운 벡터다.

## 핵심 개념 6. 정사영 행렬은 대칭이고 멱등이다

\[
\mathbf P=\mathbf Q\mathbf Q^\top
\]

이면

\[
\mathbf P^\top
=
(\mathbf Q\mathbf Q^\top)^\top
=
\mathbf Q\mathbf Q^\top
=
\mathbf P
\]

이다.

또한

\[
\mathbf P^2
=
\mathbf Q\mathbf Q^\top\mathbf Q\mathbf Q^\top
=
\mathbf Q\mathbf I_k\mathbf Q^\top
=
\mathbf P
\]

이다. 한 번 정사영한 벡터는 이미 부분공간에 있으므로 같은 정사영을 다시 적용해도 바뀌지 않는다.

## 핵심 개념 7. Gram-Schmidt 과정은 기저를 정규직교화한다

선형독립 벡터 $\mathbf v_1,\ldots,\mathbf v_k$에서 시작한다. 첫 벡터를 정규화해

\[
\mathbf q_1
=
\frac{\mathbf v_1}{\|\mathbf v_1\|_2}
\]

로 둔다. 둘째 벡터에서 $\mathbf q_1$ 방향 성분을 빼면

\[
\mathbf u_2
=
\mathbf v_2
-
(\mathbf q_1^\top\mathbf v_2)\mathbf q_1
\]

이고

\[
\mathbf q_2
=
\frac{\mathbf u_2}{\|\mathbf u_2\|_2}
\]

로 정규화한다. 이후 벡터에서도 앞에서 만든 모든 $\mathbf q_i$ 방향 성분을 뺀다.

이 과정은 span을 유지하면서 정규직교기저를 만든다. 수치 계산에서는 수정 Gram-Schmidt나 QR 분해가 안정성을 개선한다.

## 핵심 개념 8. 최소제곱은 열공간 위의 정사영이다

$\mathbf A\mathbf c=\mathbf b$에 정확한 해가 없으면 $\mathbf A\mathbf c$가 $\mathbf b$에 가까워지도록

\[
\min_{\mathbf c}
\|\mathbf A\mathbf c-\mathbf b\|_2^2
\]

를 푼다. $\mathbf A\mathbf c$는 $\operatorname{im}(\mathbf A)$에 속하므로 최적 근삿값은 $\mathbf b$를 열공간에 정사영한 벡터다.

최적 잔차

\[
\mathbf r=\mathbf b-\mathbf A\widehat{\mathbf c}
\]

는 모든 열과 직교하므로

\[
\mathbf A^\top\mathbf r=\mathbf 0
\]

이다. 따라서

\[
\mathbf A^\top\mathbf A\widehat{\mathbf c}
=
\mathbf A^\top\mathbf b
\]

라는 정규방정식을 얻는다. $\mathbf A$의 열이 독립이면 해가 하나다.

## 예제 1. 정규직교기저의 좌표

\[
\mathbf q_1=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\1\end{bmatrix},
\qquad
\mathbf q_2=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\-1\end{bmatrix}
\]

은 $\mathbb R^2$의 정규직교기저다. $\mathbf x=\begin{bmatrix}3\\1\end{bmatrix}$의 좌표는

\[
c_1
=
\mathbf q_1^\top\mathbf x
=
\frac{4}{\sqrt2}
=
2\sqrt2
\]

\[
c_2
=
\mathbf q_2^\top\mathbf x
=
\frac{2}{\sqrt2}
=
\sqrt2
\]

이다. 따라서

\[
[\mathbf x]_{\mathcal Q}
=
\begin{bmatrix}
2\sqrt2\\
\sqrt2
\end{bmatrix}
\]

이다.

## 예제 2. 평면 위로 정사영

\[
\mathbf q_1=
\begin{bmatrix}1\\0\\0\end{bmatrix},
\qquad
\mathbf q_2=
\begin{bmatrix}0\\1\\0\end{bmatrix}
\]

가 만드는 평면 $V$에

\[
\mathbf x=
\begin{bmatrix}2\\-1\\4\end{bmatrix}
\]

를 정사영하면

\[
\widehat{\mathbf x}
=
(\mathbf q_1^\top\mathbf x)\mathbf q_1
+
(\mathbf q_2^\top\mathbf x)\mathbf q_2
=
\begin{bmatrix}2\\-1\\0\end{bmatrix}
\]

이다. 잔차는

\[
\mathbf r=
\begin{bmatrix}0\\0\\4\end{bmatrix}
\]

이며 두 기저 벡터와 직교한다.

## 예제 3. Gram-Schmidt 계산

\[
\mathbf v_1=
\begin{bmatrix}1\\1\end{bmatrix},
\qquad
\mathbf v_2=
\begin{bmatrix}1\\0\end{bmatrix}
\]

에서 시작하자.

\[
\mathbf q_1
=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\1\end{bmatrix}
\]

이다. 둘째 벡터의 $\mathbf q_1$ 방향 성분을 빼면

\[
\mathbf u_2
=
\begin{bmatrix}1\\0\end{bmatrix}
-
\frac{1}{\sqrt2}\mathbf q_1
=
\begin{bmatrix}1/2\\-1/2\end{bmatrix}
\]

이다. $\|\mathbf u_2\|_2=1/\sqrt2$이므로

\[
\mathbf q_2
=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\-1\end{bmatrix}
\]

이다.

## 예제 4. 표현 부분공간에 투영하기

정규직교 열을 가진 $\mathbf Q\in\mathbb R^{d\times k}$가 어떤 activation 부분공간을 나타낸다고 하자. activation $\mathbf h\in\mathbb R^d$에서 이 부분공간 성분은

\[
\widehat{\mathbf h}
=
\mathbf Q\mathbf Q^\top\mathbf h
\]

이고 남은 성분은

\[
\mathbf r
=
\mathbf h-\widehat{\mathbf h}
\]

이다.

\[
\frac{\|\widehat{\mathbf h}\|_2^2}
{\|\mathbf h\|_2^2}
\]

는 해당 부분공간이 이 벡터의 제곱 norm 중 차지하는 비율이다. 이 값은 기하학적 분해를 나타낸다. 부분공간의 의미와 모델의 기능적 사용은 데이터 대조와 개입으로 따로 확인해야 한다.

## 흔한 오해

### 오해 1. 직교기저의 모든 벡터는 길이가 1이다

직교기저는 서로 직교하기만 하면 된다. 길이까지 1인 경우를 정규직교기저라고 한다.

### 오해 2. $\mathbf Q\mathbf Q^\top=\mathbf I$가 정규직교 열에서 성립한다

$\mathbf Q\in\mathbb R^{n\times k}$의 열이 정규직교이면 $\mathbf Q^\top\mathbf Q=\mathbf I_k$다. $k<n$이면 $\mathbf Q\mathbf Q^\top$은 $\mathbb R^n$ 전체의 항등행렬이 아니라 $k$차원 열공간 위의 정사영 행렬이다.

### 오해 3. 정사영은 좌표 일부를 0으로 만드는 연산이다

표준 좌표축이 부분공간의 기저일 때만 그렇게 보인다. 일반 부분공간에서는 모든 표준 좌표가 함께 변할 수 있다.

### 오해 4. 정사영된 activation이 크면 모델이 그 부분공간을 사용한다

큰 정사영 norm은 activation이 그 부분공간 방향을 많이 포함한다는 관찰이다. 기능적 사용은 해당 성분을 제거하거나 교체하는 개입으로 평가해야 한다.

## 연습문제

### 1. 직교와 정규직교 판정

\[
\mathbf v_1=
\begin{bmatrix}1\\1\\0\end{bmatrix},
\qquad
\mathbf v_2=
\begin{bmatrix}1\\-1\\0\end{bmatrix}
\]

가 직교하는지 판단하고, 각각을 정규화하라.

<details>
<summary>해설 보기</summary>

\[
\mathbf v_1^\top\mathbf v_2=1-1=0
\]

이므로 직교한다. 두 norm은 모두 $\sqrt2$이므로

\[
\mathbf q_1=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\1\\0\end{bmatrix},
\qquad
\mathbf q_2=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\-1\\0\end{bmatrix}
\]

이다.

</details>

### 2. 정규직교기저 좌표

문제 1의 $\mathbf q_1,\mathbf q_2$가 만드는 부분공간에서

\[
\mathbf x=
\begin{bmatrix}4\\2\\0\end{bmatrix}
\]

의 좌표를 구하라.

<details>
<summary>해설 보기</summary>

\[
c_1=\mathbf q_1^\top\mathbf x
=
\frac{6}{\sqrt2}
=
3\sqrt2
\]

이고

\[
c_2=\mathbf q_2^\top\mathbf x
=
\frac{2}{\sqrt2}
=
\sqrt2
\]

이다. 따라서 좌표벡터는

\[
\begin{bmatrix}3\sqrt2\\\sqrt2\end{bmatrix}
\]

이다.

</details>

### 3. 부분공간 정사영

문제 1의 두 벡터가 만드는 부분공간 $V$에

\[
\mathbf y=
\begin{bmatrix}3\\1\\5\end{bmatrix}
\]

를 정사영하고 잔차를 구하라.

<details>
<summary>해설 보기</summary>

$V$는 $z=0$인 평면이다. 내적으로 구하면

\[
\mathbf q_1^\top\mathbf y=2\sqrt2,
\qquad
\mathbf q_2^\top\mathbf y=\sqrt2
\]

이다. 따라서

\[
\operatorname{proj}_V(\mathbf y)
=
2\sqrt2\mathbf q_1+\sqrt2\mathbf q_2
=
\begin{bmatrix}3\\1\\0\end{bmatrix}
\]

이고 잔차는

\[
\begin{bmatrix}0\\0\\5\end{bmatrix}
\]

이다.

</details>

### 4. 정사영 행렬

\[
\mathbf q=
\frac{1}{\sqrt2}
\begin{bmatrix}1\\1\end{bmatrix}
\]

이 만드는 직선 위의 정사영 행렬 $\mathbf P=\mathbf q\mathbf q^\top$을 구하라.

<details>
<summary>해설 보기</summary>

\[
\mathbf P
=
\frac12
\begin{bmatrix}1\\1\end{bmatrix}
\begin{bmatrix}1&1\end{bmatrix}
=
\frac12
\begin{bmatrix}
1&1\\
1&1
\end{bmatrix}
\]

이다. 이 행렬은 대칭이고 직접 곱하면 $\mathbf P^2=\mathbf P$임을 확인할 수 있다.

</details>

### 5. 가장 가까운 벡터

\[
V=\operatorname{span}
\left\{
\begin{bmatrix}1\\0\end{bmatrix}
\right\},
\qquad
\mathbf x=
\begin{bmatrix}2\\3\end{bmatrix}
\]

일 때 $V$에서 $\mathbf x$와 가장 가까운 벡터와 거리의 제곱을 구하라.

<details>
<summary>해설 보기</summary>

$V$는 $x$축이므로 정사영은

\[
\widehat{\mathbf x}
=
\begin{bmatrix}2\\0\end{bmatrix}
\]

이다. 잔차는 $\begin{bmatrix}0\\3\end{bmatrix}$이고 거리의 제곱은

\[
\|\mathbf x-\widehat{\mathbf x}\|_2^2=9
\]

이다.

</details>

### 6. 최소제곱의 직교 조건

$\widehat{\mathbf c}$가

\[
\min_{\mathbf c}
\|\mathbf A\mathbf c-\mathbf b\|_2^2
\]

의 해라고 하자. 잔차 $\mathbf r=\mathbf b-\mathbf A\widehat{\mathbf c}$가 만족하는 직교 조건과 정규방정식을 쓰라.

<details>
<summary>해설 보기</summary>

최적 근삿값 $\mathbf A\widehat{\mathbf c}$는 $\mathbf b$를 $\operatorname{im}(\mathbf A)$에 정사영한 벡터다. 잔차는 $\mathbf A$의 모든 열과 직교하므로

\[
\mathbf A^\top\mathbf r=\mathbf 0
\]

이다. $\mathbf r=\mathbf b-\mathbf A\widehat{\mathbf c}$를 대입하면

\[
\mathbf A^\top\mathbf A\widehat{\mathbf c}
=
\mathbf A^\top\mathbf b
\]

를 얻는다.

</details>

### 7. 표현 부분공간 해석

activation $\mathbf h$를 부분공간 $V$에 정사영했더니

\[
\frac{\|\operatorname{proj}_V(\mathbf h)\|_2^2}
{\|\mathbf h\|_2^2}
=
0.9
\]

였다. 이 값에서 직접 말할 수 있는 내용과 추가 실험이 필요한 내용을 각각 적어라.

<details>
<summary>해설 보기</summary>

선택한 Euclidean 내적에서 $\mathbf h$의 제곱 norm 중 90%가 $V$ 방향 성분에 있다는 기하학적 사실을 말할 수 있다.

$V$가 인간이 붙인 개념을 안정적으로 나타내는지, 다른 데이터에서도 비율이 유지되는지, 모델이 예측에 이 성분을 사용하는지는 이 값만으로 알 수 없다. 데이터 대조, 기저 안정성 검사와 개입 실험이 필요하다.

</details>

## 단원 요약

- 직교기저는 서로 직교하는 기저이며 정규직교기저는 각 벡터의 norm도 1이다.
- 정규직교기저에서 좌표는 기저 벡터와의 내적으로 구한다.
- $\mathbf Q\mathbf Q^\top\mathbf x$는 $\mathbf x$를 $\operatorname{im}(\mathbf Q)$ 위로 정사영한다.
- 정사영 잔차는 부분공간과 직교하며 정사영 결과는 가장 가까운 벡터다.
- Gram-Schmidt 과정은 독립 기저의 span을 유지하며 정규직교기저를 만든다.
- 최소제곱 해는 목표를 행렬의 열공간에 정사영한 결과와 연결된다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- 직교기저와 정규직교기저를 구분할 수 있는가?
- 정규직교기저에서 좌표를 내적으로 구할 수 있는가?
- 부분공간 정사영과 잔차를 계산할 수 있는가?
- 정사영 행렬의 대칭성과 멱등성을 확인할 수 있는가?
- 두 벡터에 Gram-Schmidt 과정을 적용할 수 있는가?
- 최소제곱을 열공간 정사영으로 설명할 수 있는가?

## 다음 단원

- [M02-10 determinant의 최소 이해](M02-10-determinant-minimum.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] 직교와 정규직교를 구분했다.
- [x] 정규직교기저 좌표와 부분공간 정사영을 계산했다.
- [x] 가장 가까운 벡터 성질을 직교 잔차로 설명했다.
- [x] Gram-Schmidt와 최소제곱 연결을 포함했다.
- [x] 모든 문제에 해설이 있다.
- [x] 정사영 크기와 기능적 사용 주장을 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 내부 링크와 수식 구분자를 확인했다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
