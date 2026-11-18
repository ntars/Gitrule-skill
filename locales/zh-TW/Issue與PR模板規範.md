# Issue與PR模板規範

> 本檔案解決什麼問題：定義 `.github/ISSUE_TEMPLATE/*.yml` 結構化表單與 `.github/PULL_REQUEST_TEMPLATE.md` 自查清單的欄位設計、格式與寫作要求，使問題反饋與變更提交具備可執行的輸入約束。

## 1. 設計原則

1. **結構化優先於自由文字**：Issue 表單使用 YAML 定義，透過下拉框、核取方塊、必填項引導填寫，減少無效反饋。
2. **必填最小化**：僅保留定位問題所必需的欄位，可選欄位不得標為必填。
3. **自查顯式化**：PR 模板以清單形式列出可勾選的自查項，避免貢獻者跳過關鍵步驟。
4. **職責單一**：Issue 表單負責收集資訊，不承載專案介紹；PR 模板負責自查，不重複功能說明（對應 [文件矩陣](./文件矩陣.md)）。

## 2. Issue 表單結構

### 2.1 檔案與命名

- 路徑固定為 `.github/ISSUE_TEMPLATE/*.yml`，每個模板一個檔案。
- 檔名使用小寫與連字元，如 `bug-report.yml`、`feature-request.yml`、`question.yml`。
- 至少提供「缺陷報告」與「功能請求」兩類别範本。

### 2.2 標準欄位

| 欄位 | 型別 | 必填 | 用途 |
| --- | --- | --- | --- |
| `name` | 字串 | 是 | 模板顯示名稱 |
| `description` | 字串 | 是 | 模板用途說明 |
| `title` | 字串字首 | 是 | 自動生成的問題標題字首 |
| `labels` | 陣列 | 否 | 自動附加的標籤 |
| `body` | 陣列 | 是 | 表單欄位列表 |

`body` 中常用欄位型別：

| 型別 | 適用場景 | 示例 |
| --- | --- | --- |
| `markdown` | 說明文字，無輸入 | 填寫須知 |
| `textarea` | 長文字描述 | 問題復現步驟 |
| `input` | 單行短文字 | 版本號 |
| `dropdown` | 有限選項 | 作業系統、嚴重程度 |
| `checkboxes` | 多項確認 | 是否已搜尋重複問題 |

### 2.3 缺陷報告欄位清單

1. 問題描述（`textarea`，必填）：發生了什麼。
2. 預期行為（`textarea`，必填）：應當發生什麼。
3. 復現步驟（`textarea`，必填）：編號列出，可獨立復現。
4. 執行環境（`input` 或 `dropdown`）：作業系統、執行時、專案版本。
5. 日誌或截圖（`textarea`）：提供錯誤資訊，敏感資訊須脫敏。
6. 重複檢查確認（`checkboxes`，必填）：已搜尋現有 issue。

### 2.4 功能請求欄位清單

1. 問題陳述（`textarea`，必填）：當前缺少什麼能力。
2. 使用場景（`textarea`，必填）：誰在什麼情況下需要。
3. 期望方案（`textarea`）：希望如何實現。
4. 替代方案（`textarea`）：已考慮過的其他方式。
5. 相容性影響（`dropdown`）：是否涉及破壞性變更。

## 3. PR 模板結構

### 3.1 必備區塊

`PULL_REQUEST_TEMPLATE.md` 須包含以下區塊，順序固定：

1. 變更說明：本次改動做了什麼，對應的 issue 編號。
2. 變更型別：用核取方塊勾選（功能、修復、文件、重構、測試等，型別見 [提交資訊規範](./提交資訊規範.md)）。
3. 自測清單：可勾選的自查項。
4. 破壞性變更：若無寫「無」；若有須寫遷移方式（見 [遷移指南規範](./遷移指南規範.md)）。
5. 相關文件：是否同步更新 README、CHANGELOG、API 文件。

### 3.2 自測清單示例

```markdown
## 自測清單

- [ ] 本地構建透過
- [ ] 相關測試透過，新增功能已補測試
- [ ] 已按 [提交資訊規範](./提交資訊規範.md) 撰寫提交資訊
- [ ] 文件已同步更新或確認無需更新
- [ ] 未引入金鑰、隱私資料或大檔案
```

## 4. 可複製模板

### 4.1 缺陷報告表單

儲存為 `.github/ISSUE_TEMPLATE/bug-report.yml`：

