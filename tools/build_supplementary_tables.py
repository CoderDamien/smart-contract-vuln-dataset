from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter


ROOT = Path(__file__).resolve().parents[1]
REPLICATION = ROOT / "replication"
RESULTS = REPLICATION / "results"
SUPP = ROOT / "supplementary"
TABLES = SUPP / "tables"


TABLE_DEFS = [
    ("S1", "Formal experiment matrix and completion status", "paper_experiment_matrix_closure.csv"),
    ("S2", "Model inventory and experiment coverage by model family", "model_summary.csv"),
    ("S3", "Complete model-task-method metric matrix", "paper_experiment_metrics_all.csv"),
    ("S4", "Vulnerability existence detection results", "has_vul_metrics.csv"),
    ("S5", "Vulnerability type classification results", "vul_type_metrics.csv"),
    ("S6", "Vulnerable line localization results", "vul_line_metrics.csv"),
    ("S7", "Traditional pretrained-code baselines", None),
    ("S8", "Qwen2.5-Coder parameter-scale analysis", None),
    ("S9", "Prompt ablation results for Qwen2.5-Coder-7B and 32B", "prompt_ablation.csv"),
    ("S10", "Data-completion before/after paired results", "data_completion_pairs.csv"),
    ("S11", "Complete method-pair comparison records", None),
    ("S12", "Runtime and performance trade-off records", "all_result_metrics.csv"),
    ("S13", "Prediction artifact and parsing-error audit", None),
    ("S14", "Figure source data and generated figure inventory", None),
]

