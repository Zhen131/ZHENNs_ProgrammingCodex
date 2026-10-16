---
type: 技术卡片
status: 草稿
aliases: [Proof of Stake, PoS, 权益证明, Staking, 质押, Validator, 验证者, Slashing, 罚没, Inactivity Leak, Liquid Staking, 流动性质押, Solo Staking]
created: 2026-10-11
updated: 2026-10-16
---

# Proof of Stake（权益证明）

## 一句话

Proof of Stake（PoS）让你把币锁起来当押金，协议按押金多少挑人出块、投票。干得好有奖励，作恶就没收押金。Proof of Work 比谁烧的电多，PoS 比谁押的钱多。

## 背景：只靠电费撑得住安全吗

Proof of Work 里，攻击者要买算力、交电费。电费花掉就花掉了，协议没办法在你作恶之后再多罚你一分。

PoS 换了一种成本。你想参与，先得把一大笔钱押在链上。一旦被协议抓到作恶，这笔钱直接烧掉。攻击不再只是"花钱"，而是"拿本金去赌"。

## 核心机制

以 ETH 为例，自己当 Validator（验证者）的流程叫 Solo Staking（自己质押）：

1. 准备 32 ETH，再准备一台常开的机器。机器上跑 execution client（执行层客户端，处理交易和状态，例如 Geth）、consensus client（共识层客户端，负责 PoS 共识，例如 Lighthouse），以及保管签名密钥的 validator client。
2. 生成两套密钥。signing key 放在线上，用来给区块和投票签名。withdrawal credentials 指向你的提款地址，本金和收益最终回到这里。
3. 把 32 ETH 转进 deposit contract（官方存款合约）。
4. 在 activation queue（激活队列）里排队。人多的时候要等几小时到几周。激活之后你才算 Validator。
5. 开始干活。每个 epoch 做一次 [[Attestation（验证者投票）]]，偶尔被随机选中当 Proposer（出块者），打包区块。被选中的概率和 effective balance（有效质押量）成正比，随机性来自 [[RANDAO（链上随机数）]]。
6. 收奖励。来源有投票奖励、出块奖励，以及出块时拿到的交易小费和 MEV（最大可提取价值，靠排列交易顺序多赚的钱）。
7. 想走就发一条 voluntary exit（自愿退出）消息，进 exit queue（退出队列），等一段时间后本金可以提走。

### 罚款

| 情况 | 后果 |
|---|---|
| 离线、投票晚了 | 小额罚款 |
| 链很久无法 finalize，你一直离线 | Inactivity Leak（怠速泄漏）：离线者被加速扣款，直到在线的人重新凑够 2/3 |
| 同一个高度签两个不同的区块，或投前后矛盾的票 | Slashing（罚没）：立刻没收一部分押金，强制踢出，之后还有一次罚款。同一时间作恶的人越多，罚得越重 |

初始罚没的具体比例随协议升级调整过，待确认最新数字。

### 不想自己跑机器

- 流动性质押 Liquid Staking（Lido、Rocket Pool 这类）：存任意数量 ETH，换回一个会增值的代币（stETH、rETH），还能拿去做 DeFi。风险在智能合约漏洞和协议过度集中。
- 交易所质押：最省事，但币在交易所手里，要承担托管风险。

### 协议升级带来的变化

2025 年 5 月 7 日的 Pectra 升级（EIP-7251）把单个 Validator 的有效质押上限从 32 ETH 提到最多 2048 ETH，要把 withdrawal credentials 换成新类型才生效。EIP-7002 让提款地址也能直接触发退出。

年化收益大约 3% 到 4%，随全网质押量变化，待确认最新数字。

## 局限性

激活和退出都要排队，想快也快不了。

同一套 signing key 不能在两台机器上同时跑，否则可能被判 Slashing。迁移机器时要把客户端的 slashing protection 数据库一起搬走。

## 容易混淆

**质押不是把币借出去。** 币锁在合约里，你不能花，但它仍然是你的，退出后拿回来。

**攻击门槛不是 51%。** PoW 看算力是否过半。PoS 看质押量：控制 1/3 就能让链无法 finalize，控制 2/3 就能单方面决定哪个检查点被 finalize。要回滚一个已经 finalize 的区块，至少有 1/3 的质押量要被 slashing。见 [[51% Attack（51% 攻击）]] 和 [[Finality（最终性）]]。

## 关联

- [[Attestation（验证者投票）]]：Validator 最日常的工作，每个 epoch 一次，自动完成。
- [[RANDAO（链上随机数）]]：决定谁当 Proposer、进哪个委员会的随机数从这里来。
- [[Finality（最终性）]]：投票攒到 2/3 质押量，区块才变成不可逆。
- [[51% Attack（51% 攻击）]]：PoS 里对应的攻击门槛是 1/3 和 2/3。
- [[Crypto Wallet（加密钱包）]]：提款地址对应的私钥，同样由钱包保管。
- [[Proof of Work（工作量证明）]]：PoS 用押金代替 PoW 的电费，比特币没有押金，靠电费和拉黑挡捣乱。
