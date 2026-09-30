---
id: "I06-01"
title: "행동과 표현 질문 설계"
part: 3
stage: "I06"
status: "완료"
prerequisites:
  - "N05-25"
  - "M04-17"
estimated_time: "120~150분"
---

# I06-01. 행동과 표현 질문 설계

## 이 단원이 필요한 이유

모델 해석 실험은 activation을 먼저 모으는 일로 시작하지 않는다. 모델의 어떤 행동을 설명하려는지, 어느 내부량을 관찰할지, 둘을 어떤 비교로 연결할지를 먼저 고정해야 한다. 이 셋이 빠지면 큰 tensor를 모은 뒤 눈에 띄는 패턴에 설명을 붙이게 된다.

이 단원에서는 질문을 **행동 대상, 내부 대상, 비교와 주장**으로 나눈다. 이 설계는 뒤에서 다룰 probe, attribution, intervention과 circuit 분석의 공통 출발점이다.

## 학습 목표

- 행동 질문과 표현 질문을 서로 다른 측정값으로 적을 수 있다.
- claim, estimand와 measurement를 한 줄로 연결할 수 있다.
- model·layer·token·component·조건을 명시해 내부 대상을 고정할 수 있다.
- 관찰 단위와 반복 측정을 구분할 수 있다.
- 관찰, 복원, 사용과 인과 주장의 강도를 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [N05-25 hook과 activation 수집](../../part-2-neural-computation/N05/N05-25-hook-activation-collection.md), [M04-17 실험설계와 재현성](../../part-1-foundations/M04/M04-17-experimental-design-reproducibility.md)
- 확인 질문: 같은 문장의 여러 token activation을 여러 독립 표본으로 세어도 되는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $x_i$ | `input x sub i` | $i$번째 입력 | token sequence |
| $b(x_i)$ | `b of x sub i` | 입력에서 측정한 모델 행동 | scalar 또는 structured output |
| $a_{i,l,t}$ | `the activation for input i at layer l and token t` | 입력·layer·token을 고정한 activation | $\mathbb R^d$ |
| $\Delta_b$ | `delta b` | 두 조건 사이의 행동 차이 | scalar 또는 vector |
| estimand | `estimand` | 질문이 요구하는 이상적인 목표량 | population quantity |
| measurement | `measurement` | 실제 코드가 기록하는 값 | observed quantity |

## 1. 행동 질문과 표현 질문

행동 질문은 모델의 입력과 출력 사이에서 정의한다. 예를 들면 다음과 같다.

- 사실 문장과 반사실 문장에서 정답 token의 logit margin이 얼마나 달라지는가?
- prompt 형식이 바뀌어도 분류 정확도가 유지되는가?
- 특정 단어를 바꿨을 때 다음 token probability가 얼마나 변하는가?

행동값을 $b(x)$라고 쓰면 두 조건 $C_1,C_0$의 평균 차이는 다음처럼 정할 수 있다.

\[
\Delta_b=\mathbb E[b(X)\mid C_1]-\mathbb E[b(X)\mid C_0].
\]

표현 질문은 내부 위치를 포함한다. 같은 입력이라도 layer $l$, token $t$와 component가 달라지면 다른 tensor를 관찰한다. 따라서 `중간 표현을 본다`는 문장은 질문이 아니다. 적어도 다음을 정해야 한다.

1. model과 checkpoint
2. module 또는 component
3. layer index
4. token 위치를 정하는 규칙
5. 입력 조건과 대조 조건
6. activation에서 계산할 통계량

## 2. claim, estimand, measurement

세 항목은 서로 바꿔 쓸 수 없다.

| 구분 | 이 단원의 예 |
|---|---|
| claim | 장소 문맥과 동물 문맥에서 layer 5 MLP update의 분포가 다르다. |
| estimand | 두 입력 모집단에서 선택 activation 평균의 차이 $\mu_{place}-\mu_{animal}$ |
| measurement | 고정한 8개 prompt의 마지막 token에서 얻은 표본평균 차이 |

measurement가 estimand를 잘 근사하려면 입력 표본과 측정 절차가 질문에 맞아야 한다. 여덟 문장만 측정한 결과를 모든 언어·문장 형식·checkpoint에 일반화할 수 없다. 반대로 좁은 파일럿임을 밝히면 작은 실험도 hook 위치와 분석 절차를 검증하는 데 유용하다.

