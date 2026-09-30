---
id: "M03-10"
title: "total derivative와 differential"
part: 1
stage: "M03"
status: "완료"
prerequisites:
  - "M01-10"
  - "M01-12"
  - "M03-07"
estimated_time: "125~150분"
---

# M03-10. total derivative와 differential

## 이 단원이 필요한 이유

편미분은 여러 입력 중 한 좌표만 움직였을 때의 변화율이다. 여러 좌표가 함께 변할 때의 일차 변화는 하나의 선형사상이 맡는다. 이 선형사상이 total derivative다.

신경망의 한 층은 vector를 vector로 보내고, 작은 activation 변화는 다음 층의 작은 변화로 전달된다. total derivative를 함수의 국소 선형근사로 이해하면 연쇄법칙을 선형사상의 합성으로 읽을 수 있다. Jacobian은 다음 단원에서 이 사상을 좌표행렬로 나타낸다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- total derivative를 오차항까지 포함한 국소 선형근사로 정의할 수 있다.
- 편미분, 방향미분과 total derivative의 관계를 설명할 수 있다.
- scalar 출력에서 differential이 covector가 되는 이유를 설명할 수 있다.
- 작은 변화에 대한 일차 출력 변화를 계산하고 실제 변화와 비교할 수 있다.
- 다변수 연쇄법칙을 선형사상의 합성으로 계산할 수 있다.
- 국소 선형근사가 허용하는 민감도 주장과 전역 행동 주장을 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [M01-10 여러 변수와 편미분](../M01/M01-10-multivariable-partial-derivatives.md)
- 선수 단원: [M01-12 Taylor 근사](../M01/M01-12-taylor-approximation.md)
- 선수 단원: [M03-07 쌍대공간과 covector](M03-07-dual-spaces-covectors.md)
- 확인 질문: 좌표별 편미분을 계산할 수 있는가?
- 확인 질문: 일변수 Taylor 일차 근사의 오차가 입력 변화보다 작아진다는 뜻을 설명할 수 있는가?
- 확인 질문: differential과 gradient를 타입으로 구분할 수 있는가?

편미분이나 differential이 불분명하면 선수 단원을 먼저 복습한다.

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | 타입·shape |
|---|---|---|---|
| $f:\mathbb R^n\to\mathbb R^m$ | `f maps R to the n into R to the m` | vector 입력을 vector 출력으로 보내는 함수 | 입력 $n$, 출력 $m$ |
| $\mathbf x$ | `x` | 선형화 기준점 | $\mathbb R^n$ |
| $\mathbf h$ | `h` | 기준점에 더하는 작은 변화벡터 | $\mathbb R^n$ |
| $Df(\mathbf x)$ | `D f at x` | $\mathbf x$에서의 total derivative | $\mathbb R^n\to\mathbb R^m$ 선형사상 |
| $df_{\mathbf x}$ | `d f at x` | differential | 이 단원에서는 $Df(\mathbf x)$와 같은 선형근사 |
| $\mathbf r(\mathbf h)$ | `r of h` | 일차근사 뒤에 남는 오차 | $\mathbb R^m$ |
| $o(\|\mathbf h\|)$ | `little o of the norm of h` | $\|\mathbf h\|$보다 빠르게 작아지는 오차 | 비율이 0으로 간다. |

## 핵심 개념 1. total derivative는 가장 잘 맞는 선형근사다

$f:\mathbb R^n\to\mathbb R^m$가 $\mathbf x$에서 미분 가능하다는 말은 선형사상

\[
L:\mathbb R^n\to\mathbb R^m
\]

이 존재해

\[
f(\mathbf x+\mathbf h)
=
f(\mathbf x)+L(\mathbf h)+\mathbf r(\mathbf h)
\]

이고

\[
\lim_{\mathbf h\to\mathbf 0}
\frac{\|\mathbf r(\mathbf h)\|}
{\|\mathbf h\|}
=
0
\]

이 성립한다는 뜻이다. 이 선형사상 $L$을

\[
Df(\mathbf x)
\]

로 쓴다.

따라서

\[
f(\mathbf x+\mathbf h)
\approx
f(\mathbf x)+Df(\mathbf x)(\mathbf h)
\]

이다. 근사 오차는 입력 변화의 크기보다 더 빠르게 작아진다. 이는 오차의 절댓값만 작다는 조건보다 강하다.

## 핵심 개념 2. total derivative는 하나의 선형사상이다

입력 변화 두 개와 scalar에 대해

