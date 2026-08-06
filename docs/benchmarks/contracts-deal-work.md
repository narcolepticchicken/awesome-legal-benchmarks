# Contracts and deal work

<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->

Clause extraction, provision classification, entailment, retrieval, merger agreements, and redlining.

Snapshot: **2026-08-05** · 11 entries

[Back to README](../../README.md) · [Catalog index](../catalog.md) · [Selection guide](../selection-guide.md) · [Metric field guide](../metric-theory.md) · [Methodology](../methodology.md)

## On this page

- [Contract Understanding Atticus Dataset](#cuad)
- [LEDGAR](#ledgar)
- [ContractNLI](#contractnli)
- [Merger Agreement Understanding Dataset](#maud)
- [Atticus Clause Retrieval Dataset](#acord)
- [ContractEval](#contracteval)
- [RedlineBench](#redlinebench)
- [LegalOn Contract Review Benchmark 2026](#legalon-contract-review-2026)
- [Ivo Contract Review Comparison](#ivo-contract-review-study)
- [legalbenchmarks.ai](#legalbenchmarks-ai)
- [AGB-DE](#agb-de)

<a id="cuad"></a>
## Contract Understanding Atticus Dataset

`cuad` · **benchmark** · **recommended** · fixed-release

Locate 41 categories of commercially important clauses in long contracts.

**Also known as:** CUAD

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | The Atticus Project (nonprofit) |
| Catalog geography | United States |
| Last verified update | [2024-05-23](https://huggingface.co/datasets/theatticusproject/cuad-qa)<br>*Hugging Face dataset update* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare extraction systems on locating 41 categories of commercially important clauses in long contracts.
- Test abstention when a clause is absent (no-answer handling) in contract-review pipelines.
- Research baseline for extractive contract QA with an established comparison literature.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | Extractive QA turns issue spotting into span retrieval: a model should find every relevant token while avoiding unrelated language and correctly abstain when a clause is absent. |
| Jurisdiction | United States / SEC filings |
| Languages | English |
| Size | 510 contracts; 13,000+ expert labels; common QA release has 22,450 train and 4,182 test rows |
| Splits | Train/test SQuAD-style QA release |
| Source material | Material contracts filed in SEC EDGAR |
| Input | Contract text plus a clause-category question |
| Output | One or more answer spans, or no answer |
| Baselines / leaderboard context | Paper reports BERT-family extractive QA baselines; many later long-context systems reuse the public test set. |
| Dataset access | Public |
| License | CC BY 4.0 for annotations/release; source contracts retain underlying rights |
| Gating | None |
| Maintenance | Stable established release. |
| Reproducibility | Data and evaluation code are public; normalize tokenization and no-answer handling exactly. |

### Metrics

- **Token intersection-over-union (Jaccard):** |predicted-token set ∩ gold-token set| / |union|, with precision/recall and AUPR across confidence thresholds. **Primary.**
- **AUPR:** Area under the precision–recall curve over clause predictions, useful under strong class imbalance.

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | [https://github.com/The-Atticus-Project/cuad](https://github.com/The-Atticus-Project/cuad) |
| Hugging Face | [https://huggingface.co/datasets/theatticusproject/cuad-qa](https://huggingface.co/datasets/theatticusproject/cuad-qa) |
| Paper / arXiv | [https://arxiv.org/abs/2103.06268](https://arxiv.org/abs/2103.06268) |
| Leaderboard / competition | None located |
| Project | [https://www.atticusprojectai.org/cuad](https://www.atticusprojectai.org/cuad) |

### Validity and evidence

**Risks / caveats**
- Public contracts and gold spans are heavily reused and contamination-prone.
- Boilerplate similarity can reward memorization more than issue spotting on novel drafting styles.

**Verified facts**
- Official project, GitHub, paper, and author HF release agree on the benchmark identity.

**Unresolved ambiguity**
- Published descriptions count annotations, QA rows, and labels differently; state which unit is reported.

**Related entries**

- [ContractEval](contracts-deal-work.md#contracteval)

Original source bullet(s): #4

[Back to page index](#on-this-page)

<a id="ledgar"></a>
## LEDGAR

`ledgar` · **dataset** · **specialist** · fixed-release

Classify contract provisions into clause/topic labels.

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | LEDGAR authors (academic) |
| Catalog geography | United States |
| Last verified update | [2020-10-19](https://github.com/dtuggener/LEDGAR_provision_classification)<br>*Original GitHub repository push* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare provision classifiers on SEC contract clause topics in the original or LexGLUE 100-label variant.
- Test rare-label performance via macro-F1 when selecting a clause-tagging model.
- Source corpus for provision-classification training and document-family-grouped holdout design.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | Provision classification measures whether representations separate contract-language topics; macro-F1 exposes rare-label performance while micro-F1 emphasizes the frequent-label mass. |
| Jurisdiction | United States / SEC filings |
| Languages | English |
| Size | Original corpus: about 846,274 provisions, 12,608 labels, 60,540 contracts; LexGLUE subset: 60k/10k/10k over 100 labels |
| Splits | Original and LexGLUE splits differ |
| Source material | SEC EDGAR contracts |
| Input | A contract provision |
| Output | Provision label(s) |
| Baselines / leaderboard context | Original paper and LexGLUE report neural and transformer classifiers. |
| Dataset access | Public code/data paths; LexGLUE package is directly loadable |
| License | LexGLUE package CC BY 4.0; underlying filing rights and original release terms should be reviewed |
| Gating | None |
| Maintenance | Original dataset is stable; LexGLUE is the maintained standardized task. |
| Reproducibility | Strong if the exact original versus LexGLUE variant, label vocabulary, and split are named. |

### Metrics

- **Micro-F1 and macro-F1:** Micro pools all label decisions; macro averages per-label F1 so rare labels have equal weight. **Primary.**

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | [https://github.com/dtuggener/LEDGAR_provision_classification](https://github.com/dtuggener/LEDGAR_provision_classification)<br>[https://github.com/coastalcph/lex-glue](https://github.com/coastalcph/lex-glue) |
| Hugging Face | [https://huggingface.co/datasets/coastalcph/lex_glue](https://huggingface.co/datasets/coastalcph/lex_glue) |
| Paper / arXiv | [https://aclanthology.org/2020.lrec-1.155/](https://aclanthology.org/2020.lrec-1.155/) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- SEC boilerplate enables document-family leakage and near-duplicate memorization.
- Reporting LEDGAR without naming the original or 100-label LexGLUE variant is ambiguous.

**Verified facts**
- The README's Metatext link is secondary; the original repository and LexGLUE are canonical sources.

**Unresolved ambiguity**
- Source-rights treatment is not identical to the annotation license.

**Related entries**

- [LexGLUE](reasoning-education.md#lexglue)

Original source bullet(s): #5

[Back to page index](#on-this-page)

<a id="contractnli"></a>
## ContractNLI

`contractnli` · **benchmark** · **recommended** · fixed-release

Determine whether a non-disclosure agreement entails, contradicts, or does not mention a fixed legal hypothesis and identify supporting evidence.

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | Stanford NLP (academic) |
| Catalog geography | United States |
| Last verified update | [2022-02-11](https://github.com/stanfordnlp/contract-nli)<br>*GitHub repository push* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test document-level entailment of 17 fixed legal hypotheses against full NDAs.
- Test whether entailment decisions are grounded in the correct evidence spans, not just correct labels.
- Regression-test NDA screening components against the fixed official splits.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | Three-way document NLI tests semantic/legal relation to 17 hypotheses; evidence identification tests whether the decision is grounded in the right spans. |
| Jurisdiction | Commercial NDAs / primarily United States practice |
| Languages | English |
| Size | 607 NDAs and 17 fixed hypotheses |
| Splits | 423 train / 61 development / 123 test contracts |
| Source material | Publicly available NDAs annotated for hypotheses and evidence |
| Input | Full NDA plus one hypothesis |
| Output | Entailment, contradiction, or not-mentioned label plus evidence spans |
| Baselines / leaderboard context | Official project reports document-NLI and evidence-selection baselines. |
| Dataset access | Public official project/GitHub |
| License | CC BY 4.0 |
| Gating | None |
| Maintenance | Stable research release. |
| Reproducibility | High with official splits and evidence scorer; third-party HF copies are not canonical. |

### Metrics

- **Micro/macro F1 for NLI:** F1 over the three labels with stated aggregation. **Primary.**
- **Evidence identification F1:** Overlap/classification F1 over evidence spans or sentence selections. **Primary.**

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | [https://github.com/stanfordnlp/contract-nli](https://github.com/stanfordnlp/contract-nli) |
| Hugging Face | None located |
| Paper / arXiv | [https://arxiv.org/abs/2110.01799](https://arxiv.org/abs/2110.01799) |
| Leaderboard / competition | None located |
| Project | [https://stanfordnlp.github.io/contract-nli/](https://stanfordnlp.github.io/contract-nli/) |

### Validity and evidence

**Risks / caveats**
- Only 17 fixed hypotheses invite template-specific learning.
- NDA boilerplate and public test labels create near-duplicate and contamination risk.

**Verified facts**
- Official Stanford project/repository/paper define 607 NDAs and 17 hypotheses.

**Unresolved ambiguity**
- No author-owned canonical HF dataset was found; available HF copies are third-party.

[Back to page index](#on-this-page)

<a id="maud"></a>
## Merger Agreement Understanding Dataset

`maud` · **benchmark** · **recommended** · fixed-release

Answer fine-grained questions about merger-agreement provisions.

**Also known as:** MAUD

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | The Atticus Project (nonprofit) |
| Catalog geography | United States |
| Last verified update | [2023-11-24](https://arxiv.org/abs/2301.00876)<br>*arXiv revision* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test fine-grained deal-point QA on public merger agreements across 92 expert-annotated question types.
- Compare models for M&A diligence review on provision-level answers including no-answer classes.
- Template for designing agreement-family-grouped splits in internal M&A evaluations.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | Question-conditioned provision classification tests whether models can identify deal terms and exceptions across complex acquisition agreements. |
| Jurisdiction | United States / public-company M&A |
| Languages | English |
| Size | 152 merger agreements, more than 39,000 examples, more than 47,000 expert annotations, 92 question types |
| Splits | Official release includes full and abridged task files |
| Source material | Public merger agreements with expert legal annotations |
| Input | Agreement text/provision plus a legal question |
| Output | Categorical answer or no-answer class |
| Baselines / leaderboard context | Paper evaluates transformer encoders and prompted LLMs. |
| Dataset access | Public |
| License | Official release license applies; underlying agreements remain source documents |
| Gating | None observed |
| Maintenance | Stable Atticus Project release. |
| Reproducibility | Good with named full/abridged variant, split, and question aggregation. |

### Metrics

- **Micro-F1 and macro-F1:** Micro summarizes all decisions; macro weights each question/label class equally. **Primary.**

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | [https://github.com/TheAtticusProject/maud](https://github.com/TheAtticusProject/maud) |
| Hugging Face | [https://huggingface.co/datasets/theatticusproject/maud](https://huggingface.co/datasets/theatticusproject/maud) |
| Paper / arXiv | [https://arxiv.org/abs/2301.00876](https://arxiv.org/abs/2301.00876)<br>[https://aclanthology.org/2023.emnlp-main.1019/](https://aclanthology.org/2023.emnlp-main.1019/) |
| Leaderboard / competition | None located |
| Project | [https://www.atticusprojectai.org/maud](https://www.atticusprojectai.org/maud) |

### Validity and evidence

**Risks / caveats**
- Only 152 agreements can produce agreement-family leakage across poorly grouped splits.
- Public deal documents and annotations are contamination-prone.

**Verified facts**
- Official GitHub/HF/project/paper identify 152 agreements and 92 questions.

**Unresolved ambiguity**
- Counts differ depending on examples versus annotations; report the unit.

[Back to page index](#on-this-page)

<a id="acord"></a>
## Atticus Clause Retrieval Dataset

`acord` · **benchmark** · **recommended** · fixed-release

Rank precedent contract clauses for an attorney-written drafting need.

**Also known as:** ACORD

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | The Atticus Project (nonprofit) |
| Catalog geography | United States |
| Last verified update | [2025-09-21](https://arxiv.org/abs/2501.06582)<br>*arXiv revision* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Rank precedent-clause retrieval against attorney-graded 1-to-5-star relevance for drafting requests.
- Compare retrieval and reranking stacks on nDCG@5/10 and star-threshold precision for clause libraries.
- Product evaluation of a drafting assistant's clause-suggestion quality.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | Graded expert relevance (1–5 stars, encoded 0–4) supports nDCG, while star-threshold precision@5 asks whether the top drafting candidates meet stricter usefulness levels. |
| Jurisdiction | United States / commercial contracts |
| Languages | English |
| Size | 114 queries and 126,662+ explicitly rated query-clause pairs across nine clause categories |
| Splits | 45% train / 5% validation / 50% test by query |
| Source material | SEC EDGAR and selected Fortune 500 terms, with attorney-written queries and ratings |
| Input | Attorney drafting query plus clause corpus |
| Output | Ranked clauses |
| Baselines / leaderboard context | Paper/repository compare sparse, embedding, and reranking systems. |
| Dataset access | Public GitHub zip and HF mirror |
| License | CC BY 4.0 data; repository code/license metadata also includes MIT |
| Gating | None |
| Maintenance | Stable expert-annotated release. |
| Reproducibility | High with official BEIR files and qrels; HF viewer currently mis-parses the zip, so use raw files. |

### Metrics

- **nDCG@5 and nDCG@10:** Discounted cumulative gain over 0–4 relevance, normalized by the ideal ranking. **Primary.**
- **3/4/5-star precision@5:** Precision among top five at progressively stricter attorney-rating thresholds. **Primary.**

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | [https://github.com/TheAtticusProject/acord](https://github.com/TheAtticusProject/acord) |
| Hugging Face | [https://huggingface.co/datasets/theatticusproject/acord](https://huggingface.co/datasets/theatticusproject/acord) |
| Paper / arXiv | [https://arxiv.org/abs/2501.06582](https://arxiv.org/abs/2501.06582)<br>[https://aclanthology.org/2025.acl-long.1206/](https://aclanthology.org/2025.acl-long.1206/) |
| Leaderboard / competition | None located |
| Project | [https://www.atticusprojectai.org/acord/](https://www.atticusprojectai.org/acord/) |

### Validity and evidence

**Risks / caveats**
- Only 114 queries make per-category estimates sensitive to individual queries.
- Explicitly rating irrelevant clauses reduces false negatives but cannot exhaust every potentially useful precedent.

**Verified facts**
- Official project/GitHub/HF agree on query count, pair count, splits, ratings, and metrics.

**Unresolved ambiguity**
- HF dataset viewer failure is an access UX issue, not missing data.

[Back to page index](#on-this-page)

<a id="contracteval"></a>
## ContractEval

`contracteval` · **evaluation-protocol** · **related artifact** · fixed-release

Evaluate long-context LLM clause-risk extraction on the public CUAD test set.

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | ContractEval authors (academic) |
| Catalog geography | United States |
| Last verified update | — |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Reuse the protocol to test long-context clause extraction and abstention (false no-relevant-clause rate) on CUAD without writing a new scorer.
- Protocol template for recall-weighted extraction scoring (F2) in a contract-review product evaluation.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | F1/F2 and Jaccard trade off overlap precision and recall, while false-no-related-clause rate isolates abstention failures; the protocol reuses CUAD rather than defining new ground truth. |
| Jurisdiction | United States / SEC filings |
| Languages | English |
| Size | CUAD test set, about 4,182 QA rows over 41 categories |
| Splits | Reused public CUAD test |
| Source material | CUAD |
| Input | Contract plus clause question |
| Output | Span(s) or no-related-clause response |
| Baselines / leaderboard context | Paper evaluates 19 contemporary LLMs under one protocol. |
| Dataset access | Uses public CUAD |
| License | No separate dataset; CUAD terms apply |
| Gating | Model APIs may be required |
| Maintenance | Paper protocol, not a separately maintained benchmark release. |
| Reproducibility | Moderate if prompts/model versions are available; public API aliases can drift. |

### Metrics

- **F1 / F2 / Jaccard:** Overlap scores; F2 weights recall twice as strongly as precision. **Primary.**
- **False no-related-clause rate:** Share of positive items incorrectly rejected as containing no relevant clause.

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | None located |
| Hugging Face | [https://huggingface.co/datasets/theatticusproject/cuad-qa](https://huggingface.co/datasets/theatticusproject/cuad-qa) |
| Paper / arXiv | [https://arxiv.org/abs/2508.03080](https://arxiv.org/abs/2508.03080) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- It is not a new dataset and should not be counted as independent evidence from CUAD.
- Paper figures use both 4,128 and 4,182, an unresolved count inconsistency.

**Verified facts**
- The protocol evaluates CUAD rather than releasing new labeled examples.

**Unresolved ambiguity**
- 4,128 versus 4,182 evaluation rows.

**Related entries**

- [Contract Understanding Atticus Dataset](contracts-deal-work.md#cuad)

Original source bullet(s): #15

[Back to page index](#on-this-page)

<a id="redlinebench"></a>
## RedlineBench

`redlinebench` · **benchmark** · **check before use** · active

Negotiate commercial contracts over four turns by producing native Word tracked changes and comments.

**Also known as:** Crosby RedlineBench

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | Crosby (company; commercial interest) |
| Catalog geography | United States |
| Last verified update | [2026-06-26](https://github.com/crosbylegal/redline-bench)<br>*GitHub repository push* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test whether an agent produces playbook-grounded native-Word tracked changes and threaded comments across four negotiation turns on Crosby's harness.
- Compare agents on the five deal-work dimensions: commercial context, legal correctness, negotiation quality, closing orientation, and counterparty acceptance.
- Protocol inspiration for rubric-scored redlining evaluations on private playbooks.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | Weighted expert rubrics model five dimensions of good deal work; turn-weighted scoring balances all scenario×turn cells and penalizes edits that are legally wrong, commercially misaligned, or unlikely to close. |
| Jurisdiction | United States / commercial contracting |
| Languages | English |
| Size | 140 runnable Harbor tasks across three synthetic MSA scenarios and four turns |
| Splits | Public tasks/test index; repeated expert-rubric variants share some identical inputs |
| Source material | Synthetic SaaS/professional-services negotiations with attorney-authored playbooks and rubrics |
| Input | Commercial context, side playbook, and evolving DOCX contract |
| Output | DOCX with native tracked changes/threaded comments plus finalization metadata |
| Baselines / leaderboard context | Crosby report and HF benchmark metadata publish model results; reproduction CLI supports custom agents. |
| Dataset access | Public 115 MB HF benchmark |
| License | CC BY 4.0 data; MIT code |
| Gating | Agent/model APIs and Word-processing tool environment required |
| Maintenance | Active 2026 vendor release registered as an HF Benchmark. |
| Reproducibility | Strong public task bundles and driver; judge/model versions and document-tool behavior must be pinned. |

### Metrics

- **Redline overall (0–100):** Per task clamp((earned − penalty)/total positive rubric weight); average within identical-input groups, then equally average 12 scenario×turn cells. Judge: LLM judge panel against attorney-authored weighted rubrics. **Primary.**
- **Five dimension scores:** Commercial context, legal correctness, negotiation quality, deal-closing orientation, and counterparty-acceptance prediction. Judge: LLM judge panel.

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | [https://github.com/crosbylegal/redline-bench](https://github.com/crosbylegal/redline-bench) |
| Hugging Face | [https://huggingface.co/datasets/crosbylegal/RedlineBench](https://huggingface.co/datasets/crosbylegal/RedlineBench) |
| Paper / arXiv | None located |
| Leaderboard / competition | [https://huggingface.co/datasets/crosbylegal/RedlineBench](https://huggingface.co/datasets/crosbylegal/RedlineBench) |
| Project | [https://intelligence.crosby.ai/benchmark](https://intelligence.crosby.ai/benchmark) |

### Validity and evidence

**Risks / caveats**
- Only three negotiation scenarios limit external validity.
- Vendor-created benchmark and LLM panel may favor the authors' negotiation style and tool stack.

**Verified facts**
- Official GitHub/HF/report define all 140 tasks, five dimensions, exact aggregation, and licenses.

**Unresolved ambiguity**
- HF source attribution is community/source rather than inspect-ai verified, per the dataset card.

[Back to page index](#on-this-page)

<a id="legalon-contract-review-2026"></a>
## LegalOn Contract Review Benchmark 2026

`legalon-contract-review-2026` · **private-benchmark** · **check before use** · private

Review contracts against precision-critical guidelines and identify or explain material issues.

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | LegalOn Technologies (company; commercial interest) |
| Catalog geography | Evaluation population not published |
| Last verified update | [2026-06-03](https://www.legalontech.com/post/the-contract-review-benchmark-2026)<br>*Official displayed Last updated date* |
| Access level | private |
| Test labels | hidden |
| Independently runnable | no |

### Possible use cases

- Read LegalOn's 2026 results as vendor-run evidence about precision-critical contract review.
- Reuse the order-reversed pairwise judging protocol to reduce presentation-order bias in an internal review study.
- Use the 21-guideline taxonomy as a lead when designing a private contract-specific holdout.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | Blind pairwise preference across concrete review guidelines estimates comparative usefulness while reversed ordering attempts to control positional bias. |
| Jurisdiction | Not fully disclosed |
| Languages | English |
| Size | 3,282 head-to-head reviews across 21 guidelines and 11 models |
| Splits | Private comparison set |
| Source material | Proprietary contract-review scenarios and guidelines |
| Input | Contract plus review guideline |
| Output | Issue identification and review analysis |
| Baselines / leaderboard context | Official post compares 11 named models; underlying reviews and score sheet are not public. |
| Dataset access | Private |
| License | Not publicly stated |
| Gating | No public tasks, data, scorer, GitHub, Hugging Face, paper, or independent leaderboard |
| Maintenance | One dated 2026 vendor study; no public version history. |
| Reproducibility | Low because the contracts, guidelines, outputs, judge model, and detailed scores are private. |

### Metrics

- **Pairwise win/tie and Elo rating:** A blind LLM judge evaluates each pair twice with answer order reversed; a model wins only if preferred in both orders, otherwise the pair is a tie. Report Elo with 95% confidence intervals. Judge: Independent LLM judge; exact model not publicly identified. **Primary.**

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | None located |
| Hugging Face | None located |
| Paper / arXiv | None located |
| Leaderboard / competition | None located |
| Project | [https://www.legalontech.com/post/the-contract-review-benchmark-2026](https://www.legalontech.com/post/the-contract-review-benchmark-2026) |

### Validity and evidence

**Risks / caveats**
- LegalOn owns the benchmark and sells a contract-review product.
- An undisclosed LLM judge and private data prevent independent reproduction.
- Elo depends on the comparison pool and should not be compared across unrelated benchmark versions.

**Verified facts**
- LegalOn's official page reports 3,282 pairwise reviews, 21 guidelines, 11 models, reversed order, tie handling, Elo, and confidence intervals.

**Unresolved ambiguity**
- The page exposes a last-updated date but no separate original publication date, so the creation date is an earliest verified first-party date rather than a confirmed launch.

[Back to page index](#on-this-page)

<a id="ivo-contract-review-study"></a>
## Ivo Contract Review Comparison

`ivo-contract-review-study` · **evaluation-protocol** · **check before use** · completed

Review and redline real contracts while preserving formatting and exercising lawyer-like judgment.

**Also known as:** Ivo vs. Claude for Word Contract Review Benchmark

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | Ivo (company; commercial interest) |
| Catalog geography | United States |
| Last verified update | — |
| Access level | private |
| Test labels | hidden |
| Independently runnable | no |

### Possible use cases

- Study a native-document contract-review protocol that includes tracked-change precision and formatting retention.
- Use the five lawyer-rated dimensions when designing blind review of an internal redlining system.
- Treat Ivo's result as a vendor-sponsored comparative study, not an independently reproducible leaderboard.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | Blind lawyer ratings across issue spotting, surgical redlining, formatting retention, judgment, and comments measure substantive and document-fidelity quality together. |
| Jurisdiction | United States commercial contracting |
| Languages | English |
| Size | 19 real anonymized NDAs, MSAs, and DPAs |
| Splits | Single private study set |
| Source material | Real anonymized commercial contracts |
| Input | Native contract document |
| Output | Reviewed/redlined contract with comments |
| Baselines / leaderboard context | Ivo was compared with Claude for Word and human work associated with the three special-counsel reviewers under the published study protocol. |
| Dataset access | Private |
| License | Not publicly stated |
| Gating | Contracts, outputs, detailed ratings, and scorer files are not public |
| Maintenance | Completed April 2026 comparative study; no public update history. |
| Reproducibility | Low because the contracts, outputs, and score sheet are private despite a concrete human-evaluation protocol. |

### Metrics

- **Mean lawyer rating across five 1–10 dimensions:** Three AmLaw 25 special counsel blindly rate issue spotting, surgical redlining, formatting retention, judgment, and comments; report dimension means and overall mean. Judge: Three human attorney judges. **Primary.**

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | None located |
| Hugging Face | None located |
| Paper / arXiv | None located |
| Leaderboard / competition | None located |
| Project | [https://www.ivo.ai/news/ivo-outperforms-claude-for-word-in-independent-contract-review-benchmark](https://www.ivo.ai/news/ivo-outperforms-claude-for-word-in-independent-contract-review-benchmark) |

### Validity and evidence

**Risks / caveats**
- Ivo sponsored the study and sells one of the compared products.
- Nineteen contracts are too few for broad practice-area claims.
- The private score sheet prevents error-level audit and uncertainty reconstruction.

**Verified facts**
- Ivo's official page states the April 2026 timing, 19 contracts, three special-counsel judges, compared systems, and five 1–10 criteria.

**Inference**
- The protocol is most valuable as a design reference for native-file review.

**Unresolved ambiguity**
- No independent paper, public data, full score sheet, repository, or update date was found.

[Back to page index](#on-this-page)

<a id="legalbenchmarks-ai"></a>
## legalbenchmarks.ai

`legalbenchmarks-ai` · **private-benchmark** · **check before use** · private

Draft contract work products and extract information from native legal documents.

**Also known as:** Legal Benchmarks AI

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | legalbenchmarks.ai (company; commercial interest) |
| Catalog geography | Multi-jurisdiction and supranational |
| Last verified update | [2026-07](https://www.legalbenchmarks.ai/leaderboard)<br>*Official leaderboard's displayed update month* |
| Access level | private |
| Test labels | hidden |
| Independently runnable | no |

### Possible use cases

- Compare public leaderboard results on native-file contract drafting and information extraction while preserving the private-test boundary.
- Use its all-criteria reliability definition to reason about matter-level failure rates.
- Use the separate usefulness dimensions to avoid equating formal criterion coverage with a usable work product.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | Reliability requires every criterion on a task to pass, while usefulness separately rates clarity, length, and structure on a three-point scale. |
| Jurisdiction | United States, United Kingdom, English-language commercial practice |
| Languages | English |
| Size | 63 tasks: 34 contract drafting and 29 information extraction |
| Splits | Private task files, source documents, and criteria; public rolling leaderboard |
| Source material | Native legal files and commercially relevant drafting/extraction tasks |
| Input | Single-turn instruction plus native files |
| Output | Drafted document or extracted information |
| Baselines / leaderboard context | The public leaderboard reports tested models and systems; underlying examples are available only by request. |
| Dataset access | Private; access by request |
| License | Not publicly stated |
| Gating | Tasks, documents, and criteria are not public |
| Maintenance | Active commercial leaderboard; series began April 2025 and was updated July 2026. |
| Reproducibility | Low independently because tasks and criteria are private, though the public page discloses judge models and score definitions. |

### Metrics

- **Reliability:** Share of tasks on which every criterion passes; a single failed criterion makes the task unreliable. Judge: Claude Sonnet 4.6. **Primary.**
- **Usefulness:** Average 1–3 ratings for clarity, length, and structure from two judges. Judge: Claude Sonnet 4.6 and Gemini 3.1 Pro.

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | None located |
| Hugging Face | None located |
| Paper / arXiv | None located |
| Leaderboard / competition | [https://www.legalbenchmarks.ai/leaderboard](https://www.legalbenchmarks.ai/leaderboard) |
| Project | [https://www.legalbenchmarks.ai/](https://www.legalbenchmarks.ai/) |

### Validity and evidence

**Risks / caveats**
- The benchmark operator controls private tasks and the leaderboard.
- All-pass reliability declines mechanically as criteria count rises, so task difficulty and rubric length matter.
- US/UK English skew limits jurisdictional generalization.

**Verified facts**
- The official leaderboard states 63 tasks, the 34/29 task split, judge models, reliability/usefulness definitions, and update timing.

**Unresolved ambiguity**
- Ownership details, task-level scores, criteria counts, and licensing are not fully public.

[Back to page index](#on-this-page)

<a id="agb-de"></a>
## AGB-DE

`agb-de` · **benchmark** · **specialist** · fixed-release

Detect potentially void clauses in German consumer standard terms and conditions.

**Also known as:** AGB-DE German consumer-clause benchmark

### Identity, update, and access

| Field | Detail |
| --- | --- |
| Owner | AGB-DE authors (academic) |
| Catalog geography | Germany |
| Last verified update | [2026-07-02](https://github.com/DaBr01/AGB-DE)<br>*GitHub repository push; latest change was citation metadata rather than benchmark data* |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Classify German consumer standard-form clauses as valid or potentially void under German law.
- Compare lexical and transformer baselines under the official train/test split and class imbalance.
- Use topic labels to stratify clause-review errors before designing a private German contract holdout.

### Evaluation contract

| Field | Detail |
| --- | --- |
| Construct / theory | Binary precision, recall, and F1 measure clause-level detection of potentially void terms; topic labels support analysis but do not replace substantive validity review. |
| Jurisdiction | Germany |
| Languages | German |
| Size | Paper and repository describe 3,764 clauses from 93 contracts; the live Hugging Face release contains 3,759 rows |
| Splits | 3,004 train and 755 test rows in the live Hub release |
| Source material | German consumer standard-form contracts annotated for validity and topic |
| Input | German contract clause |
| Output | Valid or potentially void label, with topic metadata |
| Baselines / leaderboard context | The paper compares SVM, German BERT, XLM-R, GerPT2, and GPT-3.5; the best reported F1 is 0.54 on an under-sampled variant. |
| Dataset access | Public GitHub/Hugging Face release |
| License | Hugging Face metadata: CC BY-SA 4.0; no separate root repository license was located |
| Gating | None observed |
| Maintenance | Stable ACL 2024 release; the latest 2026 repository update appears citation-only, so it is not evidence of a new dataset version. |
| Reproducibility | Good for the released split and standard classification metrics after pinning whether the 3,759-row Hub or 3,764-clause paper corpus is used. |

### Metrics

- **Precision / recall / F1:** Compute binary classification precision, recall, and F1 on the fixed test set; report the positive-class definition and any resampling. **Primary.**

### Resources

| Resource | Direct URL |
| --- | --- |
| GitHub | [https://github.com/DaBr01/AGB-DE](https://github.com/DaBr01/AGB-DE) |
| Hugging Face | [https://huggingface.co/datasets/d4br4/agb-de](https://huggingface.co/datasets/d4br4/agb-de) |
| Paper / arXiv | [https://arxiv.org/abs/2406.06809](https://arxiv.org/abs/2406.06809)<br>[https://aclanthology.org/2024.acl-long.559/](https://aclanthology.org/2024.acl-long.559/) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- The five-row paper/release discrepancy can change small test-set results.
- Severe class imbalance and topic/source shortcuts can inflate apparent validity detection.
- Public clauses and labels permit contamination and direct tuning.

**Verified facts**
- The official GitHub, Hugging Face, arXiv, and ACL artifacts establish the German clause-validity task, 93-contract source, fixed split, metrics, and baselines.
- The live Hub split totals 3,759 rows, while the paper and repository state 3,764 clauses.

**Inference**
- AGB-DE is a specialist clause-screening benchmark, not a substitute for lawyer review of enforceability in context.

**Unresolved ambiguity**
- The reason for the five missing Hub rows and the licensing of underlying contract text are not explained.

[Back to page index](#on-this-page)
