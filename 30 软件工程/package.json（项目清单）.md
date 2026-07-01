---
type: 技术卡片
status: 草稿
tags: [类型/技术卡片, 领域/软件工程, 语言/JavaScript, 层级/基础]
aliases: [package.json, 项目清单, npm manifest, 项目说明文件, 命令菜单]
created: 2026-06-29
updated: 2026-07-01
---

# package.json（项目清单）

## 一句话

`package.json（项目清单）` 是 JavaScript/TypeScript 项目的核心说明文件，记录项目元信息、命令脚本和依赖清单，可以先粗略理解成项目说明书，也可以理解成 npm 要读取的按钮面板。

## 背景：它出现前的问题

拿到一个 JavaScript 项目时，如果不知道项目怎么启动、用了哪些工具、哪些库是运行必需，直接去翻所有目录会很快迷路。特别是看到 `node_modules/` 时，初学者容易把第三方依赖也当成当前项目源码。

## 它解决了什么

package.json 给项目提供一个稳定入口：

- 项目叫什么。
- 项目版本是多少。
- 项目是否私有。
- 有哪些可运行命令。
- 运行时依赖哪些 package。
- 开发、测试、构建时依赖哪些 package。

因此它既是项目说明，也像项目的命令菜单和依赖清单。

这次可以先记一个依赖系统心智模型：

```text
package.json
= 遥控器说明书 / 按钮面板

scripts
= 遥控器上的按钮

dependencies/devDependencies
= 我要 npm 帮我安装哪些机器和零件
```

## 核心机制

常见字段包括：

```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "test": "vitest run"
  },
  "dependencies": {},
  "devDependencies": {}
}
```

`scripts` 让 [[npm（Node 包管理器）]] 可以执行统一命令，例如 `npm run dev`。它对应的稳定概念是 [[npm scripts（npm 脚本）]]。`dependencies` 和 `devDependencies` 描述 [[Dependency（依赖）]] 的不同阶段。

例如 `npm run dev` 可以理解成：让 npm 去按 package.json 里的 `dev` 按钮。npm 看到 `"dev": "next dev"` 后，会去启动本地安装的 `next` 工具，并把 `dev` 当成传给这个工具的模式参数。

## 典型使用场景

- 新接手项目时先看项目如何启动。
- 判断项目使用了哪些框架和工具。
- 区分运行时依赖和开发依赖。
- 找到测试、构建、lint 的标准命令。

## 局限性

package.json 是声明文件，不是依赖实体。真正下载到本地的 package 在 [[node_modules（依赖实体目录）]] 中；精确版本和完整依赖树在 [[package-lock.json（依赖锁文件）]] 中。

## 和其他概念的关系

- [[npm（Node 包管理器）]] 读取 package.json 执行安装和脚本。
- [[npm scripts（npm 脚本）]] 是 package.json 中 `scripts` 字段表达的命令快捷入口。
- [[Package（软件包）]] 在 package.json 中被声明为依赖。
- [[Dependency（依赖）]] 区分 `dependencies` 与 `devDependencies`。
- [[JavaScript Project Structure（JavaScript 项目结构）]] 把 package.json 视为优先阅读入口之一。

## 进一步理解

- [[Next.js（Next 应用框架）]]：`npm run dev` 常会通过 package.json 的 scripts 启动 `next dev`，这说明 package.json 不只是依赖清单，也是框架运行入口。
- [[npm scripts（npm 脚本）]]：`scripts` 不是工具本体，而是给常用命令起的项目级快捷名。
- [[package-lock.json（依赖锁文件）]]：package.json 说“我要什么机器”，lockfile 记录“实际装的是哪个精确型号”。

## 关联

- [[npm（Node 包管理器）]]
- [[npm scripts（npm 脚本）]]
- [[Dependency（依赖）]]
- [[package-lock.json（依赖锁文件）]]
- [[Next.js（Next 应用框架）]]
- [[为什么 package.json 是读 JavaScript 项目的入口]]
