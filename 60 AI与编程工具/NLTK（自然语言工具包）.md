---
type: 技术卡片
status: 已整理
tags: [类型/技术卡片, 领域/AI, 语言/Python, 层级/基础]
aliases: [NLTK, Natural Language Toolkit, 自然语言工具包]
created: 2026-09-15
updated: 2026-09-25
---

# NLTK（自然语言工具包）

## 一句话

NLTK（Natural Language Toolkit，自然语言工具包）是一个诞生于 2001 年的 Python 库，把分词、词性标注、句法分析等经典 NLP 任务打包成开箱即用的 API，长期被用作 NLP 教学和研究工具。

## 背景：它出现前的问题

早期做自然语言处理研究或教学的人，要各自实现分词、词性标注这类基础算法，缺乏一个统一、可复用的工具箱，重复造轮子的成本很高。

## 它解决了什么

把经典 NLP 任务统一成一致的 Python 接口，并附带可下载的预训练小模型（比如断句/分词用的 `punkt` 模型），不需要自己从零写规则。

## 核心机制

NLTK 本身很"轻"，很多功能依赖额外下载的数据包。典型用法：

```python
import nltk
nltk.download('punkt')       # 下载分词用的 punkt 模型
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize
word_tokenize("Good muffins cost $3.88\nin New York.")
```

`word_tokenize` 依赖 `punkt` 模型识别标点、缩写等规则，比单纯按空格 `split()` 更聪明（比如能正确处理 `$3.88`、`Mr. Smith` 里的句号不代表句子结束）。它属于基于规则和统计的传统方法，不是 [[Deep Learning（深度学习）]] 模型。

## 典型使用场景

- NLP 课程教学、demo，用来演示"词级分词"等经典任务长什么样。
- 快速搭建传统 NLP 任务的原型（词性标注、句法分析、情感分析等）。

## 局限性

- 不是为深度学习 / 大模型场景设计的，速度和覆盖度都不如现代分词库。
- 不直接支持训练给 Transformer 类模型用的 subword（子词）分词器，这部分现在通常交给 [[Hugging Face]] 的 `tokenizers` 库来做。

## 和其他概念的关系

- [[Hugging Face]]：现代深度学习时代的对照——NLTK 偏传统规则/统计方法，Hugging Face 生态偏子词分词 + 预训练模型。
- [[Tokenization（分词）]]：`word_tokenize` 是 word-level 分词的一种具体实现。
- [[N-Gram（N元语法）]]：NLTK 提供 `nltk.util.ngrams` 等工具，常和词级分词配合做 N-Gram 统计，同属传统统计式 NLP。

## 关联

- [[Hugging Face]]
- [[Tokenization（分词）]]
- [[N-Gram（N元语法）]]
