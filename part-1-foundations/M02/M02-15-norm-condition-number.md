---
id: "M02-15"
title: "norm과 condition number"
part: 1
stage: "M02"
status: "완료"
prerequisites:
  - "M02-06"
  - "M02-13"
  - "M02-14"
estimated_time: "120~145분"
---

# M02-15. norm과 condition number

## 이 단원이 필요한 이유

벡터와 행렬의 크기를 말하려면 어떤 norm을 사용하는지 정해야 한다. 같은 벡터도 L1 norm, Euclidean norm과 maximum norm에서 다른 값을 갖는다. 행렬에서는 원소 전체의 크기와 입력을 가장 크게 증폭하는 크기도 구분해야 한다.

condition number는 가역 선형계의 입력 오차가 해에서 얼마나 증폭될 수 있는지 나타낸다. determinant가 0이 아니어도 condition number가 크면 작은 측정 오차와 반올림오차가 해를 크게 바꿀 수 있다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- L1, L2와 infinity norm을 계산하고 차이를 설명할 수 있다.
- Frobenius norm과 spectral norm을 특이값에 연결할 수 있다.
- 행렬 norm으로 $\|\mathbf A\mathbf x\|_2$의 상한을 구할 수 있다.
- 가역 정사각행렬의 2-norm condition number를 계산할 수 있다.
- 상대오차 증폭 경계를 condition number로 설명할 수 있다.
- rank, determinant, norm과 condition number가 답하는 질문을 구분할 수 있다.

## 선수지식 확인

- 선수 단원: [M02-06 연립방정식과 역행렬](M02-06-linear-systems-inverse.md)
- 선수 단원: [M02-13 특이값분해](M02-13-singular-value-decomposition.md)
- 선수 단원: [M02-14 공분산과 PCA](M02-14-covariance-pca.md)
- 확인 질문: 가역행렬의 역행렬과 선형계의 해를 설명할 수 있는가?
- 확인 질문: 가장 큰 특이값과 가장 작은 특이값이 방향별 증폭에서 맡는 역할을 설명할 수 있는가?

역행렬이나 SVD가 불분명하면 선수 단원을 먼저 복습한다.

## 기호와 용어

| 기호·용어 | 읽는 법 | 의미 | 조건 |
|---|---|---|---|
| $\|\mathbf x\|_1$ | 엑스의 일 노름 | 성분 절댓값의 합 | L1 norm |
| $\|\mathbf x\|_2$ | 엑스의 이 노름 | 성분 제곱합의 제곱근 | Euclidean norm |
| $\|\mathbf x\|_\infty$ | 엑스의 무한대 노름 | 성분 절댓값의 최댓값 | maximum norm |
| $\|\mathbf A\|_F$ | 에이의 에프 노름 | 모든 원소 제곱합의 제곱근 | Frobenius norm |
| $\|\mathbf A\|_2$ | 에이의 이 노름 | 단위 입력의 최대 증폭률 | spectral norm |
| $\kappa_2(\mathbf A)$ | 에이의 이 노름 condition number | 최댓값과 최솟값 방향의 증폭률 비 | 이 단원에서는 가역 정사각행렬 |
| 상대오차 | relative error | 오차 크기를 기준값 크기로 나눈 비 | 기준값이 0이 아니어야 한다. |

## 핵심 개념 1. norm은 벡터 크기의 규칙이다

벡터의 norm은 다음 성질을 만족하는 함수다.

1. $\|\mathbf x\|\ge0$이고 $\|\mathbf x\|=0$인 경우는 $\mathbf x=\mathbf 0$뿐이다.
2. $\|\alpha\mathbf x\|=|\alpha|\|\mathbf x\|$다.
3. $\|\mathbf x+\mathbf y\|\le\|\mathbf x\|+\|\mathbf y\|$다.

셋째 조건을 삼각부등식이라고 한다. 서로 다른 norm은 모두 크기를 재지만 좌표를 결합하는 방식이 다르다.

## 핵심 개념 2. 자주 쓰는 세 벡터 norm은 강조점이 다르다

$\mathbf x=(x_1,\ldots,x_n)^\top$에 대해

\[
\|\mathbf x\|_1
=
\sum_{i=1}^{n}|x_i|
\]

\[
\|\mathbf x\|_2
=
\sqrt{\sum_{i=1}^{n}x_i^2}
\]

