# 문체와 표기 규칙

이 문서는 모든 본문, 문제, 해설, 실습과 HTML에 적용한다. 특정 단원에서 다른 표기가 꼭 필요하면 최초 사용 지점에서 차이를 설명하고 이 문서의 예외 목록에 기록한다.

## 1. 한국어 문체

### 1.1 기본 어조

- 본문은 `~이다`, `~한다` 평서체로 쓴다.
- `~입니다`와 `~이다`를 섞지 않는다.
- 독자에게 사고나 계산을 요청할 때 `살펴보자`, `계산해보자`를 제한적으로 사용한다.
- 친절하게 설명하되 유아적인 말투나 과도한 격려를 사용하지 않는다.
- 독자가 모를 수 있는 내용을 `쉽다`, `당연하다`, `자명하다`고 표현하지 않는다.
- 저자를 드러내는 `우리는`은 공동으로 수행하는 계산이나 정의가 분명할 때만 사용한다.

권장:

> 행렬은 숫자의 배열이지만, 이 단원에서는 벡터를 다른 벡터로 바꾸는 선형변환으로 이해한다.

피함:

> 행렬은 사실 아주 간단하다. 그냥 숫자를 네모나게 모아 놓은 것이다.

### 1.2 설명 순서

새 개념은 필요한 범위에서 다음 순서를 따른다.

```text
문제 또는 필요성
→ 직관
→ 정확한 정의
→ 기호 해독
→ 작은 예제
→ 모델에서의 역할
→ 한계와 오해
```

모든 절을 같은 문구로 시작하지 않는다. 설명 순서는 독자의 이해를 위한 기본 순서이며 고정된 문단 공식이 아니다.

개정할 때는 정의·수식·개념 사이에서 생략된 이해 과정을 먼저 보충한다. 정의의 구성요소를 풀어 설명하고, 수식 전개의 이유와 각 항의 관계를 밝히며, 이미 배운 개념에서 새 개념으로 이어지는 연결을 적는다. 비슷한 개념을 구분하는 데 필요한 설명도 본문에 둔다.

필요성·예시·AI 활용·한계를 모든 개념에 반복해서 붙이지 않는다. 예시는 개념 설명에 필요한 경우에만 쓰며 기존 예제를 우선 활용한다. 수학적 조건과 주장 강도는 유지한다. 충분한 문단은 그대로 두고, 분량 증가율이나 항목 수를 채우려고 늘리지 않는다.

본문 개정안을 완성한 뒤 시각화를 설계한다. 전권 설명 보강 단계에서는 새 그림을 제작하지 않고 기존 그림을 보존한다. 캡션·대체 텍스트와 그림 안내 문장은 본문 설명 보강으로 계산하지 않는다. 승인된 M00-03~05의 설명 수준을 참고하되 같은 문단 구조나 길이를 강제하지 않는다.

### 1.3 문장과 문단

- 한 문단은 하나의 설명 기능을 맡는다.
- 문장 길이를 숫자로 제한하지 않는다.
- 조건, 원인, 양보와 대조가 한 번에 읽히지 않으면 문장을 나눈다.
- 짧게 쓰기 위해 논리의 중간 단계를 생략하지 않는다.
- 같은 결론을 도입과 결말에서 표현만 바꿔 반복하지 않는다.
- 항목을 열거하거나 비교할 때 목록과 표를 사용한다.
- 이어지는 논증이나 유도 과정을 전부 글머리표로 분해하지 않는다.
- 대명사의 선행사가 불분명하면 대상의 이름을 다시 쓴다.

### 1.4 직관과 정의

직관적 설명과 수학적 정의를 문장 안에서 구분한다.

- `직관적으로는`: 이해를 돕는 그림이나 비유
- `정확히는`: 수학적 정의나 조건
- `이 단원에서는`: 교육 범위를 제한한 설명
- `이 조건에서는`: 성립 범위를 제한한 주장
- `항상 그런 것은 아니다`: 대표적 예외가 있는 경우

예:

> 직관적으로 gradient는 함수가 가장 빠르게 증가하는 방향이다. 정확히는 선택한 내적을 이용해 differential을 벡터로 나타낸 것이다.

### 1.5 비유

- 비유는 첫 직관을 만드는 데만 사용한다.
- 하나의 개념에 서로 다른 비유를 연달아 붙이지 않는다.
- 비유가 성립하지 않는 지점을 필요한 만큼 밝힌다.
- 비유를 정의나 증거 대신 사용하지 않는다.
- 비유 뒤에는 수식 또는 작은 예제를 둔다.

### 1.6 주장 강도

다음 표현을 구분한다.

| 표현 | 사용 조건 |
|---|---|
| 계산된다 | 정의와 식에서 직접 얻었다. |
| 관찰됐다 | 지정된 데이터와 실험에서 확인했다. |
| 복원할 수 있다 | probe나 decoder가 정보를 읽어냈다. |
| 관련된다 | 상관관계나 조건별 차이가 있다. |
| 시사한다 | 가능한 해석을 지지하지만 단정하지 못한다. |
| 사용한다 | 모델 계산에 기능적으로 관여한다는 개입 증거가 있다. |
| 원인이다 | 개입과 대조군 아래 인과 효과를 확인했다. |
| 일반화된다 | 독립된 데이터, 조건이나 모델에서 평가했다. |

