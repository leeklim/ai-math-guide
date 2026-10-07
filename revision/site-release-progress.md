# 한영 탐색 구조·검색 정보·공개 배포 진행

## 기준과 승인

- 전체 수행 기준: `site/RELEASE-PLAN.md`.
- 기준 커밋: `07549af` (`codex/english-edition`). 추적 파일 수정 없음. 무관한 미추적 `programming-assignment-1/`, `tmp/` 보존.
- 이전 검증 기록의 기준 수량: 언어별 199개 단원·1,154개 문제/해설·205개 공개 문서, 공유 SVG 1,355개. 이번 작업의 통합 보존 검사는 최종에 수행한다.
- 대표 화면 검증 후 전권 적용, 최종 검증 후 `leeklim/ai-math-guide` main push·GitHub Pages 공개 배포를 사용자가 사전 승인했다. 두 지점에서 재승인을 기다리지 않는다.
- 수학 내용 정정과 범위 확대는 별도 승인 대상이다. 기존 원문 의문점은 정정 없이 기록 분류만 유지한다. 철회된 M00-10 작은 cross-entropy 우려는 제외한다.

## 현재 단계

- Goal 활성화 및 전체 지시 보관 완료. 프로젝트 명세·문체·단원 템플릿 확인.
- 표본 설명 5개를 원문과 대조 검토하고 국소 문구 보완 완료. 공통 공개 표시 변환·4부 탐색 구조·앵커 보존·학습 순서 footer·검색/공유 metadata 구현.
- 대표 화면 검수 통과 후 전권 적용 완료. 17개 단위·205개 경로의 한영 설명을 두 작성자가 작성하고 별도 검토자가 원문과 대조했다. 205/205 검토 통과, 조건·용어의 국소 수정 반영, 현재 차단 결함 0. 원고 재작성 없음.
- 기존 로그인에서 GA4 속성 접근 확인(실제 수신 검증 전). Search Console의 승인된 URL-prefix 속성을 생성하고 HTML meta 인증값을 읽어 설정·template에 반영. 인증 실행과 sitemap 제출은 공개 배포 후 수행한다.

## 실제 수행한 검사

- git status/branch/log/remote 읽기 확인. 원격 쓰기 없음.
- 두 작성자가 표본 metadata JSON 구문·경로 및 원고 diff 보존 확인. 검토자가 표본 5개의 원문 근거 확인.
- `tests.test_reader_navigation tests.test_bilingual_site tests.test_homepage`: 최신 실행 36개 통과. 범위 참조(전체·축약 ID), protected code/math, 기존 앵커 및 HTML reader-text 검사를 포함.
- KO/EN strict HTML build 통과(KO 6.55초, EN 16.50초). 전권 metadata 작성 전 대표 검수 빌드이며 최종 통합 빌드는 별도로 수행한다.
- 홈페이지·학습 경로·M00-03/M03-11/N05-15/I07-07/A09-GEO-02를 한영·1440×900/390×844·밝은/어두운 테마에서 확인. 관찰 페이지의 가로 넘침/깨진 이미지 없음. 긴 모바일 breadcrumb는 줄바꿈으로 보완 후 재확인.
- 처음부터 학습, 모바일 부→모듈→단원 선택, 선수단원 왕복, 검색 진입 후 위치 확인, 같은 단원의 한영 전환, 이전/다음 순서, 키보드·터치 이동 확인. N05-15 수식·그림·코드·실행 결과 확인. 브라우저 수식 오류 요소와 console 오류 없음.
- 검토자: 공개 본문 제목 앵커 11,282개 누락 0건, 표본 HTML 중복 ID 0건. ID 범위 변환 결함 수정 후 회귀 테스트와 staging 재확인.
- 대표 화면 자료: `.build/release-proof/`(로컬 산출물). 표본 주소: `http://127.0.0.1:8005/ai-math-guide/` 및 `/en/`.
- 원격 main read-only 확인: `92f44ff3e110f1c925505b7912a0034d5f18c6bd`. 원격 쓰기·공개 배포는 아직 수행하지 않음.
- Git 호스트 실행 맥락 읽기 확인: 소유권 차이로 첫 실행이 실패했으나 이 저장소만 명령 단위 `safe.directory`로 지정하여 저장소 루트·HEAD·상태 및 main ancestry를 확인. 전역 설정 변경 없음.
- 독립 보존 확인: baseline `07549af` 대비 KO/EN 원고·지원 문서·SVG/생성 코드/manifest·labs diff 없음. 각 언어 199단원·1,154문제/해설(일반 1,146+누적 8), SVG/manifest 1,355개·누락 0. translation audit 205 verified·0 stale. 비추적 실행 결과는 Git baseline 비교 대상이 아니며 wrapper freshness 검사를 사용한다.
- 최종 `scripts/build_site.ps1`(기존 실행결과 재사용) exit 0: 환경 진단, 자동검사 187개 중 186통과·선택 GPU 검사 1 skip, figure audit 1,355개·개념 audit 976개, source audit KO/EN, strict build KO 17.41초/EN 6.66초, bilingual merge 모두 통과. 각 언어 199페이지·1,154 details·reading tables199. 링크/자산/fragment 오류 0. 학습 순서·고유 배치·ID 노출·페이지 description/OG/Twitter·locale·canonical/hreflang·205페이지 sitemap·Search Console meta tag 검사 통과. GA4 runtime 모의검사 언어별19개 통과(실제 Google 요청 아님).
- 최종 병합 산출물 preview: `http://127.0.0.1:8006/ai-math-guide/` 및 `/en/`. 한영 홈페이지 실제 화면·description·canonical·인증 meta 확인. 로컬 동의 거부 후 읽기 가능, 가로 넘침 없음. 대표 화면을 `.build/release-proof/*-desktop-final.jpg`에 저장. 독립 전체 앵커 검토 및 공개 배포 검증은 다음 단계.
- 실제 host-root `https://leeklim.github.io/robots.txt`는 GitHub Pages 404. 호스트 robots 차단 규칙은 발견하지 않았으며 호스트 루트 변경 없음. 공개 HTML의 noindex 검사는 배포 후 별도 확인한다.

## 다음 작업

독립 최종 생성물 검토 확인 → 승인 범위의 main push·Pages 배포 → 실제 공개 주소·GA4 수신·Search Console 검증. 외부 계정 확인은 로컬 검사로 대체하지 않는다.
