# Smart Contract Vulnerability Dataset

A large-scale dataset for smart contract vulnerability detection, vulnerability type classification, and vulnerable line localization.

Recommended repository name: `smart-contract-vuln-dataset`.

This repository draft is prepared for publishing processed benchmark data, normalized annotations, construction tools, and documentation used in research on open-source large language models for smart contract vulnerability detection.

Chinese version: [README.zh-CN.md](README.zh-CN.md).

## Highlights

- 105,278 merged samples for binary vulnerability detection.
- 95,573 merged samples for vulnerability type classification.
- 24,178 merged samples with vulnerable-line annotations.
- 8 public upstream sources integrated across curated benchmarks, injected benchmarks, audit-derived labels, weak static-analysis labels, and vulnerability finding databases.
- 19,557 low-frequency candidate samples mined, 3,157 review samples prepared, and 2,666 confirmed low-frequency samples accepted for downstream construction.
- 8 normalized vulnerability categories.
- Task-specific train/validation/test splits for three benchmark tasks.
- Multi-source construction pipeline with normalized staging data, merged data, and processed benchmark splits.
- Reproducible tools for importing, normalizing, deduplicating, merging, splitting, and auditing data.

To the best of our knowledge, this dataset is one of the largest publicly available smart contract vulnerability datasets that integrates vulnerability existence labels, vulnerability type labels, and line-level vulnerability annotations. Before using a stronger claim such as "the largest publicly available smart contract vulnerability dataset", please cite a public comparison table against existing datasets.

## Tasks

The dataset supports three tasks:

| Task ID | Task | Description |
|---|---|---|
| `has_vul` | Vulnerability Detection | Binary classification of vulnerable vs. clean smart contract samples. |
| `vul_type` | Vulnerability Type Classification | Multi-label classification over normalized vulnerability categories. |
| `vul_line` | Vulnerable Line Localization | Multi-line prediction of one or more vulnerable source-code lines. |

## Dataset Statistics

### Merged Dataset

| Dataset | Samples | Main Use |
|---|---:|---|
| `has_vul_merged_stage0` | 105,278 | Binary vulnerability detection |
| `vul_type_merged_stage0` | 95,573 | Vulnerability type classification |
| `vul_line_merged_stage0` | 24,178 | Vulnerable line localization |

### Processed Benchmark Splits

The current recommended processed split is `balanced_stage1_resplit_721`.

| Dataset | Train | Validation | Test | Total |
|---|---:|---:|---:|---:|
| `has_vul_721_stratified_v1` | 17,411 | 4,667 | 2,363 | 24,441 |
| `vul_type_721_stratified_v1` | 18,573 | 3,829 | 1,992 | 24,394 |
| `vul_line_721_stratified_v1` | 10,155 | 1,529 | 807 | 12,491 |

## Vulnerability Categories

The normalized label space contains the following vulnerability categories:

| Label | Description |
|---|---|
| `access_control` | Access-control and authorization-related vulnerabilities. |
| `arithmetic` | Integer overflow, underflow, and arithmetic-related vulnerabilities. |
| `bad_randomness` | Unsafe or predictable randomness. |
| `denial_service` | Denial-of-service vulnerabilities. |
| `front_running` | Transaction-order dependence and front-running-related vulnerabilities. |
| `reentrancy` | Reentrancy vulnerabilities. |
| `time_manipulation` | Timestamp and time-dependency vulnerabilities. |
| `unchecked_low_calls` | Unchecked low-level calls, unchecked send, and unhandled external-call results. |

Some intermediate files may also contain `other` or `unknown` labels for source findings that cannot be reliably mapped into the main taxonomy. The recommended benchmark splits filter or document these labels according to the task protocol.

## Data Sources

The dataset integrates and normalizes samples from multiple public smart contract vulnerability sources:

