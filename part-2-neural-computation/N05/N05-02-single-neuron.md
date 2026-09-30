---
id: "N05-02"
title: "하나의 neuron"
part: 2
stage: "N05"
status: "완료"
prerequisites:
  - "N05-01"
  - "M01-06"
estimated_time: "110~140분"
---

# N05-02. 하나의 neuron

## 이 단원이 필요한 이유

하나의 neuron은 입력의 weighted sum에 bias를 더하고 activation function을 적용한다. 이 계산을 분해할 수 있어야 weight와 activation을 구분하고, 어느 지점의 값을 저장하거나 바꿀지 정할 수 있다.

이 단원은 neuron을 생물학적 세포의 모형으로 설명하지 않는다. 신경망에서 반복되는 affine transformation과 elementwise nonlinearity의 가장 작은 계산 단위로 다룬다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- 입력, weight와 bias로 pre-activation을 계산할 수 있다.
- affine transformation과 linear transformation을 구분할 수 있다.
- pre-activation과 post-activation을 구분할 수 있다.
- ReLU neuron의 forward value와 gradient를 손으로 계산할 수 있다.
- 직접 쓴 PyTorch tensor 연산을 수식의 각 항에 대응시킬 수 있다.

## 선수지식 확인

- 선수 단원: [N05-01 tensor와 계산 그래프](N05-01-tensors-computation-graphs.md)
- 선수 단원: [M01-06 합성함수와 연쇄법칙](../../part-1-foundations/M01/M01-06-composition-chain-rule.md)
- 확인 질문: 두 길이 2 vector의 dot product를 계산할 수 있는가?
- 확인 질문: $L=(a-1)^2$의 $a$에 대한 도함수를 구할 수 있는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\mathbf x$ | `x` | neuron에 들어오는 입력 vector | $\mathbf x\in\mathbb R^d$ |
| $\mathbf w$ | `w` | 입력 성분의 계수를 모은 weight vector | $\mathbf w\in\mathbb R^d$ |
| $b$ | `b` | dot product에 더하는 bias | $b\in\mathbb R$ |
| $z=\mathbf w^\top\mathbf x+b$ | `z equals w transpose x plus b` | activation 전의 pre-activation | $z\in\mathbb R$ |
| $a=\phi(z)$ | `a equals phi of z` | activation 뒤의 post-activation | $a\in\mathbb R$ |
| $\operatorname{ReLU}(z)$ | `ReLU of z` | $\max(0,z)$로 정의한 activation function | $\mathbb R\to\mathbb R$ |
| $\mathcal L$ | `script L` | 이 예제에서 줄이려는 scalar loss | $\mathcal L\in\mathbb R$ |

## 핵심 개념 1. weighted sum과 bias

입력 $\mathbf x=(x_1,\ldots,x_d)$와 weight $\mathbf w=(w_1,\ldots,w_d)$의 dot product에 bias를 더하면

\[
z=\mathbf w^\top\mathbf x+b
=\sum_{i=1}^{d}w_ix_i+b
\]

를 얻는다. $z$를 pre-activation이라고 한다. 각 $w_i$는 대응하는 입력 성분이 $z$에 기여하는 부호와 크기를 조절한다. $b$는 입력과 곱해지지 않고 전체 합을 이동시킨다.

## 핵심 개념 2. affine transformation은 bias를 포함한다

$\mathbf w^\top\mathbf x$는 $\mathbf x$에 대한 linear map이다. $b\ne0$이면

\[
f(\mathbf x)=\mathbf w^\top\mathbf x+b
\]

는 일반적으로 원점을 원점으로 보내지 않으므로 linear map이 아니다. 이런 형태를 affine transformation이라고 한다. 신경망 코드에서 `Linear` layer라는 이름을 쓰더라도 bias가 켜져 있으면 수학적 함수는 affine이다.

## 핵심 개념 3. activation 전과 후를 구분한다

activation function을 $\phi$라고 하면 neuron 출력은

\[
a=\phi(z)=\phi(\mathbf w^\top\mathbf x+b)
\]

이다. 이 단원에서는

\[
\operatorname{ReLU}(z)=\max(0,z)
\]

를 사용한다. $z>0$이면 $a=z$, $z<0$이면 $a=0$이다. $z=0$에서는 미분값을 하나로 정할 수 없으며 PyTorch는 backward에서 0을 사용한다.

pre-activation $z$와 post-activation $a$를 둘 다 activation이라고 부르면 hook 위치와 gradient 해석이 불분명해진다. 이 책에서는 둘을 이름으로 구분한다.

