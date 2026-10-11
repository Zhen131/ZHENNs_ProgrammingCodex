---
type: 技术卡片
status: 草稿
aliases: [Finality, 最终性, 最终确定性, Confirmation, 确认数, Probabilistic Finality, 概率最终性, Casper FFG, Justified, Finalized, Economic Finality, 经济最终性]
created: 2026-10-11
updated: 2026-10-11
---

# Finality（最终性）

## 一句话

Finality 说的是一笔交易有多难被撤回。比特币这类 PoW 链靠"多等几个块，越来越安全"，ETH 这类 PoS 链则由协议明确宣布"这个区块不可逆了"。

## 背景：商家什么时候能放心发货

你开咖啡店，客户转来一笔钱。交易刚广播出去、还没进任何区块时，叫 0 confirmations（0 个确认），这时它随时可能被抢跑或替换，见 [[Race Attack（竞速攻击）]]。

进了一个区块，叫 1 confirmation（1 个确认）。这时仍可能因为分叉被回滚。再多一个块压在上面，回滚就更难一点。比特币社区习惯等 6 个确认再认为大额交易安全。这是习惯，不是协议规则。

这种"等得越久越安全，但永远不是 100%"的状态，叫 probabilistic finality（概率最终性）。

## 核心机制

ETH PoS 用 Casper FFG 给检查点一个明确的状态：

1. 每个 epoch，Validator 通过 [[Attestation（验证者投票）]] 给检查点投票。
2. 同一个 target 拿到超过 2/3 质押量的票，这个检查点变成 justified。
3. 再过一个 epoch，它被下一个检查点确认，变成 finalized。

从投票到 finalized 要两个 epoch，约 12.8 分钟。因为流程是流水线，每个 epoch 都会 finalize 一个新检查点。

要回滚一个已经 finalized 的区块，至少 1/3 的质押量要被 slashing。这叫 economic finality（经济最终性）：不是不可能，而是代价高到烧掉三分之一的押金。

## 容易混淆

**Confirmation 和 Finality 不是一回事。** 确认数是数"这笔交易上面压了几个块"，是个计数。Finality 是协议给的一个状态，到了就是到了。

## 关联

- [[Race Attack（竞速攻击）]]：0 确认时的漏洞，等确认就是在换取更高的最终性。
- [[51% Attack（51% 攻击）]]：PoW 下，攻击者靠重写历史把已确认的交易推翻。
- [[Double Spending（双花）]]：Finality 越强，双花越难成功。
- [[Proof of Stake（权益证明）]]：Finality 依赖质押量的 2/3 和 1/3 门槛。
- [[Longest Chain Rule（最长链规则）]]：PoW 下"越长越安全"的来源。
