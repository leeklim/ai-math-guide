---
id: "I06-15"
title: "종합 실습: 표현 보고서"
part: 3
stage: "I06"
status: "완료"
prerequisites: ["I06-14"]
estimated_time: "180~240분"
---

# I06-15. 종합 실습: 표현 보고서

## 이 단원이 필요한 이유

표현 분석은 activation 수집, 통계, probe와 visualization을 따로 실행하는 것으로 끝나지 않는다. 하나의 질문에 대해 데이터 정의부터 control, 불확실성과 claim boundary까지 연결해야 한다. 이 단원은 I06 전체를 짧은 재현 보고서 형식으로 묶는다.

## 학습 목표

- 행동·표현 질문을 하나의 preregistered 분석 계약으로 작성할 수 있다.
- activation dataset의 provenance와 품질 검사를 보고할 수 있다.
- 기술통계, probe control과 안정성 결과를 한 표로 통합할 수 있다.
- 결과가 허용하는 claim과 허용하지 않는 claim을 명시할 수 있다.
- 코드·manifest·artifact hash로 보고서를 재현할 수 있다.

## 선수지식 확인

- 선수 단원: [I06-14 표현 주장 작성](I06-14-writing-representation-claims.md)
- 확인 질문: probe accuracy가 높아도 보고서의 최대 claim이 `recoverable`에 머물 수 있는 이유는 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| analysis contract | `analysis contract` | 데이터·위치·metric·control·중단 기준의 사전 명세 | protocol |
| primary estimand | `primary estimand` | 보고서가 우선 추정하는 목표량 | population quantity |
| primary metric | `primary metric` | estimand에 대응하는 주 평가값 | scalar 또는 vector |
| sensitivity analysis | `sensitivity analysis` | 합리적 선택을 바꿨을 때 결론이 유지되는지 보는 검사 | analysis set |
| artifact manifest | `artifact manifest` | 입력·코드·model·결과 hash와 자원을 잇는 기록 | JSON document |
| bounded conclusion | `bounded conclusion` | 증거와 검증 범위를 넘지 않게 제한한 결론 | report statement |

## 1. 보고서 질문

예시 질문은 다음과 같다.

> Pythia-160M `step143000`의 layer 5 MLP update 마지막 token에서 장소·동물 prompt 조건을 구분하는 선형 정보가 있는가?

primary estimand는 사전 정의 prompt 모집단에서 held-out linear probe와 matched control의 accuracy 차이다. 파일럿 8개 입력은 full inference용 표본이 아니라 pipeline 검증 자료다. 정식 보고서에는 더 큰 독립 입력과 group split이 필요하다.

$$
\Delta_{\mathrm{sel}}
=
\mathbb{E}[A_{\mathrm{task}}-A_{\mathrm{control}}]
$$

여기서 $A_{\mathrm{task}}$와 $A_{\mathrm{control}}$은 같은 split과 tuning budget에서 얻은 held-out accuracy이다. 표본에서 계산한 차이는 $\Delta_{\mathrm{sel}}$의 estimate이며 estimand 자체와 구분한다.

## 2. 필수 보고서 구조

### A. 데이터와 측정

- input source, 포함·제외와 group ID
- model·tokenizer repository, requested revision과 resolved SHA
- module·layer·token·component
- sample 수, sequence length와 결측·중복
- activation shape·dtype·artifact hash

### B. 분석 계획

- primary estimand와 metric
- train·validation·test split 단위
- probe class, regularization과 tuning budget
- label·input-only control
- seed 수와 uncertainty 방법
- 여러 layer·coordinate를 볼 때 selection 규칙

### C. 결과

- norm·coordinate 분포와 이상치 provenance
- effect size와 confidence interval
- task·control score와 selectivity
- PCA·CKA·RSA 또는 feature stability 중 질문에 필요한 보조 분석
- 사전 기준을 통과하지 못한 항목

### D. 결론

- 지원되는 claim level
- 대안 설명
- 검증한 generalization scope
- 다음에 필요한 개입 실험

## 3. failure gate

다음이면 강한 결론을 쓰지 않고 수집·설계를 고친다.

- hook 호출 수와 입력 행 수가 맞지 않는다.
- split에 같은 원문 group이 겹친다.
- test로 layer·hyperparameter를 골랐다.
- control과 task의 tuning budget이 다르다.
- artifact source hash가 현재 코드와 다르다.
- 결과가 한 seed·소수 이상치에 의존한다.

실패를 다음 분석으로 덮지 않는다.

## 4. CPU 종합 실습

80×8 합성 representation에서 조건별 평균 차이, held-out probe, shuffled-label control, selectivity와 회전 CKA를 한 report object로 만든다.

<!-- I06_EXAMPLE: i06_15_representation_report -->

보고서의 결론은 `이 합성 held-out 표본에서 label이 선형 복원됐다`로 제한된다. 기능적 사용과 인과 개입은 검사하지 않았다.

## 5. Pythia 파일럿 연결

실제 모델 결과는 I06-02의 160M activation dataset과 I06-08의 410M 규모 비교 manifest에 남는다. 보고서에는 수치만 복사하지 않고 다음 provenance를 연결한다.

