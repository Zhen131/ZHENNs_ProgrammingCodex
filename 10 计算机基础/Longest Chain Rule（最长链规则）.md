---
type: 技术卡片
status: 草稿
aliases: [Longest Chain Rule, 最长链规则, Heaviest Chain, 最重链, Fork, 分叉, Orphan Block, Stale Block, 孤块, 过期块, Fork Choice]
created: 2026-10-11
updated: 2026-10-16
---

# Longest Chain Rule（最长链规则）

## 一句话

Longest Chain Rule 是节点遇到分叉时的裁判规则：永远认最长的那条链。没有中央裁判，每个节点各自按这条规则判断，也会得出同样的结论。

## 背景：两个矿工同时挖出了块

两个矿工几乎同时挖出了第 100 号区块，网络暂时分成两派，各认各的。没有人可以宣布"哪个对"。

规则很简单：谁先在自己那条链上再挖出 101 号，谁的链就更长，所有节点都切换过去。输掉的那个 100 号块叫 orphan block（孤块，也叫 stale block），里面的交易回到等待区，重新排队。

## 核心机制

节点收到多条竞争的链，选累计 proof of work 最多的那条，也就是最长的。这样每个诚实节点独立算出来，结论是同一条。

这条规则的另一面是：**谁能造出更长的链，谁就说了算**。后面这些攻击都在利用它：

- [[51% Attack（51% 攻击）]]：过半算力，能一直保持更长。
- [[Selfish Mining（自私挖矿）]]：藏起区块，在合适的时机放出，让诚实区块变成孤块。

## 容易混淆

**"最长"其实是累计工作量最大。** 实际比的不是区块数，而是链上累计的工作量，叫 heaviest chain。多数情况下两者一致，所以习惯叫最长链。

**PoS 链不用它。** ETH 的 PoS 用 LMD GHOST（按 Validator 最新投票的权重选链头）加 Casper FFG（定 finalized），见 [[Attestation（验证者投票）]] 和 [[Finality（最终性）]]。

## 关联

- [[51% Attack（51% 攻击）]]：最长链规则让"过半算力"变成"永远赢"。
- [[Selfish Mining（自私挖矿）]]：利用平局和领先，让诚实区块变成孤块。
- [[Finality（最终性）]]：PoW 下"越长越安全"，是 probabilistic finality 的来源。
- [[Attestation（验证者投票）]]：PoS 里选链头靠投票权重，而不是链的长度。
- [[Proof of Work（工作量证明）]]："累计工作量"是怎么算出来的，target 和难度在那张卡。
- [[Block Header（区块头）]]：两个区块指向同一个 Previous Block Hash，就是分叉。
