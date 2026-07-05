---
type: 问题卡片
status: 草稿
tags: [类型/问题卡片, 问题/前端架构, 领域/Web与网络, 语言/JavaScript]
aliases: [为什么不要手动操作 DOM, React 为什么不用 querySelector 改页面, 手动 DOM 更新的问题]
created: 2026-07-05
updated: 2026-07-05
---

# 为什么 React 不推荐手动操作 DOM

## 痛点

直接操作 [[DOM（文档对象模型）]] 的思路是：数据变了，开发者自己找到页面元素，然后一个一个修改。小页面里这很直观，但复杂业务页面会很容易漏改。

账本页面新增一笔 BTC 交易后，可能同时影响交易列表、BTC 持仓数量、平均成本、资产汇总和未实现盈亏。如果这些位置都靠手动 DOM 更新，一处漏掉就会导致页面显示不一致。

## 以前怎么解决

传统 JavaScript 可能会写成：

```js
const tradeList = document.querySelector("#trade-list");
const btcAmount = document.querySelector("#btc-amount");
const avgCost = document.querySelector("#avg-cost");

tradeList.innerHTML += "<li>买入 BTC 0.01</li>";
btcAmount.innerText = "0.01 BTC";
avgCost.innerText = "$60000";
```

这段代码的问题不是“不能用”，而是页面依赖越多，手动同步成本越高。

## 技术演进

[[React（React UI 库）]] 把思路改成：

```text
用户操作
-> 修改 React State
-> React 根据新状态重新渲染页面
```

开发者主要维护数据状态，而不是到处手动找 DOM 节点。比如账本项目里，新增交易后更新 [[LedgerData（账本数据对象）]]，再由页面根据 `ledgerData.trades` 和计算出的持仓结果重新显示。

## 相关技术

- [[DOM（文档对象模型）]]
- [[React（React UI 库）]]
- [[React State（React 状态）]]
- [[useState（React 状态 Hook）]]
- [[LedgerData（账本数据对象）]]

## 我的理解

React 不是说 DOM 不重要，而是把“我手动改页面”升级成“我维护数据，页面是数据的结果”。这样更适合账本这类多个区域依赖同一份数据的复杂页面。

## 关联

- [[为什么账本页面不能继续使用写死数据]]
- [[为什么前端项目要把界面、逻辑、样式和框架分层]]
