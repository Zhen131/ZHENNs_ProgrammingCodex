---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/Web与网络, 语言/JavaScript, 层级/基础]
aliases: [Component, 组件, UI 组件, React Component, React 组件]
created: 2026-06-29
updated: 2026-06-29
---

# UI Component（UI 组件）

## 一句话

`UI Component（UI 组件）` 是用户界面的组成单元，可以把复杂页面拆成更小、更容易理解和复用的界面零件。

## 背景：它出现前的问题

如果一个页面的所有结构、样式和交互都堆在同一个地方，页面越复杂就越难改。账本项目里，交易表单、交易列表、持仓表格、资产汇总和价格输入框本来就是不同职责的界面块。

## 它解决了什么

组件化让开发者可以把复杂界面拆成小块：

- 每个组件负责一小块界面。
- 组件可以被组合成页面。
- 重复出现的界面可以复用。
- 修改某个小组件时，不必同时理解整个页面。

## 核心机制

在 [[React（React UI 库）]] 中，component 可以先粗略理解成“返回界面结构的函数”。它通常用 [[JSX（JavaScript XML）]] 或 [[TSX（TypeScript XML）]] 描述界面长什么样，用 JavaScript / [[TypeScript（类型化 JavaScript）]] 写行为逻辑。

用 Lego（乐高）类比，component 就是一块界面 piece。它可以是一个很小的按钮，也可以是由输入框、按钮和提示文字组合出来的表单。[[CSS（层叠样式表）]] / [[Tailwind CSS（Tailwind 样式工具）]] 决定它的颜色、间距和摆放，[[Next.js（Next 应用框架）]] 则可能把某些 component 放进页面、布局或路由规则里。

## 典型使用场景

- `TradeForm`：新增或编辑交易。
- `TradeList`：展示交易列表。
- `PositionTable`：展示持仓。
- `AssetSummary`：展示资产概览。
- `PriceSnapshotForm`：输入价格快照。

## 局限性

组件拆得太粗会回到大文件问题；拆得太细会让初学者在文件之间跳来跳去。组件边界应该围绕真实职责，而不是为了拆分而拆分。

## 和其他概念的关系

- [[React（React UI 库）]] 以 component 作为核心组织方式。
- [[Next.js（Next 应用框架）]] 会把某些 component 赋予页面或布局角色。
- [[JSX（JavaScript XML）]] / [[TSX（TypeScript XML）]] 常用来描述 component 的结构。
- [[为什么前端项目要把界面、逻辑、样式和框架分层]] 解释了组件为什么只是前端分层中的一层。

## 关联

- [[React（React UI 库）]]
- [[JSX（JavaScript XML）]]
- [[TSX（TypeScript XML）]]
- [[CSS（层叠样式表）]]
- [[Tailwind CSS（Tailwind 样式工具）]]
- [[Next.js App Router（Next 应用路由）]]
