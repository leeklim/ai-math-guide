---
id: "N05-17"
title: "residual stream"
part: 2
stage: "N05"
status: "완료"
prerequisites:
  - "N05-16"
estimated_time: "120~150분"
---

# N05-17. residual stream

## 이 단원이 필요한 이유

Transformer block의 attention과 MLP는 새 hidden state를 처음부터 만드는 대신 같은 residual stream에 update를 더한다. 어느 activation을 관찰하거나 바꿨는지 말하려면 block input, sublayer output과 덧셈 뒤 stream을 구분해야 한다.

## 학습 목표

- residual update 식을 tensor shape과 함께 계산할 수 있다.
- attention·MLP output이 stream에 더해지는 순서를 추적할 수 있다.
- skip path가 gradient에 주는 항을 식으로 확인할 수 있다.
- residual stream 위치와 sublayer 내부 activation을 구분할 수 있다.
- stream decomposition의 관찰과 인과 주장을 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [N05-16 MHA, MQA와 GQA](N05-16-mha-mqa-gqa.md)
- 확인 질문: attention output의 마지막 dimension이 residual input과 같아야 하는 이유를 설명할 수 있는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\mathbf R^{(l)}$ | `R at layer l` | layer $l$ 입구의 residual stream | $\mathbb R^{B\times T\times d_{model}}$ |
| $\Delta\mathbf R_A$ | `attention update` | attention sublayer가 stream에 더하는 update | residual과 같은 shape |
| $\Delta\mathbf R_M$ | `MLP update` | MLP sublayer가 stream에 더하는 update | residual과 같은 shape |
| skip path | `skip path` | sublayer를 거치지 않고 항등적으로 이어지는 경로 | identity map |
| residual addition | `residual addition` | stream과 update의 원소별 덧셈 | shape-preserving |

## 핵심 개념 1. 같은 공간에 더한다

정규화 위치를 잠시 생략하면 한 block은

\[
\mathbf R_{mid}=\mathbf R_{in}+A(\mathbf R_{in}),
\qquad
\mathbf R_{out}=\mathbf R_{mid}+M(\mathbf R_{mid})
\]

로 적을 수 있다. $A$는 attention sublayer, $M$은 MLP sublayer다. 두 update가 더해지려면 $A$와 $M$의 최종 output dimension이 $d_{model}$이어야 한다.

`residual stream`은 별도의 module 이름이라기보다 block 사이를 이어 가며 update가 누적되는 표현 경로를 가리킨다.

## 핵심 개념 2. update를 따라가는 법

$\mathbf R_{mid}$를 볼 때는 attention output만 본 것이 아니다. 이전 stream과 attention update의 합을 본 것이다. 마찬가지로 $\mathbf R_{out}$은 입력, attention update와 MLP update가 누적된 결과다. 단, MLP update 자체도 $\mathbf R_{mid}$에 의존하므로 세 항을 독립적인 고정 vector처럼 취급하면 안 된다.

## 핵심 개념 3. gradient의 skip term

단순 residual map $\mathbf y=\mathbf x+F(\mathbf x)$의 Jacobian은

\[
\frac{\partial\mathbf y}{\partial\mathbf x}
=\mathbf I+J_F(\mathbf x)
\]

이다. 역전파에는 sublayer Jacobian 경로뿐 아니라 identity path의 항이 있다. 이것이 gradient가 항상 안정적이라는 보장은 아니지만, skip path를 제거한 $J_F$만의 연쇄와는 다른 계산이다.

## 예제

실습은 두 token의 2차원 stream에 선형 attention update와 MLP update를 차례로 더한다.

\[
\mathbf R_{in}=
\begin{bmatrix}1&-1\\2&0\end{bmatrix},
\quad
\Delta\mathbf R_A=
\begin{bmatrix}0.5&0.5\\1&0\end{bmatrix}
\]

이면 $\mathbf R_{mid}=\begin{bmatrix}1.5&-0.5\\3&0\end{bmatrix}$다. MLP update를 더한 최종 stream은

\[
\mathbf R_{out}=
\begin{bmatrix}1.375&-0.125\\3&0.75\end{bmatrix}
\]

이다.

## 실행 실습

### 실행 환경과 원본

- 환경: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- 확인일: 2026-10-01
- 구성요소 등급: `Stable core`
- 예제 ID: `n05_17_residual_stream`
- 코드 원본: `labs/N05/n05_17_residual_stream.py`
- 테스트: `tests/N05/test_n05_17.py`
- 실행 명령: `.venv\Scripts\python.exe -m labs.N05.n05_17_residual_stream`

### 자원 예산

