# 上游许可证核查

核查日期：2026-05-22

推荐仓库名：`smart-contract-vuln-dataset`

公开发布策略：不再分发原始 raw 数据。

## 结论摘要

| 来源 | 公开链接 | 许可证/条款观察 | 处理结论 |
|---|---|---|---|
| SmartBugs Curated | https://github.com/smartbugs/smartbugs-curated | GitHub 页面显示 Apache-2.0；README 说明合约保留原始许可证。 | 需要标注 Apache-2.0 和来源；不发布 raw 合约。 |
| SolidiFI Benchmark | https://github.com/DependableSystemsLab/SolidiFI-benchmark | LICENSE 为 MIT，同时说明原始合约保留原始许可证。 | 需要标注 MIT、引用论文；不发布 raw 合约。 |
| DAppSCAN | https://github.com/InPlusLab/DAppSCAN | 未观察到清晰仓库级 license。 | 不发布 raw；若发布含源码 processed 样本，需要授权。 |
| Slither Audited Smart Contracts | https://huggingface.co/datasets/mwritescode/slither-audited-smart-contracts | Hugging Face 页面显示 license 为 MIT；其中源码可能保留原始许可证。 | 可标注 MIT 元数据；源码默认不再分发。 |
| ScrawlD | https://github.com/sujeetc/ScrawlD | README 请求引用，未观察到清晰仓库级 license。 | 不发布 raw；若发布含源码 processed 样本，需要授权。 |
| Smart Contract VulnDB / SCVD | https://www.scvd.dev/ | 网站说明 SOURCE: MIT，DATASET: CC0。 | 可发布派生发现级元数据，标注来源和访问日期。 |
| Smart Contract Sanctuary | https://github.com/tintinweb/smart-contract-sanctuary | README 提供引用；合约文件可能保留各自源码许可证。 | 只作为源码恢复引用；不默认发布恢复源码。 |
| Empirical Analysis of Vulnerability Detection Tools for Solidity Smart Contracts | https://github.com/fsalzano/Empirical-Analysis-of-Vulnerability-Detection-Tools-for-Solidity-Smart-Contracts | 未确认清晰可再分发 license。 | 若发布含源码 processed 样本，需要授权或改为来源指针。 |

## 需要标注的来源

- SmartBugs Curated：标注 Apache-2.0、项目 URL 和原始合约许可证保留说明。
- SolidiFI Benchmark：标注 MIT、项目 URL、ISSTA 2020 论文引用和原始合约许可证保留说明。
- Slither Audited Smart Contracts：标注 Hugging Face 数据集 URL、MIT license 和 Etherscan 验证源码来源说明。
- ScrawlD：标注项目 URL 和论文引用。
- Smart Contract Sanctuary：标注项目 URL 和 README 中给出的引用格式。
- SCVD：标注网站 URL、SOURCE MIT、DATASET CC0 和访问日期。

## 需要授权或避免再分发的情况

如果 processed 文件包含 Solidity 源码全文，则以下来源需要特别谨慎：

- DAppSCAN：未见清晰仓库级 license。
- ScrawlD：未见清晰仓库级 license。
- Empirical Analysis...：未确认清晰可再分发 license。
- Smart Contract Sanctuary：合约源码可能保留各自许可证。
- SmartBugs Curated / SolidiFI / Slither Audited：虽然仓库或数据集有许可证，但合约源码可能保留原始许可证。

保守发布方案：

1. 不上传 raw 数据。
2. 对 license 不清晰或源码许可证混合的来源，不发布含源码全文的 processed 样本。
3. 发布 source pointer、sample ID、标签、统计、schema、映射规则和重建脚本。
4. 如确需发布含源码样本，先向维护者申请书面授权。

