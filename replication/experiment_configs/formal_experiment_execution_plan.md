# 正式实验执行方案

## 文档地位

本文档是区块链智能合约漏洞检测实验的正式执行依据。后续实验调度、服务器分工、模型选择、结果汇总和论文结果分析，应优先遵循本文档。

如需变更本文档中的模型矩阵、任务定义、方法范围、服务器分工或暂停点，必须先与用户确认，再修改文档和对应执行脚本。

## 实验目标

本实验不以证明某一种模型或训练方法最好为目标，而是系统展示不同资源条件下的模型选择结果，帮助读者根据自身条件选择合适方案。

实验需要同时回答以下问题：

- 传统代码预训练模型在智能合约漏洞检测任务上的表现如何。
- 开源代码大模型在不同参数规模下的表现如何。
- 同一模型在 direct、prompt、full fine-tune、QLoRA 等方式下的差异如何。
- 小参数模型与 7B 以上模型相比，性能、训练成本和运行时间如何变化。
- API 闭源强模型在无微调条件下能达到怎样的上限。

## 数据集与任务

正式实验统一使用数据集：

`balanced_stage1_resplit_721`

数据目录：

`data/prepared/balanced_stage1_resplit_721`

三类任务保持不变：

- `has_vul`：漏洞存在性二分类。
- `vul_type`：漏洞类型检测，多真实标签评估；模型预测命中任一真实漏洞类型即视为类型命中。
- `vul_line`：漏洞行定位，使用 line-rank 候选行排序方案，记录 strict、tolerant、contract hit、candidate recall 等指标。

`vul_type` 中多漏洞样本必须单独输出预测结果和指标，用于论文中单独分析多漏洞检测能力。

## 方法矩阵

所有本地开源模型原则上按以下方法运行：

- `direct`：不训练，不加复杂提示，直接执行任务。
- `prompt`：不训练，加入提示工程、输出格式约束和 few-shot 示例。
- `full`：全参数监督微调。
- `qlora`：QLoRA 参数高效微调。

不同规模模型的方法范围如下：

| 模型规模 | direct | prompt | full | qlora |
|---|---|---|---|---|
| 0.5B 到 3B | 必做 | 必做 | 必做 | 必做 |
| 6B 到 8B | 必做 | 必做 | 不做 | 必做 |
| 13B 到 15B | 必做 | 必做 | 不做 | 必做 |
| 20B 以上 | 必做 | 必做 | 不做 | 必做，排在最后 |

7B 以上模型不做 full fine-tune 的原因必须在论文中说明：在单卡 P6000 pro 条件下，全参数微调显存和时间成本过高，不适合作为统一可复现实验条件；QLoRA 是更合理的低资源可训练方案。

## 实验分层

正式实验分为五层。

| 层级 | 作用 | 模型类型 | 方法 |
|---|---|---|---|
| Level 0 | 最低基准 | majority、random、rule-based | 不训练 |
| Level 1 | 传统代码模型基准 | CodeBERT、GraphCodeBERT、UniXcoder、CodeT5 | full |
| Level 2 | 开源小/中参数代码 LLM | 0.5B、1.3B、1.5B、2B、3B | direct、prompt、full、qlora |
| Level 3 | 开源 6B 到 15B 代码 LLM | 6.7B、7B、8B、13B、14B、15B | direct、prompt、qlora |
| Level 4 | API 闭源强模型上限 | GPT、Claude、Gemini 等 | direct、prompt |

Level 0 到 Level 4 都属于正式实验体系，不再标记为“可选”。其中高成本、超大参数或 API 成本较高的模型排在最后执行。

## 基础基准

基础基准必须实现并记录结果。

- `majority`：始终预测训练集多数类。
- `random`：按训练集类别分布随机预测。
- `rule-based`：使用简单规则或关键词作为弱基线；如果规则不可稳定定义，可只保留 majority 和 random，并在文档中说明。

基础基准不参与训练耗时对比，只作为最低性能参照。

## 传统代码模型基准

以下模型为必做基准，延续旧论文实验方案，并作为传统代码预训练模型对照组。

| 模型 | 方法 |
|---|---|
| `microsoft/codebert-base` | full |
| `microsoft/graphcodebert-base` | full |
| `microsoft/unixcoder-base` | full |
| `Salesforce/codet5-base` | full |

如果统一程序暂时无法直接支持某一模型结构，应先补适配层，再运行；不能因为当前脚本未适配就从方案中删除。

## 开源代码大模型矩阵

以下模型全部纳入正式实验。高成本模型排在后面执行，但不标记为可选。

