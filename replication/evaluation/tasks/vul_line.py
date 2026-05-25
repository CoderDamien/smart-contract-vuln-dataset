from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Any

from ..data.loader import join_context_lines


@dataclass(slots=True)
class VulLineExample:
    sample_id: str
    code: str
    true_lines: list[int]


@dataclass(slots=True)
class VulLineCandidate:
    sample_id: str
    line_no: int
    candidate_text: str
    context_text: str
    true_lines: list[int]
    label: int

    @property
    def code(self) -> str:
        return self.context_text


def normalize_lines(lines: list[Any], max_line: int | None = None) -> list[int]:
    normalized: set[int] = set()
    for value in lines:
        if isinstance(value, str):
            value = value.strip()
        try:
            line = int(value)
        except (TypeError, ValueError):
            continue
        if line <= 0:
            continue
        if max_line is not None and line > max_line:
            continue
        normalized.add(line)
    return sorted(normalized)


class VulLineTask:
    name = "vul_line"

    @staticmethod
    def from_raw(items: list[dict[str, Any]]) -> list[VulLineExample]:
        examples: list[VulLineExample] = []
        for index, item in enumerate(items):
            vulnerabilities = item.get("vulnerabilities", [])
            if not vulnerabilities:
                continue

            code = join_context_lines(item)
            max_line = max(len(code.splitlines()), 1)
            lines = normalize_lines([vuln.get("line") for vuln in vulnerabilities], max_line=max_line)
            if not lines:
                continue

            contract = item.get("contract") or f"sample_{index}"
            examples.append(
                VulLineExample(
                    sample_id=str(contract),
                    code=code,
                    true_lines=lines,
                )
            )
        return examples


def _line_priority(line: str) -> int:
    text = line.strip().lower()
    if not text:
        return -100
    score = 0
    keywords = [
        "call.value",
        ".call(",
        "delegatecall",
        "send(",
        "transfer(",
        "tx.origin",
        "block.timestamp",
        "now",
        "selfdestruct",
        "suicide",
        "assembly",
        "sha3",
        "keccak256",
        "require(",
        "assert(",
    ]
    score += sum(3 for keyword in keywords if keyword in text)
    if any(token in text for token in ["if ", "for ", "while ", "return "]):
        score += 1
    if text.startswith("//") or text.startswith("*"):
        score -= 2
    return score


def build_candidate_text(lines: list[str], line_no: int, *, context_window: int) -> str:
    start = max(line_no - context_window, 1)
    end = min(line_no + context_window, len(lines))
    rendered: list[str] = []
    for current in range(start, end + 1):
        marker = ">>" if current == line_no else "  "
        rendered.append(f"{marker} {current}: {lines[current - 1]}")
    return "\n".join(rendered)


def build_line_rank_candidates(
    examples: list[VulLineExample],
    *,
    context_window: int = 4,
    max_candidates: int = 0,
    include_all_positive: bool = True,
) -> list[VulLineCandidate]:
    candidates: list[VulLineCandidate] = []
    for example in examples:
        lines = example.code.splitlines()
        true_set = set(example.true_lines)
        line_numbers = [index for index, line in enumerate(lines, start=1) if line.strip()]
        if max_candidates and len(line_numbers) > max_candidates:
            protected = true_set if include_all_positive else set()
            ranked = sorted(
                line_numbers,
                key=lambda line_no: (
                    line_no in protected,
                    _line_priority(lines[line_no - 1]),
                    -line_no,
                ),
                reverse=True,
            )
            line_numbers = sorted(ranked[:max_candidates])

        for line_no in line_numbers:
            candidates.append(
                VulLineCandidate(
                    sample_id=example.sample_id,
                    line_no=line_no,
                    candidate_text=lines[line_no - 1],
                    context_text=build_candidate_text(lines, line_no, context_window=context_window),
                    true_lines=example.true_lines,
                    label=1 if line_no in true_set else 0,
                )
            )
    return candidates


def sample_line_rank_train_candidates(
    examples: list[VulLineExample],
    *,
    context_window: int = 4,
    negatives_per_positive: int = 8,
    seed: int = 42,
) -> list[VulLineCandidate]:
    rng = random.Random(seed)
    sampled: list[VulLineCandidate] = []
    for example in examples:
        all_candidates = build_line_rank_candidates(
            [example],
            context_window=context_window,
            max_candidates=0,
            include_all_positive=True,
        )
        positives = [candidate for candidate in all_candidates if candidate.label == 1]
        negatives = [candidate for candidate in all_candidates if candidate.label == 0]
        negative_count = min(len(negatives), max(len(positives), 1) * negatives_per_positive)
        sampled.extend(positives)
        sampled.extend(rng.sample(negatives, negative_count) if negative_count else [])
    rng.shuffle(sampled)
    return sampled
