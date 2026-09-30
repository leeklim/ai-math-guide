---
id: "A09-KER-04"
title: "RKHS 입문"
part: 4
stage: "A09-KER"
status: "완료"
prerequisites: ["A09-KER-01", "A09-KER-02", "A09-KER-03"]
estimated_time: "90~120분"
---

# A09-KER-04. RKHS 입문

## 이 단원이 필요한 이유

positive semidefinite kernel은 함수들의 Hilbert space를 정한다. 이 공간에서는 point evaluation을 inner product로 표현할 수 있다. reproducing property와 RKHS norm을 알면 kernel regression의 해가 왜 training sample을 중심으로 한 kernel section의 합으로 나타나는지 이해할 수 있다.

## 학습 목표

- RKHS의 reproducing property를 쓸 수 있다.
- kernel section $k(x,\cdot)$의 역할을 설명할 수 있다.
- RKHS norm이 kernel에 의존하는 complexity measure임을 설명할 수 있다.
- representer theorem의 결론을 finite expansion으로 표현할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-KER-01 함수공간과 operator](A09-KER-01-function-spaces-operators.md), [A09-KER-02 positive definite kernel](A09-KER-02-positive-definite-kernel.md), [A09-KER-03 feature map과 kernel trick](A09-KER-03-feature-map-kernel-trick.md)
- 확인 질문: vector $v$와의 inner product $\langle w,v\rangle$가 $w$에 대한 linear functional인 이유는 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\mathcal H_k$ | `the RKHS associated with k` | kernel $k$가 정한 reproducing kernel Hilbert space | function space |
| $k_x(\cdot)=k(x,\cdot)$ | `the kernel section at x` | evaluation을 대표하는 함수 | element of $\mathcal H_k$ |
| $f(x)=\langle f,k_x\rangle_{\mathcal H_k}$ | `f of x equals the inner product of f and k sub x in H k` | reproducing property | scalar identity |
| $\lVert f\rVert_{\mathcal H_k}$ | `the RKHS norm of f` | kernel 기준 함수 complexity | nonnegative scalar |

## 핵심 개념

RKHS $\mathcal H_k$는 함수들의 Hilbert space이며 각 $x$에 대한 evaluation $f\mapsto f(x)$가 continuous하다. Riesz representation에 따라 evaluation을 대표하는 $k_x\in\mathcal H_k$가 있고

$$
f(x)=\langle f,k_x\rangle_{\mathcal H_k}
$$

가 성립한다. $f=k_{x'}$를 대입하면 $k(x',x)=\langle k_{x'},k_x\rangle$를 얻는다.

regularized empirical risk

$$
\min_{f\in\mathcal H_k}
\frac1n\sum_{i=1}^n \ell(f(x_i),y_i)+\lambda\lVert f\rVert_{\mathcal H_k}^2
$$

의 해는 넓은 조건에서

$$
\hat f(\cdot)=\sum_{i=1}^n\alpha_i k(x_i,\cdot)
$$

형태를 갖는다. representer theorem은 infinite-dimensional optimization을 $n$개 coefficient 문제로 줄인다. RKHS norm이 작다는 말은 선택한 kernel이 선호하는 방향에서 함수가 작다는 뜻이다. kernel을 바꾸면 같은 함수의 norm과 smoothness 해석도 달라진다.

## 작은 예제

$f=2k_{x_1}-k_{x_2}$이면 reproducing property로

$$
f(z)=2k(x_1,z)-k(x_2,z)
$$

를 바로 계산한다. 별도의 coordinate representation이 필요하지 않다.

## 흔한 오해

- RKHS norm이 작은 함수를 모든 관점에서 단순하다고 부를 수는 없다. 단순성은 kernel에 상대적이다.
- representer theorem은 선택한 loss와 regularizer 아래 해의 형태를 정하며 coefficient 값이나 generalization을 자동 보장하지 않는다.

## 연습문제

### 1. reproducing
$f=3k_a+2k_b$일 때 $f(x)$를 kernel 값으로 쓰라.
<details><summary>해설 보기</summary>

$f(x)=3k(a,x)+2k(b,x)$이다.
</details>

### 2. inner product
$\langle k_a,k_b\rangle_{\mathcal H_k}$를 구하라.
<details><summary>해설 보기</summary>

reproducing property에 따라 $k(a,b)$이다.
</details>

### 3. finite expansion
training sample이 20개이면 representer form에는 최대 몇 개의 kernel section이 필요한가?
<details><summary>해설 보기</summary>

training sample마다 하나씩 최대 20개가 필요하다. coefficient 일부가 0이면 더 적을 수 있다.
</details>

### 4. 모델 해석
두 representation에 같은 Gaussian kernel을 적용했지만 bandwidth가 다르다. RKHS norm을 그대로 비교해도 되는가?
<details><summary>해설 보기</summary>

bandwidth가 다른 kernel은 서로 다른 함수공간 geometry를 정한다. norm의 scale과 선호 함수가 달라지므로 kernel parameter를 맞추거나 별도의 calibration을 해야 한다.
</details>

## 근거와 갱신 경계

이 단원은 scalar-valued RKHS와 quadratic norm regularization의 representer form을 다룬다. Hilbert space의 completeness 증명과 vector-valued RKHS는 다루지 않는다.

## 단원 요약

- RKHS에서는 evaluation을 kernel section과의 inner product로 계산한다.
- kernel section은 sample 위치를 중심으로 한 함수이다.
- representer form은 해를 training sample 기반 finite expansion으로 쓴다.
- RKHS norm의 의미는 kernel 선택에 의존한다.

## 통과 기준

- reproducing property로 함수값과 inner product를 계산할 수 있는가?
- RKHS norm을 kernel-relative complexity로 설명할 수 있는가?

## 다음 단원

- [A09-KER-05 spectrum과 compact operator 입문](A09-KER-05-spectrum-compact-operators.md)

## 집필자 점검표

- [x] reproducing property·kernel section·representer form을 연결했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