`복원할 수 있다`를 `모델이 사용한다`로 바꾸지 않는다. `activation이 변했다`를 `개념을 학습했다`로 바로 바꾸지 않는다.

### 1.7 피해야 할 표현

다음 표현은 금지어가 아니지만 구체적인 내용 없이 사용하지 않는다.

- 매우 중요하다
- 놀랍게도
- 강력하다
- 혁신적이다
- 본질적으로
- 단순히 말하면
- 완벽하게 이해할 수 있다
- 쉽게 알 수 있다
- 당연히

중요성은 형용사보다 결과로 설명한다.

> Jacobian을 알면 입력의 작은 변화가 다음 층 activation에 어떻게 전달되는지 계산할 수 있다.

### 1.8 한국어와 영어 용어

- 처음 등장할 때 `한국어(영어)`로 쓴다.
- 널리 영어로 사용하는 용어는 영어를 본용어로 둘 수 있다.
- 약어는 최초 등장 때 전체 이름과 함께 정의한다.
- 같은 대상을 단조로움을 피하려고 여러 동의어로 바꾸지 않는다.
- 용어 선택은 [용어집](04-GLOSSARY.md)을 따른다.

예:

```text
활성값(activation)
그래디언트(gradient)
야코비안(Jacobian)
특이값분해(singular value decomposition, SVD)
```

## 2. 수식 설명 원칙

### 2.1 새 수식을 읽는 세 단계

중요한 새 수식은 다음 세 수준으로 설명한다.

1. 기호별 의미와 shape
2. 수식을 한국어 문장으로 읽기
3. 수식이 나타내는 관계와 계산의 역할. 모델이나 분석 수식이면 해당 문맥에서의 역할을 설명한다.

예:

\[
h_{\ell+1}=f_\ell(h_\ell)
\]

- $h_\ell$: $\ell$번째 층의 activation
- $f_\ell$: $\ell$번째 층이 수행하는 함수
- $h_{\ell+1}$: 다음 층의 activation

문장으로 읽으면 현재 activation을 해당 층의 함수에 넣어 다음 activation을 만든다는 뜻이다. 이 식은 신경망의 forward pass 한 단계를 나타낸다.

### 2.2 전개 생략

- 학습 목표인 계산은 중간 단계를 생략하지 않는다.
- 이미 통과한 선수 단원의 단순 계산은 필요한 경우 줄일 수 있다.
- `정리하면`, `계산하면` 뒤에 핵심 변형이 숨어 있으면 그 단계를 펼친다.
- 생략할 때는 어떤 규칙을 적용했는지 적는다.

### 2.3 등호와 근사 기호

- 정확한 등식은 $=$를 쓴다.
- 근사는 $\approx$를 쓴다.
- 정의는 문맥이 불명확할 때 $\coloneqq$를 쓴다.
- 비례관계는 $\propto$를 쓴다.
- 모양만 같다는 이유로 등호를 사용하지 않는다.

### 2.4 English mathematical reading

`기호와 용어` 표의 두 번째 열 이름은 `Common spoken reading`으로 통일한다. 이 열은 기호를 영어권 강의나 연구 발표에서 소리 내어 읽을 때 쓸 짧은 대표 발화를 제공한다. 전체 문구를 Markdown 백틱으로 감싸며 영어만 쓴다.

읽기와 뜻은 서로 다른 정보다.

| 항목 | 내용 |
|---|---|
| 기호·용어 | 화면에 적힌 수식이나 용어 |
| Common spoken reading | 실제로 말할 짧은 영어 발화 하나 |
| 의미 | 수학적 정의, 조건과 문맥을 설명하는 한국어 |

`arg max over x of f of x`는 읽기다. `the argument that maximizes f of x`는 뜻을 설명하는 문장이므로 읽기 열에 넣지 않는다.

#### 2.4.1 구성별 원칙

- 첨자는 `sub`로 읽는다: $w_i$는 `w sub i`, $A_{ij}$는 `A sub i j`이다.
- 제곱과 세제곱은 `squared`, `cubed`로 읽고 일반 거듭제곱은 `to the n`처럼 읽는다.
- 함수 적용은 `of`를 쓴다: $f(x)$는 `f of x`, $log(x)$는 `log of x`이다.
- $exp(x)$의 대표 읽기는 `the exponential of x`이다. $e^x$를 강조하는 문맥에서는 `e to the x`도 가능하다.
- 일변수 미분은 `d f over d x`, 편미분은 `partial f over partial x`로 읽는다. 변수를 문장으로 강조할 때는 `with respect to x`를 쓸 수 있다.
- gradient는 `the gradient of f with respect to x`, Jacobian은 `the Jacobian of f at x`처럼 대상과 기준점을 밝힌다.
- 범위가 있는 합은 `sum over i from one to n of ...`로 읽는다. 적분은 `the integral from a to b of ... d x`로 읽는다.
- 조건부확률과 조건부분포는 `given`을 쓴다: $P(A\mid B)$는 `P of A given B`이다.
- 기댓값과 분산은 각각 `the expectation of X`, `the variance of X`로 읽는다.
- transpose, inverse, determinant, trace와 rank는 해당 영어 연산명을 쓴다.
- norm은 종류를 밝힌다: $\|x\|_2$는 `the L two norm of x`이다.
- 최적화 기호는 `arg max over ...`, `arg min over ...`, `max over ...`, `min over ...`로 시작한다.
- entropy는 `H of p`, KL divergence는 방향을 포함해 `K L divergence from p to q`로 읽는다.
- 그리스 문자는 `theta`, `lambda`, `sigma`, `epsilon`처럼 영어 이름을 쓴다. 대문자와 소문자를 구분해야 할 때만 `capital`을 붙인다.
- initialism은 통상적인 글자 이름으로 읽는다. 이 교재에서는 `K L`, `M L E`, `H V P`, `N L L`처럼 공백으로 글자를 구분해 적는다.

