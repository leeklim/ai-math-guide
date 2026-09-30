---
id: "M03-08"
title: "bilinear form과 quadratic form"
part: 1
stage: "M03"
status: "완료"
prerequisites:
  - "M03-03"
  - "M03-07"
  - "M02-12"
estimated_time: "120~145분"
---

# M03-08. bilinear form과 quadratic form

## 이 단원이 필요한 이유

내적, attention score와 이차 근사는 벡터 두 개를 scalar로 보내거나 벡터 하나를 두 번 넣어 scalar를 만드는 식을 사용한다. 행렬식 $\mathbf x^\top\mathbf A\mathbf y$는 bilinear form을, $\mathbf x^\top\mathbf A\mathbf x$는 quadratic form을 좌표로 나타낸다.

같은 행렬이 선형사상과 bilinear form을 모두 표현할 수 있지만 기저변환 법칙은 다르다. 선형연산자의 행렬은 similarity transformation을 따르고, bilinear form의 행렬은 congruence transformation을 따른다. 행렬의 원소만 보고 대상의 타입을 정하면 이 차이를 놓친다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- bilinear map과 bilinear form의 두 입력별 선형성을 확인할 수 있다.
- 기저를 고른 bilinear form을 $\mathbf x^\top\mathbf A\mathbf y$로 계산할 수 있다.
- 대칭 bilinear form과 내적의 추가 조건을 구분할 수 있다.
- quadratic form에서 행렬의 대칭 부분만 기여함을 설명할 수 있다.
- 기저변환 아래 congruence transformation을 계산할 수 있다.
- attention score와 Hessian의 이차식에서 bilinear 구조의 범위를 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [M03-03 기저변환과 좌표 의존성](M03-03-change-of-basis-coordinate-dependence.md)
- 선수 단원: [M03-07 쌍대공간과 covector](M03-07-dual-spaces-covectors.md)
- 선수 단원: [M02-12 대칭행렬과 스펙트럼 정리](../M02/M02-12-symmetric-matrices-spectral-theorem.md)
- 확인 질문: 행렬의 quadratic form과 양의 준정부호를 설명할 수 있는가?
- 확인 질문: covector가 벡터를 scalar로 보내는 방식을 설명할 수 있는가?
- 확인 질문: 기저변환행렬의 방향을 읽을 수 있는가?

quadratic form이나 기저변환이 불분명하면 선수 단원을 먼저 복습한다.

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | 타입 |
|---|---|---|---|
| $B:V\times W\to\mathbb R$ | `B maps V cross W to R` | 각 입력에 대해 선형인 함수 | bilinear map |
| $B:V\times V\to\mathbb R$ | `B maps V cross V to R` | 같은 벡터공간의 두 벡터를 받는 bilinear map | bilinear form |
| $\mathbf A$ | `A` | 기저를 고른 bilinear form의 행렬 | $n\times n$ |
| $q:V\to\mathbb R$ | `q maps V to R` | $q(\mathbf x)=B(\mathbf x,\mathbf x)$인 함수 | quadratic form |
| $\mathbf A_{\mathrm{sym}}$ | `A sub sym` | $\frac12(\mathbf A+\mathbf A^\top)$ | 대칭 부분 |
| congruence transformation | `congruence transformation` | bilinear form의 기저별 행렬을 연결하는 변환 | $\mathbf P^\top\mathbf A\mathbf P$ |

## 핵심 개념 1. bilinear map은 각 입력에 대해 따로 선형이다

\[
B:V\times W\to\mathbb R
\]

가 bilinear라는 말은 한 입력을 고정했을 때 다른 입력에 대한 함수가 선형이라는 뜻이다.

첫 입력에 대해서는

\[
B(\alpha\mathbf u_1+\beta\mathbf u_2,\mathbf v)
=
\alpha B(\mathbf u_1,\mathbf v)
+
\beta B(\mathbf u_2,\mathbf v)
\]

이고 둘째 입력에 대해서는

\[
B(\mathbf u,\alpha\mathbf v_1+\beta\mathbf v_2)
=
\alpha B(\mathbf u,\mathbf v_1)
+
\beta B(\mathbf u,\mathbf v_2)
\]

