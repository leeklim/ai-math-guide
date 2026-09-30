---
id: "M03-05"
title: "부분공간, 직합과 분해"
part: 1
stage: "M03"
status: "완료"
prerequisites:
  - "M03-01"
  - "M02-08"
  - "M02-09"
estimated_time: "120~145분"
---

# M03-05. 부분공간, 직합과 분해

## 이 단원이 필요한 이유

표현공간을 여러 성분으로 나눌 때 각 성분이 부분공간인지, 서로 겹치는지, 원래 벡터를 유일하게 복원하는지 확인해야 한다. 두 부분공간의 벡터를 더해 원래 공간을 만들 수 있어도 분해가 유일하지 않을 수 있다. 겹침이 없는 직합(direct sum)은 이 유일성을 보장한다.

모델 해석에서는 activation을 특정 feature 부분공간과 나머지 성분으로 분해하거나, 저랭크 부분공간에 투영한 뒤 잔차를 분석한다. 분해 결과는 선택한 부분공간과 내적에 의존한다. 부분공간에서 정보를 복원했다는 결과만으로 모델이 그 부분공간을 기능적으로 사용한다고 결론 내릴 수는 없다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- 두 부분공간의 합과 교집합을 정의하고 작은 예제에서 구할 수 있다.
- 부분공간의 합이 직합인지 교집합으로 판정할 수 있다.
- 직합에서 벡터 분해가 유일함을 설명할 수 있다.
- 차원 공식을 사용해 부분공간 합의 차원을 계산할 수 있다.
- 직교여공간과 정사영으로 벡터를 신호 성분과 잔차로 분해할 수 있다.
- 모델 표현의 부분공간 분해가 허용하는 주장과 허용하지 않는 주장을 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [M03-01 추상 벡터공간](M03-01-abstract-vector-spaces.md)
- 선수 단원: [M02-08 kernel, image와 rank](../M02/M02-08-kernel-image-rank.md)
- 선수 단원: [M02-09 직교기저와 정사영](../M02/M02-09-orthogonal-basis-projection.md)
- 확인 질문: 부분공간을 영벡터 포함과 연산의 닫힘으로 판정할 수 있는가?
- 확인 질문: 정규직교기저를 사용해 벡터를 부분공간에 정사영할 수 있는가?

부분공간과 정사영 계산이 불분명하면 선수 단원을 먼저 복습한다.

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | 조건 |
|---|---|---|---|
| $U,W$ | `U and W` | 벡터공간 $V$의 부분공간 | $U,W\le V$ |
| $U+W$ | `U plus W` | $\mathbf u+\mathbf w$ 꼴 벡터들의 부분공간 | $\mathbf u\in U,\mathbf w\in W$ |
| $U\cap W$ | `U intersection W` | 두 부분공간에 모두 속하는 벡터들의 공간 | 적어도 영벡터를 포함한다. |
| $U\oplus W$ | `U direct sum W` | 교집합이 영공간인 부분공간 합 | 각 벡터의 분해가 유일하다. |
| $U^\perp$ | `U perp` | $U$의 모든 벡터와 직교하는 벡터들의 공간 | 내적이 정해져야 한다. |
| $\operatorname{proj}_U\mathbf x$ | `the projection of x onto U` | $U$에서 $\mathbf x$에 가장 가까운 벡터 | Euclidean 내적 기준 |

## 핵심 개념 1. 부분공간의 합은 두 공간의 성분을 더해 만든다

$U,W\le V$일 때 두 부분공간의 합을

\[
U+W
=
\{\mathbf u+\mathbf w:\mathbf u\in U,\ \mathbf w\in W\}
\]

로 정의한다. $U+W$는 $U\cup W$와 다르다. 합에는 두 공간의 벡터를 섞은 선형결합도 들어간다.

$U+W$는 $V$의 부분공간이다. 영벡터는 $\mathbf 0_U+\mathbf 0_W$로 쓸 수 있다. 두 원소

\[
\mathbf x=\mathbf u_1+\mathbf w_1,
\qquad
\mathbf y=\mathbf u_2+\mathbf w_2
\]

를 더하면

