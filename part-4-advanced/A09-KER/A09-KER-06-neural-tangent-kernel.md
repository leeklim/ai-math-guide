---
id: "A09-KER-06"
title: "neural tangent kernel"
part: 4
stage: "A09-KER"
status: "완료"
prerequisites: ["M03-11", "N05-06", "A09-KER-03"]
estimated_time: "90~120분"
---

# A09-KER-06. neural tangent kernel

## 이 단원이 필요한 이유

neural tangent kernel은 parameter gradient의 inner product로 training sample 사이의 local coupling을 측정한다. network를 initialization 근처에서 linearize하면 squared-loss gradient flow를 kernel dynamics로 쓸 수 있다. 이 근사는 넓은 network의 학습 이론과 finite model 진단을 연결한다.

## 학습 목표

- model Jacobian에서 empirical NTK를 계산할 수 있다.
- squared-loss gradient flow의 output dynamics를 쓸 수 있다.
- fixed-kernel approximation의 가정을 설명할 수 있다.
- NTK similarity와 learned feature semantics를 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [M03-11 Jacobian](../../part-1-foundations/M03/M03-11-jacobian.md), [N05-06 backpropagation](../../part-2-neural-computation/N05/N05-06-backpropagation.md), [A09-KER-03 feature map과 kernel trick](A09-KER-03-feature-map-kernel-trick.md)
- 확인 질문: scalar output $f_\theta(x)$의 parameter gradient는 parameter 수와 같은 길이의 어떤 vector인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $J_\theta(x)=\nabla_\theta f_\theta(x)$ | `J theta of x equals the parameter gradient of f theta of x` | input별 parameter Jacobian row | $p$-vector for scalar output |
| $K_\theta(x,x')$ | `K theta of x and x prime` | neural tangent kernel | scalar |
| $K_\theta=JJ^\top$ | `K theta equals J J transpose` | training sample empirical NTK | $n\times n$ |
| $\dot f_t$ | `f dot at time t` | training output의 시간 미분 | $n$-vector |

## 핵심 개념

scalar-output network에서 empirical NTK는

$$
K_\theta(x,x')=\nabla_\theta f_\theta(x)^\top\nabla_\theta f_\theta(x')
$$

이다. sample Jacobian을 $J\in\mathbb R^{n\times p}$로 쌓으면 $K_\theta=JJ^\top$이므로 PSD이다.

squared loss $L=\tfrac12\lVert f-y\rVert^2$와 parameter gradient flow $\dot\theta=-\nabla_\theta L$를 쓰면 training output은

$$
\dot f_t=-K_{\theta_t}(f_t-y)
$$

를 따른다. $K_{\theta_t}\approx K_{\theta_0}$가 training 동안 유지되면 각 kernel eigenmode의 residual은 큰 eigenvalue 방향부터 빠르게 줄어든다.

finite-width network에서는 Jacobian과 NTK가 변한다. learning rate, parameterization, normalization과 optimizer가 fixed-kernel 근사의 품질에 영향을 준다. NTK는 local training dynamics를 설명하지만 neuron이나 feature의 semantic identity를 정하지 않는다.

## 작은 예제

linear model $f_w(x)=w^\top x$에서는 $\nabla_w f_w(x)=x$이므로 NTK는 $K(x,x')=x^\top x'$이다. parameter가 변해도 kernel은 고정되어 kernel dynamics가 정확하다.

## 흔한 오해

- initialization NTK가 같다고 finite training trajectory 전체가 같다고 결론낼 수는 없다.
- NTK eigenvector는 sample-level learning mode이며 neuron basis의 feature 하나와 같지 않다.

## 연습문제

### 1. NTK
$f_w(x)=wx$인 scalar model에서 두 input $x=2$, $x'=3$의 NTK를 구하라.
<details><summary>해설 보기</summary>

$\partial f/\partial w=x$이므로 $K(2,3)=2\cdot3=6$이다.
</details>

### 2. shape
sample이 10개이고 parameter가 100개이면 scalar-output Jacobian $J$와 $JJ^\top$의 shape은 무엇인가?
<details><summary>해설 보기</summary>

$J$는 $10\times100$, empirical NTK는 $10\times10$이다.
</details>

### 3. eigenmode
fixed NTK eigenvalue가 5인 residual mode와 1인 mode 중 gradient flow에서 어느 쪽이 빠르게 감소하는가?
<details><summary>해설 보기</summary>

동일한 초기 amplitude라면 decay rate가 eigenvalue에 비례하므로 eigenvalue 5인 mode가 빠르다.
</details>

### 4. 모델 해석
한 layer를 ablate한 뒤 NTK가 크게 변했다. 그 layer가 특정 concept을 표현한다고 결론내릴 수 있는가?
<details><summary>해설 보기</summary>

ablation이 local parameter-gradient geometry를 바꿨다는 증거이다. concept 표현에는 labeled behavior, representation control과 intervention specificity가 더 필요하다.
</details>

## 근거와 갱신 경계

output dynamics 식은 continuous-time gradient flow와 squared loss에서 제시했다. discrete optimizer, cross entropy와 multi-output kernel에는 수정이 필요하다.

## 단원 요약

- NTK는 parameter gradient feature의 Gram kernel이다.
- squared-loss output dynamics는 현재 NTK가 residual에 작용하는 식으로 쓴다.
- fixed-kernel regime에서는 eigenvalue가 mode별 학습 속도를 정한다.
- finite network의 NTK는 training 동안 변할 수 있다.

## 통과 기준

- Jacobian에서 empirical NTK와 shape을 계산할 수 있는가?
- fixed-NTK 결론의 가정과 해석 한계를 말할 수 있는가?

## 다음 단원

- [A09-KER-07 parameter-space와 function-space 비교](A09-KER-07-parameter-function-space.md)

## 집필자 점검표

- [x] Jacobian Gram matrix와 output dynamics를 연결했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
