---
title: summaries/student-technical-guide
type: summary
source_type: note
created: 2026-05-01
updated: 2026-05-01
sources: [student-technical-guide]
tags: [student-guide, semantic-communication, mcp]
---

# 学生技术执行指南

**Source**: `raw/notes/student-technical-guide.md`

## Key takeaways

- 项目希望从 Shannon 式“比特无损传输”转向 Weaver 式“语义准确传递”。
- 系统需要一个动态[[语义知识库]]，把静态动作语义和动态环境语义结合起来，用于补全模糊指令。
- 技术模块包括语义提取、[[MCP 语义适配器]]、具身对齐和安全防护。
- 初步指标包括语义增益、端到端延迟、交互轮次和语义熔断。

## Core claims

这份指南把学生任务从“控制无人机”提升为“构建语义闭环”。它给出了本项目最小链路：语音或文本输入经过语义编码，得到任务标签和槽位，再映射为无人机工具调用；执行前后都要由环境语义和安全规则约束。

## Concepts introduced / referenced

- [[无人机语义通信]]
- [[语义知识库]]
- [[MCP 语义适配器]]
- [[实验验证指标]]
