---
id: "N05-24"
title: "Chain-of-thought의 관찰 지위"
part: 2
stage: "N05"
status: "완료"
prerequisites:
  - "N05-23"
estimated_time: "120~150분"
---

# N05-24. Chain-of-thought의 관찰 지위

## 이 단원이 필요한 이유

model이 생성한 단계별 설명은 직접 관찰할 수 있는 output token sequence다. 읽기 쉽고 때로 문제 해결에 도움이 되지만, 그 문장이 내부 계산을 충실히 보고한다는 결론은 별도의 검증이 필요하다. 해석 연구에서는 `생성됐다`와 `실제 원인이다` 사이의 간격을 유지해야 한다.

## 학습 목표

- generated CoT를 행동 관찰로 분류할 수 있다.
- legibility, correctness와 faithfulness를 구분할 수 있다.
- 같은 output이 내부 표현을 유일하게 정하지 않는 예를 계산할 수 있다.
- CoT intervention과 내부 activation intervention의 질문 차이를 설명할 수 있다.
- CoT 근거로 허용되는 주장과 추가 검증이 필요한 주장을 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [N05-23 decoding과 생성](N05-23-decoding-generation.md)
- 확인 질문: 같은 logits에서도 sampling 결과가 달라질 수 있고, 같은 greedy token에서도 logit margin이 다를 수 있음을 설명할 수 있는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| CoT | `chain of thought` | answer 전에 생성된 단계별 자연어 token sequence | observable output |
| legibility | `legibility` | 사람이 표현된 내용을 읽고 해석할 수 있는 정도 | evaluation property |
| correctness | `correctness` | 중간 명제와 최종 답이 사실·규칙에 맞는 정도 | evaluation property |
| faithfulness | `faithfulness` | 표현된 reasoning이 answer를 만든 model process를 반영하는 정도 | causal claim |
| post-hoc rationale | `post-hoc rationale` | 결론을 만든 뒤 그럴듯하게 구성된 설명 | possible behavior |

## 핵심 개념 1. 무엇을 직접 관찰하는가

prompt $x$가 주어졌을 때 model이 CoT $c$와 answer $a$를 생성했다면 직접 관찰한 것은

\[
(c,a)\sim p_\theta(c,a\mid x)
\]

라는 output behavior다. token, log probability, decoding 조건과 answer accuracy를 기록할 수 있다. 이것만으로 hidden activation, 실제 사용한 feature와 causal path가 자동으로 주어지지는 않는다.

## 핵심 개념 2. 세 평가축

- legibility: 문장이 사람이 이해 가능한가?
- correctness: 적힌 계산과 사실이 맞는가?
- faithfulness: 적힌 이유가 answer를 만든 model process와 연결되는가?

읽기 쉽고 정답인 CoT도 faithfulness가 검증되지 않을 수 있다. 반대로 서툰 표현이 곧 내부 계산과 무관하다는 뜻도 아니다.

## 핵심 개념 3. output의 비식별성

두 표현을 invertible coordinate change $\mathbf h_B=\mathbf h_A\mathbf P$로 연결하고 unembedding을 함께 $\mathbf W_B=\mathbf W_A\mathbf P$로 바꾸면 적절한 직교 $\mathbf P$에 대해

\[
\mathbf h_B\mathbf W_B^\top
=\mathbf h_A\mathbf W_A^\top
\]

를 만들 수 있다. hidden coordinate는 다르지만 logits와 생성 token은 같다. 이 작은 예는 output만으로 내부 좌표 표현을 유일하게 복원할 수 없음을 보여준다. 실제 CoT faithfulness 전체를 이 예 하나로 판정한다는 뜻은 아니다.

## 예제

실습은 두 position의 hidden state에서 두 feature coordinate를 교환하고 unembedding도 같은 방식으로 바꾼다. hidden tensor는 달라지지만 logits는 정확히 같고 greedy token IDs도 `[1, 0]`으로 같다. 관찰된 token sequence가 동일해도 내부 representation 기술은 하나로 결정되지 않는다.

## 실행 실습

### 실행 환경과 원본

- 환경: Python 3.12, PyTorch 2.13.0 CPU, NumPy 2.5.3
- 확인일: 2026-10-01
- 구성요소 등급: 해석상 주의사항
- 예제 ID: `n05_24_cot_observation`
- 코드 원본: `labs/N05/n05_24_cot_observation.py`
- 테스트: `tests/N05/test_n05_24.py`
- 실행 명령: `.venv\Scripts\python.exe -m labs.N05.n05_24_cot_observation`

### 자원 예산

position 2개, hidden dimension 2와 vocabulary 3의 행렬곱만 수행한다. 언어모델 호출은 없다.

### 실제 코드와 실행 결과

<!-- N05_EXAMPLE: n05_24_cot_observation -->

### 검사

테스트는 hidden coordinate가 다른지, logits가 같은지와 greedy output이 같은지를 각각 확인한다.

## faithfulness를 묻는 실험

