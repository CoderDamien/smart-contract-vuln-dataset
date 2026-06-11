# Release Checklist

Use this checklist before publishing the dataset repository.

## Required Before Public Release

- [x] Choose final repository name: `smart-contract-vuln-dataset`.
- [x] Choose final GitHub owner and URL: `https://github.com/CoderDamien/smart-contract-vuln-dataset`.
- [x] Confirm raw upstream publication policy: raw data will not be published.
- [x] Complete first-pass license review for each upstream source.
- [x] Add source URLs, citations, licenses, and access dates.
- [x] Decide recommended license for repository code and documentation: MIT.
- [x] Decide recommended license for self-created metadata and annotations: CC BY 4.0, subject to upstream compatibility.
- [x] Add `LICENSE`.
- [x] Update `CITATION.cff` with final title, author metadata, repository URL, and release version. Paper DOI is not available yet.
- [x] Generate final `metadata/dataset_statistics.json` from the released files.
- [x] Verify that no private server paths, tokens, local usernames, or unpublished paper notes are included in release-facing metadata and replication indexes.
- [ ] Verify that processed train/validation/test splits do not leak duplicates across splits.
- [ ] Verify that all line labels are in range.
- [x] Verify that README statistics match released files.
- [ ] Tag the current release version on GitHub after committing the release-preparation changes.

## Recommended Before Public Release

- [ ] Add a comparison table against existing smart contract vulnerability datasets.
- [ ] Add a small example subset if the full data is large.
- [ ] Add a script that validates schema consistency.
- [ ] Add a script that prints dataset statistics.
- [ ] Add a model-agnostic baseline evaluation example.
- [ ] Archive the current release on Zenodo to obtain a DOI, then update `CITATION.cff`, `README.md`, and `metadata/release_metadata.json`.
