---
id: "M02-04"
title: "행렬과 행렬곱"
part: 1
stage: "M02"
status: "완료"
prerequisites:
  - "M00-09"
  - "M02-02"
  - "M02-03"
estimated_time: "110~135분"
---

# M02-04. 행렬과 행렬곱

## 이 단원이 필요한 이유

행렬은 여러 벡터 계산을 하나의 식으로 묶는다. 신경망의 가중치, token activation 묶음과 attention score는 행렬로 저장되며, forward pass의 대부분은 행렬곱으로 표현된다.

행렬곱은 대응 원소끼리 곱하는 연산이 아니다. 한 행과 한 열의 내적이며, 동시에 한 행렬의 열벡터를 선형결합하는 연산이다. 두 관점을 함께 익히면 shape 오류를 찾고 신경망 수식의 계산 경로를 읽을 수 있다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- 행렬의 행, 열, 원소와 shape을 표기로 읽을 수 있다.
- 행렬과 벡터의 곱을 행의 내적과 열의 선형결합으로 계산할 수 있다.
- 두 행렬의 곱이 정의되는 shape 조건과 출력 shape을 판단할 수 있다.
- 행렬곱의 원소 공식을 사용해 작은 곱을 계산할 수 있다.
- 행렬곱의 결합법칙, 항등행렬과 순서 의존성을 설명할 수 있다.
- 열벡터 관례와 행 단위 데이터 관례를 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [M00-09 스칼라·벡터·행렬의 shape](../M00/M00-09-scalars-vectors-matrices-shape.md)
- 선수 단원: [M02-02 선형결합과 span](M02-02-linear-combinations-span.md)
- 선수 단원: [M02-03 내적, 길이와 각도](M02-03-inner-product-length-angle.md)
- 확인 질문: 두 벡터의 내적과 여러 벡터의 선형결합을 계산할 수 있는가?
- 확인 질문: 행렬의 shape $(m,n)$에서 행과 열의 수를 말할 수 있는가?

내적, 선형결합이나 shape이 불분명하면 선수 단원을 먼저 복습한다.

## 기호와 용어

| 기호·용어 | 읽는 법 | 의미 | shape·범위 |
|---|---|---|---|
| $\mathbf A=[a_{ij}]$ | 행렬 에이 | $a_{ij}$를 원소로 갖는 행렬 | $\mathbf A\in\mathbb R^{m\times n}$ |
| $a_{ij}$ | 에이 아래 아이 제이 | $\mathbf A$의 $i$번째 행, $j$번째 열 원소 | scalar |
| $\mathbf A_{i:}$ | 에이의 아이 번째 행 | $i$번째 행벡터 | $1\times n$ |
| $\mathbf A_{:j}$ | 에이의 제이 번째 열 | $j$번째 열벡터 | $m\times1$ |
| $\mathbf I_n$ | 엔 차 항등행렬 | 대각 원소가 1이고 나머지가 0인 행렬 | $n\times n$ |
| $\mathbf C=\mathbf A\mathbf B$ | 에이 곱하기 비 | 행과 열의 내적으로 만든 행렬곱 | 안쪽 dimension이 같아야 한다. |

## 핵심 개념 1. 행렬은 행과 열을 가진 수의 배열이다

$m$개의 행과 $n$개의 열을 가진 행렬을

\[
\mathbf A
=
\begin{bmatrix}
a_{11}&a_{12}&\cdots&a_{1n}\\
a_{21}&a_{22}&\cdots&a_{2n}\\
\vdots&\vdots&\ddots&\vdots\\
a_{m1}&a_{m2}&\cdots&a_{mn}
\end{bmatrix}
\in\mathbb R^{m\times n}
\]

로 쓴다. 첫 첨자 $i$는 행, 둘째 첨자 $j$는 열을 가리킨다.

shape의 순서는 행 수 다음 열 수다. $\mathbb R^{2\times3}$ 행렬은 행이 2개이고 열이 3개이며 원소는 6개다.

## 핵심 개념 2. 행렬과 벡터의 곱은 행별 내적이다

$\mathbf A\in\mathbb R^{m\times n}$과 $\mathbf x\in\mathbb R^n$을 곱하면

