from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime
from pathlib import Path
from typing import Any


def _parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def _runtime_fields(state_path: Path) -> dict[str, Any]:
    if not state_path.exists():
        return {
            "started_at": None,
            "completed_at": None,
            "runtime_seconds": None,
            "runtime_minutes": None,
        }
    state = json.loads(state_path.read_text(encoding="utf-8"))
    started_at = state.get("started_at")
    completed_at = state.get("completed_at") or state.get("updated_at")
    started = _parse_iso(started_at)
    completed = _parse_iso(completed_at)
    runtime_seconds = None
    if started and completed and state.get("status") in {"completed", "failed", "unsupported"}:
        runtime_seconds = max(0.0, (completed - started).total_seconds())
    return {
        "started_at": started_at,
        "completed_at": completed_at,
        "runtime_seconds": runtime_seconds,
        "runtime_minutes": None if runtime_seconds is None else runtime_seconds / 60,
    }


def _state_path_for_row(output_root: Path, row: dict[str, str]) -> Path:
    model_dir = (row.get("model_name") or "").replace("/", "_")
    task = row["task"]
    mode_dir = "finetune" if row["mode"] == "finetune" else row["mode"]
    return output_root / row["run_name"] / model_dir / f"{task}__{mode_dir}" / "state.json"


def enrich(summary_dir: Path, output_root: Path) -> None:
    csv_path = summary_dir / "matrix_summary.csv"
    json_path = summary_dir / "matrix_summary.json"
    if not csv_path.exists():
        raise FileNotFoundError(csv_path)

    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    enriched_rows: list[dict[str, Any]] = []
    for row in rows:
        enriched = dict(row)
        state_fields = _runtime_fields(_state_path_for_row(output_root, row))
        for key, value in state_fields.items():
            if not enriched.get(key):
                enriched[key] = value
        enriched_rows.append(enriched)

    out_csv = summary_dir / "matrix_summary_with_runtime.csv"
    out_json = summary_dir / "matrix_summary_with_runtime.json"
    fieldnames = list(enriched_rows[0].keys()) if enriched_rows else []
    for extra in ("started_at", "completed_at", "runtime_seconds", "runtime_minutes"):
        if extra not in fieldnames:
            fieldnames.append(extra)
    with out_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(enriched_rows)
    out_json.write_text(json.dumps(enriched_rows, ensure_ascii=False, indent=2), encoding="utf-8")

    if json_path.exists():
        json_path.write_text(json.dumps(enriched_rows, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Backfill per-job runtime fields from state.json into matrix summaries.")
    parser.add_argument("--summary-dir", required=True)
    parser.add_argument("--output-root", required=True)
    args = parser.parse_args()
    enrich(Path(args.summary_dir), Path(args.output_root))


if __name__ == "__main__":
    main()
