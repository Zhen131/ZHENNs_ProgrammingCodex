---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/编程语言, 语言/JavaScript, 层级/基础]
aliases: [Node, Node.js Runtime, Node 运行环境, Node]
created: 2026-06-29
updated: 2026-06-29
---

# Node.js（Node 运行环境）

## 一句话

`Node.js（Node 运行环境）` 是让 JavaScript 可以离开浏览器，在本地电脑、服务器和命令行工具里运行的 runtime。

## 背景：它出现前的问题

JavaScript 最早主要运行在浏览器里，用来控制页面、响应点击、操作 DOM 和请求后端数据。随着 Web 工程变复杂，人们希望 JavaScript 也能做服务器、脚本、构建、测试、命令行工具等浏览器外的事情。

如果没有 Node.js，现代前端项目就很难用统一的 JavaScript/TypeScript 工具链完成开发服务器、打包、测试和自动化脚本。

## 它解决了什么

Node.js 让 JavaScript 获得了浏览器外的运行能力：

- 在终端执行 JavaScript 文件。
- 启动本地开发服务器。
- 运行前端构建工具。
- 运行测试工具。
- 编写后端 API 或命令行工具。

所以可以粗略理解为：

```text
JavaScript 是语言
Node.js 是运行 JavaScript 的环境
```

## 核心机制

Node.js 内部使用 [[V8（JavaScript 引擎）]] 执行 JavaScript，然后在 V8 外面提供文件、路径、网络、进程、环境变量、服务器等能力。

这和浏览器 runtime 的差异在于：

- 浏览器主要提供页面和 DOM 能力。
- Node.js 主要提供操作系统、文件、网络和工程工具能力。

因此 `node hello.js` 更像 `python hello.py`：代码本身只是文本，runtime 负责把代码跑起来。

## 典型使用场景

- 运行 `npm run dev` 启动前端开发服务器。
- 用 `npm test` 运行测试工具。
- 用 JavaScript/TypeScript 写服务端 API。
- 写命令行脚本或自动化工具。

## 局限性

Node.js 不是一门新语言，也不是 [[node_modules（依赖实体目录）]]。把 Node.js 和 node_modules 混在一起，会导致看项目时分不清“运行环境”和“依赖实体目录”。

## 和其他概念的关系

- [[JavaScript Runtime（JavaScript 运行时）]] 是理解 Node.js 的上位概念。
- [[npm（Node 包管理器）]] 运行在 Node.js 生态中，用来管理 package。
- [[package.json（项目清单）]] 记录 Node/JavaScript 项目的命令和依赖。
- [[node_modules（依赖实体目录）]] 是 npm 下载依赖后的本地目录，不是 Node.js 本体。

## 在项目中的表现

- [[26_06_29 账本项目 - 理解 Node.js、npm 与 node_modules]]：账本项目需要 Node.js 来运行 Next.js 开发服务器、Vitest 测试和 npm scripts。

## 关联

- [[JavaScript Runtime（JavaScript 运行时）]]
- [[V8（JavaScript 引擎）]]
- [[npm（Node 包管理器）]]
- [[为什么读 JavaScript 项目要先识别工程骨架]]
