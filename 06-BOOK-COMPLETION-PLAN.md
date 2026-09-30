# 제2부~제4부 완주 실행 명세

## 0. 문서 상태

| 항목 | 값 |
|---|---|
| 기준 커밋 | `819ba380317f3533e73da0dddbb3dccbb55f5e9a` |
| 기준 브랜치 | `main` |
| 원격 저장소 | `https://github.com/leeklim/ai-math-guide.git` |
| 기준 확인일 | 2026-10-01 |
| 적용 범위 | N05-04부터 A09-CAU-08까지의 집필·실습·사이트 통합 |
| 이 문서의 목적 | 한 번의 후속 Goal이 Phase gate를 차례로 통과하며 전권을 완주하게 하는 실행 계약 |

이 문서는 단원 내용을 새로 정하지 않는다. 단원 ID·제목·순서의 단일 기준은 [전체 교육과정](01-CURRICULUM.md)이다. 문체·표기·Common spoken reading은 [문체와 표기 규칙](02-STYLE-AND-NOTATION.md), 단원 내용의 완료 조건은 [프로젝트 명세](00-PROJECT-SPEC.md)를 따른다. 이 문서는 그 기준을 어떤 순서로 구현하고 어떻게 검증할지를 정한다.

기준 문서 사이에 충돌이 생기면 `README.md`의 우선순위를 적용한다. 이 문서가 기존 기준과 충돌하거나 새로운 내용 결정을 요구하면 작업자가 임의로 고치지 않고 이 문서의 결정 기록에 열린 항목으로 남긴다.

## 1. 현재 기준선과 보존 조건

### 1.1 완료 상태

| 범위 | 완료 | 전체 | 상태 |
|---|---:|---:|---|
| M00~M04 | 70 | 70 | 완료 |
| N05 | 3 | 28 | N05-01~03 완료 |
| I06 | 0 | 15 | 계획 |
| I07 | 0 | 17 | 계획 |
| I08 | 0 | 13 | 계획 |
| A09 7개 모듈 | 0 | 56 | 계획 |
| 합계 | 73 | 199 | 126개 단원 남음 |

현재 기준선에는 다음 실행 계약이 있다.

- Markdown이 유일한 본문 원본이다. HTML은 `.build` 아래에서 생성한다.
- 기존 `.venv`는 Python 3.12, NumPy 2.5.3, PyTorch 2.13.0 CPU 환경이다.
- N05 코드는 `labs/N05`의 `.py` 파일이 단일 원본이다.
- `scripts/run_n05_examples.py`가 예제를 실행해 `.build/n05/results`에 결과를 만들고, `scripts/site.py`가 source hash를 대조한 뒤 HTML에 코드와 결과를 넣는다.
- `scripts/build_site.ps1`은 환경 진단, 단위 테스트, N05 예제 실행, source audit, strict MkDocs build와 생성 사이트 검증을 순서대로 수행한다.
- GitHub Actions는 CPU 환경에서 같은 검사를 수행하며 사이트를 배포하지 않는다.

### 1.2 기준선에서 그대로 보존할 것

- M00~M04의 70개 완료 단원과 N05-01~03의 본문은 후속 범위의 필요만으로 다시 쓰지 않는다.
- `.venv`를 GPU 환경으로 바꾸지 않는다. CPU wheel과 CUDA wheel을 같은 환경에 설치하지 않는다.
- `00-PROJECT-SPEC.md`, `01-CURRICULUM.md`, `02-STYLE-AND-NOTATION.md`의 역할을 합치거나 복제하지 않는다.
- HTML, 실행 결과, 모델 weight, cache와 전체 activation은 Git에 넣지 않는다.
- 기존 단원의 집필자 점검표는 Markdown 원본에 남기고 공개용 staging과 HTML에서만 제거한다.
- 기존 기준선의 strict build가 실패한 상태에서는 새 단원 집필을 시작하지 않는다.

### 1.3 현재 구현에서 확장해야 할 지점

현재 `scripts/site.py`는 M00~M04의 70개와 N05의 연속 prefix만 안다. `N05_EXAMPLES`와 `N05_LAB_PATHS`도 N05-01~03에 고정돼 있고, 생성 사이트 검증은 모든 작성된 N05 단원이 이 mapping에 있다고 가정한다. N05-04를 추가하기 전에 다음을 일반화해야 한다.

1. 작성된 단원은 단계별 연속 prefix로 발견하되 계획된 전체 수를 넘지 않게 한다.
2. 실행 예제가 있는 단원만 예제 registry와 marker 검사를 받게 한다.
3. I06, I07, I08과 A09 모듈을 단계 registry에 추가할 수 있게 한다.
4. source lesson 수, nav 수와 HTML 수를 현재 작성 상태에서 계산하고 Phase 8에서 정확히 199개인지 검사한다.
5. CPU 예제와 로컬 GPU 예제를 서로 다른 runner와 gate로 분리한다.

이 변경은 Phase 1의 첫 작업이다. 기존 73개 단원에 대한 검사 강도를 낮추지 않는다.

## 2. 전체 Phase 지도

