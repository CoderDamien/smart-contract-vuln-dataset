# 数据文件

该目录包含可公开下载的数据压缩包。

## merged 与 processed 的区别

| 数据层级 | 用途 | 使用场景 |
|---|---|---|
| `data/merged/` | 多源规范化、标签映射和基础清理后的大规模合并池。 | 当推荐 processed 数据量不够，需要自行扩充训练集、重新采样或重新切分时使用。 |
| `data/processed/` | 经过任务级过滤、均衡、去重和 train/validation/test 构建后的推荐正式基准。 | 直接训练、评测、复现实验和论文对比时使用。 |

`merged` 更大，因为它保留了更多规范化后的多源样本和源码上下文；`processed` 更小，因为它是经过任务筛选、类别均衡和切分控制后的正式基准数据。

## merged 数据包

| 文件 | 大小 | 样本数 | 内容 |
|---|---:|---:|---|
| `merged/has_vul_merged_stage0.tar.gz` | 605 MB | 105,278 | 漏洞存在性判断合并池。 |
| `merged/vul_type_merged_stage0.tar.gz` | 568 MB | 95,573 | 漏洞类型分类合并池。 |
| `merged/vul_line_merged_stage0.tar.gz` | 2.9 MB | 24,178 | 漏洞行定位合并池，包含 context-relative 行号坐标元数据。 |

## 推荐 processed 数据包

| 文件 | 大小 | 内容 |
|---|---:|---|
| `processed/balanced_stage1_resplit_721.tar.gz` | 210 MB | `has_vul`、`vul_type`、`vul_line` 三类任务的推荐训练集、验证集和测试集；`vul_line` 包含行号坐标元数据。 |

压缩包内容：

```text
balanced_stage1_resplit_721/
├── build_report.json
├── has_vul_721_stratified_v1/
│   ├── train.json
│   ├── val.json
│   └── test.json
├── vul_type_721_stratified_v1/
│   ├── train.json
│   ├── val.json
│   └── test.json
└── vul_line_721_stratified_v1/
    ├── train.json
    ├── val.json
    └── test.json
```

## 解压

```bash
tar -xzf data/processed/balanced_stage1_resplit_721.tar.gz -C data/processed/
tar -xzf data/merged/has_vul_merged_stage0.tar.gz -C data/merged/
tar -xzf data/merged/vul_type_merged_stage0.tar.gz -C data/merged/
tar -xzf data/merged/vul_line_merged_stage0.tar.gz -C data/merged/
```

## 说明

- 本仓库不再分发原始 raw 数据。
- merged 阶段的大型中间 JSON 暂未上传，因为多个文件单文件超过 3GB。
- 来源与许可证说明见 `metadata/upstream_license_review.zh-CN.md`。
- 对于 `vul_line`，`vulnerabilities[].line` 和 `line_end` 是相对于已发布 `context` 字段的 1-based 行号。仅当可还原时，原始源码文件行号才通过 `source_line` 和 `source_line_end` 提供。
