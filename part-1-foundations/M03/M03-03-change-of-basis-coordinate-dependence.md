---
id: "M03-03"
title: "기저변환과 좌표 의존성"
part: 1
stage: "M03"
status: "완료"
prerequisites:
  - "M03-01"
  - "M03-02"
  - "M02-07"
estimated_time: "120~145분"
---

# M03-03. 기저변환과 좌표 의존성

## 이 단원이 필요한 이유

같은 벡터도 기저가 달라지면 다른 숫자 열로 표현된다. 같은 선형사상도 입력과 출력 기저가 달라지면 다른 행렬로 표현된다. 좌표값이나 행렬 원소를 분석할 때 이 의존성을 무시하면 표현 방식의 차이를 대상 자체의 차이로 오해할 수 있다.

모델 해석에서 neuron 하나는 구현이 정한 좌표축 하나다. 특정 neuron의 activation이 큰 현상은 그 좌표계에서는 명확한 사실이지만, 표현공간의 기저를 섞으면 같은 추상 벡터가 여러 좌표에 분산될 수 있다. 따라서 좌표에 의존하는 주장과 기저를 바꿔도 유지되는 주장을 구분해야 한다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- 같은 벡터의 두 기저 좌표를 좌표변환행렬로 바꿀 수 있다.
- 좌표변환행렬의 열과 아래첨자 방향을 설명할 수 있다.
- 같은 선형사상의 두 행렬 표현을 기저변환 공식으로 연결할 수 있다.
- similarity transformation 공식을 convention과 함께 유도할 수 있다.
- 좌표 의존적인 양과 기저변환 아래 유지되는 성질을 구분할 수 있다.
- 수동적 좌표변경과 벡터를 실제로 바꾸는 능동적 변환을 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [M03-01 추상 벡터공간](M03-01-abstract-vector-spaces.md)
- 선수 단원: [M03-02 선형사상과 행렬 표현](M03-02-linear-maps-matrix-representation.md)
- 선수 단원: [M02-07 선형독립, 기저와 차원](../M02/M02-07-linear-independence-basis-dimension.md)
- 확인 질문: 벡터와 그 벡터의 기저 좌표를 구분할 수 있는가?
- 확인 질문: 행렬 표현의 각 열이 정의역 기저벡터의 출력 좌표라는 사실을 설명할 수 있는가?

행렬 표현의 아래첨자가 불분명하면 M03-02를 먼저 복습한다.

## 기호와 용어

| 기호·용어 | 읽는 법 | 의미 | shape |
|---|---|---|---|
| $\mathcal B=(\mathbf b_1,\ldots,\mathbf b_n)$ | 기저 비 | $V$의 이전 기저 | 순서 있는 기저 |
| $\mathcal C=(\mathbf c_1,\ldots,\mathbf c_n)$ | 기저 시 | $V$의 새 기저 | 순서 있는 기저 |
| $\mathbf P_{\mathcal C\leftarrow\mathcal B}$ | 비 좌표에서 시 좌표로 가는 피 | $\mathcal B$ 좌표를 $\mathcal C$ 좌표로 바꾸는 행렬 | $n\times n$ |
| $[T]_{\mathcal B}$ | 기저 비에서의 티 행렬 | 정의역과 공역에 모두 $\mathcal B$를 쓴 표현 | $n\times n$ |
| similarity transformation | 유사변환 | 같은 선형연산자의 기저별 행렬을 연결하는 변환 | $\mathbf P^{-1}\mathbf A\mathbf P$ 꼴 |
| 좌표 의존성 | coordinate dependence | 기저 선택에 따라 수치 표현이 달라지는 성질 | 좌표값과 행렬 원소 등 |

## 핵심 개념 1. 좌표변환은 같은 벡터의 숫자 표현을 바꾼다

$V$의 두 기저를 $\mathcal B$와 $\mathcal C$라 하자. 좌표변환행렬

\[
\mathbf P_{\mathcal C\leftarrow\mathcal B}
\]

는 같은 벡터 $\mathbf v$의 $\mathcal B$ 좌표를 $\mathcal C$ 좌표로 바꾼다.

\[
[\mathbf v]_{\mathcal C}
=
\mathbf P_{\mathcal C\leftarrow\mathcal B}
[\mathbf v]_{\mathcal B}
\]

좌표변환은 벡터 $\mathbf v$ 자체를 바꾸지 않는다. $\mathbf v$를 기술하는 숫자 열만 바꾼다.

