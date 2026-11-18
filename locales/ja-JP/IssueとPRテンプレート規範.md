# IssueとPRテンプレート規範

> このファイルが解決する問題：`.github/ISSUE_TEMPLATE/*.yml` の構造化フォームと `.github/PULL_REQUEST_TEMPLATE.md` のセルフチェックリストについて、フィールド設計・形式・記述要件を定義し、問題報告と変更提出に実行可能な入力制約を持たせる。

## 1. 設計原則

1. **自由テキストより構造化を優先する**：Issue フォームは YAML で定義し、ドロップダウン、チェックボックス、必須項目によって入力を誘導し、無効な報告を減らす。
2. **必須項目を最小化する**：問題の特定に必要なフィールドのみを残し、任意フィールドを必須として扱ってはならない。
3. **セルフチェックを明示する**：PR テンプレートはチェック可能なセルフチェック項目をリスト形式で列挙し、コントリビューターが重要な手順を飛ばすことを防ぐ。
4. **責務を単一に保つ**：Issue フォームは情報収集を担い、プロジェクト紹介を載せない。PR テンプレートはセルフチェックを担い、機能説明を重複させない（[ドキュメントマトリクス](./ドキュメントマトリクス.md) に対応）。

## 2. Issue フォームの構造

### 2.1 ファイルと命名

- パスは `.github/ISSUE_TEMPLATE/*.yml` に固定し、テンプレートごとに 1 ファイルとする。
- ファイル名は小文字とハイフンを使用し、`bug-report.yml`、`feature-request.yml`、`question.yml` などとする。
- 少なくとも「不具合報告」と「機能リクエスト」の 2 種類のテンプレートを提供する。

### 2.2 標準フィールド

| フィールド | 型 | 必須 | 用途 |
| --- | --- | --- | --- |
| `name` | 文字列 | はい | テンプレートの表示名 |
| `description` | 文字列 | はい | テンプレートの用途説明 |
| `title` | 文字列プレフィックス | はい | 自動生成される問題タイトルのプレフィックス |
| `labels` | 配列 | いいえ | 自動付与するラベル |
| `body` | 配列 | はい | フォームフィールドのリスト |

`body` でよく使うフィールド型：

| 型 | 適用場面 | 例 |
| --- | --- | --- |
| `markdown` | 説明文、入力なし | 記入上の注意 |
| `textarea` | 長文の説明 | 問題の再現手順 |
| `input` | 単一行の短いテキスト | バージョン番号 |
| `dropdown` | 選択肢が限られる項目 | オペレーティングシステム、深刻度 |
| `checkboxes` | 複数項目の確認 | 重複問題を検索済みか |

### 2.3 不具合報告のフィールド一覧

1. 問題の説明（`textarea`、必須）：何が起きたか。
2. 期待する動作（`textarea`、必須）：どうなるべきか。
3. 再現手順（`textarea`、必須）：番号付きで列挙し、単独で再現できること。
4. 実行環境（`input` または `dropdown`）：オペレーティングシステム、ランタイム、プロジェクトのバージョン。
5. ログまたはスクリーンショット（`textarea`）：エラー情報を提供し、機密情報はマスキングすること。
6. 重複確認（`checkboxes`、必須）：既存の issue を検索済みであること。

### 2.4 機能リクエストのフィールド一覧

1. 問題の記述（`textarea`、必須）：現在どのような能力が欠けているか。
2. 利用シナリオ（`textarea`、必須）：誰がどのような状況で必要とするか。
3. 期待する案（`textarea`）：どのように実現したいか。
4. 代替案（`textarea`）：検討済みの他の方法。
5. 互換性への影響（`dropdown`）：破壊的変更を含むかどうか。

## 3. PR テンプレートの構造

### 3.1 必須ブロック

`PULL_REQUEST_TEMPLATE.md` は以下のブロックを含み、順序は固定とする：

