# Experiment 02: MCP Tello Control

目标：把无人机基础动作封装成可由 LLM/MCP 调用的工具。

建议先在模拟器或无桨安全环境中验证，再连接真实无人机。

最小工具集：

- `takeoff`
- `land`
- `move`
- `rotate`
- `capture_image`
- `emergency_stop`

验收：

- 每个工具有输入 schema、输出 schema 和失败返回。
- 危险动作前检查电量、连接状态和安全约束。
- 记录一次完整 demo 的日志。
