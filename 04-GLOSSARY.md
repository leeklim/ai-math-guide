# 용어집

이 문서는 프로젝트 전체에서 사용하는 표준 용어를 기록한다. 새 용어를 정의할 때 기존 항목과 충돌하지 않는지 확인한다.

## 사용 규칙

- 본문 첫 등장에서는 `한국어(영어)`로 쓴다.
- 이후에는 `권장 표기`를 사용한다.
- 같은 개념을 문맥 없이 동의어로 교체하지 않는다.
- 정의는 해당 개념의 입문 단원에서 더 자세히 설명한다.

## 기본 수학

| 권장 표기 | 영어 | 피하거나 구분할 표현 | 짧은 뜻 | 최초 단원 |
|---|---|---|---|---|
| 수 | number | 숫자 기호와 구분 | 셈, 순서와 크기 등을 표현하는 수학적 대상 | M00-01 |
| 값 | value | 기호와 구분 | 수나 수학적 대상이 현재 나타내는 내용 | M00-01 |
| 기호 | symbol | 값과 구분 | 수학적 대상을 표시하는 표식 | M00-01 |
| 절댓값 | absolute value | 부호 있는 값과 구분 | 실수의 부호를 제외한 0으로부터의 거리 | M01-03 |
| 변수 | variable | 미지수와 항상 같지 않음 | 값이 달라질 수 있는 기호 | M00-01 |
| 상수 | constant | 고정값 | 문맥 안에서 값이 변하지 않는 대상 | M00-01 |
| 파라미터 | parameter | 모든 문맥에서 상수인 것은 아님 | 모델이 학습을 통해 조정하는 값 | M00-01 |
| 하이퍼파라미터 | hyperparameter | 파라미터와 구분 | 학습 절차 밖에서 정하거나 탐색하는 설정값 | M00-01 |
| 입력 | input | 파라미터와 구분 | 모델이나 함수에 주는 데이터 | M00-01 |
| 출력 | output | 입력과 구분 | 모델이나 함수가 계산해 내놓는 결과 | M00-01 |
| 식 | expression | 방정식과 구분 | 수와 연산을 조합한 표현 | M00-02 |
| 등식 | equality | 방정식과 구분 | 두 표현이 같다는 명제 | M00-02 |
| 좌변 | left-hand side, LHS | 왼쪽 항 하나로 한정하지 않음 | 등호 왼쪽의 전체 표현 | M00-02 |
| 우변 | right-hand side, RHS | 오른쪽 항 하나로 한정하지 않음 | 등호 오른쪽의 전체 표현 | M00-02 |
| 방정식 | equation | 등식 전체와 구분 | 미지수의 값에 따라 참·거짓이 달라지는 등식 | M00-02 |
| 해 | solution | 계산 결과 전체와 구분 | 방정식이나 조건을 참으로 만드는 값 | M00-02 |
| 항등식 | identity | 특정 값에서만 성립하는 등식과 구분 | 허용된 모든 변수 값에서 성립하는 등식 | M00-02 |
| 함수 | function | 공식과 동일시하지 않음 | 입력에 출력을 대응시키는 규칙 | M00-03 |
| 함수값 | function value | 함수 자체와 구분 | 특정 입력에 함수를 적용해 얻은 출력 | M00-03 |
| 정의역 | domain | 입력 범위 | 함수가 입력으로 받는 대상의 집합 | M00-03 |
| 공역 | codomain | 치역과 구분 | 함수 출력이 속하도록 지정한 집합 | M00-03 |
| 치역 | image, range | 공역과 구분 | 실제로 나오는 출력들의 집합 | M00-03 |
| 좌표 | coordinate | 점 자체와 구분 | 기준축에 따라 점의 위치를 나타내는 값 | M00-04 |
| 순서쌍 | ordered pair | 순서를 바꿀 수 있는 집합과 구분 | 첫째 값과 둘째 값의 역할을 보존한 두 값의 묶음 | M00-04 |
| 좌표평면 | coordinate plane | 함수의 정의역과 구분 | 두 좌표축으로 점의 위치를 나타내는 평면 | M00-04 |
| 그래프 | graph | 그래프 자료구조와 문맥상 구분 | 함수의 입력과 출력을 좌표의 점으로 나타낸 대상 | M00-04 |
| 절편 | intercept | 기울기와 구분 | 그래프가 좌표축과 만나는 위치 | M00-04 |
| 지수 | exponent | 지수함수 전체와 구분 | 거듭제곱에서 밑의 반복 횟수를 확장한 값 | M00-05 |
| 밑 | base | 로그의 입력과 구분 | 거듭제곱과 로그의 기준이 되는 수 | M00-05 |
| 지수함수 | exponential function | 거듭제곱함수와 구분 | 입력이 지수에 놓이는 함수 $a^x$ | M00-05 |
| 로그 | logarithm | 자연로그로 한정되지 않음 | 밑을 몇 제곱해야 입력값이 되는지 나타내는 함수 | M00-05 |
| 자연로그 | natural logarithm | 밑 10인 상용로그와 구분 | 자연상수 $e$를 밑으로 한 로그 | M00-05 |
| 인덱스 | index | 값 자체와 구분 | 여러 대상의 위치나 역할을 구분하는 첨자 | M00-06 |
| 합 | summation | 단일 덧셈과 문맥상 구분 | 지정한 범위의 항들을 더하는 연산 | M00-06 |
| 곱 기호 | product notation | 곱의 미분법과 구분 | 지정한 범위의 항들을 곱하는 표기 | M01-07 |
| 더미 인덱스 | dummy index | 자유 인덱스와 구분 | 합 안에서만 변하며 이름을 바꿀 수 있는 인덱스 | M00-06 |
| 산술평균 | arithmetic mean | 중앙값과 구분 | 값들의 합을 개수로 나눈 값 | M00-06 |
| 가중합 | weighted sum | 산술평균과 구분 | 각 항에 가중치를 곱해 더한 값 | M00-06 |
| 집합 | set | 수열과 구분 | 구분 가능한 대상들을 원소로 모은 대상 | M00-07 |
| 원소 | element | 부분집합과 구분 | 집합에 속하는 개별 대상 | M00-07 |
| 부분집합 | subset | 원소 관계와 구분 | 한 집합의 원소가 모두 다른 집합에도 속하는 관계 | M00-07 |
| 공집합 | empty set | 공집합을 원소로 가진 집합과 구분 | 원소가 없는 집합 | M00-07 |
| 합집합 | union | 교집합과 구분 | 두 집합 중 하나 이상에 속하는 원소의 집합 | M00-07 |
| 교집합 | intersection | 합집합과 구분 | 두 집합 모두에 속하는 원소의 집합 | M00-07 |
| 명제 | proposition | 값이 정해지지 않은 조건과 구분 | 참·거짓을 판단할 수 있는 문장 | M00-07 |
| 함의 | implication | 인과관계와 동일시하지 않음 | 한 명제가 참일 때 다른 명제도 참인 논리 관계 | M00-07 |
| 필요조건 | necessary condition | 충분조건과 구분 | 결론이나 성질이 성립하려면 갖춰야 하는 조건 | M00-07 |
| 충분조건 | sufficient condition | 필요조건과 구분 | 만족하면 결론이나 성질을 보장하는 조건 | M00-07 |
| 반례 | counterexample | 단순한 다른 예와 구분 | 전칭명제를 거짓으로 만드는 사례 | M00-07 |
| 합성함수 | composition | 함수의 곱과 구분 | 한 함수의 출력을 다른 함수의 입력으로 넣음 | M00-08 |
| 항등함수 | identity function | 상수함수와 구분 | 입력을 그대로 출력하는 함수 | M00-08 |
| 역함수 | inverse function | 함수값의 역수와 구분 | 함수의 출력을 원래 입력으로 되돌리는 함수 | M00-08 |
| 일대일 함수 | injective function | 전사와 구분 | 서로 다른 입력을 서로 다른 출력으로 보내는 함수 | M00-08 |
| 전사 함수 | surjective function | 일대일과 구분 | 공역의 각 원소가 실제 출력으로 나오는 함수 | M00-08 |
| 전단사 함수 | bijective function | 일대일 또는 전사 하나만인 함수와 구분 | 일대일이면서 전사인 함수 | M00-08 |
| 스칼라 | scalar | 숫자 | 하나의 크기로 표현되는 값 | M00-09 |
| 벡터 | vector | 단순 목록과 동일시하지 않음 | 벡터공간의 원소 | M00-09 |
| 성분 | component | 벡터 전체와 구분 | 벡터를 좌표로 나타낼 때의 개별 값 | M02-01 |
| 영벡터 | zero vector | scalar 0과 구분 | 모든 성분이 0인 벡터 | M02-01 |
| 벡터 덧셈 | vector addition | scalar 덧셈과 문맥상 구분 | 같은 dimension의 벡터를 대응 성분끼리 더하는 연산 | M02-01 |
| 스칼라곱 | scalar multiplication | 두 벡터의 내적과 구분 | 벡터의 모든 성분에 같은 scalar를 곱하는 연산 | M02-01 |
| 덧셈 역원 | additive inverse | 역수와 구분 | 원래 벡터와 더하면 영벡터가 되는 벡터 | M02-01 |
| 행렬 | matrix | 표와 동일시하지 않음 | 선형사상의 좌표 표현 또는 수의 배열 | M00-09 |
| shape | shape | dimension과 문맥상 구분 | 배열이나 행렬의 각 축 크기를 순서대로 적은 것 | M00-09 |
| dimension | dimension | 벡터의 노름과 구분 | 벡터의 독립 좌표 또는 성분의 수 | M00-09 |
| 전치 | transpose | 역행렬과 구분 | 행과 열을 맞바꾸는 연산 | M00-09 |
| 내적 | inner product, dot product | 원소별 곱과 구분 | 같은 dimension의 두 벡터를 스칼라로 보내는 연산 | M00-09 |
| 노름 | norm | dimension과 구분 | 벡터의 크기를 나타내는 스칼라 | M00-09 |
| 아핀 층 | affine layer | 선형변환만 있는 층과 구분 | 가중치 행렬을 곱한 뒤 편향을 더하는 층 | M00-09 |
| 가중치 | weight | 가중합의 계수와 문맥상 연결 | 입력 성분이 출력에 반영되는 방식을 정하는 파라미터 | M00-09 |
| 편향 | bias | 통계적 편향과 문맥상 구분 | 선형변환 결과에 더하는 파라미터 | M00-09 |