CoT를 중간에서 자르거나, 일부 단계를 바꾸거나, paraphrase한 뒤 answer distribution이 어떻게 달라지는지 볼 수 있다. prompt에 answer hint를 넣고 model이 실제로 그 hint에 반응했을 때 CoT가 이를 드러내는지도 검사할 수 있다. 이 실험들은 특정 operational definition의 faithfulness를 측정하며 모든 내부 reasoning을 완전히 읽는 것은 아니다.

내부 activation patching이나 circuit intervention은 또 다른 질문을 다룬다. 자연어 CoT token을 바꾸는 intervention과 hidden state를 바꾸는 intervention을 같은 것으로 취급하지 않는다.

## 모델 해석과의 연결

CoT는 black-box behavioral evidence로서 유용하다. 오류 유형, self-correction, prompt sensitivity와 answer dependence를 찾는 출발점이 된다. 그러나 white-box 설명으로 승격하려면 activation, gradient, intervention과 대조군을 연결해야 한다.

faithfulness는 model·task·prompt·decoding에 따라 달라질 수 있다. 한 benchmark 결과를 모든 model과 reasoning trace로 일반화하지 않는다.

## 흔한 오해

### 오해 1. CoT는 내부 activation을 영어로 출력한 것이다

CoT도 autoregressive하게 생성된 token이다. 내부 상태의 직접 dump가 아니다.

### 오해 2. 중간 계산이 맞으면 반드시 faithful하다

correctness는 확인됐지만 그 계산이 answer 생성에 실제로 사용됐는지는 별도 질문이다.

### 오해 3. CoT가 unfaithful할 수 있으므로 아무 정보도 없다

output behavior, 오류 패턴과 intervention 반응을 측정할 수 있다. 증거 수준을 제한해 사용하면 된다.

## 연습문제

### 1. 증거 분류

model이 `2+2=4`라고 생성했다는 사실은 activation 관찰인가 output 관찰인가?

<details><summary>해설 보기</summary>output token의 행동 관찰이다.</details>

### 2. 평가축

문장은 유창하지만 중간 산술이 틀렸다. legibility와 correctness를 각각 평가하라.

<details><summary>해설 보기</summary>읽기 쉬우므로 legibility는 높을 수 있지만 산술이 틀려 correctness는 낮다.</details>

### 3. faithfulness

CoT가 정답이라는 사실만으로 faithfulness가 입증되는가?

<details><summary>해설 보기</summary>아니다. answer를 만든 process와 표현된 이유의 연결을 intervention 등으로 검사해야 한다.</details>

### 4. 비식별성

서로 다른 hidden representation이 같은 logits를 낼 수 있다면 output만으로 hidden coordinate를 유일하게 복원할 수 있는가?

<details><summary>해설 보기</summary>없다. 여러 내부 표현과 parameterization이 같은 observable output을 만들 수 있다.</details>

### 5. intervention 구분

CoT 문장 하나를 지우는 것과 layer 4 residual을 patch하는 것은 같은 조작인가?

<details><summary>해설 보기</summary>아니다. 전자는 이후 입력 token context를 바꾸고 후자는 지정한 내부 activation 경로를 바꾼다.</details>

### 6. 허용 주장

CoT 중간을 잘라도 answer probability가 거의 변하지 않았다. 가장 안전한 결론은?

<details><summary>해설 보기</summary>해당 task·model·truncation 조건에서 뒤 answer가 제거된 CoT suffix에 강하게 의존하지 않았다는 증거다. 전체 CoT나 모든 내부 reasoning이 불필요하다고 일반화할 수 없다.</details>

## 근거와 갱신 경계

CoT faithfulness를 truncation, perturbation과 hint intervention으로 측정하는 문제 설정은 [Measuring Faithfulness in Chain-of-Thought Reasoning](https://arxiv.org/abs/2307.13702)을 따른다. 이후 reasoning model 연구도 보고된 CoT와 내부 process를 동일시할 수 없음을 보여주지만, 수치는 model과 task별 결과이므로 일반 법칙으로 옮기지 않는다.

## 단원 요약

- generated CoT는 직접 관찰 가능한 output token sequence다.
- legibility, correctness와 faithfulness는 다른 평가축이다.
- 같은 output은 내부 representation을 유일하게 정하지 않는다.
- CoT intervention과 activation intervention은 다른 경로를 바꾼다.
- CoT는 행동 증거로 쓰되 내부 인과 설명에는 추가 검증이 필요하다.

## 통과 기준

- CoT의 관찰 지위를 분류할 수 있는가?
- 세 평가축을 사례에 적용할 수 있는가?
- output 비식별성 예를 설명할 수 있는가?
- 두 intervention의 질문을 구분할 수 있는가?
- 증거에 맞는 제한된 주장을 쓸 수 있는가?

## 다음 단원

- [N05-25 hook과 activation 수집](N05-25-hook-activation-collection.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] CoT의 행동 관찰과 내부 설명을 구분했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
- [x] Markdown에 실행 코드를 손으로 복제하지 않았다.
- [x] 코드 원본·테스트 경로·자원 예산·확인일을 기록했다.
- [x] coordinate·logit·output equality test가 있다.

