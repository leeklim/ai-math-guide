---
id: "A09-SYM-02"
title: "orbit와 stabilizer"
part: 4
stage: "A09-SYM"
status: "완료"
prerequisites: ["A09-SYM-01", "M03-06"]
estimated_time: "90~120분"
---

# A09-SYM-02. orbit와 stabilizer

## 이 단원이 필요한 이유

대칭변환으로 서로 이동할 수 있는 parameter는 같은 기능적 해의 여러 coordinate 표현일 수 있다. orbit는 한 대상의 모든 대칭 복사본을 모으고 stabilizer는 그 대상을 그대로 두는 변환을 모은다.

## 학습 목표

- orbit와 stabilizer를 계산할 수 있다.
- orbit가 동치류를 만드는 이유를 설명할 수 있다.
- orbit–stabilizer 관계를 finite example에 적용할 수 있다.
- parameter distance가 symmetry orbit 때문에 커질 수 있음을 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-SYM-01 group과 action](A09-SYM-01-groups-actions.md), [M03-06 동치관계와 몫공간](../../part-1-foundations/M03/M03-06-equivalence-relations-quotient-spaces.md)
- 확인 질문: 동치관계로 같은 것으로 볼 대상을 묶으면 무엇이 생기는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $G\cdot x$ | `the G orbit of x` | $x$의 orbit | subset of $X$ |
| $G_x$ | `the stabilizer of x` | $x$를 고정하는 subgroup | subgroup of $G$ |
| $X/G$ | `X modulo G` | orbit들의 quotient | set of equivalence classes |
| $\lvert G\cdot x\rvert$ | `the size of the orbit of x` | finite orbit cardinality | positive integer |

## 핵심 개념 1. orbit는 한 대상을 움직여 얻는 모든 결과다

group $G$가 집합 $X$에 작용한다고 하자. $x\in X$의 orbit는

$$
G\cdot x
=
\{g\cdot x:g\in G\}
$$

다. group element는 여러 개여도 같은 orbit point에 도착할 수 있다. orbit는 사용한 변환의 목록이 아니라 서로 다른 **도착 대상**의 집합이다.

$y=g\cdot x$인 어떤 $g$가 존재할 때 $x\sim y$라고 정의하면 이 관계는 동치관계다. identity가 reflexivity를, inverse가 symmetry를, group product가 transitivity를 보장한다. 따라서 $X$는 서로 겹치지 않는 orbit들로 분할된다.

## 핵심 개념 2. stabilizer는 한 점을 움직이지 않는 변환들이다

$x$의 stabilizer는

$$
G_x
=
\{g\in G:g\cdot x=x\}
$$

다. identity는 항상 $G_x$에 속하고, $x$를 고정하는 두 변환의 곱과 inverse도 $x$를 고정한다. 그러므로 $G_x$는 $G$의 subgroup이다.

stabilizer가 크다는 말은 여러 group element가 $x$에 작용했을 때 새 위치를 만들지 못하고 같은 $x$로 돌아온다는 뜻이다. 대칭이 많은 대상일수록 stabilizer가 커질 수 있다.

<figure class="lesson-figure" markdown="1">

![Three points in an orbit and two stabilizer transformations that leave the original point fixed](../../figures/assets/A09-SYM/A09-SYM-02-orbit-stabilizer.svg)

<figcaption>왼쪽 orbit는 x가 도달할 수 있는 서로 다른 대상들을 모은다. 오른쪽 stabilizer는 서로 다른 변환이라도 결과를 같은 x에 남기는 경우를 모은다.</figcaption>
</figure>

그림에서 왼쪽의 화살표 수와 orbit point 수는 같을 필요가 없다. 서로 다른 두 변환이 같은 점으로 보내면 그 차이는 $x$를 고정하는 stabilizer element로 설명된다. 바로 이 중복 때문에 stabilizer의 크기가 orbit의 크기를 줄인다.

## 핵심 개념 3. orbit 크기는 stabilizer의 coset 수다

finite group에서는 map $g\mapsto g\cdot x$를 생각할 수 있다. 두 element $g_1,g_2$가 같은 orbit point를 만들 조건은

$$
g_1\cdot x=g_2\cdot x
\quad\Longleftrightarrow\quad
g_2^{-1}g_1\in G_x
$$

다. 즉, 같은 left coset에 속하는 group element들은 $x$에서 같은 결과를 만든다. 따라서 서로 다른 orbit point의 수는 stabilizer coset의 수와 같고

