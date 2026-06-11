# Release v1.0.3

This schema and metadata revision clarifies vulnerable-line coordinate semantics and restores source-line coordinates where they can be reconstructed by source-level audit, while preserving backward compatibility with the original `vulnerabilities[].line` field.

- Repository: https://github.com/CoderDamien/smart-contract-vuln-dataset
- Version: `v1.0.3`
- This release includes the manuscript-aligned replication package and the vulnerable-line coordinate schema revision.
- Audited source commit before release preparation: `6639cdd3f12a6bab308849434e3eab7e06897eda`
- DOI: pending Zenodo archival after the GitHub release is published.

## Contents

- Processed benchmark archive: `data/processed/balanced_stage1_resplit_721.tar.gz`
- Merged data archives: `data/merged/has_vul_merged_stage0.tar.gz`, `data/merged/vul_type_merged_stage0.tar.gz`, and `data/merged/vul_line_merged_stage0.tar.gz`
- Replication package: `replication/`
- Current manuscript figure set: `replication/figures/figures_q1_redesign/`
- Numbered supplementary tables: `supplementary/`
- Dataset metadata and release notes: `metadata/`
- Archive checksums: `metadata/archive_checksums.csv`

## Schema Revision

- `vulnerabilities[].line` is retained as a backward-compatible field.
- For `vul_line`, `line` and `line_end` are 1-based line numbers relative to the released `context` field.
- New annotation-level fields clarify the coordinate system: `line_coordinate_system`, `context_start_line`, `source_line`, `source_line_end`, `raw_loc`, `raw_length`, `line_scope`, `source_mapping_status`, and `source_mapping_method`.
- SolidiFI line mappings in `vul_line_merged_stage0` were audited: all 24,264 vulnerability annotations satisfy `line = raw_loc - context_start_line + 1`.
- For the processed `vul_line_721_stratified_v1` split, all 35,975 vulnerability annotations now have `source_mapping_status = available`.
- Mapping methods include SolidiFI raw-location offsets, source-level full-context identity mappings for DAppSCAN, ScrawlD, and Slither-derived annotations, and full-context identity mappings for unattributed legacy samples.
- The current manuscript evaluates representative vulnerable start lines; `line_end` and `source_line_end` are retained for future range-aware evaluation.

## Manuscript Alignment

- Formal experiment matrix: 226 model-task-mode evaluation units.
- Model coverage: 25 models from 8 model families.
- Use modes: direct inference, structured prompting, full fine-tuning, and QLoRA.
- Prompt ablation supplement: 16 comparisons for Qwen2.5-Coder-7B and 32B over `vul_type` and `vul_line`.
- Current manuscript figures: `fig1_protocol.svg`, `fig4_qwen_scaling.svg`, `fig5_prompt_ablation.svg`, `fig8_line_boundary.svg`, and `fig9_runtime_tradeoff.svg` under `replication/figures/figures_q1_redesign/`.

## Citation

Until the Zenodo DOI is issued, cite the repository URL and this release tag. After archival, replace the URL-only citation with the Zenodo DOI.
