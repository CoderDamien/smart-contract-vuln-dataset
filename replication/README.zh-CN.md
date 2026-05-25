# 论文复现包

本目录将数据集发布仓库补充为面向论文结果复核的 replication package。为避免重复上传大体量数据，本目录不再次展开复制完整切分 JSON，而是通过索引精确指向 `data/processed/balanced_stage1_resplit_721.tar.gz` 归档内部的切分文件，并记录每个切分文件的 SHA-256 校验值。

## 目录说明

| 路径 | 作用 |
|---|---|
| `data_splits/balanced_stage1_resplit_721/split_file_index.csv` | 本文 `has_vul`、`vul_type`、`vul_line` 三个任务的 train/validation/test 切分索引；每行给出 processed 数据包内的具体路径。 |
| `data_splits/balanced_stage1_resplit_721/build_report.json` | 本文使用切分版本的数据构建报告。 |
| `label_mapping/` | 归一化漏洞标签空间，以及不同来源标签到本文标签体系的映射。 |
| `experiment_configs/` | 正式实验方案、运行队列脚本、项目配置、逐 run 配置 bundle 和 `run_configs_index.csv`。 |
| `evaluation/` | 三个论文任务和评价指标相关代码，包括漏洞行定位指标。 |
| `results/` | 从论文工作 Excel 表导出的 CSV 结果表，以及原始 Excel 工作簿。 |
| `prediction_summaries/` | 预测文件索引，包含行数、文件大小、SHA-256 和本地来源路径。 |
| `figures/` | 论文使用或重绘过的 SVG 图。 |
| `figure_source/` | 图表生成/审计脚本，以及可作为图表源数据的结果 CSV。 |
| `manifest.json` | 本 replication package 的文件级校验清单。 |

## 与论文结果的对应关系

| 论文内容 | 对应文件 |
|---|---|
| 数据集规模、任务划分和训练/验证/测试集 | `data/processed/balanced_stage1_resplit_721.tar.gz`; `replication/data_splits/balanced_stage1_resplit_721/split_file_index.csv`; `replication/data_splits/balanced_stage1_resplit_721/build_report.json`; `metadata/dataset_statistics.json` |
| 标签归一化和漏洞类型体系 | `replication/label_mapping/paper_label_space.json`; `replication/label_mapping/dataset_label_mapping_draft.json`; `docs/schema.zh-CN.md`; `docs/data_processing_and_augmentation.md` |
| 主实验矩阵和完成情况 | `replication/results/paper_experiment_matrix_closure.csv`; `replication/results/paper_experiment_closure_summary.csv`; `replication/results/model_summary.csv`; `replication/experiment_configs/formal_experiment_execution_plan.md` |
| 模型、任务、方法维度的主结果表 | `replication/results/paper_experiment_metrics_all.csv`; `replication/results/all_result_metrics.csv`; `replication/results/paper_experiment_results.xlsx` |
| `has_vul` 漏洞存在性判断结果 | `replication/results/has_vul_metrics.csv`; `replication/evaluation/tasks/has_vul.py` |
| `vul_type` 漏洞类型分类结果 | `replication/results/vul_type_metrics.csv`; `replication/evaluation/tasks/vul_type.py`; `replication/label_mapping/` |
| `vul_line` 漏洞行定位结果 | `replication/results/vul_line_metrics.csv`; `replication/evaluation/tasks/vul_line.py`; `replication/evaluation/metrics_vul_line.py` |
| Prompt 消融分析 | `replication/results/prompt_ablation.csv`; `replication/evaluation/prompts/templates.py`; `replication/evaluation/prompts/parsers.py` |
| 数据补齐、低频类别补充和数据建设工作量分析 | `replication/results/data_completion_before_after.csv`; `replication/results/data_completion_pairs.csv`; `docs/data_processing_and_augmentation.md`; `docs/construction_effort.md` |
| 图表源数据和论文图 | `replication/figure_source/`; `replication/results/*.csv`; `replication/figures/` |
| 预测结果文件审计 | `replication/prediction_summaries/prediction_artifact_index.csv`; `replication/prediction_summaries/prediction_artifact_index.json` |

## 使用方式

1. 使用 Git LFS 克隆或下载本仓库。
2. 解压 `data/processed/balanced_stage1_resplit_721.tar.gz`。
3. 根据 `replication/data_splits/balanced_stage1_resplit_721/split_file_index.csv` 检查解压后的切分文件是否与本文版本一致。
4. 使用 `replication/results/paper_experiment_metrics_all.csv` 复核论文主实验指标。
5. 使用 `replication/experiment_configs/run_configs_index.csv`、`replication/experiment_configs/run_configs_bundle.jsonl` 和 `replication/prediction_summaries/prediction_artifact_index.csv` 将每条论文结果追溯到对应配置和预测文件。

本目录的目标是支持论文结果审计和复核。完整模型 checkpoint 和完整预测 JSONL 文件未在本仓库中重复发布；本仓库提供对应预测文件的摘要索引、行数、大小和哈希值。
