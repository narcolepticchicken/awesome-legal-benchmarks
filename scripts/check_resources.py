#!/usr/bin/env python3
"""Verify every canonical repository, dataset, paper, leaderboard, and project URL."""

from __future__ import annotations

import argparse
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalog" / "benchmarks.json"
SNAPSHOT_PATH = ROOT / "catalog" / "resource-snapshot.json"
USER_AGENT = "awesome-legal-benchmarks-resource-audit/1.0"


def load_catalog() -> dict:
    return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))


def expected_resources(catalog: dict) -> dict[str, dict]:
    resources: dict[str, dict] = {}
    for entry in catalog["entries"]:
        for family in ("github", "huggingface", "papers", "leaderboards", "project"):
            for url in entry["resources"].get(family, []):
                record = resources.setdefault(
                    url,
                    {"url": url, "kind": family, "families": [], "benchmark_ids": []},
                )
                if family not in record["families"]:
                    record["families"].append(family)
                if entry["id"] not in record["benchmark_ids"]:
                    record["benchmark_ids"].append(entry["id"])
    for record in resources.values():
        record["benchmark_ids"].sort()
        record["families"].sort()
    return resources


def request(url: str, *, accept_json: bool = False) -> tuple[int, str, object | None]:
    headers = {"User-Agent": USER_AGENT}
    if accept_json:
        headers["Accept"] = "application/json"
    github_token = os.environ.get("GITHUB_TOKEN")
    hf_token = os.environ.get("HF_TOKEN")
    if "api.github.com" in url and github_token:
        headers["Authorization"] = f"Bearer {github_token}"
    if "huggingface.co/api/" in url and hf_token:
        headers["Authorization"] = f"Bearer {hf_token}"
    req = Request(url, headers=headers, method="GET")
    with urlopen(req, timeout=25) as response:
        body = response.read() if accept_json else b""
        payload = json.loads(body.decode("utf-8")) if body else None
        return response.status, response.geturl(), payload


def check_github(record: dict) -> dict:
    parsed = urlparse(record["url"])
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 2:
        raise ValueError("GitHub URL does not identify owner/repository")
    owner, repository = parts[0], parts[1].removesuffix(".git")
    api_url = f"https://api.github.com/repos/{quote(owner)}/{quote(repository)}"
    status, _, payload = request(api_url, accept_json=True)
    assert isinstance(payload, dict)
    license_info = payload.get("license") or {}
    canonical = payload.get("html_url") or record["url"]
    return {
        **record,
        "ok": status == 200 and not payload.get("disabled", False),
        "verification_status": "available",
        "verification_method": "github-api",
        "http_status": status,
        "canonical_url": canonical,
        "api_url": api_url,
        "metadata": {
            "full_name": payload.get("full_name"),
            "private": payload.get("private"),
            "archived": payload.get("archived"),
            "disabled": payload.get("disabled"),
            "default_branch": payload.get("default_branch"),
            "pushed_at": payload.get("pushed_at"),
            "license_spdx": license_info.get("spdx_id"),
        },
        "error": None,
    }


def check_huggingface(record: dict) -> dict:
    parsed = urlparse(record["url"])
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) >= 3 and parts[0] == "datasets":
        dataset_id = "/".join(parts[1:3])
        api_url = f"https://huggingface.co/api/datasets/{quote(dataset_id, safe='/')}"
        status, _, payload = request(api_url, accept_json=True)
        assert isinstance(payload, dict)
        card_data = payload.get("cardData") or {}
        tags = payload.get("tags") or []
        licenses = sorted(
            {
                tag.split(":", 1)[1]
                for tag in tags
                if isinstance(tag, str) and tag.startswith("license:")
            }
        )
        if card_data.get("license") and card_data["license"] not in licenses:
            licenses.append(card_data["license"])
        return {
            **record,
            "ok": status == 200 and not payload.get("disabled", False),
            "verification_status": "available",
            "verification_method": "huggingface-api",
            "http_status": status,
            "canonical_url": f"https://huggingface.co/datasets/{payload.get('id', dataset_id)}",
            "api_url": api_url,
            "metadata": {
                "id": payload.get("id"),
                "private": payload.get("private"),
                "gated": payload.get("gated"),
                "disabled": payload.get("disabled"),
                "last_modified": payload.get("lastModified"),
                "downloads": payload.get("downloads"),
                "likes": payload.get("likes"),
                "licenses": licenses,
            },
            "error": None,
        }

    status, canonical, _ = request(record["url"], accept_json=False)
    subtype = "collection" if parts and parts[0] == "collections" else "namespace"
    return {
        **record,
        "ok": status == 200,
        "verification_status": "available",
        "verification_method": "http-get",
        "subtype": subtype,
        "http_status": status,
        "canonical_url": canonical,
        "api_url": None,
        "metadata": {},
        "error": None,
    }


