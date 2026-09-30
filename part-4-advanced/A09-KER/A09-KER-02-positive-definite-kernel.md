---
id: "A09-KER-02"
title: "positive definite kernel"
part: 4
stage: "A09-KER"
status: "완료"
prerequisites: ["M02-03", "M02-12", "A09-KER-01"]
estimated_time: "90~120분"
---

# A09-KER-02. positive definite kernel

## 이 단원이 필요한 이유

kernel method는 sample 쌍의 similarity를 Gram matrix로 모은다. 임의의 similarity function이 inner product처럼 작동하지는 않는다. positive semidefinite 조건을 확인해야 optimization과 함수공간 해석에 필요한 geometry를 얻는다.

## 학습 목표

- kernel function에서 Gram matrix를 만들 수 있다.
- positive semidefinite 조건을 quadratic form으로 검사할 수 있다.
- linear·polynomial·Gaussian kernel의 성질을 비교할 수 있다.
- kernel 값과 causal·semantic similarity를 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [M02-03 내적, 길이와 각도](../../part-1-foundations/M02/M02-03-inner-product-length-angle.md), [M02-12 대칭행렬과 스펙트럼 정리](../../part-1-foundations/M02/M02-12-symmetric-matrices-spectral-theorem.md), [A09-KER-01 함수공간과 operator](A09-KER-01-function-spaces-operators.md)
- 확인 질문: symmetric matrix가 positive semidefinite라는 말은 모든 vector의 quadratic form에 어떤 조건을 거는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $k(x,x')$ | `k of x and x prime` | 두 input 사이의 kernel value | scalar |
| $K_{ij}=k(x_i,x_j)$ | `K sub i j equals k of x i and x j` | sample Gram matrix | $n\times n$ |
| $c^\top Kc$ | `c transpose K c` | Gram matrix의 quadratic form | nonnegative scalar |
| $\lambda_{\min}(K)$ | `the smallest eigenvalue of K` | PSD 진단에 쓰는 최소 고유값 | scalar |

## 핵심 개념

대칭 함수 $k:\mathcal X\times\mathcal X\to\mathbb R$가 positive semidefinite kernel이라는 뜻은 임의의 sample $x_1,\ldots,x_n$과 coefficient $c\in\mathbb R^n$에 대해

$$
\sum_{i=1}^n\sum_{j=1}^n c_i c_j k(x_i,x_j)=c^\top Kc\ge 0
$$

가 성립한다는 것이다. 문헌은 positive definite kernel이라는 이름으로 semidefinite 조건을 포함해 쓰기도 한다. Gram matrix $K$의 모든 eigenvalue가 음수가 아니면 이 finite sample에서 조건을 만족한다.

linear kernel은 $k(x,x')=x^\top x'$이다. polynomial kernel $(x^\top x'+b)^p$와 Gaussian kernel

$$
k(x,x')=\exp\left(-\frac{\lVert x-x'\rVert^2}{2\sigma^2}\right)
$$

도 적절한 parameter에서 PSD kernel이다. kernel은 연구자가 정한 geometry를 반영한다. 큰 값 자체가 인간이 해석하는 semantic equivalence나 모델의 causal dependence를 보장하지 않는다.

## 작은 예제

$x_1=1$, $x_2=2$에 linear kernel을 쓰면

$$
K=\begin{bmatrix}1&2\\2&4\end{bmatrix}.
$$

$K=vv^\top$ with $v=(1,2)^\top$이므로 $c^\top Kc=(v^\top c)^2\ge0$이다.

## 흔한 오해

- kernel function의 kernel은 linear map의 null space와 다른 용어이다.
- finite precision에서 매우 작은 음의 eigenvalue가 나오면 tolerance와 matrix symmetrization을 먼저 확인한다.

## 연습문제

### 1. Gram matrix
$x_1=(1,0)$, $x_2=(1,1)$에 linear kernel을 적용해 $K$를 구하라.
<details><summary>해설 보기</summary>

내적을 계산하면 $K=\begin{bmatrix}1&1\\1&2\end{bmatrix}$이다.
</details>

### 2. PSD
$K=\begin{bmatrix}1&-1\\-1&1\end{bmatrix}$가 PSD인지 eigenvalue로 판단하라.
<details><summary>해설 보기</summary>

eigenvalue는 $0$과 $2$이므로 둘 다 음수가 아니며 PSD이다.
</details>

### 3. symmetry
$k(x,x')\ne k(x',x)$인 함수를 그대로 real inner-product kernel로 쓸 수 있는가?
<details><summary>해설 보기</summary>

real inner product가 대칭이므로 그대로는 쓸 수 없다. 대칭화만으로 PSD가 자동 성립하지도 않는다.
</details>

### 4. 모델 해석
activation kernel 값이 큰 두 prompt를 찾았다. 바로 같은 feature를 사용한다고 결론내릴 수 있는가?
<details><summary>해설 보기</summary>

해당 kernel이 정한 similarity가 크다는 증거이다. feature identity나 causal mechanism에는 추가 alignment와 intervention 검증이 필요하다.
</details>

## 근거와 갱신 경계

이 단원은 real-valued symmetric PSD kernel을 다룬다. conditionally positive definite kernel과 indefinite similarity method는 범위 밖이다.

## 단원 요약

- kernel은 sample 쌍을 scalar로 비교한다.
- PSD 조건은 모든 finite Gram matrix의 quadratic form에 적용된다.
- kernel 선택은 분석 geometry를 정한다.
- 높은 kernel similarity만으로 기능적 동일성을 주장할 수 없다.

## 통과 기준

- kernel에서 Gram matrix를 만들고 PSD를 검사할 수 있는가?
- kernel similarity의 주장 범위를 제한할 수 있는가?

## 다음 단원

- [A09-KER-03 feature map과 kernel trick](A09-KER-03-feature-map-kernel-trick.md)

## 집필자 점검표

- [x] symmetric PSD 조건과 finite Gram matrix를 연결했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
