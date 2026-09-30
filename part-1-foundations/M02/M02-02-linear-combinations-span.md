---
id: "M02-02"
title: "선형결합과 span"
part: 1
stage: "M02"
status: "완료"
prerequisites:
  - "M02-01"
estimated_time: "95~120분"
---

# M02-02. 선형결합과 span

## 이 단원이 필요한 이유

신경망의 많은 계산은 여러 벡터에 수를 곱한 뒤 더하는 형태다. 한 neuron의 입력 가중합, attention의 value 가중합과 여러 feature 방향의 합이 모두 이 구조를 갖는다. 이때 어떤 벡터를 만들 수 있는지 묻는 개념이 생성공간, 즉 span이다.

span을 이해하면 주어진 방향들이 평면 전체를 만드는지, 한 직선에만 머무는지, 목표 벡터를 표현할 수 있는지 판단할 수 있다. 부분공간, 기저, rank와 SVD를 배우기 전 필요한 출발점이다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- 벡터들의 선형결합을 정의하고 직접 계산할 수 있다.
- 한 개 또는 두 개 벡터가 만드는 생성공간을 기하적으로 설명할 수 있다.
- 목표 벡터가 주어진 벡터들의 span에 속하는지 계수 방정식으로 판단할 수 있다.
- 생성 벡터가 중복될 때 표현이 유일하지 않을 수 있음을 설명할 수 있다.
- 신경망의 가중합을 선형결합으로 읽고 그 결과가 허용하는 주장 범위를 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [M02-01 벡터와 벡터 연산](M02-01-vectors-vector-operations.md)
- 확인 질문: 벡터에 스칼라를 곱한 뒤 같은 dimension의 벡터끼리 더할 수 있는가?
- 확인 질문: $\alpha\mathbf v$에서 $\alpha$의 부호가 방향에 미치는 영향을 설명할 수 있는가?

벡터 덧셈이나 스칼라곱이 불분명하면 M02-01을 먼저 복습한다.

## 기호와 용어

| 기호·용어 | 읽는 법 | 의미 | 조건 |
|---|---|---|---|
| $c_i$ | 씨 아래 아이 | $i$번째 벡터에 곱하는 계수 | $c_i\in\mathbb R$ |
| $\sum_{i=1}^{k}c_i\mathbf v_i$ | 아이는 1부터 케이까지 씨 아이 브이 아이의 합 | $k$개 벡터의 선형결합 | 모든 $\mathbf v_i$의 dimension이 같다. |
| $\operatorname{span}\{\mathbf v_1,\ldots,\mathbf v_k\}$ | 브이 원부터 브이 케이가 생성하는 공간 | 가능한 모든 선형결합의 집합 | $\mathbf v_i\in\mathbb R^n$ |
| 생성 벡터 | generating vector | 선형결합의 재료가 되는 벡터 | 같은 벡터공간에 속한다. |

## 핵심 개념 1. 선형결합은 스칼라곱을 더한 것이다

$\mathbf v_1,\ldots,\mathbf v_k\in\mathbb R^n$과 실수 $c_1,\ldots,c_k$가 있을 때

\[
c_1\mathbf v_1
+c_2\mathbf v_2
+\cdots
+c_k\mathbf v_k
\]

를 벡터들의 선형결합이라고 한다. 합 기호로는

\[
\sum_{i=1}^{k}c_i\mathbf v_i
\]

라고 쓴다.

계수 $c_i$는 각 벡터를 얼마나, 어느 방향으로 사용할지 정한다. 양수는 같은 방향, 음수는 반대 방향, 0은 해당 벡터를 사용하지 않는 경우다.

## 핵심 개념 2. span은 가능한 모든 계수를 허용한다

벡터 $\mathbf v_1,\ldots,\mathbf v_k$의 생성공간은

\[
\operatorname{span}\{\mathbf v_1,\ldots,\mathbf v_k\}
=
\left\{
\sum_{i=1}^{k}c_i\mathbf v_i
\;\middle|\;
c_1,\ldots,c_k\in\mathbb R
\right\}
\]

