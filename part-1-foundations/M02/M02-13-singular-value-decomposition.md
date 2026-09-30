---
id: "M02-13"
title: "특이값분해"
part: 1
stage: "M02"
status: "완료"
prerequisites:
  - "M02-08"
  - "M02-09"
  - "M02-12"
estimated_time: "120~145분"
---

# M02-13. 특이값분해

## 이 단원이 필요한 이유

고유값분해는 같은 공간을 같은 공간으로 보내는 정사각행렬에 적용한다. 신경망의 weight와 activation 행렬은 직사각형인 경우가 많다. 특이값분해(singular value decomposition, SVD)는 임의의 실수 행렬을 입력의 직교 방향, 방향별 증폭률과 출력의 직교 방향으로 나눈다.

SVD를 사용하면 rank, 방향별 최대 증폭과 최적 저랭크 근사를 같은 분해에서 읽을 수 있다. 표현 분석에서 activation의 주요 부분공간을 찾거나 weight의 저랭크 구조를 조사할 때 쓰인다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- full SVD와 compact SVD의 행렬 shape을 읽을 수 있다.
- 오른쪽 특이벡터, 특이값과 왼쪽 특이벡터의 역할을 설명할 수 있다.
- $\mathbf A^\top\mathbf A$와 특이값의 관계를 계산할 수 있다.
- 특이값에서 rank와 두 가지 행렬 norm을 구할 수 있다.
- truncated SVD로 작은 행렬의 저랭크 근사를 만들 수 있다.
- 저랭크 구조와 인간 해석 가능한 feature 또는 인과적 사용을 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [M02-08 kernel, image와 rank](M02-08-kernel-image-rank.md)
- 선수 단원: [M02-09 직교기저와 정사영](M02-09-orthogonal-basis-projection.md)
- 선수 단원: [M02-12 대칭행렬과 스펙트럼 정리](M02-12-symmetric-matrices-spectral-theorem.md)
- 확인 질문: rank와 정규직교기저를 설명할 수 있는가?
- 확인 질문: 대칭 PSD 행렬의 고유값과 고유벡터를 해석할 수 있는가?

rank, 정규직교기저나 스펙트럼 정리가 불분명하면 선수 단원을 먼저 복습한다.

## 기호와 용어

| 기호·용어 | 읽는 법 | 의미 | shape·조건 |
|---|---|---|---|
| $\mathbf A=\mathbf U\boldsymbol\Sigma\mathbf V^\top$ | 에이는 유 시그마 브이 전치 | $\mathbf A$의 full SVD | $\mathbf A\in\mathbb R^{m\times n}$ |
| $\mathbf v_i$ | 브이 아래 아이 | $i$번째 오른쪽 특이벡터 | 입력공간 $\mathbb R^n$의 단위벡터 |
| $\sigma_i$ | 시그마 아래 아이 | $i$번째 특이값 | $\sigma_1\ge\cdots\ge0$ |
| $\mathbf u_i$ | 유 아래 아이 | $i$번째 왼쪽 특이벡터 | 출력공간 $\mathbb R^m$의 단위벡터 |
| $\mathbf A_k$ | 에이 아래 케이 | 상위 $k$개 특이성분으로 만든 rank-$k$ 근사 | $k\le\operatorname{rank}(\mathbf A)$ |
| $\|\mathbf A\|_2$ | 에이의 이 노름 | 가장 큰 방향별 증폭률 | spectral norm |
| $\|\mathbf A\|_F$ | 에이의 에프 노름 | 모든 원소 제곱합의 제곱근 | Frobenius norm |

## 핵심 개념 1. full SVD는 세 행렬로 분해한다

\[
\mathbf A\in\mathbb R^{m\times n}
\]

에 대해 full SVD는

\[
\mathbf A
=
\mathbf U\boldsymbol\Sigma\mathbf V^\top
\]

이다. shape은

