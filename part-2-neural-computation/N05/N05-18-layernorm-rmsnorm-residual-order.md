---
id: "N05-18"
title: "LayerNorm, RMSNorm과 residual 순서"
part: 2
stage: "N05"
status: "완료"
prerequisites:
  - "N05-17"
estimated_time: "120~150분"
---

# N05-18. LayerNorm, RMSNorm과 residual 순서

## 이 단원이 필요한 이유

normalization의 종류와 위치는 block의 수식, activation scale과 hook 의미를 바꾼다. `norm output`, `residual input`과 `block output`을 같은 것으로 취급하면 모델 구조를 잘못 읽게 된다.

## 학습 목표

- LayerNorm과 RMSNorm을 작은 vector에 계산할 수 있다.
- centering 유무와 학습 parameter를 구분할 수 있다.
- pre-norm과 post-norm block 식을 순서대로 쓸 수 있다.
- normalization axis와 output shape를 확인할 수 있다.
- 서로 다른 norm 위치의 activation을 직접 비교할 때의 한계를 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [N05-17 residual stream](N05-17-residual-stream.md)
- 확인 질문: sublayer output과 residual addition 뒤 stream을 구분할 수 있는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\mu$ | `mu` | 한 token vector의 feature mean | scalar |
| $\sigma^2$ | `sigma squared` | feature variance | nonnegative scalar |
| $\operatorname{RMS}(\mathbf x)$ | `the root mean square of x` | feature 제곱평균의 제곱근 | nonnegative scalar |
| $\boldsymbol\gamma$ | `gamma` | feature별 learned scale | $\mathbb R^{d_{model}}$ |
| pre-norm | `pre-norm` | sublayer 전에 normalization하는 순서 | architecture choice |
| post-norm | `post-norm` | residual addition 뒤 normalization하는 순서 | architecture choice |

## 핵심 개념 1. LayerNorm

feature dimension이 $d$인 token vector $\mathbf x$에 대해

\[
\mu=\frac1d\sum_{j=1}^{d}x_j,
\qquad
\sigma^2=\frac1d\sum_{j=1}^{d}(x_j-\mu)^2
\]

로 두면

\[
\operatorname{LN}(\mathbf x)
=\boldsymbol\gamma\odot
\frac{\mathbf x-\mu\mathbf 1}{\sqrt{\sigma^2+\epsilon}}
+\boldsymbol\beta
\]

이다. centering과 rescaling을 모두 한다. 보통 각 token의 마지막 feature axis에서 통계를 계산한다.

## 핵심 개념 2. RMSNorm

\[
\operatorname{RMS}(\mathbf x)
=\sqrt{\frac1d\sum_{j=1}^{d}x_j^2+\epsilon},
\qquad
\operatorname{RMSNorm}(\mathbf x)
=\boldsymbol\gamma\odot\frac{\mathbf x}{\operatorname{RMS}(\mathbf x)}
\]

이다. mean을 빼지 않으므로 일반적으로 output mean은 0이 아니다. bias 사용 여부는 구현에 따라 다르지만 기준 RMSNorm 식은 learned scale을 사용한다.

## 핵심 개념 3. residual 순서

하나의 sublayer $F$에 대한 대표식은 다음과 같다.

\[
\text{pre-norm:}\quad
\mathbf y=\mathbf x+F(\operatorname{Norm}(\mathbf x))
\]

\[
\text{post-norm:}\quad
\mathbf y=\operatorname{Norm}(\mathbf x+F(\mathbf x))
\]

연산 순서가 다르므로 weight가 같아도 같은 함수가 아니다. 원래 Transformer는 post-norm 식을 사용했고 현대 decoder에는 pre-norm 계열도 널리 쓰인다. 실제 모델은 config와 forward code로 확인한다.

## 예제

$\mathbf x=(1,2,3)$, $\gamma=1$, $\beta=0$이고 작은 $\epsilon$만 둔다. LayerNorm은 mean 2를 빼므로 약

\[
(-1.2247,0,1.2247)
\]

이 된다. RMSNorm은 mean을 빼지 않아 약

\[
(0.4629,0.9258,1.3887)
\]

이다. 두 결과는 shape가 같지만 보존하는 정보와 scale 기준이 다르다.

## 실행 실습

### 실행 환경과 원본

- 환경: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- 확인일: 2026-10-01
- 구성요소 등급: `Common modern variant`
- 예제 ID: `n05_18_normalization_order`
- 코드 원본: `labs/N05/n05_18_normalization_order.py`
- 테스트: `tests/N05/test_n05_18.py`
- 실행 명령: `.venv\Scripts\python.exe -m labs.N05.n05_18_normalization_order`

### 자원 예산

batch 1, token 2개, model dimension 3의 normalization과 단일 sublayer 순서만 계산한다.

### 실제 코드와 실행 결과

<!-- N05_EXAMPLE: n05_18_normalization_order -->

### 검사

