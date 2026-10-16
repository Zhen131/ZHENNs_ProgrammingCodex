---
type: 技术卡片
status: 草稿
aliases: [Nonce, 账户 Nonce, 交易序号, 账户交易序号, Account Nonce, Replay Protection, 重放保护, Speed up, Cancel, nonce too low, replacement transaction underpriced]
created: 2026-10-11
updated: 2026-10-16
---

# Nonce（账户交易序号）

## 一句话

Nonce 是账户自己的计数器，从 0 开始，每发出一笔 TX 就加 1。下一笔 TX 必须正好用下一个编号，不能跳，也不能重复。

## 背景：钱包里一笔 TX 卡住，后面全都不动

你发了 5 笔 TX，第 3 笔手续费给低了，一直 Pending。后面第 4、5 笔也跟着不动。

原因就是 Nonce：节点按编号顺序处理，前一个没走，后一个不能先走。

类比：支票本上的编号。第 5 号还没兑付，第 6 号不会提前兑。第 5 号兑付过了，再拿同一张来，银行不认。

## 核心机制

节点收到你的 TX 时，拿 TX 里的 nonce 和**链上你这个账户当前的 nonce** 比较。链上的值表示你已经发过多少笔，也是你下一笔该用的编号。假设链上是 5：

| 你发的 TX | 节点怎么处理 | 常见报错 |
|---|---|---|
| nonce = 4（用过了） | 直接拒绝 | `nonce too low` |
| nonce = 5（正好是下一个） | 可以执行，进内存池等打包 | 无 |
| nonce = 6（跳号） | 放进队列等，要等 5 先上链 | 有的工具会报 `nonce too high` |
| 又一条 nonce = 5 | 和之前那条冲突，只有一条能留下 | `replacement transaction underpriced` |

### 它同时做三件事

- **防重放 replay protection**：别人拿到你已上链的那条签名 TX，再广播一遍，节点一看 nonce 已经用过，直接拒绝。nonce 在你的签名里面，别人改不了。
- **保证顺序**：先发的一定先执行。先 approve 授权、再 swap 兑换，顺序反了会失败。
- **能替换卡住的 TX**：nonce 就是一个槽位，同一个槽位只放一条。用**同一个 nonce** 发一条出价更高的 TX，就能顶掉旧的。

钱包里的 **Speed up** 就是同样内容、更高手续费。**Cancel** 是用同一个 nonce 给自己转 0 ETH，手续费更高，原来那笔就被顶掉了。节点通常要求新手续费比旧的高至少 10%，否则报 `replacement transaction underpriced`，具体比例因节点而异，待确认。

### 几个细节

- 失败的 TX 也会消耗 nonce。TX 被打包但执行失败，手续费照扣，nonce 照样 +1。
- 没被打包不消耗。TX 只停在内存池，被节点丢弃，nonce 没用掉，可以重用。
- nonce 存在链上，属于账户状态，不在钱包里。钱包发 TX 前向节点查当前值。
- 每个账户独立计数，你的 nonce 5 和别人的毫无关系。
- 新合约的地址由"部署者地址 + 部署时的 nonce"算出，所以部署前就能算出合约会在哪个地址。

## 局限性

顺序是它最大的优点，也是它最大的代价：

- 队头阻塞（head-of-line blocking）：一条 TX 卡住，后面全卡。
- 同一个账户很难并行发多笔 TX，要自己管理 nonce。
- 多个设备共用一个账户容易冲突。

后来有改进：有的合约用无序 nonce（不要求连续，比如 Uniswap 的 Permit2），account abstraction（ERC-4337）里有二维 nonce（用一个 key 分出多条并行序列）。这两点我没核实最新规范，待确认。

## 容易混淆

**挖矿里的 nonce 是另一回事。** PoW 矿工不断试的那个数，用来凑出满足难度的哈希，和账户 nonce 只是同名。

**收钱不加 nonce。** 只有你自己发出一笔 TX 才加 1。别人转给你，你的 nonce 不动。去质押、调合约都是你发的 TX，会加。

**nonce 防的是重放，不是冒签。** 别人没有你的私钥，签不出你的签名，验签那一步就挡住了。nonce 挡的是把你签过的真 TX 复制再发一遍。

**比特币没有账户 nonce。** 比特币用 UTXO 模型：每个币是一张独立的"钞票"，花掉就作废，天然防重放。账户 nonce 是 account-based 模型（ETH 用的）才需要的设计。

## 关联

- [[为什么账户交易需要 nonce]]：为什么用一个整数就解决了去重、排序、替换，对比了几种笨办法。
- [[Transaction（区块链交易）]]：Nonce 是 TX 里的一个字段，TX 的完整流程在那张卡。
- [[Crypto Wallet（加密钱包）]]：钱包发 TX 前要向节点查 nonce，多设备共用账户时会冲突。
- [[Proof of Work（工作量证明）]]：同名的挖矿 nonce 在那张卡，别和账户 nonce 混。