def check_generic(record: dict) -> dict:
    parsed = urlparse(record["url"])
    if record["kind"] == "papers" and parsed.netloc.casefold() in {"doi.org", "dx.doi.org"}:
        doi = unquote(parsed.path.lstrip("/"))
        if not doi:
            raise ValueError("DOI URL does not identify a DOI")
        api_url = f"https://api.crossref.org/works/{quote(doi, safe='')}"
        status, _, payload = request(api_url, accept_json=True)
        assert isinstance(payload, dict) and isinstance(payload.get("message"), dict)
        message = payload["message"]
        title = message.get("title") or []
        return {
            **record,
            "ok": status == 200,
            "verification_status": "available",
            "verification_method": "crossref-api",
            "http_status": status,
            "canonical_url": message.get("URL") or record["url"],
            "api_url": api_url,
            "metadata": {
                "doi": message.get("DOI"),
                "title": title[0] if title else None,
                "publisher": message.get("publisher"),
                "work_type": message.get("type"),
            },
            "error": None,
        }

    status, canonical, _ = request(record["url"], accept_json=False)
    return {
        **record,
        "ok": 200 <= status < 400,
        "verification_status": "available",
        "verification_method": "http-get",
        "http_status": status,
        "canonical_url": canonical,
        "api_url": None,
        "metadata": {},
        "error": None,
    }


def check_one(record: dict) -> dict:
    try:
        if record["kind"] == "github":
            return check_github(record)
        if record["kind"] == "huggingface":
            return check_huggingface(record)
        return check_generic(record)
    except HTTPError as exc:
        access_limited = (
            record["kind"] in {"papers", "leaderboards", "project"}
            and exc.code in {401, 403}
        )
        return {
            **record,
            "ok": access_limited,
            "verification_status": "access-limited" if access_limited else "failed",
            "verification_method": "http-get",
            "http_status": exc.code,
            "canonical_url": record["url"] if access_limited else None,
            "api_url": exc.url,
            "metadata": {},
            "error": f"HTTP {exc.code}: {exc.reason}",
        }
    except (URLError, TimeoutError, ValueError, json.JSONDecodeError, AssertionError) as exc:
        return {
            **record,
            "ok": False,
            "verification_status": "failed",
            "verification_method": None,
            "http_status": None,
            "canonical_url": None,
            "api_url": None,
            "metadata": {},
            "error": f"{type(exc).__name__}: {exc}",
        }