ZH_TITLES = {
    "Table S1": "正式实验矩阵与完成状态",
    "Table S2": "模型清单与模型族实验覆盖",
    "Table S3": "完整模型-任务-方法指标矩阵",
    "Table S4": "漏洞存在性检测结果",
    "Table S5": "漏洞类型分类结果",
    "Table S6": "漏洞行定位结果",
    "Table S7": "传统预训练代码模型基线",
    "Table S8": "Qwen2.5-Coder 参数规模分析",
    "Table S9": "Qwen2.5-Coder-7B 与 32B 的提示消融结果",
    "Table S10": "数据补齐前后配对结果",
    "Table S11": "完整方法配对比较记录",
    "Table S12": "运行成本与性能权衡记录",
    "Table S13": "预测产物与解析错误审计",
    "Table S14": "图表源数据与生成图文件清单",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = sorted({key for row in rows for key in row.keys()})
    if not fields:
        fields = ["note"]
        rows = [{"note": "No records"}]
    with path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def value(row: dict[str, str], *names: str) -> str:
    for name in names:
        if name in row and str(row[name]).strip():
            return str(row[name]).strip()
    return ""


def number(text: str):
    if text is None:
        return None
    text = str(text).strip()
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def metric_for(row: dict[str, str]):
    task = value(row, "任务", "task")
    if task == "has_vul":
        return number(value(row, "f1"))
    if task == "vul_type":
        return number(value(row, "macro_f1", "f1"))
    if task == "vul_line":
        return number(value(row, "tolerant_f1", "strict_f1"))
    return None


def table_s7(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    baseline_terms = ("codebert", "graphcodebert", "unixcoder", "codet5")
    return [r for r in rows if any(term in value(r, "模型", "model").lower() for term in baseline_terms)]


def table_s8(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return [r for r in rows if "qwen2.5-coder" in value(r, "模型", "model").lower()]


def table_s11(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    grouped: dict[tuple[str, str], dict[str, dict[str, str]]] = {}
    for row in rows:
        model = value(row, "模型", "model")
        task = value(row, "任务", "task")
        method = value(row, "方法", "method")
        if not model or not task or not method:
            continue
        grouped.setdefault((model, task), {})[method] = row

    comparisons = [
        ("prompt_vs_direct", "prompt", "direct"),
        ("qlora_vs_direct", "qlora", "direct"),
        ("full_vs_direct", "full", "direct"),
        ("full_vs_qlora", "full", "qlora"),
    ]
    out = []
    for (model, task), methods in grouped.items():
        for label, left, right in comparisons:
            if left not in methods or right not in methods:
                continue
            lv = metric_for(methods[left])
            rv = metric_for(methods[right])
            if lv is None or rv is None:
                continue
            out.append(
                {
                    "comparison": label,
                    "model": model,
                    "task": task,
                    "left_method": left,
                    "right_method": right,
                    "left_metric": f"{lv:.6f}",
                    "right_metric": f"{rv:.6f}",
                    "delta": f"{(lv - rv):.6f}",
                    "metric_used": "f1 for has_vul; macro_f1 for vul_type; tolerant_f1 for vul_line",
                }
            )
    return out


def table_s13() -> list[dict[str, str]]:
    pred_rows = read_csv(REPLICATION / "prediction_summaries" / "prediction_artifact_index.csv")
    prompt_rows = read_csv(RESULTS / "prompt_ablation.csv")
    out = []
    for row in pred_rows:
        out.append(
            {
                "source": "prediction_artifact_index",
                "run_name": value(row, "run_name"),
                "model": value(row, "model"),
                "task": value(row, "task"),
                "method": value(row, "method"),
                "prediction_rows": value(row, "prediction_rows"),
                "size_bytes": value(row, "size_bytes"),
                "sha256": value(row, "sha256"),
                "source_path": value(row, "source_path"),
            }
        )
    for row in prompt_rows:
        selected = {
            "source": "prompt_ablation_parse_summary",
            "run_name": value(row, "run_name", "运行名称"),
            "model": value(row, "模型"),
            "task": value(row, "任务"),
            "method": value(row, "模式"),
        }
        for key, val in row.items():
            key_l = key.lower()
            if any(token in key_l for token in ["parse", "empty", "format", "json", "fail"]):
                selected[key] = val
        out.append(selected)
    return out


def table_s14() -> list[dict[str, str]]:
    rows = []
    for base in [REPLICATION / "figures", REPLICATION / "figure_source"]:
        for path in sorted(base.rglob("*")):
            if path.is_file():
                rows.append(
                    {
                        "artifact_type": "figure" if path.suffix.lower() == ".svg" else "figure_source",
                        "path": path.relative_to(ROOT).as_posix(),
                        "size_bytes": str(path.stat().st_size),
                        "sha256": sha256(path),
                    }
                )
    return rows


def build_tables() -> list[dict[str, str]]:
    all_metrics = read_csv(RESULTS / "paper_experiment_metrics_all.csv")
    TABLES.mkdir(parents=True, exist_ok=True)
    produced = []
    for sid, title, source in TABLE_DEFS:
        if sid == "S7":
            rows = table_s7(all_metrics)
            sources = "replication/results/paper_experiment_metrics_all.csv"
        elif sid == "S8":
            rows = table_s8(all_metrics)
            sources = "replication/results/paper_experiment_metrics_all.csv"
        elif sid == "S11":
            rows = table_s11(all_metrics)
            sources = "replication/results/paper_experiment_metrics_all.csv"
        elif sid == "S13":
            rows = table_s13()
            sources = "replication/prediction_summaries/prediction_artifact_index.csv; replication/results/prompt_ablation.csv"
        elif sid == "S14":
            rows = table_s14()
            sources = "replication/figures/; replication/figure_source/"
        else:
            rows = read_csv(RESULTS / source)
            sources = f"replication/results/{source}"

        filename = f"Table_{sid}.csv"
        path = TABLES / filename
        write_csv(path, rows)
        produced.append(
            {
                "supplementary_table": f"Table {sid}",
                "title": title,
                "file": f"supplementary/tables/{filename}",
                "source": sources,
                "rows": str(len(rows)),
                "sha256": sha256(path),
            }
        )
    write_csv(SUPP / "Supplementary_Table_Index.csv", produced)
    return produced


def clean_sheet_name(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9_]", "_", text)
    return text[:31]


def build_workbook(index: list[dict[str, str]]) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Index"
    write_sheet(ws, index)
    for item in index:
        csv_path = ROOT / item["file"]
        rows = read_csv(csv_path)
        ws = wb.create_sheet(clean_sheet_name(item["supplementary_table"].replace(" ", "_")))
        ws["A1"] = f"{item['supplementary_table']}. {item['title']}"
        ws["A1"].font = Font(bold=True, size=13)
        write_sheet(ws, rows, start_row=3)
    wb.save(SUPP / "supplementary_tables.xlsx")


def write_sheet(ws, rows: list[dict[str, str]], start_row: int = 1) -> None:
    fields = sorted({key for row in rows for key in row.keys()}) or ["note"]
    header_row = start_row
    for col, field in enumerate(fields, 1):
        cell = ws.cell(header_row, col, field)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="3B4A5A")
    for r_idx, row in enumerate(rows, header_row + 1):
        for c_idx, field in enumerate(fields, 1):
            ws.cell(r_idx, c_idx, row.get(field, ""))
    ws.freeze_panes = ws.cell(header_row + 1, 1).coordinate
    ws.auto_filter.ref = f"A{header_row}:{get_column_letter(len(fields))}{max(header_row + 1, header_row + len(rows))}"
    for col_idx, field in enumerate(fields, 1):
        max_len = len(field)
        for row in rows[:200]:
            max_len = max(max_len, len(str(row.get(field, ""))))
        ws.column_dimensions[get_column_letter(col_idx)].width = min(max(max_len + 2, 10), 48)


def write_readme(index: list[dict[str, str]]) -> None:
    lines = [
        "# Supplementary Tables",
        "",
        "This directory contains the numbered supplementary tables referenced by the manuscript. The table numbers are stable and match the in-text references in `Q1_English_IST_polished.md`.",
        "",
        "| Table | Title | CSV | Rows | Source |",
        "|---|---|---|---:|---|",
    ]
    for item in index:
        lines.append(f"| {item['supplementary_table']} | {item['title']} | `{item['file']}` | {item['rows']} | {item['source']} |")
    lines.extend(
        [
            "",
            "Critical manuscript references:",
            "",
            "- Line 124 refers to Supplementary Table S1, available as `supplementary/tables/Table_S1.csv`.",
            "- Line 316 refers to Supplementary Tables S5, S9, and S13, available as `supplementary/tables/Table_S5.csv`, `supplementary/tables/Table_S9.csv`, and `supplementary/tables/Table_S13.csv`.",
            "",
            "A combined workbook is provided as `supplementary/supplementary_tables.xlsx` with worksheets named `Table_S1` to `Table_S14`.",
        ]
    )
    (SUPP / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    zh = [
        "# 补充材料表",
        "",
        "本目录存放论文正文引用的编号补充表。表号与 `Q1_English_IST_polished.md` 中的正文引用保持一致。",
        "",
        "| 表号 | 标题 | CSV | 行数 | 来源 |",
        "|---|---|---|---:|---|",
    ]
    for item in index:
        zh_title = ZH_TITLES.get(item["supplementary_table"], item["title"])
        zh.append(f"| {item['supplementary_table']} | {zh_title} | `{item['file']}` | {item['rows']} | {item['source']} |")
    zh.extend(
        [
            "",
            "重点正文引用核对：",
            "",
            "- 第 124 行引用 Supplementary Table S1，对应 `supplementary/tables/Table_S1.csv`。",
            "- 第 316 行引用 Supplementary Tables S5, S9, and S13，分别对应 `supplementary/tables/Table_S5.csv`、`supplementary/tables/Table_S9.csv` 和 `supplementary/tables/Table_S13.csv`。",
            "",
            "同时提供合并工作簿 `supplementary/supplementary_tables.xlsx`，其中工作表命名为 `Table_S1` 至 `Table_S14`。",
        ]
    )
    (SUPP / "README.zh-CN.md").write_text("\n".join(zh) + "\n", encoding="utf-8")


def write_manifest() -> None:
    files = []
    for path in sorted(SUPP.rglob("*")):
        if path.is_file() and path.name != "manifest.json":
            files.append(
                {
                    "path": path.relative_to(ROOT).as_posix(),
                    "size_bytes": path.stat().st_size,
                    "sha256": sha256(path),
                }
            )
    (SUPP / "manifest.json").write_text(
        json.dumps({"file_count": len(files), "files": files}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    index = build_tables()
    build_workbook(index)
    write_readme(index)
    write_manifest()


if __name__ == "__main__":
    main()
