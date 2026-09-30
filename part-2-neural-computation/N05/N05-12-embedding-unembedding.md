---
id: "N05-12"
title: "embedding과 unembedding"
part: 2
stage: "N05"
status: "완료"
prerequisites:
  - "N05-11"
estimated_time: "120~150분"
---

# N05-12. embedding과 unembedding

## 이 단원이 필요한 이유

token ID는 범주 index다. embedding table은 각 ID를 연속 vector로 바꾸고, unembedding은 마지막 hidden vector를 vocabulary logit으로 바꾼다. 두 행렬의 row와 column을 정확히 알아야 token별 activation과 logit을 연결할 수 있다.

## 학습 목표

- token ID lookup을 embedding matrix의 row 선택으로 표현할 수 있다.
- embedding과 unembedding의 shape를 검산할 수 있다.
- hidden state에서 vocabulary logit을 계산할 수 있다.
- weight tying과 untied weight를 구분할 수 있다.
- 선택된 embedding row의 gradient sparsity를 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [N05-11 token과 tokenizer](N05-11-token-tokenizer.md)
- 확인 질문: integer index로 matrix row를 선택할 수 있는가?
- 확인 질문: $(T,d)(d,V)$의 결과 shape를 구할 수 있는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\mathbf E$ | `E` | embedding matrix | $\mathbb R^{V\times d}$ |
| $a_t$ | `a sub t` | position $t$의 token ID | $\{0,\ldots,V-1\}$ |
| $\mathbf h_t$ | `h sub t` | token embedding 또는 hidden state | $\mathbb R^d$ |
| $\mathbf U$ | `U` | unembedding matrix | $\mathbb R^{V\times d}$ |
| $\mathbf z_t$ | `z sub t` | vocabulary logit vector | $\mathbb R^V$ |
| weight tying | `weight tying` | $\mathbf U$와 $\mathbf E$가 parameter를 공유하는 선택 | architecture option |

## 핵심 개념 1. embedding은 row lookup이다

token ID $a_t$의 embedding은

\[
\mathbf h_t=\mathbf E[a_t]
\]

이다. sequence ID tensor가 $(B,T)$이면 embedding output은 $(B,T,d)$다. ID의 숫자 크기는 vector 크기나 의미 순서를 나타내지 않는다.

## 핵심 개념 2. unembedding은 hidden을 logit으로 보낸다

\[
\mathbf z_t=\mathbf U\mathbf h_t+\mathbf b
\]

이며 row-batch 표기에서는 $\mathbf H\mathbf U^\top+\mathbf b$다. output의 마지막 axis 길이는 vocabulary size $V$다. softmax는 그다음에 적용한다.

## 핵심 개념 3. tying은 공유 선택이다

weight tying은 보통 unembedding weight를 embedding weight와 공유한다. shape가 같다는 사실만으로 parameter가 자동 공유되지는 않는다. Pythia 공개 config는 `tie_word_embeddings: false`를 사용하므로 두 weight를 구분한다.

## 예제

$V=4$, $d=3$인 table에서 ID $(0,2)$를 고르면 embedding row 0과 2가 hidden이 된다. 실습의 unembedding을 적용한 logit은

\[
\begin{bmatrix}1&0&0&-1\\0&0&1&0.5\end{bmatrix}
\]

이다. shape는 $(2,4)$다. target loss를 backward하면 선택되지 않은 embedding row 1과 3의 gradient는 0이다.

## 실행 실습

### 실행 환경과 원본

- 환경: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- 확인일: 2026-10-01
- 구성요소 등급: `Stable core`; tying은 architecture option
- 예제 ID: `n05_12_embedding_unembedding`
- 코드 원본: `labs/N05/n05_12_embedding_unembedding.py`
- 테스트: `tests/N05/test_n05_12.py`
- 실행 명령: `.venv\Scripts\python.exe -m labs.N05.n05_12_embedding_unembedding`

### 자원 예산

