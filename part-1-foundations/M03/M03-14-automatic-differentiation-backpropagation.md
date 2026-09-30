---
id: "M03-14"
title: "자동미분과 역전파"
part: 1
stage: "M03"
status: "완료"
prerequisites:
  - "M01-06"
  - "M03-10"
  - "M03-13"
estimated_time: "130~155분"
---

# M03-14. 자동미분과 역전파

## 이 단원이 필요한 이유

신경망의 gradient는 하나의 거대한 미분 공식을 전개해서 얻지 않는다. 프로그램을 작은 연산으로 나눈 뒤, 각 연산의 값과 국소 미분을 연쇄법칙으로 연결해 계산한다. 이 절차가 자동미분이다. 출력이 scalar인 학습 문제에서는 reverse mode가 많은 파라미터의 gradient를 한 번의 역방향 전달로 계산하며, 이 특별한 사용을 보통 역전파라고 부른다.

자동미분을 이해하면 forward pass, backward pass, 계산 그래프, gradient 누적, detach, checkpointing 같은 구현 용어를 수학식과 연결할 수 있다. 또한 gradient가 맞는지 확인할 때 기호미분, 수치미분, 자동미분의 역할을 혼동하지 않게 된다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- 자동미분을 기호미분·수치미분과 구분할 수 있다.
- 계산 그래프의 node, edge, 국소 미분을 식별할 수 있다.
- forward mode에서 primal과 tangent를 함께 전달할 수 있다.
- reverse mode에서 cotangent를 역순으로 전달할 수 있다.
- 분기한 변수가 여러 경로에 기여할 때 gradient를 합산할 수 있다.
- 역전파를 scalar loss에 대한 reverse-mode 자동미분으로 설명할 수 있다.
- 저장 메모리와 재계산 사이의 tradeoff를 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [M01-06 함수합성과 연쇄법칙](../M01/M01-06-composition-chain-rule.md)
- 선수 단원: [M03-10 total derivative와 differential](M03-10-total-derivative-differential.md)
- 선수 단원: [M03-13 JVP와 VJP](M03-13-jvp-vjp.md)
- 확인 질문: 합성함수의 미분을 국소 미분의 곱으로 나타낼 수 있는가?
- 확인 질문: JVP와 VJP가 계산 그래프를 통과하는 순서를 구분할 수 있는가?

## 기호와 용어

| 표기·용어 | 뜻 |
|---|---|
| primal | 원래 프로그램이 계산하는 값 |
| tangent | 입력 방향에 따른 값의 일차 변화량 |
| cotangent | scalar 출력의 변화에 대한 역방향 민감도 |
| $\dot z$ | 변수 $z$의 tangent |
| $\bar z$ | 변수 $z$에 도착한 cotangent, scalar loss이면 $\partial L/\partial z$ |
| local derivative | 한 연산의 입력과 출력 사이 미분 |
| seed | 자동미분 전달을 시작하는 tangent 또는 cotangent |
| tape | reverse pass에 필요한 연산 순서와 중간값의 기록 |

## 핵심 개념 1. 자동미분은 프로그램에 연쇄법칙을 적용한다

자동미분은 미분 가능한 기본 연산으로 작성된 프로그램과 그 실행값을 이용한다. 덧셈, 곱셈, 지수함수, 행렬곱 같은 각 기본 연산에는 미분 규칙이 있다. 프로그램이 실제로 실행한 연산 순서에 이 규칙을 합성하면 원하는 derivative product를 얻는다.

예를 들어

\[
a=xy,\qquad z=a+x,\qquad L=z^2
\]

는 다음 세 국소 연산으로 나뉜다.

\[
(x,y)\mapsto a=xy,\qquad (a,x)\mapsto z=a+x,\qquad z\mapsto L=z^2.
\]

각 연산의 국소 미분은 짧다.

\[
da=y\,dx+x\,dy,\qquad dz=da+dx,\qquad dL=2z\,dz.
\]

