# General legal reasoning and education

<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->

Broad suites, legal language understanding, professional exams, and jurisdiction-specific knowledge tests.

Snapshot: **2026-08-05** · 22 entries

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
- [KBL](#kbl)
- [LegalBench.PT](#legalbench-pt)
- [OAB-Bench](#oab-bench)
- [Professional Reasoning Benchmark (PRBench)](#prbench)
- [PLawBench](#plawbench)
- [LexGenius](#lexgenius)
- [PILOT-Bench](#pilot-bench)
- [MoZIP](#mozip)
- [JuDGE](#judge)
- [VLegal-Bench](#vlegal-bench)
- [MizanQA](#mizanqa)
- [LexSumm](#lexsumm)

<a id="legalbench"></a>
## LegalBench

`legalbench` · **benchmark-suite** · **recommended** · active

Task-specific legal reasoning across classification, extraction, question answering, and generation.

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | LegalBench collaboration (mixed) |
| Catalog geography | United States |
| Last verified update | [2026-03-30](https://github.com/HazyResearch/legalbench)<br>*GitHub repository push* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare models per-task on 162 lawyer-authored reasoning tasks (issue-spotting, rule application, interpretation) to position research against published results.
- Shortlist models by picking the task subset that matches the target legal job and comparing per-task scores.
- Regression-test prompt or model changes against a pinned task subset and harness commit.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
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

**Related entries**

- [LegalBench.PT](reasoning-education.md#legalbench-pt)
- [OAB-Bench](reasoning-education.md#oab-bench)

Original source bullet(s): #1

[Back to page index](#on-this-page)

<a id="lawbench"></a>
## LawBench

`lawbench` · **benchmark-suite** · **recommended** · fixed-release

Chinese legal memorization, understanding, and application across 20 tasks.

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | OpenCompass / Shanghai AI Laboratory (mixed) |
| Catalog geography | China |
| Last verified update | [2025-03-07](https://huggingface.co/datasets/doolayer/LawBench)<br>*Hugging Face dataset update* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare models per-task on 20 Chinese tasks spanning memorization, understanding, and application, including prison-term estimation scored by normalized log-distance.
- Shortlist models for Chinese legal work using the task scores that match the target job.
- Regression-test with a pinned scorer revision, since answer parsing and abstention handling change results.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
| GitHub | [https://github.com/open-compass/LawBench](https://github.com/open-compass/LawBench) |
| Hugging Face | [https://huggingface.co/datasets/doolayer/LawBench](https://huggingface.co/datasets/doolayer/LawBench) |
| Paper / arXiv | [https://arxiv.org/abs/2309.16289](https://arxiv.org/abs/2309.16289) |
| Leaderboard / competition | [https://lawbench.opencompass.org.cn/](https://lawbench.opencompass.org.cn/) |
| Project | None located |

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

**Related entries**

- [JuDGE](reasoning-education.md#judge)
- [STARD](retrieval-rag-citation.md#stard)

Original source bullet(s): #2

[Back to page index](#on-this-page)

<a id="lexeval"></a>
## LexEval

`lexeval` · **benchmark-suite** · **specialist** · fixed-release

Chinese legal knowledge, inference, generation, discrimination, and ethics across 23 tasks.

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | LexEval authors (academic) |
| Catalog geography | China |
| Last verified update | [2024-11-26](https://arxiv.org/abs/2409.20288)<br>*arXiv revision* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare Chinese-capable models across 23 tasks in six ability groups, from legal memorization to generation and ethics.
- Screen models for Chinese legal QA or drafting work before building a private Chinese-law holdout.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
| GitHub | [https://github.com/CSHaitao/LexEval](https://github.com/CSHaitao/LexEval) |
| Hugging Face | [https://huggingface.co/datasets/CSHaitao/LexEval](https://huggingface.co/datasets/CSHaitao/LexEval) |
| Paper / arXiv | [https://arxiv.org/abs/2409.20288](https://arxiv.org/abs/2409.20288) |
| Leaderboard / competition | None located |
| Project | None located |

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

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | LexGLUE authors (academic) |
| Catalog geography | Multi-jurisdiction and supranational |
| Last verified update | [2025-07-23](https://github.com/coastalcph/lex-glue)<br>*GitHub repository push* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Position a model against published results on seven standardized English legal NLU tasks with fixed splits.
- Compare architectures per-task across ECtHR, SCOTUS, EUR-LEX, LEDGAR, UNFAIR-ToS, and CaseHOLD.
- Regression-test classification components using the reproducible task configurations.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
| GitHub | [https://github.com/coastalcph/lex-glue](https://github.com/coastalcph/lex-glue) |
| Hugging Face | [https://huggingface.co/datasets/coastalcph/lex_glue](https://huggingface.co/datasets/coastalcph/lex_glue) |
| Paper / arXiv | [https://arxiv.org/abs/2110.00976](https://arxiv.org/abs/2110.00976)<br>[https://aclanthology.org/2022.acl-long.297/](https://aclanthology.org/2022.acl-long.297/) |
| Leaderboard / competition | None located |
| Project | None located |

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

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | LEXTREME authors (academic) |
| Catalog geography | Multi-jurisdiction and supranational |
| Last verified update | [2026-05-20](https://huggingface.co/datasets/joelniklaus/lextreme)<br>*Hugging Face dataset update* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare multilingual models per language and task on European legal classification and NER across 24 languages.
- Check language balance with the harmonic aggregate when selecting a model that must not fail quietly on any language.
- Position research against the published multilingual baselines.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
| GitHub | [https://github.com/JoelNiklaus/LEXTREME](https://github.com/JoelNiklaus/LEXTREME) |
| Hugging Face | [https://huggingface.co/datasets/joelniklaus/lextreme](https://huggingface.co/datasets/joelniklaus/lextreme) |
| Paper / arXiv | [https://arxiv.org/abs/2301.13126](https://arxiv.org/abs/2301.13126) |
| Leaderboard / competition | [https://wandb.ai/lextreme/paper_results](https://wandb.ai/lextreme/paper_results) |
| Project | None located |

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

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | LEXam team (academic) |
| Catalog geography | Multi-jurisdiction and supranational |
| Last verified update | [2026-05-21](https://huggingface.co/datasets/LEXam-Benchmark/LEXam)<br>*Hugging Face dataset update* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare models on bilingual English/German law-school multiple-choice and open-answer exam questions.
- Research open-answer legal grading using the documented versioned judge ensemble.
- Screen models for legal-education or exam-preparation products.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
| GitHub | [https://github.com/LEXam-Benchmark/LEXam](https://github.com/LEXam-Benchmark/LEXam) |
| Hugging Face | [https://huggingface.co/datasets/LEXam-Benchmark/LEXam](https://huggingface.co/datasets/LEXam-Benchmark/LEXam) |
| Paper / arXiv | [https://arxiv.org/abs/2505.12864](https://arxiv.org/abs/2505.12864) |
| Leaderboard / competition | None located |
| Project | [https://lexam-benchmark.github.io/](https://lexam-benchmark.github.io/) |

### Validity and evidence

**Risks / caveats**
- Public exams and answers are contamination-prone.
- Open-answer rankings can move when hosted judges or ensemble membership changes.

**Verified facts**
- Official GitHub/HF/project sources agree on the current 7,537-question release.

**Unresolved ambiguity**
- Jurisdiction is course-dependent rather than a single national-law corpus.

**Related entries**

- [LegalBench.PT](reasoning-education.md#legalbench-pt)

Original source bullet(s): #11

[Back to page index](#on-this-page)

<a id="arablegaleval"></a>
## ArabLegalEval

`arablegaleval` · **benchmark-suite** · **check before use** · active

Arabic legal knowledge, classification, question answering, and translation, with substantial Saudi-law coverage.

**Also known as:** ArLegalBench

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | THIQAH R&D (company; commercial interest unclear) |
| Catalog geography | Saudi Arabia |
| Last verified update | [2025-05-21](https://github.com/Thiqah/ArabLegalEval)<br>*GitHub repository push* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare models on Arabic legal multiple-choice, classification, and QA with substantial Saudi-law coverage.
- Separate scores on locally sourced versus translated/synthetic subsets when shortlisting a model for Arabic legal work.
- Test English-to-Arabic legal translation handling inside the same suite.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
| GitHub | [https://github.com/Thiqah/ArabLegalEval](https://github.com/Thiqah/ArabLegalEval) |
| Hugging Face | [https://huggingface.co/datasets/THIQAH-RD/ArabLegalEval](https://huggingface.co/datasets/THIQAH-RD/ArabLegalEval) |
| Paper / arXiv | [https://arxiv.org/abs/2408.07983](https://arxiv.org/abs/2408.07983) |
| Leaderboard / competition | None located |
| Project | None located |

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

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | THIQAH R&D (company; commercial interest unclear) |
| Catalog geography | Saudi Arabia |
| Last verified update | [2025-10-15](https://huggingface.co/datasets/THIQAH-RD/ALARB)<br>*Hugging Face dataset update* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test verdict and argument completion on Saudi commercial-law cases against reference judgments.
- Test identification of the governing statutory article for a case via the MCQ split.
- Source verified Saudi case material when designing an internal Arabic-law evaluation set.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
| GitHub | None located |
| Hugging Face | [https://huggingface.co/datasets/THIQAH-RD/ALARB](https://huggingface.co/datasets/THIQAH-RD/ALARB) |
| Paper / arXiv | [https://arxiv.org/abs/2510.00694](https://arxiv.org/abs/2510.00694) |
| Leaderboard / competition | None located |
| Project | None located |

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

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | Exploration Lab (academic) |
| Catalog geography | India |
| Last verified update | [2025-06-07](https://github.com/Exploration-Lab/IL-TUR)<br>*GitHub repository push* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare models per-task across eight Indian legal tasks: NER, rhetorical roles, judgment and bail prediction, statute and precedent retrieval, summarization, and translation.
- Shortlist models for Indian-language legal work using per-language reporting.
- Research positioning against the maintained IL-TUR leaderboard.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
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

**Related entries**

- [AILA 2019](retrieval-rag-citation.md#aila-2019)

[Back to page index](#on-this-page)

<a id="kcl"></a>
## Korean Canonical Legal Benchmark

`kcl` · **benchmark-suite** · **recommended** · active

Answer Korean bar-exam MCQs and essays with question-aligned supporting precedents.

**Also known as:** KCL

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | LBOX / KCL authors (mixed; commercial interest unclear) |
| Catalog geography | South Korea |
| Last verified update | [2026-01-23](https://github.com/lbox-kr/kcl)<br>*GitHub repository push* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare models on Korean bar-exam MCQs with and without supplied precedents, isolating reasoning from memorized Korean law.
- Test Korean legal essay writing against official point-weighted rubrics.
- Screen models for Korean-law products before building a counsel-reviewed holdout.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
| GitHub | [https://github.com/lbox-kr/kcl](https://github.com/lbox-kr/kcl) |
| Hugging Face | [https://huggingface.co/datasets/lbox/kcl](https://huggingface.co/datasets/lbox/kcl) |
| Paper / arXiv | [https://arxiv.org/abs/2512.24572](https://arxiv.org/abs/2512.24572)<br>[https://aclanthology.org/2026.eacl-short.17/](https://aclanthology.org/2026.eacl-short.17/) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- The essay judge helped generate rubric sets, creating model-family dependence despite attorney review.
- Question-aligned precedents reduce knowledge load but may make retrieval unrealistically solved.

**Verified facts**
- Official paper/GitHub/HF define counts, 2,905-point aggregation, and Gemini 2.5 Flash judge.

**Related entries**

- [KBL](reasoning-education.md#kbl)

[Back to page index](#on-this-page)

<a id="kbl"></a>
## KBL

`kbl` · **benchmark-suite** · **specialist** · active

Answer Korean legal knowledge, legal reasoning, and bar-examination multiple-choice questions with or without retrieved statutes and precedents.

**Also known as:** Korean Benchmark for Legal Language Understanding

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | LBox / KBL authors (mixed; commercial interest unclear) |
| Catalog geography | South Korea |
| Last verified update | [2025-05-19](https://huggingface.co/datasets/lbox/kbl)<br>*Hugging Face benchmark dataset update* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare Korean legal knowledge, reasoning, and bar-exam performance under one multiple-choice harness.
- Measure the effect of statute and precedent retrieval by running the same tasks closed-book and with the released RAG corpus.
- Diagnose Korean task-level failures rather than combining KBL with the distinct KCL or LBOX OPEN identities.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | Per-task accuracy measures exact option selection across heterogeneous knowledge and reasoning tasks; closed-book versus BM25-RAG deltas isolate the practical value and failure modes of retrieved Korean legal sources. |
| Jurisdiction | South Korea |
| Languages | Korean |
| Size | Paper release: 510 examples in seven knowledge tasks, 288 in four reasoning tasks, and 2,510 bar-exam examples (3,308 total); live Hugging Face release: 3,456 rows across 67 configs after adding 2025 bar exams |
| Splits | Every Hugging Face task/config exposes a public test split; the live release has no hidden holdout |
| Source material | Lawyer-designed and lawyer-verified tasks, Korean bar and professional-responsibility exams, active statutes, municipal rules, and Korean precedents |
| Input | Korean question and A–E options, optionally augmented with BM25-retrieved statutes and/or precedents |
| Output | One answer-option label |
| Baselines / leaderboard context | The paper evaluates four open-source and five commercial model families, including EEVE, KULLM3, EXAONE, Qwen2, GPT-3.5/4/4o-mini, and Claude 3/3.5, plus a most-frequent-label baseline; GPT-4 averages 72.0 on the seven knowledge tasks and 48.1 on the 2024 bar-exam domains in the reported table. |
| Dataset access | Public Hugging Face benchmark and companion RAG corpus |
| License | CC BY-NC 4.0 for the released datasets according to the paper and Hugging Face metadata; the GitHub repository has no detected standalone license |
| Gating | None observed, but noncommercial dataset terms apply |
| Maintenance | The live Hub dataset added 2025 bar-exam configs after the paper; pin both the benchmark revision and the RAG corpus snapshot. |
| Reproducibility | Good for public-label reruns through lm-eval-harness, but paper/live row counts differ and the companion RAG corpus viewer does not expose a stable aggregate size. |

### Metrics

- **Per-task accuracy:** Exact option correctness is reported for each knowledge, reasoning, and bar-exam config; suite summaries average named task accuracies rather than invoking an LLM judge. **Primary.**
- **Closed-book versus RAG accuracy delta:** Compare the same model and task under no retrieval, precedent retrieval, statute retrieval, or both; report corpus and retrieved-document count.

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | [https://github.com/lbox-kr/kbl](https://github.com/lbox-kr/kbl) |
| Hugging Face | [https://huggingface.co/datasets/lbox/kbl](https://huggingface.co/datasets/lbox/kbl)<br>[https://huggingface.co/datasets/lbox/kbl-rag](https://huggingface.co/datasets/lbox/kbl-rag) |
| Paper / arXiv | [https://arxiv.org/abs/2410.08731](https://arxiv.org/abs/2410.08731)<br>[https://aclanthology.org/2024.findings-emnlp.319/](https://aclanthology.org/2024.findings-emnlp.319/) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- Public exams, prompts, and answers are contamination-prone, especially for older annual exams.
- The paper's 3,308-example release and the live 3,456-row release are not interchangeable; unpinned comparisons silently mix versions.
- Accuracy collapses diverse legal constructs and does not assess the quality of generated legal analysis.
- RAG results depend on mutable corpora, retrieval depth, and tokenizer/context limits.

**Verified facts**
- The ACL paper defines seven knowledge tasks, four reasoning tasks, four bar-exam domains, multiple-choice scoring, closed-book/RAG conditions, and the paper-release counts.
- The official Hugging Face Dataset Viewer reports 3,456 rows across 67 public test configs and a 2025-05-19 update; the data metadata states CC BY-NC 4.0.

**Inference**
- KBL complements KCL: KBL mixes knowledge and reasoning, while KCL was designed to supply supporting precedents and reduce knowledge dependence.

**Unresolved ambiguity**
- No official leaderboard was located, and the GitHub code license is not declared separately from dataset terms.

**Related entries**

- [Korean Canonical Legal Benchmark](reasoning-education.md#kcl)
- [LRAGE](related-evaluators.md#lrage)

[Back to page index](#on-this-page)

<a id="legalbench-pt"></a>
## LegalBench.PT

`legalbench-pt` · **benchmark** · **check before use** · active

Answer European Portuguese questions testing knowledge and application of Portuguese law across 31 legal fields.

**Also known as:** LegalBench PT

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | LegalBench.PT authors (mixed; commercial interest unclear) |
| Catalog geography | Portugal |
| Last verified update | [2026-05-06](https://huggingface.co/datasets/BeatrizCanaverde/LegalBench.PT)<br>*Hugging Face dataset update* |
| Access level | open |
| Test labels | public |
| Independently runnable | partial |

### Possible use cases

- Compare zero-shot model performance across 31 fields of Portuguese law and six closed-form question formats.
- Identify Portuguese-law areas requiring a fresh expert-authored holdout instead of relying on a single overall score.
- Study synthetic benchmark construction and label-quality failure modes using the paper's lawyer and participant audits.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | Balanced accuracy scores single-answer formats under class imbalance, while F1 balances selected-pair precision and recall for multiple-selection and matching items; weighted aggregation preserves the released field/type distribution. |
| Jurisdiction | Portugal |
| Languages | Portuguese (European) |
| Size | 4,723 generated questions from 626 distinct exam exercises across 31 legal fields: 1,099 multiple-choice, 983 cloze, 89 case-analysis, 1,309 true/false, 695 multiple-selection, and 548 matching questions |
| Splits | Hugging Face exposes 31 field configs, each with one public test split; no hidden labels |
| Source material | Solved 2021–2024 law-school exams from the University of Lisbon, transformed by GPT-4o and filtered for duplicates and explicit article-number prompts |
| Input | Portuguese legal question with type-specific instructions, optional statement/assumptions, and choices or matching items |
| Output | One option, true/false label, a set of options, or matching pairs |
| Baselines / leaderboard context | The paper evaluates GPT-4o, GPT-4o-mini, Claude 3 Opus, Claude 3.5 Sonnet, Llama 3.1 8B/70B/405B, and Mixtral 8x7B zero-shot; reported overall scores range from 68.6 to 85.4, with GPT-4o at 85.4 and Claude 3.5 Sonnet at 85.1. |
| Dataset access | Public Hugging Face dataset with public test labels |
| License | No license was declared in the Hugging Face metadata or paper |
| Gating | None observed; absence of a license is not permission to redistribute or use commercially |
| Maintenance | The Hub artifact was updated in May 2026, but no semantic release notes or executable canonical scorer repository were located. |
| Reproducibility | Moderate: rows and expected answers are public and the paper specifies parsing and metrics, but there is no official code repository or hidden test, and the exact live-versus-paper revision must be pinned. |

### Metrics

- **Balanced accuracy:** Score multiple-choice, cloze, case-analysis, and true/false items by class-balanced accuracy after parsing the required output form. **Primary.**
- **F1 for multiple selection and matching:** Compute F1 from parsed predicted versus gold option sets or matching pairs, then combine question-type and field results by weighted average. **Primary.**

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | None located |
| Hugging Face | [https://huggingface.co/datasets/BeatrizCanaverde/LegalBench.PT](https://huggingface.co/datasets/BeatrizCanaverde/LegalBench.PT) |
| Paper / arXiv | [https://arxiv.org/abs/2502.16357](https://arxiv.org/abs/2502.16357) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- GPT-4o generated every benchmark item from exam material, creating generator style artifacts and possible model-family advantage.
- The paper's lawyer review and broader participant study found nontrivial incorrect and ambiguous gold answers; field-level scores can therefore reflect label noise.
- Several legal fields contain very few questions, making their percentages unstable and unsuitable for strong claims.
- All test labels are public, enabling contamination and direct prompt tuning.

**Verified facts**
- The paper and official Hugging Face release agree on 4,723 questions, 31 legal fields, six formats, zero-shot evaluation, and the public test-only organization.
- The official Dataset Viewer reports exactly 4,723 rows; the Hub API records creation on 2024-10-28 and update on 2026-05-06.

**Inference**
- Because label quality is measured only on samples, a fresh expert-reviewed subset is necessary for any procurement claim.

**Unresolved ambiguity**
- No official GitHub repository, leaderboard, project site, or benchmark license was located.
- The paper names balanced accuracy, F1, and weighted aggregation but no separately versioned scorer implementation was located.

**Related entries**

- [LegalBench](reasoning-education.md#legalbench)
- [LEXam](reasoning-education.md#lexam)
- [OAB-Bench](reasoning-education.md#oab-bench)

[Back to page index](#on-this-page)

<a id="oab-bench"></a>
## OAB-Bench

`oab-bench` · **benchmark** · **specialist** · active

Draft Brazilian legal documents and answer discursive professional-exam questions under official examiner guidelines.

**Also known as:** oab-bench

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | Maritaca AI / OAB-Bench authors (mixed; commercial interest) |
| Catalog geography | Brazil |
| Last verified update | [2026-06-01](https://huggingface.co/datasets/maritaca-ai/oab-bench)<br>*Hugging Face dataset update for the expanded release* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Evaluate Portuguese-language legal drafting and discursive answers against Brazilian Bar Examination Phase 2 grading criteria.
- Audit criterion-level LLM-judge decisions through the structured JSON scorer instead of relying only on a total score.
- Compare model passing rates across seven practice areas while keeping exam edition and judge version fixed.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | Official grading-table items define atomic legal-writing requirements; an LLM judge scores each item, programmatic summation produces a 0–10 question score, and a six-point threshold operationalizes exam passing at the edition-by-area level. |
| Jurisdiction | Brazil |
| Languages | Portuguese (Brazilian) |
| Size | Current v2 contains 210 unique questions across seven areas and six exam editions (39–44); Hugging Face exposes 420 rows because questions and matching guidelines are separate 210-row configs, not independent examples |
| Splits | Two public train configs named questions and guidelines; no hidden test split |
| Source material | Brazilian Bar Examination (OAB) Phase 2 legal-writing and discursive questions with the corresponding official examiner scoring guidelines |
| Input | Open-ended legal-writing or discursive question, with reference materials and scoring table where supplied |
| Output | A drafted legal document or prose legal answer |
| Baselines / leaderboard context | The original paper evaluates four LLMs on 105 questions and validates automated judging against human scores; the current v2 repository reports 12 models on 210 questions, led by Gemini 3.1 Pro at 9.39 average and 42/42 exams passed under the GPT-5.2 structured judge. |
| Dataset access | Public GitHub and Hugging Face release with questions, guidelines, outputs, and evaluation code |
| License | Apache-2.0 for the repository and Hugging Face release |
| Gating | None observed; model APIs are required to reproduce hosted-model and judge runs |
| Maintenance | Active versioned benchmark: v1 had 105 questions from editions 39–41; the March 2026 v2 release added editions 42–44, structured judging, and a 12-model table. |
| Reproducibility | Good for a pinned data, output, and judge configuration because the harness and structured judgments are public; headline scores remain dependent on a hosted proprietary judge and API snapshots. |

### Metrics

- **Criterion-summed score (0–10):** The recommended structured GPT-5.2 judge evaluates each guideline item independently and returns item scores; code sums the item scores into the question total. Judge: GPT-5.2 with high reasoning effort in the current v2 protocol. **Primary.**
- **Average score and passing rate:** Average question scores and count edition-by-area exams scoring at least 6.0; v2 reports 42 exams from six editions times seven areas. Judge: GPT-5.2 for current reported results. **Primary.**

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | [https://github.com/maritaca-ai/oab-bench](https://github.com/maritaca-ai/oab-bench) |
| Hugging Face | [https://huggingface.co/datasets/maritaca-ai/oab-bench](https://huggingface.co/datasets/maritaca-ai/oab-bench) |
| Paper / arXiv | [https://arxiv.org/abs/2504.21202](https://arxiv.org/abs/2504.21202) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- Public exam questions, official guidelines, and reference outputs create contamination and targeted-optimization risk.
- Judge upgrades can change scores even when candidate outputs are fixed; v1 and v2 results are not directly interchangeable.
- The two Hub configs duplicate question identities and must not be counted as 420 benchmark questions.
- Owner-reported model comparisons have a commercial-interest conflict and require independent reruns.

**Verified facts**
- The official repository and Hub release define the v1/v2 lineage, 210 current questions, seven areas, six editions, two overlapping configs, Apache-2.0 terms, structured scoring, and the 42-exam passing denominator.
- Official GitHub and Hugging Face APIs record initial public creation on 2025-04-28/29 and the latest Hub update on 2026-06-01.

**Inference**
- OAB-Bench is more directly relevant to Brazilian legal writing than closed-form bar-exam accuracy, but it still does not simulate client files or iterative practice workflow.

**Unresolved ambiguity**
- No separately operated leaderboard was located; the result table lives in the mutable repository README.

**Related entries**

- [LegalBench.PT](reasoning-education.md#legalbench-pt)
- [LegalBench](reasoning-education.md#legalbench)
- [Harvey Legal Agent Benchmark (LAB)](agents-workflows.md#harvey-lab)

[Back to page index](#on-this-page)

<a id="prbench"></a>
## Professional Reasoning Benchmark (PRBench)

`prbench` · **benchmark** · **check before use** · active

Produce open-ended professional legal analysis that satisfies granular expert-authored criteria.

**Also known as:** PRBench

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | Scale AI / JusticeBench (company; commercial interest) |
| Catalog geography | Multi-jurisdiction and supranational |
| Last verified update | [2026-06-24](https://huggingface.co/datasets/ScaleAI/PRBench)<br>*Hugging Face dataset update* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare open-response legal reasoning on 500 practitioner-authored tasks spanning 114 countries and 47 US jurisdictions.
- Shortlist models for professional legal analysis using weighted atomic criteria rather than multiple-choice accuracy.
- Adapt the weighted-rubric protocol when building a fresh, jurisdiction-specific professional holdout.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
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

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | PLawBench authors / SKYLENAGE-AI (mixed; commercial interest unclear) |
| Catalog geography | China |
| Last verified update | [2026-07](https://aclanthology.org/2026.acl-long.458/)<br>*ACL 2026 publication* |
| Access level | partial |
| Test labels | public |
| Independently runnable | partial |

### Possible use cases

- Test Chinese legal consultation, practical case analysis, and document drafting with granular rubric scoring.
- Compare models on open-ended Chinese legal work after verifying which portion of the reported corpus is actually released.
- Use the scenario and rubric taxonomy as a starting point for a private Chinese-law evaluation.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | Scenario-specific rubric items measure whether an open response covers expected legal issues and work-product requirements. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | Paper reports 850 questions in 13 scenarios with about 12,500 rubric items; current public artifacts expose about 280 items |
| Splits | Paper-defined evaluation collection; public artifact completeness is unresolved |
| Source material | Chinese legal consultation, practical cases, and drafting scenarios |
| Input | Question, facts, or drafting instruction |
| Output | Legal advice, case analysis, or drafted document |
| Baselines / leaderboard context | ACL paper reports model comparisons across the three task families. |
| Dataset access | Partial public repository |
| License | No clear repository-wide license located |
| Gating | No account gate observed; artifact appears incomplete relative to the paper |
| Maintenance | Recent ACL 2026 release; no stable versioned complete package was verified. |
| Reproducibility | Partial until the reported 850-question corpus, evaluator model, prompts, and aggregation are reconciled with the public files. |

### Metrics

- **Item-level rubric scoring rate:** An LLM evaluator checks granular expected items; report scenario-level results and the exact evaluator configuration. Judge: LLM evaluator; exact public model/version unresolved. **Primary.**

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | [https://github.com/SKYLENAGE-AI/PLawBench](https://github.com/SKYLENAGE-AI/PLawBench) |
| Hugging Face | None located |
| Paper / arXiv | [https://aclanthology.org/2026.acl-long.458/](https://aclanthology.org/2026.acl-long.458/) |
| Leaderboard / competition | None located |
| Project | None located |

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

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | LexGenius authors (academic) |
| Catalog geography | China |
| Last verified update | [2026-04-16](https://arxiv.org/abs/2512.04578)<br>*arXiv v3 revision* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare Chinese legal knowledge and reasoning across civil, criminal, and commercial law on 8,385 multiple-choice questions.
- Contrast model results with the benchmark's legal-professional human baseline.
- Use dimension and ability scores to find capability gaps before constructing a fresh Chinese-law holdout.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
| GitHub | [https://github.com/QwenQKing/LexGenius](https://github.com/QwenQKing/LexGenius) |
| Hugging Face | None located |
| Paper / arXiv | [https://arxiv.org/abs/2512.04578](https://arxiv.org/abs/2512.04578)<br>[https://aclanthology.org/2026.findings-acl.926/](https://aclanthology.org/2026.findings-acl.926/) |
| Leaderboard / competition | None located |
| Project | None located |

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

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | PILOT-Bench authors / TeamLab (academic) |
| Catalog geography | United States |
| Last verified update | [2026-03-10](https://huggingface.co/datasets/Yehoon/pilot-bench)<br>*Hugging Face dataset and GitHub repository update* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test issue, rule, and conclusion classification on US Patent Trial and Appeal Board appeals.
- Compare legal reasoning under appellant/examiner-separated, merged, and claim-augmented input settings.
- Diagnose label coverage and class imbalance using exact, micro, macro, weighted, and balanced metrics.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
| GitHub | [https://github.com/TeamLab/pilot-bench](https://github.com/TeamLab/pilot-bench) |
| Hugging Face | [https://huggingface.co/datasets/Yehoon/pilot-bench](https://huggingface.co/datasets/Yehoon/pilot-bench) |
| Paper / arXiv | [https://arxiv.org/abs/2601.04758](https://arxiv.org/abs/2601.04758)<br>[https://aclanthology.org/2025.nllp-1.17/](https://aclanthology.org/2025.nllp-1.17/) |
| Leaderboard / competition | None located |
| Project | None located |

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

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | MoZIP authors / AI-for-Science (academic) |
| Catalog geography | Multi-jurisdiction and supranational |
| Last verified update | [2024-08-20](https://github.com/AI-for-Science/MoZi)<br>*Canonical GitHub repository push* |
| Access level | open |
| Test labels | public |
| Independently runnable | partial |

### Possible use cases

- Compare multilingual intellectual-property knowledge on public multiple-choice questions across Chinese, English, German, Spanish, Japanese, Korean, and Portuguese.
- Evaluate open-ended intellectual-property answers with a disclosed human pairwise preference protocol in seven languages.
- Test Chinese and English patent-abstract matching while auditing whether distractor construction creates retrieval shortcuts.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
| GitHub | [https://github.com/AI-for-Science/MoZi](https://github.com/AI-for-Science/MoZi) |
| Hugging Face | [https://huggingface.co/datasets/BNNT/IPQuiz](https://huggingface.co/datasets/BNNT/IPQuiz)<br>[https://huggingface.co/datasets/BNNT/IPQA](https://huggingface.co/datasets/BNNT/IPQA)<br>[https://huggingface.co/datasets/BNNT/PatentMatch](https://huggingface.co/datasets/BNNT/PatentMatch) |
| Paper / arXiv | [https://arxiv.org/abs/2402.16389](https://arxiv.org/abs/2402.16389)<br>[https://aclanthology.org/2024.lrec-main.1018/](https://aclanthology.org/2024.lrec-main.1018/) |
| Leaderboard / competition | None located |
| Project | None located |

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

<a id="judge"></a>
## JuDGE

`judge` · **benchmark** · **specialist** · fixed-release

Generate a complete Chinese criminal judgment document from a factual description.

**Also known as:** Judgment Document Generation Evaluation

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | JuDGE authors / Tsinghua University (academic) |
| Catalog geography | China |
| Last verified update | [2025-08-07](https://github.com/oneal2000/JuDGE)<br>*GitHub repository push* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Evaluate Chinese criminal-judgment document generation from case facts with separate penalty, charge, statutory-reference, reasoning, and judgment-result metrics.
- Compare direct generation, in-context learning, supervised fine-tuning, and multi-source RAG under the released 2,004/501 split.
- Use the public evaluation scripts as a starting point for document-generation diagnostics while adding expert review for legal validity.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | Twelve automatic measures compare a generated judgment with the authoritative reference across penalties, charges, cited statutes, reasoning text, and judgment-result text; this is document generation, not appellate error review. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | 2,505 expert-filtered fact–judgment pairs; 103,251 supplementary judgment documents and 55,348 statutory articles |
| Splits | 2,004 train and 501 test pairs (4:1); public labels and reference judgments |
| Source material | China Judgments Online criminal judgments, transformed into structured fact/reasoning/judgment/penalty/charge/statute fields and filtered by two law-student reviewers |
| Input | Case factual description, optionally with retrieved statutes and precedent judgments |
| Output | Full judgment document including judicial reasoning, result, sentence, fine, charges, and statutory references |
| Baselines / leaderboard context | The paper compares Qwen2.5 3B/7B base and instruct models, HanFei-7B, and LexiLaw-6B using direct generation, in-context learning, supervised fine-tuning, and multi-source RAG where applicable. |
| Dataset access | Public subset and test references in GitHub; the official README links a larger Google Drive corpus |
| License | MIT repository and dataset according to the official paper and README |
| Gating | None for GitHub; external Google Drive hosts the full supplementary corpus |
| Maintenance | The repository was last pushed August 7, 2025 and has no tagged releases; pin a commit and the external corpus revision. |
| Reproducibility | Public data, expected outputs, evaluation scripts, prompts, and baseline result files support reruns, but external corpus hosting and model-version drift still need pinning. |

### Metrics

- **Penalty accuracy:** Normalized similarity for predicted versus reference prison term and fine, implemented by the official evaluation scripts. **Primary.**
- **Charge and statutory-reference precision / recall / F1:** Set-based classification scores separately evaluate convictions and cited criminal-law provisions. **Primary.**
- **Reasoning and judgment METEOR / BERTScore:** Reference-based lexical/semantic similarity is reported separately for the judicial-reasoning and judgment-result sections. **Primary.**

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | [https://github.com/oneal2000/JuDGE](https://github.com/oneal2000/JuDGE) |
| Hugging Face | None located |
| Paper / arXiv | [https://arxiv.org/abs/2503.14258](https://arxiv.org/abs/2503.14258) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- The split and gold documents are public, creating contamination and direct overfitting risk.
- METEOR and BERTScore reward reference similarity but do not establish that alternative legal reasoning is valid or that the generated judgment is lawful.
- The paper reports anonymization and expert filtering, but downstream users still need their own privacy and source-rights review.

**Verified facts**
- The official repository contains the data, 4:1 preparation script, expected outputs, automated evaluators, baseline code/results, and MIT license.
- The official SIGIR paper reports 2,505 pairs, the 2,004/501 split, 103,251 judgment corpus, 55,348 statutes, and all twelve automatic metrics.

**Unresolved ambiguity**
- No canonical Hugging Face dataset or maintained leaderboard was located.
- The AR-BENCH paper says it reannotates JuDGE material for appellate review; JuDGE remains a separate judgment-generation benchmark and is not an AR-BENCH release.

**Related entries**

- [LawBench](reasoning-education.md#lawbench)
- [Ready Jurist One (J1Bench)](agents-workflows.md#ready-jurist-one)
- [STARD](retrieval-rag-citation.md#stard)

[Back to page index](#on-this-page)

<a id="vlegal-bench"></a>
## VLegal-Bench

`vlegal-bench` · **benchmark-suite** · **check before use** · active

Evaluate Vietnamese legal recognition, understanding, reasoning, interpretation, generation, and professional ethics across 22 named tasks.

**Also known as:** VietLegal

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | VLegal-Bench authors / CMC Institute of Science and Technology (mixed; commercial interest unclear) |
| Catalog geography | Vietnam |
| Last verified update | [2026-04-17](https://arxiv.org/abs/2512.14554)<br>*arXiv v5 revision* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Evaluate Vietnamese legal knowledge, understanding, reasoning, drafting, and ethics with task-specific metrics.
- Use the public prompts and evaluator code as a reproducible Vietnamese-law diagnostic after pinning the exact repository revision.
- Design a private Vietnamese-law holdout using the released task taxonomy without reusing its public gold answers.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | Bloom-inspired task levels separate recall and structuring from inference, generation, and ethics; task-specific scores should be reported rather than treated as one validated legal-capability scale. |
| Jurisdiction | Vietnam |
| Languages | Vietnamese |
| Size | Paper reports 10,450 examples across 22 tasks; the verified repository contains 10,467 JSONL lines across 23 task/subtask files |
| Splits | Public evaluation files with gold labels; no hidden test or unified train/development/test split |
| Source material | Vietnamese statutes, legal questions, cases, documents, and authored or transformed task material |
| Input | Task-dependent legal text, question, facts, choices, graph structure, or drafting instruction |
| Output | Choice, label, span, graph, or generated Vietnamese legal text |
| Baselines / leaderboard context | The paper evaluates Vietnamese-capable, open, and frontier language models across the five ability levels; no maintained leaderboard was located. |
| Dataset access | Public GitHub task files, prompts, inference code, and evaluation code |
| License | CC BY-NC-ND 4.0 in the repository license file |
| Gating | None observed; no canonical Hugging Face dataset was located |
| Maintenance | Active 2026 research release; pin a commit because the paper has multiple revisions and the project uses both VLegal-Bench and VietLegal names. |
| Reproducibility | Good for rerunning the public task files, but the paper/repository count mismatch and NoDerivatives license constrain modification and redistribution of derived splits. |

### Metrics

- **Task-specific accuracy / exact match / F1:** Use the repository's evaluator for closed-form, classification, extraction, and structure tasks; report every task separately. **Primary.**
- **ROUGE-L and structure F1:** Use ROUGE-L for designated generation tasks and node/edge F1 for designated structure tasks; do not average these as equivalent units without a disclosed rule.

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | [https://github.com/hieunguyen1053/vlegal-bench](https://github.com/hieunguyen1053/vlegal-bench) |
| Hugging Face | None located |
| Paper / arXiv | [https://arxiv.org/abs/2512.14554](https://arxiv.org/abs/2512.14554) |
| Leaderboard / competition | None located |
| Project | [https://vilegalbench.cmcai.vn/](https://vilegalbench.cmcai.vn/) |

### Validity and evidence

**Risks / caveats**
- All gold labels are public, creating contamination and direct benchmark-targeting risk.
- The paper's 10,450 total and repository's 10,467 JSONL lines do not reconcile.
- CC BY-NC-ND 4.0 prohibits commercial use and distribution of adapted material.

**Verified facts**
- The official arXiv record, GitHub repository, and project page establish a Vietnamese-law suite with 22 named task directories, public data, prompts, evaluator code, and CC BY-NC-ND 4.0 terms.
- A direct count of the released JSONL files produced 10,467 lines, while the paper's task table totals 10,450.

**Inference**
- The suite fills a jurisdiction gap but is not evidence of deployable end-to-end Vietnamese legal practice.

**Unresolved ambiguity**
- The paper uses VietLegal internally while the arXiv title and repository use VLegal-Bench; no canonical Hugging Face release was located.

[Back to page index](#on-this-page)

<a id="mizanqa"></a>
## MizanQA

`mizanqa` · **benchmark** · **check before use** · fixed-release

Answer expert-verified multiple-choice questions about Moroccan law and associated legal traditions.

**Also known as:** MizanQA-v0

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | MizanQA authors (academic) |
| Catalog geography | Morocco |
| Last verified update | [2026-03](https://aclanthology.org/2026.eacl-industry.10/)<br>*EACL 2026 Industry Track publication* |
| Access level | open |
| Test labels | public |
| Independently runnable | partial |

### Possible use cases

- Evaluate Arabic multiple-choice knowledge of Moroccan law, legal institutions, Maliki jurisprudence, and customary-law context.
- Compare strict correctness with partial-answer and calibration-aware measures on a pinned release.
- Build a fresh Moroccan-law evaluation while using MizanQA only as a public development diagnostic.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | Strict accuracy tests exact answer-set correctness; F1-like alpha and PMPA beta add tunable penalties for wrong selections; option-level and set-level expected calibration error compare confidence with observed correctness. |
| Jurisdiction | Morocco |
| Languages | Arabic (Modern Standard Arabic with Moroccan legal usage) |
| Size | Paper reports 1,776 expert-verified questions; the live Hugging Face release exposes 1,769 rows |
| Splits | One public split named train; no hidden test |
| Source material | Public Moroccan-law MCQ banks and exams, temporally curated by a legal expert, extracted with Gemini 2.0 Flash, then manually verified and categorized |
| Input | Arabic legal question with a variable option set, including multi-answer questions |
| Output | Selected answer option set with a confidence for each selected option |
| Baselines / leaderboard context | The paper evaluates Allam-2, Gemini 1.5/2.0 Flash, Llama 3.3/4, and other Arabic-capable models. |
| Dataset access | Public Hugging Face parquet and card |
| License | No dataset license declared in the verified Hugging Face metadata |
| Gating | None observed |
| Maintenance | Fixed public v0 release followed by an EACL 2026 publication; no code repository or maintained leaderboard was located. |
| Reproducibility | Partial: the rows are public and strict accuracy is simple, but the paper-only PMPA/calibration implementations, missing license, and count mismatch require local reconstruction. |

### Metrics

- **Strict accuracy:** Credit a question only when the predicted option set exactly equals the gold option set. **Primary.**
- **F1-like alpha / PMPA beta:** The F1-like score uses precision/recall-style overlap and alpha to increase the penalty for wrong selections; PMPA uses beta as an incorrect-answer penalty and is intended for varying gold-set sizes. The Hub release does not include a standalone scorer.
- **Option-level / set-level expected calibration error:** Bin confidence into equally spaced intervals. Option-level ECE treats option predictions separately; set-level ECE treats exact set match as correctness and multiplies selected-option confidences under an independence assumption.

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | None located |
| Hugging Face | [https://huggingface.co/datasets/adlbh/MizanQA-v0](https://huggingface.co/datasets/adlbh/MizanQA-v0) |
| Paper / arXiv | [https://arxiv.org/abs/2508.16357](https://arxiv.org/abs/2508.16357)<br>[https://aclanthology.org/2026.eacl-industry.10/](https://aclanthology.org/2026.eacl-industry.10/) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- The public rows and labels permit direct tuning and contamination.
- The paper and live release differ by seven questions.
- The paper's metric section says option counts vary from 2 to 16, while its dataset table says 2 to 12.
- One public split does not provide an independently held-out evaluation boundary.

**Verified facts**
- The arXiv paper, EACL record, and official Hugging Face release establish the Moroccan-law multi-answer task, construction pipeline, exact-set accuracy, alpha/beta partial-credit metrics, two ECE variants, and public artifact.
- The Hugging Face Dataset Viewer exposes 1,769 rows, not the paper's 1,776.

**Inference**
- Calibration metrics make MizanQA useful for confidence analysis, but they do not establish professional legal competence.

**Unresolved ambiguity**
- No public scorer code, license declaration, GitHub repository, or hidden test was located.
- The paper conflicts internally on whether the maximum option count is 12 or 16.

[Back to page index](#on-this-page)

<a id="lexsumm"></a>
## LexSumm

`lexsumm` · **benchmark-suite** · **check before use** · fixed-release

Generate abstractive summaries of legislation, cases, and government/legal reports across eight public datasets.

**Also known as:** LexSumm-LexT5

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | LexSumm authors / TUM Legal Tech (academic) |
| Catalog geography | Multi-jurisdiction and supranational |
| Last verified update | [2024-11-19](https://github.com/TUMLegalTech/LexSumm-LexT5)<br>*Canonical GitHub repository push* |
| Access level | open |
| Test labels | public |
| Independently runnable | partial |

### Possible use cases

- Compare long-document legal summarization models across eight fixed public dataset configurations.
- Analyze per-jurisdiction and per-document-type summarization performance without claiming a unified legal-fidelity score.
- Use the LexT5 baselines as a reproducible starting point before adding expert factuality and legal-effect review.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | ROUGE and BERTScore measure reference similarity per dataset; the suite does not implement a separate legal-faithfulness metric or validated cross-dataset aggregate. |
| Jurisdiction | United States, United Kingdom, European Union, India, Multi-jurisdictional legal sources |
| Languages | English |
| Size | 60,386 rows across eight Hugging Face configurations: BillSum 22,218; EUR-Lex-Sum 1,504; GovReport 19,463; IN-Abs 7,128; Multi-LexSum long 4,539, short 3,138, tiny 1,603; UK-Abs 793 |
| Splits | Every configuration exposes train, validation, and test splits |
| Source material | Bills, EU legislation, government reports, Indian and UK case summaries, and Multi-LexSum legal documents |
| Input | Long legal or government document |
| Output | Reference-style abstractive summary |
| Baselines / leaderboard context | The paper reports dataset-specific LED, PRIMERA, LongT5, SLED, Unlimiformer, and LexT5 baselines; it does not define one official aggregate rank. |
| Dataset access | Public Hugging Face dataset with eight configurations |
| License | No unified suite-wide license declaration was located; constituent dataset licenses and provenance differ |
| Gating | None observed |
| Maintenance | Fixed NLLP 2024 release; the Hub dataset was created and last updated in October 2024, and no maintained leaderboard was located. |
| Reproducibility | Partial: fixed rows and splits are public, but the repository is baseline-oriented and does not ship a unified scorer or one license for all constituents. |

### Metrics

- **ROUGE-1 / ROUGE-2 / ROUGE-L:** Compute reference n-gram and longest-common-subsequence overlap per dataset; retain each constituent split and do not imply legal correctness. **Primary.**
- **BERTScore:** Compute contextual embedding similarity against the reference summary per dataset.

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | [https://github.com/TUMLegalTech/LexSumm-LexT5](https://github.com/TUMLegalTech/LexSumm-LexT5) |
| Hugging Face | [https://huggingface.co/datasets/CJWeiss/LexSumm](https://huggingface.co/datasets/CJWeiss/LexSumm) |
| Paper / arXiv | [https://arxiv.org/abs/2410.09527](https://arxiv.org/abs/2410.09527)<br>[https://aclanthology.org/2024.nllp-1.35/](https://aclanthology.org/2024.nllp-1.35/) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- ROUGE and BERTScore can reward fluent overlap while missing factual or legally consequential errors.
- Constituent datasets differ in jurisdiction, document type, length, and source license, so aggregate comparisons are not construct-valid.
- All reference summaries are public and contamination-prone.

**Verified facts**
- The official paper, repository, and Hugging Face release establish eight configurations, 60,386 live rows, train/validation/test splits, and ROUGE/BERTScore reporting.
- The paper does not report the faithfulness metric attributed to it in a prior discovery pass; faithfulness appears only as a qualitative limitation.

**Inference**
- LexSumm qualifies as a fixed summarization suite, but its scores support reference-similarity claims rather than legal-fidelity claims.

**Unresolved ambiguity**
- No unified data license, official aggregate, hidden test, or maintained leaderboard was located.

[Back to page index](#on-this-page)