테스트는 LayerNorm output mean, RMSNorm output의 mean square와 pre-norm·post-norm output 차이를 확인한다.

## epsilon과 learned scale

$\epsilon$은 variance나 mean square가 매우 작을 때 0으로 나누는 것을 막는다. 구현마다 기본값과 제곱근 안팎의 위치가 다를 수 있으므로 수치 재현에는 정확한 식이 필요하다. $\gamma$를 적용한 최종 output의 RMS는 일반적으로 1이 아니다. `normalized`라는 말이 모든 feature의 절댓값이나 norm이 고정된다는 뜻은 아니다.

## 모델 해석과의 연결

pre-norm 모델의 sublayer input hook은 normalized activation을 보고, residual stream hook은 normalization 전 stream을 볼 수 있다. 둘의 coordinate와 scale이 다르므로 이름만 `hidden state`라고 맞춰 직접 비교하면 안 된다.

normalization output을 patch하면 feature별 rescaling과 다른 feature에 의존하는 denominator가 함께 바뀐다. 단일 neuron만 독립적으로 바꾸는 조작으로 해석할 수 없다.

## 흔한 오해

### 오해 1. RMSNorm도 mean을 0으로 만든다

RMSNorm은 제곱평균으로 scale하지만 centering하지 않는다.

### 오해 2. pre-norm과 post-norm은 식을 보기 좋게 바꾼 표기다

normalization과 nonlinear sublayer의 합성 순서가 다르므로 함수와 gradient path가 달라진다.

### 오해 3. normalization 뒤 각 token의 Euclidean norm은 항상 1이다

learned scale을 적용하기 전 RMS가 약 1이라는 것과 Euclidean norm 1은 다르다. dimension $d$에서는 RMS 1이면 norm은 $\sqrt d$다.

## 연습문제

### 1. LayerNorm mean

$x=(2,4,6)$의 feature mean은?

<details><summary>해설 보기</summary>$(2+4+6)/3=4$다.</details>

### 2. RMS

$x=(3,4)$이고 $\epsilon=0$이면 RMS는?

<details><summary>해설 보기</summary>$\sqrt{(9+16)/2}=\sqrt{12.5}$다. Euclidean norm 5와 다르다.</details>

### 3. centering

$x=(1,2,3)$에서 mean을 빼는 방식은 LayerNorm과 RMSNorm 중 어느 것인가?

<details><summary>해설 보기</summary>LayerNorm이다.</details>

### 4. pre-norm 순서

$x$, Norm, $F$와 덧셈 기호만 써 pre-norm 식을 적어라.

<details><summary>해설 보기</summary>$y=x+F(\operatorname{Norm}(x))$다.</details>

### 5. axis 진단

input shape가 `(batch, sequence, model)`일 때 token별 LayerNorm의 통계 axis는?

<details><summary>해설 보기</summary>마지막 model feature axis다. batch나 sequence를 함께 평균내지 않는다.</details>

### 6. hook 비교

normalization 전 residual과 normalization 뒤 sublayer input의 cosine similarity가 낮아졌다고 feature가 사라졌다고 말할 수 있는가?

<details><summary>해설 보기</summary>바로 말할 수 없다. centering·rescaling과 learned scale이 좌표값을 바꿨으므로 같은 위치의 표현과 행동을 추가로 검사해야 한다.</details>

## 근거와 갱신 경계

LayerNorm 정의는 [Layer Normalization](https://arxiv.org/abs/1607.06450), 원래 Transformer의 residual 순서는 [Attention Is All You Need](https://arxiv.org/abs/1706.03762), RMSNorm 정의는 [Root Mean Square Layer Normalization](https://arxiv.org/abs/1910.07467)에 근거한다. epsilon, bias와 norm 위치는 모델 config와 구현을 확인해야 하는 architecture-specific 항목이다.

## 단원 요약

- LayerNorm은 centering과 rescaling을 한다.
- RMSNorm은 mean을 빼지 않고 root mean square로 scale한다.
- pre-norm과 post-norm은 normalization의 계산 위치가 다르다.
- epsilon과 learned scale 때문에 이상화한 정규화 성질을 그대로 가정하면 안 된다.
- hook activation을 비교하기 전에 normalization 전후 위치를 확인한다.

## 통과 기준

- 두 normalization을 작은 vector에 계산할 수 있는가?
- centering 유무를 설명할 수 있는가?
- pre-norm·post-norm 식을 쓸 수 있는가?
- normalization axis와 shape를 확인할 수 있는가?
- norm 위치가 다른 activation 비교의 한계를 말할 수 있는가?

## 다음 단원

- [N05-19 dense MLP, SwiGLU와 expert routing](N05-19-dense-mlp-swiglu-expert-routing.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] LayerNorm·RMSNorm과 residual 순서를 구분했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
- [x] Markdown에 실행 코드를 손으로 복제하지 않았다.
- [x] 코드 원본·테스트 경로·자원 예산·확인일을 기록했다.
- [x] normalization invariant와 순서 test가 있다.

