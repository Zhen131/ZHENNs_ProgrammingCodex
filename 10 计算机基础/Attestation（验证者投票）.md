---
type: 技术卡片
status: 草稿
aliases: [Attestation, 验证者投票, 投票, Slot, 时隙, Epoch, 轮次, Committee, 委员会, Checkpoint, 检查点, Aggregator, LMD GHOST, Casper FFG, Slashing Protection]
created: 2026-10-11
updated: 2026-10-11
---

# Attestation（验证者投票）

## 一句话

Attestation 是 Validator 每个 epoch 必须发出的一张签名选票，内容是"我看到的最新区块是哪个、我支持哪个检查点"。它由 validator client 自动发出，不需要人手动点。

## 背景：上百万人不能同时投票

ETH 有上百万个 Validator。如果每 12 秒全体同时投一次票，网络会被压垮。

所以协议把投票摊开：每个 Validator 每个 epoch 只投一次，而且只在自己被分到的那个 slot 里投。

## 核心机制

### 两个时间单位

- **Slot（时隙）**：12 秒，对应一个区块位。
- **Epoch（轮次）**：32 个 slot，共 6.4 分钟。每个 Validator 每个 epoch 投一次票。

不要混：slot 是出块节奏，epoch 是投票和结算的周期。

### 谁在哪个 slot 投

每个 epoch 开始前，协议用 [[RANDAO（链上随机数）]] 的种子把全体 Validator 随机打乱，分进若干 Committee（委员会）。每个 Validator 被分到本 epoch 里的某一个 slot，客户端提前知道时间表，到点自动行动。

### 一个 slot 里发生什么

1. 0 秒：这个 slot 的 Proposer 广播新区块。
2. 约 1/3 处（约 4 秒）：被分到这个 slot 的 Validator 检查区块，签名并广播自己的 attestation。
3. 约 2/3 处（约 8 秒）：Aggregator（聚合者）把同一委员会的大量选票合成一个，减轻网络负担。
4. 之后的区块：Proposer 把这些选票打包上链，你拿到奖励。

这三个时间点我是按协议规范的印象写的，待确认最新版本。

### 一张票里装什么

用你的 BLS 签名密钥签名，同时表达三件事：

- head vote：我认为当前最新的区块是哪个。fork choice 规则 LMD GHOST 用它选链头。
- source：我认为上一个已被证明合理的 Checkpoint（检查点）是哪个。
- target：我支持本 epoch 的哪个检查点。

后两项属于 Casper FFG，用来达成 [[Finality（最终性）]]。检查点就是每个 epoch 的第一个区块。

## 局限性

掉线的那一轮，票就丢了，只会被小额罚款，不严重。

真正危险的是同一套密钥同时在两台机器上跑。两边各投一次，可能出现自相矛盾的票，被判作恶，触发 Slashing。客户端有一个 slashing protection 数据库专门防这件事，换机器时必须带上它。

## 关联

- [[Proof of Stake（权益证明）]]：Attestation 是 Validator 拿奖励、尽义务的主要方式。
- [[RANDAO（链上随机数）]]：谁在哪个 slot、哪个委员会投票，由它的随机种子决定。
- [[Finality（最终性）]]：同一个 target 攒够 2/3 质押量的票，检查点才会 justified，再过一个 epoch 才 finalized。