\[
\mathbf x+\mathbf y
=
(\mathbf u_1+\mathbf u_2)+(\mathbf w_1+\mathbf w_2)
\]

이고 각 괄호는 해당 부분공간에 남는다. 스칼라곱도 같은 방식으로 닫혀 있다.

## 핵심 개념 2. 교집합은 두 분해 성분의 겹침을 나타낸다

\[
U\cap W
=
\{\mathbf v\in V:\mathbf v\in U\text{이고 }\mathbf v\in W\}
\]

이다. 두 부분공간은 영벡터를 함께 가지므로 교집합이 공집합일 수 없다.

교집합에 영벡터가 아닌 $\mathbf z$가 있으면 같은 벡터를 여러 방식으로 나눌 수 있다. $\mathbf x=\mathbf u+\mathbf w$라 할 때

\[
\mathbf x
=
(\mathbf u+\mathbf z)+(\mathbf w-\mathbf z)
\]

도 같은 분해다. $\mathbf z\in U$이므로 $\mathbf u+\mathbf z\in U$이고, $\mathbf z\in W$이므로 $\mathbf w-\mathbf z\in W$다.

## 핵심 개념 3. 직합은 유일한 분해를 보장한다

\[
V=U\oplus W
\]

라는 표기는 다음 두 조건을 뜻한다.

1. $V=U+W$
2. $U\cap W=\{\mathbf 0\}$

이 조건에서 모든 $\mathbf v\in V$는

\[
\mathbf v=\mathbf u+\mathbf w
\]

로 유일하게 분해된다.

유일성을 확인하려면 두 분해를 가정한다.

\[
\mathbf v
=
\mathbf u_1+\mathbf w_1
=
\mathbf u_2+\mathbf w_2
\]

그러면

\[
\mathbf u_1-\mathbf u_2
=
\mathbf w_2-\mathbf w_1
\]

이다. 왼쪽은 $U$에 있고 오른쪽은 $W$에 있으므로 이 벡터는 $U\cap W$에 있다. 교집합이 영공간이면 두 차이는 모두 영벡터이고

\[
\mathbf u_1=\mathbf u_2,
\qquad
\mathbf w_1=\mathbf w_2
\]

다.

## 핵심 개념 4. 차원 공식은 겹친 방향을 한 번 뺀다

유한차원 부분공간에서는

\[
\dim(U+W)
=
\dim U+\dim W-\dim(U\cap W)
\]

가 성립한다. $U$와 $W$의 차원을 더하면 교집합의 방향을 두 번 세므로 한 번 뺀다.

직합이면 $U\cap W=\{\mathbf 0\}$이고 영공간의 차원은 0이므로

\[
\dim(U\oplus W)
=
\dim U+\dim W
\]

이다.

차원만 맞는다고 직합이 되는 것은 아니다. 합이 전체 공간을 만드는지와 교집합이 영공간인지 함께 확인해야 한다.

## 핵심 개념 5. 여공간은 전체 공간의 나머지 방향을 채운다

$V=U\oplus W$를 만족하는 $W$를 $U$의 여공간(complement)이라고 한다. 한 부분공간의 여공간은 일반적으로 여러 개다.

예를 들어 $V=\mathbb R^2$와 $U=\operatorname{span}\{(1,0)^\top\}$에서

\[
W_1=\operatorname{span}\{(0,1)^\top\}
\]

과

\[
W_2=\operatorname{span}\{(1,1)^\top\}
\]

는 모두 $U$의 여공간이다. 두 직선 모두 $U$와 영벡터에서만 만나고 $U$와 함께 $\mathbb R^2$를 생성한다.

내적이 정해지면 직교여공간

\[
U^\perp
=
\{\mathbf v\in V:\langle\mathbf v,\mathbf u\rangle=0
\text{ for every }\mathbf u\in U\}
\]

을 고를 수 있다. 유한차원 내적공간에서는

\[
V=U\oplus U^\perp
\]

이다.

## 핵심 개념 6. 정사영은 직교 직합의 두 성분을 계산한다

$\mathbf P_U$를 $U$ 위로의 정사영행렬이라 하면

