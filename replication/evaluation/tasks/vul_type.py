from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ..data.loader import join_context_lines


@dataclass(slots=True)
class VulTypeExample:
    sample_id: str
    code: str
    label_names: list[str]

    @property
    def label_name(self) -> str:
        return self.label_names[0]


class VulTypeTask:
    name = "vul_type"

    @staticmethod
    def from_raw(items: list[dict[str, Any]]) -> list[VulTypeExample]:
        examples: list[VulTypeExample] = []
        for index, item in enumerate(items):
            vulnerabilities = item.get("vulnerabilities", [])
            if not vulnerabilities:
                continue
            label_names = []
            for vulnerability in vulnerabilities:
                label_name = str(vulnerability.get("type", "unknown")).strip()
                if label_name and label_name != "unknown" and label_name not in label_names:
                    label_names.append(label_name)
            if not label_names:
                continue
            contract = item.get("contract") or f"sample_{index}"
            examples.append(VulTypeExample(sample_id=str(contract), code=join_context_lines(item), label_names=label_names))
        return examples

    @staticmethod
    def build_label_map(examples: list[VulTypeExample]) -> dict[str, int]:
        labels = sorted({label_name for example in examples for label_name in example.label_names})
        return {label: index for index, label in enumerate(labels)}

    @staticmethod
    def expand_for_single_label_training(examples: list[VulTypeExample]) -> list[VulTypeExample]:
        expanded: list[VulTypeExample] = []
        for example in examples:
            for label_name in example.label_names:
                expanded.append(
                    VulTypeExample(
                        sample_id=example.sample_id,
                        code=example.code,
                        label_names=[label_name],
                    )
                )
        return expanded

    @staticmethod
    def multi_reference_metrics(
        references: list[list[int]],
        predictions: list[int],
        *,
        num_labels: int,
    ) -> dict[str, float]:
        hits = [int(prediction in set(reference)) for reference, prediction in zip(references, predictions)]
        accuracy = sum(hits) / len(hits) if hits else 0.0
        true_positive = sum(hits)
        predicted_positive = len(predictions)
        actual_positive = sum(len(set(reference)) for reference in references)
        precision = true_positive / predicted_positive if predicted_positive else 0.0
        recall = true_positive / actual_positive if actual_positive else 0.0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0

        macro_precisions: list[float] = []
        macro_recalls: list[float] = []
        macro_f1s: list[float] = []
        for label in range(num_labels):
            label_tp = 0
            label_fp = 0
            label_fn = 0
            for reference, prediction in zip(references, predictions):
                reference_set = set(reference)
                if prediction == label and label in reference_set:
                    label_tp += 1
                elif prediction == label and label not in reference_set:
                    label_fp += 1
                elif prediction != label and label in reference_set:
                    label_fn += 1
            label_precision = label_tp / (label_tp + label_fp) if label_tp + label_fp else 0.0
            label_recall = label_tp / (label_tp + label_fn) if label_tp + label_fn else 0.0
            label_f1 = 2 * label_precision * label_recall / (label_precision + label_recall) if label_precision + label_recall else 0.0
            macro_precisions.append(label_precision)
            macro_recalls.append(label_recall)
            macro_f1s.append(label_f1)

        macro_precision = sum(macro_precisions) / num_labels if num_labels else 0.0
        macro_recall = sum(macro_recalls) / num_labels if num_labels else 0.0
        macro_f1 = sum(macro_f1s) / num_labels if num_labels else 0.0
        return {
            "accuracy": float(accuracy),
            "hit_accuracy": float(accuracy),
            "precision": float(precision),
            "recall": float(recall),
            "f1": float(f1),
            "macro_precision": float(macro_precision),
            "macro_recall": float(macro_recall),
            "macro_f1": float(macro_f1),
        }

    @staticmethod
    def multi_label_subset_metrics(
        references: list[list[int]],
        predictions: list[int],
        *,
        num_labels: int,
    ) -> dict[str, float]:
        subset_references: list[list[int]] = []
        subset_predictions: list[int] = []
        for reference, prediction in zip(references, predictions):
            if len(set(reference)) > 1:
                subset_references.append(reference)
                subset_predictions.append(prediction)
        metrics = VulTypeTask.multi_reference_metrics(subset_references, subset_predictions, num_labels=num_labels)
        return {
            "multi_label_examples": float(len(subset_references)),
            **{f"multi_label_{key}": value for key, value in metrics.items()},
        }
