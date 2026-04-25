# Jonny Agent Skills

プロダクトマネジメント作業を支援する、Codex / Claude Code 向けの
ローカルプラグインとスキル定義集です。

## 概要

このリポジトリには `product-management-tools` というプラグインが含まれています。
Codex と Claude Code の両方で利用できるように、各ツール向けのメタデータを用意しています。

このプラグインは、雑多なプロダクト情報を、意思決定に使える成果物と
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

プラグイン本体は次の場所にあります。

```text
plugins/product-management-tools
```

Codex 用のプラグイン manifest は次のファイルです。

```text
plugins/product-management-tools/.codex-plugin/plugin.json
```

Codex はこの manifest を使って、プラグイン名、表示情報、スキルディレクトリを検出します。

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

その後、プラグインをインストールします。

```text
/plugin install product-management-tools@jonny-agent-skills
```

ローカル checkout からテストする場合は、次のように追加します。

```text
/plugin marketplace add ./path/to/jonny-agent-skills
/plugin install product-management-tools@jonny-agent-skills
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

## ローカルでの利用

このリポジトリは、ローカルプラグインソースとして使える構成です。

Codex で利用する場合は、Codex がローカルプラグインとして参照できる環境から
`plugins/product-management-tools` をインストールまたは参照します。

Claude Code で利用する場合は、このリポジトリを marketplace として追加し、
`product-management-tools` をインストールします。

プラグインの表示名は次の通りです。

```text
Product Management Tools
```

プラグインのパッケージ名は次の通りです。

```text
product-management-tools
```

## 開発メモ

- 各スキルは、1 つのプロダクトマネジメント作業に集中させる。
- 具体的なレビュー基準と、意思決定に使える出力を重視する。
- 入力情報が不足している場合は、前提を明示する。
- どのプロダクトやチームにも当てはまるような汎用表現を避ける。
- 共通のプロダクトマネジメント概念は `references/` に置き、各 `SKILL.md` では成果物ごとの適用方法に集中する。
- プラグインレベルの機能を追加・改名・移動する場合は `.codex-plugin/plugin.json` を更新する。
