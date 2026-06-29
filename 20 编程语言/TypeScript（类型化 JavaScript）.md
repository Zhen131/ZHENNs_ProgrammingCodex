---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/编程语言, 语言/TypeScript, 语言/JavaScript, 层级/基础]
aliases: [TypeScript, TS, 类型化 JavaScript, Typed JavaScript]
created: 2026-06-29
updated: 2026-06-29
---

# TypeScript（类型化 JavaScript）

## 一句话

`TypeScript（类型化 JavaScript）` 是给 JavaScript 加上类型系统的语言，常用于让大型 JavaScript 项目更容易理解、检查和维护。

## 背景：它出现前的问题

JavaScript 很灵活，但项目变大后，开发者容易看不清对象有哪些字段、函数需要什么参数、某个值会不会缺失。读代码时，如果没有类型信息，很多数据结构只能靠猜。

在账本这类项目里，`Trade`、`TradeDraft`、`Position`、`PriceSnapshot`、`LedgerData` 这类对象如果没有明确类型，就很容易把字段含义和数据流看乱。

## 它解决了什么

TypeScript 让代码在运行前就能表达更多结构信息：

- 对象应该有哪些字段。
- 函数应该接收什么参数。
- 返回值是什么形状。
- 某个值是否可能缺失。
- 编辑器能基于类型提供提示和检查。

## 核心机制

TypeScript 可以粗略理解成 JavaScript 的增强版。它保留 JavaScript 生态，同时增加类型标注、接口、泛型等能力。

在 React 项目里，TypeScript 常和 [[TSX（TypeScript XML）]] 一起使用：逻辑和类型写在 TypeScript 中，界面结构通过 JSX 风格语法写在同一个组件文件中。

## 典型使用场景

- 给业务对象建模，例如交易、持仓、价格快照。
- 给 React component 的 props 标注类型。
- 在重构时提前发现字段名或参数类型错误。
- 与编辑器配合，降低读代码时的猜测成本。

## 局限性

TypeScript 主要在开发阶段帮助理解和检查代码。它不能替代运行时校验，也不能自动解释业务含义。类型写得太复杂时，也会让初学者先被类型系统本身挡住。

## 和其他概念的关系

- [[JavaScript Runtime（JavaScript 运行时）]] 解释代码最终运行在哪些环境里。
- [[TSX（TypeScript XML）]] 是 TypeScript 和 JSX 结合后常用于写 React 组件的文件语法。
- [[React（React UI 库）]] 项目常用 TypeScript 来约束 component 的数据结构。
- [[为什么前端项目要把界面、逻辑、样式和框架分层]] 解释了 TypeScript 在前端分层中的位置。

## 关联

- [[TSX（TypeScript XML）]]
- [[React（React UI 库）]]
- [[JavaScript Runtime（JavaScript 运行时）]]
