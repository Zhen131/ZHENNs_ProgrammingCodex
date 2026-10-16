---
type: 技术卡片
status: 草稿
aliases: [Block Header, 区块头, Block, 区块, Block Structure, 区块结构, Previous Block Hash, prevBlockHash, Merkle Root, 默克尔根, Merkle Tree, 默克尔树, Bits, Timestamp, TRX count, Transaction Count, 交易数量, Block Identifier, 区块标识, Tamper-evident, 防篡改]
created: 2026-10-16
updated: 2026-10-16
tags: [主题/区块链]
---

# Block Header（区块头）

## 一句话

Block Header 是一个区块的"封面"：80 个字节，里面写着上一块是谁、这一块装了哪些交易的总指纹、什么时间、多难、试中的号码是多少。整个区块的身份证号，就是这张封面的哈希。

## 背景：有人想偷偷改一笔旧账

假设一年前有一笔"小王转给你 1 BTC"，有人想把它改成 0.1。区块链要做到：改得了，但一改所有人都会发现。

## 核心机制

### 比特币区块头里的六样东西

| 字段 | 大小 | 写的是什么 |
|---|---|---|
| Version | 4 字节 | 这块遵守哪一版规则 |
| Previous Block Hash | 32 字节 | 上一个区块头的哈希。区块就是靠它串成链的 |
| Merkle Root | 32 字节 | 这一块里所有交易汇成的一个哈希 |
| Timestamp | 4 字节 | 出块时间 |
| Bits | 4 字节 | 压缩写法的 target，也就是这一块的难度门槛 |
| Nonce | 4 字节 | 矿工试中的那个数 |

课件的图在这六样下面还画了 **TRX count**。TRX 是 transaction 的缩写，TRX count 就是"这个区块里装了几笔交易"。严格说它紧跟在区块头后面、在交易列表前面，不在那 80 字节里，也不参与挖矿的哈希。它和难度没有关系。

### Merkle Root 怎么来

一块里有几千笔交易。每笔先算哈希，再两两合并算哈希，一层层往上，最后剩一个，就是 Merkle Root。任何一笔交易变了，它就变。它是打包交易时算一次就有的，矿工不用猜它。

### 为什么改了会被发现

1. 改一笔旧交易 → 那一块的 Merkle Root 变了。
2. Merkle Root 变了 → 那一块的区块头哈希变了。
3. 下一块里存的 Previous Block Hash 还是旧值 → 对不上，所有节点都看得出来。

想不被发现，就得把后面每一块都重新挖一遍，还得追上全网的进度。在 [[Proof of Work（工作量证明）]] 下这贵到不现实。这种"改了必露馅"叫 tamper-evident。

### Block Identifier（区块标识）

一个区块的唯一编号 = 它区块头的 `SHA256(SHA256(header))`。不是时间戳，也不是第几块。

## 容易混淆

**区块之间靠 Previous Block Hash 连接**，不是靠 Timestamp，也不是靠区块高度。

**Bits 和 Nonce 都在区块头里，但一个是题目，一个是答案。** Bits 是网络规定的门槛，所有矿工都一样；Nonce 是每个矿工自己试出来的。

## 关联

- [[Cryptographic Hash Function（密码学哈希函数）]]：区块头能防篡改，全靠哈希"输入一变、输出全变"。
- [[Proof of Work（工作量证明）]]：挖矿就是不停改区块头里的 Nonce，让区块头哈希小于 Bits 表示的 target。
- [[Transaction（区块链交易）]]：区块里装的就是 TX，Merkle Root 是它们的总指纹。
- [[Longest Chain Rule（最长链规则）]]：两个区块指向同一个 Previous Block Hash，就是分叉。
