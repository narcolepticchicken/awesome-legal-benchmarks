# Legal benchmark catalog

<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->

Snapshot: **2026-08-03**. This is the compact index for all 45 canonical entries. Each name links to a full profile with the evaluation contract, direct artifacts, reproducibility notes, verified facts, inference, and unresolved ambiguity.

[Choose a benchmark](selection-guide.md) · [Read the methodology](methodology.md) · [Understand the metrics](metric-theory.md) · [Back to README](../README.md)

## Areas

| Area | Scope | Entries |
|---|---|---:|
| [General legal reasoning and education](benchmarks/reasoning-education.md) | Broad suites, legal language understanding, professional exams, and jurisdiction-specific knowledge tests. | 9 |
| [Retrieval, RAG, and citation](benchmarks/retrieval-rag-citation.md) | Authority retrieval, exact-support retrieval, case similarity, citation grounding, and end-to-end legal RAG. | 10 |
| [Contracts and deal work](benchmarks/contracts-deal-work.md) | Clause extraction, provision classification, entailment, retrieval, merger agreements, and redlining. | 7 |
| [Prediction, fairness, and structured reasoning](benchmarks/prediction-fairness-rules.md) | Outcome prediction, subgroup performance, holding selection, deontic rules, and structured legal analysis. | 7 |
| [Agents and legal workflows](benchmarks/agents-workflows.md) | Tool use, process compliance, simulated legal work, and long-horizon professional tasks. | 4 |
| [Legal translation](benchmarks/translation.md) | Shared tasks and multilingual corpora with automatic and legal-expert translation scoring. | 3 |
| [Evaluators, private tests, and related resources](benchmarks/related-evaluators.md) | Artifacts worth tracking that are not comparable public benchmarks, including frameworks, private tests, and resource lists. | 5 |

## All entries

The `kind` field distinguishes benchmarks, datasets, shared tasks, frameworks, protocols, private tests, and resource lists. The `label` field is the catalog's reproducibility and usefulness judgment. They answer different questions.

### General legal reasoning and education

Broad suites, legal language understanding, professional exams, and jurisdiction-specific knowledge tests.