#### 2.4.2 대표 표준

| 기호 | Common spoken reading |
|---|---|
| $f(x)$ | `f of x` |
| $w_i$ | `w sub i` |
| $w_{ij}$ | `w sub i j` |
| $x^2$ | `x squared` |
| $x^3$ | `x cubed` |
| $x^n$ | `x to the n` |
| $\mathbb R^n$ | `R to the n` |
| $W^\top$ | `W transpose` |
| $A^{-1}$ | `A inverse` |
| $\det(A)$ | `the determinant of A` |
| $\operatorname{rank}(A)$ | `the rank of A` |
| $\|x\|_2$ | `the L two norm of x` |
| $p(y\mid x)$ | `p of y given x` |
| $\mathbb E[X]$ | `the expectation of X` |
| $\sum_{i=1}^n x_i$ | `sum over i from one to n of x sub i` |
| $\frac{df}{dx}$ | `d f over d x` |
| $\frac{\partial f}{\partial x}$ | `partial f over partial x` |
| $\nabla_x f$ | `the gradient of f with respect to x` |
| $\arg\max_x f(x)$ | `arg max over x of f of x` |
| $\exp(x)$ | `the exponential of x` |
| $f:\mathbb R^n\to\mathbb R^m$ | `f maps R to the n into R to the m` |
| $X\sim\mathcal N(\mu,\sigma^2)$ | `X is normally distributed with mean mu and variance sigma squared` |
| $D_{\mathrm{KL}}(p\Vert q)$ | `K L divergence from p to q` |

#### 2.4.3 허용되는 차이와 금지 사례

한 기호와 같은 문맥에는 위 표의 대표 읽기 하나를 사용한다. 수식이 다른 정보를 강조할 때만 다른 읽기를 허용한다. 예를 들어 $\exp(x)$는 표에서 `the exponential of x`로 통일하지만, 본문에서 $\exp(x)=e^x$를 설명할 때 `e to the x`라고 말할 수 있다. 약어의 발음이 연구 공동체마다 갈리면 이 절에 근거를 기록한 뒤 하나를 선택한다.

다음은 사용하지 않는다.

- `더블유 아래 아이`, `익스프레스 엑스` 같은 한글 음역
- `x below i`, `x under i`, `x upper two` 같은 위치 직역
- `open parenthesis`, `close parenthesis`처럼 기호 모양을 순서대로 읽는 표현
- 정의 전체나 긴 해설을 Common spoken reading에 넣는 방식
- 같은 기호와 문맥에 서로 다른 대표 읽기를 쓰는 방식

## 3. 수학 객체의 표기

### 3.1 기본 표기

| 대상 | 표기 | 예 |
|---|---|---|
| scalar | 이탤릭 소문자 | $x,\alpha,\ell$ |
| vector | 굵은 소문자 | $\mathbf{x},\mathbf{h}$ |
| matrix | 굵은 대문자 | $\mathbf{W},\mathbf{H}$ |
| tensor | 굵은 대문자 또는 calligraphic | $\mathbf{A},\mathcal T$ |
| 집합·공간 | 대문자 또는 blackboard bold | $V,\mathbb R^d$ |
| 함수 | 소문자 | $f,g,p$ |
| 선형사상 | 대문자 | $T:V\to W$ |
| 확률변수 | 대문자 | $X,Y,H$ |
| 관측값 | 소문자 | $x,y,h$ |
| 파라미터 | 그리스 문자 | $\theta,\phi$ |
| loss | calligraphic | $\mathcal L$ |

본문에서 굵은 수학 글꼴이 오히려 초심자의 독해를 방해하는 짧은 예제에서는 $x=(1,2)$처럼 쓸 수 있다. 같은 식 안에서는 scalar와 vector 표기를 혼동하지 않는다.

### 3.2 벡터 방향과 데이터 행렬

이론 설명에서 개별 벡터는 기본적으로 열벡터다.

\[
\mathbf y=\mathbf W\mathbf x+\mathbf b,
\qquad
\mathbf W\in\mathbb R^{d_{\mathrm{out}}\times d_{\mathrm{in}}}
\]

데이터나 token 여러 개를 쌓은 행렬은 각 행이 하나의 관측 벡터의 전치가 되도록 둔다.

\[
\mathbf H
=
\begin{bmatrix}
\mathbf h_1^\top\\
\vdots\\
\mathbf h_T^\top
\end{bmatrix}
\in\mathbb R^{T\times d}
\]

따라서 같은 선형변환을 행 단위 데이터에 적용하면

\[
\mathbf Y=\mathbf X\mathbf W^\top+{\mathbf 1}\mathbf b^\top
\]

가 된다. PyTorch나 attention 구현에서 다른 weight shape 관례를 사용하면 해당 단원에서 코드 관례를 별도로 밝힌다.

### 3.3 shape 표기

