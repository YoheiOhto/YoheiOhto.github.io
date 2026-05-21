# このサイトの編集ガイド

Academic Pages テンプレートをベースにしているため dir が多く分かりにくい。
実際に触る必要がある場所だけを以下にまとめる。

---

## 編集が必要な場所

### `_config.yml` — サイト全体の設定

- プロフィール（名前・bio・所属・メール）はここを編集する
- SNS・学術リンク（`googlescholar`、`orcid` など）が空欄のままなので、取得したら追加する

### `_pages/about.md` — トップページ（`/` に表示）

- 学歴・研究分野・学会発表テーブルが手書きで管理されている
- 学会発表は `_talks/` と**二重管理**になっているので注意（どちらかに統一したい）

### `_pages/cv.md` — CV ページ（`/cv/` に表示）

- 「（ここに所属機関を記載してください）」が残っているので修正が必要
- `about.md` と内容が一部重複・矛盾しているので合わせる

### `_publications/` — 論文リスト（`/publications/` に表示）

- **現在 5 ファイルすべてテンプレのダミー**（`paper-title-number-1〜5`）
- 論文がなければこれらを削除する
- 論文・プレプリントが出たら `YYYY-MM-DD-slug.md` の形式で追加する

### `_talks/` — 学会発表リスト（`/talks/` に表示）

- 実際の発表データは**すでにここに入っている**（5件）
- 新しい発表があれば `YYYY-MM-DD-slug.md` の形式で追加する

---

## 触らなくていい場所（テンプレの残骸）

削除しても問題ない：

| パス | 内容 |
|---|---|
| `_teaching/` | 2014・2015 年のダミー。教育実績がなければ削除でよい |
| `_portfolio/` | `portfolio-1.md`・`portfolio-2.html` はダミー。使わなければ削除 |
| `_posts/` | 2012〜2015 年のブログダミー。ブログを使わないなら削除 |
| `talkmap.py` / `talkmap.ipynb` | 発表地点の地図を描くツール。不要なら無視でよい |
| `markdown_generator/` | TSV から md を自動生成するスクリプト。手動管理するなら不要 |

以下はテンプレ管理用なので基本的に触らない：

- `_layouts/`・`_includes/`・`_sass/` — テーマのテンプレート HTML/CSS
- `assets/` — JS・CSS などの静的ファイル
- `_data/navigation.yml`・`_data/ui-text.yml` — ナビゲーションと UI 文言

---

## ファイル命名規則

### `_publications/` に論文を追加する場合

```
YYYY-MM-DD-short-slug.md
```

frontmatter の必須フィールド：

```yaml
---
title: "論文タイトル"
collection: publications
category: manuscripts   # または conferences
permalink: /publication/YYYY-MM-DD-short-slug
date: YYYY-MM-DD
venue: "雑誌名 or 学会名"
paperurl: "https://..."   # あれば
citation: "著者. (年). タイトル. <i>雑誌</i>."
---
```

### `_talks/` に学会発表を追加する場合

```
YYYY-MM-DD-short-slug.md
```

frontmatter の必須フィールド：

```yaml
---
title: "発表タイトル"
date: YYYY-MM-DD
event: "学会名"
location: "会場"
authors:
  - "Yohei OHTO"
  - "共著者名"
presentation_type: "口頭 / Oral" # または "ポスター / Poster"
session: "セッション番号"
---
```

---

## ローカルでプレビューする

```bash
bundle exec jekyll serve -l -H localhost
# → http://localhost:4000 で確認
```

Docker を使う場合：

```bash
docker compose up
# → http://localhost:4000 で確認
```
