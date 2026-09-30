---
id: "M03-06"
title: "동치관계와 몫공간"
part: 1
stage: "M03"
status: "완료"
prerequisites:
  - "M03-01"
  - "M03-02"
  - "M03-05"
estimated_time: "120~145분"
---

# M03-06. 동치관계와 몫공간

## 이 단원이 필요한 이유

서로 다른 표현을 같은 대상으로 취급하려면 “같다”의 기준을 먼저 정해야 한다. 동치관계(equivalence relation)는 여러 원소를 겹치지 않는 동치류로 묶는다. 벡터공간에서는 지정한 부분공간 방향으로만 차이 나는 벡터들을 같은 동치류로 묶어 몫공간(quotient space)을 만든다.

모델 표현에서 특정 nuisance 방향을 무시하거나, 파라미터 대칭성 때문에 같은 함수를 나타내는 여러 파라미터를 하나로 묶는 생각에 이 구조가 등장한다. 어떤 차이를 버리는지 밝히지 않으면 몫공간이 보존하는 정보와 잃는 정보를 판단할 수 없다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- 반사성, 대칭성과 추이성으로 동치관계를 판정할 수 있다.
- 동치류와 대표원을 구분하고 동치류들이 집합을 분할하는 이유를 설명할 수 있다.
- 부분공간 $U$를 사용해 $\mathbf v\sim\mathbf w$를 정의하고 세 조건을 확인할 수 있다.
- 몫공간 $V/U$의 원소와 덧셈·스칼라곱을 계산할 수 있다.
- quotient map의 kernel과 몫공간의 차원을 구할 수 있다.
- quotient와 정사영, 파라미터 대칭성을 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [M03-01 추상 벡터공간](M03-01-abstract-vector-spaces.md)
- 선수 단원: [M03-02 선형사상과 행렬 표현](M03-02-linear-maps-matrix-representation.md)
- 선수 단원: [M03-05 부분공간, 직합과 분해](M03-05-subspaces-direct-sums-decomposition.md)
- 확인 질문: 부분공간이 덧셈과 스칼라곱에 닫혀 있음을 설명할 수 있는가?
- 확인 질문: 선형사상의 kernel과 image를 구할 수 있는가?

부분공간과 kernel이 불분명하면 선수 단원을 먼저 복습한다.

## 기호와 용어

| 기호·용어 | 읽는 법 | 의미 | 범위 |
|---|---|---|---|
| $x\sim y$ | 엑스와 와이는 동치 | 정한 기준에서 두 원소를 같은 것으로 취급한다. | 동치관계가 필요하다. |
| $[x]$ | 엑스의 동치류 | $x$와 동치인 모든 원소의 집합 | $x$는 대표원이다. |
| $\mathbf v+U$ | 브이 플러스 유 | $\mathbf v$에 $U$의 모든 벡터를 더한 집합 | $U$의 coset |
| $V/U$ | 브이 몫 유 | $U$ 방향 차이를 무시한 동치류들의 집합 | quotient space |
| $\pi:V\to V/U$ | 파이 | 벡터를 자기 동치류로 보내는 quotient map | $\pi(\mathbf v)=\mathbf v+U$ |
| 대표원 | representative | 동치류를 표시하기 위해 고른 한 원소 | 같은 동치류에 여러 대표원이 있다. |

## 핵심 개념 1. 동치관계는 같은 것으로 취급할 규칙이다

집합 $X$ 위의 관계 $\sim$가 동치관계가 되려면 모든 $x,y,z\in X$에 대해 다음 조건을 만족해야 한다.

1. 반사성: $x\sim x$
2. 대칭성: $x\sim y$이면 $y\sim x$
3. 추이성: $x\sim y$이고 $y\sim z$이면 $x\sim z$

정수에서

\[
a\sim b
\quad\Longleftrightarrow\quad
a-b\text{가 }3\text{의 배수다}
\]

라고 정의하면 동치관계다. 각 정수는 나머지가 0, 1, 2인 세 부류 중 하나에 들어간다.

세 조건 중 하나라도 빠지면 동치류가 일관된 묶음을 만들지 못할 수 있다. 예를 들어 실수에서 $x\le y$는 반사성과 추이성을 만족하지만 대칭성을 만족하지 않는다.

## 핵심 개념 2. 동치류는 동치인 원소를 한 묶음으로 만든다

$x\in X$의 동치류를

\[
[x]
=
\{y\in X:y\sim x\}
\]