1. 変更説明：今回の変更で何を行ったか、対応する issue 番号。
2. 変更種別：チェックボックスで選択する（機能、修正、ドキュメント、リファクタリング、テストなど。種別は [コミットメッセージ規範](./コミットメッセージ規範.md) を参照）。
3. セルフチェックリスト：チェック可能なセルフチェック項目。
4. 破壊的変更：なければ「なし」と記す。あれば移行方法を記す（[移行ガイド規範](./移行ガイド規範.md) を参照）。
5. 関連ドキュメント：README、CHANGELOG、API ドキュメントを同時に更新したか。

### 3.2 セルフチェックリストの例

```markdown
## セルフチェックリスト

- [ ] ローカルビルドが成功した
- [ ] 関連するテストが成功し、新機能にはテストを追加した
- [ ] [コミットメッセージ規範](./コミットメッセージ規範.md) に従ってコミットメッセージを作成した
- [ ] ドキュメントを同期更新した、または更新不要と確認した
- [ ] 鍵、プライバシーデータ、大容量ファイルを持ち込んでいない
```

## 4. コピー可能なテンプレート

### 4.1 不具合報告フォーム

`.github/ISSUE_TEMPLATE/bug-report.yml` として保存する：

```yaml
name: 不具合報告
description: 再現可能な機能異常を報告する
title: "[Bug]: "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        送信前に既存の issue を検索し、重複を避けてください。
        鍵、トークン、個人のプライバシー情報を貼り付けないでください。
  - type: checkboxes
    id: duplicate-check
    attributes:
      label: 重複確認
      options:
        - label: 既存の issue を検索し、重複報告ではないことを確認した
          required: true
  - type: textarea
    id: description
    attributes:
      label: 問題の説明
      description: 実際に何が起きたか
      placeholder: install コマンド実行後のプロセス終了コードが 1 だった
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: 期待する動作
      description: どうなるべきか
    validations:
      required: true
  - type: textarea
    id: steps
    attributes:
      label: 再現手順
      description: 番号付きで列挙し、他者が単独で再現できるようにする
      placeholder: |
        1. コマンドを実行する
        2. 出力を確認する
        3. 異常が発生する
    validations:
      required: true
  - type: input
    id: version
    attributes:
      label: プロジェクトのバージョン
      placeholder: v1.0.0
    validations:
      required: true
  - type: dropdown
    id: os
    attributes:
      label: オペレーティングシステム
      options:
        - macOS
        - Linux
        - Windows
        - その他
    validations:
      required: true
  - type: textarea
    id: logs
    attributes:
      label: ログまたはスクリーンショット
      description: エラー情報を提供し、機密情報はマスキングすること
      render: shell
  - type: checkboxes
    id: security
    attributes:
      label: 情報セキュリティ確認
      options:
        - label: 鍵、トークン、個人のプライバシーを含まないことを確認した
          required: true
```

### 4.2 機能リクエストフォーム

`.github/ISSUE_TEMPLATE/feature-request.yml` として保存する：

```yaml
name: 機能リクエスト
description: 新しい能力や改善案を提案する
title: "[Feature]: "
labels: ["enhancement"]
body:
  - type: textarea
    id: problem
    attributes:
      label: 問題の記述
      description: 現在どのような能力が欠けているか
    validations:
      required: true
  - type: textarea
    id: scenario
    attributes:
      label: 利用シナリオ
      description: 誰がどのような状況でその能力を必要とするか
    validations:
      required: true
  - type: textarea
    id: proposal
    attributes:
      label: 期待する案
      description: どのように実現したいか
  - type: textarea
    id: alternatives
    attributes:
      label: 代替案
      description: 検討済みの他の方法
  - type: dropdown
    id: breaking
    attributes:
      label: 破壊的変更を含むか
      options:
        - いいえ
        - はい
        - 不明
    validations:
      required: true
```

### 4.3 PR テンプレート

`.github/PULL_REQUEST_TEMPLATE.md` として保存する：

