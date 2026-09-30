---
id: "M03-07"
title: "쌍대공간과 covector"
part: 1
stage: "M03"
status: "완료"
prerequisites:
  - "M03-02"
  - "M03-03"
  - "M01-11"
estimated_time: "125~150분"
---

# M03-07. 쌍대공간과 covector

## 이 단원이 필요한 이유

벡터는 방향을 가진 변화량을 나타낼 수 있다. covector는 벡터를 입력받아 scalar를 내놓는 선형함수다. 미분에서 differential은 입력 변화벡터를 함수값의 일차 변화량으로 보낸다. gradient는 내적을 사용해 그 covector를 벡터로 나타낸 결과다.

Euclidean 좌표에서는 differential과 gradient가 같은 숫자 목록으로 보이기 때문에 둘을 섞기 쉽다. 기저나 내적을 바꾸면 벡터와 covector의 좌표변환 법칙이 달라지고, 같은 differential에 대응하는 gradient도 달라질 수 있다. 이 구분은 Jacobian, VJP와 역전파를 읽는 데 필요하다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- covector를 벡터공간에서 실수로 가는 선형사상으로 정의할 수 있다.
- 쌍대공간과 dual basis를 작은 예제에서 구성할 수 있다.
- covector가 벡터에 작용해 scalar를 만드는 계산을 수행할 수 있다.
- 기저변환 아래 벡터 좌표와 covector 좌표가 반대 방식으로 변하는 이유를 설명할 수 있다.
- differential과 gradient를 내적을 사용해 연결할 수 있다.
- 선형 probe의 가중치와 표현 방향을 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [M03-02 선형사상과 행렬 표현](M03-02-linear-maps-matrix-representation.md)
- 선수 단원: [M03-03 기저변환과 좌표 의존성](M03-03-change-of-basis-coordinate-dependence.md)
- 선수 단원: [M01-11 방향미분과 gradient](../M01/M01-11-directional-derivative-gradient.md)
- 확인 질문: 선형사상의 입력과 출력 공간을 구분할 수 있는가?
- 확인 질문: 좌표변환행렬의 방향을 아래첨자로 읽을 수 있는가?
- 확인 질문: 방향미분을 gradient와 방향벡터의 내적으로 계산할 수 있는가?

선형사상이나 기저변환이 불분명하면 선수 단원을 먼저 복습한다.

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | 타입 |
|---|---|---|---|
| $V^*$ | `V star` | $V$ 위의 모든 covector가 이루는 쌍대공간 | 벡터공간 |
| $\varphi:V\to\mathbb R$ | `phi maps V to R` | 벡터를 scalar로 보내는 선형함수 | covector |
| $\mathcal B=(\mathbf b_1,\ldots,\mathbf b_n)$ | `the basis B consisting of b one through b n` | $V$의 순서 있는 기저 | basis |
| $\mathcal B^*=(\beta^1,\ldots,\beta^n)$ | `the dual basis B star` | $\beta^i(\mathbf b_j)=\delta_{ij}$를 만족하는 기저 | $V^*$의 basis |
| $\boldsymbol\omega^\top$ | `omega transpose` | covector의 좌표 행 | $1\times n$ |
| $df_{\mathbf x}$ | `d f at x` | 변화벡터를 함수값의 일차 변화로 보내는 differential | covector |
| $\nabla f(\mathbf x)$ | `the gradient of f at x` | 선택한 내적 아래 $df_{\mathbf x}$에 대응하는 벡터 | vector |

## 핵심 개념 1. covector는 벡터를 측정하는 선형함수다

벡터공간 $V$ 위의 covector $\varphi$는

\[
\varphi:V\to\mathbb R
\]

인 선형사상이다. 모든 $\mathbf u,\mathbf v\in V$와 $\alpha,\beta\in\mathbb R$에 대해

\[
\varphi(\alpha\mathbf u+\beta\mathbf v)
=
\alpha\varphi(\mathbf u)+\beta\varphi(\mathbf v)
\]

를 만족한다.

$V=\mathbb R^n$에 표준좌표를 사용하면 covector는 행벡터로 나타낼 수 있다.