다.

두 입력을 함께 같은 scalar로 늘리면

\[
B(\alpha\mathbf u,\alpha\mathbf v)
=
\alpha^2B(\mathbf u,\mathbf v)
\]

이다. 따라서 bilinear map은 두 입력을 묶은 하나의 벡터에 대한 선형함수와 다르다.

## 핵심 개념 2. 기저를 고르면 bilinear form은 행렬로 표현된다

$V$의 기저를 $\mathcal B=(\mathbf b_1,\ldots,\mathbf b_n)$라 하자. bilinear form $B:V\times V\to\mathbb R$의 행렬 성분을

\[
A_{ij}=B(\mathbf b_i,\mathbf b_j)
\]

로 정의한다. 그러면

\[
B(\mathbf x,\mathbf y)
=
[\mathbf x]_{\mathcal B}^\top
\mathbf A_{\mathcal B}
[\mathbf y]_{\mathcal B}
\]

이다.

shape은

\[
\underbrace{[\mathbf x]_{\mathcal B}^\top}_{1\times n}
\underbrace{\mathbf A_{\mathcal B}}_{n\times n}
\underbrace{[\mathbf y]_{\mathcal B}}_{n\times1}
\in\mathbb R
\]

이다.

행렬의 $j$번째 열은 $\mathbf y=\mathbf b_j$를 고정했을 때 생기는 covector의 좌표와 연결된다. bilinear form은 한 입력을 고정할 때마다 다른 입력에 작용하는 covector를 만든다.

## 핵심 개념 3. 대칭 bilinear form과 내적은 조건이 다르다

bilinear form이

\[
B(\mathbf x,\mathbf y)=B(\mathbf y,\mathbf x)
\]

를 만족하면 대칭이라고 한다. 기저 행렬에서는

\[
\mathbf A^\top=\mathbf A
\]

와 같다.

실수 벡터공간의 내적은 다음 조건을 만족하는 bilinear form이다.

1. 대칭성: $\langle\mathbf x,\mathbf y\rangle=\langle\mathbf y,\mathbf x\rangle$
2. 양의 정부호성: $\langle\mathbf x,\mathbf x\rangle>0$ for $\mathbf x\ne\mathbf 0$

bilinear form이라고 해서 내적인 것은 아니다. 대칭이 아니거나, 영벡터가 아닌 입력에서 $B(\mathbf x,\mathbf x)\le0$이 될 수 있다.

## 핵심 개념 4. quadratic form은 같은 벡터를 두 입력에 넣는다

bilinear form $B$에서

\[
q(\mathbf x)=B(\mathbf x,\mathbf x)
\]

로 정의한 함수를 quadratic form이라고 한다. 좌표에서는

\[
q(\mathbf x)
=
\mathbf x^\top\mathbf A\mathbf x
\]

이다.

quadratic form은 scalar 배에 대해

\[
q(\alpha\mathbf x)=\alpha^2q(\mathbf x)
\]

를 만족한다. 일반적으로

\[
q(\mathbf x+\mathbf y)
\ne
q(\mathbf x)+q(\mathbf y)
\]

이므로 선형함수가 아니다.

## 핵심 개념 5. quadratic form에는 대칭 부분만 기여한다

행렬을 대칭 부분과 반대칭 부분으로 나누자.

\[
\mathbf A
=
\underbrace{\frac12(\mathbf A+\mathbf A^\top)}_{\mathbf A_{\mathrm{sym}}}
+
\underbrace{\frac12(\mathbf A-\mathbf A^\top)}_{\mathbf A_{\mathrm{skew}}}
\]

반대칭 부분은 $\mathbf A_{\mathrm{skew}}^\top=-\mathbf A_{\mathrm{skew}}$를 만족한다. scalar

\[
s=\mathbf x^\top\mathbf A_{\mathrm{skew}}\mathbf x
\]

를 전치하면

