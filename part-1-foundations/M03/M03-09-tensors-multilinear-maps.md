---
id: "M03-09"
title: "tensor와 multilinear map"
part: 1
stage: "M03"
status: "완료"
prerequisites:
  - "M03-07"
  - "M03-08"
  - "M00-09"
estimated_time: "125~150분"
---

# M03-09. tensor와 multilinear map

## 이 단원이 필요한 이유

신경망 코드에서는 여러 축을 가진 배열을 tensor라고 부른다. 수학에서는 tensor를 기저를 바꿔도 같은 대상으로 해석할 수 있는 multilinear 구조로 정의한다. 좌표 배열은 tensor의 성분을 저장하지만, 배열의 shape만으로 수학적 tensor의 입력·출력 타입과 변환 법칙이 정해지지는 않는다.

activation, attention score와 고차 미분을 읽으려면 축의 의미와 합을 취하는 인덱스를 추적해야 한다. multilinear map은 여러 입력 중 하나씩 고정했을 때 남은 입력에 선형이다. 이 관점은 행렬곱, bilinear score와 tensor contraction을 같은 계산 규칙으로 연결한다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- multilinear map을 각 입력별 선형성으로 정의할 수 있다.
- covector와 bilinear form을 낮은 order의 tensor로 연결할 수 있다.
- 기저에서 tensor 성분을 만들고 작은 tensor를 벡터들에 적용할 수 있다.
- tensor order, 배열 shape와 행렬 rank를 구분할 수 있다.
- tensor product와 contraction의 결과 shape을 계산할 수 있다.
- 신경망 배열 연산에서 batch, token과 feature 축의 역할을 추적할 수 있다.

## 선수지식 확인

- 선수 단원: [M03-07 쌍대공간과 covector](M03-07-dual-spaces-covectors.md)
- 선수 단원: [M03-08 bilinear form과 quadratic form](M03-08-bilinear-quadratic-forms.md)
- 선수 단원: [M00-09 스칼라·벡터·행렬의 shape](../M00/M00-09-scalars-vectors-matrices-shape.md)
- 확인 질문: covector와 vector의 타입을 구분할 수 있는가?
- 확인 질문: bilinear map이 두 입력 각각에 대해 선형이라는 뜻을 설명할 수 있는가?
- 확인 질문: 행렬곱의 공유 dimension을 찾을 수 있는가?

bilinear form이나 shape 추적이 불분명하면 선수 단원을 먼저 복습한다.

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | 타입·shape |
|---|---|---|---|
| $T:V_1\times\cdots\times V_k\to\mathbb R$ | `T maps V one cross through V k to R` | 각 입력에 대해 선형인 함수 | $k$-linear map |
| $\mathcal T$ | `calligraphic T` | 좌표와 구분한 tensor 객체 | 문맥에서 타입 명시 |
| $T_{i_1\ldots i_k}$ | `T sub i one through i k` | 선택한 기저에서의 tensor 성분 | $k$개 인덱스 |
| $\alpha\otimes\beta$ | `alpha tensor beta` | 두 covector로 만든 order-2 tensor | $(\alpha\otimes\beta)(\mathbf x,\mathbf y)=\alpha(\mathbf x)\beta(\mathbf y)$ |
| tensor order | `tensor order` | tensor가 가진 vector·covector 입력 자리의 수 | 배열 축 수와 문맥상 대응 |
| contraction | `contraction` | 한 입력을 넣거나 대응 인덱스를 합해 order를 줄이는 연산 | 결과 shape 확인 필요 |

## 핵심 개념 1. multilinear map은 각 입력 자리에 대해 선형이다

\[
T:V_1\times\cdots\times V_k\to\mathbb R
\]

가 multilinear라는 말은 나머지 입력을 고정했을 때 각 입력 하나에 대한 함수가 선형이라는 뜻이다.

$r$번째 입력 자리에서

\[
T(\ldots,\alpha\mathbf u+\beta\mathbf v,\ldots)
=
\alpha T(\ldots,\mathbf u,\ldots)
+
\beta T(\ldots,\mathbf v,\ldots)
\]

