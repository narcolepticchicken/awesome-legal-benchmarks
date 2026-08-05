# Awesome Legal Benchmarks

<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re) [![Validate catalog](https://github.com/narcolepticchicken/awesome-legal-benchmarks/actions/workflows/validate.yml/badge.svg)](https://github.com/narcolepticchicken/awesome-legal-benchmarks/actions/workflows/validate.yml)

Use this catalog to pick a legal benchmark and see what its score can actually support. Each entry records the task, jurisdiction, language, data, input/output contract, scorer, access terms, primary sources, and the biggest validity problem.

**Research snapshot: 2026-08-04.** 69 canonical identities, including public benchmarks, private vendor benchmarks, datasets, shared tasks, evaluation frameworks, protocols, and one resource list.

> Start with the legal job. Then check jurisdiction, source material, interface, scorer, and prior exposure. If those do not match the system you care about, the score is weak evidence.

## Contents

- [Possible use cases](#possible-use-cases)
- [Browse by area](#browse-by-area)
- [What the labels mean](#what-the-labels-mean)
- [Read a benchmark score](#read-a-benchmark-score)
- [Files and methodology](#files-and-methodology)
- [Contribute](#contribute)

## Possible use cases

These are starting points, not interchangeable leaderboards. Each use case names the legal work, the artifact to start with, and the decision its score can inform.

| Legal work | Start with | Possible use cases |
|---|---|---|
| Broad English legal reasoning | [LegalBench](docs/benchmarks/reasoning-education.md#legalbench) + [LexGLUE](docs/benchmarks/reasoning-education.md#lexglue) + [PRBench legal](docs/benchmarks/reasoning-education.md#prbench) | Compare per-task reasoning and language-understanding scores, then test open professional analysis against granular criteria. |
| Chinese legal reasoning | [LawBench](docs/benchmarks/reasoning-education.md#lawbench) + [LexEval](docs/benchmarks/reasoning-education.md#lexeval) + [LexGenius](docs/benchmarks/reasoning-education.md#lexgenius) + [PLawBench](docs/benchmarks/reasoning-education.md#plawbench) | Screen knowledge and reasoning broadly, then inspect open-ended consultation, case analysis, and drafting. |
| Arabic and Saudi legal work | [ArabLegalEval](docs/benchmarks/reasoning-education.md#arablegaleval) + [ALARB](docs/benchmarks/reasoning-education.md#alarb) | Separate translated or synthetic tasks from Saudi case-based verdict, argument, and statutory-article tasks. |
| Multilingual legal NLU | [LEXTREME](docs/benchmarks/reasoning-education.md#lextreme) + [IL-TUR](docs/benchmarks/reasoning-education.md#il-tur) | Compare per-language and per-task behavior before relying on an aggregate multilingual score. |
| Italian and Indian statutory retrieval | [JuriFindIT](docs/benchmarks/retrieval-rag-citation.md#jurifindit) + [ILSIC](docs/benchmarks/retrieval-rag-citation.md#ilsic) | Test expert Italian article retrieval and Indian statute identification from layperson queries; keep synthetic and court-derived training sources separate. |
| Patent and intellectual-property work | [PILOT-Bench](docs/benchmarks/reasoning-education.md#pilot-bench) + [MoZIP](docs/benchmarks/reasoning-education.md#mozip) | Compare US patent-appeal classification with multilingual IP knowledge, open QA, and patent-semantic matching; neither substitutes for a private drafting or validity-review holdout. |
| Multimodal legal education | [RoD-TAL](docs/benchmarks/retrieval-rag-citation.md#rod-tal) | Test Romanian traffic-law retrieval and QA when images or signs are legally material. |
| Contract extraction and classification | [CUAD](docs/benchmarks/contracts-deal-work.md#cuad) + [ContractNLI](docs/benchmarks/contracts-deal-work.md#contractnli) + [MAUD](docs/benchmarks/contracts-deal-work.md#maud) | Test clause finding, evidence entailment, and merger-agreement provision classification on document-family-held-out data. |
| Contract retrieval | [ACORD](docs/benchmarks/contracts-deal-work.md#acord) | Rank clauses against attorney-authored requests using graded relevance judgments. |
| Redlining and contract review | [RedlineBench](docs/benchmarks/contracts-deal-work.md#redlinebench) + [LegalOn 2026](docs/benchmarks/contracts-deal-work.md#legalon-contract-review-2026) + [Ivo study](docs/benchmarks/contracts-deal-work.md#ivo-contract-review-study) + [legalbenchmarks.ai](docs/benchmarks/contracts-deal-work.md#legalbenchmarks-ai) | Test native-file edits, issue spotting, formatting retention, and review usefulness; only RedlineBench is openly runnable. |
| Legal retrieval and RAG | [LegalBench-RAG](docs/benchmarks/retrieval-rag-citation.md#legalbench-rag) + [RegLab retrieval](docs/benchmarks/retrieval-rag-citation.md#reglab-reasoning-focused-retrieval) + [bLLeQA](docs/benchmarks/retrieval-rag-citation.md#blleqa) + [Legal RAG Bench](docs/benchmarks/retrieval-rag-citation.md#legal-rag-bench) + [CanLegalRAGBench](docs/benchmarks/retrieval-rag-citation.md#canlegalragbench) | Measure authority retrieval, answer correctness, citation extraction, refusal, and grounding separately on a jurisdiction-matched corpus. |
| Citation safety | [LegalCiteBench](docs/benchmarks/retrieval-rag-citation.md#legalcitebench) + [Legal Phantom Citation](docs/benchmarks/retrieval-rag-citation.md#legal-phantom-citation) + [Large Legal Fictions](docs/benchmarks/retrieval-rag-citation.md#reglab-legal-hallucinations) + [Hallucination-Free?](docs/benchmarks/retrieval-rag-citation.md#reglab-legal-rag-hallucinations) | Test citation retrieval, abstention, phantom-citation detection, and human-coded research-tool hallucination as distinct failure modes. |
| Long-horizon legal agents | [DLawBench](docs/benchmarks/agents-workflows.md#dlawbench) + [Harvey LAB](docs/benchmarks/agents-workflows.md#harvey-lab) + [Legora BAR](docs/benchmarks/agents-workflows.md#legora-bar) + [Mercor APEX legal](docs/benchmarks/agents-workflows.md#apex-agents-corporate-law) | Evaluate consultation or matter completion with files, tools, rubrics, repeated runs, cost, and latency; BAR's full instrument is private. |
| In-house legal work | [GC AI In-House Legal Bench](docs/benchmarks/agents-workflows.md#gc-ai-in-house-legal-bench) + [CoCoBench](docs/benchmarks/agents-workflows.md#thomson-reuters-cocobench) + [Harvey BigLaw Bench](docs/benchmarks/agents-workflows.md#harvey-biglaw-bench) | Use their task taxonomies and published results as private-vendor evidence when designing an internal matter-level holdout. |
| Rule and robustness testing | [DeonticBench](docs/benchmarks/prediction-fairness-rules.md#deonticbench) + [OpenExempt](docs/benchmarks/prediction-fairness-rules.md#openexempt) | Test deontic consistency and symbolic statutory reasoning under controlled perturbations. |
| Fairness and subgroup performance | [FairLex](docs/benchmarks/prediction-fairness-rules.md#fairlex) | Compare overall, per-group, worst-group, and gap metrics with group sizes and uncertainty. |
| Legal translation | [SwiLTra-Bench](docs/benchmarks/translation.md#swiltra-bench) + [MILPaC](docs/benchmarks/translation.md#milpac) + [JUST-NLP 2025](docs/benchmarks/translation.md#just-nlp-2025-legal-mt) | Compare automatic metrics with legal-expert ratings for terminology, omissions, and legal effect. |

Pair any public comparison with a fresh, matter-specific holdout before making a deployment or procurement decision. The [selection guide](docs/selection-guide.md) gives a fuller recommendation matrix.

## Browse by area

Each category page contains full profiles with owner, creation date, latest verified update, access boundary, metrics, direct official sources, possible uses, and unresolved facts.

| Area | What is inside | Entries |
|---|---|---:|
| [General legal reasoning and education](docs/benchmarks/reasoning-education.md) | Broad suites, legal language understanding, professional exams, and jurisdiction-specific knowledge tests. | 15 |
| [Retrieval, RAG, and citation](docs/benchmarks/retrieval-rag-citation.md) | Authority retrieval, exact-support retrieval, case similarity, citation grounding, and end-to-end legal RAG. | 21 |
| [Contracts and deal work](docs/benchmarks/contracts-deal-work.md) | Clause extraction, provision classification, entailment, retrieval, merger agreements, and redlining. | 10 |
| [Prediction, fairness, and structured reasoning](docs/benchmarks/prediction-fairness-rules.md) | Outcome prediction, subgroup performance, holding selection, deontic rules, and structured legal analysis. | 7 |
| [Agents and legal workflows](docs/benchmarks/agents-workflows.md) | Tool use, process compliance, simulated legal work, and long-horizon professional tasks. | 9 |
| [Legal translation](docs/benchmarks/translation.md) | Shared tasks and multilingual corpora with automatic and legal-expert translation scoring. | 3 |
| [Evaluators, private tests, and related resources](docs/benchmarks/related-evaluators.md) | Artifacts worth tracking that are not comparable public benchmarks, including frameworks, private tests, and resource lists. | 4 |

See the [compact 69-entry index](docs/catalog.md), or filter the machine-readable [JSON](catalog/benchmarks.json), [CSV](catalog/benchmarks.csv), and [workbook](outputs/awesome-legal-benchmarks.xlsx).

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