로 정의한다. $x$는 동치류의 대표원 한 개다.

$x\sim y$이면

\[
[x]=[y]
\]

이다. $x$와 $y$가 동치가 아니면 두 동치류는 겹치지 않는다. 따라서 동치류들은 $X$를 서로 겹치지 않는 부분집합으로 나눈다. 이를 분할(partition)이라고 한다.

대표원은 유일하지 않다. 같은 동치류의 어느 원소를 써도 같은 묶음을 나타낸다.

## 핵심 개념 3. 부분공간 방향의 차이를 동치로 정의할 수 있다

$U\le V$라 하자. 두 벡터 $\mathbf v,\mathbf w\in V$에 대해

\[
\mathbf v\sim_U\mathbf w
\quad\Longleftrightarrow\quad
\mathbf v-\mathbf w\in U
\]

로 정의한다. 이 관계는 동치관계다.

반사성은

\[
\mathbf v-\mathbf v=\mathbf 0\in U
\]

에서 따른다. 대칭성은 $\mathbf v-\mathbf w\in U$일 때

\[
\mathbf w-\mathbf v=-(\mathbf v-\mathbf w)\in U
\]

이므로 성립한다. 추이성은

\[
\mathbf v-\mathbf z
=
(\mathbf v-\mathbf w)+(\mathbf w-\mathbf z)\in U
\]

에서 따른다. 세 단계에서 $U$가 영벡터를 포함하고 스칼라곱과 덧셈에 닫혀 있다는 성질을 사용했다.

## 핵심 개념 4. 동치류는 부분공간의 평행이동이다

$\mathbf v$의 동치류는

\[
[\mathbf v]
=
\{\mathbf w\in V:\mathbf w-\mathbf v\in U\}
=
\mathbf v+U
\]

로 쓸 수 있다. 여기서

\[
\mathbf v+U
=
\{\mathbf v+\mathbf u:\mathbf u\in U\}
\]

를 $U$의 coset이라고 한다.

$\mathbf v$와 $\mathbf v+\mathbf u_0$는 $\mathbf u_0\in U$일 때 같은 coset을 나타낸다.

\[
(\mathbf v+\mathbf u_0)+U
=
\mathbf v+U
\]

따라서 $\mathbf v$는 동치류의 이름을 적기 위한 대표원이며 동치류 자체와 같지 않다.

## 핵심 개념 5. 몫공간은 동치류를 벡터로 사용한다

모든 coset의 집합을

\[
V/U
=
\{\mathbf v+U:\mathbf v\in V\}
\]

로 쓴다. 이 집합에 다음 연산을 정의한다.

\[
(\mathbf v+U)+(\mathbf w+U)
=
(\mathbf v+\mathbf w)+U
\]

\[
\alpha(\mathbf v+U)
=
(\alpha\mathbf v)+U
\]

대표원을 다르게 골라도 결과 동치류가 같아야 한다. 이를 연산이 well-defined라고 표현한다.

$\mathbf v'=\mathbf v+\mathbf u_1$과 $\mathbf w'=\mathbf w+\mathbf u_2$이고 $\mathbf u_1,\mathbf u_2\in U$라 하자. 그러면

\[
(\mathbf v'+\mathbf w')-(\mathbf v+\mathbf w)
=
\mathbf u_1+\mathbf u_2\in U
\]

이므로

\[
(\mathbf v'+\mathbf w')+U
=
(\mathbf v+\mathbf w)+U
\]

다. 스칼라곱도 $\alpha\mathbf u_1\in U$이므로 같은 방식으로 확인할 수 있다.

## 핵심 개념 6. quotient map은 버리는 방향을 kernel로 갖는다

quotient map

\[
\pi:V\to V/U,
\qquad
\pi(\mathbf v)=\mathbf v+U
\]

는 선형이다. 영벡터에 해당하는 몫공간 원소는

\[
U=\mathbf 0+U
\]

다. 따라서

\[
\ker\pi
=
\{\mathbf v:\mathbf v+U=U\}
=
U
\]

이다. $\pi$는 $U$ 방향을 영벡터로 보내고, $U$ 방향으로만 다른 벡터들을 같은 출력으로 보낸다.

유한차원에서는 rank-nullity 정리를 적용해

\[
\dim(V/U)
=
\dim V-\dim U
\]

를 얻는다. quotient map의 image가 $V/U$ 전체이고 kernel이 $U$이기 때문이다.

