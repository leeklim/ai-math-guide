# 진행 현황

## 상태 정의

| 상태 | 의미 |
|---|---|
| 계획 | 목차에만 존재한다. |
| 초안 | 핵심 설명과 문제가 있으나 검토가 끝나지 않았다. |
| 검토 중 | 수학, 문체, 선수지식과 렌더링을 확인하고 있다. |
| 완료 | 단원 완료 기준을 통과했다. |
| 보류 | 외부 자료나 설계 결정이 필요하다. |

## 프로젝트 기반 문서

| 문서 | 상태 | 마지막 확인 | 비고 |
|---|---|---|---|
| `README.md` | 완료 | 2026-10-01 | 프로젝트 진입점 |
| `00-PROJECT-SPEC.md` | 완료 | 2026-10-01 | 범위와 완료 기준 |
| `01-CURRICULUM.md` | 완료 | 2026-09-30 | 단원 ID와 학습 경로 |
| `02-STYLE-AND-NOTATION.md` | 완료 | 2026-10-01 | 문체, 수학 표기와 실행 코드 규칙 |
| `03-PROGRESS.md` | 완료 | 2026-10-01 | 현재 문서 |
| `04-GLOSSARY.md` | 초안 | 2026-10-01 | 집필과 함께 확장 |
| `05-N05-ARCHITECTURE-BASELINE.md` | 완료 | 2026-10-01 | N05 아키텍처와 자료 선정 기준 |
| `N05-ENVIRONMENT.md` | 완료 | 2026-10-01 | CPU 환경, 설치와 자원 예산 |
| `GPU-ENVIRONMENT.md` | 완료 | 2026-10-01 | 분리된 CUDA 환경, Pythia cache·runner와 자원 예산 |
| `templates/lesson-template.md` | 완료 | 2026-09-30 | 단원 공통 구조 |
| `templates/n05-lesson-template.md` | 완료 | 2026-10-01 | 실행 실습 단원 확장 구조 |

## 단계별 상태

| 단계 | 범위 | 상태 | 완료/전체 | 다음 작업 |
|---|---|---|---:|---|
| M00 | 수식 읽기 | 완료 | 10/10 | M01 완료 |
| M01 | 변화와 미적분 | 완료 | 13/13 | M02 완료 |
| M02 | 벡터와 행렬 | 완료 | 15/15 | M03 완료 |
| M03 | 추상선형대수와 행렬미분 | 완료 | 15/15 | M04 완료 |
| M04 | 확률·통계·정보이론 | 완료 | 17/17 | N05 선수지식 제공 |
| N05 | 신경망과 Transformer | 완료 | 28/28 | Phase 3 GPU·Pythia 기반과 I06-01~03 |
| I06 | 표현 해석 | 완료 | 15/15 | I07 완료 |
| I07 | 귀인·인과·기계론 | 완료 | 17/17 | I08-01 checkpoint 연구 설계 |
| I08 | 학습 동역학 | 완료 | 13/13 | A09-GEO-01 집필 |
| A09-GEO | 미분기하학 | 완료 | 8/8 | A09-DYN-01 집필 |
| A09-DYN | 동역학계·확률과정 | 완료 | 8/8 | A09-SYM-01 집필 |
| A09-SYM | 군론·대칭성 | 완료 | 8/8 | A09-LRN-01 집필 |
| A09-LRN | 통계학습이론 | 완료 | 8/8 | A09-KER-01 집필 |
| A09-KER | Kernel·함수공간 | 계획 | 0/8 | 선택 |
| A09-RMT | Random matrix | 계획 | 0/8 | 선택 |
| A09-CAU | 고급 인과추론 | 계획 | 0/8 | 선택 |

## 현재 결정