이다.

이 식은 특정 계수로 만든 벡터 하나가 아니라, 모든 실수 계수를 바꾸어 만들 수 있는 벡터 전체를 뜻한다. 중괄호 오른쪽의 조건은 계수를 실수 범위에서 자유롭게 고른다는 뜻이다.

## 핵심 개념 3. 벡터 하나의 span은 원점을 지나는 직선이다

$\mathbf v\ne\mathbf 0$이면

\[
\operatorname{span}\{\mathbf v\}
=
\{c\mathbf v\mid c\in\mathbb R\}
\]

이다. $c$를 바꾸면 $\mathbf v$와 같은 방향 또는 반대 방향의 모든 배수를 얻는다. 따라서 $\mathbb R^2$나 $\mathbb R^3$에서 원점을 지나는 직선이 된다.

영벡터만 사용하면

\[
\operatorname{span}\{\mathbf 0\}
=
\{\mathbf 0\}
\]

이다. 어떤 실수를 곱해도 영벡터이기 때문이다.

## 핵심 개념 4. 서로 다른 두 방향은 평면을 만들 수 있다

$\mathbb R^2$에서 두 벡터가 같은 직선 위에 있지 않으면 두 방향을 섞어 평면의 모든 벡터를 만들 수 있다. 예를 들어

\[
\mathbf e_1=
\begin{bmatrix}1\\0\end{bmatrix},
\qquad
\mathbf e_2=
\begin{bmatrix}0\\1\end{bmatrix}
\]

이면 임의의 $\mathbf x=\begin{bmatrix}x_1\\x_2\end{bmatrix}$에 대해

\[
\mathbf x=x_1\mathbf e_1+x_2\mathbf e_2
\]

이므로

\[
\operatorname{span}\{\mathbf e_1,\mathbf e_2\}
=
\mathbb R^2
\]

이다.

두 벡터가 같은 방향의 배수라면 두 번째 벡터는 새 방향을 추가하지 않는다. 생성공간은 여전히 한 직선이다.

## 핵심 개념 5. span 소속 여부는 계수를 찾는 문제다

목표 벡터 $\mathbf b$가 $\operatorname{span}\{\mathbf v_1,\ldots,\mathbf v_k\}$에 속하는지 판단하려면

\[
c_1\mathbf v_1+\cdots+c_k\mathbf v_k=\mathbf b
\]

를 만족하는 실수 계수 $c_1,\ldots,c_k$가 있는지 찾는다.

성분별 등식을 쓰면 연립방정식이 된다. 해가 하나라도 있으면 $\mathbf b$는 span에 속하고, 해가 없으면 속하지 않는다. 연립방정식의 체계적인 해법은 M02-06에서 다룬다.

## 핵심 개념 6. span은 덧셈과 스칼라곱에 닫혀 있다

$\mathbf x$와 $\mathbf y$가 같은 생성공간에 속한다고 하자.

\[
\mathbf x=\sum_i a_i\mathbf v_i,
\qquad
\mathbf y=\sum_i b_i\mathbf v_i
\]

이면

\[
\mathbf x+\mathbf y
=
\sum_i(a_i+b_i)\mathbf v_i
\]

도 같은 벡터들의 선형결합이다. 임의의 스칼라 $\alpha$에 대해서도

\[
\alpha\mathbf x
=
\sum_i(\alpha a_i)\mathbf v_i
\]

이므로 같은 생성공간에 속한다.

이처럼 덧셈과 스칼라곱의 결과가 집합 밖으로 나가지 않는 성질을 닫힘이라고 한다. 생성공간은 부분공간의 대표적인 예다. 부분공간의 조건은 M03-05에서 더 일반적으로 다룬다.

## 핵심 개념 7. 생성 벡터가 많아도 표현이 유일하지 않을 수 있다

\[
\mathbf v_3=\mathbf v_1+\mathbf v_2
\]

라면 같은 벡터를

\[
\mathbf v_3
\]

또는

\[
\mathbf v_1+\mathbf v_2
\]

