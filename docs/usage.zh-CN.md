# 使用方法

本文档给出 processed 数据的基本读取方式。

## 读取数据划分

```python
import json
from pathlib import Path

path = Path("data/processed/balanced_stage1_resplit_721/has_vul_721_stratified_v1/train.json")
samples = json.loads(path.read_text(encoding="utf-8"))

print(len(samples))
print(samples[0]["sample_id"])
```

## 漏洞存在性判断

```python
labels = [sample["has_vulnerability"] for sample in samples]
texts = ["\n".join(sample["context"]) for sample in samples]
```

## 漏洞类型分类

```python
def get_types(sample):
    return sorted({v["type"] for v in sample["vulnerabilities"]})

labels = [get_types(sample) for sample in samples]
```

## 漏洞行定位

```python
def get_vulnerable_lines(sample):
    lines = set()
    for vuln in sample["vulnerabilities"]:
        start = vuln.get("line")
        end = vuln.get("line_end") or start
        if start is None:
            continue
        lines.update(range(start, end + 1))
    return sorted(lines)
```

## 评测建议

- `has_vul`：accuracy、precision、recall、F1 和混淆矩阵。
- `vul_type`：多标签 micro/macro precision、recall 和 F1。
- `vul_line`：集合匹配、行级 precision/recall/F1、top-k 命中率等。
