# 전체 교육과정

## 읽는 방법

- `필수` 단원은 표시된 순서로 학습한다.
- `선택` 단원은 연구 관심에 따라 학습한다.
- 단원 ID는 파일명, 진행표, 문제와 실습에서 공통으로 사용한다.
- 화살표 `A → B`는 A가 B의 직접 선수지식이라는 뜻이다.

## 전체 구조

```text
제1부: 0~4단계 수학 기초
  M00 수식 읽기
   ↓
  M01 변화와 미적분 ─┐
   ↓                 ├→ M03 추상선형대수와 행렬미분
  M02 벡터와 행렬 ───┘                ↓
                           M04 확률·통계·정보이론
                                      ↓
제2부: N05 신경망과 Transformer의 계산
                                      ↓
제3부: I06 표현 해석 → I07 인과·기계론 → I08 학습 동역학
                                      ↓
제4부: A09 선택 심화 모듈
```

## 제1부. 모델 해석을 위한 수학 기초

### 0단계 M00. 수식 읽기

목표는 수식을 계산하기 전에 구조와 역할을 읽는 것이다.

| ID | 단원 | 핵심 결과 |
|---|---|---|
| M00-01 | [수, 변수와 상수](part-1-foundations/M00/M00-01-numbers-variables.md) | 값이 정해진 대상과 변할 수 있는 대상을 구분한다. |
| M00-02 | [식, 등식과 방정식](part-1-foundations/M00/M00-02-expressions-equalities-equations.md) | 표현식과 참·거짓을 주장하는 등식을 구분한다. |
| M00-03 | [함수의 입력과 출력](part-1-foundations/M00/M00-03-functions-input-output.md) | $y=f(x)$를 계산 규칙과 대응으로 읽는다. |
| M00-04 | [좌표와 그래프](part-1-foundations/M00/M00-04-coordinates-graphs.md) | 함수의 입력 변화가 그래프에 어떻게 나타나는지 읽는다. |
| M00-05 | [지수와 로그](part-1-foundations/M00/M00-05-exponents-logarithms.md) | $\exp$, $\log$와 역관계를 이해한다. |
| M00-06 | [인덱스와 합 기호](part-1-foundations/M00/M00-06-indices-summation.md) | $x_i$, $\sum_i x_i$와 평균을 읽는다. |
| M00-07 | [집합, 조건과 논리](part-1-foundations/M00/M00-07-sets-conditions-logic.md) | 원소, 부분집합, 조건, 필요조건과 충분조건을 구분한다. |
| M00-08 | [함수 합성과 역함수](part-1-foundations/M00/M00-08-composition-inverse.md) | $f\circ g$와 계산 순서를 읽는다. |
| M00-09 | [스칼라·벡터·행렬의 shape](part-1-foundations/M00/M00-09-scalars-vectors-matrices-shape.md) | 객체의 종류와 연산 가능 여부를 shape으로 판단한다. |
| M00-10 | [AI 수식 해독 연습](part-1-foundations/M00/M00-10-ai-equation-reading.md) | 손실함수 하나를 기호별로 분해해 읽는다. |

누적 확인식:

\[
\mathcal L(\theta)
=
\frac{1}{N}\sum_{i=1}^{N}
\ell\bigl(f_\theta(x_i),y_i\bigr)
\]

각 기호, 함수 합성, 합과 평균의 역할을 설명하면 통과한다.

### 1단계 M01. 변화와 미적분

