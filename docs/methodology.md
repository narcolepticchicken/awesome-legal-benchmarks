# How this catalog works

This catalog is built for benchmark selection, not link accumulation. An entry must have a stable identity, a legal task or legally grounded evaluation protocol, and enough primary evidence to explain what the score counts.

[Catalog index](catalog.md) · [Selection guide](selection-guide.md) · [Metric field guide](metric-theory.md) · [Source audit](source-audit.md)

## What gets recorded

Every canonical record answers the same questions:

1. What capability or task is the artifact meant to measure?
2. Which jurisdiction, language, source population, and time period does it cover?
3. How were the data created, split, and released?
4. What does the system receive, and what must it return?
5. Which metric, parser, rubric, human reviewer, or model judge produces the score?
6. How are item scores aggregated, and what baselines or leaderboard results exist?
7. Can an independent user access the data, code, dependencies, and license terms?
8. How could contamination, near-duplicates, temporal leakage, judge dependence, or benchmark-specific tuning inflate the result?
9. Is the artifact maintained, fixed, annual, private, stale, or unclear?
10. Who owns the instrument, do they sell a system it evaluates, and what is the latest verified update?

The machine-readable contract lives in [`catalog/schema.json`](../catalog/schema.json). The records live in [`catalog/benchmarks.json`](../catalog/benchmarks.json).

## Artifact type comes first

The repo does not treat every legal-data project as a benchmark.

| Kind | Meaning in this catalog |
| --- | --- |
| `benchmark` | A fixed task, item set, interface, and scoring protocol intended for model or system comparison. |
| `benchmark-suite` | Multiple tasks or datasets evaluated under a named suite. |
| `shared-task` | A time-bounded competition with an official task package and scoring process. |
| `dataset` | A corpus or labeled data release that can support evaluation but does not by itself fix the full protocol. |
| `evaluation-framework` | Software for configuring and running evaluations; results depend on the selected data and settings. |
| `evaluation-protocol` | A scoring method or procedure applied to another dataset. |
| `private-benchmark` | A test whose items or scorer are materially withheld. |
| `resource-list` | A discovery list with no evaluation construct or score. |

This distinction matters because a dataset can support several incompatible benchmarks, and the same benchmark data can produce different results after a prompt, parser, split, or scorer change. The LM Evaluation Harness makes this dependency concrete: its task configuration fixes the dataset path and split, input and target templates, output type, post-processing filters, metrics, aggregation, and version metadata. It recommends sharing the task configuration with the code commit for reproduction ([official task guide](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/task_guide.md)).

## Evidence labels

Each profile separates three kinds of statements:

- **Verified fact:** supported by an official repository, official dataset card, primary paper, or official competition page linked in that profile.
- **Inference:** the catalog's interpretation of the published design or likely validity limit.
- **Unresolved ambiguity:** primary sources disagree, omit a needed detail, or point to an artifact that could not be verified.

An HTTP success in [`catalog/resource-snapshot.json`](../catalog/resource-snapshot.json) establishes that a URL was reachable on the snapshot date. It does not establish ownership, scientific validity, licensing, or reproducibility. Those require the linked primary materials.

## Update provenance

The public index, category pages, and workbook use one date for browsing: **latest verified update**. It is the newest benchmark-relevant first-party event found by the research cutoff—a repository push, dataset modification, paper revision, competition cycle, or official displayed update date. It is left blank in the source record when no later update was verified.

Each update stores precision (`year`, `month`, or `day`), basis, and a direct source URL. A repository push is evidence that the repository changed, not proof that the benchmark data or scoring protocol changed. Likewise, a paper revision may be newer than the released code without superseding it. Profiles preserve those distinctions and flag conflicting official dates or counts.

The machine-readable source retains its historical `dates.created` field for audit traceability, but the generated GitHub tables and workbook do not display it and do not use it for sorting or country grouping.

Owner and access are recorded separately from quality. A vendor can publish a strong open benchmark; an academic artifact can have an unclear license or weak scorer. The `commercial_interest` field only marks whether the owner sells a system or service materially connected to the evaluation.

## Curation labels

The label is a decision aid. It is not a model rank or a claim that one legal domain matters more than another.

| Label | Rule |
| --- | --- |
| `recommended` | The public task contract is clear, the primary artifacts are available, and reproduction is comparatively strong for that class of evaluation. |
| `specialist` | The artifact is useful within a narrower jurisdiction, language, task, or protocol. |
| `evaluate-carefully` | The artifact is real, but a judge, vendor relationship, split, license, access condition, size, or validity issue needs attention before use. |
| `related` | The artifact is a dataset, framework, protocol, private test, or resource list that should not be ranked beside public benchmarks. |

No label cancels the profile caveats. A recommended public benchmark can still be heavily contaminated. A specialist benchmark can be the right choice when its jurisdiction and task match the deployment.

## How to read capability claims

A benchmark is an instrument made from at least five coupled parts:

1. the intended construct;
2. the item population and sampling process;
3. the model interface and available tools;
4. the scorer, parser, judge, or human rubric;
5. the aggregation and uncertainty procedure.

Changing one part changes the evidence. HELM addresses this by organizing evaluations through an explicit scenario taxonomy, reporting multiple metrics, exposing prompts and predictions, and stating what its coverage misses ([official HELM site](https://crfm.stanford.edu/helm/latest/)). MTEB likewise separates selecting tasks and benchmarks from running evaluations, loading results, and contributing new artifacts ([official MTEB repository](https://github.com/embeddings-benchmark/mteb)).

Compare scores only after the benchmark version, dataset revision, task subset, prompt, tools, model endpoint, parser, metric, judge, and aggregation are pinned. The [minimum result card](metric-theory.md#minimum-honest-result-card) lists the fields to publish.

## Why the repository is split this way

The front page presents United States entries first, keeps multi-jurisdiction artifacts separate, and groups international entries by country and recency. It also routes readers by legal job while keeping the exhaustive evaluation contracts in category profiles. The compact index supports browsing; the JSON and CSV support filtering; the metric guide handles formulas; the source audit preserves corrections and duplicate identities.

That structure follows useful parts of several primary projects:

- The Awesome manifesto treats an awesome list as curation, asks maintainers to explain why an item belongs, and calls for a clear scope, contents, categories, contribution rules, and a license ([official manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md)).
- MTEB keeps overview, task selection, benchmark definitions, evaluation execution, results, and contribution paths separate ([official repository](https://github.com/embeddings-benchmark/mteb)).
- Hugging Face dataset cards expose language, license, size, task categories, provenance context, and limitations as discovery metadata and documentation ([official dataset-card documentation](https://huggingface.co/docs/hub/en/datasets-cards)).
- The LM Evaluation Harness treats the evaluation configuration and code revision as part of the result, including output parsing and aggregation ([official task guide](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/task_guide.md)).

The catalog borrows those separation principles. It does not copy their taxonomies or imply their endorsement.

## Refresh and removal

The `as_of` field is a research cutoff, not a promise that every external project is still maintained. Updates should pin the evidence date and record count or protocol conflicts instead of silently choosing one source.

An entry can move to the [watchlist](watchlist.md) when its identity, license, scorer, data release, or ownership cannot be established. It can remain in the catalog with a weaker label when the artifact is legitimate but materially limited. Removal is appropriate when the canonical identity was false, the links resolve to an unrelated artifact, or no legal evaluation object exists.