\[
\mathbf y=\mathbf A\mathbf x\in\mathbb R^m
\]

이다. $i$번째 출력 성분은

\[
y_i
=
\sum_{j=1}^{n}a_{ij}x_j
\]

이다. $\mathbf A$의 $i$번째 행과 $\mathbf x$의 내적을 계산한 값이다.

입력의 dimension $n$은 행렬의 열 수와 같아야 한다. 출력 dimension은 행렬의 행 수 $m$이다.

## 핵심 개념 3. 같은 곱을 열벡터의 선형결합으로 볼 수 있다

$\mathbf A$의 열을 $\mathbf a_1,\ldots,\mathbf a_n\in\mathbb R^m$이라고 하면

\[
\mathbf A
=
\begin{bmatrix}
\mathbf a_1&\mathbf a_2&\cdots&\mathbf a_n
\end{bmatrix}
\]

이다. 이때

\[
\mathbf A\mathbf x
=
x_1\mathbf a_1+\cdots+x_n\mathbf a_n
\]

이다.

입력 성분 $x_j$가 $\mathbf A$의 $j$번째 열에 곱해지고, 모든 열을 더해 출력 벡터를 만든다. 따라서 $\mathbf A\mathbf x$는 $\mathbf A$의 열들이 만드는 span에 속한다.

## 핵심 개념 4. 행렬곱은 가운데 dimension을 합산한다

\[
\mathbf A\in\mathbb R^{m\times n},
\qquad
\mathbf B\in\mathbb R^{n\times p}
\]

이면

\[
\mathbf C=\mathbf A\mathbf B\in\mathbb R^{m\times p}
\]

이다. 왼쪽 행렬의 열 수 $n$과 오른쪽 행렬의 행 수 $n$이 같아야 한다.

출력 원소는

\[
c_{ij}
=
\sum_{k=1}^{n}a_{ik}b_{kj}
\]

이다. $\mathbf A$의 $i$번째 행과 $\mathbf B$의 $j$번째 열을 내적한다. $k$는 곱에서 합산되어 사라지는 안쪽 인덱스다.

## 핵심 개념 5. 행렬곱은 여러 행렬-벡터 곱을 묶는다

$\mathbf B$의 열을 $\mathbf b_1,\ldots,\mathbf b_p$라고 하면

\[
\mathbf A\mathbf B
=
\begin{bmatrix}
\mathbf A\mathbf b_1&
\mathbf A\mathbf b_2&
\cdots&
\mathbf A\mathbf b_p
\end{bmatrix}
\]

이다. 오른쪽 행렬의 각 열에 $\mathbf A$를 적용한 결과를 새 행렬의 열로 쌓는다.

반대로 $\mathbf A\mathbf B$의 각 열은 $\mathbf A$의 열들의 선형결합이다. 계수는 $\mathbf B$의 해당 열에서 온다.

## 핵심 개념 6. 행렬곱은 결합할 수 있지만 순서를 바꿀 수 없다

shape이 맞으면

\[
(\mathbf A\mathbf B)\mathbf C
=
\mathbf A(\mathbf B\mathbf C)
\]

이다. 행렬곱은 결합법칙을 만족한다.

일반적으로

\[
\mathbf A\mathbf B\ne\mathbf B\mathbf A
\]

이다. 한쪽 곱만 정의될 수도 있고, 두 곱이 모두 정의돼도 값이나 shape이 다를 수 있다. 신경망 계산에서 행렬의 순서는 연산 적용 순서를 정한다.

## 핵심 개념 7. 항등행렬은 벡터와 행렬을 바꾸지 않는다

$n\times n$ 항등행렬은

\[
\mathbf I_n
=
\begin{bmatrix}
1&0&\cdots&0\\
0&1&\cdots&0\\
\vdots&\vdots&\ddots&\vdots\\
0&0&\cdots&1
\end{bmatrix}
\]

이다.

\[
\mathbf I_n\mathbf x=\mathbf x
\]

이고, $\mathbf A\in\mathbb R^{m\times n}$에 대해

\[
\mathbf I_m\mathbf A=\mathbf A,
\qquad
\mathbf A\mathbf I_n=\mathbf A
\]

이다. 항등행렬의 크기는 곱의 위치에 맞춰야 한다.