````markdown
## 変更説明

{{变更说明}}

## 変更種別

- [ ] 機能（feat）
- [ ] 修正（fix）
- [ ] ドキュメント（docs）
- [ ] フォーマット（style）
- [ ] リファクタリング（refactor）
- [ ] テスト（test）
- [ ] ビルドまたはツールチェーン（build / ci）

## セルフチェックリスト

- [ ] ローカルビルドが成功した
- [ ] 関連するテストが成功し、新機能にはテストを追加した
- [ ] コミットメッセージ規範に従ってコミットメッセージを作成した
- [ ] ドキュメントを同期更新した、または更新不要と確認した
- [ ] 鍵、プライバシーデータ、大容量ファイルを持ち込んでいない

## 破壊的変更

{{破坏性变更说明}}

## 関連ドキュメント

- [ ] README を同期済み、または更新不要
- [ ] CHANGELOG に登録済み
- [ ] API ドキュメントを同期済み、または更新不要
````

### 4.4 プレースホルダー対照表

| プレースホルダー | 必須 | 記入の要点 |
| --- | --- | --- |
| `{{变更说明}}` | はい | 変更内容を一文で述べ、`#数字` 形式の issue 番号を付す |
| `{{破坏性变更说明}}` | はい | 破壊的変更がなければ「なし」と記す。あれば移行手順を記し、移行ガイドにリンクする |

YAML フォームの `name`、`description`、`title`、`labels` はテンプレートのメタデータであり、プロジェクトの実情に合わせて置き換える。`body` 内のフィールド型と `required` の値は第 2 節・第 3 節のフィールド一覧に従って調整し、必須項目を削減してはならない。

### 4.5 記入例

不具合報告の記入例：

````markdown
## 問題の説明

`npm run build` を実行するとプロセスが終了し、終了コードは 1 であった。

## 期待する動作

ビルドが成功し、`dist/` ディレクトリが出力される。

## 再現手順

1. v1.0.0 タグをチェックアウトする
2. `npm ci` を実行する
3. `npm run build` を実行し、終了コード 1 を確認する

## プロジェクトのバージョン

v1.0.0

## オペレーティングシステム

macOS

## ログまたはスクリーンショット

```
Error: Cannot find module 'mdlint-core'
```

## 情報セキュリティ確認

- [x] 鍵、トークン、個人のプライバシーを含まないことを確認した
````

## 5. 記述要件

1. フィールドの説明は命令文または平叙文で記し、口語表現を用いてはならない。
2. 必須フィールドには記入例または形式要件を示す。
3. ヒント文は「なぜこの情報が必要か」を説明し、空疎な要求を避ける。
4. プライバシーに関わるフィールドはマスキングを促す（[セキュリティとプライバシー規範](./セキュリティとプライバシー規範.md) を参照）。
5. テンプレートはプロジェクトの進展に合わせて更新し、廃止したフィールドは削除すること。長期間にわたって蓄積してはならない。

## 6. 禁止事項

1. すべての問題種別を 1 つの自由テキストテンプレートに統合することを禁止する。
2. 問題の特定と無関係な必須フィールドを設定することを禁止する。
3. テンプレートにプロジェクト紹介やマーケティング的内容を入れることを禁止する。
4. PR テンプレートからセルフチェックリストと破壊的変更の宣言を欠落させることを禁止する。

## 関連ファイル

- ファイルの責務境界は [ドキュメントマトリクス](./ドキュメントマトリクス.md) を参照
- コントリビューション手順は [コントリビューションガイド規範](./コントリビューションガイド規範.md) を参照
- レビュー基準は [コードレビュー規範](./コードレビュー規範.md) を参照
- 破壊的変更の移行は [移行ガイド規範](./移行ガイド規範.md) を参照
- コミュニティガバナンスのチェックは次元 D14 に属し、[監査次元マトリクス](./監査次元マトリクス.md) を参照
