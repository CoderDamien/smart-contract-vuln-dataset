# 数据库建设工作量说明

本数据集不是对单一公开数据集的简单转存，而是围绕智能合约漏洞检测三类任务进行的多源数据治理工程。建设过程包括数据源筛选、格式统一、标签映射、重复样本清理、低频类别补充、候选样本复核、行级标签校验、任务级切分和发布文档整理。

## 建设工作概览

| 工作项 | 产出或规模 |
|---|---:|
| 上游公开来源 | 8 个 |
| 本地 raw 文件规模参考 | 37,914 个文件 |
| 规范化 staging 文件 | 30 个文件 |
| 候选样本文件 | 8 个文件 |
| 复核包文件 | 10 个文件 |
| 确认样本文件 | 8 个文件 |
| 合并数据和统计文件 | 21 个文件 |
| processed 数据和构建报告 | 72 个文件 |
| 数据处理与实验支持脚本 | 40+ 个 Python 脚本 |
| 最终 merged 样本规模 | 105,278 / 95,573 / 24,178 |
| 推荐 processed split 样本规模 | 24,441 / 24,394 / 12,491 |

其中，最终 merged 样本规模分别对应 `has_vul`、`vul_type` 和 `vul_line` 三类任务；推荐 processed split 样本规模对应 `balanced_stage1_resplit_721`。

## 多源数据整合工作

数据集整合了以下来源：

- Empirical-Analysis-of-Vulnerability-Detection-Tools-for-Solidity-Smart-Contracts
- SmartBugs Curated
- SolidiFI Benchmark
- DAppSCAN
- Slither Audited Smart Contracts
- ScrawlD
- Smart Contract VulnDB / SCVD
- Smart Contract Sanctuary

这些来源在数据格式、标签体系、样本粒度和标注置信度上差异明显。例如：

- 有的来源是人工整理基准。
- 有的来源是注入式漏洞基准。
- 有的来源是静态分析工具弱标签。
- 有的来源是审计报告或发现级漏洞描述。
- 有的来源只提供源码恢复能力，不直接提供标签。

因此，建设工作不是简单合并文件，而是将异构来源转换为统一数据协议。

## 统一 schema 建设

所有来源被转换为统一 JSON schema，核心字段包括：

- `sample_id`
- `source_dataset`
- `source_path`
- `granularity`
- `context`
- `has_vulnerability`
- `vulnerabilities`
- `label_confidence`
- `label_origin`
- `dedup_hash_raw`
- `dedup_hash_normalized`
- `metadata`

该 schema 支持合约级、文件级、函数级和发现级样本，并兼容漏洞存在性、漏洞类型和漏洞行定位三类任务。

## 标签体系统一工作

不同来源使用不同标签体系，例如 DASP、SWC、SolidiFI bug type、ScrawlD 标签和 Slither detector 名称。本数据集将这些标签统一映射到 8 类漏洞：

- `access_control`
- `arithmetic`
- `bad_randomness`
- `denial_service`
- `front_running`
- `reentrancy`
- `time_manipulation`
- `unchecked_low_calls`

标签治理工作包括：

- 合并同义标签，例如 `TOD`、`Transaction Order Dependence` 和 `front_running`。
- 统一低级调用类标签，例如 `Unchecked Send`、`Unhandled Exceptions` 和 `unchecked_low_calls`。
- 将 `tx.origin` 等授权问题归入 `access_control`。
- 对无法可靠映射的标签标记为 `other` 或 `unknown`。
- 在正式任务数据中按任务规则过滤不可用标签。

## 数据清理工作

清理流程覆盖以下问题：

- 原始文件缺失或路径失效。
- 源码读取失败或编码异常。
- 报告中缺少有效漏洞标签。
- 标签无法映射到统一漏洞空间。
- 行号缺失、行号非法或行号越界。
- clean 样本与漏洞记录冲突。
- vulnerable 样本缺少漏洞记录。
- 静态分析弱标签中的 `ignore`、`safe` 或不可用 detector。
- 多来源重复样本和近重复源码。

清理后，每个阶段都会生成统计文件，用于记录输入数量、保留数量、重复数量、跳过原因和标签分布。

