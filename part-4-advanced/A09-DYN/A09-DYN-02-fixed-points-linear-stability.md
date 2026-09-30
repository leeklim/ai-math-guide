---
id: "A09-DYN-02"
title: "fixed point와 선형 안정성"
part: 4
stage: "A09-DYN"
status: "완료"
prerequisites: ["A09-DYN-01", "M02-11", "M03-11"]
estimated_time: "90~120분"
---

# A09-DYN-02. fixed point와 선형 안정성

## 이 단원이 필요한 이유

학습이나 recurrent computation이 어느 state 근처에 머무는지 알려면 fixed point와 그 주변의 perturbation이 커지는지 줄어드는지를 봐야 한다. Jacobian eigenvalue는 nonlinear dynamics의 국소 안정성을 일차 근사로 판정한다.

## 학습 목표

- continuous·discrete fixed point 조건을 쓸 수 있다.
- Jacobian linearization을 계산할 수 있다.
- eigenvalue로 hyperbolic fixed point의 국소 안정성을 판정할 수 있다.
- non-hyperbolic case에서 선형화가 결론을 주지 못함을 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-DYN-01 미분방정식과 흐름](A09-DYN-01-odes-flows.md), [M02-11 고유값](../../part-1-foundations/M02/M02-11-eigenvalues-eigenvectors.md), [M03-11 Jacobian](../../part-1-foundations/M03/M03-11-jacobian.md)
- 확인 질문: matrix power에서 eigenvalue magnitude가 반복 적용에 미치는 영향은 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $x^*$ | `x star` | fixed point | state |
| $A=Df(x^*)$ | `A equals D f at x star` | linearization matrix | $d\times d$ |
| $\lambda_i(A)$ | `lambda i of A` | $A$의 eigenvalue | complex scalar |
| $\delta x$ | `delta x` | fixed point 주변 perturbation | vector |

## 핵심 개념

continuous system $\dot x=f(x)$의 fixed point는 $f(x^*)=0$이다. $x=x^*+\delta x$로 두면

$$
\dot{\delta x}=Df(x^*)\delta x+O(\|\delta x\|^2).
$$

모든 eigenvalue의 real part가 음수이면 hyperbolic fixed point는 locally asymptotically stable하다. 하나라도 양수이면 unstable direction이 있다. discrete map $x_{k+1}=F(x_k)$에서는 $F(x^*)=x^*$이고 모든 eigenvalue magnitude가 1보다 작을 때 국소 수축이 일어난다.

real part가 0이거나 discrete magnitude가 1인 eigenvalue가 있으면 higher-order term을 무시할 수 없어 선형화만으로 결론을 내리지 않는다.

## 작은 예제

$\dot x=x-x^3$의 fixed point는 $-1,0,1$이다. $f'(x)=1-3x^2$이므로 $0$에서는 $f'=1$로 불안정하고 $\pm1$에서는 $f'=-2$로 안정하다.

## 흔한 오해

- loss gradient가 0이라는 사실만으로 minimum이나 stable point가 보장되지 않는다.
- Jacobian eigenvalue는 전역 basin 크기를 알려주지 않는다.

## 연습문제

### 1. continuous stability
$\dot x=-3x$의 fixed point와 안정성을 구하라.
<details><summary>해설 보기</summary>

$x^*=0$이고 derivative가 $-3<0$이므로 locally asymptotically stable하다.
</details>

### 2. discrete stability
$x_{k+1}=0.5x_k$의 fixed point와 multiplier를 구하라.
<details><summary>해설 보기</summary>

$x^*=0$, multiplier는 $0.5$이며 magnitude가 1보다 작아 안정하다.
</details>

### 3. saddle
$A=\operatorname{diag}(-1,2)$인 linear system의 0은 안정한가?
<details><summary>해설 보기</summary>

아니다. 두 번째 방향 eigenvalue가 양수여서 perturbation이 지수적으로 커지는 saddle이다.
</details>

### 4. 학습 해석
Hessian이 singular한 stationary point에서 gradient flow 안정성을 선형화만으로 확정하기 어려운 이유는 무엇인가?
<details><summary>해설 보기</summary>

zero eigenvalue 방향에서는 일차 변화가 없으므로 higher-order loss geometry가 거동을 결정할 수 있다.
</details>

## 근거와 갱신 경계

fixed point linearization과 hyperbolic stability criterion은 dynamical systems의 표준 결과를 따른다. center manifold theory는 범위 밖이다.

## 단원 요약

- fixed point는 dynamics가 멈추는 state이다.
- Jacobian은 fixed point 주변 perturbation dynamics를 일차 근사한다.
- continuous system은 real part, discrete system은 magnitude를 본다.
- 경계 eigenvalue에서는 higher-order 분석이 필요하다.

## 통과 기준

- 간단한 nonlinear system의 fixed point와 stability를 구할 수 있는가?
- continuous·discrete 판정 기준을 구분할 수 있는가?

## 다음 단원

- [A09-DYN-03 phase portrait와 bifurcation](A09-DYN-03-phase-portrait-bifurcation.md)

## 집필자 점검표

- [x] 선형 안정성의 적용 조건과 한계를 밝혔다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
