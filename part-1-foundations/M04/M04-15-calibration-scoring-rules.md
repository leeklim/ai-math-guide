---
id: "M04-15"
title: "calibration과 scoring rule"
part: 1
stage: "M04"
status: "완료"
prerequisites:
  - "M04-03"
  - "M04-04"
  - "M04-06"
  - "M04-07"
  - "M04-08"
  - "M04-12"
estimated_time: "150~180분"
---

# M04-15. calibration과 scoring rule

## 이 단원이 필요한 이유

classification model이 정답 label을 자주 맞히는 것과 출력 probability가 믿을 만한 것은 다른 문제이다. confidence $0.8$인 prediction들을 모았을 때 약 $80\%$가 맞아야 그 confidence가 empirical frequency와 맞는다고 말할 수 있다. 이 성질을 calibration이라 한다.

calibration만으로 probability prediction의 품질이 모두 정해지지는 않는다. base rate만 내놓는 model도 집단 전체에서는 calibrated할 수 있지만 sample을 구별하지 못한다. reliability diagram과 expected calibration error(ECE)는 calibration gap을 요약하고, log score와 Brier score 같은 proper scoring rule은 prediction distribution 전체의 품질을 평가한다.

## 학습 목표

이 단원을 마치면 다음을 할 수 있다.

- binary calibration을 conditional expectation으로 정의할 수 있다.
- accuracy와 calibration을 구분할 수 있다.
- confidence bin의 accuracy와 confidence를 계산할 수 있다.
- reliability diagram과 ECE를 해석할 수 있다.
- proper scoring rule의 조건을 설명할 수 있다.
- log score와 Brier score를 계산할 수 있다.
- sharpness, temperature scaling과 distribution shift의 관계를 설명할 수 있다.
- calibration 결과가 허용하는 모델 해석 주장을 제한할 수 있다.

## 선수지식 확인

- 선수 단원: [M04-03 확률변수와 확률분포](M04-03-random-variables-distributions.md)
- 선수 단원: [M04-04 기댓값, 분산과 공분산](M04-04-expectation-variance-covariance.md)
- 선수 단원: [M04-06 표본, 모집단과 표본분포](M04-06-samples-populations-sampling-distributions.md)
- 선수 단원: [M04-07 추정, 편향과 분산](M04-07-estimation-bias-variance.md)
- 선수 단원: [M04-08 회귀와 분류](M04-08-regression-classification.md)
- 선수 단원: [M04-12 entropy와 cross entropy](M04-12-entropy-cross-entropy.md)
- 확인 질문: probability와 observed binary outcome을 구분할 수 있는가?
- 확인 질문: sample average가 population quantity의 estimate임을 설명할 수 있는가?

## 기호와 용어

| 표기·용어 | Common spoken reading | 의미 | 조건·범위 |
|---|---|---|---|
| $\widehat P$ | `P hat` | model이 출력한 positive-class probability | $0\le\widehat P\le1$ |
| $\widehat y_i$ | `y hat sub i` | sample $i$의 predicted class | multiclass 가능 |
| $\widehat c_i$ | `c hat sub i` | predicted class의 confidence | $\max_k q_i(k)$ |
| $B_m$ | `B sub m` | confidence가 일정 구간에 든 sample index 집합 | binning에 의존 |
| reliability diagram | `reliability diagram` | bin별 confidence와 accuracy 비교 | finite-sample estimate |
| ECE | `E C E` | bin별 calibration gap의 weighted average | binning에 의존 |
| scoring rule | `scoring rule` | probability prediction과 outcome에 loss를 부여하는 규칙 | 여기서는 작을수록 좋음 |
| Brier score | `Brier score` | squared error 기반 probability score | binary·multiclass |
| sharpness | `sharpness` | prediction distribution이 얼마나 집중되는지 나타내는 성질 | calibration과 별도 |

## 핵심 개념 1. calibration은 probability와 frequency의 일치를 묻는다

binary outcome $Y\in\{0,1\}$과 predicted probability $\widehat P$를 생각하자. perfect calibration의 정식 표현은

\[
\mathbb E[Y\mid \widehat P]=\widehat P
\quad\text{almost surely}
\]