가 성립해야 한다.

$k=1$이면 covector이고 $k=2$이면 bilinear form이다. $k=3$이면 세 입력을 받는 trilinear form이다.

multilinear map은 모든 입력을 한꺼번에 바꾸는 선형함수가 아니다. 각 입력을 모두 $\alpha$배하면

\[
T(\alpha\mathbf v_1,\ldots,\alpha\mathbf v_k)
=
\alpha^kT(\mathbf v_1,\ldots,\mathbf v_k)
\]

이다.

## 핵심 개념 2. tensor는 multilinear 구조와 변환 법칙을 가진다

한 벡터공간 $V$에서 실수값을 내는 covariant order-$k$ tensor를

\[
\mathcal T:V^k\to\mathbb R
\]

인 multilinear map으로 정의할 수 있다. 이 정의에서

- order 0 tensor는 scalar다.
- covariant order 1 tensor는 covector다.
- covariant order 2 tensor는 bilinear form이다.

벡터는 contravariant order 1 tensor로 분류한다. 더 일반적인 tensor는 vector 자리와 covector 자리를 함께 가질 수 있다. 이 단원에서는 covariant tensor와 좌표 배열을 중심으로 다룬다.

tensor 객체는 기저와 무관하다. 기저를 바꾸면 성분 배열이 정해진 법칙에 따라 변하고, tensor를 벡터들에 적용한 scalar는 유지된다.

## 핵심 개념 3. 기저는 tensor를 다축 성분 배열로 바꾼다

$V$의 기저를 $\mathcal B=(\mathbf b_1,\ldots,\mathbf b_n)$라 하자. order-$k$ covariant tensor의 성분은

\[
T_{i_1\ldots i_k}
=
\mathcal T(
\mathbf b_{i_1},\ldots,\mathbf b_{i_k}
)
\]

이다. 각 입력벡터를

\[
\mathbf v_r
=
\sum_{i_r=1}^{n}v_r^{i_r}\mathbf b_{i_r}
\]

로 쓰면 multilinearity에 따라

\[
\mathcal T(\mathbf v_1,\ldots,\mathbf v_k)
=
\sum_{i_1=1}^{n}\cdots\sum_{i_k=1}^{n}
T_{i_1\ldots i_k}
v_1^{i_1}\cdots v_k^{i_k}
\]

이다.

order 2에서는

\[
\mathcal T(\mathbf x,\mathbf y)
=
\sum_{i=1}^{n}\sum_{j=1}^{n}
T_{ij}x^iy^j
=
\mathbf x^\top\mathbf T\mathbf y
\]

가 되어 bilinear form의 행렬식을 얻는다.

## 핵심 개념 4. 각 tensor 인덱스는 기저변환에 참여한다

covector 성분은 vector 좌표의 역변환을 따른다. covariant tensor는 covector 자리를 여러 개 가지므로 각 인덱스가 그 변환을 하나씩 받는다.

order 2 bilinear form에서는 M03-08의

\[
\mathbf T_{\mathcal C}
=
\mathbf P_{\mathcal B\leftarrow\mathcal C}^\top
\mathbf T_{\mathcal B}
\mathbf P_{\mathcal B\leftarrow\mathcal C}
\]

가 그 법칙이다. order 3 tensor는 세 입력 좌표를 바꾸므로 세 개의 변환 인자가 성분에 작용한다.

배열이 tensor 성분을 나타내려면 기저가 바뀔 때 이 변환 법칙을 따라야 한다. 저장된 숫자 배열 하나만으로는 어떤 인덱스가 vector형인지 covector형인지 알 수 없다. 축의 수학적 의미를 함께 정의해야 한다.

## 핵심 개념 5. tensor product는 입력 자리를 결합한다

두 covector $\alpha\in V^*$와 $\beta\in W^*$의 tensor product는

\[
\alpha\otimes\beta:V\times W\to\mathbb R
\]

이고

