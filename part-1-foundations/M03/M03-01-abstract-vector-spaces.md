---
id: "M03-01"
title: "추상 벡터공간"
part: 1
stage: "M03"
status: "완료"
prerequisites:
  - "M02-01"
  - "M02-02"
  - "M02-07"
estimated_time: "110~135분"
---

# M03-01. 추상 벡터공간

## 이 단원이 필요한 이유

지금까지 벡터는 주로 숫자를 세로로 쌓은 열벡터였다. 그러나 선형대수의 규칙은 숫자 배열에만 적용되지 않는다. 다항식, 함수, 행렬도 서로 더하고 실수를 곱할 수 있으며, 그 연산이 같은 법칙을 만족하면 벡터공간으로 다룰 수 있다.

이 관점은 모델의 파라미터, activation, 함수 자체를 구분할 때 필요하다. 파라미터는 유한차원 좌표로 저장되지만 모델 하나는 입력을 출력으로 보내는 함수이기도 하다. 두 대상을 모두 벡터라고 부를 수 있는 경우에도 어떤 공간의 원소인지 먼저 정해야 같은 덧셈과 같은 기저를 말하는지 판단할 수 있다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- 실수 벡터공간의 연산과 핵심 공리를 설명할 수 있다.
- 열벡터, 다항식, 함수와 행렬에서 영벡터와 스칼라곱을 찾을 수 있다.
- 주어진 집합이 벡터공간인지 덧셈과 스칼라곱의 닫힘으로 판정할 수 있다.
- 추상 벡터와 그 벡터의 좌표 열을 구분할 수 있다.
- 선형결합, 생성공간, 기저와 차원을 일반 벡터공간에 적용할 수 있다.

## 선수지식 확인

- 선수 단원: [M02-01 벡터와 벡터 연산](../M02/M02-01-vectors-vector-operations.md)
- 선수 단원: [M02-02 선형결합과 span](../M02/M02-02-linear-combinations-span.md)
- 선수 단원: [M02-07 선형독립, 기저와 차원](../M02/M02-07-linear-independence-basis-dimension.md)
- 확인 질문: 열벡터의 덧셈과 스칼라곱을 계산할 수 있는가?
- 확인 질문: 기저가 벡터를 유일한 계수로 나타내는 독립 생성집합인 이유를 설명할 수 있는가?

선형결합과 기저가 불분명하면 선수 단원을 먼저 복습한다.

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | 범위 |
|---|---|---|---|
| $V$ | `V` | 벡터들이 속한 집합 | 이 단원에서는 실수 벡터공간 |
| $\mathbf u,\mathbf v$ | `u and v` | $V$의 원소 | 배열일 필요가 없다. |
| $\alpha,\beta$ | `alpha and beta` | 벡터에 곱하는 scalar | $\alpha,\beta\in\mathbb R$ |
| $\mathbf 0_V$ | `the zero vector in V` | $V$에서 덧셈의 항등원 | 공간마다 모양이 다르다. |
| $\mathcal P_2$ | `calligraphic P sub two` | 차수가 2 이하인 실수계수 다항식의 공간 | $\{a+bt+ct^2:a,b,c\in\mathbb R\}$ |
| $[\,\mathbf v\,]_{\mathcal B}$ | `the coordinates of v in the basis B` | 기저 $\mathcal B$에 대한 계수 열 | $\mathbb R^n$의 열벡터 |

## 핵심 개념 1. 벡터는 공간이 정한 연산의 대상이다

추상 벡터공간에서 벡터는 화살표나 숫자 열로 정의되지 않는다. 집합 $V$에 다음 두 연산이 주어진다.

- 벡터 덧셈: $\mathbf u+\mathbf v\in V$
- 스칼라곱: $\alpha\mathbf v\in V$

여기서 scalar는 이 단원에서 실수다. 두 연산이 벡터공간 공리를 만족하면 $V$를 실수 벡터공간이라고 한다. 따라서 어떤 대상이 벡터인지는 대상의 외형보다 그 대상이 속한 공간과 연산으로 정해진다.