## 미적분

| 권장 표기 | 영어 | 피하거나 구분할 표현 | 짧은 뜻 | 최초 단원 |
|---|---|---|---|---|
| 변화량 | change, increment | 끝값과 구분 | 끝값에서 시작값을 뺀 값 | M01-01 |
| 평균변화율 | average rate of change | 두 함수값의 평균과 구분 | 출력 변화량을 입력 변화량으로 나눈 비 | M01-01 |
| 기울기 | slope | 그래디언트와 문맥상 구분 | 좌표평면에서 세로 변화량을 가로 변화량으로 나눈 값 | M01-01 |
| 할선 | secant line | 접선과 구분 | 곡선 위의 서로 다른 두 점을 지나는 직선 | M01-01 |
| 극한 | limit | 함수값과 구분 | 입력이 한 값에 가까워질 때 출력이 가까워지는 값 | M01-02 |
| 좌극한 | left-hand limit | 우극한과 구분 | 입력이 작은 쪽에서 한 값에 가까워질 때의 극한 | M01-02 |
| 우극한 | right-hand limit | 좌극한과 구분 | 입력이 큰 쪽에서 한 값에 가까워질 때의 극한 | M01-02 |
| 연속 | continuity | 미분 가능성과 동일하지 않음 | 한 점에서 극한값과 함수값이 일치하는 성질 | M01-02 |
| 미분 | differentiation | 도함수와 문맥상 구분 | 국소 변화율을 구하는 과정 | M01-03 |
| 미분계수 | derivative at a point | 도함수 전체와 구분 | 한 점에서 평균변화율의 극한으로 얻는 순간변화율 | M01-03 |
| 도함수 | derivative | 미분과 문맥상 구분 | 각 점의 변화율을 주는 함수 | M01-03 |
| 접선 | tangent line | 할선과 구분 | 한 점에서 곡선의 국소 방향을 나타내는 직선 | M01-03 |
| 미분 가능 | differentiable | 연속과 동일하지 않음 | 함수 변화가 선형근사와 입력 변화보다 작은 상대오차를 갖는 성질 | M01-03 |
| 임계점 | critical point | 극값과 동일하지 않음 | 도함수가 0이거나 존재하지 않는 정의역의 점 | M01-04 |
| 정지점 | stationary point | 임계점 전체와 구분 | 도함수가 0인 점 | M01-04 |
| 국소 최댓값 | local maximum | 전역 최댓값과 구분 | 한 점 주변에서 가장 큰 함수값 | M01-04 |
| 국소 최솟값 | local minimum | 전역 최솟값과 구분 | 한 점 주변에서 가장 작은 함수값 | M01-04 |
| 합의 미분법 | sum rule | 곱의 미분법과 구분 | 함수 합을 항별로 미분하는 규칙 | M01-05 |
| 곱의 미분법 | product rule | 도함수끼리의 곱과 구분 | $(uv)'=u'v+uv'$로 미분하는 규칙 | M01-05 |
| 몫의 미분법 | quotient rule | 도함수끼리의 몫과 구분 | 함수의 몫을 분모 변화까지 반영해 미분하는 규칙 | M01-05 |
| 거듭제곱 법칙 | power rule | 지수함수의 미분과 구분 | $x^n$을 $nx^{n-1}$로 미분하는 규칙 | M01-05 |
| 연쇄법칙 | chain rule | 곱의 미분법과 구분 | 합성 경로의 국소 도함수를 곱하는 규칙 | M01-06 |
| 국소 도함수 | local derivative | 전체 경로의 도함수와 구분 | 계산 한 단계의 출력이 그 입력에 대해 갖는 도함수 | M01-06 |
| 로그합지수 | log-sum-exp | 소프트맥스와 구분 | 지수값의 합에 로그를 취한 함수 | M01-07 |
| 리만 합 | Riemann sum | 정적분의 극한값과 구분 | 함수값과 작은 구간 폭의 곱을 더한 근삿값 | M01-08 |
| 정적분 | definite integral | 부정적분과 구분 | 구간에서 함수값을 부호와 함께 누적한 스칼라 | M01-08 |
| 적분함수 | integrand | 적분 결과와 구분 | 적분 기호 안에서 누적하는 함수 | M01-08 |
| 적분변수 | variable of integration | 적분의 끝점과 구분 | 작은 구간을 나누는 입력 변수 | M01-08 |
| 구간 가법성 | interval additivity | 함수값의 덧셈과 구분 | 인접 구간의 적분을 더해 전체 구간 적분을 얻는 성질 | M01-08 |
| 누적함수 | accumulation function | 적분함수와 구분 | 적분의 끝점을 입력으로 갖는 함수 | M01-08 |
| 미적분의 기본정리 | fundamental theorem of calculus | 미분 규칙 하나와 구분 | 누적함수의 미분과 원시함수를 통한 정적분 계산을 연결하는 정리 | M01-09 |
| 원시함수 | antiderivative | 도함수와 구분 | 미분하면 주어진 함수가 되는 함수 | M01-09 |
| 부정적분 | indefinite integral | 정적분과 구분 | 적분상수를 포함한 모든 원시함수의 모음 | M01-09 |
| 적분상수 | constant of integration | 정적분의 끝점과 구분 | 부정적분에서 원시함수 사이의 상수 차이를 나타내는 값 | M01-09 |
| 순변화 정리 | net change theorem | 이동한 총거리와 구분 | 변화율의 정적분을 양 끝 함수값의 차이로 바꾸는 정리 | M01-09 |
| 편미분 | partial derivative | 전체미분과 구분 | 다른 입력을 고정한 변화율 | M01-10 |
| 편미분계수 | partial derivative at a point | 편도함수 전체와 구분 | 한 점에서 한 좌표 방향으로 측정한 순간변화율 | M01-10 |
| 편도함수 | partial derivative function | 편미분계수와 구분 | 각 입력점에 한 좌표 방향의 편미분계수를 대응시키는 함수 | M01-10 |
| 방향미분 | directional derivative | gradient와 구분 | 지정한 방향으로의 변화율 | M01-11 |
| 그래디언트 | gradient | 그래프의 기울기(slope)와 구분 | 방향미분을 나타내는 벡터 표현 | M01-11 |
| 단위벡터 | unit vector | 방향만 같은 임의 길이 벡터와 구분 | 노름이 1인 벡터 | M01-11 |
| 그래디언트 하강 | gradient descent | 그래디언트 계산과 구분 | 손실 그래디언트의 반대 방향으로 파라미터를 갱신하는 방법 | M01-11 |
| 안장점 | saddle point | 국소 최솟값과 구분 | 주변에 더 큰 값과 더 작은 값이 모두 있는 정지점 | M01-11 |
| Taylor 근사 | Taylor approximation | 정확한 등식과 구분 | 한 점의 도함수들로 가까운 함수값을 나타내는 다항식 근사 | M01-12 |
| 이차도함수 | second derivative | 일차도함수와 구분 | 도함수를 한 번 더 미분한 함수 | M01-12 |
| 잔차 | remainder | 회귀 잔차와 문맥상 구분 | 실제 함수값과 Taylor 다항식의 차이 | M01-12 |
| 수치미분 | numerical differentiation | 해석적 미분과 구분 | 가까운 함수값의 유한차분으로 도함수를 근사하는 방법 | M01-13 |
| 전진차분 | forward difference | 중앙차분과 구분 | 현재점과 앞쪽 점으로 만든 변화율 근사 | M01-13 |
| 후진차분 | backward difference | 중앙차분과 구분 | 뒤쪽 점과 현재점으로 만든 변화율 근사 | M01-13 |
| 중앙차분 | central difference | 한쪽 차분과 구분 | 기준점 양쪽의 대칭점으로 만든 변화율 근사 | M01-13 |
| 절단오차 | truncation error | 반올림오차와 구분 | 근사식에서 높은 차수 항을 버려 생기는 오차 | M01-13 |
| 반올림오차 | roundoff error | 절단오차와 구분 | 유한 정밀도 수 표현과 연산에서 생기는 오차 | M01-13 |
| 그래디언트 검사 | gradient check | 학습 성능 평가와 구분 | 해석적·자동미분 그래디언트를 수치차분과 비교하는 절차 | M01-13 |
| 적분 | integration | 단순 넓이에 한정하지 않음 | 작은 양의 연속적인 누적 | M01-08 |
| total derivative | total derivative | 편미분 목록과 구분 | 입력 변화벡터를 일차 출력 변화로 보내는 국소 선형사상 | M03-10 |
| remainder | remainder | 일차항과 구분 | 함수의 실제 변화에서 근사항을 뺀 오차 | M03-10 |
| little-o | little-o notation | 고정된 작은 상수와 구분 | 기준량으로 나눈 비가 극한에서 0이 되는 오차 차수 | M03-10 |
| 국소 선형화 | local linearization | 전역 선형성과 구분 | 한 기준점 주변에서 함수 변화를 derivative로 근사하는 일 | M03-10 |
| Jacobian | Jacobian | gradient 열벡터와 구분 | vector 함수 total derivative의 출력 행·입력 열 좌표행렬 | M03-11 |
| 국소 민감도 | local sensitivity | 전역 안정성과 구분 | 한 기준점 주변의 작은 입력 변화에 대한 출력 변화율 | M03-11 |
| Hessian | Hessian | activation 행렬 H와 구분 | scalar 함수 gradient의 Jacobian인 이차 편미분 행렬 | M03-12 |
| second differential | second differential | Hessian 좌표행렬과 구분 | 두 변화벡터를 이차 변화량으로 보내는 bilinear form | M03-12 |
| 혼합편미분 | mixed partial derivative | 같은 변수의 이차 미분과 구분 | 서로 다른 입력좌표를 차례로 미분한 값 | M03-12 |
| HVP | Hessian-vector product | 전체 Hessian과 구분 | Hessian을 한 방향벡터에 곱한 결과 | M03-12 |
| Hessian spectrum | Hessian spectrum | 한 고유값과 구분 | Hessian 고유값들의 모음 | M03-12 |
| JVP | Jacobian-vector product | 전체 Jacobian과 구분 | 입력 tangent를 출력 tangent로 보내는 Jacobian과 vector의 곱 | M03-13 |
| VJP | vector-Jacobian product | JVP와 방향 구분 | 출력 cotangent를 입력 쪽으로 당기는 transpose Jacobian과 vector의 곱 | M03-13 |
| tangent | tangent | 원래 입력값과 구분 | 지정한 입력 방향을 따라 전달되는 일차 변화량 | M03-13 |
| cotangent | cotangent | 출력 perturbation과 구분 | scalar 측정의 민감도를 입력 쪽으로 pullback하는 dual 값 | M03-13 |
| adjoint identity | adjoint identity | JVP와 VJP가 같은 vector라는 뜻이 아님 | JVP와 VJP의 scalar pairing이 같음을 나타내는 등식 | M03-13 |
| 자동미분 | automatic differentiation, AD | 수치미분과 구분 | 기본 연산의 미분 규칙을 실행된 계산에 합성하는 방법 | M03-14 |
| 계산 그래프 | computational graph | 함수 그래프와 구분 | 값과 연산의 directed dependency를 나타낸 그래프 | M03-14 |
| forward mode | forward-mode AD | 모델 forward pass 자체와 구분 | primal과 tangent를 계산 순서로 전달하는 자동미분 mode | M03-14 |
| reverse mode | reverse-mode AD | 역함수 계산과 구분 | cotangent를 연산의 역순으로 전달하는 자동미분 mode | M03-14 |
| 국소 미분 | local derivative | 전체 합성함수의 미분과 구분 | 한 기본 연산의 입력과 출력 사이 derivative | M03-14 |
| gradient 누적 | gradient accumulation | optimizer update와 구분 | 여러 계산 경로에서 온 cotangent 기여를 더하는 일 | M03-14 |
| 체크포인팅 | checkpointing | 모델 checkpoint 저장과 구분 | 중간값 일부를 다시 계산해 reverse-mode memory를 줄이는 방법 | M03-14 |

