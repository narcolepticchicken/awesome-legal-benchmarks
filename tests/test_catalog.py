import importlib.util
import json
import re
import unittest
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_catalog", ROOT / "scripts" / "validate_catalog.py"
)
VALIDATOR = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(VALIDATOR)


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "catalog" / "benchmarks.json").read_text())

    def test_catalog_contract(self):
        self.assertEqual([], VALIDATOR.validate(self.catalog))

    def test_snapshot_size_and_identity_count(self):
        self.assertEqual(89, len(self.catalog["entries"]))
        originals = [
            entry for entry in self.catalog["entries"] if entry["source_readme_bullets"]
        ]
        self.assertEqual(21, len(originals))

    def test_original_readme_coverage(self):
        bullets = [
            bullet
            for entry in self.catalog["entries"]
            for bullet in entry["source_readme_bullets"]
        ]
        self.assertEqual(list(range(1, 23)), sorted(bullets))

    def test_mleb_duplicate_is_one_identity(self):
        matches = [entry for entry in self.catalog["entries"] if entry["id"] == "mleb"]
        self.assertEqual(1, len(matches))
        self.assertEqual([3, 20], matches[0]["source_readme_bullets"])

    def test_requested_geography_and_date_structure(self):
        groups = {group["id"]: group for group in self.catalog["geography_groups"]}
        self.assertNotIn("dlawbench", groups["china"]["entries"])
        self.assertNotIn("legalbenchmarks-ai", groups["united-states"]["entries"])
        self.assertIn("dlawbench", groups["multi-jurisdiction"]["entries"])
        self.assertIn("legalbenchmarks-ai", groups["multi-jurisdiction"]["entries"])
        self.assertIn("vlegal-bench", groups["vietnam"]["entries"])
        self.assertIn("mizanqa", groups["morocco"]["entries"])
        for entry in self.catalog["entries"]:
            self.assertRegex(entry["dates"]["created"]["date"], r"^\d{4}")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("#### First recorded event in 2026", readme)
        self.assertLess(readme.index("## United States"), readme.index("## International by country"))

    def test_opus_candidates_were_independently_promoted_with_caveats(self):
        entries = {entry["id"]: entry for entry in self.catalog["entries"]}
        promoted = {
            "vlegal-bench", "mizanqa", "agb-de", "lexsumm", "courtreasoner",
            "lexrag", "predex", "legal-lens", "muser", "class-action-prediction",
        }
        self.assertTrue(promoted.issubset(entries))
        self.assertTrue(all(entries[entry_id]["risks"] for entry_id in promoted))
        self.assertEqual("evaluate-carefully", entries["prbench"]["tier"])
        self.assertEqual(
            ["https://github.com/reglab/casehold", "https://github.com/coastalcph/lex-glue"],
            entries["casehold"]["resources"]["github"],
        )

    def test_ar_bench_and_judge_are_not_conflated(self):
        entries = {entry["id"]: entry for entry in self.catalog["entries"]}
        self.assertNotIn("ar-bench", entries)
        self.assertIn("judge", entries)
        self.assertEqual(
            ["https://github.com/oneal2000/JuDGE"],
            entries["judge"]["resources"]["github"],
        )
        self.assertNotIn(
            "https://arxiv.org/abs/2601.22742",
            entries["judge"]["resources"]["papers"],
        )
        watchlist = (ROOT / "docs" / "watchlist.md").read_text(encoding="utf-8")
        self.assertIn("That negative search is not proof that no release exists.", watchlist)

    def test_every_material_entry_has_primary_source(self):
        for entry in self.catalog["entries"]:
            urls = sum(entry["resources"].values(), [])
            self.assertTrue(urls, entry["id"])

    def test_resource_snapshot_covers_every_canonical_url(self):
        snapshot = json.loads(
            (ROOT / "catalog" / "resource-snapshot.json").read_text()
        )
        expected = {
            url
            for entry in self.catalog["entries"]
            for family in ("github", "huggingface", "papers", "leaderboards", "project")
            for url in entry["resources"][family]
        }
        actual = {item["url"] for item in snapshot["resources"]}
        self.assertEqual(expected, actual)
        self.assertEqual(snapshot["summary"]["total"], len(actual))
        self.assertTrue(all(item["ok"] for item in snapshot["resources"]))
        expected_family_totals = {
            family: len(
                {
                    url
                    for entry in self.catalog["entries"]
                    for url in entry["resources"][family]
                }
            )
            for family in ("github", "huggingface", "papers", "leaderboards", "project")
        }
        self.assertEqual(
            expected_family_totals,
            {
                family: values["total"]
                for family, values in snapshot["summary"]["by_family"].items()
            },
        )

    def test_relative_markdown_links_resolve(self):
        link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
        for markdown_path in [ROOT / "README.md", *(ROOT / "docs").rglob("*.md")]:
            text = markdown_path.read_text(encoding="utf-8")
            for target in link_pattern.findall(text):
                if target.startswith(("https://", "http://", "mailto:", "#")):
                    continue
                relative_path = target.split("#", 1)[0]
                resolved = (markdown_path.parent / relative_path).resolve()
                self.assertTrue(
                    resolved.exists(),
                    f"broken local link in {markdown_path.relative_to(ROOT)}: {target}",
                )

    def test_category_profiles_cover_every_entry_once(self):
        profile_paths = sorted((ROOT / "docs" / "benchmarks").glob("*.md"))
        self.assertEqual(7, len(profile_paths))
        profile_text = "\n".join(path.read_text(encoding="utf-8") for path in profile_paths)
        for entry in self.catalog["entries"]:
            anchor = f'<a id="{entry["id"]}"></a>'
            self.assertEqual(1, profile_text.count(anchor), entry["id"])

    def test_relative_markdown_fragments_resolve(self):
        link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

        def heading_slugs(text):
            slugs = set()
            for heading in re.findall(r"^#{1,6}\s+(.+?)\s*$", text, flags=re.MULTILINE):
                clean = re.sub(r"<[^>]+>", "", heading).lower()
                clean = re.sub(r"[^\w\- ]", "", clean)
                slugs.add(re.sub(r"\s+", "-", clean.strip()))
            return slugs

        for markdown_path in [ROOT / "README.md", *(ROOT / "docs").rglob("*.md")]:
            for target in link_pattern.findall(markdown_path.read_text(encoding="utf-8")):
                if target.startswith(("https://", "http://", "mailto:")) or "#" not in target:
                    continue
                relative_path, fragment = target.split("#", 1)
                target_path = (markdown_path.parent / relative_path).resolve() if relative_path else markdown_path
                target_text = target_path.read_text(encoding="utf-8")
                explicit = re.search(rf'<a\s+id=["\']{re.escape(fragment)}["\']', target_text)
                self.assertTrue(
                    explicit or fragment in heading_slugs(target_text),
                    f"broken fragment in {markdown_path.relative_to(ROOT)}: {target}",
                )

    def test_workbook_integrity_and_counts(self):
        workbook_path = ROOT / "outputs" / "awesome-legal-benchmarks.xlsx"
        snapshot = json.loads(
            (ROOT / "catalog" / "resource-snapshot.json").read_text()
        )
        self.assertTrue(workbook_path.is_file())
        self.assertTrue(zipfile.is_zipfile(workbook_path))

        spreadsheet_ns = {
            "x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
        }
        expected_sheets = [
            "Summary",
            "Catalog",
            "Selection Guide",
            "Metric Theory",
            "Source Audit",
            "Resource Check",
            "Watchlist",
            "Not Separate",
        ]

        with zipfile.ZipFile(workbook_path) as archive:
            workbook = ET.fromstring(archive.read("xl/workbook.xml"))
            sheet_names = [
                sheet.attrib["name"]
                for sheet in workbook.findall(".//x:sheet", spreadsheet_ns)
            ]
            self.assertEqual(expected_sheets, sheet_names)

            summary = ET.fromstring(archive.read("xl/worksheets/sheet1.xml"))
            cells = {
                cell.attrib["r"]: cell.findtext("x:v", namespaces=spreadsheet_ns)
                for cell in summary.findall(".//x:c", spreadsheet_ns)
            }
            self.assertEqual(str(len(self.catalog["entries"])), cells["B4"])
            self.assertEqual("22", cells["B5"])
            self.assertEqual("21", cells["B6"])
            self.assertEqual(
                str(sum(not entry["source_readme_bullets"] for entry in self.catalog["entries"])),
                cells["B7"],
            )
            self.assertEqual(
                str(sum(entry["tier"] == "recommended" for entry in self.catalog["entries"])),
                cells["B8"],
            )
            self.assertEqual(
                str(sum(entry["access_profile"]["level"] == "open" for entry in self.catalog["entries"])),
                cells["B9"],
            )
            self.assertEqual(
                str(sum(entry["owner"]["commercial_interest"] == "yes" for entry in self.catalog["entries"])),
                cells["B10"],
            )
            self.assertEqual(str(snapshot["summary"]["ok"]), cells["B11"])

            expected_last_rows = {
                "xl/worksheets/sheet2.xml": 4 + len(self.catalog["entries"]),
                "xl/worksheets/sheet3.xml": 41,
                "xl/worksheets/sheet4.xml": 52,
                "xl/worksheets/sheet5.xml": 26,
                "xl/worksheets/sheet6.xml": 4 + len(snapshot["resources"]),
                "xl/worksheets/sheet7.xml": 24,
                "xl/worksheets/sheet8.xml": 11,
            }
            for sheet_path, expected_last_row in expected_last_rows.items():
                worksheet = ET.fromstring(archive.read(sheet_path))
                row_numbers = [
                    int(row.attrib["r"])
                    for row in worksheet.findall(".//x:row", spreadsheet_ns)
                ]
                self.assertEqual(expected_last_row, max(row_numbers), sheet_path)

            for index in range(1, len(expected_sheets) + 1):
                worksheet = ET.fromstring(
                    archive.read(f"xl/worksheets/sheet{index}.xml")
                )
                self.assertFalse(
                    worksheet.findall('.//x:c[@t="e"]', spreadsheet_ns),
                    f"formula error cell in sheet {index}",
                )
                for cell in worksheet.findall(".//x:c[x:f]", spreadsheet_ns):
                    self.assertIsNotNone(
                        cell.find("x:v", spreadsheet_ns),
                        f"formula without cached value at {cell.attrib['r']} in sheet {index}",
                    )


if __name__ == "__main__":
    unittest.main()