\[
\varphi(\mathbf v)
=
\boldsymbol\omega^\top\mathbf v
\]

shape은

\[
\underbrace{\boldsymbol\omega^\top}_{1\times n}
\underbrace{\mathbf v}_{n\times1}
\in\mathbb R
\]

이다. 행벡터 $\boldsymbol\omega^\top$은 선택한 기저에서의 좌표 표현이며 covector 자체는 선형함수다.

## 핵심 개념 2. 모든 covector가 이루는 집합도 벡터공간이다

$V$ 위의 모든 covector를 모아

\[
V^*
=
\{\varphi:V\to\mathbb R\mid\varphi\text{는 선형이다}\}
\]

로 쓰고 $V$의 쌍대공간(dual space)이라고 한다.

두 covector의 합과 스칼라곱은 점별로 정의한다.

\[
(\varphi+\psi)(\mathbf v)
=
\varphi(\mathbf v)+\psi(\mathbf v)
\]

\[
(\alpha\varphi)(\mathbf v)
=
\alpha\varphi(\mathbf v)
\]

$V$가 유한차원이라면

\[
\dim V^*=\dim V
\]

이다. 차원이 같다는 사실만으로 $V$와 $V^*$를 같은 공간으로 취급할 수는 없다. 벡터는 $V$의 원소이고 covector는 $V$에서 scalar로 가는 함수다. 두 공간을 대응시키려면 기저나 내적 같은 추가 구조를 선택해야 한다.

## 핵심 개념 3. dual basis는 기저 계수를 하나씩 읽는다

$V$의 기저가

\[
\mathcal B=(\mathbf b_1,\ldots,\mathbf b_n)
\]

일 때 dual basis

\[
\mathcal B^*=(\beta^1,\ldots,\beta^n)
\]

는

\[
\beta^i(\mathbf b_j)=\delta_{ij}
\]

를 만족한다. $\delta_{ij}$는 $i=j$이면 1이고 다르면 0이다.

\[
\mathbf v
=
v^1\mathbf b_1+\cdots+v^n\mathbf b_n
\]

이면

\[
\beta^i(\mathbf v)=v^i
\]

다. $\beta^i$는 $\mathcal B$ 좌표의 $i$번째 값을 읽는다.

임의의 covector $\varphi\in V^*$도

\[
\varphi
=
\omega_1\beta^1+\cdots+\omega_n\beta^n
\]

로 유일하게 나타낼 수 있다. 이때

\[
\varphi(\mathbf v)
=
\sum_{i=1}^{n}\omega_i v^i
\]

이다.

## 핵심 개념 4. 벡터와 covector 좌표는 서로 반대로 변한다

두 기저 $\mathcal B,\mathcal C$ 사이에서 벡터 좌표가

\[
[\mathbf v]_{\mathcal C}
=
\mathbf P_{\mathcal C\leftarrow\mathcal B}
[\mathbf v]_{\mathcal B}
\]

로 변한다고 하자. covector의 두 좌표 행을

\[
\boldsymbol\omega_{\mathcal B}^\top,
\qquad
\boldsymbol\omega_{\mathcal C}^\top
\]

로 쓴다. 같은 scalar 값은 기저와 무관해야 하므로

\[
\boldsymbol\omega_{\mathcal B}^\top[\mathbf v]_{\mathcal B}
=
\boldsymbol\omega_{\mathcal C}^\top[\mathbf v]_{\mathcal C}
\]

이다. 벡터 좌표변환을 대입하면

\[
\boldsymbol\omega_{\mathcal B}^\top[\mathbf v]_{\mathcal B}
=
\boldsymbol\omega_{\mathcal C}^\top
\mathbf P_{\mathcal C\leftarrow\mathcal B}
[\mathbf v]_{\mathcal B}
\]

이므로

\[
\boldsymbol\omega_{\mathcal C}^\top
=
\boldsymbol\omega_{\mathcal B}^\top
\mathbf P_{\mathcal B\leftarrow\mathcal C}
\]

