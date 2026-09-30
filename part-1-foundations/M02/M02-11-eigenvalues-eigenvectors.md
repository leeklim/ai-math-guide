---
id: "M02-11"
title: "고유값과 고유벡터"
part: 1
stage: "M02"
status: "완료"
prerequisites:
  - "M02-06"
  - "M02-07"
  - "M02-10"
estimated_time: "110~135분"
---

# M02-11. 고유값과 고유벡터

## 이 단원이 필요한 이유

선형변환은 벡터의 방향을 섞지만 일부 특별한 방향은 같은 직선 위에 남는다. 그 방향을 나타내는 벡터가 고유벡터이고, 그 방향에서의 확대·축소 계수가 고유값이다.

고유방향을 찾으면 같은 행렬을 반복 적용하는 계산, 선형 동역학과 곡률 행렬을 방향별로 나누어 볼 수 있다. 정사각행렬만 대상으로 하며, 비대칭행렬은 실수 고유벡터가 충분하지 않을 수 있다는 제한도 함께 확인해야 한다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- 고유값과 고유벡터를 $\mathbf A\mathbf v=\lambda\mathbf v$로 정의할 수 있다.
- 특성방정식으로 작은 행렬의 고유값을 구할 수 있다.
- 각 고유값의 고유공간을 kernel로 계산할 수 있다.
- 고유값의 부호와 크기를 방향별 변환으로 해석할 수 있다.
- 행렬 거듭제곱이 고유방향에 미치는 영향을 계산할 수 있다.
- 고유벡터 기저가 있을 때 대각화를 설명하고 실패하는 경우를 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [M02-06 연립방정식과 역행렬](M02-06-linear-systems-inverse.md)
- 선수 단원: [M02-07 선형독립, 기저와 차원](M02-07-linear-independence-basis-dimension.md)
- 선수 단원: [M02-10 determinant의 최소 이해](M02-10-determinant-minimum.md)
- 확인 질문: 동차연립방정식의 kernel 기저를 구할 수 있는가?
- 확인 질문: determinant 0과 정사각행렬의 비가역성을 연결할 수 있는가?

kernel, 기저나 determinant가 불분명하면 선수 단원을 먼저 복습한다.

## 기호와 용어

| 기호·용어 | 읽는 법 | 의미 | 조건 |
|---|---|---|---|
| $\lambda$ | 람다 | 고유방향의 확대·축소 계수 | scalar |
| $\mathbf v$ | 굵은 브이 | 고유값 $\lambda$에 대응하는 고유벡터 | $\mathbf v\ne\mathbf 0$ |
| $\mathbf A\mathbf v=\lambda\mathbf v$ | 에이 브이는 람다 브이 | 변환 뒤 같은 직선 위에 남는 조건 | $\mathbf A$는 정사각행렬 |
| $\det(\mathbf A-\lambda\mathbf I)=0$ | 에이 마이너스 람다 아이의 determinant는 0 | 고유값을 찾는 특성방정식 | $\lambda$에 관한 방정식 |
| $E_\lambda$ | 람다 고유공간 | $\lambda$에 대응하는 고유벡터들과 영벡터의 공간 | $\ker(\mathbf A-\lambda\mathbf I)$ |
| 대각화 | diagonalization | 고유벡터 기저에서 행렬을 대각행렬로 나타내는 것 | 독립인 고유벡터가 충분해야 한다. |

## 핵심 개념 1. 고유벡터는 방향이 유지되는 0이 아닌 벡터다

정사각행렬 $\mathbf A\in\mathbb R^{n\times n}$에 대해

\[
\mathbf A\mathbf v=\lambda\mathbf v,
\qquad
\mathbf v\ne\mathbf 0
\]

를 만족하면 $\mathbf v$를 고유벡터, $\lambda$를 대응하는 고유값이라고 한다.

$\lambda>0$이면 같은 방향에서 $|\lambda|$배 되고, $\lambda<0$이면 반대 방향으로 뒤집히며 $|\lambda|$배 된다. $\lambda=0$이면 고유벡터가 kernel 방향에 있어 영벡터로 간다.

