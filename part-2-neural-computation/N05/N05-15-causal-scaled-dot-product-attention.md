---
id: "N05-15"
title: "causal scaled dot-product attention"
part: 2
stage: "N05"
status: "완료"
prerequisites:
  - "N05-14"
estimated_time: "120~150분"
---

# N05-15. causal scaled dot-product attention

## 이 단원이 필요한 이유

attention output은 QK score 하나로 정해지지 않는다. score를 head dimension으로 scale하고, causal mask로 미래 위치를 제외하고, softmax로 정규화한 뒤 value를 가중합해야 한다. 이 순서를 알아야 attention map과 실제 output을 구분해 해석할 수 있다.

## 학습 목표

- scaled dot-product attention을 순서대로 계산할 수 있다.
- causal mask가 막는 score 위치를 표시할 수 있다.
- attention weight의 행 합과 output shape를 검산할 수 있다.
- attention weight와 value-weighted output의 주장을 구분할 수 있다.
- mask를 적용하는 시점이 잘못된 코드를 찾을 수 있다.

## 선수지식 확인

- 선수 단원: [N05-14 query, key와 value](N05-14-query-key-value.md)
- 확인 질문: QK transpose의 row와 column이 가리키는 position을 설명할 수 있는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $d_k$ | `d sub k` | 한 key 또는 query head의 dimension | positive integer |
| $S_{ij}$ | `S sub i j` | scaled attention score | scalar |
| $M_{ij}$ | `M sub i j` | 허용 여부를 나타내는 additive mask | $0$ 또는 $-\infty$ |
| $A_{ij}$ | `A sub i j` | query $i$가 value $j$에 주는 attention weight | $[0,1]$ |
| $\mathbf O$ | `O` | value를 가중합한 attention output | $\mathbb R^{T\times d_v}$ |

## 핵심 개념 1. scale

한 head의 score는

\[
\mathbf S=\frac{\mathbf Q\mathbf K^\top}{\sqrt{d_k}}
\]

이다. $d_k$가 커질 때 dot product의 크기가 함께 커지는 효과를 완화한다. 분모는 model dimension $d_{model}$이 아니라 해당 head의 query-key dimension이다.

## 핵심 개념 2. causal mask

왼쪽에서 오른쪽으로 생성하는 decoder에서 query position $i$는 미래 key position $j>i$를 볼 수 없다. additive mask를

\[
M_{ij}=\begin{cases}
0,&j\le i,\\
-\infty,&j>i
\end{cases}
\]

로 두면 masked score는 $\widetilde{\mathbf S}=\mathbf S+\mathbf M$이다. softmax 전에 $-\infty$가 된 위치의 probability는 0이 된다.

## 핵심 개념 3. softmax와 value 가중합

\[
A_{ij}=\frac{\exp(\widetilde S_{ij})}
{\sum_{r=1}^{T}\exp(\widetilde S_{ir})},
\qquad
\mathbf O=\mathbf A\mathbf V
\]

이다. softmax는 각 query row에서 계산하므로 $\sum_j A_{ij}=1$이다. output row $\mathbf o_i$는 허용된 value row들의 convex combination이다.

## 예제

N05-14의 Q·K·V를 사용하면 scaled score는 약

\[
\mathbf S=
\begin{bmatrix}
0.7071&3.5355\\
3.5355&12.0208
\end{bmatrix}
\]

이다. 첫 query의 미래 score를 가리면 첫 attention row는 $(1,0)$이 된다. 둘째 query는 두 key를 모두 볼 수 있어 약 $(0.000206,0.999794)$를 얻는다. 따라서 output은

\[
\mathbf O\approx
\begin{bmatrix}
2&1\\
5.9992&1.9998
\end{bmatrix}
\]

이다.

## 실행 실습

### 실행 환경과 원본

- 환경: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- 확인일: 2026-10-01
- 구성요소 등급: `Stable core`
- 예제 ID: `n05_15_causal_attention`
- 코드 원본: `labs/N05/n05_15_causal_attention.py`
- 테스트: `tests/N05/test_n05_15.py`
- 실행 명령: `.venv\Scripts\python.exe -m labs.N05.n05_15_causal_attention`

### 자원 예산

sequence length 2, head dimension 2와 head 1개를 사용한다. 모델 다운로드나 학습은 없다.

### 실제 코드와 실행 결과

<!-- N05_EXAMPLE: n05_15_causal_attention -->

### 검사

테스트는 masked score의 $-\infty$, attention row sum, 첫 query의 미래 probability와 output 수치를 확인한다.

