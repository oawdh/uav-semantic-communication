# Index — 无人机语义通信

> 面向 SemanticDrone 项目的语义通信、无人机语义安全、MCP 工具封装与实验验证知识库。

## Navigation

- [[#Concepts]] · [[#Entities]] · [[#Summaries]] · [[#Open Questions]]

## Concepts

### 语义通信与系统架构

- [[无人机语义通信]] — 以意图恢复和安全执行为核心的通信视角。
- [[SemanticDrone 系统架构]] — 语义编码层、协议适配层、具身执行层及实验闭环。
- [[语义知识库]] — 研究知识库与运行时场景语义图谱。

### 协议、执行与安全

- [[MCP 语义适配器]] — 将意图 JSON 映射为 MCP 工具调用，并执行 safety gate。
- [[无人机语义安全]] — 行为语义是否符合预期与安全边界。
- [[实验验证指标]] — 成功率、延迟、交互轮次、安全拒绝率与传输负载。

### 学生协作

- [[学生学习路线]] — 学习、实验、写回 wiki、提交 PR 的循环。

## Entities

- [[entities/drone-mcp|drone-mcp]] — 参考开源项目，展示如何用 MCP server 封装 DJI Tello 控制。
- [[entities/LLM Wiki|LLM Wiki]] — 本项目使用的 LLM 驱动知识库构建方法。

## Summaries (chronological)

- 2026-05-01 — [[summaries/uav-semantic-security-review]] — 无人机语义安全综述。
- 2026-05-01 — [[summaries/student-technical-guide]] — 学生技术执行指南。
- 2026-05-01 — [[summaries/stitp-proposal]] — STITP 申报书。
- 2026-05-01 — [[summaries/code-projects-and-learning-resources]] — 参考代码项目与学习资源。
- 2026-05-01 — [[summaries/drone-mcp]] — drone-mcp GitHub 项目初步摘要。

## Open Questions

- Q1: 语义通信链路的最小可验证形态是什么：语义向量、意图 JSON，还是二者结合？
- Q2: 语义安全中的“预期行为”如何转化为学生可执行的测试用例？
- Q3: MCP 工具调用前的 safety gate 应如何设计，才能既安全又不过度保守？
- Q4: 视觉 grounding 中目标不存在、多目标冲突、低置信度时如何反问？
- Q5: 如何证明语义链路相对传统 ASR 命令链路有明确实验优势？