영벡터는 모든 $\lambda$에 대해 식을 만족하므로 고유벡터에서 제외한다.

## 핵심 개념 2. 고유값은 특성방정식으로 찾는다

\[
\mathbf A\mathbf v=\lambda\mathbf v
\]

를 옮기면

\[
(\mathbf A-\lambda\mathbf I)\mathbf v=\mathbf 0
\]

이다. 0이 아닌 해 $\mathbf v$가 존재하려면 $\mathbf A-\lambda\mathbf I$가 특이행렬이어야 한다. 따라서

\[
\det(\mathbf A-\lambda\mathbf I)=0
\]

을 만족하는 $\lambda$를 찾는다.

\[
p_{\mathbf A}(\lambda)
=
\det(\mathbf A-\lambda\mathbf I)
\]

를 특성다항식이라고 한다. 부호를 반대로 둔 $\det(\lambda\mathbf I-\mathbf A)$도 같은 근을 가지며 문헌에서 함께 사용한다.

## 핵심 개념 3. 고유벡터는 각 고유값의 kernel에서 찾는다

고유값 $\lambda$를 구한 뒤

\[
(\mathbf A-\lambda\mathbf I)\mathbf v=\mathbf 0
\]

을 푼다.

\[
E_\lambda
=
\ker(\mathbf A-\lambda\mathbf I)
\]

를 $\lambda$의 고유공간이라고 한다. 고유공간은 영벡터도 포함하지만, 고유벡터는 그 안의 0이 아닌 벡터들이다.

한 고유벡터의 0이 아닌 scalar배도 같은 고유값의 고유벡터다. 고유벡터 하나의 숫자 목록보다 고유공간 전체가 변환의 방향 구조를 나타낸다.

## 핵심 개념 4. 반복 적용에서는 고유값이 거듭제곱된다

\[
\mathbf A\mathbf v=\lambda\mathbf v
\]

이면

\[
\mathbf A^2\mathbf v
=
\mathbf A(\lambda\mathbf v)
=
\lambda^2\mathbf v
\]

이고 일반적으로

\[
\mathbf A^k\mathbf v
=
\lambda^k\mathbf v
\]

이다.

- $|\lambda|>1$이면 반복할수록 해당 방향 성분의 크기가 커진다.
- $|\lambda|<1$이면 해당 방향 성분이 줄어든다.
- $\lambda<0$이면 반복 횟수에 따라 방향이 번갈아 뒤집힌다.

$|\lambda|=1$에서는 크기가 유지되지만 비대각화 행렬의 다른 성분은 커질 수 있다. 고유값 크기만으로 일반 행렬의 모든 반복 동작을 판단하지 않는다.

## 핵심 개념 5. 고유벡터 기저가 있으면 행렬을 대각화할 수 있다

$n$개의 선형독립 고유벡터 $\mathbf v_1,\ldots,\mathbf v_n$이 있고 대응 고유값이 $\lambda_1,\ldots,\lambda_n$이라고 하자.

\[
\mathbf V=
\begin{bmatrix}
\mathbf v_1&\cdots&\mathbf v_n
\end{bmatrix},
\qquad
\boldsymbol\Lambda=
\begin{bmatrix}
\lambda_1&&0\\
&\ddots&\\
0&&\lambda_n
\end{bmatrix}
\]

로 두면

\[
\mathbf A\mathbf V=\mathbf V\boldsymbol\Lambda
\]

이고 $\mathbf V$가 가역이므로

\[
\mathbf A
=
\mathbf V\boldsymbol\Lambda\mathbf V^{-1}
\]

이다. 이를 대각화라고 한다.

고유벡터 기저의 좌표에서는 $\mathbf A$가 각 좌표에 고유값만 곱한다. 또한

\[
\mathbf A^k
=
\mathbf V\boldsymbol\Lambda^k\mathbf V^{-1}
\]

로 거듭제곱을 계산할 수 있다.

## 핵심 개념 6. 모든 정사각행렬이 실수에서 대각화되지는 않는다

\[
\mathbf S=
\begin{bmatrix}
1&1\\
0&1
\end{bmatrix}
\]