\[
\mathbf x
=
\underbrace{\mathbf P_U\mathbf x}_{\mathbf x_U\in U}
+
\underbrace{(\mathbf I-\mathbf P_U)\mathbf x}_{\mathbf x_\perp\in U^\perp}
\]

이다. 두 성분은 직교한다.

\[
\langle\mathbf x_U,\mathbf x_\perp\rangle=0
\]

따라서 Pythagorean 관계가 성립한다.

\[
\|\mathbf x\|_2^2
=
\|\mathbf x_U\|_2^2+\|\mathbf x_\perp\|_2^2
\]

이 분해는 부분공간 $U$와 내적을 고정했을 때 유일하다.

## 예제 1. 좌표 부분공간의 직합

### 문제

$V=\mathbb R^3$에서

\[
U=\operatorname{span}
\left\{
\begin{bmatrix}1\\0\\0\end{bmatrix},
\begin{bmatrix}0\\1\\0\end{bmatrix}
\right\},
\qquad
W=\operatorname{span}
\left\{
\begin{bmatrix}0\\0\\1\end{bmatrix}
\right\}
\]

라 하자. $V=U\oplus W$임을 확인하고

\[
\mathbf x=
\begin{bmatrix}
2\\
-1\\
4
\end{bmatrix}
\]

를 분해하라.

### 풀이

$U$의 벡터는 $(a,b,0)^\top$ 꼴이고 $W$의 벡터는 $(0,0,c)^\top$ 꼴이다. 두 꼴을 모두 만족하는 벡터는 영벡터뿐이므로

\[
U\cap W=\{\mathbf 0\}
\]

이다. 모든 $(x_1,x_2,x_3)^\top$은

\[
\begin{bmatrix}
x_1\\x_2\\x_3
\end{bmatrix}
=
\begin{bmatrix}
x_1\\x_2\\0
\end{bmatrix}
+
\begin{bmatrix}
0\\0\\x_3
\end{bmatrix}
\]

로 쓸 수 있으므로 $U+W=V$다. 따라서 $V=U\oplus W$다.

주어진 벡터의 분해는

\[
\mathbf x
=
\underbrace{
\begin{bmatrix}
2\\-1\\0
\end{bmatrix}}_{\in U}
+
\underbrace{
\begin{bmatrix}
0\\0\\4
\end{bmatrix}}_{\in W}
\]

이다.

### 결과의 의미

$U$는 첫 두 좌표 성분을 담고 $W$는 셋째 좌표 성분을 담는다. 두 부분공간이 겹치지 않으므로 세 좌표를 두 성분으로 나누는 방법이 유일하다.

## 예제 2. 합이 직합이 아닌 경우

### 문제

$V=\mathbb R^2$에서

\[
U=\operatorname{span}\{\mathbf e_1\},
\qquad
W=\mathbb R^2
\]

라 하자. $U+W$와 $U\cap W$를 구하고 $\mathbf e_1$의 서로 다른 두 분해를 제시하라.

### 풀이

$U\subset W$이므로

\[
U+W=W=\mathbb R^2
\]

이고

\[
U\cap W=U
\]

이다. 교집합에 영벡터가 아닌 $\mathbf e_1$이 있으므로 합은 직합이 아니다.

\[
\mathbf e_1
=
\mathbf e_1+\mathbf 0
\]

과

\[
\mathbf e_1
=
\mathbf 0+\mathbf e_1
\]

은 각각 첫 성분이 $U$, 둘째 성분이 $W$에 속하는 서로 다른 분해다.

### 결과의 의미

두 부분공간이 전체 공간을 생성한다는 조건만으로는 유일한 성분 분해를 얻지 못한다.

## 예제 3. activation을 방향과 잔차로 분해하기

정규화된 방향

\[
\mathbf u
=
\frac{1}{\sqrt2}
\begin{bmatrix}
1\\
1\\
0
\end{bmatrix}
\]

이 생성하는 부분공간을 $U=\operatorname{span}\{\mathbf u\}$라 하자. activation

\[
\mathbf h=
\begin{bmatrix}
3\\
1\\
2
\end{bmatrix}
\]