\[
(\alpha\otimes\beta)(\mathbf x,\mathbf y)
=
\alpha(\mathbf x)\beta(\mathbf y)
\]

로 정의한다. 각 입력에 대해 선형이므로 order-2 tensor다.

$\dim V=m$, $\dim W=n$이고 각 공간에 기저를 골랐다고 하자. $\alpha,\beta$의 좌표 열을 각각 $\mathbf a,\mathbf b$라 하면 성분 행렬은

\[
\mathbf a\mathbf b^\top
\]

이다. 이를 outer product라고 한다. shape은

\[
\underbrace{\mathbf a}_{m\times1}
\underbrace{\mathbf b^\top}_{1\times n}
\in\mathbb R^{m\times n}
\]

이다.

여러 tensor의 합은 일반적인 order-2 tensor를 만든다. 한 outer product로 표현된다는 조건은 order가 2라는 조건과 다르다.

## 핵심 개념 6. contraction은 입력을 넣고 인덱스를 합한다

order-3 tensor 성분 $T_{ijk}$에 벡터 $\mathbf z$를 셋째 입력으로 넣으면

\[
S_{ij}
=
\sum_{k}T_{ijk}z^k
\]

를 얻는다. 결과는 두 입력이 남은 order-2 tensor다. 이 연산은 셋째 인덱스에 대한 contraction이다.

모든 입력을 넣으면

\[
\mathcal T(\mathbf x,\mathbf y,\mathbf z)
=
\sum_i\sum_j\sum_k
T_{ijk}x^iy^jz^k
\]

인 scalar를 얻는다.

행렬-벡터 곱

\[
y_i=\sum_jA_{ij}x_j
\]

도 공유 인덱스 $j$를 합하는 contraction으로 읽을 수 있다. 구현에서는 einsum 같은 표기가 어떤 축을 합하고 어떤 축을 남기는지 명시한다.

## 핵심 개념 7. order, shape와 rank는 다른 정보다

다음 용어를 구분해야 한다.

| 용어 | 답하는 질문 | 예 |
|---|---|---|
| tensor order | multilinear 입력 자리가 몇 개인가? | $T_{ijk}$는 order 3 |
| 배열의 축 수 | 저장 배열에 인덱스가 몇 개인가? | shape $2\times3\times4$는 축 3개 |
| 각 축의 dimension | 각 인덱스가 몇 값을 갖는가? | 2, 3, 4 |
| 행렬 rank | 독립인 행·열 방향이 몇 개인가? | order-2 배열에서 계산 |
| tensor rank | rank-1 tensor 합이 몇 개 필요한가? | 정의와 계산법을 따로 명시 |

행렬은 order-2 배열이지만 행렬 rank가 2라는 뜻은 아니다. order-3 tensor의 rank도 축 수 3과 같지 않다.

## 핵심 개념 8. 머신러닝 tensor는 축 의미를 가진 다축 배열이다

신경망 구현은 scalar, vector와 matrix를 포함한 다축 배열을 tensor라고 부른다. 예를 들어 Transformer activation은

\[
\mathbf H^{(\ell)}
\in
\mathbb R^{B\times T\times d_{\mathrm{model}}}
\]

로 저장할 수 있다.

- 첫 축은 batch다.
- 둘째 축은 token 위치다.
- 셋째 축은 feature 좌표다.

세 축만으로 이 배열을 수학적 의미의 covariant order-3 tensor라고 결론 내릴 수 없다. batch와 token 축은 표본을 나열하는 인덱스일 수 있고, feature 축만 기저변환의 대상일 수 있다.

배열 연산을 읽을 때는 shape과 축 의미를 먼저 확인한다. 좌표 독립적인 주장을 하려면 어떤 축에 어떤 기저변환이 작용하는지도 밝혀야 한다.

## 예제 1. order-3 tensor 평가하기

### 문제

$V=\mathbb R^2$에서 trilinear form을

\[
\mathcal T(\mathbf u,\mathbf v,\mathbf w)
=
u_1v_1w_1+2u_2v_1w_2
\]

로 정의한다.