로 표현할 수 있다. 생성 벡터 사이에 중복된 방향이 있으면 계수가 여러 가지일 수 있다.

span은 만들 수 있는 벡터의 집합만 말한다. 표현의 유일성은 생성 벡터의 선형독립성과 관련되며 M02-07에서 다룬다.

## 예제 1. 선형결합 계산

\[
\mathbf v_1=
\begin{bmatrix}1\\2\end{bmatrix},
\qquad
\mathbf v_2=
\begin{bmatrix}3\\-1\end{bmatrix}
\]

일 때 $2\mathbf v_1-\mathbf v_2$는

\[
2
\begin{bmatrix}1\\2\end{bmatrix}
-
\begin{bmatrix}3\\-1\end{bmatrix}
=
\begin{bmatrix}2\\4\end{bmatrix}
-
\begin{bmatrix}3\\-1\end{bmatrix}
=
\begin{bmatrix}-1\\5\end{bmatrix}
\]

이다.

## 예제 2. 목표 벡터가 span에 속하는지 확인

\[
\mathbf v_1=
\begin{bmatrix}1\\1\end{bmatrix},
\qquad
\mathbf v_2=
\begin{bmatrix}1\\-1\end{bmatrix},
\qquad
\mathbf b=
\begin{bmatrix}4\\2\end{bmatrix}
\]

라고 하자. $c_1\mathbf v_1+c_2\mathbf v_2=\mathbf b$를 성분별로 쓰면

\[
c_1+c_2=4
\]

\[
c_1-c_2=2
\]

이다. 두 식을 더하면 $2c_1=6$이므로 $c_1=3$이고, 첫 식에서 $c_2=1$이다.

\[
\mathbf b=3\mathbf v_1+\mathbf v_2
\]

이므로 $\mathbf b$는 두 벡터의 span에 속한다.

## 예제 3. 새 방향을 추가하지 않는 벡터

\[
\mathbf v_1=
\begin{bmatrix}1\\2\end{bmatrix},
\qquad
\mathbf v_2=
\begin{bmatrix}2\\4\end{bmatrix}
\]

이면 $\mathbf v_2=2\mathbf v_1$이다. 임의의 계수 $a,b$에 대해

\[
a\mathbf v_1+b\mathbf v_2
=
(a+2b)\mathbf v_1
\]

이므로 두 벡터의 모든 선형결합은 $\mathbf v_1$의 배수다.

\[
\operatorname{span}\{\mathbf v_1,\mathbf v_2\}
=
\operatorname{span}\{\mathbf v_1\}
\]

이다. 생성 벡터가 두 개여도 방향은 하나뿐이다.

## 예제 4. 신경망의 가중합

세 value 벡터 $\mathbf v_1,\mathbf v_2,\mathbf v_3\in\mathbb R^d$와 가중치 $a_1,a_2,a_3$가 있을 때

\[
\mathbf z
=
a_1\mathbf v_1+a_2\mathbf v_2+a_3\mathbf v_3
\]

는 세 벡터의 선형결합이다. 따라서

\[
\mathbf z
\in
\operatorname{span}\{\mathbf v_1,\mathbf v_2,\mathbf v_3\}
\]

이다.

attention에서는 가중치가 보통 음이 아니고 합이 1이라는 추가 제약을 갖는다. 그러므로 실제 가능한 출력은 전체 span보다 좁을 수 있다. span 소속은 어떤 벡터들로 표현할 수 있음을 말할 뿐, 모델이 특정 의미를 사용한다는 인과 증거는 아니다.

## 흔한 오해

### 오해 1. span은 벡터들을 한 번 더한 결과다

span은 벡터 하나가 아니라 모든 실수 계수로 만들 수 있는 선형결합의 집합이다.

### 오해 2. 생성 벡터의 개수가 곧 생성공간의 dimension이다

서로 배수인 벡터들은 같은 방향을 반복한다. 생성 벡터가 세 개여도 실제 독립 방향은 하나나 둘일 수 있다.

### 오해 3. 두 벡터의 span은 언제나 평면 전체다