vocabulary 4, sequence length 2, model dimension 3과 parameter 28개를 사용한다. training update는 없다.

### 실제 코드와 실행 결과

<!-- N05_EXAMPLE: n05_12_embedding_unembedding -->

### 검사

테스트는 lookup row, logit shape, probability 합과 embedding gradient row를 확인한다.

## 모델 해석과의 연결

embedding geometry는 입력 table의 vector 관계를 나타낸다. residual stream의 후반 representation과 같은 공간이라고 단정하려면 basis와 transform을 확인해야 한다.

logit lens는 intermediate hidden에 unembedding을 적용한다. 원래 model이 그 지점에서 직접 token을 예측했다는 뜻은 아니며 normalization과 후속 layer를 생략한 diagnostic이다.

## 흔한 오해

### 오해 1. embedding ID가 가까우면 의미도 가깝다

ID는 row index다. vector distance는 embedding row에서 계산한다.

### 오해 2. unembedding은 embedding의 역함수다

unembedding은 hidden을 logit으로 보내는 learned linear map이다. 일반적인 matrix inverse가 아니다.

### 오해 3. shape가 같으면 weight가 공유된다

parameter object를 공유하도록 구현하거나 config로 tying해야 한다.

## 연습문제

### 1. shape

$V=100$, $d=16$, ID batch shape가 `(2,5)`일 때 embedding output shape는?

<details><summary>해설 보기</summary>

`(2,5,16)`이다.

</details>

### 2. parameter 수

embedding과 unembedding을 공유하지 않고 bias가 없으면 parameter 수는?

<details><summary>해설 보기</summary>

$2Vd=3200$개다.

</details>

### 3. logit shape

hidden shape `(2,5,16)`과 $U\in\mathbb R^{100\times16}$에서 logit shape는?

<details><summary>해설 보기</summary>

`(2,5,100)`이다.

</details>

### 4. gradient row

한 batch에 ID 7이 한 번도 없었다. embedding row 7의 직접 lookup gradient는?

<details><summary>해설 보기</summary>

그 batch의 lookup 경로에서는 0이다. tying이나 다른 사용 경로가 있다면 별도 기여가 생길 수 있다.

</details>

### 5. tying

weight tying의 장점 한 가지와 해석상 주의점 한 가지를 적어라.

<details><summary>해설 보기</summary>

parameter 수를 줄인다. 입력 embedding 변화와 output classifier 변화가 같은 parameter에 묶이므로 역할을 분리해 해석하기 어렵다.

</details>

### 6. 주장 비판

intermediate logit lens의 top token이 정답이므로 model이 이미 답을 결정했다는 결론을 평가하라.

<details><summary>해설 보기</summary>

diagnostic projection의 결과다. 후속 layer가 representation과 최종 logit을 바꿀 수 있으므로 결정 완료를 보장하지 않는다.

</details>

## 단원 요약

- embedding은 token ID로 matrix row를 고른다.
- unembedding은 hidden state를 vocabulary logit으로 보낸다.
- weight tying은 두 map의 parameter를 공유하는 선택이다.
- lookup gradient는 사용된 row에 직접 모인다.
- logit lens는 diagnostic이며 원래 forward의 중간 출력과 같지 않다.

## 통과 기준

- embedding과 unembedding shape를 적을 수 있는가?
- 작은 table에서 lookup과 logit을 계산할 수 있는가?
- tying 여부를 config에서 확인할 수 있는가?
- gradient가 모이는 row를 설명할 수 있는가?
- logit lens 주장의 한계를 설명할 수 있는가?

## 다음 단원

- [N05-13 위치정보와 RoPE](N05-13-position-information-rope.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] embedding과 unembedding shape를 검산했다.
- [x] tying과 inverse를 구분했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
- [x] Markdown에 실행 코드를 손으로 복제하지 않았다.
- [x] 코드 원본·테스트 경로·자원 예산·확인일을 기록했다.
- [x] shape·수치·gradient test가 있다.