\[
\mathbf U\in\mathbb R^{m\times m},
\qquad
\boldsymbol\Sigma\in\mathbb R^{m\times n},
\qquad
\mathbf V\in\mathbb R^{n\times n}
\]

이다.

$\mathbf U$와 $\mathbf V$는 직교행렬이다.

\[
\mathbf U^\top\mathbf U=\mathbf I_m,
\qquad
\mathbf V^\top\mathbf V=\mathbf I_n
\]

$\boldsymbol\Sigma$는 주대각에 특이값을 놓고 나머지 원소를 0으로 둔 직사각 대각행렬이다.

## 핵심 개념 2. SVD는 입력 회전, 축별 배율과 출력 회전이다

\[
\mathbf A\mathbf x
=
\mathbf U\boldsymbol\Sigma\mathbf V^\top\mathbf x
\]

를 오른쪽부터 읽으면 다음 계산을 한다.

1. $\mathbf V^\top\mathbf x$: 입력을 오른쪽 특이벡터 기저 좌표로 바꾼다.
2. $\boldsymbol\Sigma$: 각 좌표에 특이값을 곱하고 필요한 경우 dimension을 바꾼다.
3. $\mathbf U$: 출력의 왼쪽 특이벡터 방향으로 바꾼다.

양의 특이값에 대해

\[
\mathbf A\mathbf v_i=\sigma_i\mathbf u_i
\]

이다. $\mathbf v_i$ 방향의 단위 입력이 $\mathbf u_i$ 방향으로 가며 길이가 $\sigma_i$배 된다.

## 핵심 개념 3. 특이값은 대칭행렬의 고유값에서 나온다

\[
\mathbf A
=
\mathbf U\boldsymbol\Sigma\mathbf V^\top
\]

이면

\[
\mathbf A^\top\mathbf A
=
\mathbf V\boldsymbol\Sigma^\top\boldsymbol\Sigma\mathbf V^\top
\]

이다. 따라서 $\mathbf v_i$는 $\mathbf A^\top\mathbf A$의 고유벡터이고

\[
\mathbf A^\top\mathbf A\mathbf v_i
=
\sigma_i^2\mathbf v_i
\]

이다.

마찬가지로

\[
\mathbf A\mathbf A^\top\mathbf u_i
=
\sigma_i^2\mathbf u_i
\]

이다. $\mathbf A^\top\mathbf A$와 $\mathbf A\mathbf A^\top$은 대칭 PSD 행렬이므로 고유값이 0 이상이고 정규직교 고유기저를 갖는다.

## 핵심 개념 4. compact SVD는 0이 아닌 성분만 남긴다

$\operatorname{rank}(\mathbf A)=r$라고 하자. 양의 특이값에 대응하는 열만 남기면

\[
\mathbf A
=
\mathbf U_r\boldsymbol\Sigma_r\mathbf V_r^\top
\]

이다. shape은

\[
\mathbf U_r\in\mathbb R^{m\times r},
\qquad
\boldsymbol\Sigma_r\in\mathbb R^{r\times r},
\qquad
\mathbf V_r\in\mathbb R^{n\times r}
\]

이다.

compact SVD를 합으로 쓰면

\[
\mathbf A
=
\sum_{i=1}^{r}
\sigma_i\mathbf u_i\mathbf v_i^\top
\]

이다. 각 항은 rank 1 행렬이다. 양의 특이값 수가 rank와 같다.

## 핵심 개념 5. 특이값은 행렬의 크기와 증폭을 나타낸다

가장 큰 특이값은 단위벡터를 가장 크게 늘리는 배율이다.

\[
\|\mathbf A\|_2
=
\max_{\|\mathbf x\|_2=1}
\|\mathbf A\mathbf x\|_2
=
\sigma_1
\]

Frobenius norm은 모든 특이값 제곱합의 제곱근이다.

