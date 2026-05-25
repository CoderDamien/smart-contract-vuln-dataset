# 本地已同步实验结果三线表

数据来源：`results/remote_mirror/**/matrix_summary*.json` 与 `metrics.json`。时间单位为分钟。

## 表1 分类任务结果（has_vul / vul_type）

| 模型 | 任务 | 方法 | Accuracy | F1 | Precision | Recall | Time(min) | 本地机器目录 |
|---|---|---|---:|---:|---:|---:|---:|---|
| CodeBERT-base | has_vul | full | 0.8307 | 0.8247 | 0.8778 | 0.7777 | 9.5 | B_39.105.139.36 |
| CodeBERT-base | vul_type | full | 0.7028 | 0.5714 | 0.7028 | 0.4814 | 15.8 | B_39.105.139.36 |
| CodeLlama-13B | has_vul | direct | 0.5125 | 0.1111 | 0.8372 | 0.0595 | 62.2 | C_autodl_rtxpro6000x8 |
| CodeLlama-13B | has_vul | prompt | 0.5434 | 0.2512 | 0.7835 | 0.1496 | 62.7 | C_autodl_rtxpro6000x8 |
| CodeLlama-13B | has_vul | qlora | 0.7702 | 0.7765 | 0.7736 | 0.7793 | 118.2 | C_autodl_rtxpro6000x8 |
| CodeLlama-13B | vul_type | direct | 0.2169 | 0.1763 | 0.2169 | 0.1486 | 52.7 | C_autodl_rtxpro6000x8 |
| CodeLlama-13B | vul_type | prompt | 0.1903 | 0.1547 | 0.1903 | 0.1303 | 53.5 | C_autodl_rtxpro6000x8 |
| CodeLlama-13B | vul_type | qlora | 0.6320 | 0.5139 | 0.6320 | 0.4329 | 163.5 | C_autodl_rtxpro6000x8 |
| CodeT5-base | has_vul | full | 0.8206 | 0.8226 | 0.8331 | 0.8124 | 20.8 | B_39.105.139.36 |
| CodeT5-base | vul_type | full | 0.6109 | 0.4967 | 0.6109 | 0.4185 | 29.4 | B_39.105.139.36 |
| DeepSeek-Coder-6.7B | has_vul | direct | 0.4964 | 0.0718 | 0.6389 | 0.0380 | 36.7 | C_autodl_rtxpro6000x8 |
| DeepSeek-Coder-6.7B | has_vul | prompt | 0.4994 | 0.1269 | 0.5931 | 0.0711 | 36.9 | C_autodl_rtxpro6000x8 |
| DeepSeek-Coder-6.7B | has_vul | qlora | 0.8256 | 0.8276 | 0.8381 | 0.8174 | 67.7 | C_autodl_rtxpro6000x8 |
| DeepSeek-Coder-6.7B | vul_type | direct | 0.2028 | 0.1649 | 0.2028 | 0.1389 | 31.2 | C_autodl_rtxpro6000x8 |
| DeepSeek-Coder-6.7B | vul_type | prompt | 0.1998 | 0.1624 | 0.1998 | 0.1369 | 31.5 | C_autodl_rtxpro6000x8 |
| DeepSeek-Coder-6.7B | vul_type | qlora | 0.6486 | 0.5273 | 0.6486 | 0.4443 | 94.0 | C_autodl_rtxpro6000x8 |
| Granite-20B-Code | has_vul | direct | 0.5421 | 0.2528 | 0.7689 | 0.1512 | 76.8 | C_autodl_rtxpro6000x8 |
| Granite-20B-Code | has_vul | prompt | 0.5434 | 0.2802 | 0.7266 | 0.1736 | 77.4 | C_autodl_rtxpro6000x8 |
| Granite-20B-Code | has_vul | qlora | 0.7232 | 0.7277 | 0.7332 | 0.7223 | 164.6 | C_autodl_rtxpro6000x8 |
| Granite-20B-Code | vul_type | direct | 0.2339 | 0.1902 | 0.2339 | 0.1602 | 64.8 | C_autodl_rtxpro6000x8 |
| Granite-20B-Code | vul_type | prompt | 0.1983 | 0.1612 | 0.1983 | 0.1358 | 65.6 | C_autodl_rtxpro6000x8 |
| Granite-20B-Code | vul_type | qlora | 0.6476 | 0.5265 | 0.6476 | 0.4436 | 221.4 | C_autodl_rtxpro6000x8 |
| Granite-8B-Code | has_vul | direct | 0.5366 | 0.4013 | 0.5929 | 0.3033 | 40.3 | C_autodl_rtxpro6000x8 |
| Granite-8B-Code | has_vul | prompt | 0.5413 | 0.4265 | 0.5926 | 0.3331 | 41.0 | C_autodl_rtxpro6000x8 |
| Granite-8B-Code | has_vul | qlora | 0.7736 | 0.7762 | 0.7858 | 0.7669 | 88.6 | C_autodl_rtxpro6000x8 |
| Granite-8B-Code | vul_type | direct | 0.2209 | 0.1796 | 0.2209 | 0.1513 | 33.4 | C_autodl_rtxpro6000x8 |
| Granite-8B-Code | vul_type | prompt | 0.2008 | 0.1633 | 0.2008 | 0.1376 | 34.5 | C_autodl_rtxpro6000x8 |
| Granite-8B-Code | vul_type | qlora | 0.6898 | 0.5608 | 0.6898 | 0.4725 | 120.2 | C_autodl_rtxpro6000x8 |
| GraphCodeBERT-base | has_vul | full | 0.8481 | 0.8418 | 0.9018 | 0.7893 | 9.6 | B_39.105.139.36 |
| GraphCodeBERT-base | vul_type | full | 0.6918 | 0.5624 | 0.6918 | 0.4739 | 16.0 | B_39.105.139.36 |
| Qwen2.5-Coder-0.5B | has_vul | direct | 0.4858 | 0.0257 | 0.4324 | 0.0132 | 15.5 | A_8.130.211.198 |
| Qwen2.5-Coder-0.5B | has_vul | prompt | 0.4871 | 0.0350 | 0.4783 | 0.0182 | 16.5 | A_8.130.211.198 |
| Qwen2.5-Coder-0.5B | has_vul | full | 0.8752 | 0.8756 | 0.8941 | 0.8579 | 23.0 | A_8.130.211.198 |
| Qwen2.5-Coder-0.5B | has_vul | qlora | 0.7292 | 0.7375 | 0.7321 | 0.7430 | 23.6 | A_8.130.211.198 |
| Qwen2.5-Coder-0.5B | vul_type | direct | 0.1923 | 0.1563 | 0.1923 | 0.1317 | 14.2 | A_8.130.211.198 |
| Qwen2.5-Coder-0.5B | vul_type | prompt | 0.1998 | 0.1624 | 0.1998 | 0.1369 | 14.8 | A_8.130.211.198 |
| Qwen2.5-Coder-0.5B | vul_type | full | 0.7636 | 0.6208 | 0.7636 | 0.5230 | 33.5 | A_8.130.211.198 |
| Qwen2.5-Coder-0.5B | vul_type | qlora | 0.6009 | 0.4886 | 0.6009 | 0.4116 | 33.8 | A_8.130.211.198 |
| Qwen2.5-Coder-1.5B | has_vul | direct | 0.4956 | 0.0525 | 0.6875 | 0.0273 | 8.1 | A_8.130.211.198 |
| Qwen2.5-Coder-1.5B | has_vul | prompt | 0.4824 | 0.0408 | 0.4000 | 0.0215 | 8.6 | A_8.130.211.198 |
| Qwen2.5-Coder-1.5B | has_vul | full | 0.8752 | 0.8757 | 0.8934 | 0.8587 | 62.5 | A_8.130.211.198 |
| Qwen2.5-Coder-1.5B | has_vul | qlora | 0.7507 | 0.7599 | 0.7498 | 0.7702 | 53.2 | A_8.130.211.198 |
| Qwen2.5-Coder-1.5B | vul_type | direct | 0.2425 | 0.1971 | 0.2425 | 0.1661 | 7.5 | A_8.130.211.198 |
| Qwen2.5-Coder-1.5B | vul_type | prompt | 0.1948 | 0.1584 | 0.1948 | 0.1334 | 8.3 | A_8.130.211.198 |
| Qwen2.5-Coder-1.5B | vul_type | full | 0.7706 | 0.6265 | 0.7706 | 0.5279 | 86.5 | A_8.130.211.198 |
| Qwen2.5-Coder-1.5B | vul_type | qlora | 0.6421 | 0.5220 | 0.6421 | 0.4398 | 74.9 | A_8.130.211.198 |
| Qwen2.5-Coder-14B | has_vul | direct | 0.5404 | 0.2836 | 0.7026 | 0.1777 | 30.4 | C_autodl_rtxpro6000x8 |
| Qwen2.5-Coder-14B | has_vul | prompt | 0.5049 | 0.1795 | 0.5926 | 0.1058 | 30.9 | C_autodl_rtxpro6000x8 |
| Qwen2.5-Coder-14B | has_vul | qlora | 0.7685 | 0.7718 | 0.7793 | 0.7645 | 134.0 | C_autodl_rtxpro6000x8 |
| Qwen2.5-Coder-14B | vul_type | direct | 0.2505 | 0.2037 | 0.2505 | 0.1716 | 26.4 | C_autodl_rtxpro6000x8 |
| Qwen2.5-Coder-14B | vul_type | prompt | 0.2083 | 0.1694 | 0.2083 | 0.1427 | 27.2 | C_autodl_rtxpro6000x8 |
| Qwen2.5-Coder-14B | vul_type | qlora | 0.6637 | 0.5396 | 0.6637 | 0.4546 | 182.5 | C_autodl_rtxpro6000x8 |
| Qwen2.5-Coder-3B | has_vul | direct | 0.5370 | 0.3213 | 0.6443 | 0.2140 | 268.0 | A_8.130.211.198 |
| Qwen2.5-Coder-3B | has_vul | prompt | 0.4846 | 0.1792 | 0.4854 | 0.1099 | 23.8 | A_8.130.211.198 |
| Qwen2.5-Coder-3B | has_vul | qlora | 0.7787 | 0.7871 | 0.7755 | 0.7992 | 95.6 | A_8.130.211.198 |
| Qwen2.5-Coder-3B | vul_type | direct | 0.2299 | 0.1869 | 0.2299 | 0.1575 | 20.1 | A_8.130.211.198 |
| Qwen2.5-Coder-3B | vul_type | prompt | 0.1933 | 0.1571 | 0.1933 | 0.1324 | 22.4 | A_8.130.211.198 |
| Qwen2.5-Coder-3B | vul_type | qlora | 0.6657 | 0.5412 | 0.6657 | 0.4560 | 132.1 | A_8.130.211.198 |
| Qwen2.5-Coder-7B | has_vul | direct | 0.5142 | 0.2264 | 0.6131 | 0.1388 | 22.2 | C_autodl_rtxpro6000x8 |
| Qwen2.5-Coder-7B | has_vul | prompt | 0.4833 | 0.1359 | 0.4729 | 0.0793 | 22.6 | C_autodl_rtxpro6000x8 |
| Qwen2.5-Coder-7B | has_vul | qlora | 0.7520 | 0.7610 | 0.7512 | 0.7711 | 70.2 | C_autodl_rtxpro6000x8 |
| Qwen2.5-Coder-7B | vul_type | direct | 0.2490 | 0.2024 | 0.2490 | 0.1706 | 20.6 | C_autodl_rtxpro6000x8 |
| Qwen2.5-Coder-7B | vul_type | prompt | 0.2139 | 0.1739 | 0.2139 | 0.1465 | 21.3 | C_autodl_rtxpro6000x8 |
| Qwen2.5-Coder-7B | vul_type | qlora | 0.6717 | 0.5461 | 0.6717 | 0.4601 | 96.8 | C_autodl_rtxpro6000x8 |
| StarCoder2-15B | has_vul | direct | 0.5116 | 0.1401 | 0.7121 | 0.0777 | 68.3 | C_autodl_rtxpro6000x8 |
| StarCoder2-15B | has_vul | prompt | 0.5455 | 0.2802 | 0.7411 | 0.1727 | 68.9 | C_autodl_rtxpro6000x8 |
| StarCoder2-15B | has_vul | qlora | 0.7262 | 0.7708 | 0.6745 | 0.8992 | 137.2 | C_autodl_rtxpro6000x8 |
| StarCoder2-15B | vul_type | direct | 0.2450 | 0.1992 | 0.2450 | 0.1678 | 58.0 | C_autodl_rtxpro6000x8 |
| StarCoder2-15B | vul_type | prompt | 0.2068 | 0.1682 | 0.2068 | 0.1417 | 58.8 | C_autodl_rtxpro6000x8 |
| StarCoder2-15B | vul_type | qlora | 0.5919 | 0.4812 | 0.5919 | 0.4054 | 185.7 | C_autodl_rtxpro6000x8 |
| StarCoder2-7B | has_vul | direct | 0.4778 | 0.0666 | 0.3929 | 0.0364 | 35.2 | C_autodl_rtxpro6000x8 |
| StarCoder2-7B | has_vul | prompt | 0.4807 | 0.1011 | 0.4452 | 0.0570 | 35.6 | C_autodl_rtxpro6000x8 |
| StarCoder2-7B | has_vul | qlora | 0.7490 | 0.7573 | 0.7502 | 0.7645 | 70.0 | C_autodl_rtxpro6000x8 |
| StarCoder2-7B | vul_type | direct | 0.2359 | 0.1918 | 0.2359 | 0.1616 | 30.1 | C_autodl_rtxpro6000x8 |
| StarCoder2-7B | vul_type | prompt | 0.1933 | 0.1571 | 0.1933 | 0.1324 | 30.9 | C_autodl_rtxpro6000x8 |
| StarCoder2-7B | vul_type | qlora | 0.5582 | 0.4539 | 0.5582 | 0.3824 | 95.7 | C_autodl_rtxpro6000x8 |
| UniXcoder-base | has_vul | full | 0.8612 | 0.8613 | 0.8821 | 0.8413 | 9.3 | B_39.105.139.36 |
| UniXcoder-base | vul_type | full | 0.7174 | 0.5833 | 0.7174 | 0.4914 | 15.2 | B_39.105.139.36 |

