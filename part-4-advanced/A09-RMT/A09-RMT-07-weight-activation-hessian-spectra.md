---
id: "A09-RMT-07"
title: "weight·activation·Hessian spectrum"
part: 4
stage: "A09-RMT"
status: "완료"
prerequisites: ["M02-13", "M03-12", "I06-03", "A09-RMT-06"]
estimated_time: "90~120분"
---

# A09-RMT-07. weight·activation·Hessian spectrum

## 이 단원이 필요한 이유

AI 논문은 weight, activation covariance와 Hessian의 spectrum을 모두 다루지만 세 matrix는 index와 단위가 다르다. 같은 spectral 용어를 쓴다는 이유로 eigenvalue를 직접 비교하면 구조, data distribution과 loss curvature를 섞게 된다.

## 학습 목표

- weight singular value와 covariance·Hessian eigenvalue를 구분할 수 있다.
- 세 spectrum의 index space와 normalization을 명시할 수 있다.
- 대상별 null model을 설계할 수 있다.
- spectral observation에 맞는 모델 해석 claim을 작성할 수 있다.

## 선수지식 확인

- 선수 단원: [M02-13 특이값분해](../../part-1-foundations/M02/M02-13-singular-value-decomposition.md), [M03-12 Hessian](../../part-1-foundations/M03/M03-12-hessian.md), [I06-03 분포와 기초 통계](../../part-3-interpretability/I06/I06-03-distributions-basic-statistics.md), [A09-RMT-06 signal과 noise eigenvalue](A09-RMT-06-signal-noise-eigenvalues.md)
- 확인 질문: rectangular matrix 자체의 singular value와 $W^\top W$ eigenvalue 사이에는 어떤 관계가 있는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $W=U\Sigma V^\top$ | `W equals U Sigma V transpose` | weight matrix의 singular value decomposition | rectangular matrix factorization |
| $C_h=H_c^\top H_c/n$ | `C h equals H c transpose H c over n` | centered activation covariance | $d_h\times d_h$ |
| $\nabla_\theta^2L$ | `the Hessian of L with respect to theta` | parameter-space loss curvature | $p\times p$ |
| $\rho(A)$ | `the spectral radius of A` | eigenvalue absolute value의 최대값 | nonnegative scalar |

## 핵심 개념

weight matrix $W\in\mathbb R^{d_{\mathrm{out}}\times d_{\mathrm{in}}}$에는 singular spectrum을 사용한다. $W^\top W$의 nonzero eigenvalue는 $W$ singular value의 제곱이다. scaling과 parameterization이 바뀌면 weight spectrum도 바뀐다.

activation matrix $H_c\in\mathbb R^{n\times d_h}$의 covariance

$$
C_h=\frac1nH_c^\top H_c
$$

는 지정 input distribution에서 hidden feature variance를 측정한다. layer width, token sampling, centering과 normalization이 spectrum을 바꾼다.

Hessian $\nabla_\theta^2L$은 한 parameter point에서 지정 loss와 dataset의 curvature를 측정한다. negative eigenvalue가 있을 수 있으며, symmetry와 overparameterization이 많은 near-zero direction을 만든다. full Hessian 대신 Hessian-vector product로 leading eigenvalue를 추정할 수 있다.

weight에는 entry variance와 row·column scale을 맞춘 random matrix, activation에는 sample structure를 맞춘 covariance null, Hessian에는 label·data·checkpoint를 고정한 control이 필요하다. 한 null을 세 대상에 재사용하지 않는다.

## 작은 예제

$W$ singular value가 $(3,1)$이면 $W^\top W$의 nonzero eigenvalue는 $(9,1)$이다. 같은 숫자를 activation covariance eigenvalue와 비교해도 단위와 index가 다르므로 기능적 결론은 나오지 않는다.

## 흔한 오해

- rectangular weight matrix의 eigenvalue보다 singular value가 일반적인 비교 대상이다.
- sharp Hessian direction이 곧 많이 사용되는 activation feature라는 뜻은 아니다.

## 연습문제

### 1. singular spectrum
$W$의 singular value가 $(4,2,0)$이면 $W^\top W$의 nonzero eigenvalue를 쓰라.
<details><summary>해설 보기</summary>

singular value를 제곱해 $(16,4)$이다.
</details>

### 2. activation covariance
$H_c$가 $200\times64$이면 $C_h$의 shape과 rank 상한은 무엇인가?
<details><summary>해설 보기</summary>

$C_h$는 $64\times64$이고 rank는 최대 64이다.
</details>

### 3. Hessian sign
Hessian에 negative eigenvalue가 있으면 해당 parameter point를 strict local minimum으로 볼 수 있는가?
<details><summary>해설 보기</summary>

볼 수 없다. 그 eigenvector 방향으로 second-order negative curvature가 있다.
</details>

### 4. 모델 해석
weight와 activation spectrum이 모두 heavy-tailed해 보인다. 같은 mechanism의 증거라고 말할 수 있는가?
<details><summary>해설 보기</summary>

말할 수 없다. 대상 matrix, normalization과 null이 다르므로 각 tail fit과 functional relation을 따로 검증해야 한다.
</details>

## 근거와 갱신 경계

이 단원은 세 spectrum의 측정 대상을 구분한다. heavy-tail exponent fitting, free probability와 large-scale Hessian eigensolver의 정밀 이론은 다루지 않는다.

## 단원 요약

- weight에는 singular spectrum을 사용한다.
- activation covariance spectrum은 sampled input distribution에 의존한다.
- Hessian spectrum은 loss, data와 parameter point의 curvature를 나타낸다.
- 세 대상은 각기 다른 normalization과 null model이 필요하다.

## 통과 기준

- matrix별 spectrum의 index와 단위를 적을 수 있는가?
- 하나의 spectral pattern에서 공통 mechanism을 과잉 주장하지 않을 수 있는가?

## 다음 단원

- [A09-RMT-08 종합 실습: spectrum의 null model](A09-RMT-08-capstone-spectrum-null-model.md)

## 집필자 점검표

- [x] weight·activation·Hessian spectrum의 대상을 구분했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