- 160M resolved SHA `c54a0e0b28cc667b6f278803024438d57f847b5d`
- 410M resolved SHA `c66f7467608ffee8fca0d28cf1f46a7574b53cec`
- 고정 prompt hash와 source hash
- layer 5·11 MLP down projection, 마지막 token
- peak VRAM, 실행시간과 artifact byte

SHA는 현재 파일럿의 식별자이며 `step143000` branch가 영구히 같은 대상을 가리킨다고 가정하지 않는다. local manifest가 실제 재현 기록의 기준이다.

## 6. 보고서 판단표

| 질문 | 통과 기준 | 실패 시 조치 |
|---|---|---|
| 데이터가 질문을 대표하는가? | 사전 정의 모집단·대조와 group split | 표본과 scope 수정 |
| 위치가 정확한가? | module path·shape·hook 횟수 대조 | 수집 중단 후 hook 수정 |
| 효과가 안정적인가? | seed·bootstrap·sensitivity에서 방향 유지 | 불확실성 확대 또는 결론 보류 |
| probe가 정보를 읽는가? | held-out baseline·control보다 개선 | 복원 주장 보류 |
| model이 사용하는가? | 기능 검사나 개입 | I07에서 별도 검증 |

## 흔한 오해

### 오해 1. 분석을 많이 넣을수록 보고서가 강해진다

primary question과 무관한 분석은 선택 기회만 늘릴 수 있다. 핵심 estimand와 보조 분석을 구분한다.

### 오해 2. manifest가 있으면 연구 결론도 재현된다

manifest는 계산 provenance를 돕는다. 다른 sample·seed에서 결론이 유지되는 경험적 재현은 별도다.

### 오해 3. 종합 보고서에서 causal language를 조금 써도 된다

I06의 관찰·복원 결과만으로는 causal claim을 만들지 않는다. I07의 개입 설계가 필요하다.

## 연습문제

### 1. primary estimand

`장소 정보를 본다`를 하나의 primary estimand로 좁혀라.

<details><summary>해설 보기</summary>예를 들어 `사전 정의 장소·동물 prompt 모집단에서 layer 5 마지막 token activation의 held-out linear-probe accuracy와 matched shuffled-label control accuracy의 차이`로 쓸 수 있다.</details>

### 2. provenance

model ID와 `step143000`만 기록했다. 무엇이 더 필요한가?

<details><summary>해설 보기</summary>resolved immutable SHA, tokenizer ID·SHA, source·input hash, module·layer·token, dtype·seed와 환경 version이 필요하다.</details>

### 3. failure gate

hook이 입력당 두 번 호출됐다. report 계산을 계속해야 하는가?

<details><summary>해설 보기</summary>중단한다. module 재사용이나 중복 등록을 확인해 행과 입력 대응을 복구한 뒤 다시 수집한다.</details>

### 4. control

task accuracy 0.88, control 0.85가 나왔다. 결론은 무엇인가?

<details><summary>해설 보기</summary>selectivity가 0.03으로 작아 probe capacity나 identity memorization 대안을 배제하기 어렵다. representation-specific 복원 주장을 보류한다.</details>

### 5. scope

영어 prompt 8개 결과를 한국어 prompt에도 일반화할 수 있는가?

<details><summary>해설 보기</summary>없다. 영어 파일럿으로 범위를 제한하고 한국어 tokenizer·입력에서 별도 반복한다.</details>

### 6. 다음 실험

복원 가능성 뒤 기능적 사용을 확인하려면 어떤 종류의 실험이 필요한가?

<details><summary>해설 보기</summary>probe direction 또는 관련 activation에 대한 통제된 ablation·patching·steering과 행동 metric, random·magnitude-matched control이 필요하다. I07의 범위다.</details>

## 근거와 갱신 경계

보고서 구조는 I06-01~14의 측정·통계·control·stability 규칙을 통합한다. 실제 Pythia 수치는 Git에 넣지 않고 local manifest에서 검증한다. prompt 수가 작은 파일럿은 환경과 분석 경로의 재현 gate이지 모집단 결론이 아니다.

## 단원 요약

- 표현 보고서는 질문, 데이터, 수집, 통계, control과 claim을 한 계약으로 연결한다.
- primary estimand와 보조 분석을 구분한다.
- provenance·hash는 계산 재현을, seed·dataset 반복은 결론 안정성을 검사한다.
- I06 결과는 관찰과 복원 주장까지이며 기능·인과는 별도 실험이다.

## 통과 기준

- 하나의 representation question을 완전한 analysis contract로 쓸 수 있는가?
- 데이터·hook·probe·control·stability gate를 확인할 수 있는가?
- 지원되는 claim과 다음 개입 실험을 구분할 수 있는가?

## 다음 단계

- I07-01 gradient 기반 귀인

## 집필자 점검표

- [x] 데이터 정의부터 주장 범위까지 한 보고서로 연결했다.
- [x] 160M을 주력으로 사용하고 410M을 규모 비교에만 사용했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
