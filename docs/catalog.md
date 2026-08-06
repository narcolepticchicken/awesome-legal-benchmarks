# Legal benchmark catalog

<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->

Snapshot: **2026-08-05**. This is the compact index for all 89 canonical entries. Each name links to a full profile with the evaluation contract, direct artifacts, reproducibility notes, verified facts, inference, and unresolved ambiguity.

[Choose a benchmark](selection-guide.md) · [Read the methodology](methodology.md) · [Understand the metrics](metric-theory.md) · [Back to README](../README.md)

The index is ordered by **last verified update**, with the update basis shown below each linked date. A repository push, dataset update, paper revision, competition cycle, or official page update does not by itself prove that the benchmark data or scorer changed. A dash means no later update was verified.

## Areas

| Area | Scope | Count |
| --- | --- | ---: |
| [General legal reasoning and education](benchmarks/reasoning-education.md) | Broad suites, legal language understanding, professional exams, and jurisdiction-specific knowledge tests. | 22 |
| [Retrieval, RAG, and citation](benchmarks/retrieval-rag-citation.md) | Authority retrieval, exact-support retrieval, case similarity, citation grounding, and end-to-end legal RAG. | 28 |
| [Contracts and deal work](benchmarks/contracts-deal-work.md) | Clause extraction, provision classification, entailment, retrieval, merger agreements, and redlining. | 11 |
| [Prediction, fairness, and structured reasoning](benchmarks/prediction-fairness-rules.md) | Outcome prediction, subgroup performance, holding selection, deontic rules, and structured legal analysis. | 10 |
| [Agents and legal workflows](benchmarks/agents-workflows.md) | Tool use, process compliance, simulated legal work, and long-horizon professional tasks. | 11 |
| [Legal translation](benchmarks/translation.md) | Shared tasks and multilingual corpora with automatic and legal-expert translation scoring. | 3 |
| [Evaluators, private tests, and related resources](benchmarks/related-evaluators.md) | Artifacts worth tracking that are not comparable public benchmarks, including frameworks, private tests, and resource lists. | 4 |

## United States

