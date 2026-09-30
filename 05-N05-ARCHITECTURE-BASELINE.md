# N05 아키텍처와 자료 기준

## 1. 목적

N05는 특정 제품이나 최신 모델 한 개를 설명하지 않는다. 학습자는 이 단계를 마친 뒤 공개 모델의 config와 계산 그래프를 읽고, 각 구성요소를 공통 계산과 모델별 선택으로 나눌 수 있어야 한다.

이 문서는 N05의 기준 아키텍처, 구성요소 등급, 자료 선택과 갱신 규칙을 정한다. 최초 확인일은 2026-10-01이다. N05 단원 배치를 시작할 때마다 원 논문과 공개 config를 다시 확인하고 확인일을 갱신한다.

## 2. 구성요소 등급

| 등급 | 판정 기준 | 본문 처리 |
|---|---|---|
| Stable core | token에서 logit까지 계산하거나 backward pass를 추적하는 데 필요하다. 여러 아키텍처가 같은 수학 구조를 공유한다. | 정의, shape, 손계산과 코드 실습을 모두 제공한다. |
| Instructional reference | Stable core를 한 모델로 연결하기 위해 프로젝트가 고정한 선택이다. | 모든 누적 실습에서 같은 선택을 사용한다. |
| Common modern variant | 공개 모델 계열 여러 곳에서 쓰이며 tensor shape, 정보 경로 또는 저장 상태를 바꾼다. | 기준 계산에서 무엇이 유지되고 무엇이 달라지는지 비교한다. |
| Architecture-specific | 특정 계열의 성능이나 효율을 위한 선택이며 공통 전제로 삼기 어렵다. | architecture profile이나 선택 읽을거리로 분리한다. |
| Implementation optimization | 같은 수학 함수를 다른 메모리 접근이나 kernel로 계산한다. | 수학적 출력과 실행 방식의 차이를 확인한다. |

다음 조건을 모두 만족하면 새 구성요소를 Common modern variant 이상으로 올릴 수 있다.

1. 원 논문이나 공식 기술 보고서가 계산을 명시한다.
2. 공개 config 또는 구현으로 tensor shape과 데이터 흐름을 확인할 수 있다.
3. 학습자가 activation, gradient, residual stream 또는 모델 상태를 해석할 때 차이가 생긴다.
4. 서로 독립적인 공개 모델 계열 둘 이상에서 사용 사례를 확인했거나, 한 계열에 머물더라도 후속 해석 단원의 필수 대상이다.

논문 발표 시점, leaderboard 순위와 제품 인지도만으로 등급을 올리지 않는다.

## 3. 교육용 기준 아키텍처

N05의 누적 실습은 작은 decoder-only causal language model을 직접 구현한다. 기준 모델은 다음 선택을 사용한다.

| 위치 | 기준 선택 | 비교 대상 |
|---|---|---|
| block 순서 | pre-norm decoder block | post-norm |
| normalization | RMSNorm | LayerNorm |
| 위치정보 | RoPE | learned absolute embedding, sinusoidal encoding |
| attention | causal multi-head attention | MQA, GQA |
| MLP | dense SwiGLU feed-forward network | ReLU, GELU, ordinary GLU, MoE |
| residual | attention과 MLP 출력의 residual addition | parallel residual 등 모델별 배치 |
| 출력 | 명시적인 unembedding과 softmax | input-output weight tying |
| 학습 | cross entropy와 AdamW | optimizer와 schedule 변형 |
| 추론 상태 | causal mask와 KV cache | cache가 없는 전체 재계산 |

multi-head attention과 dense MLP를 기준으로 삼으면 head와 token별 계산 경로를 직접 추적할 수 있다. GQA와 MoE는 기준 계산을 이해한 뒤 head 공유와 conditional routing의 차이로 배운다.

실습 구현은 교육용 행렬 연산을 먼저 사용한다. fused kernel이나 FlashAttention을 도입할 때 같은 입력에 대한 출력과 gradient를 기준 구현과 대조한다.

## 4. 현재 구성요소 분류