| 系列 | 模型 | 方法 |
|---|---|---|
| Qwen2.5-Coder | `Qwen/Qwen2.5-Coder-0.5B-Instruct` | direct、prompt、full、qlora |
| Qwen2.5-Coder | `Qwen/Qwen2.5-Coder-1.5B-Instruct` | direct、prompt、full、qlora |
| Qwen2.5-Coder | `Qwen/Qwen2.5-Coder-3B-Instruct` | direct、prompt、full、qlora |
| Qwen2.5-Coder | `Qwen/Qwen2.5-Coder-7B-Instruct` | direct、prompt、qlora |
| Qwen2.5-Coder | `Qwen/Qwen2.5-Coder-14B-Instruct` | direct、prompt、qlora |
| Qwen2.5-Coder | `Qwen/Qwen2.5-Coder-32B-Instruct` | direct、prompt、qlora，最后执行 |
| DeepSeek-Coder | `deepseek-ai/deepseek-coder-1.3b-base` | direct、prompt、full、qlora |
| DeepSeek-Coder | `deepseek-ai/deepseek-coder-6.7b-base` | direct、prompt、qlora |
| DeepSeek-Coder | `deepseek-ai/deepseek-coder-33b-base` | direct、prompt、qlora，最后执行 |
| StarCoder2 | `bigcode/starcoder2-3b` | direct、prompt、full、qlora |
| StarCoder2 | `bigcode/starcoder2-7b` | direct、prompt、qlora |
| StarCoder2 | `bigcode/starcoder2-15b` | direct、prompt、qlora |
| CodeGemma | `google/codegemma-2b` | direct、prompt、full、qlora |
| CodeGemma | `google/codegemma-7b` | direct、prompt、qlora |
| Granite Code | `ibm-granite/granite-3b-code-base` | direct、prompt、full、qlora |
| Granite Code | `ibm-granite/granite-8b-code-base` | direct、prompt、qlora |
| Granite Code | `ibm-granite/granite-20b-code-base` | direct、prompt、qlora，最后执行 |
| CodeLlama | `codellama/CodeLlama-7b-hf` | direct、prompt、qlora |
| CodeLlama | `codellama/CodeLlama-13b-hf` | direct、prompt、qlora |
| CodeLlama | `codellama/CodeLlama-34b-hf` | direct、prompt、qlora，最后执行 |
| WizardCoder | `vanillaOVO/WizardCoder-Python-7B-V1.0` | direct、prompt、qlora |

如某模型下载受限、许可不允许、模型文件损坏、显存不足或代码适配失败，应记录为 `blocked`，写明具体原因、时间、错误日志路径和是否需要后续补跑。不能静默跳过。

## API 强模型基准

API 模型作为闭源强模型上限基准，必须纳入正式实验。API 模型不进行本地训练，只运行 `direct` 和 `prompt`。

| 厂商 | 模型 | 方法 |
|---|---|---|
| OpenAI | `gpt-5.1` | direct、prompt |
| OpenAI | `gpt-4.1` | direct、prompt |
| OpenAI | `gpt-4.1-mini` | direct、prompt |
| Anthropic | `claude-opus-4-1-20250805` | direct、prompt |
| Anthropic | `claude-sonnet-4-20250514` | direct、prompt |
| Google | `gemini-2.5-pro` | direct、prompt |
| Google | `gemini-2.5-flash` | direct、prompt |

API 基准优先跑完整 test set。如果成本过高，可以先跑分层抽样 test subset，但必须单独标记为 `api_subset`，不能与完整 test set 的本地模型结果混在同一张主表中。

API 结果必须额外记录：

- 请求模型名和版本。
- prompt 模板版本。
- 输入 token、输出 token、总费用估算。
- 单样本平均耗时和总耗时。
- 是否完整 test set 或 subset。
- 失败请求数量和重试次数。

## 两台 P6000 pro 机器分工

两台机器按模型维度拆分，不按同一模型的任务维度拆分。这样可以避免结果目录冲突，便于断点续跑和最终汇总。

### 机器 A：Qwen 主线与 API 控制

机器 A 负责 Qwen 系列纵向对比，并可负责 API baseline 脚本调度。

执行顺序：

1. `Qwen/Qwen2.5-Coder-0.5B-Instruct`，已作为主实验完成。
2. `Qwen/Qwen2.5-Coder-1.5B-Instruct`，当前正在运行，跑完后暂停。
3. `Qwen/Qwen2.5-Coder-3B-Instruct`。
4. `Qwen/Qwen2.5-Coder-7B-Instruct`。
5. `Qwen/Qwen2.5-Coder-14B-Instruct`。
6. `Qwen/Qwen2.5-Coder-32B-Instruct`，最后执行。
7. API baseline，优先在 GPU 空闲或本地环境执行。

