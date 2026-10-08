# 한영 탐색 구조·검색 정보·공개 배포 진행

## 기준과 승인

- 전체 수행 기준: `site/RELEASE-PLAN.md`.
- 기준 커밋: `07549af` (`codex/english-edition`). 추적 파일 수정 없음. 무관한 미추적 `programming-assignment-1/`, `tmp/` 보존.
- 이전 검증 기록의 기준 수량: 언어별 199개 단원·1,154개 문제/해설·205개 공개 문서, 공유 SVG 1,355개. 이번 작업의 통합 보존 검사는 최종에 수행한다.
- 대표 화면 검증 후 전권 적용, 최종 검증 후 `leeklim/ai-math-guide` main push·GitHub Pages 공개 배포를 사용자가 사전 승인했다. 두 지점에서 재승인을 기다리지 않는다.
- 수학 내용 정정과 범위 확대는 별도 승인 대상이다. 기존 원문 의문점은 정정 없이 기록 분류만 유지한다. 철회된 M00-10 작은 cross-entropy 우려는 제외한다.

## 현재 단계

- 전체 지시 보관·프로젝트 명세·문체·단원 템플릿 확인 후 한영 탐색/공유 정보 개정과 공개 배포 완료.
- 표본 설명 5개를 원문과 대조 검토하고 국소 문구 보완 완료. 공통 공개 표시 변환·4부 탐색 구조·앵커 보존·학습 순서 footer·검색/공유 metadata 구현.
- 대표 화면 검수 통과 후 전권 적용 완료. 17개 단위·205개 경로의 한영 설명을 두 작성자가 작성하고 별도 검토자가 원문과 대조했다. 205/205 검토 통과, 조건·용어의 국소 수정 반영, 현재 차단 결함 0. 원고 재작성 없음.
- 실제 GA4 실시간 수신, 승인된 Search Console URL-prefix 소유권 인증 및 한영 sitemap 제출 완료. 공개 XML과 Google Live Test 접근도 확인했다. sitemap 보고서의 `Couldn't fetch`와 색인 여부는 별도 외부 상태이며 처리 완료로 주장하지 않는다.

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
- 독립 최종 생성물 검토 통과: 398단원의 원래 본문 heading anchor 11,282개·기존 실습 포함 공개 anchor 11,778개·한영 참고 페이지 anchor128개 누락0. 410페이지 중복 ID·metadata/언어 대응·인증 tag·일반 읽기 텍스트 관리ID 노출 오류0. footer/head 이전·다음은 양언어199단원의 교육순서와 일치. 각 언어 formal nav205경로 고유, sitemap205개 정확. 원고/그림/lab diff0. 범위 참조의 끝점과 기존 href 보존.
- 최종 모바일 재확인: 실제 `innerWidth=390, innerHeight=844`에서 A09-GEO-02 한영·밝은/어두운 테마 줄바꿈·가로 넘침0 확인. viewport 대상은 활성 탭으로 선택하여 실제 치수를 확인했다.
- 로컬 커밋: `8dc09e9` 수행 명세·진행 기록, `8718842` 공통 탐색/표시/SEO/검증, `8382825` 기초·참고 설명76페이지, `1bdbf76` 신경망·해석·심화 설명129페이지. 이 단계는 로컬 준비 완료이며 공개 배포 완료와 구분한다.
- 승인된 일반 push 성공: remote main `92f44ff` → `ab9a5364817bcfd01ad53e8c349c6a9da4dbd437`. 로컬 main도 같은 커밋으로 fast-forward 동기화(원고 파일 재checkout 없음). 작업 브랜치는 `codex/english-edition` 유지. force push/이력 재작성 없음. 무관한 미추적 두 폴더 미포함.
- GitHub Actions 실행 #22 시작: `https://github.com/leeklim/ai-math-guide/actions/runs/37621526345`, push 커밋 `ab9a536`, build 진행 중. 공개 배포와 사후 검증은 아직 완료 처리하지 않는다.
- #22 공개 배포 성공: build4분35초, deploy11초, 총4분55초. 실제 영문 홈페이지·처음부터 시작→영문 첫 단원 및 새 metadata/인증 tag 확인. 동의 전 GA script 없음, 체크 후 Accept 시 올바른 G-VXDGRXQFT3 script 로드 확인(실제 GA 대시보드 수신 확인 전).
- Search Console HTML tag 소유권 인증 실제 성공(`Ownership verified`). 승인된 URL-prefix 속성에만 적용. 사이트맵 제출 진행 중.
- 공개 화면 점검에서 홈의 OG/Twitter 제목이 일반 메뉴명 Home/홈으로 나오는 문제를 발견. 홈페이지에만 locale 교재명 사용하도록 template3줄·검증2줄 수정. 본문·원고·URL 변경 없음. 공통 template 변경이므로 관련 재검증·재배포 후 실제 공개 메타 값을 확인한다.
- 홈 공유 제목 수정 후 `scripts/build_site.ps1` 재검증 exit0: 187검사 중186통과·선택GPU1skip, figure/concept/source/reading audit 및 한영 strict build·병합 통과(KO6.53초, EN8.19초). 링크/자산/fragment 오류0, translation205 verified·0stale, 각 언어199단원·1,154해설 유지. GA4 모의검사 각19개 통과. 기존 신선한 실습 결과 재사용.
- 실제 GA4 Realtime pages 보고서 수신 확인: 공개 `/en/`와 `/en/part-1-foundations/M00/M00-01-numbers-variables/` 시험 방문이 사용자1명·조회2건으로 표시됐다. 로컬 모의검사와 구분하며 시험 트래픽은 실제 방문자 성장 지표가 아니다. 증거 화면은 `.build/release-proof/ga4-public-receipt.jpg`에 저장.
- Search Console 한국어 `sitemap.xml` 제출 성공 알림 확인. 제출 직후 상태는 `Couldn't fetch`, 상세 주소는 올바른 프로젝트 경로. 가져오기 완료로 기록하지 않으며 영문 제출과 공개 XML 응답 확인을 이어간다.
- `09f9eae163b50f9b08985ae4ed7251cf1ca8c6ba` 정상 push와 로컬 main fast-forward 완료. GitHub Actions #23 `https://github.com/leeklim/ai-math-guide/actions/runs/37623250076` build4분53초·deploy12초·총5분15초 Success 확인. 실제 공개 홈 재로드 후 KO/EN OG·Twitter 제목이 각 교재명, canonical/한영 alternate 정상임을 확인. 독립 검토자도 해당 국소 diff와 병합 HTML의 회귀 없음 확인.
- Search Console 영문 `en/sitemap.xml`도 실제 `Sitemap submitted successfully` 확인. 두 제출 행의 상태는 마지막 관찰에서 `Couldn't fetch`, 발견 페이지0. 별도 실제 HTTP GET에서 두 XML 모두200·application/xml·205개 고유loc, 로컬 병합 XML과 완전히 동일, URL 차이0·X-Robots-Tag 없음. Google URL Inspection의 Live Test도 두 sitemap 모두 `URL is available to Google` 확인. 제출·접근 검증은 완료했으나 Google 사이트맵 처리/색인은 완료로 주장하지 않는다. 제출과 Live Test 증거는 `.build/release-proof/search-console-*.jpg`.
- 실제 공개 KO/EN 기초 M00-03·해석 I07-07·심화 A09-GEO-02, EN M03-11, KO/EN N05-15 확인. 관찰 단원의 수식 오류요소·로드 완료 후 깨진 그림·가로 넘침0, canonical/lang/noindex 검사 정상. N05-15 그림9개·수식57개·표2개·코드3개와 본문/캡션 표시 확인. 대표 공개 화면은 `.build/release-proof/public-*.jpg`.
- 실제 공개 모바일390×844에서 KO N05-15 밝은 화면, EN curriculum 어두운 화면, EN Jacobian 밝은/어두운 화면과 줄바꿈 breadcrumb 확인. 모바일 메뉴→학습경로, 같은 페이지 언어 전환, EN 검색 Jacobian29문서→단원 진입·현재 위치, 선수 total derivative→Jacobian 복귀, next→Hessian 이동 확인. 긴 줄바꿈 링크는 자동 클릭 중심이 빈 영역에 놓여 키보드 Enter로 목적지 이동을 확인했다. 페이지 코드 수정 없이 실제 링크 주소와 교육순서 확인.
- 공개 분석 동의를 시험 후 Reject로 원복하고 새 로드에서 Google tag script 없음 확인. GA4 실제 수신은 `Realtime pages`의 `Last 30 min`에서 확인했으며 일반 보고서의 사용자 지정 날짜를 변경한 검사가 아니다. 추가 검수 방문으로 이후1사용자·11조회가 표시됐으며 초기1사용자·2조회 기록과 구분한다.
- 한국어 `자코비안` 검색은 실제1문서·Jacobian 단원 주소로 표시됨을 확인. 공개 한영 홈 모바일390×844·어두운 테마의 제목/표/가로 넘침0 확인 후 밝은 테마로 원복하고 임시 viewport override를 해제했다. 검수용 검색 입력을 비웠고 시험 동의는 거부 상태 유지. 공개 EN 페이지·GA4·Search Console만 결과 탭으로 보존하고 생성한 임시 로컬/robots/Actions 탭을 닫았다. 사용자 원래 탭은 닫지 않았다.