## 핵심 개념 4. 하나의 손계산

다음 값을 사용한다.

\[
\mathbf x=(2,-1),
\quad
\mathbf w=(1.5,0.5),
\quad
b=-0.5
\]

pre-activation은

\[
z=1.5\cdot2+0.5\cdot(-1)-0.5=2
\]

이고 $z>0$이므로

\[
a=\operatorname{ReLU}(2)=2
\]

이다.

target을 1로 둔 squared loss

\[
\mathcal L=(a-1)^2
\]

를 사용하면 $\mathcal L=1$이다.

## 핵심 개념 5. gradient를 연쇄법칙으로 계산한다

$z=2>0$이므로 현재 점에서 $da/dz=1$이다. 따라서

\[
\frac{\partial\mathcal L}{\partial a}=2(a-1)=2,
\qquad
\frac{\partial\mathcal L}{\partial z}=2\cdot1=2
\]

이다. $z=\sum_iw_ix_i+b$를 미분하면

\[
\frac{\partial\mathcal L}{\partial w_i}
=\frac{\partial\mathcal L}{\partial z}x_i,
\qquad
\frac{\partial\mathcal L}{\partial b}
=\frac{\partial\mathcal L}{\partial z}
\]

이므로

\[
\nabla_{\mathbf w}\mathcal L=(4,-2),
\qquad
\frac{\partial\mathcal L}{\partial b}=2
\]

를 얻는다. 입력 gradient도 같은 방식으로

\[
\nabla_{\mathbf x}\mathcal L
=2\mathbf w=(3,1)
\]

이다.

## 예제 1. bias의 역할 비교

### 문제

위의 $\mathbf x,\mathbf w$를 유지하고 $b=-3$으로 바꾸면 $z$와 $a$는 어떻게 되는가?

### 풀이

dot product는 $1.5\cdot2+0.5\cdot(-1)=2.5$다. 따라서 $z=2.5-3=-0.5$이고 $a=\operatorname{ReLU}(-0.5)=0$이다.

### 결과의 의미

weight를 바꾸지 않아도 bias가 activation 경계를 이동시켰다. 같은 입력이 ReLU의 양수 구간에 있을지 음수 구간에 있을지가 달라진다.

## 예제 2. 모델에서 찾기

MLP와 attention의 projection은 여러 neuron의 affine transformation을 한 행렬 연산으로 묶는다. 개별 neuron의 $z$를 관찰하면 activation function에 들어가기 전 값을 보고, $a$를 관찰하면 비선형 변환 뒤 값을 본다. 특정 neuron의 큰 $a$가 어떤 개념과 관련될 수는 있지만, 큰 값 하나만으로 모델이 그 개념을 사용한다고 결론 내릴 수는 없다.

## 실행 실습

### 실행 환경과 원본

- 환경: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- 확인일: 2026-10-01
- 구성요소 등급: `Stable core`
- 예제 ID: `n05_02_single_neuron`
- 코드 원본: `labs/N05/n05_02_single_neuron.py`
- 테스트: `tests/N05/test_n05_02.py`
- 실행 명령: `.venv\Scripts\python.exe labs/N05/n05_02_single_neuron.py`

### 자원 예산

이 예제는 길이 2 입력, 학습 가능한 scalar 3개, 학습 step 0개를 사용한다. CPU thread는 각각 1개이며 hard timeout은 10초다.

### 실제 코드와 실행 결과

site build는 아래 위치에 `.py` 원본과 실제 실행 결과를 삽입한다.

<!-- N05_EXAMPLE: n05_02_single_neuron -->

### 결과 해석

실행 결과의 `pre_activation=2.0`, `activation=2.0`, `loss=1.0`은 손계산과 같다. `weight.grad=[4.0, -2.0]`, `bias.grad=2.0`, `x.grad=[3.0, 1.0]`도 연쇄법칙으로 구한 값과 일치한다.

이 검사는 autograd가 값을 만들었다는 사실에 그치지 않는다. 예상 gradient를 독립적으로 적고 `torch.testing.assert_close`로 비교한다.

## 흔한 오해

### 오해 1. bias가 있더라도 linear transformation이다

$b\ne0$인 $\mathbf w^\top\mathbf x+b$는 affine transformation이다. framework class 이름과 수학적 분류를 구분해야 한다.

### 오해 2. activation은 함수와 출력값을 모두 뜻한다

문맥에서 두 용법을 볼 수 있지만, 계산을 추적할 때는 activation function $\phi$와 activation value $a$를 구분해야 한다. 이 책의 용어집은 활성화함수와 활성값을 따로 둔다.