batch 1, sequence length 2, model dimension 2와 block 1개에 해당하는 계산만 수행한다.

### 실제 코드와 실행 결과

<!-- N05_EXAMPLE: n05_17_residual_stream -->

### 검사

테스트는 두 residual addition의 값과 input stream에 대한 loss gradient를 손계산에 대조한다.

## 모델 해석과의 연결

residual stream을 특정 방향으로 projection하면 그 방향의 성분이 layer를 따라 어떻게 바뀌는지 관찰할 수 있다. 이때 layer 사이 차이는 해당 구간의 update와 연결되지만, projection 값 하나가 독립된 의미 단위임을 자동으로 보장하지 않는다.

stream에 vector를 더하거나 component output을 제거하는 것은 실제 activation을 바꾸는 intervention이다. 반면 stream을 읽어 plot만 만드는 것은 관찰이다. 두 증거를 같은 강도로 보고하지 않는다.

## 흔한 오해

### 오해 1. residual stream은 attention output이다

attention output은 stream에 더하는 update다. 덧셈 뒤 stream에는 이전 정보도 남는다.

### 오해 2. layer output을 component별 고정 vector의 합으로만 보면 충분하다

뒤 component의 update는 앞에서 갱신된 stream에 의존한다. 계산 순서를 함께 봐야 한다.

### 오해 3. identity path가 있으므로 gradient vanishing은 불가능하다

Jacobian에 identity term이 생기지만 전체 network의 normalization, sublayer Jacobian과 loss curvature가 여전히 영향을 준다.

## 연습문제

### 1. shape 조건

residual이 `(2,5,8)`이면 attention output projection의 최종 shape는?

<details><summary>해설 보기</summary>원소별로 더해야 하므로 `(2,5,8)`이다.</details>

### 2. 한 번의 update

$r=(1,2)$, attention update가 $(-0.5,1)$이면 덧셈 뒤 stream은?

<details><summary>해설 보기</summary>$(0.5,3)$이다.</details>

### 3. 두 번의 update

앞 결과에 MLP update $(2,-1)$을 더하라.

<details><summary>해설 보기</summary>$(2.5,2)$다.</details>

### 4. Jacobian

$F(x)=2x$이고 $y=x+F(x)$이면 $dy/dx$는?

<details><summary>해설 보기</summary>$1+2=3$이다. 1은 skip path의 derivative다.</details>

### 5. hook 위치

attention이 stream에 쓴 update만 저장하려면 덧셈 전후 stream 중 하나만 저장해도 충분한가?

<details><summary>해설 보기</summary>두 stream의 차이를 취하면 update를 얻을 수 있지만 normalization이나 다른 연산이 사이에 없는지 확인해야 한다. 가장 직접적인 위치는 attention output projection 뒤, residual addition 전이다.</details>

### 6. 주장 비판

한 방향의 residual projection이 커졌으므로 그 feature가 행동의 원인이라는 주장을 평가하라.

<details><summary>해설 보기</summary>방향 성분의 변화는 관찰이다. 행동과의 인과 관계에는 해당 방향을 조작하고 적절한 대조군과 output 변화를 확인하는 절차가 필요하다.</details>

## 근거와 갱신 경계

residual connection을 둔 Transformer block은 [Attention Is All You Need](https://arxiv.org/abs/1706.03762)에 근거한다. residual stream을 component update가 쓰고 읽는 공통 공간으로 분석하는 표기는 [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html)를 참고한다. module 이름과 hook 위치는 구현마다 다르다.

## 단원 요약

- attention과 MLP는 같은 residual stream에 update를 더한다.
- sublayer output과 덧셈 뒤 stream은 다른 activation이다.
- residual Jacobian에는 identity path 항이 있다.
- 뒤 update는 앞에서 갱신된 stream에 의존한다.
- stream 관찰과 stream intervention은 서로 다른 증거다.

## 통과 기준

- residual update를 shape과 함께 계산할 수 있는가?
- block 안의 stream 위치를 순서대로 표시할 수 있는가?
- residual Jacobian의 identity term을 설명할 수 있는가?
- component output과 stream을 구분할 수 있는가?
- 관찰과 intervention 주장을 구분할 수 있는가?

## 다음 단원

- [N05-18 LayerNorm, RMSNorm과 residual 순서](N05-18-layernorm-rmsnorm-residual-order.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] residual update와 gradient path를 연결했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
- [x] Markdown에 실행 코드를 손으로 복제하지 않았다.
- [x] 코드 원본·테스트 경로·자원 예산·확인일을 기록했다.
- [x] shape·수치·gradient test가 있다.

