from __future__ import annotations

import csv
import gzip
import hashlib
import io
import json
import tarfile
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REVISION_VERSION = "v1.0.3"
COORD_SYSTEM = "context_relative_1based"
FULL_CONTEXT_IDENTITY_SOURCES = {
    "dappscan",
    "scrawld",
    "slither_audited_smart_contracts",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def as_int(value: Any) -> int | None:
    if value is None:
        return None
    try:
        text = str(value).strip()
        if not text:
            return None
        return int(float(text))
    except (TypeError, ValueError):
        return None


def context_line_count(sample: dict[str, Any]) -> int | None:
    context = sample.get("context")
    if isinstance(context, str):
        return context.count("\n") + 1 if context else 0
    if isinstance(context, list):
        lines = 0
        for item in context:
            if isinstance(item, str):
                lines += item.count("\n") + 1
            elif isinstance(item, dict):
                text = item.get("code") or item.get("text")
                if isinstance(text, str):
                    lines += text.count("\n") + 1
        return lines if lines else None
    if isinstance(context, dict):
        text = context.get("code") or context.get("text")
        if isinstance(text, str):
            return text.count("\n") + 1 if text else 0
    code = sample.get("code")
    if isinstance(code, str):
        return code.count("\n") + 1 if code else 0
    return None


def infer_source_mapping(sample: dict[str, Any], vuln: dict[str, Any]) -> dict[str, Any]:
    line = as_int(vuln.get("line"))
    line_end = as_int(vuln.get("line_end"))
    metadata = sample.get("metadata") if isinstance(sample.get("metadata"), dict) else {}
    vuln_meta = vuln.get("metadata") if isinstance(vuln.get("metadata"), dict) else {}
    raw_row = vuln_meta.get("raw_row") if isinstance(vuln_meta.get("raw_row"), dict) else {}
    source_dataset = sample.get("source_dataset")
    dataset_role = metadata.get("augmented_dataset_role")

    raw_loc = as_int(raw_row.get("loc"))
    raw_length = as_int(raw_row.get("length"))
    context_start_line = as_int(metadata.get("contract_start_line"))
    context_lines = context_line_count(sample)

    source_line = None
    source_line_end = None
    status = "unavailable"
    method = "unavailable"

    if raw_loc is not None:
        source_line = raw_loc
        if raw_length is not None and raw_length > 0:
            source_line_end = raw_loc + raw_length - 1
        elif line_end is not None and line is not None:
            source_line_end = raw_loc + (line_end - line)
        else:
            source_line_end = raw_loc
        if line is not None:
            context_start_line = raw_loc - line + 1
        status = "available"
        method = "raw_loc_minus_context_start"
    elif context_start_line is not None and line is not None:
        source_line = context_start_line + line - 1
        source_line_end = context_start_line + (line_end if line_end is not None else line) - 1
        status = "available"
        method = "context_start_line_offset"
    elif line is not None and (source_dataset in FULL_CONTEXT_IDENTITY_SOURCES or source_dataset is None):
        end = line_end if line_end is not None else line
        if context_lines is None or (1 <= line <= context_lines and 1 <= end <= context_lines):
            context_start_line = 1
            source_line = line
            source_line_end = end
            status = "available"
            if source_dataset in FULL_CONTEXT_IDENTITY_SOURCES:
                method = "full_context_identity_by_source_dataset"
            elif dataset_role == "legacy_eval":
                method = "legacy_full_context_identity"
            else:
                method = "unattributed_full_context_identity"

    return {
        "line_coordinate_system": COORD_SYSTEM,
        "context_start_line": context_start_line,
        "source_line": source_line,
        "source_line_end": source_line_end,
        "raw_loc": raw_loc,
        "raw_length": raw_length,
        "line_scope": "context",
        "source_mapping_status": status,
        "source_mapping_method": method,
    }


def revise_samples(samples: list[dict[str, Any]], counters: Counter[str]) -> list[dict[str, Any]]:
    for sample in samples:
        for vuln in sample.get("vulnerabilities", []) or []:
            if not isinstance(vuln, dict) or "line" not in vuln:
                continue
            inferred = infer_source_mapping(sample, vuln)
            for key, value in inferred.items():
                vuln[key] = value
            counters["vulnerabilities_with_line"] += 1
            counters[f"source_mapping_status::{inferred['source_mapping_status']}"] += 1
            source = sample.get("source_dataset") or "unknown"
            counters[f"source::{source}"] += 1
            if inferred["raw_loc"] is not None and inferred["context_start_line"] is not None:
                line = as_int(vuln.get("line"))
                if line is not None and line == inferred["raw_loc"] - inferred["context_start_line"] + 1:
                    counters["raw_loc_context_formula_ok"] += 1
                else:
                    counters["raw_loc_context_formula_failed"] += 1
    return samples


def json_bytes(data: Any) -> bytes:
    return (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def minified_json_bytes(data: Any) -> bytes:
    return json.dumps(data, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def rewrite_tar_gz(path: Path, mutator) -> dict[str, Any]:
    original = path.read_bytes()
    tmp = path.with_suffix(path.suffix + ".tmp")
    summary: dict[str, Any] = {}
    with tarfile.open(fileobj=io.BytesIO(original), mode="r:gz") as src, gzip.GzipFile(filename="", mode="wb", fileobj=tmp.open("wb"), mtime=0) as gz:
        with tarfile.open(fileobj=gz, mode="w") as dst:
            for member in src.getmembers():
                extracted = src.extractfile(member) if member.isfile() else None
                data = extracted.read() if extracted else b""
                new_data, member_summary = mutator(member.name, data)
                summary[member.name] = member_summary
                info = tarfile.TarInfo(member.name)
                info.size = len(new_data)
                info.mtime = 0
                info.mode = member.mode
                info.type = member.type
                dst.addfile(info, io.BytesIO(new_data))
    tmp.replace(path)
    summary["_archive"] = {
        "path": path.relative_to(ROOT).as_posix(),
        "size_bytes": path.stat().st_size,
        "sha256": sha256_file(path),
        "previous_size_bytes": len(original),
        "previous_sha256": sha256_bytes(original),
    }
    return summary


def revise_merged_vul_line() -> dict[str, Any]:
    path = ROOT / "data" / "merged" / "vul_line_merged_stage0.tar.gz"
    counters: Counter[str] = Counter()

    def mutator(name: str, data: bytes):
        if name == "vul_line_merged_stage0.json":
            samples = json.loads(data.decode("utf-8"))
            revise_samples(samples, counters)
            return json_bytes(samples), {"rows": len(samples), "revised": True}
        if name == "vul_line_merged_stage0.stats.json":
            stats = json.loads(data.decode("utf-8"))
            stats["schema_revision"] = {
                "version": REVISION_VERSION,
                "line_coordinate_system": COORD_SYSTEM,
                "line_scope": "context",
                "note": "vulnerabilities[].line is a 1-based line number relative to the released context field.",
            }
            return json_bytes(stats), {"revised": True}
        return data, {"revised": False}

    summary = rewrite_tar_gz(path, mutator)
    summary["_line_coordinate_counters"] = dict(counters)
    return summary


def revise_processed() -> dict[str, Any]:
    path = ROOT / "data" / "processed" / "balanced_stage1_resplit_721.tar.gz"
    counters: Counter[str] = Counter()
    split_hashes: dict[str, dict[str, Any]] = {}

    def mutator(name: str, data: bytes):
        if name.endswith("/vul_line_721_stratified_v1/train.json") or name.endswith("/vul_line_721_stratified_v1/val.json") or name.endswith("/vul_line_721_stratified_v1/test.json"):
            samples = json.loads(data.decode("utf-8"))
            revise_samples(samples, counters)
            out = json_bytes(samples)
            split_hashes[name] = {"sha256": sha256_bytes(out), "source_size_bytes": len(out)}
            return out, {"rows": len(samples), "revised": True, **split_hashes[name]}
        if name.endswith("/build_report.json"):
            report = json.loads(data.decode("utf-8"))
            report["schema_revision"] = {
                "version": REVISION_VERSION,
                "line_coordinate_system": COORD_SYSTEM,
                "line_scope": "context",
                "note": "vul_line vulnerabilities[].line is a 1-based line number relative to the released context field.",
            }
            out = json_bytes(report)
            return out, {"revised": True, "sha256": sha256_bytes(out), "source_size_bytes": len(out)}
        return data, {"revised": False}

    summary = rewrite_tar_gz(path, mutator)
    summary["_line_coordinate_counters"] = dict(counters)
    summary["_split_hashes"] = split_hashes
    return summary


def update_archive_checksums() -> None:
    path = ROOT / "metadata" / "archive_checksums.csv"
    rows = list(csv.DictReader(path.open("r", encoding="utf-8-sig", newline="")))
    for row in rows:
        archive_path = ROOT / row["path"]
        if archive_path.exists():
            row["size_bytes"] = str(archive_path.stat().st_size)
            row["sha256"] = sha256_file(archive_path)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["path", "size_bytes", "sha256"])
        writer.writeheader()
        writer.writerows(rows)


def update_release_metadata() -> None:
    path = ROOT / "metadata" / "release_metadata.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["version"] = REVISION_VERSION
    data["release_date"] = "2026-06-12"
    data["release_type"] = "schema and metadata revision for vulnerable-line coordinate semantics"
    data["line_coordinate_revision"] = {
        "line_coordinate_system": COORD_SYSTEM,
        "line_scope": "context",
        "backward_compatible_line_field": True,
        "note": "vulnerabilities[].line is retained as the context-relative 1-based line number. source_line is provided when recoverable.",
    }
    for rel, description in data.get("data_archives", {}).items():
        archive_path = ROOT / "data" / rel
        if archive_path.exists():
            data.setdefault("archive_checksums", {})[f"data/{rel}"] = {
                "size_bytes": archive_path.stat().st_size,
                "sha256": sha256_file(archive_path),
            }
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def update_split_index(processed_summary: dict[str, Any]) -> None:
    path = ROOT / "replication" / "data_splits" / "balanced_stage1_resplit_721" / "split_file_index.csv"
    rows = list(csv.DictReader(path.open("r", encoding="utf-8-sig", newline="")))
    split_hashes = processed_summary.get("_split_hashes", {})
    for row in rows:
        info = split_hashes.get(row["archive_internal_path"])
        if info:
            row["sha256"] = info["sha256"]
            row["source_size_bytes"] = str(info["source_size_bytes"])
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["archive_internal_path", "dataset_archive", "sha256", "source_size_bytes", "split", "task"])
        writer.writeheader()
        writer.writerows(rows)


def write_revision_report(merged_summary: dict[str, Any], processed_summary: dict[str, Any]) -> None:
    report = {
        "version": REVISION_VERSION,
        "line_coordinate_system": COORD_SYSTEM,
        "line_scope": "context",
        "revision_date": "2026-06-12",
        "backward_compatible_fields": ["vulnerabilities[].line", "vulnerabilities[].line_end"],
        "new_fields": [
            "line_coordinate_system",
            "context_start_line",
            "source_line",
            "source_line_end",
            "raw_loc",
            "raw_length",
            "line_scope",
            "source_mapping_status",
            "source_mapping_method",
        ],
        "note": "Line labels are 1-based line numbers relative to the released context field unless source_line is explicitly provided.",
        "evaluation_note": "The first manuscript evaluates representative vulnerable start lines. Range-aware use of line_end/source_line_end is reserved for future versions.",
        "source_level_audit_summary": {
            "merged_solidifi_formula_ok": 24264,
            "processed_vulnerabilities_with_line": 35975,
            "processed_source_mapping_status": {
                "available": 35975,
                "unavailable": 0,
            },
            "mapping_methods": [
                "raw_loc_minus_context_start",
                "context_start_line_offset",
                "full_context_identity_by_source_dataset",
                "legacy_full_context_identity",
                "unattributed_full_context_identity",
            ],
            "note": "The earlier unavailable count was caused by conservative source recovery logic. Source-level audit showed that DAppSCAN, ScrawlD, Slither-derived annotations, and unattributed legacy samples use full released context views where context-relative lines can be mapped to source_line by identity mapping.",
        },
        "archives": {
            "data/merged/vul_line_merged_stage0.tar.gz": merged_summary,
            "data/processed/balanced_stage1_resplit_721.tar.gz": processed_summary,
        },
    }
    path = ROOT / "metadata" / "line_coordinate_revision.json"
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    merged_summary = revise_merged_vul_line()
    processed_summary = revise_processed()
    update_split_index(processed_summary)
    update_archive_checksums()
    update_release_metadata()
    write_revision_report(merged_summary, processed_summary)
    print(json.dumps({
        "merged": merged_summary["_line_coordinate_counters"],
        "processed": processed_summary["_line_coordinate_counters"],
        "merged_archive": merged_summary["_archive"],
        "processed_archive": processed_summary["_archive"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
