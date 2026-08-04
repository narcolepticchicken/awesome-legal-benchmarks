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
        "reasoning-education",
        "General legal reasoning and education",
        "Broad suites, legal language understanding, professional exams, and jurisdiction-specific knowledge tests.",
        ["legalbench", "lawbench", "lexglue", "lextreme", "lexam", "lexeval", "arablegaleval", "il-tur", "kcl"],
    ),
    (
        "retrieval-rag-citation",
        "Retrieval, RAG, and citation",
        "Authority retrieval, exact-support retrieval, case similarity, citation grounding, and end-to-end legal RAG.",
        ["mleb", "legalbench-rag", "bsard", "lleqa", "clerc", "reglab-reasoning-focused-retrieval", "lecardv2", "coliee", "legal-rag-bench", "canlegalragbench"],
    ),
    (
        "contracts-deal-work",
        "Contracts and deal work",
        "Clause extraction, provision classification, entailment, retrieval, merger agreements, and redlining.",
        ["cuad", "ledgar", "contractnli", "maud", "acord", "contracteval", "redlinebench"],
    ),
    (
        "prediction-fairness-rules",
        "Prediction, fairness, and structured reasoning",
        "Outcome prediction, subgroup performance, holding selection, deontic rules, and structured legal analysis.",
        ["ecthr", "fairlex", "casehold", "deonticbench", "alarb", "mslr", "maslegalbench"],
    ),
    (
        "agents-workflows",
        "Agents and legal workflows",
        "Tool use, process compliance, simulated legal work, and long-horizon professional tasks.",
        ["legalagentbench", "ready-jurist-one", "harvey-lab", "apex-agents-corporate-law"],
    ),
    (
        "translation",
        "Legal translation",
        "Shared tasks and multilingual corpora with automatic and legal-expert translation scoring.",
        ["just-nlp-2025-legal-mt", "swiltra-bench", "milpac"],
    ),
    (
        "related-evaluators",
        "Evaluators, private tests, and related resources",
        "Artifacts worth tracking that are not comparable public benchmarks, including frameworks, private tests, and resource lists.",
        ["legaleval-q", "lrage", "prinzbench", "open-legal-answer-benchmark", "awesome-legal-nlp"],
    ),
]

TIER_LABELS = {
    "recommended": "recommended",
    "specialist": "specialist",
    "evaluate-carefully": "check before use",
    "related": "related artifact",
}

QUICK_PICKS = [
    ("Broad English legal NLU", [("LexGLUE", "lexglue"), ("LegalBench", "legalbench")], "Use per-task scores; a blended rank hides task differences."),
    ("Broad Chinese evaluation", [("LawBench", "lawbench"), ("LexEval", "lexeval")], "Public exam data have high contamination risk."),
    ("Multilingual European law", [("LEXTREME", "lextreme")], "Harmonic aggregation makes weak language/task performance matter."),
    ("Multilingual Indian law", [("IL-TUR", "il-tur")], "Task size and language coverage vary across the suite."),
    ("Contract extraction", [("CUAD", "cuad"), ("ContractNLI", "contractnli"), ("MAUD", "maud")], "Use document-family splits and check near-duplicate exposure."),
    ("Contract clause retrieval", [("ACORD", "acord")], "Expert graded qrels are useful; the benchmark has 114 queries."),
    ("Legal retrieval / RAG", [("LegalBench-RAG", "legalbench-rag"), ("BSARD", "bsard"), ("RegLab", "reglab-reasoning-focused-retrieval")], "Report retrieval and answer grounding separately."),
    ("Agentic legal work", [("J1Bench", "ready-jurist-one"), ("LAB", "harvey-lab"), ("APEX legal slice", "apex-agents-corporate-law")], "The environment, tools, and judge are part of the instrument."),
    ("Rule/deontic reasoning", [("DeonticBench", "deonticbench")], "Pin the post-audit Prolog and test revision."),
    ("Fairness / subgroup performance", [("FairLex", "fairlex")], "Report group sizes, uncertainty, worst-group scores, and gaps."),
    ("Legal translation", [("SwiLTra-Bench", "swiltra-bench"), ("MILPaC", "milpac")], "Automatic MT metrics do not establish legal fidelity."),
]


