# 数据来源与贡献统计

本文档列出本数据集引用的上游公开数据来源、公开链接、文件数量参考以及各来源在当前数据版本中的样本贡献量。

本仓库不公开原始 raw 数据。下表中的 raw 文件数仅用于说明本地数据整理过程中的来源规模，不代表公开仓库将上传这些原始文件。

数据库建设工作量摘要见 [construction_effort.md](construction_effort.md)。

## 上游数据来源

| 来源 ID | 公开来源 | 链接 | 在本数据集中的作用 |
|---|---|---|---|
| `Empirical-Analysis-of-Vulnerability-Detection-Tools-for-Solidity-Smart-Contracts` | Empirical Analysis of Vulnerability Detection Tools for Solidity Smart Contracts | https://github.com/fsalzano/Empirical-Analysis-of-Vulnerability-Detection-Tools-for-Solidity-Smart-Contracts | 原始论文数据的核心来源。 |
| `smartbugs_curated` | SmartBugs Curated | https://github.com/smartbugs/smartbugs-curated | 高质量人工整理基准来源。 |
| `solidifi_benchmark` | SolidiFI Benchmark | https://github.com/DependableSystemsLab/SolidiFI-benchmark | 注入式漏洞基准，提供漏洞类型和定位信息。 |
| `dappscan` | DAppSCAN | https://github.com/InPlusLab/DAppSCAN | 真实 DApp 审计和源码来源，用于漏洞存在性与类型标签补充。 |
| `slither_audited_smart_contracts` | Slither Audited Smart Contracts | https://huggingface.co/datasets/mwritescode/slither-audited-smart-contracts | 基于 Slither 检测结果的大规模弱标签来源。 |
| `scrawld` | ScrawlD | https://github.com/sujeetc/ScrawlD | 用于低频漏洞类别扩充和源码支撑样本补充。 |
| `smart_contract_vulndb` | Smart Contract VulnDB / SCVD | https://www.scvd.dev/ | 漏洞描述和发现级元数据来源，用于候选样本挖掘。 |
| `smart_contract_sanctuary_ethereum` | Smart Contract Sanctuary | https://github.com/tintinweb/smart-contract-sanctuary | 源码恢复辅助来源，不作为主要标签来源。 |

## 本地 raw 文件数参考

这些数量来自本地 `data/external/<source>/` 目录的文件统计，仅用于记录数据整理过程。公开仓库不上传这些 raw 文件。

| 来源 ID | 本地 raw 文件数 | 公开发布策略 |
|---|---:|---|
| `dappscan` | 30,672 | 不再分发原始文件。 |
| `scrawld` | 1,960 | 不再分发原始文件。 |
| `slither_audited_smart_contracts` | 12 | 不以 raw 数据形式再分发。 |
| `smart_contract_vulndb` | 3 | 不再分发原始快照；可发布派生元数据。 |
| `smartbugs_curated` | 159 | 不再分发原始合约。 |
| `solidifi_benchmark` | 5,108 | 不再分发原始合约。 |

受长路径、子模块和同步盘占位文件影响，本地 raw 文件数可能不是严格的公开数据规模指标。正式数据规模应以合并数据和 processed 数据统计为准。

## 规范化中间文件数

以下数量来自本地 `data/staging/<source>/` 目录中的规范化 JSON 和统计文件。

| 来源 ID | 规范化中间文件数 |
|---|---:|
| `dappscan` | 5 |
| `scrawld` | 2 |
| `slither_audited_smart_contracts` | 5 |
| `smart_contract_vulndb` | 2 |
| `smartbugs_curated` | 8 |
| `solidifi_benchmark` | 8 |

## 合并数据中的来源贡献

以下统计来自 `data/merged/*.stats.json`。

| 来源 ID | `has_vul_merged_stage0` | `vul_type_merged_stage0` | `vul_line_merged_stage0` |
|---|---:|---:|---:|
| `solidifi_benchmark` | 24,178 | 24,178 | 24,178 |
| `dappscan` | 455 | 455 | 0 |
| `slither_audited_smart_contracts` | 80,645 | 70,940 | 0 |
| 合计 | 105,278 | 95,573 | 24,178 |

## 推荐 processed 划分中的来源贡献

以下统计来自 `data/prepared/balanced_stage1_resplit_721/build_report.json`。

| 来源 ID | `has_vul_721_stratified_v1` | `vul_type_721_stratified_v1` | `vul_line_721_stratified_v1` |
|---|---:|---:|---:|
| `dappscan` | 453 | 455 | 464 |
| `Empirical-Analysis-of-Vulnerability-Detection-Tools-for-Solidity-Smart-Contracts` | 2,182 | 1,609 | 1,519 |
| `scrawld` | 1,951 | 1,909 | 1,952 |
| `slither_audited_smart_contracts` | 18,714 | 15,217 | 2,815 |
| `solidifi_benchmark` | 1,141 | 5,204 | 5,741 |
| 合计 | 24,441 | 24,394 | 12,491 |
