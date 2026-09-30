---
id: "A09-SYM-01"
title: "group과 group action"
part: 4
stage: "A09-SYM"
status: "완료"
prerequisites: ["M03-02", "M03-15"]
estimated_time: "90~120분"
---

# A09-SYM-01. group과 group action

## 이 단원이 필요한 이유

neuron을 바꾸어 놓거나 hidden basis를 회전해도 같은 함수를 나타낼 수 있다. group은 합성 가능한 대칭변환의 구조를 표현하고, group action은 그 변환이 parameter·activation·input에 실제로 어떻게 작용하는지 정한다.

## 학습 목표

- group의 네 조건을 확인할 수 있다.
- group 자체와 action을 구분할 수 있다.
- permutation·rotation action의 예를 계산할 수 있다.
- 모델 동치가 어느 대상에 대한 action인지 명시할 수 있다.

## 선수지식 확인

- 선수 단원: [M03-02 선형사상](../../part-1-foundations/M03/M03-02-linear-maps-matrix-representation.md), [M03-15 모델 대칭성](../../part-1-foundations/M03/M03-15-reparameterization-model-symmetries.md)
- 확인 질문: 두 invertible basis change를 연달아 적용하면 어떤 종류의 변환이 되는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $(G,\circ)$ | `the group G with operation composition` | group과 연산 | algebraic structure |
| $e$ | `the identity element` | identity | element of $G$ |
| $g^{-1}$ | `g inverse` | inverse element | element of $G$ |
| $g\cdot x$ | `g acting on x` | $G$의 $X$ 위 action | element of $X$ |

## 핵심 개념

group은 closure, associativity, identity, inverse를 만족한다. action은

$$
e\cdot x=x,
\qquad
(g_1g_2)\cdot x=g_1\cdot(g_2\cdot x)
$$

를 만족하는 map $G\times X\to X$이다. 같은 group도 대상에 따라 다른 action을 가질 수 있다.

hidden unit $m$개를 재배열하는 symmetric group $S_m$은 permutation matrix $P$로 표현할 수 있다. 두 layer $h=\phi(W_1x)$, $y=W_2h$에서 elementwise $\phi$와 호환되면 $W_1\mapsto PW_1$, $W_2\mapsto W_2P^{-1}$가 같은 함수를 만들 수 있다.

## 작은 예제

두 hidden unit을 바꾸는 $P=\begin{bmatrix}0&1\\1&0\end{bmatrix}$는 $P^2=I$이므로 자기 자신이 inverse다.

## 흔한 오해

- 변환 집합이 있다는 사실만으로 group은 아니다. inverse와 closure를 확인해야 한다.
- 같은 함수라는 말은 같은 parameter coordinate라는 뜻이 아니다.

## 연습문제

### 1. group 확인
정수의 덧셈은 group인가?
<details><summary>해설 보기</summary>

그렇다. identity는 0, $n$의 inverse는 $-n$이며 closure와 associativity를 만족한다.
</details>

### 2. action 법칙
matrix multiplication $g\cdot x=gx$가 $GL(d)$의 $\mathbb R^d$ 위 action임을 설명하라.
<details><summary>해설 보기</summary>

$Ix=x$이고 $(g_1g_2)x=g_1(g_2x)$이므로 두 action 법칙을 만족한다.
</details>

### 3. permutation
위 $P$를 vector $(a,b)$에 적용한 결과를 구하라.
<details><summary>해설 보기</summary>

$(b,a)$이다.
</details>

### 4. 모델 해석
representation을 비교할 때 group action의 domain을 적어야 하는 이유는 무엇인가?
<details><summary>해설 보기</summary>

같은 변환 기호라도 input, hidden coordinate, parameter에 작용할 때 보존하는 양과 의미가 다르기 때문이다.
</details>

## 근거와 갱신 경계

group과 group action은 abstract algebra의 표준 정의를 따른다. Lie group의 smooth structure는 다루지 않는다.

## 단원 요약

- group은 합성 가능한 가역 대칭변환의 구조다.
- action은 group element가 특정 대상에 작용하는 규칙이다.
- permutation은 hidden coordinate 동치를 만들 수 있다.
- 모델 대칭성은 action 대상과 보존되는 함수를 함께 적는다.

## 통과 기준

- group 조건과 action 법칙을 확인할 수 있는가?
- neuron permutation의 보상변환을 설명할 수 있는가?

## 다음 단원

- [A09-SYM-02 orbit와 stabilizer](A09-SYM-02-orbits-stabilizers.md)

## 집필자 점검표

- [x] group과 action의 역할을 구분했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