\[
\mathbf u=
\begin{bmatrix}1\\2\end{bmatrix},
\quad
\mathbf v=
\begin{bmatrix}3\\-1\end{bmatrix},
\quad
\mathbf w=
\begin{bmatrix}4\\5\end{bmatrix}
\]

일 때 값을 계산하라.

### 풀이

정의에 좌표를 대입하면

\[
\mathcal T(\mathbf u,\mathbf v,\mathbf w)
=
1\cdot3\cdot4
+
2\cdot2\cdot3\cdot5
\]

\[
=
12+60
=
72
\]

다.

0이 아닌 성분은

\[
T_{111}=1,
\qquad
T_{212}=2
\]

뿐이다.

### 결과의 의미

성분 배열은 $2\times2\times2$ shape이지만 두 성분만 값이 있다. 세 입력 중 하나를 고정하면 남은 입력에 대해 bilinear map을 얻는다.

## 예제 2. tensor product와 outer product

### 문제

표준기저에서 두 covector의 좌표가

\[
\mathbf a=
\begin{bmatrix}1\\2\end{bmatrix},
\qquad
\mathbf b=
\begin{bmatrix}3\\-1\end{bmatrix}
\]

라고 하자. $\alpha\otimes\beta$의 성분 행렬을 구하고

\[
\mathbf x=
\begin{bmatrix}1\\1\end{bmatrix},
\qquad
\mathbf y=
\begin{bmatrix}2\\-1\end{bmatrix}
\]

에서 값을 계산하라.

### 풀이

성분 행렬은 outer product

\[
\mathbf a\mathbf b^\top
=
\begin{bmatrix}
1\\2
\end{bmatrix}
\begin{bmatrix}
3&-1
\end{bmatrix}
=
\begin{bmatrix}
3&-1\\
6&-2
\end{bmatrix}
\]

이다.

\[
\alpha(\mathbf x)
=
\begin{bmatrix}1&2\end{bmatrix}
\begin{bmatrix}1\\1\end{bmatrix}
=
3
\]

이고

\[
\beta(\mathbf y)
=
\begin{bmatrix}3&-1\end{bmatrix}
\begin{bmatrix}2\\-1\end{bmatrix}
=
7
\]

이므로

\[
(\alpha\otimes\beta)(\mathbf x,\mathbf y)
=
3\cdot7
=
21
\]

이다. 행렬로도

\[
\mathbf x^\top
\begin{bmatrix}
3&-1\\
6&-2
\end{bmatrix}
\mathbf y
=
21
\]

을 얻는다.

### 결과의 의미

tensor product는 두 개의 선형 측정을 곱해 두 입력을 받는 bilinear form을 만든다.

## 예제 3. 한 인덱스를 contraction하기

예제 1의 tensor에서 $\mathbf w=(4,5)^\top$을 셋째 입력에 넣자.

\[
S_{ij}
=
\sum_{k=1}^{2}T_{ijk}w^k
\]

이다. 0이 아닌 성분을 사용하면

\[
S_{11}=T_{111}w^1=4
\]

\[
S_{21}=T_{212}w^2=10
\]

이고 나머지는 0이다. 따라서

\[
\mathbf S=
\begin{bmatrix}
4&0\\
10&0
\end{bmatrix}
\]

이다. 남은 두 입력에서

\[
\mathbf u^\top\mathbf S\mathbf v
=
\begin{bmatrix}1&2\end{bmatrix}
\begin{bmatrix}
4&0\\
10&0
\end{bmatrix}
\begin{bmatrix}3\\-1\end{bmatrix}
=
72
\]

로 전체 평가값을 다시 얻는다.

## 예제 4. attention의 두 contraction

batch와 head를 생략하고

\[
\mathbf Q,\mathbf K\in\mathbb R^{T\times d_k},
\qquad
\mathbf V\in\mathbb R^{T\times d_v}
\]

라 하자. score 행렬의 성분은

\[
S_{ts}
=
\sum_{i=1}^{d_k}Q_{ti}K_{si}
\]