| ID | 단원 | 핵심 결과 |
|---|---|---|
| M01-01 | [변화량과 평균변화율](part-1-foundations/M01/M01-01-change-average-rate.md) | $\Delta x$, $\Delta y$와 기울기를 연결한다. |
| M01-02 | [극한의 직관](part-1-foundations/M01/M01-02-limits-intuition.md) | 한 점에 가까워질 때의 함수값을 설명한다. |
| M01-03 | [미분과 순간변화율](part-1-foundations/M01/M01-03-derivative-instantaneous-rate.md) | $f'(x)$와 $\frac{df}{dx}$를 읽고 작은 예제를 계산한다. |
| M01-04 | [도함수와 그래프](part-1-foundations/M01/M01-04-derivative-and-graphs.md) | 증가·감소와 접선의 기울기를 연결한다. |
| M01-05 | [합·곱·몫의 미분](part-1-foundations/M01/M01-05-sum-product-quotient-rules.md) | 기본 미분 규칙을 적용한다. |
| M01-06 | [합성함수와 연쇄법칙](part-1-foundations/M01/M01-06-composition-chain-rule.md) | 안쪽 변화와 바깥쪽 변화를 곱한다. |
| M01-07 | [지수·로그함수의 미분](part-1-foundations/M01/M01-07-exponential-log-derivatives.md) | softmax와 log-likelihood에 필요한 미분을 준비한다. |
| M01-08 | [적분과 누적](part-1-foundations/M01/M01-08-integration-accumulation.md) | 적분을 작은 양의 합으로 해석한다. |
| M01-09 | [미적분의 기본정리](part-1-foundations/M01/M01-09-fundamental-theorem-calculus.md) | 변화율과 누적의 관계를 설명한다. |
| M01-10 | [여러 변수와 편미분](part-1-foundations/M01/M01-10-multivariable-partial-derivatives.md) | 다른 변수를 고정한다는 뜻을 이해한다. |
| M01-11 | [방향미분과 gradient](part-1-foundations/M01/M01-11-directional-derivative-gradient.md) | 방향별 변화율과 gradient를 연결한다. |
| M01-12 | [Taylor 근사](part-1-foundations/M01/M01-12-taylor-approximation.md) | 비선형함수를 한 점 근처에서 근사한다. |
| M01-13 | [수치미분과 오차](part-1-foundations/M01/M01-13-numerical-differentiation-error.md) | 유한차분의 근사 오차와 불안정성을 확인한다. |

누적 과제는 작은 합성함수의 gradient를 직접 계산하고 계산 그래프로 표현하는 것이다.

### 2단계 M02. 벡터와 행렬

| ID | 단원 | 핵심 결과 |
|---|---|---|
| M02-01 | [벡터와 벡터 연산](part-1-foundations/M02/M02-01-vectors-vector-operations.md) | 벡터의 덧셈과 스칼라곱을 기하적으로 이해한다. |
| M02-02 | [선형결합과 span](part-1-foundations/M02/M02-02-linear-combinations-span.md) | 주어진 벡터가 만드는 방향의 집합을 설명한다. |
| M02-03 | [내적, 길이와 각도](part-1-foundations/M02/M02-03-inner-product-length-angle.md) | 유사도, 정사영과 직교를 연결한다. |
| M02-04 | [행렬과 행렬곱](part-1-foundations/M02/M02-04-matrices-matrix-multiplication.md) | 행렬곱을 여러 선형결합으로 계산한다. |
| M02-05 | [행렬을 선형변환으로 보기](part-1-foundations/M02/M02-05-matrix-as-linear-transformation.md) | 회전, 확대, 축소와 투영을 행렬로 이해한다. |
| M02-06 | [연립방정식과 역행렬](part-1-foundations/M02/M02-06-linear-systems-inverse.md) | 해의 존재와 역변환을 연결한다. |
| M02-07 | [선형독립, 기저와 차원](part-1-foundations/M02/M02-07-linear-independence-basis-dimension.md) | 좌표 표현에 필요한 독립 방향을 찾는다. |
| M02-08 | [kernel, image와 rank](part-1-foundations/M02/M02-08-kernel-image-rank.md) | 사라지는 방향과 살아남는 방향을 구분한다. |
| M02-09 | [직교기저와 정사영](part-1-foundations/M02/M02-09-orthogonal-basis-projection.md) | 부분공간에 가장 가까운 표현을 계산한다. |
| M02-10 | [determinant의 최소 이해](part-1-foundations/M02/M02-10-determinant-minimum.md) | 부피 배율과 가역성을 중심으로 이해한다. |
| M02-11 | [고유값과 고유벡터](part-1-foundations/M02/M02-11-eigenvalues-eigenvectors.md) | 방향이 유지되는 축과 증폭률을 설명한다. |
| M02-12 | [대칭행렬과 스펙트럼 정리](part-1-foundations/M02/M02-12-symmetric-matrices-spectral-theorem.md) | 직교 고유기저가 생기는 조건을 이해한다. |
| M02-13 | [특이값분해](part-1-foundations/M02/M02-13-singular-value-decomposition.md) | 입력 방향, 증폭률과 출력 방향으로 행렬을 분해한다. |
| M02-14 | [공분산과 PCA](part-1-foundations/M02/M02-14-covariance-pca.md) | 데이터의 주요 변동 방향을 찾는다. |
| M02-15 | [norm과 condition number](part-1-foundations/M02/M02-15-norm-condition-number.md) | 크기, 민감도와 수치적 안정성을 구분한다. |

