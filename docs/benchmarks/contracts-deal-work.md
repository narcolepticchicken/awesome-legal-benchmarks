# Contracts and deal work

<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->

Clause extraction, provision classification, entailment, retrieval, merger agreements, and redlining.

Snapshot: **2026-08-03** · 7 entries

[Catalog index](../catalog.md) · [Selection guide](../selection-guide.md) · [Metric field guide](../metric-theory.md) · [Methodology](../methodology.md)

## On this page

- [Contract Understanding Atticus Dataset](#cuad)
- [LEDGAR](#ledgar)
- [ContractNLI](#contractnli)
- [Merger Agreement Understanding Dataset](#maud)
- [Atticus Clause Retrieval Dataset](#acord)
- [ContractEval](#contracteval)
- [RedlineBench](#redlinebench)

<a id="cuad"></a>
## Contract Understanding Atticus Dataset

`cuad` · **benchmark** · **recommended** · fixed-release

Locate 41 categories of commercially important clauses in long contracts.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Extractive QA turns issue spotting into span retrieval: a model should find every relevant token while avoiding unrelated language and correctly abstain when a clause is absent. |
| Jurisdiction | United States / SEC filings |
| Languages | English |
| Size | 510 contracts; 13,000+ expert labels; common QA release has 22,450 train and 4,182 test rows |
| Splits | Train/test SQuAD-style QA release |
| Source | Material contracts filed in SEC EDGAR |
| Input | Contract text plus a clause-category question |
| Output | One or more answer spans, or no answer |
| Baselines / leaderboard context | Paper reports BERT-family extractive QA baselines; many later long-context systems reuse the public test set. |
| Dataset access | Public |
| License | CC BY 4.0 for annotations/release; source contracts retain underlying rights |
| Gating | None |
| Maintenance | Stable established release. |
| Reproducibility | Data and evaluation code are public; normalize tokenization and no-answer handling exactly. |

### Metrics

- **Token intersection-over-union (Jaccard):** |predicted-token set ∩ gold-token set| / |union|, with precision/recall and AUPR across confidence thresholds. **Primary.**
- **AUPR:** Area under the precision–recall curve over clause predictions, useful under strong class imbalance.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/The-Atticus-Project/cuad](https://github.com/The-Atticus-Project/cuad) |
| Hugging Face | [https://huggingface.co/datasets/theatticusproject/cuad-qa](https://huggingface.co/datasets/theatticusproject/cuad-qa) |
| Paper / arXiv | [https://arxiv.org/abs/2103.06268](https://arxiv.org/abs/2103.06268) |
| Leaderboard / competition | None |
| Project | [https://www.atticusprojectai.org/cuad](https://www.atticusprojectai.org/cuad) |

### Validity and evidence

**Risks / caveats**
- Public contracts and gold spans are heavily reused and contamination-prone.
- Boilerplate similarity can reward memorization more than issue spotting on novel drafting styles.

**Verified facts**
- Official project, GitHub, paper, and author HF release agree on the benchmark identity.

**Inference**
- None recorded.

**Unresolved ambiguity**
- Published descriptions count annotations, QA rows, and labels differently; state which unit is reported.

Original source bullet(s): #4

[Back to page index](#on-this-page)

<a id="ledgar"></a>
## LEDGAR

`ledgar` · **dataset** · **specialist** · fixed-release

Classify contract provisions into clause/topic labels.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Provision classification measures whether representations separate contract-language topics; macro-F1 exposes rare-label performance while micro-F1 emphasizes the frequent-label mass. |
| Jurisdiction | United States / SEC filings |
| Languages | English |
| Size | Original corpus: about 846,274 provisions, 12,608 labels, 60,540 contracts; LexGLUE subset: 60k/10k/10k over 100 labels |
| Splits | Original and LexGLUE splits differ |
| Source | SEC EDGAR contracts |
| Input | A contract provision |
| Output | Provision label(s) |
| Baselines / leaderboard context | Original paper and LexGLUE report neural and transformer classifiers. |
| Dataset access | Public code/data paths; LexGLUE package is directly loadable |
| License | LexGLUE package CC BY 4.0; underlying filing rights and original release terms should be reviewed |
| Gating | None |
| Maintenance | Original dataset is stable; LexGLUE is the maintained standardized task. |
| Reproducibility | Strong if the exact original versus LexGLUE variant, label vocabulary, and split are named. |

### Metrics

- **Micro-F1 and macro-F1:** Micro pools all label decisions; macro averages per-label F1 so rare labels have equal weight. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/dtuggener/LEDGAR_provision_classification](https://github.com/dtuggener/LEDGAR_provision_classification)<br>[https://github.com/coastalcph/lex-glue](https://github.com/coastalcph/lex-glue) |
| Hugging Face | [https://huggingface.co/datasets/coastalcph/lex_glue](https://huggingface.co/datasets/coastalcph/lex_glue) |
| Paper / arXiv | [https://aclanthology.org/2020.lrec-1.155/](https://aclanthology.org/2020.lrec-1.155/) |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- SEC boilerplate enables document-family leakage and near-duplicate memorization.
- Reporting LEDGAR without naming the original or 100-label LexGLUE variant is ambiguous.

**Verified facts**
- The README's Metatext link is secondary; the original repository and LexGLUE are canonical sources.

**Inference**
- None recorded.

**Unresolved ambiguity**
- Source-rights treatment is not identical to the annotation license.

Original source bullet(s): #5

[Back to page index](#on-this-page)

<a id="contractnli"></a>
## ContractNLI

`contractnli` · **benchmark** · **recommended** · fixed-release

Determine whether a non-disclosure agreement entails, contradicts, or does not mention a fixed legal hypothesis and identify supporting evidence.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Three-way document NLI tests semantic/legal relation to 17 hypotheses; evidence identification tests whether the decision is grounded in the right spans. |
| Jurisdiction | Commercial NDAs / primarily United States practice |
| Languages | English |
| Size | 607 NDAs and 17 fixed hypotheses |
| Splits | 423 train / 61 development / 123 test contracts |
| Source | Publicly available NDAs annotated for hypotheses and evidence |
| Input | Full NDA plus one hypothesis |
| Output | Entailment, contradiction, or not-mentioned label plus evidence spans |
| Baselines / leaderboard context | Official project reports document-NLI and evidence-selection baselines. |
| Dataset access | Public official project/GitHub |
| License | CC BY 4.0 |
| Gating | None |
| Maintenance | Stable research release. |
| Reproducibility | High with official splits and evidence scorer; third-party HF copies are not canonical. |

### Metrics

- **Micro/macro F1 for NLI:** F1 over the three labels with stated aggregation. **Primary.**
- **Evidence identification F1:** Overlap/classification F1 over evidence spans or sentence selections. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/stanfordnlp/contract-nli](https://github.com/stanfordnlp/contract-nli) |
| Hugging Face | None |
| Paper / arXiv | [https://arxiv.org/abs/2110.01799](https://arxiv.org/abs/2110.01799) |
| Leaderboard / competition | None |
| Project | [https://stanfordnlp.github.io/contract-nli/](https://stanfordnlp.github.io/contract-nli/) |

### Validity and evidence

**Risks / caveats**
- Only 17 fixed hypotheses invite template-specific learning.
- NDA boilerplate and public test labels create near-duplicate and contamination risk.

**Verified facts**
- Official Stanford project/repository/paper define 607 NDAs and 17 hypotheses.

**Inference**
- None recorded.

**Unresolved ambiguity**
- No author-owned canonical HF dataset was found; available HF copies are third-party.

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)

<a id="maud"></a>
## Merger Agreement Understanding Dataset

`maud` · **benchmark** · **recommended** · fixed-release

Answer fine-grained questions about merger-agreement provisions.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Question-conditioned provision classification tests whether models can identify deal terms and exceptions across complex acquisition agreements. |
| Jurisdiction | United States / public-company M&A |
| Languages | English |
| Size | 152 merger agreements, more than 39,000 examples, more than 47,000 expert annotations, 92 question types |
| Splits | Official release includes full and abridged task files |
| Source | Public merger agreements with expert legal annotations |
| Input | Agreement text/provision plus a legal question |
| Output | Categorical answer or no-answer class |
| Baselines / leaderboard context | Paper evaluates transformer encoders and prompted LLMs. |
| Dataset access | Public |
| License | Official release license applies; underlying agreements remain source documents |
| Gating | None observed |
| Maintenance | Stable Atticus Project release. |
| Reproducibility | Good with named full/abridged variant, split, and question aggregation. |

### Metrics

- **Micro-F1 and macro-F1:** Micro summarizes all decisions; macro weights each question/label class equally. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/TheAtticusProject/maud](https://github.com/TheAtticusProject/maud) |
| Hugging Face | [https://huggingface.co/datasets/theatticusproject/maud](https://huggingface.co/datasets/theatticusproject/maud) |
| Paper / arXiv | [https://arxiv.org/abs/2301.00876](https://arxiv.org/abs/2301.00876)<br>[https://aclanthology.org/2023.emnlp-main.1019/](https://aclanthology.org/2023.emnlp-main.1019/) |
| Leaderboard / competition | None |
| Project | [https://www.atticusprojectai.org/maud](https://www.atticusprojectai.org/maud) |

### Validity and evidence

**Risks / caveats**
- Only 152 agreements can produce agreement-family leakage across poorly grouped splits.
- Public deal documents and annotations are contamination-prone.

**Verified facts**
- Official GitHub/HF/project/paper identify 152 agreements and 92 questions.

**Inference**
- None recorded.

**Unresolved ambiguity**
- Counts differ depending on examples versus annotations; report the unit.

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)

<a id="acord"></a>
## Atticus Clause Retrieval Dataset

`acord` · **benchmark** · **recommended** · fixed-release

Rank precedent contract clauses for an attorney-written drafting need.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Graded expert relevance (1–5 stars, encoded 0–4) supports nDCG, while star-threshold precision@5 asks whether the top drafting candidates meet stricter usefulness levels. |
| Jurisdiction | United States / commercial contracts |
| Languages | English |
| Size | 114 queries and 126,662+ explicitly rated query-clause pairs across nine clause categories |
| Splits | 45% train / 5% validation / 50% test by query |
| Source | SEC EDGAR and selected Fortune 500 terms, with attorney-written queries and ratings |
| Input | Attorney drafting query plus clause corpus |
| Output | Ranked clauses |
| Baselines / leaderboard context | Paper/repository compare sparse, embedding, and reranking systems. |
| Dataset access | Public GitHub zip and HF mirror |
| License | CC BY 4.0 data; repository code/license metadata also includes MIT |
| Gating | None |
| Maintenance | Stable expert-annotated release. |
| Reproducibility | High with official BEIR files and qrels; HF viewer currently mis-parses the zip, so use raw files. |

### Metrics

- **nDCG@5 and nDCG@10:** Discounted cumulative gain over 0–4 relevance, normalized by the ideal ranking. **Primary.**
- **3/4/5-star precision@5:** Precision among top five at progressively stricter attorney-rating thresholds. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/TheAtticusProject/acord](https://github.com/TheAtticusProject/acord) |
| Hugging Face | [https://huggingface.co/datasets/theatticusproject/acord](https://huggingface.co/datasets/theatticusproject/acord) |
| Paper / arXiv | [https://arxiv.org/abs/2501.06582](https://arxiv.org/abs/2501.06582)<br>[https://aclanthology.org/2025.acl-long.1206/](https://aclanthology.org/2025.acl-long.1206/) |
| Leaderboard / competition | None |
| Project | [https://www.atticusprojectai.org/acord/](https://www.atticusprojectai.org/acord/) |

### Validity and evidence

**Risks / caveats**
- Only 114 queries make per-category estimates sensitive to individual queries.
- Explicitly rating irrelevant clauses reduces false negatives but cannot exhaust every potentially useful precedent.

**Verified facts**
- Official project/GitHub/HF agree on query count, pair count, splits, ratings, and metrics.

**Inference**
- None recorded.

**Unresolved ambiguity**
- HF dataset viewer failure is an access UX issue, not missing data.

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)

<a id="contracteval"></a>
## ContractEval

`contracteval` · **evaluation-protocol** · **related artifact** · fixed-release

Evaluate long-context LLM clause-risk extraction on the public CUAD test set.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | F1/F2 and Jaccard trade off overlap precision and recall, while false-no-related-clause rate isolates abstention failures; the protocol reuses CUAD rather than defining new ground truth. |
| Jurisdiction | United States / SEC filings |
| Languages | English |
| Size | CUAD test set, about 4,182 QA rows over 41 categories |
| Splits | Reused public CUAD test |
| Source | CUAD |
| Input | Contract plus clause question |
| Output | Span(s) or no-related-clause response |
| Baselines / leaderboard context | Paper evaluates 19 contemporary LLMs under one protocol. |
| Dataset access | Uses public CUAD |
| License | No separate dataset; CUAD terms apply |
| Gating | Model APIs may be required |
| Maintenance | Paper protocol, not a separately maintained benchmark release. |
| Reproducibility | Moderate if prompts/model versions are available; public API aliases can drift. |

### Metrics

- **F1 / F2 / Jaccard:** Overlap scores; F2 weights recall twice as strongly as precision. **Primary.**
- **False no-related-clause rate:** Share of positive items incorrectly rejected as containing no relevant clause.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | None |
| Hugging Face | [https://huggingface.co/datasets/theatticusproject/cuad-qa](https://huggingface.co/datasets/theatticusproject/cuad-qa) |
| Paper / arXiv | [https://arxiv.org/abs/2508.03080](https://arxiv.org/abs/2508.03080) |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- It is not a new dataset and should not be counted as independent evidence from CUAD.
- Paper figures use both 4,128 and 4,182, an unresolved count inconsistency.

**Verified facts**
- The protocol evaluates CUAD rather than releasing new labeled examples.

**Inference**
- None recorded.

**Unresolved ambiguity**
- 4,128 versus 4,182 evaluation rows.

Original source bullet(s): #15

[Back to page index](#on-this-page)

<a id="redlinebench"></a>
## RedlineBench

`redlinebench` · **benchmark** · **check before use** · active

Negotiate commercial contracts over four turns by producing native Word tracked changes and comments.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Weighted expert rubrics model five dimensions of good deal work; turn-weighted scoring balances all scenario×turn cells and penalizes edits that are legally wrong, commercially misaligned, or unlikely to close. |
| Jurisdiction | United States / commercial contracting |
| Languages | English |
| Size | 140 runnable Harbor tasks across three synthetic MSA scenarios and four turns |
| Splits | Public tasks/test index; repeated expert-rubric variants share some identical inputs |
| Source | Synthetic SaaS/professional-services negotiations with attorney-authored playbooks and rubrics |
| Input | Commercial context, side playbook, and evolving DOCX contract |
| Output | DOCX with native tracked changes/threaded comments plus finalization metadata |
| Baselines / leaderboard context | Crosby report and HF benchmark metadata publish model results; reproduction CLI supports custom agents. |
| Dataset access | Public 115 MB HF benchmark |
| License | CC BY 4.0 data; MIT code |
| Gating | Agent/model APIs and Word-processing tool environment required |
| Maintenance | Active 2026 vendor release registered as an HF Benchmark. |
| Reproducibility | Strong public task bundles and driver; judge/model versions and document-tool behavior must be pinned. |

### Metrics

- **Redline overall (0–100):** Per task clamp((earned − penalty)/total positive rubric weight); average within identical-input groups, then equally average 12 scenario×turn cells. Judge: LLM judge panel against attorney-authored weighted rubrics. **Primary.**
- **Five dimension scores:** Commercial context, legal correctness, negotiation quality, deal-closing orientation, and counterparty-acceptance prediction. Judge: LLM judge panel.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/crosbylegal/redline-bench](https://github.com/crosbylegal/redline-bench) |
| Hugging Face | [https://huggingface.co/datasets/crosbylegal/RedlineBench](https://huggingface.co/datasets/crosbylegal/RedlineBench) |
| Paper / arXiv | None |
| Leaderboard / competition | [https://huggingface.co/datasets/crosbylegal/RedlineBench](https://huggingface.co/datasets/crosbylegal/RedlineBench) |
| Project | [https://intelligence.crosby.ai/benchmark](https://intelligence.crosby.ai/benchmark) |

### Validity and evidence

**Risks / caveats**
- Only three negotiation scenarios limit external validity.
- Vendor-created benchmark and LLM panel may favor the authors' negotiation style and tool stack.

**Verified facts**
- Official GitHub/HF/report define all 140 tasks, five dimensions, exact aggregation, and licenses.

**Inference**
- None recorded.

**Unresolved ambiguity**
- HF source attribution is community/source rather than inspect-ai verified, per the dataset card.

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)