예를 들어 다항식 $p(t)=1+2t$와 $q(t)=t-t^2$를 더하면

\[
(p+q)(t)=1+3t-t^2
\]

이고, 실수 3을 곱하면

\[
(3p)(t)=3+6t
\]

이다. 결과가 다시 실수계수 다항식이므로 같은 공간 안에서 연산할 수 있다.

## 핵심 개념 2. 벡터공간 공리는 계산 규칙을 고정한다

모든 $\mathbf u,\mathbf v,\mathbf w\in V$와 $\alpha,\beta\in\mathbb R$에 대해 다음 법칙이 성립해야 한다.

1. 덧셈의 교환법칙: $\mathbf u+\mathbf v=\mathbf v+\mathbf u$
2. 덧셈의 결합법칙: $(\mathbf u+\mathbf v)+\mathbf w=\mathbf u+(\mathbf v+\mathbf w)$
3. 영벡터의 존재: $\mathbf v+\mathbf 0_V=\mathbf v$
4. 덧셈 역원의 존재: $\mathbf v+(-\mathbf v)=\mathbf 0_V$
5. 분배법칙: $\alpha(\mathbf u+\mathbf v)=\alpha\mathbf u+\alpha\mathbf v$
6. scalar 덧셈에 대한 분배법칙: $(\alpha+\beta)\mathbf v=\alpha\mathbf v+\beta\mathbf v$
7. 스칼라곱의 결합법칙: $\alpha(\beta\mathbf v)=(\alpha\beta)\mathbf v$
8. scalar 1의 작용: $1\mathbf v=\mathbf v$

덧셈과 스칼라곱은 $V$ 안에서 결과를 내야 한다. 이를 닫힘이라고 한다. 공리를 매번 전부 확인하기보다, 이미 알려진 벡터공간의 부분집합이라면 영벡터 포함 여부와 덧셈·스칼라곱의 닫힘을 먼저 검사하는 방법이 효율적이다.

## 핵심 개념 3. 영벡터의 모양은 공간마다 다르다

영벡터는 숫자 0 하나가 아니라 덧셈의 항등원이다.

| 공간 | 원소의 예 | 영벡터 |
|---|---|---|
| $\mathbb R^3$ | $(1,2,3)^\top$ | $(0,0,0)^\top$ |
| $\mathcal P_2$ | $1-2t+t^2$ | 영다항식 $0+0t+0t^2$ |
| 실수함수의 공간 | $f(t)=\sin t$ | 모든 입력에서 0인 함수 |
| $\mathbb R^{2\times2}$ | $2\times2$ 실수행렬 | $2\times2$ 영행렬 |

영함수와 영다항식은 값이 항상 0이지만 각각 함수공간과 다항식공간의 원소다. 같은 기호 0을 쓰더라도 소속 공간을 확인해야 한다.

## 핵심 개념 4. 익숙한 대수 개념은 대상의 종류와 무관하다

$\mathbf v_1,\ldots,\mathbf v_k\in V$의 선형결합은

\[
\alpha_1\mathbf v_1+\cdots+\alpha_k\mathbf v_k
\]

이다. 가능한 모든 선형결합의 집합이 생성공간이다. 이 정의에는 벡터의 성분이 등장하지 않는다.

벡터들이 선형독립이라는 말은

\[
\alpha_1\mathbf v_1+\cdots+\alpha_k\mathbf v_k=\mathbf 0_V
\]

을 만족하는 계수가 $\alpha_1=\cdots=\alpha_k=0$뿐이라는 뜻이다. $V$를 생성하면서 선형독립인 순서 있는 벡터 목록이 기저다.

예를 들어

\[
\mathcal B=(1,t,t^2)
\]

는 $\mathcal P_2$의 기저다. 모든 $p(t)=a+bt+ct^2$는

