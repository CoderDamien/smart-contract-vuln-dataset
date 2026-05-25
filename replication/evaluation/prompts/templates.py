from __future__ import annotations

from typing import Iterable

from ..config import ExperimentConfig
from ..tasks.has_vul import HasVulExample
from ..tasks.vul_line import VulLineCandidate, VulLineExample
from ..tasks.vul_type import VulTypeExample


ANSWER_OPEN = "<answer>"
ANSWER_CLOSE = "</answer>"


def wrap_answer(json_payload: str) -> str:
    return f"{ANSWER_OPEN}{json_payload}{ANSWER_CLOSE}"


def format_vul_line_json(lines: list[int]) -> str:
    return '{"lines": [' + ", ".join(str(line) for line in lines) + ']}'


def format_vul_line_score_json(score: int | float) -> str:
    return '{"score": ' + str(int(score)) + "}"


def format_has_vul_json(label: int) -> str:
    return '{"has_vulnerability": ' + ("1" if label else "0") + "}"


def format_vul_type_json(label_name: str) -> str:
    return '{"vulnerability_type": "' + label_name + '"}'


def _build_vul_line_examples_block(examples: Iterable[VulLineExample]) -> str:
    blocks: list[str] = []
    for example in examples:
        blocks.append(
            "\n".join(
                [
                    "Example input code:",
                    "```solidity",
                    example.code,
                    "```",
                    f"Example output: {wrap_answer(format_vul_line_json(example.true_lines))}",
                ]
            )
        )
    return "\n\n".join(blocks)


def _build_vul_line_rank_examples_block(examples: Iterable[VulLineCandidate]) -> str:
    blocks: list[str] = []
    for example in examples:
        score = 100 if example.label else 0
        blocks.append(
            "\n".join(
                [
                    "Example candidate:",
                    "```solidity",
                    example.context_text,
                    "```",
                    f"Example output: {wrap_answer(format_vul_line_score_json(score))}",
                ]
            )
        )
    return "\n\n".join(blocks)


def _build_has_vul_examples_block(examples: Iterable[HasVulExample]) -> str:
    blocks: list[str] = []
    for example in examples:
        blocks.append(
            "\n".join(
                [
                    "Example input code:",
                    "```solidity",
                    example.code,
                    "```",
                    f"Example output: {wrap_answer(format_has_vul_json(example.label))}",
                ]
            )
        )
    return "\n\n".join(blocks)


def _build_vul_type_examples_block(examples: Iterable[VulTypeExample]) -> str:
    blocks: list[str] = []
    for example in examples:
        blocks.append(
            "\n".join(
                [
                    "Example input code:",
                    "```solidity",
                    example.code,
                    "```",
                    f"Example output: {wrap_answer(format_vul_type_json(example.label_name))}",
                ]
            )
        )
    return "\n\n".join(blocks)


def build_vul_line_prompt(
    *,
    example: VulLineExample,
    config: ExperimentConfig,
    fewshot_examples: list[VulLineExample] | None = None,
) -> str:
    template_name = config.prompt_template_name or "vul_line_json"
    header = [
        "You are a smart contract vulnerability localization assistant.",
        "Read the Solidity code and predict all vulnerable line numbers.",
        f"Return exactly one answer in the form {ANSWER_OPEN}" + '{"lines": [line_numbers]}' + f"{ANSWER_CLOSE}.",
        "Do not output any code continuation, explanation, or extra text outside the answer tags.",
        "Do not explain your reasoning.",
    ]

    if template_name == "vul_line_json_with_hint":
        header.insert(
            2,
            "If no clear vulnerable line can be identified, return an empty list instead of guessing.",
        )

    prompt_parts = ["\n".join(header)]
    if fewshot_examples:
        prompt_parts.append(_build_vul_line_examples_block(fewshot_examples))

    prompt_parts.append(
        "\n".join(
            [
                "Target code:",
                "```solidity",
                example.code,
                "```",
                f"Answer using exactly one line starting with {ANSWER_OPEN} and ending with {ANSWER_CLOSE}:",
            ]
        )
    )
    return "\n\n".join(prompt_parts)