\[
s
=
s^\top
=
\mathbf x^\top\mathbf A_{\mathrm{skew}}^\top\mathbf x
=
-\mathbf x^\top\mathbf A_{\mathrm{skew}}\mathbf x
=
-s
\]

이므로 $s=0$이다. 따라서

\[
\mathbf x^\top\mathbf A\mathbf x
=
\mathbf x^\top\mathbf A_{\mathrm{sym}}\mathbf x
\]

이다. 서로 다른 두 입력을 넣는 $\mathbf x^\top\mathbf A\mathbf y$에서는 반대칭 부분이 사라지지 않는다.

대칭 bilinear form에서는 quadratic form으로 원래 form을 복원할 수 있다.

\[
B(\mathbf x,\mathbf y)
=
\frac12
\left(
q(\mathbf x+\mathbf y)-q(\mathbf x)-q(\mathbf y)
\right)
\]

이 식을 polarization identity라고 한다.

## 핵심 개념 6. bilinear form의 행렬은 congruence로 변한다

두 기저 $\mathcal B,\mathcal C$가 있고

\[
[\mathbf x]_{\mathcal B}
=
\mathbf P_{\mathcal B\leftarrow\mathcal C}
[\mathbf x]_{\mathcal C}
\]

라 하자. 같은 식을 $\mathbf y$에도 적용하면

\[
B(\mathbf x,\mathbf y)
=
[\mathbf x]_{\mathcal C}^\top
\mathbf P_{\mathcal B\leftarrow\mathcal C}^\top
\mathbf A_{\mathcal B}
\mathbf P_{\mathcal B\leftarrow\mathcal C}
[\mathbf y]_{\mathcal C}
\]

이다. 따라서

\[
\mathbf A_{\mathcal C}
=
\mathbf P_{\mathcal B\leftarrow\mathcal C}^\top
\mathbf A_{\mathcal B}
\mathbf P_{\mathcal B\leftarrow\mathcal C}
\]

이다. 이를 congruence transformation이라고 한다.

선형연산자의 similarity transformation

\[
\mathbf P^{-1}\mathbf A\mathbf P
\]

와 모양이 다르다. bilinear form은 두 입력 좌표를 모두 바꾸므로 왼쪽에 전치행렬이 붙는다.

## 핵심 개념 7. attention score와 곡률에 bilinear 식이 나타난다

열벡터 입력 $\mathbf x,\mathbf y\in\mathbb R^d$에서

\[
\mathbf q=\mathbf W_Q\mathbf x,
\qquad
\mathbf k=\mathbf W_K\mathbf y
\]

라 하면 dot-product score는

\[
\mathbf q^\top\mathbf k
=
\mathbf x^\top
\mathbf W_Q^\top\mathbf W_K
\mathbf y
\]

이다. $\mathbf x$와 $\mathbf y$에 대해 bilinear다. score에 softmax를 적용하고 value를 가중합하는 전체 attention 연산은 bilinear가 아니다.

scalar 함수의 점 $\mathbf x$ 주변 이차 근사에는

\[
\frac12
\Delta\mathbf x^\top
\mathbf H_f(\mathbf x)
\Delta\mathbf x
\]

가 나타난다. Hessian이 정하는 quadratic form은 작은 변화 방향에 따른 이차 곡률을 나타낸다. Hessian의 정의와 계산은 M03-12에서 다룬다.

## 예제 1. bilinear form과 quadratic form 계산

### 문제

\[
\mathbf A=
\begin{bmatrix}
2&4\\
-2&3
\end{bmatrix},
\qquad
\mathbf x=
\begin{bmatrix}
1\\2
\end{bmatrix},
\qquad
\mathbf y=
\begin{bmatrix}
-1\\1
\end{bmatrix}
\]

일 때 $B(\mathbf x,\mathbf y)=\mathbf x^\top\mathbf A\mathbf y$, $B(\mathbf y,\mathbf x)$와 $q(\mathbf x)$를 계산하라.

### 풀이

\[
\mathbf A\mathbf y
=
\begin{bmatrix}
2\\5
\end{bmatrix}
\]

이므로