누적 과제는 작은 activation 행렬을 SVD로 분해하고 저차원 근사의 의미를 설명하는 것이다.

### 3단계 M03. 추상선형대수와 행렬미분

| ID | 단원 | 핵심 결과 |
|---|---|---|
| M03-01 | [추상 벡터공간](part-1-foundations/M03/M03-01-abstract-vector-spaces.md) | 숫자 배열을 넘어 벡터공간의 공통 구조를 이해한다. |
| M03-02 | [선형사상과 행렬 표현](part-1-foundations/M03/M03-02-linear-maps-matrix-representation.md) | 사상과 특정 기저에서의 행렬을 구분한다. |
| M03-03 | [기저변환과 좌표 의존성](part-1-foundations/M03/M03-03-change-of-basis-coordinate-dependence.md) | 좌표가 달라져도 같은 대상이 무엇인지 구분한다. |
| M03-04 | [불변량과 equivariance 입문](part-1-foundations/M03/M03-04-invariants-equivariance.md) | 변환 아래 유지되는 양과 함께 변하는 양을 구분한다. |
| M03-05 | [부분공간, 직합과 분해](part-1-foundations/M03/M03-05-subspaces-direct-sums-decomposition.md) | 표현공간을 의미 있는 성분으로 나눈다. |
| M03-06 | [동치관계와 몫공간](part-1-foundations/M03/M03-06-equivalence-relations-quotient-spaces.md) | 표현만 다른 대상을 하나의 동치류로 본다. |
| M03-07 | [쌍대공간과 covector](part-1-foundations/M03/M03-07-dual-spaces-covectors.md) | differential과 gradient의 차이를 이해한다. |
| M03-08 | [bilinear form과 quadratic form](part-1-foundations/M03/M03-08-bilinear-quadratic-forms.md) | 내적, attention score와 곡률 표현을 연결한다. |
| M03-09 | [tensor와 multilinear map](part-1-foundations/M03/M03-09-tensors-multilinear-maps.md) | 여러 축과 여러 입력을 갖는 연산을 읽는다. |
| M03-10 | [total derivative와 differential](part-1-foundations/M03/M03-10-total-derivative-differential.md) | 여러 변수의 전체 변화를 선형근사로 나타낸다. |
| M03-11 | [Jacobian](part-1-foundations/M03/M03-11-jacobian.md) | 벡터함수의 국소 선형변환을 계산한다. |
| M03-12 | [Hessian](part-1-foundations/M03/M03-12-hessian.md) | scalar 함수의 국소 곡률을 표현한다. |
| M03-13 | [JVP와 VJP](part-1-foundations/M03/M03-13-jvp-vjp.md) | 큰 Jacobian을 만들지 않고 곱을 계산한다. |
| M03-14 | [자동미분과 역전파](part-1-foundations/M03/M03-14-automatic-differentiation-backpropagation.md) | 계산 그래프에서 연쇄법칙이 구현되는 방식을 이해한다. |
| M03-15 | [재매개화와 모델 대칭성 입문](part-1-foundations/M03/M03-15-reparameterization-model-symmetries.md) | 파라미터가 달라도 같은 함수를 나타낼 수 있음을 이해한다. |

누적 과제는 작은 다층함수의 Jacobian과 역전파를 손계산하고 자동미분 결과와 비교하는 것이다.

### 4단계 M04. 확률·통계·정보이론

