---
id: "A09-RMT-01"
title: "고차원 공간의 집중현상"
part: 4
stage: "A09-RMT"
status: "완료"
prerequisites: ["M02-03", "M04-04", "M04-05"]
estimated_time: "90~120분"
---

# A09-RMT-01. 고차원 공간의 집중현상

## 이 단원이 필요한 이유

고차원 random vector의 좌표는 흔들려도 norm과 pairwise inner product 같은 집계량은 좁은 범위에 모일 수 있다. activation의 cosine similarity나 random baseline을 해석하려면 차원이 커질 때 무엇이 집중되는지 먼저 확인해야 한다.

## 학습 목표

- isotropic Gaussian vector의 squared norm 평균과 분산을 계산할 수 있다.
- 독립 random direction의 inner product scale을 설명할 수 있다.
- concentration과 low-dimensional clustering을 구분할 수 있다.
- activation geometry에 dimension-matched null model을 설정할 수 있다.

## 선수지식 확인

- 선수 단원: [M02-03 내적, 길이와 각도](../../part-1-foundations/M02/M02-03-inner-product-length-angle.md), [M04-04 기댓값, 분산과 공분산](../../part-1-foundations/M04/M04-04-expectation-variance-covariance.md), [M04-05 주요 분포](../../part-1-foundations/M04/M04-05-common-distributions.md)
- 확인 질문: 독립 random variable의 합에서 variance는 어떤 조건 아래 더해지는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $x\sim\mathcal N(0,I_d/d)$ | `x is Gaussian with mean zero and covariance I d over d` | expected squared norm이 1인 isotropic vector | $d$-vector |
| $\lVert x\rVert_2^2$ | `the squared Euclidean norm of x` | coordinate 제곱의 합 | nonnegative scalar |
| $x^\top y$ | `x transpose y` | 두 vector의 inner product | scalar |
| $d$ | `the ambient dimension d` | vector가 놓인 ambient dimension | positive integer |

## 핵심 개념

$x_i\overset{\mathrm{iid}}\sim\mathcal N(0,1/d)$이면

$$
\lVert x\rVert_2^2=\sum_{i=1}^d x_i^2,
\qquad
E\lVert x\rVert_2^2=1,
\qquad
\operatorname{Var}(\lVert x\rVert_2^2)=\frac{2}{d}.
$$

dimension이 커질수록 squared norm의 standard deviation $\sqrt{2/d}$가 줄어든다. 독립인 $x,y\sim\mathcal N(0,I_d/d)$에 대해서도 $E[x^\top y]=0$이고 $\operatorname{Var}(x^\top y)=1/d$이다. random vector는 norm 1 근처에 모이고 서로 거의 orthogonal해진다.

concentration은 모든 dataset이 sphere에 균일하게 놓인다는 뜻이 아니다. anisotropy, dependence와 low-dimensional signal이 있으면 norm과 angle distribution이 달라진다. 관찰값을 해석할 때 dimension, marginal variance와 sample dependence를 맞춘 null distribution과 비교해야 한다.

## 작은 예제

$d=200$이면 squared norm의 standard deviation은 $\sqrt{2/200}=0.1$이다. 같은 scaling에서 독립 inner product의 standard deviation은 $1/\sqrt{200}\approx0.071$이다.

## 흔한 오해

- distance가 집중된다는 사실이 모든 point가 같은 의미를 가진다는 뜻은 아니다.
- 높은 dimension만으로 empirical sample이 population concentration regime에 들어가지는 않는다. sample dependence와 tail behavior를 확인해야 한다.

## 연습문제

### 1. norm variance
$d=50$일 때 $\lVert x\rVert^2$의 variance를 구하라.
<details><summary>해설 보기</summary>

$2/d=2/50=0.04$이다.
</details>

### 2. inner product scale
$d$가 100에서 400으로 늘면 독립 inner product의 standard deviation은 몇 배가 되는가?
<details><summary>해설 보기</summary>

$1/\sqrt d$ scaling이므로 $1/2$배가 된다.
</details>

### 3. anisotropy
한 coordinate의 variance가 다른 coordinate보다 100배 크면 isotropic null의 angle 예측을 그대로 써도 되는가?
<details><summary>해설 보기</summary>

쓸 수 없다. covariance anisotropy가 특정 방향을 지배하므로 covariance를 맞춘 null이나 whitening 뒤 비교가 필요하다.
</details>

### 4. 모델 해석
layer width가 다른 두 activation의 raw cosine histogram을 비교할 때 어떤 null을 함께 보고해야 하는가?
<details><summary>해설 보기</summary>

각 layer의 dimension, norm 또는 covariance와 sampling unit을 맞춘 random-vector cosine distribution을 함께 보고한다.
</details>

## 근거와 갱신 경계

계산은 iid Gaussian 예제에 한정한다. sub-Gaussian concentration inequality의 상수와 heavy-tailed 분포의 별도 이론은 다루지 않는다.

## 단원 요약

- isotropic Gaussian squared norm의 variance는 $2/d$이다.
- 독립 inner product의 scale은 $1/\sqrt d$이다.
- concentration은 random baseline이지 semantic structure의 부재를 뜻하지 않는다.
- null model은 dimension과 covariance 조건을 맞춰야 한다.

## 통과 기준

- norm과 inner product의 concentration scale을 계산할 수 있는가?
- observed geometry와 dimension effect를 분리하는 null을 제안할 수 있는가?

## 다음 단원

- [A09-RMT-02 random projection](A09-RMT-02-random-projection.md)

## 집필자 점검표

- [x] norm·inner product concentration과 null model을 연결했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
