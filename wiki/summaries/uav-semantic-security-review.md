---
title: summaries/uav-semantic-security-review
type: summary
source_type: paper
created: 2026-05-01
updated: 2026-05-01
sources: [uav-semantic-security-review]
tags: [uav, semantic-safety, survey]
---

# 无人机语义安全研究综述

**Source**: `raw/papers/uav-semantic-security-review.md`

## Key takeaways

- 综述把无人机端系统安全划分为软件安全、传感器安全和[[无人机语义安全]]，其中语义安全关注系统行为是否符合预期语义。
- 无人机语义安全不是单纯“被攻击后出错”，也包括设计缺陷、实现错误、性能局限和特定飞行条件组合导致的预期行为偏离。
- 论文建立了“安全检测、漏洞修复、实时防护”三类研究框架；这可以直接转化为本项目的实验验证与 failsafe 设计。
- 未来方向包括新场景语义安全、AI 语义安全、蜂群语义安全、评估体系和运行时语义强化。

## Core claims

这篇综述为本项目提供了安全视角：语义通信系统不能只证明“指令能被理解”，还要证明“执行行为符合任务语义和安全边界”。对 SemanticDrone 来说，语义目标、异常判断标准、运行时监控与实时恢复都应成为实验设计的一部分。

## Concepts introduced / referenced

- [[无人机语义安全]]
- [[实验验证指标]]
- [[SemanticDrone 系统架构]]