역방향 변환은 역행렬이다.

\[
\mathbf P_{\mathcal B\leftarrow\mathcal C}
=
\mathbf P_{\mathcal C\leftarrow\mathcal B}^{-1}
\]

\[
[\mathbf v]_{\mathcal B}
=
\mathbf P_{\mathcal B\leftarrow\mathcal C}
[\mathbf v]_{\mathcal C}
\]

두 기저가 모두 기저이므로 좌표변환행렬은 반드시 가역이다.

## 핵심 개념 2. 좌표변환행렬의 열은 출발 기저벡터의 도착 좌표다

항등사상 $\operatorname{Id}_V:V\to V$를 생각하면

\[
\mathbf P_{\mathcal C\leftarrow\mathcal B}
=
[\operatorname{Id}_V]_{\mathcal C\leftarrow\mathcal B}
\]

이다. M03-02의 행렬 표현 규칙에 따라

\[
\mathbf P_{\mathcal C\leftarrow\mathcal B}
=
\begin{bmatrix}
[\mathbf b_1]_{\mathcal C}
&
\cdots
&
[\mathbf b_n]_{\mathcal C}
\end{bmatrix}
\]

이다. 즉 각 열은 출발 기저 $\mathcal B$의 벡터를 도착 기저 $\mathcal C$로 나타낸 좌표다.

표준기저를 $\mathcal E$라 하면

\[
\mathbf P_{\mathcal E\leftarrow\mathcal B}
=
\begin{bmatrix}
\mathbf b_1&\cdots&\mathbf b_n
\end{bmatrix}
\]

로 쓸 수 있다. 이때 각 $\mathbf b_j$는 표준좌표 열이다.

## 핵심 개념 3. 같은 선형연산자의 행렬은 similarity로 연결된다

$T:V\to V$가 선형연산자이고, 정의역과 공역에 같은 기저를 사용한다고 하자. 같은 벡터에 대해

\[
[T(\mathbf v)]_{\mathcal C}
=
\mathbf P_{\mathcal C\leftarrow\mathcal B}
[T(\mathbf v)]_{\mathcal B}
\]

이다. 또한

\[
[T(\mathbf v)]_{\mathcal B}
=
[T]_{\mathcal B}[\mathbf v]_{\mathcal B}
\]

이고

\[
[\mathbf v]_{\mathcal B}
=
\mathbf P_{\mathcal B\leftarrow\mathcal C}
[\mathbf v]_{\mathcal C}
\]

이다. 세 식을 합치면

\[
[T(\mathbf v)]_{\mathcal C}
=
\mathbf P_{\mathcal C\leftarrow\mathcal B}
[T]_{\mathcal B}
\mathbf P_{\mathcal B\leftarrow\mathcal C}
[\mathbf v]_{\mathcal C}
\]

이므로

\[
[T]_{\mathcal C}
=
\mathbf P_{\mathcal C\leftarrow\mathcal B}
[T]_{\mathcal B}
\mathbf P_{\mathcal B\leftarrow\mathcal C}
\]

이다.

흔히 $\mathbf P=\mathbf P_{\mathcal B\leftarrow\mathcal C}$로 놓으면

\[
[T]_{\mathcal C}
=
\mathbf P^{-1}[T]_{\mathcal B}\mathbf P
\]

가 된다. $\mathbf P$가 어느 방향의 좌표변환인지 밝히지 않고 공식만 외우면 역행렬 위치를 바꾸기 쉽다.

## 핵심 개념 4. 모든 수치가 같은 방식으로 유지되지는 않는다

같은 벡터나 사상을 다른 기저로 표현할 때 다음을 구분해야 한다.

| 대상 | 일반적인 기저변환에서의 상태 |
|---|---|
| 벡터의 개별 좌표 | 달라진다. |
| 행렬의 개별 원소 | 달라진다. |
| 영벡터인지 여부 | 유지된다. |
| 선형독립 여부 | 유지된다. |
| 부분공간의 차원 | 유지된다. |
| 선형사상의 rank와 nullity | 유지된다. |
| 선형연산자의 determinant, trace와 고유값 | similarity 아래 유지된다. |
| 좌표의 Euclidean norm | 임의의 기저변환에서는 유지되지 않을 수 있다. |

길이와 각도를 보존하려면 내적을 함께 옮기거나 정규직교 기저 사이의 직교 좌표변환을 사용해야 한다. singular value도 일반적인 similarity transformation에서 자동으로 보존되는 양이 아니다. 어떤 변환군을 허용하는지에 따라 불변량이 달라진다.

