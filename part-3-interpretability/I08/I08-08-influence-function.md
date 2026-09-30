---
id: "I08-08"
title: "influence function"
part: 3
stage: "I08"
status: "완료"
prerequisites: ["I08-07", "I08-06", "M04-11"]
estimated_time: "100~140분"
---

# I08-08. influence function

## 이 단원이 필요한 이유

특정 training example이 test prediction에 미친 영향을 정확히 알려면 그 example을 빼고 다시 학습하는 반사실을 비교해야 한다. influence function은 최적점 주변의 미소한 data weight 변화와 Hessian inverse를 사용해 이 retraining 효과를 근사한다. 계산이 빠른 대신 국소성·미분가능성·곡률 조건을 가진다.

## 학습 목표

- example upweighting에 대한 파라미터 변화를 유도할 수 있다.
- test loss influence 식의 부호와 항을 설명할 수 있다.
- HVP와 inverse-Hessian-vector product를 구분할 수 있다.
- 근사 결과를 leave-one-out retraining으로 검증하는 설계를 세울 수 있다.

## 선수지식 확인

- 선수 단원: [I08-07 loss landscape와 mode connectivity](I08-07-loss-landscape-mode-connectivity.md), [I08-06 Hessian spectrum](I08-06-hessian-spectrum.md), [M04-11 likelihood와 maximum likelihood](../../part-1-foundations/M04/M04-11-likelihood-maximum-likelihood.md)
- 확인 질문: $H^{-1}v$와 $Hv$는 같은 계산인가?

## 기호와 용어

| 기호·용어 | Common spoken reading | 의미 | shape·범위 |
|---|---|---|---|
| $z_i$ | `z sub i` | $i$번째 training example | sample |
| $\hat\theta_\varepsilon$ | `theta hat sub epsilon` | $z_i$를 $\varepsilon$만큼 upweight한 최적점 | $\mathbb R^p$ |
| $H_{\hat\theta}$ | `H sub theta hat` | empirical risk Hessian at optimum | $p\times p$ |
| $H^{-1}v$ | `H inverse v` | inverse-Hessian-vector product | $\mathbb R^p$ |
| leave-one-out | `leave one out` | 한 example을 제거한 retraining 비교 | counterfactual procedure |

## 1. Data weight를 미소하게 바꾼다

empirical risk에 $\varepsilon\ell(z_i,\theta)$를 더한 최적점을 $\hat\theta_\varepsilon$라 하자. regularity 조건 아래 implicit differentiation을 하면

$$
\left.\frac{d\hat\theta_\varepsilon}{d\varepsilon}\right|_{\varepsilon=0}
=-H_{\hat\theta}^{-1}\nabla_\theta\ell(z_i,\hat\theta).
$$

training example gradient가 curvature에 의해 parameter 방향으로 변환된다.

## 2. Test loss 영향

test example $z_{test}$의 loss 변화율은

$$
I_{\mathrm{up,loss}}(z_i,z_{test})
=-\nabla\ell(z_{test},\hat\theta)^\top
H_{\hat\theta}^{-1}\nabla\ell(z_i,\hat\theta).
$$

부호는 upweighting 정의와 score·loss 선택에 따라 달라진다. 구현에서 “양수가 helpful”인지 “harmful”인지 문장으로 고정한다.

## 3. 성립 조건과 검증

고전 유도는 smooth loss, invertible Hessian과 잘 정의된 국소 optimum을 사용한다. deep network에서는 Hessian이 singular·indefinite하고 training이 정확한 optimum이 아닐 수 있다. damping과 iterative solve는 계산을 가능하게 하지만 가정을 복구하는 마법이 아니다.

작은 모델에서는 실제 leave-one-out retraining 순위와 influence 순위를 비교한다. seed를 여러 개 쓰고 prediction target을 고정한다.

## 4. CPU 실습

<!-- I08_EXAMPLE: i08_08_influence_function -->

