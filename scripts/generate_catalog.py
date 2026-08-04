#!/usr/bin/env python3
"""Generate the public Markdown and CSV views from catalog/benchmarks.json."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalog" / "benchmarks.json"

SECTIONS = [
    (
        "General legal reasoning and education",
        ["legalbench", "lawbench", "lexglue", "lextreme", "lexam", "lexeval", "arablegaleval", "il-tur", "kcl"],
    ),
    (
        "Retrieval, RAG, and citation",
        ["mleb", "legalbench-rag", "bsard", "lleqa", "clerc", "reglab-reasoning-focused-retrieval", "lecardv2", "coliee", "legal-rag-bench", "canlegalragbench"],
    ),
    (
        "Contracts and deal work",
        ["cuad", "ledgar", "contractnli", "maud", "acord", "contracteval", "redlinebench"],
    ),
    (
        "Prediction, fairness, and structured reasoning",
        ["ecthr", "fairlex", "casehold", "deonticbench", "alarb", "mslr", "maslegalbench"],
    ),
    (
        "Agents and legal workflows",
        ["legalagentbench", "ready-jurist-one", "harvey-lab", "apex-agents-corporate-law"],
    ),
    (
        "Legal translation",
        ["just-nlp-2025-legal-mt", "swiltra-bench", "milpac"],
    ),
    (
        "Evaluators, private tests, and related resources",
        ["legaleval-q", "lrage", "prinzbench", "open-legal-answer-benchmark", "awesome-legal-nlp"],
    ),
]

TIER_LABELS = {
    "recommended": "recommended",
    "specialist": "specialist",
    "evaluate-carefully": "evaluate carefully",
    "related": "related—not a comparable public benchmark",
}

QUICK_PICKS = [
    ("Broad English legal NLU", "LexGLUE + LegalBench", "lexglue", "Use per-task scores; do not trust one blended rank."),
    ("Broad Chinese evaluation", "LawBench + LexEval", "lawbench", "Public exam data have high contamination risk."),
    ("Multilingual European law", "LEXTREME", "lextreme", "Harmonic aggregation punishes weak languages/tasks."),
    ("Multilingual Indian law", "IL-TUR", "il-tur", "Eight tasks are uneven in size and language coverage."),
    ("Contract extraction", "CUAD + ContractNLI + MAUD", "cuad", "Split by document family and check memorization."),
    ("Contract clause retrieval", "ACORD", "acord", "Strong graded expert qrels; only 114 queries."),
    ("Legal retrieval / RAG", "LegalBench-RAG + BSARD + RegLab", "legalbench-rag", "Pair retrieval metrics with answer-grounding checks."),
    ("Agentic legal work", "J1Bench + LAB + APEX legal slice", "ready-jurist-one", "Harness, judge, and environment are part of the model."),
    ("Rule/deontic reasoning", "DeonticBench", "deonticbench", "Pin the post-audit Prolog revision."),
    ("Fairness / subgroup robustness", "FairLex", "fairlex", "Report group sizes and uncertainty with worst-group scores."),
    ("Legal translation", "SwiLTra-Bench + MILPaC", "swiltra-bench", "Automatic MT metrics do not establish legal fidelity."),
]


def load_catalog() -> dict:
    return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))


def md_links(entry: dict) -> str:
    labels = {
        "github": "GitHub",
        "huggingface": "Hugging Face",
        "papers": "paper",
        "leaderboards": "leaderboard",
        "project": "project",
    }
    links: list[str] = []
    for kind, label in labels.items():
        urls = entry["resources"][kind]
        for index, url in enumerate(urls, start=1):
            suffix = f" {index}" if len(urls) > 1 else ""
            links.append(f"[{label}{suffix}]({url})")
    return " · ".join(links)


def resource_lines(resources: dict) -> list[str]:
    labels = {
        "github": "GitHub",
        "huggingface": "Hugging Face",
        "papers": "Paper / arXiv",
        "leaderboards": "Leaderboard / competition",
        "project": "Project",
    }
    lines: list[str] = []
    for kind, label in labels.items():
        urls = resources[kind]
        value = "<br>".join(f"[{url}]({url})" for url in urls) if urls else "None"
        lines.append(f"| {label} | {value} |")
    return lines


def generate_readme(catalog: dict) -> str:
    entries = {entry["id"]: entry for entry in catalog["entries"]}
    resource_counts = {
        family: len({url for entry in catalog["entries"] for url in entry["resources"][family]})
        for family in ("github", "huggingface", "papers", "leaderboards", "project")
    }
    unique_resource_count = len(
        {url for entry in catalog["entries"] for urls in entry["resources"].values() for url in urls}
    )
    covered = [entry_id for _, section_ids in SECTIONS for entry_id in section_ids]
    missing = sorted(set(entries) - set(covered))
    duplicates = sorted({entry_id for entry_id in covered if covered.count(entry_id) > 1})
    unknown = sorted(set(covered) - set(entries))
    if missing or duplicates or unknown:
        raise ValueError(f"section map invalid: missing={missing}, duplicates={duplicates}, unknown={unknown}")

    lines = [
        "# Awesome Legal Benchmarks",
        "",
        "A curated, evidence-first guide to benchmarks for legal language models, retrieval systems, and agents.",
        "",
        f"**Research snapshot:** {catalog['as_of']} · **Canonical entries:** {len(entries)} · **Original list audited:** all 22 bullets (21 identities; MLEB was duplicated)",
        "",
        f"**Resource inventory:** [{unique_resource_count} unique canonical URLs checked](catalog/resource-snapshot.json) · {resource_counts['github']} GitHub · {resource_counts['huggingface']} Hugging Face · {resource_counts['papers']} papers · {resource_counts['leaderboards']} leaderboards/competitions · {resource_counts['project']} project pages",
        "",
        "> A benchmark score is evidence about a defined task under a defined protocol—not proof that a system is legally correct, safe, current, fair, or ready for unsupervised practice.",
        "",
        "This repository links to canonical artifacts instead of redistributing datasets. Every entry records its legal construct, exact scoring protocol, jurisdiction/language, data provenance, access and license, reproducibility limits, and leakage risk. See the [full catalog](docs/catalog.md), [metric theory](docs/metric-theory.md), [selection guide](docs/selection-guide.md), and [source audit](docs/source-audit.md).",
        "",
        "## Pick by use case",
        "",
        "| Use case | Start with | Why / caution |",
        "|---|---|---|",
    ]
    for use_case, label, entry_id, note in QUICK_PICKS:
        lines.append(f"| {use_case} | [{label}](docs/catalog.md#{entry_id}) | {note} |")
    lines += [
        "",
        "## Curation labels",
        "",
        "- **recommended** — unusually useful combination of clear task contract, primary-source artifacts, and reproducibility.",
        "- **specialist** — legitimate and useful for a narrower jurisdiction, task, or protocol.",
        "- **evaluate carefully** — real artifact with material judge, vendor, split, licensing, or validity caveats.",
        "- **related** — dataset, framework, protocol, private test, or resource list; retained so it is not mistaken for a comparable public benchmark.",
        "",
        "## Curated list",
        "",
    ]
    for title, section_ids in SECTIONS:
        lines += [f"### {title}", ""]
        for entry_id in section_ids:
            entry = entries[entry_id]
            metrics = "; ".join(metric["name"] for metric in entry["metrics"])
            jurisdictions = ", ".join(entry["jurisdictions"])
            languages = ", ".join(entry["languages"])
            lines.append(
                f"- **[{entry['name']}](docs/catalog.md#{entry_id})** "
                f"— {entry['capability']} **{TIER_LABELS[entry['tier']]}** · "
                f"{entry['kind']} · {jurisdictions} · {languages}. "
                f"**Data:** {entry['data']['size']}. **Metrics:** {metrics}. {md_links(entry)}"
            )
            lines.append(f"  - **Key caveat:** {entry['risks'][0]}")
        lines.append("")

    lines += [
        "## What counts as legitimate here",
        "",
        "An entry needs a primary or official source that identifies the artifact and defines its task and score. We then label—rather than hide—missing code, missing HF data, gates, private tests, vendor ownership, changing judges, mixed licenses, public-label contamination, and unresolved count conflicts. The [watchlist](docs/watchlist.md) contains promising releases that need more validation or maturity.",
        "",
        "## Repository map",
        "",
        "- [`catalog/benchmarks.json`](catalog/benchmarks.json) — source of truth.",
        "- [`catalog/benchmarks.csv`](catalog/benchmarks.csv) — spreadsheet-friendly flat view.",
        "- [`catalog/resources.csv`](catalog/resources.csv) — every canonical GitHub, HF, paper, project, and leaderboard URL.",
        "- [`catalog/resource-snapshot.json`](catalog/resource-snapshot.json) — live verification of every canonical repository, dataset, paper, leaderboard, competition, and project URL.",
        "- [`docs/catalog.md`](docs/catalog.md) — full human-readable benchmark profiles.",
        "- [`docs/metric-theory.md`](docs/metric-theory.md) — formulas, what each metric rewards, and where it fails.",
        "- [`docs/source-audit.md`](docs/source-audit.md) — reconstruction of the 22-bullet source list, including duplicate and stale links.",
        "- [`awesome-legal-benchmarks.xlsx`](outputs/awesome-legal-benchmarks.xlsx) — formatted workbook generated from the same catalog.",
        "",
        "## Validate and regenerate",
        "",
        "```bash",
        "python scripts/validate_catalog.py",
        "python -m unittest discover -s tests -v",
        "python scripts/generate_catalog.py --check",
        "python scripts/check_resources.py --check-snapshot",
        "```",
        "",
        "## Contributing",
        "",
        "Read [CONTRIBUTING.md](CONTRIBUTING.md). A new entry needs direct primary links, a defined evaluation contract, data provenance, access/license terms, and a concrete contamination or validity analysis. Marketing pages alone are not enough.",
        "",
        "## License",
        "",
        "Catalog prose and structured metadata are released under [CC BY 4.0](LICENSE); validation and generation code are released under [MIT](LICENSE-CODE). Linked datasets and repositories retain their own licenses.",
        "",
    ]
    return "\n".join(lines)


def generate_catalog_doc(catalog: dict) -> str:
    entries = {entry["id"]: entry for entry in catalog["entries"]}
    ordered_ids = [entry_id for _, ids in SECTIONS for entry_id in ids]
    lines = [
        "# Full benchmark catalog",
        "",
        f"Research snapshot: **{catalog['as_of']}**. Verified facts are sourced by each entry's direct resource links; inferences and unresolved ambiguities are labeled separately.",
        "",
        "Back to [README](../README.md).",
        "",
    ]
    for entry_id in ordered_ids:
        entry = entries[entry_id]
        lines += [
            f"## {entry['name']}",
            "",
            f"`{entry['id']}` · **{entry['kind']}** · **{TIER_LABELS[entry['tier']]}** · {entry['status']}",
            "",
            entry["capability"],
            "",
            "| Field | Detail |",
            "|---|---|",
            f"| Construct / theory | {entry['construct']} |",
            f"| Jurisdiction | {', '.join(entry['jurisdictions'])} |",
            f"| Languages | {', '.join(entry['languages'])} |",
            f"| Size | {entry['data']['size']} |",
            f"| Splits | {entry['data']['splits']} |",
            f"| Source | {entry['data']['source']} |",
            f"| Input | {entry['data']['input']} |",
            f"| Output | {entry['data']['output']} |",
            f"| Baselines / leaderboard context | {entry['baselines']} |",
            f"| Dataset access | {entry['access']['dataset']} |",
            f"| License | {entry['access']['license']} |",
            f"| Gating | {entry['access']['gating']} |",
            f"| Maintenance | {entry['maintenance']} |",
            f"| Reproducibility | {entry['reproducibility']} |",
        ]
        lines += ["", "### Metrics", ""]
        for metric in entry["metrics"]:
            judge = f" Judge: {metric['judge']}." if metric.get("judge") else ""
            primary = " **Primary.**" if metric.get("primary") else ""
            lines.append(f"- **{metric['name']}** — {metric['protocol']}{judge}{primary}")
        lines += ["", "### Resources", "", "| Resource | Direct URL |", "|---|---|"]
        lines += resource_lines(entry["resources"])
        lines += ["", "### Validity and evidence", ""]
        lines.append("**Risks / caveats**")
        lines += [f"- {item}" for item in entry["risks"]]
        lines += ["", "**Verified facts**"]
        lines += [f"- {item}" for item in entry["evidence"]["verified"]]
        lines += ["", "**Inference**"]
        lines += [f"- {item}" for item in entry["evidence"]["inference"]] or ["- None recorded."]
        lines += ["", "**Unresolved ambiguity**"]
        lines += [f"- {item}" for item in entry["evidence"]["ambiguities"]] or ["- None recorded."]
        source = ", ".join(f"#{number}" for number in entry["source_readme_bullets"])
        lines += ["", f"Original README bullet(s): {source or 'Curated addition.'}", ""]
    return "\n".join(lines)


def csv_rows(catalog: dict) -> tuple[list[str], list[list[str]]]:
    headers = [
        "id", "name", "kind", "tier", "status", "categories", "capability",
        "construct", "jurisdictions", "languages", "size", "splits", "source",
        "input", "output", "metrics", "baselines", "github", "huggingface",
        "papers", "leaderboards", "project", "dataset_access", "license", "gating",
        "maintenance", "reproducibility", "risks", "verified", "inference",
        "ambiguities", "source_readme_bullets", "curated_addition", "as_of",
    ]
    rows: list[list[str]] = []
    for entry in catalog["entries"]:
        rows.append([
            entry["id"], entry["name"], entry["kind"], entry["tier"], entry["status"],
            " | ".join(entry["categories"]), entry["capability"], entry["construct"],
            " | ".join(entry["jurisdictions"]), " | ".join(entry["languages"]),
            entry["data"]["size"], entry["data"]["splits"], entry["data"]["source"],
            entry["data"]["input"], entry["data"]["output"],
            " | ".join(f"{m['name']}: {m['protocol']}" for m in entry["metrics"]),
            entry["baselines"], " | ".join(entry["resources"]["github"]),
            " | ".join(entry["resources"]["huggingface"]),
            " | ".join(entry["resources"]["papers"]),
            " | ".join(entry["resources"]["leaderboards"]),
            " | ".join(entry["resources"]["project"]), entry["access"]["dataset"],
            entry["access"]["license"], entry["access"]["gating"], entry["maintenance"],
            entry["reproducibility"], " | ".join(entry["risks"]),
            " | ".join(entry["evidence"]["verified"]),
            " | ".join(entry["evidence"]["inference"]),
            " | ".join(entry["evidence"]["ambiguities"]),
            " | ".join(map(str, entry["source_readme_bullets"])),
            str(entry["curated_addition"]).lower(), catalog["as_of"],
        ])
    return headers, rows


def resources_csv(catalog: dict) -> tuple[list[str], list[list[str]]]:
    headers = ["benchmark_id", "benchmark_name", "resource_type", "url", "as_of"]
    rows: list[list[str]] = []
    for entry in catalog["entries"]:
        for resource_type, urls in entry["resources"].items():
            for url in urls:
                rows.append([entry["id"], entry["name"], resource_type, url, catalog["as_of"]])
    rows.sort(key=lambda row: (row[2], row[3], row[0]))
    return headers, rows


def render_csv(headers: list[str], rows: list[list[str]]) -> str:
    import io
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(headers)
    writer.writerows(rows)
    return output.getvalue()


def update(path: Path, content: str, check: bool) -> bool:
    existing = path.read_text(encoding="utf-8") if path.exists() else None
    if existing == content:
        return False
    if check:
        raise SystemExit(f"generated file is stale: {path.relative_to(ROOT)}")
    path.write_text(content, encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}")
    return True


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated files differ")
    args = parser.parse_args()
    catalog = load_catalog()
    headers, rows = csv_rows(catalog)
    resource_headers, resource_rows = resources_csv(catalog)
    update(ROOT / "README.md", generate_readme(catalog), args.check)
    update(ROOT / "docs" / "catalog.md", generate_catalog_doc(catalog), args.check)
    update(ROOT / "catalog" / "benchmarks.csv", render_csv(headers, rows), args.check)
    update(ROOT / "catalog" / "resources.csv", render_csv(resource_headers, resource_rows), args.check)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