## 선형대수

| 권장 표기 | 영어 | 피하거나 구분할 표현 | 짧은 뜻 | 최초 단원 |
|---|---|---|---|---|
| 벡터공간 | vector space | 숫자 열벡터의 집합에 한정하지 않음 | 벡터 덧셈과 스칼라곱이 공리를 만족하는 집합 | M03-01 |
| 벡터공간 공리 | vector space axioms | 계산 요령과 구분 | 덧셈과 스칼라곱이 만족해야 하는 대수 법칙 | M03-01 |
| 함수공간 | function space | 함수 하나와 구분 | 지정한 입력·출력과 조건을 갖는 함수들의 벡터공간 | M03-01 |
| 순서 있는 기저 | ordered basis | 순서를 무시한 기저 집합과 구분 | 각 좌표의 위치까지 정하는 순서 있는 기저 목록 | M03-02 |
| 선형사상 | linear map | 행렬 표현 자체와 구분 | 벡터의 선형결합을 보존하는 두 벡터공간 사이의 함수 | M03-02 |
| 행렬 표현 | matrix representation | 추상 선형사상과 구분 | 정의역·공역 기저를 고른 뒤 얻는 선형사상의 좌표 행렬 | M03-02 |
| 항등사상 | identity map | 항등행렬과 구분 | 각 벡터를 자기 자신으로 보내는 사상 | M03-02 |
| 좌표변환행렬 | change-of-basis matrix | 벡터 자체를 바꾸는 변환과 구분 | 한 기저의 좌표를 다른 기저의 좌표로 바꾸는 가역행렬 | M03-03 |
| 유사변환 | similarity transformation | 합동변환과 구분 | 같은 선형연산자의 서로 다른 기저 행렬을 연결하는 변환 | M03-03 |
| 좌표 의존성 | coordinate dependence | 대상 자체의 변화와 구분 | 기저 선택에 따라 수치 표현이 달라지는 성질 | M03-03 |
| 수동적 좌표변경 | passive change of coordinates | 능동적 변환과 구분 | 대상을 유지하고 그 좌표 표현만 바꾸는 일 | M03-03 |
| 능동적 변환 | active transformation | 수동적 좌표변경과 구분 | 좌표계를 유지하고 벡터 자체를 바꾸는 사상 | M03-03 |
| 불변량 | invariant | 변하지 않는다는 무조건적 주장과 구분 | 지정한 변환 아래 값이 유지되는 함수나 양 | M03-04 |
| 불변성 | invariance | equivariance와 구분 | 입력을 변환해도 출력이 같은 성질 | M03-04 |
| equivariance | equivariance | 불변성과 구분 | 입력변환에 맞춰 출력도 정해진 방식으로 변하는 성질 | M03-04 |
| 부분공간의 합 | sum of subspaces | 합집합과 구분 | 두 부분공간에서 고른 벡터를 더해 만든 부분공간 | M03-05 |
| 직합 | direct sum | 부분공간의 합 전체와 구분 | 교집합이 영공간이며 분해가 유일한 부분공간 합 | M03-05 |
| 여공간 | complement | 집합론의 여집합과 구분 | 주어진 부분공간과 직합해 전체 공간을 만드는 부분공간 | M03-05 |
| 직교여공간 | orthogonal complement | 일반 여공간과 구분 | 주어진 부분공간의 모든 벡터와 직교하는 벡터들의 공간 | M03-05 |
| 동치관계 | equivalence relation | 유사도와 구분 | 반사성·대칭성·추이성을 만족하는 관계 | M03-06 |
| 동치류 | equivalence class | 대표원 하나와 구분 | 한 원소와 동치인 모든 원소의 집합 | M03-06 |
| 대표원 | representative | 동치류 자체와 구분 | 동치류를 표시하기 위해 고른 한 원소 | M03-06 |
| coset | coset | 부분공간 자체와 구분 | 부분공간을 한 벡터만큼 평행이동한 집합 | M03-06 |
| 몫공간 | quotient space | scalar 나눗셈과 구분 | 부분공간 방향의 차이를 무시한 동치류들의 벡터공간 | M03-06 |
| quotient map | quotient map | 정사영과 구분 | 벡터를 그 벡터가 속한 coset으로 보내는 선형사상 | M03-06 |
| well-defined | well-defined | 대표원 선택에 따라 달라지는 규칙과 구분 | 허용된 모든 표현에서 결과가 모순 없이 정해지는 성질 | M03-06 |
| 계수 | coefficient | 벡터 성분과 구분 | 선형결합에서 각 벡터에 곱하는 scalar | M02-02 |
| 선형결합 | linear combination | 단순 합과 구분 | 벡터에 scalar를 곱해 더한 것 | M02-02 |
| 생성공간 | span | 범위와 혼동 주의 | 가능한 모든 선형결합의 집합 | M02-02 |
| 부분공간 | subspace | 부분집합과 구분 | 영벡터를 포함하고 벡터 덧셈과 스칼라곱에 닫힌 집합 | M02-02 |
| Euclidean 거리 | Euclidean distance | dimension과 구분 | 두 벡터 차이의 Euclidean norm | M02-03 |
| 직교 | orthogonal | 통계적 독립과 구분 | 내적이 0인 벡터 관계 | M02-03 |
| 정사영 | orthogonal projection | 좌표를 버리는 임의 연산과 구분 | 벡터를 지정한 부분공간의 가장 가까운 벡터로 보내는 연산 | M02-03 |
| cosine similarity | cosine similarity | Euclidean 거리와 구분 | 두 영이 아닌 벡터 사이 각도의 cosine | M02-03 |
| 행렬곱 | matrix multiplication | 원소별 곱과 구분 | 왼쪽 행과 오른쪽 열의 내적으로 만든 행렬 | M02-04 |
| 항등행렬 | identity matrix | 모든 원소가 1인 행렬과 구분 | 곱한 벡터나 행렬을 바꾸지 않는 정사각행렬 | M02-04 |
| Hadamard 곱 | Hadamard product | 행렬곱과 구분 | 같은 shape의 행렬을 대응 원소끼리 곱하는 연산 | M02-04 |
| 선형변환 | linear transformation | 아핀변환과 구분 | 벡터의 덧셈과 스칼라곱을 보존하는 변환 | M02-05 |
| 표준기저 | standard basis | 임의의 기저와 구분 | 한 성분만 1이고 나머지가 0인 벡터들의 기저 | M02-05 |
| 아핀변환 | affine transformation | 선형변환과 구분 | 선형변환 결과에 고정 벡터를 더하는 변환 | M02-05 |
| 확대행렬 | augmented matrix | 행렬 확대와 구분 | 계수행렬과 연립방정식 우변을 나란히 붙인 행렬 | M02-06 |
| 행 기본변환 | elementary row operation | 열 연산과 구분 | 해집합을 보존하며 행을 교환·배율·가감하는 연산 | M02-06 |
| Gaussian 소거법 | Gaussian elimination | 역행렬 계산과 동일시하지 않음 | 행 기본변환으로 연립방정식을 푸는 방법 | M02-06 |
| pivot | pivot | 단순히 큰 원소와 구분 | 행 사다리꼴에서 한 행의 첫 0이 아닌 원소 위치 | M02-06 |
| 자유변수 | free variable | 임의 오차와 구분 | pivot이 없는 미지수 열에 대응해 자유롭게 정하는 변수 | M02-06 |
| 역행렬 | inverse matrix | 원소별 역수와 구분 | 양쪽에서 곱해 항등행렬을 만드는 행렬 | M02-06 |
| 가역행렬 | invertible matrix | 정사각행렬 전체와 구분 | 역행렬이 존재하는 정사각행렬 | M02-06 |
| 특이행렬 | singular matrix | 값이 특이하다는 일상어와 구분 | 역행렬이 존재하지 않는 정사각행렬 | M02-06 |
| 선형종속 | linear dependence | 벡터가 서로 같다는 뜻에 한정하지 않음 | 영벡터를 만드는 0이 아닌 계수 조합이 있는 관계 | M02-07 |
| 좌표벡터 | coordinate vector | 벡터 자체와 구분 | 선택한 기저에 대해 벡터를 나타내는 계수 열벡터 | M02-07 |
| 선형독립 | linear independence | 직교와 동일하지 않음 | 서로를 선형결합으로 만들 수 없는 관계 | M02-07 |
| 기저 | basis | 좌표축과 동일하지 않음 | 공간을 유일하게 표현하는 독립 생성집합 | M02-07 |
| 핵공간 | kernel, null space | convolution kernel과 구분 | 선형사상이 0으로 보내는 입력 | M02-08 |
| 상 | image | 이미지 데이터와 구분 | 선형사상이 실제로 만들어내는 출력 | M02-08 |
| 랭크 | rank | 계수, 순위 | 독립적인 출력 방향의 수 | M02-08 |
| 열공간 | column space | 행공간과 구분 | 행렬 열벡터들이 생성하는 image | M02-08 |
| nullity | nullity | kernel 자체와 구분 | kernel의 차원 | M02-08 |
| rank-nullity 정리 | rank-nullity theorem | rank와 nullity가 같다는 뜻이 아님 | 입력 dimension이 rank와 nullity의 합이라는 정리 | M02-08 |
| 직교기저 | orthogonal basis | 정규직교기저와 구분 | 서로 직교하는 벡터로 이뤄진 기저 | M02-09 |
| 정규직교기저 | orthonormal basis | 직교만 하는 기저와 구분 | 서로 직교하며 각 norm이 1인 기저 | M02-09 |
| Kronecker delta | Kronecker delta | Dirac delta와 구분 | 두 인덱스가 같으면 1, 다르면 0인 기호 | M02-09 |
| 정사영 행렬 | projection matrix | 임의의 차원 축소 행렬과 구분 | 벡터를 지정한 부분공간 위로 정사영하는 행렬 | M02-09 |
| 멱등행렬 | idempotent matrix | 항등행렬과 구분 | $\mathbf P^2=\mathbf P$를 만족하는 행렬 | M02-09 |
| Gram-Schmidt 과정 | Gram-Schmidt process | 행 소거와 구분 | 독립 벡터를 같은 span의 정규직교기저로 바꾸는 과정 | M02-09 |
| 최소제곱 | least squares | 정확한 연립방정식 풀이와 구분 | 잔차의 제곱 norm을 최소화하는 문제 | M02-09 |
| 정규방정식 | normal equations | 확률분포의 정규성과 무관 | 최소제곱 잔차의 직교 조건에서 얻는 방정식 | M02-09 |
| determinant | determinant | 행렬의 모든 원소 곱과 구분 | 정사각행렬의 방향 있는 부피 배율 | M02-10 |
| 방향 순서 | orientation | 벡터 방향 하나와 구분 | 기저 축의 순서가 보존되거나 반전되는 성질 | M02-10 |
| 삼각행렬 | triangular matrix | 대각행렬과 구분 | 주대각선 한쪽의 원소가 모두 0인 정사각행렬 | M02-10 |
| 고유값 | eigenvalue | 특이값과 구분 | 고유방향의 확대·축소 계수 | M02-11 |
| 고유벡터 | eigenvector | 특이벡터와 구분 | 선형변환 뒤 방향이 유지되는 벡터 | M02-11 |
| 고유공간 | eigenspace | 고유벡터 하나와 구분 | 한 고유값에 대응하는 고유벡터들과 영벡터의 부분공간 | M02-11 |
| 특성다항식 | characteristic polynomial | 최소다항식과 구분 | $\det(\mathbf A-\lambda\mathbf I)$로 만든 고유값 방정식의 다항식 | M02-11 |
| 대각화 | diagonalization | 대각 원소만 읽는 것과 구분 | 고유벡터 기저에서 행렬을 대각행렬로 표현하는 분해 | M02-11 |
| 대칭행렬 | symmetric matrix | 원소가 모두 같은 행렬과 구분 | 전치와 같은 정사각행렬 | M02-12 |
| 스펙트럼 정리 | spectral theorem | 일반 정사각행렬 전체에 적용하지 않음 | 실수 대칭행렬에 정규직교 고유기저가 있음을 보장하는 정리 | M02-12 |
| 스펙트럼 분해 | spectral decomposition | SVD와 구분 | 대칭행렬을 $\mathbf Q\boldsymbol\Lambda\mathbf Q^\top$로 나타내는 분해 | M02-12 |
| quadratic form | quadratic form | bilinear form과 구분 | $\mathbf x^\top\mathbf A\mathbf x$ 꼴의 scalar 식 | M02-12 |
| 양의 준정부호 | positive semidefinite, PSD | 양의 정부호와 구분 | 모든 벡터에서 quadratic form이 0 이상인 성질 | M02-12 |
| 특이값분해 | singular value decomposition, SVD | 고유값분해와 구분 | 행렬을 입력방향·증폭률·출력방향으로 분해 | M02-13 |
| 특이값 | singular value | 고유값과 구분 | 오른쪽 특이방향의 0 이상인 증폭률 | M02-13 |
| 오른쪽 특이벡터 | right singular vector | 왼쪽 특이벡터와 구분 | SVD에서 입력공간의 직교 방향 | M02-13 |
| 왼쪽 특이벡터 | left singular vector | 오른쪽 특이벡터와 구분 | SVD에서 출력공간의 직교 방향 | M02-13 |
| compact SVD | compact SVD | full SVD와 구분 | 양의 특이값에 대응하는 성분만 남긴 SVD | M02-13 |
| spectral norm | spectral norm | Frobenius norm과 구분 | 행렬의 가장 큰 방향별 증폭률 | M02-13 |
| Frobenius norm | Frobenius norm | spectral norm과 구분 | 행렬 원소 또는 특이값 제곱합의 제곱근 | M02-13 |
| truncated SVD | truncated SVD | compact SVD와 구분 | 상위 일부 특이성분만 남긴 저랭크 근사 | M02-13 |
| 중심화 | centering | 표준화와 구분 | 각 feature에서 표본평균을 빼는 전처리 | M02-14 |
| 공분산행렬 | covariance matrix | 상관행렬과 구분 | feature 쌍의 표본 공분산을 모은 대칭행렬 | M02-14 |
| trace | trace | determinant와 구분 | 정사각행렬 대각 원소의 합 | M02-14 |
| 주성분 | principal component | 원래 feature 하나와 구분 | 중심화 데이터의 분산을 크게 만드는 직교 방향 | M02-14 |
| 주성분 점수 | principal component score | 주성분 방향과 구분 | 표본을 주성분 방향에 투영한 좌표 | M02-14 |
| 설명분산비율 | explained variance ratio | 재구성 정확도 전체와 동일시하지 않음 | 전체 표본분산 중 주성분이 차지하는 비율 | M02-14 |
| 표준화 | standardization | 중심화와 구분 | feature별 평균을 빼고 표준편차로 나누는 전처리 | M02-14 |
| 주성분분석 | principal component analysis, PCA | SVD와 동일하지 않음 | 데이터 변동이 큰 직교방향을 찾는 방법 | M02-14 |
| L1 norm | L1 norm | Euclidean norm과 구분 | 벡터 성분 절댓값의 합 | M02-15 |
| L2 norm | L2 norm | L1 norm과 구분 | 벡터 성분 제곱합의 제곱근 | M02-15 |
| infinity norm | infinity norm | 무한한 크기라는 뜻이 아님 | 벡터 성분 절댓값의 최댓값 | M02-15 |
| 삼각부등식 | triangle inequality | 등식으로 오해하지 않음 | 합의 norm이 각 norm의 합보다 크지 않다는 조건 | M02-15 |
| condition number | condition number | determinant와 구분 | 최댓값과 최솟값 방향의 증폭률 비 | M02-15 |
| 상대오차 | relative error | 절대오차와 구분 | 오차 norm을 기준값 norm으로 나눈 비 | M02-15 |
| 쌍대공간 | dual space | 원래 공간과 구분 | 벡터를 scalar로 보내는 선형함수들의 공간 | M03-07 |
| covector | covector | gradient vector와 구분 | 벡터에 작용해 scalar를 만드는 선형함수 | M03-07 |
| dual basis | dual basis | 원래 기저와 구분 | 원래 기저의 좌표 계수를 하나씩 읽는 covector 기저 | M03-07 |
| differential | differential | gradient vector와 구분 | 변화벡터를 함수값의 일차 변화량으로 보내는 covector | M03-07 |
| bilinear map | bilinear map | 두 입력을 묶은 선형함수와 구분 | 두 입력 각각에 대해 선형인 함수 | M03-08 |
| bilinear form | bilinear form | 내적과 동일시하지 않음 | 같은 벡터공간의 두 벡터를 scalar로 보내는 bilinear map | M03-08 |
| 대칭 부분 | symmetric part | 원래 행렬 전체와 구분 | $\frac12(\mathbf A+\mathbf A^\top)$로 얻는 대칭행렬 | M03-08 |
| congruence transformation | congruence transformation | similarity transformation과 구분 | bilinear form의 기저별 행렬을 연결하는 $\mathbf P^\top\mathbf A\mathbf P$ 변환 | M03-08 |
| polarization identity | polarization identity | quadratic form 자체와 구분 | 대칭 quadratic form에서 bilinear form을 복원하는 식 | M03-08 |
| tensor | tensor | 다축 배열과 완전히 동일하지 않음 | 기저변환 법칙을 가진 multilinear 구조의 대상 | M00-09 |
| multilinear map | multilinear map | 모든 입력을 묶은 선형함수와 구분 | 각 입력 자리에 대해 따로 선형인 함수 | M03-09 |
| tensor order | tensor order | tensor rank와 구분 | tensor의 vector·covector 입력 자리 수 | M03-09 |
| tensor product | tensor product | 원소별 곱과 구분 | multilinear 입력 자리를 결합해 새 tensor를 만드는 연산 | M03-09 |
| outer product | outer product | 내적과 구분 | 두 좌표 열로 rank-1 행렬 또는 order-2 성분 배열을 만드는 곱 | M03-09 |
| contraction | contraction | 임의의 원소 합과 구분 | 대응 인덱스를 합하거나 입력을 넣어 tensor order를 줄이는 연산 | M03-09 |
| tensor rank | tensor rank | tensor order와 구분 | tensor를 rank-1 tensor의 합으로 나타내는 데 필요한 최소 항 수에 관한 개념 | M03-09 |
| 재매개화 | reparameterization | 모델 함수 변경과 동일시하지 않음 | 같은 모델족을 다른 파라미터 map으로 표현하는 일 | M03-15 |
| 모델 대칭성 | model symmetry | 모든 파라미터 변화와 구분 | 파라미터를 바꾸면서 모든 입력에 대한 모델 함수를 보존하는 성질 | M03-15 |
| symmetry transformation | symmetry transformation | 수동적 좌표변경과 구분 | 모델 함수를 보존하는 능동적 파라미터 변환 | M03-15 |
| orbit | orbit | optimization trajectory와 구분 | 한 파라미터에 symmetry transformation을 적용해 얻는 동치류 | M03-15 |
| 함수 동치 | functional equivalence | 유한 sample에서 같은 출력과 구분 | 모든 허용 입력에서 두 parameterization의 출력 함수가 같은 관계 | M03-15 |
| hidden-unit permutation | hidden-unit permutation | unit 하나만 이동하는 변환과 구분 | 인접 layer를 함께 바꿔 hidden unit 순서를 교환하는 symmetry | M03-15 |
| 양의 scaling symmetry | positive scaling symmetry | 음의 배율과 구분 | ReLU의 양의 동차성을 이용해 들어오고 나가는 weight scale을 상쇄하는 symmetry | M03-15 |