## 핵심 개념 5. 수동적 좌표변경과 능동적 변환은 다르다

수동적 좌표변경에서는 추상 벡터 $\mathbf v$를 그대로 두고 좌표만

\[
[\mathbf v]_{\mathcal B}
\longrightarrow
[\mathbf v]_{\mathcal C}
\]

로 바꾼다.

능동적 변환에서는 기저를 고정하고 선형사상 $R$을 적용해 벡터 자체를

\[
\mathbf v
\longrightarrow
R(\mathbf v)
\]

로 바꾼다.

두 계산에 같은 모양의 행렬이 등장할 수 있지만 질문이 다르다. 좌표계를 바꿔 같은 대상을 다시 적는 것인지, 실제로 대상에 회전이나 투영을 적용한 것인지 확인해야 한다.

## 예제 1. 두 기저 사이에서 벡터 좌표 바꾸기

### 문제

$V=\mathbb R^2$에서 표준기저를 $\mathcal E$라 하고

\[
\mathcal B=
\left(
\begin{bmatrix}1\\1\end{bmatrix},
\begin{bmatrix}1\\-1\end{bmatrix}
\right)
\]

라 하자. $\mathbf v=(4,2)^\top$의 $\mathcal B$ 좌표를 구하라.

### 풀이

$\mathcal B$ 기저벡터를 표준좌표 열로 세우면

\[
\mathbf P_{\mathcal E\leftarrow\mathcal B}
=
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
\]

이다. 역행렬은

\[
\mathbf P_{\mathcal B\leftarrow\mathcal E}
=
\frac12
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
\]

이다. 따라서

\[
[\mathbf v]_{\mathcal B}
=
\mathbf P_{\mathcal B\leftarrow\mathcal E}
[\mathbf v]_{\mathcal E}
=
\frac12
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
\begin{bmatrix}
4\\
2
\end{bmatrix}
=
\begin{bmatrix}
3\\
1
\end{bmatrix}
\]

이다.

검산하면

\[
3
\begin{bmatrix}1\\1\end{bmatrix}
+
1
\begin{bmatrix}1\\-1\end{bmatrix}
=
\begin{bmatrix}4\\2\end{bmatrix}
\]

이다.

### 결과의 의미

표준좌표 $(4,2)^\top$과 $\mathcal B$ 좌표 $(3,1)^\top$은 같은 벡터를 나타낸다.

## 예제 2. 같은 선형연산자의 행렬 바꾸기

### 문제

표준기저에서 선형연산자 $T:\mathbb R^2\to\mathbb R^2$의 행렬이

\[
[T]_{\mathcal E}
=
\begin{bmatrix}
2&0\\
0&1
\end{bmatrix}
\]

이다. 예제 1의 기저 $\mathcal B$에서 $[T]_{\mathcal B}$를 구하라.

### 풀이

\[
[T]_{\mathcal B}
=
\mathbf P_{\mathcal B\leftarrow\mathcal E}
[T]_{\mathcal E}
\mathbf P_{\mathcal E\leftarrow\mathcal B}
\]

이므로

\[
[T]_{\mathcal B}
=
\frac12
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
\begin{bmatrix}
2&0\\
0&1
\end{bmatrix}
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
=
\begin{bmatrix}
\frac32&\frac12\\
\frac12&\frac32
\end{bmatrix}
\]

이다.

trace와 determinant를 비교하면

\[
\operatorname{tr}[T]_{\mathcal E}
=
\operatorname{tr}[T]_{\mathcal B}
=
3
\]

\[
\det[T]_{\mathcal E}
=
\det[T]_{\mathcal B}
=
2
\]

이다. 행렬 원소는 달라졌지만 같은 선형연산자를 표현하므로 similarity 불변량은 같다.

### 결과의 의미

표준기저에서는 두 좌표축이 각각 2배와 1배가 된다. $\mathcal B$에서는 같은 연산이 두 좌표를 섞는 행렬로 보인다. 대각행렬인지 여부조차 선택한 기저에 따라 달라질 수 있다.

## 예제 3. 모델 표현에서 좌표 의존성 읽기

한 층의 activation을 $\mathbf h\in\mathbb R^d$라 하고 가역행렬 $\mathbf P$로 새 좌표

\[
\widetilde{\mathbf h}
=
\mathbf P^{-1}\mathbf h
\]

