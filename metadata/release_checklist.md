# Release Checklist

Use this checklist before publishing the dataset repository.

## Required Before Public Release

- [x] Choose final repository name: `smart-contract-vuln-dataset`.
- [ ] Choose final GitHub owner and URL.
- [x] Confirm raw upstream publication policy: raw data will not be published.
- [x] Complete first-pass license review for each upstream source.
- [ ] Add source URLs, citations, licenses, and access dates.
- [x] Decide recommended license for repository code and documentation: MIT.
- [x] Decide recommended license for self-created metadata and annotations: CC BY 4.0, subject to upstream compatibility.
- [ ] Add `LICENSE`.
- [ ] Update `CITATION.cff` with final title, author metadata, repository URL, and paper DOI if available.
- [ ] Generate final `metadata/dataset_statistics.json` from the released files.
- [ ] Verify that no private server paths, tokens, local usernames, or unpublished paper notes are included.
- [ ] Verify that processed train/validation/test splits do not leak duplicates across splits.
- [ ] Verify that all line labels are in range.
- [ ] Verify that README statistics match released files.
- [ ] Tag release version, for example `v1.0.0`.

## Recommended Before Public Release

- [ ] Add a comparison table against existing smart contract vulnerability datasets.
- [ ] Add a small example subset if the full data is large.
- [ ] Add a script that validates schema consistency.
- [ ] Add a script that prints dataset statistics.
- [ ] Add a model-agnostic baseline evaluation example.
- [ ] Archive a release on Zenodo to obtain a DOI.
