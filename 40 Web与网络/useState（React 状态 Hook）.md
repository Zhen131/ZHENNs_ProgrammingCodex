---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/Web与网络, 语言/JavaScript, 层级/基础]
aliases: [useState, React useState, 状态 Hook, React Hook]
created: 2026-07-05
updated: 2026-07-05
---

# useState（React 状态 Hook）

## 一句话

`useState（React 状态 Hook）` 是 React 中给组件创建 state 的 Hook，它返回当前状态值和修改状态的方法。

## 背景：它出现前的问题

React 页面需要记住一些会影响显示的数据，例如计数器数值、表单输入、当前账本数据。如果这些数据只存在普通变量里，React 不一定知道页面需要重新渲染。

## 它解决了什么

useState 让组件可以声明“这个数据会影响页面显示”：

```tsx
const [count, setCount] = useState(0);
```

这里可以先理解成：

- `count` 是当前状态值。
- `setCount` 是修改状态的方法。
- `useState(0)` 表示初始值是 `0`。

当调用 `setCount(count + 1)` 时，React 会知道状态变了，需要重新渲染相关页面。

## 核心机制

在账本项目里，更关键的例子是：

```tsx
const [ledgerData, setLedgerData] = useState<LedgerData>(initialLedgerData);
```

这段代码表达的是：

- `ledgerData` 是当前页面里的临时账本数据。
- `setLedgerData` 是替换账本状态的方法。
- `initialLedgerData` 是页面刚打开时的初始账本。
- `<LedgerData>` 是 TypeScript 给 state 标注的数据形状。

新增交易时，页面不应该手动改一堆 DOM，而应该拿到新的 [[LedgerData（账本数据对象）]] 后调用 `setLedgerData(newLedgerData)`，让 [[React（React UI 库）]] 根据新 state 更新界面。

## 典型使用场景

- 保存当前表单草稿。
- 保存当前筛选条件。
- 保存 `ledgerData` 这类页面级临时数据。
- 让用户操作触发页面重新渲染。

## 局限性

useState 只负责组件状态，不负责永久存储。刷新页面后，存在 React state 里的数据会丢失。要长期保存交易记录，需要 IndexedDB、后端数据库或其他持久化方案。

如果一个组件里出现太多互相依赖的 useState，也可能说明状态模型需要上移、合并，或者交给更清晰的业务对象管理。

## 和其他概念的关系

- [[React State（React 状态）]] 是 useState 创建和维护的核心对象。
- [[TypeScript（类型化 JavaScript）]] 可以给 useState 标注状态类型。
- [[LedgerData（账本数据对象）]] 是账本项目里适合作为页面 state 的业务数据对象。
- [[为什么账本页面不能继续使用写死数据]] 是理解 `setLedgerData` 价值的问题入口。

## 关联

- [[React State（React 状态）]]
- [[React（React UI 库）]]
- [[TypeScript（类型化 JavaScript）]]
- [[LedgerData（账本数据对象）]]
- [[为什么账本页面不能继续使用写死数据]]