\[
\|\mathbf A\|_F
=
\sqrt{\sum_{i,j}a_{ij}^2}
=
\sqrt{\sum_{i=1}^{r}\sigma_i^2}
\]

두 norm은 서로 다른 질문에 답한다. spectral norm은 가장 큰 방향별 증폭을, Frobenius norm은 행렬 전체 성분의 제곱 크기를 요약한다.

## 핵심 개념 6. truncated SVD는 최적 저랭크 근사를 준다

특이값을 내림차순으로 두고 상위 $k$개 성분만 남기면

\[
\mathbf A_k
=
\sum_{i=1}^{k}
\sigma_i\mathbf u_i\mathbf v_i^\top
\]

이다. $\mathbf A_k$의 rank는 많아도 $k$다.

Eckart-Young 정리에 따르면 $\mathbf A_k$는 spectral norm이나 Frobenius norm에서 $\mathbf A$에 가장 가까운 rank-$k$ 행렬이다. 오차는

\[
\|\mathbf A-\mathbf A_k\|_2
=
\sigma_{k+1}
\]

\[
\|\mathbf A-\mathbf A_k\|_F^2
=
\sum_{i=k+1}^{r}\sigma_i^2
\]

이다.

## 핵심 개념 7. 특이벡터의 부호와 반복 특이값에는 자유도가 있다

\[
\sigma_i\mathbf u_i\mathbf v_i^\top
\]

에서 $\mathbf u_i$와 $\mathbf v_i$의 부호를 동시에 바꾸어도 같은 행렬을 얻는다. 따라서 특이벡터의 부호 자체에는 고정된 의미가 없다.

같은 특이값이 반복되면 해당 특이부분공간 안에서 정규직교기저를 회전해도 SVD를 만들 수 있다. 개별 특이벡터를 feature로 해석할 때는 seed, 표본과 반복 특이값에 따른 안정성을 확인해야 한다.

## 예제 1. 직사각 대각행렬의 SVD

\[
\mathbf A=
\begin{bmatrix}
3&0\\
0&1\\
0&0
\end{bmatrix}
\in\mathbb R^{3\times2}
\]

라고 하자. 한 full SVD는

\[
\mathbf U=\mathbf I_3,
\qquad
\boldsymbol\Sigma=
\begin{bmatrix}
3&0\\
0&1\\
0&0
\end{bmatrix},
\qquad
\mathbf V=\mathbf I_2
\]

이다. 특이값은 $\sigma_1=3$, $\sigma_2=1$이고 rank는 2다.

첫 입력 좌표 방향은 첫 출력 좌표 방향으로 3배, 둘째 입력 좌표 방향은 둘째 출력 좌표 방향으로 1배가 된다.

## 예제 2. $\mathbf A^\top\mathbf A$에서 특이값 확인

예제 1에서

\[
\mathbf A^\top\mathbf A
=
\begin{bmatrix}
9&0\\
0&1
\end{bmatrix}
\]

이다. 고유값은 9와 1이고 양의 제곱근은 3과 1이다. 오른쪽 특이벡터는 표준기저 $\mathbf e_1,\mathbf e_2$다.

## 예제 3. rank-1 근사

예제 1에서 가장 큰 특이성분만 남기면

\[
\mathbf A_1
=
3
\begin{bmatrix}1\\0\\0\end{bmatrix}
\begin{bmatrix}1&0\end{bmatrix}
=
\begin{bmatrix}
3&0\\
0&0\\
0&0
\end{bmatrix}
\]

이다.

\[
\|\mathbf A-\mathbf A_1\|_2=1,
\qquad
\|\mathbf A-\mathbf A_1\|_F=1
\]

이다. 버린 특이값이 1 하나이므로 두 오차가 같다.

## 예제 4. activation 행렬의 저랭크 근사

$N$개 표본의 중심화된 activation을 행으로 쌓은

\[
\mathbf H_c\in\mathbb R^{N\times d}
\]

