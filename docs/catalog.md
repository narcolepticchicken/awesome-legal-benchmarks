# Full benchmark catalog

Research snapshot: **2026-08-03**. Verified facts are sourced by each entry's direct resource links; inferences and unresolved ambiguities are labeled separately.

Back to [README](../README.md).

## LegalBench

`legalbench` · **benchmark-suite** · **recommended** · active

Task-specific legal reasoning across classification, extraction, question answering, and generation.

| Field | Detail |
|---|---|
| Construct / theory | The suite operationalizes six lawyer-facing forms of legal reasoning through 162 independently authored tasks; it is a task collection, not a single latent legal-intelligence score. |
| Jurisdiction | United States, mixed/common-law |
| Languages | English |
| Size | 162 tasks; per-task instance counts vary |
| Splits | Task-defined; no unified train/dev/test split |
| Source | Expert-contributed tasks plus public legal datasets and authorities |
| Input | Prompt plus task-specific facts, rules, clauses, or questions |
| Output | Labels, spans, short answers, or generated text depending on task |
| Baselines / leaderboard context | Paper evaluates 20 open and commercial LLMs; external Vals results are not the canonical paper leaderboard. |
| Dataset access | Public |
| License | Repository/data licenses vary by contributed task |
| Gating | None for the public release |
| Maintenance | Active collaborative repository; pin a commit because tasks and harness behavior can change. |
| Reproducibility | Code, prompts, and public labels are available; cross-paper comparison requires the same task subset, prompt protocol, and model version. |

### Metrics