$\mathbb R^2$에서도 두 벡터가 서로 배수이면 한 직선만 만든다. $\mathbb R^3$에서 서로 배수가 아닌 두 벡터는 보통 원점을 지나는 평면을 만들지만 공간 전체를 만들지는 않는다.

### 오해 4. 어떤 표현이 특정 feature span에 속하면 모델이 그 feature를 사용한다

span 소속은 대수적인 표현 가능성을 보여 준다. 모델 행동에 실제로 필요한지 확인하려면 제거, 패칭이나 다른 개입 증거가 필요하다.

## 연습문제

### 1. 선형결합 계산

\[
\mathbf v_1=
\begin{bmatrix}2\\1\end{bmatrix},
\qquad
\mathbf v_2=
\begin{bmatrix}-1\\3\end{bmatrix}
\]

일 때 $3\mathbf v_1+2\mathbf v_2$를 계산하라.

<details>
<summary>해설 보기</summary>

\[
3\mathbf v_1+2\mathbf v_2
=
\begin{bmatrix}6\\3\end{bmatrix}
+
\begin{bmatrix}-2\\6\end{bmatrix}
=
\begin{bmatrix}4\\9\end{bmatrix}
\]

이다.

</details>

### 2. 한 벡터의 span

\[
\mathbf v=
\begin{bmatrix}2\\-1\end{bmatrix}
\]

일 때 다음 벡터 중 $\operatorname{span}\{\mathbf v\}$에 속하는 것을 모두 고르라.

\[
\mathbf a=
\begin{bmatrix}6\\-3\end{bmatrix},
\qquad
\mathbf b=
\begin{bmatrix}-4\\2\end{bmatrix},
\qquad
\mathbf c=
\begin{bmatrix}2\\1\end{bmatrix}
\]

<details>
<summary>해설 보기</summary>

$\mathbf a=3\mathbf v$이고 $\mathbf b=-2\mathbf v$이므로 두 벡터는 span에 속한다. $\mathbf c$는 첫 성분을 맞추려면 계수가 1이어야 하지만 둘째 성분은 $-1$이 아니라 $1$이므로 $\mathbf v$의 배수가 아니다.

</details>

### 3. 표준기저로 표현

\[
\mathbf e_1=
\begin{bmatrix}1\\0\end{bmatrix},
\qquad
\mathbf e_2=
\begin{bmatrix}0\\1\end{bmatrix}
\]

를 사용해 $\begin{bmatrix}-3\\5\end{bmatrix}$를 선형결합으로 나타내라.

<details>
<summary>해설 보기</summary>

\[
\begin{bmatrix}-3\\5\end{bmatrix}
=
-3\mathbf e_1+5\mathbf e_2
\]

이다. 첫 계수가 첫 좌표, 둘째 계수가 둘째 좌표가 된다.

</details>

### 4. span 소속 방정식

\[
\mathbf v_1=
\begin{bmatrix}1\\2\end{bmatrix},
\qquad
\mathbf v_2=
\begin{bmatrix}2\\1\end{bmatrix},
\qquad
\mathbf b=
\begin{bmatrix}5\\4\end{bmatrix}
\]

일 때 $c_1\mathbf v_1+c_2\mathbf v_2=\mathbf b$를 풀어 $\mathbf b$의 span 소속 여부를 판단하라.

<details>
<summary>해설 보기</summary>

성분별 방정식은

\[
c_1+2c_2=5,
\qquad
2c_1+c_2=4
\]

이다. 첫 식에서 $c_1=5-2c_2$이고 둘째 식에 대입하면 $10-4c_2+c_2=4$다. 따라서 $c_2=2$, $c_1=1$이다.

\[
\mathbf b=\mathbf v_1+2\mathbf v_2
\]

이므로 $\mathbf b$는 span에 속한다.

</details>

### 5. 중복된 생성 벡터

\[
\mathbf v_1=
\begin{bmatrix}1\\0\end{bmatrix},
\qquad
\mathbf v_2=
\begin{bmatrix}2\\0\end{bmatrix}
\]