에 SVD를 적용하자. 상위 $k$개 오른쪽 특이벡터는 feature 공간의 주요 변동 부분공간을 만든다. $\mathbf H_{c,k}$는 Frobenius norm에서 가장 가까운 rank-$k$ activation 행렬이다.

낮은 재구성 오차는 표본 변동을 적은 선형 방향으로 근사할 수 있음을 보여 준다. 각 방향이 하나의 개념을 나타내거나 모델이 그 방향을 예측에 사용한다는 결론은 별도 검증이 필요하다.

## 흔한 오해

### 오해 1. SVD는 정사각행렬에만 적용한다

SVD는 직사각행렬을 포함한 모든 실수 행렬에 존재한다.

### 오해 2. 특이값은 고유값과 같다

특이값은 0 이상이며 $\mathbf A^\top\mathbf A$ 고유값의 제곱근이다. 일반 정사각행렬의 고유값은 음수나 복소수일 수 있다.

### 오해 3. 오른쪽 특이벡터와 왼쪽 특이벡터는 같은 공간에 있다

$\mathbf v_i$는 입력공간 $\mathbb R^n$, $\mathbf u_i$는 출력공간 $\mathbb R^m$에 있다. 직사각행렬에서는 dimension도 다르다.

### 오해 4. 상위 특이벡터 하나는 의미 feature 하나다

SVD는 분산과 행렬 norm을 기준으로 직교 방향을 고른다. 의미 해석, 기저 안정성과 기능적 사용은 별도 증거가 필요하다.

## 연습문제

### 1. full SVD shape

\[
\mathbf A\in\mathbb R^{5\times3}
\]

의 full SVD에서 $\mathbf U$, $\boldsymbol\Sigma$, $\mathbf V$의 shape을 쓰라.

<details>
<summary>해설 보기</summary>

\[
\mathbf U\in\mathbb R^{5\times5},
\qquad
\boldsymbol\Sigma\in\mathbb R^{5\times3},
\qquad
\mathbf V\in\mathbb R^{3\times3}
\]

이다. 곱 $\mathbf U\boldsymbol\Sigma\mathbf V^\top$의 결과는 $5\times3$이다.

</details>

### 2. compact SVD shape

문제 1의 $\mathbf A$가 rank 2일 때 compact SVD의 세 행렬 shape을 쓰라.

<details>
<summary>해설 보기</summary>

\[
\mathbf U_2\in\mathbb R^{5\times2},
\qquad
\boldsymbol\Sigma_2\in\mathbb R^{2\times2},
\qquad
\mathbf V_2\in\mathbb R^{3\times2}
\]

이다. $\mathbf U_2\boldsymbol\Sigma_2\mathbf V_2^\top$은 $5\times3$이다.

</details>

### 3. 방향별 변환

$\sigma_i=4$이고 $\mathbf A\mathbf v_i=\sigma_i\mathbf u_i$라고 하자. 입력 $-3\mathbf v_i$의 출력을 구하라.

<details>
<summary>해설 보기</summary>

선형성에 따라

\[
\mathbf A(-3\mathbf v_i)
=
-3\mathbf A\mathbf v_i
=
-12\mathbf u_i
\]

이다. 입력은 $\mathbf v_i$의 반대 방향으로 3배이고, 출력은 $\mathbf u_i$의 반대 방향으로 12배다.

</details>

### 4. rank와 norm

특이값이

\[
5,\ 2,\ 0,\ 0
\]

인 행렬의 rank, spectral norm과 Frobenius norm을 구하라.

<details>
<summary>해설 보기</summary>

양의 특이값이 두 개이므로 rank는 2다.

\[
\|\mathbf A\|_2=5
\]

이고

\[
\|\mathbf A\|_F
=
\sqrt{5^2+2^2}
=
\sqrt{29}
\]

이다.

</details>

### 5. truncated SVD 오차

특이값이

\[
8,\ 3,\ 1
\]

