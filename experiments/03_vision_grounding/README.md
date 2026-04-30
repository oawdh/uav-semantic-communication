# Experiment 03: Vision Grounding

目标：把语言中的目标描述与图像目标或空间位置对齐。

候选路线：

- YOLOv8：检测已知类别目标。
- CLIP：做文字和图像区域相似度匹配。
- MobileSAM：对候选目标做轻量分割。

验收：

- 输入一张图像和一句目标描述。
- 输出候选目标、置信度、位置框或 mask。
- 当没有可靠目标时返回 `target_not_found`。
