---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/编程语言, 语言/TypeScript, 层级/基础]
aliases: [TypeScript Generic, Generic, Generics, 泛型, TypeScript 泛型, 类型参数]
created: 2026-07-05
updated: 2026-07-05
---

# TypeScript Generic（TypeScript 泛型）

## 一句话

`TypeScript Generic（TypeScript 泛型）` 是把类型当作参数传给函数、类型或组件的机制，让同一段代码可以保留结构复用，同时明确它处理的数据形状。

## 背景：它出现前的问题

读 TypeScript 代码时，经常会看到尖括号写法：

```ts
useState<LedgerData>(initialLedgerData);
```

如果只学过 C、Python 或 Java 的基础语法，这段代码容易被误读成运行时创建了某个 `LedgerData` 对象。实际上这里的 `<LedgerData>` 主要是在告诉 [[TypeScript（类型化 JavaScript）]]：这个 state 应该符合 `LedgerData` 这种数据形状。

## 它解决了什么

Generic 让一段代码既能复用，又能保留具体类型信息。

例如：

```ts
const [draft, setDraft] = useState<FormDraft>(initialDraft);
```

这表示：

- `useState` 这套逻辑可以管理很多种状态。
- 这一次管理的是 `FormDraft` 类型的状态。
- `setDraft` 后续应该接收符合 `FormDraft` 的新状态。
- 编辑器和 TypeScript 编译检查可以据此发现字段或类型错误。

## 核心机制

Generic 可以理解成“类型层面的参数”：

```text
普通函数参数
= 运行时传入具体值

Generic 类型参数
= 开发阶段传入具体类型
```

在 React 项目里，`useState<T>()`、`useReducer` 的 state/action 类型、component props 类型都可能用到 Generic。

Generic 大多会在编译成 JavaScript 后消失。浏览器或 Node.js 运行的是 JavaScript，不会在运行时保留这层 TypeScript 类型检查。

## 典型使用场景

- 给 [[useState（React 状态 Hook）]] 标注 state 的数据形状。
- 给 [[useReducer（React Reducer Hook）]] 的 state 和 action 建立类型约束。
- 写可复用函数，例如 `function identity<T>(value: T): T`。
- 写可复用数据结构，例如 `Array<T>`、`Promise<T>`。

## 局限性

Generic 只能帮助开发阶段的类型理解和检查，不能替代运行时校验。用户输入、接口返回、文件导入这些外部数据仍然需要运行时检查。

Generic 写得太深时，也会增加读代码成本。初学阶段可以先抓住一个核心判断：尖括号里大多是在描述“这次代码处理什么类型的数据”，不是在创建运行时对象。

## 和其他概念的关系

- [[TypeScript（类型化 JavaScript）]] 提供 Generic 语法和类型检查能力。
- [[useState（React 状态 Hook）]] 常用 Generic 标注状态类型。
- [[useReducer（React Reducer Hook）]] 在复杂状态里也常需要 Generic 或显式类型约束。
- [[JavaScript Destructuring Assignment（JavaScript 解构赋值）]] 解释 `const [state, setState] = ...` 的左侧语法。

## 关联

- [[TypeScript（类型化 JavaScript）]]
- [[useState（React 状态 Hook）]]
- [[useReducer（React Reducer Hook）]]
- [[JavaScript Destructuring Assignment（JavaScript 解构赋值）]]
