---
id: "N05-00"
title: "단원 제목"
part: 2
stage: "N05"
status: "계획"
prerequisites: []
estimated_time: "90~120분"
---

# N05-00. 단원 제목

기존 [단원 템플릿](lesson-template.md)의 구조를 유지한다. 아래 항목은 실행 코드가 있는 N05 단원에서 해당 위치에 추가한다.

## 실행 실습

### 실행 환경

- 환경: Python 3.12, PyTorch CPU, NumPy
- 확인일: YYYY-MM-DD
- 구성요소 등급: `Stable core`
- 예제 ID: `n05_00_example`
- 코드 원본: `labs/N05/n05_00_example.py`
- 테스트: `tests/N05/test_n05_00.py`
- 실행 명령: `.venv\Scripts\python.exe labs/N05/n05_00_example.py`

### 자원 예산

실제 사용하는 batch, dimension, parameter, step과 timeout을 적는다. 사용하지 않는 항목을 억지로 나열하지 않는다.

### 실제 코드와 실행 결과

다음 표식은 한 단원에 한 번 사용한다. Markdown에 `.py` 코드를 복제하지 않는다.

```text
<!-- N05_EXAMPLE: n05_00_example -->
```

site staging은 이 위치에 원본 코드, 실행 명령, 실제 stdout, shape·gradient와 실행시간을 넣는다.

### 결과 해석

- 출력값을 손계산의 어느 항과 대조했는지 적는다.
- shape 검사와 gradient 검사를 분리한다.
- 실행 성공과 수학적 정답 확인을 구분한다.
- 구현 최적화를 수학적 함수와 같은 것으로 설명하지 않는다.

집필자 점검표에는 기존 항목과 함께 다음을 확인한다.

- [ ] Markdown에 실행 코드를 손으로 복제하지 않았다.
- [ ] 실행 결과가 생성물에서 자동으로 들어간다.
- [ ] 코드 원본·테스트 경로·자원 예산·확인일을 기록했다.
- [ ] shape·수치·gradient를 테스트했다.