\[
Df(\mathbf x)(\alpha\mathbf h_1+\beta\mathbf h_2)
=
\alpha Df(\mathbf x)(\mathbf h_1)
+
\beta Df(\mathbf x)(\mathbf h_2)
\]

가 성립한다.

$f$ 자체가 비선형이어도 한 점에서의 total derivative는 선형이다. 기준점 $\mathbf x$를 바꾸면 derivative도 달라질 수 있다.

total derivative는 변화벡터를 출력 변화벡터로 보낸다.

\[
\underbrace{\mathbf h}_{n\times1}
\longmapsto
\underbrace{Df(\mathbf x)(\mathbf h)}_{m\times1}
\]

다음 단원에서는 선택한 표준기저에서 이 선형사상을 $m\times n$ Jacobian 행렬로 나타낸다.

## 핵심 개념 3. 편미분은 total derivative의 좌표축 출력이다

$\mathbf e_j$를 입력공간의 $j$번째 표준기저벡터라 하자. $f$가 미분 가능하면

\[
Df(\mathbf x)(\mathbf e_j)
=
\frac{\partial f}{\partial x_j}(\mathbf x)
\]

이다. 오른쪽은 $m$개 출력 성분의 $x_j$ 편미분을 모은 vector다.

임의의 변화

\[
\mathbf h
=
\sum_{j=1}^{n}h_j\mathbf e_j
\]

에 대해 선형성으로

\[
Df(\mathbf x)(\mathbf h)
=
\sum_{j=1}^{n}
h_j
\frac{\partial f}{\partial x_j}(\mathbf x)
\]

를 얻는다. total derivative는 좌표별 편미분 출력들을 변화량 $h_j$로 선형결합한다.

한 점에서 모든 편미분이 존재한다는 조건만으로 total derivative의 존재가 보장되지는 않는다. 편미분들이 점 주변에서 연속이면 미분 가능성을 보장하는 충분조건을 얻는다.

## 핵심 개념 4. 방향미분은 total derivative에 방향을 넣은 값이다

방향벡터 $\mathbf v$에 대한 방향미분을

\[
D_{\mathbf v}f(\mathbf x)
=
\lim_{t\to0}
\frac{f(\mathbf x+t\mathbf v)-f(\mathbf x)}{t}
\]

로 정의한다. $f$가 $\mathbf x$에서 미분 가능하면

\[
D_{\mathbf v}f(\mathbf x)
=
Df(\mathbf x)(\mathbf v)
\]

이다.

total derivative 하나를 알면 모든 방향미분을 계산할 수 있다. 반대로 여러 방향미분이 따로 존재해도 방향에 대한 의존성이 하나의 선형사상으로 묶이지 않으면 total derivative가 존재하지 않을 수 있다.

## 핵심 개념 5. scalar 출력의 differential은 covector다

$m=1$이면

\[
Df(\mathbf x):\mathbb R^n\to\mathbb R
\]

이므로 total derivative는 covector다. 이 경우

\[
df_{\mathbf x}(\mathbf h)
=
Df(\mathbf x)(\mathbf h)
\]

라고 쓴다.

표준 Euclidean 좌표에서는

\[
df_{\mathbf x}(\mathbf h)
=
\nabla f(\mathbf x)^\top\mathbf h
\]

이다. 왼쪽은 covector가 변화벡터에 작용한 scalar이고, 오른쪽은 Euclidean 내적으로 같은 작용을 표현한 식이다.

vector 출력에서는 $Df(\mathbf x)(\mathbf h)\in\mathbb R^m$이다. 각 출력 성분 $f_i$의 differential을 쌓아 vector 변화를 만든다.

## 핵심 개념 6. 연쇄법칙은 선형근사의 합성이다

\[
f:\mathbb R^n\to\mathbb R^m,
\qquad
g:\mathbb R^m\to\mathbb R^p
\]

이고 두 함수가 해당 점에서 미분 가능하다고 하자. 합성함수는

\[
g\circ f:\mathbb R^n\to\mathbb R^p
\]

이고 total derivative는

\[
D(g\circ f)(\mathbf x)
=
Dg(f(\mathbf x))
\circ
Df(\mathbf x)
\]

이다.

입력 변화 $\mathbf h$는 먼저

\[
Df(\mathbf x)(\mathbf h)
\]

로 중간 출력 변화가 되고, 그 변화는

\[
Dg(f(\mathbf x))
\left(
Df(\mathbf x)(\mathbf h)
\right)
\]

로 최종 출력 변화가 된다. 연쇄법칙의 순서는 forward pass의 함수 적용 순서와 같다.

## 예제 1. vector 함수의 일차 변화

### 문제

