---
title: "Exploring Multi-Objective Trade-offs in Reference Compound Selection for Validation Studies of Toxicity Assays"
collection: publications
category: preprints
excerpt: "毒性評価の検証に用いる対照化合物の選定を、化学構造・物性・毒性の多様性を考慮する多目的設計問題として検討しました。"
permalink: /publication/2025-05-11-reference-compound-selection
date: 2025-05-11
venue: "arXiv"
paperurl: "https://arxiv.org/abs/2505.07140"
citation: "Yohei Ohto, Tadahaya Mizuno, Yasuhiro Yoshikai, Hiromi Fujimoto, Hiroyuki Kusuhara. (2025). Exploring Multi-Objective Trade-offs in Reference Compound Selection for Validation Studies of Toxicity Assays. <i>arXiv preprint arXiv:2505.07140</i>."
---

[プレプリントを読む（arXiv）](https://arxiv.org/abs/2505.07140)

### 研究概要（日本語）

毒性評価手法の検証に使う対照化合物の選び方を、複数の目的のバランスを考える問題として整理しました。化学構造、物理化学的性質、毒性の多様性に着目し、遺伝的アルゴリズムを使って選択肢の違いやトレードオフを探索しています。特定の化合物セットを推奨するのではなく、選定の設計を比較・検討するための方法を示しています。

### Abstract

In chemical safety assessment, validation studies rely on reference compound lists to evaluate the applicability of alternative methods prior to regulatory acceptance. These lists are expected to cover multiple aspects, including chemical structure, physicochemical properties, and toxicity profiles. In practice, however, trade-offs among these aspects are typically addressed implicitly through expert judgment, making them difficult to examine systematically. 

Here, we formulate reference compound selection for toxicity assay validation as an explicit multi-objective design problem. We define three interpretable objectives capturing structural, physicochemical, and toxicity diversity, and employ a genetic algorithm as an exploratory tool to examine the trade-off structure and resulting Pareto-optimal solutions. Rather than prescribing optimal or recommended compound sets, this formulation enables systematic exploration of designs and explicit comparison of their positions within a common design space. 

As an illustrative application, we link existing assay datasets with expert-curated validation lists by treating "selected as a reference compound" as an annotation on the underlying compound pool. We show that expert-selected, random, and algorithmically generated compound lists occupy distinct regions of the design space. Furthermore, under an illustrative fixed modeling setup, different regions of the design space were associated with different observed evaluation outcomes, supporting the view that reference compound selection constitutes a structured dimension of evaluation design. Together, these results provide a methodological perspective for treating reference compound selection as an analyzable design object, complementing established expert-driven practices.
