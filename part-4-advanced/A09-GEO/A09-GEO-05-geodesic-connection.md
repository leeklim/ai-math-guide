---
id: "A09-GEO-05"
title: "geodesic과 connection"
part: 4
stage: "A09-GEO"
status: "완료"
prerequisites: ["A09-GEO-03", "A09-GEO-04"]
estimated_time: "90~120분"
---

# A09-GEO-05. geodesic과 connection

## 이 단원이 필요한 이유

서로 다른 점의 tangent vector는 서로 다른 vector space에 속하므로 그대로 뺄 수 없다. connection은 vector를 manifold를 따라 비교하는 규칙을 주고, geodesic은 그 규칙에서 방향이 스스로 변하지 않는 curve이다.

## 학습 목표

- connection이 필요한 이유를 설명할 수 있다.
- covariant derivative와 parallel transport의 역할을 구분할 수 있다.
- geodesic equation의 항을 읽을 수 있다.
- 좌표의 직선과 geodesic을 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-GEO-03 metric과 길이](A09-GEO-03-metric-length.md), [A09-GEO-04 pullback metric과 Jacobian](A09-GEO-04-pullback-metric.md)
- 확인 질문: 서로 다른 점의 tangent vector가 같은 vector space에 속한다고 가정하면 무엇을 놓치는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\nabla_XY$ | `the covariant derivative of Y along X` | $X$ 방향에서 $Y$의 변화 | vector field |
| $\Gamma^k_{ij}$ | `Gamma k i j` | 좌표 connection coefficient | scalar field |
| $\nabla_{\dot\gamma}\dot\gamma$ | `the covariant acceleration along gamma` | curve의 intrinsic acceleration | tangent vector |
| $\gamma$ | `gamma` | manifold 위의 curve | $[a,b]\to M$ |

## 핵심 개념

connection $\nabla$는 vector field의 방향미분을 tangent vector로 되돌린다. coordinate basis에서는

$$
(\nabla_XY)^k=X^i\partial_iY^k+\Gamma^k_{ij}X^iY^j
$$

로 쓴다. 두 번째 항은 basis 자체가 점에 따라 변하는 효과를 보정한다. Riemannian metric에는 metric과 양립하고 torsion이 없는 Levi–Civita connection이 하나 존재한다.

geodesic은

$$
\nabla_{\dot\gamma}\dot\gamma=0,
\qquad
\ddot\gamma^k+\Gamma^k_{ij}\dot\gamma^i\dot\gamma^j=0
$$

을 만족한다. 국소적으로는 길이를 stationary하게 만드는 curve이며, 충분히 짧은 구간에서는 두 점 사이의 최단 curve가 된다. coordinate chart에서 성분이 휘어 보여도 intrinsic acceleration은 0일 수 있다.

## 작은 예제

Euclidean plane의 Cartesian coordinate에서는 $\Gamma^k_{ij}=0$이므로 geodesic equation은 $\ddot\gamma=0$이다. 해는 일정한 속도의 직선이다. polar coordinate에서는 같은 직선에 nonzero coordinate acceleration이 나타날 수 있다.

## 흔한 오해

- 모든 geodesic이 전역 최단 경로는 아니다.
- Christoffel symbol은 tensor가 아니며 coordinate를 바꾸면 0이 되거나 생길 수 있다.

## 연습문제

### 1. Euclidean geodesic
$\gamma(t)=p+tv$가 Cartesian Euclidean space에서 geodesic인지 확인하라.
<details><summary>해설 보기</summary>

$\ddot\gamma=0$이고 connection coefficient도 0이므로 geodesic equation을 만족한다.
</details>

### 2. 비교 규칙
서로 다른 두 점의 tangent vector를 비교하려면 어떤 추가 구조가 필요한가?
<details><summary>해설 보기</summary>

connection 또는 그것이 정하는 parallel transport 규칙이 필요하다.
</details>

### 3. coordinate effect
polar coordinate에서 직선의 coordinate acceleration이 0이 아닐 수 있는 이유는 무엇인가?
<details><summary>해설 보기</summary>

coordinate basis가 위치에 따라 변하며 Christoffel term이 그 변화를 보정하기 때문이다.
</details>

### 4. 표현 경로
activation interpolation을 geodesic이라고 부르기 전에 확인할 조건을 두 가지 쓰라.
<details><summary>해설 보기</summary>

사용한 manifold와 metric을 명시하고, 그 interpolation이 해당 metric의 geodesic equation이나 길이 최소 조건을 만족하는지 확인해야 한다.
</details>

## 근거와 갱신 경계

connection·parallel transport·geodesic 정의는 Riemannian geometry의 표준 정의를 따른다. geodesic completeness와 exponential map의 전역 성질은 다루지 않는다.

## 단원 요약

- connection은 서로 다른 tangent space의 vector를 비교하게 한다.
- Christoffel term은 coordinate basis의 변화를 보정한다.
- geodesic은 covariant acceleration이 0인 curve이다.
- 좌표 직선과 intrinsic geodesic은 구분해야 한다.

## 통과 기준

- geodesic equation의 두 항을 설명할 수 있는가?
- activation interpolation을 geodesic이라 부르기 위한 조건을 말할 수 있는가?

## 다음 단원

- [A09-GEO-06 intrinsic·extrinsic curvature](A09-GEO-06-intrinsic-extrinsic-curvature.md)

## 집필자 점검표

- [x] connection과 geodesic의 역할을 구분했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