\[
f(x,y)
=
\begin{bmatrix}
x^2+xy\\
e^y
\end{bmatrix}
\]

이고 기준점과 변화가

\[
\mathbf x=
\begin{bmatrix}
1\\0
\end{bmatrix},
\qquad
\mathbf h=
\begin{bmatrix}
0.01\\-0.02
\end{bmatrix}
\]

일 때 total derivative가 예측하는 출력 변화를 구하고 실제 변화와 비교하라.

### 풀이

첫 출력의 편미분은

\[
\frac{\partial f_1}{\partial x}=2x+y,
\qquad
\frac{\partial f_1}{\partial y}=x
\]

이고 둘째 출력의 편미분은

\[
\frac{\partial f_2}{\partial x}=0,
\qquad
\frac{\partial f_2}{\partial y}=e^y
\]

이다. 기준점에서 derivative의 좌표행렬은

\[
\begin{bmatrix}
2&1\\
0&1
\end{bmatrix}
\]

이므로 일차 변화는

\[
Df(\mathbf x)(\mathbf h)
=
\begin{bmatrix}
2&1\\
0&1
\end{bmatrix}
\begin{bmatrix}
0.01\\-0.02
\end{bmatrix}
=
\begin{bmatrix}
0\\-0.02
\end{bmatrix}
\]

이다.

실제 첫 출력은

\[
(1.01)^2+(1.01)(-0.02)
=
1.0201-0.0202
=
0.9999
\]

이므로 변화는 $-0.0001$이다. 둘째 출력 변화는

\[
e^{-0.02}-1
\approx
-0.0198013
\]

이다. 일차근사의 오차는

\[
\begin{bmatrix}
-0.0001\\
0.0001987
\end{bmatrix}
\]

정도다.

### 결과의 의미

total derivative는 두 입력좌표의 변화를 함께 받아 두 출력의 일차 변화를 만든다. 남은 오차는 이 예제에서 변화량의 제곱 크기와 같은 수준이다.

## 예제 2. scalar differential과 gradient

\[
\ell(x,y)=x^2y+\sin y
\]

라 하자. 편미분은

\[
\frac{\partial\ell}{\partial x}=2xy,
\qquad
\frac{\partial\ell}{\partial y}=x^2+\cos y
\]

이다. 점 $(1,0)$에서

\[
d\ell_{(1,0)}(\mathbf h)
=
\begin{bmatrix}
0&2
\end{bmatrix}
\mathbf h
\]

이다. Euclidean gradient는 같은 계수를 열로 세운

\[
\nabla\ell(1,0)
=
\begin{bmatrix}
0\\2
\end{bmatrix}
\]

이다.

\[
\mathbf h=
\begin{bmatrix}
0.1\\-0.05
\end{bmatrix}
\]

이면 일차 손실 변화는

\[
d\ell_{(1,0)}(\mathbf h)=-0.1
\]

이다. 이 값은 지정한 기준점과 작은 변화에 대한 국소 예측이다.

## 예제 3. 연쇄법칙을 사상 합성으로 계산하기

\[
f(x,y)
=
\begin{bmatrix}
x+y\\
xy
\end{bmatrix},
\qquad
g(u,v)=u^2+v
\]

라 하자. 점 $(1,2)$에서 $f(1,2)=(3,2)^\top$이다.

$f$의 derivative 행렬은

\[
Df(1,2)
\longleftrightarrow
\begin{bmatrix}
1&1\\
2&1
\end{bmatrix}
\]

이고 $g$의 derivative 행은

\[
Dg(3,2)
\longleftrightarrow
\begin{bmatrix}
6&1
\end{bmatrix}
\]

이다. 합성의 derivative는

\[
D(g\circ f)(1,2)
\longleftrightarrow
\begin{bmatrix}
6&1
\end{bmatrix}
\begin{bmatrix}
1&1\\
2&1
\end{bmatrix}
=
\begin{bmatrix}
8&7
\end{bmatrix}
\]

이다.

직접 합성하면

\[
(g\circ f)(x,y)
=(x+y)^2+xy
\]

이고 편미분은

\[
\frac{\partial(g\circ f)}{\partial x}
=
2(x+y)+y
\]

\[
\frac{\partial(g\circ f)}{\partial y}
=
2(x+y)+x
\]

이므로 $(1,2)$에서 8과 7을 얻는다.

## 예제 4. 편미분은 있지만 미분 가능하지 않은 함수

\[
f(x,y)
=
\begin{cases}
\dfrac{xy}{\sqrt{x^2+y^2}},
&
(x,y)\ne(0,0),\\
0,
&
(x,y)=(0,0)
\end{cases}
\]

