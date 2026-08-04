# Contributing

Contributions should make the list more useful for choosing and reproducing legal evaluations, not merely longer.

## Inclusion standard

A canonical entry needs:

- a legal task or legally grounded evaluation protocol;
- a primary artifact establishing identity and ownership;
- a concrete item/data source, input/output contract, and scoring rule;
- named jurisdiction(s), language(s), access conditions, and license status;
- enough public detail to state what is verified, inferred, and unresolved;
- a stable direct URL for every claimed repository, dataset, paper, and leaderboard.

A dataset, framework, private test, vendor report, or resource list may be included, but must be labeled as such. It must not be presented as a comparable public benchmark.

## Pull-request checklist

1. Add or edit the canonical record in [`catalog/benchmarks.json`](catalog/benchmarks.json); do not hand-edit generated `README.md`, `docs/catalog.md`, or CSV files.
2. Prefer official repositories, official Hugging Face namespaces, publisher/ACL/arXiv papers, and official competition pages. Label mirrors and secondary leaderboards.
3. Quote no marketing claim as fact without checking the item count, task protocol, scorer, and evaluation population.
4. Record dataset construction, splits, provenance, input/output, exact metrics/aggregation, judge model, baseline/leaderboard, license/access, maintenance, contamination risk, and reproducibility.
5. Put uncertainty in `evidence.ambiguities` and interpretation in `evidence.inference`; do not silently resolve conflicting sources.
6. Run:

   ```bash
   python scripts/validate_catalog.py
   python scripts/generate_catalog.py
   python scripts/generate_catalog.py --check
   python -m unittest discover -s tests -v
   ```

7. If URLs change, regenerate `catalog/resource-snapshot.json` with `python scripts/check_resources.py` and include the date. A successful HTTP response establishes availability, not scientific validity.

## Curation decisions

- **recommended:** clear task contract, canonical artifacts, and unusually strong reproducibility for its class.
- **specialist:** legitimate and useful within a narrower jurisdiction/task/protocol.
- **evaluate-carefully:** real artifact with material judge, vendor, split, license, access, or validity limitations.
- **related:** dataset, framework, protocol, private benchmark, or resource list that should not be ranked as a comparable public benchmark.

Use a watchlist contribution when the release is very new, gated, internally inconsistent, missing evaluation code, or lacks a stable canonical identity.

Catalog and documentation contributions are licensed under [CC BY 4.0](LICENSE); scripts are licensed under [MIT](LICENSE-CODE). Contributors must only submit material they have the right to license.
