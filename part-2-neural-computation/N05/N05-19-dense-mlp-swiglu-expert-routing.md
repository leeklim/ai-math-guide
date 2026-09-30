---
id: "N05-19"
title: "dense MLP, SwiGLU와 expert routing"
part: 2
stage: "N05"
status: "완료"
prerequisites:
  - "N05-18"
estimated_time: "120~150분"
---

# N05-19. dense MLP, SwiGLU와 expert routing

## 이 단원이 필요한 이유

Transformer의 token별 feed-forward 계산은 모두 같은 parameter를 쓰는 dense MLP일 수도 있고, router가 선택한 expert만 쓰는 sparse MoE일 수도 있다. SwiGLU의 gate와 MoE router를 같은 `gate`라는 말로 뭉뚱그리면 서로 다른 계산을 혼동한다.

## 학습 목표

- dense MLP와 SwiGLU의 forward 식과 shape를 계산할 수 있다.
- SwiGLU의 두 input projection 역할을 구분할 수 있다.
- top-1 expert routing의 probability와 선택 결과를 계산할 수 있다.
- dense parameter 수와 token당 활성화되는 expert parameter를 구분할 수 있다.
- router score 관찰과 expert의 인과 기여를 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [N05-18 LayerNorm, RMSNorm과 residual 순서](N05-18-layernorm-rmsnorm-residual-order.md)
- 확인 질문: token별 linear projection과 elementwise activation의 shape를 계산할 수 있는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $d_{ff}$ | `d sub f f` | feed-forward hidden dimension | positive integer |
| $\operatorname{SiLU}$ | `sigh-loo` | $z\,\sigma(z)$인 activation | elementwise |
| $\odot$ | `elementwise product` | 같은 shape tensor의 원소별 곱 | shape-preserving |
| $p_e(\mathbf x)$ | `the routing probability for expert e` | router가 expert $e$에 주는 probability | $[0,1]$ |
| top-1 routing | `top-one routing` | token마다 가장 높은 expert 하나를 선택하는 규칙 | discrete selection |
| expert | `expert` | MoE에서 선택적으로 실행되는 feed-forward subnetwork | architecture-specific |

## 핵심 개념 1. dense MLP

기본 feed-forward layer는 token마다 같은 parameter를 적용한다.

\[
\operatorname{MLP}(\mathbf x)
=\mathbf W_{down}\,\phi(\mathbf W_{up}\mathbf x+mathbf b_{up})
+\mathbf b_{down}
\]

row-vector convention에서는 weight transpose 위치가 바뀐다. 입력과 출력은 $d_{model}$, 중간 activation은 $d_{ff}$ dimension이다. `dense`는 모든 token이 같은 MLP parameter 전체를 사용한다는 뜻이다.

## 핵심 개념 2. SwiGLU

SwiGLU는 중간 표현을 두 projection의 원소별 곱으로 만든다.

\[
\mathbf h=operatorname{SiLU}(\mathbf W_g\mathbf x)
\odot(\mathbf W_u\mathbf x),
\qquad
\mathbf y=\mathbf W_d\mathbf h
\]

$\mathbf W_g$ 경로는 SiLU를 거친 gate, $\mathbf W_u$ 경로는 gate가 조절할 content를 만든다. 두 projection output은 모두 $d_{ff}$여야 한다.

## 핵심 개념 3. expert routing

$E$개 expert가 있을 때 router는

\[
\mathbf p(\mathbf x)=\operatorname{softmax}(\mathbf W_r\mathbf x),
\qquad
e^*=\operatorname*{argmax}_e p_e(\mathbf x)
\]

를 계산한다. 단순한 top-1 예에서는

\[
\mathbf y=p_{e^*}(\mathbf x)F_{e^*}(\mathbf x)
\]

로 선택된 expert output만 사용한다. 실제 MoE에는 capacity, load balancing, dropped token과 통신 같은 추가 규칙이 있을 수 있다.

SwiGLU gate는 한 MLP 내부의 featurewise multiplication이고, MoE router는 여러 parameterized subnetwork 중 실행 경로를 정한다.

## 예제

두 expert의 router weight를 coordinate axis로 두고 token $(2,-1)$을 넣으면 logits는 $(2,-1)$이다. softmax probability는 약 $(0.9526,0.0474)$이므로 expert 0을 선택한다. token $(-1,2)$는 반대로 expert 1을 선택한다. 같은 batch 안에서도 token별 경로가 달라질 수 있다.

## 실행 실습

### 실행 환경과 원본

- 환경: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- 확인일: 2026-10-01
- 구성요소 등급: dense SwiGLU는 `Common modern variant`, expert routing은 `Architecture-specific`
- 예제 ID: `n05_19_mlp_routing`
- 코드 원본: `labs/N05/n05_19_mlp_routing.py`
- 테스트: `tests/N05/test_n05_19.py`
- 실행 명령: `.venv\Scripts\python.exe -m labs.N05.n05_19_mlp_routing`

### 자원 예산

token 3개, model dimension 2, hidden dimension 2와 expert 2개를 사용한다. training이나 dispatch 통신은 없다.

### 실제 코드와 실행 결과

<!-- N05_EXAMPLE: n05_19_mlp_routing -->

### 검사

