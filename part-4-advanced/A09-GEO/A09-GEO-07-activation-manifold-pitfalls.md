---
id: "A09-GEO-07"
title: "activation manifold 분석의 함정"
part: 4
stage: "A09-GEO"
status: "완료"
prerequisites: ["A09-GEO-01", "A09-GEO-06", "I06-08"]
estimated_time: "90~120분"
---

# A09-GEO-07. activation manifold 분석의 함정

## 이 단원이 필요한 이유

유한한 activation sample이 낮은 차원 manifold 근처에 있다는 가정은 유용하지만 자동으로 참이 되지 않는다. neighborhood·metric·noise·estimator를 바꾸면 dimension과 curvature 추정치가 크게 달라질 수 있으므로 분석 계약과 null control이 필요하다.

## 학습 목표

- manifold hypothesis와 관측 데이터의 차이를 설명할 수 있다.
- neighborhood scale이 기하 추정에 미치는 영향을 설명할 수 있다.
- projection artifact와 ambient noise를 진단할 수 있다.
- activation geometry 주장에 필요한 control을 설계할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-GEO-01 manifold와 local coordinate](A09-GEO-01-manifold-local-coordinate.md), [A09-GEO-06 intrinsic·extrinsic curvature](A09-GEO-06-intrinsic-extrinsic-curvature.md), [I06-08 CCA, CKA와 RSA](../../part-3-interpretability/I06/I06-08-cca-cka-rsa.md)
- 확인 질문: finite point cloud 자체가 smooth manifold라는 결론을 보장하는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\mathcal{N}_k(x)$ | `the k nearest neighborhood of x` | $x$의 국소 표본 | finite set |
| $\hat d(x)$ | `d hat of x` | 추정한 local dimension | nonnegative scalar |
| $\varepsilon$ | `epsilon` | neighborhood radius 또는 noise scale | positive scalar |
| $P_r$ | `P sub r` | rank-$r$ projection | linear map |

## 핵심 개념

activation sample $x_1,\ldots,x_n\in\mathbb R^D$에서 local PCA를 쓰면 $x$ 주변 covariance의 leading eigenspace를 tangent space의 근사로 삼는다. 그러나 너무 작은 neighborhood는 sample 부족과 noise에 민감하고, 너무 큰 neighborhood는 curvature와 서로 다른 branch를 한 평면에 섞는다.

주요 실패 원인은 다음과 같다.

- prompt distribution이 제한되어 관측하지 못한 방향이 있다.
- token position·layer·normalization을 섞어 서로 다른 population을 합친다.
- ambient noise가 작은 singular value를 부풀린다.
- self-intersection 근처에서 먼 manifold branch가 Euclidean nearest neighbor가 된다.
- PCA·UMAP 같은 projection의 시각적 구조를 원공간 구조로 해석한다.

따라서 scale sweep, bootstrap, shuffled label, matched random subspace, repeated seed와 held-out prompt를 함께 사용한다. estimator가 안정적이라는 결과와 manifold가 실제 계산의 원인이라는 결과는 별개의 주장이다.

## 작은 예제

원 위의 점을 아주 작은 neighborhood로 보면 local PCA dimension은 1에 가깝다. 반원을 한꺼번에 묶으면 두 principal direction이 필요해져 dimension을 2로 과대평가할 수 있다.

## 흔한 오해

- 좋은 2차원 시각화는 low intrinsic dimension의 증거가 아니다.
- local dimension이 작다는 사실은 feature가 disentangled되었다는 뜻이 아니다.

## 연습문제

### 1. scale sweep
$k=5$에서 $\hat d=1$, $k=200$에서 $\hat d=8$이라면 어느 값을 정답으로 택해야 하는가?
<details><summary>해설 보기</summary>

하나를 임의로 택하면 안 된다. sample 안정성과 curvature bias가 균형을 이루는 scale 구간을 사전 기준과 bootstrap으로 평가해야 한다.
</details>

### 2. projection artifact
2차원 UMAP에서 두 cluster가 떨어져 보인다. 원공간 분리를 확인하는 검사는 무엇인가?
<details><summary>해설 보기</summary>

원래 metric에서 held-out classification 또는 within·between distance를 계산하고 random-label·random-projection control과 비교한다.
</details>

### 3. population 혼합
서로 다른 token position을 합치면 local dimension이 커질 수 있는 이유는 무엇인가?
<details><summary>해설 보기</summary>

각 position이 다른 mean이나 tangent direction을 가지면 합친 covariance가 population 간 변화를 새로운 차원으로 센다.
</details>

### 4. 주장 강도
안정적인 local dimension 추정만으로 activation manifold가 모델의 출력을 인과적으로 결정한다고 말할 수 있는가?
<details><summary>해설 보기</summary>

없다. 이는 기술적 구조에 대한 증거이며 인과 주장은 해당 방향을 조작하는 intervention과 적절한 control이 필요하다.
</details>

## 근거와 갱신 경계

이 단원은 local PCA와 neighborhood 기반 point-cloud 분석의 일반적 식별 한계를 정리한다. 특정 manifold-learning 알고리즘의 최신 순위나 기본 hyperparameter는 고정하지 않는다.

## 단원 요약

- finite activation sample은 manifold 자체가 아니다.
- neighborhood scale과 noise가 dimension·curvature 추정을 바꾼다.
- projection의 모양은 원공간 geometry의 직접 증거가 아니다.
- scale sweep·bootstrap·null control·held-out 검증이 필요하다.

## 통과 기준

- activation manifold 분석의 실패 원인을 세 가지 이상 말할 수 있는가?
- 기술적 geometry 주장과 인과 주장을 구분할 수 있는가?

## 다음 단원

- [A09-GEO-08 종합 실습: 국소 표현 기하](A09-GEO-08-capstone-local-geometry.md)

## 집필자 점검표

- [x] activation manifold 분석의 식별 한계를 설명했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
