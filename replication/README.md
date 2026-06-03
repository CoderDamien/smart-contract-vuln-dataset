# Replication Package

This directory turns the dataset release into a paper-oriented replication package aligned with the IST manuscript version dated 2026-06-03. It does not duplicate the large processed split files; instead, it points to the exact files inside `data/processed/balanced_stage1_resplit_721.tar.gz` and records SHA-256 checksums for each split.

The current manuscript reports 226 model-task-mode evaluation units over 25 models, 8 model families, and four use modes: direct inference, structured prompting, full fine-tuning, and QLoRA.

## Directory Map

| Path | Purpose |
|---|---|
| `data_splits/balanced_stage1_resplit_721/split_file_index.csv` | Exact train/validation/test split index for `has_vul`, `vul_type`, and `vul_line`; each row points to the internal path inside the processed dataset archive. |
| `data_splits/balanced_stage1_resplit_721/build_report.json` | Dataset construction report for the paper split. |
| `label_mapping/` | Normalized vulnerability label space and source-to-paper label mapping. |
| `experiment_configs/` | Formal experiment plan, queue script, project configuration files, bundled per-run configuration records, and `run_configs_index.csv`. |
| `evaluation/` | Task and metric code used to define the three paper tasks, including vulnerable-line localization metrics. |
| `results/` | Paper result tables exported from the working Excel workbook as CSV files, plus the original workbook. |
| `prediction_summaries/` | Prediction artifact index with row counts, file sizes, SHA-256 checksums, and local source paths for each prediction file. |
| `figures/` | SVG figures used for the manuscript and figure redesign drafts. The current manuscript uses `figures/figures_q1_redesign/`. |
| `figure_source/` | Scripts and CSV tables used to regenerate or audit the paper figures. |
| `manifest.json` | File-level checksum manifest for this replication package. |

Numbered supplementary tables are published in `supplementary/`. The supplement includes `Table_S1` to `Table_S14` as individual CSV files and as the combined workbook `supplementary/supplementary_tables.xlsx`.

## Mapping to Manuscript Results

| Manuscript Component | Replication Files |
|---|---|
| Dataset statistics and task splits | `data/processed/balanced_stage1_resplit_721.tar.gz`; `replication/data_splits/balanced_stage1_resplit_721/split_file_index.csv`; `replication/data_splits/balanced_stage1_resplit_721/build_report.json`; `metadata/dataset_statistics.json` |
| Label normalization and vulnerability categories | `replication/label_mapping/paper_label_space.json`; `replication/label_mapping/dataset_label_mapping_draft.json`; `docs/schema.md`; `docs/data_processing_and_augmentation.en.md` |
| Main experiment matrix and completion status | `replication/results/paper_experiment_matrix_closure.csv`; `replication/results/paper_experiment_closure_summary.csv`; `replication/results/model_summary.csv`; `replication/experiment_configs/formal_experiment_execution_plan.md` |
| Main result table across models, tasks, and methods | `replication/results/paper_experiment_metrics_all.csv`; `replication/results/all_result_metrics.csv`; `replication/results/paper_experiment_results.xlsx` |
| `has_vul` results | `replication/results/has_vul_metrics.csv`; `replication/evaluation/tasks/has_vul.py` |
| `vul_type` results | `replication/results/vul_type_metrics.csv`; `replication/evaluation/tasks/vul_type.py`; `replication/label_mapping/` |
| `vul_line` results | `replication/results/vul_line_metrics.csv`; `replication/evaluation/tasks/vul_line.py`; `replication/evaluation/metrics_vul_line.py` |
| Prompt ablation analysis | `replication/results/prompt_ablation.csv`; `replication/evaluation/prompts/templates.py`; `replication/evaluation/prompts/parsers.py` |
| Dataset expansion and low-frequency class supplementation analysis | `replication/results/data_completion_before_after.csv`; `replication/results/data_completion_pairs.csv`; `docs/data_processing_and_augmentation.en.md`; `docs/construction_effort.en.md` |
| Figure source data and rendered figures | `replication/figure_source/`; `replication/results/*.csv`; `replication/figures/` |
| Prediction artifact audit | `replication/prediction_summaries/prediction_artifact_index.csv`; `replication/prediction_summaries/prediction_artifact_index.json` |

