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
        ["legalbench", "lawbench", "lexeval", "lexglue", "lextreme", "lexam", "arablegaleval", "alarb", "il-tur", "kcl", "prbench", "plawbench", "lexgenius", "pilot-bench", "mozip"],
    ),
    (
        "retrieval-rag-citation",
        "Retrieval, RAG, and citation",
        "Authority retrieval, exact-support retrieval, case similarity, citation grounding, and end-to-end legal RAG.",
        ["mleb", "legalbench-rag", "bsard", "lleqa", "blleqa", "clerc", "reglab-reasoning-focused-retrieval", "lecardv2", "coliee", "legal-rag-bench", "canlegalragbench", "jurifindit", "ilsic", "rod-tal", "open-legal-answer-benchmark", "legalcitebench", "legal-phantom-citation", "reglab-legal-hallucinations", "reglab-legal-rag-hallucinations", "vals-legal-research-bench", "vals-caselaw-v2"],
    ),
    (
        "contracts-deal-work",
        "Contracts and deal work",
        "Clause extraction, provision classification, entailment, retrieval, merger agreements, and redlining.",
        ["cuad", "ledgar", "contractnli", "maud", "acord", "contracteval", "redlinebench", "legalon-contract-review-2026", "ivo-contract-review-study", "legalbenchmarks-ai"],
    ),
    (
        "prediction-fairness-rules",
        "Prediction, fairness, and structured reasoning",
        "Outcome prediction, subgroup performance, holding selection, deontic rules, and structured legal analysis.",
        ["ecthr", "fairlex", "casehold", "deonticbench", "mslr", "maslegalbench", "openexempt"],
    ),
    (
        "agents-workflows",
        "Agents and legal workflows",
        "Tool use, process compliance, simulated legal work, and long-horizon professional tasks.",
        ["legalagentbench", "ready-jurist-one", "harvey-lab", "apex-agents-corporate-law", "dlawbench", "harvey-biglaw-bench", "legora-bar", "gc-ai-in-house-legal-bench", "thomson-reuters-cocobench"],
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
        ["legaleval-q", "lrage", "prinzbench", "awesome-legal-nlp"],
    ),
]

TIER_LABELS = {
    "recommended": "recommended",
    "specialist": "specialist",
    "evaluate-carefully": "check before use",
    "related": "related artifact",
}