테스트는 SwiGLU shape·수치, router probability row sum, top-1 expert index와 routed output을 확인한다.

## parameter와 계산량을 구분하기

MoE는 전체 expert parameter를 모두 저장하지만 token마다 일부 expert만 활성화할 수 있다. 따라서 total parameter count와 token당 실행 parameter 수는 다르다. dense MLP와 MoE를 비교할 때 parameter, FLOP, memory traffic, communication과 quality를 따로 기록해야 한다.

top-1 `argmax`는 선택 index에 대해 미분 가능하지 않다. 실제 학습은 선택된 gate probability와 auxiliary loss 등을 통해 router를 학습한다. 이 단원의 toy routing은 그 전체 학습 알고리즘을 재현하지 않는다.

## 모델 해석과의 연결

SwiGLU hidden activation을 분석할 때 gate projection, up projection과 elementwise product 뒤 activation은 서로 다른 hook 위치다. expert model에서는 router logits, routing probability, 선택 index와 expert 내부 activation도 구분해야 한다.

한 expert가 특정 token에서 자주 선택됐다는 관찰은 그 expert가 해당 행동에 필요하다는 증거가 아니다. routing을 바꾸거나 expert output을 개입하고 load와 대조군을 통제해야 인과 주장을 할 수 있다.

## 흔한 오해

### 오해 1. SwiGLU는 expert를 선택한다

SwiGLU는 한 MLP 안에서 두 dense projection을 feature별로 곱한다. discrete expert 선택이 아니다.

### 오해 2. MoE는 parameter가 적어서 빠르다

전체 parameter는 매우 클 수 있다. token당 일부 expert만 계산해 conditional computation을 얻는다.

### 오해 3. router probability가 높은 expert가 의미를 독점한다

선택 빈도나 probability만으로 expert 내부 계산과 downstream 인과 효과를 알 수 없다.

## 연습문제

### 1. SwiGLU shape

$x:(7,8)$, $W_g$와 $W_u$가 각각 `(16,8)`이면 원소별 곱 직전 두 projection의 shape는?

<details><summary>해설 보기</summary>row-vector convention에서 둘 다 `(7,16)`이다. shape가 같아야 원소별 곱을 할 수 있다.</details>

### 2. output shape

앞 결과에 $W_d:(8,16)$을 적용하면 output shape는?

<details><summary>해설 보기</summary>`(7,8)`이다. residual stream에 더할 수 있는 model dimension으로 돌아온다.</details>

### 3. router probability

expert logits가 $(0,0)$이면 두 probability는?

<details><summary>해설 보기</summary>softmax 결과는 $(0.5,0.5)$다.</details>

### 4. tie

top-1 routing에서 같은 최대 logit이 둘이면 수학식만으로 선택 expert가 유일한가?

<details><summary>해설 보기</summary>유일하지 않다. 구현의 tie-breaking 규칙이 필요하다. PyTorch `argmax`는 같은 최댓값 중 첫 index를 반환한다.</details>

### 5. parameter 해석

expert가 8개이고 token당 1개만 실행하면 전체 expert parameter의 1/8만 저장해도 되는가?

<details><summary>해설 보기</summary>아니다. 일반적으로 8개 expert parameter를 모두 저장하되 그 token의 forward에서는 하나만 선택해 계산한다.</details>

### 6. 주장 비판

수학 token이 expert 3으로 자주 route되므로 expert 3이 수학 능력의 원인이라는 주장을 평가하라.

<details><summary>해설 보기</summary>선택 빈도에 관한 상관 관찰이다. 입력 분포, router confidence, expert output 개입과 행동 대조가 없으므로 인과 결론은 성립하지 않는다.</details>

## 근거와 갱신 경계

Transformer feed-forward sublayer는 [Attention Is All You Need](https://arxiv.org/abs/1706.03762), SwiGLU 식은 [GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202), top-1 routing의 대표 설계는 [Switch Transformers](https://arxiv.org/abs/2101.03961)에 근거한다. expert capacity, auxiliary loss와 dispatch kernel은 architecture와 구현에 따라 달라진다.

## 단원 요약

- dense MLP는 모든 token에 같은 feed-forward parameter를 적용한다.
- SwiGLU는 SiLU gate projection과 content projection을 원소별로 곱한다.
- MoE router는 token마다 실행할 expert를 선택한다.
- 전체 parameter와 token당 활성화되는 parameter는 다르다.
- routing 관찰만으로 expert의 인과 역할을 결론낼 수 없다.

## 통과 기준

- dense MLP와 SwiGLU의 shape를 계산할 수 있는가?
- SwiGLU gate와 expert router를 구분할 수 있는가?
- top-1 routing을 손으로 계산할 수 있는가?
- total parameter와 active parameter를 구분할 수 있는가?
- routing 관찰에 맞는 주장 강도를 선택할 수 있는가?

## 다음 단원

- [N05-20 decoder block과 architecture diff](N05-20-decoder-block-architecture-diff.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] dense·SwiGLU·expert routing을 구분했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
- [x] Markdown에 실행 코드를 손으로 복제하지 않았다.
- [x] 코드 원본·테스트 경로·자원 예산·확인일을 기록했다.
- [x] shape·수치·routing test가 있다.
