# Usage

This document gives basic examples for loading and using the processed dataset.

## Load a Split

```python
import json
from pathlib import Path

path = Path("data/processed/balanced_stage1_resplit_721/has_vul_721_stratified_v1/train.json")
samples = json.loads(path.read_text(encoding="utf-8"))

print(len(samples))
print(samples[0]["sample_id"])
```

## Binary Vulnerability Detection

```python
labels = [sample["has_vulnerability"] for sample in samples]
texts = ["\n".join(sample["context"]) for sample in samples]
```

## Vulnerability Type Classification

```python
def get_types(sample):
    return sorted({v["type"] for v in sample["vulnerabilities"]})

labels = [get_types(sample) for sample in samples]
```

## Vulnerable Line Localization

```python
def get_vulnerable_lines(sample):
    lines = set()
    for vuln in sample["vulnerabilities"]:
        start = vuln.get("line")
        end = vuln.get("line_end") or start
        if start is None:
            continue
        for line in range(start, end + 1):
            lines.add(line)
    return sorted(lines)

line_labels = [get_vulnerable_lines(sample) for sample in samples]
```

## Recommended Evaluation Notes

- For `has_vul`, use accuracy, precision, recall, F1, and confusion matrix.
- For `vul_type`, use micro/macro precision, recall, and F1 for multi-label classification.
- For `vul_line`, use set-based or line-level metrics. Do not evaluate it as a single floating-point regression task.

## Reproducibility Notes

When reporting results, record:

- Dataset release version.
- Task name.
- Split name.
- Model name and version.
- Prompt template or fine-tuning configuration.
- Evaluation script version.
- Random seed.
