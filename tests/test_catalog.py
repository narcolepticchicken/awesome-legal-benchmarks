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
        self.assertEqual(45, len(self.catalog["entries"]))
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
        self.assertEqual(147, len(actual))
        self.assertTrue(all(item["ok"] for item in snapshot["resources"]))
        self.assertEqual(
            {"github": 39, "huggingface": 33, "papers": 48, "leaderboards": 13, "project": 17},
            {
                family: values["total"]
                for family, values in snapshot["summary"]["by_family"].items()
            },
        )

    def test_relative_markdown_links_resolve(self):
        link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
        for markdown_path in [ROOT / "README.md", *(ROOT / "docs").glob("*.md")]:
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

    def test_workbook_integrity_and_counts(self):
        workbook_path = ROOT / "outputs" / "awesome-legal-benchmarks.xlsx"
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
            self.assertEqual("45", cells["B4"])
            self.assertEqual("22", cells["B5"])
            self.assertEqual("21", cells["B6"])
            self.assertEqual("24", cells["B7"])
            self.assertEqual("21", cells["B8"])
            self.assertEqual("147", cells["B11"])

            expected_last_rows = {
                "xl/worksheets/sheet2.xml": 49,
                "xl/worksheets/sheet4.xml": 31,
                "xl/worksheets/sheet5.xml": 26,
                "xl/worksheets/sheet6.xml": 151,
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
