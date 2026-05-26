#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="${PROJECT_ROOT:-$(pwd)}"
PYTHON_BIN="${PYTHON_BIN:-python}"
cd "${PROJECT_ROOT}"

if [[ -f "${PROJECT_ROOT}/.env" ]]; then
  # Optional local environment file for reproducing the queue on another machine.
  # The released script does not depend on a private server path.
  source "${PROJECT_ROOT}/.env"
fi

OUTPUT_ROOT="${OUTPUT_ROOT:-${PROJECT_ROOT}/artifacts/runs}"
DATA_ROOT="${DATA_ROOT:-${PROJECT_ROOT}/data/processed/balanced_stage1_resplit_721}"
DRIVER_LOG_DIR="${DRIVER_LOG_DIR:-${PROJECT_ROOT}/artifacts/driver_logs}"
mkdir -p "${DRIVER_LOG_DIR}"

wait_for_current_run() {
  echo "CHECK existing matrix_balanced721_qwen05_e1 $(date)"
  while pgrep -f -- "--run-prefix matrix_balanced721_qwen05_e1" >/dev/null 2>&1; do
    local active
    active="$(pgrep -f -- "--run-prefix matrix_balanced721_qwen05_e1" | tr '\n' ' ')"
    echo "WAIT existing matrix_balanced721_qwen05_e1 active_pids=${active} $(date)"
    sleep 300
  done
  echo "DONE existing matrix_balanced721_qwen05_e1 $(date)"
  if [[ -d "${OUTPUT_ROOT}/matrix_balanced721_qwen05_e1" ]]; then
    "${PYTHON_BIN}" scripts/runtime/enrich_matrix_runtime.py \
      --summary-dir "${OUTPUT_ROOT}/matrix_balanced721_qwen05_e1" \
      --output-root "${OUTPUT_ROOT}" || true
  fi
}

run_matrix() {
  local model="$1"
  local run_prefix="$2"
  local methods="$3"

  echo "START ${run_prefix} model=${model} methods=${methods} $(date)"
  "${PYTHON_BIN}" -m src.matrix \
    --tasks has_vul vul_type vul_line \
    --methods ${methods} \
    --model "${model}" \
    --dataset-has-vul "${DATA_ROOT}/has_vul_721_stratified_v1" \
    --dataset-vul-type "${DATA_ROOT}/vul_type_721_stratified_v1" \
    --dataset-vul-line "${DATA_ROOT}/vul_line_721_stratified_v1" \
    --output-root "${OUTPUT_ROOT}" \
    --run-prefix "${run_prefix}" \
    --max-length 512 \
    --batch-size 4 \
    --eval-batch-size 16 \
    --gradient-accumulation-steps 2 \
    --num-train-epochs 1 \
    --learning-rate 1e-5 \
    --lora-r 16 \
    --lora-alpha 32 \
    --lora-dropout 0.05 \
    --fewshot-k 2 \
    --generation-max-new-tokens 64 \
    --vul-line-strategy line_rank \
    --vul-line-max-eval-candidates 120 \
    --vul-line-prediction-top-k 3 \
    --bf16 \
    --resume

  "${PYTHON_BIN}" scripts/runtime/enrich_matrix_runtime.py \
    --summary-dir "${OUTPUT_ROOT}/${run_prefix}" \
    --output-root "${OUTPUT_ROOT}" || true
  echo "END ${run_prefix} $(date)"
}

wait_for_current_run

run_matrix "Qwen/Qwen2.5-Coder-1.5B-Instruct" "formal_balanced721_qwen25coder15b_e1" "direct prompt full qlora"
run_matrix "deepseek-ai/deepseek-coder-1.3b-base" "formal_balanced721_deepseekcoder13b_e1" "direct prompt full qlora"

# 7B-class models are evaluated without full fine-tuning on this P6000 pro server.
# Direct/prompt give zero/few-shot baselines; QLoRA gives the trainable low-memory comparison.
run_matrix "Qwen/Qwen2.5-Coder-7B-Instruct" "formal_balanced721_qwen25coder7b_e1" "direct prompt qlora"
run_matrix "deepseek-ai/deepseek-coder-6.7b-base" "formal_balanced721_deepseekcoder67b_e1" "direct prompt qlora"
run_matrix "bigcode/starcoder2-7b" "formal_balanced721_starcoder2_7b_e1" "direct prompt qlora"

echo "FORMAL QUEUE COMPLETE $(date)"