USE_CASES = [
    ("Broad English legal reasoning", [("LegalBench", "legalbench"), ("LexGLUE", "lexglue"), ("PRBench legal", "prbench")], "Compare per-task reasoning and language-understanding scores, then test open professional analysis against granular criteria."),
    ("Chinese legal reasoning", [("LawBench", "lawbench"), ("LexEval", "lexeval"), ("LexGenius", "lexgenius"), ("PLawBench", "plawbench")], "Screen knowledge and reasoning broadly, then inspect open-ended consultation, case analysis, and drafting."),
    ("Arabic and Saudi legal work", [("ArabLegalEval", "arablegaleval"), ("ALARB", "alarb")], "Separate translated or synthetic tasks from Saudi case-based verdict, argument, and statutory-article tasks."),
    ("Multilingual legal NLU", [("LEXTREME", "lextreme"), ("IL-TUR", "il-tur")], "Compare per-language and per-task behavior before relying on an aggregate multilingual score."),
    ("Italian and Indian statutory retrieval", [("JuriFindIT", "jurifindit"), ("ILSIC", "ilsic")], "Test expert Italian article retrieval and Indian statute identification from layperson queries; keep synthetic and court-derived training sources separate."),
    ("Patent and intellectual-property work", [("PILOT-Bench", "pilot-bench"), ("MoZIP", "mozip")], "Compare US patent-appeal classification with multilingual IP knowledge, open QA, and patent-semantic matching; neither substitutes for a private drafting or validity-review holdout."),
    ("Multimodal legal education", [("RoD-TAL", "rod-tal")], "Test Romanian traffic-law retrieval and QA when images or signs are legally material."),
    ("Contract extraction and classification", [("CUAD", "cuad"), ("ContractNLI", "contractnli"), ("MAUD", "maud")], "Test clause finding, evidence entailment, and merger-agreement provision classification on document-family-held-out data."),
    ("Contract retrieval", [("ACORD", "acord")], "Rank clauses against attorney-authored requests using graded relevance judgments."),
    ("Redlining and contract review", [("RedlineBench", "redlinebench"), ("LegalOn 2026", "legalon-contract-review-2026"), ("Ivo study", "ivo-contract-review-study"), ("legalbenchmarks.ai", "legalbenchmarks-ai")], "Test native-file edits, issue spotting, formatting retention, and review usefulness; only RedlineBench is openly runnable."),
    ("Legal retrieval and RAG", [("LegalBench-RAG", "legalbench-rag"), ("RegLab retrieval", "reglab-reasoning-focused-retrieval"), ("bLLeQA", "blleqa"), ("Legal RAG Bench", "legal-rag-bench"), ("CanLegalRAGBench", "canlegalragbench")], "Measure authority retrieval, answer correctness, citation extraction, refusal, and grounding separately on a jurisdiction-matched corpus."),
    ("Citation safety", [("LegalCiteBench", "legalcitebench"), ("Legal Phantom Citation", "legal-phantom-citation"), ("Large Legal Fictions", "reglab-legal-hallucinations"), ("Hallucination-Free?", "reglab-legal-rag-hallucinations")], "Test citation retrieval, abstention, phantom-citation detection, and human-coded research-tool hallucination as distinct failure modes."),
    ("Long-horizon legal agents", [("DLawBench", "dlawbench"), ("Harvey LAB", "harvey-lab"), ("Legora BAR", "legora-bar"), ("Mercor APEX legal", "apex-agents-corporate-law")], "Evaluate consultation or matter completion with files, tools, rubrics, repeated runs, cost, and latency; BAR's full instrument is private."),
    ("In-house legal work", [("GC AI In-House Legal Bench", "gc-ai-in-house-legal-bench"), ("CoCoBench", "thomson-reuters-cocobench"), ("Harvey BigLaw Bench", "harvey-biglaw-bench")], "Use their task taxonomies and published results as private-vendor evidence when designing an internal matter-level holdout."),
    ("Rule and robustness testing", [("DeonticBench", "deonticbench"), ("OpenExempt", "openexempt")], "Test deontic consistency and symbolic statutory reasoning under controlled perturbations."),
    ("Fairness and subgroup performance", [("FairLex", "fairlex")], "Compare overall, per-group, worst-group, and gap metrics with group sizes and uncertainty."),
    ("Legal translation", [("SwiLTra-Bench", "swiltra-bench"), ("MILPaC", "milpac"), ("JUST-NLP 2025", "just-nlp-2025-legal-mt")], "Compare automatic metrics with legal-expert ratings for terminology, omissions, and legal effect."),
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


def table_text(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", "<br>")


def date_link(record: dict | None) -> str:
    if record is None:
        return "No later update verified"
    return f"[{record['date']}]({record['source']}) — {table_text(record['basis'])}"


def owner_text(entry: dict) -> str:
    owner = entry["owner"]
    commercial = "; commercial interest" if owner["commercial_interest"] == "yes" else ""
    if owner["commercial_interest"] == "unclear":
        commercial = "; commercial interest unclear"
    return f"{table_text(owner['name'])} ({owner['type']}{commercial})"


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
        if urls:
            value = "<br>".join(f"[{url}]({url})" for url in urls)
            lines.append(f"| {label} | {value} |")
    return lines


def generate_readme(catalog: dict) -> str:
    entries = {entry["id"]: entry for entry in catalog["entries"]}
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
        f"**Research snapshot: {catalog['as_of']}.** {len(entries)} canonical identities, including public benchmarks, private vendor benchmarks, datasets, shared tasks, evaluation frameworks, protocols, and one resource list.",
        "",
        "> Start with the legal job. Then check jurisdiction, source material, interface, scorer, and prior exposure. If those do not match the system you care about, the score is weak evidence.",
        "",
        "## Contents",
        "",
        "- [Possible use cases](#possible-use-cases)",
        "- [Browse by area](#browse-by-area)",
        "- [What the labels mean](#what-the-labels-mean)",
        "- [Read a benchmark score](#read-a-benchmark-score)",
        "- [Files and methodology](#files-and-methodology)",
        "- [Contribute](#contribute)",
        "",
        "## Possible use cases",
        "",
        "These are starting points, not interchangeable leaderboards. Each use case names the legal work, the artifact to start with, and the decision its score can inform.",
        "",
        "| Legal work | Start with | Possible use cases |",
        "|---|---|---|",
    ]
    for legal_work, picks, uses in USE_CASES:
        lines.append(f"| {legal_work} | {quick_pick_links(picks)} | {uses} |")
    lines += [
        "",
        "Pair any public comparison with a fresh, matter-specific holdout before making a deployment or procurement decision. The [selection guide](docs/selection-guide.md) gives a fuller recommendation matrix.",
        "",
        "## Browse by area",
        "",
        "Each category page contains full profiles with owner, creation date, latest verified update, access boundary, metrics, direct official sources, possible uses, and unresolved facts.",
        "",
        "| Area | What is inside | Entries |",
        "|---|---|---:|",
    ]
    for slug, title, description, section_ids in SECTIONS:
        lines.append(f"| [{title}](docs/benchmarks/{slug}.md) | {description} | {len(section_ids)} |")
    lines += [
        "",
        f"See the [compact {len(entries)}-entry index](docs/catalog.md), or filter the machine-readable [JSON](catalog/benchmarks.json), [CSV](catalog/benchmarks.csv), and [workbook](outputs/awesome-legal-benchmarks.xlsx).",
        "",
        "## What the labels mean",
        "",
        "Artifact type and catalog label answer different questions. Public datasets may omit a fixed scorer. Frameworks supply evaluation runners or judge logic without fixed tests. Private vendor studies report evidence from owner-controlled instruments rather than public leaderboards.",
        "",
        "| Type | Meaning |",
        "|---|---|",
        "| **benchmark / benchmark suite** | Defines tasks, inputs, expected outputs, and scoring. A suite contains materially different tasks or datasets. |",
        "| **dataset** | Supplies evaluation material but may not fix a complete scoring protocol. |",
        "| **shared task** | Time-bounded competition with organizer-defined data, rules, and scoring. |",
        "| **evaluation framework / protocol** | Provides evaluation code, a judge, or a study method; results depend on the tasks and versions supplied. |",
        "| **private benchmark** | Important evaluation whose full tasks, labels, or scorer are unavailable for independent reproduction. |",
        "| **resource list** | Discovery aid, not a benchmark result. |",
        "",
        "A label is a curation judgment, not a model rank:",
        "",
        "| Label | Meaning |",
        "|---|---|",
        "| **recommended** | Clear task contract, primary artifacts, and comparatively strong reproducibility for its class. |",
        "| **specialist** | Useful within a narrower task, jurisdiction, language, or protocol. |",
        "| **check before use** | Real artifact with a material judge, vendor, split, license, access, or validity issue. |",
        "| **related artifact** | Dataset, framework, protocol, private test, or resource list. It is included so it is not mistaken for a comparable public benchmark. |",
        "",
        "The [methodology](docs/methodology.md) explains inclusion, date provenance, and the verified fact / inference / unresolved ambiguity labels.",
        "",
        "## Read a benchmark score",
        "",
        "Before repeating a benchmark number, answer five questions:",
        "",
        "1. What capability does success require, and what shortcut could produce the same score?",
        "2. Which jurisdiction, language, source population, and time period does the sample cover?",
        "3. What did the model receive, and what exact output did the scorer parse?",
        "4. How are item scores aggregated? What uncertainty, subgroup, abstention, and failure counts are missing?",
        "5. Were the questions, answers, documents, rubrics, or judge outputs exposed during training or development?",
        "",
        "The [metric field guide](docs/metric-theory.md) gives formulas and failure modes for accuracy, F-scores, retrieval metrics, overlap metrics, LLM judges, weighted rubrics, all-pass scores, and benchmark-specific composites. It includes the detailed LawBench breakdown requested for this project.",
        "",
        "## Files and methodology",
        "",
        "| Need | File |",
        "|---|---|",
        "| Canonical source of truth | [`catalog/benchmarks.json`](catalog/benchmarks.json) |",
        "| Flat spreadsheet view | [`catalog/benchmarks.csv`](catalog/benchmarks.csv) |",
        "| Every GitHub, Hugging Face, paper, project, and leaderboard URL | [`catalog/resources.csv`](catalog/resources.csv) |",
        "| URL verification result | [`catalog/resource-snapshot.json`](catalog/resource-snapshot.json) |",
        "| Original 22-bullet audit, including the duplicated MLEB rows | [`docs/source-audit.md`](docs/source-audit.md) |",
        "| Watchlist and deliberate non-additions | [`docs/watchlist.md`](docs/watchlist.md) |",
        "| Formatted workbook | [`outputs/awesome-legal-benchmarks.xlsx`](outputs/awesome-legal-benchmarks.xlsx) |",
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
            "| Entry | Owner | Kind / label | Access | Created | Latest update | Coverage | Measures |",
            "|---|---|---|---|---|---|---|---|",
        ]
        for entry_id in section_ids:
            entry = entries[entry_id]
            coverage = f"{', '.join(entry['jurisdictions'])}; {', '.join(entry['languages'])}"
            href = profile_href(entry_id, from_root=False)
            lines.append(
                f"| [{table_text(entry['name'])}]({href}) | {owner_text(entry)} | "
                f"{entry['kind']} / {TIER_LABELS[entry['tier']]} | {entry['access_profile']['level']} | "
                f"{date_link(entry['dates']['created'])} | {date_link(entry['dates']['last_updated'])} | "
                f"{table_text(coverage)} | {table_text(entry['capability'])} |"
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
        "[Back to README](../../README.md) · [Catalog index](../catalog.md) · [Selection guide](../selection-guide.md) · [Metric field guide](../metric-theory.md) · [Methodology](../methodology.md)",
        "",
        "## On this page",
        "",
    ]
    lines += [f"- [{entries[entry_id]['name']}](#{entry_id})" for entry_id in section_ids]
    lines.append("")

    for entry_id in section_ids:
        entry = entries[entry_id]
        aliases = ", ".join(entry["aliases"])
        lines += [
            f'<a id="{entry_id}"></a>',
            f"## {entry['name']}",
            "",
            f"`{entry['id']}` · **{entry['kind']}** · **{TIER_LABELS[entry['tier']]}** · {entry['status']}",
            "",
            entry["capability"],
            "",
        ]
        if aliases:
            lines += [f"**Also known as:** {aliases}", ""]
        lines += [
            "### Identity, dates, and access",
            "",
            "| Field | Detail |",
            "|---|---|",
            f"| Owner | {owner_text(entry)} |",
            f"| First documented | {date_link(entry['dates']['created'])} |",
            f"| Latest verified update | {date_link(entry['dates']['last_updated'])} |",
            f"| Access level | {entry['access_profile']['level']} |",
            f"| Test labels | {entry['access_profile']['test_labels']} |",
            f"| Independently runnable | {entry['access_profile']['runnable']} |",
            "",
            "### Possible use cases",
            "",
        ]
        lines += [f"- {item}" for item in entry["possible_uses"]]
        lines += [
            "",
            "### Evaluation contract",
            "",
            "| Field | Detail |",
            "|---|---|",
            f"| Construct / theory | {table_text(entry['construct'])} |",
            f"| Jurisdiction | {table_text(', '.join(entry['jurisdictions']))} |",
            f"| Languages | {table_text(', '.join(entry['languages']))} |",
            f"| Size | {table_text(entry['data']['size'])} |",
            f"| Splits | {table_text(entry['data']['splits'])} |",
            f"| Source material | {table_text(entry['data']['source'])} |",
            f"| Input | {table_text(entry['data']['input'])} |",
            f"| Output | {table_text(entry['data']['output'])} |",
            f"| Baselines / leaderboard context | {table_text(entry['baselines'])} |",
            f"| Dataset access | {table_text(entry['access']['dataset'])} |",
            f"| License | {table_text(entry['access']['license'])} |",
            f"| Gating | {table_text(entry['access']['gating'])} |",
            f"| Maintenance | {table_text(entry['maintenance'])} |",
            f"| Reproducibility | {table_text(entry['reproducibility'])} |",
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
        if entry["evidence"]["inference"]:
            lines += ["", "**Inference**"]
            lines += [f"- {item}" for item in entry["evidence"]["inference"]]
        if entry["evidence"]["ambiguities"]:
            lines += ["", "**Unresolved ambiguity**"]
            lines += [f"- {item}" for item in entry["evidence"]["ambiguities"]]
        if entry["related"]:
            lines += ["", "**Related entries**", ""]
            for related_id in entry["related"]:
                related = entries[related_id]
                related_slug = section_for(related_id)[0]
                lines.append(f"- [{related['name']}]({related_slug}.md#{related_id})")
        source = ", ".join(f"#{number}" for number in entry["source_readme_bullets"])
        if source:
            lines += ["", f"Original source bullet(s): {source}"]
        lines += ["", "[Back to page index](#on-this-page)", ""]
    return "\n".join(lines)


def csv_rows(catalog: dict) -> tuple[list[str], list[list[str]]]:
    headers = [
        "id", "name", "aliases", "owner", "owner_type", "commercial_interest",
        "created", "created_precision", "created_basis", "created_source",
        "last_updated", "last_updated_precision", "last_updated_basis", "last_updated_source",
        "kind", "tier", "status", "access_level", "test_labels", "runnable",
        "possible_uses", "related", "categories", "capability",
        "construct", "jurisdictions", "languages", "size", "splits", "source",
        "input", "output", "metrics", "baselines", "github", "huggingface",
        "papers", "leaderboards", "project", "dataset_access", "license", "gating",
        "maintenance", "reproducibility", "risks", "verified", "inference",
        "ambiguities", "source_readme_bullets", "curated_addition", "as_of",
    ]
    rows: list[list[str]] = []
    for entry in catalog["entries"]:
        created = entry["dates"]["created"]
        updated = entry["dates"]["last_updated"] or {}
        rows.append([
            entry["id"], entry["name"], " | ".join(entry["aliases"]),
            entry["owner"]["name"], entry["owner"]["type"], entry["owner"]["commercial_interest"],
            created["date"], created["precision"], created["basis"], created["source"],
            updated.get("date", ""), updated.get("precision", ""), updated.get("basis", ""), updated.get("source", ""),
            entry["kind"], entry["tier"], entry["status"],
            entry["access_profile"]["level"], entry["access_profile"]["test_labels"], entry["access_profile"]["runnable"],
            " | ".join(entry["possible_uses"]), " | ".join(entry["related"]),
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
