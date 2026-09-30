---
id: "I07-07"
title: "activation patching"
part: 3
stage: "I07"
status: "완료"
prerequisites: ["I07-06", "N05-25"]
estimated_time: "120~150분"
---

# I07-07. activation patching

## 이 단원이 필요한 이유

Activation patching은 clean 실행에서 얻은 내부 상태를 corrupt 실행의 같은 위치에 넣고 행동이 얼마나 회복되는지 측정한다. 표현을 읽어내는 probe와 달리 실제 forward 계산을 바꾸지만, 결과는 clean·corrupt 쌍, patch 위치와 metric에 민감하다. 회복률 하나를 component의 보편적 중요도로 읽지 않는다.

## 학습 목표

- clean·corrupt·patched 세 실행을 정확히 정의할 수 있다.
- patch effect와 normalized recovery를 계산할 수 있다.
- module 입력·출력과 residual 위치를 구분할 수 있다.
- patching 결과가 허용하는 국소 인과 주장을 쓸 수 있다.

## 선수지식 확인

- 선수 단원: [I07-06 ablation](I07-06-ablation.md), [N05-25 forward hook과 activation 수집](../../part-2-neural-computation/N05/N05-25-hook-activation-collection.md)
- 확인 질문: forward hook에서 module 입력과 출력 중 무엇을 저장했는지 왜 기록해야 하는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $x_c,x_r$ | `x clean and x corrupt` | clean·corrupt 입력 | input pair |
| $h_j(x_c)$ | `h sub j of x clean` | clean 실행의 node $j$ activation | node tensor |
| $m_c,m_r,m_p$ | `m clean, m corrupt, and m patched` | 세 실행의 행동 metric | scalars |
| $R_j$ | `R sub j` | node $j$ patch의 normalized recovery | scalar |
| interchange intervention | `interchange intervention` | 다른 실행의 내부값으로 교체 | intervention |

## 1. 세 실행

1. clean: 원하는 행동이 나타나는 $x_c$를 실행해 $h_j(x_c)$와 $m_c$를 얻는다.
2. corrupt: 대비 입력 $x_r$를 실행해 $m_r$를 얻는다.
3. patched: $x_r$ 실행 중 $h_j$를 $h_j(x_c)$로 덮어쓰고 $m_p$를 얻는다.

$$
R_j
=
\frac{m_p-m_r}{m_c-m_r}.
$$

$R_j=1$이면 지정 metric이 clean 수준으로 회복됐고 0이면 변화가 없다. 분모가 작으면 비율이 불안정하므로 원시 metric도 함께 보고한다. 0보다 작거나 1보다 큰 값도 가능한 실제 결과다.

## 2. patch 위치

Transformer에서 “layer 5를 patch했다”만으로는 부족하다.

- residual stream의 layer 입력 또는 출력
- attention·MLP의 입력 또는 출력
- 전체 token tensor 또는 특정 token
- 전체 hidden vector, neuron 좌표 또는 subspace
- normalization 전 또는 후

서로 다른 위치는 다른 edge 집합과 downstream 계산을 바꾼다.

## 3. clean·corrupt 쌍

두 입력은 목표 feature만 다르고 길이·형식·난이도는 가능한 한 맞춰야 한다. corruption이 여러 정보를 함께 바꾸면 patch가 회복한 대상도 모호해진다. 여러 입력 쌍에 대해 paired effect와 불확실성을 계산한다.

## 4. CPU 실습

<!-- I07_EXAMPLE: i07_07_activation_patching -->

작은 MLP의 전체 hidden vector를 clean 값으로 바꾸면 합성 예제에서는 recovery가 1이다. 전체 vector를 교체했으므로 개별 neuron의 역할은 결론 내리지 않는다.

## 5. Pythia-160M 실제 모델 실험

`The capital of France is`와 `The capital of Germany is`를 clean·corrupt 쌍으로 두고 layer 5 MLP down-projection의 마지막-token 출력을 patch한다. metric은 `Paris` minus `Berlin` next-token logit이다.

<!-- GPU_EXPERIMENT: pythia_160m_activation_patching -->