\[
B(\mathbf x,\mathbf y)
=
\begin{bmatrix}
1&2
\end{bmatrix}
\begin{bmatrix}
2\\5
\end{bmatrix}
=
12
\]

다.

\[
\mathbf A\mathbf x
=
\begin{bmatrix}
10\\4
\end{bmatrix}
\]

이므로

\[
B(\mathbf y,\mathbf x)
=
\begin{bmatrix}
-1&1
\end{bmatrix}
\begin{bmatrix}
10\\4
\end{bmatrix}
=
-6
\]

이다. 두 값이 다르므로 $B$는 대칭이 아니다.

\[
q(\mathbf x)
=
\mathbf x^\top\mathbf A\mathbf x
=
\begin{bmatrix}
1&2
\end{bmatrix}
\begin{bmatrix}
10\\4
\end{bmatrix}
=
18
\]

이다.

### 결과의 의미

같은 행렬도 두 입력의 순서를 바꾸면 다른 bilinear 값을 낼 수 있다. quadratic form은 한 벡터를 두 자리에 넣은 값이다.

## 예제 2. 대칭 부분만 남기기

예제 1의 행렬에서

\[
\mathbf A_{\mathrm{sym}}
=
\frac12
\left(
\begin{bmatrix}
2&4\\
-2&3
\end{bmatrix}
+
\begin{bmatrix}
2&-2\\
4&3
\end{bmatrix}
\right)
=
\begin{bmatrix}
2&1\\
1&3
\end{bmatrix}
\]

이다. 따라서

\[
\mathbf x^\top\mathbf A_{\mathrm{sym}}\mathbf x
=
\begin{bmatrix}
1&2
\end{bmatrix}
\begin{bmatrix}
4\\7
\end{bmatrix}
=
18
\]

로 원래 quadratic form과 같은 값을 얻는다.

반대칭 부분은

\[
\mathbf A_{\mathrm{skew}}
=
\begin{bmatrix}
0&3\\
-3&0
\end{bmatrix}
\]

이고

\[
\mathbf x^\top\mathbf A_{\mathrm{skew}}\mathbf x=0
\]

이다.

## 예제 3. 양의 정부호 bilinear form

\[
\mathbf G=
\begin{bmatrix}
2&1\\
1&2
\end{bmatrix}
\]

가 정하는

\[
\langle\mathbf x,\mathbf y\rangle_{\mathbf G}
=
\mathbf x^\top\mathbf G\mathbf y
\]

를 생각하자. $\mathbf G$는 대칭이다. $\mathbf x=(x_1,x_2)^\top$에 대해

\[
\mathbf x^\top\mathbf G\mathbf x
=
2x_1^2+2x_1x_2+2x_2^2
\]

이고

\[
2x_1^2+2x_1x_2+2x_2^2
=
x_1^2+x_2^2+(x_1+x_2)^2
\]

이다. $\mathbf x\ne\mathbf 0$이면 이 값은 양수다. 따라서 $B_{\mathbf G}$는 내적이다.

## 예제 4. attention score의 bilinear 행렬

\[
\mathbf W_Q=
\begin{bmatrix}
1&0\\
1&1
\end{bmatrix},
\qquad
\mathbf W_K=
\begin{bmatrix}
1&1\\
0&1
\end{bmatrix}
\]

이고

\[
\mathbf x=
\begin{bmatrix}
1\\2
\end{bmatrix},
\qquad
\mathbf y=
\begin{bmatrix}
3\\-1
\end{bmatrix}
\]

라 하자.

\[
\mathbf q=\mathbf W_Q\mathbf x=
\begin{bmatrix}
1\\3
\end{bmatrix},
\qquad
\mathbf k=\mathbf W_K\mathbf y=
\begin{bmatrix}
2\\-1
\end{bmatrix}
\]

이므로

\[
\mathbf q^\top\mathbf k=-1
\]

이다. 입력공간의 bilinear 행렬은

\[
\mathbf W_Q^\top\mathbf W_K
=
\begin{bmatrix}
1&2\\
0&1
\end{bmatrix}
\]

이고

\[
\mathbf x^\top
\mathbf W_Q^\top\mathbf W_K
\mathbf y
=
-1
\]

