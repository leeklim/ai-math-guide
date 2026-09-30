---
id: "N05-28"
title: "종합 실습: 한 token의 경로"
part: 2
stage: "N05"
status: "완료"
prerequisites:
  - "N05-27"
estimated_time: "180~240분"
---

# N05-28. 종합 실습: 한 token의 경로

## 이 단원이 필요한 이유

N05의 마지막 목표는 component 이름을 외우는 것이 아니라 한 token이 ID에서 logit까지 지나가는 tensor 경로를 재현하는 것이다. 이 종합 실습은 forward activation, residual update, output target의 gradient와 inference cache를 같은 model·input에 연결한다.

## 학습 목표

- 선택 token의 ID부터 vocabulary logit까지 tensor 경로를 순서대로 추적할 수 있다.
- 각 지점의 shape와 residual equality를 검산할 수 있다.
- 선택 logit의 embedding gradient를 수집할 수 있다.
- full causal forward와 cached inference를 대조할 수 있다.
- 관찰·local sensitivity·intervention·checkpoint evidence를 서로 다른 주장으로 분류할 수 있다.

## 선수지식 확인

- 선수 단원: [N05-27 checkpoint와 모델 상태](N05-27-checkpoint-model-state.md)
- 확인 질문: activation hook, scalar target, gradient, KV cache와 model state를 각각 한 문장으로 구분할 수 있는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $x_t$ | `the token at position t` | 선택한 input token ID | integer in $[0,V)$ |
| $\mathbf e_t$ | `the embedding at position t` | embedding table에서 조회한 vector | $\mathbb R^{d_{model}}$ |
| $\Delta\mathbf r_{A,t}$ | `the attention update at position t` | attention이 stream에 쓰는 update | $\mathbb R^{d_{model}}$ |
| $\Delta\mathbf r_{M,t}$ | `the MLP update at position t` | MLP가 stream에 쓰는 update | $\mathbb R^{d_{model}}$ |
| $\ell_{t,v}$ | `the logit for token v at position t` | 선택 position·vocabulary token의 logit | scalar |
| $\nabla_{\mathbf e_t}\ell_{t,v}$ | `the gradient of the logit with respect to the embedding` | selected logit의 embedding local sensitivity | $\mathbb R^{d_{model}}$ |

## 전체 계산 지도

선택 token position $t$의 경로를 다음 순서로 읽는다.

\[
x_t
\rightarrow \mathbf e_t
\rightarrow \operatorname{RMSNorm}
\rightarrow Q_t,K_{\le t},V_{\le t}
\rightarrow \Delta\mathbf r_{A,t}
\rightarrow \mathbf r_{mid,t}
\]

\[
\rightarrow \operatorname{RMSNorm}
\rightarrow \operatorname{SwiGLU}
\rightarrow \Delta\mathbf r_{M,t}
\rightarrow \mathbf r_{out,t}
\rightarrow \operatorname{RMSNorm}
\rightarrow \boldsymbol\ell_t
\]

attention update는 같은 position의 현재 embedding뿐 아니라 causal prefix의 K·V를 통해 앞 token에도 의존한다. 한 token의 경로는 독립된 한 줄 계산이 아니라 다른 position과 연결된 graph의 선택 slice다.

## shape ledger

실습은 $B=1$, $T=4$, $d_{model}=4$, head 1개, layer 1개와 vocabulary 16을 사용한다.

| 대상 | 전체 shape | token $t=2$ slice |
|---|---|---|
| input IDs | $(1,4)$ | scalar ID |
| embedding·residual·update | $(1,4,4)$ | $(4,)$ |
| Q·K·V | $(1,1,4,4)$ | head·position slice $(4,)$ |
| attention score | $(1,1,4,4)$ | allowed prefix 3개 |
| logits | $(1,4,16)$ | $(16,)$ |
| embedding gradient | $(1,4,4)$ | $(4,)$ |

## residual 검산

선택 position에서 반드시

