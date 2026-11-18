# Issue与PR模板规范

> 本文件解决什么问题：定义 `.github/ISSUE_TEMPLATE/*.yml` 结构化表单与 `.github/PULL_REQUEST_TEMPLATE.md` 自查清单的字段设计、格式与写作要求，使问题反馈与变更提交具备可执行的输入约束。

## 1. 设计原则

1. **结构化优先于自由文本**：Issue 表单使用 YAML 定义，通过下拉框、复选框、必填项引导填写，减少无效反馈。
2. **必填最小化**：仅保留定位问题所必需的字段，可选字段不得标为必填。
3. **自查显式化**：PR 模板以清单形式列出可勾选的自查项，避免贡献者跳过关键步骤。
4. **职责单一**：Issue 表单负责收集信息，不承载项目介绍；PR 模板负责自查，不重复功能说明（对应 [文档矩阵](./文档矩阵.md)）。

## 2. Issue 表单结构

### 2.1 文件与命名

- 路径固定为 `.github/ISSUE_TEMPLATE/*.yml`，每个模板一个文件。
- 文件名使用小写与连字符，如 `bug-report.yml`、`feature-request.yml`、`question.yml`。
- 至少提供「缺陷报告」与「功能请求」两类模板。

### 2.2 标准字段

| 字段 | 类型 | 必填 | 用途 |
| --- | --- | --- | --- |
| `name` | 字符串 | 是 | 模板显示名称 |
| `description` | 字符串 | 是 | 模板用途说明 |
| `title` | 字符串前缀 | 是 | 自动生成的问题标题前缀 |
| `labels` | 数组 | 否 | 自动附加的标签 |
| `body` | 数组 | 是 | 表单字段列表 |

`body` 中常用字段类型：

| 类型 | 适用场景 | 示例 |
| --- | --- | --- |
| `markdown` | 说明文字，无输入 | 填写须知 |
| `textarea` | 长文本描述 | 问题复现步骤 |
| `input` | 单行短文本 | 版本号 |
| `dropdown` | 有限选项 | 操作系统、严重程度 |
| `checkboxes` | 多项确认 | 是否已搜索重复问题 |

### 2.3 缺陷报告字段清单

1. 问题描述（`textarea`，必填）：发生了什么。
2. 预期行为（`textarea`，必填）：应当发生什么。
3. 复现步骤（`textarea`，必填）：编号列出，可独立复现。
4. 运行环境（`input` 或 `dropdown`）：操作系统、运行时、项目版本。
5. 日志或截图（`textarea`）：提供错误信息，敏感信息须脱敏。
6. 重复检查确认（`checkboxes`，必填）：已搜索现有 issue。

### 2.4 功能请求字段清单

1. 问题陈述（`textarea`，必填）：当前缺少什么能力。
2. 使用场景（`textarea`，必填）：谁在什么情况下需要。
3. 期望方案（`textarea`）：希望如何实现。
4. 替代方案（`textarea`）：已考虑过的其他方式。
5. 兼容性影响（`dropdown`）：是否涉及破坏性变更。

## 3. PR 模板结构

### 3.1 必备区块

`PULL_REQUEST_TEMPLATE.md` 须包含以下区块，顺序固定：

1. 变更说明：本次改动做了什么，对应的 issue 编号。
2. 变更类型：用复选框勾选（功能、修复、文档、重构、测试等，类型见 [提交信息规范](./提交信息规范.md)）。
3. 自测清单：可勾选的自查项。
4. 破坏性变更：若无写「无」；若有须写迁移方式（见 [迁移指南规范](./迁移指南规范.md)）。
5. 相关文档：是否同步更新 README、CHANGELOG、API 文档。

### 3.2 自测清单示例

```markdown
## 自测清单

- [ ] 本地构建通过
- [ ] 相关测试通过，新增功能已补测试
- [ ] 已按 [提交信息规范](./提交信息规范.md) 撰写提交信息
- [ ] 文档已同步更新或确认无需更新
- [ ] 未引入密钥、隐私数据或大文件
```

## 4. 可复制模板

### 4.1 缺陷报告表单

保存为 `.github/ISSUE_TEMPLATE/bug-report.yml`：

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

### 4.2 功能请求表单

保存为 `.github/ISSUE_TEMPLATE/feature-request.yml`：

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

### 4.3 PR 模板

保存为 `.github/PULL_REQUEST_TEMPLATE.md`：

````markdown
## 变更说明

{{变更说明}}

## 变更类型

- [ ] 功能（feat）
- [ ] 修复（fix）
- [ ] 文档（docs）
- [ ] 格式（style）
- [ ] 重构（refactor）
- [ ] 测试（test）
- [ ] 构建或工具链（build / ci）

## 自测清单

- [ ] 本地构建通过
- [ ] 相关测试通过，新增功能已补测试
- [ ] 已按提交信息规范撰写提交信息
- [ ] 文档已同步更新或确认无需更新
- [ ] 未引入密钥、隐私数据或大文件

## 破坏性变更

{{破坏性变更说明}}

## 相关文档

- [ ] README 已同步或无需更新
- [ ] CHANGELOG 已登记
- [ ] API 文档已同步或无需更新
````

### 4.4 占位符对照表

| 占位符 | 必填 | 填写要点 |
| --- | --- | --- |
| `{{变更说明}}` | 是 | 一句陈述改动内容，并附 `#数字` 形式的 issue 编号 |
| `{{破坏性变更说明}}` | 是 | 无破坏性变更写「无」；有则写迁移步骤并链接迁移指南 |

YAML 表单的 `name`、`description`、`title`、`labels` 为模板元数据，按项目实际情况替换；`body` 中字段类型与 `required` 值按第 2、3 节字段清单调整，不得删减必填项。

### 4.5 完整填写示例

缺陷报告的填写示例：

````markdown
## 问题描述

执行 `npm run build` 后进程退出，退出码为 1。

## 预期行为

构建成功并输出 `dist/` 目录。

## 复现步骤

1. 检出 v1.0.0 标签
2. 执行 `npm ci`
3. 执行 `npm run build`，观察到退出码 1

## 项目版本

v1.0.0

## 操作系统

macOS

## 日志或截图

```
Error: Cannot find module 'mdlint-core'
```

## 信息安全确认

- [x] 已确认未包含密钥、令牌或个人隐私
````

## 5. 写作要求

1. 字段说明使用祈使句或陈述句，不得口语化。
2. 每个必填字段给出填写示例或格式要求。
3. 提示文字须说明「为什么需要此信息」，避免空泛要求。
4. 涉及隐私的字段须提示脱敏（见 [安全与隐私规范](./安全与隐私规范.md)）。
5. 模板随项目演进更新，废弃字段须删除，不得长期堆积。

## 6. 禁止事项

1. 禁止把所有问题类型合并为一个自由文本模板。
2. 禁止设置与定位问题无关的必填字段。
3. 禁止在模板中放入项目介绍或营销内容。
4. 禁止 PR 模板遗漏自测清单与破坏性变更声明。

## 相关文件

- 文件职责边界见 [文档矩阵](./文档矩阵.md)
- 贡献流程见 [贡献指南规范](./贡献指南规范.md)
- 审查标准见 [代码审查规范](./代码审查规范.md)
- 破坏性变更迁移见 [迁移指南规范](./迁移指南规范.md)
- 社区治理检查属维度 D14，见 [审核维度矩阵](./审核维度矩阵.md)
