# Dataset Construction Effort

This dataset is not a simple mirror of a single public dataset. It is a multi-source data governance effort for three smart contract vulnerability detection tasks.

## Workload Summary

| Item | Output / Scale |
|---|---:|
| Public upstream sources | 8 |
| Local raw-file audit reference | 37,914 files |
| Normalized staging files | 30 files |
| Candidate files | 8 files |
| Review-pack files | 10 files |
| Confirmed-sample files | 8 files |
| Merged data and statistics files | 21 files |
| Processed data and build reports | 72 files |
| Data processing and experiment support scripts | 40+ Python scripts |
| Final merged sample scale | 105,278 / 95,573 / 24,178 |
| Recommended processed split scale | 24,441 / 24,394 / 12,491 |

The merged sample counts correspond to `has_vul`, `vul_type`, and `vul_line`; the processed split counts correspond to `balanced_stage1_resplit_721`.

## Main Work

The construction process includes:

- upstream-source screening,
- unified schema design,
- cross-taxonomy label mapping,
- invalid-label and invalid-line filtering,
- raw and normalized hash deduplication,
- low-frequency class mining,
- review-pack construction,
- confirmed sample generation,
- task-level balancing and splitting,
- release documentation and citation preparation.

## Low-Frequency Class Augmentation

The dataset includes a dedicated augmentation process for low-frequency labels such as `front_running` and `denial_service`.

| Target | Candidates | High-confidence | Medium-confidence | Seed-labeled | Heuristic candidates |
|---|---:|---:|---:|---:|---:|
| `front_running` | 9,200 | 4,200 | 5,000 | 1,200 | 8,000 |
| `denial_service` | 10,357 | 5,357 | 5,000 | 1,357 | 9,000 |
| Total | 19,557 | 9,557 | 10,000 | 2,557 | 17,000 |

Review packs:

| Target | Review samples |
|---|---:|
| `front_running` | 1,500 |
| `denial_service` | 1,657 |
| Total | 3,157 |

Confirmed samples:

| Target | Accepted | Deferred |
|---|---:|---:|
| `front_running` | 1,201 | 299 |
| `denial_service` | 1,465 | 192 |
| Total | 2,666 | 491 |

Only confirmed samples are used in downstream confirmed data and processed dataset construction.

## Publication Work

The release package includes bilingual README files, source documentation, source contribution counts, processing and augmentation notes, schema documentation, examples, license notes, third-party notices, citation metadata, and machine-readable statistics.

