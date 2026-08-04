# Awesome Legal Benchmarks

<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re) [![Validate catalog](https://github.com/narcolepticchicken/awesome-legal-benchmarks/actions/workflows/validate.yml/badge.svg)](https://github.com/narcolepticchicken/awesome-legal-benchmarks/actions/workflows/validate.yml)

Use this catalog to pick a legal benchmark and see what its score can actually support. Each entry records the task, jurisdiction, language, data, input/output contract, scorer, access terms, primary sources, and the biggest validity problem.

**Snapshot 2026-08-03:** 45 canonical entries · [all 22 source bullets audited](docs/source-audit.md) (21 identities; MLEB appeared twice) · [147 canonical URLs checked](catalog/resource-snapshot.json)

> Start with the legal job. Then check jurisdiction, source material, interface, scorer, and prior exposure. If those do not match the system you care about, the score is weak evidence.

## Contents

- [Choose a benchmark](#choose-a-benchmark)
- [Browse the catalog](#browse-the-catalog)
- [Read a score](#read-a-score)
- [Use the data](#use-the-data)
- [Contribute](#contribute)

## Choose a benchmark

1. Name the legal task, jurisdiction, language, and as-of date.
2. Match the benchmark interface to the system: closed-book QA, retrieval, drafting, translation, or tool use.
3. Inspect the split, scorer, judge, and public-label exposure before comparing models.
4. Pair public comparison data with a fresh, matter-specific holdout when the decision matters.

The [selection guide](docs/selection-guide.md) has the full recommendation matrix. These are the fastest starting points:

| Use case | Start with | Main caution |
|---|---|---|
| Broad English legal NLU | [LexGLUE](docs/benchmarks/reasoning-education.md#lexglue) + [LegalBench](docs/benchmarks/reasoning-education.md#legalbench) | Use per-task scores; a blended rank hides task differences. |
| Broad Chinese evaluation | [LawBench](docs/benchmarks/reasoning-education.md#lawbench) + [LexEval](docs/benchmarks/reasoning-education.md#lexeval) | Public exam data have high contamination risk. |
| Multilingual European law | [LEXTREME](docs/benchmarks/reasoning-education.md#lextreme) | Harmonic aggregation makes weak language/task performance matter. |
| Multilingual Indian law | [IL-TUR](docs/benchmarks/reasoning-education.md#il-tur) | Task size and language coverage vary across the suite. |
| Contract extraction | [CUAD](docs/benchmarks/contracts-deal-work.md#cuad) + [ContractNLI](docs/benchmarks/contracts-deal-work.md#contractnli) + [MAUD](docs/benchmarks/contracts-deal-work.md#maud) | Use document-family splits and check near-duplicate exposure. |
| Contract clause retrieval | [ACORD](docs/benchmarks/contracts-deal-work.md#acord) | Expert graded qrels are useful; the benchmark has 114 queries. |
| Legal retrieval / RAG | [LegalBench-RAG](docs/benchmarks/retrieval-rag-citation.md#legalbench-rag) + [BSARD](docs/benchmarks/retrieval-rag-citation.md#bsard) + [RegLab](docs/benchmarks/retrieval-rag-citation.md#reglab-reasoning-focused-retrieval) | Report retrieval and answer grounding separately. |
| Agentic legal work | [J1Bench](docs/benchmarks/agents-workflows.md#ready-jurist-one) + [LAB](docs/benchmarks/agents-workflows.md#harvey-lab) + [APEX legal slice](docs/benchmarks/agents-workflows.md#apex-agents-corporate-law) | The environment, tools, and judge are part of the instrument. |
| Rule/deontic reasoning | [DeonticBench](docs/benchmarks/prediction-fairness-rules.md#deonticbench) | Pin the post-audit Prolog and test revision. |
| Fairness / subgroup performance | [FairLex](docs/benchmarks/prediction-fairness-rules.md#fairlex) | Report group sizes, uncertainty, worst-group scores, and gaps. |
| Legal translation | [SwiLTra-Bench](docs/benchmarks/translation.md#swiltra-bench) + [MILPaC](docs/benchmarks/translation.md#milpac) | Automatic MT metrics do not establish legal fidelity. |

## Browse the catalog

Dumping 45 full profiles into one README is hard to use. This rebuild leads with the practical choice. The category pages keep claims tied to primary sources and expose the validity and contamination limits.

| Area | What is inside | Entries |
|---|---|---:|
| [General legal reasoning and education](docs/benchmarks/reasoning-education.md) | Broad suites, legal language understanding, professional exams, and jurisdiction-specific knowledge tests. | 9 |
| [Retrieval, RAG, and citation](docs/benchmarks/retrieval-rag-citation.md) | Authority retrieval, exact-support retrieval, case similarity, citation grounding, and end-to-end legal RAG. | 10 |
| [Contracts and deal work](docs/benchmarks/contracts-deal-work.md) | Clause extraction, provision classification, entailment, retrieval, merger agreements, and redlining. | 7 |
| [Prediction, fairness, and structured reasoning](docs/benchmarks/prediction-fairness-rules.md) | Outcome prediction, subgroup performance, holding selection, deontic rules, and structured legal analysis. | 7 |
| [Agents and legal workflows](docs/benchmarks/agents-workflows.md) | Tool use, process compliance, simulated legal work, and long-horizon professional tasks. | 4 |
| [Legal translation](docs/benchmarks/translation.md) | Shared tasks and multilingual corpora with automatic and legal-expert translation scoring. | 3 |
| [Evaluators, private tests, and related resources](docs/benchmarks/related-evaluators.md) | Artifacts worth tracking that are not comparable public benchmarks, including frameworks, private tests, and resource lists. | 5 |

See the [compact 45-entry index](docs/catalog.md), or filter the machine-readable [JSON](catalog/benchmarks.json) and [CSV](catalog/benchmarks.csv).

A catalog label is a curation judgment, not a leaderboard rank:

| Label | Meaning |
|---|---|
| **recommended** | Clear task contract, primary artifacts, and comparatively strong reproducibility for its class. |
| **specialist** | Useful within a narrower task, jurisdiction, language, or protocol. |
| **check before use** | Real artifact with a material judge, vendor, split, license, access, or validity issue. |
| **related artifact** | Dataset, framework, protocol, private test, or resource list. It is included so it is not mistaken for a comparable public benchmark. |

Artifact type is tracked separately. A dataset is not automatically a benchmark, and an evaluation framework does not define a fixed test. The [methodology](docs/methodology.md) explains the inclusion rule and evidence labels.

## Read a score

Before repeating a benchmark number, answer five questions:

1. What capability does success require, and what shortcut could produce the same score?
2. Which jurisdiction, language, source population, and time period does the sample cover?
3. What did the model receive, and what exact output did the scorer parse?
4. How are item scores aggregated? What uncertainty, subgroup, abstention, and failure counts are missing?
5. Were the questions, answers, documents, rubrics, or judge outputs exposed during training or development?

The [metric field guide](docs/metric-theory.md) gives the formulas and failure modes for accuracy, F-scores, retrieval metrics, overlap metrics, LLM judges, rubric scores, and benchmark-specific composites. It also breaks down LawBench's 20-task score map, LEXTREME's hierarchical harmonic mean, JUST-NLP AutoRank, KCL essay scoring, DeonticBench bootstrapping, and Ready Jurist One's dual scoring.

## Use the data

| Need | File |
|---|---|
| Canonical source of truth | [`catalog/benchmarks.json`](catalog/benchmarks.json) |
| Flat spreadsheet view | [`catalog/benchmarks.csv`](catalog/benchmarks.csv) |
| Every GitHub, Hugging Face, paper, project, and leaderboard URL | [`catalog/resources.csv`](catalog/resources.csv) |
| URL verification result | [`catalog/resource-snapshot.json`](catalog/resource-snapshot.json) |
| Original 22-bullet reconstruction | [`docs/source-audit.md`](docs/source-audit.md) |
| Releases that need more evidence | [`docs/watchlist.md`](docs/watchlist.md) |
| Formatted workbook | [`outputs/awesome-legal-benchmarks.xlsx`](outputs/awesome-legal-benchmarks.xlsx) |

Resource counts in this snapshot: 39 GitHub · 33 Hugging Face · 48 papers · 13 leaderboards or competitions · 17 project pages.

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
