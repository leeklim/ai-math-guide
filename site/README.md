# 사이트 운영 설정

## 방문 통계 (GA4)

GA4 측정 ID는 `G-VXDGRXQFT3`이며 `mkdocs.base.yml`에서 관리한다. 측정 ID는 공개 페이지의 태그에 포함되는 식별자이며 비밀번호나 API secret이 아니다. 2026-10-07 [한국어판 홈페이지](https://leeklim.github.io/ai-math-guide/) 공개 배포와 GA4 실시간 수신 확인을 완료했다. 아래 완료 기록에 배포 commit과 검수 범위를 남긴다.

공개 주소 `https://leeklim.github.io/ai-math-guide/` 아래에서 방문자가 통계 항목을 체크하고 동의한 뒤에만 Google 태그를 불러온다. 로컬 preview, HTTP, 다른 호스트와 다른 저장소 경로에서는 통계를 보내지 않는다. 방문자는 하단의 `통계 쿠키 설정`에서 동의를 바꾸거나 거부할 수 있다. 거부 뒤에는 추가 수집을 시작하지 않으며 기존 Google 쿠키와 이미 수집한 데이터를 자동 삭제하지는 않는다.

`overrides/partials/integrations/analytics/google.html`은 공개 주소·동의 여부를 확인하고 페이지마다 Google 태그를 한 번만 초기화한다. 현재의 일반 페이지 이동을 기준으로 하며 `navigation.instant`는 사용하지 않는다. 검색창 blur 이벤트를 보내지 않고 페이지 주소와 유입 주소에서 query와 hash를 제외한다. Google signals와 광고 개인 최적화 신호도 사용하지 않는다.

허용 주소는 `extra.analytics.public_url`에서 관리한다. MkDocs preview는 `site_url`을 로컬 주소로 바꾸므로 그 값을 수집 허용 기준으로 사용하지 않는다. 도메인이나 저장소 경로를 바꾸면 두 주소를 함께 확인한다.

연결 설정은 기존 Python unittest로 검사한다. Node.js가 있는 환경에서는 strict HTML build 뒤 프로젝트 루트에서 `node tests/analytics_runtime.cjs`로 공개·로컬 주소, 동의 여부와 중복 초기화를 검사할 수 있다. 이 검사는 DOM을 모의하므로 Google에 요청을 보내거나 방문 통계를 늘리지 않는다.

배포 뒤 공개 페이지에서 동의하고 이동한 다음 GA4의 실시간 보고서에서 수신을 확인한다. 이후 사용자·세션·페이지별 조회 보고서를 확인할 수 있다. 동의 거부, 추적 차단과 같은 이유로 수집하지 못한 방문은 통계에서 빠지므로 실제 방문자 전체를 정확히 센 값으로 해석하지 않는다. 공식 설정은 [Material의 방문 통계 안내](https://squidfunk.github.io/mkdocs-material/setup/setting-up-site-analytics/)와 [동의창 안내](https://squidfunk.github.io/mkdocs-material/setup/ensuring-data-privacy/)를 참고한다.

## 연결 검증 기록 (2026-10-07)

- 첫 화면 검수에서 preview의 `site_url` 재작성으로 로컬 태그 초기화 1회를 확인했다. 즉시 동의를 거부하고 `public_url`로 허용 주소를 분리했다. 첫 검수 방문이 GA4에 포함됐을 수 있으며 실제 데이터 수신 여부는 확인하지 않았다.
- 수정 뒤 production HTML과 실제 preview HTML 각각에 모의 런타임 검사 14개를 적용해 통과했다. 실제 로컬 페이지에서도 동의 뒤 GA 태그 0개, 거부 및 동의창 재열기 동작을 확인했다. preview의 주소 재작성에 대한 Python 회귀검사를 추가했다.
- Python unittest 137개 중 136개 통과, 1개 skip. source audit와 English-reading lint, strict HTML build 및 생성물 검증 통과. 단원 199개, 해설 1,154개, 깨진 링크·자산 0건을 확인했다.
- 동의창을 1440×900과 390×844에서 밝은·어두운 테마로 확인했다. 검수 화면은 `.build/ga4-consent-desktop.jpg`, `.build/ga4-consent-desktop-dark.jpg`, `.build/ga4-consent-mobile.jpg`, `.build/ga4-consent-mobile-dark.jpg`에 저장했다. 운영 안내는 공개 교재 본문에 추가하지 않았다.
- 이 연결 검증 단계에서는 GitHub 업로드, 저장소 공개 설정과 Pages 배포를 수행하지 않았다. 이후 공개 배포와 실제 수신 결과는 아래 완료 기록에 남긴다.

## 한국어판 초판 공개 준비 (2026-10-07)

사용자가 한국어판 원본·코드·기존 Git 이력을 포함한 저장소 공개와 GitHub Pages 배포를 승인했다. 이전 집필·그림 Goal의 공개 금지 기록은 당시 작업 범위로 유지한다. 현재 공개 배포 Goal에서만 commit·push·Public 전환·Pages 활성화를 수행한다.

- 공개 전 패턴 검사: 로컬 이력 27개 commit·648개 고유 blob과 현재 교재 파일을 확인했다. 토큰·개인 키·인증 URL·개인정보 패턴과 금지 경로에서 실질 검출 0건. 전문 비밀정보 스캐너는 사용하지 않았으며, 이 검사가 미검출 정보의 부재를 보증하지는 않는다.
- 원격 `main`은 로컬 HEAD의 조상이며 저장소 관리 권한을 확인했다. 무관한 `programming-assignment-1/`와 `tmp/`, 가상환경·캐시·GPU 결과·가중치·로그는 업로드 대상에서 제외한다.
- 공개 홈페이지에서 로컬 운영·대장·빌드 안내를 제외했다. 코드 블록의 `#` 주석이 절 제거를 중단하던 오류를 수정하고 회귀검사를 추가했다. 교재 본문·그림·문제와 해설은 이번 공개 준비에서 수정하지 않았다.
- 최종 로컬 검사: Python unittest 140개 중 139개 통과·선택 GPU 검사 1개 skip. CPU 예제 N05 28개·I06 12개·I07 17개·I08 13개 실행, source audit·English-reading lint·figure audit·concept audit의 두 완료 모드·strict HTML build·생성물 검증 통과. 199개 단원·해설 1,154개·SVG 1,355개, 깨진 링크·자산과 점검표 노출 0건을 확인했다.
- GA4 모의 런타임 검사 14개와 공개 홈페이지·배포 조건 검사를 통과했다. 저장된 SVG를 재생성하지 않았으며 새 모델·GPU 실험은 실행하지 않았다.
- workflow는 기존 build 검사를 유지하고 clean 환경의 I06~I08 결과 생성과 검증을 보충한다. `main` push 또는 수동 실행의 검증 성공 뒤 `.build/site`만 배포한다. PR에서는 배포하지 않는다.
- 이 기록 시점에는 GitHub 업로드·공개 전환·Pages 배포·공개 화면 검수와 GA4 실제 수신 확인이 남아 있다.
- 개정 내용을 17개 작업 단위와 공통 배포 설정 commit으로 정리했다. 배포 준비 commit은 `8abcac7`이며 원격 `main`보다 25개 commit 앞선 상태이다. GitHub push는 자동 보안 검토가 사용자 본인의 별도 재승인을 요구하여 실행되지 않았다. 원격 업로드·Public 전환·Pages 활성화는 아직 수행하지 않았다.
- GA4의 `AI Math Guide` 속성 보고서 접근을 확인했다. 첫 진입의 선택 이메일 알림 설정창은 사용자의 선택을 기다리며 저장하지 않았다. 실제 수신 검사는 공개 배포 뒤 수행한다.
- 사용자가 `leeklim/ai-math-guide`의 `main` push, Public 전환과 GitHub Pages 공개 배포를 별도로 명시 재승인했다. 최종 생성 HTML의 운영 안내 제외를 확인했고, 최신 로컬 검수 서버는 `http://127.0.0.1:8002/ai-math-guide/`이다. 이전 8001 서버와 재시작 시도 프로세스는 이 작업의 실행 명령·부모 관계를 확인한 뒤 정리했다.

## 공개 배포·실시간 수신 완료 (2026-10-07 13:36 KST)

- 검증한 한국어판을 `leeklim/ai-math-guide`의 `main`에 정상 push했다. 교재 배포 commit은 `fcaef3a4350b1da3a32609bb68aad1affb3111dd`이다. 저장소를 Public으로 전환하고 Pages의 GitHub Actions 배포를 활성화했다. 강제 push나 Git 이력 재작성은 하지 않았다.
- [Actions 실행 37571172622](https://github.com/leeklim/ai-math-guide/actions/runs/37571172622)의 clean Linux build와 Pages deploy가 모두 성공했다. 공개 홈페이지는 HTTP 200이며, 검증한 `.build/site`만 배포했다. 원본·대장·생성 코드의 Git 보관과 웹 자산을 구분했고 로컬 GPU 결과는 배포하지 않았다.
- 공개 홈페이지·목차·M03-11·N05-15·I07-07·A09-GEO-02와 대표 SVG·CSS·MathJax 설정·검색 색인을 확인했다. 단원 직접 진입과 새로고침, 수식 렌더링, SVG 로드, `자코비안` 검색 결과에서 M03-11 이동과 해설 펼치기가 정상 동작했다. 대표 수식의 렌더 오류와 깨진 그림은 0건이며 내부 작업 기록·집필자 점검표도 노출되지 않았다.
- 데스크톱 1440×900과 모바일 390×844에서 대표 화면을 밝은·어두운 테마로 확인했다. 모바일의 넓은 그림은 전용 영역의 가로 스크롤로 탐색할 수 있다. 검수 화면은 `.build/release-public-*`에만 저장하고 Git에는 올리지 않는다. 199개 단원·해설 1,154개·SVG 1,355개 보존과 최종 자동검사 근거는 위 공개 준비 기록을 따른다.
- 공개 페이지의 동의 전·거부 상태에서 GA 태그 0개, 통계 항목을 체크하고 동의한 뒤 `G-VXDGRXQFT3` 태그 1개를 확인했다. 최신 로컬 preview는 동의 뒤에도 태그 0개였다. 화면 검수 동안은 통계를 거부하고, 실제 수신 확인을 위해 공개 홈에서 최소 테스트 방문만 수행했다.
- GA4 `AI Math Guide` 속성의 `Reports → Realtime overview`에서 홈페이지 제목과 `page_view`·`first_visit`·`session_start` 각 1건을 확인했다. `Realtime pages`에서도 `/ai-math-guide/`의 활성 사용자 1명·조회 1회를 확인했다. 증거는 `.build/release-ga4-realtime.png`에 저장했다. 태그 존재만으로 수신 완료를 판단하지 않았다. 첫 연결 검수의 로컬 방문 수집 가능성 기록은 유지한다.
- GA 보고서의 선택 이메일 설정은 변경하지 않았다. 이후 보고서에 접근할 수 있어 수신 검사를 완료했다. 이 문서는 웹 자산에서 제외되는 운영 기록이므로 기록 전용 commit에는 `[skip ci]`를 사용해 같은 교재를 다시 빌드·배포하지 않는다. 동작 근거는 [GitHub workflow 실행 생략 안내](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/skip-workflow-runs)를 따른다.

남은 공개 배포 작업은 없다. 방문 현황은 GA4의 실시간 보고서와 사용자·세션·페이지별 조회 보고서에서 확인한다.

## 영문판 로컬 구축 시작 (2026-10-07)

사용자가 전체 199개 단원의 원문 기반 영문 재서술과 한영 선택 로컬 사이트 Goal을 승인했다. 이 단계는 한국어 원본·공개 URL·SVG·실습 코드를 보존한다. 영문 원본은 `translations/en/`, 대응과 검토 기록은 `revision/translation-audit.csv`에 둔다. 단원별 국소 검사, 17개 작업 단위 끝의 HTML 반영, 최종 통합 검증을 수행한다.

별도 최종 승인 전 모든 원격 브랜치 push·PR·공개 preview·배포를 금지한다. 한국어판 공개 승인은 영문 초안 공개 승인으로 확대하지 않는다. 기반 구현과 표본 M00-03·M03-11·N05-15·I07-07·A09-GEO-02의 작성·대조 검토부터 시작하며, 아직 영문판 검증이나 공개 준비 완료를 주장하지 않는다.
