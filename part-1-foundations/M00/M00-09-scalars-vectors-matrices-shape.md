---
id: "M00-09"
title: "스칼라·벡터·행렬의 shape"
part: 1
stage: "M00"
status: "완료"
prerequisites:
  - "M00-03"
  - "M00-06"
estimated_time: "105~125분"
---

# M00-09. 스칼라·벡터·행렬의 shape

## 이 단원이 필요한 이유

신경망 수식은 수 하나, 값의 목록과 직사각형 배열을 한 식에서 함께 사용한다. 기호의 shape을 확인하면 덧셈이 가능한지, 행렬곱의 안쪽 차원이 맞는지, 출력에 어떤 차원이 남는지 계산 전에 판단할 수 있다.

\[
\mathbf y=\mathbf W\mathbf x+\mathbf b
\]

이 식에서 $\mathbf x$의 길이, $\mathbf W$의 열 수와 $\mathbf b$의 길이는 서로 맞아야 한다. 논문이 shape을 생략해도 독자는 주변 정의에서 이를 복원해야 한다. 이 단원에서는 선형대수의 구조를 증명하기 전에 수학 객체의 종류와 shape 검산법부터 익힌다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- 스칼라, 벡터, 행렬과 다차원 배열을 표기와 shape으로 구분할 수 있다.
- $\mathbb R^n$과 $\mathbb R^{m\times n}$을 읽을 수 있다.
- 덧셈, 내적, 행렬·벡터 곱과 행렬곱의 shape 조건을 판단할 수 있다.
- $\mathbf y=\mathbf W\mathbf x+\mathbf b$의 각 객체에 맞는 shape을 정할 수 있다.
- batch와 token 축을 포함한 activation shape을 기호별로 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [M00-03 함수의 입력과 출력](M00-03-functions-input-output.md)
- 선수 단원: [M00-06 인덱스와 합 기호](M00-06-indices-summation.md)

다음 표기를 읽을 수 있는지 확인한다.

\[
x_i,\qquad a_{ij},\qquad \sum_{j=1}^{n}a_{ij}x_j
\]

$x_i$는 $i$번째 값이고, $a_{ij}$는 두 인덱스로 위치를 구분한다. 마지막 식은 $i$를 고정하고 $j$에 대해 항을 더한다.

## 기호와 용어

| 기호·용어 | 읽는 법 | 의미 | shape |
|---|---|---|---|
| $x\in\mathbb R$ | 엑스는 실수 | 스칼라 하나 | 스칼라, 축 없음 |
| $\mathbf x\in\mathbb R^n$ | 굵은 엑스는 엔차원 실수벡터 | 성분 $n$개인 벡터 | 이론에서 열벡터 $n\times1$ |
| $\mathbf A\in\mathbb R^{m\times n}$ | 굵은 에이는 엠 행 엔 열 실수행렬 | 행 $m$개, 열 $n$개인 행렬 | $m\times n$ |
| $a_{ij}$ | 에이 아래 아이 제이 | $\mathbf A$의 $i$행 $j$열 원소 | 스칼라 |
| $\mathbf A^\top$ | 에이 전치 | 행과 열을 바꾼 행렬 | $n\times m$ |
| $d$ | 디 | vector 또는 feature dimension | 양의 정수 |
| $B$ | 비 | batch size | 표본 수 |
| $T$ | 티 | token 또는 sequence 길이 | 위치 수 |

## 핵심 개념 1. 스칼라, 벡터와 행렬

### 스칼라

스칼라(scalar)는 수 하나다.

\[
x=3.5,\qquad \alpha=-2
\]

처럼 보통 이탤릭 소문자로 쓴다. loss 하나, 학습률과 확률 하나가 스칼라 예다.

### 벡터

벡터(vector)는 이 단원에서 순서가 있는 성분들을 열로 나타낸다.

\[
\mathbf x
=
\begin{bmatrix}
x_1\\
x_2\\
\vdots\\
x_n
\end{bmatrix}
\in\mathbb R^n
\]

$\mathbb R^n$은 실수 성분 $n$개로 이루어진 벡터들의 공간이다. $\mathbf x$의 dimension은 $n$이다. 열벡터로 펼치면 shape은 $n\times1$이지만, 벡터 표기에서는 $\mathbb R^n$으로 줄여 쓴다.

