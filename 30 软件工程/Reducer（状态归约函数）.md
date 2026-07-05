---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/软件工程, 语言/JavaScript, 层级/基础]
aliases: [Reducer, reducer, reducer function, 状态归约函数, 状态规则处理器, 状态规则层]
created: 2026-07-05
updated: 2026-07-06
---

# Reducer（状态归约函数）

## 一句话

`Reducer（状态归约函数）` 是接收旧值和输入，并返回新值的函数；在状态管理里常写成 `reducer(state, action) => newState`。

## 背景：它出现前的问题

Reducer 不是 React 独有概念。JavaScript 的 `Array.prototype.reduce`、Redux 这类状态管理思路，以及 React 的 [[useReducer（React Reducer Hook）]] 都会用到类似“旧值 + 输入 -> 新值”的模式。

复杂业务状态通常不只有一种修改方式。新增一条记录、删除一条记录、批量导入、重置数据、重新计算派生结果，可能都会影响同一份事实数据。

如果这些规则散落在多个组件或函数里，开发者很难确认每次修改都遵守同一套规则。一个地方可能校验了字段，另一个地方可能忘了；一个地方重新计算了结果，另一个地方可能只改了表面列表。

## 它解决了什么

在状态管理场景里，Reducer 把“状态怎么变化”集中到一个规则函数里：

```ts
function reducer(state, action) {
  switch (action.type) {
    case "ADD_ITEM":
      return nextState;
    case "RESET":
      return initialState;
    default:
      return state;
  }
}
```

这让调用方不需要到处直接拼新 state，而是提交一个 action，让 reducer 按统一规则产出下一份 state。

## 核心机制

Reducer 的核心公式是：

```text
旧 state + action -> 新 state
```

其中：

- `state` 是当前状态。
- `action` 是操作指令，常见格式是 `{ type, payload }`。
- `type` 表示操作类型。
- `payload` 携带这次操作需要的数据。
- 返回值必须是下一份 state。

在 [[useReducer（React Reducer Hook）]] 里，组件通过 `dispatch(action)` 发送操作意图，React 再调用 reducer 计算新 state。这里的 reducer 是通用 reducer 思路在 React 状态管理里的具体用法。

## 典型使用场景

- JavaScript 数组聚合计算，例如把一组值归约成总和、分组或统计结果。
- Redux 或 React 里的复杂业务状态管理。
- 把多种修改动作集中到一个规则层。
- 让新增、删除、更新、重置等操作更容易测试。
- 在事实数据变化后统一触发 [[Derived Data（派生数据）]] 重算。

## 局限性

Reducer 只是结构，不是自动安全机制。如果 reducer 内部仍然随意修改旧对象、跳过校验、遗漏重算，它依然会产生错误状态。

Reducer 也不适合所有状态。只有当“旧值如何变成新值”的规则需要被集中表达时，它才值得单独抽出来。在 React 里，只有当状态修改规则变复杂、多个 action 共享同一份 state，或者需要集中维护业务规则时，它才比简单 setter 更有价值。

## 和其他概念的关系

- [[useReducer（React Reducer Hook）]] 是 React 中使用 reducer 的常见入口。
- [[React State（React 状态）]] 可以由 reducer 统一计算下一份状态。
- [[useState（React 状态 Hook）]] 更适合简单状态，不需要单独 reducer。
- [[为什么复杂 React 状态适合 useReducer]] 解释什么时候 reducer 值得引入。
- [[为什么 React 不能直接修改 state]] 解释 reducer 返回新 state 的边界。

## 关联

- [[useReducer（React Reducer Hook）]]
- [[React State（React 状态）]]
- [[Derived Data（派生数据）]]
- [[为什么复杂 React 状态适合 useReducer]]
- [[为什么 React 不能直接修改 state]]
