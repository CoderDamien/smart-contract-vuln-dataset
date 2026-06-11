# 数据 schema

本文档描述统一样本 schema。

## 样本对象

| 字段 | 类型 | 必需 | 说明 |
|---|---|---:|---|
| `sample_id` | string | 是 | 稳定样本 ID。 |
| `source_dataset` | string | 是 | 来源数据集 ID。 |
| `source_split` | string | 是 | 原始或构造的数据划分。 |
| `source_path` | string/null | 否 | 原始路径、URL 或来源 ID。 |
| `granularity` | string | 是 | `contract`、`file`、`function`、`finding` 或 `project`。 |
| `contract_name` | string/null | 否 | 合约名。 |
| `function_name` | string/null | 否 | 函数名。 |
| `context` | list[string] | 是 | 模型输入代码或文本上下文。 |
| `has_vulnerability` | integer | 是 | `1` 表示存在漏洞，`0` 表示无已知漏洞。 |
| `vulnerabilities` | list[object] | 是 | 漏洞标注列表；clean 样本为空列表。 |
| `label_confidence` | string | 是 | `gold`、`silver`、`bronze` 或 `unknown`。 |
| `label_origin` | string | 是 | 标签来源，例如人工整理、工具输出、注入式基准或复核结果。 |
| `dedup_hash_raw` | string/null | 否 | 原始上下文 SHA-256 哈希。 |
| `dedup_hash_normalized` | string/null | 否 | 规范化上下文 SHA-256 哈希。 |
| `metadata` | object | 是 | 其他来源元数据。 |

## 漏洞对象

| 字段 | 类型 | 必需 | 说明 |
|---|---|---:|---|
| `type` | string | 是 | 统一漏洞类型。 |
| `line` | integer/null | 否 | 向后兼容的漏洞起始行。对于 `vul_line`，该字段是相对于已发布 `context` 字段的 1-based 行号，不一定是原始源码文件行号。 |
| `line_end` | integer/null | 否 | 与 `line` 使用同一坐标系的漏洞结束行。 |
| `line_coordinate_system` | string/null | 否 | `line` 与 `line_end` 的坐标系。当前 `vul_line` 发布版本使用 `context_relative_1based`。 |
| `line_scope` | string/null | 否 | `line` 所属范围；当前值为 `context`。 |
| `context_start_line` | integer/null | 否 | `context[0]` 对应的原始源码文件行号；仅在可还原时提供。 |
| `source_line` | integer/null | 否 | 原始源码文件中的漏洞起始行；仅在可还原时提供。 |
| `source_line_end` | integer/null | 否 | 原始源码文件中的漏洞结束行；仅在可还原时提供。 |
| `raw_loc` | integer/null | 否 | 来源数据提供的原始位置值；例如 SolidiFI 的 bug log `loc` 字段。 |
| `raw_length` | integer/null | 否 | 来源数据提供的原始漏洞范围长度。 |
| `source_mapping_status` | string/null | 否 | `available` 表示可还原 `source_line`；`unavailable` 表示当前只发布 context-relative 行号。 |
| `source_mapping_method` | string/null | 否 | `source_line` 的映射依据，例如 `raw_loc_minus_context_start`、`context_start_line_offset`、`full_context_identity_by_source_dataset`、`legacy_full_context_identity` 或 `unattributed_full_context_identity`。 |
| `source_taxonomy` | string/null | 否 | 原始标签体系，例如 DASP、SWC、SolidiFI 或 Slither。 |
| `source_label` | string/null | 否 | 映射前的原始标签。 |
| `evidence` | list[string] | 是 | 证据或备注。 |
| `metadata` | object | 是 | 标注级元数据。 |

除非显式提供 `source_line`，否则行级标签均为相对于已发布 `context` 字段的 1-based 行号。原有 `vulnerabilities[].line` 字段保留，用于向后兼容。

## 置信度

| 值 | 含义 |
|---|---|
| `gold` | 人工整理或人工验证标签。 |
| `silver` | 结构化基准或源码支撑标签。 |
| `bronze` | 弱标签、工具生成标签或候选标签。 |
| `unknown` | 置信度未确定。 |