## 다음 작업

필수 구현·보존·통합검사·공개배포·실제 사후검증·GA4 수신·Search Console 인증/제출 작업은 완료했다. 사이트 산출물을 바꾸지 않는 최종 기록만 `[skip ci]` 커밋으로 main에 정상 push한다. Google sitemap 보고서의 `Couldn't fetch` 상태는 남아 있으며 원인을 확정하지 않았다. 두 XML의200응답과 Google Live Test 접근은 통과했으므로 가져오기/색인 완료나 향후 처리 시점을 약속하지 않는다. 검색 순위·방문자 증가·색인 날짜는 이 Goal의 완료 조건이 아니다.

## GA4와 첫 방문 동의창 제거 (2026-10-08)

- 사용자 요청에 따라 공통 GA4·동의 설정, Google provider override와 한영 하단 동의 설정 링크를 제거했다. 영어 설정 생성의 consent 직접 접근과 동의 fragment의 무조건 허용 예외도 제거했다. 검색·언어 전환·테마 저장 범위·Search Console 인증은 유지한다. 단원 원고·문제/해설·그림·실습 파일은 변경하지 않았다.
- 기존 GA4 검사와 로컬/CI 호출을 비수집·동의창 부재 검사로 바꿨다. 제거 전 회귀검사의 실패를 확인했고, 수정 뒤 기본 설정/템플릿 검사는 통과했다. 최초 관련 단원 검사에서 임시 폴더 권한 오류가 발생해 프로젝트 `.build/ga4-removal-temp`를 해당 검사 프로세스의 임시 경로로 지정했다. 이후 `build_site.ps1`의 Python 검사185개 중184개 통과·선택 GPU1개 skip, 번역205건 verified·stale0, figure/concept/source/reading audit와 한영 strict build를 통과했다. 새 모델·GPU 실험·그림 재생성은 실행하지 않았다.
- 생성한 KO/EN HTML 각206개에서 GA4 initializer·태그/ID·동의창·하단 설정 링크 부재를 확인했다. 로컬 한영 첫 화면에서도 동의 UI와 Google tag가 각각0개였고 본문이 보였다. 화면 근거는 `.build/release-proof/no-consent-ko.jpg`와 `no-consent-en.jpg`에 저장했다. 샌드박스 안의 preview 연결 오류 뒤 해당 검수 서버를 종료하고 생성 교재만127.0.0.1에서 제공하는 서버로 확인했다.
- `build_site.ps1` 전체 실행이 exit0으로 끝났다. 양언어199개 단원·문제/해설1,154쌍을 유지했고 locale/최종 병합 링크·자산 오류0건, 동의/GA 태그 부재 검사 각206페이지 통과를 확인했다. 기록 문서 갱신은 웹 산출물에 영향을 주지 않아 검사를 다시 실행하지 않았다. 로컬 검수 주소는 `http://127.0.0.1:8005/ai-math-guide/`와 대응 `/en/`이다.
- 공개 배포는 사용자 응답 대기이며 원격 push·배포는 실행하지 않았다. 대체 접속 집계는 연결하지 않았고 GA4 계정·과거 데이터·기존 Google 쿠키는 삭제하지 않았다. 앞선2026-10-07 기록은 당시 GA4를 사용하던 상태의 이력으로 유지한다.

