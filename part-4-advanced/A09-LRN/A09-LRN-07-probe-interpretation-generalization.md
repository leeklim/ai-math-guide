---
id: "A09-LRN-07"
title: "probe와 해석의 일반화"
part: 4
stage: "A09-LRN"
status: "완료"
prerequisites: ["A09-LRN-03", "A09-LRN-05", "I06-06", "I06-07"]
estimated_time: "90~120분"
---

# A09-LRN-07. probe와 해석의 일반화

## 이 단원이 필요한 이유

probe가 held-out row에서 잘 작동해도 새로운 prompt template, concept paraphrase, model seed와 layer에서 일반화된다는 뜻은 아니다. 해석 연구에는 여러 population 축과 selection procedure가 있으므로 split을 claim 단위에 맞춰 설계해야 한다.

## 학습 목표

- probe의 experimental unit과 hypothesis class를 명시할 수 있다.
- row·prompt·template·concept·model split을 구분할 수 있다.
- nested selection과 control task를 설계할 수 있다.
- 복원 가능성과 모델의 기능적 사용을 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-LRN-03 generalization gap](A09-LRN-03-generalization-gap.md), [A09-LRN-05 Rademacher complexity](A09-LRN-05-rademacher-complexity.md), [I06-06 linear probe](../../part-3-interpretability/I06/I06-06-linear-probe.md), [I06-07 probe control](../../part-3-interpretability/I06/I06-07-probe-controls-selectivity.md)
- 확인 질문: 같은 prompt의 여러 token row를 train과 test에 나누면 어떤 leakage가 생기는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $D_{\mathrm{train}},D_{\mathrm{test}}$ | `D train and D test` | 독립 평가 split | datasets |
| $\mathcal H_{\mathrm{probe}}$ | `the probe hypothesis class` | probe predictor family | function class |
| $s$ | `s` | model seed 또는 split seed | index |
| $\Delta_{\mathrm{sel}}$ | `selection optimism delta` | selection으로 생긴 낙관 편향 | scalar |

## 핵심 개념

probe claim을 다음 축으로 분해한다.

- row generalization: 같은 prompt population의 unseen activation row
- prompt generalization: unseen prompt
- template·concept generalization: lexical cue를 넘은 구조
- model generalization: unseen training seed·architecture

layer, regularization, feature preprocessing과 probe class를 validation으로 고른 뒤 독립 test를 사용한다. prompt가 experimental unit이면 confidence interval과 permutation도 prompt 단위로 수행한다.

probe는 information이 predictor class에서 recoverable함을 보인다. model이 그 information을 실제 output 계산에 사용하는지는 ablation·patching·readout alignment 같은 별도 intervention이 필요하다.

## 작은 예제

문장마다 20 token이 있어도 문장 100개라면 prompt-level generalization의 독립 unit은 2,000개가 아니라 100개에 가깝다.

## 흔한 오해

- test accuracy가 높아도 label leakage나 template cue를 이용했을 수 있다.
- nonlinear probe 성능 향상은 activation에 단순하고 사용 가능한 feature가 있다는 뜻이 아니다.

## 연습문제

### 1. split
paraphrase 일반화를 보려면 어떤 split이 필요한가?
<details><summary>해설 보기</summary>

동일 의미의 표현 변형을 train과 test에 분리하고 lexical overlap control을 둔 template·paraphrase split이 필요하다.
</details>

### 2. nested selection
layer와 regularization을 고른 validation set을 최종 성능 보고에 다시 쓰면 어떤 문제가 생기는가?
<details><summary>해설 보기</summary>

selection noise에 맞춘 낙관 편향이 포함된다. 독립 test set이나 nested resampling이 필요하다.
</details>

### 3. complexity
MLP probe가 linear probe보다 좋을 때 무엇을 함께 보고해야 하는가?
<details><summary>해설 보기</summary>

capacity·regularization·sample size·random-label control과 held-out gap을 함께 보고해 memorization과 nonlinear recoverability를 구분한다.
</details>

### 4. 사용 증거
probe가 복원한 direction을 모델이 사용한다는 주장을 강화하는 실험은 무엇인가?
<details><summary>해설 보기</summary>

해당 direction을 selective ablation·patching하고 matched-norm control과 함께 output effect를 측정한다.
</details>

## 근거와 갱신 경계

이 단원은 learning-theory split과 probe control을 모델 해석 주장에 적용한다. 특정 probe architecture의 우열은 고정하지 않는다.

## 단원 요약

- generalization claim마다 독립 unit과 split 축이 다르다.
- selection은 validation에서, 최종 평가는 독립 test에서 한다.
- probe capacity와 random-label control을 함께 본다.
- recoverability와 functional use는 다른 증거다.

## 통과 기준

- probe claim에 맞는 split과 unit을 선택할 수 있는가?
- 복원·일반화·사용 주장을 구분할 수 있는가?

## 다음 단원

- [A09-LRN-08 종합 실습: 복잡도와 일반화](A09-LRN-08-capstone-complexity-generalization.md)

## 집필자 점검표

- [x] probe의 여러 일반화 축과 인과 한계를 밝혔다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