| ID | 단원 | 핵심 결과 |
|---|---|---|
| M04-01 | [사건과 확률](part-1-foundations/M04/M04-01-events-probability.md) | 사건의 가능성을 수로 표현한다. |
| M04-02 | [조건부확률과 Bayes 규칙](part-1-foundations/M04/M04-02-conditional-probability-bayes-rule.md) | 새로운 정보가 확률을 바꾸는 방식을 계산한다. |
| M04-03 | [확률변수와 확률분포](part-1-foundations/M04/M04-03-random-variables-distributions.md) | 값과 그 값이 나올 가능성의 규칙을 구분한다. |
| M04-04 | [기댓값, 분산과 공분산](part-1-foundations/M04/M04-04-expectation-variance-covariance.md) | 평균적 행동, 퍼짐과 공동변화를 설명한다. |
| M04-05 | [주요 분포](part-1-foundations/M04/M04-05-common-distributions.md) | Bernoulli, categorical과 Gaussian을 이해한다. |
| M04-06 | [표본, 모집단과 표본분포](part-1-foundations/M04/M04-06-samples-populations-sampling-distributions.md) | 관찰된 데이터와 추론 대상을 구분한다. |
| M04-07 | [추정, 편향과 분산](part-1-foundations/M04/M04-07-estimation-bias-variance.md) | 추정량의 정확성과 안정성을 구분한다. |
| M04-08 | [회귀와 분류](part-1-foundations/M04/M04-08-regression-classification.md) | 예측모형을 통계적 관점에서 이해한다. |
| M04-09 | [신뢰구간과 bootstrap](part-1-foundations/M04/M04-09-confidence-intervals-bootstrap.md) | 추정값의 불확실성을 표현한다. |
| M04-10 | [가설검정과 다중비교](part-1-foundations/M04/M04-10-hypothesis-testing-multiple-comparisons.md) | 우연한 발견과 재현 가능한 효과를 구분한다. |
| M04-11 | [likelihood와 최대우도추정](part-1-foundations/M04/M04-11-likelihood-maximum-likelihood.md) | 모델 파라미터를 데이터에 맞추는 원리를 이해한다. |
| M04-12 | [entropy와 cross entropy](part-1-foundations/M04/M04-12-entropy-cross-entropy.md) | 불확실성과 예측 손실을 연결한다. |
| M04-13 | [KL divergence](part-1-foundations/M04/M04-13-kl-divergence.md) | 두 분포의 방향성 있는 차이를 읽는다. |
| M04-14 | [mutual information](part-1-foundations/M04/M04-14-mutual-information.md) | 한 변수가 다른 변수에 제공하는 정보를 설명한다. |
| M04-15 | [calibration과 scoring rule](part-1-foundations/M04/M04-15-calibration-scoring-rules.md) | 확률 예측의 신뢰성을 평가한다. |
| M04-16 | [상관관계와 인과관계](part-1-foundations/M04/M04-16-correlation-causation.md) | 관찰, 예측과 인과 주장을 구분한다. |
| M04-17 | [실험 설계와 재현성](part-1-foundations/M04/M04-17-experimental-design-reproducibility.md) | 대조군, holdout, seed와 보고 기준을 설계한다. |

누적 과제는 probe 결과를 통계적으로 평가하고 그 결과가 허용하는 주장 범위를 작성하는 것이다.

## 제2부. 5단계 신경망과 Transformer의 실제 계산

### 5단계 N05. 신경망 계산

