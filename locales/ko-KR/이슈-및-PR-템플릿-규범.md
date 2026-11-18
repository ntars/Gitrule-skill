# 이슈 및 PR 템플릿 규범

> 이 파일이 해결하는 문제：`.github/ISSUE_TEMPLATE/*.yml` 구조화 양식과 `.github/PULL_REQUEST_TEMPLATE.md` 자체 점검 체크리스트의 필드 설계, 형식, 작성 요구사항을 정의하여, 문제 피드백과 변경 제출이 실행 가능한 입력 제약을 갖추도록 합니다.

## 1. 설계 원칙

1. **자유 텍스트보다 구조화 우선**：이슈 양식은 YAML로 정의하고, 드롭다운, 체크박스, 필수 항목을 통해 작성을 유도하여 무효 피드백을 줄입니다.
2. **필수 항목 최소화**：문제를 특정하는 데 필요한 필드만 유지하며, 선택 항목을 필수로 표시해서는 안 됩니다.
3. **자체 점검 명시화**：PR 템플릿은 체크리스트 형식으로 선택 가능한 자체 점검 항목을 나열하여, 기여자가 핵심 단계를 건너뛰지 않도록 합니다.
4. **책임 단일화**：이슈 양식은 정보 수집을 담당하며 프로젝트 소개를 담지 않습니다. PR 템플릿은 자체 점검을 담당하며 기능 설명을 반복하지 않습니다([문서 매트릭스](./문서-매트릭스.md) 대응).

## 2. 이슈 양식 구조

### 2.1 파일과 명명

- 경로는 `.github/ISSUE_TEMPLATE/*.yml`로 고정하며, 템플릿마다 파일 하나입니다.
- 파일 이름은 소문자와 하이픈을 사용합니다. 예: `bug-report.yml`, `feature-request.yml`, `question.yml`.
- 최소한 「결함 보고」와 「기능 요청」 두 가지 템플릿을 제공합니다.

### 2.2 표준 필드

| 필드 | 유형 | 필수 | 용도 |
| --- | --- | --- | --- |
| `name` | 문자열 | 예 | 템플릿 표시 이름 |
| `description` | 문자열 | 예 | 템플릿 용도 설명 |
| `title` | 문자열 접두사 | 예 | 자동 생성되는 문제 제목 접두사 |
| `labels` | 배열 | 아니오 | 자동 첨부되는 레이블 |
| `body` | 배열 | 예 | 양식 필드 목록 |

`body`에서 자주 쓰는 필드 유형：

| 유형 | 적용 시나리오 | 예시 |
| --- | --- | --- |
| `markdown` | 설명 텍스트, 입력 없음 | 작성 안내 |
| `textarea` | 긴 텍스트 설명 | 문제 재현 절차 |
| `input` | 한 줄 짧은 텍스트 | 버전 번호 |
| `dropdown` | 제한된 옵션 | 운영체제, 심각도 |
| `checkboxes` | 다중 확인 | 중복 문제 검색 여부 |

### 2.3 결함 보고 필드 목록

1. 문제 설명(`textarea`, 필수)：무슨 일이 발생했는지.
2. 예상 동작(`textarea`, 필수)：무엇이 발생해야 하는지.
3. 재현 절차(`textarea`, 필수)：번호로 나열하고, 독립적으로 재현 가능해야 함.
4. 실행 환경(`input` 또는 `dropdown`)：운영체제, 런타임, 프로젝트 버전.
5. 로그 또는 스크린샷(`textarea`)：오류 정보 제공, 민감 정보는 마스킹 필수.
6. 중복 검사 확인(`checkboxes`, 필수)：기존 이슈를 검색했음.

### 2.4 기능 요청 필드 목록

1. 문제 진술(`textarea`, 필수)：현재 어떤 능력이 부족한지.
2. 사용 시나리오(`textarea`, 필수)：누가 어떤 상황에서 필요한지.
3. 희망 방안(`textarea`)：어떻게 구현되기를 바라는지.
4. 대안(`textarea`)：이미 고려한 다른 방식.
5. 호환성 영향(`dropdown`)：파괴적 변경이 관련되는지.

## 3. PR 템플릿 구조

### 3.1 필수 블록

