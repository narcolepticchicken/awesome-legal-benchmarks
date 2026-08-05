# Prediction, fairness, and structured reasoning

<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->

Outcome prediction, subgroup performance, holding selection, deontic rules, and structured legal analysis.

Snapshot: **2026-08-04** · 7 entries

[Back to README](../../README.md) · [Catalog index](../catalog.md) · [Selection guide](../selection-guide.md) · [Metric field guide](../metric-theory.md) · [Methodology](../methodology.md)

## On this page

- [ECtHR Tasks A/B](#ecthr)
- [FairLex](#fairlex)
- [CaseHOLD](#casehold)
- [DeonticBench](#deonticbench)
- [MSLR-Bench](#mslr)
- [MASLegalBench](#maslegalbench)
- [OpenExempt](#openexempt)

<a id="ecthr"></a>
## ECtHR Tasks A/B

`ecthr` · **benchmark** · **recommended** · fixed-release

Predict European Convention articles alleged (Task A) or found violated (Task B) from case facts.

**Also known as:** ECtHR Task

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | ECtHR task authors / LexGLUE (academic) |
| First documented | [2019-06-05](https://arxiv.org/abs/1906.02059) — arXiv v1 submission |
| Latest verified update | [2022-11-08](https://arxiv.org/abs/2110.00976) — LexGLUE arXiv revision |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Research fact-to-doctrine mapping: predict alleged (Task A) or violated (Task B) Convention articles from ECtHR case facts.
- Compare long-document classification architectures on multi-label legal prediction with fixed splits.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Multi-label outcome prediction tests fact-to-doctrine mapping; macro-F1 emphasizes less frequent Convention articles and micro-F1 the total decision mass. |
| Jurisdiction | European Court of Human Rights / Council of Europe |
| Languages | English |
| Size | Roughly 11,000 cases per LexGLUE Task A/B configuration |
| Splits | Commonly 9,000 train / 1,000 validation / 1,000 test |
| Source material | Public ECtHR judgments and case facts |
| Input | Case-fact section |
| Output | Multi-label Convention article IDs |
| Baselines / leaderboard context | Original Chalkidis et al. work and LexGLUE report transformer and long-document baselines. |
| Dataset access | Public LexGLUE configs ecthr_a and ecthr_b |
| License | LexGLUE package CC BY 4.0 |
| Gating | None |
| Maintenance | Stable LexGLUE release; the older coastalcph/ecthr_cases HF path is stale. |
| Reproducibility | Good with the exact task config, long-document truncation strategy, and thresholding specified. |

### Metrics

- **Micro-F1 and macro-F1:** F1 is computed over article labels with micro and label-macro aggregation. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/coastalcph/lex-glue](https://github.com/coastalcph/lex-glue) |
| Hugging Face | [https://huggingface.co/datasets/coastalcph/lex_glue](https://huggingface.co/datasets/coastalcph/lex_glue) |
| Paper / arXiv | [https://arxiv.org/abs/1906.02059](https://arxiv.org/abs/1906.02059)<br>[https://arxiv.org/abs/2110.00976](https://arxiv.org/abs/2110.00976) |

### Validity and evidence

**Risks / caveats**
- Judgments and labels are public and likely represented in pretraining corpora.
- Outcome labels can be learned from stylistic or temporal shortcuts rather than legal reasoning.

**Verified facts**
- LexGLUE is the current canonical distribution path.

**Unresolved ambiguity**
- Counts vary slightly across original and standardized releases.

**Related entries**

- [LexGLUE](reasoning-education.md#lexglue)

Original source bullet(s): #6

[Back to page index](#on-this-page)

<a id="fairlex"></a>
## FairLex

`fairlex` · **benchmark-suite** · **recommended** · fixed-release

Evaluate legal prediction performance and group robustness across sensitive or legally salient subpopulations.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | FairLex authors (academic) |
| First documented | [2022-05](https://aclanthology.org/2022.acl-long.301/) — ACL Anthology publication month |
| Latest verified update | [2023-07-27](https://huggingface.co/datasets/coastalcph/fairlex) — Hugging Face dataset update |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Measure per-group, worst-group, and gap performance on legal prediction tasks across gender, age, region, language, and legal-area attributes.
- Test whether robustness interventions improve worst-group scores on legal tasks.
- Produce subgroup-performance documentation as one input to a product evaluation.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | FairLex pairs overall macro-F1 with worst-group and disparity views; fairness is operationalized as performance robustness across observed demographic/geographic/legal groups, not demographic parity of decisions. |
| Jurisdiction | Council of Europe, United States, Switzerland, China |
| Languages | English, German, French, Italian, Chinese |
| Size | Four legal datasets |
| Splits | WILDS-style distribution and group-aware splits/configs |
| Source material | Court decisions with gender, age, region, language, and legal-area attributes where available |
| Input | Case/document text |
| Output | Outcome or legal label |
| Baselines / leaderboard context | Official code evaluates standard, reweighting, and robustness/fairness methods. |
| Dataset access | Public package |
| License | Dataset/config-specific; inspect constituent terms |
| Gating | None observed |
| Maintenance | Stable research release. |
| Reproducibility | Good when subgroup definitions, minimum group sizes, and random seeds are retained. |

### Metrics

- **All-group macro-F1:** Macro-F1 over the full evaluation population. **Primary.**
- **Worst-group macro-F1 / group disparity:** Minimum subgroup performance and gaps across specified protected/context groups. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/coastalcph/fairlex](https://github.com/coastalcph/fairlex) |
| Hugging Face | [https://huggingface.co/datasets/coastalcph/fairlex](https://huggingface.co/datasets/coastalcph/fairlex) |
| Paper / arXiv | [https://aclanthology.org/2022.acl-long.301/](https://aclanthology.org/2022.acl-long.301/) |

### Validity and evidence

**Risks / caveats**
- Observed metadata are imperfect proxies for legally meaningful disadvantage.
- Worst-group estimates can be high variance for small groups.

**Verified facts**
- Official paper/repository cover four jurisdictions and five languages with group-robustness metrics.

[Back to page index](#on-this-page)

<a id="casehold"></a>
## CaseHOLD

`casehold` · **benchmark** · **specialist** · fixed-release

Select the correct holding that completes an excerpt from a US judicial opinion.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | CaseHOLD authors (academic) |
| First documented | [2021-04-18](https://arxiv.org/abs/2104.08671) — arXiv v1 submission |
| Latest verified update | [2021-07-06](https://arxiv.org/abs/2104.08671) — arXiv revision |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test discrimination of the correct case holding from hard distractors on US judicial opinion excerpts.
- Research the benefit of legal-domain pretraining on case-law reading.
- Quick screen of US case-law comprehension before deeper task-specific evaluation.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Five-choice accuracy measures discrimination of the true legal holding from hard negatives generated/retrieved to resemble plausible case law. |
| Jurisdiction | United States |
| Languages | English |
| Size | More than 53,000 five-choice questions |
| Splits | Official train/dev/test files; also standardized in LexGLUE |
| Source material | US case law and extracted holdings |
| Input | Opinion excerpt plus five candidate holdings |
| Output | Correct option |
| Baselines / leaderboard context | Legal-BERT and other pretrained language models in the original paper; further baselines in LexGLUE. |
| Dataset access | Public |
| License | Release/derived case-law terms apply; LexGLUE package CC BY 4.0 |
| Gating | None |
| Maintenance | Stable; LexGLUE is the easiest standardized distribution. |
| Reproducibility | High for exact-choice scoring with the same variant and split. |

### Metrics

- **Accuracy:** Exact five-way choice accuracy. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/neelguha/legal-ml-datasets](https://github.com/neelguha/legal-ml-datasets)<br>[https://github.com/coastalcph/lex-glue](https://github.com/coastalcph/lex-glue) |
| Hugging Face | [https://huggingface.co/datasets/coastalcph/lex_glue](https://huggingface.co/datasets/coastalcph/lex_glue) |
| Paper / arXiv | [https://arxiv.org/abs/2104.08671](https://arxiv.org/abs/2104.08671) |

### Validity and evidence

**Risks / caveats**
- Public US opinions and fixed distractors are contamination-prone.
- Models may exploit distractor-generation artifacts rather than legal reasoning.

**Verified facts**
- Original dataset repo/paper and LexGLUE establish the canonical task.

**Unresolved ambiguity**
- A separate current author-owned HF dataset was not located outside LexGLUE.

**Related entries**

- [LexGLUE](reasoning-education.md#lexglue)

[Back to page index](#on-this-page)

<a id="deonticbench"></a>
## DeonticBench

`deonticbench` · **benchmark-suite** · **recommended** · active

Reason about obligations, permissions, prohibitions, eligibility, and amounts under long legal/policy rules, directly or through executable Prolog.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | DeonticBench authors (academic) |
| First documented | [2026-04-06](https://arxiv.org/abs/2604.04443) — arXiv v1 submission |
| Latest verified update | [2026-06-04](https://huggingface.co/datasets/gydou/DeonticBench) — Hugging Face dataset update |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test rule application over US tax, immigration, housing, and airline-policy rules with exact outcomes and executable Prolog references.
- Diagnose whether failures come from wrong formalization, solver execution, abstention, or wrong final answers.
- Regression-test reasoning changes using the bootstrap confidence-interval protocol on a pinned post-audit revision.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Exact outcomes test rule application; executable reference programs expose a symbolic proof path and distinguish wrong legal formalization, solver failure, abstention, and wrong final answer. |
| Jurisdiction | United States federal tax, United States immigration, United States state housing, Airline policies |
| Languages | English, Prolog |
| Size | 6,232 whole-set tasks: SARA Numeric 100, SARA Binary 276, Airline 300, Housing 5,314, USCIS-AAO 242 |
| Splits | Whole plus curated hard subsets (35/30/80/78/28) and derived five-case smoke splits |
| Source material | US tax statutes, airline policies, state housing law, and USCIS AAO decisions with audited reference Prolog |
| Input | Rules/statutes, case facts, and a question |
| Output | Typed answer directly or generated Prolog program and solver result |
| Baselines / leaderboard context | Paper/repository evaluate direct, zero-shot Prolog, and few-shot Prolog across frontier/coding models and training methods. |
| Dataset access | Public |
| License | See official repository/HF metadata and constituent-source terms |
| Gating | None for data; API models may require credentials |
| Maintenance | Active; reference programs were audited/corrected on 2026-05-26. |
| Reproducibility | Strong executable oracle and bootstrap script; pin post-audit dataset revision, SWI-Prolog, prompts, and model versions. |

### Metrics

- **Bootstrapped accuracy with 95% CI:** 1,000 case-resampling replicates; one generation sampled per case. Numeric domains allow ±1 rounding tolerance; categorical domains require exact match. **Primary.**
- **Abstention and wrong rate:** Empty/error/timeout Prolog or unparsable direct answer counts as abstention; remaining incorrect parses count wrong.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/guangyaodou/DeonticBench](https://github.com/guangyaodou/DeonticBench) |
| Hugging Face | [https://huggingface.co/datasets/gydou/DeonticBench](https://huggingface.co/datasets/gydou/DeonticBench) |
| Paper / arXiv | [https://arxiv.org/abs/2604.04443](https://arxiv.org/abs/2604.04443) |
| Project | [https://guangyaodou.github.io/DeonticBench/](https://guangyaodou.github.io/DeonticBench/) |

### Validity and evidence

**Risks / caveats**
- The hard split is a subset of the public whole set, so benchmark-targeted training is possible.
- Reference Prolog was materially corrected after release, proving revision pinning is essential.

**Verified facts**
- Official GitHub/HF/paper provide all domain counts, splits, solver workflow, and bootstrap protocol.

**Inference**
- Executable traces improve diagnosability but do not guarantee the formalization captures every legally relevant ambiguity.

[Back to page index](#on-this-page)

<a id="mslr"></a>
## MSLR-Bench

`mslr` · **benchmark** · **check before use** · active

Extract structured facts and produce IRAC-style reasoning for Chinese insider-trading cases.

**Also known as:** MSLR

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | MSLR-Bench authors (academic) |
| First documented | [2025-11-11](https://arxiv.org/abs/2511.07979) — arXiv v1 submission |
| Latest verified update | [2026-06-29](https://github.com/yuwenhan07/MSLR-Bench) — GitHub repository push |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test structured field extraction from Chinese insider-trading decisions against 59,771 labeled fields.
- Test whether generated case analysis covers the expected IRAC components via IRAC recall.
- Research corpus for Chinese financial-enforcement reasoning tasks.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Field-level extraction metrics test factual structure; IRAC recall and an LLM judge test whether generated analysis covers expected legal reasoning components. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | 1,389 cases from 2005–2024 with 59,771 fields |
| Splits | HF visibly exposes one train split |
| Source material | Public Chinese insider-trading enforcement/case materials |
| Input | Case documents |
| Output | Structured JSON fields and free-text IRAC analysis |
| Baselines / leaderboard context | Official paper compares general and legal LLMs; headline percentages must be tied to a named metric. |
| Dataset access | Public |
| License | GitHub Apache-2.0 versus HF MIT metadata conflict |
| Gating | None observed |
| Maintenance | Active recent release. |
| Reproducibility | Public artifacts exist, but split isolation, license metadata, and judge version require resolution. |

### Metrics

- **Field accuracy / FCR:** Exact or normalized field correctness plus the paper's field-completion/consistency measure. **Primary.**
- **IRAC Recall and judge score:** Recall of expected IRAC elements plus LLM evaluation of generated reasoning. Judge: DeepSeek-V3. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/yuwenhan07/MSLR-Bench](https://github.com/yuwenhan07/MSLR-Bench) |
| Hugging Face | [https://huggingface.co/datasets/Yuwh07/MSLR-Bench](https://huggingface.co/datasets/Yuwh07/MSLR-Bench) |
| Paper / arXiv | [https://arxiv.org/abs/2511.07979](https://arxiv.org/abs/2511.07979) |

### Validity and evidence

**Risks / caveats**
- One visible split allows accidental train/evaluation overlap.
- Public cases and a single LLM judge create contamination and evaluator-bias risk.

**Verified facts**
- Official GitHub/HF/paper agree on the case/field scale.

**Unresolved ambiguity**
- Repository and HF licenses conflict; no hidden held-out split was verified.

Original source bullet(s): #16

[Back to page index](#on-this-page)

<a id="maslegalbench"></a>
## MASLegalBench

`maslegalbench` · **benchmark** · **check before use** · fixed-release

Multi-agent deductive reasoning about GDPR enforcement facts, rules, application, common sense, and conclusions.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | HKUST KnowComp (academic) |
| First documented | [2025-09-29](https://arxiv.org/abs/2509.24922) — arXiv v1 submission |
| Latest verified update | [2025-09-30](https://arxiv.org/abs/2509.24922) — arXiv revision |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare single-agent versus multi-agent architectures on GDPR-enforcement questions with retrievable report evidence.
- Test retrieval-at-k of supporting enforcement-report passages inside an agent pipeline.
- Research agent-coordination diagnostics (refusal, agreement statistics) in a legal setting.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Accuracy measures final MCQ correctness; retrieval-at-k tests evidence acquisition; refusal and agreement statistics diagnose coordination rather than legal validity directly. |
| Jurisdiction | United Kingdom / GDPR enforcement |
| Languages | English |
| Size | 950 MCQs from 15 UK enforcement reports: 647 yes/no and 303 four-choice |
| Splits | Public evaluation collection |
| Source material | Fifteen UK regulatory enforcement reports; questions generated with DeepSeek and reviewed |
| Input | Question plus retrievable report chunks |
| Output | Choice/yes-no answer and multi-agent traces |
| Baselines / leaderboard context | Paper compares single- and multi-agent configurations. |
| Dataset access | Public research release |
| License | MIT |
| Gating | Model APIs may be needed |
| Maintenance | Fixed recent research release. |
| Reproducibility | Prompts/code are public; hosted models and multi-agent stochasticity need repeated trials. |

### Metrics

- **Accuracy / refusal rate:** Exact final answer correctness and share of non-answers. **Primary.**
- **Retrieval@1/3/5 and Cohen's kappa:** Evidence-hit rates plus agent/human agreement statistics.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/HKUST-KnowComp/MASLegalBench](https://github.com/HKUST-KnowComp/MASLegalBench) |
| Paper / arXiv | [https://arxiv.org/abs/2509.24922](https://arxiv.org/abs/2509.24922) |

### Validity and evidence

**Risks / caveats**
- Only 15 source reports sharply limit source diversity.
- Generator-authored questions can encode DeepSeek artifacts and source overlap.

**Verified facts**
- Official paper/repository define 950 questions and the 647/303 split.

Original source bullet(s): #17

[Back to page index](#on-this-page)

<a id="openexempt"></a>
## OpenExempt

`openexempt` · **benchmark-suite** · **specialist** · active

Apply structured US bankruptcy exemption rules and remain robust under controlled perturbations.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | OpenExempt authors (academic) |
| First documented | [2026-01-11](https://huggingface.co/datasets/SergioServantez/OpenExempt) — Hugging Face dataset creation |
| Latest verified update | [2026-01-21](https://huggingface.co/datasets/SergioServantez/OpenExempt) — Hugging Face dataset update |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test symbolic statutory reasoning under US Bankruptcy Code exemption rules.
- Stress-test robustness to temporal changes, decomposition, scale, distractors, sycophancy, and obfuscation.
- Use deterministic gold solutions to separate rule-reasoning failures from LLM-judge noise.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Programmatically generated cases with deterministic symbolic solutions test rule application and targeted robustness properties without an LLM judge. |
| Jurisdiction | United States federal bankruptcy law |
| Languages | English |
| Size | 9,765 samples across nine competency and robustness suites |
| Splits | Nine suites covering competency, intermediate/advanced reasoning, temporal, decomposition, scaling, distractor, sycophancy, and obfuscation conditions |
| Source material | US Bankruptcy Code exemption rules and generated fact patterns |
| Input | Facts and applicable statutory rules |
| Output | Structured exemption determination or solution |
| Baselines / leaderboard context | Paper reports model performance across competency and robustness suites. |
| Dataset access | Public Hugging Face and GitHub release |
| License | CC BY 4.0 data |
| Gating | None; Hugging Face viewer may fail because the release uses a legacy dataset script |
| Maintenance | Fixed 2026 research release. |
| Reproducibility | Strong for the deterministic solver when code/data revisions are pinned. |

### Metrics

- **Deterministic suite accuracy:** Compare the model's structured answer with the symbolic solver's gold result; report each suite separately before any aggregate. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/servantez/OpenExempt](https://github.com/servantez/OpenExempt) |
| Hugging Face | [https://huggingface.co/datasets/SergioServantez/OpenExempt](https://huggingface.co/datasets/SergioServantez/OpenExempt) |
| Paper / arXiv | [https://arxiv.org/abs/2601.13183](https://arxiv.org/abs/2601.13183)<br>[https://aclanthology.org/2026.findings-acl.1328/](https://aclanthology.org/2026.findings-acl.1328/) |

### Validity and evidence

**Risks / caveats**
- Generated symbolic cases may not capture ambiguity, evidence, or procedure in real bankruptcy practice.
- Public generator and answers permit targeted optimization.
- A failing dataset viewer can be mistaken for unavailable data.

**Verified facts**
- Official GitHub, Hugging Face, arXiv, and ACL artifacts establish 9,765 samples and nine suites.

**Unresolved ambiguity**
- The preferred cross-suite aggregate is less important than, and should not replace, per-suite reporting.

[Back to page index](#on-this-page)
