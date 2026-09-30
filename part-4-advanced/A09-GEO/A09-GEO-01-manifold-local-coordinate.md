---
id: "A09-GEO-01"
title: "manifold와 local coordinate"
part: 4
stage: "A09-GEO"
status: "완료"
prerequisites: ["M01-10", "M02-02", "M03-01"]
estimated_time: "90~120분"
---

# A09-GEO-01. manifold와 local coordinate

## 이 단원이 필요한 이유

고차원 activation이 실제로는 몇 개 자유도 근처에 놓인다는 가설은 manifold 언어로 표현할 수 있다. manifold는 휘어진 그림 자체가 아니라 각 점 주변을 Euclidean coordinate로 기술할 수 있는 공간이다. global embedding dimension과 local intrinsic dimension을 구분해야 한다.

## 학습 목표

- manifold의 local Euclidean 조건을 설명할 수 있다.
- chart와 coordinate map을 구분할 수 있다.
- sphere에 하나의 global chart가 부족한 이유를 설명할 수 있다.
- activation cloud를 manifold라고 부를 때 필요한 가정을 열거할 수 있다.

## 선수지식 확인

- 선수 단원: [M01-10 다변수함수와 편미분](../../part-1-foundations/M01/M01-10-multivariable-partial-derivatives.md), [M02-02 선형결합과 span](../../part-1-foundations/M02/M02-02-linear-combinations-span.md), [M03-01 추상 벡터공간](../../part-1-foundations/M03/M03-01-abstract-vector-spaces.md)
- 확인 질문: $\mathbb R^D$ 안의 부분집합과 $d$차원 좌표공간은 어떻게 다른가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\mathcal M$ | `M calligraphic` | manifold | topological or smooth space |
| $(U,\varphi)$ | `U comma phi` | chart와 coordinate map | $\varphi:U\to\mathbb R^d$ |
| $d$ | `d` | intrinsic dimension | nonnegative integer |
| $D$ | `capital D` | ambient dimension | $D\ge d$ |

## 핵심 개념

$d$차원 smooth manifold는 각 점 $p$ 근처의 열린 영역 $U$가 $\mathbb R^d$의 열린집합과 smooth하게 대응되는 공간이다. $\varphi(p)$는 점 그 자체가 아니라 chart에서의 좌표다. chart가 겹치면 transition map $\psi\circ\varphi^{-1}$가 smooth해야 한다.

원 $S^1\subset\mathbb R^2$은 ambient dimension 2지만 intrinsic dimension 1이다. 각도 하나로 대부분을 표시할 수 있으나 한 점에서 좌표가 끊기므로 여러 chart가 필요하다.

activation 표본 $x_1,\ldots,x_n\in\mathbb R^D$은 유한 point cloud다. 이 표본만으로 smooth manifold의 존재가 증명되지는 않는다. noise scale, sampling density, neighborhood와 dimension estimator를 명시한다.

## 작은 예제

위쪽 반원에서는 $x\in(-1,1)$를 좌표로 써서 $y=\sqrt{1-x^2}$로 점을 복원할 수 있다. 양 끝에서는 derivative가 발산하므로 이 chart는 원 전체를 덮지 못한다.

## 흔한 오해

- 좌표선이 휘었다는 말과 manifold 자체의 intrinsic curvature는 같지 않다.
- PCA가 낮은 rank를 보였다는 사실만으로 nonlinear manifold가 확인된 것은 아니다.

## 연습문제

### 1. 차원
$S^2\subset\mathbb R^3$의 intrinsic·ambient dimension을 적어라.
<details><summary>해설 보기</summary>

intrinsic dimension은 2, ambient dimension은 3이다.
</details>

### 2. 좌표
같은 점이 두 chart에서 다른 숫자로 표현돼도 모순이 아닌 이유는 무엇인가?
<details><summary>해설 보기</summary>

좌표는 chart에 의존하며 transition map이 두 표현을 연결하기 때문이다.
</details>

### 3. 반례
두 직선이 교차한 X 모양이 교차점 근처에서 1차원 manifold가 아닌 이유를 설명하라.
<details><summary>해설 보기</summary>

교차점을 제거하면 네 갈래가 남아 열린 interval의 근방과 위상적으로 같지 않다.
</details>

### 4. 모델 해석
activation manifold 주장을 위해 point cloud 외에 기록할 항목 두 가지를 적어라.
<details><summary>해설 보기</summary>

neighborhood scale과 intrinsic-dimension estimator, sampling dataset·noise model 등을 기록한다.
</details>

## 근거와 갱신 경계

정의와 chart 표준은 John M. Lee의 *Introduction to Smooth Manifolds*의 통상 정의를 따른다. 이 단원은 topological manifold의 분리·가산성 조건을 완전 전개하지 않는다.

## 단원 요약

- manifold는 국소적으로 $\mathbb R^d$ 좌표를 갖는다.
- 좌표는 점이 아니라 chart에 따른 표현이다.
- intrinsic dimension과 ambient dimension은 다르다.
- 유한 activation cloud는 manifold 가설의 관측 표본일 뿐이다.

## 통과 기준

- chart·transition map·두 차원을 구분할 수 있는가?
- manifold가 아닌 교차점 반례를 설명할 수 있는가?

## 다음 단원

- [A09-GEO-02 tangent space와 cotangent space](A09-GEO-02-tangent-cotangent.md)

## 집필자 점검표

- [x] local coordinate와 ambient space를 구분했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