| Source | Role in Dataset | Task Support |
|---|---|---|
| [SmartBugs Curated](https://github.com/smartbugs/smartbugs-curated) | Curated benchmark source | `has_vul`, `vul_type`, `vul_line` |
| [SolidiFI Benchmark](https://github.com/DependableSystemsLab/SolidiFI-benchmark) | Injected vulnerability benchmark with location metadata | `has_vul`, `vul_type`, `vul_line` |
| [DAppSCAN](https://github.com/InPlusLab/DAppSCAN) | Real-world DApp source and audit-derived labels | `has_vul`, `vul_type` |
| [Slither Audited Smart Contracts](https://huggingface.co/datasets/mwritescode/slither-audited-smart-contracts) | Large weakly labeled dataset derived from Slither detector outputs | `has_vul`, `vul_type` |
| [ScrawlD](https://github.com/sujeetc/ScrawlD) | Source-backed low-frequency vulnerability expansion | `has_vul`, `vul_type`, `vul_line` |
| [Smart Contract VulnDB / SCVD](https://www.scvd.dev/) | Finding-level vulnerability descriptions for candidate mining and review | `vul_type` |
| [Smart Contract Sanctuary](https://github.com/tintinweb/smart-contract-sanctuary) | Source recovery and source-backed sample support | source recovery |
| [Empirical Analysis of Vulnerability Detection Tools for Solidity Smart Contracts](https://github.com/fsalzano/Empirical-Analysis-of-Vulnerability-Detection-Tools-for-Solidity-Smart-Contracts) | Original benchmark source used by the paper before multi-source expansion | `has_vul`, `vul_type`, `vul_line` |

See [docs/data_sources.md](docs/data_sources.md) for source-level notes and license-review reminders.
See [docs/source_usage.md](docs/source_usage.md) for public source links and contribution counts by source.
See [docs/data_processing_and_augmentation.md](docs/data_processing_and_augmentation.md) for processing, cleaning, deduplication, and augmentation details.
See [docs/construction_effort.md](docs/construction_effort.md) for a summary of the dataset construction effort.
See [metadata/upstream_license_review.md](metadata/upstream_license_review.md) and [metadata/authorization_requests.en.md](metadata/authorization_requests.en.md) for license and permission notes.

## Repository Layout

```text
.
|-- README.md
|-- LICENSE
|-- CITATION.cff
|-- data/
|   |-- staging/
|   |-- processed/
|   `-- metadata/
|-- tools/
|-- docs/
|-- examples/
`-- metadata/
```

Publication policy:

- Raw upstream data is not published in this repository.
- `data/staging/`: normalized per-source JSON files before cross-source merge.
- `data/processed/`: task-specific benchmark datasets ready for model training and evaluation.
- `tools/`: reusable scripts for data construction, statistics, and format conversion.
- `docs/`: source documentation, construction protocol, schema, use cases, and limitations.
- `metadata/`: machine-readable statistics, label schema, source catalog, and release checklist.

For upstream sources with unclear redistribution terms, publish source references, retrieval instructions, and derived metadata only. Do not redistribute original raw source-code archives or raw audit reports.

## Data Format

Each normalized sample follows a unified schema:

```json
{
  "sample_id": "source::split::item",
  "source_dataset": "solidifi_benchmark",
  "source_split": "train",
  "source_path": "path/or/original/id",
  "granularity": "contract",
  "contract_name": "Example",
  "function_name": null,
  "context": ["pragma solidity ...", "contract Example { ... }"],
  "has_vulnerability": 1,
  "vulnerabilities": [
    {
      "type": "reentrancy",
      "line": 42,
      "line_end": 42,
      "source_taxonomy": "source taxonomy name",
      "source_label": "original source label",
      "evidence": [],
      "metadata": {}
    }
  ],
  "label_confidence": "silver",
  "label_origin": "source_annotation",
  "dedup_hash_raw": "...",
  "dedup_hash_normalized": "...",
  "metadata": {}
}
```

See [docs/schema.md](docs/schema.md) for the full field description.

## Quick Start

```python
import json
from pathlib import Path

path = Path("data/processed/has_vul_721_stratified_v1/train.json")
samples = json.loads(path.read_text(encoding="utf-8"))

print("Samples:", len(samples))
print("Fields:", samples[0].keys())
print("Label:", samples[0]["has_vulnerability"])
```

More examples are provided in [docs/usage.md](docs/usage.md) and [examples/load_dataset.py](examples/load_dataset.py).

## Construction Pipeline

The dataset is built through the following pipeline:

1. Collect raw public datasets and source-code corpora.
2. Normalize each source into a unified sample schema.
3. Map source-specific vulnerability labels into a shared taxonomy.
4. Deduplicate samples using raw and normalized source-code hashes.
5. Merge sources by task.
6. Build task-specific train/validation/test splits.
7. Audit label coverage, line-label validity, duplicate IDs, and source distribution.

See [docs/dataset_construction.md](docs/dataset_construction.md).

## Citation

If you use this dataset, please cite the dataset repository and the related paper:

```bibtex
@dataset{xu_smart_contract_vulnerability_dataset_2026,
  title  = {A Large-Scale Smart Contract Vulnerability Dataset},
  author = {Xu, Daming},
  year   = {2026},
  publisher = {GitHub},
  url    = {https://github.com/<your-github-username>/smart-contract-vuln-dataset}
}
```

Please also cite the original upstream datasets where applicable. See [docs/data_sources.md](docs/data_sources.md).

## License

Suggested license policy for the public repository:

- Repository code and documentation: MIT.
- Self-created dataset metadata, statistics, and annotation schema: CC BY 4.0.
- Raw upstream data: not redistributed.
- Processed samples that contain upstream source code should be released only when the corresponding upstream license permits redistribution, or replaced by source pointers and reconstruction scripts.

Preserve upstream citations, notices, and license files. See [metadata/upstream_license_review.md](metadata/upstream_license_review.md).

## Limitations

This dataset integrates heterogeneous sources with different label origins, granularities, and confidence levels. Labels may include source-specific noise, synthetic vulnerabilities, weak labels, and manually reviewed subsets. See [docs/limitations.md](docs/limitations.md) before using the dataset for benchmark claims.
