---
type: 问题卡片
status: 草稿
tags: [类型/问题卡片, 问题/前端基础, 领域/Web与网络, 语言/JavaScript]
aliases: [为什么不能直接改 React State, 为什么不能直接修改 state, React state mutation, 直接修改 state 的问题]
created: 2026-07-05
updated: 2026-07-05
---

# 为什么 React 不能直接修改 state

## 痛点

初学 React 时，很容易把 state 当成普通变量或普通对象，直接写：

```ts
state.items.push(newItem);
```

问题是：你改了对象内部内容，不等于告诉 [[React（React UI 库）]] “状态已经变了”。React 不一定会按你的预期重新渲染页面，后续数据流也会变得难追踪。

## 以前怎么解决

在手写 DOM 的页面里，开发者经常直接改变量，再手动找到 DOM 节点改页面。这样虽然直接，但复杂页面会很快混乱：数据改了，列表、汇总、图表和错误提示都要人工同步。

React 的思路是把这件事反过来：

```text
不要手动同步每块 DOM
-> 通过 React 的状态更新入口提交新 state
-> 让 React 根据新 state 重新渲染
```

## 技术演进

更新 React state 时，应该走明确入口：

```ts
setState(nextState);
```

或者在复杂状态里：

```ts
dispatch(action);
```

这两个入口都在表达：“React，这次状态更新需要被你接管。”

同时，新的数组或对象通常应该通过复制旧值生成，而不是在原对象上偷偷修改：

```ts
setState({
  ...state,
  items: [...state.items, newItem],
});
```

这样做让 state 变化更明确，也让 [[useReducer（React Reducer Hook）]] 或 [[useState（React 状态 Hook）]] 的更新逻辑更容易维护。

## 相关技术

- [[React（React UI 库）]]
- [[React State（React 状态）]]
- [[useState（React 状态 Hook）]]
- [[useReducer（React Reducer Hook）]]
- [[Reducer（状态归约函数）]]

## 我的理解

React state 不是“我偷偷改掉的普通对象”，而是驱动页面重新显示的数据。直接改对象只是在内存里动了手脚；通过 `setState` 或 `dispatch` 提交更新，才是在告诉 React：请用这份新状态重新显示页面。

## 关联

- [[为什么 React 不推荐手动操作 DOM]]
- [[为什么复杂 React 状态适合 useReducer]]
- [[为什么前端页面不能长期依赖写死数据]]