이다. 벡터 좌표가 $\mathbf P$로 변하면 covector의 행 좌표는 $\mathbf P^{-1}$로 변한다. 이 반대 변환 때문에 두 좌표의 곱인 scalar가 유지된다.

covector 계수를 열로 쓰면 같은 식은

\[
\boldsymbol\omega_{\mathcal C}
=
\mathbf P_{\mathcal C\leftarrow\mathcal B}^{-\top}
\boldsymbol\omega_{\mathcal B}
\]

가 된다.

## 핵심 개념 5. 내적은 covector를 gradient vector로 나타낸다

scalar 함수 $f:V\to\mathbb R$의 점 $\mathbf x$에서 differential

\[
df_{\mathbf x}:V\to\mathbb R
\]

은 변화벡터 $\mathbf v$를 일차 변화량으로 보낸다.

\[
df_{\mathbf x}(\mathbf v)
\]

는 $\mathbf v$ 방향의 방향미분이다. differential은 $\mathbf v$에 대해 선형이므로 covector다.

내적 $\langle\cdot,\cdot\rangle$을 고르면

\[
df_{\mathbf x}(\mathbf v)
=
\langle\nabla f(\mathbf x),\mathbf v\rangle
\]

를 모든 $\mathbf v$에서 만족하는 벡터 $\nabla f(\mathbf x)$가 하나 정해진다. 이 벡터가 선택한 내적에 대한 gradient다.

표준 Euclidean 내적에서는

\[
df_{\mathbf x}(\mathbf v)
=
\nabla f(\mathbf x)^\top\mathbf v
\]

이다. 내적을

\[
\langle\mathbf a,\mathbf b\rangle_{\mathbf G}
=
\mathbf a^\top\mathbf G\mathbf b
\]

로 바꾸고 $\mathbf G$가 대칭 양의 정부호라면, differential의 좌표 열을 $\boldsymbol\omega$라 할 때

\[
\boldsymbol\omega^\top\mathbf v
=
\nabla_{\mathbf G}f(\mathbf x)^\top
\mathbf G\mathbf v
\]

이므로

\[
\nabla_{\mathbf G}f(\mathbf x)
=
\mathbf G^{-1}\boldsymbol\omega
\]

다. differential은 같은 선형함수로 남지만 gradient vector는 내적 선택에 따라 달라진다.

## 예제 1. dual basis로 좌표 읽기

### 문제

$V=\mathbb R^2$에서

\[
\mathbf b_1=
\begin{bmatrix}1\\1\end{bmatrix},
\qquad
\mathbf b_2=
\begin{bmatrix}1\\-1\end{bmatrix}
\]

로 기저 $\mathcal B$를 만든다. dual basis $\beta^1,\beta^2$를 표준좌표의 행벡터로 구하라.

### 풀이

\[
\mathbf P_{\mathcal E\leftarrow\mathcal B}
=
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
\]

이다. dual basis의 행을 쌓은 행렬은 기저행렬의 역행렬이다.

\[
\mathbf P_{\mathcal E\leftarrow\mathcal B}^{-1}
=
\frac12
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
\]

따라서

\[
\beta^1(\mathbf v)
=
\frac12
\begin{bmatrix}
1&1
\end{bmatrix}
\mathbf v
\]

\[
\beta^2(\mathbf v)
=
\frac12
\begin{bmatrix}
1&-1
\end{bmatrix}
\mathbf v
\]

이다.

검산하면

\[
\beta^1(\mathbf b_1)=1,
\quad
\beta^1(\mathbf b_2)=0,
\quad
\beta^2(\mathbf b_1)=0,
\quad
\beta^2(\mathbf b_2)=1
\]

이다.

### 결과의 의미

$\beta^1$과 $\beta^2$는 각각 $\mathcal B$ 좌표의 첫째 계수와 둘째 계수를 읽는다.

## 예제 2. covector의 기저별 좌표

### 문제

표준좌표에서 covector가

\[
\varphi(\mathbf v)
=
\begin{bmatrix}
2&-1
\end{bmatrix}
[\mathbf v]_{\mathcal E}
\]

