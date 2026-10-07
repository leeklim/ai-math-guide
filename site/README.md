# 사이트 운영 설정

## 한영 로컬 빌드와 검수

영문판 작업은 별도 최종 공개 승인 전까지 로컬에만 보관한다. 아래 명령은 원격 push·PR·preview 업로드·Pages 배포를 실행하지 않는다. 기존 한국어판의 공개 기록과 승인은 영문판 공개 승인으로 확대하지 않는다.

```powershell
.\scripts\build_site.ps1
.\scripts\preview_site.ps1 -SkipBuild -Port 8003
```

빌드는 먼저 `check-translations --require-verified`로 199개 단원과6개 부속 문서의 실제 검토 상태·원문/영문 hash를 확인한다. 빠진 원고·미검토·stale가 있으면 중단한다. 한국어 `.build/ko/site`와 영어 `.build/en/site`를 별도 strict build하고 검사한 뒤 `.build/bilingual/site`로 병합한다. 기존 `.build/site`는 덮어쓰지 않는다. 최종 Pages workflow도 한영 병합 경로만 업로드하도록 준비하며, 실제 원격 실행은 최종 승인 뒤에만 수행한다.

로컬 기본 빌드는 `.build`의 기존 필수 CPU 결과를 재사용한다. staging은 각 예제 코드의 source hash와 결과 필드를 검사하고, 환경 진단은 고정된 Python·NumPy·CPU PyTorch를 확인한다. 예제·공통 계산 코드나 환경을 변경했거나 결과가 없다면 `build_site.ps1 -RunExamples`로 N05·I06·I07·I08 결과를 각1회 생성한다. 공통 코드·환경 변경까지 자동으로 추적하는 별도 결과 캐시는 없으므로 이 경우 재실행이 필요하다. clean CI에서는 기존 네 CPU runner를 각1회 실행하고 양언어가 결과를 공유한다. 테스트 안의 작은 계산과 결과 생성 runner는 구분한다. GPU 결과·모델 가중치는 공개 빌드에 포함하지 않는다.

preview는 병합 HTML만127.0.0.1에서 정적으로 제공한다. 한국어는 `http://127.0.0.1:8003/ai-math-guide/`, 영어는 `http://127.0.0.1:8003/ai-math-guide/en/`이다. `-SkipBuild`는 이미 생성된 HTML을 읽는 옵션이므로 Markdown 수정은 자동 반영되지 않는다. 원문 수정 뒤에는 대응 영문을 대조 검토해 stale를 해소하고 다시 빌드한 후 페이지를 새로고침한다. 이미8003 포트가 사용 중이면 다른 포트를 지정한다.

한영 GA4 동의 scope는 같으며 로컬 수집은 차단된다. Node.js의 `node tests/analytics_runtime.cjs .build/ko/site/index.html`과 대응 영어 경로 검사로 양언어를 각각 확인한다. 실제 Google 수신은 영문판 공개 승인·배포 뒤에 확인하며 모의 검사 통과와 구분한다.

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

## 영문판 로컬 완성·공개 준비 완료 (2026-10-07)

위 시작 기록은 당시 상태다. 영문199개 단원과 독자용 부속 문서6개를 작성·독립 대조·HTML 확인했으며 검토205건 모두 verified, 누락·미검토·stale0건이다. 한국어199개 단원·문제/해설1,154쌍·SVG1,355개와 공유 생성/실습 원본을 보존했고 영어도 단원별1,154쌍이 대응한다. 원문에서 이어진 오류·모호성 후보는 `revision/english-progress.md`에 별도로 기록했으며 영문화 과정에서 몰래 정정하지 않았다.

실제 기본 `build_site.ps1` 전체 실행을 완료했다. Python unittest177개 중176개 통과·선택 GPU 검사1개 skip, 저장 그림/개념 감사, 양언어 source audit·English-reading lint·분리 strict build·완성 병합·GA4 mock각19개가 통과했다. 양언어 깨진 링크·자산·점검표 노출0건이다. 기존 CPU 결과를 신선도 확인 후 재사용했으며 네 예제 runner·GPU/모델·그림 재생성은 실행하지 않았다.

17작업 단위 대표와 표본5개를 데스크톱/모바일·양테마에서 실제 검수했다. 최종 완성 build에서는 표본5개·긴 수식 해설2페이지·영문 홈/용어집을 다시4조건으로 확인했다. 언어 전환과 새로고침 뒤 동의·거부 공유를 실제 확인했고, 로컬 Google script는 동의 뒤에도0개다. 검수 후 거부 상태와 기본 viewport를 복원했다. 접근성 MathML은 유지하지만 실제 스크린리더 음성 검사는 하지 않았다. Material의 불필요한 깊은 경로 sitemap 요청 오류와 기타 제한은 진행 기록을 따른다.

현재 검수 서버는 `preview_site.ps1 -SkipBuild -Port 8004`로 실행했다. [한국어 로컬 홈](http://127.0.0.1:8004/ai-math-guide/)과 [English local home](http://127.0.0.1:8004/ai-math-guide/en/)에서 상단 언어 선택을 사용할 수 있다. 산출물은 `.build/bilingual/site`이며 정적 서버라 Markdown 수정이 자동 반영되지 않는다. 대응 영어를 재검토하고 다시 빌드해야 한다.

로컬 완성본의 사용자 검수와 별도 최종 공개 승인만 후속 단계로 남는다. 이번 영문판 Goal에서는 원격 push·PR·공개 preview 업로드·Pages 배포를 하지 않았다. 기존 한국어 공개 홈페이지를 변경하지 않았으며 영어 공개 주소와 GA4 실제 수신 확인은 승인 후 배포 때 검증한다. 상세 근거와 원문 주의 항목은 `revision/english-progress.md`, 개별 검토 hash는 `revision/translation-audit.csv`에 있다.