def load_catalog() -> dict:
    return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))


def section_for(entry_id: str) -> tuple[str, str, str, list[str]]:
    for section in SECTIONS:
        if entry_id in section[3]:
            return section
    raise KeyError(f"entry is not assigned to a catalog section: {entry_id}")


def profile_href(entry_id: str, *, from_root: bool) -> str:
    slug, _, _, _ = section_for(entry_id)
    prefix = "docs/benchmarks" if from_root else "benchmarks"
    return f"{prefix}/{slug}.md#{entry_id}"


def quick_pick_links(items: list[tuple[str, str]]) -> str:
    return " + ".join(
        f"[{label}]({profile_href(entry_id, from_root=True)})"
        for label, entry_id in items
    )


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
    covered = [entry_id for _, _, _, section_ids in SECTIONS for entry_id in section_ids]
    missing = sorted(set(entries) - set(covered))
    duplicates = sorted({entry_id for entry_id in covered if covered.count(entry_id) > 1})
    unknown = sorted(set(covered) - set(entries))
    if missing or duplicates or unknown:
        raise ValueError(f"section map invalid: missing={missing}, duplicates={duplicates}, unknown={unknown}")

    lines = [
        "# Awesome Legal Benchmarks",
        "",
        "<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->",
        "",
        "[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re) [![Validate catalog](https://github.com/narcolepticchicken/awesome-legal-benchmarks/actions/workflows/validate.yml/badge.svg)](https://github.com/narcolepticchicken/awesome-legal-benchmarks/actions/workflows/validate.yml)",
        "",
        "Use this catalog to pick a legal benchmark and see what its score can actually support. Each entry records the task, jurisdiction, language, data, input/output contract, scorer, access terms, primary sources, and the biggest validity problem.",
        "",
        f"**Snapshot {catalog['as_of']}:** {len(entries)} canonical entries · [all 22 source bullets audited](docs/source-audit.md) (21 identities; MLEB appeared twice) · [{unique_resource_count} canonical URLs checked](catalog/resource-snapshot.json)",
        "",
        "> Start with the legal job. Then check jurisdiction, source material, interface, scorer, and prior exposure. If those do not match the system you care about, the score is weak evidence.",
        "",
        "## Contents",
        "",
        "- [Choose a benchmark](#choose-a-benchmark)",
        "- [Browse the catalog](#browse-the-catalog)",
        "- [Read a score](#read-a-score)",
        "- [Use the data](#use-the-data)",
        "- [Contribute](#contribute)",
        "",
        "## Choose a benchmark",
        "",
        "1. Name the legal task, jurisdiction, language, and as-of date.",
        "2. Match the benchmark interface to the system: closed-book QA, retrieval, drafting, translation, or tool use.",
        "3. Inspect the split, scorer, judge, and public-label exposure before comparing models.",
        "4. Pair public comparison data with a fresh, matter-specific holdout when the decision matters.",
        "",
        "The [selection guide](docs/selection-guide.md) has the full recommendation matrix. These are the fastest starting points:",
        "",
        "| Use case | Start with | Main caution |",
        "|---|---|---|",
    ]
    for use_case, picks, note in QUICK_PICKS:
        lines.append(f"| {use_case} | {quick_pick_links(picks)} | {note} |")
    lines += [
        "",
        "## Browse the catalog",
        "",
        "Dumping 45 full profiles into one README is hard to use. This rebuild leads with the practical choice. The category pages keep claims tied to primary sources and expose the validity and contamination limits.",
        "",
        "| Area | What is inside | Entries |",
        "|---|---|---:|",
    ]
    for slug, title, description, section_ids in SECTIONS:
        lines.append(f"| [{title}](docs/benchmarks/{slug}.md) | {description} | {len(section_ids)} |")
    lines += [
        "",
        "See the [compact 45-entry index](docs/catalog.md), or filter the machine-readable [JSON](catalog/benchmarks.json) and [CSV](catalog/benchmarks.csv).",
        "",
        "A catalog label is a curation judgment, not a leaderboard rank:",
        "",
        "| Label | Meaning |",
        "|---|---|",
        "| **recommended** | Clear task contract, primary artifacts, and comparatively strong reproducibility for its class. |",
        "| **specialist** | Useful within a narrower task, jurisdiction, language, or protocol. |",
        "| **check before use** | Real artifact with a material judge, vendor, split, license, access, or validity issue. |",
        "| **related artifact** | Dataset, framework, protocol, private test, or resource list. It is included so it is not mistaken for a comparable public benchmark. |",
        "",
        "Artifact type is tracked separately. A dataset is not automatically a benchmark, and an evaluation framework does not define a fixed test. The [methodology](docs/methodology.md) explains the inclusion rule and evidence labels.",
        "",
        "## Read a score",
        "",
        "Before repeating a benchmark number, answer five questions:",
        "",
        "1. What capability does success require, and what shortcut could produce the same score?",
        "2. Which jurisdiction, language, source population, and time period does the sample cover?",
        "3. What did the model receive, and what exact output did the scorer parse?",
        "4. How are item scores aggregated? What uncertainty, subgroup, abstention, and failure counts are missing?",
        "5. Were the questions, answers, documents, rubrics, or judge outputs exposed during training or development?",
        "",
        "The [metric field guide](docs/metric-theory.md) gives the formulas and failure modes for accuracy, F-scores, retrieval metrics, overlap metrics, LLM judges, rubric scores, and benchmark-specific composites. It also breaks down LawBench's 20-task score map, LEXTREME's hierarchical harmonic mean, JUST-NLP AutoRank, KCL essay scoring, DeonticBench bootstrapping, and Ready Jurist One's dual scoring.",
        "",
        "## Use the data",
        "",
        "| Need | File |",
        "|---|---|",
        "| Canonical source of truth | [`catalog/benchmarks.json`](catalog/benchmarks.json) |",
        "| Flat spreadsheet view | [`catalog/benchmarks.csv`](catalog/benchmarks.csv) |",
        "| Every GitHub, Hugging Face, paper, project, and leaderboard URL | [`catalog/resources.csv`](catalog/resources.csv) |",
        "| URL verification result | [`catalog/resource-snapshot.json`](catalog/resource-snapshot.json) |",
        "| Original 22-bullet reconstruction | [`docs/source-audit.md`](docs/source-audit.md) |",
        "| Releases that need more evidence | [`docs/watchlist.md`](docs/watchlist.md) |",
        "| Formatted workbook | [`outputs/awesome-legal-benchmarks.xlsx`](outputs/awesome-legal-benchmarks.xlsx) |",
        "",
        "Resource counts in this snapshot: "
        f"{resource_counts['github']} GitHub · {resource_counts['huggingface']} Hugging Face · "
        f"{resource_counts['papers']} papers · {resource_counts['leaderboards']} leaderboards or competitions · "
        f"{resource_counts['project']} project pages.",
        "",
        "Validate or regenerate the derived files:",
        "",
        "```bash",
        "python scripts/validate_catalog.py",
        "python -m unittest discover -s tests -v",
        "python scripts/generate_catalog.py --check",
        "python scripts/check_resources.py --check-snapshot",
        "```",
        "",
        "## Contribute",
        "",
        "Read [CONTRIBUTING.md](CONTRIBUTING.md). A proposed entry needs direct primary links, a defined evaluation contract, data provenance, access and license terms, and a concrete leakage or validity analysis. A marketing page by itself does not clear that bar.",
        "",
        "## License",
        "",
        "Catalog prose and structured metadata use [CC BY 4.0](LICENSE). Validation and generation code use [MIT](LICENSE-CODE). Linked datasets and repositories keep their own licenses.",
        "",
    ]
    return "\n".join(lines)


