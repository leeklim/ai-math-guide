---
id: "I07-13"
title: "mediation과 counterfactual"
part: 3
stage: "I07"
status: "완료"
prerequisites: ["I07-12", "M04-16"]
estimated_time: "120~150분"
---

# I07-13. mediation과 counterfactual

## 이 단원이 필요한 이유

입력 변화가 출력에 미치는 효과 중 얼마가 특정 내부 mediator를 통해 흐르는지 묻는 것이 mediation 분석이다. 모델 내부에서는 counterfactual activation을 덮어쓸 수 있지만, direct·indirect effect의 정의는 어떤 treatment 상태와 mediator 값을 섞는지에 의존한다. 단순한 차이 분해와 통계적 식별을 같은 것으로 취급하지 않는다.

## 학습 목표

- treatment, mediator와 outcome을 계산 그래프에 표시할 수 있다.
- total·direct·mediated effect를 작은 구조방정식에서 계산할 수 있다.
- natural·controlled effect의 개입 차이를 설명할 수 있다.
- 모델 내부 mediation 결과의 범위를 제한할 수 있다.

## 선수지식 확인

- 선수 단원: [I07-12 necessity와 sufficiency](I07-12-necessity-sufficiency.md), [M04-16 상관, 예측과 인과](../../part-1-foundations/M04/M04-16-correlation-causation.md)
- 확인 질문: node 전체를 source 값으로 바꾸는 개입과 특정 edge message만 바꾸는 개입은 어떤 경로를 다르게 건드리는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $T$ | `T` | treatment 또는 입력 조건 | binary or categorical |
| $M(t)$ | `M of t` | treatment $t$ 아래 mediator 값 | tensor |
| $Y(t,m)$ | `Y of t m` | treatment와 mediator를 정한 counterfactual outcome | scalar |
| total effect | `total effect` | treatment 전체 변화 효과 | scalar |
| mediated effect | `mediated effect` | mediator 경로를 통해 전달된 효과 | scalar |

## 1. 구조와 counterfactual

$T\to M\to Y$와 $T\to Y$가 함께 있다고 하자. Total effect는

$$
\operatorname{TE}=Y(1,M(1))-Y(0,M(0))
$$

이다. Treatment를 1로 고정한 상태에서 mediator만 $M(0)$에서 $M(1)$로 바꾸는 mediated effect는

$$
\operatorname{ME}_1=Y(1,M(1))-Y(1,M(0))
$$

이다. 이때 대응 direct effect를 $Y(1,M(0))-Y(0,M(0))$로 두면 가산 구조에서는 합이 TE와 같다.

## 2. controlled와 natural

Controlled direct effect는 mediator를 모든 단위에서 같은 $m$으로 고정한다. Natural effect는 각 treatment에서 자연히 생길 $M(t)$를 교차해서 사용한다. 후자는 한 단위가 동시에 두 treatment 아래 갖는 값을 포함하는 cross-world 정의이며 관찰자료 식별에는 추가 가정이 필요하다.

모델 내부에서는 두 forward pass에서 값을 얻어 교차 patch할 수 있지만, 그 hybrid state가 의미 있는 counterfactual인지 별도 검사가 필요하다.

## 3. mediator의 granularity

Mediator를 한 neuron, head 전체, token별 residual vector 또는 subspace로 정의할 수 있다. 작은 단위는 정밀하지만 off-manifold 위험과 다중비교가 커지고, 큰 단위는 여러 경로를 함께 바꾼다.

## 4. CPU 실습

<!-- I07_EXAMPLE: i07_13_mediation_counterfactual -->

$M=2T$, $Y=T+3M$에서 total effect 7, direct effect 1, mediated effect 6을 계산한다. 이 정확한 합은 가산 합성 구조의 성질이지 모든 신경망에 자동 적용되는 법칙이 아니다.

## 흔한 오해

### 오해 1. total effect는 언제나 direct와 indirect로 유일하게 나뉜다

상호작용과 effect 정의에 따라 분해가 달라질 수 있다. treatment를 어느 값에 고정했는지도 필요하다.

### 오해 2. mediator를 patch할 수 있으면 counterfactual이 타당하다

기술적으로 넣을 수 있다는 사실과 학습 분포에서 의미 있는 상태라는 사실은 다르다.

## 연습문제

### 1. total effect

$M=2T$, $Y=T+3M$에서 $T:0\to1$의 total effect를 구하라.

<details>
<summary>해설 보기</summary>

$T=0$이면 $M=0,Y=0$, $T=1$이면 $M=2,Y=7$이므로 total effect는 7이다.

</details>

### 2. mediated effect

$T=1$을 유지하고 mediator를 $M(0)=0$에서 $M(1)=2$로 바꿀 때 효과를 구하라.

<details>
<summary>해설 보기</summary>

$Y(1,2)-Y(1,0)=7-1=6$이다.

</details>

### 3. direct effect

Mediator를 $M(0)=0$에 고정하고 treatment만 0에서 1로 바꾸면 효과는 얼마인가?

<details>
<summary>해설 보기</summary>

$Y(1,0)-Y(0,0)=1-0=1$이다. 이 가산 예제에서는 direct 1과 mediated 6의 합이 total 7이다.

</details>

### 4. 상호작용

$Y=T\cdot M$이면 mediated effect가 treatment 고정값에 의존하는 이유를 설명하라.

<details>
<summary>해설 보기</summary>

$T=0$에 고정하면 mediator를 바꿔도 outcome은 0이다. $T=1$에서는 mediator 변화가 그대로 outcome에 나타난다.

</details>

### 5. 모델 개입

두 prompt의 head output을 교차 patch할 때 생길 수 있는 타당성 문제는 무엇인가?

<details>
<summary>해설 보기</summary>

다른 downstream state와 일관되지 않은 hybrid activation을 만들 수 있다. source·base 입력을 맞추고 manifold 거리나 resampled control을 검사한다.

</details>

### 6. 주장 작성

특정 head를 통한 mediated effect가 반복됐다. 안전한 결론을 써라.

<details>
<summary>해설 보기</summary>

정의한 treatment pair, mediator patch와 outcome에서 그 head 경로가 측정한 효과 일부를 매개했다는 증거를 얻었다고 쓴다. 인간 개념의 보편적 mediator라고 일반화하지 않는다.

</details>

## 근거와 갱신 경계

Language model 내부 component에 causal mediation을 적용한 방법은 [Vig et al. (2020)](https://proceedings.neurips.cc/paper_files/paper/2020/hash/92650b2e92217715fe312e6fa7b90d82-Abstract.html)을 기준으로 한다. 자연효과의 식별 가정과 모델 내부 hybrid state의 타당성을 분리한다.

## 단원 요약

- mediation은 treatment 효과가 내부 mediator를 통해 흐르는 부분을 묻는다.
- direct·mediated effect는 어떤 값을 고정하고 교차하는지에 의존한다.
- 가산 분해는 상호작용이 있는 모델에서 자동으로 성립하지 않는다.
- 실행 가능한 patch와 의미 있는 counterfactual은 다르다.

## 통과 기준

- 작은 구조방정식의 세 effect를 계산할 수 있는가?
- controlled와 natural effect를 구분할 수 있는가?
- mediator granularity와 타당성 한계를 쓸 수 있는가?

## 다음 단원

- [I07-14 off-manifold intervention](I07-14-off-manifold-intervention.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] treatment·mediator·outcome을 정의했다.
- [x] effect 정의와 식별 한계를 구분했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
