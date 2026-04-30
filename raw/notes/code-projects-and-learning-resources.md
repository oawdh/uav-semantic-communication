---
title: 参考代码项目与学习资源推荐
source_file: 参考代码项目与学习资源推荐.docx
source_type: docx
ingested: 2026-05-01
---

# 参考代码项目与学习资源推荐

推荐参考代码项目与学习资源清单

为了帮助学生快速进入开发状态，建议参考以下开源项目及文档：

1. 无人机控制基础 (Drone Control)

DJITelloPy：目前最稳定的 DJI Tello Python 接口库，文档齐全，适合学生快速实现起降和图像获取。

drone-mcp：本项目最直接的灵感来源，展示了如何用 MCP 协议封装无人机控制逻辑。

2. MCP 协议与模型交互 (MCP & LLM)

Model Context Protocol SDK：官方 SDK（提供 Python 和 TypeScript 版本），这是理解 MCP 服务端与客户端交互的必读代码。

MCP Servers Examples：包含了各种工具集（如 Google Search, Filesystem）的封装，学生可以模仿其结构来封装“无人机工具”。

3. 语义通信与语音处理 (SemCom & Audio)

Faster-Whisper：OpenAI Whisper 的重新实现，速度极快，适合边缘设备（如 Jetson Nano）上的实时语音转意图。

Semantic-Communication-Demo：在 GitHub 上搜索该主题，重点关注基于 Transformer 的联合源信道编码（JSCC）开源实现。

4. 具身智能与视觉对齐 (VLM & Grounding)

MobileSAM：轻量级的“全能分割模型”，适合在边缘侧实时分割出用户口中的“目标物体”。

CLIP (OpenAI)：用于实现“文字-图像”匹配的核心算法，是解决“飞向那棵树”这种指令的关键。

5. 建议学习路径

第一周：通过 djitellopy 实现按键控制无人机飞行。

第二周：阅读 MCP 官方文档，跑通一个简单的 weather-mcp-server 示例。

第三周：尝试将语音输入（使用麦克风）转化为文本，并映射到 MCP 工具调用。

第四周：集成 YOLOv8 或 CLIP，尝试实现“看到目标才执行”的逻辑约束。