\[
p=a\cdot1+b\cdot t+c\cdot t^2
\]

로 유일하게 표현된다. 따라서 $\dim\mathcal P_2=3$이다.

## 핵심 개념 5. 벡터와 좌표 열은 같은 대상이 아니다

기저 $\mathcal B=(\mathbf b_1,\ldots,\mathbf b_n)$가 정해지면

\[
\mathbf v
=
c_1\mathbf b_1+\cdots+c_n\mathbf b_n
\]

의 계수를 모아

\[
[\mathbf v]_{\mathcal B}
=
\begin{bmatrix}
c_1\\
\vdots\\
c_n
\end{bmatrix}
\]

로 쓴다. $\mathbf v$는 원래 공간 $V$의 벡터이고, $[\mathbf v]_{\mathcal B}$는 $\mathbb R^n$의 열벡터다.

다항식

\[
p(t)=2-t+3t^2
\]

자체는 함수인 다항식이고, $\mathcal B=(1,t,t^2)$에 대한 좌표는

\[
[p]_{\mathcal B}
=
\begin{bmatrix}
2\\
-1\\
3
\end{bmatrix}
\]

이다. 기저를 바꾸면 좌표 열은 달라지지만 다항식 $p$는 달라지지 않는다.

## 예제 1. 부분집합이 벡터공간인지 판정하기

### 문제

\[
S=\{(x,y)^\top\in\mathbb R^2:x+y=0\}
\]

과

\[
A=\{(x,y)^\top\in\mathbb R^2:x+y=1\}
\]

이 각각 $\mathbb R^2$의 부분공간인지 판정하라.

### 풀이

$S$에는 $(0,0)^\top$이 들어 있다. $\mathbf u=(u_1,u_2)^\top$와 $\mathbf v=(v_1,v_2)^\top$가 $S$에 있으면

\[
u_1+u_2=0,
\qquad
v_1+v_2=0
\]

이다. 따라서

\[
(u_1+v_1)+(u_2+v_2)=0
\]

이므로 $\mathbf u+\mathbf v\in S$다. 또한 $\alpha\in\mathbb R$에 대해

\[
\alpha u_1+\alpha u_2=\alpha(u_1+u_2)=0
\]

이므로 $\alpha\mathbf u\in S$다. 따라서 $S$는 부분공간이다.

$A$에는 영벡터가 들어 있지 않다. 실제로 $0+0\ne1$이다. 그러므로 $A$는 부분공간이 아니다.

### 결과의 의미

$S$는 원점을 지나는 직선이고 $A$는 그 직선을 평행이동한 affine 집합이다. 둘 다 직선처럼 보이지만 벡터공간은 영벡터를 포함해야 한다.

## 예제 2. 다항식을 벡터처럼 계산하기

### 문제

$\mathcal P_2$에서

\[
p(t)=1+t,
\qquad
q(t)=2-t+t^2
\]

일 때 $2p-q$를 구하고, 기저 $\mathcal B=(1,t,t^2)$에 대한 좌표를 구하라.

### 풀이

\[
2p(t)-q(t)
=
2(1+t)-(2-t+t^2)
=
3t-t^2
\]

이다. 따라서

\[
[2p-q]_{\mathcal B}
=
\begin{bmatrix}
0\\
3\\
-1
\end{bmatrix}
\]

이다.

### 결과의 의미

함수의 덧셈과 스칼라곱을 사용했지만 계수 계산은 열벡터 계산과 같다. 기저가 추상 벡터를 숫자 좌표로 옮겼기 때문이다.

## 예제 3. 모델에서 서로 다른 벡터공간 구분하기

폭이 $d$인 층의 한 token activation은 보통 $\mathbf h\in\mathbb R^d$로 나타낸다. 같은 모델의 가중치행렬은 $\mathbf W\in\mathbb R^{m\times d}$에 속한다. 두 대상은 모두 벡터공간의 원소로 볼 수 있지만 서로 다른 공간에 속한다.

