---
id: "A09-SYM-04"
title: "permutation symmetry"
part: 4
stage: "A09-SYM"
status: "완료"
prerequisites: ["A09-SYM-02", "M03-15"]
estimated_time: "90~120분"
---

# A09-SYM-04. permutation symmetry

## 이 단원이 필요한 이유

hidden unit와 attention head의 순서는 이름표일 수 있다. 보상되는 permutation을 무시하면 같은 계산을 하는 두 모델이 coordinate-wise로 전혀 달라 보이고, neuron matching과 parameter averaging이 실패할 수 있다.

## 학습 목표

- 두-layer network의 permutation 보상식을 쓸 수 있다.
- activation과 weight의 permutation을 추적할 수 있다.
- head permutation이 허용되는 조건을 설명할 수 있다.
- matching score와 기능적 동치를 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-SYM-02 orbit와 stabilizer](A09-SYM-02-orbits-stabilizers.md), [M03-15 모델 대칭성](../../part-1-foundations/M03/M03-15-reparameterization-model-symmetries.md)
- 확인 질문: hidden coordinate를 바꾼 뒤 다음 layer에서 inverse를 적용하면 무엇이 보존되는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $P$ | `P` | permutation matrix | orthogonal binary matrix |
| $W_1'=PW_1$ | `W one prime equals P W one` | hidden rows의 재배열 | matrix |
| $W_2'=W_2P^{-1}$ | `W two prime equals W two P inverse` | 다음 layer의 보상 | matrix |
| $\pi\in S_m$ | `pi in S m` | $m$개 unit의 permutation | group element |

## 핵심 개념

$f(x)=W_2\phi(W_1x)$에서 elementwise activation은 $\phi(Pz)=P\phi(z)$를 만족한다. 따라서

$$
W_2P^{-1}\phi(PW_1x)
=W_2P^{-1}P\phi(W_1x)=f(x).
$$

bias가 있으면 함께 permute해야 한다. Transformer head도 concatenation 뒤 output projection의 대응 block을 inverse-permute하면 같은 함수를 만들 수 있지만, head-specific mask·routing·parameter tying이 있으면 허용 symmetry가 줄어든다.

matching은 correlation이나 weight distance를 최소화하는 assignment problem으로 만들 수 있다. 높은 matching score는 기능 동치의 충분조건이 아니다.

## 작은 예제

hidden activation $h=(2,5)$를 swap해 $(5,2)$로 만들고 다음 weight $(3,7)$도 $(7,3)$으로 바꾸면 dot product는 둘 다 $41$이다.

## 흔한 오해

- neuron index가 같다고 seed 간 같은 feature인 것은 아니다.
- 모든 permutation이 symmetry인 것은 아니며 architecture connectivity를 보존해야 한다.

## 연습문제

### 1. 보상 계산
$h=(1,4)$, $w=(2,3)$을 swap permutation으로 동시에 바꿔 dot product가 보존됨을 보이라.
<details><summary>해설 보기</summary>

원래 값은 $14$, 바꾼 값은 $(3,2)\cdot(4,1)=14$이다.
</details>

### 2. bias
$h=\phi(Wx+b)$에서 unit을 permute할 때 $b$는 어떻게 변하는가?
<details><summary>해설 보기</summary>

$b'=Pb$로 같은 unit 순서에 맞춰 permute한다.
</details>

### 3. assignment
두 seed의 neuron correlation matrix에서 one-to-one matching을 쓰는 이유는 무엇인가?
<details><summary>해설 보기</summary>

여러 neuron을 같은 target에 중복 대응시키지 않고 permutation이라는 bijection 제약을 유지하기 위해서다.
</details>

### 4. 평균 모델
permutation alignment 없이 두 network weight를 평균내면 왜 성능이 떨어질 수 있는가?
<details><summary>해설 보기</summary>

서로 다른 hidden unit 역할의 좌표를 성분별로 섞어 두 함수의 symmetry-equivalent structure를 파괴할 수 있기 때문이다.
</details>

## 근거와 갱신 경계

hidden-unit permutation symmetry는 feed-forward network reparameterization의 직접 결과다. architecture-specific routing과 normalization은 case별로 symmetry를 다시 확인한다.

## 단원 요약

- hidden permutation은 다음 layer의 inverse permutation과 함께 함수를 보존할 수 있다.
- bias와 output projection도 대응해 바꾼다.
- matching은 constrained assignment 문제다.
- index·correlation 일치와 기능 동치는 구분한다.

## 통과 기준

- two-layer permutation 보상식을 전개할 수 있는가?
- head permutation의 architecture 조건을 말할 수 있는가?

## 다음 단원

- [A09-SYM-05 scaling·rotation과 gauge freedom](A09-SYM-05-scaling-rotation-gauge.md)

## 집필자 점검표

- [x] permutation 보상과 architecture 조건을 설명했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