```yaml
name: 缺陷報告
description: 回報可重現的功能異常
title: "[Bug]: "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        提交前請先搜尋現有 issue，避免重複。
        請勿貼上金鑰、權杖或個人隱私資訊。
  - type: checkboxes
    id: duplicate-check
    attributes:
      label: 重複檢查
      options:
        - label: 我已搜尋現有 issue，確認這不是重複回報
          required: true
  - type: textarea
    id: description
    attributes:
      label: 問題描述
      description: 實際發生了什麼
      placeholder: 執行 install 命令後程式結束碼為 1
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: 預期行為
      description: 應當發生什麼
    validations:
      required: true
  - type: textarea
    id: steps
    attributes:
      label: 重現步驟
      description: 以編號列出，確保他人可獨立重現
      placeholder: |
        1. 執行命令
        2. 觀察輸出
        3. 出現異常
    validations:
      required: true
  - type: input
    id: version
    attributes:
      label: 專案版本
      placeholder: v1.0.0
    validations:
      required: true
  - type: dropdown
    id: os
    attributes:
      label: 作業系統
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
      label: 日誌或截圖
      description: 提供錯誤訊息，敏感資訊須去識別化
      render: shell
  - type: checkboxes
    id: security
    attributes:
      label: 資訊安全確認
      options:
        - label: 已確認未包含金鑰、權杖或個人隱私
          required: true
```

### 4.2 功能請求表單

儲存為 `.github/ISSUE_TEMPLATE/feature-request.yml`：

```yaml
name: 功能請求
description: 提出新能力或改進建議
title: "[Feature]: "
labels: ["enhancement"]
body:
  - type: textarea
    id: problem
    attributes:
      label: 問題陳述
      description: 目前缺少什麼能力
    validations:
      required: true
  - type: textarea
    id: scenario
    attributes:
      label: 使用情境
      description: 誰在什麼情況下需要該能力
    validations:
      required: true
  - type: textarea
    id: proposal
    attributes:
      label: 期望方案
      description: 希望如何實作
  - type: textarea
    id: alternatives
    attributes:
      label: 替代方案
      description: 已考慮過的其他方式
  - type: dropdown
    id: breaking
    attributes:
      label: 是否涉及破壞性變更
      options:
        - 否
        - 是
        - 不確定
    validations:
      required: true
```

### 4.3 PR 模板

儲存為 `.github/PULL_REQUEST_TEMPLATE.md`：

````markdown
## 變更說明

{{变更说明}}

## 變更型別

- [ ] 功能（feat）
- [ ] 修復（fix）
- [ ] 文件（docs）
- [ ] 格式（style）
- [ ] 重構（refactor）
- [ ] 測試（test）
- [ ] 構建或工具鏈（build / ci）

## 自測清單

- [ ] 本地構建透過
- [ ] 相關測試透過，新增功能已補測試
- [ ] 已按提交資訊規範撰寫提交資訊
- [ ] 文件已同步更新或確認無需更新
- [ ] 未引入金鑰、隱私資料或大檔案

## 破壞性變更

{{破坏性变更说明}}

## 相關文件

- [ ] README 已同步或無需更新
- [ ] CHANGELOG 已登記
- [ ] API 文件已同步或無需更新
````

### 4.4 佔位符對照表

| 佔位符 | 必填 | 填寫要點 |
| --- | --- | --- |
| `{{变更说明}}` | 是 | 一句陳述改動內容，並附 `#数字` 形式的 issue 編號 |
| `{{破坏性变更说明}}` | 是 | 無破壞性變更寫「無」；有則寫遷移步驟並連結遷移指南 |

YAML 表單的 `name`、`description`、`title`、`labels` 為模板後設資料，按專案實際情況替換；`body` 中欄位型別與 `required` 值按第 2、3 節欄位清單調整，不得刪減必填項。

### 4.5 完整填寫示例

缺陷報告的填寫示例：

````markdown
## 問題描述

執行 `npm run build` 後程序退出，退出碼為 1。

## 預期行為

構建成功並輸出 `dist/` 目錄。

## 復現步驟

1. 檢出 v1.0.0 標籤
2. 執行 `npm ci`
3. 執行 `npm run build`，觀察到退出碼 1

## 專案版本

v1.0.0

## 作業系統

macOS

## 日誌或截圖

```
Error: Cannot find module 'mdlint-core'
```

## 資訊保安確認

- [x] 已確認未包含金鑰、令牌或個人隱私
````

## 5. 寫作要求

1. 欄位說明使用祈使句或陳述句，不得口語化。
2. 每個必填欄位給出填寫示例或格式要求。
3. 提示文字須說明「為什麼需要此資訊」，避免空泛要求。
4. 涉及隱私的欄位須提示脫敏（見 [安全與隱私規範](./安全與隱私規範.md)）。
5. 模板隨專案演進更新，廢棄欄位須刪除，不得長期堆積。

## 6. 禁止事項

1. 禁止把所有問題型別合併為一個自由文字模板。
2. 禁止設定與定位問題無關的必填欄位。
3. 禁止在模板中放入專案介紹或營銷內容。
4. 禁止 PR 模板遺漏自測清單與破壞性變更宣告。

## 相關檔案

- 檔案職責邊界見 [文件矩陣](./文件矩陣.md)
- 貢獻流程見 [貢獻指南規範](./貢獻指南規範.md)
- 審查標準見 [程式碼審查規範](./程式碼審查規範.md)
- 破壞性變更遷移見 [遷移指南規範](./遷移指南規範.md)
- 社群治理檢查屬維度 D14，見 [稽核維度矩陣](./稽核維度矩陣.md)