\[
\|\mathbf x\|_\infty
=
\max_i|x_i|
\]

이다.

L1 norm은 모든 성분의 절댓값을 합한다. L2 norm은 Euclidean 길이를 재고, infinity norm은 가장 큰 성분 하나의 크기를 잰다. 논문에서 오차나 정규화를 비교할 때 norm 종류를 확인해야 한다.

## 핵심 개념 3. Frobenius norm은 행렬 원소 전체의 크기를 잰다

\[
\mathbf A=[a_{ij}]\in\mathbb R^{m\times n}
\]

의 Frobenius norm은

\[
\|\mathbf A\|_F
=
\sqrt{\sum_{i=1}^{m}\sum_{j=1}^{n}a_{ij}^2}
\]

이다. 행렬을 긴 벡터처럼 펼쳐 Euclidean norm을 계산한 값과 같다.

SVD의 특이값으로는

\[
\|\mathbf A\|_F
=
\sqrt{\sum_i\sigma_i^2}
\]

이다. 모든 특이방향의 제곱 크기를 합한다.

## 핵심 개념 4. spectral norm은 가장 큰 방향별 증폭률이다

행렬이 유도하는 2-norm은

\[
\|\mathbf A\|_2
=
\max_{\mathbf x\ne\mathbf 0}
\frac{\|\mathbf A\mathbf x\|_2}{\|\mathbf x\|_2}
=
\sigma_{\max}(\mathbf A)
\]

이다. 단위벡터 중 가장 크게 늘어나는 오른쪽 특이벡터에서 최댓값을 얻는다.

모든 $\mathbf x$에 대해

\[
\|\mathbf A\mathbf x\|_2
\le
\|\mathbf A\|_2\|\mathbf x\|_2
\]

이다. 이 부등식은 입력 크기에서 출력 크기의 최악 상한을 준다.

## 핵심 개념 5. condition number는 방향별 배율의 불균형을 잰다

가역 정사각행렬 $\mathbf A$의 2-norm condition number는

\[
\kappa_2(\mathbf A)
=
\|\mathbf A\|_2\|\mathbf A^{-1}\|_2
\]

이다. 특이값으로 쓰면

\[
\kappa_2(\mathbf A)
=
\frac{\sigma_{\max}(\mathbf A)}
{\sigma_{\min}(\mathbf A)}
\]

이다.

\[
\kappa_2(\mathbf A)\ge1
\]

이며 모든 방향의 길이를 보존하는 직교행렬은 condition number가 1이다. 특이행렬에서는 $\sigma_{\min}=0$이므로 condition number를 무한대로 본다.

scalar $c\ne0$에 대해

\[
\kappa_2(c\mathbf A)=\kappa_2(\mathbf A)
\]

이다. condition number는 행렬 전체의 크기가 아니라 방향별 배율의 비를 잰다.

## 핵심 개념 6. condition number는 선형계 오차의 증폭 경계를 준다

\[
\mathbf A\mathbf x=\mathbf b
\]

에서 $\mathbf A$는 정확하고 우변만 $\delta\mathbf b$만큼 변한다고 하자. 해의 변화는

\[
\delta\mathbf x
=
\mathbf A^{-1}\delta\mathbf b
\]

이다.

2-norm에서

\[
\frac{\|\delta\mathbf x\|_2}{\|\mathbf x\|_2}
\le
\kappa_2(\mathbf A)
\frac{\|\delta\mathbf b\|_2}{\|\mathbf b\|_2}
\]

이다. condition number가 크면 작은 상대 입력 오차가 해의 큰 상대오차로 증폭될 수 있다.

이 식은 최악 방향의 상한이다. 특정 오차가 반드시 그만큼 증폭된다는 뜻은 아니다. $\mathbf A$ 자체에도 오차가 있을 때는 별도의 perturbation 경계가 필요하다.

## 핵심 개념 7. determinant와 condition number는 다른 정보를 준다

determinant 절댓값은 모든 특이값의 곱이다.

\[
|\det(\mathbf A)|
=
\prod_{i=1}^{n}\sigma_i
\]

condition number는 가장 큰 특이값과 가장 작은 특이값의 비다.

\[
\mathbf A=
\begin{bmatrix}
100&0\\
0&0.01
\end{bmatrix}
\]

이면

\[
\det(\mathbf A)=1
\]

이지만

\[
\kappa_2(\mathbf A)
=
\frac{100}{0.01}
=
10^4
\]

