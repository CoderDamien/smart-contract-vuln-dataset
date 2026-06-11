# Dataset Card: Smart Contract Vulnerability Dataset for Solidity and Ethereum Security

## Dataset Summary

This dataset supports smart contract vulnerability detection, vulnerability type classification, and vulnerable line localization for Solidity and Ethereum smart contracts. It is designed for blockchain security research, Web3 security analysis, static-analysis comparison, and LLM-based code security evaluation.

Current release version: `v1.0.3`.
Line-coordinate schema revision: `v1.0.3`.
This release includes the manuscript-aligned replication package and the vulnerable-line coordinate schema revision.

## Search Keywords

smart contract vulnerability dataset, Solidity security dataset, Ethereum smart contract vulnerability detection, reentrancy dataset, smart contract bug localization, vulnerable line localization, vulnerability type classification, blockchain security dataset, Web3 security dataset, LLM code security benchmark.

## Tasks

- Binary vulnerability detection: `has_vul`
- Multi-label vulnerability type classification: `vul_type`
- Multi-line vulnerable line localization: `vul_line`

For `vul_line`, line labels are 1-based line numbers relative to the released `context` field unless `source_line` is explicitly provided. In `v1.0.3`, processed vulnerable-line annotations include `source_line`/`source_line_end` plus `source_mapping_method` when source coordinates can be reconstructed from raw source metadata or full-context identity mapping.

## Labels

- `access_control`
- `arithmetic`
- `bad_randomness`
- `denial_service`
- `front_running`
- `reentrancy`
- `time_manipulation`
- `unchecked_low_calls`

## Dataset Size

| Split / Stage | `has_vul` | `vul_type` | `vul_line` |
|---|---:|---:|---:|
| Merged dataset | 105,278 | 95,573 | 24,178 |
| Recommended processed split | 24,441 | 24,394 | 12,491 |

## Source Coverage

The dataset integrates eight public upstream sources, including curated benchmarks, injected-vulnerability benchmarks, audit-derived labels, weak static-analysis labels, vulnerability finding databases, and source recovery references.

## Paper Replication Package

The repository includes a manuscript-aligned replication package for the IST submission version dated 2026-06-03. The package covers 226 model-task-mode evaluation units, 25 models, 8 model families, and four use modes: direct inference, structured prompting, full fine-tuning, and QLoRA.

Key replication files:

- Formal experiment matrix and metrics: `replication/results/paper_experiment_matrix_closure.csv`, `replication/results/paper_experiment_metrics_all.csv`
- Task-level metrics: `replication/results/has_vul_metrics.csv`, `replication/results/vul_type_metrics.csv`, `replication/results/vul_line_metrics.csv`
- Prompt ablation: `replication/results/prompt_ablation.csv`, with the manuscript-scope 16-row supplement in `supplementary/tables/Table_S9.csv`
- Dataset expansion analysis: `replication/results/data_completion_pairs.csv`, `supplementary/tables/Table_S10.csv`
- Current manuscript figures: `replication/figures/figures_q1_redesign/`
- Supplementary tables: `supplementary/supplementary_tables.xlsx`, `supplementary/tables/Table_S1.csv` to `Table_S14.csv`

Headline result anchors reported by the manuscript include:

| Task / Analysis | Manuscript Anchor |
|---|---|
| Vulnerability presence detection | Best F1 = 0.8757 with Qwen2.5-Coder-1.5B full fine-tuning |
| Vulnerability type identification | Best standard F1 = 0.6265; best macro-F1 = 0.4755; best multi-label F1 = 0.4300 |
| Vulnerable line localization | Best strict-F1 = 0.2955; best contract-hit = 0.8451 |
| Prompt ablation | 16 comparisons for Qwen2.5-Coder-7B and 32B over `vul_type` and `vul_line` |
| Dataset expansion | 6 same-model, same-task, same-method before/after pairs |

## Intended Uses

- Smart contract vulnerability detection research.
- Solidity and Ethereum security benchmarking.
- LLM-based code security evaluation.
- Vulnerability type classification.
- Vulnerable line localization.
- Dataset construction and data governance studies for blockchain security.

## Out-of-Scope Uses

- Direct commercial redistribution of upstream raw source code without checking upstream licenses.
- Treating weak static-analysis labels as manually verified ground truth.
- Evaluating vulnerable line localization as single-value regression.

## License and Redistribution

Raw upstream data is not redistributed. See [metadata/upstream_license_review.md](metadata/upstream_license_review.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Citation

```bibtex
@dataset{xu_smart_contract_vulnerability_dataset_2026,
  title  = {Smart Contract Vulnerability Dataset for Solidity and Ethereum Security},
  author = {Xu, Daming},
  year   = {2026},
  version = {v1.0.3},
  publisher = {GitHub},
  url    = {https://github.com/CoderDamien/smart-contract-vuln-dataset}
}
```
