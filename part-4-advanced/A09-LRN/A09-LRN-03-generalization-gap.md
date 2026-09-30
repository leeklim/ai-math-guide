---
id: "A09-LRN-03"
title: "generalization gap"
part: 4
stage: "A09-LRN"
status: "완료"
prerequisites: ["A09-LRN-01", "M04-09"]
estimated_time: "90~120분"
---

# A09-LRN-03. generalization gap

## 이 단원이 필요한 이유

train performance와 unseen performance의 차이는 학습된 predictor의 sample dependence를 드러낸다. generalization gap은 하나의 측정량이며, 작은 gap만으로 낮은 population risk나 distribution shift robustness가 보장되지는 않는다.

## 학습 목표

- expected·observed generalization gap을 구분할 수 있다.
- fixed hypothesis와 data-dependent hypothesis의 차이를 설명할 수 있다.
- validation reuse가 gap 추정을 편향시키는 이유를 설명할 수 있다.
- confidence interval과 paired comparison을 설계할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-LRN-01 hypothesis class와 risk](A09-LRN-01-hypothesis-class-risk.md), [M04-09 신뢰구간](../../part-1-foundations/M04/M04-09-confidence-intervals-bootstrap.md)
- 확인 질문: 학습된 $\hat h$가 training sample의 함수라는 사실은 왜 중요한가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $R(\hat h)-\hat R_n(\hat h)$ | `the generalization gap of h hat` | population minus train risk | scalar |
| $\hat R_{\mathrm{test}}(\hat h)$ | `the test risk of h hat` | held-out risk estimate | scalar |
| $E_S$ | `expectation over samples S` | dataset 반복 expectation | operator |
| $\Delta_i$ | `delta i` | paired loss difference | scalar |

## 핵심 개념

학습 sample $S$에서 얻은 $\hat h_S$의 generalization gap은

$$
R(\hat h_S)-\hat R_S(\hat h_S)
$$

이다. 실제로는 $R$을 모르므로 독립 test sample의 risk로 추정한다. train과 test가 같은 distribution이어도 finite test uncertainty가 있다.

hyperparameter·layer·probe type을 validation 결과로 반복 선택하면 selection process 전체가 learner가 된다. 최종 평가는 선택에 사용하지 않은 test set이 필요하다.

두 probe를 같은 example에서 비교하면 loss difference $\Delta_i$를 paired bootstrap하여 population gap의 차이를 더 정밀하게 추정할 수 있다.

## 작은 예제

train error 0.10, 독립 test error 0.16이면 observed gap은 0.06이다. test set uncertainty를 함께 보고해야 한다.

## 흔한 오해

- train과 test error가 둘 다 높으면 gap이 작아도 좋은 model이 아니다.
- iid gap이 작다는 사실은 다른 domain으로의 generalization을 보장하지 않는다.

## 연습문제

### 1. gap
train loss 0.25, test loss 0.31의 observed gap을 구하라.
<details><summary>해설 보기</summary>

$0.31-0.25=0.06$이다.
</details>

### 2. negative gap
observed gap이 음수가 될 수 있는가?
<details><summary>해설 보기</summary>

가능하다. finite sample variation, regularized training objective 차이, augmentation 등으로 test estimate가 train loss보다 작을 수 있다.
</details>

### 3. validation reuse
100개 layer 중 validation accuracy가 가장 높은 layer를 골랐다면 무엇을 기록해야 하는가?
<details><summary>해설 보기</summary>

layer search 전체를 selection procedure로 기록하고 독립 test set에서 선택된 layer를 한 번 평가해야 한다.
</details>

### 4. shift
held-out prompt template가 train template와 같으면 어떤 일반화만 검사하는가?
<details><summary>해설 보기</summary>

그 template population 안의 iid generalization을 주로 검사하며 새로운 template·domain 일반화는 별도 split이 필요하다.
</details>

## 근거와 갱신 경계

generalization gap과 held-out evaluation은 learning theory와 experimental design의 표준 정의를 따른다. adaptive data analysis의 정량 bound는 다루지 않는다.

## 단원 요약

- gap은 population risk와 train risk의 차이다.
- test risk도 finite sample estimate다.
- model selection을 한 validation set은 최종 test가 아니다.
- iid generalization과 distribution shift를 구분한다.

## 통과 기준

- observed gap과 uncertainty를 계산할 수 있는가?
- selection procedure를 평가 split 설계에 반영할 수 있는가?

## 다음 단원

- [A09-LRN-04 VC dimension](A09-LRN-04-vc-dimension.md)

## 집필자 점검표

- [x] gap·test uncertainty·selection bias를 연결했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