이다. feature 인덱스 $i$를 contraction해 $\mathbf S\in\mathbb R^{T\times T}$를 만든다.

attention weight $\mathbf A\in\mathbb R^{T\times T}$가 주어지면 출력 성분은

\[
O_{tj}
=
\sum_{s=1}^{T}A_{ts}V_{sj}
\]

이다. token 인덱스 $s$를 contraction해

\[
\mathbf O\in\mathbb R^{T\times d_v}
\]

를 얻는다. 두 식에서 합을 취한 축과 결과에 남은 축을 구분하면 행렬곱의 shape을 확인할 수 있다.

## 흔한 오해

### 오해 1. 축이 세 개인 배열은 수학적으로 모두 같은 종류의 order-3 tensor다

배열 shape은 저장 구조를 나타낸다. 수학적 tensor의 타입을 정하려면 각 축이 어떤 공간에 속하고 기저변환에서 성분이 어떻게 변하는지 정의해야 한다.

### 오해 2. tensor order와 tensor rank는 같다

order는 입력 자리나 인덱스의 수다. tensor rank는 rank-1 tensor들의 합으로 표현하는 문제이며 별도의 정의다.

### 오해 3. multilinear map은 모든 입력을 묶어 선형이다

multilinearity는 다른 입력을 고정했을 때 한 입력씩 선형이라는 조건이다. 모든 입력을 같은 scalar로 늘리면 order $k$만큼 거듭제곱된 배율이 나온다.

### 오해 4. contraction은 배열 원소를 임의로 더하는 연산이다

contraction은 대응하는 공간의 인덱스를 짝지어 합한다. 어떤 축을 합하는지와 어떤 축이 남는지 지정해야 한다.

### 오해 5. 같은 shape의 activation tensor는 같은 표현이다

shape은 축의 크기만 알려 준다. 원소값, feature 기저, 표본 대응과 모델의 기능적 사용은 별도 정보다.

## 연습문제

### 1. multilinearity 판정

\[
T(\mathbf u,\mathbf v,\mathbf w)=u_1v_2w_1
\]

가 $\mathbb R^2$의 세 입력에 대해 multilinear인지 판정하라.

<details>
<summary>해설 보기</summary>

나머지 두 입력을 고정하면 각 입력에서 한 좌표에 고정된 scalar를 곱하는 함수가 된다. 각 입력의 덧셈과 스칼라곱을 보존하므로 trilinear다.

</details>

### 2. trilinear 값 계산

\[
T(\mathbf u,\mathbf v,\mathbf w)=u_1v_1w_2+u_2v_2w_1
\]

이고

\[
\mathbf u=
\begin{bmatrix}1\\2\end{bmatrix},
\quad
\mathbf v=
\begin{bmatrix}3\\4\end{bmatrix},
\quad
\mathbf w=
\begin{bmatrix}5\\6\end{bmatrix}
\]

일 때 $T(\mathbf u,\mathbf v,\mathbf w)$를 구하라.

<details>
<summary>해설 보기</summary>

\[
T(\mathbf u,\mathbf v,\mathbf w)
=
1\cdot3\cdot6+2\cdot4\cdot5
=
18+40
=
58
\]

이다.

</details>

### 3. order와 성분 수

$T_{ijk}$의 각 인덱스 범위가 각각 2, 3, 4일 때 배열 shape, order와 전체 성분 수를 구하라.

<details>
<summary>해설 보기</summary>

shape은 $2\times3\times4$이고 인덱스가 세 개이므로 order는 3이다. 전체 성분 수는

\[
2\cdot3\cdot4=24
\]

개다. order 3이라는 말은 성분 수가 3이거나 tensor rank가 3이라는 뜻이 아니다.

</details>

### 4. outer product

\[
\mathbf a=
\begin{bmatrix}2\\-1\end{bmatrix},
\qquad
\mathbf b=
\begin{bmatrix}3\\0\\4\end{bmatrix}
\]

일 때 $\mathbf a\mathbf b^\top$의 shape과 원소를 구하라.

