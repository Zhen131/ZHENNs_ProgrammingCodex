---
type: 技术卡片
status: 已整理
tags: [类型/技术卡片, 领域/AI, 层级/进阶]
aliases: [BPE, Byte Pair Encoding, 字节对编码, Byte-Pair Encoding]
created: 2026-09-15
updated: 2026-09-25
---

# Byte-Pair Encoding（字节对编码，BPE）

## 一句话

BPE 是一种 subword（子词）分词算法：从单个字符开始，反复把语料中最常相邻出现的一对符号合并成新 token，逐步"长出"一个大小可控的词表。

## 背景：它出现前的问题

[[Tokenization（分词）]] 在 word-level（按完整单词切）和 character-level（按字符切）之间有一个权衡：按单词切词表要非常大才能覆盖所有词形，碰到没见过的词只能标记为 `[UNK]`（未知词）；按字符切词表很小，但一句话会被拆成很多 token，单个字符本身也没有太多语义。BPE 就是为了在两者之间找一个可控的中间点。

名字来自它的出身：BPE 最早（1994 年）是一种数据压缩算法，反复把最常见的相邻字节对替换成一个新符号；2016 年前后被引入神经机器翻译，改造成构建子词词表的方法。

## 它解决了什么

- 词表大小可以人为设定（如 `vocab_size=30000`），不会像 word-level 那样随语料无限膨胀。
- 没见过的完整单词也能拆成"认识的子词片段"表示出来，大幅减少 `[UNK]`。
- 常见片段（词根、前后缀）会被合并成单个 token，缩短序列长度。

## 核心机制

1. 先把语料中所有文本拆成单个字符（最细粒度）。
2. 统计所有相邻"符号对"在语料中出现的频率。
3. 把频率最高的那一对合并成一个新 token，加入词表。
4. 重复第 2-3 步，直到词表达到目标大小（`vocab_size`）。

用 Hugging Face 的 `tokenizers` 库训练一个 BPE 分词器的典型骨架：

```python
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace

tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
trainer = BpeTrainer(
    special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"],
    vocab_size=30000,
)
tokenizer.pre_tokenizer = Whitespace()
tokenizer.train_from_iterator(corpus, trainer)  # corpus 是文本语料的可迭代对象
tokenizer.save("tokenizer-bpe.json")
```

训练完成后，`tokenizer.encode("句子")` 就能把任意句子切成训练好的子词 token 序列。

## 典型使用场景

- GPT 系列等大语言模型的分词方案。
- 用 [[Hugging Face]] 的 `tokenizers` 库在自己的语料上训练一个专属分词器。

## 局限性

- 合并顺序完全由语料中的频率统计决定，训练语料的分布会直接影响最终词表的切分习惯，换一批语料结果可能不同。
- 合并出的 token 是"统计上高频"，不一定是语言学意义上真正的词根或词缀。
- 以字符为起点的 BPE 仍需要 `[UNK]` 兜底训练语料里完全没见过的字符（比如一种全新的文字系统）。GPT-2 之后常用的 **Byte-level BPE** 从字节而不是字符起步，任何文本都能拆成已知字节，因此不再需要 `[UNK]`。

## 和其他概念的关系

- [[Tokenization（分词）]]：BPE 是分词方案里 subword 一类的一种具体实现。
- [[WordPiece]]：思路几乎相同（都是从字符逐步合并），区别只在于挑选"合并哪一对"时用的打分方式。
- [[Hugging Face]]：`tokenizers` 库提供了训练和使用 BPE 的现成实现。
- [[Token（语言处理单位）]]：BPE 切出的子词就是模型实际处理的 token，这也解释了为什么一个词可能对应多个 token。

## 关联

- [[Tokenization（分词）]]
- [[WordPiece]]
- [[Hugging Face]]
- [[Token（语言处理单位）]]
