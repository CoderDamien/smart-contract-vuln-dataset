from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ..data.loader import join_context_lines


@dataclass(slots=True)
class HasVulExample:
    sample_id: str
    code: str
    label: int


class HasVulTask:
    name = "has_vul"
    label_names = ["clean", "vulnerable"]

    @staticmethod
    def from_raw(items: list[dict[str, Any]]) -> list[HasVulExample]:
        examples: list[HasVulExample] = []
        for index, item in enumerate(items):
            contract = item.get("contract") or f"sample_{index}"
            label = int(item.get("has_vulnerability", 0))
            examples.append(HasVulExample(sample_id=str(contract), code=join_context_lines(item), label=label))
        return examples

    @staticmethod
    def extract_label(example: HasVulExample) -> int:
        return example.label