벡터는 굵은 소문자 $\mathbf x$로 쓴다. 성분 하나 $x_i$는 스칼라다.

### 행렬

행렬(matrix)은 원소를 행과 열로 배열한 대상이다.

\[
\mathbf A
=
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n}\\
a_{21} & a_{22} & \cdots & a_{2n}\\
\vdots & \vdots & \ddots & \vdots\\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
\in\mathbb R^{m\times n}
\]

$m$은 행 수, $n$은 열 수다. shape은 행을 먼저 적어

\[
m\times n
\]

이라고 한다. 원소 $a_{ij}$에서 $i$는 행, $j$는 열을 가리킨다.

## 핵심 개념 2. shape은 연산 가능 여부를 제한한다

### 덧셈

두 벡터를 더하려면 dimension이 같아야 한다.

\[
\mathbf x,\mathbf y\in\mathbb R^n
\quad\Rightarrow\quad
\mathbf x+\mathbf y\in\mathbb R^n
\]

행렬도 shape이 같아야 원소별로 더할 수 있다.

\[
\mathbf A,\mathbf B\in\mathbb R^{m\times n}
\quad\Rightarrow\quad
\mathbf A+\mathbf B\in\mathbb R^{m\times n}
\]

$2\times3$ 행렬과 $3\times2$ 행렬은 원소 수가 같아도 위치 구조가 다르므로 그대로 더할 수 없다.

### 스칼라곱

스칼라 $\alpha$를 벡터나 행렬의 각 원소에 곱하면 shape은 유지된다.

\[
\alpha\mathbf x\in\mathbb R^n
\]

\[
\alpha\mathbf A\in\mathbb R^{m\times n}
\]

### 벡터 내적

두 $n$차원 벡터의 내적은

\[
\mathbf x^\top\mathbf y
=
\sum_{i=1}^{n}x_i y_i
\]

이며 결과는 스칼라다.

\[
\mathbf x^\top\mathbf y\in\mathbb R
\]

shape으로 보면

\[
(1\times n)(n\times1)=1\times1
\]

이고, 결과를 스칼라로 해석한다.

## 핵심 개념 3. 행렬·벡터 곱에서는 안쪽 차원이 맞아야 한다

\[
\mathbf A\in\mathbb R^{m\times n},
\qquad
\mathbf x\in\mathbb R^n
\]

이면

\[
\mathbf y=\mathbf A\mathbf x
\]

를 계산할 수 있고

\[
\mathbf y\in\mathbb R^m
\]

이다.

shape만 적으면

\[
(m\times n)(n\times1)
\longrightarrow
(m\times1)
\]

이다. 가운데의 $n$이 같아야 하며 바깥의 $m$이 출력 dimension으로 남는다.

$i$번째 출력 성분은

\[
y_i
=
\sum_{j=1}^{n}a_{ij}x_j
\]

이다. 행렬의 $i$번째 행과 입력 벡터의 모든 성분을 곱해 더한다.

### 작은 계산

\[
\mathbf A=
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}
5\\
6
\end{bmatrix}
\]

이면

\[
\mathbf A\mathbf x
=
\begin{bmatrix}
1\cdot5+2\cdot6\\
3\cdot5+4\cdot6
\end{bmatrix}
=
\begin{bmatrix}
17\\
39
\end{bmatrix}
\]

이다.

## 핵심 개념 4. 행렬곱의 출력 shape

\[
\mathbf A\in\mathbb R^{m\times n},
\qquad
\mathbf B\in\mathbb R^{n\times p}
\]

이면

\[
\mathbf A\mathbf B\in\mathbb R^{m\times p}
\]

이다.

shape 계산은

\[
(m\times n)(n\times p)
\longrightarrow
(m\times p)
\]

로 읽는다. 첫 행렬의 열 수와 둘째 행렬의 행 수가 같아야 한다.

순서를 바꾸면

\[
\mathbf B\mathbf A
\]

의 안쪽 차원은 $p$와 $m$이다. $p=m$이 아닐 경우 곱 자체가 정의되지 않는다. 두 곱이 모두 정의되더라도 출력 shape과 값이 다를 수 있다.

행렬곱의 계산법과 선형변환 해석은 M02에서 자세히 다룬다. 이 단원에서는 연산 가능 여부와 출력 shape을 먼저 판단한다.