## 핵심 개념 8. 행 단위 데이터에서는 전치가 들어간다

개별 입력을 열벡터로 두면

\[
\mathbf y=\mathbf W\mathbf x,
\qquad
\mathbf W\in\mathbb R^{d_{\mathrm{out}}\times d_{\mathrm{in}}}
\]

이다.

$N$개 입력의 전치를 행으로 쌓아

\[
\mathbf X
=
\begin{bmatrix}
\mathbf x_1^\top\\
\vdots\\
\mathbf x_N^\top
\end{bmatrix}
\in\mathbb R^{N\times d_{\mathrm{in}}}
\]

로 두면 같은 계산은

\[
\mathbf Y=\mathbf X\mathbf W^\top
\in\mathbb R^{N\times d_{\mathrm{out}}}
\]

가 된다. 벡터를 열로 쓰는 이론 관례와 표본을 행으로 쌓는 데이터 관례를 혼합하지 않아야 한다.

## 예제 1. 행렬-벡터 곱

\[
\mathbf A=
\begin{bmatrix}
1&2\\
-1&3
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}
4\\
5
\end{bmatrix}
\]

라고 하자. 행별 내적으로 계산하면

\[
\mathbf A\mathbf x
=
\begin{bmatrix}
1\cdot4+2\cdot5\\
-1\cdot4+3\cdot5
\end{bmatrix}
=
\begin{bmatrix}
14\\
11
\end{bmatrix}
\]

이다.

열의 선형결합으로 계산하면

\[
\mathbf A\mathbf x
=
4
\begin{bmatrix}1\\-1\end{bmatrix}
+
5
\begin{bmatrix}2\\3\end{bmatrix}
=
\begin{bmatrix}14\\11\end{bmatrix}
\]

로 같은 결과를 얻는다.

## 예제 2. 두 행렬의 곱

\[
\mathbf A=
\begin{bmatrix}
1&2&0\\
-1&3&1
\end{bmatrix},
\qquad
\mathbf B=
\begin{bmatrix}
2&1\\
0&4\\
5&-2
\end{bmatrix}
\]

라고 하자. shape은 각각 $2\times3$과 $3\times2$이므로 곱은 $2\times2$다.

\[
\mathbf A\mathbf B
=
\begin{bmatrix}
1\cdot2+2\cdot0+0\cdot5&
1\cdot1+2\cdot4+0(-2)\\
-1\cdot2+3\cdot0+1\cdot5&
-1\cdot1+3\cdot4+1(-2)
\end{bmatrix}
=
\begin{bmatrix}
2&9\\
3&9
\end{bmatrix}
\]

이다.

## 예제 3. 곱의 순서가 결과를 바꾼다

\[
\mathbf A=
\begin{bmatrix}
1&1\\
0&1
\end{bmatrix},
\qquad
\mathbf B=
\begin{bmatrix}
2&0\\
0&3
\end{bmatrix}
\]

이면

\[
\mathbf A\mathbf B
=
\begin{bmatrix}
2&3\\
0&3
\end{bmatrix}
\]

이고

\[
\mathbf B\mathbf A
=
\begin{bmatrix}
2&2\\
0&3
\end{bmatrix}
\]

이다. 두 행렬의 shape은 같지만 곱의 순서를 바꾸면 값이 달라진다.

## 예제 4. token 행렬에 선형 층 적용

$T$개 token activation을 행으로 쌓은

\[
\mathbf H\in\mathbb R^{T\times d_{\mathrm{in}}}
\]

과 가중치

\[
\mathbf W\in\mathbb R^{d_{\mathrm{out}}\times d_{\mathrm{in}}}
\]

가 있으면

\[
\mathbf Z=\mathbf H\mathbf W^\top
\in\mathbb R^{T\times d_{\mathrm{out}}}
\]

이다. $T$ 축은 유지되고 각 token의 feature dimension이 $d_{\mathrm{in}}$에서 $d_{\mathrm{out}}$으로 바뀐다.

shape 추적은 계산 가능성을 확인한다. 어떤 출력 좌표가 특정 개념을 나타내는지는 추가 분석이 필요하다.

## 흔한 오해

