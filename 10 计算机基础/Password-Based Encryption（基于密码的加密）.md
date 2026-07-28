---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/计算机基础, 主题/密码学, 层级/基础, 状态/待深化]
aliases: [Password-Based Encryption, 基于密码的加密, PBE, 密码加密文件]
created: 2026-07-28
updated: 2026-07-28
---

# Password-Based Encryption（基于密码的加密）

## 一句话

`Password-Based Encryption（基于密码的加密）` 不是直接拿 Password（密码）去加密数据，而是先用 Password、Salt（盐）和 `KDF（密钥派生函数）` 生成真正的 Key（密钥），再由加密算法使用 Key 和 IV（初始化向量）加密明文。

## 背景：为什么不能直接把密码当成 Key

用户选择的密码通常长短不一，而且可能来自常见单词、生日或重复组合，不适合直接充当加密算法需要的 Key。

Password-Based Encryption 会在两层工作之间做分工：

1. `PBKDF2` 这类 KDF 负责把 Password 变成符合要求的 Key。
2. `AES-GCM` 这类认证加密算法负责使用 Key 加密数据，并在解密时检查密文是否被修改。

Salt 属于第一层，IV 属于第二层。两者都可以随加密文件保存，但不能混为一谈。

## 核心流程

加密时：

```text
Password + Salt + KDF 参数
              ↓
     PBKDF2 等 KDF
              ↓
             Key

明文 + Key + 本次加密使用的 IV
              ↓
           AES-GCM
              ↓
   Ciphertext + Authentication Tag
```

重新打开文件时：

```text
Password + 文件中的 Salt + 相同 KDF 参数
                    ↓
               重新派生 Key

Ciphertext + Authentication Tag + Key + 文件中的 IV
                    ↓
             AES-GCM 解密与认证
                    ↓
                  明文
```

如果 Password、Salt、KDF 参数、Key、IV、Ciphertext 或 Authentication Tag 对不上，认证解密就应失败，而不是返回一份“看起来还能用”的明文。

## 各个角色分别负责什么

| 名称 | 负责什么 | 是否需要保密 | 加密文件通常是否保存 |
|---|---|---|---|
| Password（密码） | 用户能够记住或输入的秘密 | 是 | 否 |
| Salt（盐） | 让 KDF 针对这份数据派生 Key | 否，但应为每次派生正确生成 | 是 |
| Key（密钥） | 真正交给加密算法使用的秘密 | 是 | 通常不写入同一份加密文件 |
| IV（初始化向量） | 区分同一把 Key 下的不同加密操作 | 否，但同一把 Key 下必须避免重复 | 是 |
| Ciphertext（密文） | 明文加密后的结果 | 否 | 是 |
| Authentication Tag（认证标签） | 让 AES-GCM 在解密时验证数据是否被修改 | 否 | 是，或与 Ciphertext 一起编码 |

在浏览器里的本地加密应用中，派生出来的 Key 常只在当前运行过程使用，不随密文写入文件。但“Key 永远只存在内存”不是密码学本身保证的规则，而是应用需要落实的密钥管理设计。

## Salt 和 IV 为什么不是一回事

```text
Salt：参与“从 Password 派生 Key”
IV：参与“使用 Key 加密这一次数据”
```

- Salt 是 KDF 的输入，不是 AES-GCM 的 IV。
- IV 是 AES-GCM 的输入，不负责把 Password 变成 Key。
- Salt 需要在以后派生同一把 Key 时再次使用。
- IV 需要在以后解密对应 Ciphertext 时再次使用。

它们都可以公开保存，也都需要正确生成，但它们处在流程的不同阶段，不能因为“都是随机数据”就共用同一个字段。

## 一个适合入门的类比

可以先把 Salt 理解为“给 Password 加的一份独特小料”，两者经过 KDF 这台制钥匙机器后，才得到真正开锁用的 Key。

这个类比只帮助记住分工：

```text
Password + Salt → Key
Key + IV + 明文 → Ciphertext
```

Salt 不会凭空把弱密码变成强秘密。它主要让相同 Password 在不同文件中派生出不同的 Key，并让攻击者难以把一次预计算结果直接复用到所有文件；抵抗密码猜测还依赖密码质量和 KDF 的成本参数。

## 在加密文件中的样子

一个简化的文件结构可能是：

```json
{
  "kdf": {
    "name": "PBKDF2",
    "saltBase64Url": "S1",
    "parameters": "..."
  },
  "encryptedData": {
    "ivBase64Url": "IV1",
    "ciphertextBase64Url": "..."
  }
}
```

这里保存 Salt、KDF 参数、IV 和加密结果，是为了以后能够重复派生正确的 Key 并完成解密。Password 和真正的 Key 不应直接写进这份文件。某些实现会把 AES-GCM 的 Authentication Tag 和 Ciphertext 一起编码，所以文件里不一定有单独的 `tag` 字段。

## 从一次保存缺陷理解它的边界

2026-07-28，在审查本地账本加密文件时，发现磁盘文件中的 Salt 被修改后，程序仍可能把本次操作显示成“已保存”。

这暴露的通用问题是：

```text
写入调用结束
≠
磁盘上的加密文件已经过读取和验证
```

如果程序需要承诺“已保存且文件可重新打开”，就应在显示成功前重新读取实际文件，并验证文件结构和认证解密结果。对于原有 Ciphertext 和 Authentication Tag，Salt 被替换通常会派生出错误的 Key，随后导致 AES-GCM 认证解密失败。

密码学可以帮助发现数据不匹配，但不会替应用自动完成“重新读取磁盘文件”这一步。

## 当前理解边界

这张卡只建立 Password、Salt、Key、IV 与 Ciphertext 的基础关系，暂不展开：

- PBKDF2 的内部数学过程和参数选择；
- AES-GCM 的 AAD（附加认证数据）；
- IV 重复使用的具体攻击方式；
- 密码轮换与重新加密；
- 浏览器运行期间的 Key 生命周期。

## 关联

- [[为什么 Salt 可以公开保存在加密文件中]]：从最容易产生的疑问理解 Salt 的职责。

## 参考

- [NIST SP 800-132：Password-Based Key Derivation](https://csrc.nist.gov/pubs/sp/800/132/final)
- [NIST SP 800-38D：GCM 与认证加密](https://csrc.nist.gov/pubs/sp/800/38/d/final)
- [MDN：使用 PBKDF2 派生 AES Key](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/deriveKey)