이다. 부피는 유지되지만 방향별 배율이 크게 다르다.

## 핵심 개념 8. 정규방정식은 condition number를 제곱한다

full column rank 행렬 $\mathbf A$의 최소제곱 정규방정식은

\[
\mathbf A^\top\mathbf A\widehat{\mathbf x}
=
\mathbf A^\top\mathbf b
\]

이다. $\mathbf A^\top\mathbf A$의 고유값은 $\sigma_i^2$이므로

\[
\kappa_2(\mathbf A^\top\mathbf A)
=
\kappa_2(\mathbf A)^2
\]

이다.

따라서 condition number가 큰 문제에서 정규방정식을 직접 만들면 수치 민감도가 더 커진다. QR 분해나 SVD를 사용한 풀이가 안정적인 대안이 될 수 있다.

## 예제 1. 세 벡터 norm 비교

\[
\mathbf x=
\begin{bmatrix}3\\-4\\0\end{bmatrix}
\]

이면

\[
\|\mathbf x\|_1=3+4=7
\]

\[
\|\mathbf x\|_2=\sqrt{3^2+(-4)^2}=5
\]

\[
\|\mathbf x\|_\infty=4
\]

이다. 같은 벡터도 norm 선택에 따라 크기값이 달라진다.

## 예제 2. 두 행렬 norm 비교

\[
\mathbf A=
\begin{bmatrix}
3&0\\
0&1
\end{bmatrix}
\]

의 특이값은 3과 1이다. 따라서

\[
\|\mathbf A\|_2=3
\]

이고

\[
\|\mathbf A\|_F
=
\sqrt{3^2+1^2}
=
\sqrt{10}
\]

이다. spectral norm은 가장 큰 방향의 배율이고 Frobenius norm은 두 방향의 제곱 크기를 함께 센다.

## 예제 3. condition number와 해의 민감도

\[
\mathbf A=
\begin{bmatrix}
1&0\\
0&0.001
\end{bmatrix},
\qquad
\mathbf b=
\begin{bmatrix}1\\0.001\end{bmatrix}
\]

이면

\[
\mathbf x=
\begin{bmatrix}1\\1\end{bmatrix}
\]

이다. 특이값은 1과 0.001이므로

\[
\kappa_2(\mathbf A)=1000
\]

이다.

우변의 둘째 성분이 $0.001$에서 $0.002$로 바뀌면 해의 둘째 성분은 1에서 2로 바뀐다. 작은 절대오차가 작은 특이값 방향의 역변환에서 크게 확대됐다.

## 예제 4. norm과 모델 민감도

가중치 행렬 $\mathbf W$에 대해

\[
\|\mathbf W\|_2=12
\]

라면

\[
\|\mathbf W\delta\mathbf x\|_2
\le
12\|\delta\mathbf x\|_2
\]

이다. 선형 부분에서 입력 perturbation이 출력으로 증폭되는 최악 상한을 준다.

이 값은 실제 데이터 perturbation이 최악 특이방향과 얼마나 정렬되는지 말하지 않는다. 편향, 비선형함수와 뒤의 층까지 포함한 전체 모델의 행동 민감도도 별도 계산이 필요하다.

## 흔한 오해

### 오해 1. norm은 하나뿐이다

L1, L2와 infinity norm은 서로 다른 크기 규칙이다. 결과를 비교할 때 사용한 norm을 밝혀야 한다.

### 오해 2. Frobenius norm과 spectral norm은 같은 행렬 크기다

Frobenius norm은 모든 특이값을 합성하고 spectral norm은 가장 큰 특이값만 본다.

### 오해 3. 가역이면 수치적으로 안정하다

가역성은 가장 작은 특이값이 0이 아님을 뜻한다. 그 값이 0에 가까우면 condition number가 커져 역문제가 민감할 수 있다.

### 오해 4. condition number가 크면 특정 모델 입력에서 큰 변화가 발생한다

condition number는 선형변환의 최악 방향 상한이다. 주어진 입력 perturbation과 전체 비선형 모델의 실제 변화는 직접 측정해야 한다.

## 연습문제

### 1. 벡터 norm

\[
\mathbf x=
\begin{bmatrix}-2\\1\\2\end{bmatrix}
\]

의 L1, L2와 infinity norm을 구하라.

<details>
<summary>해설 보기</summary>

\[
\|\mathbf x\|_1=2+1+2=5
\]