### 오해 3. ReLU neuron의 gradient는 언제나 weight다

ReLU가 양수 구간에 있을 때 $da/dz=1$이지만 음수 구간에서는 0이다. loss의 바깥 미분도 곱해야 하므로 전체 gradient는 현재 입력과 loss에 따라 달라진다.

## 연습문제

### 1. forward 계산

$\mathbf x=(1,3)$, $\mathbf w=(2,-1)$, $b=0.5$일 때 $z$와 ReLU 출력 $a$를 구하라.

<details>
<summary>해설 보기</summary>

$z=2\cdot1+(-1)\cdot3+0.5=-0.5$다. 따라서 $a=0$이다.

</details>

### 2. linear와 affine

$f(\mathbf x)=\mathbf w^\top\mathbf x+b$가 linear map이 되기 위한 $b$의 조건을 적고 이유를 설명하라.

<details>
<summary>해설 보기</summary>

$b=0$이어야 한다. linear map은 $f(\mathbf0)=0$을 만족해야 하는데, 이 함수에서는 $f(\mathbf0)=b$다.

</details>

### 3. shape

$\mathbf x,\mathbf w\in\mathbb R^5$이고 $b\in\mathbb R$일 때 $z$와 $a$의 shape는 무엇인가?

<details>
<summary>해설 보기</summary>

dot product $\mathbf w^\top\mathbf x$와 bias는 scalar이므로 $z$와 $a$ 모두 scalar tensor이며 shape는 `()`다.

</details>

### 4. gradient

$z>0$, $\mathcal L=(a-t)^2$인 ReLU neuron에서 $\partial\mathcal L/\partial b$를 구하라.

<details>
<summary>해설 보기</summary>

$z>0$이면 $da/dz=1$이고 $dz/db=1$이다. 따라서 $\partial\mathcal L/\partial b=2(a-t)$다.

</details>

### 5. 음수 구간

$z<0$인 ReLU neuron에서 $a$에 의존하는 loss의 $\partial\mathcal L/\partial\mathbf w$가 0이 되는 이유를 설명하라.

<details>
<summary>해설 보기</summary>

$z<0$에서는 $a=0$이 일정하여 $da/dz=0$이다. 연쇄법칙에서 이 항이 곱해지므로 $\partial\mathcal L/\partial\mathbf w$도 0이 된다. 다른 경로로 weight가 loss에 연결돼 있다면 그 경로의 gradient는 별도로 더해야 한다.

</details>

### 6. 해석 주장

한 neuron의 activation이 특정 단어에서 크게 나왔다. 이 관찰만으로 말할 수 있는 것과 없는 것을 나눠라.

<details>
<summary>해설 보기</summary>

지정한 입력과 model에서 그 neuron의 post-activation이 컸다고 말할 수 있다. neuron이 그 단어의 개념을 유일하게 표현한다거나 모델이 행동을 만들 때 그 값을 사용한다고는 아직 말할 수 없다. 비교 입력, 복원 검사와 개입 증거가 추가로 필요하다.

</details>

## 단원 요약

- 하나의 neuron은 affine transformation 뒤에 activation function을 적용한다.
- weight는 입력 성분별 계수이고 bias는 pre-activation 전체를 이동시킨다.
- pre-activation $z$와 post-activation $a$는 서로 다른 graph node다.
- ReLU의 현재 구간은 forward value와 gradient 경로를 함께 바꾼다.
- autograd 결과는 손계산한 수치와 gradient에 대조해야 한다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- $z=\mathbf w^\top\mathbf x+b$를 원소별 합으로 펼칠 수 있는가?
- linear transformation과 affine transformation을 구분할 수 있는가?
- pre-activation과 post-activation의 hook 위치를 구분할 수 있는가?
- ReLU의 양수·음수 구간에서 gradient를 계산할 수 있는가?
- activation 관찰과 모델의 기능적 사용 주장을 구분할 수 있는가?

## 다음 단원

- [N05-03 MLP forward pass](N05-03-mlp-forward-pass.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] 모든 새 기호가 사용 전에 정의됐다.
- [x] vector와 scalar의 shape가 일관된다.
- [x] linear와 affine을 구분했다.
- [x] forward와 gradient를 손으로 검산했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
- [x] Markdown에 실행 코드를 손으로 복제하지 않았다.
- [x] 코드 원본·테스트 경로·자원 예산·확인일을 기록했다.
- [x] shape·수치·gradient test가 있다.
