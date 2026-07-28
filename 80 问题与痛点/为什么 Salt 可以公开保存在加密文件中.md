---
type: 问题卡片
status: 草稿
tags: [类型/问题卡片, 问题/概念辨析, 领域/计算机基础, 主题/密码学, 层级/基础, 状态/待深化]
aliases: [为什么盐可以公开, Salt 为什么不需要保密, 加密文件为什么保存 Salt]
created: 2026-07-28
updated: 2026-07-28
---

# 为什么 Salt 可以公开保存在加密文件中

## 痛点

刚接触 Salt（盐）时，很容易产生这样的直觉：

> 既然 Salt 和 Password（密码）一起生成 Key（密钥），把 Salt 写进文件，不就等于把秘密泄露了一半吗？

这个直觉把 Salt 当成了第二个 Password。但 Salt 的主要职责不是增加一份秘密，而是让每一次密码派生具有独特性。

## 核心原因

在 [[Password-Based Encryption（基于密码的加密）]] 中，`PBKDF2` 这类 KDF 会使用 Password、Salt 和成本参数派生 Key。

Salt 可以公开，是因为系统的安全边界仍然建立在以下条件上：

- Password 需要保密；
- 攻击者不能只靠 Salt 直接得到 Key；
- KDF 会让每一次密码猜测都要付出计算成本；
- 不同文件使用不同 Salt 后，即使 Password 相同，派生出的 Key 通常也不同。

Salt 的价值主要是阻止攻击者把针对一个 Salt 的预计算结果，直接复用到大量其他文件上。它不是用来替代强密码，也不是必须隐藏的第二把钥匙。

## 为什么必须随文件保存

KDF 是确定性的：只有输入和参数相同，才能重新派生出相同的 Key。

```text
第一次：
Password + Salt S1 + 相同参数 → Key K1

重新打开：
Password + Salt S1 + 相同参数 → 仍然得到 Key K1
```

如果软件关闭后丢失 Salt，下一次就无法重新派生出原来的 Key。因此，Salt 通常会和 KDF 名称、KDF 参数、IV（初始化向量）及 Ciphertext（密文）一起保存在加密文件中。

Password 和 Key 才是需要保密的内容；Salt 需要的是正确生成、避免不必要的重复，并在解密时能够准确取回。

## 修改 Salt 会发生什么

如果攻击者只把文件中的 Salt 从 `S1` 改成 `S2`，而原有 Ciphertext 和 Authentication Tag（认证标签）没有改变：

```text
正确 Password + 错误 Salt S2
              ↓
         派生出错误 Key
              ↓
      AES-GCM 认证解密失败
```

这通常破坏的是文件可用性，并不会让攻击者因此获得原来的明文，也不会让攻击者仅靠修改 Salt 就伪造一份能通过原密码认证的任意账本内容。

但是，应用不能因为“篡改最终会导致解密失败”就提前显示“已保存”。如果保存成功的含义包括“磁盘文件可被正确读回”，程序仍需要重新读取并验证实际文件。

## Salt 和 IV 的最小区别

| 对比 | Salt | IV |
|---|---|---|
| 所处阶段 | Password 派生 Key | Key 加密某一次数据 |
| 交给谁使用 | PBKDF2 等 KDF | AES-GCM 等加密算法 |
| 是否需要保密 | 不需要 | 不需要 |
| 为什么保存 | 以后派生同一把 Key | 以后解密对应 Ciphertext |

一句话记忆：

> Salt 帮助 Password 生成 Key，IV 帮助 Key 完成某一次加密。

## 我的理解

Salt 可以先理解成“给密码加的一份独特小料”。这份小料不是秘密配方，而是为了让同一个 Password 在不同文件里不要总做出同一把 Key。

真正负责上锁的是 Key；Salt 负责让制钥匙的过程具有独特性。

## 关联

- [[Password-Based Encryption（基于密码的加密）]]：Salt 所在的完整密码加密流程。

## 参考

- [NIST SP 800-132：Password-Based Key Derivation](https://csrc.nist.gov/pubs/sp/800/132/final)
- [MDN：PBKDF2 的 Salt 参数](https://developer.mozilla.org/en-US/docs/Web/API/Pbkdf2Params)
