# GitHub Profile README カスタマイズガイド

このガイドは、大戸陽平様の GitHub プロファイル README （`YoheiOhto/YoheiOhto` リポジトリ）をモダンで絶対にリンク切れしないデザインにアップデートするためのものです。

---

## 1. 準備する GitHub Actions ワークフローファイル

ご自身の **`YoheiOhto/YoheiOhto`（プロファイル用の同名リポジトリ）** の中に、以下のディレクトリとファイルを作成してください。

### ① 3D草・実績メトリクス自動生成ワークフロー
ファイルパス: `.github/workflows/update-profile-assets.yml`

```yaml
name: Generate Profile Assets

on:
  schedule:
    - cron: "0 0 * * *" # 毎日日本時間午前9時に実行
  workflow_dispatch: # 手動実行も可能
  push:
    branches:
      - main
      - master

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      # 1. リポジトリのチェックアウト
      - uses: actions/checkout@v3

      # 2. 3D草 (github-profile-3d-contrib) の生成
      - name: Generate 3D Contribution Graph
        uses: yoshi389111/github-profile-3d-contrib@0.7.1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          USERNAME: ${{ github.repository_owner }}

      # 3. Metrics (Achievements & Languages & Isometric Calendar) の生成
      - name: Generate GitHub Metrics SVG
        uses: lowlighter/metrics@latest
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          filename: github-metrics.svg
          base: "" # ヘッダーなどは除外してプラグインのみ表示
          config_timezone: Asia/Tokyo
          
          # Achievements (実績・トロフィー)
          plugin_achievements: yes
          plugin_achievements_display: detailed
          plugin_achievements_secrets: yes
          
          # Languages (使用言語)
          plugin_languages: yes
          plugin_languages_ignored: html, css
          plugin_languages_details: bytes-size, percentage
          
          # Isometric Calendar (立体カレンダー)
          plugin_isocalendar: yes
          plugin_isocalendar_duration: half-year

      # 4. 生成した成果物をリポジトリにコミット&プッシュ
      - name: Commit and Push
        run: |
          git config user.name github-actions
          git config user.email github-actions@github.com
          git add -A
          git commit -m "chore: Update profile assets (3D graph & metrics)" || exit 0
          git push
```

> [!NOTE]
> `GITHUB_TOKEN` で動作するため、個別の PAT（Personal Access Token）を作成・登録しなくても自動で動作します。

---

## 2. コピー用 `README.md` のテンプレート

以下をご自身のプロファイルリポジトリの `README.md` にそのままコピー＆ペーストしてください。

```markdown
# 👋 Hi, I'm Yohei Ohto

- 🔬 Researcher / Developer at **Mizuno Group**  
- 🌐 Personal Page: [yoheiohto.github.io](https://yoheiohto.github.io/)  
- 🧪 Mizuno Group HP: [mizuno-group.com](https://www.mizuno-group.com/)  
- 🧬 Mizuno Group GitHub: [github.com/mizuno-group](https://github.com/mizuno-group)

---

## 🛠️ Skills & Tech Stack

### Languages & Frameworks
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![C++](https://img.shields.io/badge/C++-00599C?style=flat&logo=c%2B%2B&logoColor=white)](https://isocpp.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://html.spec.whatwg.org/)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://www.w3.org/Style/CSS/)

### Tools & Platforms
[![RDKit](https://img.shields.io/badge/RDKit-8A2BE2?style=flat)](https://www.rdkit.org/)
[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-FFD21E?style=flat)](https://huggingface.co/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)](https://git-scm.com/)
[![Jekyll](https://img.shields.io/badge/Jekyll-CC0000?style=flat&logo=jekyll&logoColor=white)](https://jekyllrb.com/)

---

## 🧭 About Me
- 💻 Interested in **computational science**, **data-driven modeling**, and **scientific software**
- ⚙️ Passionate about building clean, reproducible, and impactful research code  
- 🌱 Always exploring new tools & frameworks to accelerate scientific discovery

---

## 📊 Activity & Statistics

### 📅 3D Contribution Calendar
<!-- 3D草をリポジトリから静的に読み込みます。リンク切れしません -->
![](./profile-3d-contrib/profile-green-animate.svg)

### 🏆 Achievements & 🈷️ Languages
<!-- GitHub Actionsで生成した実績・言語インフォグラフィックスを読み込みます。リンク切れしません -->
![](./github-metrics.svg)

---

## 📫 Contact
Feel free to reach out through **GitHub Issues**, **email** ([oy826c60@gmail.com](mailto:oy826c60@gmail.com)), or via my [website](https://yoheiohto.github.io/).
```