로 주어진다. 예제 1의 $\mathcal B$ 좌표에서 $\varphi$의 행 좌표를 구하라.

### 풀이

\[
[\mathbf v]_{\mathcal E}
=
\mathbf P_{\mathcal E\leftarrow\mathcal B}
[\mathbf v]_{\mathcal B}
\]

이므로

\[
\varphi(\mathbf v)
=
\begin{bmatrix}
2&-1
\end{bmatrix}
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
[\mathbf v]_{\mathcal B}
\]

이다. 행렬곱을 계산하면

\[
\begin{bmatrix}
2&-1
\end{bmatrix}
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
=
\begin{bmatrix}
1&3
\end{bmatrix}
\]

이므로

\[
\boldsymbol\omega_{\mathcal B}^\top
=
\begin{bmatrix}
1&3
\end{bmatrix}
\]

이다.

$[\mathbf v]_{\mathcal B}=(3,1)^\top$이면

\[
\varphi(\mathbf v)
=
\begin{bmatrix}
1&3
\end{bmatrix}
\begin{bmatrix}
3\\1
\end{bmatrix}
=
6
\]

이다. 같은 벡터의 표준좌표는 $(4,2)^\top$이고

\[
\begin{bmatrix}
2&-1
\end{bmatrix}
\begin{bmatrix}
4\\2
\end{bmatrix}
=
6
\]

으로 같은 scalar를 얻는다.

### 결과의 의미

벡터와 covector의 좌표는 모두 바뀌지만 covector가 벡터에 작용한 scalar는 유지된다.

## 예제 3. differential과 두 gradient

### 문제

\[
f(x,y)=x^2+3xy
\]

일 때 점 $\mathbf x=(1,2)^\top$에서 differential을 구하고, 변화벡터 $\mathbf v=(-1,2)^\top$에 적용하라. Euclidean 내적과

\[
\mathbf G=
\begin{bmatrix}
4&0\\
0&1
\end{bmatrix}
\]

가 정한 내적에서 gradient도 각각 구하라.

### 풀이

편미분은

\[
\frac{\partial f}{\partial x}=2x+3y,
\qquad
\frac{\partial f}{\partial y}=3x
\]

이다. $(1,2)$에서 differential의 행 좌표는

\[
\boldsymbol\omega^\top
=
\begin{bmatrix}
8&3
\end{bmatrix}
\]

이다. 따라서

\[
df_{\mathbf x}(\mathbf v)
=
\begin{bmatrix}
8&3
\end{bmatrix}
\begin{bmatrix}
-1\\2
\end{bmatrix}
=
-8+6
=
-2
\]

다.

Euclidean gradient는

\[
\nabla f(\mathbf x)
=
\begin{bmatrix}
8\\3
\end{bmatrix}
\]

이다. $\mathbf G$ 내적에 대한 gradient는

\[
\nabla_{\mathbf G}f(\mathbf x)
=
\mathbf G^{-1}\boldsymbol\omega
=
\begin{bmatrix}
\frac14&0\\
0&1
\end{bmatrix}
\begin{bmatrix}
8\\3
\end{bmatrix}
=
\begin{bmatrix}
2\\3
\end{bmatrix}
\]

이다.

두 gradient는 서로 다르지만

\[
\nabla f(\mathbf x)^\top\mathbf v=-2
\]

이고

\[
\nabla_{\mathbf G}f(\mathbf x)^\top
\mathbf G\mathbf v
=
\begin{bmatrix}
2&3
\end{bmatrix}
\begin{bmatrix}
-4\\2
\end{bmatrix}
=
-2
\]

로 같은 differential 값을 나타낸다.

### 결과의 의미

differential은 점에서의 일차 변화 규칙이다. gradient는 선택한 내적으로 그 규칙을 벡터로 표현한다.

## 예제 4. 선형 readout을 covector로 보기

activation $\mathbf h\in\mathbb R^d$에서 scalar score를

\[
s(\mathbf h)=\mathbf w^\top\mathbf h+b
\]

로 계산한다고 하자. bias를 제외한

