---
id: "M02-10"
title: "determinant의 최소 이해"
part: 1
stage: "M02"
status: "완료"
prerequisites:
  - "M02-05"
  - "M02-06"
  - "M02-08"
estimated_time: "90~115분"
---

# M02-10. determinant의 최소 이해

## 이 단원이 필요한 이유

determinant는 정사각행렬이 부피를 몇 배로 바꾸는지 나타내는 scalar다. 값이 0이면 어떤 dimension이 납작해져 역변환을 만들 수 없다. 값의 부호는 공간의 방향 순서가 뒤집혔는지를 기록한다.

모델 해석에서 determinant를 자주 직접 계산하지는 않는다. 가역성, 고유값의 특성방정식과 Jacobian의 국소 부피 변화를 읽으려면 뜻을 알아야 한다. 큰 행렬에서 determinant 하나만으로 수치 안정성이나 모델 중요도를 판단해서는 안 된다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- $2\times2$ determinant를 계산할 수 있다.
- determinant의 절댓값을 면적 또는 부피 배율로 설명할 수 있다.
- determinant의 부호와 방향 순서의 반전을 연결할 수 있다.
- determinant가 0인 경우와 가역성, rank를 연결할 수 있다.
- 곱, 역행렬과 행 기본변환에서 determinant가 어떻게 변하는지 계산할 수 있다.
- determinant의 크기만으로 수치 안정성이나 모델 기능을 단정할 수 없는 이유를 설명할 수 있다.

## 선수지식 확인

- 선수 단원: [M02-05 행렬을 선형변환으로 보기](M02-05-matrix-as-linear-transformation.md)
- 선수 단원: [M02-06 연립방정식과 역행렬](M02-06-linear-systems-inverse.md)
- 선수 단원: [M02-08 kernel, image와 rank](M02-08-kernel-image-rank.md)
- 확인 질문: 가역행렬, 특이행렬과 full rank 정사각행렬의 관계를 설명할 수 있는가?
- 확인 질문: 행렬의 열벡터가 만드는 평행사변형을 그릴 수 있는가?

가역성이나 rank가 불분명하면 선수 단원을 먼저 복습한다.

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | 조건 |
|---|---|---|---|
| $\det(\mathbf A)$ | `the determinant of A` | 정사각행렬의 방향 있는 부피 배율 | scalar |
| $|\det(\mathbf A)|$ | `the absolute value of the determinant of A` | 부호를 제외한 부피 배율 | 0 이상 |
| 방향 순서 | `orientation` | 기저의 축 순서가 오른손·왼손 방식 중 어느 쪽인지 나타내는 성질 | determinant 부호와 연결 |
| 삼각행렬 | `triangular matrix` | 대각선 한쪽이 모두 0인 정사각행렬 | determinant는 대각 원소의 곱 |

## 핵심 개념 1. $2\times2$ determinant는 교차곱의 차다

\[
\mathbf A=
\begin{bmatrix}
a&b\\
c&d
\end{bmatrix}
\]

이면

\[
\det(\mathbf A)
=
ad-bc
\]

이다.

이 값은 $\mathbf A$의 두 열벡터가 만드는 평행사변형의 방향 있는 면적이다. 실제 면적은

\[
|\det(\mathbf A)|
\]

이다.

## 핵심 개념 2. determinant의 절댓값은 부피 배율이다

정사각행렬 $\mathbf A\in\mathbb R^{n\times n}$이 단위 정육면체를 변환하면 평행다포체가 된다. 변환 뒤 $n$차원 부피는 원래 부피의

\[
|\det(\mathbf A)|
\]

배다.

- $|\det(\mathbf A)|>1$이면 부피가 늘어난다.
- $0<|\det(\mathbf A)|<1$이면 부피가 줄어든다.
- $\det(\mathbf A)=0$이면 부피가 0이 되어 낮은 차원으로 납작해진다.