`PULL_REQUEST_TEMPLATE.md`는 다음 블록을 포함해야 하며, 순서는 고정입니다：

1. 변경 설명：이번 변경이 무엇을 했는지, 대응하는 이슈 번호.
2. 변경 유형：체크박스로 선택(기능, 수정, 문서, 리팩터링, 테스트 등, 유형은 [커밋 메시지 규범](./커밋-메시지-규범.md) 참조).
3. 자체 테스트 체크리스트：선택 가능한 자체 점검 항목.
4. 파괴적 변경：없으면 「없음」으로 쓰고, 있으면 마이그레이션 방식을 씁니다([마이그레이션 가이드 규범](./마이그레이션-가이드-규범.md) 참조).
5. 관련 문서：README, CHANGELOG, API 문서를 동기 업데이트했는지.

### 3.2 자체 테스트 체크리스트 예시

```markdown
## 자체 테스트 체크리스트

- [ ] 로컬 빌드 통과
- [ ] 관련 테스트 통과, 신규 기능에 테스트 추가 완료
- [ ] [커밋 메시지 규범](./커밋-메시지-규범.md)에 따라 커밋 메시지 작성 완료
- [ ] 문서 동기 업데이트 완료 또는 업데이트 불필요 확인
- [ ] 키, 개인정보 데이터 또는 대용량 파일을 포함하지 않음
```

## 4. 복사 가능한 템플릿

### 4.1 결함 보고 양식

`.github/ISSUE_TEMPLATE/bug-report.yml`로 저장합니다：

```yaml
name: 缺陷报告
description: 报告可复现的功能异常
title: "[Bug]: "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        提交前请先搜索现有 issue，避免重复。
        请勿粘贴密钥、令牌或个人隐私信息。
  - type: checkboxes
    id: duplicate-check
    attributes:
      label: 重复检查
      options:
        - label: 我已搜索现有 issue，确认这不是重复报告
          required: true
  - type: textarea
    id: description
    attributes:
      label: 问题描述
      description: 实际发生了什么
      placeholder: 执行 install 命令后程序退出码为 1
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: 预期行为
      description: 应当发生什么
    validations:
      required: true
  - type: textarea
    id: steps
    attributes:
      label: 复现步骤
      description: 编号列出，确保他人可独立复现
      placeholder: |
        1. 执行命令
        2. 观察输出
        3. 出现异常
    validations:
      required: true
  - type: input
    id: version
    attributes:
      label: 项目版本
      placeholder: v1.0.0
    validations:
      required: true
  - type: dropdown
    id: os
    attributes:
      label: 操作系统
      options:
        - macOS
        - Linux
        - Windows
        - 其他
    validations:
      required: true
  - type: textarea
    id: logs
    attributes:
      label: 日志或截图
      description: 提供错误信息，敏感信息须脱敏
      render: shell
  - type: checkboxes
    id: security
    attributes:
      label: 信息安全确认
      options:
        - label: 已确认未包含密钥、令牌或个人隐私
          required: true
```

### 4.2 기능 요청 양식

`.github/ISSUE_TEMPLATE/feature-request.yml`로 저장합니다：

```yaml
name: 功能请求
description: 提出新能力或改进建议
title: "[Feature]: "
labels: ["enhancement"]
body:
  - type: textarea
    id: problem
    attributes:
      label: 问题陈述
      description: 当前缺少什么能力
    validations:
      required: true
  - type: textarea
    id: scenario
    attributes:
      label: 使用场景
      description: 谁在什么情况下需要该能力
    validations:
      required: true
  - type: textarea
    id: proposal
    attributes:
      label: 期望方案
      description: 希望如何实现
  - type: textarea
    id: alternatives
    attributes:
      label: 替代方案
      description: 已考虑过的其他方式
  - type: dropdown
    id: breaking
    attributes:
      label: 是否涉及破坏性变更
      options:
        - 否
        - 是
        - 不确定
    validations:
      required: true
```

### 4.3 PR 템플릿

`.github/PULL_REQUEST_TEMPLATE.md`로 저장합니다：

````markdown
## 변경 설명

{{变更说明}}

## 변경 유형

- [ ] 기능(feat)
- [ ] 수정(fix)
- [ ] 문서(docs)
- [ ] 형식(style)
- [ ] 리팩터링(refactor)
- [ ] 테스트(test)
- [ ] 빌드 또는 도구 체인(build / ci)