의 $U$ 성분은

\[
\mathbf h_U
=
(\mathbf u^\top\mathbf h)\mathbf u
=
\frac{4}{\sqrt2}
\frac{1}{\sqrt2}
\begin{bmatrix}
1\\1\\0
\end{bmatrix}
=
\begin{bmatrix}
2\\2\\0
\end{bmatrix}
\]

이다. 잔차는

\[
\mathbf h_\perp
=
\mathbf h-\mathbf h_U
=
\begin{bmatrix}
1\\-1\\2
\end{bmatrix}
\]

이다. 두 벡터의 내적은

\[
\mathbf h_U^\top\mathbf h_\perp
=
2\cdot1+2\cdot(-1)+0\cdot2
=
0
\]

이다. 또한

\[
\|\mathbf h\|_2^2=14,
\qquad
\|\mathbf h_U\|_2^2=8,
\qquad
\|\mathbf h_\perp\|_2^2=6
\]

이므로 제곱 norm도 합해진다.

이 계산은 선택한 방향에 대한 activation 성분을 정한다. 그 방향이 개념을 나타내는지, 모델이 그 성분을 예측에 사용하는지는 데이터와 개입으로 따로 검증해야 한다.

## 흔한 오해

### 오해 1. $U+W$는 $U\cup W$다

$U+W$는 한 벡터를 $U$에서, 다른 벡터를 $W$에서 골라 더한 모든 결과를 포함한다. 합집합보다 클 수 있다.

### 오해 2. 두 부분공간이 전체 공간을 만들면 직합이다

전체 공간을 만드는 조건은 $U+W=V$다. 직합에는 $U\cap W=\{\mathbf 0\}$ 조건도 필요하다.

### 오해 3. 여공간은 하나뿐이다

일반 여공간은 여러 개일 수 있다. 내적을 고정하면 직교여공간 $U^\perp$가 정해진다.

### 오해 4. 부분공간 정사영은 기저와 metric에 무관하다

같은 추상 부분공간도 선택한 내적이 달라지면 직교 조건과 정사영이 달라질 수 있다. 좌표행렬을 사용할 때는 기저와 내적을 함께 확인해야 한다.

## 연습문제

### 1. 부분공간의 합

$U=\operatorname{span}\{\mathbf e_1\}$와 $W=\operatorname{span}\{\mathbf e_2\}$가 $\mathbb R^2$의 부분공간일 때 $U+W$를 구하라.

<details>
<summary>해설 보기</summary>

임의의 $(a,b)^\top$은

\[
\begin{bmatrix}
a\\b
\end{bmatrix}
=
a\mathbf e_1+b\mathbf e_2
\]

로 쓸 수 있다. 첫 항은 $U$, 둘째 항은 $W$에 있으므로 $U+W=\mathbb R^2$다.

</details>

### 2. 직합 판정

\[
U=\operatorname{span}
\left\{
\begin{bmatrix}1\\1\end{bmatrix}
\right\},
\qquad
W=\operatorname{span}
\left\{
\begin{bmatrix}1\\-1\end{bmatrix}
\right\}
\]

일 때 $\mathbb R^2=U\oplus W$인지 판정하라.

<details>
<summary>해설 보기</summary>

두 생성벡터는 서로 scalar 배가 아니므로 선형독립이다. 따라서 두 직선의 교집합은 영벡터뿐이고 두 벡터는 $\mathbb R^2$를 생성한다. 그러므로 $\mathbb R^2=U\oplus W$다.

</details>

### 3. 직합 분해 계산

연습문제 2의 $U,W$에 대해 $\mathbf x=(4,2)^\top$을 $\mathbf u+\mathbf w$로 분해하라.

<details>
<summary>해설 보기</summary>

\[
\begin{bmatrix}
4\\2
\end{bmatrix}
=
a
\begin{bmatrix}
1\\1
\end{bmatrix}
+
b
\begin{bmatrix}
1\\-1
\end{bmatrix}
\]

에서 $a+b=4$, $a-b=2$다. 두 식을 풀면 $a=3$, $b=1$이다. 따라서