determinant는 전체 부피 배율 하나를 요약한다. 각 방향이 얼마나 늘거나 줄었는지는 따로 보여 주지 않는다.

## 핵심 개념 3. 부호는 방향 순서의 반전을 기록한다

$\det(\mathbf A)>0$이면 변환이 기저의 방향 순서를 보존하고, $\det(\mathbf A)<0$이면 방향 순서를 뒤집는다.

예를 들어 $x$축 반사행렬

\[
\mathbf R=
\begin{bmatrix}
1&0\\
0&-1
\end{bmatrix}
\]

은

\[
\det(\mathbf R)=-1
\]

이다. 면적은 유지하지만 방향 순서를 한 번 뒤집는다.

$90^\circ$ 회전행렬은 determinant가 1이다. 면적과 방향 순서를 모두 보존한다.

## 핵심 개념 4. determinant 0은 가역성 상실을 뜻한다

정사각행렬 $\mathbf A\in\mathbb R^{n\times n}$에 대해 다음 조건들은 서로 동치다.

\[
\det(\mathbf A)\ne0
\]

\[
\mathbf A\text{가 가역이다}
\]

\[
\operatorname{rank}(\mathbf A)=n
\]

\[
\ker(\mathbf A)=\{\mathbf 0\}
\]

determinant가 0이면 열벡터들이 선형종속이고 단위 정육면체의 부피가 0이 된다. 어떤 입력 방향이 다른 방향과 겹치거나 영벡터로 사라진다.

## 핵심 개념 5. 합성변환의 부피 배율은 곱해진다

같은 크기의 정사각행렬에 대해

\[
\det(\mathbf A\mathbf B)
=
\det(\mathbf A)\det(\mathbf B)
\]

이다. $\mathbf B$가 부피를 $\det(\mathbf B)$배 바꾸고 $\mathbf A$가 다시 $\det(\mathbf A)$배 바꾸므로 전체 배율은 곱이다.

$\mathbf A$가 가역이면

\[
\det(\mathbf A^{-1})
=
\frac{1}{\det(\mathbf A)}
\]

이다. 실제로

\[
1
=
\det(\mathbf I)
=
\det(\mathbf A\mathbf A^{-1})
=
\det(\mathbf A)\det(\mathbf A^{-1})
\]

이다.

## 핵심 개념 6. 행 기본변환의 효과를 추적할 수 있다

정사각행렬의 행에 기본변환을 적용하면 determinant는 다음과 같이 변한다.

1. 두 행을 맞바꾸면 부호가 바뀐다.
2. 한 행에 0이 아닌 scalar $c$를 곱하면 determinant도 $c$배 된다.
3. 한 행에 다른 행의 scalar배를 더하면 determinant는 바뀌지 않는다.

이 규칙으로 행렬을 삼각행렬로 바꾸면 determinant를 계산할 수 있다. 삼각행렬에서는

\[
\det(\mathbf U)
=
\prod_{i=1}^{n}u_{ii}
\]

이다. 소거 과정에서 수행한 행 교환과 배율을 함께 기록해야 한다.

## 핵심 개념 7. determinant 하나는 방향별 민감도를 보여 주지 않는다

\[
\mathbf A=
\begin{bmatrix}
1000&0\\
0&0.001
\end{bmatrix}
\]

이면

\[
\det(\mathbf A)=1
\]

이다. 면적은 유지되지만 첫 방향은 1000배 늘고 둘째 방향은 1000분의 1로 줄어든다. 역변환은 둘째 출력 방향의 작은 오차를 크게 확대할 수 있다.

따라서 $|\det(\mathbf A)|$가 1에 가깝다는 사실은 수치 안정성을 보장하지 않는다. 방향별 증폭은 singular value와 condition number로 조사하며 M02-13과 M02-15에서 다룬다.

## 예제 1. 면적 배율 계산

\[
\mathbf A=
\begin{bmatrix}
3&1\\
0&2
\end{bmatrix}
\]

이면