## 확률과 정보

| 권장 표기 | 영어 | 피하거나 구분할 표현 | 짧은 뜻 | 최초 단원 |
|---|---|---|---|---|
| 표본공간 | sample space | 관측 sample 집합과 구분 | 확률모형이 가능한 것으로 취급하는 outcome 전체의 집합 | M04-01 |
| 결과 | outcome | 사건과 구분 | 한 번의 시행에서 나온 표본공간의 원소 | M04-01 |
| 사건 | event | outcome 하나와 구분 | 확률을 배정하는 표본공간의 부분집합 | M04-01 |
| 확률 | probability | 경험적 빈도와 구분 | 사건에 $[0,1]$의 수를 배정하는 공리적 규칙 | M04-01 |
| 여사건 | complement event | 집합론의 여집합과 문맥상 구분 | 관심 사건이 일어나지 않는 outcome들의 사건 | M04-01 |
| 상호배반 | mutually exclusive | 독립과 구분 | 두 사건의 교집합이 공집합인 관계 | M04-01 |
| 가산가법성 | countable additivity | 겹치는 사건의 확률 합과 구분 | 서로 겹치지 않는 가산개 사건의 합집합 확률을 합으로 계산하는 공리 | M04-01 |
| 포함배제 | inclusion-exclusion | 단순 확률 합과 구분 | 합집합 확률에서 교집합의 중복을 고치는 공식 | M04-01 |
| 경험적 빈도 | empirical frequency | 모형 확률과 구분 | 관찰 횟수 중 사건이 나타난 횟수의 비 | M04-01 |
| 조건부확률 | conditional probability | 조건 방향을 바꾼 확률과 구분 | 주어진 사건 안에서 관심 사건이 차지하는 확률 비 | M04-02 |
| 분할 | partition | 겹치는 부분집합 모음과 구분 | 서로 겹치지 않고 합치면 표본공간이 되는 사건들의 모음 | M04-02 |
| 전체확률법칙 | law of total probability | 한 조건 경로와 구분 | 분할의 각 경로에서 나온 사건 확률을 합하는 법칙 | M04-02 |
| Bayes 규칙 | Bayes' rule | 조건 방향의 단순 교환과 구분 | likelihood와 prior로 posterior를 계산하는 공식 | M04-02 |
| 사전확률 | prior probability | 증거 반영 뒤의 확률과 구분 | 새 증거를 조건으로 넣기 전 관심 사건의 확률 | M04-02 |
| 사후확률 | posterior probability | likelihood와 구분 | 관측 증거를 조건으로 반영한 관심 사건의 확률 | M04-02 |
| base rate | base rate | 조건부 성능과 구분 | 관심 사건이 전체 집단에서 나타나는 기본 비율 | M04-02 |
| 독립 | independence | 상호배반과 구분 | 교집합 확률이 두 주변확률의 곱으로 분해되는 관계 | M04-02 |
| 조건부독립 | conditional independence | 무조건 독립과 구분 | 지정한 조건을 고정한 분포에서 성립하는 독립 | M04-02 |
| 확률변수 | random variable | 무작위 숫자와 동일시하지 않음 | 결과를 수에 대응시키는 함수 | M04-03 |
| 확률분포 | probability distribution | 관측값 하나와 구분 | 확률변수가 값이나 구간에 확률을 배정하는 규칙 | M04-03 |
| 확률질량함수 | probability mass function, PMF | 확률밀도함수와 구분 | 이산 확률변수의 각 값에 점확률을 배정하는 함수 | M04-03 |
| 누적분포함수 | cumulative distribution function, CDF | 확률밀도함수와 구분 | 확률변수가 임계값 이하일 확률을 주는 함수 | M04-03 |
| 확률밀도함수 | probability density function, PDF | 한 점의 확률과 구분 | 구간에 적분해 연속 확률변수의 확률을 만드는 함수 | M04-03 |
| 결합분포 | joint distribution | 주변분포 목록과 구분 | 여러 확률변수가 함께 값을 갖는 확률 규칙 | M04-03 |
| 주변분포 | marginal distribution | 조건부분포와 구분 | 결합분포에서 다른 변수 값을 합하거나 적분해 얻는 한 변수의 분포 | M04-03 |
| 조건부분포 | conditional distribution | 결합분포와 구분 | 다른 변수의 값을 조건으로 고정한 확률분포 | M04-03 |
| 역상 | preimage | 역함수와 구분 | 함수 출력 조건을 만족하도록 입력 쪽에서 모은 집합 | M04-03 |
| 기댓값 | expectation | 표본평균과 항상 같지 않음 | 분포에 따른 가중평균 | M04-04 |
| 분산 | variance | 오차와 구분 | 평균 주변의 퍼짐 | M04-04 |
| 표준편차 | standard deviation | 분산과 구분 | 분산의 제곱근으로 원래 변수와 같은 단위를 가진 퍼짐 | M04-04 |
| 지시변수 | indicator variable | 사건 자체와 구분 | 사건이 일어나면 1, 아니면 0을 갖는 확률변수 | M04-04 |
| 모멘트 | moment | 한 관측값의 거듭제곱과 구분 | 확률변수 거듭제곱이나 중심화 거듭제곱의 기댓값 | M04-04 |
| 상관계수 | correlation coefficient | 인과효과와 구분 | 공분산을 두 표준편차의 곱으로 나눈 선형 관계 요약값 | M04-04 |
| 공분산 | covariance | 인과관계가 아님 | 두 변수의 선형 공동변화를 나타내는 값 | M02-14 |
| support | support | 관측된 값 목록과 구분 | 확률변수가 가질 수 있는 값들의 집합 | M04-05 |
| Bernoulli 분포 | Bernoulli distribution | binomial 분포와 구분 | 한 번의 binary 결과에 성공확률을 배정하는 분포 | M04-05 |
| categorical 분포 | categorical distribution | one-hot 관측값과 구분 | 여러 범주 중 하나에 확률을 배정하는 분포 | M04-05 |
| binomial 분포 | binomial distribution | Bernoulli 한 번과 구분 | 독립 Bernoulli 시행 여러 번의 성공 횟수 분포 | M04-05 |
| Gaussian 분포 | Gaussian distribution | 평균·분산만 같은 임의 분포와 구분 | 평균과 분산을 파라미터로 갖는 종 모양 연속분포 | M04-05 |
| 표준정규분포 | standard normal distribution | 일반 Gaussian 분포와 구분 | 평균 0, 분산 1인 Gaussian 분포 | M04-05 |
| z-score | z-score | 원래 관측값과 구분 | 관측값이 평균에서 표준편차 몇 배 떨어졌는지 나타내는 값 | M04-05 |
| one-hot vector | one-hot vector | class 확률 vector와 구분 | 관측 class 위치만 1이고 나머지는 0인 vector | M04-05 |
| 다변량 Gaussian | multivariate Gaussian | 독립 Gaussian 성분 모음과 동일시하지 않음 | 평균벡터와 공분산행렬로 정하는 vector 분포 | M04-05 |
| 모집단 | population | 관측 sample과 구분 | 연구자가 추론하고 일반화하려는 결과 집합이나 분포 | M04-06 |
| 표본 | sample | 표본공간과 구분 | 모집단에서 관측한 유한한 값들의 모음 | M04-06 |
| 확률표본 | random sample | 관측값 목록과 구분 | 표집 전 확률변수로 나타낸 sample | M04-06 |
| iid | independent and identically distributed | 같은 source라는 뜻과 구분 | 관측들이 서로 독립이며 같은 분포를 따른다는 가정 | M04-06 |
| 모수 | parameter | 통계량과 구분 | 모집단 분포를 정하거나 요약하는 고정된 미지의 값 | M04-06 |
| 통계량 | statistic | 모수와 구분 | 관측 전 확률표본의 함수이며 모르는 모수를 직접 입력으로 쓰지 않는 양 | M04-06 |
| 표본평균 | sample mean | 모평균과 구분 | 관측값 합을 sample size로 나눈 통계량 | M04-06 |
| 표본분산 | sample variance | 모분산과 구분 | sample의 평균 주변 제곱편차를 요약한 통계량 | M04-06 |
| 경험분포 | empirical distribution | 모집단 분포와 구분 | 관측 sample의 각 값에 같은 질량을 둔 분포 | M04-06 |
| 표본분포 | sampling distribution | sample 값의 histogram과 구분 | repeated sampling에서 통계량이 갖는 확률분포 | M04-06 |
| 표준오차 | standard error | 원자료의 표준편차와 구분 | 통계량 sampling distribution의 표준편차 | M04-06 |
| 중심극한정리 | central limit theorem, CLT | 유한 sample의 정확한 Gaussian 보장과 구분 | 조건 아래 표준화한 표본평균의 분포가 Gaussian에 가까워진다는 정리 | M04-06 |
| sampling unit | sampling unit | 관측 행 하나와 항상 같지 않음 | 모집단에서 독립적으로 표집하는 기본 단위 | M04-06 |
| 추정량 | estimator | 관측 추정값과 구분 | 확률표본을 모수의 추정값으로 보내는 통계량 | M04-07 |
| 추정값 | estimate | 추정량 규칙과 구분 | 관측 sample을 추정량에 넣어 얻은 고정된 값 | M04-07 |
| 통계적 편향 | statistical bias | 신경망 bias 파라미터와 구분 | 추정량의 기댓값과 target 모수의 차이 | M04-07 |
| 불편추정량 | unbiased estimator | 관측마다 정확한 추정량과 구분 | 기댓값이 target 모수와 같은 추정량 | M04-07 |
| 평균제곱오차 | mean squared error, MSE | 분산 하나와 구분 | 추정량과 target의 제곱오차 기댓값 | M04-07 |
| bias-variance tradeoff | bias-variance tradeoff | bias나 variance 하나만의 비교와 구분 | bias를 허용해 variance와 전체 prediction error를 조절하는 관계 | M04-07 |
| shrinkage | shrinkage | 임의의 scale 축소와 구분 | 추정값을 기준점 쪽으로 줄여 variance를 낮추는 추정 방식 | M04-07 |
| 일치성 | consistency | 불편성과 구분 | sample size가 커질 때 추정량이 target에 확률적으로 가까워지는 성질 | M04-07 |
| selection bias | selection bias | 표집편향 전체와 구분 | 같은 noisy 평가값으로 후보를 고르고 보고해 생기는 체계적 낙관성 | M04-07 |
| 회귀 | regression | 분류와 구분 | 수치 target이나 그 조건부분포를 예측하는 문제 | M04-08 |
| 분류 | classification | 회귀와 구분 | 유한 class label이나 class 조건부확률을 예측하는 문제 | M04-08 |
| population risk | population risk | training loss와 구분 | target population에서 loss를 평균한 값 | M04-08 |
| empirical risk | empirical risk | population risk와 구분 | 관측 sample에서 loss를 평균한 값 | M04-08 |
| empirical risk minimization | empirical risk minimization, ERM | population risk 직접 최소화와 구분 | 관측 sample의 평균 loss를 최소화하는 학습 원리 | M04-08 |
| squared loss | squared loss | absolute loss와 구분 | target과 예측 차이를 제곱한 loss | M04-08 |
| 0-1 loss | zero-one loss | 확률 score와 구분 | class 예측이 틀리면 1, 맞으면 0인 loss | M04-08 |
| Bayes classifier | Bayes classifier | Bayes 규칙 자체와 구분 | 0-1 loss에서 조건부확률이 가장 큰 class를 고르는 최적 분류기 | M04-08 |
| 선형회귀 | linear regression | 인과효과 모형과 동일시하지 않음 | feature의 affine combination으로 수치 target을 예측하는 회귀모형 | M04-08 |
| logistic regression | logistic regression | linear regression과 구분 | feature의 affine combination으로 binary log-odds를 정하는 분류모형 | M04-08 |
| softmax regression | softmax regression | binary logistic regression과 구분 | class별 logit의 softmax로 categorical probability를 정하는 모형 | M04-08 |
| 회귀 잔차 | regression residual | Taylor remainder와 구분 | 관측 target에서 회귀 예측을 뺀 값 | M04-08 |
| 평균절대오차 | mean absolute error, MAE | MSE와 구분 | target과 예측 차이의 절댓값 평균 | M04-08 |
| confusion matrix | confusion matrix | 확률분포표와 구분 | 실제 class와 예측 class 조합의 개수를 정리한 표 | M04-08 |
| 정확도 | accuracy | calibration과 구분 | 전체 예측 중 정답 예측의 비율 | M04-08 |
| 정밀도 | precision | recall과 구분 | positive 예측 중 actual positive의 비율 | M04-08 |
| 재현율 | recall | precision과 구분 | actual positive 중 positive로 찾은 비율 | M04-08 |
| class imbalance | class imbalance | model bias와 구분 | class별 관측 빈도나 base rate가 크게 다른 상태 | M04-08 |
| 신뢰구간 | confidence interval | Bayesian credible interval과 구분 | repeated sampling에서 정한 비율로 모수를 포함하는 interval 절차 | M04-09 |
| 신뢰수준 | confidence level | 관측 구간 안의 사후확률과 구분 | 신뢰구간 절차의 target coverage $1-\alpha$ | M04-09 |
| coverage | coverage | 한 interval의 포함 여부와 구분 | 반복 표집에서 interval이 target을 포함하는 비율 | M04-09 |
| margin of error | margin of error | standard error와 구분 | 임계값과 standard error의 곱으로 정한 interval 반폭 | M04-09 |
| z interval | z interval | t interval과 구분 | 표준정규 임계값을 사용하는 confidence interval | M04-09 |
| t interval | t interval | z interval과 구분 | estimated standard deviation과 t 임계값을 사용하는 평균 interval | M04-09 |
| t 분포 | Student's t distribution | Gaussian 분포와 구분 | 모분산 추정 uncertainty를 반영해 더 두꺼운 tail을 가진 분포 | M04-09 |
| bootstrap | bootstrap | 새 population 표집과 구분 | 관측 empirical distribution에서 복원추출해 통계량 변동을 근사하는 방법 | M04-09 |
| bootstrap replicate | bootstrap replicate | 원래 estimate와 구분 | 한 bootstrap resample에서 계산한 통계량 | M04-09 |
| bootstrap standard error | bootstrap standard error | 원자료 표준편차와 구분 | bootstrap replicate들의 표준편차 | M04-09 |
| percentile interval | percentile interval | 정규형 interval과 구분 | bootstrap replicate의 양쪽 분위수를 endpoint로 쓰는 interval | M04-09 |
| paired bootstrap | paired bootstrap | 두 집단의 독립 재표집과 구분 | 짝지어진 관측 단위를 함께 재표집하는 bootstrap | M04-09 |
| cluster bootstrap | cluster bootstrap | row별 iid bootstrap과 구분 | 독립 cluster를 단위로 재표집하는 bootstrap | M04-09 |
| Monte Carlo error | Monte Carlo error | sampling bias와 구분 | 유한한 simulation·resampling 반복 수 때문에 생기는 수치 변동 | M04-09 |
| 귀무가설 | null hypothesis | 참으로 확정된 가설과 구분 | 검정통계량의 기준분포를 정하는 기준 가설 | M04-10 |
| 대립가설 | alternative hypothesis | 귀무가설의 사후확률과 구분 | 검출하려는 차이나 효과를 나타내는 가설 | M04-10 |
| 검정통계량 | test statistic | effect estimate 자체와 구분 | sample을 귀무가설 아래 극단성의 수로 바꾸는 통계량 | M04-10 |
| p-value | p-value | 귀무가설이 참일 확률과 구분 | 귀무가설 아래 관측값 이상으로 극단적인 통계량의 확률 | M04-10 |
| 유의수준 | significance level | effect size와 구분 | Type I error 통제를 위해 분석 전에 정하는 기각 기준 | M04-10 |
| Type I error | Type I error | Type II error와 구분 | 참인 귀무가설을 기각하는 오류 | M04-10 |
| Type II error | Type II error | Type I error와 구분 | 특정 대립가설이 참일 때 귀무가설을 기각하지 못하는 오류 | M04-10 |
| 검정력 | statistical power | confidence level과 구분 | 특정 효과가 있을 때 귀무가설을 기각할 확률 | M04-10 |
| effect size | effect size | p-value와 구분 | 연구 대상 차이나 관계의 크기를 나타내는 양 | M04-10 |
| 다중비교 | multiple comparisons | 검정 하나와 구분 | 여러 가설을 함께 탐색하거나 검정하는 상황 | M04-10 |
| FWER | family-wise error rate | FDR과 구분 | 한 가설 family에서 false positive가 하나 이상 생길 확률 | M04-10 |
| Bonferroni correction | Bonferroni correction | raw per-test threshold와 구분 | 전체 유의수준을 가설 수로 나눠 FWER를 통제하는 방법 | M04-10 |
| FDR | false discovery rate | FWER와 구분 | 기각한 가설 중 false discovery 비율의 기댓값 | M04-10 |
| BH 절차 | Benjamini-Hochberg procedure | Bonferroni correction과 구분 | 정렬한 p-value와 순위별 threshold로 FDR을 통제하는 절차 | M04-10 |
| 로그우도 | log-likelihood | likelihood와 구분 | likelihood의 자연로그로 iid 관측별 로그항을 합한 함수 | M04-11 |
| 최대우도추정 | maximum likelihood estimation, MLE | posterior maximization과 구분 | 관측 data likelihood를 최대화하는 parameter 추정 원리 | M04-11 |
| 최대우도추정량 | maximum likelihood estimator | 관측 MLE 값과 구분 | likelihood를 최대화하는 sample의 함수 | M04-11 |
| negative log-likelihood | negative log-likelihood, NLL | probability 자체와 구분 | log-likelihood에 음수를 붙인 minimization loss | M04-11 |
| MAP 추정 | maximum a posteriori estimation | MLE와 구분 | likelihood와 prior를 결합한 posterior를 최대화하는 추정 | M04-11 |
| model misspecification | model misspecification | optimization error와 구분 | true data distribution이 선택한 model family에 포함되지 않는 상태 | M04-11 |
| self-information | self-information | entropy 평균과 구분 | 한 outcome의 negative log-probability | M04-12 |
| surprisal | surprisal | probability 자체와 구분 | probability가 낮을수록 커지는 $-\log p(x)$ 값 | M04-12 |
| nat | nat | bit와 구분 | 자연로그를 사용한 information 단위 | M04-12 |
| bit | bit | binary outcome 하나와 구분 | base-2 logarithm을 사용한 information 단위 | M04-12 |
| predictive entropy | predictive entropy | prediction error와 구분 | 한 입력에서 model class probability의 퍼짐을 요약한 entropy | M04-12 |
| soft target | soft target | one-hot target과 구분 | 여러 class에 probability mass를 둔 target distribution | M04-12 |
| label smoothing | label smoothing | calibration 보장과 구분 | one-hot target 질량 일부를 다른 class에 나누는 학습 target 변환 | M04-12 |
| perplexity | perplexity | tokenizer와 corpus가 다른 수치의 직접 비교와 구분 | token당 평균 NLL을 지수화한 language-model 평가값 | M04-12 |
| 우도 | likelihood | probability와 관점 구분 | 관측 증거를 고정하고 가설이나 파라미터를 평가하는 함수 | M04-02 |
| 엔트로피 | entropy | 열역학 설명과 구분 | 분포의 평균적인 불확실성 | M04-12 |
| 교차엔트로피 | cross entropy | KL divergence와 구분 | target distribution에서 평균한 model의 negative log-probability | M00-10 |
| KL 발산 | Kullback–Leibler divergence | 대칭 거리가 아님 | 한 분포에서 다른 분포로의 방향성 있는 차이 | M04-13 |
| log density ratio | log density ratio | probability ratio와 구분 | 같은 outcome에서 두 분포의 질량이나 밀도 비에 log를 취한 값 | M04-13 |
| absolute continuity | absolute continuity | support가 단순히 겹치는 조건과 구분 | 기준분포가 0인 집합에 비교분포도 0의 확률을 두는 관계 | M04-13 |
| forward KL | forward KL | reverse KL과 구분 | target distribution을 평균분포로 두는 $D_{\mathrm{KL}}(p\Vert q)$ 방향 | M04-13 |
| reverse KL | reverse KL | forward KL과 구분 | approximation distribution을 평균분포로 두는 $D_{\mathrm{KL}}(q\Vert p)$ 방향 | M04-13 |
| Gibbs 부등식 | Gibbs' inequality | Jensen 부등식 자체와 구분 | KL divergence가 음수가 아님을 나타내는 부등식 | M04-13 |
| 상호정보량 | mutual information | 인과효과가 아님 | 한 변수가 다른 변수의 불확실성을 줄이는 정도 | M04-14 |
| 결합 엔트로피 | joint entropy | marginal entropy의 단순 합과 구분 | 확률변수 쌍의 joint distribution이 가진 평균 uncertainty | M04-14 |
| 조건부 엔트로피 | conditional entropy | 특정 조건 하나의 entropy와 구분 | 한 변수를 관측한 뒤 다른 변수에 남는 평균 uncertainty | M04-14 |
| 점별 상호정보량 | pointwise mutual information, PMI | 전체 상호정보량과 구분 | 한 outcome pair의 joint probability와 marginal product 사이 log ratio | M04-14 |
| marginal product | marginal product | 실제 joint distribution과 구분 | 두 marginal distribution을 곱해 만든 independence model | M04-14 |
| Markov chain | Markov chain | 임의의 변수 나열과 구분 | 중간변수를 알면 양 끝 변수가 조건부독립인 변수 관계 | M04-14 |
| data processing 부등식 | data processing inequality | estimator의 유한표본 결과와 구분 | 후처리가 source에 관한 mutual information을 늘릴 수 없다는 부등식 | M04-14 |
| 보정 | calibration | 학습 보정과 문맥 구분 | 예측확률과 실제 빈도의 일치 | M04-15 |
| reliability diagram | reliability diagram | accuracy plot과 구분 | confidence bin별 평균 confidence와 accuracy를 비교한 그림 | M04-15 |
| ECE | expected calibration error | full calibration 증명과 구분 | bin별 accuracy-confidence gap을 sample 비율로 가중한 요약값 | M04-15 |
| overconfidence | overconfidence | 오답 하나와 구분 | 예측 confidence가 대응하는 observed accuracy보다 높은 상태 | M04-15 |
| underconfidence | underconfidence | 낮은 accuracy와 구분 | 예측 confidence가 대응하는 observed accuracy보다 낮은 상태 | M04-15 |
| scoring rule | scoring rule | accuracy 하나와 구분 | probability prediction과 관측 outcome에 loss를 부여하는 규칙 | M04-15 |
| proper scoring rule | proper scoring rule | 임의의 확률 loss와 구분 | true distribution을 보고할 때 expected score가 최소가 되는 규칙 | M04-15 |
| strictly proper scoring rule | strictly proper scoring rule | proper scoring rule의 동률 허용과 구분 | true distribution에서만 expected score가 최소가 되는 규칙 | M04-15 |
| Brier score | Brier score | squared loss 회귀와 문맥 구분 | probability와 one-hot outcome 차이를 제곱해 합한 score | M04-15 |
| log score | logarithmic score | logit과 구분 | 관측 outcome에 부여한 probability의 negative logarithm | M04-15 |
| sharpness | sharpness | calibration과 구분 | forecast probability가 base rate에서 벗어나 집중되는 정도 | M04-15 |
| temperature scaling | temperature scaling | model 재학습과 구분 | positive temperature로 logit 크기를 조정해 probability concentration을 바꾸는 보정법 | M04-15 |
| 인과효과 | causal effect | association과 구분 | intervention을 달리했을 때 outcome이 변하는 정도 | M04-16 |
| intervention | intervention | 조건부 관찰과 구분 | variable을 외부에서 지정해 생성 mechanism을 바꾸는 조작 | M04-16 |
| do 연산자 | do-operator | conditioning과 구분 | $\operatorname{do}(X=x)$처럼 intervention을 표시하는 표기 | M04-16 |
| 인과 그래프 | causal graph | 관측 correlation graph와 구분 | variable 사이 causal assumption을 directed edge로 나타낸 graph | M04-16 |
| DAG | directed acyclic graph | cycle이 있는 graph와 구분 | directed cycle이 없는 directed graph | M04-16 |
| 교란변수 | confounder | mediator·collider와 구분 | treatment와 outcome의 공통원인 | M04-16 |
| 매개변수 | mediator | confounder와 구분 | treatment effect가 outcome으로 가는 경로의 중간변수 | M04-16 |
| 충돌변수 | collider | confounder와 구분 | 두 causal arrow가 모이는 공통결과 | M04-16 |
| 잠재결과 | potential outcome | 관측 outcome 하나와 구분 | 특정 treatment 상태에서 한 unit이 가질 outcome | M04-16 |
| 평균처치효과 | average treatment effect, ATE | individual effect와 구분 | $\mathbb E[Y(1)-Y(0)]$로 정의한 population 평균 causal effect | M04-16 |
| 교환가능성 | exchangeability | 단순 group equality와 구분 | treatment group이 potential outcome 관점에서 비교 가능한 조건 | M04-16 |
| positivity | positivity | outcome probability 양수 조건과 구분 | 각 confounder stratum에서 비교할 treatment가 양의 확률을 갖는 조건 | M04-16 |
| consistency | consistency | 통계적 일치성과 구분 | 받은 treatment에 대응하는 potential outcome이 관측 outcome과 같다는 조건 | M04-16 |
| 무작위 배정 | random assignment | random sampling과 구분 | treatment를 potential outcome과 독립이 되도록 확률적으로 배정하는 절차 | M04-16 |
| experimental unit | experimental unit | observation row와 구분 | treatment를 독립적으로 배정하거나 replicate를 독립 생성하는 최소 단위 | M04-17 |
| control condition | control condition | treatment condition과 구분 | intervention effect를 비교하기 위한 기준 조건 | M04-17 |
| negative control | negative control | target effect condition과 구분 | target effect가 없어야 하며 alternative explanation을 검사하는 control | M04-17 |
| positive control | positive control | primary treatment와 구분 | pipeline이 알려진 effect를 검출하는지 확인하는 control | M04-17 |
| specificity control | specificity control | target outcome 하나와 구분 | intervention이 unrelated behavior도 손상하는지 확인하는 control | M04-17 |
| sham intervention | sham intervention | target component 조작과 구분 | 절차는 같지만 target component를 바꾸지 않는 control intervention | M04-17 |
| blocking | blocking | 전체 sample의 단순 randomization과 구분 | 중요한 특성이 비슷한 block 안에서 treatment를 randomize하는 설계 | M04-17 |
| blinding | blinding | data masking과 문맥 구분 | 평가자나 참여자가 condition을 모르게 하는 절차 | M04-17 |
| holdout set | holdout set | validation set과 구분 | method 선택에 사용하지 않고 final evaluation을 위해 남긴 data | M04-17 |
| data leakage | data leakage | 일반 data 공유와 구분 | 평가 outcome 정보가 fitting이나 selection 과정에 들어가는 현상 | M04-17 |
| seed | random seed | independent replicate와 구분 | pseudorandom sequence의 초기 상태를 정하는 값 | M04-17 |
| pseudoreplication | pseudoreplication | 독립 반복과 구분 | 의존된 observation을 독립 replicate처럼 세는 오류 | M04-17 |
| preregistration | preregistration | 탐색 금지와 구분 | result 확인 전에 hypothesis와 analysis plan을 기록하는 절차 | M04-17 |
| repeatability | repeatability | independent replication과 구분 | 같은 team이 같은 artifact와 environment로 계산을 다시 실행하는 성질 | M04-17 |
| computational reproducibility | computational reproducibility | 새 data replication과 구분 | 다른 사람이 제공된 code·data·environment로 result를 재생하는 성질 | M04-17 |
| replication | replication | 같은 실행의 반복과 구분 | 독립 구현, 새 data나 새 model에서 scientific claim을 다시 시험하는 일 | M04-17 |

