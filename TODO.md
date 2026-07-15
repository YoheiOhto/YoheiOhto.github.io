# TODO — サイト修正リスト

## 🔴 緊急
*（完了済み）*

## 🟡 近いうちに対応

### コンテンツ
- [x] `_pages/terms.md` を更新 — 2016年テンプレのまま。Disqus・Google Analytics への言及があるが両方オフ。現状に合わせるか削除する

### ファイル・アセット
- [x] `files/` のテンプレ PDF を削除 — `paper1-3.pdf`・`slides1-3.pdf`・`bibtex1.bib` はすべて数KB のダミー。実ファイルがないなら削除する
- [x] プロフィール写真を差し替え — `260324_yohei_master.jpeg` を使用するよう `_config.yml`・`authors.yml` を更新

### 設定
- [x] `_config.yml` の `portfolio` コレクション定義を削除 — 中身が空なので定義ごと消した（`teaching` はコンテンツが存在するため維持）

---

## 🟢 余裕があればやりたい

### プロフィール・リンク
- [ ] `_config.yml` に Google Scholar URL を追加 — アカウントを作ったら `googlescholar:` に設定
- [x] `_config.yml` に ORCID を追加 — 取得したら `orcid:` に設定
- [x] `_config.yml` に ResearchGate・LinkedIn を追加 — 使っていれば
- [x] `_config.yml` の `bio` を更新 — 現在「Master student @ The University of Tokyo, Pharmaceutical Sciences」のみ。研究内容（NLP・毒性予測など）を一言加えると良い

### ファイル追加
- [ ] 学会発表のポスター・スライド PDF を `files/` に追加 — 各 `_talks/` ファイルの `link:` フィールドに対応するファイルを置く
- [ ] CV の PDF 版を `files/cv.pdf` として用意 — `_pages/cv-json.md` からリンクされている

### 見た目・細かい修正
- [x] `_pages/about.md` の「Selected Activities」見出しを修正 — 他の見出しと形式を揃えた
- [ ] ファビコン・OGP 画像を個人用に差し替え — 現在はテンプレのデフォルト画像
- [x] `_data/authors.yml` の bio を `_config.yml` と統一 — 現在「機械学習・バイオインフォマティクス・データ可視化」で研究内容の表現が微妙に異なる

---

## 📄 論文・発表が出たら

- [x] `_publications/` に論文・プレプリントを追加 — `HOW_TO_EDIT.md` の命名規則を参照
- [x] `_pages/about.md` の「現在準備中」を実際の citation に差し替え
- [x] `_pages/cv.md` の「特になし」を更新

---

## ✅ 対応済み

- [x] テンプレのダミーファイルを削除（`_publications/`・`_teaching/`・`_portfolio/`・`_posts/`・`_drafts/` 計15件）
- [x] `HOW_TO_EDIT.md` を作成（編集すべき場所のガイド）
- [x] `_data/cv.json` — 実データに書き直し（学歴・学会発表5件・奨学金など）
- [x] `_pages/cv.md` — 所属・学歴・研究分野・奨学金を `about.md` に合わせて統一
- [x] WINGS-IIW の年を 2024 に修正・BOOST NAIS を追加
- [x] `cv.md` に高校の記録・博士課程入学予定を追加
