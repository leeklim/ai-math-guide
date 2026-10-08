# 개인정보·통계 안내

갱신일: 2026-10-08

이 교재는 회원가입 없이 읽을 수 있다. 사이트 운영자는 접속량과 페이지 품질을 확인하기 위해 Cloudflare Web Analytics를 사용한다. Google Analytics(GA4)는 사용하지 않는다.

## 방문·조회 집계

Cloudflare는 Visits(유입 방문 횟수), Page views(페이지 조회 수), 로딩 시간과 웹 성능 지표를 집계한다. 보고서에는 페이지 경로, 유입 사이트, 국가, 기기 종류, 브라우저와 운영체제별 구분도 포함된다. Visits는 고유한 사람 수가 아니며, 한 번의 방문에서 여러 페이지를 읽을 수 있다. [집계 지표](https://developers.cloudflare.com/web-analytics/data-metrics/high-level-metrics/)와 [보고서 구분 항목](https://developers.cloudflare.com/web-analytics/data-metrics/dimensions/)에서 정의를 확인할 수 있다.

Cloudflare는 사용량 집계에 쿠키나 localStorage를 사용하지 않고, IP 주소나 브라우저 정보를 조합해 개인을 식별하는 지문을 만들지 않는다고 설명한다. [Cloudflare의 개인정보 보호 설명](https://www.cloudflare.com/web-analytics/)을 참고한다.

브라우저는 집계 정보를 Cloudflare 서버로 전송한다. 사이트 운영자는 Cloudflare 관리자 화면에서 통계를 확인하며, 개인별 방문 기록을 만들거나 광고 타기팅에 사용하지 않는다. 집계는 공개 교재 주소에서만 동작하고 로컬 검수 주소에서는 동작하지 않는다. 서비스의 정보 처리와 보관에 관한 사항은 [Cloudflare 개인정보 처리방침](https://www.cloudflare.com/privacypolicy/)에서 확인할 수 있다.

브라우저의 콘텐츠 차단 기능이나 확장 프로그램으로 Cloudflare 집계 요청을 차단할 수 있다. 집계 코드를 차단해도 교재를 읽을 수 있다. 차단이나 전송 실패 때문에 조회 수가 실제 접속보다 적을 수 있다.

## 브라우저 설정과 외부 서비스

교재 화면은 테마 등 읽기 설정을 브라우저 저장소에 보관할 수 있다. 이 저장값을 방문 통계용 개인 식별자로 사용하지 않는다.

GitHub Pages가 웹페이지를 제공하고, 수식 표시를 위해 외부 CDN에서 MathJax를 불러온다. 브라우저는 이 서비스에도 요청을 보낸다. 각 서비스의 정보 처리는 [GitHub 개인정보 처리방침](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement)과 [UNPKG 안내](https://unpkg.com/)를 참고한다.

화면의 글꼴은 Google Fonts에서 불러온다. 이 글꼴 요청은 Google Analytics 집계와 별개다. [Google Fonts 개인정보 안내](https://developers.google.com/fonts/faq/privacy)에서 처리 방식을 확인할 수 있다.

사이트 관련 문의는 [교재 GitHub 저장소](https://github.com/leeklim/ai-math-guide)를 통해 할 수 있다. 공개 게시물에 비밀번호나 민감한 개인정보를 적지 않는다.
