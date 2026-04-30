# LLM Wiki 工作流

## 为什么要用知识库

这个项目的学习材料会不断增加：综述、GitHub 项目、实验记录、课堂讨论、失败案例。如果每次都重新问 LLM，知识不会积累。LLM Wiki 的做法是把原始资料编译成持久的、交叉链接的 Markdown 页面，让知识越用越清楚。

## 五种操作

- `ingest`：把新资料放入 `raw/`，并创建摘要页。
- `compile`：把已有资料整理成概念页、实体页和索引。
- `query`：基于已有 wiki 回答问题，不够就指出缺口。
- `lint`：检查死链、孤立页、索引遗漏。
- `audit`：处理人工反馈和纠错。

## 学生提交知识的格式

新增资料：

```text
raw/papers/<paper-slug>.md
raw/articles/<project-or-article-slug>.md
raw/notes/<meeting-or-experiment-note>.md
```

新增编译页：

```text
wiki/summaries/<source-slug>.md
wiki/concepts/<concept-title>.md
wiki/entities/<entity-name>.md
```

每个 wiki 页面至少包含：

- 它回答什么问题。
- 它和哪些页面相关。
- 它来自哪些 raw 来源。
- 它还不知道什么。

## 检查

```bash
python3 scripts/lint_wiki.py .
```

如果出现死链，优先修复链接或补页面；如果出现孤立页，把它加到 `wiki/index.md` 或相关概念页。
