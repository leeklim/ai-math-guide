---
id: "A09-RMT-03"
title: "표본 공분산의 spectrum"
part: 4
stage: "A09-RMT"
status: "완료"
prerequisites: ["M02-12", "M02-14", "M04-06"]
estimated_time: "90~120분"
---

# A09-RMT-03. 표본 공분산의 spectrum

## 이 단원이 필요한 이유

activation covariance의 eigenvalue를 population variance direction으로 읽으려면 finite sample noise를 고려해야 한다. dimension $d$가 sample 수 $n$과 비슷하면 population covariance가 identity여도 sample eigenvalue가 넓게 퍼진다.

## 학습 목표

- centered data matrix에서 sample covariance를 계산할 수 있다.
- covariance rank가 sample 수와 dimension에 제한되는 방식을 설명할 수 있다.
- aspect ratio가 spectral noise에 미치는 영향을 설명할 수 있다.
- activation covariance 비교에서 experimental unit을 정할 수 있다.

## 선수지식 확인

- 선수 단원: [M02-12 대칭행렬과 스펙트럼 정리](../../part-1-foundations/M02/M02-12-symmetric-matrices-spectral-theorem.md), [M02-14 공분산과 PCA](../../part-1-foundations/M02/M02-14-covariance-pca.md), [M04-06 표본, 모집단과 표본분포](../../part-1-foundations/M04/M04-06-samples-populations-sampling-distributions.md)
- 확인 질문: centered data matrix $X\in\mathbb R^{n\times d}$에서 $X^\top X$의 shape은 무엇인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $X_c$ | `the centered data matrix X c` | feature별 sample mean을 뺀 data matrix | $n\times d$ |
| $S=\frac1nX_c^\top X_c$ | `S equals one over n times X c transpose X c` | sample covariance convention | $d\times d$ |
| $\gamma=d/n$ | `gamma equals d over n` | dimension-to-sample aspect ratio | positive scalar |
| $\lambda_j(S)$ | `the j th eigenvalue of S` | sample variance eigenvalue | nonnegative scalar |

## 핵심 개념

row가 sample이고 column이 feature인 centered matrix $X_c$에 대해

$$
S=\frac1nX_c^\top X_c
$$

를 sample covariance로 둔다. $1/(n-1)$ convention도 있으므로 보고서에 denominator를 적는다. $S$는 PSD이고 $\operatorname{rank}(S)\le\min(d,n-1)$이다. $d\ge n$이면 적어도 $d-n+1$개의 zero eigenvalue가 생긴다.

고정된 작은 $d$에서 $n$이 커지는 classical regime에서는 $S$가 population covariance에 접근한다. $d/n\to\gamma>0$인 high-dimensional regime에서는 eigenvalue 하나하나가 사라지지 않는 sampling noise를 가진다. identity population조차 nontrivial spectral bulk를 만든다.

activation row가 token이면 같은 prompt 안 token의 dependence가 effective sample size를 줄일 수 있다. rank 계산의 $n$과 uncertainty를 위한 independent unit 수를 구분해야 한다.

## 작은 예제

$n=40$, $d=100$인 centered data에서는 rank가 최대 39이다. $S$는 최소 61개의 zero eigenvalue를 가지며, 이 zero들은 population covariance의 61개 정확한 null direction을 증명하지 않는다.

## 흔한 오해

- sample eigenvalue가 서로 다르다는 사실만으로 population anisotropy를 증명할 수 없다.
- token 수를 independent sample 수로 그대로 쓰면 prompt-level dependence를 무시할 수 있다.

## 연습문제

### 1. shape
$X_c$가 $80\times300$이면 $S$의 shape은 무엇인가?
<details><summary>해설 보기</summary>

$X_c^\top X_c$이므로 $S$는 $300\times300$이다.
</details>

### 2. rank
$n=25$, $d=60$인 centered data의 covariance rank와 zero eigenvalue 수에 대한 상한·하한을 쓰라.
<details><summary>해설 보기</summary>

rank는 최대 $n-1=24$이고 zero eigenvalue는 최소 $60-24=36$개이다.
</details>

### 3. aspect ratio
$d=500$, $n=1000$이면 $\gamma$는 얼마인가?
<details><summary>해설 보기</summary>

$\gamma=d/n=0.5$이다.
</details>

### 4. 모델 해석
한 prompt당 token 50개씩 20개 prompt를 모았다. covariance matrix의 row 수와 bootstrap unit을 각각 무엇으로 둘 수 있는가?
<details><summary>해설 보기</summary>

조건을 고정하면 matrix row는 token 1,000개로 둘 수 있지만 uncertainty bootstrap의 최상위 unit은 prompt 20개로 둔다.
</details>

## 근거와 갱신 경계

sample covariance normalization은 $1/n$을 사용한다. dependent row와 heavy tail은 다음 null model의 iid 가정을 어기므로 별도 진단이 필요하다.

## 단원 요약

- sample covariance는 centered data의 Gram operator이다.
- rank는 $d$와 $n-1$ 중 작은 값에 제한된다.
- high-dimensional regime에서는 identity population도 넓은 sample spectrum을 만든다.
- matrix row 수와 independent resampling unit 수는 다를 수 있다.

## 통과 기준

- sample covariance의 shape·rank·aspect ratio를 계산할 수 있는가?
- sample eigenvalue dispersion과 population signal을 구분해야 하는 이유를 설명할 수 있는가?

## 다음 단원

- [A09-RMT-04 Marchenko–Pastur 법칙의 직관](A09-RMT-04-marchenko-pastur-intuition.md)

## 집필자 점검표

- [x] covariance spectrum의 rank와 high-dimensional noise를 설명했다.
- [x] 문제 4개에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 선수지식과 링크를 확인했다.