이다. 직관적으로는 $\widehat P=p$라고 예측한 경우의 실제 positive frequency가 $p$라는 뜻이다.

\[
\mathbb P(Y=1\mid \widehat P=p)=p.
\]

$\widehat P$가 continuous이면 exact value $p$가 관측될 probability가 0일 수 있다. 그래서 finite dataset에서는 가까운 confidence를 bin으로 묶어 calibration을 estimate한다.

## 핵심 개념 2. accuracy와 calibration은 서로 다른 질문이다

accuracy는 predicted label이 얼마나 자주 맞는지 묻는다. calibration은 predicted probability가 같은 사례들의 observed frequency와 맞는지 묻는다.

두 model의 predicted label이 같으면 accuracy도 같을 수 있다. 그러나 하나가 모든 정답에 $0.7$을, 다른 하나가 $0.99$를 부여한다면 confidence의 의미는 다르다. 두 번째 model이 $99\%$만큼 자주 맞지 않으면 overconfident하다.

반대로 population positive rate가 $0.7$일 때 모든 sample에 $0.7$을 출력하는 model은 집단 전체에서 calibrated할 수 있다. 하지만 sample마다 위험을 구별하지 못한다. calibration은 discrimination이나 usefulness를 대신하지 않는다.

## 핵심 개념 3. reliability diagram은 bin별 gap을 보여 준다

multiclass prediction $q_i(k)$에서 predicted label과 confidence를

\[
\widehat y_i=\arg\max_k q_i(k),
\qquad
\widehat c_i=\max_k q_i(k)
\]

로 둔다. confidence 구간에 따라 index set $B_1,\ldots,B_M$을 만들고 각 bin에서

\[
\operatorname{conf}(B_m)
=\frac{1}{|B_m|}
\sum_{i\in B_m}\widehat c_i
\]

와

\[
\operatorname{acc}(B_m)
=\frac{1}{|B_m|}
\sum_{i\in B_m}
\mathbf 1\{y_i=\widehat y_i\}
\]

를 계산한다. reliability diagram은 bin별 $\operatorname{conf}(B_m)$과 $\operatorname{acc}(B_m)$을 비교한다.

$\operatorname{conf}(B_m)>\operatorname{acc}(B_m)$이면 그 bin에서 overconfidence를, 반대이면 underconfidence를 시사한다. bin에 sample이 적으면 두 값의 sampling uncertainty가 커진다.

## 핵심 개념 4. ECE는 bin별 calibration gap을 한 수로 요약한다

sample 수가 $n$일 때 널리 쓰이는 ECE는

\[
\operatorname{ECE}
=\sum_{m=1}^{M}
\frac{|B_m|}{n}
\left|
\operatorname{acc}(B_m)
-\operatorname{conf}(B_m)
\right|
\]

이다. bin이 큰 만큼 gap에 큰 weight를 준다.

ECE는 bin boundary와 bin 수에 따라 달라진다. 한 bin 안의 overconfidence와 underconfidence가 평균에서 상쇄될 수도 있다. top-label ECE가 작아도 classwise calibration이나 subgroup calibration이 나쁠 수 있다. ECE 하나는 full prediction distribution의 calibration 증명이 아니다.

## 핵심 개념 5. multiclass calibration에는 여러 강도가 있다

multiclass probability vector를 $\boldsymbol q=(q_1,\ldots,q_K)^\top$라 하자. full calibration은 가능한 prediction vector $\boldsymbol q$에 대해

\[
\mathbb P(Y=k\mid \boldsymbol Q=\boldsymbol q)=q_k
\]

가 모든 class $k$에서 성립하는 조건이다. prediction vector가 high-dimensional continuous value이므로 finite sample에서 직접 확인하기 어렵다.

classwise calibration은 각 class probability를 따로 검사한다. top-label calibration은 predicted class의 confidence와 correctness만 비교한다. 둘은 full calibration보다 약한 조건이다. 어떤 calibration metric을 썼는지 밝히지 않고 “calibrated”라고만 쓰면 주장 범위가 모호해진다.

## 핵심 개념 6. proper scoring rule은 정직한 probability를 유도한다

scoring rule $S(q,y)$을 작은 값이 좋은 loss로 쓰자. true distribution이 $p$일 때 $S$가 proper하다는 것은 모든 candidate distribution $q$에 대해

