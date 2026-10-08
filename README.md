# 모델 해석을 위한 수학과 방법론

[한국어로 읽기](https://leeklim.github.io/ai-math-guide/) · [Read in English](https://leeklim.github.io/ai-math-guide/en/)

<div class="home-intro" markdown="1">

**AI 논문을 읽다가 수식에서 막힐 때, 필요한 개념부터 공부하세요.**

미분 기호와 행렬부터 Transformer 계산, 모델 내부 표현과 인과적 개입까지 설명합니다. 그림으로 관계를 확인하고, 예제와 문제·해설로 이해를 점검할 수 있습니다. 제2부부터는 Python·PyTorch 코드와 실행 결과를 함께 읽습니다.

한국어·영어 전권 무료 공개 · 로그인 없이 웹에서 읽기 · 199개 단원

</div>

## 읽기 시작 { #_4 }

관심 있는 경로에서 시작하세요. 각 단원에서 선수지식을 확인하고 필요한 기초로 돌아갈 수 있습니다.

<div class="home-paths" markdown="1">

<div class="home-path" markdown="1">

### 수학 기호부터

변수와 함수, 합 기호, 미분·적분을 읽는 단계에서 시작합니다. 벡터·행렬과 확률로 이어집니다.

[첫 단원 읽기](part-1-foundations/M00/M00-01-numbers-variables.md){ .md-button .md-button--primary }

</div>

<div class="home-path" markdown="1">

### Transformer 계산부터

텐서와 계산 그래프에서 attention, residual stream과 역전파까지 계산 순서를 따라갑니다. 기초 미적분과 행렬 연산을 알고 있다면 이 경로를 고르세요.

[신경망 계산 읽기](part-2-neural-computation/N05/N05-01-tensors-computation-graphs.md){ .md-button }

</div>

<div class="home-path" markdown="1">

### 모델 해석 실험부터

표현을 관찰하는 방법과 내부 계산에 개입하는 실험을 구분합니다. 신경망 계산을 알고 있다면 activation patching 단원부터 살펴보세요.

[개입 실험 읽기](part-3-interpretability/I07/I07-07-activation-patching.md){ .md-button }

</div>

</div>

[전체 학습경로](01-CURRICULUM.md) · [용어집](04-GLOSSARY.md)

## 그림과 설명 미리 보기 { #lesson-previews }

아래는 본문에서 사용하는 그림입니다. 각 링크에서 정의와 계산 예제, 연습문제와 해설을 함께 읽을 수 있습니다. 모바일에서는 넓은 그림을 좌우로 스크롤하세요.

### 특이값분해는 어떤 변환인가

SVD의 세 행렬을 입력 좌표변환, 축별 배율, 출력 좌표변환으로 나누어 설명합니다. 같은 벡터와 단위원의 변화를 단계마다 비교하세요.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![A unit circle and a vector passing through the three stages of singular value decomposition](figures/assets/M02/M02-13-svd-three-stage.svg)

<figcaption>좌표를 바꾸는 단계와 길이를 바꾸는 단계를 구분해 행렬의 작용을 읽습니다.</figcaption>
</figure>

[특이값분해 단원 읽기](part-1-foundations/M02/M02-13-singular-value-decomposition.md)

### Attention mask는 계산의 어디에 적용되는가

미래 토큰을 막는 causal mask를 score에 더한 뒤, 행별 softmax로 attention weight를 계산합니다. 차단한 score가 최종 가중치 0으로 이어지는 과정을 확인하세요.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Raw attention scores, causally masked scores, and row-wise softmax weights for four tokens](figures/assets/N05/N05-15-causal-mask-matrices.svg)

<figcaption>같은 토큰 행을 따라 score, 마스크 적용, 가중치 계산을 비교합니다.</figcaption>
</figure>

[Causal attention 단원 읽기](part-2-neural-computation/N05/N05-15-causal-scaled-dot-product-attention.md)

### Activation patching에서는 무엇을 비교하는가

