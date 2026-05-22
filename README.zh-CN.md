# 智能合约漏洞数据集

本仓库提供一个面向智能合约漏洞检测研究的大规模公开数据集，支持漏洞存在性判断、漏洞类型分类和漏洞行定位三类任务。数据集整合多个公开来源，并通过统一的标签空间、清洗规则、切分协议和元数据说明组织为可复现实验数据。

仓库名称：`smart-contract-vuln-dataset`。

英文版本：[README.md](README.md)。

## 数据集特点

- 漏洞存在性判断合并数据：105,278 条样本。
- 漏洞类型分类合并数据：95,573 条样本。
- 漏洞行定位合并数据：24,178 条样本。
- 整合 8 个公开来源，覆盖人工整理基准、注入式漏洞基准、审计来源、静态分析弱标签和漏洞发现库。
- 构建 19,557 条低频类别候选样本，形成 3,157 条复核样本，并确认 2,666 条可用于后续数据构建的低频类别样本。
- 覆盖 8 类常见智能合约漏洞。
- 提供三类任务的训练集、验证集和测试集划分。
- 发布规范化中间数据、整理后任务数据、数据构建工具和元数据说明。
- 不公开原始 raw 数据。

据我们所知，该数据集是当前公开可获得的最大规模智能合约漏洞数据集之一，覆盖漏洞存在性判断、漏洞类型分类和漏洞行级定位三类任务。

## 支持任务

| 任务 ID | 任务名称 | 说明 |
|---|---|---|
| `has_vul` | 漏洞存在性判断 | 判断样本是否包含已知漏洞。 |
| `vul_type` | 漏洞类型分类 | 对样本进行多标签漏洞类型分类。 |
| `vul_line` | 漏洞行定位 | 预测一个或多个漏洞所在代码行。 |

## 数据规模

### 合并数据

| 数据集 | 样本数 | 用途 |
|---|---:|---|
| `has_vul_merged_stage0` | 105,278 | 漏洞存在性判断 |
| `vul_type_merged_stage0` | 95,573 | 漏洞类型分类 |
| `vul_line_merged_stage0` | 24,178 | 漏洞行定位 |

### 推荐整理后划分

当前推荐公开版本为 `balanced_stage1_resplit_721`。

| 数据集 | 训练集 | 验证集 | 测试集 | 总计 |
|---|---:|---:|---:|---:|
| `has_vul_721_stratified_v1` | 17,411 | 4,667 | 2,363 | 24,441 |
| `vul_type_721_stratified_v1` | 18,573 | 3,829 | 1,992 | 24,394 |
| `vul_line_721_stratified_v1` | 10,155 | 1,529 | 807 | 12,491 |

## 漏洞类型

| 标签 | 含义 |
|---|---|
| `access_control` | 访问控制或授权相关漏洞 |
| `arithmetic` | 整数溢出、下溢或算术相关漏洞 |
| `bad_randomness` | 不安全或可预测随机数 |
| `denial_service` | 拒绝服务漏洞 |
| `front_running` | 抢跑或交易顺序依赖相关漏洞 |
| `reentrancy` | 重入漏洞 |
| `time_manipulation` | 时间戳依赖或时间操纵漏洞 |
| `unchecked_low_calls` | 未检查低级调用、未检查发送或未处理外部调用返回值 |

## 数据来源

本数据集整合并规范化了多个公开智能合约漏洞数据来源：

