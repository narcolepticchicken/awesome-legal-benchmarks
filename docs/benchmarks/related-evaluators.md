# Evaluators, private tests, and related resources

<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->

Artifacts worth tracking that are not comparable public benchmarks, including frameworks, private tests, and resource lists.

Snapshot: **2026-08-04** · 4 entries

[Back to README](../../README.md) · [Catalog index](../catalog.md) · [Selection guide](../selection-guide.md) · [Metric field guide](../metric-theory.md) · [Methodology](../methodology.md)

## On this page

- [LegalEval-Q](#legaleval-q)
- [LRAGE](#lrage)
- [prinzbench](#prinzbench)
- [awesome-legal-nlp](#awesome-legal-nlp)

<a id="legaleval-q"></a>
## LegalEval-Q

`legaleval-q` · **evaluation-framework** · **related artifact** · fixed-release

Predict the quality of Chinese LLM-generated legal answers.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | LegalEval-Q authors (academic) |
| First documented | [2025-05-30](https://arxiv.org/abs/2505.24826) — arXiv v1 submission |
| Latest verified update | [2026-02-26](https://github.com/lyxx3rd/LegalEval-Q) — GitHub repository push |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Scorer research: study a learned evaluator of Chinese legal answer quality and its agreement with human labels.
- Protocol inspiration for multi-dimension answer-quality rubrics in Chinese-language legal products.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | A learned five-dimension regressor and adjusted aggregate score approximate human quality labels; it evaluates outputs, not legal tasks against authoritative answers. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | About 10k source queries; 946 annotated items, about 9,460 model-output annotations, and 60 validation items |
| Splits | Evaluator-training and small validation subsets |
| Source material | Legal queries, model responses, and AI-assisted/human quality annotations |
| Input | Question and generated legal answer |
| Output | Five dimension scores and adjusted aggregate |
| Baselines / leaderboard context | Paper compares evaluator models and correlation/agreement with annotations. |
| Dataset access | Artifacts referenced through GitHub/ModelScope |
| License | Unresolved |
| Gating | Some model artifacts may require external platform access |
| Maintenance | Research release; no public leaderboard. |
| Reproducibility | Limited by licensing, model artifacts, and the small validation set. |

### Metrics

- **Dimension regression / AdjScore:** Predict per-dimension quality labels and combine them with the paper's adjustment formula. Judge: Learned LegalEval-Q evaluator. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/lyxx3rd/LegalEval-Q](https://github.com/lyxx3rd/LegalEval-Q) |
| Paper / arXiv | [https://arxiv.org/abs/2505.24826](https://arxiv.org/abs/2505.24826) |

### Validity and evidence

**Risks / caveats**
- Training an evaluator on AI-assisted annotations can create circular model-family bias.
- A high evaluator score is not independent proof that an answer is legally correct.

**Verified facts**
- Official paper/repository define it as an answer-quality evaluator.

**Unresolved ambiguity**
- Public license and complete artifact accessibility remain unresolved.

Original source bullet(s): #18

[Back to page index](#on-this-page)

<a id="lrage"></a>
## LRAGE

`lrage` · **evaluation-framework** · **related artifact** · active

Configure legal RAG evaluations across retrievers, rerankers, agents, judges, and custom corpora.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | LRAGE authors (academic) |
| First documented | [2025-04-02](https://arxiv.org/abs/2504.01840) — arXiv v1 submission |
| Latest verified update | [2026-07-03](https://github.com/hoorangyee/LRAGE) — GitHub repository push |
| Access level | open |
| Test labels | not-applicable |
| Independently runnable | yes |

### Possible use cases

- Assemble a custom legal RAG evaluation by configuring retrievers, rerankers, judges, and corpora in one harness.
- Run an internal holdout corpus through a frozen, reproducible evaluation configuration.
- Protocol reference for reporting retrieval, judge, and corpus versions together.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | LRAGE supplies orchestration rather than one fixed construct; validity is inherited from the selected corpus, task, judge, and metric configuration. |
| Jurisdiction | Global / configuration-dependent |
| Languages | Multiple / configuration-dependent |
| Size | No fixed dataset |
| Splits | Uses LegalBench, LawBench, KBL, Pile-of-Law, PLAT, bar-exam QA, housing QA, or custom JSON |
| Source material | User-selected public/custom corpora |
| Input | Configured corpus, queries, and pipeline |
| Output | Retrieval, reranking, answer, and optional judge results |
| Baselines / leaderboard context | Paper demonstrates multiple legal RAG configurations; there is no one unified leaderboard. |
| Dataset access | Framework plus selected datasets |
| License | MIT framework; selected corpus licenses vary |
| Gating | Depends on models/data |
| Maintenance | Active toolkit. |
| Reproducibility | Potentially strong with a frozen config and dependencies; weak when users omit judge/model/corpus revisions. |

### Metrics

- **Inherited task/retrieval/judge metrics:** Metric set is configuration-dependent and must be reported with corpus and judge versions. Judge: Optional/configurable. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/hoorangyee/LRAGE](https://github.com/hoorangyee/LRAGE) |
| Hugging Face | [https://huggingface.co/datasets/hoorangyee/pile-of-law-bm25](https://huggingface.co/datasets/hoorangyee/pile-of-law-bm25) |
| Paper / arXiv | [https://arxiv.org/abs/2504.01840](https://arxiv.org/abs/2504.01840) |

### Validity and evidence

**Risks / caveats**
- Cross-run comparisons are invalid when configurations differ.
- It inherits every selected corpus's leakage, rights, and temporal-validity risks.

**Verified facts**
- Official paper/repository describe a configurable framework rather than a fixed benchmark.

Original source bullet(s): #19

[Back to page index](#on-this-page)

<a id="prinzbench"></a>
## prinzbench

`prinzbench` · **private-benchmark** · **related artifact** · private

Answer obscure US legal-research and general information-search questions.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | prinz.ai (company; commercial interest) |
| First documented | [2026-01-19](https://github.com/prinz-ai/prinzbench) — GitHub repository creation |
| Latest verified update | [2026-07-18](https://github.com/prinz-ai/prinzbench) — GitHub repository push |
| Access level | private |
| Test labels | hidden |
| Independently runnable | no |

### Possible use cases

- Read as one practitioner's longitudinal signal on obscure US legal-research questions across model generations.
- Protocol inspiration for building a withheld internal research-question set with pass/fail grading.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Single-author human pass/fail attempts to measure research usefulness, but withheld items and non-blind grading prevent independent construct validation. |
| Jurisdiction | United States |
| Languages | English |
| Size | 33 withheld questions: 25 legal research and 8 search; three runs each (99 evaluations) |
| Splits | Private question set |
| Source material | Author-created withheld questions |
| Input | Free-form research question |
| Output | Free-form answer and sources |
| Baselines / leaderboard context | Repository reports selected model results; outsiders cannot rerun the same questions. |
| Dataset access | Private/withheld |
| License | No clear license visible |
| Gating | No independent access path |
| Maintenance | Author-maintained private test. |
| Reproducibility | Not independently reproducible. |

### Metrics

- **Human pass/fail and pass@1:** Author judges each answer; subtotals by legal/search category. Judge: Single benchmark author. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/prinz-ai/prinzbench](https://github.com/prinz-ai/prinzbench) |
| Leaderboard / competition | [https://github.com/prinz-ai/prinzbench](https://github.com/prinz-ai/prinzbench) |

### Validity and evidence

**Risks / caveats**
- Hidden questions reduce contamination but also block auditability and independent scoring.
- Single-author non-blind judgments may reflect unmeasured preferences.

**Verified facts**
- Public repository describes 33 private questions and 99 runs.

**Unresolved ambiguity**
- Question contents, rubric detail, and license are unavailable.

Original source bullet(s): #21

[Back to page index](#on-this-page)

<a id="awesome-legal-nlp"></a>
## awesome-legal-nlp

`awesome-legal-nlp` · **resource-list** · **related artifact** · active

Discovery index for legal NLP datasets, models, papers, surveys, books, and events.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Maastricht Law & Tech Lab (community) |
| First documented | [2020-09-16](https://github.com/maastrichtlawtech/awesome-legal-nlp) — GitHub repository creation |
| Latest verified update | [2025-10-14](https://github.com/maastrichtlawtech/awesome-legal-nlp) — GitHub repository push |
| Access level | not-applicable |
| Test labels | not-applicable |
| Independently runnable | not-applicable |

### Possible use cases

- Discovery: locate legal NLP datasets, models, papers, surveys, and events beyond this catalog.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | No evaluation construct is defined; this is a curated bibliography/resource list, not an instrument for measuring model capability. |
| Jurisdiction | Global / mixed |
| Languages | Multiple |
| Size | No benchmark instances |
| Splits | None |
| Source material | Community-curated links |
| Input | Not applicable |
| Output | Not applicable |
| Baselines / leaderboard context | None. |
| Dataset access | No dataset |
| License | MIT repository |
| Gating | None |
| Maintenance | Community-maintained resource list. |
| Reproducibility | Not applicable as an evaluation artifact. |

### Metrics

- **Not applicable:** No scorer or evaluation protocol exists. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/maastrichtlawtech/awesome-legal-nlp](https://github.com/maastrichtlawtech/awesome-legal-nlp) |

### Validity and evidence

**Risks / caveats**
- Treating a resource list as a benchmark confuses discovery coverage with measured capability.

**Verified facts**
- Repository contents are links and prose rather than instances, gold labels, or graders.

Original source bullet(s): #7

[Back to page index](#on-this-page)
