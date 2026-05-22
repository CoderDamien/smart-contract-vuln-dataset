# 数据集构建流程

本文档说明统一智能合约漏洞数据集的构建流程。

## 流程概览

数据集通过以下阶段构建：

1. 收集公开数据来源。
2. 将每个来源转换为统一样本 schema。
3. 将不同来源的漏洞标签映射到统一标签空间。
4. 基于原始源码和规范化源码哈希进行去重。
5. 按任务合并多源数据。
6. 构建任务级训练集、验证集和测试集。
7. 审计标签分布、来源分布、重复样本和行号有效性。

## 阶段目录

| 阶段 | 目录 | 作用 |
|---|---|---|
| 原始来源 | `data/raw/` 或 `data/external/<source>/raw/` | 本地原始下载、克隆或快照；公开仓库不上传。 |
| 规范化中间数据 | `data/staging/<source>/` | 每个来源独立转换后的统一 JSON。 |
| 合并数据 | `data/merged/` | 按任务合并后的跨来源数据。 |
| 整理后数据 | `data/processed/` 或 `data/prepared/` | 可直接用于训练和评测的任务数据。 |
| 元数据 | `metadata/` | 数据统计、来源目录、schema 和发布记录。 |

## 标签映射

数据集将 DASP、SWC、SolidiFI bug type、ScrawlD 标签和 Slither detector 映射到 8 类统一漏洞标签：

`access_control`、`arithmetic`、`bad_randomness`、`denial_service`、`front_running`、`reentrancy`、`time_manipulation`、`unchecked_low_calls`。

无法稳定映射的标签会被标记为 `other` 或 `unknown`，并按任务规则过滤。

## 去重与切分

去重使用：

- `dedup_hash_raw`：原始源码上下文哈希。
- `dedup_hash_normalized`：去注释、去多余空白后的源码哈希。

推荐划分 `balanced_stage1_resplit_721` 使用 group-aware split，减少重复或近重复源码跨训练集、验证集和测试集泄漏。

## 推荐数据划分

| 数据集 | 训练集 | 验证集 | 测试集 | 总计 |
|---|---:|---:|---:|---:|
| `has_vul_721_stratified_v1` | 17,411 | 4,667 | 2,363 | 24,441 |
| `vul_type_721_stratified_v1` | 18,573 | 3,829 | 1,992 | 24,394 |
| `vul_line_721_stratified_v1` | 10,155 | 1,529 | 807 | 12,491 |

## 质量审计

发布前检查：

- 样本 ID 是否重复。
- 代码上下文是否为空。
- 行号是否越界。
- 标签是否属于统一标签空间。
- 来源分布和标签分布是否与统计文件一致。
- 上游来源、许可证和引用说明是否完整。