를 정의하자. 이는 $\mathbf h$ 자체를 없애는 것이 아니라 같은 추상 표현벡터를 새 기저 좌표로 기록한 것으로 볼 수 있다.

선형 출력이

\[
\mathbf y=\mathbf W\mathbf h
\]

라면

\[
\mathbf h=\mathbf P\widetilde{\mathbf h}
\]

이므로

\[
\mathbf y
=
\mathbf W\mathbf P\widetilde{\mathbf h}
\]

이다. 새 좌표에서 입력 쪽 가중치 표현은 $\widetilde{\mathbf W}=\mathbf W\mathbf P$가 된다. activation 좌표만 바꾸고 가중치는 그대로 두면 일반적으로 같은 출력을 얻지 못한다.

이 계산은 선형 인터페이스에서의 좌표 재표현이다. 비선형함수가 중간에 있으면 임의의 기저혼합을 같은 방식으로 흡수할 수 있는지 별도로 확인해야 한다.

## 흔한 오해

### 오해 1. 기저를 바꾸면 벡터가 회전한다

수동적 기저변환에서는 벡터가 그대로이고 좌표만 바뀐다. 벡터 자체를 회전시키는 능동적 변환과 구분해야 한다.

### 오해 2. 좌표변환행렬은 기저벡터를 아무 방향으로나 열에 넣으면 된다

$\mathbf P_{\mathcal C\leftarrow\mathcal B}$의 열은 $[\mathbf b_j]_{\mathcal C}$다. 아래첨자의 출발과 도착 방향이 열의 의미를 정한다.

### 오해 3. 같은 선형사상이면 행렬 원소도 같다

행렬 원소는 기저에 의존한다. 같은 선형사상도 다른 기저에서는 다른 행렬로 나타난다.

### 오해 4. Euclidean norm은 어떤 기저에서도 같은 숫자다

정규직교 기저 사이의 좌표변환에서는 좌표의 Euclidean norm이 유지된다. 임의의 비직교 기저에서는 좌표 열의 Euclidean norm이 추상 벡터의 원래 길이와 같지 않을 수 있다.

## 연습문제

### 1. 행렬의 열 읽기

\[
\mathbf P_{\mathcal C\leftarrow\mathcal B}
=
\begin{bmatrix}
1&2\\
0&1
\end{bmatrix}
\]

일 때 두 열의 의미를 설명하라.

<details>
<summary>해설 보기</summary>

첫 열은 $\mathcal B$의 첫 기저벡터 $\mathbf b_1$을 $\mathcal C$ 좌표로 나타낸 $(1,0)^\top$이다. 둘째 열은 $\mathbf b_2$의 $\mathcal C$ 좌표인 $(2,1)^\top$이다.

</details>

### 2. 좌표 바꾸기

앞 문제에서 $[\mathbf v]_{\mathcal B}=(3,-1)^\top$일 때 $[\mathbf v]_{\mathcal C}$를 구하라.

<details>
<summary>해설 보기</summary>

\[
[\mathbf v]_{\mathcal C}
=
\begin{bmatrix}
1&2\\
0&1
\end{bmatrix}
\begin{bmatrix}
3\\
-1
\end{bmatrix}
=
\begin{bmatrix}
1\\
-1
\end{bmatrix}
\]

이다.

</details>

### 3. 역방향 좌표변환

\[
\mathbf P_{\mathcal C\leftarrow\mathcal B}
=
\begin{bmatrix}
1&2\\
0&1
\end{bmatrix}
\]

의 역행렬을 구하고 $[\mathbf v]_{\mathcal C}=(1,-1)^\top$을 $\mathcal B$ 좌표로 되돌려라.

<details>
<summary>해설 보기</summary>

\[
\mathbf P_{\mathcal B\leftarrow\mathcal C}
=
\begin{bmatrix}
1&-2\\
0&1
\end{bmatrix}
\]

이다. 따라서

\[
[\mathbf v]_{\mathcal B}
=
\begin{bmatrix}
1&-2\\
0&1
\end{bmatrix}
\begin{bmatrix}
1\\
-1
\end{bmatrix}
=
\begin{bmatrix}
3\\
-1
\end{bmatrix}
\]

이다.

</details>

### 4. similarity 계산

\[
\mathbf A_{\mathcal B}
=
\begin{bmatrix}
1&1\\
0&2
\end{bmatrix},
\qquad
\mathbf P_{\mathcal B\leftarrow\mathcal C}
=
\begin{bmatrix}
1&1\\
0&1
\end{bmatrix}
\]

