# Git 快速指南

## 基本原则

- `main` 分支保持稳定。
- 每个任务新建一个 `feature/...` 分支。
- 一次提交只解决一个清晰问题。
- 提交信息写清楚“改了什么”，不要写“update”“final”。

## 常用流程

```bash
git switch main
git pull
git switch -c feature/wiki-first-compile
```

修改文件后：

```bash
git status
git diff
git add <文件路径>
git commit -m "docs: compile first wiki pages"
git push -u origin feature/wiki-first-compile
```

在 GitHub 上提交 Pull Request，等待 review 后合并。

## 常见问题

查看自己改了什么：

```bash
git diff
```

查看已经 `git add` 的内容：

```bash
git diff --staged
```

撤销某个文件还没 add 的修改：

```bash
git restore <文件路径>
```

把 main 的最新变化合到自己的分支：

```bash
git switch main
git pull
git switch feature/你的任务名
git merge main
```

## 不要提交的内容

- 大型数据集、模型权重、视频文件。
- `.env`、API Key、Token、个人账号信息。
- 临时生成文件、缓存文件。

大文件只写引用说明，放在 `raw/refs/` 或 `data/README.md` 中说明来源、路径和用途。