의 고유값은 1 하나다. 고유공간은

\[
\ker(\mathbf S-\mathbf I)
=
\operatorname{span}
\left\{
\begin{bmatrix}1\\0\end{bmatrix}
\right\}
\]

이므로 독립 고유벡터가 하나뿐이다. $\mathbb R^2$의 고유벡터 기저를 만들 수 없어 대각화되지 않는다.

$90^\circ$ 회전행렬

\[
\begin{bmatrix}0&-1\\1&0\end{bmatrix}
\]

은 0이 아닌 실수 벡터의 방향을 모두 바꾸므로 실수 고유벡터가 없다. 복소수까지 허용하면 고유값을 찾을 수 있지만 이 단원에서는 실수 공간을 다룬다.

## 핵심 개념 7. 고유값은 정사각 선형변환의 방향별 구조다

직사각행렬에는

\[
\mathbf A\mathbf v=\lambda\mathbf v
\]

에서 양변의 dimension이 같지 않으므로 같은 방식의 고유값을 정의하지 않는다. 직사각행렬이나 서로 다른 입력·출력 공간의 방향별 증폭은 SVD로 분석한다.

비대칭 정사각행렬은 고유벡터가 직교하지 않거나 충분하지 않을 수 있다. M02-12에서는 실수 대칭행렬이 정규직교 고유기저를 갖는다는 스펙트럼 정리를 배운다.

## 예제 1. 대각행렬의 고유값

\[
\mathbf D=
\begin{bmatrix}
4&0\\
0&-2
\end{bmatrix}
\]

이면

\[
\mathbf D\mathbf e_1=4\mathbf e_1,
\qquad
\mathbf D\mathbf e_2=-2\mathbf e_2
\]

이다. $\mathbf e_1$은 고유값 4의 고유벡터이고 $\mathbf e_2$는 고유값 $-2$의 고유벡터다.

첫 방향은 4배 확대되고 둘째 방향은 반대로 뒤집히며 2배 확대된다.

## 예제 2. $2\times2$ 고유값과 고유벡터

\[
\mathbf A=
\begin{bmatrix}
2&1\\
0&3
\end{bmatrix}
\]

라고 하자. 특성방정식은

\[
\det(\mathbf A-\lambda\mathbf I)
=
\det
\begin{bmatrix}
2-\lambda&1\\
0&3-\lambda
\end{bmatrix}
=
(2-\lambda)(3-\lambda)
=
0
\]

이다. 고유값은 2와 3이다.

$\lambda=2$이면

\[
(\mathbf A-2\mathbf I)\mathbf v=\mathbf 0
\]

에서 둘째 성분이 0이므로

\[
E_2
=
\operatorname{span}
\left\{
\begin{bmatrix}1\\0\end{bmatrix}
\right\}
\]

이다.

$\lambda=3$이면 $-v_1+v_2=0$이므로

\[
E_3
=
\operatorname{span}
\left\{
\begin{bmatrix}1\\1\end{bmatrix}
\right\}
\]

이다.

## 예제 3. 고유기저에서 반복 계산

예제 2의 고유벡터를 사용해

\[
\mathbf x
=
2
\begin{bmatrix}1\\0\end{bmatrix}
+
1
\begin{bmatrix}1\\1\end{bmatrix}
\]

라고 하자. 그러면

\[
\mathbf A^k\mathbf x
=
2\cdot2^k
\begin{bmatrix}1\\0\end{bmatrix}
+
3^k
\begin{bmatrix}1\\1\end{bmatrix}
\]

이다. $k$가 커지면 고유값 3의 방향 성분이 고유값 2의 방향 성분보다 빠르게 커진다.

## 예제 4. 모델 분석에서 고유방향 읽기

대칭 Hessian의 고유벡터는 파라미터 공간의 직교 곡률 방향을 나타내고 고유값은 각 방향의 이차 변화율과 연결된다. 이 해석은 M03-12에서 미분과 함께 다룬다.

