
## `_config.yml` に行った編集（要約）

日時: 2025-11-30

ファイル: `/_config.yml`

編集内容（追加・変更した主な項目）:

- **ロケール**: `locale` を `"en-US"` から `"ja-JP"` に変更しました（サイトを日本語向けに設定）。
- **サイト名**: `title` を `"Your Name / Site Title"` から `"大戸陽平 / Yohei Ohto"` に変更しました。
- **名前アンカー**: `name`（アンカー）を `"Your Name"` から `"大戸陽平"` に変更しました。
- **説明アンカー**: `description`（アンカー）を英語のテンプレから `"大戸陽平のアカデミックポートフォリオ"` に変更しました。
- **URL**: `url` を `https://academicpages.github.io` から `https://yoheiohto.github.io` に変更しました。
- **リポジトリ**: `repository` を `"academicpages/academicpages.github.io"` から `"YoheiOhto/YoheiOhto.github.io"` に変更しました。

- **author ブロック**: サイドバーに表示される著者情報を個人用に上書きしました。
	- `author.name`: `"Your Sidebar Name"` → `"大戸陽平 (Yohei Ohto)"` に変更。
	- `author.email`: `"none@example.org"` → `"oy826c60@gmail.com"` を設定。
	- `author.bio`: 英語の短文を日本語の自己紹介（機械学習・バイオインフォマティクス等）に更新。
	- `author.location`: `"Earth"` → `"Japan"` に変更。
	- `author.employer`: テンプレから `"Independent researcher"` に変更。
	- `author.github`: `"academicpages"` → `"YoheiOhto"` に変更。

- **タイムゾーン**: `timezone` を `Etc/UTC` から `Asia/Tokyo` に変更しました。

## `_pages/about.md` に行った編集（要約）

日時: 2025-11-30

ファイル: `/_pages/about.md`

編集内容（追加・変更した主な項目）:

- Iori Azuma さんのテンプレをベースに、**大戸 洋平 (Yohei Ohto)** 用の詳細テンプレ（スキャフォールド）を作成しました。
- フロントマターは維持しつつ、`title` / `excerpt` / `author_profile` / `redirect_from` を適切に設定しました。
- 表示名・連絡先の反映:
	- `name`（ページ本文）: `大戸 洋平（おおと ようへい / Yohei Ohto）` を設定。
	- `メール`: `oy826c60@gmail.com` を本文に記載。
	- `GitHub`: `https://github.com/YoheiOhto` を本文に記載。
- セクション構成を Iori さんのテンプレに合わせて作成しました（プレースホルダ付き）:
	- `Education / 学歴`
	- `Research Interests / 研究分野`
	- `Publications and Preprints / 論文・プレプリント`
	- `Conferences / 学会発表`（International / Domestic などの小見出しあり）
	- `Internships / Employment / インターン・職歴`
	- `Other Activities / その他の活動`
	- `Awards / Honors / 受賞`
	- `Scholarships / Grants / 奨学金・助成`

- プレースホルダとして各セクションに "(ここに〜を追加)" の注記を入れてあります。実データ（学歴・業績・発表・職歴等）を渡していただければ、私の方で整形してページに反映します。
- Iori さん元データの一部（参考用の発表・受賞リスト）がファイル下部に残っているため、不要であれば削除可能です。

推奨 / 次の手順:

- 実データを渡す（箇条書きで OK）: 学歴、代表論文（BibTeX 風でも可）、学会発表（会議名・年月）、職歴、受賞、助成など。
- `author.avatar` に使うプロフィール画像を `assets/images/` 等に追加し、`_config.yml` の `author.avatar` を更新する。
- 変更をコミットしてリモートにプッシュする（必要ならコミットメッセージ案を作成します）。

この追記で問題なければ、私の方で指定セクションにデータを入れて整形します。どのセクションから埋めますか？