def generate_catalog_doc(catalog: dict) -> str:
    entries = {entry["id"]: entry for entry in catalog["entries"]}
    lines = [
        "# Legal benchmark catalog",
        "",
        "<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->",
        "",
        f"Snapshot: **{catalog['as_of']}**. This is the compact index for all {len(entries)} canonical entries. Each name links to a full profile with the evaluation contract, direct artifacts, reproducibility notes, verified facts, inference, and unresolved ambiguity.",
        "",
        "[Choose a benchmark](selection-guide.md) · [Read the methodology](methodology.md) · [Understand the metrics](metric-theory.md) · [Back to README](../README.md)",
        "",
        "## Areas",
        "",
        "| Area | Scope | Entries |",
        "|---|---|---:|",
    ]
    for slug, title, description, section_ids in SECTIONS:
        lines.append(f"| [{title}](benchmarks/{slug}.md) | {description} | {len(section_ids)} |")
    lines += [
        "",
        "## All entries",
        "",
        "The `kind` field distinguishes benchmarks, datasets, shared tasks, frameworks, protocols, private tests, and resource lists. The `label` field is the catalog's reproducibility and usefulness judgment. They answer different questions.",
        "",
    ]
    for slug, title, description, section_ids in SECTIONS:
        lines += [
            f"### {title}",
            "",
            description,
            "",
            "| Entry | Kind | Label | Jurisdiction / language | Measures |",
            "|---|---|---|---|---|",
        ]
        for entry_id in section_ids:
            entry = entries[entry_id]
            coverage = f"{', '.join(entry['jurisdictions'])}; {', '.join(entry['languages'])}"
            href = profile_href(entry_id, from_root=False)
            lines.append(
                f"| [{entry['name']}]({href}) | {entry['kind']} | {TIER_LABELS[entry['tier']]} | "
                f"{coverage} | {entry['capability']} |"
            )
        lines.append("")
    return "\n".join(lines)