인 행렬을 rank 1로 근사했다. spectral norm 오차와 Frobenius norm 오차를 구하라.

<details>
<summary>해설 보기</summary>

rank-1 근사는 첫 특이성분을 남기고 3과 1을 버린다.

\[
\|\mathbf A-\mathbf A_1\|_2=3
\]

이고

\[
\|\mathbf A-\mathbf A_1\|_F
=
\sqrt{3^2+1^2}
=
\sqrt{10}
\]

이다.

</details>

### 6. 부호 자유도

\[
\mathbf A
=
\sigma\mathbf u\mathbf v^\top
\]

인 rank-1 행렬에서 $\mathbf u$와 $\mathbf v$를 모두 음수로 바꿔도 $\mathbf A$가 유지됨을 보이라.

<details>
<summary>해설 보기</summary>

\[
\sigma(-\mathbf u)(-\mathbf v)^\top
=
\sigma(-\mathbf u)(-\mathbf v^\top)
=
\sigma\mathbf u\mathbf v^\top
\]

이다. 두 음수 부호가 상쇄된다. 따라서 특이벡터의 부호는 하나로 정해지지 않는다.

</details>

### 7. 저랭크 해석의 범위

중심화된 activation 행렬의 상위 10개 특이성분이 Frobenius norm 제곱의 95%를 차지했다. 다음을 설명하라.

1. 직접 말할 수 있는 근사 성질
2. 데이터와 계산에서 확인할 조건
3. 이 결과만으로 말할 수 없는 feature 주장

<details>
<summary>해설 보기</summary>

해당 activation 표본 행렬은 상위 10개 특이성분을 사용한 rank-10 행렬로 제곱 Frobenius norm 기준 95%를 보존하며 근사할 수 있다.

표본 선택, 중심화 방식, token과 layer, 특이값 간격과 seed에 따른 부분공간 안정성을 확인해야 한다.

10개 방향이 각각 하나의 인간 해석 가능한 개념인지, 모델이 그 방향을 행동에 사용하는지, 다른 데이터에 일반화되는지는 이 결과만으로 결론 낼 수 없다.

</details>

## 단원 요약

- SVD는 임의의 실수 행렬을 입력 직교기저, 특이값과 출력 직교기저로 분해한다.
- $\mathbf A\mathbf v_i=\sigma_i\mathbf u_i$는 입력 특이방향의 방향별 증폭을 나타낸다.
- 특이값 제곱은 $\mathbf A^\top\mathbf A$와 $\mathbf A\mathbf A^\top$의 고유값이다.
- 양의 특이값 수가 rank이며 가장 큰 특이값은 spectral norm이다.
- truncated SVD는 spectral norm과 Frobenius norm에서 최적 저랭크 근사를 만든다.
- 특이벡터의 부호와 반복 특이값 부분공간에는 비유일성이 있으며 의미와 기능은 별도 검증이 필요하다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- full SVD와 compact SVD의 shape을 쓸 수 있는가?
- 세 SVD 인자의 역할을 입력·배율·출력 방향으로 설명할 수 있는가?
- 특이값과 $\mathbf A^\top\mathbf A$ 고유값의 관계를 설명할 수 있는가?
- 특이값에서 rank와 행렬 norm을 계산할 수 있는가?
- truncated SVD 근사와 오차를 계산할 수 있는가?
- 저랭크 구조와 feature 의미·기능 주장을 구분할 수 있는가?

## 다음 단원

- [M02-14 공분산과 PCA](M02-14-covariance-pca.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] full·compact SVD의 shape을 명시했다.
- [x] 입력 방향, 증폭률과 출력 방향을 구분했다.
- [x] 대칭행렬 고유값과의 관계를 설명했다.
- [x] rank, norm과 저랭크 근사를 연결했다.
- [x] 모든 문제에 해설이 있다.
- [x] 저랭크 구조와 의미·기능 주장을 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 내부 링크와 수식 구분자를 확인했다.