고정 실행에서 clean metric은 5.0, corrupt metric은 -3.0, patched metric은 -2.5였고 recovery는 0.0625였다. 이 작은 회복은 해당 한 node patch가 이 대비를 일부만 바꿨다는 결과다. 다른 layer·component가 회로라는 결론이나 Pythia가 사실을 같은 방식으로 저장한다는 결론은 아니다.

## 흔한 오해

### 오해 1. recovery가 가장 큰 위치가 정보를 저장하는 유일한 장소다

patch effect는 downstream 경로, corruption과 metric을 포함한다. 분산 표현과 중복 경로에서는 여러 위치가 효과를 보일 수 있다.

### 오해 2. recovery 0은 component가 사용되지 않는다는 뜻이다

patch 값이 receiver가 사용할 수 없는 상태이거나 다른 경로가 동시에 손상됐을 수 있다. null result에도 검출력과 개입 타당성 검사가 필요하다.

## 연습문제

### 1. recovery 계산

$m_c=10,m_r=2,m_p=6$일 때 recovery를 구하라.

<details>
<summary>해설 보기</summary>

$(6-2)/(10-2)=4/8=0.5$이다.

</details>

### 2. overshoot

$m_p=12$라면 recovery가 1보다 큰 이유를 설명하라.

<details>
<summary>해설 보기</summary>

patch 실행이 clean metric 10을 넘어섰기 때문이다. 비율은 $(12-2)/8=1.25$이며 계산 오류라고 잘라내지 않는다.

</details>

### 3. 불안정한 분모

$m_c$와 $m_r$가 거의 같을 때 어떤 문제가 생기는가?

<details>
<summary>해설 보기</summary>

작은 측정 오차도 recovery 비율을 크게 바꾼다. clean·corrupt 대비가 행동을 충분히 분리하는지 먼저 검사하고 원시 차이를 함께 보고한다.

</details>

### 4. 위치 계약

“attention head 3을 patch했다”에 더 필요한 위치 정보 세 가지를 적어라.

<details>
<summary>해설 보기</summary>

layer, token 위치, head의 value/output 또는 residual 기여 중 무엇인지 적는다. normalization 전후와 전체 vector인지도 명시한다.

</details>

### 5. Pythia 결과

recovery 0.0625에서 직접 말할 수 있는 것을 한 문장으로 써라.

<details>
<summary>해설 보기</summary>

고정된 France/Germany prompt 쌍에서 layer 5 MLP 마지막-token 출력 patch가 Paris–Berlin logit 대비의 clean-corrupt 차이 중 6.25%를 회복했다.

</details>

### 6. 대조군

선택한 node patch의 특이성을 검사할 control 두 가지를 제시하라.

<details>
<summary>해설 보기</summary>

같은 layer의 무작위 token이나 norm-matched activation을 patch할 수 있다. clean source를 다른 무관 prompt에서 가져오는 resampled control도 가능하다.

</details>

## 근거와 갱신 경계

Interchange intervention의 인과적 틀은 [Geiger et al. (2021)](https://arxiv.org/abs/2106.02997), metric·corruption 선택이 결과에 미치는 영향은 [Zhang and Nanda (2023)](https://arxiv.org/abs/2309.16042)을 기준으로 한다. 실제 모델 결과는 고정 Pythia revision과 local manifest 범위에 한정한다.

## 단원 요약

- activation patching은 clean 값을 corrupt forward pass에 넣는 interchange intervention이다.
- normalized recovery는 원시 clean·corrupt·patched metric과 함께 본다.
- module·layer·token·좌표와 normalization 위치가 estimand를 결정한다.
- 한 patch 결과는 지정한 입력과 metric에 대한 국소 인과 증거다.

## 통과 기준

- 세 실행과 recovery를 계산할 수 있는가?
- patch 위치 계약을 완전하게 쓸 수 있는가?
- Pythia 결과의 주장 범위를 제한할 수 있는가?

## 다음 단원

- [I07-08 causal tracing](I07-08-causal-tracing.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] clean·corrupt·patched 실행을 구분했다.
- [x] 실제 Pythia 결과와 범위를 명시했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