- 네 부분으로 나눈다: 0~4, 5, 6~8, 9단계.
- Markdown을 기준 원본으로 사용하고 HTML을 기본 열람 형식으로 생성한다.
- 본문은 `~이다`, `~한다` 평서체로 쓴다.
- 한 번에 1~3개 단원을 작성한다.
- M00 수식 읽기 단계의 본문 단원 `M00-01`부터 `M00-10`까지 완료했다.
- M01 변화와 미적분 단계의 `M01-01`부터 `M01-13`까지 완료했다.
- M02 벡터와 행렬 단계의 `M02-01`부터 `M02-15`까지 완료하고 단계 교차 검토를 통과했다.
- M03 추상선형대수와 행렬미분 단계의 `M03-01`부터 `M03-15`까지 완료하고 단계 교차 검토를 통과했다.
- M04 확률·통계·정보이론 단계의 `M04-01`부터 `M04-17`까지 완료하고 단계 교차 검토를 통과했다.
- N05는 decoder-only pre-norm tiny model을 교육용 기준으로 사용하고 RMSNorm, RoPE, causal MHA와 dense SwiGLU를 누적 실습의 기본 선택으로 삼는다.
- N05 구성요소를 Stable core, Instructional reference, Common modern variant, Architecture-specific와 Implementation optimization으로 구분한다.
- N05 필수 실습은 외부 모델 다운로드 없이 실행하며 공개 모델은 config 대조와 후속 해석 실험에 사용한다.
- N05 필수 실습은 Python 3.12, PyTorch 2.13.0+cpu와 NumPy 2.5.3을 사용한다. 코드 원본은 `labs/N05`에 두고 build가 실제 결과를 HTML에 삽입한다.
- N05-01~N05-28은 문제·해설 170쌍, 실행 예제 28개와 N05 단위 test 59개를 포함한다.
- I06 이후 실제 모델 실험은 별도 `.venv-gpu`에서 Pythia 70M·160M·410M deduped를 사용한다. I06·I07은 `step143000`, I08 trajectory는 160M의 고정 checkpoint 여섯 개를 쓴다. CPU build는 model cache와 GPU 결과에 의존하지 않는다.
- 로컬 GPU artifact는 Git에서 제외하고, 추적하는 runner·registry와 manifest schema로 model·revision·hook·입력·자원 상한을 고정한다.
- I06-04~15는 NumPy·PyTorch CPU 예제 12개로 neuron, PCA·probe·CKA·RSA·sparse coding·SAE와 표현 보고서를 재현한다.
- I06는 문제·해설 90쌍을 포함하며, probe 복원과 기능적 사용을 분리하고 SAE를 reconstruction·sparsity·dead feature·seed 안정성으로 평가한다.
- I07은 문제·해설 102쌍과 CPU 예제 17개로 gradient·perturbation 귀인, node·edge 개입, necessity·sufficiency와 circuit 보고서를 재현한다.
- I07 실제 모델 gate는 Pythia-160M layer 5 MLP 마지막-token activation patch 하나이며, France/Germany 대비에서 Paris–Berlin logit recovery 0.0625를 원시 결과 그대로 보고한다.
- I08은 문제·해설 78쌍과 CPU 예제 13개로 checkpoint 계약, 파라미터·함수 거리, alignment, optimizer dynamics, Hessian, loss path, influence, feature emergence와 데이터 귀인을 재현한다.
- I08 실제 모델 gate는 Pythia-160M의 `step0`, `step1000`, `step10000`, `step50000`, `step100000`, `step143000`을 한 번에 하나씩 적재한다. 고정 8개 prompt에서 target first-token NLL은 10.91에서 2.74로 낮아졌지만 condition probe는 step0부터 1.0이고 zero-ablation margin effect는 비단조이므로 세 지표를 하나의 feature emergence로 합치지 않는다.
- A09-GEO는 문제·해설 32쌍으로 manifold, tangent·cotangent, metric, pullback, geodesic, curvature와 activation point-cloud 분석의 한계를 다룬다. projection의 시각적 굽음과 intrinsic curvature를 구분하고, metric·neighborhood·null control을 분석 계약에 포함한다.
- A09-DYN은 문제·해설 32쌍으로 ODE·flow, fixed point·bifurcation, Markov·Langevin·SDE와 SGD의 연속시간 근사를 다룬다. finite checkpoint interpolation과 실제 학습 path를 구분하고 noise covariance·autocorrelation을 근사 진단에 포함한다.
- A09-SYM은 문제·해설 32쌍으로 group action, orbit·stabilizer, invariant·equivariant, permutation·gauge symmetry와 seed 간 representation alignment를 다룬다. neuron·subspace·function identity를 분리하고 alignment를 held-out input과 intervention으로 검증한다.
- A09-LRN은 문제·해설 32쌍으로 hypothesis class·risk, bias–variance, generalization gap, VC·Rademacher·PAC와 probe 일반화를 다룬다. empirical gap·complexity bound·random-label control·functional intervention을 서로 다른 증거로 구분한다.
- 제4부는 순차 교재가 아니라 선택 모듈이다.

## 미해결 결정

본문 집필을 막는 미해결 결정은 없다. 다음 항목은 해당 단계에 들어가기 전에 정한다.

- PDF와 DOCX 배포 여부

## 검토 기록

