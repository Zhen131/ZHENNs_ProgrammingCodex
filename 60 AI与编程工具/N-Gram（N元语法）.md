---
type: 技术卡片
status: 已整理
tags: [类型/技术卡片, 领域/AI, 层级/基础]
aliases: [N-Gram, N元语法, Bigram, Trigram, 二元组, 三元组]
created: 2026-09-15
updated: 2026-09-25
---

# N-Gram（N元语法）

## 一句话

N-Gram（N元语法）是把文本中连续 N 个 token（通常是词）当作一个统计单位，用来观察"哪些词组合经常一起出现"，是 Transformer 出现之前，统计语言模型预测下一个词的基础思路。

## 背景：它出现前的问题

早期要让机器"猜下一个词"，还没有 [[Deep Learning（深度学习）]] 这种用神经网络端到端学习的方式，只能靠统计词语共现的频率来估算概率——看到前面几个词，猜下一个词最可能是什么。

## 它解决了什么

把"预测下一个词"简化成"看前面 N-1 个词，统计历史语料里最常接的是哪个词"，是一种简单、可解释的统计语言建模方法。

## 核心机制

以 Bigram（N=2）为例：

```python
def generate_ngrams(text, n):
    words = text.split()
    return [tuple(words[i:i+n]) for i in range(len(words) - n + 1)]

generate_ngrams("This is the first sentence.", 2)
# [('This', 'is'), ('is', 'the'), ('the', 'first'), ('first', 'sentence.')]
```

统计一批句子里最常见的 N-Gram 组合，可以用 `collections.Counter`：

```python
from collections import Counter
counts = Counter(all_bigrams)
counts.most_common(5)
```

## 典型使用场景

- 早期统计语言模型，用共现频率预测下一个词。
- 简单的自动补全、拼写建议。
- 文本相似度比较、轻量级特征工程。

## 局限性

- 只能捕捉"局部、固定窗口"内的词语关系，看不到更远距离的语义依赖。
- N 越大，需要的语料和存储成本越高（组合数量呈指数增长，容易出现数据稀疏问题）。
- 已先后被神经网络语言模型（RNN，之后是 Transformer）这类能建模长距离依赖的方法取代为主流，现在更多作为教学案例或轻量级特征工程手段存在。

## 和其他概念的关系

- [[Tokenization（分词）]]：N-Gram 统计的基本单位是分词之后得到的 token/词。
- [[NLTK（自然语言工具包）]]：提供现成的 N-Gram 生成工具，是做传统统计式 NLP 实验的常用库。
- [[Deep Learning（深度学习）]]：取代 N-Gram 的神经网络语言模型，能看到固定窗口之外的长距离依赖。
- [[Unsupervised Learning（无监督学习）]]：N-Gram 和 LLM 预训练的目标其实一样——从无标注文本里"预测下一个词"；前者靠计数统计，后者靠神经网络（自监督学习）。

## 关联

- [[Tokenization（分词）]]
- [[NLTK（自然语言工具包）]]
- [[Deep Learning（深度学习）]]
- [[Unsupervised Learning（无监督学习）]]
