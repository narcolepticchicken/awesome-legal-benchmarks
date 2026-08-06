#!/usr/bin/env python3
"""Validate the source-of-truth legal benchmark catalog without dependencies."""

from __future__ import annotations

import json
import re
import sys
from calendar import monthrange
from collections import Counter, defaultdict
from datetime import date as calendar_date
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "benchmarks.json"

ENTRY_KEYS = {
    "id", "name", "aliases", "kind", "tier", "status", "categories",
    "owner", "dates", "access_profile", "possible_uses", "related",
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
STATUSES = {"active", "fixed-release", "annual", "completed", "private", "archived", "stale", "unclear"}
RESOURCE_KEYS = {"github", "huggingface", "papers", "leaderboards", "project"}
DATA_KEYS = {"size", "splits", "source", "input", "output"}
EVIDENCE_KEYS = {"verified", "inference", "ambiguities"}
ACCESS_KEYS = {"dataset", "license", "gating"}
OWNER_KEYS = {"name", "type", "commercial_interest"}
OWNER_TYPES = {"academic", "company", "nonprofit", "competition", "community", "mixed", "individual", "government", "unknown"}
COMMERCIAL_INTEREST = {"yes", "no", "unclear"}
DATES_KEYS = {"created", "last_updated"}
DATE_KEYS = {"date", "precision", "basis", "source"}
DATE_PRECISIONS = {"year", "month", "day"}
ACCESS_PROFILE_KEYS = {"level", "test_labels", "runnable"}
ACCESS_LEVELS = {"open", "gated", "partial", "private", "not-applicable"}
TEST_LABEL_ACCESS = {"public", "hidden", "mixed", "not-applicable", "unclear"}
RUNNABILITY = {"yes", "partial", "no", "not-applicable", "unclear"}
GEOGRAPHY_GROUP_KEYS = {"id", "name", "scope", "description", "entries"}
GEOGRAPHY_SCOPES = {
    "united-states", "multi-jurisdiction", "international", "undisclosed",
    "no-fixed-population",
}
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
PARTIAL_DATE_RE = re.compile(r"^\d{4}(?:-\d{2}(?:-\d{2})?)?$")


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


def _check_date_record(value: object, label: str, errors: list[str]) -> None:
    if not isinstance(value, dict) or set(value) != DATE_KEYS:
        errors.append(f"{label}: expected exactly {sorted(DATE_KEYS)}")
        return
    date = value.get("date")
    precision = value.get("precision")
    if not isinstance(date, str) or not PARTIAL_DATE_RE.fullmatch(date):
        errors.append(f"{label}.date: expected YYYY, YYYY-MM, or YYYY-MM-DD")
    if precision not in DATE_PRECISIONS:
        errors.append(f"{label}.precision: invalid value {precision!r}")
    elif isinstance(date, str):
        expected_parts = {"year": 1, "month": 2, "day": 3}[precision]
        if len(date.split("-")) != expected_parts:
            errors.append(f"{label}: date {date!r} does not match {precision!r} precision")
        elif _date_bounds(value) is None:
            errors.append(f"{label}.date: invalid calendar date {date!r}")
    if not _nonempty_text(value.get("basis")):
        errors.append(f"{label}.basis: must be non-empty")
    _check_url(value.get("source"), f"{label}.source", errors)


def _date_bounds(value: object) -> tuple[calendar_date, calendar_date] | None:
    if not isinstance(value, dict):
        return None
    text = value.get("date")
    precision = value.get("precision")
    if not isinstance(text, str) or precision not in DATE_PRECISIONS:
        return None
    try:
        parts = [int(part) for part in text.split("-")]
        if precision == "year" and len(parts) == 1:
            year = parts[0]
            return calendar_date(year, 1, 1), calendar_date(year, 12, 31)
        if precision == "month" and len(parts) == 2:
            year, month = parts
            return (
                calendar_date(year, month, 1),
                calendar_date(year, month, monthrange(year, month)[1]),
            )
        if precision == "day" and len(parts) == 3:
            day = calendar_date(*parts)
            return day, day
    except (TypeError, ValueError):
        return None
    return None


def validate(catalog: dict) -> list[str]:
    errors: list[str] = []
    if catalog.get("schema_version") != 3:
        errors.append("schema_version must equal 3")
    as_of_text = str(catalog.get("as_of", ""))
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", as_of_text):
        errors.append("as_of must be YYYY-MM-DD")
        as_of_date = None
    else:
        try:
            as_of_date = calendar_date.fromisoformat(as_of_text)
        except ValueError:
            errors.append("as_of must be a valid calendar date")
            as_of_date = None
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
        owner = entry.get("owner")
        if not isinstance(owner, dict) or set(owner) != OWNER_KEYS:
            errors.append(f"{entry_id}.owner: expected exactly {sorted(OWNER_KEYS)}")
        else:
            if not _nonempty_text(owner.get("name")):
                errors.append(f"{entry_id}.owner.name: must be non-empty")
            if owner.get("type") not in OWNER_TYPES:
                errors.append(f"{entry_id}.owner.type: invalid value {owner.get('type')!r}")
            if owner.get("commercial_interest") not in COMMERCIAL_INTEREST:
                errors.append(f"{entry_id}.owner.commercial_interest: invalid value {owner.get('commercial_interest')!r}")

        dates = entry.get("dates")
        if not isinstance(dates, dict) or set(dates) != DATES_KEYS:
            errors.append(f"{entry_id}.dates: expected exactly {sorted(DATES_KEYS)}")
        else:
            _check_date_record(dates.get("created"), f"{entry_id}.dates.created", errors)
            if dates.get("last_updated") is not None:
                _check_date_record(dates.get("last_updated"), f"{entry_id}.dates.last_updated", errors)
            created_bounds = _date_bounds(dates.get("created"))
            updated_bounds = _date_bounds(dates.get("last_updated"))
            if as_of_date is not None and created_bounds is not None and created_bounds[0] > as_of_date:
                errors.append(f"{entry_id}.dates.created: date begins after catalog as_of")
            if as_of_date is not None and updated_bounds is not None and updated_bounds[0] > as_of_date:
                errors.append(f"{entry_id}.dates.last_updated: date begins after catalog as_of")
            if created_bounds is not None and updated_bounds is not None and updated_bounds[1] < created_bounds[0]:
                errors.append(f"{entry_id}.dates.last_updated: date is before creation")

        access_profile = entry.get("access_profile")
        if not isinstance(access_profile, dict) or set(access_profile) != ACCESS_PROFILE_KEYS:
            errors.append(f"{entry_id}.access_profile: expected exactly {sorted(ACCESS_PROFILE_KEYS)}")
        else:
            if access_profile.get("level") not in ACCESS_LEVELS:
                errors.append(f"{entry_id}.access_profile.level: invalid value {access_profile.get('level')!r}")
            if access_profile.get("test_labels") not in TEST_LABEL_ACCESS:
                errors.append(f"{entry_id}.access_profile.test_labels: invalid value {access_profile.get('test_labels')!r}")
            if access_profile.get("runnable") not in RUNNABILITY:
                errors.append(f"{entry_id}.access_profile.runnable: invalid value {access_profile.get('runnable')!r}")

        possible_uses = entry.get("possible_uses")
        if not isinstance(possible_uses, list) or not 1 <= len(possible_uses) <= 3:
            errors.append(f"{entry_id}.possible_uses: requires one to three items")
        elif any(not _nonempty_text(item) for item in possible_uses):
            errors.append(f"{entry_id}.possible_uses: every item must be non-empty")

        related = entry.get("related")
        if not isinstance(related, list):
            errors.append(f"{entry_id}.related: must be a list")
        elif len(related) != len(set(map(str, related))):
            errors.append(f"{entry_id}.related: contains duplicates")
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

    known_ids = set(ids)
    geography_groups = catalog.get("geography_groups")
    geography_ids: list[str] = []
    geography_entries: list[str] = []
    if not isinstance(geography_groups, list) or not geography_groups:
        errors.append("geography_groups must be a non-empty list")
    else:
        for index, group in enumerate(geography_groups):
            label = f"geography_groups[{index}]"
            if not isinstance(group, dict) or set(group) != GEOGRAPHY_GROUP_KEYS:
                errors.append(f"{label}: expected exactly {sorted(GEOGRAPHY_GROUP_KEYS)}")
                continue
            group_id = group.get("id")
            if not isinstance(group_id, str) or not SLUG_RE.fullmatch(group_id):
                errors.append(f"{label}.id: invalid slug {group_id!r}")
            else:
                geography_ids.append(group_id)
            if not _nonempty_text(group.get("name")):
                errors.append(f"{label}.name: must be non-empty")
            if not _nonempty_text(group.get("description")):
                errors.append(f"{label}.description: must be non-empty")
            if group.get("scope") not in GEOGRAPHY_SCOPES:
                errors.append(f"{label}.scope: invalid value {group.get('scope')!r}")
            group_entries = group.get("entries")
            if not isinstance(group_entries, list) or not group_entries:
                errors.append(f"{label}.entries: must be a non-empty list")
                continue
            if len(group_entries) != len(set(map(str, group_entries))):
                errors.append(f"{label}.entries: contains duplicates")
            for entry_id in group_entries:
                if not isinstance(entry_id, str) or not SLUG_RE.fullmatch(entry_id):
                    errors.append(f"{label}.entries: invalid identity {entry_id!r}")
                geography_entries.append(entry_id)
        duplicate_groups = sorted(
            group_id for group_id, count in Counter(geography_ids).items() if count > 1
        )
        if duplicate_groups:
            errors.append(f"duplicate geography group ids: {duplicate_groups}")
        geography_counts = Counter(geography_entries)
        duplicate_assignments = {
            entry_id: count for entry_id, count in geography_counts.items() if count > 1
        }
        if duplicate_assignments:
            errors.append(
                f"entries assigned to multiple geography groups: {duplicate_assignments}"
            )
        missing_geography = sorted(known_ids - set(geography_entries))
        unknown_geography = sorted(set(geography_entries) - known_ids)
        if missing_geography:
            errors.append(f"entries missing geography assignment: {missing_geography}")
        if unknown_geography:
            errors.append(f"geography groups contain unknown identities: {unknown_geography}")

    entries_by_id = {
        entry["id"]: entry for entry in entries
        if isinstance(entry, dict) and isinstance(entry.get("id"), str)
    }
    for entry_id, entry in entries_by_id.items():
        for related_id in entry.get("related", []):
            if related_id == entry_id:
                errors.append(f"{entry_id}.related: cannot reference itself")
            elif related_id not in known_ids:
                errors.append(f"{entry_id}.related: unknown identity {related_id!r}")
            elif entry_id not in entries_by_id[related_id].get("related", []):
                errors.append(f"{entry_id}.related: relationship with {related_id!r} must be bidirectional")

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
