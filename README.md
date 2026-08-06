# Awesome Legal Benchmarks

<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re) [![Validate catalog](https://github.com/narcolepticchicken/awesome-legal-benchmarks/actions/workflows/validate.yml/badge.svg)](https://github.com/narcolepticchicken/awesome-legal-benchmarks/actions/workflows/validate.yml)

Use this catalog to pick a legal benchmark and see what its score can actually support. Each entry records the task, jurisdiction, language, data, input/output contract, scorer, access terms, primary sources, and the biggest validity problem.

**Research snapshot: 2026-08-05.** 89 canonical identities, including public benchmarks, private vendor benchmarks, datasets, shared tasks, evaluation frameworks, protocols, and one resource list.

> Start with the legal job. Then check jurisdiction, source material, interface, scorer, and prior exposure. If those do not match the system you care about, the score is weak evidence.

**Date rule.** The first date is the **first recorded public event**, or the earliest first-party-dated event when no public launch is exposed; it is not a generic claim that a downloadable benchmark was released that day. Every date cell names its basis: dataset creation, data commit, repository creation, paper submission, competition year, owner-reported evaluation date, or another first-party event. The latest event can likewise be a repository push, dataset update, paper revision, or official page update; it does not by itself prove that the data or scorer changed.

> **AR-BENCH status:** its [arXiv record and v1 preprint](https://arxiv.org/abs/2601.22742) are verified at 2026-01-30. No separate public AR-BENCH data, code, scorer, dataset card, project page, or leaderboard was located in the documented host searches as of 2026-08-05. That bounded negative finding is not proof that no release exists. The paper says it reannotates JuDGE material, but [JuDGE](https://github.com/oneal2000/JuDGE) is a different benchmark and not an AR-BENCH release. See the [search record and exact caveat](docs/watchlist.md#watchlist).

## Contents

- [United States](#united-states)
- [Possible use cases](#possible-use-cases)
- [Browse by area](#browse-by-area)
- [Multi-jurisdiction and supranational](#multi-jurisdiction-and-supranational)
- [International by country](#international-by-country)
- [Population not published or fixed](#population-not-published-or-fixed)
- [What the labels mean](#what-the-labels-mean)
- [Read a benchmark score](#read-a-benchmark-score)
- [Files and methodology](#files-and-methodology)
- [Contribute](#contribute)

## United States

Benchmarks whose evaluation population is exclusively or predominantly United States law or United States legal practice. Kind, access, and tier remain separate row-level fields.

Entries are ordered newest-first by first recorded public event. Contract and workflow evaluations are described as United States legal practice rather than as jurisprudence.

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [Vaquill Open Legal-Answer Benchmark](docs/benchmarks/retrieval-rag-citation.md#open-legal-answer-benchmark) | [2026-07-09](https://github.com/Vaquill-AI/open-legal-answer-benchmark) — GitHub repository creation | [2026-07-18](https://github.com/Vaquill-AI/open-legal-answer-benchmark) — GitHub repository push | benchmark / open / check before use | United States; English | Produce current US legal answers with relevant, supported, and correctly ranged citations. |
| [RedlineBench](docs/benchmarks/contracts-deal-work.md#redlinebench) | [2026-06-15](https://github.com/crosbylegal/redline-bench) — GitHub repository creation | [2026-06-26](https://github.com/crosbylegal/redline-bench) — GitHub repository push | benchmark / open / check before use | United States / commercial contracting; English | Negotiate commercial contracts over four turns by producing native Word tracked changes and comments. |
| [GC AI In-House Legal Bench](docs/benchmarks/agents-workflows.md#gc-ai-in-house-legal-bench) | [2026-05-15](https://gc.ai/blog/in-house-legal-bench-evaluating-ai-assistants-for-in-house-legal-work) — Official publication date | [2026-06-05](https://gc.ai/blog/in-house-legal-bench-evaluating-ai-assistants-for-in-house-legal-work) — Official displayed update date | private-benchmark / partial / check before use | Primarily United States; exact distribution not fully published; English | Complete common in-house legal drafting, analysis, research, strategy, extraction, regulatory, and checklist tasks. |
| [Harvey Legal Agent Benchmark (LAB)](docs/benchmarks/agents-workflows.md#harvey-lab) | [2026-05-06](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) — Official launch post | [2026-08-03](https://github.com/harveyai/harvey-labs) — GitHub repository push | benchmark / partial / check before use | United States / commercial legal practice, mixed practice areas; English | Complete long-horizon legal matters using files, research, analysis, drafting, and validation tools. |
| [LegalCiteBench](docs/benchmarks/retrieval-rag-citation.md#legalcitebench) | [2026-05-06](https://huggingface.co/datasets/legalcitebench/LegalCiteBench) — Hugging Face dataset creation | [2026-05-11](https://arxiv.org/abs/2605.10186) — arXiv v1 submission | benchmark-suite / open / recommended | United States federal appellate courts; English | Retrieve, complete, verify, and abstain on legal citations in US appellate text. |
| [Realm Legal Reasoning](docs/benchmarks/agents-workflows.md#realm-legal-reasoning) | [2026-04-10](https://www.micro1.ai/benchmark/realm-legal) — Date of the original evaluations stated on the official benchmark page; public launch date is not separately exposed | [2026-08-05](https://www.micro1.ai/benchmark/realm-legal) — Official page HTML last-published timestamp and expanded model-evaluation notice | private-benchmark / private / check before use | United States federal and state law; English | Produce and revise United States litigation, transactional, and compliance work products across evolving multi-stage matters. |
| [Legal Phantom Citation](docs/benchmarks/retrieval-rag-citation.md#legal-phantom-citation) | [2026-04-07](https://huggingface.co/datasets/ai-law-society-lab/Legal_Phantom_Citation) — Hugging Face dataset creation | [2026-07-06](https://huggingface.co/datasets/ai-law-society-lab/Legal_Phantom_Citation) — Hugging Face dataset update | benchmark / open / specialist | United States federal appellate courts, 13 circuits; English | Identify hallucinated legal citations and affected spans in federal appellate brief text. |
| [DeonticBench](docs/benchmarks/prediction-fairness-rules.md#deonticbench) | [2026-04-06](https://arxiv.org/abs/2604.04443) — arXiv v1 submission | [2026-06-04](https://huggingface.co/datasets/gydou/DeonticBench) — Hugging Face dataset update | benchmark-suite / open / recommended | United States federal tax, United States immigration, United States state housing, Airline policies; English, Prolog | Reason about obligations, permissions, prohibitions, eligibility, and amounts under long legal/policy rules, directly or through executable Prolog. |
| [Ivo Contract Review Comparison](docs/benchmarks/contracts-deal-work.md#ivo-contract-review-study) | [2026-04](https://www.ivo.ai/news/ivo-outperforms-claude-for-word-in-independent-contract-review-benchmark) — Study month stated on the official results page | None later verified | evaluation-protocol / private / check before use | United States commercial contracting; English | Review and redline real contracts while preserving formatting and exercising lawyer-like judgment. |
| [prinzbench](docs/benchmarks/related-evaluators.md#prinzbench) | [2026-01-19](https://github.com/prinz-ai/prinzbench) — GitHub repository creation | [2026-07-18](https://github.com/prinz-ai/prinzbench) — GitHub repository push | private-benchmark / private / related artifact | United States; English | Answer obscure US legal-research and general information-search questions. |
| [OpenExempt](docs/benchmarks/prediction-fairness-rules.md#openexempt) | [2026-01-11](https://huggingface.co/datasets/SergioServantez/OpenExempt) — Hugging Face dataset creation | [2026-01-21](https://huggingface.co/datasets/SergioServantez/OpenExempt) — Hugging Face dataset update | benchmark-suite / open / specialist | United States federal bankruptcy law; English | Apply structured US bankruptcy exemption rules and remain robust under controlled perturbations. |
| [CourtReasoner](docs/benchmarks/agents-workflows.md#courtreasoner) | [2025-10-29](https://github.com/yale-nlp/CourtReasoner) — GitHub repository creation | [2025-11](https://aclanthology.org/2025.emnlp-main.1787/) — EMNLP 2025 publication | benchmark / open / check before use | United States appellate law; English | Generate appellate-style judicial reasoning that identifies constraints, uses relevant authorities, and supports a valid argument under controlled factual changes. |
| [PILOT-Bench](docs/benchmarks/reasoning-education.md#pilot-bench) | [2025-10-08](https://huggingface.co/datasets/Yehoon/pilot-bench) — Hugging Face dataset creation | [2026-03-10](https://huggingface.co/datasets/Yehoon/pilot-bench) — Hugging Face dataset and GitHub repository update | benchmark-suite / open / specialist | United States Patent Trial and Appeal Board; English | Classify contested issues, Board authorities, and outcomes in US patent appeals. |
| [Vals Legal Research Benchmark](docs/benchmarks/retrieval-rag-citation.md#vals-legal-research-bench) | [2025-10](https://www.vals.ai/benchmarks/legal_research) — Earliest first-party release period located in Vals' benchmark timeline | [2026-08-03](https://www.vals.ai/benchmarks/legal_research) — Official benchmark page update date | private-benchmark / partial / check before use | United States; English | Research US legal questions and produce answers satisfying lawyer-authored substantive and citation criteria. |
| [ContractEval](docs/benchmarks/contracts-deal-work.md#contracteval) | [2025-08-05](https://arxiv.org/abs/2508.03080) — arXiv v1 submission | None later verified | evaluation-protocol / open / related artifact | United States / SEC filings; English | Evaluate long-context LLM clause-risk extraction on the public CUAD test set. |
| [RegLab Reasoning-Focused Legal Retrieval Benchmark](docs/benchmarks/retrieval-rag-citation.md#reglab-reasoning-focused-retrieval) | [2025-05-06](https://arxiv.org/abs/2505.03970) — arXiv v1 submission | None later verified | benchmark-suite / open / recommended | United States; English | Retrieve controlling text for legal questions whose answer has low lexical overlap with the relevant source. |
| [LaborBench](docs/benchmarks/retrieval-rag-citation.md#laborbench) | [2025-05-02](https://huggingface.co/datasets/reglab/laborbench) — Hugging Face dataset creation | [2025-08-26](https://arxiv.org/abs/2508.19365) — arXiv v1 submission after the dataset release | benchmark / open / specialist | United States: 50 states, District of Columbia, Puerto Rico, and U.S. Virgin Islands; English | Extract and answer state-specific unemployment-insurance law questions from statutes and regulations. |
| [Atticus Clause Retrieval Dataset](docs/benchmarks/contracts-deal-work.md#acord) | [2025-01-11](https://arxiv.org/abs/2501.06582) — arXiv v1 submission | [2025-09-21](https://arxiv.org/abs/2501.06582) — arXiv revision | benchmark / open / recommended | United States / commercial contracts; English | Rank precedent contract clauses for an attorney-written drafting need. |
| [Harvey BigLaw Bench](docs/benchmarks/agents-workflows.md#harvey-biglaw-bench) | [2024-08-29](https://www.harvey.ai/blog/introducing-biglaw-bench) — Official launch post | [2026-03-17](https://github.com/harveyai/biglaw-bench) — GitHub repository push | private-benchmark / partial / check before use | Primarily United States; later extensions described broader coverage; English | Complete transactional and litigation research, drafting, retrieval, and long-document tasks. |
| [LegalBench-RAG](docs/benchmarks/retrieval-rag-citation.md#legalbench-rag) | [2024-08-19](https://arxiv.org/abs/2408.10343) — arXiv v1 submission | [2025-05-30](https://github.com/zeroentropy-ai/legalbenchrag) — GitHub repository push | benchmark / open / recommended | United States, mixed contracts and policies; English | Retrieve exact supporting spans from long legal and policy documents. |
| [CLERC](docs/benchmarks/retrieval-rag-citation.md#clerc) | [2024-06-24](https://arxiv.org/abs/2406.17186) — arXiv v1 submission | [2025-01-28](https://github.com/bohanhou14/CLERC) — GitHub repository push | benchmark / open / specialist | United States; English | Retrieve US case-law evidence and generate citation-grounded legal text. |
| [Hallucination-Free? Legal Research Tool Study](docs/benchmarks/retrieval-rag-citation.md#reglab-legal-rag-hallucinations) | [2024-05-30](https://arxiv.org/abs/2405.20362) — arXiv v1 submission | [2024-11-14](https://huggingface.co/datasets/reglab/legal_rag_hallucinations) — Hugging Face dataset update | evaluation-protocol / partial / recommended | United States; English | Return correct, grounded, responsive legal research answers without false authority or unsupported propositions. |
| [LegalLens](docs/benchmarks/prediction-fairness-rules.md#legal-lens) | [2024-01-23](https://huggingface.co/datasets/darrow-ai/LegalLensNER) — LegalLensNER Hugging Face dataset creation | [2024-10-15](https://arxiv.org/abs/2410.12064) — NLLP shared-task paper arXiv v1 submission | benchmark-suite / partial / check before use | United States / common-law class-action context; English | Extract potential legal-violation entities from non-legal text and infer whether a violation statement entails a harmed group or legal ground. |
| [Large Legal Fictions](docs/benchmarks/retrieval-rag-citation.md#reglab-legal-hallucinations) | [2024-01-02](https://arxiv.org/abs/2401.01301) — arXiv v1 submission | [2024-06-26](https://github.com/reglab/legal_hallucinations) — GitHub repository push | benchmark-suite / partial / specialist | United States federal courts; English | Answer verifiable closed-form questions about US federal cases without inventing cases, citations, holdings, or treatment. |
| [LegalBench](docs/benchmarks/reasoning-education.md#legalbench) | [2023-08-20](https://arxiv.org/abs/2308.11462) — arXiv v1 submission | [2026-03-30](https://github.com/HazyResearch/legalbench) — GitHub repository push | benchmark-suite / open / recommended | United States, mixed/common-law; English | Task-specific legal reasoning across classification, extraction, question answering, and generation. |
| [Merger Agreement Understanding Dataset](docs/benchmarks/contracts-deal-work.md#maud) | [2023-01-02](https://arxiv.org/abs/2301.00876) — arXiv v1 submission | [2023-11-24](https://arxiv.org/abs/2301.00876) — arXiv revision | benchmark / open / recommended | United States / public-company M&A; English | Answer fine-grained questions about merger-agreement provisions. |
| [ClassActionPrediction](docs/benchmarks/prediction-fairness-rules.md#class-action-prediction) | [2022-10-24](https://github.com/darrow-labs/ClassActionPrediction) — GitHub repository and Hugging Face dataset creation | [2024-01-24](https://huggingface.co/datasets/darrow-ai/USClassActions) — Hugging Face dataset update | benchmark / open / check before use | United States federal class actions; English | Predict whether a United States federal class-action complaint will produce a plaintiff win or loss. |
| [ContractNLI](docs/benchmarks/contracts-deal-work.md#contractnli) | [2021-10-05](https://arxiv.org/abs/2110.01799) — arXiv v1 submission | [2022-02-11](https://github.com/stanfordnlp/contract-nli) — GitHub repository push | benchmark / open / recommended | Commercial NDAs / primarily United States practice; English | Determine whether a non-disclosure agreement entails, contradicts, or does not mention a fixed legal hypothesis and identify supporting evidence. |
| [CaseHOLD](docs/benchmarks/prediction-fairness-rules.md#casehold) | [2021-04-18](https://arxiv.org/abs/2104.08671) — arXiv v1 submission | [2021-07-06](https://arxiv.org/abs/2104.08671) — arXiv revision | benchmark / open / specialist | United States; English | Select the correct holding that completes an excerpt from a US judicial opinion. |
| [Contract Understanding Atticus Dataset](docs/benchmarks/contracts-deal-work.md#cuad) | [2021-03-10](https://arxiv.org/abs/2103.06268) — arXiv v1 submission | [2024-05-23](https://huggingface.co/datasets/theatticusproject/cuad-qa) — Hugging Face dataset update | benchmark / open / recommended | United States / SEC filings; English | Locate 41 categories of commercially important clauses in long contracts. |
| [LEDGAR](docs/benchmarks/contracts-deal-work.md#ledgar) | [2020-05](https://aclanthology.org/2020.lrec-1.155/) — ACL Anthology publication month | [2020-10-19](https://github.com/dtuggener/LEDGAR_provision_classification) — Original GitHub repository push | dataset / open / specialist | United States / SEC filings; English | Classify contract provisions into clause/topic labels. |
| [TREC Legal Track](docs/benchmarks/retrieval-rag-citation.md#trec-legal-track) | [2006](https://trec.nist.gov/data/legal06.html) — First official TREC Legal Track edition | [2011](https://trec.nist.gov/data/legal11.html) — Final official TREC Legal Track edition | shared-task / partial / specialist | United States civil litigation / e-discovery; English | Find documents responsive to civil-litigation production requests while minimizing review burden. |

## Possible use cases

These are starting points, not interchangeable leaderboards. Each use case names the legal work, the artifact to start with, and the decision its score can inform.

| Legal work | Start with | Possible use cases |
|---|---|---|
| Broad English legal reasoning | [LegalBench](docs/benchmarks/reasoning-education.md#legalbench) + [LexGLUE](docs/benchmarks/reasoning-education.md#lexglue) + [PRBench legal](docs/benchmarks/reasoning-education.md#prbench) | Compare per-task reasoning and language-understanding scores, then test open professional analysis against granular criteria. |
| Chinese legal reasoning and judgment generation | [LawBench](docs/benchmarks/reasoning-education.md#lawbench) + [LexEval](docs/benchmarks/reasoning-education.md#lexeval) + [JuDGE](docs/benchmarks/reasoning-education.md#judge) + [LexGenius](docs/benchmarks/reasoning-education.md#lexgenius) + [PLawBench](docs/benchmarks/reasoning-education.md#plawbench) | Screen knowledge and reasoning broadly, then inspect judgment generation, open-ended consultation, case analysis, and drafting as separate constructs. |
| Chinese statute and case retrieval | [STARD](docs/benchmarks/retrieval-rag-citation.md#stard) + [LeCaRDv2](docs/benchmarks/retrieval-rag-citation.md#lecardv2) | Use STARD for lay-query statute retrieval and LeCaRDv2 for expert-graded criminal-case similarity; do not combine their scores. |
| Korean legal knowledge, reasoning, and RAG | [KBL](docs/benchmarks/reasoning-education.md#kbl) + [KCL](docs/benchmarks/reasoning-education.md#kcl) | Use KBL for public MCQ task cells and retrieval augmentation; use KCL separately for bar-exam MCQ and rubric-scored essays. |
| Arabic and Saudi legal work | [ArabLegalEval](docs/benchmarks/reasoning-education.md#arablegaleval) + [ALARB](docs/benchmarks/reasoning-education.md#alarb) | Separate translated or synthetic tasks from Saudi case-based verdict, argument, and statutory-article tasks. |
| Multilingual legal NLU | [LEXTREME](docs/benchmarks/reasoning-education.md#lextreme) | Compare per-language and per-task behavior before relying on its hierarchical aggregate. |
| Indian legal NLU and authority retrieval | [IL-TUR](docs/benchmarks/reasoning-education.md#il-tur) + [ILSIC](docs/benchmarks/retrieval-rag-citation.md#ilsic) + [AILA 2019](docs/benchmarks/retrieval-rag-citation.md#aila-2019) | Use IL-TUR for task/language breadth, ILSIC for lay-query statute identification, and AILA as a small historical precedent/statute retrieval diagnostic. |
| Italian statutory retrieval | [JuriFindIT](docs/benchmarks/retrieval-rag-citation.md#jurifindit) | Test article retrieval against expert Italian judgments while keeping synthetic-query results separate. |
| German case-law retrieval | [GerDaLIR](docs/benchmarks/retrieval-rag-citation.md#gerdalir) | Compare sparse and neural full-ranking systems, while treating parsed citations as proxy relevance rather than expert judgments. |
| Portuguese legal education | [LegalBench.PT](docs/benchmarks/reasoning-education.md#legalbench-pt) | Compare task and field cells on Portuguese law, then recheck synthetic labels before drawing capability conclusions. |
| Brazilian legal drafting and bar-exam work | [OAB-Bench](docs/benchmarks/reasoning-education.md#oab-bench) | Audit criterion-level judge outputs on Phase 2 writing tasks with the exam edition and judge version fixed. |
| Patent and intellectual-property work | [PILOT-Bench](docs/benchmarks/reasoning-education.md#pilot-bench) + [MoZIP](docs/benchmarks/reasoning-education.md#mozip) | Compare US patent-appeal classification with multilingual IP knowledge, open QA, and patent-semantic matching; neither substitutes for a private drafting or validity-review holdout. |
| Multimodal legal education | [RoD-TAL](docs/benchmarks/retrieval-rag-citation.md#rod-tal) | Test Romanian traffic-law retrieval and QA when images or signs are legally material. |
| Contract extraction and classification | [CUAD](docs/benchmarks/contracts-deal-work.md#cuad) + [ContractNLI](docs/benchmarks/contracts-deal-work.md#contractnli) + [MAUD](docs/benchmarks/contracts-deal-work.md#maud) | Test clause finding, evidence entailment, and merger-agreement provision classification on document-family-held-out data. |
| Contract retrieval | [ACORD](docs/benchmarks/contracts-deal-work.md#acord) | Rank clauses against attorney-authored requests using graded relevance judgments. |
| Redlining and contract review | [RedlineBench](docs/benchmarks/contracts-deal-work.md#redlinebench) + [LegalOn 2026](docs/benchmarks/contracts-deal-work.md#legalon-contract-review-2026) + [Ivo study](docs/benchmarks/contracts-deal-work.md#ivo-contract-review-study) + [legalbenchmarks.ai](docs/benchmarks/contracts-deal-work.md#legalbenchmarks-ai) | Test native-file edits, issue spotting, formatting retention, and review usefulness; only RedlineBench is openly runnable. |
| United States legal retrieval and RAG | [LegalBench-RAG](docs/benchmarks/retrieval-rag-citation.md#legalbench-rag) + [LaborBench](docs/benchmarks/retrieval-rag-citation.md#laborbench) + [RegLab retrieval](docs/benchmarks/retrieval-rag-citation.md#reglab-reasoning-focused-retrieval) + [Legal RAG Bench](docs/benchmarks/retrieval-rag-citation.md#legal-rag-bench) | Measure authority retrieval, answer correctness, citation extraction, refusal, and grounding separately on a current United States corpus. |
| Belgian legal retrieval and QA | [BSARD](docs/benchmarks/retrieval-rag-citation.md#bsard) + [LLeQA](docs/benchmarks/retrieval-rag-citation.md#lleqa) + [bLLeQA](docs/benchmarks/retrieval-rag-citation.md#blleqa) | Compare article retrieval and downstream QA on Belgian law without folding the results into other jurisdictions. |
| Canadian legal RAG | [CanLegalRAGBench](docs/benchmarks/retrieval-rag-citation.md#canlegalragbench) | Measure retrieval, answer correctness, completeness, and citation grounding on the released Canadian legal corpus. |
| United States e-discovery and technology-assisted review | [TREC Legal](docs/benchmarks/retrieval-rag-citation.md#trec-legal-track) | Use the archived annual protocols as a historical retrieval and review-effort reference, not as a current production corpus. |
| Citation safety | [LegalCiteBench](docs/benchmarks/retrieval-rag-citation.md#legalcitebench) + [Legal Phantom Citation](docs/benchmarks/retrieval-rag-citation.md#legal-phantom-citation) + [Large Legal Fictions](docs/benchmarks/retrieval-rag-citation.md#reglab-legal-hallucinations) + [Hallucination-Free?](docs/benchmarks/retrieval-rag-citation.md#reglab-legal-rag-hallucinations) | Test citation retrieval, abstention, phantom-citation detection, and human-coded research-tool hallucination as distinct failure modes. |
| Long-horizon legal agents | [DLawBench](docs/benchmarks/agents-workflows.md#dlawbench) + [Harvey LAB](docs/benchmarks/agents-workflows.md#harvey-lab) + [Realm Legal Reasoning](docs/benchmarks/agents-workflows.md#realm-legal-reasoning) + [Legora BAR](docs/benchmarks/agents-workflows.md#legora-bar) + [Mercor APEX legal](docs/benchmarks/agents-workflows.md#apex-agents-corporate-law) | Evaluate consultation or matter completion with files, tools, rubrics, repeated runs, cost, and latency; Realm and BAR remain owner-controlled instruments. |
| In-house legal work | [GC AI In-House Legal Bench](docs/benchmarks/agents-workflows.md#gc-ai-in-house-legal-bench) + [CoCoBench](docs/benchmarks/agents-workflows.md#thomson-reuters-cocobench) + [Harvey BigLaw Bench](docs/benchmarks/agents-workflows.md#harvey-biglaw-bench) | Use their task taxonomies and published results as private-vendor evidence when designing an internal matter-level holdout. |
| Rule and robustness testing | [DeonticBench](docs/benchmarks/prediction-fairness-rules.md#deonticbench) + [OpenExempt](docs/benchmarks/prediction-fairness-rules.md#openexempt) | Test deontic consistency and symbolic statutory reasoning under controlled perturbations. |
| Fairness and subgroup performance | [FairLex](docs/benchmarks/prediction-fairness-rules.md#fairlex) | Compare overall, per-group, worst-group, and gap metrics with group sizes and uncertainty. |
| Legal translation | [SwiLTra-Bench](docs/benchmarks/translation.md#swiltra-bench) + [MILPaC](docs/benchmarks/translation.md#milpac) + [JUST-NLP 2025](docs/benchmarks/translation.md#just-nlp-2025-legal-mt) | Compare automatic metrics with legal-expert ratings for terminology, omissions, and legal effect. |
| Vietnamese legal reasoning | [VLegal-Bench](docs/benchmarks/reasoning-education.md#vlegal-bench) | Run its task-specific metrics across Vietnamese legal knowledge, reasoning, drafting, and ethics; pin the exact release because the paper and repository counts disagree. |
| Moroccan legal knowledge and calibration | [MizanQA](docs/benchmarks/reasoning-education.md#mizanqa) | Measure strict answer accuracy and calibration-aware scores on Moroccan law while reporting the live 1,769-row release separately from the paper's 1,776-item claim. |
| Legal summarization | [LexSumm](docs/benchmarks/reasoning-education.md#lexsumm) | Compare models per constituent dataset with ROUGE and BERTScore; do not convert eight heterogeneous datasets into an unsupported single legal-fidelity score. |
| Judicial reasoning generation | [CourtReasoner](docs/benchmarks/agents-workflows.md#courtreasoner) | Test US appellate opinion reasoning and adversarial fact sensitivity, then separately audit how well each LLM grader agrees with human experts. |
| Outcome prediction with explanations | [PredEx](docs/benchmarks/prediction-fairness-rules.md#predex) + [ClassActionPrediction](docs/benchmarks/prediction-fairness-rules.md#class-action-prediction) | Keep Indian appeal prediction with extractive explanations separate from US class-action outcome prediction; both need leakage and shortcut audits. |
| Chinese conversational and similar-case retrieval | [LexRAG](docs/benchmarks/retrieval-rag-citation.md#lexrag) + [MUSER](docs/benchmarks/retrieval-rag-citation.md#muser) | Use LexRAG for multi-turn statute-grounded consultation and MUSER for civil similar-case retrieval; their corpora, judges, and relevance definitions are not interchangeable. |
| German consumer-contract clause review | [AGB-DE](docs/benchmarks/contracts-deal-work.md#agb-de) | Evaluate potentially void standard-form clauses in German, while disclosing the five-row difference between the paper and live Hub release. |
| Legal violation detection | [LegalLens](docs/benchmarks/prediction-fairness-rules.md#legal-lens) | Evaluate span extraction and entailment for potential legal violations in class-action source text, keeping the synthetic-then-reviewed provenance and shared-task split boundary visible. |

Pair any public comparison with a fresh, matter-specific holdout before making a deployment or procurement decision. The [selection guide](docs/selection-guide.md) gives a fuller recommendation matrix.

## Browse by area

Each category page contains full profiles with owner, first recorded public event, latest verified event, access boundary, metrics, direct official sources, possible uses, and unresolved facts.

| Area | What is inside | Entries |
|---|---|---:|
| [General legal reasoning and education](docs/benchmarks/reasoning-education.md) | Broad suites, legal language understanding, professional exams, and jurisdiction-specific knowledge tests. | 22 |
| [Retrieval, RAG, and citation](docs/benchmarks/retrieval-rag-citation.md) | Authority retrieval, exact-support retrieval, case similarity, citation grounding, and end-to-end legal RAG. | 28 |
| [Contracts and deal work](docs/benchmarks/contracts-deal-work.md) | Clause extraction, provision classification, entailment, retrieval, merger agreements, and redlining. | 11 |
| [Prediction, fairness, and structured reasoning](docs/benchmarks/prediction-fairness-rules.md) | Outcome prediction, subgroup performance, holding selection, deontic rules, and structured legal analysis. | 10 |
| [Agents and legal workflows](docs/benchmarks/agents-workflows.md) | Tool use, process compliance, simulated legal work, and long-horizon professional tasks. | 11 |
| [Legal translation](docs/benchmarks/translation.md) | Shared tasks and multilingual corpora with automatic and legal-expert translation scoring. | 3 |
| [Evaluators, private tests, and related resources](docs/benchmarks/related-evaluators.md) | Artifacts worth tracking that are not comparable public benchmarks, including frameworks, private tests, and resource lists. | 4 |

See the [compact 89-entry index](docs/catalog.md), or filter the machine-readable [JSON](catalog/benchmarks.json), [CSV](catalog/benchmarks.csv), and [workbook](outputs/awesome-legal-benchmarks.xlsx).

## Multi-jurisdiction and supranational

Fixed artifacts designed around more than one national legal system, a supranational legal order, or an official multi-country competition identity. Inclusion here is descriptive, not a claim of prestige or equal country coverage.

This is a geography bucket, not an adoption or prestige rating. The catalog does not infer that a benchmark is ‘highly regarded’ from citations, a leaderboard, or its owner's claims.

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [DLawBench](docs/benchmarks/agents-workflows.md#dlawbench) | [2026-06-09](https://github.com/SKYLENAGE-AI/DLawBench) — GitHub repository creation | [2026-06-11](https://arxiv.org/abs/2606.13931) — arXiv v1 submission | benchmark / open / recommended | China, United States; Chinese, English | Conduct multi-turn legal consultations and turn elicited facts into a reasoned legal memorandum. |
| [Professional Reasoning Benchmark (PRBench)](docs/benchmarks/reasoning-education.md#prbench) | [2025-11-13](https://github.com/scaleapi/PRBench) — GitHub and Hugging Face release | [2026-06-24](https://huggingface.co/datasets/ScaleAI/PRBench) — Hugging Face dataset update | benchmark / open / check before use | 114 countries, 47 United States jurisdictions; English | Produce open-ended professional legal analysis that satisfies granular expert-authored criteria. |
| [Massive Legal Embedding Benchmark](docs/benchmarks/retrieval-rag-citation.md#mleb) | [2025-10-22](https://arxiv.org/abs/2510.19365) — arXiv v1 submission | [2026-02-24](https://github.com/isaacus-dev/mleb) — GitHub repository push | benchmark-suite / open / specialist | United States, United Kingdom, European Union, Australia, Ireland, Singapore; English | Legal embedding quality across retrieval, retrieval-augmented QA, and zero-shot classification tasks. |
| [LEXam](docs/benchmarks/reasoning-education.md#lexam) | [2025-05-19](https://arxiv.org/abs/2505.12864) — arXiv v1 submission | [2026-05-21](https://huggingface.co/datasets/LEXam-Benchmark/LEXam) — Hugging Face dataset update | benchmark / open / recommended | Germany, United States / English-language courses, mixed law-school curricula; English, German | Answer bilingual law-school multiple-choice and open-answer examination questions. |
| [legalbenchmarks.ai](docs/benchmarks/contracts-deal-work.md#legalbenchmarks-ai) | [2025-04](https://www.legalbenchmarks.ai/leaderboard) — Benchmark series start stated on the official leaderboard | [2026-07](https://www.legalbenchmarks.ai/leaderboard) — Official leaderboard's displayed update month | private-benchmark / private / check before use | United States, United Kingdom, English-language commercial practice; English | Draft contract work products and extract information from native legal documents. |
| [LexSumm](docs/benchmarks/reasoning-education.md#lexsumm) | [2024-10-12](https://arxiv.org/abs/2410.09527) — arXiv v1 and GitHub repository creation | [2024-11-19](https://github.com/TUMLegalTech/LexSumm-LexT5) — Canonical GitHub repository push | benchmark-suite / open / check before use | United States, United Kingdom, European Union, India, Multi-jurisdictional legal sources; English | Generate abstractive summaries of legislation, cases, and government/legal reports across eight public datasets. |
| [MoZIP](docs/benchmarks/reasoning-education.md#mozip) | [2024-02-26](https://arxiv.org/abs/2402.16389) — MoZIP paper arXiv v1 submission | [2024-08-20](https://github.com/AI-for-Science/MoZi) — Canonical GitHub repository push | benchmark-suite / open / specialist | International and mixed national intellectual-property sources, WIPO patent corpus; Chinese, English, German, Spanish, Japanese, Korean, Portuguese, French, Russian | Answer multilingual intellectual-property questions and match patent abstracts to the most similar patent. |
| [LEXTREME](docs/benchmarks/reasoning-education.md#lextreme) | [2023-01-30](https://arxiv.org/abs/2301.13126) — arXiv v1 submission | [2026-05-20](https://huggingface.co/datasets/joelniklaus/lextreme) — Hugging Face dataset update | benchmark-suite / open / recommended | European Union, Council of Europe, European national jurisdictions; 24 European languages | Multilingual European legal classification and named-entity recognition across 24 languages. |
| [FairLex](docs/benchmarks/prediction-fairness-rules.md#fairlex) | [2022-05](https://aclanthology.org/2022.acl-long.301/) — ACL Anthology publication month | [2023-07-27](https://huggingface.co/datasets/coastalcph/fairlex) — Hugging Face dataset update | benchmark-suite / open / recommended | Council of Europe, United States, Switzerland, China; English, German, French, Italian, Chinese | Evaluate legal prediction performance and group robustness across sensitive or legally salient subpopulations. |
| [LexGLUE](docs/benchmarks/reasoning-education.md#lexglue) | [2021-10-03](https://arxiv.org/abs/2110.00976) — arXiv v1 submission | [2025-07-23](https://github.com/coastalcph/lex-glue) — GitHub repository push | benchmark-suite / open / recommended | Council of Europe, European Union, United States, mixed contracts/terms; English | Standardized English legal language understanding across seven classification and judgment tasks. |
| [Competition on Legal Information Extraction/Entailment](docs/benchmarks/retrieval-rag-citation.md#coliee) | [2014](https://coliee.org/COLIEE2025/overview) — Official COLIEE history; COLIEE 2025 is identified as the 12th competition | [2026-06](https://coliee.org/COLIEE2026/program) — COLIEE 2026 workshop program | shared-task / gated / recommended | Canada, Japan; English, Japanese | Retrieve and recognize entailment among Canadian cases and Japanese civil-code provisions. |

## International by country

Country-specific entries are kept out of the United States list and grouped alphabetically by jurisdiction. Within each country they are grouped by the calendar year of the first recorded public event, newest year first, then ordered newest-first inside that year. These are date-provenance bands, not claims that downloadable data were released in that year. Mixed populations remain explicit in the row instead of being silently treated as single-country evidence.

### Australia

Australian law; the full evaluation population remains visible in each row.

#### First recorded event in 2026

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [Legal RAG Bench](docs/benchmarks/retrieval-rag-citation.md#legal-rag-bench) | [2026-03-02](https://arxiv.org/abs/2603.01710) — arXiv v1 submission | [2026-03-08](https://huggingface.co/datasets/isaacus/legal-rag-bench) — Hugging Face dataset update | benchmark / open / check before use | Victoria, Australia / criminal law and procedure; English | Evaluate an end-to-end legal RAG pipeline and attribute errors to retrieval versus generation. |

### Belgium

Belgian law and Belgian legal-language evaluation.

#### First recorded event in 2025

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [bLLeQA](docs/benchmarks/retrieval-rag-citation.md#blleqa) | [2025-08-20](https://huggingface.co/datasets/clips/bLLeQA) — Hugging Face dataset creation | [2026-07-03](https://aclanthology.org/2026.knowfm-1.4.pdf) — KnowFM 2026 publication date | benchmark-suite / gated / specialist | Belgium, France and Netherlands source alignment described by the release; French, Dutch | Retrieve Belgian statutory support and answer grounded legal questions in French and Dutch, including refusal when evidence is insufficient. |

#### First recorded event in 2023

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [LLeQA](docs/benchmarks/retrieval-rag-citation.md#lleqa) | [2023-09-29](https://arxiv.org/abs/2309.17050) — arXiv v1 submission | [2024-09-03](https://huggingface.co/datasets/maastrichtlawtech/lleqa) — Hugging Face dataset update | benchmark / gated / specialist | Belgium; French | Retrieve Belgian legal authorities and generate long-form answers to practitioner-style questions. |

#### First recorded event in 2021

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [Belgian Statutory Article Retrieval Dataset](docs/benchmarks/retrieval-rag-citation.md#bsard) | [2021-08-26](https://arxiv.org/abs/2108.11792) — arXiv v1 submission | [2024-05-31](https://huggingface.co/datasets/maastrichtlawtech/bsard) — Hugging Face dataset update | benchmark / open / recommended | Belgium; French | Retrieve Belgian statutory articles relevant to a legal question. |

### Brazil

Brazilian law and Brazilian professional legal-writing evaluation.

#### First recorded event in 2025

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [OAB-Bench](docs/benchmarks/reasoning-education.md#oab-bench) | [2025-04-28](https://github.com/maritaca-ai/oab-bench) — GitHub repository creation | [2026-06-01](https://huggingface.co/datasets/maritaca-ai/oab-bench) — Hugging Face dataset update for the expanded release | benchmark / open / specialist | Brazil; Portuguese (Brazilian) | Draft Brazilian legal documents and answer discursive professional-exam questions under official examiner guidelines. |

### Canada

Canadian law; COLIEE is listed separately as a Canada/Japan competition identity.

#### First recorded event in 2026

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [CanLegalRAGBench](docs/benchmarks/retrieval-rag-citation.md#canlegalragbench) | [2026-05-28](https://arxiv.org/abs/2605.30497) — arXiv v1 submission | [2026-07-20](https://github.com/NLP-UBC/CanLegalRAGBench) — GitHub repository push | benchmark / open / specialist | Canada, Ontario, British Columbia, Alberta, other Canadian provinces/federal courts; English, some French passages | Retrieve Canadian case law for realistic layperson and legal-professional queries and generate grounded answers. |
| [Vals CaseLaw v2](docs/benchmarks/retrieval-rag-citation.md#vals-caselaw-v2) | [2026-02-05](https://www.vals.ai/benchmarks/case_law_v2) — Earliest dated first-party page located with CaseLaw v2 present | [2026-05-04](https://www.vals.ai/benchmarks/case_law_v2) — Official benchmark page update date | private-benchmark / private / related artifact | Canada; English | Answer Canadian case-law questions with correct, relevant, well-supported legal analysis. |

### China

Chinese law and Chinese-language legal evaluation; artifacts designed around China and another national legal system are listed in the multi-jurisdiction section.

#### First recorded event in 2026

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [PLawBench](docs/benchmarks/reasoning-education.md#plawbench) | [2026-01-05](https://github.com/SKYLENAGE-AI/PLawBench) — GitHub repository creation | [2026-07](https://aclanthology.org/2026.acl-long.458/) — ACL 2026 publication | benchmark-suite / partial / check before use | China; Chinese | Answer Chinese legal consultations, analyze practical cases, and draft legal documents. |

#### First recorded event in 2025

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [MSLR-Bench](docs/benchmarks/prediction-fairness-rules.md#mslr) | [2025-11-11](https://arxiv.org/abs/2511.07979) — arXiv v1 submission | [2026-06-29](https://github.com/yuwenhan07/MSLR-Bench) — GitHub repository push | benchmark / open / check before use | China; Chinese | Extract structured facts and produce IRAC-style reasoning for Chinese insider-trading cases. |
| [LexGenius](docs/benchmarks/reasoning-education.md#lexgenius) | [2025-10-27](https://github.com/QwenQKing/LexGenius) — GitHub repository creation | [2026-04-16](https://arxiv.org/abs/2512.04578) — arXiv v3 revision | benchmark-suite / open / recommended | China; Chinese | Answer broad Chinese legal knowledge and reasoning questions across seven dimensions and eleven tasks. |
| [Ready Jurist One (J1Bench)](docs/benchmarks/agents-workflows.md#ready-jurist-one) | [2025-07-05](https://arxiv.org/abs/2507.04037) — arXiv v1 submission | [2026-04-07](https://github.com/FudanDISC/J1Bench) — GitHub repository push | benchmark / open / specialist | China; Chinese | Operate interactively in Chinese legal consultation, drafting, civil-court, and criminal-court environments. |
| [LegalEval-Q](docs/benchmarks/related-evaluators.md#legaleval-q) | [2025-05-30](https://arxiv.org/abs/2505.24826) — arXiv v1 submission | [2026-02-26](https://github.com/lyxx3rd/LegalEval-Q) — GitHub repository push | evaluation-framework / open / related artifact | China; Chinese | Predict the quality of Chinese LLM-generated legal answers. |
| [JuDGE](docs/benchmarks/reasoning-education.md#judge) | [2025-02-24](https://github.com/oneal2000/JuDGE/commit/30c389ad9c506164f05f00c5e75c86bbdb8184de) — Benchmark data first committed to the official GitHub repository | [2025-08-07](https://github.com/oneal2000/JuDGE) — GitHub repository push | benchmark / open / specialist | China; Chinese | Generate a complete Chinese criminal judgment document from a factual description. |
| [LexRAG](docs/benchmarks/retrieval-rag-citation.md#lexrag) | [2025-02-10](https://github.com/CSHaitao/LexRAG) — GitHub repository creation | [2025-03-03](https://github.com/CSHaitao/LexRAG) — GitHub repository push | benchmark / open / check before use | China; Chinese | Retrieve relevant Chinese legal articles and answer five-turn legal consultation dialogues with grounded responses. |

#### First recorded event in 2024

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [LegalAgentBench](docs/benchmarks/agents-workflows.md#legalagentbench) | [2024-12-23](https://arxiv.org/abs/2412.17259) — arXiv v1 submission | [2026-04-10](https://github.com/CSHaitao/LegalAgentBench) — GitHub repository push | benchmark / open / specialist | China; Chinese | Chinese legal tool use, multi-hop information gathering, and legal writing. |
| [LexEval](docs/benchmarks/reasoning-education.md#lexeval) | [2024-09-30](https://arxiv.org/abs/2409.20288) — arXiv v1 submission | [2024-11-26](https://arxiv.org/abs/2409.20288) — arXiv revision | benchmark-suite / open / specialist | China; Chinese | Chinese legal knowledge, inference, generation, discrimination, and ethics across 23 tasks. |
| [STARD](docs/benchmarks/retrieval-rag-citation.md#stard) | [2024-03-17](https://github.com/oneal2000/STARD) — GitHub repository creation | [2025-04-24](https://github.com/oneal2000/STARD) — Last verified GitHub repository push affecting the benchmark artifact | benchmark / open / specialist | China; Chinese | Retrieve all Chinese statutory articles relevant to an informal real-world legal consultation query. |

#### First recorded event in 2023

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [LeCaRDv2](docs/benchmarks/retrieval-rag-citation.md#lecardv2) | [2023-10-26](https://arxiv.org/abs/2310.17609) — arXiv v1 submission | [2024-12-29](https://github.com/THUIR/LeCaRDv2) — GitHub repository push | benchmark / open / recommended | China; Chinese | Retrieve legally similar Chinese criminal cases using graded relevance across characterization, penalty, and procedure. |
| [LawBench](docs/benchmarks/reasoning-education.md#lawbench) | [2023-09-28](https://arxiv.org/abs/2309.16289) — arXiv v1 submission | [2025-03-07](https://huggingface.co/datasets/doolayer/LawBench) — Hugging Face dataset update | benchmark-suite / open / recommended | China; Chinese | Chinese legal memorization, understanding, and application across 20 tasks. |
| [MUSER](docs/benchmarks/retrieval-rag-citation.md#muser) | [2023-06-16](https://github.com/THUlawtech/MUSER) — GitHub repository creation | [2025-07-25](https://github.com/THUlawtech/MUSER) — GitHub repository push | benchmark / open / specialist | China; Chinese | Retrieve similar Chinese civil cases using multiple legally relevant views of case similarity. |

### Council of Europe

Evaluation tied to the European Convention system rather than one national jurisdiction.

#### First recorded event in 2019

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [ECtHR Tasks A/B](docs/benchmarks/prediction-fairness-rules.md#ecthr) | [2019-06-05](https://arxiv.org/abs/1906.02059) — arXiv v1 submission | [2025-07-23](https://github.com/coastalcph/lex-glue) — Canonical LexGLUE repository push | benchmark / open / recommended | European Court of Human Rights / Council of Europe; English | Predict European Convention articles alleged (Task A) or found violated (Task B) from case facts. |

### Germany

German law and German-language legal evaluation.

#### First recorded event in 2024

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [AGB-DE](docs/benchmarks/contracts-deal-work.md#agb-de) | [2024-05-28](https://github.com/DaBr01/AGB-DE) — GitHub repository creation | [2026-07-02](https://github.com/DaBr01/AGB-DE) — GitHub repository push; latest change was citation metadata rather than benchmark data | benchmark / open / specialist | Germany; German | Detect potentially void clauses in German consumer standard terms and conditions. |

#### First recorded event in 2021

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [GerDaLIR](docs/benchmarks/retrieval-rag-citation.md#gerdalir) | [2021-09-28](https://github.com/lavis-nlp/GerDaLIR) — GitHub repository creation | [2024-02-26](https://github.com/lavis-nlp/GerDaLIR) — Last verified GitHub repository push affecting the benchmark artifact | benchmark / open / specialist | Germany; German | Retrieve German case decisions cited by a passage expressing a legal statement or line of argument. |

### India

Indian law and Indian legal-language evaluation.

#### First recorded event in 2026

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [ILSIC](docs/benchmarks/retrieval-rag-citation.md#ilsic) | [2026-01-23](https://github.com/Law-AI/ilsic) — GitHub repository creation | [2026-02-03](https://github.com/Law-AI/ilsic) — GitHub repository push | dataset / partial / specialist | India; English, Indian legal-query language | Identify Indian statutes relevant to layperson and court-derived legal queries. |

#### First recorded event in 2025

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [JUST-NLP 2025 Legal MT Shared Task](docs/benchmarks/translation.md#just-nlp-2025-legal-mt) | [2025-12](https://aclanthology.org/2025.justnlp-main.3/) — ACL Anthology publication month | None later verified | shared-task / gated / specialist | India; English, Hindi | Translate legal text from English to Hindi. |

#### First recorded event in 2024

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [IL-TUR](docs/benchmarks/reasoning-education.md#il-tur) | [2024-07-07](https://arxiv.org/abs/2407.05399) — arXiv v1 submission | [2025-06-07](https://github.com/Exploration-Lab/IL-TUR) — GitHub repository push | benchmark-suite / open / recommended | India; English, Hindi, Bengali, Gujarati, Marathi, Malayalam, Odia, Punjabi, Tamil, Telugu | Indian legal named entities, rhetorical roles, judgment/explanation, bail, statute identification, precedent retrieval, summarization, and translation. |
| [PredEx](docs/benchmarks/prediction-fairness-rules.md#predex) | [2024-02-15](https://github.com/ShubhamKumarNigam/PredEx) — GitHub repository creation | [2026-06-03](https://github.com/ShubhamKumarNigam/PredEx) — GitHub repository push; latest change was citation metadata rather than benchmark data | benchmark / open / check before use | India; English | Predict whether an Indian Supreme Court appeal or petition is accepted or rejected and extract supporting explanatory text. |

#### First recorded event in 2023

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [Multilingual Indian Legal Parallel Corpus](docs/benchmarks/translation.md#milpac) | [2023-10-15](https://arxiv.org/abs/2310.09765) — arXiv v1 submission | [2025-07-13](https://github.com/Law-AI/MILPaC) — GitHub repository push | benchmark-suite / open / recommended | India; English, Hindi, Bengali, Marathi, Tamil, Gujarati, Telugu, Malayalam, Punjabi, Odia | Translate verified Indian legal text from English into nine Indian languages. |

#### First recorded event in 2019

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [AILA 2019](docs/benchmarks/retrieval-rag-citation.md#aila-2019) | [2019](https://ceur-ws.org/Vol-2517/T1-1.pdf) — FIRE 2019 shared-task edition; exact first public data-release date was not located | [2020-10-03](https://zenodo.org/records/4063986) — Zenodo dataset record modification | shared-task / open / specialist | India; English | Rank relevant Indian Supreme Court precedents and statutory sections for a factual legal scenario. |

### Italy

Italian law.

#### First recorded event in 2025

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [JuriFindIT](docs/benchmarks/retrieval-rag-citation.md#jurifindit) | [2025-09-29](https://huggingface.co/datasets/jurifindit/JuriFindIT) — Hugging Face dataset creation | [2026-03](https://aclanthology.org/2026.findings-eacl.221/) — Findings of EACL 2026 publication | benchmark / open / specialist | Italy, European Union materials within the corpus; Italian | Retrieve Italian statutory articles relevant to natural-language legal questions. |

### Morocco

Moroccan law and Moroccan Arabic legal evaluation.

#### First recorded event in 2025

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [MizanQA](docs/benchmarks/reasoning-education.md#mizanqa) | [2025-08-22](https://arxiv.org/abs/2508.16357) — arXiv v1 and Hugging Face dataset release | [2026-03](https://aclanthology.org/2026.eacl-industry.10/) — EACL 2026 Industry Track publication | benchmark / open / check before use | Morocco; Arabic (Modern Standard Arabic with Moroccan legal usage) | Answer expert-verified multiple-choice questions about Moroccan law and associated legal traditions. |

### Portugal

Portuguese law and European Portuguese legal evaluation.

#### First recorded event in 2024

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [LegalBench.PT](docs/benchmarks/reasoning-education.md#legalbench-pt) | [2024-10-28](https://huggingface.co/datasets/BeatrizCanaverde/LegalBench.PT) — Hugging Face dataset creation | [2026-05-06](https://huggingface.co/datasets/BeatrizCanaverde/LegalBench.PT) — Hugging Face dataset update | benchmark / open / check before use | Portugal; Portuguese (European) | Answer European Portuguese questions testing knowledge and application of Portuguese law across 31 legal fields. |

### Romania

Romanian law.

#### First recorded event in 2025

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [RoD-TAL](docs/benchmarks/retrieval-rag-citation.md#rod-tal) | [2025-07-25](https://arxiv.org/abs/2507.19666) — arXiv v1 submission | [2026-04-30](https://huggingface.co/datasets/GRAI-UNSTPB/RoD-TAL) — Hugging Face dataset update | benchmark-suite / gated / specialist | Romania; Romanian | Answer Romanian driving-law questions and retrieve governing law or traffic signs from text and images. |

### Saudi Arabia

Saudi law; translated or broader Arab-jurisdiction material remains disclosed in the row.

#### First recorded event in 2025

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [Arabic Legal Argument Reasoning Benchmark (ALARB)](docs/benchmarks/reasoning-education.md#alarb) | [2025-10-01](https://arxiv.org/abs/2510.00694) — arXiv v1 submission | [2025-10-15](https://huggingface.co/datasets/THIQAH-RD/ALARB) — Hugging Face dataset update | dataset / open / check before use | Saudi Arabia; Arabic | Reason over Saudi commercial-law cases, complete arguments, and identify governing statutory articles. |

#### First recorded event in 2024

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [ArabLegalEval](docs/benchmarks/reasoning-education.md#arablegaleval) | [2024-08-15](https://arxiv.org/abs/2408.07983) — arXiv v1 submission | [2025-05-21](https://github.com/Thiqah/ArabLegalEval) — GitHub repository push | benchmark-suite / open / check before use | Saudi Arabia, Arab jurisdictions / translated sources; Arabic, English | Arabic legal knowledge, classification, question answering, and translation, with substantial Saudi-law coverage. |

### South Korea

South Korean law.

#### First recorded event in 2025

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [Korean Canonical Legal Benchmark](docs/benchmarks/reasoning-education.md#kcl) | [2025-12-31](https://arxiv.org/abs/2512.24572) — arXiv v1 submission | [2026-01-23](https://github.com/lbox-kr/kcl) — GitHub repository push | benchmark-suite / open / recommended | South Korea; Korean | Answer Korean bar-exam MCQs and essays with question-aligned supporting precedents. |

#### First recorded event in 2024

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [KBL](docs/benchmarks/reasoning-education.md#kbl) | [2024-10-02](https://github.com/lbox-kr/kbl) — GitHub repository creation | [2025-05-19](https://huggingface.co/datasets/lbox/kbl) — Hugging Face benchmark dataset update | benchmark-suite / open / specialist | South Korea; Korean | Answer Korean legal knowledge, legal reasoning, and bar-examination multiple-choice questions with or without retrieved statutes and precedents. |

### Switzerland

Swiss law and Swiss legal languages.

#### First recorded event in 2025

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [SwiLTra-Bench](docs/benchmarks/translation.md#swiltra-bench) | [2025-03-03](https://arxiv.org/abs/2503.01372) — arXiv v1 submission | [2025-05-30](https://arxiv.org/abs/2503.01372) — arXiv revision | benchmark-suite / open / recommended | Switzerland; German, French, Italian, Romansh, English | Translate Swiss laws, court headnotes, and press releases among official Swiss languages and English. |

### United Kingdom

United Kingdom law and regulatory enforcement.

#### First recorded event in 2025

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [MASLegalBench](docs/benchmarks/prediction-fairness-rules.md#maslegalbench) | [2025-09-29](https://arxiv.org/abs/2509.24922) — arXiv v1 submission | [2025-09-30](https://arxiv.org/abs/2509.24922) — arXiv revision | benchmark / open / check before use | United Kingdom / GDPR enforcement; English | Multi-agent deductive reasoning about GDPR enforcement facts, rules, application, common sense, and conclusions. |

### Vietnam

Vietnamese law and Vietnamese-language legal evaluation.

#### First recorded event in 2025

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [VLegal-Bench](docs/benchmarks/reasoning-education.md#vlegal-bench) | [2025-12-16](https://arxiv.org/abs/2512.14554) — arXiv v1 submission | [2026-04-17](https://arxiv.org/abs/2512.14554) — arXiv v5 revision | benchmark-suite / open / check before use | Vietnam; Vietnamese | Evaluate Vietnamese legal recognition, understanding, reasoning, interpretation, generation, and professional ethics across 22 named tasks. |

## Population not published or fixed

These entries cannot honestly be assigned to one country from the public evidence. They stay separate from both United States and international country lists.

### Evaluation population not published

Owner-controlled instruments whose public materials do not support assignment to one national legal system. Private access alone is not enough to place an entry here.

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [LegalOn Contract Review Benchmark 2026](docs/benchmarks/contracts-deal-work.md#legalon-contract-review-2026) | [2026-06-03](https://www.legalontech.com/post/the-contract-review-benchmark-2026) — Earliest verified first-party dated page; displayed as Last updated, not as launch | [2026-06-03](https://www.legalontech.com/post/the-contract-review-benchmark-2026) — Official displayed Last updated date | private-benchmark / private / check before use | Not fully disclosed; English | Review contracts against precision-critical guidelines and identify or explain material issues. |
| [Thomson Reuters CoCoBench](docs/benchmarks/agents-workflows.md#thomson-reuters-cocobench) | [2026-05-04](https://www.thomsonreuters.com/en-us/posts/innovation/why-legal-ai-needs-a-new-standard-inside-thomson-reuters-cocobench/) — Official methodology post | [2026-06-22](https://www.thomsonreuters.com/en-us/posts/innovation/the-next-phase-of-professional-ai-is-here/) — Official expansion post | private-benchmark / private / check before use | Not fully disclosed; English | Complete attorney-authored legal research, drafting, review, and multi-step reasoning tasks using supplied materials. |
| [Mercor APEX-Agents — Corporate Lawyer](docs/benchmarks/agents-workflows.md#apex-agents-corporate-law) | [2026-01-20](https://arxiv.org/abs/2601.14242) — arXiv v1 submission | [2026-08-04](https://github.com/Mercor-Intelligence/archipelago) — GitHub repository push | benchmark / open / check before use | Corporate-law practice / mixed; English | Complete realistic long-horizon corporate-law tasks across applications, files, and professional work environments. |
| [Legora Benchmark for Agentic Reasoning (BAR)](docs/benchmarks/agents-workflows.md#legora-bar) | [2025-09-09](https://legora.com/bar) — Official page's displayed original publication date | [2026-07-28](https://legora.com/bar) — Official page's displayed updated date | private-benchmark / private / check before use | Multiple; exact distribution not publicly enumerated; English | Complete multi-step legal matters using source documents and produce professional files or chat answers. |

### No fixed evaluation population

Frameworks and resource lists whose jurisdiction depends on user configuration or whose purpose is discovery rather than scoring a fixed legal population.

| Entry | First recorded public event | Latest verified event | Kind / access / label | Jurisdiction / language | What it measures |
|---|---|---|---|---|---|
| [LRAGE](docs/benchmarks/related-evaluators.md#lrage) | [2025-04-02](https://arxiv.org/abs/2504.01840) — arXiv v1 submission | [2026-07-03](https://github.com/hoorangyee/LRAGE) — GitHub repository push | evaluation-framework / open / related artifact | Global / configuration-dependent; Multiple / configuration-dependent | Configure legal RAG evaluations across retrievers, rerankers, agents, judges, and custom corpora. |
| [awesome-legal-nlp](docs/benchmarks/related-evaluators.md#awesome-legal-nlp) | [2020-09-16](https://github.com/maastrichtlawtech/awesome-legal-nlp) — GitHub repository creation | [2025-10-14](https://github.com/maastrichtlawtech/awesome-legal-nlp) — GitHub repository push | resource-list / not-applicable / related artifact | Global / mixed; Multiple | Discovery index for legal NLP datasets, models, papers, surveys, books, and events. |

## What the labels mean

Artifact type and catalog label answer different questions. Public datasets may omit a fixed scorer. Frameworks supply evaluation runners or judge logic without fixed tests. Private vendor studies report evidence from owner-controlled instruments rather than public leaderboards.

| Type | Meaning |
|---|---|
| **benchmark / benchmark suite** | Defines tasks, inputs, expected outputs, and scoring. A suite contains materially different tasks or datasets. |
| **dataset** | Supplies evaluation material but may not fix a complete scoring protocol. |
| **shared task** | Time-bounded competition with organizer-defined data, rules, and scoring. |
| **evaluation framework / protocol** | Provides evaluation code, a judge, or a study method; results depend on the tasks and versions supplied. |
| **private benchmark** | Important evaluation whose full tasks, labels, or scorer are unavailable for independent reproduction. |
| **resource list** | Discovery aid, not a benchmark result. |

A label is a curation judgment, not a model rank:

| Label | Meaning |
|---|---|
| **recommended** | Clear task contract, primary artifacts, and comparatively strong reproducibility for its class. |
| **specialist** | Useful within a narrower task, jurisdiction, language, or protocol. |
| **check before use** | Real artifact with a material judge, vendor, split, license, access, or validity issue. |
| **related artifact** | Dataset, framework, protocol, private test, or resource list. It is included so it is not mistaken for a comparable public benchmark. |

The [methodology](docs/methodology.md) explains inclusion, date provenance, and the verified fact / inference / unresolved ambiguity labels.

## Read a benchmark score

Before repeating a benchmark number, answer five questions:

1. What capability does success require, and what shortcut could produce the same score?
2. Which jurisdiction, language, source population, and time period does the sample cover?
3. What did the model receive, and what exact output did the scorer parse?
4. How are item scores aggregated? What uncertainty, subgroup, abstention, and failure counts are missing?
5. Were the questions, answers, documents, rubrics, or judge outputs exposed during training or development?

The [metric field guide](docs/metric-theory.md) gives formulas and failure modes for accuracy, F-scores, retrieval metrics, overlap metrics, LLM judges, weighted rubrics, all-pass scores, and benchmark-specific composites. It includes the detailed LawBench breakdown requested for this project.

## Files and methodology

| Need | File |
|---|---|
| Canonical source of truth | [`catalog/benchmarks.json`](catalog/benchmarks.json) |
| Flat spreadsheet view | [`catalog/benchmarks.csv`](catalog/benchmarks.csv) |
| Every GitHub, Hugging Face, paper, project, and leaderboard URL | [`catalog/resources.csv`](catalog/resources.csv) |
| URL verification result | [`catalog/resource-snapshot.json`](catalog/resource-snapshot.json) |
| Original 22-bullet audit, including the duplicated MLEB rows | [`docs/source-audit.md`](docs/source-audit.md) |
| Watchlist and deliberate non-additions | [`docs/watchlist.md`](docs/watchlist.md) |
| Formatted workbook | [`outputs/awesome-legal-benchmarks.xlsx`](outputs/awesome-legal-benchmarks.xlsx) |

Validate or regenerate the derived files:

```bash
python scripts/validate_catalog.py
python -m unittest discover -s tests -v
python scripts/generate_catalog.py --check
python scripts/check_resources.py --check-snapshot
```

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md). A proposed entry needs direct primary links, a defined evaluation contract, data provenance, access and license terms, and a concrete leakage or validity analysis. A marketing page by itself does not clear that bar.

## License

Catalog prose and structured metadata use [CC BY 4.0](LICENSE). Validation and generation code use [MIT](LICENSE-CODE). Linked datasets and repositories keep their own licenses.