\[
\det(\mathbf A)
=
3\cdot2-1\cdot0
=
6
\]

이다. 단위 정사각형은 면적 6인 평행사변형으로 간다. 부호가 양수이므로 방향 순서도 보존된다.

## 예제 2. 납작해지는 변환

\[
\mathbf B=
\begin{bmatrix}
1&2\\
2&4
\end{bmatrix}
\]

이면

\[
\det(\mathbf B)
=
1\cdot4-2\cdot2
=
0
\]

이다. 두 번째 열이 첫 번째 열의 2배이므로 두 독립 방향이 한 직선으로 겹친다. rank는 1이고 역행렬은 없다.

## 예제 3. 합성변환의 determinant

\[
\mathbf A=
\begin{bmatrix}
2&0\\
0&3
\end{bmatrix},
\qquad
\mathbf R=
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}
\]

이면

\[
\det(\mathbf A)=6,
\qquad
\det(\mathbf R)=1
\]

이다. 따라서

\[
\det(\mathbf A\mathbf R)=6
\]

이다. 회전이 면적을 보존한 뒤 두 축 확대가 면적을 6배로 만든다.

## 예제 4. Jacobian determinant 미리보기

비선형함수 $f:\mathbb R^n\to\mathbb R^n$도 한 점 근처에서는 Jacobian $\mathbf J_f(\mathbf x)$로 선형근사할 수 있다. 이때

\[
|\det(\mathbf J_f(\mathbf x))|
\]

는 그 점 근처의 작은 부피가 얼마나 변하는지 나타낸다.

이는 국소 부피 변화에 관한 값이다. 함수가 특정 개념을 학습했는지, 어떤 좌표가 행동의 원인인지와는 다른 주장이다. Jacobian은 M03-11에서 계산한다.

## 흔한 오해

### 오해 1. determinant는 모든 행렬에 정의된다

이 단원에서 determinant는 정사각행렬에만 정의한다. 직사각행렬의 크기 변화는 singular value로 분석한다.

### 오해 2. determinant가 음수이면 부피가 음수다

기하학적 부피는 $|\det(\mathbf A)|$로 계산한다. 음수 부호는 방향 순서가 뒤집혔음을 나타낸다.

### 오해 3. determinant가 작으면 rank가 낮다

정확히 0일 때만 rank가 부족하다고 결론 낼 수 있다. 0이 아닌 작은 값은 가역이지만 특정 방향에서 큰 민감도를 가질 수 있다.

### 오해 4. determinant 절댓값이 크면 모델에서 더 중요한 행렬이다

determinant는 전체 부피 배율이다. 모델 성능, feature 의미와 인과적 기여는 이 scalar 하나로 결정되지 않는다.

## 연습문제

### 1. $2\times2$ 계산

\[
\mathbf A=
\begin{bmatrix}
4&-1\\
2&3
\end{bmatrix}
\]

의 determinant를 구하라.

<details>
<summary>해설 보기</summary>

\[
\det(\mathbf A)
=
4\cdot3-(-1)\cdot2
=
14
\]

이다.

</details>

### 2. 면적과 방향 순서

$\det(\mathbf B)=-5$인 $2\times2$ 행렬이 면적 3인 도형에 작용했다. 변환 뒤 면적과 방향 순서의 변화를 설명하라.

<details>
<summary>해설 보기</summary>

면적은 determinant 절댓값만큼 변하므로

\[
3\cdot|-5|=15
\]

다. determinant가 음수이므로 방향 순서는 뒤집힌다.

</details>

### 3. 가역성 판정

\[
\mathbf C=
\begin{bmatrix}
2&6\\
1&3
\end{bmatrix}
\]

가 가역인지 determinant로 판단하고 rank를 구하라.

<details>
<summary>해설 보기</summary>

\[
\det(\mathbf C)
=
2\cdot3-6\cdot1
=
0
\]

이다. 따라서 가역이 아니다. 두 번째 열이 첫 번째 열의 3배이므로 rank는 1이다.