| ID | 단원 | 핵심 결과 |
|---|---|---|
| N05-01 | tensor와 계산 그래프 | 신경망 계산을 node와 edge로 추적한다. |
| N05-02 | 하나의 neuron | 선형결합, bias와 activation을 계산한다. |
| N05-03 | MLP forward pass | 여러 neuron을 행렬 계산으로 묶는다. |
| N05-04 | activation function | ReLU, sigmoid와 GELU의 비선형성을 비교한다. |
| N05-05 | logits, softmax와 cross entropy | 점수, 확률과 분류 손실을 연결한다. |
| N05-06 | backpropagation | loss의 gradient가 층을 거슬러 전달되는 과정을 계산한다. |
| N05-07 | gradient descent와 mini-batch | 데이터 묶음으로 파라미터를 갱신한다. |
| N05-08 | momentum, Adam과 optimizer state | 업데이트 규칙과 저장 상태를 구분한다. |
| N05-09 | PyTorch tensor와 shape | 코드의 tensor 연산을 수식과 대응시킨다. |
| N05-10 | autograd, JVP와 VJP | 자동미분 결과를 확인한다. |
| N05-11 | token과 tokenizer | 문자열이 token ID로 바뀌는 과정을 이해한다. |
| N05-12 | embedding | 이산 token을 연속 벡터로 바꾼다. |
| N05-13 | 위치정보 | 순서가 표현에 들어가는 방식을 비교한다. |
| N05-14 | query, key와 value | attention의 세 투영을 계산한다. |
| N05-15 | scaled dot-product attention | attention score와 가중합을 계산한다. |
| N05-16 | multi-head attention | 여러 표현 부분공간의 병렬 계산을 추적한다. |
| N05-17 | residual stream | 정보가 층을 가로질러 더해지는 경로를 이해한다. |
| N05-18 | layer normalization | 정규화의 계산과 위치를 추적한다. |
| N05-19 | Transformer의 MLP block | token별 비선형 변환을 계산한다. |
| N05-20 | Transformer block 전체 | attention, residual과 MLP를 하나의 계산으로 연결한다. |
| N05-21 | 언어모델 목적함수 | next-token prediction과 teacher forcing을 이해한다. |
| N05-22 | decoding과 생성 | greedy, sampling과 temperature를 구분한다. |
| N05-23 | Chain-of-thought의 관찰 지위 | 생성된 설명과 내부 계산을 구분한다. |
| N05-24 | hook과 activation 수집 | 원하는 층과 token의 activation을 저장한다. |
| N05-25 | gradient 수집과 개입 준비 | backward hook과 입력 개입을 수행한다. |
| N05-26 | checkpoint와 모델 상태 | 파라미터, buffer와 optimizer state를 구분한다. |
| N05-27 | 종합 실습: 한 token의 경로 | 입력 token부터 logit까지 shape과 계산을 추적한다. |

## 제3부. 6~8단계 모델 해석의 실제

### 6단계 I06. 표현 해석

| ID | 단원 | 핵심 결과 |
|---|---|---|
| I06-01 | 행동과 표현 질문 설계 | 측정할 행동과 내부 대상을 먼저 정의한다. |
| I06-02 | activation dataset | 입력, layer, token과 조건을 통제해 activation을 수집한다. |
| I06-03 | 분포와 기초 통계 | 평균, 분산, 이상치와 조건별 차이를 확인한다. |
| I06-04 | neuron 단위 분석 | 개별 좌표 해석의 장점과 기저 의존성을 구분한다. |
| I06-05 | PCA와 SVD 분석 | 주요 변동 부분공간과 저랭크 근사를 분석한다. |
| I06-06 | linear probe | 선형적으로 복원 가능한 정보를 측정한다. |
| I06-07 | probe control과 selectivity | probe 용량과 우연한 복원을 통제한다. |
| I06-08 | CCA, CKA와 RSA | 서로 다른 표현을 여러 불변성 수준에서 비교한다. |
| I06-09 | feature visualization | feature를 강하게 활성화하는 입력과 조건을 찾는다. |
| I06-10 | superposition | feature와 neuron이 일대일로 대응하지 않는 이유를 이해한다. |
| I06-11 | sparse coding | activation을 희소 feature의 조합으로 근사한다. |
| I06-12 | sparse autoencoder | 학습, reconstruction과 sparsity를 평가한다. |
| I06-13 | feature 안정성과 identifiability | seed와 dictionary가 바뀔 때 feature가 유지되는지 검토한다. |
| I06-14 | 표현 주장 작성 | 존재, 복원, 사용과 인과를 구분해 결론을 쓴다. |
| I06-15 | 종합 실습: 표현 보고서 | 하나의 개념에 대해 수집부터 통계 검증까지 수행한다. |

### 7단계 I07. 귀인, 인과와 기계론

