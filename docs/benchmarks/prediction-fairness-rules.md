# Prediction, fairness, and structured reasoning

<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->

Outcome prediction, subgroup performance, holding selection, deontic rules, and structured legal analysis.

Snapshot: **2026-08-03** · 7 entries

[Catalog index](../catalog.md) · [Selection guide](../selection-guide.md) · [Metric field guide](../metric-theory.md) · [Methodology](../methodology.md)

## On this page

- [ECtHR Tasks A/B](#ecthr)
- [FairLex](#fairlex)
- [CaseHOLD](#casehold)
- [DeonticBench](#deonticbench)
- [ALARB](#alarb)
- [MSLR-Bench](#mslr)
- [MASLegalBench](#maslegalbench)

<a id="ecthr"></a>
## ECtHR Tasks A/B

`ecthr` · **benchmark** · **recommended** · fixed-release

Predict European Convention articles alleged (Task A) or found violated (Task B) from case facts.

### Evaluation contract

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

- **Micro-F1 and macro-F1:** F1 is computed over article labels with micro and label-macro aggregation. **Primary.**

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

Original source bullet(s): #6

[Back to page index](#on-this-page)

<a id="fairlex"></a>
## FairLex

`fairlex` · **benchmark-suite** · **recommended** · fixed-release

Evaluate legal prediction performance and group robustness across sensitive or legally salient subpopulations.

### Evaluation contract

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

- **All-group macro-F1:** Macro-F1 over the full evaluation population. **Primary.**
- **Worst-group macro-F1 / group disparity:** Minimum subgroup performance and gaps across specified protected/context groups. **Primary.**

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

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)

<a id="casehold"></a>
## CaseHOLD

`casehold` · **benchmark** · **specialist** · fixed-release

Select the correct holding that completes an excerpt from a US judicial opinion.

### Evaluation contract

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

- **Accuracy:** Exact five-way choice accuracy. **Primary.**

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

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)

<a id="deonticbench"></a>
## DeonticBench

`deonticbench` · **benchmark-suite** · **recommended** · active

Reason about obligations, permissions, prohibitions, eligibility, and amounts under long legal/policy rules, directly or through executable Prolog.

### Evaluation contract

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

- **Bootstrapped accuracy with 95% CI:** 1,000 case-resampling replicates; one generation sampled per case. Numeric domains allow ±1 rounding tolerance; categorical domains require exact match. **Primary.**
- **Abstention and wrong rate:** Empty/error/timeout Prolog or unparsable direct answer counts as abstention; remaining incorrect parses count wrong.

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

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)

<a id="alarb"></a>
## ALARB

`alarb` · **dataset** · **check before use** · fixed-release

Reason over Saudi commercial-law cases, complete arguments, and identify governing statutory articles.

### Evaluation contract

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

- **Correct / partial / incorrect judge score:** GPT-4o categorizes generated legal outputs against references. Judge: GPT-4o. **Primary.**
- **MCQ accuracy:** Exact statutory-article choice. **Primary.**

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

Original source bullet(s): #14

[Back to page index](#on-this-page)

<a id="mslr"></a>
## MSLR-Bench

`mslr` · **benchmark** · **check before use** · active

Extract structured facts and produce IRAC-style reasoning for Chinese insider-trading cases.

### Evaluation contract

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

- **Field accuracy / FCR:** Exact or normalized field correctness plus the paper's field-completion/consistency measure. **Primary.**
- **IRAC Recall and judge score:** Recall of expected IRAC elements plus LLM evaluation of generated reasoning. Judge: DeepSeek-V3. **Primary.**

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

Original source bullet(s): #16

[Back to page index](#on-this-page)

<a id="maslegalbench"></a>
## MASLegalBench

`maslegalbench` · **benchmark** · **check before use** · fixed-release

Multi-agent deductive reasoning about GDPR enforcement facts, rules, application, common sense, and conclusions.

### Evaluation contract

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

- **Accuracy / refusal rate:** Exact final answer correctness and share of non-answers. **Primary.**
- **Retrieval@1/3/5 and Cohen's kappa:** Evidence-hit rates plus agent/human agreement statistics.

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

Original source bullet(s): #17

[Back to page index](#on-this-page)