\[
\mathbf W\mathbf h\in\mathbb R^m
\]

은 정의되지만 $\mathbf W+\mathbf h$는 일반적으로 정의되지 않는다. 추상적으로 모두 벡터라는 사실만으로 서로 더할 수 있는 것은 아니다. 소속 공간과 연산의 입력 조건을 함께 확인해야 한다.

모델 함수 $f$와 $g$도 입력과 출력의 종류가 같다면 점별 덧셈

\[
(f+g)(\mathbf x)=f(\mathbf x)+g(\mathbf x)
\]

을 정의할 수 있다. 다만 특정 신경망 구조로 표현 가능한 함수들의 집합은 보통 이 덧셈에 닫혀 있다고 자동으로 결론 내릴 수 없다. 전체 함수공간과 특정 구조가 나타내는 함수족을 구분해야 한다.

## 흔한 오해

### 오해 1. 벡터는 화살표 또는 숫자 열이다

화살표와 숫자 열은 대표적인 벡터의 표현이다. 벡터공간 공리를 만족하는 다항식, 함수와 행렬도 벡터가 될 수 있다.

### 오해 2. 부분집합이 직선이나 평면이면 부분공간이다

원점을 지나지 않는 affine 직선이나 평면은 영벡터를 포함하지 않으므로 부분공간이 아니다.

### 오해 3. 모든 벡터는 서로 더할 수 있다

덧셈은 같은 벡터공간 안에서 정의된다. $\mathbb R^d$의 activation과 $\mathbb R^{m\times d}$의 가중치행렬은 서로 다른 공간의 원소다.

### 오해 4. 좌표 열이 바뀌면 벡터도 바뀐다

같은 벡터를 다른 기저로 표현하면 좌표가 바뀐다. 대상 자체와 그 대상의 좌표 표현을 구분해야 한다.

## 연습문제

### 1. 공리 읽기

\[
\alpha(\mathbf u+\mathbf v)=\alpha\mathbf u+\alpha\mathbf v
\]

를 한국어 문장으로 설명하라.

<details>
<summary>해설 보기</summary>

두 벡터를 먼저 더한 뒤 scalar $\alpha$를 곱한 결과는 각 벡터에 $\alpha$를 곱한 뒤 더한 결과와 같다. 스칼라곱이 벡터 덧셈에 대해 분배된다는 공리다.

</details>

### 2. 영벡터 찾기

$\mathcal P_3$, 실수함수의 공간, $\mathbb R^{2\times3}$에서 영벡터를 각각 설명하라.

<details>
<summary>해설 보기</summary>

$\mathcal P_3$에서는 모든 계수가 0인 영다항식이다. 함수공간에서는 모든 입력을 0으로 보내는 영함수다. $\mathbb R^{2\times3}$에서는 모든 원소가 0인 $2\times3$ 영행렬이다. 세 대상은 모양은 다르지만 각 공간의 덧셈 항등원이다.

</details>

### 3. 부분공간 판정

\[
S=\{(x,y,z)^\top\in\mathbb R^3:x-2y+z=0\}
\]

가 부분공간인지 판정하라.

<details>
<summary>해설 보기</summary>

영벡터는 식을 만족한다. $\mathbf u,\mathbf v\in S$이면 각 좌변이 0이므로 두 벡터를 더한 좌변도 0이다. $\alpha\mathbf u$의 좌변도 원래 좌변에 $\alpha$를 곱한 0이다. 영벡터 포함, 덧셈과 스칼라곱의 닫힘을 만족하므로 부분공간이다.

</details>

### 4. 벡터공간이 아닌 집합

\[
C=\{(x,y)^\top\in\mathbb R^2:x\ge0,\ y\ge0\}
\]

가 실수 벡터공간이 아닌 이유를 하나 제시하라.

<details>
<summary>해설 보기</summary>