def build_vul_line_rank_prompt(
    *,
    candidate: VulLineCandidate,
    config: ExperimentConfig,
    fewshot_examples: list[VulLineCandidate] | None = None,
) -> str:
    template_name = config.prompt_template_name or "vul_line_rank_score"
    header = [
        "You are a smart contract vulnerability localization assistant.",
        "Judge only the Solidity line marked with >>.",
        "Return a vulnerability likelihood score from 0 to 100.",
        f"Return exactly one answer in the form {ANSWER_OPEN}" + '{"score": 0_to_100}' + f"{ANSWER_CLOSE}.",
        "Use a high score only when the marked line itself is likely to be the vulnerable line.",
        "Do not output any explanation or extra text outside the answer tags.",
    ]
    if template_name == "vul_line_rank_score_with_hint":
        header.insert(3, "Nearby lines are context only; do not score them unless the marked line is the vulnerable operation.")

    prompt_parts = ["\n".join(header)]
    if fewshot_examples:
        prompt_parts.append(_build_vul_line_rank_examples_block(fewshot_examples))
    prompt_parts.append(
        "\n".join(
            [
                "Target candidate:",
                "```solidity",
                candidate.context_text,
                "```",
                f"Answer using exactly one line starting with {ANSWER_OPEN} and ending with {ANSWER_CLOSE}:",
            ]
        )
    )
    return "\n\n".join(prompt_parts)


def build_has_vul_prompt(
    *,
    example: HasVulExample,
    config: ExperimentConfig,
    fewshot_examples: list[HasVulExample] | None = None,
) -> str:
    template_name = config.prompt_template_name or "has_vul_json"
    header = [
        "You are a smart contract security assistant.",
        "Read the Solidity code and decide whether it contains a vulnerability.",
        f"Return exactly one answer in the form {ANSWER_OPEN}" + '{"has_vulnerability": 0_or_1}' + f"{ANSWER_CLOSE}.",
        "Do not output any code continuation, explanation, or extra text outside the answer tags.",
        "Do not explain your reasoning.",
    ]
    if template_name == "has_vul_json_with_hint":
        header.insert(2, "Return 0 only if the code appears clean; otherwise return 1.")
    prompt_parts = ["\n".join(header)]
    if fewshot_examples:
        prompt_parts.append(_build_has_vul_examples_block(fewshot_examples))
    prompt_parts.append(
        "\n".join(
            [
                "Target code:",
                "```solidity",
                example.code,
                "```",
                f"Answer using exactly one line starting with {ANSWER_OPEN} and ending with {ANSWER_CLOSE}:",
            ]
        )
    )
    return "\n\n".join(prompt_parts)


def build_vul_type_prompt(
    *,
    example: VulTypeExample,
    config: ExperimentConfig,
    label_names: list[str],
    fewshot_examples: list[VulTypeExample] | None = None,
) -> str:
    template_name = config.prompt_template_name or "vul_type_json"
    header = [
        "You are a smart contract vulnerability classification assistant.",
        "Read the Solidity code and predict one vulnerability type present in the contract.",
        "Choose exactly one label from this list: " + ", ".join(label_names),
        "If multiple vulnerability types are present, output any one correct label from the provided list.",
        f"Return exactly one answer in the form {ANSWER_OPEN}" + '{"vulnerability_type": "label"}' + f"{ANSWER_CLOSE}.",
        "Do not output any code continuation, explanation, or extra text outside the answer tags.",
        "Do not explain your reasoning.",
    ]
    if template_name == "vul_type_json_with_hint":
        header.insert(4, 'If uncertain, still output exactly one label from the provided list.')
    prompt_parts = ["\n".join(header)]
    if fewshot_examples:
        prompt_parts.append(_build_vul_type_examples_block(fewshot_examples))
    prompt_parts.append(
        "\n".join(
            [
                "Target code:",
                "```solidity",
                example.code,
                "```",
                f"Answer using exactly one line starting with {ANSWER_OPEN} and ending with {ANSWER_CLOSE}:",
            ]
        )
    )
    return "\n\n".join(prompt_parts)
