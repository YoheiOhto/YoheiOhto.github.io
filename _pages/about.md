---
permalink: /
title: "大戸 陽平 / Yohei Ohto"
excerpt: "Ph.D Student — Bioinformatics & Drug Discovery"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

東京大学大学院薬学系研究科 分子薬物動態学教室（楠原洋之 教授）の博士課程学生です。株式会社Preferred Networks（PFN）ではパートタイムエンジニアとして勤務しています。バイオインフォマティクスと機械学習を組み合わせて、創薬プロセスの加速に取り組んでいます。

現在の主なテーマは、**特許文書に含まれる時間軸情報の活用**です。医薬品化合物が「いつ・どのような文脈で記録されたか」という情報を *in silico* 毒性予測に組み込み、予測精度と解釈可能性の向上を目指しています。自然言語処理（NLP）による文献マイニングと化合物構造情報を組み合わせたアプローチに取り組んでいます。

Recent Activities / 最近の主な活動
------

- **2026/11/19（開催予定）**: **第41回日本薬物動態学会 PRIS 2026 オーガナイザー・座長** — [大会プログラム](https://www.jssx41.org/En/program.html)
- **2026/10–現在**: **株式会社Preferred Networks（PFN） パートタイムエンジニア**
- **2026/08–09**: **株式会社Preferred Networks（PFN） 夏期インターンシップ（ヘルスケア領域）** 修了
- **2025/12**: **bioRxiv プレプリント公開** — ["Defining and Evaluating Cell–Cell Relation Extraction from Biomedical Literature under Realistic Annotation Constraints"](https://www.biorxiv.org/content/10.1101/2025.12.01.691726v1)
- **2025/10**: **第40回日本薬物動態学会 PRIS 2025 招待講演** — ["特許時系列情報の医薬品への適用の妥当性とその in silico 毒性予測への応用"](/talks/2025-10-22-pris-2025-patent-time-series/)（みやこめっせ, 京都）

Contact / 連絡先
------
- Email: [oy826c60@gmail.com](mailto:oy826c60@gmail.com)
- GitHub: [YoheiOhto](https://github.com/YoheiOhto)

Skills / 使用技術
------

- **Python**（メイン）— データ解析・機械学習・NLP（scikit-learn, PyTorch, RDKit など）
- **C++**（基礎レベル）
- **Web 開発**（HTML / CSS / Jekyll）— 研究室ウェブサイト制作（[水野班サイト](https://www.mizuno-group.com/)）
- **機械学習・データ** — Hugging Face、vLLM、Elasticsearch、PubMed など
- **研究・開発環境** — Git、Docker、Apptainer / Singularity、Slurm、FastAPI

Publications and Preprints / 論文・プレプリント
------

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

Conferences / 学会発表
------

| 日付 | 学会 | 発表形態 | 会場 | タイトル |
|:----:|:-----|:--------:|:----|:--------|
{% for post in site.talks reversed %}| {{ post.date | date: "%Y/%m/%d" }} | {{ post.event }} | {{ post.presentation_type }} | {{ post.location }} | [{{ post.title }}]({{ post.url | relative_url }}) |
{% endfor %}

GitHub Activity / 開発活動
------

[![GitHubの年間活動を示す3Dグラフ](https://raw.githubusercontent.com/YoheiOhto/YoheiOhto/main/profile-3d-contrib/profile-green-animate.svg)](https://github.com/YoheiOhto)

---
💡 学歴・奨学金・TA実績などの詳細な経歴は [CV / 履歴書](/cv/) をご覧ください。