## 구현에서 보이는 다른 mask 표현

구현은 boolean mask를 `masked_fill`에 넘기거나, 매우 작은 유한값을 score에 더하거나, causal option이 있는 fused kernel을 쓸 수 있다. 표현은 달라도 미래 position의 probability가 0이고 허용된 각 row의 probability 합이 1이어야 한다.

padding mask는 sequence의 무효 token을 제외하고 causal mask는 시간 순서를 제한한다. 둘은 동시에 적용할 수 있지만 같은 개념은 아니다.

## 모델 해석과의 연결

attention weight $A_{ij}$는 query $i$가 value position $j$를 섞는 계수다. 그러나 최종 logit에 미친 영향은 value vector, output projection, residual addition과 이후 layer에 달려 있다. attention weight가 크다는 사실은 연결 강도에 관한 관찰이지 인과적 설명의 완결이 아니다.

mask를 바꾸는 intervention은 모델이 이용할 수 있는 정보 경로 자체를 바꾼다. 특정 attention weight만 관찰하는 것보다 강한 조작이므로 원래 모델의 동작과 intervention 뒤 동작을 구분해 보고해야 한다.

## 흔한 오해

### 오해 1. mask는 softmax 뒤에 곱하면 같다

softmax 뒤에 0을 곱하면 남은 weight의 합이 1이 아니게 된다. 다시 정규화하지 않는 한 같은 연산이 아니다.

### 오해 2. scale은 sequence length로 한다

기준식의 분모는 $\sqrt{d_k}$다.

### 오해 3. attention weight가 곧 token 기여도다

weight는 value를 섞기 전 계수다. value와 downstream 경로를 제외한 기여도 결론은 성립하지 않는다.

## 연습문제

### 1. scale 계산

$d_k=16$이면 raw score를 무엇으로 나누는가?

<details><summary>해설 보기</summary>$\sqrt{16}=4$로 나눈다.</details>

### 2. causal mask

길이 3인 sequence에서 query index 1이 볼 수 없는 zero-based key index는?

<details><summary>해설 보기</summary>미래인 index 2다. index 0과 1은 허용된다.</details>

### 3. 첫 row

causal self-attention의 첫 query row에서 padding이 없다면 attention weight는 어떻게 되는가?

<details><summary>해설 보기</summary>자기 위치만 허용되므로 첫 key에 1, 나머지 미래 key에 0이다.</details>

### 4. output shape

$A:(5,5)$, $V:(5,8)$이면 output shape는?

<details><summary>해설 보기</summary>$AV:(5,8)$이다.</details>

### 5. 코드 진단

masked position의 softmax probability가 0.2라면 가장 먼저 무엇을 확인해야 하는가?

<details><summary>해설 보기</summary>mask가 softmax 전에 score에 적용됐는지와 mask 방향이 올바른지 확인한다.</details>

### 6. 주장 비판

어떤 head가 한 token에 weight 0.9를 주므로 그 token이 예측의 원인이라는 주장을 평가하라.

<details><summary>해설 보기</summary>attention pattern은 관찰됐지만 value, output projection과 downstream 경로를 검사하지 않았고 인과 intervention도 없으므로 원인이라고 결론낼 수 없다.</details>

## 근거와 갱신 경계

scaled dot-product attention 식은 [Attention Is All You Need](https://arxiv.org/abs/1706.03762)의 정의를 따른다. fused attention kernel의 API와 mask 표현은 바뀔 수 있으므로 구현별 문서를 따로 확인한다.

## 단원 요약

- QK score를 $\sqrt{d_k}$로 나눈다.
- causal mask는 softmax 전에 미래 score를 제외한다.
- softmax는 각 query row를 probability distribution으로 만든다.
- attention output은 weight와 value의 행렬곱이다.
- attention weight만으로 최종 예측의 인과 기여를 확정할 수 없다.

## 통과 기준

- scaled score를 손으로 계산할 수 있는가?
- causal mask의 허용 영역을 표시할 수 있는가?
- attention row sum과 output shape를 검산할 수 있는가?
- mask 적용 순서 오류를 찾을 수 있는가?
- attention pattern과 인과 설명을 구분할 수 있는가?

## 다음 단원

- [N05-16 MHA, MQA와 GQA](N05-16-mha-mqa-gqa.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] scale·mask·softmax·value 가중합 순서를 설명했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
- [x] Markdown에 실행 코드를 손으로 복제하지 않았다.
- [x] 코드 원본·테스트 경로·자원 예산·확인일을 기록했다.
- [x] shape·수치·mask test가 있다.