### 오해 1. 행렬곱은 같은 위치의 원소끼리 곱한다

행렬곱의 한 원소는 왼쪽 행과 오른쪽 열의 내적이다. 같은 위치의 원소만 곱하는 Hadamard 곱과 계산 규칙이 다르다.

### 오해 2. 두 행렬의 전체 원소 수가 같으면 곱할 수 있다

행렬곱은 왼쪽 열 수와 오른쪽 행 수가 같아야 한다. 전체 원소 수는 곱의 정의 조건이 아니다.

### 오해 3. $\mathbf A\mathbf B$가 정의되면 $\mathbf B\mathbf A$도 정의된다

두 곱의 안쪽 dimension 조건은 서로 다르다. 둘 다 정의되더라도 결과가 같다는 보장은 없다.

### 오해 4. shape이 맞으면 수식의 의미도 맞다

shape은 형식적인 계산 가능성을 검사한다. 행과 열이 무엇을 나타내는지, 같은 표본과 feature 순서를 사용하는지도 확인해야 한다.

## 연습문제

### 1. 행렬 원소와 shape

\[
\mathbf A=
\begin{bmatrix}
2&-1&4\\
0&3&5
\end{bmatrix}
\]

의 shape, $a_{12}$와 $a_{23}$을 구하라.

<details>
<summary>해설 보기</summary>

행이 2개이고 열이 3개이므로 $\mathbf A\in\mathbb R^{2\times3}$이다. 첫째 행 둘째 열은 $a_{12}=-1$, 둘째 행 셋째 열은 $a_{23}=5$다.

</details>

### 2. 행렬-벡터 곱

\[
\mathbf A=
\begin{bmatrix}
2&1\\
0&-1\\
3&2
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}4\\-2\end{bmatrix}
\]

일 때 $\mathbf A\mathbf x$를 구하라.

<details>
<summary>해설 보기</summary>

\[
\mathbf A\mathbf x
=
\begin{bmatrix}
2\cdot4+1(-2)\\
0\cdot4+(-1)(-2)\\
3\cdot4+2(-2)
\end{bmatrix}
=
\begin{bmatrix}6\\2\\8\end{bmatrix}
\]

이다. $3\times2$ 행렬에 dimension 2 벡터를 곱해 dimension 3 벡터를 얻는다.

</details>

### 3. 열의 선형결합

문제 2의 $\mathbf A\mathbf x$를 $\mathbf A$의 열벡터 두 개의 선형결합으로 다시 계산하라.

<details>
<summary>해설 보기</summary>

$\mathbf A$의 두 열은

\[
\mathbf a_1=
\begin{bmatrix}2\\0\\3\end{bmatrix},
\qquad
\mathbf a_2=
\begin{bmatrix}1\\-1\\2\end{bmatrix}
\]

이다. 따라서

\[
\mathbf A\mathbf x
=
4\mathbf a_1-2\mathbf a_2
=
\begin{bmatrix}8\\0\\12\end{bmatrix}
-
\begin{bmatrix}2\\-2\\4\end{bmatrix}
=
\begin{bmatrix}6\\2\\8\end{bmatrix}
\]

이다.

</details>

### 4. shape 판단

다음 행렬에 대해 각 곱이 정의되는지 판단하고, 정의되면 출력 shape을 구하라.

\[
\mathbf A\in\mathbb R^{3\times4},
\qquad
\mathbf B\in\mathbb R^{4\times2},
\qquad
\mathbf C\in\mathbb R^{3\times2}
\]

1. $\mathbf A\mathbf B$
2. $\mathbf B\mathbf A$
3. $\mathbf A^\top\mathbf C$

<details>
<summary>해설 보기</summary>

$\mathbf A\mathbf B$는 안쪽 dimension이 4로 같아 정의되며 shape은 $3\times2$다.

$\mathbf B\mathbf A$는 $4\times2$와 $3\times4$ 사이의 안쪽 dimension이 2와 3으로 달라 정의되지 않는다.

$\mathbf A^\top\in\mathbb R^{4\times3}$이므로 $\mathbf A^\top\mathbf C$는 정의되며 shape은 $4\times2$다.

</details>

### 5. 행렬곱 계산

