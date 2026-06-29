---
type: 问题卡片
status: 草稿
tags: [类型/问题卡片, 问题/前端语法, 领域/Web与网络, 语言/JavaScript, 语言/TypeScript]
aliases: [为什么需要 JSX, 为什么需要 TSX, 为什么把 HTML 写进 JavaScript]
created: 2026-06-29
updated: 2026-06-29
---

# 为什么需要 JSX 或 TSX

## 痛点

JSX/TSX 看起来像把 HTML 写进 JavaScript 或 TypeScript。初学者会自然困惑：为什么不直接写 HTML 文件？为什么要把界面结构写进代码里？

## 以前怎么解决

传统直觉会把结构、样式、逻辑分成 HTML、CSS、JavaScript 文件。但 React 的组件化思路更关注“一个 UI component 的结构、行为和数据如何一起表达”。

## 技术演进

[[JSX（JavaScript XML）]] 让 JavaScript 可以描述界面结构。[[TSX（TypeScript XML）]] 在此基础上加入 TypeScript 类型能力。

这让一个 React component 可以同时表达：

- 这个组件的界面结构。
- 这个组件依赖的数据。
- 这个组件的交互逻辑。
- 这个组件的类型约束。

## 相关技术

- [[JSX（JavaScript XML）]]
- [[TSX（TypeScript XML）]]
- [[React（React UI 库）]]
- [[UI Component（UI 组件）]]
- [[TypeScript（类型化 JavaScript）]]

## 我的理解

目前先不追求完全理解 JSX/TSX 的底层转换，只记住：它们不是 Next.js，也不是普通 HTML；它们是 React 生态里描述界面结构的语法。

## 关联

- [[TSX 和 Next.js 是一回事吗]]
- [[为什么前端项目要把界面、逻辑、样式和框架分层]]
