---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/编程语言, 语言/JavaScript, 层级/基础]
aliases: [V8, JavaScript Engine, JS 引擎, JavaScript 引擎]
created: 2026-06-29
updated: 2026-06-29
---

# V8（JavaScript 引擎）

## 一句话

`V8（JavaScript 引擎）` 是 Google Chrome 使用的 JavaScript engine，也是 [[Node.js（Node 运行环境）]] 用来执行 JavaScript 的核心引擎。

## 背景：它出现前的问题

JavaScript 代码本身不会自动运行，必须有一个 engine 负责解析和执行它。浏览器和 Node.js 都需要这样的执行核心。

## 它解决了什么

V8 负责让 JavaScript 代码真正被执行。对学习 Node.js 来说，V8 能解释一个关键点：Node.js 不是重新发明一门语言，而是在 JavaScript engine 外面提供浏览器外的宿主能力。

## 核心机制

可以把关系理解成：

```text
V8
  负责执行 JavaScript

Node.js
  使用 V8 执行 JavaScript
  再额外提供文件、网络、服务器、命令行等能力
```

所以 [[JavaScript Runtime（JavaScript 运行时）]] 通常不只是一个 engine，还包括宿主环境提供的 API。

## 典型使用场景

- 理解 Node.js 为什么能运行 JavaScript。
- 区分 JavaScript language、JavaScript engine 和 runtime。
- 学习浏览器与 Node.js 的共同点和差异。

## 局限性

V8 不是包管理器，也不负责安装依赖。项目依赖仍然由 [[npm（Node 包管理器）]]、[[package.json（项目清单）]] 和 [[node_modules（依赖实体目录）]] 管理。

## 和其他概念的关系

- [[Node.js（Node 运行环境）]] 基于 V8 执行 JavaScript。
- [[JavaScript Runtime（JavaScript 运行时）]] 包含 JavaScript engine 和宿主能力。
- [[为什么读 JavaScript 项目要先识别工程骨架]] 中的运行环境判断，离不开 language、engine、runtime 的区分。

## 关联

- [[JavaScript Runtime（JavaScript 运行时）]]
- [[Node.js（Node 运行环境）]]