def create_snapshot(catalog: dict, *, reuse_ok: bool = False) -> dict:
    expected = expected_resources(catalog)
    checked: list[dict] = []
    pending = dict(expected)
    if reuse_ok and SNAPSHOT_PATH.exists():
        previous = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
        reusable = {
            item["url"]: {
                **item,
                "kind": expected[item["url"]]["kind"],
                "families": expected[item["url"]]["families"],
                "benchmark_ids": expected[item["url"]]["benchmark_ids"],
                "verification_status": item.get("verification_status", "available"),
                "verification_method": item.get(
                    "verification_method",
                    "github-api" if expected[item["url"]]["kind"] == "github"
                    else "huggingface-api" if "/datasets/" in item["url"]
                    else "http-get",
                ),
            }
            for item in previous.get("resources", [])
            if item.get("ok") and item["url"] in expected
        }
        checked.extend(reusable.values())
        for url in reusable:
            pending.pop(url)
        print(f"reusing {len(reusable)} successful checks from the current snapshot")
    with ThreadPoolExecutor(max_workers=8) as executor:
        future_to_url = {
            executor.submit(check_one, record): url for url, record in pending.items()
        }
        for future in as_completed(future_to_url):
            result = future.result()
            checked.append(result)
            state = (
                "ok"
                if result.get("verification_status") == "available"
                else "LIMIT"
                if result.get("verification_status") == "access-limited"
                else "FAIL"
            )
            print(f"{state:4} {result['url']}")
    checked.sort(key=lambda item: (item["kind"], item["url"]))
    by_family = {}
    for kind in ("github", "huggingface", "papers", "leaderboards", "project"):
        family = [item for item in checked if kind in item["families"]]
        by_family[kind] = {
            "total": len(family),
            "available": sum(item.get("verification_status") == "available" for item in family),
            "access_limited": sum(item.get("verification_status") == "access-limited" for item in family),
            "failed": sum(not item["ok"] for item in family),
        }
    return {
        "schema_version": 2,
        "catalog_as_of": catalog["as_of"],
        "checked_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "scope": "Every canonical GitHub repository, Hugging Face artifact, paper, leaderboard, competition, and project URL in the catalog. API/HTTP availability verifies identity and access status, not scientific validity.",
        "summary": {
            "total": len(checked),
            "ok": sum(item["ok"] for item in checked),
            "available": sum(item.get("verification_status") == "available" for item in checked),
            "access_limited": sum(item.get("verification_status") == "access-limited" for item in checked),
            "failed": sum(not item["ok"] for item in checked),
            "by_family": by_family,
        },
        "resources": checked,
    }


def validate_snapshot(catalog: dict, snapshot: dict) -> list[str]:
    errors: list[str] = []
    expected = set(expected_resources(catalog))
    actual = {item["url"] for item in snapshot.get("resources", [])}
    if expected != actual:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        if missing:
            errors.append(f"snapshot missing {len(missing)} resources: {missing}")
        if extra:
            errors.append(f"snapshot has {len(extra)} stale resources: {extra}")
    if snapshot.get("catalog_as_of") != catalog.get("as_of"):
        errors.append("snapshot catalog_as_of does not match catalog")
    if snapshot.get("schema_version") != 2:
        errors.append("snapshot schema_version must equal 2")
    failures = [item for item in snapshot.get("resources", []) if not item.get("ok")]
    if failures:
        errors.append(
            "resource checks failed: "
            + ", ".join(f"{item['url']} ({item.get('error')})" for item in failures)
        )
    summary = snapshot.get("summary", {})
    if summary.get("total") != len(actual):
        errors.append("snapshot summary total is incorrect")
    if summary.get("failed") != len(failures):
        errors.append("snapshot summary failed count is incorrect")
    if summary.get("ok") != len(actual) - len(failures):
        errors.append("snapshot summary ok count is incorrect")
    expected_kinds = {record["kind"] for record in expected_resources(catalog).values()}
    actual_kinds = {item.get("kind") for item in snapshot.get("resources", [])}
    if expected_kinds != actual_kinds:
        errors.append(f"snapshot resource kinds are incomplete: {sorted(actual_kinds)}")
    expected_records = expected_resources(catalog)
    for item in snapshot.get("resources", []):
        expected_families = expected_records.get(item["url"], {}).get("families")
        if item.get("families") != expected_families:
            errors.append(f"snapshot resource families are incorrect for {item['url']}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check-snapshot",
        action="store_true",
        help="Validate the existing snapshot without making network requests.",
    )
    parser.add_argument(
        "--reuse-ok",
        action="store_true",
        help="Reuse successful records from the current snapshot and check only new/failed URLs.",
    )
    args = parser.parse_args()
    catalog = load_catalog()

    if args.check_snapshot:
        if not SNAPSHOT_PATH.exists():
            print(f"missing snapshot: {SNAPSHOT_PATH}", file=sys.stderr)
            return 1
        snapshot = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
    else:
        snapshot = create_snapshot(catalog, reuse_ok=args.reuse_ok)
        SNAPSHOT_PATH.write_text(
            json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    errors = validate_snapshot(catalog, snapshot)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        f"Resource snapshot valid: {snapshot['summary']['ok']}/"
        f"{snapshot['summary']['total']} canonical resources verified "
        f"({snapshot['summary']['access_limited']} access-limited)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
