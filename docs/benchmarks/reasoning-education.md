# General legal reasoning and education

<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->

Broad suites, legal language understanding, professional exams, and jurisdiction-specific knowledge tests.

Snapshot: **2026-08-03** · 9 entries

[Catalog index](../catalog.md) · [Selection guide](../selection-guide.md) · [Metric field guide](../metric-theory.md) · [Methodology](../methodology.md)

## On this page

- [LegalBench](#legalbench)
- [LawBench](#lawbench)
- [LexGLUE](#lexglue)
- [LEXTREME](#lextreme)
- [LEXam](#lexam)
- [LexEval](#lexeval)
- [ArabLegalEval](#arablegaleval)
- [IL-TUR](#il-tur)
- [Korean Canonical Legal Benchmark](#kcl)

<a id="legalbench"></a>
## LegalBench

`legalbench` · **benchmark-suite** · **recommended** · active

Task-specific legal reasoning across classification, extraction, question answering, and generation.

### Evaluation contract

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

- **Task-defined exact match / accuracy / F1 / generation scores:** Each task supplies its own scorer; aggregate results must disclose task selection and averaging. **Primary.**

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

Original source bullet(s): #1

[Back to page index](#on-this-page)

<a id="lawbench"></a>
## LawBench

`lawbench` · **benchmark-suite** · **recommended** · fixed-release

Chinese legal memorization, understanding, and application across 20 tasks.

### Evaluation contract

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

- **Official 20-task metric map:** 1-1 ROUGE-L; 1-2 accuracy; 2-1 F0.5; 2-2 F1; 2-3 F1; 2-4 accuracy; 2-5 character-level rc-F1; 2-6 entity soft-F1; 2-7 ROUGE-L; 2-8 accuracy; 2-9 F1; 2-10 trigger soft-F1; 3-1 F1; 3-2 ROUGE-L; 3-3 F1; 3-4 and 3-5 normalized log-distance; 3-6 accuracy; 3-7 accuracy; 3-8 ROUGE-L. Report per-task scores because the official AVG mixes unlike scales. **Primary.**
- **Normalized log-distance (3-4/3-5):** For scorable prison-term items, score = 1 - mean(|ln(gold_months+1)-ln(pred_months+1)|)/ln(216). The evaluator uses the first parsed month value, otherwise the first year value multiplied by 12; an unparsed prediction receives distance ln(216). Gold death/life-imprisonment rows are skipped.
- **Abstention rate:** The evaluator separately reports the fraction of rows whose answer parser cannot extract a valid task-specific response. This is not folded consistently into every task score, and the 2-6 evaluator misspells its returned abstention key, so the top-level CSV records zero for that task unless corrected.

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

Original source bullet(s): #2

[Back to page index](#on-this-page)

<a id="lexglue"></a>
## LexGLUE

`lexglue` · **benchmark-suite** · **recommended** · fixed-release

Standardized English legal language understanding across seven classification and judgment tasks.

### Evaluation contract

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

- **Macro-F1 and micro-F1 / task accuracy:** Task-appropriate classification metrics; report each task and disclose any cross-task averaging. **Primary.**

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

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)

<a id="lextreme"></a>
## LEXTREME

`lextreme` · **benchmark-suite** · **recommended** · fixed-release

Multilingual European legal classification and named-entity recognition across 24 languages.

### Evaluation contract

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

- **Macro-F1:** Base metric for every task, giving each class equal weight. **Primary.**
- **Hierarchical harmonic-mean LEXTREME score:** Compute harmonic means within dataset and language views, then the harmonic mean of those two aggregates; any near-zero component dominates downward. **Primary.**

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

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)

<a id="lexam"></a>
## LEXam

`lexam` · **benchmark** · **recommended** · active

Answer bilingual law-school multiple-choice and open-answer examination questions.

### Evaluation contract

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

- **MCQ accuracy:** Exact selected-option correctness. **Primary.**
- **Open-answer judge ensemble:** Multiple LLM judges score generated answers against references; record judge model versions and aggregation. Judge: Versioned ensemble documented by LEXam. **Primary.**

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

Original source bullet(s): #11

[Back to page index](#on-this-page)

<a id="lexeval"></a>
## LexEval

`lexeval` · **benchmark-suite** · **specialist** · fixed-release

Chinese legal knowledge, inference, generation, discrimination, and ethics across 23 tasks.

### Evaluation contract

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

- **Accuracy:** Exact option/label correctness for closed-form tasks. **Primary.**
- **ROUGE-L:** Longest-common-subsequence overlap for generated answers.

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

Original source bullet(s): #12

[Back to page index](#on-this-page)

<a id="arablegaleval"></a>
## ArabLegalEval

`arablegaleval` · **benchmark-suite** · **check before use** · active

Arabic legal knowledge, classification, question answering, and translation, with substantial Saudi-law coverage.

### Evaluation contract

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

- **Accuracy / F1 / ROUGE:** Task-specific closed-form and overlap metrics. **Primary.**
- **LLM and human ratings:** GPT-4-style judge scores for some generation plus human translation ratings; record the exact judge prompt/model. Judge: Task-dependent, including GPT-4.

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

Original source bullet(s): #13

[Back to page index](#on-this-page)

<a id="il-tur"></a>
## IL-TUR

`il-tur` · **benchmark-suite** · **recommended** · active

Indian legal named entities, rhetorical roles, judgment/explanation, bail, statute identification, precedent retrieval, summarization, and translation.

### Evaluation contract

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

- **Strict macro-F1 / macro-F1 / micro-F1@k:** NER, classification, and retrieval tasks use the official task-specific F1 aggregation. **Primary.**
- **ROUGE-L / BERTScore / BLEU / GLEU / chrF++:** Explanation, summarization, and translation use reference-overlap/semantic metrics. **Primary.**

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

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)

<a id="kcl"></a>
## Korean Canonical Legal Benchmark

`kcl` · **benchmark-suite** · **recommended** · active

Answer Korean bar-exam MCQs and essays with question-aligned supporting precedents.

### Evaluation contract

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

- **MCQ accuracy:** Exact five-choice accuracy, reported with and without precedents. **Primary.**
- **Weighted rubric percentage:** Instance rubrics inherit each official essay's points; earned points are divided by 2,905 total benchmark points. Judge: Gemini 2.5 Flash. **Primary.**

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

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)
