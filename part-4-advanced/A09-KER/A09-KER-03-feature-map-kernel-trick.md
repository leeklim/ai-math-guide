---
id: "A09-KER-03"
title: "feature map과 kernel trick"
part: 4
stage: "A09-KER"
status: "완료"
prerequisites: ["M02-02", "M02-03", "A09-KER-02"]
estimated_time: "90~120분"
---

# A09-KER-03. feature map과 kernel trick

## 이 단원이 필요한 이유

positive semidefinite kernel은 어떤 feature space의 inner product로 표현할 수 있다. algorithm이 feature coordinate를 직접 만들지 않고 kernel value만 사용하면 높은 차원이나 infinite-dimensional space에서도 계산할 수 있다. 이 계산 절약이 kernel trick이다.

## 학습 목표

- explicit feature map에서 대응 kernel을 계산할 수 있다.
- Gram matrix만으로 inner product 계산을 바꾸는 과정을 설명할 수 있다.
- 같은 kernel을 만드는 feature map의 비유일성을 설명할 수 있다.
- kernel similarity 분석의 계산 단위와 대조군을 정할 수 있다.

## 선수지식 확인

- 선수 단원: [M02-02 선형결합과 span](../../part-1-foundations/M02/M02-02-linear-combinations-span.md), [M02-03 내적, 길이와 각도](../../part-1-foundations/M02/M02-03-inner-product-length-angle.md), [A09-KER-02 positive definite kernel](A09-KER-02-positive-definite-kernel.md)
- 확인 질문: feature vector 두 개의 모든 coordinate를 몰라도 inner product만 계산할 수 있다면 어떤 algorithm을 그대로 실행할 수 있는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\phi:\mathcal X\to\mathcal H$ | `phi maps X to H` | input을 feature space로 보내는 map | function |
| $k(x,x')=\langle\phi(x),\phi(x')\rangle_{\mathcal H}$ | `k of x and x prime equals the inner product of phi of x and phi of x prime in H` | feature inner product로 표현한 kernel | scalar |
| $\Phi$ | `capital phi` | sample feature matrix | $n\times d_\phi$ |
| $K=\Phi\Phi^\top$ | `K equals Phi Phi transpose` | feature Gram matrix | $n\times n$ |

## 핵심 개념

feature map $\phi$가 있으면

$$
k(x,x')=\langle\phi(x),\phi(x')\rangle_{\mathcal H}
$$

로 kernel을 만든다. sample feature를 row로 쌓은 $\Phi$에 대해 $K=\Phi\Phi^\top$이다. inner product와 sample 사이 linear combination만 사용하는 algorithm은 $\Phi$를 만들지 않고 $K$로 계산할 수 있다.

예를 들어 scalar input에 $k(x,z)=(1+xz)^2$를 쓰면

$$
\phi(x)=(1,\sqrt2x,x^2)
$$

를 택할 수 있다. 실제로 $\phi(x)^\top\phi(z)=1+2xz+x^2z^2$이다. orthogonal transformation $Q$를 적용한 $Q\phi(x)$도 같은 inner product를 만들므로 feature coordinate는 유일하지 않다.

kernel trick은 계산 표현을 바꾼다. sample 수 $n$에 비례하는 $n\times n$ Gram matrix를 저장하므로 $n$이 큰 상황에서는 계산량이 병목이 될 수 있다.

## 작은 예제

$x=1$, $z=2$이면 polynomial kernel 값은 $(1+2)^2=9$이다. explicit feature로 계산해도 $(1,\sqrt2,1)\cdot(1,2\sqrt2,4)=1+4+4=9$이다.

## 흔한 오해

- kernel trick이 모든 계산을 싸게 만드는 것은 아니다. feature dimension 대신 sample 수가 비용을 지배할 수 있다.
- kernel이 같은 두 feature map에서 coordinate별 의미까지 같지는 않다.

## 연습문제

### 1. feature map
$\phi(x)=(x,x^2)$일 때 대응 kernel을 쓰라.
<details><summary>해설 보기</summary>

$k(x,z)=xz+x^2z^2$이다.
</details>

### 2. Gram factorization
$\Phi$가 $5\times3$이면 $K=\Phi\Phi^\top$의 shape은 무엇인가?
<details><summary>해설 보기</summary>

$K$는 sample 쌍을 비교하므로 $5\times5$이다.
</details>

### 3. non-uniqueness
orthogonal $Q$에 대해 $\tilde\phi(x)=Q\phi(x)$가 같은 kernel을 만드는 이유를 보이라.
<details><summary>해설 보기</summary>

$\tilde\phi(x)^\top\tilde\phi(z)=\phi(x)^\top Q^\top Q\phi(z)=\phi(x)^\top\phi(z)$이다.
</details>

### 4. 모델 해석
두 layer의 centered Gram matrix를 비교할 때 token 수가 다르면 바로 같은 shape의 matrix를 비교할 수 있는가?
<details><summary>해설 보기</summary>

없다. 같은 experimental unit을 정렬하거나 unit 간 summary를 정의해야 한다. token sampling 차이가 representation 차이와 섞이지 않게 고정한다.
</details>

## 근거와 갱신 경계

PSD kernel의 feature-space 표현은 표준 kernel theory에 따른다. Mercer expansion의 측도 조건과 수렴 증명은 뒤 단원에서 제한적으로 다룬다.

## 단원 요약

- feature map의 inner product가 kernel을 만든다.
- kernel trick은 explicit coordinate 없이 Gram matrix로 계산한다.
- feature map은 orthogonal transformation까지 포함해 비유일하다.
- Gram method의 비용은 sample 수에 따라 커진다.

## 통과 기준

- explicit feature map과 kernel을 서로 변환할 수 있는가?
- 같은 kernel이 coordinate identity를 정하지 않는 이유를 설명할 수 있는가?

## 다음 단원

- [A09-KER-04 RKHS 입문](A09-KER-04-rkhs-introduction.md)

## 집필자 점검표

- [x] feature map·Gram matrix·kernel trick을 연결했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
