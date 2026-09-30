---
id: "N05-11"
title: "token과 tokenizer"
part: 2
stage: "N05"
status: "완료"
prerequisites:
  - "N05-10"
estimated_time: "120~150분"
---

# N05-11. token과 tokenizer

## 이 단원이 필요한 이유

언어 모델은 문자열을 바로 matrix에 넣지 않는다. tokenizer가 문자열을 token sequence로 나누고 vocabulary의 integer ID로 바꾼다. 같은 문장도 tokenizer가 다르면 sequence length와 token 경계가 달라진다.

이 단원은 고정된 toy vocabulary로 `deep learning math`를 여섯 token으로 바꾼다. 실제 tokenizer의 학습 알고리즘을 재현하는 대신 segmentation, special token, unknown token과 decode의 경계를 분명히 한다.

## 학습 목표

- text, token, token ID와 vocabulary를 구분할 수 있다.
- 고정 규칙으로 문자열을 token sequence로 바꿀 수 있다.
- special token과 unknown token의 역할을 설명할 수 있다.
- token count와 character·word count가 다른 이유를 설명할 수 있다.
- token-level 분석의 결과를 문자열 수준 주장으로 확대하지 않을 수 있다.

## 선수지식 확인

- 선수 단원: [N05-10 autograd, JVP와 VJP](N05-10-autograd-jvp-vjp.md)
- 확인 질문: sequence의 position과 token ID를 구분할 수 있는가?
- 확인 질문: finite set의 원소를 integer index에 대응시킬 수 있는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\mathcal V$ | `script V` | tokenizer vocabulary | finite set |
| $V$ | `V` | vocabulary size | $V=|\mathcal V|$ |
| $t_i$ | `t sub i` | position $i$의 token | $t_i\in\mathcal V$ |
| $a_i$ | `a sub i` | token $t_i$의 integer ID | $\{0,\ldots,V-1\}$ |
| $T$ | `T` | token sequence length | positive integer |
| attention mask | `attention mask` | 실제 token과 padding 위치를 구분하는 indicator | $\{0,1\}^T$ |

## 핵심 개념 1. tokenizer는 문자열과 ID 사이의 규칙이다

encoder를

\[
\operatorname{encode}(s)=(a_1,\ldots,a_T)
\]

로 쓴다. $T$는 문자열 길이와 같지 않다. 자주 쓰는 문자열 조각은 한 token이 되고 낯선 문자열은 여러 token으로 나뉠 수 있다.

decode는 ID를 token 문자열로 바꾼 뒤 tokenizer 규칙에 따라 합친다. normalization과 unknown mapping 때문에 모든 tokenizer에서 완전한 역함수가 보장되는 것은 아니다.

## 핵심 개념 2. special token도 vocabulary 원소다

`<bos>`와 `<eos>`는 sequence 경계를 표시한다. `<unk>`는 vocabulary에 없는 조각을 나타낸다. 모델은 이 token도 다른 token처럼 ID로 받고 embedding row를 조회한다.

padding과 attention mask는 별도 개념이다. padding ID가 존재해도 mask가 어떤 position을 계산에서 제외할지 정한다. decoder-only model은 padding token을 정의하지 않는 경우도 있다.

## 예제. 고정 vocabulary로 encoding

toy vocabulary를 다음처럼 둔다.

| token | ID |
|---|---:|
| `<unk>` | 0 |
| `<bos>` | 1 |
| `<eos>` | 2 |
| `deep` | 3 |
| `learn` | 4 |
| `ing` | 5 |
| `math` | 6 |

`learning`을 `learn`, `ing`으로 나누는 고정 규칙을 적용하면

\[
(\texttt{<bos>},\texttt{deep},\texttt{learn},\texttt{ing},\texttt{math},\texttt{<eos>})
\]

와 ID $(1,3,4,5,6,2)$를 얻는다. attention mask는 여섯 위치 모두 1이다.

## 실행 실습

### 실행 환경과 원본

- 환경: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- 확인일: 2026-10-01
- 구성요소 등급: `Stable core`; toy segmentation은 `Instructional reference`
- 예제 ID: `n05_11_toy_tokenizer`
- 코드 원본: `labs/N05/n05_11_toy_tokenizer.py`
- 테스트: `tests/N05/test_n05_11.py`
- 실행 명령: `.venv\Scripts\python.exe -m labs.N05.n05_11_toy_tokenizer`

### 자원 예산

vocabulary 7개, sequence length 6과 batch 1을 사용한다. model parameter와 training step은 0이다.