## 신경망

| 권장 표기 | 영어 | 피하거나 구분할 표현 | 짧은 뜻 | 최초 단원 |
|---|---|---|---|---|
| 활성값 | activation | 활성화함수와 구분 | 층의 중간 계산 결과 | N05-03 |
| 활성화함수 | activation function | activation과 구분 | 선형결합 뒤 적용하는 비선형함수 | N05-04 |
| 로짓 | logit | 확률과 구분 | 소프트맥스 전의 class 점수 | M00-10 |
| 소프트맥스 | softmax | argmax와 구분 | 로짓을 양수이며 합이 1인 class 확률로 바꾸는 함수 | M00-10 |
| 손실함수 | loss function | 평가 지표와 구분 | 학습에서 최소화하는 scalar 함수 | M00-10 |
| 지식증류 | knowledge distillation | 정답 label 학습만인 경우와 구분 | 교사 모델의 출력이나 중간 표현을 학생 모델 학습에 사용하는 방법 | M00-10 |
| 블랙박스 증류 | black-box distillation | 교사 내부 접근이 필요한 증류와 구분 | 교사의 출력 정보만 사용해 학생을 학습하는 증류 | M00-10 |
| 화이트박스 증류 | white-box distillation | 출력만 사용하는 증류와 구분 | 교사의 중간 표현이나 attention에 접근하는 증류 | M00-10 |
| 역전파 | backpropagation | optimizer update와 구분 | scalar loss에서 cotangent를 역순으로 전달해 gradient를 계산하는 과정 | M03-14 |
| 학습률 | learning rate | 도함숫값과 구분 | 한 번의 파라미터 갱신 크기를 조절하는 양수 | M01-04 |
| 임베딩 | embedding | 임베딩 공간 전체와 문맥 구분 | 이산 대상을 연속 벡터로 대응시킨 표현 | N05-12 |
| 잔차 스트림 | residual stream | residual connection 하나와 구분 | Transformer 층 사이에 누적되는 표현 경로 | N05-17 |
| 어텐션 | attention | 설명 자체로 간주하지 않음 | query-key 점수로 value를 가중합하는 연산 | N05-15 |
| 체크포인트 | checkpoint | 최종 모델과 구분 | 특정 학습 시점의 저장 상태 | N05-26 |
| 사고과정 텍스트 | chain-of-thought, CoT | 실제 내부 추론과 동일시하지 않음 | 모델이 생성한 중간 설명 형식의 token sequence | N05-23 |

