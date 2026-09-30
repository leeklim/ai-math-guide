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
3. 모델이나 분석에서 하는 역할

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

### 9.1 파일명

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

## 10. 예외와 변경 기록

현재 예외는 없다.

표기나 문체 규칙을 바꿀 때는 다음을 기록한다.

| 날짜 | 변경 | 이유 | 영향을 받는 단원 |
|---|---|---|---|
| 2026-09-30 | 최초 규칙 확정 | 프로젝트 시작 | 전체 |
