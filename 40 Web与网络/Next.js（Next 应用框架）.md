---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/Web与网络, 领域/软件工程, 语言/JavaScript, 层级/基础]
aliases: [Next.js, Next, Next 应用框架, next, Next React Framework]
created: 2026-06-29
updated: 2026-06-29
---

# Next.js（Next 应用框架）

## 一句话

`Next.js（Next 应用框架）` 是基于 React 的应用框架，用来规定 React 组件如何组织成完整的网站应用。

## 背景：它出现前的问题

[[React（React UI 库）]] 主要负责 UI component 怎么写、怎么组合、数据变化后怎么更新界面。但一个完整 Web 应用还需要路由、页面入口、布局、构建、开发服务器、渲染策略和部署适配。

如果只知道 React，而不知道 Next.js 负责应用级规则，读 `src/app/page.tsx`、`src/app/layout.tsx`、`.next/`、`next.config.mjs` 时就会混乱。

## 它解决了什么

Next.js 在 React 之上提供应用级能力：

- 页面路由。
- 布局规则。
- 开发服务器。
- 构建流程。
- 渲染策略。
- 静态资源处理。
- 部署适配。

可以先这样记：

```text
React 负责造和拼 UI 零件。
Next.js 负责规定这些零件如何变成完整网站应用。
```

## 核心机制

Next.js 是 [[Framework（框架）]]。它既有代码实体，也有规则和运行流程：

- Next.js 本体来自 `node_modules/next/`。
- 配置可能写在 `next.config.mjs`。
- `src/app/page.tsx`、`src/app/layout.tsx` 这类文件会被 Next.js 赋予特殊意义。
- `.next/` 是运行或构建后生成的缓存和产物，不是源码，也不是 Next.js 本体。

## 典型使用场景

- 用 `npm run dev` 启动本地开发服务器。
- 用 `page.tsx` 表示路由页面。
- 用 `layout.tsx` 表示页面共同外壳。
- 用构建命令生成生产环境产物。

## 局限性

Next.js 不是 [[TSX（TypeScript XML）]]，也不是主要负责“造 UI 零件”的工具。它让项目更有结构，但也增加了框架约定，需要学习哪些文件名和目录有特殊意义。

## 和其他概念的关系

- [[React（React UI 库）]] 是 Next.js 的 UI 基础。
- [[Next.js App Router（Next 应用路由）]] 解释 `src/app/page.tsx` 和 `layout.tsx` 的特殊意义。
- [[JavaScript Project Structure（JavaScript 项目结构）]] 帮助判断 `.next/`、`next.config.mjs`、`node_modules/next/` 的位置。
- [[React 和 Next.js 有什么区别]] 是理解 Next.js 边界的问题入口。

## 关联

- [[React（React UI 库）]]
- [[Framework（框架）]]
- [[Next.js App Router（Next 应用路由）]]
- [[TSX 和 Next.js 是一回事吗]]
- [[为什么 .next 不用读]]
