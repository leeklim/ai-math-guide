---
id: "A09-GEO-02"
title: "tangent space와 cotangent space"
part: 4
stage: "A09-GEO"
status: "완료"
prerequisites: ["A09-GEO-01", "M03-10"]
estimated_time: "90~120분"
---

# A09-GEO-02. tangent space와 cotangent space

## 이 단원이 필요한 이유

manifold의 점은 일반적으로 서로 더할 수 없지만 한 점에서 가능한 순간 속도는 vector space를 이룬다. differential은 이 tangent vector를 scalar 변화율로 보내는 cotangent vector다. gradient는 metric을 선택한 뒤에야 differential에서 얻어진다.

## 학습 목표

- curve velocity로 tangent vector를 정의할 수 있다.
- tangent와 cotangent의 pairing을 계산할 수 있다.
- differential과 gradient를 구분할 수 있다.
- decoder Jacobian으로 latent tangent를 ambient 방향에 보낼 수 있다.

## 선수지식 확인

- 선수 단원: [A09-GEO-01 manifold와 local coordinate](A09-GEO-01-manifold-local-coordinate.md), [M03-10 total derivative와 differential](../../part-1-foundations/M03/M03-10-total-derivative-differential.md)
- 확인 질문: linear functional은 vector를 어떤 종류의 값으로 보내는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $T_p\mathcal M$ | `the tangent space of M at p` | $p$에서 가능한 속도 | $d$차원 vector space |
| $T_p^*\mathcal M$ | `the cotangent space of M at p` | tangent vector의 linear functional | dual space |
| $df_p$ | `d f at p` | $f$의 differential | $T_p\mathcal M\to\mathbb R$ |
| $\langle df_p,v\rangle$ | `the pairing of d f at p and v` | $v$ 방향 변화율 | scalar |

## 핵심 개념

curve $\gamma:(-\epsilon,\epsilon)\to\mathcal M$가 $\gamma(0)=p$를 만족하면 $\dot\gamma(0)$이 tangent vector를 나타낸다. chart $x^1,\ldots,x^d$에서는 basis $\partial/\partial x^i$로 쓴다.

smooth function $f:\mathcal M\to\mathbb R$의 differential은

$$
df_p(v)=\left.\frac{d}{dt}f(\gamma(t))\right|_{t=0}
$$

이다. $df_p$는 covector다. metric $g_p$가 주어지면 $df_p(v)=g_p(\operatorname{grad}f,v)$를 만족하는 gradient vector가 정해진다.

decoder $F:\mathbb R^d\to\mathbb R^D$에서 latent velocity $u$의 ambient tangent는 $J_F(z)u$다.

## 작은 예제

원 $\gamma(t)=(\cos t,\sin t)$에서 $t=0$의 tangent는 $(0,1)$이다. 반지름 방향 $(1,0)$은 원 위 curve의 속도가 아니다.

## 흔한 오해

- tangent vector는 반드시 manifold 위의 다른 점을 가리키는 화살표가 아니다.
- differential과 gradient는 Euclidean 좌표에서 수치가 같아 보일 뿐 타입이 다르다.

## 연습문제

### 1. tangent
$\gamma(t)=(\cos t,\sin t)$의 $t=\pi/2$ tangent를 구하라.
<details><summary>해설 보기</summary>

$\dot\gamma(t)=(-\sin t,\cos t)$이므로 $(-1,0)$이다.
</details>

### 2. pairing
$df=(2,-1)$, $v=(3,4)$인 좌표에서 $df(v)$를 구하라.
<details><summary>해설 보기</summary>

$2\cdot3-1\cdot4=2$이다.
</details>

### 3. 타입
metric 없이 $df$를 tangent vector라고 부를 수 없는 이유는 무엇인가?
<details><summary>해설 보기</summary>

$df$는 tangent vector를 scalar로 보내는 dual object이며 vector로 바꾸는 식별에는 metric이 필요하다.
</details>

### 4. Jacobian
$J_F\in\mathbb R^{D\times d}$, $u\in\mathbb R^d$일 때 $J_Fu$의 shape은 무엇인가?
<details><summary>해설 보기</summary>

$\mathbb R^D$의 ambient tangent vector다.
</details>

## 근거와 갱신 경계

curve velocity와 derivation 정의는 smooth manifold의 표준적 동치 정의다. 이 단원은 vector bundle의 formal construction은 생략한다.

## 단원 요약

- tangent space는 한 점에서 가능한 curve 속도의 vector space다.
- cotangent vector는 tangent vector에 작용하는 linear functional이다.
- gradient는 differential과 metric으로부터 정해진다.
- Jacobian은 map 사이 tangent vector를 전달한다.

## 통과 기준

- curve에서 tangent를 계산할 수 있는가?
- differential·gradient·Jacobian의 타입을 구분할 수 있는가?

## 다음 단원

- [A09-GEO-03 metric과 길이](A09-GEO-03-metric-length.md)

## 집필자 점검표

- [x] tangent와 cotangent 타입을 구분했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