## 자체 테스트 체크리스트

- [ ] 로컬 빌드 통과
- [ ] 관련 테스트 통과, 신규 기능에 테스트 추가 완료
- [ ] 커밋 메시지 규범에 따라 커밋 메시지 작성 완료
- [ ] 문서 동기 업데이트 완료 또는 업데이트 불필요 확인
- [ ] 키, 개인정보 데이터 또는 대용량 파일을 포함하지 않음

## 파괴적 변경

{{破坏性变更说明}}

## 관련 문서

- [ ] README 동기 완료 또는 업데이트 불필요
- [ ] CHANGELOG 등록 완료
- [ ] API 문서 동기 완료 또는 업데이트 불필요
````

### 4.4 자리표시자 대조표

| 자리표시자 | 필수 | 작성 요점 |
| --- | --- | --- |
| `{{变更说明}}` | 예 | 변경 내용을 한 문장으로 진술하고 `#숫자` 형식의 이슈 번호를 첨부 |
| `{{破坏性变更说明}}` | 예 | 파괴적 변경이 없으면 「없음」으로 쓰고, 있으면 마이그레이션 단계를 쓰고 마이그레이션 가이드를 링크 |

YAML 양식의 `name`, `description`, `title`, `labels`는 템플릿 메타데이터이며 프로젝트 실제 상황에 따라 교체합니다. `body`의 필드 유형과 `required` 값은 제2, 3절 필드 목록에 따라 조정하며, 필수 항목을 삭제해서는 안 됩니다.

### 4.5 전체 작성 예시

결함 보고 작성 예시：

````markdown
## 문제 설명

`npm run build`를 실행한 후 프로세스가 종료되었고, 종료 코드는 1입니다.

## 예상 동작

빌드가 성공하고 `dist/` 디렉터리를 출력해야 합니다.

## 재현 절차

1. v1.0.0 태그를 체크아웃
2. `npm ci` 실행
3. `npm run build` 실행, 종료 코드 1 확인

## 프로젝트 버전

v1.0.0

## 운영체제

macOS

## 로그 또는 스크린샷

```
Error: Cannot find module 'mdlint-core'
```

## 정보 보안 확인

- [x] 키, 토큰 또는 개인정보를 포함하지 않았음을 확인
````

## 5. 작성 요구사항

1. 필드 설명은 명령문 또는 평서문을 사용하며, 구어체를 사용해서는 안 됩니다.
2. 각 필수 필드에 작성 예시 또는 형식 요구사항을 제시합니다.
3. 안내 문구는 「왜 이 정보가 필요한지」를 설명해야 하며, 공허한 요구를 피합니다.
4. 개인정보와 관련된 필드는 마스킹을 안내해야 합니다([보안 및 개인정보 규범](./보안-및-개인정보-규범.md) 참조).
5. 템플릿은 프로젝트 발전에 따라 업데이트하며, 폐기된 필드는 삭제해야 하고 장기간 쌓아두어서는 안 됩니다.

## 6. 금지 사항

1. 모든 문제 유형을 하나의 자유 텍스트 템플릿으로 통합하는 것을 금지합니다.
2. 문제 특정과 무관한 필수 필드를 설정하는 것을 금지합니다.
3. 템플릿에 프로젝트 소개나 마케팅 내용을 넣는 것을 금지합니다.
4. PR 템플릿에서 자체 테스트 체크리스트와 파괴적 변경 선언을 누락하는 것을 금지합니다.

## 관련 파일

- 파일 책임 경계는 [문서 매트릭스](./문서-매트릭스.md)를 참조하십시오
- 기여 프로세스는 [기여 가이드 규범](./기여-가이드-규범.md)을 참조하십시오
- 리뷰 기준은 [코드 리뷰 규범](./코드-리뷰-규범.md)을 참조하십시오
- 파괴적 변경 마이그레이션은 [마이그레이션 가이드 규범](./마이그레이션-가이드-규범.md)을 참조하십시오
- 커뮤니티 거버넌스 검사는 차원 D14에 속하며, [감사 차원 매트릭스](./감사-차원-매트릭스.md)를 참조하십시오
