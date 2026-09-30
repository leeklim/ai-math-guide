---
id: "A09-SYM-05"
title: "scaling·rotation과 gauge freedom"
part: 4
stage: "A09-SYM"
status: "완료"
prerequisites: ["A09-SYM-02", "M03-03", "M03-15"]
estimated_time: "90~120분"
---

# A09-SYM-05. scaling·rotation과 gauge freedom

## 이 단원이 필요한 이유

parameter와 hidden coordinate에는 기능을 바꾸지 않는 scale·basis freedom이 존재할 수 있다. gauge freedom을 무시하면 norm, angle, Hessian과 feature identity를 coordinate-independent 사실처럼 해석하게 된다.

## 학습 목표

- positive-homogeneous network의 scaling symmetry를 계산할 수 있다.
- hidden basis rotation의 보상변환을 쓸 수 있다.
- gauge-dependent quantity와 invariant quantity를 구분할 수 있다.
- gauge fixing의 이점과 임의성을 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-SYM-02 orbit와 stabilizer](A09-SYM-02-orbits-stabilizers.md), [M03-03 기저변환](../../part-1-foundations/M03/M03-03-change-of-basis-coordinate-dependence.md), [M03-15 모델 대칭성](../../part-1-foundations/M03/M03-15-reparameterization-model-symmetries.md)
- 확인 질문: basis를 바꾸어도 linear map 자체가 같게 유지되려면 matrix representation은 어떻게 바뀌는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $c>0$ | `c greater than zero` | positive scale | scalar |
| $Q^\top Q=I$ | `Q transpose Q equals I` | orthogonal basis change | matrix identity |
| $h'=Qh$ | `h prime equals Q h` | hidden coordinate rotation | vector |
| $[\theta]$ | `the equivalence class of theta` | gauge orbit | parameter class |

## 핵심 개념

ReLU는 $\phi(cz)=c\phi(z)$ for $c>0$이므로

$$
W_2\phi(W_1x)
=\frac1cW_2\phi(cW_1x)
$$

이다. 한 layer norm은 커지고 다음 layer norm은 작아져도 함수는 같다.

linear hidden interface에서는 $h'=Qh$, $W'=WQ^{-1}$로 basis를 바꿀 수 있다. nonlinearity, normalization, sparsity constraint가 있으면 arbitrary rotation symmetry가 깨질 수 있다.

gauge는 같은 observable function을 나타내는 redundant coordinate freedom이다. gauge fixing은 비교를 위해 representative를 고르지만 선택 자체가 자연법칙은 아니다. function output, properly contracted tensor와 orbit-minimized distance는 gauge-invariant 후보가 된다.

## 작은 예제

$f(x)=abx$에서 $(a,b)$를 $(ca,b/c)$로 바꿔도 product $ab$는 같다. 하지만 $a^2+b^2$는 일반적으로 달라진다.

## 흔한 오해

- weight norm 변화가 항상 function complexity 변화는 아니다.
- whitening으로 coordinate를 고정해도 degenerate eigenspace 안의 rotation freedom이 남을 수 있다.

## 연습문제

### 1. scaling
$a=2,b=3,c=4$에서 $(ca,b/c)$와 product를 구하라.
<details><summary>해설 보기</summary>

$(8,0.75)$이고 product는 원래와 같은 6이다.
</details>

### 2. norm 의존성
위 변환 전후 $a^2+b^2$를 비교하라.
<details><summary>해설 보기</summary>

전에는 13, 후에는 $64+0.5625$로 크게 달라져 gauge-dependent임을 보인다.
</details>

### 3. rotation
$h'=Qh$일 때 scalar output $w^\top h$를 보존하는 $w'$를 구하라.
<details><summary>해설 보기</summary>

$w'=Qw$이면 $w'^\top h'=w^\top Q^\top Qh=w^\top h$이다.
</details>

### 4. Hessian 해석
parameter gauge direction에서 Hessian eigenvalue가 0에 가까울 수 있는 이유는 무엇인가?
<details><summary>해설 보기</summary>

그 방향으로 움직여도 function과 loss가 변하지 않으면 local curvature가 없거나 매우 작기 때문이다.
</details>

## 근거와 갱신 경계

scaling·basis symmetry는 positive homogeneity와 linear coordinate change에서 직접 유도한다. gauge라는 용어는 observable을 보존하는 reparameterization이라는 제한된 의미로 쓴다.

## 단원 요약

- positive homogeneity는 layer 간 scale 교환을 허용한다.
- hidden basis change는 adjacent map의 보상변환이 필요하다.
- parameter norm과 Hessian에는 gauge-dependent 성분이 있다.
- gauge fixing은 비교 규칙이지 유일한 진실이 아니다.

## 통과 기준

- scaling·rotation 보상식을 계산할 수 있는가?
- gauge-dependent 주장과 invariant 주장을 구분할 수 있는가?

## 다음 단원

- [A09-SYM-06 representation theory 입문](A09-SYM-06-representation-theory.md)

## 집필자 점검표

- [x] gauge freedom과 observable을 구분했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
