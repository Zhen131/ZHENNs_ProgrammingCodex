---
type: 技术卡片
status: 草稿
aliases: [Transaction, TX, Tx, 交易, 区块链交易, 转账, Transfer, TX Hash, 交易哈希, Mempool, 内存池, Gas, Gas Limit, Gas Price, Gwei, ERC-20 Transfer, Pending]
created: 2026-10-11
updated: 2026-10-16
---

# Transaction（区块链交易）

## 一句话

Transaction（TX）是一条用你的私钥签过名的指令："我这个账户，要做某件事。"转账只是其中最常见的一种。

## 背景：老师在热钱包里点了一次转账

你在 [[Crypto Wallet（加密钱包）]] 里填收款地址和金额，点 Confirm。几秒后，界面显示 Pending，过一会儿变成 Success。这中间发生了什么，就是 TX 的完整生命周期。

## 核心机制

1. **填信息**：收款地址和金额。
2. **钱包生成 TX**：自动填好 [[Nonce（账户交易序号）]]、gas 相关字段，并估算手续费。
3. **签名 sign**：你点 Confirm 时，钱包用本地私钥对这条 TX 签名。私钥不离开设备，发出去的只有签过名的 TX。
4. **广播 broadcast**：钱包把签名后的 TX 发给一个节点，节点转发给全网，大家把它放进 mempool（内存池，还没上链的 TX 排队的地方）。
5. **被打包**：Proposer 从 mempool 里挑 TX 放进区块，手续费高的优先。见 [[Proof of Stake（权益证明）]]。
6. **确认**：Validator 通过 [[Attestation（验证者投票）]] 投票，区块最终 finalized，转账才不可逆。见 [[Finality（最终性）]]。

### 在区块浏览器里看一条 TX

在 Etherscan 这类区块浏览器里能看到这些字段：

| 字段 | 意思 |
|---|---|
| TX Hash | 这笔交易的唯一编号，像快递单号 |
| Status | Pending（在内存池）、Success、Failed |
| Block | 被打包进了哪个区块 |
| From / To | 发送方和接收方 |
| Value | 转了多少 ETH |
| Nonce | 这是发送方账户的第几笔 TX |
| Gas Limit | 你愿意最多消耗多少计算量 |
| Gas Price（单位 Gwei） | 每单位计算量你出的价 |
| Transaction Fee | 实际花了多少手续费 |

EIP-1559 之后，多数 TX 用 `maxFeePerGas` 和 `maxPriorityFeePerGas` 两个字段，钱包界面常常简化成一个 gas price。

### 转 ETH 和转代币不一样

转 ETH：To 是收款人，Value 是金额。

转 ERC-20 代币（比如 USDT）：To 是**代币合约的地址**，Value 是 0，真正的收款人和金额被编码在 data 字段里。看到 To 是个合约地址不要奇怪。

## 局限性

TX 一旦 finalized 就撤不回。地址填错、转错链，没有"退款"按钮。

Pending 的 TX 如果手续费太低，会一直卡在内存池，而且会连带卡住后面所有 TX，见 [[Nonce（账户交易序号）]]。

## 容易混淆

**Failed 不等于没花钱。** TX 被打包进区块但执行失败，手续费照扣，Nonce 也照样 +1。

**TX Hash 不是地址。** 地址标识账户，TX Hash 标识一笔交易。

## 关联

- [[Crypto Wallet（加密钱包）]]：钱包负责保管私钥、生成并签名 TX。
- [[Nonce（账户交易序号）]]：TX 里的序号字段，决定顺序、防重放、能替换卡住的 TX。
- [[Race Attack（竞速攻击）]]：两笔冲突的 TX 同时在内存池里，只有一笔能被打包。
- [[Finality（最终性）]]：TX 从 Pending 到不可逆的过程。
- [[Block Header（区块头）]]：TX 被打包后，整块交易汇成 Merkle Root 写进区块头。
- [[Proof of Work（工作量证明）]]：比特币里从 mempool 挑 TX、打包出块的过程。
