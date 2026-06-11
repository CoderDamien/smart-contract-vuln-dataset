# Data Processing, Cleaning, and Augmentation

This document describes how the dataset is built from multiple public smart contract vulnerability sources, including source-specific processing, cleaning, label mapping, deduplication, low-frequency augmentation, and task-level dataset construction.

Raw upstream data is not redistributed in this repository.

## Overall Pipeline

1. Register each source with URL, source type, supported tasks, and license status.
2. Read raw data locally without publishing raw files.
3. Convert heterogeneous records into a unified JSON schema.
4. Map source-specific labels into a shared vulnerability taxonomy.
5. Filter invalid labels, invalid line numbers, missing source files, and task-incompatible samples.
6. Deduplicate using raw and normalized source-code hashes.
7. Build task-specific `has_vul`, `vul_type`, and `vul_line` train/validation/test splits.

## Source-Specific Processing

### Empirical-Analysis-of-Vulnerability-Detection-Tools-for-Solidity-Smart-Contracts

Used as the original benchmark source. The original train/validation/test structure is preserved as a reference and used as a deduplication baseline. Line labels are checked for availability and validity before entering line-localization datasets.

### SmartBugs Curated

Curated contracts and vulnerability annotations are imported, mapped from DASP-style labels to the unified taxonomy, hashed for deduplication, and retained as high-confidence benchmark material when license-compatible.

### SolidiFI Benchmark

Solidity files and bug logs are scanned. Bug types and line numbers are parsed from log files, normalized into the unified taxonomy, and filtered for valid code and line labels. Synthetic/injected-source metadata is preserved.

### DAppSCAN

SWC reports are parsed, corresponding Solidity files are recovered, SWC identifiers are mapped into the unified taxonomy, and missing source files or unmappable labels are skipped.

### Slither Audited Smart Contracts

Parquet files are read from the Hugging Face dataset. Slither detector outputs are parsed, mapped to the project taxonomy, and stored as weak-label contract-level samples. `ignore` and `safe` detector outputs are excluded.

### ScrawlD

Vulnerability metadata is imported and matched to Solidity source files when possible. Source-backed and metadata-only samples are distinguished. ScrawlD labels are mapped to the unified taxonomy and used especially for low-frequency labels.

### Smart Contract VulnDB / SCVD

Finding-level records are parsed for vulnerability descriptions, categories, links, and metadata. These records are used for candidate mining and review, not as direct line-level ground truth.

### Smart Contract Sanctuary

Used as an auxiliary source recovery reference. Recovered source code is not redistributed by default.

## Cleaning Rules

The cleaning process removes or marks:

- missing files,
- unreadable source code,
- unmappable labels,
- empty vulnerability records,
- invalid or out-of-range line numbers,
- contradictory clean/vulnerable records,
- weak static-analysis outputs marked as `ignore` or `safe`,
- duplicate or near-duplicate samples.

## Low-Frequency Augmentation

Low-frequency labels such as `front_running` and `denial_service` are expanded through candidate mining, source filtering, review-pack generation, confirmation, and integration into downstream data construction.

## Task-Level Rules

- `has_vul`: keeps clean and vulnerable samples and balances binary classes.
- `vul_type`: keeps only samples with known mapped labels and supports multi-label records.
- `vul_line`: keeps only samples with valid line labels and treats localization as multi-line prediction rather than scalar regression.

For `vul_line`, released line labels use `context_relative_1based` coordinates: `vulnerabilities[].line` and `line_end` are 1-based line numbers relative to the released `context` field. Original source-file coordinates are provided as `source_line` and `source_line_end` only when recoverable. The first manuscript evaluates representative vulnerable start lines; range-aware evaluation using `line_end` is reserved for future versions.