## 핵심 개념 5. 전치는 행과 열을 바꾼다

\[
\mathbf A\in\mathbb R^{m\times n}
\]

의 전치(transpose)는

\[
\mathbf A^\top\in\mathbb R^{n\times m}
\]

이다. 원소 관계는

\[
(\mathbf A^\top)_{ij}=a_{ji}
\]

로 나타낸다.

예를 들어

\[
\mathbf A=
\begin{bmatrix}
1&2&3\\
4&5&6
\end{bmatrix}
\]

이면

\[
\mathbf A^\top=
\begin{bmatrix}
1&4\\
2&5\\
3&6
\end{bmatrix}
\]

이다. $\mathbf A$의 shape은 $2\times3$, $\mathbf A^\top$의 shape은 $3\times2$다.

열벡터 $\mathbf x\in\mathbb R^n$의 전치 $\mathbf x^\top$는 $1\times n$인 행벡터다.

## 핵심 개념 6. 아핀 층의 shape

입력 dimension이 $d_{\mathrm{in}}$, 출력 dimension이 $d_{\mathrm{out}}$인 아핀 층(affine layer)을

\[
\mathbf y=\mathbf W\mathbf x+\mathbf b
\]

로 쓴다.

$\mathbf W$는 가중치 행렬(weight matrix)이고 $\mathbf b$는 편향 벡터(bias vector)다.

각 객체의 shape은 다음과 같다.

\[
\mathbf x\in\mathbb R^{d_{\mathrm{in}}}
\]

\[
\mathbf W\in
\mathbb R^{d_{\mathrm{out}}\times d_{\mathrm{in}}}
\]

\[
\mathbf b,\mathbf y\in
\mathbb R^{d_{\mathrm{out}}}
\]

$\mathbf W\mathbf x$에서 안쪽 차원 $d_{\mathrm{in}}$이 맞고, 결과는 $d_{\mathrm{out}}$차원 벡터다. 같은 dimension의 $\mathbf b$를 더하면 출력 $\mathbf y$를 얻는다.

### 수치 예제

\[
\mathbf W=
\begin{bmatrix}
1&0&-1\\
2&1&0
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}
3\\
4\\
5
\end{bmatrix},
\qquad
\mathbf b=
\begin{bmatrix}
1\\
-2
\end{bmatrix}
\]

이다. shape은

\[
\mathbf W:2\times3,\qquad
\mathbf x:3\times1,\qquad
\mathbf b:2\times1
\]

이다.

\[
\mathbf W\mathbf x
=
\begin{bmatrix}
1\cdot3+0\cdot4-1\cdot5\\
2\cdot3+1\cdot4+0\cdot5
\end{bmatrix}
=
\begin{bmatrix}
-2\\
10
\end{bmatrix}
\]

이므로

\[
\mathbf y
=
\mathbf W\mathbf x+\mathbf b
=
\begin{bmatrix}
-1\\
8
\end{bmatrix}
\]

이다.

## 핵심 개념 7. batch에서는 표본을 행으로 쌓기도 한다

이론에서 개별 벡터는 열벡터로 두었다. 코드와 데이터 행렬에서는 표본 하나를 행으로 쌓는 관례를 많이 사용한다.

\[
\mathbf X\in\mathbb R^{B\times d_{\mathrm{in}}}
\]

$B$는 batch size이고, 각 행이 한 표본의 전치 $\mathbf x_b^\top$다.

같은 가중치 행렬을 모든 행에 적용하면

\[
\mathbf Y
=
\mathbf X\mathbf W^\top
+
\mathbf 1\mathbf b^\top
\]

로 쓸 수 있다.

\[
\mathbf W^\top
\in
\mathbb R^{d_{\mathrm{in}}\times d_{\mathrm{out}}}
\]

이므로

\[
(B\times d_{\mathrm{in}})
(d_{\mathrm{in}}\times d_{\mathrm{out}})
\longrightarrow
(B\times d_{\mathrm{out}})
\]

이다.

$\mathbf 1\in\mathbb R^B$는 모든 성분이 $1$인 벡터다. $\mathbf 1\mathbf b^\top$은 편향 $\mathbf b^\top$를 $B$개 행에 반복한 $B\times d_{\mathrm{out}}$ 행렬을 만든다.

