---
title: "Defining and Evaluating Cell–Cell Relation Extraction from Biomedical Literature under Realistic Annotation Constraints"
collection: publications
category: manuscripts
permalink: /publication/2025-12-29-cell-cell-relation-extraction
date: 2025-12-29
venue: "bioRxiv"
paperurl: "https://www.biorxiv.org/content/10.1101/2025.12.01.691726v1"
citation: "Mei Yoshikawa, Tadahaya Mizuno, Yohei Ohto, Hiromi Fujimoto, Hiroyuki Kusuhara. (2025). Defining and Evaluating Cell–Cell Relation Extraction from Biomedical Literature under Realistic Annotation Constraints. <i>bioRxiv preprint doi:10.1101/2025.12.01.691726</i>."
---

Cell–cell communication (CCC) plays a pivotal role in physiology and pathology. Although text mining has the potential to automate the construction of comprehensive CCC databases from biomedical literature, cell–cell relation extraction (CCRE) has not been established as a standalone natural language processing (NLP) task, and lack of annotated datasets prevents systematic evaluation. 

In this work, we define sentence-level CCRE and construct two annotated corpora to establish evaluation benchmarks. The first, SemMedCC, contains sentences filtered by rule-based literature mining, while the second, PubCC, contains unfiltered sentences directly sampled from PubMed to evaluate robustness. Using these corpora, we evaluate various relation extraction models under realistic annotation constraints, comparing different entity indication strategies, classification heads, and language model architectures (including BioBERT, PubMedBERT, and GPT-4). 

Our results demonstrate that CCRE is a challenging task due to the high semantic complexity of biological relation descriptions in literature. While domain-specific models like PubMedBERT generally outperform general-domain LLMs when training data is limited, performance is heavily dependent on training data size rather than model complexity. This work provides the first structured evaluation framework and benchmark dataset for CCRE, laying a foundation for scalable, literature-based reconstruction of cell-cell communication networks.
