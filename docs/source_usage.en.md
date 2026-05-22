# Source Usage and Contribution Counts

This document lists the upstream public datasets, URLs, local file-count references, and source-level sample contributions in the current release draft.

Raw upstream data is not redistributed. Raw file counts are only local audit references.

## Upstream Sources

| Source ID | Public Source | URL | Role |
|---|---|---|---|
| `Empirical-Analysis-of-Vulnerability-Detection-Tools-for-Solidity-Smart-Contracts` | Empirical Analysis of Vulnerability Detection Tools for Solidity Smart Contracts | https://github.com/fsalzano/Empirical-Analysis-of-Vulnerability-Detection-Tools-for-Solidity-Smart-Contracts | Core source of the original paper dataset. |
| `smartbugs_curated` | SmartBugs Curated | https://github.com/smartbugs/smartbugs-curated | Curated benchmark source. |
| `solidifi_benchmark` | SolidiFI Benchmark | https://github.com/DependableSystemsLab/SolidiFI-benchmark | Injected-vulnerability benchmark with type and line metadata. |
| `dappscan` | DAppSCAN | https://github.com/InPlusLab/DAppSCAN | Real-world DApp audit/source reference. |
| `slither_audited_smart_contracts` | Slither Audited Smart Contracts | https://huggingface.co/datasets/mwritescode/slither-audited-smart-contracts | Large weak-label source derived from Slither outputs. |
| `scrawld` | ScrawlD | https://github.com/sujeetc/ScrawlD | Low-frequency class expansion source. |
| `smart_contract_vulndb` | Smart Contract VulnDB / SCVD | https://www.scvd.dev/ | Finding-level vulnerability metadata. |
| `smart_contract_sanctuary_ethereum` | Smart Contract Sanctuary | https://github.com/tintinweb/smart-contract-sanctuary | Source recovery reference. |

## Local Raw File Counts

| Source ID | Local Raw Files Observed | Public Release Policy |
|---|---:|---|
| `dappscan` | 30,672 | Not redistributed. |
| `scrawld` | 1,960 | Not redistributed. |
| `slither_audited_smart_contracts` | 12 | Not redistributed as raw data. |
| `smart_contract_vulndb` | 3 | Raw snapshots are not redistributed; derived metadata may be released. |
| `smartbugs_curated` | 159 | Raw contracts are not redistributed. |
| `solidifi_benchmark` | 5,108 | Raw contracts are not redistributed. |

## Normalized Staging File Counts

| Source ID | Normalized Staging Files |
|---|---:|
| `dappscan` | 5 |
| `scrawld` | 2 |
| `slither_audited_smart_contracts` | 5 |
| `smart_contract_vulndb` | 2 |
| `smartbugs_curated` | 8 |
| `solidifi_benchmark` | 8 |

## Merged Dataset Contributions

| Source ID | `has_vul_merged_stage0` | `vul_type_merged_stage0` | `vul_line_merged_stage0` |
|---|---:|---:|---:|
| `solidifi_benchmark` | 24,178 | 24,178 | 24,178 |
| `dappscan` | 455 | 455 | 0 |
| `slither_audited_smart_contracts` | 80,645 | 70,940 | 0 |
| Total | 105,278 | 95,573 | 24,178 |

## Recommended Processed Split Contributions

| Source ID | `has_vul_721_stratified_v1` | `vul_type_721_stratified_v1` | `vul_line_721_stratified_v1` |
|---|---:|---:|---:|
| `dappscan` | 453 | 455 | 464 |
| `Empirical-Analysis-of-Vulnerability-Detection-Tools-for-Solidity-Smart-Contracts` | 2,182 | 1,609 | 1,519 |
| `scrawld` | 1,951 | 1,909 | 1,952 |
| `slither_audited_smart_contracts` | 18,714 | 15,217 | 2,815 |
| `solidifi_benchmark` | 1,141 | 5,204 | 5,741 |
| Total | 24,441 | 24,394 | 12,491 |

