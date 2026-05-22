# Data Files

This directory contains the publicly downloadable processed dataset archive.

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
```

## Notes

- Raw upstream data is not redistributed.
- Large merged intermediate JSON files are not included because several files exceed 3 GB each.
- Source and license notes are documented in `metadata/upstream_license_review.md`.