| ID | 단원 | 핵심 결과 |
|---|---|---|
| I07-01 | 민감도와 귀인 | 국소 변화량과 설명을 구분한다. |
| I07-02 | gradient 기반 귀인 | saliency와 gradient×input을 계산한다. |
| I07-03 | integrated gradients와 baseline | 경로와 기준점 선택의 영향을 이해한다. |
| I07-04 | perturbation 기반 귀인 | 입력 일부를 바꾸고 출력 변화를 측정한다. |
| I07-05 | 관찰과 개입 | 상관관계와 내부 node 개입을 구분한다. |
| I07-06 | ablation | neuron, head와 component의 필요성을 시험한다. |
| I07-07 | activation patching | 깨끗한 실행의 activation으로 오염된 실행을 복구한다. |
| I07-08 | causal tracing | layer와 token별 인과 효과를 추적한다. |
| I07-09 | path patching | component 사이의 계산 경로를 제한해 검증한다. |
| I07-10 | residual·logit attribution | residual 성분의 직접적인 logit 기여를 분해한다. |
| I07-11 | circuit을 그래프로 표현하기 | node, edge와 계산 경로를 명시한다. |
| I07-12 | necessity와 sufficiency | 제거와 복원 실험을 함께 설계한다. |
| I07-13 | mediation과 counterfactual | 중간변수의 역할과 대안 실행을 분석한다. |
| I07-14 | off-manifold intervention | 비현실적인 내부 상태가 만드는 혼란을 검토한다. |
| I07-15 | 대조군과 통계 검증 | 무작위 개입, matched control과 반복 실험을 설계한다. |
| I07-16 | CoT faithfulness 평가 | 언어화된 설명을 행동·내부 개입 증거와 대조한다. |
| I07-17 | 종합 실습: 작은 circuit | 행동 정의부터 circuit 검증까지 수행한다. |

### 8단계 I08. 학습 동역학

| ID | 단원 | 핵심 결과 |
|---|---|---|
| I08-01 | checkpoint 연구 설계 | 저장 시점, 지표와 비교 대상을 정의한다. |
| I08-02 | 파라미터 거리와 함수 거리 | 파라미터 차이가 행동 차이와 같지 않음을 이해한다. |
| I08-03 | representation alignment | 회전과 순열을 고려해 checkpoint 표현을 정렬한다. |
| I08-04 | SGD를 동역학으로 보기 | 이산 업데이트와 gradient flow를 연결한다. |
| I08-05 | mini-batch noise와 optimizer state | 확률적 경로 의존성을 분석한다. |
| I08-06 | Hessian spectrum | 학습 지점 주변의 곡률 방향을 근사한다. |
| I08-07 | loss landscape와 mode connectivity | 경로에 따른 loss 변화를 조사한다. |
| I08-08 | influence function | 데이터 하나의 국소적인 학습 영향을 근사한다. |
| I08-09 | feature emergence | feature가 나타나는 시점과 행동 변화를 연결한다. |
| I08-10 | grokking과 phase transition | 급격한 지표 변화의 증거를 신중히 평가한다. |
| I08-11 | seed와 데이터 순서 | 우연성과 재현성을 분리한다. |
| I08-12 | 데이터 귀인 입문 | 학습 예제와 모델 행동의 관계를 조사한다. |
| I08-13 | 종합 실습: feature의 생애 | 여러 checkpoint에서 한 feature의 형성과 사용을 추적한다. |

## 제4부. 9단계 선택 심화

9단계는 순차 교과과정이 아니라 연구 질문별 모듈이다. 제3부에서 생긴 질문에 따라 필요한 모듈을 선택한다.

### A09-GEO. 미분기하학과 표현공간

직접 선수지식: M01, M02, M03

| ID | 단원 |
|---|---|
| A09-GEO-01 | manifold와 local coordinate |
| A09-GEO-02 | tangent space와 cotangent space |
| A09-GEO-03 | metric과 길이 |
| A09-GEO-04 | pullback metric과 Jacobian |
| A09-GEO-05 | geodesic과 connection |
| A09-GEO-06 | intrinsic·extrinsic curvature |
| A09-GEO-07 | activation manifold 분석의 함정 |
| A09-GEO-08 | 종합 실습: 국소 표현 기하 |

### A09-DYN. 동역학계와 확률과정