1차원 ridge regression에서 Hessian 기반 제거 근사와 실제 leave-one-out refit을 비교한다. 이 예제에서는 순위가 잘 맞지만 exact change와 수치는 같지 않다.

## 흔한 오해

### 오해 1. influence는 training example의 인과효과를 정확히 준다

근사는 특정 최적점 주변의 작은 weight 변화에 대한 것이다. finite removal과 전체 retraining 경로는 다를 수 있다.

### 오해 2. 큰 값은 example 내용 때문만이다

중복, gradient norm, curvature, target과 model state가 함께 값을 결정한다.

## 연습문제

### 1. shape

$\theta\in\mathbb R^p$일 때 $H^{-1}\nabla\ell_i$의 shape은 무엇인가?

<details><summary>해설 보기</summary>

$H^{-1}$는 $p\times p$, gradient는 길이 $p$이므로 결과는 $\mathbb R^p$이다.

</details>

### 2. 곡률

같은 gradient 방향에서 Hessian eigenvalue가 작으면 inverse-Hessian 변위는 어떻게 되는가?

<details><summary>해설 보기</summary>

역수가 커지므로 damping이 없다면 그 방향의 추정 변위가 커진다.

</details>

### 3. singular Hessian

Hessian이 singular하면 직접 inverse를 쓸 수 없는 이유는 무엇인가?

<details><summary>해설 보기</summary>

0 eigenvalue가 있어 inverse가 존재하지 않는다. damping이나 pseudo-inverse를 쓰면 estimand가 달라짐을 기록해야 한다.

</details>

### 4. 부호

loss influence의 부호를 보고 helpful 여부를 판단하기 전에 무엇을 확인해야 하는가?

<details><summary>해설 보기</summary>

upweighting·removal 정의, loss인지 score인지, 구현의 음수 부호 convention을 확인한다.

</details>

### 5. 검증

작은 데이터셋에서 가장 직접적인 ground-truth 근사 검사는 무엇인가?

<details><summary>해설 보기</summary>

각 example을 실제로 제거하고 같은 protocol로 재학습해 test target 변화를 비교한다.

</details>

### 6. 주장 비판

“influence 상위 문장에 model knowledge가 저장돼 있다”를 비판하라.

<details><summary>해설 보기</summary>

높은 국소 gradient 정렬이 지식의 유일한 저장 위치를 뜻하지 않는다. 중복 데이터와 학습 경로, 근사 오차를 함께 조사해야 한다.

</details>

## 근거와 갱신 경계

deep model prediction을 training data로 추적하는 influence 근사는 [Koh and Liang (2017)](https://proceedings.mlr.press/v70/koh17a.html)을 기준으로 한다. 논문도 비볼록·비미분 조건에서 이론이 깨질 수 있음을 구분하므로, 이 단원은 근사값을 retraining truth로 부르지 않는다.

## 단원 요약

- influence function은 data weight의 미소 변화에 대한 국소 근사이다.
- training gradient, inverse Hessian과 test gradient가 함께 들어간다.
- deep network에서는 damping·수치해와 이론 조건을 따로 기록한다.
- 가능한 범위에서 leave-one-out retraining으로 검증한다.

## 통과 기준

- influence 식의 각 항과 shape을 설명할 수 있는가?
- HVP와 inverse-Hessian solve를 구분할 수 있는가?
- 근사 검증 실험을 설계할 수 있는가?

## 다음 단원

- [I08-09 feature emergence](I08-09-feature-emergence.md)

## 집필자 점검표

- [x] 국소 근사의 조건을 명시했다.
- [x] retraining counterfactual과 구분했다.
- [x] 모든 문제에 해설이 있다.
- [x] Common spoken reading이 실제 영어 학술 발화이며 한글 음역이나 기계적 직역을 포함하지 않는다.
- [x] 주장 강도와 읽기 표기를 확인했다.
- [x] 내부 링크와 수식을 확인했다.
