# Upstream License Review

Review date: 2026-05-22

Recommended repository name: `smart-contract-vuln-dataset`

Public release policy: raw upstream data is not redistributed.

## Summary

| Source | Public URL | Observed License / Terms | Decision |
|---|---|---|---|
| SmartBugs Curated | https://github.com/smartbugs/smartbugs-curated | GitHub shows Apache-2.0; README states contracts retain original licenses. | Attribution required; do not redistribute raw contracts. |
| SolidiFI Benchmark | https://github.com/DependableSystemsLab/SolidiFI-benchmark | LICENSE uses MIT and states original contracts retain original licenses. | Attribution and paper citation required; do not redistribute raw contracts. |
| DAppSCAN | https://github.com/InPlusLab/DAppSCAN | No clear repository-wide license observed. | Do not redistribute raw data; permission required for source-containing processed samples. |
| Slither Audited Smart Contracts | https://huggingface.co/datasets/mwritescode/slither-audited-smart-contracts | Hugging Face shows MIT license; Solidity source may retain original licenses. | MIT metadata may be cited; avoid source-code redistribution by default. |
| ScrawlD | https://github.com/sujeetc/ScrawlD | README requests citation; no clear repository-wide license observed. | Do not redistribute raw data; permission required for source-containing processed samples. |
| Smart Contract VulnDB / SCVD | https://www.scvd.dev/ | Website states SOURCE: MIT and DATASET: CC0. | Derived finding metadata can be released with source and access date. |
| Smart Contract Sanctuary | https://github.com/tintinweb/smart-contract-sanctuary | README provides citation; contract files may retain individual source licenses. | Use as source recovery reference; do not redistribute recovered source code by default. |
| Empirical Analysis of Vulnerability Detection Tools for Solidity Smart Contracts | https://github.com/fsalzano/Empirical-Analysis-of-Vulnerability-Detection-Tools-for-Solidity-Smart-Contracts | No clear redistributable license confirmed. | Permission required for source-containing processed samples, or use source pointers. |

## Sources Requiring Attribution

SmartBugs Curated, SolidiFI Benchmark, Slither Audited Smart Contracts, ScrawlD, Smart Contract Sanctuary, and SCVD should be explicitly cited in README, third-party notices, and paper references.

## Sources Requiring Permission or Source-Code Removal

If processed files contain full Solidity source code, obtain permission or remove/rewrite source fields for:

- DAppSCAN,
- ScrawlD,
- Empirical Analysis of Vulnerability Detection Tools for Solidity Smart Contracts,
- Smart Contract Sanctuary recovered source code,
- any SmartBugs Curated, SolidiFI, or Slither sample whose underlying contract license is not confirmed.

Conservative release plan:

1. Do not upload raw data.
2. Do not publish full source code for unclear or mixed-license sources.
3. Publish source pointers, labels, normalized metadata, statistics, schema, mappings, and reconstruction scripts.
4. Request written permission before publishing source-containing samples from unclear-license repositories.

