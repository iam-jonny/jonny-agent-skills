# Jonny Agent Skills

プロダクトマネジメント作業を支援する、Codex / Claude Code 向けの
ローカルプラグインとスキル定義集です。

## 概要

このリポジトリには、Codex と Claude Code の両方で利用できるローカルプラグインが含まれています。
各ツール向けのメタデータも用意しています。

## 利用できるプラグイン

| Plugin | 目的 |
| --- | --- |
| `product-management-tools` | 雑多なプロダクト情報を、合意された BRD、PRD、PBI、優先順位、ロードマップへ整理する。 |
| `project-management-tools` | 雑多なプロジェクト情報を、チャーター、計画、リスク、ステータス報告、変更判断、振り返りへ整理する。 |

## Product Management Tools

`product-management-tools` は、雑多なプロダクト情報を、意思決定に使える成果物と
合意形成プロセスへ整理することを支援します。

- 会議メモ、音声書き起こし、紙メモの OCR、ステークホルダー要望
- BRD とビジネス要件
- PRD と承認計画
- ミッション・ビジョン・バリュー
- Product Backlog Item
- バックログの優先順位付け
- プロダクトロードマップ

粗いアイデア、戦略メモ、ステークホルダーからの要望、ドラフト文書を、
より明確で意思決定に使える成果物へ整理することを目的としています。

## ワークフローモデル

各スキルは、単体でも使えますが、プロダクトマネジメントの流れに沿って
組み合わせて使えるように設計しています。

- Intake layer: 雑多な入力を、成果物作成前の構造化された文脈に整理する。
- Definition layer: BRD、PRD、MVV などの中核成果物を作成する。
- Review layer: 成果物の品質と準備状況を確認する。
- Alignment layer: 承認、レビュー会、意思決定ログ、ステークホルダー合意を支援する。
- Execution layer: PBI の整理、優先順位付け、ロードマップ化を支援する。
- Orchestration layer: 曖昧な依頼を診断し、適切なスキル順序を提案する。

典型的な流れは次の通りです。

```text
会議メモ / 紙メモ / 音声書き起こし / ステークホルダー要望
  -> product-orchestrator
  -> product-intake-synthesize
  -> brd-create
  -> business-requirements-review
  -> artifact-alignment
  -> prd-create
  -> prd-review
  -> stakeholder-review-synthesize
  -> pbi-review / pbi-prioritize / roadmap-create
```

## Codex プラグイン

Product Management Tools の本体は次の場所にあります。

```text
plugins/product-management-tools
```

Codex 用のプラグイン manifest は次のファイルです。

```text
plugins/product-management-tools/.codex-plugin/plugin.json
```

Codex はこの manifest を使って、プラグイン名、表示情報、スキルディレクトリを検出します。

Project Management Tools の本体は次の場所にあります。

```text
plugins/project-management-tools
```

Codex 用のプラグイン manifest は次のファイルです。

```text
plugins/project-management-tools/.codex-plugin/plugin.json
```

## Claude Code マーケットプレイス

Claude Code 用の marketplace manifest も含まれています。

```text
.claude-plugin/marketplace.json
```

この marketplace から、次のプラグインを公開します。

```text
plugins/product-management-tools
```

Claude Code 用のプラグイン manifest は次のファイルです。

```text
plugins/product-management-tools/.claude-plugin/plugin.json
```

このリポジトリを public にした後、Claude Code では次のように marketplace を追加できます。

```text
/plugin marketplace add iam-jonny/jonny-agent-skills
```

その後、必要なプラグインをインストールします。

```text
/plugin install product-management-tools@jonny-agent-skills
/plugin install project-management-tools@jonny-agent-skills
```

ローカル checkout からテストする場合は、次のように追加します。

```text
/plugin marketplace add ./path/to/jonny-agent-skills
/plugin install product-management-tools@jonny-agent-skills
/plugin install project-management-tools@jonny-agent-skills
```

## スキル一覧

| Skill | 目的 |
| --- | --- |
| `product-orchestrator` | 曖昧な PM 依頼を診断し、適切なスキル順序を提案する。 |
| `product-intake-synthesize` | 会議メモ、書き起こし、OCR、ステークホルダー要望を構造化された PM 文脈に整理する。 |
| `brd-create` | PRD 作成前に、ビジネス要件文書を作成する。 |
| `artifact-alignment` | ステークホルダー合意、承認、レビュー会、意思決定ログを計画する。 |
| `stakeholder-review-synthesize` | ステークホルダーのフィードバックを、決定事項、必要な修正、アクション、フォローアップに整理する。 |
| `mvv-create` | ミッション・ビジョン・バリューのドラフトを作成する。 |
| `mvv-review` | MVV を明確性、具体性、意思決定への有用性の観点でレビューする。 |
| `business-requirements-review` | ビジネス要件を成果、制約、リスク、準備状況の観点でレビューする。 |
| `prd-create` | 粗い文脈から実用的な PRD を作成する。 |
| `prd-review` | PRD を明確性、完成度、実行リスクの観点でレビューする。 |
| `pbi-review` | PBI、ユーザーストーリー、エピック、受け入れ条件をレビューする。 |
| `pbi-prioritize` | impact、confidence、effort、risk、strategic fit などの基準で PBI を優先順位付けする。 |
| `roadmap-create` | outcome oriented なプロダクトロードマップを作成する。 |
| `roadmap-review` | ロードマップを戦略適合性、順序、実現性、信頼性の観点でレビューする。 |

各スキルは次の場所にある `SKILL.md` で定義されています。

```text
plugins/product-management-tools/skills/<skill-name>/SKILL.md
```