| Phase | 단원 범위 | 새 단원 수 | 주된 산출물 | 다음 단계로 가는 gate |
|---|---|---:|---|---|
| 0 | 집필 없음 | 0 | 이 실행 명세와 기준선 검증 | 사용자 명세 검토 완료 |
| 1 | N05-04~N05-10 | 7 | 신경망 학습 계산과 확장 가능한 site registry | CPU strict build, N05-10 기준 재검토 |
| 2 | N05-11~N05-28 | 18 | tiny decoder 전체, hook·checkpoint 기반 | N05 28/28, 누적 실습과 단계 감사 |
| 3 | I06-01~I06-03 | 3 | 별도 GPU 환경, Pythia runner·manifest, 표현 분석 파일럿 | 70M smoke, 160M 필수 실험, CPU build 독립성 |
| 4 | I06-04~I06-15 | 12 | 표현 분석·probe·SAE 과정 | I06 15/15와 표현 보고서 |
| 5 | I07-01~I07-17 | 17 | 귀인·개입·circuit 과정 | I07 17/17과 작은 circuit 실습 |
| 6 | I08-01~I08-13 | 13 | checkpoint·학습 동역학 과정 | I08 13/13과 feature 생애 실습 |
| 7 | A09-GEO~A09-CAU | 56 | 선택 심화 7개 모듈 전체 | 각 모듈 8/8, A09 56/56 |
| 8 | 전권 | 0 | 199개 단원 통합 감사와 최종 보고 | 프로젝트 완료 조건 전부 통과 |

Phase 7의 모듈 순서는 교육과정에 적힌 `GEO → DYN → SYM → LRN → KER → RMT → CAU`를 사용한다. 9단계는 선택형이지만 이번 완주 범위에서는 일곱 모듈을 모두 작성한다.

## 3. 공통 작업 순환

### 3.1 배치 크기와 자동 진행

한 배치는 연속한 1~3개 단원이다. 각 배치는 다음 순서로 처리한다.

1. `01-CURRICULUM.md`에서 ID·제목·직접 선수지식을 확인한다.
2. 해당 개념의 1차 자료와 공식 구현을 확인하고 확인일을 기록한다.
3. 단원 Markdown, 실행 코드, 단위 테스트와 필요한 fixture를 함께 작성한다.
4. 단원별 검사와 source audit를 실행한다.
5. CPU 필수 실습과 strict site build를 실행한다.
6. 생성 HTML에서 수식, 표, 코드, 해설 접기와 내부 링크를 확인한다.
7. `03-PROGRESS.md`와 `04-GLOSSARY.md`를 현재 배치까지 갱신한다.
8. 배치 gate가 통과하면 사용자 입력을 기다리지 않고 다음 배치로 간다.

배치 도중 실패하면 원인을 고치고 같은 검사를 다시 실행한다. 단원 수를 줄이거나 다음 단원으로 건너뛰어 실패를 숨기지 않는다.

### 3.2 단원별 필수 구조

모든 단원은 기존 템플릿의 흐름을 유지한다.

```text
필요성
→ 관찰 가능한 학습 목표
→ 선수지식 확인
→ 기호와 용어
→ 직관과 정확한 정의
→ 수식 읽기
→ 작은 손계산
→ 코드 또는 모델 연결
→ 한계와 흔한 오해
→ 4~8개 문제와 전 문제 해설
→ 단원 요약
→ 통과 기준
```

제2부 이후의 계산 단원은 다음 네 층을 연결한다.

| 층 | 요구 내용 |
|---|---|
| 수식 | 기호 의미, shape, 성립 조건과 전체 역할 |
| 손계산 | 작은 정수나 짧은 vector로 중간값까지 전개 |
| tiny 코드 | 같은 계산을 CPU에서 재현하고 수치·shape·gradient 검사 |
| 실제 모델 | 해당 계산이 Pythia의 어느 module·layer·token 위치에 나타나는지 확인 |

실제 모델 결과가 필요하지 않은 N05 단원은 앞의 세 층으로 완료할 수 있다. I06 이후의 핵심 실험은 tiny 결과와 Pythia 결과의 역할을 분리해 제시한다.

### 3.3 설명과 주장 규칙

- Common spoken reading은 영어 발화만 백틱으로 적는다. 한글 음역과 기호 위치의 기계적 직역을 쓰지 않는다.
- `관찰됐다`, `복원할 수 있다`, `사용한다`, `원인이다`, `일반화된다`를 증거 수준에 맞춰 구분한다.
- probe 성능을 모델의 기능적 사용 증거로 바꾸지 않는다.
- activation 차이를 feature 학습이나 개념 형성으로 바로 부르지 않는다.
- 귀인 결과를 인과 효과로 부르지 않는다.
- 외부 연구의 결과, 모델 구조와 제한은 원 논문·공식 모델 카드·공개 config 또는 공식 구현으로 확인한다.
- 시점에 따라 바뀌는 라이브러리 사용법은 본문 핵심 개념과 분리하고 확인일·버전을 적는다.

### 3.4 배치 완료 조건

배치는 다음 조건을 모두 통과해야 한다.

- frontmatter ID·H1·파일명이 일치하고 단원 ID가 연속한다.
- 새 기호가 사용 전에 정의됐고 shape와 index 관례가 일치한다.
- Common spoken reading lint가 통과한다.
- 모든 문제에 판단 과정과 결과 의미를 포함한 해설이 있다.
- `.py` 원본을 Markdown에 복제하지 않았다.
- 코드가 손계산과 명시적 `rtol`·`atol` 아래 일치한다.
- 필수 예제가 자원 상한과 timeout을 지킨다.
- source audit, 단위 테스트, strict build와 generated-site validation이 통과한다.
- 새 페이지의 내부 링크, 수식, 표, 코드와 `details`가 브라우저에서 정상이다.
- 진행표와 용어집이 현재 작성 상태와 일치한다.

## 4. 자체 tiny Transformer와 실제 pretrained model의 역할

