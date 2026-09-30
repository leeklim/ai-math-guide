---
id: "A09-GEO-04"
title: "pullback metric과 Jacobian"
part: 4
stage: "A09-GEO"
status: "완료"
prerequisites: ["A09-GEO-03", "M03-11"]
estimated_time: "90~120분"
---

# A09-GEO-04. pullback metric과 Jacobian

## 이 단원이 필요한 이유

latent variable의 작은 변화가 activation이나 output에서 얼마나 크게 나타나는지는 coordinate 차이만으로 알 수 없다. map의 Jacobian이 출력 공간의 metric을 입력 공간으로 옮기면, 입력 방향별 민감도를 길이와 각도로 해석할 수 있다.

## 학습 목표

- pullback metric을 Jacobian으로 계산할 수 있다.
- Jacobian의 singular value와 국소 길이 왜곡을 연결할 수 있다.
- rank가 떨어질 때 metric이 퇴화하는 이유를 설명할 수 있다.
- decoder-induced geometry가 답하는 질문을 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [A09-GEO-03 metric과 길이](A09-GEO-03-metric-length.md), [M03-11 Jacobian](../../part-1-foundations/M03/M03-11-jacobian.md)
- 확인 질문: Jacobian은 작은 입력 변화와 작은 출력 변화를 어떻게 연결하는가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $F:Z\to X$ | `F from Z to X` | representation 또는 decoder map | smooth map |
| $J_F(z)$ | `the Jacobian of F at z` | $F$의 국소 선형화 | $n\times d$ |
| $F^*g$ | `the pullback of g by F` | $X$의 metric을 $Z$로 옮긴 metric | bilinear form |
| $G_Z(z)$ | `G sub Z of z` | 좌표 pullback metric | $d\times d$ |

## 핵심 개념

$X$가 Euclidean metric을 가질 때 $F$가 만드는 pullback metric은

$$
G_Z(z)=J_F(z)^\top J_F(z)
$$

이다. $v\in T_zZ$에 대해

$$
\|v\|_{G_Z}^2=v^\top J_F(z)^\top J_F(z)v=\|J_F(z)v\|_2^2
$$

이므로 입력의 tangent vector 길이를 실제 출력 변화량으로 잰다. $J_F$의 right singular vector는 주된 입력 방향이고 singular value는 그 방향의 국소 확대율이다.

$J_F$가 full column rank이면 $G_Z$는 positive definite이다. rank가 떨어지면 어떤 $v\ne0$에 대해 $J_Fv=0$이므로 그 방향의 길이가 0이 된다. 이 경우 $F$는 그 방향의 정보를 국소적으로 구분하지 못한다.

## 작은 예제

$F(z_1,z_2)=(2z_1,z_2,0)$이면 $J_F=\operatorname{diag}(2,1)$에 영행을 붙인 행렬이고, $G_Z=\operatorname{diag}(4,1)$이다. $z_1$ 방향의 작은 이동은 출력에서 두 배로 확대된다.

## 흔한 오해

- $J_F^\top J_F$는 모든 상황에서 입력 공간의 유일한 metric이 아니다. 선택한 map과 출력 metric에 의존한다.
- 큰 singular value가 곧 의미적으로 중요한 feature라는 결론을 주지는 않는다.

## 연습문제

### 1. pullback 계산
$F(z_1,z_2)=(z_1+z_2,z_1-z_2)$의 $G_Z$를 구하라.
<details><summary>해설 보기</summary>

$J_F=\begin{bmatrix}1&1\\1&-1\end{bmatrix}$이므로 $G_Z=J_F^\top J_F=2I$이다.
</details>

### 2. singular value
$J_F$의 singular value가 $(3,1)$이면 대응하는 두 right singular vector 방향의 길이는 각각 몇 배가 되는가?
<details><summary>해설 보기</summary>

각각 3배와 1배가 된다. squared length의 배율은 각각 9와 1이다.
</details>

### 3. rank deficiency
$J_F$의 두 열이 같으면 $G_Z$가 positive definite일 수 있는가?
<details><summary>해설 보기</summary>

없다. 열이 선형 종속이므로 null direction이 존재하고 그 방향의 pullback length가 0이다.
</details>

### 4. 모델 해석
두 decoder의 pullback metric을 비교할 때 고정해야 할 조건을 두 가지 쓰라.
<details><summary>해설 보기</summary>

같은 latent point·방향과 같은 출력 metric이 필요하다. preprocessing과 scale도 함께 고정해야 한다.
</details>

## 근거와 갱신 경계

pullback metric과 immersion 조건은 differential geometry의 표준 정의를 따른다. 이 단원은 non-Euclidean output metric의 일반식과 measure pullback은 다루지 않는다.

## 단원 요약

- pullback metric은 map 뒤에서 생기는 길이 변화를 입력 공간에 기록한다.
- Euclidean output에서는 $J_F^\top J_F$로 계산한다.
- singular value는 방향별 국소 확대율이다.
- rank가 떨어지면 구분되지 않는 국소 방향이 생긴다.

## 통과 기준

- 간단한 map의 pullback metric을 계산할 수 있는가?
- Jacobian spectrum과 국소 왜곡을 구분해 설명할 수 있는가?

## 다음 단원

- [A09-GEO-05 geodesic과 connection](A09-GEO-05-geodesic-connection.md)

## 집필자 점검표

- [x] pullback metric과 Jacobian을 연결했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
