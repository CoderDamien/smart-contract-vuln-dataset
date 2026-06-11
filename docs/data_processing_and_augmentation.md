# 数据处理、清理与补充流程

本文档说明本数据集如何从多个公开智能合约漏洞来源构建统一数据集，包括各来源的处理方式、清理规则、标签映射、去重方法、低频类别补充和最终任务数据生成流程。

本仓库不公开原始 raw 数据。数据处理流程保留来源链接、规范化中间文件、统计结果和可复现处理工具。

数据建设工作量摘要见 [construction_effort.md](construction_effort.md)。

## 总体处理流程

数据构建流程分为七个阶段：

1. 来源登记：为每个上游数据源记录公开链接、来源类型、支持任务和许可证状态。
2. 原始数据读取：从本地 raw 目录读取各来源数据，但 raw 数据不进入公开仓库。
3. 统一格式转换：将不同来源转换为统一 JSON schema。
4. 标签映射：将 SWC、DASP、SolidiFI bug type、ScrawlD 标签和 Slither detector 映射到统一漏洞类型空间。
5. 清理与过滤：移除无法映射、无有效标签、无有效行号或与任务定义不兼容的样本。
6. 去重与合并：使用原始代码哈希和规范化代码哈希去重，再按任务合并。
7. 任务数据构建：生成 `has_vul`、`vul_type`、`vul_line` 三类任务的训练集、验证集和测试集。

## 统一标签空间

所有来源被映射到以下 8 类漏洞：

| 统一标签 | 主要映射来源 |
|---|---|
| `access_control` | Access Control、tx.origin、授权类 Slither detector |
| `arithmetic` | Integer Overflow/Underflow、SWC-101、算术类 detector |
| `bad_randomness` | Bad Randomness、weak-prng、SWC-120 |
| `denial_service` | Denial of Service、DoS、SWC-113、SWC-128 |
| `front_running` | Front Running、TOD、Transaction Order Dependence、SWC-114 |
| `reentrancy` | Reentrancy、SWC-107、reentrancy detector |
| `time_manipulation` | Timestamp Dependency、Time Manipulation、SWC-116 |
| `unchecked_low_calls` | Unchecked Low Level Calls、Unchecked Send、Unhandled Exceptions、SWC-104 |

无法稳定映射的标签会被标记为 `other` 或 `unknown`。正式任务数据中，`vul_type` 和 `vul_line` 会优先过滤掉无法进入统一标签空间的样本。

## 各来源处理方式

### Empirical-Analysis-of-Vulnerability-Detection-Tools-for-Solidity-Smart-Contracts

该来源是原始论文数据的核心基础，提供早期的 `dataset-all` 和 `dataset-onlyV` 数据划分。

处理工作：

- 保留原始训练集、验证集、测试集的基本划分信息。
- 作为后续外部数据去重的基准来源。
- 统一纳入三类任务：漏洞存在性判断、漏洞类型分类和漏洞行定位。
- 在最终 processed 数据中使用公开仓库名作为来源名称。

清理工作：

- 读取 `train.json`、`val.json`、`test.json`。
- 检查样本字段、标签字段和代码上下文。
- 对代码上下文计算原始哈希和规范化哈希，用于与外部来源去重。
- 对漏洞定位任务检查行号有效性，剔除越界或缺失行号的定位标签。

补充作用：

- 作为原始基准数据，参与最终三类任务划分。
- 在推荐 processed split 中贡献：
  - `has_vul`: 2,182 条样本
  - `vul_type`: 1,609 条样本
  - `vul_line`: 1,519 条样本

### SmartBugs Curated

SmartBugs Curated 是人工整理的智能合约漏洞基准来源。

处理工作：

- 读取 curated 合约和漏洞标注文件。
- 将 DASP 等来源标签映射到统一标签空间。
- 保留合约级或可恢复的行级信息。
- 生成规范化 staging 文件和统计文件。

清理工作：

- 跳过无法读取的合约文件。
- 跳过无法映射到统一标签空间的标签。
- 对源代码上下文计算去重哈希。
- 与原始基准数据进行重复检测。

补充作用：

- 用作高质量人工整理来源。
- 在当前发布统计中作为已登记来源和中间处理来源保留。
- 后续可根据许可证确认情况纳入公开 processed 数据或作为重建来源。

### SolidiFI Benchmark

SolidiFI Benchmark 提供注入式漏洞样本和 bug log，是当前漏洞定位任务的重要来源。

处理工作：

- 扫描 `.sol` 合约文件和 `buglog_*.csv` 等 bug log 文件。
- 从 bug log 中解析漏洞类型、漏洞行号和相关元数据。
- 将 SolidiFI 原始漏洞类型映射到统一标签空间。
- 生成函数级或合约级规范化样本。