## 去重工作

为了降低跨来源重复和训练/测试泄漏风险，数据集使用两类哈希：

- `dedup_hash_raw`：基于原始源码上下文。
- `dedup_hash_normalized`：去除注释、裁剪行尾空白、压缩空白字符后的规范化源码。

去重流程包括：

1. 先对原始核心基准来源计算哈希集合。
2. 对外部来源样本计算相同哈希。
3. 将规范化哈希重复的外部样本写入 duplicates 文件。
4. 将未重复样本写入 deduped 文件。
5. 在最终 processed split 中使用 group-aware split，避免相同或近似代码跨 split 出现。

## 低频类别补充工作

原始数据中 `front_running` 和 `denial_service` 等类别样本较少，难以支撑稳定评测。因此，数据构建中专门设计了低频类别补充流程。

### 候选样本挖掘

多源候选池规模：

| 目标类别 | 候选样本数 | 高置信候选 | 中置信候选 | 种子标注样本 | 启发式候选样本 |
|---|---:|---:|---:|---:|---:|
| `front_running` | 9,200 | 4,200 | 5,000 | 1,200 | 8,000 |
| `denial_service` | 10,357 | 5,357 | 5,000 | 1,357 | 9,000 |
| 合计 | 19,557 | 9,557 | 10,000 | 2,557 | 17,000 |

候选样本来自 ScrawlD、Slither Audited Smart Contracts、Smart Contract VulnDB / SCVD、SolidiFI Benchmark、DAppSCAN 和核心基准来源。

### 复核包构建

从候选池中构建复核包：

| 目标类别 | 复核样本数 |
|---|---:|
| `front_running` | 1,500 |
| `denial_service` | 1,657 |
| 合计 | 3,157 |

复核包同时生成 JSON 和 CSV，便于人工检查、辅助判断和后续追踪。

### 确认样本生成

复核后确认样本：

| 目标类别 | 接收样本 | 暂缓样本 |
|---|---:|---:|
| `front_running` | 1,201 | 299 |
| `denial_service` | 1,465 | 192 |
| 合计 | 2,666 | 491 |

只有确认样本才进入后续 confirmed 数据和 processed 数据构建流程。

## 三类任务构建工作

### 漏洞存在性判断

`has_vul` 任务处理工作包括：

- 保留 clean 和 vulnerable 样本。
- 统一 `has_vulnerability` 二分类标签。
- 引入大规模弱标签来源扩充训练数据。
- 对训练集进行正负样本均衡。
- 在推荐 processed split 中形成 24,441 条样本。

### 漏洞类型分类

`vul_type` 任务处理工作包括：

- 保留多标签漏洞信息。
- 过滤无法映射的 `other` 和 `unknown` 标签。
- 对不同来源的标签空间进行统一。
- 对低频类别进行候选挖掘和补充。
- 在推荐 processed split 中形成 24,394 条样本。

### 漏洞行定位

`vul_line` 任务处理工作包括：

- 将定位任务重新定义为多行预测任务。
- 保留一个或多个漏洞行标签。
- 过滤缺失行号、非法行号和越界行号。
- 使用 SolidiFI、ScrawlD、DAppSCAN 和核心基准来源补充行级监督信号。
- 在推荐 processed split 中形成 12,491 条样本。

## 处理工具链

数据构建过程配套了 40+ 个 Python 脚本，覆盖：

- 数据源检查
- 数据下载
- 数据导入
- 标签映射
- 去重
- 合并
- 低频候选池构建
- 复核包生成
- 确认样本生成
- 行级补充
- 均衡数据构建
- 重新切分
- 数据质量审计
- 统计汇总

这些工具使数据集能够从原始来源重建，并为后续论文复现实验提供可追踪依据。

## 发布工作

公开发布版本额外整理了：

- 中文 README
- 英文 README
- 数据来源说明
- 来源贡献统计
- 数据处理、清理与补充流程
- 数据 schema
- 使用示例
- 许可证说明
- 第三方来源 notice
- 引用文件 `CITATION.cff`
- 机器可读统计 JSON

这些内容用于让数据集不仅能被下载，还能被理解、引用、复现和审计。