\[
\mathbf u=
\begin{bmatrix}
3\\3
\end{bmatrix},
\qquad
\mathbf w=
\begin{bmatrix}
1\\-1
\end{bmatrix}
\]

이다.

</details>

### 4. 차원 공식

$\dim U=4$, $\dim W=3$, $\dim(U\cap W)=2$일 때 $\dim(U+W)$를 구하라.

<details>
<summary>해설 보기</summary>

\[
\dim(U+W)
=
4+3-2
=
5
\]

다. 두 공간의 공통 방향 두 개를 중복해서 세었으므로 한 번 뺀다.

</details>

### 5. 여러 여공간

$U=\operatorname{span}\{(1,0)^\top\}$의 여공간이 될 수 있는 직선 두 개를 제시하고, 여공간이 될 수 없는 직선 하나를 제시하라.

<details>
<summary>해설 보기</summary>

\[
\operatorname{span}\{(0,1)^\top\},
\qquad
\operatorname{span}\{(1,1)^\top\}
\]

은 각각 $U$와 영벡터에서만 만나며 함께 $\mathbb R^2$를 생성하므로 여공간이다. $U$ 자체는 교집합이 $U$이므로 $U$의 여공간이 될 수 없다.

</details>

### 6. 정사영 분해

$U=\operatorname{span}\{(1,0)^\top\}$이고 $\mathbf x=(3,-2)^\top$일 때 $\mathbf x_U$와 $\mathbf x_\perp$를 구하라.

<details>
<summary>해설 보기</summary>

$U$ 위로의 정사영은 첫 좌표만 남기므로

\[
\mathbf x_U=
\begin{bmatrix}
3\\0
\end{bmatrix}
\]

이다. 잔차는

\[
\mathbf x_\perp
=
\mathbf x-\mathbf x_U
=
\begin{bmatrix}
0\\-2
\end{bmatrix}
\]

이다. 두 성분은 직교하고 합은 원래 벡터다.

</details>

### 7. 모델 주장 비판

“개념 probe가 부분공간 $U$에서 높은 정확도를 얻었으므로 모델은 예측할 때 $U$만 사용한다”는 결론을 비판하라.

<details>
<summary>해설 보기</summary>

probe 결과는 $U$에서 개념 정보를 복원할 수 있다는 증거다. 모델이 $U$를 기능적으로 사용하는지, $U^\perp$에도 중복 정보가 있는지, $U$를 제거하면 예측이 변하는지는 이 결과로 정해지지 않는다. $U$ 성분 제거, 대조 부분공간과 matched control을 사용한 개입이 추가로 필요하다.

</details>

## 단원 요약

- $U+W$는 두 부분공간에서 고른 벡터를 더해 만든 부분공간이다.
- 직합 $U\oplus W$는 교집합이 영공간이며 각 벡터의 분해가 유일한 합이다.
- 부분공간 합의 차원은 두 차원의 합에서 교집합의 차원을 뺀 값이다.
- 여공간은 여러 개일 수 있으며 내적을 고정하면 직교여공간을 고를 수 있다.
- 정사영은 벡터를 부분공간 성분과 직교 잔차로 유일하게 분해한다.
- 부분공간에서의 정보 복원과 모델의 기능적 사용은 다른 주장이다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- $U+W$와 $U\cap W$를 정의하고 예제에서 구할 수 있는가?
- 두 부분공간의 합이 직합인지 판정할 수 있는가?
- 직합 분해가 유일한 이유를 설명할 수 있는가?
- 차원 공식을 적용할 수 있는가?
- 여공간과 직교여공간을 구분할 수 있는가?
- 정사영 성분과 잔차를 계산할 수 있는가?
- 부분공간 분석이 허용하는 주장 범위를 제한할 수 있는가?

## 다음 단원

- [M03-06 동치관계와 몫공간](M03-06-equivalence-relations-quotient-spaces.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] 부분공간 합과 합집합을 구분했다.
- [x] 직합의 두 조건과 유일성을 설명했다.
- [x] 차원 공식과 직교분해를 계산했다.
- [x] 여공간의 비유일성을 밝혔다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 구분자를 확인했다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