| Entry | Kind | Label | Jurisdiction / language | Measures |
|---|---|---|---|---|
| [LegalBench](benchmarks/reasoning-education.md#legalbench) | benchmark-suite | recommended | United States, mixed/common-law; English | Task-specific legal reasoning across classification, extraction, question answering, and generation. |
| [LawBench](benchmarks/reasoning-education.md#lawbench) | benchmark-suite | recommended | China; Chinese | Chinese legal memorization, understanding, and application across 20 tasks. |
| [LexGLUE](benchmarks/reasoning-education.md#lexglue) | benchmark-suite | recommended | Council of Europe, European Union, United States, mixed contracts/terms; English | Standardized English legal language understanding across seven classification and judgment tasks. |
| [LEXTREME](benchmarks/reasoning-education.md#lextreme) | benchmark-suite | recommended | European Union, Council of Europe, European national jurisdictions; 24 European languages | Multilingual European legal classification and named-entity recognition across 24 languages. |
| [LEXam](benchmarks/reasoning-education.md#lexam) | benchmark | recommended | Germany, United States / English-language courses, mixed law-school curricula; English, German | Answer bilingual law-school multiple-choice and open-answer examination questions. |
| [LexEval](benchmarks/reasoning-education.md#lexeval) | benchmark-suite | specialist | China; Chinese | Chinese legal knowledge, inference, generation, discrimination, and ethics across 23 tasks. |
| [ArabLegalEval](benchmarks/reasoning-education.md#arablegaleval) | benchmark-suite | check before use | Saudi Arabia, Arab jurisdictions / translated sources; Arabic, English | Arabic legal knowledge, classification, question answering, and translation, with substantial Saudi-law coverage. |
| [IL-TUR](benchmarks/reasoning-education.md#il-tur) | benchmark-suite | recommended | India; English, Hindi, Bengali, Gujarati, Marathi, Malayalam, Odia, Punjabi, Tamil, Telugu | Indian legal named entities, rhetorical roles, judgment/explanation, bail, statute identification, precedent retrieval, summarization, and translation. |
| [Korean Canonical Legal Benchmark](benchmarks/reasoning-education.md#kcl) | benchmark-suite | recommended | South Korea; Korean | Answer Korean bar-exam MCQs and essays with question-aligned supporting precedents. |

### Retrieval, RAG, and citation

Authority retrieval, exact-support retrieval, case similarity, citation grounding, and end-to-end legal RAG.

| Entry | Kind | Label | Jurisdiction / language | Measures |
|---|---|---|---|---|
| [Massive Legal Embedding Benchmark](benchmarks/retrieval-rag-citation.md#mleb) | benchmark-suite | specialist | United States, United Kingdom, European Union, Australia, Ireland, Singapore; English | Legal embedding quality across retrieval, retrieval-augmented QA, and zero-shot classification tasks. |
| [LegalBench-RAG](benchmarks/retrieval-rag-citation.md#legalbench-rag) | benchmark | recommended | United States, mixed contracts and policies; English | Retrieve exact supporting spans from long legal and policy documents. |
| [Belgian Statutory Article Retrieval Dataset](benchmarks/retrieval-rag-citation.md#bsard) | benchmark | recommended | Belgium; French | Retrieve Belgian statutory articles relevant to a legal question. |
| [LLeQA](benchmarks/retrieval-rag-citation.md#lleqa) | benchmark | specialist | Belgium; French | Retrieve Belgian legal authorities and generate long-form answers to practitioner-style questions. |
| [CLERC](benchmarks/retrieval-rag-citation.md#clerc) | benchmark | specialist | United States; English | Retrieve US case-law evidence and generate citation-grounded legal text. |
| [Reasoning-Focused Legal Retrieval Benchmark](benchmarks/retrieval-rag-citation.md#reglab-reasoning-focused-retrieval) | benchmark-suite | recommended | United States; English | Retrieve controlling text for legal questions whose answer has low lexical overlap with the relevant source. |
| [LeCaRDv2](benchmarks/retrieval-rag-citation.md#lecardv2) | benchmark | recommended | China; Chinese | Retrieve legally similar Chinese criminal cases using graded relevance across characterization, penalty, and procedure. |
| [Competition on Legal Information Extraction/Entailment](benchmarks/retrieval-rag-citation.md#coliee) | shared-task | recommended | Canada, Japan; English, Japanese | Retrieve and recognize entailment among Canadian cases and Japanese civil-code provisions. |
| [Legal RAG Bench](benchmarks/retrieval-rag-citation.md#legal-rag-bench) | benchmark | check before use | Victoria, Australia / criminal law and procedure; English | Evaluate an end-to-end legal RAG pipeline and attribute errors to retrieval versus generation. |
| [CanLegalRAGBench](benchmarks/retrieval-rag-citation.md#canlegalragbench) | benchmark | specialist | Canada, Ontario, British Columbia, Alberta, other Canadian provinces/federal courts; English, some French passages | Retrieve Canadian case law for realistic layperson and legal-professional queries and generate grounded answers. |

### Contracts and deal work

Clause extraction, provision classification, entailment, retrieval, merger agreements, and redlining.

| Entry | Kind | Label | Jurisdiction / language | Measures |
|---|---|---|---|---|
| [Contract Understanding Atticus Dataset](benchmarks/contracts-deal-work.md#cuad) | benchmark | recommended | United States / SEC filings; English | Locate 41 categories of commercially important clauses in long contracts. |
| [LEDGAR](benchmarks/contracts-deal-work.md#ledgar) | dataset | specialist | United States / SEC filings; English | Classify contract provisions into clause/topic labels. |
| [ContractNLI](benchmarks/contracts-deal-work.md#contractnli) | benchmark | recommended | Commercial NDAs / primarily United States practice; English | Determine whether a non-disclosure agreement entails, contradicts, or does not mention a fixed legal hypothesis and identify supporting evidence. |
| [Merger Agreement Understanding Dataset](benchmarks/contracts-deal-work.md#maud) | benchmark | recommended | United States / public-company M&A; English | Answer fine-grained questions about merger-agreement provisions. |
| [Atticus Clause Retrieval Dataset](benchmarks/contracts-deal-work.md#acord) | benchmark | recommended | United States / commercial contracts; English | Rank precedent contract clauses for an attorney-written drafting need. |
| [ContractEval](benchmarks/contracts-deal-work.md#contracteval) | evaluation-protocol | related artifact | United States / SEC filings; English | Evaluate long-context LLM clause-risk extraction on the public CUAD test set. |
| [RedlineBench](benchmarks/contracts-deal-work.md#redlinebench) | benchmark | check before use | United States / commercial contracting; English | Negotiate commercial contracts over four turns by producing native Word tracked changes and comments. |

### Prediction, fairness, and structured reasoning

Outcome prediction, subgroup performance, holding selection, deontic rules, and structured legal analysis.

| Entry | Kind | Label | Jurisdiction / language | Measures |
|---|---|---|---|---|
| [ECtHR Tasks A/B](benchmarks/prediction-fairness-rules.md#ecthr) | benchmark | recommended | European Court of Human Rights / Council of Europe; English | Predict European Convention articles alleged (Task A) or found violated (Task B) from case facts. |
| [FairLex](benchmarks/prediction-fairness-rules.md#fairlex) | benchmark-suite | recommended | Council of Europe, United States, Switzerland, China; English, German, French, Italian, Chinese | Evaluate legal prediction performance and group robustness across sensitive or legally salient subpopulations. |
| [CaseHOLD](benchmarks/prediction-fairness-rules.md#casehold) | benchmark | specialist | United States; English | Select the correct holding that completes an excerpt from a US judicial opinion. |
| [DeonticBench](benchmarks/prediction-fairness-rules.md#deonticbench) | benchmark-suite | recommended | United States federal tax, United States immigration, United States state housing, Airline policies; English, Prolog | Reason about obligations, permissions, prohibitions, eligibility, and amounts under long legal/policy rules, directly or through executable Prolog. |
| [ALARB](benchmarks/prediction-fairness-rules.md#alarb) | dataset | check before use | Saudi Arabia; Arabic | Reason over Saudi commercial-law cases, complete arguments, and identify governing statutory articles. |
| [MSLR-Bench](benchmarks/prediction-fairness-rules.md#mslr) | benchmark | check before use | China; Chinese | Extract structured facts and produce IRAC-style reasoning for Chinese insider-trading cases. |
| [MASLegalBench](benchmarks/prediction-fairness-rules.md#maslegalbench) | benchmark | check before use | United Kingdom / GDPR enforcement; English | Multi-agent deductive reasoning about GDPR enforcement facts, rules, application, common sense, and conclusions. |

### Agents and legal workflows

Tool use, process compliance, simulated legal work, and long-horizon professional tasks.

| Entry | Kind | Label | Jurisdiction / language | Measures |
|---|---|---|---|---|
| [LegalAgentBench](benchmarks/agents-workflows.md#legalagentbench) | benchmark | specialist | China; Chinese | Chinese legal tool use, multi-hop information gathering, and legal writing. |
| [Ready Jurist One](benchmarks/agents-workflows.md#ready-jurist-one) | benchmark | specialist | China; Chinese | Operate interactively in Chinese legal consultation, drafting, civil-court, and criminal-court environments. |
| [Legal Agent Benchmark](benchmarks/agents-workflows.md#harvey-lab) | benchmark | check before use | United States / commercial legal practice, mixed practice areas; English | Complete long-horizon legal matters using files, research, analysis, drafting, and validation tools. |
| [APEX-Agents — Corporate Lawyer](benchmarks/agents-workflows.md#apex-agents-corporate-law) | benchmark | check before use | Corporate-law practice / mixed; English | Complete realistic long-horizon corporate-law tasks across applications, files, and professional work environments. |

### Legal translation

Shared tasks and multilingual corpora with automatic and legal-expert translation scoring.

| Entry | Kind | Label | Jurisdiction / language | Measures |
|---|---|---|---|---|
| [JUST-NLP 2025 Legal MT Shared Task](benchmarks/translation.md#just-nlp-2025-legal-mt) | shared-task | specialist | India; English, Hindi | Translate legal text from English to Hindi. |
| [SwiLTra-Bench](benchmarks/translation.md#swiltra-bench) | benchmark-suite | recommended | Switzerland; German, French, Italian, Romansh, English | Translate Swiss laws, court headnotes, and press releases among official Swiss languages and English. |
| [Multilingual Indian Legal Parallel Corpus](benchmarks/translation.md#milpac) | benchmark-suite | recommended | India; English, Hindi, Bengali, Marathi, Tamil, Gujarati, Telugu, Malayalam, Punjabi, Odia | Translate verified Indian legal text from English into nine Indian languages. |

### Evaluators, private tests, and related resources

Artifacts worth tracking that are not comparable public benchmarks, including frameworks, private tests, and resource lists.

| Entry | Kind | Label | Jurisdiction / language | Measures |
|---|---|---|---|---|
| [LegalEval-Q](benchmarks/related-evaluators.md#legaleval-q) | evaluation-framework | related artifact | China; Chinese | Predict the quality of Chinese LLM-generated legal answers. |
| [LRAGE](benchmarks/related-evaluators.md#lrage) | evaluation-framework | related artifact | Global / configuration-dependent; Multiple / configuration-dependent | Configure legal RAG evaluations across retrievers, rerankers, agents, judges, and custom corpora. |
| [prinzbench](benchmarks/related-evaluators.md#prinzbench) | private-benchmark | related artifact | United States; English | Answer obscure US legal-research and general information-search questions. |
| [Open Legal-Answer Benchmark](benchmarks/related-evaluators.md#open-legal-answer-benchmark) | benchmark | check before use | United States; English | Produce current US legal answers with relevant, supported, and correctly ranged citations. |
| [awesome-legal-nlp](benchmarks/related-evaluators.md#awesome-legal-nlp) | resource-list | related artifact | Global / mixed; Multiple | Discovery index for legal NLP datasets, models, papers, surveys, books, and events. |
