---
id: "A09-LRN-01"
title: "hypothesis class와 risk"
part: 4
stage: "A09-LRN"
status: "완료"
prerequisites: ["M04-06", "M04-08"]
estimated_time: "90~120분"
---

# A09-LRN-01. hypothesis class와 risk

## 이 단원이 필요한 이유

학습 algorithm은 가능한 predictor 전체가 아니라 정한 hypothesis class 안에서 data에 맞는 함수를 고른다. population risk와 empirical risk를 구분해야 training fit, approximation error와 generalization을 분해할 수 있다.

## 학습 목표

- hypothesis class와 learning algorithm을 구분할 수 있다.
- population·empirical risk를 쓸 수 있다.
- empirical risk minimization의 목적과 한계를 설명할 수 있다.
- loss·data distribution·class가 estimand를 정하는 방식을 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [M04-06 표본과 모집단](../../part-1-foundations/M04/M04-06-samples-populations-sampling-distributions.md), [M04-08 회귀와 분류](../../part-1-foundations/M04/M04-08-regression-classification.md)
- 확인 질문: sample average loss와 새로운 sample에서의 expected loss는 왜 같은 random quantity가 아닌가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\mathcal H$ | `the hypothesis class H` | candidate predictor 집합 | set of functions |
| $R(h)$ | `the risk of h` | population expected loss | scalar |
| $\hat R_n(h)$ | `the empirical risk of h on n samples` | sample average loss | scalar |
| $\hat h$ | `h hat` | data-dependent selected hypothesis | element of $\mathcal H$ |

## 핵심 개념

data $Z=(X,Y)\sim P$와 loss $\ell$에 대해

$$
R(h)=E_P[\ell(h(X),Y)],
\qquad
\hat R_n(h)=\frac1n\sum_{i=1}^n\ell(h(X_i),Y_i).
$$

empirical risk minimization은 $\hat h\in\arg\min_{h\in\mathcal H}\hat R_n(h)$를 고른다. 같은 class라도 optimizer와 regularizer가 다른 inductive bias를 만들 수 있다.

population optimum이 class 밖에 있으면 approximation error가 남는다. class가 너무 풍부하면 training data에 맞춘 선택 때문에 empirical risk가 population risk를 낙관적으로 추정할 수 있다.

## 작은 예제

constant classifier class $\mathcal H=\{h_0,h_1\}$에서 label 10개 중 7개가 1이면 empirical 0–1 risk는 $\hat R(h_1)=0.3$, $\hat R(h_0)=0.7$이다.

## 흔한 오해

- hypothesis class 크기만으로 실제 optimizer가 탐색한 effective class가 정해지는 것은 아니다.
- test set으로 hypothesis를 반복 선택하면 test risk도 낙관적으로 편향된다.

## 연습문제

### 1. empirical risk
loss가 $(0,1,0,1)$이면 empirical risk를 구하라.
<details><summary>해설 보기</summary>

평균은 $2/4=0.5$이다.
</details>

### 2. class
linear probe의 hypothesis class를 $h(x)=w^\top x+b$로 제한하면 무엇이 제한되는가?
<details><summary>해설 보기</summary>

activation에서 label을 복원하는 decision function의 형태가 affine linear map으로 제한된다.
</details>

### 3. approximation
Bayes predictor가 $\mathcal H$에 없으면 empirical data가 무한히 많아져도 무엇이 남을 수 있는가?
<details><summary>해설 보기</summary>

class 안 최선과 Bayes risk 사이의 approximation error가 남을 수 있다.
</details>

### 4. 모델 해석
probe test accuracy를 population claim으로 읽으려면 distribution을 어떻게 명시해야 하는가?
<details><summary>해설 보기</summary>

prompt·label·token·layer sampling을 포함한 target population과 train/test sampling protocol을 명시해야 한다.
</details>

## 근거와 갱신 경계

hypothesis class, risk와 ERM은 statistical learning theory의 표준 정의를 따른다. optimization error의 정밀 분석은 다루지 않는다.

## 단원 요약

- hypothesis class는 가능한 predictor의 집합이다.
- population risk와 empirical risk는 서로 다른 양이다.
- ERM은 sample loss를 최소화하지만 generalization을 자동 보장하지 않는다.
- loss와 target distribution이 학습 주장의 대상을 정한다.

## 통과 기준

- population·empirical risk를 계산할 수 있는가?
- approximation·estimation·optimization 문제를 구분할 수 있는가?

## 다음 단원

- [A09-LRN-02 bias–variance decomposition](A09-LRN-02-bias-variance-decomposition.md)

## 집필자 점검표

- [x] hypothesis class·algorithm·risk를 구분했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