라 하자. 두 좌표축에서는 함수값이 0이므로

\[
\frac{\partial f}{\partial x}(0,0)=0,
\qquad
\frac{\partial f}{\partial y}(0,0)=0
\]

이다.

total derivative가 존재한다면 두 편미분 때문에 후보 선형사상은 영사상이어야 한다. 그러나 $\mathbf h=(t,t)^\top$에서

\[
f(t,t)
=
\frac{t^2}{\sqrt{2t^2}}
=
\frac{|t|}{\sqrt2}
\]

이고

\[
\frac{|f(t,t)|}{\|(t,t)^\top\|_2}
=
\frac{|t|/\sqrt2}{\sqrt2|t|}
=
\frac12
\]

다. 이 비율은 0으로 가지 않으므로 원점에서 미분 가능하지 않다.

## 예제 5. 신경망 층의 국소 변화

한 층을

\[
\mathbf h^{(\ell+1)}
=
f_\ell(\mathbf h^{(\ell)})
\]

로 쓰자. 현재 activation에 작은 변화 $\Delta\mathbf h^{(\ell)}$를 주면

\[
\Delta\mathbf h^{(\ell+1)}
\approx
Df_\ell(\mathbf h^{(\ell)})
\left(
\Delta\mathbf h^{(\ell)}
\right)
\]

이다. 여러 층에서는 각 derivative를 합성해 입력 변화가 뒤쪽 activation에 전달되는 일차 효과를 계산한다.

이 근사는 기준 activation 주변의 작은 변화에 적용된다. 큰 perturbation이나 activation 분포 밖의 개입에서는 고차항이 커질 수 있으므로 실제 forward pass와 비교해야 한다.

## 흔한 오해

### 오해 1. total derivative는 편미분을 모두 적은 목록이다

편미분은 좌표축 방향의 출력 변화다. total derivative는 임의의 작은 변화벡터를 출력 변화벡터로 보내는 하나의 선형사상이다.

### 오해 2. 모든 편미분이 존재하면 미분 가능하다

한 점에서 편미분이 존재해도 하나의 선형근사가 모든 접근 방향의 오차를 통제하지 못할 수 있다.

### 오해 3. differential과 gradient는 같은 타입이다

scalar 함수의 differential은 covector다. gradient는 선택한 내적으로 그 covector를 나타낸 vector다.

### 오해 4. derivative가 크면 먼 입력에서도 같은 변화가 난다

derivative는 기준점 주변의 일차 민감도다. 기준점에서 멀어지면 derivative 자체와 고차항이 달라질 수 있다.

## 연습문제

### 1. 정의 읽기

\[
\lim_{\mathbf h\to\mathbf 0}
\frac{
\|f(\mathbf x+\mathbf h)-f(\mathbf x)-L(\mathbf h)\|
}{
\|\mathbf h\|
}
=
0
\]

을 한국어 문장으로 설명하라.

<details>
<summary>해설 보기</summary>

$f$의 실제 출력 변화에서 선형예측 $L(\mathbf h)$를 뺀 오차를 입력 변화의 크기로 나눈 비율이 $\mathbf h\to\mathbf 0$일 때 0으로 간다는 뜻이다. 이 조건을 만족하는 선형사상 $L$이 total derivative다.

</details>

### 2. scalar differential

\[
f(x,y)=x^2y+\sin y
\]

의 $(1,0)$에서 differential을 구하고 $\mathbf h=(0.1,-0.05)^\top$에 적용하라.

<details>
<summary>해설 보기</summary>

\[
\frac{\partial f}{\partial x}=2xy,
\qquad
\frac{\partial f}{\partial y}=x^2+\cos y
\]

이므로 $(1,0)$에서 행 좌표는 $(0,2)$다. 따라서

\[
df_{(1,0)}(\mathbf h)
=
\begin{bmatrix}
0&2
\end{bmatrix}
\begin{bmatrix}
0.1\\-0.05
\end{bmatrix}
=
-0.1
\]

이다.

</details>

### 3. vector 함수의 derivative

\[
f(x,y)
=
\begin{bmatrix}
x+y\\
xy
\end{bmatrix}
\]

에서 $(1,2)$의 total derivative를 좌표행렬로 나타내고 $\mathbf h=(3,-1)^\top$에 적용하라.

<details>
<summary>해설 보기</summary>

첫 출력의 편미분은 $(1,1)$이고 둘째 출력의 편미분은 $(y,x)$다. 따라서

\[
Df(1,2)
\longleftrightarrow
\begin{bmatrix}
1&1\\
2&1
\end{bmatrix}
\]