### 실제 코드와 실행 결과

<!-- N05_EXAMPLE: n05_11_toy_tokenizer -->

### 검사

테스트는 segmentation, ID, decode와 unknown token을 확인한다. toy 규칙은 BPE나 unigram tokenizer 학습을 흉내 내지 않는다.

## 공개 모델과의 대조

Pythia 공개 tokenizer config는 GPT-NeoX tokenizer를 가리키고 `<|endoftext|>`를 BOS, EOS와 unknown token으로 설정한다. 이 사실은 toy vocabulary의 special token 선택을 정당화하지 않는다. 같은 역할도 model family마다 ID와 문자열이 다르므로 model의 tokenizer artifact를 함께 고정해야 한다.

## 모델 해석과의 연결

token activation을 비교하려면 text span과 token position의 대응을 저장해야 한다. 두 tokenizer에서 position 5는 다른 문자열 조각을 나타낼 수 있다.

한 token의 attribution을 단어 전체의 attribution으로 합칠 때 aggregation rule이 필요하다. subword 수가 다른 표현을 단순 합이나 평균으로 비교하면 estimand가 달라진다.

## 흔한 오해

### 오해 1. token은 단어다

token은 tokenizer vocabulary의 원소다. 한 단어가 여러 token으로 나뉘거나 공백·구두점이 token 일부에 포함될 수 있다.

### 오해 2. token ID의 크기에 의미가 있다

ID는 vocabulary row를 찾는 index다. ID 6이 ID 3보다 의미가 크다는 순서 관계는 없다.

### 오해 3. decode는 항상 원문을 복원한다

normalization, unknown mapping과 special token 처리에 따라 정보가 사라질 수 있다.

## 연습문제

### 1. 길이

예제 문장의 word 수와 special token을 포함한 token 수를 적어라.

<details><summary>해설 보기</summary>

word는 3개이고 token은 6개다. `learning`이 둘로 갈라지고 BOS·EOS가 추가됐다.

</details>

### 2. unknown token

toy tokenizer로 `deep ocean`을 encode하면 token은 무엇인가?

<details><summary>해설 보기</summary>

`<bos>`, `deep`, `<unk>`, `<eos>`다.

</details>

### 3. ID 의미

token ID에 Euclidean distance를 적용해 의미 유사도를 판단해도 되는가?

<details><summary>해설 보기</summary>

안 된다. ID는 범주 index다. 의미 유사도는 embedding이나 다른 representation에서 정의해야 한다.

</details>

### 4. mask

padding 두 위치를 붙여 length 8로 만들면 attention mask의 마지막 두 값은 무엇인가?

<details><summary>해설 보기</summary>

padding을 제외하는 convention에서는 0, 0이다. 앞의 실제 token 위치는 1이다.

</details>

### 5. 재현성

model weight만 공개하고 tokenizer files를 공개하지 않으면 어떤 문제가 생기는가?

<details><summary>해설 보기</summary>

문자열을 같은 ID sequence로 바꾸지 못해 입력과 출력 token의 의미를 재현할 수 없다.

</details>

### 6. 주장 비판

두 prompt가 같은 token 수이므로 같은 언어 구조를 가진다는 결론을 평가하라.

<details><summary>해설 보기</summary>

token 수는 tokenizer segmentation의 결과다. 구문과 의미의 동일성을 보장하지 않는다.

</details>

## 단원 요약

- tokenizer는 text를 vocabulary token과 ID sequence로 바꾼다.
- token 경계는 word나 character 경계와 같지 않다.
- special token과 unknown token도 vocabulary row를 가진다.
- tokenizer artifact는 model 입력 재현에 필요하다.
- token-level 해석에는 text span 대응이 필요하다.

## 통과 기준

- text, token과 ID를 구분할 수 있는가?
- toy example을 encode하고 decode할 수 있는가?
- special token과 mask를 구분할 수 있는가?
- tokenizer가 분석 단위를 바꾸는 이유를 설명할 수 있는가?
- token 수에 근거한 과도한 주장을 비판할 수 있는가?

## 다음 단원

- [N05-12 embedding과 unembedding](N05-12-embedding-unembedding.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] text, token, ID와 position을 구분했다.
- [x] toy tokenizer의 한계를 명시했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
- [x] Markdown에 실행 코드를 손으로 복제하지 않았다.
- [x] 코드 원본·테스트 경로·자원 예산·확인일을 기록했다.
- [x] shape·수치·gradient test가 있다.
