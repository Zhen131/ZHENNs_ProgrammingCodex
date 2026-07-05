---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/Web与网络, 语言/JavaScript, 层级/基础]
aliases: [useState, React useState, 状态 Hook, React Hook, setState, state setter]
created: 2026-07-05
updated: 2026-07-05
---

# useState（React 状态 Hook）

## 一句话

`useState（React 状态 Hook）` 是 React 中给组件创建 state 的 Hook，它返回当前状态值和修改状态的方法。

## 背景：它出现前的问题

React 页面需要记住一些会影响显示的数据，例如计数器数值、表单输入、当前筛选条件或业务数据。如果这些数据只存在普通变量里，React 不一定知道页面需要重新渲染。

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

左侧的 `[count, setCount]` 不是 React 专属语法，而是 [[JavaScript Destructuring Assignment（JavaScript 解构赋值）]]：React 返回一个数组，代码按位置把第一个值命名为 `count`，第二个值命名为 `setCount`。

## 核心机制

在真实页面里，更常见的例子是：

```tsx
const [draft, setDraft] = useState<FormDraft>(initialDraft);
```

这段代码表达的是：

- `draft` 是当前页面里的表单草稿。
- `setDraft` 是修改表单草稿的方法。
- `initialDraft` 是页面刚打开时的初始值。
- `<FormDraft>` 是 [[TypeScript Generic（TypeScript 泛型）]]，用来告诉 TypeScript 这份 state 应该符合什么数据形状。

用户输入改变时，页面不应该手动改一堆 DOM，而应该调用 `setDraft(nextDraft)`，让 [[React（React UI 库）]] 根据新 state 更新界面。

## 典型使用场景

- 保存当前表单草稿。
- 保存当前筛选条件。
- 保存页面级临时业务数据。
- 让用户操作触发页面重新渲染。

## 局限性

useState 只负责组件状态，不负责永久存储。刷新页面后，存在 React state 里的数据会丢失。要长期保存交易记录，需要 IndexedDB、后端数据库或其他持久化方案。

如果一个组件里出现太多互相依赖的 useState，也可能说明状态模型需要上移、合并，或者交给 [[useReducer（React Reducer Hook）]] 这类更集中的规则层管理。

useState 的 setter 接收的是“新状态”或“如何从旧状态得到新状态的函数”。它不适合让很多组件到处手写复杂业务修改规则，否则就会遇到 [[为什么复杂 React 状态适合 useReducer]] 里描述的维护问题。

## 和其他概念的关系

- [[React State（React 状态）]] 是 useState 创建和维护的核心对象。
- [[TypeScript Generic（TypeScript 泛型）]] 可以给 useState 标注状态类型。
- [[JavaScript Destructuring Assignment（JavaScript 解构赋值）]] 解释 `const [state, setState] = useState(...)` 的左侧语法。
- [[useReducer（React Reducer Hook）]] 适合复杂 state 的统一修改规则。
- [[为什么 React 不能直接修改 state]] 解释为什么要通过 setter 提交更新。
- [[为什么前端页面不能长期依赖写死数据]] 是理解页面 state 价值的问题入口。

## 关联

- [[React State（React 状态）]]
- [[React（React UI 库）]]
- [[TypeScript（类型化 JavaScript）]]
- [[TypeScript Generic（TypeScript 泛型）]]
- [[JavaScript Destructuring Assignment（JavaScript 解构赋值）]]
- [[useReducer（React Reducer Hook）]]
- [[为什么 React 不能直接修改 state]]
- [[为什么复杂 React 状态适合 useReducer]]
- [[为什么前端页面不能长期依赖写死数据]]
