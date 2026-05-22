# Dataset Construction

This document describes the construction process used to build the unified smart contract vulnerability dataset.

## Pipeline Overview

The dataset is constructed through staged processing:

1. Raw source collection.
2. Per-source normalization.
3. Label taxonomy mapping.
4. Source-code deduplication.
5. Cross-source merge.
6. Task-specific dataset construction.
7. Stratified train/validation/test splitting.
8. Dataset audit and statistics generation.

## Directory Stages

| Stage | Directory | Purpose |
|---|---|---|
| Raw sources | `data/raw/` or `data/external/<source>/raw/` | Untouched upstream downloads, clones, or snapshots. |
| Staging data | `data/staging/<source>/` | Per-source normalized JSON files before global merge. |
| Merged data | `data/merged/` | Cross-source merged datasets for each task. |
| Processed data | `data/processed/` or `data/prepared/` | Task-specific benchmark splits ready for model training and evaluation. |
| Metadata | `metadata/` | Statistics, source catalog, schema, and release records. |

## Unified Schema

Each source is transformed into a unified sample schema containing:

- Sample identity and source metadata.
- Source-code context.
- Vulnerability existence label.
- One or more vulnerability records.
- Original source label and normalized label.
- Label confidence and label origin.
- Raw and normalized deduplication hashes.

See `docs/schema.md`.

## Label Mapping

Source-specific labels are mapped into the shared taxonomy:

| Normalized Label | Typical Source Labels |
|---|---|
| `access_control` | access control, tx.origin, authorization-related findings |
| `arithmetic` | integer overflow, integer underflow, arithmetic |
| `bad_randomness` | weak randomness, predictable randomness |
| `denial_service` | DoS, denial of service, selected SWC denial-service findings |
| `front_running` | front running, transaction-order dependence, TOD |
| `reentrancy` | reentrancy |
| `time_manipulation` | timestamp dependency, time manipulation |
| `unchecked_low_calls` | unchecked low-level call, unchecked send, unhandled exception |

Unmapped or unsupported labels are stored as `other`, `unknown`, or excluded from benchmark splits according to the task protocol.

## Deduplication

The construction pipeline computes two hashes:

- `dedup_hash_raw`: SHA-256 hash of the raw joined source context.
- `dedup_hash_normalized`: SHA-256 hash after removing comments, trimming lines, and normalizing whitespace.

The processed `balanced_stage1_resplit_721` split uses group-aware splitting with the grouping key:

```text
dedup_hash_normalized | dedup_hash_raw | context_sha256
```

This reduces train/validation/test leakage caused by duplicate or near-duplicate source code.

## Recommended Benchmark Split

The current recommended public benchmark split is `balanced_stage1_resplit_721`.

| Dataset | Train | Validation | Test | Total |
|---|---:|---:|---:|---:|
| `has_vul_721_stratified_v1` | 17,411 | 4,667 | 2,363 | 24,441 |
| `vul_type_721_stratified_v1` | 18,573 | 3,829 | 1,992 | 24,394 |
| `vul_line_721_stratified_v1` | 10,155 | 1,529 | 807 | 12,491 |

## Task Protocols

### Vulnerability Detection

`has_vul` is a binary task:

- `0`: no known vulnerability.
- `1`: at least one vulnerability label is attached to the sample.

### Vulnerability Type Classification

`vul_type` is a multi-label task. A single sample may contain multiple vulnerability types.

### Vulnerable Line Localization

`vul_line` is a multi-line localization task. A model prediction may contain one or more line numbers. Evaluation should use set-based or line-level metrics instead of single-value regression.

Recommended metrics include:

- Exact set match.
- Tolerant set match.
- Line-level precision, recall, and F1.
- Top-k hit rate.
- Optional interval or IoU-style metrics when ranges are available.

## Audit Requirements

Before publishing a release, run audits for:

- Duplicate sample IDs.
- Duplicate or near-duplicate source code across splits.
- Out-of-range line labels.
- Empty source-code contexts.
- Samples with contradictory labels.
- Source distribution per split.
- Label distribution per split.
- License and citation completeness.

