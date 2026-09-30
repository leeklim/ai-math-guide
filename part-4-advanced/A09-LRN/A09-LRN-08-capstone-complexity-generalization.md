---
id: "A09-LRN-08"
title: "종합 실습: 복잡도와 일반화"
part: 4
stage: "A09-LRN"
status: "완료"
prerequisites: ["A09-LRN-01", "A09-LRN-02", "A09-LRN-03", "A09-LRN-04", "A09-LRN-05", "A09-LRN-06", "A09-LRN-07"]
estimated_time: "120~180분"
---

# A09-LRN-08. 종합 실습: 복잡도와 일반화

## 이 단원이 필요한 이유

complexity theory를 해석 실험에 적용하려면 theorem 이름을 붙이는 것보다 class, norm constraint, sample unit, selection과 target population을 고정해야 한다. 이 실습은 probe capacity ladder와 여러 generalization split을 한 계약으로 묶는다.

## 학습 목표

- probe capacity ladder와 nested evaluation을 설계할 수 있다.
- empirical gap·random-label control·complexity bound를 분리할 수 있다.
- prompt·template·model generalization을 동시에 기록할 수 있다.
- 결과에 맞는 recoverability claim을 작성할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-LRN-01~07](A09-LRN-07-probe-interpretation-generalization.md)
- 확인 질문: 더 복잡한 probe가 높은 train score를 얻는 것은 왜 예상 가능한가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $c\in\mathcal C$ | `c in the capacity set C` | probe capacity setting | discrete index |
| $G_c$ | `G sub c` | capacity별 generalization gap | scalar |
| $A_{\mathrm{null}}$ | `null-control accuracy` | random-label·random-feature score | scalar |
| $R_{\mathrm{shift}}$ | `risk under distribution shift` | shifted population risk | scalar |

## 분석 계약

같은 activation dataset에 constant, linear, norm-constrained linear, 작은 MLP probe를 사용한다. prompt를 최상위 experimental unit으로 두고 train·validation·iid test·template-shift test를 분리한다. layer·capacity·regularization 선택은 validation 안에서 끝낸다.

## 측정 절차

1. 각 capacity의 train·iid test·shift test risk를 계산한다.
2. prompt bootstrap으로 gap과 model difference interval을 구한다.
3. label permutation과 matched random feature에서 같은 selection pipeline을 반복한다.
4. linear class에는 weight·input norm과 empirical Rademacher upper bound를 기록한다.
5. 독립 model seed에서 선택된 probe protocol을 그대로 반복한다.
6. selected direction intervention을 별도 기능 검증으로 수행한다.

## 결과 기록표

| 증거 | 답하는 질문 | 답하지 못하는 질문 |
|---|---|---|
| iid test risk | 같은 population의 prediction | distribution shift |
| shift risk | 지정 shift의 transfer | 모든 domain |
| random-label control | pipeline memorization | causal use |
| complexity bound | uniform deviation 상한 | 정확한 observed gap |
| intervention | 지정 조작의 output effect | 유일한 mechanism |

## 흔한 오해

- 가장 높은 test score의 probe가 representation의 유일한 올바른 설명은 아니다.
- loose bound와 좋은 empirical generalization은 모순이 아니다.

## 연습문제

### 1. selection
네 capacity 중 하나를 validation으로 고른 뒤 어느 split에서 최종 iid score를 보고하는가?
<details><summary>해설 보기</summary>

capacity 선택에 사용하지 않은 독립 iid test split에서 보고한다.
</details>

### 2. null
real-label score와 random-label score가 둘 다 높으면 무엇을 의심하는가?
<details><summary>해설 보기</summary>

probe capacity 과다, leakage 또는 non-independent split으로 인한 memorization을 의심한다.
</details>

### 3. bound
theoretical upper bound가 0.8인데 observed gap이 0.04여도 모순이 아닌 이유는 무엇인가?
<details><summary>해설 보기</summary>

upper bound는 worst-case 허용 범위이며 실제 data·algorithm에서 tight할 필요가 없기 때문이다.
</details>

### 4. claim
iid와 template shift에서는 잘 되지만 unseen model seed에서 실패했다. 어떻게 결론내리는가?
<details><summary>해설 보기</summary>

해당 model에서 prompt·template generalization은 보였지만 seed 간 representation 일반화는 확인되지 않았다고 제한한다.
</details>

## 근거와 갱신 경계

이 실습은 VC·Rademacher·PAC의 역할을 empirical probe protocol과 연결한다. theory bound를 post hoc으로 맞추기 위해 class·norm을 바꾸지 않는다.

## 단원 요약

- capacity selection과 final evaluation을 분리한다.
- iid·shift·model generalization을 별도 risk로 기록한다.
- null control과 complexity bound는 서로 다른 역할을 한다.
- intervention을 recoverability와 분리된 기능 증거로 둔다.

## 통과 기준

- class–sample–selection–risk–control 계약을 완성할 수 있는가?
- bound·empirical gap·functional use를 구분할 수 있는가?

## 다음 단원

- 다음 선택 모듈은 A09-KER이다.

## 집필자 점검표

- [x] complexity와 여러 일반화 축의 분석 계약을 완성했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
