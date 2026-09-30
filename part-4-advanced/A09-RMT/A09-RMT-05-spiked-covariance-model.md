---
id: "A09-RMT-05"
title: "spiked covariance model"
part: 4
stage: "A09-RMT"
status: "완료"
prerequisites: ["M02-11", "M04-04", "A09-RMT-04"]
estimated_time: "90~120분"
---

# A09-RMT-05. spiked covariance model

## 이 단원이 필요한 이유

low-rank signal이 isotropic noise에 더해져도 sample PCA가 signal direction을 항상 복원하지는 않는다. signal strength와 aspect ratio 사이에 spectral separation threshold가 있다. spiked covariance model은 큰 eigenvalue의 탐지 가능성과 eigenvector 회복을 분리해 보여준다.

## 학습 목표

- rank-one spiked covariance의 population eigenvalue를 계산할 수 있다.
- spectral separation threshold를 aspect ratio와 연결할 수 있다.
- outlier eigenvalue와 eigenvector alignment를 구분할 수 있다.
- activation PCA의 약한 component에 대한 주장 범위를 제한할 수 있다.

## 선수지식 확인

- 선수 단원: [M02-11 고유값과 고유벡터](../../part-1-foundations/M02/M02-11-eigenvalues-eigenvectors.md), [M04-04 기댓값, 분산과 공분산](../../part-1-foundations/M04/M04-04-expectation-variance-covariance.md), [A09-RMT-04 Marchenko–Pastur 법칙의 직관](A09-RMT-04-marchenko-pastur-intuition.md)
- 확인 질문: unit vector $u$에 대해 $uu^\top$는 어느 direction에 eigenvalue 1을 갖는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\Sigma=I+\beta uu^\top$ | `Sigma equals I plus beta u u transpose` | rank-one spiked population covariance | $d\times d$ |
| $\lambda_{\mathrm{pop}}=1+\beta$ | `the population spike equals one plus beta` | signal direction의 population eigenvalue | scalar greater than 1 |
| $\beta>\sqrt\gamma$ | `beta is greater than square root gamma` | unit-noise spectral separation 조건 | asymptotic condition |
| $|\hat u^\top u|^2$ | `the squared alignment between u hat and u` | sample·population direction alignment | number in $[0,1]$ |

## 핵심 개념

unit vector $u$와 signal strength $\beta>0$에 대해

$$
\Sigma=I+\beta uu^\top
$$

를 생각한다. $u$ direction의 population eigenvalue는 $1+\beta$이고 직교 방향의 eigenvalue는 1이다. dimension과 sample이 함께 증가해 $d/n\to\gamma$일 때 unit-noise rank-one model은 $\beta>\sqrt\gamma$에서 sample outlier가 MP bulk와 분리된다.

threshold 위에서 population spike $\ell=1+\beta$에 대응하는 sample outlier 위치는 asymptotic하게

$$
\hat\lambda
\to
\ell\left(1+\frac{\gamma}{\ell-1}\right)
$$

이다. threshold 아래에서는 largest sample eigenvalue가 bulk edge에 붙고 sample eigenvector가 $u$와 유의한 alignment를 유지하지 못한다. finite sample에서는 transition이 날카로운 판정선처럼 보이지 않을 수 있다.

이 model은 low-rank signal 탐지의 기준 사례이다. 실제 activation noise가 anisotropic하거나 여러 spike가 가깝게 있으면 eigenvector 개별 비교보다 signal subspace와 matched null을 분석한다.

## 작은 예제

$\gamma=0.25$이면 threshold는 $\beta>0.5$이다. $\beta=1$이면 $\ell=2$이고 predicted sample outlier는 $2(1+0.25)=2.5$이다. MP upper edge 2.25보다 크다.

## 흔한 오해

- population spike가 1보다 크다는 사실만으로 sample eigenvector가 안정적으로 복원되지는 않는다.
- threshold 위 outlier도 task relevance나 causal use를 자동 보장하지 않는다.

## 연습문제

### 1. population spectrum
$d=5$이고 $\beta=2$이면 $\Sigma=I+2uu^\top$의 eigenvalue를 쓰라.
<details><summary>해설 보기</summary>

$u$ direction에 3 하나, 직교 방향에 1 네 개가 있다.
</details>

### 2. threshold
$\gamma=0.36$일 때 spectral separation을 위한 $\beta$ 조건은 무엇인가?
<details><summary>해설 보기</summary>

$\sqrt{0.36}=0.6$이므로 asymptotic unit-noise model에서 $\beta>0.6$이다.
</details>

### 3. outlier location
$\gamma=0.5$, $\beta=1$이면 predicted sample outlier 위치를 구하라.
<details><summary>해설 보기</summary>

$\ell=2$이므로 $2(1+0.5/1)=3$이다.
</details>

### 4. 모델 해석
PCA 1번 direction이 한 data split에서는 label과 정렬되지만 다른 split에서는 direction이 크게 바뀐다. 어떻게 보고하는가?
<details><summary>해설 보기</summary>

sample eigenvector 안정성이 확인되지 않았으므로 재현 가능한 signal direction이라고 부르지 않는다. subspace overlap, eigenvalue gap과 split별 prediction을 함께 보고한다.
</details>

## 근거와 갱신 경계

threshold와 outlier 식은 unit isotropic noise, rank-one spike와 standard high-dimensional asymptotic를 따른다. finite-size p-value나 general covariance spike는 다루지 않는다.

## 단원 요약

- rank-one spike는 한 population direction의 variance를 높인다.
- sample separation은 signal strength와 aspect ratio의 비에 달려 있다.
- threshold 아래에서는 PCA direction 회복이 실패할 수 있다.
- 실제 representation에서는 individual vector보다 stable subspace가 적절할 수 있다.

## 통과 기준

- population spike와 separation threshold를 계산할 수 있는가?
- eigenvalue outlier와 eigenvector·task relevance를 구분할 수 있는가?

## 다음 단원

- [A09-RMT-06 signal과 noise eigenvalue](A09-RMT-06-signal-noise-eigenvalues.md)

## 집필자 점검표

- [x] spike strength·outlier·eigenvector 회복을 구분했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