| 구성요소 | 등급 | N05 처리 |
|---|---|---|
| tensor shape, affine map, activation, softmax, cross entropy | Stable core | N05-01~05 |
| backpropagation, mini-batch, optimizer state, autograd | Stable core | N05-06~10 |
| tokenization, embedding, unembedding | Stable core | N05-11~12 |
| causal scaled dot-product attention과 residual addition | Stable core | N05-14~17 |
| RoPE, RMSNorm, SwiGLU | Instructional reference | 단순한 선행 방식과 같은 단원에서 비교한다. |
| MHA | Instructional reference | 모든 head의 query, key와 value를 명시한다. |
| MQA와 GQA | Common modern variant | key-value head 공유와 cache shape 변화를 계산한다. |
| KV cache | Common modern variant | 학습 계산과 autoregressive inference 상태를 구분한다. |
| FlashAttention과 fused attention kernel | Implementation optimization | attention 정의와 분리한다. |
| MoE와 expert routing | Architecture-specific | dense MLP와의 계산 경로 차이만 필수로 다룬다. |
| MLA, sparse·linear attention, SSM과 hybrid block | Architecture-specific | architecture profile에 기록하고 공통 선수지식으로 요구하지 않는다. |
| quantization과 speculative decoding | Architecture-specific | 수치 표현 또는 시스템 최적화 선택 단원으로 보낸다. |

## 5. 실습 모델과 외부 모델

필수 실습은 CPU에서도 실행할 수 있는 tiny decoder를 사용한다. 단원 본문은 특정 라이브러리의 고수준 Transformer block을 정답으로 삼지 않는다.

실행 환경과 자원 제한은 [N05 실행 환경](N05-ENVIRONMENT.md)을 따른다. 코드 원본은 `labs/N05`의 `.py` 파일이며, test와 site build는 같은 파일을 import하거나 실행한다. N05-01~N05-03 파일럿에서 이 경로를 검증했고 후속 단원도 같은 방식으로 확장한다.

외부 모델은 두 목적으로만 사용한다.

- 공개 config와 실제 tensor shape을 기준 모델과 대조한다.
- hook, checkpoint와 학습 동역학 실험이 필요한 후속 단원에서 재현 자료를 사용한다.

외부 모델을 정할 때 공개 가중치만 보지 않는다. config, tokenizer, forward 구현, 라이선스와 필요한 계산 자원을 함께 확인한다. Pythia처럼 여러 훈련 checkpoint와 데이터 순서를 제공하는 모델은 I08의 학습 동역학 실습 후보로 둔다. N05의 필수 계산은 외부 모델을 다운로드하지 않아도 수행할 수 있어야 한다.

## 6. 자료 우선순위

단원에서 아키텍처 사실을 확인할 때 다음 순서를 따른다.

1. 원 논문
2. 공식 기술 보고서
3. 공개 config와 forward 구현
4. 공식 모델 카드와 훈련 기록
5. 재현 논문

survey, 강의와 블로그는 탐색에 사용할 수 있지만 핵심 계산의 단독 근거로 사용하지 않는다. 비공개 모델은 확인할 수 있는 사실만 architecture profile에 적는다.

초기 기준을 정할 때 확인한 1차 자료는 다음과 같다.

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [Root Mean Square Layer Normalization](https://arxiv.org/abs/1910.07467)
- [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864)
- [GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202)
- [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://arxiv.org/abs/2305.13245)
- [FlashAttention](https://arxiv.org/abs/2205.14135)
- [OpenELM](https://arxiv.org/abs/2404.14619)
- [Pythia](https://arxiv.org/abs/2304.01373)
- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

## 7. 단원별 기록 형식

N05 단원은 아키텍처 구성요소를 다룰 때 다음 항목을 포함한다.

- 상태: `Stable core`, `Instructional reference`, `Common modern variant`, `Architecture-specific`, `Implementation optimization` 중 하나
- 확인일: `YYYY-MM-DD`
- 기준 계산: 입력·출력 shape과 핵심 식
- 비교 대상: 무엇을 공유하고 무엇을 바꾸는가
- 해석 영향: activation, gradient, cache와 개입 위치 중 달라지는 항목
- 근거: 원 논문과 확인한 공개 config 또는 구현

N05 집필자는 N05-10, N05-20과 N05-28을 마친 뒤 이 문서와 구성요소 분류를 다시 검토한다. 새 논문이 나왔다는 이유만으로 완료한 단원을 고치지 않는다. 기존 설명의 오류가 드러나거나 구성요소 등급이 바뀔 근거가 쌓이면 단원과 확인일을 함께 갱신한다.

## 8. N05-10 재검토 기록

- 확인일: 2026-10-01
- 범위: N05-01~N05-10
- 결과: tensor, activation, softmax, cross entropy, backpropagation, mini-batch, optimizer state와 automatic differentiation의 `Stable core` 분류를 유지한다.
- API 확인: local PyTorch 2.13.0+cpu에서 `torch.func.jvp`, `vjp`와 `jacrev`를 실행하고 current stable 공식 문서의 정의와 대조했다.
- 공개 config: N05-01~N05-10은 model-independent 계산이므로 특정 model config를 근거로 추가하지 않았다. Transformer component를 다루는 N05-11 이후에 공개 config 대조를 시작한다.