### 4.1 자체 tiny Transformer

자체 tiny decoder는 필수 개념의 기준 계산이다.

- 외부 다운로드 없이 CPU와 GitHub Actions에서 실행한다.
- RMSNorm, RoPE, causal MHA, dense SwiGLU와 pre-norm residual block을 교육용 기준으로 사용한다.
- 수식, 손계산, tensor shape, gradient와 cache 상태를 직접 대조한다.
- architecture variant는 이 기준 계산에서 무엇이 유지되고 무엇이 바뀌는지 비교한다.
- N05-28까지 token ID에서 logit까지의 경로와 KV cache를 추적할 수 있어야 한다.

### 4.2 Pythia

Pythia는 실제 공개 모델의 module 구조, activation, 개입과 checkpoint 변화를 확인하는 연구용 기준이다. Pythia의 결과를 tiny 모델의 수학적 정답으로 사용하지 않는다.

| 등급 | 모델 | 고정 revision | 역할 | 완료 gate 포함 여부 |
|---|---|---|---|---|
| smoke | `EleutherAI/pythia-70m-deduped` | `step143000` | hook·tokenizer·runner 빠른 확인 | 포함 |
| 주력 | `EleutherAI/pythia-160m-deduped` | `step143000` | I06·I07의 실제 모델 분석 | 포함 |
| 규모 비교 | `EleutherAI/pythia-410m-deduped` | `step143000` | I06-08의 표현 유사도 규모 비교 | I06-08에 포함 |
| 선택 확장 | `EleutherAI/pythia-1b-deduped` | `step143000` | 여유 자원에서의 추가 비교 | 불포함 |

I08의 checkpoint 비교는 주력 160M에 `step0`, `step1000`, `step10000`, `step50000`, `step100000`, `step143000`을 사용한다. 파일럿에서 더 촘촘한 초기 변화가 필요하다는 증거가 나오면 교육과정의 checkpoint 목록을 바꾸지 않고 실험 manifest의 보조 관측으로만 추가한다.

모델과 tokenizer는 같은 repository ID와 같은 revision으로 불러온다. 최초 다운로드 때 branch 이름과 Hugging Face가 반환한 immutable commit SHA를 manifest에 함께 기록한다. 이후 같은 실험은 resolved SHA를 사용한다. `main`과 revision 생략은 금지한다. `trust_remote_code=False`를 사용한다.