## 핵심 개념 7. kernel로 나눈 공간은 image와 같은 선형 구조를 갖는다

선형사상 $T:V\to W$에서

\[
\mathbf v-\mathbf w\in\ker T
\]

이면

\[
T(\mathbf v)-T(\mathbf w)
=
T(\mathbf v-\mathbf w)
=
\mathbf 0
\]

이므로 $T(\mathbf v)=T(\mathbf w)$다. $T$는 같은 kernel coset에 속한 입력을 구분하지 않는다.

이에 따라

\[
\widetilde T:V/\ker T\to\operatorname{im}T,
\qquad
\widetilde T(\mathbf v+\ker T)=T(\mathbf v)
\]

를 정의할 수 있다. 이 사상은 일대일이고 전사인 선형사상이다. 따라서

\[
V/\ker T\cong\operatorname{im}T
\]

로 쓴다. 이 결과는 선형사상이 잃는 방향을 kernel로 제거하면 남은 입력 구조가 실제 출력 구조와 대응한다는 뜻이다.

## 예제 1. 평면을 한 방향으로 나누기

### 문제

$V=\mathbb R^2$와

\[
U=\operatorname{span}
\left\{
\begin{bmatrix}1\\0\end{bmatrix}
\right\}
\]

를 생각하자. $\mathbf v=(2,3)^\top$의 동치류를 구하고 $(5,3)^\top$, $(2,4)^\top$가 같은 동치류에 속하는지 판정하라.

### 풀이

$U$는 $x$축이므로

\[
\mathbf v+U
=
\left\{
\begin{bmatrix}
2+a\\
3
\end{bmatrix}
:a\in\mathbb R
\right\}
\]

이다. 이는 높이가 3인 수평선이다.

\[
\begin{bmatrix}5\\3\end{bmatrix}
-
\begin{bmatrix}2\\3\end{bmatrix}
=
\begin{bmatrix}3\\0\end{bmatrix}
\in U
\]

이므로 $(5,3)^\top$는 같은 동치류에 속한다.

\[
\begin{bmatrix}2\\4\end{bmatrix}
-
\begin{bmatrix}2\\3\end{bmatrix}
=
\begin{bmatrix}0\\1\end{bmatrix}
\notin U
\]

이므로 $(2,4)^\top$는 다른 동치류에 속한다.

### 결과의 의미

$V/U$에서는 첫 좌표의 차이를 무시하고 둘째 좌표만 구분한다. 각 몫공간 원소는 점 하나가 아니라 수평선 하나다.

## 예제 2. 몫공간 연산 계산하기

### 문제

예제 1의 $U$에 대해

\[
\mathbf v=
\begin{bmatrix}2\\3\end{bmatrix},
\qquad
\mathbf w=
\begin{bmatrix}-1\\4\end{bmatrix}
\]

일 때 $(\mathbf v+U)+(\mathbf w+U)$와 $2(\mathbf v+U)$를 구하라.

### 풀이

\[
(\mathbf v+U)+(\mathbf w+U)
=
(\mathbf v+\mathbf w)+U
=
\begin{bmatrix}
1\\7
\end{bmatrix}
+U
\]

이다. 이 coset은 높이가 7인 수평선이다.

\[
2(\mathbf v+U)
=
(2\mathbf v)+U
=
\begin{bmatrix}
4\\6
\end{bmatrix}
+U
\]

이고 높이가 6인 수평선이다.

### 결과의 의미

첫 좌표는 대표원에 따라 달라질 수 있다. 연산 결과 동치류는 둘째 좌표 7과 6으로 정해진다.

## 예제 3. 미분사상에서 상수항 없애기

미분사상

\[
D:\mathcal P_2\to\mathcal P_1,
\qquad
D(p)=p'
\]

의 kernel은 상수다항식 공간

\[
\ker D=\operatorname{span}\{1\}
\]

이다. $p(t)=2+3t+t^2$와 $q(t)=-5+3t+t^2$는 상수항만 다르므로

\[
p-q=7\in\ker D
\]

이고 같은 동치류에 속한다. 실제로

\[
D(p)=3+2t=D(q)
\]

다.

몫공간 $\mathcal P_2/\ker D$에서는 상수항 차이를 무시한다. 각 동치류는 $bt+ct^2$의 두 계수로 구분되므로 차원이 2다.

\[
\dim(\mathcal P_2/\ker D)
=
3-1
=
2
\]

