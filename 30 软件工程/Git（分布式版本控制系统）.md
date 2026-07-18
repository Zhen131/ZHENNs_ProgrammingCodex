---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/软件工程, 工具/Git, 层级/基础, 用途/常见Git指令]
aliases: [Git, 版本控制, 常见 Git 指令, Git 常用命令]
created: 2026-07-18
updated: 2026-07-18
---

# Git（分布式版本控制系统）

## 一句话

`Git（分布式版本控制系统）` 用 Commit（提交）记录文件变化，并用 Branch（分支）指向不同的开发历史。

## 常见指令

- `git status`：查看工作区和暂存区状态；例：`git status`。
- `git add <路径>`：把变化加入 Staging Area（暂存区）；路径有空格时加引号，例如 `git add "notes/Git basics.md"`。
- `git add -u`：暂存已跟踪文件的修改和删除，不包含全新的未跟踪文件；例：`git add -u`。
- `git commit -m "说明"`：把暂存区内容创建为一次 Commit；例：`git commit -m "docs: update Git notes"`。
- `git commit --amend --no-edit`：用当前暂存内容修正最近一次 Commit，并保留原提交说明；这会产生新的 Commit Hash。
- `git branch`：查看本地分支，`*` 表示当前分支；例：`git branch`。
- `git switch <分支>`：切换分支；例：`git switch main`。
- `git merge --ff-only <分支>`：只允许 Fast-Forward（快进）合并，历史已分叉时拒绝执行；例：`git merge --ff-only feature/login`。
- `git branch -d <分支>`：安全删除已经合并的本地分支；例：`git branch -d feature/login`。
- `git push origin <分支>`：把本地分支推送到远程；例：`git push origin main`。

## 分支合并

- Fast-Forward：目标分支没有产生新 Commit 时，只需把它的指针向前移动，不会产生额外提交。
- Merge Commit（合并提交）：两条历史已经分叉时，普通 `git merge` 可能创建一个通常拥有两个 Parent Commits（父提交）的新 Commit。
- Branch 是指向 Commit 的引用；删除已经合并的 Branch，不会删除已进入主历史的 Commit。

常见的短期功能分支流程：

```bash
git switch main
git merge --ff-only feature/login
git branch -d feature/login
git push origin main
```

## 关联

- [[JavaScript Project Structure（JavaScript 项目结构）]]：Git 可以跟踪项目源码和配置的版本变化，而 `.git/` 保存仓库内部数据。