딥러닝 라이브러리는 브로드캐스팅(broadcasting)으로 같은 계산을 간단히 적는다. 수학식에서는 어떤 축으로 값을 반복하는지 shape으로 명시한다.

## 핵심 개념 8. activation은 축이 셋 이상일 수 있다

Transformer의 한 layer activation을

\[
\mathbf H^{(\ell)}
\in
\mathbb R^{B\times T\times d_{\mathrm{model}}}
\]

로 나타낼 수 있다.

- $B$: batch 안의 표본 수
- $T$: 각 표본의 token position 수
- $d_{\mathrm{model}}$: token 하나의 hidden dimension
- $\ell$: layer 인덱스

원소

\[
h^{(\ell)}_{b,t,i}
\]

는 $\ell$번째 layer에서 batch 항목 $b$, token 위치 $t$, feature $i$의 스칼라 activation이다.

구현에서는 축이 셋 이상인 배열을 텐서(tensor)라고 부른다. 추상적인 텐서의 정의는 M03에서 다룬다. 지금은 각 축이 무엇을 세는지와 축의 순서를 확인한다.

예를 들어

\[
B=2,\qquad T=4,\qquad d_{\mathrm{model}}=3
\]

이면 activation 원소 수는

\[
2\cdot4\cdot3=24
\]

개다.

## 예제 1. 객체 종류와 shape 구분

다음 세 대상을 분류하자.

\[
a=2
\]

\[
\mathbf x=
\begin{bmatrix}
1\\
0\\
-1
\end{bmatrix}
\]

\[
\mathbf A=
\begin{bmatrix}
1&2&3\\
4&5&6
\end{bmatrix}
\]

$a$는 스칼라다. $\mathbf x$는 dimension $3$인 벡터이며 열 표기에서 shape은 $3\times1$이다. $\mathbf A$는 행 $2$개, 열 $3$개인 행렬이므로 shape은 $2\times3$이다.

## 예제 2. 연산 가능 여부 판단

\[
\mathbf A\in\mathbb R^{4\times3},
\quad
\mathbf B\in\mathbb R^{3\times2},
\quad
\mathbf C\in\mathbb R^{4\times2}
\]

라고 하자.

\[
\mathbf A\mathbf B
\]

는 안쪽 차원 $3$이 같으므로 계산할 수 있고 shape은 $4\times2$다. 따라서

\[
\mathbf A\mathbf B+\mathbf C
\]

도 두 항의 shape이 $4\times2$로 같아서 계산할 수 있다.

반면 $\mathbf B\mathbf A$는

\[
(3\times2)(4\times3)
\]

에서 안쪽 차원 $2$와 $4$가 다르므로 정의되지 않는다.

## 예제 3. 잘못된 layer 식 찾기

입력 dimension이 $5$, 출력 dimension이 $2$라고 하자. 다음 shape을 사용하면

\[
\mathbf x\in\mathbb R^5,
\qquad
\mathbf W\in\mathbb R^{5\times2},
\qquad
\mathbf b\in\mathbb R^2
\]

식

\[
\mathbf W\mathbf x+\mathbf b
\]

를 계산할 수 없다.

\[
(5\times2)(5\times1)
\]

의 안쪽 차원 $2$와 $5$가 맞지 않기 때문이다. 열벡터 관례에서 weight shape을

\[
\mathbf W\in\mathbb R^{2\times5}
\]

로 바꾸면

\[
(2\times5)(5\times1)
\longrightarrow
(2\times1)
\]

이 되어 bias와 더할 수 있다.

## 흔한 오해

### 오해 1. 벡터의 dimension과 크기는 같은 말이다

dimension은 성분의 개수다. 벡터의 크기 또는 노름(norm)은 성분값으로 계산한 스칼라다. 두 개념은 M02에서 구분해 다룬다.

### 오해 2. $m\times n$에서 $m$은 열 수다

행렬 shape은 행 수를 먼저 쓴다. $m\times n$은 $m$행 $n$열이다.

### 오해 3. 원소 수가 같으면 두 행렬을 더할 수 있다

$2\times3$과 $3\times2$는 원소가 각각 $6$개지만 대응하는 행과 열 구조가 다르다. 행렬 덧셈에는 shape이 같아야 한다.

### 오해 4. 행렬곱은 원소별 곱이다

행렬곱은 행과 열 사이의 곱을 합한다. 딥러닝 라이브러리에서 원소별 곱과 행렬곱은 다른 연산자로 구현한다.

