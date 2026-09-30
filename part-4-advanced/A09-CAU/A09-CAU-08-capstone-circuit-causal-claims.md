---
id: "A09-CAU-08"
title: "종합 실습: circuit 수준 인과 주장"
part: 4
stage: "A09-CAU"
status: "완료"
prerequisites: ["A09-CAU-01", "A09-CAU-02", "A09-CAU-03", "A09-CAU-04", "A09-CAU-05", "A09-CAU-06", "A09-CAU-07"]
estimated_time: "120~180분"
---

# A09-CAU-08. 종합 실습: circuit 수준 인과 주장

## 이 단원이 필요한 이유

circuit claim은 높은 attribution score나 ablation effect 하나로 완성되지 않는다. variable·graph·intervention·counterfactual·control·population을 한 계약에 묶고, necessity·sufficiency·mediation·abstraction의 증거를 각각 기록해야 한다. 이 실습은 claim strength를 측정 결과에 맞추는 최종 틀을 만든다.

## 학습 목표

- circuit hypothesis를 SCM과 potential outcome으로 표현할 수 있다.
- node·path intervention과 matched control을 설계할 수 있다.
- mediation과 causal abstraction 검증을 held-out data에 배치할 수 있다.
- internal·behavioral·external claim을 증거 수준에 맞춰 작성할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-CAU-01~07](A09-CAU-07-external-validity-internal-interventions.md)
- 확인 질문: 한 component의 necessity와 sufficiency를 모두 보였어도 유일한 mechanism이라고 결론내릴 수 없는 이유는 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $C=(V_C,E_C)$ | `the circuit C with nodes V C and edges E C` | 검증할 circuit hypothesis | directed graph |
| $Y_i(z)$ | `the outcome for prompt i under intervention z` | prompt별 potential outcome | scalar or vector |
| $\tau_C=E[Y(1)-Y(0)]$ | `the average intervention effect of circuit C` | circuit intervention의 평균 effect | scalar or vector contrast |
| $\epsilon_{\mathrm{abs}}$ | `epsilon sub abs` | high·low-level intervention 불일치 | nonnegative scalar |

## 분석 계약

behavior $Y$와 experimental unit인 prompt를 먼저 정한다. clean·corrupted prompt pair, model·checkpoint·token 위치를 고정한다. circuit node는 residual component나 aligned subspace로 정의하고 edge는 downstream information transfer hypothesis로 정의한다. node 선택용 validation set과 final test set을 분리한다.

## 측정 절차

1. observational activation과 attribution으로 candidate를 고르되 이 결과는 localization evidence로만 기록한다.
2. node ablation과 activation patching으로 prompt별 paired necessity·sufficiency effect를 계산한다.
3. path patching으로 candidate edge effect를 측정하고 same-norm random path control과 비교한다.
4. mediator patch를 사용해 total·direct·indirect contrast를 계산하고 interaction을 검사한다.
5. source pairing, zero·mean·resample baseline과 off-manifold distance를 바꿔 robustness를 평가한다.
6. high-level variable과 low-level intervention의 causal abstraction error를 held-out operation에서 측정한다.
7. 새 template와 model seed에서 aligned circuit의 effect를 반복해 외적 타당성 범위를 정한다.

## 결과 기록표

| 증거 | 허용 claim | 추가로 필요한 증거 |
|---|---|---|
| attribution | candidate localization | intervention |
| ablation | 지정 조작에서 necessity | redundancy·baseline control |
| patching | 지정 source에서 sufficiency | source specificity·off-manifold 진단 |
| path effect | 지정 graph edge의 effect | alternate path·interaction control |
| mediation | 정의한 contrast의 indirect effect | identification assumptions |
| abstraction | tested operation의 implementation consistency | unseen operation·domain |
| seed transfer | aligned circuit의 제한적 재현 | architecture·population transfer |

## 흔한 오해

- 여러 positive test를 통과해도 test들이 같은 prompt와 selection을 재사용하면 독립된 증거가 아니다.
- circuit completeness는 관찰한 behavior와 intervention family에 상대적이다.

## 연습문제

### 1. unit
한 prompt에서 30개 token effect를 얻었다. paired uncertainty의 최상위 unit을 무엇으로 두는가?
<details><summary>해설 보기</summary>

prompt를 최상위 unit으로 두고 token effect를 prompt 안에서 요약하거나 clustered inference를 사용한다.
</details>

### 2. sufficiency
candidate circuit만 clean activation으로 patch해 behavior가 복원됐지만 full-model ablation에서 alternate circuit도 같은 복원을 보였다. 어떤 claim을 피하는가?
<details><summary>해설 보기</summary>

candidate circuit이 유일한 sufficient mechanism이라는 claim을 피한다. redundant sufficient path가 있을 수 있다.
</details>

### 3. mediation
node A와 B를 함께 patch한 effect가 개별 effect 합보다 크다. path effect를 어떻게 다루는가?
<details><summary>해설 보기</summary>

interaction을 명시하고 additive mediation decomposition을 그대로 적용하지 않는다. joint intervention contrast를 별도 estimand로 보고한다.
</details>

### 4. final claim
held-out prompt와 두 seed에서 node·path effect는 재현됐지만 새 architecture는 평가하지 않았다. 결론을 작성하라.
<details><summary>해설 보기</summary>

지정 architecture의 두 seed와 평가한 prompt population에서 aligned circuit intervention effect가 재현됐다고 쓴다. 다른 architecture로의 일반화는 주장하지 않는다.
</details>

## 근거와 갱신 경계

이 실습은 circuit claim의 분석 계약과 증거 사다리를 제공한다. 모든 latent confounding을 제거하거나 high-level algorithm의 유일성을 증명하지 않는다.

## 단원 요약

- circuit claim은 graph, intervention family와 population에 상대적이다.
- necessity·sufficiency·path·mediation은 서로 다른 estimand이다.
- causal abstraction은 high·low-level intervention correspondence를 검증한다.
- 외적 타당성은 prompt, seed와 architecture 단계별로 확장한다.

## 통과 기준

- graph–unit–intervention–control–estimand–claim 계약을 완성할 수 있는가?
- positive result와 미검증 범위를 한 문단에 함께 쓸 수 있는가?

## 다음 단원

- A09 선택 심화 7개 모듈의 통합 감사로 넘어간다.

## 집필자 점검표

- [x] circuit 수준 causal claim의 증거 사다리와 외적 범위를 완성했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