- shape은 처음 등장할 때 수식 옆에 쓴다.
- dimension 이름은 가능하면 의미를 드러낸다.
- 단일 sequence와 batch를 섞지 않는다.

기본 기호:

| 기호 | 의미 |
|---|---|
| $B$ | batch size |
| $T$ | token 또는 sequence 길이 |
| $d$ | 일반 feature dimension |
| $d_{\mathrm{model}}$ | Transformer hidden dimension |
| $d_k,d_v$ | key와 value dimension |
| $C$ | class 또는 vocabulary size |
| $L$ | layer 수 |
| $H$ | attention head 수. 확률변수나 activation 행렬과 혼동될 때 다른 글자를 쓴다. |

Transformer activation은 기본적으로

\[
\mathbf H^{(\ell)}\in\mathbb R^{B\times T\times d_{\mathrm{model}}}
\]

로 쓴다. batch를 생략할 때는 생략 사실을 적고 $T\times d_{\mathrm{model}}$로 쓴다.

### 3.4 인덱스

| 인덱스 | 기본 의미 |
|---|---|
| $i,j$ | 일반 원소, feature 또는 class |
| $n$ | sample |
| $b$ | batch |
| $t,s$ | token position 또는 time |
| $\ell,m$ | layer |
| $a$ | attention head. $h$와 hidden state의 혼동을 피한다. |

다른 의미로 사용할 때는 해당 식 앞에서 정의한다.

## 4. 미분 표기

### 4.1 scalar 함수

일변수 함수는

\[
f'(x)=\frac{df}{dx}
\]

를 사용한다.

여러 변수의 scalar 함수 $f:\mathbb R^n\to\mathbb R$는

\[
\frac{\partial f}{\partial x_i},
\qquad
\nabla_{\mathbf x}f\in\mathbb R^n
\]

로 쓴다.

### 4.2 differential과 gradient

- $df_{\mathbf x}$는 $\mathbf x$에서의 differential이다.
- $\nabla_{\mathbf x}f$는 선택한 내적 아래 differential에 대응하는 gradient vector다.
- 입문 단원에서는 둘의 차이를 필요한 수준까지만 설명하고, M03-07에서 엄밀히 구분한다.

### 4.3 Jacobian


\[
f:\mathbb R^n\to\mathbb R^m
\]

이면 Jacobian은 출력 성분을 행, 입력 성분을 열로 둔다.

\[
\mathbf J_f(\mathbf x)
=
\left[
\frac{\partial f_i}{\partial x_j}
\right]
\in\mathbb R^{m\times n}
\]

따라서 국소 선형화는

\[
f(\mathbf x+\Delta\mathbf x)
\approx
f(\mathbf x)+\mathbf J_f(\mathbf x)\Delta\mathbf x
\]

로 쓴다.

### 4.4 Hessian

scalar 함수 $f:\mathbb R^n\to\mathbb R$의 Hessian은

\[
\mathbf H_f(\mathbf x)
=
\left[
\frac{\partial^2 f}{\partial x_i\partial x_j}
\right]
\in\mathbb R^{n\times n}
\]

로 쓴다. activation 행렬 $\mathbf H$와 혼동될 때 본문에서 `Hessian`이라고 병기한다.

### 4.5 JVP와 VJP

- JVP: $\mathbf J_f(\mathbf x)\mathbf v$
- VJP의 열벡터 표현: $\mathbf J_f(\mathbf x)^\top\mathbf u$

프레임워크 API가 행 covector 표기를 사용하면 대응 관계를 설명한다.

## 5. 확률과 정보이론 표기

- 확률변수는 대문자 $X$, 관측값은 소문자 $x$로 쓴다.
- 분포는 $p(x)$, 조건부분포는 $p(y\mid x)$로 쓴다.
- 기대값은 분포를 필요한 경우 아래첨자로 명시한다.

\[
\mathbb E_{X\sim p}[f(X)]
\]

- $\log$는 별도 언급이 없으면 자연로그다.
- entropy는 $\mathrm H(p)$, cross entropy는 $\mathrm H(p,q)$ 또는 $\mathcal L_{\mathrm{CE}}$로 쓴다.
- KL divergence는 방향을 생략하지 않는다.

\[
D_{\mathrm{KL}}(p\Vert q)
=
\sum_x p(x)\log\frac{p(x)}{q(x)}
\]

- 모델 예측은 $p_\theta(y\mid x)$로 쓴다.
- teacher와 student가 함께 나오면 $p_T$, $p_S$를 사용하고 temperature는 $\tau$를 사용한다.

## 6. 선형대수 표기

- transpose는 $(\cdot)^\top$를 쓴다.
- inverse는 $(\cdot)^{-1}$를 쓰되 존재 조건을 확인한다.
- pseudoinverse는 $(\cdot)^+$를 쓴다.
- Euclidean norm은 $\|\mathbf x\|_2$, Frobenius norm은 $\|\mathbf A\|_F$로 쓴다.
- 내적은 $\langle\mathbf x,\mathbf y\rangle$ 또는 $\mathbf x^\top\mathbf y$를 사용한다.
- span은 $\operatorname{span}\{\cdot\}$, kernel은 $\ker(T)$, image는 $\operatorname{im}(T)$로 쓴다.
- rank는 $\operatorname{rank}(\mathbf A)$로 쓴다.
- identity matrix는 $\mathbf I_d$, all-ones vector는 $\mathbf 1$로 쓴다.