미분사상의 image인 $\mathcal P_1$도 차원이 2이며, $p+\ker D$를 $p'$로 보내는 사상이 두 공간을 연결한다.

## 예제 4. 표현에서 nuisance 부분공간 무시하기

activation 공간 $V=\mathbb R^d$에서 분석자가 nuisance 방향들의 부분공간 $U$를 정했다고 하자. quotient 표현

\[
\mathbf h+U
\]

는 $\mathbf h$와 $\mathbf h+\mathbf u$를 모든 $\mathbf u\in U$에 대해 같은 원소로 취급한다.

몫공간은 대표원 하나를 자동으로 고르지 않는다. Euclidean 내적을 사용해

\[
\operatorname{proj}_{U^\perp}\mathbf h
\]

를 대표원으로 고를 수 있지만, 이는 직교여공간과 metric을 추가로 선택한 결과다. quotient 자체는 $U$ 방향의 차이를 무시한다는 동치관계만 정한다.

분석자가 nuisance 방향을 잘못 정하면 과제에 필요한 정보도 같은 동치류 안에서 사라진다. quotient 결과를 사용하려면 $U$의 선택 근거와 제거 전후의 과제 성능을 함께 보고해야 한다.

## 흔한 오해

### 오해 1. 비슷해 보이는 관계는 동치관계다

동치관계는 반사성, 대칭성과 추이성을 모두 만족해야 한다. 거리 임계값 안에 있다는 관계는 추이성을 만족하지 않을 수 있다.

### 오해 2. 동치류는 대표원 하나다

대표원은 동치류를 표시하는 한 원소다. 동치류는 그 대표원과 동치인 원소 전체의 집합이다.

### 오해 3. $V/U$는 벡터를 성분별로 나누는 연산이다

$V/U$는 scalar 나눗셈이 아니다. $U$ 방향으로 차이 나는 벡터들을 같은 원소로 묶어 만든 새 벡터공간이다.

### 오해 4. quotient는 정사영과 같다

quotient는 동치류를 원소로 사용한다. 정사영은 내적과 여공간을 사용해 각 동치류에서 특정 대표원을 고르는 한 방법이다.

### 오해 5. 모든 모델 대칭성의 quotient는 벡터공간이다

부분공간의 덧셈 차이로 정의한 quotient는 벡터공간이다. neuron 순열이나 비선형 재매개화로 생긴 동치류는 일반적인 vector-space quotient가 아닐 수 있다.

## 연습문제

### 1. 동치관계 판정

정수에서

\[
a\sim b
\quad\Longleftrightarrow\quad
a-b\text{가 짝수다}
\]

라고 정의한다. 반사성, 대칭성과 추이성을 확인하라.

<details>
<summary>해설 보기</summary>

$a-a=0$은 짝수이므로 반사성을 만족한다. $a-b$가 짝수이면 $b-a=-(a-b)$도 짝수이므로 대칭성을 만족한다. $a-b$와 $b-c$가 짝수이면 합인 $a-c$도 짝수이므로 추이성을 만족한다. 따라서 동치관계다.

</details>

### 2. 동치류 구하기

연습문제 1의 관계에서 $[0]$과 $[1]$을 설명하라.

<details>
<summary>해설 보기</summary>

$[0]$은 0과 차이가 짝수인 모든 짝수의 집합이다. $[1]$은 1과 차이가 짝수인 모든 홀수의 집합이다. 두 동치류는 겹치지 않으며 모든 정수는 둘 중 하나에 속한다.

</details>

### 3. coset 판정

$V=\mathbb R^3$와 $U=\operatorname{span}\{\mathbf e_1,\mathbf e_2\}$에서

\[
\mathbf v=
\begin{bmatrix}1\\2\\3\end{bmatrix},
\qquad
\mathbf w=
\begin{bmatrix}5\\-1\\3\end{bmatrix}
\]

가 같은 coset을 나타내는지 판정하라.

<details>
<summary>해설 보기</summary>

\[
\mathbf v-\mathbf w
=
\begin{bmatrix}
-4\\3\\0
\end{bmatrix}
\]

는 $\mathbf e_1,\mathbf e_2$의 선형결합이므로 $U$에 속한다. 따라서 $\mathbf v\sim_U\mathbf w$이고 $\mathbf v+U=\mathbf w+U$다.

</details>

### 4. 몫공간 연산

연습문제 3의 $U$에 대해

