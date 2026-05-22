# Data Files

This directory contains publicly downloadable dataset archives.

## Merged vs. Processed

| Dataset Level | Purpose | When to Use |
|---|---|---|
| `data/merged/` | Large multi-source merged pools after normalization, label mapping, and basic cleaning. | Use when the recommended processed split is not enough and you want to build your own larger training set, sampling policy, or split. |
| `data/processed/` | Recommended task-ready benchmark split after filtering, balancing, deduplication, and train/validation/test construction. | Use for direct model training, evaluation, and paper reproduction. |

`merged` is larger because it keeps more normalized multi-source samples and source-code context. `processed` is smaller because it is a curated benchmark split with task-specific filtering, balancing, and split controls.

## Merged Dataset Archives

| File | Size | Samples | Content |
|---|---:|---:|---|
| `merged/has_vul_merged_stage0.tar.gz` | 605 MB | 105,278 | Binary vulnerability detection merged pool. |
| `merged/vul_type_merged_stage0.tar.gz` | 568 MB | 95,573 | Vulnerability type classification merged pool. |
| `merged/vul_line_merged_stage0.tar.gz` | 2.5 MB | 24,178 | Vulnerable line localization merged pool. |

## Processed Benchmark Archive

| File | Size | Content |
|---|---:|---|
| `processed/balanced_stage1_resplit_721.tar.gz` | 213 MB | Recommended task-specific train/validation/test splits for `has_vul`, `vul_type`, and `vul_line`. |

The archive contains:

```text
balanced_stage1_resplit_721/
├── build_report.json
├── has_vul_721_stratified_v1/
│   ├── train.json
│   ├── val.json
│   └── test.json
├── vul_type_721_stratified_v1/
│   ├── train.json
│   ├── val.json
│   └── test.json
└── vul_line_721_stratified_v1/
    ├── train.json
    ├── val.json
    └── test.json
```

## Extract

```bash
tar -xzf data/processed/balanced_stage1_resplit_721.tar.gz -C data/processed/
tar -xzf data/merged/has_vul_merged_stage0.tar.gz -C data/merged/
tar -xzf data/merged/vul_type_merged_stage0.tar.gz -C data/merged/
tar -xzf data/merged/vul_line_merged_stage0.tar.gz -C data/merged/
```

## Notes

- Raw upstream data is not redistributed.
- Large merged intermediate JSON files are not included because several files exceed 3 GB each.
- Source and license notes are documented in `metadata/upstream_license_review.md`.