로 같은 score를 얻는다.

이 계산은 softmax 전 score 하나의 bilinear 구조만 설명한다. attention weight와 최종 출력에는 normalization과 value 가중합이 더 들어간다.

## 흔한 오해

### 오해 1. $\mathbf x^\top\mathbf A\mathbf y$는 두 입력을 함께 본 선형함수다

한 입력을 고정하면 다른 입력에 대해 선형이다. 두 입력을 함께 $\alpha$배하면 출력은 $\alpha^2$배가 된다.

### 오해 2. 대칭 bilinear form은 모두 내적이다

내적에는 양의 정부호성도 필요하다. 대칭행렬이 음의 고유값을 가지면 내적을 정의하지 못한다.

### 오해 3. quadratic form은 행렬의 모든 정보를 보존한다

quadratic form은 행렬의 대칭 부분만 사용한다. 반대칭 부분은 $\mathbf x^\top\mathbf A\mathbf x$에서 사라진다.

### 오해 4. bilinear form의 행렬도 similarity로 변한다

bilinear form은 두 입력 좌표를 함께 바꾸므로 congruence transformation을 따른다.

### 오해 5. attention 전체가 bilinear다

query-key dot product는 입력 쌍에 대해 bilinear로 쓸 수 있다. softmax와 이후 가중합까지 포함한 attention 함수는 비선형이다.

## 연습문제

### 1. bilinearity 확인

\[
B(\mathbf x,\mathbf y)=x_1y_1+2x_2y_1
\]

가 $\mathbb R^2\times\mathbb R^2$에서 bilinear인지 판정하라.

<details>
<summary>해설 보기</summary>

$\mathbf y$를 고정하면 $B(\mathbf x,\mathbf y)=y_1x_1+2y_1x_2$이므로 $\mathbf x$에 대해 선형이다. $\mathbf x$를 고정하면 $B(\mathbf x,\mathbf y)=(x_1+2x_2)y_1+0y_2$이므로 $\mathbf y$에 대해 선형이다. 따라서 bilinear다.

</details>

### 2. 행렬로 계산하기

\[
\mathbf A=
\begin{bmatrix}
1&2\\
3&0
\end{bmatrix},
\quad
\mathbf x=
\begin{bmatrix}2\\-1\end{bmatrix},
\quad
\mathbf y=
\begin{bmatrix}1\\4\end{bmatrix}
\]

일 때 $\mathbf x^\top\mathbf A\mathbf y$를 구하라.

<details>
<summary>해설 보기</summary>

\[
\mathbf A\mathbf y
=
\begin{bmatrix}
9\\3
\end{bmatrix}
\]

이므로

\[
\mathbf x^\top\mathbf A\mathbf y
=
\begin{bmatrix}
2&-1
\end{bmatrix}
\begin{bmatrix}
9\\3
\end{bmatrix}
=
15
\]

이다.

</details>

### 3. 대칭성 판정

\[
\mathbf A=
\begin{bmatrix}
2&-1\\
-1&4
\end{bmatrix}
\]

가 정하는 bilinear form이 대칭인지 판정하라.

<details>
<summary>해설 보기</summary>

$\mathbf A^\top=\mathbf A$이므로

\[
\mathbf x^\top\mathbf A\mathbf y
=
\mathbf y^\top\mathbf A\mathbf x
\]

가 모든 $\mathbf x,\mathbf y$에서 성립한다. 따라서 대칭 bilinear form이다.

</details>

### 4. 대칭 부분 구하기

\[
\mathbf A=
\begin{bmatrix}
1&5\\
-1&2
\end{bmatrix}
\]

의 대칭 부분을 구하라.

<details>
<summary>해설 보기</summary>

\[
\mathbf A_{\mathrm{sym}}
=
\frac12(\mathbf A+\mathbf A^\top)
=
\frac12
\begin{bmatrix}
2&4\\
4&4
\end{bmatrix}
=
\begin{bmatrix}
1&2\\
2&2
\end{bmatrix}
\]