일 때 $\begin{bmatrix}4\\0\end{bmatrix}$를 두 가지 다른 선형결합으로 나타내라.

<details>
<summary>해설 보기</summary>

예를 들어

\[
\begin{bmatrix}4\\0\end{bmatrix}
=
4\mathbf v_1+0\mathbf v_2
\]

이고

\[
\begin{bmatrix}4\\0\end{bmatrix}
=
0\mathbf v_1+2\mathbf v_2
\]

이다. $\mathbf v_2=2\mathbf v_1$이므로 생성 방향이 중복되고 계수 표현이 유일하지 않다.

</details>

### 6. 닫힘 확인

$\mathbf x,\mathbf y\in\operatorname{span}\{\mathbf v_1,\mathbf v_2\}$일 때 $2\mathbf x-3\mathbf y$도 같은 span에 속함을 계수로 보이라.

<details>
<summary>해설 보기</summary>

어떤 실수 $a_1,a_2,b_1,b_2$가 있어서

\[
\mathbf x=a_1\mathbf v_1+a_2\mathbf v_2,
\qquad
\mathbf y=b_1\mathbf v_1+b_2\mathbf v_2
\]

라고 쓸 수 있다. 그러면

\[
2\mathbf x-3\mathbf y
=
(2a_1-3b_1)\mathbf v_1
+
(2a_2-3b_2)\mathbf v_2
\]

이다. 새 계수도 실수이므로 결과는 같은 span에 속한다.

</details>

### 7. 모델 연결과 주장 비판

activation $\mathbf h$가 두 방향 $\mathbf f_1,\mathbf f_2$의 span에 속한다는 결과를 얻었다. 다음 두 문장을 각각 판단하라.

1. $\mathbf h=c_1\mathbf f_1+c_2\mathbf f_2$를 만족하는 계수가 적어도 하나 존재한다.
2. 모델은 예측을 만들 때 $\mathbf f_1$과 $\mathbf f_2$를 반드시 인과적으로 사용한다.

<details>
<summary>해설 보기</summary>

첫 문장은 span의 정의이므로 맞다. 두 번째 문장은 span 소속만으로 결론 낼 수 없다. 표현 가능성과 실제 계산에서의 사용은 다른 주장이다. 인과적 사용을 말하려면 해당 방향을 제거하거나 바꾸었을 때 행동이 어떻게 변하는지 조사해야 한다.

</details>

## 단원 요약

- 선형결합은 같은 공간의 벡터들에 실수 계수를 곱해 더한 벡터다.
- 생성공간은 가능한 모든 선형결합의 집합이다.
- 영이 아닌 벡터 하나의 span은 원점을 지나는 직선이다.
- 목표 벡터의 span 소속 여부는 목표를 만드는 계수가 존재하는지 풀어 판단한다.
- 생성 방향이 중복되면 벡터의 선형결합 표현이 유일하지 않을 수 있다.
- 가중합이 특정 span에 속한다는 사실은 표현 가능성을 말하며 인과적 사용을 보장하지 않는다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- 선형결합과 생성공간을 수식으로 정의할 수 있는가?
- 한 벡터와 두 벡터의 span을 기하적으로 설명할 수 있는가?
- 계수 방정식을 풀어 목표 벡터의 span 소속 여부를 판단할 수 있는가?
- 생성 벡터의 개수와 독립 방향의 수가 다를 수 있음을 설명할 수 있는가?
- span 소속과 모델의 인과적 사용을 구분할 수 있는가?

## 다음 단원

- [M02-03 내적, 길이와 각도](M02-03-inner-product-length-angle.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] 선형결합과 생성공간을 집합 표기로 정의했다.
- [x] 직선과 평면의 기하학적 의미를 설명했다.
- [x] span 소속 여부를 작은 연립방정식으로 계산했다.
- [x] 생성과 표현의 유일성을 구분했다.
- [x] 모든 문제에 해설이 있다.
- [x] 표현 가능성과 인과적 사용을 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 선수지식 밖의 체계적인 연립방정식 해법을 요구하지 않는다.
- [x] 내부 링크와 수식 구분자를 확인했다.
