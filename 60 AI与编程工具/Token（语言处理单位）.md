---
type: 技术卡片
status: 草稿
aliases: [Token, 词元, 语言处理单位, Input Token, Output Token, Reasoning Token, Cached Input, 输入 Token, 输出 Token]
created: 2026-07-13
updated: 2026-10-08
---

# Token（语言处理单位）

## 一句话

Token 是模型真正"看到"的最小单位。你发给模型的是一段文字，模型拿到的是一串数字 ID，每个 ID 对应一个 token。它不是字数，不是单词数，也不是文件大小——它是模型自己的计数单位。

## 背景：模型为什么不直接读字符串

你写"梯度下降"四个字，模型看不懂汉字。它只认数字。所以中间必须有一步：把字符串切成小块，每块换成一个数字。这一步叫 [[Tokenization（分词）]]，切出来的每一小块就是一个 token。

麻烦在于，怎么切是每个模型自己定的。同一句话，GPT 切出 20 个 token，Claude 可能切出 23 个。英文一个单词常常就是一个 token，中文一个字可能是一个 token，也可能一个半。所以你没法背一个"一个汉字 = 几个 token"的换算表，换个模型就不对了。

想估的话，用那个模型自带的 tokenizer 工具数一下，这是唯一靠谱的办法。

## 核心机制

账单上通常把 token 分四类，你看用量时要分开看：

- **Input Token（输入 Token）**：这次请求里送进模型的所有东西。不只是你打的那句话，还包括 system prompt、之前的对话历史、工具返回的结果、你贴的文件。Agent 用量大，大头就在这里。
- **Cached Input（缓存输入）**：输入里命中 Prompt Caching（提示缓存）的那部分。比如你连续几轮都带着同一份 10 万字的 system prompt，API 可以不重算，按低价收。它还是算输入用量，只是便宜。
- **Output Token（输出 Token）**：模型吐出来的字。模型是一个 token 一个 token 往外蹦的，所以输出越长越贵，而且一般比输入单价高。
- **Reasoning Token（推理 Token）**：推理模型在回答前"想"的那部分。有的平台给你看，有的不给看，但都要算钱。所以别以为模型想了半天不花钱。

## 容易混淆

**Token 不是钱。** Token 是用量，钱 = 各类 token 数 × 各自单价。两个模型 token 数一样，账单可能差十倍。`total_tokens` 一个数字算不出费用，得拆开看 input / cached / output。

**Token 不是 MB。** 见 [[为什么 Token 不能直接等同于 MB]]。

**Token 不是工作量。** 它只说明模型处理了多少符号，不说明任务多难、模型理解了多少。把它叫"AI 工作量单位"只是个方便的说法。

**订阅额度不是 API 价格。** ChatGPT、Codex 这类订阅产品有自己的额度规则，不能拿 OpenAI API 的 token 单价去套。

## 关联

- [[Tokenization（分词）]]：字符串怎么变成 token 串，就是这一步决定的。
- [[Context Window（上下文窗口）]]：一次调用最多能装多少 token，这就是它的上限。
- [[为什么 Token 不能直接等同于 MB]]：两种单位回答的是不同问题。
- [[为什么 AI Agent 比普通聊天消耗更多 Token]]：一句"修一下 bug"为什么能烧掉几十万 token。