Clean run에서 얻은 activation을 corrupted run의 지정한 위치에 넣고, 이후 계산을 실행합니다. 기준 실행과 개입 실행을 구분하고, 측정한 효과로 어떤 주장을 할 수 있는지 살펴보세요.

<figure class="lesson-figure lesson-figure--wide" markdown="1">

![Clean, corrupted, and patched model runs with a clean activation inserted at a specified node](figures/assets/I07/I07-07-three-runs.svg)

<figcaption>세 실행의 입력과 개입 위치를 구분한 뒤 출력 차이를 해석합니다.</figcaption>
</figure>

[Activation patching 단원 읽기](part-3-interpretability/I07/I07-07-activation-patching.md)

## 네 부분 { #_2 }

| 부분 | 범위 | 목적 |
|---|---|---|
| 제1부 | 0~4단계 | 수식, 미적분, 선형대수, 확률·통계·정보이론 |
| 제2부 | 5단계 | 신경망과 Transformer의 실제 계산 |
| 제3부 | 6~8단계 | 표현, 인과, 기계론, 학습 동역학 해석 |
| 제4부 | 9단계 | 기하학, 동역학, 대칭성, 학습이론 등 선택 심화 |

전권을 처음부터 읽거나, [전체 학습경로](01-CURRICULUM.md)에서 필요한 단원을 찾아 읽을 수 있습니다. 본문에는 문제·해설 1,154쌍과 그림 1,355개가 있습니다. 실습을 실행하려면 별도의 환경 설정이 필요하지만 웹 교재를 읽는 데에는 설치가 필요하지 않습니다.

## 자료 소개와 오류 제보 { #about-this-guide }

개인 학습에서 출발해 AI의 도움으로 작성·개정한 교재입니다. 한영 원문 대조, 링크·수식 표기·그림 자산 검사와 코드 실행 결과 확인을 진행했습니다. 이 검사를 외부 전문가의 동료 심사나 모든 설명의 무오류 보증으로 해석하지는 않습니다.