\[
\mathbf r_{mid,t}=\mathbf e_t+\Delta\mathbf r_{A,t}
\]

\[
\mathbf r_{out,t}=\mathbf r_{mid,t}+\Delta\mathbf r_{M,t}
\]

가 성립해야 한다. 이 equality는 component hook을 잘못 잡았는지 찾는 기본 검사다.

## output과 gradient

실습의 token index 2에서 greedy vocabulary index는 15다. 선택 target을 $\ell_{2,15}$로 두고

\[
\nabla_{\mathbf e_2}\ell_{2,15}
\]

를 backward로 구한다. 이 gradient는 같은 weight·input의 기준점에서 embedding perturbation에 대한 local sensitivity다. token 15가 왜 선택됐는지에 대한 완전한 설명은 아니다.

## cache 대조

full forward의 layer별 K·V shape는 `(1,1,4,4)`다. 같은 네 token을 하나씩 넣어 cache를 늘리고 각 step logit을 이어 붙였을 때 full logits와의 최대 절대 차이는 약 $1.19\times10^{-7}$이다. tolerance 아래 같은 causal function을 재현한다.

## 실행 실습

### 실행 환경과 원본

- 환경: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- 확인일: 2026-10-01
- 구성요소 등급: N05 `Instructional reference` 종합 실습
- 공통 구현: `labs/N05/tiny_decoder.py`
- 예제 ID: `n05_28_token_path`
- 코드 원본: `labs/N05/n05_28_token_path.py`
- 테스트: `tests/N05/test_n05_28.py`
- 실행 명령: `.venv\Scripts\python.exe -m labs.N05.n05_28_token_path`

### 자원 예산

parameter 300개의 model에서 sequence length 4 full forward·backward와 tokenwise cached forward를 실행한다. model download와 training은 없다.

### 실제 코드와 실행 결과

<!-- N05_EXAMPLE: n05_28_token_path -->

### 검사

테스트는 아홉 activation·gradient slice의 shape, 두 residual equality, predicted token, nonzero gradient, K·V cache shape와 cached logit equivalence를 확인한다.

## 증거 층을 분리하기

이 실습에서 얻는 증거는 다음처럼 구분한다.

- forward trace: 실제로 관찰된 activation과 shape
- gradient: 선택 target의 기준점 주변 local sensitivity
- intervention: activation을 바꾼 뒤 측정한 conditional effect
- checkpoint comparison: 학습 시점 사이의 state·behavior 차이

한 층의 결과를 다른 층의 결론으로 자동 승격하지 않는다. 예를 들어 nonzero gradient는 feature의 필요성 증거가 아니고 checkpoint 차이는 특정 training example의 원인 효과가 아니다.

## architecture 경계

교육용 model은 full-dimension RoPE, causal MHA, serial pre-RMSNorm residual과 dense SwiGLU를 사용한다. Pythia는 partial RoPE, GPT-J parallel residual, GELU 계열 MLP와 다른 normalization·implementation profile을 갖는다. 후속 실제 모델 실험에서는 module path와 tensor 위치를 Pythia code에 맞춰 다시 지정한다.

tiny decoder에서 확인한 것은 공통 수학과 검사 절차다. hook 이름과 모든 intermediate value가 architecture를 넘어 그대로 대응한다는 뜻은 아니다.

## 흔한 오해

### 오해 1. 한 token의 경로는 그 token 내부에서만 닫힌다

causal attention으로 과거 token의 K·V와 연결된다.

### 오해 2. predicted token의 gradient만 보면 생성 이유가 완전히 설명된다

한 target의 local sensitivity를 본 것이다. 대안 target, nonlinear effect와 distributed path가 남는다.

### 오해 3. tiny model hook path를 Pythia에 그대로 쓰면 된다

architecture와 implementation이 다르므로 config와 forward code에서 대응 위치를 다시 찾아야 한다.

## 누적 확인과제

### 1. ID에서 embedding