清理工作：

- 修正常见标签别名和拼写差异，例如 `Re-entrancy`、`Timestamp Dependency`、`Unchecked Send` 等。
- 解析并标准化行号、起始行和结束行。
- 对没有有效合约匹配或没有有效标签的记录进行剔除。
- 对行号越界的定位标签进行过滤。
- 保留 synthetic/injected 来源属性，避免与真实漏洞样本混淆。

补充作用：

- 大幅补充行级定位样本。
- 在 merged 数据中贡献：
  - `has_vul`: 24,178 条样本
  - `vul_type`: 24,178 条样本
  - `vul_line`: 24,178 条样本
- 在推荐 processed split 中贡献：
  - `has_vul`: 1,141 条样本
  - `vul_type`: 5,204 条样本
  - `vul_line`: 5,741 条样本

### DAppSCAN

DAppSCAN 提供真实 DApp 审计和源码相关数据。

处理工作：

- 读取 `DAppSCAN-source/SWCsource` 下的 SWC 报告。
- 根据报告中的 `filePath` 找回对应 Solidity 源文件。
- 从 SWC 报告中解析漏洞类别、函数信息和行号。
- 将 SWC 编号映射到统一标签空间。
- 生成 file-level 规范化样本。

清理工作：

- 跳过缺少 `filePath` 或 SWC 列表异常的报告。
- 跳过找不到对应 Solidity 源文件的报告。
- 跳过没有可映射漏洞标签的报告。
- 对行号字段进行整数解析，只保留正整数行号。
- 生成缺失源文件数、跳过样本数和标签分布统计。

补充作用：

- 补充真实 DApp 场景下的漏洞类型和存在性样本。
- 在 merged 数据中贡献：
  - `has_vul`: 455 条样本
  - `vul_type`: 455 条样本
- 在推荐 processed split 中贡献：
  - `has_vul`: 453 条样本
  - `vul_type`: 455 条样本
  - `vul_line`: 464 条样本

### Slither Audited Smart Contracts

Slither Audited Smart Contracts 是基于 Slither 检测结果的大规模弱标签来源。

处理工作：

- 读取 Hugging Face parquet 数据。
- 解析每条样本中的合约源码和 Slither `results` 字段。
- 提取 detector 结果并映射到统一漏洞标签。
- 将 `ignore`、`safe` 等 detector 结果排除。
- 生成 contract-level 规范化样本。

清理工作：

- 跳过无法解析的 detector 结果。
- 将未覆盖的 detector 映射为 `other`，并在正式任务中按需要过滤。
- 保留 detector 原始名称、detector 数量和 parquet 来源文件。
- 将该来源标注为弱标签来源，置信度低于人工整理数据。
- 与原始基准数据进行规范化哈希去重。

补充作用：

- 大规模补充 `has_vul` 和 `vul_type` 训练样本。
- 在 merged 数据中贡献：
  - `has_vul`: 80,645 条样本
  - `vul_type`: 70,940 条样本
- 在推荐 processed split 中贡献：
  - `has_vul`: 18,714 条样本
  - `vul_type`: 15,217 条样本
  - `vul_line`: 2,815 条样本

### ScrawlD

ScrawlD 用于补充低频漏洞类别，尤其是 `denial_service` 和 `front_running`。

处理工作：

- 读取 ScrawlD 的漏洞元数据文件。
- 尝试根据合约名、路径或 ID 匹配 Solidity 源文件。
- 对无法找到源码的记录生成 metadata-only 样本。
- 将 ScrawlD 标签映射到统一标签空间。
- 保留源码匹配状态和原始标签信息。

清理工作：

- 跳过无法映射到统一标签空间的标签。
- 解析并校验行号。
- 区分源码支撑样本和 metadata-only 样本。
- 对低频类别候选样本进行后续筛选和确认。

补充作用：

- 补充低频类别样本池。
- 用于构建 `denial_service` 和 `front_running` 的候选集、复核集和确认集。
- 在推荐 processed split 中贡献：
  - `has_vul`: 1,951 条样本
  - `vul_type`: 1,909 条样本
  - `vul_line`: 1,952 条样本

### Smart Contract VulnDB / SCVD

Smart Contract VulnDB / SCVD 提供漏洞发现级描述和真实漏洞案例信息。

处理工作：

- 读取漏洞发现 JSON 快照。
- 提取漏洞标题、描述、分类、来源链接和相关元数据。
- 将发现级记录转为候选样本。
- 用于低频类别候选挖掘，而不是直接作为行级训练样本。

清理工作：

- 过滤缺少有效漏洞描述或标签的记录。
- 将原始分类映射到统一标签空间。
- 保留来源链接和发现级元数据。
- 对候选样本进行人工或辅助复核后才进入确认集。

