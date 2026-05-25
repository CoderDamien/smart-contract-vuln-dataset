# Q1 figure redesign notes

Source workbook: `本地实验结果汇总_按模型任务结果.xlsx`.

## Statistical scope

- Main formal figures use 220 records after excluding the narrative-only `补齐前后对比` rows.
- The closure statement remains `226/226/0` because the workbook contains 226 completed formal rows.
- Fig.6 uses the six explicit before/after pairs from `补齐前后12条明细`.
- Excluded `补齐前后对比` rows from main statistics: 6.
- Rows whose `run_name` is duplicated in the raw formal table: 8.

## Figure set

- Fig.1: protocol and closed experiment matrix.
- Fig.2: task hierarchy using best and mean task-specific scores.
- Fig.3: paired method deltas within the same model and task.
- Fig.4: Qwen2.5-Coder scaling by mode.
- Fig.5: prompt ablation for 7B/32B, including output failure rates.
- Fig.6: dataset completion before/after pairs.
- Fig.7: family-task-mode heatmap.
- Fig.8: line localization exactness versus contract-level hit.
- Fig.9: runtime/performance trade-off.