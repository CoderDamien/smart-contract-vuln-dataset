# 数据来源

本文档记录本数据集整合的公开来源、使用方式、许可证状态和发布策略。

本仓库不公开原始 raw 数据。对于再分发权限不明确或合约源码保留原始许可证的来源，本仓库只发布来源链接、下载说明、转换脚本、统计数据和允许公开的派生元数据。

文件数和样本贡献量见 [source_usage.md](source_usage.md)。处理、清理和补充流程见 [data_processing_and_augmentation.md](data_processing_and_augmentation.md)。

## 来源概览

| 来源 ID | 显示名称 | 角色 |
|---|---|---|
| `Empirical-Analysis-of-Vulnerability-Detection-Tools-for-Solidity-Smart-Contracts` | Empirical Analysis of Vulnerability Detection Tools for Solidity Smart Contracts | 原始论文数据核心来源 |
| `smartbugs_curated` | SmartBugs Curated | 人工整理基准 |
| `solidifi_benchmark` | SolidiFI Benchmark | 注入式漏洞基准 |
| `dappscan` | DAppSCAN | 真实 DApp 审计与源码来源 |
| `slither_audited_smart_contracts` | Slither Audited Smart Contracts | Slither 弱标签大规模来源 |
| `scrawld` | ScrawlD | 低频类别扩充来源 |
| `smart_contract_vulndb` | Smart Contract VulnDB / SCVD | 发现级漏洞元数据 |
| `smart_contract_sanctuary_ethereum` | Smart Contract Sanctuary | 源码恢复辅助来源 |

## 许可证与标注策略

| 来源 | 许可证/条款概况 | 发布策略 |
|---|---|---|
| SmartBugs Curated | 仓库为 Apache-2.0；合约保留原始许可证。 | 标注来源和 Apache-2.0；不再分发 raw 合约。 |
| SolidiFI Benchmark | 仓库材料为 MIT；原始合约保留原始许可证。 | 标注 MIT 和论文引用；不再分发 raw 合约。 |
| DAppSCAN | 未观察到清晰仓库级 license。 | 只发布引用、统计和重建说明；含源码再发布需授权。 |
| Slither Audited Smart Contracts | Hugging Face 标注 MIT；其中 Solidity 源码可能保留原始许可证。 | 可标注 MIT 元数据；默认不再分发源码。 |
| ScrawlD | README 要求引用；未观察到清晰仓库级 license。 | 只发布引用、统计和重建说明；含源码再发布需授权。 |
| Smart Contract VulnDB / SCVD | 网站说明 source 为 MIT，dataset 为 CC0。 | 可发布派生发现级元数据，保留来源和访问日期。 |
| Smart Contract Sanctuary | README 提供引用；合约来自 Etherscan 等公开来源，可能保留各自许可证。 | 仅作为源码恢复引用；默认不再分发恢复源码。 |
| Empirical Analysis... | 未确认清晰可再分发 license。 | 标注来源；含源码 processed 样本发布前需授权或改为来源指针。 |

