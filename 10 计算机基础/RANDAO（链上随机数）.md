---
type: 技术卡片
status: 草稿
aliases: [RANDAO, 链上随机数, randao_reveal, randao mix, Last Revealer Problem, 最后揭示者问题, Selective Abort, 选择性中止, VDF, Verifiable Delay Function, 可验证延迟函数]
created: 2026-10-11
updated: 2026-10-11
---

# RANDAO（链上随机数）

## 一句话

RANDAO 让每个 Proposer 在出块时交一个只有自己能产生的数，全网把这些数混在一起，当作共同的随机种子。只要有一个人没和别人串通，别人就算不出最终结果。

## 背景：谁来掷骰子

协议要在下个 epoch 开始前决定"谁当 Proposer、谁进哪个委员会"。这得靠随机数。

如果由某一个节点掷骰子，结果就由他说了算。如果每个节点各自掷，大家的结果不一样，共识就崩了。

所以链上随机数要同时满足三条：全网算出同一个结果（deterministic），结果事先没人能预测（unpredictable），没人能影响结果（unbiasable）。

"计算机只有伪随机数"不是问题所在。伪随机函数没问题，问题是种子由谁定。

早期有人用智能合约做 commit-reveal：先提交哈希，再揭示秘密。最后一个揭示的人可以拒绝揭示，结果就被他影响。RANDAO 在 ETH 里换了一种做法。

## 核心机制

1. 每个区块里带一个 `randao_reveal`，它是 Proposer 用自己的私钥对当前 epoch 编号签的 BLS 签名。
2. 签名是确定性的：同一个私钥签同一个编号，结果永远一样。Proposer 不能挑一个对自己有利的值，别人没有他的私钥，也算不出来。
3. 协议维护一个 randao mix，每来一个区块更新一次：`mix = mix XOR hash(randao_reveal)`。XOR（异或，相同为 0、不同为 1）的特点是，只要有一个输入不可预测，结果就不可预测。
4. 种子提前定好。给某个 epoch 排班用的是倒数第二个 epoch 末尾的 mix，所以 Validator 至少有一个完整 epoch 提前知道自己的任务。

## 局限性

RANDAO 能做到 unpredictable，做不到完全 unbiasable。

一个 epoch 最后一个 Proposer 手里有两个选择：交出自己的 reveal，或者不出块。他能提前算出两种结果，挑对自己有利的那个。这叫 Last Revealer Problem（最后揭示者问题）。

末尾连续几个 slot 都归同一个攻击者，选择就更多，k 个尾部 slot 最多有 2^k 种结果。代价是每放弃一次就丢掉一个区块的奖励。

eth2book 的结论是：RANDAO 可以被影响，但没到破坏协议的程度。想系统性地占领末尾 slot，质押量要接近一半。

根治思路是 VDF（可验证延迟函数）：把 mix 再丢进一个必须花固定时间才能算完、无法加速的函数，这样最后一个人必须在不知道结果的时候就决定出不出块。来源写的是目前 ETH 没有落地的计划，待确认最新进展。

## 容易混淆

**Unpredictable 和 unbiasable 是两件事。** 前者是"事先没人知道结果"，后者是"没人能影响结果"。RANDAO 满足前者，对后者只做到了"影响很小、要花钱"。

## 关联

- [[为什么链上随机数很难做到公平]]：从痛点出发，讲清楚为什么这件事难，以及一个带数字的例子。
- [[Proof of Stake（权益证明）]]：RANDAO 的结果决定 Proposer 的人选。
- [[Attestation（验证者投票）]]：谁在哪个 slot 投票，也由这个种子打乱分配。
