---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/Web与网络, 语言/JavaScript, 层级/基础]
aliases: [React, React.js, React UI Library, React UI 库]
created: 2026-06-29
updated: 2026-06-29
---

# React（React UI 库）

## 一句话

`React（React UI 库）` 是 JavaScript / TypeScript 生态中用来构建用户界面的库，它的核心思想是把界面拆成 [[UI Component（UI 组件）]]。

## 背景：它出现前的问题

复杂页面如果把 HTML 结构、交互逻辑、数据变化和界面更新都写在一起，文件会很快变成难维护的大块代码。账本页面可能有交易表单、交易列表、持仓表格、资产卡片、价格输入框、按钮和弹窗，如果不拆分，就很难读。

## 它解决了什么

React 主要帮助开发者解决：

- 界面如何拆成组件。
- 组件之间如何组合。
- 数据变化后界面如何更新。

暂时可以把 React component 理解成“一个返回界面结构的函数”：

```tsx
function TradeButton() {
  return <button>新增交易</button>;
}
```

用 Lego（乐高）类比，React 像一套界面零件系统。它关心的不是一次性写出整面墙，而是把页面拆成按钮、表单、列表、卡片这些 component，再把 component 组合成更大的界面。

## 核心机制

React 属于 JavaScript / TypeScript 生态。普通 React 前端项目里，组件逻辑通常用 JavaScript 或 [[TypeScript（类型化 JavaScript）]] 写，界面结构通常用 [[JSX（JavaScript XML）]] 或 [[TSX（TypeScript XML）]] 描述，样式再交给 [[CSS（层叠样式表）]] 或 [[Tailwind CSS（Tailwind 样式工具）]]。

React 更偏 UI 层。它不等于 [[Next.js（Next 应用框架）]]，Next.js 是在 React 之上组织完整应用的 framework。

所以在乐高类比里，React 负责“有 component 这种零件、零件可以组合、数据变化后零件可以重新显示”；Next.js 负责“这些零件如何按页面和路由拼成完整作品”。

## 典型使用场景

- 拆分账本页面：`LedgerPage`、`TradeForm`、`TradeList`、`PositionTable`。
- 把重复出现的按钮、表单、表格抽成可复用组件。
- 在数据变化后更新页面显示。

## 局限性

React 主要负责 UI component，不直接规定完整应用的路由、构建、部署和渲染策略。这也是为什么 React 项目常常会搭配 Next.js 这类应用框架。

## 和其他概念的关系

- [[UI Component（UI 组件）]] 是 React 的核心组织单元。
- [[Next.js（Next 应用框架）]] 基于 React，并提供应用级规则。
- [[TSX（TypeScript XML）]] 常用于在 TypeScript 中写 React component。
- [[React 和 Next.js 有什么区别]] 是理解 React 边界的问题入口。

## 关联

- [[UI Component（UI 组件）]]
- [[JSX（JavaScript XML）]]
- [[TSX（TypeScript XML）]]
- [[Next.js（Next 应用框架）]]
- [[为什么前端项目要把界面、逻辑、样式和框架分层]]