\[
\mathbf h\longmapsto\mathbf w^\top\mathbf h
\]

는 covector다. $\mathbf w$를 “score 방향”이라고 부를 때는 Euclidean 내적으로 covector와 벡터를 대응시켰다는 가정이 들어간다.

선형 probe가 높은 정확도를 얻으면 activation에서 label 관련 정보를 이 covector로 복원할 수 있음을 보인다. 모델이 같은 covector를 내부 계산에 사용한다는 결론에는 개입이나 회로 증거가 더 필요하다.

## 흔한 오해

### 오해 1. covector는 벡터를 가로로 쓴 것이다

행벡터는 선택한 기저에서 covector를 나타내는 좌표다. covector 자체는 벡터를 scalar로 보내는 선형함수다.

### 오해 2. $V$와 $V^*$는 차원이 같으므로 같은 공간이다

두 공간의 원소 타입이 다르다. 내적이나 기저를 선택하면 둘 사이의 대응을 만들 수 있지만 그 선택을 생략해서는 안 된다.

### 오해 3. differential과 gradient는 언제나 같은 대상이다

differential은 covector다. gradient는 선택한 내적을 통해 differential에 대응시킨 벡터다.

### 오해 4. probe weight는 기저와 무관한 feature 방향이다

probe weight의 좌표는 activation 기저와 feature scaling에 의존한다. 방향으로 해석할 때 사용한 내적과 전처리도 함께 밝혀야 한다.

## 연습문제

### 1. covector 판정

$\varphi:\mathbb R^2\to\mathbb R$가

\[
\varphi(x,y)=3x-2y
\]

로 주어진다. 선형성을 확인하고 표준좌표의 행 표현을 적어라.

<details>
<summary>해설 보기</summary>

두 벡터 $\mathbf u,\mathbf v$와 scalar $\alpha,\beta$에 대해 각 좌표의 선형결합을 대입하면

\[
\varphi(\alpha\mathbf u+\beta\mathbf v)
=
\alpha\varphi(\mathbf u)+\beta\varphi(\mathbf v)
\]

가 성립한다. 행 표현은

\[
\boldsymbol\omega^\top=
\begin{bmatrix}
3&-2
\end{bmatrix}
\]

이다.

</details>

### 2. covector 작용 계산

\[
\boldsymbol\omega^\top=
\begin{bmatrix}
1&-3&2
\end{bmatrix},
\qquad
\mathbf v=
\begin{bmatrix}
2\\1\\-1
\end{bmatrix}
\]

일 때 $\boldsymbol\omega^\top\mathbf v$를 구하라.

<details>
<summary>해설 보기</summary>

\[
\boldsymbol\omega^\top\mathbf v
=
1\cdot2+(-3)\cdot1+2\cdot(-1)
=
-3
\]

이다. covector가 벡터에 작용한 결과는 scalar다.

</details>

### 3. 표준 dual basis

$\mathbb R^3$의 표준기저에 대한 dual basis $\varepsilon^1,\varepsilon^2,\varepsilon^3$가 벡터 $(a,b,c)^\top$에 어떻게 작용하는지 적어라.

<details>
<summary>해설 보기</summary>

\[
\varepsilon^1(a,b,c)^\top=a,
\qquad
\varepsilon^2(a,b,c)^\top=b,
\qquad
\varepsilon^3(a,b,c)^\top=c
\]

이다. 각 covector는 대응하는 표준좌표 하나를 읽는다.

</details>

### 4. 기저변환과 scalar 보존

벡터 좌표가 $\mathbf v_{\mathcal C}=\mathbf P\mathbf v_{\mathcal B}$로 변한다. $\boldsymbol\omega_{\mathcal C}^\top\mathbf v_{\mathcal C}=\boldsymbol\omega_{\mathcal B}^\top\mathbf v_{\mathcal B}$가 되도록 $\boldsymbol\omega_{\mathcal C}^\top$을 구하라.

<details>
<summary>해설 보기</summary>

\[
\boldsymbol\omega_{\mathcal C}^\top
\mathbf P\mathbf v_{\mathcal B}
=
\boldsymbol\omega_{\mathcal B}^\top\mathbf v_{\mathcal B}
\]

