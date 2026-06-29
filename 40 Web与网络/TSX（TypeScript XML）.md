---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/Web与网络, 语言/TypeScript, 语言/JavaScript, 层级/基础]
aliases: [TSX, TypeScript XML, .tsx]
created: 2026-06-29
updated: 2026-06-29
---

# TSX（TypeScript XML）

## 一句话

`TSX（TypeScript XML）` 是 TypeScript + JSX，常用于在 TypeScript 文件里写 React component 或 Next.js 页面。

## 背景：它出现前的问题

React component 既需要界面结构，也需要逻辑和数据类型。只用 `.ts` 文件不能直接写 JSX 结构；只用 `.jsx` 又缺少 TypeScript 类型信息。

## 它解决了什么

TSX 允许开发者在同一个组件文件中同时表达：

- TypeScript 逻辑和类型。
- 类似 HTML 的 JSX 界面结构。

常见后缀关系可以先这样记：

```text
.ts   = TypeScript 文件
.tsx  = TypeScript + JSX，通常写 React 组件或页面
.js   = JavaScript 文件
.jsx  = JavaScript + JSX
```

## 核心机制

TSX 是文件语法，不是 [[Next.js（Next 应用框架）]]。Next.js 项目经常有 `.tsx` 文件，是因为 Next.js 基于 [[React（React UI 库）]]，而 React + TypeScript 项目常用 TSX 写组件和页面。

## 典型使用场景

- 写 React component。
- 写 Next.js 的 `page.tsx` 和 `layout.tsx`。
- 给 component props 标注类型，同时返回 JSX 界面结构。

## 局限性

TSX 只是语法层。它不规定路由、布局、构建、部署，也不等于 Next.js。把 TSX 当成框架，会混淆“文件怎么写”和“应用怎么组织”。

## 和其他概念的关系

- [[JSX（JavaScript XML）]] 是 TSX 的界面语法基础。
- [[TypeScript（类型化 JavaScript）]] 提供类型系统。
- [[Next.js App Router（Next 应用路由）]] 会把特定位置的 `page.tsx`、`layout.tsx` 赋予特殊角色。
- [[TSX 和 Next.js 是一回事吗]] 是对应问题入口。

## 在项目中的表现

- [[26_06_29 账本项目 - 建立 React 和 Next.js 的基础心智模型]]：这次学习校正了“TSX 不是 Next.js”这个误区。

## 关联

- [[TypeScript（类型化 JavaScript）]]
- [[JSX（JavaScript XML）]]
- [[React（React UI 库）]]
- [[Next.js（Next 应用框架）]]
- [[TSX 和 Next.js 是一回事吗]]
