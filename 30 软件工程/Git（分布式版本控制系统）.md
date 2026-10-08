---
type: 技术卡片
status: 草稿
tags: [工具/Git, 用途/常见Git指令]
aliases: [Git, 版本控制, 常见 Git 指令, Git 常用命令]
created: 2026-07-18
updated: 2026-10-08
---

# Git（分布式版本控制系统）

## 一句话

Git 给你的代码拍快照。每次 `commit` 就是一张快照，你随时能回到任何一张；`branch` 是从某张快照分出去的另一条线，让你在不碰主线的情况下试东西。

## 背景：它出现前的问题

没有版本控制的时候，你会有 `main.py`、`main_v2.py`、`main_final.py`、`main_final_真的final.py`。改坏了想回退，靠记忆；两个人改同一个文件，靠手动合并。Git 把"这个文件在每个时间点长什么样"全部记下来，回退、对比、合并都变成一条命令。

## 核心机制

三个地方：**工作区**（你正在改的文件）→ **暂存区 Staging Area**（你挑出来准备提交的）→ **仓库**（已经拍成快照的）。`git add` 把文件从工作区挪到暂存区，`git commit` 把暂存区拍成一张快照。

分支只是一个指向某个 commit 的指针。你在 `feature/login` 上提交，指针往前走；`main` 指针不动。合并时如果 `main` 这边没有新提交，Git 直接把 `main` 指针挪到 `feature/login` 的位置，这叫 Fast-Forward（快进），不产生额外提交。如果两边都有新提交，历史已经分叉，普通 `git merge` 会生成一个有两个父提交的 Merge Commit（合并提交）。

删掉一个已经合并的分支不会丢任何东西——分支只是指针，commit 还在主线历史里。

## 速查

- `git status`：看工作区和暂存区现在什么状态。先敲这个再做别的。
- `git add <路径>`：把改动放进暂存区。路径有空格要加引号：`git add "notes/Git basics.md"`。
- `git add -u`：只暂存已跟踪文件的修改和删除，新建的文件不包括。
- `git commit -m "说明"`：把暂存区拍成快照。
- `git commit --amend --no-edit`：把当前暂存的内容补进上一次提交，提交说明不变。会生成新的 commit hash，推过的提交别这么干。
- `git branch`：列出本地分支，`*` 是当前所在。
- `git switch <分支>`：切分支。
- `git merge --ff-only <分支>`：只允许快进合并，历史分叉了就拒绝。想保持主线干净用这个。
- `git branch -d <分支>`：删已经合并的分支。没合并的会拒绝，保护你。
- `git push origin <分支>`：推到远程。

短期功能分支的标准流程：

```bash
git switch main
git merge --ff-only feature/login
git branch -d feature/login
git push origin main
```

## 局限性

Git 记的是文本的行级差异，对二进制文件（图片、Excel）只能整个存，历史会很快变大。它也不会帮你解决逻辑冲突：两个人改了同一行，它只会停下来让你自己决定留哪个。

## 关联

- [[JavaScript Project Structure（JavaScript 项目结构）]]：`.git/` 目录在项目里的位置，以及 Git 跟踪的是源码和配置、不是 `node_modules`。