SVD는

\[
\mathbf A=\mathbf U\boldsymbol\Sigma\mathbf V^\top
\]

로 통일한다. singular value는 $\sigma_1\ge\sigma_2\ge\cdots\ge0$ 순서로 둔다.

## 7. 신경망과 모델 해석 표기

### 7.1 층과 activation

\[
\mathbf h^{(\ell+1)}
=
f_\ell\bigl(\mathbf h^{(\ell)}\bigr)
\]

- 위첨자 괄호 $(\ell)$는 layer를 나타낸다.
- 거듭제곱과 혼동되는 $h^\ell$ 표기를 피한다.
- pre-activation이 필요하면 $\mathbf z^{(\ell)}$, activation은 $\mathbf h^{(\ell)}$로 쓴다.

### 7.2 Attention

batch와 head를 생략한 기본식은 다음과 같다.

\[
\mathbf Q=\mathbf X\mathbf W_Q,
\quad
\mathbf K=\mathbf X\mathbf W_K,
\quad
\mathbf V=\mathbf X\mathbf W_V
\]

\[
\mathbf A
=
\operatorname{softmax}
\left(
\frac{\mathbf Q\mathbf K^\top}{\sqrt{d_k}}
\right),
\qquad
\mathbf O=\mathbf A\mathbf V
\]

이 절에서는 token이 행에 놓인 코드 관례를 사용한다. 단일 벡터의 열벡터 관례와의 차이를 N05-14에서 설명한다.

### 7.3 해석 실험

- 원래 실행은 `original` 또는 `clean` 중 실험 설계에 맞는 말을 사용한다.
- 교란된 실행은 `corrupted`로 통일한다.
- activation을 교체한 실행은 `patched`로 통일한다.
- ablation, patching과 intervention을 동의어처럼 섞지 않는다.
- 평가 함수는 $M(f(x))$처럼 모델 출력과 구분한다.

개입 효과의 기본 표기는

\[
\Delta M
=
M\bigl(f_{\mathrm{patched}}(x)\bigr)
-
M\bigl(f_{\mathrm{baseline}}(x)\bigr)
\]

로 한다. baseline이 original인지 corrupted인지 반드시 밝힌다.

## 8. 문제와 해설 문체

### 8.1 문제

- 문제는 `구하라`, `설명하라`, `판단하라`, `설계하라`로 끝낸다.
- 한 문제에서 평가할 핵심 능력을 명확히 한다.
- 배우지 않은 기법을 숨은 선수지식으로 요구하지 않는다.
- 필요한 shape, 단위와 조건을 제공한다.
- 여러 답이 가능하면 평가 기준을 밝힌다.

### 8.2 해설

해설은 필요한 범위에서 다음을 포함한다.

1. 문제에서 묻는 것
2. 사용할 개념
3. 계산 또는 판단 과정
4. 답
5. 결과의 의미
6. 흔한 오답과 그 이유

정답을 먼저 제시한 뒤 계산을 억지로 맞추지 않는다. 계산 문제에서도 마지막에 결과가 무엇을 의미하는지 한 문장으로 설명한다.

### 8.3 해설 접기

Markdown 원본에서는 다음 구조를 사용한다.

```html
<details>
<summary>해설 보기</summary>

해설 내용

</details>
```

해설 안의 수식이 HTML 변환 후 정상적으로 렌더링되는지 확인한다.

## 9. Markdown과 파일 형식

- 제목은 파일당 하나의 `#`만 사용한다.
- 절은 `##`, 하위 절은 `###`을 사용한다.
- 네 단계보다 깊은 제목 구조는 피한다.
- 강조가 꼭 필요한 용어만 굵게 쓴다.
- 수식을 코드 표시로 감싸지 않는다.
- 표가 너무 넓어지면 목록이나 여러 표로 나눈다.
- 내부 링크는 상대경로를 사용한다.
- 이미지에는 내용이 드러나는 대체 텍스트를 쓴다.
- HTML 표현은 `details`처럼 Markdown만으로 어려운 기능에 제한한다.

### 9.1 실행 코드와 결과

- 실행 가능한 `.py` 파일을 코드의 단일 원본으로 둔다.
- Markdown에는 같은 코드를 손으로 복제하지 않는다. N05 단원은 `N05_EXAMPLE` 표식으로 원본 코드와 생성 결과가 들어갈 위치를 지정한다.
- 코드 블록 앞에서 입력·출력 shape와 대응하는 수식을 설명한다.
- 실행 결과는 stdout을 손으로 옮기지 않고 build가 실제 실행 결과를 삽입한다.
- 출력값, shape, gradient, seed, device와 실행시간을 서로 구분한다.
- 수치 비교는 기대 문자열이 아니라 명시적인 `rtol`과 `atol`을 사용한다.
- 고수준 API는 직접 tensor 계산을 보인 뒤 비교 목적으로만 사용한다.
- 생성 결과와 그림은 `.build` 아래에 두며 원본 Markdown이 생성물 없이도 예제 ID, 명령과 원본 경로를 알 수 있게 한다.

### 9.2 파일명

단원 파일은 다음 규칙을 따른다.

```text
M00-01-numbers-variables.md
M03-11-jacobian.md
N05-15-scaled-dot-product-attention.md
I07-07-activation-patching.md
A09-GEO-04-pullback-metric.md
```

