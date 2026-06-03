# Release v1.0.1

This manuscript-aligned release updates the dataset repository information, replication mapping, supplementary tables, and figure references for the IST manuscript version dated 2026-06-03. The large data archives are unchanged from the initial `v1.0.0` data release.

- Repository: https://github.com/CoderDamien/smart-contract-vuln-dataset
- Version: `v1.0.1`
- Initial data release: `v1.0.0`
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

## Manuscript Alignment

- Formal experiment matrix: 226 model-task-mode evaluation units.
- Model coverage: 25 models from 8 model families.
- Use modes: direct inference, structured prompting, full fine-tuning, and QLoRA.
- Prompt ablation supplement: 16 comparisons for Qwen2.5-Coder-7B and 32B over `vul_type` and `vul_line`.
- Current manuscript figures: `fig1_protocol.svg`, `fig4_qwen_scaling.svg`, `fig5_prompt_ablation.svg`, `fig8_line_boundary.svg`, and `fig9_runtime_tradeoff.svg` under `replication/figures/figures_q1_redesign/`.

## Citation

Until the Zenodo DOI is issued, cite the repository URL and this release tag. After archival, replace the URL-only citation with the Zenodo DOI.