\[
\|\mathbf x\|_2
=
\sqrt{(-2)^2+1^2+2^2}
=
3
\]

\[
\|\mathbf x\|_\infty=2
\]

이다.

</details>

### 2. Frobenius norm

\[
\mathbf A=
\begin{bmatrix}
1&-2\\
2&1
\end{bmatrix}
\]

의 Frobenius norm을 구하라.

<details>
<summary>해설 보기</summary>

\[
\|\mathbf A\|_F
=
\sqrt{1^2+(-2)^2+2^2+1^2}
=
\sqrt{10}
\]

이다.

</details>

### 3. spectral norm 상한

$\|\mathbf A\|_2=5$이고 $\|\mathbf x\|_2=3$이라고 하자. $\|\mathbf A\mathbf x\|_2$의 상한을 구하라. 실제 값이 반드시 상한과 같은지도 판단하라.

<details>
<summary>해설 보기</summary>

\[
\|\mathbf A\mathbf x\|_2
\le
\|\mathbf A\|_2\|\mathbf x\|_2
=
15
\]

이다. 입력이 가장 큰 오른쪽 특이방향과 정렬될 때 상한에 도달한다. 다른 방향에서는 실제 값이 더 작을 수 있다.

</details>

### 4. condition number 계산

가역행렬의 특이값이 $8,2,0.5$라고 하자. 2-norm condition number를 구하라.

<details>
<summary>해설 보기</summary>

\[
\kappa_2(\mathbf A)
=
\frac{\sigma_{\max}}{\sigma_{\min}}
=
\frac{8}{0.5}
=
16
\]

이다.

</details>

### 5. 상대오차 경계

$\kappa_2(\mathbf A)=200$이고 우변의 상대오차가 $10^{-5}$라고 하자. 행렬 자체에는 오차가 없을 때 해의 상대오차 상한을 구하라.

<details>
<summary>해설 보기</summary>

\[
\frac{\|\delta\mathbf x\|_2}{\|\mathbf x\|_2}
\le
200\cdot10^{-5}
=
2\times10^{-3}
\]

이다. 이는 최악 방향의 상한이며 실제 오차가 이 값과 같다는 뜻은 아니다.

</details>

### 6. 네 개념 구분

정사각행렬에 대해 rank, determinant, spectral norm과 condition number가 각각 답하는 질문을 한 문장씩 적어라.

<details>
<summary>해설 보기</summary>

rank는 독립적으로 살아남는 출력 방향의 수를 센다. determinant는 방향 있는 전체 부피 배율을 나타낸다.

spectral norm은 단위 입력을 가장 크게 늘리는 배율이다. condition number는 가장 큰 배율과 가장 작은 배율의 비로 역문제의 최악 상대 민감도를 나타낸다.

</details>

### 7. M02 누적 확인과제: activation 행렬의 SVD와 저랭크 근사

중심화된 activation 행렬이

\[
\mathbf H_c=
\begin{bmatrix}
2&0\\
-1&1\\
-1&-1
\end{bmatrix}
\in\mathbb R^{3\times2}
\]

라고 하자. 다음을 수행하라.

1. 각 feature 열의 평균이 0인지 확인하라.
2. $\mathbf H_c^\top\mathbf H_c$와 표본 공분산행렬을 구하라.
3. 특이값과 오른쪽 특이벡터를 구하라.
4. rank-1 SVD 근사 $\mathbf H_{c,1}$을 구하라.
5. 보존된 제곱 Frobenius norm의 비율과 재구성 오차를 구하라.
6. 이 결과가 허용하는 표현 주장과 허용하지 않는 기능 주장을 구분하라.

<details>
<summary>해설 보기</summary>

첫 열의 합은 $2-1-1=0$이고 둘째 열의 합은 $0+1-1=0$이다. 두 feature 평균은 0이다.

\[
\mathbf H_c^\top\mathbf H_c
=
\begin{bmatrix}
6&0\\
0&2
\end{bmatrix}
\]

이다. $N=3$이므로 표본 공분산행렬은

\[
\mathbf S
=
\frac{1}{2}
\mathbf H_c^\top\mathbf H_c
=
\begin{bmatrix}
3&0\\
0&1
\end{bmatrix}
\]

이다.

$\mathbf H_c^\top\mathbf H_c$의 고유값은 6과 2이므로 특이값은

