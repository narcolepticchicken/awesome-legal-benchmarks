# Retrieval, RAG, and citation

<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->

Authority retrieval, exact-support retrieval, case similarity, citation grounding, and end-to-end legal RAG.

Snapshot: **2026-08-05** · 28 entries

[Back to README](../../README.md) · [Catalog index](../catalog.md) · [Selection guide](../selection-guide.md) · [Metric field guide](../metric-theory.md) · [Methodology](../methodology.md)

## On this page

- [Massive Legal Embedding Benchmark](#mleb)
- [LegalBench-RAG](#legalbench-rag)
- [Belgian Statutory Article Retrieval Dataset](#bsard)
- [LLeQA](#lleqa)
- [bLLeQA](#blleqa)
- [CLERC](#clerc)
- [RegLab Reasoning-Focused Legal Retrieval Benchmark](#reglab-reasoning-focused-retrieval)
- [LeCaRDv2](#lecardv2)
- [STARD](#stard)
- [Competition on Legal Information Extraction/Entailment](#coliee)
- [AILA 2019](#aila-2019)
- [GerDaLIR](#gerdalir)
- [TREC Legal Track](#trec-legal-track)
- [Legal RAG Bench](#legal-rag-bench)
- [CanLegalRAGBench](#canlegalragbench)
- [JuriFindIT](#jurifindit)
- [ILSIC](#ilsic)
- [RoD-TAL](#rod-tal)
- [Vaquill Open Legal-Answer Benchmark](#open-legal-answer-benchmark)
- [LegalCiteBench](#legalcitebench)
- [Legal Phantom Citation](#legal-phantom-citation)
- [Large Legal Fictions](#reglab-legal-hallucinations)
- [Hallucination-Free? Legal Research Tool Study](#reglab-legal-rag-hallucinations)
- [Vals Legal Research Benchmark](#vals-legal-research-bench)
- [Vals CaseLaw v2](#vals-caselaw-v2)
- [LaborBench](#laborbench)
- [LexRAG](#lexrag)
- [MUSER](#muser)

<a id="mleb"></a>
## Massive Legal Embedding Benchmark

`mleb` · **benchmark-suite** · **specialist** · active

Legal embedding quality across retrieval, retrieval-augmented QA, and zero-shot classification tasks.

**Also known as:** MLEB

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Isaacus (company; commercial interest) |
| Catalog geography | Multi-jurisdiction and supranational |
| First recorded public event | [2025-10-22](https://arxiv.org/abs/2510.19365) — arXiv v1 submission |
| Latest verified event | [2026-02-24](https://github.com/isaacus-dev/mleb) — GitHub repository push |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Select embedding models for legal search on nDCG@10 across ten retrieval, QA, and classification datasets in six English-speaking jurisdictions.
- Regression-gate embedding upgrades in a legal RAG stack before swapping models.
- Research comparison of legal-domain versus general-purpose embeddings.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | MTEB-compatible task configurations treat rank quality—usually nDCG@10—as the main proxy for useful legal representations, supplemented by QA and classification task scores. |
| Jurisdiction | United States, United Kingdom, European Union, Australia, Ireland, Singapore |
| Languages | English |
| Size | 10 constituent datasets |
| Splits | Dataset-specific MTEB evaluation splits |
| Source material | Public legal retrieval, QA, and classification datasets assembled by Isaacus |
| Input | Queries and candidate texts or labeled examples |
| Output | Ranked candidates, answers, or zero-shot labels |
| Baselines / leaderboard context | Public result files and an Isaacus-hosted leaderboard compare general and legal embedding models. |
| Dataset access | Public constituent datasets |
| License | MIT code; constituent dataset licenses vary |
| Gating | Dataset-specific |
| Maintenance | Active vendor-maintained suite; pin task configs and result commit. |
| Reproducibility | Evaluator is public and MTEB-compatible; API embeddings and changing hosted model aliases can still move scores. |

### Metrics

- **nDCG@10:** Discounted graded gain at rank 10, normalized by the ideal ranking; constituent tasks may add QA/classification metrics. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/isaacus-dev/mleb](https://github.com/isaacus-dev/mleb) |
| Hugging Face | [https://huggingface.co/isaacus/datasets](https://huggingface.co/isaacus/datasets) |
| Paper / arXiv | [https://arxiv.org/abs/2510.19365](https://arxiv.org/abs/2510.19365) |
| Leaderboard / competition | [https://isaacus.com/mleb](https://isaacus.com/mleb) |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- All public queries and labels permit benchmark-targeted optimization.
- Benchmark owner also sells a leading model, so independently reproduced results are preferable.

**Verified facts**
- Both source README bullets resolve to the same GitHub repository and benchmark identity.

**Unresolved ambiguity**
- The original awesome-list Kanon/MLEB URL could not be verified as canonical.

**Related entries**

- [Legal RAG Bench](retrieval-rag-citation.md#legal-rag-bench)
- [GerDaLIR](retrieval-rag-citation.md#gerdalir)

Original source bullet(s): #3, #20

[Back to page index](#on-this-page)

<a id="legalbench-rag"></a>
## LegalBench-RAG

`legalbench-rag` · **benchmark** · **recommended** · fixed-release

Retrieve exact supporting spans from long legal and policy documents.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | ZeroEntropy (company; commercial interest) |
| Catalog geography | United States |
| First recorded public event | [2024-08-19](https://arxiv.org/abs/2408.10343) — arXiv v1 submission |
| Latest verified event | [2025-05-30](https://github.com/zeroentropy-ai/legalbenchrag) — GitHub repository push |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test whether retrieval returns the exact supporting spans, scored by character-level precision and recall, rather than whole documents.
- Compare chunking and retrieval configurations at fixed context budgets in a legal RAG product.
- Regression-test the retrieval component in isolation from answer generation.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Character-level precision and recall directly measure whether retrieved text covers gold support while limiting extra context; this isolates retrieval from answer generation. |
| Jurisdiction | United States, mixed contracts and policies |
| Languages | English |
| Size | 714 documents, more than 79M characters; 6,858 queries in abstract versus 6,889 in a paper table |
| Splits | Public fixed evaluation release |
| Source material | Four public contract/policy datasets |
| Input | Query plus document corpus |
| Output | Document identifier and character start/end spans |
| Baselines / leaderboard context | Paper evaluates retrieval systems at several context budgets. |
| Dataset access | Public repository/external bundle |
| License | MIT code; constituent source licenses vary |
| Gating | None observed |
| Maintenance | Fixed public release. |
| Reproducibility | High for retrieval when the exact commit, corpus, character normalization, and context budget are pinned. |

### Metrics

- **Character precision and recall:** Overlap between predicted and reference character sets, exposing both missed support and context bloat. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/zeroentropy-ai/legalbenchrag](https://github.com/zeroentropy-ai/legalbenchrag) |
| Hugging Face | None located |
| Paper / arXiv | [https://arxiv.org/abs/2408.10343](https://arxiv.org/abs/2408.10343) |
| Leaderboard / competition | None located |
| Project | [https://www.dropbox.com/scl/fo/r7xfa5i3hdsbxex1w6amw/AID389Olvtm-ZLTKAPrw6k4?rlkey=5n8zrbk4c08lbit3iiexofmwg&st=0hu354cq&dl=0](https://www.dropbox.com/scl/fo/r7xfa5i3hdsbxex1w6amw/AID389Olvtm-ZLTKAPrw6k4?rlkey=5n8zrbk4c08lbit3iiexofmwg&st=0hu354cq&dl=0) |

### Validity and evidence

**Risks / caveats**
- No hidden split; queries, corpus, and spans are public.
- The paper's query counts conflict and should never be silently harmonized.

**Verified facts**
- Official repository and paper define exact-span evaluation.

**Unresolved ambiguity**
- 6,858 versus 6,889 query count remains unresolved.

**Related entries**

- [LaborBench](retrieval-rag-citation.md#laborbench)

Original source bullet(s): #9

[Back to page index](#on-this-page)

<a id="bsard"></a>
## Belgian Statutory Article Retrieval Dataset

`bsard` · **benchmark** · **recommended** · fixed-release

Retrieve Belgian statutory articles relevant to a legal question.

**Also known as:** BSARD

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Maastricht Law & Tech Lab (academic) |
| Catalog geography | Belgium |
| First recorded public event | [2021-08-26](https://arxiv.org/abs/2108.11792) — arXiv v1 submission |
| Latest verified event | [2024-05-31](https://huggingface.co/datasets/maastrichtlawtech/bsard) — Hugging Face dataset update |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare retrievers on matching French-language legal questions to Belgian statutory articles.
- Test recall@k of required provisions before answer generation in a statutory QA pipeline.
- Research baseline for non-English statutory retrieval.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Recall@k tests whether needed authority appears in the candidate set; MRR/MAP reward placing one or all relevant provisions early. |
| Jurisdiction | Belgium |
| Languages | French |
| Size | 1,108 legal questions and 22,633 statutory articles |
| Splits | Official benchmark splits/files |
| Source material | Questions from Belgian legal practitioners and Belgian legislation |
| Input | Natural-language legal question plus statutory corpus |
| Output | Ranked statutory articles |
| Baselines / leaderboard context | Official paper reports sparse, dense, and cross-encoder systems; best reported Recall@100 was 74.8% in the paper setting. |
| Dataset access | Public |
| License | CC BY-NC-SA 4.0 |
| Gating | None observed |
| Maintenance | Stable Maastricht Law & Tech release. |
| Reproducibility | High for retrieval with frozen corpus, tokenizer, and cutoff. |

### Metrics

- **Recall@k:** Fraction of gold relevant articles retrieved by cutoff k. **Primary.**
- **MAP / MRR:** MAP averages precision at all relevant ranks; MRR uses reciprocal rank of the first relevant article.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/maastrichtlawtech/bsard](https://github.com/maastrichtlawtech/bsard) |
| Hugging Face | [https://huggingface.co/datasets/maastrichtlawtech/bsard](https://huggingface.co/datasets/maastrichtlawtech/bsard) |
| Paper / arXiv | [https://arxiv.org/abs/2108.11792](https://arxiv.org/abs/2108.11792)<br>[https://aclanthology.org/2022.acl-long.468/](https://aclanthology.org/2022.acl-long.468/) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- Static statutes can become temporally stale.
- Incomplete relevance judgments can mark alternative valid authorities as false positives.

**Verified facts**
- Official GitHub/HF/paper establish 1,108 questions and 22,633 articles.

[Back to page index](#on-this-page)

<a id="lleqa"></a>
## LLeQA

`lleqa` · **benchmark** · **specialist** · fixed-release

Retrieve Belgian legal authorities and generate long-form answers to practitioner-style questions.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Maastricht Law & Tech Lab (academic) |
| Catalog geography | Belgium |
| First recorded public event | [2023-09-29](https://arxiv.org/abs/2309.17050) — arXiv v1 submission |
| Latest verified event | [2024-09-03](https://huggingface.co/datasets/maastrichtlawtech/lleqa) — Hugging Face dataset update |
| Access level | gated |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test retrieve-then-answer pipelines on Belgian practitioner questions with expert reference answers.
- Diagnose whether failures come from authority retrieval or answer synthesis.
- Research long-form legal question answering in French.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | The benchmark joins retrieval coverage with answer similarity/grounding, allowing diagnosis of whether failure came from authority retrieval or answer synthesis. |
| Jurisdiction | Belgium |
| Languages | French |
| Size | 1,868 questions with expert answers/references and 27,941 legal articles |
| Splits | Official release; access is gated by data agreement |
| Source material | Belgian legal questions, detailed answers, and statutory materials |
| Input | Legal question plus searchable corpus |
| Output | Ranked authorities and long-form answer |
| Baselines / leaderboard context | Official paper compares retrieval, reranking, and generative QA pipelines. |
| Dataset access | Gated |
| License | Access under project data agreement |
| Gating | HF access request/agreement required |
| Maintenance | Stable research release. |
| Reproducibility | Good after approved access; exact corpus snapshot and generation protocol remain necessary. |

### Metrics

- **Recall@k / MRR:** Retrieval coverage and first-relevant rank. **Primary.**
- **ROUGE / METEOR / BERTScore:** Reference-overlap and semantic-similarity metrics for generated answers; human/grounding checks should accompany them.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/maastrichtlawtech/lleqa](https://github.com/maastrichtlawtech/lleqa) |
| Hugging Face | [https://huggingface.co/datasets/maastrichtlawtech/lleqa](https://huggingface.co/datasets/maastrichtlawtech/lleqa) |
| Paper / arXiv | [https://arxiv.org/abs/2309.17050](https://arxiv.org/abs/2309.17050) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- Reference overlap under-rewards legally equivalent answers and can reward unsupported paraphrase.
- Gating limits frictionless independent reruns.

**Verified facts**
- Official GitHub/HF/paper establish the dataset and gated access.

**Related entries**

- [bLLeQA](retrieval-rag-citation.md#blleqa)

[Back to page index](#on-this-page)

<a id="blleqa"></a>
## bLLeQA

`blleqa` · **benchmark-suite** · **specialist** · active

Retrieve Belgian statutory support and answer grounded legal questions in French and Dutch, including refusal when evidence is insufficient.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | University of Antwerp bLLeQA authors (academic) |
| Catalog geography | Belgium |
| First recorded public event | [2025-08-20](https://huggingface.co/datasets/clips/bLLeQA) — Hugging Face dataset creation |
| Latest verified event | [2026-07-03](https://aclanthology.org/2026.knowfm-1.4.pdf) — KnowFM 2026 publication date |
| Access level | gated |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Evaluate French and Dutch legal RAG on aligned Belgian questions, answers, and supporting statutes.
- Measure retrieval, citation extraction, refusal when evidence is incomplete, and generation quality as separate stages.
- Study translation-derived Dutch performance while comparing it with the original French material.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | A bilingual parallel extension of LLeQA decomposes end-to-end RAG into retrieval, citation, refusal, faithfulness, and answer-quality components. |
| Jurisdiction | Belgium, France and Netherlands source alignment described by the release |
| Languages | French, Dutch |
| Size | 25,982 statutory articles and 1,461 aligned questions |
| Splits | 1,125 train, 181 validation, and 155 test questions |
| Source material | LLeQA-derived French legal QA and supporting articles; Dutch parallel data generated with GPT-5 |
| Input | Legal question plus retrieved or gold statutory context |
| Output | Answer with cited statutory article IDs or refusal |
| Baselines / leaderboard context | KnowFM paper compares open and proprietary systems across retrieval, citation extraction, refusal, and generation. |
| Dataset access | Manually gated Hugging Face release |
| License | CC BY-NC-SA 4.0 data; MIT code |
| Gating | Data-use request required; academic/noncommercial terms stated in the gate |
| Maintenance | Active July 2026 release. |
| Reproducibility | Good after access approval; exact retrieval context, judge model, and language configuration must be pinned. |

### Metrics

- **Retrieval and citation metrics:** Evaluate relevant-article retrieval and extracted citation IDs at named cutoffs with public utilities. **Primary.**
- **Refusal and generation quality:** Score refusal when support is incomplete plus correctness and RAGAS faithfulness; pin model judge and context setup. Judge: Repository supports DeepEval correctness and RAGAS faithfulness; default faithfulness judge Gemini 3 Flash. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/nikolay-banar/blleqa](https://github.com/nikolay-banar/blleqa) |
| Hugging Face | [https://huggingface.co/datasets/clips/bLLeQA](https://huggingface.co/datasets/clips/bLLeQA) |
| Paper / arXiv | [https://aclanthology.org/2026.knowfm-1.4.pdf](https://aclanthology.org/2026.knowfm-1.4.pdf) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- Dutch questions were generated from French with GPT-5 and can contain translation/model artifacts.
- Model-based correctness and faithfulness scores inherit judge error.
- Gating and noncommercial terms limit independent product evaluation.

**Verified facts**
- The official repository, gated Hugging Face card, and KnowFM paper establish 1,461 questions, the 1,125/181/155 split, and bilingual RAG tasks.

**Unresolved ambiguity**
- The paper and code use several generation/judge configurations; every result needs the exact setup rather than a bare overall score.

**Related entries**

- [LLeQA](retrieval-rag-citation.md#lleqa)

[Back to page index](#on-this-page)

<a id="clerc"></a>
## CLERC

`clerc` · **benchmark** · **specialist** · fixed-release

Retrieve US case-law evidence and generate citation-grounded legal text.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Johns Hopkins CLSP (academic) |
| Catalog geography | United States |
| First recorded public event | [2024-06-24](https://arxiv.org/abs/2406.17186) — arXiv v1 submission |
| Latest verified event | [2025-01-28](https://github.com/bohanhou14/CLERC) — GitHub repository push |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test large-corpus retrieval of cited US case-law support at deep cutoffs such as Recall@1000.
- Test citation-grounded generation and measure hallucinated-citation rates in case-law drafting.
- Research citation-conditioned retrieval and generation at realistic corpus scale.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Large-corpus recall measures whether cited support is retrieved; generation metrics and citation/hallucination analysis assess whether answers use that evidence faithfully. |
| Jurisdiction | United States |
| Languages | English |
| Size | Large US case-law corpus with citation-linked retrieval and generation examples |
| Splits | Official dataset configurations |
| Source material | Public US judicial opinions and citations |
| Input | Case context/query plus candidate opinions |
| Output | Ranked cases and generated continuation/answer with citations |
| Baselines / leaderboard context | Paper reports sparse/dense retrieval and RAG generation systems. |
| Dataset access | Public |
| License | See official dataset card/repository; source case-law terms apply |
| Gating | None observed |
| Maintenance | Research release from JHU CLSP. |
| Reproducibility | Substantial corpus size makes exact index, snapshot, and retrieval settings essential. |

### Metrics

- **Recall@k (including Recall@1000):** Share of gold cited/relevant cases present by cutoff; paper reports a 48.3% zero-shot Recall@1000 result for a leading setting. **Primary.**
- **ROUGE and citation/hallucination metrics:** Generation overlap plus whether generated citations/support are valid under the paper protocol.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/bohanhou14/CLERC](https://github.com/bohanhou14/CLERC) |
| Hugging Face | [https://huggingface.co/datasets/jhu-clsp/CLERC](https://huggingface.co/datasets/jhu-clsp/CLERC) |
| Paper / arXiv | [https://arxiv.org/abs/2406.17186](https://arxiv.org/abs/2406.17186) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- Citation links are not identical to relevance and may encode court-writing conventions.
- Public opinions and citation graph can appear in pretraining.

**Verified facts**
- Official JHU repository/HF/paper define retrieval and generation tasks.

**Unresolved ambiguity**
- Dataset scale is configuration-dependent; cite the exact config rather than one loose total.

[Back to page index](#on-this-page)

<a id="reglab-reasoning-focused-retrieval"></a>
## RegLab Reasoning-Focused Legal Retrieval Benchmark

`reglab-reasoning-focused-retrieval` · **benchmark-suite** · **recommended** · fixed-release

Retrieve controlling text for legal questions whose answer has low lexical overlap with the relevant source.

**Also known as:** Reasoning-Focused Legal Retrieval Benchmark, RegLab Legal RAG Benchmarks

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Stanford RegLab (academic) |
| Catalog geography | United States |
| First recorded public event | [2025-05-06](https://arxiv.org/abs/2505.03970) — arXiv v1 submission |
| Latest verified event | None later verified |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare retrievers where the controlling text shares little vocabulary with the question, on bar-exam and housing-law QA over million-passage corpora.
- Test whether retrieved authority actually improves downstream answer accuracy.
- Shortlist retrieval components intended for reasoning-heavy legal queries.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | The suite intentionally stresses semantic/legal reasoning in retrieval; Recall@k/MRR measure evidence ranking and downstream QA accuracy tests whether the retrieved authority is usable. |
| Jurisdiction | United States |
| Languages | English |
| Size | BarExam QA: 1,195 historical plus 1,815 Barbri questions over about 856,835 passages; Housing QA: 6,853 queries over about 1,837,403 passages |
| Splits | Dataset-specific evaluation sets |
| Source material | Bar exam questions and US housing-law questions paired with large legal corpora |
| Input | Legal question plus passage corpus |
| Output | Ranked passages and optionally answer choice/text |
| Baselines / leaderboard context | Paper compares lexical, general dense, and legal-domain retrievers plus downstream QA. |
| Dataset access | Public HF datasets/collection |
| License | Dataset-specific |
| Gating | None observed |
| Maintenance | Fixed RegLab release/project site. |
| Reproducibility | Good with exact corpus/passages and task split; no canonical GitHub code repository was located. |

### Metrics

- **Recall@k / MRR@10:** Evidence coverage by cutoff and reciprocal rank of first relevant passage. **Primary.**
- **Downstream QA accuracy:** Answer correctness when the retriever's evidence is supplied to the QA model.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | None located |
| Hugging Face | [https://huggingface.co/collections/reglab/a-reasoning-focused-legal-retrieval-benchmark-67a00c363f7e0d14619e95c5](https://huggingface.co/collections/reglab/a-reasoning-focused-legal-retrieval-benchmark-67a00c363f7e0d14619e95c5)<br>[https://huggingface.co/datasets/reglab/barexam_qa](https://huggingface.co/datasets/reglab/barexam_qa)<br>[https://huggingface.co/datasets/reglab/housing_qa](https://huggingface.co/datasets/reglab/housing_qa) |
| Paper / arXiv | [https://arxiv.org/abs/2505.03970](https://arxiv.org/abs/2505.03970) |
| Leaderboard / competition | None located |
| Project | [https://reglab.github.io/legal-rag-benchmarks/](https://reglab.github.io/legal-rag-benchmarks/) |

### Validity and evidence

**Risks / caveats**
- Bar exam questions and source law are public and contamination-prone.
- Lexical-overlap filtering may select an artificial difficulty distribution.

**Verified facts**
- Official RegLab project/paper/HF collection define both datasets and retrieval metrics.

**Unresolved ambiguity**
- No canonical GitHub URL was found.

**Related entries**

- [LaborBench](retrieval-rag-citation.md#laborbench)

[Back to page index](#on-this-page)

<a id="lecardv2"></a>
## LeCaRDv2

`lecardv2` · **benchmark** · **recommended** · fixed-release

Retrieve legally similar Chinese criminal cases using graded relevance across characterization, penalty, and procedure.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | THUIR (academic) |
| Catalog geography | China |
| First recorded public event | [2023-10-26](https://arxiv.org/abs/2310.17609) — arXiv v1 submission |
| Latest verified event | [2024-12-29](https://github.com/THUIR/LeCaRDv2) — GitHub repository push |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare case-similarity retrieval on Chinese criminal cases with expert relevance graded across characterization, penalty, and procedure.
- Test first-stage recall at large cutoffs (100 to 1,000) before reranking.
- Research baseline for case similarity beyond lexical overlap.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Expert multi-aspect relevance separates factual/legal similarity from mere lexical overlap; recall at large k tests first-stage retrieval and nDCG/precision support reranking analysis. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | 800 query cases, 55,192 judged candidates sampled from 4.3M criminal cases |
| Splits | 640 train / 160 test queries for the reported fine-tuning setup |
| Source material | Chinese criminal judgments with expert graded relevance |
| Input | Query case and candidate case corpus |
| Output | Ranked similar cases |
| Baselines / leaderboard context | Official paper/repository compare sparse, dense, and legal-pretrained retrieval/reranking methods. |
| Dataset access | Public official repository |
| License | See repository/data terms |
| Gating | None observed |
| Maintenance | Fixed academic release. |
| Reproducibility | Good with the official candidate pool and qrels; full 4.3M source corpus handling may vary. |

### Metrics

- **Recall@100/200/500/1000:** Coverage of judged relevant cases at first-stage retrieval cutoffs. **Primary.**
- **nDCG / precision at k:** Graded ranking quality and top-result relevance for reranking settings.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/THUIR/LeCaRDv2](https://github.com/THUIR/LeCaRDv2) |
| Hugging Face | None located |
| Paper / arXiv | [https://arxiv.org/abs/2310.17609](https://arxiv.org/abs/2310.17609) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- Judged candidate pooling can miss relevant cases outside the pool.
- Chronological and court-source shortcuts may inflate similarity.

**Verified facts**
- Official repository/paper establish 800 queries, 55,192 candidates, and 4.3M source cases.

**Related entries**

- [STARD](retrieval-rag-citation.md#stard)
- [GerDaLIR](retrieval-rag-citation.md#gerdalir)

[Back to page index](#on-this-page)

<a id="stard"></a>
## STARD

`stard` · **benchmark** · **specialist** · fixed-release

Retrieve all Chinese statutory articles relevant to an informal real-world legal consultation query.

**Also known as:** STAtute Retrieval Dataset

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | STARD authors / Tsinghua University (academic) |
| Catalog geography | China |
| First recorded public event | [2024-03-17](https://github.com/oneal2000/STARD) — GitHub repository creation |
| Latest verified event | [2025-04-24](https://github.com/oneal2000/STARD) — Last verified GitHub repository push affecting the benchmark artifact |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Benchmark Chinese statute retrieval for informal questions from non-lawyers against a 55,348-article corpus.
- Compare lexical, dense, legal-domain, and task-fine-tuned retrievers with recall and reciprocal-rank curves.
- Use the released annotation design as a template for building jurisdiction-specific lay-query retrieval tests.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Recall at several cutoffs measures whether a retriever finds the full set of annotated statutes, while reciprocal rank measures how early the first relevant statute appears; the labels operationalize legal relevance through a three-step lawyer annotation process. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | 1,543 anonymized consultation queries, 55,348 candidate statutory articles, 1,445 unique relevant articles, and 2,717 relevance occurrences |
| Splits | The repository provides query/corpus files and a random 4:1 train/development partition; the paper evaluates supervised retrievers with five-fold cross-validation |
| Source material | Questions derived from the official 12348 China Legal Service website; current national laws, regulations, and judicial interpretations downloaded by the legal team |
| Input | Informal Chinese legal question and a corpus of article-level statutes |
| Output | Ranked statutory-article identifiers |
| Baselines / leaderboard context | The paper compares QL, BM25, Chinese RoBERTa, SEED, coCondenser, SAILER, Lawformer, Dense-CAIL, Dense-GPT4, LSI-STARD, and five-fold Dense-STARD; Dense-STARD reports the best Recall@100 at 0.9065. |
| Dataset access | Public GitHub data and code with public qrels |
| License | MIT according to the paper and repository |
| Gating | None observed |
| Maintenance | The repository remains public but has no tagged benchmark releases; pin a commit and legal-source snapshot. |
| Reproducibility | High for the published retrieval experiment because queries, corpus, labels, splits, and code are public; exact reproduction still requires the pinned preprocessing and model checkpoints. |

### Metrics

- **Recall@5/10/20/30/50/100/200:** For each query, measure the fraction of annotated relevant statutory articles appearing in the top-k ranking; aggregate across queries. **Primary.**
- **MRR@3/5/10:** Average the reciprocal rank of the first relevant statutory article, truncated at the named cutoff. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/oneal2000/STARD](https://github.com/oneal2000/STARD) |
| Hugging Face | None located |
| Paper / arXiv | [https://arxiv.org/abs/2406.15313](https://arxiv.org/abs/2406.15313) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- All queries and qrels are public, so direct contamination and benchmark-specific tuning are easy.
- The statutory corpus is time-sensitive and can become legally stale even if retrieval scores remain reproducible.
- Cohen's kappa of 0.5312 indicates only moderate pre-filter annotation agreement, and disagreement cases were excluded from the final set.
- Citation-derived or consultation-derived relevance does not prove that the retrieved set is legally complete for every valid interpretation.

**Verified facts**
- The official paper and repository agree on 1,543 queries, 55,348 candidate articles, the annotation process, retrieval metrics, baseline family, public artifacts, and MIT terms.
- Official GitHub API metadata records repository creation on 2024-03-17 and the last benchmark push on 2025-04-24.

**Inference**
- STARD is best treated as a specialist retrieval benchmark, not as evidence of end-to-end legal-advice quality.

**Unresolved ambiguity**
- No canonical Hugging Face dataset or maintained leaderboard was located.

**Related entries**

- [LeCaRDv2](retrieval-rag-citation.md#lecardv2)
- [JuDGE](reasoning-education.md#judge)
- [LawBench](reasoning-education.md#lawbench)

[Back to page index](#on-this-page)

<a id="coliee"></a>
## Competition on Legal Information Extraction/Entailment

`coliee` · **shared-task** · **recommended** · annual

Retrieve and recognize entailment among Canadian cases and Japanese civil-code provisions.

**Also known as:** COLIEE

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | COLIEE organizers (competition) |
| Catalog geography | Multi-jurisdiction and supranational |
| First recorded public event | [2014](https://coliee.org/COLIEE2025/overview) — Official COLIEE history; COLIEE 2025 is identified as the 12th competition |
| Latest verified event | [2026-06](https://coliee.org/COLIEE2026/program) — COLIEE 2026 workshop program |
| Access level | gated |
| Test labels | hidden |
| Independently runnable | partial |

### Possible use cases

- Enter or replicate a pinned annual edition to compare case and statute retrieval and entailment systems against official hidden-test results.
- Compare retrieval systems on Canadian case-law and Japanese civil-code tasks within one edition.
- Research comparison where competition-held labels reduce direct leakage.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Four annual tasks separate first-stage authority retrieval from textual entailment; official hidden tests reduce direct leakage, while task-specific precision/recall/F1 and accuracy measure different stages. |
| Jurisdiction | Canada, Japan |
| Languages | English, Japanese |
| Size | Annual task packages; counts change by year |
| Splits | Released training data plus competition-held test labels |
| Source material | Canadian case law and Japanese civil-code/bar-exam materials |
| Input | Query case or legal question with candidate cases/statutes |
| Output | Relevant authorities and entailment/yes-no decisions |
| Baselines / leaderboard context | Annual proceedings and official results compare participating systems. |
| Dataset access | Competition registration/package |
| License | Year/task-specific terms |
| Gating | Registration may be required |
| Maintenance | Annual competition; never mix editions without naming the year. |
| Reproducibility | Strong within an edition if official data/scripts are retained; no single canonical GitHub or HF release spans years. |

### Metrics

- **Precision / recall / F1:** Official task scripts score retrieved cases/statutes and entailment selections; exact primary metric varies by task/year. **Primary.**
- **Accuracy:** Used for binary statutory entailment/answer tasks where specified by the year's rules.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | None located |
| Hugging Face | None located |
| Paper / arXiv | None located |
| Leaderboard / competition | [https://coliee.org/COLIEE2025/submission](https://coliee.org/COLIEE2025/submission) |
| Project | [https://coliee.org/COLIEE2025/overview](https://coliee.org/COLIEE2025/overview) |

### Validity and evidence

**Risks / caveats**
- Task definitions, corpora, and metrics change between annual editions.
- Competition access terms and later link rot can limit retrospective reproduction.

**Verified facts**
- Official COLIEE 2025 site defines four tasks and competition access.

**Unresolved ambiguity**
- There is intentionally no single edition-independent dataset size or metric.

**Related entries**

- [AILA 2019](retrieval-rag-citation.md#aila-2019)
- [GerDaLIR](retrieval-rag-citation.md#gerdalir)

[Back to page index](#on-this-page)

<a id="aila-2019"></a>
## AILA 2019

`aila-2019` · **shared-task** · **specialist** · completed

Rank relevant Indian Supreme Court precedents and statutory sections for a factual legal scenario.

**Also known as:** FIRE 2019 Artificial Intelligence for Legal Assistance Track

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | FIRE 2019 AILA organizers (competition) |
| Catalog geography | India |
| First recorded public event | [2019](https://ceur-ws.org/Vol-2517/T1-1.pdf) — FIRE 2019 shared-task edition; exact first public data-release date was not located |
| Latest verified event | [2020-10-03](https://zenodo.org/records/4063986) — Zenodo dataset record modification |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Benchmark Indian Supreme Court precedent retrieval and Indian statute retrieval from anonymized factual scenarios.
- Compare modern retrievers with the original FIRE submissions using the same trec_eval measures.
- Use the explicit 10/40 query split as a small historical diagnostic, not as a comprehensive Indian-law score.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | MAP rewards repeated early precision across all known relevant authorities, while P@10, BPREF, and reciprocal rank separately expose top-ten concentration, robustness to incomplete judgments, and first-hit rank. |
| Jurisdiction | India |
| Languages | English |
| Size | 50 anonymized factual queries, 2,914 candidate Supreme Court case documents, and 197 candidate statutory sections |
| Splits | 10 training queries and 40 test queries with relevance judgments; all are now public |
| Source material | Indian Supreme Court judgments from 1952 through February 2018 and statutory material; queries were manually extracted and anonymized from case facts |
| Input | Natural-language factual scenario |
| Output | Ranked precedent identifiers for Task 1 or ranked statute identifiers for Task 2 |
| Baselines / leaderboard context | The official overview reports 22 Task 1 and 18 Task 2 runs using BM25, TF-IDF, language models, vector models, and embeddings; best MAP was 0.1492 for precedent retrieval and 0.1566 for statute retrieval. |
| Dataset access | Public Zenodo archive and GitHub pointer with queries, documents, and qrels |
| License | CC BY 4.0 in the Zenodo record; the overview paper is also CC BY 4.0 |
| Gating | None observed for the archived release |
| Maintenance | Completed 2019 shared task; the archived Zenodo record is stable, while later AILA editions are separate versioned competitions. |
| Reproducibility | Good for the archived 2019 task because the collection, qrels, metric definitions, trec_eval protocol, and official results are public. |

### Metrics

- **Mean Average Precision (primary):** Compute average precision per test query and average over the 40 queries using trec_eval; rank submitted runs by MAP. **Primary.**
- **P@10 / BPREF / reciprocal rank:** Report top-ten precision, binary preference under potentially incomplete qrels, and mean reciprocal rank of the first relevant item.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/Law-AI/aila-2019-dataset](https://github.com/Law-AI/aila-2019-dataset) |
| Hugging Face | None located |
| Paper / arXiv | [https://ceur-ws.org/Vol-2517/T1-1.pdf](https://ceur-ws.org/Vol-2517/T1-1.pdf) |
| Leaderboard / competition | None located |
| Project | [https://zenodo.org/records/4063986](https://zenodo.org/records/4063986)<br>[https://sites.google.com/view/fire-2019-aila/](https://sites.google.com/view/fire-2019-aila/) |

### Validity and evidence

**Risks / caveats**
- Only 40 test queries make the aggregate unstable and narrow relative to Indian legal practice.
- The overview warns that some genuinely relevant statutes or precedents may be absent from the judgments and therefore from the qrels.
- All data and qrels are public and old enough to appear in training corpora.
- Source collection through Westlaw India requires careful downstream provenance review even though the released archive is CC BY 4.0.

**Verified facts**
- The official FIRE overview, GitHub repository, and Zenodo record agree on the two tasks, 50 queries, 2,914 cases, 197 statutes, 10/40 split, metrics, and archived data identity.
- Zenodo reports publication on 2020-10-02, modification on 2020-10-03, and CC BY 4.0 metadata.

**Inference**
- AILA is best preserved as a completed shared-task identity rather than merged into the later IL-TUR suite that reuses related Indian tasks.

**Unresolved ambiguity**
- No Hugging Face release or continuously maintained leaderboard was located.

**Related entries**

- [ILSIC](retrieval-rag-citation.md#ilsic)
- [IL-TUR](reasoning-education.md#il-tur)
- [Competition on Legal Information Extraction/Entailment](retrieval-rag-citation.md#coliee)

[Back to page index](#on-this-page)

<a id="gerdalir"></a>
## GerDaLIR

`gerdalir` · **benchmark** · **specialist** · fixed-release

Retrieve German case decisions cited by a passage expressing a legal statement or line of argument.

**Also known as:** German Dataset for Legal Information Retrieval

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | LAVIS NLP / GerDaLIR authors (academic) |
| Catalog geography | Germany |
| First recorded public event | [2021-09-28](https://github.com/lavis-nlp/GerDaLIR) — GitHub repository creation |
| Latest verified event | [2024-02-26](https://github.com/lavis-nlp/GerDaLIR) — Last verified GitHub repository push affecting the benchmark artifact |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Benchmark full-ranking German case-law retrieval from passage-length legal arguments.
- Train and compare sparse, embedding, and neural reranking systems on a large fixed German legal collection.
- Diagnose citation-derived retrieval separately from expert-judged semantic relevance.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Top-rank quality is measured by MRR@10 and nDCG@20, while Recall@100/1000 measures corpus coverage; relevance is operationalized by parsed case citations rather than independent expert judgments. |
| Jurisdiction | Germany |
| Languages | German |
| Size | 122,975 query passages, 131,446 collection case documents represented by 3,095,383 passages, and 144,324 positive labels |
| Splits | 98,380 train / 12,297 development / 12,298 test queries; 115,360 / 14,570 / 14,394 positive labels |
| Source material | 201,825 German case documents from Open Legal Data; passages citing known collection cases become queries |
| Input | German case-law passage with citations sanitized to a [REF] token |
| Output | Ranked collection case or passage identifiers |
| Baselines / leaderboard context | The paper compares TF-IDF, default and tuned BM25, GloVe/fastText word-centroid similarity, and BERT/ELECTRA reranking; ELECTRA reports the best MRR@10 at 0.436 and nDCG@20 at 0.481, while tuned document-level BM25 reaches Recall@1000 of 0.829. |
| Dataset access | Public compressed TSV downloads linked from GitHub, including collection, train/dev/test queries, qrels, and optional BM25 candidates |
| License | MIT repository license; verify Open Legal Data source terms for downstream redistribution |
| Gating | None observed, but the multi-gigabyte download and external host must remain available |
| Maintenance | Fixed research release with nine repository commits; pin the February 2024 artifact revision and external download checksums. |
| Reproducibility | High for fixed retrieval experiments because exact splits, qrels, download formats, baselines, and metric cutoffs are public. |

### Metrics

- **MRR@10 / nDCG@20:** Measure first-hit rank through position 10 and graded top-20 ranking quality over all positive citation labels. **Primary.**
- **Recall@100 / Recall@1000:** Measure the fraction of known cited cases retrieved within broad candidate cutoffs. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/lavis-nlp/GerDaLIR](https://github.com/lavis-nlp/GerDaLIR) |
| Hugging Face | None located |
| Paper / arXiv | [https://aclanthology.org/2021.nllp-1.13/](https://aclanthology.org/2021.nllp-1.13/) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- A citation is a noisy proxy for relevance: courts cite cases for many purposes, and uncited but useful authorities become false negatives.
- Random query splitting can place closely related passages or matters across train and test and should be audited for document-family leakage.
- All qrels are public, permitting direct overfitting.
- External multi-gigabyte downloads are a durability risk even though the GitHub metadata remains available.

**Verified facts**
- The official ACL paper and repository agree on task identity, collection/query/label counts, the 80/10/10 split, metric cutoffs, public downloads, and baseline results.
- The GitHub API records repository creation on 2021-09-28, benchmark push on 2024-02-26, and an MIT license.

**Inference**
- GerDaLIR is strong for German full-ranking research but should not be interpreted as expert validation of substantive case similarity.

**Unresolved ambiguity**
- No canonical Hugging Face release or maintained leaderboard was located.

**Related entries**

- [Competition on Legal Information Extraction/Entailment](retrieval-rag-citation.md#coliee)
- [LeCaRDv2](retrieval-rag-citation.md#lecardv2)
- [Massive Legal Embedding Benchmark](retrieval-rag-citation.md#mleb)

[Back to page index](#on-this-page)

<a id="trec-legal-track"></a>
## TREC Legal Track

`trec-legal-track` · **shared-task** · **specialist** · archived

Find documents responsive to civil-litigation production requests while minimizing review burden.

**Also known as:** TREC Legal

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | NIST TREC Legal Track organizers (mixed) |
| Catalog geography | United States |
| First recorded public event | [2006](https://trec.nist.gov/data/legal06.html) — First official TREC Legal Track edition |
| Latest verified event | [2011](https://trec.nist.gov/data/legal11.html) — Final official TREC Legal Track edition |
| Access level | partial |
| Test labels | public |
| Independently runnable | partial |

### Possible use cases

- Reproduce historical United States e-discovery and technology-assisted review experiments with official topics and qrels.
- Compare ranking, recall-at-review-depth, and probability-calibration strategies on the 2010/2011 Enron collection.
- Use the annual protocols as methodological precedent when designing a fresh private document-review benchmark.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | The series operationalizes e-discovery retrieval through attorney-authored production requests, pooled or sampled responsiveness judgments, and review-effort tradeoffs; later learning tasks jointly evaluate ranking and estimated probabilities of responsiveness. |
| Jurisdiction | United States civil litigation / e-discovery |
| Languages | English |
| Size | Edition-specific; the 2011 learning task ranks 685,592 Enron messages and attachments for three production-request topics, with 16,999 sampled documents assessed for the gold standard |
| Splits | Annual topics, qrels, reference runs, and interactive or learning phases rather than one conventional train/dev/test split |
| Source material | 2006–2009 civil-discovery collections and 2010–2011 EDRM Enron Dataset v2, with attorney topic authorities and professional or legally trained assessors |
| Input | Production request and coding guidelines, document corpus, seed assessments, and optional bounded feedback from a topic authority |
| Output | Responsive-document set or full ranking with estimated probability of responsiveness |
| Baselines / leaderboard context | NIST publishes annual participant runs and result appendices. In 2011, ten organizations submitted automatic or technology-assisted systems, including learning-to-rank, relevance-feedback, search, and review workflows. |
| Dataset access | NIST still hosts annual topics, qrels, scripts, and results; source document collections are separate large archives and may be harder to obtain |
| License | No single benchmark-wide license covers NIST artifacts and the underlying tobacco/Enron corpora; source-corpus terms must be checked separately |
| Gating | Partial: metadata and judgments are public, but a complete rerun also requires the corresponding edition's source corpus |
| Maintenance | Archived official series: six editions ran from 2006 through 2011, and NIST continues to host the data and proceedings pages. |
| Reproducibility | Moderate for a pinned edition because qrels, scripts, papers, and results remain public; lower for end-to-end reruns when legacy corpus hosting, formats, or interactive feedback are unavailable. |

### Metrics

- **Recall / precision / F1 at review cutoffs:** Later editions estimate retrieval effectiveness at named production or review depths from stratified samples; report topic, cutoff, and confidence procedure. Judge: Human responsiveness assessments with topic-authority adjudication. **Primary.**
- **Probability-estimate accuracy:** Compare submitted estimates of responsive-document counts with sampled post-hoc estimates; the 2010/2011 learning tasks evaluate calibration as well as ranking. Judge: Human responsiveness assessments with topic-authority adjudication.
- **Edition-specific official measures:** Earlier ad hoc, relevance-feedback, batch, and interactive tasks use the evaluation scripts bundled with that year's qrels; never compare scores across editions without naming the task and script. Judge: Human relevance assessors.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | None located |
| Hugging Face | None located |
| Paper / arXiv | [https://trec.nist.gov/pubs/trec15/papers/LEGAL06.OVERVIEW.pdf](https://trec.nist.gov/pubs/trec15/papers/LEGAL06.OVERVIEW.pdf)<br>[https://trec.nist.gov/pubs/trec20/papers/LEGAL.OVERVIEW.2011.pdf](https://trec.nist.gov/pubs/trec20/papers/LEGAL.OVERVIEW.2011.pdf) |
| Leaderboard / competition | [https://trec.nist.gov/pubs/trec20/appendices/legal.html](https://trec.nist.gov/pubs/trec20/appendices/legal.html) |
| Project | [https://trec.nist.gov/data/legal.html](https://trec.nist.gov/data/legal.html) |

### Validity and evidence

**Risks / caveats**
- Pooling and stratified sampling leave unjudged documents and introduce estimator assumptions; qrels are not exhaustive truth.
- The final 2011 task has only three topics, so system ranks are sensitive to topic choice.
- Historical email and litigation collections may not represent current enterprise document formats or discovery practice.
- Cross-year scores are not directly comparable because corpora, tasks, feedback budgets, and evaluation methods changed.

**Verified facts**
- NIST's official landing page enumerates annual Legal Track editions from 2006 through 2011 and hosts their qrels, scripts, results, and proceedings.
- The official 2011 overview defines 685,592 documents, three topics, 16,999 assessed documents, full-corpus ranking/probability output, feedback budget, human adjudication, and recall/precision/F1 evaluation.

**Inference**
- TREC Legal remains methodologically important for e-discovery, but its archived scores should be used as historical baselines rather than current product ranks.

**Unresolved ambiguity**
- There is no canonical GitHub, Hugging Face dataset, arXiv record, or live leaderboard; source-corpus access varies by edition.

[Back to page index](#on-this-page)

<a id="legal-rag-bench"></a>
## Legal RAG Bench

`legal-rag-bench` · **benchmark** · **check before use** · active

Evaluate an end-to-end legal RAG pipeline and attribute errors to retrieval versus generation.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Isaacus / Umar Butler (mixed; commercial interest) |
| Catalog geography | Australia |
| First recorded public event | [2026-03-02](https://arxiv.org/abs/2603.01710) — arXiv v1 submission |
| Latest verified event | [2026-03-08](https://huggingface.co/datasets/isaacus/legal-rag-bench) — Hugging Face dataset update |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Attribute end-to-end RAG errors to retrieval versus generation using Isaacus's factorial retriever-by-generator design.
- Test correctness and groundedness on Victorian criminal-law questions against expert answers and supporting passages.
- Protocol reference for hierarchical error decomposition in a RAG product evaluation.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | A full factorial retriever×generator design plus hierarchical error decomposition tests whether gold support was retrieved, whether an answer is correct against expert reference, and whether its claims are grounded in supplied context. |
| Jurisdiction | Victoria, Australia / criminal law and procedure |
| Languages | English |
| Size | 4,876 passages and 100 expert-crafted questions |
| Splits | Public test corpus and QA files |
| Source material | Victorian Criminal Charge Book with human answers/supporting passages |
| Input | Question plus retrieved top-k passages |
| Output | Long-form answer and recorded retrieved context |
| Baselines / leaderboard context | Official code evaluates three embedders × two generators at k=5 (600 question-level iterations). |
| Dataset access | Public |
| License | CC BY-NC-SA 4.0 data; MIT code |
| Gating | Commercial embedding/generator/judge APIs may be required for the paper run |
| Maintenance | Active 2026 vendor research release. |
| Reproducibility | Code and data are public, but API nondeterminism, moving aliases, tuned prompts, and provider dependencies are explicitly acknowledged. |

### Metrics

- **Retrieval accuracy:** Whether the gold relevant passage appears in retrieved context at configured k (default k=5 in the released run). **Primary.**
- **Correctness / groundedness:** Binary LLM judgments against the human answer and provided context, reported per factorial cell. Judge: GPT-5.2 high-reasoning in released code. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/isaacus-dev/legal-rag-bench](https://github.com/isaacus-dev/legal-rag-bench) |
| Hugging Face | [https://huggingface.co/datasets/isaacus/legal-rag-bench](https://huggingface.co/datasets/isaacus/legal-rag-bench) |
| Paper / arXiv | [https://arxiv.org/abs/2603.01710](https://arxiv.org/abs/2603.01710) |
| Leaderboard / competition | None located |
| Project | [https://huggingface.co/blog/isaacus/legal-rag-bench](https://huggingface.co/blog/isaacus/legal-rag-bench) |

### Validity and evidence

**Risks / caveats**
- Benchmark owner sells one evaluated legal embedder and reports it as strongest.
- Only 100 questions from one source manual constrain generalization; the judge is a moving hosted model.

**Verified facts**
- Official GitHub/HF/paper define the corpus, factorial protocol, exact judge, and result fields.

**Related entries**

- [Massive Legal Embedding Benchmark](retrieval-rag-citation.md#mleb)

[Back to page index](#on-this-page)

<a id="canlegalragbench"></a>
## CanLegalRAGBench

`canlegalragbench` · **benchmark** · **specialist** · active

Retrieve Canadian case law for realistic layperson and legal-professional queries and generate grounded answers.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | UBC NLP (academic) |
| Catalog geography | Canada |
| First recorded public event | [2026-05-28](https://arxiv.org/abs/2605.30497) — arXiv v1 submission |
| Latest verified event | [2026-07-20](https://github.com/NLP-UBC/CanLegalRAGBench) — GitHub repository push |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare retrievers on Canadian case-law queries written from layperson and legal-professional personas.
- Test claim-level factuality and groundedness of generated answers against expert references and retrieved documents.
- Shortlist retrieval and generation components for Canadian legal research products.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Macro retrieval metrics score authority coverage/ranking; claim-level factuality compares generated atomic claims to expert answers and retrieved documents, separating answer agreement from grounding. |
| Jurisdiction | Canada, Ontario, British Columbia, Alberta, other Canadian provinces/federal courts |
| Languages | English, some French passages |
| Size | 532 queries, 3,193 gold query-document pairs, 588 unique gold documents; released corpus currently has 1,649 rows |
| Splits | One public comparative-evaluation release |
| Source material | Generated realistic queries filtered by an LLM, annotated by senior law students/paralegal, with Canadian case law and limited statutes |
| Input | Query plus Canadian legal corpus |
| Output | Ranked documents and long-form answer |
| Baselines / leaderboard context | Official code/paper evaluate BM25L, dense models, reranking, and iterative retrieval-generation, then three answer generators. |
| Dataset access | Public |
| License | MIT annotations/code; each source document retains its upstream license |
| Gating | None observed |
| Maintenance | Very recent active release; HF card still contains pre-publication 'coming soon' text. |
| Reproducibility | Code/data are public; private Caseway-derived distractors/source terms, API judges, and incomplete relevance pooling must be considered. |

### Metrics

- **Macro Recall@10 / nDCG@10:** Per-query recall and graded/binary ranking quality averaged equally across 532 queries; MRR and @25 variants are also reported. **Primary.**
- **Claim accuracy / groundedness:** Gemini-2.5-Pro decomposes answers into atomic claims and judges entailment against gold-answer claims or retrieved documents, FActScore-style. Judge: Gemini 2.5 Pro via Ragas-style pipeline. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/NLP-UBC/CanLegalRAGBench](https://github.com/NLP-UBC/CanLegalRAGBench) |
| Hugging Face | [https://huggingface.co/datasets/UBC-VL/CanLegalRAGBench](https://huggingface.co/datasets/UBC-VL/CanLegalRAGBench) |
| Paper / arXiv | [https://arxiv.org/abs/2605.30497](https://arxiv.org/abs/2605.30497) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- Expert rejudging found relevant documents outside the gold set, so automatic retrieval scores undercount some valid retrievals.
- Questions were model-generated and many source rows lack explicit upstream-license metadata.

**Verified facts**
- Official GitHub/HF/paper define 532 queries, 588 gold documents, metrics, and claim-level formulas.

**Unresolved ambiguity**
- The HF viewer shows 1,649 released corpus rows while the paper emphasizes 588 unique gold documents; these count different units.

[Back to page index](#on-this-page)

<a id="jurifindit"></a>
## JuriFindIT

`jurifindit` · **benchmark** · **specialist** · active

Retrieve Italian statutory articles relevant to natural-language legal questions.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | JuriFindIT authors (academic) |
| Catalog geography | Italy |
| First recorded public event | [2025-09-29](https://huggingface.co/datasets/jurifindit/JuriFindIT) — Hugging Face dataset creation |
| Latest verified event | [2026-03](https://aclanthology.org/2026.findings-eacl.221/) — Findings of EACL 2026 publication |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare Italian statutory retrievers on 895 expert-authored questions across four legal macro-areas.
- Train retrieval models on 169,301 synthetic questions, then evaluate only on the expert validation set.
- Test whether a legislative graph and cross-article references improve retrieval beyond dense similarity.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Expert question-to-article relevance judgments test the lexical and conceptual gap between ordinary questions and statute text; graph experiments test cross-article structure. |
| Jurisdiction | Italy, European Union materials within the corpus |
| Languages | Italian |
| Size | 23,458 articles from 159 documents; 895 expert questions; 169,301 synthetic questions; 20,608 cross-article references |
| Splits | Expert questions: train and validation; synthetic questions: train; statutory corpus: corpus split |
| Source material | National and European legislative acts in Akoma Ntoso; four legal professionals authored expert questions; Qwen3-32B generated synthetic questions |
| Input | Natural-language legal question plus statutory corpus |
| Output | Ranked statutory articles |
| Baselines / leaderboard context | The dataset card reports BM25, pretrained embeddings, and DAR-legal-it fine-tuned retrieval baselines. |
| Dataset access | Public Hugging Face release |
| License | CC BY-NC-SA 4.0 |
| Gating | None; Dataset Viewer is available |
| Maintenance | Active EACL 2026 release; no canonical GitHub repository was found. |
| Reproducibility | Strong for the published data and retrieval metrics when the corpus and model revisions are pinned. |

### Metrics

- **Recall, nDCG, MRR, and mAP at k:** Official validation results report Recall@5/20/60/100 plus nDCG, MRR, and mAP at named cutoffs; keep expert validation separate from synthetic training data. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | None located |
| Hugging Face | [https://huggingface.co/datasets/jurifindit/JuriFindIT](https://huggingface.co/datasets/jurifindit/JuriFindIT) |
| Paper / arXiv | [https://aclanthology.org/2026.findings-eacl.221/](https://aclanthology.org/2026.findings-eacl.221/) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- The 169,301 synthetic questions should not be mixed into the expert evaluation set.
- Static statutes can become stale, and public labels permit tuning.
- Noncommercial share-alike terms may not fit product evaluation workflows.

**Verified facts**
- The official Hugging Face card and ACL paper agree on 23,458 articles, 895 expert questions, 169,301 synthetic questions, and four macro-areas.

**Unresolved ambiguity**
- No canonical GitHub repository or official leaderboard was located.

[Back to page index](#on-this-page)

<a id="ilsic"></a>
## ILSIC

`ilsic` · **dataset** · **specialist** · active

Identify Indian statutes relevant to layperson and court-derived legal queries.

**Also known as:** Corpora for Identifying Indian Legal Statutes from Queries by Laypeople

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Law-AI / ILSIC authors (academic) |
| Catalog geography | India |
| First recorded public event | [2026-01-23](https://github.com/Law-AI/ilsic) — GitHub repository creation |
| Latest verified event | [2026-02-03](https://github.com/Law-AI/ilsic) — GitHub repository push |
| Access level | partial |
| Test labels | public |
| Independently runnable | partial |

### Possible use cases

- Study Indian statute identification from informal layperson questions rather than only court-written facts.
- Compare transfer from judgment queries to layperson queries across hundreds of statutes.
- Build a statute-routing evaluation after pinning the external data download, split, and scorer.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Parallel query populations test whether statute identification trained on formal court language transfers to informal questions from non-professionals. |
| Jurisdiction | India |
| Languages | English, Indian legal-query language |
| Size | ILSIC-Lay: 8,127 queries over 569 statutes; ILSIC-Multi: about 7,000 queries over 399 statutes |
| Splits | Paper-defined lay and court-query corpora; exact public split files require the external download |
| Source material | KaKanoon, legal forums, and court judgments |
| Input | Layperson or court-derived legal query |
| Output | Relevant Indian statute label or ranked statutes |
| Baselines / leaderboard context | Paper reports zero/few-shot, retrieval-augmented, supervised, and transfer-learning baselines. |
| Dataset access | External Google Drive download linked by the official repository |
| License | MIT code; dataset license not clearly stated |
| Gating | No account gate observed, but data are not versioned inside GitHub or Hugging Face |
| Maintenance | Recent EACL 2026 research release. |
| Reproducibility | Partial because the repository points to a mutable external data folder and does not expose a complete versioned benchmark package. |

### Metrics

- **Statute-identification classification/retrieval metrics:** The paper compares zero-shot, few-shot, RAG, supervised fine-tuning, and court-to-lay transfer; report the exact task split and official metric implementation. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/Law-AI/ilsic](https://github.com/Law-AI/ilsic) |
| Hugging Face | None located |
| Paper / arXiv | [https://arxiv.org/abs/2602.00881](https://arxiv.org/abs/2602.00881) |
| Leaderboard / competition | None located |
| Project | [https://drive.google.com/drive/folders/1m_tU6Cb55Q5mVQEImFUp-cUSVZzoHzfd](https://drive.google.com/drive/folders/1m_tU6Cb55Q5mVQEImFUp-cUSVZzoHzfd) |

### Validity and evidence

**Risks / caveats**
- Court and lay-query sources can contain duplicates or source-specific shortcuts.
- External Drive hosting weakens version pinning.
- Dataset license and exact public split/scorer contract are unclear.

**Verified facts**
- The official repository and arXiv paper establish the lay/court transfer task and 500+ statute scope.

**Unresolved ambiguity**
- Exact data revision, split files, aggregate scorer, and dataset license need stronger first-party documentation.

**Related entries**

- [AILA 2019](retrieval-rag-citation.md#aila-2019)

[Back to page index](#on-this-page)

<a id="rod-tal"></a>
## RoD-TAL

`rod-tal` · **benchmark-suite** · **specialist** · active

Answer Romanian driving-law questions and retrieve governing law or traffic signs from text and images.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | GRAI-UNSTPB / RoD-TAL authors (academic) |
| Catalog geography | Romania |
| First recorded public event | [2025-07-25](https://arxiv.org/abs/2507.19666) — arXiv v1 submission |
| Latest verified event | [2026-04-30](https://huggingface.co/datasets/GRAI-UNSTPB/RoD-TAL) — Hugging Face dataset update |
| Access level | gated |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test Romanian traffic-law retrieval and question answering on text-only exam questions.
- Test visual retrieval and visual question answering where signs or scene images are legally material.
- Compare no-RAG, retrieved-RAG, and ideal-context performance with citation and hallucination diagnostics.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Four text/vision task families test whether systems connect driving-exam questions and images to legal articles, signs, explanations, and correct answers. |
| Jurisdiction | Romania |
| Languages | Romanian |
| Size | 1,206 question rows across four configs: 638 text train/test, 181 additional text, 316 visual, and 71 visual/sign questions; 443 law passages and 140 traffic-sign items |
| Splits | split_1 has 510 train and 128 test; split_2/3/4 expose 181/316/71 all sets plus separate law/sign qrels |
| Source material | Romanian driving-license exam questions, traffic-law text, traffic signs, annotated legal references, and human explanations |
| Input | Text question or image-bearing driving scenario plus legal/sign corpora |
| Output | Ranked law/sign items and selected/generated answer |
| Baselines / leaderboard context | Paper/repository compare dense retrieval, reranking, fine-tuned embeddings, LLMs, and o4-mini visual QA configurations. |
| Dataset access | Manually gated Hugging Face release |
| License | CC BY-NC-SA 4.0 data; MIT code |
| Gating | Gate permits academic/noncommercial use and prohibits redistribution |
| Maintenance | Active EACL 2026 release; Hugging Face namespace redirects from the older unstpb-nlp name to GRAI-UNSTPB. |
| Reproducibility | Good after gate approval; public notebooks expose retrieval, QA, visual, and judge experiments. |

### Metrics

- **IR / visual IR precision, recall, and nDCG:** Evaluate legal-article and traffic-sign retrieval with named cutoffs under text, caption, or image reformulations. **Primary.**
- **QA / visual QA exact match, precision, recall, and F1:** Compare no-RAG, retrieved-RAG, and ideal-RAG answer predictions; separate post-hoc citation/hallucination judging. Judge: Optional LLM judge for error analysis, not the sole core scorer. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/vladman-25/RoD-TAL](https://github.com/vladman-25/RoD-TAL) |
| Hugging Face | [https://huggingface.co/datasets/GRAI-UNSTPB/RoD-TAL](https://huggingface.co/datasets/GRAI-UNSTPB/RoD-TAL) |
| Paper / arXiv | [https://arxiv.org/abs/2507.19666](https://arxiv.org/abs/2507.19666)<br>[https://aclanthology.org/2026.findings-eacl.295/](https://aclanthology.org/2026.findings-eacl.295/) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- Driving-license exams are legal education, not general Romanian legal practice.
- Multiple-choice and source formatting may supply shortcuts.
- Gated noncommercial access limits product evaluation, and optional LLM diagnostics add judge variance.

**Verified facts**
- The official repository, arXiv/ACL paper, and Hugging Face metadata establish four task families, exact config counts, two corpora, licensing, and the manual gate.

**Unresolved ambiguity**
- The older Hugging Face namespace now redirects to GRAI-UNSTPB; use the canonical target URL.

[Back to page index](#on-this-page)

<a id="open-legal-answer-benchmark"></a>
## Vaquill Open Legal-Answer Benchmark

`open-legal-answer-benchmark` · **benchmark** · **check before use** · active

Produce current US legal answers with relevant, supported, and correctly ranged citations.

**Also known as:** Open Legal-Answer Benchmark

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Vaquill AI (company; commercial interest) |
| Catalog geography | United States |
| First recorded public event | [2026-07-09](https://github.com/Vaquill-AI/open-legal-answer-benchmark) — GitHub repository creation |
| Latest verified event | [2026-07-18](https://github.com/Vaquill-AI/open-legal-answer-benchmark) — GitHub repository push |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test whether a system answers current US legal questions with the must-include propositions present and forbidden claims absent.
- Test citation support and in-range pinpointing for each answered claim.
- Regression-test a research product against the versioned question set after retrieval or model updates.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Checklist and citation metrics separate substantive required points, forbidden claims, authority retrieval, and citation entailment/range instead of collapsing answer quality into one judge score. |
| Jurisdiction | United States |
| Languages | English |
| Size | 54 base questions (29 hard, 25 controls) plus 8 adversarial variants; 62 JSONL rows |
| Splits | Public versioned evaluation set |
| Source material | Sponsor-authored current-law questions and cited authorities |
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
| Hugging Face | None located |
| Paper / arXiv | None located |
| Leaderboard / competition | [https://github.com/Vaquill-AI/open-legal-answer-benchmark/blob/main/LEADERBOARD.md](https://github.com/Vaquill-AI/open-legal-answer-benchmark/blob/main/LEADERBOARD.md) |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- Fully public questions permit direct optimization.
- Sponsor-run results are not an independent third-party audit.

**Verified facts**
- Official repository exposes the 62-row JSONL and leaderboard.

**Unresolved ambiguity**
- Temporal legal changes can make older gold expectations stale.

Original source bullet(s): #22

[Back to page index](#on-this-page)

<a id="legalcitebench"></a>
## LegalCiteBench

`legalcitebench` · **benchmark-suite** · **recommended** · active

Retrieve, complete, verify, and abstain on legal citations in US appellate text.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | LegalCiteBench authors (academic) |
| Catalog geography | United States |
| First recorded public event | [2026-05-06](https://huggingface.co/datasets/legalcitebench/LegalCiteBench) — Hugging Face dataset creation |
| Latest verified event | [2026-05-11](https://arxiv.org/abs/2605.10186) — arXiv v1 submission |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test citation retrieval, completion, verification, and abstention on US federal appellate opinions.
- Measure whether a model refuses when a valid citation cannot be supplied instead of fabricating authority.
- Regression-test citation components separately from end-to-end legal answer quality.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Five citation tasks separate finding authority, producing citation text, checking validity, and declining unsupported requests. |
| Jurisdiction | United States federal appellate courts |
| Languages | English |
| Size | 23,646 instances derived from 1,000 opinions |
| Splits | Five task-specific benchmark sets |
| Source material | CourtListener and the Appellate Case Law Project |
| Input | Opinion text or citation context |
| Output | Citation, verification decision, or abstention response |
| Baselines / leaderboard context | Paper compares frontier and open models across all five tasks. |
| Dataset access | Public Hugging Face release |
| License | CC0-1.0 data; MIT code |
| Gating | None observed |
| Maintenance | Active 2026 release; pin data, scorer, and judge versions. |
| Reproducibility | Public data and code support reruns; response scoring still depends on a named proprietary judge. |

### Metrics

- **MAR, citation F1, and correct-response rate:** Report task-specific 0–100 scores; mean average recall measures ranked citation retrieval, citation F1 measures generated citation components, and correct-response rate covers response/abstention decisions. Judge: GPT-4o-mini is reported for response scoring; Qwen3-32B appears in abstention analysis. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/Sijia711/LegalCiteBench](https://github.com/Sijia711/LegalCiteBench) |
| Hugging Face | [https://huggingface.co/datasets/legalcitebench/LegalCiteBench](https://huggingface.co/datasets/legalcitebench/LegalCiteBench) |
| Paper / arXiv | [https://arxiv.org/abs/2605.10186](https://arxiv.org/abs/2605.10186) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- Public opinions and generated examples may appear in training data.
- Citation-form correctness is not the same as precedential relevance or support for a proposition.
- Judge-model drift can change response scores.

**Verified facts**
- Official GitHub, Hugging Face, and arXiv artifacts establish 23,646 instances, 1,000 opinions, and five tasks.

**Unresolved ambiguity**
- The paper rounds the collection to about 24,000; use the released 23,646-instance count when pinning this version.

[Back to page index](#on-this-page)

<a id="legal-phantom-citation"></a>
## Legal Phantom Citation

`legal-phantom-citation` · **benchmark** · **specialist** · active

Identify hallucinated legal citations and affected spans in federal appellate brief text.

**Also known as:** LePhantomCite

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Princeton Polaris Lab / AI, Law & Society Lab (academic) |
| Catalog geography | United States |
| First recorded public event | [2026-04-07](https://huggingface.co/datasets/ai-law-society-lab/Legal_Phantom_Citation) — Hugging Face dataset creation |
| Latest verified event | [2026-07-06](https://huggingface.co/datasets/ai-law-society-lab/Legal_Phantom_Citation) — Hugging Face dataset update |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test whether a system detects fabricated or materially distorted citations in federal appellate briefs.
- Compare citation-hallucination detectors using span-level precision, recall, and F1.
- Build adversarial citation checks around verified holdings and authentic brief excerpts.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Expert-verified real and phantom citation examples turn citation safety into span detection rather than open-ended answer judging. |
| Jurisdiction | United States federal appellate courts, 13 circuits |
| Languages | English |
| Size | 1,300 excerpts: 1,000 real excerpts from 245 briefs and 300 verified holding entries |
| Splits | 390-example evaluation split and 910 auxiliary training examples |
| Source material | Federal appellate briefs filed from 2012–2021 plus verified case holdings |
| Input | Brief excerpt containing citation-bearing legal text |
| Output | Hallucination span and type labels |
| Baselines / leaderboard context | Paper reports detector baselines and agent results on the held-out evaluation split. |
| Dataset access | Public Hugging Face release |
| License | CC BY 4.0 |
| Gating | None observed |
| Maintenance | Active 2026 research release. |
| Reproducibility | Public labels and span scorer support reruns when the matching rule and split revision are pinned. |

### Metrics

- **Span precision, recall, and F1:** Relaxed substring matching compares predicted hallucination spans with expert labels; report precision, recall, and F1. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/princeton-polaris-lab/legal-hallucination-agent](https://github.com/princeton-polaris-lab/legal-hallucination-agent) |
| Hugging Face | [https://huggingface.co/datasets/ai-law-society-lab/Legal_Phantom_Citation](https://huggingface.co/datasets/ai-law-society-lab/Legal_Phantom_Citation) |
| Paper / arXiv | [https://arxiv.org/abs/2606.21155](https://arxiv.org/abs/2606.21155) |
| Leaderboard / competition | None located |
| Project | [https://princeton-polaris-lab.github.io/legal-hallucination-webpage/](https://princeton-polaris-lab.github.io/legal-hallucination-webpage/) |

### Validity and evidence

**Risks / caveats**
- The benchmark detects cited-text hallucinations but does not measure omitted controlling authority.
- Briefs from 2012–2021 may not represent current filing practices or all courts.
- Relaxed span matching can credit approximate localization without proving the underlying legal diagnosis.

**Verified facts**
- The official paper, project, GitHub, and Hugging Face artifacts establish the 1,300-example collection and 13-circuit coverage.

[Back to page index](#on-this-page)

<a id="reglab-legal-hallucinations"></a>
## Large Legal Fictions

`reglab-legal-hallucinations` · **benchmark-suite** · **specialist** · fixed-release

Answer verifiable closed-form questions about US federal cases without inventing cases, citations, holdings, or treatment.

**Also known as:** RegLab Legal Hallucinations

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Stanford RegLab / Yale authors (academic) |
| Catalog geography | United States |
| First recorded public event | [2024-01-02](https://arxiv.org/abs/2401.01301) — arXiv v1 submission |
| Latest verified event | [2024-06-26](https://github.com/reglab/legal_hallucinations) — GitHub repository push |
| Access level | partial |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Measure hallucination on closed-form questions about US federal cases, citations, dispositions, and overruling dates.
- Test sycophancy and cross-run consistency on verifiable legal facts.
- Use the public release to study how model scale and court hierarchy correlate with legal hallucination.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Questions tied to case metadata and holdings make hallucination observable through correctness, contradiction, and consistency labels. |
| Jurisdiction | United States federal courts |
| Languages | English |
| Size | Public release contains more than 48,000 rows across task configurations |
| Splits | About 90% public data with a roughly 10% reserved portion described by the release |
| Source material | US federal case metadata, citations, holdings, and treatment history |
| Input | Closed-form question about a named or cited federal case |
| Output | Case-existence, citation, disposition, or overruling answer |
| Baselines / leaderboard context | Paper profiles GPT-3.5, Llama-2, and related model families rather than maintaining a live leaderboard. |
| Dataset access | Large public release plus a described reserve |
| License | No clear Hugging Face dataset license declaration located |
| Gating | None for public files |
| Maintenance | Fixed 2024 research release; not a live product benchmark. |
| Reproducibility | Public code and data support reruns; exact task configuration, model snapshot, and manual coding protocol must be pinned. |

### Metrics

- **Correctness and hallucination rate:** Score answer correctness against case metadata and manual labels; report hallucination, sycophancy, and consistency analyses by task and court level. Judge: Rule-based checks plus manual coding under the paper protocol. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/reglab/legal_hallucinations](https://github.com/reglab/legal_hallucinations) |
| Hugging Face | [https://huggingface.co/datasets/reglab/legal_hallucinations](https://huggingface.co/datasets/reglab/legal_hallucinations) |
| Paper / arXiv | [https://arxiv.org/abs/2401.01301](https://arxiv.org/abs/2401.01301) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- The evaluated models are historically dated and results should not be treated as current rankings.
- Closed-form case facts do not cover legal research completeness or drafting quality.
- Case metadata and prompts are public and contamination-prone.

**Verified facts**
- Official arXiv, GitHub, and Hugging Face artifacts establish the benchmark and public data release.

**Unresolved ambiguity**
- The release does not declare a clear dataset license in Hugging Face metadata.

[Back to page index](#on-this-page)

<a id="reglab-legal-rag-hallucinations"></a>
## Hallucination-Free? Legal Research Tool Study

`reglab-legal-rag-hallucinations` · **evaluation-protocol** · **recommended** · completed

Return correct, grounded, responsive legal research answers without false authority or unsupported propositions.

**Also known as:** RegLab Legal RAG Hallucinations

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Stanford RegLab (academic) |
| Catalog geography | United States |
| First recorded public event | [2024-05-30](https://arxiv.org/abs/2405.20362) — arXiv v1 submission |
| Latest verified event | [2024-11-14](https://huggingface.co/datasets/reglab/legal_rag_hallucinations) — Hugging Face dataset update |
| Access level | partial |
| Test labels | mixed |
| Independently runnable | partial |

### Possible use cases

- Study correctness, groundedness, responsiveness, and hallucination in AI legal research answers using human-coded labels.
- Reuse the released queries and coding taxonomy for a current, independently run product audit.
- Compare failure modes such as false retrieval and false grounding rather than reporting one generic hallucination rate.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | A preregistered human-coding protocol separates correctness, completeness/relevance, grounding, and distinct hallucination mechanisms in product answers. |
| Jurisdiction | United States |
| Languages | English |
| Size | More than 200 legal queries; public release contains 400 rows representing about half of the evaluated product-query outputs |
| Splits | About 50% public release and 50% reserve |
| Source material | Hand-authored legal research queries and captured answers from commercial tools and GPT-4 in 2024 |
| Input | Legal research query submitted to a product |
| Output | Product answer with cited sources, then expert coding labels |
| Baselines / leaderboard context | Study compares Lexis+ AI, Westlaw AI-Assisted Research, Ask Practical Law AI, and GPT-4 as they existed in 2024. |
| Dataset access | Partial public release |
| License | CC BY 4.0 on the Hugging Face release |
| Gating | No gate for public rows; remaining study data are not public |
| Maintenance | Completed empirical study of product versions captured in 2024; a peer-reviewed version appeared in 2025. |
| Reproducibility | The coding protocol and half-release support partial audit; exact historical commercial product behavior cannot be recreated. |

### Metrics

- **Human-coded correctness, groundedness, responsiveness, and hallucination rates:** Experts code each answer for correctness, incomplete/irrelevant content, source support, false retrieval, and false grounding under the study codebook. Judge: Human legal expert coding. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | None located |
| Hugging Face | [https://huggingface.co/datasets/reglab/legal_rag_hallucinations](https://huggingface.co/datasets/reglab/legal_rag_hallucinations) |
| Paper / arXiv | [https://arxiv.org/abs/2405.20362](https://arxiv.org/abs/2405.20362) |
| Leaderboard / competition | None located |
| Project | [https://reglab.stanford.edu/publications/hallucination-free-assessing-the-reliability-of-leading-ai-legal-research-tools/](https://reglab.stanford.edu/publications/hallucination-free-assessing-the-reliability-of-leading-ai-legal-research-tools/) |

### Validity and evidence

**Risks / caveats**
- Commercial products are moving targets, so the reported ranking is historical.
- The query set is small relative to legal practice and only half of product outputs are public.
- Vendor disputes around early results reinforce the need to inspect the codebook and released evidence.

**Verified facts**
- The official paper, RegLab page, and Hugging Face release document the products, human-coded dimensions, and partial data release.

**Inference**
- The protocol is more reusable than the historical product ranking.

**Unresolved ambiguity**
- Exact recreation of the tested 2024 product versions is impossible.

[Back to page index](#on-this-page)

<a id="vals-legal-research-bench"></a>
## Vals Legal Research Benchmark

`vals-legal-research-bench` · **private-benchmark** · **check before use** · private

Research US legal questions and produce answers satisfying lawyer-authored substantive and citation criteria.

**Also known as:** Vals Legal Research Bench

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Vals AI (company; commercial interest) |
| Catalog geography | United States |
| First recorded public event | [2025-10](https://www.vals.ai/benchmarks/legal_research) — Earliest first-party release period located in Vals' benchmark timeline |
| Latest verified event | [2026-08-03](https://www.vals.ai/benchmarks/legal_research) — Official benchmark page update date |
| Access level | partial |
| Test labels | hidden |
| Independently runnable | no |

### Possible use cases

- Read current leaderboard results on US legal research questions across eight practice areas.
- License the private validation set to evaluate research systems with lawyer-authored answers and rubrics.
- Report all-pass and weighted partial credit together to separate complete answers from near misses.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Peer-reviewed questions and 1–31 weighted rubric items measure both complete matter-level success and partial coverage across eight practice areas. |
| Jurisdiction | United States |
| Languages | English |
| Size | 413 expert-authored and peer-reviewed questions |
| Splits | 5 public samples, 200 private validation questions available for license, and 208 hidden test questions |
| Source material | Lawyer-authored questions, reference answers, and rubrics across eight practice areas |
| Input | Legal research question |
| Output | Research answer with relevant authority |
| Baselines / leaderboard context | Vals publishes a current model/product leaderboard on the benchmark page. |
| Dataset access | Five samples public; validation available under license; test private |
| License | Commercial/private license for validation access |
| Gating | License request required; hidden test remains operator-controlled |
| Maintenance | Active private benchmark updated August 3, 2026. |
| Reproducibility | Partial for licensed participants and low for outsiders because most questions, rubrics, and test labels are private. |

### Metrics

- **All-pass task rate:** A task passes only when every rubric item passes. Judge: GPT-5.4. **Primary.**
- **Weighted partial-credit score:** Sum satisfied rubric weights divided by total rubric weight; rubrics contain 1–31 items with a reported mean of 9.35. Judge: GPT-5.4.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | None located |
| Hugging Face | None located |
| Paper / arXiv | None located |
| Leaderboard / competition | [https://www.vals.ai/benchmarks/legal_research](https://www.vals.ai/benchmarks/legal_research) |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- Vals controls the private data, judge configuration, and leaderboard.
- All-pass scores depend strongly on rubric length.
- A GPT-5.4 judge can introduce model-family and prompt sensitivity.

**Verified facts**
- The official Vals page reports 413 questions, the 5/200/208 split, eight practice areas, rubric ranges, both score types, GPT-5.4 judging, and the update date.

**Unresolved ambiguity**
- October 2025 is the earliest first-party release period located, not a separately labeled launch date.

[Back to page index](#on-this-page)

<a id="vals-caselaw-v2"></a>
## Vals CaseLaw v2

`vals-caselaw-v2` · **private-benchmark** · **related artifact** · archived

Answer Canadian case-law questions with correct, relevant, well-supported legal analysis.

**Also known as:** CaseLaw v2

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Vals AI (company; commercial interest) |
| Catalog geography | Canada |
| First recorded public event | [2026-02-05](https://www.vals.ai/benchmarks/case_law_v2) — Earliest dated first-party page located with CaseLaw v2 present |
| Latest verified event | [2026-05-04](https://www.vals.ai/benchmarks/case_law_v2) — Official benchmark page update date |
| Access level | private |
| Test labels | hidden |
| Independently runnable | no |

### Possible use cases

- Use archived results as historical evidence about Canadian case-law question answering under Vals' seven-dimension rubric.
- Use its archived/saturated status as a warning against continuing to optimize on a benchmark that no longer separates systems.
- Borrow the multi-dimension rubric structure when designing a fresh Canadian case-law holdout.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Seven judge dimensions assess case-law answer quality, but the private benchmark is now archived after reported saturation. |
| Jurisdiction | Canada |
| Languages | English |
| Size | 404 questions: 300 validation and 104 test |
| Splits | Private 300-question validation and 104-question test sets |
| Source material | Private Canadian court-case questions and reference materials |
| Input | Canadian case-law question |
| Output | Legal answer with case support |
| Baselines / leaderboard context | Archived Vals leaderboard reports historical model results; Vals labels the benchmark saturated. |
| Dataset access | Private |
| License | Not publicly stated |
| Gating | No public task set, labels, GitHub, Hugging Face, or paper |
| Maintenance | Archived/saturated; official page last updated May 4, 2026. |
| Reproducibility | Low outside Vals because questions, labels, and evaluator are private; historical page remains inspectable. |

### Metrics

- **Seven-dimension answer score:** Vals grades answers across seven disclosed quality dimensions under its private evaluator; use the archived page's exact protocol when interpreting historical scores. Judge: Private Vals evaluator configuration. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | None located |
| Hugging Face | None located |
| Paper / arXiv | None located |
| Leaderboard / competition | [https://www.vals.ai/benchmarks/case_law_v2](https://www.vals.ai/benchmarks/case_law_v2) |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- Vals controls the private instrument and historical leaderboard.
- Saturation weakens its ability to discriminate current systems.
- Private data and judge prevent independent reproduction.

**Verified facts**
- The official Vals page marks CaseLaw v2 archived/saturated and reports 300 validation plus 104 test questions.

**Inference**
- A fresh Canadian case-law holdout is preferable for current model selection.

**Unresolved ambiguity**
- February 5, 2026 is the earliest dated first-party documentation located, not necessarily the original launch date; exact seven-dimension judge details are incomplete.

[Back to page index](#on-this-page)

<a id="laborbench"></a>
## LaborBench

`laborbench` · **benchmark** · **specialist** · fixed-release

Extract and answer state-specific unemployment-insurance law questions from statutes and regulations.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Stanford Regulation, Evaluation, and Governance Lab (academic) |
| Catalog geography | United States |
| First recorded public event | [2025-05-02](https://huggingface.co/datasets/reglab/laborbench) — Hugging Face dataset creation |
| Latest verified event | [2025-08-26](https://arxiv.org/abs/2508.19365) — arXiv v1 submission after the dataset release |
| Access level | open |
| Test labels | public |
| Independently runnable | partial |

### Possible use cases

- Test state-by-state unemployment-insurance statutory and regulatory question answering on lawyer-maintained source material.
- Compare no-retrieval and RAG systems on the released Boolean supplement using accuracy, precision, recall, and F1.
- Use the jurisdiction field to diagnose state-level performance variation rather than relying only on one national average.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | LaborBench converts an annually lawyer-maintained Department of Labor comparison into structured questions; the paper's scored experiment tests Boolean legal QA with and without retrieval from StateCodes. |
| Jurisdiction | United States: 50 states, District of Columbia, Puerto Rico, and U.S. Virgin Islands |
| Languages | English |
| Size | Hugging Face exposes 3,700 QA rows, a 3,015-row Boolean supplement, and 83 table records; the configs overlap by design and must not be summed as independent questions |
| Splits | Each released configuration exposes one public train split; no hidden test split is published |
| Source material | 2023 U.S. Department of Labor Comparison of State Unemployment Insurance Laws tables; the paper pairs the Boolean task with the 2023 StateCodes statute/regulation corpus |
| Input | Jurisdiction-specific question, optional source-table context, and optionally top-five retrieved statutory or regulatory sections |
| Output | Typed answer (Boolean, string, or integer); the paper's scored experiment emits a Boolean JSON field and optional citation URL |
| Baselines / leaderboard context | The paper compares no-retrieval with E5-large, Gemini, Okapi BM25, and OpenAI retrieval across GPT-4o mini, Gemini 1.5 Flash, Claude 3.5 Haiku, Llama 3.1 70B Instruct, and DeepSeek V3; the best reported RAG F1 is 0.691. |
| Dataset access | Public Hugging Face release with public labels |
| License | MIT according to the Hugging Face dataset metadata |
| Gating | None observed; no canonical benchmark repository or executable scorer was located |
| Maintenance | The public dataset was created and last modified on May 2, 2025; the paper appeared on August 26, 2025. No later versioned LaborBench data release was verified by the 2026-08-05 cutoff. |
| Reproducibility | The rows and labels are public, but the released hub artifact has no hidden split or canonical end-to-end harness; reproducing the paper also requires a pinned StateCodes crawl, retrievers, model versions, prompts, and output parser. |

### Metrics

- **Accuracy / precision / recall / F1:** The paper scores the Boolean supplement as binary classification and reports nonparametric-bootstrap standard errors from 1,000 resamples; report all four metrics because class behavior is asymmetric. **Primary.**
- **Citation retrieval diagnostics:** The paper manually checks elicited citations and separately reports OpenAI retriever recall@5; these diagnostics are not a single canonical LaborBench score. Judge: Human review for the cited subset.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | None located |
| Hugging Face | [https://huggingface.co/datasets/reglab/laborbench](https://huggingface.co/datasets/reglab/laborbench) |
| Paper / arXiv | [https://arxiv.org/abs/2508.19365](https://arxiv.org/abs/2508.19365) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- All questions and labels are public and may be used for tuning or appear in model training.
- The legal source snapshot is from 2023, so later statutory and regulatory changes can make answers temporally stale.
- A single public split makes accidental evaluation-on-training easy, and the scored Boolean supplement does not represent every answer type in the main QA release.

**Verified facts**
- The official Hugging Face API exposes 3,700 QA rows, 3,015 Boolean-supplement rows, 83 tables, one train split per config, an MIT tag, and a May 2, 2025 creation date.
- The official paper defines the Department of Labor source, StateCodes pairing, binary metrics, model/retriever baselines, and bootstrap protocol.

**Inference**
- A fresh held-out annual update would be more useful for current procurement than the fully public 2023-source release.

**Unresolved ambiguity**
- No canonical LaborBench GitHub scorer, hidden test set, leaderboard, or post-paper dataset revision was located.

**Related entries**

- [RegLab Reasoning-Focused Legal Retrieval Benchmark](retrieval-rag-citation.md#reglab-reasoning-focused-retrieval)
- [LegalBench-RAG](retrieval-rag-citation.md#legalbench-rag)

[Back to page index](#on-this-page)

<a id="lexrag"></a>
## LexRAG

`lexrag` · **benchmark** · **check before use** · fixed-release

Retrieve relevant Chinese legal articles and answer five-turn legal consultation dialogues with grounded responses.

**Also known as:** LexiT

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | LexRAG authors (academic) |
| Catalog geography | China |
| First recorded public event | [2025-02-10](https://github.com/CSHaitao/LexRAG) — GitHub repository creation |
| Latest verified event | [2025-03-03](https://github.com/CSHaitao/LexRAG) — GitHub repository push |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Evaluate multi-turn Chinese legal-article retrieval and grounded consultation response generation.
- Compare retrieval quality at each dialogue turn before attributing generation failures to the answer model.
- Reuse the public LexiT pipeline to build a private, time-held-out Chinese-law conversational RAG evaluation.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Rank metrics measure article retrieval at each turn, while keyword coverage and a disclosed LLM judge score answer factuality, satisfaction, clarity, coherence, and completeness. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | 1,013 five-turn dialogues (5,065 query turns) over 17,228 legal articles; average 1.09 relevant articles per query |
| Splits | One fixed public evaluation collection with dialogue-level labels; no hidden test |
| Source material | Chinese legal consultation dialogues and a statute/law library |
| Input | Conversation history and current legal query, plus the retrievable law corpus |
| Output | Ranked legal articles and a grounded consultation response |
| Baselines / leaderboard context | The paper and LexiT toolkit compare sparse, dense, and hybrid retrievers plus generation models under conversational and single-turn settings. |
| Dataset access | Public repository with full dialogue JSON, 17,228-article law library, prompts, and evaluation pipeline |
| License | No repository-wide code or data license was located |
| Gating | None observed; model/API access may be needed to reproduce judge scores |
| Maintenance | Fixed 2025 research release; pin the repository because no versioned dataset package or maintained leaderboard was located. |
| Reproducibility | Good for public retrieval reruns and partial for generation because the released prompt still depends on a model snapshot and no license is declared. |

### Metrics

- **Recall and nDCG @1/3/5/10:** Evaluate ranked relevant-article retrieval at the stated cutoffs; the toolkit also exposes MRR, precision, and F1 variants. **Primary.**
- **Keyword accuracy and 1–10 response score:** Measure required-keyword coverage and ask the disclosed judge to rate factuality, satisfaction, clarity, coherence, and completeness using the released prompt. Judge: Qwen2.5-72B-Instruct. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/CSHaitao/LexRAG](https://github.com/CSHaitao/LexRAG) |
| Hugging Face | None located |
| Paper / arXiv | [https://arxiv.org/abs/2502.20640](https://arxiv.org/abs/2502.20640) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- All dialogues, relevance labels, and legal articles are public, creating contamination and tuning risk.
- One LLM judge can encode stylistic and model-family preferences.
- The paper contains one 17,728-article typo; the repository and other tables consistently support 17,228.

**Verified facts**
- The official repository contains 1,013 complete five-turn dialogues, 17,228 law-library records, evaluation prompts, and runnable retrieval/generation code.
- The arXiv paper defines the retrieval cutoffs and Qwen2.5-72B-Instruct generation judge.

**Inference**
- LexRAG tests a distinct conversational RAG construct but shares lab lineage with LexEval and should not be treated as independent institutional replication.

**Unresolved ambiguity**
- No license, Hugging Face release, hidden test, or maintained leaderboard was located.

[Back to page index](#on-this-page)

<a id="muser"></a>
## MUSER

`muser` · **benchmark** · **specialist** · fixed-release

Retrieve similar Chinese civil cases using multiple legally relevant views of case similarity.

**Also known as:** Multi-view Similar Case Retrieval

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Tsinghua University LawTech / MUSER authors (academic) |
| Catalog geography | China |
| First recorded public event | [2023-06-16](https://github.com/THUlawtech/MUSER) — GitHub repository creation |
| Latest verified event | [2025-07-25](https://github.com/THUlawtech/MUSER) — GitHub repository push |
| Access level | open |
| Test labels | public |
| Independently runnable | partial |

### Possible use cases

- Evaluate Chinese civil similar-case retrieval under fact, dispute-focus, and statutory-law views of relevance.
- Compare sparse, dense, and legal-element ranking systems on the public candidate pools and qrels.
- Diagnose whether a retriever finds the same cases for the same reasons before building a private civil-law retrieval test.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Top-rank and average-precision metrics score retrieval against multi-view qrels, while element-prediction F1 tests an intermediate structured representation of facts, disputes, and law. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | 100 queries and 4,024 total case documents; 100 candidates per query and an average 10.38 relevant candidates per query |
| Splits | Public qrels and score files; the deep model uses an 80/20 query split, while sparse/element baselines evaluate all queries |
| Source material | Chinese civil cases annotated for legal fact, dispute focus, and statutory-law relevance |
| Input | Chinese civil query case and candidate case pool |
| Output | Ranked similar cases and optional predicted legal elements |
| Baselines / leaderboard context | The paper compares BM25, TF-IDF, LMIR, Lawformer, and a legal-element retrieval model. |
| Dataset access | Core cases, qrels, gold labels, and result files are public in GitHub; some deep-model train/test assets are linked through Google Drive |
| License | MIT repository license |
| Gating | Core benchmark is open; durability of external Drive assets is weaker |
| Maintenance | Stable research release with later repository maintenance through July 2025. |
| Reproducibility | Good for core sparse retrieval with pinned qrels; partial for deep-model reproduction that depends on externally hosted files. |

### Metrics

- **P@5 / P@10 / MAP:** Measure early precision and mean average precision over the public multi-view relevance judgments. **Primary.**
- **nDCG@10 / @20 / @30:** Measure discounted graded ranking quality at the stated cutoffs. **Primary.**
- **Element prediction precision / recall / F1:** Evaluate the intermediate legal-element predictions separately from case ranking.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/THUlawtech/MUSER](https://github.com/THUlawtech/MUSER) |
| Hugging Face | None located |
| Paper / arXiv | [https://arxiv.org/abs/2310.15602](https://arxiv.org/abs/2310.15602) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- Only 100 queries make aggregate results sensitive to query selection.
- Public qrels and candidates permit direct tuning.
- Candidate-pool overlap with LeCaRDv2 or other Chinese case corpora has not been ruled out at document level.

**Verified facts**
- The official arXiv paper and MIT-licensed repository establish 100 queries, 4,024 documents, public multi-view qrels, metric cutoffs, score files, and baselines.

**Inference**
- MUSER complements criminal-case LeCaRDv2 with a civil-law relevance construct but is weaker on query scale.

**Unresolved ambiguity**
- No canonical Hugging Face release, maintained leaderboard, or published corpus-overlap audit was located.

[Back to page index](#on-this-page)