- [Empirical Analysis of Vulnerability Detection Tools for Solidity Smart Contracts](https://github.com/fsalzano/Empirical-Analysis-of-Vulnerability-Detection-Tools-for-Solidity-Smart-Contracts)
- [SmartBugs Curated](https://github.com/smartbugs/smartbugs-curated)
- [SolidiFI Benchmark](https://github.com/DependableSystemsLab/SolidiFI-benchmark)
- [DAppSCAN](https://github.com/InPlusLab/DAppSCAN)
- [Slither Audited Smart Contracts](https://huggingface.co/datasets/mwritescode/slither-audited-smart-contracts)
- [ScrawlD](https://github.com/sujeetc/ScrawlD)
- [Smart Contract VulnDB / SCVD](https://www.scvd.dev/)
- [Smart Contract Sanctuary](https://github.com/tintinweb/smart-contract-sanctuary)

本仓库不公开原始 raw 数据。对于再分发权限不明确的来源，本仓库仅提供来源链接、下载说明、转换脚本和允许公开的派生元数据，不上传原始源码包、原始审计报告或完整 raw 快照。

各来源的文件数和样本贡献量见 [docs/source_usage.md](docs/source_usage.md)。

各来源的处理、清理、去重和补充流程见 [docs/data_processing_and_augmentation.md](docs/data_processing_and_augmentation.md)。

数据库建设工作量说明见 [docs/construction_effort.md](docs/construction_effort.md)。

许可证核查和授权申请模板见 [metadata/upstream_license_review.zh-CN.md](metadata/upstream_license_review.zh-CN.md) 与 [metadata/authorization_requests.zh-CN.md](metadata/authorization_requests.zh-CN.md)。

## 数据格式

每条样本采用统一 JSON schema，核心字段包括：

```json
{
  "sample_id": "source::split::item",
  "source_dataset": "solidifi_benchmark",
  "source_split": "train",
  "source_path": "path/or/original/id",
  "granularity": "contract",
  "contract_name": "Example",
  "function_name": null,
  "context": ["pragma solidity ...", "contract Example { ... }"],
  "has_vulnerability": 1,
  "vulnerabilities": [
    {
      "type": "reentrancy",
      "line": 42,
      "line_end": 42,
      "source_taxonomy": "source taxonomy name",
      "source_label": "original source label",
      "evidence": [],
      "metadata": {}
    }
  ],
  "label_confidence": "silver",
  "label_origin": "source_annotation",
  "dedup_hash_raw": "...",
  "dedup_hash_normalized": "...",
  "metadata": {}
}
```

## 使用示例

```python
import json
from pathlib import Path

path = Path("data/processed/has_vul_721_stratified_v1/train.json")
samples = json.loads(path.read_text(encoding="utf-8"))

print("样本数量:", len(samples))
print("字段:", samples[0].keys())
print("漏洞存在性标签:", samples[0]["has_vulnerability"])
```

## 数据构建流程

1. 收集多个公开智能合约漏洞数据来源。
2. 将各来源转换为统一样本格式。
3. 将不同来源的漏洞标签映射到统一漏洞分类体系。
4. 基于原始代码和规范化代码哈希进行去重。
5. 按任务合并数据。
6. 构建训练集、验证集和测试集。
7. 审计样本数量、标签分布、来源分布、重复样本和漏洞行标注有效性。

## 引用方式

如果使用本数据集，请引用数据集仓库和相关论文：

```bibtex
@dataset{xu_smart_contract_vulnerability_dataset_2026,
  title  = {A Large-Scale Smart Contract Vulnerability Dataset},
  author = {Xu, Daming},
  year   = {2026},
  publisher = {GitHub},
  url    = {https://github.com/<your-github-username>/smart-contract-vuln-dataset}
}
```

同时，请根据实际使用的数据子集引用对应的原始公开数据来源。

## 许可证说明

- 本仓库自有代码和文档使用 MIT。
- 自行整理的统计、schema、标签映射和元数据使用 CC BY 4.0。
- 原始 raw 数据不上传。
- 如果整理后样本仍包含上游源码内容，则仅在对应上游许可证允许再分发时公开；否则使用来源指针和重建脚本替代。
- 本仓库保留所有上游来源的引用、许可证和致谢信息。

## 局限性

本数据集整合了人工整理标签、注入型漏洞标签、审计来源标签、静态分析工具弱标签和候选样本复核标签。不同来源的标签置信度、粒度和噪声水平并不完全一致。使用该数据集进行模型评测或论文对比时，应明确报告数据版本、任务定义、数据划分和评价指标。
