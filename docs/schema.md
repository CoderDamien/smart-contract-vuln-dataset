# Dataset Schema

This document describes the unified sample schema used by the dataset.

## Sample Object

| Field | Type | Required | Description |
|---|---|---:|---|
| `sample_id` | string | yes | Stable sample identifier. |
| `source_dataset` | string | yes | Source dataset ID, such as `solidifi_benchmark` or `slither_audited_smart_contracts`. |
| `source_split` | string | yes | Original or constructed split name. |
| `source_path` | string or null | no | Original source path, URL, or source-specific item ID. |
| `granularity` | string | yes | One of `contract`, `file`, `function`, `finding`, or `project`. |
| `contract_name` | string or null | no | Contract name when available. |
| `function_name` | string or null | no | Function name when available. |
| `context` | list[string] | yes | Source-code lines or text context used as model input. |
| `has_vulnerability` | integer | yes | `1` for vulnerable samples, `0` for clean samples. |
| `vulnerabilities` | list[object] | yes | List of vulnerability annotations. Clean samples should have an empty list. |
| `label_confidence` | string | yes | One of `gold`, `silver`, `bronze`, or `unknown`. |
| `label_origin` | string | yes | Origin of the label, such as curated annotation, tool output, injected benchmark, or manual review. |
| `dedup_hash_raw` | string or null | no | SHA-256 hash of raw source context. |
| `dedup_hash_normalized` | string or null | no | SHA-256 hash of normalized source context. |
| `metadata` | object | yes | Additional source-specific metadata. |

## Vulnerability Object

| Field | Type | Required | Description |
|---|---|---:|---|
| `type` | string | yes | Normalized vulnerability type. |
| `line` | integer or null | no | Start line of the vulnerability annotation, if available. |
| `line_end` | integer or null | no | End line of the annotation, if available. |
| `source_taxonomy` | string or null | no | Original source taxonomy, such as DASP, SWC, SolidiFI bug type, or Slither detector. |
| `source_label` | string or null | no | Original source label before normalization. |
| `evidence` | list[string] | yes | Optional evidence snippets or notes. |
| `metadata` | object | yes | Additional annotation-level metadata. |

## Label Confidence

| Value | Meaning |
|---|---|
| `gold` | Curated or manually verified annotation. |
| `silver` | Structured benchmark or source-backed annotation with strong metadata. |
| `bronze` | Weak label, tool-derived label, or candidate label. |
| `unknown` | Confidence not determined. |

## Granularity

| Value | Meaning |
|---|---|
| `contract` | The sample is a contract-level source-code unit. |
| `file` | The sample is a source file. |
| `function` | The sample is a function-level unit. |
| `finding` | The sample is a finding record or vulnerability description. |
| `project` | The sample is a project-level unit. |

## Example

```json
{
  "sample_id": "solidifi_benchmark::train::example",
  "source_dataset": "solidifi_benchmark",
  "source_split": "train",
  "source_path": "buggy_contracts/example.sol",
  "granularity": "contract",
  "contract_name": "Example",
  "function_name": null,
  "context": [
    "pragma solidity ^0.4.24;",
    "contract Example {",
    "  function withdraw() public { ... }",
    "}"
  ],
  "has_vulnerability": 1,
  "vulnerabilities": [
    {
      "type": "reentrancy",
      "line": 3,
      "line_end": 3,
      "source_taxonomy": "SolidiFI",
      "source_label": "Re-entrancy",
      "evidence": [],
      "metadata": {}
    }
  ],
  "label_confidence": "silver",
  "label_origin": "injected_benchmark",
  "dedup_hash_raw": "TODO",
  "dedup_hash_normalized": "TODO",
  "metadata": {}
}
```

