# Language-Augmented Video Action Anticipation: Evidence Package and Catalogue

This repository contains the machine-readable evidence package and the versioned catalogue accompanying the review article **Language-Augmented Video Action Anticipation: Design Fundamentals, Benchmarks, and Open Challenges**.

## Contents

- `data/`: coded evidence inventory, focal-selection matrix, component assignments, protocol metadata, source locators, BCAP materials, search/verification records, and the automated audit.
- `awesome_catalogue/`: version 1.0.0 catalogue of the 25 focal methods, organised by task regime and C1-C4 assignment.

## Validate the evidence package

From the repository root:

```bash
python data/audit_submission.py
python awesome_catalogue/scripts/validate_catalogue.py
```

The expected retained synthesis set is 69 works, with 79 inventory records in total and 25 focal methods. The focal component counts are C1=8, C2=7, C3=4, and C4=6.

## Public release

Before publishing release `v1.0.0`, set the repository URL and release date in `awesome_catalogue/release_metadata.json`, then run:

```bash
python awesome_catalogue/scripts/validate_catalogue.py --release-mode
```

An archival DOI should be added only after one has actually been issued.

## Licence

The evidence package and catalogue are released under CC BY 4.0. See `LICENSE`.