이다.

\[
Df(1,2)(\mathbf h)
=
\begin{bmatrix}
1&1\\
2&1
\end{bmatrix}
\begin{bmatrix}
3\\-1
\end{bmatrix}
=
\begin{bmatrix}
2\\5
\end{bmatrix}
\]

이다.

</details>

### 4. remainder 확인

$f(x)=x^2$를 $x=2$에서 선형화하고 remainder가 미분 가능성 조건을 만족함을 확인하라.

<details>
<summary>해설 보기</summary>

\[
f(2+h)
=(2+h)^2
=
4+4h+h^2
\]

이므로 선형항은 $L(h)=4h$이고 remainder는 $r(h)=h^2$다.

\[
\frac{|r(h)|}{|h|}
=
|h|
\to0
\]

이므로 total derivative의 정의를 만족한다.

</details>

### 5. 방향미분

$Df(\mathbf x)$의 좌표행렬이

\[
\begin{bmatrix}
1&2\\
-1&3
\end{bmatrix}
\]

일 때 $\mathbf v=(2,-1)^\top$ 방향의 변화율 vector를 구하라.

<details>
<summary>해설 보기</summary>

\[
D_{\mathbf v}f(\mathbf x)
=
Df(\mathbf x)(\mathbf v)
=
\begin{bmatrix}
1&2\\
-1&3
\end{bmatrix}
\begin{bmatrix}
2\\-1
\end{bmatrix}
=
\begin{bmatrix}
0\\-5
\end{bmatrix}
\]

이다.

</details>

### 6. 연쇄법칙

$Df(\mathbf x):\mathbb R^2\to\mathbb R^3$와 $Dg(f(\mathbf x)):\mathbb R^3\to\mathbb R$가 주어졌을 때 합성 derivative의 입력·출력 공간과 사상 순서를 적어라.

<details>
<summary>해설 보기</summary>

합성 derivative는

\[
D(g\circ f)(\mathbf x)
=
Dg(f(\mathbf x))\circ Df(\mathbf x)
:
\mathbb R^2\to\mathbb R
\]

이다. 변화벡터는 먼저 $Df(\mathbf x)$를 거쳐 $\mathbb R^3$의 변화가 되고, 그다음 $Dg(f(\mathbf x))$를 거쳐 scalar 변화가 된다.

</details>

### 7. 모델 주장 비판

“한 입력에서 derivative가 작으므로 이 모델은 모든 입력 perturbation에 안정적이다”라는 문장을 비판하라.

<details>
<summary>해설 보기</summary>

한 점의 derivative는 그 점 주변의 작은 변화에 대한 일차 민감도다. 다른 입력에서는 derivative가 달라질 수 있고, 큰 perturbation에서는 고차항과 영역 이동이 영향을 준다. 안정성을 주장하려면 입력 집합, perturbation 크기와 norm을 정하고 여러 점의 실제 출력 변화를 평가해야 한다.

</details>

## 단원 요약

- total derivative는 함수의 실제 변화와의 오차가 입력 변화보다 빠르게 작아지는 선형근사다.
- 편미분은 total derivative가 표준기저벡터를 보낸 출력이다.
- 함수가 미분 가능하면 방향미분은 total derivative에 방향벡터를 넣어 계산한다.
- scalar 출력의 differential은 covector이고 gradient는 내적을 이용한 vector 표현이다.
- 다변수 연쇄법칙은 각 함수의 total derivative를 합성한다.
- 국소 derivative만으로 큰 perturbation이나 전역 안정성을 결론 내릴 수 없다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- total derivative를 remainder 조건과 함께 정의할 수 있는가?
- 편미분과 total derivative의 관계를 설명할 수 있는가?
- 변화벡터의 일차 출력 변화를 계산할 수 있는가?
- differential과 gradient를 구분할 수 있는가?
- 연쇄법칙을 선형사상 합성으로 쓸 수 있는가?
- 편미분의 존재만으로 미분 가능성이 보장되지 않는 이유를 설명할 수 있는가?
- 국소 민감도 주장의 범위를 제한할 수 있는가?

## 다음 단원

- [M03-11 Jacobian](M03-11-jacobian.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] total derivative를 remainder 조건으로 정의했다.
- [x] 편미분과 방향미분을 선형사상과 연결했다.
- [x] scalar differential의 covector 타입을 밝혔다.
- [x] 연쇄법칙을 사상 합성으로 계산했다.
- [x] 편미분만 존재하는 반례를 포함했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 내부 링크와 수식 구분자를 확인했다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
