# Limitations

This dataset integrates heterogeneous public sources. Users should consider the following limitations when interpreting benchmark results.

## Heterogeneous Label Origins

The dataset combines curated labels, injected benchmark labels, audit-derived labels, tool-derived labels, and reviewed candidate labels. These labels do not all have the same confidence level.

## Synthetic and Real-World Samples

Some samples come from injected vulnerability benchmarks, while others come from real-world contracts or audit datasets. Synthetic vulnerabilities are useful for controlled evaluation, but they may not fully represent real-world vulnerability patterns.

## Weak Labels

Large sources derived from static-analysis tool outputs may include false positives or tool-specific biases. Such samples should be interpreted as weak labels unless manually verified.

## Line-Level Annotation Coverage

Line-level annotations are not available for all sources. The `vul_line` task therefore uses a smaller subset than detection and type classification.

## Multi-Label and Multi-Line Complexity

A smart contract may contain multiple vulnerability types and multiple vulnerable lines. Evaluation should preserve this structure. Reducing the task to a single class or a single line can distort performance.

## Source Overlap

Different public datasets may share contracts, examples, or derived variants. Deduplication hashes are used to reduce leakage, but users should still report the dataset version and splitting protocol.

## License Constraints

Raw upstream datasets may have different redistribution permissions. Public releases should preserve all upstream notices and should avoid redistributing raw data when permission is unclear.

