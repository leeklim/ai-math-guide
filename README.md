# 모델 해석을 위한 수학과 방법론

수학 기호를 읽는 단계에서 시작해 신경망 내부 표현, 인과적 개입, 학습 동역학과 고급 이론까지 공부하는 교육과정이다.

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

## 네 부분

| 부분 | 범위 | 목적 |
|---|---|---|
| 제1부 | 0~4단계 | 수식, 미적분, 선형대수, 확률·통계·정보이론 |
| 제2부 | 5단계 | 신경망과 Transformer의 실제 계산 |
| 제3부 | 6~8단계 | 표현, 인과, 기계론, 학습 동역학 해석 |
| 제4부 | 9단계 | 기하학, 동역학, 대칭성, 학습이론 등 선택 심화 |

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
