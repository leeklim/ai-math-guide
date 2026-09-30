---
id: "A09-KER-07"
title: "parameter-space와 function-space 비교"
part: 4
stage: "A09-KER"
status: "완료"
prerequisites: ["M03-15", "N05-03", "A09-KER-06"]
estimated_time: "90~120분"
---

# A09-KER-07. parameter-space와 function-space 비교

## 이 단원이 필요한 이유

neural network의 parameterization에는 permutation과 scaling symmetry가 있다. 같은 함수를 나타내는 parameter point 사이의 Euclidean distance가 클 수 있다. 반대로 작은 parameter perturbation도 Jacobian의 큰 singular direction을 따르면 output을 크게 바꾼다. kernel 관점은 local parameter displacement를 function change와 연결한다.

## 학습 목표

- parameter distance와 function distance의 측정 대상을 구분할 수 있다.
- Jacobian linearization으로 local function change를 근사할 수 있다.
- reparameterization이 parameter metric과 NTK를 바꿀 수 있음을 설명할 수 있다.
- model 비교에 필요한 input distribution과 output metric을 명시할 수 있다.

## 선수지식 확인

- 선수 단원: [M03-15 재매개화와 모델 대칭성 입문](../../part-1-foundations/M03/M03-15-reparameterization-model-symmetries.md), [N05-03 MLP forward pass](../../part-2-neural-computation/N05/N05-03-mlp-forward-pass.md), [A09-KER-06 neural tangent kernel](A09-KER-06-neural-tangent-kernel.md)
- 확인 질문: hidden unit 두 개의 순서를 함께 바꾸어도 MLP output이 유지되는 이유는 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $\Delta\theta$ | `delta theta` | parameter displacement | $p$-vector |
| $J_\theta(x)\Delta\theta$ | `J theta of x times delta theta` | local output change의 first-order 근사 | output-shaped vector |
| $d_\Theta(\theta,\theta')$ | `d sub theta of theta and theta prime` | parameter-space distance | nonnegative scalar |
| $d_P(f,g)$ | `d sub P of f and g` | distribution $P$ 아래 function distance | nonnegative scalar |

## 핵심 개념

parameter distance의 한 예는 $d_\Theta(\theta,\theta')=\lVert\theta-\theta'\rVert_2$이다. function distance는 input distribution $P$와 output metric을 정해

$$
d_P(f_\theta,f_{\theta'})^2
=E_{X\sim P}\left[\lVert f_\theta(X)-f_{\theta'}(X)\rVert_2^2\right]
$$

처럼 정의한다. 두 거리는 다른 space의 양이다.

작은 displacement에서는

$$
f_{\theta+\Delta\theta}(x)-f_\theta(x)
\approx J_\theta(x)\Delta\theta
$$

이다. 여러 input의 Jacobian을 쌓으면 local function distance는 $\Delta\theta^\top J^\top J\Delta\theta$와 연결된다. $J^\top J$는 parameter 방향의 sensitivity를, $JJ^\top$는 sample 사이의 NTK coupling을 나타낸다.

parameter coordinate를 $\theta=g(\eta)$로 바꾸면 Jacobian에 coordinate change가 곱해진다. Euclidean parameter metric과 NTK는 일반적으로 바뀐다. 함수값은 같아도 parameterization-dependent geometry가 달라질 수 있으므로 optimizer와 parameterization을 명세해야 한다.

## 작은 예제

두 layer scalar linear network $f_{a,b}(x)=abx$에서 $(a,b)=(1,1)$과 $(10,0.1)$은 모든 $x$에 같은 함수 $f(x)=x$를 만든다. parameter distance는 크지만 function distance는 0이다.

## 흔한 오해

- weight distance가 작다는 사실만으로 behavior가 비슷하다고 결론낼 수 없다.
- finite prompt set에서 function distance가 0이어도 input space 전체에서 같은 함수라고 할 수 없다.

## 연습문제

### 1. symmetry
$f_{a,b}(x)=abx$에서 $(a,b)=(2,3)$과 같은 함수를 만드는 다른 parameter pair 하나를 쓰라.
<details><summary>해설 보기</summary>

곱이 6이면 된다. 예를 들어 $(a,b)=(1,6)$이 같은 함수를 만든다.
</details>

### 2. linearization
$J=(2,1)$이고 $\Delta\theta=(0.1,-0.2)^\top$일 때 first-order output change를 구하라.
<details><summary>해설 보기</summary>

$J\Delta\theta=2(0.1)+1(-0.2)=0$이다.
</details>

### 3. two Gram matrices
$J$가 $n\times p$이면 $JJ^\top$와 $J^\top J$의 shape과 index 대상을 쓰라.
<details><summary>해설 보기</summary>

$JJ^\top$는 $n\times n$ sample Gram matrix이고 $J^\top J$는 $p\times p$ parameter sensitivity matrix이다.
</details>

### 4. 모델 해석
두 language model의 logits를 비교할 때 $P$와 output metric에 무엇을 명시해야 하는가?
<details><summary>해설 보기</summary>

prompt·token position sampling으로 $P$를 정하고 raw logits, centered logits, probability 또는 KL divergence 중 어느 output comparison을 쓰는지 명시한다.
</details>

## 근거와 갱신 경계

Jacobian linearization은 local approximation이다. displacement가 크거나 activation pattern이 바뀌면 remainder가 커질 수 있다. 자연 gradient와 quotient geometry는 이름만 언급하고 전개하지 않는다.

## 단원 요약

- parameter distance와 function distance는 측정 공간이 다르다.
- Jacobian은 local parameter displacement를 output change로 보낸다.
- $JJ^\top$와 $J^\top J$는 같은 nonzero singular spectrum을 공유하지만 index가 다르다.
- parameterization을 바꾸면 Euclidean metric과 NTK가 바뀔 수 있다.

## 통과 기준

- 두 공간의 distance를 각각 정의할 수 있는가?
- symmetry와 input sampling이 비교 결론을 제한하는 이유를 설명할 수 있는가?

## 다음 단원

- [A09-KER-08 종합 실습: kernel 관점의 학습](A09-KER-08-capstone-kernel-learning.md)

## 집필자 점검표

- [x] parameter·function distance와 Jacobian geometry를 구분했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
