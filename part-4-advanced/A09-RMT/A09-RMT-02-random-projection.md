---
id: "A09-RMT-02"
title: "random projection"
part: 4
stage: "A09-RMT"
status: "완료"
prerequisites: ["M02-04", "M02-09", "A09-RMT-01"]
estimated_time: "90~120분"
---

# A09-RMT-02. random projection

## 이 단원이 필요한 이유

representation dimension이 커도 finite point set의 pairwise distance를 보존하는 낮은 차원 random embedding을 만들 수 있다. random projection은 시각화나 압축의 대조군이며, learned projection이 얻은 성능을 dimension reduction 자체의 효과와 분리하는 데 쓴다.

## 학습 목표

- Gaussian random projection의 scaling을 쓸 수 있다.
- Johnson–Lindenstrauss 보장의 대상을 설명할 수 있다.
- target dimension이 point 수와 distortion에 의존하는 방식을 설명할 수 있다.
- random projection을 learned projection의 control로 설계할 수 있다.

## 선수지식 확인

- 선수 단원: [M02-04 행렬과 행렬곱](../../part-1-foundations/M02/M02-04-matrices-matrix-multiplication.md), [M02-09 직교기저와 정사영](../../part-1-foundations/M02/M02-09-orthogonal-basis-projection.md), [A09-RMT-01 고차원 공간의 집중현상](A09-RMT-01-high-dimensional-concentration.md)
- 확인 질문: matrix $R\in\mathbb R^{m\times d}$가 $d$-vector에 작용하면 output shape은 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $R\in\mathbb R^{m\times d}$ | `R is an m by d matrix` | random projection matrix | $m\times d$ |
| $z=Rx$ | `z equals R x` | projected representation | $m$-vector |
| $\varepsilon$ | `epsilon` | 허용 relative distance distortion | number in $(0,1)$ |
| $m=O(\varepsilon^{-2}\log n)$ | `m is on the order of epsilon to the minus two log n` | JL target dimension scaling | positive integer order |

## 핵심 개념

$R_{ij}\sim\mathcal N(0,1/m)$로 독립 추출하고 $z=Rx$로 둔다. 고정 vector $v$에 대해 $E\lVert Rv\rVert^2=\lVert v\rVert^2$이다. concentration 때문에 실제 norm도 충분한 $m$에서 원래 norm 근처에 놓인다.

Johnson–Lindenstrauss lemma는 $n$개 point의 finite set에 대해 $m=O(\varepsilon^{-2}\log n)$ 차원으로 보내는 map이 존재하며 모든 pairwise squared distance를 대략

$$
(1-\varepsilon)\lVert x_i-x_j\rVert^2
\le
\lVert Rx_i-Rx_j\rVert^2
\le
(1+\varepsilon)\lVert x_i-x_j\rVert^2
$$

범위에 보존할 수 있다고 말한다. 확률 보장의 정확한 상수는 projection distribution과 failure probability에 따라 달라진다.

random projection은 지정 finite set의 distance 보존을 다룬다. unseen population, label separation이나 nonlinear manifold의 topology를 자동 보장하지 않는다.

## 작은 예제

point 수를 100배 늘려도 필요한 dimension은 $\log n$만큼 증가한다. 반면 허용 distortion을 절반으로 줄이면 $\varepsilon^{-2}$ scaling 때문에 필요한 dimension order가 4배로 커진다.

## 흔한 오해

- random projection과 PCA는 목적이 다르다. PCA는 data variance를 사용하고 random projection은 data-independent matrix를 쓴다.
- 2차원 시각화가 pairwise distance를 잘 보존할 것이라는 보장은 보통 없다.

## 연습문제

### 1. scaling
$R_{ij}$의 variance를 $1/m$로 두는 이유를 한 문장으로 설명하라.
<details><summary>해설 보기</summary>

$m$개 projected coordinate의 expected squared contribution을 합했을 때 원래 squared norm이 유지되도록 scaling한다.
</details>

### 2. distortion
$\varepsilon$을 $0.2$에서 $0.1$로 줄이면 JL dimension order는 몇 배가 되는가?
<details><summary>해설 보기</summary>

$\varepsilon^{-2}$에 비례하므로 4배가 된다.
</details>

### 3. finite set
training activation의 거리가 보존됐다는 결과가 unseen prompt에도 같은 distortion을 보장하는가?
<details><summary>해설 보기</summary>

보장하지 않는다. JL statement의 finite set에 unseen point가 포함되지 않았기 때문이다.
</details>

### 4. 모델 해석
learned 64-dimensional projection의 probe accuracy를 평가할 때 어떤 random control을 두는가?
<details><summary>해설 보기</summary>

같은 input activation과 output dimension에 여러 random projection seed를 적용하고 동일한 probe selection·test protocol을 반복한다.
</details>

## 근거와 갱신 경계

이 단원은 Gaussian random projection과 JL scaling의 역할을 다룬다. sparse transform의 계산 복잡도와 최적 상수는 범위 밖이다.

## 단원 요약

- Gaussian projection은 expected squared norm을 보존하도록 scale한다.
- JL lemma는 finite point set의 pairwise distance를 낮은 차원에서 보존한다.
- 필요한 dimension은 $\log n$과 $\varepsilon^{-2}$에 따라 증가한다.
- random projection은 learned compression의 data-independent control이다.

## 통과 기준

- projection shape과 scaling을 쓸 수 있는가?
- JL 보장이 답하지 않는 population 질문을 구분할 수 있는가?

## 다음 단원

- [A09-RMT-03 표본 공분산의 spectrum](A09-RMT-03-sample-covariance-spectrum.md)

## 집필자 점검표

- [x] JL 보장의 대상·dimension scaling·control 역할을 구분했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
