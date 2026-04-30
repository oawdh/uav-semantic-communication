---
title: drone-mcp
source_url: https://github.com/0xKoda/drone-mcp
source_type: github
ingested: 2026-05-01
---

# drone-mcp

`drone-mcp` 是本项目申报书中提到的直接参考项目。它展示了如何把 DJI Tello 无人机封装为 MCP server，使 LLM 客户端可以通过工具调用触发无人机动作。

初步观察：

- 项目定位是一个 MCP server，而不是完整的自主无人机系统。
- 主要价值在于“协议封装方式”：将起飞、降落、移动、旋转、翻转、相机/视频流等能力暴露给 LLM 客户端。
- README 明确提示该项目偏实验性质，默认无鉴权、无 CORS 限制，并涉及 root/sudo 运行风险。因此本项目不能直接照搬为实飞系统，必须增加鉴权、安全约束、危险动作确认和 failsafe。
- 它适合作为 `MCP 语义适配器` 的最小参考：先学会如何把无人机动作变成工具，再进一步加入语义意图、置信度、环境状态和安全策略。

本项目的使用方式：

1. 先复现最小工具封装，而不是急着实飞。
2. 将工具输入输出改造成结构化 schema。
3. 在每个工具前加入安全检查，如电量、连接状态、空间边界、置信度。
4. 将“自然语言 -> 意图 JSON -> MCP Tool”的链路与 `drone-mcp` 的工具封装方式连接起来。
