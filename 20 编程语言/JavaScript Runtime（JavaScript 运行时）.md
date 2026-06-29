---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/编程语言, 语言/JavaScript, 层级/基础]
aliases: [Runtime Environment, 运行环境, JavaScript 运行环境, JS Runtime]
created: 2026-06-29
updated: 2026-06-29
---

# JavaScript Runtime（JavaScript 运行时）

## 一句话

`JavaScript Runtime（JavaScript 运行时）` 是让 JavaScript 代码真正跑起来的环境，它不仅执行语言本身，还会提供文件、页面、网络、定时器等宿主能力。

## 背景：它出现前的问题

初学项目时很容易把 `JavaScript（JavaScript 语言）`、浏览器、[[Node.js（Node 运行环境）]] 混在一起，好像只要写的是 `.js` 文件，能调用的能力就一样。

但代码运行时能做什么，不只取决于语言语法，也取决于它被放进了哪个 runtime。

## 它解决了什么

运行时这个概念帮助区分两件事：

- 语言本身：变量、函数、对象、模块等语法和语义。
- 宿主环境：浏览器提供 `window`、`document`、`DOM`，Node.js 提供文件系统、路径、环境变量、命令行、服务器等能力。

理解这层区别后，就不会把浏览器里的 JavaScript 和 Node.js 里的 JavaScript 误认为完全一样。

## 核心机制

同一门 JavaScript 语言可以运行在不同宿主环境中。

浏览器 runtime 常见能力：

- `window`
- `document`
- DOM
- 页面事件
- 浏览器本地存储

Node.js runtime 常见能力：

- 读写文件
- 处理路径
- 读取环境变量
- 启动本地服务器
- 执行命令行脚本
- 运行测试、构建和包管理工具

[[V8（JavaScript 引擎）]] 负责执行 JavaScript，runtime 则把引擎和宿主能力组合起来。

## 典型使用场景

- 理解为什么前端项目需要 Node.js 才能运行 `npm run dev`。
- 判断一段 JavaScript 代码应该在浏览器里跑，还是在 Node.js 里跑。
- 排查 `window is not defined` 或文件系统 API 不能在浏览器使用这类环境差异问题。

## 局限性

Runtime 不是业务代码，也不是 package。理解 runtime 只能说明代码在哪里跑，不能直接说明项目依赖了哪些第三方工具；依赖关系还要看 [[package.json（项目清单）]] 和 [[Dependency（依赖）]]。

## 和其他概念的关系

- [[Node.js（Node 运行环境）]] 是 JavaScript 在浏览器外运行的典型 runtime。
- [[V8（JavaScript 引擎）]] 是 Node.js 使用的 JavaScript engine。
- [[JavaScript Project Structure（JavaScript 项目结构）]] 会把 runtime、包管理、业务源码放在同一个项目根目录中。
- [[为什么读 JavaScript 项目要先识别工程骨架]] 解释了为什么不能把所有文件都当作源码读。

## 在项目中的表现

- [[26_06_29 账本项目 - 理解 Node.js、npm 与 node_modules]]：这次学习中，Ethan 把 JavaScript 语言、Node.js runtime、npm 和 node_modules 拆开理解。

## 关联

- [[Node.js（Node 运行环境）]]
- [[V8（JavaScript 引擎）]]
- [[package.json（项目清单）]]
- [[为什么读 JavaScript 项目要先识别工程骨架]]
