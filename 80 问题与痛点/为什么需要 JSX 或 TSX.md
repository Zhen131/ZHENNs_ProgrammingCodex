---
type: 问题卡片
status: 草稿
tags: [问题/前端语法, 领域/Web与网络, 语言/JavaScript, 语言/TypeScript]
aliases: [为什么需要 JSX, 为什么需要 TSX, 为什么把 HTML 写进 JavaScript]
created: 2026-06-29
updated: 2026-10-08
---

# 为什么需要 JSX 或 TSX

## 痛点

JSX/TSX 看起来像把 HTML 写进 JavaScript 或 TypeScript。初学者会自然困惑：为什么不直接写 HTML 文件？为什么要把界面结构写进代码里？

## 以前怎么解决

传统直觉会把结构、样式、逻辑分成 HTML、CSS、JavaScript 文件。但 React 的组件化思路更关注“一个 UI component 的结构、行为和数据如何一起表达”。

## 技术演进

[[JSX（JavaScript XML）]] 让 JavaScript 可以描述界面结构。[[TSX（TypeScript XML）]] 在此基础上加入 TypeScript 类型能力。

这样一个 React 组件的结构、它用到的数据、点击后干什么、数据是什么类型，全在同一个文件里，不用在三个文件之间来回跳。

用 Lego（乐高）类比，JSX/TSX 更像零件的结构说明：这块 component 里放了哪些子零件、文字和输入框。JavaScript / TypeScript 处理行为和数据，CSS / Tailwind 处理装饰和摆放，Next.js 处理这些零件如何进入完整应用。

## 我的理解

目前先不追求完全理解 JSX/TSX 的底层转换，只记住：它们不是 Next.js，也不是普通 HTML；它们是 React 生态里描述界面结构的语法。

## 关联

- [[JSX（JavaScript XML）]]：让 JavaScript 里能直接写界面结构的语法。
- [[TSX（TypeScript XML）]]：JSX 加上 TypeScript 类型，React + TS 项目的标配。
- [[React（React UI 库）]]：JSX 是为 React 组件发明的，离开 React 基本用不到。
- [[UI Component（UI 组件）]]：JSX 描述的就是一个组件长什么样。
- [[TypeScript（类型化 JavaScript）]]：TSX 里的"T"。
- [[CSS（层叠样式表）]] / [[Tailwind CSS（Tailwind 样式工具）]]：JSX 管结构，它们管样子。
- [[Next.js（Next 应用框架）]]：Next.js 项目里的页面文件是 `.tsx`，但 TSX 不是 Next.js 的东西。
- [[TSX 和 Next.js 是一回事吗]]：这个混淆的专门解释。
- [[为什么前端项目要把界面、逻辑、样式和框架分层]]：JSX 在分层里的位置。
