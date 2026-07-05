---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/软件工程, 领域/数据与存储, 层级/基础]
aliases: [LedgerData, 账本数据, 总账本状态, 临时账本]
created: 2026-07-05
updated: 2026-07-05
---

# LedgerData（账本数据对象）

## 一句话

`LedgerData（账本数据对象）` 是账本项目里承载当前账本事实数据的总对象，可以先理解成页面打开期间的临时总账本。

## 背景：它出现前的问题

如果交易列表、资产汇总、持仓表格和价格快照各自保存一份小数组，页面看起来能跑，但数据源会变散。用户新增一笔交易后，列表可能更新了，资产汇总却还是旧值；持仓结果也可能和交易记录对不上。

账本系统需要先明确：哪些数据是事实，哪些数据是根据事实计算出来的结果。

## 它解决了什么

LedgerData 给账本页面一个共同的数据来源。它大致可以包含：

```ts
type LedgerData = {
  assets: Asset[];
  trades: Trade[];
  priceSnapshots: PriceSnapshot[];
  feeRules: FeeRule[];
};
```

在 Week 4 的账本项目里，最关键的是：

- `LedgerData.trades` 是用户录入的交易事实。
- `Position[]` 是根据交易和价格计算出来的 [[Derived Data（派生数据）]]。

## 核心机制

LedgerData 可以先放在 [[React State（React 状态）]] 里，用来打通页面业务链路：

```text
TradeDraft
-> validateTradeDraft
-> Trade
-> LedgerData.trades
-> calculatePositions
-> Position[]
```

这条链路表达的是：用户输入先变成交易草稿，校验通过后成为正式交易，交易进入总账本，再由 positionService 或 calculator 计算当前持仓。

## 典型使用场景

- 页面初始化时提供一份 `initialLedgerData`。
- 新增交易后生成新的 LedgerData。
- 交易列表读取 `ledgerData.trades`。
- 资产汇总和持仓表读取由 LedgerData 计算出来的结果。

## 局限性

LedgerData 放在 React state 里时只是临时数据，刷新页面会丢失。它解决的是“页面运行期间有统一数据源”的问题，不等于已经完成持久化。

另外，LedgerData 不应该变成所有逻辑的垃圾桶。交易校验、持仓计算、手续费规则等逻辑仍然应该拆到清晰的 service、validator 或 calculator 中。

## 和其他概念的关系

- [[React State（React 状态）]] 可以暂时保存 LedgerData，让页面由账本数据驱动。
- [[useState（React 状态 Hook）]] 是在 React 组件里声明 LedgerData state 的常见方式。
- [[Derived Data（派生数据）]] 解释为什么 `Position[]` 应该由 `Trade[]` 计算，而不是手动保存成第二套事实。
- [[为什么账本页面不能继续使用写死数据]] 解释为什么页面应该读取 LedgerData，而不是维护假数据。

## 关联

- [[React State（React 状态）]]
- [[useState（React 状态 Hook）]]
- [[Derived Data（派生数据）]]
- [[TypeScript（类型化 JavaScript）]]
- [[为什么账本页面不能继续使用写死数据]]
- [[为什么 Position 不应该作为事实数据保存]]