\[
\mathbb E_{Y\sim p}[S(p,Y)]
\le
\mathbb E_{Y\sim p}[S(q,Y)]
\]

임을 뜻한다. equality가 $q=p$에서만 성립하면 strictly proper이다. expected score를 낮추려는 forecaster가 자신의 true belief를 그대로 보고할 이유를 주는 성질이다.

log score는

\[
S_{\log}(q,y)=-\log q(y)
\]

이다. expected log score는 cross entropy이고, true distribution과 candidate distribution 사이 KL divergence만큼 증가한다. 따라서 support condition 아래 strictly proper이다.

## 핵심 개념 7. Brier score는 probability error를 제곱한다

binary outcome $y\in\{0,1\}$과 positive probability $q$의 Brier score는

\[
S_{\mathrm{Brier}}(q,y)=(q-y)^2
\]

이다. multiclass에서는 one-hot target을 사용해

\[
S_{\mathrm{Brier}}(\boldsymbol q,y)
=\sum_{k=1}^{K}
\left(q_k-\mathbf 1\{k=y\}\right)^2
\]

로 쓴다.

log score는 realized class에 아주 작은 probability를 준 prediction을 강하게 벌한다. Brier score는 bounded squared error를 사용한다. 두 score 모두 strictly proper이지만 individual sample에 부여하는 penalty의 모양은 다르다.

## 핵심 개념 8. calibration과 sharpness를 함께 봐야 한다

sharpness는 prediction이 base rate 주변에만 머무르지 않고 sample에 따라 $0$이나 $1$에 가까운 informative probability를 내는 정도를 가리킨다. sharpness는 outcome을 조건으로 정의하는 calibration과 달리 prediction distribution 자체의 집중도를 본다.

모든 sample에 base rate를 출력하는 model은 aggregate calibration을 만족할 수 있지만 sharp하지 않다. 반대로 극단적인 probability를 내는 model은 sharp해 보여도 calibration이 나쁠 수 있다. 좋은 probability forecast는 calibration을 유지하면서 useful discrimination과 sharpness를 가져야 한다.

## 핵심 개념 9. temperature scaling은 logit의 크기를 조정한다

logit vector $\boldsymbol z$에 temperature $T>0$를 적용하면

\[
q_T(k\mid x)
=\frac{\exp(z_k/T)}
{\sum_j\exp(z_j/T)}
\]

이다. $T>1$이면 distribution이 부드러워지고 confidence가 낮아진다. $0<T<1$이면 distribution이 더 뾰족해진다.

positive temperature는 logit order를 바꾸지 않으므로 predicted class와 accuracy는 유지한다. 보통 held-out validation set의 negative log-likelihood를 낮추도록 $T$를 fit한다. 이 절차가 새로운 population에서도 calibration을 보장하지는 않는다.

## 핵심 개념 10. calibration은 평가 population에 종속된다

calibration은 input·label·prediction의 joint distribution에 관한 성질이다. class prevalence, input distribution이나 labeling process가 바뀌면 같은 model의 calibration도 달라질 수 있다.

전체 dataset에서 ECE가 작아도 특정 subgroup에서는 gap이 클 수 있다. deployment report에는 calibration set과 test set의 분리, binning rule, subgroup result, proper score와 distribution shift 조건을 함께 기록해야 한다.

## 예제 1. 두 bin의 ECE

두 bin이 각각 전체 sample의 절반을 포함한다고 하자.

| bin | confidence | accuracy |
|---|---:|---:|
| $B_1$ | $0.70$ | $0.60$ |
| $B_2$ | $0.90$ | $1.00$ |

ECE는

\[
\operatorname{ECE}
=\frac12|0.60-0.70|
+\frac12|1.00-0.90|
=0.10
\]

이다. 첫 bin은 overconfident하고 둘째 bin은 underconfident하지만 absolute gap을 쓰므로 서로 상쇄되지 않는다.

## 예제 2. binary Brier score

positive probability가 $q=0.8$일 때 outcome이 $y=1$이면

\[
(0.8-1)^2=0.04
\]

이다. outcome이 $y=0$이면

