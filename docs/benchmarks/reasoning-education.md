# General legal reasoning and education

<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->

Broad suites, legal language understanding, professional exams, and jurisdiction-specific knowledge tests.

Snapshot: **2026-08-04** · 15 entries

[Back to README](../../README.md) · [Catalog index](../catalog.md) · [Selection guide](../selection-guide.md) · [Metric field guide](../metric-theory.md) · [Methodology](../methodology.md)

## On this page

- [LegalBench](#legalbench)
- [LawBench](#lawbench)
- [LexEval](#lexeval)
- [LexGLUE](#lexglue)
- [LEXTREME](#lextreme)
- [LEXam](#lexam)
- [ArabLegalEval](#arablegaleval)
- [Arabic Legal Argument Reasoning Benchmark (ALARB)](#alarb)
- [IL-TUR](#il-tur)
- [Korean Canonical Legal Benchmark](#kcl)
- [Professional Reasoning Benchmark (PRBench)](#prbench)
- [PLawBench](#plawbench)
- [LexGenius](#lexgenius)
- [PILOT-Bench](#pilot-bench)
- [MoZIP](#mozip)

<a id="legalbench"></a>
## LegalBench

`legalbench` · **benchmark-suite** · **recommended** · active

Task-specific legal reasoning across classification, extraction, question answering, and generation.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | LegalBench collaboration (mixed) |
| First documented | [2023-08-20](https://arxiv.org/abs/2308.11462) — arXiv v1 submission |
| Latest verified update | [2026-03-30](https://github.com/HazyResearch/legalbench) — GitHub repository push |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare models per-task on 162 lawyer-authored reasoning tasks (issue-spotting, rule application, interpretation) to position research against published results.
- Shortlist models by picking the task subset that matches the target legal job and comparing per-task scores.
- Regression-test prompt or model changes against a pinned task subset and harness commit.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | The suite operationalizes six lawyer-facing forms of legal reasoning through 162 independently authored tasks; it is a task collection, not a single latent legal-intelligence score. |
| Jurisdiction | United States, mixed/common-law |
| Languages | English |
| Size | 162 tasks; per-task instance counts vary |
| Splits | Task-defined; no unified train/dev/test split |
| Source material | Expert-contributed tasks plus public legal datasets and authorities |
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

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | OpenCompass / Shanghai AI Laboratory (mixed) |
| First documented | [2023-09-28](https://arxiv.org/abs/2309.16289) — arXiv v1 submission |
| Latest verified update | [2025-03-07](https://huggingface.co/datasets/doolayer/LawBench) — Hugging Face dataset update |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare models per-task on 20 Chinese tasks spanning memorization, understanding, and application, including prison-term estimation scored by normalized log-distance.
- Shortlist models for Chinese legal work using the task scores that match the target job.
- Regression-test with a pinned scorer revision, since answer parsing and abstention handling change results.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Tasks are arranged into memorization, understanding, and application levels, testing retrieval of legal knowledge separately from applying it to cases and generated outputs. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | 10,000 examples: 20 tasks × 500 |
| Splits | Evaluation-oriented task files; no unified hidden split |
| Source material | Chinese exams and public legal NLP datasets including CAIL/JEC-QA/LAIC sources |
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

<a id="lexeval"></a>
## LexEval

`lexeval` · **benchmark-suite** · **specialist** · fixed-release

Chinese legal knowledge, inference, generation, discrimination, and ethics across 23 tasks.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | LexEval authors (academic) |
| First documented | [2024-09-30](https://arxiv.org/abs/2409.20288) — arXiv v1 submission |
| Latest verified update | [2024-11-26](https://arxiv.org/abs/2409.20288) — arXiv revision |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare Chinese-capable models across 23 tasks in six ability groups, from legal memorization to generation and ethics.
- Screen models for Chinese legal QA or drafting work before building a private Chinese-law holdout.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Six ability groups broaden evaluation beyond exams, but accuracy and ROUGE-L remain task proxies rather than a validated unidimensional legal-capability scale. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | 14,150 questions across 23 tasks and six ability groups |
| Splits | Evaluation collection; mostly multiple choice plus generation |
| Source material | Chinese legal exams, public datasets, authored and transformed tasks |
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

### Validity and evidence

**Risks / caveats**
- Public exams and answers are highly contamination-prone.
- ROUGE-L can reward surface overlap without legal validity.

**Verified facts**
- Official repository and paper define 14,150 questions and 23 tasks.

**Unresolved ambiguity**
- No stable current official leaderboard or project page was verified; the historical Collam hostname currently fails TLS validation.

Original source bullet(s): #12

[Back to page index](#on-this-page)

<a id="lexglue"></a>
## LexGLUE

`lexglue` · **benchmark-suite** · **recommended** · fixed-release

Standardized English legal language understanding across seven classification and judgment tasks.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | LexGLUE authors (academic) |
| First documented | [2021-10-03](https://arxiv.org/abs/2110.00976) — arXiv v1 submission |
| Latest verified update | [2025-07-23](https://github.com/coastalcph/lex-glue) — GitHub repository push |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Position a model against published results on seven standardized English legal NLU tasks with fixed splits.
- Compare architectures per-task across ECtHR, SCOTUS, EUR-LEX, LEDGAR, UNFAIR-ToS, and CaseHOLD.
- Regression-test classification components using the reproducible task configurations.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | LexGLUE standardizes task splits and reporting across ECtHR A/B, SCOTUS, EUR-LEX, LEDGAR, UNFAIR-ToS, and CaseHOLD; it measures a portfolio of NLU tasks rather than one jurisdiction-neutral ability. |
| Jurisdiction | Council of Europe, European Union, United States, mixed contracts/terms |
| Languages | English |
| Size | Seven constituent datasets |
| Splits | Fixed task-specific train/validation/test splits |
| Source material | Previously released legal datasets normalized by the LexGLUE authors |
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

### Validity and evidence

**Risks / caveats**
- All constituent test labels are public and likely present in model-development workflows.
- A single aggregate hides jurisdiction and task-family failures.

**Verified facts**
- Official GitHub/HF/paper define seven tasks and standardized splits.

**Inference**
- LexGLUE is a strong comparability suite, not a deployability claim.

**Related entries**

- [CaseHOLD](prediction-fairness-rules.md#casehold)
- [ECtHR Tasks A/B](prediction-fairness-rules.md#ecthr)
- [LEDGAR](contracts-deal-work.md#ledgar)

[Back to page index](#on-this-page)

<a id="lextreme"></a>
## LEXTREME

`lextreme` · **benchmark-suite** · **recommended** · fixed-release

Multilingual European legal classification and named-entity recognition across 24 languages.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | LEXTREME authors (academic) |
| First documented | [2023-01-30](https://arxiv.org/abs/2301.13126) — arXiv v1 submission |
| Latest verified update | [2026-05-20](https://huggingface.co/datasets/joelniklaus/lextreme) — Hugging Face dataset update |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare multilingual models per language and task on European legal classification and NER across 24 languages.
- Check language balance with the harmonic aggregate when selecting a model that must not fail quietly on any language.
- Position research against the published multilingual baselines.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Hierarchical harmonic means require balanced performance across datasets and languages: one dataset aggregate and one language aggregate are combined so a weak component depresses the final score. |
| Jurisdiction | European Union, Council of Europe, European national jurisdictions |
| Languages | 24 European languages |
| Size | 11 datasets covering 24 languages |
| Splits | Dataset-specific train/validation/test splits |
| Source material | European legislation, cases, and legal NLP datasets |
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

### Validity and evidence

**Risks / caveats**
- Missing language-task cells and very different dataset scales complicate interpretation.
- Harmonic aggregation is intentionally harsh and should accompany—not replace—per-task scores.

**Verified facts**
- Paper defines 11 datasets, 24 languages, macro-F1, and hierarchical harmonic aggregation.

[Back to page index](#on-this-page)

<a id="lexam"></a>
## LEXam

`lexam` · **benchmark** · **recommended** · active

Answer bilingual law-school multiple-choice and open-answer examination questions.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | LEXam team (academic) |
| First documented | [2025-05-19](https://arxiv.org/abs/2505.12864) — arXiv v1 submission |
| Latest verified update | [2026-05-21](https://huggingface.co/datasets/LEXam-Benchmark/LEXam) — Hugging Face dataset update |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare models on bilingual English/German law-school multiple-choice and open-answer exam questions.
- Research open-answer legal grading using the documented versioned judge ensemble.
- Screen models for legal-education or exam-preparation products.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | MCQ accuracy measures answer selection; open-answer ensemble judging estimates substantive coverage against references, making judge version and rubric part of the instrument. |
| Jurisdiction | Germany, United States / English-language courses, mixed law-school curricula |
| Languages | English, German |
| Size | 7,537 questions from 340 exams and 116 courses: 2,841 open-answer and 4,696 MCQ |
| Splits | Versioned JSON release; no single training split is required |
| Source material | University law examinations and course materials |
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
| Project | [https://lexam-benchmark.github.io/](https://lexam-benchmark.github.io/) |

### Validity and evidence

**Risks / caveats**
- Public exams and answers are contamination-prone.
- Open-answer rankings can move when hosted judges or ensemble membership changes.

**Verified facts**
- Official GitHub/HF/project sources agree on the current 7,537-question release.

**Unresolved ambiguity**
- Jurisdiction is course-dependent rather than a single national-law corpus.

Original source bullet(s): #11

[Back to page index](#on-this-page)

<a id="arablegaleval"></a>
## ArabLegalEval

`arablegaleval` · **benchmark-suite** · **check before use** · active

Arabic legal knowledge, classification, question answering, and translation, with substantial Saudi-law coverage.

**Also known as:** ArLegalBench

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | THIQAH R&D (company; commercial interest unclear) |
| First documented | [2024-08-15](https://arxiv.org/abs/2408.07983) — arXiv v1 submission |
| Latest verified update | [2025-05-21](https://github.com/Thiqah/ArabLegalEval) — GitHub repository push |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare models on Arabic legal multiple-choice, classification, and QA with substantial Saudi-law coverage.
- Separate scores on locally sourced versus translated/synthetic subsets when shortlisting a model for Arabic legal work.
- Test English-to-Arabic legal translation handling inside the same suite.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | The suite combines local and translated tasks; task scores therefore mix Arabic legal competence, general task performance, and translation artifacts. |
| Jurisdiction | Saudi Arabia, Arab jurisdictions / translated sources |
| Languages | Arabic, English |
| Size | HF card exposes about 15.3k ArLegalBench rows, 11.6k MCQs, and 79 QA rows |
| Splits | Configuration-specific |
| Source material | Local legal material, translated benchmarks, and synthetic items |
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

### Validity and evidence

**Risks / caveats**
- Synthetic GPT-4/Claude items and translated tasks can introduce generator artifacts.
- The QA component is very small relative to the multiple-choice collection.

**Verified facts**
- Official organization GitHub/HF and paper establish the suite identity.

**Unresolved ambiguity**
- A unified release-wide license was not found.

Original source bullet(s): #13

[Back to page index](#on-this-page)

<a id="alarb"></a>
## Arabic Legal Argument Reasoning Benchmark (ALARB)

`alarb` · **dataset** · **check before use** · fixed-release

Reason over Saudi commercial-law cases, complete arguments, and identify governing statutory articles.

**Also known as:** ALARB

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | THIQAH R&D (company; commercial interest unclear) |
| First documented | [2025-10-01](https://arxiv.org/abs/2510.00694) — arXiv v1 submission |
| Latest verified update | [2025-10-15](https://huggingface.co/datasets/THIQAH-RD/ALARB) — Hugging Face dataset update |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test verdict and argument completion on Saudi commercial-law cases against reference judgments.
- Test identification of the governing statutory article for a case via the MCQ split.
- Source verified Saudi case material when designing an internal Arabic-law evaluation set.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Verdict/argument generation is judged for correctness and partial correctness, while article selection uses MCQ accuracy; the protocol mixes open and closed-form constructs. |
| Jurisdiction | Saudi Arabia |
| Languages | Arabic |
| Size | 13,344 cases linked to eight statutes; reported experiments use 1,329 cases and 1,159 MCQs per article task |
| Splits | HF exposes a release without a clearly isolated hidden test |
| Source material | Saudi commercial cases and statutes, restructured with LLM assistance |
| Input | Case facts/reasoning context or article question |
| Output | Verdict/reasoning text or selected article |
| Baselines / leaderboard context | Paper evaluates multiple Arabic/general LLMs. |
| Dataset access | Public HF release |
| License | HF metadata: Apache-2.0 |
| Gating | None observed |
| Maintenance | Fixed research release; no canonical GitHub repository located. |
| Reproducibility | Data are inspectable, but hosted-judge drift and absence of a hidden split limit strict reproduction. |

### Metrics

- **Correct / partial / incorrect judge score:** GPT-4o categorizes generated legal outputs against references. Judge: GPT-4o. **Primary.**
- **MCQ accuracy:** Exact statutory-article choice. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| Hugging Face | [https://huggingface.co/datasets/THIQAH-RD/ALARB](https://huggingface.co/datasets/THIQAH-RD/ALARB) |
| Paper / arXiv | [https://arxiv.org/abs/2510.00694](https://arxiv.org/abs/2510.00694) |

### Validity and evidence

**Risks / caveats**
- LLM-assisted restructuring and mapping can propagate annotation errors.
- Public cases, labels, and references permit contamination and evaluation-set training.

**Verified facts**
- Paper and THIQAH-RD HF release identify the dataset.

**Unresolved ambiguity**
- No canonical GitHub or independent leaderboard was found.

Original source bullet(s): #14

[Back to page index](#on-this-page)

<a id="il-tur"></a>
## IL-TUR

`il-tur` · **benchmark-suite** · **recommended** · active

Indian legal named entities, rhetorical roles, judgment/explanation, bail, statute identification, precedent retrieval, summarization, and translation.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Exploration Lab (academic) |
| First documented | [2024-07-07](https://arxiv.org/abs/2407.05399) — arXiv v1 submission |
| Latest verified update | [2025-06-07](https://github.com/Exploration-Lab/IL-TUR) — GitHub repository push |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare models per-task across eight Indian legal tasks: NER, rhetorical roles, judgment and bail prediction, statute and precedent retrieval, summarization, and translation.
- Shortlist models for Indian-language legal work using per-language reporting.
- Research positioning against the maintained IL-TUR leaderboard.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Eight task-specific datasets cover legal understanding and production; strict/macro/micro F1, retrieval F1@k, generation overlap, and translation metrics should be read per task, not as one legal score. |
| Jurisdiction | India |
| Languages | English, Hindi, Bengali, Gujarati, Marathi, Malayalam, Odia, Punjabi, Tamil, Telugu |
| Size | Eight tasks; examples include 105 NER opinions, 21,184 rhetorical-role sentences, and 34k+ judgment documents |
| Splits | Task-specific folds and train/dev/test files |
| Source material | Indian Supreme/High Court cases, statutes, summaries, and MILPaC parallel text |
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

**Unresolved ambiguity**
- HF metadata cites MILPaC arXiv alongside the IL-TUR paper; cite both appropriately.

[Back to page index](#on-this-page)

<a id="kcl"></a>
## Korean Canonical Legal Benchmark

`kcl` · **benchmark-suite** · **recommended** · active

Answer Korean bar-exam MCQs and essays with question-aligned supporting precedents.

**Also known as:** KCL

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | LBOX / KCL authors (mixed; commercial interest unclear) |
| First documented | [2025-12-31](https://arxiv.org/abs/2512.24572) — arXiv v1 submission |
| Latest verified update | [2026-01-23](https://github.com/lbox-kr/kcl) — GitHub repository push |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare models on Korean bar-exam MCQs with and without supplied precedents, isolating reasoning from memorized Korean law.
- Test Korean legal essay writing against official point-weighted rubrics.
- Screen models for Korean-law products before building a counsel-reviewed holdout.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Providing supporting precedents is designed to reduce dependence on memorized Korean law and expose reasoning; MCQ exactness and weighted instance rubrics then score application. |
| Jurisdiction | South Korea |
| Languages | Korean |
| Size | KCL-MCQA: 283 questions and 1,103 precedents; KCL-Essay: 169 questions, 550 precedents, 2,739 rubrics |
| Splits | Evaluation variants with and without supporting precedents |
| Source material | 2021–2025 Korean Bar Exam questions, expert commentaries, and retrieved precedents |
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

### Validity and evidence

**Risks / caveats**
- The essay judge helped generate rubric sets, creating model-family dependence despite attorney review.
- Question-aligned precedents reduce knowledge load but may make retrieval unrealistically solved.

**Verified facts**
- Official paper/GitHub/HF define counts, 2,905-point aggregation, and Gemini 2.5 Flash judge.

[Back to page index](#on-this-page)

<a id="prbench"></a>
## Professional Reasoning Benchmark (PRBench)

`prbench` · **benchmark** · **recommended** · active

Produce open-ended professional legal analysis that satisfies granular expert-authored criteria.

**Also known as:** PRBench

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Scale AI / JusticeBench (company; commercial interest) |
| First documented | [2025-11-13](https://github.com/scaleapi/PRBench) — GitHub and Hugging Face release |
| Latest verified update | [2026-06-24](https://huggingface.co/datasets/ScaleAI/PRBench) — Hugging Face dataset update |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare open-response legal reasoning on 500 practitioner-authored tasks spanning 114 countries and 47 US jurisdictions.
- Shortlist models for professional legal analysis using weighted atomic criteria rather than multiple-choice accuracy.
- Adapt the weighted-rubric protocol when building a fresh, jurisdiction-specific professional holdout.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Weighted atomic criteria operationalize professional issue coverage and reasoning quality; the legal slice should be reported separately from the finance slice. |
| Jurisdiction | 114 countries, 47 United States jurisdictions |
| Languages | English |
| Size | 1,100 prompts: 500 law and 600 finance; 19,356 criteria reported by JusticeBench |
| Splits | Full and hard subsets; legal-hard contains 250 tasks |
| Source material | Prompts and rubrics authored by 182 legal and finance professionals |
| Input | Professional scenario or question |
| Output | Open-ended analysis or recommendation |
| Baselines / leaderboard context | JusticeBench publishes separate legal and finance leaderboards for frontier models. |
| Dataset access | Public GitHub and Hugging Face release |
| License | CC BY 4.0 data; MIT repository code |
| Gating | None observed |
| Maintenance | Active Scale/JusticeBench release; pin the dataset revision and leaderboard date. |
| Reproducibility | Public tasks and rubrics support reruns, but exact judge-model disclosure is incomplete. |

### Metrics

- **Weighted rubric score:** Each task has 10–30 binary criteria weighted from −10 to +10; report legal-slice rubric-weighted and minimum-normalized aggregates under the official protocol. Judge: Automated judge model not fully identified in the public artifacts. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/scaleapi/PRBench](https://github.com/scaleapi/PRBench) |
| Hugging Face | [https://huggingface.co/datasets/ScaleAI/PRBench](https://huggingface.co/datasets/ScaleAI/PRBench) |
| Paper / arXiv | [https://arxiv.org/abs/2511.11562](https://arxiv.org/abs/2511.11562) |
| Leaderboard / competition | [https://scale.com/leaderboard/prbench-legal](https://scale.com/leaderboard/prbench-legal)<br>[https://scale.com/leaderboard/prbench-finance](https://scale.com/leaderboard/prbench-finance) |
| Project | [https://www.justicebench.org/dataset/prbench](https://www.justicebench.org/dataset/prbench) |

### Validity and evidence

**Risks / caveats**
- Public prompts and rubrics create contamination and benchmark-targeting risk.
- JusticeBench reports 19,356 criteria while the Hugging Face card reports 18,692; version scope must be pinned.
- Scale has a commercial interest in the leaderboard and benchmark ecosystem.

**Verified facts**
- Official JusticeBench, GitHub, Hugging Face, and arXiv artifacts agree on 1,100 tasks split between law and finance.

**Inference**
- The legal slice is more useful for legal model selection than the cross-domain combined score.

**Unresolved ambiguity**
- The exact automated judge model and the criteria-count discrepancy remain unresolved.

[Back to page index](#on-this-page)

<a id="plawbench"></a>
## PLawBench

`plawbench` · **benchmark-suite** · **check before use** · active

Answer Chinese legal consultations, analyze practical cases, and draft legal documents.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | PLawBench authors / SKYLENAGE-AI (mixed; commercial interest unclear) |
| First documented | [2026-01-05](https://github.com/SKYLENAGE-AI/PLawBench) — GitHub repository creation |
| Latest verified update | [2026-07](https://aclanthology.org/2026.acl-long.458/) — ACL 2026 publication |
| Access level | partial |
| Test labels | public |
| Independently runnable | partial |

### Possible use cases

- Test Chinese legal consultation, practical case analysis, and document drafting with granular rubric scoring.
- Compare models on open-ended Chinese legal work after verifying which portion of the reported corpus is actually released.
- Use the scenario and rubric taxonomy as a starting point for a private Chinese-law evaluation.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Scenario-specific rubric items measure whether an open response covers expected legal issues and work-product requirements. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | Paper reports 850 questions in 13 scenarios with about 12,500 rubric items; current public artifacts expose about 280 items |
| Splits | Paper-defined evaluation collection; public artifact completeness is unresolved |
| Source material | Chinese legal consultation, practical cases, and drafting scenarios |
| Input | Question, facts, or drafting instruction |
| Output | Legal advice, case analysis, or drafted document |
| Baselines / leaderboard context | ACL paper reports model comparisons across the three task families. |
| Dataset access | Partial public repository and anonymous release |
| License | No clear repository-wide license located |
| Gating | No account gate observed; artifact appears incomplete relative to the paper |
| Maintenance | Recent ACL 2026 release; no stable versioned complete package was verified. |
| Reproducibility | Partial until the reported 850-question corpus, evaluator model, prompts, and aggregation are reconciled with the public files. |

### Metrics

- **Item-level rubric scoring rate:** An LLM evaluator checks granular expected items; report scenario-level results and the exact evaluator configuration. Judge: LLM evaluator; exact public model/version unresolved. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/SKYLENAGE-AI/PLawBench](https://github.com/SKYLENAGE-AI/PLawBench) |
| Paper / arXiv | [https://aclanthology.org/2026.acl-long.458/](https://aclanthology.org/2026.acl-long.458/) |
| Project | [https://anonymous.4open.science/r/PLawbench-B524/](https://anonymous.4open.science/r/PLawbench-B524/) |

### Validity and evidence

**Risks / caveats**
- The paper's 850-question claim conflicts with roughly 280 visible public artifacts.
- An incompletely disclosed LLM judge can materially change scores.
- No clear license was found.

**Verified facts**
- The ACL paper and GitHub repository establish the benchmark and its three task families.

**Unresolved ambiguity**
- Public artifact completeness, exact judge configuration, splits, and license remain unresolved.

[Back to page index](#on-this-page)

<a id="lexgenius"></a>
## LexGenius

`lexgenius` · **benchmark-suite** · **recommended** · active

Answer broad Chinese legal knowledge and reasoning questions across seven dimensions and eleven tasks.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | LexGenius authors (academic) |
| First documented | [2025-10-27](https://github.com/QwenQKing/LexGenius) — GitHub repository creation |
| Latest verified update | [2026-04-16](https://arxiv.org/abs/2512.04578) — arXiv v3 revision |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare Chinese legal knowledge and reasoning across civil, criminal, and commercial law on 8,385 multiple-choice questions.
- Contrast model results with the benchmark's legal-professional human baseline.
- Use dimension and ability scores to find capability gaps before constructing a fresh Chinese-law holdout.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | A hierarchical ability taxonomy maps multiple-choice performance to 20 legal abilities; reported dimension scores remain proxies for the sampled questions. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | 8,385 multiple-choice questions; 7 dimensions, 11 tasks, and 20 abilities |
| Splits | Official evaluation release |
| Source material | Recent Chinese cases and examination questions, manually and LLM reviewed |
| Input | Legal question with answer choices |
| Output | Selected answer option |
| Baselines / leaderboard context | Paper reports frontier/general/legal models and a legal-professional human baseline. |
| Dataset access | Public GitHub release |
| License | No clear repository-wide license located |
| Gating | None observed |
| Maintenance | Recent ACL Findings release; pin the question set and prompt protocol. |
| Reproducibility | Public questions and deterministic scoring support reruns; model formatting and contamination controls still matter. |

### Metrics

- **Accuracy:** Exact option accuracy reported by task, dimension, ability, and overall mean. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/QwenQKing/LexGenius](https://github.com/QwenQKing/LexGenius) |
| Paper / arXiv | [https://arxiv.org/abs/2512.04578](https://arxiv.org/abs/2512.04578)<br>[https://aclanthology.org/2026.findings-acl.926/](https://aclanthology.org/2026.findings-acl.926/) |

### Validity and evidence

**Risks / caveats**
- Public cases and exam questions are highly contamination-prone.
- Multiple-choice accuracy does not establish drafting, research, or client-work competence.
- No clear license was found.

**Verified facts**
- Official GitHub, arXiv, and ACL artifacts agree on 8,385 questions and the seven-dimension taxonomy.

**Unresolved ambiguity**
- Repository-wide data and code license remains unresolved.

[Back to page index](#on-this-page)

<a id="pilot-bench"></a>
## PILOT-Bench

`pilot-bench` · **benchmark-suite** · **specialist** · active

Classify contested issues, Board authorities, and outcomes in US patent appeals.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | PILOT-Bench authors / TeamLab (academic) |
| First documented | [2025-10-08](https://huggingface.co/datasets/Yehoon/pilot-bench) — Hugging Face dataset creation |
| Latest verified update | [2026-03-10](https://huggingface.co/datasets/Yehoon/pilot-bench) — Hugging Face dataset and GitHub repository update |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test issue, rule, and conclusion classification on US Patent Trial and Appeal Board appeals.
- Compare legal reasoning under appellant/examiner-separated, merged, and claim-augmented input settings.
- Diagnose label coverage and class imbalance using exact, micro, macro, weighted, and balanced metrics.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Three classification tasks map PTAB appeal text to IRAC stages: issue type, governing Board authority, and subdecision outcome. |
| Jurisdiction | United States Patent Trial and Appeal Board |
| Languages | English |
| Size | About 18,000 PTAB appeals and roughly 15,000 opinion-split instances |
| Splits | Base appellant/examiner split, role-neutral merge, and split-plus-claim input settings |
| Source material | PTAB decisions aligned with USPTO patent data |
| Input | Appellant arguments, examiner findings, PTAB opinion, and optionally claim text |
| Output | Multi-label issue and authority sets; fine- or coarse-grained subdecision class |
| Baselines / leaderboard context | Official paper/repository compare commercial and open models under standardized zero-shot prompts. |
| Dataset access | Public GitHub and Hugging Face release |
| License | CC BY 4.0 under the repository's stated terms |
| Gating | None; Hugging Face Dataset Viewer is currently unavailable |
| Maintenance | Active release updated March 2026. |
| Reproducibility | Public data, prompts, and sklearn scorers support reruns; pin input setting and coverage handling. |

### Metrics

- **Issue / authority exact match and micro/macro precision, recall, F1:** Multi-label subset accuracy and micro/macro metrics with hamming loss and coverage diagnostics; undefined divisions are set to zero. **Primary.**
- **Subdecision accuracy, balanced accuracy, and macro/micro/weighted F1:** Multi-class scoring for 23 fine or 6 coarse outcome labels with prediction/ground-truth coverage diagnostics. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/TeamLab/pilot-bench](https://github.com/TeamLab/pilot-bench) |
| Hugging Face | [https://huggingface.co/datasets/Yehoon/pilot-bench](https://huggingface.co/datasets/Yehoon/pilot-bench) |
| Paper / arXiv | [https://arxiv.org/abs/2601.04758](https://arxiv.org/abs/2601.04758)<br>[https://aclanthology.org/2025.nllp-1.17/](https://aclanthology.org/2025.nllp-1.17/) |

### Validity and evidence

**Risks / caveats**
- Outcome and authority labels may be predictable from opinion drafting conventions rather than full patent reasoning.
- Public PTAB opinions and labels can appear in training data.
- The README combines CC BY 4.0 with an additional use restriction, so legal compatibility should be checked.

**Verified facts**
- Official GitHub, Hugging Face, arXiv, and NLLP pages establish three IRAC-aligned tasks and their exact metric families.

**Unresolved ambiguity**
- The repository README's license wording adds a use restriction that is not standard CC BY 4.0 language.

**Related entries**

- [MoZIP](reasoning-education.md#mozip)

[Back to page index](#on-this-page)

<a id="mozip"></a>
## MoZIP

`mozip` · **benchmark-suite** · **specialist** · fixed-release

Answer multilingual intellectual-property questions and match patent abstracts to the most similar patent.

**Also known as:** MoZIP Benchmark

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | MoZIP authors / AI-for-Science (academic) |
| First documented | [2023-05-19](https://huggingface.co/datasets/BNNT/IPQA) — Earliest constituent benchmark dataset creation on Hugging Face |
| Latest verified update | [2024-08-20](https://github.com/AI-for-Science/MoZi) — Canonical GitHub repository push |
| Access level | open |
| Test labels | public |
| Independently runnable | partial |

### Possible use cases

- Compare multilingual intellectual-property knowledge on public multiple-choice questions across Chinese, English, German, Spanish, Japanese, Korean, and Portuguese.
- Evaluate open-ended intellectual-property answers with a disclosed human pairwise preference protocol in seven languages.
- Test Chinese and English patent-abstract matching while auditing whether distractor construction creates retrieval shortcuts.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Three task families separate closed-form IP knowledge, human preference over open answers, and bilingual patent-semantic matching; they do not form one validated overall IP-capability scale. |
| Jurisdiction | International and mixed national intellectual-property sources, WIPO patent corpus |
| Languages | Chinese, English, German, Spanish, Japanese, Korean, Portuguese, French, Russian |
| Size | 3,121 items: IPQuiz 2,021; IPQA 100; PatentMatch 1,000 |
| Splits | Public evaluation files only: IPQuiz 834 English, 564 Chinese, and 623 across five other languages; IPQA 100 across seven languages; PatentMatch 500 English and 500 Chinese |
| Source material | Public IP quizzes and regulations; authored/collected IP questions; 2010–2022 WIPO-granted patent parallel abstracts sampled from a 250,000-patent corpus |
| Input | Question plus answer candidates; open IP question; or patent abstract plus four candidate abstracts |
| Output | One or more option letters; generated answer; or selected most-similar patent candidate |
| Baselines / leaderboard context | The paper compares MoZi-7B, BLOOMZ-7B, BELLE-7B, ChatGLM-6B, and ChatGPT / gpt-3.5-turbo; there is no maintained leaderboard. |
| Dataset access | Three public Hugging Face datasets with public labels |
| License | IPQuiz and IPQA: CC BY-NC-SA 4.0; PatentMatch and GitHub code: Apache-2.0 |
| Gating | None observed; no hidden test or official leaderboard |
| Maintenance | Fixed LREC-COLING 2024 research release; the canonical repository was last pushed August 20, 2024, and the three dataset revisions date from 2023. |
| Reproducibility | Public data support MCQ reruns, but the repository does not release an end-to-end benchmark scorer and IPQA requires new human pairwise judgments. |

### Metrics

- **IPQuiz answer accuracy:** Parse predicted option letters with the paper's regular-expression procedure, manually verify parsing, and report exact answer accuracy by language. **Primary.**
- **IPQA human pairwise preference:** Human evaluators compare model answers pairwise and report win, tie, and loss outcomes; the paper's tie-discounted agreement gives full credit for matching judgments, half credit when one evaluator ties, and zero for opposite preferences. Judge: Human evaluators. **Primary.**
- **PatentMatch accuracy:** Exact accuracy for selecting the most semantically similar patent abstract from four candidates, reported for Chinese and English. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/AI-for-Science/MoZi](https://github.com/AI-for-Science/MoZi) |
| Hugging Face | [https://huggingface.co/datasets/BNNT/IPQuiz](https://huggingface.co/datasets/BNNT/IPQuiz)<br>[https://huggingface.co/datasets/BNNT/IPQA](https://huggingface.co/datasets/BNNT/IPQA)<br>[https://huggingface.co/datasets/BNNT/PatentMatch](https://huggingface.co/datasets/BNNT/PatentMatch) |
| Paper / arXiv | [https://arxiv.org/abs/2402.16389](https://arxiv.org/abs/2402.16389)<br>[https://aclanthology.org/2024.lrec-main.1018/](https://aclanthology.org/2024.lrec-main.1018/) |

### Validity and evidence

**Risks / caveats**
- All labels are public and IPQuiz draws from searchable websites, creating direct contamination and tuning risk.
- IPQuiz languages, sources, and legal regimes are uneven, so the nine-language union should not be interpreted as balanced jurisdictional coverage.
- PatentMatch distractors are selected with BM25 and ada-002/Pinecone retrieval, which may reward retrieval artifacts rather than legally meaningful patent similarity.
- The paper evaluates older baseline models and does not define a maintained leaderboard or unified aggregate score.

**Verified facts**
- The official repository links all three Hugging Face datasets and the LREC-COLING paper.
- The paper reports 2,021 IPQuiz items, 100 IPQA items, 1,000 PatentMatch items, task-specific language counts, accuracy for both closed-form tasks, and human pairwise preference for IPQA.

**Inference**
- MoZIP is useful as a specialist diagnostic suite, not as evidence of end-to-end patent-law competence.

**Unresolved ambiguity**
- The paper describes collective multilingual coverage rather than balanced jurisdiction labels, and no canonical executable implementation of the complete evaluation protocol was located.

**Related entries**

- [PILOT-Bench](reasoning-education.md#pilot-bench)

[Back to page index](#on-this-page)
