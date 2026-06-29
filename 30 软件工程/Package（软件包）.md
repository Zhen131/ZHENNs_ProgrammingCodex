---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/软件工程, 语言/JavaScript, 层级/基础]
aliases: [package, 包, JavaScript package, npm package, 第三方包]
created: 2026-06-29
updated: 2026-06-29
---

# Package（软件包）

## 一句话

`Package（软件包）` 是别人写好并发布出来、可以安装进项目复用的代码工具包。

## 背景：它出现前的问题

现代项目很少从零实现所有功能。框架、测试、类型检查、样式、精确小数计算等能力通常来自第三方 package。如果不知道 package 是什么，看到项目根目录里的依赖清单和 `node_modules/` 时就会误以为那些都是自己项目的业务源码。

## 它解决了什么

Package 把可复用能力封装成可安装单元，降低重复造轮子的成本。项目只需要在 [[package.json（项目清单）]] 中声明依赖，再由 [[npm（Node 包管理器）]] 安装。

## 核心机制

一个 package 通常包含：

- 可被项目 import 的代码。
- 版本号。
- 自己的依赖声明。
- 类型声明、构建产物或命令行入口。

在 JavaScript/Node 生态中，package 被 npm 安装后会落到 [[node_modules（依赖实体目录）]] 中。

## 典型使用场景

- `react`：通过 [[React（React UI 库）]] 写 UI 组件。
- `next`：通过 [[Next.js（Next 应用框架）]] 构建 React 应用。
- `decimal.js`：做高精度小数计算。
- `typescript`：通过 [[TypeScript（类型化 JavaScript）]] 做类型检查和编译。
- `vitest`：运行测试。
- `eslint`：做代码检查。
- `tailwindcss`：提供 [[Tailwind CSS（Tailwind 样式工具）]]。

## 局限性

Package 复用了外部能力，也引入了外部依赖。依赖越多，项目越需要清楚区分直接依赖、传递依赖、运行时依赖和开发依赖，避免把依赖目录当成业务源码阅读。

## 和其他概念的关系

- [[npm（Node 包管理器）]] 负责安装和运行 package 相关命令。
- [[Dependency（依赖）]] 描述项目为什么需要某个 package。
- [[package.json（项目清单）]] 声明项目直接依赖哪些 package。
- [[node_modules（依赖实体目录）]] 保存安装后的 package 实体。
- [[Framework（框架）]]、UI library 和样式工具都可以作为 package 被安装。

## 在项目中的表现

- [[26_06_29 账本项目 - 理解 Node.js、npm 与 node_modules]]：账本项目中的 `next`、`react`、`decimal.js`、`typescript`、`vitest` 都是 package。

## 关联

- [[Dependency（依赖）]]
- [[npm（Node 包管理器）]]
- [[package.json（项目清单）]]
- [[React（React UI 库）]]
- [[Next.js（Next 应用框架）]]
- [[Tailwind CSS（Tailwind 样式工具）]]
- [[为什么不要从 node_modules 读项目]]