## 3. 분석 단위와 반복 측정

입력 문장 하나에서 12개 layer와 20개 token을 측정했다고 해서 독립 표본이 240개가 되는 것은 아니다. 같은 입력에서 나온 측정값은 공통 원인을 공유한다. 입력이 experimental unit이면 layer와 token은 그 입력 안의 반복 측정이다.

입력별 차이를 먼저 계산하는 paired design도 가능하다. 원문 $x_i$와 최소 수정한 대조문 $x'_i$가 있으면

\[
d_i=b(x_i)-b(x'_i)
\]

를 입력 쌍마다 구한 뒤 $d_i$의 분포를 분석한다. 이 방식은 문장마다 다른 난이도를 일부 상쇄한다.

## 4. 내부 위치를 계산 의미로 적기

module 이름만 적으면 불충분하다. `MLP output`은 residual에 더하기 전 update인지, block output인지에 따라 뜻이 달라진다. Pythia 실험에서 사용하는

```text
gpt_neox.layers.0.mlp.dense_4h_to_h
```

는 첫 block MLP의 down projection output이다. 마지막 token의 이 output은 residual addition 직전 MLP update다. residual stream 전체와 같지 않다.

token도 문자열 위치가 아니라 tokenizer 결과로 정의한다. 이 단원의 smoke test는 prompt를 tokenize한 뒤 attention mask가 가리키는 마지막 실제 token을 선택한다.

## 5. 주장 사다리

모델 해석 결과는 증거 수준에 따라 문장을 달리 쓴다.

1. **관찰**: 두 조건에서 activation 통계가 달랐다.
2. **복원**: activation으로 label을 예측할 수 있었다.
3. **사용**: 해당 정보가 행동 계산에 기능적으로 쓰인다는 증거가 있다.
4. **인과**: 통제된 개입이 행동값을 바꿨다.
5. **일반화**: 다른 입력·seed·checkpoint·model에서도 결과가 유지됐다.

1단계 결과만으로 3단계나 4단계 문장을 쓰면 안 된다. activation 차이는 representation에 정보가 존재할 가능성을 보여주지만, 모델이 그 차이를 출력에 사용한다는 보장은 없다.

## 6. 질문 명세 한 줄 쓰기

실험 전에 다음 문장을 완성한다.

> `[model@revision]`에서 `[입력 모집단과 대조 조건]`을 사용해 `[행동값]`과 `[layer·token·component의 내부량]`을 측정하고, `[분석 단위]` 기준의 `[비교량]`을 추정한다.

예시는 다음과 같다.

> `pythia-160m-deduped@step143000`에서 장소 문장 네 개와 동물 문장 네 개를 사용해 마지막 token 예측과 layer 5 MLP update를 측정하고, 입력 문장 기준의 조건별 평균 차이를 계산한다.

이 문장은 좁지만 실행 가능하다. `모델이 장소 개념을 어떻게 이해하는지 알아본다`는 문장은 대상과 측정값이 없어 그대로 실행할 수 없다.

## 실제 모델 실습

### 70M smoke의 역할

70M 실험은 해석 결론을 내리기 위한 표본이 아니다. tokenizer, 고정 revision, module path, hook 호출, 마지막 token 선택과 manifest 기록이 서로 맞는지 확인하는 계측기 검사다.

<!-- GPU_EXPERIMENT: pythia_70m_smoke -->

실험은 전체 activation을 저장하지 않고 `(1, hidden_size)`의 선택 vector만 남긴다. 통과했다는 사실은 runner가 정상이라는 증거이지, 특정 feature를 발견했다는 증거가 아니다.

## 흔한 오해

### 오해 1. 흥미로운 activation을 찾으면 질문은 나중에 정해도 된다

탐색 분석은 가능하지만, 탐색에서 만든 가설과 확인 실험을 분리해야 한다. 같은 데이터를 보고 가설을 만들고 같은 데이터로 확증하면 선택 편향이 생긴다.

### 오해 2. layer와 token 수가 많으면 표본 수도 자동으로 많아진다

같은 입력에서 나온 반복 측정이다. 독립성 가정과 분석 단위는 데이터 생성 과정을 기준으로 정한다.

### 오해 3. 내부량과 행동값이 상관되면 원인이다

공통 입력 요인 때문에 함께 변할 수 있다. 인과 주장은 대조군과 개입, 대안 설명에 대한 검사가 더 필요하다.

## 연습문제

### 1. 질문 분해

`모델이 부정을 이해하는지 본다`에서 빠진 항목을 세 가지 이상 적어라.

<details><summary>해설 보기</summary>행동값, 입력과 대조 조건, model·revision, 내부 component, layer, token 규칙, 분석 단위와 비교 통계가 빠져 있다. 예를 들어 원문과 부정문에서 정답 token logit margin과 layer 6 마지막 token activation의 쌍별 차이를 측정하도록 좁힐 수 있다.</details>

### 2. estimand와 measurement

모든 영어 장소 문장의 평균 activation 차이가 estimand인데 실제로 4개 문장만 측정했다. 두 값은 같은가?

<details><summary>해설 보기</summary>같지 않다. 전자는 입력 모집단에 대한 목표량이고 후자는 선택한 네 문장에서 얻은 표본 측정값이다. 표본 선택과 불확실성을 밝혀야 한다.</details>

### 3. 분석 단위

문장 10개에서 layer 12개를 측정했다. 문장이 독립 추출 단위라면 독립 표본 수를 120으로 두어도 되는가?

<details><summary>해설 보기</summary>안 된다. layer 측정은 같은 문장 안에서 반복되므로 기본 독립 단위는 10개 문장이다. layer를 포함한 모형을 쓰더라도 문장 내 의존성을 반영해야 한다.</details>

### 4. component 구분

`dense_4h_to_h` output과 block output을 같은 표현이라고 불러도 되는가?

<details><summary>해설 보기</summary>안 된다. 전자는 residual에 더하기 전 MLP update이고 후자는 이전 residual과 여러 update가 반영된 block 출력이다. 계산 위치가 다르다.</details>

### 5. 주장 강도

activation으로 장소·동물 label을 90% 정확도로 복원했다. 허용되는 가장 직접적인 주장은 무엇인가?

<details><summary>해설 보기</summary>해당 표본과 평가 절차에서 label이 activation으로 복원 가능했다는 주장이다. 모델이 그 정보를 행동에 사용한다거나 activation이 원인이라는 주장은 추가 개입 없이는 나오지 않는다.</details>

### 6. smoke test 해석

70M hook 실험이 통과했다. 이것만으로 layer 0 MLP가 사실 지식을 저장한다고 결론낼 수 있는가?

<details><summary>해설 보기</summary>결론낼 수 없다. smoke test는 model load, tokenization, hook 위치와 저장 절차가 작동한다는 계측 검증이다. 지식에 관한 estimand와 대조 실험이 없다.</details>

## 근거와 갱신 경계

Pythia model ID와 checkpoint 체계는 [EleutherAI Pythia 공식 repository](https://github.com/EleutherAI/pythia)와 [Pythia-70M-deduped model card](https://huggingface.co/EleutherAI/pythia-70m-deduped)를 기준으로 2026-10-01에 확인했다. hook의 호출 계약은 [PyTorch `nn.Module` 문서](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html)를 따른다. module path와 library API는 version별 구현 항목이며, 행동·표현·분석 단위의 구분은 특정 library에 의존하지 않는다.

## 단원 요약

- 행동 질문은 출력 측정값, 표현 질문은 model 내부 위치와 통계량을 요구한다.
- claim, estimand와 measurement를 구분해야 표본 결과의 범위를 알 수 있다.
- layer와 token은 같은 입력 안의 반복 측정일 수 있다.
- 관찰, 복원, 사용, 인과와 일반화는 서로 다른 강도의 주장이다.
- smoke test 통과는 계측 절차의 증거이지 해석 결론이 아니다.

## 통과 기준

- 하나의 해석 질문을 행동값과 내부량으로 분해할 수 있는가?
- estimand와 실제 measurement의 차이를 설명할 수 있는가?
- model·layer·token·component와 분석 단위를 명시할 수 있는가?
- 관찰 결과에 맞는 강도의 결론을 쓸 수 있는가?

## 다음 단원

- [I06-02 activation dataset](I06-02-activation-dataset.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] 행동·표현 질문과 claim·estimand·measurement를 연결했다.
- [x] experimental unit과 반복 측정을 구분했다.
- [x] 실제 모델 실험의 module·layer·token을 명시했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