### 오해 5. 코드가 브로드캐스팅을 수행하면 수학적으로 shape가 같다고 볼 수 있다

Broadcasting은 특정 축으로 값을 반복하는 구현 규칙이다. 수학식에서는 반복 방식이나 all-ones vector를 적어 결과 shape을 명확히 해야 한다.

## 연습문제

### 1. 객체 분류

다음 대상이 스칼라, 벡터 또는 행렬 중 무엇인지 말하고 shape을 적어라.

\[
c=-1
\]

\[
\mathbf v=
\begin{bmatrix}
2\\
3\\
4\\
5
\end{bmatrix}
\]

\[
\mathbf M=
\begin{bmatrix}
1&0\\
0&1\\
1&1
\end{bmatrix}
\]

<details>
<summary>해설 보기</summary>

$c$는 스칼라다.

$\mathbf v$는 dimension $4$인 벡터이며 열 표기에서 shape은 $4\times1$이다.

$\mathbf M$은 행 $3$개, 열 $2$개인 행렬이므로 shape은 $3\times2$다.

</details>

### 2. 행렬 원소 읽기

\[
\mathbf A=
\begin{bmatrix}
2&4&6\\
1&3&5
\end{bmatrix}
\]

일 때 $a_{1,3}$과 $a_{2,1}$을 구하고 $\mathbf A$의 shape을 적어라.

<details>
<summary>해설 보기</summary>

$a_{1,3}$은 1행 3열의 원소이므로 $6$이다. $a_{2,1}$은 2행 1열의 원소이므로 $1$이다.

$\mathbf A$는 2행 3열이므로

\[
\mathbf A\in\mathbb R^{2\times3}
\]

이다.

</details>

### 3. 덧셈 가능 여부

\[
\mathbf A\in\mathbb R^{2\times4},
\qquad
\mathbf B\in\mathbb R^{2\times4},
\qquad
\mathbf C\in\mathbb R^{4\times2}
\]

일 때 $\mathbf A+\mathbf B$와 $\mathbf A+\mathbf C$의 계산 가능 여부를 판단하라.

<details>
<summary>해설 보기</summary>

$\mathbf A$와 $\mathbf B$는 shape이 $2\times4$로 같으므로 더할 수 있다. 결과 shape도 $2\times4$다.

$\mathbf A$와 $\mathbf C$는 각각 $2\times4$, $4\times2$이므로 shape이 다르다. 원소 수가 같아도 행과 열의 배치가 달라서 더할 수 없다.

</details>

### 4. 내적 계산

\[
\mathbf x=
\begin{bmatrix}
1\\
2\\
3
\end{bmatrix},
\qquad
\mathbf y=
\begin{bmatrix}
4\\
-1\\
2
\end{bmatrix}
\]

일 때 $\mathbf x^\top\mathbf y$를 계산하고 결과의 종류를 말하라.

<details>
<summary>해설 보기</summary>

\[
\mathbf x^\top\mathbf y
=
1\cdot4+2\cdot(-1)+3\cdot2
\]

\[
=4-2+6
=8
\]

이다. 두 벡터의 내적 결과는 스칼라다.

</details>

### 5. 행렬·벡터 곱

\[
\mathbf A=
\begin{bmatrix}
1&2&0\\
-1&0&3
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}
2\\
1\\
4
\end{bmatrix}
\]

일 때 $\mathbf A\mathbf x$를 계산하라.

<details>
<summary>해설 보기</summary>

$\mathbf A$는 $2\times3$, $\mathbf x$는 $3\times1$이므로 결과는 $2\times1$이다.

\[
\mathbf A\mathbf x
=
\begin{bmatrix}
1\cdot2+2\cdot1+0\cdot4\\
-1\cdot2+0\cdot1+3\cdot4
\end{bmatrix}
\]

\[
=
\begin{bmatrix}
4\\
10
\end{bmatrix}
\]

이다.

</details>

### 6. 행렬곱 shape

\[
\mathbf A\in\mathbb R^{5\times3},
\qquad
\mathbf B\in\mathbb R^{3\times7},
\qquad
\mathbf C\in\mathbb R^{4\times5}
\]

일 때 다음 곱의 계산 가능 여부와 가능한 경우 출력 shape을 적어라.

