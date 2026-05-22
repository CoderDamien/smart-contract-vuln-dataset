# 数据文件

该目录包含可公开下载的 processed 数据压缩包。

## 推荐 processed 数据包

| 文件 | 大小 | 内容 |
|---|---:|---|
| `processed/balanced_stage1_resplit_721.tar.gz` | 213 MB | `has_vul`、`vul_type`、`vul_line` 三类任务的推荐训练集、验证集和测试集。 |

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
```

## 说明

- 本仓库不再分发原始 raw 数据。
- merged 阶段的大型中间 JSON 暂未上传，因为多个文件单文件超过 3GB。
- 来源与许可证说明见 `metadata/upstream_license_review.zh-CN.md`。

