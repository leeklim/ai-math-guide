---
id: "N05-20"
title: "decoder block과 architecture diff"
part: 2
stage: "N05"
status: "완료"
prerequisites:
  - "N05-19"
estimated_time: "150~180분"
---

# N05-20. decoder block과 architecture diff

## 이 단원이 필요한 이유

앞 단원에서 분리해 계산한 embedding, attention, normalization, MLP와 residual update를 한 decoder-only model로 연결할 차례다. 동시에 `Transformer`라는 이름 아래 block 순서와 component가 달라질 수 있음을 config 수준에서 구분해야 한다.

## 학습 목표

- token ID부터 logit까지 tiny decoder의 계산 순서를 추적할 수 있다.
- block 안의 주요 tensor shape를 계산할 수 있다.
- 기준 아키텍처와 공개 모델 config의 차이를 표로 정리할 수 있다.
- mathematical component와 implementation optimization을 구분할 수 있다.
- architecture가 다른 모델의 hook 이름을 그대로 대응시키지 않을 수 있다.

## 선수지식 확인

- 선수 단원: [N05-19 dense MLP, SwiGLU와 expert routing](N05-19-dense-mlp-swiglu-expert-routing.md)
- 확인 질문: pre-norm residual block의 attention·MLP update 순서를 식으로 쓸 수 있는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\mathbf X^{(0)}$ | `X at layer zero` | token embedding 뒤 첫 residual stream | $\mathbb R^{B\times T\times d_{model}}$ |
| $\mathbf X^{(l+1)}$ | `X at layer l plus one` | block $l$을 지난 residual stream | 같은 residual shape |
| $\mathbf Z$ | `Z` | final normalization output | $\mathbb R^{B\times T\times d_{model}}$ |
| $\mathbf L$ | `L` | vocabulary logits | $\mathbb R^{B\times T\times V}$ |
| architecture diff | `architecture diff` | 두 모델의 component·순서·shape 선택 차이 | comparison record |
| fused kernel | `fused kernel` | 여러 연산을 한 실행 경로로 합친 구현 | implementation detail |

## 핵심 개념 1. 기준 decoder 경로

교육용 기준 모델은 다음 계산을 사용한다.

\[
\mathbf X^{(0)}=E[\text{input IDs}]
\]

각 block $l$에서

\[
\mathbf U^{(l)}=\mathbf X^{(l)}+
A_l(\operatorname{RMSNorm}(\mathbf X^{(l)}))
\]

\[
\mathbf X^{(l+1)}=\mathbf U^{(l)}+
M_l(\operatorname{RMSNorm}(\mathbf U^{(l)}))
\]

를 계산하고 마지막에

\[
\mathbf Z=\operatorname{RMSNorm}(\mathbf X^{(L)}),
\qquad
\mathbf L=\mathbf Z\mathbf W_U^\top
\]

로 vocabulary logit을 만든다. attention에는 RoPE와 causal MHA, MLP에는 dense SwiGLU를 사용한다.

## 핵심 개념 2. shape ledger

$B=1$, $T=3$, $d_{model}=4$, head 1개, vocabulary 16인 실습의 주요 shape는 다음과 같다.

| 위치 | shape |
|---|---|
| input IDs | $(1,3)$ |
| embedding·residual | $(1,3,4)$ |
| Q·K·V | $(1,1,3,4)$ |
| attention score | $(1,1,3,3)$ |
| attention·MLP update | $(1,3,4)$ |
| logits | $(1,3,16)$ |

residual addition 지점의 두 tensor shape가 같고, 마지막 axis만 unembedding에서 vocabulary size로 바뀐다.

## 핵심 개념 3. architecture diff를 읽는 순서

모델끼리 비교할 때 다음 항목을 따로 확인한다.

1. decoder-only인지 encoder-decoder인지
2. normalization 종류와 위치
3. attention head와 key-value head 수
4. 위치정보와 적용 범위
5. MLP activation과 dense·expert 구조
6. serial·parallel residual 순서
7. embedding-unembedding weight tying
8. cache layout과 fused kernel

수학 함수를 바꾸는 선택과 같은 함수를 빠르게 계산하는 구현을 같은 열에 넣지 않는다.

## Pythia config 대조

Pythia-160M 공개 training config에는 12 layers, hidden size 768, 12 attention heads, RoPE 비율 0.25, `gpt-j-residual: true`, `no-weight-tying: true`와 FlashAttention 사용이 기록돼 있다. 교육용 기준은 1 layer, dimension 4, full-dimension RoPE, serial residual, 명시적 untied unembedding을 사용한다.

따라서 교육용 모델은 Pythia의 축소 복제품이 아니다. 공통 계산을 작은 수치로 검증한 뒤 실제 모델의 차이를 읽기 위한 기준 좌표다.

## 실행 실습

### 실행 환경과 원본

- 환경: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- 확인일: 2026-10-01
- 구성요소 등급: 기준 block은 `Instructional reference`, architecture diff는 `Architecture-specific`
- 공통 구현: `labs/N05/tiny_decoder.py`
- 예제 ID: `n05_20_decoder_block`
- 코드 원본: `labs/N05/n05_20_decoder_block.py`
- 테스트: `tests/N05/test_n05_20.py`
- 실행 명령: `.venv\Scripts\python.exe -m labs.N05.n05_20_decoder_block`

