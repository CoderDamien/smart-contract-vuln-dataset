# 工具

该目录用于放置公开发布版数据处理脚本。

建议包含：

- `import_datasets.py`：将原始上游数据导入统一 schema。
- `dedup_external_datasets.py`：计算哈希并去重。
- `merge_external_datasets.py`：按任务合并多源数据。
- `build_balanced_task_datasets.py`：构建训练集、验证集和测试集。
- `validate_schema.py`：校验发布 JSON 文件。
- `summarize_dataset.py`：生成 README 和 metadata 使用的数据统计。

公开脚本应避免私有路径、token、服务器地址和论文内部临时说明。

