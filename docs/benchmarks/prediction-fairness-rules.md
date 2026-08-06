# Prediction, fairness, and structured reasoning

<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->

Outcome prediction, subgroup performance, holding selection, deontic rules, and structured legal analysis.

Snapshot: **2026-08-05** · 10 entries

[Back to README](../../README.md) · [Catalog index](../catalog.md) · [Selection guide](../selection-guide.md) · [Metric field guide](../metric-theory.md) · [Methodology](../methodology.md)

## On this page

- [ECtHR Tasks A/B](#ecthr)
- [FairLex](#fairlex)
- [CaseHOLD](#casehold)
- [DeonticBench](#deonticbench)
- [MSLR-Bench](#mslr)
- [MASLegalBench](#maslegalbench)
- [OpenExempt](#openexempt)
- [PredEx](#predex)
- [LegalLens](#legal-lens)
- [ClassActionPrediction](#class-action-prediction)

<a id="ecthr"></a>
## ECtHR Tasks A/B

`ecthr` · **benchmark** · **recommended** · fixed-release

Predict European Convention articles alleged (Task A) or found violated (Task B) from case facts.

**Also known as:** ECtHR Task

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | ECtHR task authors / LexGLUE (academic) |
| Catalog geography | Council of Europe |
| Last verified update | [2025-07-23](https://github.com/coastalcph/lex-glue)<br>*Canonical LexGLUE repository push* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Research fact-to-doctrine mapping: predict alleged (Task A) or violated (Task B) Convention articles from ECtHR case facts.
- Compare long-document classification architectures on multi-label legal prediction with fixed splits.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
| GitHub | [https://github.com/coastalcph/lex-glue](https://github.com/coastalcph/lex-glue) |
| Hugging Face | [https://huggingface.co/datasets/coastalcph/lex_glue](https://huggingface.co/datasets/coastalcph/lex_glue) |
| Paper / arXiv | [https://arxiv.org/abs/1906.02059](https://arxiv.org/abs/1906.02059)<br>[https://arxiv.org/abs/2110.00976](https://arxiv.org/abs/2110.00976) |
| Leaderboard / competition | None located |
| Project | None located |

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

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | FairLex authors (academic) |
| Catalog geography | Multi-jurisdiction and supranational |
| Last verified update | [2023-07-27](https://huggingface.co/datasets/coastalcph/fairlex)<br>*Hugging Face dataset update* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Measure per-group, worst-group, and gap performance on legal prediction tasks across gender, age, region, language, and legal-area attributes.
- Test whether robustness interventions improve worst-group scores on legal tasks.
- Produce subgroup-performance documentation as one input to a product evaluation.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
| GitHub | [https://github.com/coastalcph/fairlex](https://github.com/coastalcph/fairlex) |
| Hugging Face | [https://huggingface.co/datasets/coastalcph/fairlex](https://huggingface.co/datasets/coastalcph/fairlex) |
| Paper / arXiv | [https://aclanthology.org/2022.acl-long.301/](https://aclanthology.org/2022.acl-long.301/) |
| Leaderboard / competition | None located |
| Project | None located |

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

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | CaseHOLD authors (academic) |
| Catalog geography | United States |
| Last verified update | [2021-07-06](https://arxiv.org/abs/2104.08671)<br>*arXiv revision* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test discrimination of the correct case holding from hard distractors on US judicial opinion excerpts.
- Research the benefit of legal-domain pretraining on case-law reading.
- Quick screen of US case-law comprehension before deeper task-specific evaluation.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
| GitHub | [https://github.com/reglab/casehold](https://github.com/reglab/casehold)<br>[https://github.com/coastalcph/lex-glue](https://github.com/coastalcph/lex-glue) |
| Hugging Face | [https://huggingface.co/datasets/coastalcph/lex_glue](https://huggingface.co/datasets/coastalcph/lex_glue) |
| Paper / arXiv | [https://arxiv.org/abs/2104.08671](https://arxiv.org/abs/2104.08671) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- Public US opinions and fixed distractors are contamination-prone.
- Models may exploit distractor-generation artifacts rather than legal reasoning.

**Verified facts**
- The author-owned CaseHOLD repository, original paper, and LexGLUE establish the canonical task.

**Unresolved ambiguity**
- A separate current author-owned HF dataset was not located outside LexGLUE.

**Related entries**

- [LexGLUE](reasoning-education.md#lexglue)

[Back to page index](#on-this-page)

<a id="deonticbench"></a>
## DeonticBench

`deonticbench` · **benchmark-suite** · **recommended** · active

Reason about obligations, permissions, prohibitions, eligibility, and amounts under long legal/policy rules, directly or through executable Prolog.

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | DeonticBench authors (academic) |
| Catalog geography | United States |
| Last verified update | [2026-06-04](https://huggingface.co/datasets/gydou/DeonticBench)<br>*Hugging Face dataset update* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test rule application over US tax, immigration, housing, and airline-policy rules with exact outcomes and executable Prolog references.
- Diagnose whether failures come from wrong formalization, solver execution, abstention, or wrong final answers.
- Regression-test reasoning changes using the bootstrap confidence-interval protocol on a pinned post-audit revision.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
| GitHub | [https://github.com/guangyaodou/DeonticBench](https://github.com/guangyaodou/DeonticBench) |
| Hugging Face | [https://huggingface.co/datasets/gydou/DeonticBench](https://huggingface.co/datasets/gydou/DeonticBench) |
| Paper / arXiv | [https://arxiv.org/abs/2604.04443](https://arxiv.org/abs/2604.04443) |
| Leaderboard / competition | None located |
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

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | MSLR-Bench authors (academic) |
| Catalog geography | China |
| Last verified update | [2026-06-29](https://github.com/yuwenhan07/MSLR-Bench)<br>*GitHub repository push* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test structured field extraction from Chinese insider-trading decisions against 59,771 labeled fields.
- Test whether generated case analysis covers the expected IRAC components via IRAC recall.
- Research corpus for Chinese financial-enforcement reasoning tasks.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
| GitHub | [https://github.com/yuwenhan07/MSLR-Bench](https://github.com/yuwenhan07/MSLR-Bench) |
| Hugging Face | [https://huggingface.co/datasets/Yuwh07/MSLR-Bench](https://huggingface.co/datasets/Yuwh07/MSLR-Bench) |
| Paper / arXiv | [https://arxiv.org/abs/2511.07979](https://arxiv.org/abs/2511.07979) |
| Leaderboard / competition | None located |
| Project | None located |

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

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | HKUST KnowComp (academic) |
| Catalog geography | United Kingdom |
| Last verified update | [2025-09-30](https://arxiv.org/abs/2509.24922)<br>*arXiv revision* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare single-agent versus multi-agent architectures on GDPR-enforcement questions with retrievable report evidence.
- Test retrieval-at-k of supporting enforcement-report passages inside an agent pipeline.
- Research agent-coordination diagnostics (refusal, agreement statistics) in a legal setting.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
| GitHub | [https://github.com/HKUST-KnowComp/MASLegalBench](https://github.com/HKUST-KnowComp/MASLegalBench) |
| Hugging Face | None located |
| Paper / arXiv | [https://arxiv.org/abs/2509.24922](https://arxiv.org/abs/2509.24922) |
| Leaderboard / competition | None located |
| Project | None located |

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

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | OpenExempt authors (academic) |
| Catalog geography | United States |
| Last verified update | [2026-01-21](https://huggingface.co/datasets/SergioServantez/OpenExempt)<br>*Hugging Face dataset update* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test symbolic statutory reasoning under US Bankruptcy Code exemption rules.
- Stress-test robustness to temporal changes, decomposition, scale, distractors, sycophancy, and obfuscation.
- Use deterministic gold solutions to separate rule-reasoning failures from LLM-judge noise.

### Evaluation contract

| Field | Detail |
| --- | --- |
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
| --- | --- |
| GitHub | [https://github.com/servantez/OpenExempt](https://github.com/servantez/OpenExempt) |
| Hugging Face | [https://huggingface.co/datasets/SergioServantez/OpenExempt](https://huggingface.co/datasets/SergioServantez/OpenExempt) |
| Paper / arXiv | [https://arxiv.org/abs/2601.13183](https://arxiv.org/abs/2601.13183)<br>[https://aclanthology.org/2026.findings-acl.1328/](https://aclanthology.org/2026.findings-acl.1328/) |
| Leaderboard / competition | None located |
| Project | None located |

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

<a id="predex"></a>
## PredEx

`predex` · **benchmark** · **check before use** · fixed-release

Predict whether an Indian Supreme Court appeal or petition is accepted or rejected and extract supporting explanatory text.

**Also known as:** Prediction with Explanation

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | L-NLProc / PredEx authors (academic) |
| Catalog geography | India |
| Last verified update | [2026-06-03](https://github.com/ShubhamKumarNigam/PredEx)<br>*GitHub repository push; latest change was citation metadata rather than benchmark data* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Evaluate Indian Supreme Court appeal/petition outcome prediction together with extractive explanations.
- Compare label performance and explanation overlap separately under the public 12,178/3,044 split.
- Audit whether explanations remain useful to legal experts after controlling for outcome, citation, and source shortcuts.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | Classification metrics score the binary outcome; overlap, semantic, and small-sample expert ratings separately score whether the extracted rationale resembles the annotated explanation. |
| Jurisdiction | India |
| Languages | English |
| Size | 15,222 human-annotated Supreme Court of India case documents |
| Splits | 12,178 train and 3,044 test; repository also defines 10,961 fine-tuning and 1,217 validation examples within train |
| Source material | Indian Kanoon Supreme Court case proceedings annotated by ten legal annotators |
| Input | Case proceeding text |
| Output | Accepted/rejected outcome plus extractive explanation |
| Baselines / leaderboard context | The paper compares classification and explanation models, including transformer and long-document architectures, under the fixed split. |
| Dataset access | Public GitHub and Hugging Face train/test files |
| License | GitHub software: MIT; Hugging Face dataset card: Apache-2.0 |
| Gating | None observed |
| Maintenance | Stable Findings of ACL 2024 release; the 2026 repository update appears citation-only and is not evidence of new data. |
| Reproducibility | Good for fixed labels and automatic metrics; weaker for the 50-example expert review and any hosted model baselines. |

### Metrics

- **Macro precision / recall / F1 and accuracy:** Score the binary outcome with macro-averaged class metrics and accuracy on the fixed test set. **Primary.**
- **ROUGE / BLEU / METEOR / BERTScore / BLANC:** Compare extracted explanations with references using lexical, semantic, and informativeness measures; report metric families separately. **Primary.**
- **Expert explanation rating:** Legal experts rate 50 randomly sampled explanations on 1–5 scales; do not generalize this small sample to every output. Judge: Legal experts.

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | [https://github.com/ShubhamKumarNigam/PredEx](https://github.com/ShubhamKumarNigam/PredEx) |
| Hugging Face | [https://huggingface.co/datasets/L-NLProc/PredEx](https://huggingface.co/datasets/L-NLProc/PredEx) |
| Paper / arXiv | [https://arxiv.org/abs/2406.04136](https://arxiv.org/abs/2406.04136)<br>[https://aclanthology.org/2024.findings-acl.255/](https://aclanthology.org/2024.findings-acl.255/) |
| Leaderboard / competition | None located |
| Project | [https://huggingface.co/collections/L-NLProc/predex-datasets-6650a75907cc2255eab18d01](https://huggingface.co/collections/L-NLProc/predex-datasets-6650a75907cc2255eab18d01) |

### Validity and evidence

**Risks / caveats**
- Outcome labels and public judgments are contamination-prone and may support citation, chronology, or drafting-style shortcuts.
- Potential overlap or lineage with ILDC/CJPE inside IL-TUR has not been ruled out at the case-ID level.
- Reference-overlap explanation metrics do not establish legal sufficiency or causal faithfulness.

**Verified facts**
- The official paper, repository, and Hugging Face release agree on 15,222 annotated cases, the 12,178/3,044 split, ten legal annotators, binary outcome task, and explanation metric families.
- The repository license is MIT and the Hub dataset card says Apache-2.0; a prior claim of CC BY was incorrect.

**Inference**
- PredEx is a stronger standalone explanation benchmark than the tiny ILDC-Expert subset, but it is not independent evidence until case-level overlap is audited.

**Unresolved ambiguity**
- Case-level overlap with ILDC/CJPE and the source-judgment licensing boundary remain unresolved.

[Back to page index](#on-this-page)

<a id="legal-lens"></a>
## LegalLens

`legal-lens` · **benchmark-suite** · **check before use** · completed

Extract potential legal-violation entities from non-legal text and infer whether a violation statement entails a harmed group or legal ground.

**Also known as:** NLLP 2024 Shared Task on Legal Violation Identification

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | Darrow / LegalLens authors (company; commercial interest) |
| Catalog geography | United States |
| Last verified update | [2024-10-15](https://arxiv.org/abs/2410.12064)<br>*NLLP shared-task paper arXiv v1 submission* |
| Access level | partial |
| Test labels | mixed |
| Independently runnable | partial |

### Possible use cases

- Detect spans describing potential legal violations, affected people, responsible parties, and legal grounds in class-action source text.
- Test three-way entailment between alleged violations, harmed groups, and legal bases.
- Compare with the NLLP 2024 shared-task results only after pinning whether the formerly hidden test labels are available.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | Exact-span F1 scores legal-violation extraction, while macro-F1 scores three-way entailment; the original datasets and later shared task have related but not identical public split boundaries. |
| Jurisdiction | United States / common-law class-action context |
| Languages | English |
| Size | Original public releases: 1,327 NER rows and 312 NLI rows; shared-task Hub releases expose 976 NER rows and 312 NLI rows |
| Splits | Original NER has 710 train and 617 test; original NLI is one 312-row train split; shared-task Hub files expose train data, while post-competition publication of the formerly hidden test was not verified |
| Source material | Web/news text transformed with GPT-4/4o and validated by legal experts for class-action-relevant violations |
| Input | Text passage for entity extraction or premise/hypothesis pair for NLI |
| Output | Violation-related entity spans or entailment/contradiction/neutral label |
| Baselines / leaderboard context | The original paper reports transformer baselines; the 38-team NLLP 2024 shared task reports top scores of 0.416 weighted NER F1 and 0.853 NLI macro-F1. |
| Dataset access | Original and shared-task training datasets are public on Hugging Face; full shared-task hidden-test availability was not verified |
| License | GitHub software: GPL-3.0; Hugging Face dataset metadata: Apache-2.0 |
| Gating | No gate on public files; the competition test boundary was hidden during the task |
| Maintenance | Completed NLLP 2024 shared task layered on the original LegalLens release; preserve the identity and split version in every result. |
| Reproducibility | Partial because public datasets and metric definitions exist, but the post-task hidden-test release and one canonical end-to-end scorer package were not verified. |

### Metrics

- **NER precision / recall / F1:** Original work uses seqeval-style span metrics; the shared task uses weighted exact-span F1. Name the variant with every score. **Primary.**
- **NLI macro-F1:** Compute macro-F1 across entailment, contradiction, and neutral labels. **Primary.**

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | [https://github.com/darrow-labs/LegalLens](https://github.com/darrow-labs/LegalLens) |
| Hugging Face | [https://huggingface.co/datasets/darrow-ai/LegalLensNER](https://huggingface.co/datasets/darrow-ai/LegalLensNER)<br>[https://huggingface.co/datasets/darrow-ai/LegalLensNLI](https://huggingface.co/datasets/darrow-ai/LegalLensNLI)<br>[https://huggingface.co/datasets/darrow-ai/LegalLensNER-SharedTask](https://huggingface.co/datasets/darrow-ai/LegalLensNER-SharedTask)<br>[https://huggingface.co/datasets/darrow-ai/LegalLensNLI-SharedTask](https://huggingface.co/datasets/darrow-ai/LegalLensNLI-SharedTask) |
| Paper / arXiv | [https://arxiv.org/abs/2402.04335](https://arxiv.org/abs/2402.04335)<br>[https://arxiv.org/abs/2410.12064](https://arxiv.org/abs/2410.12064) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- GPT-generated then expert-validated examples may encode generator artifacts and synthetic phrasing.
- Darrow has a commercial interest in legal-violation and class-action detection.
- Small NLI and public-label splits permit overfitting; the shared-task and original counts should not be merged.

**Verified facts**
- The official papers, Darrow repository, and four Hugging Face releases establish the NER/NLI tasks, public row counts, metric variants, licenses, and 38-team shared task.
- The live Hub viewers expose 1,327 original NER rows, 312 original NLI rows, 976 shared-task NER rows, and 312 shared-task NLI rows.

**Inference**
- The shared task provides useful external participation evidence, but not an independently hidden benchmark after all labels become public.

**Unresolved ambiguity**
- A public post-competition copy of the hidden test labels and one canonical scorer for both task generations were not located.

**Related entries**

- [ClassActionPrediction](prediction-fairness-rules.md#class-action-prediction)

[Back to page index](#on-this-page)

<a id="class-action-prediction"></a>
## ClassActionPrediction

`class-action-prediction` · **benchmark** · **check before use** · fixed-release

Predict whether a United States federal class-action complaint will produce a plaintiff win or loss.

**Also known as:** USClassActions

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | Darrow / ClassActionPrediction authors (company; commercial interest) |
| Catalog geography | United States |
| Last verified update | [2024-01-24](https://huggingface.co/datasets/darrow-ai/USClassActions)<br>*Hugging Face dataset update* |
| Access level | open |
| Test labels | public |
| Independently runnable | partial |

### Possible use cases

- Study binary outcome prediction on US federal class-action complaints using the public 3,000-row sample.
- Audit calibration and domain shortcuts before considering complaint-text outcome models.
- Use the documented shortcut failures as a negative-control case when designing a fresh time- and matter-held-out prediction benchmark.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | Accuracy measures binary outcome classification on balanced data, while expected calibration error tests probability reliability; the paper's shortcut analysis questions whether the model learns legally valid signals. |
| Jurisdiction | United States federal class actions |
| Languages | English |
| Size | Public Hugging Face sample has 3,000 rows; the paper describes a larger curated corpus of about 10,800 cases that is not fully public |
| Splits | Hugging Face exposes one 3,000-row train split; the paper uses random 70/15/15 splits plus five-fold cross-validation and five seeds, but those split assignments are not shipped |
| Source material | US federal class-action complaint text curated by Darrow |
| Input | Complaint text, including allegations or document sections under the paper's variants |
| Output | Binary win/loss label and optional probability |
| Baselines / leaderboard context | The paper compares BERT, legal-domain BERT/LegalRoBERTa/CaseLawBERT, Longformer, and BigBird variants; the best allegations-based result is about 66.8% accuracy. |
| Dataset access | Public 3,000-row Hugging Face sample and public code repository; the full paper corpus is not public |
| License | Repository: GPL-3.0; Hugging Face metadata also says GPL-3.0, though applicability to source complaint text is not independently resolved |
| Gating | None for the public sample |
| Maintenance | Fixed 2022 research release with a 2024 Hugging Face metadata/data update; no maintained leaderboard was located. |
| Reproducibility | Partial because the public sample, code, and metrics exist, but the full corpus and paper split assignments are not released. |

### Metrics

- **Accuracy:** Compute binary accuracy on the paper's balanced evaluation protocol; report the exact locally constructed split and seed. **Primary.**
- **Expected calibration error:** Compare predicted confidence with empirical correctness before and after temperature scaling using the paper's binning protocol.

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | [https://github.com/darrow-labs/ClassActionPrediction](https://github.com/darrow-labs/ClassActionPrediction) |
| Hugging Face | [https://huggingface.co/datasets/darrow-ai/USClassActions](https://huggingface.co/datasets/darrow-ai/USClassActions) |
| Paper / arXiv | [https://arxiv.org/abs/2211.00582](https://arxiv.org/abs/2211.00582) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- The paper documents domain and label shortcuts that undermine substantive legal-validity claims.
- Random splitting may place related firms, allegations, or matters across partitions unless independently checked.
- Darrow has a commercial interest, and public complaint labels are contamination-prone.

**Verified facts**
- The official paper, GPL-3.0 repository, and Hugging Face release establish the prediction task, public 3,000-row sample, paper-scale 10.8K corpus, accuracy/calibration metrics, and model baselines.

**Inference**
- This benchmark is valuable mainly as a cautionary outcome-prediction study unless rerun on matter- and time-held-out data.

**Unresolved ambiguity**
- The full corpus, exact public split assignments, matter-family leakage, and legal effect of GPL metadata on source documents remain unresolved.

**Related entries**

- [LegalLens](prediction-fairness-rules.md#legal-lens)

[Back to page index](#on-this-page)
