---
type: 技术卡片
status: 已整理
tags: [类型/技术卡片, 领域/AI, 层级/基础]
aliases: [Token, 语言处理单位, 输入 Token, 输出 Token, Input Token, Output Token, Reasoning Token]
created: 2026-07-13
updated: 2026-07-13
---

# Token（语言处理单位）

## 一句话

Token 是模型通过 [[Tokenization（分词）]] 得到并实际处理的离散符号单位；它可以用来描述输入、输出和部分模型的内部推理用量，但不是字数、单词数或数据大小。

## 背景：为什么不能只数文字

自然语言和代码都是字符串，而模型接收的是数字 ID 序列。同一个字、单词或标点在不同 tokenizer、语言和上下文中可能被切成不同数量的 token，因此不存在稳定的“一个汉字等于一个 token”换算公式。

日常可以用 tokenizer 工具做估算，但不能把中文字符数直接当成精确账单。数量级类比（例如“一百万 token 等于一本小说”）也只适合建立粗略直觉，不能跨语言、模型和文本类型精确换算。

## 常见用量分类

- **Input Token（输入 Token）**：本次请求中提供给模型处理的内容，可能包括用户消息、系统指令、历史对话、工具结果、代码和文件内容。
- **Cached Input（缓存输入）**：输入 token 中命中 Prompt Caching（提示缓存）的部分。它仍属于输入用量，但某些 API 会以更低价格处理。
- **Output Token（输出 Token）**：模型生成的输出用量。在自回归生成中，模型逐 token 预测后续内容。
- **Reasoning Token（推理 Token）**：部分 reasoning model（推理模型）内部用于推理的 token。是否展示、如何计入输出与如何计费取决于具体模型和平台，不能笼统地说“思考一定不消耗 token”。

## Token 与费用不是同一个概念

Token 是用量单位，费用则是“各类 token 数量 × 对应费率”的结果。不同模型、服务层级和产品可能采用不同费率或额度规则，所以：

- `total_tokens` 不一定足以独立推导费用，还要看 input、cached input、output 等分类。
- Output Token 经常比 Input Token 单价高，但这是定价策略，不是 Token 定义，也不是所有产品永远不变的规律。
- ChatGPT、Codex 等订阅产品的额度规则不能直接套用 OpenAI API 的按 token 价格。

## 它能衡量什么，不能衡量什么

Token 数可以近似表示模型处理了多少符号序列，适合观察上下文规模、生成长度和 API 用量。它不能直接衡量：

- 内容占多少 KB 或 MB；
- 任务到底有多难；
- 模型进行了多少“理解”；
- Agent 完成任务的质量。

因此，把 Token 称为“AI 工作量单位”有助于建立直觉，但更准确的说法是：**Token 是模型计算与计量所围绕的序列单位，工作量和成本还受模型、缓存、推理方式及调用轮数影响。**

## 关联

- [[Tokenization（分词）]]：说明字符串怎样变成 token 序列。
- [[Context Window（上下文窗口）]]：限制一次模型调用可处理的 token 范围。
- [[为什么 Token 不能直接等同于 MB]]：区分语言序列计量与字节计量。
- [[为什么 AI Agent 比普通聊天消耗更多 Token]]：解释多轮工具工作流如何累积 token 用量。