</details>

### 4. 삼각행렬

\[
\mathbf U=
\begin{bmatrix}
2&1&4\\
0&-3&5\\
0&0&6
\end{bmatrix}
\]

의 determinant를 구하라.

<details>
<summary>해설 보기</summary>

삼각행렬의 determinant는 대각 원소의 곱이다.

\[
\det(\mathbf U)
=
2(-3)6
=
-36
\]

이다.

</details>

### 5. 행 기본변환

$\det(\mathbf A)=7$이라고 하자. 다음 연산 뒤 determinant를 각각 구하라.

1. 첫째 행과 둘째 행을 맞바꾼다.
2. 첫째 행에 4를 곱한다.
3. 둘째 행에 첫째 행의 3배를 더한다.

각 연산은 원래 $\mathbf A$에 따로 적용한다.

<details>
<summary>해설 보기</summary>

행 교환은 부호를 바꾸므로 $-7$이다. 한 행에 4를 곱하면 determinant도 4배가 되어 $28$이다. 다른 행의 배수를 더하는 연산은 determinant를 바꾸지 않으므로 $7$이다.

</details>

### 6. 역행렬의 determinant

$\det(\mathbf A)=\frac14$인 가역행렬에 대해 $\det(\mathbf A^{-1})$를 구하라.

<details>
<summary>해설 보기</summary>

\[
\det(\mathbf A^{-1})
=
\frac{1}{\det(\mathbf A)}
=
4
\]

이다. 원래 변환이 바꾼 부피 배율을 역변환이 되돌린다.

</details>

### 7. 안정성 주장 비판

\[
\mathbf D=
\begin{bmatrix}
10^6&0\\
0&10^{-6}
\end{bmatrix}
\]

에 대해 determinant를 구하고, 그 값만으로 수치적으로 안정하다고 결론 낼 수 있는지 판단하라.

<details>
<summary>해설 보기</summary>

\[
\det(\mathbf D)
=
10^6\cdot10^{-6}
=
1
\]

이다. 전체 면적은 유지된다.

첫 방향은 $10^6$배 확대되고 둘째 방향은 $10^{-6}$배 축소된다. 방향별 배율 차이가 크므로 determinant 1만으로 안정성을 결론 낼 수 없다. singular value와 condition number를 확인해야 한다.

</details>

## 단원 요약

- $2\times2$ determinant는 $ad-bc$이며 정사각행렬의 방향 있는 부피 배율이다.
- 절댓값은 부피 배율이고 부호는 방향 순서의 보존 또는 반전을 나타낸다.
- determinant가 0인 정사각행렬은 rank가 부족하고 역행렬이 없다.
- 합성변환의 determinant는 각 determinant의 곱이다.
- 행 기본변환과 삼각행렬 성질을 이용해 determinant를 계산할 수 있다.
- determinant 하나는 방향별 증폭과 수치 안정성, 모델의 기능적 중요도를 보여 주지 않는다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- $2\times2$ determinant를 계산할 수 있는가?
- determinant의 절댓값과 부호를 기하적으로 설명할 수 있는가?
- determinant 0과 가역성·rank를 연결할 수 있는가?
- 곱과 역행렬의 determinant를 계산할 수 있는가?
- 행 기본변환이 determinant에 미치는 영향을 설명할 수 있는가?
- determinant가 안정성 지표로 부족한 이유를 예로 설명할 수 있는가?

## 다음 단원

- [M02-11 고유값과 고유벡터](M02-11-eigenvalues-eigenvectors.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] $2\times2$ 공식과 부피 배율을 연결했다.
- [x] 부호, 가역성, rank와 kernel의 관계를 설명했다.
- [x] 곱과 행 기본변환 성질을 포함했다.
- [x] 방향별 증폭이 숨는 반례를 제시했다.
- [x] 모든 문제에 해설이 있다.
- [x] determinant와 모델 기능 주장을 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 내부 링크와 수식 구분자를 확인했다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