weight matrix가 직사각형이면 고유값 분석을 그대로 적용할 수 없다. 정사각행렬에서도 비대칭이면 고유벡터가 불안정하거나 기저를 이루지 못할 수 있다. 분석 대상의 shape과 대칭성을 먼저 확인한다.

## 흔한 오해

### 오해 1. 고유벡터는 변환해도 값이 그대로인 벡터다

고유벡터는 같은 직선 위에 남는 벡터다. 고유값에 따라 크기가 변하고 부호가 음수이면 방향이 뒤집힌다.

### 오해 2. 영벡터도 고유벡터다

영벡터는 모든 $\lambda$에 대해 식을 만족해 고유값을 구분하지 못한다. 정의에서 제외한다.

### 오해 3. 고유값이 중복되면 독립 고유벡터도 그만큼 있다

반복되는 고유값의 고유공간 dimension은 중복 횟수보다 작을 수 있다. 독립 고유벡터가 $n$개 있어야 $n\times n$ 행렬을 대각화할 수 있다.

### 오해 4. 큰 고유값은 모델에서 중요한 feature를 뜻한다

고유값 크기는 해당 선형변환의 고유방향 증폭을 나타낸다. 인간이 해석한 feature와의 대응이나 모델 행동의 인과적 중요성은 추가 증거가 필요하다.

## 연습문제

### 1. 고유쌍 확인

\[
\mathbf A=
\begin{bmatrix}
3&0\\
0&-1
\end{bmatrix},
\qquad
\mathbf v=
\begin{bmatrix}0\\2\end{bmatrix}
\]

에 대해 $\mathbf v$가 고유벡터인지 확인하고 고유값을 구하라.

<details>
<summary>해설 보기</summary>

\[
\mathbf A\mathbf v
=
\begin{bmatrix}0\\-2\end{bmatrix}
=
-1
\begin{bmatrix}0\\2\end{bmatrix}
\]

이다. $\mathbf v\ne\mathbf 0$이고 변환 결과가 $\mathbf v$의 $-1$배이므로 고유값은 $-1$이다.

</details>

### 2. 고유값 구하기

\[
\mathbf B=
\begin{bmatrix}
1&2\\
0&4
\end{bmatrix}
\]

의 특성방정식과 고유값을 구하라.

<details>
<summary>해설 보기</summary>

\[
\det(\mathbf B-\lambda\mathbf I)
=
\det
\begin{bmatrix}
1-\lambda&2\\
0&4-\lambda
\end{bmatrix}
=
(1-\lambda)(4-\lambda)
\]

이다. 특성방정식을 0으로 두면 고유값은 $\lambda=1,4$다.

</details>

### 3. 고유공간 구하기

문제 2의 각 고유값에 대한 고유공간의 기저를 구하라.

<details>
<summary>해설 보기</summary>

$\lambda=1$이면

\[
\mathbf B-\mathbf I
=
\begin{bmatrix}0&2\\0&3\end{bmatrix}
\]

이므로 $v_2=0$이다. 따라서

\[
E_1
=
\operatorname{span}
\left\{
\begin{bmatrix}1\\0\end{bmatrix}
\right\}
\]

이다.

$\lambda=4$이면

\[
\mathbf B-4\mathbf I
=
\begin{bmatrix}-3&2\\0&0\end{bmatrix}
\]

이므로 $-3v_1+2v_2=0$이다. 예를 들어 $\mathbf v=\begin{bmatrix}2\\3\end{bmatrix}$를 고를 수 있어

\[
E_4
=
\operatorname{span}
\left\{
\begin{bmatrix}2\\3\end{bmatrix}
\right\}
\]

이다.

</details>

### 4. 반복 적용

$\mathbf A\mathbf v=-2\mathbf v$일 때 $\mathbf A^5\mathbf v$를 구하고 방향과 크기 변화를 설명하라.

<details>
<summary>해설 보기</summary>

\[
\mathbf A^5\mathbf v
=
(-2)^5\mathbf v
=
-32\mathbf v
\]

이다. 크기는 32배가 되고 홀수 번의 음수 배율 때문에 원래 벡터와 반대 방향이다.

</details>

### 5. 대각화 가능성

