# Data Sources

This document records the public sources integrated into the dataset and the role each source plays in the construction pipeline.

The public release policy is to exclude raw upstream data. If redistribution permission is unclear, publish only source URLs, download instructions, normalized metadata allowed by the license, and scripts that reproduce the transformation locally.

For file counts and sample contribution counts by source, see [source_usage.md](source_usage.md).
For processing, cleaning, deduplication, and augmentation details, see [data_processing_and_augmentation.md](data_processing_and_augmentation.md).

## License Review Summary

| Source | URL | License / Redistribution Notes | Public Release Decision |
|---|---|---|---|
| SmartBugs Curated | https://github.com/smartbugs/smartbugs-curated | Repository metadata lists Apache-2.0; README says contracts retain their original licenses. | Do not publish raw contracts. Publish references, normalized labels, and scripts; include upstream notice. |
| SolidiFI Benchmark | https://github.com/DependableSystemsLab/SolidiFI-benchmark | Repository has MIT license for software/materials; license text says original contracts retain original licenses. | Do not publish raw contracts. Publish derived metadata and scripts; include upstream notice. |
| DAppSCAN | https://github.com/InPlusLab/DAppSCAN | Public README available, but no clear repository-wide license observed during review. | Do not publish raw data. Publish references and reconstruction instructions only. |
| Slither Audited Smart Contracts | https://huggingface.co/datasets/mwritescode/slither-audited-smart-contracts | Hugging Face metadata lists MIT license. Solidity source code may still retain original source licenses. | Publish metadata and derived labels; avoid redistributing raw source code unless license-compatible. |
| ScrawlD | https://github.com/sujeetc/ScrawlD | README requests citation; no clear repository-wide license observed during review. | Do not publish raw data. Publish references, derived statistics, and scripts only. |
| Smart Contract VulnDB / SCVD | https://www.scvd.dev/ | Website states source is MIT and dataset is CC0 public domain. | Can publish derived finding metadata with attribution; keep snapshot date. |
| Smart Contract Sanctuary Ethereum | https://github.com/tintinweb/smart-contract-sanctuary | README provides citation; repository includes verified contracts that may have their own licenses. | Use as source recovery reference; do not publish raw recovered source code by default. |

## Source Summary

| Source ID | Display Name | Tier | Used For | Notes |
|---|---|---|---|---|
| `smartbugs_curated` | SmartBugs Curated | gold | Detection, type classification, line localization | Curated community benchmark with vulnerability labels. |
| `solidifi_benchmark` | SolidiFI Benchmark | silver | Detection, type classification, line localization | Synthetic injected vulnerabilities with bug logs that support location mapping. |
| `dappscan` | DAppSCAN | silver | Detection, type classification | Real-world DApp source data and audit-derived labels. |
| `slither_audited_smart_contracts` | Slither Audited Smart Contracts | bronze | Detection, type classification | Large weakly labeled dataset derived from Slither detector outputs. |
| `scrawld` | ScrawlD | silver | Low-frequency label expansion and line/source-backed samples | Used especially for denial-of-service and front-running expansion. |
| `smart_contract_vulndb` | Smart Contract VulnDB | bronze | Finding-level candidate mining and review | Used for realistic finding text and low-frequency candidate discovery. |
| `smart_contract_sanctuary_ethereum` | Smart Contract Sanctuary Ethereum | support source | Source-code recovery | Used to recover source-backed samples where needed. |
| `Empirical-Analysis-of-Vulnerability-Detection-Tools-for-Solidity-Smart-Contracts` | Empirical Analysis of Vulnerability Detection Tools for Solidity Smart Contracts | gold | Original benchmark source | Used by the original paper dataset before multi-source expansion. |

## Source Roles

### SmartBugs Curated

SmartBugs Curated is treated as a high-confidence curated benchmark source. It is useful for vulnerability existence labels, vulnerability type labels, and line-level annotations when available.

Release checklist:

- Confirm upstream repository URL.
- Preserve Apache-2.0 repository notice and original-license warning for contracts.
- Preserve original citation and license notice.
- Do not redistribute raw contracts in this release.

### SolidiFI Benchmark

SolidiFI provides injected vulnerabilities and metadata that can support type and line-level labels. Because injected vulnerabilities differ from real-world vulnerabilities, downstream experiments should preserve the synthetic-source flag or source metadata.

Release checklist:

- Confirm upstream repository URL.
- Preserve MIT notice and original-license warning for source contracts.
- Preserve original citation and license notice.
- Explicitly mark synthetic/injected samples in metadata.
- Do not redistribute raw contracts in this release.

### DAppSCAN

DAppSCAN contributes real-world DApp source files and audit-derived labels. The current normalized data is suitable for file-level vulnerability detection and type classification.

Release checklist:

- Confirm upstream repository URL and submodule status.
- No clear repository-wide license was observed during review.
- Preserve links between audit reports and source files when possible.
- Do not redistribute raw DAppSCAN files in this release.

### Slither Audited Smart Contracts

This source provides a large set of weak labels derived from Slither detector results. It is useful for scaling the training corpus but should be distinguished from manually verified ground truth.

Release checklist:

- Confirm Hugging Face dataset URL.
- Preserve MIT dataset metadata notice.
- Record detector-to-taxonomy mapping.
- Mark source labels as weak or bronze confidence.
- Avoid redistributing raw Solidity source code unless license-compatible.

### ScrawlD

ScrawlD is used for source-backed expansion of low-frequency labels such as `denial_service` and `front_running`. The release should document how source code was recovered and how labels were mapped.

Release checklist:

- Confirm upstream source URL.
- No clear repository-wide license was observed during review.
- Record label mapping from ScrawlD labels to the project taxonomy.
- Record source recovery status.
- Do not redistribute raw ScrawlD files in this release.

### Smart Contract VulnDB

Smart Contract VulnDB is used as a finding-level source for candidate mining and review, especially for low-frequency vulnerability classes. It should not be presented as direct line-level ground truth unless a finding has been source-backed and reviewed.

Release checklist:

- Confirm upstream source URL.
- Preserve SCVD license notice: source MIT, dataset CC0.
- Separate finding text from source-code benchmark samples.
- Record access date and snapshot identifier.

### Smart Contract Sanctuary Ethereum

Smart Contract Sanctuary Ethereum is used as a support source for source-code recovery. It should be documented as a support corpus rather than a primary label source unless labels are independently assigned.

Release checklist:

- Confirm source URL.
- Treat recovered contracts as retaining their own source licenses.
- Document which samples were recovered from this source.
- Do not redistribute raw recovered source code by default.

## Citation Policy

Users of this dataset should cite:

- This dataset repository.
- The accompanying paper, once available.
- Each upstream dataset used in their experiment subset.

The final release should include a source citation table with URLs, papers, licenses, and access dates.