직접 선수지식: M01, M03, M04, I08

| ID | 단원 |
|---|---|
| A09-DYN-01 | 미분방정식과 흐름 |
| A09-DYN-02 | fixed point와 선형 안정성 |
| A09-DYN-03 | phase portrait와 bifurcation |
| A09-DYN-04 | Markov process |
| A09-DYN-05 | Langevin dynamics |
| A09-DYN-06 | 확률미분방정식 입문 |
| A09-DYN-07 | SGD의 연속시간 근사 |
| A09-DYN-08 | 종합 실습: 학습 궤적 분석 |

### A09-SYM. 군론, 대칭성과 표현 정렬

직접 선수지식: M02, M03, I06, I08

| ID | 단원 |
|---|---|
| A09-SYM-01 | group과 group action |
| A09-SYM-02 | orbit와 stabilizer |
| A09-SYM-03 | invariant와 equivariant |
| A09-SYM-04 | permutation symmetry |
| A09-SYM-05 | scaling·rotation과 gauge freedom |
| A09-SYM-06 | representation theory 입문 |
| A09-SYM-07 | 모델 정렬과 동치류 |
| A09-SYM-08 | 종합 실습: seed 간 표현 정렬 |

### A09-LRN. 통계학습이론

직접 선수지식: M04, N05, I06

| ID | 단원 |
|---|---|
| A09-LRN-01 | hypothesis class와 risk |
| A09-LRN-02 | bias–variance decomposition |
| A09-LRN-03 | generalization gap |
| A09-LRN-04 | VC dimension |
| A09-LRN-05 | Rademacher complexity |
| A09-LRN-06 | PAC learning |
| A09-LRN-07 | probe와 해석의 일반화 |
| A09-LRN-08 | 종합 실습: 복잡도와 일반화 |

### A09-KER. Kernel, 함수공간과 operator

직접 선수지식: M02, M03, M04, N05

| ID | 단원 |
|---|---|
| A09-KER-01 | 함수공간과 operator |
| A09-KER-02 | positive definite kernel |
| A09-KER-03 | feature map과 kernel trick |
| A09-KER-04 | RKHS 입문 |
| A09-KER-05 | spectrum과 compact operator 입문 |
| A09-KER-06 | neural tangent kernel |
| A09-KER-07 | parameter-space와 function-space 비교 |
| A09-KER-08 | 종합 실습: kernel 관점의 학습 |

### A09-RMT. Random matrix와 고차원 통계

직접 선수지식: M02, M04, I06, I08

| ID | 단원 |
|---|---|
| A09-RMT-01 | 고차원 공간의 집중현상 |
| A09-RMT-02 | random projection |
| A09-RMT-03 | 표본 공분산의 spectrum |
| A09-RMT-04 | Marchenko–Pastur 법칙의 직관 |
| A09-RMT-05 | spiked covariance model |
| A09-RMT-06 | signal과 noise eigenvalue |
| A09-RMT-07 | weight·activation·Hessian spectrum |
| A09-RMT-08 | 종합 실습: spectrum의 null model |

### A09-CAU. 고급 인과추론

직접 선수지식: M04, I07

| ID | 단원 |
|---|---|
| A09-CAU-01 | 구조적 인과모형 |
| A09-CAU-02 | do 연산과 intervention |
| A09-CAU-03 | confounding과 identifiability |
| A09-CAU-04 | mediation의 가정 |
| A09-CAU-05 | counterfactual과 potential outcome |
| A09-CAU-06 | causal abstraction |
| A09-CAU-07 | 내부 개입의 외적 타당성 |
| A09-CAU-08 | 종합 실습: circuit 수준 인과 주장 |

### 권장 학습 경로

#### 실험 중심 경로

```text
M00 → M01·M02 → M03·M04 → N05 → I06 → I07
```

#### 학습과정 연구 경로

```text
기본 경로 → I08 → A09-DYN·A09-RMT·A09-SYM
```

#### 표현기하 연구 경로

```text
기본 경로 → I06 → A09-GEO·A09-SYM·A09-RMT
```

#### 이론 연구 경로

```text
기본 경로 → A09-LRN·A09-KER·A09-DYN
```
