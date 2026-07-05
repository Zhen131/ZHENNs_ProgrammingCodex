---
type: 问题卡片
status: 草稿
tags: [类型/问题卡片, 问题/数据建模, 领域/软件工程, 领域/数据与存储]
aliases: [为什么持仓不应该手动保存, 为什么 Position 应该计算, Position 和 Trade 的关系]
created: 2026-07-05
updated: 2026-07-05
---

# 为什么 Position 不应该作为事实数据保存

## 痛点

`Position[]` 表示当前持仓、平均成本、市值和未实现盈亏。它看起来像一组重要数据，但在账本项目里，它不是用户直接录入的事实，而是根据交易记录和价格快照计算出来的结果。

如果把 `Trade[]` 和 `Position[]` 都当成事实保存，就可能出现两套数据冲突。

## 以前怎么解决

初学时很容易觉得“页面要显示什么，就保存什么”。这种想法在简单页面里省事，但账本系统会因此失去单一事实来源。

比如：

```text
Trade[] 显示我买了 0.01 BTC
Position[] 却显示我持有 0.02 BTC
```

这时系统就不知道谁才是真的。

## 技术演进

更稳定的建模方式是区分事实数据和 [[Derived Data（派生数据）]]：

- `Trade[]`：什么时候买、买了多少、价格多少、手续费多少。
- `PriceSnapshot[]`：某个时间点的价格事实。
- `Position[]`：根据交易和价格计算出来的结果。

所以账本链路应该是：

```text
LedgerData.trades + LedgerData.priceSnapshots
-> calculatePositions(...)
-> Position[]
-> 页面展示
```

## 相关技术

- [[Derived Data（派生数据）]]
- [[LedgerData（账本数据对象）]]
- [[React State（React 状态）]]
- [[TypeScript（类型化 JavaScript）]]

## 我的理解

账本系统里应该优先保存不可替代的事实，再从事实计算结果。`Position[]` 可以展示、可以缓存，但不能随便变成和 `Trade[]` 平行的第二套真相。

## 关联

- [[为什么账本页面不能继续使用写死数据]]
