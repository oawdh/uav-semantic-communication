# Experiment 01: Intent Parsing Baseline

目标：把自然语言指令解析为结构化意图 JSON。

输入示例：

```text
飞到红色目标附近，保持两米距离并拍照
```

输出草案：

```json
{
  "action": "approach_and_capture",
  "target": "red object",
  "distance_m": 2,
  "safety_constraint": "keep_distance",
  "confidence": 0.0
}
```

验收：

- 至少 20 条指令样例。
- 给出人工标注结果和模型解析结果。
- 记录错误类型：动作错、目标错、距离错、安全约束丢失、应反问但未反问。