## 모델 해석

| 권장 표기 | 영어 | 피하거나 구분할 표현 | 짧은 뜻 | 최초 단원 |
|---|---|---|---|---|
| 모델 해석 | model interpretability | 설명가능성과 문맥상 구분 | 모델의 행동과 내부 계산을 이해하고 검증하는 연구 | I06-01 |
| 표현 | representation | activation 하나와 항상 같지 않음 | 모델이 입력 정보를 내부 상태로 나타낸 방식 | I06-01 |
| 탐침 | probe | 모델이 실제 사용한다는 증거가 아님 | activation에서 정보를 복원하는 보조모형 | I06-06 |
| 중첩 | superposition | 단순 feature 합과 구분 | 제한된 차원에 더 많은 feature가 겹쳐 표현되는 현상 | I06-10 |
| 희소 오토인코더 | sparse autoencoder, SAE | feature의 유일성을 보장하지 않음 | 희소 latent로 activation을 재구성하는 모형 | I06-12 |
| 귀인 | attribution | 인과 설명과 동일하지 않음 | 출력에 대한 입력·성분의 기여를 배분하는 분석 | I07-01 |
| 제거 실험 | ablation | patching과 구분 | component를 제거하거나 무력화하는 개입 | I07-06 |
| 활성값 패칭 | activation patching | 단순 관찰과 구분 | 한 실행의 activation을 다른 실행에 주입하는 개입 | I07-07 |
| 회로 | circuit | 물리 회로가 아님 | 특정 행동을 만드는 내부 계산 component와 경로 | I07-11 |
| 필요성 | necessity | 충분성과 구분 | 없애면 기능이 손상되는 성질 | I07-12 |
| 충분성 | sufficiency | 필요성과 구분 | 해당 구조만으로 기능을 상당 부분 복원하는 성질 | I07-12 |
| 학습 동역학 | training dynamics | 최종 상태 분석과 구분 | 학습 중 파라미터·표현·행동의 시간적 변화 | I08-01 |
| 식별가능성 | identifiability | 재현성과 구분 | 관찰 가능한 함수나 분포로부터 파라미터를 유일하게 정할 수 있는 성질 | M03-15 |