\[
\mathbf A=
\begin{bmatrix}
1&2\\
3&0
\end{bmatrix},
\qquad
\mathbf B=
\begin{bmatrix}
-1&4\\
2&1
\end{bmatrix}
\]

일 때 $\mathbf A\mathbf B$를 구하라.

<details>
<summary>해설 보기</summary>

\[
\mathbf A\mathbf B
=
\begin{bmatrix}
1(-1)+2\cdot2&1\cdot4+2\cdot1\\
3(-1)+0\cdot2&3\cdot4+0\cdot1
\end{bmatrix}
=
\begin{bmatrix}
3&6\\
-3&12
\end{bmatrix}
\]

이다.

</details>

### 6. 순서 비교

문제 5의 두 행렬에 대해 $\mathbf B\mathbf A$도 계산하고 $\mathbf A\mathbf B$와 비교하라.

<details>
<summary>해설 보기</summary>

\[
\mathbf B\mathbf A
=
\begin{bmatrix}
-1\cdot1+4\cdot3&-1\cdot2+4\cdot0\\
2\cdot1+1\cdot3&2\cdot2+1\cdot0
\end{bmatrix}
=
\begin{bmatrix}
11&-2\\
5&4
\end{bmatrix}
\]

이다. $\mathbf A\mathbf B$와 값이 다르므로 이 두 행렬은 곱셈 순서를 바꿀 수 없다.

</details>

### 7. 데이터 행렬의 shape

$N=32$, $d_{\mathrm{in}}=128$, $d_{\mathrm{out}}=64$이고

\[
\mathbf X\in\mathbb R^{32\times128},
\qquad
\mathbf W\in\mathbb R^{64\times128}
\]

라고 하자.

1. $\mathbf X\mathbf W^\top$의 shape을 구하라.
2. 결과 행렬의 한 행이 무엇을 나타내는지 설명하라.
3. shape만으로 출력 좌표의 의미를 결정할 수 있는지 판단하라.

<details>
<summary>해설 보기</summary>

$\mathbf W^\top\in\mathbb R^{128\times64}$이므로

\[
\mathbf X\mathbf W^\top
\in
\mathbb R^{32\times64}
\]

이다. 각 행은 한 입력 표본의 128차원 벡터에 같은 선형 계산을 적용해 얻은 64차원 출력이다.

shape은 행이 표본이고 열이 출력 feature라는 구조를 알려 준다. 각 feature가 어떤 의미를 갖거나 모델 행동에 어떻게 관여하는지는 shape만으로 결정할 수 없다.

</details>

## 단원 요약

- $m\times n$ 행렬은 $m$개의 행과 $n$개의 열을 가지며 첫 첨자가 행을 가리킨다.
- 행렬-벡터 곱은 행별 내적이며 행렬 열의 선형결합으로도 읽을 수 있다.
- $\mathbf A\mathbf B$는 왼쪽 열 수와 오른쪽 행 수가 같을 때 정의된다.
- 행렬곱은 결합법칙을 만족하지만 곱셈 순서를 바꾸면 결과가 달라질 수 있다.
- 표본을 행으로 쌓으면 열벡터 식의 가중치에 전치를 붙여 같은 계산을 표현한다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- 행렬 원소 $a_{ij}$의 행과 열을 읽을 수 있는가?
- 행렬-벡터 곱을 두 관점으로 계산할 수 있는가?
- 행렬곱의 정의 조건과 출력 shape을 판단할 수 있는가?
- 작은 행렬곱의 원소를 직접 계산할 수 있는가?
- 결합법칙과 곱셈 순서의 차이를 설명할 수 있는가?
- 열벡터 관례와 행 단위 데이터 관례를 변환할 수 있는가?

## 다음 단원

- [M02-05 행렬을 선형변환으로 보기](M02-05-matrix-as-linear-transformation.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] 행, 열, 원소와 shape을 정의했다.
- [x] 행별 내적과 열의 선형결합을 모두 설명했다.
- [x] 행렬곱의 shape과 원소 공식을 제시했다.
- [x] 열벡터와 행 단위 데이터 관례를 구분했다.
- [x] 모든 문제에 해설이 있다.
- [x] shape과 의미 해석을 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 내부 링크와 수식 구분자를 확인했다.