| 날짜 | 범위 | 결과 | 후속 작업 |
|---|---|---|---|
| 2026-09-30 | 프로젝트 골격 | 명세, 목차, 문체·표기와 템플릿 생성 | 구조 검증 |
| 2026-09-30 | 구조 검증 | 단원 ID 중복 없음, 단계별 단원 수 일치, H1과 내부 링크 정상 | M00-01 집필 |
| 2026-09-30 | M00-01 | 수, 변수와 상수 본문·예제·문제 6개와 해설 작성 | M00-02 집필 |
| 2026-09-30 | M00-02 | 식, 등식, 방정식과 항등식 설명·문제 6개와 해설 작성 | M00-03 집필 |
| 2026-09-30 | M00-03 | 함수 표기, 정의역·공역·치역, 모델 표기 설명·문제 7개와 해설 작성 | M00-04 집필 |
| 2026-09-30 | M00-04 | 좌표, 함수 그래프, 절편과 그래프 해석 설명·문제 7개와 해설 작성 | M00-05 집필 |
| 2026-09-30 | M00-05 | 지수·로그의 역관계, 계산법칙과 AI 적용 설명·문제 7개와 해설 작성 | M00-06 집필 |
| 2026-09-30 | M00-06 | 인덱스, 합 기호, 평균·가중합과 이중 합 설명·문제 7개와 해설 작성 | M00-07 집필 |
| 2026-09-30 | M00-07 | 집합 연산, 조건문, 양화기와 필요·충분조건 설명·문제 7개와 해설 작성 | M00-08 집필 |
| 2026-09-30 | M00-08 | 함수 합성, 전단사, 역함수와 근사 복원 구분 설명·문제 7개와 해설 작성 | M00-09 집필 |
| 2026-09-30 | M00-09 | 스칼라·벡터·행렬, shape 검산과 activation 축 설명·문제 8개와 해설 작성 | M00-10 집필 |
| 2026-09-30 | M00-10 | 아핀 분류기, 소프트맥스, 평균 loss와 지식증류 수식 해독·문제 8개와 해설 작성 | M01-01 시작 |
| 2026-09-30 | M01-01 | 변화량, 평균변화율, 단위와 할선 기울기 설명·문제 7개와 해설 작성 | M01-02 집필 |
| 2026-09-30 | M01-02 | 극한, 좌극한·우극한, 연속성과 미분 준비 설명·문제 7개와 해설 작성 | M01-03 집필 |
| 2026-09-30 | M01-03 | 미분계수 정의, 접선, 좌우미분과 국소 민감도 설명·문제 7개와 해설 작성 | M01-04 집필 |
| 2026-09-30 | M01-04 | 도함수 부호, 증가·감소, 임계점과 국소 극값 설명·문제 7개와 해설 작성 | M01-05 집필 |
| 2026-09-30 | M01-05 | 합·곱·몫과 거듭제곱 미분, 평균 손실 미분 설명·문제 7개와 해설 작성 | M01-06 집필 |
| 2026-09-30 | M01-06 | 연쇄법칙, 중간변수, 계산 그래프와 경로 변화율 설명·문제 7개와 해설 작성 | M01-07 집필 |
| 2026-09-30 | M01-07 | 지수·로그 도함수, 음의 로그 손실과 로그합지수 설명·문제 7개와 해설 작성 | M01-08 집필 |
| 2026-09-30 | M01-08 | 리만 합, 정적분, 부호 있는 넓이와 누적 설명·문제 7개와 해설 작성 | M01-09 집필 |
| 2026-09-30 | M01-09 | 미적분 기본정리, 원시함수, 부정적분과 순변화 설명·문제 7개와 해설 작성 | M01-10 집필 |
| 2026-09-30 | M01-10 | 다변수 스칼라 함수, 편미분과 좌표 민감도 설명·문제 7개와 해설 작성 | M01-11 집필 |
| 2026-09-30 | M01-11 | 방향미분, 그래디언트, 최급방향과 좌표 의존성 설명·문제 7개와 해설 작성 | M01-12 집필 |
| 2026-09-30 | M01-12 | 일차·이차 Taylor 근사, 잔차와 다변수 선형화 설명·문제 7개와 해설 작성 | M01-13 집필 |
| 2026-09-30 | M01-13 | 유한차분, 절단·반올림오차와 누적 확인과제 작성 | M01 단계 교차 검토 |
| 2026-09-30 | M01 단계 교차 검토 | 13개 단원, 문제·해설 91쌍, 제목·수식·링크·용어 일관성 검사 통과 | M02-01 집필 |
| 2026-09-30 | M02-01 | 벡터 성분, 덧셈·뺄셈, 스칼라곱과 기하적 이동 설명·문제 7개와 해설 작성 | M02-02 집필 |
| 2026-09-30 | M02-02 | 선형결합, 생성공간, 소속 판정과 표현 가능성의 범위 설명·문제 7개와 해설 작성 | M02-03 집필 |
| 2026-09-30 | M02-01~02 배치 검토 | 문제·해설 14쌍, 제목·수식 구분자·내부 링크·용어 중복·문체 검사 통과 | M02-03 집필 |
| 2026-09-30 | M02-03 | 내적, Euclidean norm·거리, 각도, 직교와 정사영 설명·문제 7개와 해설 작성 | M02-04 집필 |
| 2026-09-30 | M02-04 | 행렬-벡터 곱, 행렬곱, 항등행렬과 데이터 행렬 관례 설명·문제 7개와 해설 작성 | M02-05 집필 |
| 2026-09-30 | M02-05 | 행렬의 선형변환 해석, 표준기저, 기하 변환과 합성 설명·문제 7개와 해설 작성 | M02-06 집필 |
| 2026-09-30 | M02-03~05 배치 검토 | M02 누적 5개 단원과 문제·해설 35쌍, 제목·수식 구분자·내부 링크·용어 중복·문체 검사 통과 | M02-06 집필 |
| 2026-09-30 | M02-06 | 연립방정식, 행 소거, 해의 분류와 역행렬 설명·문제 7개와 해설 작성 | M02-07 집필 |
| 2026-09-30 | M02-07 | 선형독립·종속, 기저, 좌표와 차원 설명·문제 7개와 해설 작성 | M02-08 집필 |
| 2026-09-30 | M02-08 | kernel, image, rank, nullity와 해의 존재·유일성 설명·문제 7개와 해설 작성 | M02-09 집필 |
| 2026-09-30 | M02-06~08 배치 검토 | M02 누적 8개 단원과 문제·해설 56쌍, 제목·수식 구분자·내부 링크·용어 중복·문체 검사 통과 | M02-09 집필 |
| 2026-09-30 | M02-09 | 직교·정규직교기저, 부분공간 정사영, Gram-Schmidt와 최소제곱 설명·문제 7개와 해설 작성 | M02-10 집필 |
| 2026-09-30 | M02-10 | determinant의 부피 배율, 부호, 가역성과 행 연산 성질 설명·문제 7개와 해설 작성 | M02-11 집필 |
| 2026-09-30 | M02-11 | 고유쌍, 특성방정식, 고유공간, 반복 적용과 대각화 설명·문제 7개와 해설 작성 | M02-12 집필 |
| 2026-09-30 | M02-09~11 배치 검토 | M02 누적 11개 단원과 문제·해설 77쌍, 제목·수식 구분자·내부 링크·용어 중복·문체 검사 통과 | M02-12 집필 |
| 2026-09-30 | M02-12 | 대칭행렬, 스펙트럼 정리, quadratic form과 PSD 설명·문제 7개와 해설 작성 | M02-13 집필 |
| 2026-09-30 | M02-13 | full·compact SVD, 특이방향, 행렬 norm과 저랭크 근사 설명·문제 7개와 해설 작성 | M02-14 집필 |
| 2026-09-30 | M02-14 | 중심화, 공분산, PCA, 설명분산비율과 재구성 설명·문제 7개와 해설 작성 | M02-15 집필 |
| 2026-09-30 | M02-12~14 배치 검토 | M02 누적 14개 단원과 문제·해설 98쌍, 제목·수식 구분자·내부 링크·용어 중복·문체 검사 통과 | M02-15 집필 |
| 2026-09-30 | M02-15 | vector·matrix norm, condition number, 상대오차 경계와 M02 누적 확인과제 작성 | M02 단계 교차 검토 |
| 2026-09-30 | M02 단계 교차 검토 | 15개 단원, 문제·해설 105쌍, 누적 과제·단계 통과 기준, 제목·선수지식 ID·수식·링크·용어·문체 검사 통과 | M03-01 집필 |
| 2026-09-30 | M03-01 | 추상 벡터공간의 공리, 다항식·함수·행렬 예시와 좌표 표현 설명·문제 7개와 해설 작성 | M03-02 집필 |
| 2026-09-30 | M03-02 | 선형사상, 기저별 행렬 표현, 합성, kernel과 image 설명·문제 7개와 해설 작성 | M03-03 집필 |
| 2026-09-30 | M03-03 | 좌표변환, similarity transformation, 좌표 의존성과 수동·능동 변환 설명·문제 7개와 해설 작성 | M03 배치 검토 |
| 2026-09-30 | M03-01~03 배치 검토 | 문제·해설 21쌍, 제목·선수지식 ID·수식 구분자·내부 링크·용어 중복·문체 검사 통과 | M03-04 집필 |
| 2026-09-30 | M03-04 | 불변량, 직교·순열 변환의 불변성과 equivariance 설명·문제 7개와 해설 작성 | M03-05 집필 |
| 2026-09-30 | M03-05 | 부분공간 합·교집합, 직합, 여공간과 정사영 분해 설명·문제 7개와 해설 작성 | M03-06 집필 |
| 2026-09-30 | M03-06 | 동치관계, coset, 몫공간, quotient map과 kernel·image 대응 설명·문제 7개와 해설 작성 | M03 배치 검토 |
| 2026-09-30 | M03-04~06 배치 검토 | M03 누적 6개 단원과 문제·해설 42쌍, 제목·선수지식 ID·수식 구분자·내부 링크·용어 중복·문체 검사 통과 | M03-07 집필 |
| 2026-09-30 | M03-07 | 쌍대공간, dual basis, covector 기저변환과 differential·gradient 구분 설명·문제 7개와 해설 작성 | M03-08 집필 |
| 2026-09-30 | M03-08 | bilinear·quadratic form, 대칭 부분, congruence와 attention score 설명·문제 7개와 해설 작성 | M03-09 집필 |
| 2026-09-30 | M03-09 | multilinear map, tensor 성분, tensor product·contraction과 배열 축 설명·문제 7개와 해설 작성 | M03 배치 검토 |
| 2026-09-30 | M03-07~09 배치 검토 | M03 누적 9개 단원과 문제·해설 63쌍, 제목·선수지식 ID·수식 구분자·내부 링크·용어 중복·문체 검사 통과 | M03-10 집필 |
| 2026-09-30 | M03-10 | total derivative의 remainder 정의, 편미분·방향미분·differential과 연쇄법칙 설명·문제 7개와 해설 작성 | M03-11 집필 |
| 2026-09-30 | M03-11 | Jacobian convention·shape, JVP, 합성, 신경망 층과 국소 민감도 설명·문제 7개와 해설 작성 | M03-12 집필 |
| 2026-09-30 | M03-12 | Hessian, second differential, Taylor 이차항, 임계점 판정과 HVP 설명·문제 7개와 해설 작성 | M03 배치 검토 |
| 2026-09-30 | M03-10~12 배치 검토 | M03 누적 12개 단원과 문제·해설 84쌍, 제목·선수지식 ID·수식 구분자·내부 링크·용어 중복·문체 검사 통과 | M03-13 집필 |
| 2026-09-30 | M03-13 | JVP·VJP의 타입과 shape, adjoint identity, forward·reverse 합성과 HVP 연결 설명·문제 7개와 해설 작성 | M03-14 집필 |
| 2026-09-30 | M03-14 | 자동미분, 계산 그래프, tangent·cotangent 전달, gradient 누적과 checkpointing 설명·문제 7개와 해설 작성 | M03-15 집필 |
| 2026-09-30 | M03-15 | 재매개화, 함수 동치, 선형 basis change, permutation·ReLU scaling symmetry 설명·누적 확인과제 포함 문제 7개와 해설 작성 | M03 배치 검토 |
| 2026-09-30 | M03-13~15 배치 검토 | M03 누적 15개 단원과 문제·해설 105쌍, 제목·수식 구분자·내부 링크·용어 중복·문체 검사 통과 | M03 단계 교차 검토 |
| 2026-09-30 | M03 단계 교차 검토 | 15개 단원, 문제·해설 105쌍, 누적 확인과제·단계 통과 기준, 제목·선수지식 ID·수식·링크·용어·문체 검사 통과 | M04-01 집필 |
| 2026-09-30 | M04-01 | 표본공간, outcome, 사건, 확률 공리, 여사건·포함배제와 경험적 빈도 설명·문제 7개와 해설 작성 | M04-02 집필 |
| 2026-09-30 | M04-02 | 조건부확률, 곱셈·전체확률법칙, Bayes 규칙, 독립·조건부독립 설명·문제 7개와 해설 작성 | M04-03 집필 |
| 2026-09-30 | M04-03 | 확률변수, PMF·CDF·PDF, 결합·주변·조건부분포 설명·문제 7개와 해설 작성 | M04 배치 검토 |
| 2026-09-30 | M04-01~03 배치 검토 | M04 누적 3개 단원과 문제·해설 21쌍, 제목·선수지식 ID·수식 구분자·내부 링크·용어 중복·문체 검사 통과 | M04-04 집필 |
| 2026-09-30 | M04-04 | 기댓값의 선형성, 분산·표준편차, 공분산·상관계수와 공분산행렬 설명·문제 7개와 해설 작성 | M04-05 집필 |
| 2026-09-30 | M04-05 | Bernoulli·categorical·binomial·Gaussian 분포와 신경망 출력의 분포 파라미터 해석 설명·문제 7개와 해설 작성 | M04-06 집필 |
| 2026-09-30 | M04-06 | 모집단·표본·통계량, 경험분포·sampling distribution, 표준오차와 독립 실험 단위 설명·문제 7개와 해설 작성 | M04 배치 검토 |
| 2026-09-30 | M04-04~06 배치 검토 | M04 누적 6개 단원과 문제·해설 42쌍, 제목·선수지식 ID·수식 구분자·내부 링크·용어 중복·문체 검사 통과 | M04-07 집필 |
| 2026-09-30 | M04-07 | estimator·estimate, 통계적 bias·variance·MSE decomposition, 불편성·일치성과 shrinkage 설명·문제 7개와 해설 작성 | M04-08 집필 |
| 2026-09-30 | M04-08 | 회귀·분류, population·empirical risk, Bayes predictor, 선형·logistic·softmax regression과 평가 metric 설명·문제 7개와 해설 작성 | M04-09 집필 |
| 2026-09-30 | M04-09 | confidence coverage, z·t interval, bootstrap standard error·percentile interval과 paired·clustered resampling 설명·문제 7개와 해설 작성 | M04 배치 검토 |
| 2026-09-30 | M04-07~09 배치 검토 | M04 누적 9개 단원과 문제·해설 63쌍, 제목·선수지식 ID·수식 구분자·내부 링크·용어 중복·문체 검사 통과 | M04-01~09 교차 검토 |
| 2026-09-30 | M04-01~09 교차 검토 | 9개 단원, 문제·해설 63쌍, 단원 상태·제목·선수지식 ID·수식·목차 및 단원 링크·용어·문체 검사 통과 | M04-10 집필 |
| 2026-09-30 | M04-10 | 귀무·대립가설, p-value, Type I·II error, power, Bonferroni·BH 다중비교 correction 설명·문제 7개와 해설 작성 | M04-11 집필 |
| 2026-09-30 | M04-11 | likelihood·log-likelihood·NLL, Bernoulli·Gaussian MLE와 회귀·분류 loss 연결 설명·문제 7개와 해설 작성 | M04-12 집필 |
| 2026-09-30 | M04-12 | self-information, entropy·cross entropy, one-hot·soft-target loss, perplexity와 predictive entropy 설명·문제 7개와 해설 작성 | M04 배치 검토 |
| 2026-09-30 | M04-10~12 배치 검토 | M04 누적 12개 단원과 문제·해설 84쌍, 제목·선수지식 ID·수식 구분자·내부 링크·용어 중복·문체 검사 통과 | M04-13 집필 |
| 2026-09-30 | M04-13 | KL 방향·support mismatch·비대칭성·비음수성, cross entropy decomposition과 증류 해석 한계 설명·문제 7개와 해설 작성 | M04-14 집필 |
| 2026-09-30 | M04-14 | joint·conditional entropy, mutual information의 KL·entropy 표현, data processing과 추정 한계 설명·문제 7개와 해설 작성 | M04-15 집필 |
| 2026-09-30 | M04-15 | binary·multiclass calibration, reliability diagram·ECE, proper score·sharpness·temperature scaling 설명·문제 7개와 해설 작성 | M04 배치 검토 |
| 2026-09-30 | M04-13~15 배치 검토 | M04 누적 15개 단원과 문제·해설 105쌍, 제목·선수지식 ID·수식 구분자·내부 링크·용어 중복·문체 검사 통과 | M04-16 집필 |
| 2026-09-30 | M04-16 | association·prediction·causation, confounder·mediator·collider, potential outcome과 모델 개입 증거 설명·문제 7개와 해설 작성 | M04-17 집필 |
| 2026-09-30 | M04-17 | estimand·실험 단위·control·split·seed·paired design·재현성 설명과 M04 누적 확인과제 포함 문제 7개와 해설 작성 | M04 배치 검토 |
| 2026-09-30 | M04-16~17 배치 검토 | M04 17개 단원과 문제·해설 119쌍, 제목·선수지식 ID·수식 구분자·내부 링크·용어 중복·문체 검사 통과 | M04 단계 교차 검토 |
| 2026-09-30 | M04 단계 교차 검토 | 17개 단원, 문제·해설 119쌍, 누적 확인과제·단계 통과 기준, 제목·선수지식 ID·수식·링크·용어·문체 검사 통과 | M01~M04 완료 감사 |
| 2026-09-30 | M01~M04 완료 감사 | 60개 단원, 문제·해설 420쌍, frontmatter·H1·수식 구분자·선수지식·목차 및 내부 링크·누적 확인과제·용어 중복 검사 통과 | N05 기준 확정 |
| 2026-10-01 | N05 집필 전 기준 검토 | 교육용 기준 아키텍처, 구성요소 등급, 자료 우선순위와 28개 단원 목차 확정 | N05-01 집필 |
| 2026-10-01 | N05 실행 기반 | Python 3.12.14, PyTorch 2.13.0+cpu, NumPy 2.5.3 환경 진단과 단일 원본·timeout·자원 상한·결과 삽입 구현 | 파일럿 집필 |
| 2026-10-01 | N05-01~03 파일럿 | tensor graph·neuron·MLP 설명, 문제·해설 18쌍, 실행 예제 3개와 N05 test 10개 작성 | strict build 검증 |
| 2026-10-01 | N05 파일럿 검증 | 전체 73개 단원·읽기 셀 486개, 예제 8.82초, broken link 0개, checklist 노출 0개로 strict build 통과 | N05-04 집필 |
| 2026-10-01 | N05-04~06 | activation·gating, stable softmax·cross entropy, scalar backpropagation 설명, 문제·해설 18쌍, 실행 예제 3개와 N05 test 7개 추가 | strict build 검증 |
| 2026-10-01 | N05-07~08 | mini-batch mean gradient, gradient descent update, momentum·AdamW와 optimizer state 설명, 문제·해설 12쌍, 실행 예제 2개와 N05 test 4개 추가 | strict build 검증 |
| 2026-10-01 | N05-09~10 | PyTorch shape·broadcast·dtype, autograd·JVP·VJP 설명, 문제·해설 12쌍, 실행 예제 2개와 N05 test 4개 추가 | N05-01~10 단계 검토 |
| 2026-10-01 | N05-01~10 단계 검토 | Stable core 분류와 공식 API 근거 재확인, 누적 확인과제·CPU 예산·source audit 통과 | strict build와 브라우저 검수 |
| 2026-10-01 | N05-11~13 | toy tokenizer, embedding·unembedding, 위치정보·RoPE 설명, 문제·해설 18쌍, 실행 예제 3개와 N05 test 6개 추가 | strict build 검증 |
| 2026-10-01 | N05-14~16 | Q·K·V projection, causal scaled dot-product attention, MHA·MQA·GQA 설명, 문제·해설 18쌍, 실행 예제 3개와 N05 test 4개 추가 | strict build 검증 |
| 2026-10-01 | N05-17~19 | residual stream, LayerNorm·RMSNorm과 residual 순서, dense MLP·SwiGLU·expert routing 설명, 문제·해설 18쌍, 실행 예제 3개와 N05 test 6개 추가 | strict build 검증 |
| 2026-10-01 | N05-20~22 | tiny decoder block, architecture diff, next-token objective, causal inference와 KV cache 설명, 문제·해설 18쌍, 실행 예제 3개와 N05 test 6개 추가 | N05-20 architecture 재검토와 strict build 검증 |
| 2026-10-01 | N05-23~25 | greedy·temperature·top-k·top-p decoding, CoT의 관찰 지위, forward hook과 최소 activation 수집 설명, 문제·해설 18쌍, 실행 예제 3개와 N05 test 6개 추가 | strict build 검증 |
| 2026-10-01 | N05-26~28 | activation gradient·intervention, checkpoint state, 한 token의 누적 경로 설명, 문제·해설 20쌍, 실행 예제 3개와 N05 test 6개 추가 | N05 단계 감사와 strict build 검증 |
| 2026-10-01 | Phase 3 GPU 기반 | Python 3.12.14, PyTorch 2.13.0+cu132, Transformers 5.17.0 분리 환경과 CUDA 결정성 진단 통과 | Pythia cache·runner 검증 |
| 2026-10-01 | Pythia 70M·160M·410M gate | immutable revision, hook·선택 activation·최소 gradient, VRAM·artifact·timeout manifest 검증 통과 | I06-01~03 집필 |
| 2026-10-01 | I06-01~03 | 질문 설계, activation dataset, 분포·기초 통계 설명과 문제·해설 18쌍 작성 | CPU·로컬 GPU site 검증 |
| 2026-10-01 | I06-04~06 | neuron 기저 의존성, PCA·SVD, linear probe 설명과 CPU 예제 3개·문제 해설 18쌍 작성 | probe control 배치 |
| 2026-10-01 | I06-07~09 | selectivity, CCA·CKA·RSA, feature visualization 설명과 CPU 예제 3개·문제 해설 18쌍 작성 | superposition 배치 |
| 2026-10-01 | I06-10~12 | superposition, sparse coding, SAE와 reconstruction·sparsity·dead feature 평가 설명·CPU 예제 3개·문제 해설 18쌍 작성 | 안정성·보고서 배치 |
| 2026-10-01 | I06-13~15 | feature·subspace 안정성, claim ledger, 종합 표현 보고서와 CPU 예제 3개·문제 해설 18쌍 작성 | I06 단계 감사 |
| 2026-10-01 | I06 단계 감사 | 15개 단원, 문제·해설 90쌍, CPU 예제 12개, Pythia 3종 GPU manifest, 82개 test, 113개 HTML 페이지와 broken link·checklist 노출 0개 검증 | I07-01 집필 |
| 2026-10-01 | I07-01~03 | 민감도, gradient·gradient×input, integrated gradients와 baseline 설명·CPU 예제 3개·문제 해설 18쌍 작성 | perturbation·개입 배치 |
| 2026-10-01 | I07-04~06 | perturbation, 관찰·개입, ablation과 redundancy 설명·CPU 예제 3개·문제 해설 18쌍 작성 | activation patching 배치 |
| 2026-10-01 | I07-07~09 | activation patching, causal tracing, path patching 설명·CPU 예제 3개·Pythia-160M patch·문제 해설 18쌍 작성 | circuit 표현 배치 |
| 2026-10-01 | I07-10~12 | direct logit attribution, circuit graph, necessity·sufficiency 설명·CPU 예제 3개·문제 해설 18쌍 작성 | mediation·control 배치 |
| 2026-10-01 | I07-13~15 | mediation, off-manifold intervention, paired control·통계 검증 설명·CPU 예제 3개·문제 해설 18쌍 작성 | CoT·종합 실습 배치 |
| 2026-10-01 | I07-16~17 | CoT faithfulness와 작은 circuit 종합 보고서·CPU 예제 2개·문제 해설 12쌍 작성 | I07 단계 감사 |
| 2026-10-01 | I07 단계 감사 | 17개 단원, 문제·해설 102쌍, CPU 예제 17개, Pythia-160M activation patching, 101개 test, 130개 HTML 페이지와 broken link·checklist 노출 0개 검증 | I08-01 집필 |
| 2026-10-01 | I08-01~03 | checkpoint 연구 계약, parameter·function distance, Procrustes·CKA alignment 설명·CPU 예제 3개·문제 해설 18쌍 작성 | optimizer dynamics 배치 |
| 2026-10-01 | I08-04~06 | gradient flow, mini-batch noise·optimizer state, Hessian spectrum·HVP 설명·CPU 예제 3개·문제 해설 18쌍 작성 | loss path·feature 배치 |
| 2026-10-01 | I08-07~09 | loss path·mode connectivity, influence function, feature emergence의 네 증거 설명·CPU 예제 3개·문제 해설 18쌍 작성 | grokking·seed 배치 |
| 2026-10-01 | I08-10~11 | grokking transition의 측정 한계, paired seed·data-order 설계 설명·CPU 예제 2개·문제 해설 12쌍 작성 | 데이터 귀인·종합 실습 배치 |
| 2026-10-01 | I08-12~13 | TracIn 데이터 귀인과 feature 생애 보고서·CPU 예제 2개·Pythia-160M 여섯 checkpoint·문제 해설 12쌍 작성 | I08 단계 감사 |
| 2026-10-01 | I08 단계 감사 | 13개 단원, 문제·해설 78쌍, CPU 예제 13개, Pythia-160M 여섯 checkpoint manifest, 117개 test, 143개 HTML 페이지와 broken link·checklist 노출 0개 검증 | A09-GEO-01 집필 |
| 2026-10-01 | A09-GEO-01~03 | manifold·local coordinate, tangent·cotangent space, Riemannian metric·curve length 설명과 문제·해설 12쌍 작성 | pullback·geodesic 배치 |
| 2026-10-01 | A09-GEO-04~06 | Jacobian pullback metric, connection·geodesic, intrinsic·extrinsic curvature 설명과 문제·해설 12쌍 작성 | 분석 함정·종합 실습 배치 |
| 2026-10-01 | A09-GEO-07~08 | activation manifold 추정의 함정과 국소 표현 기하 분석 계약·문제 해설 8쌍 작성 | A09-GEO 모듈 감사 |
| 2026-10-01 | A09-GEO 모듈 감사 | 8개 단원, 문제·해설 32쌍, 117개 test, 151개 HTML 페이지, broken link·asset·checklist 노출 0개와 첫·수식·종합 단원 브라우저 검수 통과 | A09-DYN-01 집필 |
| 2026-10-01 | A09-DYN-01~03 | ODE·flow, fixed point·linear stability, phase portrait·bifurcation 설명과 문제·해설 12쌍 작성 | 확률과정 배치 |
| 2026-10-01 | A09-DYN-04~06 | Markov process, Langevin dynamics, Itô SDE 입문과 문제·해설 12쌍 작성 | SGD 근사·종합 실습 배치 |
| 2026-10-01 | A09-DYN-07~08 | SGD 연속시간 근사의 가정·진단과 학습 궤적 분석 계약·문제 해설 8쌍 작성 | A09-DYN 모듈 감사 |
| 2026-10-01 | A09-DYN 모듈 감사 | 8개 단원, 문제·해설 32쌍, 117개 test, 159개 HTML 페이지, broken link·asset·checklist 노출 0개와 첫·종합 단원 브라우저 검수 통과 | A09-SYM-01 집필 |
| 2026-10-01 | A09-SYM-01~03 | group action, orbit·stabilizer, invariant·equivariant map 설명과 문제·해설 12쌍 작성 | model symmetry 배치 |
| 2026-10-01 | A09-SYM-04~06 | permutation, scaling·rotation gauge, representation theory 입문과 문제·해설 12쌍 작성 | alignment·종합 실습 배치 |
| 2026-10-01 | A09-SYM-07~08 | model equivalence class와 seed 간 표현 정렬 계약·문제 해설 8쌍 작성 | A09-SYM 모듈 감사 |
| 2026-10-01 | A09-SYM 모듈 감사 | 8개 단원, 문제·해설 32쌍, 117개 test, 167개 HTML 페이지, broken link·asset·checklist 노출 0개와 첫·종합 단원 브라우저 검수 통과 | A09-LRN-01 집필 |
| 2026-10-01 | A09-LRN-01~03 | hypothesis class·risk, squared-loss bias–variance, generalization gap과 문제·해설 12쌍 작성 | capacity 배치 |
| 2026-10-01 | A09-LRN-04~06 | VC dimension, Rademacher complexity, PAC learning과 문제·해설 12쌍 작성 | probe 일반화·종합 실습 배치 |
| 2026-10-01 | A09-LRN-07~08 | probe 일반화 축과 complexity·generalization 분석 계약·문제 해설 8쌍 작성 | A09-LRN 모듈 감사 |
| 2026-10-01 | A09-LRN 모듈 감사 | 8개 단원, 문제·해설 32쌍, 117개 test, 175개 HTML 페이지, broken link·asset·checklist 노출 0개와 첫·종합 단원 브라우저 검수 통과 | A09-KER-01 집필 |