가 모든 $\mathbf v_{\mathcal B}$에서 성립해야 하므로

\[
\boldsymbol\omega_{\mathcal C}^\top\mathbf P
=
\boldsymbol\omega_{\mathcal B}^\top
\]

이다. 따라서

\[
\boldsymbol\omega_{\mathcal C}^\top
=
\boldsymbol\omega_{\mathcal B}^\top\mathbf P^{-1}
\]

이다.

</details>

### 5. differential 계산

\[
f(x,y)=x^2+y^2
\]

에서 $\mathbf x=(1,-2)^\top$일 때 $df_{\mathbf x}$의 행 좌표를 구하고 $\mathbf v=(3,1)^\top$에 적용하라.

<details>
<summary>해설 보기</summary>

편미분은 $2x$와 $2y$이므로

\[
df_{\mathbf x}
\longleftrightarrow
\begin{bmatrix}
2&-4
\end{bmatrix}
\]

이다. 따라서

\[
df_{\mathbf x}(\mathbf v)
=
\begin{bmatrix}
2&-4
\end{bmatrix}
\begin{bmatrix}
3\\1
\end{bmatrix}
=
2
\]

다.

</details>

### 6. metric에 따른 gradient

differential의 좌표 열이

\[
\boldsymbol\omega=
\begin{bmatrix}
6\\2
\end{bmatrix}
\]

이고

\[
\mathbf G=
\begin{bmatrix}
3&0\\
0&2
\end{bmatrix}
\]

일 때 $\mathbf G$ 내적에 대한 gradient를 구하라.

<details>
<summary>해설 보기</summary>

\[
\nabla_{\mathbf G}f
=
\mathbf G^{-1}\boldsymbol\omega
=
\begin{bmatrix}
\frac13&0\\
0&\frac12
\end{bmatrix}
\begin{bmatrix}
6\\2
\end{bmatrix}
=
\begin{bmatrix}
2\\1
\end{bmatrix}
\]

이다.

</details>

### 7. 모델 주장 비판

“probe weight와 activation 벡터가 모두 $\mathbb R^d$의 열이므로 같은 종류의 feature다”라는 문장을 비판하라.

<details>
<summary>해설 보기</summary>

activation은 표현공간의 벡터다. probe weight는 activation을 score로 보내는 covector의 좌표이며, Euclidean 내적을 선택할 때 열벡터와 대응시킬 수 있다. 두 배열의 shape이 같다는 사실만으로 타입과 변환 법칙이 같아지지 않는다.

</details>

## 단원 요약

- covector는 벡터를 scalar로 보내는 선형함수이고 모든 covector는 쌍대공간 $V^*$를 이룬다.
- dual basis는 원래 기저의 좌표 계수를 하나씩 읽는다.
- 벡터 좌표와 covector 좌표는 반대 변환 법칙을 따라 scalar 작용값을 보존한다.
- differential은 변화벡터를 일차 변화량으로 보내는 covector다.
- gradient는 선택한 내적을 사용해 differential을 벡터로 나타낸 결과다.
- 선형 readout 가중치를 방향으로 해석할 때 기저, scaling과 내적을 밝혀야 한다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- covector와 쌍대공간을 정의할 수 있는가?
- dual basis가 기저 좌표를 읽는 방식을 설명할 수 있는가?
- covector가 벡터에 작용하는 계산을 수행할 수 있는가?
- 기저변환 아래 covector 좌표의 변화를 유도할 수 있는가?
- differential과 gradient를 타입과 내적 기준으로 구분할 수 있는가?
- probe weight를 covector로 해석할 때 필요한 가정을 말할 수 있는가?

## 다음 단원

- [M03-08 bilinear form과 quadratic form](M03-08-bilinear-quadratic-forms.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] covector를 선형함수로 정의했다.
- [x] dual basis와 기저변환을 계산했다.
- [x] differential과 gradient의 타입을 구분했다.
- [x] metric에 따른 gradient 변화를 포함했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 구분자를 확인했다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