补充作用：

- 为 `front_running`、`denial_service` 等低频类别提供候选来源。
- 作为候选发现库和复核依据，不直接等同于最终训练标签。

### Smart Contract Sanctuary

Smart Contract Sanctuary 主要用于源码恢复。

处理工作：

- 根据合约地址、路径或相关元数据查找可用 Solidity 源码。
- 为缺少源码的候选样本提供 source-backed 支撑。
- 作为辅助来源记录，不作为主要标签来源。

清理工作：

- 不将恢复源码直接作为 raw 数据公开。
- 保留源码恢复状态、来源路径和可追溯信息。
- 只有在标签来源明确、许可证允许且样本通过清理后，才进入任务数据。

补充作用：

- 提升候选样本的源码可用性。
- 支持低频类别样本从文本发现记录转为可用于模型输入的源码样本。

## 去重策略

去重使用两类哈希：

- `dedup_hash_raw`：对原始代码上下文拼接后计算 SHA-256。
- `dedup_hash_normalized`：去除注释、裁剪行尾空白、压缩空白字符后计算 SHA-256。

处理步骤：

1. 先对核心原始基准来源计算哈希集合。
2. 对外部来源样本计算相同哈希。
3. 如果外部样本的规范化哈希已存在，则记为重复样本。
4. 重复样本单独保存到 duplicates 文件，未重复样本进入后续合并。
5. 最终 processed split 使用 group-aware split，避免相同或近似代码跨训练集、验证集和测试集泄漏。

## 任务级过滤规则

### `has_vul`

- 保留漏洞样本和 clean 样本。
- 根据 `has_vulnerability` 字段构建二分类任务。
- 对训练集进行正负样本均衡，使 clean 和 vulnerable 尽量保持可比。

### `vul_type`

- 仅保留包含已知统一漏洞标签的样本。
- 过滤 `unknown`、`other` 或无法映射的标签。
- 支持多标签样本，一个合约可以包含多个漏洞类型。
- 通过类别目标和来源优先级缓解类别不均衡。

### `vul_line`

- 仅保留包含有效行号的漏洞样本。
- 剔除缺失行号、行号小于 1 或超过代码总行数的标签。
- 将漏洞定位定义为多行预测任务，而不是单个浮点数回归任务。
- 支持一对多或多对多的漏洞行匹配。
- 已发布数据中的 `vulnerabilities[].line` 和 `line_end` 使用 `context_relative_1based` 坐标系，即相对于已发布 `context` 字段的 1-based 行号。
- 仅当可以可靠还原时，原始源码文件行号通过 `source_line` 和 `source_line_end` 提供；否则 `source_mapping_status` 为 `unavailable`。
- 第一篇论文当前按 representative vulnerable start line / vulnerable start-line evaluation 报告结果；`line_end` 和 `source_line_end` 保留给后续 range-aware 评价。

## 低频类别补充

低频类别主要包括：

- `denial_service`
- `front_running`
- `bad_randomness`
- 部分来源中的 `reentrancy`、`time_manipulation` 等少样本组合

补充流程：

1. 从 ScrawlD、Smart Contract VulnDB / SCVD、DAppSCAN 和其他来源抽取候选样本。
2. 将候选样本映射到统一标签空间。
3. 区分 source-backed 样本和 metadata-only 样本。
4. 对候选池进行去重和来源过滤。
5. 生成 review pack 和 review sheet。
6. 对确认样本写入 confirmed 数据。
7. 将确认样本合并到 merged 或 processed 数据构建流程。

这种方式避免直接把弱标签候选样本当作高置信度训练数据，同时提高低频类别覆盖率。

## 均衡与切分

推荐 processed split 为 `balanced_stage1_resplit_721`。

处理策略：

- `has_vul` 任务按 clean/vulnerable 进行二分类均衡。
- `vul_type` 任务按统一漏洞类型设置最小和最大目标数量。
- `vul_line` 任务优先保留有效行级监督样本。
- 使用 `dedup_hash_normalized | dedup_hash_raw | context_sha256` 作为 group split key，减少相似样本跨 split 泄漏。
- 输出每个任务的 `train.json`、`val.json`、`test.json` 和构建报告。

## 审计与质量控制

数据发布前执行以下检查：

- 样本 ID 是否重复。
- 代码上下文是否为空。
- 标签是否属于统一标签空间。
- clean 样本是否错误包含漏洞记录。
- vulnerable 样本是否缺少漏洞记录。
- 行号是否越界。
- 同一代码是否跨训练集、验证集、测试集重复出现。
- 各来源贡献量和标签分布是否与统计文件一致。
- 上游来源、许可证和引用信息是否完整。