$3\times3$ 행렬이 서로 다른 고유값 세 개를 갖는다고 하자. 대각화 가능한지 판단하고 이유를 설명하라.

<details>
<summary>해설 보기</summary>

서로 다른 고유값에 속하는 고유벡터들은 선형독립이다. 따라서 독립 고유벡터 세 개가 $\mathbb R^3$의 기저를 이루며 행렬은 대각화 가능하다.

</details>

### 6. 실수 고유벡터의 부재

\[
\mathbf R=
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}
\]

의 특성방정식을 구하고 실수 고유값이 있는지 판단하라.

<details>
<summary>해설 보기</summary>

\[
\det(\mathbf R-\lambda\mathbf I)
=
\det
\begin{bmatrix}
-\lambda&-1\\
1&-\lambda
\end{bmatrix}
=
\lambda^2+1
\]

이다. 실수 $\lambda$에 대해 $\lambda^2+1=0$을 만족하는 해가 없으므로 실수 고유값과 실수 고유벡터가 없다.

</details>

### 7. 분석 방법 선택

다음 각 행렬에 고유값분해와 SVD 중 어느 분석이 우선 맞는지 판단하고 이유를 설명하라.

1. $\mathbf H\in\mathbb R^{d\times d}$인 실수 대칭 Hessian
2. $\mathbf W\in\mathbb R^{64\times128}$인 직사각 weight matrix
3. $\mathbf A\in\mathbb R^{d\times d}$인 비대칭 정사각행렬

<details>
<summary>해설 보기</summary>

대칭 Hessian은 실수 정규직교 고유기저를 가지므로 고유값분해가 방향별 곡률을 해석하는 데 맞는다.

직사각행렬은 같은 공간의 벡터를 같은 공간으로 보내지 않으므로 보통의 고유값 식을 적용할 수 없다. SVD로 입력 방향, 증폭률과 출력 방향을 나눈다.

비대칭 정사각행렬에는 고유값을 정의할 수 있지만 실수 고유벡터가 충분하지 않거나 직교하지 않을 수 있다. 연구 질문이 반복 동역학이면 고유값을 볼 수 있고, 안정적인 방향별 증폭과 저랭크 구조가 목적이면 SVD가 더 적합할 수 있다.

</details>

## 단원 요약

- 고유벡터는 선형변환 뒤 같은 직선 위에 남는 0이 아닌 벡터이고 고유값은 그 배율이다.
- 고유값은 $\det(\mathbf A-\lambda\mathbf I)=0$에서 찾고 고유공간은 $\ker(\mathbf A-\lambda\mathbf I)$다.
- 행렬을 반복 적용하면 고유방향 성분에 고유값의 거듭제곱이 곱해진다.
- 독립 고유벡터가 공간의 기저를 이루면 행렬을 대각화할 수 있다.
- 실수 정사각행렬도 실수 고유벡터가 없거나 대각화되지 않을 수 있다.
- 고유값은 변환의 방향별 구조이며 feature 의미나 인과적 중요도를 직접 보여 주지 않는다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- 고유값과 고유벡터를 식과 말로 정의할 수 있는가?
- $2\times2$ 특성방정식에서 고유값을 구할 수 있는가?
- 각 고유값의 고유공간 기저를 구할 수 있는가?
- 반복 적용에서 고유값이 거듭제곱되는 이유를 설명할 수 있는가?
- 대각화에 필요한 독립 고유벡터 수를 판단할 수 있는가?
- 고유값분해와 SVD의 적용 대상을 구분할 수 있는가?

## 다음 단원

- [M02-12 대칭행렬과 스펙트럼 정리](M02-12-symmetric-matrices-spectral-theorem.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] 고유쌍, 특성방정식과 고유공간을 정의했다.
- [x] 부호·크기와 반복 적용을 연결했다.
- [x] 대각화 조건과 실패 사례를 포함했다.
- [x] 정사각행렬과 직사각행렬의 분석법을 구분했다.
- [x] 모든 문제에 해설이 있다.
- [x] 고유값과 모델 feature 주장의 범위를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 내부 링크와 수식 구분자를 확인했다.
