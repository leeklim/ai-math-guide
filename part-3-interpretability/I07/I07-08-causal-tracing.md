---
id: "I07-08"
title: "causal tracing"
part: 3
stage: "I07"
status: "완료"
prerequisites: ["I07-07"]
estimated_time: "120~150분"
---

# I07-08. causal tracing

## 이 단원이 필요한 이유

Causal tracing은 corruption으로 행동을 무너뜨린 뒤 layer와 token 위치를 하나씩 복원해 어느 위치의 clean state가 행동을 회복하는지 지도로 만든다. 이 지도는 localization 도구다. peak 위치를 지식의 단일 저장 장소나 weight editing의 최적 위치로 바로 해석하면 안 된다.

## 학습 목표

- corruption과 restoration 단계로 causal trace를 설계할 수 있다.
- layer×token recovery map을 계산하고 읽을 수 있다.
- localization과 mechanism·editing 주장을 구분할 수 있다.
- multiple testing과 위치 선택 bias를 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [I07-07 activation patching](I07-07-activation-patching.md)
- 확인 질문: normalized recovery의 분모가 작을 때 결과가 불안정한 이유는 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $R_{\ell,t}$ | `R sub ell t` | layer $\ell$, token $t$ 복원 효과 | scalar |
| $H\in\mathbb R^{L\times T}$ | `H in R to the L by T` | recovery heatmap | matrix |
| corruption | `corruption` | target 행동을 약화시키는 입력·상태 변형 | intervention |
| restoration | `restoration` | clean activation을 한 위치에 복원 | patch |
| localization | `localization` | 효과가 큰 위치를 찾는 단계 | search result |

## 1. 알고리즘

1. clean 실행의 모든 후보 activation을 저장한다.
2. 입력이나 초기 representation을 corrupt해 metric을 낮춘다.
3. 한 번에 한 $(\ell,t)$ 위치를 clean 값으로 복원한다.
4. 각 patched metric으로 $R_{\ell,t}$를 계산한다.

$$
H_{\ell,t}
=
\frac{m_{\ell,t}^{\mathrm{restore}}-m_r}{m_c-m_r}.
$$

후보마다 다른 입력을 쓰지 않고 같은 clean·corrupt pair를 유지한다.

## 2. heatmap이 말하는 것

높은 셀은 그 위치의 clean state가 나머지 corrupt 실행 안에서 metric을 회복시켰다는 뜻이다. 다음은 추가 실험 없이 말할 수 없다.

- 정보가 그 위치에만 저장된다.
- 그 위치가 원래 clean 실행에서 유일하게 필요하다.
- 그 layer의 weight를 편집하면 원하는 행동만 바뀐다.
- 같은 위치가 다른 prompt와 모델에서도 일반화된다.

## 3. search와 검증 분리

수백 개 위치를 훑어 최대값을 고르면 noise peak도 선택된다. discovery 입력에서 위치를 찾고 held-out 입력에서 고정 위치 효과를 다시 평가한다. layer·token 전체를 보고한 heatmap과 사후 선택한 peak 효과를 구분한다.

## 4. CPU 실습

<!-- I07_EXAMPLE: i07_08_causal_tracing -->

2×2 후보 위치의 recovery map을 계산한다. 합성 그래프의 최대 위치는 layer 1 token 0이지만, 이는 정의한 그래프와 corruption에만 해당한다.

## 흔한 오해

### 오해 1. trace peak가 지식의 주소다

복원 효과는 정보, causal bottleneck과 downstream 접근 가능성을 함께 반영한다. 분산된 계산을 한 주소로 축약하지 않는다.

### 오해 2. 위치를 찾으면 편집 위치도 찾았다

activation restoration과 weight update는 다른 개입이다. localization과 editing 성공의 상관은 별도로 검증해야 한다.

## 연습문제

### 1. map shape

12개 layer와 20개 token을 모두 추적하면 recovery map의 shape은 무엇인가?

<details>
<summary>해설 보기</summary>

$12\times20$이다. component 종류까지 나누면 별도 축이 추가된다.

</details>

### 2. recovery 계산

$m_c=4,m_r=0$이고 한 셀의 복원 metric이 1이면 $H_{\ell,t}$는 얼마인가?

<details>
<summary>해설 보기</summary>

$(1-0)/(4-0)=0.25$이다.

</details>

### 3. corruption 검증

corrupt 실행의 metric이 clean과 거의 같으면 tracing을 진행하면 안 되는 이유는 무엇인가?

<details>
<summary>해설 보기</summary>

복원할 행동 차이가 없고 recovery 분모도 작아진다. corruption이 target 행동을 충분히 약화시키는지 먼저 확인해야 한다.

</details>

### 4. selection bias

가장 큰 셀을 같은 데이터에서 최종 효과로 보고할 때 생기는 문제는 무엇인가?

<details>
<summary>해설 보기</summary>

noise와 표본 특이성이 큰 위치를 선택한 뒤 그 값을 다시 쓰므로 효과를 과대평가한다. held-out 입력에서 위치를 고정해 재평가한다.

</details>

### 5. localization과 editing

trace peak가 weight editing 성공을 보장하지 않는 이유를 설명하라.

<details>
<summary>해설 보기</summary>

activation patch는 한 실행의 상태를 바꾸고 weight edit는 모든 입력의 함수 자체를 바꾼다. 목적함수, 입력과 부작용이 다르다.

</details>

### 6. 주장 작성

held-out prompt에서도 같은 layer·token의 복원 효과가 반복됐다. 정당한 결론을 써라.

<details>
<summary>해설 보기</summary>

사전 고정한 입력 범위와 corruption에서 그 layer·token clean state가 target metric 회복에 일관되게 관여했다고 쓴다. 유일한 저장 위치라고 쓰지 않는다.

</details>

## 근거와 갱신 경계

Noise corruption과 state restoration을 이용한 factual recall localization은 [Meng et al. (2022)](https://arxiv.org/abs/2202.05262)을 기준으로 한다. Localization과 editing을 동일시하지 말아야 한다는 반례는 [Hase et al. (2023)](https://arxiv.org/abs/2301.04213)을 함께 본다.

## 단원 요약

- causal tracing은 여러 위치의 activation restoration effect를 지도화한다.
- heatmap peak는 정의한 corruption과 metric 아래의 localization 결과다.
- discovery와 held-out 검증을 분리해야 한다.
- localization은 mechanism의 완전성이나 editing 성공을 보장하지 않는다.

## 통과 기준

- tracing 절차와 map shape을 설명할 수 있는가?
- recovery map을 계산할 수 있는가?
- peak의 과도한 해석과 selection bias를 지적할 수 있는가?

## 다음 단원

- [I07-09 path patching](I07-09-path-patching.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] corruption·restoration·localization을 구분했다.
- [x] selection bias와 held-out 검증을 포함했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 렌더링을 확인했다.