- 단원 ID는 대문자를 유지한다.
- slug는 소문자 kebab-case로 쓴다.
- 파일명을 바꾸면 목차, 진행표와 내부 링크를 함께 수정한다.

### 9.3 교재용 그림

그림은 문장을 장식하는 요소가 아니라 공간 관계, 계산 흐름 또는 실험 설계를 압축해 보여 주는 설명 단위로 사용한다.

본문 설명 검증을 마친 전권 그림 단계에서는 ‘그림이 있으면 더 쉽게 이해하거나 비교할 수 있는가’를 기준으로 핵심개념·구분·중간 계산마다 판단한다. 단원당 그림 수를 제한하지 않고 해당 문단 가까이에 역할이 구분된 그림을 배치한다. 완성된 본문을 재집필하지 않으며, 캡션과 그림을 읽는 짧은 연결 문장만 보충한다. 기존 SVG 배치·화살촉·색상 양식을 재사용하되 단원의 수치와 관계에 맞춰 확인한다.

- 그림 내부의 축, 단계와 객체 이름은 영어로 쓴다. 수학 기호는 본문 표기와 일치시킨다.
- 캡션은 한국어로 쓰고 그림에서 무엇을 비교하거나 따라가야 하는지 밝힌다.
- 현재 figcaption에서는 Markdown 수식 처리가 적용되지 않으므로 간단한 기호는 T, b₁, (-3,8)ᵀ, √2 같은 plain/Unicode 표기로 쓴다. raw `$...$`나 LaTeX 명령을 넣어 문자로 노출하지 않는다. 정확한 수식 전개는 기존 본문에 둔다.
- 대체 텍스트는 `diagram`, `graph` 같은 종류만 적지 않고 핵심 객체와 관계를 영어로 설명한다.
- 본문에서 그림을 직접 가리키며 해석한다. 본문에서 설명하지 않는 장식용 그림은 넣지 않는다.
- 개념마다 독립된 시각적 질문이 있는지 판단한다. 서로 다른 방향, 변환, 사영, 조건화 또는 개입을 한 장의 추상 상자로 뭉개지 않는다.
- 질문이 공간 관계나 계산 과정이면 그 관계를 그림 자체에서 추적할 수 있게 한다. 문장이나 숫자표를 SVG로 옮기는 것만으로 보강하지 않는다. 행렬의 대응 성분이나 비교표 자체가 질문의 대상인 경우에는 그 구조를 사용할 수 있다.
- 색칠한 상자만으로 상태를 구분하지 않는다. 대표 좌표, 수치, token, shape 또는 변환 전후 가운데 적어도 하나를 그림 안에서 실제로 추적할 수 있게 한다.
- `V2`와 `V3`의 여러 장면을 하나의 SVG에 배치할 때도 각 패널의 제목, 축·행·열의 의미와 읽는 순서를 명시한다.
- SVG 바깥 안전 여백은 40~48px, 독립 객체 사이 간격은 24px 이상을 기본값으로 사용한다. 화살표는 글자와 범례를 통과하지 않게 배치한다.
- 벡터 화살촉은 `markerUnits="userSpaceOnUse"`로 고정 크기를 사용한다. 기본 형태는 길이가 짧고 끝이 뾰족한 작은 dart로 하며, SVG marker 안에서는 브라우저 호환성이 확인된 `fill="context-stroke"`를 사용한다. 화살촉의 위아래 폭은 선 굵기보다 충분히 커서 실제 HTML 크기에서도 식별돼야 한다. 짧은 선 끝에 크고 둥글게 보이는 삼각형을 붙이지 않는다. 화살촉 길이는 선분 길이의 약 15% 이하를 기본값으로 하고, 짧은 벡터에서는 화살촉을 더 줄이거나 선분을 늘린다.
- 독립된 화살표에는 각각 별도의 `path`나 `line`에 marker를 적용한다. 여러 subpath를 한 `path`로 묶고 `marker-end` 하나를 적용하면 마지막 끝에만 화살촉이 붙을 수 있다. 공유 끝점에서는 다른 선이나 점이 화살촉을 덮어 색과 방향을 혼동시키지 않는지 직접 확인한다.
- 일반 라벨은 16px, 주요 라벨은 18px, 제목은 22px 이상을 기본값으로 사용한다. 이 크기를 지킬 수 없으면 그림을 나눈다.
- SVG 원본의 글자 크기만으로 가독성을 판정하지 않는다. normal 그림은 모바일의 실제 이미지 폭 약 319px로도 읽어 확인한다. 한 좌표계나 세로 흐름은 넓은 가로 스크롤을 강제하기보다 세로형 배치와 큰 라벨을 우선한다. 폭 520px에서는 주요 라벨 26~28px, tick·축 22px 정도를 출발점으로 삼고 실제 표시에서 조정한다.
- 좌표와 이동을 설명하는 그림에는 핵심 선보다 옅은 축과 격자를 둔다. 행렬 그림에는 query·key 같은 행과 열의 의미를 적는다.
- 입력, 변환, 출력, 관찰과 개입에 쓰는 색의 의미를 그림 사이에서 바꾸지 않는다.
- 색상만으로 대상을 구분하지 않고 선 모양, 표식 또는 라벨을 함께 사용한다.
- SVG에는 `viewBox`를 두고 외부 URL, 실행 스크립트, embedded raster image와 `foreignObject`를 넣지 않는다.
- 다른 자료의 구성을 참고해 다시 그렸다면 본문이나 캡션에 출처와 재구성 사실을 밝힌다.