def generate_category_doc(
    catalog: dict,
    slug: str,
    title: str,
    description: str,
    section_ids: list[str],
) -> str:
    entries = {entry["id"]: entry for entry in catalog["entries"]}
    lines = [
        f"# {title}",
        "",
        "<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->",
        "",
        description,
        "",
        f"Snapshot: **{catalog['as_of']}** · {len(section_ids)} entries",
        "",
        "[Catalog index](../catalog.md) · [Selection guide](../selection-guide.md) · [Metric field guide](../metric-theory.md) · [Methodology](../methodology.md)",
        "",
        "## On this page",
        "",
    ]
    lines += [f"- [{entries[entry_id]['name']}](#{entry_id})" for entry_id in section_ids]
    lines.append("")

    for entry_id in section_ids:
        entry = entries[entry_id]
        lines += [
            f'<a id="{entry_id}"></a>',
            f"## {entry['name']}",
            "",
            f"`{entry['id']}` · **{entry['kind']}** · **{TIER_LABELS[entry['tier']]}** · {entry['status']}",
            "",
            entry["capability"],
            "",
            "### Evaluation contract",
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
            lines.append(f"- **{metric['name']}:** {metric['protocol']}{judge}{primary}")
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
        lines += ["", f"Original source bullet(s): {source or 'Curated addition.'}", "", "[Back to page index](#on-this-page)", ""]
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
    path.parent.mkdir(parents=True, exist_ok=True)
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
    for slug, title, description, section_ids in SECTIONS:
        update(
            ROOT / "docs" / "benchmarks" / f"{slug}.md",
            generate_category_doc(catalog, slug, title, description, section_ids),
            args.check,
        )
    update(ROOT / "catalog" / "benchmarks.csv", render_csv(headers, rows), args.check)
    update(ROOT / "catalog" / "resources.csv", render_csv(resource_headers, resource_rows), args.check)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
