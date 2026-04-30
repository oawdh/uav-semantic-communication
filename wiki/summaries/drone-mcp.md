---
title: summaries/drone-mcp
type: summary
source_type: github
source_url: https://github.com/0xKoda/drone-mcp
created: 2026-05-01
updated: 2026-05-01
sources: [drone-mcp]
tags: [mcp, drone-control, reference-project]
---

# drone-mcp

**Source**: `raw/articles/drone-mcp.md`

## Key takeaways

- `drone-mcp` 的核心价值是把 DJI Tello 无人机能力封装为 MCP server 工具。
- 它适合作为本项目[[MCP 语义适配器]]的起点，但不是完整的语义通信系统。
- 该项目的公开说明包含明显安全提醒：实验性质、默认无鉴权、无 CORS 限制，并可能涉及高权限运行。
- 本项目需要在它的工具封装思想上增加意图 schema、环境状态、置信度检查和 failsafe。

## Core claims

`drone-mcp` 给出“LLM 调用无人机工具”的工程入口；SemanticDrone 的研究价值在于把工具调用前的语义理解和工具调用后的安全验证补完整。

## Concepts introduced / referenced

- [[MCP 语义适配器]]
- [[SemanticDrone 系统架构]]
- [[entities/drone-mcp|drone-mcp]]