일 때 $\mathbf A_{\mathcal C}=\mathbf P^{-1}\mathbf A_{\mathcal B}\mathbf P$를 구하라.

<details>
<summary>해설 보기</summary>

\[
\mathbf P^{-1}
=
\begin{bmatrix}
1&-1\\
0&1
\end{bmatrix}
\]

이고

\[
\mathbf A_{\mathcal B}\mathbf P
=
\begin{bmatrix}
1&2\\
0&2
\end{bmatrix}
\]

이다. 따라서

\[
\mathbf A_{\mathcal C}
=
\begin{bmatrix}
1&-1\\
0&1
\end{bmatrix}
\begin{bmatrix}
1&2\\
0&2
\end{bmatrix}
=
\begin{bmatrix}
1&0\\
0&2
\end{bmatrix}
\]

이다.

</details>

### 5. 불변량 확인

연습문제 4의 두 행렬에서 trace, determinant와 고유값을 비교하라.

<details>
<summary>해설 보기</summary>

두 행렬의 trace는 모두 3이고 determinant는 모두 2다. 두 행렬은 삼각행렬이므로 고유값은 대각 원소인 1과 2다. similarity transformation으로 연결된 같은 선형연산자의 표현이므로 이 값들이 일치한다.

</details>

### 6. 수동과 능동 구분

다음 두 문장을 수동적 좌표변경과 능동적 변환으로 분류하라.

1. 같은 지리적 위치를 동서·남북 좌표 대신 회전된 두 축의 좌표로 기록한다.
2. 좌표축은 고정하고 물체를 원점 주위로 30도 회전한다.

<details>
<summary>해설 보기</summary>

첫 문장은 대상의 위치를 유지하고 숫자 표현만 바꾸므로 수동적 좌표변경이다. 둘째 문장은 좌표축을 유지한 채 물체의 위치 자체를 바꾸므로 능동적 변환이다.

</details>

### 7. 모델 주장 비판

“한 neuron에 개념 정보가 집중되어 있으므로 그 개념은 어떤 기저에서도 한 좌표에 저장된다”는 결론을 비판하라.

<details>
<summary>해설 보기</summary>

neuron 하나는 구현 좌표계의 축 하나다. 가역적인 기저혼합을 적용하면 같은 추상 표현벡터의 정보가 여러 좌표에 분산될 수 있다. 원래 좌표에서 한 neuron이 예측이나 개입에 중요하다는 증거는 제시할 수 있지만, 한 좌표 집중이 모든 기저에서 유지된다는 결론은 따르지 않는다. 어떤 변환을 허용하며 모델 함수를 어떻게 보존하는지도 명시해야 한다.

</details>

## 단원 요약

- 좌표변환은 같은 벡터를 다른 기저의 숫자 열로 나타낸다.
- $\mathbf P_{\mathcal C\leftarrow\mathcal B}$의 열은 $\mathcal B$ 기저벡터의 $\mathcal C$ 좌표다.
- 같은 선형연산자의 두 행렬은 similarity transformation으로 연결된다.
- 행렬 원소와 벡터 좌표는 기저에 의존하지만 rank, 차원과 similarity 불변량은 유지된다.
- 좌표의 Euclidean norm은 임의의 기저변환에서 자동으로 보존되지 않는다.
- 수동적 좌표변경과 능동적 벡터변환은 서로 다른 질문이다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- 좌표변환행렬의 아래첨자와 각 열을 설명할 수 있는가?
- 한 벡터의 두 기저 좌표를 왕복 변환할 수 있는가?
- similarity transformation 공식을 좌표식에서 유도할 수 있는가?
- 같은 선형사상의 두 행렬 표현을 계산할 수 있는가?
- 좌표 의존적인 값과 유지되는 성질을 구분할 수 있는가?
- 수동적 좌표변경과 능동적 변환을 구분할 수 있는가?

## 다음 단원

- [M03-04 불변량과 equivariance 입문](M03-04-invariants-equivariance.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] 좌표변환 방향을 아래첨자로 명시했다.
- [x] similarity transformation을 convention과 함께 유도했다.
- [x] 수동적 좌표변경과 능동적 변환을 구분했다.
- [x] 좌표 의존량과 유지되는 성질을 구분했다.
- [x] 예제 계산을 검산했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 내부 링크와 수식 구분자를 확인했다.
