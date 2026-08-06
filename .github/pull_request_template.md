## What changed

<!-- Keep the summary specific. Link the canonical record or documentation section. -->

## Evidence and scope

- [ ] Canonical source-of-truth records are updated; generated views were regenerated.
- [ ] Direct first-party URLs were checked.
- [ ] Jurisdiction, language, input/output, splits, metrics, access, license, and maintenance are recorded.
- [ ] Verified fact, inference, and unresolved ambiguity are separated.
- [ ] Duplicate identities and contamination risks were checked.

## Verification

```bash
python scripts/validate_catalog.py
python scripts/generate_catalog.py --check
python -m unittest discover -s tests -v
python scripts/check_resources.py --check-snapshot
```

<!-- Paste the results or explain any intentionally skipped check. -->