\[
\sigma_1=\sqrt6,
\qquad
\sigma_2=\sqrt2
\]

이다. 오른쪽 특이벡터는

\[
\mathbf v_1=
\begin{bmatrix}1\\0\end{bmatrix},
\qquad
\mathbf v_2=
\begin{bmatrix}0\\1\end{bmatrix}
\]

로 고를 수 있다.

첫 특이성분만 남기면 둘째 열을 제거한

\[
\mathbf H_{c,1}
=
\begin{bmatrix}
2&0\\
-1&0\\
-1&0
\end{bmatrix}
\]

이다.

전체 제곱 Frobenius norm은

\[
\|\mathbf H_c\|_F^2
=
\sigma_1^2+\sigma_2^2
=
8
\]

이고 rank-1 근사가 보존한 값은 6이다. 보존 비율은

\[
\frac68=0.75
\]

이다. 재구성 오차는

\[
\|\mathbf H_c-\mathbf H_{c,1}\|_F
=
\sigma_2
=
\sqrt2
\]

이다.

선택한 세 표본의 activation 변동 중 제곱 norm 기준 75%가 첫 feature 방향에 있으며 rank-1 근사가 Frobenius norm에서 최적이라고 말할 수 있다. 첫 방향이 특정 인간 개념을 뜻하는지, 모델이 그 방향을 예측에 사용하는지, 다른 데이터에서도 같은 부분공간이 나타나는지는 이 계산만으로 결론 낼 수 없다.

</details>

## 단원 요약

- norm은 벡터나 행렬의 크기를 재는 규칙이며 종류에 따라 강조하는 구조가 다르다.
- Frobenius norm은 모든 특이값을 합성하고 spectral norm은 가장 큰 특이값이다.
- $\|\mathbf A\mathbf x\|_2\le\|\mathbf A\|_2\|\mathbf x\|_2$는 출력 크기의 최악 상한을 준다.
- condition number는 가장 큰 특이값과 가장 작은 특이값의 비이며 역문제의 상대 민감도를 나타낸다.
- 가역행렬도 condition number가 크면 수치적으로 민감할 수 있다.
- determinant, rank, norm과 condition number는 서로 다른 행렬 성질을 측정한다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- 세 벡터 norm을 계산하고 차이를 설명할 수 있는가?
- Frobenius norm과 spectral norm을 특이값으로 계산할 수 있는가?
- 행렬 norm으로 출력 크기의 상한을 구할 수 있는가?
- condition number를 특이값 비로 계산할 수 있는가?
- 선형계의 상대오차 경계를 해석할 수 있는가?
- rank, determinant, norm과 condition number를 구분할 수 있는가?

## M02 단계 통과 기준

다음 작업을 자료 없이 수행할 수 있으면 M02 단계를 통과한다.

- 벡터의 덧셈, 스칼라곱, 내적과 norm을 계산한다.
- 선형결합, span, 선형독립, 기저와 차원을 연결한다.
- 행렬곱을 행의 내적과 열의 선형결합으로 계산하고 선형변환으로 해석한다.
- 연립방정식의 해를 구하고 kernel, image와 rank로 존재성과 유일성을 설명한다.
- 직교기저를 만들고 부분공간 정사영과 최소제곱을 계산한다.
- determinant, 고유값분해와 대칭행렬의 스펙트럼 분해를 구분한다.
- SVD로 입력 방향, 특이값과 출력 방향을 찾고 저랭크 근사를 만든다.
- 공분산과 PCA를 계산하고 데이터·좌표·개입 증거에 맞춰 주장 범위를 제한한다.
- condition number로 선형계의 수치 민감도를 판단한다.

## 다음 단원

다음 단원은 [M03-01 추상 벡터공간](../M03/M03-01-abstract-vector-spaces.md)이다. 숫자 열벡터에서 배운 연산 법칙을 함수, 다항식과 행렬을 포함하는 일반 벡터공간으로 확장한다.

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] 세 벡터 norm과 두 행렬 norm을 구분했다.
- [x] condition number를 특이값과 상대오차 경계로 연결했다.
- [x] determinant, rank와 condition number의 차이를 설명했다.
- [x] M02 누적 확인과제와 단계 통과 기준을 포함했다.
- [x] 모든 문제에 해설이 있다.
- [x] 수치 민감도와 실제 모델 행동 주장을 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 내부 링크와 수식 구분자를 확인했다.
