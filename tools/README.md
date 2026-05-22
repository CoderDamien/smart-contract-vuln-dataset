# Tools

This directory is reserved for public release scripts.

Recommended tools to include:

- `import_datasets.py`: import raw upstream datasets into the unified schema.
- `dedup_external_datasets.py`: compute raw and normalized hashes and remove duplicates.
- `merge_external_datasets.py`: merge normalized sources into task-specific datasets.
- `build_balanced_task_datasets.py`: build processed train/validation/test splits.
- `validate_schema.py`: validate released JSON files against the unified schema.
- `summarize_dataset.py`: generate dataset statistics used by README and metadata.

For public release, prefer small, self-contained scripts with stable command-line arguments and no private local paths.