자동미분은 이 관계를 필요한 방향으로 전달한다. 긴 닫힌형식의 미분식을 먼저 만들 필요가 없다.

## 핵심 개념 2. 기호미분·수치미분·자동미분은 목적이 다르다

기호미분은 식을 다른 식으로 변환한다. $d(x^2)/dx=2x$처럼 사람이 읽을 수 있는 도함수 식을 얻는 데 적합하지만, 큰 계산 그래프에서는 식이 반복되어 커질 수 있다.

수치미분은 작은 $\varepsilon$에 대해

\[
\frac{L(\boldsymbol\theta+\varepsilon\mathbf v)-L(\boldsymbol\theta)}{\varepsilon}
\]

로 방향미분을 근사한다. 구현을 검사하는 기준으로 유용하지만 truncation error와 floating-point error가 있으며, 많은 좌표의 gradient를 계산하기에는 비싸다.

자동미분은 실행한 점에서 연쇄법칙으로 derivative product를 계산한다. 기본 연산의 미분 규칙이 정확하다는 전제에서 수치차분 오차를 만들지 않는다. 다만 floating-point 연산 자체의 반올림 오차는 남는다.

## 핵심 개념 3. 계산 그래프는 값의 의존관계를 기록한다

계산 그래프의 node는 입력이나 중간값이고, directed edge는 어떤 값이 다음 연산에 사용되는지를 나타낸다. 앞의 예제에서 $x$는 $a=xy$와 $z=a+x$ 두 경로에 모두 사용된다. 따라서 $x$에 대한 최종 gradient에는 두 경로의 기여가 모두 들어가야 한다.

그래프는 미분 가능한 함수 그 자체와 동일하지 않다. 같은 함수를 서로 다른 연산 순서로 구현할 수 있고, 그때 중간 node와 메모리 사용량도 달라질 수 있다. 자동미분은 선택한 프로그램 경로에 규칙을 적용한다.

## 핵심 개념 4. forward mode는 primal과 tangent를 함께 보낸다

입력 방향 $(\dot x,\dot y)$를 정하면 각 연산은 값과 tangent를 함께 계산한다.

\[
\begin{aligned}
a&=xy, & \dot a&=y\dot x+x\dot y,\\
z&=a+x, & \dot z&=\dot a+\dot x,\\
L&=z^2, & \dot L&=2z\dot z.
\end{aligned}
\]

이는 전체 함수의 JVP를 국소 JVP의 합성으로 계산한 것이다. 한 번의 forward-mode 실행은 한 입력 방향의 영향을 모든 중간값과 출력으로 보낸다. 입력 방향의 수가 적을 때 유리하다.

## 핵심 개념 5. reverse mode는 cotangent를 역순으로 보낸다

scalar $L$에 대해 $\bar L=1$을 seed로 둔다. forward pass에서 계산한 값을 이용해 연산의 역순으로 cotangent를 전달한다.

\[
\bar z=\bar L\frac{\partial L}{\partial z},\qquad
\bar a=\bar z\frac{\partial z}{\partial a},\qquad
\bar x\mathrel{+}=\bar z\frac{\partial z}{\partial x}.
\]

그다음 $a=xy$를 거슬러 간다.

\[
\bar x\mathrel{+}=\bar a\frac{\partial a}{\partial x},\qquad
\bar y\mathrel{+}=\bar a\frac{\partial a}{\partial y}.
\]

$\mathrel{+}=$ 표기는 이미 도착한 기여에 새 경로의 기여를 더한다는 뜻이다. reverse mode는 local VJP를 연속해서 적용한다. 출력이 하나이고 입력이 많을 때 한 번의 reverse pass로 모든 입력 좌표의 gradient를 얻을 수 있다.

## 핵심 개념 6. 역전파는 신경망 loss의 reverse-mode 자동미분이다

