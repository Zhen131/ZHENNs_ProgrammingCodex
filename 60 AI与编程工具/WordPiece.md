---
type: 技术卡片
status: 已整理
tags: [类型/技术卡片, 领域/AI, 层级/进阶]
aliases: [WordPiece, Word Piece]
created: 2026-09-15
updated: 2026-09-25
---

# WordPiece

## 一句话

WordPiece 是另一种 subword（子词）分词算法，思路和 [[Byte-Pair Encoding（字节对编码，BPE）]] 几乎一样（都是从字符开始逐步合并出词表），区别在于挑选"合并哪一对符号"时的打分标准不同。

## 背景：它出现前的问题

和 BPE 面对的是同一个问题：word-level 分词词表太大、覆盖不了新词，character-level 分词序列太长、语义太碎。Google 在训练 BERT 时选择了 WordPiece 作为默认分词方案。

## 它解决了什么

和 BPE 一样，用可控大小的词表覆盖尽量多的文本，减少 `[UNK]`（未知词）。WordPiece 的合并标准更偏向"这次合并能不能让语言模型的概率/似然提升更多"，而不是单纯看这对符号在语料里出现得够不够频繁。

## 核心机制

训练流程和 BPE 几乎一模一样：从字符开始，迭代合并，直到词表达到目标大小。唯一的区别是"选哪一对合并"的打分函数不同——BPE 纯看共现频率，WordPiece 用似然提升来打分。

切分结果里，不在词首的子词会带 `##` 前缀，例如 `playing` 可能被切成 `play` 和 `##ing`，表示 `##ing` 要接在前一个片段后面拼回原词。

用 `tokenizers` 库训练 WordPiece，代码结构和训练 BPE 高度相似，只是把类名换掉：

```python
from tokenizers.models import WordPiece
from tokenizers.trainers import WordPieceTrainer
from tokenizers import Tokenizer
from tokenizers.pre_tokenizers import Whitespace

tokenizer_wp = Tokenizer(WordPiece(unk_token="[UNK]"))
trainer_wp = WordPieceTrainer(
    special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"],
    vocab_size=30000,
)
tokenizer_wp.pre_tokenizer = Whitespace()
tokenizer_wp.train_from_iterator(corpus, trainer_wp)
tokenizer_wp.save("tokenizer-wp.json")
```

## 典型使用场景

- BERT、DistilBERT 等 BERT 系模型默认使用的分词方案（RoBERTa 例外，它改用了 Byte-level BPE）。

## 局限性

- 和 BPE 一样，最终切分习惯依赖训练语料的分布。
- 调用方式和 BPE 几乎一致，初学者容易忽略两者内部打分逻辑的差异，把它们当成完全一样的东西。

## 和其他概念的关系

- [[Byte-Pair Encoding（字节对编码，BPE）]]：同一类思路的另一种实现，差别在合并打分方式。
- [[Tokenization（分词）]]：WordPiece 是 subword 分词方案里的一种。
- [[Hugging Face]]：`tokenizers` 库同时提供了 BPE 和 WordPiece 的训练实现。

## 关联

- [[Byte-Pair Encoding（字节对编码，BPE）]]
- [[Tokenization（分词）]]
- [[Hugging Face]]
