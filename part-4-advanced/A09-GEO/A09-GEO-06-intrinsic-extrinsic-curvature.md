---
id: "A09-GEO-06"
title: "intrinsic·extrinsic curvature"
part: 4
stage: "A09-GEO"
status: "완료"
prerequisites: ["A09-GEO-05"]
estimated_time: "90~120분"
---

# A09-GEO-06. intrinsic·extrinsic curvature

## 이 단원이 필요한 이유

representation이 고차원 공간에서 굽어 보인다는 관찰은 두 종류의 curvature를 섞기 쉽다. intrinsic curvature는 manifold 내부의 metric만으로 측정하고, extrinsic curvature는 ambient space 안에 어떻게 놓였는지를 측정한다.

## 학습 목표

- intrinsic curvature와 extrinsic curvature를 구분할 수 있다.
- plane과 cylinder의 예로 차이를 설명할 수 있다.
- sectional curvature가 보는 대상을 말할 수 있다.
- embedding의 시각적 굽음을 intrinsic geometry로 단정하지 않을 수 있다.

## 선수지식 확인

- 선수 단원: [A09-GEO-05 geodesic과 connection](A09-GEO-05-geodesic-connection.md)
- 확인 질문: 좌표선이 휘어 보인다는 사실만으로 metric의 curvature를 알 수 있는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $R(X,Y)Z$ | `R of X comma Y applied to Z` | Riemann curvature operator | tangent vector |
| $K(\sigma)$ | `the sectional curvature of sigma` | tangent two-plane $\sigma$의 curvature | scalar |
| $\mathrm{II}(u,v)$ | `the second fundamental form of u comma v` | ambient normal 방향 굽음 | normal vector |
| $K_G$ | `Gaussian curvature` | surface의 intrinsic curvature | scalar |

## 핵심 개념

Riemann curvature는 covariant derivative의 순서가 일반적으로 교환되지 않는 정도를 잰다.

$$
R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z.
$$

sectional curvature는 한 점의 tangent two-plane마다 intrinsic curvature를 준다. 반면 second fundamental form은 ambient derivative의 normal component를 통해 embedding이 바깥 공간에서 얼마나 굽는지를 잰다.

plane과 cylinder의 표면은 국소적으로 길이를 보존하며 펼칠 수 있으므로 둘 다 Gaussian curvature가 0이다. 그러나 cylinder는 3차원 ambient space에서 extrinsically curved이다. sphere는 Gaussian curvature가 양수이므로 plane에 distortion 없이 펼칠 수 없다.

## 작은 예제

종이를 말아 cylinder로 만들 때 종이 위 짧은 선분의 길이와 각도는 바뀌지 않는다. embedding은 굽었지만 intrinsic metric은 평평하게 유지된다.

## 흔한 오해

- 2차원 projection이 휘어 보인다는 사실은 원래 representation manifold의 curvature 추정치가 아니다.
- nonlinear map의 image가 반드시 nonzero intrinsic curvature를 갖는 것은 아니다.

## 연습문제

### 1. cylinder
cylinder의 Gaussian curvature와 extrinsic bending을 각각 설명하라.
<details><summary>해설 보기</summary>

Gaussian curvature는 0이지만 ambient 3차원 공간에서는 normal 방향으로 굽어 있다.
</details>

### 2. sphere
sphere를 plane에 길이 보존으로 펼칠 수 없는 이유를 curvature로 설명하라.
<details><summary>해설 보기</summary>

sphere는 양의 intrinsic Gaussian curvature를 갖고 plane은 0이므로 local isometry로 전체를 펼칠 수 없다.
</details>

### 3. 좌표선
flat plane에 polar coordinate를 쓰면 coordinate line이 휘어진다. intrinsic curvature도 생기는가?
<details><summary>해설 보기</summary>

생기지 않는다. coordinate 표현은 바뀌지만 plane의 intrinsic curvature는 0이다.
</details>

### 4. 모델 해석
PCA plot에서 class trajectory가 굽어 보일 때 curvature 주장에 필요한 추가 검증을 두 가지 쓰라.
<details><summary>해설 보기</summary>

projection distortion을 통제하고, 원래 공간에서 정의한 metric과 neighborhood에 따른 curvature estimator의 안정성을 확인해야 한다.
</details>

## 근거와 갱신 경계

Riemann tensor·sectional curvature·second fundamental form의 구분은 differential geometry의 표준 정의를 따른다. Gauss equation과 curvature tensor의 성분 계산은 범위 밖이다.

## 단원 요약

- intrinsic curvature는 manifold 내부의 metric으로 정한다.
- extrinsic curvature는 ambient embedding에 의존한다.
- cylinder는 intrinsic하게 flat이지만 extrinsically curved이다.
- representation plot의 굽음을 curvature로 바로 해석하면 안 된다.

## 통과 기준

- plane·cylinder·sphere의 curvature 차이를 설명할 수 있는가?
- 시각적 굽음에서 intrinsic 주장으로 넘어갈 때 필요한 검증을 말할 수 있는가?

## 다음 단원

- [A09-GEO-07 activation manifold 분석의 함정](A09-GEO-07-activation-manifold-pitfalls.md)

## 집필자 점검표

- [x] intrinsic·extrinsic curvature를 구분했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
