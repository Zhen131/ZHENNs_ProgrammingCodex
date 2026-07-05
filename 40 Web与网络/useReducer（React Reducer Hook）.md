---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/Web与网络, 语言/JavaScript, 层级/基础]
aliases: [useReducer, React useReducer, Reducer Hook, React Reducer Hook, reducer Hook]
created: 2026-07-05
updated: 2026-07-05
---

# useReducer（React Reducer Hook）

## 一句话

`useReducer（React Reducer Hook）` 是 React 中用来管理复杂 state 的 Hook，它让组件通过 `dispatch(action)` 提交操作意图，再由 [[Reducer（状态归约函数）]] 根据旧 state 和 action 计算新 state。

## 背景：它出现前的问题

[[useState（React 状态 Hook）]] 很适合简单状态：输入框内容、弹窗开关、当前 tab、简单计数器。问题出现在同一份 [[React State（React 状态）]] 会被很多操作修改时。

例如一份业务数据可能会被新增、删除、更新、重置、导入和重新计算影响。如果每个组件都直接写一段 `setState(nextState)` 逻辑，规则会散落到页面各处，后面很容易出现“有的地方更新了事实数据，但忘了重新计算 [[Derived Data（派生数据）]]”的问题。

## 它解决了什么

useReducer 多出来的不是普通中间层，而是一层统一的状态修改规则：

```tsx
const [state, dispatch] = useReducer(reducer, initialState);
```

这段代码可以读成：

- `state` 是当前状态。
- `dispatch` 是发送 action 的函数。
- `reducer` 是根据旧状态和 action 计算新状态的函数。
- `initialState` 是初始状态。

核心区别是：

```text
useState
= 直接提交新状态

useReducer
= 提交操作意图，由 reducer 生成新状态
```

## 核心机制

useReducer 的核心流程是：

```text
用户操作
-> dispatch(action)
-> reducer(state, action)
-> newState
-> React 根据新 state 重新渲染页面
```

常见 action 长这样：

```ts
dispatch({
  type: "ADD_TRADE",
  payload: newTrade,
});
```

这里 `dispatch` 不直接接收新状态，而是接收“我要做什么”。真正怎么改 state，由 reducer 统一决定。

餐厅类比里，`dispatch` 更像把点菜单送到后厨的服务员；action 是点菜单；reducer 才是后厨规则管理员，负责根据当前状态和点菜单决定最终产出。

## 典型使用场景

- 一份核心业务 state 会被很多操作修改。
- 新增、删除、更新、重置、导入等操作都要走统一规则。
- 状态变化后需要同步重新计算 [[Derived Data（派生数据）]]。
- 希望把页面组件的职责限制为“用户做了什么”，把“业务数据如何变化”放进独立规则层。

## 局限性

useReducer 主要不是为了性能，而是为了结构。它不会自动让状态更安全，也不会自动替开发者校验数据。只有把校验、重算和拒绝非法操作的规则写进 reducer，它才会成为可靠的规则层。

如果只是弹窗开关、搜索框文本、当前选中项这类简单 UI 状态，用 useReducer 反而会让代码显得笨重。这类状态继续用 [[useState（React 状态 Hook）]] 更直接。

## 和其他概念的关系

- [[React State（React 状态）]] 是 useReducer 管理的对象。
- [[Reducer（状态归约函数）]] 是 useReducer 中真正计算新 state 的函数。
- [[useState（React 状态 Hook）]] 适合简单状态，useReducer 适合复杂状态修改规则。
- [[为什么复杂 React 状态适合 useReducer]] 是 useReducer 的问题入口。
- [[为什么 React 不能直接修改 state]] 解释为什么必须通过 React 的更新入口改变 state。

## 关联

- [[React（React UI 库）]]
- [[React State（React 状态）]]
- [[Reducer（状态归约函数）]]
- [[useState（React 状态 Hook）]]
- [[Derived Data（派生数据）]]
- [[为什么复杂 React 状态适合 useReducer]]
- [[为什么 React 不能直接修改 state]]