## Cloudflare 집계·한영 안내 연결 (2026-10-08)

- 사용자가 가입한 Cloudflare 계정의 Web Analytics에 `leeklim.github.io`를 등록했다. 공개 beacon token을 공통 설정에 연결했으며 API 비밀키·DNS·호스팅·결제 설정은 변경하지 않았다. 태그는 정확한 HTTPS 공개 origin과 `/ai-math-guide/` 경로에서만 한 번 로드된다. 로컬·다른 호스트·유사 경로는 수집하지 않는다.
- 한국어 `PRIVACY.md`와 대응 영어를 추가하고 전 페이지 하단에 해당 언어의 안내 링크를 연결했다. Visits와 고유 인원 수의 차이, 조회·성능 통계, 전송·차단에 따른 누락, 브라우저 환경설정과 외부 서비스 요청을 고지한다. 쿠키 미사용을 모든 국가의 법적 면제나 데이터 전송 부재로 설명하지 않는다. Google Fonts 요청은 GA4와 구분해 고지했다.
- 독립 검토자가 한영 의미 대응과 실제 config/template/inventory/test diff를 검토했다. 단원 원고·문제/해설·그림·실습 변경은 없으며 무관한 미추적 두 폴더는 보존한다. 사용자는 검증 후 GA4·동의창 제거와 Cloudflare·안내 변경을 함께 main에 push하고 공개 배포하도록 명시 승인했다.
- Python unittest189개 중188개 통과·선택 GPU1개 skip. 양언어 source audit/English-reading lint와 strict HTML build 통과(KO16.17초, EN17.08초). 저장 그림 audit1,355개와 concept audit976개 통과. 생성 HTML 검사 각207파일에서 GA4·동의 UI 부재와 언어별 안내 링크를 확인하고, 공개/로컬/유사 경로 및 중복 로드10조건을 네트워크 없는 모의검사로 확인했다.
- 실제 로컬 KO/EN 안내 페이지의 본문·외부 링크·footer·줄바꿈을 확인했다. 동의 UI·Google tag·로컬 Cloudflare tag·가로 넘침은 각각0이었다. desktop 화면은 `.build/release-proof/cloudflare-notice-ko.jpg`와 `cloudflare-notice-en.jpg`에 저장했다. 신규 안내의 번역 대장을 verified로 기록했으며 공개 문서는 언어별206개다. 새 모델·GPU 실험·그림 재생성은 수행하지 않았다.
- 배포 전 등록 대시보드는 GMT+9·Last24hours·bot 제외에서 Visits/Page views0을 표시했다. 이는 공개 태그 배포 전 상태이며 수신 완료를 뜻하지 않는다. 한영 통합 검증·공개 배포·실제 수신 확인을 이어간다.
- KO/EN 각각의 전체 생성물 검증을 통과했다. 각199단원·1,154해설·reading table199개, 링크/자산 오류와 점검표 노출0건이다. 언어 간 최종 링크 검사는 로컬에서 계속하며 GitHub에서도 동일한 최종 검증이 배포 선행 조건이므로 승인된 main push와 CI를 병렬로 진행한다. 이 단계는 공개 배포 성공이나 실제 통계 수신 완료로 기록하지 않는다.
- `a512b9f05e4f80b4d3bfd45841d1a7aff17690f9`를 정상 커밋·main push했다. 이전 원격 main은 로컬 준비 기준 `d27ce9c`와 같았고 force push·이력 재작성은 하지 않았다. 요청 범위20파일만 포함했으며 무관한 두 폴더는 미추적 상태로 남는다.
- [Actions #24](https://github.com/leeklim/ai-math-guide/actions/runs/37760310996)의 clean 전체 검사·한영 strict build·최종 병합과 Pages deploy가 Success였다(build3분9초, deploy34초). 공개 KO/EN 홈페이지와 안내 페이지에서 GA 태그·동의 UI0, 올바른 Cloudflare module tag1개와 언어별 footer 주소를 확인했다. 공개 footer 안내 진입과 같은 안내의 영어 전환도 확인했다. 관찰 페이지의 console 오류와 가로 넘침은0이었다.
- Cloudflare에서 실제 공개 테스트 조회 수신을 확인했다. `leeklim.github.io`·Last24hours·GMT+9·bot 제외에서 Visits1·Page views8·load time565ms를 표시했다. 이는 연결 검수 트래픽을 포함하며 실제 독자 증가로 해석하지 않는다. 최초0값은 등록/배포 직후 상태였다. 계정 식별 정보가 제외된 화면을 `.build/release-proof/cloudflare-public-receipt.jpg`에 저장했다. 시험용8007서버는 종료했고 기존8005 교재 preview는 유지한다.
- 로컬 `site.py merge`의 최초 실행은25분 이상 CPU 계산을 이어가 중단했다. 같은 기존 명령을 호스트 실행 환경에서 다시 실행하여 exit0으로 마쳤다. 검사 코드·기준은 변경하지 않았고, 정확한 성능 원인을 프로파일링하지는 않았다. 최종 병합 링크/자산 오류0건, 번역206개 present/reviewed/verified·missing/unreviewed/stale0건을 확인했다. 갱신한 README와 이 기록은 공개 원고·산출물에 영향을 주지 않으므로 전체 검사를 재실행하지 않는다.
- 필수 구현·공개 배포·실제 수신 검증은 완료했다. 공개 홈페이지와 Cloudflare 대시보드를 결과 탭으로 남기고 임시 Actions 탭을 닫았다. 최종 기록2파일만 `[skip ci]` 커밋으로 정상 main push하여 같은 교재를 다시 배포하지 않는다. DNS·호스팅·결제·GA4 계정/과거 데이터와 Search Console 설정은 변경하지 않았다.
