# Retrieval, RAG, and citation

<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->

Authority retrieval, exact-support retrieval, case similarity, citation grounding, and end-to-end legal RAG.

Snapshot: **2026-08-03** · 10 entries

[Catalog index](../catalog.md) · [Selection guide](../selection-guide.md) · [Metric field guide](../metric-theory.md) · [Methodology](../methodology.md)

## On this page

- [Massive Legal Embedding Benchmark](#mleb)
- [LegalBench-RAG](#legalbench-rag)
- [Belgian Statutory Article Retrieval Dataset](#bsard)
- [LLeQA](#lleqa)
- [CLERC](#clerc)
- [Reasoning-Focused Legal Retrieval Benchmark](#reglab-reasoning-focused-retrieval)
- [LeCaRDv2](#lecardv2)
- [Competition on Legal Information Extraction/Entailment](#coliee)
- [Legal RAG Bench](#legal-rag-bench)
- [CanLegalRAGBench](#canlegalragbench)

<a id="mleb"></a>
## Massive Legal Embedding Benchmark

`mleb` · **benchmark-suite** · **specialist** · active

Legal embedding quality across retrieval, retrieval-augmented QA, and zero-shot classification tasks.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | MTEB-compatible task configurations treat rank quality—usually nDCG@10—as the main proxy for useful legal representations, supplemented by QA and classification task scores. |
| Jurisdiction | United States, United Kingdom, European Union, Australia, Ireland, Singapore |
| Languages | English |
| Size | 10 constituent datasets |
| Splits | Dataset-specific MTEB evaluation splits |
| Source | Public legal retrieval, QA, and classification datasets assembled by Isaacus |
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
| Project | None |

### Validity and evidence

**Risks / caveats**
- All public queries and labels permit benchmark-targeted optimization.
- Benchmark owner also sells a leading model, so independently reproduced results are preferable.

**Verified facts**
- Both source README bullets resolve to the same GitHub repository and benchmark identity.

**Inference**
- None recorded.

**Unresolved ambiguity**
- The original awesome-list Kanon/MLEB URL could not be verified as canonical.

Original source bullet(s): #3, #20

[Back to page index](#on-this-page)

<a id="legalbench-rag"></a>
## LegalBench-RAG

`legalbench-rag` · **benchmark** · **recommended** · fixed-release

Retrieve exact supporting spans from long legal and policy documents.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Character-level precision and recall directly measure whether retrieved text covers gold support while limiting extra context; this isolates retrieval from answer generation. |
| Jurisdiction | United States, mixed contracts and policies |
| Languages | English |
| Size | 714 documents, more than 79M characters; 6,858 queries in abstract versus 6,889 in a paper table |
| Splits | Public fixed evaluation release |
| Source | Four public contract/policy datasets |
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
| Hugging Face | None |
| Paper / arXiv | [https://arxiv.org/abs/2408.10343](https://arxiv.org/abs/2408.10343) |
| Leaderboard / competition | None |
| Project | [https://www.dropbox.com/scl/fo/r7xfa5i3hdsbxex1w6amw/AID389Olvtm-ZLTKAPrw6k4?rlkey=5n8zrbk4c08lbit3iiexofmwg&st=0hu354cq&dl=0](https://www.dropbox.com/scl/fo/r7xfa5i3hdsbxex1w6amw/AID389Olvtm-ZLTKAPrw6k4?rlkey=5n8zrbk4c08lbit3iiexofmwg&st=0hu354cq&dl=0) |

### Validity and evidence

**Risks / caveats**
- No hidden split; queries, corpus, and spans are public.
- The paper's query counts conflict and should never be silently harmonized.

**Verified facts**
- Official repository and paper define exact-span evaluation.

**Inference**
- None recorded.

**Unresolved ambiguity**
- 6,858 versus 6,889 query count remains unresolved.

Original source bullet(s): #9

[Back to page index](#on-this-page)

<a id="bsard"></a>
## Belgian Statutory Article Retrieval Dataset

`bsard` · **benchmark** · **recommended** · fixed-release

Retrieve Belgian statutory articles relevant to a legal question.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Recall@k tests whether needed authority appears in the candidate set; MRR/MAP reward placing one or all relevant provisions early. |
| Jurisdiction | Belgium |
| Languages | French |
| Size | 1,108 legal questions and 22,633 statutory articles |
| Splits | Official benchmark splits/files |
| Source | Questions from Belgian legal practitioners and Belgian legislation |
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
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Static statutes can become temporally stale.
- Incomplete relevance judgments can mark alternative valid authorities as false positives.

**Verified facts**
- Official GitHub/HF/paper establish 1,108 questions and 22,633 articles.

**Inference**
- None recorded.

**Unresolved ambiguity**
- None recorded.

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)

<a id="lleqa"></a>
## LLeQA

`lleqa` · **benchmark** · **specialist** · fixed-release

Retrieve Belgian legal authorities and generate long-form answers to practitioner-style questions.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | The benchmark joins retrieval coverage with answer similarity/grounding, allowing diagnosis of whether failure came from authority retrieval or answer synthesis. |
| Jurisdiction | Belgium |
| Languages | French |
| Size | 1,868 questions with expert answers/references and 27,941 legal articles |
| Splits | Official release; access is gated by data agreement |
| Source | Belgian legal questions, detailed answers, and statutory materials |
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
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Reference overlap under-rewards legally equivalent answers and can reward unsupported paraphrase.
- Gating limits frictionless independent reruns.

**Verified facts**
- Official GitHub/HF/paper establish the dataset and gated access.

**Inference**
- None recorded.

**Unresolved ambiguity**
- None recorded.

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)

<a id="clerc"></a>
## CLERC

`clerc` · **benchmark** · **specialist** · fixed-release

Retrieve US case-law evidence and generate citation-grounded legal text.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Large-corpus recall measures whether cited support is retrieved; generation metrics and citation/hallucination analysis assess whether answers use that evidence faithfully. |
| Jurisdiction | United States |
| Languages | English |
| Size | Large US case-law corpus with citation-linked retrieval and generation examples |
| Splits | Official dataset configurations |
| Source | Public US judicial opinions and citations |
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
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Citation links are not identical to relevance and may encode court-writing conventions.
- Public opinions and citation graph can appear in pretraining.

**Verified facts**
- Official JHU repository/HF/paper define retrieval and generation tasks.

**Inference**
- None recorded.

**Unresolved ambiguity**
- Dataset scale is configuration-dependent; cite the exact config rather than one loose total.

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)

<a id="reglab-reasoning-focused-retrieval"></a>
## Reasoning-Focused Legal Retrieval Benchmark

`reglab-reasoning-focused-retrieval` · **benchmark-suite** · **recommended** · fixed-release

Retrieve controlling text for legal questions whose answer has low lexical overlap with the relevant source.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | The suite intentionally stresses semantic/legal reasoning in retrieval; Recall@k/MRR measure evidence ranking and downstream QA accuracy tests whether the retrieved authority is usable. |
| Jurisdiction | United States |
| Languages | English |
| Size | BarExam QA: 1,195 historical plus 1,815 Barbri questions over about 856,835 passages; Housing QA: 6,853 queries over about 1,837,403 passages |
| Splits | Dataset-specific evaluation sets |
| Source | Bar exam questions and US housing-law questions paired with large legal corpora |
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
| GitHub | None |
| Hugging Face | [https://huggingface.co/collections/reglab/a-reasoning-focused-legal-retrieval-benchmark-67a00c363f7e0d14619e95c5](https://huggingface.co/collections/reglab/a-reasoning-focused-legal-retrieval-benchmark-67a00c363f7e0d14619e95c5)<br>[https://huggingface.co/datasets/reglab/barexam_qa](https://huggingface.co/datasets/reglab/barexam_qa)<br>[https://huggingface.co/datasets/reglab/housing_qa](https://huggingface.co/datasets/reglab/housing_qa) |
| Paper / arXiv | [https://arxiv.org/abs/2505.03970](https://arxiv.org/abs/2505.03970) |
| Leaderboard / competition | None |
| Project | [https://reglab.github.io/legal-rag-benchmarks/](https://reglab.github.io/legal-rag-benchmarks/) |

### Validity and evidence

**Risks / caveats**
- Bar exam questions and source law are public and contamination-prone.
- Lexical-overlap filtering may select an artificial difficulty distribution.

**Verified facts**
- Official RegLab project/paper/HF collection define both datasets and retrieval metrics.

**Inference**
- None recorded.

**Unresolved ambiguity**
- No canonical GitHub URL was found.

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)

<a id="lecardv2"></a>
## LeCaRDv2

`lecardv2` · **benchmark** · **recommended** · fixed-release

Retrieve legally similar Chinese criminal cases using graded relevance across characterization, penalty, and procedure.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Expert multi-aspect relevance separates factual/legal similarity from mere lexical overlap; recall at large k tests first-stage retrieval and nDCG/precision support reranking analysis. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | 800 query cases, 55,192 judged candidates sampled from 4.3M criminal cases |
| Splits | 640 train / 160 test queries for the reported fine-tuning setup |
| Source | Chinese criminal judgments with expert graded relevance |
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
| Hugging Face | None |
| Paper / arXiv | [https://arxiv.org/abs/2310.17609](https://arxiv.org/abs/2310.17609) |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Judged candidate pooling can miss relevant cases outside the pool.
- Chronological and court-source shortcuts may inflate similarity.

**Verified facts**
- Official repository/paper establish 800 queries, 55,192 candidates, and 4.3M source cases.

**Inference**
- None recorded.

**Unresolved ambiguity**
- None recorded.

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)

<a id="coliee"></a>
## Competition on Legal Information Extraction/Entailment

`coliee` · **shared-task** · **recommended** · annual

Retrieve and recognize entailment among Canadian cases and Japanese civil-code provisions.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Four annual tasks separate first-stage authority retrieval from textual entailment; official hidden tests reduce direct leakage, while task-specific precision/recall/F1 and accuracy measure different stages. |
| Jurisdiction | Canada, Japan |
| Languages | English, Japanese |
| Size | Annual task packages; counts change by year |
| Splits | Released training data plus competition-held test labels |
| Source | Canadian case law and Japanese civil-code/bar-exam materials |
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
| GitHub | None |
| Hugging Face | None |
| Paper / arXiv | None |
| Leaderboard / competition | [https://coliee.org/COLIEE2025/submission](https://coliee.org/COLIEE2025/submission) |
| Project | [https://coliee.org/COLIEE2025/overview](https://coliee.org/COLIEE2025/overview) |

### Validity and evidence

**Risks / caveats**
- Task definitions, corpora, and metrics change between annual editions.
- Competition access terms and later link rot can limit retrospective reproduction.

**Verified facts**
- Official COLIEE 2025 site defines four tasks and competition access.

**Inference**
- None recorded.

**Unresolved ambiguity**
- There is intentionally no single edition-independent dataset size or metric.

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)

<a id="legal-rag-bench"></a>
## Legal RAG Bench

`legal-rag-bench` · **benchmark** · **check before use** · active

Evaluate an end-to-end legal RAG pipeline and attribute errors to retrieval versus generation.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | A full factorial retriever×generator design plus hierarchical error decomposition tests whether gold support was retrieved, whether an answer is correct against expert reference, and whether its claims are grounded in supplied context. |
| Jurisdiction | Victoria, Australia / criminal law and procedure |
| Languages | English |
| Size | 4,876 passages and 100 expert-crafted questions |
| Splits | Public test corpus and QA files |
| Source | Victorian Criminal Charge Book with human answers/supporting passages |
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
| Leaderboard / competition | None |
| Project | [https://huggingface.co/blog/isaacus/legal-rag-bench](https://huggingface.co/blog/isaacus/legal-rag-bench) |

### Validity and evidence

**Risks / caveats**
- Benchmark owner sells one evaluated legal embedder and reports it as strongest.
- Only 100 questions from one source manual constrain generalization; the judge is a moving hosted model.

**Verified facts**
- Official GitHub/HF/paper define the corpus, factorial protocol, exact judge, and result fields.

**Inference**
- None recorded.

**Unresolved ambiguity**
- None recorded.

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)

<a id="canlegalragbench"></a>
## CanLegalRAGBench

`canlegalragbench` · **benchmark** · **specialist** · active

Retrieve Canadian case law for realistic layperson and legal-professional queries and generate grounded answers.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Macro retrieval metrics score authority coverage/ranking; claim-level factuality compares generated atomic claims to expert answers and retrieved documents, separating answer agreement from grounding. |
| Jurisdiction | Canada, Ontario, British Columbia, Alberta, other Canadian provinces/federal courts |
| Languages | English, some French passages |
| Size | 532 queries, 3,193 gold query-document pairs, 588 unique gold documents; released corpus currently has 1,649 rows |
| Splits | One public comparative-evaluation release |
| Source | Generated realistic queries filtered by an LLM, annotated by senior law students/paralegal, with Canadian case law and limited statutes |
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
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Expert rejudging found relevant documents outside the gold set, so automatic retrieval scores undercount some valid retrievals.
- Questions were model-generated and many source rows lack explicit upstream-license metadata.

**Verified facts**
- Official GitHub/HF/paper define 532 queries, 588 gold documents, metrics, and claim-level formulas.

**Inference**
- None recorded.

**Unresolved ambiguity**
- The HF viewer shows 1,649 released corpus rows while the paper emphasizes 588 unique gold documents; these count different units.

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)