기본 형식은 다음과 같다.

```html
<figure class="lesson-figure" markdown="1">

![Descriptive English alt text](../../figures/assets/stage/lesson-id-figure.svg)

<figcaption>그림을 읽는 순서와 핵심 관계를 설명하는 한국어 캡션.</figcaption>
</figure>
```

숫자가 있는 행렬이나 여러 단계를 가로로 비교해 모바일에서 축소하면 글자를 읽기 어려운 그림에는 `lesson-figure--wide`를 추가한다.

```html
<figure class="lesson-figure lesson-figure--wide" markdown="1">
```

일반 그림에는 확장형 class를 붙이지 않는다. 확장형 그림은 모바일에서 figure 내부만 가로로 스크롤한다.

교재용 개념도와 저장된 수치 그래프는 `figures/assets/`에 둔다. 수치 그래프 생성 코드는 `figures/generators/`에 둔다. 실행 중에만 의미가 있는 모델 출력과 실험 산출물은 `.build`에 둔다.

#### 9.3.1 반복 배치 오류의 처리

- HTML에서 결함을 발견하면 SVG 원본의 겹침·경계 문제와 페이지의 이미지 크기·비율·래퍼·축소 문제를 먼저 구분한다. 원본에도 겹치면 해당 SVG나 생성 코드의 배치를 고치고, 페이지에서만 작아지거나 잘리면 실제 표시 크기와 figure class·CSS를 확인한다.
- 라벨과 범례를 놓을 공간을 먼저 확보하고 선·화살표를 배치한다. 위 안전 여백과 객체 간격은 출발값이다. 긴 라벨, 화살촉 끝, 축 이름까지 경계 안에 들어가는지 확인하고 필요하면 패널 배치나 줄바꿈을 조정한다. 라벨끼리도 좌표 기준점이 아니라 실제 글자 폭·높이 사이의 간격을 확인한다. 그래프 하단 설명의 여백은 축 상자의 끝이 아니라 tick·축 라벨의 실제 글자 범위부터 확보한다. 단원마다 다른 좌표·흐름을 같은 고정 배치로 강제하지 않는다.
- 짧은 벡터에서도 선과 작은 화살촉을 함께 읽을 수 있어야 한다. 위 화살촉 비율을 적용하되 수학적 끝점을 임의로 옮기지 않는다. 표시 척도를 조정하거나 촉을 줄이고, 실제 HTML에서 방향의 식별과 촉의 소실·겹침을 확인한다.
- SVG의 연속 공백으로 서로 다른 라벨의 간격을 만들지 않는다. 공백이 축약되어 라벨이 붙는 경우에는 해당 라벨을 별도 text 요소로 나누고 실제 글자 범위 사이의 여백을 확인한다.
- 글자 크기는 원본과 페이지 축소율을 함께 확인한다. normal의 실제 모바일 이미지 폭은 페이지 여백에 따라 약 307~319px가 될 수 있다. 이 폭에서 주요 라벨·축·범례를 읽고, 단순 그림은 세로 배치·큰 글자를 우선하며 복합 가로 비교는 wide의 내부 스크롤을 사용한다. 세로형이 페이지 높이 제한과 object-fit으로 과도하게 축소되는 것이 확인되면 해당 figure에만 `lesson-figure--tall`을 추가할 수 있다. 이 선택형 표시는 가로 스크롤 없이 비율을 유지하고 데스크톱 최대 폭 26rem, 모바일 본문 폭으로 표시한다. 원본 font-size나 figure class만으로 통과 처리하지 않는다.
- 반복 원인의 해결책은 대표 그림의 실제 1440×900·390×844와 밝은·어두운 테마에서 효과를 확인한 뒤 공통 기준에 반영한다. 조정자가 기준을 관리하고 병렬 작업자에게 공유한다. 새 그림과 아직 검수 중인 그림부터 적용하며, 완료 그림은 같은 결함이 확인된 경우에만 고친다.
- 생성 코드·사이트 설정은 반복 원인으로 확인한 부분만 최소 수정한다. 별도 제작 시스템이나 무관한 리팩터링을 추가하지 않는다. 기준 문구 변경만으로 전권 재생성·전체 검사를 반복하지 않으며, 공통 코드 변경의 관련 검사와 최종 통합 검증은 기존 주기를 따른다. 진행 기록에는 원인·반영 기준·실제 확인 결과만 남긴다.

## 10. 예외와 변경 기록

한국어 문체·한국어 캡션 규칙은 한국어판에 적용한다. 영문판의 언어별 적용은 제11절을 따른다. 수학 표기 규칙은 양언어에 공통이다.

표기나 문체 규칙을 바꿀 때는 다음을 기록한다.

