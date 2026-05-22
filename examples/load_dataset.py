from __future__ import annotations

import json
from pathlib import Path


def load_split(path: str | Path) -> list[dict]:
    path = Path(path)
    return json.loads(path.read_text(encoding="utf-8"))


def vulnerability_types(sample: dict) -> list[str]:
    return sorted({item["type"] for item in sample.get("vulnerabilities", [])})


def vulnerable_lines(sample: dict) -> list[int]:
    lines: set[int] = set()
    for vuln in sample.get("vulnerabilities", []):
        start = vuln.get("line")
        end = vuln.get("line_end") or start
        if start is None:
            continue
        lines.update(range(int(start), int(end) + 1))
    return sorted(lines)


def main() -> None:
    samples = load_split("data/processed/has_vul_721_stratified_v1/train.json")
    first = samples[0]
    print(f"samples: {len(samples)}")
    print(f"sample_id: {first['sample_id']}")
    print(f"has_vulnerability: {first['has_vulnerability']}")
    print(f"vulnerability_types: {vulnerability_types(first)}")
    print(f"vulnerable_lines: {vulnerable_lines(first)}")


if __name__ == "__main__":
    main()

