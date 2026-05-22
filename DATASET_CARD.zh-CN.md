# 数据集卡片：面向 Solidity 与以太坊安全研究的智能合约漏洞数据集

## 数据集简介

本数据集支持 Solidity 与以太坊智能合约的漏洞存在性判断、漏洞类型分类和漏洞行定位，可用于区块链安全研究、Web3 安全分析、静态分析工具比较和大语言模型代码安全评测。

## 搜索关键词

智能合约漏洞数据集、Solidity 安全数据集、以太坊智能合约漏洞检测、重入漏洞数据集、智能合约漏洞定位、漏洞行定位、漏洞类型分类、区块链安全数据集、Web3 安全数据集、大语言模型代码安全评测。

## 支持任务

- 二分类漏洞存在性判断：`has_vul`
- 多标签漏洞类型分类：`vul_type`
- 多行漏洞定位：`vul_line`

## 标签空间

- `access_control`
- `arithmetic`
- `bad_randomness`
- `denial_service`
- `front_running`
- `reentrancy`
- `time_manipulation`
- `unchecked_low_calls`

## 数据规模

| 阶段 | `has_vul` | `vul_type` | `vul_line` |
|---|---:|---:|---:|
| 合并数据 | 105,278 | 95,573 | 24,178 |
| 推荐 processed 划分 | 24,441 | 24,394 | 12,491 |

## 来源覆盖

数据集整合 8 个公开来源，覆盖人工整理基准、注入式漏洞基准、审计来源标签、静态分析弱标签、漏洞发现库和源码恢复参考。

## 适用场景

- 智能合约漏洞检测研究。
- Solidity 与以太坊安全基准评测。
- 大语言模型代码安全能力评测。
- 漏洞类型分类。
- 漏洞行定位。
- 区块链安全数据治理研究。

## 不适用场景

- 未核查上游许可证时直接商业化再分发源码。
- 将静态分析弱标签直接视为人工验证真值。
- 将漏洞行定位任务简化为单个数值回归。

## 许可证和再分发

本仓库不再分发原始上游数据。详见 [metadata/upstream_license_review.zh-CN.md](metadata/upstream_license_review.zh-CN.md) 和 [THIRD_PARTY_NOTICES.zh-CN.md](THIRD_PARTY_NOTICES.zh-CN.md)。