## Current Manuscript Figures

| Manuscript Figure | Rendered SVG | Source / Audit Files |
|---|---|---|
| Figure 1. Reproducible evaluation framework | `replication/figures/figures_q1_redesign/fig1_protocol.svg` | `replication/figure_source/redraw_q1_figures.py` |
| Figure 2. Qwen2.5-Coder scale trends | `replication/figures/figures_q1_redesign/fig4_qwen_scaling.svg` | `replication/results/paper_experiment_metrics_all.csv`; `replication/figure_source/redraw_q1_figures.py` |
| Figure 3. Structured prompt ablation | `replication/figures/figures_q1_redesign/fig5_prompt_ablation.svg` | `replication/results/prompt_ablation.csv`; `replication/figure_source/redraw_q1_figures.py` |
| Figure 4. Candidate-hit versus exact line localization boundary | `replication/figures/figures_q1_redesign/fig8_line_boundary.svg` | `replication/results/vul_line_metrics.csv`; `replication/figure_source/redraw_q1_figures.py` |
| Figure 5. Runtime-performance Pareto trade-off | `replication/figures/figures_q1_redesign/fig9_runtime_tradeoff.svg` | `replication/results/all_result_metrics.csv`; `replication/figure_source/redraw_q1_figures.py` |

## Current Manuscript Result Anchors

| Result Claim | Value / Scope | Supporting Files |
|---|---|---|
| Formal matrix size | 226 evaluation units: 63 direct, 63 prompt, 63 QLoRA, and 37 full fine-tuning units | `replication/results/paper_experiment_matrix_closure.csv`; `replication/results/paper_experiment_metrics_all.csv` |
| Model coverage | 25 models from 8 model families | `replication/results/model_summary.csv`; `replication/experiment_configs/formal_experiment_execution_plan.md` |
| Best vulnerability-presence result | F1 = 0.8757 with Qwen2.5-Coder-1.5B full fine-tuning | `replication/results/has_vul_metrics.csv`; `replication/results/paper_experiment_metrics_all.csv` |
| Best vulnerability-type results | standard F1 = 0.6265; macro-F1 = 0.4755; multi-label F1 = 0.4300 | `replication/results/vul_type_metrics.csv`; `replication/results/paper_experiment_metrics_all.csv` |
| Best vulnerable-line results | strict-F1 = 0.2955; contract-hit = 0.8451 | `replication/results/vul_line_metrics.csv`; `replication/results/paper_experiment_metrics_all.csv` |
| Prompt ablation scope | 16 comparisons: 2 Qwen2.5-Coder models x 2 tasks x 4 prompt settings | `replication/results/prompt_ablation.csv`; `supplementary/tables/Table_S9.csv` |
| Dataset expansion analysis | 6 same-model, same-task, same-method before/after pairs | `replication/results/data_completion_pairs.csv`; `supplementary/tables/Table_S10.csv` |

## How to Use

1. Download or clone the repository with Git LFS enabled.
2. Extract `data/processed/balanced_stage1_resplit_721.tar.gz`.
3. Use `replication/data_splits/balanced_stage1_resplit_721/split_file_index.csv` to verify that the extracted split files match the paper split checksums.
4. Use `replication/results/paper_experiment_metrics_all.csv` for the manuscript-level metrics table.
5. Use `replication/experiment_configs/run_configs_index.csv`, `replication/experiment_configs/run_configs_bundle.jsonl`, and `replication/prediction_summaries/prediction_artifact_index.csv` to trace each reported row back to its run configuration and prediction artifact.

The package is intended to make the paper results auditable. Full model checkpoints and full prediction JSONL files are not duplicated in this repository; their checksums and local source paths are indexed in `prediction_summaries/`.
The released indexes use stable artifact paths such as `artifacts/predictions/...`, `artifacts/metrics/...`, and `artifacts/configs/...` instead of private server paths. These paths identify the artifact class and run-level provenance; the corresponding row counts, file sizes, and SHA-256 checksums provide the audit trail.