`v0` 계열은 주력 실습에서 제외한다. 7B 이상 모델은 필수·선택 실행 범위에서 모두 제외한다. Pythia 공식 자료가 밝힌 현재 suite와 checkpoint 체계는 [EleutherAI Pythia repository](https://github.com/EleutherAI/pythia)와 [Pythia-160M-deduped model card](https://huggingface.co/EleutherAI/pythia-160m-deduped)를 기준으로 한다.

## 5. 실행 환경 등급과 분리

### 5.1 등급

| 등급 | 실행 위치 | 네트워크 | 완료 gate |
|---|---|---|---|
| CPU 필수 | 기존 `.venv`, 로컬과 GitHub Actions | 설치 뒤 불필요 | 모든 Phase에 필수 |
| 로컬 GPU 필수 | Phase 3 이후 `.venv-gpu`, RTX 5060 Laptop GPU | 최초 model cache 준비에만 필요 | I06~I08의 지정 실험에 필수 |
| 선택 외부 실행 | 사용자가 별도로 승인한 환경 | 환경별 | 어떤 Phase도 막지 않음 |

유료 notebook, cloud GPU와 hosted inference API는 기본 계획에 없다. 로컬 GPU가 필수 gate를 통과하지 못해도 작업자가 외부 서비스로 자동 전환하지 않는다.

### 5.2 CPU 환경

기존 `.venv`를 그대로 사용한다. CPU requirements, 환경 진단과 현재 자원 상한은 `N05-ENVIRONMENT.md`가 단일 기준이다. GPU package를 이 환경에 설치하지 않는다.

### 5.3 GPU 환경

GPU 환경은 Phase 3에서만 만든다. 현재 확인된 장치는 NVIDIA GeForce RTX 5060 Laptop GPU, VRAM 8151 MiB, driver 595.95, CUDA driver 13.2, compute capability 12.0이다.

Phase 3은 다음 파일을 별도로 만든다.

- GPU direct dependency와 CUDA wheel index를 고정한 requirements 파일
- 전체 resolved dependency를 기록한 lock 또는 환경 manifest
- `.venv-gpu` 생성·진단 script
- Pythia cache를 명시적으로 준비하는 script
- GPU 예제 runner와 manifest schema
- GPU 전용 단위·통합 test

초기 direct pin은 Python 3.12, PyTorch 2.13.0 CUDA 13.2 wheel, NumPy 2.5.3, Transformers 5.17.0이다. PyTorch 설치 명령은 [공식 previous versions 문서](https://pytorch.org/get-started/previous-versions/)의 `cu132` index를 사용한다. Phase 3 진단이 GPT-NeoX load와 hook을 통과한 뒤 전체 dependency와 wheel source를 manifest에 고정한다. setup은 모델을 자동 다운로드하지 않는다.

## 6. 자원 예산

### 6.1 CPU 필수 실습

| 항목 | 상한 |
|---|---:|
| batch size | 2 |
| sequence length | 32 |
| model dimension | 64 |
| Transformer layer | 2 |
| attention head | 4 |
| vocabulary size | 256 |
| 전체 parameter | 250,000 |
| 학습 step | 50 |
| DataLoader worker | 0 |
| PyTorch intra-op·inter-op thread | 각각 1 |
| 개별 예제 hard timeout | 10초 |
| 전체 CPU 예제 hard timeout | 120초 |
| 전체 CPU 예제 실행시간 목표 | 30초 |

이 상한을 바꿀 필요가 생기면 N05 단원의 규모를 키우기 전에 알고리즘과 예제를 줄인다. multiprocessing은 사용하지 않는다.

### 6.2 로컬 GPU 실습

모델은 한 번에 하나만 GPU에 올린다. full training, optimizer state 적재와 전체 activation 저장은 하지 않는다.

| 모델 등급 | dtype | batch | sequence | peak allocated VRAM | 개별 실행 hard timeout |
|---|---|---:|---:|---:|---:|
| 70M smoke | float16 | 1 | 128 | 2.5 GiB | 120초 |
| 160M 주력 | float16 | 1 | 128 | 4.0 GiB | 180초 |
| 410M 비교 | float16 | 1 | 64 | 6.5 GiB | 300초 |
| 1B 선택 | float16, inference only | 1 | 32 | 7.0 GiB | 300초 |

- 필수 GPU suite hard timeout은 1,200초다. 최초 weight 다운로드 시간은 계산 timeout에서 제외하고 별도 기록한다.
- 실행 직전 가용 VRAM이 6 GiB보다 적으면 필수 GPU suite를 시작하지 않는다.
- backward가 필요한 실험은 70M 또는 160M에서 수행한다. 410M은 기본적으로 inference·hook 비교만 한다.
- 1B 실패는 Phase를 막지 않는다. 70M smoke와 160M 주력 gate 실패는 Phase 3 이후 진행을 막는다.
- peak VRAM은 `torch.cuda.max_memory_allocated()`와 실행 전후 `nvidia-smi` 값을 함께 기록한다.
- OOM이 나면 cache를 비운 뒤 batch와 sequence를 먼저 줄인다. precision을 임의로 바꾸거나 CPU offload로 상한을 숨기지 않는다.

### 6.3 disk와 artifact

- 필수 Pythia cache 예산은 12 GiB다. 1B 선택 확장까지 사용할 때만 18 GiB까지 허용한다.
- 한 실행에서 디스크에 저장하는 선택 activation은 256 MiB 이하로 제한한다.
- 전체 layer·token activation dump는 금지한다.
- artifact quota를 넘으면 실행 전에 실패시키고 layer, token, sample 또는 통계량 범위를 줄인다.

## 7. 코드, cache, artifact와 manifest

### 7.1 단일 원본

- 실행 코드는 `labs` 아래 `.py` 파일만 원본으로 둔다.
- Markdown에는 예제 ID, 실행 명령, 환경 등급과 결과 삽입 marker만 둔다.
- site generator는 source hash가 일치하는 실행 결과만 삽입한다.
- 손으로 복사한 stdout, 수치표와 그림을 결과인 것처럼 넣지 않는다.
- 공통 분석 함수와 교육용 entry point를 분리하되, 한 번만 쓰는 추상화는 만들지 않는다.

CPU strict build에서 실제 모델 marker를 만나면 코드 경로, 고정 revision, 실행 명령과 “로컬 GPU 결과가 삽입되지 않음” 상태를 렌더링한다. 로컬 GPU build는 별도 flag가 있을 때만 manifest의 source hash·model revision·artifact hash를 검증하고 실제 결과를 같은 marker에 삽입한다. GPU manifest가 없다는 이유로 CPU build가 model download를 시작해서는 안 된다.

### 7.2 경로

Phase 3에서 다음 경로 계약을 구현한다.

```text
.cache/huggingface/                       # model·tokenizer cache, Git 제외
.build/gpu/results/<experiment_id>/       # 실행 결과와 manifest, Git 제외
.build/gpu/activations/<experiment_id>/   # 선택 activation, Git 제외
labs/real_models/                         # 실제 모델 코드 원본
tests/real_models/                        # CPU fixture test와 로컬 GPU test
```

`.cache/`, `.build/`, model weight 확장자와 activation artifact 확장자는 `.gitignore`와 source audit에서 중복 차단한다.

### 7.3 manifest 필수 필드

각 실제 모델 실행은 다음 정보를 JSON manifest에 기록한다.

- schema version, experiment ID와 lesson ID
- source path, source SHA-256와 Git commit
- 실행 명령, 시작 시각, 종료 상태와 단계별 시간
- Python, PyTorch, Transformers, NumPy 버전
- GPU 이름, VRAM, driver, CUDA runtime와 compute capability
- model ID, 요청 revision, resolved commit SHA와 config hash
- tokenizer ID, 요청 revision, resolved commit SHA와 vocab 관련 설정
- seed, deterministic 설정, dtype와 inference·gradient mode
- 입력 source와 입력 SHA-256, batch와 sequence length
- hook의 module path, layer, token, component와 capture 조건
- artifact별 path, SHA-256, shape, dtype와 byte 수
- peak allocated VRAM, 실행 전후 가용 VRAM
- 수치 tolerance, 통과한 assertion과 실패 이유

manifest는 artifact가 없어도 실행 조건과 누락 이유를 읽을 수 있어야 한다. secret, access token, 사용자 로컬 절대경로와 개인 입력은 기록하지 않는다.

### 7.4 Git 추적 금지

다음 파일은 크기와 관계없이 Git에 넣지 않는다.

- model·tokenizer weight와 Hugging Face cache
- optimizer state와 full checkpoint
- 전체 activation과 gradient dump
- runner가 생성한 JSON, stdout, plot, HTML과 notebook output
- 외부 서비스에서 받은 생성 결과

`git status --short`와 `git ls-files` 패턴 검사를 Phase gate에 넣는다. 작은 파일이라는 이유로 예외를 만들지 않는다.

## 8. test와 검수 체계

### 8.1 단위 테스트

각 실습은 최소한 다음 가운데 해당하는 항목을 검사한다.

- 입력·중간값·출력 shape
- 손계산한 forward value
- gradient, JVP 또는 VJP
- parameter와 buffer 수
- mask, normalization, cache와 hook 위치
- seed 재현성과 수치 tolerance
- 자원 spec과 timeout
- 결과 schema와 source hash

실제 모델을 요구하지 않는 분석 함수는 synthetic tensor와 tiny CPU fixture로 검사한다. fixture는 사람이 정의한 최소 입력과 기대 성질을 사용하며 Pythia 실행 결과를 복사하지 않는다.

### 8.2 source audit

source audit은 작성된 모든 단계에 대해 다음을 검사한다.

- 교육과정에 있는 ID·제목·순서와 파일 prefix
- frontmatter, H1, 파일명과 선수지식 ID
- H1 하나, 수식 구분자, Common spoken reading 표와 lint
- 집필자 점검표 하나와 4~8개 문제·해설 대응
- 로컬 source link와 실행 marker
- 계획 수보다 많은 파일, 중복 ID와 미래 단원 링크
- Git 금지 패턴과 Markdown에 복제된 실행 코드·stdout

### 8.3 strict build와 생성 사이트 검증

CPU build는 항상 clean checkout만으로 통과해야 한다.

1. CPU 환경 진단
2. 모든 CPU 단위 테스트
3. 필수 CPU 예제 실행
4. source audit
5. staging 생성
6. MkDocs `--strict --clean` build
7. generated-site validation

generated-site validation은 source·staging·HTML 단원 수, nav 고유성, code source hash, result schema, 수식 wrapper, `details` 수, search index, broken link·asset 0개와 집필자 점검표 노출 0개를 검사한다.

### 8.4 GitHub Actions

GitHub Actions에서는 다음을 하지 않는다.

- CUDA wheel 설치와 GPU test
- Hugging Face model·tokenizer 다운로드
- network가 필요한 Pythia 실행
- GPU artifact 생성 또는 복원

Actions는 기존 `.venv`와 같은 CPU dependency, tiny 모델 예제, synthetic fixture, source audit와 strict site build만 검사한다. GPU code는 import, schema, 분석 함수와 mock hook을 CPU fixture로 검사한다. 실제 Pythia gate의 증거는 로컬 manifest와 로컬 validation report에만 둔다.

### 8.5 브라우저 검수

각 배치에서 새 페이지 전부를 자동 검증한다. 사람 눈으로는 새 배치의 첫 페이지와 마지막 페이지, 그리고 넓은 표·긴 수식·실행 결과·그림을 가진 페이지를 확인한다.

- desktop 1440×900에서 light와 dark theme
- mobile 390×844에서 nav, 표 overflow와 코드 가로 스크롤
- 수식 잘림, 표 header, 해설 접기, 이전·다음 링크와 search hit
- 집필자 점검표와 내부 파일명이 노출되지 않는지 확인

Phase 8에서는 각 단계에서 최소 두 페이지와 각 A09 모듈의 종합 실습 페이지를 다시 확인한다.

## 9. Phase별 실행 계약

### Phase 0. 기준선 동결과 본 명세 확정

**입력**

- 기준 커밋 `819ba380317f3533e73da0dddbb3dccbb55f5e9a`
- 현재 기준 문서, 템플릿, N05-01~03, labs, tests와 site code

**실행 순서**

1. HEAD, branch, working tree와 `origin/main`을 확인한다.
2. 기준 문서와 현재 실행 계약을 읽는다.
3. 현재 목차 수, 코드 경로, resource limit와 build gate를 대조한다.
4. 이 문서를 작성하고 내부 모순·누락·검증 불가능한 조건을 감사한다.
5. 기존 CPU 환경에서 `scripts/build_site.ps1`을 실행한다.
6. 변경 파일이 이 문서 하나인지 확인한다.

**완료 조건**

- 기존 73개 단원, N05 예제 3개, source audit와 strict build가 그대로 통과한다.
- 기준 문서와 다른 사항은 결정 기록으로 분리돼 있다.
- commit과 push를 하지 않는다.
- 사용자 검토 전에는 Phase 1을 시작하지 않는다.

### Phase 1. N05-04~N05-10

**선수조건**

- 사용자가 Phase 0 명세와 14절의 두 결정을 승인했다.
- 후속 전체 Goal의 첫 작업으로 승인된 `06-BOOK-COMPLETION-PLAN.md`만 Phase 0 기록 commit에 넣고 private `main`에 일반 push한다.
- working tree가 깨끗하고 local HEAD, `origin/main`과 승인된 시작 commit이 같다.

**범위와 배치**

1. N05-04~N05-06: activation·gating, logits·softmax·cross entropy, backpropagation
2. N05-07~N05-08: mini-batch gradient descent, momentum·AdamW·optimizer state
3. N05-09~N05-10: PyTorch tensor·dtype, autograd·JVP·VJP

제목은 `01-CURRICULUM.md`의 정확한 표기를 사용한다.

**산출물**

- 7개 단원 Markdown
- 필요한 `labs/N05` 코드와 단위 테스트
- 작성 단원과 선택적 실행 예제를 다루는 일반화된 site registry
- 갱신된 진행표·용어집·N05 architecture 확인일

**완료 조건**

- N05가 10/28이다.
- N05-10 누적 검토에서 Stable core 분류와 공개 config 근거를 다시 확인한다.
- CPU resource limit, full build와 브라우저 검수가 통과한다.

### Phase 2. N05-11~N05-28

**범위와 배치**

1. N05-11~13: tokenizer, embedding·unembedding, 위치정보·RoPE
2. N05-14~16: query·key·value, causal attention, MHA·MQA·GQA
3. N05-17~19: residual stream, normalization·residual 순서, dense MLP·SwiGLU·routing
4. N05-20~22: decoder block·architecture diff, 언어모델 목적함수, causal inference·KV cache
5. N05-23~25: decoding, CoT의 관찰 지위, hook·activation 수집
6. N05-26~28: gradient 수집, checkpoint·모델 상태, 한 token의 종합 경로

**산출물**

- 18개 단원 Markdown과 tiny decoder 누적 코드
- attention, residual, normalization, MLP, objective, cache, hook와 checkpoint tests
- N05-20과 N05-28 architecture baseline 재검토 기록

**완료 조건**

- N05가 28/28이다.
- N05-28이 token ID에서 logit까지 shape, residual 경로와 cache 상태를 재현한다.
- 외부 모델을 받지 않은 clean CPU 환경에서 N05 전체 build가 통과한다.
- 다음 단계에 필요한 hook·activation·gradient·checkpoint API가 tiny 모델에서 검증됐다.

### Phase 3. GPU·Pythia 기반과 I06 파일럿

**선수조건**

- N05 28/28과 CPU build 통과
- GPU hardware·driver 재확인
- model cache에 필요한 disk 여유 확인

**실행 순서**

1. `.venv-gpu` setup·requirements·진단을 만든다.
2. CUDA matmul, autograd, deterministic seed, peak VRAM과 timeout을 검사한다.
3. Pythia registry, cache 준비 script, runner와 manifest schema를 만든다.
4. 70M `step143000` smoke를 통과시킨다.
5. 160M `step143000`에서 지정 layer·token hook과 최소 gradient 실험을 통과시킨다.
6. 410M 최종 checkpoint를 inference-only 규모 비교로 확인한다.
7. I06-01~03을 한 배치로 집필한다.
8. CPU build가 GPU 환경과 cache 없이 그대로 통과하는지 다시 검사한다.

**산출물**

- 분리된 GPU 환경 파일과 로컬 runner
- Pythia model·tokenizer revision registry
- manifest, artifact quota와 GPU validation report
- I06-01 행동과 표현 질문 설계
- I06-02 activation dataset
- I06-03 분포와 기초 통계

**완료 조건**

- 70M smoke와 160M 주력 실험이 resource gate 안에서 통과한다.
- model·tokenizer의 requested revision과 resolved SHA가 기록된다.
- 전체 activation을 저장하지 않고 필요한 layer·token slice만 수집한다.
- GitHub Actions와 CPU build는 model download 없이 통과한다.
- 실제 Pythia 결과의 사이트 배포 방식은 `결정 완료 1`을 따른다.

### Phase 4. I06 전체

**범위와 배치**

1. I06-04~06: neuron, PCA·SVD, linear probe
2. I06-07~09: probe control·selectivity, CCA·CKA·RSA, feature visualization
3. I06-10~12: superposition, sparse coding, sparse autoencoder
4. I06-13~15: feature 안정성·identifiability, 표현 주장, 종합 표현 보고서

**완료 조건**

- I06가 15/15이다.
- probe 결과와 모델의 정보 사용 주장이 명시적으로 분리된다.
- SAE는 reconstruction, sparsity, dead feature, seed·dictionary 안정성을 함께 평가한다.
- I06-15는 데이터 정의, activation 수집, 통계, control과 주장 강도를 한 보고서로 연결한다.
- 160M이 주력이고 70M은 smoke에만 사용된다. 410M은 I06-08의 CKA·RSA 규모 비교 한 곳에서만 필수로 사용한다.

### Phase 5. I07 전체

**범위와 배치**

`I07-01~03`, `04~06`, `07~09`, `10~12`, `13~15`, `16~17`의 여섯 배치로 진행한다. 각 ID·제목은 교육과정의 순서를 그대로 사용한다.

**완료 조건**

- I07이 17/17이다.
- gradient·integrated gradients·perturbation을 귀인 방법으로 비교한다.
- ablation, activation patching, causal tracing과 path patching의 개입 대상을 구분한다.
- necessity와 sufficiency를 별도 대조군으로 검사한다.
- off-manifold intervention과 CoT faithfulness의 주장 한계를 포함한다.
- I07-17에서 작은 circuit의 행동 정의, node·edge, 개입, 대조군과 통계 검증을 연결한다.

### Phase 6. I08 전체

**범위와 배치**

`I08-01~03`, `04~06`, `07~09`, `10~11`, `12~13`의 다섯 배치로 진행한다.

**완료 조건**

- I08이 13/13이다.
- checkpoint revision, data·seed·metric과 비교 대상이 manifest에 고정된다.
- parameter distance와 function distance를 구분한다.
- alignment, Hessian spectrum, loss path와 influence 근사의 조건을 설명한다.
- Pythia 160M의 고정 checkpoint 여섯 개를 순차적으로 한 번에 하나씩 불러온다.
- I08-13에서 한 feature의 형성, 복원 가능성, 사용 증거와 행동 변화를 시간축으로 구분한다.

### Phase 7. A09 선택 심화 전체

각 모듈은 독립 subphase다. 모듈 안에서는 `01~03`, `04~06`, `07~08`의 세 배치로 진행한다.

| subphase | 범위 | 직접 선수지식 | 종합 gate |
|---|---|---|---|
| 7A | A09-GEO-01~08 | M01, M02, M03 | 국소 표현 기하 실습 |
| 7B | A09-DYN-01~08 | M01, M03, M04, I08 | 학습 궤적 분석 |
| 7C | A09-SYM-01~08 | M02, M03, I06, I08 | seed 간 표현 정렬 |
| 7D | A09-LRN-01~08 | M04, N05, I06 | 복잡도와 일반화 |
| 7E | A09-KER-01~08 | M02, M03, M04, N05 | kernel 관점의 학습 |
| 7F | A09-RMT-01~08 | M02, M04, I06, I08 | spectrum null model |
| 7G | A09-CAU-01~08 | M04, I07 | circuit 수준 인과 주장 |

**완료 조건**

- 일곱 모듈이 각각 8/8이고 A09가 56/56이다.
- 선택 모듈이 다른 A09 모듈을 숨은 선수지식으로 요구하지 않는다.
- 각 모듈은 입문 경로와 종합 실습을 포함한다.
- 연구 질문에 필요하지 않은 완전한 증명이나 전공과정 전체를 요구하지 않는다.
- 수치 실험이 없는 단원은 증명 연습이나 반례 설계로 관찰 가능한 통과 기준을 둔다.

### Phase 8. 전권 통합 검증

**실행 순서**

1. curriculum, filesystem, progress와 site nav의 ID·제목·개수를 대조한다.
2. 199개 단원의 frontmatter, H1, 선수지식과 링크를 감사한다.
3. Common spoken reading, 수식 구분자, 용어 중복과 표기 충돌을 검사한다.
4. 문제·해설 대응과 단계별 종합 과제를 검사한다.
5. CPU clean build와 generated-site validation을 실행한다.
6. 로컬 GPU 필수 suite를 cache 고정 상태에서 실행한다.
7. Git 금지 artifact가 추적되지 않았는지 검사한다.
8. 단계별 브라우저 표본과 모든 종합 실습 페이지를 검수한다.
9. README, 진행표, 용어집과 환경 문서를 최종 상태로 갱신한다.

**완료 조건**

- source lesson은 정확히 199개다: M00~M04 70, N05 28, I06 15, I07 17, I08 13, A09 56.
- 필수 단계 0~8과 A09 일곱 모듈이 모두 완료 상태다.
- 모든 내부 링크와 asset가 유효하고 generated lesson page가 199개다.
- 집필자 점검표 노출, broken link·asset, 중복 ID와 미래 단원 링크가 0개다.
- CPU 필수 실습은 외부 모델 없이 재현된다.
- 지정된 Pythia 실험은 고정 revision·manifest·자원 상한 아래 재현된다.
- 네 부분이 하나의 nav와 search index에서 연결된다.

## 10. 진행표, commit과 push

### 10.1 진행표

각 배치가 끝날 때 `03-PROGRESS.md`에 다음을 기록한다.

- 완료한 ID 범위와 문제·해설 수
- 추가한 lab·test와 실행 환경 등급
- source audit, build와 브라우저 검수 결과
- resource 사용량과 실제 모델 revision
- 다음 배치 또는 Phase gate

`완료/전체` 수는 filesystem과 자동 대조한다. 사람이 쓴 숫자만 믿지 않는다.

### 10.2 commit 단위

- 후속 전체 Goal은 승인된 이 문서만 담은 Phase 0 기록 commit을 먼저 만들고 push한다. 이 commit에는 단원·환경·실행 코드 변경을 섞지 않는다.
- Phase 1~6은 Phase gate가 모두 통과한 뒤 Phase당 한 개의 명확한 commit을 만든다.
- Phase 7은 56개 단원을 한 diff로 묶지 않는다. 7A~7G를 각각 하나의 gate이자 단일 commit으로 취급한다.
- Phase 8은 통합 수정과 최종 검증 기록을 하나의 commit으로 만든다.
- 배치 검증은 commit 전에 반복하지만, 부분 통과 상태를 완료 commit으로 만들지 않는다.
- commit message는 범위와 결과를 드러낸다. 예: `Complete N05-04 through N05-10`.

### 10.3 private main push

1. Phase 시작 전에 원격 저장소가 private이고 default branch가 `main`인지 확인한다.
2. `git fetch origin` 뒤 local HEAD와 `origin/main`을 비교한다.
3. 예상하지 못한 원격 commit이 있으면 merge, rebase와 force push를 하지 않고 멈춘다.
4. Phase gate 뒤 변경 파일을 확인하고 하나의 commit을 만든다.
5. `git push origin main`으로 일반 push한다.
6. push 뒤 remote commit과 local commit이 같은지 확인한다.

`--force`, `--force-with-lease`, history rewrite와 자동 conflict resolution은 금지한다.

## 11. 사용자 입력 없이 계속하는 조건

후속 전체 집필 Goal은 다음 조건을 모두 만족하면 다음 배치 또는 Phase로 자동 진행한다.

- 직전 batch·Phase의 필수 gate가 모두 통과했다.
- working tree에 범위 밖 변경이 없다.
- 원격 `main`에 예상하지 못한 변경이 없다.
- 다음 단원의 ID·제목·선수지식이 교육과정에 명시돼 있다.
- 필요한 자료가 공개 1차 자료이며 인증·결제·사용자 데이터 전송을 요구하지 않는다.
- CPU 또는 해당 GPU resource budget 안에서 실행할 수 있다.
- 새로 발견한 미결 항목이 다음 작업의 결과를 바꾸지 않는다.

진행 중간의 단순 상태 보고를 이유로 멈추지 않는다. 실패를 수정할 수 있고 범위가 같으면 수정 후 gate를 다시 실행한다.

## 12. 반드시 멈추는 조건

다음 상황에서는 범위를 임의로 바꾸지 않고 원인, 영향 범위, 이미 통과한 gate와 필요한 사용자 입력을 보고한다.

- GitHub, Hugging Face 또는 다른 필수 자원에 새 인증이 필요하다.
- `origin/main`에 예상하지 못한 commit이나 충돌이 있다.
- 유료 서비스, cloud GPU, hosted API 또는 새 외부 계정이 필요하다.
- 사용자 코드·문서·prompt·artifact를 새 외부 서비스에 전송해야 한다.
- 라이선스나 model card 조건이 계획한 교육·배포 방식과 충돌한다.
- 기준 문서끼리 내용 범위, 표기, 완료 조건이 충돌한다.
- 다음 단원의 ID·제목·직접 선수지식이 빠져 있어 두 가지 이상으로 해석된다.
- CPU 필수 build가 기존 완료 단원에서 회귀하고 범위 안 수정으로 해결할 수 없다.
- 160M 필수 실험이 sequence와 capture 범위를 줄인 두 번의 재시도 뒤에도 VRAM·timeout 상한을 넘는다.
- 같은 blocker가 세 번 연속 반복되며 사용자 선택이나 외부 상태 변화 없이는 진전할 수 없다.
- 범위 밖 파일의 사용자 변경과 겹쳐 안전한 편집이 불가능하다.

선택 1B 실행 실패, 선택 외부 실행 부재와 CPU target time 초과는 hard gate가 아니다. 단, hard timeout과 정확성 검사는 그대로 통과해야 한다.

## 13. 최종 보고 항목

후속 전체 집필 Goal의 최종 보고에는 다음을 포함한다.

- 시작·종료 commit과 원격 동기화 상태
- 단계·모듈별 완료/전체 단원 수
- 새 Markdown, lab, test와 환경 파일 수
- 문제·해설 쌍 수와 단계별 종합 실습 목록
- CPU 환경과 전체 build 시간, test 수와 validation summary
- GPU 환경, model·tokenizer revision, resolved SHA, peak VRAM와 필수 실험 시간
- 브라우저 검수한 대표 페이지와 발견·수정한 렌더링 문제
- glossary·표기·Common spoken reading 감사 결과
- Git에 추적되지 않은 cache·artifact 경로와 quota 준수 여부
- 남은 선택 확장, 알려진 한계와 열린 결정

완료라는 말은 Phase 8의 수치화된 gate가 모두 통과했을 때만 사용한다.

## 14. 결정 기록

### 결정 완료 1. 실제 Pythia 결과를 배포 HTML에 유지하는 방법

현재 규칙은 HTML과 모든 생성 결과를 Git에서 제외한다. GitHub Actions는 GPU와 외부 모델 다운로드를 사용하지 않는다. 따라서 clean checkout으로 만든 원격 HTML에는 실제 Pythia 실행 결과를 영구 삽입할 수 없다.

**결정:** 현재 규칙을 유지한다. public 또는 private GitHub build에는 tiny CPU 결과와 실제 모델 실험의 재현 절차·manifest schema만 넣고, Pythia 수치·plot은 로컬 GPU build에서만 삽입한다. 나중에 실제 결과를 공개 사이트에 고정하려면 작은 검증 완료 reference artifact를 Git에 둘지, 별도 release artifact를 사용할지 사용자가 명시적으로 결정한 뒤 Git 추적 금지 규칙을 수정한다.

사용자가 2026-10-01에 이 방식을 승인했다. Phase 3은 추가 확인 없이 이 규칙을 적용한다.

### 결정 완료 2. Phase 7 commit 해석

“Phase별 단일 commit”을 Phase 7 전체에 그대로 적용하면 56개 단원과 실습이 한 commit에 묶인다. 검토와 복구 단위가 너무 크다.

**결정:** Phase 7A~7G를 독립 gate로 보고 모듈당 한 commit을 만든다. A09 전체 상태는 7G가 끝난 뒤 한 번에 완료로 바꾼다.

사용자가 2026-10-01에 이 방식을 승인했다.

## 15. Phase 0 검증 기록

이 절은 이 문서를 작성한 같은 Goal에서 채운다. 후속 집필 결과를 이 기록에 섞지 않는다.

| 검사 | 기대값 | 결과 |
|---|---|---|
| HEAD | `819ba380317f3533e73da0dddbb3dccbb55f5e9a` | 확인 |
| branch | `main` | 확인 |
| local과 `origin/main` | 동일 | 확인 |
| 변경 범위 | `06-BOOK-COMPLETION-PLAN.md` 하나 | 확인 |
| 기존 source lesson | 73 | 73 |
| N05 실행 예제 | 3 | 3 |
| CPU full build | 통과 | 14 tests, strict build·validation 통과 |
| N05 예제 suite | 120초 이하, 목표 30초 | 8.86초 |
| Common spoken reading | 표 73개, cell 486개 | 73개, 486개 |
| generated lesson page | 73 | 73 |
| broken link·asset | 0 | 0 |
| 집필자 점검표 HTML 노출 | 0 | 0 |

