from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(slots=True)
class VulLineMetrics:
    strict_precision: float
    strict_recall: float
    strict_f1: float
    tolerant_precision: float
    tolerant_recall: float
    tolerant_f1: float
    contract_hit: float
    top_k_hit: float
    avg_min_distance: float

    def to_dict(self) -> dict[str, float]:
        return {
            "strict_precision": self.strict_precision,
            "strict_recall": self.strict_recall,
            "strict_f1": self.strict_f1,
            "tolerant_precision": self.tolerant_precision,
            "tolerant_recall": self.tolerant_recall,
            "tolerant_f1": self.tolerant_f1,
            "contract_hit": self.contract_hit,
            "top_k_hit": self.top_k_hit,
            "avg_min_distance": self.avg_min_distance,
        }


def _safe_div(numerator: float, denominator: float) -> float:
    return numerator / denominator if denominator else 0.0


def _f1(precision: float, recall: float) -> float:
    return _safe_div(2 * precision * recall, precision + recall)


def _is_tolerant_match(pred_line: int, true_lines: Iterable[int], tolerance: int) -> bool:
    return any(abs(pred_line - true_line) <= tolerance for true_line in true_lines)


def _min_distance(pred_line: int, true_lines: list[int]) -> int:
    if not true_lines:
        return 0
    return min(abs(pred_line - true_line) for true_line in true_lines)


def compute_vul_line_metrics(
    predictions: list[list[int]],
    references: list[list[int]],
    *,
    tolerance: int = 2,
    top_k: int = 3,
) -> VulLineMetrics:
    if len(predictions) != len(references):
        raise ValueError("Predictions and references must have the same length.")

    strict_tp = 0
    strict_pred_total = 0
    strict_true_total = 0

    tolerant_tp_pred = 0
    tolerant_tp_true = 0
    tolerant_pred_total = 0
    tolerant_true_total = 0

    contract_hits = 0
    top_k_hits = 0
    min_distances: list[int] = []

    for pred_lines, true_lines in zip(predictions, references):
        pred_set = sorted(set(pred_lines))
        true_set = sorted(set(true_lines))

        strict_matches = set(pred_set).intersection(true_set)
        strict_tp += len(strict_matches)
        strict_pred_total += len(pred_set)
        strict_true_total += len(true_set)

        tolerant_pred_hits = sum(1 for pred_line in pred_set if _is_tolerant_match(pred_line, true_set, tolerance))
        tolerant_true_hits = sum(1 for true_line in true_set if _is_tolerant_match(true_line, pred_set, tolerance))
        tolerant_tp_pred += tolerant_pred_hits
        tolerant_tp_true += tolerant_true_hits
        tolerant_pred_total += len(pred_set)
        tolerant_true_total += len(true_set)

        if tolerant_true_hits > 0:
            contract_hits += 1

        if any(_is_tolerant_match(pred_line, true_set, tolerance) for pred_line in pred_set[:top_k]):
            top_k_hits += 1

        if pred_set and true_set:
            min_distances.extend(_min_distance(pred_line, true_set) for pred_line in pred_set)

    strict_precision = _safe_div(strict_tp, strict_pred_total)
    strict_recall = _safe_div(strict_tp, strict_true_total)
    tolerant_precision = _safe_div(tolerant_tp_pred, tolerant_pred_total)
    tolerant_recall = _safe_div(tolerant_tp_true, tolerant_true_total)
    avg_min_distance = _safe_div(sum(min_distances), len(min_distances))

    total_samples = len(predictions)
    return VulLineMetrics(
        strict_precision=strict_precision,
        strict_recall=strict_recall,
        strict_f1=_f1(strict_precision, strict_recall),
        tolerant_precision=tolerant_precision,
        tolerant_recall=tolerant_recall,
        tolerant_f1=_f1(tolerant_precision, tolerant_recall),
        contract_hit=_safe_div(contract_hits, total_samples),
        top_k_hit=_safe_div(top_k_hits, total_samples),
        avg_min_distance=avg_min_distance,
    )
