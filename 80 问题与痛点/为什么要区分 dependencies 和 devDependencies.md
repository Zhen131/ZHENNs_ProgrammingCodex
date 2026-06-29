---
type: 问题卡片
status: 草稿
tags: [类型/问题卡片, 问题/依赖管理, 领域/软件工程, 语言/JavaScript]
aliases: [dependencies 和 devDependencies 的区别, 为什么区分运行时依赖和开发依赖, 运行时依赖 vs 开发依赖]
created: 2026-06-29
updated: 2026-06-29
---

# 为什么要区分 dependencies 和 devDependencies

## 痛点

一个项目会用很多 package，但这些 package 不一定都服务同一个阶段。有些是用户使用项目时必须参与运行的，有些只是开发者写代码、检查代码、跑测试、构建项目时需要。

如果不区分它们，读项目时就很难判断哪些属于业务运行，哪些属于开发工具链。

## 以前怎么解决

粗暴做法是把所有 package 都放在一起。但这样会带来理解成本：

- 无法快速看出项目运行时真正依赖什么。
- 无法判断某个工具是不是只在本地开发时使用。
- 初学者容易把 `vitest`、`eslint`、`typescript` 等工具误解成业务功能的一部分。

## 技术演进

[[package.json（项目清单）]] 通过依赖分类表达 package 的角色：

- `dependencies（运行时依赖）`：项目运行时需要，例如 `next`、`react`、`decimal.js`。
- `devDependencies（开发依赖）`：开发、测试、构建、类型检查时需要，例如 `typescript`、`vitest`、`eslint`、`tailwindcss`、`@types/node`。

这背后的稳定概念是 [[Dependency（依赖）]]。

## 相关技术

- [[Dependency（依赖）]]
- [[package.json（项目清单）]]
- [[Package（软件包）]]
- [[npm（Node 包管理器）]]

## 我的理解

dependencies 和 devDependencies 的区别，本质上是在问：

```text
这个 package 是项目运行本身需要？
还是开发者把项目做出来、测出来、构建出来时需要？
```

这个判断能帮助我读项目时先看业务主线，再看工具链。

## 关联

- [[为什么 package.json 是读 JavaScript 项目的入口]]
- [[为什么读 JavaScript 项目要先识别工程骨架]]
