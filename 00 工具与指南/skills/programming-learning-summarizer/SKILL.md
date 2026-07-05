---
name: programming-learning-summarizer
description: Summarize programming learning from another project into a vault-ready learning packet for 编程宝典. Use when the user asks to整理学习过程, summarize debugging, explain code they just learned, capture AI coding lessons, or prepare notes before importing them into the Obsidian programming knowledge base.
---

# Programming Learning Summarizer

Use this skill outside the `编程宝典` vault when Ethan learns something while working in another project.

The goal is to produce a clear learning packet that can later be imported into `编程宝典` by `programming-knowledge-ingest`.

## Workflow

1. Identify the learning context.
   - Project name
   - Feature, bug, file, command, conversation, or code path involved
   - What Ethan originally did not understand

2. Extract the real pain point.
   - What problem appeared before the technique was understood?
   - Why did the code feel like a black box?
   - What would go wrong if Ethan only copied the AI-generated answer?

3. Extract candidate cards.
   - Technology card candidates: stable concepts worth reusing.
   - Problem card candidates: questions that explain why the technology matters.
   - Project context snippets: concrete file paths, symptoms, or code observations that should be embedded inside the relevant cards.

4. Explain with Chinese logic and English terms.
   - Use Chinese for reasoning and learning reflection.
   - Keep technical terms in English.
   - First mention format: `English（中文）`.

5. Separate facts from uncertainty.
   - Do not invent conclusions.
   - Mark uncertain items as `待确认`.
   - If a claim depends on code context, cite the file path or observed behavior.

## Output Format

```markdown
# 待入库学习包：主题

## 1. 学习背景

- 项目：
- 场景：
- 当时的问题：

## 2. 核心痛点

用中文说明为什么这件事值得学习。

## 3. 我学到的关键技术

### English Term（中文翻译）

- 一句话：
- 背景问题：
- 核心机制：
- 局限性：
- 相关代码或现象：

## 4. 问题卡片候选

- `为什么需要 X`
- `X 解决了什么问题`

## 5. 技术卡片候选

- `English Term（中文翻译）`

## 6. 项目语境

- 可以写进技术卡片或问题卡片正文的项目、文件、bug、命令或代码观察。

## 7. 建议入库动作

- 新建：
- 更新：
- 暂存到 `90 素材与临时笔记`：

## 8. 待确认

- [ ] 不确定点
```

## Rules

- Do not write directly into `编程宝典` unless the user explicitly asks.
- Prefer concrete code observations over generic textbook explanations.
- Do not propose standalone aggregation notes; project context should be embedded in technical/problem cards.
- Keep the packet compact enough to import, but complete enough that another AI can perform入库 without rereading the whole project.