신경망 층도 행렬곱, bias 덧셈, 활성화함수 같은 기본 연산의 합성이다. loss $L$이 scalar이면 $\bar L=1$에서 시작해 각 층의 local VJP를 뒤에서 앞으로 적용한다. 이 계산이 역전파이다.

역전파는 optimizer update와 구분해야 한다. 역전파는 $\nabla_{\boldsymbol\theta}L$을 계산한다. SGD나 Adam은 계산된 gradient를 사용해 $\boldsymbol\theta$를 갱신한다. gradient를 계산했다고 파라미터가 자동으로 바뀌는 것은 아니다.

## 핵심 개념 7. reverse mode에는 중간값 저장 비용이 따른다

곱셈 $a=xy$의 역방향 규칙에는 forward 값 $x$와 $y$가 필요하다. ReLU의 역방향 규칙에는 어느 입력이 양수였는지 필요하다. 따라서 reverse mode는 보통 forward pass의 중간값이나 이를 복원할 정보를 저장한다.

모든 값을 저장하면 reverse pass는 빠르지만 메모리를 많이 쓴다. 일부 값만 저장하고 나머지를 다시 계산하면 메모리는 줄고 계산량은 늘어난다. checkpointing은 이 tradeoff를 조절하는 방법이다. 이는 미분식의 정확성을 바꾸는 문제가 아니라 같은 derivative를 어떤 계산·메모리 비용으로 얻는지의 문제이다.

## 예제 1. 한 계산 그래프의 forward mode

### 문제

\[
a=xy,\qquad b=x,\qquad z=a+b,\qquad L=z^2
\]

에서 $(x,y)=(2,3)$이고 입력 방향이 $(\dot x,\dot y)=(1,-1)$이다. $\dot L$을 계산한다.

### 풀이

먼저 primal을 계산한다.

\[
a=6,\qquad b=2,\qquad z=8,\qquad L=64.
\]

tangent를 같은 순서로 전달한다.

\[
\dot a=y\dot x+x\dot y=3-2=1,
\]

\[
\dot b=\dot x=1,\qquad \dot z=\dot a+\dot b=2,
\]

\[
\dot L=2z\dot z=2\cdot 8\cdot 2=32.
\]

### 결과의 의미

$(1,-1)$ 방향으로 입력을 움직일 때 $L$의 일차 변화율은 $32$이다. 이는 전체 gradient와 방향의 내적과 같아야 한다.

## 예제 2. 같은 그래프의 reverse mode

$\bar L=1$에서 시작한다.

\[
\bar z=2z=16,
\]

\[
\bar a=16,\qquad \bar b=16.
\]

$a=xy$에서 오는 기여와 $b=x$에서 오는 기여를 합하면

\[
\bar x=\bar a y+\bar b=16\cdot 3+16=64,
\]

\[
\bar y=\bar a x=16\cdot 2=32.
\]

따라서

\[
\nabla L(2,3)=
\begin{bmatrix}
64\\32
\end{bmatrix}.
\]

forward-mode 결과와 비교하면

\[
\nabla L(2,3)^\top
\begin{bmatrix}
1\\-1
\end{bmatrix}
=64-32=32=\dot L
\]

이다. 두 mode가 같은 derivative를 서로 다른 방향으로 계산했음을 확인할 수 있다.

## 예제 3. 수치차분으로 구현 결과 확인하기

이 함수는

\[
L(x,y)=x^2(y+1)^2
\]

이므로 $(2,3)$에서 gradient는 $(64,32)$이다. 방향 $\mathbf v=(1,-1)^\top$의 중앙차분은

\[
\frac{L((2,3)+\varepsilon\mathbf v)-L((2,3)-\varepsilon\mathbf v)}{2\varepsilon}
\]