<details>
<summary>해설 보기</summary>

shape은 $(2\times1)(1\times3)=2\times3$이다.

\[
\mathbf a\mathbf b^\top
=
\begin{bmatrix}
2\\-1
\end{bmatrix}
\begin{bmatrix}
3&0&4
\end{bmatrix}
=
\begin{bmatrix}
6&0&8\\
-3&0&-4
\end{bmatrix}
\]

이다.

</details>

### 5. contraction shape

$T_{ijk}$의 shape이 $2\times3\times4$이고 $\mathbf z\in\mathbb R^4$일 때

\[
S_{ij}=\sum_{k=1}^{4}T_{ijk}z_k
\]

의 shape과 order를 구하라.

<details>
<summary>해설 보기</summary>

$k$ 인덱스를 합으로 없애고 $i,j$를 남긴다. 따라서 $\mathbf S$의 shape은 $2\times3$이고 order는 2다.

</details>

### 6. attention shape 추적

\[
\mathbf Q,\mathbf K\in\mathbb R^{5\times3},
\qquad
\mathbf V\in\mathbb R^{5\times4}
\]

일 때 $\mathbf Q\mathbf K^\top$과 $\mathbf A\mathbf V$의 shape을 구하라. $\mathbf A$는 score에 softmax를 적용한 행렬이다.

<details>
<summary>해설 보기</summary>

\[
(5\times3)(3\times5)=5\times5
\]

이므로 $\mathbf Q\mathbf K^\top$의 shape은 $5\times5$다. 따라서 $\mathbf A\in\mathbb R^{5\times5}$이고

\[
(5\times5)(5\times4)=5\times4
\]

이므로 $\mathbf A\mathbf V$의 shape은 $5\times4$다.

</details>

### 7. 모델 주장 비판

“두 모델의 activation tensor shape이 모두 $B\times T\times d$이므로 두 모델은 같은 tensor 표현을 학습했다”는 문장을 비판하라.

<details>
<summary>해설 보기</summary>

같은 shape은 batch, token과 feature 축의 크기가 같다는 사실만 보인다. activation 값과 표본 대응, feature 기저, 허용 가능한 정렬, 정보 복원과 모델의 기능적 사용은 확인하지 못한다. 표현의 동일성을 주장하려면 비교 기준과 변환 불변성을 따로 정해야 한다.

</details>

## 단원 요약

- multilinear map은 각 입력 자리에 대해 따로 선형이다.
- covariant order-$k$ tensor는 $k$개의 벡터를 scalar로 보내는 multilinear map으로 볼 수 있다.
- 기저를 고르면 tensor는 다축 성분 배열로 나타나고 각 인덱스가 기저변환에 참여한다.
- tensor product는 입력 자리를 결합하고 contraction은 인덱스를 합해 order를 줄인다.
- tensor order, 배열 shape와 행렬·tensor rank는 서로 다른 정보다.
- 머신러닝 tensor를 해석할 때는 각 축의 의미와 contraction 축을 명시해야 한다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- multilinear map의 각 입력별 선형성을 설명할 수 있는가?
- covector와 bilinear form을 tensor order와 연결할 수 있는가?
- tensor 성분으로 작은 multilinear 값을 계산할 수 있는가?
- tensor product와 contraction의 결과 shape을 구할 수 있는가?
- tensor order, 배열 축 수와 rank를 구분할 수 있는가?
- attention 식에서 합하는 축과 남는 축을 찾을 수 있는가?
- 배열 shape만으로 표현 동일성을 결론 낼 수 없는 이유를 설명할 수 있는가?

## 다음 단원

- [M03-10 total derivative와 differential](M03-10-total-derivative-differential.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] multilinearity를 각 입력별로 정의했다.
- [x] tensor 객체와 성분 배열을 구분했다.
- [x] tensor order, shape와 rank를 구분했다.
- [x] tensor product와 contraction을 계산했다.
- [x] 신경망 배열 축과 수학적 tensor 타입을 구분했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 내부 링크와 수식 구분자를 확인했다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
