---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/软件工程, 语言/JavaScript, 层级/基础]
aliases: [npm scripts, scripts, package.json scripts, npm 脚本, 命令脚本, node_modules/.bin]
created: 2026-07-01
updated: 2026-07-01
---

# npm scripts（npm 脚本）

## 一句话

`npm scripts（npm 脚本）` 是写在 [[package.json（项目清单）]] 里的命令快捷名，像遥控器上的按钮，让开发者用 `npm run xxx` 执行项目约定好的开发、测试、构建命令。

## 背景：它出现前的问题

JavaScript 项目会用很多工具，例如 `next`、`vite`、`vitest`、`eslint`、`tsc`。如果每个人都手动记完整命令，或者直接去找工具安装在哪个目录，项目启动和协作就会变乱。

## 它解决了什么

npm scripts 把常用命令集中到 package.json：

```json
{
  "scripts": {
    "dev": "next dev",
    "test": "vitest run",
    "build": "next build"
  }
}
```

这样开发者只需要记：

```bash
npm run dev
npm test
npm run build
```

## 核心机制

可以先这样理解：

```text
scripts
= 遥控器上的按钮

node_modules/.bin
= 机器暴露出来的开关入口
```

当执行 `npm run dev` 时，[[npm（Node 包管理器）]] 会读取 package.json 的 `scripts.dev`。如果里面写的是 `next dev`，npm 会在执行脚本时把 `node_modules/.bin` 加进命令查找路径，所以本地安装在 [[node_modules（依赖实体目录）]] 里的 `next` 命令也能被找到。

换成遥控器类比：

```text
npm run dev
= 你让 npm 去按 package.json 里的 dev 按钮

"dev": "next dev"
= 按 dev 按钮时，要启动 next 这台机器，并传入 dev 模式

node_modules/.bin/next
= next 这台机器暴露出来的启动入口
```

接下来就是 [[Next.js（Next 应用框架）]] 自己开始运行，例如启动开发服务器。

## 典型使用场景

- `npm run dev`：启动开发服务器。
- `npm test`：运行测试。
- `npm run build`：构建生产版本。
- `npm run lint`：运行代码检查。

## 局限性

npm scripts 只是命令快捷入口，不是工具本体。真正的工具 package 仍然来自 [[Dependency（依赖）]] 声明，并被 npm 安装到 node_modules 中。读脚本时还要继续追问：这个命令背后调用的工具是什么，它对应哪个依赖。

## 和其他概念的关系

- [[package.json（项目清单）]] 保存 scripts 字段。
- [[npm（Node 包管理器）]] 负责读取并执行 scripts。
- [[node_modules（依赖实体目录）]] 保存本地安装的工具实体。
- [[Next.js（Next 应用框架）]] 的 `next dev` 是 npm scripts 调用本地工具的典型例子。
- [[Dependency（依赖）]] 解释这些工具为什么会被安装。
- [[为什么 package.json 是读 JavaScript 项目的入口]] 解释为什么 scripts 是读项目时的关键入口。

## 关联

- [[package.json（项目清单）]]
- [[npm（Node 包管理器）]]
- [[node_modules（依赖实体目录）]]
- [[Next.js（Next 应用框架）]]
- [[Dependency（依赖）]]
- [[为什么 package.json 是读 JavaScript 项目的入口]]
