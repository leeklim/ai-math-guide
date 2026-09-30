---
id: "A09-GEO-03"
title: "metric과 길이"
part: 4
stage: "A09-GEO"
status: "완료"
prerequisites: ["A09-GEO-02", "M02-03"]
estimated_time: "90~120분"
---

# A09-GEO-03. metric과 길이

## 이 단원이 필요한 이유

coordinate 차이의 Euclidean norm을 representation 거리로 쓰면 좌표 선택을 geometry로 오해할 수 있다. Riemannian metric은 각 tangent space에서 길이와 각도를 정하며, curve length와 geodesic distance의 출발점이 된다.

## 학습 목표

- Riemannian metric의 positive-definite bilinear 조건을 설명할 수 있다.
- 좌표 metric matrix로 tangent norm을 계산할 수 있다.
- curve length가 재매개화에 불변임을 설명할 수 있다.
- metric 선택이 activation 거리 해석을 바꾸는 이유를 말할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-GEO-02 tangent space와 cotangent space](A09-GEO-02-tangent-cotangent.md), [M02-03 내적, 길이와 각도](../../part-1-foundations/M02/M02-03-inner-product-length-angle.md)
- 확인 질문: positive-definite matrix가 만드는 quadratic form은 왜 음수가 되지 않는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $g_p(u,v)$ | `g at p of u comma v` | $p$의 tangent inner product | scalar |
| $G(x)$ | `G of x` | 좌표에서의 metric matrix | $d\times d$ positive definite |
| $\|v\|_{g,p}$ | `the g norm of v at p` | metric tangent norm | nonnegative scalar |
| $L_g(\gamma)$ | `the g length of gamma` | curve의 metric length | nonnegative scalar |

## 핵심 개념

Riemannian metric은 각 $p$에 smooth하게 변하는 inner product $g_p$를 배정한다. 좌표에서

$$
g_p(u,v)=u^\top G(x)v,
\qquad
\|v\|_{g,p}=\sqrt{v^\top G(x)v}.
$$

curve length는

$$
L_g(\gamma)=\int_a^b
\sqrt{\dot\gamma(t)^\top G(\gamma(t))\dot\gamma(t)}\,dt
$$

이다. 속도를 바꾸는 monotone 재매개화는 적분의 시간척도와 속도를 함께 바꿔 길이를 보존한다.

activation space의 Euclidean metric, covariance whitening metric과 decoder-induced metric은 다른 질문을 만든다. metric을 사후에 성능이 좋아 보이는 것으로 고르면 선택 편향이 생긴다.

## 작은 예제

$G=\operatorname{diag}(4,1)$에서 $v=(1,2)$의 squared norm은 $4+4=8$, norm은 $2\sqrt2$이다.

## 흔한 오해

- metric은 두 점의 거리 함수만을 뜻하지 않고 tangent inner product field를 뜻한다.
- coordinate가 nonlinear하다는 말만으로 공간에 intrinsic curvature가 생기지 않는다.

## 연습문제

### 1. norm
$G=\operatorname{diag}(9,1)$, $v=(1,0)$의 metric norm을 구하라.
<details><summary>해설 보기</summary>

$\sqrt9=3$이다.
</details>

### 2. angle
$G=I$이고 $u=(1,0)$, $v=(1,1)$일 때 cosine을 구하라.
<details><summary>해설 보기</summary>

$u^\top v/(\|u\|\|v\|)=1/\sqrt2$이다.
</details>

### 3. position dependence
$G(x)$가 점마다 달라지면 같은 좌표 velocity의 길이가 달라질 수 있는가?
<details><summary>해설 보기</summary>

그렇다. norm은 velocity와 현재 점의 metric matrix에 함께 의존한다.
</details>

### 4. 모델 해석
cosine distance와 whitening distance를 비교할 때 먼저 고정할 것은 무엇인가?
<details><summary>해설 보기</summary>

데이터, centering·normalization, covariance 추정법과 연구 질문에 맞는 metric 선택 규칙이다.
</details>

## 근거와 갱신 경계

metric·curve length 정의는 Riemannian geometry의 표준 정의를 따른다. 이 단원은 distance completeness와 Hopf–Rinow theorem은 다루지 않는다.

## 단원 요약

- metric은 tangent space마다 inner product를 준다.
- curve length는 metric matrix와 velocity로 계산한다.
- 같은 좌표 차이도 metric에 따라 길이가 달라진다.
- activation geometry에서는 metric 선택을 분석 계약에 포함한다.

## 통과 기준

- metric norm과 curve length를 계산할 수 있는가?
- 좌표·metric·distance를 구분할 수 있는가?

## 다음 단원

- [A09-GEO-04 pullback metric과 Jacobian](A09-GEO-04-pullback-metric.md)

## 집필자 점검표

- [x] metric과 좌표 거리를 구분했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