이며, 적당히 작은 $\varepsilon$에서 $32$에 가까워진다. 너무 큰 $\varepsilon$은 근사 오차를 키우고 너무 작은 $\varepsilon$은 반올림과 상쇄 오차를 키울 수 있다. 수치차분은 자동미분 결과를 독립적으로 점검하는 도구이지 학습 때 gradient를 계산하는 기본 방식은 아니다.

## 예제 4. 분기에서 gradient가 더해지는 이유

$z=x^2+x$에서는 $x$가 제곱 경로와 항등 경로로 분기한다. reverse mode에서 두 기여는

\[
\bar x=\bar z\cdot 2x+\bar z\cdot 1
\]

로 합쳐진다. $\bar z=1$이면 $dz/dx=2x+1$이다. 한 경로만 남기면 같은 변수의 전체 효과가 아니라 일부 경로의 효과만 계산하게 된다.

## 흔한 오해

### 오해 1. 자동미분은 수치미분을 자동으로 해 주는 방법이다

자동미분은 유한차분으로 함숫값을 여러 번 평가하는 방식이 아니다. 기본 연산의 미분 규칙과 연쇄법칙을 실행 경로에 적용한다.

### 오해 2. 역전파와 gradient descent는 같은 과정이다

역전파는 gradient 계산이고 gradient descent는 그 gradient를 이용한 파라미터 갱신이다. 두 과정은 연속해서 실행될 수 있지만 역할이 다르다.

### 오해 3. 분기한 변수에는 먼저 도착한 gradient만 쓰면 된다

변수가 출력에 영향을 주는 모든 directed path의 기여를 합해야 한다. 누락하면 total derivative가 아니라 일부 경로의 derivative가 된다.

### 오해 4. reverse mode는 원래 함수를 역함수로 바꾼다

reverse라는 말은 cotangent 전달 순서를 가리킨다. 각 연산을 invert할 필요가 없으며, ReLU처럼 역함수가 없는 연산에도 reverse-mode 규칙을 적용할 수 있다.

### 오해 5. 자동미분 gradient는 모든 점에서 의미가 하나로 정해진다

ReLU의 0 같은 비미분점에서는 library가 선택한 convention이 반환된다. 실행된 branch, detach, in-place modification도 결과에 영향을 줄 수 있으므로 프로그램의 미분 가능성과 구현 규칙을 확인해야 한다.

## 연습문제

### 1. 세 미분 방식 구분

$f(x)=\sin(x^2)$의 미분을 식으로 단순화하는 작업, $[f(x+\varepsilon)-f(x)]/\varepsilon$을 계산하는 작업, 실행된 $x^2$와 $\sin$ 연산의 국소 미분을 합성하는 작업을 각각 무엇이라 부르는가?

<details>
<summary>해설 보기</summary>

각각 기호미분, 수치미분, 자동미분이다. 세 방법은 모두 derivative와 관련되지만 결과 형태와 오차, 계산 목적이 다르다.

</details>

### 2. forward-mode 전달

$a=x^2$, $z=\exp(a)$에서 $x=1$, $\dot x=3$이다. $a,z,\dot a,\dot z$를 계산하라.

<details>
<summary>해설 보기</summary>

\[
a=1,\qquad z=e,
\]

\[
\dot a=2x\dot x=6,\qquad \dot z=\exp(a)\dot a=6e.
\]

</details>

### 3. reverse-mode 전달

$a=x^2$, $L=3a$에서 $x=-2$이다. $\bar L=1$에서 시작해 $\bar a$와 $\bar x$를 계산하라.

<details>
<summary>해설 보기</summary>

$\bar a=\bar L\,\partial L/\partial a=3$이다. 이어서

\[
\bar x=\bar a\frac{\partial a}{\partial x}=3(2x)=-12
\]

이다.

</details>

### 4. gradient 누적

$L=x^2+3x$를 $a=x^2$, $b=3x$, $L=a+b$라는 그래프로 계산한다. $x=2$에서 두 경로가 $\bar x$에 주는 기여와 최종값을 구하라.

