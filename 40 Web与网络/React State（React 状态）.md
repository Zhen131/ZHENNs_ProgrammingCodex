---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/Web与网络, 语言/JavaScript, 层级/基础]
aliases: [State, React State, 状态, React 状态, 页面状态, 组件状态]
created: 2026-07-05
updated: 2026-07-05
---

# React State（React 状态）

## 一句话

`React State（React 状态）` 是 React 组件中会影响页面显示的数据；当 state 改变时，React 会根据新数据重新渲染相关界面。

## 背景：它出现前的问题

没有状态驱动思路时，页面数据变化后，开发者往往需要自己找到 DOM 节点并逐个改页面。小页面还能接受，复杂业务页面会很快变乱：交易列表、资产汇总、平均成本、盈亏和图表都可能依赖同一份数据。

如果每个地方各自维护一份显示结果，页面就容易出现“列表已经更新，但汇总还是旧值”的问题。

## 它解决了什么

React State 让前端开发从“手动同步页面”变成“维护数据状态”：

```text
用户操作
-> 修改 state
-> React 根据 state 重新渲染页面
```

在账本项目里，重要的 state 不是示例里的 `count`，而是 `ledgerData` 这类会影响交易列表和资产汇总的页面数据。

## 核心机制

State 可以先理解成“页面打开期间 React 暂时保存的数据”。它存在于当前页面运行期间，不等于永久数据库。

在 Week 4 的账本阶段，`ledgerData` 放在 React state 里，意思是先让页面打通：

```text
页面表单
-> TradeDraft
-> 校验
-> Trade
-> LedgerData.trades
-> 计算 Position[]
-> 页面展示
```

刷新页面后 state 丢失，不一定是 bug；如果当前目标只是验证输入、校验、入账、计算、展示链路，临时 state 是可以接受的阶段性方案。永久保存要交给后续的 IndexedDB 或其他存储方案。

## 典型使用场景

- 表单输入影响页面预览。
- 新增交易后刷新交易列表。
- `ledgerData` 改变后重新计算并展示资产汇总。
- 在组件里调用 [[useState（React 状态 Hook）]] 创建和更新状态。

## 局限性

State 不是数据库，也不是全局业务大脑。组件里堆太多状态和业务逻辑，会让 React 页面承担不该承担的职责。

在账本项目里，页面应该收集输入、调用 `tradeService`，然后用新的 [[LedgerData（账本数据对象）]] 更新 state；交易校验、持仓计算和盈亏计算应该放在 service、validator 或 calculator 里，而不是塞进组件。

## 和其他概念的关系

- [[React（React UI 库）]] 通过 state 把“数据变了”转成“界面重新显示”。
- [[useState（React 状态 Hook）]] 是创建组件 state 的常见 Hook。
- [[DOM（文档对象模型）]] 是 React 最终要更新的浏览器页面结构。
- [[LedgerData（账本数据对象）]] 可以作为账本页面中的重要 state。
- [[为什么账本页面不能继续使用写死数据]] 解释为什么页面应该从真实 state 读取数据。

## 关联

- [[React（React UI 库）]]
- [[useState（React 状态 Hook）]]
- [[DOM（文档对象模型）]]
- [[LedgerData（账本数据对象）]]
- [[为什么 React 不推荐手动操作 DOM]]
- [[为什么账本页面不能继续使用写死数据]]