一部のスキルには、Codex UI 向けの表示名、短い説明、デフォルトプロンプトを定義する
`agents/openai.yaml` も含まれています。

## プロダクトマネジメントの共通リファレンス

共通のプロダクトマネジメント指針は次のファイルにまとめています。

```text
plugins/product-management-tools/references/product-management-principles.md
```

このリファレンスには、教科書的なプロダクトマネジメントの考え方と、
実務で使う判断基準を整理しています。対象は Discovery、Delivery、Metrics、
Prioritization、Roadmaps、よくある失敗パターンです。

各スキルは、この共通リファレンスのうち関連する部分を参照しつつ、
成果物ごとの具体的な作成・レビュー観点を追加しています。

## Project Management Tools

`project-management-tools` は、プロジェクトマネージャーの実務フローに沿って、
曖昧な入力から計画、管理、報告、変更判断、振り返りまでを支援します。

- Intake layer: 会議メモ、書き起こし、OCR、ステークホルダー要望、リスク、決定事項を整理する。
- Definition layer: プロジェクトチャーターとプロジェクト計画を作成する。
- Control layer: リスク登録簿、ステータス報告、変更要求を扱う。
- Communication layer: ステークホルダー更新、意思決定依頼、エスカレーションを設計する。
- Learning layer: 振り返りを具体的な改善アクションへ変換する。
- Orchestration layer: 曖昧なプロジェクト依頼を診断し、適切なスキル順序を提案する。

典型的な流れは次の通りです。

```text
会議メモ / ステークホルダー要望 / プロジェクト案
  -> project-orchestrator
  -> project-intake-synthesize
  -> project-charter-create
  -> project-plan-create
  -> risk-register-create
  -> stakeholder-communication-plan
  -> status-report-create / change-request-review
  -> meeting-action-synthesize / retrospective-synthesize
```

Project Management Tools のスキル一覧:

| Skill | 目的 |
| --- | --- |
| `project-orchestrator` | 曖昧なプロジェクト依頼を診断し、適切なスキル順序を提案する。 |
| `project-intake-synthesize` | 会議メモ、書き起こし、OCR、ステークホルダー要望を構造化されたプロジェクト文脈に整理する。 |
| `project-charter-create` | 詳細計画の前に、プロジェクトチャーターを作成する。 |
| `project-plan-create` | マイルストーン、担当者、依存関係、リスク、コミュニケーション頻度を含む計画を作成する。 |
| `risk-register-create` | オーナー、トリガー、軽減策、代替策、エスカレーション条件を含むリスク登録簿を作成する。 |
| `stakeholder-communication-plan` | ステークホルダー更新、意思決定依頼、チャネル、頻度、エスカレーションを計画する。 |
| `status-report-create` | RAG、進捗、リスク、意思決定、依頼事項を含むスポンサー向けステータス報告を作成する。 |
| `change-request-review` | プロジェクト変更要求をレビューし、承認、条件付き承認、却下、延期、分割、エスカレーションを提案する。 |
| `meeting-action-synthesize` | プロジェクト会議を、決定事項、アクション、リスク、依存関係、フォローアップに整理する。 |
| `retrospective-synthesize` | 振り返りを、学び、担当者、プロセス改善へ変換する。 |

共通のプロジェクトマネジメント指針は次のファイルにまとめています。

```text
plugins/project-management-tools/references/project-management-principles.md
```

## プロンプト例

```text
product-management-tools の product-orchestrator を使って、この PM 依頼の進め方を診断してください。
```

```text
product-management-tools の product-intake-synthesize を使って、この会議メモを PM 文脈に整理してください。
```

```text
product-management-tools の brd-create を使って、このステークホルダー要望から BRD を作成してください。
```

```text
product-management-tools の mvv-create を使って、このプロダクトの MVV を作成してください。
```

```text
product-management-tools の prd-review を使って、この PRD の課題を洗い出してください。
```

```text
product-management-tools の artifact-alignment を使って、この PRD の承認計画を作成してください。
```

```text
product-management-tools の pbi-prioritize を使って、このバックログを優先順位付けしてください。
```

```text
project-management-tools の project-orchestrator を使って、このプロジェクト依頼の進め方を診断してください。
```

```text
project-management-tools の project-intake-synthesize を使って、この会議メモをプロジェクト文脈に整理してください。
```

```text
project-management-tools の project-charter-create を使って、このプロジェクト案からチャーターを作成してください。
```

```text
project-management-tools の status-report-create を使って、スポンサー向けステータス報告を作成してください。
```

## ローカルでの利用

このリポジトリは、ローカルプラグインソースとして使える構成です。

Codex で利用する場合は、Codex がローカルプラグインとして参照できる環境から
対象プラグインのディレクトリをインストールまたは参照します。

Claude Code で利用する場合は、このリポジトリを marketplace として追加し、
必要なプラグインをインストールします。

プラグインの表示名は次の通りです。

```text
Product Management Tools
```

プラグインのパッケージ名は次の通りです。

```text
product-management-tools
project-management-tools
```

## 開発メモ

- 各スキルは、1 つのプロダクトマネジメント作業に集中させる。
- 具体的なレビュー基準と、意思決定に使える出力を重視する。
- 入力情報が不足している場合は、前提を明示する。
- どのプロダクトやチームにも当てはまるような汎用表現を避ける。
- 共通のプロダクトマネジメント概念は `references/` に置き、各 `SKILL.md` では成果物ごとの適用方法に集中する。
- プラグインレベルの機能を追加・改名・移動する場合は `.codex-plugin/plugin.json` を更新する。
