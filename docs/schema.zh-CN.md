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
| `line` | integer/null | 否 | 漏洞起始行号。 |
| `line_end` | integer/null | 否 | 漏洞结束行号。 |
| `source_taxonomy` | string/null | 否 | 原始标签体系，例如 DASP、SWC、SolidiFI 或 Slither。 |
| `source_label` | string/null | 否 | 映射前的原始标签。 |
| `evidence` | list[string] | 是 | 证据或备注。 |
| `metadata` | object | 是 | 标注级元数据。 |

## 置信度

| 值 | 含义 |
|---|---|
| `gold` | 人工整理或人工验证标签。 |
| `silver` | 结构化基准或源码支撑标签。 |
| `bronze` | 弱标签、工具生成标签或候选标签。 |
| `unknown` | 置信度未确定。 |