token ID 2가 embedding vector로 바뀌는 연산과 output shape를 적어라.

<details><summary>해설 보기</summary>embedding table의 row lookup $E[2]$다. 한 token slice는 $(d_{model},)=(4,)$다.</details>

### 2. causal prefix

zero-based position 2의 query가 볼 수 있는 key position은?

<details><summary>해설 보기</summary>0, 1, 2다. position 3은 미래라 mask된다.</details>

### 3. residual equality

embedding $(1,0)$과 attention update $(0.2,-0.3)$의 residual mid를 구하라.

<details><summary>해설 보기</summary>원소별로 더해 $(1.2,-0.3)$이다.</details>

### 4. MLP 경로

SwiGLU에서 같은 hidden shape가 필요한 두 tensor는?

<details><summary>해설 보기</summary>$\operatorname{SiLU}(W_gx)$와 $W_ux$다. 둘을 원소별로 곱한다.</details>

### 5. logit 선택

logits shape가 `(16,)`이면 greedy token을 어떻게 구하는가?

<details><summary>해설 보기</summary>vocabulary axis의 `argmax` index를 구한다.</details>

### 6. gradient 해석

$\nabla_{e_t}\ell_{t,v}$가 nonzero라는 가장 제한된 결론은?

<details><summary>해설 보기</summary>기준점에서 embedding의 작은 변화가 선택 logit을 일차적으로 바꿀 수 있다는 local sensitivity evidence다.</details>

### 7. cache 검산

layer 2개, K·V head 2개, length 8, head dimension 4, batch 1의 K와 V 전체 element 수는?

<details><summary>해설 보기</summary>$2\times L\times B\times h_{kv}\times T\times d_h=2\times2\times1\times2\times8\times4=256$개다.</details>

### 8. 실제 모델 이전

Pythia에서 같은 분석을 하기 전에 추가로 확인할 항목 네 가지를 적어라.

<details><summary>해설 보기</summary>model·tokenizer revision, config의 layer·head·RoPE·residual 구조, 정확한 module path·hook output type, dtype·device·cache layout을 확인한다. input token index와 target도 고정한다.</details>

## 근거와 갱신 경계

attention·residual·decoder 계산은 [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 교육용 variant는 [RMSNorm](https://arxiv.org/abs/1910.07467), [RoFormer](https://arxiv.org/abs/2104.09864)와 [GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202)에 근거한다. Pythia 대응 경계는 [공식 Pythia repository와 config](https://github.com/EleutherAI/pythia)를 확인했다.

## 단원 요약

- 한 token의 경로는 embedding, attention, 두 residual update, final norm과 logits를 잇는다.
- shape ledger와 residual equality가 hook 위치를 검산한다.
- 선택 logit gradient는 embedding의 local sensitivity를 나타낸다.
- cached inference는 full causal logits와 tolerance 아래 일치해야 한다.
- tiny model의 수학적 검사 절차와 실제 model의 module 대응을 분리한다.

## 통과 기준

- token ID부터 logit까지 경로를 재현할 수 있는가?
- 모든 주요 shape와 residual equality를 검산할 수 있는가?
- 선택 logit의 embedding gradient를 수집할 수 있는가?
- cached·full logits와 K·V shape를 대조할 수 있는가?
- 네 증거 층에 맞는 주장 강도를 선택할 수 있는가?

## 다음 단계

- I06-01 행동 질문과 표현 질문은 Phase 3의 GPU·Pythia 기반을 만든 뒤 집필한다.

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] token ID부터 logit까지 누적 경로를 연결했다.
- [x] residual·gradient·cache를 같은 input에서 검증했다.
- [x] N05 누적 확인과제를 포함했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
- [x] Markdown에 실행 코드를 손으로 복제하지 않았다.
- [x] 코드 원본·테스트 경로·자원 예산·확인일을 기록했다.
- [x] shape·residual·gradient·cache equivalence test가 있다.