## 表2 漏洞行定位任务结果（vul_line）

| 模型 | 方法 | Strict F1 | Tolerant F1 | Top-k Hit | Time(min) | 本地机器目录 |
|---|---|---:|---:|---:|---:|---|
| CodeBERT-base | full | 0.2662 | 0.3816 | 0.8030 | 69.8 | B_39.105.139.36 |
| DeepSeek-Coder-6.7B | direct | 0.0473 | 0.1136 | 0.2838 | 1120.7 | C_autodl_rtxpro6000x8 |
| Granite-8B-Code | direct | 0.0527 | 0.0837 | 0.2057 | 765.3 | C_autodl_rtxpro6000x8 |
| GraphCodeBERT-base | full | 0.2677 | 0.3792 | 0.8178 | 69.6 | B_39.105.139.36 |
| Qwen2.5-Coder-0.5B | direct | 0.0452 | 0.1077 | 0.2689 | - | A_8.130.211.198 |
| Qwen2.5-Coder-0.5B | prompt | 0.0520 | 0.0894 | 0.2193 | - | A_8.130.211.198 |
| Qwen2.5-Coder-0.5B | full | 0.2926 | 0.3904 | 0.8451 | - | A_8.130.211.198 |
| Qwen2.5-Coder-0.5B | qlora | 0.2547 | 0.3728 | 0.7893 | - | A_8.130.211.198 |
| Qwen2.5-Coder-1.5B | direct | 0.0549 | 0.1374 | 0.3098 | 95.9 | A_8.130.211.198 |
| Qwen2.5-Coder-1.5B | prompt | 0.0632 | 0.1610 | 0.3668 | 93.8 | A_8.130.211.198 |
| Qwen2.5-Coder-1.5B | full | 0.2900 | 0.3948 | 0.8278 | 733.1 | A_8.130.211.198 |
| Qwen2.5-Coder-1.5B | qlora | 0.2565 | 0.3786 | 0.7918 | 536.8 | A_8.130.211.198 |
| Qwen2.5-Coder-14B | direct | 0.0498 | 0.1059 | 0.2739 | 318.5 | C_autodl_rtxpro6000x8 |
| Qwen2.5-Coder-14B | prompt | 0.0484 | 0.1336 | 0.3160 | 367.5 | C_autodl_rtxpro6000x8 |
| Qwen2.5-Coder-3B | direct | 0.0531 | 0.0823 | 0.2045 | 149.6 | A_8.130.211.198 |
| Qwen2.5-Coder-3B | prompt | 0.0477 | 0.1186 | 0.2739 | 190.3 | A_8.130.211.198 |
| Qwen2.5-Coder-3B | qlora | 0.2633 | 0.3866 | 0.8178 | 965.8 | A_8.130.211.198 |
| Qwen2.5-Coder-7B | direct | 0.0589 | 0.1288 | 0.3073 | 161.5 | C_autodl_rtxpro6000x8 |
| Qwen2.5-Coder-7B | prompt | 0.0694 | 0.1738 | 0.4040 | 194.5 | C_autodl_rtxpro6000x8 |
| Qwen2.5-Coder-7B | qlora | 0.2763 | 0.3861 | 0.8141 | 670.3 | C_autodl_rtxpro6000x8 |
| StarCoder2-7B | direct | 0.0419 | 0.0975 | 0.2330 | 1085.6 | C_autodl_rtxpro6000x8 |
| UniXcoder-base | full | 0.2727 | 0.3793 | 0.8092 | 69.2 | B_39.105.139.36 |