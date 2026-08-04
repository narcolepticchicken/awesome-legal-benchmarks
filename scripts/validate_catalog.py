#!/usr/bin/env python3
"""Validate the source-of-truth legal benchmark catalog without dependencies."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "benchmarks.json"

ENTRY_KEYS = {
    "id", "name", "aliases", "kind", "tier", "status", "categories",
    "capability", "construct", "jurisdictions", "languages", "data",
    "metrics", "baselines", "resources", "access", "maintenance",
    "reproducibility", "risks", "evidence", "source_readme_bullets",
    "curated_addition",
}
KINDS = {
    "benchmark", "dataset", "benchmark-suite", "shared-task",
    "evaluation-framework", "evaluation-protocol", "private-benchmark",
    "resource-list",
}
TIERS = {"recommended", "specialist", "evaluate-carefully", "related"}
STATUSES = {"active", "fixed-release", "annual", "completed", "private", "stale", "unclear"}
RESOURCE_KEYS = {"github", "huggingface", "papers", "leaderboards", "project"}
DATA_KEYS = {"size", "splits", "source", "input", "output"}
EVIDENCE_KEYS = {"verified", "inference", "ambiguities"}
ACCESS_KEYS = {"dataset", "license", "gating"}
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def load_catalog(path: Path = CATALOG) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def _nonempty_text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _check_url(url: object, label: str, errors: list[str]) -> None:
    if not isinstance(url, str):
        errors.append(f"{label}: URL must be a string")
        return
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.netloc:
        errors.append(f"{label}: URL must be direct HTTPS: {url!r}")
    if "google.com/search" in url or "github.com/search" in url:
        errors.append(f"{label}: search-result URLs are not canonical resources: {url}")


def validate(catalog: dict) -> list[str]:
    errors: list[str] = []
    if catalog.get("schema_version") != 1:
        errors.append("schema_version must equal 1")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(catalog.get("as_of", ""))):
        errors.append("as_of must be YYYY-MM-DD")
    if not _nonempty_text(catalog.get("selection_policy")):
        errors.append("selection_policy must be non-empty")
    entries = catalog.get("entries")
    if not isinstance(entries, list) or not entries:
        return errors + ["entries must be a non-empty array"]

    ids: list[str] = []
    names: list[str] = []
    url_owners: dict[str, list[str]] = defaultdict(list)
    bullet_owners: dict[int, list[str]] = defaultdict(list)

    for index, entry in enumerate(entries):
        prefix = f"entries[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{prefix}: must be an object")
            continue
        missing = ENTRY_KEYS - set(entry)
        extra = set(entry) - ENTRY_KEYS
        if missing:
            errors.append(f"{prefix}: missing keys {sorted(missing)}")
        if extra:
            errors.append(f"{prefix}: unknown keys {sorted(extra)}")
        entry_id = entry.get("id")
        if not isinstance(entry_id, str) or not SLUG_RE.fullmatch(entry_id):
            errors.append(f"{prefix}.id: invalid slug {entry_id!r}")
            entry_id = prefix
        ids.append(entry_id)
        name = entry.get("name")
        if not _nonempty_text(name):
            errors.append(f"{entry_id}.name: must be non-empty")
        else:
            names.append(name.casefold())
        if entry.get("kind") not in KINDS:
            errors.append(f"{entry_id}.kind: invalid value {entry.get('kind')!r}")
        if entry.get("tier") not in TIERS:
            errors.append(f"{entry_id}.tier: invalid value {entry.get('tier')!r}")
        if entry.get("status") not in STATUSES:
            errors.append(f"{entry_id}.status: invalid value {entry.get('status')!r}")
        for field in ("capability", "construct", "baselines", "maintenance", "reproducibility"):
            if not _nonempty_text(entry.get(field)):
                errors.append(f"{entry_id}.{field}: must be non-empty")
        for field in ("aliases", "categories", "jurisdictions", "languages", "risks"):
            value = entry.get(field)
            if not isinstance(value, list) or (field != "aliases" and not value):
                errors.append(f"{entry_id}.{field}: must be a {'non-empty ' if field != 'aliases' else ''}list")
            elif len(value) != len(set(map(str, value))):
                errors.append(f"{entry_id}.{field}: contains duplicates")

        data = entry.get("data")
        if not isinstance(data, dict) or set(data) != DATA_KEYS:
            errors.append(f"{entry_id}.data: expected exactly {sorted(DATA_KEYS)}")
        else:
            for field, value in data.items():
                if not _nonempty_text(value):
                    errors.append(f"{entry_id}.data.{field}: must be non-empty")

        metrics = entry.get("metrics")
        if not isinstance(metrics, list) or not metrics:
            errors.append(f"{entry_id}.metrics: must be a non-empty list")
        else:
            for metric_index, metric in enumerate(metrics):
                mlabel = f"{entry_id}.metrics[{metric_index}]"
                if not isinstance(metric, dict) or not {"name", "protocol"} <= set(metric):
                    errors.append(f"{mlabel}: requires name and protocol")
                    continue
                if set(metric) - {"name", "protocol", "judge", "primary"}:
                    errors.append(f"{mlabel}: contains unknown keys")
                if not _nonempty_text(metric.get("name")) or not _nonempty_text(metric.get("protocol")):
                    errors.append(f"{mlabel}: name and protocol must be non-empty")
                if "primary" in metric and not isinstance(metric["primary"], bool):
                    errors.append(f"{mlabel}.primary: must be boolean")

        resources = entry.get("resources")
        if not isinstance(resources, dict) or set(resources) != RESOURCE_KEYS:
            errors.append(f"{entry_id}.resources: expected exactly {sorted(RESOURCE_KEYS)}")
        else:
            if not any(resources.values()):
                errors.append(f"{entry_id}.resources: at least one primary resource is required")
            for resource_type, urls in resources.items():
                if not isinstance(urls, list):
                    errors.append(f"{entry_id}.resources.{resource_type}: must be a list")
                    continue
                if len(urls) != len(set(map(str, urls))):
                    errors.append(f"{entry_id}.resources.{resource_type}: duplicate URL")
                for url in urls:
                    _check_url(url, f"{entry_id}.resources.{resource_type}", errors)
                    if isinstance(url, str):
                        url_owners[url].append(entry_id)
                        host = urlparse(url).netloc.casefold()
                        if resource_type == "github" and host != "github.com":
                            errors.append(f"{entry_id}: non-GitHub URL in github resources: {url}")
                        if resource_type == "huggingface" and host != "huggingface.co":
                            errors.append(f"{entry_id}: non-HF URL in huggingface resources: {url}")

        access = entry.get("access")
        if not isinstance(access, dict) or set(access) != ACCESS_KEYS:
            errors.append(f"{entry_id}.access: expected exactly {sorted(ACCESS_KEYS)}")
        evidence = entry.get("evidence")
        if not isinstance(evidence, dict) or set(evidence) != EVIDENCE_KEYS:
            errors.append(f"{entry_id}.evidence: expected exactly {sorted(EVIDENCE_KEYS)}")
        elif not isinstance(evidence["verified"], list) or not evidence["verified"]:
            errors.append(f"{entry_id}.evidence.verified: requires at least one verified fact")

        bullets = entry.get("source_readme_bullets")
        if not isinstance(bullets, list) or any(not isinstance(n, int) or not 1 <= n <= 22 for n in bullets):
            errors.append(f"{entry_id}.source_readme_bullets: invalid bullet list")
            bullets = []
        for bullet in bullets:
            bullet_owners[bullet].append(entry_id)
        expected_curated = not bool(bullets)
        if entry.get("curated_addition") is not expected_curated:
            errors.append(f"{entry_id}.curated_addition: must be {expected_curated}")

    for label, values in (("id", ids), ("name", names)):
        dupes = sorted(value for value, count in Counter(values).items() if count > 1)
        if dupes:
            errors.append(f"duplicate {label}s: {dupes}")
    missing_bullets = sorted(set(range(1, 23)) - set(bullet_owners))
    repeated_bullets = {n: owners for n, owners in bullet_owners.items() if len(owners) > 1}
    if missing_bullets:
        errors.append(f"source audit omits README bullets: {missing_bullets}")
    if repeated_bullets:
        errors.append(f"source README bullets assigned to multiple identities: {repeated_bullets}")
    if bullet_owners.get(3) != ["mleb"] or bullet_owners.get(20) != ["mleb"]:
        errors.append("README bullets 3 and 20 must both map to canonical identity mleb")

    # Shared URLs are valid for component suites; flag only surprising cross-identity reuse.
    permitted_shared = {
        "https://github.com/coastalcph/lex-glue",
        "https://huggingface.co/datasets/coastalcph/lex_glue",
        "https://arxiv.org/abs/2110.00976",
        "https://huggingface.co/datasets/theatticusproject/cuad-qa",
        "https://exploration-lab.github.io/IL-TUR/",
    }
    unexpected_shared = {
        url: owners for url, owners in url_owners.items()
        if len(set(owners)) > 1 and url not in permitted_shared
    }
    if unexpected_shared:
        errors.append(f"unexpected cross-identity resource reuse: {unexpected_shared}")
    return errors


def main() -> int:
    try:
        catalog = load_catalog()
    except (OSError, json.JSONDecodeError) as exc:
        print(f"catalog load failed: {exc}", file=sys.stderr)
        return 1
    errors = validate(catalog)
    if errors:
        print("Catalog validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Catalog valid: {len(catalog['entries'])} canonical entries; all 22 source bullets mapped.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
