# Evaluators, private tests, and related resources

<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->

Artifacts worth tracking that are not comparable public benchmarks, including frameworks, private tests, and resource lists.

Snapshot: **2026-08-03** · 5 entries

[Catalog index](../catalog.md) · [Selection guide](../selection-guide.md) · [Metric field guide](../metric-theory.md) · [Methodology](../methodology.md)

## On this page

- [LegalEval-Q](#legaleval-q)
- [LRAGE](#lrage)
- [prinzbench](#prinzbench)
- [Open Legal-Answer Benchmark](#open-legal-answer-benchmark)
- [awesome-legal-nlp](#awesome-legal-nlp)

<a id="legaleval-q"></a>
## LegalEval-Q

`legaleval-q` · **evaluation-framework** · **related artifact** · fixed-release

Predict the quality of Chinese LLM-generated legal answers.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | A learned five-dimension regressor and adjusted aggregate score approximate human quality labels; it evaluates outputs, not legal tasks against authoritative answers. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | About 10k source queries; 946 annotated items, about 9,460 model-output annotations, and 60 validation items |
| Splits | Evaluator-training and small validation subsets |
| Source | Legal queries, model responses, and AI-assisted/human quality annotations |
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
| Hugging Face | None |
| Paper / arXiv | [https://arxiv.org/abs/2505.24826](https://arxiv.org/abs/2505.24826) |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Training an evaluator on AI-assisted annotations can create circular model-family bias.
- A high evaluator score is not independent proof that an answer is legally correct.

**Verified facts**
- Official paper/repository define it as an answer-quality evaluator.

**Inference**
- None recorded.

**Unresolved ambiguity**
- Public license and complete artifact accessibility remain unresolved.

Original source bullet(s): #18

[Back to page index](#on-this-page)

<a id="lrage"></a>
## LRAGE

`lrage` · **evaluation-framework** · **related artifact** · active

Configure legal RAG evaluations across retrievers, rerankers, agents, judges, and custom corpora.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | LRAGE supplies orchestration rather than one fixed construct; validity is inherited from the selected corpus, task, judge, and metric configuration. |
| Jurisdiction | Global / configuration-dependent |
| Languages | Multiple / configuration-dependent |
| Size | No fixed dataset |
| Splits | Uses LegalBench, LawBench, KBL, Pile-of-Law, PLAT, bar-exam QA, housing QA, or custom JSON |
| Source | User-selected public/custom corpora |
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
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Cross-run comparisons are invalid when configurations differ.
- It inherits every selected corpus's leakage, rights, and temporal-validity risks.

**Verified facts**
- Official paper/repository describe a configurable framework rather than a fixed benchmark.

**Inference**
- None recorded.

**Unresolved ambiguity**
- None recorded.

Original source bullet(s): #19

[Back to page index](#on-this-page)

<a id="prinzbench"></a>
## prinzbench

`prinzbench` · **private-benchmark** · **related artifact** · private

Answer obscure US legal-research and general information-search questions.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Single-author human pass/fail attempts to measure research usefulness, but withheld items and non-blind grading prevent independent construct validation. |
| Jurisdiction | United States |
| Languages | English |
| Size | 33 withheld questions: 25 legal research and 8 search; three runs each (99 evaluations) |
| Splits | Private question set |
| Source | Author-created withheld questions |
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
| Hugging Face | None |
| Paper / arXiv | None |
| Leaderboard / competition | [https://github.com/prinz-ai/prinzbench](https://github.com/prinz-ai/prinzbench) |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Hidden questions reduce contamination but also block auditability and independent scoring.
- Single-author non-blind judgments may reflect unmeasured preferences.

**Verified facts**
- Public repository describes 33 private questions and 99 runs.

**Inference**
- None recorded.

**Unresolved ambiguity**
- Question contents, rubric detail, and license are unavailable.

Original source bullet(s): #21

[Back to page index](#on-this-page)

<a id="open-legal-answer-benchmark"></a>
## Open Legal-Answer Benchmark

`open-legal-answer-benchmark` · **benchmark** · **check before use** · active

Produce current US legal answers with relevant, supported, and correctly ranged citations.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Checklist and citation metrics separate substantive required points, forbidden claims, authority retrieval, and citation entailment/range instead of collapsing answer quality into one judge score. |
| Jurisdiction | United States |
| Languages | English |
| Size | 54 base questions (29 hard, 25 controls) plus 8 adversarial variants; 62 JSONL rows |
| Splits | Public versioned evaluation set |
| Source | Sponsor-authored current-law questions and cited authorities |
| Input | Legal question |
| Output | Answer with cited sources |
| Baselines / leaderboard context | Sponsor-maintained self-runs are recorded in the repository leaderboard. |
| Dataset access | Public |
| License | CC BY 4.0 data; MIT code |
| Gating | None |
| Maintenance | Active sponsor-maintained benchmark; versioning matters for current-law questions. |
| Reproducibility | Public data and scorer support reruns; browser/search availability and current sources can change outcomes. |

### Metrics

- **Must-include / must-not / authority retrieval:** Rule/checklist scoring of required propositions, prohibited errors, and retrieval of the right authority. **Primary.**
- **Citation support and in-range:** Check whether citations support the associated claim and point to the relevant passage; optional LLM judging is separate. Judge: Optional/configurable. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/Vaquill-AI/open-legal-answer-benchmark](https://github.com/Vaquill-AI/open-legal-answer-benchmark) |
| Hugging Face | None |
| Paper / arXiv | None |
| Leaderboard / competition | [https://github.com/Vaquill-AI/open-legal-answer-benchmark/blob/main/LEADERBOARD.md](https://github.com/Vaquill-AI/open-legal-answer-benchmark/blob/main/LEADERBOARD.md) |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Fully public questions permit direct optimization.
- Sponsor-run results are not an independent third-party audit.

**Verified facts**
- Official repository exposes the 62-row JSONL and leaderboard.

**Inference**
- None recorded.

**Unresolved ambiguity**
- Temporal legal changes can make older gold expectations stale.

Original source bullet(s): #22

[Back to page index](#on-this-page)

<a id="awesome-legal-nlp"></a>
## awesome-legal-nlp

`awesome-legal-nlp` · **resource-list** · **related artifact** · active

Discovery index for legal NLP datasets, models, papers, surveys, books, and events.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | No evaluation construct is defined; this is a curated bibliography/resource list, not an instrument for measuring model capability. |
| Jurisdiction | Global / mixed |
| Languages | Multiple |
| Size | No benchmark instances |
| Splits | None |
| Source | Community-curated links |
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
| Hugging Face | None |
| Paper / arXiv | None |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Treating a resource list as a benchmark confuses discovery coverage with measured capability.

**Verified facts**
- Repository contents are links and prose rather than instances, gold labels, or graders.

**Inference**
- None recorded.

**Unresolved ambiguity**
- None recorded.

Original source bullet(s): #7

[Back to page index](#on-this-page)
