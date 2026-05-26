# Supplementary Tables

This directory contains the numbered supplementary tables referenced by the manuscript. The table numbers are stable and match the in-text references in `Q1_English_IST_polished.md`.

| Table | Title | CSV | Rows | Key columns | Source |
|---|---|---|---:|---|---|
| Table S1 | Formal experiment matrix and completion status | `supplementary/tables/Table_S1.csv` | 226 | model; task; method; status; execution_source | replication/results/paper_experiment_matrix_closure.csv |
| Table S2 | Model inventory and experiment coverage by model family | `supplementary/tables/Table_S2.csv` | 32 | model_family; model; task_count; completed_count | replication/results/model_summary.csv |
| Table S3 | Complete model-task-method metric matrix | `supplementary/tables/Table_S3.csv` | 226 | model; task; method; status; f1/macro_f1/tolerant_f1 | replication/results/paper_experiment_metrics_all.csv |
| Table S4 | Vulnerability existence detection results | `supplementary/tables/Table_S4.csv` | 94 | model; method; f1; precision; recall | replication/results/has_vul_metrics.csv |
| Table S5 | Vulnerability type classification results | `supplementary/tables/Table_S5.csv` | 97 | model; method; macro_f1; multi_label_f1; status | replication/results/vul_type_metrics.csv |
| Table S6 | Vulnerable line localization results | `supplementary/tables/Table_S6.csv` | 99 | model; method; strict_f1; tolerant_f1; contract_hit | replication/results/vul_line_metrics.csv |
| Table S7 | Traditional pretrained-code baselines | `supplementary/tables/Table_S7.csv` | 16 | model; task; method; status; f1/macro_f1/tolerant_f1 | replication/results/paper_experiment_metrics_all.csv |
| Table S8 | Qwen2.5-Coder parameter-scale analysis | `supplementary/tables/Table_S8.csv` | 63 | model; task; method; status; model_family | replication/results/paper_experiment_metrics_all.csv |
| Table S9 | Prompt ablation results for Qwen2.5-Coder-7B and 32B | `supplementary/tables/Table_S9.csv` | 16 | model; task; prompt_version; mode; parseable_ratio; f1/strict_f1/tolerant_f1 | replication/results/prompt_ablation.csv |
| Table S10 | Dataset expansion before/after paired results | `supplementary/tables/Table_S10.csv` | 6 | model; task; method; expansion_stage; dataset_view | replication/results/data_completion_pairs.csv |
| Table S11 | Complete method-pair comparison records | `supplementary/tables/Table_S11.csv` | 168 | model; task; comparison; left_metric; right_metric; delta | replication/results/paper_experiment_metrics_all.csv |
| Table S12 | Runtime and performance trade-off records | `supplementary/tables/Table_S12.csv` | 321 | model; task; method; runtime_minutes; status | replication/results/all_result_metrics.csv |
| Table S13 | Prediction artifact and parsing-error audit | `supplementary/tables/Table_S13.csv` | 379 | source; run_name; model; task; method; parseable_ratio | replication/prediction_summaries/prediction_artifact_index.csv; replication/results/prompt_ablation.csv |
| Table S14 | Figure source data and generated figure inventory | `supplementary/tables/Table_S14.csv` | 23 | artifact_type; path; sha256 | replication/figures/; replication/figure_source/ |

Critical manuscript references:

- Section 5 refers to Supplementary Table S1, available as `supplementary/tables/Table_S1.csv`.
- Section 7.9 refers to Supplementary Tables S5, S9, and S13, available as `supplementary/tables/Table_S5.csv`, `supplementary/tables/Table_S9.csv`, and `supplementary/tables/Table_S13.csv`.

A combined workbook is provided as `supplementary/supplementary_tables.xlsx` with worksheets named `Table_S1` to `Table_S14`. Each worksheet starts with the column header in row 1.
