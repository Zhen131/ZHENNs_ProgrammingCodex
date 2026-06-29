---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/软件工程, 语言/JavaScript, 层级/基础]
aliases: [npm, Node Package Manager, Node 包管理器, 包管理器]
created: 2026-06-29
updated: 2026-06-29
---

# npm（Node 包管理器）

## 一句话

`npm（Node Package Manager，Node 包管理器）` 是 Node 生态里的包管理器，用来安装 package、管理依赖，并执行项目脚本。

## 背景：它出现前的问题

JavaScript 项目通常依赖许多外部 package。手动下载、维护版本、处理依赖之间的依赖关系非常容易出错。项目也需要统一入口来运行开发服务器、测试和构建命令。

## 它解决了什么

npm 把依赖安装和命令执行标准化：

```bash
npm install
npm run dev
npm test
npm run build
```

这让开发者不用手工管理每一个包的文件，只需要维护 [[package.json（项目清单）]] 和锁文件。

## 核心机制

npm 主要围绕三个东西工作：

- [[package.json（项目清单）]]：记录项目脚本、依赖和元信息。
- [[package-lock.json（依赖锁文件）]]：记录精确依赖版本和完整依赖树。
- [[node_modules（依赖实体目录）]]：保存 npm 下载到本地的依赖实体。

`npm run dev` 这类命令本质上是在执行 package.json 的 `scripts` 中定义好的命令。

## 典型使用场景

- `npm install`：根据依赖清单安装 package。
- `npm run dev`：启动开发模式。
- `npm test`：运行测试命令。
- `npm run build`：构建正式版本。

## 局限性

npm 不是业务代码，也不是运行环境本身。它依赖 [[Node.js（Node 运行环境）]] 生态工作，负责管理 package 和执行 scripts。看项目时不应该把 npm、Node.js、node_modules 混成同一个概念。

## 和其他概念的关系

- [[Package（软件包）]] 是 npm 管理的基本单元。
- [[Dependency（依赖）]] 是项目和 package 之间的需要关系。
- [[package.json（项目清单）]] 是 npm 的主要入口文件。
- [[为什么 package.json 是读 JavaScript 项目的入口]] 解释了为什么工程师会先看 package.json。

## 在项目中的表现

- [[26_06_29 账本项目 - 理解 Node.js、npm 与 node_modules]]：账本项目通过 npm scripts 启动 Next.js、运行 Vitest、执行构建和检查。
- [[26_06_29 账本项目 - 建立 React 和 Next.js 的基础心智模型]]：这次学习把 `npm run dev` 理解为启动 Next.js 开发服务器的项目命令入口。

## 关联

- [[Node.js（Node 运行环境）]]
- [[Package（软件包）]]
- [[package.json（项目清单）]]
- [[node_modules（依赖实体目录）]]
- [[Next.js（Next 应用框架）]]
