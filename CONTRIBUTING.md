# Contributing

The bar is usefulness. A new link belongs here only when a reader can tell what the artifact measures, how the score is produced, and why that evidence fits a legal use case.

Read the [catalog methodology](docs/methodology.md) before proposing a new entry.

## Inclusion standard

A canonical entry needs all of the following:

- a legal task or legally grounded evaluation protocol;
- a primary artifact establishing identity and ownership;
- a concrete item/data source, input/output contract, and scoring rule;
- named jurisdiction(s), language(s), access conditions, and license status;
- enough public detail to separate verified fact, catalog inference, and unresolved ambiguity;
- a stable direct URL for every claimed repository, dataset, paper, and leaderboard.

A dataset, framework, private test, vendor report, or resource list may be useful. Label it as that artifact type; do not present it as a comparable public benchmark.

## Pull-request checklist

1. Add or edit the canonical record in [`catalog/benchmarks.json`](catalog/benchmarks.json). Do not hand-edit generated `README.md`, `docs/catalog.md`, `docs/benchmarks/*.md`, or CSV files.
2. Prefer official repositories, official Hugging Face namespaces, publisher/ACL/arXiv papers, and official competition pages. Label mirrors and secondary leaderboards.
3. Check the item count, task protocol, scorer, and evaluation population before carrying over a project claim. A marketing page by itself is not evidence.
4. Record owner and commercial interest; first-documented and latest-update dates with basis and direct source; access level, label visibility, and runnability; dataset construction, splits, provenance, input/output, exact metrics/aggregation, judge model, baseline/leaderboard, license/access, maintenance, contamination risk, and reproducibility.
5. Add one to three concrete `possible_uses` naming the legal task, material, and decision the score can inform. Do not use generic claims such as “evaluate model performance.”
6. Put uncertainty in `evidence.ambiguities` and interpretation in `evidence.inference`; do not silently resolve conflicting sources.
7. Run:

   ```bash
   python scripts/validate_catalog.py
   python scripts/generate_catalog.py
   python scripts/generate_catalog.py --check
   python -m unittest discover -s tests -v
   ```

8. If URLs change, regenerate `catalog/resource-snapshot.json` with `python scripts/check_resources.py` and include the date. A successful HTTP response establishes availability on that date. It does not establish ownership, licensing, scientific validity, or reproducibility.

## Curation decisions

- **recommended:** clear task contract, canonical artifacts, and comparatively strong reproducibility for its class.
- **specialist:** legitimate and useful within a narrower jurisdiction/task/protocol.
- **evaluate-carefully** (displayed as **check before use**): real artifact with material judge, vendor, split, license, access, or validity limitations.
- **related** (displayed as **related artifact**): dataset, framework, protocol, private benchmark, or resource list that should not be ranked as a comparable public benchmark.

Use a watchlist contribution when the release is very new, gated, internally inconsistent, missing evaluation code, or missing a stable canonical identity.

Catalog and documentation contributions are licensed under [CC BY 4.0](LICENSE); scripts are licensed under [MIT](LICENSE-CODE). Contributors must only submit material they have the right to license.