机器 A 的主要论文价值是 Qwen 系列纵向分析：`0.5B -> 1.5B -> 3B -> 7B -> 14B -> 32B`。

### 机器 B：传统基准与非 Qwen 对照组

机器 B 负责传统基准和其他开源代码模型。

执行顺序：

1. `microsoft/codebert-base`。
2. `microsoft/graphcodebert-base`。
3. `microsoft/unixcoder-base`。
4. `Salesforce/codet5-base`。
5. `deepseek-ai/deepseek-coder-1.3b-base`。
6. `deepseek-ai/deepseek-coder-6.7b-base`。
7. `bigcode/starcoder2-3b`。
8. `bigcode/starcoder2-7b`。
9. `google/codegemma-2b`。
10. `google/codegemma-7b`。
11. `ibm-granite/granite-3b-code-base`。
12. `ibm-granite/granite-8b-code-base`。
13. `codellama/CodeLlama-7b-hf`。
14. `codellama/CodeLlama-13b-hf`。
15. `vanillaOVO/WizardCoder-Python-7B-V1.0`。
16. `bigcode/starcoder2-15b`，后做。
17. `ibm-granite/granite-20b-code-base`，后做。
18. `deepseek-ai/deepseek-coder-33b-base`，后做。
19. `codellama/CodeLlama-34b-hf`，后做。

机器 B 的主要论文价值是横向分析：相近参数规模下，不同模型系列的效果、成本和稳定性差异。

## 主实验与正式实验区别

主实验：

- 当前主实验为 `matrix_balanced721_qwen05_e1`。
- 使用 `Qwen/Qwen2.5-Coder-0.5B-Instruct` 跑完整流程。
- 目标是验证数据集、任务定义、评估指标、断点续跑、结果保存、运行时间记录和多漏洞样本记录是否可靠。
- 主实验结果可以进入论文作为 Qwen 0.5B 数据点，但其主要职责是流程验证。

正式实验：

- 正式实验以 `formal_balanced721_*` 为 run prefix。
- 覆盖本文档定义的全部基准、开源模型和 API 模型。
- 正式实验结果是论文主结果表、横向对比、纵向对比和消融分析的主要来源。

## 当前执行状态

截至本文档创建时：

- 主实验 `matrix_balanced721_qwen05_e1` 已完成 12/12。
- 正式实验 `formal_balanced721_qwen25coder15b_e1` 正在运行。
- 已人为暂停正式队列父进程，保留当前模型子进程继续运行。
- 当前 `Qwen/Qwen2.5-Coder-1.5B-Instruct` 跑完后，不应自动进入下一个模型。
- 后续应先根据本文档重写两台机器队列，再继续执行。

## 暂停与恢复规则

当前模型跑完后必须暂停，先汇报以下内容：

- 当前模型 12 个任务是否全部完成。
- 每个任务和方法的核心指标。
- runtime 是否完整写入。
- predictions 和 multi-label predictions 是否存在。
- 是否有失败、重试、跳过或 blocked 项。
- 数据盘剩余空间是否足够继续下一组实验。

恢复实验前必须确认：

- 两台机器的代码版本一致。
- 两台机器的数据集版本一致。
- 两台机器的依赖、CUDA、PyTorch 和 Transformers 版本一致。
- 两台机器的输出目录和 run prefix 不冲突。
- 当前文档中的模型矩阵已同步到执行脚本。

## 结果合并规则

每个 run prefix 必须至少保留：

- `matrix_summary.csv`
- `matrix_summary_with_runtime.csv`
- `matrix_summary_with_runtime.json`
- 每个任务的 `predictions*.jsonl`
- 每个任务的 `state.json`
- 训练日志和驱动日志

最终合并时按以下维度建主表：

- model_family
- model_name
- parameter_scale
- task
- method
- train_mode
- test_set
- metric_main
- accuracy
- precision
- recall
- f1
- strict_f1
- tolerant_f1
- contract_hit
- candidate_recall
- multi_label_hit_accuracy
- runtime_minutes
- gpu_type
- blocked_reason

## 论文分析口径

论文中至少应形成以下分析：

- 传统代码模型与开源 LLM 的比较。
- direct、prompt、full、QLoRA 方法比较。
- 小参数模型与 7B 以上模型比较。
- 同系列纵向参数规模比较。
- 不同系列相近参数横向比较。
- 多漏洞样本单独分析。
- 漏洞行定位任务单独分析。
- API 强模型上限与本地开源模型比较。
- 性能、训练成本、推理耗时、部署可行性的综合讨论。
