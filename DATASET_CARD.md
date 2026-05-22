# Dataset Card: Smart Contract Vulnerability Dataset for Solidity and Ethereum Security

## Dataset Summary

This dataset supports smart contract vulnerability detection, vulnerability type classification, and vulnerable line localization for Solidity and Ethereum smart contracts. It is designed for blockchain security research, Web3 security analysis, static-analysis comparison, and LLM-based code security evaluation.

## Search Keywords

smart contract vulnerability dataset, Solidity security dataset, Ethereum smart contract vulnerability detection, reentrancy dataset, smart contract bug localization, vulnerable line localization, vulnerability type classification, blockchain security dataset, Web3 security dataset, LLM code security benchmark.

## Tasks

- Binary vulnerability detection: `has_vul`
- Multi-label vulnerability type classification: `vul_type`
- Multi-line vulnerable line localization: `vul_line`

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
  publisher = {GitHub},
  url    = {https://github.com/CoderDamien/smart-contract-vuln-dataset}
}
```

