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

M00~M04의 70개 기초 단원, N05의 28개 단원, I06의 15개 단원, I07의 17개 단원과 I08의 13개 단원을 집필했다. 자세한 상태는 [진행 현황](03-PROGRESS.md)에 기록한다.

## 로컬 HTML 검수

사이트는 MkDocs Material과 Python 3.12를 사용한다. Markdown 원본은 현재 위치에 두고, build script가 `.build/docs`에 공개용 사본을 만든다. `.build/site`의 HTML과 staging 파일은 Git에서 제외한다.

Windows PowerShell에서 처음 한 번 가상환경과 dependency를 설치한다.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\scripts\setup_n05.ps1
```

자동 검사 테스트, 원본 감사, production build와 생성물 검증을 한 번에 실행한다.

```powershell
.\scripts\build_site.ps1
```

로컬 preview를 `127.0.0.1:8000`에서 연다.

```powershell
.\scripts\preview_site.ps1 -SkipBuild
```

GitHub Actions는 같은 build와 검증만 수행한다. GitHub Pages deployment는 비활성 상태이며, 검수가 끝날 때까지 사이트를 공개하지 않는다.