### 자원 예산

batch 1, sequence length 3, dimension 4, layer 1, head 1, vocabulary 16과 parameter 300개를 사용한다.

### 실제 코드와 실행 결과

<!-- N05_EXAMPLE: n05_20_decoder_block -->

### 검사

테스트는 embedding부터 logit까지의 shape, 두 residual addition과 parameter count를 확인한다.

## 모델 해석과의 연결

activation 이름은 계산 위치와 함께 기록해야 한다. `layer 3 hidden state`만으로는 block input, attention update, residual mid, MLP update와 block output 중 어느 tensor인지 알 수 없다.

두 architecture의 layer index가 같아도 계산 깊이와 residual 배치가 다를 수 있다. 표현 비교 전에는 component correspondence를 정하고 대응되지 않는 위치를 억지로 맞추지 않는다.

## 흔한 오해

### 오해 1. decoder block은 모든 모델에서 같은 순서다

normalization, parallel residual, attention variant와 MLP 구조가 달라질 수 있다.

### 오해 2. FlashAttention은 새로운 attention 수식이다

기준 FlashAttention은 exact attention을 memory-efficient하게 계산하는 implementation optimization이다. mask와 수치 정밀도 같은 실행 조건은 따로 확인한다.

### 오해 3. parameter 수가 같으면 activation shape도 같다

head 수, vocabulary, layer 수와 parameter sharing에 따라 내부 shape는 달라질 수 있다.

## 연습문제

### 1. logit shape

$B=2$, $T=5$, vocabulary가 100이면 logit shape는?

<details><summary>해설 보기</summary>$(2,5,100)$이다.</details>

### 2. residual 조건

attention 내부 head를 합친 tensor가 dimension 12이고 residual dimension이 8이면 무엇이 필요한가?

<details><summary>해설 보기</summary>residual addition 전에 output projection으로 마지막 dimension을 8로 바꿔야 한다.</details>

### 3. 순서 추적

기준 block에서 첫 normalization output은 어디에 입력되는가?

<details><summary>해설 보기</summary>causal attention sublayer에 입력된다. 원래 residual은 attention update와 더하기 위해 skip path에 남는다.</details>

### 4. diff 분류

MHA를 GQA로 바꾸는 것과 같은 attention을 fused kernel로 계산하는 것 중 tensor 공유 구조를 바꾸는 것은?

<details><summary>해설 보기</summary>MHA에서 GQA로의 변경이다. fused kernel은 같은 수학 함수를 다른 실행 방식으로 계산한다.</details>

### 5. config 해석

`no-weight-tying: true`는 embedding과 unembedding에 대해 무엇을 뜻하는가?

<details><summary>해설 보기</summary>두 위치가 같은 parameter matrix를 공유하지 않는다는 뜻이다.</details>

### 6. hook 비교

serial residual 모델의 `residual_mid`와 parallel residual 모델에서 무엇을 일대일 대응시키기 어려운가?

<details><summary>해설 보기</summary>parallel 구조에서는 attention update만 더하고 MLP 전 입력으로 쓰는 동일한 중간 stream이 없을 수 있다. 계산 그래프를 보고 대응 가능 여부를 먼저 정해야 한다.</details>

## 근거와 갱신 경계

기준 block의 공통 attention·feed-forward 구조는 [Attention Is All You Need](https://arxiv.org/abs/1706.03762), GPT-NeoX 계열의 공개 설명은 [GPT-NeoX-20B](https://arxiv.org/abs/2204.06745), Pythia 수치는 [Pythia-160M 공식 config](https://github.com/EleutherAI/pythia/blob/main/models/160M/pythia-160m.yml)를 확인했다. 공개 config와 구현은 바뀔 수 있으므로 실제 실험에서는 고정 revision을 사용한다.

## 단원 요약

- tiny decoder는 embedding, pre-norm attention, pre-norm MLP, final norm과 unembedding을 잇는다.
- residual axis는 block 전체에서 $d_{model}$을 유지한다.
- architecture diff는 component, 순서, 공유와 구현을 나눠 읽는다.
- 교육용 기준은 실제 모델의 축소 복제품이 아니라 계산 대조군이다.
- hook 비교에는 정확한 계산 위치의 대응이 필요하다.

## 통과 기준

- token ID에서 logit까지 순서를 그릴 수 있는가?
- 주요 tensor shape를 계산할 수 있는가?
- config에서 architecture 차이를 추출할 수 있는가?
- component 변경과 kernel 최적화를 구분할 수 있는가?
- 대응되지 않는 hook 위치를 식별할 수 있는가?

## 다음 단원

- [N05-21 언어모델 목적함수](N05-21-language-model-objective.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] tiny decoder 전체 경로와 architecture diff를 연결했다.
- [x] Pythia 공식 config를 확인했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
- [x] Markdown에 실행 코드를 손으로 복제하지 않았다.
- [x] 코드 원본·테스트 경로·자원 예산·확인일을 기록했다.
- [x] shape·residual·parameter test가 있다.

