# Source Catalog

| Source ID | Display Name | URL | Tier | Priority | Supports `has_vul` | Supports `vul_type` | Supports `vul_line` |
|---|---|---|---|---|---:|---:|---:|
| `smartbugs_curated` | SmartBugs Curated | https://github.com/smartbugs/smartbugs-curated | gold | high | yes | yes | yes |
| `solidifi_benchmark` | SolidiFI Benchmark | https://github.com/DependableSystemsLab/SolidiFI-benchmark | silver | high | yes | yes | yes |
| `dappscan` | DAppSCAN | https://github.com/InPlusLab/DAppSCAN | silver | high | yes | yes | no |
| `slither_audited_smart_contracts` | Slither Audited Smart Contracts | https://huggingface.co/datasets/mwritescode/slither-audited-smart-contracts | bronze | high | yes | yes | no |
| `scrawld` | ScrawlD | https://github.com/sujeetc/ScrawlD | silver | high | yes | yes | yes |
| `smart_contract_vulndb` | Smart Contract VulnDB / SCVD | https://www.scvd.dev/ | bronze | high | no | yes | no |
| `smart_contract_sanctuary_ethereum` | Smart Contract Sanctuary | https://github.com/tintinweb/smart-contract-sanctuary | support | support | no | no | no |
| `Empirical-Analysis-of-Vulnerability-Detection-Tools-for-Solidity-Smart-Contracts` | Empirical Analysis of Vulnerability Detection Tools for Solidity Smart Contracts | https://github.com/fsalzano/Empirical-Analysis-of-Vulnerability-Detection-Tools-for-Solidity-Smart-Contracts | gold | original | yes | yes | yes |

Tier meanings:

- `gold`: curated or manually verified benchmark labels.
- `silver`: structured labels or source-backed labels with strong metadata.
- `bronze`: weak labels, tool-derived labels, or candidate sources.
- `support`: source recovery or auxiliary metadata, not a primary label source.