\[
\mathbf A\mathbf B,\qquad
\mathbf C\mathbf A,\qquad
\mathbf B\mathbf A
\]

<details>
<summary>해설 보기</summary>

\[
(5\times3)(3\times7)
\]

은 안쪽 차원이 같으므로 $\mathbf A\mathbf B$를 계산할 수 있고 결과 shape은 $5\times7$이다.

\[
(4\times5)(5\times3)
\]

도 안쪽 차원이 같으므로 $\mathbf C\mathbf A$를 계산할 수 있고 결과 shape은 $4\times3$이다.

\[
(3\times7)(5\times3)
\]

은 안쪽 차원 $7$과 $5$가 다르므로 $\mathbf B\mathbf A$를 계산할 수 없다.

</details>

### 7. 아핀 층 shape

입력 dimension이 $d_{\mathrm{in}}=6$, 출력 dimension이 $d_{\mathrm{out}}=4$다. 열벡터 식

\[
\mathbf y=\mathbf W\mathbf x+\mathbf b
\]

에서 $\mathbf x$, $\mathbf W$, $\mathbf b$, $\mathbf y$의 shape을 적어라.

<details>
<summary>해설 보기</summary>

\[
\mathbf x\in\mathbb R^6
\]

\[
\mathbf W\in\mathbb R^{4\times6}
\]

\[
\mathbf b\in\mathbb R^4
\]

\[
\mathbf y\in\mathbb R^4
\]

이다. 행렬·벡터 곱의 shape은

\[
(4\times6)(6\times1)
\longrightarrow
(4\times1)
\]

이며 bias와 출력의 dimension도 $4$다.

</details>

### 8. Transformer activation shape

\[
\mathbf H^{(\ell)}
\in
\mathbb R^{B\times T\times d_{\mathrm{model}}}
\]

이고 $B=8$, $T=128$, $d_{\mathrm{model}}=512$라고 하자.

1. $h^{(\ell)}_{3,10,20}$은 어떤 종류의 값인가?
2. activation 원소 수를 구하라.
3. $\ell$의 역할을 설명하라.

<details>
<summary>해설 보기</summary>

$h^{(\ell)}_{3,10,20}$은 특정 batch 항목, token 위치와 feature를 지정한 스칼라 activation이다.

원소 수는

\[
8\cdot128\cdot512=524{,}288
\]

개다.

$\ell$은 layer를 구분하는 인덱스다. $\mathbf H^{(\ell)}$의 위첨자 괄호는 거듭제곱이 아니라 layer 위치를 나타낸다.

</details>

## 단원 요약

- 스칼라는 값 하나, 벡터는 성분 $n$개, 행렬은 $m$행 $n$열의 대상이다.
- 행렬 shape은 행 수와 열 수의 순서로 $m\times n$이라고 쓴다.
- 덧셈에는 같은 shape이 필요하고, 행렬곱에는 안쪽 차원의 일치가 필요하다.
- 열벡터 관례에서 $\mathbf W\in\mathbb R^{d_{\mathrm{out}}\times d_{\mathrm{in}}}$이다.
- Transformer activation의 각 축은 batch, token과 feature처럼 서로 다른 대상을 센다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- 스칼라, 벡터와 행렬을 표기로 구분할 수 있는가?
- $m\times n$에서 행 수와 열 수를 찾을 수 있는가?
- 행렬곱의 가능 여부와 출력 shape을 계산할 수 있는가?
- 아핀 층의 입력·가중치·편향·출력 shape을 정할 수 있는가?
- $B\times T\times d_{\mathrm{model}}$의 각 축을 설명할 수 있는가?

## 다음 단원

다음 단원은 [M00-10 AI 수식 해독 연습](M00-10-ai-equation-reading.md)이다. 지금까지 배운 변수, 함수, 합, 로그와 shape을 사용해 손실함수 하나를 처음부터 끝까지 읽는다.

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] 모든 새 기호와 shape을 사용 전에 정의했다.
- [x] 열벡터와 batch 행렬 관례를 구분했다.
- [x] 행렬곱의 안쪽 차원을 검산했다.
- [x] 아핀 층 예제의 수치를 검산했다.
- [x] 모든 문제에 해설이 있다.
- [x] 구현의 브로드캐스팅과 수학적 표기를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 내부 링크와 수식 구분자를 확인했다.