<details>
<summary>해설 보기</summary>

$\bar L=1$이면 $\bar a=1$, $\bar b=1$이다. $a$ 경로는 $2x=4$, $b$ 경로는 $3$을 기여한다. 따라서 $\bar x=4+3=7$이다.

</details>

### 5. JVP와 VJP 비교

$f:\mathbb R^{1000}\to\mathbb R$의 한 점에서 모든 입력 좌표에 대한 gradient가 필요하다. forward mode와 reverse mode 중 어느 쪽이 보통 더 적은 seed 실행을 요구하는가?

<details>
<summary>해설 보기</summary>

reverse mode는 출력 cotangent seed $1$ 하나로 $1000$개 입력 좌표의 gradient를 얻는다. 좌표별 forward mode를 쓰면 표준기저 방향이 최대 $1000$개 필요하다. 실제 비용은 연산 구조와 메모리 조건에도 좌우된다.

</details>

### 6. 메모리와 재계산

reverse pass에 필요한 모든 activation을 저장하지 않고 일부 구간을 다시 계산하는 방법이 줄이는 비용과 늘리는 비용을 각각 말하라.

<details>
<summary>해설 보기</summary>

저장해야 할 activation memory를 줄이고, reverse pass 전에 일부 forward 연산을 다시 수행하므로 계산량과 실행시간을 늘린다. 미분 대상 함수가 같고 재계산이 일관되다면 목표 derivative는 같다.

</details>

### 7. 모델 주장 비판

“자동미분이 정확한 gradient를 반환했으므로 학습된 모델의 설명도 정확하다”라는 주장의 문제를 설명하라.

<details>
<summary>해설 보기</summary>

자동미분의 정확성은 주어진 프로그램이 계산한 함수의 국소 derivative에 관한 주장이다. gradient가 모델의 인과적 설명인지, 데이터 밖에서도 안정적인지, 사용한 attribution 정의가 적절한지는 별도 문제이다. 비미분점 convention과 구현된 그래프가 의도한 함수와 같은지도 확인해야 한다.

</details>

## 단원 요약

- 자동미분은 기본 연산으로 구성된 프로그램에 연쇄법칙을 적용한다.
- forward mode는 primal과 tangent를 계산 순서대로 전달해 JVP를 구한다.
- reverse mode는 cotangent를 역순으로 전달해 VJP를 구한다.
- 같은 변수가 여러 경로로 사용되면 역방향 기여를 모두 합산한다.
- 역전파는 scalar 신경망 loss에 적용한 reverse-mode 자동미분이다.
- 역전파와 optimizer update는 서로 다른 단계이다.
- reverse mode의 중간값 저장과 재계산 사이에는 memory-compute tradeoff가 있다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- 자동미분을 기호미분·수치미분과 구분할 수 있는가?
- 작은 계산 그래프에서 primal과 tangent를 전달할 수 있는가?
- $\bar L=1$에서 시작해 cotangent를 역순으로 계산할 수 있는가?
- 분기에서 gradient 기여를 합산할 수 있는가?
- 역전파와 optimizer update의 역할을 구분할 수 있는가?
- forward mode와 reverse mode에 필요한 seed 수를 비교할 수 있는가?
- checkpointing의 memory-compute tradeoff를 설명할 수 있는가?

## 다음 단원

- [M03-15 재매개화와 모델 대칭성 입문](M03-15-reparameterization-model-symmetries.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] 자동미분을 기호미분·수치미분과 구분했다.
- [x] 계산 그래프와 국소 미분을 설명했다.
- [x] 같은 예제에서 forward mode와 reverse mode를 대조했다.
- [x] 분기에서 gradient 누적을 계산했다.
- [x] 역전파와 optimizer update를 구분했다.
- [x] 메모리와 재계산의 tradeoff를 밝혔다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 내부 링크와 수식 구분자를 확인했다.
