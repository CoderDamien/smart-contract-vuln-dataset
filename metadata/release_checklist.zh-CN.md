# 发布检查清单

## 公开发布前必须完成

- [x] 仓库名：`smart-contract-vuln-dataset`。
- [ ] 确认最终 GitHub owner 和 URL。
- [x] 原始 raw 数据不公开。
- [x] 完成上游来源许可证初步核查。
- [ ] 补充每个来源的访问日期、引用格式和许可证说明。
- [x] 仓库自有代码和文档建议使用 MIT。
- [x] 自建元数据和标注建议使用 CC BY 4.0，前提是与上游条款兼容。
- [ ] 添加最终 `LICENSE`、`DATA_LICENSE.md` 和第三方 notice。
- [ ] 更新 `CITATION.cff` 中的最终仓库 URL、论文 DOI 或正式题名。
- [ ] 根据最终发布文件重新生成 `metadata/dataset_statistics.json`。
- [ ] 检查不包含私有服务器路径、token、本地用户名或未公开论文内部说明。
- [ ] 检查 processed split 中不存在重复样本跨 split 泄漏。
- [ ] 检查行号标签均在有效范围内。
- [ ] 检查 README 统计与最终发布文件一致。
- [ ] 为当前发布版本创建 GitHub tag。

## 建议完成

- [ ] 增加与已有智能合约漏洞数据集的规模对比表。
- [ ] 增加小规模示例数据。
- [ ] 增加 schema 校验脚本。
- [ ] 增加统计生成脚本。
- [ ] 增加模型无关 baseline 示例。
- [ ] 在 Zenodo 归档获得 DOI。