Benchmarks whose evaluation population is exclusively or predominantly United States law or United States legal practice. Kind, access, and tier remain separate row-level fields.

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [Realm Legal Reasoning](benchmarks/agents-workflows.md#realm-legal-reasoning)<br>*private-benchmark · private · check before use* | [2026-08-05](https://www.micro1.ai/benchmark/realm-legal)<br>*Official page HTML last-published timestamp and expanded model-evaluation notice* | United States federal and state law; English | Produce and revise United States litigation, transactional, and compliance work products across evolving multi-stage matters. |
| [Harvey Legal Agent Benchmark (LAB)](benchmarks/agents-workflows.md#harvey-lab)<br>*benchmark · partial · check before use* | [2026-08-03](https://github.com/harveyai/harvey-labs)<br>*GitHub repository push* | United States / commercial legal practice, mixed practice areas; English | Complete long-horizon legal matters using files, research, analysis, drafting, and validation tools. |
| [Vals Legal Research Benchmark](benchmarks/retrieval-rag-citation.md#vals-legal-research-bench)<br>*private-benchmark · partial · check before use* | [2026-08-03](https://www.vals.ai/benchmarks/legal_research)<br>*Official benchmark page update date* | United States; English | Research US legal questions and produce answers satisfying lawyer-authored substantive and citation criteria. |
| [prinzbench](benchmarks/related-evaluators.md#prinzbench)<br>*private-benchmark · private · related artifact* | [2026-07-18](https://github.com/prinz-ai/prinzbench)<br>*GitHub repository push* | United States; English | Answer obscure US legal-research and general information-search questions. |
| [Vaquill Open Legal-Answer Benchmark](benchmarks/retrieval-rag-citation.md#open-legal-answer-benchmark)<br>*benchmark · open · check before use* | [2026-07-18](https://github.com/Vaquill-AI/open-legal-answer-benchmark)<br>*GitHub repository push* | United States; English | Produce current US legal answers with relevant, supported, and correctly ranged citations. |
| [Legal Phantom Citation](benchmarks/retrieval-rag-citation.md#legal-phantom-citation)<br>*benchmark · open · specialist* | [2026-07-06](https://huggingface.co/datasets/ai-law-society-lab/Legal_Phantom_Citation)<br>*Hugging Face dataset update* | United States federal appellate courts, 13 circuits; English | Identify hallucinated legal citations and affected spans in federal appellate brief text. |
| [RedlineBench](benchmarks/contracts-deal-work.md#redlinebench)<br>*benchmark · open · check before use* | [2026-06-26](https://github.com/crosbylegal/redline-bench)<br>*GitHub repository push* | United States / commercial contracting; English | Negotiate commercial contracts over four turns by producing native Word tracked changes and comments. |
| [GC AI In-House Legal Bench](benchmarks/agents-workflows.md#gc-ai-in-house-legal-bench)<br>*private-benchmark · partial · check before use* | [2026-06-05](https://gc.ai/blog/in-house-legal-bench-evaluating-ai-assistants-for-in-house-legal-work)<br>*Official displayed update date* | Primarily United States; exact distribution not fully published; English | Complete common in-house legal drafting, analysis, research, strategy, extraction, regulatory, and checklist tasks. |
| [DeonticBench](benchmarks/prediction-fairness-rules.md#deonticbench)<br>*benchmark-suite · open · recommended* | [2026-06-04](https://huggingface.co/datasets/gydou/DeonticBench)<br>*Hugging Face dataset update* | United States federal tax, United States immigration, United States state housing, Airline policies; English, Prolog | Reason about obligations, permissions, prohibitions, eligibility, and amounts under long legal/policy rules, directly or through executable Prolog. |
| [LegalCiteBench](benchmarks/retrieval-rag-citation.md#legalcitebench)<br>*benchmark-suite · open · recommended* | [2026-05-11](https://arxiv.org/abs/2605.10186)<br>*arXiv v1 submission* | United States federal appellate courts; English | Retrieve, complete, verify, and abstain on legal citations in US appellate text. |
| [LegalBench](benchmarks/reasoning-education.md#legalbench)<br>*benchmark-suite · open · recommended* | [2026-03-30](https://github.com/HazyResearch/legalbench)<br>*GitHub repository push* | United States, mixed/common-law; English | Task-specific legal reasoning across classification, extraction, question answering, and generation. |
| [Harvey BigLaw Bench](benchmarks/agents-workflows.md#harvey-biglaw-bench)<br>*private-benchmark · partial · check before use* | [2026-03-17](https://github.com/harveyai/biglaw-bench)<br>*GitHub repository push* | Primarily United States; later extensions described broader coverage; English | Complete transactional and litigation research, drafting, retrieval, and long-document tasks. |
| [PILOT-Bench](benchmarks/reasoning-education.md#pilot-bench)<br>*benchmark-suite · open · specialist* | [2026-03-10](https://huggingface.co/datasets/Yehoon/pilot-bench)<br>*Hugging Face dataset and GitHub repository update* | United States Patent Trial and Appeal Board; English | Classify contested issues, Board authorities, and outcomes in US patent appeals. |
| [OpenExempt](benchmarks/prediction-fairness-rules.md#openexempt)<br>*benchmark-suite · open · specialist* | [2026-01-21](https://huggingface.co/datasets/SergioServantez/OpenExempt)<br>*Hugging Face dataset update* | United States federal bankruptcy law; English | Apply structured US bankruptcy exemption rules and remain robust under controlled perturbations. |
| [CourtReasoner](benchmarks/agents-workflows.md#courtreasoner)<br>*benchmark · open · check before use* | [2025-11](https://aclanthology.org/2025.emnlp-main.1787/)<br>*EMNLP 2025 publication* | United States appellate law; English | Generate appellate-style judicial reasoning that identifies constraints, uses relevant authorities, and supports a valid argument under controlled factual changes. |
| [Atticus Clause Retrieval Dataset](benchmarks/contracts-deal-work.md#acord)<br>*benchmark · open · recommended* | [2025-09-21](https://arxiv.org/abs/2501.06582)<br>*arXiv revision* | United States / commercial contracts; English | Rank precedent contract clauses for an attorney-written drafting need. |
| [LaborBench](benchmarks/retrieval-rag-citation.md#laborbench)<br>*benchmark · open · specialist* | [2025-08-26](https://arxiv.org/abs/2508.19365)<br>*arXiv v1 submission after the dataset release* | United States: 50 states, District of Columbia, Puerto Rico, and U.S. Virgin Islands; English | Extract and answer state-specific unemployment-insurance law questions from statutes and regulations. |
| [LegalBench-RAG](benchmarks/retrieval-rag-citation.md#legalbench-rag)<br>*benchmark · open · recommended* | [2025-05-30](https://github.com/zeroentropy-ai/legalbenchrag)<br>*GitHub repository push* | United States, mixed contracts and policies; English | Retrieve exact supporting spans from long legal and policy documents. |
| [CLERC](benchmarks/retrieval-rag-citation.md#clerc)<br>*benchmark · open · specialist* | [2025-01-28](https://github.com/bohanhou14/CLERC)<br>*GitHub repository push* | United States; English | Retrieve US case-law evidence and generate citation-grounded legal text. |
| [Hallucination-Free? Legal Research Tool Study](benchmarks/retrieval-rag-citation.md#reglab-legal-rag-hallucinations)<br>*evaluation-protocol · partial · recommended* | [2024-11-14](https://huggingface.co/datasets/reglab/legal_rag_hallucinations)<br>*Hugging Face dataset update* | United States; English | Return correct, grounded, responsive legal research answers without false authority or unsupported propositions. |
| [LegalLens](benchmarks/prediction-fairness-rules.md#legal-lens)<br>*benchmark-suite · partial · check before use* | [2024-10-15](https://arxiv.org/abs/2410.12064)<br>*NLLP shared-task paper arXiv v1 submission* | United States / common-law class-action context; English | Extract potential legal-violation entities from non-legal text and infer whether a violation statement entails a harmed group or legal ground. |
| [Large Legal Fictions](benchmarks/retrieval-rag-citation.md#reglab-legal-hallucinations)<br>*benchmark-suite · partial · specialist* | [2024-06-26](https://github.com/reglab/legal_hallucinations)<br>*GitHub repository push* | United States federal courts; English | Answer verifiable closed-form questions about US federal cases without inventing cases, citations, holdings, or treatment. |
| [Contract Understanding Atticus Dataset](benchmarks/contracts-deal-work.md#cuad)<br>*benchmark · open · recommended* | [2024-05-23](https://huggingface.co/datasets/theatticusproject/cuad-qa)<br>*Hugging Face dataset update* | United States / SEC filings; English | Locate 41 categories of commercially important clauses in long contracts. |
| [ClassActionPrediction](benchmarks/prediction-fairness-rules.md#class-action-prediction)<br>*benchmark · open · check before use* | [2024-01-24](https://huggingface.co/datasets/darrow-ai/USClassActions)<br>*Hugging Face dataset update* | United States federal class actions; English | Predict whether a United States federal class-action complaint will produce a plaintiff win or loss. |
| [Merger Agreement Understanding Dataset](benchmarks/contracts-deal-work.md#maud)<br>*benchmark · open · recommended* | [2023-11-24](https://arxiv.org/abs/2301.00876)<br>*arXiv revision* | United States / public-company M&A; English | Answer fine-grained questions about merger-agreement provisions. |
| [ContractNLI](benchmarks/contracts-deal-work.md#contractnli)<br>*benchmark · open · recommended* | [2022-02-11](https://github.com/stanfordnlp/contract-nli)<br>*GitHub repository push* | Commercial NDAs / primarily United States practice; English | Determine whether a non-disclosure agreement entails, contradicts, or does not mention a fixed legal hypothesis and identify supporting evidence. |
| [CaseHOLD](benchmarks/prediction-fairness-rules.md#casehold)<br>*benchmark · open · specialist* | [2021-07-06](https://arxiv.org/abs/2104.08671)<br>*arXiv revision* | United States; English | Select the correct holding that completes an excerpt from a US judicial opinion. |
| [LEDGAR](benchmarks/contracts-deal-work.md#ledgar)<br>*dataset · open · specialist* | [2020-10-19](https://github.com/dtuggener/LEDGAR_provision_classification)<br>*Original GitHub repository push* | United States / SEC filings; English | Classify contract provisions into clause/topic labels. |
| [TREC Legal Track](benchmarks/retrieval-rag-citation.md#trec-legal-track)<br>*shared-task · partial · specialist* | [2011](https://trec.nist.gov/data/legal11.html)<br>*Final official TREC Legal Track edition* | United States civil litigation / e-discovery; English | Find documents responsive to civil-litigation production requests while minimizing review burden. |
| [ContractEval](benchmarks/contracts-deal-work.md#contracteval)<br>*evaluation-protocol · open · related artifact* | — | United States / SEC filings; English | Evaluate long-context LLM clause-risk extraction on the public CUAD test set. |
| [Ivo Contract Review Comparison](benchmarks/contracts-deal-work.md#ivo-contract-review-study)<br>*evaluation-protocol · private · check before use* | — | United States commercial contracting; English | Review and redline real contracts while preserving formatting and exercising lawyer-like judgment. |
| [RegLab Reasoning-Focused Legal Retrieval Benchmark](benchmarks/retrieval-rag-citation.md#reglab-reasoning-focused-retrieval)<br>*benchmark-suite · open · recommended* | — | United States; English | Retrieve controlling text for legal questions whose answer has low lexical overlap with the relevant source. |

## Multi-jurisdiction and supranational

Fixed artifacts designed around more than one national legal system, a supranational legal order, or an official multi-country competition identity. Inclusion here is descriptive, not a claim of prestige or equal country coverage.

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [legalbenchmarks.ai](benchmarks/contracts-deal-work.md#legalbenchmarks-ai)<br>*private-benchmark · private · check before use* | [2026-07](https://www.legalbenchmarks.ai/leaderboard)<br>*Official leaderboard's displayed update month* | United States, United Kingdom, English-language commercial practice; English | Draft contract work products and extract information from native legal documents. |
| [Professional Reasoning Benchmark (PRBench)](benchmarks/reasoning-education.md#prbench)<br>*benchmark · open · check before use* | [2026-06-24](https://huggingface.co/datasets/ScaleAI/PRBench)<br>*Hugging Face dataset update* | 114 countries, 47 United States jurisdictions; English | Produce open-ended professional legal analysis that satisfies granular expert-authored criteria. |
| [DLawBench](benchmarks/agents-workflows.md#dlawbench)<br>*benchmark · open · recommended* | [2026-06-11](https://arxiv.org/abs/2606.13931)<br>*arXiv v1 submission* | China, United States; Chinese, English | Conduct multi-turn legal consultations and turn elicited facts into a reasoned legal memorandum. |
| [Competition on Legal Information Extraction/Entailment](benchmarks/retrieval-rag-citation.md#coliee)<br>*shared-task · gated · recommended* | [2026-06](https://coliee.org/COLIEE2026/program)<br>*COLIEE 2026 workshop program* | Canada, Japan; English, Japanese | Retrieve and recognize entailment among Canadian cases and Japanese civil-code provisions. |
| [LEXam](benchmarks/reasoning-education.md#lexam)<br>*benchmark · open · recommended* | [2026-05-21](https://huggingface.co/datasets/LEXam-Benchmark/LEXam)<br>*Hugging Face dataset update* | Germany, United States / English-language courses, mixed law-school curricula; English, German | Answer bilingual law-school multiple-choice and open-answer examination questions. |
| [LEXTREME](benchmarks/reasoning-education.md#lextreme)<br>*benchmark-suite · open · recommended* | [2026-05-20](https://huggingface.co/datasets/joelniklaus/lextreme)<br>*Hugging Face dataset update* | European Union, Council of Europe, European national jurisdictions; 24 European languages | Multilingual European legal classification and named-entity recognition across 24 languages. |
| [Massive Legal Embedding Benchmark](benchmarks/retrieval-rag-citation.md#mleb)<br>*benchmark-suite · open · specialist* | [2026-02-24](https://github.com/isaacus-dev/mleb)<br>*GitHub repository push* | United States, United Kingdom, European Union, Australia, Ireland, Singapore; English | Legal embedding quality across retrieval, retrieval-augmented QA, and zero-shot classification tasks. |
| [LexGLUE](benchmarks/reasoning-education.md#lexglue)<br>*benchmark-suite · open · recommended* | [2025-07-23](https://github.com/coastalcph/lex-glue)<br>*GitHub repository push* | Council of Europe, European Union, United States, mixed contracts/terms; English | Standardized English legal language understanding across seven classification and judgment tasks. |
| [LexSumm](benchmarks/reasoning-education.md#lexsumm)<br>*benchmark-suite · open · check before use* | [2024-11-19](https://github.com/TUMLegalTech/LexSumm-LexT5)<br>*Canonical GitHub repository push* | United States, United Kingdom, European Union, India, Multi-jurisdictional legal sources; English | Generate abstractive summaries of legislation, cases, and government/legal reports across eight public datasets. |
| [MoZIP](benchmarks/reasoning-education.md#mozip)<br>*benchmark-suite · open · specialist* | [2024-08-20](https://github.com/AI-for-Science/MoZi)<br>*Canonical GitHub repository push* | International and mixed national intellectual-property sources, WIPO patent corpus; Chinese, English, German, Spanish, Japanese, Korean, Portuguese, French, Russian | Answer multilingual intellectual-property questions and match patent abstracts to the most similar patent. |
| [FairLex](benchmarks/prediction-fairness-rules.md#fairlex)<br>*benchmark-suite · open · recommended* | [2023-07-27](https://huggingface.co/datasets/coastalcph/fairlex)<br>*Hugging Face dataset update* | Council of Europe, United States, Switzerland, China; English, German, French, Italian, Chinese | Evaluate legal prediction performance and group robustness across sensitive or legally salient subpopulations. |

## International by country

Countries are alphabetical; entries within each country are grouped by last-verified-update year, newest year first, and then newest-first within that year.

### Australia

Australian law; the full evaluation population remains visible in each row.

#### Updated in 2026

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [Legal RAG Bench](benchmarks/retrieval-rag-citation.md#legal-rag-bench)<br>*benchmark · open · check before use* | [2026-03-08](https://huggingface.co/datasets/isaacus/legal-rag-bench)<br>*Hugging Face dataset update* | Victoria, Australia / criminal law and procedure; English | Evaluate an end-to-end legal RAG pipeline and attribute errors to retrieval versus generation. |

### Belgium

Belgian law and Belgian legal-language evaluation.

#### Updated in 2026

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [bLLeQA](benchmarks/retrieval-rag-citation.md#blleqa)<br>*benchmark-suite · gated · specialist* | [2026-07-03](https://aclanthology.org/2026.knowfm-1.4.pdf)<br>*KnowFM 2026 publication date* | Belgium, France and Netherlands source alignment described by the release; French, Dutch | Retrieve Belgian statutory support and answer grounded legal questions in French and Dutch, including refusal when evidence is insufficient. |

#### Updated in 2024

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [LLeQA](benchmarks/retrieval-rag-citation.md#lleqa)<br>*benchmark · gated · specialist* | [2024-09-03](https://huggingface.co/datasets/maastrichtlawtech/lleqa)<br>*Hugging Face dataset update* | Belgium; French | Retrieve Belgian legal authorities and generate long-form answers to practitioner-style questions. |
| [Belgian Statutory Article Retrieval Dataset](benchmarks/retrieval-rag-citation.md#bsard)<br>*benchmark · open · recommended* | [2024-05-31](https://huggingface.co/datasets/maastrichtlawtech/bsard)<br>*Hugging Face dataset update* | Belgium; French | Retrieve Belgian statutory articles relevant to a legal question. |

### Brazil

Brazilian law and Brazilian professional legal-writing evaluation.

#### Updated in 2026

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [OAB-Bench](benchmarks/reasoning-education.md#oab-bench)<br>*benchmark · open · specialist* | [2026-06-01](https://huggingface.co/datasets/maritaca-ai/oab-bench)<br>*Hugging Face dataset update for the expanded release* | Brazil; Portuguese (Brazilian) | Draft Brazilian legal documents and answer discursive professional-exam questions under official examiner guidelines. |

### Canada

Canadian law; COLIEE is listed separately as a Canada/Japan competition identity.

#### Updated in 2026

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [CanLegalRAGBench](benchmarks/retrieval-rag-citation.md#canlegalragbench)<br>*benchmark · open · specialist* | [2026-07-20](https://github.com/NLP-UBC/CanLegalRAGBench)<br>*GitHub repository push* | Canada, Ontario, British Columbia, Alberta, other Canadian provinces/federal courts; English, some French passages | Retrieve Canadian case law for realistic layperson and legal-professional queries and generate grounded answers. |
| [Vals CaseLaw v2](benchmarks/retrieval-rag-citation.md#vals-caselaw-v2)<br>*private-benchmark · private · related artifact* | [2026-05-04](https://www.vals.ai/benchmarks/case_law_v2)<br>*Official benchmark page update date* | Canada; English | Answer Canadian case-law questions with correct, relevant, well-supported legal analysis. |

### China

Chinese law and Chinese-language legal evaluation; artifacts designed around China and another national legal system are listed in the multi-jurisdiction section.

#### Updated in 2026

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [PLawBench](benchmarks/reasoning-education.md#plawbench)<br>*benchmark-suite · partial · check before use* | [2026-07](https://aclanthology.org/2026.acl-long.458/)<br>*ACL 2026 publication* | China; Chinese | Answer Chinese legal consultations, analyze practical cases, and draft legal documents. |
| [MSLR-Bench](benchmarks/prediction-fairness-rules.md#mslr)<br>*benchmark · open · check before use* | [2026-06-29](https://github.com/yuwenhan07/MSLR-Bench)<br>*GitHub repository push* | China; Chinese | Extract structured facts and produce IRAC-style reasoning for Chinese insider-trading cases. |
| [LexGenius](benchmarks/reasoning-education.md#lexgenius)<br>*benchmark-suite · open · recommended* | [2026-04-16](https://arxiv.org/abs/2512.04578)<br>*arXiv v3 revision* | China; Chinese | Answer broad Chinese legal knowledge and reasoning questions across seven dimensions and eleven tasks. |
| [LegalAgentBench](benchmarks/agents-workflows.md#legalagentbench)<br>*benchmark · open · specialist* | [2026-04-10](https://github.com/CSHaitao/LegalAgentBench)<br>*GitHub repository push* | China; Chinese | Chinese legal tool use, multi-hop information gathering, and legal writing. |
| [Ready Jurist One (J1Bench)](benchmarks/agents-workflows.md#ready-jurist-one)<br>*benchmark · open · specialist* | [2026-04-07](https://github.com/FudanDISC/J1Bench)<br>*GitHub repository push* | China; Chinese | Operate interactively in Chinese legal consultation, drafting, civil-court, and criminal-court environments. |
| [LegalEval-Q](benchmarks/related-evaluators.md#legaleval-q)<br>*evaluation-framework · open · related artifact* | [2026-02-26](https://github.com/lyxx3rd/LegalEval-Q)<br>*GitHub repository push* | China; Chinese | Predict the quality of Chinese LLM-generated legal answers. |

#### Updated in 2025

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [JuDGE](benchmarks/reasoning-education.md#judge)<br>*benchmark · open · specialist* | [2025-08-07](https://github.com/oneal2000/JuDGE)<br>*GitHub repository push* | China; Chinese | Generate a complete Chinese criminal judgment document from a factual description. |
| [MUSER](benchmarks/retrieval-rag-citation.md#muser)<br>*benchmark · open · specialist* | [2025-07-25](https://github.com/THUlawtech/MUSER)<br>*GitHub repository push* | China; Chinese | Retrieve similar Chinese civil cases using multiple legally relevant views of case similarity. |
| [STARD](benchmarks/retrieval-rag-citation.md#stard)<br>*benchmark · open · specialist* | [2025-04-24](https://github.com/oneal2000/STARD)<br>*Last verified GitHub repository push affecting the benchmark artifact* | China; Chinese | Retrieve all Chinese statutory articles relevant to an informal real-world legal consultation query. |
| [LawBench](benchmarks/reasoning-education.md#lawbench)<br>*benchmark-suite · open · recommended* | [2025-03-07](https://huggingface.co/datasets/doolayer/LawBench)<br>*Hugging Face dataset update* | China; Chinese | Chinese legal memorization, understanding, and application across 20 tasks. |
| [LexRAG](benchmarks/retrieval-rag-citation.md#lexrag)<br>*benchmark · open · check before use* | [2025-03-03](https://github.com/CSHaitao/LexRAG)<br>*GitHub repository push* | China; Chinese | Retrieve relevant Chinese legal articles and answer five-turn legal consultation dialogues with grounded responses. |

#### Updated in 2024

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [LeCaRDv2](benchmarks/retrieval-rag-citation.md#lecardv2)<br>*benchmark · open · recommended* | [2024-12-29](https://github.com/THUIR/LeCaRDv2)<br>*GitHub repository push* | China; Chinese | Retrieve legally similar Chinese criminal cases using graded relevance across characterization, penalty, and procedure. |
| [LexEval](benchmarks/reasoning-education.md#lexeval)<br>*benchmark-suite · open · specialist* | [2024-11-26](https://arxiv.org/abs/2409.20288)<br>*arXiv revision* | China; Chinese | Chinese legal knowledge, inference, generation, discrimination, and ethics across 23 tasks. |

### Council of Europe

Evaluation tied to the European Convention system rather than one national jurisdiction.

#### Updated in 2025

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [ECtHR Tasks A/B](benchmarks/prediction-fairness-rules.md#ecthr)<br>*benchmark · open · recommended* | [2025-07-23](https://github.com/coastalcph/lex-glue)<br>*Canonical LexGLUE repository push* | European Court of Human Rights / Council of Europe; English | Predict European Convention articles alleged (Task A) or found violated (Task B) from case facts. |

### Germany

German law and German-language legal evaluation.

#### Updated in 2026

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [AGB-DE](benchmarks/contracts-deal-work.md#agb-de)<br>*benchmark · open · specialist* | [2026-07-02](https://github.com/DaBr01/AGB-DE)<br>*GitHub repository push; latest change was citation metadata rather than benchmark data* | Germany; German | Detect potentially void clauses in German consumer standard terms and conditions. |

#### Updated in 2024

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [GerDaLIR](benchmarks/retrieval-rag-citation.md#gerdalir)<br>*benchmark · open · specialist* | [2024-02-26](https://github.com/lavis-nlp/GerDaLIR)<br>*Last verified GitHub repository push affecting the benchmark artifact* | Germany; German | Retrieve German case decisions cited by a passage expressing a legal statement or line of argument. |

### India

Indian law and Indian legal-language evaluation.

#### Updated in 2026

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [PredEx](benchmarks/prediction-fairness-rules.md#predex)<br>*benchmark · open · check before use* | [2026-06-03](https://github.com/ShubhamKumarNigam/PredEx)<br>*GitHub repository push; latest change was citation metadata rather than benchmark data* | India; English | Predict whether an Indian Supreme Court appeal or petition is accepted or rejected and extract supporting explanatory text. |
| [ILSIC](benchmarks/retrieval-rag-citation.md#ilsic)<br>*dataset · partial · specialist* | [2026-02-03](https://github.com/Law-AI/ilsic)<br>*GitHub repository push* | India; English, Indian legal-query language | Identify Indian statutes relevant to layperson and court-derived legal queries. |

#### Updated in 2025

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [Multilingual Indian Legal Parallel Corpus](benchmarks/translation.md#milpac)<br>*benchmark-suite · open · recommended* | [2025-07-13](https://github.com/Law-AI/MILPaC)<br>*GitHub repository push* | India; English, Hindi, Bengali, Marathi, Tamil, Gujarati, Telugu, Malayalam, Punjabi, Odia | Translate verified Indian legal text from English into nine Indian languages. |
| [IL-TUR](benchmarks/reasoning-education.md#il-tur)<br>*benchmark-suite · open · recommended* | [2025-06-07](https://github.com/Exploration-Lab/IL-TUR)<br>*GitHub repository push* | India; English, Hindi, Bengali, Gujarati, Marathi, Malayalam, Odia, Punjabi, Tamil, Telugu | Indian legal named entities, rhetorical roles, judgment/explanation, bail, statute identification, precedent retrieval, summarization, and translation. |

#### Updated in 2020

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [AILA 2019](benchmarks/retrieval-rag-citation.md#aila-2019)<br>*shared-task · open · specialist* | [2020-10-03](https://zenodo.org/records/4063986)<br>*Zenodo dataset record modification* | India; English | Rank relevant Indian Supreme Court precedents and statutory sections for a factual legal scenario. |

#### No verified update

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [JUST-NLP 2025 Legal MT Shared Task](benchmarks/translation.md#just-nlp-2025-legal-mt)<br>*shared-task · gated · specialist* | — | India; English, Hindi | Translate legal text from English to Hindi. |

### Italy

Italian law.

#### Updated in 2026

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [JuriFindIT](benchmarks/retrieval-rag-citation.md#jurifindit)<br>*benchmark · open · specialist* | [2026-03](https://aclanthology.org/2026.findings-eacl.221/)<br>*Findings of EACL 2026 publication* | Italy, European Union materials within the corpus; Italian | Retrieve Italian statutory articles relevant to natural-language legal questions. |

### Morocco

Moroccan law and Moroccan Arabic legal evaluation.

#### Updated in 2026

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [MizanQA](benchmarks/reasoning-education.md#mizanqa)<br>*benchmark · open · check before use* | [2026-03](https://aclanthology.org/2026.eacl-industry.10/)<br>*EACL 2026 Industry Track publication* | Morocco; Arabic (Modern Standard Arabic with Moroccan legal usage) | Answer expert-verified multiple-choice questions about Moroccan law and associated legal traditions. |

### Portugal

Portuguese law and European Portuguese legal evaluation.

#### Updated in 2026

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [LegalBench.PT](benchmarks/reasoning-education.md#legalbench-pt)<br>*benchmark · open · check before use* | [2026-05-06](https://huggingface.co/datasets/BeatrizCanaverde/LegalBench.PT)<br>*Hugging Face dataset update* | Portugal; Portuguese (European) | Answer European Portuguese questions testing knowledge and application of Portuguese law across 31 legal fields. |

### Romania

Romanian law.

#### Updated in 2026

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [RoD-TAL](benchmarks/retrieval-rag-citation.md#rod-tal)<br>*benchmark-suite · gated · specialist* | [2026-04-30](https://huggingface.co/datasets/GRAI-UNSTPB/RoD-TAL)<br>*Hugging Face dataset update* | Romania; Romanian | Answer Romanian driving-law questions and retrieve governing law or traffic signs from text and images. |

### Saudi Arabia

Saudi law; translated or broader Arab-jurisdiction material remains disclosed in the row.

#### Updated in 2025

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [Arabic Legal Argument Reasoning Benchmark (ALARB)](benchmarks/reasoning-education.md#alarb)<br>*dataset · open · check before use* | [2025-10-15](https://huggingface.co/datasets/THIQAH-RD/ALARB)<br>*Hugging Face dataset update* | Saudi Arabia; Arabic | Reason over Saudi commercial-law cases, complete arguments, and identify governing statutory articles. |
| [ArabLegalEval](benchmarks/reasoning-education.md#arablegaleval)<br>*benchmark-suite · open · check before use* | [2025-05-21](https://github.com/Thiqah/ArabLegalEval)<br>*GitHub repository push* | Saudi Arabia, Arab jurisdictions / translated sources; Arabic, English | Arabic legal knowledge, classification, question answering, and translation, with substantial Saudi-law coverage. |

### South Korea

South Korean law.

#### Updated in 2026

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [Korean Canonical Legal Benchmark](benchmarks/reasoning-education.md#kcl)<br>*benchmark-suite · open · recommended* | [2026-01-23](https://github.com/lbox-kr/kcl)<br>*GitHub repository push* | South Korea; Korean | Answer Korean bar-exam MCQs and essays with question-aligned supporting precedents. |

#### Updated in 2025

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [KBL](benchmarks/reasoning-education.md#kbl)<br>*benchmark-suite · open · specialist* | [2025-05-19](https://huggingface.co/datasets/lbox/kbl)<br>*Hugging Face benchmark dataset update* | South Korea; Korean | Answer Korean legal knowledge, legal reasoning, and bar-examination multiple-choice questions with or without retrieved statutes and precedents. |

### Switzerland

Swiss law and Swiss legal languages.

#### Updated in 2025

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [SwiLTra-Bench](benchmarks/translation.md#swiltra-bench)<br>*benchmark-suite · open · recommended* | [2025-05-30](https://arxiv.org/abs/2503.01372)<br>*arXiv revision* | Switzerland; German, French, Italian, Romansh, English | Translate Swiss laws, court headnotes, and press releases among official Swiss languages and English. |

### United Kingdom

United Kingdom law and regulatory enforcement.

#### Updated in 2025

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [MASLegalBench](benchmarks/prediction-fairness-rules.md#maslegalbench)<br>*benchmark · open · check before use* | [2025-09-30](https://arxiv.org/abs/2509.24922)<br>*arXiv revision* | United Kingdom / GDPR enforcement; English | Multi-agent deductive reasoning about GDPR enforcement facts, rules, application, common sense, and conclusions. |

### Vietnam

Vietnamese law and Vietnamese-language legal evaluation.

#### Updated in 2026

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [VLegal-Bench](benchmarks/reasoning-education.md#vlegal-bench)<br>*benchmark-suite · open · check before use* | [2026-04-17](https://arxiv.org/abs/2512.14554)<br>*arXiv v5 revision* | Vietnam; Vietnamese | Evaluate Vietnamese legal recognition, understanding, reasoning, interpretation, generation, and professional ethics across 22 named tasks. |

## Population not published or fixed

### Evaluation population not published

Owner-controlled instruments whose public materials do not support assignment to one national legal system. Private access alone is not enough to place an entry here.

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [Mercor APEX-Agents — Corporate Lawyer](benchmarks/agents-workflows.md#apex-agents-corporate-law)<br>*benchmark · open · check before use* | [2026-08-04](https://github.com/Mercor-Intelligence/archipelago)<br>*GitHub repository push* | Corporate-law practice / mixed; English | Complete realistic long-horizon corporate-law tasks across applications, files, and professional work environments. |
| [Legora Benchmark for Agentic Reasoning (BAR)](benchmarks/agents-workflows.md#legora-bar)<br>*private-benchmark · private · check before use* | [2026-07-28](https://legora.com/bar)<br>*Official page's displayed updated date* | Multiple; exact distribution not publicly enumerated; English | Complete multi-step legal matters using source documents and produce professional files or chat answers. |
| [Thomson Reuters CoCoBench](benchmarks/agents-workflows.md#thomson-reuters-cocobench)<br>*private-benchmark · private · check before use* | [2026-06-22](https://www.thomsonreuters.com/en-us/posts/innovation/the-next-phase-of-professional-ai-is-here/)<br>*Official expansion post* | Not fully disclosed; English | Complete attorney-authored legal research, drafting, review, and multi-step reasoning tasks using supplied materials. |
| [LegalOn Contract Review Benchmark 2026](benchmarks/contracts-deal-work.md#legalon-contract-review-2026)<br>*private-benchmark · private · check before use* | [2026-06-03](https://www.legalontech.com/post/the-contract-review-benchmark-2026)<br>*Official displayed Last updated date* | Not fully disclosed; English | Review contracts against precision-critical guidelines and identify or explain material issues. |

### No fixed evaluation population

Frameworks and resource lists whose jurisdiction depends on user configuration or whose purpose is discovery rather than scoring a fixed legal population.

| Benchmark | Last verified update | Coverage | What it measures |
| --- | --- | --- | --- |
| [LRAGE](benchmarks/related-evaluators.md#lrage)<br>*evaluation-framework · open · related artifact* | [2026-07-03](https://github.com/hoorangyee/LRAGE)<br>*GitHub repository push* | Global / configuration-dependent; Multiple / configuration-dependent | Configure legal RAG evaluations across retrievers, rerankers, agents, judges, and custom corpora. |
| [awesome-legal-nlp](benchmarks/related-evaluators.md#awesome-legal-nlp)<br>*resource-list · not-applicable · related artifact* | [2025-10-14](https://github.com/maastrichtlawtech/awesome-legal-nlp)<br>*GitHub repository push* | Global / mixed; Multiple | Discovery index for legal NLP datasets, models, papers, surveys, books, and events. |