\[
(0.8-0)^2=0.64
\]

이다. 높은 positive probability를 보고한 prediction은 positive outcome에서 낮은 loss를, negative outcome에서 높은 loss를 받는다.

## 예제 3. log score

$q=0.8$을 positive probability로 보고했다. $y=1$이면 log score는

\[
-\log0.8\approx0.223
\]

이고 $y=0$이면

\[
-\log(1-0.8)
=-\log0.2
\approx1.609
\]

이다. realized outcome에 작은 probability를 준 두 번째 경우가 더 큰 penalty를 받는다.

## 예제 4. calibrated하지만 구별하지 못하는 model

population의 positive rate가 $0.7$이고 모든 sample에 $\widehat P=0.7$을 출력한다고 하자. 충분히 큰 sample에서 $\widehat P=0.7$인 집단의 positive frequency도 $0.7$이므로 aggregate calibration은 맞는다.

그러나 모든 sample의 score가 같아 positive와 negative를 rank하지 못한다. calibration만으로 discrimination을 평가할 수 없는 예이다.

## 흔한 오해

### 오해 1. accuracy가 높으면 probability도 calibrated하다

같은 predicted label과 accuracy를 가진 model도 confidence는 다를 수 있다. calibration은 confidence별 frequency를 따로 검사한다.

### 오해 2. ECE가 낮으면 모든 class와 subgroup에서 calibrated하다

top-label ECE는 bin average에 기반한 한 가지 summary이다. classwise·subgroup·full-vector calibration을 보장하지 않는다.

### 오해 3. calibrated model은 informative하다

base-rate-only predictor도 aggregate calibration을 만족할 수 있다. discrimination과 sharpness를 별도로 봐야 한다.

### 오해 4. temperature scaling은 model의 accuracy를 높이는 방법이다

positive scalar temperature는 logit order를 유지한다. predicted class와 accuracy는 그대로이고 probability concentration만 바뀐다.

### 오해 5. 한 test set의 calibration은 deployment에서도 유지된다

calibration은 평가 population에 종속된다. prevalence나 input distribution이 바뀌면 다시 평가해야 한다.

## 연습문제

### 1. perfect calibration 해석

어떤 binary model이 $\widehat P=0.6$인 사례를 많이 만들었다. perfect calibration이라면 이 사례들에서 기대하는 positive 비율은 얼마인가?

<details>
<summary>해설 보기</summary>

calibration 정의에 따라

\[
\mathbb P(Y=1\mid \widehat P=0.6)=0.6
\]

이어야 한다. finite sample의 observed proportion은 sampling variation 때문에 정확히 $0.6$이 아닐 수 있다.

</details>

### 2. bin accuracy와 confidence

한 bin에 confidence가 $0.7,0.8,0.9,0.8$인 네 prediction이 있다. 정답 여부는 $1,1,0,1$이다. bin confidence와 accuracy를 구하라.

<details>
<summary>해설 보기</summary>

bin confidence는

\[
\frac{0.7+0.8+0.9+0.8}{4}=0.8
\]

이고 accuracy는

\[
\frac{1+1+0+1}{4}=0.75
\]

이다. 이 bin은 confidence가 accuracy보다 $0.05$ 높다.

</details>

### 3. ECE 계산

$B_1,B_2$가 각각 sample의 $40\%,60\%$를 포함한다. 두 bin의 $(\operatorname{acc},\operatorname{conf})$가 각각 $(0.7,0.8)$과 $(0.9,0.85)$이다. ECE를 구하라.

<details>
<summary>해설 보기</summary>

\[
\begin{aligned}
\operatorname{ECE}
&=0.4|0.7-0.8|
+0.6|0.9-0.85|\\
&=0.04+0.03\\
&=0.07.
\end{aligned}
\]

</details>

### 4. Brier score 비교

$y=1$인 sample에 model A는 $q_A=0.9$, model B는 $q_B=0.6$을 출력했다. 각 Brier score를 구하고 비교하라.

<details>
<summary>해설 보기</summary>

\[
S_A=(0.9-1)^2=0.01,
\qquad
S_B=(0.6-1)^2=0.16.
\]

이 sample에서는 realized positive outcome에 더 큰 probability를 준 model A의 score가 낮다.

