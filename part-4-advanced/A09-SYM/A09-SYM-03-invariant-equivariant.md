---
id: "A09-SYM-03"
title: "invariant와 equivariant"
part: 4
stage: "A09-SYM"
status: "완료"
prerequisites: ["A09-SYM-01", "M03-04"]
estimated_time: "90~120분"
---

# A09-SYM-03. invariant와 equivariant

## 이 단원이 필요한 이유

입력을 변환했을 때 출력이 그대로여야 하는지, 대응되게 변해야 하는지는 task에 따라 다르다. invariant와 equivariant를 구분하면 data augmentation, architecture constraint와 representation metric의 가정을 정확히 쓸 수 있다.

## 학습 목표

- invariant·equivariant map의 식을 쓸 수 있다.
- input·output action을 명시할 수 있다.
- averaging으로 invariant를 만드는 원리를 설명할 수 있다.
- empirical invariance와 architectural guarantee를 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-SYM-01 group과 action](A09-SYM-01-groups-actions.md), [M03-04 불변량과 equivariance](../../part-1-foundations/M03/M03-04-invariants-equivariance.md)
- 확인 질문: image를 회전할 때 class label과 segmentation mask는 각각 어떻게 변해야 하는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $f(g\cdot x)=f(x)$ | `f of g acting on x equals f of x` | invariance | unchanged output |
| $f(g\cdot x)=\rho(g)f(x)$ | `f of g acting on x equals rho of g acting on f of x` | equivariance | transformed output |
| $\rho(g)$ | `rho of g` | output-space action | linear or nonlinear map |
| $\bar f(x)$ | `f bar of x` | group-averaged function | invariant summary |

## 핵심 개념

invariant map은 input orbit 전체에 같은 값을 주며 quotient 위의 함수로 볼 수 있다. equivariant map은 input 변환을 output 변환으로 옮긴다.

finite group에서

$$
\bar f(x)=\frac1{|G|}\sum_{g\in G}f(g\cdot x)
$$

는 적절한 조건 아래 invariant다. equivariance는 information을 보존한 채 coordinate를 변환하고, 이후 invariant pooling으로 task output을 만들 수 있다.

훈련 데이터에서 작은 변화만 관측됐다는 것은 approximate empirical invariance다. 모든 group element에 대한 architecture-level identity와는 증거 수준이 다르다.

## 작은 예제

coordinate permutation group에서 $f(x)=\sum_i x_i$는 invariant이고 $f(x)=x$는 같은 permutation action에 equivariant다.

## 흔한 오해

- invariance가 항상 좋지는 않다. task-relevant transformation까지 지우면 정보가 손실된다.
- augmentation은 exact equivariance를 보장하지 않는다.

## 연습문제

### 1. invariant
$f(x)=\|x\|_2$가 orthogonal group에 invariant임을 보이라.
<details><summary>해설 보기</summary>

$\|Qx\|_2^2=x^\top Q^\top Qx=\|x\|_2^2$이다.
</details>

### 2. equivariant
$f(x)=Ax$가 permutation $P$에 equivariant이려면 어떤 식을 만족해야 하는가?
<details><summary>해설 보기</summary>

같은 output action을 쓰면 $AP=PA$가 모든 허용 $P$에 대해 성립해야 한다.
</details>

### 3. group average
부호 group에서 $\bar f(x)=[f(x)+f(-x)]/2$가 even function임을 설명하라.
<details><summary>해설 보기</summary>

$\bar f(-x)=[f(-x)+f(x)]/2=\bar f(x)$이다.
</details>

### 4. 모델 평가
test augmentation에서 output 변화가 작으면 exact invariance라 부를 수 있는가?
<details><summary>해설 보기</summary>

아니다. 지정 sample·transformation에 대한 approximate empirical result로 보고하고 architecture proof와 구분한다.
</details>

## 근거와 갱신 경계

invariance·equivariance와 group averaging은 representation theory의 표준 구성이다. Haar integration이 필요한 infinite compact group은 다루지 않는다.

## 단원 요약

- invariant map은 orbit에 같은 값을 준다.
- equivariant map은 input action을 output action으로 옮긴다.
- group averaging은 invariant를 만드는 한 방법이다.
- empirical robustness와 exact symmetry guarantee를 구분한다.

## 통과 기준

- 주어진 map의 invariance·equivariance를 확인할 수 있는가?
- 어떤 정보를 보존하거나 제거하는지 설명할 수 있는가?

## 다음 단원

- [A09-SYM-04 permutation symmetry](A09-SYM-04-permutation-symmetry.md)

## 집필자 점검표

- [x] invariant와 equivariant의 output action을 명시했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
