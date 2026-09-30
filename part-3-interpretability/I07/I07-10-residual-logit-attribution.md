---
id: "I07-10"
title: "residual·logit attribution"
part: 3
stage: "I07"
status: "완료"
prerequisites: ["I07-09", "N05-17"]
estimated_time: "90~120분"
---

# I07-10. residual·logit attribution

## 이 단원이 필요한 이유

Transformer residual stream은 embedding, attention과 MLP update의 합으로 쓸 수 있다. 최종 logit readout이 선형인 지점에서는 각 residual 성분의 직접 logit 기여를 내적으로 분해할 수 있다. 이 계산은 빠른 회계 도구이지만 downstream nonlinear interaction과 component의 필요성을 측정하지 않는다.

## 학습 목표

- residual 성분과 logit direction의 내적을 계산할 수 있다.
- 선형 readout에서 기여 합이 전체 logit과 일치함을 확인할 수 있다.
- LayerNorm·RMSNorm 때문에 정확한 가산 분해가 깨지는 위치를 설명할 수 있다.
- direct attribution과 causal effect를 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [I07-09 path patching](I07-09-path-patching.md), [N05-17 residual stream](../../part-2-neural-computation/N05/N05-17-residual-stream.md)
- 확인 질문: residual update가 합으로 누적될 때 최종 residual vector를 component별 합으로 쓰는 방법은 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $r=\sum_c r_c$ | `r equals the sum over c of r sub c` | residual 성분의 합 | $r,r_c\in\mathbb R^d$ |
| $u_y$ | `u sub y` | token $y$의 unembedding direction | $\mathbb R^d$ |
| $a_{c,y}=u_y^\top r_c$ | `a sub c y equals u sub y transpose r sub c` | component의 direct logit 기여 | scalar |
| logit difference | `logit difference` | target logit minus foil logit | scalar |
| direct logit attribution | `direct logit attribution` | 선택 readout에서의 선형 기여 | decomposition |

## 1. 선형 readout

정규화 이후 vector $z$에 unembedding을 적용하면 token $y$ logit은

$$
\ell_y=u_y^\top z+b_y
$$

이다. $z$가 component 합 $\sum_c z_c$라면

$$
\ell_y-b_y=\sum_c u_y^\top z_c.
$$

target $y$와 foil $q$의 logit 차이는 $u_y-u_q$라는 한 direction으로 분석할 수 있다.

## 2. normalization 경계

최종 residual $r$에 LayerNorm이나 RMSNorm을 적용해 $z=N(r)$를 만든다면 일반적으로

$$
N\left(\sum_c r_c\right)\ne\sum_c N(r_c).
$$

각 raw component를 독립적으로 normalize해 더하는 것은 실제 forward pass와 다르다. 고정된 local linearization이나 특정 decomposition 관례를 쓰면 그 근사와 조건을 명시한다.

## 3. direct와 total effect

direct logit attribution은 component vector가 현재 readout direction과 정렬된 정도다. component를 제거하면 downstream attention·MLP와 normalization이 다시 계산되므로 ablation effect와 같지 않다. 큰 direct contribution은 개입 증거가 아니다.

## 4. CPU 실습

<!-- I07_EXAMPLE: i07_10_residual_logit_attribution -->

세 residual 성분의 내적 합과 전체 residual logit이 같은지 확인한다. 코드는 final nonlinearity를 포함하지 않았다고 결과에 명시한다.

## 흔한 오해

### 오해 1. direct contribution이 큰 head가 필수다

다른 component가 상쇄하거나 대체할 수 있고, head를 제거하면 downstream 계산도 달라진다.

### 오해 2. 모든 layer의 residual 성분을 그대로 최종 logit에 투영하면 정확하다

중간 성분은 이후 layer와 최종 normalization을 통과한다. direct projection은 정한 관례의 진단값이다.

## 연습문제

### 1. 내적

$r_c=(1,2)$, $u_y=(3,-1)$일 때 direct contribution을 구하라.

<details>
<summary>해설 보기</summary>

$3\cdot1+(-1)\cdot2=1$이다.

</details>

### 2. 합 검산

$r_1=(1,0)$, $r_2=(0,2)$, $u=(3,4)$일 때 각 기여와 전체 logit을 구하라.

<details>
<summary>해설 보기</summary>

기여는 3과 8이고 합은 11이다. 전체 residual $(1,2)$와 $u$의 내적도 11이다.

</details>

### 3. logit difference

target direction $u_y=(2,1)$, foil direction $u_q=(1,-1)$이면 차이 direction은 무엇인가?

<details>
<summary>해설 보기</summary>

$u_y-u_q=(1,2)$이다. residual과 이 vector의 내적이 bias를 제외한 logit 차이 기여다.

</details>

### 4. normalization

$N(r)=r/\|r\|$일 때 일반적으로 $N(r_1+r_2)=N(r_1)+N(r_2)$가 아닌 이유를 설명하라.

<details>
<summary>해설 보기</summary>

왼쪽 분모는 합 vector의 norm이고 오른쪽은 각 vector의 norm을 따로 쓴다. normalization은 선형 연산이 아니다.

</details>

### 5. causal claim

한 MLP가 target logit에 큰 양의 direct contribution을 보였다. 다음 검사는 무엇인가?

<details>
<summary>해설 보기</summary>

해당 MLP 출력의 ablation 또는 matched activation patch를 하고 같은 logit difference와 행동 metric 변화를 paired하게 측정한다.

</details>

### 6. 음의 기여

음의 direct contribution을 “해로운 component”로 부르면 안 되는 이유는 무엇인가?

<details>
<summary>해설 보기</summary>

선택한 한 token 대비를 낮춘다는 뜻일 뿐 다른 token, calibration이나 downstream 계산에 필요한 역할을 할 수 있다. 전체 기능 평가는 별도다.

</details>

## 근거와 갱신 경계

Residual stream을 통신 채널로 보고 component를 readout direction에 투영하는 틀은 [Elhage et al. (2021)](https://transformer-circuits.pub/2021/framework/index.html)을 기준으로 한다. 선형 분해가 정확한 계산 위치와 normalization 관례를 항상 함께 기록한다.

## 단원 요약

- 선형 readout에서는 residual component의 내적 기여가 logit을 가산 분해한다.
- logit difference는 target-minus-foil direction으로 계산한다.
- normalization은 raw residual 성분의 단순 가산 투영을 어렵게 한다.
- direct attribution과 ablation·patching effect는 다른 값이다.

## 통과 기준

- component logit 기여를 계산할 수 있는가?
- 가산성이 성립하는 위치를 말할 수 있는가?
- direct contribution과 causal effect를 구분할 수 있는가?

## 다음 단원

- [I07-11 circuit을 그래프로 표현하기](I07-11-circuit-graph.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] 선형 readout과 normalization 경계를 구분했다.
- [x] direct와 causal effect를 분리했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