- **Task-defined exact match / accuracy / F1 / generation scores** — Each task supplies its own scorer; aggregate results must disclose task selection and averaging. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/HazyResearch/legalbench](https://github.com/HazyResearch/legalbench) |
| Hugging Face | [https://huggingface.co/datasets/nguha/legalbench](https://huggingface.co/datasets/nguha/legalbench) |
| Paper / arXiv | [https://arxiv.org/abs/2308.11462](https://arxiv.org/abs/2308.11462) |
| Leaderboard / competition | [https://www.vals.ai/benchmarks/legal_bench](https://www.vals.ai/benchmarks/legal_bench) |
| Project | [https://legalbench.ai/](https://legalbench.ai/) |

### Validity and evidence

**Risks / caveats**
- Public prompts and gold labels create direct contamination and overfitting risk.
- Averaging heterogeneous tasks can hide severe failures in legally important sub-capabilities.

**Verified facts**
- Official paper and repository identify 162 tasks and six reasoning categories.

**Inference**
- The suite is best used diagnostically rather than as a single legal-intelligence rank.

**Unresolved ambiguity**
- Constituent task licenses are not uniform.

Original README bullet(s): #1

## LawBench

`lawbench` · **benchmark-suite** · **recommended** · fixed-release

Chinese legal memorization, understanding, and application across 20 tasks.

| Field | Detail |
|---|---|
| Construct / theory | Tasks are arranged into memorization, understanding, and application levels, testing retrieval of legal knowledge separately from applying it to cases and generated outputs. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | 10,000 examples: 20 tasks × 500 |
| Splits | Evaluation-oriented task files; no unified hidden split |
| Source | Chinese exams and public legal NLP datasets including CAIL/JEC-QA/LAIC sources |
| Input | Task-specific JSON text, questions, facts, or documents |
| Output | Choices, labels, extracted items, numeric values, or generated text |
| Baselines / leaderboard context | Official paper compares general and legal-domain LLMs; OpenCompass hosts results. |
| Dataset access | Public GitHub release; linked HF copy is third-party |
| License | Repository license applies to code; source-dataset terms vary |
| Gating | None observed |
| Maintenance | Repository is available; use a pinned revision. |
| Reproducibility | Prompts and evaluator code are public, but there is no canonical author-owned HF dataset and source tasks have mixed provenance. Pin and inspect the scorer: parsing rules, skipped rows, and abstention handling affect the result. |

### Metrics

- **Official 20-task metric map** — 1-1 ROUGE-L; 1-2 accuracy; 2-1 F0.5; 2-2 F1; 2-3 F1; 2-4 accuracy; 2-5 character-level rc-F1; 2-6 entity soft-F1; 2-7 ROUGE-L; 2-8 accuracy; 2-9 F1; 2-10 trigger soft-F1; 3-1 F1; 3-2 ROUGE-L; 3-3 F1; 3-4 and 3-5 normalized log-distance; 3-6 accuracy; 3-7 accuracy; 3-8 ROUGE-L. Report per-task scores because the official AVG mixes unlike scales. **Primary.**
- **Normalized log-distance (3-4/3-5)** — For scorable prison-term items, score = 1 - mean(|ln(gold_months+1)-ln(pred_months+1)|)/ln(216). The evaluator uses the first parsed month value, otherwise the first year value multiplied by 12; an unparsed prediction receives distance ln(216). Gold death/life-imprisonment rows are skipped.
- **Abstention rate** — The evaluator separately reports the fraction of rows whose answer parser cannot extract a valid task-specific response. This is not folded consistently into every task score, and the 2-6 evaluator misspells its returned abstention key, so the top-level CSV records zero for that task unless corrected.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/open-compass/LawBench](https://github.com/open-compass/LawBench) |
| Hugging Face | [https://huggingface.co/datasets/doolayer/LawBench](https://huggingface.co/datasets/doolayer/LawBench) |
| Paper / arXiv | [https://arxiv.org/abs/2309.16289](https://arxiv.org/abs/2309.16289) |
| Leaderboard / competition | [https://lawbench.opencompass.org.cn/](https://lawbench.opencompass.org.cn/) |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Public exam and CAIL-derived answers create high contamination risk.
- The headline AVG arithmetically mixes heterogeneous task metrics, while task-specific parsers and inconsistent abstention handling can change scores.
- A third-party HF mirror can drift from the canonical repository.

**Verified facts**
- Official repository defines 20 tasks with 500 samples per task.
- Official README and evaluator code define the task-to-metric map, normalized log-distance, and parser-based abstention reporting.

**Inference**
- Per-task reporting is more interpretable than the heterogeneous official AVG.

**Unresolved ambiguity**
- No official canonical HF release was located.
- The official 2-6 evaluator returns the misspelled key 'anstention_rate', so the top-level evaluator silently writes zero abstention for that task.

Original README bullet(s): #2

## LexGLUE

`lexglue` · **benchmark-suite** · **recommended** · fixed-release

Standardized English legal language understanding across seven classification and judgment tasks.

| Field | Detail |
|---|---|
| Construct / theory | LexGLUE standardizes task splits and reporting across ECtHR A/B, SCOTUS, EUR-LEX, LEDGAR, UNFAIR-ToS, and CaseHOLD; it measures a portfolio of NLU tasks rather than one jurisdiction-neutral ability. |
| Jurisdiction | Council of Europe, European Union, United States, mixed contracts/terms |
| Languages | English |
| Size | Seven constituent datasets |
| Splits | Fixed task-specific train/validation/test splits |
| Source | Previously released legal datasets normalized by the LexGLUE authors |
| Input | Case facts, opinions, provisions, legislation, or terms of service |
| Output | Single/multi-label class or five-choice answer |
| Baselines / leaderboard context | Official repository reports BERT, RoBERTa, LegalBERT, hierarchical, Longformer, and BigBird baselines. |
| Dataset access | Public |
| License | CC BY 4.0 package; constituent-source rights should still be checked |
| Gating | None |
| Maintenance | Stable, widely used standardized release. |
| Reproducibility | High when task config, long-document handling, thresholds, and aggregate convention are pinned. |

### Metrics

- **Macro-F1 and micro-F1 / task accuracy** — Task-appropriate classification metrics; report each task and disclose any cross-task averaging. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/coastalcph/lex-glue](https://github.com/coastalcph/lex-glue) |
| Hugging Face | [https://huggingface.co/datasets/coastalcph/lex_glue](https://huggingface.co/datasets/coastalcph/lex_glue) |
| Paper / arXiv | [https://arxiv.org/abs/2110.00976](https://arxiv.org/abs/2110.00976)<br>[https://aclanthology.org/2022.acl-long.297/](https://aclanthology.org/2022.acl-long.297/) |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- All constituent test labels are public and likely present in model-development workflows.
- A single aggregate hides jurisdiction and task-family failures.

**Verified facts**
- Official GitHub/HF/paper define seven tasks and standardized splits.

**Inference**
- LexGLUE is a strong comparability suite, not a deployability claim.

**Unresolved ambiguity**
- None recorded.

Original README bullet(s): Curated addition.

## LEXTREME

`lextreme` · **benchmark-suite** · **recommended** · fixed-release

Multilingual European legal classification and named-entity recognition across 24 languages.

| Field | Detail |
|---|---|
| Construct / theory | Hierarchical harmonic means require balanced performance across datasets and languages: one dataset aggregate and one language aggregate are combined so a weak component depresses the final score. |
| Jurisdiction | European Union, Council of Europe, European national jurisdictions |
| Languages | 24 European languages |
| Size | 11 datasets covering 24 languages |
| Splits | Dataset-specific train/validation/test splits |
| Source | European legislation, cases, and legal NLP datasets |
| Input | Legal text or token sequence |
| Output | Document labels or entity spans/classes |
| Baselines / leaderboard context | Official paper/repository and W&B project publish multilingual transformer baselines. |
| Dataset access | Public |
| License | Constituent dataset licenses vary |
| Gating | None observed |
| Maintenance | Fixed research suite; pin repository and HF revisions. |
| Reproducibility | Good with exact language/task coverage and aggregation code. |

### Metrics

- **Macro-F1** — Base metric for every task, giving each class equal weight. **Primary.**
- **Hierarchical harmonic-mean LEXTREME score** — Compute harmonic means within dataset and language views, then the harmonic mean of those two aggregates; any near-zero component dominates downward. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/JoelNiklaus/LEXTREME](https://github.com/JoelNiklaus/LEXTREME) |
| Hugging Face | [https://huggingface.co/datasets/joelniklaus/lextreme](https://huggingface.co/datasets/joelniklaus/lextreme) |
| Paper / arXiv | [https://arxiv.org/abs/2301.13126](https://arxiv.org/abs/2301.13126) |
| Leaderboard / competition | [https://wandb.ai/lextreme/paper_results](https://wandb.ai/lextreme/paper_results) |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Missing language-task cells and very different dataset scales complicate interpretation.
- Harmonic aggregation is intentionally harsh and should accompany—not replace—per-task scores.

**Verified facts**
- Paper defines 11 datasets, 24 languages, macro-F1, and hierarchical harmonic aggregation.

**Inference**
- None recorded.

**Unresolved ambiguity**
- None recorded.

Original README bullet(s): Curated addition.

## LEXam

`lexam` · **benchmark** · **recommended** · active

Answer bilingual law-school multiple-choice and open-answer examination questions.

| Field | Detail |
|---|---|
| Construct / theory | MCQ accuracy measures answer selection; open-answer ensemble judging estimates substantive coverage against references, making judge version and rubric part of the instrument. |
| Jurisdiction | Germany, United States / English-language courses, mixed law-school curricula |
| Languages | English, German |
| Size | 7,537 questions from 340 exams and 116 courses: 2,841 open-answer and 4,696 MCQ |
| Splits | Versioned JSON release; no single training split is required |
| Source | University law examinations and course materials |
| Input | Question, optional choices, and metadata |
| Output | Choice or open-form answer |
| Baselines / leaderboard context | Official results compare broad frontier/open models; project site tracks benchmark resources. |
| Dataset access | Public |
| License | CC BY 4.0 data; Apache-2.0 code |
| Gating | None |
| Maintenance | Active versioned benchmark; item count changed from an earlier 4,886-item release. |
| Reproducibility | Good when dataset revision, prompts, judge ensemble, and model endpoints are pinned. |

### Metrics

- **MCQ accuracy** — Exact selected-option correctness. **Primary.**
- **Open-answer judge ensemble** — Multiple LLM judges score generated answers against references; record judge model versions and aggregation. Judge: Versioned ensemble documented by LEXam. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/LEXam-Benchmark/LEXam](https://github.com/LEXam-Benchmark/LEXam) |
| Hugging Face | [https://huggingface.co/datasets/LEXam-Benchmark/LEXam](https://huggingface.co/datasets/LEXam-Benchmark/LEXam) |
| Paper / arXiv | [https://arxiv.org/abs/2505.12864](https://arxiv.org/abs/2505.12864) |
| Leaderboard / competition | None |
| Project | [https://lexam-benchmark.github.io/](https://lexam-benchmark.github.io/) |

### Validity and evidence

**Risks / caveats**
- Public exams and answers are contamination-prone.
- Open-answer rankings can move when hosted judges or ensemble membership changes.

**Verified facts**
- Official GitHub/HF/project sources agree on the current 7,537-question release.

**Inference**
- None recorded.

**Unresolved ambiguity**
- Jurisdiction is course-dependent rather than a single national-law corpus.

Original README bullet(s): #11

## LexEval

`lexeval` · **benchmark-suite** · **specialist** · fixed-release

Chinese legal knowledge, inference, generation, discrimination, and ethics across 23 tasks.

| Field | Detail |
|---|---|
| Construct / theory | Six ability groups broaden evaluation beyond exams, but accuracy and ROUGE-L remain task proxies rather than a validated unidimensional legal-capability scale. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | 14,150 questions across 23 tasks and six ability groups |
| Splits | Evaluation collection; mostly multiple choice plus generation |
| Source | Chinese legal exams, public datasets, authored and transformed tasks |
| Input | Questions, facts, choices, or generation prompts |
| Output | Choice/label or generated legal text |
| Baselines / leaderboard context | Official paper evaluates general and legal-domain LLMs; the historical Collam site is not a stable leaderboard. |
| Dataset access | Public |
| License | MIT repository; verify constituent-source terms |
| Gating | None observed |
| Maintenance | Research release; claims of continuous updating are not a substitute for semantic versions. |
| Reproducibility | Public prompts and data support reruns; pin task revision and generation decoding. |

### Metrics

- **Accuracy** — Exact option/label correctness for closed-form tasks. **Primary.**
- **ROUGE-L** — Longest-common-subsequence overlap for generated answers.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/CSHaitao/LexEval](https://github.com/CSHaitao/LexEval) |
| Hugging Face | [https://huggingface.co/datasets/CSHaitao/LexEval](https://huggingface.co/datasets/CSHaitao/LexEval) |
| Paper / arXiv | [https://arxiv.org/abs/2409.20288](https://arxiv.org/abs/2409.20288) |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Public exams and answers are highly contamination-prone.
- ROUGE-L can reward surface overlap without legal validity.

**Verified facts**
- Official repository and paper define 14,150 questions and 23 tasks.

**Inference**
- None recorded.

**Unresolved ambiguity**
- No stable current official leaderboard or project page was verified; the historical Collam hostname currently fails TLS validation.

Original README bullet(s): #12

## ArabLegalEval

`arablegaleval` · **benchmark-suite** · **evaluate carefully** · active

Arabic legal knowledge, classification, question answering, and translation, with substantial Saudi-law coverage.

| Field | Detail |
|---|---|
| Construct / theory | The suite combines local and translated tasks; task scores therefore mix Arabic legal competence, general task performance, and translation artifacts. |
| Jurisdiction | Saudi Arabia, Arab jurisdictions / translated sources |
| Languages | Arabic, English |
| Size | HF card exposes about 15.3k ArLegalBench rows, 11.6k MCQs, and 79 QA rows |
| Splits | Configuration-specific |
| Source | Local legal material, translated benchmarks, and synthetic items |
| Input | Arabic questions, text, choices, or translation prompts |
| Output | Labels, choices, answers, or translations |
| Baselines / leaderboard context | Paper evaluates Arabic-capable and frontier LLMs across configurations. |
| Dataset access | Public HF release |
| License | No single clear unified code/data license located |
| Gating | None observed |
| Maintenance | HF and GitHub artifacts exist; pin revision because configurations have evolved. |
| Reproducibility | Mixed: public data, but judge/model versions and configuration counts require careful pinning. |

### Metrics

- **Accuracy / F1 / ROUGE** — Task-specific closed-form and overlap metrics. **Primary.**
- **LLM and human ratings** — GPT-4-style judge scores for some generation plus human translation ratings; record the exact judge prompt/model. Judge: Task-dependent, including GPT-4.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/Thiqah/ArabLegalEval](https://github.com/Thiqah/ArabLegalEval) |
| Hugging Face | [https://huggingface.co/datasets/THIQAH-RD/ArabLegalEval](https://huggingface.co/datasets/THIQAH-RD/ArabLegalEval) |
| Paper / arXiv | [https://arxiv.org/abs/2408.07983](https://arxiv.org/abs/2408.07983) |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Synthetic GPT-4/Claude items and translated tasks can introduce generator artifacts.
- The QA component is very small relative to the multiple-choice collection.

**Verified facts**
- Official organization GitHub/HF and paper establish the suite identity.

**Inference**
- None recorded.

**Unresolved ambiguity**
- A unified release-wide license was not found.

Original README bullet(s): #13

## IL-TUR

`il-tur` · **benchmark-suite** · **recommended** · active

Indian legal named entities, rhetorical roles, judgment/explanation, bail, statute identification, precedent retrieval, summarization, and translation.

| Field | Detail |
|---|---|
| Construct / theory | Eight task-specific datasets cover legal understanding and production; strict/macro/micro F1, retrieval F1@k, generation overlap, and translation metrics should be read per task, not as one legal score. |
| Jurisdiction | India |
| Languages | English, Hindi, Bengali, Gujarati, Marathi, Malayalam, Odia, Punjabi, Tamil, Telugu |
| Size | Eight tasks; examples include 105 NER opinions, 21,184 rhetorical-role sentences, and 34k+ judgment documents |
| Splits | Task-specific folds and train/dev/test files |
| Source | Indian Supreme/High Court cases, statutes, summaries, and MILPaC parallel text |
| Input | Legal document, query case, or English translation source |
| Output | Entities, roles, labels, salient sentences, statutes/cases, summary, or translation |
| Baselines / leaderboard context | Official paper/repository provide task-specific neural, transformer, and LLM baselines plus a leaderboard. |
| Dataset access | HF repository is public but gated by contact-information acceptance |
| License | CC BY-NC-SA 4.0 |
| Gating | HF terms acceptance required |
| Maintenance | Active unified HF distribution layered over task-specific sources. |
| Reproducibility | Good after access approval, but each task's original source, split, and evaluator must be retained. |

### Metrics

- **Strict macro-F1 / macro-F1 / micro-F1@k** — NER, classification, and retrieval tasks use the official task-specific F1 aggregation. **Primary.**
- **ROUGE-L / BERTScore / BLEU / GLEU / chrF++** — Explanation, summarization, and translation use reference-overlap/semantic metrics. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/Exploration-Lab/IL-TUR](https://github.com/Exploration-Lab/IL-TUR) |
| Hugging Face | [https://huggingface.co/datasets/Exploration-Lab/IL-TUR](https://huggingface.co/datasets/Exploration-Lab/IL-TUR) |
| Paper / arXiv | [https://arxiv.org/abs/2407.05399](https://arxiv.org/abs/2407.05399)<br>[https://aclanthology.org/2024.acl-long.618/](https://aclanthology.org/2024.acl-long.618/) |
| Leaderboard / competition | [https://exploration-lab.github.io/IL-TUR/](https://exploration-lab.github.io/IL-TUR/) |
| Project | [https://exploration-lab.github.io/IL-TUR/](https://exploration-lab.github.io/IL-TUR/) |

### Validity and evidence

**Risks / caveats**
- The suite re-bundles existing datasets, so results are not independent evidence from those components.
- Task sizes and language coverage are highly uneven.

**Verified facts**
- Official GitHub/HF/project/paper define eight tasks and exact task metrics.

**Inference**
- None recorded.

**Unresolved ambiguity**
- HF metadata cites MILPaC arXiv alongside the IL-TUR paper; cite both appropriately.

Original README bullet(s): Curated addition.

## Korean Canonical Legal Benchmark

`kcl` · **benchmark-suite** · **recommended** · active

Answer Korean bar-exam MCQs and essays with question-aligned supporting precedents.

| Field | Detail |
|---|---|
| Construct / theory | Providing supporting precedents is designed to reduce dependence on memorized Korean law and expose reasoning; MCQ exactness and weighted instance rubrics then score application. |
| Jurisdiction | South Korea |
| Languages | Korean |
| Size | KCL-MCQA: 283 questions and 1,103 precedents; KCL-Essay: 169 questions, 550 precedents, 2,739 rubrics |
| Splits | Evaluation variants with and without supporting precedents |
| Source | 2021–2025 Korean Bar Exam questions, expert commentaries, and retrieved precedents |
| Input | Question/options or essay problem, optionally with precedents |
| Output | Five-choice answer or legal essay |
| Baselines / leaderboard context | Paper evaluates 30+ Korean/multilingual, general/reasoning, open/API models. |
| Dataset access | Public |
| License | CC BY-NC 4.0 with KOGL/source constraints noted by the release |
| Gating | None observed |
| Maintenance | Active EACL 2026 release. |
| Reproducibility | Good with official prompts/rubrics and pinned Gemini judge; API drift remains. |

### Metrics

- **MCQ accuracy** — Exact five-choice accuracy, reported with and without precedents. **Primary.**
- **Weighted rubric percentage** — Instance rubrics inherit each official essay's points; earned points are divided by 2,905 total benchmark points. Judge: Gemini 2.5 Flash. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/lbox-kr/kcl](https://github.com/lbox-kr/kcl) |
| Hugging Face | [https://huggingface.co/datasets/lbox/kcl](https://huggingface.co/datasets/lbox/kcl) |
| Paper / arXiv | [https://arxiv.org/abs/2512.24572](https://arxiv.org/abs/2512.24572)<br>[https://aclanthology.org/2026.eacl-short.17/](https://aclanthology.org/2026.eacl-short.17/) |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- The essay judge helped generate rubric sets, creating model-family dependence despite attorney review.
- Question-aligned precedents reduce knowledge load but may make retrieval unrealistically solved.

**Verified facts**
- Official paper/GitHub/HF define counts, 2,905-point aggregation, and Gemini 2.5 Flash judge.

**Inference**
- None recorded.

**Unresolved ambiguity**
- None recorded.

Original README bullet(s): Curated addition.

## Massive Legal Embedding Benchmark

`mleb` · **benchmark-suite** · **specialist** · active

Legal embedding quality across retrieval, retrieval-augmented QA, and zero-shot classification tasks.

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

- **nDCG@10** — Discounted graded gain at rank 10, normalized by the ideal ranking; constituent tasks may add QA/classification metrics. **Primary.**

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

Original README bullet(s): #3, #20

## LegalBench-RAG

`legalbench-rag` · **benchmark** · **recommended** · fixed-release

Retrieve exact supporting spans from long legal and policy documents.

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

- **Character precision and recall** — Overlap between predicted and reference character sets, exposing both missed support and context bloat. **Primary.**

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

Original README bullet(s): #9

## Belgian Statutory Article Retrieval Dataset

`bsard` · **benchmark** · **recommended** · fixed-release

Retrieve Belgian statutory articles relevant to a legal question.

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

- **Recall@k** — Fraction of gold relevant articles retrieved by cutoff k. **Primary.**
- **MAP / MRR** — MAP averages precision at all relevant ranks; MRR uses reciprocal rank of the first relevant article.

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

Original README bullet(s): Curated addition.

## LLeQA

`lleqa` · **benchmark** · **specialist** · fixed-release

Retrieve Belgian legal authorities and generate long-form answers to practitioner-style questions.

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

- **Recall@k / MRR** — Retrieval coverage and first-relevant rank. **Primary.**
- **ROUGE / METEOR / BERTScore** — Reference-overlap and semantic-similarity metrics for generated answers; human/grounding checks should accompany them.

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

Original README bullet(s): Curated addition.

## CLERC

`clerc` · **benchmark** · **specialist** · fixed-release

Retrieve US case-law evidence and generate citation-grounded legal text.

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

- **Recall@k (including Recall@1000)** — Share of gold cited/relevant cases present by cutoff; paper reports a 48.3% zero-shot Recall@1000 result for a leading setting. **Primary.**
- **ROUGE and citation/hallucination metrics** — Generation overlap plus whether generated citations/support are valid under the paper protocol.

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

Original README bullet(s): Curated addition.

## Reasoning-Focused Legal Retrieval Benchmark

`reglab-reasoning-focused-retrieval` · **benchmark-suite** · **recommended** · fixed-release

Retrieve controlling text for legal questions whose answer has low lexical overlap with the relevant source.

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

- **Recall@k / MRR@10** — Evidence coverage by cutoff and reciprocal rank of first relevant passage. **Primary.**
- **Downstream QA accuracy** — Answer correctness when the retriever's evidence is supplied to the QA model.

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

Original README bullet(s): Curated addition.

## LeCaRDv2

`lecardv2` · **benchmark** · **recommended** · fixed-release

Retrieve legally similar Chinese criminal cases using graded relevance across characterization, penalty, and procedure.

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

- **Recall@100/200/500/1000** — Coverage of judged relevant cases at first-stage retrieval cutoffs. **Primary.**
- **nDCG / precision at k** — Graded ranking quality and top-result relevance for reranking settings.

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

Original README bullet(s): Curated addition.

## Competition on Legal Information Extraction/Entailment

`coliee` · **shared-task** · **recommended** · annual

Retrieve and recognize entailment among Canadian cases and Japanese civil-code provisions.

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

- **Precision / recall / F1** — Official task scripts score retrieved cases/statutes and entailment selections; exact primary metric varies by task/year. **Primary.**
- **Accuracy** — Used for binary statutory entailment/answer tasks where specified by the year's rules.

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

Original README bullet(s): Curated addition.

## Legal RAG Bench

`legal-rag-bench` · **benchmark** · **evaluate carefully** · active

Evaluate an end-to-end legal RAG pipeline and attribute errors to retrieval versus generation.

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

- **Retrieval accuracy** — Whether the gold relevant passage appears in retrieved context at configured k (default k=5 in the released run). **Primary.**
- **Correctness / groundedness** — Binary LLM judgments against the human answer and provided context, reported per factorial cell. Judge: GPT-5.2 high-reasoning in released code. **Primary.**

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

Original README bullet(s): Curated addition.

## CanLegalRAGBench

`canlegalragbench` · **benchmark** · **specialist** · active

Retrieve Canadian case law for realistic layperson and legal-professional queries and generate grounded answers.

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

- **Macro Recall@10 / nDCG@10** — Per-query recall and graded/binary ranking quality averaged equally across 532 queries; MRR and @25 variants are also reported. **Primary.**
- **Claim accuracy / groundedness** — Gemini-2.5-Pro decomposes answers into atomic claims and judges entailment against gold-answer claims or retrieved documents, FActScore-style. Judge: Gemini 2.5 Pro via Ragas-style pipeline. **Primary.**

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

Original README bullet(s): Curated addition.

## Contract Understanding Atticus Dataset

`cuad` · **benchmark** · **recommended** · fixed-release

Locate 41 categories of commercially important clauses in long contracts.

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

- **Token intersection-over-union (Jaccard)** — |predicted-token set ∩ gold-token set| / |union|, with precision/recall and AUPR across confidence thresholds. **Primary.**
- **AUPR** — Area under the precision–recall curve over clause predictions, useful under strong class imbalance.

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

Original README bullet(s): #4

## LEDGAR

`ledgar` · **dataset** · **specialist** · fixed-release

Classify contract provisions into clause/topic labels.

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

- **Micro-F1 and macro-F1** — Micro pools all label decisions; macro averages per-label F1 so rare labels have equal weight. **Primary.**

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

Original README bullet(s): #5

## ContractNLI

`contractnli` · **benchmark** · **recommended** · fixed-release

Determine whether a non-disclosure agreement entails, contradicts, or does not mention a fixed legal hypothesis and identify supporting evidence.

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

- **Micro/macro F1 for NLI** — F1 over the three labels with stated aggregation. **Primary.**
- **Evidence identification F1** — Overlap/classification F1 over evidence spans or sentence selections. **Primary.**

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

Original README bullet(s): Curated addition.

## Merger Agreement Understanding Dataset

`maud` · **benchmark** · **recommended** · fixed-release

Answer fine-grained questions about merger-agreement provisions.

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

- **Micro-F1 and macro-F1** — Micro summarizes all decisions; macro weights each question/label class equally. **Primary.**

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

Original README bullet(s): Curated addition.

## Atticus Clause Retrieval Dataset

`acord` · **benchmark** · **recommended** · fixed-release

Rank precedent contract clauses for an attorney-written drafting need.

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

- **nDCG@5 and nDCG@10** — Discounted cumulative gain over 0–4 relevance, normalized by the ideal ranking. **Primary.**
- **3/4/5-star precision@5** — Precision among top five at progressively stricter attorney-rating thresholds. **Primary.**

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

Original README bullet(s): Curated addition.

## ContractEval

`contracteval` · **evaluation-protocol** · **related—not a comparable public benchmark** · fixed-release

Evaluate long-context LLM clause-risk extraction on the public CUAD test set.

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

- **F1 / F2 / Jaccard** — Overlap scores; F2 weights recall twice as strongly as precision. **Primary.**
- **False no-related-clause rate** — Share of positive items incorrectly rejected as containing no relevant clause.

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

Original README bullet(s): #15

## RedlineBench

`redlinebench` · **benchmark** · **evaluate carefully** · active

Negotiate commercial contracts over four turns by producing native Word tracked changes and comments.

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

- **Redline overall (0–100)** — Per task clamp((earned − penalty)/total positive rubric weight); average within identical-input groups, then equally average 12 scenario×turn cells. Judge: LLM judge panel against attorney-authored weighted rubrics. **Primary.**
- **Five dimension scores** — Commercial context, legal correctness, negotiation quality, deal-closing orientation, and counterparty-acceptance prediction. Judge: LLM judge panel.

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

Original README bullet(s): Curated addition.

## ECtHR Tasks A/B

`ecthr` · **benchmark** · **recommended** · fixed-release

Predict European Convention articles alleged (Task A) or found violated (Task B) from case facts.

| Field | Detail |
|---|---|
| Construct / theory | Multi-label outcome prediction tests fact-to-doctrine mapping; macro-F1 emphasizes less frequent Convention articles and micro-F1 the total decision mass. |
| Jurisdiction | European Court of Human Rights / Council of Europe |
| Languages | English |
| Size | Roughly 11,000 cases per LexGLUE Task A/B configuration |
| Splits | Commonly 9,000 train / 1,000 validation / 1,000 test |
| Source | Public ECtHR judgments and case facts |
| Input | Case-fact section |
| Output | Multi-label Convention article IDs |
| Baselines / leaderboard context | Original Chalkidis et al. work and LexGLUE report transformer and long-document baselines. |
| Dataset access | Public LexGLUE configs ecthr_a and ecthr_b |
| License | LexGLUE package CC BY 4.0 |
| Gating | None |
| Maintenance | Stable LexGLUE release; the older coastalcph/ecthr_cases HF path is stale. |
| Reproducibility | Good with the exact task config, long-document truncation strategy, and thresholding specified. |

### Metrics

- **Micro-F1 and macro-F1** — F1 is computed over article labels with micro and label-macro aggregation. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/coastalcph/lex-glue](https://github.com/coastalcph/lex-glue) |
| Hugging Face | [https://huggingface.co/datasets/coastalcph/lex_glue](https://huggingface.co/datasets/coastalcph/lex_glue) |
| Paper / arXiv | [https://arxiv.org/abs/1906.02059](https://arxiv.org/abs/1906.02059)<br>[https://arxiv.org/abs/2110.00976](https://arxiv.org/abs/2110.00976) |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Judgments and labels are public and likely represented in pretraining corpora.
- Outcome labels can be learned from stylistic or temporal shortcuts rather than legal reasoning.

**Verified facts**
- LexGLUE is the current canonical distribution path.

**Inference**
- None recorded.

**Unresolved ambiguity**
- Counts vary slightly across original and standardized releases.

Original README bullet(s): #6

## FairLex

`fairlex` · **benchmark-suite** · **recommended** · fixed-release

Evaluate legal prediction performance and group robustness across sensitive or legally salient subpopulations.

| Field | Detail |
|---|---|
| Construct / theory | FairLex pairs overall macro-F1 with worst-group and disparity views; fairness is operationalized as performance robustness across observed demographic/geographic/legal groups, not demographic parity of decisions. |
| Jurisdiction | Council of Europe, United States, Switzerland, China |
| Languages | English, German, French, Italian, Chinese |
| Size | Four legal datasets |
| Splits | WILDS-style distribution and group-aware splits/configs |
| Source | Court decisions with gender, age, region, language, and legal-area attributes where available |
| Input | Case/document text |
| Output | Outcome or legal label |
| Baselines / leaderboard context | Official code evaluates standard, reweighting, and robustness/fairness methods. |
| Dataset access | Public package |
| License | Dataset/config-specific; inspect constituent terms |
| Gating | None observed |
| Maintenance | Stable research release. |
| Reproducibility | Good when subgroup definitions, minimum group sizes, and random seeds are retained. |

### Metrics

- **All-group macro-F1** — Macro-F1 over the full evaluation population. **Primary.**
- **Worst-group macro-F1 / group disparity** — Minimum subgroup performance and gaps across specified protected/context groups. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/coastalcph/fairlex](https://github.com/coastalcph/fairlex) |
| Hugging Face | [https://huggingface.co/datasets/coastalcph/fairlex](https://huggingface.co/datasets/coastalcph/fairlex) |
| Paper / arXiv | [https://aclanthology.org/2022.acl-long.301/](https://aclanthology.org/2022.acl-long.301/) |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Observed metadata are imperfect proxies for legally meaningful disadvantage.
- Worst-group estimates can be high variance for small groups.

**Verified facts**
- Official paper/repository cover four jurisdictions and five languages with group-robustness metrics.

**Inference**
- None recorded.

**Unresolved ambiguity**
- None recorded.

Original README bullet(s): Curated addition.

## CaseHOLD

`casehold` · **benchmark** · **specialist** · fixed-release

Select the correct holding that completes an excerpt from a US judicial opinion.

| Field | Detail |
|---|---|
| Construct / theory | Five-choice accuracy measures discrimination of the true legal holding from hard negatives generated/retrieved to resemble plausible case law. |
| Jurisdiction | United States |
| Languages | English |
| Size | More than 53,000 five-choice questions |
| Splits | Official train/dev/test files; also standardized in LexGLUE |
| Source | US case law and extracted holdings |
| Input | Opinion excerpt plus five candidate holdings |
| Output | Correct option |
| Baselines / leaderboard context | Legal-BERT and other pretrained language models in the original paper; further baselines in LexGLUE. |
| Dataset access | Public |
| License | Release/derived case-law terms apply; LexGLUE package CC BY 4.0 |
| Gating | None |
| Maintenance | Stable; LexGLUE is the easiest standardized distribution. |
| Reproducibility | High for exact-choice scoring with the same variant and split. |

### Metrics

- **Accuracy** — Exact five-way choice accuracy. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/neelguha/legal-ml-datasets](https://github.com/neelguha/legal-ml-datasets)<br>[https://github.com/coastalcph/lex-glue](https://github.com/coastalcph/lex-glue) |
| Hugging Face | [https://huggingface.co/datasets/coastalcph/lex_glue](https://huggingface.co/datasets/coastalcph/lex_glue) |
| Paper / arXiv | [https://arxiv.org/abs/2104.08671](https://arxiv.org/abs/2104.08671) |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Public US opinions and fixed distractors are contamination-prone.
- Models may exploit distractor-generation artifacts rather than legal reasoning.

**Verified facts**
- Original dataset repo/paper and LexGLUE establish the canonical task.

**Inference**
- None recorded.

**Unresolved ambiguity**
- A separate current author-owned HF dataset was not located outside LexGLUE.

Original README bullet(s): Curated addition.

## DeonticBench

`deonticbench` · **benchmark-suite** · **recommended** · active

Reason about obligations, permissions, prohibitions, eligibility, and amounts under long legal/policy rules, directly or through executable Prolog.

| Field | Detail |
|---|---|
| Construct / theory | Exact outcomes test rule application; executable reference programs expose a symbolic proof path and distinguish wrong legal formalization, solver failure, abstention, and wrong final answer. |
| Jurisdiction | United States federal tax, United States immigration, United States state housing, Airline policies |
| Languages | English, Prolog |
| Size | 6,232 whole-set tasks: SARA Numeric 100, SARA Binary 276, Airline 300, Housing 5,314, USCIS-AAO 242 |
| Splits | Whole plus curated hard subsets (35/30/80/78/28) and derived five-case smoke splits |
| Source | US tax statutes, airline policies, state housing law, and USCIS AAO decisions with audited reference Prolog |
| Input | Rules/statutes, case facts, and a question |
| Output | Typed answer directly or generated Prolog program and solver result |
| Baselines / leaderboard context | Paper/repository evaluate direct, zero-shot Prolog, and few-shot Prolog across frontier/coding models and training methods. |
| Dataset access | Public |
| License | See official repository/HF metadata and constituent-source terms |
| Gating | None for data; API models may require credentials |
| Maintenance | Active; reference programs were audited/corrected on 2026-05-26. |
| Reproducibility | Strong executable oracle and bootstrap script; pin post-audit dataset revision, SWI-Prolog, prompts, and model versions. |

### Metrics

- **Bootstrapped accuracy with 95% CI** — 1,000 case-resampling replicates; one generation sampled per case. Numeric domains allow ±1 rounding tolerance; categorical domains require exact match. **Primary.**
- **Abstention and wrong rate** — Empty/error/timeout Prolog or unparsable direct answer counts as abstention; remaining incorrect parses count wrong.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/guangyaodou/DeonticBench](https://github.com/guangyaodou/DeonticBench) |
| Hugging Face | [https://huggingface.co/datasets/gydou/DeonticBench](https://huggingface.co/datasets/gydou/DeonticBench) |
| Paper / arXiv | [https://arxiv.org/abs/2604.04443](https://arxiv.org/abs/2604.04443) |
| Leaderboard / competition | None |
| Project | [https://guangyaodou.github.io/DeonticBench/](https://guangyaodou.github.io/DeonticBench/) |

### Validity and evidence

**Risks / caveats**
- The hard split is a subset of the public whole set, so benchmark-targeted training is possible.
- Reference Prolog was materially corrected after release, proving revision pinning is essential.

**Verified facts**
- Official GitHub/HF/paper provide all domain counts, splits, solver workflow, and bootstrap protocol.

**Inference**
- Executable traces improve diagnosability but do not guarantee the formalization captures every legally relevant ambiguity.

**Unresolved ambiguity**
- None recorded.

Original README bullet(s): Curated addition.

## ALARB

`alarb` · **dataset** · **evaluate carefully** · fixed-release

Reason over Saudi commercial-law cases, complete arguments, and identify governing statutory articles.

| Field | Detail |
|---|---|
| Construct / theory | Verdict/argument generation is judged for correctness and partial correctness, while article selection uses MCQ accuracy; the protocol mixes open and closed-form constructs. |
| Jurisdiction | Saudi Arabia |
| Languages | Arabic |
| Size | 13,344 cases linked to eight statutes; reported experiments use 1,329 cases and 1,159 MCQs per article task |
| Splits | HF exposes a release without a clearly isolated hidden test |
| Source | Saudi commercial cases and statutes, restructured with LLM assistance |
| Input | Case facts/reasoning context or article question |
| Output | Verdict/reasoning text or selected article |
| Baselines / leaderboard context | Paper evaluates multiple Arabic/general LLMs. |
| Dataset access | Public HF release |
| License | HF metadata: Apache-2.0 |
| Gating | None observed |
| Maintenance | Fixed research release; no canonical GitHub repository located. |
| Reproducibility | Data are inspectable, but hosted-judge drift and absence of a hidden split limit strict reproduction. |

### Metrics

- **Correct / partial / incorrect judge score** — GPT-4o categorizes generated legal outputs against references. Judge: GPT-4o. **Primary.**
- **MCQ accuracy** — Exact statutory-article choice. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | None |
| Hugging Face | [https://huggingface.co/datasets/THIQAH-RD/ALARB](https://huggingface.co/datasets/THIQAH-RD/ALARB) |
| Paper / arXiv | [https://arxiv.org/abs/2510.00694](https://arxiv.org/abs/2510.00694) |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- LLM-assisted restructuring and mapping can propagate annotation errors.
- Public cases, labels, and references permit contamination and evaluation-set training.

**Verified facts**
- Paper and THIQAH-RD HF release identify the dataset.

**Inference**
- None recorded.

**Unresolved ambiguity**
- No canonical GitHub or independent leaderboard was found.

Original README bullet(s): #14

## MSLR-Bench

`mslr` · **benchmark** · **evaluate carefully** · active

Extract structured facts and produce IRAC-style reasoning for Chinese insider-trading cases.

| Field | Detail |
|---|---|
| Construct / theory | Field-level extraction metrics test factual structure; IRAC recall and an LLM judge test whether generated analysis covers expected legal reasoning components. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | 1,389 cases from 2005–2024 with 59,771 fields |
| Splits | HF visibly exposes one train split |
| Source | Public Chinese insider-trading enforcement/case materials |
| Input | Case documents |
| Output | Structured JSON fields and free-text IRAC analysis |
| Baselines / leaderboard context | Official paper compares general and legal LLMs; headline percentages must be tied to a named metric. |
| Dataset access | Public |
| License | GitHub Apache-2.0 versus HF MIT metadata conflict |
| Gating | None observed |
| Maintenance | Active recent release. |
| Reproducibility | Public artifacts exist, but split isolation, license metadata, and judge version require resolution. |

### Metrics

- **Field accuracy / FCR** — Exact or normalized field correctness plus the paper's field-completion/consistency measure. **Primary.**
- **IRAC Recall and judge score** — Recall of expected IRAC elements plus LLM evaluation of generated reasoning. Judge: DeepSeek-V3. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/yuwenhan07/MSLR-Bench](https://github.com/yuwenhan07/MSLR-Bench) |
| Hugging Face | [https://huggingface.co/datasets/Yuwh07/MSLR-Bench](https://huggingface.co/datasets/Yuwh07/MSLR-Bench) |
| Paper / arXiv | [https://arxiv.org/abs/2511.07979](https://arxiv.org/abs/2511.07979) |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- One visible split allows accidental train/evaluation overlap.
- Public cases and a single LLM judge create contamination and evaluator-bias risk.

**Verified facts**
- Official GitHub/HF/paper agree on the case/field scale.

**Inference**
- None recorded.

**Unresolved ambiguity**
- Repository and HF licenses conflict; no hidden held-out split was verified.

Original README bullet(s): #16

## MASLegalBench

`maslegalbench` · **benchmark** · **evaluate carefully** · fixed-release

Multi-agent deductive reasoning about GDPR enforcement facts, rules, application, common sense, and conclusions.

| Field | Detail |
|---|---|
| Construct / theory | Accuracy measures final MCQ correctness; retrieval-at-k tests evidence acquisition; refusal and agreement statistics diagnose coordination rather than legal validity directly. |
| Jurisdiction | United Kingdom / GDPR enforcement |
| Languages | English |
| Size | 950 MCQs from 15 UK enforcement reports: 647 yes/no and 303 four-choice |
| Splits | Public evaluation collection |
| Source | Fifteen UK regulatory enforcement reports; questions generated with DeepSeek and reviewed |
| Input | Question plus retrievable report chunks |
| Output | Choice/yes-no answer and multi-agent traces |
| Baselines / leaderboard context | Paper compares single- and multi-agent configurations. |
| Dataset access | Public research release |
| License | MIT |
| Gating | Model APIs may be needed |
| Maintenance | Fixed recent research release. |
| Reproducibility | Prompts/code are public; hosted models and multi-agent stochasticity need repeated trials. |

### Metrics

- **Accuracy / refusal rate** — Exact final answer correctness and share of non-answers. **Primary.**
- **Retrieval@1/3/5 and Cohen's kappa** — Evidence-hit rates plus agent/human agreement statistics.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/HKUST-KnowComp/MASLegalBench](https://github.com/HKUST-KnowComp/MASLegalBench) |
| Hugging Face | None |
| Paper / arXiv | [https://arxiv.org/abs/2509.24922](https://arxiv.org/abs/2509.24922) |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Only 15 source reports sharply limit source diversity.
- Generator-authored questions can encode DeepSeek artifacts and source overlap.

**Verified facts**
- Official paper/repository define 950 questions and the 647/303 split.

**Inference**
- None recorded.

**Unresolved ambiguity**
- None recorded.

Original README bullet(s): #17

## LegalAgentBench

`legalagentbench` · **benchmark** · **specialist** · fixed-release

Chinese legal tool use, multi-hop information gathering, and legal writing.

| Field | Detail |
|---|---|
| Construct / theory | Success and progress scores estimate whether an agent selects and sequences tools toward a task; BERTScore assesses writing similarity, but neither alone proves legal correctness. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | 17 corpora, 37 tools, 300 tasks |
| Splits | Tasks span one-to-five-hop and writing categories |
| Source | Chinese legal corpora wrapped as tools and authored tasks |
| Input | Natural-language task plus tool environment |
| Output | JSON tool calls and a final legal answer or document |
| Baselines / leaderboard context | Paper compares multiple LLM agents and prompting configurations. |
| Dataset access | Public code, data, prompts, and environment |
| License | MIT repository |
| Gating | Model/API credentials may be needed to run baselines |
| Maintenance | Fixed research release. |
| Reproducibility | Harness is public; API model drift and environment dependencies still affect trajectories. |

### Metrics

- **Keyword success rate / progress rate** — Rule-based matching of required milestones and final keywords across task trajectories. **Primary.**
- **BERTScore** — Contextual token similarity for generated legal writing; token use is also reported.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/CSHaitao/LegalAgentBench](https://github.com/CSHaitao/LegalAgentBench) |
| Hugging Face | None |
| Paper / arXiv | [https://arxiv.org/abs/2412.17259](https://arxiv.org/abs/2412.17259) |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Keyword graders can be gamed without producing a legally adequate result.
- Public solutions and tool corpora permit benchmark-specific planning.

**Verified facts**
- Official repository specifies 17 corpora, 37 tools, and 300 tasks.

**Inference**
- Use as a tool-use benchmark with legal grounding checks, not as proof of deployable lawyering.

**Unresolved ambiguity**
- None recorded.

Original README bullet(s): #10

## Ready Jurist One

`ready-jurist-one` · **benchmark** · **specialist** · active

Operate interactively in Chinese legal consultation, drafting, civil-court, and criminal-court environments.

| Field | Detail |
|---|---|
| Construct / theory | J1-EVAL uses dual outcome- and process-oriented scoring so an agent must reach the right result and follow required procedural steps, formats, reasoning, and citation constraints. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | Paper reports 508 environments across six scenarios and three levels |
| Splits | Scenario/level-specific interactive environments |
| Source | Chinese judgments and legal articles, structured into role-based environments |
| Input | Multi-turn role interactions, facts, and procedural state |
| Output | Answers, complaints/defences, courtroom actions, reasons, citations, and judgments |
| Baselines / leaderboard context | Official paper evaluates 17 general, open, and legal-specific agents; OpenCompass integration is linked. |
| Dataset access | Public code/data links |
| License | No clear repository license was visible in the primary GitHub page |
| Gating | API models and significant compute may be required |
| Maintenance | Active ACL 2026 release. |
| Reproducibility | Harness and data are public, but simulator/judge model drift and stochastic multi-agent interaction require repeated trials. |

### Metrics

- **Outcome-oriented scores** — Binary/non-binary answer score, component document score, judgment score, crime accuracy, and normalized-log penalty deviation. Judge: Rule-based plus task-specific LLM judges. **Primary.**
- **Process-oriented scores** — Format following, procedural stage completeness, reasoning quality, and cited-law precision; except procedural completeness, metrics use explicit references. Judge: Rule-based plus task-specific LLM judges. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/FudanDISC/J1Bench](https://github.com/FudanDISC/J1Bench) |
| Hugging Face | [https://huggingface.co/datasets/CimoInkPool/J1-Eval_Dataset](https://huggingface.co/datasets/CimoInkPool/J1-Eval_Dataset) |
| Paper / arXiv | [https://arxiv.org/abs/2507.04037](https://arxiv.org/abs/2507.04037)<br>[https://aclanthology.org/2026.acl-long.471/](https://aclanthology.org/2026.acl-long.471/) |
| Leaderboard / competition | [https://hub.opencompass.org.cn/dataset-detail/J1Bench](https://hub.opencompass.org.cn/dataset-detail/J1Bench) |
| Project | [https://j1bench.github.io/](https://j1bench.github.io/) |

### Validity and evidence

**Risks / caveats**
- LLM-driven roles and judges can create correlated simulator/evaluator bias.
- The paper states 508 total but lists 160 + 186 + 192 = 538 level instances; this arithmetic conflict is unresolved.

**Verified facts**
- Official GitHub/project/paper define six scenarios and the dual metric table.

**Inference**
- None recorded.

**Unresolved ambiguity**
- Reported total and per-level counts conflict; licensing is unclear.

Original README bullet(s): Curated addition.

## Legal Agent Benchmark

`harvey-lab` · **benchmark** · **evaluate carefully** · active

Complete long-horizon legal matters using files, research, analysis, drafting, and validation tools.

| Field | Detail |
|---|---|
| Construct / theory | All-pass treats legal work as conjunctive reliability: a task passes only if every required expert rubric criterion passes; rubric pass rate exposes partial completion but is not the headline autonomy threshold. |
| Jurisdiction | United States / commercial legal practice, mixed practice areas |
| Languages | English |
| Size | Evolving public release; launch materials describe 1,200+ tasks, 24 practice areas, and 75,000+ rubric criteria, with later contracting extensions |
| Splits | Public task set plus Harvey's separate holdout used for published model results |
| Source | Synthetic client matters and expert-curated instructions, files, outputs, and rubrics |
| Input | Matter instruction and sandboxed document/file environment |
| Output | Research, analysis, and professional work-product artifacts |
| Baselines / leaderboard context | Harvey publishes frontier-model holdout results; public tasks/harness allow community runs but are not identical to the holdout. |
| Dataset access | Public tasks and harness; published headline holdout is private |
| License | MIT |
| Gating | Running agents/judges requires model access and compute |
| Maintenance | Rapidly evolving vendor-maintained benchmark. |
| Reproducibility | Public harness is reproducible in principle; headline holdout scores cannot be independently reproduced and model/judge versions change. |

### Metrics

- **All-pass rate** — A task receives 1 only when every applicable rubric criterion passes; mean across tasks. Judge: Repeated cross-model LLM judging under repository rubric protocol. **Primary.**
- **Rubric pass rate** — Fraction of individual criteria passed; also report cost and latency for deployment trade-offs. Judge: LLM judge with expert-authored rubrics.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/harveyai/harvey-labs](https://github.com/harveyai/harvey-labs) |
| Hugging Face | None |
| Paper / arXiv | None |
| Leaderboard / competition | None |
| Project | [https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)<br>[https://www.harvey.ai/blog/legal-agent-benchmark-initial-results](https://www.harvey.ai/blog/legal-agent-benchmark-initial-results) |

### Validity and evidence

**Risks / caveats**
- Benchmark owner is a legal-AI vendor and publishes results on a private mirror holdout.
- All-pass is sensitive to rubric granularity and judge false negatives; a single criterion zeroes the task.

**Verified facts**
- Official GitHub and Harvey posts define the harness, expert rubrics, all-pass, and rubric-pass metrics.

**Inference**
- None recorded.

**Unresolved ambiguity**
- The evolving public task count should be read from a pinned release rather than a timeless number.

Original README bullet(s): Curated addition.

## APEX-Agents — Corporate Lawyer

`apex-agents-corporate-law` · **benchmark** · **evaluate carefully** · active

Complete realistic long-horizon corporate-law tasks across applications, files, and professional work environments.

| Field | Detail |
|---|---|
| Construct / theory | Pass@1 measures single-run task completion against multiple criteria; the legal slice tests workflow execution, not legal knowledge in isolation. |
| Jurisdiction | Corporate-law practice / mixed |
| Languages | English |
| Size | 480 total APEX tasks, including 160 corporate-law tasks across 12 worlds |
| Splits | Role-specific public benchmark and leaderboard evaluations |
| Source | Tasks authored by corporate lawyers, consultants, and bankers with files, rubrics, and gold outputs |
| Input | Professional task plus realistic multi-file application world |
| Output | Cross-application actions and completed professional artifact |
| Baselines / leaderboard context | Official Mercor leaderboard compares agent/model configurations by professional role. |
| Dataset access | Public HF benchmark including prompts, rubrics, gold outputs, files, and metadata |
| License | See dataset/harness repositories |
| Gating | Substantial agent infrastructure/model access required |
| Maintenance | Active Mercor professional-agent benchmark. |
| Reproducibility | Public benchmark and harness support reruns, but desktop/application state and model endpoints must be pinned. |

### Metrics

- **Pass@1** — Fraction of tasks passed on one evaluated trajectory under task rubrics. Judge: Archipelago task graders / rubric evaluation. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/Mercor-Intelligence/archipelago](https://github.com/Mercor-Intelligence/archipelago) |
| Hugging Face | [https://huggingface.co/datasets/mercor/apex-agents](https://huggingface.co/datasets/mercor/apex-agents) |
| Paper / arXiv | [https://arxiv.org/abs/2601.14242](https://arxiv.org/abs/2601.14242) |
| Leaderboard / competition | [https://www.mercor.com/apex/apex-agents-leaderboard/corporate-lawyer-agent/](https://www.mercor.com/apex/apex-agents-leaderboard/corporate-lawyer-agent/) |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Only one third of APEX is legal; aggregate APEX scores are not legal scores.
- Public gold outputs/rubrics permit targeted agent tuning.

**Verified facts**
- Official paper/HF/leaderboard identify 480 total and a 160-task corporate-law slice.

**Inference**
- None recorded.

**Unresolved ambiguity**
- Jurisdiction varies by authored task and is not summarized as one national corpus.

Original README bullet(s): Curated addition.

## JUST-NLP 2025 Legal MT Shared Task

`just-nlp-2025-legal-mt` · **shared-task** · **specialist** · completed

Translate legal text from English to Hindi.

| Field | Detail |
|---|---|
| Construct / theory | Reference-based machine-translation metrics reward n-gram or character overlap; the shared task complements them with semantic metrics but still cannot alone establish legal fidelity. |
| Jurisdiction | India |
| Languages | English, Hindi |
| Size | InLMT: 50,000 train, 5,000 validation, 5,000 hidden test sentences |
| Splits | Train/validation plus hidden Codabench test references |
| Source | Indian legal parallel text released for the shared task |
| Input | XLSX rows containing English legal sentences and IDs |
| Output | CSV with ID and Hindi translation |
| Baselines / leaderboard context | The findings paper's Table 2 ranks Team-SVNIT first at AutoRank 61.62; the abstract instead says the highest AutoRank was 72.1, an unresolved internal conflict. |
| Dataset access | Competition bundle via Codabench |
| License | Not clearly stated in the durable public materials |
| Gating | Codabench account may be required for files/submission |
| Maintenance | Completed 2025 shared task; not a continuously maintained benchmark. |
| Reproducibility | Hidden references support clean competition scoring, but long-term artifact access and exact dependency versions are uncertain. |

### Metrics

- **AutoRank** — Arithmetic mean of six 0–100 normalized metrics: BLEU, METEOR, inverted TER, chrF++, BERTScore, and COMET; each receives equal weight. **Primary.**
- **BLEU / METEOR / TER / chrF++ / BERTScore / COMET** — Report all six component metrics; higher is better except raw TER, where lower is better. ROUGE scores appear in additional model analysis but are not part of AutoRank.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | None |
| Hugging Face | None |
| Paper / arXiv | [https://aclanthology.org/2025.justnlp-main.3/](https://aclanthology.org/2025.justnlp-main.3/) |
| Leaderboard / competition | [https://www.codabench.org/competitions/10351/](https://www.codabench.org/competitions/10351/)<br>[https://exploration-lab.github.io/JUST-NLP/JustNLP25_L-MT_Result.pdf](https://exploration-lab.github.io/JUST-NLP/JustNLP25_L-MT_Result.pdf) |
| Project | [https://exploration-lab.github.io/JUST-NLP/](https://exploration-lab.github.io/JUST-NLP/) |

### Validity and evidence

**Risks / caveats**
- Automatic overlap metrics can reward fluent mistranslations or penalize legally equivalent wording.
- The original README linked stale Codabench competition 3682; 10351 is the verified competition.

**Verified facts**
- The official findings paper and competition materials define the 50k/5k/5k splits, six AutoRank components, normalization direction, and equal-weight aggregation.

**Inference**
- None recorded.

**Unresolved ambiguity**
- A clear dataset license was not located.
- The findings abstract reports a top AutoRank of 72.1 while Table 2 and the official result sheet report 61.62.

Original README bullet(s): #8

## SwiLTra-Bench

`swiltra-bench` · **benchmark-suite** · **recommended** · fixed-release

Translate Swiss laws, court headnotes, and press releases among official Swiss languages and English.

| Field | Detail |
|---|---|
| Construct / theory | Reference-based and learned semantic metrics compare translation fidelity; SwiLTra-Judge is calibrated against legal experts to better capture specialized legal adequacy than lexical overlap alone. |
| Jurisdiction | Switzerland |
| Languages | German, French, Italian, Romansh, English |
| Size | More than 180,000 aligned translation pairs across three document families |
| Splits | Dataset-specific train/test evaluation sets |
| Source | Swiss laws, decision summaries/headnotes, and Supreme Court press releases |
| Input | Legal text in one source language |
| Output | Translation in a target language |
| Baselines / leaderboard context | Paper evaluates frontier LLMs, specialized MT systems, and fine-tuned smaller models. |
| Dataset access | Public HF datasets |
| License | Dataset/source-specific |
| Gating | None observed |
| Maintenance | Stable 2025 release. |
| Reproducibility | Good for public data; learned judges and frontier API baselines require pinned checkpoints/endpoints. |

### Metrics

- **XCOMET / BLEURT / GEMBA-MQM** — Learned/reference and LLM translation-quality scores reported by document/language pair; preserve model versions. Judge: GEMBA-MQM uses an LLM evaluator. **Primary.**
- **SwiLTra-Judge / expert rating** — Specialized judge compared with human legal-expert assessments. Judge: SwiLTra-Judge. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/JoelNiklaus/SwissLegalTranslations](https://github.com/JoelNiklaus/SwissLegalTranslations) |
| Hugging Face | [https://huggingface.co/collections/joelniklaus/swiltra-bench](https://huggingface.co/collections/joelniklaus/swiltra-bench)<br>[https://huggingface.co/datasets/joelniklaus/SwissLawTranslations](https://huggingface.co/datasets/joelniklaus/SwissLawTranslations)<br>[https://huggingface.co/datasets/joelniklaus/SwissDecisionSummaryTranslations](https://huggingface.co/datasets/joelniklaus/SwissDecisionSummaryTranslations)<br>[https://huggingface.co/datasets/joelniklaus/SwissSupremeCourtPressReleaseTranslations](https://huggingface.co/datasets/joelniklaus/SwissSupremeCourtPressReleaseTranslations) |
| Paper / arXiv | [https://arxiv.org/abs/2503.01372](https://arxiv.org/abs/2503.01372)<br>[https://aclanthology.org/2025.acl-long.725/](https://aclanthology.org/2025.acl-long.725/) |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Machine metrics correlate imperfectly with legal-expert judgments.
- Document families and language pairs differ sharply in size and difficulty.

**Verified facts**
- Official paper/GitHub/HF collection define the corpus families and evaluator set.

**Inference**
- None recorded.

**Unresolved ambiguity**
- There is no single HF dataset; the canonical resource is a three-dataset collection.

Original README bullet(s): Curated addition.

## Multilingual Indian Legal Parallel Corpus

`milpac` · **benchmark-suite** · **recommended** · fixed-release

Translate verified Indian legal text from English into nine Indian languages.

| Field | Detail |
|---|---|
| Construct / theory | BLEU/GLEU/chrF++ measure reference overlap at word/character levels, while law-practitioner ratings test preservation of meaning, suitability for legal use, and fluency—the intended high-stakes construct. |
| Jurisdiction | India |
| Languages | English, Hindi, Bengali, Marathi, Tamil, Gujarati, Telugu, Malayalam, Punjabi, Odia |
| Size | 17,853 aligned pairs across three datasets |
| Splits | Corpus/dataset-specific evaluation files |
| Source | Verified IP primers, Indian statutes/acts, and legal FAQ materials ratified by legal experts |
| Input | English legal text unit |
| Output | Translation in one of nine Indian languages |
| Baselines / leaderboard context | Paper compares commercial MT, academic systems, open models, and LLMs. |
| Dataset access | Public GitHub |
| License | Non-commercial license |
| Gating | None observed |
| Maintenance | Stable benchmark/corpus release; also included as IL-TUR's translation task. |
| Reproducibility | Strong for automatic metrics with recorded tokenizer/SacreBLEU signature; human survey replication requires the same protocol. |

### Metrics

- **BLEU / GLEU / chrF++** — Corpus/reference overlap scaled 0–100; IndicNLP tokenization and SacreBLEU signature are recorded for BLEU/chrF++. **Primary.**
- **POM / SLU / FLY human ratings** — Law practitioners rate Preservation of Meaning, Suitability for Legal Use, and Fluency on the study scale. Judge: Human law practitioners/students. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/Law-AI/MILPaC](https://github.com/Law-AI/MILPaC) |
| Hugging Face | None |
| Paper / arXiv | [https://arxiv.org/abs/2310.09765](https://arxiv.org/abs/2310.09765)<br>[https://doi.org/10.1145/3748313](https://doi.org/10.1145/3748313) |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Automatic metrics show low correlation with legal-human scores for several languages/datasets.
- Reusing MILPaC through IL-TUR is duplicate evidence, not a second independent translation benchmark.

**Verified facts**
- Official GitHub, arXiv, and ACM article define 17,853 pairs, nine target languages, and exact automatic/human metrics.

**Inference**
- None recorded.

**Unresolved ambiguity**
- None recorded.

Original README bullet(s): Curated addition.

## LegalEval-Q

`legaleval-q` · **evaluation-framework** · **related—not a comparable public benchmark** · fixed-release

Predict the quality of Chinese LLM-generated legal answers.

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

- **Dimension regression / AdjScore** — Predict per-dimension quality labels and combine them with the paper's adjustment formula. Judge: Learned LegalEval-Q evaluator. **Primary.**

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

Original README bullet(s): #18

## LRAGE

`lrage` · **evaluation-framework** · **related—not a comparable public benchmark** · active

Configure legal RAG evaluations across retrievers, rerankers, agents, judges, and custom corpora.

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

- **Inherited task/retrieval/judge metrics** — Metric set is configuration-dependent and must be reported with corpus and judge versions. Judge: Optional/configurable. **Primary.**

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

Original README bullet(s): #19

## prinzbench

`prinzbench` · **private-benchmark** · **related—not a comparable public benchmark** · private

Answer obscure US legal-research and general information-search questions.

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

- **Human pass/fail and pass@1** — Author judges each answer; subtotals by legal/search category. Judge: Single benchmark author. **Primary.**

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

Original README bullet(s): #21

## Open Legal-Answer Benchmark

`open-legal-answer-benchmark` · **benchmark** · **evaluate carefully** · active

Produce current US legal answers with relevant, supported, and correctly ranged citations.

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

- **Must-include / must-not / authority retrieval** — Rule/checklist scoring of required propositions, prohibited errors, and retrieval of the right authority. **Primary.**
- **Citation support and in-range** — Check whether citations support the associated claim and point to the relevant passage; optional LLM judging is separate. Judge: Optional/configurable. **Primary.**

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

Original README bullet(s): #22

## awesome-legal-nlp

`awesome-legal-nlp` · **resource-list** · **related—not a comparable public benchmark** · active

Discovery index for legal NLP datasets, models, papers, surveys, books, and events.

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

- **Not applicable** — No scorer or evaluation protocol exists. **Primary.**

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

Original README bullet(s): #7
