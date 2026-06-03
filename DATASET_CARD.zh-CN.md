# 数据集卡片：面向 Solidity 与以太坊安全研究的智能合约漏洞数据集

## 数据集简介

本数据集支持 Solidity 与以太坊智能合约的漏洞存在性判断、漏洞类型分类和漏洞行定位，可用于区块链安全研究、Web3 安全分析、静态分析工具比较和大语言模型代码安全评测。

当前与 IST 投稿稿件对齐的版本：`v1.0.1`。
初始数据发布版本：`v1.0.0`。

## 搜索关键词

智能合约漏洞数据集、Solidity 安全数据集、以太坊智能合约漏洞检测、重入漏洞数据集、智能合约漏洞定位、漏洞行定位、漏洞类型分类、区块链安全数据集、Web3 安全数据集、大语言模型代码安全评测。

## 支持任务

- 二分类漏洞存在性判断：`has_vul`
- 多标签漏洞类型分类：`vul_type`
- 多行漏洞定位：`vul_line`

## 标签空间

- `access_control`
- `arithmetic`
- `bad_randomness`
- `denial_service`
- `front_running`
- `reentrancy`
- `time_manipulation`
- `unchecked_low_calls`

## 数据规模

| 阶段 | `has_vul` | `vul_type` | `vul_line` |
|---|---:|---:|---:|
| 合并数据 | 105,278 | 95,573 | 24,178 |
| 推荐 processed 划分 | 24,441 | 24,394 | 12,491 |

## 来源覆盖

数据集整合 8 个公开来源，覆盖人工整理基准、注入式漏洞基准、审计来源标签、静态分析弱标签、漏洞发现库和源码恢复参考。

## 论文复现包

本仓库包含与 2026-06-03 版 IST 投稿稿件对齐的论文复现包。该复现包覆盖 226 个模型-任务-模式评价单元、25 个模型、8 个模型族，以及 direct、prompt、full fine-tuning 和 QLoRA 四种使用模式。

关键复现文件包括：

- 正式实验矩阵和主指标：`replication/results/paper_experiment_matrix_closure.csv`、`replication/results/paper_experiment_metrics_all.csv`
- 任务级指标：`replication/results/has_vul_metrics.csv`、`replication/results/vul_type_metrics.csv`、`replication/results/vul_line_metrics.csv`
- Prompt 消融：`replication/results/prompt_ablation.csv`，以及对应论文口径的 16 行补充表 `supplementary/tables/Table_S9.csv`
- 数据集扩展分析：`replication/results/data_completion_pairs.csv`、`supplementary/tables/Table_S10.csv`
- 当前正文图：`replication/figures/figures_q1_redesign/`
- 补充材料表：`supplementary/supplementary_tables.xlsx`、`supplementary/tables/Table_S1.csv` 至 `Table_S14.csv`

当前稿件的关键结果锚点包括：

| 任务 / 分析 | 论文口径 |
|---|---|
| 漏洞存在性判断 | 最佳 F1 = 0.8757，来自 Qwen2.5-Coder-1.5B full fine-tuning |
| 漏洞类型识别 | 最佳 standard F1 = 0.6265；最佳 macro-F1 = 0.4755；最佳 multi-label F1 = 0.4300 |
| 漏洞行定位 | 最佳 strict-F1 = 0.2955；最佳 contract-hit = 0.8451 |
| Prompt 消融 | Qwen2.5-Coder-7B 和 32B 在 `vul_type`、`vul_line` 上的 16 组比较 |
| 数据集扩展 | 6 组同模型、同任务、同方法的扩展前后配对比较 |

## 适用场景

- 智能合约漏洞检测研究。
- Solidity 与以太坊安全基准评测。
- 大语言模型代码安全能力评测。
- 漏洞类型分类。
- 漏洞行定位。
- 区块链安全数据治理研究。

## 不适用场景

- 未核查上游许可证时直接商业化再分发源码。
- 将静态分析弱标签直接视为人工验证真值。
- 将漏洞行定位任务简化为单个数值回归。

## 许可证和再分发

本仓库不再分发原始上游数据。详见 [metadata/upstream_license_review.zh-CN.md](metadata/upstream_license_review.zh-CN.md) 和 [THIRD_PARTY_NOTICES.zh-CN.md](THIRD_PARTY_NOTICES.zh-CN.md)。
