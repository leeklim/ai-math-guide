---
id: "A09-KER-05"
title: "spectrum과 compact operator 입문"
part: 4
stage: "A09-KER"
status: "완료"
prerequisites: ["M02-11", "M02-12", "A09-KER-04"]
estimated_time: "90~120분"
---

# A09-KER-05. spectrum과 compact operator 입문

## 이 단원이 필요한 이유

Gram matrix의 eigenvector는 finite sample에만 정의된다. population 수준의 kernel geometry를 말하려면 data distribution에 대한 integral operator를 정의해야 한다. compact self-adjoint operator의 spectrum은 행렬의 spectral decomposition을 함수공간으로 옮기는 통로를 제공한다.

## 학습 목표

- kernel integral operator를 정의할 수 있다.
- operator eigenfunction과 matrix eigenvector를 구분할 수 있다.
- kernel expansion에서 eigenvalue와 eigenfunction의 역할을 설명할 수 있다.
- empirical spectrum이 sample과 measure에 의존함을 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [M02-11 고유값과 고유벡터](../../part-1-foundations/M02/M02-11-eigenvalues-eigenvectors.md), [M02-12 대칭행렬과 스펙트럼 정리](../../part-1-foundations/M02/M02-12-symmetric-matrices-spectral-theorem.md), [A09-KER-04 RKHS 입문](A09-KER-04-rkhs-introduction.md)
- 확인 질문: symmetric matrix의 eigenvector basis에서 quadratic form은 어떻게 분해되는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $(T_kf)(x)$ | `T sub k applied to f at x` | kernel integral operator의 출력 | scalar-valued function |
| $T_k\psi_j=\lambda_j\psi_j$ | `T k psi j equals lambda j psi j` | operator eigenfunction equation | function identity |
| $\mu$ | `mu` | input space의 reference distribution | probability measure |
| $d_{\mathrm{eff}}(\tau)$ | `the effective dimension at tau` | threshold에 따른 spectral dimension | nonnegative scalar |

## 핵심 개념

distribution $\mu$와 kernel $k$에 대해 integral operator를

$$
(T_kf)(x)=\int_{\mathcal X}k(x,x')f(x')\,d\mu(x')
$$

로 정의한다. 적절한 boundedness 조건 아래 $T_k$는 positive self-adjoint compact operator가 된다. compact operator는 bounded set을 상대적으로 compact한 set으로 보내며, 무한차원에서도 0 밖의 eigenvalue를 discrete sequence로 다룰 수 있게 한다.

조건이 맞으면 kernel은

$$
k(x,x')=\sum_{j=1}^{\infty}\lambda_j\psi_j(x)\psi_j(x')
$$

로 전개된다. 큰 $\lambda_j$를 가진 eigenfunction은 $\mu$ 아래 kernel variation을 많이 담는다. finite sample에서는 $K/n$의 eigenpair가 population operator를 근사하지만 sample size, normalization과 sampling distribution이 결과에 영향을 준다.

regularization scale $\tau>0$에서

$$
d_{\mathrm{eff}}(\tau)=\sum_j\frac{\lambda_j}{\lambda_j+\tau}
$$

를 쓰면 hard rank보다 scale-sensitive한 dimension을 얻는다.

## 작은 예제

두 point에 uniform measure를 두고 $K=\begin{bmatrix}1&\rho\\\rho&1\end{bmatrix}$를 쓰면 empirical integral operator는 $K/2$이다. eigenvalue는 $(1+\rho)/2$와 $(1-\rho)/2$이며 eigenvector는 constant mode와 contrast mode에 대응한다.

## 흔한 오해

- Gram matrix eigenvalue와 population operator eigenvalue는 normalization 없이 같지 않다.
- 빠른 spectral decay가 곧 label prediction이나 causal mechanism을 뜻하지 않는다.

## 연습문제

### 1. operator
$k(x,x')=1$이고 $\mu$가 probability measure일 때 $(T_kf)(x)$를 쓰라.
<details><summary>해설 보기</summary>

$(T_kf)(x)=\int f(x')d\mu(x')=E_\mu[f(X)]$이며 $x$와 무관한 constant function이다.
</details>

### 2. eigenmode
위 constant kernel operator에서 eigenvalue 1을 갖는 normalized constant function 외의 mean-zero 함수는 어느 eigenvalue를 갖는가?
<details><summary>해설 보기</summary>

mean-zero 함수는 적분값이 0이므로 operator가 zero function으로 보내며 eigenvalue 0을 갖는다.
</details>

### 3. effective dimension
eigenvalue가 $(4,1)$이고 $\tau=1$이면 $d_{\mathrm{eff}}(1)$을 구하라.
<details><summary>해설 보기</summary>

$4/(4+1)+1/(1+1)=0.8+0.5=1.3$이다.
</details>

### 4. 모델 해석
두 model의 activation Gram spectrum을 비교할 때 prompt distribution을 맞춰야 하는 이유는 무엇인가?
<details><summary>해설 보기</summary>

integral operator 자체가 reference distribution $\mu$에 의존한다. prompt distribution이 다르면 model 차이와 measure 차이가 spectrum에 함께 들어간다.
</details>

## 근거와 갱신 경계

spectral expansion은 kernel, domain과 measure에 관한 regularity 조건을 요구한다. 이 단원은 조건의 역할만 밝히며 functional analysis의 증명은 다루지 않는다.

## 단원 요약

- kernel integral operator는 population distribution을 포함한다.
- eigenfunction은 함수공간의 spectral direction이다.
- Gram spectrum은 finite-sample approximation이며 normalization이 필요하다.
- effective dimension은 regularization scale에 따라 달라진다.

## 통과 기준

- integral operator와 eigenfunction equation을 쓸 수 있는가?
- empirical spectrum을 population spectrum과 구분할 수 있는가?

## 다음 단원

- [A09-KER-06 neural tangent kernel](A09-KER-06-neural-tangent-kernel.md)

## 집필자 점검표

- [x] Gram matrix와 population integral operator를 구분했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
