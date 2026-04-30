---
title: drone-mcp
type: entity
entity_type: tool
created: 2026-05-01
updated: 2026-05-01
sources: [drone-mcp, stitp-proposal]
tags: [mcp, tello, reference]
---

# drone-mcp

`drone-mcp` 是一个参考开源项目，用 MCP server 的形式封装 DJI Tello 无人机控制能力。它在本项目中的角色不是直接替代我们的系统，而是提供一个最小工程参照：如何把无人机动作暴露为 LLM 可调用的工具。

## Key features for this project

- 工具封装：将无人机动作表示为可调用接口。
- 客户端连接：为 LLM/MCP 客户端提供无人机工具入口。
- 工程警示：公开说明中提示实验性质和安全风险，本项目必须加入安全层。

## Related concepts

- [[MCP 语义适配器]] — 参考其封装方式，但加入语义 schema 与安全约束。
- [[SemanticDrone 系统架构]] — `drone-mcp` 只覆盖其中的协议与执行接口的一部分。

## Sources

- [[summaries/drone-mcp]]
- [[summaries/stitp-proposal]]