| 날짜 | 변경 | 이유 | 영향을 받는 단원 |
|---|---|---|---|
| 2026-09-30 | 최초 규칙 확정 | 프로젝트 시작 | 전체 |
| 2026-10-01 | 실행 코드 단일 원본과 결과 생성 규칙 추가 | N05 재현 실습 기반 구축 | N05 이후 |
| 2026-10-01 | 교재용 SVG와 시각적 직관 기준 추가 | 개념 설명 보강 개정판의 그림 품질과 재현성 고정 | 전체 |
| 2026-10-01 | 시각화 판단 단위를 단원에서 독립된 시각적 메커니즘으로 구체화 | 색칠한 상자 중심 도식이 실제 변화와 공간 관계를 가리는 문제 수정 | 전체 |
| 2026-10-01 | 핵심 개념 대장과 그림 여백·글자·격자 기준 추가 | 설명 누락과 SVG 요소 겹침을 개념 단위로 검수 | 전체 |
| 2026-10-02 | 전권 본문 설명 검증 후 시각화 진행; 본문 상태와 수정 근거 분리 | 그림 추가로 설명 개정을 완료 처리하는 문제 방지 | 전체 |
| 2026-10-02 | 생략된 이해 과정 보충을 개정 기준으로 고정; 항목 충족과 분량 확대율 요구 제외 | 승인된 M00-03~05처럼 개념 자체를 충분히 설명하고 주변 사례의 기계적 확장 방지 | 전체 |
| 2026-10-06 | 완료 본문을 보존하며 개념별 풍부한 SVG 보강·기존 양식 재사용 | 이해와 비교에 도움이 되는 관계를 그림 수 제한 없이 보여 주고 중복 제작을 줄임 | 전체 |
| 2026-10-06 | 반복 배치 오류의 원본/페이지 원인 구분과 검증된 해결책 공유 | 실제 HTML에서 확인한 글자·촉·여백 문제의 재발 방지 | 신규·검수 중 그림; 완료 그림은 같은 결함 발견 시 |
| 2026-10-07 | 원문 기반 영문 재서술·언어별 제목/캡션/점검표·대조 검수 기준 추가 | 교육 내용을 보존하고 영어 문장과 UI를 분리 관리 | 영문판 전체와 공통 사이트 처리 |

## 11. 영문판 문체와 보존 기준

`translations/en/`에는 같은 한국어 내용을 미국식 영어 교재 문체로 재서술한다. `ko-en-academic-writing`의 `english_prose.md`와 `editorial_protocol.md`가 주 기준이며 stop-slop은 빈말·과장·내용 없는 반복에만 보조 적용한다. 필요한 수동태·명사화·유보·전문 용어 반복·긴 설명을 일괄 삭제하지 않는다. 학술지 형식이나 새로운 논증 구조를 교재에 강제하지 않는다.

- 문장을 합치거나 나누고 영어 어순으로 쓸 수 있지만 기존 단원/절/문단의 역할·순서·내용·논리 관계를 보존한다. 분량이나 문장 길이를 목표로 삼지 않는다.
- 정의·조건·부정·양화·관측/개입·정보 복원/실제 사용·필요/충분·상관/인과를 대조한다. `may`, `can`, `shows`, `suggests` 등은 문체용 동의어가 아니다.
- 용어집의 확정된 영어를 사용하되 다의어는 문맥을 확인한다. 같은 개념에 동의어를 번갈아 쓰지 않는다. 수학 객체, 열벡터/행 데이터, Jacobian 행/열, differential/metric-dependent gradient의 구분을 유지한다.
- 영어 표 헤더는 `Symbol or term | Common spoken reading | Meaning | Shape and conditions`를 기본으로 한다. 원문이 3열이면 3열을 유지하고 `Meaning` 또는 `Meaning in this lesson`을 쓴다. 4열 원문의 마지막 열은 원래 역할에 맞게 `Cautions`, `Examples`, `Scope` 등으로 옮길 수 있으며 없는 열·조건을 추가하지 않는다. 읽기 열의 내용과 백틱은 한국어판과 동일하게 유지한다.
- 공통 절은 `Why this lesson matters`, `Learning objectives`, `Prerequisite check`, `Symbols and terms`, `Core concepts`, `Common misconceptions`, `Exercises`, `Lesson summary`, `Pass criteria`, `Next lesson`, `Author checklist`로 옮긴다. 실제 하위 절·예제 제목은 원문의 뜻을 영어로 쓰며 새 절을 만들지 않는다.
- 번호가 붙은 개별 핵심 개념 제목은 `Core concept 1. ...`처럼 단수로 쓴다. `Core concepts`는 여러 개념을 묶는 총괄 절에 사용한다.
- 문제는 `Calculate`, `Explain`, `Determine`, `Design`처럼 묻는 행동을 밝힌다. 번호·위치·수치·조건·정답과 해설 논리를 보존하며 `<summary>Show solution</summary>`을 사용한다.
- figure의 위치·class·SVG 경로·영어 alt를 유지하고 캡션만 영어로 쓴다. figcaption에는 raw LaTeX를 넣지 않는다. 영어 길이에 따른 표시 보정은 해당 언어에만 최소 적용한다.
- frontmatter의 `id`, `part`, `stage`, `prerequisites`와 파일명은 유지한다. `title`·`estimated_time`은 영어화하며 `status`의 `완료`는 영어에서 `complete`로 쓴다. 이 상태는 원본 집필 완료를 뜻하며 번역 검수 완료는 translation audit으로 별도 판정한다.
- 내부 점검표는 영문 `Author checklist`로 유지하고 공개 build에서 제거한다. 읽기 점검 문장은 `Common spoken reading uses actual English academic speech, without Korean transliteration or mechanical descriptions of symbol placement.`로 쓴다.
- 원문 오류·번역 오류·문체 문제·화면 문제를 구분하여 기록한다. 원문 오류를 재서술에서 몰래 고치거나 검토한 것처럼 처리하지 않는다.