</details>

### 5. log score 비교

$y=0$인 binary sample에 positive probability $q=0.1$과 $q=0.8$을 각각 보고했다. 두 log score를 구하라.

<details>
<summary>해설 보기</summary>

$y=0$의 predicted probability는 $1-q$이다. 따라서

\[
-\log(1-0.1)=-\log0.9\approx0.105
\]

이고

\[
-\log(1-0.8)=-\log0.2\approx1.609
\]

이다. realized class에 더 작은 probability를 준 두 번째 prediction의 loss가 크다.

</details>

### 6. temperature scaling

overconfident한 model에 $T>1$을 적용했다. probability distribution, predicted class와 accuracy가 어떻게 변하는지 설명하라.

<details>
<summary>해설 보기</summary>

logit을 $T>1$로 나누면 class probability가 더 부드러워지고 top confidence가 낮아진다. positive scalar로 나누어도 logit order는 같으므로 predicted class는 변하지 않는다. 같은 dataset에서 accuracy도 변하지 않는다.

</details>

### 7. calibration 주장 비판

한 연구가 test set의 10-bin top-label ECE가 낮다는 이유로 “모든 사용자 집단에서 probability가 신뢰 가능하다”고 결론 내렸다. 필요한 추가 검사를 설명하라.

<details>
<summary>해설 보기</summary>

ECE는 bin boundary와 sample size에 의존하며 top-label calibration만 요약한다. classwise reliability, subgroup별 calibration과 confidence interval을 확인해야 한다. log score나 Brier score 같은 proper score도 함께 보고 calibration에 사용하지 않은 held-out set에서 평가해야 한다. deployment distribution이 다르면 prevalence와 input shift 아래 calibration을 다시 측정해야 한다.

</details>

## 단원 요약

- binary calibration은 $\mathbb E[Y\mid\widehat P]=\widehat P$로 표현한다.
- accuracy는 label correctness를, calibration은 probability와 frequency의 일치를 묻는다.
- reliability diagram은 confidence bin별 accuracy와 confidence를 비교한다.
- ECE는 binning에 의존하며 full·classwise·subgroup calibration을 보장하지 않는다.
- proper scoring rule은 true distribution을 보고할 때 expected loss가 최소가 되게 한다.
- log score와 Brier score는 서로 다른 penalty 모양을 가진 strictly proper scoring rule이다.
- calibration과 sharpness·discrimination을 함께 평가해야 한다.
- temperature scaling은 predicted class를 유지한 채 probability concentration을 조정한다.
- calibration 결과는 평가 population에 종속된다.

## 통과 기준

다음 질문에 자료를 보지 않고 답할 수 있으면 통과한다.

- binary calibration을 conditional expectation으로 쓸 수 있는가?
- accuracy와 calibration의 차이를 예로 설명할 수 있는가?
- bin confidence·accuracy와 ECE를 계산할 수 있는가?
- top-label ECE의 한계를 설명할 수 있는가?
- proper scoring rule의 조건을 쓸 수 있는가?
- log score와 Brier score를 계산하고 비교할 수 있는가?
- temperature scaling이 바꾸는 것과 유지하는 것을 구분할 수 있는가?
- distribution shift 아래 calibration을 다시 평가해야 하는 이유를 설명할 수 있는가?

## 다음 단원

- [M04-16 상관관계와 인과관계](M04-16-correlation-causation.md)

## 집필자 점검표

- [x] 학습 목표가 관찰 가능한 행동으로 작성됐다.
- [x] binary·multiclass calibration을 구분했다.
- [x] reliability diagram과 ECE를 계산했다.
- [x] ECE의 binning·subgroup 한계를 밝혔다.
- [x] proper scoring rule을 정의했다.
- [x] log score와 Brier score를 비교했다.
- [x] calibration과 sharpness를 구분했다.
- [x] temperature scaling과 distribution shift를 설명했다.
- [x] 모든 문제에 해설이 있다.
- [x] 모델 해석 주장의 강도를 구분했다.
- [x] 용어집과 표기 규칙을 따랐다.
- [x] 선수지식 밖의 내용을 몰래 요구하지 않는다.
- [x] 내부 링크와 수식 구분자를 확인했다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
