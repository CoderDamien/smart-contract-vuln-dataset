from __future__ import annotations

import json
import re
from dataclasses import dataclass

from .templates import ANSWER_CLOSE, ANSWER_OPEN
from ..tasks.vul_line import normalize_lines


@dataclass(slots=True)
class ParsedLines:
    lines: list[int]
    raw_text: str
    parser_used: str
    parse_error: str | None = None


@dataclass(slots=True)
class ParsedHasVul:
    label: int | None
    raw_text: str
    parser_used: str
    parse_error: str | None = None


@dataclass(slots=True)
class ParsedVulType:
    label_name: str | None
    raw_text: str
    parser_used: str
    parse_error: str | None = None


@dataclass(slots=True)
class ParsedLineScore:
    score: float
    raw_text: str
    parser_used: str
    parse_error: str | None = None


def _extract_first_json_object(text: str) -> str | None:
    start = text.find("{")
    if start < 0:
        return None

    depth = 0
    for index in range(start, len(text)):
        char = text[index]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start : index + 1]
    return None


def _extract_answer_region(text: str) -> str | None:
    start = text.find(ANSWER_OPEN)
    end = text.find(ANSWER_CLOSE)
    if start < 0:
        return None
    if end < 0 or end <= start:
        return text[start + len(ANSWER_OPEN) :].strip()
    return text[start + len(ANSWER_OPEN) : end].strip()


def parse_vul_line_output(text: str, max_line: int | None = None) -> ParsedLines:
    answer_region = _extract_answer_region(text)
    parse_text = answer_region or text
    json_block = _extract_first_json_object(parse_text)
    if json_block is not None:
        try:
            payload = json.loads(json_block)
            lines = payload.get("lines", [])
            return ParsedLines(
                lines=normalize_lines(lines if isinstance(lines, list) else [lines], max_line=max_line),
                raw_text=text,
                parser_used="answer_json" if answer_region else "json",
            )
        except (json.JSONDecodeError, TypeError, ValueError) as exc:
            json_error = str(exc)
        else:  # pragma: no cover - defensive structure
            json_error = None
    else:
        json_error = "No JSON object found."

    number_candidates = re.findall(r"\d+", parse_text)
    if number_candidates:
        return ParsedLines(
            lines=normalize_lines(number_candidates, max_line=max_line),
            raw_text=text,
            parser_used="answer_regex_numbers" if answer_region else "regex_numbers",
            parse_error=json_error,
        )

    return ParsedLines(
        lines=[],
        raw_text=text,
        parser_used="empty",
        parse_error=json_error,
    )


def parse_has_vul_output(text: str) -> ParsedHasVul:
    answer_region = _extract_answer_region(text)
    parse_text = answer_region or text
    json_block = _extract_first_json_object(parse_text)
    if json_block is not None:
        try:
            payload = json.loads(json_block)
            value = payload.get("has_vulnerability")
            if isinstance(value, bool):
                return ParsedHasVul(label=int(value), raw_text=text, parser_used="answer_json" if answer_region else "json")
            label = int(value)
            if label in {0, 1}:
                return ParsedHasVul(label=label, raw_text=text, parser_used="answer_json" if answer_region else "json")
            json_error = f"Invalid has_vulnerability value: {value}"
        except (json.JSONDecodeError, TypeError, ValueError) as exc:
            json_error = str(exc)
    else:
        json_error = "No JSON object found."

    lowered = parse_text.lower()
    if "vulnerable" in lowered:
        return ParsedHasVul(label=1, raw_text=text, parser_used="answer_keyword" if answer_region else "keyword", parse_error=json_error)
    if "clean" in lowered or "safe" in lowered:
        return ParsedHasVul(label=0, raw_text=text, parser_used="answer_keyword" if answer_region else "keyword", parse_error=json_error)

    digits = re.findall(r"\d+", parse_text)
    for digit in digits:
        if digit in {"0", "1"}:
            return ParsedHasVul(label=int(digit), raw_text=text, parser_used="answer_regex_digit" if answer_region else "regex_digit", parse_error=json_error)

    return ParsedHasVul(label=None, raw_text=text, parser_used="empty", parse_error=json_error)


def parse_vul_type_output(text: str, label_names: list[str]) -> ParsedVulType:
    answer_region = _extract_answer_region(text)
    parse_text = answer_region or text
    json_block = _extract_first_json_object(parse_text)
    label_lookup = {label.lower(): label for label in label_names}
    if json_block is not None:
        try:
            payload = json.loads(json_block)
            value = str(payload.get("vulnerability_type", "")).strip()
            if value.lower() in label_lookup:
                return ParsedVulType(label_name=label_lookup[value.lower()], raw_text=text, parser_used="answer_json" if answer_region else "json")
            json_error = f"Invalid vulnerability_type value: {value}"
        except (json.JSONDecodeError, TypeError, ValueError) as exc:
            json_error = str(exc)
    else:
        json_error = "No JSON object found."

    lowered = parse_text.lower()
    for label in label_names:
        if label.lower() in lowered:
            return ParsedVulType(label_name=label, raw_text=text, parser_used="answer_keyword" if answer_region else "keyword", parse_error=json_error)

    return ParsedVulType(label_name=None, raw_text=text, parser_used="empty", parse_error=json_error)


def parse_vul_line_score_output(text: str) -> ParsedLineScore:
    answer_region = _extract_answer_region(text)
    parse_text = answer_region or text
    json_block = _extract_first_json_object(parse_text)
    if json_block is not None:
        try:
            payload = json.loads(json_block)
            value = float(payload.get("score", 0))
            return ParsedLineScore(
                score=max(0.0, min(100.0, value)),
                raw_text=text,
                parser_used="answer_json" if answer_region else "json",
            )
        except (json.JSONDecodeError, TypeError, ValueError) as exc:
            json_error = str(exc)
    else:
        json_error = "No JSON object found."

    lowered = parse_text.lower()
    if any(token in lowered for token in ["yes", "vulnerable", "true"]):
        return ParsedLineScore(score=100.0, raw_text=text, parser_used="keyword", parse_error=json_error)
    if any(token in lowered for token in ["no", "safe", "false", "clean"]):
        return ParsedLineScore(score=0.0, raw_text=text, parser_used="keyword", parse_error=json_error)

    numbers = re.findall(r"-?\d+(?:\.\d+)?", parse_text)
    if numbers:
        try:
            value = float(numbers[0])
            return ParsedLineScore(
                score=max(0.0, min(100.0, value)),
                raw_text=text,
                parser_used="answer_regex_number" if answer_region else "regex_number",
                parse_error=json_error,
            )
        except ValueError:
            pass

    return ParsedLineScore(score=0.0, raw_text=text, parser_used="empty", parse_error=json_error)