$$
|G\cdot x|
=
\frac{|G|}{|G_x|}
$$

이다. 이 식은 group element 수를 결과 수로 단순히 나눈 암기식이 아니라, 같은 결과를 만드는 변환 묶음의 크기가 $|G_x|$라는 counting statement다.

## 핵심 개념 4. quotient는 symmetry 방향을 하나로 묶는다

quotient $X/G$는 각 orbit를 하나의 원소로 보는 집합이다. parameter symmetry에서 한 orbit 전체가 같은 함수를 나타낸다면 quotient의 한 점이 하나의 기능적 해에 대응할 수 있다. 그러나 quotient를 쓴다고 각 orbit에서 대표 parameter가 자동으로 선택되는 것은 아니다.

model parameter $\theta$의 orbit가 같은 function을 나타낸다면 raw distance

$$
\|\theta_1-\theta_2\|
$$

는 기능적 차이와 symmetry orbit을 따른 이동을 함께 센다. 허용한 group $G$ 아래 symmetry-aligned distance는

$$
d_G(\theta_1,\theta_2)
=
\min_{g\in G}
\|\theta_1-g\cdot\theta_2\|
$$

처럼 정의할 수 있다. 어떤 $G$를 허용했는지와 minimum을 실제로 찾았는지가 결과의 일부다. alignment 뒤 거리가 작다는 사실은 선택한 symmetry 아래 parameter가 가깝다는 뜻이며, 모든 입력에서 함수가 같다는 결론은 별도 평가가 필요하다.

## 작은 예제

$S_3$가 vector $(1,1,2)$의 coordinate를 permute한다고 하자. group 크기는 $|S_3|=6$이지만 orbit에는

$$
(1,1,2),\quad(1,2,1),\quad(2,1,1)
$$

세 개만 있다. 첫 두 좌표의 값이 모두 1이므로 identity와 두 1의 위치를 바꾸는 permutation이 원래 vector를 그대로 둔다. 따라서 stabilizer 크기는 2이고

$$
|S_3\cdot(1,1,2)|
=
\frac{6}{2}
=3
$$

으로 실제 orbit 크기와 일치한다. 만약 세 coordinate 값이 모두 달랐다면 stabilizer에는 identity만 남고 orbit 크기는 6이 된다.

## 흔한 오해

- stabilizer는 orbit와 반대 개념이 아니라 orbit 크기를 결정하는 subgroup이다.
- quotient를 취했다고 각 동치류의 canonical representative가 자동으로 정해지지 않는다.

## 연습문제

### 1. orbit
부호 group $\{+1,-1\}$이 실수에 곱셈으로 작용할 때 $x=3$의 orbit를 구하라.
<details><summary>해설 보기</summary>

$\{3,-3\}$이다.
</details>

### 2. stabilizer
같은 action에서 $x=0$의 stabilizer를 구하라.
<details><summary>해설 보기</summary>

두 element 모두 0을 고정하므로 group 전체다.
</details>

### 3. orbit–stabilizer
$|G|=24$, $|G_x|=6$이면 orbit 크기는 얼마인가?
<details><summary>해설 보기</summary>

$24/6=4$이다.
</details>

### 4. checkpoint 비교
두 checkpoint의 raw parameter distance가 큰데 같은 orbit일 수 있다면 무엇을 추가로 계산해야 하는가?
<details><summary>해설 보기</summary>

허용한 group action에 대해 $\min_g\|\theta_1-g\cdot\theta_2\|$ 같은 symmetry-aligned distance나 function distance를 계산한다.
</details>

## 근거와 갱신 경계

orbit·stabilizer·quotient action은 group theory의 표준 정의를 따른다. continuous group에서의 measure와 orbit geometry는 다루지 않는다.

## 단원 요약

- orbit는 한 대상의 모든 symmetry copy다.
- stabilizer는 대상을 고정하는 subgroup이다.
- quotient는 orbit를 하나의 동치류로 본다.
- raw parameter distance는 orbit 방향 이동을 기능 차이로 셀 수 있다.

## 통과 기준

- finite action의 orbit와 stabilizer를 구할 수 있는가?
- symmetry-aligned 비교가 필요한 이유를 설명할 수 있는가?

## 다음 단원

- [A09-SYM-03 invariant와 equivariant](A09-SYM-03-invariant-equivariant.md)

## 집필자 점검표

- [x] orbit·stabilizer·quotient를 연결했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
