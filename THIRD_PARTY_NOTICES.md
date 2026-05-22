# Third-Party Notices

This repository integrates metadata, labels, and processing logic derived from multiple public smart contract vulnerability sources. Raw upstream datasets are not redistributed in this repository.

Review date: 2026-05-22

## SmartBugs Curated

- URL: https://github.com/smartbugs/smartbugs-curated
- License note: GitHub shows Apache-2.0; the upstream README states that contracts retain their original licenses.
- Release decision: raw contracts are not redistributed. References, derived labels, statistics, and reconstruction scripts may be published.

## SolidiFI Benchmark

- URL: https://github.com/DependableSystemsLab/SolidiFI-benchmark
- License note: upstream LICENSE uses MIT terms and states that original contracts retain their original licenses.
- Release decision: raw contracts are not redistributed. MIT notice and paper citation should be preserved.

## DAppSCAN

- URL: https://github.com/InPlusLab/DAppSCAN
- License note: no clear repository-wide license was observed.
- Release decision: raw files are not redistributed. Permission is required before publishing source-containing processed samples.

## Slither Audited Smart Contracts

- URL: https://huggingface.co/datasets/mwritescode/slither-audited-smart-contracts
- License note: Hugging Face shows MIT. Third-party Solidity source code may retain original licenses.
- Release decision: detector-derived metadata and scripts may be published; raw source code is avoided by default.

## ScrawlD

- URL: https://github.com/sujeetc/ScrawlD
- License note: the upstream README requests citation; no clear repository-wide license was observed.
- Release decision: raw files are not redistributed. Permission is required before publishing source-containing processed samples.

## Smart Contract VulnDB / SCVD

- URL: https://www.scvd.dev/
- License note: the website states `SOURCE: MIT` and `DATASET: CC0 (PUBLIC DOMAIN)`.
- Release decision: derived finding metadata may be published with attribution and access date.

## Smart Contract Sanctuary

- URL: https://github.com/tintinweb/smart-contract-sanctuary
- License note: the upstream README provides citation instructions. Verified contracts may retain their own licenses.
- Release decision: use as a source recovery reference; do not redistribute recovered source code by default.

## Empirical Analysis of Vulnerability Detection Tools for Solidity Smart Contracts

- URL: https://github.com/fsalzano/Empirical-Analysis-of-Vulnerability-Detection-Tools-for-Solidity-Smart-Contracts
- License note: no clear redistributable license has been confirmed.
- Release decision: use the upstream repository name in public documentation. Permission is required before publishing source-containing processed samples, unless source fields are replaced with pointers.

