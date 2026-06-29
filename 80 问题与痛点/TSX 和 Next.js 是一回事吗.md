---
type: 问题卡片
status: 草稿
tags: [类型/问题卡片, 问题/前端语法, 领域/Web与网络, 语言/TypeScript]
aliases: [TSX 是 Next.js 吗, TSX 和 Next 的关系, .tsx 和 Next.js]
created: 2026-06-29
updated: 2026-06-29
---

# TSX 和 Next.js 是一回事吗

## 痛点

Next.js 项目里经常看到 `.tsx` 文件，例如 `src/app/page.tsx` 和 `src/app/layout.tsx`。这很容易让人误以为 TSX 就是 Next.js，或者 `.tsx` 后缀本身就代表页面。

## 以前怎么解决

只看文件后缀会误判。`.tsx` 只说明这个文件使用 TypeScript + JSX 语法，不说明它在应用里一定是页面、布局或路由。

## 技术演进

需要把语法和框架规则拆开：

- [[TSX（TypeScript XML）]] 是文件语法。
- [[Next.js（Next 应用框架）]] 是应用框架。
- [[Next.js App Router（Next 应用路由）]] 才是让 `src/app/page.tsx` 和 `src/app/layout.tsx` 拥有特殊意义的规则。

## 相关技术

- [[TSX（TypeScript XML）]]
- [[TypeScript（类型化 JavaScript）]]
- [[JSX（JavaScript XML）]]
- [[Next.js（Next 应用框架）]]
- [[Next.js App Router（Next 应用路由）]]

## 我的理解

TSX 回答“这个文件怎么写”；Next.js 回答“这个文件在应用中扮演什么角色”。Next.js 项目经常使用 TSX，是因为它基于 React，而 React + TypeScript 常用 TSX 写组件。

## 关联

- [[26_06_29 账本项目 - 建立 React 和 Next.js 的基础心智模型]]
- [[React 和 Next.js 有什么区别]]
- [[为什么需要 JSX 或 TSX]]
