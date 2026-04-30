# 无人机语义通信 Knowledge Base

> Schema document — read at the start of every session together with `wiki/index.md`.
> 本知识库采用 Karpathy / llm-wiki 风格：raw 是来源，wiki 是编译后的知识网络。

## Scope

What this wiki covers:
- 无人机语义通信：意图编码、语义传输、语义增益、低信噪比鲁棒性。
- SemanticDrone 系统：语义编码层、MCP 协议适配层、具身执行层。
- 无人机语义安全：安全检测、漏洞修复、运行时防护和 failsafe。
- 学生实验：意图解析、MCP 工具封装、视觉 grounding、鲁棒性评估。
- 项目管理：学生学习路线、Git 协作、实验记录与知识库维护。

What this wiki deliberately excludes:
- 与本项目无关的通用无人机科普。
- 不可复现实飞炫技视频。
- 大型模型训练细节，除非直接服务于意图解析或语义鲁棒性实验。
- 未经验证的外部代码片段和无法追溯来源的结论。

## Operations

This wiki follows the llm-wiki skill's five operations: `compile`, `ingest`, `query`, `lint`, `audit`.
Every operation appends an entry to `log/YYYYMMDD.md`.

## Naming conventions

- **Concept pages** (`wiki/concepts/`): 中文概念名或中英混合名，保持简短，例如 `无人机语义通信.md`。
- **Entity pages** (`wiki/entities/`): 工具、项目、论文、方法名，例如 `drone-mcp.md`。
- **Summary pages** (`wiki/summaries/`): kebab-case source slug，例如 `uav-semantic-security-review.md`。
- **Experiment notes**: 先写入 `outputs/queries/` 或 `raw/notes/`，稳定后再 promote 到 `wiki/concepts/`。

All pages require YAML frontmatter: `title`, `type`, `created`, `updated`, `sources`, `tags`.

### Diagrams and formulas

- All diagrams are **mermaid**. No ASCII art.
- All formulas are **KaTeX** (inline `$...$` or block `$$...$$`).

### Raw file policy

- Small text/PDF/docx sources may be extracted into `raw/`.
- Large binaries, datasets, videos, model weights, flight logs → do not commit; create a pointer file at `raw/refs/<slug>.md`.

## Current articles

### Concepts

- [[无人机语义通信]] — 以意图恢复和安全执行为核心的无人机通信视角。
- [[SemanticDrone 系统架构]] — 三层架构和四个实验闭环。
- [[语义知识库]] — 研究知识库与运行时场景语义图谱。
- [[MCP 语义适配器]] — 意图 JSON 到无人机工具调用的协议层。
- [[无人机语义安全]] — 行为语义、检测、修复、运行时防护。
- [[实验验证指标]] — 成功率、延迟、交互轮次、安全拒绝等指标。
- [[学生学习路线]] — 从知识库阅读到最小实验再到 PR 的路线。

### Entities

- [[entities/drone-mcp|drone-mcp]] — MCP server 形式的 DJI Tello 参考项目。
- [[entities/LLM Wiki|LLM Wiki]] — 本项目采用的知识库编译方法。

### Summaries

- [[summaries/uav-semantic-security-review]] — 无人机语义安全综述。
- [[summaries/student-technical-guide]] — 学生技术执行指南。
- [[summaries/stitp-proposal]] — STITP 申报书。
- [[summaries/code-projects-and-learning-resources]] — 参考代码项目与学习资源。
- [[summaries/drone-mcp]] — drone-mcp GitHub 项目初步摘要。

## Open research questions

- 语义通信实验中，应该传输语义向量、结构化意图 JSON，还是二者结合？
- 语义相似度如何与无人机动作成功率建立可解释对应关系？
- MCP 工具调用前的 safety gate 应包含哪些硬规则与软规则？
- 模糊指令中目标不存在或多目标冲突时，如何设计反问策略？
- 运行时语义知识库先用 JSON、SQLite 还是图结构？
- 如何在不实飞或低风险实飞条件下验证语义安全防护？

## Research gaps

Sources to ingest:
- [ ] MCP 官方文档 — 统一 Resources、Tools、客户端交互方式。
- [ ] DJITelloPy 文档 — 建立 Tello 基础控制实验。
- [ ] Faster-Whisper 或 Whisper 部署文档 — 支持语音到意图实验。
- [ ] CLIP / YOLO / MobileSAM 参考资料 — 支持视觉 grounding。
- [ ] Deep JSCC / semantic communication 代表论文 — 为语义链路设计提供理论支撑。

## Audit backlog

*(none — run `python3 scripts/audit_review.py . --open` to refresh)*

## Notes for the LLM

- Language: zh first; technical terms can be bilingual.
- Tone: academic but student-friendly.
- Depth: start with survey-level maps, promote to deep technical pages after experiments.
- Handling contradictions: state both, cite each source summary, add to Open Research Questions.
- Do not invent experiment results. If a metric is not measured yet, write `待测`.
