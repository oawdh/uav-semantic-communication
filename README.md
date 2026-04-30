# 无人机语义通信组

本项目面向“语义驱动的具身智能无人机交互系统”。我们希望把语义通信、无人机控制、MCP 工具协议、视觉语言模型和安全验证放到同一个可实验的框架里：学生一边读综述和开源项目，一边把知识沉淀成可检索的知识库，再把关键想法落实成小实验。

## 项目一句话

让无人机理解“我要做什么”，而不只是接收“每个字节是否正确”。

传统链路更关注语音识别文本是否正确、控制指令是否完整传输；本项目更关注用户真实意图是否被可靠恢复、是否能映射到安全的无人机动作、是否能在噪声和低带宽条件下保持任务成功率。

## 你会学到什么

- 语义通信：Shannon 比特传输范式与 Weaver 语义传递范式的差异。
- 无人机系统：传感器、决策中心、动作器、闭环控制与安全约束。
- LLM 知识库：使用 Karpathy 风格的 LLM Wiki，把论文、文档、代码项目编译成可增长的知识网络。
- MCP 工具协议：把无人机状态和动作封装为 LLM 可调用的 Resources 和 Tools。
- 具身对齐：把语音中的“那边、红色目标、灭火器”等语义与视觉目标、空间位置和安全边界对齐。
- 实验验证：用可量化指标比较传统指令链路与语义链路的鲁棒性。

## 仓库结构

```text
.
├── README.md
├── CLAUDE.md                  # LLM Wiki 的项目 schema，Agent 每次工作先读它
├── raw/                       # 原始资料：论文、项目说明、外部资源引用
├── wiki/                      # LLM 编译出的交叉链接知识库
├── audit/                     # 人工反馈与纠错入口
├── log/                       # 每次 ingest/compile/lint 的操作日志
├── docs/                      # 项目目标、Git 指南、知识库流程
├── experiments/               # 分阶段实验
├── src/semantic_drone/        # 后续沉淀可复用代码
├── configs/                   # 实验配置
├── data/                      # 数据目录，不直接提交大文件
├── notebooks/                 # 探索性分析
├── scripts/                   # 文档抽取、wiki lint、audit 工具
└── tests/                     # 后续单元测试与集成测试
```

## 我们的工作方式

这个项目有两条主线。

第一条是知识库主线：把综述、开源项目、课堂讨论和实验结论放进 `raw/`，由 LLM 编译成 `wiki/` 页面。不要把学习停留在“我看过了”，而要沉淀为一个能被下一位同学继续使用的知识节点。

第二条是实验主线：把每一个问题变成可复现实验。实验先放在 `experiments/`，稳定后再把通用模块抽到 `src/semantic_drone/`。

推荐节奏：

1. 先读 [wiki/index.md](wiki/index.md)，了解已有知识图谱。
2. 在 [docs/project-goals.md](docs/project-goals.md) 选择一个阶段目标。
3. 阅读对应 `raw/` 来源和 `wiki/` 概念页。
4. 在 `experiments/<编号>_<主题>/` 做一个最小实验。
5. 把实验结论写回 `wiki/` 或 `outputs/queries/`。
6. 用 Git 分支提交 Pull Request。

## 第一阶段建议目标

先不要一上来追求“完整无人机智能体”。第一阶段只做四个小闭环：

- `M1`：用 DJITelloPy 或模拟器完成起飞、降落、前进、转向、拍照的基础控制。
- `M2`：把一句中文/英文语音或文本解析为结构化意图 JSON。
- `M3`：把结构化意图映射到 MCP Tool 调用，例如 `move_to`、`capture_image`、`return_home`。
- `M4`：设计一个抗噪声实验，对比“文本命令链路”和“语义意图链路”的成功率、延迟和交互轮次。

更完整的里程碑在 [docs/project-goals.md](docs/project-goals.md)。

## Git 最小指令集

第一次参与：

```bash
git clone <仓库地址>
cd <仓库目录>
git status
```

每天开始前：

```bash
git switch main
git pull
git switch -c feature/你的任务名
```

完成一个小任务后：

```bash
git status
git add README.md docs/project-goals.md
git commit -m "docs: add project goals"
git push -u origin feature/你的任务名
```

然后在 GitHub 上发 Pull Request。不要直接往 `main` 分支提交。

常用查看命令：

```bash
git log --oneline --max-count=5
git diff
git diff --staged
git branch
```

## 知识库操作

本项目已经安装并使用 `llm-wiki` skill 的结构。常用命令：

```bash
# 首次处理 PDF / Word 资料前安装抽取依赖
python3 -m pip install -r requirements-dev.txt

# 把本项目的 PDF / Word 资料抽成 raw/ markdown
python3 scripts/extract_sources.py

# 检查 wiki 链接、孤立页面、索引遗漏
python3 scripts/lint_wiki.py .

# 查看人工反馈
python3 scripts/audit_review.py . --open
```

写知识库时遵守三点：

- `raw/` 只放来源材料，不随意改写事实。
- `wiki/` 放编译后的概念页、实体页、摘要页。
- 任何公式使用 KaTeX，任何流程图使用 Mermaid。

## 当前资料

- `raw/papers/uav-semantic-security-review.md`：无人机语义安全综述。
- `raw/notes/stitp-proposal.md`：STITP 申报书。
- `raw/notes/student-technical-guide.md`：学生技术执行指南。
- `raw/notes/code-projects-and-learning-resources.md`：参考代码项目与学习资源。
- `raw/articles/drone-mcp.md`：`drone-mcp` GitHub 项目的初步来源说明。

## 给学生的建议

这个项目最有趣的地方，不是“让大模型控制无人机”这个表面结果，而是把一句模糊的人类意图变成可解释、可验证、可恢复的物理动作。每次做实验都问三个问题：意图有没有被理解，动作有没有被安全执行，失败时系统有没有办法解释并恢复。