설명이 불분명하거나 계산·표기에 오류가 있으면 [GitHub Issues](https://github.com/leeklim/ai-math-guide/issues)에 해당 단원의 주소와 문제 구절을 남겨주세요. 문제·해설도 함께 확인할 수 있습니다.

## 기준 문서

다음 문서가 프로젝트의 기준이다. 내용이 충돌하면 번호가 앞선 문서를 우선하되, 실제 학습 내용에 관한 세부 규칙은 해당 전문 문서를 따른다.

1. [프로젝트 명세](00-PROJECT-SPEC.md)
2. [전체 교육과정](01-CURRICULUM.md)
3. [문체와 표기 규칙](02-STYLE-AND-NOTATION.md)
4. [진행 현황](03-PROGRESS.md)
5. [용어집](04-GLOSSARY.md)
6. [N05 아키텍처와 자료 기준](05-N05-ARCHITECTURE-BASELINE.md)
7. [N05 실행 환경](N05-ENVIRONMENT.md)
8. [GPU·Pythia 실행 환경](GPU-ENVIRONMENT.md)
9. [단원 템플릿](templates/lesson-template.md)
10. [N05 단원 템플릿](templates/n05-lesson-template.md)

## 제작 원칙

- Markdown을 유일한 원본으로 관리한다.
- 수식은 LaTeX 표기를 사용한다.
- HTML은 Markdown에서 생성하며 직접 편집하지 않는다.
- 각 단원은 선수지식, 개념, 예제, 문제, 해설과 통과 기준을 갖는다.
- 제2부부터 실행 가능한 실습을 추가한다.
- 용어와 수학 표기는 프로젝트 전체에서 통일한다.
- `기호와 용어` 표의 Common spoken reading은 실제 영어 학술 발화로 쓰고 자동 검사한다.
- 새로운 단원을 완료할 때마다 진행표와 용어집을 갱신한다.

## 현재 상태

M00~M04의 70개 기초 단원, N05의 28개 단원, I06의 15개 단원, I07의 17개 단원, I08의 13개 단원과 A09 선택 심화 단원 56개를 포함한 전체 199개 단원을 집필했다. 자세한 상태는 [진행 현황](03-PROGRESS.md)에 기록한다.

## 로컬 HTML 검수

사이트는 MkDocs Material과 Python 3.12를 사용한다. Markdown 원본은 현재 위치에 두고, build script가 `.build/docs`에 공개용 사본을 만든다. `.build/site`의 HTML과 staging 파일은 Git에서 제외한다.

Windows PowerShell에서 처음 한 번 가상환경과 dependency를 설치한다.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\scripts\setup_n05.ps1
```

교재용 수치 그래프를 새로 만들거나 저장된 SVG의 재현성을 검사할 때만 그림 dependency를 추가로 설치한다. 완성된 HTML을 빌드하고 읽는 데에는 필요하지 않다.

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-figures.txt
.\.venv\Scripts\python.exe scripts/figures.py generate
.\.venv\Scripts\python.exe scripts/figures.py check --reproduce
```

개념도와 생성된 그래프의 최종 SVG는 `figures/assets`에 있으며, `figures/manifest.json`이 단원과 생성 코드를 연결한다. 전권 단원 등급은 `revision/visual-audit.csv`에, 실제 개념별 설명·그림 필요성과 진행 상태는 `revision/concept-audit.csv`에 기록한다.

전권 199개 단원·976개 핵심개념의 본문 설명과 시각화 통합 검증을 완료했다. 기존 본문과 문제·해설 1,154쌍을 보존하며 교재용 SVG 1,355개를 배치했다. 개념도 661개는 SVG 자체가 원본이며, 수치 그림 694개는 저장된 코드로 재생성할 수 있다. 그림·캡션과 필요한 짧은 연결 문장은 해당 설명 가까이에 두었으며, 그림 필요성과 제외 근거는 개념 대장에 기록했다. 본문 상태는 `explanation_status`, 본문과 그림의 통합 상태는 `status`로 구분한다.

그림 단계에서는 단원 담당자가 읽기·진단·설계·제작·자체 검수를 이어가고 서로 다른 단원을 병렬 진행한다. 조정자가 공유 자산 목록과 대장·빌드를 통합한다. 신규·수정 그림은 모두 직접 렌더링하고 변경 페이지의 HTML 반영을 확인한다. 공통 유형의 대표 페이지에서 데스크톱·모바일과 밝은·어두운 화면을 확인하며, 넓고 복잡하거나 새로운 배치는 개별 검수를 추가한다. M00~M04 각각, N05의 전·후반 각각, I06~I08 각각, A09의 7개 모듈 각각이 끝나면 상세 대장과 사이트 준비·strict HTML build를 수행한다. 전권 검사는 최종 통합 단계에서 수행하며 작은 파일 묶음마다 반복하지 않는다.

```powershell
.\.venv\Scripts\python.exe scripts/concepts.py check
# 전권 본문 완료 시 사용한다. 미완료 개념이 남아 있으면 실패한다.
.\.venv\Scripts\python.exe scripts/concepts.py check --require-explanations
# 필수 그림 검수까지 포함한 전권 통합 완료 시 사용한다.
.\.venv\Scripts\python.exe scripts/concepts.py check --require-verified
```

자동 검사 테스트, 원본 감사, production build와 생성물 검증을 한 번에 실행하는 통합 검사 명령은 다음과 같다.

```powershell
.\scripts\build_site.ps1
```

로컬 preview를 `127.0.0.1:8000`에서 연다.

```powershell
.\scripts\preview_site.ps1 -SkipBuild
```

GitHub Actions는 build와 검증을 수행한다. `main`의 push와 수동 실행에서 검증을 통과하면 `.build/site`만 GitHub Pages에 배포한다. Pull request에서는 검사만 수행한다. 공개 주소는 https://leeklim.github.io/ai-math-guide/ 이며, 운영 설정과 배포 기록은 [사이트 운영 안내](site/README.md)에 둔다.