\[
\left(
\begin{bmatrix}1\\0\\2\end{bmatrix}
+U
\right)
+
\left(
\begin{bmatrix}0\\4\\-1\end{bmatrix}
+U
\right)
\]

을 계산하라.

<details>
<summary>해설 보기</summary>

대표원을 더하면

\[
\begin{bmatrix}1\\0\\2\end{bmatrix}
+
\begin{bmatrix}0\\4\\-1\end{bmatrix}
=
\begin{bmatrix}1\\4\\1\end{bmatrix}
\]

이므로 결과는

\[
\begin{bmatrix}1\\4\\1\end{bmatrix}
+U
\]

다. 이 quotient에서는 첫째와 둘째 좌표 차이를 무시하므로 셋째 좌표가 1인 모든 벡터가 같은 coset에 속한다.

</details>

### 5. 몫공간 차원

$\dim V=8$이고 $\dim U=3$일 때 $\dim(V/U)$를 구하라.

<details>
<summary>해설 보기</summary>

\[
\dim(V/U)
=
\dim V-\dim U
=
8-3
=
5
\]

다. quotient map의 kernel이 $U$이고 image가 $V/U$ 전체이므로 rank-nullity 정리에서도 같은 값을 얻는다.

</details>

### 6. quotient와 image

$T:\mathbb R^3\to\mathbb R^2$가

\[
T(x,y,z)^\top=(x,y)^\top
\]

로 주어진다. $\ker T$, $\operatorname{im}T$와 $\mathbb R^3/\ker T$의 차원을 구하라.

<details>
<summary>해설 보기</summary>

\[
\ker T
=
\operatorname{span}
\left\{
\begin{bmatrix}0\\0\\1\end{bmatrix}
\right\}
\]

이고 $\operatorname{im}T=\mathbb R^2$다. 따라서

\[
\dim(\mathbb R^3/\ker T)
=
3-1
=
2
\]

다. quotient의 동치류는 셋째 좌표 차이를 무시하며, 각 동치류는 출력 $(x,y)^\top$와 일대일로 대응한다.

</details>

### 7. 모델 주장 비판

“nuisance 부분공간 $U$로 quotient를 취하면 의미 정보만 남는다”는 주장을 비판하라.

<details>
<summary>해설 보기</summary>

quotient는 $U$ 방향의 모든 차이를 제거하지만 그 방향이 nuisance만 담는지는 보장하지 않는다. $U$가 과제 관련 정보도 포함하면 그 정보도 사라진다. 분석자는 $U$의 추정 절차, 독립 데이터에서의 안정성, quotient 전후 복원·과제 성능과 대조 부분공간을 검사해야 한다.

</details>

## 단원 요약

- 동치관계는 반사성, 대칭성과 추이성을 만족해 원소들을 동치류로 나눈다.
- 부분공간 $U$에 대해 $\mathbf v-\mathbf w\in U$이면 두 벡터를 동치로 둘 수 있다.
- 동치류 $\mathbf v+U$는 $U$의 평행이동이며 대표원은 유일하지 않다.
- 몫공간 $V/U$는 coset을 원소로 사용하고 대표원과 무관한 연산을 갖는다.
- quotient map의 kernel은 $U$이고 유한차원에서 $\dim(V/U)=\dim V-\dim U$다.
- $V/\ker T$는 $\operatorname{im}T$와 같은 선형 구조를 갖는다.
- quotient는 동치류를 만들고 정사영은 추가한 내적에 따라 대표원을 고른다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- 관계가 반사성, 대칭성과 추이성을 만족하는지 검사할 수 있는가?
- 동치류와 대표원을 구분할 수 있는가?
- 부분공간으로 만든 관계가 동치관계임을 확인할 수 있는가?
- coset과 몫공간의 연산을 계산할 수 있는가?
- quotient map의 kernel과 몫공간의 차원을 구할 수 있는가?
- $V/\ker T$와 $\operatorname{im}T$의 대응을 설명할 수 있는가?
- quotient와 정사영을 구분할 수 있는가?

## 다음 단원

- [M03-07 쌍대공간과 covector](M03-07-dual-spaces-covectors.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] 동치관계의 세 조건을 확인했다.
- [x] 동치류, 대표원과 coset을 구분했다.
- [x] 몫공간 연산의 well-defined 조건을 설명했다.
- [x] quotient map과 kernel·image를 연결했다.
- [x] 정사영 및 일반 모델 대칭성과의 차이를 밝혔다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 내부 링크와 수식 구분자를 확인했다.
