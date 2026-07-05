---
type: 问题卡片
status: 草稿
tags: [类型/问题卡片, 问题/前端架构, 领域/Web与网络, 领域/软件工程]
aliases: [useState 和 useReducer 有什么区别, 什么时候用 useReducer, 为什么要用 useReducer, 复杂状态管理, React 复杂状态]
created: 2026-07-05
updated: 2026-07-05
---

# 为什么复杂 React 状态适合 useReducer

## 痛点

[[useState（React 状态 Hook）]] 可以直接提交新状态，适合简单 UI 状态。但当同一份 [[React State（React 状态）]] 会被很多操作修改时，问题会变成：修改规则到底放在哪里？

如果新增、删除、更新、导入、重置都散落在不同组件里，每个地方都自己拼一份新 state，就很容易漏掉校验、重算或一致性规则。

## 以前怎么解决

简单阶段可以直接写：

```ts
setState(nextState);
```

这相当于告诉 React：“这是我已经算好的新数据。”它足够直观，也适合弹窗开关、搜索框文本、当前 tab 这类状态。

但复杂业务状态往往不是“把一个值换掉”这么简单。比如一条交易变了，交易列表、持仓、现金、汇总和错误标记都可能受影响。如果每个入口都手写更新逻辑，长期维护风险会变高。

## 技术演进

[[useReducer（React Reducer Hook）]] 把修改方式从“直接提交结果”改成“提交操作意图”：

```text
dispatch(action)
-> reducer(state, action)
-> newState
```

这样分工更清楚：

- 页面组件负责描述用户做了什么。
- action 负责描述操作意图。
- [[Reducer（状态归约函数）]] 负责按统一规则计算下一份 state。

它的主要价值不是性能，而是结构：让复杂状态修改更集中、更容易测试，也更容易看出每种操作是否都遵守同一套规则。

## 相关技术

- [[React State（React 状态）]]
- [[useState（React 状态 Hook）]]
- [[useReducer（React Reducer Hook）]]
- [[Reducer（状态归约函数）]]
- [[Derived Data（派生数据）]]

## 我的理解

useState 像“我把算好的结果直接交给 React”。useReducer 像“我告诉 React 我要做什么，再让统一规则层根据旧状态和操作指令算出新状态”。

所以它们不是谁替代谁。简单 UI 状态继续用 useState；会被很多操作修改的核心业务状态，更适合用 useReducer。

## 关联

- [[为什么 React 不能直接修改 state]]
- [[为什么前端页面不能长期依赖写死数据]]
- [[为什么派生数据不应该当成事实数据保存]]
- [[React（React UI 库）]]