$(1,1)^\top\in C$지만 scalar $-1$을 곱한 $(-1,-1)^\top$은 $C$에 없다. 실수 스칼라곱에 닫혀 있지 않으므로 실수 벡터공간이 아니다.

</details>

### 5. 다항식 좌표

$p(t)=4-2t+t^2$의 기저 $\mathcal B=(1,t,t^2)$에 대한 좌표를 구하라. 좌표와 $p$ 자체의 차이도 설명하라.

<details>
<summary>해설 보기</summary>

\[
[p]_{\mathcal B}
=
\begin{bmatrix}
4\\
-2\\
1
\end{bmatrix}
\]

이다. $p$는 입력 $t$를 값으로 보내는 다항식이고, 좌표는 선택한 기저에서 $p$를 조립하는 계수를 모은 열벡터다.

</details>

### 6. 기저와 차원

$\mathbb R^{2\times2}$에서 다음 네 행렬이 기저가 되는 이유를 설명하라.

\[
\mathbf E_{11}=
\begin{bmatrix}1&0\\0&0\end{bmatrix},
\quad
\mathbf E_{12}=
\begin{bmatrix}0&1\\0&0\end{bmatrix},
\quad
\mathbf E_{21}=
\begin{bmatrix}0&0\\1&0\end{bmatrix},
\quad
\mathbf E_{22}=
\begin{bmatrix}0&0\\0&1\end{bmatrix}
\]

<details>
<summary>해설 보기</summary>

임의의 $\mathbf A=\begin{bmatrix}a&b\\c&d\end{bmatrix}$는

\[
\mathbf A
=
a\mathbf E_{11}+b\mathbf E_{12}+c\mathbf E_{21}+d\mathbf E_{22}
\]

로 유일하게 표현된다. 따라서 네 행렬은 공간을 생성하고 선형독립이다. 그러므로 기저이며 $\dim\mathbb R^{2\times2}=4$다.

</details>

### 7. 모델 주장 비판

“activation과 가중치는 모두 벡터이므로 직접 더해서 하나의 표현으로 분석할 수 있다”는 문장을 비판하라.

<details>
<summary>해설 보기</summary>

activation과 가중치를 각각 어떤 공간의 원소로 보는지 먼저 밝혀야 한다. 보통 activation은 $\mathbb R^d$의 열벡터이고 가중치는 $\mathbb R^{m\times d}$의 행렬이므로 직접 덧셈이 정의되지 않는다. 임의로 펼치거나 사상한 뒤 더할 수는 있지만, 그때는 새 표현공간과 사상 규칙을 명시해야 한다.

</details>

## 단원 요약

- 벡터공간은 벡터 덧셈과 스칼라곱이 정해지고 공리를 만족하는 집합이다.
- 다항식, 함수와 행렬도 적절한 연산 아래 벡터공간의 원소가 된다.
- 부분공간은 영벡터를 포함하고 덧셈과 스칼라곱에 닫혀 있어야 한다.
- 선형결합, 생성공간, 선형독립, 기저와 차원은 성분 표현 없이 정의된다.
- 추상 벡터와 선택한 기저에서의 좌표 열은 서로 다른 대상이다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- 실수 벡터공간의 두 연산과 핵심 공리를 설명할 수 있는가?
- 함수공간과 행렬공간의 영벡터를 찾을 수 있는가?
- 부분집합이 부분공간인지 닫힘으로 판정할 수 있는가?
- 다항식의 기저와 좌표를 계산할 수 있는가?
- 추상 벡터와 좌표 열을 구분할 수 있는가?

## 다음 단원

- [M03-02 선형사상과 행렬 표현](M03-02-linear-maps-matrix-representation.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] 실수 벡터공간의 연산과 공리를 구분했다.
- [x] 다항식, 함수와 행렬의 예를 포함했다.
- [x] 추상 벡터와 좌표 열을 구분했다.
- [x] 예제 계산을 검산했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 구분자를 확인했다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
