---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/Web与网络, 语言/JavaScript, 层级/基础]
aliases: [React, React.js, React UI Library, React UI 库]
created: 2026-06-29
updated: 2026-07-05
---

# React（React UI 库）

## 一句话

`React（React UI 库）` 是 JavaScript / TypeScript 生态中用来构建用户界面的库，它的核心思想是把界面拆成 [[UI Component（UI 组件）]]，并让页面根据数据状态自动更新。

## 背景：它出现前的问题

复杂页面如果把 HTML 结构、交互逻辑、数据变化和界面更新都写在一起，文件会很快变成难维护的大块代码。账本页面可能有交易表单、交易列表、持仓表格、资产卡片、价格输入框、按钮和弹窗，如果不拆分，就很难读。

另一个痛点是手动更新 [[DOM（文档对象模型）]]：一笔交易变化后，交易列表、资产汇总、平均成本和盈亏都要同步变化。如果每个区域都靠 `querySelector` 找节点再手动改，很容易漏掉某一处。

## 它解决了什么

React 主要帮助开发者解决：

- 界面如何拆成组件。
- 组件之间如何组合。
- 数据变化后界面如何更新。
- 如何用 [[React State（React 状态）]] 代替到处手动修改 DOM。

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

更具体地说，React 的页面更新思路是：

```text
用户操作
-> 修改 state
-> React 根据 state 重新渲染页面
```

在业务页面里，这意味着用户操作后不应该手动修改每一块 DOM，而是生成新的页面状态或业务数据，调用 [[useState（React 状态 Hook）]] 返回的更新方法，让页面根据新 state 重新显示。

当这份 state 的修改规则变复杂时，React 还可以用 [[useReducer（React Reducer Hook）]]：组件通过 `dispatch(action)` 描述用户操作，[[Reducer（状态归约函数）]] 统一计算下一份 state。这样页面组件更专注于“用户做了什么”，业务规则更集中。

## 典型使用场景

- 拆分账本页面：`LedgerPage`、`TradeForm`、`TradeList`、`PositionTable`。
- 把重复出现的按钮、表单、表格抽成可复用组件。
- 在数据变化后更新页面显示。
- 让列表、汇总和预览从同一份页面状态或事实数据读取结果。
- 用 useReducer 管理会被多种操作修改的核心业务状态。

## 局限性

React 主要负责 UI component 和界面更新，不直接规定完整应用的路由、构建、部署和渲染策略。这也是为什么 React 项目常常会搭配 Next.js 这类应用框架。

React state 也不是永久数据库。放在页面内存里的账本数据刷新后会丢失；如果需要长期保存交易记录，需要 IndexedDB、后端数据库或其他持久化方案。

## 和其他概念的关系

- [[UI Component（UI 组件）]] 是 React 的核心组织单元。
- [[React State（React 状态）]] 让 React 根据数据变化重新渲染页面。
- [[useState（React 状态 Hook）]] 是创建组件 state 的常见 Hook。
- [[useReducer（React Reducer Hook）]] 是管理复杂 state 修改规则的常见 Hook。
- [[Reducer（状态归约函数）]] 让复杂状态变化集中到统一规则层。
- [[DOM（文档对象模型）]] 是浏览器中的页面结构，React 会帮助开发者减少手动 DOM 同步。
- [[Next.js（Next 应用框架）]] 基于 React，并提供应用级规则。
- [[TSX（TypeScript XML）]] 常用于在 TypeScript 中写 React component。
- [[React 和 Next.js 有什么区别]] 是理解 React 边界的问题入口。
- [[为什么 React 不推荐手动操作 DOM]] 解释 React 的状态驱动更新为什么重要。
- [[为什么复杂 React 状态适合 useReducer]] 解释简单状态和复杂状态的管理分界。

## 关联

- [[UI Component（UI 组件）]]
- [[React State（React 状态）]]
- [[useState（React 状态 Hook）]]
- [[useReducer（React Reducer Hook）]]
- [[Reducer（状态归约函数）]]
- [[DOM（文档对象模型）]]
- [[JSX（JavaScript XML）]]
- [[TSX（TypeScript XML）]]
- [[Next.js（Next 应用框架）]]
- [[为什么前端项目要把界面、逻辑、样式和框架分层]]
- [[为什么 React 不推荐手动操作 DOM]]
- [[为什么 React 不能直接修改 state]]
- [[为什么复杂 React 状态适合 useReducer]]