이다. $\mathbf x^\top\mathbf A\mathbf x$는 이 대칭행렬로 계산해도 같다.

</details>

### 5. congruence transformation

\[
\mathbf A_{\mathcal B}
=
\begin{bmatrix}
2&0\\
0&1
\end{bmatrix},
\qquad
\mathbf P_{\mathcal B\leftarrow\mathcal C}
=
\begin{bmatrix}
1&1\\
0&1
\end{bmatrix}
\]

일 때 $\mathbf A_{\mathcal C}$를 구하라.

<details>
<summary>해설 보기</summary>

\[
\mathbf A_{\mathcal C}
=
\mathbf P^\top\mathbf A_{\mathcal B}\mathbf P
\]

이고

\[
\mathbf A_{\mathcal B}\mathbf P
=
\begin{bmatrix}
2&2\\
0&1
\end{bmatrix}
\]

이다. 따라서

\[
\mathbf A_{\mathcal C}
=
\begin{bmatrix}
1&0\\
1&1
\end{bmatrix}
\begin{bmatrix}
2&2\\
0&1
\end{bmatrix}
=
\begin{bmatrix}
2&2\\
2&3
\end{bmatrix}
\]

이다.

</details>

### 6. attention score 읽기

$\mathbf q=\mathbf W_Q\mathbf x$와 $\mathbf k=\mathbf W_K\mathbf y$일 때 $\mathbf q^\top\mathbf k$를 $\mathbf x^\top\mathbf A\mathbf y$ 꼴로 쓰고 $\mathbf A$를 밝혀라.

<details>
<summary>해설 보기</summary>

\[
\mathbf q^\top\mathbf k
=
(\mathbf W_Q\mathbf x)^\top
(\mathbf W_K\mathbf y)
=
\mathbf x^\top
\mathbf W_Q^\top\mathbf W_K
\mathbf y
\]

이다. 따라서

\[
\mathbf A=\mathbf W_Q^\top\mathbf W_K
\]

다.

</details>

### 7. 모델 주장 비판

“attention score가 bilinear form이므로 attention layer 전체는 선형이다”라는 문장을 비판하라.

<details>
<summary>해설 보기</summary>

query-key score는 두 입력을 각각 고정했을 때 선형인 bilinear 식이다. 두 입력을 함께 바꾸는 함수는 선형이 아니며, attention layer에는 score scaling, softmax와 value 가중합도 들어간다. score의 bilinear 구조만으로 전체 layer의 선형성을 결론 낼 수 없다.

</details>

## 단원 요약

- bilinear map은 두 입력 각각에 대해 선형이고 bilinear form은 같은 공간의 두 벡터를 받는다.
- 기저를 고르면 bilinear form은 $\mathbf x^\top\mathbf A\mathbf y$로 나타난다.
- 내적은 대칭성과 양의 정부호성을 갖는 bilinear form이다.
- quadratic form은 같은 벡터를 두 입력에 넣으며 행렬의 대칭 부분만 사용한다.
- bilinear form의 기저별 행렬은 congruence transformation으로 연결된다.
- attention의 query-key score와 Hessian의 이차식에 bilinear·quadratic 구조가 나타난다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- bilinear map의 두 선형성 조건을 쓸 수 있는가?
- 행렬 표현으로 bilinear form을 계산할 수 있는가?
- 대칭 bilinear form과 내적을 구분할 수 있는가?
- quadratic form에서 대칭 부분만 남는 이유를 설명할 수 있는가?
- congruence transformation을 계산할 수 있는가?
- attention score에서 bilinear 행렬을 찾을 수 있는가?
- bilinear score와 전체 비선형 layer를 구분할 수 있는가?

## 다음 단원

- [M03-09 tensor와 multilinear map](M03-09-tensors-multilinear-maps.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] bilinear map의 두 입력별 선형성을 정의했다.
- [x] 행렬 표현과 shape을 명시했다.
- [x] 대칭 부분과 quadratic form을 연결했다.
- [x] congruence와 similarity를 구분했다.
- [x] attention score와 전체 연산의 범위를 구분했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 내부 링크와 수식 구분자를 확인했다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
